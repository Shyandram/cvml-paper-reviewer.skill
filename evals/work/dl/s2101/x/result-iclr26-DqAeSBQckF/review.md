# Academic Paper Review: BLISS (Bilevel Influence Scoring for Pretraining Data Selection)

Date: 2026-11-10 · Mode: full · Target venue: ICLR (stated) · Literature check: strict, cutoff 2025-09-24 · Confirmation skipped (as requested)

> This is a simulation of how a careful panel would likely see this draft, not a prediction of any real outcome. Figures were not available (text extraction only): judgments on figures rest on captions and text, and say so where it matters. The five passes below were run one after another by a single model, in separate role-based passes; they share one context and are not independent agents.

---

## Phase 0: Paper Analysis and Reviewer Configuration Card

| Item | Finding |
|------|---------|
| Title | BLISS: A Lightweight Bilevel Influence Scoring Method for Data Selection in Language Model Pretraining |
| Primary Discipline | Machine learning → data-centric LLM pretraining (data selection) |
| Secondary Discipline(s) | Bilevel optimization; influence functions / data attribution |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Bilevel optimization with a small proxy LM and a score model; hypergradient via Hessian-vector products; multi-round top-20% selection |
| Target Venue | ICLR (stated by user); profile key `iclr` (2026 cycle, scale status "secondary") |
| Venue-Specific Notes | Submissions and reviews are public; a revised PDF can be uploaded during discussion, so separate fixable from fundamental issues. Accepted share about 27%. |
| Paper Maturity | Submission-ready draft (PDF header reads "Preprint") |
| Ethics-Relevant Content | None beyond web-scraped C4 pretraining data; footnote 1 discusses terms of service of commercial models |

### Claimed Contributions (as stated by the authors)
1. **C1**: A principled bilevel influence scoring framework (proxy model + score model) that "explicitly account[s] for the long-term impact of selected data" and runs without any external pretrained model (Abstract; §1 contribution 1; §4.1).
2. **C2**: Empirical gains over the strongest baseline MATES: "1.7× speedup" at 1B (Abstract; §1; §5.4; Figure 2b), "1.4% performance improvement" at 2.8B (§1; Table 2), +0.6% on LLaMA-0.5B (Table 3).
3. **C3**: "Extensive ablation studies" show each component is effective (§1 contribution 3; §6; Appendix C).
4. **C4 (implicit)**: Independence from external models removes bias and legal risk (§1 footnote 1; §4.1) and costs fewer FLOPs than MATES (§5.5, Table 4).

### Paper memory (factual record shared with all reviewers)
- **Setup:** C4, five equal shards, R = 5 rounds, round 1 random warm-up, then top-20% of each shard by score; LLM trained 10,000 steps per round (§5.1, §5.4, Figure 1). Pythia-410M/1B (25B tokens), Pythia-2.8B (15B tokens, 3 rounds, data selected in the 1B run), LLaMA-0.5B (3 rounds). Proxy and score model: Pythia-31M (410M target), Pythia-160M (1B target), LLaMA-134M (§5.2, Table 9). Validation set for the upper level: LAMBADA (§5.1). Evaluation: nine zero-shot tasks with lm-evaluation-harness, "accuracy with standard error" (Table 1). Seeds / number of runs: not stated after search. Hardware: 8 A6000 GPUs (Appendix E). Code release: not stated after search.
- **Splits and selection:** no test-set tuning is stated; hyperparameters in Table 9; how they were chosen is not stated. Appendix C.4 compares four validation sets and notes LAMBADA "yields the highest average accuracy".
- **Baselines:** MATES evaluated from the MATES authors' released 50k-step checkpoint; other baselines "quote Table 1 from MATES" (Appendix D).
- **Headline numbers:** 1.7× speedup (Fig. 2b, curve not readable here); 1.4% (Table 2, round 3: 49.0 vs 47.6); +0.6% (Table 3, round 3: 45.65 vs 45.01); Table 1 average 45.9 vs 45.7 (410M), 47.9 vs 47.5 (1B).
- **Appendix adds:** model details (A), LLaMA variant protocol (B), ablations (C.1–C.4, Tables 5–7, Figs. 3–5), full results (Table 8), hyperparameters (Table 9), loss curves (Figs. 6–8), distributed softmax (G).
- **Unverifiable here:** all figures (2–8). Some equation symbols are garbled in extraction (not treated as errors).

### Integrity signals
`scripts/integrity_scan.py` found no reviewer-directed text or hidden characters. No injected instructions were noticed while reading.

### Literature-check status
Strict mode, cutoff 2025-09-24, fingerprint written. The arXiv API answered **HTTP 429 (rate limited)** to every `search` attempt (two foreground tries, one delayed retry), so Round 1/2 claim and benchmark searches, `scout`, `coverage`, `similarity` and `novelty` could **not** be run and no search results were kept. `related_search.py verify` did work for three of four recommended titles later (marked below). Domain-review novelty and baseline tables are therefore built from the paper's own related work and from knowledge, with `[verify]` where unverified. Gap left open: no claim-level novelty profile; no under-reported-baseline check.

### Review Team (fictional personas)
- **EIC (meta-reviewer): Halvard Pereira-Wong**, area chair type at a large European public university. Senior; optimization and LLM training. Style: reads the tables before the prose.
- **Reviewer 1 (Methodology): Dr. Lucia Brandvold**, industrial research lab (North America). Mid-career; pretraining data curation and evaluation. Style: recomputes every average and insists on matched compute.
- **Reviewer 2 (Domain): Dr. Kwabena Asare-Mensah**, ML group, public research university (West Africa / Europe). Senior; influence functions, data attribution, learning-to-reweight. Style: asks what exactly is new versus the closest line of work.
- **Reviewer 3 (Perspective): Dr. Mei-Ling Sørensen**, applied optimization and operations research department (East Asia / Northern Europe). Mid-career; stochastic bilevel optimization, control. Style: constructive, looks for transfers from other fields.
- **Reviewer 4 (Generalist): Dr. Rafael Iturbe-Campos**, NLP group, private university (Latin America). Mid-career; language modeling in general. Style: typical program-committee member; weighs contribution against polish.
- **Devil's Advocate: Dr. Ingrid Valtonen-Mbeki**, evaluation-methodology researcher, independent institute (Europe). Senior; causal inference, benchmark validity. Style: rigorous, never hostile.

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Reviewer Reports

---

# Peer Review Report (R1)

## Paper: BLISS: A Lightweight Bilevel Influence Scoring Method for Data Selection in Language Model Pretraining
## Reviewer: Dr. Lucia Brandvold, Methodology Reviewer (industrial research lab; fictional persona)
## Expertise: pretraining data curation; zero-shot LLM evaluation; hypergradient methods
## Date: 2026-11-10

