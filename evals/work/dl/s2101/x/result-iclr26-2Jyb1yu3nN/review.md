# Simulated Peer Review: "Circuit Insights: Towards Interpretability Beyond Activations"

*Date: 2026-11-10 · Skill: academic-paper-reviewer v2.10.1 · Mode: full · Target venue: ICLR (profile `iclr`, 2026 cycle) · Literature check: strict, cutoff 2025-09-24.*
*This is a simulation of how a careful panel would likely see this draft, not a prediction of any outcome. The five reviewer passes were run one after another in a single model context (no subagents); they share that context and are not independent agents. Figures were not available: figure-dependent claims are judged from captions and text only.*

---

## Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Circuit Insights: Towards Interpretability Beyond Activations |
| Primary Discipline | Machine learning → mechanistic interpretability / automated interpretability of LLM features |
| Secondary Discipline(s) | Explainable AI; NLP (lexical/vocabulary-space analysis); LLM-as-judge evaluation |
| Paper Type | Empirical (method + benchmark-style evaluation; composite weights: empirical) |
| Core Technique(s) | Transcoders (Gemma Scope, GPT-2, Llama-3.2-1B), weight-space projection to vocabulary, z-score outlier selection, attribution to attention heads / features, Jaccard + DBSCAN clustering, explainer-LLM descriptions, FADE metrics |
| Target Venue | ICLR (top-tier ML conference) (stated by user); profile key `iclr` |
| Venue-Specific Notes | none (ICLR form: Soundness / Presentation / Contribution, rating; public reviews, revised PDF allowed during discussion) |
| Paper Maturity | Submission-ready (complete paper, no limitations section, quantitative evaluation on one model) |
| Ethics-Relevant Content | none (interpretability tooling for LLMs; no human data; indirect safety relevance) |

### Claimed Contributions (as stated by the authors)
1. **C1 (method/result):** WeightLens, a framework for interpreting transcoder features "using only their weights and the weights of their transcoders", whose descriptions "match or exceed activation-based descriptions for context-independent features" (Section 1 bullet 1, Abstract, Section 4, Table 1).
2. **C2 (method):** CircuitLens, circuit-based analysis of feature activations for context-dependent features: (i) isolating input patterns that trigger activations via attention-head attribution and (ii) identifying which outputs a feature influences (Section 1 bullet 2, Section 3.2, Section 5, Table 2).
3. **C3 (method/result):** Circuit-based clustering handles polysemanticity (Section 1 closing paragraph, Section 3.2); the abstract adds that "these methods increase interpretability robustness", and Section 5 ("Resolving the Clarity Problem") and the Conclusion claim reduced dataset size and explainer-LLM dependence.

### Paper memory (factual record shared with all reviewers)
- **Setup:** Transcoders for GPT-2 Small, Gemma-2-2b (Gemma Scope; footnote 3 links a 16k-width transcoder), Llama-3.2-1B (Section 4). Quantitative evaluation only on Gemma-2-2b layers 0, 7, 12, 21 (Tables 1–2); "∼250 features per layer" for Table 1 (Section 4); the number and selection of features for Table 2 is not stated after search. Pile (uncopyrighted) used: 6 GB (3.6B tokens) for MaxAct*, 40 MB (24M tokens) for circuit-based descriptions, descriptions from the training partition and evaluation from the test partition (Appendix B). Explainer LLM GPT-4o-mini (Section 3.2, Appendix C.2); a "secondary LLM" gpt-4o-mini-2024-07-18 for WeightLens+Out+LLM (Section 4). Metrics: FADE Clarity, Responsiveness, Purity, Faithfulness (Section 3.3). Sampling: B = 20 quantile bins, α = 0.9, N = 100 (Section 3.2).
- **Not stated after search:** the FADE judge / synthetic-data LLM; the z-score threshold; ρ (frequency filter); DBSCAN eps / min-samples; seeds, repeated runs or confidence intervals; compute or wall-clock cost; the explainer model and prompt used for the MaxAct* and Neuronpedia baselines; how the ~250 features were chosen; human evaluation; a limitations section.
- **Headline numbers:** 32.7% / 58.8% / 25.4% of features with validated input-invariant descriptions for Gemma / GPT-2 / Llama (Section 4, Figure 3); 1.05 / 4.5 / 2.8 / 2.95 average clusters per feature for layers 0 / 7 / 12 / 21 (Section 5); +1.4% of samples from extending output analysis at layer 0 (Section 5, Figure 7).
- **Appendix adds:** extended related work (A), dataset processing (B), the two LLM prompts (C), KDE plots of metric distributions (D, Figures 9–10; not viewable).
- **Unverifiable:** all figures (1–10), bolding in Tables 1–2, exact typesetting of Eq. (1)–(5) (extraction garbled the layout; symbols were read from the surrounding text).
- **Integrity scan:** `integrity_scan.py` found no reviewer-directed text or hidden characters. No injection found while reading. The reviewers read `reviewer_copy.txt` (identical to the paper text).

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Adaeze Brandvold, senior area chair profile (research university, Northern Europe)
- **Seniority / Expertise**: Senior faculty / sparse dictionary learning, representation analysis in language models
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Calibrates to what ICLR accepts; discounts points the paper already answers.

### Reviewer 1 (Methodology): Ruoxi Almeida, mid-career (industrial research lab, South America)
- **Seniority / Expertise**: Mid-career / evaluation of automated interpretability, LLM-as-judge validity, clustering
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on matched explainer prompts and repeated runs.

### Reviewer 2 (Domain): Priyanka Vandenberg, senior (public research university, Western Europe)
- **Seniority / Expertise**: Senior faculty / SAE and transcoder circuits; vocabulary-space analysis of MLP weights
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Checks every "new" claim against earlier weight-space work.

### Reviewer 3 (Perspective): Mateo Szymanski, mid-career (cognitive science / psycholinguistics department, Central Europe)
- **Seniority / Expertise**: Mid-career / lexical semantics, usage-based construction grammar, feature-description evaluation by humans
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; sees potential and points to it.

### Reviewer 4 (Generalist): Ngozi Halloran, mid-career (industry lab, West Africa / Europe)
- **Seniority / Expertise**: Mid-career / deep learning for NLP, model analysis in general
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee reader; weighs weaknesses against what accepted papers carry.

### Devil's Advocate: Dmitri Okonkwo-Reyes, senior (statistics and evaluation methodology group, research university, East Asia)
- **Seniority / Expertise**: Senior / evaluation methodology, causal inference, construct validity of automated metrics
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; asks what else could explain the numbers.

*Personas are fictional. Assumptions: paper type empirical; venue ICLR as stated by the user.*

---

## Phase 1: Independent Multi-Perspective Review

# Peer Review Report

## Paper: Circuit Insights: Towards Interpretability Beyond Activations
## Reviewer: Ruoxi Almeida, Reviewer 1 / Methodology (industrial research lab, South America; fictional persona)
## Expertise: evaluation of automated interpretability; LLM-as-judge validity; clustering
## Date: 2026-11-10

---

## Summary
The paper builds two description pipelines for Gemma-2-2b transcoder features. WeightLens builds a token list for a feature from encoder-to-embedding projections, features inherited from earlier layers, a forward-pass check, and decoder-to-unembedding projections, with lemmatization (Section 3.1). CircuitLens attributes a feature's activation to attention-head/token pairs and to the output logits (Eq. 4–5), masks the inputs to those tokens, clusters inputs by Jaccard similarity and DBSCAN, and has GPT-4o-mini describe each cluster and then merge them (Section 3.2). Both are scored with the FADE metrics against Neuronpedia and a MaxAct* baseline on four layers (Tables 1–2).

---

## Strengths

### S1: A useful, cheap partial route to descriptions
Section 4 shows that for token-driven features a description can be built from weights plus a single check, with no explainer LLM in the basic variant (WeightLens, Table 1). Section 4 reports the share of features covered per model (32.7% / 58.8% / 25.4%, Figure 3), an honest coverage statistic that most auto-interp papers omit.

### S2: A comparison that separates dataset effects from method effects
Section 5 adds "(top)" variants of CircuitLens run on the same large top-activation data as MaxAct* (Table 2, Appendix B). This is the right control for the claim that the circuit view, not the data, drives the result.

### S3: Candid reporting of weaknesses of the setup
The paper states that Faithfulness is "consistently low across layers and methods" (Section 4), that purity favours activation-based baselines, and that "circuit-based methods still depend on the dataset" (Section 5). The honest layer-wise breakdown by ℓ0 and the cluster counts (Figure 8) make the analysis useful beyond the headline numbers.

### S4: Reasonable data hygiene
Descriptions come from the Pile training partition and are evaluated on the test partition (Appendix B). I found no statement of tuning or selection on the evaluation split (protocol sweep: no "tuned", "selected" or "validation" statements about the reported split).

---

## Weaknesses

