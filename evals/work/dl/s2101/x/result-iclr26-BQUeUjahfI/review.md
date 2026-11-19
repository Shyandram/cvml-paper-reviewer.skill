# Academic Paper Review: "Learning Tractable Distributions of Language Model Continuations" (LTLA)

Date: 2026-11-10 · Mode: full · Target venue: ICLR (2026 profile, scale status *secondary*) · Literature check: **strict, cutoff 2025-09-24, requested but not completed** (see Phase 1.5) · Simulation of how a careful panel would likely see this draft, not a prediction.

**Execution disclosure.** The five reviewer passes and the EIC pass were run one after another in a single model context (no subagents). They are role-based perspectives from a shared context, not independent agents. Figures 1–4 were not available (text extraction only); statements that depend on figures are judged from captions and text and flagged "figure-dependent". The integrity scan (`integrity_scan.py`) found no reviewer-directed text or hidden characters; the reviewers read the redacted copy, which is identical to the original.

---

## Phase 0: Paper Analysis and Reviewer Configuration Card

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Learning Tractable Distributions of Language Model Continuations |
| Primary Discipline | ML → tractable probabilistic models for controlled language generation |
| Secondary Discipline(s) | NLP (constrained decoding, detoxification); vision–language models |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | HMM surrogate of an LM; neural encoder predicting the HMM latent-state prior; Monarch-structured HMMs; Ctrl-G (DFA constraints) and TRACE-style attribute reweighting |
| Target Venue | ICLR (stated by user); profile key `iclr` |
| Venue-Specific Notes | none (ICLR form: Soundness / Presentation / Contribution 1–4, Rating, Confidence) |
| Paper Maturity | Submission-ready in form, short experimental section; appendix holds only proofs, DFA definition and complexities (A, B, C) |
| Ethics-Relevant Content | Detoxification on Hateful Memes with Perspective API toxicity scores; dual-use (steering toward toxicity); no limitations or broader-impact section |

### Claimed Contributions (as stated by the authors, §1)
1. **C1 (method).** LTLA: reuse the base LM to predict the prior of an HMM over continuations, with a fixed HMM decoder and one batched HMM update; extension to multimodal context via a VLM (§1, contribution 1; §3).
2. **C2 (design study).** Architectural choices for the neural encoder (linear / extra transformer layer / fine-tuned backbone) and the tractable decoder (dense vs Monarch), and their effect on modeling, overhead and downstream performance (§1, contribution 2; §3.2, §4.1).
3. **C3 (result).** Better conditional log-likelihood than standard HMMs, "especially for the next few tokens" (§1, contribution 3; Fig. 3, Fig. 4).
4. **C4 (result).** Improved constraint satisfaction in controlled generation for language models (Ctrl-G, CommonGen) and VLMs (TRACE-style detoxification on Hateful Memes) with small inference overhead (§1, contribution 3; Table 2, Table 3).

### Paper memory (factual record shared with all reviewers)
- **Setup facts.** Data are sequences sampled unconditionally from GPT2-large, GPT2-large fine-tuned on CommonGen, and Qwen2.5-VL-2B, length T = 32, uniformly random split position (§4 "Datasets"). Number of sampled sequences: not stated after search. Hidden sizes: shown only on the x-axis of Fig. 3. Optimizer: only "sensitive to the hyperparameters of the AdamW optimizer" (§4.1); values not stated. Seeds, runs, variance, compute (hardware, GPU-hours), batch size, epochs, learning rate: not stated after search. Code / data availability: not stated. Evaluation split for CommonGen (Table 2): not stated. Ctrl-G: "128 beams" and "select the top hypothesis by base-LM log-likelihood" (§4.2). VLM: "distill LTLA from Qwen2-VL-Instruct-2B" (§4.2) versus "Qwen2.5-VL-2B" (§4 Datasets).
- **Headline numbers.** Table 2 (BLEU-4, CIDEr, ROUGE-L, average / max perplexity at max length 20 and 32); Table 3 (toxicity 0.064 vs 0.087 vanilla, perplexity 3.564 vs 2.359); "approximately 10× the LTLA decoding time" for the MC baseline (§4.2). No numeric table for the distillation experiment (Figures 3–4 only).
- **Appendix content.** A: proof of the proposition (restated as "Proposition 2"); B: DFA definition; C: Table 4 complexities. No extra experiments, no implementation details.
- **Unverifiable.** Figures 1, 3, 4 (extraction only). The "Neural Monarch HMM" row of Table 3 does not say which encoder variant it uses.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Rafael Quintero-Ashby, large public research university (North America)
- **Seniority / Expertise**: Senior faculty / probabilistic machine learning, decoding-time control of LMs
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Judges against what ICLR actually accepts; asks whether the headline claim is *measured*.

### Reviewer 1 (Methodology): Dr. Tobias Wennerlund, industrial research lab (Northern Europe)
- **Seniority / Expertise**: Senior industry scientist / sequence-model distillation, evaluation of constrained decoding
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on matched compute and on every claimed number having a table.

### Reviewer 2 (Domain): Prof. Ananya Raghunathan-Fox, public research university (South Asia)
- **Seniority / Expertise**: Senior faculty / tractable probabilistic circuits, HMM language models
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Checks novelty claim by claim against the closest prior work.

### Reviewer 3 (Perspective): Dr. Kofi Adjei-Marlow, speech and signal-processing group, university (West Africa)
- **Seniority / Expertise**: Mid-career / structured state-space models, speech recognition decoding
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive and expansive; the most positive voice, but flags missing measurements.

### Reviewer 4 (Generalist): Dr. Siew Hwa Lim-Corda, vision-and-language lab, university (Southeast Asia)
- **Seniority / Expertise**: Mid-career / multimodal learning, generation
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; weighs weaknesses against typical accepted papers.

### Devil's Advocate: Prof. Daniela Brandt-Okafor, statistics department, public university (Central Europe)
- **Seniority / Expertise**: Senior faculty / evaluation methodology, causal inference
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; checks every superlative against a table.

*Personas are fictional.*

---

## Phase 1: Five Reports

# Peer Review Report (R1)

## Paper: Learning Tractable Distributions of Language Model Continuations
## Reviewer: Dr. Tobias Wennerlund, Methodology (industrial research lab, Northern Europe; fictional persona)
## Expertise: sequence-model distillation; constrained-decoding evaluation; HMM training
## Date: 2026-11-10

## Summary
The paper keeps an HMM as the tractable lookahead model but replaces its prefix encoder (the forward filter) by a neural network that reads the base LM's hidden states and outputs a prior over the HMM latent state (§3, Eq. 7). The HMM decoder stays fixed, so the backward tables used by Ctrl-G or TRACE can be precomputed and reused. The authors compare neural-encoded HMMs with standard HMMs in perplexity on sampled continuations (Figs. 3–4), then plug them into Ctrl-G on CommonGen (Table 2) and a TRACE-style toxicity controller for captioning on Hateful Memes (Table 3).

## Strengths
### S1: The design isolates the right degree of freedom
Conditioning only the latent prior while the transition and emission matrices stay fixed (§3, Eq. 7; §3.1 "Complexity") keeps Ctrl-G / TRACE precomputation valid, and Table 4 (Appendix C) states the complexity consequences relative to full conditioning.
### S2: The motivating example and the complexity argument are concrete
Figure 1 gives a readable example of prefix insensitivity (caption: "they fired the <x> after just one"), and §3.1 explains why per-prefix HMM parameters give decoding time quadratic in length.
### S3: Useful, honest negative finding on prior HMM-training tricks
§4.1 reports that the neural reparameterization plus latent variable distillation of Lee & Berg-Kirkpatrick (2025) worsened results and that AdamW hyperparameters matter, which is useful for the community (but see W5).
### S4: Two constraint families, one of them multimodal
The paper attempts hard (DFA) and soft (attribute) control, and a VLM setting that a text-only HMM cannot address (§4.2).

