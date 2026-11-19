# Simulated Panel Review: "G-KV: Decoding-Time KV Cache Eviction with Global Attention"

*Skill: academic-paper-reviewer v2.10.1, full mode. Date: 2026-11-10. This is a simulation of how a careful panel would likely see this draft, not a prediction of any real outcome. Reviewer personas are fictional. Figures were not available: figure-dependent claims are judged from captions, axis text and surrounding prose only, and this is stated where it matters.*

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | G-KV: Decoding-Time KV Cache Eviction with Global Attention |
| Primary Discipline | Machine learning → efficient LLM inference (KV cache compression for long-CoT reasoning models) |
| Secondary Discipline(s) | RL post-training for LLMs; sparse attention; ML systems |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Attention-score-based KV eviction with an exponentially decayed historical ("global") score; redundancy score from R-KV; GRPO with the real eviction mask ("RL-Sparse"); KL distillation under a sparse mask |
| Target Venue | ICLR (stated by the user; 2026 cycle, scale status *secondary*); profile key `iclr` |
| Venue-Specific Notes | none (ICLR: Soundness/Presentation/Contribution 1–4, Rating, Confidence; public discussion with revisable PDF) |
| Paper Maturity | Submission-ready draft (the footer reads "Published as preprint paper"; no limitations section) |
| Ethics-Relevant Content | none (no human data, no deployment-risk content; LLM-use disclosure in Appendix A) |
| Literature check | **strict**, cutoff 2025-09-24, requested. The arXiv API was unreachable (HTTP 429, then 503; 1 query logged, 0 results). Per the skill, Phase 1.5 falls back to knowledge with `[verify]`. No search-based labels (prior / recent / concurrent) exist; every reference below is from the reviewers' knowledge. |
| Integrity scan | `integrity_scan.py` on the full text: no reviewer-directed text, no hidden characters. Reviewers read the (identical) redacted copy. |

### Claimed Contributions (as stated by the authors, §1 and Abstract)
1. **C1**: a "simple and effective global score" combining local attention with historical scores for decoding-time eviction; "improves other methods by 5% to 20%" at a 512-token budget (§1, §5).
2. **C2**: an RL framework (RL-Sparse) that samples with the compressed cache and trains with the matching sparse attention mask, "significantly superior" to RL on the full cache (§1, §6, §7.4).
3. **C3**: a distillation-style alternative for tasks without verifiable rewards (Appendix C, §7.4).
4. **C4** (implied by §7.5/App G): large throughput and memory gains ("up to 12.18× and 19.7×", "approximately a 90% reduction").

### Paper memory (shared factual record)
- **Setup:** DeepSeek-R1-Distill-Qwen-7B and -Llama-8B (§7.1); AMC 2023 (16k max length), AIME 2024 (32k), LiveCodeBench (version/length not stated); pass@1 from 32 samples at T=0.6, top-p 0.95 (§7.1). Compression every s=128 tokens, window w=16, budget b=512 in the ablation (§7.2); budgets 256–2048 in main results (Figs. 5–6).
- **Hyperparameters:** α from a sweep on AMC 23 (Fig. 4, §7.2) → α=0.8 (§7.3); λ re-tuned for the redundancy mix (App D, Fig. 12): 0.7 (Qwen), 0.9 (Llama). Baselines: "other parameters follow the settings specified in their respective papers" (§7.3).
- **Training (§7.4, App C, E):** DeepScaleR-40k; RL: 16 questions × 8 responses, 400 steps, max length 4096, reward 0/1, no KL term (§6); distillation: 27k correct samples, 250 steps, batch 128, lr 1e-6; RL-Sparse uses G-KV at budget 2048; evaluation capped at 4096 tokens.
- **Headline numbers:** Table 1 (AMC/AIME pass@1 at budgets 512/1024/2048); Table 2 throughput; Tables 3–4 compression time; App G memory (2.18/3.93/7.43 GB; 96.1/92.9/86.7%).
- **Main comparisons (Figs. 5, 6, 18, 19) are figures only; no numeric table.** Not readable here.
- **Appendix adds:** attention sparsity (B), distillation loss (C), integration with SnapKV/R-KV (D), training curves (E), decoding-time vs batch size (F), memory (G), Llama-8B results (H), a speculative "wait"-token discussion (I), one case study (J).
- **Not available / unverifiable:** all figure content (Figs. 1, 4–8, 11–19); equation extraction is legible.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Halvard Okonkwo-Reyes, large public research university (Europe)
- **Seniority / Expertise**: senior faculty / efficient transformers, LLM inference, area chair experience at ML venues
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: judges against what the venue actually accepts; asks whether any single issue is fatal

### Reviewer 1 (Methodology): Dr. Katarzyna Elmsworth, industrial research lab (Europe)
- **Seniority / Expertise**: senior industry scientist / LLM evaluation protocols, RL post-training for reasoning
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: insists on matched tuning effort and held-out selection

### Reviewer 2 (Domain): Prof. Daichi Morwenna, LLM inference group, public university (East Asia)
- **Seniority / Expertise**: mid-career faculty / KV cache eviction and sparse attention, long-context benchmarks
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: checks each novelty claim against the closest prior method

### Reviewer 3 (Perspective): Dr. Amara Tessler-Quispe, computer-architecture and systems group, university (South America)
- **Seniority / Expertise**: postdoc / memory hierarchies and cache replacement, GPU serving systems
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: constructive, looks for what the work could connect to

### Reviewer 4 (Generalist): Dr. Jonas Ferreira-Lindqvist, ML group, mid-size research university (North America)
- **Seniority / Expertise**: mid-career / deep learning broadly, not LLM efficiency specifically
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: typical program-committee member; weighs weaknesses against contribution

### Devil's Advocate: Prof. Yusra Halloran-Baek, evaluation methodology and statistics, university (Oceania)
- **Seniority / Expertise**: senior faculty / experimental design, causal attribution in ML comparisons
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: rigorous, never hostile

*Personas are fictional. Proceeding with the stated assumptions (target venue ICLR, paper type empirical).*

---

# Phase 1: Independent Reviews

*Five role-based passes in one model context (no subagents were launched); each report below was written from the reviewer copy and the paper memory only, without the other reports.*

---

# Peer Review Report (Reviewer 1)

## Paper: G-KV: Decoding-Time KV Cache Eviction with Global Attention
## Reviewer: Dr. Katarzyna Elmsworth, Methodology (industrial research lab, Europe; fictional persona)
## Expertise: LLM evaluation protocols; RL post-training for reasoning; efficiency measurement
## Date: 2026-11-10

---

## Summary
The paper studies decoding-time KV cache eviction for long chain-of-thought models. It argues that scores from a single recent observation window (§4) lose tokens that matter later, and proposes a score that is an exponentially decayed running combination of per-window attention (max, mean or sum form, Eqs. 3–5), usually mixed with R-KV's redundancy score. A second component trains the model under the actual eviction mask, with GRPO ("RL-Sparse", §6) or with KL distillation (App C). Results are reported on AMC 23, AIME 24 and LiveCodeBench with two distilled reasoning models, plus throughput and memory analyses.

## Protocol sweep (split and selection statements)
- Selection of α: "This range is recommended as the optimal hyperparameter setting." (§7.2, Fig. 4, whose caption names the AMC 23 benchmark). Then "and we set α to 0.8" (§7.3). AMC 23 is also reported in the main results (Fig. 5, left panel) and in the headline "nearly a 20% improvement" (§7.3).
- Selection of λ: "we re-tune the hyperparameter λ instead of directly adopting the value" (App D); the benchmark behind Fig. 12 is not stated.
- Baselines: "other parameters follow the settings specified in their respective papers" (§7.3).
- Train/validation/test: AMC 23 and AIME 24 have no separate validation split in the paper; the RL "validation set" is 32 questions drawn from the *training* set (App E). Seeds, run counts, RL learning rate and clip ε: not stated after search (the sentence "The learning rate is set to 1 × 10⁻⁶" sits in the distillation paragraph, §7.4).

## Strengths

### S1: A clean, plug-in scoring idea with a well-specified algorithm
§3 gives a unified framework (Eqs. 1–2) and §5 defines three update rules (Eqs. 3–5), including the handling of newly entering tokens and the first step. Appendix D shows how the score replaces SnapKV's or R-KV's local score. A reader can implement it.

### S2: The sparse-mask RL training is a real engineering contribution with a sensible design principle
Sampling under the compressed policy and training with the recorded mask (§6) removes a train/inference mismatch, and Appendix G is candid about the mask memory cost (14 GB in the stated example) and the offloading workaround. Table 1 compares against an RL baseline trained on the full cache (RL-Full), which is the right control.

### S3: Efficiency is measured, not assumed, and overheads are reported
Table 2 gives measured throughput at several batch sizes with OOM entries, Tables 3–4 report the extra compression time of the global score (about 5 ms per step), and Appendix G derives memory arithmetic that I recomputed and found correct.