### W1: Which features are evaluated is undefined, and the baselines' numbers change between tables
Section 4 evaluates "∼250 features per layer" and the abstract limits the claim to "context-independent features", but Section 4 never says whether these are the validated token-based features (32.7% of Gemma features) or a random sample, nor how Table 2's features were chosen. The same baselines have different scores in the two tables: MaxAct* Clarity at layer 12 is 0.33 in Table 1 but 0.17 in Table 2; at layer 21 it is 0.53 vs 0.39; Neuronpedia layer 12 Clarity is 0.28 vs 0.15 (Error Log ERR-1). The likely explanation is different feature populations, but that is not stated. If WeightLens is evaluated only on features it succeeded on, Table 1 measures "when the method applies, it is as good", not "matches or exceeds" activation methods.
- **Suggested Fix**: State the selection rule and N per layer for each table; report Table 1 on (a) validated features, (b) all features with abstention counted as zero/"no description", and (c) a matched random sample for all methods. Cost: description generation for ~250 features × 4 layers, minutes to a few GPU-hours.

### W2: No variance or confidence intervals; many differences are 0.01–0.03
There are no seeds, repeated runs, bootstrap intervals or paired tests in Tables 1–2. WeightLens vs MaxAct* Responsiveness at layer 0 is 0.24 vs 0.21; CircuitLens-Input (top) vs MaxAct* Responsiveness is +0.03, +0.02, −0.01, +0.01 across layers (Table 2). The FADE metrics rely on LLM generation and judging, which are stochastic. With ~250 features per layer a paired bootstrap over features is cheap. Without it the "on par or better" and "competitive" statements (Sections 4–5) cannot be separated from noise.
- **Suggested Fix**: Paired bootstrap over features for each metric and layer, plus 3 re-runs of the generation/judging stage. About 3× the evaluation cost, a few GPU/API-hours.

### W3: The circuit contribution is confounded with prompt, sampling and explainer choices; there is no ablation
CircuitLens differs from MaxAct* in at least five ways: quantile sampling (Section 3.2), pattern masking, clustering, a new explainer prompt that instructs "Avoid vague phrases like" and to output exact tokens (Appendix C.2), and a merge step. Clarity, the metric that improves most, rewards specific descriptions. Table 2 has no row with the new prompt on unmasked top-activation text, no row with masking but no clustering, and no row with clustering but plain-activation inputs (embedding clusters as in Kopf et al., cited in Appendix A.1). The explainer model and prompt for the MaxAct* baseline are not stated. Therefore the claim that circuits reveal what "activation-only approaches cannot identify" is not isolated by the experiments.
- **Suggested Fix**: Add three ablation rows at the same data and explainer: (i) new prompt on raw top activations; (ii) masking without clustering; (iii) activation-embedding clustering instead of circuit clustering. Cost: 3 × the existing CircuitLens description run.

### W4: Table 2 does not support "improves quality" on three of four metrics
CircuitLens (top) vs MaxAct* (Table 2): Clarity improves by +0.16, +0.14, +0.10, +0.15 (mean +0.14), but Purity is lower at all four layers (−0.04, −0.01, −0.02, −0.01), Responsiveness is within ±0.03, and Faithfulness is 0.00–0.04 for every method. For the small-data variant (CircuitLens-Full), layer 21 drops to Responsiveness 0.64 vs 0.71 and Purity 0.54 vs 0.64 while Clarity rises 0.39 → 0.52. At layer 7, CircuitLens-Input has Clarity 0.39 against 0.44 (Neuronpedia) and 0.48 (MaxAct*). This is a trade-off, not a uniform gain.
- **Suggested Fix**: Report the trade-off explicitly, add a combined or Pareto view, and narrow the wording in the abstract and conclusion to Clarity.

### W5: Efficiency and scalability are claimed but never measured
The abstract says the methods enhance scalable analysis "while maintaining efficiency and quality", yet there is no wall-clock, token or API cost for any method. Section 5 says output-based analysis needs a forward and backward pass per generated token, and Section 5 concedes the full-distribution sampling is "memory-intensive". CircuitLens also calls an LLM once per cluster plus once to merge, i.e., more LLM calls than a one-description baseline, and Layer 7 has 4.5 clusters per feature on average (Section 5).
- **Suggested Fix**: A cost table (feature-hours, LLM calls and tokens, GPU memory) per method and layer.

### W6: Key procedure parameters are missing, so the method cannot be re-implemented from the paper
After a text search, I found no z-score threshold (Section 3.1 steps 1 and 3; Section 3.2 input-centric bullet), no ρ (Section 3.2), no DBSCAN eps/min-samples, and no FADE judge/synthetic-data model. Section 5 says that "more careful hyperparameter tuning could yield more generalizable results", which implies parameters were not tuned systematically, and no sensitivity analysis is given. Step 2 ("Retain only tokens that activate the feature in a forward pass") does not say in what context a token is tested; a single context cannot test the claim in Assumption 2 that the feature activates "regardless of context", and the forward pass may reintroduce dataset dependence.
- **Suggested Fix**: A parameter table in the appendix, a sensitivity sweep for z-threshold, ρ, eps, and a description of the validation contexts. Footnote links may contain code (not viewable here); the text should still stand alone.

### Error Log

| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E6 | Table 1 vs Table 2 (MaxAct*, Neuronpedia, Gemma-2-2b, same layers) | Table 1: "MaxAct* 0.50 0.21 0.08 0.04 0.54 0.15 0.08 0.05 0.33"; Table 2: "MaxAct* 0.50 0.21 0.09 0.04 0.48 0.15 0.09 0.03 0.17" | The same baseline on the same model and layer has different scores (layer 12 Clarity 0.33 vs 0.17; layer 21 Clarity 0.53 vs 0.39); the paper does not explain the different populations | Cross-referenced two tables | High that values differ; Medium on cause | MAJOR | State and justify the feature set of each table |
| ERR-2 | E5 | Abstract vs Table 1 (Purity, Faithfulness) | "need for explainer models or datasets while matching or exceeding the" | MaxAct* has higher Purity at all four layers (e.g., 0.08 vs 0.03 at layer 0; 0.74 vs 0.65 at layer 21) and equal or higher Faithfulness at three of four layers; mean Purity over layers: 0.18 (WeightLens) vs 0.24 (MaxAct*, reading 0.7 as 0.07) | Recomputed means from Table 1 | High | MAJOR | Say "higher Clarity and Responsiveness, lower Purity" in the abstract |
| ERR-3 | E5/E6 | Section 4 vs Table 1 | "perform poorly in terms of descriptions quality" | Layers 0 and 7 have higher Clarity (0.56, 0.62) than layer 12 (0.47), which the same section calls "the least interpretable"; poor only relative to layer 21 | Cross-referenced text and table | Medium (depends on the metric meant) | MINOR | Name the metric and baseline |
| ERR-4 | E1 | Table 1, MaxAct* layer 12 Purity | "0.33 0.11 0.7 0.00 0.53" | The cell "0.7" is inconsistent with the 0.02–0.10 range of its neighbours; likely 0.07 | Cross-referenced row | Medium | MINOR | Correct the cell |
| ERR-5 | E5 | Section 4 "LLM postprocessing is not essential" vs Table 1 | "LLM postprocessing is not essential" | Adding the output tokens lowers Clarity at all four layers relative to plain WeightLens (0.56→0.51, 0.62→0.55, 0.47→0.39, 0.71→0.63); the LLM step recovers 0.01–0.05 but stays below plain WeightLens. The text does not discuss that the output component hurts Clarity and never raises Faithfulness | Recomputed differences | High | MAJOR | Discuss; justify the output component or drop it |

---

## Missing References
Not my role (see Reviewer 2).

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Sound basic idea but undefined evaluation populations, no variance, confounded comparison |
| Clarity | 3 | Understandable; key parameters and tables' populations missing |
| Significance | 2 | Useful for a subset of features; gains modest and one model |
| Originality | 2 | Combination of known weight projections and attribution; clustering step new in form |

## Dimension Scores (0–100)

**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline comparison rests on single runs over an undefined feature set with differences often ≤ 0.03 (Tables 1–2), and the circuit contribution is not isolated from prompt and sampling changes (Section 3.2, Appendix C.2).

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Reasonable pipeline; thresholds, validation contexts and Eq. 4's treatment of intermediate layers unspecified |
| Clarity & Presentation | 62 | Competent | Readable; table caption/typos and undefined populations |
| Novelty & Originality | 56 | Competent | Weight-space token lists and attribution are known ingredients; the circuit clustering is a new combination |
| Significance & Impact | 52 | Developing | Helps a minority of features; quantitative evidence on one 2B model |
| Experimental Validation | 46 | Developing | Four layers, one model, no variance, no ablation, no human check of the judge |
| Reproducibility | 50 | Developing | Prompts given (Appendix C); main parameters absent; links not viewable |
| Ethical Compliance | 66 | Competent | Nothing at stake; limitations only partly discussed |

---

