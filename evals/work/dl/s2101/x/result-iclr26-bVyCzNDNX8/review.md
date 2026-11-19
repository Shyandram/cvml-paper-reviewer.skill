# Academic Paper Review: MixtureKit (ICLR, full mode)

Date: 2026-11-10 · Skill: academic-paper-reviewer v2.10.1 · Request: "Review this paper. Target venue: ICLR. Full review, skip confirmation, literature check: strict, cutoff date 2025-09-24."

**Run disclosures.** (1) The five reviewer reports are sequential role-based passes that share one model context, not independent agents. (2) Figures were not available; Figures 1–3 are judged from captions and extracted text only. (3) **Literature check:** `related_search.py` was attempted twice (strict mode, cutoff 2025-09-24) and the arXiv API returned HTTP 429 both times. No results were kept, so no ledger-backed labels exist. Missing references and novelty statements below rest on knowledge and are marked `[verify]`. (4) `integrity_scan.py` was not run, because this run was limited to reading files and the aggregation script. Instead the full paper text was searched manually for text addressed to reviewers or AI systems, and none was found. The reviewers read the unredacted text. (5) The paper has no appendix beyond an "LLM Usage" note and no supplement.

---

# PHASE 0: Paper Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | MixtureKit: A General Framework for Composing, Training, and Visualizing Mixture-of-Experts Models |
| Primary Discipline | ML → LLM systems / sparse Mixture-of-Experts (MoE) tooling |
| Secondary Discipline(s) | Model merging and upcycling; multilingual NLP (Egyptian Arabic, code-switching); interpretability tooling; research software engineering |
| Paper Type | **System** (open-source library) (composite weights: system) |
| Core Technique(s) | Composing HuggingFace checkpoints into MoE (Traditional/Mixtral-style, BTX) and stitch-based (BTS) models; regex-driven class patching; Streamlit routing visualizer |
| Target Venue | ICLR (stated); profile key `iclr` (2026 cycle, scale status: secondary) |
| Venue-Specific Notes | ICLR has no software or library track; reviewers will still ask for a scientific contribution or convincing evidence. Submissions and reviews are public. |
| Paper Maturity | Submission-ready in form (about 9 pages of main text), but the evaluation is thin |
| Ethics-Relevant Content | None direct (no human subjects). The experiment uses web or instruction data (Wild-Chat, Arabic and Arabizi corpora), with no data statement. |

### Claimed Contributions (as stated by the authors)
1. **C1** Unified composer class: a one-line merge/build function and full pipeline that patches model config, decoder and causal-LM classes and saves a unified checkpoint (§1 bullet 1, §3.2).
2. **C2** Traditional MoE, BTX and BTS implementations "previously unavailable to the open community" with "full support for all model families", plus a load-balancing implementation (§1 bullet 2, §3.1).
3. **C3** Token-routing visualization at a high level (dominant expert per token) and a low level (per-token expert percentages) (§1 bullet 3, §3.3, Fig. 3).
4. **C4** Empirical: a BTX model built with the toolkit "can outperform baseline dense models on multiple benchmarks"; the authors "successfully reproduced the findings" of Nile-Chat (Abstract, §4, Table 1).
5. **C5** Cost and extensibility: recycling checkpoints "substantially" reduces training cost; new MoE variants need only "a small adapter module" (§1, §3.2 Extensibility, §5).

### Paper memory (shared factual record)
- **Setup facts.** Base model Gemma3-4B-pt, continually pre-trained separately on Arabic-script and Latin-script data to give two experts (§4). Combined by BTX into 3 experts (base + 2) with top-2 routing, "6B activated parameters" (Nile-Chat-3x4B-A6B), and a 2-expert variant (2x4B-A6B). Training: SFT with LoRA (alpha 512, lr 1e-4, effective batch 256), English Wild-Chat mixed in, then DPO. Not stated anywhere: LoRA rank and target modules, whether routers are trained, load-balancing α used, data sizes, total parameter count, compute or GPU-hours, seeds or number of runs, benchmark names and sizes, the dense baselines' recipe, train/val/test protocol or checkpoint selection. The paper defers "the evaluation procedure" to Shang et al. (2025).
- **Headline numbers** (all from Table 1, single values, no variance): Avg Arabic 53.01 (dense 4B), 55.87 (2x4B), 55.74 (3x4B), 60.0 (dense 12B); Avg Latin 49.07 / 52.32 / 51.23 / 52.61; Translation-Long chrF 58.4 / 61.59 / 61.9 / 60.61; Translation-Short 52.01 / 53.71 / 55.37 / 53.53; Transliteration 80.44 / 83.89 / 83.97 / 80.97.
- **Appendix:** only "A LLM Usage". **Unverifiable:** Fig. 1 and Fig. 3 are text-extracted only. Fig. 3 Arabic strings are garbled by extraction and are not treated as errors.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Lucía Ferreira-Oyelaran, large public research university (Latin America)
- **Seniority / Expertise**: Senior faculty, repeat area chair / sparse and conditional-computation models, scalable training systems
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Rewards honest scope and measured evidence; asks what a reader learns that they could not get from the code README.

### Reviewer 1 (Methodology): Dr. Kwabena Adjei-Marlow, industrial research lab (Europe)
- **Seniority / Expertise**: Mid-career industry scientist / LLM evaluation protocols, MoE training and router dynamics
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on matched active and total parameter budgets and on stated protocols.

### Reviewer 2 (Domain): Dr. Priyanka Ranganathan-Holt, large public research university (South Asia)
- **Seniority / Expertise**: Senior faculty / model merging, sparse upcycling, parameter-efficient adaptation
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Checks what each cited work actually does before accepting a novelty statement.

### Reviewer 3 (Perspective): Prof. Mateo Brandt-Szabo, software-engineering department, public university (Central Europe)
- **Seniority / Expertise**: Senior faculty / research-software sustainability, developer tooling, human-centred interpretability tools
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive; looks for how a tool survives contact with real users.

### Reviewer 4 (Generalist): Dr. Yuki Tanabe-Okafor, university NLP/ML group (East Asia)
- **Seniority / Expertise**: Mid-career / language models, multilingual NLP (typical ICLR program-committee member)
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Pragmatic; asks "is this an ICLR paper or a README?"

### Devil's Advocate: Dr. Oskar Lindqvist-Amara, independent evaluation-methodology lab (Northern Europe)
- **Seniority / Expertise**: Senior research scientist / evaluation methodology, reproducibility, causal attribution of gains
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; separates "unsupported" from "contradicted".

*Personas are fictional. Proceeding with the stated assumptions.*

---

# PHASE 1: Independent Reviews

(Base rate for the pool-position estimate: ICLR 2026 accepted share ≈ 27% of submissions.)

---

# Peer Review Report

## Paper: MixtureKit: A General Framework for Composing, Training, and Visualizing Mixture-of-Experts Models
## Reviewer: Dr. Kwabena Adjei-Marlow, Methodology (industrial research lab, Europe; fictional persona)
## Expertise: LLM evaluation protocols; MoE training and router dynamics
## Date: 2026-11-10

## Summary
The paper presents an open-source Python library that builds MoE models from existing HuggingFace checkpoints. It offers a Mixtral-style "Traditional" MoE, BTX (per-projection routers over expert FFNs) and BTS (frozen experts joined by trainable stitch layers). It automates config and class patching and ships a Streamlit visualizer for per-token expert weights. The only empirical evidence is one case study (§4, Table 1): two BTX-composed Egyptian Arabic/Arabizi models (2 and 3 experts, built from Gemma3-4B) compared with dense 4B and 12B Nile-Chat models and with the two script experts. The authors say they reproduced earlier published results.

