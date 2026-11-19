# Review of "ZSPAPrune: Zero-Shot Prompt-Aware Token Pruning for Vision-Language Models"

Skill: academic-paper-reviewer v2.10.1 · Mode: full · Target venue: ICLR (profile `iclr`, 2026 cycle, stated by user) · Date: 2026-11-10
Request: "literature check: strict, cutoff date 2025-09-24".
Figures were not available (text extraction only): Figures 1–3 were judged from captions and text. The simulation is not a prediction of the real outcome.

**Literature check status.** One strict-mode query was issued (`visual token pruning`, claim C1). The arXiv API did not respond (`error: arXiv API unreachable (The read operation timed out)`). The skill's rule for no network was followed: the check ran as `off`. No kept results, no `similarity`, `novelty`, `scout` or `coverage` output exist. Every reference recommended below comes from the reviewers' knowledge, is marked `[verify]`, and was published before the 2025-09-24 cutoff as far as the reviewers know. Unverified items are never treated as required comparisons beyond "peer-reviewed prior work as far as recalled".

**Integrity scan.** `scripts/integrity_scan.py` found no reviewer-directed text or hidden characters. No injection was found while reading. The reviewers read the (identical) redacted copy.

---

## Phase 0: Paper Analysis and Reviewer Configuration Card

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | ZSPAPrune: Zero-Shot Prompt-Aware Token Pruning for Vision-Language Models |
| Primary Discipline | ML / Computer Vision → efficient multimodal LLM inference (visual token pruning) |
| Secondary Discipline(s) | Vision-language models; submodular / max-min diversity selection; embedded and edge inference |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Training-free pruning of projected visual tokens: cosine similarity to a mean-pooled prompt embedding (Eq. 4–7), then greedy max-min diversity fill (Eq. 8–9) |
| Target Venue | ICLR, top-tier ML conference (stated); profile key `iclr` |
| Venue-Specific Notes | None. ICLR 2026 accepted share ≈ 27% (≈ 45% rejected, ≈ 24% withdrawn). Rating scale shown as {0,2,4,6,8,10} (secondary status) |
| Paper Maturity | Submission-ready in form, early in substance (one main baseline, no code at submission) |
| Ethics-Relevant Content | None (public benchmarks, no human-subject data). Appendix C discloses LLM use |

### Claimed Contributions (as stated by the authors, Section 1)
1. **C1** (method): "a novel, zero-shot, plug-and-play token pruning method for VLMs. Its hierarchical and decoupled design ensures both high performance and broad applicability."
2. **C2** (problem framing): "reframe the visual token pruning problem as a tunable balance between task relevance and information diversity."
3. **C3** (result): "performance that is competitive with, and in several cases surpasses, current state-of-the-art methods" (abstract: "matches or surpasses the state-of-the-art with only minimal accuracy loss, even when pruning up to 90%"; "significant reductions in GPU memory footprint and inference latency").

### Paper memory (shared with all reviewers; factual record)
- **Setup facts.** Models: LLaVA-1.5-7B, LLaVA-NeXT-7B, Qwen2.5-VL-7B-Instruct (§4.1). Only one keep rate: 90% pruning (§4.2). Baselines: Original, DivPrune, and a self-implemented "All-in Task-Relevance" (§4.1), all "reproduced ... within our experimental framework". Benchmarks and splits (Appendix B): MMMU "official test split" (B.2.1), GQA test-dev balanced (B.2.2), POPE "official test split" (B.2.3), AI2D "official test split" (B.3.1), TextVQA "validation split" (B.3.2), ChartQA "official test split" (B.3.3). Tuning: "the relevance-diversity balance coefficient ... we used the optimal ratio for each specific benchmark" (§4.2). Seeds: "a fixed random seed" (Reproducibility Statement). Hardware, batch size, precision, prompt template, image resolution (e.g., Qwen max pixels), decoding settings, LLaVA-NeXT LLM backbone: not stated after search. Code: "Upon acceptance" only.
- **Headline numbers.** Abstract: "up to 90%" pruning; Introduction: "retaining approximately 90% of the original accuracy, even at ... 10%" keep rate. Table 1 (three models × six benchmarks), Table 2 (k sweep, Qwen), Table 3 (latency/memory, LLaVA-1.5, MMMU, 900 samples), Table 4 (pooling ablation, Qwen, MMMU and POPE).
- **Appendix.** A: architecture descriptions of the three VLMs (no "modifications" described). B: benchmark descriptions and splits. C: LLM-use statement. No extra experiments.
- **Unverifiable.** Figures 1–3 (images absent). The pruning insertion point in each VLM and the exact definition of k are not given (see reports).

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Tobias Reinholt, large public research university (Central Europe)
- **Seniority / Expertise**: senior faculty, area chair at several ML venues / efficient inference, multimodal learning
- **Role**: reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: calibrates to what ICLR actually accepts; checks each decisive quote himself.

### Reviewer 1 (Methodology): Dr. Mei-Ling Qiu, industrial research lab (East Asia)
- **Seniority / Expertise**: senior industry scientist / VLM benchmark evaluation (lmms-eval-style harnesses), latency measurement
- **Review Focus**: research design, statistics, comparison fairness, reproducibility
- **Style**: insists on matched protocols; searches the whole text for tuning statements.

### Reviewer 2 (Domain): Dr. Ravindra Pillai, industrial research lab (South Asia)
- **Seniority / Expertise**: mid-career / token reduction for ViTs and VLMs, KV-cache and attention-based pruning
- **Review Focus**: literature, theoretical framework, domain contribution
- **Style**: checks every novelty sentence against the closest prior work.

### Reviewer 3 (Perspective): Dr. Isabela Cardoso, embedded-systems and HCI group, university (South America)
- **Seniority / Expertise**: mid-career / on-device inference, retrieval and relevance feedback in IR
- **Review Focus**: cross-disciplinary connections, deployment, broader impact
- **Style**: constructive; names opportunities.

### Reviewer 4 (Generalist): Dr. Jonas Albrecht, vision group, public research institute (Northern Europe)
- **Seniority / Expertise**: mid-career / visual recognition, general vision-language
- **Review Focus**: contribution clarity, venue fit, presentation
- **Style**: typical program-committee member; weighs weaknesses against what accepted papers carry.

### Devil's Advocate: Dr. Amara Nwosu, evaluation-methodology group, university (West Africa / UK)
- **Seniority / Expertise**: mid-career / evaluation methodology, causal ablation design
- **Review Focus**: core-argument challenges, logic, overclaiming
- **Style**: rigorous, never hostile.

*Personas are fictional. Proceeding with the stated assumptions.*

---

## Phase 1: Independent Reports

The five reports were written one after another by a single model context in separate role passes (no subagents). Independence is simulated, not real; this is disclosed per SKILL.md.

---

# Peer Review Report (Reviewer 1)

## Paper: ZSPAPrune: Zero-Shot Prompt-Aware Token Pruning for Vision-Language Models
## Reviewer: Dr. Mei-Ling Qiu, Methodology (industrial research lab, East Asia; fictional persona)
## Expertise: VLM evaluation harnesses; latency and memory measurement; ablation design
## Date: 2026-11-10

## Summary
The paper prunes 90% of the visual tokens that a VLM passes to its LLM. It keeps a "core" set of tokens whose cosine similarity to the mean-pooled prompt embedding is highest (Eq. 4–7), and fills the rest of the budget greedily with tokens least similar to everything already chosen (Eq. 8–9). A coefficient k sets the core share. On LLaVA-1.5-7B, LLaVA-NeXT-7B and Qwen2.5-VL-7B the method is compared with DivPrune and with a relevance-only baseline on six benchmarks (Table 1), with a k sweep (Table 2), a latency and memory table (Table 3) and a pooling ablation (Table 4).

## Protocol Sweep (Step 0)
Searched the full text for `select`, `optimal`, `tuned`, `validation`, `test split`, `seed`, `hyperparameter`, `GPU`, `batch`, `resolution`.
- Tuning statement: "all experimental parameters were held constant, with the sole exception of the relevance-diversity balance coefficient for ZSPAPrune, for which we used the optimal ratio for each specific benchmark." (§4.2, Table 1 paragraph). Table 2 gives the sweep per benchmark on the same Qwen2.5-VL runs.
- Selection check: Table 1 Qwen row ZSPAPrune (MMMU 43.9, GQA 49.0, POPE 69.0) equals the best cell of each Table 2 row (MMMU 43.9 at k = 0.4; GQA 49.0 at 0.1; POPE 69.0 at 0.2). §4.3 states "MMMU achieves peak performance with a balancing coefficient of 0.4 ... GQA and POPE perform best at coefficients of 0.1 and 0.2".
- Splits reported: Appendix B.2.1–B.3.3 (see paper memory). No separate validation split for tuning is mentioned anywhere. Passed to the Devil's Advocate.
- Seeds: only "a fixed random seed" (Reproducibility Statement). Hardware, batch size, precision, prompt template, resolution settings: not stated after search.

## Strengths
### S1: Simple, training-free, attention-free design
The method needs only the projected visual tokens and prompt embeddings (Eq. 3–9), so it does not need attention maps and is compatible with fused attention kernels (§1). It is easy to implement and applies to three different VLM families.
### S2: A useful control: the relevance-only baseline
The "All-in Task-Relevance" baseline (§4.1, Table 1) isolates the cost of dropping diversity. The drop is large (e.g., Qwen POPE 49.5 vs. 69.0 for ZSPAPrune), which supports the paper's reason for adding diversity tokens.
### S3: Honest reporting of losses and an informative k sweep
The paper reports where its method loses to DivPrune (AI2D, TextVQA, §4.2) and shows the full k sweep in Table 2, so that a reader can see the sensitivity. Table 2 trends are monotone for GQA and POPE, which is a plausible sanity check on the implementation.
### S4: Efficiency is measured end to end
Table 3 reports measured E2E latency and peak memory rather than only token counts, which is the right type of evidence for an efficiency claim (though thin, see W4).

