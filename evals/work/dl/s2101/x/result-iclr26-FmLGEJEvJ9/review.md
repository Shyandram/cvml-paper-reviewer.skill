# Simulated Review: "On Differentially Private String Distances" (target venue: ICLR)

Date: 2026-11-10 · Mode: full · Literature check requested: strict, cutoff 2025-09-24 · Simulation of a panel, not a prediction of the real outcome.

**Execution note.** The five reviewer passes were run one after another by a single model context (no subagents), so they share one context. I tried to keep them independent by writing each from its own role file and not reading the other reports until Phase 2. The manuscript is text extracted from the PDF: no figures exist in the paper (none are referenced), and extraction garbled some tildes, exponents and the occasional equality sign. Garbled glyphs are treated as "unverifiable", never as the authors' mistakes. The integrity scan (`integrity_scan.py`) found no reviewer-directed text or hidden characters. The paper has no supplementary material beyond Appendices A and B, which were read.

---

## Phase 0: Paper Analysis and Reviewer Configuration Card

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | On Differentially Private String Distances |
| Primary Discipline | Theoretical computer science → differential privacy / data structures |
| Secondary Discipline(s) | Sublinear string algorithms (edit distance, sketching), privacy-preserving similarity search |
| Paper Type | Theoretical (composite weights: theoretical) |
| Core Technique(s) | Randomized response (bit flipping) on XOR-based Hamming sketches; Landau–Vishkin edit-distance DP with a noisy LCP oracle built from a dyadic tree of private sketches |
| Target Venue | ICLR (stated by the user); profile key `iclr`, 2026 cycle, scale status "secondary" |
| Venue-Specific Notes | None. ICLR accepts theory, but a reader will ask how the work relates to learning. Authors are visible only as a removed block; no identity information used. |
| Paper Maturity | Submission-ready draft (12 pages main text + 6 pages appendix; no experiments, no code) |
| Ethics-Relevant Content | None directly (no human data collected). The motivating example uses private medical data (Sec. 1). |

### Claimed Contributions (as stated by the authors)
1. **C1** (Thm. 1.1 / 4.1, Sec. 4): an ε-DP data structure for Hamming distance in the function-release model, with Õ(mk+n) query time, Õ(mk) space and error Õ(k/e^{ε/log k}), for queries within distance k of all database strings.
2. **C2** (Thm. 1.2 / 5.3, Sec. 5, App. B): an ε-DP data structure for edit distance with Õ(mk²+n) query time, Õ(mn) space and error Õ(k/e^{ε/(log k log n)}), built on a DP longest-common-prefix (LCP) structure.
3. **C3** (Sec. 4 intro; Remark 5.9): a "novel adaptation of the randomized response technique as a bit flipping procedure" whose error is "exponentially small" compared with Laplace noise, plus a structural result that an LCP oracle with additive error δ gives edit distance with additive error O(kδ) ("the first edit distance algorithm, based on noisy LCP implementations").

### Paper memory (factual record shared with all reviewers)
- **Setup facts:** no datasets, splits, training, seeds or compute (theory paper). Neighboring databases differ in one bit of one string (Sec. 1, footnote 1). Pure ε-DP only (Sec. 3.2). Public random hash functions h, g (Algorithm 1). Parameters M1 = 10 log k, M2 = 2k, M3 = 400 log²k (Algorithm 1); M1 = log k + log log n + 10, M2 = 1, M3 = 10 for DP-LCP nodes (Algorithm 3). Success probability 0.99 per structure (Thm. 4.1, 5.3), boosted to 1−β in Remark 4.8 only for Hamming.
- **Headline numbers:** query time Õ(mk+n) and Õ(mk²+n); error Õ(k/e^{ε/log k}) and Õ(k/e^{ε/(log k log n)}); space Õ(mk) and Õ(mn) (Abstract, Thm. 1.1/1.2, Conclusion).
- **Appendix:** A.1–A.4 prove Lemmas 4.3–4.6; B gives Algorithms 3–4 (DP-LCP) and Lemmas B.1–B.6.
- **Unverifiable:** no figures or tables exist; some extracted exponents/tildes are garbled.
- **Literature check:** the arXiv API was unreachable (HTTP 503) when `related_search.py` ran. Phase 1.5 was skipped as the skill prescribes for no network access. Missing references below come from knowledge and are marked `[verify]` where I am not fully sure.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Helena Marchetti-Sato, public research university (Western Europe)
- **Seniority / Expertise**: senior faculty / differential privacy, algorithms and data structures
- **Role**: reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style**: accepts theory with real weaknesses, but wants each main theorem's proof to be sound as written

### Reviewer 1 (Methodology): Dr. Anselm Okonkwo-Reyes, large public research university (North America)
- **Seniority / Expertise**: mid-career / DP mechanisms and their proofs; composition; randomized sketching
- **Review Focus**: proof correctness, parameters and constants, privacy accounting
- **Style**: re-derives each calculation line by line and recomputes constants

### Reviewer 2 (Domain): Dr. Yevgenia Prokhorova-Baptiste, industrial research lab (Central Europe)
- **Seniority / Expertise**: senior industry scientist / sublinear-time string algorithms, edit distance, sketching
- **Review Focus**: literature, novelty relative to sketching and private-similarity work
- **Style**: asks what is new relative to the closest known technique

### Reviewer 3 (Perspective): Dr. Naledi Mokoena-Fraser, medical school bioinformatics department (Southern Africa)
- **Seniority / Expertise**: mid-career / genomic data privacy, sequence-alignment practice
- **Review Focus**: deployment, assumptions behind the threat model, broader impact
- **Style**: constructive; starts from "who would use this?"

### Reviewer 4 (Generalist): Dr. Haruto Ikeda-Moreau, industrial ML lab (East Asia)
- **Seniority / Expertise**: mid-career / privacy-preserving ML, learning theory
- **Review Focus**: contribution clarity, ICLR fit, presentation
- **Style**: the typical program-committee member; reads the whole paper, not every derivation

### Devil's Advocate: Prof. Beatrix Oyelaran-Whitcombe, public university (Oceania)
- **Seniority / Expertise**: senior faculty / evaluation methodology, theoretical computer science
- **Review Focus**: core-argument challenges, overclaiming
- **Style**: rigorous, never hostile; checks whether the theorem proves what the abstract says

---
*Personas are fictional. Proceeding with the stated assumptions (theoretical paper type; ICLR profile).*

---

# Phase 1: Independent Reviews

---

# Peer Review Report (Reviewer 1)

## Paper: On Differentially Private String Distances
## Reviewer: Dr. Anselm Okonkwo-Reyes, Methodology Reviewer (large public research university, North America; fictional persona)
## Expertise: DP mechanisms and proofs; composition; randomized sketching
## Date: 2026-11-10

## Summary
The paper builds ε-DP "function release" data structures for Hamming and edit distance. For Hamming (Sec. 4), a Porat–Lipsky-style XOR sketch of the string is released after flipping each sketch bit with probability 1/(1+e^{ε′/(2M1)}); the query is sketched without noise and the distance is read from the sketch difference. For edit distance (Sec. 5, App. B), a dyadic tree of such sketches gives a noisy LCP oracle that replaces the suffix tree in the Landau–Vishkin–Myers dynamic program. The claims are privacy against unboundedly many queries plus additive error Õ(k/e^{ε/log k}) (Hamming) and Õ(k/e^{ε/(log k log n)}) (edit).

## Protocol Sweep and Omission Sweep (theory paper: no experiments)
Searched `test set`, `validation`, `held-out`, `selected`, `tuned`, `hyperparameter`, `per task`: no empirical evaluation exists. The only "select" is the analytic parameter choice in Lemma B.4 ("We select M1 = log k + log log n + 10 ..."). Omission sweep: privacy proof **present** (A.1, B.2); hash-function storage/derandomization **not stated after search**; code **not stated**; failure probability across many queries **not stated**; limitations **present only as one sentence in Sec. 6**.

## Strengths
### S1: Clean, checkable privacy argument for the Hamming structure
Lemma 4.3 (App. A.1) is correct as an argument. Encode touches M1 cells per position, so a one-bit change alters at most 2M1 sketch cells ("Since for each position, Encode changes at most M1 bits"), and per-cell randomized response with parameter ε/(2M1) composes to ε. Privacy holds regardless of how many queries are made, because the released object is the noisy sketch and queries are post-processing (Lemma 3.5). The denominator typo "(1+e^{ε/(2M1)})^n" (should be the sketch size) does not affect the bound.

### S2: The exponent improvement over per-coordinate Laplace is real in the high-ε regime
Sec. 4 intro explains why Laplace noise on a Θ̃(k)-bit sketch costs error Õ(k/ε), and that randomized response on bits gives an error decaying exponentially in ε/log k. Reading the paper charitably, to reach O(1) error the needed ε drops from ~k log k to ~log²k. That is a meaningful technical observation.