## Questions for Authors
1. Which features are in Tables 1 and 2 (selection rule, N), and why do baseline numbers differ between the tables? A matched-population table would raise my Experimental Validation score.
2. What are the z-score thresholds, ρ, and DBSCAN settings, and how sensitive are the results to them? Strong sensitivity would lower my score.
3. How does CircuitLens perform if the same explainer prompt is applied to raw top-activation text (no masking, no clustering)?
4. In what context is a token "validated" in Step 2, and does a single positive forward pass establish "regardless of context"?
5. Does Eq. (4) include the Jacobian term for heads at layers l′ < l, as Eq. (2) does for features?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially. Dataset dependence, low Faithfulness and the coverage of token-based features are discussed inline, but there is no limitations section and nothing on single-model evaluation, LLM-judge validity, or compute cost.

## Ethics Review Flag
**No**: no human data or misuse potential.

## Overall Score
**3**: A sensible idea with honest partial results, but the experiments do not yet isolate the claimed contribution or establish the size of the effects; the typical rejected submission shares these gaps.

## Confidence
**4**: Confident on the evaluation design; I could not view the figures or the supplement-linked code.

---

# Peer Review Report

## Paper: Circuit Insights: Towards Interpretability Beyond Activations
## Reviewer: Priyanka Vandenberg, Reviewer 2 / Domain (public research university, Western Europe; fictional persona)
## Expertise: SAE and transcoder circuits; vocabulary-space analysis of MLP weights
## Date: 2026-11-10

---

## Summary
The paper proposes to move transcoder-feature interpretation partly out of activation space. WeightLens reads token descriptions off the weights, and CircuitLens uses attribution to attention heads and output logits to isolate activation-relevant tokens and cluster inputs by shared contributors. The authors evaluate on Gemma Scope transcoders with the FADE metrics. The motivating gap is the dependence of automated interpretability on explainer LLMs and large datasets (Section 1).

---

## Strengths

### S1: Well-chosen foundation
Building on transcoders, which factor a feature-to-feature contribution into an input-dependent activation and an input-invariant weight term (Eq. 1), is a principled place to attempt weight-based description. The paper cites and describes Dunefsky et al., Ameisen et al. (TWERA) and Paulo et al. accurately for what Section 2 attributes to them.

### S2: A clear, testable problem statement
Section 1 argues that SAE/transcoder features are often too specific for top-activation prompts (citing FADE), and Section 5 shows two concrete cases (L12F619 and L21F91, Figures 5–6) where attribution reveals a pattern the activations hide. Even without figures the captions describe the claim clearly.

### S3: Layer-wise analysis of where token-level weight analysis works
The ℓ0-linked discussion of Gemma-2-2b layers (Section 4) and the cluster counts per layer (Section 5, Figure 8) provide an empirical map that practitioners can use, including the finding that the proportion of token-based features differs strongly between GPT-2, Gemma and Llama (Figure 3).

---

## Weaknesses

### W1: The weight-space half of the contribution is not positioned against earlier vocabulary-space and weight-based neuron analysis
Projecting encoder/decoder directions through the embedding and unembedding matrices and reading off outlier tokens (Section 3.1, steps 1 and 3) is the established "FFN weights in vocabulary space" approach to MLP neurons and SAE/transcoder features. Section 2 and Appendix A discuss only auto-interp pipelines and transcoder circuits and never mention earlier weight-based analyses of MLP neurons or logit-lens-style projections (see Missing References). The novelty over this line is the transcoder-specific recursion over earlier-layer features (step 1) and the z-score selection; that delta is not stated. Consequently "reducing dependence on both the underlying dataset and explainer LLMs" (Section 1) is presented as new without a baseline from this line (for example, plain output-vocabulary projections as in Gur-Arieh et al., which the paper cites but does not run).
- **Suggested Fix**: Add the weight-space line to Section 2 and compare against a plain unembedding-projection baseline (top-k tokens, no z-score, no inheritance) to show what the inheritance step buys.

### W2: The polysemanticity claim has no comparison to the closest clustering work
Kopf et al. (2025) (PRISM) cluster activating inputs for multi-concept descriptions; it appears only in Appendix A.1 and not in Section 2. The "circuit-based clustering" contribution (Section 3.2; Section 1: it "handles polysemanticity") is never compared with embedding-based clustering, either conceptually in the main text or empirically in Table 2. Section 3.2 states that "Semantic clustering of activations in embedding space is insufficient", which is an empirical claim with no test.
- **Suggested Fix**: Move the discussion to Section 2 and add embedding-clustering (k-means over text embeddings, as in Kopf et al.) as a baseline inside the CircuitLens pipeline.

### W3: Baselines are a narrow slice of the auto-interp literature
Table 1–2 compare only Neuronpedia and MaxAct*. The paper cites output-centric descriptions (Gur-Arieh et al.), fine-tuned explainers (Choi et al.), and intervention-based scoring (Paulo et al.) but runs none of them, and it cannot claim superiority over "existing methods" (Abstract) in general. The output side of CircuitLens, "identifying which model outputs are influenced" (Section 1 bullet 2), is closest to Gur-Arieh et al., and no difference or comparison is given.
- **Suggested Fix**: Run at least the output-centric baseline of Gur-Arieh et al. on the same features, or narrow the claims to the two baselines tested.

### W4: Theoretical statements are heuristics presented as assumptions
Assumptions 1 and 2 (Section 3.1) are design heuristics (outliers are meaningful; strongly supported tokens should activate the feature regardless of context). The second is contradicted by the paper's own finding that most features are context-dependent (Figure 3), and the "validation step" only checks tokens in some forward pass. The discussion of Ameisen et al. in Section 2 says raw transcoder weights "diverge substantially" from attribution-based weights; yet WeightLens uses raw W_dec·f_enc between layers (Section 3.1 step 1) without addressing the interference problem the paper itself describes in Section 2 and A.3.
- **Suggested Fix**: Reframe as heuristics; quantify, for validated features, how often the inherited tokens survive the forward-pass check, which is a direct measure of the interference.

### Minor
Section 4 explains the lower quality in middle layers of Llama and Gemma with RoPE ("A likely explanation is the use of RoPE in Llama and Gemma"), but Gemma-2 and Llama also differ from GPT-2 in transcoder training method, width and norms; label the explanation as a hypothesis and do not state it as a finding. "WeigthLens"/"WeightLens+Output+LLM" naming is inconsistent (Table 1 vs Section 4).

---

## Missing References
*(Pre-literature-check draft; the Literature-check addendum below supersedes these entries.)*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Important | Geva, Schuster, Berant, Levy. "Transformer Feed-Forward Layers Are Key-Value Memories", EMNLP 2021 | Early analysis of FFN weights as key-value memories, with vocabulary-space reading of value vectors. |
| Important | Geva, Caciularu, Wang, Goldberg. "Transformer Feed-Forward Layers Build Predictions by Promoting Concepts in the Vocabulary Space", EMNLP 2022 | Projects FFN value vectors to the vocabulary and describes them by promoted tokens, the output half of WeightLens. |
| Important | Marks, Rager, Michaud, Belinkov, Bau, Mueller. "Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models", ICLR 2025 `[verify]` | Feature-level circuit discovery with sparse dictionaries; relevant to the circuit claim. |

### Literature-check addendum (Phase 1.5, strict mode, cutoff 2025-09-24)

**Status of the check.** The fingerprint was written (`fingerprint.json`; paper title, method names and distinctive phrases, used only for exclusion; `benchmarks` found no external benchmark, because Tables 1–2 use only FADE metrics and Neuronpedia/MaxAct* baselines). One claim query was issued (`--purpose claim --tag C1`, strict mode, 4 concept words) but the arXiv API stayed unreachable: the script retried for about ten minutes and then exited reporting that the arXiv API was unreachable (HTTP error 429) and to fall back to [verify] (only the query entry is in `search_ledger.jsonl`). Following `references/literature_search.md` ("API is unreachable: say so and fall back to `literature check: off`"), no further queries were run (1 of 12 budgeted queries used), so there are **no kept results**, no `similarity` run, no `novelty` profile and no baseline scout table. Consequently:
- the verdicts below are built from the paper's own related work and from my knowledge, and every entry is marked `[verify]`;
- nothing here is a required comparison; no claim is judged "known" or "novel" from search results;
- gaps left open: all three claim queries (C1, C2, C3), the baseline query, and the coverage/expansion round.