### Summary
The paper selects pretraining data with a small proxy LM and a score model trained by bilevel optimization: the proxy is trained on sample-weighted data (weights are a softmax over the score model's sigmoid outputs), and the score model is updated by a hypergradient so that the proxy does well on LAMBADA. The top 20% of each shard by score is used to train Pythia-410M/1B (and, with transferred data, 2.8B) over five rounds, and compared against MATES and others on nine zero-shot tasks. Reported gains over MATES are small in average accuracy but come with a claimed 1.7× speedup and lower selection FLOPs.

### Strengths
**S1: Clear, implementable algorithm with sound hypergradient.** Eq. (3)–(6) and Algorithm 1–2 define the update. I re-derived Eq. (5) from Eq. (1) with P_i = softmax(h_i): ∂P_i/∂θs = P_i(∇h_i − Σ_j P_j∇h_j) gives exactly the two terms printed in Eq. (5). The conjugate-gradient-free "3 steps of GDLS" is a reasonable approximation.
**S2: Selection cost is accounted for.** Table 4 reports FLOPs for pretraining, warm-up, bilevel optimization and scoring; the rows sum correctly (e.g., MATES 410M: 6.35+0.29+0.01+1.46 = 8.11; BLISS 1B: 17.67+0.07+0.261+1.53 = 19.53).
**S3: Multiple targets and ablations.** Three Pythia sizes plus LLaMA (Tables 1–3), and ablations on softmax, single versus bilevel, KL, proxy size, score-model initialization and validation set (Tables 5–7, Figs. 3–5). Hyperparameters are in Table 9 and the per-round selection time is reported (Appendix G).
**S4: Re-evaluation of MATES with the authors' own harness.** Appendix D states MATES's released checkpoint was re-evaluated, which avoids copying numbers from another evaluation pipeline for the main comparison.

### Weaknesses

**W1: The gains over MATES are within what the evaluation can resolve, and no variance across runs is reported.** Table 1 average gains are 45.9 vs 45.7 (410M) and 47.9 vs 47.5 (1B), i.e. +0.2 and +0.4; the Table 1 text says BLISS "improves ... 0.2% on average accuracy". Per-task standard errors are 0.5–2.1 points and every row is one run (no seeds stated after search). Table 2 gives direct evidence of the noise scale: round 1 is random data for both methods ("Round 1 (Random)"), yet MATES scores 45.9 and BLISS 45.2, a 0.7-point difference with no selection involved, larger than the round-2 gain (47.6 vs 47.4 = +0.2) and half of the headline 1.4 (round 3). In Table 3, the round-2 gap is 0.04 (44.57 vs 44.53). The wording "consistently outperforms MATES" (§5.4, quoted below) is stronger than this supports.
- **Suggested Fix:** Report ≥3 seeds for at least the 410M setting (selection plus pretraining), or paired bootstrap / McNemar tests on per-example correctness against MATES; report a random-data seed-to-seed spread. Cost at 410M: 3 seeds × ~8e19 FLOPs, roughly 3× the existing 410M run.

**W2: The "long-term influence" claim (C1) is never isolated and the implementation does not match Eq. (1).** The lower level in Eq. (1) is an arg min, but the proxy is updated by a single step (Algorithm 1, line 9; §5.3 "single-step" for 410M), 5 inner steps for 1B (Appendix E), 4 for LLaMA (Appendix B), for 3k total steps on 0.1% of each shard (Table 9, §5.1), with periodic resets (Appendix B). The text then says the models are "trained to convergence within relatively few steps" (§5.5), but no convergence evidence is given: §5.3 describes the losses in Figures 6–7 as ones that "initially decrease rapidly before experiencing a slight increase" (curves not readable here). The only mechanism ablation (§6.1, Table 5) compares bilevel against a single-level joint update, not converged-lower-level versus one-step influence, which is the stated difference to MATES (§4.1). Table 5 shows 44.7 vs 44.2 (+0.5) on one run.
- **Suggested Fix:** Ablate the number of lower-level steps (1, 5, 50) and a one-step-influence variant of the same score model at fixed compute; report lower-level gradient norm or loss plateau as evidence of convergence.

**W3: Weights in the bilevel problem are nearly uniform by construction.** §4.1 maps scores to (0,1) and Appendix A ends the score model with a Sigmoid; importance weights are P_i = e^{h_i}/Σ_j e^{h_j} (Eq. 1, Appendix G). Because h ∈ (0,1), the ratio between the largest and smallest possible weight in a batch is at most e ≈ 2.7, so the lower-level objective is close to unweighted training. Appendix C.1 states softmax "naturally amplifies important samples", which is bounded this way. Selection then uses only the ranking of h (Algorithm 1 line 14), so the magnitude of the weights matters only through the training signal that shapes θs. This limits what "importance weights" can express and may explain why the KL term, not the validation objective, is decisive (W4).
- **Suggested Fix:** Report the empirical distribution of P_i·B across a batch; test a temperature on the softmax or unbounded logits.

**W4: The upper-level objective does not track downstream quality in the authors' own diagnostic.** §6.2 notes that removing KL gives lower validation loss (Figure 8 vs 6) yet worse downstream accuracy, and §5.3 reports validation loss that rises in the second phase while the upper level is being minimized. The explanation (KL aligns the proxy with the LLM) is asserted, not tested (e.g., by measuring proxy-LLM agreement or by choosing γ). This leaves open that the score model is mostly a learned LAMBADA-similarity / proxy-loss ranker. Also, the LLaMA experiment removes the KL term altogether ("we remove the KL divergence regulation term in the lower level loss function", Appendix B) and replaces it with a 240-step distillation plus resets every 50 steps, so the LLaMA results test a different algorithm than the Pythia ones.
- **Suggested Fix:** Sweep γ (0, 1e-3, 1e-2, 1e-1) at 410M; add a simple proxy-loss or reference-loss selector at equal cost; state that LLaMA uses a variant.

**W5: Baseline protocol and compute claims.** (a) MATES comes from its authors' released checkpoint (Appendix D), BLISS from the authors' own run; other baselines are quoted from the MATES paper, so seed, harness version and data order are not matched; the 1.7× curve (Figure 2b) needs intermediate MATES checkpoints that Appendix D does not describe. (b) Table 1 lists "BLISS (8.08)" FLOPs in the 1B block, which is the 410M total; Table 4 gives 19.53 for 1B. (c) "BLISS achieves higher average downstream performance while consuming fewer FLOPs" (§5.5) rests on 8.08 vs 8.11 (−0.4%) and 19.53 vs 19.97 (−2.2%): effectively equal compute, not an efficiency gain. (d) Scoring cost is identical for the 31M and 160M proxy (1.53 in both Table 4 blocks, as is the 0.07 warm-up), which I would not expect for models with 5× different parameter count (question, not an error).
- **Suggested Fix:** Fix Table 1; run MATES and BLISS under one codebase and seed; plot accuracy against total FLOPs including selection for both.

**W6: Metric choice weakens every comparison.** Four of nine tasks sit at chance in the printed tables (ARC-C 24.8–25.9, LogiQA 24.7–28.7, OBQA ≈ 30, BoolQ ≈ 59–61 vs the majority-class level), and BoolQ alone drives much of the ablation differences (Table 5: 52.8/55.0/58.9). The authors acknowledge this ("it is hard to learn when the answer is too short", §C.4). On 410M, BLISS is below MATES on OBQA (−1.2) and BoolQ (−1.3); on 1B on ARC-C (−1.1), LogiQA (−2.9) and BoolQ (−1.1).
- **Suggested Fix:** Report macro average over informative tasks (SciQ, ARC-E, HellaSwag, PIQA, WinoGrande), plus validation perplexity on held-out C4 and a non-LAMBADA benchmark such as MMLU-style 5-shot at 2.8B.

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Severity | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|----------|-----|
| ERR-1 | E1 | Table 6, row "BLISS (Pythia-160M)" | "63.8(1.5) 40.8(1.0) 23.4(1.2) 27.5(1.8) 29.8(2.0) 51.3(0.9) 38.3(0.5) 67.6(1.1) 50.4(1.4) 44.1(1.3)" | Nine entries sum to 392.9, mean 43.66, printed 44.1 | Recomputed | High | MAJOR (the 31M vs 160M gap is 1.0 not 0.6, but conclusion "31M is sufficient" is unchanged) | Correct the average |
| ERR-2 | E1/E6 | Table 1 (1B block) vs Table 4 | "BLISS (8.08)" | 1B-block FLOPs equal the 410M total; Table 4 gives 19.53 for 1B | Cross-referenced two locations | High | MAJOR (it understates BLISS's 1B cost by 2.4×; the paper's cost claim uses Table 4) | Replace with 19.53 |
| ERR-3 | E1 | §5.4 text vs Table 1 (410M) | "0.8% on LogiQA" | Table 1: 27.3 − 26.1 = 1.2 | Recomputed | High | MINOR | Fix the text |
| ERR-4 | E1 | Table 1, MATES 410M average | "45.7 (1.4)" | Row entries sum to 410.3, mean 45.59, which rounds to 45.6; stated gain 0.2 would be 0.3 | Recomputed | Medium (MATES numbers may be copied from source) | MINOR | Recheck |
| ERR-5 | E5 | App. C.1 | "softmax weighting consistently outperforms naive weighting" | Table 5: softmax variant lower on ARC-E (40.8 vs 41.0), OBQA (29.8 vs 30.0), HellaSwag (36.0 vs 38.8); gain is carried by BoolQ (+6.1) | Cross-referenced Table 5 | High | MAJOR (claim wording) | Say "on average" and report BoolQ-excluded mean |
| ERR-6 | E6 | §5.2 vs title/abstract/Table 2 | "consists of 410 million, 1 billion or 2.5 billion trainable parameters" | The third model is called 2.8B everywhere else | Cross-referenced | High | MINOR | Harmonize |
| ERR-7 | E6 | Algorithm 1, lines 5–6 vs §4.2 | "if r > 1 else" | With r starting at 0, round r=1 re-initializes θs and θtr, contradicting "resumes training from the previous round's checkpoint" | Cross-referenced | Medium (may be index typo) | MINOR | Use r > 0 |
| ERR-8 | E6 | Table 9 vs Eq. (4), (6) | "Proxy/Score model learning rate(η1 /η2 ) 1e-5" | η2 is the GDLS step in Eq. (4) (Table 9: 1e-2) and η3 is the score-model rate | Cross-referenced | Medium | MINOR | Rename |

**Minor:** Table 8 caption says "standard deviations" while Table 1 says "standard error"; typos ("visulize", "multiuple", "updata"); Eq. (1) indexes i from 0 and the softmax denominator from 1.

### Claim-to-evidence map
| ID | Claim | Evidence | Verdict |
|----|-------|----------|---------|
| C1 | Long-term influence from a converged lower level, no external model | Eq. (1)–(6), Alg. 1, Table 5 | Partially: no external model is true; "converged / long-term" not tested |
| C2 | 1.7× speedup; 1.4% at 2.8B | Fig. 2b (not readable), Table 2, Table 3 | Partially: gains positive but small and single-run |
| C3 | Each component effective | Tables 5–7, Fig. 3 | Partially: differences 0.4–1.4 on single runs; Table 6 favors the smaller proxy |
| C4 | Fewer FLOPs than MATES | Table 4 | Marginally (0.4–2.2%) |

**Protocol sweep:** no statement was found that any hyperparameter, checkpoint or validation set was selected on the nine reported tasks. LAMBADA is not among the nine evaluation tasks (§5.1). Appendix C.4 notes LAMBADA gave the highest average accuracy among four validation sets, but does not say the main-run choice was made that way: asked as a question.

### Dimension Scores (0–100)
**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the gains over the one close baseline are within the noise visible in the paper's own Table 2, and the central mechanism claim is untested.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Sound hypergradient, but theory–implementation gap (W2), bounded weights (W3), three numeric inconsistencies |
| Clarity & Presentation | 55 | Competent | Understandable, but several cross-section inconsistencies |
| Novelty & Originality | 50 | Developing | Application of known bilevel reweighting to pretraining; see R2 |
| Significance & Impact | 48 | Developing | Small gains on one corpus and ≤2.8B models |
| Experimental Validation | 42 | Developing | One MATES baseline, single runs, chance-level tasks |
| Reproducibility | 58 | Competent | Table 9 and Appendix A/B/E/G; no seeds, no code statement |
| Ethical Compliance | 55 | Competent | Only a one-sentence limitation (language only, §7) |

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Mean of rigor and validation is 47 |
| Clarity | 2 | Score 55 |
| Significance | 2 | Score 48 |
| Originality | 2 | Score 50 |

### Questions for Authors
1. How many seeds support Table 1? If MATES and BLISS differ by less than the Table 2 round-1 gap (0.7) under repeated runs, my rating stays at 3; a significant paired test would raise it to 4.
2. Does a one-step version of your score model (same budget) match BLISS? This is the experiment that would verify C1.
3. Was LAMBADA chosen as the validation set because it gave the best average in Appendix C.4, and did MATES use the same validation data?
4. Why are the scoring costs identical (1.53) in the 31M and 160M proxy settings of Table 4?

### Limitations Assessment
**Partially.** §7 only says the approach is limited to language models. Missing: single corpus (C4), ≤2.8B scale, sensitivity to the fixed 20% ratio, run-to-run variance.

### Ethics Review Flag
**No**

## Overall Score
**3**: Borderline Reject. Sound and implementable, but the evidence does not separate the method from noise and the key mechanism claim is untested.

## Confidence
**4**: Recomputed all reported averages and checked Eq. (5).

---

# Peer Review Report (R2)

## Paper: BLISS: A Lightweight Bilevel Influence Scoring Method for Data Selection in Language Model Pretraining
## Reviewer: Dr. Kwabena Asare-Mensah, Domain Reviewer (ML group, public research university; fictional persona)
## Expertise: influence functions and data attribution; learning-to-reweight; data selection for LLMs
## Date: 2026-11-10

### Summary
The paper argues that existing pretraining data selection either depends on external pretrained models (e.g., QuRating) or uses one-step influence (MATES), and proposes a bilevel scheme in which a score model produces sample weights for training a small proxy LM, with the upper level minimizing validation loss. It reports modest gains over MATES at 410M, 1B and 2.8B and with LLaMA.

### Strengths
**S1: Relevant and timely problem.** Selecting pretraining data without an external scorer (§1) is a meaningful motivation, and the comparison set in Table 8 (DSIR, SemDeDup, DsDm, LESS, QuRating, MATES) covers the main published families at 410M/1B.
**S2: Right closest competitor.** MATES is the natural reference; §4.1 states the difference (one step vs trained to convergence) clearly and Table 4 compares cost on the same scale.
**S3: Honest scope in related work.** §2 differentiates from SEAL (fine-tuning, LoRA) and states the setting difference explicitly.
**S4: Broad empirical surface.** Several model sizes and an architecture change (Tables 1–3).

### Weaknesses

**W1: Novelty claim is overstated relative to the learning-to-reweight literature.** §2 closes with "the first to leverage bilevel optimization techniques for data selection in LLM pretraining". Hypergradient-based example weighting with a validation set (Learning to Reweight Examples; Meta-Weight-Net, which learns a network mapping a sample's training loss to its weight) is the same core mechanism as Eq. (1)–(6), and neither is cited. The paper cites ScaleBiO (Pan et al., 2024) and Grangier et al. (2023), bilevel reweighting for LM training, and gives no empirical comparison. The new ingredients are scale-oriented engineering: a proxy model, a distributed softmax (Appendix G), reuse of the score model across rounds, and top-k selection. The paper says the contribution is "principled", but there is no theory for the practical single-loop version (Algorithm 1).
- **Suggested Fix:** Reword "first" to the narrower claim; add a related-work paragraph on learning-to-reweight and learned sample-weight networks; compare against a ScaleBiO-style reweighting baseline at 410M or explain why not applicable.

**W2: A directly relevant pretraining paper is missing.** "Data Selection via Optimal Control for Language Models" (Gu et al., arXiv 2410.07064, Oct 2024; verified via `related_search.py verify`, prior to the cutoff) selects pretraining data by reasoning about training dynamics, which overlaps with the "long-term impact" motivation (§1, §2). Per its title it frames selection as optimal control over the training trajectory; I have not read beyond the title with the search tool, so the exact overlap needs checking by the authors. §2's statement that existing influence-based methods look at a "fixed LLM" ignores it. Not cited, not compared.
- **Suggested Fix:** Cite and differentiate; if feasible, include it as a baseline at 410M.

**W3: The framing "external pretrained model dependence" is under-specified and untested.** §1 and §5.5 say MATES "requires" external pretrained models, but the paper never says which external model MATES uses or how it affects outcomes; footnote 1 argues legal risk with only ToS references (OpenAI, 2024; Google, 2024), which concern LLM-generated data, not the BERT-style scorers used by data influence models. No experiment tests the benefit of independence (e.g., the effect of the external model on MATES).
- **Suggested Fix:** Name the exact external model in MATES; add an ablation where the external component is replaced with a from-scratch one in MATES, or soften the claim.

**W4: Related positioning at the proxy-model level.** Small proxy models for large-model data decisions are an established idea (DoReMi, DoGE for mixtures; reference-model selection such as RHO-loss; RegMix for mixtures), and the paper cites DoReMi and DoGE only in a list. A cheap proxy-based selector at equal cost is the right control for the claim that bilevel influence is needed.
- **Suggested Fix:** Add a proxy-loss/excess-loss selector using the same 31M/160M proxy.

**W5: Contribution size.** At 410M the average gain is +0.2, at 1B +0.4 (Table 1); at 2.8B +0.2 in round 2 and +1.4 in round 3 (Table 2); LLaMA +0.04 then +0.64 (Table 3). In the field snapshot I would use (no search possible; knowledge only), recent data selection work reports gains of ≥1 point average or ≥2× efficiency over strong baselines on larger or more varied corpora. The 1.7× claim is the strongest, but its evidence is a figure I cannot read and a single run.

### Missing References
*Verification status: found by `related_search.py verify` unless marked [verify]. The arXiv API was rate limited, so no searches were run.*

| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | Gu, Dong, Wang, Hao, Dong, Wei, Huang. *Data Selection via Optimal Control for Language Models*, arXiv 2024 (found: arxiv.org/abs/2410.07064). Peer-review venue not verified: [verify] | Same problem (pretraining data selection, long-term/dynamics-aware); likely closest conceptual neighbor |
| Important | Ren, Zeng, Yang, Urtasun. *Learning to Reweight Examples for Robust Deep Learning*, ICML 2018 (found: arxiv.org/abs/1803.09050) | Validation-driven sample weights by bilevel/meta-gradient: same core mechanism |
| Important | Shu, Xie, Yi, Zhao, Zhou, Xu, Meng. *Meta-Weight-Net: Learning an Explicit Mapping For Sample Weighting*, NeurIPS 2019 (found: arxiv.org/abs/1902.07379) | A learned network mapping a sample's training loss to its weight, trained by bilevel optimization |
| Important | Mindermann et al. *Prioritized Training on Points that are Learnable, Worth Learning, and Not Yet Learnt*, ICML 2022 [verify] | Small hold-out model for data selection: a cheap proxy-based control |
| Helpful | Liu et al. *RegMix: Data Mixture as Regression for Language Model Pre-training*, 2024 [verify] | Small proxy runs inform large-model data decisions |
| Helpful | Lin et al. *Rho-1: Not All Tokens Are What You Need*, 2024 [verify] | Reference-model-based selection signal |

**Novelty delta (from the paper's own related work and knowledge; no literature-check profile):**
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|----------------------|-------------------|----------------------|------------------|---------------------------|
| C1 bilevel scoring for pretraining | Learning to Reweight / Meta-Weight-Net; ScaleBiO (Pan et al. 2024) | Validation-driven sample weights; scalable bilevel for LLM data reweighting | Proxy + score model for top-k selection in pretraining | ScaleBiO yes; the other two no |
| C1 long-term effect | MATES (one-step) [cited]; Gu et al. 2024 | Model-aware selection; dynamics-aware selection | Training proxy over many steps | MATES yes; Gu et al. no |
| C2 results | MATES | Same protocol | +0.2 to +1.4 average | yes |

**Per-claim novelty (knowledge-based, `[verify]`):** C1 method: medium to incremental; C2 result: incremental. No claim is "known" as a whole.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Experiments leave the main mechanism untested |
| Clarity | 3 | Readable, positioning is clear for MATES |
| Significance | 2 | Small gains |
| Originality | 2 | Known mechanism applied at scale |

### Dimension Scores (0–100)
**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the closest prior mechanisms are uncited and the gain over the one close baseline is small.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 55 | Competent | Correct derivation, but untested approximations |
| Clarity & Presentation | 60 | Competent | Clear organization |
| Novelty & Originality | 48 | Developing | Known mechanism, new application scale; "first" overstated |
| Significance & Impact | 50 | Developing | Small gains, narrow evidence |
| Experimental Validation | 48 | Developing | One strong baseline compared directly |
| Reproducibility | 60 | Competent | Hyperparameters present |
| Ethical Compliance | 58 | Competent | Limitations thin |

### Questions for Authors
1. Which external pretrained model does MATES use, and how large is its effect on MATES's result? (A clear answer supports C4 and would raise my rating.)
2. How does BLISS differ from learning-to-reweight / Meta-Weight-Net and from the optimal-control view of data selection, in mechanism and in results?
3. Would a proxy-loss-only selector at the same cost match BLISS?

### Limitations Assessment
**Partially.** Only the modality limitation is stated.

### Ethics Review Flag
**No**

## Overall Score
**3**: Borderline Reject. A competent application of a known mechanism with a modest, thinly evidenced gain.

## Confidence
**4**: Familiar with the sub-field; the literature check was only partly possible.

---

# Peer Review Report (R3)

## Paper: BLISS: A Lightweight Bilevel Influence Scoring Method for Data Selection in Language Model Pretraining
## Reviewer: Dr. Mei-Ling Sørensen, Perspective Reviewer (applied optimization department; fictional persona)
## Expertise: stochastic bilevel optimization; control and system identification
## Date: 2026-11-10

### Summary
The paper recasts pretraining data selection as a bilevel problem with a cheap surrogate (proxy) and learned weights, and uses Hessian-vector products to obtain hypergradients so that the whole procedure runs from scratch. From an optimization viewpoint, this is an appealing way to turn an intractable subset search into a differentiable relaxation, and the efficiency numbers suggest it could be practical.

### Strengths
**S1: A good relaxation of a combinatorial problem.** §4.1 states the subset-selection difficulty and replaces it with a differentiable weight model; the HVP-based approximation (Eq. 4) is a standard, memory-friendly choice (§4.2).
**S2: Engineering that makes it practical.** Distributed softmax with three communications (Appendix G), bilevel time "within 1.5 hours" per round, and a total overhead of about 3% of pretraining on top of scoring (Table 4).
**S3: Self-contained data pipeline.** No external scorer is a practical advantage for groups that cannot call proprietary models (footnote 1), even though the legal argument is stated more strongly than it is evidenced.
**S4: Reasonable transfer demonstration.** Selecting with a 160M proxy and using the data for 2.8B (Table 2) tests transfer across scale, a deployment-relevant question.

### Weaknesses

**W1: Assumptions behind the proxy-transfer story are untested.** The method assumes that "the data preferences of the proxy model align with those of the LLM" (§4.1) and uses KL to enforce it, but there is no measurement of preference agreement (e.g., rank correlation between proxy-derived and LLM-derived influence), and Table 6 shows a larger proxy (160M) scoring lower than the smaller one (31M). Control-theory viewpoint: a surrogate with a documented fidelity measure would clarify when this transfers.
- **Suggested Fix:** Report rank correlation of scores between proxy sizes, and between rounds.

**W2: Single-corpus, single-distribution validation.** The method optimizes for LAMBADA loss (§5.1) and evaluates on nine tasks that are not LAMBADA, so the "validation similar to downstream" assumption in §3 is the whole bridge. Appendix C.4 / Figure 5 show different validation sets give different downstream profiles. A deployment would not know its downstream tasks.
- **Suggested Fix:** Evaluate with a multi-task or task-agnostic validation set (e.g., held-out C4 perplexity) and report which tasks move.

**W3: Scale and drift.** The selection ratio is fixed at 20% per shard (Figure 1), with five rounds; the interaction between a continuously updated score model and a changing LLM (Algorithm 1) has no analysis or stability check. Extensions: mixture-of-domains data, multilingual data, and the optimal-control view of the problem.
- **Suggested Fix:** Report selection-ratio sensitivity (10/20/40%) and score drift between rounds.

**W4: Limitations and societal impact are minimal.** §7 has one sentence; no energy/carbon estimate of the added selection compute beyond FLOPs, and no discussion that quality filtering by a learned score may remove minority-dialect or low-resource text (a standard fairness risk in web-data curation).
- **Suggested Fix:** Add a short broader-impact paragraph and a domain-composition analysis of selected versus random data.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound method, evidence thinner than ideal |
| Clarity | 3 | Understandable |
| Significance | 3 | Practical potential |
| Originality | 3 | Useful combination |

### Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear practical idea with positive results in three settings and ordinary weaknesses; I weigh potential generously, as my role suggests.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound derivation and practical approximations |
| Clarity & Presentation | 62 | Competent | Readable |
| Novelty & Originality | 60 | Competent | Useful combination |
| Significance & Impact | 62 | Competent | Practical path for from-scratch selection |
| Experimental Validation | 56 | Competent | Several settings, thin statistics |
| Reproducibility | 64 | Competent | Hyperparameters and hardware given |
| Ethical Compliance | 62 | Competent | Nothing high-risk; limitations thin |

### Questions for Authors
1. How stable is the score ranking across rounds and proxy sizes? (High agreement would raise my confidence in transfer.)
2. What happens when the downstream tasks are unknown and the validation set is generic C4?
3. Do selected subsets change domain composition relative to random data?

### Limitations Assessment
**Partially.**

### Ethics Review Flag
**No**

## Overall Score
**4**: Borderline Accept. A practical, reasonable idea with positive though modest results; I lean toward the contribution over the evidence gaps.

## Confidence
**3**: Not a data-curation specialist; I did not recompute the tables.

---

# Peer Review Report (R4)

## Paper: BLISS: A Lightweight Bilevel Influence Scoring Method for Data Selection in Language Model Pretraining
## Reviewer: Dr. Rafael Iturbe-Campos, Generalist Reviewer (NLP group, private university; fictional persona)
## Expertise: language modeling; evaluation of pretrained LMs
## Date: 2026-11-10

### Summary
The paper presents BLISS, a way to pick the most useful 20% of each shard of web text for LLM pretraining using a small proxy model and a score model trained with bilevel optimization against validation loss on LAMBADA. It claims better downstream accuracy than MATES and others at 410M and 1B, with transfer to 2.8B and LLaMA, at about the same compute and with no external model.

### Strengths
**S1: Focused, well-motivated problem and clear pipeline.** Figure 1 (caption) and Algorithm 1 let a non-specialist follow the five-round procedure.
**S2: Fair-looking cost accounting.** Table 4 shows the selection overhead as a share of total FLOPs.
**S3: Direct comparison with the closest method on shared settings.** §5.4 and Appendix D state that MATES's setting is reused; Table 8 has seven baselines.
**S4: Includes ablations** on the components (Section 6).

### Venue criteria checklist (ICLR)
| Criterion | Grade | Location |
|-----------|-------|----------|
| Claims supported by evidence | Partly: gains small and single run | Tables 1–3 |
| Soundness of method | Met: clear derivation | §4, Eq. (3)–(6) |
| Significance to the community | Partly: one corpus, ≤2.8B | §5 |
| Presentation | Partly: several inconsistencies | Table 1 vs Table 4; §5.2 |
| Reproducibility | Partly: Table 9, no seeds or code | Table 9, App. E |

### Weaknesses

**W1: Headline wording exceeds the evidence.** The paper says "Our algorithm consistently outperforms MATES and random selection methods across multiple tasks" (§5.4) while Table 1 shows BLISS below MATES on OBQA and BoolQ at 410M and on ARC-C, LogiQA and BoolQ at 1B, and below Random on ARC-C at 410M (25.1 vs 25.6). The abstract presents the 1.7× speedup and a "1.4%" gain without stating that 1.4 is one round of one run with a 0.2 gain one round earlier (Table 2).
- **Suggested Fix:** State per-setting average gains and the number of tasks where BLISS loses; move Figure 2 numbers into a table.

**W2: Table 1 hides most baselines and has a wrong entry.** The main table has only Random, MATES and BLISS, while §5 lists seven baselines (they are in Table 8). The 1B BLISS cost is printed as 8.08, the 410M value (Table 4 says 19.53), which a reader would take as a roughly 2.4× cost advantage.
- **Suggested Fix:** Put all baselines in the main table and fix the cost.

**W3: Where the gain comes from is unclear.** The reader cannot tell from the paper whether the gain arises from the long-term bilevel formulation, the KL term (a 1.4-point effect in Figure 3, "9.3% accuracy boost on LogiQA", whose absolute/relative meaning is unclear and whose bar values I cannot read), or from the choice of LAMBADA (Appendix C.4). Different settings use different procedures (single-loop 410M, five inner steps 1B, resets and no KL for LLaMA: Appendices B, E).
- **Suggested Fix:** One consolidated ablation table at one scale with variance, and a summary of the per-setting differences in the main text.

**W4: Inconsistent details reduce trust.** The third model is "2.5 billion" parameters in §5.2 and 2.8B elsewhere; Table 8 says "standard deviations" and Table 1 "standard error"; round-1 results differ between methods in Table 2 though both are random data.

**Minor:** typos in the Table 5 caption ("updata") and §5.3 ("visulize"); Algorithm 1 index "r > 1".

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gains thin, key mechanism untested |
| Clarity | 3 | Mostly clear |
| Significance | 2 | Modest |
| Originality | 2 | Incremental over MATES / known weighting |

### Dimension Scores (0–100)
**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: clear and competent, but the improvement over the main baseline is small and the claim wording is ahead of the table.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Competent | Sound but untested approximations |
| Clarity & Presentation | 62 | Competent | Clear pipeline, some contradictory numbers |
| Novelty & Originality | 52 | Developing | Incremental |
| Significance & Impact | 52 | Developing | Narrow evidence |
| Experimental Validation | 48 | Developing | Single runs |
| Reproducibility | 62 | Competent | Table 9 |
| Ethical Compliance | 58 | Competent | Thin limitations |

### Questions for Authors
1. Which of the three ingredients (long-term bilevel, KL, LAMBADA) is responsible for most of the gain? An ablation at one scale with seeds would move my rating up.
2. Can the paper show per-task wins and losses against MATES with confidence intervals?

### Limitations Assessment
**Partially.**

### Ethics Review Flag
**No**

## Overall Score
**3**: Borderline Reject. A competent but incremental paper whose evidence is not yet at the level of a typical accepted ICLR paper.

## Confidence
**3**: Not a data-selection specialist.

---

# Devil's Advocate Report

## Paper: BLISS: A Lightweight Bilevel Influence Scoring Method for Data Selection in Language Model Pretraining
## Reviewer: Dr. Ingrid Valtonen-Mbeki, evaluation-methodology researcher (independent institute, Europe; fictional persona)

---

## Steelman
A from-scratch method that picks data using only small models, runs at about the cost of the best existing model-aware method, and still edges it out in every reported setting is practically useful. The bilevel formulation is a principled way to ask which data helps a model that is trained on it, and the multiple ablations suggest each ingredient contributes.

## Core Argument Chain
1. Existing methods either need external models or measure one-step influence (§1).
2. Training a proxy to convergence on weighted data and measuring validation loss captures long-term influence (§4.1, Eq. 1).
3. A score model trained this way ranks data well for the LLM (§4.2, via KL alignment).
4. Data selected this way gives better downstream accuracy than MATES at equal or lower compute (Tables 1–4, Figure 2).
5. Each component is needed (Section 6, Appendix C).
∴ BLISS is a better, independent data-selection method because it models long-term influence.

## Strongest Counter-Argument
Even if every number in Tables 1–3 is correct, they do not show that the *long-term influence* is what helps. Premise 2 is not what the code does: Eq. (1) is an arg min, but Algorithm 1 takes one gradient step per iteration (five at 1B, four in LLaMA, 3k steps at lr 1e-5 on 0.1% of the shard, with resets), and no experiment compares this against a one-step-influence version of the same pipeline; the only mechanism ablation (§6.1) swaps bilevel for a joint single-level update, which changes the objective rather than the horizon. The authors' own diagnostics point elsewhere: removing KL gives lower validation loss but worse downstream accuracy (§6.2, Figure 8 vs 6), the validation loss rises in the second phase while the upper level is being minimized (§5.3), and the softmax over sigmoid scores bounds relative weights at about e (Appendix A, §4.1, Eq. 1), so the bilevel weighting is close to uniform. A more parsimonious account is that the score model is a learned ranker that favors data resembling LAMBADA (the sole validation set, §5.1; Appendix C.4 shows other choices give a different profile) and the proxy's loss; the KL alignment with the LLM then does the work. Under this account the gains are those of a cheap model-aware filter, not of long-term influence. The sizes of the gains (+0.2 and +0.4 average at 410M and 1B; +0.04/+0.64 for LLaMA; Table 2 round 1 shows 0.7 spread between identical random-data runs) leave the alternative open. The authors must show that the converged-lower-level horizon, not the validation choice or KL, drives the improvement.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The paper's own results show a positive average gain in every reported setting and no test-set selection is stated (the nine evaluation tasks differ from the LAMBADA validation set, §5.1), so the core empirical claim survives in a weaker form; the issues below are MAJOR because narrowing the claim and adding controls would address them.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic / Evidence (supports a weaker claim only) | §4.1 vs Alg. 1 line 9; §5.3; §6.1; Table 5 | "Long-term influence if the proxy is trained to convergence" is untested; the lower level is a few steps and no one-step vs multi-step ablation exists | Ablate inner steps and one-step influence at fixed compute; show lower-level convergence, or narrow C1 |
| DA-M2 | Evidence | Tables 1–3; Table 2 round 1 | Gains of +0.2, +0.4, +0.04/+0.64 average are inside the visible noise (0.7 between identical random-data rounds); single runs; "consistently outperforms" (§5.4) overstated | Seeds or paired tests; replace "consistently" with per-setting numbers |
| DA-M3 | Alternative explanation | §5.1; App. C.4; §6.2 | Gains may come from LAMBADA-similarity or KL alignment rather than bilevel horizon; LAMBADA is reported as best among four validation sets by downstream average (App. C.4) without saying how the main-run choice was made | Sweep γ and validation sets; report how LAMBADA was chosen; add a proxy-loss selector |
| DA-M4 | Evidence / fairness | App. D; Table 1 (1B block); Table 4; §5.5 | MATES from its own released checkpoint vs BLISS from the authors' run; other baselines quoted; 1B FLOPs printed 8.08 vs 19.53; "fewer FLOPs" is −0.4% / −2.2% | Fix table; same-codebase comparison; state savings accurately |
| DA-M5 | Overgeneralization | Abstract; §1; Table 2; §7 | "1.7× speedup" and "1.4%" are single-point claims (1B Figure 2b; round 3 of 3 at 2.8B on transferred data); single corpus C4 and ≤2.8B | Report the full curves in a table; scope claims |
| DA-M6 | Logic | Table 6 vs §5.2, App. C.2 | The 160M proxy (used for 1B) scores lower (printed 44.1; recomputed 43.7) than the 31M proxy (44.7) at 410M, which undermines the premise that closer proxy fidelity helps | Explain, or test 31M for 1B |
| DA-M7 | Metric validity | Tables 1, 5; §C.4 | Four of nine tasks are at chance; BoolQ drives ablation differences (52.8/55.0/58.9) | Report informative-task macro averages and perplexity |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Clarity | §5.2 | "2.5 billion" vs 2.8B |
| DA-m2 | Clarity | §5.4 text vs Table 1 | "0.8% on LogiQA" vs 1.2 |
| DA-m3 | Clarity | Table 8 vs Table 1 | "standard deviations" vs "standard error" |
| DA-m4 | Reproducibility | Alg. 1 lines 5–6; Table 9 | Index and notation (η2 vs η3) inconsistencies |
| DA-m5 | Claim distortion (E5) | App. C.1 | "consistently outperforms naive weighting" vs Table 5 rows |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| 2.8B gain at round 3 (Table 2) | "1.4%" | 49.0 − 47.6 = 1.4 | Yes |
| LLaMA round 3 gain (Table 3) | "0.6%" | 45.65 − 45.01 = 0.64 | Yes |
| LogiQA gain vs MATES, 410M | "0.8%" | 27.3 − 26.1 = 1.2 | **No** |
| MATES 410M average (Table 1) | 45.7 | 410.3 / 9 = 45.59 | Off by 0.1 |
| BLISS 1B average (Table 1) | 47.9 | 431.0 / 9 = 47.89 | Yes |
| BLISS Pythia-160M average (Table 6) | 44.1 | 392.9 / 9 = 43.66 | **No** |
| Softmax gain (Table 5, C.1) | "1.1%" | 44.7 − 43.6 = 1.1 | Yes |
| Single-level gap (§6.1) | "0.5%" | 44.7 − 44.2 = 0.5 | Yes |
| BLISS 1B total FLOPs | 8.08 (Table 1) / 19.53 (Table 4) | 17.67+0.07+0.261+1.53 = 19.53 | Table 1 wrong |

## Ignored Alternative Explanations
- LAMBADA similarity or KL alignment drives the gain, not the horizon (DA-M3).
- Run-to-run variance and differing run provenance between MATES (released checkpoint) and BLISS (Appendix D).
- The larger share of the average from BoolQ and other near-chance tasks.
- The fixed 20% selection ratio and number of rounds favor any model-aware selector over random.

## Missing Stakeholder Perspectives
Practitioners who must pick the validation set for an unknown downstream mixture (§3 assumes similar distributions); communities whose text may be filtered out by a learned quality score (no domain-composition analysis).

## Observations (Non-Defects)
The hypergradient in Eq. (5) matches a direct derivation; Table 4's rows sum correctly; the authors disclose the LLaMA protocol difference in Appendix B; re-evaluating MATES in the authors' harness is good practice; footnote 1 states a legal motivation clearly.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 46 | Mechanism untested, theory–practice gap |
| Clarity & Presentation | 58 | Clear but inconsistent numbers |
| Novelty & Originality | 46 | Known mechanism, "first" overstated |
| Significance & Impact | 44 | Small gains in narrow settings |
| Experimental Validation | 40 | Single runs, noise-level gains |
| Reproducibility | 56 | Hyperparameters present, no seeds |
| Ethical Compliance | 55 | Thin limitations |

Pool position: better than about 35% of submissions to ICLR. Deciding evidence: gains inside the paper's own noise, mechanism claim untested.

## Overall: 2 | Confidence: 4

---

# Phase 1.5 / 1.6: Literature-check addendum and Report Check

**Literature check:** strict mode, cutoff 2025-09-24; arXiv API rate-limited (HTTP 429) for all search attempts, so Round 1/2 searches, scout, coverage, similarity and novelty were not run (0 results kept). Three recommended titles were later confirmed by `verify` (Gu et al.; Ren et al.; Shu et al.); two are marked `[verify]`. The Domain addendum above is built from the paper's related work and knowledge. No missing baseline was graded "required"; per the rules only prior, verified work could be; the optimal-control paper is prior (Oct 2024) and verified but its overlap was not checked beyond title, so it is "Important", not "Critical".

**Report check (Synthesizer Step 0):**
| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R2 | W2 abstract overlap wording | Rewritten | Per rule 3, statement about the prior work's content limited to what its title supports |
| R2 | W4 proxy-model positioning | Moved to Minor-level / kept as lower priority | Cited as line of work; less specific than W1–W3 |
| R3 | W3 "Scale and drift" | Rewritten | No specific location for drift; now tied to Alg. 1 and Figure 1 |
| R3 | W4 minority-dialect risk | Kept as question-level | Speculative; no evidence in paper |
| R4 | W4 | Moved to Minor | Cosmetic inconsistencies, already covered by R1 Error Log |
| R1, DA | None dropped | Kept | Each has a location, a quote or recomputation, and a fix |

Scores were not changed.

---

# Phase 2: EIC Meta-Review and Decision

## Synthesizer package (Part A)

**Master issue list**
| Issue | Sources | Class |
|-------|---------|-------|
| Gains within noise; single runs; "consistently" overstated | R1-W1, R4-W1, DA-M2, R2-W5 | CONSENSUS-4 |
| Long-term / convergence mechanism untested; theory–practice gap | R1-W2, DA-M1, R3-W1 (proxy fidelity), R4-W3 | CONSENSUS-4 |
| Confound: validation set / KL / alternative explanation | R1-W4, DA-M3, R3-W2, R4-W3 | CONSENSUS-4 |
| Baseline protocol, FLOPs table error, compute claim | R1-W5, R4-W2, DA-M4 | CONSENSUS-3 |
| Novelty vs learning-to-reweight and optimal-control work | R2-W1, R2-W2, R2-W4 | SOLO (R2) |
| Metric validity (chance-level tasks) | R1-W6, DA-M7 | CONSENSUS-2 |
| Table 6 average error / proxy size | R1 ERR-1, DA-M6 | CONSENSUS-2 |
| Limitations/ethics thin | R3-W4, R1 | CONSENSUS-2 |
| Bounded softmax weights | R1-W3, DA counter-argument | CONSENSUS-2 |
| Reviewer split on overall merit | R3 (4) vs R1, R2, R4 (3) vs DA (2) | SPLIT |

DA-CRITICAL issues: none. Hinge points: gain vs noise (Table 2 round 1), the 1.7× claim, Table 6 / Table 1 errors, uncited prior mechanisms.

**BEFORE (official, provisional)**: mean rating 3.00, official composite 53.2 (`before.json`).

## EIC Meta-Review (Halvard Pereira-Wong)

### The Case For and Against
- **For acceptance:** a practical, fully from-scratch selector with a correct hypergradient, positive average gains over the strongest model-aware baseline in all four settings (Tables 1–3), selection cost reported, and ablations across several design choices.
- **Against acceptance:** the gains (+0.04 to +0.6 average, one +1.4) are no larger than the 0.7 spread between identical random-data rounds in Table 2, all single runs; the central "long-term influence" mechanism is untested; two prior mechanisms (learning-to-reweight, optimal-control data selection) are not discussed; and several tables contradict each other.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Table 2 round 1 differs (45.9 vs 45.2) for random data | R1-W1, DA-M2 | Table 2 | Verified | Direct evidence of ≥0.7 spread; round-1 is random for both methods |
| Table 1 1B BLISS FLOPs 8.08 vs Table 4 19.53 | R1 ERR-2, R4-W2, DA-M4 | Table 1, Table 4 | Verified | Quote present; Table 4 sum 19.53 |
| Table 6 160M average 44.1 vs recomputed 43.66 | R1 ERR-1, DA | Table 6 | Verified | Recomputed |
| "0.8% on LogiQA" vs 1.2 | R1 ERR-3, DA-m2 | §5.4, Table 1 | Verified | Minor |
| MATES 410M average 45.7 vs 45.59 | R1 ERR-4 | Table 1 | Partly correct | True arithmetic; may come from source paper; minor |
| "softmax consistently outperforms" | R1 ERR-5 | App. C.1, Table 5 | Verified | Three tasks lower; BoolQ carries the gap |
| Lower level is a few steps, not converged | R1-W2, DA-M1 | Alg. 1 l.9, Table 9, §5.3, §5.5 | Verified | Wording "trained to convergence" at §5.5; no convergence evidence |
| Weights bounded by about e | R1-W3, DA | §4.1, App. A, App. G | Verified | Follows from h ∈ (0,1) and the softmax denominator |
| BLISS below MATES on 3 of 9 tasks at 1B, 2 at 410M | R4-W1, R1-W6 | Table 1 | Verified | |
| "First to leverage bilevel optimization ... pretraining" and missing learning-to-reweight / optimal-control work | R2-W1/W2 | §2; reference list | Partly correct | Reference list does not contain these; overlap with the optimal-control paper is judged from title only |
| Footnote 1's ToS argument covers MATES's scorer | R2-W3 | fn. 1 | Overstated | ToS relate to LLM-generated data; unknown which model MATES uses |
| R3: transfer via 160M proxy to 2.8B "tests scale" | R3-S4 | Table 2 | Partly correct | The data were chosen in the 1B run; round-1 gap shows noise |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Every numeric claim in the Error Log checked out; mostly calibrated; decisive for the outcome |
| R2 (Domain) | 3 | 4 | 1.0 | Missing references real; W3's ToS argument overstated; overlap judged on a title |
| R3 (Perspective) | 4 | 3 | 0.75 | Pool position 66 and Overall 4 rest on transfer and robustness claims that Table 2's own round-1 gap and Table 6 do not support; fairly generic |
| R4 (Generalist) | 3 | 3 | 1.0 | Sound, typical review; W1 verified |
| DA | 2 | 4 | 1.0 | Counter-argument survived the check; Overall 2 is slightly severe but its weaknesses are verified |

### DA-CRITICAL Rulings
None raised ("No CRITICAL issues found"). AC test applied to the strongest MAJOR (DA-M1, mechanism untested): not fatal alone, because the empirical claim stands in a narrower form and the fix is an additional ablation; it stays MAJOR.

### Final Decision and Justification
The official mean is 3.00 and the EIC-weighted rating is 2.92, so the starting point is **3 (Borderline Reject)**. The composite cross-check (official 53.2, EIC-weighted 52.4) also lands in band 3, so there is no disagreement to explain. I do not depart: no verified issue that the ratings missed pushes the decision either way. R3's lone 4 rests on a favorable reading (transfer, practicality) that the verified numbers do not support at that strength, which is why its weight is lowered. No DA ceiling applies. **My pool position: better than about 46% of ICLR submissions.** Deciding evidence: a competent, correct method whose margin over the one close baseline is inside the noise that Table 2 reveals, with the key mechanism claim untested; a typical accepted ICLR paper would show either a clearer gain or the ablation that isolates the long-term effect. The authors can repair this in a revision (seeds, one-step ablation, fixed tables, positioning), so it is not a fundamental rejection.

**Final (EIC): 3 (Borderline Reject). ICLR label: 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}).**

---

# Editorial Decision

## Paper: BLISS: A Lightweight Bilevel Influence Scoring Method for Data Selection in Language Model Pretraining
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC Halvard Pereira-Wong; R1 Dr. Lucia Brandvold; R2 Dr. Kwabena Asare-Mensah; R3 Dr. Mei-Ling Sørensen; R4 Dr. Rafael Iturbe-Campos; DA Dr. Ingrid Valtonen-Mbeki

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00 · official composite 53.2
**EIC assessment** (internal): weighted rating 2.92 → starting point 3 · weighted composite 52.4 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**ICLR rating label** (scale status "secondary"): 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); Soundness 2, Presentation 2, Contribution 2.

