# Academic Paper Review: PureKV (ICLR, full mode)

*Date: 2026-11-10 · Skill academic-paper-reviewer v2.10.1 · Request: full review, skip confirmation, literature check: strict, cutoff 2025-09-24.*
*All five reviewer passes were performed sequentially in one shared model context (no subagents); they are role-based passes, not independent agents. Figures were not available: figure-dependent claims are judged from captions and text only and are marked as such.*

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | PureKV: Plug-and-Play KV Cache Optimization with Spatial-Temporal Sparse Attention for Vision-Language Large Models |
| Primary Discipline | ML / Computer Vision → efficient inference for video-language models (KV cache compression) |
| Secondary Discipline(s) | Sparse attention kernels; efficient transformer systems |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Training-free KV eviction (recent window + top-h), cross-layer reuse of lower-layer attention scores weighted by value norm, fixed spatial-temporal sparse attention mask for prefill |
| Target Venue | ICLR 2026 cycle, top-tier conference (stated by user); profile key `iclr` (scale status: secondary) |
| Venue-Specific Notes | Submissions/reviews public; ICLR accept rate ≈ 27% (venue_profiles); none other |
| Paper Maturity | Submission-ready in form, but with an unfinished evaluation (no limitations section, details missing) |
| Ethics-Relevant Content | None specific (public benchmarks MVBench, AVSD; no human-subject data added) |

**Integrity scan (Phase 0, `integrity_scan.py`):** no reviewer-directed text or hidden characters found. Reviewers read the (identical) redacted copy. During reading I also saw no instructions addressed to reviewers or AI systems.

**Literature check:** mode `strict`, cutoff 2025-09-24, arXiv API, 6 queries of the 12-query budget (claim C1, claim C2, baseline "multimodal KV cache compression", expansion "token selection early layers", plus a refused 5-word query that did not count). `related_search.py benchmarks` returned no benchmarks (MVBench and AVSD identified by hand; MVBench scouted through the multimodal KV-cache query). `coverage` gap left open: no prior work kept from 2021–2022. Run after the five reports were drafted; its results feed the Domain addendum only.

### Paper memory (shared, factual)

- **Claims (as stated, §1 and Abstract):**
  - C1: "lightweight, attention-score-free token importance estimator" that reuses lower-layer attention × value norm for high layers and is FlashAttention-compatible (§1 contributions, §3.1, Eq. 1–4).
  - C2: ST-SpAttn, a spatial-temporal sparse attention for prefill that "purifies" the KV cache and speeds up prefill (§3.2, Fig. 2c).
  - C3: "5.0× KV cache compression and 3.16× prefill acceleration, with negligible quality degradation" on VideoLLaMA2 and Qwen2.5-VL (Abstract; §4).
- **Setup facts:** MVBench, "14 tasks" extracted (§4.1), but each of Tables 1 and 2 reports 10 task columns, and the sets differ between the two models; metric "ROUGE" (§4.1) vs "average accuracy" (App. 6.3); models VideoLLaMA2 and Qwen2.5-VL-7B; baselines H2O, SnapKV, StreamingLLM, FastV, LOOK-M (LOOK-M absent from Table 2); hardware one A100 40 GB (§4.1). Not stated after search: number of frames / tokens per video, w and h values, CLIE layer and ST-SpAttn start layer used for the main tables, prompts, decoding settings, sample counts, seeds/variance, code link, limitations section, how Table 3 latencies were measured (batch, resolution, kernel), whether baselines use FlashAttention.
- **Headline numbers:** 5.0× (=20% budget, Tables 1–2); 3.16× prefill (Table 3: 0.1190 vs 0.0376 ms/token); VideoLLaMA2 20% avg 0.6189 vs full 0.6635 (Table 2); Qwen2.5-VL 20% avg 0.5429 vs full 0.5136 (Table 1).
- **Appendix adds:** Table 6 (baselines + "PureKV"), Table 5 (AVSD, one score per method), Table 7 + Fig. 6 (sparse-pattern variants).
- **Unverifiable:** all figures (Fig. 3–6 contents, incl. Fig. 4 and 5 heat-maps beyond their extracted numbers); Eq. 3/4 norm notation is garbled by extraction (the text says an L2 norm of V).

### Claimed contributions
1. C1 attention-score-free cross-layer importance estimator (CLIE) with value-norm weighting.
2. C2 ST-SpAttn spatial-temporal sparse attention that also accelerates prefill.
3. C3 large-scale experiments showing 5.0× compression, 3.16× prefill speed-up, negligible degradation.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Ingrid Valtonen, technical university (Northern Europe)
- **Seniority / Expertise**: senior faculty / efficient inference, multimodal learning, area chair at top ML conferences
- **Role**: reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style**: wants the claim to match the measurement; tolerant of single-benchmark papers only if the claim is scoped to it

### Reviewer 1 (Methodology): Dr. Lukas Bernardsson, industrial ML-systems lab (Northern Europe)
- **Seniority / Expertise**: mid-career industry scientist / LLM/VLM inference benchmarking, latency measurement methodology
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: insists on matched settings, measured latency and stated protocols

### Reviewer 2 (Domain): Prof. Yuna Takeda-Moreau, vision-language group, large public university (East Asia)
- **Seniority / Expertise**: senior faculty / KV-cache and token pruning for VLMs, video LLM benchmarks
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: checks every cited work against what it actually is

### Reviewer 3 (Perspective): Dr. Amara Nwosu-Lindgren, computer-architecture / embedded systems group (North America)
- **Seniority / Expertise**: mid-career faculty / GPU kernels, memory-bound inference, edge deployment
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: constructive, asks "what happens on real hardware at real lengths?"

### Reviewer 4 (Generalist): Dr. Felix Haddad, vision research group, mid-sized research university (Middle East)
- **Seniority / Expertise**: mid-career / video understanding (not KV compression)
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: typical PC member; weighs weaknesses against what ICLR usually accepts

### Devil's Advocate: Dr. Soledad Ibarra-Kim, industrial research lab (Latin America)
- **Seniority / Expertise**: senior industry scientist / evaluation methodology, causal reasoning about ablations
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: rigorous, never hostile

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Independent Reviews

---

# Peer Review Report

## Paper: PureKV: Plug-and-Play KV Cache Optimization with Spatial-Temporal Sparse Attention for Vision-Language Large Models
## Reviewer: Dr. Lukas Bernardsson, Reviewer 1 (Methodology) (industrial ML-systems lab, Northern Europe; fictional persona)
## Expertise: VLM inference benchmarking; latency and memory measurement; evaluation protocols
## Date: 2026-11-10

---

## Summary
The paper proposes PureKV, a training-free KV-cache compression scheme for video-language models. It scores tokens in a few lower layers using the attention that a recent window of queries pays to earlier tokens, weights this by the L2 norm of V, and reuses that ranking in higher layers so that those layers can run FlashAttention/sparse kernels (Eq. 1–4, §3.1). A fixed sparse mask (first frame + current frame + same position in previous frame, §3.2) accelerates prefill and is argued to "purify" the cache. Experiments on MVBench subsets with VideoLLaMA2 and Qwen2.5-VL-7B report accuracy at 20% and 10% cache budgets (Tables 1–2), a latency table (Table 3), a one-task ablation (Table 4), and appendix integrations (Tables 5–7).

## Strengths

### S1: Practically motivated problem and a simple, training-free recipe
Reconciling score-based eviction with fused attention kernels is a real deployment concern (§1, Fig. 1). The recipe needs no training and only a few extra operations (Eq. 2–4), so it is easy to adopt if it works.

### S2: Reasonable measured prefill speed-up on one model
Table 3 reports 0.1190 ms/token for full-cache prefill versus 0.0376 at the 20% budget; recomputed 0.1190/0.0376 = 3.16×, matching the abstract. Decoding goes from 36.73 to 28.32 ms/token (1.30×).

### S3: Ablation and variant studies exist, and the arithmetic in the tables is internally consistent
Tables 4, 6 and 7 test the three components and several sparse-attention variants (Fig. 6). I recomputed the "Avg." column for the Full Cache and PureKV rows of Tables 1 and 2 and for all rows of Table 7: all match to the fourth decimal (e.g., Table 2 PureKV 20% sums to 6.1887/10 = 0.6189).

### S4: Cross-layer correlation analysis is a sensible sanity check (§3.3, Fig. 4)
Reporting a rank correlation between estimated and own-layer scores is more than many eviction papers do, even if its strength is overstated (W3).

## Weaknesses

