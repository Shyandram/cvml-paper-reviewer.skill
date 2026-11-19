# Simulated Panel Review: "Why does Weak-OOD Help? A Further Step Towards Understanding Jailbreaking VLMs"

*Simulation of how a careful panel would likely see this draft; not a prediction of any outcome. Date: 2026-11-05. Mode: full. Target venue: ICLR. Literature check: strict, cutoff 2025-09-24. Figures were not available (text extraction only): figure-dependent statements rest on captions, axis text and the appendix tables, and say so where it matters. The five reviewer passes were run one after another in a single model context (no subagents); independence was kept by not consulting earlier reports while writing a later one.*

---

## Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Why does Weak-OOD Help? A Further Step Towards Understanding Jailbreaking VLMs |
| Primary Discipline | ML → trustworthy/safe multimodal learning → jailbreak attacks on vision-language models |
| Secondary Discipline(s) | Mechanistic interpretability (refusal/harmfulness directions); adversarial robustness; OCR / typographic prompts |
| Paper Type | Analysis/Insight with a method component (composite weights: analysis) |
| Core Technique(s) | OOD-style image manipulation jailbreaks (SI-Attack, CS-DJ, JOOD); latent-space cosine probes on Qwen2.5-VL-7B; typographic jailbreak with randomized text perturbation (JOCR); LLM-as-judge ASR |
| Target Venue | ICLR (stated by user); profile key `iclr` (2026 cycle, scale status: secondary) |
| Venue-Specific Notes | none (ICLR form: Soundness/Presentation/Contribution 1–4, Rating, Confidence) |
| Paper Maturity | Early draft / borderline submission-ready: appendix carries core definitions, no Limitations section |
| Ethics-Relevant Content | Dual-use: a more effective jailbreak against deployed commercial VLMs, code released (Reproducibility Statement) |

### Claimed Contributions (as stated by the authors; §1 contribution list, Abstract)
1. **C1**: First to investigate current VLM jailbreak methods "from a feature perspective" and to identify the "weak-OOD" phenomenon (mild manipulation beats none; strong manipulation hurts) (§1, §2.2, Fig. 1).
2. **C2**: The phenomenon is a trade-off between *input intent perception* and *model refusal triggering*, which respond inconsistently to OOD manipulation (§3, Table 2, Figs. 3–4).
3. **C3**: The inconsistency stems from the pre-training/alignment gap, with "a theoretical argument for the inevitability of such inconsistency" (Abstract, §3.3, §4.1, App. E–F).
4. **C4**: JOCR, a simple OCR-robustness-based jailbreak, "outperforms SOTA baselines" in performance and efficiency (§4.2, Tables 4–6, App. G.2).

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Ingrid Valdemar, senior faculty at a technical university (Northern Europe)
- **Seniority / Expertise**: Senior faculty, repeat area chair / ML safety, robustness, evaluation methodology
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style**: Decides on whether the central claim is measured; tolerant of ordinary weaknesses, intolerant of untested explanations

### Reviewer 1 (Methodology): Dr. Tomasz Reinholt, industrial research lab (Central Europe)
- **Seniority / Expertise**: Senior industry scientist / red-teaming evaluation, LLM-as-judge validity, representation probing
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every table; asks which split/judge/seed produced each number

### Reviewer 2 (Domain): Prof. Adaeze Okonkwo-Brandt, large public research university (West Africa)
- **Seniority / Expertise**: Mid-career faculty / multimodal jailbreak and defense literature, VLM safety alignment
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Compares claims against the cited abstracts; checks bibliography entries

### Reviewer 3 (Perspective): Dr. Mateo Salcedo, security and human-computer-interaction group, public university (South America)
- **Seniority / Expertise**: Postdoc / applied security, content moderation pipelines, usable red-teaming
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; asks what a defender could do with the result

### Reviewer 4 (Generalist): Dr. Priya Raghunathan, vision lab, large public university (South Asia)
- **Seniority / Expertise**: Mid-career faculty / vision-language models, typical PC member, not a safety specialist
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Reads like a first-time reader; weighs weaknesses against what accepted papers carry

### Devil's Advocate: Dr. Elias Brandvold, evaluation-methodology group, research institute (Northern Europe)
- **Seniority / Expertise**: Senior researcher / causal reasoning in ML evaluation, benchmark validity
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous and fair; asks whether the experiments could have come out differently

*Personas are fictional. Assumptions: paper type "analysis" (a reasonable reader could call it "empirical"); venue ICLR as stated.*

### Paper memory (shared with all reviewers)

- **Claims:** C1–C4 above, with locations.
- **Setup facts.** Sec. 2: 3 targets (GPT-4o, GPT-4.1, Doubao-1.6), GPT-4o as judge (§2.2, App. H); SI-attack on 200 category-balanced MM-SafetyBench items, CS-DJ on 200 HarmBench "training set" items, JOOD on its original 150-item set (§2.2). Sec. 2.3/3.2: Qwen2.5-VL-7B-Instruct, layers 17/19/21 (PCA) and layers 16–28 (Figs. 3–4), 100 refused MM-SafetyBench items, 10 shuffles each (§3.2.3). Sec. 3.3: GPT-4o-mini on full MM-SafetyBench, 4 shuffled variants + unshuffled; 5 (Exp 1–2) or 10 (Exp 3) trials. Sec. 4: seven models (Qwen2.5-VL-7B, InternVL2.5-8B, GPT-4o, GPT-4o-mini, GPT-4.1, Gemini 2.5 Pro; the text says "seven", Table 4 lists six); RedTeam-2K (2,000 questions) and HarmBench (n not stated; values are multiples of 0.5, consistent with 200). Seeds/repeats for ASR: **not stated**. Compute: **not stated**. Splits/tuning for JOCR ranges: **not stated** (App. C only gives the ranges). API model versions/dates: **not stated** (only Doubao access date, bibliography). Code: anonymous GitHub link claimed (Reproducibility Statement); not provided to the panel.
- **Headline numbers:** Table 4 ASR (JOCR 56.80/62.30/31.65/50.40/50.50/43.25 on RedTeam-2K; 78.00/71.50/50.00/70.50/74.50/64.50 on HarmBench); Table 4 caption "JOCR achieves over 10% ASR higher than baselines"; Table 2 (intent similarity, harm accuracy, refusal rate); Table 7 SI-attack ASR 0.475 → 0.605 (GPT-4o).
- **Appendix summary:** App. B related work; C implementation/baselines; D.1 Tables 7–9 (Fig. 1 data), D.2 extra PCA panels; E.1/F formal modeling (Eqs. 8–17); G ablations (Table 10), efficiency note (G.2), JOCR examples (G.3, images not available); H judge prompt.
- **Unverifiable:** all figures (Figs. 1–5 read from axis text only); Eq. 5 symbols partly garbled in extraction; JOCR example images; anonymous code.

### Integrity signals
Manual full-text scan (the `integrity_scan.py` script was not run: this evaluation permits only the aggregation and related-search scripts). No text addressed to reviewers or AI systems was found. Appendix A discloses LLM use for "data generation, result evaluation ... paper polishing ... retrieving related work".

### Literature check (strict, cutoff 2025-09-24)
7 arXiv queries of 12 (claim: C1, C2, C3; baseline: 1; expansion: 2; one expansion query returned unparsable output and was not used). The `similarity` run found no text overlap (0 shared 8-grams with any kept abstract; highest conceptual cosine 0.252 vs JOOD, below the 0.30 flag). Gaps left open: no `scout`/`coverage` run, so the baseline scout table is partial. Search results are arXiv-only.

---

# Phase 1: Independent Reviews

# Peer Review Report (Reviewer 1)

## Paper: Why does Weak-OOD Help? A Further Step Towards Understanding Jailbreaking VLMs
## Reviewer: Dr. Tomasz Reinholt, Methodology (industrial research lab, Central Europe; fictional persona)
## Expertise: red-teaming evaluation; LLM-as-judge validity; representation probing
## Date: 2026-11-05

## Summary
The paper reports that for three OOD-style VLM jailbreaks, attack success is an inverted-U function of the perturbation strength ("weak-OOD"). It explains the effect with two latent-space probes on Qwen2.5-VL-7B (an "intent perception" similarity and a "refusal triggering" similarity) and three behavioral experiments on GPT-4o-mini, attributes it to a pre-training/alignment gap, and proposes JOCR, a typographic attack with randomized font size, spacing, colour and layout, reported to beat prior attacks on six VLMs.

