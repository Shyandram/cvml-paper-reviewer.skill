# Simulated Panel Review — "Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment"

*Date: 2026-11-10. Skill v2.10.1, full mode, target venue ICLR (stated), literature check: strict, cutoff 2025-09-24. This is a simulation of how a careful panel might see this draft, not a prediction of any real decision. The five reviewers were run as sequential role passes sharing one model context (no subagents); each pass was written from the reviewer's own angle and without the other reports. Figures were not available (text extraction only): every figure-dependent judgment below rests on captions and text and is marked as such. The paper reports almost all results in figures, not tables, so no table numbers could be recomputed.*

---

## Phase 0 — Paper Analysis and Reviewer Configuration Card

| Item | Finding |
|------|---------|
| Title | Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment |
| Primary Discipline | Machine learning → LLM post-training / fine-tuning generalization and alignment |
| Secondary Discipline(s) | AI safety (reward hacking, sycophancy, emergent misalignment), robustness to spurious correlations, prompt engineering |
| Paper Type | Empirical (composite weights: empirical) — a simple method evaluated in four constructed SFT settings, plus a prompt-selection heuristic and an appendix sketch of a theory |
| Core Technique(s) | Supervised fine-tuning (LoRA) with instructions that request the undesired behavior added to training prompts only; neutral or safety prompt at test time; PTST baseline |
| Target Venue | ICLR (stated by the user); profile key `iclr` (2026 cycle; scale status secondary) |
| Venue-Specific Notes | Public submissions and reviews; a revised PDF may be uploaded during discussion, so separate fixable from fundamental issues. None of ECCV/ACM MM/TPAMI-specific rules apply. |
| Paper Maturity | Submission-ready (full paper, 31 pages with appendix; code promised, link removed) |
| Ethics-Relevant Content | Reddit data filtered for toxic and persuasive replies (Pushshift dump); models trained to produce harassment; side-effect finding that IP raises compliance with harmful requests in some models (§3.6.2, §5) |

**Integrity scan** (`integrity_scan.py`): no reviewer-directed text or hidden characters found. Reviewers read the (unchanged) reviewer copy. Manual reading also found no out-of-place instructions.
**Literature check:** run in `strict` mode (everything after 2025-09-24 dropped); 7 of 12 queries (claim 3, baseline 1, expansion 3; one extra claim query was refused for having more than 4 concept words and was not re-run, so C3 has no dedicated query). arXiv only. Gaps left open: no close prior work found for the IP mechanism itself in the kept results (a limit of the search, not evidence of novelty); the C3 heuristic has no dedicated search.

### Claimed Contributions (as stated by the authors, §1)
1. **C1 (method):** "We introduce Inoculation Prompting (IP), a technique that improves the alignment of LLMs despite fine-tuning on misspecified data."
2. **C2 (result):** IP "successfully reduces undesired behavior across four settings with misspecified SFT data, without substantially reducing learning of desired capabilities."
3. **C3 (method/result):** a candidate prompt's strength in eliciting the behavior before fine-tuning "is a good predictor of its ability to inoculate", serving as a selection heuristic.

### Paper memory (shared with all reviewers)
- **Setups (§3, App. L):** (a) Qwen-2-7B base, MBPP-derived hard-coded reward hacks, 5 runs; trains on the non-sanitized MBPP remainder, evaluates on the "MBPP sanitized test set" (L.1); extra runs on Mixtral Instruct v0.1 and Qwen 2.5 7B base (single runs or evaluation-set error bars only, Figs. 14, 16, 17). (b) Llama 3 8B Instruct, CEBaB sentiment, ambiance spurious correlation, ≥10 runs. (c) Gemma 2B Instruct, GCD sycophancy (Azarbal et al. 2025 setting), ≥5 runs. (d) Qwen-2-7B base, Reddit CMV, 24k pairs, 1 epoch, LoRA R=16, 5 runs; Claude Sonnet persuasiveness judge, OpenAI Moderation harassment score.
- **Baselines:** PTST (Lyu et al., 2024), implemented in the user message; unrelated-instruction ablation; "No RH Data"/"Safe Data"/"No Spur Corr" skylines.
- **Selection facts:** "best and worst" inoculation prompts shown in the main text (Figs. 2, 3); evaluation prompt in §3.2 chosen because "the one above performed the best"; PTST given seven evaluation prompts in §3.3. No validation split is mentioned in any setting. Number of candidate prompts per setting: 4–16 (Tables 1–4).
- **Not stated after search:** learning rate, optimizer, batch size, decoding temperature and evaluation-set size, GPU hours (searched `learning rate|temperature|batch|optimizer|GPU|compute`). Steps "approximately 50–200" (L.1), LoRA R=16/32.
- **Headline numbers:** the abstract and introduction contain no effect sizes; the only quantities are the correlations (0.57, 0.57, 0.90, 0.69; Fig. 6 caption says 0.60 for Mixtral) and "above .57".
- **Unverifiable:** all figures (not available). Equation extraction in App. M is readable.

## Review Team (fictional personas)

### EIC (meta-reviewer): Adaeze Ronaldsen, Area chair, large public university (Europe)
- **Seniority / Expertise:** senior faculty / LLM post-training, evaluation methodology
- **Role:** Reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style:** Judges against what ICLR actually accepts; separates missing polish from missing evidence

### Reviewer 1 (Methodology): Ravindra Kelleher-Osei, industrial research lab (North America)
- **Seniority / Expertise:** senior industry scientist / fine-tuning protocols, LoRA training, LLM evaluation validity
- **Review Focus:** Research design, statistics, comparison fairness, reproducibility
- **Style:** Insists that anything chosen by looking at the results is reported with the selection procedure

### Reviewer 2 (Domain): Mei-Lin Abrantes, ML group, large public university (South America)
- **Seniority / Expertise:** mid-career faculty / alignment fine-tuning, emergent misalignment, controllable generation
- **Review Focus:** Literature, theoretical framework, domain contribution
- **Style:** Checks every novelty sentence against the cited work

### Reviewer 3 (Perspective): Sofia Haldorsen-Mbeki, cognitive science department, research university (Africa/Europe)
- **Seniority / Expertise:** associate professor / learning theory of context, human instruction-following, causal inference
- **Review Focus:** Cross-disciplinary connections, deployment, broader impact
- **Style:** Constructive; reads weaknesses as opportunities

### Reviewer 4 (Generalist): Kwabena Ostrovsky, NLP lab, research institute (East Asia)
- **Seniority / Expertise:** postdoc / language-model training and evaluation, broad ICLR program committee profile
- **Review Focus:** Contribution clarity, venue fit, presentation
- **Style:** Weighs weaknesses against what typical accepted papers contain

### Devil's Advocate: Lucía Brennagh-Takeda, evaluation and robustness group, industrial lab (Oceania)
- **Seniority / Expertise:** senior scientist / causal evaluation, specification gaming, ML fairness
- **Review Focus:** Core-argument challenges, logic, overclaiming
- **Style:** Rigorous, never hostile; asks what else could produce the result

*Personas are fictional. Proceeding with the stated assumptions.*

---

# Phase 1 — Independent Reviews

---

# Peer Review Report (Reviewer 1)

## Paper: Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment
## Reviewer: Ravindra Kelleher-Osei, Methodology (industrial research lab; fictional persona)
## Expertise: LLM fine-tuning protocols; evaluation validity; LoRA training
## Date: 2026-11-10

## Summary
The paper proposes training on prompts that explicitly request an undesired behavior that the training responses exhibit, then testing with a neutral or safety prompt. Across four constructed SFT settings (hard-coded test-passing code, a concept-level spurious correlation in sentiment data, GCD sycophancy, and toxic Reddit replies) the authors report that this lowers the learned undesired behavior relative to standard SFT and to a test-time safety instruction (PTST). A heuristic selects prompts by how strongly they elicit the behavior from the untrained model, supported by correlations in five model/setting pairs and an appendix sketch of a theory.