### S4: A direct ablation of the central component exists
Fig. 4 compares global score forms and α against a purely local score (MorphKV) and a CAKE-style shift score, with the redundancy term absent. This is the most controlled evidence in the paper.

## Weaknesses

### W1: Hyperparameters are selected on a reported benchmark, and baselines are left at defaults (E4; MAJOR)
α is swept and chosen on AMC 23 (§7.2, Fig. 4), then AMC 23 supplies the largest headline gain (§7.3; §1 "improves other methods by 5% to 20%"). λ is re-tuned only for G-KV (App D), while R-KV and the others use paper defaults (§7.3). AMC 23 is a 40-problem test benchmark without a validation split. Because the α plateau is wide (§7.2: "relatively stable when α ∈ [0.8, 0.9]") and AIME 24 / LiveCodeBench use the same α without further tuning, I do not think the qualitative conclusion depends on this, but the size of the AMC 23 gap does.
- **Suggested Fix:** choose α and λ on a held-out set (e.g., 200–500 DeepScaleR problems not used for training) and report AMC/AIME/LCB once; give R-KV, MorphKV and SnapKV the same sweep budget (their λ/pooling/window). Roughly 3 α × 3 λ × 2 models × 3 baselines at 40 problems × 32 samples is on the order of 100–150 GPU-hours on A100-class hardware.

### W2: The gain is not attributed to the global score (E4; MAJOR)
"G-KV" is defined as the global score *plus* R-KV's redundancy score (§7.3), with a new max-normalisation of both terms and a re-tuned λ (App D). The only clean comparison of global vs. local scores is Fig. 4 (AMC 23, no redundancy, one model per panel). The comparisons that carry the headline (Figs. 5, 6, 18, 19) change several things at once relative to R-KV.
- **Suggested Fix:** a 2×2 grid {local, global} × {no redundancy, redundancy} on AMC, AIME and LCB at 512/1024 budgets, and R-KV with the same normalisation. About 8 configs × 3 benchmarks × 2 models.

### W3: No variance anywhere, on very small benchmarks (E8; MAJOR)
"we perform sampling 32 times to estimate the pass@1 score" (§7.1) reduces sampling noise but not problem-set or training noise. AMC 23 and AIME 24 have roughly 40 and 30 problems. Table 1 reports one trained model per row; the AIME 24 gaps of RL-Sparse over RL-Full are 1.57, 1.04 and 0.73 points (recomputed from Table 1; derived). Also, Distill beats RL-Sparse at AIME 512 (14.27 vs 13.75).
- **Suggested Fix:** paired bootstrap over questions with 95% CIs for every main comparison; at least 3 training seeds for Table 1 (RL-Full and RL-Sparse, 400 steps each; order of 60–100 GPU-hours per seed pair depending on hardware).

### W4: The training comparison (Table 1) lacks the reference points needed to read it (E4; MAJOR)
(i) No full-KV row for the untrained or trained models at the 4096-token cap, so the claim that RL-Sparse "minimizes the training-inference discrepancy" (§7.4) cannot be read as "closes the gap to full cache". (ii) Training and evaluation both use a 4096 cap (§7.4): RL may mostly teach shorter reasoning; RL-Full controls this in part, but output-length statistics and the truncation rate (advantage zeroed for truncated samples, §6) are not reported. (iii) RL-Sparse is trained at budget 2048 only and evaluated only with G-KV. (iv) "significantly outperforming models trained with the Full KV cache" (§7.4) is stated without a test.
- **Suggested Fix:** add Full-KV rows, mean output length and truncation fraction per method, one cross-policy evaluation (RL-Sparse model with R-KV), and soften "significantly" or support it with CIs.

### W5: Mechanism analyses are uncontrolled (E5; MAJOR)
(a) Observation 2 reports overlap with a union of three earlier windows: "even when retaining only 55% of the tokens, the overlap approaches 95%" (§4). A union of three random 55% sets already covers 1 − 0.45³ ≈ 0.909 of the tokens (derived), so a null is needed to read 95%; and Fig. 1's regime (kept rate 0.6–0.9 from the axis text; not verifiable from the extraction) is far from the ~3–10% retention used in §7.3. (b) The token-retention ratio is "calculated exclusively for cases where the model generates the correct answer" (§7.3) and then read as "the tokens retained by our method have a higher information density". A method that solves more hard (longer) problems has a lower ratio mechanically, so the metric is confounded with accuracy. (c) The Fig. 7 explanation (RoPE, semantic similarity) is asserted, not tested.
- **Suggested Fix:** random-set and shuffled-window nulls at the deployed retention; report the ratio on the intersection of problems all methods solve, or drop the "information density" claim.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E4 | §7.2 + §7.3, Fig. 4/5 | "This range is recommended as the optimal hyperparameter setting." | α chosen on AMC 23, which also supplies the headline gain; baselines left at defaults | Cross-referenced Fig. 4 caption (AMC 23), §7.3 ("we set α to 0.8"), Fig. 5 | High | MAJOR | Held-out selection; equal tuning |
| ERR-2 | E5 | §4, Observation 2 | "even when retaining only 55% of the tokens, the overlap approaches 95%" | Chance level for a 3-window union at 55% is about 0.91 | Derived: 1 − 0.45³ = 0.909 | High | MAJOR | Add null baseline |
| ERR-3 | E5 | §7.3 | "This ratio is calculated exclusively for cases where the model generates the correct answer." | Conditioning on correctness confounds the metric with accuracy; supports no "information density" claim | Derived from the metric definition | Medium | MAJOR | Intersection-of-solved analysis |
| ERR-4 | E1/E6 | §7.5 vs Table 2 | "is approximately 40% of that of Full-KV" | Table 2 implies 62.41/261.32 ≈ 24% (batch 32, budget 512); §7.5/App F also say decoding time is "similar" across budgets while Table 2 throughput differs 261.32 vs 170.64 | Recomputed ratio; cross-referenced Fig. 8 text, App F, Table 2 | Medium (depends on equal token counts) | MINOR | State output lengths; reconcile |
| ERR-5 | E7 | §7.1 vs References | "Qwen 2.5 (Team, 2024)" | The bibliography entry is the "Qwen2 technical report" | Cross-referenced text and reference list | High | MINOR | Cite the Qwen2.5 report |

### Claim-to-evidence map (key claims)
| ID | Claim | Where stated | Evidence | Verdict |
|----|-------|--------------|----------|---------|
| C1 | Global score "significantly enhances performance", 5–20% at b=512 | §1, §5, §7.3 | Fig. 4, 5, 11 (figures only) | Partially: supported in direction on 2 models; α tuned on AMC 23; no variance; attribution unclear |
| C2 | RL-Sparse "significantly superior" to RL-Full | §1, §7.4 | Table 1 | Partially: AMC gaps 3.4–4.9 points, AIME gaps 0.7–1.6; single run |
| C3 | Distillation is a practical alternative | §7.4, App C | Table 1 (Distill rows) | Supported modestly (+1.6 to +2.9) |
| C4 | Up to 12.18× / 19.7× throughput, ~90% KV memory saving | §7.5, App G | Table 2, App G | Supported for the stated implementation; stack and equal-accuracy comparison unverified |
| C5 | Retained tokens have "higher information density" | §7.3 | Figs. 6, 7 | Not tested |

**Recomputation.** Table 1 deltas in parentheses all match (e.g., 51.01 − 45.00 = 6.01; 13.75 − 11.56 = 2.19). Table 2 ratios: 261.32/62.41 = 4.19 (text 4.18), 760.74/62.41 = 12.19 (text 12.18; compares batch 128 with Full-KV at batch 32 because larger batches OOM), 612.60/31.08 = 19.71 (text 19.7). App G: 28×128×2×16384×2×2 B ≈ 0.44 GB; (512+128)/16384 → 96.1% saving. These match up to truncation.

## Reproducibility (mine to score)
Present: budgets, s, w, α, λ, GRPO group sizes, step counts, sampling parameters, memory arithmetic, a code link ("The code of this paper is available on:"; link removed). Not stated: seeds, RL learning rate and clip ε, training hardware and time, LiveCodeBench version and length cap, the serving stack behind Table 2, whether R-KV's λ was re-tuned.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Sound idea, but tuning on a reported benchmark and no variance weaken the evidence |
| Clarity | 2 | Algorithm clear; main results exist only as figures |
| Significance | 2 | Useful if it holds up; scope is narrow |
| Originality | 2 | Decayed accumulation of attention is close to known history-based eviction |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline gain is measured on the benchmark used to select α, against untuned baselines, without variance, and the gain is not isolated from the redundancy term.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Sound mechanics; selection and attribution gaps; uncontrolled mechanism analyses |
| Clarity & Presentation | 60 | Competent | Method clear; results only in figures |
| Novelty & Originality | 50 | Developing | Incremental over history-based eviction plus R-KV |
| Significance & Impact | 56 | Competent | Practical interest, narrow evidence |
| Experimental Validation | 46 | Developing | Three benchmarks, two models, but no variance and tuned-vs-default asymmetry |
| Reproducibility | 58 | Competent | Many details; seeds, RL optimiser details, stack missing; code promised |
| Ethical Compliance | 60 | Competent | Nothing at stake; no limitations section |