## Strengths
### S1: Practical, concrete engineering design
§3.2 describes the config-driven pipeline (Fig. 2), expert composition into a unified state dict, and class patching through `replace_script`, `modify_decoder` and `modify_model`. This is specific enough to understand what the tool does and how a new variant would be registered.

### S2: Demonstration on a family outside the earlier tools' stated support
The §2 critique of Mergoo is that it targets hand-written configs for Phi3, Mistral and Llama. §4 builds MoE models from Gemma3-4B, which the paper does not list among those families. This is one weak data point for the generality claim.

### S3: Case study shows the composed models are functional and behave sensibly
In Table 1 both composed models beat the dense 4B model on all five columns (e.g., Avg Arabic 55.87 vs 53.01; Transliteration 83.89 vs 80.44). The Latin expert collapses on Arabic translation (37.09 Long chrF), which is consistent with script specialization.

## Weaknesses
### W1: The evidence does not test the library claims, and no variance is reported (most severe)
The main empirical claim (C4) is "can outperform baseline dense models on multiple benchmarks". The library claims (C1, C2, C5) are about generality, three methods and lower cost. Table 1 covers one base model, one method (BTX) and one language pair. Traditional MoE and BTS are never evaluated, and the load-balancing loss is never exercised (Fig. 2 even sets `"alpha": 0`). There is no latency, memory, throughput or GPU-hour measurement, so "substantially reducing computational training costs" (§1) is unmeasured. All results are single numbers with no seeds. Several margins are small: Translation-Short 53.71 (2x4B) vs 53.53 (12B) is 0.18 chrF, derived.
- **Suggested Fix**: Evaluate all three methods on one common setup (about 3 seeds × 3 methods, roughly 100–300 GPU-hours at 4B scale). Report training and inference cost against dense models: wall-clock, peak memory, tokens/s, total and active parameters.

### W2: "Reproduced the findings" cannot be verified, and the baselines are undefined
§4 says "we successfully reproduced the findings", but Table 1 gives no numbers from the original Nile-Chat work next to the reproduced ones. The dense "Nile-Chat-4B" and "-12B" rows are not described (data, SFT/DPO recipe, whether the 12B uses the same data). The comparison of 6B-active/larger-total MoE against a 4B dense model is therefore not matched in active or total parameters, data or compute. The fairness checklist items (same data, same schedule, same tuning effort) are all "unclear".
- **Suggested Fix**: Add original vs. reproduced columns, and describe the dense baselines. Include a parameter-matched dense control and the total parameter count for each MoE.

### W3: Key experimental details are missing, so §4 is not self-contained
Protocol sweep (searched the whole text for test/validation/held-out/selected/tuned/checkpoint/best/hyperparameter): none of these appears. LoRA rank and targets, whether routers are trainable, the α used, data sizes, benchmark names and checkpoint selection are not stated. A reader cannot tell which split produced Table 1 or how the final checkpoint was picked. All of it is deferred to Shang et al. (2025).
- **Suggested Fix**: Add a short appendix with the full recipe, the benchmark list and split, and the selection rule. State the compute used.

### W4: The component-level claims have no ablation
§3.1 asserts that per-projection routers (BTX) give "greater degrees of freedom" while Traditional routing has fewer parameters, and that router-only tuning "results in a slight degradation of performance". None of this is tested here. The added base-model expert "enhanced English capabilities" (§4), but no English benchmark is reported, and 3x4B is below 2x4B on Latin (51.23 vs 52.32, derived −1.09).
- **Suggested Fix**: Add Traditional vs BTX vs router-only vs full fine-tuning, plus an English benchmark for the 3-expert variant. Otherwise remove the claims.

**Minor**: "Acree-AI" (§2) vs. "Arcee" in the reference; "Osborne (2024) Furthermore, the work by Osborne et al. (2024)" (§1) is a duplicated citation fragment; `stitch_freq` appears in a BTX config (Fig. 2).

### Claim-to-Evidence Map
| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | One-line unified composer | §1, §3.2, Fig. 2 | Description only; one working example | Partially (works for Gemma3 BTX; no test matrix) |
| C2 | 3 methods, "all model families", load balancing | §1, §3.1 | BTX only in §4 | Partially / Unsupported for BTS, Traditional, "all families", load balancing |
| C3 | Routing visualization is useful | §3.3, Fig. 3 | One toy-scale example | Partially (exists; usefulness untested) |
| C4 | BTX model outperforms dense baselines; reproduced | Abstract, §4, Table 1 | Table 1 | Partially (beats 4B on all 5 columns; below 12B on 2 of 5; reproduction unverifiable) |
| C5 | Reduces cost; extensible | §1, §5 | None measured | Unsupported |

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E5/E6 | §1 bullet 2 vs §2 Mergoo | "previously unavailable to the open community, are now accessible with full support for all model families" vs "was the first package to deliver open-source implementations of new MoE-based merging techniques such as BTX" | The paper's own related work says BTX was already available in an open package, so "previously unavailable" is wrong for BTX. §2 also notes MergeKit offers MoE merging. | Cross-referenced (two locations) | High | MAJOR | Narrow to what is new (e.g., BTS, wider architecture coverage) and say which families were tested |
| ERR-2 | E5 | §4 | "enhanced English capabilities" | No English result appears in Table 1 or elsewhere | Searched text for "English": only the sentence itself and the Wild-Chat mixing | High | MAJOR | Add an English benchmark or remove the claim |
| ERR-3 | E5 | Abstract vs Table 1 | "can outperform baseline dense models on multiple benchmarks" | The 12B dense model beats both MoEs on Avg Arabic (60.0 vs 55.87 / 55.74, derived +4.13 / +4.26) and on Avg Latin vs 3x4B (52.61 vs 51.23, derived +1.38). The claim holds against the 4B dense only. | Recomputed from Table 1 | High | MAJOR (claim wording; the weaker claim survives) | Name the baseline and note the 12B result in the abstract |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 1 | Single runs, one method evaluated, no ablation, undefined baselines |
| Clarity | 2 | Readable, but §4 is not self-contained and Table 1 columns are undefined |
| Significance | 2 | Useful if it works broadly, but the breadth is not shown |
| Originality | 1 | The methods are prior; the contribution is engineering |

## Dimension Scores (0–100)
**Pool position:** better than about 25% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the library claims are tested by one single-run case study of one method, and "reproduction" is not checkable. These are signals of a typical rejected submission.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 38 | Developing | Implementation detail is plausible, but no verification of fidelity to BTX/BTS and no ablation |
| Clarity & Presentation | 58 | Competent | Clear structure, but undefined baselines and missing recipe |
| Novelty & Originality | 32 | Developing | Re-implementation of cited methods; "Traditional MoE" is an existing recipe |
| Significance & Impact | 45 | Developing | Real practical value is plausible but unquantified |
| Experimental Validation | 28 | Developing | One case study, no seeds, no efficiency measurement |
| Reproducibility | 45 | Developing | Code promised, but recipe, LoRA rank, data and compute are absent |
| Ethical Compliance | 60 | Competent | Future Work lists tool limitations; no data or broader-impact statement |

## Questions for Authors
1. What are the original Nile-Chat numbers for each Table 1 column, and how large is the gap to your reproduction? A match within noise would raise my Experimental Validation score.
2. What are the total parameters of the 2x4B and 3x4B models, and the measured latency and memory against the dense 4B and 12B? This would test the efficiency framing.
3. Which split and benchmarks produce Table 1, and how was the final checkpoint chosen? A rule independent of the reported split would remove a protocol doubt.
4. Do the Traditional and BTS implementations reproduce the results of their original papers on any shared setup? If not, in what sense are they "supported"?

