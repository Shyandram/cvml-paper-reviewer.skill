# Review Simulation: "Negotiated Reasoning: On Provably Addressing Relative Over-Generalization"

Date: 2026-11-10 · Skill: academic-paper-reviewer 2.10.1 · Mode: full · Target venue: ICLR (profile `iclr`, 2026 cycle) · Literature check: strict, cutoff 2025-09-24

*Simulation, not a prediction: this is how a careful panel would likely see this draft. The five reviewer passes were run one after another in one shared model context (no subagents); the reviewers are fictional personas. Figures were not available (text extraction only): figure-dependent claims are judged from captions and text and marked as such.*

---

## Phase 0: Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | Negotiated Reasoning: On Provably Addressing Relative Over-Generalization |
| Primary Discipline | Machine learning → cooperative multi-agent reinforcement learning (MARL) |
| Secondary Discipline(s) | Game theory (equilibrium selection), probabilistic inference (Stein variational methods), cognitive science (motivating analogy only) |
| Paper Type | Theoretical (composite weights: theoretical). The headline is "provably", with definitions, theorems and a small empirical section on toy games; the 0–100 composite therefore weights Technical Rigor at 0.30 |
| Core Technique(s) | Maximum-entropy MARL, message-passing Stein variational gradient descent (MPSVGD), amortized SVGD actor, centralized critic (CTDE) |
| Target Venue | ICLR, top-tier ML conference (stated by the user); profile key `iclr` |
| Venue-Specific Notes | none; ICLR rating scale is `secondary` status in the skill, so labels are shown as "as reported for 2026" |
| Paper Maturity | Submission-ready in form; appendix proofs are short sketches |
| Ethics-Relevant Content | none (simulated games only) |

### Claimed Contributions (as stated by the authors, §1 end)
1. **C1**: "We confirm the existence of provably addressing RO methods." Proves RO is avoided under *consistent reasoning* (Defs. 4.1–4.3, Thms 5.1–5.2).
2. **C2**: A novel framework, negotiated reasoning (NR), and its instance SVNR, "the first MARL method that can provably address RO" (§5–§6).
3. **C3**: A practical amortized implementation of SVNR (§7, Algorithm 1) with "superior performance in achieving global optimal cooperation in RO-challenged tasks" (§8).

### Paper memory (factual record, shared with all reviewers)
- **Claims and locations:** C1 §1, Abstract; Defs. 4.1–4.3 (§4); Thm 5.1, 5.2 (§5); proofs C.1, C.2. C2: Eq. 5.1, 5.2, §6.1 Eq. 6.3–6.4, strict nested sets C_i = {1,…,i}. Thm 6.3 (SVNR policy iteration) rests on Lemmas 6.1 and 6.2 (§6.2). C3: Eq. 7.1–7.4, Algorithm 1, Fig. 2.
- **Setup facts:** environments: Max of Three (three agents, 1-D continuous action in [−10, 10], s² ∈ {3.0, 2.0, 1.5}), Two Modalities (§8.1), Particle Gather (four agents, 25 steps, §8.2). Baselines: MADDPG, MASQL, PR2, ROMMEO, Lenient MADRL (§8). Hyperparameters: TPE sampler, 50 trials, ranges given, selected values not stated. Optimizer ADAM, buffer 10⁶, batch 512. Seeds: 5 (Fig. 4 and 6 captions); seeds/episodes for Table 1: not stated. Training budget 5000 episodes. Network architecture, compute/hardware, code link: **not stated after search** (no match for GPU, hidden, layer, architecture, code, wall-clock).
- **Headline numbers:** Table 1 (execution returns): SVNR 9.60±0.30 / 9.64±0.17 / 9.71±0.20 / 4.76±0.20; best baseline per column 9.54±0.13 (L-MADRL) / 1.63±2.51 (L-MADRL) / −0.07±0.04 (L-MADRL) / 0.00±0.00 (MADDPG).
- **Appendix summary:** A (Thm A.1, nested factorization capacity), B.1–B.2 (derivations, headed "Equation 12" and "Equation 9"), C.1–C.7 (proofs; short). No additional experiments.
- **Unverifiable:** Figures 1–7 (not available; judged from captions), Figure 1 payoffs, exact typesetting of Eq. 6.6/7.2/7.4 (extraction is partly garbled but readable).

### Integrity signals
`scripts/integrity_scan.py` found **no** text addressed to reviewers or AI systems (0 findings). Text-overlap check: no 8-gram overlap with any kept abstract. The reviewers read the (unchanged, since nothing was flagged) reviewer copy.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Prof. Elin Vastarien, public research university (Northern Europe)
- **Seniority / Expertise**: senior faculty / cooperative MARL, equilibrium selection in games
- **Role**: reads all five reviews, checks decisive points against the paper, weights the reviewers, decides
- **Style**: area-chair pragmatism: asks whether the central claim is measured and whether the weaknesses are typical of accepted ICLR papers

### Reviewer 1 (Methodology): Dr. Mateo Orsolini, industrial research lab (North America)
- **Seniority / Expertise**: mid-career industry scientist / deep RL evaluation, off-policy actor-critic, MARL benchmarking
- **Review Focus**: design, fairness of comparison, reproducibility, proof checking at the level of derivation steps
- **Style**: reads every equation against its algorithm; insists on matched tuning budgets

### Reviewer 2 (Domain): Prof. Sunita Raghavendran, public research university (South Asia)
- **Seniority / Expertise**: senior faculty / opponent modeling, recursive reasoning, coordination games
- **Review Focus**: literature positioning, theory framing, domain contribution
- **Style**: demands precise differentiation from the closest prior formulations

### Reviewer 3 (Perspective): Dr. Amara Nwosu, research institute (Europe)
- **Seniority / Expertise**: mid-career / sampling and variational inference (Stein methods), statistical physics of learning
- **Review Focus**: cross-disciplinary links (sampling, correlated equilibria, autoregressive models), deployment, assumptions
- **Style**: constructive, looks for what the idea could become

### Reviewer 4 (Generalist): Dr. Yuki Tanabe, university lab (East Asia)
- **Seniority / Expertise**: postdoc / reinforcement learning and generative models, not MARL theory
- **Review Focus**: clarity of contribution, venue fit, presentation
- **Style**: the typical program-committee member; needs the contribution in one paragraph

### Devil's Advocate: Prof. Dmitri Kovalenko, public research university (Eastern Europe)
- **Seniority / Expertise**: senior faculty / evaluation methodology, learning in games
- **Review Focus**: core-argument challenges, logic, overclaiming
- **Style**: rigorous skeptic; fair, never hostile

*Personas are fictional. Assumptions: paper type theoretical; target venue ICLR as stated; strict literature check as of 2025-09-24.*

---

## Phase 1: Independent Reviews

*Sequential role-based passes sharing one model context, not independent agents. Each pass applied its own role file and the shared paper memory.*

---

# Peer Review Report (Reviewer 1)

## Paper: Negotiated Reasoning: On Provably Addressing Relative Over-Generalization
## Reviewer: Dr. Mateo Orsolini, Methodology (industrial research lab, North America; fictional persona)
## Expertise: deep RL evaluation; off-policy actor-critic; MARL benchmarking
## Date: 2026-11-10

---

## Summary
The paper studies relative over-generalization (RO), where cooperating agents settle on a sub-optimal joint action because exploration by others makes the optimal one look bad. It defines perceived and executed variants (PRO, ERO), proposes "consistent reasoning" as a sufficient condition, and builds SVNR: agents sample actions by message-passing SVGD over a nested conditioning structure, learned as a noise-conditioned actor with a centralized soft Q-critic. Experiments on three small, low-dimensional games show SVNR finding the optimum where five older baselines do not.

---

## Protocol sweep and claim-to-evidence map

**Protocol sweep (searched: test, validation, held-out, select, tuned, best, checkpoint).** The only selection statement is §8 Hyperparameters: "based on the maximum mean reward in 50 trails" (TPE sampler over learning rate, particle number, α). The paper reports no separate validation or test protocol; in these stateless or short-horizon games there is no data split, so the selection is on the same environment that is reported. It is not stated whether baselines received the same 50-trial budget ("Other hyperparameters follow the ROMMEO"). Table 1 "execution performances in testings": number of seeds and episodes not stated.

| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | RO is provably avoided under consistent reasoning | Abstract, §1, Thms 5.1–5.2 | Proofs C.1, C.2 | **Partially**: Thm 5.1 assumes its own conclusion; Thm 5.2 needs α→0 and finite/deterministic structure not used in experiments |
| C2 | SVNR "the first MARL method that can provably address RO"; "guaranteed to reach consistent reasoning and optimal cooperation" | §1, §6, Thm 6.3 | Lemmas 6.1–6.2, App. C.4–C.7 | **Partially**: guarantee covers an idealized (finite action set, exact particles) algorithm, not Algorithm 1 |
| C3 | "superiority and efficiency of SVNR" on "many RO-challenged environments" | Abstract, §8 | Table 1, Figs 4–7 | **Partially / Unsupported for efficiency**: three toy settings; no computational measurement anywhere |