## Weaknesses
### W1: Downstream gains are within noise and in places negative, yet described as "significant" (E5)
Table 2 shows differences of 0.002–0.016 in BLEU-4 and CIDEr, from single runs with no variance. At length 20 the Transformer-Block row is *below* the standard HMM on BLEU-4 (0.297 vs 0.301), CIDEr (1.536 vs 1.552) and ROUGE-L (0.446 vs 0.448); the Linear row has *worse* average perplexity (41.99 vs 39.59). §4.2 nevertheless states "LTLA leads to significant improvements" and "consistent syntactical gains … across metrics". At length 32 CIDEr is identical for Standard and Linear (1.566) and ROUGE-L is identical across all rows (0.448).
- **Suggested Fix**: Run ≥ 3 seeds (and different DFA keyword sets) per row, report mean ± std and a paired bootstrap over the CommonGen instances; reword the claims to what survives. Cost: Ctrl-G with 128 beams on CommonGen for 3 models × 3 seeds, roughly 20–40 GPU-hours.
### W2: The headline downstream comparison for VLMs omits the baseline that tests the claim
Table 3 compares "Neural Monarch HMM" against Vanilla, Prompting and Sampling but not against the standard (text-only) HMM under the same TRACE controller, which is the only comparison that shows the neural encoder (and thus visual context) matters (abstract: "a standalone HMM cannot encode visual context"). The Sampling baseline is capped at k = 1 and gives perplexity 43.142 and *higher* toxicity than Vanilla (0.097 vs 0.087), which indicates a broken rather than a competitive baseline. No VLM distillation likelihood (LL/perplexity of Qwen continuations) is reported, although the abstract says LTLA "approximates continuation distributions for vision–language models".
- **Suggested Fix**: Add (i) a standard-HMM TRACE row, (ii) a text-LM TRACE experiment (RealToxicityPrompts) so numbers can be compared with the original TRACE paper, (iii) a stronger sampling baseline (e.g., SMC / twisted SMC with several particles) at matched wall-clock, and (iv) VLM continuation perplexity for the neural vs standard HMM.
### W3: Fluency and caption-quality evidence for Table 3 is thin, and the cost is understated
LTLA raises perplexity from 2.359 to 3.564 (+51%, derived), described as "preserving fluency" (§4.2). Perplexity is measured by the base model itself, so it penalizes any steering; no image–caption relevance (CLIPScore, CIDEr) or human check is given, so a toxicity drop of 0.023 absolute (0.087 → 0.064) may come from blander captions. Base toxicity is already low (0.087), and no variance over images or decoding seeds is reported.
- **Suggested Fix**: Report caption quality (reference-based and image-grounded), Perspective-score distributions (e.g., fraction above 0.5), and confidence intervals via bootstrap over images.
### W4: Efficiency claims are asserted from complexity, not measured
"Minimal inference overhead" (abstract) and "Low" decoding overhead (Table 1) are supported only by Table 4 (asymptotic) and one sentence that MC is "approximately 10× the LTLA decoding time" (§4.2). There is no wall-clock / memory comparison of LTLA vs standard HMM, nor across encoder variants (linear, extra layer, fine-tuned backbone), although contribution 2 (§1) promises to study "decoding overhead". The fine-tuned-backbone variant (Fig. 2(c)) changes the LM, so it cannot "reuse the same base LM" for generation without a second forward pass.
- **Suggested Fix**: Table of ms/token and peak memory (hardware, batch size, precision) for HMM, LTLA-linear, LTLA-layer, LTLA-finetune on both settings.
### W5: Missing protocol details make the results unreproducible (E8)
After a text search of the whole paper (including appendices A–C): number of training sequences, optimizer settings, learning rate, epochs, batch size, hidden sizes of the compared models in Table 2/3, seeds, compute, code release, and the evaluation split for Table 2 are not stated. The statement that Lee & Berg-Kirkpatrick's techniques "worsen performance" (§4.1) is given without numbers; the tuning split for "appropriate hyperparameters" for the baseline HMM is not stated.
- **Suggested Fix**: Add an implementation appendix with all of the above and the baseline-tuning protocol; release code.
### W6: The central comparison is not compute- or parameter-matched
The encoder uses a frozen GPT2-large (≈774M parameters) plus a head or layer; the baseline HMM has none of this capacity. Fig. 3 varies hidden size, but a fair test of whether *neural context* (rather than extra parameters/compute) helps needs at least a small non-neural baseline of comparable FLOPs and, importantly, the "Prefix-Parameterized TPM" row of Table 1, which is never evaluated, so the cost-benefit of conditioning only the prior is unknown (figure-dependent for the scaling plots).
- **Suggested Fix**: Add the full-conditioning variant at small H, and plot perplexity against decode-time FLOPs.

### Error Log
| ID | Cat. | Location | Verbatim quote | Why it is an error | How verified | Conf. | Sev. | Fix |
|----|------|----------|----------------|--------------------|--------------|-------|------|-----|
| ERR-1 | E5/E1 | §4.2 vs Table 2 | "slashing the maximum perplexity by more than half" | Max perplexity vs 1569.51: 616.73 (−60.7%) and 671.88 (−57.2%) halve; 1458.38 (−7.1%) and 1065.47 (−32.1%) do not (2 of 4 neural rows) | Recomputed from Table 2 | High | MAJOR | State per-row, add robust fluency statistic (median / 95th pct.) |
| ERR-2 | E5 | §4.2 vs Table 2 | "consistent syntactical gains over the standard HMM across metrics including BLEU-4, Cider, and RougeL" | At length 20 Transformer-Block is lower on all three; ROUGE-L equal to the standard HMM in 3 of the 4 neural-vs-standard comparisons | Cross-referenced Table 2 rows | High | MAJOR | Narrow wording, add variance |
| ERR-3 | E6 | §3.2.1 vs Appendix A | "Although Proposition 2 provides a strong motivation" | Result is stated as "Proposition 1" in §3.2.1 and restated as "Proposition 2" in Appendix A | Cross-referenced | High | MINOR | Fix numbering |
| ERR-4 | E6 | §4 Datasets vs §4.2 | "Qwen2.5-VL-2B" / "Qwen2-VL-Instruct-2B" | Two different VLM names for the VLM data and the distilled model | Cross-referenced | High | MINOR | State the exact model once |
| ERR-5 | E8 | Abstract / §1 vs §4 | "with minimal inference overhead" | No latency or memory measurement is reported for LTLA | Search of all sections | High | MAJOR | Add timing table |

**Minor**: Table 2 gives identical max perplexity for Standard HMM at both lengths (1569.51) (is this the same outlier sample?); typos ("surpisingly", "a-axis", "it learns to injects", "computing such conditional queries exactly and efficiently"); Krause et al. (2020, 2021) are the same GeDi paper listed twice.

## Missing References
Not my focus (see R2).

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Sound idea, but the downstream evidence is single-run and partly contradicts the text |
| Clarity | 3 | Mostly clear; some inconsistencies (ERR-3, ERR-4) |
| Significance | 2 | Value depends on downstream gains that are not demonstrated |
| Originality | 2 | Natural, modest extension of Ctrl-G / TRACE HMMs |