**Novelty delta table (from the paper's own text and knowledge; `[verify]`)**

| Claimed contribution | Closest prior work (as cited by the paper) | What that work already does | What is actually new here | Cited and differentiated? |
|----------------------|--------------------------------------------|-----------------------------|---------------------------|---------------------------|
| C1 WeightLens (weight-derived token descriptions for transcoder features) | Dunefsky et al. 2024 (transcoders; case studies, manual); Ameisen et al. 2025 (weight interpretability, TWERA); Paulo et al. 2025b | Shows input-invariant weight terms can be read for single features, mostly by manual analysis (Section 2, Appendix A.3) | Automated description from encoder/decoder projections with z-score outliers, inherited tokens from earlier layers, forward-pass validation and lemmatization (Section 3.1) | Yes for transcoders; the older MLP-weight vocabulary-projection line is not cited `[verify]` |
| C2 CircuitLens input/output attribution | Dunefsky et al. 2024; Ameisen et al. 2025 (Jacobian-corrected attributions); Gur-Arieh et al. 2025 (output-centric descriptions) | Attribution of feature activations to earlier features and heads; output-side descriptions | Using attribution to mask the input to contributing tokens for automated descriptions (Section 3.2) | Yes; no empirical comparison with Gur-Arieh et al. |
| C3 Circuit-based clustering | Kopf et al. 2025 (PRISM; embedding clustering of activating inputs) | Multi-concept descriptions through clustering of top activations | Clustering by shared circuit contributors with Jaccard + DBSCAN | Cited only in Appendix A.1; not in Section 2; no comparison |

Per-claim novelty (knowledge-based, not search-based): C1 medium (new combination for transcoders; ingredients known), C2 medium, C3 medium to incremental `[verify]`. These are at most MAJOR findings (cite, differentiate, compare) and none makes the paper "known".

**Field snapshot (knowledge-based, as of the cutoff; no kept results).** Automated interpretability started from LLM-written neuron descriptions scored by simulation (2023). It moved to SAE features (2023–2024), where work showed that many features are too specific for top-activation prompts (FADE, ACL Findings 2025) and that explainer choice matters. In parallel, transcoders and attribution graphs (2024–2025) made feature-to-feature circuits computable. Open problems named in the paper's own related work are dependence on explainer LLMs, polysemantic features, unreliable output-side validation (low Faithfulness), and the absence of human-grounded metrics. What counts as significant now: a method that gives descriptions that are more *correct* (validated by interventions or humans) or far cheaper at equal quality across several models; a Clarity-only gain under one LLM-judged metric on one 2B model is incremental. I used this to score Significance at 52–66 and Novelty at 54–66.

**Verified missing references.** None could be verified with `related_search.py verify` (no response). Entries are kept only where I am confident the work exists as described, and all are marked `[verify]`:

| Priority | Reference (authors, title, venue/year as I know them) | Why it matters |
|----------|-------------------------------------------------------|----------------|
| Important | Geva, Schuster, Berant, Levy. "Transformer Feed-Forward Layers Are Key-Value Memories", EMNLP 2021 `[verify]` | Early analysis of FFN weights as key–value memories with vocabulary-space reading of value vectors. |
| Important | Geva, Caciularu, Wang, Goldberg. "Transformer Feed-Forward Layers Build Predictions by Promoting Concepts in the Vocabulary Space", EMNLP 2022 `[verify]` | Describes FFN value vectors by tokens they promote through unembedding, the output half of WeightLens. |
| Important | Marks, Rager, Michaud, Belinkov, Bau, Mueller. "Sparse Feature Circuits: Discovering and Editing Interpretable Causal Graphs in Language Models", ICLR 2025 `[verify]` | Feature-level circuit discovery with sparse dictionaries; relevant to the circuit and automated-circuit claims. |
| Helpful | Work on human-grounded evaluation of neuron/feature descriptions in auto-interp (described as a line of work, no specific paper) | Anchors LLM-judge metrics. |

The citation check (E7) for the paper's own load-bearing citations: Dunefsky et al. (transcoders; case studies based mainly on manual analysis), Ameisen et al. (TWERA; Jacobian-corrected attributions) and Puri et al. (FADE metrics) are described in Section 2 and Appendix A in a way consistent with how I know them. No mismatch found; abstracts were not retrievable, so this is `[verify]`.

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Reasonable approach; untested comparisons to the closest weight-space and clustering work |
| Clarity | 3 | Clear motivation and structure |
| Significance | 2 | Narrow: a minority of features, one 2B model |
| Originality | 3 | A new combination, new circuit clustering; weight projection itself is not new |

## Dimension Scores (0–100)

**Pool position:** better than about 52% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the idea (weight-derived token descriptions plus circuit-based clustering on transcoders) is appealing and above the median in ambition, but the weight-projection and clustering ingredients are not positioned against earlier work and the gains over baselines are modest (Tables 1–2).

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 58 | Competent | Principled grounding in Eq. 1–5; heuristics labelled as assumptions |
| Clarity & Presentation | 64 | Competent | Clear framing; related work incomplete |
| Novelty & Originality | 60 | Competent | New combination for transcoders; ingredients established |
| Significance & Impact | 56 | Competent | Useful for the transcoder circuit toolbox if validated more widely |
| Experimental Validation | 50 | Developing | Two baselines, one model for quantitative results |
| Reproducibility | 54 | Developing | Prompts available; parameters missing |
| Ethical Compliance | 66 | Competent | Not at stake |

---

## Questions for Authors
1. What exactly does the inheritance step (earlier-layer features, Section 3.1 step 1) add over a direct W_E·f_enc projection? A measured delta would raise my Novelty score.
2. How does circuit-based clustering compare with embedding-based clustering of the same samples (as in Kopf et al.)? If similar, Novelty would drop.
3. How are results for GPT-2 and Llama-3.2-1B (Figure 3) related to the quantitative metrics, which are reported only for Gemma?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially (see Reviewer 1).

## Ethics Review Flag
**No**

## Overall Score
**3**: The direction is promising, but novelty against the weight-space and clustering literature is undemonstrated and the empirical gains are modest and mixed across metrics.

## Confidence
**4**: Know the transcoder/SAE literature well; figures not viewable.

---

# Peer Review Report

## Paper: Circuit Insights: Towards Interpretability Beyond Activations
## Reviewer: Mateo Szymanski, Reviewer 3 / Perspective (cognitive science and psycholinguistics department, Central Europe; fictional persona)
## Expertise: lexical semantics; construction grammar; human evaluation of concept descriptions
## Date: 2026-11-10

---

## Summary
The paper argues that descriptions of sparse LLM features should draw on model structure (weights and attribution circuits) rather than only on text where the feature fires. For token-like features the weights alone give a description; for context-dependent features, tracing which earlier tokens and heads cause a feature to fire yields more specific descriptions and a way to separate several concepts in one feature.

---

## Strengths

### S1: A principled view of "what a feature means"
Distinguishing input-invariant (weight) from input-dependent (activation) contributions (Eq. 1) gives interpretability a vocabulary closer to linguistics' lexical vs. constructional meaning. The finding that layer 21 features act as key–value pairs mapping tokens to collocations (Section 4: "apologize for", "will be") fits what usage-based accounts would predict.

### S2: Descriptions of grammatical, not just lexical, patterns
The case study of L12F619 (Section 5, Figure 5) describes a feature that tracks definite and demonstrative reference ("the", "this", "that", "former", "latter"), a discourse-level pattern that top-activation text rarely reveals. The prompt in Appendix C.2 explicitly asks for grammatical patterns and function words, a useful design choice.

### S3: Cost-aware design thinking
Section 5's analysis of how many generated tokens are needed (most influence on the first token; +1.4% of samples at layer 0 for more tokens, Figure 7) is the kind of practical guidance deployers need, and the paper recognizes that output-centric analysis is costly.

---

## Weaknesses

### W1: No human evaluation of whether the descriptions are actually understandable
All evidence is from FADE, whose judge and generator are LLMs (Section 3.3). Descriptions that are token lists ("apologize for", lemmatized forms) can score well on Clarity because they generate matching synthetic data, whether or not a person finds the feature understood. In psycholinguistics terms, the metric tests production-from-description, not comprehension. A small human study (say 30 features × 3 raters, forced choice between the description and a distractor) would anchor the metrics, especially as methods differ strongly in output format (token lists vs. one sentence).
- **Suggested Fix**: A small human validation on a stratified subset of features, with agreement statistics.

### W2: Lemmatization and token sets assume a lexical view of meaning
Lemmatization (Section 3.1) merges inflected forms, which will blur features that are morphologically specific (tense, agreement, number), exactly the kind of grammatical features that Section 5's prompts try to describe. The paper does not examine whether features that fail validation are disproportionately grammatical or syntactic, which would tell readers what the 25–59% coverage means linguistically.
- **Suggested Fix**: Categorize validated vs. unvalidated features (lexical / morphological / syntactic / semantic-topical) on a small hand-labelled sample.

### W3: Applicability beyond text-only English next-token models is unaddressed
The pipeline relies on tokens, an unembedding matrix and attention heads (Eq. 4–5). Multilingual, code and multimodal settings (where tokenization is not word-like) would change what a "validated token" means, and the paper does not discuss this. The Pile test partition (Appendix B) is English-heavy.
- **Suggested Fix**: Discuss scope, and show at least one code- or non-English-heavy slice.

### W4: Practical use for safety is asserted but not demonstrated
The Introduction motivates the work with safe and reliable deployment and with the risk of unfaithful explainer LLMs (Lermen et al.). Neither WeightLens nor CircuitLens is shown to find or fix any model behaviour, and CircuitLens still uses an explainer LLM per cluster (Section 3.2). The safety framing is thus aspirational.
- **Suggested Fix**: Include one downstream example (e.g., locating features for a specific behaviour with the descriptions) or tone down the framing.

### Minor
Figure 6 and Figure 5 selection (L12F619, L21F91) is not described; say whether they were random or curated.

---

## Missing References

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Helpful | Work on human evaluation of neuron/feature descriptions in auto-interp (describe the line of work; no specific paper recommended) | Anchors the LLM-judge metrics. |

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Solid framing, evaluation only by LLM-judged proxies on one model |
| Clarity | 3 | Understandable |
| Significance | 3 | A path to cheaper, less LLM-dependent descriptions and circuit-aware ones |
| Originality | 3 | A fresh combination aimed at an important gap |

## Dimension Scores (0–100)

**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clearly motivated, interesting direction with concrete qualitative cases, but the quantitative evidence is limited; I lean slightly toward the accept side because the framing could change how transcoder features are described.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Reasonable formulation |
| Clarity & Presentation | 66 | Competent | Clear narrative and cases |
| Novelty & Originality | 66 | Competent | Weight-plus-circuit view is a fresh combination |
| Significance & Impact | 66 | Competent | Plausibly useful for circuit-style interpretability |
| Experimental Validation | 54 | Developing | LLM-judged proxies only |
| Reproducibility | 58 | Competent | Prompts shared |
| Ethical Compliance | 70 | Competent | Nothing at stake |

---

## Questions for Authors
1. Would a small human study agree with the FADE ranking of WeightLens vs. MaxAct*? Agreement would raise my Experimental Validation score; disagreement would lower it.
2. What kinds of features fail the validation step (Section 3.1 step 2)?
3. Can you show one case where a description led to a behaviour-relevant discovery?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No**

## Overall Score
**4**: A promising, clearly motivated idea whose contribution to practice may be larger than the current evidence shows; the weaknesses are of the kind many accepted papers carry.

## Confidence
**3**: Outside the exact sub-area; relied on the text and captions.

---

# Peer Review Report

## Paper: Circuit Insights: Towards Interpretability Beyond Activations
## Reviewer: Ngozi Halloran, Reviewer 4 / Generalist (industry lab, West Africa / Europe; fictional persona)
## Expertise: deep learning for NLP; model analysis
## Date: 2026-11-10

---

## Summary
The paper introduces two interpretability tools for transcoder features of language models. WeightLens describes features from weights alone and works for features that fire on specific tokens; CircuitLens uses attribution to attention heads and output logits to isolate activation-relevant context and splits features into circuit-defined clusters before generating descriptions with an LLM. On Gemma-2-2b it improves FADE Clarity relative to top-activation baselines while leaving other metrics roughly flat or lower.

---

## Strengths

### S1: Clearly stated problem and venue fit
The Introduction (Section 1) states the gap well: explainer-LLM dependence, data dependence, and the limits of looking only at activations. ICLR regularly publishes interpretability work, and the transcoder/circuit setting is timely.

### S2: Two complementary methods with a sensible structure
Sections 3.1 and 3.2 are cleanly split by input-invariant vs input-dependent analysis, and Figure 1/Figure 2 captions describe the pipelines. The method section can be followed by a non-specialist who knows SAEs.

### S3: Honest results discussion
Section 4 and 5 describe where methods fail (layer 12; low Faithfulness; Purity favouring activation-based baselines), and the paper does not hide these.

### S4: Prompts in the appendix
Appendix C shows both prompts in full, which is helpful for reproducibility.

---

## Weaknesses

### W1: Headline claims are broader than the evidence
The abstract says the methods "increase interpretability robustness" and enhance scalable analysis "while maintaining efficiency and quality". The evidence in Tables 1–2 is a Clarity gain at four layers of one 2B model, no robustness test (no perturbation, seed or dataset-shift analysis beyond the 24M vs 3.6B token comparison), and no cost numbers. The conclusion's "covering up to 58.8% of cases" refers to GPT-2, while all quantitative tests use Gemma, where coverage is 32.7%.
- **Suggested Fix**: Rewrite the abstract and conclusion to match what is shown (higher Clarity; coverage per model; no efficiency claim unless measured).

### W2: Evaluation scope is thin for ICLR
Four layers (0, 7, 12, 21) of one model, ~250 features per layer, two baselines, no repeated runs, no human check (Tables 1–2). The Introduction mentions applications to GPT-2 and Llama, but Section 4 only reports their coverage (Figure 3). Why these layers and how features were drawn is not stated.
- **Suggested Fix**: Add at least a second model or a second layer set for Table 2, and state the sampling.

### W3: Presentation of results
Tables 1–2 carry many numbers without an indication of which differences matter; the captions say "Best results marked in bold", but without intervals the reader cannot tell. Section 4 and Section 5 mix model facts (ℓ0, RoPE) and method findings; no limitations section. Figure-dependent claims (Figures 3–8) could not be checked.
- **Suggested Fix**: Add a short summary table of per-metric mean differences with CIs; add a Limitations paragraph.

### Minor
Typos in Table 1 ("WeigthLens"; "0.7" in the MaxAct* layer-12 Purity cell), "similartly" (Section 4), the possessive "it’s" for "its" in Section 3.3.

---

## Missing References
Not my role (see Reviewer 2).

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Reasonable but under-tested |
| Clarity | 3 | Clear |
| Significance | 2 | A subset of features; narrow evaluation |
| Originality | 3 | A combination of ideas not seen together before |

## Dimension Scores (0–100)

**Pool position:** better than about 54% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: clear and well-motivated, but the evidence for the main claims is limited to one model and modest, mixed metric changes; a typical reader would want more before publication.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Pipeline sound; unstated parameters |
| Clarity & Presentation | 62 | Competent | Clear structure; abstract overclaims |
| Novelty & Originality | 58 | Competent | New for transcoders |
| Significance & Impact | 56 | Competent | Useful but narrow |
| Experimental Validation | 50 | Developing | Thin for ICLR |
| Reproducibility | 54 | Developing | Prompts, but no parameters |
| Ethical Compliance | 68 | Competent | Not at stake |

---

## Questions for Authors
1. Why layers 0, 7, 12, 21, and how were the ~250 features per layer drawn?
2. Can the abstract's "robustness" and "efficiency" be supported with a measurement? That would raise my rating.
3. Would the results transfer to a second model family (e.g., the Llama-3.2-1B transcoders already used for Figure 3)?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No**

## Overall Score
**3**: Interesting and clear, but the evidence is below what a typical accepted ICLR paper provides for claims of this breadth; narrowing the claims and adding a second model would move it to the accept side.

## Confidence
**3**: Not an interpretability specialist; read the full text.

---

# Devil's Advocate Report

## Paper: Circuit Insights: Towards Interpretability Beyond Activations
## Reviewer: Dmitri Okonkwo-Reyes (statistics and evaluation methodology group, research university, East Asia; fictional persona)

---

## Steelman
Transcoders split a feature's contribution into a weight-only term and an input-dependent activation, so a part of each feature's meaning can be read from weights without any explainer LLM or dataset, and the rest can be located by attributing activations to heads and tokens. The authors give a quantitative comparison with the standard activation-based pipeline on four layers and report where each method wins and loses.

---

## Core Argument Chain
1. Activation-based auto-interp is dataset- and explainer-LLM-dependent and often vague (Section 1).
2. Transcoder weights give input-invariant attributions that can be analyzed directly (Eq. 1; Section 3.1).
3. For token-based features, weight-derived token lists score at least as well as activation descriptions (Table 1).
4. For context-dependent features, attribution to heads and outputs isolates what triggers a feature, and circuit clustering separates concepts (Section 3.2; Table 2).
5. Circuit descriptions have higher Clarity than activation-based descriptions (Table 2).
∴ Structure-based methods make automated interpretability more robust, scalable and less dependent on data and LLMs (Abstract, Conclusion).

---

## Strongest Counter-Argument
The central inference from premises 3–5 to the conclusion rests on the FADE metrics, and those metrics are not neutral across the compared description formats. Clarity asks whether an LLM can generate text that activates the feature from the description. A WeightLens description is, by construction, a list of tokens that were verified to activate the feature in a forward pass (Section 3.1, step 2), so it will generate activating text trivially; at the same time the same lists score 0.02–0.03 Purity at three of four layers, i.e., they also generate text that activates the feature on unrelated content. The CircuitLens prompt tells the explainer to "Avoid vague phrases like" and to emit exact tokens (Appendix C.2), which again favours Clarity. In both cases the metric that improves is the one the method's output format is built to satisfy, while Purity (precision) is flat or lower, Responsiveness is within ±0.03 for the matched-data comparison, and Faithfulness is at floor (0.00–0.05) for every method, so it cannot discriminate.

So the data support a narrower claim: "format and prompt changes increase LLM-judged Clarity". Whether the descriptions are more correct, or more useful to a human, is untested, and no human, causal or downstream measurement exists in the paper. Add to this that Table 1's feature set is undefined, baseline numbers differ between Table 1 and Table 2 (e.g., MaxAct* layer-12 Clarity 0.33 vs 0.17), and there are no variance estimates. A skeptical reader can explain the entire pattern (Clarity up, Purity down) as a trade-off driven by description specificity rather than by access to circuit structure. The authors need an experiment that gives the baseline the same prompt and format, or a measurement that is not LLM-judged.

---

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The main claims are supported in a narrower form by the paper's own results (Clarity gains), the evaluation uses a held-out test partition (Appendix B), and the weaknesses below are fixable by narrowing claims and adding controls.

### MAJOR Issues

| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence / metric validity | Section 3.3; Tables 1–2; Appendix C.2 | The one metric that improves (Clarity) is sensitive to description format and prompt specificity; Purity (precision) is flat or lower, Faithfulness at floor. The evidence supports "higher LLM-judged Clarity", not "better interpretability". | Add a human-judged validation and a prompt-matched baseline. |
| DA-M2 | Scope / claim distortion (E5) | Abstract (claim of matching or exceeding existing methods); Table 1 | MaxAct* has higher Purity at all four layers and equal or higher Faithfulness at three of four; the abstract claim has no qualifier. The same holds for CircuitLens (Table 2: Purity lower at layer 21, 0.63 vs 0.64 for (top) and 0.54 vs 0.64 for the small-data variant). | Narrow the abstract to Clarity/Responsiveness. |
| DA-M3 | Evidence (selection bias) | Section 4 "∼250 features per layer"; Figure 3; Table 1 | If Table 1 uses features for which WeightLens produced a validated description, the comparison conditions on method success, and only 32.7% (Gemma) of features qualify. Table 1 and Table 2 give different baseline values for the same layers. | State and justify populations; report on all features with failures counted. |
| DA-M4 | Alternative explanation | Section 3.2 sampling; Table 2 vs MaxAct* | CircuitLens changes sampling (quantile vs top), masking, clustering, prompt and merge together; the "(top)" variants only equalize data, and no ablation isolates circuits. | Ablate prompt, masking and clustering separately. |
| DA-M5 | Overclaiming (E5) | Section 1 closing paragraph; Section 5; Abstract "scalable", "efficiency" | The paper says the approach "addresses the large dataset requirements and explainer LLM dependence", while Section 5 says that "circuit-based methods still depend on the dataset", CircuitLens uses GPT-4o-mini per cluster plus a merge, and no cost is measured. | Limit the claim to WeightLens, or demonstrate reduced cost. |
| DA-M6 | Logic | Section 4 explanations | Causal explanations are asserted without test: weak baselines at layers 0 and 7 "reflect" high ℓ0 ("which also explains the weak activation-based baselines"), and middle-layer drops are due to RoPE. | Present as hypotheses; test with ℓ0-matched transcoders or a RoPE-free comparison if feasible. |

### MINOR Issues

| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Presentation | Table 1 caption | Caption lists "Circuit-Based" though Table 1 has only WeightLens variants; "0.7" cell; "WeigthLens". |
| DA-m2 | Reproducibility | Section 3.2 | ρ, eps, min-samples, z-thresholds not given. |
| DA-m3 | Selection | Section 5, Figures 5–6 | Qualitative cases L12F619 and L21F91 have no stated selection rule. |
| DA-m4 | Soundness | Eq. (4) | No Jacobian for heads at l′ < l, unlike Eq. (2); clarify. |

---

## Numerical Sanity Check

| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| WeightLens vs MaxAct* Clarity, mean over layers (Table 1) | "Clarity and Responsiveness" higher | WL 0.59 vs MaxAct* 0.475 (+0.115); layer-wise +0.06, +0.08, +0.14, +0.18 | Yes |
| WeightLens vs MaxAct* Purity, mean (Table 1) | "activation maximization attains higher Purity" | WL 0.18 vs MaxAct* 0.2425 (reading "0.7" as 0.07) | Yes, text states it; abstract omits |
| Output tokens' effect on Clarity (Table 1, WL → WL+Out) | "comparable" | −0.05, −0.07, −0.08, −0.08 | Not discussed in text |
| Large-data vs small-data CircuitLens-Input (Table 2) | larger dataset "strongest performance across layers, particularly in clarity and responsiveness" | (top) − small: Clarity +0.15, +0.23, +0.08, +0.12; Responsiveness +0.04, +0.03, −0.01, +0.13 | Yes for Clarity; Responsiveness mixed |
| CircuitLens-Input (top) vs MaxAct* (Table 2) | circuit analysis improves quality | Clarity +0.16, +0.14, +0.10, +0.15; Responsiveness +0.03, +0.02, −0.01, +0.01; Purity −0.04, −0.01, −0.02, −0.01 | Clarity yes; Responsiveness within ±0.03; Purity lower |
| Small-data CircuitLens-Full vs MaxAct* Clarity (Table 2) | "in some cases outperform activation-based baselines" | +0.02, −0.04, +0.07, +0.13 | Yes (mixed) |
| WL+CircuitLens-Full vs CircuitLens-Full (top) gap (Table 2) | "further reduces sensitivity" | gap to (top) in Clarity: 0.14→0.11, 0.17→0.10, 0.02→0.01, 0.04→0.01 | Yes, modest |
| Abstract "up to 58.8%" | 58.8% | GPT-2 only; Gemma 32.7% (Section 4) | Yes, but tested model differs |

## Ignored Alternative Explanations
- The Clarity gain is produced by the more specific explainer prompt and output format, not by circuit information.
- Token lists are easy for an LLM to turn into activating text, so WeightLens Clarity and Responsiveness reflect format.
- Differences between Tables 1 and 2 come from different feature sets, and the "matches or exceeds" statement holds only on that set.
- Differences across models (Figure 3) reflect transcoder training (width, sparsity, architecture), not RoPE.

## Missing Stakeholder Perspectives
Practitioners who use descriptions for auditing need correctness and not only specificity. Humans who read descriptions are not consulted.

## Observations (Non-Defects)
- Held-out evaluation partition and open reporting of failures.
- The inclusion of "(top)" controls and the partial reporting by layer show a willingness to test their own claims.

---

## Dimension Scores (0–100)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 50 | Heuristics with no thresholds; metric validity untested |
| Clarity & Presentation | 60 | Readable, abstract overstated |
| Novelty & Originality | 54 | Combination; ingredients known |
| Significance & Impact | 52 | Narrow evidence |
| Experimental Validation | 44 | No variance, no ablation, no human check |
| Reproducibility | 50 | Missing parameters |
| Ethical Compliance | 66 | Not at stake |

**Pool position:** better than about 44% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main empirical gain (Clarity) is the one metric that the method's format is built to satisfy, and the comparison is not controlled for prompt or feature set.

## Overall: 3 | Confidence: 4

---

## Phase 1.6: Report Check (Synthesizer, Step 0)

Each weakness was tested for specificity, whether the paper already answers it, consistency with the paper, and actionability. Scores were not changed.

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1 (feature populations; Table 1 vs 2) | kept | Located; the paper does not answer it (searched Section 4, Appendix B) |
| R1 | W2 (no variance) | kept | Specific numbers and a concrete fix |
| R1 | W3 (confounded circuit contribution) | kept | Prompt in Appendix C.2 confirmed; no ablation rows in Table 2 |
| R1 | W4 (Table 2 trade-off) | kept; one number corrected | Layer-7 Clarity comparison rewritten (0.39 vs 0.44/0.48) after re-checking Table 2 |
| R1 | W5 (efficiency unmeasured) | kept | Search for runtime/GPU/hours found nothing |
| R1 | W6 (missing parameters) | kept | Search found no threshold, ρ value, DBSCAN settings or judge model |
| R1 | ERR-3 (layers 0/7 "poor") | moved to Minor | Depends on the metric intended; Medium confidence |
| R1 | ERR-4 ("0.7" cell) | moved to Minor | Cosmetic table typo |
| R2 | W1 (weight-space prior work) | kept, marked `[verify]` | Rests on my knowledge of earlier work, not on retrieved abstracts (literature check unavailable) |
| R2 | W2 (PRISM / embedding clustering) | kept | Verified: Kopf et al. is only in Appendix A.1 |
| R2 | W3 (narrow baselines) | kept | Only Neuronpedia and MaxAct* in Tables 1–2 |
| R2 | W4 (assumptions as heuristics) | rewritten | The claim that Figure 3 contradicts Assumption 2 is overstated: Assumption 2 is conditional ("If a token is strongly supported") and the figure is not viewable; kept as a request to quantify how many inherited tokens survive validation |
| R3 | W1 (no human evaluation) | kept | Search for "human" in the paper found nothing relevant |
| R3 | W2 (lemmatization) | kept as a question-style weakness | Speculative about what fails validation; fix is a small labelling study |
| R3 | W3 (scope beyond English text) | moved to Minor | Generic; does not bear on the main claims |
| R3 | W4 (safety use not shown) | kept | The Introduction motivates with safety; no demonstration |
| R4 | W1 (claims vs evidence) | kept | Abstract/conclusion quoted |
| R4 | W2 (thin evaluation) | kept | Merges with R1-W1/W2 in Phase 2 |
| R4 | W3 (presentation of results) | rewritten | Reduced to "add a summary of differences with CIs and a limitations paragraph" |
| DA | M1–M5 | kept | Each has a location and a fix |
| DA | M6 (causal explanations asserted) | kept | Quotes from Section 4 verified |
| DA | m4 (Eq. 4 Jacobian) | moved to Questions | Cannot verify from extracted equations; a clarity question, not an error |

## Phase 2: EIC Meta-Review and Decision

**Synthesizer part A** (issue map, official scores): see "Consensus and Disagreement Map" below. Official scores were computed with `aggregate_scores.py` (`scores_before.json` → `before.json`): official rating 3.20, official composite 56.5, no consistency warnings, no dimension spread above 20, no DA-CRITICAL issue raised, no integrity-scan finding.

# Editorial Decision

## Paper: Circuit Insights: Towards Interpretability Beyond Activations
## Submission ID: iclr26-2Jyb1yu3nN
## Date: 2026-11-10
## Target Venue: ICLR (stated by the user; profile `iclr`, scale status: secondary) | Paper Type: empirical
## Review Team (fictional personas): EIC (meta-reviewer) Adaeze Brandvold; R1 Methodology Ruoxi Almeida, R2 Domain Priyanka Vandenberg, R3 Perspective Mateo Szymanski, R4 Generalist Ngozi Halloran, DA Dmitri Okonkwo-Reyes

---

## Decision: Borderline Reject (3), shown as ICLR rating 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 3 → mean 3.20 · official composite 56.5
**EIC assessment** (internal): weighted rating 3.17 → starting point 3 · weighted composite 56.1 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**EIC pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%): the paper is in the upper half of the typical-rejected band (30–54), below the 55–69 borderline range.
**Journal recommendation:** not applicable (conference target).

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A timely, clearly motivated attempt to ground feature descriptions in transcoder weights and attribution circuits. WeightLens gives a cheap, LLM-free description route for token-driven features and reports honest coverage per model (Section 4, Figure 3). CircuitLens shows a consistent Clarity gain over the baselines on identical data (Table 2 "(top)" rows: +0.10 to +0.16), and the paper reports its own failures (Purity, Faithfulness, layer 12).
- **Against acceptance:** The evidence for the headline claims is thin for ICLR: one 2B model for all quantitative results, four layers, two baselines, no variance, an undefined feature population, baseline numbers that differ between Tables 1 and 2, and a circuit method whose contribution is confounded with sampling and prompt changes. The metric that improves (Clarity) is the one most sensitive to description format, while Purity is lower and Faithfulness at floor. The abstract and conclusion state more than the tables show.

