# Simulated Review: EFRame: Deeper Reasoning via Exploration-Filter-Replay Reinforcement Learning Framework

*Simulation of how a careful ICLR panel would likely see this draft (not a prediction). Date: 2026-11-05. Mode: full, confirmation skipped, literature check: strict, cutoff 2025-09-24. The five reviewer passes were run one after another in a single model context (no subagents); they share one context and are not independent agents. Figures were not available (text extraction only): every figure-dependent claim (Figs. 1, 2, 4, 5, 6) is judged from captions and surrounding text and is marked as such.*

---

## Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | EFRame: Deeper Reasoning via Exploration-Filter-Replay Reinforcement Learning Framework |
| Primary Discipline | ML → reinforcement learning with verifiable rewards (RLVR) for LLM / MLLM reasoning |
| Secondary Discipline(s) | Multimodal (vision-language) math reasoning; policy-gradient theory (entropy dynamics) |
| Paper Type | Empirical (composite weights: empirical) |
| Core Technique(s) | GRPO, additional high-temperature rollouts for hard prompts, positive-only online filtering, replay buffer; Qwen2.5-VL-7B-Instruct via EasyR1/VeRL |
| Target Venue | ICLR (stated by the user); profile key `iclr` (2026 cycle, scale status: secondary) |
| Venue-Specific Notes | none |
| Paper Maturity | Submission-ready draft with presentation rough edges (a broken citation "?", typos) |
| Ethics-Relevant Content | none (public math/diagram datasets, no human subjects, no deployment risk) |

### Claimed Contributions (as stated by the authors)
1. **C1:** Additional high-temperature rollouts on prompts whose initial group has no correct response "explore high-quality trajectories" and "enable access to deeper reasoning capabilities that remain unattainable under vanilla GRPO" (Abstract, §4.2, §6.1).
2. **C2:** Online filtering (keep non-zero-advantage regular samples, keep only positives from additional rollouts) removes noise and variance (§4.3, §6.2).
3. **C3:** A replay buffer re-exploits rare high-advantage samples, so that EFRame "establishes a complete and stable learning cycle" with stable entropy (§4.4, §6.3, Thm 4.5).
4. **C4:** Empirical gains: +16.80 on Geometry3K ("36.5%" over GRPO) and +5.66 average on four multimodal math benchmarks (§1, Tables 1–2, §5.2).
5. **C5:** A categorization of training samples (regular / high-quality / low-quality) giving "a deeper analysis of how different types of samples contribute" (Abstract, §1).