## Strengths
### S1: The inverted-U is real for SI-attack on two of three targets
Table 7 shows GPT-4o ASR 0.475 (1 patch) → 0.605 (4) → 0.380 (25), and GPT-4.1 0.505 → 0.640 → 0.425. With n = 200 each (§2.2) these differences are about 2.6–2.8 standard errors (my computation, unpaired), so the basic observation is not noise for these two models.
### S2: Behavioral probes complement the latent probes
Table 2 measures intent and refusal behavior directly on a deployed model (Exp 1–3, GPT-4o-mini, full MM-SafetyBench, repeated trials). This is a sound design idea and the strongest evidence for C2.
### S3: Reasonable breadth for the headline attack comparison
Table 4 covers two benchmarks (RedTeam-2K at n ≈ 2,000 per cell; HarmBench), four proprietary and two open models, and seven baselines; the FigStep rows are identical in Tables 4 and 5 (consistent). Table 10 reports range sensitivity.
### S4: Concrete reporting of ranges for JOCR
App. C gives the ranges for all five perturbations, so the attack is implementable in principle.

## Weaknesses
### W1: The two latent metrics do not measure what the text says they measure
§3.1 states harmfulness (intent) is encoded at the last token of the full input t_post-inst and refusal at the last token of the user instruction t_inst. §3.2.1 then measures *intent* at t_inst (Eq. 3) and §3.2.2 measures *refusal* at t_post-inst (Eq. 5): the positions are swapped relative to the paper's own premise (also App. E.1). Further, "intent perception" is the cosine between h(x) and h(A(x)) at the same layer: since the text instruction is identical, a high value (0.86–1.00, Fig. 3a axis) is expected for any image change and is not evidence of recognising *malicious* intent; no control (benign image pairs, random images) is given. In Eq. 5, e ∈ R^V is a vocabulary-sized vector while "embedding vectors v_k ∈ R^V" of 50 refusal tokens are also said to be in R^V, and model.head is said to map to "the token embedding space"; a head maps to logits, and applying it to intermediate layers is a logit-lens choice that is not described. The token list is not given and the values are ~0.00–0.02 (Fig. 3b axis), with no control token set.
- **Suggested Fix**: State which position carries which quantity, reconcile §3.1/App. E.1 with §3.2; use a linear probe or the published refusal/harm directions for each position; add benign and random-image controls and a non-refusal token set. ≈ 10 GPU-hours on a 7B VLM.
### W2: The "trade-off" is not shown to explain the ASR curve
(a) §3.2.3 and §3.3 never link the two scores to attack outcomes per sample: each x is shuffled 10 times "regardless of whether the shuffle succeeded in jailbreak". (b) Table 2 refusal keeps falling through Shuffle-25 (84.11% → 73.52 → 67.98 → 65.52 → 63.08), while ASR *falls* after patch 4 (Table 7: 0.605 → 0.380 on GPT-4o); the weak-OOD peak therefore has to come from the intent side, yet intent measures move little (Harm Accuracy 38.80% → 34.02%, a 12% relative drop at Shuffle-25 versus 25% for refusal; derived). (c) The probes run on Qwen2.5-VL-7B / GPT-4o-mini whereas the ASR curves are on GPT-4o/GPT-4.1/Doubao (Fig. 1); no ASR curve exists for Qwen. (d) Fig. 4 compares "sharp" and "gradual" decay using two y-axes with different, independent ranges (≈0.92–1.00 versus ≈0.006–0.012, from the axis text); the visual contrast is a property of axis scaling. (e) The PCA argument in §2.3 (Shuffle-4 farthest, Shuffle-9 nearest to the refusal region; "not due to simple feature destruction") is a 2-D projection with an unspecified "Class Boundary", no distances reported, and conflicts with the monotone trends of Fig. 3–4 and Table 2 for the same model family.
- **Suggested Fix**: On one model, collect per-sample (intent score, refusal score, jailbreak success) and fit a simple model of success on the two scores; normalise the two metrics (z-scores over the unshuffled distribution) before comparing decay; report distances instead of PCA pictures.
### W3: The pre-training vs alignment attribution (C3) has no experiment that separates the two
§3.3 labels Exp 1–2 "pre-training" and Exp 3 "alignment", but all three are run on one post-trained, safety-aligned model (GPT-4o-mini), and Exp 2 ("Harmful/Harmless" judgment) is itself an aligned behavior. Nothing compares a pre-alignment checkpoint with its aligned counterpart. The "theoretical argument for inevitability" (Abstract) consists of definitions and assumptions (Eqs. 7, 11–17: e.g. Eq. 15 and Eq. 16–17 are asserted, ε_dev "is a large deviation threshold"); no theorem is derived, and dist(·, D_pre/D_align) (Eq. 10) is never computed.
- **Suggested Fix**: Test the claim with an open VLM pair (before/after safety tuning, or with/without safety data) and report both behaviors across shuffle degrees; otherwise rename the section a hypothesis and drop "inevitability".
### W4: JOCR comparison and judge protocol
(a) SI-attack and JOOD, the two attacks the paper analyses in §2–3 (and whose OOD logic motivates JOCR), are excluded from Table 4 because "the input ... is images" (App. C); no adaptation is attempted. (b) Table 4's caption says "over 10% ASR higher than baselines" and §4.2.2 says JOCR is higher "compared to all baselines"; recomputed against the best baseline (CS-DJ in every cell), JOCR is below it on RedTeam-2K/GPT-4o (31.65 vs 37.50) and above by more than 10 points in only 4 of 12 cells (derived; mean margin ≈ 8.1 points). (c) ASR comes from a single GPT-4o judge (App. H) that is also a target (Table 4), with no human validation and no stated ASR threshold on the "safe/unsafe plus score" output. (d) App. G.2 reveals "one LLM query for question rewriting", a pipeline step not described in §4.2.1 and not controlled in Table 5 (is FigStep given the same rewriting? which rewriting model? which accompanying text prompt?). (e) Single run per cell; HarmBench cells are ≈ 200 items (≈ ±3.5 points at 50%), so e.g. GPT-4o 50.00 vs 47.50 is not distinguishable.
- **Suggested Fix**: Adapt SI-attack/JOOD to the text-to-image setting (render the query as an image) or add them on their own protocol; give per-cell 95% CIs (bootstrap over items, ≥ 3 repeats); validate the judge on ≈ 200 human-labelled responses and add a second judge from a different family; ablate the rewriting step. ≈ 30–60 GPU-equivalents of API calls.
### W5: Universality of weak-OOD is stated more strongly than Tables 8–9 allow
§2 says results "verified its universality". For CS-DJ (Table 8) the smallest setting is CSI = 3 and for JOOD (Table 9) α = 0.1: neither includes a no-perturbation reference, so "compared to non-OOD" (§2.2) can only be checked for SI-attack. For Doubao-1.6 the SI-attack gain from 1 to 4 patches is +0.045 (0.575 → 0.620; ≈ 0.9 SE, derived). JOOD ASR spans 0.145–0.265 and neighbouring settings differ by 0.01–0.05, within one SE at n = 150–200. No intervals anywhere in Fig. 1/Tables 7–9.
- **Suggested Fix**: Add the zero-perturbation setting for CS-DJ and JOOD, error bars, and report which cells exceed noise.
### W6: JOCR ablations share the reporting benchmark and over-read small differences
Tables 6 and 10 are HarmBench, the same benchmark as the headline (Table 4: 50.00/70.50/74.50 equal the (20,50)/(30,50) row of Table 10). How the ranges and the five perturbation families were chosen is not stated. §4.3.2 calls Word Spacing "crucial" for drops of 4.5/3.0/6.5 points (Table 6) while Layout/Colour changes of up to 2.5 points are "no significant changes", without any test. In Table 10 the best-scoring row is the headline for two of three models, but the claim holds across all rows, so this is a protocol question rather than a leak.
- **Suggested Fix**: State how the configuration was fixed; tune on a separate split (e.g., a held-out part of RedTeam-2K) and report the rest.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E6 | §3.1 vs §3.2.1/§3.2.2 | "Harmfulness (intent perception): Last token of full input (tpost-inst )" | Intent is then measured at t_inst (Eq. 3), refusal at t_post-inst (Eq. 5): swapped relative to §3.1 | Cross-referenced (two locations) | High | MAJOR | Reconcile positions; justify choice |
| ERR-2 | E1/E5 | Table 4 caption vs Table 4 | "JOCR achieves over 10% ASR higher than baselines" | JOCR 31.65 < CS-DJ 37.50 (RedTeam-2K, GPT-4o); gap > 10 points in 4/12 cells | Recomputed per cell | High | MAJOR | Correct the claim; report the per-cell margin |
| ERR-3 | E6 | Eq. 4/6 vs Figs. 3–4 | "compute the average of Simintent,l across all layers" | Figs. 3–4 plot and average layers 16–28 only | Cross-referenced | Medium | MINOR | State the layer range in the equations |
| ERR-4 | E1 | Table 8 | rows "16" then "15" (CSI); Doubao ASR "0.361" | Row order non-monotone (also in Fig. 1b axis); 0.361 is not a multiple of 1/200 though n = 200 (§2.2) | Cross-referenced; arithmetic | Medium | MINOR | Fix labels; state averaging if any |