## Limitations Assessment
**Partially.** §6 lists the dependence on HuggingFace config versions, missing vLLM kernels and same-architecture merging only. Missing: memory overhead of BTS, untested model families, and the single-case evaluation.

## Ethics Review Flag
**No.**

## Overall Score
**2**: A useful-looking toolkit, but the experiments do not test its main claims and the baselines are not described. This is below the ICLR bar as submitted.

## Confidence
**4**: Confident. I read the whole text (short, no appendix). I could not see figures.

---

# Peer Review Report

## Paper: MixtureKit: A General Framework for Composing, Training, and Visualizing Mixture-of-Experts Models
## Reviewer: Dr. Priyanka Ranganathan-Holt, Domain (large public research university, South Asia; fictional persona)
## Expertise: Model merging; sparse upcycling; parameter-efficient adaptation
## Date: 2026-11-10

## Summary
The submission packages three ways of turning pre-trained or fine-tuned checkpoints into an MoE (Mixtral-style "Traditional", BTX, BTS) behind one configuration interface, adds a routing visualizer, and illustrates the pipeline on an Egyptian Arabic/Arabizi model family. The stated gap is that MergeKit and Mergoo are tied to specific model families and lack BTS or fine-grained BTX.

## Strengths
### S1: Well-motivated gap
§1 and §2 position the work against MergeKit (fixed Mixtral/DeepSeek/Qwen MoE layouts) and Mergoo (hand-written configs for Phi3/Mistral/Llama). The "recycling" motivation (§1, citing Osborne et al. 2024 on models left unused) is reasonable.

### S2: Faithful basic description of BTM → BTX → BTS lineage
§2 and §3.1 describe Branch-Train-Merge, BTX (FFN experts, averaged attention) and BTS (frozen experts, stitch layers with softmax/sigmoid gating). The BTS description of two stitch directions is concrete.

### S3: Useful interpretability angle
Making per-token expert weights inspectable (§3.3, Fig. 3) is a sensible companion to composed MoEs, especially for a script-specialized setting where a "right" routing is easy to judge.

## Weaknesses
### W1: The algorithmic content is entirely prior work, and a closely related line is not cited
BTX (Sukhbaatar et al. 2024), BTS (Zhang et al. 2025) and BTM (Li et al. 2022) are cited and credited. "Traditional MoE" is called "a variant of BTX" proposed here (§3.1: "we propose a variant of BTX called Traditional MoE"), but it is, in substance, the standard Mixtral-style top-k FFN-expert layer built from existing checkpoints. That recipe is the established dense-to-MoE "upcycling" approach, which is not cited `[verify]`. The paper's own §2 notes MergeKit already builds Mixtral-style MoEs. Contribution C2 is therefore "an implementation", not a method.
- **Suggested Fix**: Cite and contrast sparse upcycling (see Missing References). Reword "propose" to "implement", and state the delta over MergeKit's MoE mode precisely.

### W2: The "previously unavailable" claim conflicts with the paper's own related work
§1 says the implementations were "previously unavailable to the open community", but §2 says Mergoo "was the first package to deliver open-source implementations of new MoE-based merging techniques such as BTX". Mergoo and MergeKit cover BTX and Mixtral-style MoE respectively, so at most BTS and wider architecture coverage could be new. Even for BTS, nothing here confirms that the implementation reproduces the BTS paper's behaviour.
- **Suggested Fix**: Add a capability table (method × tool: MergeKit, Mergoo, MixtureKit, architectures actually tested), and report any BTS/BTX reproduction against the original papers.

### W3: Attribution of the BTX design needs checking
The abstract and §3.1/§3.3 describe BTX as "separate routers for each specified sub-layer" (a router for each of gate/up/down). My recollection of Sukhbaatar et al. (2024) is that BTX places one router per MoE (FFN) layer, which is closer to what MixtureKit calls "Traditional". If so, the toolkit's "BTX" differs from the cited method, and the §4 results are for that variant. I cannot check the original text here, so I record it as a question (Q1) and mark it `[verify]`.
- **Suggested Fix**: State exactly which design from the BTX paper each mode implements, and cite the section.

### W4: Several statements about prior work do not match the cited works
§2: "these two models were not released as open-weight models for further experimentation by the community" (Switch Transformer / GLaM). Released Switch Transformer checkpoints exist on public hubs as far as I recall `[verify]`. §2: "Random Forests (Chamma et al., 2023)", where the cited entry is a paper on conditional-permutation variable importance, not on ensemble methods. §2: Mixtral "was the first open-weight model pre-trained from scratch" as a mixture of experts `[verify]` (earlier open MoE checkpoints may exist).
- **Suggested Fix**: Re-check each against the cited abstract, and soften or replace the citations.

**Minor**: "Acree-AI" for Arcee; the Mergoo footnote has no formal citation.

### Literature-check addendum
Search unavailable (arXiv HTTP 429 on two attempts; strict mode, cutoff 2025-09-24). The following is from knowledge and carries `[verify]`.

| Claim | Dimension | Novelty | Closest prior work (from knowledge) | Cited? | Reasoning |
|-------|-----------|---------|--------------------------------------|--------|-----------|
| C1 composer | resource | incremental | MergeKit MoE mode; Mergoo | Yes | Generality via regex patching is the delta; untested beyond Gemma3 |
| C2 methods | method/resource | incremental | BTX, BTS, BTM (all cited); sparse upcycling | BTX/BTS yes; upcycling no `[verify]` | Re-implementation; no new method |
| C3 visualizer | resource | medium–incremental | Routing analyses in Mixtral and OLMoE papers `[verify]` | No | Interactive UI is useful; analysis content is standard |
| C4 result | result | n/a (reproduction) | Shang et al. 2025 (Nile-Chat) | Yes | Reproduction of the authors' or a cited setup, not a new finding |

**Baseline scout:** the only external benchmark family is the Nile-Chat set, with no public leaderboard counterpart. Not applicable. **Field snapshot** (from knowledge, uncertain): by 2025 open MoE LLMs are routinely released directly, and merging/upcycling toolkits are common. A toolkit paper is significant at ICLR only with a demonstrated capability or measured finding, such as a quantified cost or quality benefit of recycling versus training from scratch or dense continual training. Convenience alone is a software contribution.

## Missing References
*No search was possible; every entry is marked `[verify]` and given only to the precision I am confident of.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Komatsuzaki et al., "Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints", ICLR 2023 `[verify]` | Standard dense-to-MoE conversion; the "Traditional MoE" mode is this idea applied to checkpoints |
| Important | Gale et al., "MegaBlocks: Efficient Sparse Training with Mixture-of-Experts", MLSys 2023 `[verify]` | Efficient MoE kernels; relevant to the inference gap admitted in §6 |
| Important | Zoph et al., "ST-MoE: Designing Stable and Transferable Sparse Expert Models", 2022 `[verify]` | Router stability and load-balancing practice behind the α trade-off in §3.1 |
| Important | Muennighoff et al., "OLMoE: Open Mixture-of-Experts Language Models", ICLR 2025 `[verify]` | Open MoE with routing-specialization analysis, relevant to the visualization claim |
| Helpful | Shen et al., "Mixture-of-Experts Meets Instruction Tuning", ICLR 2024 `[verify]` | MoE plus instruction tuning, relevant to the SFT stage in §4 |
| Helpful | Wu et al., "Mixture of LoRA Experts", ICLR 2024 `[verify]` | LoRA-expert composition, related to the plug-in framing of BTS |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 1 | Prior-work statements partly inaccurate; claims untested |
| Clarity | 2 | Clear on mechanics; positioning inconsistent |
| Significance | 2 | Plausibly useful to practitioners |
| Originality | 1 | Implementations of cited methods |

