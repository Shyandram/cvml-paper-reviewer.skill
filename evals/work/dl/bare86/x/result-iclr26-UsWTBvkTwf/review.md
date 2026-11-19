# Review: Forget-It-All (FIA): Multi-Concept Machine Unlearning via Concept-Aware Neuron Masking

*Figures were not available. Visual claims are judged from captions and text only.*

## Summary
The paper proposes FIA, a training-free method for erasing many concepts from Stable Diffusion by pruning individual weights, with no fine-tuning.

- **Saliency.** Per-weight "Contrastive Concept Saliency" is computed from |W|, the input-channel norm and an |cosine| term. It is contrasted between concept prompts ("a golf ball in a park") and base prompts ("a park"), with a one-sigma subtraction.
- **Selection.** Scores are aggregated over denoising steps (mean strength plus activation frequency). A selection that intersects a per-output-channel top-k with a layer-global top-k then yields per-concept binary masks.
- **Fusion.** Masks are fused across concepts. Neurons selected by at least a fraction α of the concepts are called "concept-agnostic" and kept. Neurons selected by fewer concepts are pruned.
- **Setting.** The pruned layer is the second FFN projection, and the sparsity is below 0.3%.
- **Results.** FIA is evaluated on three tasks and reports state-of-the-art results on all of them:
  - ten-class Imagenette forgetting (1.9% average accuracy);
  - NudeNet counts on I2P (32 detections versus 743 for SD v1.4);
  - five-artist style erasure.
- **Extras.** The paper also reports ablations, a scaling experiment to 50 concepts, and robustness to Ring-A-Bell, MMA and UnlearnDiffAtk.

## Strengths
- The problem (multi-concept erasure without per-concept fine-tuning) is practically relevant, and the method is simple, cheap and easy to apply. Run-time is about 11 s per concept, memory is constant, and no training is needed.
- Fusing masks while protecting neurons shared by many concepts is a sensible, intuitive idea. The α ablation (Table 12) shows it matters: the naïve union gives CLIP 28.32 and α=0.6 gives 29.46.
- Evaluation covers three task types and many baselines, including training-free ones (CP, UCE). It includes a forget/preserve split with a harmonic-mean score (Table 2) and a scaling study to 50 concepts.
- The component ablations (pruned layer, granularity, α) are informative. They show the choice of FFN2 matters a great deal: cross- and self-attention pruning barely forgets.
- Headline forgetting numbers are strong, and the paper includes an adversarial-robustness table.

## Weaknesses

1. **Hyperparameters are tuned per task and per concept on the evaluation metrics, which undercuts the "plug-and-play, minimal tuning" claim.**
   - Table 8 uses different r2 per concept (0.7 versus 3.0 for golf ball, parachute and gas pump). The paper defines "hard" concepts by whether forgetting accuracy is low enough under the default.
   - α differs per task (0.6 versus 0.8), chosen by watching forgetting accuracy (Fig. 5).
   - r2 and α are thus selected against the same classifier-based forgetting accuracy that is later reported as the main result. Baselines use "recommended configurations" with no comparable per-concept tuning.
   - There is no held-out selection and no joint sensitivity analysis over r1, r2 and α in the main text.

2. **The evaluation likely favours FIA through prompt overlap, and the metrics are weak.**
   - The mask is derived from templated prompts ("a <concept> in/near a <place>"), and the Imagenette evaluation prompts follow the same template family. Whether the test prompts are disjoint from the 30 `<place>` strings used for mask construction is not stated.
   - There is no evaluation on paraphrases, synonyms, unrelated contexts, or concepts embedded in compositional prompts.
   - Forgetting accuracy from a ResNet-50 says nothing about residual visual traces.
   - For art styles, CLIPa (CLIP score between the artist-name prompt and the image) and FSR conflate style removal with general degradation and prompt misalignment. FSR is a per-prompt "any decrease" indicator with no margin. There is no style classifier or human study.
   - Preservation is measured only on the other Imagenette classes and COCO-30K CLIP/FID. There is no check that related or neighbouring concepts survive. Examples: erasing "church" versus other buildings, "Van Gogh" versus other post-impressionists, or "naked" versus clothed people.

3. **The quality-preservation claim is overstated.**
   - Table 1 shows FIA's CLIP (29.56) is about 1.9 points below SD v1.5 (31.42) and below most fine-tuning baselines. The text calls the baselines' advantage "marginal" while noting they forget far less.
   - FID is not reported for Imagenette.
   - The comparison is a Pareto trade-off, not a clean win. CP, the closest method, also forgets well (7.3% versus 1.9%).
   - The conclusion says the paper "resolves the core trade-off", yet the Limitations section admits quality degrades as concepts scale.

4. **Reported numbers are internally inconsistent, and the statistics look unreliable.**
   - FIA's CLIPcoco is 29.56 in Table 1, but the same configuration gives 29.46 in the α=0.6 column of Table 12, the FFN2 column of Table 13 and the "Both" column of Table 14.
   - On explicit content, "Both" in Table 11 gives total 32 with CLIP 31.38, whereas Table 3 and the FFN2 column of Table 10 give total 32 with CLIP 31.18.
   - Table 10 is labelled "Imagenette classes" but contains NudeNet categories.
   - The CP average in Table 5 (27.90) does not equal the mean of its per-style values (27.82).
   - The ± values added in Tables 18–20 are suspicious. FIA, CP and UCE have a standard deviation of exactly 0.0 on almost everything, including FID and CLIP over COCO-30K, while other methods have non-zero values. Either fixed seeds were used (so these are not variances) or the values were not computed.
   - Seeds, images per class and number of runs are not given. Small gaps such as 2.1 versus 2.7 (FIA versus CP in Table 2) and the average-rank gap in Table 4 come with no significance information.
   - Some baseline numbers on I2P are copied from prior papers (MACE and SA are marked †), and SD v1.4 and v1.5 are used in different tables.