**Minor**: Eq. 2 compares g(A(x)) with a threshold τ while the text says it must be "lower than that for original malicious input x"; §3.1 cites "Eqs. 8–9" that exist only in App. E.1 (main text has Eqs. 1–2); JOOD ASRs (e.g. 0.145 = 21.75/150) are not multiples of 1/150 though §2.2 says 150 samples (possibly averaged over repeats; see Questions).

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Main mechanism claims rest on mis-specified latent probes and aggregate behavioral numbers |
| Clarity | 2 | Core definitions in appendix; swapped positions; notation gaps |
| Significance | 2 | Useful red-team baseline; explanatory value unproven |
| Originality | 2 | Phenomenon is a new framing of tuned-hyperparameter behavior; JOCR is incremental |

## Dimension Scores (0–100)
**Pool position:** better than about 36% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the central explanatory claim is not measured by the experiments (W1–W3) and the SOTA claim is contradicted in a cell and lacks CIs/judge validation (W4).

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 42 | Developing | Swapped positions, uncontrolled probes, untested attribution |
| Clarity & Presentation | 52 | Developing | Readable story, but definitions split across appendix, inconsistent numbering |
| Novelty & Originality | 48 | Developing | Observation is new framing; method is typography + jitter |
| Significance & Impact | 50 | Developing | Real phenomenon, limited insight beyond tuning |
| Experimental Validation | 44 | Developing | Single runs, one judge, excluded baselines, no zero baselines |
| Reproducibility | 52 | Developing | Ranges given; code unverified; judge threshold, rewriting model, API versions missing |
| Ethical Compliance | 50 | Developing | Boilerplate ethics statement; no dual-use discussion |

## Questions for Authors
1. Is the intent probe at t_inst (as in §3.2.1) or t_post-inst (as in §3.1)? A per-sample regression of jailbreak success on both scores that recovers the inverted-U would raise my rating; a null result would lower it.
2. What is the ASR threshold on the judge's output, and how well does it agree with human labels on ≈ 200 responses? Agreement ≥ 0.85 κ would remove my main concern in W4(c).
3. Is the JOOD/CS-DJ ASR averaged over repeats (n = 150/200 do not give 0.145 / 0.361)? If so, report SDs.
4. Which LLM rewrites the question for JOCR, with what prompt, and does FigStep receive the same rewriting? If not, Table 5's FigStep gap includes a confound.

## Limitations Assessment
**Partially.** No Limitations section exists; the Ethics and Reproducibility statements are generic (see R3). Add: surrogate-model transfer, judge validity, scope of three attacks, absence of defense evaluation.

## Ethics Review Flag
**No** from the methodology side (R3 gives the dual-use view).

## Overall Score
**2**: The inverted-U observation is credible, but the explanation (C2–C3) is not supported by measures that match the paper's own definitions and the "outperforms SOTA" claim is overstated.

## Confidence
**4**: Checked tables and equations in detail; figures were not viewable.

---

# Peer Review Report (Reviewer 2)

## Paper: Why does Weak-OOD Help? A Further Step Towards Understanding Jailbreaking VLMs
## Reviewer: Prof. Adaeze Okonkwo-Brandt, Domain (large public research university, West Africa; fictional persona)
## Expertise: multimodal jailbreak/defense literature; VLM safety alignment
## Date: 2026-11-05

## Summary
The paper positions three recent OOD-style jailbreaks (SI-attack, CS-DJ, JOOD) as one family, argues that their effectiveness peaks at mild perturbation, offers a refusal-versus-intent account building on the harmfulness/refusal-separation literature, and derives a typographic attack (JOCR) from it. The contribution is part empirical observation, part explanation, part new attack.

## Strengths
### S1: Timely, well-chosen question
Why moderate perturbation helps is a real open question for OOD jailbreaks (§1), and putting three methods side by side (Table 1, Fig. 1) is a useful organising step.
### S2: Grounded in a credible line of interpretability work
§3.1 builds on refusal-direction and harmfulness/refusal-separation findings (Arditi et al. 2024; Jiang et al. 2025; Zhao et al. 2025a) and checks them on shuffled images, a sensible extension to the VLM setting.
### S3: Simple, easy-to-adopt attack
JOCR needs no optimisation (§4.2.1, App. G.2), which makes it a useful baseline for defenders.
### S4: Honest comparison to a hard baseline
CS-DJ, a strong recent method, is included (Table 4) rather than only weak baselines.

## Weaknesses
### W1: Novelty claim "first from a feature perspective" is not accurate as worded (C1, §1 contribution 1)
HiddenDetect (Jiang et al. 2025), which the paper itself cites for layer choice (§2.3), already studies VLM jailbreaks through hidden-state monitoring; the literature check also found *Internal Activation Revision* (arXiv 2501.16378, prior, arXiv-only), whose abstract reports that adding images shifts a VLM's internal activations and weakens safety, and *Eyes Closed, Safety On* (ECCV 2024) which analyses safety-mechanism failure for MLLMs. The decoupling premise of C2 comes from Zhao et al. 2025a (found: arXiv 2507.11878, a recent preprint, so it cannot be a required comparison and is cited by the paper). What is new is applying this lens to *OOD-shuffle attacks*; narrow the claim accordingly. Claim-level verdicts: C1 medium, C2 medium, C3 no close prior work found (arXiv only; at most medium), C4 incremental (closest: FigStep, level 4).
- **Suggested Fix**: Reword to "we analyse OOD attacks in latent space" and position against hidden-state analyses of VLM jailbreaks.
### W2: Citation errors that touch the paper's main baselines and arguments (E7)
(a) CS-DJ is attributed to "Jeong et al. (2025b)" (Table 1, §2.1, App. C), but the bibliography lists two *identical* "Playing the fool" entries (2025a/b), which is JOOD. The CS-DJ paper in the kept results is *Distraction is All You Need for Multimodal Large Language Model Jailbreaking* (Yang et al., CVPR 2025) and is not in the reference list. (b) "GPT-4.1 (Achiam et al., 2023)" (§2.2, App. C) cites the GPT-4 technical report. (c) The weak-alignment-generalisation argument in §4.1.3 cites "Liu et al. (2025)", the reference list's GeoShield, a geolocation-privacy paper by its title; App. F.3 even leaves the raw title in the sentence. I checked only the title, so I cannot say what that paper contains, but it is not a natural source for "small alignment datasets generalise weakly".
- **Suggested Fix**: Correct the CS-DJ entry; cite a source on alignment-data size and OOD generalisation (e.g., the safety-generalisation work already cited as Ren et al. 2024); fix the GPT-4.1 reference.
### W3: JOCR is FigStep with randomised typography; the delta against FigStep and against the OOD baselines is the actual contribution and is thin
§4.2.1 says the embedding step "is consistent with FigStep" and adds five random perturbations (Table 3). Table 5 shows FigStep-shuffle already adds +5 to +28 points over FigStep on HarmBench (e.g. GPT-4.1 24.50 → 52.50), so a large part of the gain is the generic effect of OOD-ing the typography; JOCR over FigStep-shuffle adds a further +13 to +24. SI-attack and JOOD, the attacks of §2–3, are not compared (App. C), and Visual Contextual Attack (Miao et al., found; prior) is a recent MM-SafetyBench-based attack that is not discussed.
- **Suggested Fix**: Add the closest typographic/OOD baselines (rendered-text adaptation of SI-attack/JOOD; FigStep with the same rewriting) and describe JOCR as FigStep + randomisation.
### W4: Related work is relegated to the appendix and omits the VLM hidden-state defense/analysis line
App. B lists attack papers only; there is no discussion of VLM safety analyses or safety fine-tuning for VLMs, which is what the "alignment generalises poorly" story (§4.1.3) needs to engage.
- **Suggested Fix**: Move a condensed related work to the main text; add the analysis and defense lines.