### S3: Structural reduction from noisy LCP to edit distance (Remark 5.9, Lemma 5.8)
The argument that an LCP oracle with one-sided additive error δ yields edit distance error O(kδ) (Part I monotonicity via Lemma 5.7; Part II induction on G) is a clean, reusable observation, and Lemma 5.7's proof is correct.

### S4: Appendix proofs are complete and self-contained
Appendices A and B give all lemma proofs inline; the paper has no deferred "proof omitted" steps, which made this audit possible.

## Weaknesses

### W1: Sketch comparison across different offsets is not justified, so Theorem 5.1 (and Theorem 1.2) rests on an unproven step
DP-LCP compares IntervalSketch(T^A, i, i+mid) with IntervalSketch(T^B, j, j+mid) for i ≠ j (Algorithm 4; in Algorithm 2, j = F+d with d ≠ 0 in general). Each node sketch is Algorithm 1 run on the node's substring (Algorithm 3: "DPHammingDistance.Init(A[j·n/2^i : (j+1)·n/2^i], ...)"), so Encode hashes the key 2(p−1)+A_p with p relative to the node start. The dyadic decompositions of [i,i+mid] and [j,j+mid] differ when i ≠ j, so equal substrings get different keys. Concrete check (ε = ∞): n = 4, A[1:2] = 01 is one size-2 node with keys {2·0+0, 2·1+1} = {0, 3}; B[2:3] = 01 is two size-1 nodes with keys {0, 1}. The substrings are identical (z = 0), yet the XOR sketches toggle different cells. Lemma B.4's claim for z = 0 ("Therefore, the output of the hash function is also the same") therefore fails under the construction as written. Standard LCP structures get shift-invariance from suffix trees or polynomial fingerprints; the XOR/hash sketch has none.
- **Suggested Fix**: use a shift-invariant fingerprint, or build the B-side tree once per diagonal d ∈ [−k,k] and state the cost (likely Õ(nk), which would break the Õ(mk²+n) claim). Either way Lemma B.4–B.6 need re-derivation. Cost: a revision of Sec. 5 and App. B (days of theory work, no compute).

### W2: The probability analysis of the DP-LCP threshold test contains an arithmetic error and a threshold/noise mismatch (Lemma B.5, Algorithm 4)
(a) In the proof of Lemma B.5, Hoeffding with L = √(M1M3) gives e^{−2L²/(M1M3)} = e^{−2}, a constant, yet the text continues "≤ e^{−2(log k+log log n)} ≤ 1/(300k² log n)". The required 1/(300k² log n) per test is not established. (b) Algorithm 4 uses threshold 1.5·M1M3/(1+e^{ε/(log k log n)}), but the flip probability actually used is 1/(1+e^{ε′/(2M1)}) with ε′ = ε/log n and M1 = log k + log log n + 10 (Alg. 1 line 26, Alg. 3 line 8); the exponents differ by 2M1/log k. (c) When the threshold falls below 1 (large ε), the test passes only if no cell is flipped, so identical strings are falsely rejected with probability ≈ 10·M1·p, which exceeds 1/(300k²) for a wide range of ε; this violates "w̃ ≥ w" that Part I of Lemma 5.8 needs.
- **Suggested Fix**: redo B.5 with multiplicative Chernoff bounds and a threshold consistent with the true flip rate, and state the regime of ε where the guarantee holds.

### W3: Constants in the exponent are dropped inside e^{·}, so the stated error bounds are not what the proofs give (Lemma 4.7, Lemma 5.8)
Lemma 4.7's proof uses flip probability 1/(1+e^{ε/M1}) while Algorithm 1 uses e^{ε′/(2M1)}; with M1 = 10 log k the actual exponent is ε/(20 log k), and M1M2M3 = 8000·k log³k (the proof writes k log³k). Õ(·) hides polylog factors, not constants inside an exponent: k·e^{−ε/(20 log k)} is not Õ(k·e^{−ε/log k}) once ε ≫ log k. The same applies to Theorem 1.2 (exponent ε/(2 log n·M1) vs. ε/(log k log n)). The theorems are correct only after replacing ε by ε/20 (or ε/(2M1/log k)), which changes the quantitative statement the abstract advertises.
- **Suggested Fix**: restate the bounds with explicit constants, or rescale the flip probability so the stated exponent holds; the privacy proof has slack to allow this.

### W4: The success-probability boosting of Remark 4.8 ignores privacy composition
Remark 4.8: "take log(1/β) independent copies of the data structure, and query all of them", and for m strings log(m/β) copies. Each copy is released, so the total privacy loss is log(1/β)·ε by basic composition unless each copy uses ε/log(1/β). Theorem 1.1 claims ε-DP and success 1−β simultaneously with error Õ(k/e^{ε/log k}); after splitting ε the exponent becomes ε/(log k·log(m/β)), which polylog factors in Õ cannot absorb. Theorem 1.2 states 1−β but no boosting argument is given for edit distance at all.
- **Suggested Fix**: split the budget and restate the bound, or state the theorems for constant success probability and say so.

### W5: Adaptive queries inside the edit-distance DP break the union bound (Lemma 5.8)
"There are 3k2 LCP queries, by union bound, the probability is at least 0.99." Theorem 5.1's guarantee holds for a fixed pair (i,j) over the structure's randomness. In Algorithm 2 the arguments F(i−1,j) are outputs of earlier noisy queries, so the queried pairs depend on the randomness. A union bound over the 3k² queries actually made is not valid; a union bound over all n² pairs would force per-query failure ≲ 1/n², changing M1 from log k + log log n to Θ(log n) and the exponent from log k·log n to log²n. The count is also inconsistent: Lemma 5.5 says k² queries, Lemma 5.8 3k², while Algorithm 2 makes up to 3·k·(2k+1) ≈ 6k²+3k calls.
- **Suggested Fix**: prove the guarantee for all pairs simultaneously (and restate the exponent), or analyze the adaptive process explicitly.

### W6 (smaller): utility is stated for a fixed query; hash functions are public and fully random
The 0.99/0.98 success probabilities (Thm. 4.1, Lemma 4.7) are per query over fresh h, g and flips; h, g are public and fixed once, so an adaptive adversary who chooses B after seeing h, g can create collisions that Lemma 4.4–4.5 exclude only for fixed B. Also h: [2n]→[M2] and g: [2n]×[M1]→[M3] are "random hash functions"; storing them costs Θ(n log k) bits, which is not counted in the Õ(mk) space bound. Please state the independence needed and the resulting space.

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Severity | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|----------|-----|
| ERR-1 | E2 | App. B, Alg. 3/4, Lemma B.4 | "Therefore, the output of the hash function is also the same." | Node-relative keys make sketches of equal substrings at different offsets differ (example n=4 above) | Small hand example from Alg. 1 Encode + Alg. 3 lines 4, 11 | Medium (depends on the literal construction) | MAJOR | Shift-invariant sketch or per-diagonal trees |
| ERR-2 | E2 | App. B.3, proof of Lemma B.5 | "e−2(log k+log log n)" | With L = √(M1M3), Hoeffding gives e^{−2}, not e^{−2(log k+log log n)} | Recomputed 2L²/(M1M3) = 2 | High | MAJOR | Use Chernoff; adjust constants |
| ERR-3 | E6 | Alg. 4 line 8 vs Alg. 1 line 26, Alg. 3 line 8 | "threshold ← 1.5M1 M3" | Threshold assumes flip rate 1/(1+e^{ε/(log k log n)}); the algorithm flips at 1/(1+e^{ε′/(2M1)}), ε′ = ε/log n | Cross-referenced three locations | High | MAJOR | Align threshold and flip rate |
| ERR-4 | E2/E3 | Remark 4.8 | "take log(1/β) independent copies of the data structure, and query all of them" | Releasing independent ε-DP copies composes to ε·log(1/β) | Derived (basic composition) | High | MAJOR | Split ε across copies; restate error |
| ERR-5 | E1/E6 | Lemma 4.7 proof vs Alg. 1 | "Flip each Si,j,c with independent probability" (Alg. 1, line 26) | Proof uses e^{ε/M1}; algorithm uses e^{ε′/(2M1)}; M1M2M3 = 8000 k log³k, not k log³k | Recomputed from Algorithm 1 parameters | High | MAJOR | State constants in the exponent |
| ERR-6 | E2 | Lemma 5.8 | "There are 3k2 LCP queries, by union bound, the probability is at least 0.99." | Queries are adaptive; also count differs from Lemma 5.5 and Alg. 2 (≈6k²+3k) | Cross-referenced Alg. 2 lines 13–22, Lemma 5.5 | Medium | MAJOR | All-pairs union bound or adaptive analysis |
| ERR-7 | E2 | Sec. 5, recurrence for D(i,j) | "D(i − 1, j − 1) + 1" | The second branch should be D(i, j−1)+1 (insertion); as printed it duplicates substitution and no base cases are given | Cross-checked against the standard recurrence and the F-recurrence below it | High | MINOR | Correct the recurrence |
| ERR-8 | E6 | Sec. 3 | "1[Ai = Bi ]" | Dham is defined as the number of equal positions, but is used as number of differing positions (Lemma 4.4 uses Ap ≠ Bp) | Cross-referenced Sec. 3 and Lemma 4.4 | High | MINOR | Use ≠ |
| ERR-9 | E6 | Alg. 3 line 23 | "T B ←BuildTree(B, n, k, 0)" | With ε = 0, Alg. 1 line 26 flips each bit with probability 1/2, destroying the query sketch; the query should be un-noised | Cross-referenced Alg. 1 line 26 | Medium (likely typo) | MINOR | Skip flipping for the query |
| ERR-10 | E6 | Thm. 5.1/5.3, Lemma 5.4 vs Lemma B.1 | "O(n log n(log k +" | Theorems say Init is O(n(log k+log log n)); Lemma B.1's own sum gives an extra log n | Recomputed Σ 2^i·(n/2^i)·M1 = n·M1·(log n+1) | High | MINOR (absorbed in Õ) | Fix the statement |
| ERR-11 | E6 | Sec. 4 intro | "Let t = log k/ǫ" | With this t, Laplace error O(ε⁻¹k log k) = O(tk) and the new error is k·e^{−1/t}; the text states O(t⁻¹k) and O(e^{−t}k), i.e. t should be ε/log k | Recomputed | High | MINOR | Define t = ε/log k |

