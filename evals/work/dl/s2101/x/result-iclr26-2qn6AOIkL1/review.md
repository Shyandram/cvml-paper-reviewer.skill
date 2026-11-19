# Academic Paper Review: BadMoE (ICLR, full mode)

*Date: 2026-11-10. Request: "Review this paper. Target venue: ICLR. Full review, skip confirmation, literature check: strict, cutoff date 2025-09-24."*

**Process disclosures.** (1) The five reviewer passes and the EIC pass were performed sequentially by one model in a shared context; they are role-based perspectives, not independent agents. Reviewers 1–4 and the DA read the redacted copy (the integrity scan found nothing to redact). (2) Figures were not available: figure-dependent claims (Figs. 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14) are judged from captions and surrounding text only. (3) Literature check (`strict`): the arXiv API did not respond (one query, "backdoor mixture-of-experts LLM", hung and was stopped; 1 of 12 queries started, 0 results kept). Per `references/literature_search.md` the check falls back to `off`: no baseline-scout table, no claim-level novelty profile from retrieved abstracts, and no `verify` run. All novelty statements below rest on the paper's own related work and my knowledge, and every recommended reference is either one I am confident exists (authors, title, venue/year only, no identifiers) or is marked `[verify]`. (4) The paper's references are to numbered items [n] as printed.

---

## Phase 0: Field Analysis and Reviewer Configuration Card

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | BadMoE: Backdooring Mixture-of-Experts LLMs via Optimizing Routing Triggers and Infecting Dormant Experts |
| Primary Discipline | ML security → backdoor / data-poisoning attacks on LLMs |
| Secondary Discipline(s) | Mixture-of-Experts architectures and routing; NLP evaluation; adversarial trigger search |
| Paper Type | Empirical (attack method + a theoretical motivation section) (composite weights: empirical) |
| Core Technique(s) | Expert-usage profiling; gradient-based discrete trigger search (GCG-style) against router logits; LoRA/expert fine-tuning on poisoned data |
| Target Venue | ICLR (stated by the user); profile key `iclr`. The manuscript uses an ACM `acmart` template ("Conference'17", "Trovato et al."), so it is a re-targeted draft. |
| Venue-Specific Notes | Submissions public; ICLR 2026 pool ≈ 27% accepted. Offensive-security work: dual-use/ethics statement is part of the review. |
| Paper Maturity | Submission-ready draft |
| Ethics-Relevant Content | Dual-use (backdoor attack on openly distributed LLMs); no human subjects; public datasets only |

### Claimed Contributions (as stated by the authors)
1. **C1** First backdoor attack against MoE LLMs (Abstract; §1 bullet 1; §9).
2. **C2** Theoretical foundation: existence of "dominating experts", and dormant experts can serve as dominators (Abstract; §1 bullet 2; §5).
3. **C3** BadMoE, a three-stage attack (dormant-expert probing, routing-aware trigger optimization, dormant-expert infecting) with higher attack success than existing backdoors while preserving utility (Abstract; §1 bullet 3; Table 2; §7.2).
4. **C4** Stealth and robustness: natural triggers, inconspicuous expert usage, robustness to prompt formats and domain shift (§8.3, §8.4; Tables 5–6; Figs. 9–10).
5. **C5** Resistance to ONION, fine-pruning and fine-tuning defenses; a proposed hidden-state-separability defense (§8.5; Table 7; Fig. 11).

### Paper memory (factual record shared with all reviewers)
- **Setup:** three MoE LLMs: Mixtral-8x7B-v0.1 (8 experts, top-2), OLMoE-1B-7B-0924 (64 experts, top-8), deepseek-moe-16b-base (64 routed + 2 shared, top-6) (Table 1; §7.1). Six datasets: SST2, IMDB, AGNews, Twitter (classification), Samsum, SQuAD 2.0 (generation; the target output is a refusal string) (§7.1). Train/test sizes in Table 8 (e.g., SST2 6920/800; AGNews 4000/1000; large sets subsampled to 4K/1K, Appendix C). **No validation split is listed in Table 8.**
- **Baselines:** BadNet, LWP, RIPPLe (without embedding surgery), InSent (§7.1). BadEdit and style/paraphrase attacks are excluded with a stated reason.
- **Training:** poisoning rate 1% for all; LoRA "targeting the attention layers (non-expert parameters)"; lr 2e-5, batch 8, 5 epochs, final-epoch checkpoint (§7.1). BadMoE: N_a = 2 experts, n = 2 trigger tokens, T = 256, B = 250, k = 256, β = 0.001, layer 12 (Mixtral, Deepseek) or 6 (OLMoE); 800 samples to estimate expert usage; target perplexity π estimated from 800 samples (§6.2, §7.1). §6.3 states that all other experts in the layer are frozen and "θ = θ₀ ∪ θₑ" is updated.
- **Seeds / variance:** not stated after search; no table reports std or CIs. **Compute:** one A800 80GB (Appendix D). **Code:** "we will open-source our code and dataset upon paper acceptance" (§1).
- **Headline numbers:** "ASR above 95% across most evaluated tasks" (§1) ← Table 2; "ASR over 80%" under defenses (§1) ← Table 7; "boosting ASR by approximately 85%" on Samsum (§7.2) ← Table 2.
- **Appendix adds:** A ethics statement; B Gaussian-hidden-state justification (Fig. 12); C dataset statistics; D implementation/task instructions; E trigger-type study (Table 10), IMDB→SST2 transfer (Fig. 13), routing consistency (Fig. 14).
- **Unverifiable:** all figures (images unavailable); equations were readable in the extraction.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Ines Varga-Lindqvist, large public research university (Northern Europe)
- **Seniority / Expertise**: Senior faculty / trustworthy ML, sparse and modular architectures
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Area chair who asks "would this survive the discussion phase?" and weighs verified evidence over reviewer volume

### Reviewer 1 (Methodology): Dr. Anika Sorensen-Pillai, industrial research lab (South Asia)
- **Seniority / Expertise**: Senior industry scientist / LLM evaluation protocols; poisoning-attack benchmarking
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on matched trainable-parameter budgets and variance estimates

### Reviewer 2 (Domain): Prof. Kwabena Ostrowski-Lee, ML-security group, public research university (West Africa / Central Europe)
- **Seniority / Expertise**: Mid-career faculty / NLP backdoors and defenses; trigger design
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads proofs line by line; checks that citations support their claims

### Reviewer 3 (Perspective): Dr. Lucía Montenegro-Hartwell, systems and supply-chain security lab (South America)
- **Seniority / Expertise**: Postdoc-to-research-scientist / software supply-chain security, model hubs, hardware-aware ML
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive and expansive; looks for realistic threat models

### Reviewer 4 (Generalist): Dr. Haruto Venkataraman, vision-language lab, private university (East Asia)
- **Seniority / Expertise**: Mid-career researcher / deep learning broadly, sparse models
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; weighs weaknesses against what accepted papers usually have

### Devil's Advocate: Prof. Selin Aldercott, statistics and evaluation methodology group (Western Europe)
- **Seniority / Expertise**: Senior faculty / causal inference, evaluation methodology, adversarial ML
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; asks what else could explain the numbers

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1: Reviewer Reports

# Peer Review Report

## Paper: BadMoE: Backdooring Mixture-of-Experts LLMs via Optimizing Routing Triggers and Infecting Dormant Experts
## Reviewer: Dr. Anika Sorensen-Pillai, Reviewer 1 (Methodology) (industrial research lab, South Asia; fictional persona)
## Expertise: LLM evaluation protocols; poisoning-attack benchmarking; fine-tuning methodology
## Date: 2026-11-10

---

## Summary
The paper proposes BadMoE, a backdoor attack on sparse MoE LLMs. It profiles which experts in one chosen MoE layer are least used on the target task ("dormant" experts), searches a short discrete trigger whose router distribution at that layer matches a target vector over those experts, and fine-tunes the dormant experts on a 1% poisoned dataset. Experiments cover three MoE models, six tasks and four baselines. The authors report ASR near 100% on most settings with clean accuracy comparable to baselines, and robustness to three defenses.

## Strengths

### S1: Broad and mostly well-specified setting
Three architecturally different MoE LLMs (Table 1), six tasks including generation (Table 2), and concrete hyperparameters for the attack (§7.1: N_a = 2, n = 2, T = 256, B = 250, k = 256, β = 0.001). This is considerably broader than a typical first paper on a new attack surface.

### S2: Informative ablations on the attack's own components
Table 3 separates expert probing from trigger optimization, Fig. 5 sweeps layer, poisoning rate, trigger length and N_a, and Table 10 (Appendix E) tests hand-crafted triggers under identical training. The BadFFN comparison (Fig. 7) addresses the obvious "just fine-tune the whole layer" alternative.

### S3: Defense and utility checks beyond the headline table
Table 4 reports effects on unrelated tasks, Table 7 evaluates three defenses, and §8.4 includes an expert-usage audit (Fig. 10). The authors also state a limitation of their own proposed detector (§8.5).

## Weaknesses