## Dimension Scores (0–100)
**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main claim (neural context helps the downstream controller) rests on Table 2 differences within plausible noise and on a Table 3 without the key HMM baseline; protocol details are missing.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Method sound; evidence–claim gaps (W1, W2, ERR-1/2) |
| Clarity & Presentation | 62 | Competent | Readable; numbering/model-name slips |
| Novelty & Originality | 54 | Developing/Competent | Encoder swap in an existing framework |
| Significance & Impact | 50 | Developing | Downstream benefit unproven |
| Experimental Validation | 42 | Developing | Single runs, missing HMM baseline in Table 3, no timing |
| Reproducibility | 38 | Developing | No hyperparameters, data sizes, compute or code |
| Ethical Compliance | 55 | Competent | No limitations section; dual-use not discussed |

## Questions for Authors
1. What are the means and standard deviations over seeds for Table 2, and what is the CommonGen split used? (A gap of ≤ 0.01 BLEU-4 with std ≥ 0.005 would lower my view of C4 further.)
2. What does a standard-HMM TRACE row look like in Table 3? (If LTLA clearly beats it, I would move Experimental Validation up by ~8 points.)
3. By the paper's own formula (§3.2.1) with V = 50,257 (GPT-2 vocabulary; assumed), τ for Monarch h = 16384 is about 8.5M (16384^1.5 ≈ 2.1M plus 128·V ≈ 6.4M) versus about 52.5M for dense h = 1024 (1024² + 1024·V). §4.1 calls these "comparable". Which constants and which vocabulary size support "comparable compute"? (derived, medium confidence)
4. Which encoder variant is the "Neural Monarch HMM" in Table 3?

## Limitations Assessment
**Partially.** No limitations section exists. Add: dependence on a distillation dataset sampled from the base LM, failure when the LM drifts from its sampled distribution, cost of the encoder, and the scope of constraints tested.

## Ethics Review Flag
**No.** (Toxicity control is benign; dual-use should be noted.)

## Overall Score
**3**: Reasonable idea with clean complexity argument, but downstream claims are not supported at the strength stated and key controls and details are missing.

## Confidence
**4**: Read the full text including appendices; figures not viewed.

---

# Peer Review Report (R2)

## Paper: Learning Tractable Distributions of Language Model Continuations
## Reviewer: Prof. Ananya Raghunathan-Fox, Domain (public research university, South Asia; fictional persona)
## Expertise: tractable probabilistic circuits; HMM language models; controlled decoding
## Date: 2026-11-10

## Summary
LTLA is a hybrid of a neural prefix encoder and a fixed HMM decoder to approximate an LM's continuation distribution so that exact queries (DFA acceptance, factorized classifiers) can be computed. It positions itself against sampling-based steering, learned future discriminators, and HMM distillation (Ctrl-G, TRACE), and shows perplexity improvements plus two controlled-generation experiments.

## Strengths
### S1: Clear conceptual separation of "lookback" and "lookahead"
§1 and §3 articulate that only the decoder must be tractable (§3, "Our key insight …"), which is a clean way to see why the HMM's forward filter can be replaced.
### S2: Fits the existing tractable-control pipeline without changing it
Eq. 8 and the Ctrl-G recap in §3.1 show the drop-in nature, and Table 1 positions four alternatives along four axes.
### S3: Reasonable related-work scope for the tractable-modeling community
§5 cites the relevant TPM lines (Zhang et al. 2023; 2024; Yidou-Weng et al. 2025; Chiu & Rush 2020; Lee & Berg-Kirkpatrick 2025; Shao et al. 2020; Dos Martires 2024).

## Weaknesses
### W1: Novelty is incremental and not delineated against hybrid neural/tractable models
The only new element relative to Ctrl-G / TRACE is the encoder for q(z_t | x_≤t) (Eq. 7). The closest conceptual neighbors the paper itself cites, conditional sum-product networks (Shao et al. 2020) and probabilistic neural circuits (Dos Martires 2024), are dismissed in one sentence in §5 ("similar to hybrid neural and tractable models in other settings"). The paper should state what is different in kind (fixed decoder for reuse) and test it. Contribution C2 (architecture study) is a small sweep of three encoder heads (Fig. 2) and a dense vs Monarch choice taken from Zhang et al. (2025a).
- **Suggested Fix**: A novelty delta paragraph and a quantitative comparison with at least one prior neural-conditioned tractable model; discuss the relation to neural HMMs of Chiu & Rush (2020), which already parameterize HMMs with neural nets.
### W2: The motivating claim "HMMs are insensitive to the prefix" is shown by one example
§1 and §2 ("a HMM trained to approximate a GPT2-large … unable to effectively encode dependence on context") rest on Fig. 1 (one context, *they fired the <x> after just one*). An HMM's forward filter q(z_t | x_1:t) does depend on the prefix; the real limitation is the capacity of the discrete state (the paper's own Proposition 1: I(X_<t; X_≥t) ≤ log|Z|). A quantitative statistic (e.g., average KL between continuation distributions under different contexts, or an estimate of mutual information captured) is missing, and the proposition applies to neural-encoded HMMs with the same bound, so §3.2.1 does not explain why an arbitrary encoder helps (it improves how the H states are used, not the cap).
- **Suggested Fix**: Report a quantitative context-sensitivity metric for HMM, LTLA and the LM, and discuss how the bound relates to the observed gain.
### W3: Positioning against decoding-time controllers is thin
§5 lists FUDGE, GeDi, NADO, COLD, SMC variants but experiments compare only to the HMM of Ctrl-G, prompting and one-particle MC. Learned prefix/value scorers for controlled decoding are not discussed (see Missing References).
- **Suggested Fix**: Add a short comparison or discussion; at least one learned future-discriminator baseline in the detoxification setting.
### W4: Claim "state-of-the-art" for tractable surrogates is not backed
The conclusion says LTLA "significantly boosts the perplexity of tractable models over the prior state-of-the-art" (§5); the compared prior art is the authors' own tuned standard HMM, and the reference method of Lee & Berg-Kirkpatrick (2025) is reported to be worse than the standard HMM without numbers (§4.1).
- **Suggested Fix**: Report the numbers and describe the HMM baseline training in the same detail as LTLA.
### W5: Citations
CommonGen (the benchmark of Table 2), GPT-2 and the Qwen VL models are used without a reference in the bibliography; Krause et al. 2020 and 2021 are the same paper; Choi et al. (2019, IJAR) is cited for tractable models being "less expressive than … neural autoregressive models" (§2), but that paper concerns Bayesian vs neural networks, so the support is indirect (medium confidence; stated as a question below).
- **Suggested Fix**: Add the missing citations and de-duplicate.

## Missing References
*Literature check could not run (arXiv API returned HTTP 429 / timeouts), so none of these were verified with `related_search.py verify`; each is given from memory and marked [verify] unless I am sure it exists as described. All are older than the cutoff. No search was made for the reviewed paper.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Important | Mudgal et al., "Controlled Decoding from Language Models", ICML 2024 [verify] | Learned prefix scorers for future reward used at decoding time; direct alternative to tractable lookahead |
| Important | Liu et al., "DExperts: Decoding-Time Controlled Text Generation with Experts and Anti-Experts", ACL 2021 | Standard detoxification baseline at decoding time |
| Important | Lin et al., "CommonGen: A Constrained Text Generation Challenge for Generative Commonsense Reasoning", Findings of EMNLP 2020 | Benchmark used in Table 2 but not cited |
| Helpful | Dathathri et al., "Plug and Play Language Models: A Simple Approach to Controlled Text Generation", ICLR 2020 | Classic attribute-controlled decoding |
| Helpful | Deng & Raffel, "Reward-Augmented Decoding: Efficient Controlled Text Generation With a Unidirectional Reward Model", EMNLP 2023 [verify] | Cheap learned reward model on prefixes, comparable overhead profile |
| Helpful | Gloeckle et al., "Better & Faster Large Language Models via Multi-token Prediction", ICML 2024 [verify] | Predicting several future tokens from hidden states: related to the "context-aware lookahead from LM hidden states" idea |

