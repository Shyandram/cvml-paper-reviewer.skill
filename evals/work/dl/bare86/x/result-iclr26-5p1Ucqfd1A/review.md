# Review: CRAG-MM: Multi-modal Multi-turn Comprehensive RAG Benchmark (ICLR 2026)

Note: figures are not available. Fig. 3 and Fig. 4 were judged from the extracted numbers and captions. The paper appears to be truncated after Appendix C.1, so I did not see the rest of Appendix C (the extended model comparison) or Appendix D (industry-system querying).

## Summary

The paper introduces CRAG-MM, a benchmark for multi-modal retrieval-augmented generation (MM-RAG) aimed at wearable (smart-glasses) use. It has about 6.5K single-turn (image, question, answer) triplets and about 2K multi-turn conversations over 13 domains. 6.2K of the 7.9K images are egocentric, captured with Ray-Ban Meta glasses. The paper annotates five image-quality issues, six question types, entity popularity (head/torso/tail) and conversation structure.

Three tasks are defined:
- **Task 1:** image-KG retrieval only.
- **Task 2:** image-KG plus web retrieval.
- **Task 3:** multi-turn conversations.

Retrieval resources are a CLIP-based mock image KG (68K images, 26K entities) and an 800K-page web corpus, both with built-in distractors. Scoring is truthfulness (+1 / 0 / −1), using a GPT-4o judge. Multi-turn conversations are early-stopped after two consecutive failures.

Baselines are Llama-3.2-90B, GPT-5-mini and Gemini-2.5-Flash, either alone or in simple RAG pipelines. The paper also reports KDD Cup 2025 winning solutions and three commercial systems. Results are sliced by image quality, entity recognition, popularity, question type and context dependence. The headline findings are that simple RAG reaches only about 32% truthfulness (single-turn) and 43% (multi-turn), and that commercial systems hallucinate heavily (26–49%).

## Strengths

1. **Relevant problem and a real gap.** Egocentric, wearable-style queries with low-quality images are under-represented in knowledge-based VQA benchmarks (OK-VQA, A-OKVQA, InfoSeek, E-VQA, SnapNTell and others). Having thousands of images captured with real smart glasses is a real asset.
2. **Reusable retrieval environment.** Providing a mock image-KG API and a web-search API, with hard negatives and a controlled signal-to-noise ratio, allows comparable end-to-end systems. It also allows component-level analysis (recognition, query rewriting, generation). The mock API is more useful than most benchmarks, which give only QA pairs.
3. **Rich annotation axes.** Image quality, popularity, question type, domain and context dependence enable diagnostic slicing. The reported slices are informative: low-light and occluded images are hardest, OCR-able entities are easier than visual-only ones, and tail entities are harder.
4. **Truthfulness metric with abstention.** Penalising hallucination relative to "I don't know" is well suited to this setting. The winning KDD Cup solutions are mostly abstention-driven, which shows the metric rewards calibration.
5. **Community validation.** The benchmark was used in a public competition with about 1K participants and 5K submissions. The validation and public test splits are released, and a private split is held out, including two domains held out entirely.

## Weaknesses

1. **Inconsistencies in dataset statistics and framing.**
   - The paper alternately says "6.5K triplets and 2K conversations", "8K conversations" (with "89% focusing on factual questions"), "7.9K images" and "6.2K egocentric images".
   - Table 3 gives 6,462 single-turn questions and 1,956 conversations, which is not "8K conversations".
   - The claim that "15% of images are low-quality egocentric" does not match Table 2. Low-quality egocentric images are 6248 − 5143 = 1105, about 18% of egocentric images and 14% of all images.
   - The abstract's "32% and 43%" is presented as "straightforward RAG" while the "(32%/45%)" industry numbers are similar. The details are unclear.
   - These problems make it hard to trust other derived numbers, such as the "<5% margin of error for most slices" claim. This claim needs the actual per-slice n, and it fails for many cells in Table 3, e.g. Simple-rec. in Animal (n=10), Book (12) and Style (13).