### Literature-check addendum (strict, cutoff 2025-09-24)
**Novelty delta (closest prior work):**
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|---|---|---|---|---|
| C1 weak-OOD | JOOD (Jeong et al., CVPR 2025; cosine 0.252, closest) | OOD strategy for MLLM jailbreak, hyperparameter α in Mixup | Systematic sweep across three attacks, non-monotonic ASR | Cited; sweep is new |
| C2 trade-off | Internal Activation Revision (arXiv 2501.16378) | Images shift VLM activations, weakening safety | Probes on shuffled inputs, refusal-vs-intent framing | Not cited |
| C3 attribution | none found (arXiv only) | – | Hypothesis | – |
| C4 JOCR | FigStep (AAAI 2025) | Typographic image prompts | Random font/space/colour/layout jitter | Cited; delta small |

**Per-claim novelty (script):** C1 medium, C2 medium, C3 no close prior work found (at most medium), C4 incremental; attribution: FigStep; paper reading: no central claim fully covered by prior work. **Worth discussing (not required, not a weakness):** *Towards Effective MLLM Jailbreaking Through Balanced On-Topicness and OOD-Intensity* (Li et al., arXiv 2508.09218, 2025-08-11), concurrent: it studies the balance between OOD intensity and on-topicness, close in spirit to C1/C2; *LLMs Encode Harmfulness and Refusal Separately* (Zhao et al., arXiv 2507.11878; already cited).
**Baseline scout:** partial (benchmarks MM-SafetyBench/HarmBench/RedTeam-2K; no `scout` table was produced; no under-reported baseline checked).
**Field snapshot (as of the cutoff):** three years ago VLM jailbreaks were dominated by white-box adversarial images; since 2023–2024 black-box typographic and role-play attacks (FigStep, MM-SafetyBench query-relevant images, Visual-RolePlay) reach high ASR on open models, and 2025 work targets closed models with OOD or distraction strategies (SI-attack, JOOD, CS-DJ). Defense and analysis work has moved to hidden-state monitoring and activation steering. A significant contribution now is either a defense-relevant mechanism supported by causal evidence, or an attack that survives guard models; "+5 ASR over CS-DJ" on a single judge is incremental. I used this to score Significance at the incremental end.

## Missing References
| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical (citation fix) | Z. Yang et al., "Distraction is All You Need for Multimodal Large Language Model Jailbreaking", CVPR 2025 (verified, arXiv 2502.10794) | The paper that CS-DJ actually refers to; currently mis-cited as Jeong et al. 2025b |
| Important | Y. Gou et al., "Eyes Closed, Safety On: Protecting Multimodal LLMs via Image-to-Text Transformation", ECCV 2024 (verified, arXiv 2403.09572) | Analysis of why visual input defeats LLM safety; positions the "feature perspective" claim |
| Important | Q. Li et al., "Internal Activation Revision: Safeguarding Vision Language Models Without Parameter Update", arXiv 2025 (verified, arXiv 2501.16378; arXiv-only, prior) | Activation shifts from images and safety; directly relevant to C1/C2 |
| Helpful | Z. Miao et al., "Visual Contextual Attack: Jailbreaking MLLMs with Image-Driven Context Injection", 2025 (verified, arXiv 2507.02844) | Recent MM-SafetyBench-based attack not compared |
| Helpful (concurrent) | Z. Li et al., "Towards Effective MLLM Jailbreaking Through Balanced On-Topicness and OOD-Intensity", arXiv 2025 (verified, arXiv 2508.09218) | Concurrent; worth discussing, not required |
| Helpful | Y. Zong et al., "Safety Fine-Tuning at (Almost) No Cost: A Baseline for Vision Large Language Models", ICML 2024 [verify] (not found on arXiv by title) | VLM safety fine-tuning data and generalisation; supports §4.1.3 |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Argument chain has untested links; citation errors |
| Clarity | 2 | Related work in appendix; positioning thin |
| Significance | 2 | Useful baseline, limited explanatory depth |
| Originality | 2 | Phenomenon moderately new; method incremental |

## Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the observation and attack are useful but incremental, and the overclaim of being "first" plus citation errors lower confidence in positioning.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Reasonable idea, uneven execution (see R1) |
| Clarity & Presentation | 55 | Competent | Story is followable |
| Novelty & Originality | 46 | Developing | C4 incremental, C1–C2 medium |
| Significance & Impact | 52 | Developing | Sub-area interest, defensive implications not shown |
| Experimental Validation | 50 | Developing | Several baselines, some missing |
| Reproducibility | 55 | Competent | Ranges listed |
| Ethical Compliance | 50 | Developing | Generic statement |

## Questions for Authors
1. How does the analysis differ from hidden-state analyses of VLM jailbreaks (HiddenDetect, Internal Activation Revision)? A concrete difference would restore the "first" claim to "first for OOD attacks".
2. Can CS-DJ be re-identified in the bibliography, and were the CS-DJ numbers in Table 4 produced with its official code?
3. Does JOCR retain its advantage over FigStep when FigStep receives the same question rewriting?

## Limitations Assessment
**Partially.** Related-work scope and baseline exclusions are not acknowledged.

## Ethics Review Flag
**No** from the domain side.

## Overall Score
**3**: A useful framing and a simple attack, but the claimed novelty is overstated and the positioning has gaps.

## Confidence
**4**: Checked the cited abstracts via search; did not review code.

---

# Peer Review Report (Reviewer 3)

## Paper: Why does Weak-OOD Help? A Further Step Towards Understanding Jailbreaking VLMs
## Reviewer: Dr. Mateo Salcedo, Perspective (security and HCI group, public university, South America; fictional persona)
## Expertise: content-moderation pipelines; applied security; usable red-teaming
## Date: 2026-11-05

## Summary
The paper studies why mildly distorted harmful images slip past VLM safety, argues that models still understand the harmful request while refusal behavior is brittle, and builds an attack that randomises text appearance in typographic prompts. For defenders, the message is that safety alignment covers a narrow region of the input space around standard presentations of harmful content.

## Strengths
### S1: A defender-relevant message
The refusal-versus-understanding asymmetry (Table 2) is a useful working hypothesis for safety data design: augment alignment data with visual-form variation (§4.1.3).
### S2: Connects to known robustness thinking
The inverted-U in perturbation strength resembles the classic "distribution-shift sweet spot" for robustness attacks and data augmentation, making the result interpretable to outsiders.
### S3: A cheap red-team baseline
JOCR needs no model access or optimisation (App. G.2), so safety teams can run it routinely.
### S4: Clear scope statement of the attack setting
Black-box, image + text, six deployed or open models (Table 4).

