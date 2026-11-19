# Review: Benchmarking Optimizers for Large Language Model Pretraining (ICLR 2026)

*Scope note: I read the main text (through the Discussion). I did not read the appendices (hyperparameter grids, extra figures). Figures are not available, so I relied on captions and text; plot-dependent claims such as the size of gaps are judged from captions only.*

## Summary
The paper benchmarks 11 optimizers (AdamW, ADOPT, AdEMAMix, Lion, Signum, Sophia, SOAP, Muon/D-Muon, SF-AdamW, Prodigy, MARS) for LLM pretraining on FineWeb. It uses Llama-style dense models (124M, 210M, 583M, 720M) and one 520M MoE. It varies batch size (16k to 2M tokens) and training duration (1B to about 50B tokens, below and beyond Chinchilla). Hyperparameters are tuned near the Chinchilla-optimal horizon and then reused for longer runs; the authors report about 2900 runs and 30k GPU hours. The paper also includes ablations on weight decay, warmup, LR schedule, final LR, z-loss, and wall-clock cost. The main conclusions are:
- AdEMAMix is the best overall; MARS is also strong at large batch and model size.
- D-Muon is robust, while plain Muon is poor because it lacks weight decay on 2D parameters.
- Sign-based methods and MARS benefit from large batches, but Lion and Signum scale poorly with model size.
- SOAP's advantage over AdamW shrinks with longer training and is sensitive to setup details (final LR, weight decay, z-loss).
- Many popular defaults are suboptimal (final LR of 0.1x, small weight decay, beta2 = 0.95).
- Rankings transfer from dense models to the MoE.

Code is released.

## Strengths
- **Useful, timely question and broad coverage.** There are many optimizers, several batch sizes, several durations (including over-training) and an MoE case. A comparison like this is directly valuable to practitioners.
- **Experimental discipline.** The paper tunes each method rather than using defaults and states how tuning was done. It decays the LR to 0.01x gamma_max and uses decoupled weight decay everywhere. It reports compute cost and releases code.
- **Corrections to prior setups.** Prior benchmarks omit or under-tune weight decay, decay the LR to only 0.1x, and add a z-loss. The paper shows that these choices change rankings. In particular, it finds AdamW >= SOAP at 583M with a 2M-token batch under better-tuned settings, which contradicts an earlier claim (Fig. 16, Takeaway 9). The Muon vs. D-Muon result (Figs. 4, 8) and the Signum coupled-weight-decay implementation issue are concrete and actionable.
- **Practical ablations.** The results on warmup (optimizer-dependent, contradicting the "25% of the horizon" claim), schedule (cosine vs. WSD vs. linear, optimizer-dependent), weight decay (large lambda for short runs, 0.1 for long runs), the beta2/beta3 increase for longer runs, and LR transfer to an 8x longer run are informative.
- The paper is honest about several limitations: loss only, scale <=720M, and some optimizers not covered.

## Weaknesses
1. **Tuning is not equal across optimizers, and this is the main threat to the headline rankings.**
   - Hyperparameters are tuned at one near-Chinchilla horizon and then frozen. The authors themselves show the optimum shifts (beta2 0.95 -> 0.999 for AdamW, beta3 0.999 -> 0.9999 for AdEMAMix; Fig. 21). The ranking at long horizons is therefore confounded with how well each method's frozen settings extrapolate.
   - The paper says SOAP vs. AdEMAMix flips depending on whether beta is re-tuned (Fig. 6 right, Fig. 19 caption). That shows the conclusions are sensitive to tuning protocol.
   - Search grids and effort differ by method (e.g., sign-based methods and Sophia were re-tuned at 210M and 720M, MARS betas follow the original paper). It is hard to tell whether "AdEMAMix wins" reflects a real advantage or the extra hyperparameters it has (beta3, alpha) being searched.
   - AdEMAMix has an extra slow EMA, so its memory and state costs differ. The comparison is on iterations and tokens, with no memory or throughput normalization beyond a small single-GPU timing test.
2. **No statistical uncertainty.**
   - Rankings are drawn from single-seed final validation losses. Many differences are in the 0.01-0.03 range, for example the gaps among AdamW, D-Muon, SOAP and ADOPT at long horizons. These may be within seed noise. I saw no seed-to-seed variance for the loss comparisons (only for wall-clock time).
   - Statements such as "all methods remain at the same position in our tier-list" or "ranking does not change" are not supported without confidence intervals.
