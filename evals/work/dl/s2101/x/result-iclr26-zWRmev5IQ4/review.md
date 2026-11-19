# Academic Paper Review: DiTraj: Training-free Trajectory Control For Video Diffusion Transformer

*Simulated review (full mode), target venue ICLR, literature check: strict, cutoff 2025-09-24. Date: 2026-11-10. This is a simulation of how a careful panel would likely see this draft, not a prediction of the outcome. The five reviewers were run one after another in a single model context (not independent agents). Figures were not available: figure-dependent claims are judged from captions and text only, and this is stated where it matters. Figure 1 (including its caption) is absent from the extracted text altogether.*

---

# Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | DiTraj: Training-free Trajectory Control For Video Diffusion Transformer |
| Primary Discipline | Computer Vision / ML → controllable video generation (text-to-video diffusion) |
| Secondary Discipline(s) | Transformer position encodings (RoPE); computer graphics (animation / cinematography); LLM prompt engineering |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Video DiT with 3D full attention and 3D-RoPE (Wan2.1-1.3B, CogVideoX-5B); cross-attention masking; position-embedding manipulation; LLM-derived foreground/background prompts (Qwen3) |
| Target Venue | ICLR (stated by the user); profile key `iclr` (2026 cycle, scale status *secondary*) |
| Venue-Specific Notes | none (no ECCV/ACM MM/TPAMI-specific rule applies) |
| Paper Maturity | Submission-ready draft; no limitations section, no code link |
| Ethics-Relevant Content | Generative video model (misuse potential not discussed); a 24-participant user study (§4.3) without a stated consent/ethics statement |

### Claimed Contributions (as stated by the authors, §1 and §5)
1. **C1**: "the first training-free framework tailored for DiT for trajectory controllable video generation, which requires no inversion and inference-time optimization" (contribution 1).
2. **C2**: foreground-background separation guidance: an LLM splits the prompt into foreground and background prompts, applied through a box-derived cross-attention mask (§3.2).
3. **C3**: STD-RoPE: align the spatial position embedding of foreground tokens across frames to an anchor box, keep the temporal part, plus a self-attention "R-token" mask (§3.3).
4. **C4**: "3D-aware trajectory control by regulating the density of position embedding" (§3.4, Fig. 5).
5. **C5**: "DiTraj outperforms existing methods in both video quality and trajectory controllability" (Abstract, §4.3, Table 1).
6. (Conclusion) "We reveal the potential connection between position embedding and attention score" (§5).

## Paper memory (factual record shared with all reviewers)

- **Setup facts.** Backbones: Wan2.1 (1.3B per Table 4) and CogVideoX (5B per Table 4); 50 inference steps, ta = 30, tb = 5 (§4.1). Wan: 480×832, 81 frames, CFG 5; CogVideoX: 480×720, 49 frames, CFG 6; single A100 (A.2.1). LLM: Qwen3, size not stated (A.2.1; template in A.2.3). Evaluation: 56 prompts × 10 noises = 560 videos per method (A.2.1); prompts "mostly extended from previous baselines (Jain et al., 2024; Ma et al., 2024)" with a manually designed box trajectory per prompt (A.2.2). Metrics: five VBench dimensions (SC, BC, MS, AQ, IQ) and, following Peekaboo, OWL-ViT-large detections → Cov, mIoU, CD, AP50 (§4.3). User study: 24 participants, choose best of seven videos on three aspects (§4.3, Table 2). Baselines: Peekaboo, TrailBlazer, FreeTraj (training-free); Tora, Direct-a-Video, LVD (training/optimization-based) "followed their original models and parameter settings" (A.2.1); their backbones, resolutions and frame counts are not stated. Tora receives only the box centre point (A.2.1). Not stated after search: seeds/variance, a separate tuning/validation prompt set, code/data release, limitations or failure cases, ethics statement, Qwen3 size.
- **Headline numbers** (no numbers in the abstract): §4.3 "improvements of 2.1%, 15.9%, 18.2%, and 2.9%" in Cov, mIoU, CD, AP50 over the second-ranked training-free method (Table 1); §4.4 "slight decrease of 0.4%, 0.1%, and 2.0%" and "improvements of 33.6%, 25.0%, and 97.3%" relative to SG alone (Table 3); Table 4 overhead 5.9% / 4.7%.
- **Appendix adds**: hyperparameters and compute (A.2.1), the full prompt list (A.2.2, 56 prompts), the LLM instruction template (A.2.3), inference overhead (Table 4), the ta/tb sweep (Table 5, Figs. 8–9), extra qualitative results (Figs. 10–11, DiTraj only).
- **Unverifiable here**: all figures (Fig. 1 absent from the text; Figs. 2–11 captions only), colour marking of best/second-best in Tables 1–3, bold in Table 5; the algorithm box (Alg. 1) was extracted as running text.

## Integrity scan (Phase 0, Hard Rule 9)

`scripts/integrity_scan.py --redact` found **no** reviewer-directed text or hidden characters. No injected instructions were noticed while reading. The reviewers read the (unchanged) reviewer copy.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Imara Deschênes-Tull, senior chair at a large public university (North America)
- **Seniority / Expertise**: senior faculty / generative models, evaluation of controllable generation
- **Role**: reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style**: accepts papers with ordinary weaknesses, but enforces protocol rules strictly

### Reviewer 1 (Methodology): Dr. Kasimir Oduya, industrial research lab (Europe)
- **Seniority / Expertise**: senior industry scientist / video diffusion evaluation (VBench-style metrics, detector-based control metrics), generative human-preference studies
- **Review Focus**: research design, statistics, comparison fairness, reproducibility
- **Style**: insists on matched backbones and a tuning set disjoint from the reported set

### Reviewer 2 (Domain): Prof. Leilani Brandvold, vision and graphics group, public university (Oceania)
- **Seniority / Expertise**: senior faculty / controllable video diffusion (motion and trajectory control), position encodings in transformers
- **Review Focus**: literature, theory, domain contribution
- **Style**: reads related work against each design claim

### Reviewer 3 (Perspective): Dr. Mateus Ferrandini, computational cinematography and animation studio research team (South America)
- **Seniority / Expertise**: mid-career / animation pipelines, camera and object blocking, interactive authoring tools
- **Review Focus**: cross-disciplinary connections, deployment, broader impact
- **Style**: constructive, asks how a practitioner would use the method

### Reviewer 4 (Generalist): Dr. Sunniva Achterberg, vision lab, mid-sized research university (Northern Europe)
- **Seniority / Expertise**: mid-career / vision backbones and detection (not video generation)
- **Review Focus**: contribution clarity, venue fit, presentation
- **Style**: typical program-committee member; weighs weaknesses against what ICLR usually accepts

### Devil's Advocate: Dr. Rohan Vellacott, evaluation-methodology group, research institute (South Asia)
- **Seniority / Expertise**: senior researcher / evaluation protocols, causal confounds in generative benchmarks
- **Review Focus**: core-argument challenges, logic, overclaiming
- **Style**: rigorous, never hostile

*Personas are fictional. Assumptions: venue ICLR (stated), paper type empirical, literature check strict with cutoff 2025-09-24.*

---

# Phase 1: Independent Reviews

*(Written before the literature check; the literature-check addendum is appended to Reviewer 2 in Phase 1.5.)*

## Reviewer 1: Methodology

# Peer Review Report

## Paper: DiTraj: Training-free Trajectory Control For Video Diffusion Transformer
## Reviewer: Dr. Kasimir Oduya, Methodology (industrial research lab, Europe; fictional persona)
## Expertise: video diffusion evaluation; detector-based control metrics; human preference studies
## Date: 2026-11-10

### Protocol sweep (full-text search, appendix included)
- Selection: "Therefore, we selected 30 and 5 as the relatively optimal values for ta and tb, respectively." (A.3.2, after Table 5). Table 5 reports the same metrics as Table 1, and its rows (ta=30, tb=5) and (ta=30, tb=0) equal the "DiTraj" and "w/ SG" rows of Table 3 and the Wan2.1 row of Table 1, so the sweep runs on the reported evaluation set.
- Evaluation set: "we generate a total of 560 videos for each inference method, utilizing 56 prompts" (A.2.1); "Our prompt set is mostly extended from previous baselines ... we manually designed a bounding-box trajectory for each prompt" (A.2.2). A separate validation/tuning prompt set is **not stated after search**.
- Also: "We set the number of inference steps to 50, with ta set to 30 and tb set to 5" (§4.1). Both values are fixed for CogVideoX as well, which has no separate sweep.

### Summary
The paper proposes DiTraj, a training-free way to steer where an object appears in text-to-video DiTs. An LLM splits the prompt into foreground and background prompts that are tied to the box region through cross-attention masks (§3.2); in the first few denoising steps, the spatial rotary position embedding of all foreground tokens is replaced by that of an anchor box so that foreground tokens in different frames attend to each other more strongly, with a self-attention mask on repeated-embedding tokens (§3.3); varying the density of the anchor embedding is said to give depth control (§3.4). On 56 prompts the method on Wan2.1 and CogVideoX is compared with six U-Net-era or DiT-trained baselines on VBench quality metrics, detector-based control metrics and a user study (Tables 1–2).