## Weaknesses

### W1 (most severe): The reported ZSPAPrune numbers use a per-benchmark k chosen on the reported splits
§4.2 says "we used the optimal ratio for each specific benchmark", and Table 1's Qwen row reproduces the best entry of each Table 2 row. The sweep and the reporting set are the same benchmark, and no tuning split is described. Against DivPrune's fixed setting this is an unequal comparison: DivPrune has no tunable knob, ZSPAPrune gets an oracle. The paper's own Table 2 shows that the claimed advantage is not robust to k: relative to DivPrune on Qwen (MMMU 42.6, GQA 48.2, POPE 65.7), ZSPAPrune is ahead on GQA only for k ≤ 0.2 (48.5) and ties at 0.3 (48.2); on POPE it is ahead at k = 0.1, 0.2, 0.4 (68.2, 69.0, 66.4), behind at 0.3 (65.3) and from 0.6 on (63.7 → 53.9). The "zero-shot" label is also strained: a benchmark-specific hyperparameter fitted with the benchmark's labels is not zero-shot.
- **Suggested Fix**: fix k once (e.g., from a held-out subset of a different dataset, or one value for all benchmarks) and report Table 1 with it, with the oracle-k numbers as a separate "upper bound" row. Cost: the Table 2 runs already exist for Qwen's three benchmarks; for the other benchmarks and models ≈ 30–40 GPU-hours.

### W2: No variance or significance evidence for gains of 0.1–1.3 points; the stated justification is wrong
The Reproducibility Statement says "a fixed random seed, which guarantees deterministic inference. As a result, statistical significance tests or error bars are not required for interpretation." Determinism removes run-to-run noise but not finite-sample noise in the benchmark: the Qwen gains over DivPrune are +1.3 (MMMU), +0.8 (GQA), +0.1 (ChartQA) points absolute (computed from Table 1), against sets of unknown size (Table 3 uses 900 MMMU samples). A paired bootstrap or McNemar test over per-sample correctness needs no extra training and would settle it. The k sweep on MMMU varies only between 43.0 and 43.9 for k ∈ [0.1, 0.8] (Table 2), yet §4.3 interprets the peak at 0.4 as "a need for a relatively balanced mix of tokens". With n = 900 one point is nine questions; this ordering is likely noise.
- **Suggested Fix**: paired bootstrap 95% CIs on every Table 1/2/4 difference. Cost: negligible (post-processing existing per-sample outputs).

### W3: Baselines are too few to support "matches or surpasses the state-of-the-art"
Only DivPrune and a self-built relevance-only top-k are compared (§4.1). No existing prompt-aware or training-free text-guided pruning method is run, although §2 itself lists PAR and GlimpsePrune, and the paper says "no existing method represents the 'All-in Task-Relevance' approach". The self-built baseline gets no tuning of its own (e.g., no similarity measure variants). Attention-based pruning (FastV, cited) is also not run. The SOTA wording in the abstract and Conclusion rests on a single competitor.
- **Suggested Fix**: add at least FastV and one or two text-guided training-free methods at the same keep rate and prompts, under the same harness. Cost ≈ 20–40 GPU-hours.

### W4: Efficiency evidence is a single model, single benchmark, three memory samples
Table 3 covers LLaVA-1.5-7B on MMMU only (900 samples), while the paper's headline model is Qwen2.5-VL. Hardware, batch size, precision, output length and whether pruning time is inside the "E2E latency" are not stated. ZSPAPrune is slower than DivPrune (264.2 vs. 256.9 ms, +7.3 ms, as the text admits), and peak memory is identical to DivPrune's. The memory saving is 172, 234 and 174 MB of about 14.3 GB (1.2%, 1.6%, 1.2%, computed from Table 3), described as "a clear and substantial reduction" (§4.4). FLOPs, prefill time and time-to-first-token are not reported.
- **Suggested Fix**: report latency, TTFT, FLOPs and peak memory for all three models at several keep rates, with hardware and batch size; tone down "substantial". Cost ≈ 10 GPU-hours.

### W5: Single keep rate (90%) and three ablation settings
Every experiment prunes 90%. The abstract and introduction say "up to 90%" and "even at an aggressive token keep rate of just 10%", but no 50%, 75% or 95% results exist, so no accuracy-vs-budget curve. The only ablation is pooling (Table 4, two benchmarks, one model). There is no ablation of the similarity function, of where in the model pruning happens, of the diversity stage's reference set, or of k = 0 (which should reproduce DivPrune and would check the shared implementation).
- **Suggested Fix**: add keep rates {25%, 11%, 5%} and the k = 0 and random-core-set controls. Cost ≈ 40 GPU-hours.

### Error Log

| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E6 | Reproducibility Statement vs. Appendix A | "Appendix A describes them." (re "clearly documented architectural and implementation modifications") | Appendix A.1–A.3 only describe the three VLMs; no modification of any model is described | Cross-referenced (two locations) | High | MAJOR | Describe the insertion point and any code changes, or remove the claim |
| ERR-2 | E6 | Table 3 / §4.4 vs. Appendix B.2.1 | "Table 3: Efficiency analysis on LLaVA 1.5-7B across MMMU. (900 samples)" | B.2.1 states MMMU "comprises 11.5K questions" and uses "the official test split"; 900 samples is a subset or a different (validation-sized) split. Which split Table 1 uses is therefore unclear | Cross-referenced | Medium | MAJOR | State the exact split and sample count for every table |
| ERR-3 | E6 | §4.2 vs. Table 1 (LLaVA-NeXT) | "its behavior and relative trends ... are highly consistent with the LLaVA-1.5-7B model" | GQA retention is 89.3% on LLaVA-1.5 but 68.3% on LLaVA-NeXT, whose 90% pruning leaves a far larger absolute budget | Recomputed from Table 1 (52.4/58.7; 41.0/60.0) | High | MINOR | Explain the LLaVA-NeXT GQA drop, or say how pruning is applied to the AnyRes grid |
| ERR-4 | E6 | Table 1 | "25.4 / 100.0%" (LLaVA-1.5 MMMU, all three pruned rows 25.3–25.4) | Not an error by itself; see Question 2 (original scores near chance make retention percentages uninformative) | Observed | Low | n/a | Moved to Questions |

(ERR-4 is listed only to show that it was demoted to Question 2 under the precision rules.)

*Claim-to-evidence map (compressed).*

| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | novel zero-shot plug-and-play method | §1, abstract | Eq. 4–9, Table 1 | Partially: training-free yes; "zero-shot" strained by per-benchmark k |
| C2 | "tunable balance" improves representativeness | §1 | Table 2 | Partially: GQA and POPE peak at the most diversity-heavy k tested; the benefit of relevance is ≤ 0.8 on GQA (49.0 vs. 48.2) |
| C3a | "matches or surpasses the state-of-the-art" | abstract | Table 1 vs. one baseline | Partially: ties DivPrune on LLaVA models, +0.35 mean absolute on Qwen, one baseline only |
| C3b | "minimal accuracy loss" at 90% | abstract | Table 1 | Contradicted for Qwen: POPE 85.8 → 69.0, TextVQA 77.9 → 54.9, AI2D 80.6 → 65.3 |
| C3c | "significant reductions in GPU memory footprint and inference latency" | abstract | Table 3 | Partially: latency −27.7% on one model; memory −1.2%…−1.6%; no gain over DivPrune |

*Recomputed*: Qwen mean retention ZSPAPrune (91.1+85.0+81.0+80.4+70.5+100.0)/6 = 84.67%; DivPrune (88.4+83.5+82.3+76.6+73.6+99.9)/6 = 84.05% (+0.62 points). Qwen mean absolute score 59.32 vs. 58.97 (+0.35). Table 3: 365.6 − 264.2 = 101.4 ms (27.7%), matches the text.

**Minor:** "MMVU" for MMMU in the Reproducibility Statement; symbol k means a token count in Eq. 6 and a ratio in §4.3; "Qwen2.5-VL-Instruct" caption wording.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Per-benchmark k on reported splits, single baseline, no variance |
| Clarity | 2 | Readable, but k is defined two ways and key setup facts are missing |
| Significance | 2 | Small gains over DivPrune, at one keep rate |
| Originality | 2 | DivPrune with a relevance-selected seed set |

## Dimension Scores (0–100)
**Pool position:** better than about 35% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline comparison depends on an oracle k on the reporting splits and is against one baseline; gains over it are mostly within plausible benchmark noise.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 46 | Developing | Method is sound as stated, but the evaluation protocol favors the method (W1) and statistics are waved away (W2) |
| Clarity & Presentation | 56 | Competent | Clear narrative; ambiguous k, missing setup details |
| Novelty & Originality | 46 | Developing | See R2; incremental over DivPrune |
| Significance & Impact | 46 | Developing | Useful if it held up; evidence is thin |
| Experimental Validation | 42 | Developing | One real baseline, one keep rate, three ablated settings, no variance |
| Reproducibility | 42 | Developing | No code, no hardware, no prompts, no resolution; "Upon acceptance" release |
| Ethical Compliance | 60 | Competent | Nothing at stake; limitations not discussed |

