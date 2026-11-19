# Simulated Panel Review: "Debiasing CLIP: Interpreting and Correcting Bias in Attention Heads"

Date: 2026-11-10 · Mode: full · Target venue: ICLR (stated) · Literature check: strict, cutoff 2025-09-24 · Confirmation skipped (as requested)

*Simulation, not a prediction: this is how a careful panel might see this draft. Figures were not available (text extraction only); figure-dependent claims (Figs. 1–4, 10, 11, 21–28) are judged from captions and surrounding text only and are marked "unverifiable" where it matters. All five reviewer passes share one model context; they were performed one after another and each was written from its own role file without reading the other reports. The integrity scan found no reviewer-directed text; the paper has no appendix reference to missing supplementary files.*

---

# Phase 0: Paper Analysis and Reviewer Configuration Card

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Debiasing CLIP: Interpreting and Correcting Bias in Attention Heads |
| Primary Discipline | Machine learning → robustness / fairness of vision-language models |
| Secondary Discipline(s) | Mechanistic interpretability of vision transformers; spurious-correlation / group robustness |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | Residual-stream decomposition of CLIP ViT into per-head states, logit-lens attribution, contrastive head selection (correctly vs. wrongly classified minority-group samples), mean ablation, LLM-derived orthogonal "knowledge injection" |
| Target Venue | ICLR (stated by user); profile key `iclr` (ICLR 2026 cycle, scale status: secondary) |
| Venue-Specific Notes | None. Submission is an anonymized preprint ("Preprint. Under review."); pool base rate ≈ 27% accepted |
| Paper Maturity | Submission-ready, with visible polish gaps (table/figure cross-reference slips, notation drift) |
| Ethics-Relevant Content | Gender-bias evaluation on synthetic occupation images (GenderBias-VL) and face images (FairFace); binary gender only; web-derived models; LLM (GPT-4o) use for feature generation |
| Integrity scan | `integrity_scan.py`: no reviewer-directed text or hidden characters found. Reviewers read the (unchanged) reviewer copy |

### Claimed Contributions (as stated by the authors)
1. **C1** (method, Abstract, §4.2): LTC, a contrastive procedure that automatically identifies spurious and class-salient attention heads in CLIP's ViT, replacing manual head interpretation (Gandelsman et al. 2023).
2. **C2** (method + result, Abstract, §4.3, §5.1): Targeted correction, i.e. mean ablation of spurious heads and orthogonal-projection "knowledge injection" on target heads, giving "over a > 50% gain in worst-group accuracy compared to non-training post-hoc baselines" on background and gender bias benchmarks.
3. **C3** (result, §5.1, Table 1): LTC also works as a lightweight extension to parameter-tuning methods (JTT-LTC beats Contrastive Adapters and JTT on Waterbirds).
4. **C4** (analysis, §6, App. D): The visualized/SHAP-interpreted heads "corroborate" the contrastive mechanism and give "significantly greater interpretability than existing methods" (§1).

### Paper memory (factual record shared with all reviewers)
- **Setup facts:** OpenCLIP ViT-B/16, L/14, H/14 ("We evaluate on OpenCLIP", §5.1; pretrained checkpoint/data not stated). Template "A photo of a [class]" (App. A.1). Waterbirds: "validation" 4,795 images (|G_N| = 240), test 5,794 (|G_N| = 2,897) (Table 4; the 4,795/240 figures coincide with the original Waterbirds *train* split; inference, not stated). CounterAnimal: 45 classes inside 1,000-way ImageNet classification, easy subset D_E used for mapping, hard subset D_H (5,926) evaluated (App. A.1, Table 4). GenderBias-VL: 25 occupations for optimization, 152 for evaluation (§5.1); bias via BLS-derived stereotype labels (App. A.1). FairFace: 10,954 images, heads reused from GenderBias without tuning (App. A.1). Compute: single A100 80GB (App. E). Seeds / runs: single deterministic pass per configuration; only Table 9 varies the LLM feature set (3 sets). γ is a fixed heuristic, "no cross-validation" (§5.2). Layers considered: last 4 (B, L) or last 8 (H) layers (captions of Figs. 12–20). N_u (number of LLM features): "3" for GenderBias/CounterAnimal prompts (Table 5), not stated for Waterbirds. GPT-4o version/date/decoding: not stated.
- **Headline numbers:** Abstract ">50% gain in worst-group accuracy" ← Table 1 (Waterbirds WG: ZS 49.7/44.5/50.3 → LTC 73.3/74.6/71.3 for B/L/H). Table 2 (GenderBias bias metrics), Table 3 (FairFace MaxSkew), Table 6/7 (ablations).
- **Appendix adds:** dataset sizes (Table 4), CounterAnimal pairing dictionary, baseline descriptions (A.2), JTT hyperparameters (λ_up, lr, hidden size), per-head contribution heatmaps (App. C, figures unavailable), SHAP/TextSpan interpretation tables (App. D), sample-size and mask sensitivity (B.3), full-vs-negative-group locating (B.4, Table 8), prompt-set sensitivity (B.5, Table 9), compute (E), societal impact (F).
- **Unverifiable:** all figures (Figs. 1–4, 5–11, 12–28), bold/underline in tables, Eq. 7/10 typesetting (garbled by extraction; treated as unverifiable except where the surrounding prose is explicit).

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Dr. Marguerite Okonjo-Lindqvist, area-chair profile, large public research university (Europe)
- **Seniority / Expertise**: Senior faculty / robust and fair representation learning, vision-language models
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style**: Judges against what ICLR actually accepts; allergic to both overclaiming and review inflation

### Reviewer 1 (Methodology): Dr. Anselm Kowarik, mid-career, industrial research lab (Central Europe)
- **Seniority / Expertise**: Mid-career / group-robustness evaluation protocols, zero-shot CLIP evaluation, intervention experiments
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Recomputes every table; insists on matched supervision across baselines

### Reviewer 2 (Domain): Dr. Leocadia Mbeki-Strand, senior faculty, public research university (Southern Africa)
- **Seniority / Expertise**: Senior faculty / mechanistic interpretability of vision transformers; concept erasure and projection-based debiasing
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Wants a one-sentence delta against the closest prior work

### Reviewer 3 (Perspective): Dr. Joaquín Ferreyra-Holm, mid-career, social-computing / algorithmic-fairness group (Latin America)
- **Seniority / Expertise**: Mid-career / fairness auditing, causal mediation analysis, measurement validity of bias metrics
- **Review Focus**: Cross-disciplinary connections, deployment, assumptions, broader impact
- **Style**: Constructive; asks what the metric actually measures

### Reviewer 4 (Generalist): Dr. Sun-hee Ostrowska, senior industry scientist, applied vision team (East Asia)
- **Seniority / Expertise**: Senior industry scientist / multimodal learning, general ML program-committee member
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Reads like a typical PC member; weighs weaknesses against what accepted papers carry

### Devil's Advocate: Dr. Beatrix Nakamura-Cole, mid-career, evaluation-methodology lab (North America)
- **Seniority / Expertise**: Mid-career / evaluation methodology, causal inference for ML, fairness and robustness claims
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Steelmans first; attacks the inference, not the authors

---
*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Independent Reviews

---

# Peer Review Report

## Paper: Debiasing CLIP: Interpreting and Correcting Bias in Attention Heads
## Reviewer: Dr. Anselm Kowarik, Methodology Reviewer (industrial research lab, Central Europe; fictional persona)
## Expertise: Group-robustness evaluation, zero-shot CLIP protocols, intervention experiments
## Date: 2026-11-10

---

## Summary
The paper decomposes CLIP's ViT image representation into per-head contributions, finds heads that mostly carry the spurious attribute (S) or class evidence (Y) by contrasting head attributions on wrongly vs. correctly classified minority-group samples (Eq. 10), mean-ablates the former and adds an LLM-derived discriminative direction to the latter (Alg. 1). It reports gains on Waterbirds, CounterAnimal and GenderBias-VL/FairFace over three training-free baselines (Tables 1–3), an extension on top of JTT, ablations (Tables 6–7), and SHAP/text interpretations of the selected heads (§6, App. D).

## Strengths

### S1: Informative ablation design
Table 6/7 separate mean ablation (LTC (MA)), knowledge injection alone (LTC (KI)), random head selection (LTC (R)) and Roboshot's injection alone (RS (KI)). LTC (R) is below zero-shot on Waterbirds (e.g., WG 36.9 vs 49.7 for ViT-B), which shows head choice matters; LTC (KI) vs RS (KI) isolates "where" the projection is applied.

### S2: Protocol separation between locating and evaluation on Waterbirds
Heads are located on a "validation" split and evaluated on the standard test split (Table 4), and GenderBias uses 25 occupations for optimization vs. 152 for evaluation (§5.1). I found no statement that any reported configuration was selected on the reported test split (protocol sweep below).

### S3: Honest sensitivity analyses in the appendix
B.3 (sample size, single-state variant), B.4 (locating on all data instead of G_N, Table 8) and B.5 (three LLM feature sets, Table 9) report cases where the method is fragile (ViT-B collapses when locating on the full data; Table 8 WG 15).