## Weaknesses
### W1: No defense-side experiment, although the conclusion claims to inform alignment
The Conclusion says the findings are "informing VLM safety alignment" but there is no test of a mitigation: for instance, safety fine-tuning with typographically-perturbed harmful images, an OCR-then-text-moderation guard in front of the model, or a hidden-state detector. Practical guards for typographic jailbreaks typically extract the text and moderate it; JOCR's random font size/spacing may or may not survive OCR, and whether it does is the deployment-relevant question.
- **Suggested Fix**: Evaluate JOCR against (i) an OCR + text-guard pipeline and (ii) a model fine-tuned on perturbed-typography refusals; report ASR before/after. Few GPU-hours with an open VLM.
### W2: Unexamined assumptions that decide external validity
(i) The latent analysis uses one 7B open model, but the conclusions are applied to closed models whose alignment pipeline is unknown (§3.2.3 vs §2.2). (ii) The harm of an "attack success" is judged by one LLM judge; a response flagged "unsafe" may be vague or off-topic. (iii) The premise that pre-training data contain many perturbed text-in-image samples (§4.1.2, "Text Variation Robustness") is not evidenced. Each can change the practical reading of the results.
- **Suggested Fix**: State these assumptions explicitly, add one more open model family, and sample 100 successes for manual harm assessment.
### W3: Dual-use and disclosure are not discussed; the Ethics Statement does not match the paper
The Ethics Statement says "the sole purpose of this research is to advance the development of web-based agent systems" and that no "ethically controversial" models were used, yet the paper evaluates attacks on deployed commercial systems (GPT-4o, GPT-4.1, Gemini 2.5 Pro) and releases an attack implementation (Reproducibility Statement). No vendor disclosure, mitigation or responsible-release discussion appears.
- **Suggested Fix**: Replace the statement with a dual-use discussion (what is released, harmful-content handling in examples, vendor notification, suggested mitigations).

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Some evidence, but applicability is not shown |
| Clarity | 3 | Understandable message |
| Significance | 3 | Defender-relevant, if validated |
| Originality | 2 | Interesting framing, simple method |

## Dimension Scores (0–100)
**Pool position:** better than about 47% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: relevant topic and a real phenomenon, but the defender-facing implications are asserted, not tested.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Sound idea, weak controls |
| Clarity & Presentation | 56 | Competent | Message clear |
| Novelty & Originality | 55 | Competent | New angle on a trending topic |
| Significance & Impact | 58 | Competent | Safety relevance |
| Experimental Validation | 50 | Developing | No defenses, one judge |
| Reproducibility | 56 | Competent | Ranges listed |
| Ethical Compliance | 42 | Developing | Mismatched ethics statement; no dual-use discussion |

## Questions for Authors
1. Does JOCR still succeed when the text is first extracted by OCR and moderated? Persistence of high ASR would raise my significance score; collapse would lower it.
2. Were harmful outputs in the Appendix examples handled under any release policy?
3. Would you share the model-version dates for API results?

## Limitations Assessment
**No.** There is no limitations section and the ethics statement is not specific.

## Ethics Review Flag
**Yes** (light-touch): dual-use of a stronger attack on deployed systems with a boilerplate ethics statement that names a different purpose ("web-based agent systems"); recommend an ethics read, not a block.

## Overall Score
**3**: Relevant and potentially useful for defenders, but implications and ethics handling are not at ICLR level yet.

## Confidence
**3**: Outside my core ML-interpretability expertise.

---

# Peer Review Report (Reviewer 4)

## Paper: Why does Weak-OOD Help? A Further Step Towards Understanding Jailbreaking VLMs
## Reviewer: Dr. Priya Raghunathan, Generalist (vision lab, large public university, South Asia; fictional persona)
## Expertise: vision-language models; typical PC member outside the safety niche
## Date: 2026-11-05

## Summary
The paper identifies an inverted-U between perturbation strength and jailbreak success for three OOD-style attacks, explains it as a trade-off between a model's understanding of harmful intent and its refusal, ties this to the gap between pre-training and alignment, and proposes JOCR, a typographic attack with random text styling that reports higher attack success than prior methods on six VLMs.

## Strengths
### S1: Compact, clear storyline
Observation (§2) → mechanism (§3) → method (§4) is easy to follow, and the contribution list (§1) maps onto sections.
### S2: Several kinds of evidence
Latent probes (Figs. 2–4), behavioral experiments (Table 2) and an attack evaluation (Tables 4–6) address different levels of the question.
### S3: Good venue topic
Safety of multimodal models is squarely in scope for ICLR; the question "why do OOD attacks work" is of interest to the community.
### S4: Reasonable table design
Tables 4 and 5 give the complete grid of models × baselines; appendix tables (7–9) give the numbers behind Fig. 1, which helps checking.

## Weaknesses
### W1: Abstract and conclusion outrun the evidence
"Theoretical argument for the inevitability" (Abstract) corresponds to definitions and asserted inequalities (App. E–F); "outperforms SOTA baselines in performance and efficiency" (Conclusion) is supported by ASR only (efficiency is a one-paragraph comparison in App. G.2 with no measured cost, and against SI-attack, which is not in Table 4); "informing VLM safety alignment" has no alignment experiment. I read these as claim-distortion issues that a revision can fix by rewording.
- **Suggested Fix**: Match each abstract sentence to a result, or soften; add a measured query/cost table.
### W2: Core definitions and cross-references are split between main text and appendix and inconsistent
§3.1 refers to "Eqs. 8-9" which are appendix equations (main text has Eqs. 1–2); the key assumption set (Eqs. 11–17) sits only in App. F; the JOCR description in §4.2.1 omits the question-rewriting step revealed in App. G.2 and the accompanying text prompt; Table 1's "Core Principle" column mixes descriptions of the attacks' motivations with claims; related work is only in App. B; Fig. 5's caption lists layers "18, 20, 23, 24, 25, 26" whereas the panels are labelled 18, 20, 22, 23, 24, 25; the text says JOCR is evaluated on "seven different models" (§4.2.2) but Table 4 lists six.
- **Suggested Fix**: Move the minimal definitions and the full JOCR pipeline into the main text; fix numbering and counts.
### W3: Missing limitations and an ethics statement that does not describe this paper
No Limitations section; the Ethics Statement states a purpose ("web-based agent systems") unrelated to this paper; the Reproducibility Statement cites "training hyperparameter settings" although nothing is trained.
- **Suggested Fix**: Add a Limitations paragraph and rewrite both statements for this work.

### ICLR criteria checklist
| Item | Status | Location |
|------|--------|----------|
| Claims supported by evidence | Partly: phenomenon yes; mechanism and "SOTA" partly | §2.2, §3.3, Table 4 |
| Soundness of methods | Partly: probe definitions inconsistent | §3.1–3.2 |
| Presentation/organisation | Partly | App. B, E, F |
| Reproducibility | Partly | App. C |
| Contribution/significance | Partly (incremental) | §4 |
| Limitations/ethics | Not met | Ethics Statement |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Mixed support |
| Clarity | 2 | Appendix-dependent, inconsistencies |
| Significance | 3 | Of interest to the safety audience |
| Originality | 2 | Incremental in method |

## Dimension Scores (0–100)
**Pool position:** better than about 44% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a readable, on-topic paper with real weaknesses that are more than typical (claims overshoot; inconsistent definitions).

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Mixed |
| Clarity & Presentation | 52 | Developing | Appendix dependence; inconsistent numbering |
| Novelty & Originality | 52 | Developing | New framing, incremental method |
| Significance & Impact | 55 | Competent | Relevant topic |
| Experimental Validation | 50 | Developing | Breadth good, controls thin |
| Reproducibility | 55 | Competent | Ranges listed; code not seen |
| Ethical Compliance | 50 | Developing | Boilerplate |

## Questions for Authors
1. Can the main text be reorganised so a reader can verify C2 without the appendix?
2. Which models make up the "seven" evaluated models?
3. Is there a measured cost comparison (queries, tokens, time) behind "efficiency"?

## Limitations Assessment
**No.** No limitations discussion.

## Ethics Review Flag
**No** (deferring to R3 on dual-use).

## Overall Score
**3**: A readable paper on a relevant topic with real gains in places, but the claims outrun the evidence.

## Confidence
**3**: Not a safety specialist.

---

# Devil's Advocate Report

## Paper: Why does Weak-OOD Help? A Further Step Towards Understanding Jailbreaking VLMs
## Reviewer: Dr. Elias Brandvold, evaluation methodology (research institute, Northern Europe; fictional persona)

## Steelman
Three independent OOD attacks show the same inverted-U, behavioral measurements on a deployed model show that harm understanding degrades slowly with shuffling while refusal collapses quickly, and a new attack designed to exploit that gap (OCR-robust randomised typography) beats the strongest baseline on most models. Together these make a coherent, partly validated story about why alignment fails off-distribution.

