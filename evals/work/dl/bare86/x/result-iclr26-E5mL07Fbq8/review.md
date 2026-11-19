# Review: Semantic Energy: Detecting LLM Hallucination Beyond Entropy

(Figures were not available; Fig. 1–3 are judged from captions and text only.)

## Summary
The paper argues that semantic entropy (SE) cannot flag hallucinations when all sampled answers fall into one semantic cluster, because SE is then exactly zero. This happens often, and nearly half of those answers are wrong on some datasets. The authors propose "Semantic Energy". It replaces the softmax-probability-based cluster mass with a score built from raw logits: the negative selected-token logit, averaged over tokens and aggregated over each semantic cluster. The justification is an analogy to the Boltzmann distribution and to energy-based OOD detection. Experiments use Qwen3-8B and ERNIE-4.5-21B-A3B on CSQA (Chinese SimpleQA) and TriviaQA. The only baseline is SE. Reported AUROC gains are 2.8–5.9 points over SE overall (Table 1). On the subset where SE is constant (single cluster), AUROC is 58.9–66.7 for energy versus 50 for SE (Table 2). The paper also reports a think-mode experiment and an ablation on semantic clustering (Fig. 3).

## Strengths
- The failure mode is real and clearly illustrated: "confidently wrong" consistent answers give SE = 0. Studying this regime is sensible and practically relevant.
- The idea is simple and cheap. It needs no extra forward passes beyond those already used for SE, and logit access is the only extra requirement.
- The paper is candid in the conclusion that logits are not strictly energies, because cross-entropy is invariant to logit shift and scale.
- Table 1 gains are positive on all 4 model/dataset pairs and on all three metrics. Table 2 shows that the signal in the single-cluster regime is above chance.
- Code and intermediate data are promised.

## Weaknesses
1. **The baselines are inadequate, so the central claim ("beyond entropy") is not established.** The only comparison is SE. The paper does not compare against:
   - simple single-sample or logit-based scores: sequence log-likelihood, length-normalized NLL, mean/min token probability, max-logit, or token-level entropy (Eqs. 2–4, which are defined but never evaluated);
   - discrete SE or other consistency/sample-count baselines;
   - verbalized confidence, P(True), or semantic-entropy probes;
   - other recent UQ methods such as LogTokU, which is cited and is the closest prior work.

   The natural question is whether the gain comes from energy specifically or from using any magnitude- or likelihood-based signal. Since Table 2 compares against a constant (AUROC exactly 50), nearly any non-degenerate score beats it.
2. **The headline "13% improvement in cases where SE is confident" is an uninformative comparison.** In Table 2 SE is identically zero, so it is chance by construction. The paper itself says this. Presenting "≥13% AUROC improvement" as a contribution (Intro, Sec. 4.3.1) is misleading. A meaningful comparison would use a competent likelihood-based score on the same subset. The same applies to AUPR/FPR95, where SE's numbers just reflect base rate.
3. **The theory is weak and partly incoherent.**
   - The Boltzmann derivation assumes Z_t is constant across t and across contexts. This is exactly what softmax does not guarantee, and it is the quantity the method claims to exploit. The justification for ignoring Z is circular.
   - Eqs. 13–16 (a Bayesian marginalization over θ, then an approximation by a subset-vocabulary conditional) are not used in the final estimator and do not give a derivation of Eq. 19.
   - The claim that the method captures epistemic uncertainty is asserted and never tested. There is no experiment separating epistemic from aleatoric uncertainty, for example with an unknown-entity probe or a training-frequency analysis.
   - Softmax is shift-invariant, so raw logit magnitude is not well-defined as "energy". The paper concedes this in the conclusion, which undermines the framing in the title and abstract. The abstract also says "logits of penultimate layer", but logits are the output of the final layer. The terminology is confused.
4. **The estimator is ill-specified and inconsistent.**
   - Eq. 12 sums energy over cluster members. Eq. 18 divides by n. Eq. 19 uses 1/(nT_i) and sums over x^(i) in C_k, with T_i inside the sum. It is unclear how a per-response or per-question uncertainty is produced from cluster energies (selected cluster? majority cluster? min over clusters?).
   - If cluster energy is a sum over members, larger clusters get a more negative sum and so a lower "uncertainty". The score then partly encodes cluster size or consistency rather than logit magnitude. No ablation separates the two effects.
   - How the score behaves when K>1 is never explained. Fig. 1 suggests a per-cluster score, but evaluation needs a single scalar per question.
