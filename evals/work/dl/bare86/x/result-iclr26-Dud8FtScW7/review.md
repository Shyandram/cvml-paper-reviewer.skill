# Review: "The Quest for Efficient Reasoning: A Data-Centric Benchmark to CoT Distillation" (DC-CoT)

(Text-only review. Figures 5 and 6 are not available, so I judged them from captions and the surrounding text.)

## Summary
The paper presents DC-CoT, a benchmark and empirical study of data-centric chain-of-thought distillation. It covers three families of data manipulation:
- Augmentation: question rephrasing, question augmentation, answer augmentation, reverse thinking.
- Selection: teacher-correctness filtering, student-error filtering, LLM-as-judge filtering.
- Mixing: length-based and teacher-based.

Teachers include Gemini-1.5-Pro, GPT-4, Claude-3.5, GPT-4o and o4-mini. Students are Llama-3.1-8B (and an R1-distilled variant), Mistral-7B, Gemma-7B and Qwen-2.5 (0.5B–7B, plus Qwen2.5-VL-3B). Evaluation covers seven textual datasets, WebArena (agentic) and Visual-CoT. Experiments cover teacher/student pairings, student size, seed-data volume and IID/OOD transfer.

The main claims are:
1. Augmentation, especially reverse thinking, gives the largest gains.
2. Selection is useful for quality control, and LLM-as-judge is "highly effective".
3. Mixing gives only nuanced benefits.
4. The "small-model learnability gap" is confirmed.
5. Reverse scales better with data than vanilla CoT.
6. CoT distillation transfers OOD.

## Strengths
- The topic is timely and practically relevant. A unified comparison of data-centric CoT distillation recipes under one setup is useful, since the literature is fragmented.
- Coverage is broad: several teachers, student families and sizes, and text, agentic and visual tasks. Textual results are averaged over three runs.
- Some reporting is honest. Mixing gives no average gain, Reverse is not universally beneficial across student sizes (Q7), and OOD transfer is sometimes negative (GSM8K→MATH, Visual-CoT→OK-VQA).
- Code and data are said to be released.

## Weaknesses
1. **The augmentation vs. selection vs. mixing comparison is confounded by training-set size and compute.**
   - Augmentation methods generate L samples per question or add new questions, so the student sees several times more examples and tokens than under vanilla CoT or the selection and mixing variants. Reverse thinking also adds backward questions with their own rationales.
   - Selection shrinks the data. Dataset sizes are never stated.
   - No size-matched or token-matched comparison is given, for example subsampling the augmented set to the vanilla size.
   - The headline conclusion ("augmentation is most effective", Q1) therefore cannot be separated from "more data". The Table 4 results (Vanilla CoT degrades with more seed data, Reverse improves) are also hard to interpret without this control.

2. **Several claims are contradicted by the paper's own tables.**
   - Q2 states that "LLM-as-a-Judge filtering is highly effective, often surpassing simpler heuristics", and the conclusion lists it as crucial. In Table 1 the judge row (textual avg 41.04) is below No Selection (42.80), Teacher Filtering (44.73) and Student Filtering (43.87). It is the worst selection method on SQA, CSQA, MATH and WebArena.
   - The Q3 recommendations prescribe LLM-as-a-Judge for text, agentic and visual tasks, yet it hurts WebArena (15.64 vs 22.78) and is barely better than no selection on Visual-CoT.
   - Q2 says teacher-correctness filtering "consistently improve[s] over no selection or other methods". It drops WebArena from 22.78 to 14.66, ANLI from 35.42 to 24.11 and MATH from 7.39 to 5.04.
   - The "augment → filter → mix" pipelines recommended in Q3 are never evaluated. They are speculative guidelines presented as findings, even though the paper's own results show filtering and mixing can hurt.

3. **Baselines and tables are internally inconsistent.**
   - The "No Selection" and "No Mixing" rows reproduce the "No CoT" textual numbers (42.80), while "Vanilla CoT" is 41.81. The WebArena and Visual columns of the same rows use Vanilla CoT values. It is unclear which baseline selection and mixing are compared against.
   - Vanilla CoT distillation is worse than No CoT on text (41.81 vs 42.80), and worse than zero-shot CoT on ARC, ANLI and Date. On MATH it gets 4.38, below zero-shot CoT (11.76) and No CoT (7.39). This suggests a weak fine-tuning recipe (hyperparameters, truncated rationales, answer-format problems). It calls the whole pipeline into question when an 8B model fine-tuned on teacher CoT scores below zero-shot.
   - Table 4 shows swings far too large to attribute to CoT data volume (Llama ARC with Vanilla CoT: 79.95 at 25%, 55.34 at 100%; GSM8K Reverse: 30.0, 47.0, 59.7, 76.4 across fractions). The paper interprets these as "noise from additional traces". They look more like training instability or hyperparameter sensitivity.
   - Table 4's Vanilla CoT rows (e.g., ARC 79.95 at 25%) do not fit with the Table 1 Vanilla CoT numbers (ARC 55.63), so the recipes may not be comparable.

4. **Statistical rigor is weak.** Only means over three runs are reported, with no variance, confidence intervals or significance tests. Many interpreted differences are 1–2 points ("slight edge", "marginally better", "slight decrease of 0.83%"). Visual and agentic results appear to be single runs. WebArena success rates on small task subsets are very noisy, and test-set sizes are not given.