## Claim-to-Evidence Map
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | ε-DP Hamming structure, error Õ(k/e^{ε/log k}), 1−β success | Thm. 1.1, 4.1 | Lemmas 4.3–4.7, Remark 4.8 | Partially (privacy correct; error exponent and 1−β boosting not as stated: W3, W4) |
| C2 | ε-DP edit structure, error Õ(k/e^{ε/(log k log n)}) | Thm. 1.2, 5.3 | Thm. 5.1, Lemma 5.8, App. B | Unsupported as written (W1, W2, W5) |
| C3 | "exponentially small" error vs Laplace; first noisy-LCP edit algorithm | Sec. 4 intro; Remark 5.9 | Lemma 4.7; Lemma 5.8 | Partially (true only for ε ≳ log k) |

## Questions for Authors
1. In Algorithm 3, is the hash key of a node sketch node-relative or global? If global, how are sketches of A[i:i+L] and B[j:j+L] for i ≠ j made comparable? An answer that gives a shift-invariant construction would raise my score; a per-diagonal construction with its cost would be a lower-claim but acceptable fix.
2. Can the Hoeffding step of Lemma B.5 be repaired for the actual regime of ε (threshold < 1)? Which values of ε does Theorem 1.2 cover?
3. Is Theorem 1.1 meant for constant β with the stated exponent, or with ε split across copies?

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Hamming privacy is sound; the edit-distance proof has verified gaps (W1, W2); technical rigor 42 and empirical-validation 32 average below the usual 2-band because a theory paper has no experiments, so I keep Quality at 2 |
| Clarity | 3 | Readable structure, many notation slips (ERR-7–ERR-11) |
| Significance | 2 | Only meaningful for large ε; edit part unproven |
| Originality | 2 | Randomized response on a known sketch is a modest step; the noisy-LCP reduction is new |

## Dimension Scores (0–100)
**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the edit-distance half of the paper rests on a construction that fails my small example (ERR-1) and a probability bound that does not follow (ERR-2); the Hamming half is sound but its stated bound is overstated by constants in an exponent (ERR-5).

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 42 | Developing | Multiple verified proof gaps in the main theorem for edit distance; privacy proof for Hamming is correct |
| Clarity & Presentation | 62 | Competent | Organized; recurring notation/typo errors |
| Novelty & Originality | 52 | Developing/Competent | Known sketch + RR; new noisy-LCP reduction |
| Significance & Impact | 48 | Developing | Non-vacuous only when ε is large |
| Experimental Validation | 32 | Developing | No empirical sanity check of constants, no lower bound, no comparison to alternative private sketches |
| Reproducibility | 55 | Competent | Full proofs and algorithms, but constants and hash storage are loose |
| Ethical Compliance | 65 | Competent | No ethics issue; limitations are one sentence |

## Limitations Assessment
**Partially.** Sec. 6 says only that better utility is interesting. Missing: the ε regime where the bounds are non-trivial, the "all strings within k of the query" assumption, and the per-query nature of the success probability.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: the Hamming result is a reasonable contribution with overstated constants; the edit-distance theorem is not established by the proofs as written, and the fixes appear to need re-analysis.

## Confidence
**4**: I re-derived each calculation; the offset issue (W1) depends on reading Algorithm 3 literally.

---

# Peer Review Report (Reviewer 2)

## Paper: On Differentially Private String Distances
## Reviewer: Dr. Yevgenia Prokhorova-Baptiste, Domain Reviewer (industrial research lab, Central Europe; fictional persona)
## Expertise: sublinear-time string algorithms, edit distance, sketching
## Date: 2026-11-10

## Summary
The paper privatizes the Porat–Lipsky Hamming sketch by randomized response and plugs a private LCP oracle into the Landau–Vishkin framework for the k-bounded edit distance. It positions itself against output-perturbation and Laplace noise on sketches and against non-private k-bounded edit-distance algorithms.

## Strengths
### S1: Appropriate algorithmic backbone
Using the sketch of [PL07] (Sec. 4) for the near-distance regime and Landau–Vishkin/Myers diagonals for edit distance (Sec. 5, Lemma 5.2) is the right toolbox, and the SETH remark in Sec. 1 correctly motivates the k-bounded regime.

### S2: A correct and useful remark on why per-query output noise fails
Sec. 1 explains that averaging repeated queries defeats output perturbation, which motivates the function-release model of [HRW13]. This is accurate and sets up the right model.

### S3: Clear statement of what is claimed relative to non-private optimality
The Conclusion and Sec. 1 note that Õ(k²+n) is near-optimal under SETH for m = 1 [GKKS23], so the time overhead of privacy is only polylogarithmic. That positioning is honest.

### S4: The noisy-LCP-to-edit-distance reduction is a genuinely new structural observation (Remark 5.9)
I could not recall a prior edit-distance algorithm built from an LCP oracle with additive error; the observation that error multiplies by k is simple but useful.

## Weaknesses

### W1: Related work on private similarity sketches is missing, so the novelty of the "bit flipping on sketches" idea is overstated
Sec. 2 covers DP in ML broadly (CV, NLP, federated learning) and function release, but not the closest lines: randomized response applied to Bloom-filter/bit sketches for private similarity (RAPPOR-style and BLIP-style), and DP via Johnson–Lindenstrauss sketches for distance queries. The abstract's "novel adaptation of the randomized response technique" and Sec. 4's "we present a novel scheme that flips each bit of the sketch" need to be differentiated from these. The XOR/hash sketch and the max-over-rows decoding are the new parts; plain RR on a bit sketch is not.
- **Suggested Fix**: add a related-work paragraph and a comparison table (setting, privacy notion, error vs ε) against these lines.

### W2: No comparison to simpler baselines in the actual regime of interest
Sec. 4 compares only with Laplace noise on each sketch coordinate (error Õ(k/ε)) and claims an exponential gap. The alternatives a reader would try are not analyzed: (i) a JL-style private sketch, (ii) randomized response on the input bits with debiasing (error ~√n/ε-type), (iii) the trivial data-independent answer k/2, which already has error ≤ k/2 for every ε since the query is guaranteed within k of every string. The paper's bound is below k/2 only when e^{ε/log k} ≳ log³k, i.e. ε ≳ 3 log k·ln log k with constants dropped, and only for ε ≳ 20 log k·ln(8000 log³k) with the algorithm's own constants. I derived the latter from Algorithm 1 (M1M2M3 = 8000 k log³k; flip exponent ε/(20 log k)); for k = 1024 and log = log₂ this is ε ≈ 3,200, versus ≈ 69 with constants dropped.
- **Suggested Fix**: state the non-trivial regime, add the trivial-baseline comparison, and report a lower bound (packing/group-privacy arguments give error Ω(1/ε) at least; see Missing References).

### W3: The "all database strings within k of the query" assumption is much stronger than the cited motivation
Sec. 1 justifies the assumption by SETH hardness and by the k-bounded edit-distance literature, where the promise is that the two strings being compared are close. Here the promise is max_i D(A_i,B) ≤ k (Thm. 1.1/1.2), i.e. every string in the database is within k of the query. That is a clustered-database promise, not a nearest-neighbor query. Behavior for queries violating it is not stated. The intro's own attack examples (querying 0^n or e_j, Sec. 1) violate the promise whenever strings have weight above k.
- **Suggested Fix**: add a "report distance or ⊥ if > k" variant, or discuss clearly which applications meet the promise.