### W1: The evaluation does not support "negligible quality degradation" or the headline compression/speed numbers (E5/E1)
(a) Table 2, VideoLLaMA2: Full Cache 0.6635, PureKV 20% 0.6189 (−0.0446, −6.7% relative) and PureKV 10% 0.5047 (−0.1588, −23.9%). Per-task drops are large (SC 0.6869→0.4751, UA 0.7851→0.6975, MA 0.6800→0.5814). Abstract: "with negligible quality degradation". §4.3 says PureKV "maintains stable performance on both VLLMs" at 10%; this holds for Qwen2.5-VL (Table 1) but not for VideoLLaMA2.
(b) "5.0×" is just the 20% budget setting (§4.2: "reduces KV cache memory usage by 80%"); no peak GPU memory is measured. "3.16×" is VideoLLaMA2-only, from one latency row, and nearly independent of the budget (0.0355–0.0376 ms/token across 50%–5%, Table 3), i.e. it comes from ST-SpAttn rather than from KV compression, and the abstract fuses the two.
- **Suggested Fix**: Scope the abstract to what Tables 1–3 show (per model and budget), report measured peak memory and end-to-end TTFT, and separate the prefill gain of ST-SpAttn from the memory gain of compression. Effort: low–medium, about 10 GPU-hours.

### W2: Metric, benchmark subset and baselines undermine comparability (E4/E6)
- §4.1: "We use ROUGE as the experimental evaluation metric" while App. 6.3 says "average accuracy of 0.6189". MVBench is multiple choice, so it is unclear how ROUGE is computed or answers are parsed.
- The Full Cache of Qwen2.5-VL scores 0.1674 on OS and 0.2859 on SC (Table 1), at or below what I would expect from chance on a multiple-choice task (number of options is not stated in the paper; I did not verify it).
- LOOK-M scores 0.0610 and 0.0389 average (Table 1), with several tasks at 0.00–0.03. A baseline this far below any plausible floor looks like a parsing/implementation failure, not information loss, and it inflates the apparent margin.
- §4.1 says "We extracted 14 tasks"; Table 1 has 10 columns (AC AP UA OI OS AL ST SC MA CI) and Table 2 a different 10 (AC AP UA AC SC OE MC MA EN CI), with "AC" appearing twice. The union is 14, but why each model gets a different subset, and why 6 of 20 tasks were dropped, is not explained. §4.1 lists five baselines; Table 2 has four (no LOOK-M).
- **Suggested Fix**: Report accuracy on the full 20-task MVBench for both models with a fixed answer-parsing rule; fix or drop LOOK-M; state the subset-selection rule. Effort: medium, ~30–60 GPU-hours.

### W3: No evidence on sample noise; many differences are within it (E8)
Every number is a single deterministic run with no confidence interval, test or sample count. Per-task differences of 0.01–0.03 (Table 1: OI, AL, ST, SC across methods) are the size one expects from sampling a few hundred questions per task (I believe MVBench has about 200 per task; not stated in the paper, [verify]; at that size one question is 0.005 and the standard error of a task accuracy near 0.5 is about 0.035). The surprising result that compressed PureKV beats the full cache on Qwen2.5-VL (0.5429 vs 0.5136 at 20%; 0.5360 at 10%) and that FastV also exceeds it (0.5154) is more consistent with noise or a weak full-cache reference than with real "purification".
- **Suggested Fix**: Paired bootstrap over questions for PureKV vs. each baseline and vs. full cache; report CIs in Tables 1–2. Effort: low (post-hoc on existing outputs if per-question results were saved).

### W4: Ablations are on one task and omit the key control (E4)
Table 4 is "on the Action Sequence (AC) task" only, one task of ten. The CLIE effect is 0.7311 vs 0.7307 (Qwen) and 0.7020 vs 0.6985 (VideoLLaMA2), i.e. +0.0004 and +0.0035, "no degradation" at best. The ST-SpAttn effect on Qwen is 0.7490 − 0.7311 = 0.0179 (about 3–4 questions at 200 per task). Missing: ST-SpAttn alone with the full (100%) cache versus dense full cache, which is needed to tell "purification helps compression" apart from "sparse attention changes the model". Table 6's "+PureKV" rows cannot isolate it either (it is unclear which PureKV components are added, App. 6.1).
- **Suggested Fix**: Full 2×2×2 ablation on the full task set at both budgets, plus ST-SpAttn-only at 100% budget. Effort: medium, ~20 GPU-hours.

### W5: Unstated hyperparameters and unreported selection protocol (E8)
After a text search for split/selection/tuning terms, the only selection-related content is §4.5/Fig. 5, a sweep over CLIE layer × ST-SpAttn start layer. Its numbers (.7588, .7595, …) coincide with the Action Sequence value in Table 2 (.7588) and Table 4 (.7588), and the text says "When the CLIE layer index is 2, PureKV performs the best". The paper does not state how the layers, w and h used in Tables 1–3 were chosen, or on which data; MVBench has no separate dev split. If the Fig. 5 sweep selected the configuration, one reported column is test-selected (effect on the 10-task mean is small but unquantified). §3.3 uses layer 1 for its analysis while §4.5 says layer 2 is best; w and h are never given. Table 3 gives no batch size, resolution, frame count or kernel.
- **Suggested Fix**: State the configuration per table, select it on a held-out set (e.g., tasks not reported), and give w, h, frames, prompts, decoding, latency protocol. Effort: low (text) plus ~10 GPU-hours.

### W6: Efficiency evidence is thin relative to the claim (E8)
Table 3 compares PureKV only against full cache, yet §4.2 states PureKV achieves "faster decoding speed than the comparison method"; no baseline appears in Table 3. "ms/token" for prefill is not defined; whether full cache uses FlashAttention is not stated; whether ST-SpAttn uses a block-sparse kernel (a dense masked FlashAttention gives no speed-up) is not stated. Decoding latency barely changes from 35% (28.50) to 5% (27.92 ms/token), suggesting KV size is not the bottleneck on these short MVBench clips.
- **Suggested Fix**: Latency/peak memory for all baselines on the same stack, long videos (hundreds to thousands of frames), and a description of the kernel. Effort: medium.

### Claim-to-evidence map

| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | Lower-layer scores suffice for higher-layer KV importance, FlashAttention-compatible | §1, §3.1, Fig. 4 | Spearman ρ mostly 0.2–0.4 (Fig. 4, text of §3.3); Table 4 CLIE rows on one task | Partially (weak correlation, no top-h overlap, one-task ablation) |
| C2 | ST-SpAttn "purifies" KV and improves compression | §3.2, Table 4, Table 7 | One-task ablation; Table 7 variants (avg 0.6189 vs 0.5504 spatial-only) | Partially (mechanism untested; no ST-SpAttn-only control) |
| C3 | 5.0× compression, 3.16× prefill, negligible degradation | Abstract, Tables 1–3 | Qwen ok; VideoLLaMA2 −4.5 pts (20%), −15.9 pts (10%) | Partially / Overstated |

### Error Log

| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E5 | Abstract vs Table 2 | "with negligible quality degradation" | VideoLLaMA2 avg 0.6635 → 0.6189 (20%) and 0.5047 (10%); drops of 6.7% and 23.9% relative | Recomputed from Table 2 | High | MAJOR | Narrow the claim |
| ERR-2 | E6 | §4.1 vs App. 6.3 | "We use ROUGE as the experimental evaluation metric." | Appendix reports "average accuracy of 0.6189" for the same number | Cross-referenced | High | MAJOR | State the metric and parser |
| ERR-3 | E6 | §4.1 vs Tables 1–2 | "We extracted 14 tasks from them to validate our algorithm" | Each table has 10 columns, different subsets; Table 2 lists "AC" twice | Cross-referenced | High | MINOR | Explain subset rule; fix header |
| ERR-4 | E1 | §4.2 vs Table 3 | "achieving faster decoding speed than the comparison method" | Table 3 contains no comparison method, only Full Cache and PureKV | Cross-referenced | High | MAJOR | Add baseline latencies or remove claim |
| ERR-5 | E5/E1 | App. 6.2 vs Table 5 | "Our proposed PureKV method significantly outperforms all other baselines." | 0.4265 vs SnapKV 0.4249 (+0.0016) and StreamingLLM 0.4249; Full Cache 0.4795 | Recomputed | High | MAJOR | Tone down; add significance |
| ERR-6 | E6 | §3.3 vs §4.5 | "We use the cumulative attention scores from the layer 1" | §4.5 says CLIE layer 2 is best; layer used for the main tables unstated | Cross-referenced | Medium | MINOR | State the layer |

### Questions on suspected issues (low confidence, not errors)
- Table 5: SnapKV and StreamingLLM are both 0.4249 to four decimals. A copy error, or genuinely identical?
- Table 2, 20%: StreamingLLM and PureKV share 0.7588 on the first task (also Table 4/Fig. 5); coincidence?

**Minor:** "StreamingLLm" spelling; "Object Existenc"; §4.3 says results are in "Table 1 and 2, respectively" for VideoLLaMA2 and Qwen2.5-VL but the order is reversed; Table 4 caption abbreviations.

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 1 | Evaluation does not support the central claim as worded (W1–W4); average of TR 44 and EV 36 maps to 1 |
| Clarity | 2 | Clear idea, but metric/subset/hyperparameter inconsistencies |
| Significance | 2 | Useful if it scales; evidence limited to short clips |
| Originality | 2 | Incremental combination (see R2) |