**Citation check (E7).** Checked from the paper's own text: (i) Zhang et al. (2023) is described as "state-of-the-art performance on controlled generation benchmarks" (§2), consistent with the Ctrl-G / GeLaTo line; (ii) the claim that Lee & Berg-Kirkpatrick (2025) advocate neural reparameterization plus latent variable distillation (§4.1) cannot be checked without the paper; the authors should quote the setting. No wrong-paper mapping was found.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Evidence for downstream benefit is weak |
| Clarity | 3 | Clear overall |
| Significance | 2 | Narrow community, modest demonstrated gain |
| Originality | 2 | Incremental over Ctrl-G / TRACE HMMs |

## Dimension Scores (0–100)
**Pool position:** better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a sensible, clean idea with modest novelty and an experimental section that does not show how much the encoder matters downstream.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Sound formulation, Prop. 1 elementary |
| Clarity & Presentation | 62 | Competent | Well organized; Table 1 helpful |
| Novelty & Originality | 56 | Competent | Encoder replacement; closest hybrids only mentioned |
| Significance & Impact | 54 | Developing/Competent | Useful to TPM-control users |
| Experimental Validation | 46 | Developing | Narrow baselines |
| Reproducibility | 42 | Developing | Details not stated |
| Ethical Compliance | 58 | Competent | Little discussion, low risk |

## Questions for Authors
1. How does LTLA differ from, and compare with, conditional SPNs or probabilistic neural circuits for this task? (A matched comparison would raise Novelty.)
2. Does Choi et al. (2019) support the §2 statement about tractable vs autoregressive expressiveness? Please quote or cite a better source.
3. Can you show a quantitative context-sensitivity measure behind the §1 claim?

## Limitations Assessment
**Partially.** No limitations section.

## Ethics Review Flag
**No.**

## Overall Score
**3**: A sound but incremental extension whose empirical justification is thin for ICLR.

## Confidence
**4**: Know the TPM-control literature; literature check unavailable.

---

# Peer Review Report (R3)

## Paper: Learning Tractable Distributions of Language Model Continuations
## Reviewer: Dr. Kofi Adjei-Marlow, Perspective (speech / state-space group, university, West Africa; fictional persona)
## Expertise: HMM-based decoding in speech recognition; structured state-space models
## Date: 2026-11-10

## Summary
The paper revisits an old idea in sequence modeling, a neural network that provides the state prior to an HMM, and applies it to give LMs an exact, cheap lookahead for constraint satisfaction. The contribution is to preserve the HMM's reusable backward computation while making the encoder as rich as the LM itself.

## Strengths
### S1: A neat bridge between neural encoders and exact inference
This resembles hybrid hidden-Markov/neural acoustic models, where a neural network produces state posteriors and a structured decoder does exact search; §3 makes the same separation of "encode the past" and "search the future".
### S2: Plug-and-play with arbitrary constraints
Because only the encoder changes, one trained surrogate serves many constraints (§2, "amortizes the cost across different constraints α"); Ctrl-G (DFA) and TRACE (classifier) are both shown (§4.2).
### S3: Multimodal reach
Using a VLM's hidden states lets an HMM, which has no mechanism for images, condition on visual context (§1, §4.2), an elegant use of existing representations.
### S4: Deployment-oriented complexity analysis
Table 4 (Appendix C) makes memory and time scaling explicit, including the batch-size blow-up of full conditioning.

## Weaknesses
### W1: Deployment claims are not measured
"Negligible overhead" for the linear head (§3.2.2) and "negligible inference overhead" (§4.2) depend on the HMM step cost (τ = O(h² + hV), §3) at large hidden sizes and vocabularies; the HMM forward step over *all* V candidates is not free next to a small VLM (Qwen 2B). A wall-clock table on the target hardware would turn a plausible claim into a usable one.
- **Suggested Fix**: Report tokens/s and memory vs the base model and vs a standard HMM.
### W2: Assumption that the surrogate remains valid under steering
The surrogate is distilled from *unconditional* samples of the LM (§4 "Datasets"), but during controlled decoding the prefix distribution is shifted toward the constraint (e.g., toxic-avoiding captions). Neural encoders may extrapolate worse than the HMM filter to such shifted prefixes. No analysis of on-policy vs off-policy prefixes is given.
- **Suggested Fix**: Evaluate the surrogate's continuation perplexity on prefixes produced during controlled decoding, or fine-tune with on-policy samples.
### W3: Evaluation of the multimodal benefit and safety framing
Detoxifying captions of Hateful Memes with a Perspective-API-scored classifier (§4.2) captures lexical toxicity but not the multimodal harm of a meme whose caption is innocuous; Perspective is known to be biased across dialects. The paper has no limitations or broader-impact discussion, and the same steering could be used to *increase* toxicity.
- **Suggested Fix**: Add a short impact and limitations section; add a human check on a small sample.
### W4: Connections to other fields are missing
Hybrid neural/HMM models in speech (hybrid DNN-HMM, transducer lattices) and weighted-finite-state-transducer composition are natural precedents and tools: the DFA product in Ctrl-G is WFST composition. Discussing these would clarify what is new and open directions (e.g., HSMMs for length control).
- **Suggested Fix**: Add a paragraph in §5; consider HSMM or state-space decoders to tackle the log-H cap of Proposition 1.

## Missing References
Not my focus; see R2.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound formulation; experiments adequate for a first demonstration |
| Clarity | 3 | Clear |
| Significance | 3 | A practical building block for controllable decoding |
| Originality | 3 | A fresh application of a known pattern |

## Dimension Scores (0–100)
**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a practical, well-motivated idea with a plausible efficiency story; experiments are thin, which keeps it on the borderline side of the bar for me.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound derivation (Eq. 7–8) |
| Clarity & Presentation | 68 | Competent | Clear structure |
| Novelty & Originality | 62 | Competent | Known pattern, new setting |
| Significance & Impact | 66 | Competent | Reusable component |
| Experimental Validation | 56 | Competent | Adequate demonstration, thin |
| Reproducibility | 55 | Competent | Method reproducible in outline; hyperparameters absent |
| Ethical Compliance | 60 | Competent | Low risk, no discussion |

## Questions for Authors
1. What is the measured tokens/s of LTLA vs the vanilla VLM at the HMM sizes used in Table 3? (A small overhead would raise my Significance score.)
2. How does the surrogate behave on prefixes generated under control?
3. Would an HSMM or state-space decoder lift the log-H bound?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**4**: A useful, pragmatic building block that deserves to be seen, despite thin experiments.

## Confidence
**3**: Outside the TPM-for-LM niche; comparisons with prior TRACE/Ctrl-G numbers not checked.

---

# Peer Review Report (R4)

## Paper: Learning Tractable Distributions of Language Model Continuations
## Reviewer: Dr. Siew Hwa Lim-Corda, Generalist (vision-and-language lab, university, Southeast Asia; fictional persona)
## Expertise: multimodal generation; VLM evaluation
## Date: 2026-11-10