5. **The experimental protocol is under-specified.** The following are missing: the number of samples n, sampling temperature and top-p, the clustering method (NLI model? LLM judge?), and how correctness is labeled (exact match or an LLM judge, and which one). There are no seeds, confidence intervals, or significance tests. Gains of 3–6 AUROC with a single run are hard to interpret. The AUPR convention (positive class = correct) is unstated. Table 1 and Fig. 3 label the Chinese dataset differently ("CSQA" vs "CSimpleQA"), and the main-text names should be reconciled. The same numbers appear in Fig. 3 (74.8, 76.1), so the "with semantic" ablation is the same configuration as Table 1.
6. **Narrow scope.** There are two datasets of short-form factoid QA, and two ~8–21B models, one from the authors' own company. No larger models, no other families (Llama, Gemma, GPT-style APIs that expose only top-k logprobs), no long-form generation, no reasoning/math tasks (despite motivating applications in CoT), and no other benchmarks (NQ, SciQ, SQuAD, BioASQ as in the SE literature). It is unclear whether the effect generalizes across model families, since logit scales differ substantially across architectures, training recipes, and quantization. The think-mode result (Fig. 2) is only said to be "consistent" and is not quantified in the text.
7. **The semantic-clustering ablation (Sec. 4.3.3, Fig. 3) is thin.** The comparison is shown only via density plots and one AUROC per panel (69.1 vs 74.8; 63.0 vs 76.1). The "without semantic" variant is single-response energy. It is unclear whether the difference comes from semantic grouping or merely from averaging over n samples (an ensembling effect). A control with unclustered averaging over the n samples is needed.
8. **Failure modes and limitations are not analyzed.** Energy is high-confidence for responses with large-magnitude logits regardless of correctness. Models that are overconfident or fine-tuned (RLHF, distillation) may have uninformative logit magnitudes. There is no calibration analysis (ECE, selective-prediction curves, risk–coverage) despite the claim of "better calibration" in Sec. 4.2. AUROC/AUPR/FPR95 do not measure calibration. There is also no error analysis of the single-cluster wrong-answer cases, and no ablations on n, temperature, or length normalization.
9. **Writing and presentation.** There are many unclear or overstated statements: "approaches 50% in some datasets" has no table or evidence, "accounts for a large proportion" has no quantification, "calibration" is claimed without a calibration metric, and the "free energy density" claim is not substantiated. Several typos and grammar issues are present ("In of physics", "partial function" for partition function, "where n are the sampling times... and a lower energy" is a dangling sentence). Related work is a list of citations without positioning against the closest methods.

## Questions
1. How exactly is a scalar uncertainty obtained per question when K>1 clusters exist? Is Eq. 19 a sum over members, and does cluster size drive the score?
2. How does Semantic Energy compare with (a) mean/min token log-likelihood, (b) max-logit, (c) LogTokU, (d) discrete SE, (e) verbalized confidence, and (f) a simple combination of SE with sequence NLL, at both the full-data and single-cluster levels?
3. What fraction of questions fall in the single-cluster regime in each dataset/model, and what is the accuracy there? What is the overall AUROC if SE is combined with energy as a tie-breaker?
4. What are the sample count, temperature, clustering method, and correctness judge? Can you report variance over seeds and bootstrap CIs?
5. Is the signal a property of logit magnitude, or of averaging over samples? Please ablate unclustered multi-sample average energy.
6. Does the method hold on other model families and sizes, on long-form or reasoning tasks, and on other QA benchmarks? Are results sensitive to logit-scale differences (e.g., after temperature scaling or fine-tuning)?
7. Can you provide direct evidence that energy captures epistemic rather than aleatoric uncertainty (e.g., questions about entities with controlled pre-training frequency)?

## Scores
- Soundness: 2
- Presentation: 2
- Contribution: 2

## Rating: 4 (marginally below the acceptance threshold)
The motivating failure case is real and the method is cheap and sensible, but it is a small variation (swap softmax probability for logit magnitude within SE). The theory does not support the "energy" framing. The evaluation compares against a single baseline, on two datasets and two models, with the headline gain measured against a degenerate constant score. Without stronger baselines, a clear estimator definition, and broader and statistically rigorous evidence, the claims are not adequately supported.

## Confidence: 4