## Questions for Authors
1. How was k chosen for AI2D, TextVQA, ChartQA and for both LLaVA models (no sweeps are shown)? Would results with one fixed k (e.g., 0.2) still beat DivPrune on all six benchmarks? A yes would raise my Experimental Validation by about 10 points.
2. The unpruned LLaVA-1.5 scores on MMMU (25.4) and AI2D (29.1) in Table 1 are near what chance would give on multiple-choice questions, and the unpruned ChartQA (44.0) is below all pruned variants. What prompt and answer-extraction rule were used? As I recall, the Qwen2.5-VL report's unpruned MMMU/ChartQA numbers are well above 48.2/73.8 [verify]; what image resolution limits were used?
3. For five of twelve LLaVA cells ZSPAPrune and DivPrune are identical to the decimal (LLaVA-1.5 MMMU, GQA, POPE; LLaVA-NeXT MMMU, GQA). What k was used there, and does k → 0 recover DivPrune exactly?
4. Is the "Mean" arm of Table 4 run at the benchmark's best k (the values 43.9 and 69.0 equal Table 1), and were the "None"/"Max" arms also tuned? How is the score defined for "None" (a max, a mean over prompt tokens)?
5. Which prompt tokens enter Eq. 4 (system prompt, template, answer options)?

## Limitations Assessment
**Partially.** There is no limitations section; the loss on AI2D/TextVQA is explained but not framed as a limitation, and the dependence on benchmark-specific k is not discussed.

## Ethics Review Flag
**No.**

## Overall Score
**3**: Borderline Reject. Sound simple idea with an evaluation that does not isolate its benefit; fixing k and adding variance and baselines could change this.

## Confidence
**4**: Confident; I could not see the figures or any supplement beyond Appendix A–C.

---

# Peer Review Report (Reviewer 2)

## Paper: ZSPAPrune: Zero-Shot Prompt-Aware Token Pruning for Vision-Language Models
## Reviewer: Dr. Ravindra Pillai, Domain (industrial research lab, South Asia; fictional persona)
## Expertise: token reduction in ViTs and VLMs; attention- and diversity-based pruning
## Date: 2026-11-10

## Summary
The paper presents a two-stage, training-free pruner: top-k tokens by cosine similarity to the mean-pooled prompt, then a greedy farthest-point style fill. It argues that attention-based and diversity-based pruners are "prompt-agnostic" and that the right objective balances task relevance and diversity. Experiments cover three 7B VLMs at 90% pruning against DivPrune and a self-built relevance-only baseline.

## Literature-check note
The literature check could not run (arXiv API unreachable, see header). The novelty delta table below is built from the paper's own related work and the reviewer's knowledge; entries are marked `[verify]` and no `related_search.py` outputs (similarity, novelty profile, baseline scout) exist. Neither field-snapshot claims nor novelty verdicts below are search-based.

## Strengths
### S1: Clear, well-motivated two-stage structure
The relevance-then-diversity pipeline (§3.3.2–3.3.3) is easy to state and to implement. Figure 1 (judged from its caption "Trade-off between task relevance and information diversity") and the text in §1 give an intuitive account of why either extreme is incomplete.
### S2: The relevance-only baseline supports the diversity part of the story
Table 1 shows large drops when diversity is removed (e.g., Qwen2.5-VL POPE 49.5 vs. 69.0, LLaVA-1.5 TextVQA 11.6 vs. 33.0). This is genuine evidence that pure prompt-similarity top-k over projected tokens is a poor selector.
### S3: Relevant model coverage
Testing an older (LLaVA-1.5), a high-resolution (LLaVA-NeXT) and a recent (Qwen2.5-VL) model is a good choice for a plug-and-play claim.
### S4: Candid reporting where DivPrune wins
AI2D and TextVQA losses are reported with an explanation (§4.2), which is more useful to readers than a cherry-picked table.

## Weaknesses

### W1: Novelty is incremental, and the paper's own framing of prior work is partly inaccurate
The method is DivPrune's max-min diversity selection (cited, described in §2 as solving an MMDP) with the selected set initialised by a relevance top-k. The related-work argument that existing methods are "predominantly ... prompt-agnostic" (§1) is undercut by the paper's own discussion of PAR and GlimpsePrune (§2, "Prompt-Aware Pruning"). FastV is described as using "the attention scores from the final layer of a Vision Transformer" (§2), yet the cited FastV title is "An image is worth 1/2 tokens after layer 2" (bibliography). As I understand it, FastV prunes inside the LLM after an early layer using attention that includes the text query, so it is neither a vision-encoder method nor plainly prompt-agnostic [verify against the FastV abstract]. The positioning ("fills this gap", §2) therefore overstates the gap.
- **Suggested Fix**: correct the FastV description; state precisely what is new relative to DivPrune (the conditioning of MMDP on a relevance-selected seed) and to the training-free, text-guided methods listed below.

### W2: Missing training-free, text-guided and "dominant plus contextual" baselines
The "All-in Task-Relevance" baseline is introduced because "no existing method represents" that approach (§4.1). I recall earlier training-free methods that select visual tokens by similarity to the text query (e.g., a CLIP-similarity-based text-guided reduction method) and text-guided sparsification inside the LLM (SparseVLM, ICML 2025) [verify]; VisionZip (CVPR 2025) keeps "dominant" tokens and adds "contextual" ones, a structure close to core plus diversity, but without the prompt [verify]. See Missing References. The comparison set (DivPrune only) cannot support a state-of-the-art statement.
- **Suggested Fix**: run SparseVLM-type and VisionZip-type baselines at the same keep rate and prompt pipeline; at minimum cite and differentiate them.

### W3: The theoretical motivation is weaker than presented
§1 calls MAE's reconstruction from 25% of patches "a strong theoretical basis for token compression". MAE masks input patches for a reconstruction objective in the encoder; it says nothing about how many projected tokens an LLM decoder needs for question answering, and it is not a theoretical result. Eq. 5 further assumes that cosine similarity between the mean of the LLM's text-token embeddings and the vision projector's output is a meaningful relevance score ("aligned with the text semantic space", §3.3). The projector is trained by next-token prediction, not for geometric alignment with the input embedding table. The only evidence is indirect (relevance-only top-k is bad, Table 1; relevance helps a little at k = 0.1–0.2, Table 2), and the paper never tests whether the top-scored tokens are relevant (e.g., against ground-truth regions on GQA or POPE).
- **Suggested Fix**: add a control with a random or prompt-shuffled core set, and a relevance-quality check on a grounded benchmark; replace "theoretical basis" with "motivation".

### W4: The central "must be prompt-aware" conclusion is not supported by Table 2
§4.3 concludes "effective token pruning ... must be prompt-aware". In Table 2, GQA and POPE are best at the most diversity-heavy k tested (0.1 and 0.2) and decline monotonically as relevance share grows, so the evidence is compatible with "diversity does most of the work, and a small relevance share adds up to 0.8 points on GQA (49.0 vs. DivPrune 48.2)". On LLaVA-1.5 and LLaVA-NeXT the two methods coincide on five of twelve cells (Table 1). On the two benchmarks where the authors expect relevance to matter most (TextVQA, AI2D: question-driven OCR and diagrams), ZSPAPrune loses to DivPrune (§4.2), and the paper's explanation ("less strongly task-driven") is the reverse of what a prompt-aware method should show for TextVQA.
- **Suggested Fix**: evaluate k = 0, prompt-shuffled and random-seed controls; moderate the conclusion.

### W5: Domain details (Qwen2.5-VL, FastV) in Appendix A and §2 may be inaccurate
Appendix A.1 says Qwen2.5-VL "connects a Vision Transformer (ViT) encoder to the language model backbone using a cross-attention mechanism". To my knowledge Qwen2.5-VL uses a patch-merger MLP before the LLM, not cross-attention [verify against the cited technical report]. This matters because Eq. 2–3 assume projected tokens are concatenated with text tokens, and the paper does not say where pruning is inserted for Qwen2.5-VL. *(Stated as a question for the authors, not an error, because I cannot check the report here.)*
- **Suggested Fix**: describe the insertion point per model (after the projector/merger? per image tile for LLaVA-NeXT?).

### Novelty delta table (from the paper's own related work and knowledge; no search results)
| Claimed contribution | Closest prior work | What that work already does | What is actually new here | Cited and differentiated? |
|---|---|---|---|---|
| C1 method | DivPrune (CVPR 2025, cited) | MMDP diversity selection, training-free | A relevance top-k seed set before the same greedy diversity step | Cited, weakly differentiated |
| C1 method | SparseVLM (ICML 2025) [verify] | Text-guided, training-free pruning of visual tokens inside the LLM | Pruning before the LLM; mean-pooled prompt cosine | Not cited |
| C1 method | VisionZip (CVPR 2025) [verify] | Training-free, dominant plus contextual tokens | Prompt-guided core | Not cited |
| C2 framing | Conditional-diversity pruning, CDPruner (arXiv mid-2025) [verify] | Conditions diversity selection on the instruction | Same framing with a simpler, greedy form | Not cited. Recent preprint (< 6 months before the cutoff): worth discussing only, not a required comparison |
| C3 result | PAR, GlimpsePrune (cited) | Prompt-aware pruning | Not compared empirically | Cited, not compared |

Per-claim verdict without search: C1 incremental, C2 medium-to-incremental, C3 not novel as a result type. A caveat that the search did not run means "no verdict of 'known'" is warranted.

