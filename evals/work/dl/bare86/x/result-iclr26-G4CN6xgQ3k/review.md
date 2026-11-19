# Review: Failure Modes of Maximum Entropy RLHF (ICLR 2026)

Figures were not available. I judged them from captions, legends and text only.

## Summary
The paper makes two claims.

1. **Theory.** SimPO is "derived" as Maximum Entropy RL. The derivation applies the DPO-style reparameterisation to the optimal policy of an entropy-regularised bandit objective, π ∝ exp(r/α). It then sets α = β/|y| and adds a target margin γ.
2. **Experiments.** The authors run online RLOO on TL;DR with Pythia-1B and 2.8B. They compare a KL-penalised reward (Eq. 17) against a length-normalised entropy bonus (Eq. 18).
   - Max-entropy runs "consistently" overoptimise or show growing KL drift, even at very small learning rates.
   - Entropy is described as correlating with, and possibly causing, reward hacking.
   - A short "minimum entropy" variant is reported only in prose.
   - A discussion of why SimPO works offline attributes it to dataset constraints and margins.

## Strengths
- The question is reasonable: does the reference-free, entropy-based view carry over to online RLHF?
- Negative results about regularisers are useful when they are well controlled.
- Several diagnostics are reported (KL to reference, consecutive-policy KL, PPO clipping, a reduced clip ε). The paper is honest that entropy coefficient 0 performs about as well as the working runs.
- It is clearly written, and the scope is acknowledged to be modest.

## Weaknesses
1. **The theoretical contribution is largely a relabelling and is not correct as stated.**
   - Eq. 12 writes r = α log π + α log Z. Substituting this into Bradley–Terry makes *any* policy "optimal" for some reward. This is the same trivial step as in DPO, but DPO's reference ratio gives the KL structure real content. Here the claim reduces to "a log-likelihood-difference reward is a reward".
   - The cancellation of Z(x) requires α to be constant across y1 and y2. Setting α = β/|y| makes the temperature response-dependent. Then π_r(y|x) ∝ exp(|y| r/β) has a different normaliser, and it is not the solution of Eq. 10 for any single α.
   - The leap from Eq. 15 to Eq. 16 is therefore not a derivation. Eq. 15 has α log π*(y1) − α log π*(y2), while Eq. 16 has (β/|y1|) log π(y1) − (β/|y2|) log π(y2). The "adaptive temperature" is not a temperature of any MaxEnt objective the paper defines.
   - The margin γ is added by analogy to ΨPO, not derived.
   - The statement that SimPO "inherits analogous guarantees" from DPO is deferred to an appendix that mostly restates DPO's lemmas. These are not checked for the length-normalised case. Length normalisation breaks the equivalence-class argument.
   - Liu et al. (2024) already made the MaxEnt observation, and the incremental theory is thin.
2. **The online experiment does not test the object the theory describes.**
   - SimPO is an offline, supervised loss on fixed pairs. Eq. 18 is an online per-sample entropy bonus (−β/|y| log π) added to a learned reward model.
   - The "asymmetry" between offline success and online failure compares different algorithms, data regimes and reward sources. It does not compare one objective in two settings.
   - The conclusion that "reference-free approaches face fundamental limitations in online training" is not supported. No SimPO or online SimPO-style baseline is run, and no unregularised RL baseline appears in the main comparisons.
3. **Confounded and under-controlled comparisons.**
   - KL-constrained runs use different learning rates and coefficients from the MaxEnt runs. For 2.8B, that is LR=3e-6 with β=0.2, against 5e-8 with a bonus of 0.01.
   - There is a large LR gap between "well-behaved" KL runs and the failing MaxEnt runs. The claim that KL is more robust is not tested by a matched sweep.
   - The paper admits KL regularisation is highly sensitive to β, and that one coefficient change flips the outcome. This weakens the "KL is stable, MaxEnt is not" narrative.
   - Hyperparameters were reportedly tuned by "simple grid search" for the entropy coefficient only.
   - I see no seeds, error bars or confidence intervals. Win rates of 0.3–2% against reference summaries, and 18–20% for 2.8B, come from single runs judged by GPT-4o-mini. These are collapsed models whose outputs likely look degenerate.
   - Several results are text-only, with no data shown. This includes the minimum-entropy results, the "quadratic clipping behaviour", and the ε=1e-4 runs.
4. **Causal claims are unsupported.**
   - "Entropy actually exacerbates reward hacking" is inferred from the fact that overoptimised runs have rising entropy. When a policy degenerates (long, repetitive or noisy outputs), its sequence entropy rises mechanically. Rising entropy is a symptom, not evidence of a cause.
   - With a positive entropy bonus, the incentive is to spread probability mass. An ablation separating reward hacking from the bonus (coefficient 0 at the same LR for 2.8B, which should be shown) is needed.
   - The 1B coefficient-0 result is only mentioned in text.
   - At LR 1e-6 even coefficient 0.01 overoptimises, which the authors themselves call "unsurprising". A plain RL baseline at the same LRs is the right control, and the effect of the entropy term cannot be isolated without it.
5. **Section 4.3 is speculative.**
   - The claim that SimPO is stabilised by "dataset constraints and margins that approximate a reference" rests on one DPO diagnostic (Fig. 4, the batch average of the reference log ratio in Pythia-1B). That is a description of a statistic, not evidence of a mechanism.
   - There is no SimPO experiment, no ablation on γ, and no comparison to other offline methods.
   - The χ² result is "not reproducible" by the authors, with no details. The conclusion that references are "neither necessary nor sufficient" is not established.
6. **Scale and generality.** Only Pythia 1B and 2.8B on TL;DR are used, with a small reward model and one proxy judge. The generality of "failure modes of MaxEnt RLHF" is overstated. There is no larger model, no other task, and no human evaluation. "Fully reproducible" is claimed without code or configs.
7. **Presentation.** The title and abstract promise both a theory and failure modes, and both are weakly supported. Claims are hedged inconsistently ("appears to", "suggests", "clear failure case", "fundamental limitations"). Fig. 3 and Fig. 5 are referred to out of order. Typos appear ("standart", "REPRODUCIBIBLITY").

## Questions
- In Eq. 16, what exactly is the policy π* when α depends on |y|? What objective does it maximise, and does Z(x) still cancel?
- Does SimPO's loss correspond to any MaxEnt problem with a per-prompt constant α? If not, in what sense is SimPO "the" MaxEnt RL solution?
- Please show coefficient-0 (plain RLOO) runs at the same LRs for both model sizes, over multiple seeds. Please also show a KL-penalised sweep across LRs matched to the MaxEnt LRs.
- Is rising entropy a cause of overoptimisation, or a symptom? Can you intervene, e.g. by clipping or detaching the entropy term?
- Can you run SimPO itself on the same TL;DR setup and show whether the online failure has an offline analogue (e.g. multi-epoch or on-policy SimPO)?
- Why does the 2.8B model collapse at KL values similar to those of the healthy 1B run?
- Please report the minimum-entropy results and the PPO clipping diagnostics as figures or tables.

## Scores
- **Soundness:** 2. The derivation does not hold as written, and the empirical evidence is single-seed, confounded and partly unreported.
- **Presentation:** 2
- **Contribution:** 2

**Rating:** 2

**Confidence:** 4

The theory is a notational reparameterisation with a flawed step. The experiments are narrow and uncontrolled, and the headline causal conclusions go beyond the evidence. With matched baselines, seeds, an actual SimPO comparison and a corrected derivation, this could become a useful negative-results note.