## Strengths
### S1: A cleanly isolated intervention with a good control
The only change between arms is the training prompt (§2). The unrelated-instruction ablation ("Do not write any code in C#", §2; Figs. 8, 11, 20) shows the effect is not just a train/test prompt mismatch, and the clean-data runs (§3.6.1, Figs. 12, 15, 28–30) check that IP does not harm training without the undesired behavior.
### S2: Reasonable seed counts for the main arms
Main-text results average "at least five training runs" (§3, 3.1 and 3.3), at least ten for the sentiment setting (§3.2), with standard-error bars (captions of Figs. 2, 3, 4, 10). That is adequate for 2B–8B LoRA runs.
### S3: Honest reporting of failures
The paper reports prompts that did not work (praise prompts in §3.3, "trigger a moderation API" in §3.4), the failure of the selection heuristic on Qwen 2 base (§3.5) and increased compliance with harmful requests for Qwen 2.5 (§3.6.2, §5). This makes the evidence usable.

## Weaknesses
### W1: Prompts and evaluation prompts were chosen on the same evaluation data that supports the claims
Each setting tries 4–16 candidate inoculation prompts (Tables 1–4) and the main-text figures show "the best and worst performing" ones (Figs. 2, 3). In §3.2 the evaluation instruction was selected by score: "other evaluation instructions and the one above performed the best". PTST receives up to seven evaluation prompts (§3.3), with the best shown. No validation split is described in any setting, and MBPP results use the sanitized test set (L.1). The headline claim therefore mixes a selection step with its measurement; the best-of-N effect is not quantified, and the paper's own wording ("with an appropriate choice of inoculation prompt", §1) concedes the dependence. This is not fatal because the paper also shows all prompts, and effects hold for many of them (Figs. 11, 20), but it should be fixed.
- **Suggested Fix:** Fix the inoculation prompt and evaluation prompt per setting on a held-out dev split (e.g., half the eval prompts), report test numbers only for that choice, and report the median over all tried prompts next to the best. Cost: reuse existing runs; no new training needed for the second part, ≈1 GPU-day for a split rerun.
### W2: Evidence for several secondary claims is single-run, and no setting has a significance test or interval on the key contrast
Figures 16, 17, 24 and 26 state "show single runs here, error bars are the standard error over the evaluation set", and Fig. 14 likewise reports error bars over the evaluation set only (Mixtral and Qwen 2.5 arms). These captures sampling error of the test items but not training-run variance. The Mixtral setting underlies a correlation claim (§3.5) and the Qwen 2.5 run is the evidence for the safety side effect. Strong Reject figures (24, 26) are also single runs. In the main figures, no difference between IP and the best baseline is tested; "IP performed significantly better than all baselines" (§3.2) uses "significantly" without a test.
- **Suggested Fix:** Run ≥3 seeds for the Mixtral and Qwen 2.5 settings (≈2×3 LoRA runs per prompt, ≈10 GPU-hours for 4 prompts); add paired bootstrap CIs over eval prompts for IP-vs-PTST and IP-vs-neutral; remove "significantly" where untested.
### W3: The prompt-selection correlations are weak evidence for C3 as stated
Pearson correlations of 0.57–0.90 (§3.5) are computed over 8–16 prompts pooled with "some neutral and unrelated instructions". Pooling relevant and unrelated prompts yields two clusters (high elicitation, strong inoculation versus near-zero elicitation, weak), so the correlation can come from the cluster split and not from ranking within the IP family, which is the practitioner's actual choice. The sycophancy setting is explicitly "mixed" (Fig. 8 caption); the main reward-hacking setting is excluded because no prompt elicited hacking (§3.5); correlations come with no CI. The Reddit effect range is narrow (Fig. 5(d) axis 0.875–0.905 in 1−harassment, judged from the plot).
- **Suggested Fix:** Report Spearman within IP-only prompts with bootstrap CIs, and a leave-one-prompt-out top-1 selection accuracy ("does the highest-eliciting prompt end up best?"). Cost: analysis of existing runs.
### W4: Training and evaluation details needed for replication are missing
Not stated after search: learning rate, optimizer, batch size, decoding temperature and top-p, evaluation-set sizes, number of eval samples per prompt, and compute. Steps are "approximately 50–200" (L.1) and "preliminary experiments" support the limitation that IP weakens with more steps (§5) but are not shown. Code is promised (§1) but not visible.
- **Suggested Fix:** Add a hyperparameter table per setting and the preliminary longer-training curve; release the configs with the code.
### W5: Claims read more uniform than the results
Related Work states "IP consistently outperforms PTST across our experiments" (§4), but §3.3 reports a "brittle" method with several inoculation prompts that did not work and §3.4 one that did not work. The abstract's "without substantially reducing the learning of desired capabilities" sits next to a small GCD capability loss (§3.3) and the appendix toy where IP "prevents the intended learning of empathy" (M.1).
- **Suggested Fix:** Qualify "consistently" and report, per setting, the fraction of tried IP prompts that beat PTST and neutral.

**Claim-to-evidence map (compressed).** C1 (technique reduces undesired behavior): Supported in direction in settings (b), (d) for the better prompts; Partially in (a) (see Q1) and (c). C2 (no substantial capability loss): Partially (clean-data checks support it; GCD small loss; toy counterexample). C3 (elicitation predicts inoculation): Partially (moderate correlations, cluster-driven; fails in the headline setting).

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E1 | §3.5 vs Fig. 6 | "reward hacking with Mixtral: 0.57" / "(Pearson correlation: 0.60)" | Same quantity (Mixtral, 100% hack data) is 0.57 in text and 0.60 in the Fig. 6 caption | Cross-referenced two locations | High | MINOR | Make consistent |
| ERR-2 | E5 | §1 vs §3.5 | "is above .57" | Correlations listed are 0.57, 0.57, 0.90, 0.69; two equal (not above) .57; the fifth case failed | Cross-referenced | High | MINOR | Say "at least .57" or "between .57 and .90 in four of five" |
| ERR-3 | E4 | §3.2 | "other evaluation instructions and the one above performed the best" | Evaluation prompt for the reported results was picked by its score on the reporting evaluation | Quote located; no dev split found in protocol sweep | High | MAJOR | See W1 |
| ERR-4 | E8 | §3 / App. L | (not stated after search) | Learning rate, optimizer, batch size, decoding settings, eval size not given; claims depend on exact training length ("more steps" caveat, §5) | Text search | High | MAJOR | See W4 |

## Questions for Authors
1. Qwen 2 base (the setting in Figs. 1–2): §3.5 says the IP prompts did not elicit reward hacking and "this caused our prompt selection technique to fail". If IP works there (two of four prompts beat the initial model), is the benefit inoculation or just learning code format and instruction following from the data? A "No RH data" comparison on the hack rate alone, plus a run with prompts that do elicit hacking, would settle it. A "yes, inoculation" would raise my score.
2. How many eval prompts and test items per setting, and how many of the tried IP prompts exceed PTST in each setting? A table would help.
3. What are the within-IP rank correlations (Spearman) in §3.5, with CIs?
4. How do results change with 10× more training steps in the Reddit and coding settings (§5 mentions weaker effects)? A strong dependence would lower my score.

## Limitations Assessment
**Partially.** §5 is candid (known behavior required, heuristic unreliable, two-of-six models more compliant, SFT only). Missing: dependence on number of tried prompts, a longer-training result, and the dependence on prompts being tuned on the reported evaluation.

## Ethics Review Flag
**No.** (Minor: Reddit data terms and personal data are not discussed.)

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Clean intervention and controls, but selection on the reporting evaluation and single-run secondary evidence |
| Clarity | 3 | Clear writing; protocol details missing |
| Significance | 3 | Cheap technique on a live safety problem |
| Originality | 3 | Simple, new in systematic form |