5. **Inconsistent experimental specification and reproducibility.**
   - The abstract and introduction list o4-mini, GPT-4o and Claude-3.5. The main text and tables use Gemini-1.5-Pro (text), Claude-3.5 (agentic) and "GPT-4-mini" (visual), plus GPT-4 and GPT-4.1-mini. Q5 mentions "o1-mini", which appears nowhere else. The intro mentions Gemma and Qwen as students at 3–8B, but Qwen is only used in the size sweep.
   - Different tasks use different teachers and judges, so cross-task comparison is not controlled. The textual judge is Llama-2-70B, a weak and outdated judge for reasoning quality, which probably explains the poor judge results.
   - The judge prompt, threshold τ and mixing ratio α are not given in the main text, nor are fine-tuning hyperparameters, LoRA vs full fine-tuning, training-set sizes, or the exact training target (rationale+answer).
   - For "student-error" selection, the student that produces the errors is not specified.
   - Table 1's "Visual+Agentic" average is only defined for some rows.

6. **Teacher and learnability-gap conclusions are over-claimed.**
   - Q5 claims "strong support" for the small-model learnability gap from Table 3. The evidence is one Visual-CoT experiment with a 3B student: 42.92 (GPT-4) vs 45.44 (GPT-4-mini) vs 45.20 (o4-mini), a gap of about 2.5 points. GPT-4 and GPT-4-mini are different model generations, not just sizes, with different rationale styles. The claim that GPT-4 rationales are "too complex" is never measured (no length or complexity analysis).
   - On textual tasks the Gemini-1.5-Pro vs GPT-4 differences are small and non-systematic. The explanation offered ("architectural alignment") is speculation.
   - The "prior distillation history hurts" claim for Llama-3.1-8B-R1 rests on differences of roughly 0.4–3.7 points, with no controls.
   - Table 3's Llama results are WebArena-only, with Claude/GPT-4o as teachers.

7. **The OOD/generalization analysis (Section 4.4.2) is weakly designed.**
   - Q11 says Table 5 "consistently" shows improvement, but several rows are flat or negative (MATH, OK-VQA). Q12 acknowledges this, which contradicts the earlier wording.
   - The gains are largely format and task-style adaptation. Zero-shot Llama-3.1-8B is poor at answer formatting (e.g., GSM8K 19.64 zero-shot vs 80.74 after MATH training), so the improvement does not demonstrate transfer of "reasoning skills". Controls are missing: fine-tuning on an unrelated or no-CoT dataset, or comparison with in-domain fine-tuning. The 80.74 on GSM8K after training on MATH is also hard to reconcile with MATH accuracy of 4–5% after in-domain fine-tuning.
   - Some "OOD" pairs are near-distribution (SQA→BoolQ, GSM8K→GSM8K-Rev, WebArena easy/hard share sites).
   - The text cites "Table 4" for this analysis, but the table is Table 5.

8. **Novelty and contribution.**
   - No new method is introduced. All evaluated techniques are existing ones (MetaMath, ReverseThinking, I-SHEEP, learnability-gap mixing). The contribution is the experimental protocol, which the issues above weaken.
   - "First benchmark" is a strong claim. No new evaluation set, leaderboard or fixed protocol is provided beyond the generated CoT data.
   - The benchmarks are small and older (StrategyQA, CSQA, ARC, ANLI, Date), and the teachers (GPT-4, Claude-3.5, Gemini-1.5) are dated.
   - Modern long-CoT / reasoning-trace distillation (R1-style data curation), which is where data-centric distillation matters most today, is not studied.

9. **Presentation.** There are many typos and errors ("Sourse", "Lenth", "Llama-3-8.1 B", "Dsource to the target dataset Dsource", "Visuan-CoT", "GPT-4-mini"). Figure 1's student list does not match the text, and the judge-filtering definition writes Dsource where Dtarget is meant. The analysis is written as Q&A lists with hedged language ("likely", "suggests") and untested mechanistic explanations (e.g., Reverse "fosters a deeper understanding by teaching bi-directional reasoning").

## Questions
1. Are the augmentation, selection and mixing variants matched in number of training examples and tokens? What are the training-set sizes? Please add size-matched ablations (e.g., Reverse subsampled to the vanilla size; Answer Aug with L=1).
2. Which baseline do "No Selection" and "No Mixing" use? Why do they equal the "No CoT" numbers? Why is Vanilla CoT distillation worse than No CoT and zero-shot CoT on several tasks (MATH 4.38)? Were hyperparameters tuned per method?
3. Please provide standard deviations, significance tests, test-set sizes and seed counts for WebArena and Visual-CoT.
4. Why is Llama-2-70B the textual judge? Do the judge conclusions change with a stronger judge? Please give the judge prompt and threshold.
5. Please reconcile the text with Table 1 on the judge and teacher-correctness claims (Q1–Q3, conclusion).
6. How did you separate format learning from "reasoning transfer" in Table 5? What happens when fine-tuning on an unrelated dataset?
7. Can the learnability-gap claim be verified with controlled teachers (same family, varying size, with rationale-length statistics) and multiple seeds?
8. Were the recommended combinations in Q3 (augment → filter → mix) actually evaluated?
9. Does the Reverse benefit hold with stronger, modern students and with long-CoT (R1-style) teachers? Why does Reverse give +52 on Llama GSM8K but degrade ARC/GSM8K for Qwen (Q7)?

## Scores
- Soundness: 2
- Presentation: 2
- Contribution: 2

**Rating: 4** (marginally below the acceptance threshold)

**Confidence: 4**

Rationale: A systematic study of data-centric CoT distillation is useful, but in its current form the headline comparison is confounded by data and compute. Several claims (judge and teacher-correctness filtering) are contradicted by the tables, the baselines are inconsistent, and small differences are interpreted without statistical support. The experimental specification differs between abstract and body, and the guidelines are partly untested speculation. With size-matched controls, variance reporting, consistent baselines and a modern long-CoT setting, this could become a solid benchmark paper.
