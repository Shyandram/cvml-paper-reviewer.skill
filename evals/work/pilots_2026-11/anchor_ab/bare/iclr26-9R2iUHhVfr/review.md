# Review: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

Note: I only had the text extracted from the PDF. Figures 1–4 were not available, so I judge figure-dependent claims (language and repository breakdowns, task distributions) from captions and the main text only.

## Summary

The paper introduces SWE-Bench Pro, a repository-level issue-resolution benchmark with 1,865 problems from 41 repositories, split into three sets:
- a public set: 731 problems from 11 GPL/copyleft repositories;
- a held-out set: 858 problems from 12 copyleft repositories, kept private;
- a commercial set: 276 problems from 18 proprietary startup codebases, with results reported but code kept private.

Problems come from consecutive commit pairs that show a fail2pass transition. Trivial edits are filtered out: every gold patch has at least 10 changed lines, and the mean is 107.4 LOC across 4.1 files. Human annotators add three things to each problem: a rewritten problem statement, a list of test-grounded "requirements", and an optional "interface" spec naming the functions and classes the tests expect. Environments are hand-built Docker images, tests are re-run three times to remove flaky ones, and annotators filter out fail2pass tests that are too broad or irrelevant.

Using SWE-Agent with a 200-turn limit, frontier models score at most 23.3% on the public set (GPT-5) and at most 17.8% on the commercial set (Claude Opus 4.1). The paper also breaks results down by language and repository, and classifies failed trajectories into failure modes with GPT-5 as the judge.

## Strengths

1. **Timely and useful resource.** SWE-Bench Verified is close to saturation, so a harder, multi-language, multi-file benchmark with working Docker environments has clear value for the community. The scale (1.8k problems), the larger patches (about 107 LOC and 4 files on average), and coverage of Go, JS and TS beyond Python are real improvements over SWE-Bench Verified.
2. **Careful task specification against false negatives.** The "interface" field addresses a well-known false-negative source: tests that hard-code names the issue never states. The requirements and the human filtering of over-broad tests also address it. The appendix example from Open Library makes the process concrete.
3. **Held-out and private splits.** A held-out set from separate repositories that can be used later to detect overfitting is a sound design choice. Evaluating on truly private commercial code is new for an academic benchmark.
4. **Environment engineering.** Expert-built Docker images, flaky-test removal by repeated runs, and pass2pass tests should make the benchmark more reproducible than scraped-environment alternatives.
5. **Failure analysis.** Trajectory-level failure-mode analysis is a useful start toward explaining why models fail, not just how often.

## Weaknesses

1. **The failure-mode numbers in the text do not match Table 3, and Table 3 is internally implausible.**
   - The text gives these failure rates, none of which appear in Table 3:

     | Model | Category | Text | Table 3 |
     |---|---|---|---|
     | Opus 4.1 | wrong solution | 35.9% | 48.5% |
     | Opus 4.1 | syntax errors | 24.2% | 32.7% |
     | Gemini 2.5 | tool errors | 38.8% | 84.0% |
     | Gemini 2.5 | syntax errors | 30.5% | 57.0% |
     | Gemini 2.5 | wrong solutions | 18.0% | 33.6% |
     | Qwen3 32B | tool error | 42.0% | 86.0% |

   - For Sonnet 4, the text describes "context overflow (35.6%)" and "endless file reading (17.0%)", but Table 3 has no such columns. Its Long-Context column shows 61.6%.
   - The categories in the judge prompt (Appendix B: misunderstood_problem_statement, endless_file_reading, infinite_loop, context_overflow_from_listing, …) also differ from Table 3's columns (Instruction Following, Long-Context, Stuck in Loop, …). The paper never explains how prompt labels map to table columns.
   - The analysis is said to cover only unresolved public instances, yet the instance counts exceed the size of the public set. Opus 4.1 has 681+239 = 920 instances, Gemini has 915, Qwen has 792 and GPT-4o has 789, against N=731. With a 22.7% resolve rate, Opus should have about 565 unresolved instances. Either the analysis covers other data (multiple runs? the commercial set?) or the counts are wrong.
   - The text seems to describe an older version of the analysis. As written, Section 6.2 cannot be trusted.
2. **Inconsistencies in the main results.**
   - The text gives Claude Sonnet 4 at 16.3% and GPT-4o at 3.9%, but Table 1 shows 17.6% and 4.9%.
   - Qwen-3 32B is called a "DeepSeek" model.
   - The abstract cites SWE-Bench as [25], which is SWE-bench-Live. "Social media posts [1, 25]" cites two arXiv papers.
   - Together these errors weaken confidence in the care taken with the whole artifact.
3. **The contamination-resistance claim is asserted, not shown.**
   - The central claim is that copyleft licensing creates "legal barriers" to inclusion in training corpora. That claim is weak: GPL code is widely present in public code corpora such as The Stack and GitHub crawls, and the paper gives no evidence that model developers exclude it.
   - There is no empirical contamination analysis. Examples would be performance versus commit date relative to model cutoffs, memorization probes on the public repositories, or a comparison with the held-out set.
   - The held-out set, which is the main tool for detecting overfitting, is not evaluated at all, so even a baseline public-vs-held-out comparison is missing.
   - The public set is now openly released, so its contamination resistance will fade. The paper should discuss this.
4. **The public-vs-commercial gap is over-interpreted.** The paper credits the lower commercial scores to "the greater complexity of enterprise codebases". However, the two sets differ in repositories, languages, patch sizes, and possibly annotation pipelines, and none of these is controlled. The paper also gives no descriptive statistics for the commercial set, so the claim cannot be checked.
5. **Unverified claims about difficulty and realism.**
   - "Hours to days for a professional software engineer" is not backed by any human timing study.
   - There is no human-solvability rate or annotator-agreement statistic for the verification stages.
   - The paper gives no counts for how many candidate problems or tests were dropped at each stage.
   - LOC and file counts are a weak proxy for long-horizon difficulty.