### W4: Citation and description checks (E7)
(a) The baseline "Laplace noise gives error O(ε⁻¹k log k)" is attributed to an analysis of a generic sketch (Sec. 4 intro) but the sketch of [PL07] used here has Θ̃(k) cells with each position touching M1 cells, so sensitivity of the sketch is 2M1, not 1 ("only one coordinate would change"). The Laplace baseline is therefore under-counted by a polylog factor; the gap to the new method is slightly different from what is claimed. (b) [GKKS23] is used for "O(n+k²) optimal" correctly. (c) The related-work paragraph on DP lists many applications that are unrelated to the technique (CV, NLP, peer review) and omits technique-relevant work; the list reads as padding.
- **Suggested Fix**: recompute the Laplace baseline with the true sensitivity; trim or retarget the DP-applications list.

### W5: Edit-distance claims "first ... based on noisy LCP implementations" are unverified
Remark 5.9 says "To the best of our knowledge, this is the first edit distance algorithm, based on noisy LCP implementations." Because no literature search is possible offline here, I treat this as plausible but unchecked; the authors should support it with a short survey of approximate/robust LCP oracles.

### Literature-check addendum
The literature check was **not run** (arXiv API unreachable, HTTP 503), so there is no claim-level novelty profile, baseline scout table or similarity score. From knowledge: closest lines are (a) private similarity on bit sketches (BLIP, RAPPOR), (b) DP-JL sketches, (c) function release [HRW13]-type results the paper cites. Per-claim novelty (knowledge only, `[verify]`): C1 medium (RR on a known sketch; the max-row decoder is new); C2 medium-to-high (private LCP/edit structure not known to me); C3 medium. Field snapshot (knowledge-based): DP data-structure and similarity-search results at ML venues are valued when they give non-trivial utility at ε = O(1) or give lower bounds; large-ε upper bounds are seen as incremental unless they come with a new technique.

## Missing References
*Literature check not run; entries below are from knowledge. Entries I am less sure of are marked `[verify]`.*
| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Important | M. Alaggan, S. Gambs, A.-M. Kermarrec, "BLIP: Non-interactive Differentially-Private Similarity Computation on Bloom Filters", SSS 2012 `[verify]` | Bit flipping on bit sketches for similarity under DP: the closest prior idea to the proposed scheme |
| Important | Ú. Erlingsson, V. Pihur, A. Korolova, "RAPPOR: Randomized Aggregatable Privacy-Preserving Ordinal Response", ACM CCS 2014 | Randomized response on Bloom-filter bits; shows the technique is established |
| Important | J. Blocki, A. Blum, A. Datta, O. Sheffet, "The Johnson–Lindenstrauss Transform Itself Preserves Differential Privacy", FOCS 2012 | DP sketching for distance queries; natural baseline |
| Important | K. Kenthapadi, A. Korolova, I. Mironov, N. Mishra, "Privacy via the Johnson–Lindenstrauss Transform", Journal of Privacy and Confidentiality, 2013 | Same line; baseline for distance estimation |
| Helpful | S. L. Warner, "Randomized response: a survey technique for eliminating evasive answer bias", JASA 1965 | Origin of randomized response; frames the "adaptation" claim |
| Helpful | M. Hardt, K. Talwar, "On the Geometry of Differential Privacy", STOC 2010 `[verify]` | Packing arguments for lower bounds on private query release |
| Helpful | Line of work: DP approximate nearest-neighbor / LSH-based private similarity search (2018–2024) `[verify]` | Same application as the intro's database-query motivation |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Main claims plausible but proofs have gaps I did not check line by line (R1's domain); utility regime unaddressed |
| Clarity | 3 | Clear organization |
| Significance | 2 | Meaningful only at large ε; narrow promise on queries |
| Originality | 2 | Modest for Hamming; noisy-LCP reduction is new |

## Dimension Scores (0–100)
**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main contribution is applying RR to a known sketch, positioned without the closest private-sketch literature, with a utility regime that is not shown to be useful.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Framework sound; sensitivity/Laplace baseline off (W4); I rely on R1 for the proofs |
| Clarity & Presentation | 64 | Competent | Clear narrative |
| Novelty & Originality | 50 | Developing | RR on sketches is established; noisy-LCP reduction new |
| Significance & Impact | 50 | Developing | Large-ε regime and strong promise limit use |
| Experimental Validation | 35 | Developing | No empirical sanity check, no lower bound, no baseline comparison |
| Reproducibility | 58 | Competent | Algorithms explicit |
| Ethical Compliance | 65 | Competent | No issue; thin limitations |

## Questions for Authors
1. What is the smallest ε for which the Hamming error bound beats the trivial answer k/2, with explicit constants? (A clear answer in the paper would raise my significance score.)
2. How does the scheme compare with a JL-style private sketch on the same promise? (A matching or better bound would raise novelty; a worse one lowers it.)
3. Is a "distance ≤ k or ⊥" variant, which avoids the all-strings-within-k promise, possible with the same structure?

## Limitations Assessment
**Partially.** See R1.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: a plausible but incremental Hamming result with weak positioning and an unproven edit-distance half.

## Confidence
**4**: confident about the literature context; I did not independently verify the lemma-level proofs.

---

# Peer Review Report (Reviewer 3)

## Paper: On Differentially Private String Distances
## Reviewer: Dr. Naledi Mokoena-Fraser, Perspective Reviewer (medical school bioinformatics department, Southern Africa; fictional persona)
## Expertise: genomic data privacy; sequence alignment in practice
## Date: 2026-11-10

## Summary
The paper proposes private, fast distance estimators between a query string and a database of bit strings, motivated by private medical data (Sec. 1: m patients, n symptoms) and sequence comparison in biology. It makes the privacy guarantee hold for an unbounded number of queries by releasing a noisy sketch once.

## Strengths
### S1: A well-posed model for repeated queries
Function release (Sec. 1, Def. 3.4) is the right abstraction for a database that many clients query; per-query noise would leak through averaging, as Sec. 1 argues.

### S2: Time guarantees that match the non-private state of the art up to polylog
Õ(mk²+n) for edit distance (Thm. 1.2) is close to the SETH-optimal Õ(k²+n) for m = 1, which matters for genomics-scale n.

### S3: The ideas travel
The noisy-LCP reduction (Remark 5.9) could serve other alignment tasks (e.g., approximate matching in biological databases) where an approximate LCP oracle is available.

### S4: Honest scope on privacy notion
The paper states its neighbor notion (one bit of one string, footnote 1) rather than leaving it implicit.

## Weaknesses

### W1: The privacy notion does not match the stated medical threat model
The intro (Sec. 1) worries about an adversary learning "whether patient i has symptom j"; this matches the one-bit neighbor relation. But protecting a patient's whole record changes up to n bits, and group privacy then gives e^{nε}, vacuous for any ε used here. The paper should say which of the two protections it provides. For genomic data the second notion is the one regulators care about.
- **Suggested Fix**: add a paragraph on record-level vs bit-level privacy and what ε means for each.

### W2: The utility promise excludes the paper's own attack examples
The attack examples (querying 0^n, or e_j and 0^n) have distance up to n to the database strings, while the guarantee requires max_i D(A_i,B) ≤ k (Thm. 1.1/1.2). Privacy still holds for those queries, but the estimates are not guaranteed there. A practitioner needs to know what the structure returns outside the promise, and whether it can be used as a screening step ("near or not") without a promise.
- **Suggested Fix**: state output behavior outside the promise; add a thresholded variant.

### W3: The practical privacy regime is not discussed
Because the error is k·e^{−ε/log k}·polylog (with constants hidden inside the exponent), nontrivial accuracy requires ε of order log k or more (Sec. 4, Lemma 4.7). In deployments, ε ≤ 1–10 is typical. The authors should say what ε they consider useful, and show one numeric instance (e.g., k = 1000) of ε versus error.
- **Suggested Fix**: add a short table or plot of the bound versus ε for representative k; even a numeric table needs no experiments.

### W4: Alternatives from other communities are not discussed
Private sequence comparison via cryptographic protocols (the paper cites [WHZ+15] only in the applications list) offers exact answers with different trust assumptions; local-DP randomized response (RAPPOR-style) and DP-JL sketches also target distance queries.
- **Suggested Fix**: add a short comparison of trust models and what each gives.

## Assumption Audit
(1) i.i.d./adversary model: adversary sees the released noisy sketch and the public hash functions; fine for privacy. (2) The promise max_i D ≤ k for the query (W2). (3) Hash functions are idealized random functions and public (Algorithm 1, "h and g are public random hash function"); their storage is not counted.