## Questions for Authors
1. Was R-KV's λ (or SnapKV's pooling, MorphKV's window) re-tuned in your setting? Equal sweeps would raise my Experimental Validation score; a held-out selection of α/λ that preserves the AMC gap would raise it further.
2. Which benchmark is Fig. 12 computed on, and is α=0.8 the best-scoring value in Fig. 4?
3. What are the RL learning rate, clip ε, hardware and wall-clock, and how many training seeds exist for Table 1?
4. Which LiveCodeBench version, date range and length cap were used, and can Fig. 5/6/18/19 be given as tables with CIs?
5. How do the 4.18× throughput (Table 2) and "approximately 40%" decoding time (§7.5) reconcile, i.e., what are the mean output lengths per method?

## Limitations Assessment
**Partially.** There is no limitations section; Appendix F notes a decoding-time/batch-size trade-off and App E notes reduced exploration. Add scope limits (two 7–8B distilled models, math and code, 4096-token training cap).

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: a plausible, practical idea with a useful training component, but the headline evidence is tuned on the reported benchmark against untuned baselines and has no variance.

## Confidence
**4**: I checked the arithmetic and the protocol statements; I could not see the figures.

**Minor:** "StreamLLM" label in Figs. 6/19 vs "StreamingLLM"; "GKV" vs "G-KV" in §7.5; "DeepSeek-Qwen-Llama-8B" in §7.5.

---

# Peer Review Report (Reviewer 2)

## Paper: G-KV: Decoding-Time KV Cache Eviction with Global Attention
## Reviewer: Prof. Daichi Morwenna, Domain (LLM inference group, public university, East Asia; fictional persona)
## Expertise: KV cache eviction; sparse attention; long-context and reasoning benchmarks
## Date: 2026-11-10

---

## Summary
The submission improves attention-based KV eviction during decoding by keeping a decayed memory of per-window attention, so a token attended earlier survives a window in which it is quiet. It combines this with R-KV's redundancy score and offers sparse-mask RL and distillation to adapt the model to eviction. It positions itself against prefill-time methods (SnapKV, PyramidKV, Ada-KV, HeadKV, KVzip) and decoding-time methods (H2O, MorphKV, R-KV, CAKE, Song et al.).

## Strengths

### S1: The gap is real and well chosen
Long-CoT outputs dwarf prompts, so prefill-only compression gives "only marginal benefits" (§1). Decoding-time eviction under a fixed budget is where current reasoning-model efficiency work sits, and §2/§3 give a clean unified description of MorphKV, R-KV and Song et al.

### S2: Compatibility with existing methods is demonstrated
App D shows the score can replace SnapKV's local score (Fig. 11) and be mixed with R-KV's redundancy score (Fig. 12), and is honest that SnapKV's pooling does not help in decoding.

### S3: Training adaptation for eviction is a worthwhile direction
Few eviction papers ask whether the model itself should be adapted; §6 and Table 1 give a first reasoning-model result with an RL-Full control.

## Weaknesses

### W1: The core mechanism is close to history-based eviction that is cited but not compared (Novelty; MAJOR)
§2 says H2O "uses the accumulated attention received by each token as its score", then dismisses it in one clause. The "sum" form of Eq. 5 at α=1 is H2O-style accumulation, and the persistence-of-importance idea behind it (Scissorhands, NeurIPS 2023; see Missing References) is the same premise as §4. The novelty is the decay, the max-normalisation and the decoding-time window, which is a modest delta. H2O is not in the §7.3 baseline list ("StreamingLLM ..., MorphKV ..., and R-KV", plus an adapted SnapKV).
- **Suggested Fix:** run H2O and an α=1 sum variant as baselines in §7.3, and state the delta to history-based methods explicitly in §2.

### W2: Related work misses the training-for-eviction line (Novelty/positioning; MAJOR)
C2/C3 are presented against pre-training sparse attention (§1: Xiao et al., Chen et al.) and Nawrot et al. (cited only as merging, §2). Work that retrofits a pretrained model to learn which tokens to evict or attend to, and trained sparse-attention gates for reasoning models, is the natural comparator and is not discussed (see Missing References, marked `[verify]`).
- **Suggested Fix:** add a related-work paragraph and, if code exists, one comparison against a retrofit method at matched budget.

### W3: "Global" is a short-horizon decayed memory; the motivating analysis does not match the deployed regime (Theory/motivation; MAJOR)
From Eqs. 3–5, a token's historical contribution is scaled by α per compression step, so at α=0.8, s=128 the effective horizon is 1/(1−α) = 5 steps ≈ 640 generated tokens (derived), against 16k–32k generation lengths (§7.1). §4 supports "long-term importance" with four windows inside the last 512 tokens, and Observation 2 lacks a chance baseline (a union of three random 55% sets covers ≈ 0.91, derived). The human-memory analogy (§5) motivates but does not test the design.
- **Suggested Fix:** call it "decayed" or "multi-window" score, or show a long-horizon analysis (reuse distance of attention over thousands of tokens) and a null.

### W4: Descriptions of prior work should be checked (Citation, E7; MINOR/MAJOR as noted)
(i) "Qwen 2.5 (Team, 2024)" points to the Qwen2 technical report in References. (ii) §7.2 uses "the attention variance within a local window" as a stand-in for CAKE and compares only that score; CAKE as a method also allocates budgets across layers, so "perform notably better than the attention shift score in CAKE" (§7.2) is a statement about a component, not CAKE. I could not verify CAKE's exact definition against its abstract here, so I raise it as a question rather than an error.
- **Suggested Fix:** correct the Qwen citation; label the CAKE comparison "CAKE-style shift score" everywhere and, if possible, run the full method.

## Questions for Authors
1. Is the α=1 sum variant (Eq. 5) equivalent to H2O's accumulated score in your framework, and how does it perform on AIME/LCB? If H2O/Scissorhands-style accumulation is competitive, my Novelty score drops; a clear delta would raise it.
2. How does RL-Sparse relate to retrofitting methods that learn to evict, and would the same rollouts work with R-KV's policy (cross-policy generalisation)?
3. Do AMC 2023 and AIME 2024 refer to the 40-problem and 30-problem sets? The references cite "2023 amc 8 – aops wiki" and "2024 aime i – aops wiki", which would be different (smaller or different-level) sets.

## Literature-check addendum (strict mode requested; search unavailable)
The arXiv API returned HTTP 429/503, so there is no ledger, no kept results and no novelty profile. The table below is built from the paper's own related work and my knowledge; uncertain entries are `[verify]`. No prior/recent/concurrent label exists, so none of this can be a required comparison under the skill's rules beyond what the paper itself cites (H2O).

| Claimed contribution | Closest prior work | What that work already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|-----------------------------|------------------|---------------------------|
| C1 global score | H2O (Zhang et al., NeurIPS 2023, cited); Scissorhands (Liu et al., NeurIPS 2023, not cited) | Accumulate attention across steps to find persistent heavy hitters | Decay, max-normalisation, windowed observation at decode time | H2O cited, dismissed in one clause, not run; Scissorhands not cited |
| C2 sparse-mask RL | Retrofitting for learned eviction (Nawrot et al. 2024, cited as merging; Łańcucki et al. 2025 `[verify]`) | Train the model to tolerate/learn compression | GRPO with real eviction mask and a verifiable reward on reasoning models | Partly (Nawrot cited as merging) |
| C3 distillation | Knowledge distillation (Hinton et al., cited) | Soft-target KL | Applied under a sparse mask | Yes |

**Per-claim novelty (from knowledge, no search):** C1 *incremental* (level ~4 against history-based eviction); C2 *medium* (level ~3); C3 *incremental*. This is a claim-level finding, MAJOR at most, not "known results".

**Baseline scout (by knowledge):** on AMC/AIME with R1-distilled models the relevant decoding-time baselines are R-KV, MorphKV, H2O/TOVA-style methods, SnapKV-adapted. H2O and a TOVA-style last-token policy are the notable absentees. No under-reported baseline can be checked without the baselines' own numbers in this setting.

**Field snapshot (knowledge only, as of the cutoff).** Three years ago eviction meant heavy-hitter accumulation (H2O, Scissorhands) and attention sinks (StreamingLLM) for long prompts. With long-CoT reasoning models in 2025, the problem moved to decoding time under a fixed budget (R-KV, MorphKV, Song et al.), where redundancy and recency windows dominate. Current evaluation uses AIME/AMC/MATH-style pass@1 with distilled 7–8B models and budgets of 512–4096 tokens; larger models and Qwen3-class models are the natural next step. Open problems: reliability at long horizons, interaction with serving systems, and model adaptation. What counts as significant now: a clear accuracy gain at a fixed budget on several models and benchmarks with fair baselines, or a new capability (adapting the model) shown beyond a single configuration. A few points on a 40-problem set at one budget is incremental.