## Score Summary

### Official Scores and EIC Assessment (script output, `--venue iclr --final 3`)

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share |
|---|---|---|---|---|
| R1 (Meth.) | 4 | 0.85 | 1.25 | 27% |
| R2 (Domain) | 4 | 0.85 | 1.00 | 21% |
| R3 (Persp.) | 3 | 0.70 | 0.75 | 13% |
| R4 (Gen.) | 3 | 0.70 | 1.00 | 18% |
| DA | 4 | 0.85 | 1.00 | 21% |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 52 | 55 | 62 | 54 | 46 | 53.8 | 53.0 | 16 |
| Clarity & Presentation | 55 | 60 | 62 | 62 | 58 | 59.4 | 58.9 | 7 |
| Novelty & Originality | 50 | 48 | 60 | 52 | 46 | 51.2 | 50.4 | 14 |
| Significance & Impact | 48 | 50 | 62 | 52 | 44 | 51.2 | 50.1 | 18 |
| Experimental Validation | 42 | 48 | 56 | 48 | 40 | 46.8 | 45.7 | 16 |
| Reproducibility | 58 | 60 | 64 | 62 | 56 | 60.0 | 59.5 | 8 |
| Ethical Compliance | 55 | 58 | 62 | 58 | 55 | 57.6 | 57.1 | 7 |
| **Composite** | 50.3 | 53.1 | 60.7 | 54.2 | 47.6 | **53.2 (before)** | **52.4 (after)** | |
| Pool position (P%) | 38 | 45 | 66 | 48 | 35 | | | |