### Verification of Decisive Points (EIC read of the paper)

| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Baseline scores differ between Table 1 and Table 2 (MaxAct* L12 Clarity 0.33 vs 0.17; L21 0.53 vs 0.39; Neuronpedia L12 0.28 vs 0.15) | R1 ERR-1, DA-M3 | Tables 1–2; Section 4 | Verified | Re-read both tables. Cause (different feature sets) is plausible but unstated. |
| Abstract says WeightLens matches or exceeds existing methods, but Purity (and Faithfulness at 3 of 4 layers) favour MaxAct* | R1 ERR-2, DA-M2 | Abstract; Table 1; Section 4 | Verified | Section 4 text does admit the Purity gap; the abstract does not. Mean Purity 0.18 vs 0.24. |
| Adding output tokens lowers Clarity at all four layers relative to plain WeightLens | R1 ERR-5 | Table 1 | Verified | 0.56→0.51, 0.62→0.55, 0.47→0.39, 0.71→0.63; not discussed in Section 4. |
| CircuitLens's gain is not isolated from prompt, sampling and merge changes; no ablation | R1-W3, DA-M4, R2-W2 | Section 3.2; Appendix C.2; Table 2 | Verified | Table 2 has no prompt-only, masking-only or embedding-clustering row. |
| The only metric that improves (Clarity) is sensitive to format/prompt | DA-M1, R3-W1 | Section 3.3; Table 1–2; Appendix C.2 | Partly correct | The pattern (Clarity up, Purity down or flat) is verified; that Clarity "rewards specificity" is an inference about FADE that the paper does not test. |
| CircuitLens Clarity gain over MaxAct* on identical data is +0.10 to +0.16 while Responsiveness is within ±0.03 and Purity −0.01 to −0.04 | R1-W4, DA numerical check | Table 2 | Verified | Recomputed. |
| Dataset and explainer-LLM dependence is "addressed" vs "circuit-based methods still depend on the dataset" | DA-M5 | Section 1 closing paragraph; Section 5 | Verified | CircuitLens also calls GPT-4o-mini per cluster (Section 3.2). WeightLens's basic variant has no LLM. |
| No cost, runtime or variance reported | R1-W2/W5 | whole paper | Verified | Text search found no GPU/hours/seeds/CIs. |
| Missing procedure parameters (z-threshold, ρ, DBSCAN) and FADE judge | R1-W6, DA-m2 | Sections 3.1–3.3 | Verified | Search found none; may sit in unavailable code. Treated as a reproducibility gap, not a fatal one. |
| Weight-space vocabulary-projection prior work is not cited | R2-W1 | Section 2; Appendix A | Partly correct | Absence from the paper is verified; the precedent comes from reviewer knowledge (literature check unavailable), so it stays `[verify]` and is not a required comparison. |
| PRISM (Kopf et al.) appears only in Appendix A.1, no comparison with embedding clustering | R2-W2 | Section 2; Appendix A.1; Section 3.2 | Verified | Section 2 does not mention it. |
| Assumption 2 is contradicted by Figure 3 | R2-W4 | Section 3.1; Figure 3 | Overstated | Assumption 2 is conditional; figure not viewable. The underlying request (quantify surviving inherited tokens) stands. |
| "58.8%" coverage refers to GPT-2; quantitative tests use Gemma (32.7%) | R4-W1 | Conclusion; Section 4 | Verified | |
| Layers 0 and 7 "perform poorly" vs Table 1 | R1 ERR-3 | Section 4; Table 1 | Partly correct | Poor relative to layer 21 (Responsiveness, Purity), not relative to layer 12 (Clarity). Minor. |
| Eq. (4) omits the Jacobian for heads at l′ < l | DA-m4 | Section 3.2 | Unverifiable | Extraction garbles equations; treated as a question to authors. |