### Strengths
**S1: The mechanism is simple, cheap and plausibly general.** Only position indices and masks change in the first tb = 5 of 50 steps, with 5.9% / 4.7% extra latency (Table 4) and no inversion or optimisation. Two DiT backbones are covered (Table 1).
**S2: Reported arithmetic is consistent.** I recomputed the text's relative gains from Tables 1 and 3: Cov 0.96/0.94 → +2.1%; mIoU 47.3/40.8 → +15.9%; CD (0.11−0.09)/0.11 → 18.2%; AP50 50.5/49.1 → +2.9%; and for the ablation SC −0.4%, MS −0.1%, IQ −2.0%, mIoU +33.6%, CD −25.0%, AP50 +97.3%. All match; Table 3's "DiTraj" row equals the Wan2.1 row of Table 1; Table 4 percentages (11/185, 10/213) match; each column of Table 2 sums to 100%.
**S3: A hyperparameter sweep is shown, and the effect of ta/tb is not hidden.** Table 5 and Figs. 8–9 show that large tb (10, 20) degrades quality and small tb (1) gives weaker control, which is honest evidence about sensitivity.
**S4: Implementation detail for the LLM step is unusually complete.** The Qwen3 instruction template is given verbatim (A.2.3), and the full prompt list is in A.2.2.

### Weaknesses