## Strengths

### S1: A clear, well-chosen failure mode and a clean separation on it
The PRO/ERO split (Defs. 4.2, 4.1) is a useful way to talk about where RO enters (training vs. execution), and Fig. 1 (caption only; figure unavailable) is described as a minimal two-agent illustration. In §8.1 the Max-of-Three family with a tunable s² gives a controlled difficulty knob, and Table 1 shows baselines near or below 0 where SVNR is near 9.6–9.7 at s² ∈ {2.0, 1.5}: a large effect, far outside the reported spreads.

### S2: Ablation targeting the central design choice
§8.3 compares SVNR (C_i = {1,…,i}), SVNR-F (C_i = −i) and SVNR-M (C_i = {}). The finding that removing conditioning on others' noise (SVNR-M) leaves the agent stuck in RO (Fig. 7, caption and text) directly tests the "agents must condition on each other" idea.

### S3: Honest scalability limitation
§9 states "One main limitation of our SVNR approach is its scalability in scenarios involving many agents", and notes the sparse-structure gap with the nested requirement.

---

## Weaknesses

### W1: The theoretical guarantees do not apply to the experiments or to Algorithm 1
(a) Lemmas 6.1, 6.2 and Thm 6.3 are stated for finite action sets ("|U| < ∞"), while all experiments use "common one-dimension bounded continuous action space of [−10, 10]" (§8.1) and the SVGD direction (Eq. 6.4) needs gradients. (b) Thm 5.2 needs α → 0, but §8 anneals "α = α′ + exp(−0.1 × max(steps − 10, 0)) ∗ 500" with "α′ is the initial α" tuned in [10⁻¹, 10]; the entropy coefficient therefore ends at α′ ≥ 0.1, never at 0 (and is set to 1 in the PRO study). (c) The SVGD convergence invoked in App. C.4 is cited to [22] and is a statement about the particle distribution; the algorithm uses M ∈ [16, 64] particles and one gradient step per update (App. B.2, Eq. 7.3), with no bound relating the amortized network to the fixed point of Eq. 6.6. "Provably RO-free" is therefore a statement about an idealized procedure, not about what was run.
- **Suggested Fix:** State the theorems for the continuous setting or restrict the claims to the idealized algorithm; add a finite-particle/finite-step error term or at least an experiment that varies M and K and shows the RO-free behaviour persists; report results with α annealed to near zero.

### W2: Theorem 5.1 is close to circular, and the headline link "consistent reasoning ⇒ no RO" has no theorem
Thm 5.1 states agents "are PRO-free with K steps negotiated reasoning if" the perceived joint policy converges to π*; the proof (C.1) is "Thus it is PRO-free after K reasoning rounds." Since PRO is defined by comparing against the optimal-opponent-policy objective (Eq. 4.2), assuming p = π* assumes the conclusion. The non-trivial content is whether negotiation reaches π*, which is deferred to C.4. Further, §4 says "It is straightforward that agents do not suffer from RO if all agents are free from ERO at convergence", but no theorem in §4 states or proves it, even though the Abstract and C1 say the paper "proves that RO can be avoided" under consistent reasoning. App. C.7 is titled "Proof for Theorem 4.3", which does not exist (Def. 4.3 and Thm 6.3 do).
- **Suggested Fix:** Add a formal statement bridging Defs. 4.1–4.3 to the original RO definition (preference for a sub-optimal NE, §4 first paragraph), and rewrite Thm 5.1 so the hypothesis is the negotiation dynamics, not their limit.

### W3: Evaluation is narrow, baselines are old, and tuning parity is unstated
All baselines date from 2017–2019 (MADDPG, MASQL, PR2, ROMMEO, Lenient MADRL, §8) while the paper compares to "state-of-the-art methods" in the Abstract. Three tiny games (3–4 agents, stateless or 25 steps) are used for "many RO-challenged environments". SVNR's hyperparameters get a 50-trial TPE search per environment; the paper does not say baselines get the same budget. Table 1 reports ± without the number of seeds or whether it is std or variance (Fig. 4 caption says "mean and variance … with 5 different seeds"). At s² = 3.0, SVNR 9.60 ± 0.30 vs L-MADRL 9.54 ± 0.13 differs by 0.06, well inside the spread, yet the Table 1 caption says SVNR "achieves the highest returns in all scenarios".
- **Suggested Fix:** Give every method the same tuning budget and report it; add at least one multi-step benchmark with more agents; report seeds, std vs. SE, and soften the s² = 3.0 claim to "comparable to L-MADRL". Cost: roughly 5 seeds × 6 methods × 3 settings; small (tens of GPU-hours at most).

### W4: "Efficient computation" is claimed but not measured; reproducibility details are missing
The Abstract says amortization makes "computation efficient" and that experiments show "efficiency", yet there is no wall-clock, FLOP or per-step comparison against the non-amortized procedure or baselines. The network architecture, hidden sizes, noise dimension, number of particles actually chosen, selected α′, compute and any code link are not stated after search. §7's text on Algorithm 1 uses K for "particle numbers" while §5 uses K for negotiation rounds and M for particles.
- **Suggested Fix:** Add a table of chosen hyperparameters and network sizes, hardware and time per 1000 steps for SVNR, SVNR without amortization (small N), and each baseline.

### W5: The ablation cannot support the claimed role of the "strict nested" structure
Thm A.1 says nested structures give full capacity and the Appendix remarks "ROMMEO takes Ci = −i, ∀i, which satisfies our nested factorization requirement and achieves the full capacity". SVNR-F (C_i = −i) performs on par with SVNR (§8.3: "both SVNR and SVNR-F outperform SVNR-M"), so Fig. 6 does not show that *strict* nesting matters, which is the condition used in Lemma 6.2, Thm 6.3 and the proof of C.4. There is also no ablation of amortization, of K, or of M.
- **Suggested Fix:** Either prove the results for C_i = −i as well, or add an experiment where strict nesting versus full conditioning visibly differ.

**Minor:** Fig. 6 caption is a copy of Fig. 4's ("different baselines in the Max Of Three"); Eq. 7.4 omits γ (compare Eq. 6.5); App. B headings refer to "Equation 12" and "Equation 9" while the main text numbers are 6.4, 7.2, 7.3; "lim k→K" with finite K in Eq. 5.1 and Thm 5.1; the sum in Eq. 3.1 starts at t = 1.

### Error Log

| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E3 | §8 Hyperparameters vs Thm 5.2 | "α = α′ + exp(−0.1 × max(steps − 10, 0)) ∗ 500" | Thm 5.2 requires α → 0; this schedule tends to α′ ≥ 0.1 | Cross-referenced (§5 Thm 5.2, §8) | High | MAJOR | Anneal toward 0 or state that Thm 5.2 does not cover the experiments |
| ERR-2 | E3 | §6.2 Lemmas 6.1–6.2 vs §8.1 | "common one-dimension bounded continuous action space of [−10, 10]" | Lemmas assume |U| < ∞; experiments use a continuous action space | Cross-referenced | High | MAJOR | Restate the lemmas for continuous actions |
| ERR-3 | E1/E6 | §8.1 text vs Fig. 4/6 captions | "the more severe the RO issue" (smaller s²) vs "the agents encounter a higher impact of relative" (larger s²) | Opposite directions; §8.1 first paragraph also says a high s² makes agents "easy to suffer from ERO"; Table 1 shows baselines fail at small s² | Cross-referenced three locations and Table 1 | High | MINOR | Fix the sentences/captions |
| ERR-4 | E2 | Eq. 6.6, App. C.6 | "π̃ = exp 1/α (Q(ui , uCi , s) − V (uCi , s))" | Q(u_i,u_Ci,s) is an expectation under the current π̂ of later agents' actions; the conditional of the Boltzmann joint needs a soft (log-sum-exp) marginalization. C.6 equates π̂′ with π̃ and then "proves" improvement "as in Appendix A.1 of [13]" without showing π̃ is the KL-projection used there | Derived by reading Eq. 6.6 against SQL's improvement step; extraction of Eq. 6.6 is partly garbled | Medium | MAJOR | Show that π̂′ = Boltzmann of Q (or state the lemma for what π̃ actually is) |
| ERR-5 | E2 | Eq. 7.2 vs Eq. 6.4 | "∇ u′ Q θ (st , u′)" in Eq. 7.2 vs "∇yi log π ∗ yi | y Ci" in Eq. 6.4 | The theory's score is the conditional on C_i = {1..i}; Eq. 7.2 uses the gradient of the joint Q with all other agents fixed (conditional on −i), which equals the nested conditional only if C_i = −i | Compared Eq. 6.4, B.1 ("Take pϕ and exp(Qθ) as q and p") and Eq. 7.2; garbled extraction | Medium | MAJOR (could be answered by clarification) | Derive Eq. 7.2 from Eq. 6.4 for C_i = {1..i} |

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Proof gaps (W1, W2, ERR-4/5) and narrow evaluation (W3) |
| Clarity | 2 | Notation clashes and mis-numbered appendix; understandable with effort |
| Significance | 2 | Toy-scale demonstration of a real pathology |
| Originality | 2 | New combination (SVGD sampling + nested conditioning) with limited differentiation |