## Summary
LTLA lets an LM's own hidden states set the latent prior of a fixed HMM that models the continuation, so that exact constraint probabilities can be computed quickly while using richer context than an HMM alone can encode. The contribution, in one paragraph: a better surrogate for LM continuations at the same decoding cost, shown with perplexity curves and two controlled-generation demos.

## Strengths
### S1: A simple idea explained with a helpful comparison table
Table 1 lists tractability, context awareness, extra LM calls, reuse and overhead for five alternatives, which makes the design rationale easy to follow.
### S2: Respectable breadth for a methods paper
Language (CommonGen, GPT-2) and vision–language (Hateful Memes, Qwen VL) settings, dense and Monarch HMMs, three encoder heads (Fig. 2).
### S3: Honest remarks on what did not help
Monarch with a very large hidden size did not beat compute-matched dense HMMs (§4.1) and some prior tricks hurt.
### S4: Generally readable
The structure from motivation to complexity to experiments is easy to follow for a non-specialist.

## Weaknesses
### W1: Venue-criteria checklist (ICLR): evidence for the central claim is partly met
| Criterion | Status | Location |
|-----------|--------|----------|
| Claims supported by evidence | Partly: distillation claim by figures (not viewed), downstream claims not supported at stated strength | §4.1, Table 2, Table 3 |
| Soundness of method | Met | §3, Eq. 7–8 |
| Significance to audience | Partly: niche (TPM-based control) | §1, §5 |
| Presentation | Partly: tables clear, but protocol details and some naming slips | §4, §4.2 |
| Reproducibility | Not met: no code, hyperparameters, data sizes | §4 |
### W2: Abstract wording is stronger than the experiments
The abstract and §1 say LTLA "improves constraint satisfaction". Table 2 reports reference-overlap metrics and perplexity; no constraint-satisfaction rate is given (hard DFA constraints under Ctrl-G are satisfied by construction, so success rate cannot differentiate the methods), and Table 3 reports toxicity of captions, not a satisfaction metric. "Substantially / significant" is used for differences that are small (§4.2).
- **Suggested Fix**: Align the abstract with the measured quantities ("reference-overlap and perplexity under hard constraints", "caption toxicity").
### W3: VLM contribution is under-documented
The VLM story (a headline point of the abstract) occupies one paragraph and Table 3. The reader cannot tell which encoder variant and hidden size were used, how the log-linear toxicity model is trained beyond "trained on RealToxicityPrompts" (§4.2), or how many images/captions were evaluated. The qualitative side (example captions) is absent.
- **Suggested Fix**: Add the setup details and 4–6 random (not curated) captions with and without control.
### W4: Distillation results exist only as plots
RQ1–RQ2 are answered with Figures 3–4 and no numbers; a table (perplexity at fixed hidden sizes, per encoder, per continuation length) would let readers verify "consistently reduces perplexity" (§4.1) (figure-dependent; not verified by me).
- **Suggested Fix**: Add a numeric table of Fig. 3/4 values with variance.
**Minor**: spacing/typos listed by R1; duplicated Krause references; benchmark and base-model citations missing.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Claims outpace evidence |
| Clarity | 3 | Clear |
| Significance | 2 | Niche, gains unproven |
| Originality | 2 | Incremental |

## Dimension Scores (0–100)
**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: typical rejected-submission signals (gain over closest prior work small and not shown with variance, narrow setting, missing details) outweigh a clean method.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing/Competent | Sound design, evidence gaps |
| Clarity & Presentation | 64 | Competent | Table 1 and flow are good |
| Novelty & Originality | 56 | Competent | Incremental |
| Significance & Impact | 52 | Developing | Niche |
| Experimental Validation | 46 | Developing | Thin |
| Reproducibility | 44 | Developing | Details missing |
| Ethical Compliance | 56 | Competent | No limitations section |

## Questions for Authors
1. Which results show *constraint satisfaction* improved, as claimed in the abstract? (A satisfaction/success metric on soft constraints would address this.)
2. Which encoder and hidden size produce Table 3?
3. How many captions were scored in Table 3?

## Limitations Assessment
**No** (no dedicated section).

## Ethics Review Flag
**No.**

## Overall Score
**3**: A clean idea that a typical ICLR panel would likely find under-validated.

## Confidence
**4**: Comfortable with the VLM side; less with HMM details.

---

# Devil's Advocate Report

## Paper: Learning Tractable Distributions of Language Model Continuations
## Reviewer: Prof. Daniela Brandt-Okafor, evaluation methodology (public university, Central Europe; fictional persona)

## Steelman
Standard HMMs distilled from an LM are cheap and exact but poor at using context; letting the LM's own hidden states set only the HMM's latent prior preserves tractability and lets context in, so conditional-query estimates and, with them, Ctrl-G / TRACE controllers should get better at nearly zero cost, including for VLMs.

## Core Argument Chain
1. P1: Standard HMM surrogates are weakly context aware (Fig. 1).
2. P2: A neural prior over the latent state increases the surrogate's likelihood of continuations (Figs. 3–4).
3. P3: The extra encoder keeps backward tables reusable, so overhead is low (§3.1, Table 4).
4. P4: Better surrogate likelihood translates into better control (Table 2, Table 3).
5. P5: Visual context can enter via a VLM encoder (Table 3).
∴ LTLA is a better tractable surrogate that improves constraint satisfaction with minimal overhead, text and multimodal.