**W1: Hyperparameters were chosen on the same 56 prompts that produce the headline numbers, and the headline win does not hold at the other swept values.** A.3.2 selects tb = 5 (best mIoU 47.3, CD 0.09, AP50 50.5 in Table 5) and ta = 30; those exact numbers are the Table 1 entries. At other tb values the comparison with the best baseline is lost: tb = 1 gives mIoU 37.9 < TrailBlazer 40.8 and AP50 30.7 < 49.1; tb = 10 gives AP50 47.4 < 49.1; tb = 20 gives AP50 44.7 < 49.1 and SC 0.911 below every baseline in Table 1 (SC 0.920–0.936). With no disjoint tuning set, the reported margins are optimistic by an unknown amount. (This is the DA's criterion-3 territory; I flag it as MAJOR protocol flaw E4 and pass the quotes to the DA.)
- **Suggested Fix**: fix ta, tb on a separate set of 20–30 new prompt/trajectory pairs, then report the 56-prompt result and a fresh disjoint test set (e.g., 56 new prompts × 10 noises, ≈ 560 videos × 185 s ≈ 29 A100-hours for Wan2.1-1.3B).

**W2: Table 1 compares different generator backbones, so the video-quality and part of the control gains are not attributable to the method.** The baselines' backbones, resolutions and frame counts are not stated (A.2.1: "we followed their original models and parameter settings"), while DiTraj runs at 480×832×81 (Wan) or 480×720×49 (CogVideoX). VBench Aesthetic/Imaging Quality (AQ 0.627 vs. 0.482–0.593; IQ 0.677 vs. 0.544–0.671) and the user study (Table 2) are strongly backbone-dependent. The only same-backbone controls are "original" and "w/ SG" (Table 3); no baseline mechanism (e.g., TrailBlazer/Peekaboo-style masking or FreeTraj noise initialisation) is ported to Wan2.1.
- **Suggested Fix**: add Wan2.1-based baselines (Wan2.1 + box-masked cross-attention; Wan2.1 + FreeTraj-style noise rearrangement) and list every baseline's backbone, resolution and length in Table 1. Cost ≈ 3 methods × 560 videos × ~185 s ≈ 86 A100-hours; a 20-prompt subset is ≈ 10 hours.

**W3: Most design claims have no ablation.** Table 3 only contains {original, w/ SG, full}. There is no STD-RoPE without SG, no ablation of the R-token mask (claimed to remove artifacts and "further enhances control performance", §1), none for keeping the temporal PE ("ensures the coherence of the object", §3.3), none for the random anchor of Alg. 1 line 3 vs. a fixed or centred anchor, and no quantitative evaluation of the "3D-aware" depth control (C4; §3.4 relies on Fig. 1 and Fig. 5, which I could not inspect).
- **Suggested Fix**: extend Table 3 with {SG, STD-RoPE w/o mask, STD-RoPE + mask, temporal PE also aligned, anchor choices} and, for C4, a metric (e.g., box-area/depth-ordering correlation) on dynamic-size box trajectories with and without density change. Cost ≈ 5 extra configurations ≈ 25 A100-hours.

**W4: The LLM step rewrites each prompt into 80–100-word foreground and background prompts, which is a confound for "separation guidance".** §3.2 describes "appropriate semantic expansion", and A.2.3 requires "around 80-100 words". Table 3 attributes the "w/ SG" quality gain (IQ 0.608 → 0.691, SC 0.924 → 0.941, MS 0.976 → 0.991) to the guidance, but the paper does not say whether "original" uses the short original prompt (most benchmark prompts in A.2.2 are short, roughly 5–15 words), nor include a Wan2.1 + prompt-extension control. Part or all of the quality gain may come from prompt expansion, not from separation.
- **Suggested Fix**: add "original + the same expanded prompt (no mask)" and "SG with the original prompt as both foreground and background" rows.

**W5: No variance, and several "outperforms" claims rest on third-decimal differences.** Ten noises per prompt exist (A.2.1) but Tables 1, 3, 5 report single means without std or CI. SC 0.937 vs. Tora 0.936, BC 0.957 vs. 0.956 are called best "across all metrics" (§4.3). The user study (Table 2) uses 24 participants, one choice among seven videos, with no agreement statistic, no statement of randomised order, and no statement of which "Ours" (Wan or CogVideoX) was shown.
- **Suggested Fix**: report mean ± std over noises/prompts (bootstrap over prompts for mIoU/AP50), a paired test vs. the best baseline, binomial/sign tests with CIs for Table 2, and rater counts per item.

**W6: Metric validity and unequal conditioning for Tora.** Control is measured by OWL-ViT detections (§4.3); detection failures change Cov (the "original" model has the best Cov, 0.97 in Table 3). Tora gets only the box centre (A.2.1) but is scored with box-overlap metrics (AP50 3.4, mIoU 21.3 in Table 1), so the Tora row is not a like-for-like comparison. CD has no unit or normalisation. The motivating difficulty is "large movements" (§1, §3.3), but no result is stratified by movement size.
- **Suggested Fix**: state CD's normalisation, report a centre-based metric for Tora, stratify Table 1 by displacement bins, and report detector-failure rate.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E4 | A.3.2 / Table 5 vs. Table 1 | "we selected 30 and 5 as the relatively optimal values for ta and tb" | Hyperparameters picked by score on the reported evaluation set; chosen values give the Table 1 headline numbers | Cross-referenced Table 5 row (30,5) = Table 3 DiTraj = Table 1 Wan2.1 row | High | MAJOR (DA to rule on criterion 3) | Disjoint tuning set |
| ERR-2 | E4 | Table 1, A.2.1 | "we followed their original models and parameter settings" | Baseline backbones/resolutions unstated; quality metrics compared across different generators | Searched full text for baseline backbones: none given | High (omission), Medium (size of effect) | MAJOR | Matched-backbone baselines |
| ERR-3 | E4 | §3.2, A.2.3, Table 3 | "around 80-100 words long" | Prompt expansion is bundled with SG; "original" prompt length not stated | Cross-referenced template vs. A.2.2 prompt list | Medium | MAJOR | Prompt-extension control |
| ERR-4 | E4 | A.2.1 vs. Table 1 | "we use the center point of the bounding-box ... as the condition" | Tora scored with box metrics (AP50 3.4) while given a point | Cross-referenced | Medium | MINOR–MAJOR | Centre-based metric for Tora |

Minor: Algorithm 1 (line 6, `while i ≠ f`) iterates i = 0…f−1 while T has f+1 boxes B0…Bf (could be an extraction/notation artifact; unverifiable); the baseline name is spelled "Trailbrazer" in Fig. 6 and "TrailBlazer"/"Trailblazer" elsewhere; the prompt "A corgi running on the grassland on the grassland." (A.2.2) has a duplicated phrase; "CogVideoX"/"CogvideoX" inconsistent; Table 1 best/second-best colours are not recoverable from text.

### Claim-to-evidence map (key claims)
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | first training-free DiT-tailored, no inversion/optimisation | Abstract, §1, §5 | Method description; Table 4 | Partially (the "no inversion/optimisation" part is shown; "first" untested, see R2) |
| C2 | SG injects the trajectory | §3.2, Table 3 | w/ SG vs. original (mIoU 23.7 → 35.4) | Partially (prompt-expansion confound, W4) |
| C3 | STD-RoPE strengthens cross-frame FG attention and control | §3.3, Fig. 4, Table 3 | One attention map (Fig. 4, block 1, step 1, one prompt); w/ SG → full (mIoU 35.4 → 47.3) | Partially (no aggregate attention statistics; mask and temporal parts unablated) |
| C4 | 3D-aware control by PE density | §3.4, Fig. 5, Fig. 1 | Qualitative only | Unsupported quantitatively (figures unavailable here) |
| C5 | Outperforms existing methods in quality and control | Abstract, §4.3 | Table 1, Table 2 | Partially (backbone confound, selection on eval set, no variance) |

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Sound idea, but selection on the reported set, cross-backbone comparison, incomplete ablation |
| Clarity | 3 | Readable; method steps clear; Alg. 1 and unit/definition gaps |
| Significance | 2 | Useful if it holds on matched baselines; scope is one control type |
| Originality | 2 | STD-RoPE is new; SG largely follows prior masking work |

### Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline margins are measured on the set used to pick ta/tb and against baselines on other backbones; a typical rejected submission shares these flaws and a typical accepted paper has matched baselines.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing | Arithmetic correct; mechanism claim (§3.3) supported by one attention map; sub-components unablated |
| Clarity & Presentation | 66 | Competent | Easy to follow, template disclosed |
| Novelty & Originality | 56 | Competent | PE alignment is a fresh idea; SG is incremental |
| Significance & Impact | 54 | Developing | Niche but real control capability; evidence limited to 56 prompts |
| Experimental Validation | 46 | Developing | Backbone-mismatched baselines, tuning on eval set, no variance, small prompt set |
| Reproducibility | 56 | Competent | Hyperparameters, resolutions, LLM template present; no code, baseline settings and trajectories not released |
| Ethical Compliance | 56 | Competent | No limitations or misuse discussion |

### Questions for Authors
1. Were ta and tb (Table 5) tuned on the 56 evaluation prompts? Results on a prompt set not used to pick them would raise my score; a drop below TrailBlazer/FreeTraj would lower it.
2. Which backbones, resolutions and lengths do the six baselines use in Table 1? A Wan2.1-matched baseline would resolve my largest concern.
3. Does the "original" row of Table 3 use the short prompt or the expanded one? Which mechanism produces the SC/IQ gain?
4. Does Alg. 1 use a random anchor in the main experiments, and how much do results vary with the anchor?
5. What is CD's unit, and how is a trajectory with changing box size handled in the 56 trajectories (does §3.4 apply in Table 1)?

### Limitations Assessment
**Partially.** The paper has no limitations or failure-case section (searched "limitation", "failure"). Add failure cases (multiple objects, occlusion, very small boxes, large aspect-ratio changes) and the dependence on LLM prompt quality.

### Ethics Review Flag
**No**: the generative-video misuse discussion is missing but not a flag-level concern here.

### Overall Score
**3 (Borderline Reject)**: the idea is interesting and cheap, but as evaluated the gains cannot be separated from backbone choice, prompt expansion and tuning on the reported set.

### Confidence
**4**: I checked the tables, the appendix and the arithmetic; I could not see the figures.

---

## Reviewer 2: Domain

# Peer Review Report

## Paper: DiTraj: Training-free Trajectory Control For Video Diffusion Transformer
## Reviewer: Prof. Leilani Brandvold, Domain (vision and graphics group, public university, Oceania; fictional persona)
## Expertise: controllable video diffusion; positional encodings in transformers
## Date: 2026-11-10

### Summary
DiTraj targets box-trajectory control for text-to-video DiTs without training. It combines (i) an LLM-driven split of the prompt into foreground and background prompts with a box-based cross-attention mask, (ii) a re-indexing of foreground tokens' spatial RoPE to a single anchor box during the early "layout" steps so foreground tokens across frames attend to each other, with a mask to remove artifacts from duplicated indices, and (iii) a density change of the anchor embedding to suggest depth. The related-work argument is that U-Net-era training-free methods (Peekaboo, TrailBlazer, FreeTraj, LVD, Motion-zero) do not exploit DiT's joint spatio-temporal attention, while DiT-based Tora needs training.

### Strengths
**S1: A genuinely new handle on DiT trajectory control.** Manipulating RoPE indices rather than latents, noise or attention maps (§3.3) is not something I know from the prior trajectory-control papers cited in §2.2, and it fits the architecture (3D full attention). The idea that attention in video DiTs has a RoPE-induced locality that blocks large displacements (Fig. 4(a)) is a useful observation, consistent with the cited attention analyses (Luo et al., 2025; Wen et al., 2025, §1).
**S2: Correct and fair positioning against the cited baselines in motivation.** §1 and §2.2 correctly separate training-based (Tora, Direct-a-video) from training-free methods and describe inversion/optimisation costs; Tora is correctly identified as the DiT-based, training-based counterpart.
**S3: The method is described at the level of the underlying model.** §3.1 gives 3D full attention and 3D-RoPE in terms of Wan2.1, so the transfer to another DiT is clear (CogVideoX, Table 1).
**S4: Both a within-backbone ablation and cross-method comparison are given**, which is more than many training-free control papers provide (Table 3, Table 1).

### Weaknesses
**W1: Related work omits the most direct neighbours of the design.** §2.2 does not cite box-conditioned or trajectory control with training (Boximator, Ctrl-V, MotionCtrl), training-free motion control for video diffusion (MOFT, MotionClone), training-free 3D-trajectory object control (ObjCtrl-2.5D), or analyses of position encoding for video (VideoRoPE). Several are arXiv-only or concern I2V, so none is a *required* comparison, but the 3D-aware claim (C4) and the "training-free" positioning should be discussed against them (see the addendum).
- **Suggested Fix**: add a short paragraph and table row per line of work; clearly state what is different (box-conditioning, DiT, training-free).

**W2: "First" and "tailored for DiT" are asserted, not shown.** The claim in §1 contribution 1 and §5 is checked only against the authors' own related work. The method relies only on 3D-RoPE and cross-attention, so its DiT specificity is an argument rather than a result: no experiment shows that SG alone or STD-RoPE alone fails on a U-Net video model, or that a simpler per-frame mask on Wan2.1 would be insufficient (cf. R1-W2).
- **Suggested Fix**: soften "first" to "to our knowledge" and add a Wan2.1 + masked-attention baseline.

**W3: The mechanism explanation in §3.3 is not rigorous.** The paper attributes the diagonal attention to the fact that "similar 3D-RoPE embeddings lead to comparable rotation angles ... resulting in more similar feature representations and thus higher attention scores". RoPE rotates queries and keys and gives a relative-position-dependent dot product; it does not make features similar. The observation is supported by a single attention map (Fig. 4, block 1, first step, one prompt). Same-PE regions having "highly similar attention scores" (Fig. 4(b)) is also consistent with identical positional bias with content playing no role, and does not isolate the claimed cause. The conclusion's claim of a "connection between position embedding and attention score" (§5) is therefore stronger than the evidence.
- **Suggested Fix**: replace the explanation with a measured one: average foreground cross-frame attention mass over blocks, heads, steps and prompts with and without STD-RoPE; reword the "reveal" claim.

**W4: C2 is substantially covered by prior masking work; its novelty is the LLM split.** Box-masked cross-attention for foreground and background is the central device of Peekaboo and TrailBlazer (cited, §2.2); the new element is the LLM-generated pair of prompts, which is small and, as R1-W4 notes, bundled with prompt expansion.
- **Suggested Fix**: state this lineage in §3.2 and present SG as an adaptation to DiT cross-attention.

**W5: 3D-aware control conflates box size and depth.** In §3.4, bounding-box size changes already change the foreground region; the PE-density change is claimed to convey camera distance, but without a quantitative test (and with Fig. 1 not available to me) it is not shown that density is needed in addition to the box.
- **Suggested Fix**: ablate with/without density modification on dynamic-size trajectories and report apparent-size and depth-order metrics.

### Missing References
*Follow the citation-integrity rule; every entry below was found by `related_search.py verify` (arXiv).* See the literature-check addendum for priority classes and links.

### Novelty and literature-check addendum (Phase 1.5)

**Run:** `literature check: strict`, cutoff 2025-09-24; 7 queries (5 claim, 1 expansion, 1 baseline; budget 12); similarity run; coverage gap closed except benchmark scout (VBench is not a trajectory benchmark: the scout returned VBench itself and unrelated papers, no comparable baseline numbers). All searches used concept words only; no result was the paper itself, no text-overlap flag (shared 8-grams = 0 for all kept results; highest cosine 0.241, below the 0.30 overlap threshold). arXiv-only search: "no close prior work found" is a limit of the search, not evidence of novelty.

**Per-claim novelty (claim-level profile, `related_search.py novelty`):**

| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|---------------------------------------------|-----------|
| C1 first training-free DiT trajectory control | method | medium | FreeTraj (3, https://arxiv.org/abs/2406.16863v1, prior arXiv-only, cited); TrailBlazer (3, cited); Tora (3, https://arxiv.org/abs/2407.21705v4, prior peer-reviewed, cited) | No prior training-free DiT-specific trajectory method found in this arXiv search; U-Net training-free and DiT training-based work partly cover the problem. "First" cannot be confirmed from this search. |
| C2 FG/BG separation guidance | method | incremental | TrailBlazer (4, https://arxiv.org/abs/2401.00896v2, prior arXiv-only, cited) | Box-masked cross-attention is covered by Peekaboo/TrailBlazer; the LLM prompt split is the delta. |
| C3 STD-RoPE + R-token mask | method | high (arXiv-only search) | VideoRoPE (2, https://arxiv.org/abs/2502.05173v3, not cited) | No close prior method re-indexes foreground RoPE across frames for control found. |
| C4 3D-aware control by PE density | method | medium | ObjCtrl-2.5D (3, https://arxiv.org/abs/2412.07721v2, I2V training-free 3D trajectory via camera poses, not cited) | Same goal (depth-aware training-free trajectory), different mechanism. |

Script reading: "no central claim fully covered by prior work"; attribution (closest to the paper as a whole): TrailBlazer. One established-ish claim (C2) is a claim-level finding of MAJOR at most.

**Novelty delta table (closest prior works):**

| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|----------------------|------------------|---------------------------|
| C2 | TrailBlazer, Peekaboo | Masked cross/spatial attention from boxes, training-free (U-Net) | LLM-generated FG and BG prompts; DiT cross-attention | Cited (§2.2); differentiation limited to "U-Net" |
| C1/C5 | FreeTraj | Training-free box trajectories via noise and attention | DiT, no noise rearrangement | Cited; compared (Table 1, different backbone) |
| C4 | ObjCtrl-2.5D | Training-free depth-aware trajectory via camera poses (I2V) | PE density in T2V | Not cited |
| C3 | (none found) | – | RoPE re-indexing of foreground tokens | – |

**Baseline scout table:** not applicable: the paper reports on its own 56-prompt protocol (adapted from Peekaboo) plus VBench dimensions on its own videos, so no external leaderboard numbers can be checked; no under-reported baseline can be judged. Under the stated setting, the earlier concern about baseline settings is a question (R1-W2).

**Field snapshot (as of the cutoff).** Three to four years ago, controllable video generation meant U-Net T2V models with adapters (VideoComposer-style) or inference-time tricks (Peekaboo, TrailBlazer, FreeTraj, LVD). By 2025 open DiT video models (CogVideoX, HunyuanVideo, Wan) dominate, and trajectory control is delivered mostly by trained adapters (Tora, and others). Training-free control tailored to DiT attention/position encodings is an open sub-problem, with training-free motion work such as MOFT and MotionClone still mostly on U-Net backbones. A significant contribution in this sub-field now is a control capability that works on a strong DiT backbone without training, evaluated against baselines run on the same backbone, ideally with a held-out prompt/trajectory benchmark; a few-point gain over old U-Net baselines on a small prompt set is the expected baseline, not a significance argument. I used this to score Novelty above the typical submission (a new handle) but Significance and Experimental Validation at the borderline.

**Missing references (verified, priority by label):**

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | none | No prior work found with the same task *and* mechanism |
| Important | Jiawei Wang et al., "Boximator: Generating Rich and Controllable Motions for Video Synthesis", arXiv 2024 (https://arxiv.org/abs/2402.01566v1; prior, arXiv-only) | Box-conditioned motion control for video diffusion (training-based); the closest conditioning interface |
| Important | Zeqi Xiao et al., "Video Diffusion Models are Training-free Motion Interpreter and Controller", NeurIPS 2024 (https://arxiv.org/abs/2405.14864v3; prior, peer-reviewed) | Training-free motion control through features of video diffusion models |
| Important | Zhouxia Wang et al., "ObjCtrl-2.5D: Training-free Object Control with Camera Poses", arXiv 2024 (https://arxiv.org/abs/2412.07721v2; prior, arXiv-only) | Training-free, depth-aware 3D trajectory control; relevant to C4 |
| Helpful | Zhouxia Wang et al., "MotionCtrl: A Unified and Flexible Motion Controller for Video Generation", SIGGRAPH 2024 (https://arxiv.org/abs/2312.03641v2; prior, peer-reviewed) | Object and camera motion control by training |
| Helpful | Ge Ya Luo et al., "Ctrl-V: Higher Fidelity Video Generation with Bounding-Box Controlled Object Motion", TMLR 2025 (https://arxiv.org/abs/2406.05630v3; prior, peer-reviewed) | Bounding-box-controlled video generation |
| Helpful | Xilin Wei et al., "VideoRoPE: What Makes for Good Video Rotary Position Embedding?", arXiv 2025 (https://arxiv.org/abs/2502.05173v3; prior, arXiv-only) | Analysis of spatio-temporal RoPE design that bears on the STD-RoPE rationale |

*Citation check (E7).* The cited baselines match their bibliography entries: Peekaboo (2312.07509), TrailBlazer (2401.00896), FreeTraj (2406.16863), Tora (2407.21705); §2.2 describes FreeTraj as "noise initialization and resampling, alongside ... a soft mask", consistent with FreeTraj's kept abstract (noise construction and attention computation); the description of Tora ("text, visual, and trajectory conditions") was not checked against its full abstract. One observation: the bibliography entry "Motion-zero" (2401.10150) is cited (§1, §2.2) as inversion-based but is not compared in §4.1, without explanation.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Claims partly unsupported (mechanism, depth, mask) |
| Clarity | 3 | Well organised |
| Significance | 2 | Useful, narrow |
| Originality | 3 | RoPE re-indexing is new |

### Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a new, cheap mechanism for an open sub-problem (no close training-free DiT prior found), offset by thin related work and an unrigorous mechanism explanation.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Reasoning about RoPE in §3.3 is loose; method otherwise coherent |
| Clarity & Presentation | 64 | Competent | Clear; related work short |
| Novelty & Originality | 66 | Competent | New handle; SG incremental; field snapshot: new capability on DiT without training is valued |
| Significance & Impact | 60 | Competent | Control capability with small overhead; scope narrow |
| Experimental Validation | 56 | Competent | Reasonable comparisons but backbone-mismatched |
| Reproducibility | 58 | Competent | Details present; no code |
| Ethical Compliance | 58 | Competent | Little discussion |

### Questions for Authors
1. Why is Motion-zero not a baseline when it is cited as the inversion-based alternative (§1, §2.2)?
2. Can you show on a U-Net or on a per-frame-mask Wan2.1 baseline that STD-RoPE adds control beyond what SG gives (raises Novelty/Significance)?
3. How do you separate the density change from the bounding-box-size change in §3.4?

### Limitations Assessment
**Partially.** No limitations or failure cases are discussed.

### Ethics Review Flag
**No.**

### Overall Score
**4 (Borderline Accept)**: a new and well-motivated mechanism for DiT trajectory control that I would like to see at the venue; the evaluation needs matched baselines and the mechanism claim needs measuring.

### Confidence
**4**: I know this sub-field; the search is arXiv-only.

---

## Reviewer 3: Perspective

# Peer Review Report

## Paper: DiTraj: Training-free Trajectory Control For Video Diffusion Transformer
## Reviewer: Dr. Mateus Ferrandini, Perspective (computational cinematography and animation research team, South America; fictional persona)
## Expertise: animation blocking and camera/object choreography; interactive authoring tools
## Date: 2026-11-10

### Summary
The paper gives users a simple "draw a box path" interface to steer a subject in a text-to-video model without fine-tuning. For practitioners the attraction is that the control is applied at inference time on top of strong open DiT models, adds under 6% latency (Table 4), and needs only boxes plus a prompt. The paper argues that the DiT's joint attention gives a better substrate for control than U-Net's factorised attention (§1, Fig. 2).

### Strengths
**S1: Practical interface and cost.** Box trajectories are the kind of control that animators and storyboard artists already draw (blocking). Latency overhead of 11 s on 185 s and 10 s on 213 s is negligible for a production pass (Table 4).
**S2: Plug-in on two different DiTs.** The same ta = 30, tb = 5 settings are used for Wan2.1 and CogVideoX (§4.1), which suggests robustness of the idea to model details; both variants beat several baselines in Table 1.
**S3: Quality and control are reported together.** VBench quality metrics (SC, BC, MS, AQ, IQ) and detector-based control metrics are in the same table (Table 1), and the ablation in Table 5 shows the trade-off explicitly (large tb costs quality), a useful guide to practitioners.
**S4: The depth idea is attractive for authoring.** A single mechanism for "closer to the camera" is what a director would want (§3.4), even though it is only shown qualitatively (Fig. 5; Fig. 1 not available to me).

### Weaknesses
**W1: The evaluation is far from real authoring conditions.** The 56 prompts are short single-subject descriptions (A.2.2); there are no multi-object scenes, occlusion, camera motion, subjects that rotate, or box paths that cross. A typical production brief involves several actors and a moving camera; the paper says nothing about two boxes or overlapping boxes (the R-token mask of Eq. 6 blocks attention between repeated-embedding tokens and foreground tokens, which could interfere when two foregrounds share an anchor).
- **Suggested Fix**: add a multi-object/crossing-trajectory test and a camera-motion test; show failure cases (very small boxes, aspect ratio changes, extreme speeds).

**W2: Dependence on an LLM rewrite and fixed template.** The foreground prompt is forced to be a "close-up shot ... the main subject fills the entire frame" (A.2.3), which will change style/composition for non-animal subjects and may conflict with user intent (e.g., wide shots). Sensitivity to LLM size/choice (Qwen3 size is not given) and to user-written, longer prompts is unreported.
- **Suggested Fix**: ablate LLM choice and report results for human-written detailed prompts; allow users to supply their own FG/BG prompts.

**W3: Misuse and limitations are not discussed.** Precise object/person motion control in video generation raises misuse (fabricated footage of people, e.g., prompt "A man in gray clothes running in the summer", A.2.2) and no statement on safeguards, provenance, or limitations appears (searched). The 24-person user study has no stated consent or compensation statement (§4.3).
- **Suggested Fix**: add a short broader-impact and limitations section; state user-study protocol.

**W4: Assumption: the box marks a *foreground object that stays the same object*.** Several design choices assume one rigid, always-visible foreground (an object mask by box; repeated-PE logic by anchor box). Non-rigid or deformable subjects, or objects that leave the frame, are not exercised.
- **Suggested Fix**: include such cases or state the scope.

### Cross-disciplinary connections
- Graphics: layout-conditioned image generation has used region-specific prompts and attention masks for years; the paper's FG/BG split resembles *regional prompting*, and the paper could cite it as lineage (no specific citation recommended without verification).
- Signal processing: STD-RoPE re-indexes positions, i.e., a coordinate re-mapping; the 3D-aware step resamples position indices by nearest-neighbour upsampling, which is a resampling of the coordinate grid with possible aliasing; interpolation alternatives (e.g., linear interpolation of RoPE angles, as used in position-interpolation approaches for long-context transformers) could be tested.
- Animation: authors could allow keyframed boxes with easing curves; at present trajectories are "manually designed" (A.2.2) with no stated sampling of speeds.

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence limited to simple scenes |
| Clarity | 3 | Clear |
| Significance | 3 | Practical, low-cost control |
| Originality | 3 | New handle |

### Dimension Scores (0–100)
**Pool position:** better than about 68% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a practically attractive, plug-in control capability on current open DiTs, with results on two models; limited by narrow scenes and no limitations discussion.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Coherent design |
| Clarity & Presentation | 66 | Competent | Understandable |
| Novelty & Originality | 66 | Competent | New control handle |
| Significance & Impact | 68 | Competent | Useful to authoring workflows |
| Experimental Validation | 58 | Competent | Simple scenes only |
| Reproducibility | 60 | Competent | Details given; no code |
| Ethical Compliance | 52 | Developing | No limitations or misuse discussion |

### Questions for Authors
1. What happens with two foreground boxes (different anchors, crossing paths)? A working example would raise my score.
2. How does the method behave when the foreground prompt is not a close-up (A.2.3 forces "close-up")?
3. Is the 3D-aware control quantified anywhere?

### Limitations Assessment
**No.** No limitations section.

### Ethics Review Flag
**No**: standard generative-video misuse concerns, not an acute violation.

### Overall Score
**4 (Borderline Accept)**: a useful, cheap capability with a clear interface, and weaknesses that are typical of accepted control papers (narrow scenes, simple prompts).

### Confidence
**3**: I am outside the method's technical core and could not see the figures.

---

## Reviewer 4: Generalist

# Peer Review Report

## Paper: DiTraj: Training-free Trajectory Control For Video Diffusion Transformer
## Reviewer: Dr. Sunniva Achterberg, Generalist (vision lab, mid-sized research university, Northern Europe; fictional persona)
## Expertise: visual recognition and detection; transformers for vision (not video generation)
## Date: 2026-11-10

### Summary
The paper presents a training-free method that lets users specify a sequence of bounding boxes to control where a foreground object moves in videos produced by DiT-based text-to-video models. Contributions: LLM-based foreground/background prompts guided through attention masks (§3.2); re-indexing foreground position embeddings across frames so foreground tokens attend to each other (§3.3); and a density variation for depth (§3.4). Experiments on Wan2.1 and CogVideoX with VBench and detector metrics, a user study and ablations show improvement over six baselines (Tables 1–3).

### Venue criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims backed by evidence | Partly: headline gains vs. baselines on other backbones; selection of ta/tb on eval set | Tables 1, 5 |
| Presentation: clear writing and figures | Met (figures not seen) | §3, Fig. 3 caption |
| Contribution: new and useful for the community | Partly met: new RoPE-based handle; narrow evaluation | §3.3, Table 1 |
| Reproducibility / details | Partly: hyperparameters and LLM template given; no code | §4.1, A.2 |
| Limitations stated honestly | Not met | whole paper |

### Strengths
**S1: A clear problem, with a simple and easy-to-state idea.** The one-sentence summary (align foreground position indices across frames so they can attend to each other) is easy to remember and to implement, and the description in §3.3 with Fig. 4 is accessible even to a non-specialist.
**S2: Good coverage of the settings in the paper.** Quality metrics, control metrics, a user study, an ablation, a hyperparameter sweep and inference overhead are all provided (Tables 1–5), which is a more complete experimental section than many method papers of this type.
**S3: Strong numbers on the control metrics.** mIoU 47.3 vs. 40.8 and CD 0.09 vs. 0.11 for the second-best training-free method (Table 1), and +97.3% AP50 over SG-only in the ablation (Table 3) are large for a training-free change applied for 5 of 50 steps.
**S4: Honest sensitivity analysis.** Table 5 shows ranges where the method degrades.

### Weaknesses
**W1: Comparisons are with older, smaller or differently-backboned systems, which makes "outperforms existing methods" (Abstract) hard to interpret.** The baselines are from 2023–2024, mostly U-Net based (§4.1), while DiTraj uses newer DiT backbones; the paper does not show that a trivially adapted baseline on the same backbone would fall behind (R1-W2 gives the detailed protocol). As a non-specialist, I cannot tell how much of Table 1 comes from Wan2.1 being a better video model.
- **Suggested Fix**: add a Wan2.1-based baseline and a table of baseline backbones.

**W2: Presentation of the evidence is thinner than the claims.** Only two qualitative examples are compared with all methods (Fig. 6, "horse" and "tiger", both running animals), the selection is not described, and other qualitative figures only show DiTraj (Figs. 10–11). Phrases such as "outperforming all other methods" (§4.2) and "significantly surpasses" (§4.3) are stronger than what is shown, without variance.
- **Suggested Fix**: random (not curated) prompt grids for all methods, with the selection procedure stated; report variance.

**W3: Missing limitations/failure analysis, and some method details are hard to follow.** Algorithm 1 draws the anchor randomly (line 3) while §3.4 uses the smallest box; which one applies to Table 1 is unclear; the "R-token" definition (Eq. 5–6) is understandable only after careful reading; there is no limitations section.
- **Suggested Fix**: add a limitations paragraph; clarify which anchor rule is used in each experiment and give a small worked example for Eq. 5–6.

Minor: duplicated phrase in A.2.2; inconsistent capitalisation of method names (Fig. 6 "Trailbrazer").

### NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Comparisons need matched backbones |
| Clarity | 3 | Good |
| Significance | 3 | Useful, popular topic |
| Originality | 3 | New mechanism |

### Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: clear, simple, practical idea with sizeable gains and a fuller-than-usual experiment section; accepted papers of this type routinely share the backbone-comparison and small-prompt-set weaknesses.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Sound; some gaps |
| Clarity & Presentation | 64 | Competent | Readable; some undefined choices (anchor) |
| Novelty & Originality | 62 | Competent | New mechanism |
| Significance & Impact | 64 | Competent | Popular task |
| Experimental Validation | 56 | Competent | Many tables, but confounded |
| Reproducibility | 60 | Competent | Details present |
| Ethical Compliance | 56 | Competent | No limitations/impact statement |

### Questions for Authors
1. Which anchor rule (random frame vs. smallest box) was used for Table 1, and how stable is the result across anchors?
2. Which "Ours" was used in the user study (Table 2)?
3. How were the examples in Fig. 6 selected?

### Limitations Assessment
**No.**

### Ethics Review Flag
**No.**

### Overall Score
**4 (Borderline Accept)**: clear idea, solid-looking gains, and weaknesses that are typical of accepted papers at this venue; the comparison caveats keep this from a higher rating.

### Confidence
**4**: Confident about the presentation and venue fit; less about video-generation-specific baselines.

---

## Devil's Advocate

# Devil's Advocate Report

## Paper: DiTraj: Training-free Trajectory Control For Video Diffusion Transformer
## Reviewer: Dr. Rohan Vellacott, evaluation-methodology group, research institute (South Asia; fictional persona)

---

## Steelman
A single, inexpensive change to position indices in the first five denoising steps, together with box-masked prompts, makes a strong open DiT follow box trajectories far better than the unmodified model (mIoU 23.7 → 47.3, AP50 7.7 → 50.5 within the same backbone, Table 3), at a ~5% latency cost, on two different DiTs.

## Core Argument Chain
1. P1: In video DiTs, attention is local in position-embedding space (Fig. 4(a)), so large displacements break cross-frame foreground attention.
2. P2: Aligning the spatial PE of foreground tokens (STD-RoPE) raises cross-frame foreground attention (Fig. 4(c)) and fixes large-motion control.
3. P3: With SG and STD-RoPE the method gives better trajectory accuracy and video quality than prior methods (Table 1, Table 2).
4. P4: The hyperparameters ta = 30, tb = 5 are "relatively optimal" (Table 5).
∴ DiTraj is a superior, training-free, DiT-tailored trajectory controller that generalises across DiTs.

## Strongest Counter-Argument
The headline comparison is not a test of the proposed mechanism; it is a test of one configuration selected on the test set against baselines on different backbones. First, the configuration that produces every DiTraj number in Table 1 (ta = 30, tb = 5) was chosen from Table 5, whose rows are computed on the same 56 prompts × 10 noises (A.2.1): the (30,5) and (30,0) rows are identical to Table 3's "DiTraj" and "w/ SG" rows and to the Wan2.1 row of Table 1. No other prompt set exists in the paper; the prompts and trajectories were made by the authors. Within that very sweep the headline win is fragile: at tb = 10 AP50 is 47.4 (TrailBlazer 49.1), at tb = 1 mIoU is 37.9 (TrailBlazer 40.8), at tb = 20 SC is 0.911 (all baselines 0.920–0.936). So the reported superiority holds at one point of a sweep chosen for being best on the same data. Second, DiTraj runs on Wan2.1 or CogVideoX, while the baselines are other, mostly older, generators with unstated resolution and length, so VBench quality metrics and the user study (Table 2) mostly measure backbone strength. Third, the within-backbone gain that does isolate the method is only shown for Wan2.1 with an expanded prompt (80–100 words, A.2.3) versus presumably the short original, so even the "w/ SG" row cannot attribute quality gains to separation. If the authors rerun on a disjoint prompt set with matched baselines and the advantage over the best baseline survives, the paper becomes solid; as written, the headline claim of superior controllability and quality is an upper bound produced by selection, not an estimate.

## Issue List

### CRITICAL Issues

| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| DA-C1 | Evidence / Evaluation leakage (criterion 3) | A.3.2 + Table 5 vs. Tables 1 and 3; A.2.1, A.2.2 | Selection quote: "Therefore, we selected 30 and 5 as the relatively optimal values for ta and tb, respectively." Table 5 (same metrics, same 56-prompt set; no separate tuning split exists, A.2.1–A.2.2 "we manually designed a bounding-box trajectory for each prompt") shows (30,5) is the best-scoring tb on mIoU (47.3), CD (0.09), AP50 (50.5). Those same numbers are the headline results: Table 1 "Ours (Wan2.1)" 0.937/0.957/0.990/0.627/0.677 and 0.96/47.3/0.09/50.5 and Table 3 "DiTraj". The main comparison does not hold at other swept values (tb=1: mIoU 37.9 < TrailBlazer 40.8, AP50 30.7 < 49.1; tb=10: AP50 47.4 < 49.1; tb=20: AP50 44.7 < 49.1). Per the criterion-3 table: best-scoring option, chosen by score, produces headline numbers. | Choose ta/tb on a disjoint tuning prompt/trajectory set; report the main table on a fresh held-out set (≥ 56 new prompts × 10 noises) | New data/experiments |

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | Table 1, A.2.1 | Cross-backbone comparison; baseline backbones/resolutions unstated; quality metrics and user study partly measure backbone strength. Supported claim: "better than these systems as released", not "better method" | Matched-backbone baselines; list baseline settings |
| DA-M2 | Alternative explanation | §3.2, A.2.3, Table 3 | 80–100 word LLM-expanded prompts vs. original; the "w/ SG" quality gain (IQ 0.608 → 0.691) may come from prompt expansion | Prompt-extension controls |
| DA-M3 | Claim distortion (E5) | Abstract, §4.3 | "outperforms previous methods in both video quality and trajectory controllability" and "significantly surpasses": the video-quality margins vs. Tora are 0.001–0.003 on SC/BC/MS (Table 1), with no variance; the "first ... tailored for DiT" claim is untested (§1 contribution 1) | Narrow wording; add variance and tests |
| DA-M4 | Logic / mechanism | §3.3, Fig. 4, §5 | Mechanism claim ("similar rotation angles ... more similar feature representations") is asserted from one attention map; the §5 claim of a "connection between position embedding and attention score" overreaches. Components (R-token mask, temporal decoupling, anchor choice) are untested | Aggregate attention statistics; ablations (as R1-W3) |
| DA-M5 | Scope | §3.4, Fig. 5 | 3D-aware claim (C4) has no quantitative evidence, and box-size change is a confound for density | Ablate density vs. box size; add depth-ordering metric |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Qualitative evidence | Fig. 6 | Only two prompts compared across methods; selection not stated (figures not seen; judged from caption and §4.2) |
| DA-m2 | Metric | Table 1 | Tora given only a centre point but scored with box metrics (A.2.1); CD unit unstated |
| DA-m3 | Reporting | Table 2 | 24 participants, seven-way choice, no agreement or CI; which "Ours" shown not stated |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Cov gain vs. second-ranked training-free | 2.1% | (0.96 − 0.94)/0.94 = 2.13% | Yes |
| mIoU gain | 15.9% | (47.3 − 40.8)/40.8 = 15.93% | Yes |
| CD gain | 18.2% | (0.11 − 0.09)/0.11 = 18.18% | Yes |
| AP50 gain | 2.9% | (50.5 − 49.1)/49.1 = 2.85% | Yes |
| SC/MS/IQ change DiTraj vs. SG | −0.4%, −0.1%, −2.0% | 0.941 → 0.937 = −0.43%; 0.991 → 0.990 = −0.10%; 0.691 → 0.677 = −2.03% | Yes |
| mIoU/CD/AP50 change | +33.6%, 25.0%, +97.3% | 35.4 → 47.3 = +33.6%; 0.12 → 0.09 = −25.0%; 25.6 → 50.5 = +97.3% | Yes |
| Inference overhead | 5.9%, 4.7% | 11/185 = 5.95%; 10/213 = 4.69% | Yes |
| Table 2 columns sum to 100% | – | 100.00 / 100.00 / 100.00 | Yes |
| Table 5 (30,0) and (30,5) rows vs. Table 3 | – | identical | Yes (this is what makes DA-C1 apply) |
| "best performance across all metrics" vs. training-based methods (§4.3) | – | true for Ours (Wan2.1) on all nine columns; **not** for Ours (CogVideoX): Cov 0.94 < Tora 0.95; SC 0.935 < Tora 0.936; AQ 0.580 < LVD 0.593 | Partly: holds for the Wan variant only |
| "outperforms all other methods across the five dimensions of video quality" | – | Wan variant: SC 0.937 ≥ 0.936, BC 0.957 ≥ 0.956, MS 0.990 ≥ 0.988, AQ 0.627, IQ 0.677 – holds, but margins of 0.001–0.002 | Yes (immaterial margins) |

## Ignored Alternative Explanations
- Backbone strength (Wan2.1/CogVideoX vs. older generators) explains quality metrics and user preference.
- Prompt expansion by Qwen3 (80–100 words) explains quality gains attributed to SG.
- Prompt/trajectory set overfitting: ta/tb chosen on the evaluation prompts; trajectories are authors' own.
- Detector effects: OWL-ViT on higher-quality videos detects subjects more reliably, inflating Cov/mIoU/AP50 independent of control.
- Simple alternative: Wan2.1 with box-masked cross-attention only plus mild noise initialisation might close part of the gap.

## Missing Stakeholder Perspectives
Creators who need multi-object and camera motion are not addressed; people depicted in generated footage (e.g., "A man in gray clothes running", A.2.2) are not considered; no misuse or provenance discussion.

## Observations (Non-Defects)
- Arithmetic in the text is accurate everywhere I checked.
- The tb sweep is shown openly (Table 5), which is what made DA-C1 detectable, and the ta sweep shows the choice of ta is insensitive above 5.
- The LLM template and prompt list are disclosed (A.2.2, A.2.3).
- Overhead is measured, not estimated (Table 4).

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 50 | Selection on eval set; unablated components; loose mechanism |
| Clarity & Presentation | 62 | Clear |
| Novelty & Originality | 56 | New handle plus incremental SG |
| Significance & Impact | 54 | Useful, but the size of the gain is uncertain |
| Experimental Validation | 44 | Confounds and selection |
| Reproducibility | 56 | No code; settings of baselines missing |
| Ethical Compliance | 56 | No limitations/impact |

**Pool position:** better than about 52% of submissions to ICLR. Deciding evidence: selection on the evaluation set plus backbone-mismatched baselines (typical-rejected signals) against a genuinely new mechanism.

## Overall: 3 | Confidence: 4

---

# Phase 1.5: Literature check

Mode strict, cutoff 2025-09-24; 7 of 12 queries (5 claim, 1 expansion, 1 baseline); similarity, coverage, novelty profile and baseline scout run; results are in the Domain Reviewer's addendum above. No text-overlap flag, no high-conceptual-overlap flag (top cosine 0.241 < 0.30; closest prior works by similarity: FreeTraj, VRoPE, MASH-VLM, the last two are not about trajectory control). Gaps left open: no external trajectory benchmark exists to scout; arXiv-only coverage (published-venue works outside arXiv were not searched).

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1–W6 | kept | Each has location, concrete fix; none answered in the paper (searched A.2, A.3) |
| R1 | W6 (metric validity) | rewritten (ordered last; CD/Tora points kept) | Partly question-like; kept as MAJOR/MINOR |
| R1 | Minor line | moved to Minor | Alg. 1 loop index, typos, duplicates |
| R2 | W1 missing related work | rewritten | Downgraded to "worth discussing / Important": all items are arXiv-only, I2V or training-based, none a required comparison under strict mode |
| R2 | W3 mechanism | kept | Quote from §3.3 verified |
| R2 | W2 "first" | kept | Consistent with the search result (no prior found; untested) |
| R3 | W1–W4 | kept; W4 reordered last | W3's "no limitations" point verified by search |
| R4 | W2 (qualitative thinness) | kept | Verified: Fig. 6 shows two prompts (caption) |
| R4 | Minor line | moved to Minor | typos |
| DA | DA-M3 | kept | Numbers verified; "first" claim narrowed to untested |
| DA | DA-C1 | kept | Selection quote verified at A.3.2; table cross-reference verified |

Scores were not changed.

# Phase 2: EIC Meta-Review and Decision

## Synthesizer part A: issue list and consensus map

| Merged issue | Source IDs | Classification | Hinge? |
|--------------|-----------|----------------|--------|
| Tuning ta/tb on the reported evaluation set; headline margin not robust across the sweep | R1-W1, DA-C1 | CONSENSUS-2 (+ DA-CRITICAL) | **Yes** |
| Cross-backbone baselines; baseline settings unstated | R1-W2, R4-W1, DA-M1 | CONSENSUS-3 | **Yes** |
| Prompt-expansion confound for SG | R1-W4, DA-M2 (R2-W4 related) | CONSENSUS-2 | Partly |
| Missing ablations (R-token mask, temporal PE, anchor, density) | R1-W3, DA-M4, DA-M5, R2-W5 | CONSENSUS-3 | Partly |
| No variance, tiny margins called "outperforms"; user-study reporting | R1-W5, DA-M3, R4-W2, DA-m3 | CONSENSUS-3 | No |
| Mechanism claim (§3.3, §5) not rigorous | R2-W3, DA-M4 | CONSENSUS-2 | No |
| No limitations / failure cases / misuse discussion | R3-W3, R4-W3, R1 limitations, R2 limitations | CONSENSUS-4 | No |
| Related work gaps; "first" untested | R2-W1, R2-W2, DA-M3 | CONSENSUS-2 | No |
| Simple single-object scenes; LLM close-up template | R3-W1, R3-W2 | SOLO | No |
| Metric validity (OWL-ViT, Tora point input, CD unit) | R1-W6, DA-m2 | CONSENSUS-2 | No |
| SPLIT: the overall judgment (R1/DA 3 vs. R2/R3/R4 4) | – | SPLIT | Yes |

**Official score** (plain mean, `scripts/aggregate_scores.py` BEFORE run, no `eic_weight`, DA-C1 provisionally upheld): ratings R1 3, R2 4, R3 4, R4 4, DA 3 → mean 3.60; official composite 57.8; before-EIC starting suggestion 4; cap 3. Dimension spreads ≤ 14, none flagged. Pool positions: 50, 66, 68, 66, 52 (spread 18 < 30).

## EIC Meta-Review (Prof. Imara Deschênes-Tull)

### The Case For and Against
- **For acceptance:** a simple, cheap and new mechanism (re-indexing foreground RoPE across frames, 5 of 50 steps, +5% latency) turns a base DiT with poor trajectory following (mIoU 23.7, Table 3) into one that follows boxes well (47.3), on two backbones; the arithmetic is consistent, the template and prompts are disclosed, and no close training-free DiT prior was found (C3 high, C1 medium).
- **Against acceptance:** the headline numbers come from the (ta, tb) setting chosen by score on the very 56 prompts used to report them, and the main win over the best baseline disappears at other swept values; the baselines run on other, mostly older, backbones; prompt expansion is bundled with separation guidance; most sub-components and the 3D-aware claim lack ablation or quantitative tests; no variance or limitations.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| ta/tb selected on the evaluation set; quote exists | R1-W1, DA-C1 | A.3.2 "we selected 30 and 5 as the relatively optimal values"; Table 5 vs. Tables 1, 3 | **Verified** | Table 5 rows (30,5) and (30,0) equal Table 3 DiTraj and w/ SG; A.2.1/A.2.2 show one authors-built 56-prompt set; no tuning split stated after search |
| Chosen tb is best-scoring and chosen by score | DA-C1 | Table 5 | **Verified** | tb=5 best on mIoU 47.3, CD 0.09, AP50 50.5 (tb=1 is higher on quality columns: SC 0.939, MS 0.991, IQ 0.688 vs. 0.937, 0.990, 0.677; Cov 0.96 is equal at tb=1 and 5, so "best" is on the control metrics) |
| Headline = selected configuration | DA-C1 | Table 1 Wan2.1 row = Table 5 (30,5) | **Verified** | 0.937/0.990/0.677/0.96/47.3/0.09/50.5 identical |
| Main comparison does not hold at other swept values | DA-C1 | Table 5 vs. Table 1 | **Verified** | tb=1: mIoU 37.9 < 40.8 (TrailBlazer), AP50 30.7 < 49.1; tb=10: AP50 47.4 < 49.1; tb=20: AP50 44.7 < 49.1; SC 0.911 below all baselines (0.920–0.936) |
| Baseline backbones/resolutions unstated | R1-W2, R4-W1, DA-M1 | A.2.1, §4.1 | **Verified** | "we followed their original models and parameter settings" |
| Prompt expansion confound | R1-W4, DA-M2 | §3.2, A.2.3, Table 3 | **Partly correct** | The 80–100-word requirement is verified; whether "original" uses the short prompt is not stated, so the size of the confound is unverified |
| Recomputed gains (2.1/15.9/18.2/2.9; −0.4/−0.1/−2.0; 33.6/25.0/97.3) | R1-S2, DA | §4.3, §4.4 | **Verified** | all match |
| Tora scored with box metrics but point input | R1-W6, DA-m2 | A.2.1, Table 1 | **Verified** | impact on the conclusion small (Tora is not the best baseline on control either way) |
| CogVideoX variant "best across all metrics" vs. training-based | DA numerical check | §4.3, Table 1 | **Verified** (it holds only for Wan2.1) | The text says "our approach"; Wan variant satisfies it |
| Mechanism explanation (similar rotation angles → similar features) is loose | R2-W3, DA-M4 | §3.3 | **Verified** (as stated in the text); the attention maps are not visible to me | Fig. 4 not available |
| Missing ablations for mask/temporal/anchor/density | R1-W3 | Table 3 only has 3 rows | **Verified** | |
| No limitations/failure cases | R1, R3, R4 | whole paper | **Verified** | searched |
| "No close prior; first" | R2-W2 | Literature check (arXiv-only) | **Partly correct** | Not contradicted; not confirmable |
| R2's missing references are "required" | R2-W1 | – | **Overstated** (as first drafted) | All items are arXiv-only, I2V or training-based; treated as worth discussing |

No integrity-scan findings and no text-overlap flags were reported.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Decisive point verified at its location (Table 5 vs. Table 1), arithmetic checked, mostly calibrated; one point (prompt confound size) unverified |
| R2 (Domain) | 4 | 4 | 1.0 | Sound; one overstated "missing reference" framing, mechanism critique verified; it did not weigh the selection issue |
| R3 (Perspective) | 4 | 3 | 1.0 | Constructive, correct; relies on figures not visible, mostly generic about practice |
| R4 (Generalist) | 4 | 4 | 1.0 | Fair venue calibration; did not check the sweep against the main table |
| DA | 3 | 4 | 1.25 | Its decisive argument (DA-C1) survived my check, with correct quote and numbers; DA-M3/M4 only partly decisive |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| DA-C1 | The AC test alone would give "No" (small, fixable, paper's idea is interesting). But the criterion-3 table applies: the quote is in the paper (A.3.2), the chosen value is the best-scoring option in its selection table and was chosen by its score, the same numbers are the headline results (Table 1, Table 3), and the main comparison with the best baseline would not hold at other swept values (tb=1, 10, 20). The reporting set is not a hidden-label validation split: the prompts and trajectories were designed by the authors (A.2.2), so the field-practice exception does not apply. The size of the margin is not a reason to downgrade. | **Upheld** (row 3 of the criterion-3 table; no downgrade reason from the table applies) | **New data/experiments** (a disjoint tuning set and a fresh held-out evaluation set; the existing sweep does not contain results selected without the evaluation set) |

### Final Decision and Justification
The EIC-weighted rating is 3.53, which rounds to a **starting point of 4 (Borderline Accept)**; the composite cross-check (EIC-weighted 57.3 → band 3) disagrees by one step, close to the boundary of the band (a one-step disagreement near a boundary is not by itself a reason to depart). The decision departs from the starting point for a named, verified issue: DA-C1, upheld above, which the reviewers rating 4 did not account for (R2, R3, R4 do not mention the selection of ta/tb on the reported set) and which sets a hard **ceiling of 3 (Borderline Reject)** because the fix requires new experiments. I therefore decide **3 (Borderline Reject)**, which does not exceed the ceiling. This is not a judgment that the idea is weak: the mechanism is new and cheap, and the weaknesses besides DA-C1 (backbone-mismatched baselines, missing ablations, no variance, no limitations) are typical of papers accepted at ICLR. A disjoint-set rerun in which the advantage over the best baseline survives, with a matched-backbone baseline and the ablations, would move this paper to Borderline Accept or Accept. **My pool position: better than about 54% of submissions** (upper edge of the typical-rejected band 30–54), deciding evidence: the headline margin is selected on the evaluation set and not shown to be robust, set against a genuinely new mechanism with no close prior. Reviewer pool positions (50–68, spread 18) were not 30 or more apart, so no extra arbitration was needed. For ICLR the venue label of this decision is "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})" per `aggregate_scores.py` (scale status: secondary; verify against the current form).

---

# Editorial Decision

## Paper: DiTraj: Training-free Trajectory Control For Video Diffusion Transformer
## Submission ID: iclr26-zWRmev5IQ4
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC Prof. Imara Deschênes-Tull; R1 Methodology Dr. Kasimir Oduya, R2 Domain Prof. Leilani Brandvold, R3 Perspective Dr. Mateus Ferrandini, R4 Generalist Dr. Sunniva Achterberg, DA Dr. Rohan Vellacott

---

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 3, R2 4, R3 4, R4 4, DA 3 → mean **3.60** · official composite **57.8**
**EIC assessment** (internal): weighted rating **3.53** → starting point **4** · weighted composite **57.3** → band 3 (cross-check, ⚠ differs by one step near the boundary) · **DA ceiling**: 3 · **Final (EIC)**: **3**
**ICLR translation** (scale status: secondary): Soundness 2, Presentation 3, Contribution 2; rating label: "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})". The simulation is not a prediction; verify the scale against the current ICLR form.

---

## Score Summary

### Official Scores and EIC Assessment (output of `aggregate_scores.py scores.json --venue iclr --final 3`)

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| R1 (Meth.) | 4 | 0.85 | 1.25 | 24% |
| R2 (Domain) | 4 | 0.85 | 1.00 | 19% |
| R3 (Persp.) | 3 | 0.70 | 1.00 | 16% |
| R4 (Gen.) | 4 | 0.85 | 1.00 | 19% |
| DA | 4 | 0.85 | 1.25 | 24% |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 54 | 60 | 62 | 60 | 50 | 57.2 | 56.6 | 12 |
| Clarity & Presentation | 66 | 64 | 66 | 64 | 62 | 64.4 | 64.3 | 4 |
| Novelty & Originality | 56 | 66 | 66 | 62 | 56 | 61.2 | 60.6 | 10 |
| Significance & Impact | 54 | 60 | 68 | 64 | 54 | 60.0 | 59.2 | 14 |
| Experimental Validation | 46 | 56 | 58 | 56 | 44 | 52.0 | 51.1 | 14 |
| Reproducibility | 56 | 58 | 60 | 60 | 56 | 58.0 | 57.7 | 4 |
| Ethical Compliance | 56 | 58 | 52 | 56 | 56 | 55.6 | 55.8 | 6 |
| **Composite** | 54.3 | 60.1 | 61.9 | 60.1 | 52.7 | **57.8 (before: 57.8)** | **57.3 (after)** | |
| Pool position (P%) | 50 | 66 | 68 | 66 | 52 | | | |

Ratings: official mean 3.60; EIC-weighted rating 3.53 → starting point 4 (Borderline Accept); composite band 3. DA-CRITICAL cap: 1 upheld (DA-C1), cap 3 (needs new data/experiments).

### Target-Venue Scores (ICLR 2026, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| Venue-weighted composite | 57.4 (band 3, with DA cap 3) |
| Rating (final 3) | "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})" |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "DiTraj: Training-free Trajectory Control For Video Diffusion Transformer" to ICLR. Training-free control of object trajectories in video DiTs is a timely topic, and re-indexing position embeddings is an original way to approach it.

**Overall Assessment:**
The panel found the idea simple, inexpensive and promising, and several reviewers rated the paper as borderline accept. The decisive concern is the evaluation protocol: the chosen hyperparameters were selected on the same set that produces the headline results, and the comparison is not matched in backbone.

**Key Strengths Identified by Reviewers:**
1. A new, cheap mechanism (position-embedding re-indexing in 5 of 50 steps, ≈5% overhead) with a clear rationale in 3D full attention (R2, R3, R4).
2. Consistent reporting of arithmetic and an unusually complete LLM template and prompt list; honest hyperparameter sweep (R1, DA).
3. Works on two DiT backbones, with quality and control reported together (R3, R4).

**Key Concerns Requiring Attention:**
1. Hyperparameters ta and tb were selected on the evaluation prompts, and the advantage over the best baseline does not hold at other swept values (R1-W1, DA-C1; CONSENSUS-2, DA-CRITICAL).
2. Baselines run on different, mostly older backbones with unstated settings; prompt expansion is bundled with the guidance (R1-W2/W4, R4-W1, DA-M1/M2; CONSENSUS-3).
3. Missing ablations (R-token mask, temporal PE, anchor choice, density control), no variance, and no limitations section (CONSENSUS-3/4).

**Critical Challenge (Devil's Advocate):**
The DA argues that every DiTraj number in Table 1 comes from a configuration chosen by score from Table 5 on the same 56 prompts, and that the win over TrailBlazer on AP50 and mIoU vanishes at other tb values. The EIC upheld this after checking Tables 1, 3, 5 and A.2.1–A.3.2. It must be addressed with a disjoint tuning set and a held-out evaluation.

**Decision: Borderline Reject (3)**

This is a decision on the evidence as submitted: the capped rating reflects the need for new experiments rather than a negative view of the idea. If a held-out evaluation with matched-backbone baselines confirms the gains, and the ablations of the mask, temporal PE and 3D control are added, the panel would likely view the paper as a Borderline Accept or better. Please refer to the Revision Roadmap below.

Sincerely,
Prof. Imara Deschênes-Tull
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| No limitations/failure-case discussion | R1, R2, R3, R4 | CONSENSUS-4 |
| Baselines on other backbones; settings unstated | R1, R4, DA | CONSENSUS-3 |
| Component ablations missing (mask, temporal PE, anchor, density) | R1, R2, DA | CONSENSUS-3 |
| No variance; "outperforms" on tiny margins; user-study reporting | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Overall recommendation (accept-leaning vs. reject-leaning) | R2, R3, R4 (4) | R1, DA (3) | EIC verified R1/DA's selection point; the accept-leaning reports did not account for it. Decision 3 via DA ceiling |
| Whether related-work gaps are significant | R2 (framed as required) | – | EIC: worth discussing only (arXiv-only/I2V/training-based, strict mode) |
| Importance of the 3D-aware claim | R3 (attractive) | R2, DA (unsupported) | EIC: promising but not evidenced quantitatively |

### Score Spread Discussion
No dimension exceeds the 20-point flag (largest spreads: Significance 14 and Experimental Validation 14). The widest gap is in Experimental Validation: R1 and DA (46, 44) judge the confounds (selection, backbone), while R2–R4 (56–58) judge the breadth of tables; the EIC sides with R1/DA after verifying Table 5 against Table 1.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-C1 | CRITICAL | ta/tb selected on the reported evaluation set; margin not robust across sweep | Yes (R1-W1 as MAJOR) | **Upheld** | New data/experiments |
| DA-M1 | MAJOR | Cross-backbone comparison | Yes (R1-W2, R4-W1) | n/a | n/a |
| DA-M2 | MAJOR | Prompt-expansion confound | Yes (R1-W4) | n/a | n/a |
| DA-M3 | MAJOR | Claim wording vs. margins and "first" | Partly (R4-W2, R2-W2) | n/a | n/a |
| DA-M4 | MAJOR | Mechanism and components untested | Yes (R2-W3, R1-W3) | n/a | n/a |
| DA-M5 | MAJOR | 3D-aware claim unquantified | Yes (R2-W5, R1-W3) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Hyperparameters selected on the evaluation set; headline margin not robust | DA-C1, R1-W1 | A.3.2, Table 5, Tables 1/3 | Pick ta, tb on a separate tuning prompt/trajectory set; report all main tables on a fresh disjoint set (≥ 56 prompts × 10 noises) and the sweep as sensitivity only; keep best-baseline comparison at the chosen values | Medium; ≈ 30–60 A100-h | Yes (partially; one week is tight for the full set, a 30-prompt subset is feasible) |
| R2 | Backbone-matched comparison | R1-W2, R4-W1, DA-M1 | Table 1, A.2.1 | Add Wan2.1-based baselines (box-masked cross-attention; FreeTraj-style noise rearrangement); list every baseline's backbone, resolution, length | Medium–High; ≈ 10–90 A100-h | Partly |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Prompt-expansion confound | R1-W4, DA-M2 | Add "expanded prompt, no mask" and "original prompt in SG" rows | Low–Medium; ≈ 10 A100-h | Yes |
| S2 | Missing component ablations (R-token mask, temporal PE, anchor, density) | R1-W3, DA-M4/M5, R2-W5 | Extend Table 3; quantify depth control against box size | Medium; ≈ 25 A100-h | Yes (partly) |
| S3 | Variance and tests; user-study reporting; claim wording | R1-W5, DA-M3, R4-W2 | mean ± std/bootstrap CI, paired tests, rater statistics; "outperforms" → "improves over"; "first" → "to our knowledge" | Low | Yes |
| S4 | Mechanism explanation | R2-W3, DA-M4 | Aggregate cross-frame foreground attention before/after STD-RoPE over blocks, heads, steps, prompts; rewrite the RoPE argument | Medium | Yes |
| S5 | Limitations, failure cases, misuse statement; user-study consent | R3-W3, R4-W3 | Add limitations and broader-impact sections; show failure cases | Low | Yes |
| S6 | Missing references (worth discussing) | R2-W1 | Boximator, MOFT, ObjCtrl-2.5D (Important); MotionCtrl, Ctrl-V, VideoRoPE (Helpful) | Low | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Multi-object / crossing trajectories / camera motion | R3-W1 | Add tests |
| N2 | Close-up template and LLM choice | R3-W2 | Ablate LLM and template |
| N3 | Metric validity (CD unit, Tora centre-based metric, displacement bins) | R1-W6, DA-m2 | Clarify and stratify |
| N4 | Fig. 6 sample selection; broader qualitative set for all methods | R4-W2, DA-m1 | Random grids |
| N5 | Alg. 1 loop index, typos, duplicated phrase, anchor rule per experiment | R1 Minor, R4-W3 | Fix |
| N6 | Why Motion-zero is not a baseline | R2 Q1 | Explain or add |

---

## Estimated Revision Effort
- Priority 1: 2 items, ≈ 40–150 A100-hours plus 2–5 days
- Priority 2: 6 items, ≈ 35–50 A100-hours plus writing, 3–5 days
- Priority 3: 6 items
- **Total estimated revision time**: about 2–3 weeks including a clean held-out evaluation

*Post-Review Analysis (Gap Scout) was not requested and was not run.*