## Dimension Scores (0–100)
**Pool position:** better than about 26% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: no new method or finding, and the overclaimed "previously unavailable" is contradicted by §2.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 42 | Developing | Descriptions are mostly right, but attribution and unchecked claims about prior work |
| Clarity & Presentation | 60 | Competent | Understandable; positioning needs repair |
| Novelty & Originality | 30 | Developing | Engineering of cited ideas |
| Significance & Impact | 46 | Developing | Niche but real |
| Experimental Validation | 32 | Developing | Domain-level comparisons (vs MergeKit/Mergoo) absent |
| Reproducibility | 48 | Developing | Code open-sourced per the abstract; recipe missing |
| Ethical Compliance | 60 | Competent | Basic limitations only |

## Questions for Authors
1. Does the BTX of Sukhbaatar et al. use one router per FFN layer or one per projection? If one per layer, which mode here equals the original, and does the §4 result depend on the difference? A clear answer would resolve W3.
2. What does MixtureKit do that MergeKit's MoE mode plus a short script does not, on the same Gemma3 checkpoints? A side-by-side would raise my Novelty score.
3. Have you verified your BTS against the BTS paper's reported behaviour on any shared setting?

## Limitations Assessment
**Partially.** See R1; additionally the paper does not discuss the overlap with existing upcycling tools.

## Ethics Review Flag
**No.**

## Overall Score
**2**: A competent engineering effort whose contribution as a research paper is the packaging of known methods, with overclaimed availability and unverified prior-work statements.

## Confidence
**4**: Confident about the field; I could not verify my recollection of the BTX router design.

---

# Peer Review Report

## Paper: MixtureKit: A General Framework for Composing, Training, and Visualizing Mixture-of-Experts Models
## Reviewer: Prof. Mateo Brandt-Szabo, Perspective (software-engineering department, public university, Central Europe; fictional persona)
## Expertise: Research-software sustainability; developer tooling; human-centred interpretability tools
## Date: 2026-11-10

## Summary
The paper offers a config-driven toolkit that converts HuggingFace checkpoints into MoE models and lets users inspect routing in an interactive viewer. It frames this as lowering the barrier to MoE research and as a way to recycle existing models. A case study composes script-specialized Egyptian Arabic experts and shows routing for a code-switched sentence.

## Strengths
### S1: Addresses a real user pain
Hand-editing modeling files to add MoE layers is error-prone. A single configuration dictionary (Fig. 2) and a `build_moe(config)` call (§3.1 "User-Centric Configuration") is the right interface idea for non-experts.

### S2: The code-switching use case is a good fit for routing inspection
Fig. 3 shows Arabic-script tokens going to the Arabic expert and Latin-script tokens to the Latin expert. A user can see at a glance that the router is separating scripts, which is an intuitive debugging aid for multilingual systems.

### S3: Honest statement of tool limits
§6 admits dependence on HuggingFace config versions via regex matching and missing vLLM MoE kernels. Maintenance burden is the main risk for such tools, and the authors name it.

### S4: Community value of open release
Releasing the toolkit and a BTS implementation (if verified) would let others study stitch-based composition, which is hard to try otherwise.

## Weaknesses
### W1: Deployment realism: no inference-cost picture
An MoE built by copying FFNs multiplies stored parameters; the paper reports "6B activated parameters" but never the total, memory footprint or latency (§4, Table 1). §6 admits no optimized kernels. A practitioner cannot tell whether a composed model is cheaper to serve than the dense 12B that beats it on Arabic (60.0 vs 55.87, Table 1).
- **Suggested Fix**: Report total parameters, peak memory and tokens/s for dense 4B, dense 12B and the composed models on one GPU. Discuss vLLM/MegaBlocks-style serving paths.

### W2: Fragility of regex-based patching is untested
The tool copies and rewrites `modeling_<base>.py` and `configuration_<base>.py` (§3.2 "Architecture Patching") and "full support for all model families" is claimed (§1). Software-engineering practice would require a compatibility matrix (families × transformers versions) and automated tests. None is shown, so "general" is an aspiration.
- **Suggested Fix**: Publish a tested-architecture table and CI results (e.g., 6–10 families, two library versions). State known failures.

### W3: The visualizer's value is asserted, not studied
§3.3 says the tool "has proven valuable for diagnosing expert under-utilization, detecting routing collapse" with no example of either. Fig. 3 shows one sentence with round-number weights (20/80, 95/5…), which looks illustrative. Averaging softmax weights over layers and projections can hide layer-specific behaviour. The tool covers Traditional and BTX only, not BTS, the method the paper calls "more inherently interpretable".
- **Suggested Fix**: Add at least one real diagnostic case (a collapsed router found and fixed with load balancing), plus a per-layer view. Consider a small user study with MoE practitioners.

### W4: No data, licence or provenance statement
The case study uses web-derived instruction data (Wild-Chat) and Arabic/Arabizi corpora (§4). The paper says nothing about licences, personal data in code-switched social text, or the dialect-community perspective. For a toolkit that "encourages reuse" of third-party checkpoints, licence compatibility between merged experts is a practical concern.
- **Suggested Fix**: Add a short data and licence note and a warning about combining checkpoints with incompatible licences.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Plausible engineering, little verification |
| Clarity | 3 | Easy to follow |
| Significance | 2 | Useful to a niche of practitioners |
| Originality | 1 | Packaging |

## Dimension Scores (0–100)
**Pool position:** better than about 38% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: genuine practical utility and an intuitive interpretability aid, but the tooling claims are not verified and ICLR rarely accepts tool papers on utility alone.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Design is sensible; no tests shown |
| Clarity & Presentation | 62 | Competent | Clear |
| Novelty & Originality | 42 | Developing | New packaging, not new ideas |
| Significance & Impact | 55 | Competent | Practitioner value if broad support holds |
| Experimental Validation | 40 | Developing | Single case study |
| Reproducibility | 58 | Competent | Open release is a plus, details missing |
| Ethical Compliance | 62 | Competent | Limits stated; no data or licence note |

## Questions for Authors
1. Which model families and library versions have you actually run end to end? A table would substantially raise my view of the "general" claim.
2. Can you show one real case where the visualizer diagnosed a routing problem that you then fixed?
3. What is the maintenance plan as HuggingFace modeling files change?

## Limitations Assessment
**Partially.** §6 is honest but short; add memory/serving costs and licence caveats.

## Ethics Review Flag
**No.** (A data/licence note is advisable, not a flag.)

## Overall Score
**3**: Practically motivated and clearly written, but the evidence for generality, cost savings and visualization value is not there yet.

## Confidence
**3**: Fairly confident; I am not a MoE specialist and could not run the code.

---

# Peer Review Report

## Paper: MixtureKit: A General Framework for Composing, Training, and Visualizing Mixture-of-Experts Models
## Reviewer: Dr. Yuki Tanabe-Okafor, Generalist (university NLP/ML group, East Asia; fictional persona)
## Expertise: Language models; multilingual NLP
## Date: 2026-11-10

## Summary
MixtureKit lets users combine existing model checkpoints into a Mixture-of-Experts model through a configuration object, choosing between a standard routed MoE, BTX and the stitch-based BTS. It also includes an interactive tool that shows which expert handles each token. A worked example builds Egyptian Arabic models that handle both Arabic and Latin script and are compared with dense models of 4B and 12B parameters.