## Broader Impact
Privacy-enhancing technology; low misuse risk. A mild risk is false assurance: a deployer might read "ε-DP" without noticing ε must be large for useful answers. Ethics Review Flag: No.

## Future Directions
Lower bounds for private distance estimation; a thresholded "near/far" version; extension to larger alphabets; a short empirical study on genomic strings.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound privacy argument; I did not audit every lemma |
| Clarity | 3 | Understandable |
| Significance | 3 | Real motivation, but regime/assumption limits |
| Originality | 3 | Fresh combination (noisy LCP, RR on sketch) |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clean model and near-optimal runtimes for a hard problem, with weaknesses (regime, promise) that many accepted theory papers share.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Privacy proof correct; the rest I could not fully audit |
| Clarity & Presentation | 68 | Competent | Readable |
| Novelty & Originality | 62 | Competent | New reduction, new application of RR |
| Significance & Impact | 60 | Competent | Useful abstraction; limited regime |
| Experimental Validation | 45 | Developing | No evidence beyond proofs |
| Reproducibility | 62 | Competent | Algorithms listed |
| Ethical Compliance | 66 | Competent | Low risk; limitations thin |

## Questions for Authors
1. Which privacy notion should a hospital take away: bit-level or record-level, and what ε is needed for each?
2. Can you give one worked example (k, n, m, ε, error) in the medical setting of Sec. 1? A convincing example would raise my score; an example that shows ε ≈ 1000 would lower it.
3. What does the structure output when the query is farther than k from some strings?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**4 (Borderline Accept)**: a well-motivated model and close-to-optimal time bounds make it worth a look; I weigh the regime and promise issues as typical of accepted theory papers.

## Confidence
**3**: outside my core area (DP data-structure proofs); I did not check the proofs in detail.

---

# Peer Review Report (Reviewer 4)

## Paper: On Differentially Private String Distances
## Reviewer: Dr. Haruto Ikeda-Moreau, Generalist Reviewer (industrial ML lab, East Asia; fictional persona)
## Expertise: privacy-preserving ML, learning theory
## Date: 2026-11-10

## Summary
In my words: the paper asks whether one can release, once and with ε-DP, a structure that lets anyone estimate Hamming or edit distances from a query to all strings in a database fast, as long as the query is near all strings. It answers yes with randomized response on sketches, with additive error that decays exponentially in ε/polylog, and with near-optimal running time.

## Strengths
### S1: Clear problem statement and two headline theorems
Thm. 1.1 and 1.2 are stated crisply with time, space, error and privacy. A reader sees at once what is promised.

### S2: Good model discussion
The explanation in Sec. 1 of why output perturbation fails for repeated queries and the role of the function release model is short and clear.

### S3: Complete proofs in the appendix
All lemmas have proofs (App. A, B); nothing is deferred to an unavailable supplement.

### S4: Honest conclusion
Sec. 6 says utility could be improved; the authors do not oversell it there.

## Weaknesses

### W1: Venue fit and presentation of the ICLR contribution
The paper has no learning component and no experiment; its link to ICLR's audience is via the broad "privacy" theme and a one-line mention of ML applications in Sec. 2 ("training deep neural networks", "computer vision" ...). The ICLR criteria (Soundness, Presentation, Contribution) are all judged on the theory. The main text (12 pages) defers the key utility proofs to the appendix and gives no proof sketch of the central technical idea for edit distance; Sec. 5 text mostly reproduces a standard algorithm.
- **Suggested Fix**: add a half-page "technical overview" and a sentence on relevance to the ICLR community (private retrieval, DP search over embeddings).

### W2: Abstract and intro overstate the guarantee
The abstract says "strong privacy guarantees" and the Sec. 4 intro says the error is "exponentially small". Both hold only when ε is large relative to log k; for ε = O(1) the stated bound is above the trivial k/2 (my check from Lemma 4.7 with polylog factors dropped: k log³k/e^{ε/log k} ≥ k/2 whenever ε ≤ 3 log k·ln(log k)). The abstract should state the regime.
- **Suggested Fix**: add a clause "non-trivial for ε ≳ log k" to the abstract and Theorem 1.1.

### W3: Notation and statement slips reduce trust
Examples: Sec. 3 defines Dham with equality (1[Ai = Bi ]); footnote 1 indexes strings by i ∈ [n] instead of [m]; the Sec. 4 intro defines t = log k/ǫ but then uses t as ε/log k; Theorem 1.1 has "perprocesses"; Algorithm 3 stores Ti,j with indexes swapped relative to its BuildTree loop; Theorem 5.1 mixes a probability statement with an expectation ("E[Dham(...)] ≤"). None is fatal, but together they make the proof-checking burden high.
- **Suggested Fix**: a careful notation pass.

### W4 (minor): no empirical sanity check
A 10-line simulation of Algorithm 1 for a few (k, ε) values would show the regime and test the constants. I do not require it; I would simply find the paper more convincing with it.

## ICLR Criteria Checklist
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: main theorems proven | Partly | Sec. 4–5, App. A–B (see R1 for the gaps) |
| Soundness: assumptions stated | Met | Sec. 1 (promise), Sec. 3 |
| Presentation: self-contained and readable | Partly | Notation slips (W3); no technical overview |
| Contribution: new technique or finding | Partly | RR on sketches; noisy-LCP reduction |
| Contribution: relevance to the venue's audience | Partly | W1 |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Looks sound at a read; others found gaps |
| Clarity | 3 | Understandable with errors |
| Significance | 2 | Narrow regime and promise |
| Originality | 2 | Moderately new |

## Dimension Scores (0–100)
**Pool position:** better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the contribution is clear and technical, but its audience fit at ICLR is narrow and the abstract overclaims; I place it near the median, slightly above because proofs are complete.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Complete proofs, with typos and constant slips |
| Clarity & Presentation | 60 | Competent | Clear structure, many notation slips |
| Novelty & Originality | 55 | Competent | Moderate |
| Significance & Impact | 52 | Developing | Narrow |
| Experimental Validation | 40 | Developing | None; I do not expect experiments in full |
| Reproducibility | 58 | Competent | Algorithms fully listed |
| Ethical Compliance | 62 | Competent | Nothing to flag |

## Questions for Authors
1. Can you add a non-trivial-regime statement to Theorem 1.1? (This would raise Clarity and Soundness.)
2. Why is ICLR the right venue, and what ML use do you envision (e.g., private search over binary embeddings)?
3. Is a short simulation feasible?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: a clear but narrow theory contribution whose abstract overclaims and whose audience fit is modest; most weaknesses are fixable.

## Confidence
**3**: I read the whole paper but did not re-derive every lemma.

---

# Devil's Advocate Report

## Paper: On Differentially Private String Distances
## Reviewer: Prof. Beatrix Oyelaran-Whitcombe, Devil's Advocate (public university, Oceania; fictional persona)

---

## Steelman
The paper gives, in the function-release model, a privacy-preserving analogue of the classical k-bounded Hamming and edit-distance data structures at almost no cost in running time, with a technical idea (randomized response on an XOR sketch, then decoding with max-over-rows) that avoids the k·log k/ε error of Laplace noise, and a clean structural reduction from noisy LCP to edit distance.

## Core Argument Chain
1. Noisy per-bit randomized response on the Porat–Lipsky sketch is ε-DP (Lemma 4.3).
2. The same noise gives additive error Õ(k/e^{ε/log k}) on the decoded distance (Lemma 4.7).
3. Therefore Hamming estimation is private and accurate ("strong privacy guarantees", Abstract).
4. A dyadic tree of such sketches gives an ε-DP LCP oracle with small additive error (Thm. 5.1, App. B).
5. An LCP oracle with additive error δ yields edit distance with additive error O(kδ) (Lemma 5.8).
∴ ε-DP edit-distance structures with Õ(mk²+n) time and error Õ(k/e^{ε/(log k log n)}) exist (Thm. 1.2).

## Strongest Counter-Argument
The headline is "strong privacy plus small error". But the data-independent answer k/2 is within k/2 of the truth for every query that satisfies the paper's promise, at ε = 0. So an accuracy claim means something only below k/2, and Lemma 4.7's bound k·log³k/e^{ε/log k} is below k/2 only when ε ≳ log k·ln(log³k) (≈ 69 for k = 1024, log = log₂, constants dropped). With the algorithm's own constants (M1M2M3 = 8000 k log³k, flip exponent ε/(20 log k)), the threshold is ε ≈ 20 log k·ln(8000 log³ k) ≈ 3,200 at the same k. A guarantee that is non-trivial only for ε in the tens to thousands is not "strong privacy", and the Laplace comparison that motivates the scheme is an analysis of a naive baseline, not of the best alternative. This matters because the decisive step for edit distance goes through Appendix B, and there the verified problems compound. The DP-LCP construction compares sketches of A[i:i+mid] and B[j:j+mid] for i ≠ j, yet each tree node hashes node-relative positions, so even identical substrings at different offsets produce different sketches (Lemma B.4's z = 0 case fails on a four-symbol example). The probability bound that is supposed to make each threshold test reliable uses a Hoeffding step that evaluates to e^{−2}, not 1/(300k² log n). The threshold in Algorithm 4 is calibrated to a different flip probability than the one Algorithm 1 uses. And the 3k² "union bound" is applied to queries whose arguments depend on earlier noisy answers. Each defect alone could be a patch; together they mean Theorem 1.2 is not proven by the paper. A fix that restores shift-invariance likely changes the claimed Õ(mk²+n) time or Õ(mn) space, so the edit-distance theorem as stated may simply be false for this construction. The authors need to answer: what is the construction, with which cost, and for which ε?

