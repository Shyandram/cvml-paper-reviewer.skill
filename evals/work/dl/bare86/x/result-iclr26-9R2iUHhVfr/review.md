# Review: SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

Note: the text was extracted from the PDF and figures were not available. Statements about Figures 1–4 rely on captions and body text only.

## Summary
The paper introduces SWE-Bench Pro, a benchmark of 1,865 issue-resolution tasks from 41 repositories. It has three splits:
- **Public:** 731 tasks from 11 GPL-licensed repositories.
- **Held-out:** 858 tasks from 12 other GPL repositories, kept private.
- **Commercial:** 276 tasks from 18 proprietary startup codebases, with results reported but the data private.

Tasks are built from commit pairs with fail-to-pass and pass-to-pass tests. Trivial edits (under 10 lines) are filtered out, so reference patches average 107 lines across 4.1 files. Humans rewrite the problem statement and add a "requirements" list and an "interface" spec grounded in the gold patch and tests. Tests are run 3 times to remove flaky ones, and humans drop tests that are irrelevant or too broad.

Under a single SWE-Agent scaffold with one prompt and a 200-turn cap, the best model (GPT-5) resolves 23.3% of the public set. Claude Opus 4.1 resolves 22.7% on public and 17.8% on commercial. Results are broken down by language and repository. A GPT-5 LLM-as-judge classifies failure modes from the last 20 turns of failed trajectories.

The authors argue that SWE-Bench Verified is saturating and potentially contaminated, and that Pro is contamination-resistant (GPL licensing plus private code) and more representative of enterprise work.

## Strengths
- **Timely benchmark.** SWE-Bench Verified is near saturation, and a harder, multi-file, multi-language benchmark with real test-based verification is useful to the community.
- **Private data.** The private commercial and held-out splits are a sensible anti-overfitting design. They allow a public-vs-private comparison that could detect leaderboard overfitting.
- **Task difficulty.** The filtering produces larger patches than SWE-Bench Verified (about 107 lines and 4 files on average).
- **Test curation.** Running tests 3 times for flakiness, requiring fail-to-pass, and human filtering of broad or irrelevant tests are reasonable steps. Dockerized environments are released.
- **Honest limitations.** The paper acknowledges prescriptive requirements, test dependence, and limited language coverage. The example instance and judge prompt in the appendix aid transparency.
- **Diagnostics.** Per-language and per-repository breakdowns and a trajectory-level failure analysis go beyond a single leaderboard number.

## Weaknesses
1. **The contamination-resistance claim is asserted, not measured.**
   - The central claim is that GPL licensing "creates legal barriers" to inclusion in training corpora. This is not a technical barrier. GPL code is publicly crawlable, and a license does not prevent a model developer from training on a repository.
   - The paper offers no empirical contamination analysis. Examples would be memorization probes, comparing performance on pre- and post-cutoff commits, or comparing GPL repositories with permissive ones.
   - The public set is, by construction, public on HuggingFace and will be crawled. Only the held-out and commercial sets are protected, and the paper reports no public-vs-held-out results at all.
   - The commits are historical, and model cutoffs postdate many of them. The title-level claim "contamination-resistant" is therefore unsupported for the public set.
2. **Held-out results are missing, and commercial results are unverifiable.**
   - The held-out set (858 tasks, the largest split) is described but never evaluated, so its stated purpose of checking overfitting is not demonstrated.
   - The commercial set cannot be inspected or reproduced. It is sourced from "Scale's internal assets," including companies founded by Scale employees and acquired companies, and the authors are the data vendor. There are potential conflicts of interest and selection effects, and the paper gives no information on the commercial repositories (languages, size, domains, task-type distribution).
   - The claim that commercial tasks are "more complex" is based only on lower resolve rates. Lower rates could equally reflect harder environments, less-documented code, or noisier specifications. No complexity statistics (files and lines changed) are given for the commercial set.
   - The commercial set averages about 15 tasks per repository (276/18). This contradicts the stated "50–100 instances per repository" constraint. Per-repository numbers on the commercial set would be very noisy.
