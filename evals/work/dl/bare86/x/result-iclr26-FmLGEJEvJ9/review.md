# Review: On Differentially Private String Distances (ICLR 2026)

I read the extracted text only and judged the algorithms and proofs from it. The paper has no figures that I could see, so none were needed.

## Summary
The paper studies ε-DP data structures that estimate Hamming and edit distance between a query B and each of m database bit strings. Privacy is in the function-release model: the structure is released once and then queried arbitrarily often. Neighbouring databases differ in one bit of one string. Accuracy is promised only when every database string is within distance k of B.

- **Hamming distance.** The authors take the Pagh–Lugosi style sketch of size Õ(k): a two-level hash with M1 = Θ(log k), M2 = 2k and M3 = Θ(log² k). They apply bit-wise randomized response to the sketch. One input bit touches 2·M1 sketch cells, so each cell is flipped with probability 1/(1+e^{ε/(2M1)}).
  - The query takes Õ(mk + n) time and the space is Õ(mk).
  - The additive error is Õ(k / e^{ε/log k}).
  - The paper contrasts this with Laplace noise on the sketch, which gives Õ(k/ε).
- **Edit distance.** They build a DP longest-common-prefix (LCP) oracle. It is a binary tree of tiny Hamming sketches with budget ε/log n per node, queried by binary search over XOR-merged interval sketches. This replaces the suffix-tree LCP oracle in the Landau–Myers–Schmidt O(n+k²) algorithm.
  - The query takes Õ(mk² + n) time and the space is Õ(mn).
  - The error is Õ(k / e^{ε/(log k log n)}).
  - A structural lemma says an LCP oracle with additive error δ yields an edit-distance error of O(kδ).

## Strengths
- The problem is clean. It sits at the intersection of DP function release and fine-grained string algorithms.
- Randomized response on a sketch is a sensible idea. The privacy argument for Hamming distance (Lemma 4.3) is short and, as far as I checked, correct. Privacy for the edit-distance structure then follows cleanly by post-processing (Lemma 5.6).
- The running times track the non-private state of the art: Õ(n+k²) for edit distance, which is conditionally optimal. The authors say so honestly.
- The DP noise in the LCP oracle only ever overestimates the LCP (w̃ ≥ w), and it propagates additively through the DP recurrence. This is a neat, modular observation (Remark 5.9).
- The paper is short and mostly easy to follow.

## Weaknesses

1. **The utility guarantee is vacuous in the regime that matters.**
   - The Hamming error bound is O(k log³k / e^{ε/log k}). The true distance is at most k by assumption, so outputting 0 already has error ≤ k. The bound beats that trivial answer only when e^{ε/log k} ≳ log³k, i.e. ε ≳ 3·log k·log log k.
   - Reaching O(1) error needs ε ≳ log² k. For k = 1000 that is on the order of 50 or more.
   - For edit distance the requirement is worse, around ε ≳ log² k · log n, which is several hundred for realistic n and k.
   - For ε = O(1), the standard DP regime, the flip probability is essentially 1/2 and the output is noise. The error exceeds k.
   - The abstract and introduction ("exponentially small error", "strong privacy guarantees") are therefore misleading. The comparison with Laplace noise is asymptotic only, with the budget left free. The paper never shows the regime where its bound wins, and it never says the guarantee is trivial for moderate ε.
   - The log k factor in the exponent comes from composing over M1 = Θ(log k) repetitions, and edit distance loses a further log n. No lower bound is given to say whether this loss is necessary.

2. **No empirical evaluation and no baselines.**
   - There are no experiments. Constants matter a lot here: M3 = 400 log² k, M1 = 10 log k and the collision constants. The practical sketch size is about 8000·k·log³k cells per string, which exceeds n for most realistic k.
   - The claim that "for moderate k both structures support sublinear query" needs k·polylog(k) ≪ n, which is very restrictive given those constants.
   - There is no comparison with simple alternatives:
     - de-biased per-bit randomized response on the raw string, which is ε-DP with error roughly √n/ε-ish and no k assumption;
     - the DP similarity-to-private-datasets approach of Backurs et al. (ICLR 2024), which the paper cites but does not compare with;
     - Laplace noise or randomized response on a smaller sketch with an optimised budget.
   - That randomized-response baseline might already beat the proposed error for moderate k, ε and n. The paper should address it.