## Missing References
*Citation-integrity rule applied: only references I am confident exist; others marked `[verify]`.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Important | Zichang Liu et al., "Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time", NeurIPS 2023 | Same premise as §4 (tokens important earlier stay important); history-based eviction |
| Important | Matanel Oren et al., "Transformers are Multi-State RNNs" (TOVA), EMNLP 2024 | Decoding-time eviction by last-token attention; natural baseline for the local-score family |
| Important | Muhammad Adnan et al., "Keyformer: KV Cache Reduction through Key Tokens Selection for Efficient Generative Inference", MLSys 2024 | Decoding-time score design with regularised accumulation |
| Important | Łańcucki et al., "Inference-Time Hyper-Scaling with KV Cache Compression", 2025 `[verify]` | Trains/retrofits models for compressed KV cache on reasoning tasks |
| Helpful | Gao et al., "SeerAttention-R: Sparse Attention Adaptation for Long Reasoning", 2025 `[verify]` | Adapts reasoning models to sparse attention with a trained gate |
| Helpful | Haoyue Zhang et al., "LazyEviction: Lagged KV Eviction with Attention Pattern Observation for Efficient Long Reasoning", 2025 `[verify]` | Recurrence of token importance in reasoning; discuss only, preprint close to the cutoff |
| Helpful | Jiaming Tang et al., "Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference", ICML 2024 | Non-evicting alternative that avoids permanent loss |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Mechanism OK; baseline set and analysis gaps |
| Clarity | 3 | Related work and framework are clear |
| Significance | 2 | Useful, narrow |
| Originality | 2 | Incremental over history-based eviction |

## Dimension Scores (0–100)
**Pool position:** better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the method is a modest delta over history-based eviction and R-KV, the closest ancestor (H2O) is not run, and the training component is a first but narrowly validated result.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Sound; horizon and null issues |
| Clarity & Presentation | 62 | Competent | Positioning clear, some missing prior work |
| Novelty & Originality | 48 | Developing | Incremental; one component (RL-Sparse) is newer |
| Significance & Impact | 58 | Competent | Practical interest at low budgets |
| Experimental Validation | 50 | Developing | Missing H2O/TOVA-type baselines; narrow models |
| Reproducibility | 60 | Competent | Clear algorithm, code promised |
| Ethical Compliance | 60 | Competent | Nothing at stake; no limitations section |

## Limitations Assessment
**Partially.** See R1; also state the scope of the analysis horizon.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: a practical, readable idea whose conceptual delta over history-based eviction is small and whose closest ancestor is not tested.

## Confidence
**3**: no literature search was possible; novelty judgements rest on my knowledge and are marked `[verify]` where uncertain.

**Minor:** inconsistent method names (G-KV/GKV), "A cases presented" (§7.3).

---

# Peer Review Report (Reviewer 3)

## Paper: G-KV: Decoding-Time KV Cache Eviction with Global Attention
## Reviewer: Dr. Amara Tessler-Quispe, Perspective (systems and architecture group, university, South America; fictional persona)
## Expertise: cache replacement policies; GPU memory hierarchy; LLM serving
## Date: 2026-11-10

---

## Summary
The paper turns KV eviction for reasoning models into a policy with memory: each token carries a decayed attention history, and tokens with weak current but strong past attention are kept. It also trains the model under the resulting sparse attention. The strongest practical claims are large decode throughput gains (Table 2) and a roughly 90% KV memory reduction (App G) with accuracy that approaches full cache at larger budgets.

## Strengths

### S1: A recognisable systems idea applied cleanly
The "decayed score" is essentially a recency-frequency counter, a long-standing family in cache management (see below), and §5 explains its three scenarios clearly (Fig. 2 caption). It adds only ~5 ms per compression step (Table 3; about 1% of decoding time, Table 4).

### S2: Memory arithmetic and overhead are transparent
App G derives KV size (0.44 GB per 16k sequence), the (b+s)/length rule that counts the compression interval, the score cache (about 1/(2d) of KV), and the training-time mask cost. It is unusual and useful to see the mask memory problem written down.

### S3: Practical framing around batch size
§7.5 and App F show that compression enables larger batches and that decoding time per batch grows with batch size; the authors warn against over-large batches.

### S4: The adaptation angle is promising for deployment
Training a model for the cache policy it will actually run under (§6) is the kind of co-design that matters in production; RL-Sparse beating RL-Full at all three budgets on AMC (Table 1) is encouraging.

## Cross-disciplinary connections
- **Cache replacement:** an exponentially decayed access counter that combines recency and frequency is the LRFU family (Lee et al., IEEE Trans. Computers, 2001 `[verify]` year/venue); the "max" form is a leaky peak-hold detector from signal processing. Tuning α corresponds to LRFU's recency/frequency knob, and ARC/TinyLFU-style admission could guard against one-hit tokens. Framing the contribution this way would help both audiences and suggests adaptive α.
- **Signal processing:** exponential smoothing with a max-normalised input is an exponential moving average of normalised spectra; its failure modes (the normaliser being dominated by a single attention sink) deserve a check.

## Assumption audit
1. *Attention mass equals importance.* Scoring ignores value norms and head role; kept tokens are inferred important because they were attended, which is circular for the "information density" interpretation (§7.3).
2. *Short math/code benchmarks with a 16k–32k cap represent deployment reasoning.* No multi-turn, agentic or retrieval-style workloads are evaluated.
3. *Throughput at one stack represents serving.* See W1.
4. *Scale.* Two 7–8B distilled models; the paper's own intro frames the problem for "reasoning models" broadly (§1).

## Weaknesses

### W1: Efficiency evidence lacks serving-stack context and conflates per-token cost with time to solution (MAJOR)
Table 2 gives Full-KV at 62.41 tokens/s for batch 32, i.e., about 1.95 tokens/s per sequence (derived); the inference stack (framework, attention kernel, padding handling) and the A100 memory size are not stated, only "a single A100 GPU" (§7.5). Memory-bandwidth arithmetic for a 7B model at 16k context suggests far higher full-cache throughput on an optimised stack, so the 12.18×/19.7× figures (compared at larger batch sizes because Full-KV OOMs) may partly reflect baseline implementation. Throughput counts valid tokens per second, yet compressed models may produce longer or less efficient outputs (§7.3 token-retention ratio, Fig. 6); the claim "approximately 40% of that of Full-KV" (§7.5, Fig. 8) differs from the ≈24% implied by Table 2. Llama-8B scaling in Table 2 is also odd: G-KV (512) rises from 158.43 (batch 16) to 517.30 (batch 32), 3.27× for a 2× batch (derived).
- **Suggested Fix:** state the stack and A100 variant; add a vLLM-class full-cache baseline if feasible; report time-to-solution at equal accuracy and mean output length.

### W2: The deployment cost of per-head, irregular selection is not discussed (MAJOR/MINOR)
§3 selects different tokens per KV head every 128 tokens. Compatibility with paged KV layouts, prefix caching and fused attention kernels (which may not expose window attention scores) is not discussed; the compression step costs 46–121 ms (Table 3), which at small batch sizes may matter more than "about 1%" (Table 4 is at batch 32).
- **Suggested Fix:** add a short deployment section or limitations paragraph; report Table 3/4 across batch sizes.

### W3: Narrow, single-run evidence behind a broad scalability claim (MAJOR)
"enabling efficient and scalable reasoning for LLMs" (§8) rests on two distilled 7–8B models, AMC 23/AIME 24/LCB, one training run per row (Table 1) and no variance. Larger models (where KV memory dominates) and a second model family trained with RL-Sparse are absent.
- **Suggested Fix:** one 14B–32B evaluation of the training-free method, and either narrow the §8 wording or add seeds.

### W4: Absolute accuracy at low budgets deserves a plain statement (MINOR/MAJOR)
At b=512 even the best method is well under full-KV accuracy for the 7B model in Fig. 5 (read from the plot labels; not verifiable here), so "nearly a 20% improvement" (§7.3) is relative to other compressed methods, not to the uncompressed model. A reader choosing a budget needs the accuracy-vs-memory frontier with full-KV as a reference line in a table.
- **Suggested Fix:** add a table of pass@1 per budget with the full-KV row and the percentage of full-KV accuracy retained.