## Missing References
*Network unavailable: none could be verified with `related_search.py verify`; all are `[verify]` and given only as pointers.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Zhang et al., "SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference", ICML 2025 `[verify]` | Training-free, text-guided pruning; directly contradicts "no existing method" and the prompt-agnostic framing |
| Critical | Yang et al., "VisionZip: Longer is Better but Not Necessary in Vision Language Models", CVPR 2025 `[verify]` | Training-free dominant-plus-contextual token selection, a standard strong baseline in 2025 |
| Important | Xing et al., "PyramidDrop: Accelerating Your Large Vision-Language Models via Pyramid Visual Redundancy Reduction", CVPR 2025 `[verify]` | Progressive attention-based pruning inside the LLM |
| Important | Song et al., "Less is More: A Simple yet Effective Token Reduction Method for Efficient Multi-modal LLMs" (TRIM) `[verify]` | CLIP-similarity text-guided selection; close to the relevance-only baseline |
| Important | Wen et al., "Stop Looking for Important Tokens in Multimodal Language Models: Duplication Matters More" (DART), 2025 `[verify]` | Duplication-aware pruning; closest in spirit to diversity selection |
| Helpful | Zhang et al., "Beyond Attention or Similarity: Maximizing Conditional Diversity for Token Pruning in MLLMs" (CDPruner), arXiv 2025 `[verify]` | Recent preprint; worth discussing, not required |
| Helpful | Shang et al., "LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models", 2024 `[verify]` | Earlier adaptive selection plus merging |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evaluation is narrow; claims exceed evidence |
| Clarity | 3 | Readable; positioning partly inaccurate |
| Significance | 2 | Small, tuned gains over one prior method |
| Originality | 2 | Incremental over DivPrune |

## Dimension Scores (0–100)
**Pool position:** better than about 33% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: incremental over DivPrune, thin comparison set, and the conclusion drawn ("must be prompt-aware") is not shown by Table 2.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Algorithm sound; the alignment assumption in Eq. 5 is untested |
| Clarity & Presentation | 58 | Competent | Clear; prior-work descriptions need correcting |
| Novelty & Originality | 42 | Developing | Two training-free ideas combined; incremental |
| Significance & Impact | 44 | Developing | Pruning at 90% is a crowded line; gains are small |
| Experimental Validation | 44 | Developing | See R1 |
| Reproducibility | 50 | Competent | Algorithm simple enough to re-implement; details of insertion point missing |
| Ethical Compliance | 62 | Competent | Nothing at stake |

## Field snapshot (knowledge only, unverified; no kept results)
Before the cutoff, visual token pruning moved from attention-score selection inside the LLM (FastV-style) to pre-LLM, training-free selection by redundancy or diversity (VisionZip, DivPrune, DART-style). Prompt-conditioned variants appeared in 2024–2025. A paper in 2025 is judged by gains at several keep rates (e.g., 192/128/64 tokens on LLaVA-1.5) against several strong training-free baselines on 10+ benchmarks, plus cost measurements. A +0.3 mean difference over one baseline is incremental. [verify]

## Questions for Authors
1. What exactly separates ZSPAPrune from running DivPrune conditioned on a top-k seed set, and does the authors' claim that no existing method uses relevance-only selection hold against text-guided training-free methods? A clear differentiation would raise my Novelty score.
2. Where is pruning inserted for Qwen2.5-VL and LLaVA-NeXT (before the merger, after, per tile)?
3. Does a random or prompt-shuffled core set yield similar accuracy at k = 0.1–0.2? If it does, the prompt-aware claim fails.
4. Appendix A.1 describes Qwen2.5-VL as connected via "cross-attention"; is that what the technical report states?

## Limitations Assessment
**Partially.** No limitation section; no discussion of where relevance can be harmful (TextVQA, AI2D losses are explained away).

## Ethics Review Flag
**No.**

## Overall Score
**3**: Borderline Reject. An easy-to-use idea, but incremental, with weak positioning and a conclusion beyond the evidence.

## Confidence
**4**: Confident on the field; unable to verify the new references offline.

---

# Peer Review Report (Reviewer 3)

## Paper: ZSPAPrune: Zero-Shot Prompt-Aware Token Pruning for Vision-Language Models
## Reviewer: Dr. Isabela Cardoso, Perspective (embedded-systems and HCI group, university, South America; fictional persona)
## Expertise: on-device inference; relevance feedback and query-conditioned retrieval
## Date: 2026-11-10

## Summary
The paper proposes a query-conditioned pruning step for the visual tokens of a VLM: choose the tokens most similar to the question, then fill the budget with visually diverse tokens. It shows that, at 90% pruning, a relevance-only selector collapses while the hybrid retains 70–100% of unpruned accuracy depending on the benchmark and model, and reports modest latency savings on LLaVA-1.5.

## Strengths
### S1: A familiar and sensible idea transplanted into VLMs
Query-conditioned selection with a diversity term is the shape of maximal marginal relevance in retrieval and of coreset-style selection in active learning. Importing it into VLM token pruning is natural, and §1 and Figure 1 (caption) explain the intuition well.
### S2: Practical positioning
Training-free, attention-free, and applicable to three VLMs makes the approach attractive for deployment on constrained hardware (§1: "zero-shot and resource-constrained settings"). Mean pooling plus cosine similarity is cheap.
### S3: The k sweep is a useful practical result
Table 2 and Figure 3 (caption) show that the preferred relevance share depends on the task: ratio near 0.4 for MMMU, much lower for GQA and POPE. A knob that practitioners can set per workload is a real deployment asset, if a default can be given.
### S4: Candid trade-off between ZSPAPrune and DivPrune
The latency overhead (+7.3 ms, §4.4) is stated plainly.

## Weaknesses

### W1: No deployment-realistic evaluation of the benefit claimed
The abstract claims "significant reductions in GPU memory footprint and inference latency". Table 3 shows latency down 27.7% on LLaVA-1.5 (365.6 → 264.2 ms), but ZSPAPrune is slower than DivPrune, and the memory change is 172–234 MB of about 14.3 GB (≈ 1.2–1.6%, computed). The hardware, batch size and precision are missing, and no result is given for the model (Qwen2.5-VL) where accuracy is reported as most favorable. For deployment the relevant numbers (TTFT, throughput on edge GPUs, long-input or multi-image cases) are missing.
- **Suggested Fix**: report TTFT, throughput and peak memory at several keep rates and for all three models, on one data-center and one edge-class GPU; reword the memory claim.

### W2: The knob k needs a default, otherwise the method is not plug-and-play
The paper says a "controllable balance" is a feature (C2), but deployment of a pruner on arbitrary user prompts has no benchmark label to pick k from. Table 2 shows that the wrong k loses 15 points of POPE (69.0 at 0.2 vs. 53.9 at 0.9). Without an automatic rule (the Conclusion lists "automated tuning of this balance" as future work), the "plug-and-play" and "zero-shot" claims in the abstract and contribution 1 are only partly delivered.
- **Suggested Fix**: propose and evaluate a prompt-dependent rule for k (e.g., from the entropy of the relevance scores) or one default value tested on all benchmarks.

### W3: Assumptions about the shared embedding space and mean-pooled prompts
Eq. 4–5 compare a mean-pooled prompt vector to projected visual tokens. In IR, mean-pooled query embeddings are a known weak baseline, and multi-aspect queries (a question with options, as in MMMU and AI2D) dilute into one vector. The paper tests only pooling variants (Table 4) on two benchmarks, not whether the prompt contains template boilerplate (system text, "Answer with a single word") that dominates the mean. Multi-vector or max-over-query-terms scoring, and relevance computed from the LLM's own early-layer attention, are natural alternatives from retrieval and are not discussed.
- **Suggested Fix**: strip templates before pooling; compare against ColBERT-style late-interaction scoring (as a method class) and against an early-layer cross-attention relevance.

### W4: Failure analysis and broader impact are absent
There is no limitations or broader-impact paragraph. Pruning 90% of the tokens degrades OCR-heavy and hallucination-sensitive tasks substantially (Qwen2.5-VL TextVQA 77.9 → 54.9, POPE 85.8 → 69.0, Table 1). For safety-relevant uses (document reading, accessibility) a method that silently drops 20–30% of accuracy deserves a warning, and a hallucination-sensitive benchmark (POPE) is reported only as F1.
- **Suggested Fix**: add a limitations section with failure cases; report precision and recall on POPE.

### Missing perspective on additional modalities
The paper says VLMs process "image or video inputs" (§1), but all experiments are on single images; multi-image and video settings, where token redundancy is largest, are untested.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gains small and tuned per benchmark |
| Clarity | 3 | Clear writing |
| Significance | 2 | Practical value if k can be set |
| Originality | 2 | Known IR idea, new to this setting |

## Dimension Scores (0–100)
**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: sensible, practical idea, but the evidence for the claimed practical benefits is thin.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Sound mechanism; assumptions untested |
| Clarity & Presentation | 60 | Competent | Clear |
| Novelty & Originality | 48 | Developing | Adaptation of a known idea |
| Significance & Impact | 52 | Developing | Practical appeal; limited evidence |
| Experimental Validation | 46 | Developing | Narrow |
| Reproducibility | 50 | Competent | Simple method, missing setup details |
| Ethical Compliance | 60 | Competent | No major issue; limitations not discussed |

## Questions for Authors
1. Can k be set automatically from the prompt? Evidence of a single default working across six benchmarks would raise my Significance score.
2. What are TTFT and throughput on Qwen2.5-VL at 90% pruning?
3. How does the method behave on multi-image or video inputs, which §1 motivates?

## Limitations Assessment
**No.** There is no limitations section.

## Ethics Review Flag
**No.**

