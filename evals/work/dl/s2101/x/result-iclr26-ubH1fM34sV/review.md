# Academic Paper Review: "Improving GUI Grounding with Explicit Position-to-Coordinate Mapping"

Date: 2026-11-10 · Mode: full · Target venue: ICLR (profile `iclr`, 2026 cycle) · Literature check: strict, cutoff 2025-09-24 · Submission ID: iclr26-ubH1fM34sV

*Simulation notice: this is a simulation of how a careful panel would likely see this draft, not a prediction of any outcome. The five reviewer passes were run one after another in one shared model context, not as independent agents; the EIC pass followed after all five reports were final. Figures were not available (text extraction only), so figure-dependent claims (Figures 1–4) are judged from captions and text.*

---

# Phase 0: Field Analysis and Reviewer Configuration

## Paper Analysis

| Item | Finding |
|------|---------|
| Title | Improving GUI Grounding with Explicit Position-to-Coordinate Mapping |
| Primary Discipline | Multimodal ML → GUI grounding / computer-use agents |
| Secondary Discipline(s) | Positional encodings for transformers (RoPE variants); VLM architecture |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Auxiliary "RULER" coordinate-reference tokens sharing position IDs with image patches; Interleaved MRoPE (I-MRoPE); LLaVA-NeXT (SigLIP-SO400M + Qwen2.5-7B, LoRA) and Qwen2.5-VL-7B fine-tuning on UGround |
| Target Venue | ICLR (stated by user); profile key `iclr`; ICLR-2026 form: Soundness / Presentation / Contribution, Rating, Confidence |
| Venue-Specific Notes | None (no contribution-type declaration). Rating scale status is `secondary`. |
| Paper Maturity | Submission-ready draft, short (8 pages + references + appendix) |
| Ethics-Relevant Content | None directly (public benchmarks, UGround web screenshots). Dual-use of GUI automation is not discussed. |

### Claimed Contributions (as stated by the authors, §1)
1. **C1 (problem):** "We identify and formalize the implicit mapping problem" in coordinate-as-text GUI grounding, "showing how it leads to poor accuracy and resolution brittleness".
2. **C2 (method):** RULER tokens, an explicit coordinate reference mechanism "that transforms unstable regression into robust spatial referencing".
3. **C3 (method):** I-MRoPE, a balanced positional embedding giving "equal spatial modeling capacity across dimensions".
4. **C4 (result, from the abstract/§1/§5):** consistent gains on ScreenSpot, ScreenSpot-V2, ScreenSpot-Pro, largest on high-resolution interfaces ("31.1% to 37.2%" on ScreenSpot-Pro through fine-tuning alone).
5. **C5 (efficiency):** RULER adds "less than 1%" to the token count even for 8K displays.

## Paper Memory (shared factual record; the reviewers read the redacted copy plus this)

- **Setup facts.** From-scratch: LLaVA-NeXT, SigLIP-SO400M-14@384, Qwen2.5-7B-Instruct, stage 1 = LLaVA-558K projector alignment, stage 2 = UGround finetuning with full projector + LoRA rank 16, 1 epoch (§4, App. A.1). Finetune: Qwen2.5-VL-7B-Instruct, all components trainable, 1 epoch on UGround, LR 1e-5, eff. batch 128 (App. A.2). RULER interval s = 8 default (§4). Training data: UGround, "approximately 8M element annotations across 775K screenshots", web only (§4). Eval: ScreenSpot, ScreenSpot-V2, ScreenSpot-Pro, element accuracy, evaluation code of GUI-Actor, greedy decoding (§4, App. A.3). Hardware: 8×H100 (App. A); GPU-hours not stated. Seeds / number of runs / variance: not stated after search. Test-time resolution settings: not stated beyond "same maximum sequence length as training" (App. A.3). Code release: not stated.
- **Headline numbers.** ScreenSpot-Pro 31.1 → 37.2 (§1; Table 1); fine-tune Table 1: 34.6 → 37.2; Table 2: 86.8 → 87.7; Table 3: 88.2 → 89.0; from-scratch: Table 1 29.4 (I-MRoPE) → 32.1 (+RULER), Table 2 83.0 → 83.3, Table 3 84.5 → 85.6; "<1%" token overhead (abstract/§1/§6) vs 2.8% worst case for mobile (§5.3).
- **Appendix adds.** Full hyperparameters for both settings (A.1, A.2), evaluation protocol (A.3). No extra experiments, no qualitative results, no failure analysis.
- **Unverifiable parts.** Figures 1–4 (no images; Fig. 3 bar values and Fig. 4 axis labels are garbled in extraction), bold/underline formatting in Tables 1–3, whether Eq. 2/3/6/8 are rendered exactly as in the PDF.

## Integrity Signals (EIC only)

`scripts/integrity_scan.py` ran on the paper text: **no reviewer-directed text or hidden characters found.** The reviewers read the redacted copy (identical to the text here). One factual note for the editor (not an injection, no score effect): §2 states the Qwen3-VL design was "confirmed through correspondence with the team members of Qwen3-VL", a private, unverifiable communication in a blinded submission.

## Literature Check (Phase 1.5, strict, cutoff 2025-09-24)

Run via `scripts/related_search.py` (arXiv API): 6 search queries logged (claim ×3, baseline ×1, expansion ×2; all with concept-only wording), 33 unique kept results (7 prior peer-reviewed, 8 prior arXiv-only, 9 recent preprints, 9 concurrent), `coverage`, `scout` (ScreenSpot-Pro), `similarity` and 3 `verify` runs. One gap left open: no prior work kept from 2021 (closed by verifying Pix2Seq separately). Similarity: no high-overlap (max cosine 0.17), no text-overlap flag; closest prior works are visual position-encoding papers (V2PE, PyPE), not GUI grounding papers. The arXiv-only search cannot see non-arXiv work.

## Review Team (fictional personas)

### EIC (meta-reviewer): Marguerite Okonkwo-Reyes, large public research university (Southern Europe)
- **Seniority / Expertise**: Senior faculty / multimodal LLMs, vision-language pretraining, area-chairing for ICLR-type venues
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Judges against the accepted pool; wants a verified, named issue before departing from the reviewers' ratings

### Reviewer 1 (Methodology): Kasimir Delacroix-Ahn, industrial research lab (Northern Europe)
- **Seniority / Expertise**: Senior industry scientist / VLM evaluation protocols, GUI/agent benchmarks, fine-tuning recipes
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every table average; insists on matched baselines and variance

### Reviewer 2 (Domain): Odalys Brennerman, vision-language group, large private research university (North America)
- **Seniority / Expertise**: Mid-career faculty / rotary positional embeddings for VLMs, GUI grounding models
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Checks novelty statements against the prior work's own abstract

### Reviewer 3 (Perspective): Ravindra Haldane-Osei, human–computer interaction and robotics institute (South Asia / Africa)
- **Seniority / Expertise**: Mid-career researcher / accessibility tooling, desktop/UI automation in practice, robot localization
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; asks what would make the idea travel

### Reviewer 4 (Generalist): Linnea Quispe-Tanaka, multimodal group, public research university (East Asia)
- **Seniority / Expertise**: Postdoc / general vision-language modeling, not GUI-specific
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Reads like a typical program-committee member; weighs weaknesses against ICLR's accepted papers

### Devil's Advocate: Bartholomew Nakagawa-Iyer, evaluation-methodology lab (Oceania)
- **Seniority / Expertise**: Senior faculty / causal evaluation, ablation design, benchmark validity
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, fair-minded; asks "what else explains the numbers?"

*Personas are fictional. Proceeding with the stated assumptions (paper type empirical, venue ICLR as stated).*

---

# Phase 1: Independent Reviews

*(Reports are shown in their final form after the Phase 1.6 report check; see that section for what changed.)*

---

# Peer Review Report: Reviewer 1 (Methodology)

## Paper: Improving GUI Grounding with Explicit Position-to-Coordinate Mapping
## Reviewer: Kasimir Delacroix-Ahn, Methodology (industrial research lab; fictional persona)
## Expertise: VLM evaluation protocols; GUI/agent benchmarks; fine-tuning recipes
## Date: 2026-11-10

## Summary
The paper argues that VLMs emit pixel coordinates as text without an explicit link between visual position and number, which hurts accuracy and resolution transfer. It adds "RULER" tokens (digit-valued reference tokens that share position IDs with image patches, placed at interval s) and proposes I-MRoPE (interleaving rotary frequency bands across axes). Evaluation is on ScreenSpot, -V2 and -Pro, with a LLaVA-NeXT + Qwen2.5-7B model trained on UGround (PE variants ± RULER) and a Qwen2.5-VL-7B fine-tune ± RULER.

## Protocol Sweep (full text incl. appendix)
- Training split: "Both experimental settings are trained on the UGround dataset" (§4); finetune "Training runs for 1 epoch on the UGround dataset" (App. A.2). No checkpoint selection (single epoch, final model) is stated.
- Reported split: ScreenSpot / -V2 / -Pro are evaluation-only benchmarks with no validation split; "We use the evaluation setting and the code provided by Wu et al. (2025a)" (§4).
- Selection statements: the only selection is the interval, "we adopt the setting of s = 8 as a good trade-off between performance and efficiency" (§5.2), after the sweep in Fig. 3 on the same benchmarks. It is described as a quality/cost trade-off, all intervals improve over no-RULER, and the sweep is flat ("does not yield significant or consistent improvements"), so the main comparison does not depend on s. No other tuning, no per-task selection found (searched: tuned, select, validation, best, checkpoint, per task).