## Missing References (optional)
LRFU: Lee et al., "LRFU: A Spectrum of Policies that Subsumes the Least Recently Used and Least Frequently Used Policies", IEEE Trans. Computers, 2001 `[verify]`. Also Quest (Tang et al., ICML 2024) as a non-evicting alternative.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence narrow, no variance |
| Clarity | 3 | Well explained |
| Significance | 3 | Practical relevance for reasoning inference |
| Originality | 2 | Familiar cache-policy idea, new setting |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a timely, practically relevant problem with a simple method and measured efficiency gains, held back by narrow scope and unspecified measurement stack.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound mechanics, honest overhead accounting |
| Clarity & Presentation | 66 | Competent | Clear scenarios and appendices |
| Novelty & Originality | 58 | Competent | Known policy family, new context plus training |
| Significance & Impact | 68 | Competent | Timely efficiency problem |
| Experimental Validation | 58 | Competent | Reasonable breadth, no variance |
| Reproducibility | 64 | Competent | Code promised, details mostly present |
| Ethical Compliance | 64 | Competent | Nothing at stake; limitations thin |

## Questions for Authors
1. Which inference framework and attention kernels produced Table 2, and what does a vLLM-class full-cache run give at batch 32? A strong optimised baseline that preserves a multi-× gain would raise my Significance score.
2. What are mean output lengths per method in Table 2, and what is time-to-solution at equal accuracy?
3. Does the max-normaliser in Eqs. 3–5 get dominated by the attention-sink token, and does α adapt across layers?

## Limitations Assessment
**Partially.** No dedicated section; add deployment and scale limits.

## Ethics Review Flag
**No.**

## Overall Score
**4 (Borderline Accept)**: a practical, timely contribution with a sensible training extension; the unspecified measurement stack and narrow scope keep it from a higher score.

## Confidence
**3**: systems claims checked by arithmetic; I could not see the figures or the code.

**Minor:** the GPU memory of the A100 is not given.

---

# Peer Review Report (Reviewer 4)

## Paper: G-KV: Decoding-Time KV Cache Eviction with Global Attention
## Reviewer: Dr. Jonas Ferreira-Lindqvist, Generalist (ML group, mid-size university, North America; fictional persona)
## Expertise: deep learning broadly; efficiency and training
## Date: 2026-11-10

---

## Summary
Reasoning LLMs produce very long outputs, so the KV cache dominates memory. The paper proposes to score cached tokens by a decayed history of the attention they received rather than only by the last few tokens, combines this with a redundancy score, and shows gains over several eviction baselines on math and code benchmarks. It further trains the model with RL or distillation under the sparse attention caused by eviction, and reports throughput and memory savings.

## Venue-criteria checklist (ICLR: Soundness / Presentation / Contribution, rating)
| Criterion | Grade | Location |
|-----------|-------|----------|
| Claims supported by evidence | Partly | Figs. 4–5, Table 1; no variance, tuned on AMC 23 |
| Technically sound method | Met | §3, §5, Eqs. 1–5 |
| Clear presentation of main results | Partly | main comparisons are figures only (Figs. 5, 6, 18, 19) |
| Contribution matters to the ICLR audience | Met | reasoning-model efficiency is of broad interest |
| Limitations and scope stated | Not met | no limitations section; §8 says "efficient and scalable reasoning for LLMs" |
| Reproducibility | Partly | code promised; seeds, RL optimiser details missing |

## Strengths

### S1: A clear problem, a clear idea, easy to explain
§1 and §5 make the argument in one paragraph: local windows forget, history helps. Fig. 2 (caption) and the three bullet scenarios in §5 make the mechanism easy to follow for a non-specialist.

### S2: Two complementary levers with an informative control
Training-free scoring (§5) and model adaptation (§6) are separate levers, and Table 1 includes RL-Full to separate "RL helps" from "RL under compression helps".

### S3: Honest accounting of costs
Tables 3–4 and App G report the overhead of the new score and the memory of the extra score cache, and App F states a downside (decoding time rises with batch size).

### S4: Evaluation breadth is reasonable for the venue
Two model families, three benchmarks, budgets from 250 to 2000 (Figs. 5, 18), and a model-adaptation study with three budgets (Table 1).

## Weaknesses

### W1: The central comparison cannot be read from the paper (MAJOR)
Figs. 5, 6, 18 and 19 carry the headline ("nearly a 20% improvement under a 512-token budget", §7.3), yet there is no table of numbers, no error bars and no confidence intervals; in the text extraction, the panel values are not readable. Table 1 has the only numbers and they come from single runs. Reviewers and later readers cannot verify "our method achieves SOTA performance across most budgets and benchmarks" (§7.3).
- **Suggested Fix:** add an appendix table with pass@1 (± CI) per method, budget, benchmark and model.

### W2: Wording runs ahead of the evidence (MAJOR)
"RL-Sparse ... significantly outperforming models trained with the Full KV cache" (§7.4) is stated without a significance test and on AIME the margins are 0.7–1.6 points (Table 1, derived); "enabling efficient and scalable reasoning for LLMs" (§8) rests on two 7–8B models; "the tokens retained by our method have a higher information density" (§7.3) is not tested; and Appendix I builds a strong narrative ("compression as intelligence") from a word cloud of one head and one easy case study (Figs. 20–24). The appendix reads as speculation and sits oddly next to the careful systems material.
- **Suggested Fix:** replace "significantly" with measured differences and CIs, tone down or move App I into a clearly labelled speculation paragraph with a causal test (e.g., ablate "wait" tokens), and soften §8.

### W3: The two halves are loosely coupled and the second is narrowly validated (MAJOR/MINOR)
The title and Fig. 4/5 concern training-free eviction; §6/§7.4 concern RL on one 7B model, trained at one budget (2048) and one cap (4096), math only, evaluated only with G-KV. A reader cannot tell whether the RL benefit is specific to G-KV or general.
- **Suggested Fix:** evaluate the RL-Sparse model with a second eviction policy, or state the scope in §7.4.

### W4: No limitations section; scope not stated (MINOR)
The paper ends with a one-paragraph conclusion; limitations (two models, 4096-cap training, hyperparameters tuned on AMC 23) are not discussed.
- **Suggested Fix:** add a limitations paragraph.

## Questions for Authors
1. Can you provide tables behind Figs. 5/6/18/19 with CIs? That would let me credit the headline gain and raise Clarity/Contribution.
2. Is the RL gain specific to G-KV, i.e., does an RL-Sparse model trained with G-KV also help R-KV at test time?
3. What is the budget for hyperparameters (α, λ, s, w) for each baseline?

## Limitations Assessment
**No.**

## Ethics Review Flag
**No.**

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Reasonable evidence, no variance, tuned α |
| Clarity | 3 | Understandable, results in figures |
| Significance | 3 | Of interest to the audience |
| Originality | 2 | Incremental in the policy, new in the training part |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear, useful idea with a decent evaluation for the venue and an informative training control; typical accepted-paper weaknesses (no variance, a few overclaims) rather than a fatal flaw.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound method; protocol gaps |
| Clarity & Presentation | 62 | Competent | Clear writing; results in figures; speculative appendix |
| Novelty & Originality | 58 | Competent | Incremental plus a new training component |
| Significance & Impact | 66 | Competent | Timely, practical |
| Experimental Validation | 58 | Competent | Enough to support direction, not size |
| Reproducibility | 64 | Competent | Code promised, details mostly present |
| Ethical Compliance | 62 | Competent | Nothing at stake; no limitations |

## Overall Score
**4 (Borderline Accept)**: weaknesses are typical of accepted ML-efficiency papers (no variance, some overclaim) and are outweighed by a clear, practical idea and an informative training control.

## Confidence
**3**: I am not a KV-cache specialist and did not recompute every figure.

**Minor:** typos ("A cases presented", "DeepSeek-Qwen-Llama-8B"), inconsistent names (StreamLLM/StreamingLLM, GKV/G-KV), "Published as preprint paper" footer.

---

# Devil's Advocate Report

## Paper: G-KV: Decoding-Time KV Cache Eviction with Global Attention
## Reviewer: Prof. Yusra Halloran-Baek (evaluation methodology and statistics, university, Oceania; fictional persona)

---

## Steelman
Reasoning models generate long outputs, so eviction under a fixed budget is the binding constraint. Attention to a token is intermittent, so a score that remembers past attention saves tokens that a single window would discard, and the retained set is spread more evenly over the sequence (Fig. 7). Adapting the model with RL under the true eviction mask further recovers accuracy. Together they give large accuracy gains at small budgets and large throughput gains.

## Core Argument Chain
1. Attention sets of different windows are not fully consistent (Observation 1, §4), but the union of earlier windows covers the last window's set well (Observation 2).
2. Hence a decayed history score retains tokens that matter later (§5).
3. Hence G-KV beats local-score and redundancy-aware baselines, most at small budgets (Figs. 4, 5).
4. The model should be trained under the sparse mask; RL-Sparse beats RL-Full (Table 1).
5. Compression yields large throughput and memory savings (Table 2, App G).
∴ G-KV plus RL-Sparse enables efficient, scalable reasoning.