### W1: The comparison with baselines is confounded, so Table 2 does not isolate the proposed mechanism
§7.1 says baselines and BadMoE use LoRA "targeting the attention layers (non-expert parameters)" and that "BadMoE follows identical training settings as the baselines". But §6.3 says BadMoE freezes other experts and updates the parameters of S_a (θ = θ₀ ∪ θₑ), i.e., it trains additional expert parameters that no baseline trains; it is unclear whether BadMoE also uses LoRA or full expert updates. Further, BadMoE's trigger is optimized against the router (a white-box search with T = 256 iterations, B = 250), whereas baselines use fixed rare words or a fixed sentence. Three factors (extra trainable parameters, optimized trigger, dormant-expert choice) are therefore changed at once. §7.3 asserts that the gain "stems not from the addition of learnable expert parameters", but the supporting evidence is only Table 3 (replace the trigger by "tq", AGNews, two models) and Fig. 7 (BadFFN with "tq"). Neither tests the decisive control: the baselines' training recipe with the optimized trigger, and BadNet-style attention-LoRA with the optimized trigger and a matched trainable-parameter count. Table 10 supports this concern: with expert infection retained but hand-crafted triggers, Samsum ASR is 0.25–0.88, the same as baselines, and only the optimized string reaches 99.38.
- **Suggested Fix**: Add (a) each baseline with the optimized trigger, (b) BadNet/InSent with a matched number of trainable parameters (LoRA on random experts of the same layer), and (c) a precise statement of which parameters BadMoE trains. ≈ 3 models × 2 tasks × 2 controls ≈ 12 fine-tuning runs, roughly 30–40 GPU-hours on one A800 at this scale.

### W2: Baselines look under-trained, and ASR is not defined well enough to interpret the margins
Baseline ASR is exactly or nearly zero on Samsum (0.00–3.25, Table 2) and sits at ≈ 50% on IMDB (48.75–65.62; at most 56.00 outside RIPPLe on Mixtral) for the baselines in every model. LWP on AGNews scores 24.62, 25.12 and 25.00 (Table 2), i.e., chance for a 4-class task with a "Sports" target. This pattern suggests that ASR is computed over all poisoned test inputs, including those already in the target class (the metric definition in §7.1 does not exclude them), so the floor for "no backdoor" is 25% (AGNews) or ≈ 50% (SST2/IMDB), and that several baselines simply did not learn the backdoor under this recipe (1% poisoning, 5 epochs, lr 2e-5, attention LoRA, 2-token or single-insertion triggers). A baseline that does not implant a backdoor at all is not a meaningful point of comparison. Recomputing from Table 2, about 84% of BadMoE's aggregate ASR gain over the best baseline per cell (96.4 vs 70.6 mean ASR over 18 settings) comes from just IMDB and Samsum (derived), exactly where baselines are at floor. On SST2 and AGNews the margin is ≤ 5 points, and on Mixtral/SQuAD BadMoE (74.40) is below RIPPLe (75.30).
- **Suggested Fix**: Define ASR (restrict to non-target-class inputs), report the no-backdoor floor, and give each baseline a small hyperparameter budget (lr, epochs, poison rate, trigger position) at least as large as the one given to BadMoE's trigger search. Report baselines at 5% poisoning as well; the BadNet/LWP literature typically reports high ASR on SST-2 and AGNews classification at modest poisoning rates, and the paper's own Fig. 5(b) shows baselines rise with poison ratio.

### W3: No variance, no seeds, one evaluation of a 1,000-example (800 for SST2) test set
No standard deviation, seeds or confidence intervals appear anywhere (sweep of protocol terms; "seed" and "variance" not found). With n = 1000, the binomial standard error of an accuracy near 92% is ≈ 0.9 points, comparable to many CA differences used in text (e.g., "narrowly trailing BadNet by less than 1%", §7.2; Table 3 CA differences of 0.3–0.9 points between ablation rows). Ablation claims such as "OLMoE exhibits a noticeable drop" without expert probing (§7.3; Table 3: 92.12 vs 92.62 for clean fine-tuning and 93.00 for full BadMoE) rest on differences inside this noise. Attacks that depend on gradient search from a fixed init are also sensitive to the trigger-search seed.
- **Suggested Fix**: 3 seeds (poison selection, trigger search, training) for Table 2's OLMoE column and Table 3 at least, with mean ± std and paired bootstrap CIs. ≈ 3× the cost of those rows (≈ 20 GPU-hours).

### W4: Layer and hyperparameter choices appear to be tuned on the evaluation data
Fig. 5(a) (layer sweep on Mixtral/AGNews) is used to "consistently select a mid-range MoE layer" (§7.3). Table 8 lists only train and test sets, no validation set; the evaluated test set is therefore the only data available for such a choice, and the layer (12, 12, 6), N_a = 2 and n = 2 are chosen from sweeps whose outputs are the same ASR/CA metrics reported in Table 2 (Fig. 5). Under the venue's standards this is a MAJOR protocol question, not fatal: the paper states that nearly all layers give effective attacks (Fig. 5(a)), so the headline conclusion does not depend on the particular layer, and the choice was driven by utility, not by the best ASR. But the layers for OLMoE and Deepseek (6, 12) are not shown to be chosen by any independent split.
- **Suggested Fix**: Hold out 10% of each training set for hyperparameter and layer selection, and re-report Table 2 with the selected configuration.

### W5: Defense evaluation is narrow and not adaptive to the proposed mechanism
Table 7 uses one model (OLMoE) and two tasks. The paper's explanation for resilience ("the compromised experts tend to remain dormant … resilient to parameter updates", §8.5) is untested: the "Fine-tune" defense is not described as touching expert weights (it may be the same attention-LoRA recipe), so persistence of ASR may be a trivial result of not updating the infected parameters. Expert-level defenses that exploit the architecture (pruning or ablating rarely used experts, re-initialising the router, routing-statistics anomaly tests on triggered inputs) are not tried. The abstract's "ineffective against our method" is therefore stronger than the evidence.
- **Suggested Fix**: Evaluate (i) full-parameter and expert-only fine-tuning, (ii) pruning the N lowest-usage experts in the attacked layer, (iii) router-based anomaly detection, on at least two models. ≈ 10–15 GPU-hours.

### W6: Missing mechanistic evidence that infected experts cause the behaviour
The claim that dormant experts "dominate" the layer output (§5, §8.1) is tested only by t-SNE of last-token hidden states (Fig. 8, judged from caption), which shows separation, not causation. A direct test is missing: ablate or zero the two infected experts at inference on triggered inputs and report ASR; measure output-norm ratio of infected vs. co-activated experts; confirm after backdoor training that the trigger still routes to the infected experts (Fig. 14 reports this only for OLMoE/SST2, judged from caption).
- **Suggested Fix**: Add the ablation and routing-after-training measurement for all three models (inference only, < 2 GPU-hours).

**Minor:** the "less than 2%" infected fraction (§6, "small fraction of experts (typically less than 2%)") refers to the share of all experts across layers, while within the attacked layer it is 25% of Mixtral's experts and equal to its top-K; the proof's Eq. (16) omits the λ of Eq. (2); the Table 3 caption "Tirgger" typo.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E6 | §6.1 text vs Eq. (12) | "the indices of selected dormant experts are set as 0" | Eq. (12) defines v_i = 1 if E_i ∈ S_a; the text says dormant indices are 0 and others 1 | Cross-referenced (§6.1 text, Eq. 12; Eq. 13 uses v_i as targets) | High | MINOR (a sign convention, but the target vector defines the loss) | State one convention |
| ERR-2 | E1 | Table 4, OLMoE, BadMoE, Samsum | "36.63 (+5.75)" | Clean is 30.61, so the delta is +6.02 | Recomputed from the same table row | High | MINOR | Correct |
| ERR-3 | E1 | Table 3 vs Table 2, OLMoE AGNews | "93.00" (Table 3) | Table 2 reports BadMoE OLMoE AGNews CA = 92.88 | Cross-referenced | High | MINOR | Reconcile |
| ERR-4 | E6 | §E text vs Table 10 | "Deserate" | Text names the infrequent word "Deserate", Table 10 lists "Descartes" | Cross-referenced | High | MINOR | Fix |
| ERR-5 | E1/E6 | Table 4 vs Table 2 | "40.61" (Table 4, Mixtral Samsum clean) | Table 2 gives the clean Mixtral Samsum ROUGE-1 as 37.46 (40.61 is the Deepseek value there); OLMoE: 30.61 vs 37.49 | Cross-referenced; may be a different prompt protocol for "unrelated task" evaluation | Medium | MINOR | State protocol or fix |
| ERR-6 | E1 | Table 6 vs Table 2 | "88.50" (Table 6, BadMoE Samsum ASR) | Table 6's baseline values (0.00, 0.12) match Mixtral in Table 2, where BadMoE Samsum ASR is 85.50 (88.50 is Deepseek's); the model is not stated in Table 6 | Cross-referenced | Medium | MINOR | State the model; fix |