## Strengths
### S1: The goal is clear and easy to state
A one-line way to build and train an MoE from available checkpoints is a clear contribution to the community's tooling (§1 contributions).

### S2: Good readability and structure
The paper is short, with a logical flow from motivation to design (§3), visualization (§3.3) and example (§4). The Fig. 2 configuration example makes the interface concrete.

### S3: A relevant and interesting application
Script-specialized experts for Egyptian Arabic/Arabizi (§4) is a natural showcase for token-level routing, and results beat the dense 4B model across the five Table 1 columns.

## Weaknesses
### W1: Venue fit: a library description without a research finding
ICLR reviewers look for a new idea, a measured finding, or a rigorous empirical study. §3 mostly documents API and patching mechanics, and §4 revisits a setup from earlier work ("adopt the experimental setup from (Shang et al., 2025) and try to reproduce the results"). The paper never answers a question such as "when is recycling better than dense continual training or training MoE from scratch?" despite motivating the work with exactly that (§1).
- **Suggested Fix**: Add a controlled study that yields a transferable finding (recycled MoE vs dense continual pretraining vs scratch at matched compute), or submit to a software-oriented venue or track.

### W2: Table 1 is hard to interpret and the text slightly overreads it
The columns (e.g., "Average Arabic") and the benchmarks behind them are not defined. The text says the MoE models "perform comparably on Latin script (52.32 ≈ 52.61)", citing the 2x4B model, while 3x4B scores 51.23 (derived gap −1.38). The abstract's "outperform baseline dense models" omits that the 12B dense model wins Avg Arabic by about 4 points. Bold and underline marks are described but cannot be verified from the extracted text.
- **Suggested Fix**: Define each column and benchmark, report both MoE variants in every sentence, and align the abstract with the table.

### W3: Contribution list mixes product features with claims
Bullets in §1 ("one-line merge function", "regex pattern matching") are features rather than contributions, and "full support for all model families" is not demonstrated. The relation among Traditional MoE, BTX and BTS is explained only verbally, with no summary table of what differs functionally.
- **Suggested Fix**: Add a comparison table (routing granularity, trainable parts, memory, plug-in ability, visualization support) and tone down "all model families".

**Minor**: §1 has a stray "Osborne (2024) Furthermore"; "Acree-AI"; Fig. 2's config sets `stitch_freq` for BTX.

### Venue criteria checklist (ICLR)
| Criterion | Grade | Location |
|-----------|-------|----------|
| Soundness (claims supported) | Partly | Table 1 supports only a narrow claim |
| Contribution (new idea/finding) | Not met | §3.1 methods are cited prior work |
| Presentation | Met (minor issues) | whole paper |
| Reproducibility | Partly | §4 recipe incomplete; code link (removed in blinded copy) |
| Fit to ICLR audience | Partly | Tool value without measured insight |

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 1 | Thin evidence |
| Clarity | 3 | Well written |
| Significance | 2 | Useful tool |
| Originality | 1 | Known methods |

## Dimension Scores (0–100)
**Pool position:** better than about 30% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: no new finding and a single case study; clear writing does not offset it.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 46 | Developing | Sensible but unverified |
| Clarity & Presentation | 62 | Competent | Well organized |
| Novelty & Originality | 36 | Developing | Known methods |
| Significance & Impact | 45 | Developing | Niche |
| Experimental Validation | 34 | Developing | One setting |
| Reproducibility | 50 | Developing | Details missing |
| Ethical Compliance | 60 | Competent | Basic |

## Questions for Authors
1. What would a reader learn from this paper that is not already in the repository README? Name the finding.
2. In what sense did you "successfully reproduce" Shang et al.: do the numbers match, and which are new?
3. Can you show recycled MoE vs dense continual pre-training at equal compute?

## Limitations Assessment
**Partially.**

## Ethics Review Flag
**No.**

## Overall Score
**2**: Clear and useful as a tool description, but below the ICLR bar for contribution and evidence.

## Confidence
**4**: Confident.

---

# Devil's Advocate Report

## Paper: MixtureKit: A General Framework for Composing, Training, and Visualizing Mixture-of-Experts Models
## Reviewer: Dr. Oskar Lindqvist-Amara, independent evaluation-methodology lab (Northern Europe; fictional persona)

---

## Steelman
Existing merging tools hard-code a few model families and omit newer recipes such as BTS. A well-designed, config-driven library that can patch arbitrary HuggingFace architectures and expose routing decisions lowers the barrier for MoE recycling research, and a working Gemma3-based Arabic/Arabizi example shows that the pipeline yields models that beat dense 4B models.

## Core Argument Chain
1. Existing open tools are limited to a few families and lack BTS (§2).
2. MixtureKit supports Traditional MoE, BTX and BTS for "all model families" (§1).
3. It includes a visualizer that diagnoses routing (§3.3).
4. A BTX model built with it outperforms dense baselines and reproduces Shang et al. (§4, Table 1).
5. Hence recycling checkpoints reduces training cost and MixtureKit is "a practical foundation" (Abstract, §5).
∴ MixtureKit is a general, useful framework that advances MoE research.

## Strongest Counter-Argument
Even if every line of the code works, the paper's evidence cannot distinguish "the library is general and useful" from "one earlier pipeline was re-run once". Table 1 is the only experiment, and it is one BTX recipe on one 4B base in one language setting. Premise 2 (three methods, "all model families") is exercised only for BTX on Gemma3; Traditional MoE and BTS are never run, load balancing is never run (Fig. 2 uses `"alpha": 0`), and the visualizer is shown on a single sentence. The "reproduction" in Premise 4 is not checkable: the original numbers are not shown, and the dense Nile-Chat-4B/12B rows are undefined, so whether the MoE gains come from the BTX composition, from the extra parameters (6B active, larger total, against a 4B dense), from the LoRA/DPO recipe, or from data mixing is not identified. The only controlled contrast available, MoE vs dense 4B, is confounded by capacity, and the 12B dense control wins on Arabic by about 4 points (60.0 vs 55.87, derived 4.13). Premise 5's cost claim is not measured at all: no GPU-hours, memory or latency appears anywhere. The conclusion's "strong empirical results" therefore overstates a single, uncontrolled data point. Finally, the novelty premise 1 is internally inconsistent: §2 itself says Mergoo already delivered BTX and MergeKit already builds MoE merges, so "previously unavailable to the open community" can hold at most for BTS, whose implementation is never validated against its source paper. What the authors need to answer: what is the evidence that MixtureKit's BTX/BTS implementations are correct, general and cheaper than the alternatives, as opposed to one successfully executed run?

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim, that a working toolkit exists and produces functional composed models, is not contradicted by anything in the paper. The failures are of narrower, fixable claims.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence (unsupported, not contradicted) | §1 bullet 2, §3.1, §4 | "All model families", BTS, Traditional MoE and load balancing are claimed; only BTX on Gemma3-4B is evaluated | Evaluate each method on a shared setup or narrow the claims |
| DA-M2 | Evidence | §4, Table 1 | "Successfully reproduced" with no original numbers; dense baselines undefined; capacity not matched | Side-by-side with the original, define baselines, add a parameter-matched control |
| DA-M3 | Evidence | Abstract, §5 vs Table 1 | "Strong empirical results" and "outperform baseline dense models": 12B dense wins Avg Arabic by 4.13 and Avg Latin vs 3x4B by 1.38 (derived) | Name the baseline; state the 12B result in the abstract |
| DA-M4 | Scope | §1 bullet 2 vs §2 | "Previously unavailable" contradicted by the paper's own account of Mergoo (BTX) and MergeKit (MoE) | Rephrase to the true delta; add a capability table |
| DA-M5 | Alternative explanation | §4 | The base-model "third expert" is credited with "enhanced English capabilities" without English evaluation; 3x4B is lower than 2x4B on Latin (−1.09, derived) | Add English and general benchmarks, or drop the claim |
| DA-M6 | Protocol | §4 (Table 1) | Protocol sweep: no statement of splits, tuning or checkpoint selection after searching for test/validation/held-out/selected/tuned/checkpoint/best/hyperparameter. This is a question about the protocol, not evidence of test-set selection | State the split and selection rule |
| DA-M7 | Evidence (cost) | §1, §5 | Cost reduction is asserted, not measured | Report GPU-hours and serving cost vs dense and vs scratch MoE |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Scope | §3.3 | The visualizer excludes BTS, the method presented as most interpretable |
| DA-m2 | Consistency (E6) | §1 bullet 3 vs §3.3 | Dominant expert defined by "the most votes across transformer blocks" in §1, but as the arg max of average normalized weight in §3.3. These can differ. |
| DA-m3 | Presentation | §1, §2 | Duplicated citation fragment; "Acree-AI"; Fig. 2 BTX config sets `stitch_freq` |
| DA-m4 | Consistency | §3.3 | The routing equation types the projection input as R^d for gate, up and down. The input to `down_proj` is usually the intermediate-size vector. Possibly notational; a question for the authors. |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| "(53.01 < 55.87 < 60.0)" Avg Arabic | 53.01 / 55.87 / 60.0 | Table 1: dense 4B 53.01, 2x4B 55.87, 12B 60.0 | Yes (but 3x4B is 55.74, and the 12B gap is 4.13) |
| "perform comparably on Latin script (52.32 ≈ 52.61)" | 0.29 gap | 52.61 − 52.32 = 0.29; for 3x4B 52.61 − 51.23 = 1.38 | Yes for 2x4B only |
| "top-2 highest scores across all translation and transliteration" | claim | Long: 61.9, 61.59 top-2. Short: 55.37, 53.71 top-2 (12B 53.53). Translit: 83.97, 83.89 top-2 | Yes, with margins of 0.18 chrF (Short, vs 12B) and 0.08 (3x4B vs 2x4B, Translit), single runs |
| MoE vs dense 4B, all five columns | claim implied | 2x4B gains: +2.86, +3.25, +3.19, +1.70, +3.45 | Yes |