## Strongest Counter-Argument
The central causal claim is that the *global* score explains the gains, but the paper's evidence does not isolate it. The only controlled comparison is Fig. 4: global vs. local score, no redundancy term, on AMC 23, with α picked from that very sweep ("This range is recommended as the optimal hyperparameter setting", §7.2) and then fixed at 0.8 for the headline (§7.3). Everything that carries the headline (Figs. 5, 6, 18, 19) compares "G-KV", defined as global score *plus* R-KV's redundancy score, with a new max-normalisation and a re-tuned λ (App D), against R-KV and others at default settings ("other parameters follow the settings specified in their respective papers", §7.3). The comparison therefore confounds the global score with normalisation, mixing weight and tuning effort. The motivating evidence is also weaker than its framing: four windows inside the last 512 tokens (§4), a union of three sets that is expected to overlap ≈ 91% by chance at 55% retention (derived: 1 − 0.45³), and kept rates of 0.6–0.9 (from axis text) that are far from the 512/16k regime in which the method operates. At α=0.8 and s=128 the decay horizon is only ≈ 640 tokens (derived: 128/(1−0.8)), so the score is "global" in name only for 16k–32k outputs. Finally, the mechanistic explanations (retained tokens have "higher information density", position spread, "wait" tokens) are correlational. If the gain is mostly redundancy plus tuning, the paper is a modest variant of R-KV; if it is truly the global score, the cheap 2×2 ablation will show it, and the authors have not provided it.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim survives because the α plateau is wide (§7.2), the same α is used untuned on AIME 24 and LiveCodeBench, and the weakest evidence (single runs, tuning on AMC 23) supports a narrower but still positive claim; it is MAJOR, not fatal.

| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| – | – | – | none | – | – |

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | §7.2, Fig. 4; §7.3; App D, Fig. 12 | α (and λ) selected on AMC 23, which also supplies the headline; baselines at defaults. Evidence supports a weaker claim (gain exists), not a contradicting one. Protocol sweep: no held-out selection statement found. Row applied (decision table criterion 3): selection can't be shown to be the best-scoring value from the text; main claim plausibly holds across the plateau and on untuned AIME/LCB, so MAJOR | Held-out selection set; equal sweeps for baselines |
| DA-M2 | Logic | §4, Fig. 1, Observations 1–2 | Observation 2 lacks a chance baseline (≈ 0.91 at 55% for a 3-window union, derived), Observation 1's overlaps (axis range 0.80–1.00) can equally be read as high persistence supporting local scores, and the regime (kept 0.6–0.9) is not the deployed one | Null baselines at deployed retention; long-horizon reuse analysis |
| DA-M3 | Scope | §5, Eqs. 3–5; §1 "long-term importance" | Effective horizon 1/(1−α) = 5 compression steps ≈ 640 tokens at α=0.8, s=128 (derived) versus 16k–32k outputs; "global" and "long-term" overstate. Evidence supports "multi-window decayed" | Rename or add long-horizon evidence |
| DA-M4 | Evidence | §7.3, App D | Attribution: G-KV = global + redundancy + normalisation + λ; no 2×2 ablation on AIME/LCB; R-KV's λ re-tuning not stated | 2×2 grid; matched normalisation |
| DA-M5 | Logic | §7.3 (retention ratio, Fig. 7 explanation); App I; Figs. 20–24 | Mechanism claims untested: ratio conditioned on correctness, position-spread explanation (RoPE/semantic similarity) asserted, "wait"-token narrative from a word cloud and one easy case | Matched-problem analysis; causal ablation; label as speculation |
| DA-M6 | Evidence | §7.4, Table 1, Fig. 14 | RL-Sparse vs RL-Full is one run; AIME margins 0.73–1.57; no full-KV reference or length/truncation statistics; Fig. 14's validation set is 32 *training* questions with 4 samples each (App E) | Seeds, CIs, full-KV rows, length statistics |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Evidence | §7.3 | "our method achieves SOTA performance across most budgets and benchmarks" is not checkable without a numeric table |
| DA-m2 | Evidence | Table 1 | Distill beats RL-Sparse at AIME 512 (14.27 vs 13.75), consistent with "most settings" but not "significantly" |
| DA-m3 | Consistency | §7.5, Fig. 8, App F, Table 2 | "similar" decoding time across budgets and "approximately 40%" of Full-KV vs throughput ratios of 4.18×/3.41×/2.73× (implied ≈ 24%/29%/37%, derived) |
| DA-m4 | Citation | References | "2023 amc 8" and "2024 aime i" entries vs benchmark description; "Qwen 2.5" vs Qwen2 report |
| DA-m5 | Framing | §7.2 | CAKE comparison is a component, not the full method |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| RL-Sparse AMC 512 gain | +6.01 | 51.01 − 45.00 = 6.01 | Yes |
| RL-Sparse vs RL-Full AMC 512 | not stated | 51.01 − 47.65 = 3.36 | n/a |
| RL-Sparse vs RL-Full AIME (512/1024/2048) | "significantly outperforming" | 1.57 / 1.04 / 0.73 | Small margins |
| Throughput Qwen budget 512, batch 32 | 4.18× | 261.32/62.41 = 4.19 | Yes (truncation) |
| Throughput Llama, max | 19.7× | 612.60/31.08 = 19.71 (batch 64 vs Full at batch 16) | Yes, mismatched batch |
| KV memory, 512 | 2.18 GB, 96.1% | 56 GB × 640/16384 = 2.19 GB; 96.1% | Yes |
| Decoding time vs Full-KV | "approximately 40%" | implied ≈ 24% at batch 32, budget 512 | Needs reconciliation |
| Chance overlap, union of 3 sets at 55% | 95% observed | 1 − 0.45³ = 0.909 | Observed only ≈ 4 points above chance |

## Ignored Alternative Explanations
- Gains come from the redundancy term, max-normalisation or re-tuned λ rather than from the global score.
- Baseline defaults are suboptimal for this setting, while G-KV's α/λ are tuned on AMC 23.
- RL under a 4096 cap teaches shorter reasoning; the RL-Sparse vs RL-Full gap may reflect length or truncation behaviour rather than mask adaptation.
- Lower token-retention ratios reflect more problems solved at longer lengths.
- Throughput gains partly reflect an unoptimised full-cache baseline or longer outputs.

## Missing Stakeholder Perspectives
Practitioners running optimised serving stacks (paged KV, prefix caching), where per-head irregular selection may not drop in; and RL practitioners for whom the sparse mask's memory cost (App G) limits sequence length.

## Observations (Non-Defects)
The α plateau (§7.2) and the evaluation on benchmarks that were not used for tuning (AIME 24, LCB) make the qualitative claim fairly robust; the RL-Full control is the right one; the memory and overhead accounting (App G, Tables 3–4) is careful and arithmetically correct.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 46 | Attribution, null baselines and horizon issues |
| Clarity & Presentation | 58 | Clear method; results as figures; speculative appendix |
| Novelty & Originality | 46 | Incremental over history-based eviction plus R-KV |
| Significance & Impact | 52 | Useful but narrow |
| Experimental Validation | 42 | Tuning asymmetry, no variance, no attribution |
| Reproducibility | 56 | Many details, key ones missing |
| Ethical Compliance | 58 | Nothing at stake; no limitations section |

**Pool position:** better than about 42% of submissions to ICLR. Deciding evidence: the headline is not isolated from tuning and the redundancy term, and the motivating analysis lacks a null.

## Overall: 3 | Confidence: 4

---

# Phase 1.5: Literature Check

Mode: **strict**, cutoff 2025-09-24. Status: **not completed**. `related_search.py search` (claim C1, then one retry) failed with arXiv API HTTP 429 and 503; ledger holds one query record, no results. No benchmark scout, coverage, similarity or novelty step could run. Per the skill the review falls back to knowledge with `[verify]`; the Domain Reviewer's addendum above says so explicitly. No text-overlap or similarity flags exist.

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | Draft: "RL learning rate unstated" | Rewritten as Q3 | The sentence "The learning rate is set to 1 × 10⁻⁶" (§7.4) sits in the distillation paragraph and may cover both; ambiguity, not an omission |
| R2 | Draft: "CAKE is misdescribed" | Rewritten as a question inside W4 | Cannot be checked against CAKE's abstract without search; test 3 (consistency with prior work) not met |
| R2 | "AMC/AIME references" (draft weakness) | Moved to Q3 | Depends on knowledge outside the paper; a question, not an error |
| R4 | Typos and naming | Moved into the Minor line | Cosmetic |
| R1/DA | Fig. 1 kept-rate "0.6–0.9" vs text "55%" | Kept as qualified remark only | Axis text extraction only; unverifiable, not an error |
| DA | DA-M1 | Kept; ruled MAJOR (decision-table row stated) | Not CRITICAL: no best-scoring-value evidence, wide plateau, untuned benchmarks |
| R3 | Draft W on "memory of the A100 not stated" | Moved to Minor | Cosmetic relative to W1 |