## Protocol sweep (Step 0)
Searches for split/selection statements found: "Note that we only assume access to ground truth group labels for the validation set, following Cont Adapter" (§5.1); "we do not perform any cross-validation to optimize" γ (§5.2); GenderBias "We randomly select 25 occupations for optimization and evaluate on the remaining 152" (§5.1); the top-10 biased occupations are chosen "via zero-shot inference of the respective model" (Table 2 caption) and the 10 worst occupations of the validation set are used for optimization (App. A.1). CounterAnimal: mapping ȳ:y "using D_E" and the same settings applied to baselines (§5.1, App. A.1). **Not stated after search:** which split JTT/ERM hyperparameters (λ_up = 90/100, lr, hidden size) were tuned on; how the number of last layers (4 vs 8) was chosen; whether the mean in mean-ablation is computed on the evaluation set (Alg. 1, "sample-independent … across the full inference dataset"); the OpenCLIP pretrained checkpoint; the GPT-4o version and decoding.

## Claim-to-evidence map

| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | Automatic, contrastive identification of S and Y heads | Abstract, §4.2 | Eq. 10, Tables 6–8, Figs. 10–11 (unavailable), App. C | Partially: downstream gains support that selected heads matter; the derivation in §4.2 is internally inconsistent (ERR-2) and head labels (Z_S vs Z_SY) drift |
| C2 | ">50% gain in worst-group accuracy vs non-training post-hoc baselines" | Abstract | Table 1 | **Partially / overstated**: holds only vs zero-shot; vs best baseline +7.6%, +1.8%, +17.5% (ERR-1) |
| C2b | "LTC surpasses all non-tuning baselines, bridging both the gap between groups and overall performance" | §5.1 | Table 1 | Partially: ViT-L Gap 9.4 vs Ortho-Cali 5.3 and Roboshot 8.5 |
| C2c | Effective for gender bias in classification and retrieval | §5.1, Tables 2–3 | Tables 2, 3, 7 | Partially: BO is not best for ViT-L/H; Table 3 ties TextSpan/loses to Ortho-Cali |
| C3 | JTT-LTC is an effective extension to tuning methods | §5.1 | Table 1 lower block | Partially: single run, margins 1.6–5.9 pts vs Cont Adapter, tuning/selection of baselines not stated |
| C4 | Interpretation "corroborates" the contrastive mechanism | Abstract, §6 | Fig. 3, Tables 11–20 | Weak: selection criterion makes the SHAP outcome largely expected; figures unverifiable |

## Weaknesses

### W1: Headline claim and results narrative overstate the gain over baselines (E1/E5)
Abstract: "achieving over a > 50% gain in worst-group accuracy compared to non-training post-hoc baselines". From Table 1 (Waterbirds WG), relative gain over ZS is +47.5%, +67.6%, +41.7% (B/L/H), but those are gains over the *unmodified model*. Against the strongest non-tuning baseline the gains are 73.3 vs 68.1 (+7.6%), 74.6 vs 73.3 (+1.8%), 71.3 vs 60.7 (+17.5%); averaged over the three sizes, 73.07 vs 67.37 (+8.5%). The only comparison that exceeds 50% against a post-hoc *method* is ViT-H vs Ortho-Cali (18.1, see W2). The text "LTC surpasses all non-tuning baselines, bridging both the gap between groups and overall performance" (§5.1) also fails for ViT-L Gap (LTC 9.4 vs Ortho-Cali 5.3, Roboshot 8.5) and ViT-B Gap vs LTC-Ŝ/Roboshot.
- **Suggested Fix:** Restate the abstract against the best baseline per backbone (or "relative to zero-shot"), and qualify §5.1. Zero cost.

### W2: Baseline comparison is not like-for-like in supervision, and one baseline looks broken (E4)
LTC's locating step needs labeled data with spurious-attribute annotation ("we only assume access to ground truth group labels for the validation set", §5.1), while TextSpan and Roboshot use none (§5.1, A.2) and Ortho-Cali needs a spurious-attribute prompt set plus a validation-derived projection (A.2). The authors acknowledge this with LTC-Ŝ (predicted group labels), but LTC-Ŝ is the fair row, and there ViT-B (WG 61.8) is below Ortho-Cali (68.1), and ViT-L (75.5 vs 73.3, +2.2 pts) is within the single-run noise (W4). In addition, Table 1 reports Ortho-Cali on ViT-H as WG 18.1 / Avg 41.9, below zero-shot (50.3/69.5) and below chance accuracy for a binary task, without explanation; Roboshot ViT-B Avg 63.0 vs ZS 72.1 is also a large degradation. Since ViT-H is the model where LTC's relative gain is largest, an unexplained collapsed baseline matters. The text claims "Ortho-Cali consistently underperforms" (§5.1), which Table 1 contradicts for ViT-B/L, where it is the strongest baseline.
- **Suggested Fix:** (i) Add a supervised, equal-label-budget baseline using the same group-labeled validation set (e.g., group-balanced last-layer re-training; Kirichenko et al., ICLR 2023, verified link below) and report it next to LTC; (ii) debug/explain Ortho-Cali ViT-H and state whether baseline numbers come from official code or re-implementation; (iii) correct the "consistently underperforms" sentence. ~1 GPU-day.

### W3: GenderBias "worst-group" metric is selected on the evaluation outcome; overall-bias and accuracy are not reported (E4/E8)
BT is "the 10 occupations with the highest discrepancy in classification between genders, chosen via zero-shot inference of the respective model" (Table 2 caption), and App. A.1 states "we select the 10 occupations with highest bias scores during zero-shot inference" (the text is ambiguous on whether those 10 come from the 152 evaluation occupations or from the 25 optimization ones; App. A.1 says the 10 worst in the *validation* set are used for optimization). If the evaluation set's top-10 are selected on zero-shot bias, any perturbation, including random head selection, regresses toward the mean. Table 7 is consistent with this: LTC (R) cuts B10 from 74.0→30.5 (B), 54.7→35.3 (L), 67.7→33.4 (H), i.e. 43.5, 19.4, 34.3 points, while its overall bias B_ovl is unchanged or worse (16.3→12.2, 12.9→14.6, 15.2→15.0). On the metric that is not selection-biased (BO, Table 2), LTC is best only for ViT-B (9.4 vs Ortho-Cali 10.2); for ViT-L (9.8 vs 9.2) and ViT-H (10.1 vs 9.4) Ortho-Cali is lower. The text's "Ortho-Cali performs comparably to LTC, except on ViT-B" (§5.1) understates this. Further, Tables 2/3/7 report only *gap* metrics: a method can lower the gender gap by lowering accuracy for the advantaged group ("leveling down"); occupation accuracy and retrieval recall are never shown.
- **Suggested Fix:** Select the top-10 occupations on a held-out split (or report all 152 sorted by ZS bias with a regression-to-mean control, e.g., random-edit baselines on BT), report per-gender accuracy and overall accuracy, and report retrieval relevance next to MaxSkew. ≈ 2–3 GPU-hours.

### W4: No variance or significance reporting for small margins (E8)
Every Table 1–3, 6, 7 entry is a single deterministic pass; only Table 9 varies something (LLM feature sets), and there the spread is as large as the gap to the baseline for ViT-H (LTC 66.7 ± 5.5 vs RS 59.5 ± 6.2) and ViT-L (74.4 ± 2.9 vs 68.8 ± 4.2). Table 1's main LTC numbers (71.3 for ViT-H) sit above that mean (66.7), so the reported row may be a favorable feature set; which set the main table uses is not stated. For Waterbirds, if the worst group is the 642-image waterbird-on-land group of the standard test split (my recollection of the split, not stated in the paper), the binomial standard error at 73% is ≈ 1.75 points (derived), so LTC vs Ortho-Cali on ViT-L (74.6 vs 73.3) is not distinguishable. On CounterAnimal, LTC's gains over ZS are +0.4, +0.2, +1.1 points on 5,926 images (SE of the accuracy ≈ 0.65 points, derived), yet the text says LTC "is the only method that consistently improves over zero-shot CLIP" (§5.1).
- **Suggested Fix:** Bootstrap 95% CIs over test images (paired against ZS and the best baseline), report which feature set the main table uses and the mean ± std over the three sets for all rows, and soften the CounterAnimal claim. Negligible compute.

### W5: Method description has an internal inconsistency in the key derivation (E2/E6)
§4.1 states that V is "averaged over D and normalized such that the total contributions sums to 1" after the one-hot encoding of Eq. 7, which makes V a non-negative histogram of "which head is top contributor". §4.2 then argues from signs: "VN W < 0" and "VN C > 0" (as extracted), and that Eq. 10 "isolates the positive VS terms while filtering out the negative VY terms". A non-negative normalized histogram cannot be negative, so the sign argument and the normalization argument cannot both apply. The paper's own text also changes what "spurious head" means: §6 says the heads found by Eq. 10 encode the S–Y *association* (Z_SY), not S (Z_S), and App. B.3 refers to "Z_Y and Z_SY", while §4.3/Alg. 1 and Table 1 captions speak of Z_S. (Equation typesetting is garbled in extraction, so I rate this Medium confidence and ask for clarification.)
- **Suggested Fix:** State exactly what is thresholded (signed logit differences vs. one-hot frequencies), give a small worked example with numbers, and use Z_SY consistently when that is what is ablated.

