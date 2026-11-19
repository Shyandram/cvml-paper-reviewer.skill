# Academic Paper Review: "Mapping Post-Training Forgetting in Language Models at Scale"

*Simulated panel review (a simulation, not a prediction). Date: 2026-11-10. Request: full review, target venue ICLR, literature check strict, cutoff 2025-09-24, confirmation skipped.*
*Text-extracted manuscript; **figures (Fig. 1–16) were not available**. Figure-dependent claims are judged from captions and the appendix tables (Tables 2–35) only; this is stated where it matters.*

---

## Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Mapping Post-Training Forgetting in Language Models at Scale |
| Primary Discipline | Machine learning → continual learning / evaluation of LLM post-training |
| Secondary Discipline(s) | LLM benchmarking and evaluation methodology; model merging; psychometrics (guessing correction) |
| Paper Type | Analysis/Insight (an empirical study of public checkpoints plus a proposed metric); composite weights: analysis (0.25 / 0.10 / 0.20 / 0.20 / 0.15 / 0.05 / 0.05) |
| Core Technique(s) | Per-item 1→0 / 0→1 transition counting; chance-adjusted variants F_true, BT_true for multiple-choice; zero-shot/few-shot CoT evaluation in LightEval; linear/SLERP interpolation of checkpoints |
| Target Venue | ICLR 2026 cycle, top-tier ML conference, accepted share about 27% (stated by user); profile key `iclr` (scale status: secondary) |
| Venue-Specific Notes | none (ICLR form: Soundness / Presentation / Contribution 1–4, Rating, Confidence) |
| Paper Maturity | Submission-ready (footer reads "Preprint"); no dedicated limitations section |
| Ethics-Relevant Content | none (no human subjects; SaladBench/TruthfulQA are used as evaluation sets only) |

**Integrity scan** (`scripts/integrity_scan.py`): no reviewer-directed text or hidden characters found. Reviewers read the (unchanged) redacted copy.
**Literature check status:** mode *strict*, cutoff 2025-09-24, fingerprint written. Three search attempts hit the arXiv API (one returned HTTP 429, two timed out; one more query was refused for exceeding four concept words). With the API unreachable, Phase 1.5 fell back to *literature check: off*: the Domain Reviewer relies on knowledge, every recommended reference is marked `[verify]`, and no `similarity`, `novelty`, `scout` or `coverage` script output exists.

### Claimed Contributions (as stated by the authors)
1. **C1** – A sample-wise paradigm: count 1→0 transitions as forgetting and 0→1 as backward transfer, because task averages "conflate these effects" (Abstract, §1, §2, App. C.2/Fig. 10).
2. **C2** – Chance-adjusted metrics F_true and BT_true (plus ceilings F_max, BT_max) that "do not need logits or repeated sampling" (§1, §2).
3. **C3** – A large-scale map (~30 model–training combinations, 12 benchmarks, ~100 subdomains in 8–9 categories): domain-continual pretraining, instruction tuning and reasoning SFT/RL from base give low-to-moderate forgetting, with backward transfer in math/logic (§3.1–3.3.1, Figs. 3–5, Tables 2–15).
4. **C4** – Reasoning training from instruct models depends on data scale: low-data gives small effects; high-data gives mixed effects (§3.3.2–3.3.3, Figs. 6–7, Tables 16–23).
5. **C5** – Two-checkpoint model merging "does not reliably mitigate forgetting" (§4, Fig. 8, App. D, Tables 24–35).
6. **C6 (implicit)** – Real post-training pipelines show "far less forgetting" than the continual-learning literature suggests (Table 1 caption; Conclusion).

### Paper memory (factual record shared with all reviewers)
- **Setup:** all evaluated models are public checkpoints; the authors train nothing. LightEval, per-sample logging, zero-shot CoT with a fixed "Answer: $LETTER" format; base models get few-shot CoT "solely to teach the format"; decoding temperature 0.6, top-p 0.95, 32K token cap (4K for Qwen2.5-Math models) (§3 "Experimental setup", App. B.1). Splits: "official evaluation splits" (App. B.2). Categories are built post hoc (App. B.2). Number of runs/seeds: **not stated after search** (the words "seed" and "runs" occur only in unrelated places); the "±" in Tables 2–35 is described only as "standard deviation" (App. E preamble); contamination analysis: **not stated after search**; compute: not stated; code/logs: promised ("will release", §3), while the first-page footnote says they "are available".
- **Headline numbers:** none quantitative in the abstract. The only numeric illustration is the 80%→70% example (§2). Quantitative support is in Tables 2–35 (appendix); the main text has no table of results.
- **Appendix adds:** extended related work (App. A), prompts and category definitions (App. B), prompting comparison (Fig. 9) and conventional-vs-sample-wise comparison (Fig. 10) for one model (App. C), merge failure cases (Figs. 11–16), all numeric tables with ceilings in brackets.
- **Unverifiable:** all figures; qualitative sample inspections are described but not quantified.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Marguerite Okonkwo, senior faculty, large public research university (North America)
- **Seniority / Expertise:** senior faculty / continual learning, LLM evaluation, area chair experience at ICLR-type venues
- **Role:** Reads all five reviews, checks decisive points against the paper, weights reviewers, decides
- **Style:** Judges against what the venue actually accepts; weights reviewers by what they got right

### Reviewer 1 (Methodology): Dr. Anselm Voigtlander, mid-career researcher, evaluation-methodology group at a European research institute
- **Expertise:** LLM benchmark evaluation and answer extraction; statistical reporting for sampled generations
- **Review Focus:** Research design, statistics, comparison fairness, reproducibility
- **Style:** Recomputes every number, insists on noise floors and matched prompts

### Reviewer 2 (Domain): Dr. Linh Thao Verhoeven, senior industry scientist, industrial research lab (Southeast Asia)
- **Expertise:** catastrophic forgetting and continual pretraining of LLMs; model merging
- **Review Focus:** Literature, theoretical framework, domain contribution
- **Style:** Checks every positioning claim against what the cited work says

### Reviewer 3 (Perspective): Dr. Camila Ortega-Lindqvist, associate professor of quantitative psychology/psychometrics, university (South America)
- **Expertise:** item response theory, guessing correction, test reliability; cognitive models of forgetting and retrieval
- **Review Focus:** Cross-disciplinary connections, deployment, assumptions, broader impact
- **Style:** Constructive and expansive; the most positive voice on the panel

### Reviewer 4 (Generalist): Dr. Kwame Abiodun Fairweather, associate professor, university (West Africa)
- **Expertise:** NLP and representation learning (not forgetting specifically)
- **Review Focus:** Contribution clarity, venue fit, presentation
- **Style:** The typical program-committee member; weighs weaknesses against what accepted papers carry

### Devil's Advocate: Dr. Henrik Salonen-Reyes, independent research institute (Northern Europe)
- **Expertise:** causal inference for benchmarking, measurement validity
- **Review Focus:** Core-argument challenges, logic, overclaiming
- **Style:** Rigorous, never hostile; asks what else could produce the same tables

*Personas are fictional. Assumptions: venue ICLR (stated), paper type analysis. Phase 1 passes below were run one after another in one model context (no subagents), so they share a context; independence was kept by writing each report from the paper and the shared paper memory only, without reading the other reports. The literature check (arXiv) could not run, so no reviewer used search results.*

---

## Phase 1: Independent Reviews

# Peer Review Report (Reviewer 1)

## Paper: Mapping Post-Training Forgetting in Language Models at Scale
## Reviewer: Dr. Anselm Voigtlander, Methodology Reviewer (evaluation-methodology group, European research institute; fictional persona)
## Expertise: LLM benchmark evaluation and answer extraction; statistics of sampled generations
## Date: 2026-11-10

## Summary
The paper measures, for ~30 public pre/post checkpoint pairs and 12 multiple-choice benchmarks, the share of items that flip from correct to incorrect (F) or incorrect to correct (BT) after a post-training stage, and subtracts an expected chance-flip term to obtain F_true and BT_true. It groups items into 8–9 post hoc categories and reports that forgetting is "low-to-moderate" in most pipelines, with backward transfer concentrated in math and logic, an unclear data-scale effect for instruct→reasoning training, and no reliable benefit from two-checkpoint merging. Numbers are in Tables 2–35; figures were not available to me.

## Strengths
### S1: Breadth and a numerically transparent appendix
Tables 2–35 report, for every model and category, F or BT with a "±" value and the ceiling F_max/BT_max in brackets (App. E). Showing headroom is a good practice that most forgetting papers skip, and it lets a reader recompute several claims (done below).
### S2: Candid about measurement confounds
The authors state that "much of the backward transfer reflects improved instruction following" (§3.3.1), that results are "highly dependent on the extraction method used" (§3.3.3), and that F_true "need not imply" lost knowledge (§2 "Assumptions and scope"). These caveats are accurate and I treat them as the paper's own findings.
### S3: Per-item logging and a stated release plan
Per-sample logs for every sub-benchmark are promised (§3), which makes the claims checkable and is a real service to the community if delivered.
### S4: A reported negative result with failure cases
Section 4 and App. D show merge failures (Figs. 11–14) rather than hiding them.