## Issue List

### CRITICAL Issues
| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| DA-C1 | Logic/Evidence | App. B, Algorithms 3–4, Lemmas B.4–B.6; Thm. 5.1; Thm. 1.2 | Criterion 1 (the paper's own lemma is contradicted by its own construction): Lemma B.4 for z = 0 says "Therefore, the output of the hash function is also the same", but Algorithm 3 builds node sketches with node-relative keys (Alg. 3 line 11 runs Algorithm 1 on a substring), so IntervalSketch of equal substrings at different offsets differs (A = 01.., B = .01. example in R1-W1). Lemma B.5's Hoeffding step gives e^{−2}, not 1/(300k² log n) ("e−2(log k+log log n)"), and the test threshold uses a different flip rate than Alg. 1 line 26. Consequently Theorem 5.1, hence Theorem 1.2 (half the paper), is not established. | Use a shift-invariant fingerprint, or per-diagonal trees with an honest cost; redo B.4–B.6 with Chernoff bounds and consistent constants; restate Thm. 1.2 | Redesign / new analysis (needs re-derived structure, possibly different complexity) |

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Scope/Overclaim | Abstract; Thm. 1.1; Lemma 4.7; Sec. 4 intro | "On top of the strong privacy guarantees" and "exponentially small" error hold only for ε ≳ log k·loglog k (≈ 69 at k = 1024) or ≈ 3,200 with the algorithm's constants; for smaller ε the bound exceeds the trivial k/2. The evidence supports a weaker claim. | State the regime; add the trivial-baseline comparison; give explicit constants |
| DA-M2 | Evidence | Remark 4.8; Thm. 1.1; Thm. 1.2 | "take log(1/β) independent copies of the data structure, and query all of them": composition is not accounted; Theorem 1.2 claims 1−β with no argument | Split ε across copies; restate bounds |
| DA-M3 | Logic | Lemma 4.7 vs Alg. 1; Lemma 5.8 | Constants inside the exponent (ε/20 vs ε; 2M1 vs log k) are not absorbed by Õ; error bounds as stated are stronger than proved | Rescale ε or restate with constants |
| DA-M4 | Evidence | Lemma 5.8 | 3k² adaptive queries under a union bound: the guarantee is per fixed pair; Alg. 2's arguments depend on earlier outputs; query counts disagree (k², 3k², ≈6k²+3k) | All-pairs union bound or adaptive argument |
| DA-M5 | Scope | Thm. 1.1/1.2; Sec. 1 | The promise max_i D(A_i,B) ≤ k restricts to clustered databases; behavior outside is unspecified; intro's attack queries 0^n and e_j violate it | Add thresholded variant; discuss |
| DA-M6 | Overclaim | Abstract; Thm. 1.1 | "ε-DP against any sequence of queries" is a privacy statement; utility is per fixed query over fresh randomness with public hash functions; an adaptive adversary choosing B after seeing h, g is not covered | State that utility is for non-adaptive queries or prove adaptive robustness |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Presentation | Sec. 3 | Dham defined via equality ("1[Ai = Bi ]") |
| DA-m2 | Presentation | Sec. 5 | Recurrence for D(i,j) has "D(i − 1, j − 1) + 1" twice; no base cases |
| DA-m3 | Presentation | Sec. 4 intro | t defined as log k/ε, used as ε/log k |
| DA-m4 | Presentation | Thm. 5.1 vs Lemma B.6 | Probability statement mixed with an expectation; Alg. 3 line 23 uses ε = 0 for the query; Init time in Thm. 5.3 omits the log n from Lemma B.1 |
| DA-m5 | Logic | Lemma 4.5 (App. A.3) | Bound "> 0.5": with |T_j| ≤ 10 log k the union-bound sum is 0.5 + 0.025/log k, so Pr[E_i] is slightly below 0.5; constants need adjusting (not fatal) |
| DA-m6 | Logic | Lemma 4.4–4.6 | T_j defined via h(p) for p ∈ [n], but Algorithm 1 hashes keys 2(p−1)+A_p (A's and B's keys at a bad position can land in different buckets); easily repaired |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Cells in Alg. 1 sketch | "k log³k" (Lemma 4.7 proof) | 10 log k · 2k · 400 log²k = 8000·k log³k | No (constant) |
| Flip exponent | e^{ε/M1} (Lemma 4.7 proof); e^{ε′/(2M1)} (Alg. 1 line 26) | M1 = 10 log k → e^{ε/(20 log k)} | No (stated e^{ε/log k}) |
| Hoeffding bound, L = √(M1M3) | "e−2(log k+log log n)" | e^{−2L²/(M1M3)} = e^{−2} ≈ 0.135 | No |
| Number of LCP queries | 3k² (Lemma 5.8), k² (Lemma 5.5) | 3 · k · (2k+1) ≈ 6k²+3k from Alg. 2 | No |
| Init time of DP-LCP | O(n(log k+log log n)) (Thm. 5.1) | n·M1·(log n+1) (Lemma B.1 sum) | No (log n factor) |
| Lemma 4.4 union bound | 0.99 | 2k · 1/(200k) = 0.01 failure | Yes |
| Threshold ε for non-trivial error, k = 1024 | not stated | ≈ 69 (constants dropped); ≈ 3,200 (algorithm's constants), log = log₂ | n/a (derived) |

## Ignored Alternative Explanations
The exponential-in-ε/log k decay may be an artifact of the huge sketch overhead: Θ(k log³k) cells each flipped independently, so a gain at large ε can be a consequence of ε being large, not of the technique being better than JL-style or Laplace-based private sketches at equal ε. No equal-ε comparison to any alternative is given. A simpler method (data-independent k/2; debiased randomized response on the raw bits) may match the bound over the range where it is non-trivial.

## Missing Stakeholder Perspectives
Practitioners who need ε ≤ 10; clinicians who need record-level (not bit-level) protection (footnote 1 neighbor notion); implementers who cannot store fully random hash functions of domain 2n.

## Observations (Non-Defects)
The Hamming privacy proof (Lemma 4.3) is correct and neatly handles arbitrarily many queries through post-processing; Lemma 5.7 and the monotonicity argument in Part I of Lemma 5.8 are correct; the paper contains full proofs and a straightforward statement of its model; the noisy-LCP→edit-distance reduction (Remark 5.9) is a nice observation that may survive a repaired LCP structure.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 36 | The main theorem for edit distance is not established; constants inconsistent |
| Clarity & Presentation | 58 | Notation errors, but readable |
| Novelty & Originality | 48 | RR on sketches established; reduction new |
| Significance & Impact | 44 | Non-trivial only for large ε |
| Experimental Validation | 30 | No sanity check or lower bound |
| Reproducibility | 50 | Constants/hash storage unresolved |
| Ethical Compliance | 60 | No issue; thin limitations |

**Pool position:** better than about 28% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: Theorem 1.2's proof does not hold as written, and the Hamming bound is overstated by constants in an exponent.

## Overall: 2 | Confidence: 4

---

# Phase 1.5: Literature Check

Not run. `related_search.py fingerprint` was written (title, method names DPHammingDistance / DPEditDistance / DPLCP, cutoff 2025-09-24), but the first search (`private Hamming distance sketch`, strict) returned "arXiv API unreachable (HTTP 503)". As the skill prescribes, there is no claim-level novelty profile, baseline scout table or similarity score. Missing references in R2's report come from knowledge; uncertain entries are marked `[verify]`. No reviewer used literature-check results to raise or lower a score.

# Phase 1.6: Report Check (Editorial Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1–W5 | kept | Specific, located, with quotes and checks; not answered in the paper |
| R1 | W6 | kept as a smaller point | Specific; hash-storage point stays a question-style item |
| R2 | W5 ("first ... noisy LCP" unverified) | moved to Questions/Minor | No literature check possible; not a verified weakness |
| R2 | W4(a) (Laplace sensitivity) | rewritten | Paper says one coordinate changes in the *plain* [PL07] sketch; sensitivity 2M1 applies to the paper's own Algorithm 1 sketch, so the point is a precision note, not an error |
| R2 | W4(c) ("padding" in DP applications list) | rewritten | Neutralized wording; critique of the work only |
| R3 | W1–W4 | kept | Specific and located; W4 is an expansion suggestion, ordered last |
| R4 | W4 (no empirical check) | moved to Minor | Theory paper; the point is optional |
| R4 | W3 (notation slips) | kept, grouped | Verified against paper (Sec. 3, footnote 1, Sec. 4 intro) |
| DA | DA-m5 (Lemma 4.5) | kept as Minor | Arithmetic verified, repairable by constants |

Scores were not changed.

# Phase 2: EIC Meta-Review and Decision

## Editorial Synthesizer package (Part A)

**Master issue list and classes**

| Issue | Sources | Class |
|-------|---------|-------|
| Edit-distance DP-LCP proof not established (offset comparability; Hoeffding; threshold mismatch) | R1-W1, R1-W2, DA-C1 | CONSENSUS-2 + **DA-CRITICAL** |
| Non-trivial utility only for large ε; abstract overclaims | R1-W3 (partly), R2-W2, R3-W3, R4-W2, DA-M1 | CONSENSUS-4 |
| Constants inside exponents / bounds stronger than proved | R1-W3, DA-M3 | CONSENSUS-2 |
| Boosting composition (Remark 4.8) | R1-W4, DA-M2 | CONSENSUS-2 |
| Adaptive queries in union bound; fixed-query utility | R1-W5, R1-W6, DA-M4, DA-M6 | CONSENSUS-2 |
| Promise max_i D ≤ k too strong / unspecified outside | R2-W3, R3-W2, DA-M5 | CONSENSUS-3 |
| Missing private-sketch related work; novelty of RR on sketches | R2-W1, DA (novelty row) | CONSENSUS-2 (literature check not run) |
| Bit-level vs record-level privacy | R3-W1 | SOLO |
| Venue fit, no technical overview | R4-W1 | SOLO |
| Notation/typos | R1 Error Log, R4-W3, DA-m1–m4 | CONSENSUS-3 |
| Absence of experiments/simulation | R4-W4, R1-W (EV score), R3 | SPLIT (R4 optional; R1/R2 note no baselines) |

**Hinge issues:** DA-C1 / R1-W1–W2 (decides whether half the paper holds); the large-ε regime (decides significance); R3's higher rating rests on not auditing Appendix B.

**Official aggregation (before EIC weights, DA-C1 provisionally upheld).** Official mean 3.00; official composite 51.8; cap 3 (see below). Dimension spreads: Technical Rigor 26 ⚠ (R3 62 vs DA 36), others ≤ 16. Consistency warnings: R1's own composite 48.9 implies Overall 2 against its rating 3 (a one-step gap, explained by R1's note that the Hamming half is sound).

## EIC Meta-Review (Prof. Helena Marchetti-Sato)

### The Case For and Against
- **For acceptance:** a clean model (function release), a correct privacy proof for Hamming, near-optimal running times, and a new noisy-LCP-to-edit-distance reduction; most weaknesses in theory papers like this are fixable constants and framing.
- **Against acceptance:** utility is non-trivial only for ε of order log k or more (and, with the algorithm's constants, far more), the abstract calls this "strong privacy", and the proof of the edit-distance theorem relies on a sketch comparison that fails on a small example plus a probability bound that does not follow. Half the contribution is not established by the paper as written.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Node-relative keys make sketches of equal substrings at different offsets differ | R1-W1/ERR-1, DA-C1 | Alg. 1 `Encode` (hash of 2(p−1)+A_p, p over the passed string); Alg. 3 lines 4, 11; Lemma B.4 proof | **Verified** (on the literal construction) | n = 4 example reproduced: A[1:2] = 01 keys {0,3}; B[2:3] = 01 keys {0,1}. The authors could define keys globally and compensate shifts, but nothing in the text does so |
| Hoeffding step yields e^{−2} | R1-W2/ERR-2, DA-C1 | App. B.3, proof of Lemma B.5 | **Verified** | "e−2M1 M3 /(M1 M3 )" = e^{−2}, then "≤ e−2(log k+log log n)" does not follow |
| Threshold calibrated to a different flip rate than Alg. 1 | R1-ERR-3, DA-C1 | Alg. 4 line 8; Alg. 1 line 26; Alg. 3 line 8 | **Verified** | |
| Bound non-trivial only for ε ≳ log k·loglog k (≈69 at k = 1024; ≈3,200 with constants) | R2-W2, R4-W2, DA-M1 | Lemma 4.7; Alg. 1 params | **Verified** | The k/2 argument needs the promise D ≤ k, which Thm. 1.1 assumes |
| Remark 4.8 ignores composition | R1-W4, DA-M2 | Remark 4.8 | **Verified** | Basic composition over copies; the Theorem statements assume ε total |
| Constants in the exponent not absorbed by Õ | R1-W3, DA-M3 | Lemma 4.7 vs Alg. 1 line 26 | **Verified** | Fixable by rescaling ε, which changes the stated bound |
| Union bound over 3k² adaptive LCP queries | R1-W5, DA-M4 | Lemma 5.8 text; Alg. 2 | **Partly correct** | The gap is real as written; the all-pairs fix likely changes log k to log n in the exponent. The query-count mismatch is Verified (k² vs 3k² vs ≈6k²+3k) |
| Missing private-sketch related work (BLIP, RAPPOR, DP-JL) | R2-W1 | Sec. 2 | **Partly correct** | Cannot be checked offline; the lines of work are relevant but concern local-DP or JL settings, so "novel" is overstated in degree, not wrong |
| Attack examples violate the promise | R3-W2, DA-M5 | Sec. 1 (0^n, e_j) vs Thm. 1.1 | **Verified** | |
| Sec. 4 intro defines t inconsistently | R1-ERR-11, R4-W3 | Sec. 4 intro | **Verified** | |
| "No experiments" as a weakness | R4-W4 | whole paper | **Overstated** if read as a defect | Acceptable for a theory paper; a sanity check is optional |
| Laplace baseline sensitivity (R2-W4a) | R2 | Sec. 4 intro | **Partly correct** | Valid for the paper's own sketch (2M1 cells), not for "a" generic sketch |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Every Error Log item at MAJOR level checked and held (ERR-1/2/3/4/5; ERR-6 partly); minor overstatement in how strongly W1 depends on the literal reading |
| R2 (Domain) | 3 | 4 | 1.0 | Positioning points reasonable; related-work claims cannot be verified offline; one precision slip (W4a) |
| R3 (Perspective) | 4 | 3 | 1.0 | Points on promise and privacy notion verified; rating rests on not auditing Appendix B, which is expected for this role |
| R4 (Generalist) | 3 | 3 | 1.0 | Notation points verified; "no experiments" slightly overstated; calibration reasonable |
| DA | 2 | 4 | 1.25 | DA-C1 and DA-M1–M4 verified; DA-M6 partly interpretive; numeric table checked |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| DA-C1 | Yes. Theorem 1.2 is half the paper's claimed contribution; the paper's own Lemma B.4 case z = 0 fails for its own construction at i ≠ j, which is how Algorithm 2 calls it, and the probability bound for the test is not derived. This meets the strict criterion that the paper's own results (its lemma and construction) contradict the claim, not merely that an experiment is missing. Repairing it probably changes the construction and the stated bounds | **Upheld** | Redesign / new analysis (not clarification or minor additions) |

### Final Decision and Justification
The reviewers' ratings are 3, 3, 4, 3, 2 (official mean 3.00). The EIC-weighted rating is 2.92, so the starting point is **3 (Borderline Reject)**. The composite cross-check agrees (official 51.8, EIC-weighted 50.9, band 3, no ⚠), and the ICLR-weighted composite is 50.6. The upheld DA-CRITICAL issue sets a ceiling of **3** because the repair needs a redesign; the final decision is **3**, so no departure from the starting point and no ceiling conflict. My own pool position for this paper is **better than about 40% of ICLR submissions**: the Hamming part is a correct but modest result whose headline bound is overstated by constants in an exponent and is non-trivial only for large ε, and the edit-distance part is not established by its proofs. Weaknesses that many accepted theory papers share (no experiments, a narrow promise, typos) did not drive this decision; the unproven main theorem and the overclaimed regime did. If the authors supply a shift-invariant LCP construction with honest costs, fix the Hoeffding/threshold analysis, state explicit constants and the non-trivial ε regime, and account for composition in Remark 4.8, I would expect the paper to move to Borderline Accept. This is how a careful panel would likely see this draft, not a prediction of the real outcome.

---

## Score Summary

### Official Scores and EIC Assessment

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|---------------------------|--------|
| Technical Rigor | 42 | 50 | 62 | 50 | 36 | 48.0 | 46.6 | 26 ⚠ |
| Clarity & Presentation | 62 | 64 | 68 | 60 | 58 | 62.4 | 62.1 | 10 |
| Novelty & Originality | 52 | 50 | 62 | 55 | 48 | 53.4 | 52.7 | 14 |
| Significance & Impact | 48 | 50 | 60 | 52 | 44 | 50.8 | 50.0 | 16 |
| Experimental Validation | 32 | 35 | 45 | 40 | 30 | 36.4 | 35.5 | 15 |
| Reproducibility | 55 | 58 | 62 | 58 | 50 | 56.6 | 56.0 | 12 |
| Ethical Compliance | 65 | 65 | 66 | 62 | 60 | 63.6 | 63.5 | 6 |
| **Composite** | 48.9 | 51.8 | 61.0 | 52.9 | 44.3 | **51.8** (before) | **50.9** (after) | |
| Pool position (P%) | 38 | 45 | 66 | 52 | 28 | | | |

Reviewer weights (confidence × EIC weight): R1 24%, R2 19%, R3 16%, R4 16%, DA 24%.

**Official ratings:** R1 3, R2 3, R3 4, R4 3, DA 2 → mean **3.00**. **EIC-weighted rating:** **2.92** → starting point **3**. **DA-CRITICAL cap:** 1 upheld (DA-C1) needing redesign → cap 3. **Final (EIC): 3.**

### Target-Venue Scores (ICLR 2026, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 1 / 3 / 2 |
| Rating | **4 on {0,2,4,6,8,10}** (5 on the older {1,3,5,6,8,10} scale); both are the script's mapping of final Overall 3 |
| Venue-weighted composite | 50.6 |

The ICLR rating scale is labelled "secondary" in `references/venue_profiles.md`; do not read it as official wording.

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "On Differentially Private String Distances" to ICLR. The question of releasing a private, fast-to-query structure for Hamming and edit distance under unlimited queries is well chosen.

**Overall Assessment:** The panel found a clean model, a correct privacy proof for the Hamming structure, near-optimal running times, and an interesting reduction from a noisy LCP oracle to edit distance. The panel was concerned that the edit-distance theorem is not established by the proofs in Appendix B and that the utility guarantees are non-trivial only for large ε.

**Key Strengths Identified by Reviewers:**
1. Function-release model and privacy proof for the Hamming structure (R1, R3, R4).
2. Running time within polylog of the non-private k-bounded optimum (R2, R3).
3. The noisy-LCP-to-edit-distance reduction (R1, R2, R3).

**Key Concerns Requiring Attention:**
1. The DP-LCP construction compares sketches at different offsets, the Hoeffding step in Lemma B.5 does not give the stated probability, and the threshold uses a different flip rate (R1, DA; DA-CRITICAL, upheld).
2. The error bound is non-trivial only for ε ≳ log k·loglog k, and constants inside the exponent differ from the stated bound (R1, R2, R3, R4, DA; CONSENSUS-4).
3. Remark 4.8's boosting ignores composition; the edit-distance statement of 1−β has no argument (R1, DA).

**Critical Challenge (Devil's Advocate):** Theorem 1.2 rests on Theorem 5.1, whose proof compares sketches in a way the construction does not support. Without a repaired LCP structure with a re-derived cost, the edit-distance half of the contribution stands unproven.

**Decision: Borderline Reject (3)** (ICLR rating 4 on the {0,2,4,6,8,10} scale in the script's secondary mapping).

The decision turns on the upheld critical issue: a repair needs a redesign and new analysis, not a clarification. A revision with a repaired LCP construction, consistent constants, an explicit non-trivial-ε regime, and composition accounted for would be a Borderline Accept candidate. Please see the Revision Roadmap.

Sincerely,
Prof. Helena Marchetti-Sato (fictional persona)
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Non-trivial utility only for large ε; abstract overclaims | R2, R3, R4, DA (+ R1 partly) | CONSENSUS-4 |
| Promise max_i D ≤ k too strong / unspecified outside | R2, R3, DA | CONSENSUS-3 |
| Notation and statement slips | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Whether the proofs are sound enough for acceptance | R3 (4) | R1, DA | R3 did not audit Appendix B; the EIC verified R1/DA's points, so R3's rating is down-weighted by role, not by weight |
| Absence of experiments | R4 (optional sanity check) | R1/R2 (no baseline comparison, no lower bound) | The EIC treats lack of experiments as acceptable for theory, and the lack of any baseline comparison or lower bound as a moderate gap |

### Score Spread Discussion
Technical Rigor spread 26 ⚠: R3 (62) and R4 (50) vs R1 (42) and DA (36). The gap comes from audit depth: R1 and DA re-derived Appendix B and found verified errors; R3 relied on a surface read. The EIC adopts the audited view for this dimension.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-C1 | CRITICAL | Theorem 5.1/1.2 not established (offset sketches; Hoeffding; threshold) | Yes (R1-W1, W2) | **Upheld** | Redesign / new analysis |
| DA-M1 | MAJOR | Strong-privacy framing vs ε regime | Yes (R2, R3, R4) | n/a | n/a |
| DA-M2 | MAJOR | Composition in Remark 4.8 | Yes (R1) | n/a | n/a |
| DA-M3 | MAJOR | Constants in exponent | Yes (R1) | n/a | n/a |
| DA-M4 | MAJOR | Adaptive queries in union bound | Yes (R1) | n/a | n/a |
| DA-M5 | MAJOR | All-strings-within-k promise | Yes (R2, R3) | n/a | n/a |
| DA-M6 | MAJOR | Utility per fixed query | Yes (R1-W6) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Sketches of A[i:i+L] and B[j:j+L] are not comparable for i ≠ j | DA-C1, R1-W1 | App. B, Alg. 3–4, Lemma B.4; Thm. 5.1/1.2 | Shift-invariant fingerprint or per-diagonal trees with honest complexity; re-derive B.4–B.6; restate Thm. 1.2 | High (theory work, days–weeks; no compute) | Partly (a corrected construction and statement; full proof may exceed a week) |
| R2 | Hoeffding step and threshold mismatch in the LCP test | DA-C1, R1-W2 | App. B.3 Lemma B.5; Alg. 4 line 8; Alg. 1 line 26 | Chernoff-based analysis, threshold matched to the true flip rate, state ε regime | Medium–High | Yes (analysis) |
| R3 | Error bound constants in the exponent | R1-W3, DA-M3 | Lemma 4.7; Lemma 5.8; Thm. 1.1/1.2 | Restate bounds with explicit constants or rescale the flip probability | Low–Medium | Yes |
| R4 | Composition in the 1−β boosting | R1-W4, DA-M2 | Remark 4.8; Thm. 1.1/1.2 | Split ε across copies; restate; give the argument for edit distance or restrict to constant β | Low–Medium | Yes |

*R2–R4 are Priority 1 because the EIC verified that they change a stated bound of a main theorem (Roadmap rule: issues verified as undermining a main claim).*

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Non-trivial regime and abstract wording ("strong privacy", "exponentially small") | DA-M1, R2-W2, R3-W3, R4-W2 | State the regime ε ≳ log k·loglog k; compare with the trivial k/2 and with JL-style/RR baselines; one numeric table | Low | Yes |
| S2 | Adaptive queries and all-pairs union bound | DA-M4, R1-W5 | All-pairs guarantee (restating the exponent) or an adaptive argument | Medium | Partly |
| S3 | All-strings-within-k promise; behavior outside | DA-M5, R2-W3, R3-W2 | Thresholded "≤k or ⊥" variant; discuss applications | Medium | Partly |
| S4 | Fixed-query utility, public fully random hash functions and their storage | DA-M6, R1-W6 | State non-adaptive utility; specify limited-independence hashing and space | Medium | Yes |
| S5 | Missing related work on private similarity sketches | R2-W1 | Add BLIP, RAPPOR, DP-JL lines; differentiate (verify citations first) | Low | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Notation and statement slips (Dham equality, footnote 1 index, recurrence, t, Alg. 3 ε = 0, Init time, Lemma 4.5 constant, T_j definition) | R1 Error Log, R4-W3, DA-m1–m6 | One careful pass; fix the recurrence and base cases |
| N2 | Bit-level vs record-level privacy | R3-W1 | Add a clarifying paragraph |
| N3 | Technical overview and venue relevance | R4-W1 | Half-page overview; one sentence on the ICLR audience |
| N4 | Optional small simulation of Algorithm 1 | R4-W4 | A few (k, ε) values |
| N5 | Lower bound / packing argument | R2-W2 | State a baseline lower bound (see Missing References) |

---

## Estimated Revision Effort
- Priority 1: 4 items; roughly 2–4 weeks of theory work (R1 dominates; no compute).
- Priority 2: 5 items; roughly 1–2 weeks.
- Priority 3: 5 items; a few days.
- **Total estimated revision time**: about 1–2 months for a convincing resubmission.

---

## Journal-style recommendation
Not applicable (conference target).

## Post-Review Analysis
Not requested (Gap Scout not run).