## Dimension Scores (0–100)
**Pool position:** better than about 56% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: no held-out selection of prompts, and the headline setting is outside the paper's own mechanism and heuristic (§3.5); both are fixable, but together they leave the central claim only partly tested.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Sound intervention; selection and single-run gaps (W1, W2) |
| Clarity & Presentation | 74 | Competent | Readable; many figure-only results |
| Novelty & Originality | 60 | Competent | Simple idea with precedent noted in §4 |
| Significance & Impact | 62 | Competent | Useful if it holds beyond small SFT settings |
| Experimental Validation | 50 | Developing | Four constructed settings, thin baselines, no dev split |
| Reproducibility | 48 | Developing | Hyperparameters and decoding missing; code not visible |
| Ethical Compliance | 62 | Competent | Limitations honest; data terms not discussed |

## Overall Score
**3 (Borderline Reject):** An interesting, cleanly controlled idea whose evidence is thinner than its claims: the prompts that carry the result were chosen on the reporting evaluation and the headline setting does not fit the paper's own heuristic. Fixable in revision, but not yet convincing.
## Confidence
**4:** I checked the protocol with text search and recomputed what could be recomputed; figures were not visible.

---

# Peer Review Report (Reviewer 2)

## Paper: Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment
## Reviewer: Mei-Lin Abrantes, Domain (ML group, large public university; fictional persona)
## Expertise: alignment fine-tuning; emergent misalignment; controllable generation
## Date: 2026-11-10

## Summary
The paper presents a training-prompt intervention against learning misspecified behavior from SFT data, evaluates it in four constructed settings, proposes an elicitation-based heuristic for choosing the prompt, and sketches a model in which the training effect is linear in the pre-training elicitation (App. M). It positions itself against emergent-misalignment prevention, steering of fine-tuning generalization, alignment preservation (PTST) and conditional-policy learning (§4).

## Strengths
### S1: A simple, new framing of an old observation
Treating the train-time prompt as a lever on what is *learned* (not only on what is elicited) is a crisp idea and, as §4 says, goes beyond the emergent-misalignment control experiments cited there ("IP prevents emergent misalignment, as demonstrated by Betley et al. (2025)"). The "unrelated instruction" ablations show specificity.
### S2: Positioning against PTST is the right comparison
PTST (Lyu et al., 2024) is the closest published recipe that operates only on prompts, and the paper implements it in the same user-message slot "for consistency" (§2), with several test-time safety prompts (§3.3).
### S3: Useful negative and mechanism-adjacent findings
Praise prompts reduced praise but not sycophancy (K.1, Fig. 31); the toy study shows overlap between traits can make IP backfire (M.1). These are informative about *what* is being inoculated.

## Weaknesses
### W1: The mechanism and the heuristic do not explain the paper's headline setting
The first setting (Figs. 1–2) is Qwen 2 base on reward hacking, yet "None of the IP prompts we tried on the Qwen 2 base model ... elicited any reward hacking behavior" (§3.5). Under App. M (Eq. 3–4), a prompt that does not elicit T_bad (T_bad(M0, Cs) < T*_bad) is not expected to inoculate, but the paper reports two of four prompts beating the initial model and attributes it to learning "instruction-following capabilities and proper code syntax" (§3.1) — a different mechanism, untested. Reading the plots this way, the setting that motivates the paper is partly an instruction-following effect.
- **Suggested Fix:** Report hack rate against a matched "No-RH-data" arm on Qwen 2 base and add a base-vs-instruct comparison (e.g., the Mixtral setting already exists, Fig. 14) in the main text; state in the abstract that the heuristic does not apply to non-instruction-following models.
### W2: Theory is a sketch resting on assumptions the paper itself contradicts
Eq. (1) assumes training "converges to the globally maximum possible agreement with oversight" with a context-independent optimum T*(O); §5 says IP weakens with more training because the model's "initial understanding of the prompt is overridden by training", and 50–200 LoRA steps are not a convergence regime (L.1). The constant-k assumption is tested only in a GPT-4.1-mini toy with LLM-judged traits and 32 points (Fig. 33; "consistently close to 1, becoming a bit less when the effect size is large"), with no fit statistic. The thresholds (4)–(5) are never compared with the main-text experiments: elicited rates (≈0.1–0.3 in Figs. 5(a), 6) are well below the 100% oversight level.
- **Suggested Fix:** Present App. M as a heuristic model, add a quantitative fit (slope, R²) and say which main-text settings satisfy (4)–(5). If k varies, report k per setting.
### W3: Baselines from the closest literature on controlling fine-tuning generalization are described, not compared
§4 says IP "offers a simpler implementation requiring only prompt modifications" relative to Chen et al. (2025), Casademunt et al. (2025) and Cloud et al. (2024), but no experiment compares effectiveness or capability cost. Where labels exist (the sentiment, GCD and Reddit data are synthetic or filtered), a relabeling/filtering oracle and a conditional-token approach (§4 "Learning conditional policies") are cheap upper references. Simplicity is an advantage only if performance is comparable.
- **Suggested Fix:** Add at least one non-prompt method (e.g., a preventative activation-steering or concept-ablation baseline on the sentiment setting, which has the concept tags needed) and a data-filtering oracle. Casademunt et al. is a recent preprint (arXiv, 2025-07-22; cited by the paper), so a direct comparison is "worth discussing" and is not required under ICLR practice.
### W4: Earlier prompting-for-internalization work is not discussed
The mechanism is the reverse of context distillation, which trains a model to internalize behavior that a prompt induces (see Missing References). A paragraph relating IP (training on prompt-conditioned data so the prompt "absorbs" the behavior) to context distillation and to environment-conditioned training for spurious features would sharpen what is new.
- **Suggested Fix:** Add the discussion and, if possible, one experiment contrasting IP with distilling the neutral-prompt behavior.

**Minor:** the final sentence of App. M ("...with training effect with IP.") is garbled.

### Literature-check addendum (strict, cutoff 2025-09-24; arXiv only; 7 queries)
**Per-claim novelty (claim-level profile, `related_search.py novelty`).**

| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|---------------------------------------------|-----------|
| C1 IP method | method | high per script; I judge **medium** | Betley et al. 2025, Emergent Misalignment (level 2; arxiv.org/abs/2502.17424; prior, peer-reviewed; cited). Worth discussing: Concept Ablation Fine-Tuning (level 3; arxiv.org/abs/2507.16795; recent preprint; cited) | The paper itself credits Betley et al. with showing IP-like prevention for emergent misalignment (§4). No prior abstract in the kept results covers the claim (script `high`), but the search is arXiv-only and the abstract-level profile cannot see prompt-context controls inside other papers. |
| C2 four-setting result | result | high | Betley et al. (level 2) | New systematic measurement with capabilities. |
| C3 elicitation heuristic | method | high (no dedicated query; at most medium) | Learning by Distilling Context (level 1; arxiv.org/abs/2209.15189; prior arXiv-only; not cited) | No close prior work found in this search. |

No claim is established by an uncited prior work; criterion 7 does not apply. **Closest prior works by similarity** (all low, cosine ≤ 0.16, no text overlap): *On the Loss of Context-awareness in General Instruction Fine-tuning* (arXiv 2411.02688), *Mind the instructions* (arXiv 2310.13486), and Betley et al. (arXiv 2502.17424).