## Weaknesses
### W1: The chance-adjusted estimator is not validated and is biased under the paper's own model (E2/E3/E6)
(a) The only worked example is inconsistent with the equations: §2 states that for an 80%→70% drop on a 4-option test "raw forgetting is 10%, but chance-adjusted forgetting is only about 6%". With k=4, F_chance = (1−0.80)/3 × (1−0.70) = 0.020, so F_true = 0.10 − 0.02 = 8%, not about 6% (and F is the flip rate, which is ≥ the net drop). Either the example or the formula used for the tables is different from the stated one.
(b) Under the paper's own know-or-guess-uniformly model, an item known before and lost after is still answered correctly by luck with probability 1/k, so it is recorded as 1→1, not 1→0. The expected observed 1→0 from true loss is therefore only (k−1)/k of the true loss (75% for k=4, 50% for k=2); F_true is not corrected for this, so if the model holds it underestimates true loss by that factor. Separately, the independence assumption (§2, "Assuming independence between pre- and post-training guessing events") fails for items that are hard both before and after (P(post wrong | pre unknown) exceeds 1 − ā_post), which makes F_chance too small and F_true too large. The two biases have opposite signs, so the net sign and size are unknown without a simulation.
(c) The Introduction defines F_true as "among items the model genuinely knew before, what fraction became wrong beyond chance?", a conditional rate, while §2 defines F_true = max(F − F_chance, 0) in units of all N items; the tables report the latter, with F_max beside it. Ratios matter for the scale claims (see W5).
(d) k is not given per sub-benchmark (several BBH tasks are binary; TruthfulQA MC1 and SaladBench "mrq" have different formats), and LLM option choice is known to be non-uniform.
- **Suggested Fix:** Simulate the know/guess process with known true loss and show bias; report F_true/F_max; state k per sub-benchmark; give a paired item-level bootstrap CI. Cost: small (CPU only, <1 day).

### W2: No noise floor and no defined uncertainty (E8)
Decoding uses "temperature 0.6 with nucleus sampling (top_p) of 0.95" with, apparently, one sample per item, so even an unchanged model flips items. The paper says the metric needs no "repeated sampling" (§1) but never measures how large the null flip rate is. The "±" is only "standard deviation" (App. E preamble) with no stated number of runs, seeds or resampling unit. The text uses "significantly more forgetting" for math models (§3.1) without any test, and the clip at zero (§2) biases small values upward. One informative row exists: INTELLECT-2 (from a reasoning model it hardly changes) shows F total 1.3 (Table 16), suggesting the floor may be small for large reasoning models, but this is never presented as a control and may not hold for base/instruct models evaluated few-shot vs zero-shot. The accuracy ceilings for QwQ differ slightly between Tables 14 and 16 (Culture 59.8 vs 60.2; Logic 86.7 vs 87.4), which hints at run-to-run or item-set differences.
- **Suggested Fix:** Re-evaluate each pre-model twice (and with a different seed) to get a null F/BT per category; report F − F_null with item-level bootstrap CIs; state n runs. Cost: roughly one extra evaluation pass per pre-model (~10 pre-models).

### W3: "Forgetting" and "backward transfer" are not separated from elicitation and extraction (E4)
Base models get few-shot CoT while post-trained models get zero-shot CoT plus chat templates (§3 setup, App. B.1), so pre and post differ in prompt as well as weights. Several large "forgetting" results are attributed by the authors to format failure (§3.1 coder answering with code; §3.3.1 Qwen2.5-Math-Instruct "random multi-lingual text"; §3.3.3 code models answering numerically), but the share of unparseable outputs is never reported, and these rows stay in the cross-model comparisons. Backward transfer is, by the authors' own words, mostly instruction following (§3.3.1), which is not knowledge acquisition.
- **Suggested Fix:** Report, per model, the rate of missing/invalid "Answer:" lines; add a log-probability-over-options evaluation with identical prompts for pre and post (no generation); report F/BT on parse-valid items only. Cost: ~1 evaluation pass per pair (a few GPU-hours for 7B, more for 32B).

### W4: Cross-checkpoint comparisons are uncontrolled and some groups are mislabeled (E6)
All checkpoints come from different labs with different data mixes, so statements such as "perhaps due to the breadth of the training datamix" (§3.3.3) are untested. Cross-referencing the ceilings shows two mislabelings: (i) R1-Distill-Qwen (7B) in Table 12 has F_max identical, category by category, to Qwen2.5-Math-Instruct (7B) (59.6, 46.3, 53.9, 55.3, 36.3, 49.5, 43.1), i.e., its reference is the Math model, while §3.3.1 says "different models (Qwen2.5 Base and Llama 8B base)"; (ii) Open Math 2 (8B) sits in the "from instruct, high-data" group (Table 16), yet its F_max column (64.5, 79.1, 42.5, 60.8, …) equals the Llama-3.1 *base* accuracies of Table 4 and Table 12. It also has the largest forgetting in the paper (Total 28.8 of 54.5, i.e. 53% of known knowledge), which then drives the "no dominant factor" conclusion (§3.3.3).
- **Suggested Fix:** Relabel the reference model of every row; for the scale/data claims, train 2–3 small controlled runs (e.g., 3B–7B instruct model, SFT on a fixed reasoning mix at 3 data sizes; roughly 200–500 GPU-hours).

### W5: Category construction is post hoc and some clusters are tiny (E4/E5)
App. B.2: "They are grouped such that (sub-)benchmarks in the same group show similar trends in forgetting and improvement." Grouping by outcome and then reporting group-level trends makes the category findings partly circular. "Culture" consists only of two BBH tasks (sports understanding, movie recommendation), yet it is the headline "spike" (§3.2, §3.3.1); "Knowledge" includes BBH object counting. The scale claim "forgetting decreases as parameters increase" holds for totals (Table 2: 8.5, 8.2, 8.0, 6.7 for 3B–32B) but not for Culture (11.7, 16.5, 14.0, 15.2) or Knowledge/QA (6.8, 15.0, 23.4, 15.3); in Table 3 Culture rises from 15.0 to 19.1.
- **Suggested Fix:** Use a pre-specified taxonomy (e.g., original MMLU supercategories, BBH task families), report per-benchmark numbers with CIs, and state the scale claim per category.

### W6: The merging experiment does not support its conclusion as worded (E4/E6)
Section 4 compares merged models to θ_post (Fig. 8), whereas mitigating forgetting means retaining θ_pre's knowledge. The paper's own relative-to-base table points the other way for small mixes: Qwen2.5-Coder 7B alone has F total 7.6 (F_max 60.4, Table 8) while the Linear (0.2) merge has 6.1 (F_max 58.0, Table 24), with BT 4.8 vs 6.2 (Tables 25, 10). The two totals are not strictly comparable (Table 24 includes a Safety/Truth row that App. B.2 footnote says is excluded when a base model is involved). The α convention is unclear: §4 defines θ(α)=α θ_pre + (1−α) θ_post, yet F relative to base *rises* from α=0.2 to 0.8 (Table 24: 6.1 → 9.3). The OpenThinker merges are reported on MMLU only (Figs. 11, 15, 16; Tables 28–35). Finally, F_max should be identical across columns for one reference model, but is not: Table 32 Knowledge/QA 60.3 (α=0.2) vs 45.0 (α=0.8); Logic 75.2 vs 74.2; Table 28 shows 60.3/75.2 for both columns.
- **Suggested Fix:** Report F and BT of each merge relative to θ_pre alongside θ_post at the same benchmark set, define α, sweep α finely (a curve), include an identical-item guarantee, and add the interpolation baselines from the weight-interpolation literature (see R2). Cost: low (reuse logs).

**Minor:** §3.2 Results says "scaling model size reduces forgetting and increases backward transfer" while Table 5 totals fall (10.5, 11.0, 8.9, 8.2) and the Fig. 4 caption/Key Findings say both decrease; "nine" categories in §3 vs eight rows in Tables 2–15; the text names "OpenCodeReasoner" (§3.3.3) while Tables 17/19 list "Nemotron Code Reasoning"; duplicate bibliography entries (Fernando et al. 2024/2025; Li & Lee 2024a/b; Yıldız et al. 2024/2025); footnote "available" vs "will release".