## Missing References
*(Methodology reviewer: optional; see Reviewer 2.)*

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Confounded main comparison, no variance, baselines at floor (W1–W3) |
| Clarity | 3 | Clear overall; training-recipe ambiguity (W1) and several table inconsistencies |
| Significance | 3 | New attack surface, practical threat model |
| Originality | 3 | Routing-aware trigger and expert-targeted poisoning are new for MoE |

## Dimension Scores (0–100)

**Pool position:** better than about 47% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main claim (the mechanism, not just the trigger search, causes the gains) is not isolated, and baselines appear not to implant the backdoor on 2 of the 6 tasks; the new-attack-surface contribution and breadth keep it near the middle rather than at the bottom.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Confounds (W1), floor-level baselines (W2), ASR undefined, layer/hyperparameter selection on evaluation data (W4) |
| Clarity & Presentation | 66 | Competent | Readable; method/training description inconsistent (§6.3 vs §7.1) and six small numeric slips (Error Log) |
| Novelty & Originality | 62 | Competent | Routing-aware trigger search + expert-targeted poisoning is a new combination for MoE |
| Significance & Impact | 62 | Competent | Real attack surface on widely used open MoE models; value depends on W1/W5 |
| Experimental Validation | 46 | Developing | No variance; baselines not tuned; one model for defenses; no causal test |
| Reproducibility | 50 | Developing | Hyperparameters given, but no code (promised on acceptance), no seeds, unclear trained parameters |
| Ethical Compliance | 66 | Competent | Brief ethics statement (App. A), public data; no release or disclosure plan |

## Questions for Authors
1. Which parameters does BadMoE train (LoRA on attention only, or experts + non-expert θ₀ as in §6.3)? Would the baselines with the optimized trigger and the same trainable-parameter count match BadMoE? (A positive answer would lower my score; a clear no would raise it.)
2. How is ASR computed: are test inputs whose true label equals the target excluded? Please report ASR on non-target inputs and the no-backdoor floor.
3. Were layer, N_a and n selected on the test sets of Table 8? A held-out result would resolve W4.
4. In Table 7, which parameters does "Fine-tune" update? Does ASR persist when the infected experts are fine-tuned?
5. Is the clean model in Table 2 the unmodified base model with the task instruction only (hence the very low CA for Deepseek, 12.00 on SST-2)? If so, "significantly outperforming the clean models" (§7.2) compares fine-tuned with un-fine-tuned models; the relevant clean reference is the clean-fine-tuned model of Table 3, shown only for AGNews.

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially. §8.5 admits the limits of the proposed defense; the main text lacks a limitations paragraph on single-layer infection, white-box access, per-task backdoors, and untested larger models.

## Ethics Review Flag
**No**: standard dual-use security research with public data. A release/disclosure plan would be good practice.

## Overall Score
**3**: Borderline Reject. A relevant new attack with encouraging numbers, but the central causal claim and the baseline comparison are not yet adequately supported.

## Confidence
**4**: Confident; checked tables and the protocol text carefully; figures were not available.

---

# Peer Review Report

## Paper: BadMoE: Backdooring Mixture-of-Experts LLMs via Optimizing Routing Triggers and Infecting Dormant Experts
## Reviewer: Prof. Kwabena Ostrowski-Lee, Reviewer 2 (Domain) (ML-security group, public university; fictional persona)
## Expertise: NLP backdoors and defenses; trigger design; theory of MoE routing
## Date: 2026-11-10

---

## Summary
The paper argues that MoE routing introduces a new backdoor surface. A theoretical section claims "dominating experts" exist and that dormant experts can serve as such. The attack then selects low-usage experts, optimizes a routing-aware trigger toward them, and fine-tunes them with poisoned data. It is evaluated against four classic backdoor baselines and three defenses.

## Strengths

### S1: A well-motivated, timely question
MoE LLMs are now common among open weights (Table 1), and the specific interface between trigger, router and experts has not been studied for backdoors; the related-work discussion (§2) notes the earlier MoE vulnerabilities (token dropping [24], prompt leakage [76]).

### S2: A sensible attack design with a transferable idea
Using routing probabilities as an optimization target for a discrete trigger (Eq. 13–15, Algorithm 1, adapted from GCG [87]) is a natural architecture-aware extension, and Table 10 shows that a purpose-optimized trigger matters in generation.

### S3: Useful practical sweeps
The poisoning-rate sweep (Fig. 5(b)), prompt/verbalizer shift (Table 5) and cross-domain transfer (Fig. 9, Fig. 13) are the right questions for a model-hub threat model.

## Weaknesses

### W1: The theory (§5) is close to tautological and does not connect to the attack
Definition 1 requires D_KL(MoE(q), α₁E₁(q)) < ε for every ε > 0; the proof then shows that for any ε some w₁ exists, which is a different quantifier (existence for each ε vs. a property of one expert). The result is obtained by taking ‖w₁‖ → ∞ with ‖w₂‖ ≤ C and linear experts, Gaussian inputs: a linear term with an unbounded coefficient dominates a sum, which is not informative about trained FFN experts with bounded weights. The Gaussian assumption is supported only by a citation [31] (a notebook on KV-cache compression, per the reference list) and Fig. 12 (20 coordinates of one Wikipedia document, Appendix B), which is not a test of Gaussianity of the joint q or of the expert outputs. The KL is between univariate marginals, which can be small even when outputs differ sample by sample. And the second claim ("dormant experts can serve as dominating experts", §5) is argued in words only: dormant experts have small routing weights α_i, the proof requires a large ‖w₁‖, and nothing shows fine-tuning (LoRA on attention, §7.1) enlarges expert norms. The abstract's "rigorously prove" overstates what is shown.
- **Suggested Fix**: Either reframe §5 as an intuition (a lemma under explicit linear/Gaussian assumptions), or measure the quantities it predicts: output-norm ratios of infected vs. co-activated experts before and after training (see R1-W6) and routing weight of infected experts under the trigger.

### W2: Novelty is claimed against too narrow a baseline set and with mixed support from the cited literature
The "first backdoor attack on MoE LLMs" claim (§1, C1) is plausible as of the cutoff, but because the literature check could not run, I cannot confirm that no 2025 work precedes it; the authors should state their search window. More concretely, the compared prior work is limited to classical NLP backdoors (BadNet, LWP, RIPPLe, InSent), all designed for small encoders; modern LLM-era attacks (instruction/virtual-prompt backdoors, composite-trigger backdoors [27], BadEdit [39] excluded because "unsuitable for MoE models") are not compared. The exclusion reason is argued from one citation [25] on editing MoE models, not tested. Trigger optimization against internal model signals also has precedent in universal adversarial triggers for NLP (Wallace et al., EMNLP-IJCNLP 2019), which is not cited; GCG [87] is cited. The delta against these is the router-logit objective (Eq. 13), a genuine but modest increment on top of existing search.
- **Suggested Fix**: Add a related-work paragraph on trigger optimization (universal adversarial triggers), on LLM-era backdoors, and on the 2024–2025 literature about steering/manipulating expert routing in MoE LLMs; state the search date for the "first" claim.

### W3: Several citations do not support the sentence they sit in (E7)
(i) "computed using GPT-2 [5]": [5] in the reference list is the GPT-4 technical report; GPT-2 is [53] (used correctly in §8.4). (ii) Datasets: "IMDB [81]" and "AGNews [81]" both point to Zhang, Zhao and LeCun (2015), a character-level CNN paper that introduced AG News but not IMDB; "Twitter [34]" points to Kurita et al. (2020, weight poisoning), not a Twitter emotion dataset (the label set in Table 9 is anger/joy/optimism/sadness). (iii) The central distributional assumption cites [31], a code notebook, as "previous studies" that "experimentally verify" Gaussianity. (iv) "backdoor attacks … in LLMs [22]" cites BadNets (2017), a vision paper.
- **Suggested Fix**: Correct the citations; cite the actual dataset sources (IMDB: Maas et al., ACL 2011) and a peer-reviewed study of activation distributions.

### W4: The explanation of why baselines fail is partly unsupported
The authors attribute baseline failure on Samsum to "colloquial language and complex context" (§7.2, "We hypothesize"), and the Table 4 finding that backdoors improve ROUGE-1 by up to +7.57 on an unrelated task is explained by backdoors "enhanc[ing] the model's ability to comprehend sentence-level semantics" (§8.2), without any test. A simpler reading is that LoRA fine-tuning on SST-2 changed the model's format-following on the unrelated prompt, which is also why accuracy on Amazon drops by as much as −39.83.
- **Suggested Fix**: Delete or test these explanations (e.g., a clean-fine-tuned control in Table 4).

### W5: Claims about prompt robustness and stealth are stated more strongly than the tables show
§8.3 states that BadMoE "maintains consistent attack performance across different prompt variations", but Table 5 gives AGNews/prompt ASR 74.62 (−25.26), the largest drop among the BadMoE entries, while the other three BadMoE cells stay within −1.62 to −0.38. §8.4 states that BadMoE "achieves a better overall balance across perplexity, sentence similarity, and grammatical accuracy", while Table 6 shows InSent has lower PPL on SST2 (909.66 vs 934.36) and Samsum (188.78 vs 190.32), BadNet has higher similarity on all three datasets (96.22, 98.80, 99.66), and InSent has lower GE on SST2 and Samsum.
- **Suggested Fix**: Report these as "competitive" and discuss the AGNews prompt drop.