5. **The average rank in Table 4 hides weaknesses.**
   - FIA is not best on FID (16.7 versus MACE 15.9) or CLIP (30.56 versus SPM 31.33). The combined rank gives equal weight to CLIPa and FSR, which are strongly correlated.
   - The advantage is almost entirely on the unlearning metrics.

6. **The method is under-motivated, and several design choices are ad hoc.**
   - Eq. (1) is a Wanda-like product with a cosine term. The cosine is between whole channel vectors over N token/spatial positions. This is a heuristic with no theory, and its contribution is not ablated.
   - Eq. (2) subtracts σ_b from the mean difference. This is neither a significance test nor a calibrated quantity, so "statistically significant" is not justified.
   - The rule that neurons shared by at least α·C concepts are retained is questionable. Such a neuron is by construction highly concept-sensitive, and if it helps encode the concepts it will leak them. The ablation shows that retaining more neurons increases residual accuracy, which exposes this tension.
   - Table 9 shows only 127–1,348 neurons are treated as agnostic out of ~207k selected, yet they change CLIP substantially. This suggests a handful of weights (possibly large-magnitude channels) dominate the effect, and that the saliency is partly picking up general-purpose high-norm weights.
   - Ablations (Tables 12–14) are all on Imagenette. They do not show whether the choices transfer to the other tasks.

7. **Robustness and "erasure" claims are weak.**
   - UnlearnDiffAtk still recovers erased content in 61.7% of cases against FIA, only marginally better than CP (64.8%).
   - The arrows in Table 15 are unexplained (Ring-A-Bell and MMA ↑, UnlearnDiffAtk ↓).
   - Pruning ~0.06% of weights using a few templated prompts may remove only the surface route to a concept. There is no test with fine-tuning recovery, concept inversion or embedding probing.
   - Explicit-content experiments use only two concept words ("naked", "sexual"). Categories such as violence are not covered, and NudeNet is used at a single threshold. Some counted classes (armpits, belly, feet) are not really harmful, and FIA's "Genitalia (M)" count (8) is not better than SD's (7).

8. **Novelty relative to existing work is limited, and positioning is imprecise.**
   - The closest work is ConceptPrune (Chavhan et al., 2024), which also prunes FFN neurons using concept/neutral activation contrast, and Jia et al. on sparsity for unlearning. The "first unstructured neuron masking for multi-concept unlearning" claim rests on a narrow reading.
   - The deltas (a different saliency score, temporal aggregation and mask fusion) are incremental. No ablation puts ConceptPrune's scoring inside the same fusion pipeline, so the gain from the saliency versus from the fusion is not isolated.
   - Related-work descriptions contain errors. COGFD is cited with ESD's reference, and ESD is described in the introduction as using "an LLM-derived concept graph and adversarial feature decoupling", which is COGFD. An SDXL paper and a graph-neural-network systems survey are cited as machine-unlearning references.

9. **Scale and reproducibility.**
   - Experiments use SD v1.4/1.5 only. There is no SDXL, SD3 or DiT model, although the introduction cites such models. The FFN2 choice may be U-Net-specific.
   - The code is "to be released".
   - The claim that "up to 45 concepts" is acceptable depends on arbitrary thresholds. The 50-class experiment uses extra classes chosen because ResNet-50 can reliably identify them.

## Questions for the authors
1. Are the evaluation prompts disjoint from those used to build the masks (placeholders and templates)? What are the results with paraphrases, synonyms (e.g. "cathedral" for church), and new contexts?
2. Please report joint sensitivity to r1, r2 and α, and a protocol for choosing them without the evaluation classifier. What happens with a fixed r2 for all concepts, or if the baselines are tuned equally?
3. Why do CLIPcoco values for the identical FIA configuration differ across Tables 1, 3 and 10–14? Why are the standard deviations exactly 0.0 for FIA, CP and UCE? How many seeds and images were used?
4. Can you ablate each factor in Eq. (1) and the σ_b term in Eq. (2), and run ConceptPrune's saliency inside your fusion pipeline?
5. What are the 127–1,348 concept-agnostic neurons (layers, channels)? Are they high-magnitude channels? Does keeping them leak concepts under white-box attacks?
6. How does erasing one concept affect semantically related ones? Can you provide FID/CLIP on Imagenette and a style classifier or user study for artist erasure?
7. Do the results transfer to SDXL/SD3 or other architectures, and is FFN2 still the right layer?
8. Can the pruned model recover concepts after a small amount of fine-tuning or with textual inversion?

## Soundness: 2
## Presentation: 2
## Contribution: 2

## Rating: 4

## Confidence: 4

**Justification.** The method is simple and appealing, and the headline numbers are strong. The evidence has several problems:
- hyperparameters tuned on the evaluation metric;
- weak style and preservation metrics;
- internal inconsistencies and implausible zero-variance statistics;
- a modest conceptual step over ConceptPrune and related sparsity work;
- limited robustness evidence for pruning-based erasure.

I would raise the score if the evaluation were held out, the inconsistencies explained, and the saliency and fusion contributions isolated.