### W6: Generality claims rest on a narrow setting (E5)
Backbones are OpenCLIP ViTs only, with the pretrained checkpoint unspecified (E8); Waterbirds is the only binary background benchmark; CounterAnimal results are marginal; gender is binary and evaluated on synthetic images plus FairFace (the race/age attributes in FairFace are unused). Heads, layers and the mean/KI vectors are located per dataset, so the result is a dataset-specific edit rather than a "debiased CLIP". The effect on general zero-shot performance (e.g., ImageNet accuracy) is not reported. CelebA is dropped because "we do not find significant bias present in zero-shot CLIP" (§5.1), which is a reasonable but non-verifiable choice.
- **Suggested Fix:** Add one more standard spurious-correlation benchmark used by the baselines (the Roboshot paper also reports PACS/VLCS-style shifts, per my recollection of that paper), report ImageNet zero-shot accuracy before/after, and state the exact OpenCLIP checkpoints.

### Error Log

| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1/E5 | Abstract vs Table 1 | "achieving over a > 50% gain in worst-group accuracy compared to non-training post-hoc baselines" | Gain vs best post-hoc baseline is +7.6%/+1.8%/+17.5% (B/L/H); >50% only vs zero-shot (ViT-L +67.6%) | Recomputed from Table 1 | High | MAJOR | Reword |
| ERR-2 | E2/E6 | §4.1 vs §4.2 | "normalized such that the total contributions sums to 1" | Normalized non-negative V cannot satisfy "VNW < 0" used in the Eq. 10 argument | Cross-referenced (two locations), equations partly garbled | Medium | MAJOR (clarity of method) | Clarify |
| ERR-3 | E1/E5 | §5.1 vs Table 1 | "Ortho-Cali consistently underperforms" | Ortho-Cali WG 68.1 and 73.3 on ViT-B/L, the strongest baseline (ViT-H 18.1 is the outlier) | Table 1 read | High | MAJOR | Correct |
| ERR-4 | E1 | Table 1 vs Table 6 vs Table 9 | LTC ViT-L/14 Gap: 9.4 (Table 1), 9.6 (Table 6) | Same configuration, different Gap; Avg−WG = 84.1−74.6 = 9.5 | Recomputed | High | MINOR | Reconcile |
| ERR-5 | E6 | §6 vs App. D | "we use GPT4-o to generate"; "we prompt MiniCPM-V 2.6" | Captioner for SHAP is GPT-4o in §6, Table 10 caption "using GPT4o", but MiniCPM-V 2.6 in App. D text | Cross-referenced | High | MINOR | State which was used |
| ERR-6 | E6 | §5.2 vs Limitations | "without tuning the masking threshold" | Threshold is called γ in §4.2/§5.2, λ in Limitations; λ_up is JTT's upsampling factor | Cross-referenced | High | MINOR | Rename |

**Minor:** B.5 cites "Tab. 10" for Table 9; Table 9 row says "ViT-L/16" (model is L/14); "Waterbird:" heading in A.1; Table 10 caption vs text on captioner (ERR-5); CounterAnimal "Gap" equals (fixed easy-subset accuracy − Avg) for every row (e.g., 54.8+21.1 = 75.9 = 52.6+23.3), so it carries no information beyond Avg.

