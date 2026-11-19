# Review: Forget to Know, Remember to Use: Context-Aware Unlearning for LLMs

(Figures were not available; figure-dependent claims are judged from captions and text.)

## Summary
The paper observes that standard LLM unlearning methods (GradAscent, GradDiff, DPO, NPO, RMU, UNDIAL) evaluated on TOFU degrade "contextual utility". This is the model's ability to answer a forget-set question when the ground-truth answer is placed in the prompt. The authors add a plug-in term to the unlearning loss: a KL divergence between the unlearning model and the frozen original model on (question + gold context) prompts built from the forget set. Applied to NPO, RMU and UNDIAL on Gemma-2B-IT and Qwen3-8B, it raises Contextual QA LLM-Judge scores to about 0.95–0.99. The authors report Direct QA (forgetting) and model utility as largely unchanged. Supporting material includes forget-ratio ablations, a λc ablation and small qualitative studies.

## Strengths
- The question is practically relevant. Unlearned models are deployed with RAG or user-supplied context, and "forget but still read" is a reasonable desideratum. The finding that RMU, GradAscent and GradDiff collapse on in-context QA is a concrete and useful observation.
- The method is simple and plugs into several base methods. The effect is large and consistent across two models and three base methods.
- Both vanilla and context-aware variants are reported, with per-epoch curves and a λc sweep.
- The paper is clearly written.

## Weaknesses
1. **The fix trains on the evaluation distribution.** The context term is a KL to the original model on exactly the forget-set questions paired with their gold answers in context. Contextual QA is then measured on those same questions and contexts. This is train-on-test for the contextual metric, and nothing shows generalization. Missing evaluations:
   - different questions about the same forgotten facts;
   - other context forms (paraphrased, partial, long, multi-document, noisy RAG retrieval);
   - held-out forget examples not used in the context term.

   The only robustness evidence (Sec. 6.2, Table 4) is one hand-picked example with manual paraphrases. That is anecdotal.

2. **Forgetting may be undermined, and this is not tested.** The context term trains on forget-set facts with an anchor to the original model, which knows them. Plausibly this re-injects the knowledge into the weights, or teaches a general "copy the answer from context" behaviour. The paper cites work (Hu et al., Cooper et al., Shumailov et al.) showing that unlearning often only suppresses knowledge. It does not test whether forgetting survives under stronger probes: paraphrased or multiple-choice queries, partial context, related-fact prompts, relearning or jailbreak attacks. The only forgetting evidence is Direct QA with fixed prompts.

3. **The "no cost" claim is overstated and forgetting metrics are weak.**
   - Direct QA shifts are called marginal, but RMU on Gemma goes from 0.04 to 0.13 ROUGE-L and NPO from 0.19 to 0.25 LLM-Judge. These are in the wrong direction. λc selection explicitly allows δ = 0.06 slack in Direct LLM-Judge.
   - Standard TOFU Forget Quality, truth ratio and probability metrics are dropped. There is no comparison to a retain-only model on Direct QA beyond a brief remark.
   - Utility is the TOFU aggregate only. There is no general-capability benchmark, which matters for a regularizer anchored to the original model.

4. **Hyperparameters and checkpoints are selected on the evaluation metrics.** λc is chosen per method and model (0.01 to 2.0) by grid search on the same evaluation data. The reported epoch is the "earliest epoch at which it has converged" relative to the global best of the same run, which is oracle selection. There is no validation split and there are no seeds or variance. The "insensitive to λc" claim rests on Gemma curves only, and the chosen values differ by two orders of magnitude across methods.

5. **Baselines are limited.** The only comparison is vanilla versus vanilla plus the KL term. Obvious alternatives are missing:
   - cross-entropy or SFT on gold-context prompts;
   - contextual prompts added to the retain set;
   - a KL-versus-CE ablation;
   - prompt-only approaches.

   The method is effectively data augmentation with a distillation loss, and this is not compared against the simpler versions. Only three of six methods receive the fix.

6. **Scope and realism.** All evidence is from TOFU, which is synthetic, single-hop and fine-tuned on fictitious facts. Transfer to pre-trained knowledge (WMDP, MUSE), larger models, or long multi-fact contexts is not shown. The motivating examples (outdated regulations, historical comparison) differ substantially from the evaluation. The target "near original level" is also questionable. A retrain-on-retain model is the gold standard for forgetting, and its contextual QA behaviour is not reported.

7. **Metric and judging issues.**
   - LLM-Judge is binary, uses Claude 3.5 Sonnet, and is not validated against humans.
   - For Qwen, Contextual ROUGE-L is about 0.63–0.68 while LLM-Judge is about 0.97, which suggests lenient judging when the answer is in the prompt.
   - The qualitative examples are single instances.
   - The vanilla RMU/GradAscent outputs are gibberish, which suggests general collapse on forget-related text rather than selective suppression of context use. The mechanistic claim that suppression "ripples through the representation space" (Sec. 4.1, A.3) is asserted, not measured.

8. **Possible over-training.** For several vanilla methods the contextual failure may reflect over-trained or unstable runs. Headline numbers come from selected epochs, and no comparison to early-stopped or lower-learning-rate baselines is given.

9. **Modest novelty.** The technical contribution is a KL regularizer to the original model on extra prompts. It is close to existing retain-set KL terms and standard distillation. The main value is the problem framing and the protocol, which is simple.

## Questions
1. Does the gain transfer to held-out questions and contexts about forgotten entities not seen by the context term, and to paraphrased or noisy retrieved contexts at scale?
2. How does Direct QA fare under stronger probes (paraphrase, multiple choice, partial context, relearning attacks) before and after adding the term? Is knowledge re-injected?
3. How do CE/SFT on gold-context prompts, and adding contextual prompts to the retain set, compare with the KL term?
4. Can you report TOFU Forget Quality, truth ratio and probability metrics, plus general-capability benchmarks?
5. How were λc and checkpoints chosen without a held-out split? Please report multiple seeds and fixed stopping epochs.
6. What happens when the context contains a wrong or contradicting fact about forgotten content? Does the model trust any context uncritically?
7. Does the approach work for pre-trained knowledge (WMDP, MUSE) and with larger models?
8. What does a retain-only model achieve on Contextual QA?

## Scores
- Soundness: 2
- Presentation: 3
- Contribution: 2
- Rating: 4
- Confidence: 4

Rationale: The problem is real and the observation is useful. But the proposed fix is trained on the evaluated examples, comparisons to simple baselines are missing, forgetting is evaluated shallowly, and selection is oracle-like. The scope is a single synthetic benchmark. This falls below the acceptance bar as it stands.