## Core Argument Chain
1. OOD attacks are effective only at mild perturbation (Fig. 1, Tables 7–9).
2. A jailbreak needs both intent retained and refusal reduced (Eqs. 1–2).
3. Latent and behavioral probes show refusal decays faster than intent (Figs. 3–4, Table 2).
4. Therefore the inverted-U arises from the trade-off between the two (C2).
5. Intent is acquired in pre-training and refusal in alignment, so the gap is the root cause (C3, §3.3, §4.1).
6. An attack that preserves OCR-readable intent while adding visual noise should therefore win (JOCR) and does (Table 4).
∴ The mechanism is validated, and JOCR is a better attack because of it.

## Strongest Counter-Argument
The argument contains a near-tautology and an inferential gap. Step 2 defines a successful jailbreak as "intent retained and refusal lowered" (Eqs. 1–2); so "success peaks where both are satisfied" follows from definition, and any attack with a tunable perturbation strength has an inverted-U because too much perturbation destroys the content. Showing that refusal falls faster than intent (Table 2) is informative, but it does not explain why the ASR *peaks and then falls*: Table 2's refusal rate keeps falling through Shuffle-25 (63.08%), so refusal alone would predict ASR rising monotonically, while the measured intent changes are small (Harm Accuracy 38.80% → 34.02%). No analysis ties these quantities to ASR sample by sample, and the probes use a different model (Qwen2.5-VL-7B, GPT-4o-mini) from the ASR curves (GPT-4o, GPT-4.1, Doubao).

The step from "better attack" to "mechanism validated" is also open. JOCR is FigStep (a typographic format known to bypass alignment) plus random styling (Tables 3, 5). A simpler alternative explanation is that typographic images with irregular styling lie outside the *format* distribution of safety data (a data-coverage story), with no reference to "preserved intent" at all. JOCR's intent preservation is never measured: there is no OCR accuracy on perturbed text, no harm-judgment probe on JOCR images, no refusal probe. The "pre-training vs alignment" attribution is never separated experimentally because all behavior is measured on aligned models. Finally, the claimed superiority over "SOTA" excludes the two attacks the paper analyses (SI-attack, JOOD), uses one GPT-4o judge that is also a target, and is contradicted in one of twelve cells (Table 4, GPT-4o on RedTeam-2K). If the authors cannot show JOCR's gains track the two measured factors, the mechanism claim reduces to "a typographic attack with random styling works well".

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The inverted-U for SI-attack on two targets is statistically solid, JOCR beats the best baseline in 11 of 12 cells, and the behavioral probes give partial support to a weaker version of C2; every problem below is fixable by narrowing claims or adding controls, and none is leakage, fabrication or a contradiction of the main observation.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic | Eqs. 1–2, §3.2–3.3 | Two-factor "trade-off" is partly definitional; refusal keeps falling to Shuffle-25 (Table 2) so the downturn in ASR (Table 7) isn't explained; no sample-level link | Per-sample regression; alternative explanation tests |
| DA-M2 | Evidence | §3.1 vs §3.2.1–3.2.2; Eqs. 3, 5 | Latent probes use swapped positions; intent probe is self-similarity; refusal probe dimensions inconsistent | Re-specify and control the probes (see R1-W1) |
| DA-M3 | Scope (E5) | Abstract; Conclusion; Table 4 caption | "first", "theoretical argument for inevitability", "outperforms SOTA ... efficiency", "over 10%" not supported as worded (4/12 cells; one cell reversed; no cost measured) | Reword; add CIs and cost table |
| DA-M4 | Evidence | §3.3; Table 2; §4.1 | Pre-training/alignment attribution untested (single aligned model; Exp 2 is aligned behavior; no alignment-stage comparison) | Base vs aligned comparison or label as hypothesis |
| DA-M5 | Evidence | App. C; Table 4; App. H | SI-attack/JOOD excluded; single judge (also target); ASR threshold unspecified; JOCR's rewriting step uncontrolled | Adapt/add baselines; second judge; ablate rewriting |
| DA-M6 | Evidence | Tables 8–9, §2.2 | "Universality" without zero-perturbation baselines for CS-DJ/JOOD; Doubao-1.6 effect within noise | Add baselines and CIs |
| DA-M7 | Ethics | Ethics Statement | Stated purpose does not match; no dual-use discussion | Rewrite |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Integrity of citations | Bibliography | Duplicate "Playing the fool" entries; CS-DJ missing; GPT-4.1 cited to GPT-4 report (see R2-W2) |
| DA-m2 | Presentation | Fig. 5 caption; §4.2.2 | Layer list vs panels; "seven models" vs six in Table 4 |
| DA-m3 | Numbers | Table 8 | Row "15" after "16"; Doubao 0.361 not a multiple of 1/200 |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| JOCR "over 10% ASR higher than baselines" (Table 4 caption) | >10% | Margin over best baseline (CS-DJ): RedTeam-2K +7.95, +19.00, −5.85, +4.75, +9.55, +0.85; HarmBench +16.50, +16.00, +2.50, +7.00, +13.50, +5.50; >10 in 4/12 cells; mean +8.10 | No |
| JOCR higher than "all baselines" (§4.2.2) | all | GPT-4o, RedTeam-2K: 31.65 vs 37.50 | No (one cell) |
| Intent robustness (Table 2), relative change at Shuffle-25 | "not affected" for mild | Intent sim −11.3%, Harm acc −12.3%, refusal −25.0%; at Shuffle-4: +0.3%, −3.0%, −12.6% | Qualitatively yes (mild), but all metrics decline monotonically |
| SI-attack gain, GPT-4o (Table 7) | 0.475 → 0.605 | +0.130, z ≈ 2.6 (n = 200, unpaired) | Yes (significant) |
| SI-attack gain, Doubao-1.6 (Table 7) | 0.575 → 0.620 | +0.045, z ≈ 0.9 | Not distinguishable from noise |
| Table 5 vs Table 4 FigStep and JOCR (HarmBench) | same values | Identical (49.50/42.50/19.00/35.00/24.50/23.00; 78.00/71.50/50.00/70.50/74.50/64.50) | Yes |
| Table 10 headline row vs Table 4 | 50.00/70.50/74.50 | (20,50),(30,50) row: 50.00/70.50/74.50 | Yes (same benchmark) |

## Ignored Alternative Explanations
- Format-coverage explanation: irregular typography simply lies outside the safety-training format distribution, independent of "intent preservation".
- Judge effects: GPT-4o judging GPT-4o outputs; "success" may include vague or off-topic answers.
- Selection of refused-only items (§3.2.3): conditioning on items Qwen refused biases both probes.
- Best-of-N in SI-attack (Table 1: toxicity-judge feedback; App. G.2: 20 shuffle attempts): if enabled in §2.2, the shuffle-count effect is entangled with selection by a judge.
- Longer or smaller text at high patch counts reduces legibility for OCR, a plain feature-destruction effect at the high end (not isolated by the PCA argument).

## Missing Stakeholder Perspectives
Defenders and model vendors (no mitigation evaluated or disclosure described); content-moderation practitioners (OCR-based guards); users of safety-critical VLM applications.

## Observations (Non-Defects)
The phenomenon for SI-attack is reproducible from the paper's own tables; the paper reports negative-looking numbers (JOCR below CS-DJ in a cell) in Table 4 rather than hiding them; Tables 7–9 give underlying numbers, which allowed the checks above; the analysis moves from latent to behavioral evidence, a good design direction.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 40 | Mis-specified probes, untested attribution |
| Clarity & Presentation | 54 | Readable; inconsistencies |
| Novelty & Originality | 45 | Framing + incremental method |
| Significance & Impact | 48 | Limited explanatory power |
| Experimental Validation | 40 | Excluded baselines, one judge, no CIs |
| Reproducibility | 52 | Ranges; missing judge threshold and rewriting model |
| Ethical Compliance | 45 | Mismatched statement |

**Pool position:** better than about 33% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the central explanatory claim is not tested by the reported measurements.

## Overall: 2 | Confidence: 4

---