### Claim-to-Evidence Map
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | Sample-wise counts reveal what task averages hide | Abstract, §1, App. C.2 | Fig. 10 (one model, not available) | Partially: F ≥ net drop by construction (F − BT = acc_pre − acc_post), so "more forgetting" is guaranteed, not a finding |
| C2 | Chance adjustment needs only accuracies and k | §1, §2 | Eqs. in §2 | Partially: worked example off; (k−1)/k attenuation; no validation (W1) |
| C3 | Low-to-moderate forgetting; BT in math/logic | §3.1–3.3.1 | Tables 2–15 | Partially: labels undefined; elicitation confound (W3, W5) |
| C4 | Data-scale dependence | §3.3.2–3.3.3 | Tables 16–23 | Weak: groups mislabeled, models uncontrolled (W4); paper itself says "No single factor" |
| C5 | Merging does not mitigate | §4, App. D | Tables 24–35 | Unsupported as worded (W6) |
| C6 | Far less than CL literature | Table 1 caption | Table 1 vs Tables 2–23 | Unsupported: different models, metrics, no common scale (R2-W2) |

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1/E2 | §2, worked example | "raw forgetting is 10%, but chance-adjusted forgetting is only about 6%" | Eq. in §2 gives F_chance = (0.2/3)(0.3) = 0.02, F_true = 8% | Recomputed from the §2 formulas | High | MAJOR | Correct the example or the formula used |
| ERR-2 | E2/E3 | §2 "A chance baseline for flips" | "Assuming independence between pre- and post-training guessing events" | Known-then-lost items are retained by luck w.p. 1/k, so observed 1→0 from true loss is (k−1)/k of it (attenuation); correlated difficulty biases the other way, so the net bias is unknown | Derived from the paper's own response model | Medium (depends on reading of the model) | MAJOR | Derive the unbiased estimator; simulate |
| ERR-3 | E6 | §1 vs §2 | "among items the model genuinely knew before, what fraction became wrong beyond chance?" | F_true = max(F − F_chance, 0) is a fraction of all N items, not of known items | Cross-referenced §1 and §2, Tables 2–23 | High | MAJOR | State which quantity the tables report; add F_true/F_max |
| ERR-4 | E6/E4 | Table 32 vs Table 28 | "25.7 ±8.0 (60.3)" and "18.0 ±5.2 (45.0)" | Same reference model (Qwen2.5 Instruct) and benchmark, but F_max differs across α columns; Table 28 shows 60.3 in both columns | Cross-referenced two tables | High | MAJOR | Explain item-set differences or fix |
| ERR-5 | E6 | §3.3.1 vs Table 12; Table 16 vs Table 4 | "different models (Qwen2.5 Base and Llama 8B base)" | R1-Distill-Qwen-7B and Open Math 2 have ceilings equal to other reference models | Cross-referenced ceilings column by column; reference identity is inferred | Medium-High | MAJOR | Relabel reference models and groups |
| ERR-6 | E6 | §3.2 Results vs Table 5 | "scaling model size reduces forgetting and increases backward transfer" | Table 5 Total BT: 10.5, 11.0, 8.9, 8.2 (3B→32B) | Read from table | High | MINOR | Correct text |

## Missing References
*Not this reviewer's role (see R2).*

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Metric unvalidated; no noise floor; confounded elicitation |
| Clarity | 2 | Qualitative labels undefined; text–table slips |
| Significance | 2 | Useful map, but conclusions as worded outrun the evidence |
| Originality | 2 | Counting flips is known; chance correction is a modest adaptation |

## Dimension Scores (0–100)
**Pool position:** better than about 40% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the central metric is unvalidated and shows an arithmetic/estimator inconsistency, and no noise floor or prompt-matched control separates forgetting from elicitation; typical rejected-submission signals ("main claim not tested by the experiments").

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 46 | Developing | ERR-1/2/3: example and estimator issues; independence assumption |
| Clarity & Presentation | 58 | Competent | Readable; labels undefined; text–table inconsistencies |
| Novelty & Originality | 52 | Developing | Known idea (per-example flips) applied to LLM post-training; modest chance correction |
| Significance & Impact | 58 | Competent | Timely, public-checkpoint map; conclusions overreach |
| Experimental Validation | 50 | Developing | No null control; mislabeled groups; merging design |
| Reproducibility | 55 | Competent | Prompts and decoding given; seeds/n runs and ± undefined; logs promised only |
| Ethical Compliance | 60 | Competent | Nothing at stake; limitations only inline |

## Questions for Authors
1. What does "±" represent (runs, seeds, resampling), and what is F for the same model evaluated twice? A null F of ≳3 points would change several "low" vs "moderate" calls.
2. Which formula produced the "about 6%" in §2, and is the same one used in the tables?
3. What fraction of outputs lacks a parseable answer for each post-trained model, and do the headline F/BT change when restricted to parse-valid items?
4. What are the reference checkpoints for R1-Distill-Qwen-7B and Open Math 2, and what is the benchmark set behind Table 24 versus Table 8?
5. How is α defined in Tables 24–35, and what are F/BT of the merges relative to θ_pre on the same benchmarks as the post-trained model?

## Limitations Assessment
**Partially.** Confounds are admitted in-line, but there is no limitations section and nothing on contamination, noise or the independence assumption's failure modes.

## Ethics Review Flag
**No.**

## Overall Score
**3**: Borderline Reject. A broad, useful measurement effort whose headline conclusions rest on an unvalidated metric and uncontrolled prompt/extraction effects.

## Confidence
**4**: Recomputed several items; figures unavailable.

---

# Peer Review Report (Reviewer 2)

## Paper: Mapping Post-Training Forgetting in Language Models at Scale
## Reviewer: Dr. Linh Thao Verhoeven, Domain Reviewer (industrial research lab, Southeast Asia; fictional persona)
## Expertise: forgetting and continual pretraining of LLMs; model merging
## Date: 2026-11-10

## Summary
The paper argues that continual-learning results of severe forgetting do not transfer to how modern LLMs are post-trained, and supports this with a measurement study of public checkpoints, using per-item correct→incorrect transitions with a guessing correction. It positions itself against task-level backward transfer (Lopez-Paz & Ranzato, 2017) and surveys prior LLM forgetting studies in Table 1.

## Strengths
### S1: A real gap is identified
Most published LLM forgetting work fine-tunes small models on small tasks (Table 1, App. A); evaluating released reasoning-era checkpoints (s1.1, LIMO, OpenThinker, INTELLECT-2; §3.3) is timely.
### S2: A useful synthesis of prior work
Table 1 and App. A organize CPT / SFT / RL forgetting studies by stage; App. A also covers scale effects (Ramasesh et al.; Luo et al.), which is the right literature for the scale claim.
### S3: Appropriate comparison family for merging
Section 4 connects to interpolation/EMA merging in continual learning (Roth et al. 2024; Yadav et al.) and openly reports surprise that it fails (App. A "Hence, we were quite surprised that model merging does not work…").
### S4: Open about preliminary status
Statements such as "the results here remain preliminary" (§3.3.3) calibrate the claims to the evidence.