## Omission sweep
Splits: present (§4). Seeds/runs/variance: **not stated after search**. Baseline settings: partly (§4 "reported from original papers or reproduced", row-level source marked only by † on some rows). Hyperparameters: present (App. A.1–A.2), their selection: not stated. Compute: hardware present, GPU-hours not stated. Failure cases: not present. Code/data availability: not stated. Evaluation resolution / max pixels: not stated after search.

## Claim-to-Evidence Map

| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | Implicit mapping causes poor accuracy and resolution brittleness; "formalize" | §1, contribution (1) | No diagnostic experiment, no formalization; baselines are never evaluated across resolutions | **Unsupported** (assertion, cites other papers) |
| C2 | RULER turns regression into reference-and-adjust ("copy then add a bounded number") | §1, §3.1 | Tables 1–3 show gains; no evidence the model copies/adds; no control for extra tokens; Fig. 3 flat in s | **Partially** (gains yes, mechanism untested) |
| C3 | I-MRoPE gives balanced spatial modeling and better grounding | §3.2, §5.1 | Table 1: 29.2 → 29.4; Table 2: 82.5 → 83.0; Table 3: 84.0 → 84.5; "lower training loss" has no numbers/curve in the text | **Partially** (≤0.5-point gains, single run) |
| C4 | Consistent gains, largest on high-res; 31.1% → 37.2% | Abstract, §1, §5.1 | Matched baseline in Table 1 is 34.6, so +2.6; from-scratch +2.7 (29.4 → 32.1); ScreenSpot +0.3/+0.9, V2 +1.1/+0.8; several columns decrease | **Partially** (gains real in direction; headline inflated; "consistent" overstated) |
| C5 | <1% token overhead | Abstract, §1, §5.3, §6 | §5.3: 0.2% at 8K with s = 2, but "2.8%" for mobile; token counts only, no latency | **Partially** |

## Strengths
### S1: Clean, small, plug-in intervention with a matched fine-tuning comparison
RULER is added to an otherwise unchanged Qwen2.5-VL recipe ("We do not change the original model's MRoPE", §4), so the fine-tune rows in Tables 1–3 isolate the token set from the architecture, assuming the "Qwen2.5-VL" row is trained under the same UGround recipe (see Question 1).
### S2: Controlled positional-embedding ablation in the from-scratch setting
Table 1–3 hold encoder, LLM, data and schedule fixed across LLaVA PE / MRoPE / I-MRoPE / +RULER, giving a four-step ladder rather than a single before/after.
### S3: Hyperparameters are largely specified and the sensitivity analysis is reported honestly
Appendix A.1–A.2 give LR, batch, epochs, LoRA rank, DeepSpeed stage; §5.2 reports that varying s is not significant and that s = 16 hurts mobile subtasks.
### S4: Honest scoping on SOTA
"RULER does not achieve state-of-the-art results" (§5.1); Table 1 caption flags non-comparable groups.

## Weaknesses

### W1: The central mechanism and the resolution-generalization claim are never tested
The paper's thesis (abstract, §1, §3.1) is that RULER fixes brittleness on unseen resolutions by enabling "reference-then-copy" plus resolution-independent bounded arithmetic. Evidence offered is the accuracy gain on ScreenSpot-Pro (Table 1). But ScreenSpot-Pro differs from the training data in domain as well as resolution ("greater domain shift", §4), so the gain cannot be attributed to resolution. There is no resolution sweep (the same test images rescaled), no comparison of x/y numeric error vs. wrong-element errors, no attention or probing evidence of copying, and no control that separates "explicit coordinate values at shared position IDs" from "extra tokens in the context" (e.g., RULER tokens with shuffled values or with unshared position IDs). Fig. 3 shows results roughly flat across s ∈ {4, 8, 16}; if bounded arithmetic with b = s × p mattered, a 4× change in b would be expected to show.
- **Suggested Fix**: (i) Inference-only resolution sweep on ScreenSpot-Pro/-V2 (e.g., 0.5×, 1×, 1.5×, 2× of the same screenshots, same model ± RULER, plus UGround-V1-7B and UI-TARS-7B): a few GPU-hours. (ii) Error decomposition (x/y digit error vs wrong element). (iii) Two control fine-tunes (shuffled-value RULER; unshared-position-ID RULER) at the A.2 recipe, ≈ 2 × the paper's fine-tune cost.

### W2: No variance estimate; most gains are within benchmark sampling noise
All results are single runs (not stated otherwise). With n = 1,581 (Pro) and n = 1,272 (ScreenSpot; "1,272 instructions", §4), the binomial standard error of an accuracy near 35% / 87% is about 1.2 / 0.9 points (derived), so the unpaired SE of a difference is ≈ 1.7 / 1.3. The I-MRoPE gain over MRoPE on Pro is +0.2 (29.2 → 29.4, Table 1) and +0.5 on ScreenSpot and V2; RULER gains are +0.3 (Table 2, from scratch) and +0.8 to +1.1 (Table 3, both settings). Several sub-columns fall (see Error Log). The Pro gains (+2.6, +2.7) are the only ones plausibly above noise, and even those are not tested. The text says "significant improvements" (§1) without a test.
- **Suggested Fix**: paired bootstrap over test items (free, uses existing per-sample outputs) and 3 seeds for the LLaVA-NeXT ladder (3 × 4 configs × 1 epoch on 8×H100; the authors know the cost, I estimate on the order of 100–200 GPU-hours total).

### W3: Headline gain is measured against the wrong baseline, and baseline provenance is unclear
§1 says "we improve accuracy from 31.1% to 37.2%". In Table 1, 31.1 is UGround-V1-7B, a different model; the matched Qwen2.5-VL fine-tune is 34.6 (+2.6). Whether the "Qwen2.5-VL" row is the off-the-shelf checkpoint or the same UGround fine-tune without RULER is not stated (App. A.2 says RULER is used "when specified", suggesting the latter). §4 states "All baseline numbers are reported from original papers or reproduced", but Tables 1–3 mark only some rows with † (and UGround-V1, UI-TARS-7B carry none), so the reader cannot tell which were reproduced and under what coordinate conversion (footnote 1). "Note that our models use less training data than GUI-Actor" (§4) is not quantified.
- **Suggested Fix**: state the baseline row's construction; report +2.6 as the headline; mark copied vs reproduced per row; give training-set sizes for GUI-Actor / UI-TARS / UGround vs this paper.

### W4: I-MRoPE is evaluated only in the weaker from-scratch setting, and its support is thin
The finetune setting keeps vanilla MRoPE (§4), so I-MRoPE is never shown to help a strong model. In the from-scratch setting a Qwen2.5 LLM pretrained with 1D RoPE is re-parameterized with MRoPE or I-MRoPE and adapted via LoRA rank 16 for one epoch, so the I-MRoPE vs MRoPE gap may reflect adaptation ease as much as spatial-modeling quality. "Achieves both lower training loss and stronger grounding performance" (§5.1) is asserted with no loss values or curve in the text (figures unavailable; I mark it unverifiable rather than wrong).
- **Suggested Fix**: show the training-loss curves; train Qwen2.5-VL with I-MRoPE swapped in from the start of a short continued pretraining if feasible, or reduce the claim to the LLaVA-NeXT setting.

### W5: Efficiency evidence is token counts only, with inconsistencies
§5.3 reports ratios of RULER to vision tokens (0.2% at 8K, s = 2; up to 2.8% for mobile) but no latency, FLOPs, or measured throughput; the abstract/intro say "less than 1%" without the mobile caveat. The text calls the setting "p = 8" while §3.1 defines p as patch size (SigLIP-14 here). How multi-digit RULER values map to tokens (a digit-wise tokenizer would multiply the count) is not described.
- **Suggested Fix**: report measured prefill latency on a stated GPU at 1080p/4K; define p and the tokenization of RULER values.

**Minor**: "Languge" typo (§2 heading); "1,272 instructions each on mobile, desktop, and web platforms" (§4) reads as per-platform counts (it is the total); Aguvis row has † on a single cell (Table 2).

### Error Log

| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Sev. | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|------|-----|
| ERR-1 | E1/E5 | §1 vs Table 1 | "we improve accuracy from 31.1% to 37.2%" | 31.1 is UGround-V1-7B; matched baseline is 34.6, so the fine-tuning gain is 37.2 − 34.6 = 2.6 | Cross-referenced (§1, Table 1 rows UGround-V1-7B and Qwen2.5-VL) | High | MAJOR | Report 34.6 → 37.2 |
| ERR-2 | E1/E6 | Tables 2–3 "Avg" for own rows | (numeric) | Own rows' Avg equals the unweighted mean of the six columns (e.g., Table 2 Qwen2.5-VL + RULER: (94.2+84.1+93.6+76.5+92.4+85.3)/6 = 87.68 → 87.7), whereas the baselines' Avg are sample-weighted: with ScreenSpot subset sizes 273/229/194/140/230/206 (sum 1,272, the paper's stated total) OS-Atlas-7B gives 82.48 (printed 82.5) and UI-TARS-7B 89.47 (printed 89.5); the same weighting gives 88.58 for the RULER row vs 87.7 printed (and 87.55 vs 86.8 for the base row) | Recomputed (subset sizes are from my knowledge of the benchmark, not in the paper; validated on two baseline rows) | Medium | MINOR (disfavors the authors by ≈0.8; affects cross-row ranking vs UI-TARS/GUI-Actor) | Use one averaging rule for all rows |
| ERR-3 | E6 | Eq. 8, §4 | "we use 2D MRoPE and I-MRO PE" | The 2D assignment is written with h and t (p_j = h if j mod 2 = 0, t otherwise) although the text says there is no temporal dimension; presumably w | Cross-referenced (Eq. 6 uses w/h/t; §4 text) | Medium | MINOR | Correct to w |
| ERR-4 | E7/E6 | §4 vs App. A.1 vs bibliography | "pretraining on the LLaVA-558K dataset (Liu et al., 2024a)" | Appendix cites the same dataset as (Liu et al., 2023); the bibliography's 2024a is "Visual anchors are strong information aggregators…" | Cross-referenced (3 locations) | Medium | MINOR | Fix citation |
| ERR-5 | E6 | §5.3 | "an efficiency analysis in the p = 8 setting" | §3.1 defines p as patch size (SigLIP-SO400M-**14** here) and s as interval (default 8); the paragraph then uses "an interval of s = 2" | Cross-referenced | Medium | MINOR | Define the setting |

## Questions for Authors
1. Is the "Qwen2.5-VL" row in Tables 1–3 the off-the-shelf checkpoint or the same UGround fine-tune without RULER? (Would raise my Experimental Validation score if the latter.)
2. Table 1 "Avg" for your rows matches the unweighted mean of six categories while baseline rows do not; which averaging was used for each? (A low-confidence observation from recomputation.)
3. A.2 states "counts ranging from 784 to 50,176" pixels (≈ 224² at the top). Is this the training/eval pixel budget? If so how are 4K Pro screenshots processed, and are predicted coordinates mapped back to the original frame?
4. What is the exact supervised target: the final number only, or reference + offset (Fig. 1 suggests "280 … +20")?
5. Per-sample outputs for a paired bootstrap on all three benchmarks?

## Limitations Assessment
**Partially.** §6 mentions future work but no limitations (no failure cases, no scope of resolutions, web-only training).

## Ethics Review Flag
**No**

## Scores
| Dimension | NeurIPS-style (1–4) | Rationale |
|-----------|---------------------|-----------|
| Quality | 2 | Mechanism untested, no variance |
| Clarity | 2 | Method details/target format under-specified |
| Significance | 2 | Small plug-in gains |
| Originality | 2 | RULER plausible; I-MRoPE concurrent/identical |

**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main claim (resolution generalization via explicit mapping) is not tested and gains are single-run and mostly ≤1 point; typical rejected-submission signals.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Sound idea, mechanism untested, E1/E5 issues |
| Clarity & Presentation | 60 | Competent | Readable, key details of RULER format missing |
| Novelty & Originality | 50 | Developing | See Reviewer 2 |
| Significance & Impact | 52 | Developing | +2.6 on Pro, ≤1 elsewhere |
| Experimental Validation | 46 | Developing | No variance, no resolution experiment, no control |
| Reproducibility | 62 | Competent | Good Appendix A; no code statement, no GPU-hours |
| Ethical Compliance | 62 | Competent | Nothing at stake; limitations thin |

## Overall Score
**3 (Borderline Reject)**: a sensible, cheap idea with directionally consistent gains, but the paper's thesis is not tested by its experiments and the headline is inflated; fixable but not in a rebuttal-only form.

## Confidence
**4**: checked tables and appendix; could not see figures.

---

# Peer Review Report: Reviewer 2 (Domain)

## Paper: Improving GUI Grounding with Explicit Position-to-Coordinate Mapping
## Reviewer: Odalys Brennerman, Domain (vision-language group, large private research university, North America; fictional persona)
## Expertise: rotary positional embeddings for VLMs; GUI grounding models
## Date: 2026-11-10

## Summary
The paper positions itself against two families: coordinate-as-text GUI models (SeeClick, UI-TARS, Jedi, GTA1/SE-GUI, Phi-Ground) and coordinate-free grounding (GUI-Actor), and against MRoPE-style positional encodings in Qwen2-VL/2.5-VL. It contributes RULER tokens (explicit digit-valued reference tokens at shared position IDs) to keep autoregressive coordinate output while giving a copy-able reference, plus I-MRoPE, an interleaved frequency allocation. Gains are reported on the three ScreenSpot benchmarks; the authors say the method does not reach state of the art.

## Strengths
### S1: A genuinely different remedy for text-coordinate grounding
RULER keeps the autoregressive output design ("keeping the model's original autoregressive generation design", §2) while adding a retrievable coordinate frame; this differs from label-smoothing (Phi-Ground), coordinate-free patch selection (GUI-Actor) and RL (GTA1, SE-GUI). In the literature search I found no prior work with this specific mechanism (shared-position-ID reference tokens carrying coordinate values).
### S2: Candid handling of concurrency
§2 states that Qwen3-VL "independently developed Interleaved-MRoPE" with "nearly identical designs through independent research paths". Concurrent work cannot count against the paper (the authors themselves call it concurrent, and the cited page is dated by the paper as accessed 01-10-2025, after the cutoff).
### S3: Relevant, well-motivated problem and right evaluation family
Resolution extrapolation on ScreenSpot-Pro is an open issue for text-coordinate GUI models; the paper picks the benchmark where it matters.
### S4: The theory of the RoPE imbalance is stated correctly
Eq. 4–7 describe standard RoPE and the sequential Θt/Θh/Θw allocation of MRoPE correctly, and Eq. 7 correctly shows reduction to 1D RoPE for text.

## Weaknesses

### W1: "A previously overlooked issue" and C3 are not positioned against earlier frequency-allocation work
§1 calls the MRoPE frequency imbalance "a previously overlooked issue", and C3 lists I-MRoPE as a contribution. Prior work on position-encoding design for multimodal RoPE exists: HoPE and Resonance RoPE are cited but described in one sentence each, and "VideoRoPE: What Makes for Good Video Rotary Position Embedding?" (Wei et al., 2025, arXiv; verified to exist, prior arXiv-only 6+ months before the cutoff) is not cited. I did not retrieve its abstract, so I cannot say how far it overlaps with C3; the authors should check and differentiate. Per-claim novelty (profile below): partial coverage by cited work (HoPE, Resonance RoPE), VideoRoPE unread (**medium**, pending). Separately the authors themselves say Qwen3-VL has a "nearly identical" design, so the contribution is a concurrent re-derivation, not a first; this is not a mark against the paper, but "previously overlooked" is too strong and the contribution should be framed as an independent confirmation.
- **Suggested Fix**: cite and differentiate VideoRoPE, HoPE and Resonance RoPE; replace "previously overlooked" with a scoped statement; state I-MRoPE's contribution as an analysis + GUI-grounding evaluation.

### W2: RULER's relation to explicit visual/coordinate referencing is not discussed or compared
The paper treats "explicit spatial guidance" as new, but there are close conceptual precedents: set-of-mark visual prompting (explicit index marks overlaid on the image so the model refers to marks instead of coordinates), quantized coordinate vocabularies in sequence-based detectors (Pix2Seq), and region/point tokens in referring models. None are discussed; there is no empirical comparison with a cheap alternative that gives the same information, e.g., a visible grid or tick-mark overlay on the screenshot, or digit-weighted label smoothing (Phi-Ground, cited) trained on the same UGround data. Without these, the claim that "explicit position-to-coordinate mapping" (rather than any extra spatial cue) is the useful ingredient is unsupported (also DA-M1, R1-W1).
- **Suggested Fix**: add a related-work paragraph and one same-data comparison with a visible-grid overlay baseline and with Phi-Ground-style label smoothing.

### W3: Resolution handling is a crowded sub-line of GUI grounding that is not engaged
ScreenSpot-Pro results in 2025 were driven mostly by RL fine-tuning, zoom/crop test-time methods and resolution-aware designs. Prior (peer-reviewed or old-enough arXiv) examples found in the search include a visual test-time-scaling method that reports "28+%" gains on ScreenSpot-Pro for UI-TARS and Qwen2.5-VL by region selection, and a CVPR 2025 GUI agent (SpiritSight; I did not read its abstract, so I do not describe its method) returned by the search on resolution generalization. The paper's +2.6 is small relative to these and complementary at best; its role (does RULER stack with RL or zoom?) is not tested, which limits significance (see baseline scout).
- **Suggested Fix**: discuss and, if feasible, show RULER composes with a zoom or RL-trained model.

### W4: Citation and description checks
In the three or four citations the argument leans on: UGround, UI-TARS, GUI-Actor, Qwen2.5-VL are described consistently with their abstracts (GUI-Actor: "Most existing work formulates this as a text-based coordinate generation task" matches §2). The dataset citation for LLaVA-558K is inconsistent between §4 and Appendix A.1 (ERR-4 in R1). "Video RoPE (Liu et al., 2025)" in §2 corresponds to the bibliography entry titled "Vrope: Rotary position embedding for video large language models"; the name used in the text differs from the cited title.
- **Suggested Fix**: correct names/citations.

**Minor**: related work on RoPE reads as a list; the one-paragraph GUI related work could state each baseline's coordinate format.

## Literature-Check Addendum (strict, cutoff 2025-09-24; arXiv search only)

**Per-claim novelty (claim-level profile; prior labels only set the verdict).**

| Claim | Dim. | Novelty | Top prior work (level, label, cited?) | Reasoning |
|-------|------|---------|----------------------------------------|-----------|
| C1 problem: implicit mapping → accuracy / resolution brittleness | problem | medium | GUI-Actor, arXiv 2506.03143 (level 3, recent preprint → discuss only; cited by the paper) | GUI-Actor already diagnoses the "mismatch" between dense screen coordinates and patch-level features for text coordinates; the paper adds a resolution angle but no new diagnostic |
| C2 RULER tokens | method | high (no close prior work found in 6 queries / 33 kept; arXiv only, so at most medium-high) | Closest by concept: Set-of-Mark prompting (level 2, prior, arXiv 2310.11441, not cited); Pix2Seq (level 2, prior, 2021) | Shared-position-ID reference tokens with coordinate values: not found |
| C3 I-MRoPE | method | medium (pending) | HoPE, Resonance RoPE (cited, partial coverage, level 2–3 from the paper's own one-line descriptions); VideoRoPE (prior arXiv-only; not cited; abstract not retrieved, unrated); Qwen3-VL (concurrent per authors, level 5 from the authors' own statement, **discuss only**) | Position-encoding design for multimodal RoPE is partly covered; a concurrent independent design exists |
| C4 results | result | n/a | — | Results claims, no prior coverage |
| C5 efficiency | result | n/a | — | — |

Script reading: no established claim from prior (peer-reviewed or old-arXiv) work; not a candidate for criterion 7. Closest prior works by similarity (pointers only, cosine ≤ 0.17): V2PE (arXiv 2412.09616), Pyramid-descent Visual Position Encoding (arXiv 2501.10967), BREEN (arXiv 2503.12446); none shares task and mechanism.

**Novelty delta table (closest prior works).**

| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|----------------------|------------------|---------------------------|
| RULER | Set-of-Mark prompting (Yang et al., 2023) | Explicit index marks on the image so the model refers to marks | Digit-valued tokens at shared position IDs, no image modification | Not cited |
| RULER | GUI-Actor (cited; recent preprint) | Coordinate-free patch-attention grounding | Keeps text output | Cited, one sentence (§2) |
| I-MRoPE | VideoRoPE (Wei et al., 2025) | RoPE design for video inputs (abstract not retrieved; overlap with C3 unverified) | Interleaved allocation, GUI use | Not cited |
| I-MRoPE | Qwen3-VL (concurrent) | Interleaved MRoPE | — | Cited, disclosed as concurrent/identical |

**Baseline scout (ScreenSpot-Pro; only prior rows can be "missing required baselines").**

| Benchmark / metric | Prior method (label) | Its reported number | Compared in the paper? | Note |
|--------------------|----------------------|---------------------|------------------------|------|
| ScreenSpot-Pro, accuracy | Visual Test-time Scaling for GUI Agent Grounding (prior, peer-reviewed, ICCV 2025 per metadata) | abstract: "28+%" gains on ScreenSpot-Pro for UI-TARS / Qwen2.5-VL (setting-specific; not a comparable absolute number) | No | Training-free, complementary; discuss, not required |
| ScreenSpot-Pro | Think Twice, Click Once (prior arXiv-only) | 13.3% (its own weaker backbone) | No | Different setting; no under-reported-baseline check applies |
| ScreenSpot-Pro | SE-GUI (cited), GUI-G1, GUI-G², Phi-Ground (cited), UI-AGILE (all recent preprint/concurrent) | e.g., SE-GUI abstract: 47.3% | No | Discuss only; **not** a weakness and no effect on scores |

No under-reported baseline found: the Table 1 numbers for UGround-V1-7B (31.1) and UI-TARS-7B (35.7) are consistent with how I know the original papers report them, but I did not retrieve those abstracts, so this is unverified rather than confirmed.

**Field snapshot (as of the cutoff).** Three to four years ago, GUI grounding relied on HTML/DOM or detector-based pipelines; the 2024–early 2025 paradigm was supervised fine-tuning of general VLMs on synthetic screenshot data with coordinates as text (SeeClick, OS-Atlas, UGround, UI-TARS). During 2025 the field shifted to (i) RL with verifiable rewards (kept results: SE-GUI reports 47.3% on ScreenSpot-Pro at 7B; GUI-G1, GUI-G², GTA1), (ii) coordinate-free or attention-based grounding (GUI-Actor), and (iii) zoom/crop test-time methods. Open problems named by recent work: high-resolution professional screens, small icons, cross-resolution robustness (ZonUI-3B, recent preprint, targets exactly this), and data scale. What counts as significant now: +2–3 points on ScreenSpot-Pro from a 7B plug-in alone is incremental; a method that stacks with RL/zoom pipelines or that explains and removes a failure mode with direct evidence (e.g., large gains under controlled resolution shift) would be significant. I used this to score Significance at the Developing/Competent boundary and Novelty at 52.

## Missing References
*(Citation-integrity rule: all items below were checked with `related_search.py verify` or found in the kept search results; none is marked [verify]. Links as returned by the script.)*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Important | Xilin Wei et al., "VideoRoPE: What Makes for Good Video Rotary Position Embedding?", 2025 (arXiv 2502.05173) | Prior study of RoPE design for multimodal/video inputs; the authors should check overlap with C3's "previously overlooked" framing (abstract not read by this reviewer) |
| Important | Jianwei Yang et al., "Set-of-Mark Prompting Unleashes Extraordinary Visual Grounding in GPT-4V", 2023 (arXiv 2310.11441) | Explicit visual marks as a referencing mechanism, the natural alternative to RULER |
| Important | Ting Chen, Saurabh Saxena, Lala Li, David J. Fleet, Geoffrey Hinton, "Pix2seq: A Language Modeling Framework for Object Detection", ICLR 2022 (arXiv 2109.10852) | Coordinates as a discrete token vocabulary in sequence models; precedent for the coordinate-as-text formulation |
| Important | "Visual Test-time Scaling for GUI Agent Grounding", ICCV 2025 per search metadata (arXiv 2505.00684; authors as listed on the link) | Training-free alternative that targets ScreenSpot-Pro resolution; complementary |
| Helpful | "SpiritSight Agent: Advanced GUI Agent with One Look", CVPR 2025 per search metadata (arXiv, March 2025) | GUI agent returned for the resolution-generalization query; for awareness (method not assessed) |
| Helpful | "ZonUI-3B: A Lightweight Vision-Language Model for Cross-Resolution GUI Grounding" (recent preprint, 2025-06) | Same problem (cross-resolution); discuss only |
| Helpful | "SparkUI-Parser" (concurrent, 2025-09) and "Structuring GUI Elements through Vision Language Models" (concurrent, 2025-08) | Both address text-coordinate weakness; discuss only |
| Helpful | "Advancing General Multimodal Capability of VLMs with Pyramid-descent Visual Position Encoding" (arXiv 2501.10967, 2025) | Closest by similarity score; visual position-encoding for VLMs |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence thinner than claims |
| Clarity | 3 | Readable |
| Significance | 2 | Incremental over a crowded 2025 field |
| Originality | 2 | RULER medium-high; I-MRoPE concurrent/partly covered |

## Dimension Scores (0–100)
**Pool position:** better than about 44% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: RULER is a fresh, cheap idea, but the contribution is shown only through small gains in one data regime, with the second half of the paper (I-MRoPE) concurrent and thinly supported.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 55 | Competent | Theory in §3.2 correct; mechanism not verified |
| Clarity & Presentation | 62 | Competent | Reads well; citation inconsistencies |
| Novelty & Originality | 52 | Competent (low) | RULER medium-high; C3 medium; C1 medium |
| Significance & Impact | 52 | Developing | See field snapshot |
| Experimental Validation | 50 | Developing | No comparison with alternative explicit-guidance baselines |
| Reproducibility | 60 | Competent | Appendix A helpful |
| Ethical Compliance | 62 | Competent | Nothing at stake |

## Questions for Authors
1. Does RULER stack with an RL-trained or zoom-based grounding pipeline? (A positive answer would raise Significance.)
2. How does a visible-grid overlay compare to RULER under the same data?
3. How do you differ from VideoRoPE's frequency allocation, beyond the axis assignment?

## Limitations Assessment
**Partially.** Concurrency disclosed; limitations of scope (web-only data, one scale) not discussed.

## Ethics Review Flag
**No**

## Overall Score
**3 (Borderline Reject)**: novel enough in RULER, but evidence and positioning are not at the ICLR accepted-paper level.

## Confidence
**4**

---

# Peer Review Report: Reviewer 3 (Perspective)

## Paper: Improving GUI Grounding with Explicit Position-to-Coordinate Mapping
## Reviewer: Ravindra Haldane-Osei, Perspective (HCI and robotics institute; fictional persona)
## Expertise: desktop/UI automation in practice; accessibility tooling; robot localization
## Date: 2026-11-10

## Summary
The paper asks why VLMs click in the wrong place on screens larger than those seen in training, and answers with a measurement-style fix: give the model a "ruler" of coordinate-valued tokens that share position IDs with the image, and let it read off and adjust. A second change rebalances rotary frequencies between height and width. Results on ScreenSpot-family benchmarks improve, most visibly on the high-resolution Pro set.

## Strengths
### S1: A transferable idea: explicit reference frames
Ruler tokens resemble landmark/anchor referencing in robot localization and piecewise-linear interpolation between calibration knots (knots at multiples of s × p, residual bounded by b). Framing the readout as "nearest knot plus bounded offset" (§3.1) is a nice way to make number prediction resolution-independent in principle.
### S2: Practical, low-overhead integration
RULER tokens are generated "during the preparation of multimodal inputs" (§3.1) and cost fractions of a percent (§5.3, Fig. 4 caption), so a deployment team could add them without architectural change.
### S3: Gains concentrate where practitioners hurt
The Pro benchmark (professional high-resolution desktop apps) shows the largest improvement: +2.6 for fine-tuning and +2.7 from scratch (Table 1), versus ≤1.1 on ScreenSpot/V2 (Tables 2–3), consistent with the claimed target.
### S4: I-MRoPE is a drop-in change for any MRoPE model
Eq. 6–7 keep text tokens identical to 1D RoPE, so existing LLM behavior is preserved.

## Weaknesses

### W1: Real-world resolution diversity is argued but not exercised
Deployed agents face DPI scaling, multi-monitor setups, window crops, 4K/8K canvases and anisotropic resizing. Evaluation covers three static benchmarks; no resolution sweep or scaling-factor test is run, and §5.1 states that the gain "reflect[s] how its reference-then-copy mechanism… help generalization to higher resolution grounding tasks" as if shown. (That explanation is plausible but untested; see R1-W1.)
- **Suggested Fix**: rescale ScreenSpot-Pro screenshots to several sizes (inference only) and report accuracy vs. scale for ±RULER.

### W2: Hidden assumptions about squareness and coordinate frames
The mapping is shared between height and width because "each image patch covers a square part of image" (§3.1) and coordinates are converted to raw pixels (§4). It is unstated how the vision processor's resizing (App. A.2 "dynamic resolution", pixel counts 784–50,176) interacts with this: if the model sees a resized image, the RULER values refer to the resized frame, and predictions must be mapped back to the original frame to score against bounding boxes. Anisotropic resize, letterboxing, and multi-image inputs ("a RULER token sequence before each image", §3.1) are untested.
- **Suggested Fix**: state the preprocessing/coordinate round-trip and test one anisotropic and one multi-image case.

### W3: Scale and scope of the transfer claim
The conclusion suggests "broader applications beyond GUI automation" (§6) after tests on two 7B backbones trained on one web-only dataset. Mobile subtasks are hurt by coarse s (§5.2).
- **Suggested Fix**: either narrow the sentence or add one non-GUI localization task (e.g., referring expression comprehension at varied resolution).

### W4: No broader-impact or safety discussion
GUI agents can automate transactions, bypass access controls (e.g., captcha-type tools) and capture screen content with private data. Even a one-paragraph note on intended use and safeguards is missing; §6 has no limitations on this.
- **Suggested Fix**: a short impact paragraph.

**Minor**: report latency on a real desktop GPU; show qualitative failure cases.

## Missing References
None required from this reviewer. (Cross-field method pointers: CoordConv-style explicit coordinate channels, learned lookup-table interpolation; no specific citations asserted.)

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound idea, modest evidence |
| Clarity | 3 | Understandable |
| Significance | 3 | Practical, low-cost |
| Originality | 3 | RULER fresh |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: an elegant, cheap, deployable idea with gains in the claimed direction on three benchmarks; evidence is modest, but ICLR accepts such papers when the idea is clean.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound construction; single runs |
| Clarity & Presentation | 68 | Competent | Clear story, Fig. 1 concept |
| Novelty & Originality | 64 | Competent | RULER is a new view of coordinate readout |
| Significance & Impact | 66 | Competent | Plug-in for agent stacks |
| Experimental Validation | 58 | Competent (low) | Consistent direction, thin controls |
| Reproducibility | 66 | Competent | Appendix details |
| Ethical Compliance | 66 | Competent | Little at stake; impact discussion absent |

## Questions for Authors
1. Does the approach hold when the model sees a rescaled screenshot (e.g., 125%/150% DPI)? A yes would raise my Significance score.
2. Does the benefit persist once a stronger baseline (RL-trained) is used?
3. What happens with non-square patches (anisotropic resizing)?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No**: no ethics review needed; a brief dual-use statement is advisable.

## Overall Score
**4 (Borderline Accept)**: I lean toward accept because the idea is clean, cheap and directionally validated, with real concerns about the strength of evidence.

## Confidence
**3**: not a GUI-grounding specialist; may have missed details.

---

# Peer Review Report: Reviewer 4 (Generalist)

## Paper: Improving GUI Grounding with Explicit Position-to-Coordinate Mapping
## Reviewer: Linnea Quispe-Tanaka, Generalist (multimodal group, public research university, East Asia; fictional persona)
## Expertise: general vision-language modeling
## Date: 2026-11-10

## Summary (contribution in one paragraph)
The paper contributes a simple architectural-input trick (RULER tokens) and a positional-embedding variant (I-MRoPE) for VLM-based GUI grounding, with improvements of about 1–3 points on three ScreenSpot-family benchmarks, the larger ones on the high-resolution ScreenSpot-Pro; the model remains below the strongest published 7B grounding models.

## Venue Fit and Criteria Checklist (ICLR: Soundness / Presentation / Contribution)

| Criterion (from the ICLR form) | Met? | Location / note |
|-------------------------------|------|-----------------|
| Claims supported by evidence (Soundness) | Partly | Directional gains in Tables 1–3; mechanism and resolution claims unsupported (§3.1, §5.1) |
| Experimental protocol described | Partly | App. A good; baseline construction and averaging unclear (§4, Tables 1–3) |
| Clarity of method (Presentation) | Partly | Eq. 1–3 clear in outline; supervised target format, tokenization of RULER values unclear (§3.1, Fig. 1) |
| Contribution significant for the ICLR audience | Partly | Positional encodings + agents are in scope; gains modest (Table 1: +2.6) |
| Related work positioned | Partly | Good GUI coverage; RoPE coverage listing-style (§2) |
| Limitations honestly discussed | Not met | §6 "Conclusions and Limitations" contains no limitations paragraph |

## Strengths
### S1: Clear, memorable idea communicated through two figures
Figures 1–2 (judged from captions) present the "ruler" metaphor and the architecture; §1 states the problem in a way a non-specialist follows.
### S2: Appropriate benchmark triple and honest about not being state of the art
The paper states "RULER does not achieve state-of-the-art results" (§5.1) and the Table 1 caption separates non-comparable groups.
### S3: Efficiency and sensitivity analyses included
§5.2 (interval sweep) and §5.3 (overhead) pre-empt two obvious reviewer questions; the admission that s = 16 hurts mobile is useful.
### S4: Appendix gives enough to attempt reproduction
Optimizers, batch sizes, sequence lengths, LoRA rank, evaluation decoding (App. A.1–A.3).

## Weaknesses

### W1: The paper's evidence for its two contributions is asymmetric and the headline overstates
I-MRoPE has gains of 0.2 (Pro), 0.5, 0.5 over MRoPE (Tables 1–3) and is not used in the strongest (finetune) setting; RULER has +2.6 on Pro but ≤1.1 elsewhere. The abstract and introduction promise "consistent gains" and "significant improvements" (§1) and quote 31.1% → 37.2%, which compares against UGround-V1-7B rather than the matched 34.6 baseline. A reader skimming the abstract would expect more than +2.6 on one benchmark.
- **Suggested Fix**: lead with 34.6 → 37.2; present I-MRoPE as a secondary, concurrent-with-Qwen3-VL contribution.

### W2: The method description leaves the training/inference format ambiguous
It is unclear whether the model is trained to emit the final number directly or "reference + offset" (Fig. 1 shows "280 … +20 … 300"), how multi-digit RULER values are tokenized, where in the prompt RULER tokens sit relative to the chat template ("We use Qwen2.5-VL's default system prompt and chat template", §4, but Eq. 1 places RULER after the system tokens), and what t0 means (Eq. 2 calls it "a fixed temporal index" and §3.1 then calls it "the initial spatial position ID of the image patches"). Eq. 8 writes the 2D assignment with t instead of w.
- **Suggested Fix**: add a worked example (token sequence with position IDs, and the target string) and correct Eq. 8.

### W3: No qualitative results, failure analysis or limitations
The paper contains no qualitative examples or failure cases, and §6's "Conclusions and Limitations" lists only future work. For a method whose claim is "reliable position-to-coordinate mapping", showing where it still fails (small icons, 4K) is essential to judge significance.
- **Suggested Fix**: add 6–8 random (not curated) failure/success examples and a limitations paragraph.

### W4: Baseline comparison framing
The best absolute baselines (UI-TARS-7B 35.7, GUI-Actor + Verifier 44.2 on Pro; UI-TARS 89.5/91.6 and GUI-Actor + Verifier 89.7/90.9 on ScreenSpot/V2) are above the proposed fine-tuned model on two of three benchmarks, and the argument that this is due to "limited training data and domains" (§5.1) is untested; a matched-data comparison with at least one of these methods would make the comparison fair. Also RL-based and zoom-based 2025 methods are discussed only in related work (recent preprints; worth discussing, not required).
- **Suggested Fix**: add one baseline trained on UGround alone with the A.2 recipe (UGround-V1 is already close) and discuss RL/zoom.

**Minor**: typo "Languge" (§2); "I-MRO PE" spacing; garbled table formatting in the text (extraction) not counted.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence thinner than claims |
| Clarity | 2 | Method format ambiguous |
| Significance | 2 | Modest |
| Originality | 3 | RULER fresh |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: median-to-slightly-above submission: a clear idea but with small gains and limited analysis; typical ICLR accepted papers have stronger evidence for their central claim.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 55 | Competent | |
| Clarity & Presentation | 58 | Competent | Ambiguity in method format |
| Novelty & Originality | 54 | Competent | |
| Significance & Impact | 54 | Developing | |
| Experimental Validation | 50 | Developing | |
| Reproducibility | 60 | Competent | |
| Ethical Compliance | 62 | Competent | |

## Questions for Authors
1. What exactly is the training target and the token layout (a worked example)? A clear answer would raise Clarity.
2. Can you show qualitative failure cases on ScreenSpot-Pro?
3. Would you restate the headline as 34.6 → 37.2?

## Limitations Assessment
**No.** §6 has no limitations content.

## Ethics Review Flag
**No**

## Overall Score
**3 (Borderline Reject)**: balanced but below the ICLR bar on evidence strength and clarity; revisions could change it.

## Confidence
**4**

---

# Devil's Advocate Report

## Paper: Improving GUI Grounding with Explicit Position-to-Coordinate Mapping
## Reviewer: Bartholomew Nakagawa-Iyer, evaluation-methodology lab (Oceania; fictional persona)

---

## Steelman
Text-coordinate VLMs must convert patch positions into digit tokens; adding coordinate-valued tokens that share position IDs with patches gives the transformer a retrievable ruler and reduces the readout to nearest-reference plus a bounded offset. Across a controlled ladder (LLaVA PE → MRoPE → I-MRoPE → +RULER) and a matched Qwen2.5-VL fine-tune, accuracy rises, most on the highest-resolution benchmark, at under 1% extra tokens.

## Core Argument Chain
1. P1: Coordinate-as-text grounding forces an implicit position→number mapping (§1, §3.1).
2. P2: The implicit mapping is learned per resolution and therefore fails on unseen resolutions (§3.1: "inherently resolution-specific", supported by citations only).
3. P3: RULER lets the model copy a reference value and add a bounded offset independent of resolution (§3.1; induction-head analogy).
4. P4: Therefore RULER improves accuracy, especially on higher-resolution inputs (Tables 1–3, ScreenSpot-Pro).
5. P5: I-MRoPE removes a frequency imbalance and further improves spatial accuracy (§3.2, Tables 1–3).
∴ "Explicit spatial guidance rather than implicit learning" yields more reliable GUI grounding across resolutions and platforms.

## Strongest Counter-Argument
The data show that adding RULER tokens correlates with higher accuracy; they do not show that the *explicit position-to-coordinate mechanism* is the reason, nor that *resolution* is the axis on which it helps. Three things could produce the same numbers. (a) Extra tokens with coordinate digits near the image could act as a generic spatial scaffold or attention sink for any model, with no copy-and-add behavior; no control (shuffled values, unshared position IDs, a visible grid overlay, or equal-length dummy tokens) is run. (b) The Pro gain (+2.6 fine-tuned, +2.7 from scratch) is confounded with domain shift: the paper itself says Pro has "greater domain shift" and high-resolution, desktop-only professional applications, whereas the other two benchmarks (web, mobile, desktop at ordinary sizes) improve by ≤1.1. A higher gain on a harder benchmark is not evidence about resolution; no experiment varies resolution while holding content fixed. (c) The interval sweep (Fig. 3, §5.2) is described as not changing results meaningfully ("does not yield significant or consistent improvements"); if the bounded offset b = s × p did the work, quadrupling b from s = 4 to s = 16 should matter. Meanwhile the "problem" itself (C1) is argued from citations, not measured: no baseline is evaluated across resolutions to show the claimed brittleness. Finally, every comparison is a single run on benchmarks whose sampling noise (≈ 1–1.2 points per accuracy) is comparable to most reported differences, so even the direction of the smaller effects (I-MRoPE: +0.2 on Pro) is uncertain. If the authors answer (a)–(c), the paper would stand; as it stands, the title's claim is an interpretation, not a finding.

---

## Issue List

### CRITICAL Issues
**No CRITICAL issues found.** The evidence supports a weaker version of the claim (RULER correlates with +2–3 points on Pro in two settings), so the issues below are MAJOR (fix: narrow claims or add controls), and the protocol sweep found no selection on the held-out benchmark that determines headline numbers (the only selection, s = 8, is a stated trade-off and the sweep is flat).

### MAJOR Issues

| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic / Evidence | §3.1; Fig. 3; §5.2 | Mechanism untested; no control for "extra tokens" vs "explicit mapping"; the flat response to s sits uneasily with the bounded-arithmetic story. Evidence supports a weaker claim ("RULER helps"), not the stated mechanism | Shuffled-value and unshared-position controls; visible-grid baseline; attention/probing or error decomposition |
| DA-M2 | Scope / Evidence | §4 ("greater domain shift"); Table 1 | Resolution-generalization claim confounded with domain shift; no resolution-controlled experiment; the "problem" (C1) is never measured | Resolution sweep with fixed content; evaluate baselines across resolutions |
| DA-M3 | Claim distortion (E5) | §1 "we improve accuracy from 31.1% to 37.2%"; abstract "consistent gains" | Headline uses UGround-V1-7B as baseline (31.1) instead of matched 34.6; "consistent" is contradicted by decreases (see check below); "significant" has no test | Restate as +2.6; report decreases; add significance test |
| DA-M4 | Novelty / Scope | §1 "overlooked issue that impacts grounding precision"; §2 "nearly identical designs through independent research paths" | I-MRoPE is a concurrent near-duplicate of Qwen3-VL's design, has ≤0.5-point gains, and is not evaluated in the fine-tuned setting; "previously overlooked" is too strong given prior multimodal-RoPE design work (HoPE and Resonance RoPE are cited; VideoRoPE is not) | Reframe as concurrent confirmation; cite and differentiate VideoRoPE |
| DA-M5 | Statistics | Tables 1–3 | Single runs; no CIs; many deltas within 1 SE (derived) | Paired bootstrap; 3 seeds on the ladder |
| DA-M6 | Overgeneralization | Abstract: "our approach enables more reliable GUI automation across diverse"; §6 "broader applications beyond GUI" | No end-to-end agent task, web-only training, two 7B backbones; "platforms" generalization is only via ScreenSpot subsets | Narrow wording or add an agent benchmark |

### MINOR Issues

| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Numbers | Tables 2–3 Avg | Own rows use unweighted mean, baselines sample-weighted (R1 ERR-2); disfavors authors by ≈ 0.8 |
| DA-m2 | Consistency | Eq. 8; §5.3 "p = 8"; §4 vs App. A.1 citation | Notation/citation inconsistencies |
| DA-m3 | Efficiency | Abstract/§1/§6 "<1%" vs §5.3 "2.8%" | Overhead claim omits mobile worst case; no latency |
| DA-m4 | Integrity/anonymity (for the editor) | §2 "confirmed through correspondence with the team members" | Private, unverifiable communication in a blinded submission; no score effect |
| DA-m5 | Reproducibility | App. A.2 "counts ranging from 784 to 50,176" | Pixel budget implausibly small for 4K images unless units differ; eval resolution not stated |

## Numerical Sanity Check

| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Fine-tune gain on Pro (§1) | 31.1 → 37.2 (+6.1) | Matched baseline 34.6 → 37.2 = +2.6 | **No** (baseline differs) |
| Table 1 Avg, Qwen2.5-VL + RULER | 37.2 | (34.2+36.5+21.1+43.9+55.4+32.0)/6 = 37.18 | Yes (unweighted mean) |
| Table 1 Avg, GUI-Actor-7B + Verifier | 44.2 | (38.8+40.5+37.2+44.5+64.8+43.9)/6 = 44.95 | No (baseline Avg is not the unweighted mean; own rows are) |
| RULER gain from scratch on Pro | 29.4 → 32.1 | +2.7 | Yes |
| I-MRoPE gain on Pro | 29.2 → 29.4 | +0.2 | Yes (tiny) |
| Table 2 Avg, Qwen2.5-VL + RULER | 87.7 | unweighted 87.68; sample-weighted (273/229/194/140/230/206) 88.58 | Matches unweighted only |
| Table 2 Avg, OS-Atlas-7B / UI-TARS-7B | 82.5 / 89.5 | weighted 82.48 / 89.47 | Yes (weighted) |
| "Consistent" RULER improvement, Table 2 (from scratch) | 83.0 → 83.3 | D-Icon 73.4 → 73.2; W-Icon 77.7 → 77.2 | Decreases in 2 of 6 columns |
| RULER vs I-MRoPE, Table 3 (from scratch) | 84.5 → 85.6 | D-Text 91.3 → 90.3 | Decrease in 1 of 6 columns |
| Fine-tune, Table 2 | 86.8 → 87.7 | D-Text 94.6 → 93.6 | Decrease in 1 column |
| Pro SE at 35%, n = 1,581 | — | √(.35×.65/1581) = 1.2 pts | derived |
| ScreenSpot SE at 87%, n = 1,272 | — | √(.87×.13/1272) = 0.94 pts | derived |

## Ignored Alternative Explanations
- Extra context tokens as a generic spatial scaffold or attention-sink effect.
- Domain/content differences of ScreenSpot-Pro rather than resolution.
- Better adaptation of a LoRA-tuned LLM to I-MRoPE vs MRoPE (re-parameterization).
- Benchmark sampling noise; per-subset decreases suggest some gains are within noise.
- A simple visible-grid overlay or digit-weighted loss (Phi-Ground) achieving similar gains.

## Missing Stakeholder Perspectives
Users with high-DPI/multi-monitor setups, accessibility tool developers, platform owners worried about automated interaction at scale; no discussion of misuse (automation of access-controlled interfaces).

## Observations (Non-Defects)
- The fine-tune comparison is a minimal diff on a strong baseline, which is a robust design when the baseline row is matched.
- The sensitivity analysis and the "does not achieve state-of-the-art" statement are honest.
- Eq. 7 is a correct, useful reduction showing text behavior is preserved.
- The efficiency argument (bounded token overhead) is logically sound at the token level.

## Dimension Scores (0–100)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 44 | Mechanism untested, E1/E5 issues |
| Clarity & Presentation | 56 | Ambiguities in target format/notation |
| Novelty & Originality | 46 | I-MRoPE concurrent; RULER untested vs alternatives |
| Significance & Impact | 46 | Modest, below strongest baselines |
| Experimental Validation | 40 | No controls, no variance, no resolution experiment |
| Reproducibility | 55 | Appendix good, protocol gaps |
| Ethical Compliance | 60 | Nothing at stake |

**Pool position:** better than about 36% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: central claim untested and gains within noise for most columns.

## Overall: 2 | Confidence: 4

---

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | "Hyperparameters, batch size and LR not given" (draft) | Dropped | Appendix A.1–A.2 give them; replaced by "selection of hyperparameters not stated" in the omission sweep |
| R2 | "VRoPE not cited" (draft) | Dropped / rewritten | The paper cites Liu et al. 2025 (VRoPE); rewritten as a naming mismatch under W4 |
| R4 | "RL methods (GTA1, SE-GUI) are missing baselines" (draft) | Rewritten | Cited in §2; recent preprints → "worth discussing", not required (W4 text) |
| R3 | "No limitations discussed" (draft) | Rewritten | §6 is titled "Conclusions and Limitations" but contains no limitations; stated precisely in W4/Limitations |
| DA | "Qwen3-VL not cited" (draft) | Dropped | Cited as (Qwen, 2025) in §2 |
| R1 | Efficiency (W5) | Kept, ordered last | Not a main claim; MINOR-level severity |
| All | Typos ("Languge"), spacing | Moved to Minor lines | Cosmetic |

Scores unchanged.

---

# Phase 2: Editorial Decision

# Editorial Decision

## Paper: Improving GUI Grounding with Explicit Position-to-Coordinate Mapping
## Submission ID: iclr26-ubH1fM34sV
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC (meta-reviewer) Marguerite Okonkwo-Reyes; R1 Methodology Kasimir Delacroix-Ahn, R2 Domain Odalys Brennerman, R3 Perspective Ravindra Haldane-Osei, R4 Generalist Linnea Quispe-Tanaka, DA Bartholomew Nakagawa-Iyer

---

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00 · official composite 54.9
**EIC assessment** (internal): weighted rating 2.92 → starting point 3 · weighted composite 54.2 → band 3 (cross-check, agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**ICLR rating (secondary scale, `{0,2,4,6,8,10}`)**: 4 (earlier-cycle scale: 5) · Soundness 2 / Presentation 2 / Contribution 2

---

## EIC Meta-Review

### Synthesizer package (Part A): merged issues and classes

| Merged issue | Sources | Class |
|--------------|---------|-------|
| Mechanism / resolution-generalization claim untested; no controls | R1-W1, R2-W2, R3-W1, DA-M1, DA-M2 | CONSENSUS-4 |
| Single runs, gains within noise | R1-W2, DA-M5 | CONSENSUS-2 |
| Headline 31.1 → 37.2 vs matched 34.6; "consistent" overstated | R1-W3/ERR-1, R4-W1, DA-M3 | CONSENSUS-3 |
| I-MRoPE: concurrent/identical to Qwen3-VL, tiny gains, "overlooked" overclaim | R1-W4, R2-W1, R4-W1, DA-M4 | CONSENSUS-3 |
| Method format/notation ambiguities | R4-W2, R3-W2, R1-ERR-3/5 | CONSENSUS-3 |
| Baseline coverage / matched-data comparison | R2-W3, R4-W4, R1-W3 | CONSENSUS-3 |
| No limitations/qualitative/failure cases | R4-W3, R3-W4, R1 Limitations | CONSENSUS-3 |
| Resolution-diversity (DPI, anisotropy) | R3-W1/W2 | SOLO |
| Avg protocol (unweighted vs weighted) | R1-ERR-2, DA-m1 | CONSENSUS-2 |
| Efficiency evidence tokens-only | R1-W5, DA-m3 | CONSENSUS-2 |
| Positive-vs-negative reading of "gains are consistent" | R3 (positive) vs DA (negative) | SPLIT |
| DA-CRITICAL | none | — |

Hinge points: mechanism/resolution claim; I-MRoPE novelty/support; headline accuracy.

### The Case For and Against
- **For acceptance:** RULER is a clean, cheap, plug-in idea with a matched fine-tune comparison; gains are in the right direction on three benchmarks, largest on the high-resolution Pro (+2.6/+2.7), the authors are candid about not reaching SOTA and about concurrent work, and the appendix is reasonably complete.
- **Against acceptance:** The thesis (explicit mapping fixes resolution brittleness) is not tested by any resolution-controlled experiment or mechanism control, the headline gain is measured against the wrong baseline, most deltas are single-run and within benchmark noise, I-MRoPE is a concurrent near-duplicate with ≤0.5-point gains, and the fine-tuned model trails UI-TARS on two of three benchmarks.

### Verification of Decisive Points (EIC read of the paper)

| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Headline 31.1 → 37.2 uses UGround-V1-7B as baseline; matched baseline is 34.6 (+2.6) | R1-ERR-1, R4-W1, DA-M3 | §1; Table 1 | **Verified** | "we improve accuracy from 31.1% to 37.2%"; 31.1 is the UGround-V1-7B row |
| No resolution-controlled experiment; Pro confounded with domain shift | R1-W1, DA-M2, R3-W1 | §4; Table 1; §5.1 | **Verified** | §4: Pro has "greater domain shift"; no resolution sweep anywhere |
| No mechanism control / evidence of copy-and-add | R1-W1, DA-M1, R2-W2 | §3.1; Fig. 3; §5.2 | **Verified** | None in main text or appendix; Fig. 3 values are flat per §5.2 text (figure not viewable) |
| I-MRoPE gains tiny (0.2/0.5/0.5) | R1-W4, DA-M4 | Tables 1–3 | **Verified** | 29.2→29.4; 82.5→83.0; 84.0→84.5 |
| I-MRoPE concurrent near-identical to Qwen3-VL | R2-W1, DA-M4 | §2 | **Verified** | Authors' own statement; concurrent → no score effect |
| "Consistent gains" contradicted by decreases | DA-M3 | Tables 2–3 | **Verified** | e.g., D-Icon 73.4→73.2; W-Icon 77.7→77.2 (T2); D-Text 91.3→90.3 (T3) |
| Own-row Avg is unweighted, baselines weighted | R1-ERR-2, DA-m1 | Tables 2–3 | **Partly correct** | Recomputation holds (own rows = unweighted means; OS-Atlas/UI-TARS reproduce under weighted sizes), but subset sizes are not in the paper; effect small and against the authors |
| §5.3 "p = 8" vs patch size 14 / s = 8 | R1-ERR-5 | §5.3, §3.1, §4 | **Verified** | Terminology inconsistent; effect unclear |
| A.2 pixel range "784 to 50,176" implausibly small | R1 Q3, DA-m5 | App. A.2 | **Partly correct** | Text is as quoted; whether it is an error or a unit convention cannot be determined |
| LLaVA-558K citation mismatch | R1-ERR-4, R2-W4 | §4 vs App. A.1 | **Verified** | (2024a) vs (2023) |
| "<1%" vs 2.8% mobile | R1-W5, DA-m3 | §5.3 vs Abstract | **Partly correct** | The <1% statement is for 8K/desktop; mobile worst-case 2.8% is disclosed in §5.3 |
| R3: "gains reflect resolution generalization" | R3-W1/S3 | §5.1 | **Overstated** | The text itself asserts it; untested |
| Literature: missing comparisons on RL/zoom 2025 methods | R2-W3, R4-W4 | §2, Table 1 | **Overstated as weakness** | Recent preprints/concurrent: "worth discussing" only; only RegionFocus (prior) is a prior item and is training-free/complementary |

Literature-ledger check: no weakness depends on a recent/concurrent/newer item; every recommended reference is verified (links in R2's addendum). The Qwen3-VL overlap is concurrent and does not lower any score. No criterion-7 candidate exists (no verified prior work with the same task and mechanism).

### Reviewer Weights

| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 3 | 4 | **1.25** | Central points (ERR-1, W1, W2) all verified; recomputations hold; well calibrated for ICLR |
| R2 (Domain) | 3 | 4 | 1.0 | Mostly verified; novelty/positioning sound, litigated recent items correctly as discuss-only |
| R3 (Perspective) | 4 | 3 | **0.75** | Pool position (66) and Overall 4 are lenient for the evidence; accepts the resolution-generalization story as shown (Overstated); rest of its points are sound |
| R4 (Generalist) | 3 | 4 | 1.0 | Verified; typical program-committee calibration |
| DA | 2 | 4 | 1.0 | Counter-argument survived my check on all of its main points; Overall 2 is a little harsh against the verified evidence (no fatal flaw), which role-wise is expected |

### DA-CRITICAL Rulings

| Issue | AC test | Ruling | Resolvable by |
|-------|---------|--------|---------------|
| none raised | n/a | n/a ("No CRITICAL issues found"; DA-M1…M6 are MAJOR) | n/a |

Selection check: the protocol sweep (searched for test set, validation, selected, tuned, best, checkpoint) shows no held-out-test selection behind the headline numbers; s = 8 is chosen as a stated trade-off (§5.2), the headline Table 1–3 numbers use s = 8 for all rows and the sweep (Fig. 3, per text) is flat.

### Final Decision and Justification

The EIC-weighted rating is 2.92, so the starting point is 3 (Borderline Reject); the composite cross-check (54.2, band 3) agrees, so no departure is warranted. I place the paper at about the 47th percentile of ICLR submissions: the idea is fresh and cleanly integrated, which keeps it from the lower band, but the verified issues (untested central mechanism and resolution claim; inflated headline; single-run, mostly sub-1-point gains; concurrent I-MRoPE with ≤0.5-point gains) are the ones that typically separate rejected from accepted submissions at this venue, and the weaknesses are not the "ordinary" kind (missing seeds alone) that accepted papers carry, because they touch the thesis itself. This is a Borderline Reject rather than Reject because none of the issues is fatal: a resolution sweep, two control fine-tunes and variance estimates could plausibly turn the paper into an accept-level contribution, and the revision can be done on the existing recipe. The decision (3) does not exceed the DA ceiling (none).

### Editorial Decision Letter

Dear Authors,

Thank you for submitting "Improving GUI Grounding with Explicit Position-to-Coordinate Mapping" to ICLR.

**Overall Assessment:** The panel found RULER a clean and inexpensive idea that gives text-coordinate VLMs an explicit coordinate reference, with gains that point in the intended direction on three ScreenSpot benchmarks, and appreciated the candor about not reaching state of the art and about the concurrent Qwen3-VL design. The concerns concern how well the evidence supports the paper's stated explanation and headline.

**Key Strengths Identified by Reviewers:**
1. A new, plug-in mechanism with minimal token overhead and a matched fine-tuning comparison (R1, R2, R3).
2. Gains largest on the high-resolution ScreenSpot-Pro, in both training settings (R3, R4, DA observation).
3. Honest reporting of sensitivity (§5.2), concurrency (§2) and non-SOTA status (§5.1) (R2, R4).

**Key Concerns Requiring Attention:**
1. The resolution-generalization and "explicit mapping" explanation is untested: no resolution-controlled experiment, no mechanism control, and ScreenSpot-Pro differs by domain (R1, R2, R3, DA: CONSENSUS-4).
2. The headline "31.1% to 37.2%" is measured against a different model; the matched gain is 34.6 → 37.2; "consistent" gains include decreases (R1, R4, DA: CONSENSUS-3).
3. Single runs with gains mostly at the level of benchmark sampling noise; I-MRoPE gains of 0.2–0.5 points and concurrent with Qwen3-VL (R1, R2, R4, DA).

**Critical Challenge (Devil's Advocate):** No CRITICAL issue was raised. The DA's strongest objection is that the data show correlation between adding RULER tokens and accuracy, not that the explicit mapping mechanism or resolution generalization is the cause; controls (shuffled values, unshared position IDs, visible-grid baseline) and a resolution sweep would address it.

**Decision: Borderline Reject (3)**

On balance the reasons to reject outweigh the reasons to accept for this draft, mainly because the central explanation is not tested and the headline is inflated; both are fixable with inference-only analyses and a few fine-tuning controls, and a revised version with a resolution sweep, controls, variance estimates and a corrected headline would be a considerably stronger submission. Please refer to the Revision Roadmap below.

Sincerely,
Marguerite Okonkwo-Reyes
Editor-in-Chief (meta-reviewer)

---

## Score Summary

### Official Scores and EIC Assessment (`aggregate_scores.py scores.json --venue iclr --final 3`)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 52 | 55 | 62 | 55 | 44 | 53.6 | 52.9 | 18 |
| Clarity & Presentation | 60 | 62 | 68 | 58 | 56 | 60.8 | 60.2 | 12 |
| Novelty & Originality | 50 | 52 | 64 | 54 | 46 | 53.2 | 52.2 | 18 |
| Significance & Impact | 52 | 52 | 66 | 54 | 46 | 54.0 | 53.0 | 20 |
| Experimental Validation | 46 | 50 | 58 | 50 | 40 | 48.8 | 47.9 | 18 |
| Reproducibility | 62 | 60 | 66 | 60 | 55 | 60.6 | 60.2 | 11 |
| Ethical Compliance | 62 | 62 | 66 | 62 | 60 | 62.4 | 62.1 | 6 |
| **Composite** | 53.3 | 55.0 | 63.5 | 55.2 | 47.7 | **54.9** (before) | **54.2** (after) | |
| Pool position | 42 | 44 | 66 | 50 | 36 | | EIC: 47 | |

Reviewer weights (EIC, internal): R1 0.85 × 1.25, R2 0.85 × 1.0, R3 0.70 × 0.75, R4 0.85 × 1.0, DA 0.85 × 1.0. No spread exceeds 20 (Significance is at 20, not above); the only notable divergence is R3's lenient column vs the DA's strict column, adjudicated above.

### Target-Venue Scores (ICLR 2026 cycle, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution | 2 / 2 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); Overall 3 (Borderline Reject) |

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Mechanism / resolution claim untested | R1, R2, R3, DA | CONSENSUS-4 |
| Headline gain vs matched baseline; overclaiming | R1, R4, DA | CONSENSUS-3 |
| I-MRoPE concurrency/tiny gains | R1, R2, R4, DA | CONSENSUS-4 |
| Method format ambiguity | R1, R3, R4 | CONSENSUS-3 |
| Baseline coverage / matched data | R1, R2, R4 | CONSENSUS-3 |
| No limitations / failure cases | R1, R3, R4 | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Are the gains "consistent" and the idea sufficient for acceptance? | R3 (consistent, practical; Overall 4) | DA, R1 (not tested, within noise) | Direction is consistent in aggregates but not in all sub-columns; verified against Tables 1–3; weights favor R1/DA on rigor |
| Severity of the Pro result | R3 (aligned with target) | DA (confounded with domain shift) | §4 itself states domain shift; DA correct |

### Score Spread Discussion
No dimension exceeds 20 (Significance = 20, flagged only if > 20). R3's scores sit 8–20 above the others; the EIC down-weights R3 to 0.75 because the paper's resolution claim is stated as shown but untested.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Mechanism untested | Yes (R1, R2) | n/a | n/a |
| DA-M2 | MAJOR | Resolution confound | Yes (R1, R3) | n/a | n/a |
| DA-M3 | MAJOR | Headline/claim distortion | Yes (R1, R4) | n/a | n/a |
| DA-M4 | MAJOR | I-MRoPE concurrency, overclaim | Yes (R2, R4) | n/a | n/a |
| DA-M5 | MAJOR | Single runs | Yes (R1) | n/a | n/a |
| DA-M6 | MAJOR | Overgeneralization | Partly (R3-W3) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix; EIC-verified issues undermining main claims)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Resolution-generalization and mechanism claims untested | R1-W1, DA-M1, DA-M2, R2-W2, R3-W1 | §1, §3.1, §5.1, Fig. 3 | (a) inference-only resolution sweep (rescale the same screenshots, ±RULER, plus two baselines); (b) shuffled-value and unshared-position control fine-tunes; (c) visible-grid overlay baseline; (d) x/y-digit vs wrong-element error decomposition | Medium–High; sweep: a few GPU-h; 3 control fine-tunes at the A.2 recipe ≈ 3× one fine-tune | Partly (sweep and error decomposition yes; controls borderline) |
| R2 | Headline and wording: 31.1 → 37.2; "consistent", "significant", "overlooked" | ERR-1, R4-W1, DA-M3, DA-M4 | Abstract, §1, §5.1 | Report 34.6 → 37.2; state decreases; scope wording; state the baseline row's construction | Low | Yes |
| R3 | No variance; deltas within noise | R1-W2, DA-M5 | Tables 1–3 | Paired bootstrap on per-item outputs; 3 seeds for the LLaVA-NeXT ladder (≈ 100–200 GPU-h, estimate) | Low (bootstrap) / Medium (seeds) | Bootstrap yes |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | I-MRoPE: cite and differentiate VideoRoPE/HoPE; present Qwen3-VL as concurrent; show training-loss evidence; reduce claim to tested setting | R2-W1, R1-W4, DA-M4 | Edit text; add loss curves | Low | Yes |
| S2 | Baseline provenance and matched-data comparison; mark copied vs reproduced rows; unify the averaging rule | R1-W3, ERR-2, R4-W4 | Add †/‡ marks; recompute Avg consistently; add one matched-data baseline | Low–Medium | Yes |
| S3 | Method clarity: worked token-layout example, training target format, RULER value tokenization, Eq. 2 and Eq. 8 notation, p/s definitions | R4-W2, R1-ERR-3/5 | Add an example figure/box | Low | Yes |
| S4 | Efficiency evidence: measured latency; consistent "<1%" scope | R1-W5, DA-m3 | Latency at 1080p/4K on stated GPU | Low | Yes |
| S5 | Related work: Set-of-Mark, Pix2Seq, VideoRoPE, resolution/zoom GUI methods (verified references) | R2-W2/W3 | Add paragraph; discuss recent preprints as worth discussing | Low | Yes |
| S6 | Qualitative examples, failure cases and a real limitations paragraph | R4-W3, R3-W4 | Add random examples, limitations and dual-use note | Low | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | DPI/anisotropic/multi-image tests | R3-W1/W2 | Add one test each |
| N2 | Non-GUI localization task or narrow the §6 sentence | R3-W3 | Edit or add |
| N3 | Typos, citation (LLaVA-558K 2024a/2023), "Video RoPE" name, A.2 pixel units | R1, R2 | Fix |
| N4 | Private-communication sentence in §2 | DA-m4 | Rephrase to cite a public source |

## Estimated Revision Effort
- Priority 1: 3 items, ≈ 1–2 weeks (resolution sweep and error decomposition in days; controls and seeds ≈ 1–2 weeks of GPU time on 8×H100).
- Priority 2: 6 items, ≈ 3–5 days (mostly writing and re-averaging).
- Priority 3: 4 items, ≈ 1–2 days.
- **Total estimated revision time**: ≈ 2–3 weeks.

*(Gap Scout / Post-Review Analysis not requested; not run.)*