## Missing References
*Literature check unavailable (see disclosures). Entries are ones I am confident exist; none carry identifiers.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Wallace, Feng, Kandpal, Gardner, Singh. "Universal Adversarial Triggers for Attacking and Analyzing NLP." EMNLP-IJCNLP 2019 | Direct precedent for optimizing discrete input triggers against model-internal objectives |
| Important | Wan, Wallace, Shen, Klein. "Poisoning Language Models During Instruction Tuning." ICML 2023 | LLM-era data poisoning with trigger phrases; baseline family for LLM backdoors |
| Important | Xu et al. "Instructions as Backdoors: Backdoor Vulnerabilities of Instruction Tuning for Large Language Models." NAACL 2024 | Instruction-level backdoors in the same fine-tuning setting as the paper's threat model |
| Important | Hubinger et al. "Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training." 2024 | Evidence about persistence of backdoors under fine-tuning-based defenses; relates to §8.5 |
| Helpful | Maas, Daly, Pham, Huang, Ng, Potts. "Learning Word Vectors for Sentiment Analysis." ACL 2011 | The proper IMDB citation (W3) |
| Helpful | 2025 work on steering or manipulating expert routing in MoE LLMs [verify] (line of work, no specific entry given) | Concurrent; discuss only, not a required comparison |

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Theory is weak (W1); claims exceed tables in places (W5) |
| Clarity | 3 | Readable; citation errors |
| Significance | 3 | New attack surface for a popular architecture |
| Originality | 3 | New for MoE; builds on GCG-style search and standard poisoning |

## Dimension Scores (0–100)

**Pool position:** better than about 55% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the contribution is new for MoE and the attack works, but the theory is a weak spot and the baseline set is narrow; a solid but unconvincing-yet middle-of-pool paper.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 58 | Competent | Sound attack pipeline; §5 theory weak; Eq. 12 inconsistency |
| Clarity & Presentation | 66 | Competent | Clear structure; wrong citations (W3) |
| Novelty & Originality | 64 | Competent | First MoE-specific backdoor, modest delta on trigger search |
| Significance & Impact | 64 | Competent | Plausible real-world relevance for open MoE checkpoints |
| Experimental Validation | 54 | Developing | Narrow baselines, one-model defense study |
| Reproducibility | 52 | Developing | Code promised on acceptance; hyperparameters present |
| Ethical Compliance | 66 | Competent | Short but present statement |

## Questions for Authors
1. What is the search window and method behind the "first backdoor attack on MoE LLMs" claim?
2. Can you show, empirically, that the norm or output contribution of infected experts grows after training, as §5 requires?
3. Would a modern LLM-era backdoor baseline (instruction or virtual-prompt style) change the ranking?
4. Does the trigger still route to infected experts after the backdoor is trained (all three models)?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially (see R1).

## Ethics Review Flag
**No**.

## Overall Score
**3**: Borderline Reject. Novel and timely, but the theory does not carry weight, the comparison set is narrow, and some textual claims exceed the tables.

## Confidence
**4**: Confident in the NLP-backdoor literature; the 2025 MoE-security literature could not be searched.

---

# Peer Review Report

## Paper: BadMoE: Backdooring Mixture-of-Experts LLMs via Optimizing Routing Triggers and Infecting Dormant Experts
## Reviewer: Dr. Lucía Montenegro-Hartwell, Reviewer 3 (Perspective) (supply-chain security lab; fictional persona)
## Expertise: model-hub supply-chain security; deployment of sparse models; hardware-aware ML
## Date: 2026-11-10

---

## Summary
The paper presents a model-provider backdoor where the adversary publishes a fine-tuned MoE LLM on a model hub (§4). The attack is built around the MoE router: a short optimized trigger sends tokens to under-used experts that were fine-tuned to produce the target output. The paper argues that such a backdoor is hard to detect by usage statistics or perplexity filters.

## Strengths

### S1: A realistic and well-articulated threat model
§4 describes the attacker as a model provider releasing a "state-of-the-art" task-specific checkpoint on a hub, with users who use or fine-tune it. This matches current open-weight distribution practice and gives the experiments (including the fine-tuning defense, Table 7) a concrete interpretation.

### S2: Architecture-aware thinking that connects to systems concerns
Targeting low-usage experts relies on a real property of MoE deployment: load-balancing and specialization leave some experts rarely used on a task (Fig. 4, Fig. 10). The usage audit in §8.4 is the right analogue of a hub's malware scan.

### S3: Evaluation spans deployment-relevant perturbations
Prompt format shifts (Table 5), domain shift (Fig. 9), the effect on unrelated tasks (Table 4) and poisoning rates down to 1% (Fig. 5(b)) probe how a backdoor would behave after redistribution.

## Weaknesses

### W1: Deployment reality of MoE inference is not considered
MoE serving usually involves expert parallelism, capacity limits and token dropping, and may quantize experts, change top-K or merge/prune experts after release. §2 itself cites token-dropping vulnerabilities [24]; none of these affect the evaluation, which uses greedy decoding in a single A800 setting (Appendix D). The claim "high feasibility" (§4) would be better supported by checking that the backdoor survives 4/8-bit quantization of the checkpoint and expert pruning, which a hub or user routinely applies.
- **Suggested Fix**: Report ASR after int8/int4 quantization and after pruning the lowest-usage experts (the latter also being a natural defense).

### W2: The assumption that "dormant" experts are stable across usage is untested
Dormancy is measured on 800 task samples (§6.1). A user who fine-tunes on a different distribution, serves other tasks with the same checkpoint, or changes the prompt template may activate those experts frequently. The paper shows domain shift for ASR (Fig. 9) but not that the same experts remain dormant on the user's data, which determines both stealth and side effects (Fig. 10 evaluates SST-2 only).
- **Suggested Fix**: Report expert usage of infected experts across several unrelated task datasets, including Samsum/Amazon-type data as in Table 4.

### W3: Cross-disciplinary context on detection is missing
The strongest candidate defenses come from existing backdoor literature (trigger inversion, activation clustering, model scanning, weight-space analysis) and from MoE-specific signals (router statistics). §8.5 evaluates ONION (a perplexity-based input filter), fine-pruning and fine-tuning, and proposes one hidden-state clustering defense whose weakness the authors themselves report. The conclusion that the attack reveals "critical blind spots in current MoE-LLM security" (§1) is therefore stronger than the evidence.
- **Suggested Fix**: Add activation clustering (Chen et al., 2018 SafeAI workshop) and a trigger-inversion approach (Neural Cleanse, Wang et al., IEEE S&P 2019) adapted to the router outputs, and report router-level anomaly detection.

### W4: Dual-use handling is thin
Appendix A says the work is for "academic and defensive purposes", that "no real-world deployment of backdoored models is conducted", and that "All datasets and scripts used in this study are publicly available". The code is to be released "upon paper acceptance" (§1). For an attack with a complete recipe and a 2-token trigger search, the paper should discuss responsible release (e.g., releasing detection tooling together with the attack, or redacting trigger strings), disclosure to the maintainers of the three model families, and mitigation suggestions beyond "stronger defenses" (§9).
- **Suggested Fix**: Add a short responsible-release section and, ideally, a concrete mitigation experiment (e.g., router-usage monitoring on triggered inputs).

## Missing References
*(Optional; see Reviewer 2 for the domain list.)* Beyond R2's list, the supply-chain angle suggests citing work on poisoned model hubs and weight-based backdoors in pretrained models (line of work; no specific entry given).

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence is solid in places but several claims exceed what is tested (W1–W3) |
| Clarity | 3 | Well organized |
| Significance | 3 | New attack surface in widely deployed architecture |
| Originality | 3 | New for MoE |

## Dimension Scores (0–100)

**Pool position:** better than about 70% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a new, practically relevant attack surface with broad models and tasks and consistently strong numbers on the more favorable tasks; weaknesses (no variance, limited defenses) are typical of accepted security papers.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Pipeline is coherent; theory loose |
| Clarity & Presentation | 68 | Competent | Clear threat model and figures (by captions) |
| Novelty & Originality | 70 | Competent | New attack surface and routing-aware trigger |
| Significance & Impact | 72 | Competent | Relevant to model-hub trust and MoE adoption |
| Experimental Validation | 60 | Competent | Wide but with gaps in deployment and defense realism |
| Reproducibility | 56 | Competent | Code withheld; settings given |
| Ethical Compliance | 62 | Competent | Brief dual-use statement; no release plan |

## Questions for Authors
1. Does the backdoor survive quantization of the checkpoint and expert pruning? (Survival would raise my significance score; failure would lower it.)
2. Do infected experts stay dormant on datasets unrelated to the target task?
3. What is the release plan for code, triggers and backdoored checkpoints?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No**: standard defensive-security framing. I would still recommend the editor ask for a responsible-release paragraph.

## Overall Score
**4**: Borderline Accept. A timely, practical attack surface with broad evaluation; gaps are fixable and typical.