### Paper memory (factual record shared with all reviewers)
- **Setup facts.** Backbone Qwen2.5-VL-7B-Instruct (§5.1). Training data: Geometry3K, and a 6k sample "from the dataset proposed in (Wei et al., 2025b;a)" (§5.1). Framework EasyR1/VeRL; 8 A800 GPUs; max response length 2048; global batch 128; rollout batch 512; G1=5, temperature 1.0; lr 1e-6; ε_low=ε_high=0.2 for GRPO and EFRame; DAPO with ε_high=0.3 plus length penalty; EFRame: G2=20, temperature 1.2, replay buffer 5120, replay every 5 steps, samples with |Â|>1 stored (§5.1). Binary reward (App. A).
- **Not stated after text search** (terms searched: test set, test split, validation, held-out, checkpoint, seed, best model, select, early stop, epoch, steps): evaluation split for Geometry3K accuracy; which training set produced Table 1; number of training steps/epochs; KL coefficient β; checkpoint selection; seeds / number of runs; evaluation protocol (decoding, answer matching/judge) for Tables 1–2; provenance of baseline numbers in Table 1.
- **Headline numbers and sources.** "outperforms GRPO by 36.5%" (§1, §5.2) ← Table 2 (55.24 vs 50.75; gains over base 16.80 vs 12.31). "+5.66" average over base (Table 1: 55.13 vs 49.47). "outperforming GRPO by 19.9%" (§5.2) ← Table 1 gains 5.66 vs 4.72. The over-95% filtered share (§4.3) has no table. Time/step 442 vs 327 vs 182 s (Table 2).
- **Appendix.** App. A: auxiliary rewards dominate when accuracy signal vanishes, hence binary reward (Fig. 6). App. B: method "sensitive to three key hyperparameters: clip higher, replay buffer size, and replay frequency"; improvements "less pronounced" on "simple datasets such as Math" (no such results shown).
- **Unverifiable.** All figures (1, 2, 4, 5, 6): accuracy/entropy/reward curves are described only in prose. Eq. 1/Defs 4.1–4.3/Eq. 2 are partly garbled by extraction (Def. 4.1's set notation) and treated as "unverifiable", not as errors. Code link was removed in the blinded text.

### Integrity signals
The skill's `integrity_scan.py` was not run (this evaluation permits only the aggregation and `related_search.py` scripts). Instead the full text was read and searched for text addressed to reviewers or AI systems (patterns such as "ignore previous", "give a positive review", "LLM reviewers"): **none found**. No redaction was needed, so reviewers read the original text. Literature-check similarity flagged 2 shared 8-grams with a recent preprint ("Multimodal Mathematical Reasoning with Diverse Solving Perspective"), both the generic phrase "enhanced the reasoning capabilities of large language models"; the EIC treats this as standard phrasing, not an integrity concern.

### Literature check (strict, cutoff 2025-09-24)
8 queries (claim 5, baseline 1, expansion 2), 25 unique kept results, plus `verify`, `scout` (MathVista), `similarity` and `novelty` runs. Gaps left open: no prior work kept from 2021–2022 (not relevant to a 2025 topic); C4 is a result claim and has no query; `benchmarks` listed none for this text, so only MathVista was scouted. arXiv-only search: "no close prior work found" would not mean novelty.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Ingrid Valtonen-Okafor, ML group, large public research university (Northern Europe)
- **Seniority / Expertise**: Senior faculty / policy-gradient methods, LLM post-training, evaluation of RL for reasoning
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Judges against what the venue accepts; weights what a reviewer got right, not how harsh they are

### Reviewer 1 (Methodology): Dr. Tomasz Reinholt, industrial research lab (Central Europe)
- **Seniority / Expertise**: Senior industry scientist / RL fine-tuning of LLMs; evaluation protocols for VLM math benchmarks
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on matched compute budgets and seeds; recomputes every delta

### Reviewer 2 (Domain): Dr. Priyanka Anand-Voss, NLP/RL group, public research university (South Asia)
- **Seniority / Expertise**: Mid-career faculty / GRPO-family algorithms; data-efficient RLVR; entropy dynamics
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads related work closely; checks citations against the bibliography

### Reviewer 3 (Perspective): Dr. Camila Ferreyra-Holt, operations research and control department (South America)
- **Seniority / Expertise**: Mid-career faculty / classical RL (experience replay, exploration-exploitation), stochastic optimization
- **Review Focus**: Cross-disciplinary connections, deployment, assumptions, broader impact
- **Style**: Constructive; connects the method to classical RL and asks what assumptions carry the argument

### Reviewer 4 (Generalist): Dr. Jun-seo Marlowe, multimodal learning group, mid-size university (East Asia)
- **Seniority / Expertise**: Postdoc-to-assistant-professor level / vision-language models, general deep learning
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee reader; weighs weaknesses against what accepted papers carry

### Devil's Advocate: Dr. Oluwaseun Brandt, industrial research lab (West Africa / North America)
- **Seniority / Expertise**: Senior scientist / evaluation methodology, causal attribution of gains, robustness
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous, never hostile; steelmans first

*Personas are fictional. Proceeding with the stated assumptions.*

---

## Phase 1: Independent Reports

# Peer Review Report

## Paper: EFRame: Deeper Reasoning via Exploration-Filter-Replay Reinforcement Learning Framework
## Reviewer: Dr. Tomasz Reinholt, Methodology (industrial research lab, Central Europe; fictional persona)
## Expertise: RL fine-tuning of LLMs; evaluation protocols for VLM math benchmarks
## Date: 2026-11-05

---

## Summary
The paper adds three components to GRPO for RLVR on a 7B vision-language model. For prompts where all G1=5 initial rollouts fail, it draws G2=20 more samples at temperature 1.2, keeps only the positive ones, and stores high-advantage samples in a replay buffer that is replayed every 5 steps. It reports +16.80 accuracy on Geometry3K (Table 2) and +5.66 average over the base model on four multimodal math benchmarks (Table 1), and argues through ablations (Fig. 5) and an entropy argument (Thm 4.5) that each part is needed.

---

## Strengths

### S1: A clear, implementable recipe with stated key hyperparameters
§5.1 lists G1, G2, temperatures, buffer size 5120, replay period, and the |Â|>1 storage rule, and the code is said to be available. For an RLVR paper this is better specified than many.

### S2: Cost is reported, and it is modest
Table 2 reports time per step (442 s vs 327 s for GRPO, ×1.35; recomputed 442/327 = 1.35). Reporting cost next to accuracy is the right habit.

### S3: In-domain gain is large relative to the same-framework baselines
Table 2: 55.24 vs 50.75 (GRPO) and 49.09 (DAPO) on Geometry3K; base 38.44. All three RL methods use the same backbone, framework and batch settings (§5.1), which keeps this comparison cleaner than the Table 1 comparison against external models.

### S4: Honest hint of sensitivity
Appendix B states the method is "sensitive to three key hyperparameters: clip higher, replay buffer size, and replay frequency", and that gains are smaller on simple data. This is useful, though it is not backed by any sweep.

---

## Weaknesses

### W1: Headline gains over GRPO are small or unverified, are single-run, and are reported with a misleading denominator
The abstract-level claim "it outperforms GRPO by 36.5%" (§1) is the ratio of gains over the base model (16.80/12.31), not an accuracy ratio. In absolute terms Table 2 shows +4.49 points over GRPO (55.24 vs 50.75, 8.8% relative); in Table 1 the average gain over GRPO is +0.94 (55.13 vs 54.19), and "outperforming GRPO by 19.9%" (§5.2) is again 5.66/4.72. On MathVision EFRame (28.82) is below GRPO (29.11). No seeds, runs or intervals are reported anywhere, so a +0.94 average on four benchmarks (and a −0.29 on one) cannot be separated from run-to-run noise (RL fine-tuning of this scale is single-seed noisy). 
- **Suggested Fix**: Report absolute gains over each baseline; run ≥3 seeds for Table 2 and the GRPO/EFRame rows of Table 1 (or a paired bootstrap over test items for Table 1). Estimated cost: 3 seeds × 2 methods × Geo3K run ≈ 6 runs on 8 GPUs; the paper does not give steps, so roughly a few hundred GPU-hours [my estimate].

### W2: Baselines are not compute-matched, and DAPO is a partial reimplementation
EFRame draws extra rollouts (G2=20) on hard prompts and extra replay gradient steps, at ×1.35 step time (Table 2). Fig. 1's caption shows that simply raising GRPO's G from 5 to 20 improves accuracy at four times the per-step time, but no GRPO row with matched rollouts or matched wall-clock appears in Table 2, and I could not see the Fig. 1 numbers. The DAPO baseline is described as "ϵhigh = 0.3 and an additional length-aware linear penalty (up to 0.5)" (§5.1), i.e. without DAPO's dynamic sampling, which is the closest existing counterpart to the paper's filtering; it also changes the reward (length penalty) while GRPO/EFRame use a binary reward (App. A), so DAPO differs in more than one factor. DAPO is faster than GRPO (×0.57), which suggests the shorter-response effect, not sampling, dominates its cost.
- **Suggested Fix**: Add (i) GRPO with G chosen to match EFRame's samples per step and wall-clock, (ii) DAPO with dynamic sampling on the binary reward, (iii) GRPO + replay only, GRPO + extra rollouts only, matched in total gradient updates. Cost: about 3–4 extra Geo3K runs.

### W3: The "deeper reasoning" and "aha moment" claims are not measured
The abstract says EFRame "enables access to deeper reasoning capabilities that remain unattainable under vanilla GRPO" and §4.2 says it increases "the frequency of emergent" aha moments. The paper's own motivation is the pass@k ceiling (§1, citing Yue et al.), yet no pass@k curve, no solve-rate on the initially unsolvable prompts, and no frequency count of reflection behaviours is shown; all evidence is pass@1 accuracy and training curves. Pass@1 gains support a weaker claim ("better pass@1 and a smoother training curve"), not boundary expansion. The sentence that the "steadily increasing response length during training reflects" improved reasoning (§5.2) is asserted from length alone.
- **Suggested Fix**: Report pass@k (k up to 64–256) on Geometry3K and MathVista for base, GRPO, EFRame; report the fraction of originally-unsolved training prompts that become solved; or narrow the wording.

### W4: Ablations are confounded and shown only as curves on one dataset
Fig. 5 (Geometry3K only, not visible in the text extraction) carries Claims 1–3. The "no filtering" variant removes both zero-advantage filtering and the discarding of negatives (§6.2), so Claim 2 ("Low-quality samples ... mislead optimization") is not isolated from the effect of zero-advantage samples. The "no replay" variant (§6.3) is said to fall "even falling below that of the vanilla GRPO baseline", which, if true, mostly shows that positive-only training on 1–2 rare samples per hard prompt is unstable without reuse, not that replay is the stabilizing mechanism. No table gives final ablation numbers.
- **Suggested Fix**: Provide an ablation table (accuracy at fixed steps, with seeds) with single-component and pairwise variants, including (a) extra rollouts keeping negatives, (b) replay on regular samples only, and a second dataset.

### W5: The protocol is under-specified, so the numbers cannot be audited
After searching the whole text I found no statement of: which Geometry3K split is evaluated; which training set (Geometry3K or the 6k mix) produced Table 1; training steps/epochs; KL β; checkpoint selection (final vs best); decoding and answer-matching for MathVision/MathVerse/MathVista/We-Math; and whether the external baselines in Table 1 (GPT-4o, Claude, QvQ, Skywork R1V, MM-Eureka, OpenVLThinker, ThinkLite-VL, VLAA-Thinker) are copied or re-evaluated. If checkpoints were chosen by test accuracy this would be a leakage issue; it is **not stated**, so it is a question, not a charge. 
- **Suggested Fix**: State all of the above; mark copied baselines; report the final checkpoint at a pre-fixed step.

### W6: Internal inconsistencies about what is replayed and which clip range is used (see Error Log)
§4.4 describes the buffer as holding high-quality (positive, hard-prompt) samples, while §5.1 stores "responses with absolute advantage larger than 1". With binary rewards, a single incorrect answer in a group of five has Â ≈ −1.8 to −2.0 (derived), so negatives from easy prompts can qualify. And §5.1 sets "ϵlow = ϵhigh = 0.2" while Eq. 2 and App. B treat clip-higher as a key hyperparameter.
- **Suggested Fix**: State exactly what enters the buffer and the ε values; give a sensitivity table for the three hyperparameters App. B names.

**Minor**: Typos ("challanging", "distorb", "avail able", "aand"); Fig. 1/Table 2 time ratio 182/327 rounds to ×0.56, printed ×0.57.

### Claim-to-evidence map
| ID | Claim | Where stated | Supporting evidence | Verdict |
|----|-------|-------------|---------------------|---------|
| C1 | Extra rollouts unlock deeper reasoning | Abstract, §4.2, §6.1 | Fig. 5 reward plateau (not visible) | Partially (pass@1 only) |
| C2 | Positive-only filtering stabilizes, saves compute | §4.3, §6.2 | Fig. 5; the over-95% filtered share is untabulated | Partially (confounded) |
| C3 | Replay stabilizes entropy and is necessary | §4.4, §6.3, Thm 4.5 | Fig. 5; theorem not tested | Partially |
| C4 | Beats GRPO: 36.5% (Geo3K), +5.66 avg | §1, Tables 1–2 | Tables 1–2 (recomputed OK) | Partially (small abs. margin, single run, one reversal) |
| C5 | Sample categorization gives insight | Abstract, §1 | Qualitative reading of Fig. 5 | Unsupported as a distinct contribution |

### Protocol sweep (quotes)
No statement found for evaluation split, checkpoint choice, validation set, or seeds (search terms above). The only split-related sentences: "reward on the training set plateaus" (§6.1) and "little improvement on the test set" (§6.2); no selection on the test set is stated.

### Error Log
| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E5/E1 | §1, §5.2, Table 2, Table 1 | "it outperforms GRPO by 36.5%" | 36.5% = 16.80/12.31 (ratio of gains over base); accuracy gap is 55.24−50.75 = 4.49 points (8.8%) | Recomputed from Table 2; same for 19.9% = 5.66/4.72 (Table 1) | High | MAJOR (wording; the numbers themselves are right) | Report absolute gains; state the ratio is of gains over base |
| ERR-2 | E6 | §5.1 vs Eq. 2 vs App. B | "GRPO and our method adopt ϵlow = ϵhigh = 0.2" | App. B names "clip higher" as a key hyperparameter of the method, but the stated EFRame setting is symmetric | Cross-referenced (3 locations) | Medium (may mean the clip-higher value is simply 0.2) | MINOR | State the values and sweep |
| ERR-3 | E6 | §4.4 vs §5.1 | "responses with absolute advantage larger than 1 are stored in a replay buffer of size 5120" | §4.4 describes only high-quality (positive) samples; |Â|>1 also admits incorrect answers in mostly-correct groups (4/5 correct → incorrect Â = −2.0 with population std) | Derived | Medium (depends on implementation) | MAJOR if negatives are in the buffer | Clarify the rule; if positives only, say so |
| ERR-4 | E3 | §4.5, Thm 4.5 vs §5.1 | "If the actor policy πθ is a tabular softmax policy updated via natural policy gradient" | Experiments use a 7B network with PPO-style clipping, token-level loss and off-policy replay with stale advantages; the theorem covers none of these | Cross-referenced | High | MAJOR | State it as heuristic, or measure Cov(log π, A) in training |
| ERR-5 | E1 | Table 2 | "182(×0.57)" | 182/327 = 0.557 → ×0.56 | Recomputed | High | MINOR | Fix rounding |

---

## Missing References
*(Domain Reviewer owns this section; R1 adds none beyond the protocol points above.)*

---

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Single-run, unmatched baselines, untested mechanism |
| Clarity | 2 | Enough to implement, but protocol and replay rule unclear |
| Significance | 2 | Modest verified gain over strongest same-framework baseline |
| Originality | 2 | Components exist separately; combination is the contribution |

## Dimension Scores (0–100)

**Pool position:** better than about 33% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main claim over GRPO rests on one run per method with an average margin of +0.94 on Table 1, and the baselines are neither compute-matched nor complete (W1, W2).

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Mechanism asserted via a theorem that does not apply; confounded ablations |
| Clarity & Presentation | 55 | Competent | Understandable recipe; broken citation, undefined protocol items |
| Novelty & Originality | 45 | Developing | Each component has close prior art (see R2) |
| Significance & Impact | 50 | Developing | In-domain gain real; OOD gain over GRPO small |
| Experimental Validation | 44 | Developing | One model, single runs, partial DAPO, Geo3K-only ablations |
| Reproducibility | 50 | Developing | Hyperparameters given but steps, β, eval protocol, seeds absent; code promised |
| Ethical Compliance | 62 | Competent | Nothing at stake; limitations only briefly stated (App. B) |

---

## Questions for Authors
1. Which split and which checkpoint produced Table 2 and Table 1, and was either chosen using test accuracy? (A clear "fixed final step, separate validation" would remove the main audit concern.)
2. What do GRPO with G matched to EFRame's per-step sample count, and DAPO with dynamic sampling and a binary reward, score on Geometry3K? (A matched GRPO within 1–2 points would lower my score; a clear gap would raise it.)
3. Over ≥3 seeds, what are the mean and spread of Table 2 and Table 1 averages?
4. What exactly enters the replay buffer, and what is the clip-higher value used?
5. Does EFRame raise pass@k at large k beyond the base model?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially. App. B mentions hyperparameter sensitivity and smaller gains on simple data, but the paper presents no failure cases and no results on those simple datasets.

## Ethics Review Flag
**No**: public math datasets, no human subjects.

## Overall Score
**3**: A workable recipe with one large in-domain gain, but the headline margin over GRPO is small, single-run and not compute-matched, and the main mechanism claims are not measured.

## Confidence
**4**: I rechecked every delta and searched the text for protocol statements; figures were not visible, so ablation shapes are taken from text.

---

# Peer Review Report

## Paper: EFRame: Deeper Reasoning via Exploration-Filter-Replay Reinforcement Learning Framework
## Reviewer: Dr. Priyanka Anand-Voss, Domain (NLP/RL group, public research university, South Asia; fictional persona)
## Expertise: GRPO-family algorithms; data-efficient RLVR; policy entropy dynamics
## Date: 2026-11-05

---

## Summary
EFRame combines three known ideas in one GRPO pipeline: extra sampling for hard prompts, discarding zero-advantage and (in the extra round) negative samples, and replaying high-advantage samples. The authors support the design with an entropy argument based on a covariance identity for softmax policies and show gains for Qwen2.5-VL-7B on Geometry3K and four multimodal math benchmarks. Their stated position is that earlier GRPO fixes "typically focus on individual components" while EFRame integrates exploration, stability and sample efficiency (§2).

---

## Strengths

### S1: A coherent diagnosis of GRPO's failure modes
§3.2 organizes limitations into exploration, sample efficiency and instability, and ties them to vanishing advantage when all samples are correct or all wrong (§1, §3.2). This framing is useful and consistent with the cited literature (Yue et al.; Yu et al.).

### S2: The entropy lens is the right tool
Using the covariance view of entropy change (Thm 4.5) to reason about why rewarding rare correct samples raises entropy, and why re-exposure lowers it, is a sensible qualitative explanation worth testing (§4.5).

### S3: Attention to reward design
App. A explains why auxiliary rewards can dominate the group-normalized advantage when accuracy vanishes, and the paper therefore uses a binary reward. This is a practical insight that is easy to miss.

### S4: The ablation structure follows the three components
§6.1–6.3 map one ablation to each component, which makes the paper's argument easy to follow even where the evidence is thin.

---

## Weaknesses

### W1: The contribution is a combination of components that each have close, uncited prior art
The literature check (strict mode, cutoff 2025-09-24) found work on each component. **C1** (extra rollouts for hard prompts at higher temperature): Liao et al., "Enhancing Efficiency and Exploration in Reinforcement Learning for LLMs" (EMNLP 2025, prior peer-reviewed; https://arxiv.org/abs/2505.18573) allocates more rollouts to harder questions and adds a temperature adjustment to keep entropy stable; the paper neither cites nor differentiates it. Per the claim-level profile the verdict for C1 is *incremental* (coverage level 4: the budget allocation and the temperature/entropy motivation overlap, but positive-only filtering and replay are absent there). **C2/C3**: Sun et al., "Improving Data Efficiency for LLM Reinforcement Fine-tuning Through Difficulty-targeted Online Data Selection and Rollout Replay" (NeurIPS 2025, prior peer-reviewed; https://arxiv.org/abs/2506.05316) uses difficulty-targeted selection plus a rollout-replay buffer (level 3: partial coverage, different goal: cost saving); RePO (Li et al., 2025; https://arxiv.org/abs/2506.09340) is a replay-for-GRPO method (recent preprint, "worth discussing", not a required comparison). §2 cites only DAPO, Dr.GRPO, CPPO, VL-Rethinker, LUFFY and similar, so the "integrated solution" positioning is not tested against the closest neighbours. This is a MAJOR novelty weakness (one claim incremental, two medium), not a "known results" issue: no single prior work covers all central claims.
- **Suggested Fix**: Add the three works to §2, add a differentiation paragraph (positive-only filtering on hard prompts; what the replay buffer stores; entropy rationale), and ideally one empirical comparison against dynamic rollout allocation.

### W2: The theoretical grounding is heuristic and its source is non-archival, with a broken citation
Thm 4.5 is attributed to "Liu (2025)", a Zhihu blog post (reference list), and extended "by ?" (§4.5: "organized and extended by ?"); the proof is deferred to these two sources. The covariance form appears, to my knowledge, in "The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models" (Cui et al., 2025; https://arxiv.org/abs/2505.22617, found by `verify`; the authors should check and cite the archival source). More importantly the theorem is for a tabular softmax policy under exact NPG, but §4.5 uses it to argue about token-level PPO-clip training with off-policy replay and stale advantages (E3). The paper does not measure Cov(log π, A) during training, so "the replay buffer here serves to reduce policy entropy" is a plausible story, not a result. Thm 4.4 is the elementary identity that advantages in a group sum to zero.
- **Suggested Fix**: Cite the archival source, state the theorem as motivation, and log the covariance term for with/without replay.

### W3: The treatment of negative samples sits uneasily with the work the paper cites
§1 notes that "Previous studies have shown that both positive and negative samples contribute to RLVR training (Zhu et al., 2025)" and then §4.3 discards all negatives from the exploration round, while Claim 2 (§6.2) says low-quality samples "mislead optimization". The cited Zhu et al. paper's own title ("The surprising effectiveness of negative reinforcement in LLM reasoning") points the other way. The paper's claim is narrower (negatives from *hard* prompts at temperature 1.2) but never says so or tests it, and its ablation (W4 of R1) does not isolate it.
- **Suggested Fix**: Add a variant that keeps negatives from the exploration round but down-weights them, and discuss the tension with Zhu et al.

### W4: Citation accuracy issues (E7)
§1 says "DeepSeek-R1 introduced Group Relative Policy Optimization (GRPO)" while §2/§3 and the reference list correctly credit Shao et al. (2024); DPO appears twice (Rafailov 2023 and 2024 entries are the same paper); "Lin et al., 2025" (CPPO, an acceleration method) is cited for "increasing k yields only marginal improvements" (§1), which is not the main point of that work as its title suggests [verify].
- **Suggested Fix**: Correct attributions and de-duplicate the list.

### Novelty delta table
| Claimed contribution | Closest prior work (link) | What that work already does | What is actually new here | Cited and differentiated? |
|----------------------|---------------------------|-----------------------------|---------------------------|---------------------------|
| C1 extra rollouts for hard prompts, T=1.2 | Liao et al. 2025 (https://arxiv.org/abs/2505.18573) | Difficulty-based rollout budgets; temperature adjustment to hold entropy | Trigger rule (all-fail in G1=5), fixed G2=20 | No |
| C2 positive-only filtering in exploration round | Sun et al. 2025 (https://arxiv.org/abs/2506.05316); GRESO (https://arxiv.org/abs/2506.02177, recent) | Difficulty-aware online selection; skipping uninformative prompts | Discarding negatives of hard prompts | No |
| C3 replay of high-advantage samples | Sun et al. 2025; RePO (https://arxiv.org/abs/2506.09340, recent) | Rollout replay; replay buffers for GRPO | Selection by |Â|>1; link to entropy stabilization | No |
| C4 +16.80 / +5.66 | Vision-R1 (https://arxiv.org/abs/2503.06749) | Cold-start data + RL on a 7B MLLM; abstract reports 73.5% MathVista | Not comparable setting | No |

### Per-claim novelty (`related_search.py novelty`)
| Claim | Dimension | Novelty | Top prior work (level, link, label, cited?) | Reasoning |
|-------|-----------|---------|---------------------------------------------|-----------|
| C1 | method | incremental | Liao et al., level 4, arXiv 2505.18573, prior (peer-reviewed), not cited | Same trigger idea (more rollouts for harder prompts) and entropy motivation |
| C2 | method | medium | Sun et al., level 3, arXiv 2506.05316, prior (peer-reviewed), not cited | Online difficulty-aware selection, different rule |
| C3 | method | medium | Sun et al., level 3, same | Replay exists; selection rule and entropy account differ |
| C4 | result | high | Vision-R1, level 2, prior (peer-reviewed) | Different setting; no matching number |
Script reading: "no central claim fully covered by prior work"; attribution to Sun et al. Search is arXiv-only.

### Baseline scout (MathVista; Geometry3K and the other benchmarks returned no usable abstracts)
| Benchmark / metric | Prior method (link, label) | Its reported number | Compared in the paper? | Paper's number for it | Note |
|--------------------|----------------------------|---------------------|------------------------|-----------------------|------|
| MathVista accuracy | Vision-R1-7B (arXiv 2503.06749, prior peer-reviewed) | 73.5% (abstract) | No | EFRame 73.40 | Different pipeline (cold start + RL); a missing comparison at most MAJOR; not an under-reported baseline |
| MathVista | VL-Rethinker (arXiv 2504.08837, recent preprint) | n/a in abstract | Cited, not in Table 1 | n/a | Worth discussing only |

### Field snapshot (as of 2025-09-24)
Three years ago RL for LLMs meant PPO-based RLHF for preference alignment. DeepSeekMath's GRPO and DeepSeek-R1 moved the field to critic-free group-relative RLVR in 2025. Since then dozens of GRPO variants have addressed the same three problems this paper names: zero-advantage groups (dynamic sampling, selective rollouts), entropy collapse (clip-higher, entropy-covariance regularizers), and sample efficiency (difficulty-aware selection, replay). Multimodal math RLVR with Qwen2.5-VL-7B on MathVista/MathVerse/MathVision/We-Math is a crowded, benchmark-saturating setting where several 7B systems already sit within ~1–3 points of each other. In that setting, a +1-point average over a tuned GRPO is incremental; significant contributions show a new capability (e.g., pass@k beyond the base model), equal accuracy at a fraction of the compute, or a verified mechanism. I scored Novelty and Significance against this bar.

---

## Missing References
*Verified with `related_search.py verify`/search unless marked; all prior-labelled items found are ≤ cutoff.*

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Mengqi Liao et al., "Enhancing Efficiency and Exploration in Reinforcement Learning for LLMs", EMNLP 2025 (arXiv 2505.18573, prior peer-reviewed) | Difficulty-based rollout allocation plus entropy-stabilizing temperature; same problem as C1 |
| Important | Yifan Sun et al., "Improving Data Efficiency for LLM Reinforcement Fine-tuning Through Difficulty-targeted Online Data Selection and Rollout Replay", NeurIPS 2025 (arXiv 2506.05316) | Online difficulty-aware selection and rollout replay; closest to C2/C3 |
| Important | Ganqu Cui et al., "The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models", 2025 (arXiv 2505.22617; recent preprint, source check for Thm 4.5; verify that its statement matches) | Archival source for the entropy–covariance relation used in Thm 4.5 |
| Important | Wenxuan Huang et al., "Vision-R1: Incentivizing Reasoning Capability in Multimodal Large Language Models", 2025 (arXiv 2503.06749, prior peer-reviewed) | 7B multimodal RL baseline on the same benchmarks |
| Helpful | Siheng Li et al., "RePO: Replay-Enhanced Policy Optimization", 2025 (arXiv 2506.09340, recent preprint; discuss only) | Replay for GRPO |
| Helpful | Haizhong Zheng et al., "Act Only When It Pays: Efficient Reinforcement Learning for LLM Reasoning via Selective Rollouts", 2025 (arXiv 2506.02177, recent preprint; discuss only) | Skipping uninformative prompts before rollout |

---

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Theory is heuristic and ablations unisolated |
| Clarity | 2 | Positioning against closest work missing |
| Significance | 2 | Crowded setting, modest margins |
| Originality | 2 | Combination of three known components |

## Dimension Scores (0–100)

**Pool position:** better than about 35% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: each of the three components has peer-reviewed prior art that the paper does not cite, and the empirical margin over a tuned GRPO is small in a saturated setting.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Entropy argument is outside the theorem's assumptions |
| Clarity & Presentation | 54 | Competent | Positioning paragraph is a list; broken citation |
| Novelty & Originality | 42 | Developing | C1 incremental, C2/C3 medium |
| Significance & Impact | 50 | Developing | Useful recipe; limited incremental impact |
| Experimental Validation | 48 | Developing | Only DAPO/GRPO as RL baselines |
| Reproducibility | 52 | Developing | Hyperparameters listed; code promised |
| Ethical Compliance | 62 | Competent | Nothing at stake |

---

## Questions for Authors
1. How does EFRame differ from dynamic rollout allocation by difficulty (Liao et al.) and from difficulty-targeted selection with rollout replay (Sun et al.)? A concrete, tested difference would raise my novelty score.
2. Do the replayed high-advantage samples include negatives (see §5.1)? If so, is the "replay serves to reduce entropy" argument still the same?
3. Why is discarding hard-prompt negatives compatible with Zhu et al., which you cite for the usefulness of negatives?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially (App. B only; no discussion of prior art overlap or failure cases).

## Ethics Review Flag
**No**.

## Overall Score
**3**: A reasonable engineering combination with a plausible entropy story, but with uncited close prior art for each component and a small margin over GRPO.

## Confidence
**4**: Literature check supports the novelty profile; arXiv-only search.

---

# Peer Review Report

## Paper: EFRame: Deeper Reasoning via Exploration-Filter-Replay Reinforcement Learning Framework
## Reviewer: Dr. Camila Ferreyra-Holt, Perspective (operations research and control department, South America; fictional persona)
## Expertise: classical RL (exploration, experience replay); stochastic optimization
## Date: 2026-11-05

---

## Summary
The paper treats a known difficulty of sparse-reward RL, learning from rare successes, and brings classical remedies (more exploration where the agent fails, discarding uninformative or harmful data, prioritized replay of rare high-return experience) into GRPO training of a vision-language model. It reports large in-domain gains on Geometry3K and gains over the base model on four math benchmarks, plus an entropy-dynamics explanation.

---

## Strengths

### S1: Good fit with classical RL intuition
Reusing rare successful trajectories with prioritization by advantage magnitude (§4.4, §5.1 "absolute advantage larger than 1") is a direct descendant of prioritized experience replay. The paper applies it where RLVR genuinely lacks signal: prompts with an all-fail group (Def. 4.1). This is a sensible bridge between fields.

### S2: Cost-aware practical value
Table 2 shows ×1.35 time per step, and the recipe fits 8 A800 40GB GPUs (§5.1). A lab with a single node could adopt it. The fact that the improvement on Geometry3K is large (38.44 → 55.24) suggests real value for narrow, hard-prompt-heavy domains.

### S3: A useful taxonomy of samples
The regular / high-quality / low-quality split (§1) gives practitioners a vocabulary for what to log and filter during RL training, and App. A on reward design is a practical warning for anyone adding length or format rewards.

### S4: Candid on sensitivity
App. B states the method is sensitive to clip-higher, buffer size and replay frequency and less effective on simpler datasets. This is the kind of candour deployment readers need.

---

## Weaknesses

### W1: Assumptions behind the entropy story go unexamined
Three assumptions carry the argument. (i) Thm 4.5 is for a tabular softmax policy with exact NPG; the paper applies it to a 7B network with PPO-clip and token-level loss (§4.5, §5.1). (ii) Replayed samples are treated as if they are on-policy with fresh advantages, but stale advantages and importance ratios change the covariance term; replay in classical RL typically needs off-policy corrections. (iii) "Hard prompt" is defined by 5 failed samples (Def. 4.1), which is a noisy estimate: a prompt with p=0.1 success fails all 5 draws about 59% of the time, so the "hard" set mixes truly unsolvable prompts and merely unlucky ones, and the extra-rollout cost is mostly spent filtering them (§4.3: over 95% of exploration samples discarded).
- **Suggested Fix**: Report the fraction of hard prompts that ever yield a positive in G2=20; log Cov(log π, A) with and without replay; consider adaptive G1 or a success-probability estimate.

### W2: Generality is untested beyond one model, one data family
All experiments use Qwen2.5-VL-7B-Instruct on geometry/diagram math (§5.1). The introduction frames the method for "large language models" and "mathematical reasoning benchmarks" ("range of multimodal and mathematical reasoning benchmarks", §1), but no text-only math benchmark (e.g., MATH500, AIME) or other backbone/size appears, even though App. B reports results exist for "simple datasets such as Math" that are not shown.
- **Suggested Fix**: Add one text-only math result and one other backbone, or restrict the claims to this setting; include the "Math" result mentioned in App. B.

### W3: Replay with rare samples raises memorization and overfitting risks that are not examined
With ~1 positive among 20 samples on a hard training prompt (over 95% of exploration samples filtered, §4.3) and replay every 5 steps from a 5120-sample buffer, the model sees a few solutions to the same hard training problems repeatedly. On Geometry3K (a small training set) large in-domain gains may partly reflect memorizing training problems that resemble test problems; App. B itself says gradients must lie "between underfitting, proper fitting, and overfitting". Table 1 would address this, but its training set is not stated.
- **Suggested Fix**: State which training set produced Table 1; report train-test duplication checks for Geometry3K (near-duplicate diagrams), and a learning curve vs. replay count.

### W4: Practical deployment issues are not discussed
Variable per-step time (hard-prompt fraction changes over training), memory for the buffer, and the interaction with large rollout batches (512 prompts × 5) are not discussed; the paper reports one average time per step (Table 2).
- **Suggested Fix**: Plot step time and fraction of hard prompts over training.

### Cross-disciplinary connections
Prioritized experience replay and importance-weighted off-policy correction (Retrace/V-trace-style corrections) from deep RL; "hard example mining" and curriculum design from supervised learning; rare-event sampling from simulation. Named as method families only.

---

## Missing References
*(Method families only; no specific papers asserted.)* Prioritized experience replay and importance-corrected off-policy actor-critic methods from deep RL; curriculum learning by success probability.

---

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Assumptions untested |
| Clarity | 2 | Fine for an RL reader; protocol gaps |
| Significance | 2 | Practically useful for narrow domains |
| Originality | 2 | Known ideas applied |

## Dimension Scores (0–100)

**Pool position:** better than about 55% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a simple, cheap recipe with a large in-domain gain and honest sensitivity notes, balanced against untested assumptions and a single backbone.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Reasonable design; assumptions untested |
| Clarity & Presentation | 56 | Competent | Readable; rough edges |
| Novelty & Originality | 50 | Developing | Classical ideas in a new setting |
| Significance & Impact | 58 | Competent | Practical for hard-prompt domains |
| Experimental Validation | 50 | Developing | One backbone, narrow data |
| Reproducibility | 58 | Competent | Hyperparameters and code promised |
| Ethical Compliance | 64 | Competent | Nothing at stake; limitations noted |

---

## Questions for Authors
1. What fraction of hard prompts yield a positive in G2=20, and how does it change over training? (A low fraction would lower my significance score.)
2. How do results change with a different backbone or a text-only math set?
3. Is there overlap between Geometry3K training and test problems that replay could exploit?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No**.

## Overall Score
**3**: Practically interesting and cheap, but generality and the mechanism are untested; I lean towards reject for this draft with a clear path to acceptance.

## Confidence
**3**: I am a classical-RL reader and did not check the multimodal benchmark protocols.

---

# Peer Review Report

## Paper: EFRame: Deeper Reasoning via Exploration-Filter-Replay Reinforcement Learning Framework
## Reviewer: Dr. Jun-seo Marlowe, Generalist (multimodal learning group, mid-size university, East Asia; fictional persona)
## Expertise: vision-language models; general deep learning
## Date: 2026-11-05

---

## Summary
EFRame adds extra sampling for hard prompts, positive-only filtering, and sample replay to GRPO. On Qwen2.5-VL-7B it improves over the base model on Geometry3K (+16.80) and on four multimodal math benchmarks (+5.66 average), and compared with GRPO and DAPO under the same framework it does better on average, at ×1.35 the time of GRPO.

**Contribution in one paragraph (my words):** a practical training recipe that gives GRPO more signal on hard prompts while trying to keep entropy under control; the paper's insight is that high-advantage rare samples must be reused, and that negative samples from hard prompts are harmful.

---

## Strengths

### S1: Clear motivation with a concrete problem statement
§1 and §3.2 explain the vanishing-advantage problem simply, and Fig. 1/Fig. 2 captions summarise the sample-efficiency and collapse issues in a way a non-specialist can follow.

### S2: Reasonable evaluation breadth for the multimodal side
Table 1 covers four benchmarks and compares with closed and open 7B models, and Table 2 adds a controlled comparison with GRPO/DAPO on the in-domain set. Reporting average and per-benchmark deltas is easy to read.

### S3: Cost reported next to accuracy
Table 2's time/step row is a good practice and lets readers see the price of the method.

### S4: The ablation section mirrors the three components
§6.1–6.3 make each component's role easy to find (Claims 1–3).

---

## Weaknesses

### W1: The evidence supports "a modest, plausible improvement" more than the framing "deeper reasoning" and "complete and stable learning cycle"
Against the closest controlled baselines the gain is +0.94 average (Table 1: 55.13 vs 54.19) and EFRame is below GRPO on MathVision (28.82 vs 29.11). The title, abstract and conclusion (§7: a shift "toward a more structured and reliable process of reinforcement learning") are broader than what a single-seed table shows. The 36.5% and 19.9% figures are ratios of gains over the base model, not accuracy gaps (Table 2: +4.49 points over GRPO).
- **Suggested Fix**: Report absolute margins in the abstract/intro; soften "deeper reasoning" unless pass@k evidence is added.

### W2: Presentation of the method and theory has gaps for a general reader
Thm 4.4 (advantages sum to zero within a group) is an elementary identity presented as a theorem; Thm 4.5 is attributed to a blog post and "extended by ?" (§4.5); Def. 4.1 and Defs 4.2–4.3 are hard to parse after extraction (I treat this as unverifiable). §5.1 does not say which training set produced Table 1 or the evaluation protocol. Figures carry most of the training-dynamics claims (Figs. 2, 4, 5), and their captions are evaluative ("our method not only achieves excellent performance but also demonstrates superior exploration capability", Fig. 4) rather than descriptive.
- **Suggested Fix**: Fix the citation, state the protocol, and add a table with the numbers that the figures show.

### W3: Venue fit is fine, but the bar at ICLR for a GRPO variant is high
ICLR has received many GRPO-variant submissions; accepted ones usually show one of: a mechanism measured directly, matched-compute wins, or gains across models/tasks. Here the experiments use one backbone and one data family (§5.1).
- **Suggested Fix**: See R1/R3: matched baselines, seeds, a second backbone.

**Minor**: typos ("challanging", "distorb", "avail able", "aand"); duplicated DPO reference; "DeepSeek-R1 introduced ... GRPO" in §1; "Skywork R1V" listed as 38B in Table 1 and "Skywork R1V-32B" in §5.1 (text vs table size mismatch: 38B vs 32B).

### Venue criteria checklist (ICLR)
| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness (claims supported) | Partly | Tables 1–2; mechanism untested |
| Presentation | Partly | broken citation, missing protocol |
| Contribution (significance/novelty) | Partly | components have prior art |
| Reproducibility | Partly | hyperparameters given; steps/β/seeds missing |
| Honest limitations | Partly | App. B |

---

## Missing References
*(Domain Reviewer owns this section.)*

---

## NeurIPS-Style Scores
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Single runs, partial baselines |
| Clarity | 2 | Understandable; gaps |
| Significance | 2 | Modest |
| Originality | 2 | Combination of known parts |

## Dimension Scores (0–100)

**Pool position:** better than about 42% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the recipe is clear and the in-domain gain is large, but the headline margin over the strongest controlled baseline is small and the framing overshoots the evidence.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 52 | Developing | Mechanism not measured |
| Clarity & Presentation | 52 | Developing | Missing protocol, broken citation, evaluative captions |
| Novelty & Originality | 46 | Developing | Components known |
| Significance & Impact | 52 | Developing | Practical value, modest margin |
| Experimental Validation | 46 | Developing | One backbone, single runs |
| Reproducibility | 54 | Developing | Code promised, details partial |
| Ethical Compliance | 60 | Competent | Nothing at stake |

---

## Questions for Authors
1. Can you give a table with final numbers behind Figs. 4–5 and state the number of runs? (Clear numbers with seeds could raise my score.)
2. Is Skywork R1V 32B or 38B in Table 1?
3. Which training set produced Table 1?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No**.

## Overall Score
**3**: A clear recipe whose evidence is thinner than its framing; reasons to reject slightly outweigh reasons to accept for this draft.

## Confidence
**3**: Generalist reading; the RL theory was not checked line by line.

---

# Devil's Advocate Report

## Paper: EFRame: Deeper Reasoning via Exploration-Filter-Replay Reinforcement Learning Framework
## Reviewer: Dr. Oluwaseun Brandt (industrial research lab, West Africa / North America; fictional persona)

---

## Steelman
The paper identifies a genuine failure of GRPO (all-fail prompts give no gradient), proposes an inexpensive fix (targeted extra sampling, positive-only filtering, replay), and shows a large in-domain gain (38.44 → 55.24, Table 2) with a modest out-of-domain gain over both the base model and GRPO/DAPO (Table 1). The entropy story offers a coherent explanation of why the pieces belong together.

---

## Core Argument Chain
1. GRPO gets no learning signal on prompts where all sampled responses fail (§1, §3.2).
2. Extra high-temperature sampling on those prompts finds rare correct responses (§4.2).
3. Negative samples from those prompts are noise and are harmful; positives are valuable (§4.3, Claim 2).
4. Rare positives cause entropy spikes and instability unless replayed, which restores entropy to a stable level (§4.4–4.5, Claim 3).
5. Therefore the combination of exploration, filtering and replay improves performance and unlocks reasoning unreachable by GRPO (Abstract, Tables 1–2).
∴ EFRame is a more stable, efficient and deeper-reasoning RLVR method than GRPO.

---

## Strongest Counter-Argument
Even if every number in Tables 1–2 is right, the paper does not show that EFRame's three components are what produce the gain, nor that the gain is more than extra compute and extra gradient steps on a single seed. First, the comparison is between a method that draws up to 25 samples on hard prompts and replays stored samples (an extra gradient exposure per sample) against GRPO at G=5 with no matched-budget control. The paper's own Fig. 1 caption says that raising GRPO's G to 20 already "provides a performance improvement" at four times the per-step cost; the fair question is where EFRame at ×1.35 sits relative to GRPO at matched samples and matched updates, and relative to DAPO with its actual dynamic sampling (the DAPO row is described as ε_high=0.3 plus a length penalty, §5.1). Second, the margin over the best same-framework baseline on the out-of-domain average is +0.68 (55.13 vs DAPO 54.45; derived) to +0.94 (vs GRPO), with a loss on MathVision to GRPO, and there is not a single seed or interval. Third, the causal story about entropy is told in an unverified theorem for tabular policies and never measured; the text even treats rising entropy as a collapse symptom in §3.2 ("sudden spikes in both gradient and policy entropy") and as a feature of EFRame in §5.2 ("our method further increases entropy to encourage continued exploration"). Finally, the "deeper reasoning" claim is a claim about the reachable set of solutions, the paper's own reference point is pass@k, and pass@k is never reported. A reader could reasonably conclude that EFRame is a well-tuned GRPO variant with more compute on hard prompts and a heuristic story attached.

---

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The core claim survives in a weaker form: the evidence supports "better pass@1 than same-framework GRPO/DAPO on one model, at 1.35× step time", which is a narrower claim, not a contradicted one; no leakage is stated (the protocol is simply not stated, which is a MAJOR question).

| # | Dimension | Location | Issue | Suggested Fix | Resolvable by |
|---|-----------|----------|-------|---------------|---------------|
| – | – | – | none | – | – |

### MAJOR Issues
| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Evidence | Tables 1–2, §5.1, Fig. 1 caption | No compute-matched GRPO and a partial DAPO; gain could be extra samples/updates | Matched-sample and matched-wall-clock GRPO, full DAPO |
| DA-M2 | Evidence | Tables 1–2, §5.2 | Single runs; Table 1 margin vs GRPO +0.94 average and −0.29 on MathVision | Seeds or paired bootstrap |
| DA-M3 | Scope | Abstract, §4.2, §5.2 | "Deeper reasoning" and "aha moment" frequency never measured; length growth read as reasoning gain | pass@k and solved-prompt analysis, or narrow wording |
| DA-M4 | Logic | §4.5, Thm 4.5, §3.2 vs §5.2 | Tabular theorem used for a 7B PPO-clip system with replay; entropy rise is both a collapse symptom (§3.2) and a feature (§5.2) | Measure Cov(log π, A); reconcile the narrative |
| DA-M5 | Logic | §4.3, §6.2, §1 | "Negatives from hard prompts are harmful" not isolated; tension with the cited Zhu et al. | Variant keeping/down-weighting negatives |
| DA-M6 | Protocol | §5.1, Tables 1–2 | Eval split, training set for Table 1, steps, β, checkpoint, decoding not stated; baseline provenance unknown | Full protocol statement |
| DA-M7 | Scope | §1, App. B | Generality ("LLMs", "mathematical reasoning") rests on one backbone; App. B mentions unreported "Math" results | Second backbone or text-only math; report App. B results |

### MINOR Issues
| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Presentation | §4.5 | "extended by ?" broken citation; blog as theorem source |
| DA-m2 | Citation | §1 vs §2, ref list | GRPO attributed to DeepSeek-R1 in §1; DPO duplicated |
| DA-m3 | Numbers | Table 2 | ×0.57 should be ×0.56 |
| DA-m4 | Numbers | Table 1 vs §5.1 | Skywork R1V 38B vs "R1V-32B" |

---

## Numerical Sanity Check
| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Avg gain over base (Table 1) | +5.66 | 55.13 − 49.47 = 5.66 | Yes |
| Ours avg | 55.13 | (28.82+48.81+73.40+69.48)/4 = 55.1275 | Yes |
| GRPO avg | 54.19 | (29.11+47.51+72.60+67.53)/4 = 54.1875 | Yes |
| "outperforming GRPO by 19.9%" | 19.9% | 5.66/4.72 = 1.199 (ratio of gains; accuracy gap is +0.94) | Arithmetic yes; framing misleading |
| Geo3K gain over base | +16.80 | 55.24 − 38.44 = 16.80 | Yes |
| "36.5% relative advantage" | 36.5% | 16.80/12.31 = 1.365 (ratio of gains; accuracy gap 4.49 points = 8.8%) | Arithmetic yes; framing misleading |
| Time ratio EFRame | ×1.35 | 442/327 = 1.352 | Yes |
| Time ratio DAPO | ×0.57 | 182/327 = 0.557 → ×0.56 | Off by rounding |

## Ignored Alternative Explanations
Extra samples/updates (compute) rather than component design; lucky seed; Geometry3K train–test similarity amplified by replay; the length penalty and binary-reward difference in the DAPO baseline making it weaker; evaluation-protocol differences explaining Table 1 rows copied from other papers.

## Missing Stakeholder Perspectives
Practitioners who must run this on other models or with larger rollout batches: no per-step cost profile beyond one average; no failure cases (when hard prompts are truly unsolvable and 20 extra samples are wasted).

## Observations (Non-Defects)
The arithmetic in Tables 1–2 is internally consistent; cost is reported; the paper openly states hyperparameter sensitivity (App. B) and that gains are smaller on easy data; the recipe is specified well enough to implement.

---

## Dimension Scores (0–100)
| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 44 | Mechanism unmeasured, theorem misapplied |
| Clarity & Presentation | 52 | Understandable; missing protocol |
| Novelty & Originality | 38 | Components known |
| Significance & Impact | 42 | Small margin in crowded setting |
| Experimental Validation | 38 | Single runs, unmatched baselines |
| Reproducibility | 48 | Key details missing |
| Ethical Compliance | 58 | Nothing at stake |

**Pool position:** better than about 25% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the main claim is not tested by a compute-matched, multi-seed comparison and the mechanism is untested.

## Overall: 2 | Confidence: 4

---

## Phase 1.6: Report Check (Synthesizer, Step 0)

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | ε inconsistency (ERR-2) | rewritten (confidence lowered to Medium, severity MINOR) | Could be read as "clip-higher value is 0.2"; kept as a question-grade error |
| R1 | "No code" note | dropped | Abstract says code is available (link removed in blinded text) |
| R2 | "C1 is already done by Liao et al." | rewritten | The Liao et al. abstract describes difficulty-based rollout budgets and temperature adjustment, not positive-only filtering or replay: "incremental", not "known" |
| R2 | Zhu et al. "contradicts the paper" | rewritten as tension + question | The paper's claim is limited to hard-prompt negatives |
| R3 | "Broader impact missing" | dropped | Nothing at stake; Ethics scored on limitations |
| R4 | Typos, duplicated DPO entry | moved to Minor | Cosmetic |
| R4 | "Skywork 38B vs 32B" | kept (Minor) | Table 1 says 38B, §5.1 says R1V-32B |
| DA | DA-M4 entropy narrative | kept | §3.2 and §5.2 quotes verified |

Scores were not changed.

## Phase 2: Synthesizer Package (Part A)

**Issue list and classes.** 
| Issue | Sources | Class |
|-------|---------|-------|
| No compute-matched / partial DAPO baselines | R1-W2, DA-M1, R4-W3 | CONSENSUS-3 |
| Single runs, small/unverified margin, misleading 36.5%/19.9% | R1-W1, R4-W1, DA-M2 | CONSENSUS-3 |
| "Deeper reasoning" unmeasured | R1-W3, R4-W1, DA-M3 | CONSENSUS-3 |
| Theory heuristic/misapplied, broken citation | R1 ERR-4, R2-W2, R3-W1, DA-M4, R4-W2 | CONSENSUS-4 |
| Protocol under-specified | R1-W5, R4-Q, DA-M6, R3-W3 | CONSENSUS-3 |
| Ablation confounds / negatives claim | R1-W4, R2-W3, DA-M5 | CONSENSUS-3 |
| Uncited prior art for each component | R2-W1 | SOLO |
| Generality (one backbone, App. B unreported results) | R3-W2, DA-M7 | CONSENSUS-2 |
| Replay content/ε inconsistency | R1-W6, R2-Q2 | CONSENSUS-2 |
| DA-CRITICAL | none | – |

**Hinges:** headline margin and compute matching (R1-W1/W2), the "deeper reasoning" wording, and R2's novelty finding.

**Official output (from `scores_before.json`)**: ratings R1 3, R2 3, R3 3, R4 3, DA 2 → mean 2.80; official composite 50.1; per-dimension spreads ≤ 16 (no ⚠). Composite band 2 vs rating-based 3: flagged.

---

# Editorial Decision

## Paper: EFRame: Deeper Reasoning via Exploration-Filter-Replay Reinforcement Learning Framework
## Submission ID: iclr26-AIKURJjxXT
## Date: 2026-11-05
## Target Venue: ICLR | Paper Type: empirical
## Review Team (fictional personas): EIC (meta-reviewer) Prof. Ingrid Valtonen-Okafor; R1 Methodology Dr. Tomasz Reinholt, R2 Domain Dr. Priyanka Anand-Voss, R3 Perspective Dr. Camila Ferreyra-Holt, R4 Generalist Dr. Jun-seo Marlowe, DA Dr. Oluwaseun Brandt

---

## Decision: Borderline Reject (3), ICLR rating 4 on {0,2,4,6,8,10} (secondary scale label; 5 on the older {1,3,5,6,8,10} scale)

**Official ratings** (shown to authors): R1 3, R2 3, R3 3, R4 3, DA 2 → mean 2.80 · official composite 50.1
**EIC assessment** (internal): weighted rating 2.84 → starting point 3 · weighted composite 50.2 → band 3 (cross-check agrees; ICLR-weighted composite 50.0) · **DA ceiling**: none · **Final (EIC)**: 3
**Journal recommendation**: n/a (conference target)

---

## EIC Meta-Review

### The Case For and Against
- **For acceptance:** A simple, cheap recipe (×1.35 step time) addresses a real GRPO failure (no signal on all-fail prompts), with a large in-domain gain (38.44 → 55.24 on Geometry3K, Table 2) and a consistent gain over the base model on four multimodal benchmarks (Table 1), and the paper is candid about hyperparameter sensitivity (App. B).
- **Against acceptance:** The margin over the best same-framework baseline is small and single-run (+0.94 average vs GRPO, −0.29 on MathVision), the baselines are neither compute-matched nor complete (partial DAPO), the "deeper reasoning" and entropy-mechanism claims are not measured, each component has uncited peer-reviewed prior art, and the protocol is under-specified.

### Verification of Decisive Points (EIC read of the paper)
| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| 36.5% and 19.9% are ratios of gains over base, not accuracy gaps | R1 ERR-1, R4-W1, DA | Table 2, Table 1, §1, §5.2 | **Verified** | 55.24 vs 50.75 = +4.49 points; 55.13 vs 54.19 = +0.94. Numbers correct, framing misleading |
| No seeds/runs; margin inside plausible noise | R1-W1, DA-M2 | Tables 1–2 | **Verified** | Searched the full text: no seeds, intervals or run counts |
| Baselines not compute-matched; DAPO partial | R1-W2, DA-M1 | §5.1, Table 2, Fig. 1 caption | **Verified** | DAPO described as ε_high=0.3 plus length penalty; no matched-G GRPO row (Fig. 1 contents not visible) |
| "Deeper reasoning" unmeasured (no pass@k) | R1-W3, DA-M3 | Abstract, §4.2, §5.2 | **Verified** | Only pass@1 accuracy and curves; length growth read as reasoning |
| Thm 4.5 applicability; broken citation; blog source | R1 ERR-4, R2-W2, DA-M4 | §4.5 | **Verified** | Quote "organized and extended by ?" present; theorem assumptions (tabular softmax, NPG) vs §5.1 setup |
| Entropy rise framed as collapse sign (§3.2) and as feature (§5.2) | DA-M4 | §3.2, §5.2 | **Verified** | Both quotes present; may be reconcilable (spike vs sustained level) but not reconciled |
| Replay buffer content: |Â|>1 admits negatives | R1 ERR-3 | §4.4 vs §5.1 | **Partly correct** | Derivation is right for binary rewards; whether negatives are actually stored depends on code not available |
| ε_low=ε_high inconsistent with "clip higher" | R1 ERR-2 | §5.1, App. B | **Partly correct** | Textual tension, but "clip higher" could mean value 0.2; MINOR |
| C1 "known" via Liao et al. | R2-W1 | Literature check | **Partly correct** | Abstract shows overlapping idea (difficulty-based rollouts, entropy-stabilizing temperature) but not positive-only filtering/replay: incremental, not known |
| Negative-sample claim in tension with Zhu et al. | R2-W3, DA-M5 | §1, §4.3, §6.2 | **Partly correct** | Tension real; paper's claim restricted to hard-prompt negatives, untested |
| Time ratios | R1 ERR-5 | Table 2 | **Verified** | 182/327 = 0.557 (×0.56); trivial |
| Skywork 38B vs 32B | R4 | Table 1, §5.1 | **Verified** | "38B" in Table 1, "R1V-32B" in §5.1; trivial |
| R3: "large in-domain gain suggests real value for narrow domains" | R3-S2 | Table 2 | **Partly correct** | The gain is real vs base; vs GRPO it is +4.49 points on one run |

No integrity concern was found in the text. The text-overlap flag (2 shared 8-grams, generic sentence) is not an integrity concern. High conceptual overlap (cosine 0.30) with a concurrent preprint on data efficiency in RLVR is "worth discussing" only and affects no score.

### Reviewer Weights
| Reviewer | Overall | Confidence | EIC quality weight (0.5–1.5) | Reason |
|----------|---------|------------|------------------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Recomputations verified; compute-matching and protocol findings verified; one error (ERR-2) only partly correct |
| R2 (Domain) | 3 | 4 | 1.0 | Literature findings verified against abstracts; "incremental" verdict correctly hedged |
| R3 (Perspective) | 3 | 3 | 1.0 | Sound but partly generic; several concerns duplicate R1 |
| R4 (Generalist) | 3 | 3 | 1.0 | Fair, well calibrated; minor catches verified |
| DA | 2 | 4 | 0.75 | Arguments mostly verified, but Overall 2 / pool 25 is harsher than the evidence (real in-domain gain, no leakage or contradiction), so the rating is calibrated low for this venue |

### DA-CRITICAL Rulings
| Issue | AC test: fatal on its own? | Ruling | Resolvable by |
|-------|---------------------------|--------|---------------|
| none raised | n/a | n/a | n/a |

### Final Decision and Justification
The EIC-weighted rating is 2.84, rounded to 3 (Borderline Reject), and I keep it. The composite cross-check agrees: the EIC-weighted composite is 50.2 (band 3), though it sits only 0.2 points above the band 2/3 edge (the unweighted panel composite before weighting was 49.9, band 2), which I read as a borderline signal on the low side of 3; it is not a reason to depart. No ratings rest on a claim I found incorrect, and I verified no issue that the ratings overlooked: every verified issue (small single-run margin, unmatched baselines, unmeasured mechanism, under-specified protocol, uncited prior art) is already reflected in the 3's. There is no DA ceiling (no upheld CRITICAL issue). My own pool position is **about 40%**: a typical rejected submission with an above-median in-domain result. The deciding evidence is that the main claim over GRPO rests on a +0.94 average margin from one run per method, not compute-matched, while the genuine strengths (large Geometry3K gain, cheap recipe, honest sensitivity note) are the kind a rebuttal with seeds, matched baselines and pass@k could convert. Most issues are fixable without new ideas, which is why I rank this near the top of the reject band and not lower.

---

## Score Summary

### Official Scores and EIC Assessment
(Per-dimension tables below are from `aggregate.json`; official = plain mean.)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) |
|-----------|----|----|----|----|----|---------------------|
| Technical Rigor | 50 | 52 | 56 | 52 | 44 | 50.8 |
| Clarity & Presentation | 55 | 54 | 56 | 52 | 52 | 53.8 |
| Novelty & Originality | 45 | 42 | 50 | 46 | 38 | 44.2 |
| Significance & Impact | 50 | 50 | 58 | 52 | 42 | 50.4 |
| Experimental Validation | 44 | 48 | 50 | 46 | 38 | 45.2 |
| Reproducibility | 50 | 52 | 58 | 54 | 48 | 52.4 |
| Ethical Compliance | 62 | 62 | 64 | 60 | 58 | 61.2 |
| **Composite** | 49.8 | 50.6 | 55.2 | 50.9 | 44.2 | **50.1 (before)** / **50.2 (after, EIC-weighted)** |

### Target-Venue Scores (ICLR, scale status: secondary)
ICLR-weighted composite 50.0 · Soundness 2 · Presentation 2 · Contribution 2 (1–4); rating 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}), from `aggregate.json --final 3`. Reviewer weight shares: R1 0.269, R2 0.215, R3 0.177, R4 0.177, DA 0.161. No consistency warnings.

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "EFRame: Deeper Reasoning via Exploration-Filter-Replay Reinforcement Learning Framework" to ICLR. The problem, learning signal from prompts a GRPO policy never solves, is a real and timely one.

**Overall Assessment:** The panel found a clearly described, inexpensive recipe with a large in-domain gain, but judged that the evidence does not yet show that the gain over a tuned GRPO comes from the three components rather than from extra compute, or that it reflects "deeper reasoning".

**Key Strengths Identified by Reviewers:**
1. A clear, implementable recipe with reported cost (R1, R3, R4).
2. A large in-domain gain on Geometry3K (38.44 → 55.24, Table 2) (R1, R3).
3. A useful diagnosis of GRPO's vanishing-advantage problem and a practical note on reward design (R2, R3).

**Key Concerns Requiring Attention:**
1. Margins over GRPO/DAPO are small, from single runs, and the 36.5% / 19.9% figures are ratios of gains over the base model (CONSENSUS-3).
2. No compute-matched GRPO and only a partial DAPO baseline (CONSENSUS-3).
3. The "deeper reasoning" and entropy-mechanism claims are not measured; Thm 4.5 does not cover the setting (CONSENSUS-3/4).
4. Each component has close prior art not cited (R2, SOLO).

**Decision: Borderline Reject (3).** Reasons to reject outweigh reasons to accept for this draft: the central comparison with GRPO is not controlled for compute, has no variance estimate, and the mechanism claims are asserted rather than measured. A revision with matched baselines, seeds, pass@k analysis, a full protocol statement and positioning against the closest prior work could change the outcome.

Please refer to the Revision Roadmap below.

Sincerely,
Prof. Ingrid Valtonen-Okafor
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Theory heuristic/misapplied; broken citation | R1, R2, R3, R4, DA | CONSENSUS-4 |
| Small, single-run margin; misleading 36.5% / 19.9% | R1, R4, DA | CONSENSUS-3 |
| Baselines not compute-matched; partial DAPO | R1, R4, DA | CONSENSUS-3 |
| "Deeper reasoning" unmeasured | R1, R4, DA | CONSENSUS-3 |
| Protocol under-specified | R1, R3, R4, DA | CONSENSUS-3+ |
| Ablation confounds / negatives claim | R1, R2, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Overall severity | R3 (practical value; pool 55) | DA (pool 25) | Evidence supports the middle: real in-domain gain, uncontrolled main comparison |
| Is C1 prior art decisive? | R2 (incremental, Critical missing ref) | DA (did not raise as CRITICAL) | Incremental, not known; MAJOR at most |

### Score Spread Discussion
No dimension exceeds the 20-point spread flag. Pool positions differ by 30 points (R3 55 vs DA 25); the evidence behind it is R3's weight on practicality vs DA's weight on the uncontrolled comparison; I rule for the uncontrolled comparison being a real weakness (verified) but not fatal.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Compute-matched baselines | Yes (R1) | n/a | n/a |
| DA-M2 | MAJOR | Single runs | Yes (R1, R4) | n/a | n/a |
| DA-M3 | MAJOR | "Deeper reasoning" unmeasured | Yes (R1, R4) | n/a | n/a |
| DA-M4 | MAJOR | Theorem misapplied; entropy narrative | Yes (R1, R2, R3) | n/a | n/a |
| DA-M5 | MAJOR | Negatives claim | Yes (R2) | n/a | n/a |
| DA-M6 | MAJOR | Protocol | Yes (R1) | n/a | n/a |
| DA-M7 | MAJOR | Generality | Yes (R3) | n/a | n/a |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | Compute-matched and complete baselines | R1-W2, DA-M1 | Table 2, §5.1, Fig. 1 | GRPO with matched samples/wall-clock; full DAPO (dynamic sampling, binary reward); component-only variants | High; roughly 4–6 extra Geo3K runs on 8 GPUs (hundreds of GPU-hours, my estimate) | Partly |
| R2 | Variance for headline claims | R1-W1, DA-M2, R4-W1 | Tables 1–2 | ≥3 seeds or paired bootstrap; report absolute gains over each baseline | Medium–High; ~6 runs | Partly |
| R3 | Measure or narrow "deeper reasoning" | R1-W3, DA-M3 | Abstract, §4.2, §5.2 | pass@k up to 64–256 vs base/GRPO; solved-prompt analysis; else soften wording | Medium; evaluation only (tens of GPU-hours) | Yes |
| R4 | Correct headline wording | R1 ERR-1, R4-W1 | §1, §5.2, abstract | State absolute gains; define 36.5% / 19.9% as ratios of gains | Low | Yes |
| R5 | Full protocol statement | R1-W5, DA-M6 | §5.1 | Eval split, training set per table, steps, β, checkpoint, decoding, baseline provenance | Low | Yes |

### Priority 2 — Strongly Suggested (Should Fix)
| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Theory vs setting; entropy narrative | R1 ERR-4, R2-W2, R3-W1, DA-M4 | Cite archival source; log Cov(log π, A) with/without replay; reconcile §3.2 vs §5.2 | Medium | Yes |
| S2 | Ablation isolation, table of numbers, 2nd dataset | R1-W4, R2-W3, DA-M5 | Single/pairwise variants; keep-negatives variant | High | Partly |
| S3 | Position against closest prior art | R2-W1 | Add Liao et al., Sun et al., Cui et al. (source check), Vision-R1; discuss RePO, GRESO | Low | Yes |
| S4 | Generality | R3-W2, DA-M7 | Second backbone or text-only math; report App. B "Math" result | High | Partly |
| S5 | Replay content and ε values; hyperparameter sweeps | R1-W6 | State rule and values; sweep clip-higher, buffer, period | Medium | Yes |
| S6 | Hard-prompt statistics, memorization check | R3-W1, R3-W3 | Fraction of hard prompts yielding positives; train–test duplicate check | Low–Medium | Yes |

### Priority 3 — Nice to Fix (Optional)
| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Typos, "?" citation, duplicate DPO, GRPO attribution in §1, ×0.57 → ×0.56, Skywork 38B/32B | R1, R4, DA | Clean-up |
| N2 | Per-step time profile and buffer memory | R3-W4 | Plot over training |
| N3 | Evaluative figure captions | R4-W2 | Descriptive captions plus numbers table |

## Estimated Revision Effort
- Priority 1: 5 items, about 1–2 weeks (two items need new runs)
- Priority 2: 6 items, about 1–2 weeks
- Priority 3: 3 items, about 1 day
- **Total estimated revision time**: roughly 3–4 weeks including new experiments