## Overall Score
**3**: Borderline Reject. An appealing practical idea, but I would need a default for k and real efficiency evidence.

## Confidence
**3**: Fairly confident; I am not a specialist in the pruning literature.

---

# Peer Review Report (Reviewer 4)

## Paper: ZSPAPrune: Zero-Shot Prompt-Aware Token Pruning for Vision-Language Models
## Reviewer: Dr. Jonas Albrecht, Generalist (vision group, public research institute, Northern Europe; fictional persona)
## Expertise: visual recognition; vision-language understanding
## Date: 2026-11-10

## Summary (contribution in one paragraph)
The paper offers a training-free way to cut the visual tokens a VLM processes by 90%. It first keeps the visual tokens closest to the question, then adds tokens that look least like those already kept, controlled by a ratio k. It reports that this matches or slightly improves on a diversity-only method (DivPrune) on several benchmarks and models, and runs faster and uses less memory than the unpruned model.

## Venue fit and criteria checklist (ICLR)
| Criterion | Met / partly / not met | Location |
|-----------|------------------------|----------|
| Soundness: claims supported by the experiments | Partly: gains over DivPrune are small and tuned; "minimal accuracy loss" contradicted on Qwen | Table 1, §4.2 |
| Contribution: a new idea or finding | Partly: a combination of two known pruning ideas | §3.3, §2 |
| Presentation: self-contained, consistent notation | Partly: k has two meanings; setup details missing | Eq. 6, §4.3 |
| Evidence breadth (models, benchmarks, budgets) | Partly: three models, six benchmarks, one keep rate | §4.2 |
| Reproducibility: code, settings | Not met at submission (code "Upon acceptance") | Reproducibility Statement |
| Limitations stated | Not met | no section |

## Strengths
### S1: Clear problem statement and motivation
§1 puts the efficiency problem and the limitation of prompt-agnostic selection in plain terms. Figure 1 (caption) and Figure 2 (title only) aim at the relevance/diversity trade-off.
### S2: Readable, well-organised paper
Section order (Method, Experiments, Insights, Efficiency, Ablation) is easy to follow, and the algorithm is short enough to implement from Eq. 4–9.
### S3: Multiple models and benchmarks, with relative retention
Table 1's "score / % of original" format makes cross-model comparison easy, and covers six benchmarks over three VLMs.
### S4: Informative negative observations
The k sweep (Table 2) and the admission that ZSPAPrune loses on AI2D and TextVQA help a reader decide when to use it.

## Weaknesses

### W1: The main empirical claim is weaker than the abstract and conclusion say
The abstract promises "matches or surpasses the state-of-the-art with only minimal accuracy loss, even when pruning up to 90%". On Qwen2.5-VL, the mean retained accuracy is 84.7% (computed: 508.0/6), with POPE at 80.4% and TextVQA at 70.5% (Table 1). Against DivPrune the mean advantage is 0.6 retention points (84.67 vs. 84.05), and on LLaVA-1.5/NeXT the methods tie on most cells. The introduction's "approximately 90% of the original accuracy" holds only for some model–benchmark cells. The comparison is to one baseline, so "state-of-the-art" is unsupported.
- **Suggested Fix**: reword to "competitive with DivPrune, up to +3.3 points POPE on Qwen2.5-VL" and give per-model averages; present the AI2D/TextVQA losses in the abstract.

### W2: Missing setup details block understanding
The paper does not say where pruning is applied in each VLM, how k is defined (Eq. 6 uses k as a count of core tokens, §4.3 as a ratio in [0.1, 0.9], and k̃ is the count of diversity tokens with budget = k + k̃), what prompt tokens enter Eq. 4, which resolution settings are used for Qwen2.5-VL and LLaVA-NeXT, and what LLM sits inside LLaVA-NeXT-7B (Appendix A.3 lists "Mistral-7B and Yi-34B", §4.2 calls it "a derivative version of LLaVA-1.5-7B"). The Eq. 8 text restricts the redundancy maximum to "y ∈ I_core" while the prose says "all previously selected tokens", so it is unclear whether newly added diversity tokens are included.
- **Suggested Fix**: add an algorithm box with explicit variables and an appendix with model-specific insertion points, prompts and resolution settings.

