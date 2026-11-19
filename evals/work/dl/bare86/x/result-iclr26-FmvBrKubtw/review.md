# Review: Negotiated Reasoning: On Provably Addressing Relative Over-Generalization (ICLR 2026)

Note: the text I had covers the main paper only. Proofs (Appendix B/C) and all figures are unavailable, so I judged figure-dependent claims from captions and text.

## Summary
The paper studies relative over-generalization (RO) in cooperative MARL under CTDE. It defines Perceived RO (PRO, during training) and Executed RO (ERO, during execution). It defines "consistent reasoning": each agent's model of the others equals the others' optimal marginal policy during training, and equals their executed actions at execution. It states that consistent reasoning implies no RO. It then proposes "negotiated reasoning" (NR). Agents hold M particles of the joint action and iteratively perturb their own action conditioned on a negotiation set C_i. For the instantiation SVNR, the perturbation is an (MP)SVGD step on the Boltzmann joint policy exp(Q/α), with strict nested sets C_i = {1..i}. The paper claims that max-entropy policy iteration with this scheme converges to the optimal joint policy and is PRO-free. It also claims ERO-freedom as α→0. A practical version distils the negotiation into a neural network f_ψi(ξ_i; ξ_{C_i}, s) trained with amortized SVGD and a soft-Q critic. Experiments are on a 3-agent differential game (Max of Three, Two Modalities) and a 4-agent Particle Gather. SVNR beats MADDPG, MASQL, PR2, ROMMEO and Lenient MADRL on all of them.

## Strengths
- RO is a real and under-theorized pathology. Separating perceived and executed RO, and the "consistent reasoning" condition, is a reasonable conceptual framing. The Fig. 1 payoff examples are intuitive.
- The idea of using SVGD/MPSVGD for conditional, sequential action refinement in a max-entropy MARL setting is coherent. It connects to soft Q-learning and amortized SVGD.
- The experiments are targeted at RO. The Max-of-Three coverage parameter s² gives a controllable difficulty knob. The Two Modalities visualization directly tests mode coverage, and an ablation on the negotiation structure is included.
- The paper has a limitations paragraph that acknowledges scalability in the number of agents.

## Weaknesses
1. **"Provable" claims are conditional and partly circular.**
   - Theorem 5.1 essentially assumes what it needs: negotiation is PRO-free if the perceived joint policy converges to π*. The substantive claim, that nested SVGD reaches π*, is deferred to Appendix C.4, which I could not check.
   - It also rests on K→∞ rounds, M→∞ particles, an exact π* (or exactly evaluated Q), finite-action policy evaluation (|U|<∞ in Lemmas 6.1–6.2), and α→0.
   - None of these hold in the deployed algorithm, which uses amortized networks, a learned critic, finite particles, and approximate importance sampling. The title and abstract overstate what is established for the practical method.
   - Lemma 6.2 and Theorem 6.3 are stated for finite action spaces, yet the experiments use continuous actions. The "provably" claim therefore does not cover the experiments.
2. **The theory is in tension with its own requirements.**
   - ERO-freedom requires α→0, while PRO-freedom and the max-entropy convergence argument rely on the Boltzmann policy at α>0. A joint-policy argument that is exact at α>0 but only a limit at α→0 is not formalized.
   - The experiments anneal α to a positive α′, which is tuned over [0.1, 10]. This contradicts the ERO-free condition. "We anneal α to 1 when investigating PRO" is also not consistent with α→0.
   - The definition of ERO (Eq. 4.1) and the proof sketch for Theorem 5.2 are informal. Whether sampling u_i^{0,K} from correlated particles is actually "executed" independently per agent is not discussed.
3. **Decentralized execution is not really decentralized.**
   - Agent i's action is f_ψi(ξ_i; ξ_{C_i}, s) with C_i = {1..i}. Agent N must receive the noises of all other agents, and agent 1 receives none. Execution therefore needs a shared random seed or communication.
   - This is effectively an autoregressive or centrally sampled joint policy that uses shared randomness as a correlation device. Correlation could be what removes RO, rather than "reasoning". The claim of a decentralized, product-form executed policy π̄ = ∏π̄_i is hard to reconcile with this.
   - The paper should state this assumption clearly and compare with autoregressive and sequential-update methods (e.g., Multi-Agent Transformer, sequential policy updates, HAPPO), and with value-based methods that search over joint actions.
4. **Experimental scope is narrow and toy-like.**
   - There are only three environments: a stateless 3-agent differential game and a 4-agent, 25-step particle task. There is no standard cooperative benchmark (SMAC/SMACv2, MPE variants beyond Gather, MA-MuJoCo, Overcooked, Hanabi-like tasks) and no more than 4 agents.
   - Claims of "superiority and efficiency" on "many RO-challenged environments" are not supported. Efficiency, in terms of wall-clock time, compute, and the cost of the sequential nested sampling, is never measured.
   - The competing methods are relatively old, and several are known to be fragile. Recent RO or optimistic-learning approaches and modern CTDE baselines (QMIX-style with exploration, MAPPO, MAT) are missing.