Scores unchanged. The only appendix-answered point found: Appendix E answers "why entropy differs" (not raised); App B answers "is attention sparse after compression" (not raised).

# Phase 2: Synthesizer Part A: Package for the EIC

## Merged issue list and consensus
| Issue | Source IDs | Class | Hinges on? |
|-------|-----------|-------|------------|
| Hyperparameters tuned on AMC 23, baselines at defaults | R1-W1, DA-M1, (R4 Q3) | CONSENSUS-2 | Yes |
| Gain not attributed to global score (redundancy, normalisation, λ) | R1-W2, DA-M4 | CONSENSUS-2 | Yes |
| No variance, tiny benchmarks, single runs | R1-W3, R3-W3, R4-W1, DA-M6 | CONSENSUS-4 | Yes |
| Training comparison lacks references; "significantly" | R1-W4, R4-W2, DA-M6 | CONSENSUS-3 | Partly |
| Mechanism analyses untested (Obs 2 null, retention ratio, App I) | R1-W5, R2-W3, R4-W2, DA-M2, DA-M5 | CONSENSUS-4 | Yes |
| "Global"/"long-term" overstated; horizon ≈ 640 tokens | R2-W3, DA-M3 | CONSENSUS-2 | No |
| H2O / history-based eviction not compared; related work gaps | R2-W1, R2-W2 | SOLO | No |
| Efficiency evidence: stack, equal-accuracy, 40% vs 24% | R3-W1, R1-ERR-4, DA-m3 | CONSENSUS-3 | Partly |
| Breadth of models/tasks; scalable claim | R3-W3, R4-W3 | CONSENSUS-2 | No |
| No limitations section | R3, R4-W4 | CONSENSUS-2 | No |
| Per-head deployment cost, absolute accuracy at 512 | R3-W2, R3-W4 | SOLO | No |
| SPLIT | Overall rating (R3, R4 = 4; R1, R2, DA = 3) | SPLIT | Yes |

DA-CRITICAL issues: none.

## Official output (script, before EIC weights)
Official ratings: R1 3, R2 3, R3 4, R4 4, DA 3 → mean **3.40**; official composite **56.4**; no consistency warnings; no dimension spread above 20 (max 16). Composite band 3. ICLR view (before): Soundness 2, Presentation 2, Contribution 2.

---

# Editorial Decision

## Paper: G-KV: Decoding-Time KV Cache Eviction with Global Attention
## Submission ID: iclr26-4Uxtzc5Jns
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC (meta-reviewer) Prof. Halvard Okonkwo-Reyes; R1 Methodology Dr. Katarzyna Elmsworth, R2 Domain Prof. Daichi Morwenna, R3 Perspective Dr. Amara Tessler-Quispe, R4 Generalist Dr. Jonas Ferreira-Lindqvist, DA Prof. Yusra Halloran-Baek

---

## Decision: Borderline Reject (3)  (ICLR label as printed by the script: "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})"; scale status secondary, verify against the current form)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 4, DA 3 → mean 3.40 · official composite 56.4
**EIC assessment** (internal): weighted rating 3.33 → starting point 3 · weighted composite 55.5 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**Journal recommendation**: not applicable (conference target)

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** a timely problem, a simple plug-in score that is cheap (≈5 ms per step, Table 3), an informative RL-Full control (Table 1), honest overhead and memory accounting (App G), and a consistent direction of improvement on two models and three benchmarks, including benchmarks that were not used to pick α.
- **Against acceptance:** the headline gain (nearly 20% on AMC 23 at 512) is measured on the benchmark used to select α, against baselines at defaults, with the global score confounded with R-KV's redundancy term and no variance on 30–40-problem benchmarks; the motivating analysis has no null and a short real horizon; the closest ancestor (H2O) is not run; and the mechanism claims (information density, "wait" tokens) are untested.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| α chosen on AMC 23, headline on AMC 23 | R1-W1, DA-M1 | §7.2 (Fig. 4 caption), §7.3, Fig. 5 | Verified | Quotes present: "This range is recommended as the optimal hyperparameter setting."; "we set α to 0.8". Fig. 12's benchmark is unstated |
| Baselines at defaults, λ re-tuned for G-KV | R1-W1, DA-M1 | §7.3, App D | Partly correct | Default-settings sentence present; whether R-KV's λ was re-tuned is not stated |
| Observation 2 lacks a chance baseline (≈ 0.91) | R1-W5, R2-W3, DA-M2 | §4, Fig. 1 | Verified | Arithmetic 1 − 0.45³ = 0.909; the figure itself is not viewable |
| Token-retention ratio is conditioned on correctness | R1-W5, DA-M5 | §7.3 | Verified | Quote "calculated exclusively for cases where the model generates the correct answer" |
| Decay horizon ≈ 640 tokens at α=0.8, s=128 | R2-W3, DA-M3 | §5 Eqs. 3–5, §7.2 | Verified | Follows from the recursion; "global" is a naming/claim-strength issue |
| "Significantly" for RL-Sparse vs RL-Full | R1-W4, R4-W2, DA-M6 | §7.4, Table 1 | Partly correct | AMC gaps 3.36/4.92/3.83 are sizeable; AIME gaps 1.57/1.04/0.73 and a single run; no test |
| Full-KV baseline stack/time claims | R3-W1, R1-ERR-4, DA-m3 | §7.5, Table 2, Fig. 8, App F | Partly correct | Ratios recompute; stack not stated (searched "A100", "GPU"); "40% vs 24%" depends on equal token counts |
| H2O cited but not run | R2-W1 | §2, §7.3 | Verified | Absent from the §7.3 baseline list; MAJOR at most (cited, peer-reviewed prior work) |
| "Qwen 2.5" cites the Qwen2 report | R1-ERR-5, R2-W4 | §7.1, References | Verified | MINOR |
| No limitations section | R3, R4-W4 | whole paper | Verified | Text search for "limitation" finds only the intro sentences |
| "wait"-token and "compression as intelligence" narrative | R4-W2, DA-M5 | App I, Figs. 20–24 | Overstated (by the authors) | Word cloud of one head and one easy case; speculative |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Every entry in the Error Log that I checked at its location held (ERR-1, 2, 3, 5); ERR-4 partly; well calibrated |
| R2 (Domain) | 3 | 3 | 1.0 | Sound; the novelty delta rests on knowledge without a search and is marked `[verify]`; no point found incorrect |
| R3 (Perspective) | 4 | 3 | 1.0 | Useful systems checks (Table 2 per-sequence rate, superlinear Llama scaling verified); the "optimised stack" inference is an estimate |
| R4 (Generalist) | 4 | 3 | 1.0 | Fair and balanced; its Overall 4 sits at the generous edge given the verified tuning/attribution issues it did not list, but this is a role-typical view, not an error |
| DA | 3 | 4 | 1.25 | Numerical checks all held; correctly refused to call anything CRITICAL; DA-M2 and DA-M3 verified |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | n/a (no ceiling) | n/a |

I also checked criterion 3 independently, since α is selected on AMC 23: the sweep's best-scoring α cannot be read from the text, the plateau is wide, and AIME 24/LCB use the same α without separate tuning, so the decision-table row is MAJOR, not CRITICAL; no ceiling applies.

### Final Decision and Justification
The EIC-weighted rating is 3.33, so the starting point is 3 (Borderline Reject); the weighted composite is 55.5 (band 3) and agrees, so there is no cross-check disagreement. I keep the starting point. The three reviewers whose Overall is 3 and the two who say 4 differ mostly on how much weight the practical value deserves; the verified issues (tuning on the benchmark that carries the headline, attribution of the gain, no variance on very small benchmarks, an untested motivating observation) are ordinary for ICLR submissions individually, but together they leave the size and cause of the main gain unestablished. My own pool position is about 52: the problem is timely and the idea is sound and cheap, but the evidence sits where a typical rejected submission sits (small benchmarks, one run, tuned-vs-default asymmetry), and the paper's new elements (decayed accumulation, sparse-mask RL) are incremental or narrowly validated. This is not "unsure": the deciding evidence points to the reject side, with a clearly fixable path (held-out selection, a 2×2 ablation, CIs and one larger model). The decision does not exceed any DA ceiling (none). The literature check could not run, so no missing-reference point affected the decision.

---

## Score Summary