## Dimension Scores (0–100)

**Pool position:** better than about 35% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the "provable" claim is not matched by the algorithm and experiments (W1, ERR-1/2), and the only evidence is three toy games against 2017–2019 baselines with unmatched tuning (W3).

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 40 | Developing | Circular Thm 5.1, finite-vs-continuous and α→0 mismatches, unjustified steps in C.6 and 7.2 |
| Clarity & Presentation | 52 | Developing | Readable but notation clashes and stale appendix labels |
| Novelty & Originality | 52 | Developing | Method novel in combination; claims of "first provable" need differentiation |
| Significance & Impact | 45 | Developing | Toy settings; limited evidence it scales |
| Experimental Validation | 42 | Developing | Old baselines, 3 toy games, tuning parity and seeds unclear |
| Reproducibility | 40 | Developing | No architecture, compute, selected hyperparameters or code |
| Ethical Compliance | 60 | Competent | Nothing at stake; limitations partly discussed (§9) |

## Questions for Authors
1. Did all baselines receive the same 50-trial TPE budget? If yes and the gap persists, my Experimental Validation score rises; if no, it falls.
2. Can Thm 6.3 be stated for continuous actions with finite particles, and what changes when α stays at α′ ≥ 0.1 at convergence?
3. Is the Table 1 ± a standard deviation over 5 seeds, and how many evaluation episodes are used?
4. Please derive Eq. 7.2 from Eq. 6.4 for C_i = {1,…,i} (ERR-5); a clean derivation would remove a MAJOR concern.

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially: §9 covers scalability only; it omits the finite-action/particle idealization and the dependence on α → 0.

## Ethics Review Flag
**No**

## Overall Score
**2 (Reject)**: the central "provable" claim is not established for the method as implemented and the empirical case is thin; fixable but not by clarification alone.

## Confidence
**4**: I checked each theorem, lemma and the equations cited above; Eq. 6.6/7.2 extraction is imperfect.

---

# Peer Review Report (Reviewer 2)

## Paper: Negotiated Reasoning: On Provably Addressing Relative Over-Generalization
## Reviewer: Prof. Sunita Raghavendran, Domain (public research university, South Asia; fictional persona)
## Expertise: opponent modeling; recursive reasoning; coordination games
## Date: 2026-11-10

---

## Summary
The paper recasts RO as a failure of consistency between an agent's model of others and what others actually do, introduces PRO/ERO to split training-time and execution-time effects, and proposes negotiation among agents (sequential conditional sampling via SVGD) as the mechanism that yields consistency. It positions itself against lenient learning and reasoning-endowed methods (PR2, ROMMEO, MASQL).

---

## Strengths

### S1: A principled angle on RO within the maximum-entropy reasoning line
Building on MaxEnt MARL (§3.2, [34; 37; 38]) and defining RO per update (§4: "we extend RO by considering each update") is a natural continuation of the PR2/ROMMEO line and gives a vocabulary (PRO, ERO) that the literature lacked.

### S2: Concrete mechanism for consistency
Using nested conditional policies with SVGD (§6.1, Eq. 6.3–6.4) and linking nested structure to full joint representability (Thm A.1) is a coherent construction; the Two Modalities experiment (§8.1) probes mode coverage, which a reasoning method should handle.

### S3: Relevant testbeds from the RO literature
Max-of-Two descendants and Particle Gather are the settings used by the closest reasoning papers (§8 cites [28], [25]), so the comparison with PR2/ROMMEO is on familiar ground.

---

## Weaknesses

### W1: "First method that can provably address RO" is not differentiated from other RO lines
The Related Work (§2) covers only lenient learning and reasoning-endowed methods and says "There are also a number of heuristic ideas to mitigate RO" without naming them. Work on RO in value factorization and policy gradients (listed below) is not discussed, although some of it gives optimality-type analysis of why and when representation limits cause RO. The claim "the first MARL method that can provably address RO" (§1, §6) and the Abstract's "lack of theoretical understanding of RO" need a comparison with these lines, in particular on what "provably" covers in each. Literature check (strict): claim C1 "medium" (closest prior: Weighted QMIX, level 3, uncited), C2/C3 "high" (no close prior in 4 arXiv queries; limited to arXiv).
- **Suggested Fix:** Add a paragraph and a table of formal guarantees (what is proved, under which assumptions) for value-factorization, optimistic policy-gradient and reasoning methods, and re-scope "first".