### Reviewer Weights

| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Most points verified against both tables (ERR-1, ERR-2, ERR-5, missing parameters); well calibrated; one number corrected in Phase 1.6 and two minor entries. |
| R2 (Domain) | 3 | 4 | 1.0 | W2 and W3 verified; W1 rests on knowledge, not retrieved abstracts, and W4's Figure-3 point is overstated; these offset. |
| R3 (Perspective) | 4 | 3 | 1.0 | Sound, constructive, and the human-evaluation gap is verified; some points are generic. Lenient end is the role's job, not a defect. |
| R4 (Generalist) | 3 | 3 | 1.0 | Typical PC-style review; the overclaim and scope points are verified; largely overlaps R1. |
| DA | 3 | 4 | 1.0 | M2, M3, M4, M5 verified; M1 partly inferential; correctly raised no CRITICAL issue. |

### DA-CRITICAL Rulings

| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | n/a | n/a |

The EIC also checked the five CRITICAL criteria against the paper (no evidence contradicts the main claim; the experiments do test Clarity, Responsiveness and Purity; the reported split is a test partition, Appendix B, with no selection statement found; no fabrication signal; the method is understandable), so no issue was added.

### Final Decision and Justification
The EIC-weighted rating (3.17) rounds to 3 and the composite (56.1, band 3) agrees, so the starting point and the cross-check coincide and I keep 3. The reviewers' recommendations cluster at 3 because the verified issues are those that typical rejected submissions share: a comparison whose population is undefined, no variance, a headline gain that is not isolated from prompt and sampling, and an abstract that goes beyond the tables. R3's 4 rests on potential rather than on verified evidence of the effect size, and I give it its own weight but not more. There is no DA ceiling (no CRITICAL issue). The decision is not "the idea is poor": the weaknesses are fixable (state the populations, add variance and two or three ablations, narrow the claims), which is why this is a Borderline Reject and not a Reject. I would expect a revised version with a matched-prompt ablation, confidence intervals, a second model and a human spot-check to move into the borderline range or above. This is a simulation of how a careful panel would likely see this draft, not a prediction.