### W3: Overinterpretation of small differences and an untested explanation
Table 2's MMMU row varies by under one point across k ∈ [0.1, 0.8], yet §4.3 builds a story ("MMMU ... is highly dependent on the preservation of core, task-relevant tokens"). ChartQA's "22.7% improvement" over the unpruned LLaVA-1.5 is explained as "noise reduction" with no test, even though the relevance-only baseline also beats the original (50.3 vs. 44.0): a common-cause explanation (answer formatting or the original model's weak score under this harness) is at least as likely. Appendix A.1's "cross-attention" description of Qwen2.5-VL should be checked against the cited report [verify].
- **Suggested Fix**: label these explanations as hypotheses, or test them (e.g., random pruning on ChartQA).

### W4: Reproducibility statement does not match the content
The statement says "Appendix A describes them" for "architectural and implementation modifications", but Appendix A only describes the models; it names "MMVU" instead of MMMU; and it says error bars "are not required" because inference is deterministic. Code and the evaluation platform are promised "Upon acceptance".
- **Suggested Fix**: provide an anonymous repository at submission, correct the statement.

**Minor:** Figure 2 is only a title in the extracted text; "e.g. ViT" typography; "Qwen2. 5-vl" in the reference list; "LLaVa"/"LLaVA" spelling; Figure 3 repeats Table 2.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence thin for the claim |
| Clarity | 3 | Mostly clear; k ambiguous |
| Significance | 2 | Modest |
| Originality | 2 | Incremental |

## Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: clear, simple, but a typical rejected-submission profile: small gain over one baseline, narrow evaluation.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Sound idea; protocol gaps |
| Clarity & Presentation | 58 | Competent | Clear flow; ambiguity in k and insertion point |
| Novelty & Originality | 46 | Developing | Combination of two known mechanisms |
| Significance & Impact | 48 | Developing | Useful tool; small gain |
| Experimental Validation | 46 | Developing | One baseline, one keep rate |
| Reproducibility | 48 | Developing | No code, missing settings |
| Ethical Compliance | 60 | Competent | Nothing at stake |

## Questions for Authors
1. What is the exact definition of k in Eq. 6 versus §4.3, and what happens at k = 0?
2. Why are the LLaVA-1.5 numbers for MMMU and AI2D (25.4, 29.1) so low for the unpruned model, and is that consistent with the model's reported results? A convincing answer removes my concern about the retention percentages.
3. Could you add results at 50% and 75% pruning? A flat advantage over DivPrune across rates would raise my Significance score.

## Limitations Assessment
**No.** No limitations section.

## Ethics Review Flag
**No.**

## Overall Score
**3**: Borderline Reject. A clearly written paper whose claims and evidence do not yet line up; a revision with fixed k, more baselines and keep rates could be a reasonable ICLR paper.

## Confidence
**3**: Fairly confident; not a token-pruning specialist.

---

# Devil's Advocate Report

## Paper: ZSPAPrune: Zero-Shot Prompt-Aware Token Pruning for Vision-Language Models
## Reviewer: Dr. Amara Nwosu (evaluation-methodology group, university, West Africa / UK; fictional persona)

## Steelman
Existing token pruners ignore the question being asked. A cheap, training-free step that first keeps the tokens most relevant to the prompt and then restores coverage with diversity tokens gives accuracy on par with or above the diversity-only state of the art while pruning 90% of the tokens, on three VLM families, and the relevance-only ablation shows that diversity is needed.

## Core Argument Chain
1. Prior pruners are prompt-agnostic (§1, §2).
2. Cosine similarity between mean-pooled prompt embeddings and projected visual tokens measures task relevance (Eq. 4–5, §3.3).
3. A top-k relevance core plus greedy diversity fill balances relevance and diversity (§3.3.2–3.3.3).
4. With the balance tuned per benchmark, ZSPAPrune matches or beats DivPrune on most benchmarks and models (Table 1, §4.2).
5. The relevance-only baseline is much worse, so diversity is needed; the k sweep shows task-dependent optimal balance (Table 1, Table 2).
∴ Effective VLM token pruning "must be prompt-aware" and balanced (§4.3), and ZSPAPrune is state of the art or competitive with large efficiency gains (abstract, Conclusion).

## Strongest Counter-Argument
Even if every number in Tables 1–4 is correct, they do not show that the *prompt* does any work. The relevance stage is validated only indirectly. What the tables show is that diversity matters (relevance-only top-k collapses) and that DivPrune with a small, benchmark-tuned relevance seed is about as good as DivPrune, sometimes by a few points. For GQA and POPE the best k is the most diversity-heavy value swept (0.1 and 0.2) and accuracy falls monotonically as the relevance share grows (Table 2: GQA 49.0 → 42.8; POPE 68.2 → 53.9). The sweep stops at 0.1, one step from pure DivPrune, and its edge over DivPrune is 0.8 on GQA (49.0 vs. 48.2). On LLaVA-1.5 and LLaVA-NeXT the two methods give identical numbers in five of twelve cells (Table 1), and on the two benchmarks where the question determines where to look (TextVQA, AI2D) ZSPAPrune loses. A simpler account fits all of this: any small, partly arbitrary seed set followed by farthest-point filling gives DivPrune-like results, and the best k is picked on the evaluation data, which creates the apparent gain.

The test that would distinguish the accounts is absent: replace the relevance core by a random core of the same size, and replace the prompt by another sample's prompt. If accuracy at k = 0.1–0.2 does not change, prompt-awareness contributes nothing, and the paper's title, its Contribution 2 and the "must be prompt-aware" conclusion fail. Meanwhile, the selection of k on the reporting splits (DA-C1) can by itself produce the 0.8–3.3-point gains that the paper counts as evidence. The authors need to answer both: show a fixed k that wins, and show that the relevance signal, not the filling procedure, is responsible.

## Issue List

### CRITICAL Issues

| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| DA-C1 | Evidence (criterion 3: selection on the reported split) | §4.2 (Table 1 paragraph); Table 1 Qwen row; Table 2; §4.3; Appendix B.2.1–B.3.3 | Verbatim: "the sole exception of the relevance-diversity balance coefficient for ZSPAPrune, for which we used the optimal ratio for each specific benchmark" (§4.2). The Qwen row of Table 1 (MMMU 43.9, GQA 49.0, POPE 69.0) equals the maximum of the matching Table 2 row (k = 0.4, 0.1, 0.2), so k was selected by its score on the benchmark that is then reported. The paper states the reported splits are the "official test split" (MMMU B.2.1, POPE B.2.3) or the standard test-dev (GQA B.2.2); no validation split for tuning is mentioned. Per the decision table: best-scoring option, chosen by score, producing the headline numbers (Table 1, the abstract's "matches or surpasses" and §4.2's "accuracy gains of ... 3.8% on POPE"). The comparison does not hold at the other swept values: GQA is above DivPrune (48.2) only at k = 0.1 and 0.2; POPE is above DivPrune (65.7) at 0.1, 0.2 and 0.4 only (65.3 at 0.3, ties at 0.5, 63.7 to 53.9 for 0.6–0.9). POPE has no validation split, so it is a true held-out test set under the rule. The field-practice exception (public-label validation split reported because test labels are hidden) could at most soften the MMMU and GQA cells, not POPE, and does not apply to the paper's own wording ("official test split"). | Fix k once from a split not used for reporting (e.g., a held-out sample from another dataset or from the training data), or use one k for every benchmark; report Table 1 with it, keeping the oracle-k row as an upper bound | New experiments (the fixed-k runs exist only for three Qwen benchmarks, Table 2; AI2D, TextVQA, ChartQA and both LLaVA models need new runs) |

### MAJOR Issues

| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic / Evidence | §4.3; Table 2; Table 1 | "Must be prompt-aware" does not follow: the prompt's causal role is untested (random-core, shuffled-prompt controls absent); GQA and POPE peak at the most diversity-heavy k tested; the two question-driven OCR/diagram benchmarks favor DivPrune (evidence supports a weaker claim) | Add random-core, shuffled-prompt, k = 0 controls; narrow the conclusion |
| DA-M2 | Overgeneralisation | Abstract, §1, Conclusion | "matches or surpasses the state-of-the-art with only minimal accuracy loss": one competitor; Qwen2.5-VL loses 19.6 (POPE), 15.3 (AI2D), 23.0 (TextVQA) points absolute at 90% (Table 1) | Narrow to "competitive with DivPrune"; show a keep-rate curve |
| DA-M3 | Statistics | Reproducibility Statement | "statistical significance tests or error bars are not required for interpretation": determinism does not remove test-sample noise; gains are 0.1–1.3 points (Qwen; absolute); MMMU subset in Table 3 has 900 samples | Paired bootstrap CIs |
| DA-M4 | Claim distortion (E5) | §1 (para. 1); §2 | MAE reconstruction from 25% of patches is called "a strong theoretical basis for token compression"; FastV described as using a ViT's final-layer attention while the cited title says "after layer 2"; "predominantly ... prompt-agnostic" while §2 itself reviews prompt-aware work | Rewrite; cite and differentiate text-guided methods |
| DA-M5 | Alternative explanation | §4.2 (ChartQA) | The 22.7% ChartQA gain over the unpruned LLaVA-1.5 is attributed to "noise reduction"; the relevance-only baseline also beats the original (50.3 vs. 44.0), and unpruned MMMU/AI2D (25.4/29.1) are near chance level; an evaluation-harness effect is at least as plausible | Report prompt and answer-extraction rules; sanity-check the unpruned numbers against published values |
| DA-M6 | Evidence | §4.4, Table 3 | "clear and substantial reduction in the overall memory footprint": 1.2–1.6% of peak memory (computed), identical to DivPrune; latency worse than DivPrune; one model | Reword; measure all models |

### MINOR Issues

| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | §4.4 vs. §2 | DivPrune is described as solving an MMDP (§2) and as "single-pass similarity matrix calculation" (§4.4) |
| DA-m2 | Consistency | Reproducibility Statement | "MMVU" (should be MMMU); "Appendix A describes them" refers to modifications that are not described |
| DA-m3 | Consistency | Appendix A.3 vs. §4.2 | LLaVA-NeXT backbone not specified (Mistral/Yi vs. "derivative version of LLaVA-1.5-7B") |
| DA-m4 | Scope | §1, §4.1 | "image or video inputs" and "For image-based tasks" suggest video evaluation; none is reported |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| ZSPAPrune vs. DivPrune on Qwen MMMU | "2.7%" (§4.2) | retention 91.1 − 88.4 = 2.7 points; absolute 43.9 − 42.6 = 1.3 | Yes, but retention points, not accuracy |
| POPE gain | "3.8%" | retention 80.4 − 76.6 = 3.8; absolute 69.0 − 65.7 = 3.3 | Yes, same caveat |
| Relevance-only gap on LLaVA-1.5 GQA | 15.7% | 89.3 − 73.6 = 15.7 | Yes |
| TextVQA relevance-only drop | "approximately 54%" | 83.5 − 29.4 = 54.1 | Yes |
| Qwen mean retention | not reported | ZSPAPrune 84.67% vs. DivPrune 84.05% (+0.62) | derived |
| Latency | −101.4 ms | 365.6 − 264.2 = 101.4 (27.7%) | Yes |
| Memory | 172/234/174 MB | 1.2%, 1.6%, 1.2% of 14336.8/14398.8/14318.8 MB | Yes (small) |
| "approximately 90% of the original accuracy" | §1 | Qwen mean 84.7%; LLaVA-NeXT mean 91.5%; LLaVA-1.5 mean 98.9% (inflated by ChartQA 122.7) | Partly |

## Ignored Alternative Explanations
- Diversity filling, not relevance, produces the results; the "core" acts as an arbitrary seed set.
- Per-benchmark k (DA-C1) accounts for the headline gains.
- Evaluation-harness artefacts (answer extraction, resolution limits) explain the weak unpruned baselines and the ChartQA "improvement".
- At 90% pruning, differences of 0.1–1.3 points are within benchmark sampling noise.

## Missing Stakeholder Perspectives
Practitioners who deploy VLMs for document reading and accessibility: the method silently loses 20–30% accuracy on OCR-heavy and hallucination-sensitive tasks (Qwen2.5-VL TextVQA, POPE, Table 1), and no guidance is given on when not to prune.

## Observations (Non-Defects)
The monotone Table 2 trends and the large relevance-only deficit (Table 1) are internally coherent and suggest a working implementation. The paper's disclosure of its tuning and of the AI2D/TextVQA losses makes the problem visible, which is a point in the authors' favor, though disclosure does not make the numbers valid. Appendix C declares LLM use.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 38 | Selection on reported splits (DA-C1), untested alignment assumption, no variance |
| Clarity & Presentation | 52 | Readable; ambiguous k; reproducibility statement inaccurate |
| Novelty & Originality | 40 | Incremental over DivPrune; prior work mischaracterised |
| Significance & Impact | 42 | Gains small, one keep rate |
| Experimental Validation | 36 | One baseline; no controls; oracle k |
| Reproducibility | 38 | No code, no hardware, prompts or resolution |
| Ethical Compliance | 58 | Nothing at stake; no limitations section |

**Pool position:** better than about 28% of submissions to ICLR. Deciding evidence: the headline gains rest on benchmark-level selection of k and the relevance signal's contribution is untested.

## Overall: 2 | Confidence: 4

---

## Phase 1.5: Literature Check

Mode: strict (requested), ran as **off** (arXiv API unreachable). Queries: 1 claim query issued, 0 results; 0 baseline, 0 expansion queries; `verify`, `similarity`, `novelty`, `scout` and `coverage` could not run; gaps left open: all. Reviewers 2 and the DA relied on knowledge; every entry is marked `[verify]`. The Domain Reviewer's addendum (novelty delta table, missing references, field snapshot) is included in the R2 report above, built without search results.

## Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | Initial "no random seeds" | Rewritten (W2) | The paper states a fixed seed; the real issue is finite-sample noise, not seeds |
| R1 | ERR-4 (near-chance original scores) | Moved to Questions (Q2) | Low confidence; an interpretation of harness behavior, no verifiable error |
| R2 | "Qwen2.5-VL uses a patch merger, not cross-attention" | Rewritten as question (W5, Q4) | Reviewer cannot check the cited report; Hard Rule 10 |
| R2 | FastV description (W1) | Kept, with `[verify]` | The cited bibliography title supports it; the statement about FastV's mechanism is recalled, not checked |
| R3 | "No video experiments" | Moved to Minor/Missing-perspective line | Not a claim of the paper beyond a motivating sentence |
| R4 | Figure 2 not visible | Moved to Minor | Figure-extraction limit, not a paper defect |
| R4 | Related-work insufficiency | Kept as pointer to R2-W2 (merged in Phase 2) | Duplicate |
| DA | DA-M5 (ChartQA) | Rewritten as alternative explanation | "Noise reduction" is the authors' untested mechanism, not an error |

Scores unchanged.

### Issue list and consensus map (Synthesizer, Part A)

| Issue | Sources | Class |
|-------|---------|-------|
| k tuned per benchmark on reported splits; "zero-shot" label | R1-W1, DA-C1, R3-W2 (k needs a default), R2-W4 (partly) | CONSENSUS-4 (DA-CRITICAL) |
| Too few baselines, SOTA wording unsupported | R1-W3, R2-W2, R4-W1, DA-M2 | CONSENSUS-4 |
| No variance/significance; incorrect justification | R1-W2, DA-M3, R4-W4 | CONSENSUS-3 |
| Prompt-awareness not shown (controls missing); "must be prompt-aware" | R2-W4, DA-M1, R1-W5 (k = 0), R3-W3 | CONSENSUS-4 |
| Efficiency evidence thin and overclaimed | R1-W4, R3-W1, DA-M6 | CONSENSUS-3 |
| Incremental novelty; prior work mischaracterised (FastV, MAE) | R2-W1, R2-W3, DA-M4 | CONSENSUS-3 |
| Missing setup details, k ambiguity, repro statement mismatch | R4-W2, R4-W4, R1 ERR-1/ERR-2, DA-m2/m3 | CONSENSUS-3 |
| Weak unpruned baselines / ChartQA artefact | R1-Q2, DA-M5, R4-Q2 | CONSENSUS-3 (question-level) |
| Single keep rate, few ablations | R1-W5, R4-Q3 | CONSENSUS-2 |
| No limitations / failure analysis | R3-W4, R1, R4, R2 limitations | CONSENSUS-4 (minor) |
| Qwen2.5-VL description possibly wrong | R2-W5, R4-W3 | CONSENSUS-2 (low confidence) |

SPLIT issues: none (R3 is more positive on practicality but cites the same gaps). Outcome may hinge on: DA-C1, "prompt-awareness not shown", and the SOTA/efficiency overclaims.

**Official output (BEFORE the EIC, no weights, DA-C1 provisionally upheld; `before.json`):** official mean rating 2.80; official composite 47.9 → band 2; DA cap 3.

---

# Phase 2: EIC Meta-Review (Prof. Tobias Reinholt)

# Editorial Decision

## Paper: ZSPAPrune: Zero-Shot Prompt-Aware Token Pruning for Vision-Language Models
## Submission ID: iclr26-5Y8PMEeAkv
## Date: 2026-11-10
## Target Venue: ICLR (2026 cycle) | Paper Type: empirical
## Review Team (fictional personas): EIC Tobias Reinholt; R1 Methodology Mei-Ling Qiu, R2 Domain Ravindra Pillai, R3 Perspective Isabela Cardoso, R4 Generalist Jonas Albrecht, DA Amara Nwosu

---

## Decision: Borderline Reject (3), ICLR rating 4 on the {0,2,4,6,8,10} scale (5 on {1,3,5,6,8,10}); scale status: secondary

**Official ratings** (shown to authors): R1 3, R2 3, R3 3, R4 3, DA 2 → mean 2.80 · official composite 47.9
**EIC assessment** (internal): weighted rating 2.75 → starting point 3 · weighted composite 47.2 → band 2 (cross-check) · **DA ceiling**: 3 · **Final (EIC)**: 3
**EIC pool position**: better than about 38% of ICLR submissions.

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A simple, training-free, attention-free pruner whose structure (relevance core plus diversity fill) is easy to adopt. It was run on three VLM families, it improves on DivPrune on several Qwen2.5-VL benchmarks (POPE +3.3 points), and its relevance-only baseline gives a clear reason for the diversity stage. The paper reports the losses openly.
- **Against acceptance:** The headline ZSPAPrune numbers come from a per-benchmark k picked on the same evaluation data (DA-C1), the comparison set is one baseline, the paper never shows that the prompt does any work (no random-core or shuffled-prompt control), the gains are 0.1–1.3 points on Qwen (identical to DivPrune in five of twelve LLaVA cells), variance is dismissed, and efficiency evidence is thin and overstated.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| k chosen per benchmark: quote exists | R1-W1, DA-C1 | §4.2, line "we used the optimal ratio for each specific benchmark" | Verified | Searched the text; quote present verbatim |
| Table 1 Qwen ZSPAPrune = best cell of Table 2 | R1-W1, DA-C1 | Table 1 (43.9/49.0/69.0), Table 2 (max 43.9 at 0.4, 49.0 at 0.1, 69.0 at 0.2) | Verified | Both values written; same numbers |
| Comparison vs. DivPrune fails at other k | DA-C1 | Table 2 vs. Table 1 (DivPrune 42.6/48.2/65.7) | Verified | GQA ahead only at 0.1–0.2 (tie 0.3); POPE ahead at 0.1, 0.2, 0.4; MMMU ahead for k ≤ 0.8, behind at 0.9 (41.6). MMMU claim is more robust than R1/DA implied |
| POPE and MMMU are "official test split" | DA-C1 | B.2.1, B.2.3 | Verified (as stated) | Table 3's 900 MMMU samples conflict with B.2.1's 11.5K questions, so the real MMMU split is unclear (R1 ERR-2: Partly correct, medium confidence) |
| No separate tuning split | R1, DA-C1 | Full-text search for `validation`, `tuned`, `held-out` | Verified | Only TextVQA "validation split" (B.3.2) as a reporting split |
| "Minimal accuracy loss" at 90% | DA-M2, R4-W1 | Table 1 Qwen | Verified | POPE 85.8 → 69.0; TextVQA 77.9 → 54.9; AI2D 80.6 → 65.3 |
| Qwen mean retention 84.67 vs. 84.05 | R4-W1, R1 | Table 1 | Verified | Recomputed from the table |
| Variance statement | R1-W2, DA-M3 | Reproducibility Statement | Verified | "statistical significance tests or error bars are not required for interpretation" is quoted exactly |
| Memory saving 1.2–1.6%; latency worse than DivPrune | R1-W4, R3-W1, DA-M6 | Table 3, §4.4 | Verified | 172/14336.8 = 1.2%; ZSPAPrune 264.2 ms vs. 256.9 ms |
| FastV mis-described | R2-W1, DA-M4 | §2, bibliography | Partly correct | The cited title ("after layer 2") contradicts "final layer of a Vision Transformer"; the exact mechanism of FastV is recalled, not checked. Not decision-relevant |
| "Appendix A describes them" has no content | R1 ERR-1 | Reproducibility Statement, Appendix A.1–A.3 | Verified | Appendix A has only model descriptions |
| Qwen2.5-VL "cross-attention" | R2-W5, R4-W3 | Appendix A.1 | Unverifiable here | Both reviewers flagged it as a question; kept as a question |
| Prompt-awareness not tested (no random/shuffled control) | R2-W4, DA-M1 | §4.3, Tables 2, 4 | Verified | No such control anywhere in the paper; GQA and POPE peak at the most diversity-heavy k tested |
| R3's "significant reductions in memory and latency" accepted as practical value | R3-S2, W1 | Table 3 | Overstated | R3's own W1 corrects this; S2 stays positive on deployment appeal without data |
| Literature-based points (SparseVLM, VisionZip, etc.) | R2 | Missing References | Not verifiable (no network) | All marked `[verify]`; treated as "worth discussing / expected comparisons" for the decision, never as a score-lowering fact on their own |

*Text-overlap / injection:* none; the integrity scan was clean.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Decisive point (per-benchmark k) and recomputations verified; error-log entries verified, one (ERR-2) medium confidence |
| R2 (Domain) | 3 | 4 | 1.0 | Mostly sound; the FastV and Qwen points rest on recall, handled as questions |
| R3 (Perspective) | 3 | 3 | 0.75 | Praises "clear" deployment value in S2 that Table 3 does not support (partly corrected in its own W1); calibration somewhat lenient (pool 48) |
| R4 (Generalist) | 3 | 3 | 1.0 | Sound and calibrated; no overstated points |
| DA | 2 | 4 | 1.25 | CRITICAL issue verified against the text, with the right locating quotes; counter-argument (untested relevance) survives my check |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| DA-C1 (per-benchmark k selected on reported splits) | Yes. §4.2 quote verified verbatim; the chosen k is the best-scoring option in Table 2 and the same values are the headline Qwen numbers in Table 1; the main comparison with DivPrune does not hold at other swept values (GQA, POPE). Decision-table row: best-scoring, chosen by score, produces headline numbers → CRITICAL. POPE has no validation split. I cannot downgrade: not "not the best-scoring"; main claim not robust across the sweep; headline configuration not fixed in advance; no separate validation split; not ablation-only. The effect size (0.8–3.3 points) is not a reason to downgrade. | **Upheld** | New experiments: fixed-k results exist only for three Qwen benchmarks in Table 2 (and at k = 0.1–0.2 they in fact beat DivPrune on all three); AI2D, TextVQA, ChartQA and both LLaVA models need new runs |

### Final Decision and Justification
The EIC-weighted rating is 2.75, so the starting point is **3**. The composite (47.2) falls in band 2; the rating and composite differ by one step, near the band boundary of 50 and 35–49, and I named no verified issue that the ratings missed, so I keep the starting point and note the composite as a borderline-reject signal. The DA ceiling is 3 (DA-C1 upheld, needs new experiments), and 3 sits on it. **Final: 3, Borderline Reject.** My pool position is about 38: the paper is clearly written and has a working, easy-to-adopt idea, but it has the profile of a typical rejected submission at ICLR: small gains over one baseline (mean +0.35 points absolute on Qwen), headline numbers from an oracle-selected hyperparameter, no control showing that the prompt matters, a thin baseline set and no variance. A revision that fixes k, adds text-guided and VisionZip-type baselines, keep-rate curves, bootstrap CIs and a random-core control could be a reasonable ICLR paper; the fixed-k Table 2 numbers at 0.1–0.2 suggest the Qwen gains may survive. Because the literature check could not run, I did not lower any score for missing references, as the venue rules and the skill require.

---

## Score Summary

### Official Scores and EIC Assessment (script output, `scores.json` with `--venue iclr --final 3`)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 46 | 50 | 52 | 50 | 38 | 47.2 | 46.2 | 14 |
| Clarity & Presentation | 56 | 58 | 60 | 58 | 52 | 56.8 | 56.2 | 8 |
| Novelty & Originality | 46 | 42 | 48 | 46 | 40 | 44.4 | 43.9 | 8 |
| Significance & Impact | 46 | 44 | 52 | 48 | 42 | 46.4 | 45.7 | 10 |
| Experimental Validation | 42 | 44 | 46 | 46 | 36 | 42.8 | 42.1 | 10 |
| Reproducibility | 42 | 50 | 50 | 48 | 38 | 45.6 | 44.6 | 12 |
| Ethical Compliance | 60 | 62 | 60 | 60 | 58 | 60.0 | 59.9 | 4 |
| **Composite** | 47.2 | 48.7 | 51.6 | 49.9 | 41.9 | **47.9 (before)** | **47.2 (after)** | |

No dimension has a spread above 20.

Reviewer weights (EIC, internal): R1 25%, R2 20%, R3 12%, R4 17%, DA 25% (confidence × quality weight).
EIC-weighted rating 2.75 (before EIC weights: 2.78 with all weights 1.0 and the DA cap applied); official mean 2.80.

### Target-Venue Scores (ICLR, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 1 / 2 / 1 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); venue-weighted composite 46.9; band 3 → 3 after DA cap |

Scale labels are shown with their `secondary` status; ICLR's rating wording should be checked against the current form.

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "ZSPAPrune: Zero-Shot Prompt-Aware Token Pruning for Vision-Language Models" to ICLR. Reducing the visual-token cost of vision-language models is a timely problem, and a training-free, attention-free approach is attractive.

**Overall Assessment:** The panel found the idea clear and practical and valued the relevance-only baseline and the open reporting of losses. The panel was concerned that the headline gains rest on a balance coefficient chosen per benchmark on the evaluation data, that the comparison has a single competitor, and that the role of the prompt itself is not isolated.

**Key Strengths Identified by Reviewers:**
1. A simple, training-free, attention-free method, usable across three VLM families (R1, R2, R3, R4).
2. The relevance-only baseline and Table 2 reveal that diversity is needed and that the balance matters (R1, R2, R3).
3. Candid reporting of cases where DivPrune is better and of latency overhead (R1, R2, R3).

**Key Concerns Requiring Attention:**
1. Per-benchmark selection of k on the reported splits; "zero-shot" and "plug-and-play" need a fixed default (R1, R3, DA: CONSENSUS-4, DA-CRITICAL).
2. Narrow comparison and overstated claims ("state-of-the-art", "minimal accuracy loss", memory) (R1, R2, R4, DA: CONSENSUS-4).
3. The prompt's contribution is not shown by a random-core or shuffled-prompt control, and Table 2 trends are consistent with diversity doing most of the work (R2, DA, R1).
4. No variance or significance analysis; reasoning given in the Reproducibility Statement is not sound (R1, R4, DA).

**Critical Challenge (Devil's Advocate):** The reported benefits over DivPrune could come from selecting k on the benchmarks themselves and from the diversity stage alone, rather than from prompt-awareness. The authors need to show a fixed k that wins and a control showing that the prompt matters.

**Decision: Borderline Reject (3).** The upheld critical issue needs new experiments, so the ceiling is 3. A revision with a fixed or validation-selected k, text-guided and training-free baselines at several keep rates, bootstrap confidence intervals, a random-core control and a corrected efficiency claim would materially change the assessment. Please refer to the Revision Roadmap.

Sincerely,
Prof. Tobias Reinholt
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| k tuned per benchmark on reported splits; no default | R1, R3, DA (R2 partly) | CONSENSUS-4 (DA-CRITICAL) |
| Too few baselines, SOTA wording unsupported | R1, R2, R4, DA | CONSENSUS-4 |
| Prompt-awareness not demonstrated | R1, R2, R3, DA | CONSENSUS-4 |
| No limitations / failure analysis | R1, R2, R3, R4 (limitations assessments) | CONSENSUS-4 |
| No variance or significance testing | R1, R4, DA | CONSENSUS-3 |
| Efficiency evidence thin | R1, R3, DA | CONSENSUS-3 |
| Incremental novelty, partly inaccurate positioning | R2, R4, DA | CONSENSUS-3 |
| Setup details and k ambiguity | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Practical value of efficiency | R3 (S2) | R1, DA | Table 3 shows latency −27.7% vs. unpruned on one model, no advantage over DivPrune, memory −1.2–1.6%; R1/DA verified; R3 weight 0.75 |
| How serious the k selection is | DA (CRITICAL) | R1 (W1, not labeled critical) | Applied the DA decision table; upheld |

### Score Spread Discussion
No dimension has a spread above 20 (largest: Technical Rigor 14, driven by the DA's 38).

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-C1 | CRITICAL | per-benchmark k selected on reported splits | Yes (R1-W1, R3-W2) | Upheld | New experiments |
| DA-M1 | MAJOR | "must be prompt-aware" unsupported; controls missing | Yes (R2-W4) | n/a | n/a |
| DA-M2 | MAJOR | SOTA and "minimal accuracy loss" overclaim | Yes (R4-W1, R1-W3) | n/a | n/a |
| DA-M3 | MAJOR | no variance, flawed justification | Yes (R1-W2, R4-W4) | n/a | n/a |
| DA-M4 | MAJOR | MAE "theoretical basis", FastV mis-described | Partly (R2-W1, W3) | n/a | n/a |
| DA-M5 | MAJOR | ChartQA "noise reduction" untested; weak unpruned baselines | Partly (R1-Q2, R4-Q2) | n/a | n/a |
| DA-M6 | MAJOR | memory claim overstated | Yes (R1-W4, R3-W1) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | k chosen per benchmark on reporting splits; "zero-shot" | DA-C1, R1-W1, R3-W2 | §4.2, Table 1, Table 2 | Fix k once (held-out source or one global value); report oracle-k separately; report Table 1 for all models with it | Medium; ≈ 30–40 GPU-h | Partly (Qwen fixed-k numbers exist for three benchmarks) |
| R2 | Prompt-awareness not isolated | DA-M1, R2-W4 (Verified: no control exists) | §4.3, Tables 2, 4 | Random-core, prompt-shuffled, and k = 0 controls (k = 0 should reproduce DivPrune) | Low–Medium; ≈ 15 GPU-h | Yes |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Single competitor; SOTA wording | R1-W3, R2-W2, R4-W1, DA-M2 | Add FastV, a text-guided training-free method, a VisionZip-type method (all `[verify]`); narrow claims | Medium; 20–40 GPU-h | Partly |
| S2 | No variance/significance; wrong justification | R1-W2, DA-M3, R4-W4 | Paired bootstrap CIs on Tables 1, 2, 4; remove the "not required" sentence | Low; negligible compute | Yes |
| S3 | Keep rate and ablations | R1-W5, R4-Q3 | Keep rates 50/25/11/5%; similarity-function, insertion-point ablations | Medium; ≈ 40 GPU-h | Partly |
| S4 | Efficiency evidence | R1-W4, R3-W1, DA-M6 | TTFT, throughput, FLOPs, memory for all three models; hardware/batch/precision; reword memory claim | Low–Medium; ≈ 10 GPU-h | Yes |
| S5 | Setup ambiguity and reproducibility statement | R4-W2, R4-W4, R1 ERR-1/ERR-2 | Define k once; algorithm box; insertion point per model; prompts, resolution, LLaVA-NeXT backbone; exact splits; correct "Appendix A" and "MMVU" | Low | Yes |
| S6 | Prior-work mischaracterisation; positioning | R2-W1, R2-W3, DA-M4 | Correct FastV description, replace "theoretical basis", differentiate from SparseVLM/VisionZip/DART; discuss CDPruner as concurrent (`[verify]`) | Low | Yes |
| S7 | Weak unpruned baselines, ChartQA | R1-Q2, DA-M5 | Report prompts and answer extraction; compare unpruned scores with published ones; test "noise reduction" with random pruning | Low–Medium | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Automatic prompt-dependent k | R3-W2 | Rule from relevance-score entropy |
| N2 | Multi-aspect prompts, template tokens | R3-W3 | Strip templates; compare late-interaction scoring |
| N3 | Limitations and failure cases | R3-W4, R4 | Add a section; POPE precision/recall |
| N4 | Video and multi-image evaluation | R3, DA-m4 | Add or drop the video wording |
| N5 | Typos and notation (MMVU, Qwen2. 5, "LLaVa") | R4 | Fix |
| N6 | DivPrune complexity description | DA-m1 | Make §2 and §4.4 consistent |

## Estimated Revision Effort
- Priority 1: 2 items, about 45–55 GPU-hours, 1 week.
- Priority 2: 7 items, about 70–90 GPU-hours, 1–2 weeks.
- Priority 3: 6 items.
- **Total estimated revision time**: roughly 2–3 weeks.

*(Post-Review Analysis / Gap Scout: not requested, not run.)*
