# Review: Structured Attention Matters to Multimodal LLMs in Document Understanding

(Figures were not available. Attention maps and Figures 3 and 6 are judged from captions and text only.)

## Summary
The paper studies how input format affects MLLM document QA. It makes three claims:
1. Raw OCR text alongside page images can hurt performance (Obs. 1).
2. Having an MLLM rewrite the OCR text and image into "structured" LaTeX (sections, tables, figure placeholders) and feeding that with the image improves accuracy (Obs. 2).
3. Attention analysis shows that structured text yields "structured attention", which is "the key" to the improvement (Obs. 3).

Experiments use four 7B MLLMs (Qwen2-VL, Qwen2.5-VL, LLaVA-1.6-Mistral, Phi-3.5-Vision) on MMLongBench-Doc, LongDocUrl, PaperTab and FetaTab. Evidence pages are given (closed domain) or taken from top-1 retrieval. Answers are judged by Llama-3.1-8B.

## Strengths
- The question is practical: how should OCR/layout information be presented to a general MLLM, with no training and only API-level access?
- The method is simple and cheap to adopt.
- It is evaluated on four models and four benchmarks, with ablations on text-only inputs (Table 2) and per-evidence-type results (Table 3).
- The ablations include "structured text only", which is reported to be worse than image plus text. This is an honest and useful negative result.

## Weaknesses
1. **The paper's own results do not support Observation 1 or the headline claim.**
   - In Table 1, image+OCR beats image-only on average for all four models: 0.300 vs 0.272, 0.427 vs 0.314, 0.219 vs 0.116 and 0.261 vs 0.161. The only degradation is on MMLongBench, for Qwen2-VL (0.292 to 0.287) and Qwen2.5-VL (0.389 to 0.375). That is a 1–2 point drop with no variance estimate. "OCR often impairs performance across multiple datasets" is overstated; the data say OCR mostly helps.
   - Structured text is not clearly better than plain OCR either. For Qwen2.5-VL, structured text gives an average of 0.371 vs 0.427 for OCR+image. On LongDocUrl it gives 0.221 vs 0.399, a large loss. On MMLongBench it gives 0.435 vs 0.375, a gain. For Qwen2-VL the average is 0.313 vs 0.300, and for LLaVA it is 0.222 vs 0.219, which is essentially a tie.
   - The percentage gains in Table 1 appear to be relative to image-only. That is the weakest baseline and is not the right comparison for a claim about *structure*.
2. **The comparison is confounded, so "structure" is not isolated.**
   - The structured text comes from an extra MLLM pass that sees both the image and the OCR. The paper does not say which model performs this pass, and the prompt is not given.
   - That pass adds compute, denoises OCR errors, summarizes, may hallucinate or inject answer-relevant content, and amounts to a second reading of the page.
   - Controls that are missing:
     - OCR text rewritten by the same MLLM without LaTeX, e.g. plain text, Markdown, HTML or JSON tables.
     - OCR with layout, i.e. reading order or boxes.
     - Structuring by a different or stronger model.
     - A length-matched control.
     - A "transcribe/caption the page" baseline.
   - Without these, the gain cannot be attributed to the LaTeX paradigm or to structure, which is exactly what the title and abstract claim.
3. **The attention analysis is weak and the causal claim is unsupported.**
   - The evidence is one aggregate distribution (Fig. 3) over 370 samples, one qualitative example (Fig. 5), and layer-wise attention weights (Fig. 6).
   - The method (following a [CLS]-attention token-pruning paper) is under-specified. It does not say which tokens or layers are aggregated, how attention is normalized when the prompt length changes (structured text adds many tokens), or how the 370 samples were chosen.
   - "Less scattered attention" and lower border-token attention are not quantified. Examples of what could be reported are attention mass on ground-truth evidence regions, entropy, and a split by correct vs incorrect answers.
   - Attention is not shown to be causal. There is no intervention, such as masking or steering attention, and no unstructured text that induces the same attention pattern.
   - "Structured attention is the key" and "directly improves the abilities" are therefore unsupported. The OCR-text attention condition is also never analyzed, so why OCR causes "dispersion" is not shown.
4. **Evaluation rigor.**
   - The Llama-3.1-8B judge is not validated against human judgment or the benchmarks' standard metrics. It is unclear whether the baseline numbers, taken from the cited framework, use the same judge.
   - There are no seeds, confidence intervals or significance tests, yet several discussed effects are 1–2 points.
   - Only 7B models are tested. The paper frames the work around general-purpose MLLMs, but stronger or larger models (e.g. Qwen2.5-VL-72B, GPT-4o, Gemini) may already extract structure from images, so generalization is untested.
   - The open-domain setting uses top-1 retrieval, which mixes retrieval quality with format effects.
5. **Internal inconsistencies and overclaiming.**
   - The text says OCR lowers MMLongBench accuracy "from 0.389 to 0.370", but Table 1 shows 0.375.
   - In Table 3, the Qwen2.5-VL image+text "Avg" is 0.285, while its columns are 0.375/0.367/0.374/0.420/0.388. That is inconsistent. The image-only average (0.395) also differs from Table 1 (0.389).
   - Table 2 shows that text-only inputs (OCR or structured) are much worse than images. It supports "images are needed", not synergy between structured text and images.
   - The "more pronounced gain on charts/tables" claim is not clear from Table 3 numbers. Note that Table 3 compares against image+text for some rows and against structured text only for others, which is hard to follow.
   - The explanation that every model improves on MMLongBench "because almost all evidence pages contain tables and graphs" is speculative.
   - Words like "proves", "fully demonstrates" and "convincingly demonstrates" are not warranted.
6. **Novelty is limited.** Converting page content into structured markup (LaTeX/Markdown/HTML) with a model is a known idea, as in Nougat/MinerU-style parsing and layout-aware text serialization. The paper neither compares with nor cites this work. The related work focuses on RAG and context extension, which are not the relevant baselines.
7. **Presentation and reproducibility.**
   - The Methodology gives no algorithm, no prompts and no identification of the structuring model, and no code is mentioned.
   - The OCR text shown in Fig. 4 has character-level garbling (e.g. "Er stwhile ITC Ho te ls"), which suggests a particularly noisy OCR baseline. That would inflate the benefit of any rewrite.
   - The writing is repetitive.
   - There is no failure analysis, no cost analysis of the extra MLLM pass, and no error analysis of the structuring step.

## Questions
1. Which model produces the structured text, and with what prompt? For Qwen2.5-VL, does it structure its own input? What are the added latency and token cost?
2. How does the method compare with a plain-text or Markdown rewrite by the same model, or with an OCR-only LaTeX conversion (no image in the structuring step)?
3. Why is structured text much worse than OCR on LongDocUrl for Qwen2.5-VL (0.221 vs 0.399)? How does this fit "structured attention is the key"?
4. Can attention be reported quantitatively (mass on ground-truth regions, entropy, correct vs incorrect split) and tested with an intervention?
5. What are the variance and significance of the 1–2 point differences? Is the Llama-3.1-8B judge validated?
6. Do the results hold for stronger or larger MLLMs?
7. Please fix the numerical inconsistencies between the text, Table 1 and Table 3.

## Ratings
- Soundness: 2
- Presentation: 2
- Contribution: 2
- **Rating: 2**
- Confidence: 4