6. **The requirements and interface fields change what is measured, and their effect is not quantified.**
   - The requirements are "grounded on the unit tests" and give exact strings, URLs, file paths and function names. The example names the file, the function, the expected call (`Batch.add_items`) and the fallback conditions. This is close to a solution sketch.
   - The benchmark therefore largely measures implementation from a detailed spec, not issue resolution. The authors admit this in the limitations section.
   - An ablation is needed: problem statement only, versus plus requirements, versus plus interface. It would show how much the augmentation helps, and whether the reported difficulty comes from the repositories or from the spec.
   - Who checks that the requirements do not leak the solution? "Requirements never … leak solutions" is stated but never audited.
7. **The evaluation protocol is thin.**
   - Only one scaffold (SWE-Agent) is used. Agentless is dismissed without numbers.
   - Each model gets a single run, with no confidence intervals, although the gaps between models are small (GPT-5 23.3 vs Opus 22.7) and per-category sample sizes are about 20–30.
   - There is no reporting of cost, tokens or wall-clock time.
   - In Table 3, 63.1% of GPT-5 failures are "Not-Submitted", and 97.6% of those are tool-use failures. This strongly suggests that the scaffold, the syntax-parsing tool interface, or the turn and context limits are hurting some models. The rankings may therefore partly reflect scaffold compatibility rather than capability.
   - Reporting results with at least one more scaffold, or each vendor's recommended scaffold, would make the leaderboard far more informative.
8. **The LLM-as-judge methodology is under-validated.**
   - The 87% human-alignment figure is borrowed from prior work that used a different taxonomy and setup.
   - The claim that 20 turns gave "the highest correspondence with human validations" comes with no numbers, sample size or protocol.
   - Using GPT-5 as the judge while also evaluating GPT-5 creates a possible self-preference bias, and the paper does not discuss it.
9. **The dataset description contradicts itself.**
   - The paper says "each repository contributes between 50 and 100 instances". However, the commercial set averages about 15 problems per repository (276 problems over 18 repositories).
   - The paper says it "excludes trivial edits (1–10 lines)" and also says "every problem involves at least 10 lines".
   - It claims language diversity, yet Java, C++ and Rust are absent.
   - The sourcing of private repositories ("internal assets, … companies acquired …, startups founded by [affiliation] employees") raises questions about representativeness and selection that the paper does not address.
10. **Reproducibility and governance of the private splits.** Results on the commercial and held-out sets cannot be reproduced by others, and the paper does not describe how external researchers will get evaluated on them. Possible mechanisms include a submission server, rate limits, and protection against test-set probing.
11. **Presentation.**
    - The paper's analysis is shallow for its length; much of the length goes to a verbatim tool prompt in the appendix.
    - The Figure 4 caption mentions "10+ files and 500+ LOC" categories that the text never discusses.
    - Table 4 is cut off.
    - Related work leaves out several directly relevant recent benchmarks and datasets, such as SWE-Gym, SWE-rebench, SWE-PolyBench and SWE-bench-Java. It also gives no quantitative comparison table against SWE-Bench, Verified, Multi-SWE-bench and SWE-bench-Live (size, languages, LOC, files, contamination strategy).

## Questions

1. Please reconcile Section 6.2 with Table 3. Which numbers are correct? How do the judge-prompt categories map to the table columns? Why do the per-model counts exceed 731 unresolved public instances?
2. What are the resolve rates with (a) the problem statement only and (b) the problem statement plus requirements, without the interface?
3. Can you report results on the held-out set, and run some contamination analysis, such as performance versus commit date relative to model cutoffs?
4. What evidence supports the claim that GPL code is excluded from training corpora? Have you checked whether the public repositories appear in open corpora such as The Stack v2?
5. How many candidate commit pairs, problems and tests were removed at each filtering stage? What was the inter-annotator agreement on requirement writing and test filtering, and was any independent solvability check run, for example a held-out engineer solving from the description alone?
6. Why did GPT-5 fail to submit in 63% of its failures, almost all through tool-use errors? Did you tune the scaffold or prompt per model, and how sensitive are the rankings to the turn limit and context-management settings?
7. Can you give confidence intervals or multiple seeds for Tables 1 and 2, and statistics for the commercial set (languages, LOC, files)?
8. How will external researchers be evaluated on the commercial and held-out sets, and how will you prevent the private sets from being probed through repeated submissions?
9. What were the Agentless numbers?

## Ratings

- **Soundness:** 2. The core construction pipeline is reasonable, but the analysis has substantial numerical inconsistencies, the contamination claims are not tested empirically, and the evaluation is a single scaffold with single runs.
- **Presentation:** 2. The paper is readable, but there are many mismatches between text and tables, citation errors, and contradictory dataset statements.
- **Contribution:** 3. The benchmark itself is likely to be valuable and widely used. The scientific insight beyond the artifact is limited.

## Rating: 4 (marginally below the acceptance threshold)

The benchmark is a potentially high-impact resource, and I would like to see it published. As submitted, though, the paper has serious problems: the failure-mode analysis does not match its own table and has impossible instance counts, the results are misreported in the text, the contamination-resistance claim is untested and the held-out set is unevaluated, there is no ablation of the test-derived requirements and interface fields that heavily shape the task, and the evaluation uses a single scaffold that appears to disadvantage some models. A revision that fixes the numbers, adds held-out and ablation results, and validates the judge would raise my score.

## Confidence: 4
