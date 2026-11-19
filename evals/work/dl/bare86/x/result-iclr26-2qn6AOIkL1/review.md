# Review: BadMoE: Backdooring Mixture-of-Experts LLMs via Optimizing Routing Triggers and Infecting Dormant Experts

(Figures were not available; figure-dependent claims are judged from captions and text only.)

## Summary
The paper proposes BadMoE, which it describes as the first backdoor attack designed for MoE LLMs. The attack has three stages:
1. **Probing.** Find the least-used ("dormant") experts at one chosen MoE layer from routing statistics on clean task data.
2. **Trigger optimization.** Run a GCG-style discrete search for a short (2-token) trigger. A routing-aware cross-entropy loss pushes the router at that layer toward a binary target vector over the dormant experts, with a perplexity regularizer on the trigger.
3. **Infection.** Fine-tune the dormant experts, plus non-expert parameters, on a data-poisoned set built with the optimized trigger.

Section 5 gives a "proof" that "dominating experts" exist, using a Gaussian/KL argument. Experiments cover three MoE LLMs (Mixtral-8x7B, OLMoE-1B-7B, DeepSeek-MoE-16B), four classification tasks and two generation tasks (refusal target). Four dense-model backdoor baselines are compared (BadNet, LWP, RIPPLe, InSent). The reported ASR is mostly above 95%, against much lower ASR for baselines on several tasks. The paper also reports ablations, transfer across domains and prompt formats, and robustness to ONION, fine-pruning and fine-tuning. It ends with a hidden-state clustering "defense" analysis.

## Strengths
- The topic is timely. MoE LLMs are widely deployed, and a router-aware attack surface is a natural thing to study.
- The pipeline is concrete and reproducible in principle. It combines a routing-targeted GCG-style trigger search with a perplexity term, and selects experts by usage.
- The evaluation covers three architecturally different MoE models (coarse-grained, fine-grained, shared experts), six datasets and both classification and generation. The ablations (probing, trigger optimization, number of experts, layer, poisoning rate, trigger length) are useful.
- The "BadFFN" comparison (poisoning all experts in the layer) is a sensible sanity check. The utility, stealth (PPL, similarity, grammar errors) and expert-usage analyses are broader than usual for an attack paper.
- The attack achieves high ASR at a 1% poisoning rate, and the results appear fairly consistent across models.

## Weaknesses

1. **The theoretical result does not support the claim.**
   - Section 5 "rigorously proves" the existence of dominating experts. The argument is a Gaussian toy model with a single-vector linear expert, K=2, and the limit ‖w1‖→∞.
   - Taking one expert's weight norm to infinity trivially makes it dominate the sum. This says nothing about trained MoE LLMs, whose expert weights are bounded and where SwiGLU FFNs are nonlinear. It also says nothing about dormant experts, whose router scores are small by definition.
   - The Gaussian assumption on hidden states is justified by a citation to a KV-cache blog notebook.
   - The KL expression in Eq. (9) appears inconsistent. The mean term uses only α2·w2ᵀμ, and the variance ratio is mishandled when w1 is unbounded. Definition 1 ("for ∀ε>0") is not a meaningful property of a given expert.
   - The "extension to more experts" is a one-sentence claim.
   - Nothing connects this result to the actual mechanism, which is that fine-tuning moves the dormant experts' weights. Calling it a "theoretical foundation" is an overstatement.

2. **Implementation is inconsistent with the method, and the baselines are not comparable.**
   - The implementation details say LoRA is applied to the attention layers (non-expert parameters), and that this "intentionally avoids modifying router and expert parameters." Yet Section 6.3 says the parameters of the dormant experts (θe) are updated, together with the non-expert parameters θ0.
   - It is therefore unclear what is trained. Is it LoRA on attention only, or the full dormant experts, with or without LoRA? If experts are additionally tuned for BadMoE but not for the baselines, the baselines get fewer trainable parameters and a non-optimized trigger.
   - The ablation "w/o Expert Probing" (random experts) retains 99.4% and 98.6% ASR. "w/o Trigger Optimizing" with "tq" retains 96% and 89%. This means the dormant-expert selection, the headline idea, adds about 1 point of ASR in the one ablation reported. The claim that gains come from "novel architectural design" is not demonstrated.
   - The missing control is a baseline given identical trainable parameters at the same layer, once with a non-routing-optimized trigger and once with a comparably optimized trigger for a dense model (e.g., a GCG-optimized trigger plus the same fine-tuning). BadFFN is the only attempt, and it uses a different trigger ("tq") and a different setting.
   - Baseline numbers also look poorly tuned. Samsum ASR is about 0 for all baselines (0.00–3.25%) on Mixtral and OLMoE, and IMDB ASR is about 50% (chance for a binary task with a "Positive" target) for nearly all baselines. This suggests implementation or training failures (e.g., trigger lost in long text, a single trigger insertion, 1% poisoning, LoRA on attention only). The "superior" comparison is then largely against broken baselines. Results are also reported from a single run, with no variance or seeds.

3. **No direct evidence that the mechanism operates.**
   - The paper never reports, for triggered inputs, how often the dormant experts are actually in the top-K after infection. It also never reports whether the optimized trigger routes to them before fine-tuning.
   - It never tests whether the optimized trigger works at other layers. Only one layer is attacked, and the router-level effect of a single trigger token is unverified in deeper layers, where token identity is mixed with context.
   - The t-SNE plots (Fig. 8) are qualitative and hard to interpret, and show the final-token hidden state of one layer. Claims about "strong control exerted by poisoned experts" are inferred from this, not measured. For example, expert ablation at inference (zeroing the dormant experts) is not used to check whether ASR collapses.
   - The claim that routing is token-ID dependent and hence triggers are "query-independent" is borrowed from other papers and not verified here. The trigger is placed at random positions, but nothing is shown on positional or context sensitivity.