## Weaknesses
### W1: Precedent for sample-wise forgetting is under-credited in the positioning
The Introduction presents sample-wise measurement as the alternative to the task level "as proposed by Lopez-Paz & Ranzato (2017)". The work of Toneva et al. (2019) on per-example forgetting events is cited, but only in App. A ("Benchmark paradigm"), not in §1/§2 where the contribution is claimed. Toneva et al. count forgetting events during training of one model rather than between two snapshots, so the delta is real (pre/post stage transitions on LLM benchmarks) but should be stated. Likewise, correction for guessing in multiple-choice scoring is an old psychometric idea; no source is cited for it (see Missing References).
- **Suggested Fix:** State the delta in §1/§2 and cite the psychometric and example-forgetting precedents there.
### W2: Table 1's contrast with the literature is not like-for-like
The caption says "we find far less forgetting when testing widely used post-training pipelines", but Table 1's "Level" (Low/Med/High) is assigned by the authors without criteria, from studies using different models, tasks, metrics and fine-tuning data (e.g., "∼ 2% on MMLU" vs "∼10% MMLU drop"), while the new study evaluates released checkpoints without their data or recipes. The "gap between continual learning setups and how people post-train" (Table 1 caption) is therefore asserted, not measured.
- **Suggested Fix:** Re-run one or two classical setups (e.g., sequential SFT on narrow tasks) with the new metric on the same models, or soften the claim to "in the public checkpoints we examined".
### W3: Related work omits several directly relevant lines
(i) SFT-vs-RL differences in retained generality; (ii) weight interpolation between pre- and post-trained models as a forgetting/robustness remedy (relevant to §4's interpretation: interpolation helps retention in several works, so "surprise" needs more analysis); (iii) evaluation sensitivity to prompt format and option position for MCQ benchmarks (relevant to every F/BT number); (iv) scaling-law treatments of forgetting under fine-tuning. See the list below, all marked `[verify]` because the literature search could not run.
### W4: Merging literature is not engaged at the level of its claims
Section 4 and App. A cite Lin et al. (2024), who frame averaging as a way to recover pre-RLHF abilities, then evaluate merges against θ_post rather than θ_pre, and merge only two checkpoints; the paper itself says prior work "often merges eight or more" and hypothesizes larger weight drift (§4). That is a reasonable explanation, but it makes "does not reliably mitigate forgetting" a statement about this narrow setting.
- **Suggested Fix:** Reword the claim; add a pre-relative analysis.

### Citation check (E7)
- §3.3.3: "OpenCodeReasoner and OpenMath2 (Bercovich et al., 2025)". The cited work is the Llama-Nemotron report in the bibliography; I am not certain it is the source for both checkpoints `[verify]`. The tables name "Nemotron Code Reasoning", not "OpenCodeReasoner".
- Duplicate entries: Fernando et al. (2024) and (2025) are the same arXiv 2410.15483; Li & Lee 2024a/b the same arXiv 2401.03129; Yıldız 2024 (arXiv) and 2025 (TMLR) are one work. Appendix A uses "Yıldız et al. (2025)" while Table 1 uses 2024.
- Table 1 summaries for Fernando et al. and Li et al. agree with the entries' own titles as far as I can tell.

## Missing References
*No literature search results were available (arXiv API unreachable; fallback to knowledge). Every entry is `[verify]`; none is presented as a required comparison.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Important | Chu et al., "SFT Memorizes, RL Generalizes: A Comparative Study of Foundation Model Post-training", ICML 2025 `[verify]` | SFT vs RL effects on retained/generalizing ability; relevant to §3.3 where SFT and RL are pooled |
| Important | Wortsman et al., "Robust fine-tuning of zero-shot models", CVPR 2022 `[verify]` | Interpolating pre- and post-trained weights to retain pre-trained behavior; frames §4 |
| Important | Scialom, Chakrabarty, Muresan, "Fine-tuned Language Models are Continual Learners", EMNLP 2022 `[verify]` | Instruction-tuned LMs and forgetting; direct precedent for §3.2 |
| Important | Ke et al., "Continual Pre-training of Language Models", ICLR 2023 `[verify]` | Domain-continual pretraining forgetting (§3.1) |
| Important | Zheng et al., "Large Language Models Are Not Robust Multiple Choice Selectors", ICLR 2024 `[verify]` | Option-position bias breaks the uniform-guessing assumption of §2 |
| Important | Sclar et al., "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design…", ICLR 2024 `[verify]` | Prompt-format sensitivity; bears on few-shot vs zero-shot pre/post comparison |
| Helpful | Jagielski et al., "Measuring Forgetting of Memorized Training Examples", ICLR 2023 `[verify]` | Per-example forgetting measurement in language models |
| Helpful | Kalajdzievski, "Scaling Laws for Forgetting When Fine-Tuning Large Language Models", arXiv 2024 `[verify]` | Scale and forgetting under fine-tuning |
| Helpful | Shenfeld et al., "RL's Razor: Why Online Reinforcement Learning Forgets Less", arXiv, Sept. 2025 `[verify]` (within ~3 weeks of the cutoff: recent preprint, worth discussing only) | RL vs SFT forgetting |
| Helpful | The psychometric literature on correction for guessing in multiple-choice scoring and on the three-parameter logistic IRT model (guessing parameter): a line of work, no single reference given | Precedent for §2's chance correction |

### Literature-check addendum (strict mode, cutoff 2025-09-24; no script output available)
**Novelty delta table** (built from the paper's own related work and knowledge; uncertain entries marked):
| Claimed contribution | Closest prior work | What it already does | What is new here | Cited and differentiated? |
|---|---|---|---|---|
| C1 sample-wise 1→0 / 0→1 | Toneva et al. 2019 (in bibliography); Lopez-Paz & Ranzato 2017 | Per-example forgetting events during training; task-level backward transfer | Pre/post-stage flip rates for LLM benchmarks | Cited only in App. A |
| C2 chance-adjusted flips | Psychometric guessing correction `[verify]` | Subtracts expected lucky guesses from scores | Applies it to flip rates under an independence assumption | Not cited |
| C3 map of public pipelines | Luo et al. 2025; Kotha et al. 2024; Li & Lee 2024; Li et al. 2025 (all cited) | Fine-tuning forgetting studies, mostly small models or narrow data | Released reasoning-era checkpoints, 12 benchmarks | Cited, partly differentiated |
| C5 merging for forgetting | Lin et al. 2024 (cited) | Model averaging reduces alignment tax | Two-checkpoint merges of released models | Cited; direction partly contradicted |

**Per-claim novelty (claim-level profile, judged by hand, not by `novelty`):** C1 incremental-to-medium; C2 medium; C3 medium-high (new coverage, no new concept); C4 medium; C5 incremental (negative result). No claim is "known"; nothing here supports a criterion-7 issue.
**Baseline scout:** not run. The benchmarks (MMLU, BBH, GPQA, MuSR, ARC, TruthfulQA, HellaSwag, Social IQa, MCTest, PIQA, CommonsenseQA, SaladBench) are used as evaluation sets, not as leaderboard comparisons, so there are no baseline numbers to cross-check.
**Field snapshot (as of the cutoff):** Until 2024, LLM forgetting studies centred on supervised fine-tuning of ≤7B models, with mixed findings (scale raising or lowering forgetting; alignment tax; implicit-inference accounts). During 2025 the post-training stack shifted to long-chain reasoning via distillation SFT and RL with verifiable rewards, and open checkpoints (s1.1, LIMO, OpenThinker, INTELLECT-2) became widely available; work on forgetting there is early (temporal forgetting, early RL-vs-SFT comparisons). A significant contribution now would be a validated, reusable measurement plus controlled evidence about which factors (data scale, objective, mixture) drive forgetting; broad descriptive coverage of released checkpoints is useful but is not by itself a strong result. I used this to calibrate Significance and Novelty.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Positioning claims (Table 1) not like-for-like |
| Clarity | 3 | Related work readable; some duplicate/mismatched citations |
| Significance | 3 | Timely descriptive map |
| Originality | 2 | Incremental metric; new coverage, not new concept |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: genuine but descriptive contribution with incremental methods; central positioning claim unsupported by like-for-like evidence. Borderline-reject side.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Positioning evidence weak; merging framing |
| Clarity & Presentation | 62 | Competent | Related work well organized |
| Novelty & Originality | 52 | Developing | Per-example flips and guessing correction have precedent; coverage is new |
| Significance & Impact | 60 | Competent | Useful reference map for practitioners |
| Experimental Validation | 52 | Developing | No common-scale comparison with prior studies |
| Reproducibility | 58 | Competent | Logs promised |
| Ethical Compliance | 62 | Competent | Nothing at stake |

## Questions for Authors
1. Can the new metric be applied to a classical sequential-fine-tuning setup so Table 1's contrast is measured on one scale? A "yes, and forgetting is still much smaller" would raise my score.
2. How does your delta relate to Toneva et al. (2019), and was a psychometric guessing correction considered?
3. For merging, are results relative to θ_pre consistent with the literature that finds interpolation retains pre-trained behavior?

## Limitations Assessment
**Partially.** Scope ("public checkpoints", "two checkpoints") is not carried into the headline wording.

## Ethics Review Flag
**No.**

## Overall Score
**3**: Borderline Reject. Interesting and timely, with a positioning claim that the evidence does not yet carry.

## Confidence
**4**: Know the forgetting/merging literature; literature search unavailable, so some entries are `[verify]`.

---

# Peer Review Report (Reviewer 3)

## Paper: Mapping Post-Training Forgetting in Language Models at Scale
## Reviewer: Dr. Camila Ortega-Lindqvist, Perspective Reviewer (quantitative psychology/psychometrics; university, South America; fictional persona)
## Expertise: item response theory; test reliability; cognitive models of forgetting and retrieval
## Date: 2026-11-10

## Summary
The paper asks whether the post-training stages that make LMs useful erase the factual and reasoning knowledge acquired in pretraining, and answers by comparing each model's item-by-item correctness before and after, with a correction for lucky guesses on multiple-choice items. Its message is that, in the public checkpoints studied, forgetting is modest and often outweighed by gains in math and logic, and that simple weight-interpolation does not rescue the rest.

## Strengths
### S1: The item-level view matches how knowledge is actually tested
Treating each question as a distinct unit, rather than averaging them (§1), is the standard stance of test theory and is right for "knowledge" (as the president/NumPy examples show).
### S2: Headroom is made visible
Reporting F_max/BT_max (§2; brackets in Tables 2–35) is similar in spirit to reliability ceilings in psychometrics and prevents misreading tiny F values in low-accuracy categories.
### S3: Practitioner-relevant framing
The question "does scaling post-training erode breadth of knowledge" (§1) matters for anyone iterating through multi-stage pipelines, and the finding that the effect depends on the recipe (Table 16: INTELLECT-2 F 1.3 vs Open Math 2 F 28.8) is actionable.
### S4: Honest about storage vs elicitation
§2 notes that F_true "could quantify failure to elicit previously accessible knowledge", which is the right conceptual caveat.

## Weaknesses (opportunities)
### W1: The guessing model could borrow from item response theory
Psychometrics models guessing with a per-item "pseudo-guessing" parameter alongside item difficulty, rather than a uniform, independent guess (§2: "it guesses uniformly at random"). Items that are hard before are hard after, so the independence of pre and post guesses is unlikely, and LLMs have systematic option preferences. Fitting a simple 3-parameter model over many models, or using several models as "test-takers", could estimate per-item difficulty and guessing and give calibrated, uncertainty-aware flip rates.
- **Suggested Fix:** Fit a 2PL/3PL model across the evaluated checkpoints and compare its implied chance-flip rate with the §2 closed form.
### W2: Retrieval failure versus loss is the central conceptual question and is not tested
Cognitive models separate storage from retrieval; the paper acknowledges the distinction (§2) but the evaluation (generated CoT with answer extraction) mixes both. Option log-likelihood scoring, answer-prefix probing, or cloze-style evaluation would test whether the "forgotten" items are still recoverable.
- **Suggested Fix:** A 3B–7B subset with logit-based scoring and with a few-shot rescue prompt for the post-trained model; report the fraction of 1→0 items that become correct again.
### W3: Coverage gaps relative to the motivation
The Introduction motivates the study with "coding, math, tool use and safety", but tool use and coding ability are not evaluated; safety appears only as a category in Tables 16–23 (SaladBench, TruthfulQA, moral-scenario subsets of MMLU) with no discussion in the text. Forgetting of safety behavior is arguably the most consequential case.
- **Suggested Fix:** Discuss the Safety/Truth rows explicitly and add one capability (code execution or tool-call) evaluation.
### W4: The closing recommendations are untested
The Conclusion lists three mitigation directions (penalizing 1→0 transitions, synthetic repair corpora, retrieval). They are plausible but come with no experiment, so they should be framed as hypotheses.

### Assumption Audit
(1) Uniform, independent guessing (§2); (2) benchmark items stand for "pretraining knowledge", although BBH "logic" and "math" clusters are mostly reasoning skills (App. B.2); (3) one decoding configuration (T=0.6, single sample) is representative for base, instruct and reasoning models alike. Scale assumption: conclusions on 3B–32B models may not carry to frontier-scale pipelines.

### Broader impact and ethics
No human data and no deployment risk; the safety rows deserve a sentence on what they imply for alignment retention. Limitations are discussed inline only.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound intent; assumptions need validation |
| Clarity | 3 | Clear framing |
| Significance | 3 | Useful to practitioners |
| Originality | 3 | Fresh combination of ideas from test theory and continual learning |

## Dimension Scores (0–100)
**Pool position:** better than about 65% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a timely, broad empirical map whose practical message (forgetting is modest in current practice) is valuable if the measurement holds; weaknesses are of the kind many accepted analysis papers carry.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Assumptions untested but acknowledged |
| Clarity & Presentation | 66 | Competent | Readable and well framed |
| Novelty & Originality | 60 | Competent | New combination, modest technical novelty |
| Significance & Impact | 70 | Competent | A clear practical takeaway for post-training pipelines |
| Experimental Validation | 60 | Competent | Breadth strong, controls thin |
| Reproducibility | 62 | Competent | Settings stated, logs promised |
| Ethical Compliance | 68 | Competent | Nothing at stake; limitations inline |

## Questions for Authors
1. How many of the 1→0 items become correct under option-likelihood scoring? A high share would show the effect is elicitation, which would change how practitioners should read the paper.
2. How stable are the per-item flips across repeated sampling (test–retest reliability)?
3. Why is tool use/safety behavior not evaluated given the §1 motivation?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**4**: Borderline Accept. The strong evidence that forgetting is modest under current practice, together with a practical, reusable measurement view, outweighs the open validity questions for me, though these are real.

## Confidence
**3**: I read the methods and appendix tables; I am less familiar with the LLM post-training checkpoints themselves.

---

# Peer Review Report (Reviewer 4)

## Paper: Mapping Post-Training Forgetting in Language Models at Scale
## Reviewer: Dr. Kwame Abiodun Fairweather, Generalist Reviewer (university, West Africa; fictional persona)
## Expertise: NLP and representation learning
## Date: 2026-11-10

## Summary
The paper contributes a way to count and chance-correct per-question changes after post-training and a large evaluation of public checkpoints across domain pretraining, instruction tuning, reasoning SFT/RL and merging. The community takeaway is that forgetting under current recipes is low-to-moderate, that math/logic benefit, and that mitigation by simple merging is not reliable.

## Strengths
### S1: Relevant to ICLR's audience
Understanding what post-training does to existing capabilities is of broad interest, and the study spans several model families and sizes (§3, Tables 2–23).
### S2: Clear problem statement and visuals as described
The four-quadrant view (Fig. 1) and the takeaway boxes in each subsection make the narrative easy to follow, and Table 1 is a helpful orienting summary.
### S3: Transparent numbers and ceilings in the appendix
Every figure has a numeric counterpart with ceilings (App. E), which lets readers check magnitudes.
### S4: Honest about unclear results
"No single factor robustly explains the dynamics" (§3.3.3) and the merging caveats are stated plainly rather than spun.

## Venue Criteria Checklist (ICLR 2026 form)
| Criterion | Grade | Location |
|-----------|-------|----------|
| Soundness (claims supported by evidence) | Partly | §3 claims vs W2 below; metric validity open |
| Presentation | Partly | Clear structure; undefined qualitative labels; text–table slips |
| Contribution (new, useful finding or tool) | Partly | Useful map; metric is incremental; no new method |
| Reproducibility | Partly | Prompts/decoding stated; logs "will release" |
| Honest limitations | Partly | In-line only; no section |

## Weaknesses
### W1: The main findings are expressed in undefined qualitative bins
"Low", "moderate", "large", "minimal" are used throughout (Abstract; §3.1–3.3; Key Findings) with no thresholds, and Table 1 assigns Low/Med/High to prior work with no criteria. Abstract item (3) says effects "are mixed and warrant further study with better controls", which is a non-finding; item (4) is "does not reliably mitigate". A reader cannot tell what number counts as "moderate" (e.g., Table 2's Culture 11.7–16.5 out of ceilings of 55.8–78.9 vs Table 16's Open Math 2 Total 28.8).
- **Suggested Fix:** Define bins relative to F_max (e.g., <5%, 5–20%, >20% of known knowledge) and tabulate the main-text results.
### W2: Text, captions and tables disagree in places
§3.2 Results ("scaling model size reduces forgetting and increases backward transfer") disagrees with its own Takeaway and Fig. 4 caption and with Table 5; "nine" groups (§3) vs eight rows in Tables 2–15; "OpenCodeReasoner" (§3.3.3) vs "Nemotron Code Reasoning" (Tables 17, 19). With figures carrying all main-text evidence and no main-text table, these slips are hard to catch and erode trust.
- **Suggested Fix:** Add one compact main-text table (per pipeline: F_true, BT_true, ceilings, with CIs) and reconcile text with Tables 2–23.
### W3: The "practical yardstick" is not demonstrated to change a conclusion
The abstract promises "a practical yardstick", but App. C.2/Fig. 10 compares the new metric with the conventional one for one model only, and sample-wise F is ≥ the net accuracy drop by construction, so "more forgetting is uncovered" does not show that conventional metrics mislead. A case where conventional and sample-wise views rank two pipelines differently would justify the contribution.
- **Suggested Fix:** Show rank disagreements across the 30 combinations and an example where net accuracy hides a clear loss.

**Minor:** typographical issues ("adhearance", "elicted"); duplicated bibliography entries; footnote "available" vs "will release".

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Broad; some unresolved validity points |
| Clarity | 3 | Readable, but labels undefined |
| Significance | 3 | Of interest to the post-training community |
| Originality | 2 | Metric incremental |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear, broad and relevant study whose weaknesses (qualitative bins, text slips, modest method novelty) are of the kind accepted analysis papers commonly carry.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Sound at the level a PC member can check |
| Clarity & Presentation | 64 | Competent | Clear narrative; qualitative bins and slips |
| Novelty & Originality | 58 | Competent | Incremental metric, new coverage |
| Significance & Impact | 66 | Competent | Relevant to many practitioners |
| Experimental Validation | 60 | Competent | Broad, but controls thin |
| Reproducibility | 62 | Competent | Details present |
| Ethical Compliance | 64 | Competent | Nothing at stake |

## Questions for Authors
1. How do you define "low/moderate/high", and do they depend on F_max?
2. In which comparisons does the sample-wise metric change a ranking relative to the net accuracy change?
3. Will the logs and code be available at review time?

## Limitations Assessment
**Partially.** A short limitations section on metric assumptions and checkpoint selection is needed.

## Ethics Review Flag
**No.**

## Overall Score
**4**: Borderline Accept. A clear, relevant empirical study that the community would read, with fixable presentation and validity issues.

## Confidence
**4**

---

# Devil's Advocate Report

## Paper: Mapping Post-Training Forgetting in Language Models at Scale
## Reviewer: Dr. Henrik Salonen-Reyes, Devil's Advocate (independent research institute, Northern Europe; fictional persona)

## Steelman
Evaluating publicly released checkpoints at item level, with ceilings and chance correction, gives the first broad picture of what happens to pretrained knowledge across current post-training recipes, and shows that the dramatic forgetting predicted by classical continual learning is rare in those recipes. The authors disclose the main measurement caveats themselves.

## Core Argument Chain
1. Counting per-item 1→0 / 0→1 flips measures forgetting / backward transfer better than task averages (C1).
2. Subtracting expected chance flips isolates genuine knowledge change (C2).
3. Applied to ~30 released checkpoint pairs, flips are low-to-moderate in most pipelines (C3).
4. Therefore sequential post-training "does not automatically erode pre-training knowledge" and continual-learning forgetting results do not describe practice (C6).

## Strongest Counter-Argument
Even if the metric were perfect, premise 3 does not license conclusion 4. The sample is a set of **released** checkpoints, i.e., survivors: labs choose data mixtures, replay general data and discard recipes that visibly damage general benchmarks before release. The study therefore measures forgetting under pipelines already engineered against it, and says nothing about whether sequential training erodes knowledge "automatically"; the one counterfactual family where the recipe is narrow (Open Math 2, Nemotron code, Qwen2.5-Math-Instruct) shows the largest losses (e.g., Table 16 Total 28.8 of a 54.5 ceiling, or 53% of known knowledge), and these are explained away as extraction artifacts (§3.3.1, §3.3.3) without quantifying how much of the effect is artifact. The explanation is asymmetric: artifacts are invoked where forgetting is large; no equally targeted check is made where forgetting is small, although several mechanisms deflate F: a lost item still lands on the right option with probability 1/k (an attenuation of F_true by (k−1)/k under the paper's own model, ERR-2, whose size relative to the opposing bias from correlated difficulty is unknown), a reasoning model may have seen benchmark-like items in its post-training data, and the clip at zero hides negative drift. Backward transfer, in turn, is mostly improved instruction following (§3.3.1), so the pair "forgetting vs backward transfer" is "format cost vs format benefit", not "knowledge lost vs knowledge gained". The comparison with prior literature (Table 1) uses different models, tasks and metrics, with author-assigned Low/Med/High, so "far less forgetting" is not measured. The authors can answer by narrowing the claim ("in the released checkpoints we examined, under CoT-MCQ evaluation") and adding a null-F and a prompt-matched evaluation; as worded, the conclusion overreaches. (This is MAJOR, not CRITICAL: the evidence supports the narrower claim.)

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The central descriptive claim survives in narrower form (released checkpoints, CoT-MCQ evaluation); no leakage, selection on a reported test split, or contradiction of the main claim by the paper's own results was found in the protocol sweep (below).

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Scope (selection of checkpoints) | Conclusion; §3 setup; Table 1 caption | "sequential training does not automatically erode pre-training knowledge" generalizes from released, engineered pipelines (E5 claim distortion) | Narrow wording; add controlled runs with a narrow vs mixed data recipe |
| DA-M2 | Evidence | §3.3.1, §3.3.3; App. B.1 | Large forgetting is attributed to format failure without quantification; BT is "improved instruction following"; pre/post prompts differ | Report parse-failure rates; matched-prompt and log-probability evaluation |
| DA-M3 | Logic | Table 1 caption; Conclusion | "far less forgetting" compares unlike setups with undefined levels | Common-scale re-run of a classical setup or soften |
| DA-M4 | Alternative explanation | §3.3 models; no section | No contamination or training-data overlap analysis; post-training data of reasoning models may contain benchmark-like items (deflates F, inflates BT) | Report overlap checks or evaluate on post-cutoff items |
| DA-M5 | Evidence | App. B.2; §3.1 | Categories built post hoc from outcomes ("grouped such that…show similar trends"); "significantly more forgetting" for math models without a test; Culture = 2 BBH tasks | Pre-specified taxonomy; CIs; per-benchmark tables |
| DA-M6 | Evidence | §4; Tables 24–35 | Merge claim measured against θ_post, ambiguous α, differing F_max across columns, MMLU-only for two merges | Redo relative to θ_pre with an α sweep |
| DA-M7 | Logic | §3.3.2–3.3.3; Tables 16–23 | Data-scale effect confounded with family, teacher and objective; text concedes "No single factor"; one "from-instruct" row has a base-model reference (ERR-5) | Controlled data-scale runs; relabel |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Presentation | §3.2 Results vs Table 5 | "increases backward transfer" contradicts Table 5 totals |
| DA-m2 | Presentation | Bibliography | Duplicate entries (Fernando 2024/2025; Li & Lee 2024a/b; Yıldız 2024/2025) |
| DA-m3 | Consistency | §3 vs Tables 2–15 | "nine" groups vs eight rows |

### Protocol sweep
No train/validation/test selection occurs (all checkpoints are public; "official evaluation splits", App. B.2). The only selection on results is the category grouping (App. B.2), which affects aggregation, not a tuned configuration; DA-M5. Not criterion 3.

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| §2 example: 80%→70%, k=4, F_true | "about 6%" | F_chance = (0.2/3)·0.3 = 0.02; F_true = 0.10 − 0.02 = 8% | **No** |
| Scale effect on total F, Q2.5 Inst. (Table 2) 3B→32B | 8.5, 8.2, 8.0, 6.7 (F_max 50.2→72.3) | F/F_max = 16.9%, 14.0%, 11.5%, 9.3% | Decreasing; stronger in relative terms |
| Scale effect, Culture (Table 2) | "forgetting decreases with scale" | 11.7, 16.5, 14.0, 15.2 | **No** (non-monotone/rising) |
| Open Math 2 share of known knowledge lost (Table 16) | Total 28.8 (54.5) | 28.8/54.5 = 52.8% | Large; not "low-to-moderate" |
| Merge vs post, Coder 7B, F total | Table 8: 7.6 (60.4); Table 24 Linear 0.2: 6.1 (58.0) | 12.6% vs 10.5% of ceiling | Merge lower; different benchmark sets |

## Ignored Alternative Explanations
Sampling noise at T=0.6 (no null F); answer-extraction failures; prompt differences between pre and post; option-position bias; selection of released checkpoints; benchmark overlap with post-training data; heterogeneous k across sub-benchmarks; CoT length caps (4K for Qwen2.5-Math).

## Missing Stakeholder Perspectives
Practitioners who care about forgetting of tool use, safety refusals and long-tail languages (not evaluated; Safety/Truth rows not discussed); users of small models where knowledge capacity is tight.

## Observations (Non-Defects)
Ceilings (F_max/BT_max) reported for every cell; failure cases for merging are shown; INTELLECT-2 (F 1.3, Table 16) incidentally acts as a near-null reference and suggests that the floor can be small, which, if made explicit, would strengthen the paper.

## Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: main conclusions are worded beyond what a validated, controlled evidence base supports.

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 44 | ERR-1/2/3; independence assumption; no null |
| Clarity & Presentation | 58 | Readable; undefined bins; slips |
| Novelty & Originality | 48 | Incremental |
| Significance & Impact | 56 | Useful if narrowed |
| Experimental Validation | 46 | Confounded and uncontrolled |
| Reproducibility | 54 | Logs promised only; ± undefined |
| Ethical Compliance | 60 | Nothing at stake |

## Overall: 3 | Confidence: 4

---

## Phase 1.5 / 1.6

**Literature check:** strict mode requested; the arXiv API was unreachable (HTTP 429, two timeouts), so zero queries completed (1 refused for length). The Domain Reviewer's addendum above is knowledge-based with `[verify]` markers; no labels (prior/recent/concurrent) could be computed, so nothing counts as a required comparison.

### Report check (Phase 1.6; scores unchanged)
| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R2 | "Toneva et al. is not cited" | rewritten | The paper cites it in App. A; the real point is that §1/§2 do not credit it |
| R3 | "No safety evaluation" | dropped, replaced by W3 | SaladBench/TruthfulQA are in the Safety/Truth rows; the gap is the lack of discussion |
| R4 | "Derivation of F_chance missing" | dropped | §2 derives it; the valid points are in R1-W1 |
| R1 | "Merging reduces forgetting" (stated flatly) | rewritten as W6 | Table 24 vs Table 8 totals use different benchmark sets; reframed as unsupported conclusion and question |
| R3 | "No limitations section" | moved to Limitations/Minor | Caveats exist in-line (§2, §3.3.3, §4) |
| R1 | Typos, duplicate bibliography entries | moved to Minor | Cosmetic |
| DA | Contamination (DA-M4) | kept | Search for "contamin" finds nothing in the paper |
| R2 | OpenCodeReasoner citation mismatch | rewritten as a `[verify]` question | Not certain the cited report is the wrong source |

---

## Phase 2: Synthesizer (Part A) and EIC Meta-Review

### Master issue list and consensus map
| Issue | Sources | Class |
|-------|---------|-------|
| I1 Metric validity (example, (k−1)/k bias, independence, definition mismatch) | R1-W1, R3-W1, R2-W1 (psychometric precedent), DA-M2 (partly) | CONSENSUS-3 |
| I2 Elicitation / prompt / extraction confound; BT = instruction following | R1-W3, R3-W2, DA-M2 | CONSENSUS-3 |
| I3 No noise floor; ± undefined | R1-W2, DA (alt. explanations), R3 Q2 | CONSENSUS-2 |
| I4 Table 1 / "far less forgetting" not like-for-like; overgeneralization from released checkpoints | R2-W2, DA-M1, DA-M3, R4-W1 (undefined bins) | CONSENSUS-3 |
| I5 Uncontrolled comparisons, mislabeled groups, data-scale | R1-W4, DA-M7, DA-M1 | CONSENSUS-2 |
| I6 Category construction and small clusters | R1-W5, DA-M5 | CONSENSUS-2 |
| I7 Merging conclusion | R1-W6, R2-W4, DA-M6 | CONSENSUS-3 |
| I8 Qualitative bins undefined | R4-W1, DA-M5 | CONSENSUS-2 |
| I9 Novelty/positioning of sample-wise metric | R2-W1, R4-W3 | CONSENSUS-2 |
| I10 Contamination | DA-M4 | SOLO |
| I11 Safety/tool-use coverage; untested recommendations | R3-W3, R3-W4 | SOLO |
| I12 Text–table inconsistencies | R1 Minor, R4-W2, DA-m1/m3 | CONSENSUS-3 (minor) |
| SPLIT: practical value of the headline ("modest forgetting is a useful correction") | R3 for; DA, R1 against | SPLIT |
DA-CRITICAL: none raised. Issues the outcome may hinge on: I1, I2, I3, I4.

**Official score (BEFORE run, `scores_before.json`, `da_critical: []`):** official rating 3.40 (R1 3, R2 3, R3 4, R4 4, DA 3); official composite 56.5; suggested Overall 3; no warnings; spreads all ≤ 16 (none flagged).

---

# Editorial Decision

## Paper: Mapping Post-Training Forgetting in Language Models at Scale
## Submission ID: iclr26-qCIg2WGudx (evaluation id)
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: analysis
## Review Team (fictional personas): EIC (meta-reviewer) Prof. Marguerite Okonkwo; R1 Methodology Dr. Voigtlander; R2 Domain Dr. Verhoeven; R3 Perspective Dr. Ortega-Lindqvist; R4 Generalist Dr. Fairweather; DA Dr. Salonen-Reyes

---

## Decision: Borderline Reject (3)   *(ICLR rating label: "4" on {0,2,4,6,8,10}; "5" on {1,3,5,6,8,10}; scale status: secondary)*

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 4, DA 3 → mean 3.40 · official composite 56.5
**EIC assessment** (internal): weighted rating 3.32 → starting point 3 · weighted composite 55.6 → band 3 (agrees with rating; no ⚠) · **DA ceiling**: none · **Final (EIC)**: 3
**EIC pool position:** better than about 50% of submissions (accepted ≈ 27%)

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A timely, broad measurement of released post-training checkpoints (about 30 model–training combinations, 12 benchmarks), with ceilings reported in every cell, candid caveats, and a negative merging result. The per-item framing is sensible, and the descriptive message (recipes matter; INTELLECT-2 changes almost nothing while Open Math 2 loses over half of what it knew) is useful to practitioners. Weaknesses such as no seeds or undefined bins are of a kind accepted analysis papers often carry.
- **Against acceptance:** The central claim (current pipelines erode far less than continual-learning results suggest) rests on a metric whose only worked example is inconsistent with its formula, whose estimator is biased under its own model, and which has no null control, no matched-prompt evaluation and no like-for-like comparison with the literature; the checkpoints are uncontrolled survivors, a group is mislabeled, and the merging conclusion is measured in the wrong direction. The main novelty (per-item flips, guessing correction) has precedent that is credited only in an appendix.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| 80%→70% example gives 8%, not "about 6%" | R1 ERR-1, DA numeric check | §2 | **Verified** | F_chance = (0.2/3)(0.3) = 0.02; text says 6% |
| F_true attenuated by (k−1)/k under the paper's own model; independence failure biases the other way (net sign unknown) | R1 ERR-2, DA | §2 | **Verified** (derivation) | Depends on reading the response model as stated; assumptions (i)/(ii) quoted in §2 |
| §1 defines F_true as a conditional rate; §2 as a share of N | R1 ERR-3 | §1, §2 | **Verified** | Tables follow §2 |
| No null/noise control; "±" undefined; seeds not stated | R1-W2, DA | §3 setup, App. B.1, App. E | **Verified** | Text search finds no seeds/runs; INTELLECT-2 row (Table 16) is an informal floor |
| F_max differs across α columns for one reference model | R1 ERR-4 | Tables 28 vs 32; Table 24 | **Verified** | e.g., 60.3 vs 45.0 |
| R1-Distill-Qwen-7B / Open Math 2 reference identities differ from the text/group | R1 ERR-5, DA-M7 | §3.3.1; Tables 12, 16, 4 | **Partly correct** | Ceilings match other models exactly; identity is inferred, not stated |
| Merging reduces F relative to base at α=0.2 (6.1 vs 7.6) | R1-W6, DA table | Tables 24, 8 | **Partly correct** | Benchmark sets differ (Safety/Truth row); the conclusion is at least unsupported |
| "Forgetting decreases with scale" | R1-W5, DA | Tables 2, 3 | **Partly correct** | True for totals and relative to ceilings; false for Culture, Knowledge |
| §3.2 text vs Table 5 on BT scaling | R1, R4, DA | §3.2, Table 5 | **Verified** | Minor |
| Sample-wise F ≥ net drop by construction, so Fig. 10 shows no discovery | R1 map, R4-W3, DA | App. C.2 | **Verified** | F − BT = acc_pre − acc_post |
| Categories built from outcomes | R1-W5, DA-M5 | App. B.2 | **Verified** (quote present) | |
| No contamination analysis | DA-M4 | whole paper | **Verified** | Search finds nothing |
| Toneva et al. credited only in App. A | R2-W1 | §1; App. A | **Verified** | Delta (pre/post flips vs training-time events) is real |
| R3: "strong evidence that forgetting is modest under current practice" | R3 | §3; Tables 2–23; Table 16 | **Overstated** | Metric unvalidated; Table 16 shows Open Math 2 losing 52.8% of known items |
| R2: OpenCodeReasoner citation | R2 | §3.3.3 | Unverified | Kept as a question |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Error-log items ERR-1, 3, 4, 6 verified exactly; ERR-2/5 verified with stated caveat; decisive for the outcome; calibration fits ICLR |
| R2 (Domain) | 3 | 4 | 1.0 | Mostly verified; Table 1 point sound; citation point left unverified |
| R3 (Persp.) | 4 | 3 | 0.75 | Useful psychometric and storage/elicitation points, but the headline "strong evidence" is overstated against Table 16 and the unvalidated metric; pool position 65 not consistent with the open validity questions |
| R4 (Generalist) | 4 | 4 | 1.0 | Sound, typical PC review; presentation points verified |
| DA | 3 | 4 | 1.25 | Counter-argument (selection of released checkpoints, asymmetric artifact reasoning) and numeric checks verified; correctly refrained from CRITICAL |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | n/a | n/a |

I checked the DA's strongest objection against the criteria independently: the evidence supports a narrower claim, so it is MAJOR, not CRITICAL (no leakage; no contradiction of the main claim; the experiment can test the narrower, descriptive claim).

### Final Decision and Justification
The reviewers' recommendations give an EIC-weighted rating of 3.32 (official mean 3.40), starting point 3; the weighted composite is 55.6, also band 3, so the two signals agree and I keep the starting point. No DA ceiling applies. What decides it: the paper's own headline (current pipelines forget much less than the literature suggests) is a comparative claim on a new measurement, and three verified issues are not accounted for in the more favorable ratings (R3, R4): the unvalidated and arithmetically inconsistent estimator (ERR-1/2/3), the absence of a null control and of a prompt-matched evaluation (the paper's own text says backward transfer is mostly instruction following), and the unmeasured comparison with prior work (Table 1). Against that, the empirical map is useful and honest and most of these gaps can be closed with existing logs (null F, bootstrap CIs, parse-valid subsets, pre-relative merge analysis) and some small controlled runs, so this is a borderline rather than a clear reject. My pool position is about 50: below the typical accepted analysis paper because the central measurement is not yet validated, but not at the low end because the data are broad and the authors are candid. The final decision, 3, does not exceed the (absent) ceiling. This is a simulation of how a careful panel might see the draft, not a prediction.

---

## Score Summary

### Official Scores and EIC Assessment
| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 46 | 52 | 60 | 60 | 44 | 52.4 | 51.1 | 16 |
| Clarity & Presentation | 58 | 62 | 66 | 64 | 58 | 61.6 | 60.9 | 8 |
| Novelty & Originality | 52 | 52 | 60 | 58 | 48 | 54.0 | 53.2 | 12 |
| Significance & Impact | 58 | 60 | 70 | 66 | 56 | 62.0 | 60.9 | 14 |
| Experimental Validation | 50 | 52 | 60 | 60 | 46 | 53.6 | 52.6 | 14 |
| Reproducibility | 55 | 58 | 62 | 62 | 54 | 58.2 | 57.6 | 8 |
| Ethical Compliance | 60 | 62 | 68 | 64 | 60 | 62.8 | 62.1 | 8 |
| **Composite** | 52.6 | 55.4 | 63.1 | 61.5 | 50.2 | **56.5 (before)** | **55.6 (after)** | |

Reviewer weight shares (confidence × EIC weight): R1 0.244, R2 0.195, R3 0.121, R4 0.195, DA 0.244.

### Target-Venue Scores (ICLR, scale status: secondary; heuristic, not official wording)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 2 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) |
| Venue composite | 55.4 |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Mapping Post-Training Forgetting in Language Models at Scale" to ICLR. The question of what post-training does to pretrained knowledge is important, and a broad look at released reasoning-era checkpoints is welcome.

**Overall Assessment:** The panel valued the breadth of the study, the ceilings reported in every cell, and your candor about elicitation and extraction confounds. It also found that the central comparative conclusion is not yet supported at the level of the wording, mainly because the metric has not been validated and the pre/post comparison is not separated from prompt and extraction effects. The decision is Borderline Reject (3).

**Key Strengths Identified by Reviewers:**
1. A broad, transparent measurement of about 30 checkpoint pairs with per-cell ceilings (R1, R3, R4).
2. A timely question and a useful per-item framing, with honest caveats (R2, R3, R4).
3. A reported negative result on merging with failure cases (R1, R2).

**Key Concerns Requiring Attention:**
1. Metric validity and noise: the worked example (§2) gives 8%, not 6%; F_true is biased under your own model; no null F or CIs (R1, R3, DA; CONSENSUS-3).
2. Elicitation/prompt/extraction confound and instruction-following as "backward transfer" (R1, R3, DA; CONSENSUS-3).
3. The comparison with prior literature (Table 1) and the generalization from released checkpoints are not like-for-like (R2, DA, R4; CONSENSUS-3).

**Decision: Borderline Reject (3)**

Closing these gaps requires mostly re-analysis of existing logs plus a few small controlled runs. A revision that narrows the claims, validates the estimator, reports a null control and prompt-matched results, fixes the merging analysis and relabels the mislabeled groups would make this a solid analysis paper.

Please refer to the Revision Roadmap below.

Sincerely,
Prof. Marguerite Okonkwo, Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Metric validity (example, bias, independence, definition) | R1, R3, R2 (+DA) | CONSENSUS-3 |
| Elicitation / prompt / extraction confound | R1, R3, DA | CONSENSUS-3 |
| Table 1 and generalization claim | R2, DA, R4 | CONSENSUS-3 |
| Merging conclusion | R1, R2, DA | CONSENSUS-3 |
| Text–table inconsistencies | R1, R4, DA | CONSENSUS-3 (minor) |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| The headline "forgetting is modest in current practice" is a useful, established correction | R3 (strong), R4 | R1, DA, R2 | Established only for the examined released checkpoints and only if the metric holds; Table 16 shows a large loss for one recipe. Overstated as worded. |

### Score Spread Discussion
No dimension exceeds the 20-point spread (max 16, Technical Rigor: R3/R4 at 60 vs DA 44). The EIC adopts the lower view for Technical Rigor because ERR-1/2/3 were verified.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Survivorship of released checkpoints vs "does not automatically erode" | R2 partly | n/a | Narrow wording / controlled runs |
| DA-M2 | MAJOR | Elicitation vs forgetting, asymmetric artifact reasoning | Yes (R1, R3) | n/a | Matched prompts, parse rates |
| DA-M3 | MAJOR | Table 1 not like-for-like | Yes (R2) | n/a | Common-scale re-run or soften |
| DA-M4 | MAJOR | Contamination not examined | No | n/a | Overlap check |
| DA-M5 | MAJOR | Post hoc categories; "significantly" without test | Yes (R1, R4) | n/a | Pre-specified taxonomy, CIs |
| DA-M6 | MAJOR | Merging analysis | Yes (R1, R2) | n/a | Pre-relative analysis |
| DA-M7 | MAJOR | Data-scale confounds and mislabeled groups | Yes (R1) | n/a | Relabel; controlled runs |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*No DA-CRITICAL issue was upheld; these are issues the EIC verified as undermining a main claim.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Estimator validity: correct the 6%/8% example, derive an unbiased estimator (k−1)/k, state F_true definition, k per sub-benchmark | R1-W1 (ERR-1/2/3), R3-W1 | §1, §2, Tables 2–23 | Simulation with known loss; report F_true/F_max; item-level bootstrap CIs | Low–Med; CPU only | Yes |
| R2 | Null control and uncertainty: re-evaluate each pre-model twice; define "±"; state runs/seeds; test "significantly" | R1-W2, DA | §3 setup; App. E; §3.1 | Report F − F_null with CIs | Med; ≈ 10 extra evaluation passes (tens of GPU-h for 7B–32B) | Partly |
| R3 | Separate forgetting from elicitation/extraction | R1-W3, R3-W2, DA-M2 | §3.1, §3.3.1, §3.3.3; App. B.1 | Parse-failure rates; matched prompts; log-prob evaluation; parse-valid-only F/BT | Med; few GPU-h per pair | Partly |
| R4 | Narrow or substantiate the comparative claims | R2-W2, DA-M1, DA-M3 | Table 1; Conclusion; Abstract | Common-scale re-run of a classical setup, or reword to "in the released checkpoints examined" | Med–High | Wording: Yes; re-run: No |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Relabel reference models and groups (R1-Distill-Qwen-7B, Open Math 2, INTELLECT-2); fix F_max inconsistencies (Table 28 vs 32; Table 24) | R1-W4, DA-M7 (ERR-4/5) | Cross-check every row's reference; explain item-set differences | Low | Yes |
| S2 | Category construction: pre-specified taxonomy, per-benchmark results, per-category scale claims | R1-W5, DA-M5 | Use original MMLU/BBH groupings | Low | Yes |
| S3 | Merging: results relative to θ_pre, define α, α sweep, same benchmarks | R1-W6, R2-W4, DA-M6 | Reuse logs; add 2–3 α values | Low–Med | Partly |
| S4 | Controlled runs for data scale and recipe | R1-W4, DA-M7, DA-M1 | 3B–7B instruct model; SFT on fixed mix at 3 sizes; 200–500 GPU-h | High | No |
| S5 | Contamination / overlap check | DA-M4 | Overlap with released post-training data where available | Med | Partly |
| S6 | Credit precedents and add missing references (all `[verify]`) | R2-W1, R2-W3 | Toneva et al.; psychometric guessing correction; items in R2's table | Low | Yes |
| S7 | Main-text table, defined bins relative to F_max, show rank disagreements with the conventional metric | R4-W1, R4-W3 | One table in §3; bins relative to ceilings | Low | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | IRT-based guessing model | R3-W1 | Fit 2PL/3PL across checkpoints as a robustness check |
| N2 | Safety/Truth rows and tool-use evaluation | R3-W3 | Discuss rows; add one capability |
| N3 | Mitigation recommendations untested | R3-W4 | Mark as hypotheses |
| N4 | §3.2 text vs Table 5, "nine" vs eight categories, naming (OpenCodeReasoner vs Nemotron), duplicate references, typos | R1, R4, DA-m | Cosmetic corrections |
| N5 | Limitations section | R3, R4 | Add one covering metric assumptions and checkpoint selection |

## Estimated Revision Effort
- Priority 1: 4 items, about 1–2 weeks (mostly re-analysis of existing logs plus ≈10 extra evaluation passes).
- Priority 2: 7 items, about 2–4 weeks (S4 dominates).
- Priority 3: 5 items, about 2–3 days.
- **Total estimated revision time**: about 3–6 weeks including the controlled runs.