5. **Experimental rigor.**
   - Only 5 seeds are used. The reported stds are large for some baselines, which hints at instability rather than a systematic failure.
   - SVNR's hyperparameters are tuned with TPE for 50 trials. It is not said whether the baselines received an equivalent budget (the text says "other hyperparameters follow ROMMEO"). This favors the proposed method.
   - The text on s² is contradictory. It says "the smaller the s², the more severe the RO issue", yet the Fig. 4 caption says "with the larger s², the agents encounter a higher impact of relative over-generalization". Table 1 also shows baselines stuck at the local optimum at s²=1.5 and 2.0 and recovering at 3.0, which is consistent with the text rather than the caption.
   - Table 1 uses "±" without stating what it denotes. The training curves report "variance" of instantaneous rewards rather than a confidence interval across seeds.
   - Given the hand-designed Max-of-Three reward, a gradient-free or particle-based optimizer would likely solve it. The experiments do not isolate whether the gains come from negotiation or merely from SVGD-driven particle diversity, i.e., better exploration. Baselines with a comparable exploration mechanism (e.g., SVGD-based or particle-based single-agent policies such as a soft Q-learning joint-policy sampler) are absent.
6. **Ablation is thin and partly undercuts the claims.**
   - SVNR-F (full conditioning, C_i = −i) performs comparably to nested SVNR. This does not show that the strict nested structure is needed for the empirical gains. The theory says full negotiation is not guaranteed to converge, but it works as well in practice.
   - SVNR-M (no conditioning) fails, which is expected. There are no ablations on the number of particles M, the number of negotiation rounds, amortization versus explicit particles, or the α schedule. No experiment tests the consistency condition itself, e.g., measuring PRO/ERO quantities directly.
7. **Novelty relative to the literature.** The inference ingredients are SVGD/MPSVGD, soft Q-learning and amortized SVGD, all taken from prior work. The new element is mainly conditioning on previous agents' noise. Connections to autoregressive/sequential joint policies, coordination graphs, and correlated equilibrium/communication are not discussed. The related-work claims that "this is the first method that provably addresses RO" need qualification, since prior joint-action and centralized-policy methods avoid RO trivially (e.g., a single joint policy with a joint-action critic).
8. **Presentation.**
   - There are many typos and unclear statements: the "Figrue" typo, Eq. 3.1 sums from t=1, "knowing the word model", and "perceive opponent policy" used loosely. Theorem 5.1 is garbled.
   - Several notations are overloaded or inconsistent: u, a and ξ; π̂ and p; the particle count is "M" in some places and "K" in Algorithm 1; "ϕ" is used for both the SVGD direction and a network.
   - Eq. 6.6 mixes Q and V definitions with a per-agent subscript in an unclear way. The inference of PRO from Eq. 4.2 is hard to follow.
   - The cognitive-science motivation (the "snake/rope" analogy) is loose and adds little.

## Questions
1. Can you give the precise statement and proof sketch of the nested-set convergence result (App. C.4) in the main text? In particular, what exactly is the role of the nested structure, and how does it differ from an autoregressive factorization of π*?
2. Does execution require sharing noises ξ_{C_i} among agents? If so, how is this compatible with "decentralized execution", and how would performance change if agents used independent noises at test time?
3. How do you reconcile ERO-freedom requiring α→0 with the tuned, non-vanishing α used in experiments? Please report results with α annealed to near zero, and also the measured PRO/ERO quantities.
4. Do the theorems extend to continuous action spaces and to function approximation errors (critic and amortization error)? If not, what can actually be said about the deployed algorithm?
5. Were baselines tuned with an equal budget (50 TPE trials)? Please report this, and also include a joint-policy autoregressive baseline, MAT/HAPPO, and an SVGD/particle-based exploration baseline without negotiation.
6. How does the method scale in N, with both runtime and success rate, e.g., on 6–10 agent versions of Max-of-N and Particle Gather, and on a standard benchmark?
7. Clarify the contradictory statements regarding s² and the severity of RO. What does "±" in Table 1 denote?

## Ratings
- **Soundness: 2** — The theory is conditional on idealized assumptions that do not hold for the implemented method. The execution-time communication assumption is not addressed, and the α→0 requirement conflicts with the experiments.
- **Presentation: 2** — Typos, inconsistent notation, and contradictory statements.
- **Contribution: 2** — An interesting framing and a reasonable algorithm, but the novelty over sequential/autoregressive and SVGD-based methods is limited, and the empirical validation is small-scale.

**Rating: 4** (marginally below the acceptance threshold)

**Confidence: 3**