## Ignored Alternative Explanations
- Gains over dense 4B may come from added total capacity or from the SFT/DPO recipe and English data mixing, not from BTX composition.
- Script-specific gains may arise from the two continual-pretraining runs themselves, which a dense model trained on the union may match.
- Small chrF gaps are within plausible run-to-run variation, with no seeds reported.

## Missing Stakeholder Perspectives
Maintainers and downstream users who must keep up with changing HuggingFace modeling code; speakers of Egyptian Arabic whose code-switched text is used, with no data statement.

## Observations (Non-Defects)
- The limitations section (§6) honestly names regex fragility and missing inference kernels.
- The tool surfaces a result that is easy to sanity-check: the Latin expert scores 37.09 on Arabic Long translation, versus 58.81 for the Arabic expert (Table 1).
- BTX/BTS/BTM prior work is cited and credited, so criterion 7 does not apply.

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 38 | Claims go well beyond tested configurations |
| Clarity & Presentation | 56 | Inconsistent definitions, undefined baselines |
| Novelty & Originality | 28 | Prior algorithms; availability claim contradicted |
| Significance & Impact | 38 | Value unquantified |
| Experimental Validation | 24 | One uncontrolled case study |
| Reproducibility | 42 | Missing recipe |
| Ethical Compliance | 56 | No data statement |

**Pool position:** better than about 15% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a single uncontrolled, single-run case study carries all the claims.

## Overall: 2 | Confidence: 4

---

# PHASE 1.5: Literature Check

Mode: strict, cutoff 2025-09-24. **Not completed.** `fingerprint.json` was written, but both `search` attempts (concept queries on toolkit/merging/experts and on upcycling) failed with "arXiv API unreachable (HTTP Error 429)". 0 results kept; the other subcommands (`benchmarks`, `scout`, `coverage`, `similarity`, `novelty`, `verify`) were not run because they need kept results. Fallback per the skill: knowledge-based novelty table and missing references, all `[verify]` (see R2). This is a coverage limitation of the run, not evidence about the paper.

# PHASE 1.6: Report Check

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1–W4 | kept | Specific, locations given, not answered by the paper (no appendix) |
| R1 | Error Log ERR-1..3 | kept | Quotes and cross-references hold on re-check |
| R2 | W1 | kept, rewritten | "Sparse upcycling is the same as Traditional MoE" softened to "in substance the standard upcycling recipe `[verify]`" because it relies on memory |
| R2 | W3 (BTX router granularity) | moved to Questions | Rests on memory of the BTX paper; cannot be checked here |
| R2 | W4 (Switch/GLaM release, Chamma, Mixtral "first") | rewritten | Kept as a prior-work accuracy question with `[verify]`; the Chamma citation mismatch rests on the title of the bibliography entry |
| R3 | W1–W4 | kept | W3 rephrased to say "asserted, not studied" |
| R4 | W1–W3 | kept | Typos moved to Minor |
| DA | M1–M7 | kept | M6 explicitly states it is a protocol question |
| DA | m4 (R^d for down_proj) | kept as Question-level Minor | Possibly notation |
| All | cosmetic items | moved to Minor | Typos and duplicated citation fragment |

Scores unchanged.

---

# PHASE 2: Synthesizer Package (Part A)

**Merged issue list**
| ID | Issue | Sources | Class |
|----|-------|---------|-------|
| I1 | Evidence covers only BTX on one base; BTS, Traditional, load balancing, "all families" untested | R1-W1, R1-W4, R3-W2, R4-W3, DA-M1 | CONSENSUS-4 |
| I2 | "Reproduced" unverifiable; baselines undefined; capacity not matched | R1-W2, R4-W2, DA-M2 | CONSENSUS-3 |
| I3 | Cost reduction and inference cost not measured | R1-W1, R3-W1, DA-M7 | CONSENSUS-3 |
| I4 | "Previously unavailable" contradicted by §2; Traditional MoE is an existing recipe | R1 ERR-1, R2-W1, R2-W2, DA-M4 | CONSENSUS-3 |
| I5 | Abstract/§5 wording vs Table 1 (12B wins Arabic) | R1 ERR-3, R4-W2, DA-M3 | CONSENSUS-3 |
| I6 | Missing protocol/recipe details | R1-W3, DA-M6 | CONSENSUS-2 |
| I7 | Unsupported "enhanced English capabilities" | R1 ERR-2, DA-M5 | CONSENSUS-2 |
| I8 | Visualizer value untested; excludes BTS | R3-W3, DA-m1 | CONSENSUS-2 |
| I9 | Missing upcycling and related references | R2 | SOLO |
| I10 | Prior-work statements possibly inaccurate (Switch/GLaM release, Chamma entry, BTX router granularity) | R2-W3, R2-W4 | SOLO (unverifiable here) |
| I11 | Venue fit (no research finding) | R4-W1 | SOLO |
| I12 | Compatibility matrix and maintainability; licence note | R3-W2, R3-W4 | SOLO |
| I13 | §1 vs §3.3 definition of "dominant expert" | DA-m2 | SOLO |

**DA-CRITICAL:** none. **SPLIT:** none explicit (R3 is more positive on significance, not a disagreement on facts). **Hinge points:** I1 and I2 (whether the evidence supports the claims), I4 (availability claim).
Warnings from the "before" aggregation are reproduced under Score Summary.