## Dimension Scores (0–100)

**Pool position:** better than about 32% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a single short-video benchmark with an unclear metric, a baseline scoring near zero, and a headline claim ("negligible degradation") contradicted by the paper's own Table 2.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 44 | Developing | Sound idea; weak validation of the mechanism and over-stated correlation evidence |
| Clarity & Presentation | 52 | Developing | Readable, but inconsistent metric/task naming |
| Novelty & Originality | 48 | Developing | Reuse of early-layer attention and value norms is known (R2) |
| Significance & Impact | 46 | Developing | Short clips only |
| Experimental Validation | 36 | Developing | One benchmark, subset changes by model, one-task ablation, broken baseline |
| Reproducibility | 38 | Developing | w, h, layers, frames, kernels, code absent |
| Ethical Compliance | 55 | Competent | Nothing at stake; but no limitations discussion |

## Questions for Authors
1. How is ROUGE computed on a multiple-choice benchmark, and how are answers parsed? Why does the Full Cache score 0.1674 on OS? (A clean accuracy protocol would raise my Experimental Validation score.)
2. Which CLIE layer, ST-SpAttn start layer, w and h were used for Tables 1–3, and were they chosen on MVBench tasks that are also reported?
3. What do Tables 1–2 look like on all 20 MVBench tasks with CIs? (A result holding on the full set would raise my score; an unstable one would lower it.)
4. What is the latency/peak memory of H2O/SnapKV/StreamingLLM/FastV on the same stack as Table 3?
5. What are the per-question results for ST-SpAttn alone at 100% budget?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No. The paper has no limitations section; scope (short clips, two models, fixed masks) is not discussed.

## Ethics Review Flag
**No**: no human-subject or misuse concern specific to this work.

## Overall Score
**2**: Promising practical idea, but the evidence does not support the headline claim and the evaluation protocol is under-specified.

## Confidence
**4**: Confident; I could not see the figures and the supplementary code, if any.

---

# Peer Review Report

## Paper: PureKV: Plug-and-Play KV Cache Optimization with Spatial-Temporal Sparse Attention for Vision-Language Large Models
## Reviewer: Prof. Yuna Takeda-Moreau, Reviewer 2 (Domain) (vision-language group, large public university, East Asia; fictional persona)
## Expertise: KV-cache eviction for VLMs; visual token pruning; video LLM benchmarks
## Date: 2026-11-10

---

## Summary
PureKV combines a cross-layer importance estimator (reuse of lower-layer attention × value norm) with a fixed spatial-temporal sparse attention mask for prefill, aimed at making KV compression compatible with FlashAttention and at "purifying" the cache. It is evaluated against H2O, SnapKV, StreamingLLM, FastV and LOOK-M on MVBench for two VLMs.

## Strengths

### S1: Right problem framing
The tension between score-based eviction and fused kernels is real and under-addressed in multimodal settings (§1, §2).

### S2: Video-specific structure is exploited
A pattern tied to frame structure (§3.2) is a plausible way to make prefill cheaper for video, and Table 7 shows that the choice of pattern matters (0.6189 vs 0.5504, 0.5302, 0.4995, 0.3794 for the alternatives).

### S3: Positioning against a recognizable baseline set
The comparison includes both text-origin (H2O, SnapKV, StreamingLLM) and VLM-specific (FastV, LOOK-M) methods (§4.1).

## Weaknesses

### W1: The main mechanisms are close to uncited or lightly differentiated prior work (novelty is incremental)
Literature check (strict, cutoff 2025-09-24), details in the addendum below:
- Early-layer attention used to decide what later layers keep: GemFilter (arXiv 2409.17422, prior arXiv-only) and the paper's own baseline FastV ("An image is worth 1/2 tokens after layer 2") follow this idea; the paper treats FastV only as a baseline and does not discuss the shared principle (§1, §2).
- Value-norm importance plus temporal redundancy for video KV caches: InfiniPot-V (NeurIPS 2025, arXiv 2506.15745; abstract: "removes temporally redundant tokens via Temporal-axis Redundancy (TaR) metric" and "keeps semantically significant tokens via Value-Norm (VaN) ranking") is uncited. It also frames the problem as training-free video KV compression. The paper asserts that previous work "ignor[es] the impact of V vectors on output" (§3.1, quote "Previous work mainly rely on attention based metrics to evaluate the importance of KV cache"), which this work contradicts in part.
- §2 asserts "No existing sparse attention scheme explicitly designs sparsity patterns" to synergize with KV pruning. I did not find a prior work in my results with exactly this pattern (see C2 verdict), but the statement is absolute and the search covers arXiv only.
- **Suggested Fix**: Cite and differentiate GemFilter, InfiniPot-V and the value-aware-pruning line of work; reword the novelty statements to "to our knowledge".

### W2: Prior work is mischaracterized, and citations do not support their claims (E7)
- §2: "kernelized methods (e.g., Linear Transformer (Wang et al., 2020))": the matching bibliography entry is Linformer (arXiv 2006.04768), a low-rank method, not a kernelized Linear Transformer.
- §2: "LSH-based Reformer (Chen et al., 2020)": the bibliography entry is Mongoose (a learnable LSH framework), not Reformer.
- §1/§2 cite knowledge-tracing papers (Zhou et al., 2025a, 2025b) as examples of *sparse attention*, and a talking-avatar paper (Chen et al., 2025) and a 3D Gaussian paper (Yu et al., 2024) as VLM applications; federated-learning and model-merging papers (Jiang et al., 2025; Li et al., 2025b) for "growing computational demands" of VLMs; a neuromorphic-hardware paper for quantization (Abreu et al., 2025). These look unrelated to the claims. I report this factually as a citation-quality concern for the editor; it does not alter my scores.
- "Alexandre et al., 2023" is the Mistral 7B entry with the first and last names swapped; "Tang et al." (§1) has no year.
- **Suggested Fix**: Audit all citations; replace unrelated ones with the actual sparse-attention and VLM-efficiency literature.

### W3: Baselines miss the closest KV-compression-for-VLM methods and are run inconsistently
VL-Cache (Tu et al., 2024) is cited in §2 but not compared. Newer multimodal/video KV methods (MEDA, NAACL 2025; InfiniPot-V, NeurIPS 2025; both prior at the cutoff) and the baseline's own team's MadaKV are not compared; only prior-labelled work counts as required: VL-Cache, MEDA and InfiniPot-V qualify. FastV is a visual-token pruning method, not a KV-eviction scheme, and the same method behaves very differently on the two models (Table 1 at 10%: 0.5072; Table 2 at 10%: 0.3193), which needs an explanation. No baseline is given the sparse attention that PureKV uses, so Table 1–2 mix "compression policy" and "sparse prefill" effects.
- **Suggested Fix**: Add VL-Cache, MEDA, InfiniPot-V (and one score-free baseline such as StreamingLLM + ST-SpAttn) to Tables 1–2 under identical settings.

### W4: Theory is loosely used (§1, §3.3)
The introduction states that lower-layer scores "serve as a sufficient statistic" for higher-layer importance; §3.3 states that "our goal is to prove" Eq. 5, via Spearman correlation. A correlation of 0.2–0.4 ("exceeds 0.4" in most layers, "above 0.2" in the highest) is not sufficiency, and "statistically significant" for rank correlations over thousands of tokens says little about usefulness for top-h selection. The relevant quantity is the overlap/recall of the true top-h set.
- **Suggested Fix**: Report top-h overlap per layer, with random and recency baselines, and with and without ST-SpAttn; rephrase "prove" and "sufficient statistic".

## Literature-check addendum (strict mode, cutoff 2025-09-24)

**Per-claim novelty (`related_search.py novelty`)**

| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|---------------------------------------------|-----------|
| C1 cross-layer importance estimator | method | medium (script); I would say medium-to-incremental after reading InfiniPot-V | GemFilter, level 3, https://arxiv.org/abs/2409.17422v1, prior (arXiv-only), not cited | Uses early layers to select tokens for later layers; the value-norm ranking is in InfiniPot-V (https://arxiv.org/abs/2506.15745v2, prior peer-reviewed, not cited). The attention × V-norm combination for FlashAttention-compatible reuse across layers is a combination, not a new principle. |
| C2 ST-SpAttn | method | high (script) | Sparse-to-Dense, level 2, https://arxiv.org/abs/2505.19155v2, prior peer-reviewed, not cited | Shares topic (sparse attention for video LLMs), different mechanism (decoding-time speculative sparse/dense). No close prior work with the same fixed first-frame/current-frame/previous-frame pattern in 6 queries (arXiv only); fixed local patterns are, however, standard in sparse attention, so I rate "medium" in practice. |
| C3 result (5.0×/3.16×) | result | high (script) | MEDA, level 2, prior peer-reviewed, not cited | Numbers are not comparable across benchmarks. |