---

## Score Summary

### Official Scores and EIC Assessment (from `aggregate.json`, `--venue iclr --final 3`)

Reviewer table: official rating mean 3.20; EIC-weighted rating 3.17 (weights = confidence × EIC quality weight; shares R1 25.5%, R2 20.4%, R3 16.8%, R4 16.8%, DA 20.4%). Per-reviewer composites: R1 53.6, R2 57.4, R3 62.4, R4 56.7, DA 52.3.

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 52 | 58 | 62 | 56 | 50 | 55.6 | 55.2 | 12 |
| Clarity & Presentation | 62 | 64 | 66 | 62 | 60 | 62.8 | 62.7 | 6 |
| Novelty & Originality | 56 | 60 | 66 | 58 | 54 | 58.8 | 58.4 | 12 |
| Significance & Impact | 52 | 56 | 66 | 56 | 52 | 56.4 | 55.8 | 14 |
| Experimental Validation | 46 | 50 | 54 | 50 | 44 | 48.8 | 48.4 | 10 |
| Reproducibility | 50 | 54 | 58 | 54 | 50 | 53.2 | 52.8 | 8 |
| Ethical Compliance | 66 | 66 | 70 | 68 | 66 | 67.2 | 67.0 | 4 |
| **Composite** | 53.6 | 57.4 | 62.4 | 56.7 | 52.3 | **56.5 (before)** | **56.1 (after)** | |