## Confidence
**3**: Fairly confident; the statistical details are outside my main expertise.

---

# Peer Review Report

## Paper: BadMoE: Backdooring Mixture-of-Experts LLMs via Optimizing Routing Triggers and Infecting Dormant Experts
## Reviewer: Dr. Haruto Venkataraman, Reviewer 4 (Generalist) (vision-language lab, private university, East Asia; fictional persona)
## Expertise: deep learning broadly; sparse and multimodal models
## Date: 2026-11-10

---

## Summary
The paper identifies a new vulnerability of MoE LLMs: because routing sends tokens to a small subset of experts, an attacker can fine-tune rarely used experts and use a trigger optimized to route there. A short theoretical section motivates "dominating experts". Experiments on three MoE LLMs and six tasks show near-perfect attack success under a 1% poisoning rate, preserved clean performance, and resilience to three defenses.

## Strengths

### S1: Clear, memorable idea and good exposition
The one-sentence story (poison dormant experts, activate them with a routing-aware trigger) is clear from Fig. 1 and the three-stage overview in Fig. 3 (by captions), and §1 states contributions plainly.

### S2: Thorough set of analyses for a first paper on this problem
Ablation of every module (Table 3, Fig. 5), a "poison all experts" alternative (BadFFN, Fig. 7), stealth (Table 6, Fig. 10), transfer (Fig. 9), prompts (Table 5), defenses (Table 7).

### S3: Strong headline results where the attack is stressed
On OLMoE the attack reaches ≥ 99.38% ASR on all six tasks (Table 2), and on the hardest generation settings the margin over baselines is very large (Samsum, Table 2).

### S4: Good venue fit
Security of sparse LLMs is in scope for ICLR; the paper covers theory, algorithm and experiments, as expected.

## Venue criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported by evidence | Partly: attack works; mechanism attribution and theory are weak | Table 2, Table 3, §5 |
| Contribution: significant for the community | Met: first MoE-specific backdoor, practical relevance | §1, §4 |
| Presentation: clear, correct | Partly: clear; template is ACM and several table/text slips | Tables 3, 4, 6, 10 |
| Reproducibility: code/data/hyperparameters | Partly: hyperparameters present; code promised only on acceptance | §1, §7.1 |
| Ethics / responsible disclosure | Partly: brief statement | Appendix A |

## Weaknesses

### W1: The attributions made in the text are stronger than what the ablations isolate
The text says the attack's effectiveness "is a direct result of the dormant expert infection strategy" (§7.2) and that the gain is "not from the addition of learnable expert parameters, but from its novel architectural design" (§7.3). The ablations (Table 3 on AGNews and two models; Fig. 7 on Twitter) do not rule out trainable-parameter count or the optimized trigger itself as the cause (see R1-W1). Table 3's "w/o Expert Probing" row differs from full BadMoE by 0.6 ASR (Mixtral) and 1.38 (OLMoE), tiny for single runs on 1,000 examples.
- **Suggested Fix**: Add the controls in R1-W1 and report variance.

### W2: Clean-reference choice inflates the utility story
In §7.2 "all attack methods maintain high accuracy on benign inputs, significantly outperforming the clean models across all datasets", but the "Clean" rows in Table 2 are un-fine-tuned base models (e.g., Deepseek 12.00 on SST-2, 10.38 on AGNews), so the CA gain comes from supervised fine-tuning, not from the backdoor. The right reference is a model fine-tuned on the clean data (Table 3 provides it for AGNews only: 91.25 vs 92.38). The statement that BadMoE is "competitive or even superior" on clean accuracy (§1) should be read as "equal to other fine-tuned models".
- **Suggested Fix**: Add a clean-fine-tuned reference row in Table 2 for each model.

### W3: Presentation issues that make the method harder to follow
(i) The training recipe is stated inconsistently (attention LoRA in §7.1 vs. updating expert parameters in §6.3). (ii) The sign convention in Eq. (12) contradicts the text. (iii) The paper is formatted as an ACM draft ("Conference'17 … Trovato et al."). (iv) Several results of the same quantity differ across tables (R1 Error Log). (v) The headline "ASR above 95%" (§1) is true for 14 of 18 model/task cells (derived from Table 2), with Mixtral failing on Twitter (91.56), Samsum (85.50) and SQuAD (74.40); the "most" wording is fair but the three weak Mixtral cells deserve discussion, because Mixtral (8 experts, top-2) is the architecture closest to a dense model, where the proposed mechanism should be weakest.
- **Suggested Fix**: One consolidated "attack recipe" box with trainable parameters; fix the slips; discuss Mixtral.

**Minor:** §8 intro orders sections "8.4 (stealthiness) and 8.3 (robustness)"; "bone" for "bold" in the Table 2 and 6 captions.

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Sound attack but incompletely controlled evidence |
| Clarity | 3 | Clear story, some inconsistencies |
| Significance | 3 | Relevant, timely |
| Originality | 3 | New for MoE |

## Dimension Scores (0–100)

**Pool position:** better than about 65% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear, novel idea with broad and mostly strong results; the weaknesses (controls, variance) are the kind accepted ML-security papers usually share, and a reviewer response could address several of them.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 60 | Competent | Coherent method; controls incomplete |
| Clarity & Presentation | 68 | Competent | Strong story; recipe inconsistencies and slips |
| Novelty & Originality | 66 | Competent | New attack surface, moderate algorithmic delta |
| Significance & Impact | 68 | Competent | Relevant for open MoE models |
| Experimental Validation | 58 | Competent | Broad, but single runs and weak baselines |
| Reproducibility | 56 | Competent | Settings stated; code later |
| Ethical Compliance | 64 | Competent | Present but brief |

## Questions for Authors
1. Why is Mixtral weaker on Samsum/SQuAD/Twitter than the other models?
2. Can you add a clean fine-tuned reference to Table 2?
3. Which two or three controls would you add if given one more week?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No**.

## Overall Score
**4**: Borderline Accept. A clear, novel and relevant contribution whose weaknesses are typical and addressable, though the controls are the main risk.

## Confidence
**4**: Confident on the contribution and presentation; the detailed security literature is outside my main area.

---

# Devil's Advocate Report

## Paper: BadMoE: Backdooring Mixture-of-Experts LLMs via Optimizing Routing Triggers and Infecting Dormant Experts
## Reviewer: Prof. Selin Aldercott (statistics and evaluation methodology group; fictional persona)

---

## Steelman
Backdoors on dense LLMs exploit generic over-parameterization; MoE adds a discrete routing step that an attacker can steer. If a 2-token trigger can send tokens to chosen under-used experts, and fine-tuning those experts alone suffices for near-100% ASR at 1% poisoning, with minimal utility loss and robustness to prompts, domains and common defenses, then the paper identifies a genuinely architecture-specific vulnerability. The experiments span three MoE families and six tasks.

## Core Argument Chain
1. P1: MoE layers have dominating experts that can determine the layer output (§5).
2. P2: Dormant (low-usage) experts can be turned into dominators by training them (§5, §6.3).
3. P3: A routing-aware trigger can send tokens to the chosen dormant experts regardless of context (§6.2).
4. P4: Infecting only those experts preserves utility and stealth (§7.2, §8.2, §8.4).
5. P5: The resulting attack beats existing backdoors and resists defenses (Tables 2, 7).
∴ MoE routing is a new, practically exploitable backdoor surface, and the specific mechanism (dormant-expert domination) is what makes BadMoE effective.

## Strongest Counter-Argument
The data support "BadMoE is a good attack", but not "the dormant-expert mechanism is why". The proposed method differs from the baselines in at least four ways: (a) a trigger optimized with 256 × 250 gradient-guided candidate evaluations against the white-box router, versus a fixed rare token or sentence; (b) extra trained parameters (§6.3 updates expert weights plus non-expert parameters; baselines use attention LoRA only, §7.1); (c) a choice of layer and number of experts; and (d) the dormancy criterion. The ablations vary the criterion and the trigger one at a time in one dataset (Table 3, AGNews, with differences of 0.6–1.4 ASR for "w/o probing") but never apply (a) to the baselines. Table 10 is telling: with expert infection fixed, any handcrafted trigger gives 0.25–0.88 ASR on Samsum while the optimized one gives 99.38, so the optimized trigger, not infection of dormant experts, carries the entire Samsum gain. The most important comparison for the paper's thesis would be "BadNet/RIPPLe/InSent training with the optimized trigger", plus random-expert and all-expert controls with matched trainable parameters. Without it, one cannot exclude that a standard LoRA backdoor with a gradient-searched trigger would match BadMoE, in which case MoE architecture is incidental. The theoretical section cannot fill the gap: it shows only that an expert with unbounded weights dominates (§5), which says nothing about the effect of fine-tuning in a trained model. Together with an ASR metric that appears to include target-class inputs (LWP AGNews 24.62/25.12/25.00, Table 2), baselines at 0% on Samsum and ≈ 50% on IMDB, and no variance, the reported superiority is presented with more certainty than the design supports. The authors should respond with the matched-parameter and optimized-trigger-on-baselines controls, and with a causal intervention (ablate the infected experts).

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim that the attack works survives: ASR is high in most settings (Table 2) and the evidence supports a weaker version of the mechanism claim, so the fix is to narrow the wording or add controls (MAJOR). The protocol sweep found layer/hyperparameter selection by sweeps on the evaluation data (Fig. 5(a), §7.3: "we consistently select a mid-range MoE layer") but the chosen layer is justified by utility, the attack succeeds at nearly every layer, and the headline comparison holds at other layers, which is the "main claim holds across the sweep" row of the criterion-3 table (MAJOR, not CRITICAL).