Script reading: no established claim; `paper_novelty` 0.689; attribution: GemFilter. No text-overlap flag (similarity: closest CAKE 0.205, LOOK-M 0.188, Sparse-to-Dense 0.185 cosine; all 8-gram overlaps 0). No criterion-7 candidate.

**Novelty delta table**

| Claimed contribution | Closest prior work | What that work already does | What is new here | Cited and differentiated? |
|---|---|---|---|---|
| C1 | GemFilter; FastV (cited as baseline) | Early layers select which tokens later layers process | Reuse as a ranking for per-layer KV eviction with value-norm weighting, FlashAttention-compatible | FastV cited as baseline only; GemFilter not cited |
| C1 (value norm) | InfiniPot-V | Value-norm ranking and temporal redundancy removal for video KV | Combination with cross-layer reuse | Not cited |
| C2 | Sparse-to-Dense; CASP (arXiv 2503.05936, prior arXiv-only) | Sparse attention for video-LLM decoding; attention sparsity for compressing multimodal models | Fixed spatial-temporal prefill mask tied to KV purification | Not cited |

**Baseline scout (MVBench, from the multimodal KV query):**

| Benchmark | Prior method (link, label) | Its reported number | Compared in the paper? | Paper's number | Note |
|---|---|---|---|---|---|
| MVBench | VL-Cache (Tu et al., 2024, in the paper's references) | not read | No | n/a | Cited, not compared |
| MVBench | MEDA (https://arxiv.org/abs/2502.17599v2, prior peer-reviewed) | abstract gives none for MVBench | No | n/a | Worth comparing |
| MVBench | InfiniPot-V (https://arxiv.org/abs/2506.15745v2, prior peer-reviewed) | abstract: long-video and streaming benchmarks | No | n/a | Not the same setting |

No under-reported baselines could be checked (settings differ). **Worth discussing only (recent preprints or concurrent, not required):** MadaKV (arXiv 2506.15724, cited by the paper as Li et al., 2025a), LightVLM (arXiv 2509.00419), StreamMem (arXiv 2508.15717), "Enhancing Large Multimodal Models with Adaptive Sparsity and KV Cache Compression" (arXiv 2507.20613).

**Field snapshot (as of the cutoff).** A few years ago, KV-cache reduction for LLMs meant H2O-style accumulated attention and StreamingLLM sinks; SnapKV and layer-wise budget allocation (CAKE, ICLR 2025; Ada-KV) then moved the focus to observation-window scoring and per-layer budgets. For multimodal models the current work targets video/streaming settings (LOOK-M, MEDA, InfiniPot-V, StreamMem), reports on long-video benchmarks, and treats kernel compatibility (FlashAttention-compatible, query-agnostic scoring: KVzip, KeyDiff) as a design constraint. Open problems: query-agnostic compression, hard memory caps for streaming video, and honest end-to-end latency. In this sub-field a result is significant when it shows a clear memory/latency gain on long video at near-lossless accuracy against the current VLM-specific baselines; modest gains on a short-clip benchmark are incremental. I used this to place Novelty and Significance in the 48–52 range.

## Missing References

| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Critical | Kim, Shim, Choi, Chang et al., "InfiniPot-V: Memory-Constrained KV Cache Compression for Streaming Video Understanding", NeurIPS 2025 (arXiv 2506.15745; verified via arXiv) | Training-free video KV compression with value-norm ranking and temporal redundancy: overlaps C1 and C2 |
| Critical | Wan et al., "MEDA: Dynamic KV Cache Allocation for Efficient Multimodal Long-Context Inference", NAACL 2025 (arXiv 2502.17599; verified) | Recent multimodal KV baseline from the same group as LOOK-M |
| Important | Shi, Ming, Nguyen, Liang et al., "Discovering the Gems in Early Layers: Accelerating Long-Context LLMs with 1000x Input Token Reduction" (arXiv 2409.17422; verified) | Early-layer attention as a token filter for later layers |
| Important | Zhang, Du, Yu, Wu et al., "Sparse-to-Dense: A Free Lunch for Lossless Acceleration of Video Understanding in LLMs", ACL 2025 (arXiv 2505.19155; verified) | Sparse attention in video LLMs at inference |
| Important | Jiang et al., "MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention" (arXiv 2407.02490; verified) | Prefill sparse attention and its interaction with long-context inference |
| Helpful | Zhang et al., "SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference" (arXiv 2410.04417; verified) | Training-free token sparsification for VLMs |
| Helpful | Work on value-aware token importance for KV eviction ("value matters too", 2024) [verify]; not found by title on arXiv, give as a line of work | The claim that previous work ignores V |

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Method plausible, validation thin |
| Clarity | 2 | Citation errors and naming inconsistencies |
| Significance | 2 | Short-clip evidence |
| Originality | 2 | Combination of known principles |

## Dimension Scores (0–100)

**Pool position:** better than about 40% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: incremental combination of known ideas with uncited close prior work, evaluated on one benchmark against a partial baseline set.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | "Sufficient statistic"/"prove" language not backed |
| Clarity & Presentation | 56 | Competent | Readable; citation problems |
| Novelty & Originality | 50 | Developing | Medium for C1, medium-high for C2 |
| Significance & Impact | 52 | Developing | Useful engineering if validated at scale |
| Experimental Validation | 46 | Developing | Baseline coverage gaps |
| Reproducibility | 45 | Developing | Missing settings |
| Ethical Compliance | 58 | Competent | Nothing at stake; no limitations |

## Questions for Authors
1. How does the value-norm ranking differ from InfiniPot-V's VaN ranking, and the cross-layer reuse from GemFilter/FastV? (A convincing delta plus comparison would raise Novelty.)
2. How does Eq. 2 (accumulated attention of the last w queries onto the prefix) differ from the observation-window scoring in SnapKV? (I could not confirm from the SnapKV abstract alone; please state it.)
3. Why were VL-Cache and MEDA not compared?
4. Why are the knowledge-tracing, federated-learning and avatar papers cited for the statements in §1–2?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No.

## Ethics Review Flag
**No**: (citation quality is reported to the editor as a factual concern).

## Overall Score
**3**: A useful but incremental engineering combination, with uncited close work and an incomplete baseline set.

## Confidence
**4**: Confident on the literature checked; I could not read all baselines' abstracts in detail.

---

# Peer Review Report

## Paper: PureKV: Plug-and-Play KV Cache Optimization with Spatial-Temporal Sparse Attention for Vision-Language Large Models
## Reviewer: Dr. Amara Nwosu-Lindgren, Reviewer 3 (Perspective) (computer-architecture / embedded systems group, North America; fictional persona)
## Expertise: GPU kernels and memory-bound inference; edge deployment; sparse patterns in hardware
## Date: 2026-11-10

---

## Summary
The paper treats KV-cache compression and fused/sparse attention as one design problem for video-language models. It proposes a cross-layer score reuse that avoids materializing attention in higher layers, and a fixed spatial-temporal sparse mask. The target applications are real-time multimodal deployments (Abstract, §1).

## Strengths

### S1: A systems-aware framing
Thinking about kernel compatibility rather than only about the eviction score is the right lens for deployment (§1, Fig. 1).

### S2: The fixed mask is hardware-friendly in principle
A static pattern (first frame, current frame, previous-frame same position) gives a predictable block structure that could map to block-sparse kernels without data-dependent indexing (§3.2, Fig. 2c). Table 3 shows a measured prefill gain.

### S3: Plug-and-play / training-free
No retraining, which matters for practitioners with fixed checkpoints. Table 6 and Table 5 (AVSD) hint at applicability beyond one pipeline.

## Weaknesses

### W1: The deployment regime the paper motivates is not tested
The abstract promises "scalable deployments for real-time multimodal applications", and §1 stresses "high-resolution" inputs. All experiments are on MVBench clips (§4.1) on one A100 40 GB; frame count, token count and batch size are not stated, and Table 3 reports only a single sequence length implicitly. For short clips the KV cache is small relative to the weights, consistent with decoding latency flattening (28.50 → 27.92 ms/token from 35% to 5% budget, Table 3). The memory-bound regime where KV compression pays off (hundreds of frames, concurrent requests) is not examined.
- **Suggested Fix**: Evaluate on long-video benchmarks and report latency/peak memory versus sequence length and batch size, ideally on an edge-class GPU too.

### W2: Fixed sparse mask assumptions are not stress-tested (assumption audit)
Assumptions behind ST-SpAttn: (i) tokens are spatially aligned between consecutive frames (§3.2: "its corresponding token in the previous frame"); (ii) the first frame is a good global anchor; (iii) frames have a fixed token grid. Camera motion, scene cuts, variable-resolution inputs (Qwen2.5-VL uses dynamic resolution, §2) and how text/question tokens attend are not discussed. The method-vs-model mapping for Qwen2.5-VL is not described. These assumptions could explain per-task swings in Table 7 (e.g., SC 0.4751 for ST vs 0.6219 for spatial-only; OE 0.7206 vs 0.3420).
- **Suggested Fix**: Show failure cases (scene cuts, motion) and an analysis of which tasks lose; describe how text tokens are handled and how the mask is built for Qwen2.5-VL.

### W3: Single shared ranking across layers and heads
Eq. 4 reuses one lower-layer ranking for all high layers, but attention patterns differ by layer and head (the paper itself uses GQA groups, Fig. 4). Per-layer heterogeneity is the reason methods like Ada-KV and CAKE allocate budgets per layer/head. Cross-layer sharing is justified only by correlations of 0.2–0.4 in upper layers (§3.3).
- **Suggested Fix**: Compare with per-layer own-score selection at equal budget on full tasks, and with a layer-wise budget allocation.

### W4: Cross-disciplinary connections to exploit
Cache-replacement policies and streaming-window methods from systems, and static block-sparse patterns from sparse-linear-algebra kernels, give natural baselines and kernel designs (e.g., kernels in the style of block-sparse attention libraries); a latency model in terms of memory traffic would explain why prefill gain is budget-independent in Table 3.
- **Suggested Fix**: Add a roofline-style analysis of where time goes.

### Minor
No limitations or broader-impact paragraph; hardware details limited to one GPU.

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Deployment claims untested |
| Clarity | 2 | Missing setup details |
| Significance | 2 | Potentially useful; unproven at scale |
| Originality | 2 | Engineering combination |

## Dimension Scores (0–100)

**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a practical, well-motivated direction with a measured prefill speed-up, but unvalidated in the regime that motivates it.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing | Assumptions unstated |
| Clarity & Presentation | 58 | Competent | Clear story |
| Novelty & Originality | 52 | Developing | Combination |
| Significance & Impact | 56 | Competent | Real problem; narrow evidence |
| Experimental Validation | 46 | Developing | Short clips only |
| Reproducibility | 48 | Developing | Missing hyperparameters |
| Ethical Compliance | 55 | Competent | Low stakes; no limitations text |

## Questions for Authors
1. What are the frames/tokens per video and the batch size in Table 3? (A long-video latency curve would raise my Significance score.)
2. Does ST-SpAttn use a block-sparse kernel, and what is the prefill time versus FlashAttention-2 on the same input?
3. How does the mask handle scene cuts and Qwen2.5-VL's dynamic resolution?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No.

## Ethics Review Flag
**No**.

## Overall Score
**3**: A promising systems-flavoured idea whose evidence stays outside the regime it targets.

## Confidence
**3**: Fairly confident; I did not audit the baselines' implementations.

---

# Peer Review Report

## Paper: PureKV: Plug-and-Play KV Cache Optimization with Spatial-Temporal Sparse Attention for Vision-Language Large Models
## Reviewer: Dr. Felix Haddad, Reviewer 4 (Generalist) (vision research group, mid-sized research university, Middle East; fictional persona)
## Expertise: video understanding, video-language benchmarks
## Date: 2026-11-10

---

## Summary
PureKV makes training-free KV-cache pruning for video-language models compatible with fast attention kernels by estimating high-layer token importance from a lower layer and by adding a structured sparse attention pattern in prefill. It reports 5× cache compression and a 3.16× prefill speed-up with accuracy close to the full cache on MVBench for two models.

## Strengths

### S1: A clear one-paragraph story
The two-part idea (reuse lower-layer scores; make the cache "cleaner" with sparse attention) is easy to state, and Fig. 1/Fig. 2 convey it (captions only; figures not available).

### S2: Consistent gains over baselines in the main tables
PureKV has the best average in all four settings of Tables 1–2. Recomputed: Qwen2.5-VL 20% 0.5429 vs best baseline FastV 0.5154 (+0.0275); VideoLLaMA2 20% 0.6189 vs StreamingLLM 0.5274 (+0.0915).

### S3: Breadth of supporting experiments
Appendix adds baselines + PureKV (Table 6), an audio-video setting (Table 5), and sparse-pattern variants (Table 7). Efforts beyond the main table are visible.

## Weaknesses

### W1: Venue-criteria checklist: evidence for the main claim is only partly met
Criteria turned into checks (ICLR: soundness, presentation, contribution; claims supported):
| Check | Status | Location |
|-------|--------|----------|
| Claims supported by evidence | Partly: "negligible quality degradation" fails on VideoLLaMA2 | Abstract, Table 2 |
| Evaluation beyond one benchmark | Not met (MVBench only; AVSD single numbers) | §4.1, Table 5 |
| Reproducibility details | Not met (w, h, frames, layers) | §3.1, §4 |
| Contribution clearly separated from prior work | Partly | §1–2 |
| Honest limitations | Not met (no limitations section) | §5 |
| Presentation | Partly (task/metric naming) | §4.1, Tables 1–2 |

### W2: Presentation inconsistencies hide what was actually measured
The metric is "ROUGE" in §4.1 but "accuracy" in App. 6.3; Table 2 has two columns named "AC"; §4.4 calls the ablation task "Action Sequence (AC)" while §4.1 defines AS as Action Sequence and AC as Action Count; tables have 10 columns while the text says 14 tasks. A reader cannot tell which tasks, metric and subset each number refers to.
- **Suggested Fix**: Unify names; one sentence per table saying the model, tasks, budget and metric.

### W3: Reported gains and several textual claims go beyond the tables
Table 5: PureKV 0.4265 vs SnapKV/StreamingLLM 0.4249 (+0.0016) is described as "significantly outperforms all other baselines", and the Full Cache (0.4795) is well above all methods; the dataset metric and the budget are not given. §4.4 says disabling ST-SpAttn "significantly decreases" performance, based on one task with differences of 0.018 (Qwen) and 0.057 (VideoLLaMA2).
- **Suggested Fix**: Replace "significantly" with measured differences and CIs; give budget and metric for Table 5.

### W4: Scope for ICLR
The contribution is a training-free engineering method with modest conceptual novelty, evaluated on a single short-video benchmark. ICLR accepts such papers when the evidence is broad (several long-video benchmarks, several models) and the claims are scoped; here it is closer to a workshop/system-venue result.
- **Suggested Fix**: Add Video-MME-style long-video benchmarks and a third model family; scope claims.

### Minor
Typos ("StreamingLLm", "Object Existenc", "criticals"); Fig. 5 is hard to read in extracted form (figure unavailable); the reference list has inconsistent formats ("Alexandre et al." for Mistral).

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evaluation thin |
| Clarity | 2 | Inconsistent naming |
| Significance | 2 | Narrow evidence |
| Originality | 2 | Incremental |

## Dimension Scores (0–100)

**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: single short-video benchmark, partial-baseline comparison, claims worded beyond the tables.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Mechanism partially tested |
| Clarity & Presentation | 52 | Developing | Naming and metric inconsistencies |
| Novelty & Originality | 50 | Developing | Incremental |
| Significance & Impact | 52 | Developing | Useful but narrow |
| Experimental Validation | 46 | Developing | One benchmark |
| Reproducibility | 44 | Developing | Missing details |
| Ethical Compliance | 56 | Competent | Low stakes, no limitations |

## Questions for Authors
1. Which tasks does each table cover and why? Can you report all 20 MVBench tasks? (This would raise my Clarity and Validation scores.)
2. What metric and budget are used for Table 5, and why is SnapKV equal to StreamingLLM?
3. Can you show one long-video benchmark?

## Limitations Assessment
**Have the authors adequately addressed limitations?** No.

## Ethics Review Flag
**No**.

## Overall Score
**3**: Clear and plausible, but the evidence is narrow and the wording outruns it; typical rejected-pool paper at ICLR.

## Confidence
**4**: Confident on presentation and venue fit; not a KV-cache specialist.

---

# Devil's Advocate Report

## Paper: PureKV: Plug-and-Play KV Cache Optimization with Spatial-Temporal Sparse Attention for Vision-Language Large Models
## Reviewer: Dr. Soledad Ibarra-Kim (industrial research lab, Latin America; fictional persona)

---

## Steelman
KV-cache eviction that needs per-layer attention scores blocks fused kernels. If lower-layer attention × value norm ranks tokens well enough, high layers can use fused/sparse kernels, saving memory and time. A video-structured sparse prefill pattern makes the cache easier to compress and speeds up prefill, and the numbers (Tables 1–3) support both at 20% and 10% budgets for two VLMs.

## Core Argument Chain
1. P1: Score-based eviction is incompatible with FlashAttention/sparse attention (§1, Fig. 1a).
2. P2: Lower-layer accumulated attention × V-norm approximates higher-layer importance (Eq. 4–5, Fig. 4: ρ mostly 0.2–0.4).
3. P3: Dense attention "gradually confuses" important and unimportant information in high layers (§3.2, Fig. 1c), harming importance estimation.
4. P4: A fixed spatial-temporal sparse mask "purifies" the cache, so compression improves (§3.2, Tables 4, 6, 7).
5. P5: Accuracy at 20% and 10% budgets is "negligibly" degraded and prefill is 3.16× faster (Abstract, Tables 1–3).
∴ PureKV is a plug-and-play framework that bridges KV compression and efficient attention.

## Strongest Counter-Argument
The paper's accuracy gains may come from two unrelated things that it never separates, and its "purification" story is untested. (1) The proposed method differs from every baseline in two ways at once: it uses a different eviction policy and it replaces dense attention with a restricted mask in the higher layers. The baselines are run with dense attention. Any change in accuracy therefore mixes eviction quality with the effect of restricting what tokens see. The control that would separate them, ST-SpAttn alone at a 100% cache against dense full cache, is absent. Table 6 does not rescue this: "+PureKV" rows leave it unclear what is added, and the resulting scores (0.4950–0.5680) remain far below PureKV alone (0.6189), so the benefit is not attributable to the sparse mask. (2) The "purification" mechanism (P3–P4) is never measured. Fig. 4 reports the cross-layer correlation without ST-SpAttn applied or removed, so there is no evidence that ST-SpAttn improves the estimation quality that the argument rests on. The only supporting ablation is one MVBench task (Table 4), with differences of 0.0179 (Qwen) that correspond to a handful of questions. (3) The evidence that compressed PureKV *exceeds* full cache on Qwen2.5-VL (0.5429 vs 0.5136; 0.5360 at 10%) is not a sign of purification but of an unstable evaluation: ROUGE on a multiple-choice benchmark, a full-cache score of 0.1674 on OS (Table 1), a LOOK-M baseline at 0.0610, and a result on OE for VideoLLaMA2 (0.7206 at 20%, above full cache 0.6600, then 0.3792 at 10%) that no other method approaches (best baseline 0.3779). A pipeline with that much variance cannot establish "negligible degradation", and where it can be checked (VideoLLaMA2) the degradation is −6.7% (20%) and −23.9% (10%) relative. The authors must show per-question paired results with CIs, ST-SpAttn alone, and ranking-quality evidence with and without ST-SpAttn to survive this challenge.

---

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim survives in a weaker form: for Qwen2.5-VL the results (Table 1) are consistent with near-lossless compression, and the fixes (scoping the claim, adding controls) do not require abandoning the method. I considered the Fig. 5 sweep against criterion 3: the paper never states that it selected the main-table configuration from it, the sweep covers one of ten reported tasks, and only the selection protocol is missing; per the decision table, "not stated after the protocol sweep" is MAJOR (DA-M1).

### MAJOR Issues

| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence (protocol) | §4.5, Fig. 5, Table 2/4 | Fig. 5 values coincide with the Action Sequence number in Table 2 (.7588) and Table 4; text: "When the CLIE layer index is 2, PureKV performs the best". The selection protocol for layer, w, h used in Tables 1–3 is not stated and MVBench has no dev split; the sweep is on a reported task. | State the protocol; select on unreported tasks; report the 9-task mean excluding the swept task |
| DA-M2 | Evidence (confound) | Tables 1–2, 4, 6 | Method differs from baselines in eviction policy and sparse prefill; no ST-SpAttn-only control | Add ST-SpAttn at 100% budget and baseline + ST-SpAttn |
| DA-M3 | Logic | §3.2, Fig. 1c, §3.3 | "Purification" is asserted, never measured; Fig. 4 has no with/without ST-SpAttn comparison | Report top-h overlap with and without ST-SpAttn |
| DA-M4 | Overclaiming (E5) | Abstract, §4.2, §4.3, App. 6.2 | "negligible quality degradation", "stable performance on both VLLMs", "significantly outperforms" contradicted or not supported by Tables 2 and 5 | Rewrite claims with numbers and CIs |
| DA-M5 | Evidence (metric) | §4.1, Tables 1–2 | ROUGE on a multiple-choice benchmark; sub-chance full-cache scores (OS 0.1674); LOOK-M ≈ 0.06; outlier OE 0.7206 | Accuracy with a fixed parser; fix/drop LOOK-M; per-question CIs |
| DA-M6 | Scope | §4, §1 | Motivation is long, high-resolution video; evidence is short MVBench clips | Add long-video benchmarks |
| DA-M7 | Integrity-adjacent (citation quality) | §1–2, References | Unrelated citations (knowledge tracing, avatars, federated learning, neuromorphic hardware) used as support; Linformer cited as "Linear Transformer" and Mongoose as "Reformer" | Audit; reported factually to the editor |

### MINOR Issues

| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | Table 2 header | "AC" appears twice |
| DA-m2 | Consistency | §4.3 | "Table 1 and 2, respectively" order reversed |
| DA-m3 | Questions | Table 5 | SnapKV and StreamingLLM both 0.4249 (suspected copy error) |
| DA-m4 | Terminology | §1, §3.3 | "sufficient statistic" and "prove" used for a correlation |

---

## Numerical Sanity Check

| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Prefill speed-up | 3.16× (Abstract) | 0.1190 / 0.0376 = 3.165 (Table 3, 20% budget) | Yes (single model, 20% budget) |
| Decoding speed-up at 20% | not stated | 36.73 / 28.32 = 1.30× | n/a |
| Table 2 PureKV 20% average | 0.6189 | Sum 6.1887 / 10 = 0.6189 | Yes |
| Table 1 PureKV 20% average | 0.5429 | Sum 5.4296 / 10 = 0.5430 | Yes (rounding) |
| Table 7 averages (Spatial, Temporal, Local, Atrous) | 0.5504, 0.5302, 0.4995, 0.3794 | 5.5045, 5.3024, 4.9953, 3.7941 /10 | Yes |
| "negligible quality degradation" on VideoLLaMA2 | n/a | 0.6635 → 0.6189 = −0.0446 (−6.7%); → 0.5047 = −0.1588 (−23.9%) | No (overstated) |
| AVSD "significantly outperforms all" | n/a | 0.4265 − 0.4249 = +0.0016; Full Cache 0.4795 | No |
| Table 2 20% mean without the OE column | n/a | (6.1887 − 0.7206)/9 = 0.6076 | Informational |

## Ignored Alternative Explanations
- Sparse prefill itself changes representations; accuracy changes could come from that, not from "purification".
- Evaluation noise at a few hundred questions per task (not stated; [verify]) and an unreliable ROUGE parser can generate differences of the observed size.
- Short clips: any ordering policy retains most information, so budget-insensitivity may reflect small caches rather than good selection.
- On Qwen2.5-VL, compressed > full may reflect that fewer tokens reduce distraction or a weak full-cache pipeline, independently of PureKV.

## Missing Stakeholder Perspectives
Practitioners serving many concurrent long videos (memory-bound regime) and edge-device users, the stated beneficiaries ("real-time multimodal applications"), are not represented in the evaluation.

## Observations (Non-Defects)
- Table averages are arithmetically consistent in every row I checked.
- The paper honestly shows that CLIE layer 0 collapses (Fig. 5 extracted numbers ~0.01), which is a useful, falsifiable observation.
- The tradeoff between prefill speed and budget is visible in Table 3 rather than hidden.

---

## Dimension Scores (0–100)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 42 | Mechanism untested; confound between policy and sparse prefill |
| Clarity & Presentation | 55 | Readable, but inconsistent metric/task naming |
| Novelty & Originality | 46 | Incremental, uncited close work |
| Significance & Impact | 44 | Narrow evidence |
| Experimental Validation | 34 | One short-video benchmark, odd metric, near-zero baseline |
| Reproducibility | 38 | Core hyperparameters missing |
| Ethical Compliance | 52 | No limitations; citation quality |

**Pool position:** better than about 30% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline claim is contradicted in part by the paper's own Table 2 and the central mechanism is untested.

## Overall: 2 | Confidence: 4

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | "No seeds / no variance" (draft) | Rewritten (W3) | Training-free, deterministic inference; the real concern is sampling noise at the task level, not training seeds |
| R1 | "No ablation of V weighting" (draft) | Dropped | Table 4 has the V ✘ row; narrowed to "one task only" (W4) |
| R2 | "Does not cite FastV" (draft) | Rewritten (W1) | FastV is cited and compared; the issue is the lack of discussion of the shared principle |
| R2 | Claim that SnapKV already has Eq. 2 (draft) | Moved to a question | Could not confirm from SnapKV's abstract; Hard Rule 1/2 |
| R3 | "No ethical statement" (draft) | Moved to Minor | Low-stakes paper |
| R3 | "No FlashAttention comparison" (draft) | Rewritten as a question | Table 3 does not state which kernel is used; unverified, not absent |
| R4 | Typos list | Moved to one Minor line | Cosmetic |
| DA | "Test-set selection (criterion 3)" (draft CRITICAL) | Rewritten as MAJOR DA-M1 | The paper does not state the main configuration came from Fig. 5; decision-table row "not stated" |
| DA | Table 5 identical values | Moved to Minor/Question | Low-confidence suspicion |

*Scores were not changed.* Identified integrity items: citation-quality concern (R2-W2, DA-M7); no reviewer-directed text (scan clean).

# Phase 2: Synthesizer Part A (package for the EIC)

### Merged issue list and classes

| Issue | Sources | Class |
|-------|---------|-------|
| "Negligible degradation"/stable-performance overclaim vs Table 2; Table 5 "significantly" | R1-W1, R4-W3, DA-M4 | CONSENSUS-3 (hinges) |
| Single short-video benchmark, no long video, deployment regime untested | R1-W6, R3-W1, R4-W4, DA-M6 | CONSENSUS-4 |
| Metric/task subset/baseline anomalies (ROUGE, sub-chance, LOOK-M, 10 vs 14 tasks) | R1-W2, R4-W2, DA-M5 | CONSENSUS-3 (hinges) |
| No ST-SpAttn-only control; one-task ablation; purification untested | R1-W4, DA-M2, DA-M3 | CONSENSUS-2 (hinges) |
| Unstated hyperparameters and selection protocol | R1-W5, DA-M1, R4-W1 | CONSENSUS-3 |
| Novelty incremental; uncited InfiniPot-V/GemFilter | R2-W1 | SOLO |
| Citation errors / unrelated citations | R2-W2, DA-M7 | CONSENSUS-2 |
| Correlation evidence overstated ("sufficient statistic", "prove") | R2-W4, DA-m4, R1-S4/W | CONSENSUS-2 |
| Single shared ranking across layers | R3-W3 | SOLO |
| Efficiency evidence thin (Table 3 only vs full cache) | R1-W6, R3-W1 | CONSENSUS-2 |
| DA-CRITICAL | none raised | n/a |
| SPLIT | none; R3 more positive on significance, R1/DA stricter on validation | n/a |

Warnings from the first script run are in `before.json`.

---

# Phase 2: EIC Meta-Review

**Editorial Decision (draft header filled after the script runs; see the full package below).**

## Editorial Decision

## Paper: PureKV: Plug-and-Play KV Cache Optimization with Spatial-Temporal Sparse Attention for Vision-Language Large Models
## Date: 2026-11-10
## Target Venue: ICLR (2026 cycle) | Paper Type: empirical
## Review Team (fictional personas): EIC Prof. Ingrid Valtonen; R1 Methodology Dr. Lukas Bernardsson; R2 Domain Prof. Yuna Takeda-Moreau; R3 Perspective Dr. Amara Nwosu-Lindgren; R4 Generalist Dr. Felix Haddad; DA Dr. Soledad Ibarra-Kim

### Decision: Borderline Reject (3), ICLR rating label from the script (see Score Summary)

**Official ratings** (shown to authors): R1 2, R2 3, R3 3, R4 3, DA 2 → mean 2.60 · official composite 48.1
**EIC assessment** (internal): weighted rating 2.56 → starting point 3 · weighted composite 47.8 → Reject band (cross-check, one band below) · **DA ceiling**: none · **Final (EIC)**: 3

### The Case For and Against
- **For acceptance:** A practical, training-free recipe addressing a real tension (score-based eviction vs fused kernels), with a measured 3.16× prefill speed-up on VideoLLaMA2, best averages in all four main-table settings (e.g., +0.0915 over the best baseline on VideoLLaMA2 at 20%) and consistent arithmetic across tables. On Qwen2.5-VL results are close to or above full cache.
- **Against acceptance:** The headline "negligible quality degradation" is contradicted on VideoLLaMA2 (−6.7% at 20%, −23.9% at 10%); the evaluation uses one short-video benchmark with an unclear metric, task subsets that differ by model, and a near-zero LOOK-M baseline; the "purification" mechanism and ST-SpAttn-alone control are missing; key hyperparameters, selection protocol and latency settings are unstated; close prior work (InfiniPot-V, GemFilter) is uncited, and several citations do not match their claims.

### Verification of Decisive Points (EIC read of the paper)

| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| "Negligible quality degradation" vs VideoLLaMA2 numbers | R1-W1, DA-M4, R4-W3 | Abstract, Table 2 | Verified | 0.6635 → 0.6189 (−6.7%) and 0.5047 (−23.9%); Qwen is fine |
| Prefill speed-up is budget-independent, i.e., from ST-SpAttn | R1-W1 | Table 3 | Verified | 0.0355–0.0376 ms/token for 5%–50% |
| "5.0×" is the nominal budget, memory not measured | R1-W1 | §4.2, Tables 1–3 | Verified | No peak-memory number in paper |
| ROUGE vs accuracy | R1-W2, R4-W2 | §4.1, App. 6.3 | Verified | "We use ROUGE…" vs "average accuracy of 0.6189" |
| Full cache OS 0.1674 / LOOK-M ≈ 0.06 | R1-W2, DA-M5 | Table 1 | Verified (numbers); "sub-chance" is Partly correct | Option count is not stated in the paper, so I treat chance level as likely but unverified |
| Table 4 is one task | R1-W4, DA-M3 | §4.4, Table 4 | Verified | "on the Action Sequence (AC) task" |
| Fig. 5 selection concerns | R1-W5, DA-M1 | §4.5, Fig. 5 | Partly correct | Number coincidence verified (.7588 in Fig. 5, Table 2, Table 4); that the main config was chosen from it is not stated. Figure unavailable. |
| Table 3 has no comparison method | R1-W6 | §4.2, Table 3 | Verified | |
| Table 5 "significantly outperforms" | R4-W3, R1 ERR-5, DA | App. 6.2, Table 5 | Verified | +0.0016 over SnapKV; below full cache by 0.053 |
| Citation errors (Linformer, Mongoose) | R2-W2 | §2, References | Verified | Entries are "Linformer" and "Mongoose" |
| Unrelated citations | R2-W2, DA-M7 | §1–2 | Verified | Knowledge tracing cited for sparse attention |
| InfiniPot-V / GemFilter uncited | R2-W1 | References | Verified | Neither is in the reference list; both are prior at the cutoff (abstracts read) |
| SnapKV already has Eq. 2 | R2 draft | Eq. 2 | Not asserted (kept as a question) | Cannot confirm from abstract |
| Table 5 SnapKV = StreamingLLM | R1, DA-m3 | Table 5 | Verified as a fact (0.4249 twice); cause unknown | Question only |
| Averages recomputed | R1-S3, DA | Tables 1, 2, 7 | Verified | All matched within rounding |

*Missing-comparison check against the ledger:* VL-Cache, MEDA and InfiniPot-V are labelled prior (cited or peer-reviewed), so their omission is a MAJOR issue at most. MadaKV, LightVLM, StreamMem are recent preprints/concurrent and are discuss-only. R2's novelty claims rest on abstracts I read. No text-overlap flag; no criterion-7 candidate.

### Reviewer Weights

| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | Error-log entries all verified at their locations; hedged the sub-chance claim and framed the selection issue as a question |
| R2 (Domain) | 3 | 4 | 1.0 | Citation errors and uncited work verified; novelty rested on abstracts; one weakness moved to a question |
| R3 (Perspective) | 3 | 3 | 1.0 | Sound, partly generic deployment points; no incorrect claims found |
| R4 (Generalist) | 3 | 4 | 1.0 | Presentation points verified; calibrated to ICLR |
| DA | 2 | 4 | 1.0 | Counter-argument and numerics verified; correctly declined to raise CRITICAL; "stable performance" and the SnapKV/StreamingLLM point are low-confidence |

### DA-CRITICAL Rulings

None raised (DA wrote "No CRITICAL issues found"). I confirmed this by applying the criteria independently: the evidence supports a weaker claim (not contradicted), the experiments can test the claim in principle, no leakage is stated (the Fig. 5 sweep is MAJOR under "not stated after the protocol sweep"), no fabrication signal, no ethical violation, and the method is understandable. DA ceiling: none.

### Final Decision and Justification
The EIC-weighted rating is 2.56, which rounds half up to 3 (a borderline-of-rounding value: within 0.1 of 2.5), and the 0–100 cross-check is one band lower (Reject). I keep the starting point 3 rather than depart: I cannot name a verified issue that the ratings left out, since the issues that would push down (the overclaim, the metric and baseline anomalies, the missing controls) are already reflected in R1's and the DA's 2s. I also do not move up: the strengths (practical idea, consistent arithmetic, real prefill gain) are those of a typical rejected-pool submission, not of a typical accepted ICLR paper. **My pool position: better than about 40% of ICLR submissions** (accepted share ≈ 27%). Deciding evidence: the paper's own Table 2 contradicts its headline claim, its evaluation is confined to one short-video benchmark with an unclear metric, and the central mechanism ("purification") has no direct test. The reviewers' pool positions (30–48) agree within 18 points, so no disagreement needs adjudicating. For a first paper that adds a method (not a new task), the bar is controlled evidence, which this version lacks. The decision does not exceed the DA ceiling (none). *Simulation, not a prediction.*

---

## Score Summary

*(The numbers below are reproduced from `aggregate.json`, which is the output of the script run with the EIC's weights and `--final 3`.)*

**Reviewer weights (EIC, internal)**

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| R1 (Meth.) | 4 | 0.85 | 1.25 | 25% |
| R2 (Domain) | 4 | 0.85 | 1.00 | 20% |
| R3 (Persp.) | 3 | 0.70 | 1.00 | 16% |
| R4 (Gen.) | 4 | 0.85 | 1.00 | 20% |
| DA | 4 | 0.85 | 1.00 | 20% |

**Official scores and EIC assessment**

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 44 | 52 | 54 | 50 | 42 | 48.4 | 48.0 | 12 |
| Clarity & Presentation | 52 | 56 | 58 | 52 | 55 | 54.6 | 54.4 | 6 |
| Novelty & Originality | 48 | 50 | 52 | 50 | 46 | 49.2 | 49.0 | 6 |
| Significance & Impact | 46 | 52 | 56 | 52 | 44 | 50.0 | 49.6 | 12 |
| Experimental Validation | 36 | 46 | 46 | 46 | 34 | 41.6 | 41.2 | 12 |
| Reproducibility | 38 | 45 | 48 | 44 | 38 | 42.6 | 42.2 | 10 |
| Ethical Compliance | 55 | 58 | 55 | 56 | 52 | 55.2 | 55.2 | 6 |
| **Composite** | 44.6 | 50.8 | 52.3 | 49.7 | 43.2 | **48.1 (before)** | **47.8 (after)** | |
| Pool position (P%) | 32 | 40 | 48 | 42 | 30 | | | |

Official mean rating 2.60 · EIC-weighted rating 2.56 (before weights: 2.59) → starting point 3 (Borderline Reject). Composite cross-check: official 48.1 → band 2; EIC-weighted 47.8 → band 2. ⚠ Cross-check: composite band 2 (Reject) differs from the rating-based starting point 3 (discussed in the Final Decision above). Decision ceiling: none (no DA-CRITICAL raised). No dimension spread exceeds 20 points.

### Target-Venue Scores (ICLR 2026, scale status: secondary; not official wording)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 1 / 2 / 2 |
| Rating (script label for final Overall 3) | "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})"; this is the script's internal-to-ICLR mapping for a Borderline Reject, to be verified against the current ICLR form |
| Final Overall (internal) | 3 (Borderline Reject) |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "PureKV: Plug-and-Play KV Cache Optimization with Spatial-Temporal Sparse Attention for Vision-Language Large Models" to ICLR. The topic, making KV-cache compression compatible with fused and sparse attention in video-language models, is practically important.

**Overall Assessment:**
The panel found the idea simple and well-motivated, with a real prefill speed-up and a clear main-table advantage over the baselines. It also found that the evidence is narrower than the claims: one short-video benchmark with an unclear metric, task subsets that change by model, a missing control for the sparse prefill, and several statements that go beyond the tables.

**Key Strengths Identified by Reviewers:**
1. A real and under-addressed problem, with a practical, training-free recipe (R1, R3, R4).
2. A measured 3.16× prefill speed-up on VideoLLaMA2 and best averages in all four main settings (R1, R4).
3. Table arithmetic is internally consistent, and the sparse-pattern variants in Table 7 are informative (R1, R2).

**Key Concerns Requiring Attention:**
1. "Negligible quality degradation" and "stable performance" are contradicted by Table 2 (−6.7% at 20%, −23.9% at 10% relative on VideoLLaMA2); App. 6.2's "significantly outperforms" rests on +0.0016 (CONSENSUS-3).
2. Evaluation scope and protocol: one short-video benchmark, "ROUGE" vs accuracy, 10 of 14 tasks per model with different subsets, near-zero LOOK-M baseline, no CIs (CONSENSUS-3/4).
3. Missing controls and measurements: ST-SpAttn alone at full cache, the "purification" mechanism, top-h overlap, measured peak memory and baseline latencies (CONSENSUS-2).
4. Unstated hyperparameters, layer and window sizes, and the selection protocol (CONSENSUS-3).
5. Positioning and citations: InfiniPot-V and GemFilter uncited; Linformer/Mongoose cited as Linear Transformer/Reformer; several unrelated citations (R2, DA).

**Decision: Borderline Reject (3).**
A careful panel would likely see this draft as below the bar for ICLR in its current form. It would be reconsidered if the claims were scoped to the evidence and the controls and long-video results below were added. Please see the Revision Roadmap.

Sincerely,
Prof. Ingrid Valtonen
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Evidence limited to short MVBench clips / long-video and deployment regime untested | R1, R3, R4, DA | CONSENSUS-4 |
| Overclaiming of "negligible degradation"/"significantly" | R1, R4, DA | CONSENSUS-3 |
| Metric/subset/baseline anomalies | R1, R4, DA | CONSENSUS-3 |
| Unstated hyperparameters and selection protocol | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Significance of the contribution | R3 (potentially useful, hardware-friendly) | R1, DA (evidence too narrow) | Significance depends on long-video validation that is absent; R3's own questions point to the same gap |
| Novelty level | R2 (incremental) | R4 (clear, plausible idea) | R2 verified with abstracts; uncited close work exists |

### Score Spread Discussion
No dimension is flagged ⚠ (largest spread 12 points, on Technical Rigor, Significance and Experimental Validation). The widest Experimental Validation gap is between R2/R3/R4 (46) and R1/DA (36/34), reflecting how heavily R1 and the DA weight the metric anomalies; I verified those anomalies, so I lean to the lower end.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Selection protocol / Fig. 5 coincidence | Yes (R1-W5) | n/a | n/a |
| DA-M2 | MAJOR | No ST-SpAttn-only control | Yes (R1-W4) | n/a | n/a |
| DA-M4 | MAJOR | Overclaiming | Yes (R1, R4) | n/a | n/a |
| DA-M5 | MAJOR | Metric/baseline anomalies | Yes (R1, R4) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*No DA-CRITICAL issue was upheld; these are the issues the EIC verified as undermining a main claim.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | Headline claims contradicted/overstated ("negligible", "stable", "significantly") | R1-W1, R4-W3, DA-M4 | Abstract, §4.2–4.3, App. 6.2, Tables 2, 5 | Scope to per-model, per-budget numbers; add CIs | Low | Yes |
| P1-2 | Metric, task subset and baseline validity | R1-W2, R4-W2, DA-M5 | §4.1, Tables 1–2 | Accuracy with a fixed parser on all 20 MVBench tasks; fix or drop LOOK-M; explain subsets | Medium, ~30–60 GPU-h | Partly |
| P1-3 | Missing controls for C2 and the "purification" mechanism | R1-W4, DA-M2, DA-M3 | §3.2, Table 4, Table 6, Fig. 4 | ST-SpAttn alone at 100% budget; full ablation on all tasks; top-h overlap with/without ST-SpAttn | Medium, ~20 GPU-h | Partly |
| P1-4 | Evidence in the motivating regime | R1-W6, R3-W1, R4-W4, DA-M6 | §4, Table 3 | Long-video benchmarks; measured peak memory and TTFT for all baselines with a described kernel | High, ~50–100 GPU-h | No |

### Priority 2: Strongly Suggested (Should Fix)

| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Hyperparameters and selection protocol (layers, w, h, frames, prompts); the Fig. 5 selection on a reported task | R1-W5, DA-M1 | State per-table configuration; select on unreported tasks; report the 9-task mean | Low | Yes |
| S2 | Missing prior-work comparisons and discussion: VL-Cache, MEDA, InfiniPot-V, GemFilter | R2-W1, R2-W3 | Add comparisons/discussion | Medium | Partly |
| S3 | Citation errors and unrelated citations | R2-W2, DA-M7 | Audit and replace | Low | Yes |
| S4 | "Sufficient statistic"/"prove" language; correlation evidence | R2-W4, DA-m4 | Rephrase; report top-h recall | Low | Yes |
| S5 | Single shared ranking across layers/heads | R3-W3 | Compare to per-layer own-score selection | Medium | Partly |

### Priority 3: Nice to Fix (Optional)

| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | ST-SpAttn assumptions (scene cuts, dynamic resolution, text tokens) | R3-W2 | Failure-case analysis; describe Qwen2.5-VL mapping |
| N2 | Table 5 duplicate values, missing metric/budget | R1, DA-m3 | Verify and state |
| N3 | Typos, Table 2 header, §4.3 table order, Alexandre/Sablayrolles name order | R1, R4, DA | Fix |
| N4 | Roofline-style latency analysis; cross-disciplinary kernel ideas | R3-W4 | Optional |
| N5 | Add a limitations section | All | Add |

## Estimated Revision Effort
- Priority 1: 4 items, about 2–3 weeks including long-video runs (100–200 GPU-hours)
- Priority 2: 5 items, about 1 week
- Priority 3: 5 items, about 2 days
- **Total estimated revision time**: roughly 4 weeks

*Gap Scout (post-review analysis) was not requested and was not run.*
