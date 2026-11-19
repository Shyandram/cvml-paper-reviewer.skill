# Review: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

Note: only the extracted text was available. Figures 1–4 (difficulty distributions, per-language and per-repository resolve rates) could not be inspected, so claims that rest on them are judged from captions and prose only.

## Summary

The paper introduces SWE-Bench Pro, an issue-resolution benchmark in the SWE-Bench style. It has 1,865 tasks from 41 repositories in Python, Go, JavaScript and TypeScript, split three ways:
- a public set of 731 tasks from 11 GPL/copyleft repositories;
- a private held-out set of 858 tasks from 12 repositories;
- a commercial set of 276 tasks from 18 proprietary startup codebases, with results reported but code not released.

Tasks come from consecutive commit pairs with fail2pass tests. Trivial edits are excluded: every task changes at least 10 lines, and the averages are 107 lines across 4.1 files. Human annotators rewrite each task into a problem statement, a list of requirements grounded in the tests, and an optional interface specification. Professional engineers build Docker environments, and tests are filtered for flakiness and relevance.

Under SWE-Agent with a 200-turn cap, frontier models resolve at most 23.3% of the public set (GPT-5) and 17.8% of the commercial set (Opus 4.1). A GPT-5-as-judge analysis then sorts the failed trajectories into failure modes.

## Strengths

1. **A timely and useful artifact.** SWE-Bench Verified is close to saturation, and the community needs a harder, multi-language, multi-file successor. The task-size filter (at least 10 LOC, about 4 files on average) and the cap of 100 tasks per repository answer known weaknesses of SWE-Bench Verified.
2. **The commercial set is a real novelty.** Evaluating on proprietary startup codebases, with results reported but code kept private, plus a held-out set for later overfitting checks, is a sensible design. It is hard for academic groups to reproduce.
3. **Substantial engineering.** Expert-built Docker environments, triple-run flakiness filtering, and human review of the fail2pass tests should make the benchmark more reliable than scraped alternatives.
4. **Interface and requirements fields.** These address a known source of false negatives: correct solutions that fail because of naming mismatches with the hidden tests. The appendix example makes the format concrete.
5. **Broad model coverage.** The evaluation includes frontier, open-weight and SWE-Smith fine-tuned models, with a first-cut breakdown of failure modes.

## Weaknesses

1. **Internal numerical inconsistencies undermine trust in the reported results.**
   - The prose disagrees with Table 1: Sonnet 4 is "16.3%" in the text but 17.6% in the table, and GPT-4o is "3.9%" in the text but 4.9% in the table. The text also calls Qwen-3 32B "DeepSeek Qwen-3 32B".
   - The failure-mode prose does not match Table 3:
     - Opus 4.1: the text says "wrong solutions 35.9%, syntax errors 24.2%", but the table gives 48.5% and 32.7% of submitted failures.
     - Gemini: the text says "tool errors 38.8%, syntax 30.5%, wrong 18.0%", but the table gives 84.0%, 57.0% and 33.6%.
     - Qwen: the text says "tool error 42.0%"; the table gives 86.0%.
   - The counts in Table 3 are not compatible with the dataset size. For Opus 4.1 the submitted and not-submitted failures sum to 681 + 239 = 920 unresolved trajectories on a 731-task public set. Given its 22.7% resolve rate, about 565 are expected. For GPT-5, the 724 failures imply about 1% resolved, not 23.3%.
   - Either the analysis used a different set or number of runs than stated, or the table is wrong. For a benchmark paper, whose main product is trustworthy numbers, this is a serious problem.
2. **The contamination-resistance claim is asserted, not measured.**
   - The argument for the public set is that GPL licensing "creates legal barriers" to inclusion in training corpora. That is a guess about the practices of model developers. GPL code is widely available on the web and in code crawls, and the paper offers no evidence either way.
   - No contamination analysis is reported. Candidates include performance before and after the training cutoff by commit date, comparison of the public set with the held-out set (which exists for exactly this purpose but is not evaluated), and membership-inference or verbatim-completion probes.
   - "Contamination-resistant" appears in the title figure and the conclusion, so it needs empirical support.
3. **The public/commercial gap is over-interpreted.** The gap is attributed to "the greater complexity of enterprise codebases". But the commercial set differs in its repositories, languages, augmentation and possibly its difficulty distribution. Without controlling for task statistics (LOC, number of files, language mix), the gap cannot be attributed to enterprise complexity or to the absence of contamination.
4. **Human augmentation is under-documented, and it changes what is measured.**
   - The requirements are "grounded on the unit tests" and include, for example, exact log strings and file paths. The interface lists exact function names and locations. This substantially narrows the solution space and moves the task towards spec-following.
   - There is no ablation without requirements or interface, though the paper itself notes that this setting is "potentially interesting". Without one, the "long-horizon" and "hours to days for a professional engineer" framing is not supported.
   - No human solve times are measured, and no annotator-difficulty ratings are given.
   - The paper reports no annotator count, no inter-annotator agreement, no audit of how often the augmentation leaks the solution, and no funnel of how many candidate tasks were dropped at each stage. SWE-Bench Verified's contribution rested on exactly this kind of accounting.