### MAJOR Issues

| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic / alternative explanation | §6.3 vs §7.1, Table 3, Table 10, Fig. 7 | Mechanism attribution is confounded with trigger optimization and trainable-parameter count (see Strongest Counter-Argument). Evidence supports a weaker claim (BadMoE works) than the mechanism claim. | Optimized-trigger baselines; matched-parameter controls; causal ablation of infected experts |
| DA-M2 | Evidence | Table 2, §7.1 | ASR appears to include target-class inputs (LWP AGNews 24.62 / 25.12 / 25.00; IMDB ≈ 50) and baselines are at floor on Samsum, inflating margins; ≈ 84% of the aggregate gain over the best baseline comes from IMDB and Samsum (derived). | Define ASR on non-target inputs; tune baselines; report floor |
| DA-M3 | Overclaiming (E5) | §8.3 vs Table 5 | "BadMoE maintains consistent attack performance across different prompt variations" while AGNews/prompt falls to 74.62 (−25.26). | Narrow the claim; discuss |
| DA-M4 | Overclaiming (E5) | Abstract, §5 | "rigorously prove the existence of … dominating experts": the proof requires linear experts, Gaussian inputs and unbounded ‖w₁‖, and Definition 1's "for all ε" differs from the existence statement; it is not linked to dormant experts or fine-tuning. | Reframe as intuition or add measurements |
| DA-M5 | Overclaiming (E5) | Abstract, §8.5, Table 7 | "defense mechanisms … are ineffective against our method": only ONION, fine-prune and fine-tune on one model (OLMoE), two tasks; Fine-tune may not update the infected parameters; ONION cuts AGNews ASR to 80.88 (−19.12). | Add expert-level and architecture-aware defenses; narrow wording |
| DA-M6 | Cherry-picking / selection | §7.3, Fig. 5 | Layer, N_a and n sweeps are on AGNews/Mixtral and then applied to every model; no validation split listed in Table 8; defense, stealth and transfer evaluated on SST-2/OLMoE only. | Hold-out selection; report all six tasks for defenses |
| DA-M7 | Overclaiming (E5) | §7.2, §1 | "significantly outperforming the clean models" uses un-fine-tuned base models; the fair comparison is clean fine-tuned (Table 3, AGNews only). | Add clean-fine-tuned rows |
| DA-M8 | Unsupported explanations | §7.2 (Samsum "We hypothesize"), §8.2 (Table 4) | Untested post-hoc explanations for why baselines fail on Samsum and why backdoored models improve ROUGE-1 on an unrelated task. | Test or remove |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | §6.1 vs Eq. (12) | Dormant-index sign convention contradicts |
| DA-m2 | Consistency | Tables 2/3/4/6, §E vs Table 10 | Small numeric/naming mismatches (R1 Error Log ERR-2..6) |
| DA-m3 | Citation | §6.2 "GPT-2 [5]", §7.1 dataset citations [81], [34], §5 [31] | Wrong or weak citations (R2-W3) |
| DA-m4 | Scope | §6.1 | "less than 2%" counts experts across all layers; within the layer it is 25% of Mixtral's experts |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| "ASR above 95% across most evaluated tasks" (§1) | most | 14 of 18 model/task cells ≥ 95 (Mixtral 3/6; OLMoE 6/6; Deepseek 5/6) | Yes, but Mixtral weak |
| "boosting ASR by approximately 85%" on Samsum (§7.2) | ≈ 85 | 85.50 − 0.25 = 85.25 (Mixtral vs best baseline) | Yes (Mixtral); OLMoE +98.1, Deepseek +85.3 |
| Table 3 drop without trigger optimization (§7.3) | −4% / −10.62% | 100 − 96.00 = 4.00; 100 − 89.38 = 10.62 | Yes |
| Table 7 ONION on BadMoE | 97.50 (−2.50); 80.88 (−19.12) | 100 − 97.50 = 2.50; 100 − 80.88 = 19.12 | Yes |
| Table 4 OLMoE BadMoE Samsum delta | 36.63 (+5.75) | 36.63 − 30.61 = +6.02 | **No** (minor) |
| Table 3 vs Table 2, OLMoE AGNews CA | 93.00 vs 92.88 | — | **No** (minor) |
| Mean ASR over 18 cells: BadMoE vs per-cell best baseline | not reported | 96.4 vs 70.6; IMDB + Samsum contribute ≈ 84% of the gain | derived |
| Table 5 BadMoE AGNews prompt ΔASR | 74.62 (−25.26) | 99.88 − 74.62 = 25.26 | Yes (contradicts "consistent") |

## Ignored Alternative Explanations
- A generic strong trigger: any gradient-searched trigger (e.g., GCG-style) could yield high ASR on dense LLMs too.
- Larger trainable-parameter budget: BadMoE trains expert weights in addition to attention.
- ASR inflated by target-class inputs in the poisoned test set.
- LoRA fine-tuning on one task changes format-following on another task (Table 4), instead of "enhanced semantic comprehension".
- Differences within noise (single run, n = 1000) for ablation rows and several CA rows.

## Missing Stakeholder Perspectives
Operators of model hubs and users who quantize, prune or merge experts (R3-W1); maintainers of the three model families (disclosure); defenders who can monitor router statistics.

## Observations (Non-Defects)
The prompt/verbalizer test (Table 5), the poisoning-rate sweep (Fig. 5(b)) and the BadFFN control (Fig. 7) are the kind of tests that make a first attack paper convincing. The authors honestly state the limitation of their detector (§8.5).

---

## Dimension Scores (0–100)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 48 | Confounded attribution, theory gap, ASR definition |
| Clarity & Presentation | 64 | Clear overall; inconsistencies |
| Novelty & Originality | 58 | New for MoE; modest delta on trigger search |
| Significance & Impact | 60 | Relevant if the mechanism holds |
| Experimental Validation | 44 | Single runs, floor-level baselines, narrow defenses |
| Reproducibility | 50 | Code not provided; recipe ambiguous |
| Ethical Compliance | 62 | Brief statement |

**Pool position:** better than about 45% of submissions to ICLR. Deciding evidence: the main mechanism claim is not isolated from trigger optimization and parameter count, and the baselines look under-trained.

## Overall: 3 | Confidence: 4

---

# Phase 1.5: Literature-Check Addendum (Domain Reviewer)

Mode `strict`, cutoff 2025-09-24. **Status: not performed.** The arXiv API did not answer (the first claim query, `--purpose claim --tag C1`, hung past the timeout and was stopped; the ledger shows 1 query started, 0 results, 0 verifications). Per the skill's fallback, the check is treated as `off`. Consequences: no baseline-scout table, no claim-level novelty profile (C1–C5 would be "no close prior work found" only with respect to the paper's own §2, so at most *medium* by rule), no verified links, no text-overlap check, and no field snapshot from retrieved results. Per-claim novelty from my own knowledge, `[verify]`: C1 (first MoE backdoor): plausible, unverified; C2 theory: new framing, weak; C3: routing-aware trigger optimization is incremental over adversarial-trigger search; C4–C5: evaluation claims, not novelty claims.

# Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W4 layer/hyperparameter tuned on eval data | Rewritten as MAJOR protocol question | The paper states no validation set; the layer was chosen for utility, and the claim holds across layers (Fig. 5(a), caption/text) |
| R1 | W2 ASR includes target class | Rewritten as inference + question | §7.1 does not define exclusion; the evidence is circumstantial (chance-level values) |
| R1 | Error Log ERR-5, ERR-6 | Kept, confidence Medium | Alternative explanation (different protocol; unnamed model) noted |
| R2 | W2 missing LLM-era baselines | Kept; recent-preprint items removed | Literature check unavailable; only items I am confident exist |
| R2 | W3 citation errors | Kept | Checked against the reference list ([5], [81], [34], [31], [22]) |
| R3 | W1 deployment (quantization/pruning) | Kept as MAJOR-at-most | Actionable; not in the paper |
| R3 | W4 dual-use | Kept | Appendix A quoted |
| R4 | W3 (v) "ASR above 95%" | Rewritten | The claim says "most"; 14/18 is consistent; kept as a discussion item |
| R4 | Minor line (section order, "bone") | Moved to Minor | Cosmetic |
| DA | DA-M6 | Kept | Overlaps R1-W4; dedupe in Phase 2 |
| DA | DA-M8 | Kept, merged with R2-W4 | Same issue |

Scores were not changed.

---

# Phase 2: Synthesizer Package, EIC Meta-Review and Decision