2. **The headline "winning solutions improve baseline by 28%" is not an apples-to-apples comparison.** In Table 5 the winning team (private test) scores 19.7 and the "Llama 3.2 11B RAG" baseline scores −8.6. The 28-point gain is 19.7 − (−8.6). The paper itself admits that the winning team's results are on the private test set while the baseline and the industry systems use the public test set. The two splits are described as "similar distributions", but the private split also contains two held-out domains. So the +28% mixes a different split and different domains with the model improvement. It also mostly reflects a shift from answering wrongly to abstaining: accuracy actually dropped from 35.3 to 29.3, and the missing rate rose from 21% to 61%. The abstract presents this as "improving baseline performance", which overstates the finding. It also shows the −1/0/+1 metric can be dominated by an abstention strategy. The paper never reports an "always say I don't know" baseline (truthfulness 0), which would be a useful reference. It is nearly matched by the winning solution (19.7) and exceeds Claude (−2.8) and Llama baselines.

3. **Weak, partially unfair evaluation of "industry SOTA".**
   - The paper's claim that commercial systems have "similar quality" (32%/45%) rests on three black-box systems. Their search engines, prompts, versions and date of query are not given in the main text. The commercial systems use the live web, not the benchmark's mock corpus, so they cannot be compared fairly with benchmark-API solutions.
   - The answer correctness reference for time-sensitive questions (prices, "cheaper at Target or Walmart", movie lists) will drift with time. The paper does not discuss ground-truth staleness or dynamism, even though the abstract lists "differing information dynamism" as a design dimension. No results on dynamism are shown.
   - "GPT-5" is in the industry group while "GPT-5 mini" is a baseline. The model/system names are ambiguous ("Gemini", "Claude Sonnet" with no versions; the references cite Claude 3.7).
   - Results are single runs with no confidence intervals or seeds.

4. **Evaluation protocol validity.**
   - The judge is GPT-4o. Its reported "99% accuracy" is dominated by the trivial Missing class (100%). For the Incorrect class, precision is only 68.1%, i.e. the judge flags many correct answers as incorrect. That matters because incorrect answers carry −1 penalty. The judge was validated on what appears to be a modest sample whose size, source and human agreement (kappa) are not reported. Truncating answers to 75 tokens may also bias the evaluation against systems that give longer answers (e.g. the commercial ones).
   - Using −1 for hallucination makes the metric highly sensitive to abstention thresholds. Models are compared with different prompts ("encourage 'I don't know'"). Accuracy, missing and hallucination should be analysed jointly, e.g. via accuracy-at-coverage curves.
   - The multi-turn early-stop rule scores skipped turns as 0, which makes later-turn difficulty and conversation length interact. The paper gives no analysis of how sensitive the rankings are to this design choice.

5. **Data construction limits the claims of realism.**
   - Single-turn questions are generated from KG templates plus annotator-written questions. The multi-turn conversations are produced by Llama-3.2-90B-Vision-Instruct from seed questions, then filtered by annotators. This introduces a risk of model-family bias, since Llama is also evaluated as a baseline. No annotator agreement statistics, per-question verification rate or the fraction of LLM-generated turns discarded or edited are reported. The claim that multi-turn conversations "simulate natural topic drift" is not backed by a comparison with real user conversations.
   - For egocentric images, the questions are written by annotators to be "plausible", not collected from real wearable users. Vendors collected images "whenever possible" and otherwise searched for images online, so the egocentric fraction in the pre-defined set is not purely egocentric. The paper never says what fraction of the 6.2K egocentric images came from the pre-defined versus free-form collection.
   - The image KG is built to include "hard negatives" via the benchmark's own query images (S(i)). The recall of 52% with a full-image CLIP query is therefore a property of the authors' construction, not of "realistic wearable retrieval". Similarly, the web corpus is built from Brave search results for the ground-truth queries plus decoys, so the "1:2" ratio and "89% recall" are by construction. The paper does not show whether the benchmark is about retrieval ability or about the corpus design.

6. **Limited empirical depth and analysis.**
   - The paper only presents "straightforward" baselines. Missing are stronger, well-known MM-RAG baselines such as cropping/entity-detection-then-retrieve, reranking, agentic/iterative search, and open-source models of different sizes (the main text defers a larger comparison to Appendix C.3). Without stronger baselines, "ample room for improvement" is the weak claim that naive systems are bad.
   - There is no ablation to check that each claimed property matters, such as egocentric vs. normal images for the same entities, or whether the multi-turn tasks actually require history. Fig. 4e suggests context-dependent questions are harder, but the confound with question type is not controlled.
   - The conclusion claims "inform directions for future advances" but the RQ3 insights (low-quality images are harder, tail entities are harder, multi-hop is harder) are expected and mostly correlational. There is no failure-mode taxonomy (recognition vs. retrieval vs. generation errors), even though the benchmark metadata should permit one.
   - Leakage and contamination are not discussed. This applies to public Wikipedia-derived KG content and the web corpus, and to the possibility that commercial models have seen validation/public-test content. The single-source claim (Task 1 gives only marginal gains) also leaves open that many models already recognise head entities.