3. **Strong internal inconsistencies in the reported numbers.** These undermine confidence in the evaluation pipeline.
   - Sonnet 4 is reported at 17.6% in Table 1 but 16.3% in the text. GPT-4o is 4.9% in Table 1 and 3.9% in the text. Qwen3-32B is called a "DeepSeek Qwen-3 32B" in the text.
   - Table 2 lists Sonnet 4 at 9.1%, and the text says the best models score "less than 20%" on commercial. This is consistent only loosely, and the commercial table is not discussed beyond that sentence.
   - Table 3 contradicts the prose.
     - The text says Opus 4.1 has 35.9% wrong solutions and 24.2% syntax errors. The table says 48.5% and 32.7%.
     - The text says Sonnet 4's primary failure is context overflow at 35.6%. The table shows 61.6–63.4%.
     - The text says Qwen3's tool-error rate is 42.0%. The table says 86.0%.
     - The text says Gemini's tool errors are 38.8%. The table says 84.0%.
   - Several Table 3 counts exceed N=731. For example, Opus 4.1 has 681 submitted plus 239 not-submitted, which is 920. GPT-4o has 569+220 and Qwen3 has 386+406. These cannot be counts of unresolved instances. The submitted and not-submitted percentages also do not obviously match resolve rates, and it is unclear what the denominators are.
   - The failure categories in the table (Wrong Solution, Syntax Error, Incorrect File, Instruction Following, Edge Case, Other, Tool-Use, Long-Context, Stuck in Loop) differ from the categories in the judge prompt (e.g., misunderstood_problem_statement, endless_file_reading, context_overflow_from_listing, infinite_loop), and the mapping is not explained.
4. **The failure analysis is weakly validated and partly confounded.**
   - The single GPT-5 judge looks at only the last 20 turns. The justification is "highest correspondence with human validation," but no sample size, agreement figure or confusion matrix is given. The cited 87% agreement comes from a different paper and setup.
   - The judge is also one of the evaluated models, which risks self-preference bias.
   - A single label per trajectory conflates symptom and cause. A "syntax error" in the last turns may be a downstream effect.
   - The headline interpretation ("larger models fail on semantics, smaller on tooling") partly reflects the scaffold and prompt, not the models. Opus 4.1 submits 74% of the time versus 37% for GPT-5. GPT-5's 63% non-submission, with "tool-use" as the dominant exit reason, suggests scaffold incompatibility (e.g., the SWE-Agent action format) rather than capability. This casts doubt on the headline ranking.
5. **Evaluation protocol is narrow, and single-run without uncertainty.**
   - Only one scaffold (SWE-Agent) and one prompt are used. Agentless was dropped after "difficulty with multi-file editing" with no numbers. Strong commercial scaffolds (OpenHands, Claude Code, Codex CLI) are not evaluated. Absolute numbers like "23%" are scaffold-dependent, and the paper's own failure analysis suggests that scaffold mismatch is a large factor.
   - Pass@1 is reported from what appears to be a single run, with no confidence intervals, seeds, or temperature settings. Differences such as GPT-5 vs Opus 4.1 (0.6 points on N=731) are well within noise. Per-repository results with 50–100 tasks are noisy, and the paper's own caveat about 20–30 examples for some buckets applies broadly.
   - Open-weight evaluation is limited to Qwen3-32B and SWE-Smith-32B. Strong open models are absent. "Gemini 2.5 Pro Preview" is old relative to the September 2025 evaluation date, and "latest versions" is vague.
6. **Validity of the tasks: test over-specification.**
   - The tests are the original unit tests from the commit, and the "requirements" and "interface" are written by humans after seeing the gold patch and tests. This makes the task partly "write to the test." Requirements such as exact log strings, function names and URL formats (see the appendix example) leak test specifics. This removes ambiguity but also changes the task from realistic issue resolution into a spec-following task.
   - The inverse risk is false negatives: valid alternative solutions that fail the tests. The paper acknowledges but does not quantify this. There is no human audit of a sample of failed-but-plausible patches, and no estimate of the false-negative rate. Given the headline number of 23%, this matters for interpreting "models are far from solving long-horizon tasks."
   - The effect of the augmentation is not ablated. The paper does not evaluate the original unaugmented issue versus the augmented one, although it states that the no-requirements setting "is potentially interesting."