---

# PHASE 2: EIC Meta-Review

*(Prof. Lucía Ferreira-Oyelaran. I read the five reports and the package first, then re-read the abstract, contributions, §2, §3.1, §3.3, §4, Table 1, §5–6 and a text search for latency/GPU/seed/ablation/memory/English/split/selection terms.)*

### The Case For and Against
- **For acceptance:** A real, open-source tool addressing a practical need (recycling checkpoints into MoEs across families), with a BTS implementation that may be new, an interpretability viewer, and a working demonstration on a non-Llama base showing consistent gains over the dense 4B baseline. The writing is clear and the limitations section is honest.
- **Against acceptance:** The algorithms are all prior work. The only evidence is one single-run case study of one method (BTX), with undefined baselines and an unverifiable "reproduction". The paper's own related work contradicts its availability claim. The generality, cost, load-balancing and visualization claims are not tested at all. ICLR has no tool track, and the paper does not offer a transferable finding.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Only BTX evaluated; no Traditional, BTS or load-balancing result | R1-W1, DA-M1, R4-W3 | §4, Table 1, Fig. 2 | **Verified** | §4 says "employing the BTX"; Fig. 2 has `"alpha": 0`; no other method result in the text |
| "Previously unavailable" vs Mergoo/BTX | R1 ERR-1, R2-W2, DA-M4 | §1 bullet 2, §2 | **Verified** | Both quotes present as cited |
| 12B beats MoE on Avg Arabic by 4.13; abstract omits it | R1 ERR-3, DA-M3 | Table 1, Abstract | **Verified** | 60.0 − 55.87 = 4.13; 60.0 − 55.74 = 4.26 |
| "Reproduced findings" lacks original numbers | R1-W2, DA-M2 | §4 | **Verified** | Table 1 has no original-paper columns |
| No cost, latency or memory numbers | R1-W1, R3-W1, DA-M7 | whole paper | **Verified** | Text search finds none |
| "Enhanced English capabilities" unsupported | R1 ERR-2, DA-M5 | §4 | **Verified** | The only English mention is Wild-Chat mixing |
| No stated split or checkpoint selection | R1-W3, DA-M6 | §4 | **Verified** (as an omission; no sign of test-set selection) | Not criterion 3 |
| BTX uses a router per projection vs original BTX | R2-W3 | Abstract, §3.1 | **Unverifiable here** | Cannot check the BTX paper; stays a question |
| Switch/GLaM "not released as open-weight" | R2-W4 | §2 | **Unverifiable here** | Needs a source check; at most Minor |
| Chamma et al. cited for Random Forests | R2-W4 | §2, references | **Partly correct** | The entry title concerns variable importance; the in-text claim is generic about ensembles. A weak citation, not a decisive error |
| "Dominant expert" defined two ways | DA-m2 | §1 bullet 3, §3.3 | **Verified** (minor) | "most votes" vs arg max of average weight |
| Visualizer "has proven valuable" with no example | R3-W3 | §3.3 | **Verified** | One illustrative figure |
| R^d input to `down_proj` | DA-m4 | §3.3 equations | **Partly correct** | Possibly notation; not decisive |

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | Decisive points all verified against Table 1 and the text; calibrated to the pool |
| R2 (Domain) | 2 | 4 | 1.0 | The §1-vs-§2 contradiction is verified; the BTX-granularity and release statements rest on memory and are unverified |
| R3 (Perspective) | 3 | 3 | 1.0 | Points valid; somewhat generous on significance, but role-appropriate |
| R4 (Generalist) | 2 | 4 | 1.0 | Sound venue-fit argument and Table 1 reading; typical review |
| DA | 2 | 4 | 1.25 | Counter-argument verified point by point; correctly declined to raise a CRITICAL issue |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| None raised | n/a | n/a | n/a |

**DA ceiling: none.**

### Final Decision and Justification
The starting point is the EIC-weighted rating, 2.15, which rounds to **2** (official mean 2.20). The 0–100 composite (EIC-weighted 43.6; official 44.3) is a cross-check; its band (Reject, 35–49) agrees, so there is no ⚠ disagreement to explain. I decide **Reject (2)**, equal to the starting point. No upheld DA-CRITICAL issue exists, so there is no ceiling. My pool position is **24**: better than about a quarter of ICLR submissions. Deciding evidence: every contribution is either prior work or an engineering feature, and the single case study (one method, one base, no variance, undefined baselines, unverifiable reproduction) cannot test generality, cost or visualization claims. The weaknesses here are of the kind that sink a paper (the main claims are not tested), not the ordinary ones that accepted papers carry. R3's mild positive view, based on practical utility, is outweighed because utility is asserted rather than measured, and the pool position of the panel (15–38) is consistent. No reviewer disagreement of 30 points or more exists on pool position. This is a software contribution that could be strengthened into a good tools or analysis paper with a controlled evaluation. Under the skill's rules this is a simulation of how a careful panel would likely see this draft, not a prediction of any real outcome.

---

## Score Summary
*(From `aggregate_scores.py --venue iclr`. BEFORE = no EIC weights; AFTER = EIC weights R1 1.25, R2 1.0, R3 1.0, R4 1.0, DA 1.25, `--final 2`. Script warnings: none, in either run. No ⚠ spreads: the largest spread is 17, on Significance.)*

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 38 | 42 | 52 | 46 | 38 | 43.2 | 42.4 | 14 |
| Clarity & Presentation | 58 | 60 | 62 | 62 | 56 | 59.6 | 59.3 | 6 |
| Novelty & Originality | 32 | 30 | 42 | 36 | 28 | 33.6 | 33.0 | 14 |
| Significance & Impact | 45 | 46 | 55 | 45 | 38 | 45.8 | 45.1 | 17 |
| Experimental Validation | 28 | 32 | 40 | 34 | 24 | 31.6 | 30.8 | 16 |
| Reproducibility | 45 | 48 | 58 | 50 | 42 | 48.6 | 47.8 | 16 |
| Ethical Compliance | 60 | 60 | 62 | 60 | 56 | 59.6 | 59.4 | 6 |
| **Composite** | 41.7 | 43.8 | 51.8 | 45.8 | 38.2 | **44.3 (before)** | **43.6 (after)** | |

Overall ratings: R1 2, R2 2, R3 3, R4 2, DA 2. Official rating 2.20; EIC-weighted rating 2.15 (2.17 before weights). Each reviewer's Overall matches the band implied by their own composite.

### Target-Venue Scores (ICLR, scale status: secondary)
| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 1 / 2 / 1 |
| Rating | 2 on {0,2,4,6,8,10} (3 on {1,3,5,6,8,10}); ICLR-weighted composite 43.3 |

No Cross-Venue Outlook was requested.

---

# Editorial Decision

## Paper: MixtureKit: A General Framework for Composing, Training, and Visualizing Mixture-of-Experts Models
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: system
## Review Team (fictional personas): EIC Prof. Lucía Ferreira-Oyelaran; R1 Dr. Kwabena Adjei-Marlow; R2 Dr. Priyanka Ranganathan-Holt; R3 Prof. Mateo Brandt-Szabo; R4 Dr. Yuki Tanabe-Okafor; DA Dr. Oskar Lindqvist-Amara

## Decision: Reject (2)  (ICLR rating label: see the Score Summary)