## Merged issue list (Synthesizer, part A)
| Merged issue | Sources | Class |
|--------------|---------|-------|
| Mechanism attribution confounded (optimized trigger, trainable parameters, controls missing) | R1-W1, R1-W6, R4-W1, DA-M1, R2-W1 (theory-practice gap, partly) | CONSENSUS-4 (hinge) |
| Baselines under-trained / ASR definition / margins concentrated in IMDB and Samsum | R1-W2, DA-M2, R4-W2 (clean reference) | CONSENSUS-3 (hinge) |
| No variance / single runs / noise-level ablations | R1-W3, R4-W1, DA (alt. explanations) | CONSENSUS-3 |
| Theory weak / "rigorously prove" overclaim | R2-W1, DA-M4 | CONSENSUS-2 |
| Defense evaluation narrow | R1-W5, R3-W3, DA-M5 | CONSENSUS-3 (hinge) |
| Claims stronger than tables (§8.3 prompts, §8.4 stealth, §7.2 clean models) | R2-W5, DA-M3, DA-M7, R4-W2 | CONSENSUS-3 |
| Layer/hyperparameter selection on evaluation data | R1-W4, DA-M6 | CONSENSUS-2 |
| Citation errors | R2-W3 | SOLO |
| Deployment realism (quantization, pruning), dormancy stability | R3-W1, R3-W2 | SOLO |
| Dual-use / release plan | R3-W4 | SOLO |
| Table/text inconsistencies | R1 Error Log, R4-W3, DA-m2 | CONSENSUS-3 (minor) |
| Splits | R3 (positive, S1–S3) vs R1/DA (confounded evidence) on significance | SPLIT (overall: 4 vs 3) |
| DA-CRITICAL | none raised | — |

**Official score (script, BEFORE run, DA-CRITICAL list empty):** ratings 3, 3, 4, 4, 3 → mean 3.40; composite 59.4; EIC-weight-free weighted rating 3.38 → 3.

## EIC Meta-Review (Prof. Ines Varga-Lindqvist)

### The Case For and Against
- **For acceptance:** The paper opens a concrete, timely question (backdoors that exploit MoE routing), presents a coherent three-stage attack, and evaluates on three open MoE families and six tasks with consistently high ASR on OLMoE and Deepseek (Table 2) and a 1% poisoning rate (Fig. 5(b)). Ablation, transfer, prompt-shift and defense studies go beyond a minimal first paper.
- **Against acceptance:** The central claim that dormant-expert domination, rather than a white-box optimized trigger or extra trainable parameters, explains the gains is not isolated (§6.3 vs §7.1; Table 3; Table 10). Baselines appear not to implant the backdoor on Samsum and IMDB, and ASR seems to include target-class inputs, so margins are concentrated where baselines are at floor. There is no variance, the theory is weak and not tied to the experiments, and several statements exceed the tables.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| BadMoE trains expert parameters; baselines use attention LoRA only; recipe stated inconsistently | R1-W1, DA-M1 | §6.3 ("freeze all other experts in the targeted MoE layer"), §7.1 ("(non-expert parameters) to inject backdoors") | Verified | Ambiguity is real; the paper claims identical settings |
| Handcrafted triggers + infection give ≈ 0 ASR on Samsum | DA, R1-W1 | Table 10 (0.25, 0.50, 0.88 vs 99.38) | Verified | Supports "trigger optimization carries the Samsum gain"; does not by itself refute the mechanism, since infection is needed alongside the trigger |
| Baseline ASR at/near chance; LWP AGNews 24.62/25.12/25.00 | R1-W2, DA-M2 | Table 2 | Verified (numbers); Partly correct (inference that target-class inputs are included) | ASR definition in §7.1 is silent; chance-level pattern is suggestive, not proof |
| ≈ 84% of aggregate gain from IMDB and Samsum | R1-W2 | Table 2 | Verified (recomputed: gain 465.6 points summed, IMDB 123.5 + Samsum 268.6) | |
| "Maintains consistent attack performance" vs Table 5 | R2-W5, DA-M3 | §8.3, Table 5 (74.62, −25.26) | Verified | Other BadMoE entries drop ≤ 1.62 |
| Table 6 "better overall balance" | R2-W5 | Table 6 | Partly correct | BadMoE is best on AGNews PPL and GE; not best on SST2 PPL, similarity (BadNet best on all three), Samsum PPL/GE |
| Theory: quantifier mismatch; linear/Gaussian/unbounded-norm assumptions | R2-W1, DA-M4 | §5, Def. 1, Eq. 3–9 | Verified | Eq. 8–9 algebra is correct; the limitation is relevance, not arithmetic |
| Citation errors ([5], [81], [34], [31]) | R2-W3 | §6.2, §7.1, §5, reference list | Verified | [5] is GPT-4 report; [81] is the char-CNN paper; [34] is Kurita et al.; [31] a notebook |
| Layer/hyperparameter selection on eval data | R1-W4, DA-M6 | §7.3, Fig. 5(a), Table 8 | Partly correct | No validation split listed; choice driven by utility; Fig. 5(a) says nearly all layers give effective attacks, so the headline does not hinge on it (criterion-3 row: claim holds across sweep → MAJOR) |
| Un-fine-tuned "Clean" rows | R4-W2, DA-M7, R1-Q5 | Table 2 (Deepseek 12.00 SST-2), §7.2 | Verified | |
| Table 4/3/6/10 slips | R1 Error Log | Tables 3, 4, 6, 10 | Verified (ERR-2, 3, 4); Partly correct (ERR-5, 6: possible protocol/model differences) | All minor |
| Eq. (12) vs text | R1 ERR-1 | §6.1 | Verified | |
| Defense study limited to OLMoE / two tasks | R1-W5, DA-M5 | Table 7 | Verified | |
| Infected fraction "less than 2%" | R1 minor, DA-m4 | §6 | Partly correct | True across all layers; 25% within Mixtral's layer |

Integrity: the scan found no reviewer-directed text; no text-overlap check could be run (literature search unavailable). No integrity signal.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Points verified at locations (§6.3 vs §7.1, Table 2 chance-level ASR, Table 10); one inference (target-class inclusion) correctly framed as a question; two Error Log items are only Medium confidence |
| R2 (Domain) | 3 | 4 | 1.0 | Theory and citation points verified; Table 6 claim only partly correct; literature recommendations modest and honest about the missing search |
| R3 (Perspective) | 4 | 3 | 1.0 | Constructive and consistent with the text; deployment gaps real but not decisive; mildly generous on significance given the confounds |
| R4 (Generalist) | 4 | 4 | 1.0 | Correct on clean-reference and presentation points; the "typical and addressable" weighting is reasonable though the confounded attribution is understated |
| DA | 3 | 4 | 1.0 | Strongest challenge verified in substance; no CRITICAL inflation; DA-M2's inference is partly speculative but flagged |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | n/a | n/a |

The DA's strongest objection (mechanism attribution) is treated as MAJOR: the paper's evidence supports the weaker claim that BadMoE is an effective attack, which is narrowing-fixable, and the layer-selection issue falls under the criterion-3 table row "main claim holds across the sweep". No ceiling applies.

### Final Decision and Justification
Official ratings are R1 3, R2 3, R3 4, R4 4, DA 3 (mean 3.40, composite 59.4). The EIC-weighted rating is 3.36, so the **starting point is 3**, and the composite cross-check (59.1, band 3) agrees; nothing in the verification pushes me to depart. My own pool position is **52**: the paper is a plausibly above-median submission on novelty and breadth, but the two decisive issues (the mechanism attribution is not isolated from the optimized trigger and parameter count; the baselines and ASR definition make the margins hard to interpret) are shared by typical rejected submissions rather than by typical accepted ones, and the lack of any variance estimate removes the cushion for ablations with sub-1-point differences. The strongest reasons to accept (new attack surface, broad models and tasks) are real; they put the paper near the line, not over it, and they are largely recoverable in a revision (controls, variance, ASR definition, claim narrowing), so I rate it **Borderline Reject (3)**. The decision does not exceed any DA ceiling (none applies). On the venue scale the ICLR label for the final Overall 3 is "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})" (secondary status; not official wording).

**Journal-style recommendation:** not applicable (conference target); if mapped, Major Revision.

---

## Editorial Decision

## Paper: BadMoE: Backdooring Mixture-of-Experts LLMs via Optimizing Routing Triggers and Infecting Dormant Experts
## Submission ID: iclr26-2qn6AOIkL1
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC Prof. Ines Varga-Lindqvist; R1 Methodology Dr. Anika Sorensen-Pillai; R2 Domain Prof. Kwabena Ostrowski-Lee; R3 Perspective Dr. Lucía Montenegro-Hartwell; R4 Generalist Dr. Haruto Venkataraman; DA Prof. Selin Aldercott

---

## Decision: Borderline Reject (3)

*A simulation of how a careful panel would likely see this draft, not a prediction of the venue's outcome.*

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 4, DA 3 → mean **3.40** · official composite **59.4**
**EIC assessment** (internal): weighted rating **3.36** → starting point **3** · weighted composite **59.1** → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: **3**
**ICLR translation (scale status: secondary):** rating label "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})"; Soundness 2, Presentation 3, Contribution 3.
**EIC pool position:** about 52% (better than about 52% of ICLR submissions).