### Official Scores and EIC Assessment

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|---------------------------|--------|
| Technical Rigor | 52 | 56 | 62 | 62 | 46 | 55.6 | 54.5 | 16 |
| Clarity & Presentation | 60 | 62 | 66 | 62 | 58 | 61.6 | 61.2 | 8 |
| Novelty & Originality | 50 | 48 | 58 | 58 | 46 | 52.0 | 51.3 | 12 |
| Significance & Impact | 56 | 58 | 68 | 66 | 52 | 60.0 | 59.0 | 16 |
| Experimental Validation | 46 | 50 | 58 | 58 | 42 | 50.8 | 49.6 | 16 |
| Reproducibility | 58 | 60 | 64 | 64 | 56 | 60.4 | 59.8 | 8 |
| Ethical Compliance | 60 | 60 | 64 | 62 | 58 | 60.8 | 60.5 | 6 |
| **Composite** | 53.3 | 55.3 | 62.3 | 61.4 | 49.5 | **56.4 (before)** | **55.5 (after)** | |

Official rating (plain mean of Overall): 3.40. EIC-weighted rating: 3.33. No consistency warnings; no spread above 20.

### Target-Venue Scores (ICLR, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 2 / 2 |
| Rating at the EIC's final Overall 3 | "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})" (as printed by the script; secondary status, not official wording) |
| ICLR venue composite | 55.4 (band 3, final 3) |

*Cross-venue outlook not requested.*

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "G-KV: Decoding-Time KV Cache Eviction with Global Attention" to ICLR. The topic, memory-efficient decoding for long chain-of-thought models, is timely, and the combination of a training-free score with training under the actual eviction mask is an appealing package.

**Overall Assessment:**
The panel found the idea clear, cheap and plausible, appreciated the careful accounting of overhead and memory, and valued the RL-Full control. The consensus concern is that the size and cause of the headline gain are not yet established: hyperparameters are selected on a benchmark that also supplies the headline result, baselines are at defaults, the global score is not separated from the redundancy term, and no variance is reported on very small benchmarks. The panel's ratings are split between borderline reject and borderline accept.

**Key Strengths Identified by Reviewers:**
1. A simple, implementable score with measured overhead of about 5 ms per compression step (R1, R3, R4).
2. Sparse-mask RL/distillation with an RL-Full control (R1, R2, R4).
3. Transparent memory and throughput accounting (R1, R3).

**Key Concerns Requiring Attention:**
1. Selection of α/λ on AMC 23 and untuned baselines; no 2×2 ablation (CONSENSUS-2: R1, DA).
2. No variance, small benchmarks, results only as figures (CONSENSUS-4: R1, R3, R4, DA).
3. Untested mechanism claims: Observation 2 without a null, the token-retention ratio, and Appendix I (CONSENSUS-4).
4. Efficiency measurements without a stated serving stack and an equal-accuracy view (CONSENSUS-3).

No Devil's Advocate CRITICAL issue was raised.

**Decision: Borderline Reject (3)**

The idea is worth publishing once the evidence is firmer. What would change the decision: a held-out selection of α and λ with equal tuning for baselines, a {local, global} × {no redundancy, redundancy} ablation on all three benchmarks, confidence intervals and training seeds for Table 1, a null baseline for Observation 2 at the deployed retention, and one larger model. Please see the Revision Roadmap.

Sincerely,
Prof. Halvard Okonkwo-Reyes
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| No variance / tiny benchmarks / figures-only results | R1, R3, R4, DA | CONSENSUS-4 |
| Mechanism analyses untested | R1, R2, R4, DA | CONSENSUS-4 |
| Training comparison lacks references and "significantly" is unsupported | R1, R4, DA | CONSENSUS-3 |
| Efficiency evidence lacks stack and equal-accuracy view | R3, R1, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Overall rating | R3, R4 (4) | R1, R2, DA (3) | Verified tuning/attribution/variance issues were under-weighted by the 4s; deciding evidence points to the reject side (weighted 3.33) |
| Practical significance of the efficiency gains | R3 | R1, DA | Arithmetic holds; stack unspecified; credit pending an optimised baseline |

### Score Spread Discussion
No dimension exceeds the 20-point flag (maximum spread 16: Technical Rigor, Significance, Experimental Validation). The lower scores (R1, R2, DA) track verified protocol issues; the higher scores (R3, R4) track practical value and clarity; the weighted means sit within about 1 point of the raw means.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | α/λ tuned on AMC 23; baselines at defaults | Yes (R1-W1) | n/a | n/a |
| DA-M2 | MAJOR | Observation 2 without a null; regime mismatch | Yes (R1-W5, R2-W3) | n/a | n/a |
| DA-M3 | MAJOR | "Global" horizon ≈ 640 tokens | Yes (R2-W3) | n/a | n/a |
| DA-M4 | MAJOR | Gain not attributed (redundancy, normalisation, λ) | Yes (R1-W2) | n/a | n/a |
| DA-M5 | MAJOR | Mechanism claims untested | Yes (R1-W5, R4-W2) | n/a | n/a |
| DA-M6 | MAJOR | Table 1 single run, small AIME margins | Yes (R1-W3/W4, R4-W2) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*No DA-CRITICAL issue was upheld. These are issues the EIC verified as undermining the evidence for a main claim.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | α, λ selected on AMC 23 with baselines at defaults | R1-W1, DA-M1 | §7.2, §7.3, App D, Figs. 4, 5, 12 | Select on a held-out set; give baselines equal sweeps; report all benchmarks once | High; ≈100–150 GPU-h | Partly (reduced grid) |
| P1-2 | Gain not attributed to the global score | R1-W2, DA-M4 | §7.3, App D | {local, global} × {no redundancy, redundancy} on AMC/AIME/LCB at 512/1024; R-KV with matched normalisation | Medium; ≈40–60 GPU-h | Yes |
| P1-3 | No variance on very small benchmarks; single training runs | R1-W3, R3-W3, R4-W1, DA-M6 | §7.1, Table 1, Figs. 5, 6 | Paired bootstrap CIs; ≥3 training seeds for Table 1; numeric tables for Figs. 5/6/18/19 | Medium–High; ≈60–100 GPU-h per seed pair | Partly (CIs and tables yes, seeds maybe) |
| P1-4 | Motivating analysis lacks a null and a matching regime; "global" overstates | R1-W5, R2-W3, DA-M2, DA-M3 | §4, Fig. 1, §5, Eqs. 3–5 | Random/shuffled-window null at deployed retention; long-horizon reuse analysis; rename or justify | Low–Medium | Yes |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Table 1 reference points: full-KV rows, output-length and truncation statistics, cross-policy evaluation, "significantly" wording | R1-W4, R4-W2/W3, DA-M6 | Add rows and statistics; test RL-Sparse with R-KV | Medium | Partly |
| S2 | Efficiency evidence: stack, A100 variant, optimised full-cache baseline, equal-accuracy time-to-solution, 40% vs 24% | R3-W1, R1-ERR-4, DA-m3 | Report and reconcile | Medium | Yes |
| S3 | Retention-ratio and position-spread explanations untested; App I speculative | R1-W5, R4-W2, DA-M5 | Matched-problem analysis; causal ablation; relabel App I | Low–Medium | Yes |
| S4 | Add H2O/TOVA-style baselines and the α=1 sum variant; position against history-based and retrofit-for-eviction work | R2-W1/W2 | Run H2O, TOVA; add related work (see references below) | Medium | Partly |
| S5 | Scope: one 14–32B model; second model family for RL-Sparse; limitations section | R3-W3, R4-W3/W4 | One larger evaluation; limitations paragraph | High / Low | Partly |
| S6 | Critical/Important missing references (all unverified: literature search unavailable): Scissorhands (NeurIPS 2023), TOVA (EMNLP 2024), Keyformer (MLSys 2024), and `[verify]` Łańcucki et al. 2025 | R2 | Cite and differentiate | Low | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Per-head irregular selection and deployment compatibility | R3-W2 | Short deployment discussion; Tables 3/4 across batch sizes |
| N2 | Absolute accuracy at 512 vs full-KV | R3-W4 | Table with percent of full-KV accuracy |
| N3 | Citation/naming: Qwen2.5 vs Qwen2 report; "2023 amc 8"/"2024 aime i" entries; CAKE-style label; StreamLLM/StreamingLLM; GKV/G-KV; "A cases presented" | R1, R2, R4, DA | Fix |
| N4 | Cross-domain framing (cache-replacement policies such as LRFU `[verify]`, Quest as a non-evicting alternative) | R3 | Add to related work |
| N5 | Fig. 14 validation set is 32 training questions | DA-M6 | Use a held-out set |

## Estimated Revision Effort
- Priority 1: 4 items, roughly 200–300 GPU-hours and about 1–2 weeks.
- Priority 2: 6 items, roughly 100–200 GPU-hours plus writing, about 1–2 weeks.
- Priority 3: 5 items, a few days.
- **Total estimated revision time**: about 3–4 weeks for a full revision; the rebuttal window can cover the CIs, tables, the 2×2 ablation and a reduced held-out selection.

---

## Notes on running the skill
Literature check (strict) was requested but the arXiv API returned 429/503; the review proceeded with knowledge and `[verify]` marks and states this in Phase 0, Phase 1.5 and the Domain report. No Gap Scout was run (not requested). No instructions addressed to reviewers were found in the paper.