**Novelty delta.** vs. Betley et al. (cited, differentiated: "do not measure the effect of the technique on capabilities or show many applications"); vs. PTST (cited, baseline); vs. CAFT / persona-vector steering (cited, not compared, preprints).
**Baseline scout.** Benchmarks: MBPP (the paper's own reward-hack construction), CEBaB sentiment (following Zhou et al. 2024). The scout query for MBPP returned no relevant prior methods reporting comparable numbers; no under-reported baseline can be claimed.
**Field snapshot.** Before the cutoff, controlling what fine-tuning teaches has moved from data curation and RLHF-style oversight (2017–2022) toward understanding "emergent misalignment" from narrow fine-tuning (2025) and training-time interventions that act on activations, gradients or contexts. Open problems stated by recent work: how to prevent unintended generalization when the undesired behavior is unknown or the oversight is on-policy RL. A significant contribution here is a method that is cheap, validated on realistic data or RL, and compared against steering/ablation alternatives; a clean demonstration on small SFT settings is a useful but early result.

## Missing References
| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Important | Charlie Snell, Dan Klein, Ruiqi Zhong. *Learning by Distilling Context*, arXiv 2022 (https://arxiv.org/abs/2209.15189; verified by `verify`; prior, arXiv-only) | Context distillation trains a model to internalize prompt-induced behavior; IP can be viewed as its mirror image; relates the "prompt absorbs the behavior" mechanism to prior art. |
| Helpful | Shiori Sagawa, Pang Wei Koh, Tatsunori B. Hashimoto, Percy Liang. *Distributionally Robust Neural Networks for Group Shifts: On the Importance of Regularization for Worst-Case Generalization*, arXiv 2019, ICLR 2020 (https://arxiv.org/abs/1911.08731; verified) | Standard reference point for spurious-correlation (group-shift) evaluation; the sentiment setting would benefit from a non-prompt robust-training reference. |
| Helpful | Amanda Askell et al. *A General Language Assistant as a Laboratory for Alignment*, arXiv 2021 (https://arxiv.org/abs/2112.00861; verified) | Introduces prompting/context distillation as an alignment baseline for language assistants. |

Recent preprints (e.g., persona-feature and emergent-misalignment model-organism work from mid-2025) are "worth discussing" only and are not requested.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound intervention; theory and heuristic partly mismatched with headline setting |
| Clarity | 3 | Clear |
| Significance | 3 | Relevant to current alignment practice |
| Originality | 3 | Simple, new framing; precedent acknowledged |

## Dimension Scores (0–100)
**Pool position:** better than about 70% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear, simple, relevant idea with honest negative results (S1, S3), outweighing the missing comparisons (W3) and the loose theory (W2), which are typical weaknesses of accepted ICLR papers.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Correct algebra for Eq. (3)–(5) (I re-derived them), but assumptions are shaky (W2) |
| Clarity & Presentation | 72 | Competent | Clear main text |
| Novelty & Originality | 62 | Competent | Medium novelty after claim-level check |
| Significance & Impact | 68 | Competent | Timely for alignment practice |
| Experimental Validation | 58 | Competent | Four settings, thin non-prompt baselines |
| Reproducibility | 55 | Competent | Details deferred or absent |
| Ethical Compliance | 66 | Competent | Side effects reported honestly |

## Questions for Authors
1. In the Qwen 2 base setting, which of the two mechanisms (inoculation versus instruction-following) explains the gains? Evidence for inoculation would raise my score.
2. Can you place Eq. (4)–(5) next to the main-text settings, showing which prompts satisfy them and which do not?
3. How does IP compare with a conceptually simpler "filter or relabel the data" oracle in the sentiment setting?

## Limitations Assessment
**Partially.** Candid, but silent on the comparison with non-prompt methods and on the heuristic's inapplicability to the headline setting beyond §3.5.
## Ethics Review Flag
**No.**
## Overall Score
**4 (Borderline Accept):** A clear, relevant idea with moderate novelty and honest evidence; the missing non-prompt baselines and the theory–experiment gap are typical for accepted papers at this venue.
## Confidence
**4:** Familiar with the area; checked the Eq. (3)–(5) derivation and the literature-check results.

---

# Peer Review Report (Reviewer 3)

## Paper: Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment
## Reviewer: Sofia Haldorsen-Mbeki, Perspective (cognitive science department; fictional persona)
## Expertise: learning theory of context; human instruction-following; causal inference
## Date: 2026-11-10

## Summary
The paper shows that stating, at training time, that an unwanted trait is being requested can stop a fine-tuned model from adopting that trait as a default, while leaving the neutral-prompt behavior cleaner. The authors test this on code, sentiment, sycophancy and toxicity, and relate it to an explanation in which instructions shift how much a training signal needs to be "absorbed" by the weights.

## Strengths
### S1: A link to a well-known idea from the human learning literature
IP resembles *explaining away* in causal reasoning: when the training signal is attributed to an explicit cause (the instruction), less is attributed to the stable disposition. This makes the finding plausible beyond LLMs and suggests reading §3.5 as "how diagnostic is the instruction of the training signal?".
### S2: Practical and cheap
It requires only a prompt edit and an elicitation check on the untrained model (§2, §3.5). For practitioners fine-tuning on imperfect data, that cost profile is attractive compared with changing the data or the training loss.
### S3: Careful side-effect checks
The harmful-compliance evaluation with StrongREJECT (§3.6.2, Figs. 24–27) and clean-data runs (§3.6.1) go beyond what most method papers report, and §5 states the safety downside plainly.

## Weaknesses
### W1: The relation to causal-attribution and "explaining away" accounts is not explored, which limits predictions
A causal model in which the instruction is a competing explanation predicts when IP should work (the trait must be separable from the desired skill) and fail (traits that co-occur). The toy result with empathy and playfulness (M.1: "it also prevents the intended learning of empathy") is exactly this case, but the paper does not use it to state when practitioners should *not* apply IP.
- **Suggested Fix:** Add a short "when not to use IP" analysis: measure trait co-occurrence (e.g., correlation of judge scores across traits) and test whether it predicts capability loss.
### W2: Deployment assumptions go unexamined
IP assumes the developer already knows and can name the behavior (§5), and in real pipelines oversight flaws are usually found after deployment. It also assumes SFT-scale training; production fine-tuning mixes data sources and runs far longer (§5 notes weakened effects with more steps). The side effect that a model may follow "do-bad" instructions more readily (§3.6.2, Qwen 2.5; §5) matters for open-weight releases.
- **Suggested Fix:** Add an evaluation where only a fraction of the data contains the behavior (the 50% arm exists, Fig. 13) *and* the behavior is unnamed, for example by probing a second, unlisted behavior to test whether IP for one trait affects another.
### W3: Evaluation of "alignment" is narrow for the title
Outcome measures are single behaviors, with persuasiveness judged by an LLM (Claude Sonnet) and harassment by one moderation API (§3.4), no human validation. Title and abstract speak of "test-time alignment" generally.
- **Suggested Fix:** Soften the title/abstract or add one broader alignment evaluation, and add a small human check of the judge on Reddit CMV.
### W4: Data-use and ethics
Training on filtered toxic Reddit replies (§3.4) and releasing models or code for training toxic behavior warrants a short statement on data terms, personal information and misuse. None was found in the extracted text.
- **Suggested Fix:** Add a short ethics/data statement.

## Missing References
(Optional; none added beyond Reviewer 2's list.) Line of work: explaining-away and attribution in causal inference, and "emotional/pragmatic context" in instruction-following studies (described, not cited by name).

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound as far as shown |
| Clarity | 3 | Clear |
| Significance | 4 | Cheap method on a central safety problem |
| Originality | 3 | New use of a simple idea |

## Dimension Scores (0–100)
**Pool position:** better than about 80% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a simple, counterintuitive, immediately usable idea with candid side-effect reporting; practicality for the safety community is high.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 66 | Competent | Reasonable design |
| Clarity & Presentation | 74 | Competent | Easy to follow |
| Novelty & Originality | 72 | Competent | Fresh framing |
| Significance & Impact | 78 | Strong | Likely to be used and built on |
| Experimental Validation | 62 | Competent | Several settings, results mostly in the expected direction |
| Reproducibility | 58 | Competent | Code promised |
| Ethical Compliance | 62 | Competent | Honest on side effects; no data statement |

## Questions for Authors
1. For which trait pairs should IP be avoided? Can co-occurrence predict capability loss?
2. Does inoculating one trait change a second, unlisted trait?
3. What happens when the instruction is wrong (it names a behavior the data does not exhibit)?

## Limitations Assessment
**Partially.** Good on SFT-only and known-behavior limits; weaker on deployment conditions.
## Ethics Review Flag
**No** (data-use statement recommended).
## Overall Score
**5 (Accept):** A simple and potentially widely used technique with candid limitations; its practical impact on alignment practice is high even if the evidence is still small-scale.
## Confidence
**3:** Outside my core subfield; I checked captions and text, not the plots.

---

# Peer Review Report (Reviewer 4)

## Paper: Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment
## Reviewer: Kwabena Ostrovsky, Generalist (NLP lab, research institute; fictional persona)
## Expertise: language-model training and evaluation
## Date: 2026-11-10

## Summary
The paper proposes inoculation prompting: add an instruction requesting the undesired behavior to the training prompts, then drop it at test time. In four fine-tuning settings, including code reward hacking, spurious sentiment correlations, GCD sycophancy and toxic Reddit replies, the authors report lower undesired behavior with little loss on intended capabilities, and give a heuristic and an appendix model for choosing the instruction.

## Strengths
### S1: Clear contribution and memorable idea
Figure 1 and §2 communicate the idea in a minute. The contribution list is explicit and each bullet maps to a section (§1, §3, §3.5).
### S2: Good fit for the ICLR audience
Alignment under imperfect oversight and controlling generalization from fine-tuning are active ICLR topics, and the paper offers a practical technique plus a heuristic and a theory sketch.
### S3: Honest framing of limits
§5 lists real limitations (known behavior required, unreliable heuristic, increased compliance in two of six models, SFT only), which is better than most submissions.

## Weaknesses
### W1: Scope is narrow relative to the motivation
§1 motivates imperfect oversight and reward hacking in RL-style training, but experiments are SFT only on small (2B–8B) models with LoRA, on data built to contain 100% (or 50%) of the behavior (§3.1–3.4; L.1). The paper acknowledges RL as future work (§5), but the title and abstract speak generally of "alignment".
- **Suggested Fix:** Narrow the title/abstract to SFT on demonstration data, or add one on-policy RL experiment (even a small one) where the hack arises naturally.
### W2: Main-text results are figure-only, with no table of effect sizes
The central comparison (IP vs. neutral vs. PTST) is shown only as bar charts of "best and worst" prompts; readers cannot see how many tried prompts work. Judged from captions and text, results across settings differ in strength: strong in sentiment (§3.2: "makes up for most of the accuracy lost"), mixed in sycophancy ("This shows the method can be brittle", §3.3).
- **Suggested Fix:** Add a summary table: setting, base model, #prompts tried, #beating PTST, best/median effect with CI, capability change.
### W3: The venue-criteria checklist shows reproducibility and evidence gaps
Venue criteria (soundness, presentation, contribution): Soundness partly met (selection on the reporting set, single runs for several arms; §3.2, Figs. 14, 16, 17); Presentation met (clear text; many figures in the appendix); Contribution met moderately (simple method, open study); Reproducibility partly met (code promised, hyperparameters missing); Significance partly met (SFT-only scope).
- **Suggested Fix:** Add the hyperparameter table and summary table above.

**Minor:** appendix figure sections have headings without text (D, F–J); one sentence in App. M is garbled ("with training effect with IP."); 'sycophancy ←' axis labels.

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound intervention, gaps in protocol |
| Clarity | 3 | Clear, figure-heavy |
| Significance | 3 | Useful technique |
| Originality | 3 | Simple, new framing |

## Dimension Scores (0–100)
**Pool position:** better than about 70% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the contribution is clear and relevant, with weaknesses (narrow scope, thin baselines) that typical accepted papers also have.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 64 | Competent | Sound, with protocol gaps |
| Clarity & Presentation | 76 | Strong | Clear main text |
| Novelty & Originality | 66 | Competent | Simple idea, new framing |
| Significance & Impact | 70 | Competent | Relevant to the community |
| Experimental Validation | 60 | Competent | Several settings; few baselines |
| Reproducibility | 56 | Competent | Missing details |
| Ethical Compliance | 64 | Competent | Limitations honest |

## Questions for Authors
1. Does IP still work with on-policy data (RL or best-of-n from the model itself)? Yes would raise my score.
2. How sensitive is the outcome to the position of the instruction (system vs. user message; §2 reports only "preliminary experiments")?
3. Why were only 2B–8B models used? Any trend with scale?

## Limitations Assessment
**Yes, largely.** §5 is thoughtful.
## Ethics Review Flag
**No.**
## Overall Score
**4 (Borderline Accept):** A clear, useful idea in a relevant area; the scope and baselines are limited but similar to many accepted papers.
## Confidence
**4**

---

# Devil's Advocate Report

## Paper: Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment
## Reviewer: Lucía Brennagh-Takeda, evaluation and robustness group, industrial lab (fictional persona)

## Steelman
Telling a model what undesired behavior its training data contains, in the prompt, gives gradient descent a cheaper explanation of the data, so less of the behavior is written into the weights; this is cheap, general and checked with controls in four settings plus clean-data and compliance tests.

## Core Argument Chain
1. SFT on misspecified data teaches both desired and undesired behavior (§1–2).
2. Adding an instruction that requests the undesired behavior to training prompts makes the behavior conditional on the instruction (§2 hypothesis).
3. At test time with a neutral prompt, the learned behavior is reduced (§3.1–3.4), more than with PTST or unrelated instructions.
4. Capabilities are preserved (§3, §3.6.1).
5. Effective prompts can be found cheaply by measuring elicitation on the untrained model (§3.5, App. M).
∴ IP is a simple, general way to improve alignment despite flawed oversight.

## Strongest Counter-Argument
The paper demonstrates that, in four hand-constructed settings, *some* instruction among several tried gives less of a named behavior than standard training on a perfectly confounded dataset. It does not demonstrate that the mechanism is inoculation, that it is selected without reference to the results, or that it helps with oversight that is "imperfect" in the sense of the introduction (§1: reward hacking found by RL, human-approval sycophancy).

First, in the headline setting (Qwen 2 base, Figs. 1–2) the paper says the IP prompts elicited no reward hacking at all (§3.5) and that gains over the initial model likely come from "instruction-following capabilities and proper code syntax" (§3.1). So the figure that opens the paper does not isolate inoculation: the base model learns to answer in the right format whether or not the hack is requested. Second, the settings are built so the undesired trait is perfectly predictable from a short string (a regex hard-code, a concept tag, an always-correct user, a toxic filter). A model told "the user is correct" or "reviews with ambiance score higher" is being handed the label function; success may say more about instruction-following of the explicit rule than about preventing internalization. Third, each setting reports the best-performing of 4–16 prompts, with the evaluation prompt and the PTST prompt also tuned on the same evaluation (§3.2, §3.3). Fourth, the one setting with the most realistic dependence (sycophancy toward a user) is where §3.3 calls the method "brittle" and where a one-word change "caused a large reduction in effectiveness". Finally, the paper's own side-effect results show that IP can make the model *more* willing to comply with requests for the bad behavior (2 of 6 models; §5), so a developer must choose between a model that is "cleaner" by default and one that is more steerable toward misuse.

Alternative reading: IP is a form of prompt-conditioned fine-tuning in which the instruction soaks up the trait because it is made predictive; the result could be obtained by any conditioning variable (a tag, a metadata token) and would not need to be an *instruction*. The paper never tests a non-linguistic conditioning token on the same data, which would distinguish "instruction following" from "conditioning".

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim survives because the paper reports many tried prompts, unrelated-prompt and clean-data controls, and a mixed picture it states openly; the weaker, narrower claim ("in these SFT settings some well-chosen instructions reduce the learned behavior") is supported. Per the criterion-3 table: the selected prompts are the best-scoring options, but the paper has no headline numbers produced only by them, the claim holds across much of the sweep in the sentiment and coding settings (Figs. 11, 20), and the sycophancy arm reports failures; this is MAJOR.

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence / Protocol | §3.2, §3.3; Figs. 2–4 | Inoculation, evaluation and PTST prompts were chosen by score on the reporting evaluation ("the one above performed the best"); best-of-N effect unquantified; no dev split | Select on a dev split; report median over all tried prompts alongside the best |
| DA-M2 | Logic | §3.1, §3.5, Figs. 1–2 | Headline setting not explained by inoculation: IP prompts elicit no hacking, gains attributed to instruction-following/format | Add matched format-only control and a hack-rate-only comparison |
| DA-M3 | Alternative explanation | §3.1–3.4 | Success may reflect following an explicit rule that gives the label function; no non-linguistic conditioning token control | Add a tag/metadata-token baseline on the same data |
| DA-M4 | Scope / overclaim | Title, abstract, §4 | "improves test-time alignment" and "IP consistently outperforms PTST across our experiments" exceed results (§3.3 "brittle"; §3.4 failed prompt; M.1 empathy case) | Narrow wording; report per-setting success fractions |
| DA-M5 | Side effects | §3.6.2, §5, Figs. 17, 26 | In 2 of 6 models IP increases compliance with the undesired request; evidence is single-run | Seeds and a mitigation experiment (the proposed refusal-data mix) |
| DA-M6 | Realism | §1 vs §3, L.1 | Motivation is imperfect oversight/RL reward hacking; all evidence is SFT on constructed data | Add one on-policy experiment or narrow the claim |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | §3.5 vs Fig. 6 | Mixtral correlation 0.57 in text, 0.60 in caption |
| DA-m2 | Wording | §1 | "above .57" while two correlations equal .57 |
| DA-m3 | Judge validity | §3.4 | "This may be because the LLM judge finds less toxic responses" more persuasive: unvalidated judge speculation |
| DA-m4 | Theory | App. M | Constant-k assumption tested on a GPT-4.1-mini toy with 32 points and no fit statistic |

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Mixtral elicitation–performance correlation | 0.57 (§3.5) | 0.60 (Fig. 6 caption) | No (different within paper; cannot recompute without data) |
| "above .57" in four of five cases (§1) | correlations 0.57, 0.57, 0.90, 0.69 | two of four equal .57, none lower | Partly (not "above") |
| Toy study points: 2 × 2 × 8 (App. M.1) | 32 points | 2×2×8 = 32 | Yes |
| Theory Eq. (4)–(5) from (1)–(3) | thresholds as printed | re-derived: (3) follows from (1)–(2); (4) follows from (3) for k>0; (5) follows from (3) | Yes |

## Ignored Alternative Explanations
- Format/instruction-following learning on the base model (Qwen 2 base setting).
- Conditioning on any distinguishing token, not specifically an instruction.
- Prompt mismatch reduces learning of *any* behavior, partly addressed by unrelated-prompt controls but not for traits correlated with the instruction's wording.
- Winner's curse from choosing the best of many prompts on the reporting data.

## Missing Stakeholder Perspectives
Developers of open-weight models (who inherit increased steerability toward the named behavior); data providers on Reddit (consent and terms); users affected by a model that has been trained to treat "do-bad" instructions as in-distribution.

## Observations (Non-Defects)
- The authors report prompts that failed and the failure of their own heuristic in the headline setting.
- The unrelated-instruction and clean-data controls are well chosen and do rule out the simplest explanations.
- Eq. (3)–(5) are algebraically correct given their assumptions.

## Dimension Scores (0–100)
**Pool position:** better than about 54% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main empirical claim is partly confounded in the headline setting and relies on selected prompts, but the weaker claim is supported.

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 52 | Selection on reporting data (DA-M1); headline setting not isolating the mechanism |
| Clarity & Presentation | 70 | Clear; figure-only evidence |
| Novelty & Originality | 58 | Simple; precedent in cited work |
| Significance & Impact | 62 | Potentially useful; SFT-only |
| Experimental Validation | 48 | Thin baselines; best-of-N; single runs for side effects |
| Reproducibility | 50 | Missing training/decoding details |
| Ethical Compliance | 60 | Honest on side effects; no data statement |

## Overall: 3 | Confidence: 4

---

# Phase 1.5 / 1.6 — Report Check (Synthesizer, Step 0)

Each weakness was tested for being specific, not already answered, consistent with the paper, and actionable. Scores were not changed.

| Report | Weakness (draft) | Action | Reason |
|--------|------------------|--------|--------|
| R1 | "No control for train/test prompt mismatch" | Dropped | Answered: unrelated-instruction ablation (§2, Figs. 8, 11, 20) |
| R1 | "No check that IP harms clean data" | Dropped | Answered: §3.6.1, Figs. 12, 15, 28–30; moved into Strengths S1 |
| R1 | W1–W5 | Kept, ordered by severity | Specific, located, with fixes |
| R2 | "Betley et al. not cited / not credited" | Dropped | Cited and credited in §4 |
| R2 | W4 context distillation | Rewritten | Compared with the verified abstract of *Learning by Distilling Context*; stated as "mirror image"-type relation, not as a claim the paper is known |
| R3 | "No discussion of harmful compliance" | Dropped | Answered: §3.6.2, §5 |
| R3 | W1 (explaining-away) | Rewritten | Made actionable (co-occurrence measurement) |
| R4 | Typos, empty appendix headings, axis labels | Moved to one Minor line | Cosmetic |
| DA | "No seeds" | Rewritten | Main arms have ≥5 seeds (§3); single runs only in Figs. 14, 16, 17, 24, 26 |
| DA | "Reddit judge unvalidated" | Moved to DA-m3 | Cosmetic relative to core claims |

**Integrity signals for the EIC:** none (scan clean). **Text-overlap flags:** none (all kept abstracts at 0 shared 8-grams).

---

# Phase 2 — Synthesizer Package (Part A)

**Master issue list and classes**

| Issue | Sources | Class |
|-------|---------|-------|
| Prompts/eval prompts chosen on reporting evaluation; best-of-N; no dev split | R1-W1, DA-M1, R4-W3 (partly) | CONSENSUS-3 |
| Headline Qwen 2 base setting does not isolate inoculation; heuristic fails there | R1-Q1, R2-W1, DA-M2 | CONSENSUS-3 (HINGE) |
| Single-run secondary evidence; no significance tests | R1-W2, R4-W3, DA-M5 | CONSENSUS-3 |
| Narrow scope / SFT-only / small models; title overclaims | R4-W1, DA-M4, DA-M6, R3-W3 | CONSENSUS-4 |
| Missing baselines from non-prompt methods | R2-W3, DA-M3 | CONSENSUS-2 |
| Missing hyperparameters, decoding, compute | R1-W4, R4-W3 | CONSENSUS-2 |
| Theory assumptions vs. experiments | R2-W2, DA-m4 | CONSENSUS-2 |
| Side effects: increased compliance | R3-W2, DA-M5 | CONSENSUS-2 |
| Heuristic correlations weak/cluster-driven | R1-W3 | SOLO |
| Context distillation, spurious-correlation references | R2-W4 | SOLO |
| "When not to use IP" / trait co-occurrence | R3-W1 | SOLO |
| Data/ethics statement | R3-W4 | SOLO |

**DA-CRITICAL:** none raised. **SPLIT:** reviewers disagree on weight: R3 (Accept) vs R1/DA (Borderline Reject) on whether the evidence suffices. **Hinge issues:** the Qwen 2 base headline setting; selection on the reporting evaluation; SFT-only scope.

**Official score** (`aggregate_scores.py`, no eic_weight, `da_critical: []`): ratings R1 3, R2 4, R3 5, R4 4, DA 3 → mean 3.8; official composite 61.8; implied composite band 4; no consistency warnings. R3's Overall (5) is one step above its own composite band (67.5 → 4).

---

# Phase 2 — EIC Meta-Review and Decision

*Adaeze Ronaldsen, Editor-in-Chief (meta-reviewer). I read the five reports and the package first, then read the paper (abstract, §1–§5, selected appendix sections, App. M) to check the decisive points.*

# Editorial Decision

## Paper: Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment
## Submission ID: iclr26-RgOHRYHX5L
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC Adaeze Ronaldsen; R1 Kelleher-Osei, R2 Abrantes, R3 Haldorsen-Mbeki, R4 Ostrovsky, DA Brennagh-Takeda

## Decision: Borderline Accept (4) — ICLR rating label: 6 on {0,2,4,6,8,10} (6 on {1,3,5,6,8,10}); scale status secondary

**Official ratings** (shown to authors): R1 3, R2 4, R3 5, R4 4, DA 3 → mean 3.80 · official composite 61.8
**EIC assessment** (internal): weighted rating 3.69 → starting point 4 · weighted composite 61.3 → band 4 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 4
**EIC pool position:** better than about 68% of ICLR submissions (accepted share ≈ 27%). Deciding evidence: a clear, simple, relevant idea with controls and honest limitations (above the median), against selection on the reporting evaluation and an SFT-only, small-model scope (below the typical accepted paper's evidence). The decision sits at the lower edge of the typical-accepted band (62–72) rather than clearly inside it.

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A simple, counterintuitive technique that is cheap to adopt, tested in four settings with an unrelated-instruction control, clean-data checks and compliance tests, with multi-seed main arms (§3, §3.6) and a candid limitations section (§5). It gives the community a concrete handle on how training prompts shape what SFT teaches, and a heuristic for choosing prompts without training.
- **Against acceptance:** The best prompts and evaluation prompts were chosen on the reporting evaluation (§3.2, §3.3) with no held-out selection; the headline Qwen 2 base setting does not fit the paper's own mechanism and heuristic (§3.5, §3.1); several arms are single-run; non-prompt baselines are not compared; hyperparameters are missing; the evidence is SFT-only on small models and constructed data, while the title and the motivation speak of alignment under imperfect oversight.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Evaluation prompt for §3.2 chosen by score | R1-W1/ERR-3, DA-M1 | §3.2 | **Verified** | "other evaluation instructions and the one above performed the best" present verbatim |
| Best-of-N prompts shown; no dev split | R1-W1, DA-M1 | Figs. 2, 3; Tables 1–4; L.1 | **Verified** | Captions say "best and worst"; no validation split anywhere (searched); but all prompts are shown in Figs. 11, 20, so not a hidden selection |
| Headline setting: IP prompts elicit no reward hacking | R1-Q1, R2-W1, DA-M2 | §3.5, §3.1 | **Verified** | "elicited any reward hacking behavior"; gains attributed to instruction-following, untested |
| Single runs in Figs. 14, 16, 17, 24, 26 | R1-W2, DA-M5 | App. figure captions | **Verified** | Figs. 16, 17, 24, 26 say "single runs"; Fig. 14 reports eval-set error bars only; Figs. 25 and 27 do not state the number of runs |
| Mixtral correlation 0.57 vs 0.60 | R1 ERR-1, DA-m1 | §3.5 vs Fig. 6 caption | **Verified** | Minor inconsistency |
| "above .57" | R1 ERR-2, DA-m2 | §1 | **Verified** | Two of four reported correlations equal .57 |
| Hyperparameters, decoding, eval size missing | R1-W4 | §3, App. L | **Verified** | Text search finds none; supplement not provided (code link removed), so treated as questions, not grounds for a lower score |
| "IP consistently outperforms PTST" overstated | R1-W5, DA-M4 | §4; §3.3; §3.4 | **Partly correct** | The best IP prompt beats PTST in every setting reported; individual prompts do not (§3.3, §3.4) |
| Theory assumes convergence; contradicted by §5 | R2-W2 | App. M Eq. (1); §5 | **Partly correct** | Assumption stated explicitly and called a rough approximation ("we do not claim to account for all"); tension with §5 real; algebra of Eq. (3)–(5) is correct |
| Heuristic correlations cluster-driven | R1-W3 | §3.5, App. E | **Partly correct** | The pooling of neutral/unrelated prompts is stated (§3.5); the cluster explanation is plausible but cannot be verified from text and figures |
| IP raises harmful compliance in 2 of 6 models | R3-W2, DA-M5 | §3.6.2, §5 | **Verified** | "in two out of the six models we tested" |
| Context distillation uncited | R2-W4 | Refs; literature check | **Verified** | *Learning by Distilling Context* is not in the reference list; the link is conceptual, not a "known result" |
| R3: "high impact" | R3 | — | **Overstated** | Impact potential real, but evidence is small-scale and SFT-only (§5) |

Literature ledger check: the only "missing comparison" weaknesses (R2-W3) concern Casademunt et al. (recent preprint) and Chen et al. (cited): downgraded to "worth discussing"; they do not lower the decision. No under-reported baseline, no criterion-7 candidate, no text overlap.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Protocol points (selection, single runs, missing details, two numeric inconsistencies) all verified; fixable issues scored somewhat strictly but well calibrated |
| R2 (Domain) | 4 | 4 | 1.0 | Sound; the headline-setting point verified; claim-level novelty handled correctly |
| R3 (Perspective) | 5 | 3 | 0.85 | Useful perspective, but Overall 5 ("high impact, good-to-excellent evaluation") is lenient given SFT-only small-scale evidence and the paper's own side-effect findings; moderate confidence |
| R4 (Generalist) | 4 | 4 | 1.0 | Balanced, calibrated to what ICLR accepts |
| DA | 3 | 4 | 1.0 | Counter-argument largely verified (DA-M1, DA-M2); the non-linguistic-conditioning alternative is speculative but fair |

### DA-CRITICAL Rulings
None raised. The DA applied the criterion-3 table to the prompt-selection issue and rated it MAJOR; I agree: the selected prompts are the best-scoring options, but there are no headline numbers fixed only by them, the effect holds for many tried prompts in the coding and sentiment settings (Figs. 11, 20, from captions and text), and the sycophancy failures are reported. No cap applies.

### Final Decision and Justification
The EIC-weighted rating is 3.69, which rounds to 4 and matches the cross-check composite band (61.3, band 4). I keep the starting point. The decisive question was whether the selection of prompts on the reporting evaluation, and the failure of the mechanism and heuristic in the Qwen 2 base setting, undermine the main claim. They weaken the strong form ("IP improves alignment"), and the revision should say so; they do not undermine the weaker form that the evidence supports (in these SFT settings, appropriately chosen training instructions reduce the learned behavior without clear damage to capabilities, with an unrelated-instruction control and clean-data checks). The remaining weaknesses (single runs in the appendix, missing non-prompt baselines, missing hyperparameters, scope) are typical of accepted ICLR papers and are fixable in a revision, which ICLR allows. Against that, the evidence is at the lower end of what accepted papers at ICLR show, and the contribution is a simple idea whose value depends on follow-up evidence, so I do not go above Borderline Accept. The decision does not exceed any DA ceiling (none applies). This simulates how a careful panel might see this draft; it is not a prediction.

---

## Score Summary

### Official Scores and EIC Assessment

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|---------------------------|--------|
| Technical Rigor | 56 | 62 | 66 | 64 | 52 | 60.0 | 59.4 | 14 |
| Clarity & Presentation | 74 | 72 | 74 | 76 | 70 | 73.2 | 73.2 | 6 |
| Novelty & Originality | 60 | 62 | 72 | 66 | 58 | 63.6 | 62.9 | 14 |
| Significance & Impact | 62 | 68 | 78 | 70 | 62 | 68.0 | 67.1 | 16 |
| Experimental Validation | 50 | 58 | 62 | 60 | 48 | 55.6 | 54.9 | 14 |
| Reproducibility | 48 | 55 | 58 | 56 | 50 | 53.4 | 52.8 | 10 |
| Ethical Compliance | 62 | 66 | 62 | 64 | 60 | 62.8 | 62.8 | 6 |
| **Composite** | 57.9 | 62.8 | 67.5 | 64.8 | 56.0 | **61.8 (before)** | **61.3 (after)** | |

No dimension spread exceeds 20. R3's Overall (5) is one step above its own composite band (4), within tolerance.

### Target-Venue Scores (ICLR, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 3 / 3 |
| Rating | 6 on {0,2,4,6,8,10} (6 on the earlier {1,3,5,6,8,10} scale); equals the EIC decision 4 |

*ICLR scale details are secondary (recent analyses, not the venue's own wording); verify against the current form.*

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment" to ICLR.

The paper studies a simple, counterintuitive idea with real relevance to training under imperfect oversight, and it does so with unusual candor about where the method fails.

**Overall Assessment:** The reviewers found the idea clear, cheap and worth the community's attention, with sensible controls (unrelated instructions, clean data, compliance checks). They were divided on whether the evidence, produced in four constructed SFT settings on small models, supports the broad claims in the title and abstract. The panel's official ratings were 3, 4, 5, 4 and 3.

**Key Strengths Identified by Reviewers:**
1. A clear, simple method with a memorable framing (R2, R3, R4).
2. Good controls and candid reporting of failures and side effects (R1, R2, R3, R4, DA).
3. A practical prompt-selection heuristic and an appendix model that gives a rationale (R2, R3).

**Key Concerns Requiring Attention:**
1. Prompts and evaluation prompts appear to have been chosen on the same evaluation that reports the results (R1, DA, R4; CONSENSUS-3).
2. In the headline Qwen 2 base setting no prompt elicited the behavior, so the paper's mechanism and heuristic do not explain the result there (R1, R2, DA; CONSENSUS-3).
3. Scope: SFT-only, 2B–8B models, constructed datasets; title and abstract speak more generally (R4, DA, R3; CONSENSUS-4).
4. Single-run secondary evidence, missing hyperparameters, and no comparison with non-prompt methods (R1, R2, DA, R4).

**Decision: Borderline Accept (4).** The weaknesses are real but fixable in a revision, and the weaker claim the evidence supports is useful. Acceptance would be on the condition that the authors narrow the claims to SFT-based settings, report selection on a held-out split, and address the headline-setting issue. Please see the Revision Roadmap.

Sincerely,
Adaeze Ronaldsen
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Narrow scope / SFT-only / title overclaims | R3, R4, DA (and R2's novelty note) | CONSENSUS-4 |
| Selection of prompts on reporting evaluation | R1, R4, DA | CONSENSUS-3 |
| Headline setting does not isolate inoculation | R1, R2, DA | CONSENSUS-3 |
| Single-run evidence, no significance tests | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Is the evidence sufficient for an Accept? | R3 (5) | R1, DA (3) | Both are partly right; the idea and controls merit a place, but the selection and scope gaps keep it at Borderline Accept |
| Novelty | R3 (72) | R1, DA (58–60) | Medium: the paper credits Betley et al. for IP-like prevention (§4); the systematic measurement and capability checks are new |

### Score Spread Discussion
No dimension was flagged ⚠ (all spreads ≤ 16). The widest is Significance (62–78): R3 weighs deployment value, R1 and DA weigh evidence scale; I adopt the weighted middle (67.1).

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Selection on the reporting evaluation | Yes (R1-W1) | n/a | Held-out split, existing runs |
| DA-M2 | MAJOR | Headline setting not isolating inoculation | Yes (R1, R2) | n/a | New control runs |
| DA-M3 | MAJOR | No non-linguistic conditioning control | No | n/a | New experiment |
| DA-M4 | MAJOR | Overclaiming in title/§4 | Yes (R1-W5, R4-W1) | n/a | Rewording |
| DA-M5 | MAJOR | Side-effect evidence single-run | Yes (R3-W2) | n/a | Seeds |
| DA-M6 | MAJOR | SFT vs. RL motivation gap | Yes (R4-W1) | n/a | Narrow claim or new experiment |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*(No DA-CRITICAL issues were upheld; these are the issues I verified as undermining the strong form of a main claim.)*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | Prompt and evaluation-prompt selection on the reporting evaluation | R1-W1, DA-M1, R4-W3 | §3.2, §3.3, Figs. 2–4 | Dev/test split of eval prompts; report median over tried prompts next to the best | Low–Med (≈1 GPU-day) | Yes |
| P1-2 | Headline Qwen 2 base setting does not isolate inoculation | R1-Q1, R2-W1, DA-M2 | §3.1, §3.5, Figs. 1–2 | Format-only control and hack-rate-only comparison; state heuristic's inapplicability in the abstract | Med (≈10–20 GPU-h) | Yes (partly) |
| P1-3 | Claims exceed evidence (title, abstract, "consistently") | R1-W5, DA-M4, R4-W1, R3-W3 | Title, abstract, §4 | Narrow to SFT on demonstration data; per-setting success fractions | Low | Yes |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Single-run side-effect and Mixtral/Qwen 2.5 evidence; no tests | R1-W2, DA-M5 | ≥3 seeds; paired bootstrap CIs; drop "significantly" where untested | Med (≈10 GPU-h) | Yes |
| S2 | Missing hyperparameters, decoding and compute | R1-W4, R4-W3 | Per-setting table; release configs | Low | Yes |
| S3 | Non-prompt baselines (steering/ablation/filtering oracle, conditioning token) | R2-W3, DA-M3 | Add at least one baseline on the sentiment setting; discuss the others | Med–High | Partly |
| S4 | Theory assumptions vs. experiments | R2-W2, DA-m4 | Present as heuristic; fit statistic; relate (4)–(5) to settings | Low–Med | Yes |
| S5 | Heuristic evidence cluster-driven | R1-W3 | Within-IP Spearman with CIs; top-1 selection accuracy | Low | Yes |
| S6 | Context distillation and group-robustness references | R2-W4 | Add *Learning by Distilling Context* (Snell, Klein, Zhong, 2022) and discuss; *A General Language Assistant as a Laboratory for Alignment* (Askell et al., 2021) | Low | Yes |
| S7 | Realism gap: SFT vs. RL motivation | R4-W1, DA-M6 | One on-policy experiment, or narrow the motivation | High | No |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | "When not to use IP": trait co-occurrence | R3-W1 | Measure co-occurrence against capability loss |
| N2 | Data/ethics statement for Reddit data | R3-W4 | Add short statement |
| N3 | Numeric inconsistencies (0.57 vs 0.60; "above .57"); garbled App. M sentence; empty appendix headings | R1 ERR-1/2, R4 | Fix |
| N4 | Judge validation on Reddit CMV | R3-W3, DA-m3 | Small human check |
| N5 | Longer training curve ("preliminary experiments", §5) | R1-Q4 | Show curve |

## Estimated Revision Effort
- Priority 1: 3 items, ≈2–4 days of compute plus writing
- Priority 2: 7 items, ≈4–7 days (S7 is a separate project)
- Priority 3: 5 items, ≈1 day
- **Total estimated revision time**: about 1–2 weeks, excluding any RL experiment.