No dimension exceeds the 20-point spread threshold; no consistency warnings.

### Target-Venue Scores (ICLR, scale status: secondary: recent forms use these fields; verify against the current form)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 2 |
| Rating (from the final decision 3) | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); venue composite 56.0, band 3 |

### Cross-Venue Outlook
Not requested.

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Circuit Insights: Towards Interpretability Beyond Activations" to ICLR.

The paper addresses a real bottleneck in automated interpretability, the dependence of feature descriptions on explainer LLMs and large datasets, by using the structure that transcoders expose.

**Overall Assessment:**
The panel found the direction timely and the writing clear, and appreciated that you report where your methods fail. The consensus concern is that the experiments, as presented, do not yet establish the size and source of the gains, and that the abstract and conclusion claim more than Tables 1–2 show.

**Key Strengths Identified by Reviewers:**
1. A cheap, LLM-free route to descriptions for token-driven transcoder features, with honest coverage numbers per model (R1, R3, R4).
2. A principled split into input-invariant and input-dependent analysis, with concrete case studies for context-dependent features (R2, R3, R4).
3. Useful controls and candid reporting (the "(top)" rows; Purity and Faithfulness limits discussed) (R1, R4, DA).

**Key Concerns Requiring Attention:**
1. Claims broader than the evidence ("matching or exceeding", "robustness", "efficiency", dataset and LLM dependence "addressed") (R1, R4, DA, R3; CONSENSUS-4).
2. Undefined evaluation population and baseline numbers that differ between Tables 1 and 2; no variance or intervals (R1, R4, DA; CONSENSUS-3).
3. The circuit contribution is confounded with sampling, prompt and merge changes; no ablation or embedding-clustering baseline (R1, R2, DA; CONSENSUS-3).

No Devil's Advocate CRITICAL issue was raised.

**Decision: Borderline Reject (3)**

The balance falls slightly toward reject because the central quantitative claims rest on one model, undefined feature sets and single runs, and the improvement is concentrated in a format-sensitive metric. The issues are fixable. A revision that states the evaluation populations, adds intervals, isolates the circuit contribution with matched-prompt ablations, narrows the abstract, and adds a second model and a small human check would move this toward acceptance. Please refer to the Revision Roadmap below.

Sincerely,
Adaeze Brandvold
Editor-in-Chief (meta-reviewer; fictional persona)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Claims (robustness, efficiency, "matching or exceeding", dataset/LLM dependence) go beyond the evidence | R1 (ERR-2), R3 (W4), R4 (W1), DA (M2, M5) | CONSENSUS-4 |
| Evaluation scope thin, no variance or intervals; undefined feature population | R1 (W1, W2), R4 (W2, W3), DA (M3), R2 (W3 narrow baselines) | CONSENSUS-4 |
| Circuit contribution not isolated (prompt, sampling, clustering ablations missing) | R1 (W3), R2 (W2), DA (M4) | CONSENSUS-3 |
| Efficiency/scalability unmeasured | R1 (W5), R4 (W1), DA (M5) | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Overall leaning and significance of the direction | R3 (Overall 4; Significance 66) | R1, R2, R4, DA (Overall 3) | The verified evidence supports the narrower view; R3's reasons concern potential, not demonstrated effect. Kept at 3. |
| LLM-judge metrics adequacy | R3-W1, DA-M1 (inadequate without humans) | R1, R2, R4 (accept FADE as standard but ask for variance) | FADE is a published metric, so no reviewer is wrong, but a human check is cheap and is on the Roadmap (Priority 2). |
| Weight-space novelty | R2-W1 (not positioned) | R3 (novel combination) | Unverified without retrieval; handled as a `[verify]` reference suggestion. |

### Score Spread Discussion
No dimension is flagged (all spreads ≤ 14). R3 is the high outlier on Significance and Novelty (66 vs 52–60 for the others); the EIC weights its view at 1.0 and sees no verified evidence for the gap.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| none | CRITICAL | No CRITICAL issues found | n/a | n/a | n/a |
| DA-M1 | MAJOR | Clarity is format-sensitive; evidence supports only LLM-judged Clarity gains | Yes (R3-W1) | n/a | n/a |
| DA-M2 | MAJOR | Abstract claim vs Purity/Faithfulness | Yes (R1 ERR-2, R4) | n/a | n/a |
| DA-M3 | MAJOR | Feature population undefined; Table 1 vs 2 | Yes (R1-W1) | n/a | n/a |
| DA-M4 | MAJOR | Circuit contribution confounded | Yes (R1-W3) | n/a | n/a |
| DA-M5 | MAJOR | Dataset/LLM-dependence and efficiency overclaimed | Yes (R1-W5, R4-W1) | n/a | n/a |
| DA-M6 | MAJOR | Causal explanations in Section 4 untested | Partly (R2 Minor) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*No DA-CRITICAL issue was upheld. These items were verified by the EIC as undermining a main claim as worded.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Claims in Abstract/Conclusion exceed the tables (matching/exceeding, robustness, efficiency, dataset/LLM dependence) | R1 ERR-2, R4-W1, DA-M2, DA-M5, R3-W4 | Abstract; Section 1; Conclusion; Tables 1–2 | Say "higher Clarity and Responsiveness, lower Purity on token-based features"; drop or measure "robust"/"efficient"; limit LLM-independence to WeightLens basic variant | Low (text) | Yes |
| R2 | Evaluation population undefined; Table 1 vs Table 2 baseline numbers differ | R1-W1/ERR-1, DA-M3 | Section 4; Tables 1–2; Appendix B | State selection rule and N per table; report on all features with failures counted, and on a matched random sample for every method | Low–Med (≈ a few GPU/API-hours) | Yes |
| R3 | Circuit contribution not isolated from sampling/prompt/merge | R1-W3, DA-M4, DA-M1, R2-W2 | Section 3.2; Appendix C.2; Table 2 | Ablate: new prompt on raw top activations; masking without clustering; embedding clustering instead of circuit clustering; same explainer for all baselines | Med (3× the CircuitLens description run) | Partly |
| R4 | No variance or intervals; differences of 0.01–0.03 | R1-W2, R4-W3, DA numerical check | Tables 1–2 | Paired bootstrap over features, 3 re-runs of generation/judging | Low–Med | Yes |

### Priority 2 — Strongly Suggested (Should Fix)

| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Missing parameters (z-threshold, ρ, DBSCAN eps/min-samples, FADE judge) and no sensitivity | R1-W6, DA-m2 | Parameter table and a sensitivity sweep; describe the validation contexts in Step 2 | Low–Med | Yes |
| S2 | No cost/runtime numbers | R1-W5, DA-M5 | Cost table (feature-hours, LLM calls/tokens, memory) | Low | Yes |
| S3 | LLM-judge validity untested | R3-W1, DA-M1 | Small human study (e.g., 30 features × 3 raters, forced choice) with agreement | Med | Partly |
| S4 | Output component hurts Clarity and never raises Faithfulness | R1 ERR-5, Table 1 | Discuss; justify or drop the "+Out" variant | Low | Yes |
| S5 | Related work: weight-space vocabulary analyses; PRISM only in Appendix | R2-W1, R2-W2, Missing References | Move/extend Section 2; add a plain unembedding-projection baseline and an embedding-clustering baseline | Med | Partly |
| S6 | One model, four layers, two baselines | R4-W2, R2-W3 | Second model (e.g., the Llama-3.2-1B transcoders already used) for Table 2; add an output-centric baseline | Med–High | No |
| S7 | Causal explanations in Section 4 untested | DA-M6, R2 Minor | Label as hypotheses or test with ℓ0-matched/RoPE-free comparisons | Low | Yes |

### Priority 3 — Nice to Fix (Optional)

| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Lemmatization and failed-validation features (lexical vs grammatical) | R3-W2 | Small hand-labelled breakdown |
| N2 | Eq. (4) Jacobian for l′ < l | DA-m4, R1 Q5 | Clarify in Section 3.2 |
| N3 | Typos and table issues ("WeigthLens", "0.7", Table 1 caption, "similartly") | R1 ERR-4, R4 Minor, DA-m1 | Fix |
| N4 | Qualitative case selection (L12F619, L21F91) | DA-m3, R3 Minor | State selection rule |
| N5 | Safety motivation not demonstrated; scope beyond English text | R3-W3/W4 | One downstream example or tone down |
| N6 | Points the EIC judged overstated (Assumption 2 vs Figure 3) | R2-W4 | Reframe as heuristics |

---

## Estimated Revision Effort
- Priority 1: 4 items, about 3–5 days (mostly re-running evaluation with intervals and ablations, plus text edits).
- Priority 2: 7 items, about 1–2 weeks (human study and second model dominate).
- Priority 3: 6 items, under 1 day.
- **Total estimated revision time**: roughly 2–3 weeks; the Priority 1 items are largely feasible within an ICLR discussion period.

*Not part of the review: the optional Gap Scout (Post-Review Analysis) was not requested and was not run.*