3. **Scale is modest relative to the claims.**
   - The largest model is 720M and the largest run is about 48B tokens, with a 512-token context. The title and abstract speak of "LLM pretraining" and guidance for practitioners. The paper itself states that behavior changes with scale (Lion/Signum degrade, and the Prodigy and SOAP stories differ between 124M and 720M). That suggests extrapolation to 1B+ models is risky.
   - The 720M experiments cover only three durations and one batch size. The 583M experiment compares just two optimizers.
   - The MoE result ("results transfer smoothly") rests on one small MoE with untuned hyperparameters. The claim is also partly contradicted by the paper's own note that SOAP beats AdEMAMix there.
4. **Evaluation is validation loss only.** No downstream tasks are reported. Loss differences between top methods are small, so practical significance is unclear. The sharpness of conclusions such as "AdEMAMix and MARS dominate by a huge gap" is not tied to downstream quality or to cost-to-reach-a-target-loss.
5. **Several explanations and generalizations are asserted without a test.**
   - The paper says Prodigy's effective LR "emulates AdamW" and that Lion works "similar to AdEMAMix". Sophia is dropped from the small-batch setting after it diverges, which biases the comparison, and its divergence is a negative result for a method with known sensitive tuning.
   - The Muon vs. D-Muon gap is attributed to weight decay, but there is no ablation that adds weight decay to Muon in isolation with LR re-tuned (the D-Muon variant also changes the LR scaling rule).
   - The claim that "Muon degrades with model size" is thin, based on three sizes.
6. **Novelty is limited.** The contribution is an empirical benchmark, and several findings reproduce or extend known results (weight decay importance, decaying to a small final LR, beta2 for long training, cosine vs. WSD). That is acceptable for a benchmark, but the "first large-scale, controlled benchmark" claim should be softened, since earlier benchmarks (e.g., AlgoPerf, Zhang et al.) overlap. The comparisons with earlier work are mostly assertions that "our results contradict" it, without a controlled reproduction of the earlier setup in every case.
7. **Presentation.**
   - The text is long and takeaway-heavy, with 12 takeaways, many of which restate figures. Key evidence is in the appendix.
   - I saw no single table of final losses with numbers in the main text, so the rankings are read from figures.
   - Some wording is loose ("careful tuning", "huge gap", "remarkably") without quantified differences.
   - Typos and grammar problems are frequent.

## Questions
1. Can you report seed variance (>=3 seeds) for the top methods at one or two settings, and mark which rankings in Figs. 1, 5, 13 and 17 are statistically separated?
2. How much of AdEMAMix's lead survives a matched tuning budget? That means the same number of trials per method, and re-tuning every method at the longest horizon rather than only AdamW/AdEMAMix (beta2, beta3).
3. Could you add a cost-normalized comparison (time-to-target loss, optimizer state memory, step time at the 720M scale), since AdEMAMix and SOAP use more state or compute than AdamW?
4. For plain Muon, does adding decoupled weight decay (with LR re-tuned) fully close the gap to D-Muon? Is the LR scaling rule an independent factor?
5. Do the rankings (especially MARS vs. AdEMAMix vs. D-Muon) persist at >=1.3B parameters or with a longer context? If not, I'd suggest scoping the claims to <=720M.
6. Is there any downstream evaluation (even a few standard benchmarks) for the top 3-4 optimizers to check that small loss gaps are meaningful?
7. Why was Sophia dropped from the small-batch setting rather than tuned further? Is it excluded from the aggregate ranking?

## Ratings
- **Soundness:** 3. The experiments are careful and mostly well designed, but there are single seeds, an unequal tuning protocol across horizons, and conclusions stated with more certainty than the evidence supports.
- **Presentation:** 3. The text is clear in its structure, but it is verbose and relies on figures with no numeric tables in the main text.
- **Contribution:** 3. This is a valuable empirical resource and a useful correction of existing setups, but it has limited conceptual novelty and limited scale.

**Rating: 6** (marginally above the acceptance threshold)

**Confidence: 4**

The benchmark is large and useful, and the corrections to popular defaults are the most durable contribution. I would raise my score with seed-variance evidence and a more equal tuning comparison, and I would lower it if the rankings turn out to be within noise.