## Strongest Counter-Argument
The chain breaks at P4 and P5, the two links that give the paper its practical meaning. For P4, the only controlled-generation evidence for language models is Table 2, where the effects are in the third decimal (BLEU-4 0.301 / 0.303 / 0.297; CIDEr 1.552 / 1.566 / 1.536), the sign flips across rows and lengths, runs are single, and the "constraint satisfaction" named in the abstract is not measured (a DFA-constrained Ctrl-G decode satisfies the constraints by construction, so the informative metrics are quality metrics, which barely move). The one large effect, "maximum perplexity" falling from 1569.51 to 616.73, is a max-statistic over outputs; a single outlier decode controls it, and the Standard-HMM value is *identical* at both lengths (1569.51), which suggests the same outlier, so it says little about the encoder. For P5, Table 3 lacks the control that tests the claim: a text-only standard HMM running the same TRACE controller. Without it, the toxicity reduction (0.087 → 0.064) cannot be attributed to visual or neural context rather than to the controller alone. The comparators that remain are a one-prompt instruction and a one-particle MC estimator whose perplexity is 43.142 and whose toxicity is *higher* than vanilla, which indicates a degenerate baseline, not evidence that tractable lookahead beats sampling. Meanwhile LTLA raises perplexity by 51% (2.359 → 3.564). Everything else (P1–P3) is plausible but mostly unmeasured: P1 has one example, P3 has no timing. The authors can answer this by adding variance, an HMM-TRACE row, a satisfaction metric and timing; until then the downstream claim is "better surrogate likelihood, downstream effect unclear", which is a weaker paper than the one summarized in the abstract.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim (neural encoding improves distillation likelihood) is plausible and not contradicted; the problems narrow the claims and are fixable by evidence additions or rewording. No test-set selection is stated: Ctrl-G's "select the top hypothesis by base-LM log-likelihood" (§4.2) is selection by a score independent of the reported references.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence (E5) | Abstract; §4.2; Table 2 | "improves constraint satisfaction" is not measured; "significant improvements" rests on ≤ 0.016 differences in single runs, sign-flipping across rows | Add satisfaction metrics, seeds + CIs; reword |
| DA-M2 | Evidence/Logic | Table 3; §4.2 | No standard-HMM TRACE row, so neural/visual-context benefit is untested; Sampling baseline degenerate (k = 1, perplexity 43.142, toxicity 0.097 > 0.087) | Add rows; stronger sampling baseline at matched time |
| DA-M3 | Scope | Abstract; §4.1 | "approximates continuation distributions for VLMs" has no VLM likelihood result (§4.1 reports GPT2-large only) | Add VLM perplexity, neural vs HMM |
| DA-M4 | Alternative explanation | Fig. 3 (figure-dependent); §3.2.2 | Gain may come from added parameters/compute of a frozen GPT2-large encoder; no matched baseline; "Prefix-Parameterized TPM" (Table 1) never evaluated | Compute-matched baseline; full-conditioning at small H |
| DA-M5 | Evidence | §4.2 "approximately 10×"; Table 1 | Overhead claims are asymptotic; no timing for LTLA vs HMM | Timing table |
| DA-M6 | Logic | §3.2.1, Proposition 1 | The bound is identical for standard and neural-encoded HMMs, so it motivates larger H, not the neural encoder; and §4.1 finds larger Monarch H did not help | Reframe the role of Prop. 1 |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | §3.2.1 / App. A | Proposition 1 vs "Proposition 2" |
| DA-m2 | Consistency | §4 vs §4.2 | Qwen2.5-VL-2B vs Qwen2-VL-Instruct-2B |
| DA-m3 | Evidence | Table 2 | Max perplexity of Standard HMM identical (1569.51) at both lengths |
| DA-m4 | Evidence | §4.1 | Claims about Lee & Berg-Kirkpatrick (2025) given without numbers |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| "slashing the maximum perplexity by more than half" | 1569.51 → 616.73 / 671.88 / 1065.47 / 1458.38 | −60.7% / −57.2% / −32.1% / −7.1% | Partly (2 of 4 rows) |
| Toxicity reduction vs Vanilla | 0.087 → 0.064 | −0.023 abs, −26.4% rel; max toxicity 0.249 → 0.188 = −24.5% | Consistent |
| "preserving fluency" | Perplexity 2.359 → 3.564 | +51.1% | Not preserved relative to vanilla (still far below Sampling 43.142) |
| Table 2 Transformer-Block vs Standard HMM, length 20 | BLEU-4 0.297 vs 0.301; CIDEr 1.536 vs 1.552 | −0.004; −0.016 | Contradicts "consistent gains" |
| Monarch 16384 vs Dense 1024 "comparable compute" | §4.1 | ≈ 8.5M vs ≈ 52.5M by §3.2.1 formulas with V = 50,257 (assumed) | Unclear; depends on constants (medium confidence) |