# Phase 1.5/1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1–W6 | kept; W6 moved to lower severity | All specific, located, actionable; W6 is a protocol question not an error |
| R1 | Minor line (Eq. 2, Eqs. 8–9, JOOD 0.145) | kept as Minor / question | Cosmetic or low-confidence |
| R2 | W1 "first from feature perspective" | kept, rewritten to quote abstracts only | Novelty statements must match prior abstracts; IAR/ECSO stated from their abstracts via search |
| R2 | W2(c) GeoShield | rewritten as title-based observation | Abstract not checked; kept as medium-confidence |
| R2 | W4 related-work placement | moved to Minor-level | Presentation/placement |
| R3 | W1–W3 | kept | Specific and actionable; W3's quote verified in Ethics Statement |
| R4 | W2 | kept, trimmed | "seven" vs six models verified in §4.2.2/Table 4 |
| R4 | W3 | merged with R3-W3 in the master list | Duplicate |
| DA | M1–M7, m1–m3 | kept | M3 quotes verified; DA says "No CRITICAL" |

*Scores unchanged. No weakness was dropped as already answered by the appendix (the appendix was searched for each).*

# Phase 2: Synthesizer Package (Part A)

**Master issue list (classification):** I1 latent probes mismatched/unspecified (R1-W1, DA-M2) CONSENSUS-2 *(hinges)*; I2 trade-off not shown to explain ASR curve (R1-W2, DA-M1) CONSENSUS-2 *(hinges)*; I3 pre-training/alignment untested (R1-W3, DA-M4, R4-W1 in part) CONSENSUS-3 *(hinges)*; I4 SOTA/10% claim and baseline set/judge (R1-W4, DA-M3/M5, R2-W3, R4-W1) CONSENSUS-4 *(hinges)*; I5 universality and noise (R1-W5, DA-M6) CONSENSUS-2; I6 citation errors (R2-W2, DA-m1) CONSENSUS-2; I7 novelty/"first" (R2-W1) SOLO; I8 no defense experiment (R3-W1) SOLO; I9 ethics statement/dual-use (R3-W3, R4-W3, DA-M7) CONSENSUS-3; I10 structure/inconsistencies (R4-W2, R1 minor, DA-m2/m3) CONSENSUS-3. DA-CRITICAL: none. SPLIT: none (R3 more positive on significance, no explicit disagreement). Official output: see Score Summary (before.json: before composite 49.5, official mean rating 2.60).

# Phase 2: EIC Meta-Review

# Editorial Decision

## Paper: Why does Weak-OOD Help? A Further Step Towards Understanding Jailbreaking VLMs
## Submission ID: iclr26-gUw8n109ki
## Date: 2026-11-05
## Target Venue: ICLR | Paper Type: analysis
## Review Team (fictional personas): EIC Prof. Ingrid Valdemar; R1 Methodology Dr. Tomasz Reinholt, R2 Domain Prof. Adaeze Okonkwo-Brandt, R3 Perspective Dr. Mateo Salcedo, R4 Generalist Dr. Priya Raghunathan, DA Dr. Elias Brandvold

---

## Decision: Borderline Reject (3); ICLR rating 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}), scale status secondary

**Official ratings** (shown to authors): R1 2, R2 3, R3 3, R4 3, DA 2 → mean **2.60** · official composite **49.5**
**EIC assessment** (internal): weighted rating **2.51** → starting point **3** · weighted composite **49.0** → band 2 (cross-check) · **DA ceiling**: none · **Final (EIC)**: **3**

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A timely question on VLM jailbreaks with a statistically solid observation (SI-attack inverted-U on GPT-4o and GPT-4.1, Table 7), a behavioral experiment that points in the right direction (Table 2), and a simple attack that beats the strongest included baseline in 11 of 12 cells (Table 4). A defender-relevant message.
- **Against acceptance:** The title question ("why") is answered by probes that do not match the paper's own definitions (§3.1 vs §3.2), a two-factor account that is partly definitional and not tied to ASR, and a pre-training/alignment attribution that no experiment separates. The "outperforms SOTA" claim excludes the two analysed attacks, relies on one unvalidated judge, is reversed in one cell, and has no intervals. Citation errors on baselines and a boilerplate ethics statement add to the sense of an unfinished draft.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Intent/refusal positions swapped between §3.1 and §3.2 | R1-W1/ERR-1, DA-M2 | §3.1, §3.2.1, §3.2.2, Eqs. 3, 5 | Verified | Text states intent at t_post-inst and refusal at t_inst; metrics use the reverse |
| JOCR not best in every cell; ">10%" only in 4/12 | R1-W4/ERR-2, DA-M3 | Table 4, caption, §4.2.2 | Verified | GPT-4o RedTeam-2K 31.65 vs CS-DJ 37.50; cells >10 points: 19.00, 16.50, 16.00, 13.50 |
| Refusal falls monotonically to Shuffle-25 while ASR falls after patch 4 | R1-W2, DA-M1 | Table 2, Table 7 | Verified | 84.11→63.08% vs ASR 0.605→0.380 (different models) |
| Pre-training/alignment attribution untested | R1-W3, DA-M4 | §3.3, §4.1, App. E–F | Verified | All three experiments on GPT-4o-mini; Eqs. 11–17 asserted, not derived or measured |
| CS-DJ mis-cited as Jeong et al. 2025b (= JOOD) | R2-W2, DA-m1 | Table 1, §2.1, App. C; bibliography | Verified | Both Jeong entries identical; CS-DJ proper (Yang et al., CVPR 2025) absent |
| GeoShield cited for alignment weak generalisation | R2-W2(c) | §4.1.3, App. F.3 | Partly correct | Title-level observation; abstract not checked |
| "First ... from a feature perspective" overstated | R2-W1 | §1 | Partly correct | HiddenDetect is cited by the paper; the OOD-attack focus is new, so the claim is overstated rather than wrong |
| Trade-off is partly definitional | DA-M1 | Eqs. 1–2, §3.1 | Partly correct | Definitions make "both conditions" necessary, but Table 2's differential decay is non-trivial evidence |
| No zero-perturbation baseline for CS-DJ/JOOD | R1-W5, DA-M6 | Tables 8–9 | Verified | Lowest settings CSI = 3, α = 0.1 |
| Table 8 anomalies (row order; 0.361) | R1/ERR-4, DA-m3 | Table 8 | Partly correct | Row order verified; 0.361 vs n = 200 depends on unstated averaging |
| Ethics Statement names an unrelated purpose | R3-W3, R4-W3, DA-M7 | Ethics Statement | Verified | "the sole purpose ... web-based agent systems" |
| Judge is also a target; ASR threshold unstated | R1-W4(c), DA-M5 | §2.2, App. C, App. H, Table 4 | Verified | GPT-4o is both |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | Both MAJOR errors (ERR-1, ERR-2) verified at their locations; derived numbers hold; one minor point (0.361) rests on an assumption |
| R2 (Domain) | 3 | 4 | 1.0 | Citation findings verified; "first" point partly overstated; sound, typical review |
| R3 (Perspective) | 3 | 3 | 1.0 | Ethics-statement mismatch verified; defense-side points reasonable; lower confidence acknowledged |
| R4 (Generalist) | 3 | 3 | 1.0 | Cross-reference and "seven models" errors verified; claims-vs-evidence point sound |
| DA | 2 | 4 | 1.25 | Arguments largely survived checking (Table 4 recomputation, Table 2 vs Table 7, excluded baselines); correctly raised no CRITICAL; the "tautology" point is only partly correct |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | n/a | n/a |

### Final Decision and Justification
The EIC-weighted rating is 2.51 (official mean 2.60), giving a starting point of 3; the 0–100 composite (49.0) falls in band 2, one point from the band-3 edge (50), and the rating sits within 0.1 of 2.5, so the two signals are on a boundary and swap easily. I trust the rating, because the reviewers' Overall ratings already reflect the weak dimension scores, and I cannot name a verified issue the ratings overlooked that would justify going lower; the decisive points above were all accounted for in the reports. No upheld DA-CRITICAL issue exists, so there is no ceiling; the decision is 3. **My pool position: better than about 40% of ICLR submissions**, which is the typical-rejected range (30–54). The deciding evidence is that the paper's headline "why" is not measured by what it reports (swapped positions, untested attribution) and the headline attack claim is overstated, while the observation and attack are real but incremental. The paper would be a candidate for acceptance if a revision measured the mechanism at the sample level on one model, separated alignment from pre-training with a model pair, and brought the SOTA claim in line with Table 4 with intervals and a validated judge. This is a simulated panel view, not a prediction.