5. **The evaluation protocol is thin.**
   - There is a single scaffold. Agentless is dismissed in one sentence without numbers.
   - There is a single run per model, with no confidence intervals or variance across seeds. Reporting CIs matters on a 276-task commercial set, where differences of a few points (e.g., Sonnet 4 against Gemini) are within noise.
   - There are no cost or token budgets. A 200-turn cap combined with context limits may be what drives "context overflow" failures, so some failure modes may come from the scaffold rather than the model.
   - Different models get different tool-use mechanisms (native tool use against syntax parsing), which confounds the comparison of open-weight models.
6. **The failure analysis is shallow and partly self-referential.**
   - GPT-5 judges its own trajectories and those of competitors. Validity rests on an 87% agreement figure taken from a different paper and a different taxonomy.
   - The claim that 20 turns gave "the highest correspondence with human validations" is stated without the validation data.
   - The buckets are not used to draw any actionable insight beyond descriptive percentages.
7. **The contribution is mainly an artifact, with limited insight.** Apart from the dataset, the findings ("harder tasks get lower scores", "frontier models are more consistent", "Python and Go are easier") are descriptive. There is no analysis of why tasks are hard, for example resolve rate as a function of LOC or number of files with controls. Only the Figure 4 caption, which I could not inspect, hints at such a breakdown.
8. **Related work and presentation.**
   - Related work omits closely related recent benchmarks and analyses, among them SWE-bench+ (cited only for contamination), SWE-Lancer, SWE-Gym/SWE-rebench-style continuously refreshed benchmarks, and SWE-bench-Live (cited but not discussed as an alternative contamination strategy).
   - The writing has many typos and rough sentences ("50–100+ instances", "models current perform better").
   - The blinding is imperfect: the text refers to "startups founded by Scale employees".

## Questions

1. Please reconcile Table 1 and Table 3 with the prose. Specifically, how can Opus 4.1 have 920 unresolved trajectories on a 731-task set? Were several runs pooled, or the held-out or commercial sets included?
2. Can you report results on the held-out set, or any direct contamination test (e.g., resolve rate as a function of commit date relative to model cutoffs) to support "contamination-resistant"?
3. What is the resolve rate without the requirements and interface fields, or with only the problem statement? How much of the difficulty survives when the spec does not leak the test expectations?
4. How many annotators were involved, what were their qualifications and agreement rates, and how many candidate tasks were filtered at each stage? Was any independent audit done of solvability and of solution leakage in the requirements?
5. Can you give confidence intervals and multiple seeds, and the cost per task for each model? Does raising the turn or context budget change the ranking or the context-overflow failure share?
6. Could the public/commercial gap be explained by differences in task statistics (LOC, number of files, language)? Can you report the gap after matching on these?
7. What were the Agentless numbers?
8. Is there evidence that GPL-licensed repositories are in fact absent from major training corpora?

## Scores

- **Soundness:** 2. The core numbers are internally inconsistent, and the central contamination claim is untested.
- **Presentation:** 2. The paper is clear at a high level but sloppy, with mismatched numbers, typos and an imperfect anonymization.
- **Contribution:** 3. A valuable and likely widely used artifact, with a novel commercial split, but limited scientific insight.

## Calibration bracket

- **Anchor just below: B** (a claim stated more strongly than its evidence, pool about 30). SWE-Bench Pro is above B because it delivers a concrete, useful artifact whose central purpose (a harder, multi-file, multi-language issue-resolution benchmark) is clearly met. Its difficulty claim is supported by the resolve rates, unlike B's toy-to-real gap. It does share B's pattern for its secondary headline claim: "contamination-resistant" is asserted from licensing logic with no measurement (W2), and the public/commercial gap is interpreted beyond the evidence (W3).
- **Anchor just above: C** (a careful, useful study without an insight, pool about 50). SWE-Bench Pro resembles C: a useful benchmark with descriptive "model X scores Y on setting S" findings and no explanation of why (W7). It is somewhat below C because it is less careful than C:
  - its reported numbers are internally inconsistent (W1);
  - it has a single run with no CIs and a single scaffold (W5);
  - its human-augmentation process is not documented to the standard a benchmark requires (W4).

  No accept reason of D's kind (something new shown working, or a mechanism explained) is present. The artifact alone does not move the paper above C.
- **Placement:** between B and C, near C (pool about 40). This maps to a rating of 4.

## Rating

**4** (marginally below the acceptance threshold)

## Confidence

**4**