No dimension spread exceeds 20; no script warnings.

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "BLISS: A Lightweight Bilevel Influence Scoring Method for Data Selection in Language Model Pretraining" to ICLR. Selecting pretraining data without an external scorer is a worthwhile goal, and the paper gives a clear, implementable algorithm.

**Overall Assessment:** The panel found the method sound and the cost accounting welcome, but did not find the evidence sufficient. Gains over the closest baseline are small and come from single runs; the claim that long-term influence is the cause is not isolated; and the work needs to be placed against earlier bilevel sample-weighting and dynamics-aware selection work.

**Key Strengths Identified by Reviewers:**
1. A correct, practical hypergradient scheme with a proxy and score model that run from scratch (R1, R3, R4).
2. Selection cost reported in FLOPs, with positive average gains over MATES in all four settings (R1, R2, R4).
3. Several ablations, hyperparameters and hardware stated (R1, R4).

**Key Concerns Requiring Attention:**
1. Gains (+0.04 to +0.6, one +1.4) are not separated from run-to-run noise; Table 2's round-1 gap alone is 0.7 (CONSENSUS-4).
2. The long-term/convergence mechanism is not tested against a one-step variant, and the weights are bounded (CONSENSUS-4).
3. Validation set, KL term and proxy size are confounded with the bilevel horizon (CONSENSUS-4); Table 1 and Table 6 contain numeric errors and conflict with other tables (CONSENSUS-3).
4. Related work on learning-to-reweight and optimal-control data selection is missing (R2, SOLO).