---

## Score Summary

### Official Scores and EIC Assessment

#### Reviewer weights (EIC, internal)
| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| R1 (Meth.) | 4 | 0.85 | 1.25 | 24% |
| R2 (Domain) | 4 | 0.85 | 1.00 | 19% |
| R3 (Persp.) | 3 | 0.70 | 1.00 | 16% |
| R4 (Gen.) | 3 | 0.70 | 1.00 | 16% |
| DA | 4 | 0.85 | 1.25 | 24% |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 42 | 50 | 52 | 50 | 40 | 46.8 | 45.9 | 12 |
| Clarity & Presentation | 52 | 55 | 56 | 52 | 54 | 53.8 | 53.7 | 4 |
| Novelty & Originality | 48 | 46 | 55 | 52 | 45 | 49.2 | 48.6 | 10 |
| Significance & Impact | 50 | 52 | 58 | 55 | 48 | 52.6 | 52.0 | 10 |
| Experimental Validation | 44 | 50 | 50 | 50 | 40 | 46.8 | 46.1 | 10 |
| Reproducibility | 52 | 55 | 56 | 55 | 52 | 54.0 | 53.7 | 4 |
| Ethical Compliance | 50 | 50 | 42 | 50 | 45 | 47.4 | 47.5 | 8 |
| **Composite** | 47.0 | 50.4 | 53.6 | 51.9 | 44.9 | **49.5 (before)** | **49.0 (after)** | |
| Pool position (P%) | 36 | 42 | 47 | 44 | 33 | | | |

No dimension spread exceeds 20 points.

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 2 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); both shown; internal Overall 3 (Borderline Reject) |
| Confidence | EIC-assessed 3–4 (reviewers 3–4) |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Why does Weak-OOD Help? A Further Step Towards Understanding Jailbreaking VLMs" to ICLR. The question of why mildly distorted harmful inputs defeat safety alignment in vision-language models is important, and we appreciate the effort to combine observation, analysis and a concrete attack.

**Overall Assessment:** Reviewers agreed that the inverted-U behavior of SI-attack is real and that JOCR is a simple, effective red-team baseline. They were not convinced that the paper establishes why the effect occurs, and found several claims worded more strongly than the evidence.

**Key Strengths Identified by Reviewers:**
1. A statistically solid inverted-U for SI-attack on GPT-4o and GPT-4.1 (R1-S1, DA Observations).
2. Behavioral experiments (Table 2) that point toward a faster decay of refusal than of intent understanding (R1-S2, R4-S2).
3. A simple, optimisation-free attack with broad model coverage and a strong baseline included (R1-S3, R2-S3/S4, R3-S3).

**Key Concerns Requiring Attention:**
1. The latent probes do not match the paper's own definitions (positions swapped between §3.1 and §3.2; self-similarity as "intent"), and nothing ties the two factors to attack success sample by sample (R1-W1/W2, DA-M1/M2; CONSENSUS-2).
2. The pre-training/alignment attribution is not tested; the "theoretical argument for inevitability" consists of assumptions (R1-W3, DA-M4, R4-W1; CONSENSUS-3).
3. "Outperforms SOTA": SI-attack/JOOD are not compared, JOCR is below CS-DJ in one cell and ">10%" holds in 4 of 12 cells, with one judge, no intervals, and an uncontrolled rewriting step (R1-W4, R2-W3, DA-M3/M5, R4-W1; CONSENSUS-4).
4. Citation errors (CS-DJ cited as the JOOD entry; GPT-4.1; GeoShield) and an ethics statement that names a different purpose and ignores dual-use (R2-W2, R3-W3, R4-W3; CONSENSUS-3).

The Devil's Advocate raised no CRITICAL issue.

**Decision: Borderline Reject (3)**

The ratings sit between reject and borderline; the verified problems concern the central explanatory claim and the strength of the headline comparison, which a revision can address with new experiments (sample-level analysis, a pre-/post-alignment model pair, validated judge, intervals). Please refer to the Revision Roadmap below.

Sincerely,
Prof. Ingrid Valdemar
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| SOTA / ">10%" claim, excluded baselines, judge protocol | R1, R2, R4, DA | CONSENSUS-4 |
| Pre-training/alignment attribution untested | R1, R4 (claims), DA | CONSENSUS-3 |
| Ethics statement / dual-use | R3, R4, DA | CONSENSUS-3 |
| Structure, cross-reference and count inconsistencies | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| How significant the contribution is | R3 (Significance 58, defender-relevant) | R1, DA (≈ 48–50) | Significance is real but untested on the defense side; EIC sides with the lower scores on explanatory value |
| Whether the trade-off is non-trivial | R1 (Table 2 is the strongest evidence) | DA (partly definitional) | Partly correct on both sides (see verification table) |

### Score Spread Discussion
No dimension flagged (all spreads ≤ 12).

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Trade-off partly definitional; no sample-level link | Yes (R1-W2) | n/a | n/a |
| DA-M3 | MAJOR | Claims outrun evidence (E5) | Yes (R1, R4) | n/a | n/a |
| DA-M4 | MAJOR | Attribution untested | Yes (R1-W3) | n/a | n/a |
| (CRITICAL) | – | None raised | – | – | – |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*Issues the EIC verified as undermining a main claim.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Probes inconsistent with definitions; intent measured as self-similarity; refusal metric dimensions | R1-W1, DA-M2 | §3.1, §3.2.1–3.2.2, Eqs. 3–6, App. E.1 | Re-specify positions; use probes/directions; add benign and random controls | Med; ≈ 10 GPU-h | Yes |
| R2 | Mechanism not linked to ASR | R1-W2, DA-M1 | §2.3, §3.2.3, Table 2, Fig. 4, Table 7 | Per-sample regression on one model; normalised comparison | Med; ≈ 20 GPU-h | Partly |
| R3 | Pre-training vs alignment attribution | R1-W3, DA-M4, R4-W1 | §3.3, §4.1, App. E–F, Abstract | Base vs aligned model pair; otherwise soften "inevitability" | High; ≈ 50 GPU-h | No |
| R4 | SOTA claim, excluded baselines, judge | R1-W4, R2-W3, DA-M3/M5 | Table 4, App. C, App. H, Conclusion | Adapt SI-attack/JOOD; CIs; human-validated second judge; ablate rewriting; reword claim | High; ≈ 60 GPU-eq. API | Partly |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | "Universality" without zero baselines; noise | R1-W5, DA-M6 | Add baselines, error bars | Med | Yes |
| S2 | Citation errors (CS-DJ, GPT-4.1, GeoShield) | R2-W2, DA-m1 | Correct entries; cite Yang et al. (CVPR 2025) | Low | Yes |
| S3 | "First from a feature perspective" | R2-W1 | Reword; cite Eyes Closed, Safety On; Internal Activation Revision; discuss concurrent Li et al. | Low | Yes |
| S4 | No defense-side experiment | R3-W1 | OCR + text-guard; safety fine-tuning test | Med | Partly |
| S5 | Ethics statement / dual-use | R3-W3, R4-W3, DA-M7 | Rewrite; disclosure plan | Low | Yes |
| S6 | JOCR ablation protocol (same benchmark) and over-read differences | R1-W6 | Fix config on a separate split | Med | Partly |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Related work in appendix; add VLM analysis/defense lines | R2-W4 | Move/condense |
| N2 | Cross-reference/numbering issues (Eqs. 8–9, Fig. 5 caption, "seven models", Table 8 labels, Eq. 2 wording) | R1, R4, DA-m2/m3 | Fix |
| N3 | Efficiency claim without measured cost | R4-W1 | Add cost table |
| N4 | Limitations section | R1, R4 | Add |

## Estimated Revision Effort
- Priority 1: 4 items, ≈ 3–5 weeks (≈ 150 GPU-hours plus API cost)
- Priority 2: 6 items, ≈ 1–2 weeks
- Priority 3: 4 items, ≈ 1–2 days
- **Total estimated revision time**: ≈ 5–7 weeks

---
*Journal mapping not applicable (conference target). Literature-check mode: strict, cutoff 2025-09-24. The simulation reflects how a careful panel would likely see this draft; it makes no promise about any real decision.*