### Score Summary: Official Scores and EIC Assessment (script output, with EIC weights)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 52 | 58 | 62 | 60 | 48 | 56.0 | 55.6 | 14 |
| Clarity & Presentation | 66 | 66 | 68 | 68 | 64 | 66.4 | 66.3 | 4 |
| Novelty & Originality | 62 | 64 | 70 | 66 | 58 | 64.0 | 63.7 | 12 |
| Significance & Impact | 62 | 64 | 72 | 68 | 60 | 65.2 | 64.8 | 12 |
| Experimental Validation | 46 | 54 | 60 | 58 | 44 | 52.4 | 51.8 | 16 |
| Reproducibility | 50 | 52 | 56 | 56 | 50 | 52.8 | 52.6 | 6 |
| Ethical Compliance | 66 | 66 | 62 | 64 | 62 | 64.0 | 64.2 | 4 |
| **Composite** | 56.4 | 60.0 | 64.3 | 62.5 | 53.7 | **59.4 (before)** | **59.1 (after)** | |

No dimension spread exceeds 20 points. R2's own composite (60.0) implies band 4 versus its rating 3, and R4's pool position (65) is within the band for its rating; the script raised no cross-check flag.

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "BadMoE" to ICLR. Backdoor vulnerabilities that exploit expert routing in sparse LLMs are a timely topic, and the paper's three-stage attack, broad model and task coverage, and the ablation, prompt-shift and defense studies are valuable for a first paper on this surface.

**Overall Assessment:** The panel saw a clear, novel idea with broad evidence and consistently high attack success on OLMoE and Deepseek, but could not confirm that the proposed mechanism (poisoning dormant experts) is what produces the gains. Ratings split 3/3/4/4/3.

**Key Strengths Identified by Reviewers:**
1. A new, practically relevant attack surface on widely used open MoE models, with a realistic model-provider threat model (R3, R4, R2).
2. A coherent attack pipeline with module ablations, poisoning-rate, prompt/domain-shift and utility studies (R1, R4).
3. Strong results where the attack is stressed, e.g., near-100% ASR across six tasks on OLMoE and large gains on Samsum (R4, DA).

**Key Concerns Requiring Attention:**
1. The mechanism attribution is confounded with the optimized trigger and extra trainable parameters; the decisive controls are missing (R1, R4, DA, R2: CONSENSUS-4).
2. The baselines appear under-trained (≈ 0% ASR on Samsum, chance-level ASR on AGNews/IMDB for some), ASR is not defined to exclude target-class inputs, and most of the margin lies on two tasks (R1, DA: CONSENSUS-3).
3. No variance or seeds; sub-1-point ablation differences are within noise (R1, R4, DA).
4. The theory (§5) is not connected to the attack and the "rigorously prove" wording is overstated (R2, DA).
5. Several statements exceed the tables (§8.3 prompt consistency; §8.4 "better overall balance"; "ineffective" defenses; clean-model comparison) and there are citation and table slips (R2, R4, DA).

**Decision: Borderline Reject (3)**

The idea is promising and the reasons to accept are real, but the central causal claim and the comparison with baselines are not yet adequately supported. The controls requested below are inexpensive, and with them, narrower claims and variance estimates, the paper would likely be judged much more favorably. Please refer to the Revision Roadmap.

Sincerely,
Prof. Ines Varga-Lindqvist
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Mechanism not isolated (optimized trigger, trainable parameters, causal test) | R1, R4, DA, R2 | CONSENSUS-4 |
| Baseline strength / ASR definition / margin concentration | R1, DA, R4 | CONSENSUS-3 |
| Missing variance, seeds, significance | R1, R4, DA | CONSENSUS-3 |
| Defense evaluation narrow and non-adaptive | R1, R3, DA | CONSENSUS-3 |
| Text claims exceed tables | R2, R4, DA | CONSENSUS-3 |
| Table/text slips | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the contribution strong enough to accept? | R3, R4 (4) | R1, R2, DA (3) | Both sides agree on strengths; the disagreement is about how much the missing controls matter. EIC sides with the 3s because the controls bear on the main claim and baselines look floor-level |
| Significance and novelty | R3 (72/70) | DA (60/58) | Novelty is real for MoE but the algorithmic delta over trigger search is modest; significance depends on the unverified mechanism and on defense realism |

### Score Spread Discussion
No dimension exceeds the 20-point flag. The largest spread is Experimental Validation (44–60): R1 and DA score lower for confounds and floor-level baselines, R3 and R4 for breadth. The EIC adopts the lower view because the confounds were verified (Table 10, §6.3 vs §7.1).

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Mechanism confounded | Yes (R1, R4) | n/a | New experiments (≈ 30–40 GPU-h) |
| DA-M2 | MAJOR | ASR definition/baselines at floor | Yes (R1) | n/a | Re-evaluation; small tuning |
| DA-M3 | MAJOR | "consistent" prompt claim vs Table 5 | Yes (R2) | n/a | Rewording |
| DA-M4 | MAJOR | "rigorously prove" overclaim | Yes (R2) | n/a | Rewording / measurements |
| DA-M5 | MAJOR | Defenses "ineffective" | Yes (R1, R3) | n/a | New defense experiments |
| DA-M6 | MAJOR | Selection on eval data | Yes (R1) | n/a | Hold-out re-run |
| DA-M7 | MAJOR | Un-fine-tuned clean rows | Yes (R4) | n/a | Add rows |
| DA-M8 | MAJOR | Untested explanations | Yes (R2) | n/a | Remove or test |
No CRITICAL issues were raised.

---

## Revision Roadmap

### Priority 1: Required (must fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | Isolate the mechanism from the optimized trigger and trainable-parameter count | R1-W1, R4-W1, DA-M1, R2-W1 | §6.3, §7.1, Table 3, Table 10, Fig. 7 | Baselines with the optimized trigger; matched-parameter LoRA/expert controls; state exactly which parameters BadMoE trains; causal ablation of infected experts (R1-W6) | Medium; ≈ 30–40 GPU-h | Yes (partly: 2 models × 2 tasks) |
| P1-2 | Make baseline comparison interpretable | R1-W2, DA-M2, R4-W2 | Table 2, §7.1 | Define ASR on non-target inputs and report the floor; give baselines a tuning budget; add a clean-fine-tuned reference row | Medium; ≈ 20 GPU-h | Yes |
| P1-3 | Add seeds and variance | R1-W3, DA | Table 2, Table 3 | ≥ 3 seeds with mean ± std for at least OLMoE and Table 3 | Medium; ≈ 20 GPU-h | Partly |
| P1-4 | Align claims with evidence | R2-W1, R2-W5, DA-M3/M4/M5/M7 | Abstract, §5, §7.2, §8.3, §8.4, §8.5 | Narrow "rigorously prove", "consistent", "better overall balance", "ineffective"; fix clean-model wording | Low | Yes |

### Priority 2: Strongly suggested (should fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| P2-1 | Defense evaluation | R1-W5, R3-W3, DA-M5 | Expert-level fine-tuning, expert pruning, router anomaly detection, activation clustering and trigger inversion, on ≥ 2 models | Medium; 10–15 GPU-h | Partly |
| P2-2 | Selection on evaluation data | R1-W4, DA-M6 | Hold-out split for layer/N_a/n selection; report defenses on all six tasks | Medium | Partly |
| P2-3 | Citations and missing related work | R2-W2, R2-W3 | Fix [5], [81], [34], [31]; add universal adversarial triggers, LLM-era poisoning/backdoor papers, MoE-routing manipulation work `[verify]`; state the "first" search window | Low | Yes |
| P2-4 | Table/text inconsistencies | R1 Error Log, DA-m1/m2 | Fix Eq. (12), Tables 3, 4, 6, 10, §E text; clarify model in Table 6 | Low | Yes |
| P2-5 | Deployment realism | R3-W1, R3-W2 | ASR after int8/int4 quantization and expert pruning; expert usage across unrelated tasks | Low–Medium | Yes |
| P2-6 | Untested explanations | R2-W4, DA-M8 | Test or delete (§7.2 Samsum, §8.2 Table 4) | Low | Yes |

### Priority 3: Nice to fix (optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Dual-use/release plan | R3-W4 | Add a responsible-release and disclosure paragraph; pair with detection tooling |
| N2 | Mixtral weakness | R4-Q1 | Discuss why the 8-expert/top-2 model is weaker on three tasks |
| N3 | "less than 2%" phrasing | R1 Minor, DA-m4 | State per-layer share |
| N4 | Template and typos | R4 Minor | Use the venue template; fix "bone", "Tirgger" |

## Estimated Revision Effort
- Priority 1: 4 items, ≈ 70–80 GPU-hours plus 1–2 days of writing
- Priority 2: 6 items, ≈ 25 GPU-hours plus 2–3 days
- Priority 3: 4 items, < 1 day
- **Total estimated revision time**: roughly 2 weeks including experiments.

*No Post-Review Analysis (Gap Scout) was requested.*