7. **Venue fit, ethics and reproducibility.**
   - The paper is a benchmark and dataset paper, a good fit for ICLR's datasets track. But the scholarly contribution is mostly engineering and data collection, with limited methodological novelty. The main text is dense with numbers and much of the key detail (recall computation, annotation guidelines, industry-system protocol, additional models) sits in appendices.
   - Egocentric images captured by vendors in daily life may include bystanders, faces, licence plates and private locations. The paper does not say how consent, face/PII blurring and licensing were handled, nor the licence of the released data and of web-crawled pages. The web corpus (800K pages) has copyright/redistribution implications.
   - The test set is partly hidden and was used in a public competition, so a gap exists between what is released (validation + public test, 60%) and what the headline numbers measure (private test for winners, public for everything else).
   - The authors are all from the organisation that built the glasses and hosted the challenge. That is not a flaw in itself, but evaluation of closed commercial systems with competitor products should be reproducible by outsiders.

8. **Presentation.** There are typos and inconsistent terms (e.g. "winnings' solutions", "this pace", unclear "Hallu." vs "Accurate"/"Incorrect" labels). Table 4's caption says "Even the best MM-LLM achieves only 18%..." while the text describes "accuracy" and "truthfulness" interchangeably in places (e.g. "improved the accuracy to 50%", "improved only to 32% truthfulness"). Fig. 4 is hard to read as extracted, and there are no error bars.

## Questions

1. Please reconcile the dataset statistics (6.5K vs. 8K conversations; 15% vs. 18%/14% low-quality images). What exactly are the sizes of the validation, public test and private test sets, per task and per domain?
2. How is "+28%" computed, and what is the baseline score of the Llama 3.2 11B RAG baseline on the private test set? What would an "always abstain" baseline score? Please give accuracy/coverage trade-offs for all systems.
3. How many examples were used to validate the GPT-4o judge, and what is the human–judge agreement (kappa), particularly for the Incorrect class where precision is 68%? Do the results change with a different judge (e.g. an open model, or a GPT-5-family judge)? Is there a self-preference bias for GPT-family answers?
4. What fraction of Llama-generated multi-turn turns were edited, rewritten or removed by annotators? Does Llama (as the data generator) have an advantage on the multi-turn tasks? How would the rankings change with a different generator?
5. How were commercial systems queried (dates, versions, whether the image was supplied directly, whether with web search enabled)? How are answers affected by temporal drift in prices and availability? Do you re-verify ground truth?
6. What are the per-slice sample sizes in Fig. 4, and how large are the confidence intervals? For example, how many "occluded/rotated" egocentric examples are there (only 116 and 161 in total)?
7. How do the egocentric and normal images compare for the same entities? Does the egocentric property itself, rather than entity popularity or domain, cause the performance drop?
8. How were privacy (faces, bystanders, locations), consent and licence terms handled for the egocentric images and web pages?
9. How well does the CLIP-based KG retrieval, with 52% recall of the full image, reflect what realistic recognisers (e.g. detector + crop + stronger encoders) would achieve? Is the benchmark intended to measure retrieval or generation capability?

## Ratings

- **Soundness: 2/4.** The benchmark design is sensible, but the metric is dominated by abstention, the judge is only partially validated, the comparison of winners/industry/baselines is not like-for-like, and the statistics are inconsistent.
- **Presentation: 2/4.** Clear overall structure, but numerical inconsistencies, loose terminology and key details in appendices.
- **Contribution: 3/4.** Useful, relevant resource with the egocentric images and retrieval APIs. Limited methodological novelty, and the insights are largely expected.

**Rating: 6** (marginally above the acceptance threshold). The resource is valuable and fills a real gap for wearable MM-RAG, with a retrieval environment more complete than most prior benchmarks. However, the reporting and evaluation weaknesses above (misleading headline gain, inconsistent statistics, judge validation, unfair comparison with commercial systems, missing strong baselines, no privacy discussion) should be fixed. If those are addressed in the rebuttal, I would be comfortable supporting acceptance.

**Confidence: 4/5.** I am familiar with VQA/RAG benchmark design. I could not view the figures, and the appendix sections after C.1 were not in the extracted text.