3. **The privacy notion does not match the motivation.**
   - The introduction motivates the work with patient records and an adversary who learns "the number of symptoms of patient i" or whether patient i has symptom j.
   - The neighbouring relation changes one bit of one string. This protects a single symptom bit. It does not hide a patient's whole record or the presence of a patient.
   - By group privacy, hiding a full record costs a factor of up to n in ε, which makes the already vacuous bound hopeless. The paper should say this limitation explicitly and discuss user-level privacy.
   - Footnote 1 has an index typo: "one i ∈ [n]" should be [m].
   - Accuracy holds only if all m strings are within k of B. The paper does not say what happens otherwise.

4. **Technical gaps and sloppiness in the proofs.**
   - Lemma 4.7: the proof writes |z̃ − z| = Σ_j max_i Σ_c R_{ijc}. After flipping, |S − S^B| can also decrease (when S ≠ S^B and the cell is flipped), so equality fails. The upper bound is salvageable by the triangle inequality, but the text is wrong as written. The lemma also combines a mean bound with Chebyshev loosely and gives only constant success probability. Boosting is deferred to a remark.
   - DP-LCP, IntervalSketch: the sketch of an interval is the XOR of up to O(log n) noisy node sketches. The effective flip probability per cell grows to about log n · p, up to 1/2. Lemma B.5 uses the single-node flip probability in its Hoeffding argument and does not account for this. Either the analysis, the thresholds, or the log n factors in the exponent are off.
   - Theorem 5.1 states the LCP error as an expectation, E[D_ham] ≤ …. Lemma B.6 gives a high-probability bound, and the edit-distance proof (Lemma 5.8) uses the high-probability version. These should be consistent.
   - Algorithm 3, QueryInit calls BuildTree(B, n, k, 0). With ε = 0 we get ε′ = 0 and flip probability 1/2, not "no noise". It should be ε = ∞. Several index ranges in Algorithm 3 are also wrong ("i·n/2^j" with i ∈ [log n], j ∈ [2^i]).
   - Lemma 4.4 uses a loose chain of inequalities that is not clearly right for all k. The hash functions are assumed fully random over [2n]. The cost of storing or evaluating "public random hash functions" is not discussed, yet the Õ(mk+n) time and Õ(k) space claims should include it. The role of the public randomness in the 0.99 success probability should also be stated.
   - The edit-distance guarantee has a one-sided structure (r̃ ≤ r), which means that for small ε the estimator collapses towards 0. The paper never discusses the direction of this bias.

5. **Limited novelty and fit.**
   - The Hamming structure is the Pagh–Lugosi sketch with randomized response. The edit-distance structure is LMS98 with an LCP oracle. A DP LCP oracle built from log n levels of Hamming sketches is a fairly direct instantiation. The "novel utility analysis" is essentially one induction over the DP table with crude telescoping.
   - There is no learning component, so the ICLR audience gets little out of it without an empirical regime where the method beats existing private-similarity methods.
   - The related work lists generic DP applications (ML, CV, NLP) rather than the closely related DP sketching, LSH and nearest-neighbour literature.

6. **Presentation.**
   - Õ(·) hides polylog factors that actually dominate the bound, which conceals the weakness in point 1.
   - The Õ(mn) space for edit distance is no better than storing the database. This should be flagged as a limitation.
   - There are typos and sloppy notation. D_ham is defined with 1[Ai = Bi], which counts equal positions rather than differing ones. There are also "perprocesses" and "Differentiall".
   - There is no discussion of which ε values are meaningful and no table of parameters.

## Questions
1. For which (ε, k, n) does your error beat both the trivial answer (error k) and de-biased per-bit randomized response? Please give concrete numbers with the constants of Algorithm 1.
2. Is the log k loss in the exponent inherent? Can one obtain error k/e^{Ω(ε)} or k/ε^c, or prove a lower bound for any ε-DP function release with Õ(k)-size sketches?
3. How does XOR-merging O(log n) noisy node sketches in IntervalSketch change the flip probability used in Lemma B.5? Is the appendix analysis correct as written?
4. Can the guarantees be extended to user-level (full-record) privacy, or to (ε, δ)-DP with Gaussian-style noise that would avoid the log k composition?
5. What is the behaviour when the query is farther than k from some database string?
6. How are the public hash functions h and g implemented, and what do they cost in space and time?

## Ratings
- **Soundness: 2.** The Hamming privacy proof is fine. The utility bounds are meaningful only at very large ε, and there are incorrect or unjustified steps in the DP-LCP analysis.
- **Presentation: 2.** Readable overall, but with sloppy notation, algorithm errors and overstated claims.
- **Contribution: 2.** A reasonable theoretical problem, but a modest technical advance, with no lower bounds, no experiments, and a bound that is vacuous at ε = O(1).

**Rating: 4** (marginally below the acceptance threshold)

**Confidence: 3**