## Missing References
Deferred to the Domain Reviewer; for baselines I ask for: Kirichenko, Izmailov, Wilson, "Last Layer Re-Training is Sufficient for Robustness to Spurious Correlations" (ICLR 2023; verified, https://arxiv.org/abs/2204.02937v2).

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Informative ablations, but baseline supervision mismatch, selection-prone gender metric, no variance |
| Clarity | 2 | Key derivation inconsistent; cross-reference slips |
| Significance | 2 | Useful if robust, but dataset-specific edits with modest margins over best baselines |
| Originality | 2 | Head-level application of known projection ideas with a new head-selection rule |

## Dimension Scores (0–100)

**Pool position:** better than about 48% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline is stated against the weakest comparison, the baselines differ in supervision and one is unexplained-broken, and the gender metric is selected on the outcome; the ablation design and honest sensitivity appendix keep it out of the bottom half.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | ERR-2 derivation inconsistency; selection-prone BT; no controls for label usage |
| Clarity & Presentation | 56 | Competent | Readable but notation/figure-table cross-reference drift |
| Novelty & Originality | 54 | Competent | Moderate; see R2 |
| Significance & Impact | 52 | Developing | Gains over strongest baseline small on 2 of 3 backbones |
| Experimental Validation | 46 | Developing | Single runs; baseline mismatch; CounterAnimal within noise; no accuracy next to gap metrics |
| Reproducibility | 50 | Developing | Code "available" (link removed) but checkpoint, GPT-4o version, N_u (Waterbirds), layer-range selection missing |
| Ethical Compliance | 62 | Competent | Societal-impact paragraph exists; binary gender, no leveling-down check |

## Questions for Authors
1. Which split are the top-10 occupations for BT/MT chosen from, and what does a random head-edit baseline give on BT with the BT set fixed before editing? (An answer showing LTC (R) does not move BT would raise my score.)
2. Is the mean in mean-ablation computed on the evaluation set (Alg. 1)? If yes, does the result hold with the validation-set mean?
3. How were λ_up and the probe settings of JTT/ERM chosen, and are baseline numbers from official code?
4. Which feature set generated the main-table LTC rows, and what are the mean ± std for every row?
5. Why does Ortho-Cali on ViT-H collapse below chance (Table 1)?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially. The Limitations paragraph mentions threshold sub-optimality and CLIP-only scope but omits the label requirement, dataset-specific editing, and the gap-only evaluation.

## Ethics Review Flag
**No.**

## Overall Score
**3**: Sound idea with useful ablations, but the headline gain is stated against the weakest comparison and the evidence for the claimed advantage over label-aware or properly tuned baselines is not yet clean.

## Confidence
**4**: Tables recomputed; figures unavailable; equations partly garbled.

---

# Peer Review Report

## Paper: Debiasing CLIP: Interpreting and Correcting Bias in Attention Heads
## Reviewer: Dr. Leocadia Mbeki-Strand, Domain Reviewer (public research university, Southern Africa; fictional persona)
## Expertise: Mechanistic interpretability of vision transformers; concept erasure and projection-based debiasing
## Date: 2026-11-10

---

## Summary
The submission builds on head-level text-grounding of CLIP (TextSpan) and on projection-based zero-shot debiasing (Roboshot, Ortho-Cali) and combines them: instead of manual interpretation, a contrastive rule over correct/incorrect minority-group samples picks heads; spurious heads are mean-ablated and class heads receive an LLM-derived orthogonal projection. The claimed gain is better worst-group accuracy than projection on the whole embedding, with "interpretability" as a by-product.

## Strengths

### S1: Clear gap relative to TextSpan
The introduction identifies the "extensive manual effort in summarizing the representation" of TextSpan as the problem (§1), and Table 13/17 (TextSpan applied to the located states) and Table 3 (LTC (MA) matches TextSpan's FairFace numbers on ViT-B/L: 16.8, 26.2) give evidence that the automatic rule finds similar heads.

### S2: Localization of the correction is tested
RS (KI) vs LTC (KI) (Tables 6, 7) is a good isolating comparison for "same LLM features, different place of projection", and the single-top-state variant (App. B.3) shows how few heads suffice.

### S3: Unusual interpretation of what is found
§6 and Fig. 4 report that the contrastive rule finds the head encoding the S–Y association (Z_SY) and not the attribute itself (Z_S). If the figure supports this (unverifiable here), it is a more interesting finding than the debiasing numbers.

## Weaknesses

### W1: Positioning against the closest head-level work is thin, and head-level CLIP bias work is missing
Related work (§2) treats only Gandelsman et al. [2023] and Jiang et al. [2024] on heads, and describes debiasing as "no explainable insights as to why these methods work" (§2). The literature check (strict, cutoff 2025-09-24) surfaced three prior works that sit close to this one: (a) a study of CLIP attention-head *pruning* that links the most informative heads to bias amplification (Madasu, Lal, Howard, 2025, arXiv; prior, arXiv-only; https://arxiv.org/abs/2503.11103v3); (b) the general automated decomposition of ViT components into text-interpretable roles (Balasubramanian, Basu, Feizi, NeurIPS 2024; https://arxiv.org/abs/2406.01583v2); and (c) a recent projection-based debiasing method that also uses LLM-generated scene descriptions of spurious correlations (Molahasani et al., PRISM, ICCV 2025; https://arxiv.org/abs/2507.08979v1). Only (a) shares the head-level intervention; none is fatal to novelty, but each should be cited and a delta stated. Why it matters: the paper's novelty is the head-level application, so closest head-level prior work defines the bar.
- **Suggested Fix:** Add a related-work paragraph and a delta table; compare against (c) if code is available.

### W2: The contribution is a composition of known operators with a heuristic selection rule
Mean ablation (Nanda et al. 2023, cited), logit lens (cited), orthogonal projection toward LLM-derived discriminative vectors (the Roboshot recipe: "We follow the same strategy in Adila et al. [2023]", §4.3) are all established. The new element is Eq. 10's head selection plus a threshold γ chosen heuristically. Its derivation is ambiguous (see R1-W5) and "we do not perform any cross-validation to optimize" γ (§5.2). Per-claim novelty: C1 medium (head-level selection by contrast is new relative to manual TextSpan, but the selection logic is a heuristic), C2 incremental (projection recipe reused; head-level location is the delta), C3 incremental, C4 medium (SHAP-of-captions on heads is new, but the evidence is largely circular, see W4).
- **Suggested Fix:** Present the claim as "head-level localization of known corrections", and show it beats a label-aware whole-embedding projection with equal supervision.

### W3: Prior work is characterized more weakly than the prior work's own abstracts warrant
"Existing approaches to debiasing vision models often rely on extensive fine-tuning" and "there are no explainable insights as to why these methods work" (§1/§2) omit that Gandelsman et al. already show head-level roles (which is the paper's own starting point) and that other work already uses attention-head analysis for CLIP bias (Madasu et al. 2025, W1). The statement should be narrowed to "no head-level, automated procedure".
- **Suggested Fix:** Rewrite the positioning sentence and cite.

### W4: The "interpretation corroborates the mechanism" argument is largely circular (E5)
Z_Y and Z_S are chosen with class and background labels, so SHAP over captions annotated with "species" vs "background" tokens (§6, Fig. 3, App. D) will correlate with those attributes by construction. TextSpan outputs for the located states (Tables 13, 17) are mixed: ViT-B Z_Y for Waterbirds lists "Photo of a reptile", "An image with dogs", "A thistle"; ViT-H Z_Y lists "Image with polka dot patterns", "A spiky texture", yet App. D.1 says "the text outputs are fully aligned with their respective intended representations". A non-circular test would intervene (ablate Z_Y, Z_S, Z_SY and show the predicted dissociation, Fig. 4, unverifiable here) on a held-out task or model not used to pick the heads.
- **Suggested Fix:** Report the Fig. 4 dissociation numerically for all three backbones and soften "fully aligned".

## Missing References

*Verified with `related_search.py verify`/`search` unless marked [verify]; strict cutoff 2025-09-24.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Madasu, Lal, Howard. "Pruning the Paradox: How CLIP's Most Informative Heads Enhance Performance While Amplifying Bias", arXiv 2025 (https://arxiv.org/abs/2503.11103v3). Prior (arXiv-only, 6+ months before cutoff) | Head-level intervention on CLIP related to bias: closest head-level prior; cite and differentiate (a MAJOR positioning issue at most, not a known-result issue: the mechanism differs: pruning vs. targeted mean-ablation/projection) |
| Important | Molahasani et al. "PRISM: Reducing Spurious Implicit Biases in Vision-Language Models with LLM-Guided Embedding Projection", ICCV 2025 (https://arxiv.org/abs/2507.08979v1). Prior (peer-reviewed) | Data-free LLM-guided projection debiasing of CLIP: a current baseline family |
| Important | Balasubramanian, Basu, Feizi. "Decomposing and Interpreting Image Representations via Text in ViTs Beyond CLIP", NeurIPS 2024 (https://arxiv.org/abs/2406.01583v2). Prior (peer-reviewed) | Automated component roles; relevant to the "no manual effort" claim |
| Important | Kirichenko, Izmailov, Wilson. "Last Layer Re-Training is Sufficient for Robustness to Spurious Correlations", ICLR 2023 (https://arxiv.org/abs/2204.02937v2) | Label-aware, cheap post-hoc baseline for the same Waterbirds protocol |
| Important | Yang et al. "Debiasing Vison-Language Models with Text-Only Training", arXiv 2024 (https://arxiv.org/abs/2410.09365v1). Prior (arXiv-only) | Text-only debiasing of CLIP; relevant to the Waterbirds/CelebA comparisons |
| Helpful | Gandelsman et al. "Interpreting the Second-Order Effects of Neurons in CLIP", arXiv 2024 (https://arxiv.org/abs/2406.04341v3) | Complements head-level direct-effect analysis (MLP/neuron-level indirect effects omitted here, §4) |
| Helpful | Belrose et al. "LEACE: Perfect linear concept erasure in closed form", NeurIPS 2023 (https://arxiv.org/abs/2306.03819v4); Ravfogel et al. "Null It Out: Guarding Protected Attributes by Iterative Nullspace Projection", ACL 2020 (https://arxiv.org/abs/2004.07667v2) | Concept-erasure literature that the projection step relates to |

**Literature-check addendum.** Mode strict, cutoff 2025-09-24; 5 search queries (3 claim: C1, C2, C3; 1 baseline: Waterbirds; 1 expansion, 0 results), 4 `verify` calls, 1 `scout` (Waterbirds), 1 `similarity` run. Not run: `coverage`/`novelty` scripts; the per-claim verdicts below are my abstract-level ratings, and the search is arXiv-only. **Similarity:** closest prior works by TF-IDF are Gandelsman et al. 2023 (cosine 0.209), Yang et al. 2024 (0.197), Balasubramanian et al. 2024 (0.184); all below the 0.30 overlap flag; zero shared 8-grams, so no text-overlap concern.

| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|---|---|---|---|---|
| C1 automatic head selection | Gandelsman et al. 2023; Balasubramanian et al. 2024 | Head roles via text spans (manual / automated) | Label-driven contrastive selection of bias heads | Gandelsman yes; Balasubramanian no |
| C2 head-level ablation + projection | Madasu et al. 2025; Adila et al. 2023 | Head pruning vs. bias; whole-embedding projection | Head-level mean ablation + projection | Adila yes; Madasu no |
| C3 JTT-LTC | Zhang & Ré 2022 (Cont Adapter); Kirichenko et al. 2023 | Light-weight post-hoc tuning | Edit on top of tuned probe | Cont Adapter yes; Kirichenko no |
| C4 SHAP interpretation | Gandelsman et al. 2023 | Text-based head interpretation | SHAP over generated captions | partially |

| Claim | Dimension | Novelty | Top prior (level, label, cited?) | Reasoning |
|---|---|---|---|---|
| C1 | method | medium | Gandelsman 2023 (3, prior arXiv-only, cited) | Automates an existing manual step with a heuristic |
| C2 | method/result | incremental | Adila 2023 (4, cited); Madasu 2025 (3, not cited) | Same projection recipe, new location |
| C3 | result | incremental | Zhang & Ré 2022 (3, cited) | Extension on tuned probe |
| C4 | result | medium | Gandelsman 2023 (3, cited) | New measurement, weakly independent |

**Baseline scout (Waterbirds, worst-group).** Prior rows surfaced: Contrastive Adapters (peer-reviewed; compared in paper), Yang et al. 2023 "Mitigating Spurious Correlations in Multi-modal Models during Fine-tuning" (cited, not compared), Debiased Prompt Tuning (2025, arXiv-only; not cited), TOD (2024; not cited), StarFT (IJCAI 2025; not cited), PRISM (ICCV 2025; not cited). Their abstracts give no matched-setting numbers, so none is an under-reported baseline; these are *missing comparisons from prior work* at MAJOR at most, and they are fine-tuning/training-based methods, so they do not undermine the training-free comparison.

**Field snapshot.** Five years ago group robustness meant retraining (Group DRO, JTT); with CLIP the focus shifted to cheap adapters, text-only training and zero-shot projection (Adila 2023, Chuang 2023, PRISM 2025). Mechanistic work (Gandelsman 2023/2024, Balasubramanian 2024) now localizes behavior in heads/neurons. What counts as significant today: a clear gain over the strongest label-matched baseline on several benchmarks and an intervention that is shown causally, not just a gain over zero-shot. This lens is why I score Significance at 54.

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | See R1 |
| Clarity | 2 | Positioning thin |
| Significance | 2 | Incremental over Roboshot/Ortho-Cali at ViT-B/L |
| Originality | 2 | Moderate novelty at head level |

## Dimension Scores (0–100)

**Pool position:** better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the novelty is a head-level relocation of known operators with a heuristic selection rule, and uncited, closer head-level prior work exists; the automation of TextSpan's manual step and the localization ablation lift it above the median.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing | Selection logic heuristic; derivation ambiguity |
| Clarity & Presentation | 58 | Competent | Positioning sentences overstated |
| Novelty & Originality | 54 | Competent | Medium/incremental per claim |
| Significance & Impact | 54 | Developing | Gains over best baseline small on 2/3 backbones |
| Experimental Validation | 50 | Developing | Prior-art comparisons missing |
| Reproducibility | 54 | Competent | Details mostly present |
| Ethical Compliance | 62 | Competent | Brief but adequate |

## Questions for Authors
1. How does LTC differ operationally from head-pruning-based bias mitigation (Madasu et al.)? A head-level pruning baseline on Waterbirds would raise my Novelty score.
2. Do the located heads transfer across datasets with the same attribute (e.g., Z_S from Waterbirds to CounterAnimal, which the paper re-uses, §5.1)? Transfer would indicate attribute-level rather than dataset-level heads.
3. Can you show Fig. 4's S vs S+Y dissociation numerically for all backbones?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially (see R1).

## Ethics Review Flag
**No.**

## Overall Score
**3**: A reasonable head-level take on known projection debiasing; positioning and the strongest-baseline comparison need work before the contribution clears the ICLR bar.

## Confidence
**4**: Literature check completed (arXiv only); abstract-level reading of prior works.

---

# Peer Review Report

## Paper: Debiasing CLIP: Interpreting and Correcting Bias in Attention Heads
## Reviewer: Dr. Joaquín Ferreyra-Holm, Perspective Reviewer (algorithmic-fairness group, Latin America; fictional persona)
## Expertise: Fairness auditing, causal mediation analysis, validity of bias metrics
## Date: 2026-11-10

---

## Summary
The paper proposes to localize where CLIP's vision tower encodes spurious cues and gender stereotypes, edit those heads at inference time, and thereby reduce subgroup gaps without retraining. It frames this as a step from mechanistic interpretability to practical debiasing.

## Strengths

### S1: Connects mechanistic tools to a fairness-relevant intervention
Using direct-effect attribution (logit lens, §4.1) to choose where to intervene is close in spirit to causal mediation analysis for bias (Vig et al. 2020 is cited in §2), and a transparent, low-compute edit (App. E: one A100) is attractive for auditors.

### S2: Test of a "what is encoded" hypothesis
§6's finding that the contrastive rule locates an *association* state (Z_SY) rather than the attribute itself is a useful conceptual distinction for bias research: removing a stereotype link differs from removing information about the attribute. Table/Figure evidence is mostly in the appendix (unverifiable figures).

### S3: Candid about LLM failure modes
The note that Roboshot's LLM may refuse to flag gender as a spurious source (§5.1, B.2) is a practical observation for pipeline designers, though untested.

## Weaknesses

### W1: Fairness metrics measure gaps, not harm
Bias is the absolute accuracy difference between gender groups, averaged over occupations (§5.1), and MaxSkew for retrieval (Table 3). Neither shows whether accuracy for either group fell. In deployment (e.g., hiring or search surfaces) leveling down is a known failure of gap metrics. The synthetic GenderBias-VL images and BLS-derived "stereotype" labels (App. A.1) tie the notion of bias to US workforce statistics, binary gender and a pairwise y vs ȳ design; transfer to real-world imagery is not shown.
- **Suggested Fix:** Report per-group accuracy and a recall@K for retrieval; add a real-image check (FairFace race/age are available but unused).

### W2: Assumption that the sensitive attribute is known, labeled and single
LTC locates heads using group labels (§5.1, "ground truth group labels for the validation set") and edits one attribute at a time. Real bias is intersectional. The paper does not test whether ablating "gender heads" shifts other attributes (e.g., race in FairFace) or whether it leaves the model more reliant on other proxies.
- **Suggested Fix:** Evaluate cross-attribute effects with the FairFace race/age labels, and report side-effects on neutral tasks (ImageNet zero-shot).

### W3: Deployment and generality
Edits are dataset-specific and static ("sample-independent", §4.3), so each task needs a labeled calibration set and a repeat of locating; they do not generalize to new classes. Compare to concept-erasure methods in NLP (e.g., iterative nullspace projection, linear concept erasure; references in R2) that offer guarantees about linear recoverability of the attribute: a recoverability test (can a linear probe still decode gender/background from the edited image embedding?) would show whether information is removed or only the decision path changed. This is a concrete cross-field measurement the paper lacks.
- **Suggested Fix:** Add attribute-probe recoverability before/after editing, and discuss when edits stop transferring.

### W4: Societal-impact paragraph is dismissive on dual use
"the methodology requires explicit identification and manipulation of known components and would unlikely be possible on proprietary models" (App. F) argues that misuse is unlikely, but open OpenCLIP weights are exactly what the method edits, and the same edit could *amplify* an attribute reliance. A short discussion of safeguards (audit logs, edit disclosure) is missing.
- **Suggested Fix:** Replace with a short, evidence-based dual-use note.

## Missing References
Not required from this role; see R2 (concept erasure links are given there).

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Reasonable method, partial evaluation |
| Clarity | 3 | Readable with drift |
| Significance | 3 | Useful tool-like idea if generalizes |
| Originality | 3 | Fresh combination with a conceptual distinction (Z_SY) |

## Dimension Scores (0–100)

**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a coherent, inexpensive interpretability-to-intervention story with ablations and honest sensitivity analyses that most mid-pool submissions lack; held back by gap-only fairness evidence.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound edit, clear causal logic via ablations |
| Clarity & Presentation | 62 | Competent | Understandable |
| Novelty & Originality | 64 | Competent | Head-level and S–Y association angle |
| Significance & Impact | 66 | Competent | Practical, low-compute intervention |
| Experimental Validation | 58 | Competent | Several benchmarks and sizes; limits above |
| Reproducibility | 62 | Competent | Code promised (link removed), prompts given (Table 5) |
| Ethical Compliance | 62 | Competent | Impact paragraph present but thin; binary gender |

## Questions for Authors
1. After editing, can a linear probe still decode the attribute from the final image embedding? (A strong drop would raise my significance score.)
2. What happens to per-gender accuracy and retrieval relevance?
3. Does the edit change behavior on non-target attributes in FairFace?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No.** Synthetic and public benchmark data; no new human-subject data.

## Overall Score
**4**: An interesting and low-cost interpretability-grounded intervention with sensible ablations; the fairness evidence is thinner than the framing, but typical accepted papers carry comparable gaps.

## Confidence
**3**: Fairly confident; outside my main sub-area for the CLIP head-level details.

---

# Peer Review Report

## Paper: Debiasing CLIP: Interpreting and Correcting Bias in Attention Heads
## Reviewer: Dr. Sun-hee Ostrowska, Generalist Reviewer (applied vision team; East Asia; fictional persona)
## Expertise: Multimodal learning, general ML program committee
## Date: 2026-11-10

---

## Summary
The paper proposes LTC, which finds attention heads in CLIP's ViT that carry spurious or class-relevant information and corrects them by mean ablation and orthogonal projection toward LLM-derived features. It evaluates on Waterbirds, CounterAnimal, GenderBias-VL and FairFace with three OpenCLIP sizes, reports larger worst-group improvements than three training-free baselines, shows an extension on top of JTT, and analyzes the selected heads with SHAP and TextSpan.

## Strengths

### S1: A clear one-paragraph idea
"Locate-then-correct" is easy to state and positioned against whole-embedding projection (§1, Fig. 1); the contribution is understandable after the introduction.

### S2: Broad enough evaluation for the venue
Four datasets, two bias types, three model sizes, and an ablation table (Tables 1–3, 6, 7) go beyond a single benchmark; the sensitivity appendix (B.3–B.5) is unusually candid.

### S3: Interpretability is part of the method, not an afterthought
Sections 6 and App. D connect each edited head to text and pixel evidence (Figs. 2–3, 21–28, unavailable here), which fits ICLR's interpretability audience.

### S4: Low compute
All experiments run on one A100 (App. E).

## Venue criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness of claims vs evidence | Partly | Abstract ">50%" vs Table 1 |
| Contribution significance | Partly | Moderate; head-level localization |
| Presentation clarity | Partly | Dense §4.2; cross-reference slips |
| Reproducibility | Partly | Code link; checkpoint/GPT-4o version missing |
| Honest limitations | Partly | Limitations short |

## Weaknesses

### W1: Claims in the abstract and results narrative run ahead of the tables
">50% gain … compared to non-training post-hoc baselines" holds against zero-shot but not the strongest baseline (+7.6%, +1.8%, +17.5% on B/L/H, derived from Table 1); "Ortho-Cali consistently underperforms" is contradicted for ViT-B/L; "LTC is the only method that consistently improves over zero-shot CLIP" on CounterAnimal rests on +0.4/+0.2/+1.1 points.
- **Suggested Fix:** Rewrite those three sentences. Cost: none.

### W2: §4.2 is hard to follow for a non-specialist
Eq. 8–10 mix signed logit differences and one-hot-normalized scores, Z_S and Z_SY are used interchangeably, and Definition 4.1 conditions on "ŷ = y*" for G_N but the method uses G_NW and G_NC. A small worked example (e.g., two heads, four samples) would make it checkable.
- **Suggested Fix:** Add a toy example and a table of notation.

### W3: Presentation and consistency slips distract from the substance
"Tab. 10" for the sensitivity table (it is Table 9); "ViT-L/16" in Table 9; "λ" vs "γ"; "GPT4-o" vs MiniCPM-V captioner. None invalidates results, but together they lower trust in the appendix tables.
- **Suggested Fix:** A consistency pass.

## Minor
Typos ("We hypothesis"), "Waterbird:" heading, undefined N_u for Waterbirds.

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Solid ablations; some overstated claims |
| Clarity | 3 | Readable; §4.2 hard |
| Significance | 3 | Moderate |
| Originality | 3 | Reasonable |

## Dimension Scores (0–100)

**Pool position:** better than about 65% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: clean idea, broad-enough benchmarks and unusually honest sensitivity analyses; weaknesses (single runs, overclaimed wording, partial baselines) are typical of papers that are accepted.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound approach, correctly applied |
| Clarity & Presentation | 64 | Competent | Mostly clear; §4.2 dense |
| Novelty & Originality | 62 | Competent | Reasonable combination |
| Significance & Impact | 62 | Competent | Useful sub-area contribution |
| Experimental Validation | 60 | Competent | Multi-dataset, ablations |
| Reproducibility | 62 | Competent | Details mostly present |
| Ethical Compliance | 64 | Competent | Limitations and impact paragraphs present |

## Questions for Authors
1. Can you rewrite the abstract's headline relative to the best baseline? (If the gain over the strongest baseline still holds on additional backbones, I would move up.)
2. What changes in §4.2 if V is the signed logit difference rather than the one-hot histogram?
3. How do results change if the LLM features come from an open model instead of GPT-4o?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No.**

## Overall Score
**4**: A readable, reasonably broad paper whose weaknesses are typical of ICLR accepts; I lean accept if the claims are narrowed.

## Confidence
**3**: Fairly confident; did not verify derivations line by line.

---

# Devil's Advocate Report

## Paper: Debiasing CLIP: Interpreting and Correcting Bias in Attention Heads
## Reviewer: Dr. Beatrix Nakamura-Cole (evaluation-methodology lab, North America; fictional persona)

---

## Steelman
Debiasing at the granularity of single attention heads is cheap and leaves the rest of CLIP intact. The contrastive rule uses the model's own errors to find heads that carry the spurious link, and the ablations (random heads hurt, injection alone is weaker, ablation alone is weaker) are consistent with a real localization effect that whole-embedding projection cannot reach.

## Core Argument Chain
1. A contrast between head attributions on wrongly vs. correctly classified minority-group samples isolates S–Y heads (§4.2, Eq. 10).
2. Mean-ablating those heads and projecting target heads onto LLM-derived directions removes bias without harming the model (§4.3).
3. This gives larger worst-group gains than whole-embedding projection baselines (Tables 1–3).
4. SHAP/text/pixel interpretations of the heads confirm what the heads encode (§6).
∴ Locating and correcting individual heads is more effective *and* more interpretable than existing debiasing.

## Strongest Counter-Argument
The comparison that carries the paper, LTC vs. Roboshot/Ortho-Cali/TextSpan, is a comparison between a method that uses a labeled, attribute-annotated validation set to pick where to intervene and methods that do not. The LTC-Ŝ row, which reduces the label requirement, is the like-for-like entry, and there it loses on ViT-B (61.8 vs Ortho-Cali 68.1) and ties on ViT-L within what is likely run-level noise (75.5 vs 73.3). So the claim that *head-level* correction is what helps, rather than *supervision used to locate it*, is not isolated: no experiment applies the same labeled validation set to a whole-embedding projection (e.g., fit the discriminative/spurious directions from validation labels) or to a label-aware linear re-fit, and the paper's own tuned baselines (Cont Adapter 83.2/83.7/87.5 WG) are far above any training-free number. The residual advantage of LTC over the best training-free baseline averages +8.5% in WG (derived from Table 1), and the headline ">50%" is a gain over the unmodified model. On GenderBias the "worst-group" is chosen from zero-shot bias, so random edits already "improve" it (Table 7, LTC (R): 74.0→30.5 on ViT-B) while overall bias barely moves. The interpretability claim is then circular, since heads chosen with class/background labels will show class/background semantics. If the authors can show that head-level location beats an equal-supervision whole-embedding edit, a held-out-selected gender metric, and a non-circular causal test, the paper survives; as it stands, the three pillars (efficacy, fairness metric, interpretability) each depend on a confound.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The main claim (head-level correction improves worst-group accuracy over zero-shot, and often over training-free baselines) is supported in weaker form by Tables 1 and 6; every issue below is fixable by narrowing claims or adding controls, and I found no test-set selection of a reported configuration in the protocol sweep (selection statements: §5.1, §5.2, App. A.1, B.3).

### MAJOR Issues

| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence/Scope (E5) | Abstract; Table 1 | ">50% gain" is over zero-shot; vs best baseline +7.6/+1.8/+17.5% (B/L/H). Evidence supports a weaker claim | Reword |
| DA-M2 | Evidence (E4) | §5.1; A.2 | Supervision mismatch; LTC-Ŝ loses on B and is within noise on L | Equal-label-budget baseline; report LTC-Ŝ as main |
| DA-M3 | Evidence (E4) | Table 1 | Ortho-Cali ViT-H 18.1/41.9 below ZS and below chance-level Avg; unexplained | Debug, explain |
| DA-M4 | Evidence (E4) | Table 2 caption; Table 7 | BT selected on zero-shot bias; random edits reduce BT 43.5/19.4/34.3 points while BO unchanged; accuracy never shown | Hold-out selection, per-group accuracy |
| DA-M5 | Logic (E2/E6) | §4.1 vs §4.2 | Sign-based argument vs normalized one-hot V | Clarify |
| DA-M6 | Logic (E5) | §6, App. D | Circular interpretation; "fully aligned" overstated given Tables 13/17 entries such as "Photo of a reptile" | Intervention-based test; soften |
| DA-M7 | Evidence (E5) | §5.1; Table 1 (CA) | "only method that consistently improves" rests on +0.4/+0.2/+1.1 points, no CIs | CIs; soften |

### MINOR Issues

| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | Table 1/6/9 | LTC ViT-L Gap 9.4 vs 9.6 vs 9.5 (Avg−WG) |
| DA-m2 | Consistency | §6 vs App. D, Table 10 | Captioner GPT-4o vs MiniCPM-V 2.6 |
| DA-m3 | Consistency | B.5 | "Tab. 10" vs Table 9; "ViT-L/16" |
| DA-m4 | Reasoning | §5.1 | Roboshot failure attributed to LLM safeguards, untested |
| DA-m5 | Scope | A.1 | CounterAnimal ȳ-mapping uses pseudo-labels and a 45-class dictionary inside 1,000-way classification; D_E used for mapping |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| WG gain vs ZS, ViT-B | ">50%" (avg) | 73.3/49.7 = +47.5%; mean over sizes 73.07/48.17 = +51.7% | Only vs ZS, on the 3-size average |
| WG gain vs best baseline, ViT-B/L/H | n/a | +7.6% / +1.8% / +17.5% (68.1, 73.3, 60.7) | Claim not supported vs strongest |
| Waterbirds Gap, ViT-L LTC | 9.4 (Tab. 1), 9.6 (Tab. 6) | 84.1 − 74.6 = 9.5 | Mismatch (minor) |
| CounterAnimal Gap | e.g., 21.1 (ZS) | 54.8 + 21.1 = 75.9 = 55.2 + 20.7 | Gap is a fixed constant minus Avg |
| BT reduction by random states (Tab. 7) | n/a | 74.0−30.5 = 43.5; 54.7−35.3 = 19.4; 67.7−33.4 = 34.3 | Random edits move BT a lot; BO flat (16.3→12.2, 12.9→14.6, 15.2→15.0) |
| JTT-LTC vs Cont Adapter WG | n/a | +3.2 / +5.9 / +1.6 | Single run |

## Ignored Alternative Explanations
- Gains come from using labeled validation data (supervised head choice), not from head-level granularity.
- BT improvements partly reflect regression to the mean after selecting outliers by zero-shot bias.
- Z_Y heads act as generic object-category heads (Tables 13/17 mention reptiles, dogs, magnolias), so "knowledge injection" boosts generic object evidence, which also helps accuracy.
- Waterbirds background is trivially predictable (LTC-Ŝ), which may not carry over to subtler spurious features.

## Missing Stakeholder Perspectives
Users of retrieval systems affected by edits that lower accuracy for the advantaged group; practitioners who need edits that survive model updates; people with non-binary gender identities, absent from the binary gender framing.

## Observations (Non-Defects)
Random-head, MA-only, KI-only and RS (KI) ablations (Tables 6/7); the Full-vs-G_N locating analysis (Table 8, B.4) and prompt-set sensitivity (Table 9) are reported even though they show fragility.

## Dimension Scores (0–100)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 50 | Derivation ambiguity; selection-prone metric |
| Clarity & Presentation | 58 | Slips |
| Novelty & Originality | 52 | Incremental over projection debiasing |
| Significance & Impact | 52 | Small gains over best baseline |
| Experimental Validation | 46 | Confounded comparison |
| Reproducibility | 52 | Missing details |
| Ethical Compliance | 62 | Adequate |

**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the central comparison is confounded by supervision and the gender metric by selection.

## Overall: 3 | Confidence: 4

---

# Phase 1.5 / 1.6: Literature Check and Report Check

**Literature check:** mode strict, cutoff 2025-09-24, arXiv-only. 5 searches (3 claim, 1 baseline, 1 expansion with 0 results), 4 verify calls (all found), 1 scout (Waterbirds), 1 similarity (no overlap flags: max cosine 0.209, 0 shared 8-grams). `coverage` and `novelty` scripts not run (claim profile written by hand in R2's addendum). No results after the cutoff were used. Recommended references are all "prior" labels and verified; none is marked `[verify]`.

**Report check (Synthesizer Step 0):**

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | Single runs (W4) | Kept, reframed | Specific gap tied to small margins (Tables 1, 9) rather than "single run" alone |
| R1 | Table 8 ZY "8/48" contradicts Tables 14/15 | Moved to Question (not a weakness) | Different SHAP aggregations (Y/S vs species/features); low confidence (E6), could be a column-order issue |
| R2 | "Closest prior is known" (Madasu et al.) | Rewritten | Mechanism differs (pruning); MAJOR positioning issue at most; abstract-level only |
| R2 | Prior work mischaracterized (W3) | Rewritten | Only the "no explainable insights" sentence conflicts with Gandelsman's own contribution |
| R3 | Missing real-image evaluation | Kept | Actionable (FairFace race/age are available) |
| R4 | Typos/cross-refs (W3) | Moved to Minor line | Cosmetic |
| DA | "Test-set selection on GenderBias" | Downgraded from CRITICAL candidate to MAJOR (DA-M4) | Selection affects the BT metric definition, not a tuned configuration; BO and the Waterbirds results do not rely on it |
| DA | Interpretation circular | Kept as MAJOR | Specific, with Tables 13/17 quotes |

---

# Phase 2: EIC Meta-Review and Decision

*Synthesizer part A: official score computed with `aggregate_scores.py` (before.json): official rating 3.40, official composite 56.5 (before composite), no warnings, no DA-CRITICAL issues. Issue map: CONSENSUS-4: headline/overclaim wording (R1-W1, R2-W3, R4-W1, DA-M1); CONSENSUS-3: baseline/supervision mismatch and missing variance (R1-W2/W4, R2-W2, DA-M2/M7); CONSENSUS-3: gap-only fairness metric (R1-W3, R3-W1, DA-M4); CONSENSUS-2: derivation clarity (R1-W5, R4-W2, DA-M5); SOLO: dual-use paragraph (R3-W4), Madasu et al. positioning (R2-W1); SPLIT: whether the interpretability evidence is valuable (R3-S2, R4-S3) or circular (R2-W4, DA-M6).*

# Editorial Decision

## Paper: Debiasing CLIP: Interpreting and Correcting Bias in Attention Heads
## Submission ID: iclr26-md9nBwwmEh
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC (meta-reviewer) Dr. Marguerite Okonjo-Lindqvist; R1 Methodology Dr. Anselm Kowarik, R2 Domain Dr. Leocadia Mbeki-Strand, R3 Perspective Dr. Joaquín Ferreyra-Holm, R4 Generalist Dr. Sun-hee Ostrowska, DA Dr. Beatrix Nakamura-Cole

---

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 4, DA 3 → mean 3.40 · official composite 56.5
**EIC assessment** (internal): weighted rating 3.32 → starting point 3 · weighted composite 55.7 → band 3 (cross-check agrees) · **DA ceiling**: none (no CRITICAL issue raised) · **Final (EIC)**: 3
**Venue label (ICLR, scale status secondary):** 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); sub-scores Soundness 2 / Presentation 2 / Contribution 2

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A cheap, intuitive idea (head-level locate-then-correct) with ablations that isolate localization (random heads hurt; MA-only and KI-only are each weaker, Tables 6–7), three backbone sizes, a candid sensitivity appendix, and an interesting S vs S–Y association finding (§6). Weaknesses such as single runs and overclaimed wording are typical of accepted ICLR papers.
- **Against acceptance:** The headline (">50%") is a gain over zero-shot; against the best training-free baseline the gain is +7.6/+1.8/+17.5% and, for ViT-L, within likely noise. The comparison mixes label-aware LTC with label-free baselines, one baseline is unexplained-broken, the gender "worst-group" is selected on zero-shot outcome and only gap metrics are shown, CounterAnimal gains are tiny, and the interpretability evidence is largely circular.

### Verification of Decisive Points (EIC read of the paper)

| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| ">50% gain" is vs ZS; vs best baseline +7.6/+1.8/+17.5% | R1-W1, R4-W1, DA-M1 | Abstract; Table 1 | Verified | Recomputed: 73.3/68.1, 74.6/73.3, 71.3/60.7. The abstract's "non-training post-hoc baselines" can be read as including ZS only if ZS counts as a baseline; the 3-size average vs ZS is +51.7% |
| Ortho-Cali ViT-H collapse (18.1/41.9) and "consistently underperforms" | R1-W2, DA-M3 | Table 1; §5.1 | Verified | Text quote located at §5.1, contradicts B/L rows |
| LTC-Ŝ is the label-fair row and loses on ViT-B | R1-W2, DA-M2 | Table 1 | Verified | 61.8 vs 68.1; ViT-L +2.2, ViT-H LTC-Ŝ 73.7 vs RS 60.7 |
| BT selected on zero-shot bias; LTC (R) reduces BT by 43.5/19.4/34.3 | R1-W3, DA-M4 | Table 2 caption; Table 7 | Partly correct | Table 2 caption does say "chosen via zero-shot inference of the respective model", but the text leaves open whether the evaluation set or the 25-occupation split provides the top-10, so the regression-to-the-mean explanation is plausible, not established |
| BO not best for ViT-L/H (9.8 vs 9.2; 10.1 vs 9.4) | R1-W3 | Table 2 | Verified | |
| CounterAnimal gains within noise | R1-W4, DA-M7 | Table 1 (CA block) | Verified (gains) / Partly correct (noise) | Gains +0.4/+0.2/+1.1 confirmed; SE ≈ 0.65 is derived from sample size 5,926, paired SE would be smaller |
| §4.1/§4.2 sign vs normalization inconsistency | R1-W5, DA-M5 | §4.1, §4.2, Eq. 7–10 | Partly correct | Quote located; equations garbled in extraction so I treat it as a clarity issue, not an error in the math |
| Captioner GPT-4o vs MiniCPM-V | R1 ERR-5, DA-m2 | §6; App. D; Table 10 | Verified | |
| Interpretation circular; "fully aligned" overstated | R2-W4, DA-M6 | §6; App. D.1; Tables 13/17 | Partly correct | Selection criterion supports circularity; Fig. 4 (unavailable) provides some intervention evidence |
| Madasu et al. head-pruning bias work uncited | R2-W1 | §2; ledger | Verified (as to citation) / Overstated (as to novelty harm) | Prior, arXiv-only; mechanism differs; MAJOR positioning at most; not a basis for a score cut by itself |
| No test-set selection of reported configs | R1 sweep, DA | §5.1, §5.2, A.1, B.3 | Verified | Search of selection sentences found none for Waterbirds; GenderBias BT is the only ambiguity |

### Reviewer Weights

| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Points verified against Table 1/2/7; one inference (regression to the mean) partly speculative but flagged |
| R2 (Domain) | 3 | 4 | 1.0 | Sound; the Madasu et al. concern is partly overstated as a novelty problem, though the citation gap is real |
| R3 (Perspective) | 4 | 3 | 1.0 | Role-appropriate and constructive; the recoverability test is a good addition; scores somewhat lenient but not wrong |
| R4 (Generalist) | 4 | 3 | 1.0 | Typical PC member; correctly flags overclaim wording, rating leans on typical-accept logic |
| DA | 3 | 4 | 1.25 | Counter-argument survived my check (supervision confound, Table 1 anomalies); correctly no CRITICAL |

### DA-CRITICAL Rulings
The Devil's Advocate raised none ("No CRITICAL issues found."), so no ruling is needed. Independently, I checked criterion 3: the paper states no selection of a reported configuration on the reported test split (see verification row), and the GenderBias top-10 definition concerns the metric rather than a tuned setting, so it stays MAJOR (DA-M4). DA ceiling: none.

| Issue | AC test | Ruling | Resolvable by |
|-------|---------|--------|---------------|
| none raised | n/a | n/a | n/a |

### Final Decision and Justification
The starting point (EIC-weighted rating 3.32 → 3) and the composite cross-check (55.7, band 3) agree, and I keep the starting point; there is no verified issue the ratings failed to account for. The two accept-leaning ratings (R3, R4) rest on the paper's idea and breadth, which I credit, but their reasoning leans on "weaknesses typical of accepted papers" while the decisive weaknesses here are not the typical ones: the headline claim is not true against the strongest baseline, the main comparison mixes supervision regimes, and the gender worst-group metric is selection-prone. None of these is fatal, since each can be fixed with new controls or narrowed claims, which is why I do not place the paper in the bottom tier. **My pool position: better than about 54% of ICLR submissions**, i.e., at the top of the typical rejected band; the deciding evidence is (i) the +1.8% to +17.5% margin over the best training-free baseline with no variance reporting, (ii) the unexplained Ortho-Cali collapse, and (iii) gender evidence limited to selection-prone gap metrics. With the ICLR 2026 scale shown, this corresponds to a 4 on {0,2,4,6,8,10}. A revision that reports the equal-supervision baseline, held-out gender selection with per-group accuracy, CIs, and narrowed claims could plausibly move this to a borderline accept.

---

## Score Summary

### Official Scores and EIC Assessment (`aggregate_scores.py --venue iclr --final 3`)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 50 | 54 | 62 | 62 | 50 | 55.6 | 54.6 | 12 |
| Clarity & Presentation | 56 | 58 | 62 | 64 | 58 | 59.6 | 59.1 | 8 |
| Novelty & Originality | 54 | 54 | 64 | 62 | 52 | 57.2 | 56.4 | 12 |
| Significance & Impact | 52 | 54 | 66 | 62 | 52 | 57.2 | 56.2 | 14 |
| Experimental Validation | 46 | 50 | 58 | 60 | 46 | 52.0 | 50.9 | 14 |
| Reproducibility | 50 | 54 | 62 | 62 | 52 | 56.0 | 55.1 | 12 |
| Ethical Compliance | 62 | 62 | 62 | 64 | 62 | 62.4 | 62.3 | 2 |
| **Composite** | 51.9 | 54.4 | 62.1 | 62.0 | 52.0 | **56.5 (before)** | **55.7 (after)** | |

No dimension exceeds the 20-point spread flag. Pool positions: R1 48, R2 52, R3 66, R4 65, DA 50, EIC 54.

### Target-Venue Scores (ICLR 2026 cycle, scale status: secondary; verify against the current form)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution | 2 / 2 / 2 (each on 1–4) |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); venue composite 55.5 |
| Internal label | Borderline Reject (3) |

### Cross-Venue Outlook
Not requested.

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Debiasing CLIP: Interpreting and Correcting Bias in Attention Heads" to ICLR.

The paper addresses spurious and gender-linked bias in CLIP with a mechanistic, head-level correction that avoids retraining and is cheap to run.

**Overall Assessment:** The panel found the idea clear and the ablations informative, and valued the candid sensitivity analyses. It was concerned that the headline gain is measured against the least demanding comparison, that LTC and the training-free baselines use different amounts of supervision, and that the gender worst-group metric is selection-prone and reported without accuracy. The panel's official ratings were 3, 3, 4, 4 and 3.

**Key Strengths Identified by Reviewers:**
1. Ablations that isolate localization (random heads, MA-only, KI-only, RS (KI)) (R1, R2, R4).
2. Multiple datasets and three model sizes; low compute; candid sensitivity appendix (R1, R4).
3. The S vs S–Y association finding and the attempt to link intervention to interpretation (R2, R3).

**Key Concerns Requiring Attention:**
1. The ">50%" claim and §5.1 wording against Table 1 (CONSENSUS-4).
2. Supervision-matched baselines; Ortho-Cali anomaly on ViT-H; single-run margins (CONSENSUS-3).
3. Gender metrics: selection of the top-10 occupations, no per-group accuracy, retrieval gains vs TextSpan/Ortho-Cali (CONSENSUS-3).

**Critical Challenge (Devil's Advocate):** The efficacy claim is confounded: LTC uses labeled validation data to choose where to edit, so the benefit of head-level granularity is not separated from the benefit of supervision. This must be addressed with an equal-supervision control.

**Decision: Borderline Reject (3)**

We lean toward rejection in the current form: the contribution is real but the evidence does not yet support the claim as worded. What would change the decision: an equal-label-budget whole-embedding/last-layer baseline; CIs and mean ± std for all rows; a held-out selection of the gender worst-group set with per-group accuracy; an explanation of the Ortho-Cali collapse; and narrowed claims in the abstract and §5.1.

Please refer to the Revision Roadmap below.

Sincerely,
Dr. Marguerite Okonjo-Lindqvist
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Headline/wording overstates gain vs best baseline | R1, R2, R4, DA | CONSENSUS-4 |
| Baseline comparability (supervision, Ortho-Cali anomaly), variance missing | R1, R2, DA (R4 partly) | CONSENSUS-3 |
| Gap-only gender metrics / selection | R1, R3, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the interpretation evidence valuable? | R3, R4 | R2, DA | Partly circular by construction; valuable only where interventions (Fig. 4, unavailable) show the dissociation; counts little toward the score until shown numerically |
| Accept-leaning vs reject-leaning overall | R3, R4 (4) | R1, R2, DA (3) | Reject-leaning reasons verified on Tables 1/2/7; accept-leaning reasons rely on typicality not verified |

### Score Spread Discussion
No dimension flagged (> 20). The largest spreads (Significance, Experimental Validation: 14) reflect R3/R4's leniency on baseline fairness.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | ">50%" vs strongest baseline | Yes (R1, R4) | n/a | n/a |
| DA-M2 | MAJOR | Supervision confound | Yes (R1, R2) | n/a | n/a |
| DA-M3 | MAJOR | Ortho-Cali ViT-H | Yes (R1) | n/a | n/a |
| DA-M4 | MAJOR | BT selection / random edits | Yes (R1) | n/a | n/a |
| DA-M5 | MAJOR | §4.1 vs §4.2 | Yes (R1, R4) | n/a | n/a |
| DA-M6 | MAJOR | Circular interpretation | Yes (R2) | n/a | n/a |
| DA-M7 | MAJOR | CounterAnimal claim | Yes (R1) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*Issues the EIC verified as undermining a main claim as worded; no upheld DA-CRITICAL issue exists.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Headline and §5.1 claims not supported vs strongest baseline; "Ortho-Cali consistently underperforms"; CounterAnimal "only method" | R1-W1, R4-W1, DA-M1, DA-M7 | Abstract; §5.1; Table 1 | Reword to best-baseline numbers; soften CA claim | Low (0 GPU-h) | Yes |
| R2 | Supervision-mismatched comparison; no equal-label-budget baseline | R1-W2, R2-W2, DA-M2 | §5.1; A.2; Table 1 | Add whole-embedding/last-layer baseline using the same group-labeled validation data; make LTC-Ŝ the primary row | Medium (~24 GPU-h) | Yes (partially) |
| R3 | Ortho-Cali ViT-H collapse unexplained | R1-W2, DA-M3 | Table 1 | Debug/explain; state official code vs re-implementation | Low–Med (~4 GPU-h) | Yes |
| R4 | Gender worst-group selection; no per-group accuracy; BO not best for L/H | R1-W3, R3-W1, DA-M4 | Table 2; Table 7; §5.1 | Held-out top-10 selection; random-edit control; per-gender accuracy and retrieval recall | Medium (~3 GPU-h) | Yes |
| R5 | No variance for small margins; main-table feature set not stated | R1-W4, DA-M7 | Tables 1–3, 9 | Bootstrap CIs; mean ± std over feature sets for all rows | Low | Yes |

### Priority 2: Strongly Suggested (Should Fix)

| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Derivation inconsistency and Z_S/Z_SY drift | R1-W5, R4-W2, DA-M5 | Worked example; consistent notation | Low | Yes |
| S2 | Circular interpretation; "fully aligned" overstated | R2-W4, DA-M6 | Report Fig. 4 dissociation numerically; soften | Low–Med | Yes |
| S3 | Missing closest prior/related work (head pruning for CLIP bias, PRISM, automated ViT decomposition, last-layer retraining, TOD) | R2-W1/W3, Missing References | Add delta table; compare with PRISM if feasible | Low–Med | Yes |
| S4 | Generality and side-effects: ImageNet zero-shot, attribute recoverability, FairFace race/age, second benchmark | R1-W6, R3-W1/W2/W3 | Add side-effect and recoverability tests | Medium (~8 GPU-h) | Partly |
| S5 | Reproducibility details: OpenCLIP checkpoints, GPT-4o version/decoding, N_u (Waterbirds), layer-range choice, mean-ablation reference set | R1 protocol sweep | State in appendix | Low | Yes |

### Priority 3: Nice to Fix (Optional)

| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Dual-use paragraph dismissive | R3-W4 | Replace with evidence-based note |
| N2 | Table/figure cross-references and notation (λ/γ, "Tab. 10", ViT-L/16, captioner) | R4-W3, DA-m1–m3 | Consistency pass |
| N3 | LLM-safeguard explanation of Roboshot failure untested | DA-m4 | Test with an open LLM or soften |
| N4 | CounterAnimal pseudo-label/dictionary design | DA-m5 | Describe limits; report with and without |
| N5 | Table 8 ZY "8/48" vs Tables 14/15 | Report check | Clarify metric definitions |

## Estimated Revision Effort
- Priority 1: 5 items, ≈ 2–3 days (mostly reporting; ≈ 30 GPU-hours)
- Priority 2: 5 items, ≈ 2–3 days
- Priority 3: 5 items, < 1 day
- **Total estimated revision time**: ≈ 1 week

---
*Simulation only: this is how a careful panel might see this draft, not a prediction of any venue's decision.*