### W2: Closest reasoning baselines and the ROMMEO relation are under-argued
SVNR-F with C_i = −i is the ROMMEO-style full conditioning (Appendix: "ROMMEO takes Ci = −i, ∀i, which satisfies our nested factorization requirement"). If ROMMEO already has full joint capacity, the paper has to say what exactly ROMMEO fails to guarantee (consistency of the opponent model with others' *executed* behaviour?) and show it in an experiment where ROMMEO and SVNR-F differ. Table 1 shows ROMMEO with large variance (6.14 ± 4.82, 1.59 ± 5.03) but no analysis. A later member of the same reasoning family, the Recursive Reasoning Graph (AAAI 2022), is not cited.
- **Suggested Fix:** Add a "what ROMMEO/PR2 lack" analysis in the Figure 1 style, with a game in which they provably fail and SVNR-F does not.

### W3: The sequential shared-noise structure resembles known autoregressive/sequential coordination schemes
In §7 execution works because "each ξi will be shared with its neighbors Ci": agents condition on earlier agents' noises, which determine earlier agents' actions. This is a conditional (autoregressive) joint policy with shared randomness, and it is how ERO is removed. Autoregressive and sequential-update formulations of cooperative MARL exist and are not discussed (see Helpful references). The paper's cognitive-science framing ("once bitten, twice shy", §1) and the word "negotiation" overstate what is a sequential conditional sampler with a shared random seed.
- **Suggested Fix:** Present the method as conditional policies with shared randomness, state what is communicated at execution, and compare with an autoregressive-policy baseline.

### W4: Theory-to-method gap (domain-technical)
The idealized algorithm assumes finite action sets and exact SVGD convergence; the reasoning literature the paper positions against evaluates continuous control. The theoretical contribution is the formal object (PRO/ERO/consistent reasoning), but the "provably" label belongs to the idealization, not to SVNR as run (see R1-W1).
- **Suggested Fix:** Re-label: "provably RO-free in an idealized setting; empirically RO-robust in practice".

### Missing References (literature-check addendum; strict mode; 4 counted queries (3 claim, 1 expansion), cutoff 2025-09-24; no benchmark scout possible: environments are custom toy games not on arXiv; the novelty claim for C2/C3 is limited by an arXiv-only search)

| Priority | Reference (authors, title, venue/year) | Why it matters |
|----------|----------------------------------------|----------------|
| Critical | Rashid, Farquhar, Peng, Whiteson. *Weighted QMIX: Expanding Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning*, NeurIPS 2020 (found: arXiv 2006.10800; label: prior, arXiv-only 6+ months; published at NeurIPS 2020 as I know it) | Its abstract analyses why a restricted joint-value representation cannot represent action orderings that depend on other agents' actions, the mechanism behind RO; the paper should differentiate its "provable" claim from this analysis (a claim-level finding, MAJOR at most) |
| Critical | Zhao, Zhao, Li, Kannala, Pajarinen. *Optimistic Multi-Agent Policy Gradient*, ICML 2024 (found: arXiv 2311.01953, "Published at ICML 2024") | Addresses RO in policy-gradient MARL; a direct, recent, peer-reviewed comparison for a method claiming to be state of the art on RO |
| Important | Wan, Liu, Chen, Wang, Lan. *Greedy-based Value Representation for Optimal Coordination in Multi-agent Reinforcement Learning* (found: arXiv 2112.04454) | RO and "optimal consistency" for value decomposition; relevant to "provably" |
| Important | Shi, Liu, Peng. *CURO: Curriculum Learning for Relative Overgeneralization* (found: arXiv 2212.02733) | RO-specific method with empirical study of value-based and policy-gradient MARL |
| Important | Ma, Isele, Gupta, Fujimura, Kochenderfer. *Recursive Reasoning Graph for Multi-Agent Reinforcement Learning*, AAAI 2022 (found: arXiv 2203.02844) | A reasoning-endowed MARL method in the line the paper compares against |
| Helpful | Wen, Kuba, Lin, Zhang, Wen, Wang, Yang. *Multi-Agent Reinforcement Learning is a Sequence Modeling Problem*, NeurIPS 2022 (found: arXiv 2205.14953) | Autoregressive/sequential joint action generation (cf. W3) |
| Helpful | Kuba, Chen, Wen, Wen, Sun, Wang, Yang. *Trust Region Policy Optimisation in Multi-Agent Reinforcement Learning*, ICLR 2022 (found: arXiv 2109.11251) | Sequential agent-by-agent updates; relevant to the nested structure |
| Helpful | Böhmer, Kurin, Whiteson. *Deep Coordination Graphs*, ICML 2020 (found: arXiv 1910.00091; "Accepted at ICML 2020") | Message passing along coordination graphs, related to the graph-structured negotiation sets |

**Novelty delta (closest prior works from `similarity`; no text overlap; cosine ≤ 0.22):**

| Claimed contribution | Closest prior work | What that work already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|------------------------------|------------------|---------------------------|
| C2 NR/SVNR | PR2 (arXiv 1901.09207; ICLR 2019) | Level-1 probabilistic recursive reasoning in MaxEnt MARL; opponent model inferred from the agent's own actions | Opponent model made consistent through multi-round conditional sampling (negotiation) | Cited; differentiated in §2 ("not guaranteed to be consistent") |
| C2 | Recursive Reasoning Graph (AAAI 2022) | Reasoning in CTDE | As above | No |
| C1 | CURO (arXiv 2212.02733); Weighted QMIX; GVR | RO analysis/mitigation in value or PG MARL | Per-update RO definition (PRO/ERO) and consistency condition | No |

**Per-claim novelty:** C1 medium; C2 high; C3 high (no close prior found in these arXiv queries; at most medium by the skill's rule for absent matches).

**Field snapshot (as of the cutoff, from kept results only).** Earlier RO work in MARL relied on lenient and optimistic updates; later work analysed RO through representational limits of value factorization (Weighted QMIX, Greedy-based Value Representation), added curricula (CURO), or introduced optimistic policy-gradient updates (Optimistic MAPG, ICML 2024), alongside reasoning-endowed methods (PR2; Recursive Reasoning Graph, AAAI 2022). Recent RO papers study RO inside value-based *and* policy-gradient learners and more than one environment family, per their abstracts. What counts as significant now is therefore a method that removes RO beyond hand-built toy games and a theory that states clearly what is and is not guaranteed; a clean toy-scale win against 2017–2019 baselines is the entry ticket, not the contribution.

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gaps between theory and what is implemented |
| Clarity | 2 | Understandable with effort; notation inconsistencies |
| Significance | 2 | Narrow evidence |
| Originality | 3 | New concepts (PRO/ERO) and mechanism |

## Dimension Scores (0–100)

**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a genuine conceptual contribution (PRO/ERO) is offset by unaddressed RO literature and a "first provable" claim that cannot be assessed against it.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 48 | Developing | Idealization vs implementation gap; short proofs |
| Clarity & Presentation | 55 | Competent | Concepts are explained with examples (§4, Fig. 1) |
| Novelty & Originality | 56 | Competent | New formalization and mechanism; incremental over PR2/ROMMEO in spirit |
| Significance & Impact | 48 | Developing | Toy domains |
| Experimental Validation | 46 | Developing | Old baselines, narrow settings |
| Reproducibility | 45 | Developing | Missing architecture and compute details |
| Ethical Compliance | 62 | Competent | No ethical stakes |

## Questions for Authors
1. What formal guarantee does ROMMEO (C_i = −i) lack that SVNR-F has? A concrete game would change my novelty view.
2. Which prior RO analyses (value-factorization, optimistic policy gradient) do you consider covered by "heuristic ideas" in §2?
3. What exactly is communicated at execution time (noise vectors ξ_j of earlier agents)? Are baselines given the same side information?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially (§9 scalability only).

## Ethics Review Flag
**No**

## Overall Score
**3 (Borderline Reject)**: interesting concept, but positioning and the theory-to-method gap keep it below the bar.

## Confidence
**4**: I know the reasoning line well; the value-factorization comparison relies on abstracts only.

---

# Peer Review Report (Reviewer 3)

## Paper: Negotiated Reasoning: On Provably Addressing Relative Over-Generalization
## Reviewer: Dr. Amara Nwosu, Perspective (research institute, Europe; fictional persona)
## Expertise: Stein variational methods and sampling; statistical physics of learning
## Date: 2026-11-10

---

## Summary
From a sampling viewpoint, SVNR is Gibbs-style sampling of a joint Boltzmann distribution over actions: each agent moves its sample along an SVGD direction while conditioning on a subset of the others, and the resulting sampler is distilled into a noise-conditioned network. The paper argues that exact joint sampling removes the exploration-induced bias behind RO, and shows on toy games that it finds optimal coordination.

---

## Strengths

### S1: A fruitful connection between MARL pathologies and joint sampling
Treating the optimal joint policy as a Boltzmann target (Eq. 3.3) and fixing RO by getting the *joint* sampling right (Eq. 6.1 chain-rule decomposition) is elegant: the KL decomposition in Eq. 6.1 shows the per-agent update objective (Eq. 6.2) is exactly what MPSVGD optimizes.

### S2: Mode coverage is addressed explicitly
The Two Modalities scenario (§8.1, Fig. 3, judged from the caption) targets a failure mode of mean-seeking independent policies: multi-modal optima. A sampler-based policy is a natural remedy, and the paper makes the point visibly.

### S3: Amortization is the right practical instinct
Following soft Q-learning with amortized SVGD [9] (§7, Eq. 7.1–7.3) gives a one-pass actor; this is how SVGD-based RL has been made practical.

---

## Weaknesses

### W1: The ERO fix depends on shared randomness, which changes the problem
Thm 5.2 takes π̄_i = u_i^{0,K} and §7 says each "ξi will be shared with its neighbors Ci". With C_i = {1,…,i} this is a shared random seed plus ordering: coordination via a correlation device (as in correlated equilibrium), which trivially resolves the miscoordination in Fig. 1b. This is a legitimate design, but it is a stronger execution model than independent decentralized actors, and the baselines (MADDPG, PR2, etc.) are not given it. Related: with multiple optima (Two Modalities, §8.1) α → 0 makes the Boltzmann target uniform over the optima; independent deterministic agents cannot pick the same mode without exactly this shared randomness.
- **Suggested Fix:** State the execution assumption explicitly in the framework (§5) and in the ERO definition; add a baseline that also receives a shared random seed or an autoregressive actor (e.g., "MADDPG + ordered conditioning").

### W2: Scaling and sampling-quality assumptions
The nested structure grows each agent's conditioning set up to N − 1, and SVGD with an RBF kernel and median bandwidth (§8: "h = med² / log n") is known to degrade in higher dimensions. The paper acknowledges many-agent scalability (§9) but gives no experiment past four agents or one-dimensional per-agent actions; the claim that attention or sparse graphs would help is untested.
- **Suggested Fix:** A scaling curve (N = 2…8 on a tunable-difficulty game) and a sampling-quality diagnostic (e.g., sliced Wasserstein distance to the Boltzmann target for a game where it is known).

### W3: The cognitive-science framing is loosely connected to the technical content
§1 motivates RO with "once bitten, twice shy" and cites cognitive-science work on over-generalization; RO in MARL is a game-theoretic exploration/credit-assignment pathology, not generalization in the psychological sense. Likewise "negotiation" is not modeled (no bargaining, no price of agreement). The analogy is harmless but occupies the first page and sets expectations the paper does not meet.
- **Suggested Fix:** Shorten the framing and link instead to correlation devices, Gibbs sampling and message passing, which are what the method is.

### W4: Practical impact: communication and deployment
The paper does not discuss what happens if the shared noise cannot be delivered (latency, packet loss), or when agents cannot be ordered consistently. For robotics/traffic, which §1 cites as application areas, these determine deployability.
- **Suggested Fix:** A robustness test with noise corruption/dropout at execution, and a discussion of ordering choices.

**Minor:** the "negotiation policy" and "perceived opponent policy" terms are used interchangeably in places (§2 last paragraph).

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Good idea, execution-model and scaling gaps |
| Clarity | 3 | Concept readable; analogies distracting |
| Significance | 3 | Promising direction in structured joint policies |
| Originality | 3 | Fresh combination of sampling and MARL |

## Dimension Scores (0–100)

**Pool position:** better than about 55% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a fresh idea with elegant theory framing is undercut by toy-scale evidence; at the borderline floor, I do not place it above the bar.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Idealized analysis is sensible; implementation gap |
| Clarity & Presentation | 58 | Competent | Clear core idea |
| Novelty & Originality | 62 | Competent | Joint sampling for RO is a new angle |
| Significance & Impact | 56 | Competent | Could matter for structured policies |
| Experimental Validation | 50 | Developing | Toy settings |
| Reproducibility | 48 | Developing | Missing details |
| Ethical Compliance | 66 | Competent | Nothing at stake; limitations stated |

## Questions for Authors
1. What does SVNR do if agents execute with independent noises (no sharing)? A graceful degradation would raise my Significance score.
2. Is there a diagnostic of how close the amortized policy is to the Boltzmann joint?
3. How does performance scale with N and with the per-agent action dimension?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No**

## Overall Score
**3 (Borderline Reject)**: a promising connection, not yet backed by evidence beyond toy games.

## Confidence
**3**: strong on SVGD, less on the MARL benchmark landscape.

---

# Peer Review Report (Reviewer 4)

## Paper: Negotiated Reasoning: On Provably Addressing Relative Over-Generalization
## Reviewer: Dr. Yuki Tanabe, Generalist (university lab, East Asia; fictional persona)
## Expertise: reinforcement learning, generative models
## Date: 2026-11-10

---

## Summary
The paper's pitch: cooperative agents often get stuck on a safe but poor joint action; the authors define when that is avoided in theory (consistent reasoning), give an algorithm that implements it (SVNR) using Stein variational sampling with agents conditioning on each other's noise, and show it reaching optimal rewards in three small games where older methods fail.

---

## Venue-fit checklist (ICLR criteria turned into checkable items)

| Item | Status | Location |
|------|--------|----------|
| Claims supported by evidence | Partly: toy games support a narrower claim than "provably … many environments" | Abstract, §8 |
| Soundness | Partly: short appendix proofs, assumption mismatches | §5–§6, App. C |
| Contribution clear and significant for audience | Partly: new concepts; value beyond toy scale unclear | §1, §9 |
| Presentation | Partly: readable core, inconsistent notation and labels | §5–§7, App. B |
| Reproducibility | Not met: architecture, compute, code missing | §8 |
| Honest limitations | Partly | §9 |

## Strengths

### S1: Clear core idea
The contrast between independent policies (Fig. 1b) and agents that sample consistently (§5, Eq. 5.1) is easy to grasp even for non-specialists, and §4's examples make PRO vs ERO concrete.

### S2: Controlled difficulty in the main benchmark
The s² knob in Max of Three (§8.1) allows a graded test; Table 1 and Fig. 4 show baselines degrading as s² shrinks, which is a persuasive pattern.

### S3: Ablation tied to the claim
SVNR-M vs SVNR (§8.3) cleanly checks that conditioning matters.

---

## Weaknesses

### W1: Contribution framing is stronger than the evidence
The Abstract's "provably avoids RO", "many RO-challenged environments" and "superiority and efficiency … compared to state-of-the-art methods" rest on three toy games, 2017–2019 baselines (§8) and a theory for an idealized setting. A reader cannot tell which claims hold for the method as run (finite vs continuous actions, α annealing; see R1-W1). **Fix:** Narrow the Abstract and §1 to what is shown; list assumptions next to each theorem.

### W2: The theory is hard to follow and has internal inconsistencies
Thm 5.1's hypothesis is its own conclusion, and §4 asserts "straightforward" links without theorems. The text and captions contradict one another on the direction of s² (§8.1 vs Fig. 4/6 captions), notation clashes (K for rounds in §5 vs "particle numbers K" in Algorithm 1), the appendix refers to "Equation 12/9" and "Theorem 4.3". **Fix:** A notation table, consistent numbering, and a short proof overview in the main text.

### W3: Experimental reporting is thin
Table 1 lacks the number of seeds and whether ± is std; there are no results for Two Modalities beyond a qualitative scatter plot (Fig. 3, judged from caption); no efficiency measurement although the Abstract claims "making computation efficient". **Fix:** Report seeds and metrics, add a mode-coverage score for Two Modalities, add a timing table.

### W4: Practical significance unclear
All environments are low-dimensional; §9 admits scalability limits. For ICLR's audience, evidence on at least one standard cooperative benchmark would substantially raise the paper's value. **Fix:** Add one standard multi-agent benchmark where RO is known to matter.

**Minor:** Fig. 6 caption copies Fig. 4's; Eq. 7.4 lacks γ; the "Wolf models" and other related-work phrasing is terse.

---

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Gaps in proofs and experiments |
| Clarity | 2 | Inconsistencies hide the contribution |
| Significance | 2 | Toy scale |
| Originality | 3 | New formulation |

## Dimension Scores (0–100)

**Pool position:** better than about 45% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: a clear idea but overclaimed wording and toy-only evidence put it among typical rejected submissions rather than accepted ones.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | Proof gaps |
| Clarity & Presentation | 52 | Developing | Inconsistencies that obscure the claims |
| Novelty & Originality | 55 | Competent | New formulation |
| Significance & Impact | 48 | Developing | Toy-scale |
| Experimental Validation | 45 | Developing | Narrow |
| Reproducibility | 45 | Developing | Missing details |
| Ethical Compliance | 62 | Competent | Nothing at stake |

## Questions for Authors
1. Which of the Abstract's claims remain if only the continuous-action, finite-particle, α′ > 0 setting is considered?
2. Can you add at least one standard cooperative benchmark? That would move me toward borderline accept.
3. Why is "negotiation" the right word for a sampler with shared noise?

## Limitations Assessment
**Have the authors adequately addressed limitations?** Partially.

## Ethics Review Flag
**No**

## Overall Score
**3 (Borderline Reject)**: a clear idea whose evidence and wording do not yet match each other.

## Confidence
**3**: not a MARL-theory specialist; I did not recheck every proof.

---

# Devil's Advocate Report

## Paper: Negotiated Reasoning: On Provably Addressing Relative Over-Generalization
## Reviewer: Prof. Dmitri Kovalenko, evaluation methodology and learning in games (public research university, Eastern Europe; fictional persona)

---

## Steelman
RO is a real pathology; the authors give it a per-update formalization, identify a sufficient condition (agents' models of others coincide with what others do), and a sampler whose conditionals are the exact joint, which removes the bias in principle. On toy games the effect is large and baselines visibly fail.

## Core Argument Chain
1. P1: RO arises when an agent's model of others (ρ_i) differs from others' optimal/executed behaviour (Defs. 4.1–4.3).
2. P2: If the perceived joint policy converges to π*, agents are PRO-free (Thm 5.1); with α → 0 and π̄_i = u_i^{0,K}, they are ERO-free (Thm 5.2).
3. P3: Nested-conditional SVGD converges to π* and policy iteration with it converges to the optimal soft policy (App. C.4, Lemmas 6.1–6.2, Thm 6.3).
4. P4: The amortized network implements this procedure (§7).
5. P5: Experiments show SVNR escapes RO where baselines do not (Table 1, Figs 3–7).
∴ SVNR "provably" addresses RO and is superior and efficient.

## Strongest Counter-Argument
The word "provably" attaches to a chain whose links do not connect. P2's first link is circular: Thm 5.1's hypothesis is the conclusion's content, since once p = π* is assumed, "PRO-free" follows from the definition (C.1 is one sentence). The real work is P3, but P3 is proved under conditions the paper does not satisfy: finite actions (Lemmas 6.1, 6.2, Thm 6.3) versus the continuous [−10, 10] actions in every experiment; α → 0 for ERO-freeness versus an annealing schedule that stops at α′ ≥ 0.1; exact SVGD limits versus M ∈ [16, 64] particles and a single gradient step per update (App. B.2). Even in the idealized setting, the improvement step (C.6) equates the updated policy with an expectation-marginalized Boltzmann form (Eq. 6.6) and then borrows the soft Q-learning improvement proof, which is written for the exact Boltzmann policy of the joint Q. P4 breaks again: Eq. 7.2 uses the gradient of the joint Q with all other agents fixed rather than the score of the nested conditional that Eq. 6.4 requires. What then remains is P5: a method that conditions each agent's sample on earlier agents' noise and shares that noise at execution (§7), a stronger execution model than the independent actors it is compared against. Mode choice in Two Modalities, and miscoordination in Fig. 1b, are resolved by shared randomness alone, so the outcome in Table 1 may owe nothing to "consistent reasoning" or to Stein variational sampling. The ablation SVNR-F ≈ SVNR (§8.3) means even the nested structure is not tested. The honest reading: a sequential conditional sampler with a shared seed that wins on three toy games against 2017–2019 baselines. The authors need a control in which baselines receive the same shared noise or an autoregressive actor; without it, "reasoning" is not isolated as the cause.

---

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The theory gaps and overclaiming leave a weaker, still-supported claim (an empirical method plus an idealized analysis), so they are MAJOR; the hyperparameter selection is on the training environment, which has no held-out split in these games, and neither baselines' budget nor the headline configuration is shown to be test-selected (criterion 3 table: not stated parity → MAJOR).

### MAJOR Issues

| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic | Thm 5.1; App. C.1; §4 ("It is straightforward that agents do not suffer from RO if all agents are free from ERO at convergence") | Hypothesis assumes the conclusion; the bridge from consistent reasoning to RO has no formal statement | State and prove a bridge theorem; restate Thm 5.1 on dynamics |
| DA-M2 | Scope | §6.2 Lemmas 6.1–6.2 vs §8.1; §8 α schedule vs Thm 5.2 | Theorems' assumptions (finite actions, α → 0, exact SVGD) are violated by the experiments; Abstract's "provably" overstated | Restate; add experiments that satisfy the assumptions (discrete game, α → 0) |
| DA-M3 | Evidence | §7 ("each ξi will be shared with its neighbors Ci"), Thm 5.2; §8 baselines | Shared randomness at execution is the likely cause of ERO removal; baselines lack it | Add baselines with shared seed / autoregressive actor |
| DA-M4 | Logic | App. C.6, Eq. 6.6; Eq. 7.2 vs Eq. 6.4 | Improvement step and practical gradient not shown to correspond to the theory's nested conditionals (interpretation-dependent; garbled extraction) | Provide derivations |
| DA-M5 | Evidence | §8 Baselines; Table 1 | Baselines 2017–2019, none addressing RO from the later literature; tuning parity unstated | Add current RO baselines and equal-budget tuning |
| DA-M6 | Claim distortion (E5) | Abstract: "Numerical experiments on many RO-challenged environments demonstrate the superiority and efficiency of SVNR"; §1 | Three toy games; "efficiency" never measured | Narrow the wording; add timing |
| DA-M7 | Evidence | §8.3, Fig. 6; Appendix remark on ROMMEO | SVNR-F ≈ SVNR; the strict-nested requirement used in all proofs is not tested | Add a discriminating experiment |

### MINOR Issues

| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Consistency | §8.1 vs Fig. 4/6 captions | Direction of the s² effect is stated both ways |
| DA-m2 | Consistency | §8.1 text vs Table 1 | "MADDPG algorithm falls into the local optimum … under all settings" vs MADDPG 2.08 ± 4.63 at s² = 3.0 |
| DA-m3 | Labelling | App. B headings, App. C.7 | "Equation 12", "Equation 9", "Theorem 4.3" do not exist in the main text |
| DA-m4 | Reporting | Table 1 | s² = 3.0: SVNR 9.60 ± 0.30 vs L-MADRL 9.54 ± 0.13, "highest" within noise |

---

## Numerical Sanity Check

| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| SVNR − best baseline at s² = 3.0 (Table 1) | caption: "achieves the highest returns in all scenarios" | 9.60 − 9.54 = 0.06 (spreads 0.30, 0.13) | Highest in mean, indistinguishable statistically |
| SVNR − best baseline at s² = 1.5 | SVNR 9.71 ± 0.20; best baseline −0.07 ± 0.04 | 9.78 | Large, outside spreads |
| SVNR − best baseline, Particle Gather | 4.76 ± 0.20 vs 0.00 ± 0.00 | 4.76 | Large; return scale (≤ 5) conflicts with "cumulative reward for 25 timesteps" (§8.2) unless it is a per-step mean: unclear |
| Direction of s² effect | §8.1: smaller s² = more severe RO; Fig. 4 caption: larger s² = higher impact | n/a | Contradictory |

## Ignored Alternative Explanations
1. Shared random seeds/ordering at execution (DA-M3) explain miscoordination removal independently of Stein variational sampling.
2. Per-environment TPE tuning (50 trials) for SVNR against defaults for baselines (if so) explains part of the gap.
3. A simple autoregressive policy with a centralized soft critic could reach the optimum on these 3–4-agent games.
4. Max-of-Three optima are far apart and the reward gap is 10 vs 0: a method with any better exploration could win.

## Missing Stakeholder Perspectives
Practitioners deploying multi-robot or traffic systems (cited in §1) need to know what happens with noisy or delayed shared randomness and with ordering of agents; none is discussed.

## Observations (Non-Defects)
- The Two Modalities scenario and the s² knob are good experimental design (§8.1).
- §9 states a real limitation honestly.
- The PRO/ERO vocabulary is useful even if the theorems are tightened.

---

## Dimension Scores (0–100)

**Pool position:** better than about 30% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline guarantee does not apply to the method run, and the experiments do not isolate the claimed cause.

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 38 | Circular Thm 5.1, assumption violations, unjustified steps |
| Clarity & Presentation | 50 | Contradictions and stale labels |
| Novelty & Originality | 50 | Novel framing; mechanism close to sequential conditional policies |
| Significance & Impact | 42 | Toy settings, uncontrolled cause |
| Experimental Validation | 38 | No control for shared randomness; old baselines |
| Reproducibility | 40 | Details missing |
| Ethical Compliance | 58 | Nothing at stake |

## Overall: 2 | Confidence: 4

---

## Phase 1.5/1.6: Literature Check and Report Check

**Literature check:** mode strict (cutoff 2025-09-24), 4 counted queries (3 `claim` C1–C3, 1 `expansion`), 2 `verify` calls; two over-long queries were refused (not counted). No `baseline` query: environments are custom toy games, so no external benchmark could be scouted. One concurrent preprint (2025-09-19, fully decentralized MARL as context modeling) was kept and is "worth discussing" only; it is not used in any weakness. Gaps left open: no query for the dataset/benchmark papers; arXiv-only search, so "no close prior found" for C2/C3 is a search limit, not evidence of novelty. Similarity: top-3 closest prior works are PR2 (0.22), Recursive Reasoning Graph (0.21), CURO (0.21); no high overlap (≥ 0.30) and no text overlap (0 shared 8-grams).

**Report check (Synthesizer, Step 0).**

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R1 | W1–W5 | kept | Specific, located, answered nowhere in the paper (appendix searched); ERR-4/ERR-5 kept as Medium-confidence, interpretation-dependent |
| R1 | Minor items | moved to Minor line | Cosmetic |
| R2 | W1 | rewritten | Original draft implied prior work gives "provable" RO guarantees; rewritten to the claim-level request, since only abstracts were read (Hard Rule 2) |
| R2 | W2–W4 | kept | Specific; W3's "resembles autoregressive schemes" kept as a differentiation request, not a novelty accusation |
| R3 | W1, W2, W4 | kept | Located and actionable |
| R3 | W3 | rewritten | Neutralized wording about framing ("loosely connected") to critique the text, not the authors |
| R4 | W1–W4 | kept | Specific, overlap with R1 merged in Phase 2 |
| DA | DA-M1–M7 | kept | Located; DA-M4 flagged medium confidence |
| DA | DA-m2 | rewritten | "all settings" vs MADDPG 2.08 ± 4.63 at s² = 3.0 phrased as a consistency note (Fig. 4 unavailable) |
| All | cosmetic items | moved to Minor | Reviews that overweight minor issues are the main AAAI-26 complaint |

---

## Phase 2: EIC Meta-Review and Decision

### Synthesizer package (Part A)

**Master issue list and classification**

| Issue | Sources | Class | Hinges on? |
|-------|---------|-------|------------|
| Theory (finite action, α → 0, exact SVGD) does not cover the experiments/Algorithm 1; "provably" overstated | R1-W1, R2-W4, R4-W1, DA-M2 | CONSENSUS-4 | **Yes** |
| Thm 5.1 circular; no bridge theorem to RO | R1-W2, R4-W2, DA-M1 | CONSENSUS-3 | **Yes** |
| Narrow evaluation: 3 toy games, 2017–2019 baselines, unclear tuning parity/seeds | R1-W3, R4-W3/W4, DA-M5, R2-W2, R3-W2 | CONSENSUS-4 | Yes |
| Shared randomness at execution; baselines lack it | R3-W1, R2 Q3, DA-M3 | CONSENSUS-3 (R3, R2 as a question, DA) | **Yes** |
| Missing RO literature, "first provable" overclaim | R2-W1, DA-M6 (partly) | CONSENSUS-2 | No (claim-level) |
| Efficiency claimed, not measured; missing architecture/compute | R1-W4, R4-W3, DA-M6 | CONSENSUS-3 | No |
| Ablation does not test strict nesting | R1-W5, DA-M7 | CONSENSUS-2 | No |
| Cognitive-science framing loose | R3-W3, DA (Strongest) | SOLO-ish | No |
| Eq. 6.6/C.6 and 7.2 vs 6.4 derivation gaps | R1 ERR-4/5, DA-M4 | CONSENSUS-2 | Yes (EIC checks) |
| Notation/caption inconsistencies | R1 Minor/ERR-3, R4-W2, DA-m1/m3 | CONSENSUS-3 | No |
| DA-CRITICAL | none raised | — | — |
| SPLIT | none explicit; R3 is more positive on significance than R1/DA | — | — |

**Official score (BEFORE, no EIC weights, DA-CRITICAL list empty):** official rating 2.60; composite 50.2 (`before.json`).

### EIC Meta-Review (Prof. Elin Vastarien)

#### The Case For and Against
- **For acceptance:** PRO/ERO is a useful vocabulary; sampling the joint through nested conditionals is a clean idea; the experiments show a large, visible gap on a controlled difficulty family and on a mode-coverage game; the authors state a real limitation.
- **Against acceptance:** the "provable" claim is established only for an idealized procedure whose assumptions the experiments violate; the first theorem is circular; the evidence is three toy games against 2017–2019 baselines with unclear tuning parity; the likely cause of the win (shared randomness at execution) is not controlled; efficiency and reproducibility details are missing.

#### Verification of Decisive Points (EIC read of the paper)

| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Lemmas assume |U| < ∞; experiments continuous | R1-W1, DA-M2 | Lemma 6.1/6.2, Thm 6.3; §8.1 | **Verified** | Lemma 6.1 "with |U | < ∞"; §8.1 "bounded continuous action space" |
| α anneals to α′ not 0, Thm 5.2 needs α → 0 | R1 ERR-1, DA-M2 | §8 vs Thm 5.2 | **Verified** | schedule "α = α′ + exp(−0.1 × max(steps − 10, 0)) ∗ 500"; α′ tuned in [10⁻¹, 10] |
| Thm 5.1 circular | R1-W2, DA-M1 | §5 Thm 5.1; C.1 | **Verified** (slightly overstated as "tautological": the real content is deferred to C.4) | C.1 is one sentence |
| No theorem bridges consistent reasoning to RO | R1-W2 | §4 | **Verified** | "It is straightforward that agents do not suffer from RO if all agents are free from ERO at convergence" |
| Execution shares noise among agents | R3-W1, DA-M3 | §7 | **Verified** | "each ξi will be shared with its neighbors Ci"; calling it "not decentralized" would be Overstated: only noise, not observations, is shared |
| Baselines are 2017–2019 | R1-W3, DA-M5 | §8 | **Verified** | |
| Table 1 s² = 3.0 gap vs L-MADRL | R1-W3, DA-m4 | Table 1 | **Verified** (0.06 vs spreads 0.30/0.13) | |
| s² direction contradiction | R1 ERR-3, DA-m1 | §8.1, Figs 4/6 captions | **Verified** | Minor |
| No architecture/compute/code stated | R1-W4 | §8 | **Verified** (text search) | Appendix has none |
| Eq. 6.6/C.6 improvement step unjustified | R1 ERR-4, DA-M4 | Eq. 6.6; C.6 | **Partly correct** | Eq. 6.6 does use an expectation under π̂; whether π̃ equals the needed KL-projection depends on the intended definition, which is not given |
| Eq. 7.2 vs 6.4 mismatch | R1 ERR-5, DA-M4 | Eq. 6.4, 7.2, B.1 | **Partly correct** | Plausible gap (conditioning set); extraction prevents full confirmation; I treat it as a question for the authors |
| "efficiency" never measured | R1-W4, DA-M6 | Abstract; §8 | **Verified** | no timing found by text search; Fig. 4 shows sample-efficiency curves only |
| "first provable" overclaim vs RO literature | R2-W1 | §1, §6 | **Partly correct** | Prior abstracts show related RO analyses (value factorization), not the same setting; a request to differentiate, not a refutation |
| ROMMEO full capacity yet SVNR-F ≈ SVNR | R1-W5, R2-W2 | Appendix A remark; §8.3 | **Verified** | |

No integrity findings. Literature: R2's references are verified except where marked (all found by the script).

#### Reviewer Weights

| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 2 | 4 | 1.25 | Nearly all points verified at their locations, including two I would not have found quickly (α schedule, finite action sets); two Medium-confidence derivation points are flagged as such |
| R2 (Domain) | 3 | 4 | 1.0 | Sound, but the literature points rest on abstracts only; correctly hedged after the report check |
| R3 (Perspective) | 3 | 3 | 1.0 | Shared-randomness point verified and decisive; role is constructive; calibrated to the borderline |
| R4 (Generalist) | 3 | 3 | 1.0 | Typical, accurate, largely overlapping with R1 |
| DA | 2 | 4 | 1.0 | Arguments verified; none rated CRITICAL; Overall 2 is slightly harsh but follows the argument chain |

#### DA-CRITICAL Rulings
No DA-CRITICAL issue was raised, so no ruling is needed and there is no ceiling. I also checked the DA's candidate: hyperparameter selection by "maximum mean reward in 50 trails": these games have no separate held-out split, the numbers are not selected from a table on a reported test set, and parity with baselines is unstated; the criterion-3 table row is "not stated → MAJOR". No upheld issue.

#### Final Decision and Justification
The reviewers' recommendations give an EIC-weighted rating of **2.54**, starting point **3 (Borderline Reject)**; the plain mean is 2.60. The 0–100 composite is 50.2 (official) and 49.7 (EIC-weighted), 0.3 points under the band edge at 50. A one-step band disagreement this close to a boundary is not a reason to depart, and I named no verified issue the ratings missed, so I keep the rating-based starting point and note the composite as a borderline signal. My decision is **3 (Borderline Reject)**. The reviewers' pool positions are 30–55 (spread 25, below the 30-point rule); my own pool position is **about 40**: better than roughly 40% of ICLR submissions, in the typical rejected band. The deciding evidence is that the one thing the paper sells, a provable result, is not shown for the method as run (finite actions vs continuous experiments, α′ ≥ 0.1 vs α → 0) and that the improvements are measured on three toy games, against old baselines, without a control for shared randomness. These are fixable, mostly by narrowing claims, adding baselines and tightening proofs, which is why I do not decide 2: the conceptual vocabulary and the controlled s² study have real value. Not exceeding the ceiling: none applies. The decision is a simulation of how a careful panel would likely see this draft, not a prediction.

---

# Editorial Decision

## Paper: Negotiated Reasoning: On Provably Addressing Relative Over-Generalization
## Submission ID: iclr26-FmvBrKubtw
## Date: 2026-11-10
## Target Venue: ICLR | Paper Type: theoretical
## Review Team (fictional personas): EIC Prof. Elin Vastarien; R1 Methodology Dr. Mateo Orsolini; R2 Domain Prof. Sunita Raghavendran; R3 Perspective Dr. Amara Nwosu; R4 Generalist Dr. Yuki Tanabe; DA Prof. Dmitri Kovalenko

---

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 2, R2 3, R3 3, R4 3, DA 2 → mean **2.60** · official composite **50.2**
**EIC assessment** (internal): weighted rating **2.54** → starting point **3** · weighted composite **49.7** → band 2 (cross-check, 0.3 below the edge) · **DA ceiling**: none · **Final (EIC)**: **3**
**Target-venue label (ICLR, status secondary):** "4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10})", as reported for recent cycles; verify against the current form.

## Score Summary

### Official Scores and EIC Assessment (output of `aggregate_scores.py scores.json --venue iclr --final 3`)

#### Reviewer weights (EIC, internal)

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| R1 (Meth.) | 4 | 0.85 | 1.25 | 26% |
| R2 (Domain) | 4 | 0.85 | 1.00 | 20% |
| R3 (Persp.) | 3 | 0.70 | 1.00 | 17% |
| R4 (Gen.) | 3 | 0.70 | 1.00 | 17% |
| DA | 4 | 0.85 | 1.00 | 20% |

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 40 | 48 | 56 | 50 | 38 | 46.4 | 45.6 | 18 |
| Clarity & Presentation | 52 | 55 | 58 | 52 | 50 | 53.4 | 53.2 | 8 |
| Novelty & Originality | 52 | 56 | 62 | 55 | 50 | 55.0 | 54.6 | 12 |
| Significance & Impact | 45 | 48 | 56 | 48 | 42 | 47.8 | 47.4 | 14 |
| Experimental Validation | 42 | 46 | 50 | 45 | 38 | 44.2 | 43.8 | 12 |
| Reproducibility | 40 | 45 | 48 | 45 | 40 | 43.6 | 43.2 | 8 |
| Ethical Compliance | 60 | 62 | 66 | 62 | 58 | 61.6 | 61.3 | 8 |
| **Composite** | 46.5 | 51.4 | 57.4 | 51.4 | 44.3 | **50.2 (before: 50.2)** | **49.7 (after)** | |
| Pool position (P%) | 35 | 45 | 55 | 45 | 30 | | | |

No dimension is flagged ⚠ (all spreads ≤ 20); no consistency warnings.

### Target-Venue Scores (ICLR, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 1 / 2 / 2 |
| Rating | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) |
| Venue-weighted composite | 49.4 (band 3 → 3) |

*EIC pool position: about 40.*

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "Negotiated Reasoning: On Provably Addressing Relative Over-Generalization" to ICLR. Relative over-generalization is a real obstacle to optimal cooperation, and a theory-backed treatment is a worthwhile ambition.

**Overall Assessment:**
The reviewers found the PRO/ERO vocabulary, the use of nested conditional sampling with Stein variational methods, and the controlled Max-of-Three difficulty study valuable. They agreed, however, that the guarantee is shown for an idealized procedure and that the experiments, which are small and use older baselines, do not isolate the claimed cause.

**Key Strengths Identified by Reviewers:**
1. A useful decomposition of RO into training-time (PRO) and execution-time (ERO) effects (R1, R2, R4).
2. A controlled difficulty family and a mode-coverage game where baselines fail visibly (R1, R3, R4).
3. A clear conditional-sampling idea with an amortized implementation, and an honest scalability limitation (R2, R3, R1).

**Key Concerns Requiring Attention:**
1. The theory's assumptions (finite action sets, α → 0, exact SVGD) are not met by the experiments or Algorithm 1, so "provably" is overstated (CONSENSUS-4, verified by the EIC).
2. Theorem 5.1 assumes the content of its conclusion, and no theorem bridges consistent reasoning to the original RO definition (CONSENSUS-3, verified).
3. Evidence: three toy games, baselines from 2017–2019, unclear tuning parity, no efficiency measurement, and no control for the shared noise used at execution (CONSENSUS-3/4, verified).

**Critical Challenge (Devil's Advocate):** The DA argued that the empirical win may owe to shared randomness and ordering at execution rather than to "consistent reasoning". It was rated MAJOR; the EIC verified the factual basis (§7) and asks for a control with the same side information for the baselines.

**Decision: Borderline Reject (3)**

The ideas are promising and the issues are fixable, but a revised version would need to (i) restate the guarantees for the setting actually used, (ii) fix Theorem 5.1 and add the bridge theorem, and (iii) add current baselines, an equal tuning budget, shared-randomness controls and at least one standard benchmark. Any of these done well would move the paper toward Borderline Accept.

Sincerely,
Prof. Elin Vastarien (fictional persona)
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)
| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Theory does not cover the implemented/experimented setting; "provably" overstated | R1, R2, R4, DA | CONSENSUS-4 |
| Narrow evaluation, old baselines, unclear tuning parity and seeds | R1, R2, R3, R4, DA | CONSENSUS-5 (R2, R3 on baselines/scaling) |
| Circular Thm 5.1 / missing bridge theorem | R1, R4, DA | CONSENSUS-3 |
| Shared randomness at execution not controlled | R3, R2 (question), DA | CONSENSUS-3 |
| Efficiency unmeasured; missing architecture/compute details | R1, R4, DA | CONSENSUS-3 |
| Inconsistent notation/captions/appendix labels | R1, R4, DA | CONSENSUS-3 |

### Points of Disagreement
| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Significance of the idea beyond toy scale | R3 (promising direction) | R1, R4, DA (toy) | EIC: promising but unevidenced; scored at the borderline floor by R3 and below elsewhere; no reason to move the decision |
| Whether novelty is high | R3 (62) | R1, DA (50–52) | Both sides hedge: the formalization is new; the mechanism is close to sequential conditional policies; claim-level, not decisive |

### Score Spread Discussion
No dimension has spread > 20 (largest: Technical Rigor 18, R3 56 vs DA 38). R3 is the most positive; I adopt the lower values because R1's and the DA's rigor points were verified.

### Devil's Advocate Highlights
| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Circular Thm 5.1; no bridge theorem | Yes (R1, R4) | n/a | Clarification + new proof text |
| DA-M2 | MAJOR | Assumptions violated by experiments | Yes (R1, R2, R4) | n/a | New experiments/restatement |
| DA-M3 | MAJOR | Shared randomness uncontrolled | Yes (R3, R2) | n/a | New experiment |
| DA-M4 | MAJOR | Eq. 6.6/C.6, 7.2 vs 6.4 | Yes (R1) | Partly correct | Derivations |
| DA-M5–M7 | MAJOR | Baselines, claim wording, ablation | Yes | n/a | Experiments/wording |

---

## Revision Roadmap

### Priority 1: Required (Must Fix)
*No upheld DA-CRITICAL issues; these are the EIC-verified items that undermine the main claim.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| R1 | "Provably" claims not matched to what was run (finite vs continuous actions, α′ ≥ 0.1 vs α → 0, finite particles, amortization) | R1-W1, R2-W4, R4-W1, DA-M2 | Abstract, §1, Lemmas 6.1–6.2, Thm 5.2, §8 | Restate theorems for the continuous case or scope the claims to the idealized algorithm; add a discrete-action game and α → 0 run | Medium; ≈ 20 GPU-h | Partly (wording yes, experiments partly) |
| R2 | Thm 5.1 hypothesis is its conclusion; missing bridge theorem to RO; App. C.7 refers to a non-existent theorem | R1-W2, R4-W2, DA-M1 | §4, Thm 5.1, C.1, C.7 | Rewrite Thm 5.1 on negotiation dynamics; add a formal "consistent reasoning ⇒ no RO" statement | Medium (theory) | Yes |
| R3 | Shared randomness at execution not controlled; baselines do not receive it | R3-W1, DA-M3, R2-Q3 | §7, Thm 5.2, §8 | Add baselines with shared seed/ordering or autoregressive actor; state the execution model in §5 | Medium; ≈ 30 GPU-h | Partly |
| R4 | Narrow evidence: toy games, 2017–2019 baselines, tuning parity and seeds unspecified | R1-W3, R4-W3/W4, DA-M5, R3-W2 | §8, Table 1 | Equal tuning budgets; current RO baselines (see references); ≥ 1 standard cooperative benchmark with more agents; report seeds/std | High; ≈ 100–200 GPU-h | Partly |

### Priority 2: Strongly Suggested (Should Fix)

| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| S1 | Improvement step and Eq. 7.2 not shown to match the nested-conditional theory | R1 ERR-4/5, DA-M4 | Provide derivations from Eq. 6.4/6.6; fix Eq. 7.4's γ | Medium | Yes |
| S2 | "Efficiency" unmeasured; architecture, compute, chosen hyperparameters, code missing | R1-W4, R4-W3, DA-M6 | Timing table; hyperparameter and network table; code link | Low | Yes |
| S3 | Ablation cannot test strict nesting; no amortization/K/M ablation | R1-W5, DA-M7 | Discriminating game; ablate M, K, amortization | Medium; ≈ 15 GPU-h | Partly |
| S4 | RO literature not discussed; "first provable" needs differentiation | R2-W1, R2-W2 | Add Weighted QMIX, Optimistic MAPG, Greedy-based Value Representation, CURO, Recursive Reasoning Graph; table of guarantees | Low | Yes |
| S5 | Contradictions: s² direction, MADDPG "all settings", Fig. 6 caption, appendix labels, notation (K) | R1 ERR-3, R4-W2, DA-m1–m3 | Fix text and captions; notation table | Low | Yes |

### Priority 3: Nice to Fix (Optional)

| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Cognitive-science framing and the word "negotiation" | R3-W3, R2-W3 | Shorten; connect to correlation devices and Gibbs sampling |
| N2 | Scaling and communication robustness | R3-W2/W4 | Scaling curve; noise dropout test |
| N3 | Sampling-quality diagnostic of the amortized policy | R3 Q2 | Distance to the Boltzmann target on a game with known target |
| N4 | Helpful references (autoregressive / sequential-update MARL, coordination graphs) | R2 | Cite and compare |

---

## Estimated Revision Effort
- Priority 1: 4 items, about 3–5 weeks (theory rewrite 1 week; experiments ≈ 150–250 GPU-hours)
- Priority 2: 5 items, about 1–2 weeks
- Priority 3: 4 items, optional
- **Total estimated revision time**: 4–7 weeks for the full list; a rebuttal-window subset (wording, derivations, tables, literature) is feasible in one week.