**Official ratings:** R1 2, R2 2, R3 3, R4 2, DA 2 → mean 2.20
**Official composite:** 44.3
**EIC assessment (internal):** weighted rating 2.15 → starting point 2 · weighted composite 43.6 → band 2 (cross-check agrees) · **DA ceiling:** none · **Final (EIC):** 2
**ICLR label (script, scale status: secondary):** 2 on {0,2,4,6,8,10} (3 on {1,3,5,6,8,10}); Soundness 1, Presentation 2, Contribution 1

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "MixtureKit" to ICLR. Making it easy to recycle existing checkpoints into Mixture-of-Experts models is a worthwhile goal, and an open implementation of BTS and an interactive routing viewer could be useful to the community.

**Overall Assessment:** The reviewers found the paper clear and the tool plausibly useful. They agreed that the evidence does not yet support the framework-level claims. The algorithms are previously published, and the only experiment is a single-run case study of BTX on one base model.

**Key Strengths Identified by Reviewers:**
1. A concrete, config-driven pipeline and a first demonstration on a Gemma3 base (R1-S1/S2, R2-S1, R3-S1).
2. A routing viewer well suited to a code-switching use case (R2-S3, R3-S2).
3. Honest limitations and clear writing (R3-S3, R4-S2).

**Key Concerns Requiring Attention:**
1. Claims of generality, three supported methods, load balancing and "all model families" are tested only for BTX on Gemma3 (CONSENSUS-4: R1, R3, R4, DA).
2. "Reproduced the findings" cannot be checked, and the dense baselines are undefined and not capacity-matched (CONSENSUS-3: R1, R4, DA).
3. Cost reduction and inference cost are asserted but not measured (CONSENSUS-3: R1, R3, DA).
4. "Previously unavailable" conflicts with the paper's own Related Work, and "Traditional MoE" is a standard recipe (CONSENSUS-3).

**Critical Challenge (Devil's Advocate):** No CRITICAL issue was raised. The strongest challenge was that one re-run pipeline cannot distinguish "a general, useful library" from "one earlier recipe re-run once", which the authors should answer with controlled, multi-method evidence.

**Decision: Reject (2).** The paper would need a controlled evaluation (all three methods, matched baselines, seeds, cost measurements) and a repositioning of the novelty claims to move to the borderline range. A measured finding on when recycling beats dense continual training would make it a stronger research paper, and a software-oriented venue may also fit.

Please refer to the Revision Roadmap below.

Sincerely,
Prof. Lucía Ferreira-Oyelaran
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Only BTX evaluated; generality/BTS/Traditional/load-balancing untested | R1, R3, R4, DA | CONSENSUS-4 |
| Reproduction unverifiable; baselines undefined | R1, R4, DA | CONSENSUS-3 |
| Cost/latency/memory not measured | R1, R3, DA | CONSENSUS-3 |
| "Previously unavailable"/novelty positioning | R1, R2, DA | CONSENSUS-3 |
| Abstract wording vs Table 1 | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| How much practical significance counts | R3 (Overall 3) | R1, R2, R4, DA (Overall 2) | Utility is plausible but unmeasured; ICLR weighs evidence of contribution. Rating stays 2. |

### Score Spread Discussion
See the Score Summary for ⚠ dimensions. R3's higher Technical Rigor and Experimental Validation reflect a more lenient reading of the same single case study; the EIC adopts the stricter, verified reading (no ablation, no variance, no efficiency numbers).

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Claims exceed the single tested configuration | Yes (R1, R3, R4) | n/a | n/a |
| DA-M2 | MAJOR | Reproduction unverifiable; baselines | Yes (R1, R4) | n/a | n/a |
| DA-M3 | MAJOR | Abstract vs Table 1 | Yes (R1, R4) | n/a | n/a |
| DA-M4 | MAJOR | "Previously unavailable" | Yes (R1, R2) | n/a | n/a |
| DA-M5 | MAJOR | English claim unsupported | Yes (R1) | n/a | n/a |
| DA-M6 | MAJOR | Protocol not stated | Yes (R1) | n/a | n/a |
| DA-M7 | MAJOR | Cost unmeasured | Yes (R1, R3) | n/a | n/a |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*Verified issues that undermine the main claims. No DA-CRITICAL issue was upheld.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | Claims exceed the evidence: only BTX on one base evaluated | R1-W1, R1-W4, R3-W2, R4-W3, DA-M1 | §1, §3.1, §4, Table 1 | Evaluate Traditional, BTX and BTS on a shared setup with 3 seeds, or narrow the claims to what was run; add a tested-architecture table | High; about 100–300 GPU-h | Partly (narrowing claims: yes; new runs: no) |
| P1-2 | Reproduction unverifiable; baselines undefined; capacity not matched | R1-W2, R4-W2, DA-M2 | §4, Table 1 | Add original vs reproduced numbers, define dense 4B/12B recipes, total parameters, and a parameter-matched control | Medium; 20–60 GPU-h | Partly |
| P1-3 | Cost and efficiency unmeasured | R1-W1, R3-W1, DA-M7 | §1, §5 | Report GPU-hours, memory, latency and throughput vs dense and vs scratch MoE | Medium | Yes (measurement on existing checkpoints) |
| P1-4 | "Previously unavailable" and "propose Traditional MoE" contradicted by §2 and standard practice | R1 ERR-1, R2-W1, R2-W2, DA-M4 | §1 bullet 2, §2, §3.1 | Capability table (MergeKit, Mergoo, MixtureKit), cite sparse upcycling, reword | Low | Yes |

### Priority 2: Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Abstract/§5 wording vs Table 1 (12B wins Arabic) | R1 ERR-3, R4-W2, DA-M3 | Name baselines, report both MoE variants in text | Low | Yes |
| S2 | Missing recipe and protocol (LoRA rank/targets, router trainable, α, data, split, checkpoint rule, compute, seeds) | R1-W3, DA-M6 | Appendix with full recipe | Low | Yes |
| S3 | "Enhanced English capabilities" unsupported | R1 ERR-2, DA-M5 | English benchmark or remove | Low–Medium | Partly |
| S4 | Component ablations (per-projection vs per-block routing, router-only vs full tuning) | R1-W4 | Run or remove the claims | Medium | Partly |
| S5 | Visualizer value untested; excludes BTS; per-layer view | R3-W3, DA-m1 | One real diagnostic case; extend to BTS or state the limit | Medium | Partly |
| S6 | Critical/Important missing references (all `[verify]`): sparse upcycling; MegaBlocks; ST-MoE; OLMoE | R2 | Cite and discuss | Low | Yes |
| S7 | Clarify BTX router design vs the original paper | R2-W3 | State which design each mode implements | Low | Yes |

### Priority 3: Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Prior-work statements (Switch/GLaM release, Random Forests citation, Mixtral "first") | R2-W4 | Re-check against sources `[verify]` |
| N2 | Data and licence note; licence compatibility of merged checkpoints | R3-W4 | Short note |
| N3 | Venue fit; consider a software-oriented venue or a controlled study | R4-W1 | Add "recycled MoE vs dense continual vs scratch" study |
| N4 | §1 vs §3.3 "dominant expert" definition; R^d input type for `down_proj` | DA-m2, DA-m4 | Align text and equations |
| N5 | Typos: "Acree-AI", duplicated Osborne citation, `stitch_freq` in BTX config | R1, R4 | Fix |
| N6 | Helpful references: Mixture-of-Experts Meets Instruction Tuning; Mixture of LoRA Experts (`[verify]`) | R2 | Optional |

## Estimated Revision Effort
- Priority 1: 4 items, about 2–4 weeks including new runs (about 150–400 GPU-hours).
- Priority 2: 7 items, about 1 week.
- Priority 3: 6 items, about 1–2 days.
- **Total estimated revision time**: about 3–5 weeks.