No Devil's Advocate issue was rated CRITICAL.

**Decision: Borderline Reject (3).** The paper is close to the bar in design quality but below it in evidence. A revision that adds seeds or paired tests, the one-step ablation, a corrected and consolidated Table 1, and a positioning paragraph would move it into the borderline-accept range; larger-scale or multi-corpus evidence would move it further.

Sincerely,
Halvard Pereira-Wong
Editor-in-Chief (meta-reviewer, fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Gains small / noise / single run / overclaimed wording | R1, R4, R2, DA | CONSENSUS-4 |
| Long-term mechanism untested | R1, DA, R3, R4 | CONSENSUS-4 |
| Confounded explanation (validation set, KL, proxy) | R1, DA, R3, R4 | CONSENSUS-4 |
| Baseline protocol, FLOPs inconsistency | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Merit overall | R3 (4) | R1, R2, R4 (3), DA (2) | Verified numbers support 3; R3 down-weighted to 0.75 |
| Novelty | R3 (60) | R2 (48), DA (46) | Missing prior mechanisms support the lower view |

### Score Spread Discussion
No dimension was flagged above 20. Largest spread: Significance (18), R3 62 vs DA 44; adopted view: closer to the lower scores because gains are within observed noise.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| none | CRITICAL | "No CRITICAL issues found" | n/a | n/a | n/a |
| DA-M1 | MAJOR | Long-term claim untested | Yes (R1-W2) | n/a | n/a |
| DA-M2 | MAJOR | Gains within noise | Yes (R1-W1, R4-W1) | n/a | n/a |
| DA-M3 | MAJOR | Alternative explanation (validation set / KL) | Yes (R1-W4) | n/a | n/a |
| DA-M4 | MAJOR | Baseline protocol, FLOPs | Yes (R1-W5, R4-W2) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*Issues the EIC verified as undermining a main claim; there is no upheld DA-CRITICAL issue.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Gains not separated from noise; "consistently" overstated | R1-W1, R4-W1, DA-M2 | Tables 1–3, §5.4 | ≥3 seeds at 410M (selection + pretraining) or paired tests; report random-data spread; reword | High; about 3 × 8e19 FLOPs | Partly (paired tests on existing outputs: Yes) |
| R2 | Long-term/convergence mechanism untested | R1-W2, DA-M1 | §4.1, Alg. 1, §6.1, Table 5 | Inner-step ablation and one-step-influence variant at fixed compute; convergence diagnostics | Medium; a few 410M runs | Partly |
| R3 | Numeric inconsistencies in decisive tables | R1 ERR-1/2/3/5, DA | Table 1 (1B FLOPs), Table 6, §5.4, App. C.1 | Correct tables and text | Low | Yes |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Confound: validation set, KL, proxy loss | R1-W4, DA-M3, R3-W2 | γ sweep, validation-set choice rationale, proxy-loss selector baseline | Medium | Partly |
| S2 | Baseline protocol and compute claims | R1-W5, R4-W2, DA-M4 | Same-codebase MATES; all baselines in Table 1; accurate FLOPs claim | Medium | Partly |
| S3 | Missing related work and "first" claim | R2-W1/W2 | Cite and differentiate Gu et al. (2410.07064), Ren et al. (2018), Shu et al. (2019); soften "first" | Low | Yes |
| S4 | Metric validity | R1-W6, DA-M7 | Informative-task macro average, held-out perplexity | Low | Yes |
| S5 | Bounded weights | R1-W3 | Report weight distribution; temperature | Low | Yes |
| S6 | Table 6 proxy-size contradiction | R1 ERR-1, DA-M6 | Explain or rerun | Low–Medium | Partly |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Broader impact / minority-text filtering | R3-W4 | Domain-composition analysis |
| N2 | Selection-ratio sensitivity and drift | R3-W3 | 10/20/40% ratios |
| N3 | Minor inconsistencies (2.5B vs 2.8B, "standard deviations", Alg. 1 index, η notation) | R1 ERR-6/7/8, DA-m1–m5 | Harmonize |
| N4 | Missing helpful references (RHO-loss [verify], RegMix [verify], Rho-1 [verify]) | R2 | Cite |

## Estimated Revision Effort
- Priority 1: 3 items, about 1–2 weeks (seeds are the main cost).
- Priority 2: 6 items, about 1 week.
- Priority 3: 4 items, a few days.
- **Total estimated revision time**: roughly 2–3 weeks.
