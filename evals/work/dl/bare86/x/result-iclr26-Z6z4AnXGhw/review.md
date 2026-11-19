# Review: Discovering Quality-Diversity Algorithms via Meta-Black-Box Optimization

(Based on the extracted text only. I could not see the figures, so I judge figure-dependent claims from captions and surrounding text. I read the main body; the appendix was not examined closely.)

## Summary
The paper proposes Learned Quality-Diversity (LQD). It replaces the competition function of a genetic algorithm with a small transformer (4 layers, 16 features, 4 heads). The transformer maps standardized (fitness, descriptor) pairs to a scalar "competition fitness", and selection is then top-N truncation. The parameters are meta-optimized with Sep-CMA-ES, following the authors' earlier LES/LGA recipe. Training uses 22 BBOB functions in 2–12 dimensions, with noise and random rotations. Descriptors are random projections of the genotype. Three variants are trained, for fitness (F), novelty (N) and a fitness-times-novelty "QD score" (F+N). Evaluation covers training tasks, six out-of-distribution BBO functions, scaling to larger populations and dimensions, and robot control tasks (Hopper, Walker2d, HalfCheetah, Ant, Arm) against ME, DNS, GA, NS and random selection. The reported findings are:
- LQD(N) beats NS on novelty and LQD(F) beats GA on fitness on training tasks.
- LQD(F+N) does not match DNS.
- LQD(F) matches or exceeds baselines on robotics. The aggregate gain over GA is not significant.
- LQD(F) shows "emergent diversity".
- LQD with random descriptors collapses to GA.

## Strengths
- Clear and well-motivated idea. QD competition is cleanly isolated as a single function f̃ = competition(f, d), and a permutation-equivariant parameterization of it is natural.
- Zero-shot transfer from low-dimensional BBOB with random-projection descriptors to robot control (up to ~584 parameters, real behaviour descriptors) is notable if it holds up.
- The random-descriptor ablation (Sec. 6.3) is a sensible control. It shows the network actually uses descriptor information.
- 32 seeds, non-parametric tests with multiple-comparison correction, and a JAX/QDax implementation that should be reproducible.
- The paper is candid that LQD(F+N) does not beat DNS.