## Ignored Alternative Explanations
- The gain in Fig. 3/4 may come from parameters and compute of a 774M-parameter frozen encoder (a question of matched baseline).
- Perplexity reductions at short continuation lengths (Fig. 4) may reflect that next-token prediction from the LM state (which is exactly what the LM's own distribution provides) is leaking into the surrogate, rather than long-horizon lookahead quality, which is what controllers need; per-position effects at positions > 5 are not in the text.
- Toxicity reduction in Table 3 could come from shorter or blander captions, not better lookahead.
- Table 2 differences could be beam-search noise.

## Missing Stakeholder Perspectives
Users affected by Perspective-API false positives (dialect bias) and subjects of memes; people who could use the method to steer toward harmful content.

## Observations (Non-Defects)
- The complexity argument for conditioning only the prior (§3.1; Table 4) is clear and correct as written.
- The proof of Proposition 1 (App. A) is correct.
- Reporting that tuning the baseline HMM beats prior tricks is a rare and useful honesty.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 44 | Claims exceed evidence (DA-M1, DA-M2) |
| Clarity & Presentation | 56 | Inconsistencies, claims vs tables |
| Novelty & Originality | 48 | Incremental |
| Significance & Impact | 44 | Downstream effect unclear |
| Experimental Validation | 36 | Missing key control, single runs |
| Reproducibility | 34 | No hyperparameters, no code |
| Ethical Compliance | 50 | No limitations or impact section |

Pool position: better than about 38% of submissions to ICLR.

## Overall: 2 | Confidence: 4

---

## Phase 1.5: Literature Check

Requested mode: strict (cutoff 2025-09-24). **Not completed.** `related_search.py search` was run for concept queries (e.g., "neural encoder hidden Markov", "tractable lookahead language model", all `--mode strict`) and returned `arXiv API unreachable (HTTP Error 429 / read timeout)`. No result was kept, so no claim-level novelty profile, baseline scout table, similarity run, or `verify` call could be produced. Per the skill, the review falls back to knowledge with `[verify]` markers (R2's Missing References). Fingerprint was written (`fingerprint.json`). No search was made for the paper, its authors, reviews or outcome. Field snapshot, from knowledge only (not search-based): before the cutoff, tractable control of LMs used distilled HMMs (GeLaTo / Ctrl-G / TRACE), with competing decoding-time approaches via learned prefix scorers and SMC; significant contributions in this sub-field show gains on standard controlled-generation benchmarks against strong controllers at matched cost, or new constraint classes.

## Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1–W6 | kept | Each has location, fix; W6's "774M" parameter figure is an outside fact (GPT2-large), kept as a pointer |
| R1 | Minor typo line | moved to Minor | Cosmetic |
| R2 | W5 (citations) | rewritten | Choi et al. (2019) point turned into a question; CommonGen/GPT-2/Qwen missing citations verified against bibliography |
| R2 | W1 (novelty) | kept | Matches §5 text; not claiming prior work "does" something beyond its description |
| R3 | W4 (connections to other fields) | moved toward Priority 3 | Expansion suggestion |
| R3 | W1 "negligible overhead" | kept | Quotes §3.2.2 and §4.2 |
| R4 | W1 (checklist) | rewritten | Not a weakness itself; folded into the venue-criteria grid |
| DA | DA-M6 | kept | Cross-checked: §3.2.1 and §4.1 say what is stated |
| All | Checks "already answered in appendix" | none dropped | Appendix A–C contain only proofs, DFA definition, complexities |

Scores unchanged.

---

## Phase 2: Synthesizer Part A (package for the EIC)

**Merged issue list.**
| Issue | Sources | Class |
|-------|---------|-------|
| Table 2 gains tiny, single-run, sign-flipping; "significant"/"consistent" wording | R1-W1, R4-W2, DA-M1 | CONSENSUS-3 |
| Table 3 lacks standard-HMM TRACE baseline; weak Sampling baseline | R1-W2, R4-W3 (partial), DA-M2 | CONSENSUS-3 |
| Missing protocol/reproducibility details | R1-W5, R4-W1 grid, DA-m4 | CONSENSUS-3 |
| Overhead claimed, not measured | R1-W4, R3-W1, DA-M5 | CONSENSUS-3 |
| Abstract: "constraint satisfaction" not measured | R4-W2, DA-M1 | CONSENSUS-2 |
| No matched baseline / full conditioning not evaluated | R1-W6, DA-M4 | CONSENSUS-2 |
| Novelty incremental, closest hybrids undifferentiated | R2-W1, R1 (S/W originality) | SOLO |
| Prefix-insensitivity shown by single example | R2-W2 | SOLO |
| VLM likelihood missing | DA-M3, R1-W2 | CONSENSUS-2 |
| Surrogate validity under shifted prefixes | R3-W2 | SOLO |
| Ethics / limitations section missing | R3-W3, R1 limitations, R4 limitations | CONSENSUS-3 |
| DA-CRITICAL | none | n/a |

**Hinge points for the EIC:** Table 2 vs text, Table 3 baselines, constraint-satisfaction wording, unmeasured overhead.

**Official score (script, before EIC weights):** official ratings R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00; official composite 52.1; warnings: none; spread flags: Significance 22 ⚠, Reproducibility 21 ⚠ (the raw spread of Experimental Validation is 20).

---

## Phase 2: EIC Meta-Review (Prof. Rafael Quintero-Ashby)

I read the five reports and the package before re-reading the paper.

### The Case For and Against
- **For acceptance:** A clean, well-motivated idea that fits existing Ctrl-G / TRACE pipelines without breaking their precomputation (§3.1, Table 4), with a multimodal extension that a plain HMM cannot support, and a candid report that Monarch scaling and prior HMM tricks did not help (§4.1). Perplexity improvements at short horizons are plausible (Fig. 4, text).
- **Against acceptance:** The practical claim is that better surrogates give better control with minimal overhead. The evidence is a Table 2 whose differences are in the third decimal and partly negative, a Table 3 missing the baseline that isolates the contribution, no timing, no variance, no training details, and an abstract that claims "constraint satisfaction" gains that are not measured.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Table 2: Transformer-Block below Standard HMM at length 20 on BLEU-4 and CIDEr | R1-W1, DA-M1 | Table 2 | Verified | 0.297 < 0.301; 1.536 < 1.552 |
| "slashing the maximum perplexity by more than half" | R1 ERR-1, DA | §4.2, Table 2 | Verified (partly true) | Holds for 2 of 4 neural rows (60.7%, 57.2%); 32.1% and 7.1% otherwise |
| No standard-HMM row in Table 3 | R1-W2, DA-M2 | Table 3, §4.2 | Verified | Rows: Vanilla, Neural Monarch HMM, Prompting, Sampling |
| Sampling baseline degenerate (k = 1, PPL 43.142, toxicity 0.097) | R1-W2, DA-M2 | Table 3, §4.2 | Verified | Text itself says "capped at k=1" |
| "Minimal inference overhead" unmeasured | R1-W4, R3-W1, DA-M5 | Abstract, Table 1, §4.2, Table 4 | Verified | Only the ~10× MC statement; no LTLA timing |
| "Improves constraint satisfaction" not measured | R4-W2, DA-M1 | Abstract, Table 2, Table 3 | Verified | No satisfaction metric; Table 2 metrics are reference overlap and perplexity |
| No VLM likelihood result | DA-M3 | §4.1, Fig. 3–4 | Verified | §4.1 discusses GPT2-large; VLM only appears in §4.2 |
| Training details absent | R1-W5 | §4, App. A–C | Verified | Searched; none stated |
| "Perplexity +51%" vs "preserving fluency" | R1-W3, DA | Table 3 | Verified | 3.564/2.359 = 1.51; but comparison is against vanilla, and Sampling is worse |
| Prop. 1 bound applies equally to neural HMMs, so it does not explain the encoder's benefit | R2-W2, DA-M6 | §3.2.1, App. A | Verified | Paper says "holds … for neural-encoded HMMs as well" |
| "HMMs … insensitive to the prefix" by one example | R2-W2 | §1, Fig. 1 | Partly correct | Fig. 1 is one illustration; text says "we find empirically" (figure not viewed; further evidence may be in Fig. 3–4) |
| Monarch 16384 vs Dense 1024 compute mismatch | R1 Q3, DA | §4.1, §3.2.1 | Partly correct / unverifiable | Depends on V and constants not stated; kept as a question |
| R3: "negligible overhead" | R3-W1 (R3 rating rationale relies on practicality) | §3.2.2 | Overstated by the paper; R3 flagged it correctly as unmeasured | R3's Overall 4 leans on this plausibility |
| Citation: Choi et al. (2019) supports expressiveness claim | R2-W5 | §2, references | Unverifiable | Not changed |
| Qwen2.5-VL vs Qwen2-VL naming | R1 ERR-4 | §4, §4.2 | Verified | Minor |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Error log verified at every quoted location; one derived compute point labelled uncertain |
| R2 (Domain) | 3 | 4 | 1.0 | Sound, typical; novelty argument somewhat generic; references unverified because the search failed and are labelled [verify] |
| R3 (Perspective) | 4 | 3 | 0.75 | Positive rating leans on overhead and deployment value the paper does not measure; otherwise a fair perspective review |
| R4 (Generalist) | 3 | 4 | 1.0 | Venue-criteria grid and the constraint-satisfaction point verified; rating well calibrated |
| DA | 2 | 4 | 1.25 | Core objection verified (Table 2, Table 3 control); no CRITICAL inflated; Overall 2 slightly harsh but arguments survived the check |

### DA-CRITICAL Rulings
No DA-CRITICAL issues were raised, so there are no rulings and no ceiling. Checked independently: the paper states no selection on a held-out test set (the Ctrl-G "top hypothesis by base-LM log-likelihood" is independent of reported metrics; the CommonGen evaluation split is *not stated*, which is a MAJOR question rather than a leakage finding).

### Final Decision and Justification
Official ratings: R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00 · composite 52.1. EIC-weighted rating (script, weights above) = **2.88**, rounded half up to **3**: the starting point is 3 (Borderline Reject). The weighted composite is 50.9, band 3, so the two signals agree and the cross-check shows no conflict. I decide **3**, equal to the starting point, no DA ceiling.
My own pool position: better than about **46%** of ICLR submissions (accepted share ≈ 27%). Deciding evidence: the method is sound and plausibly useful, but the downstream claims that give it significance are not measured at the stated strength (verified: Table 2, Table 3, abstract wording), which are typical signals of a rejected submission; the gaps are fixable by evidence additions rather than redesign, so this is a reasonable resubmission, not a fundamental rejection. The pool positions of the reviewers range from 38 to 66 (28 points), below the 30-point threshold; the disagreement comes from how much weight to put on a plausible but unmeasured efficiency story, which I resolve against acceptance because the verified evidence points the other way. The decision does not exceed any ceiling (none applies).

---

## Score Summary

### Official Scores and EIC Assessment (script output, `--venue iclr --final 3`)

| Reviewer | Overall | Conf. | EIC weight | Pool pos. | Own composite |
|----------|---------|-------|-----------|-----------|---------------|
| R1 (Meth.) | 3 | 4 | 1.25 | 42 | 49.9 |
| R2 (Domain) | 3 | 4 | 1.00 | 52 | 53.1 |
| R3 (Persp.) | 4 | 3 | 0.75 | 66 | 61.1 |
| R4 (Gen.) | 3 | 4 | 1.00 | 50 | 52.6 |
| DA | 2 | 4 | 1.25 | 38 | 43.8 |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 52 | 56 | 62 | 54 | 44 | 53.6 | 52.4 | 18 |
| Clarity & Presentation | 62 | 62 | 68 | 64 | 56 | 62.4 | 61.6 | 12 |
| Novelty & Originality | 54 | 56 | 62 | 56 | 48 | 55.2 | 54.3 | 14 |
| Significance & Impact | 50 | 54 | 66 | 52 | 44 | 53.2 | 51.6 | 22 ⚠ |
| Experimental Validation | 42 | 46 | 56 | 46 | 36 | 45.2 | 43.8 | 20 |
| Reproducibility | 38 | 42 | 55 | 44 | 34 | 42.6 | 41.0 | 21 ⚠ |
| Ethical Compliance | 55 | 58 | 60 | 56 | 50 | 55.8 | 55.2 | 10 |
| **Composite** | 49.9 | 53.1 | 61.1 | 52.6 | 43.8 | **52.1 (before)** | **50.9 (after)** | |

Official rating (plain mean) 3.00; EIC-weighted rating 2.88; no consistency warnings; R1's composite implies Overall 2 vs reported 3 (within one step).

**Spread discussion.** Significance (22) and Reproducibility (21) diverge because R3 scored practical value and method reproducibility in outline higher (66, 55) than R1 / DA (50 / 44, 38 / 34). I adopt the lower view for Reproducibility (no hyperparameters, data sizes or code, verified) and a middle view for Significance.

### Target-Venue Scores (ICLR, scale status: secondary; verify against the current form)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 2 / 2 |
| Rating | **4 on {0,2,4,6,8,10}** (5 on {1,3,5,6,8,10}); equals the final internal Overall 3 (Borderline Reject) |
| Confidence (1–5) | Reviewers 4, 4, 3, 4, 4 |

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Learning Tractable Distributions of Language Model Continuations" to ICLR.

The paper addresses the practical problem of exact, fast lookahead for controlled generation and proposes to let the base LM supply the prior of an otherwise fixed HMM, preserving the reusable backward computation of Ctrl-G and TRACE.

**Overall Assessment:** The reviewers found the idea clear and well motivated, the complexity argument convincing, and the multimodal extension attractive. They also agreed that the empirical case for the downstream benefit is thinner than the abstract suggests. This is how a careful panel would likely see this draft; it is a simulation, not a prediction.

**Key Strengths Identified by Reviewers:**
1. A clean separation of lookback (neural) and lookahead (tractable) that keeps precomputation valid (R1-S1, R2-S1, R3-S1).
2. Works with different constraint families and with a VLM that a plain HMM cannot condition on (R1-S4, R3-S3).
3. Honest reporting that Monarch scaling and prior HMM tricks did not help (R1-S3, R4-S3).

**Key Concerns Requiring Attention:**
1. Table 2 gains are tiny, single-run and partly negative, but described as "significant" (CONSENSUS-3: R1, R4, DA).
2. Table 3 lacks a standard-HMM baseline and uses a degenerate sampling baseline; no VLM likelihood is reported (CONSENSUS-3).
3. Efficiency, constraint satisfaction and "minimal overhead" are claimed but not measured; training details and code are missing (CONSENSUS-3).

**Decision: Borderline Reject (3)** (ICLR rating 4 on the {0,2,4,6,8,10} scale).

The issues are fixable with evidence rather than a redesign. A resubmission that adds seeds and confidence intervals, a standard-HMM TRACE row, a text-LM detoxification experiment comparable to prior TRACE numbers, a satisfaction metric, a timing table and full training details, and that aligns the abstract with the measurements, would be viewed considerably more favorably. Please see the Revision Roadmap.

Sincerely,
Prof. Rafael Quintero-Ashby (fictional persona)
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Table 2 gains within noise / overstated wording | R1, R4, DA | CONSENSUS-3 |
| Table 3 missing HMM baseline, weak sampling baseline | R1, R4, DA | CONSENSUS-3 |
| Reproducibility details missing | R1, R4, DA | CONSENSUS-3 |
| Overhead not measured | R1, R3, DA | CONSENSUS-3 |
| No limitations / impact discussion | R1, R3, R4 | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the contribution worth presenting at ICLR as is? | R3 (4) | R1, R2, R4, DA (3, 3, 3, 2) | Sound idea but R3's case rests on unmeasured practicality; verified evidence supports the lower ratings |
| Does the method deliver "minimal overhead"? | R3 (plausible) | R1, DA (unmeasured) | Unmeasured; counts neither for nor against until timed |

### Score Spread Discussion
Significance ⚠ (22) and Reproducibility ⚠ (21): R3 is the high outlier on both; see above.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Constraint satisfaction unmeasured; "significant" gains tiny | Yes (R1, R4) | n/a | n/a |
| DA-M2 | MAJOR | No HMM baseline in Table 3; degenerate sampling baseline | Yes (R1) | n/a | n/a |
| DA-M3 | MAJOR | VLM distillation likelihood missing | Partly (R1) | n/a | n/a |
| DA-M4 | MAJOR | Compute/parameter-matching, full conditioning not tested | Yes (R1) | n/a | n/a |
| DA-M5 | MAJOR | Overhead unmeasured | Yes (R1, R3) | n/a | n/a |
| DA-M6 | MAJOR | Prop. 1 does not motivate the neural encoder | Yes (R2) | n/a | n/a |
| (no CRITICAL) | | | | | |

---

## Revision Roadmap

### Priority 1: Required (must fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Verified: headline downstream claims not supported as worded (tiny, single-run, sign-flipping Table 2 differences; unmeasured "constraint satisfaction") | R1-W1, R4-W2, DA-M1 | Abstract, §4.2, Table 2 | Seeds, CIs, per-instance bootstrap; add satisfaction/success metric; reword claims | Medium; ≈ 20–40 GPU-h | Yes |
| R2 | Verified: Table 3 does not isolate the contribution | R1-W2, DA-M2 | Table 3, §4.2 | Add standard-HMM TRACE row, stronger sampling baseline at matched time, text-LM detox (RealToxicityPrompts) | Medium; ≈ 30–60 GPU-h | Partly |
| R3 | Verified: efficiency claims unmeasured | R1-W4, R3-W1, DA-M5 | Abstract, Table 1, §4.2 | Timing and memory table for all encoder variants | Low; < 10 GPU-h | Yes |
| R4 | Verified: protocol and training details missing | R1-W5 | §4, appendix | Dataset size, hyperparameters, seeds, compute, split, code | Low | Yes |

### Priority 2: Strongly suggested (should fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | VLM distillation likelihood and encoder/setup details | DA-M3, R4-W3 | Report VLM perplexity for HMM vs LTLA; state encoder variant, hidden size, #captions; caption-quality metrics | Medium | Partly |
| S2 | Compute/parameter-matched baseline; evaluate full-conditioning variant | R1-W6, DA-M4 | Matched-FLOPs baseline; small-H full conditioning | Medium | Partly |
| S3 | Novelty delta against hybrid neural/tractable models; quantitative context-sensitivity metric | R2-W1, R2-W2 | Add comparison and metric; reframe Prop. 1 (DA-M6) | Medium | Partly |
| S4 | Missing citations and positioning against learned decoding-time controllers | R2-W3, R2-W5 | Cite CommonGen etc.; discuss Controlled Decoding, DExperts, RAD [verify] | Low | Yes |
| S5 | Limitations / broader impact; Perspective-API bias; human check | R3-W3, R4 | Add section, small human study | Low | Yes |
| S6 | Numbers of Fig. 3/4 as a table; Lee & Berg-Kirkpatrick numbers | R4-W4, DA-m4 | Add tables | Low | Yes |

### Priority 3: Nice to fix (optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Proposition numbering; Qwen model naming; duplicated GeDi reference; typos | R1, DA | Fix |
| N2 | Surrogate validity under shifted (controlled) prefixes | R3-W2 | On-policy evaluation |
| N3 | Connections to hybrid DNN-HMM / WFST composition; HSMM extensions | R3-W4 | Discuss |
| N4 | Max-perplexity statistic identical for Standard HMM at both lengths | DA-m3 | Explain or replace with median / 95th percentile |
| N5 | Monarch vs dense compute comparability statement | R1 Q3 | Give the constants and V |

## Estimated Revision Effort
- Priority 1: 4 items, about 1–2 weeks (experiments ≈ 60–110 GPU-hours plus writing).
- Priority 2: 6 items, about 1 week.
- Priority 3: 5 items, about 1–2 days.
- **Total estimated revision time**: 2–3 weeks.