7. **Overclaims in framing.**
   - "Long-horizon tasks that may require hours to days for a professional" is not supported by any human time estimate or study. The proxies are LOC and files changed, and 107 lines on average is a modest change.
   - "Enterprise-level" and "industrially relevant" are not substantiated beyond repository choice. The public repositories are open-source projects selected under a GPL constraint, which biases the distribution toward certain kinds of projects.
   - "First to systematically apply such a methodology" and "novel" three-stage process are stated without a comparison against SWE-bench Live, SWE-bench+, Multi-SWE-bench, or SWE-bench Verified's annotation pipeline. The related work omits several directly relevant benchmarks and training-environment efforts (e.g., SWE-Lancer, SWE-Gym).
   - Figure 1 mentions "difficulty filtering," but the dataset-creation section does not describe it. It is unclear whether low scores partly result from selection against specific models.
   - The comparison with SWE-Bench Verified (>70% vs 23%) mixes differences in scaffold, language, task size, and spec style, so it does not isolate "enterprise complexity."
8. **Presentation and reproducibility gaps.**
   - The dataset-creation section lacks key details: the number of annotators and their qualifications, annotation time, inter-annotator agreement, how many candidate tasks were dropped at each stage, and the yield of each stage.
   - The repository list is not in the main text. Distributions of language, task type and size by split are not provided for the held-out and commercial sets.
   - Wording is inconsistent: "50–100+" vs "strict cap of 100" instances per repository, and the held-out set "mirroring the public set" while having a different number of repositories and tasks.
   - Cost, token usage, and turn statistics per model are not reported, although these are central to agentic evaluation.

## Questions
1. What empirical evidence shows that GPL repositories are less contaminated than permissive ones? For example, how does performance vary with commit date relative to each model's cutoff, or with memorization probes on gold patches?
2. What are the resolve rates on the held-out set? Do they match the public set?
3. Please fix and reconcile the discrepancies between Table 1, the text, Table 3 and the failure-mode prose. What are the denominators in Table 3, and why do counts exceed 731?
4. How many runs were done? What are the confidence intervals, and is GPT-5 vs Opus 4.1 statistically distinguishable?
5. How much of GPT-5's low submission rate (37%) is due to the SWE-Agent tool format? What happens with each vendor's native or recommended scaffold?
6. What is the human-validated agreement rate of the GPT-5 judge, on what sample, and per category? Does the judge's identity bias results for GPT-5 trajectories?
7. What fraction of failures are false negatives, i.e., a human reviewer judges the patch valid but it fails the tests? Please provide an audit of a random sample.
8. What are the commercial set's language, size and task-type statistics? Why does it average about 15 tasks per repository? Are there selection effects from Scale-affiliated startups?
9. What is the performance with the original unaugmented issue text versus the augmented statement plus requirements?
10. What was the "difficulty filtering" mentioned in Figure 1, and which models were used to filter?
11. Do you have any human time estimates supporting the "hours to days" claim?

## Ratings
- **Soundness:** 2/4. The benchmark construction is reasonable, but the contamination claim is unsupported, evaluation is single-scaffold and single-run, and the reported numbers contain multiple inconsistencies.
- **Presentation:** 2/4. The paper is readable, but tables and text disagree, and key pipeline details are missing.
- **Contribution:** 3/4. A harder, partially private SWE benchmark is useful to the community, though the novelty relative to SWE-bench variants is incremental.

**Rating: 6** (marginally above the acceptance threshold; the benchmark would be valuable, but this score is conditional on correcting the numerical inconsistencies, reporting held-out results, and adding uncertainty estimates and a contamination analysis).

**Confidence: 4**