## Weaknesses
1. **The headline claim "outperform established QD baselines" is weaker than the abstract and conclusion suggest.** The evidence on the QD objective is negative: LQD(F+N) is below DNS and below ME on fitness. The robotics evaluation uses LQD(F), a fitness-only variant. It is compared mainly on fitness, against GA and QD methods, and the aggregate gain over GA is not significant. Standard QD score and coverage on robotics are not shown. Robot-task novelty is reported only relative to ME, where LQD gets ~40% of ME's value. This is not an illumination result. The claim "advance the state-of-the-art in QD" is not supported.
2. **Fitness-only comparisons are not the QD setting.** In Fig. 6 the robotics curves are max fitness. QD methods such as ME and DNS are not designed to maximize peak fitness, so comparing a fitness-trained learner against them on that axis is partly a mismatch. The relevant comparison would be QD score, coverage and archive quality. A strong fitness-only baseline is also missing: e.g., CMA-ES / Sep-CMA-ES, or a GA with tuned mutation, tournament selection and diversity-preserving variants such as fitness sharing. The text describes only a "standard GA", and its tuning and reproduction operator are unspecified in the main text.
3. **"Emergent diversity" is overinterpreted.** Evidence is the novelty score of LQD(F) versus GA, and a heatmap (Fig. 8) described qualitatively. Higher novelty than a truncation-selection GA is expected from many non-global competition rules, including noisy or rank-smoothed selection. No control isolates diversity as causal for the fitness gain, for example injecting noise into selection or comparing against a GA with matched selection pressure. The statement that "meta-learning rediscovers that diversity is fundamental to effective optimization" is speculative. The novelty is also measured in the same descriptor space and metric on which LQD(N) was trained. The explanation of ME's higher novelty (partially-filled populations "artificially inflate" scores) is asserted without quantification, which weakens the novelty metric as a fair evaluation.
4. **Interpretability of the "discovered algorithm" is minimal.** The title promises discovery of new QD algorithms, but the result is a 4-layer transformer whose behaviour is shown only through 2D heatmaps at one population state. There is no symbolic or mechanistic characterization, no input ablation (e.g., removing fitness, changing standardization), and no comparison with the DNS rule beyond qualitative statements ("sophisticated hybrid"). It is unclear what practitioners can reuse.
5. **Generalization narrative vs. design.** Training uses a single population size (128), a fixed number of generations (256), and one family of tasks. Claims of "strong generalization" to dimension and population scale (Fig. 5) rest on two functions (Schaffers F7, Katsuura) and a heatmap of one difference against ME, with no variance information visible. The "OOD" BBO functions (Ackley, Levy, Salomon, Dixon-Price, Gallagher) are closely related synthetic landscapes, so "far outside training" overstates it. Training descriptors are random linear projections of the genotype and carry no behavioural information. Table-level robotics results (final fitness with CIs) and more tasks would help.
6. **Compute and fairness.** Meta-training is 16,384 meta-generations x 256 candidates x 256 tasks x 256 inner generations on 8 H100s. The cost of the transformer competition in the inner loop at large N (attention is O(N^2)) is not compared with ME/DNS. Baseline hyperparameters (ME grid resolution, DNS k, mutation operators, GA selection) are not described in the main text and it is not shown that they were tuned with a budget comparable to that of meta-training. LQD also gets a model-selection step on held-out tasks that the baselines do not have.
7. **Statistics.** Medians/IQR (Fig. 3/4) are mixed with means/CIs (Fig. 6/7). Log-scale normalization relative to a random-selection GA (values spanning many orders of magnitude) can compress or inflate differences. The robotics aggregate (Fig. 1) is described only as p<0.005 against all baselines except GA, with little detail on cross-task normalization. With six tasks, a few can drive the aggregate.
8. **Incremental relative to LGA/LES.** The meta-optimization recipe, attention-based set architecture and BBOB meta-task are inherited from Lange et al. [29–31]. The new element is applying it to the QD competition function. This is a reasonable contribution but modest methodologically, and there is no ablation against the existing learned-GA architecture.
9. **Claims about expressivity.** "Can represent any QD algorithm" and "searching through all archive mechanisms" are not true as stated: fixed top-N truncation, a fixed featurization with population-wise standardization, and a small width constrain the class. It is not shown that LQD can represent or approximate ME or DNS (e.g., by distillation).

## Questions
1. Can you report QD score and coverage on the robotics tasks for all methods, plus a table with final values and CIs? How does LQD(F+N) behave there?
2. What happens if the competition network is trained directly to imitate DNS or ME (expressivity check)?
3. Can you control for the "emergent diversity" claim: compare LQD(F) against a GA with noisy/soft selection at matched selection pressure, or a fitness-sharing GA?
4. How are ME/DNS/GA hyperparameters chosen for robotics? Were they tuned with a budget comparable to LQD's meta-training?
5. What is the wall-clock overhead of the transformer competition relative to DNS at large N? Does it scale beyond N = 1024?
6. How sensitive are results to the meta-training seed? All results appear to come from one selected parameter set per variant.
7. What is the variance in Fig. 5, and are per-cell differences significant?
8. Why is only LQD(F) evaluated on robotics, and how do LQD(N) and LQD(F+N) perform there?

## Soundness: 2
The experiments are broadly sensible, but the central claims (outperforming QD baselines, emergent diversity, strong generalization) rest partly on mismatched metrics, limited baselines and qualitative visual evidence.

## Presentation: 3
Clear and well organized; the algorithm and architecture are easy to follow. Missing baseline details and the lack of tables for robotics results hamper evaluation.

## Contribution: 2
An interesting application of meta-BBO to QD, with zero-shot transfer being the most interesting finding, but the methodological novelty is incremental over LGA/LES and the case that it advances QD is not made.

## Rating: 4

## Confidence: 3