4. **The utility evaluation is weak.**
   - Table 2 "clean" is the untuned base model, so "CA improves over clean" is uninformative. It reflects task fine-tuning, not stealth. The relevant comparison is a clean fine-tuned model (provided only for AGNews in Table 3).
   - The side-effect evaluation (Table 4) shows substantial degradation on unrelated tasks. Amazon accuracy drops from 66.0 to 55.7 on OLMoE (and by more for the baselines), and the paper explains the gain on Samsum with a speculative story. No standard benchmarks (MMLU, etc.) are used.
   - The stealthiness claims rely on a single-layer expert usage analysis. The measure (positive router score, Eq. 10) cannot detect that a dormant expert has been modified.

5. **Defense evaluation is limited and partly self-undermining.**
   - Only ONION, fine-pruning and fine-tuning on the full clean dataset are used. There are no MoE-specific defenses (router-statistics anomaly checks, expert weight diffing, expert pruning/merging) and no trigger-inversion or model-scanning defenses (e.g., NC-style, activation clustering).
   - ONION is designed for rare-word triggers, and the optimized trigger has a perplexity constraint, so its resistance is expected.
   - The claimed resistance to fine-tuning relies on the experts being untouched when fine-tuning on the clean task. It is not shown for fine-tuning on a different task or with different hyperparameters, and fine-tuning that includes the router or experts is not studied. Defenses that exploit dormant experts specifically (e.g., pruning or re-initializing low-usage experts) are not considered. The "attack remains >80%" claim in the abstract is only for a subset of settings (ONION on AGNews is 80.88%).
   - The proposed hidden-state separability defense is only evaluated on one model (Deepseek) and one dataset.

6. **Stealthiness of the trigger is overstated.**
   - Table 6 reports sentence perplexities of 934 (SST2) and 507 (AGNews) for poisoned inputs, which are very high. These are close to the BadNet rare-word values and far from natural text. The text claims "a better overall balance", but BadMoE's PPL is higher than InSent's on both datasets, and its GE is comparable.
   - The perplexity target is the average over the task, yet the reported PPLs are in the hundreds to thousands.
   - The trigger is a two-token, GPT-2-perplexity-regularized string. Whether it is "natural" to human reviewers or detection tools is not evaluated, and the trigger text is not shown.

7. **Scope and realism.**
   - The threat model assumes the attacker releases a fine-tuned model advertised for a specific task, which is the same setting as conventional dense backdoors. An attacker with weight access and training freedom does not need routing-based triggers.
   - The motivation that "dormant" experts give stealth is not tested against an adaptive defender. The attack is on one layer, task-specific, and with simple targets (label flip, refusal). No analysis is given for instruction-tuned, chat or reasoning MoE models, or for larger-scale MoEs. All three models are base models, and the effect may not transfer to post-trained MoEs.
   - The robustness to prompt format claim (Table 5) is only partial. For AGNews with the "Prompt" format, ASR drops by 25 points.

8. **Presentation.**
   - The paper is in an ACM template with "Conference'17" and "Trovato et al." headers, and has typos ("bone" for bold, "Tirgger", "Standford"). Several citations are misattributed. GPT-2 is cited as [5], which is the GPT-4 report, and as [53]. The Gaussian claim cites a notebook.
   - The statement that data and code will be released only upon acceptance means the work cannot currently be reproduced. Many key details are in appendices.
   - The "first backdoor attack against MoE LLMs" claim should be checked against concurrent work on MoE routing/expert-level attacks.

## Questions for the authors
1. What exactly is trained in stage 3: LoRA on attention only, full dormant experts, or both? Do all baselines train the same set of parameters at the same layer? Please report parameter counts.
2. After infection, what fraction of triggered tokens/inputs route to the dormant experts, and what fraction of clean tokens do? What happens to ASR if you ablate (zero out) the infected experts at inference or swap in the original weights?
3. Can you add a control that uses the same optimized trigger, with the same training budget, on random experts or on all dense-equivalent FFNs? The current ablation suggests that expert probing adds about 1 point of ASR.
4. Why are baseline ASRs about 50% on IMDB and about 0% on Samsum? Were they tuned (poison rate, epochs, trigger position, multiple insertions)? Please report variance across seeds.
5. How does the formal result (unbounded ‖w1‖) relate to trained experts with bounded weights? Can you give a statement or empirical measurement of dominance (e.g., the contribution of the infected experts to the layer output norm under the trigger)?
6. Can you evaluate against defenses that target the MoE structure (low-usage expert pruning or re-initialization, router regularization, expert-weight diffing)? Also against standard model-level scanners?
7. Does the attack work on instruction-tuned MoE models and on more than one layer? Does it hold up after standard downstream fine-tuning of all parameters including experts?
8. Please show the optimized triggers and explain why the reported poisoned-input PPL values (hundreds to thousands) are consistent with the stated perplexity target.

## Ratings
- **Soundness:** 2/4. The theoretical claim is weak, the baselines are not parameter-matched, the single-run results have no variance, and the mechanism is not directly verified.
- **Presentation:** 2/4. The paper is mostly readable but has several inconsistencies (method vs. implementation), citation errors and template remnants.
- **Contribution:** 2/4. The topic is novel and relevant, but the gain attributable to the MoE-specific design is small in the ablations, and the practical threat beyond standard backdoors is not established.

**Rating: 4** (marginally below the acceptance threshold)

**Confidence: 4**
