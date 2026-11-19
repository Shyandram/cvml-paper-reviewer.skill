# Academic Paper Review — "From Coarse to Fine: Recursive Audio-Visual Semantic Enhancement for Speech Separation"

*Skill v2.10.1, full mode. Request: target venue ICLR, skip confirmation, literature check strict (cutoff 2025-09-24). Date: 2026-11-10. This is a simulation of how a careful panel might see this draft, not a prediction of any outcome.*

**Disclosures.**
- The five reviewer passes were run one after another in a single shared context (no subagents). Each was written from its own role file, its own angle, and the shared Phase 0 paper memory. Independence is therefore partial.
- Figures are not available in the extracted text. Claims that depend on Figures 1–8 are judged from captions and surrounding text only, and are marked "unverifiable (figure)" where it matters.
- **Literature check (strict, cutoff 2025-09-24): attempted, not completed.** `related_search.py search` was tried twice (query "audio-visual speech separation", claim C1). Both attempts failed with `arXiv API unreachable (HTTP Error 429)`. No query was logged as kept. Per `references/literature_search.md`, Phase 1.5 fell back to "off": the Domain Reviewer used the paper's own related work and prior knowledge, and entries it is not certain about are marked `[verify]`. No search ledger or similarity/novelty run exists, so no text-overlap check was done. The "novelty" statements below are therefore not backed by retrieved abstracts.
- **Integrity scan:** `integrity_scan.py` found no reviewer-directed text or hidden characters. Nothing in the paper addresses reviewers or AI systems. The reviewers read the paper text itself.

---

# PHASE 0 — Field Analysis and Reviewer Configuration

## 📋 Paper Analysis

| Item | Finding |
|------|---------|
| Title | From Coarse to Fine: Recursive Audio-Visual Semantic Enhancement for Speech Separation |
| Primary Discipline | Audio / speech processing → audio-visual speech separation (multi-speaker, monaural mixture + lip video) |
| Secondary Discipline(s) | Audio-visual speech recognition (AVSR); multimodal fusion; time-frequency-domain separation networks |
| Paper Type | Empirical (new method + benchmark evaluation); composite weights: empirical |
| Core Technique(s) | Two-pass (coarse → fine) separation; pretrained Auto-AVSR video/audio encoders reused on the coarse output; MLP-based speaker-wise fusion (SP); TF-GridNet-derived multi-range separator (MST) |
| Target Venue | ICLR 2026 (stated by user); profile key `iclr`, scale status *secondary*. Accepted share ≈ 27% of submissions |
| Venue-Specific Notes | None (no ECCV/ACM-MM/TPAMI rules). ICLR scope fit: audio / multimodal applications are in scope (the paper's own bibliography has ICLR/ICML AVSS precedents [21], [49]) |
| Paper Maturity | Submission-ready draft ("A PREPRINT - SEPTEMBER 29, 2025" header) |
| Ethics-Relevant Content | Identifiable faces and voices from LRS2, LRS3, VoxCeleb2 (web/TV/YouTube); §1 motivates passive capture "through telephoto cameras"; no limitations or broader-impact section; LLM-use statement present (Appendix A) |

### Claimed Contributions (as stated by the authors, §1)
1. **C1.** CSFNet: a coarse-to-fine framework that "recursively enhances semantics by feeding coarse audio back into a AVSR model" (§1, contribution 1; Figure 2; §3.1).
2. **C2.** A speaker-aware fusion block (SP, §3.2.3) and a multi-range spectro-temporal network (MST, §3.2.4) "improving robustness to modality degradation and capturing multi-scale T-F patterns" (§1, contribution 2).
3. **C3 (result claim).** New SOTA on LRS2/LRS3/VoxCeleb2 and two noisy sets, "primarily due to the introduction of the fine separation stage", incl. "a 10% reduction in word error rate" (§1, Abstract).

### Paper memory (shared with all reviewers; factual record)
- **Setup.** Datasets: LRS2, LRS3, VoxCeleb2 (2–4 speaker mixtures, SNR in [−5, 5] dB, 2 s clips, §4.1 / Appendix D.1); NTCD-TIMIT and LRS3+WHAM! for noisy conditions (Appendix D.2). Splits: "followed the protocols established in prior work [49, 21]"; test speakers "strictly disjoint" (Appendix D.2). Sizes of splits: not stated.
- **Architecture.** Audio encoder (Eq. 1) → SP fusion with Auto-AVSR video features → MST (6 blocks, H = 96, 4 heads, C = 192) → decoder. Stage 2 feeds coarse audio + lips into the same Auto-AVSR (VSR + ASR encoders + MLP; Appendix B), then a separator "finetuned based on the coarse separation stage" (§3.1, Figure 2 caption).
- **Training.** Adam; batch 16 / 8 and LR 1e-3 / 1e-4 (coarse / fine); ReduceLROnPlateau on validation loss; up to 200 epochs; 8×A100 40 GB; magnitude + SI-SDR loss with PIT (§4.2, Appendix E). Seeds, number of runs, code release, training time: not stated after search. Whether Auto-AVSR is frozen, and whether the coarse network is frozen during stage 2: not stated.
- **Headline numbers.** Table 1: fine vs coarse +0.6 / +0.8 / +0.7 dB SI-SDRi on LRS2 / LRS3 / VoxCeleb2; Table 4: +0.6 / +2.1 / +3.8 dB for 2 / 3 / 4 speakers; Table 5: WER; Table 3: noisy sets; Table 2: cost (10.9 M params, 64.8 G MACs, 117.39 ms).
- **Appendix.** B (Auto-AVSR), C (Table 6, separator hidden size), D (datasets), E (loss), F (missing-visual-frame protocol), G (face encoder, Table 7), H (spectrograms, Figure 8).
- **Unverifiable.** Figures 1–8 (extracted text only has stray numbers for Figures 4–5); no supplement referenced.

## 👥 Review Team (fictional personas)

### EIC (meta-reviewer): Dr. Ingrid Valmont, speech and audio ML group, large public research university (Northern Europe)
- **Seniority / Expertise**: Senior faculty / speech separation and enhancement, multimodal speech models
- **Role**: Reads all five reviews, checks decisive points against the paper, weights the reviewers, makes the final decision
- **Style**: Calibrates to what the venue accepts; weights evidence over volume of criticism

### Reviewer 1 (Methodology): Dr. Tomás Beltrane, industrial speech-technology lab (South America / Europe)
- **Seniority / Expertise**: Senior industry scientist / time-frequency separation networks, SI-SDR-family evaluation, latency measurement
- **Review Focus**: Research design, statistics, comparison fairness, reproducibility
- **Style**: Insists on matched compute and training budgets; recomputes every delta

### Reviewer 2 (Domain): Prof. Adaeze Lindqvist, audio-visual learning lab, mid-sized research university (West Africa / Northern Europe)
- **Seniority / Expertise**: Mid-career faculty / audio-visual speech separation and extraction, lip-reading front ends
- **Review Focus**: Literature, theoretical framework, domain contribution
- **Style**: Reads the bibliography entry behind every cited claim

### Reviewer 3 (Perspective): Dr. Rohan Idowu-Patel, hearing-technology and auditory-neuroscience institute (South Asia)
- **Seniority / Expertise**: Senior researcher / auditory scene analysis, hearing devices, on-device speech processing
- **Review Focus**: Cross-disciplinary connections, deployment, broader impact
- **Style**: Constructive and expansive; the most positive voice on the panel

### Reviewer 4 (Generalist): Dr. Sofia Kallergis, machine-learning group, European technical university
- **Seniority / Expertise**: Mid-career faculty / multimodal learning, general ML (not a separation specialist)
- **Review Focus**: Contribution clarity, venue fit, presentation
- **Style**: Typical program-committee member; weighs weaknesses against what accepted papers carry

### Devil's Advocate: Prof. Jun-seo Hartmann, evaluation-methodology group, research university (East Asia)
- **Seniority / Expertise**: Senior faculty / evaluation methodology, causal attribution in ML ablations
- **Review Focus**: Core-argument challenges, logic, overclaiming
- **Style**: Rigorous skeptic; asks what else would explain the result

*Personas are fictional. Proceeding with the stated assumptions.*

---

# PHASE 1 — Independent Multi-Perspective Review

---

# Peer Review Report

## Paper: From Coarse to Fine: Recursive Audio-Visual Semantic Enhancement for Speech Separation
## Reviewer: Dr. Tomás Beltrane, Reviewer 1 (Methodology) (industrial speech-technology lab; fictional persona)
## Expertise: time-frequency separation networks; SI-SDR-family evaluation; latency/compute measurement
## Date: 2026-11-10

---

## Summary
CSFNet separates 2–4 speakers from a mixture using lip video. A first pass produces coarse waveforms from the mixture plus lip features from a pretrained Auto-AVSR video encoder. In a second pass, the coarse waveforms and lips go through Auto-AVSR again, and a separator "finetuned based on the coarse separation stage" (Figure 2 caption) produces the refined output. A simple MLP-based fusion (SP) and a multi-branch TF-GridNet variant (MST) are also proposed. On LRS2/LRS3/VoxCeleb2 (Table 1), the second pass adds 0.6–0.8 dB SI-SDRi to the first. The gain grows with the number of speakers (Table 4) and WER improves (Table 5). Noisy-condition results are in Table 3.

**Protocol sweep (searched the whole text).** Split/selection statements found: "ReduceLROnPlateau scheduler… if the validation loss does not improve" (§4.2); "test speakers are strictly disjoint from the training and validation sets" (Appendix D.2); "we select H = 96 as the optimal hyperparameter" (Appendix C, split not stated). Nothing says a hyperparameter, checkpoint or configuration was selected on the reported test set. The split used for Table 6 is not stated. H = 96 is not the best-scoring row (H = 192 scores 17.1/17.3 vs 16.8/16.9), so it is a cost trade-off. No test-selection issue is raised.

**Omission sweep.** Split sizes: not stated. Seeds / number of runs / variance: not stated. Code: not stated. Hardware: present (§4.2). Training time: not stated. Frozen vs trainable Auto-AVSR, and whether the coarse network is frozen in stage 2: not stated. Which recogniser computes "Output WER" (Table 5): not stated. Mixture-input WER: not stated.

## Claim-to-evidence map

| ID | Claim | Where | Evidence | Verdict |
|----|-------|-------|----------|---------|
| C1 | Recursively feeding coarse audio into AVSR produces "more discriminative" semantics that improve separation | Abstract, §1, §3.1 | Table 1, 4, 5; Table 7 | Partially: the gain is real, the cause is not isolated (W1) |
| C2a | SP block is robust to missing visual input | §1, §3.2.3 | Figure 5 (unverifiable from text) | Partially: only vs. plain concatenation, 2-speaker design extended to 5 without explanation |
| C2b | MST captures multi-scale patterns and is efficient | §3.2.4, Table 6 | Table 6 | Partially: range and hidden size are confounded; setting unstated (W3) |
| C3 | SOTA, "primarily due to" the fine stage | §1, Table 1, 3 | Table 1, 3 | Partially: see W2 (cost) and W4 (baselines); RTFS-Net absent |
| C4 | "efficiency performance trade-off" | §4.4.2 | Table 2 | Not supported as stated (W2) |
| C5 | "10% reduction in word error rate" | §1 | Table 5 | Cannot be reproduced (ERR-2) |

## Strengths

### S1: A clear, easily testable idea with consistent first-order evidence
Re-using an AVSR model on the first-pass audio is simple to describe (Figure 2) and the coarse→fine delta is positive on every dataset (Table 1: 0.6/0.8/0.7 dB, recomputed) and every speaker count (Table 4: 0.6/2.1/3.8 dB, recomputed).

### S2: Broad evaluation axes for an AVSS paper
Three clean datasets, 2–4 speakers (Table 4), two noisy sets (Table 3), a dynamic-mixing setting (Table 1), WER as a content-preservation metric (Table 5), and missing-frame protocols (Appendix F) go beyond the usual single-metric table.

### S3: Useful component-level ablations and honest negative-ish findings
Appendix C shows the diminishing return of H (Table 6: 16.8 → 17.1 dB for 10.9 M → 26.3 M parameters), and Appendix G / Table 7 reports that adding face information stops helping after stage 2. Reporting this is good practice.

### S4: Training details are mostly specified
§4.2 gives optimizer, LR, batch sizes, schedule, epochs, clipping, window/hop, C, N, B. Appendix E gives the loss. Appendix F gives the occlusion protocol.

## Weaknesses

### W1 (MAJOR): The central causal claim is not isolated from "a second, further-trained network pass"
The paper attributes the gain to "recursive semantic enhancement" (Abstract: "validating the necessity and effectiveness"). But the fine system is a *second separator initialized from and finetuned on the first* (§3.1; Figure 2 caption: "the fine separation network is finetuned based on the coarse stage"), trained for up to another 200 epochs (§4.2: "The maximum number of training epochs is 200"), and it additionally consumes the coarse waveform through an extra pretrained ASR encoder. Competing explanations are not ruled out: (a) more training and capacity; (b) any two-pass or iterative refinement; (c) extra information from a strong pretrained audio encoder, independent of "AVSR semantics". Indirect hints point toward (b)/(c): in Table 7 the fine gain shrinks from 0.6 dB (lip-only, 16.2→16.8) to 0.3 dB (lip+face, 16.5→16.8), and both end at the same 16.8, which looks like a ceiling set by something other than the visual semantics.
- **Suggested Fix:** add controls on LRS2-2Mix (and 4Mix, where the effect is largest): (i) the same two-pass pipeline with *no* video (audio-only CSFNet, 2 passes); (ii) stage-2 fed the coarse audio through a *non-AVSR* encoder of equal size; (iii) the coarse model simply trained 200 more epochs; (iv) IIANet or AV-CrossNet run as a two-pass cascade with matching budget. Roughly 4 extra trainings × ~1–2 GPU-days on 8×A100 ≈ 1–2 weeks of cluster time; (i) and (iii) are the cheapest and most informative.

### W2 (MAJOR): The efficiency claim and Table 2 do not account for the two-stage system, and the comparison mixes training regimes
Table 2 lists CSFNet at 64.8 G MACs, 10.9 M params and 117.39 ms. Table 6's "MST, H = 96" row has exactly the same numbers (10.9 M, 64.8 G, 117.39 ms), i.e. one separator pass. The deployed system needs the first-pass separator, the second-pass (finetuned) separator, a VSR encoder (ResNet-18 + 12 Conformer blocks, Appendix B), and an ASR encoder (1-D ResNet-18 + 12 Conformer blocks), the last run once per speaker on the coarse output. The text then concludes: "most approaches rely on pretrained models, which do not introduce a significant increase in computational cost" and "clearly demonstrating the efficiency performance trade-off of our design" (§4.4.2). In addition, Table 2's CSFNet SI-SDRi (17.5) is the *dynamic-mixing* fine result from Table 1, while IIANet's 16.0 and the others (except AV-CrossNet) are the non-DM rows. Under the like-for-like non-DM setting the gap to IIANet is 16.8 − 16.0 = 0.8 dB, at 3.5× params and 3.5× MACs (10.9/3.1, 64.8/18.6, recomputed) before counting the second pass.
- **Suggested Fix:** report end-to-end params, MACs, latency and memory for the complete two-pass inference including both AVSR branches, state whether pretrained encoders are counted for every baseline, and use matched DM/non-DM rows. Measurement only: < 1 GPU-day.

### W3 (MAJOR): Component ablations do not isolate what is claimed for SP and MST
Table 6 compares TF-GridNet (H = 256) with MST at H = 64–192, so multi-range unfolding and hidden size change together; there is no MST with a single branch at H = 96, nor ablations of the I = 4, 8 choices (§3.2.4). The setting of Table 6 is not stated: the MST H = 96 row (16.8/16.9) equals the *fine-stage* numbers in Table 1 whereas the coarse stage is 16.2/16.3, which matches the TF-GridNet row (16.2/16.4). The reader cannot tell whether MST beats TF-GridNet in the coarse stage. SP fusion is only compared with plain concatenation (Figure 5; values not recoverable from the text), not with attention-based fusion that the paper says it replaces (§3.2.3, "[32, 31, 33, 10]").
- **Suggested Fix:** state the stage and split for Table 6; add (a) MST with one branch at matched parameters, (b) SP vs. one attention-based fusion at matched parameters. ~2–3 GPU-days.

### W4 (MAJOR): Baseline provenance and the noisy-condition comparison are weak
Table 1 mixes baselines copied from other papers (AV rows, no marker) with baselines "reproduced by our implementation" (only the audio-only TF-GridNet and Crossnet, marked ∗). Table 3 copies baselines from [35] ("Comparison results are from [35]") and omits the strongest AV methods used in Table 1 (IIANet, CTCNet, AV-CrossNet). It does not state which CSFNet variant (coarse/fine, DM or not) is reported. CSFNet reaches PESQ 2.72 and eSTOI 0.91 on LRS3+WHAM! vs. AVLiT's 1.52 / 0.68 while the SI-SDRi gap is only 2.3 dB (14.71 vs 12.42). That is a large perceptual jump that depends on whether the training distribution matches that of [35]. RTFS-Net [49] is cited only for the dataset protocol (Appendix D.2) and is not in Table 1. Whether the pretrained Auto-AVSR saw the LRS2/LRS3/VoxCeleb2 test utterances is not stated.
- **Suggested Fix:** mark copied vs. retrained numbers, add IIANet / CTCNet / AV-CrossNet (retrained on the Table 3 data) and RTFS-Net to Tables 1 and 3, state the variant, and state the Auto-AVSR training data and its overlap with the test sets.

### W5 (MAJOR → MINOR, see Error Log): No variance, and several text/table inconsistencies
All results are single numbers; no seeds or intervals (omission sweep). The coarse model beats IIANet by only 0.2 dB (§4.4.1: "an increase of around 0.2 dB"), so "SOTA" at the coarse stage cannot be distinguished from noise. The fine-vs-coarse gain (0.6 dB) is probably above noise but unquantified. Inconsistencies: ERR-1…ERR-5 below.
- **Suggested Fix:** 3 seeds of the coarse and fine models on LRS2-2Mix (≈ 3× training; or bootstrap CIs over test mixtures, ≈ minutes) and report mean ± std.

### W6 (MINOR/MAJOR): Reproducibility
No code or checkpoint statement; whether Auto-AVSR and the stage-1 model are frozen during stage 2 is not stated; how the "three cross-modal feature representations" for a 2-speaker mixture arise (§3.2.3) and how SP extends to 3–5 speakers is not stated; training time not given.
- **Suggested Fix:** release code, add a training-procedure pseudo-algorithm and the SP formulation for N speakers.

### Error Log

| ID | Category | Location | Verbatim quote | Why it is an error | How verified | Confidence | Severity | Fix |
|----|----------|----------|----------------|--------------------|--------------|------------|----------|-----|
| ERR-1 | E6 | §4.4.1 | "we observe that MAVINet still delivers gains over strong audio-only baselines" | "MAVINet" is never defined; the method is CSFNet | Text search of the whole paper | High | MINOR | Fix the name; clarify what is compared |
| ERR-2 | E1 | §1 vs Table 5 | "leading to a 10% reduction in word error rate (WER) on the LRS2-2Mix dataset" | Table 5 gives 22.75 → 18.89 for Auto-AVSR (3.86 abs. points = 17.0% rel.); 24.94→21.78 (12.7% rel.); 24.66→21.50 (12.8%). No 10% | Recomputed from Table 5 | Medium (baseline of the "10%" not stated) | MAJOR (headline number) | State the baseline and compute |
| ERR-3 | E6 / E1 | Table 2 vs Table 6 vs Table 1 | "which do not introduce a significant increase in computational cost" (§4.4.2) | Cost row (64.8 G, 10.9 M, 117.39 ms) equals Table 6 single-pass H = 96; SI-SDRi 17.5 equals the DM fine row of Table 1 whereas IIANet 16.0 is non-DM | Cross-referenced three tables | High | MAJOR | See W2 |
| ERR-4 | E6 | §4.1 / App. D.1 vs §4.5.2 | "randomly selecting 2, 3, or 4 speakers from each dataset" vs "consistently achieves the best performance across 2–5 speaker mixtures" | Fig. 5 / §4.5.2 use 2–5; data section defines 2–4 | Cross-referenced | High | MINOR | Define the 5-speaker data |
| ERR-5 | E5 / E1 | §4.4.1 vs Table 1 | "achieves a further 0.7 dB SI-SDR improvement over the previous best" | DM rows give 17.5 vs 16.8 (+0.7), 20.1 vs 18.3 (+1.8), 15.4 vs 14.6 (+0.8) | Recomputed | High | MINOR (understates) | Report all three |
| ERR-6 | E6 | Appendix C, Table 6 | "we select H = 96 as the optimal hyperparameter" | Setting (coarse/fine, split) unstated; row equals Table 1 fine rows | Cross-referenced | Medium | MINOR | State the setting |

**Minor:** Table 4 header "SI-SNRi" vs "SI-SDRi" elsewhere; Eq. (1) text says features from "Y1" while the input is Y0; "Speaker-wise" (§3.2.3) vs "speaker-aware" (Abstract); Table 2 time 62.51 ms is identical for AVConvTasNet and AVLiT; Table 6 H = 192 reports 2163.17 ms vs 165.99 ms at H = 128 (13× for 1.7× MACs), which is probably a measurement artifact.

## Missing References
*(Not my role; see Reviewer 2.)*

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Core gain is real but cause and cost are not isolated (W1, W2) |
| Clarity | 2 | Method clear at a high level; protocol and inconsistencies (W5, W6) |
| Significance | 2 | 0.6–0.8 dB at ≥ 2× pipeline cost; unclear generality |
| Originality | 2 | Two-pass refinement with AVSR re-use; simple fusion; TF-GridNet variant |

## Dimension Scores (0–100)

**Pool position:** better than about 44% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the gain over the closest prior work is small (+0.2 dB at the coarse stage, +0.8 dB at the fine stage vs. IIANet) and the claimed cause is not isolated; cost accounting is incomplete; no variance.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 50 | Developing | W1–W3; sound pipeline but causal and cost claims not supported |
| Clarity & Presentation | 56 | Competent | Understandable; inconsistencies and unspecified stage-2 protocol |
| Novelty & Originality | 50 | Developing | Incremental (see R2) |
| Significance & Impact | 50 | Developing | Niche gain at higher cost |
| Experimental Validation | 48 | Developing | Missing controls, copied baselines, single runs |
| Reproducibility | 50 | Developing | Hyperparameters given; no code, seeds, frozen/unfrozen details |
| Ethical Compliance | 56 | Competent | No limitations/impact discussion, see R3 |

## Questions for Authors
1. What is the result of a two-pass model with no video (or a non-AVSR second-pass encoder) at matched epochs? A gain close to 0.6 dB would sharply lower the "semantic" attribution; a much smaller gain would raise my score.
2. What are the full inference params/MACs/latency of the two-pass system including both AVSR branches, and are pretrained encoders counted for the baselines in Table 2?
3. Is Table 6 evaluated at the coarse or fine stage, and on which split?
4. Which recogniser computes Output WER in Table 5, and what is the mixture-input WER and the oracle (clean-source) WER?
5. Does the pretrained Auto-AVSR's training data include any of the test utterances or speakers?

## Limitations Assessment
**Partially.** There is no limitations section. Cost, 2-speaker design of SP, reliance on a strong pretrained AVSR, and synthetic mixtures should be discussed.

## Ethics Review Flag
**No** (see R3 for a recommended impact statement).

## Overall Score
**3 (Borderline Reject)**: A real but modest, unattributed gain; incomplete cost accounting; no variance.

## Confidence
**4**: I recomputed the deltas and cross-checked tables; figures were unavailable.

---

# Peer Review Report

## Paper: From Coarse to Fine: Recursive Audio-Visual Semantic Enhancement for Speech Separation
## Reviewer: Prof. Adaeze Lindqvist, Reviewer 2 (Domain) (audio-visual learning lab; fictional persona)
## Expertise: audio-visual speech separation / extraction; lip-reading front ends
## Date: 2026-11-10

---

## Summary
The paper argues that AVSS systems that use AVSR-derived semantics (e.g., [22], [23]) feed the AVSR model video only, so the semantics are ambiguous. It therefore passes the first-pass separated audio, together with video, back into the AVSR model, and adds a simple speaker-wise fusion block and a multi-branch TF-GridNet-like separator. The empirical claim is a consistent gain on LRS2/LRS3/VoxCeleb2 and noisy sets over IIANet, AV-CrossNet and AVLiT.

## Strengths

### S1: A well-motivated, specific gap
§1 and §2 identify a concrete limitation of AVSR-based AVSS: "these approaches still rely solely on visual input", and tie it to the finding that video-only AVSR is weaker than AV (Table 5: Auto-AVSR visual-only 30.67 vs 20.03 with coarse audio).

### S2: Correct, current choice of AVSR front end and comparison with recent AVSS
Using Auto-AVSR (a stronger front end than the word-level or Deep-AVSR models earlier methods used) and comparing to IIANet [21] (ICML 2024), CTCNet [20] (TPAMI 2024), AV-CrossNet [22] and AVSepChain [23] in Table 1 positions the work against current AVSS.

### S3: An informative front-end study
Table 5 swaps CTCNet-Lip, Deep-AVSR, AV-HuBERT and Auto-AVSR, showing that a better front end gives lower output WER (22.75 for Auto-AVSR vs 24.94 / 24.66 / 25.03), which is useful for the community.

### S4: Standard benchmark protocols reused
Appendix D follows [49] and [21] for partitioning, which makes comparison with the ICLR 2024 / ICML 2024 line possible.

## Weaknesses

### W1 (MAJOR): Novelty is incremental and the closest iterative/AVSR-based prior work is not differentiated
The delta over [22], [23] is feeding the first-pass audio into the AVSR audio branch. The paper compares empirically with AVLiT [35] (a "lightweight iterative model", per its own reference) in Tables 1–4 but §2 never discusses iterative or multi-stage separation. The reader cannot see how "recursive semantic enhancement" differs from iterative refinement beyond the re-use of Auto-AVSR. The abstract's "new paradigm" framing ("recursive semantic enhancement paradigm") is not matched by a comparison against cascades that do not use AVSR.
- **Suggested Fix:** add a related-work paragraph on iterative/cascaded separation and a baseline of this kind (see R1-W1).

### W2 (MAJOR): State-of-the-art comparison omits the closest ICLR-venue AVSS baseline and mixes protocols
RTFS-Net [49] is cited only for the dataset protocol (Appendix D.2) and absent from Tables 1 and 3, although it is a prior ICLR AVSS method on the same benchmarks. The noisy comparison (Table 3) uses older baselines from [35] and omits IIANet / CTCNet / AV-CrossNet. The audio-only SOTA TF-GridNet and CrossNet are reproduced by the authors (marked ∗ in Table 1), while all AV rows are copied.
- **Suggested Fix:** include RTFS-Net and retrain at least two recent AVSS baselines on the Table 3 data.

### W3 (MAJOR): Citation errors that bear on positioning (E7)
(a) §1 cites "[6, 7, 8, 9, 10]" as early audio-only methods; bibliography entry [10] is "Audiovisual Speaker Separation with Full-and Sub-Band Modeling in the Time-Frequency Domain", an audio-visual paper. (b) Table 1 labels "DPCL++ [5]", but [5] is the original Deep Clustering paper; DPCL++ is a later extension [verify]. (c) §2 cites "[30, 16]" for "robustness in noisy and overlapping speech conditions", where [30] is a human fMRI study; it supports the premise that visual input helps people but not any robustness claim for models. (d) Early classical methods (ICA, NMF, §2) are uncited.
- **Suggested Fix:** correct the citations and align each claim with its source.

### W4 (MINOR/MAJOR): Theoretical framing is thin
"More discriminative and speaker-aware semantic representations" (§1; Appendix B: "richer and more discriminative") is asserted. There is no representation-level evidence beyond WER (e.g., a linear probe for speaker identity or content, or a phoneme-level analysis) that the AVSR embedding computed on coarse audio carries speaker-aware information.
- **Suggested Fix:** add one probing or alignment analysis on L vs L̂ (§3.2.2).

## Missing References
*Literature check could not run (arXiv HTTP 429); entries rely on my knowledge. Entries I could not retrieve are marked [verify].*

| Priority | Reference | Why it matters |
|----------|-----------|----------------|
| Important | K. Li, R. Yang, X. Hu, "An efficient encoder-decoder architecture with top-down attention for speech separation," ICLR 2023 (TDANet) | Efficient multi-scale audio-only separator from the same group as [20], [21]; relevant baseline for the efficiency claim and the MST design |
| Important | Pegg, Li, Hu, "RTFS-Net: Recurrent Time-Frequency Modelling for Efficient Audio-Visual Speech Separation," ICLR 2024 (already [49] in the paper) | Must be compared in Tables 1 and 3, not only cited for the protocol |
| Important | U.-H. Shin, S. Lee, T. Kim, H.-M. Park, "Separate and Reconstruct: Asymmetric Encoder-Decoder for Speech Separation," NeurIPS 2024 (SepReformer) `[verify]` | Strong recent audio-only separator relevant to the audio-only baselines |
| Helpful | Z. Pan, M. Ge, H. Li, "USEV: Universal Speaker Extraction with Visual Cue," IEEE/ACM TASLP 2022 `[verify]` | Visual-cue speaker extraction; framing of what visual cues contribute |
| Helpful | Line of work: ASR- or self-supervised-feature-guided conditioning/losses for separation and enhancement; multi-stage/iterative separation | Positions "recursive semantics" relative to existing perceptual/semantic guidance; described, not named, because I cannot verify the exact entries |

## Novelty against closest prior work (built from the paper's own related work and knowledge; no retrieval)

| Claimed contribution | Closest prior work | What that work already does | What is new here | Cited and differentiated? |
|----------------------|--------------------|-----------------------------|------------------|---------------------------|
| C1 coarse→AVSR→fine | [22], [23] (AVSR semantics from video); [35] AVLiT (iterative AV separation) | AVSR semantics from video; iterative refinement of separation | Coarse separated audio is re-encoded by the AVSR audio branch | [22], [23] cited and differentiated (video-only); [35] compared but not differentiated |
| C2 SP fusion | [19], [31], [32], [33] | Concatenation and attention-based fusion | MLP per speaker + concat | Cited; no matched comparison |
| C2 MST | [9] TF-GridNet; [29] CrossNet; [49] RTFS-Net | TF-domain intra/sub-band modelling; multi-scale efficient AV separation | Multi-range unfold branches, smaller H | [9] cited; [49] not differentiated |

**Per-claim novelty (no claim profile run):** C1 incremental–medium; C2 incremental. No established claim found; no criterion-7 candidate.

**Field snapshot (from prior knowledge, before cutoff, [verify]).** Five years ago AVSS (e.g., Conv-TasNet-style AV extensions, VisualVoice) was well below 12 dB SI-SDRi on LRS2; time-frequency and cross-band networks (TF-GridNet family) and pretrained lip front ends moved 2-speaker LRS2 into the mid-teens, and recent work (IIANet, RTFS-Net, AV-CrossNet) reports gains of 0.5–2 dB with attention on efficiency. The 2-speaker benchmarks are near saturation, so what counts as significant now is either a new capability (more speakers, real recordings, robustness to missing video) or a clear efficiency gain at equal accuracy. A 0.6–0.8 dB gain at higher inference cost is incremental unless the 3–4 speaker gains (Table 4) are shown to be robust.

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Solid pipeline, but positioning and comparisons incomplete |
| Clarity | 2 | Related work thin; citation errors |
| Significance | 2 | Incremental unless multi-speaker gains hold |
| Originality | 2 | Re-use of AVSR on coarse audio; no new paradigm |

## Dimension Scores (0–100)

**Pool position:** better than about 47% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: modest, incremental novelty and an incomplete comparison with the closest prior work, partly offset by a broad benchmark suite.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 54 | Developing/Competent | Sound approach; positioning errors |
| Clarity & Presentation | 58 | Competent | Citation errors, thin related work |
| Novelty & Originality | 50 | Developing | Incremental extension of [22], [23] |
| Significance & Impact | 52 | Developing | Niche benchmark, modest delta |
| Experimental Validation | 52 | Developing | RTFS-Net and strong baselines missing in noisy table |
| Reproducibility | 54 | Developing/Competent | Standard protocols reused |
| Ethical Compliance | 56 | Competent | No limitations |

## Questions for Authors
1. How does the recursion differ from AVLiT's iterative design [35]? Would the same gain appear with an iterative baseline of equal compute?
2. Why is RTFS-Net [49] absent from Table 1?
3. Can you show representation-level evidence that L̂ is more speaker-aware than L (probe, retrieval)?
4. Can you fix the citations noted in W3 (and confirm DPCL++)?

## Limitations Assessment
**No.** No limitations section.

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: An incremental, plausible idea with a useful front-end study; positioning and comparisons incomplete.

## Confidence
**4**: I know the AVSS literature; the retrieval-based check was not available.

---

# Peer Review Report

## Paper: From Coarse to Fine: Recursive Audio-Visual Semantic Enhancement for Speech Separation
## Reviewer: Dr. Rohan Idowu-Patel, Reviewer 3 (Perspective) (hearing-technology and auditory-neuroscience institute; fictional persona)
## Expertise: auditory scene analysis; hearing devices; on-device speech processing
## Date: 2026-11-10

---

## Summary
The paper builds a two-pass audio-visual separator in which the first-pass audio is "re-listened to" by a speech recogniser together with lip video, and the resulting richer representation guides a second pass. Experiments span clean and noisy synthetic mixtures with 2–4 speakers, and degradations of the visual stream. The work is framed by the cocktail-party problem and human audiovisual perception (§1, refs [1–4], [30]).

## Strengths

### S1: A natural, biologically flavoured closed loop
Using a recogniser on a first estimate, then re-estimating, resembles analysis-by-synthesis and top-down expectation in auditory scene analysis. The paper's §1 motivation ("recursively integrate coarse separated audio into the AVSR model") is a good, reusable principle for other multimodal enhancement tasks.

### S2: Attention to degraded visual input
Section 4.5.1 and Appendix F define systematic missing-frame protocols (one or both speakers, 5–50 frames or all), and the authors report that the second stage "consistently outperforms the coarse-only stage". Visual-degradation testing is rarely done and is valuable for deployment (motion blur, occlusion, low light, §4.5.1).

### S3: Scaling with speaker count
Table 4 shows the second stage helps most for 4 speakers (+3.8 dB), which is the practically harder regime (meetings, group conversation).

### S4: Cost reported at all
Table 2 reports MACs, params, time and memory on a stated GPU, more than many separation papers do (but see R1-W2 for completeness).

## Weaknesses (opportunities)

### W1: Deployment and real-world gap (Table 2; §4.1; Appendix D)
All mixtures are synthetic sums of independent clips with SNRs in [−5, 5] dB (Appendix D.1), with no room reverberation and no real recordings. Latency is measured for 1 s of audio on an A100 (Table 2: 117.39 ms; excluding the second pass and AVSR branches, see R1-W2). For hearing devices or video-conferencing the relevant numbers are streaming/causal latency and on-device cost; the model uses non-causal 2 s clips (Appendix D.1).
- **Suggested Fix:** report a real-time factor for the full pipeline on a modest GPU/CPU, and test on a small set of real (non-synthetic) overlapped recordings, or acknowledge the limitation.

### W2: Assumptions that go unchallenged (§3.2.3, Appendix F)
(a) A tracked, correctly detected face/mouth crop is available for every speaker (RetinaFace, §4.2) and speaker count is known. (b) Visual degradation is simulated as consecutive blocks of dropped frames with other frames perfect (Appendix F), which is easier than blur, profile views or masks that corrupt every frame. (c) The SP block was designed for 2 speakers (§3.2.3 "Taking a 2-speaker mixture as an example") yet is evaluated for up to 5.
- **Suggested Fix:** add one non-block degradation (blur/noise on all frames) and a speaker-count-mismatch test.

### W3: Broader impact, privacy and misuse are absent
§1 sells the modality because video "can be captured passively through telephoto cameras without requiring user cooperation". That is also the profile of covert eavesdropping. The training/evaluation data (LRS2, LRS3, VoxCeleb2) contain identifiable faces and voices from television, talks and web videos; consent/licensing and demographic coverage (accent, face shape, facial hair, masks affect lip cues) are not discussed. There is no limitations section.
- **Suggested Fix:** add a short impact/limitations statement and per-demographic breakdowns where metadata exist (VoxCeleb2 has nationality/gender metadata).

### W4: Connect to neighbouring literatures
Joint separation-and-recognition and generative (diffusion/score-based) refiners both iterate on a first estimate; the paper may be reinventing known two-pass ideas in signal-processing and ASR. Comparing with a generative refiner pass, or showing that AVSR guidance beats a generic refiner, would sharpen the contribution.
- **Suggested Fix:** one baseline of this kind (see R1-W1).

## Missing References
*Optional. Line of work only: joint speech separation and recognition (PIT-based multi-talker ASR); score-based generative speech refiners; analysis-by-synthesis models of auditory scene analysis.*

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 3 | Sound approach; reasonable breadth |
| Clarity | 3 | Readable; some inconsistencies |
| Significance | 3 | Multi-speaker gain and degraded-video testing have practical value |
| Originality | 2 | Re-use of a recogniser in a loop |

## Dimension Scores (0–100)

**Pool position:** better than about 66% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: consistent gains across five datasets, a practically relevant multi-speaker result and visual-degradation testing, which place the paper just under the typical accepted bar; I did not weigh the missing controls as heavily as the Methodology Reviewer.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 62 | Competent | Sound, standard training |
| Clarity & Presentation | 62 | Competent | Readable |
| Novelty & Originality | 58 | Competent | Useful principle, incremental implementation |
| Significance & Impact | 64 | Competent | Practical multi-speaker and degraded-video value |
| Experimental Validation | 62 | Competent | Broad coverage |
| Reproducibility | 56 | Competent | Details given; no code |
| Ethical Compliance | 52 | Developing | Eavesdropping framing, faces, no limitations |

## Questions for Authors
1. What is the full-pipeline real-time factor, and what would a causal/streaming variant cost?
2. Do the gains hold for non-block degradations (all-frame blur) or for a real recording? A positive answer raises my score.
3. How does SP behave when the face count and the actual speaker count differ?

## Limitations Assessment
**No.** A limitations and impact paragraph should be added.

## Ethics Review Flag
**No**: no consent-specific violation is evident; a standard impact statement is recommended (W3).

## Overall Score
**4 (Borderline Accept)**: Practically relevant multi-speaker and degraded-visual results with a clear idea; I lean slightly accept despite the open controls.

## Confidence
**3**: Strong on deployment, less on the finer points of separation-model comparison.

---

# Peer Review Report

## Paper: From Coarse to Fine: Recursive Audio-Visual Semantic Enhancement for Speech Separation
## Reviewer: Dr. Sofia Kallergis, Reviewer 4 (Generalist) (machine-learning group, European technical university; fictional persona)
## Expertise: multimodal learning; general ML
## Date: 2026-11-10

---

## Summary
CSFNet is a two-stage audio-visual speech separation system. A pretrained AVSR model first reads lip video to guide a coarse separator, then reads the coarse separated audio plus video to produce stronger semantic features for a refined second pass. Two lightweight modules (a speaker-wise fusion block and a multi-branch TF-GridNet variant) accompany it. The experiments report consistent improvements on three clean and two noisy benchmarks.

**Contribution in one paragraph.** The contribution is a recipe: reuse a strong speech recogniser twice, once on the video and once on the first-pass audio, and train a second separator on its output. It matters because AVSS is a standard multimodal benchmark where recognisers are the main source of semantic cues.

## Strengths

### S1: Understandable core idea
Figures 1–2 and §3.1 make the pipeline easy to grasp for a non-specialist.

### S2: Breadth of experiments
Five datasets (Table 1, Table 3), 2–4 speakers (Table 4), DM setting, WER (Table 5) and missing-visual ablations (§4.5.1, Figure 4).

### S3: Honest side results
Appendix G (Table 7) openly shows no benefit of face information at stage 2 and offers a hypothesis ("We hypothesize that this is because the introduction of personalized speech representations…").

## Weaknesses

### W1 (MAJOR): The ML-level insight is thin for ICLR
Beyond the pipeline gain, the paper offers no analysis of *why* a second pass over coarse audio gives better semantics (no probe or representation analysis), and the main evidence is a leaderboard delta of 0.6–0.8 dB (Table 1). ICLR reviewers will expect an explanation or a controlled study. The claim in Appendix H ("strongly validate the indispensability of the fine separation stage") rests on one 4-speaker spectrogram example (Figure 8, unverifiable here) with no selection protocol.
- **Suggested Fix:** add a representation analysis and a controlled comparison (see R1-W1, R2-W4).

### W2 (MAJOR): Experimental narrative overreaches in several places
"Necessity" (Abstract), "maintains strong robustness even when visual information is partially or completely absent" (§1) versus "missing visual cues substantially degrade model performance, particularly when more than half of the frames are lost" (§4.5.1); "consistently achieves the best results across all three metrics on both datasets" (§4.4.3) with a non-matching baseline set; "On NTCD-TIMIT, CSFNet shows a particularly notable improvement in SI-SDRi with a relative gain" (§4.4.3, no number given).
- **Suggested Fix:** align the wording with the evidence and give the numbers.

### W3 (MINOR/MAJOR): Presentation and consistency
Undefined name "MAVINet" (§4.4.1), 2–4 vs 2–5 speakers (§4.1 vs §4.5.2), "speaker-aware" vs "speaker-wise", the SP description ("This results in three cross-modal feature representations", §3.2.3) is hard to follow for N speakers, and Table 5 reports only WER while the text says "strongest separation". There is no limitations section, no code statement, and the conclusion (§5) repeats the abstract.
- **Suggested Fix:** a careful proofreading pass, a limitations paragraph, a precise SP formulation.

**Minor:** Table 4 header, Eq. (1) "Y1", spelling of AVSR variants.

## Venue Criteria Checklist (ICLR)

| Criterion | Status | Location |
|-----------|--------|----------|
| Soundness: claims supported by evidence | Partly | Table 1, 4, 5; mechanism not isolated |
| Contribution: significance for the ICLR audience | Partly | Incremental, niche benchmark |
| Presentation | Partly | Inconsistencies listed above |
| Reproducibility | Not met | No code/seeds statement |
| Limitations/ethics | Not met | No section |
| Fit with venue | Met | ICLR precedents [21], [49] in the references |

## NeurIPS-Style Scores

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Quality | 2 | Reasonable but under-controlled |
| Clarity | 2 | Understandable, with inconsistencies |
| Significance | 2 | Incremental for ICLR |
| Originality | 2 | Recipe-level novelty |

## Dimension Scores (0–100)

**Pool position:** better than about 50% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: consistent but modest gains, moderate novelty and presentation problems; typical of a rejected submission at ICLR rather than the accepted set.

| Dimension | Score | Descriptor | Rationale |
|-----------|-------|------------|-----------|
| Technical Rigor | 56 | Competent | Standard, mostly sound |
| Clarity & Presentation | 58 | Competent | Understandable, inconsistent |
| Novelty & Originality | 52 | Developing | Recipe-level |
| Significance & Impact | 54 | Developing | Incremental |
| Experimental Validation | 54 | Developing | Broad but under-controlled |
| Reproducibility | 52 | Developing | No code |
| Ethical Compliance | 54 | Developing | No limitations |

## Questions for Authors
1. Can you state, in one place, the training procedure (what is frozen, which checkpoint feeds stage 2)?
2. What would change in your claims if a no-video second stage gave most of the gain?
3. Which variant is reported in Table 3?

## Limitations Assessment
**No.**

## Ethics Review Flag
**No.**

## Overall Score
**3 (Borderline Reject)**: A reasonable engineering recipe with consistent but modest gains and overreaching wording; the reasons to reject slightly outweigh those to accept at ICLR.

## Confidence
**3**: I am not a separation specialist.

---

# Devil's Advocate Report

## Paper: From Coarse to Fine: Recursive Audio-Visual Semantic Enhancement for Speech Separation
## Reviewer: Prof. Jun-seo Hartmann (evaluation-methodology group, research university; fictional persona)

---

## Steelman
A strong pretrained AVSR model reads lips and, in a second pass, also the first-pass audio, so it can disambiguate phonemes and speaker identity much better than from video alone (Table 5: 30.67 → 20.03 input WER). Feeding these better semantics to a second separator yields gains on all benchmarks, increasing with the number of overlapping speakers (Table 4), and the loop gives some resilience to degraded video.

## Core Argument Chain
1. Video-only AVSR semantics are ambiguous and speaker-agnostic (§1).
2. AVSR on (coarse audio + video) gives more discriminative, speaker-aware semantics (Table 5, Appendix G).
3. Feeding those semantics to a second separator improves separation (Tables 1, 4).
4. (Implicit) The improvement comes from the semantics, not from the extra pass, extra training or extra capacity.
5. The system is efficient (Table 2) and robust to missing video (Figure 4, 5).
∴ A "recursive semantic enhancement" framework is "necessary and effective" (Abstract).

## Strongest Counter-Argument
The step the paper never tests is premise 4. The "fine" stage is a *second separator pass*, initialized from the first (§3.1), trained for up to another 200 epochs (§4.2), and fed an extra encoder of the first-pass waveform. Any iterative-refinement system of that shape would be expected to improve on its first pass, with or without video, with or without AVSR semantics; the paper compares only against single-pass baselines (AVLiT, which is itself iterative per its title, is not analysed as such). The paper's own evidence leans in this direction: (i) the biggest gain is for 4 speakers (+3.8 dB, Table 4), where a refiner has the most residual interference to remove, which is what a generic refiner also does; (ii) in Table 7 adding *face* information to the first stage raises the coarse result from 16.2 to 16.5 and then *both* variants reach 16.8 after the second stage, so the stage-2 ceiling does not depend on how much identity/semantic information stage 1 had; (iii) the stage-2 gain is explained by the claim "personalized speech representations" (Appendix G) but only WER of the *output* is measured, not the quality of the representation; (iv) under 100% visual dropout (Figure 4, §4.5.1) there is no video, yet the second stage is said to help, which can only come from the coarse audio and a strong audio encoder; that is a denoising refinement and is not "visual semantics". If a no-video two-pass model or a non-AVSR second-stage encoder reproduces most of the gain, the paper's headline contribution reduces to "train a second, refining network", which is long known. Moreover, the efficiency claim leans on a cost row (Table 2) that equals a single-pass separator (Table 6, H = 96) and not the two-pass system. The authors need to show premise 4 and the cost of the whole system, not a single pass.

## Issue List

### CRITICAL Issues
No CRITICAL issues found. The central claim is supported in a weaker form (the two-pass system improves on a one-pass system in a like-for-like benchmark), so the fix is to narrow the claim or add the controls, and the missing controls fall under "a missing control is MAJOR".

### MAJOR Issues

| # | Dimension | Location | Issue | Suggested Fix |
|---|-----------|----------|-------|---------------|
| DA-M1 | Logic / Alternative explanation | §3.1, §4.2, Table 7, Figure 2 | Gain not attributed: no no-video two-pass, non-AVSR second encoder or matched-epoch control | Run the controls (R1-W1) or narrow to "two-pass refinement with AVSR guidance" |
| DA-M2 | Evidence / Efficiency | Table 2, Table 6, Table 1, §4.4.2 | Table 2 cost equals single-pass H = 96 separator; SI-SDRi 17.5 is DM while IIANet 16.0 is non-DM; "efficiency performance trade-off" unsupported | End-to-end cost; matched DM/non-DM rows |
| DA-M3 | Claim distortion (E5) | Abstract; §1; §4.5.1; §4.4.3 | "necessity"; "maintains strong robustness" vs "substantially degrade"; "consistently achieves the best results across all three metrics"; "10% reduction" not reproducible from Table 5 | Reword, quantify |
| DA-M4 | Evidence | Table 3 | Baselines copied from [35]; variant unspecified; weaker recent baselines; PESQ 2.72 / eSTOI 0.91 vs 1.52 / 0.68 while SI-SDRi differs by 2.3 dB | Retrain recent AV baselines; state variant; add sanity analysis |
| DA-M5 | Evidence / Variance | Table 1 DM rows | LRS3 DM coarse (17.9/18.2) is *below* the non-DM coarse (18.6/18.8) and below AV-CrossNet DM (18.3): CSFNet only becomes SOTA after the second pass; the fine gain ranges from 0.6 (LRS2, VoxCeleb2) to 2.2 dB (LRS3 DM: 20.1 − 17.9), unexplained | Seeds/CIs; explain the LRS3 DM coarse regression |

### MINOR Issues

| # | Dimension | Location | Issue |
|---|-----------|----------|-------|
| DA-m1 | Evidence | Table 2 | Identical time (62.51 ms) for AVConvTasNet and AVLiT; Table 6 H = 192 time 2163.17 ms vs 165.99 ms at H = 128: measurement artifacts to check |
| DA-m2 | Visual evidence | Appendix H, Figure 8 | One 4-speaker example; selection protocol not stated; figure unverifiable here |
| DA-m3 | Consistency | §4.4.1; §4.1 vs §4.5.2 | "MAVINet" undefined; 2–4 vs 2–5 speakers |
| DA-m4 | Evidence | Table 5 | Output-WER recogniser, mixture WER and oracle WER not stated; the "strongest separation" claim for Auto-AVSR has no SI-SDRi in Table 5 |

## Numerical Sanity Check

| Claim | Reported | Recomputed | Match? |
|-------|----------|------------|--------|
| Fine − coarse, Table 1 (LRS2/LRS3/Vox) | 0.6 / 0.8 / 0.7 dB | 16.8−16.2, 19.4−18.6, 14.8−14.1 | Yes |
| Fine − coarse, Table 4 (2/3/4 Mix) | 0.6 / 2.1 / 3.8 dB | 16.8−16.2, 15.4−13.3, 14.3−10.5 | Yes |
| "10% reduction in WER" (§1) | 10% | Table 5 Auto-AVSR 22.75→18.89 = 3.86 abs. = 17.0% rel.; AV-HuBERT 24.66→21.50 = 12.8% | No: not reproducible |
| DM vs previous best (§4.4.1) | "a further 0.7 dB" | 0.7 (LRS2), 1.8 (LRS3), 0.8 (Vox) | Only LRS2 |
| "roughly three times more parameters and MACs" vs IIANet | ~3× | 10.9/3.1 = 3.5; 64.8/18.6 = 3.5 | Roughly |
| Table 7 stage-2 gain | not discussed | lip-only 0.6 dB; lip+face 0.3 dB | n/a |
| "outperforms the SOTA AVLiT by roughly 2 dB" (§4.4.3) | ~2 dB | 14.71 − 12.42 = 2.29 | Yes |
| MST vs TF-GridNet (Appendix C) | "approximately 0.6 dB" | 16.8 − 16.2 = 0.6 | Yes |

## Ignored Alternative Explanations
- Extra training/epochs and a stage-2 network initialised from stage 1 (§3.1, §4.2).
- Generic iterative/cascaded refinement independent of video.
- Stage-1 audio re-encoded by any strong pretrained speech encoder, not specifically AVSR.
- Front-end data overlap: the pretrained Auto-AVSR may have seen the corpora from which test mixtures are made.
- DM vs non-DM training differences between rows of Table 2.

## Missing Stakeholder Perspectives
Hearing-device users and meeting participants (real, reverberant, non-frontal conditions); people whose faces and voices are in the training corpora; third parties in covert capture scenarios (§1 "telephoto cameras").

## Observations (Non-Defects)
- The Table 7 hypothesis is stated as a hypothesis, not a result.
- The coarse→fine gains are reported on every dataset and speaker count, not selectively.
- Selection of H = 96 is a trade-off, not a best-on-test selection (H = 192 scores higher), so no evaluation-leakage issue arises.

---

## Dimension Scores (0–100)

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Technical Rigor | 46 | Premise 4 untested; cost accounting |
| Clarity & Presentation | 58 | Understandable; inconsistencies |
| Novelty & Originality | 46 | Known two-pass idea plus AVSR re-use |
| Significance & Impact | 48 | Modest gains at higher cost |
| Experimental Validation | 44 | Missing controls, copied baselines, single runs |
| Reproducibility | 50 | Hyperparameters yes; code and frozen details no |
| Ethical Compliance | 55 | No limitations |

**Pool position:** better than about 36% of submissions to ICLR (accepted share ≈ 27%). Deciding evidence: the headline cause is untested and the efficiency evidence is mismatched.

## Overall: 2 | Confidence: 4

---

# PHASE 1.5 — Literature Check (strict, cutoff 2025-09-24)

**Not run.** Two attempts of `related_search.py search` failed with HTTP 429 (arXiv API unreachable), so the check fell back to off. No ledger, no `scout`, no `coverage`, no `similarity`/`novelty` output exists. Reviewer 2's missing references and novelty table are knowledge-based, with `[verify]` where unsure. All statements about prior work are limited to items published before the cutoff, and none is used to lower a score as a "required comparison" other than the paper's own cited [49].

# PHASE 1.6 — Report Check

| Report | Weakness | Action | Reason |
|--------|----------|--------|--------|
| R2 | Draft W: "[30] is an fMRI study, so the robustness citation is wrong" | Rewritten | The paper cites [30, 16] for "growing attention due to its robustness…"; [30] supports the premise that visual input helps people. Reworded as "supports the premise only" (W3c) |
| R3 | Draft W: "no real-world recordings" | Kept, merged into W1 | Specific, actionable |
| R4 | Draft W: "Figure 4/5 values unreadable" | Dropped | Text-extraction artifact, not an authors' error; noted as unverifiable |
| R1 | Draft W: "no code" | Rewritten into W6 | Merged with the protocol omission |
| R1 | Draft W: "Table 5 recogniser unnamed" | Kept as question (Q4) | Low-confidence omission, not a weakness until answered |
| R4 | Draft W: "conclusion repeats abstract" | Moved to Minor | Cosmetic |
| DA | "AVConvTasNet/AVLiT identical time" | Moved to Minor (DA-m1) | Cosmetic / measurement |
| R1 | Draft W: "single run" | Kept as MAJOR → softened in W5 | Field norm for AVSS on 2 s clips; the coarse-stage 0.2 dB margin is within plausible noise |

Scores unchanged.

---

# PHASE 2 — EIC Meta-Review and Decision

## Synthesizer Part A: Merged issue list and consensus map

| Merged issue | Source IDs | Class | Hinges? |
|--------------|-----------|-------|---------|
| Gain not attributed to semantics: no matched-compute / no-video / non-AVSR second pass controls | R1-W1, DA-M1, R2-W1, R3-W4, R4-W1 | CONSENSUS-4/5 | Yes |
| Cost accounting and Table 2 mismatch (single-pass cost; DM vs non-DM) | R1-W2, DA-M2, R3-W1 (partly) | CONSENSUS-3 | Yes |
| Baselines: copied vs retrained; Table 3 weak baselines; RTFS-Net absent | R1-W4, R2-W2, DA-M4 | CONSENSUS-3 | Yes |
| Overclaimed wording ("necessity", robustness, "10%") | R1-ERR-2, DA-M3, R4-W2 | CONSENSUS-3 | No |
| Inconsistencies (MAVINet; 2–4 vs 2–5) | R1-ERR-1/4, R4-W3, DA-m3 | CONSENSUS-3 | No |
| No variance / seeds | R1-W5, DA-M5 | CONSENSUS-2 | No |
| Component ablations (MST range vs H; SP vs attention; Table 6 setting) | R1-W3 | SOLO | No |
| Citation errors ([10], DPCL++ [5], [30]) | R2-W3 | SOLO | No |
| Ethics / deployment / limitations | R3-W1, W3, R4 | CONSENSUS-2 | No |
| Thin novelty / ML insight | R2-W1, R4-W1, DA | CONSENSUS-3 | Partly |
| SPLIT: strength of robustness-to-missing-video | R3-S2 vs R4-W2, DA-M3 | SPLIT | No |
| DA-CRITICAL | none | n/a | n/a |

Official scores (script, BEFORE run, no weights): see Score Summary. Warnings: none.

## EIC Meta-Review (Dr. Ingrid Valmont)

*Process: I read the five reports and the package first, then re-read the abstract, §1, §3, Tables 1–7, §4.4–4.5 and Appendices B, C, G of the paper to check the decisive points.*

### The Case For and Against
- **For acceptance:** A clear and simple idea (re-run a strong AVSR model on the first-pass audio) delivers consistent gains across three clean and two noisy datasets and across 2–4 speakers (Table 1, Table 3, Table 4), with a large gain at 4 speakers (+3.8 dB) and testing under degraded video. The component ablations and the Table 7 negative result are honest.
- **Against acceptance:** The central claim, that *semantic* recursion causes the gain, is untested against the obvious alternatives (no-video two-pass, non-AVSR second encoder, extra epochs), the efficiency claim uses a cost that equals one pass (Table 2 = Table 6 H = 96) and a DM-trained result against non-DM baselines, baselines are copied or old (Table 3), RTFS-Net is omitted, there are no seeds, and several wording and consistency errors exist. The gain over the closest prior method is 0.2 dB at stage 1 and 0.8 dB at stage 2 for roughly 3.5× parameters and MACs, plus a second pass.

### Verification of Decisive Points (EIC read of the paper)

| Point | Raised by | Location | EIC finding | Note |
|-------|-----------|----------|-------------|------|
| Table 2 cost equals single-pass MST H = 96 (Table 6) | R1-W2, DA-M2 | Table 2, Table 6 | **Verified** | 64.8 G / 10.9 M / 117.39 ms identical |
| Table 2 SI-SDRi 17.5 is a DM result vs non-DM baselines | R1-W2, DA-M2 | Table 1, Table 2 | **Verified** | AV-CrossNet 16.8 is also DM; IIANet 16.0 non-DM |
| Fine stage = second, finetuned network with additional epochs, no matched control | R1-W1, DA-M1 | §3.1, §4.2, Figure 2 | **Verified** (as absence of control) | No no-video or non-AVSR variant exists |
| "Semantics play no demonstrated role" (DA strongest form) | DA | Table 5, Table 7 | **Overstated** | Table 5 (30.67 → 20.03 input WER) and Table 7 give indirect support; the claim is untested, not refuted |
| "10% reduction in WER" not reproducible | R1-ERR-2, DA-M3 | §1, Table 5 | **Partly correct** | Best recomputation gives 17.0% relative / 3.86 abs.; the authors' baseline may differ. Needs clarification, not a refutation |
| "MAVINet" undefined | R1-ERR-1, R4-W3 | §4.4.1 | **Verified** | Text search |
| 2–4 vs 2–5 speakers | R1-ERR-4, R4-W3 | §4.1, App. D.1, §4.5.2, Fig. 5 | **Verified** | |
| "maintains strong robustness" vs "substantially degrade" | DA-M3, R4-W2 (R3-S2 praises) | §1, §4.5.1 | **Verified** (wording conflict); R3's robustness strength **Overstated** | Figure values unverifiable |
| LRS3 DM coarse below non-DM coarse and below AV-CrossNet DM | DA-M5 | Table 1 | **Verified** | 17.9 vs 18.6; vs 18.3 |
| Table 7: stage-2 gain shrinks from 0.6 to 0.3 with face | R1-W1, DA | Table 7 | **Verified**; interpretation **Partly correct** | Consistent with a ceiling or with identity info being absorbed |
| Table 6 setting unstated; MST H=96 equals fine-stage numbers | R1-W3, ERR-6 | Table 1, Table 6 | **Verified** (numbers); interpretation Partly | |
| Multi-range not isolated from H in Table 6 | R1-W3 | Table 6, §3.2.4 | **Verified** | |
| Table 3 baselines from [35]; variant unspecified; recent AV baselines missing | R1-W4, R2-W2, DA-M4 | Table 3 | **Verified** | |
| Citation [10] listed as audio-only | R2-W3 | §1, ref. [10] | **Verified** | Title is AV |
| "DPCL++ [5]" points to original Deep Clustering | R2-W3 | Table 1, ref. [5] | **Partly correct** | Entry is "Deep clustering…" (Hershey et al.); DPCL++ is a follow-up [verify] |
| Covert-capture language | R3-W3 | §1 | **Verified** | |
| Figure-dependent claims (Figures 4, 5, 8) | R1, R3, DA | Fig. 4, 5, 8 | **Not assessable** | Figures unavailable |
| H = 96 selection by cost, not by best test score | R1 (protocol sweep), DA | Appendix C, Table 6 | **Verified** | H = 192 scores higher; no leakage issue |

### Reviewer Weights

| Reviewer | Overall | Confidence | EIC quality weight | Reason |
|----------|---------|------------|--------------------|--------|
| R1 (Methodology) | 3 | 4 | 1.25 | Cost, DM/non-DM, Table 6 and splits points all verified; calibrated to venue; one point (ERR-2) only partly correct |
| R2 (Domain) | 3 | 4 | 1.0 | Citation points verified or partly correct; solid and typical |
| R3 (Perspective) | 4 | 3 | 0.75 | Rating leans on the robustness strength that the paper's own §4.5.1 contradicts and on a cost story that Table 2 does not support; missed the Table 2 problem; otherwise constructive |
| R4 (Generalist) | 3 | 3 | 1.0 | Sound, typical review; claim-wording points verified |
| DA | 2 | 4 | 1.0 | M1–M3, M5 verified; strongest-form statement overstated, but the DA flagged no CRITICAL issue and the score follows its text |

### DA-CRITICAL Rulings
No DA-CRITICAL issue was raised (the Devil's Advocate wrote "No CRITICAL issues found."). No DA ceiling applies. The missing attribution control (DA-M1) was checked against the criteria: the evidence supports a weaker claim ("a two-pass refinement helps"), and a missing control is MAJOR. I agree.

### Final Decision and Justification
The reviewers' official ratings are 3, 3, 4, 3, 2 (mean 3.00). The EIC-weighted rating is 2.92 (weights 1.25 / 1.0 / 0.75 / 1.0 / 1.0 times confidence), which rounds to 3, so the starting point is **3**. The 0–100 composite cross-check is 52.7 (band 3), consistent with the rating, and no ⚠ was raised; I keep the starting point. My own pool position is **48**: the paper is better than roughly half the submissions but sits on the rejected side of the bar. The deciding evidence is that (a) the gain over the closest prior method is small (+0.8 dB at stage 2, +0.2 dB at stage 1) and obtained with a roughly 3.5× larger separator plus a second pass and two AVSR branches (Table 2 vs Table 6), (b) the causal claim that gives the paper its title is not isolated from generic two-pass refinement (Table 7 hints that it is not necessarily semantic), and (c) the comparison set (Table 3, RTFS-Net omission, copied baselines) is incomplete. Weaknesses that accepted ICLR papers commonly carry (single runs on a niche benchmark, thin related work) would not alone sink it. The paper does have real strengths (consistent gains, speaker-count scaling), and most issues are fixable, but the main ones need new experiments, so a rebuttal-window fix is uncertain. The decision does not exceed any ceiling (none applies). The decision equals the starting point. **Final (EIC): 3, Borderline Reject.** ICLR rating label for 3 per the script: 4 on {0,2,4,6,8,10}.

*Integrity signals:* none (integrity scan clean; no text addressed to reviewers or AI systems). Text overlap check not run (literature check unavailable).

---

## Decision: Borderline Reject (3)

**Official ratings** (shown to authors): R1 3, R2 3, R3 4, R4 3, DA 2 → mean 3.00 · official composite 53.4
**EIC assessment** (internal): weighted rating 2.92 → starting point 3 · weighted composite 52.7 → band 3 (cross-check agrees) · **DA ceiling**: none · **Final (EIC)**: 3
**Journal recommendation:** n/a (conference target)

## Score Summary

### Official Scores and EIC Assessment (from `scripts/aggregate_scores.py`, BEFORE = no weights, AFTER = EIC weights 1.25 / 1.0 / 0.75 / 1.0 / 1.0)

| Dimension | R1 | R2 | R3 | R4 | DA | Official (raw mean) | EIC assessment (weighted) | Spread |
|-----------|----|----|----|----|----|---------------------|----------------------|--------|
| Technical Rigor | 50 | 54 | 62 | 56 | 46 | 53.6 | 52.6 | 16 |
| Clarity & Presentation | 56 | 58 | 62 | 58 | 58 | 58.4 | 58.0 | 6 |
| Novelty & Originality | 50 | 50 | 58 | 52 | 46 | 51.2 | 50.6 | 12 |
| Significance & Impact | 50 | 52 | 64 | 54 | 48 | 53.6 | 52.5 | 16 |
| Experimental Validation | 48 | 52 | 62 | 54 | 44 | 52.0 | 50.9 | 18 |
| Reproducibility | 50 | 54 | 56 | 52 | 50 | 52.4 | 52.0 | 6 |
| Ethical Compliance | 56 | 56 | 52 | 54 | 55 | 54.6 | 54.9 | 4 |
| **Composite** | 50.8 | 53.3 | 60.1 | 54.3 | 48.4 | **53.4 (before)** | **52.7 (after)** | |

No dimension spread exceeds 20 points; no warnings.

### Target-Venue Scores (ICLR, scale status: secondary)

| Venue field | Score |
|-------------|-------|
| Soundness / Presentation / Contribution (1–4) | 2 / 2 / 2 |
| Rating (EIC final 3) | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}); below the acceptance threshold |

*Scale status is "secondary": recent forms use this scale; verify against the current form.*

---

## Editorial Decision Letter

Dear Authors,

Thank you for submitting "From Coarse to Fine: Recursive Audio-Visual Semantic Enhancement for Speech Separation" to ICLR.

The paper addresses audio-visual speech separation and proposes re-using a pretrained AVSR model on a first-pass separated waveform to guide a second separation pass.

**Overall Assessment:** The panel found the idea clear and the empirical gains consistent across clean and noisy benchmarks and across speaker counts. The reviewers were concerned that the central claim (that recursive *semantic* enhancement, rather than a generic second pass or additional training, causes the gains) is not tested, and that the cost and baseline comparisons do not fully support the efficiency and state-of-the-art claims.

**Key Strengths Identified by Reviewers:**
1. A clear, simple idea with consistent coarse→fine gains on every dataset and speaker count (R1, R2, R3, R4).
2. Broad evaluation: three clean sets, two noisy sets, 2–4 speakers, WER, missing-visual-frame protocols (R1, R3, R4).
3. Useful side findings (front-end comparison in Table 5; the face-information result in Table 7) (R2, R4).

**Key Concerns Requiring Attention:**
1. Attribution: no no-video two-pass, non-AVSR second-stage encoder or matched-epoch control (R1, R2, R3, R4, DA; CONSENSUS-4/5).
2. Cost and fairness: Table 2 reports a single-pass cost, mixes DM and non-DM results; baselines are copied or dated; RTFS-Net absent (R1, R2, DA; CONSENSUS-3).
3. Overclaimed wording and inconsistencies: "necessity", robustness to missing video, "10% WER reduction", "MAVINet", 2–4 vs 2–5 speakers (R1, R4, DA; CONSENSUS-3).

**Critical Challenge (Devil's Advocate):** none was rated CRITICAL. The DA's strongest objection is that the second stage may be a generic refinement pass, which the authors must address with controls.

**Decision: Borderline Reject (3)**

The reasons to reject slightly outweigh the reasons to accept at this venue. For acceptance, the authors would need to isolate the contribution of AVSR semantics from generic two-pass refinement, report the full inference cost with like-for-like training regimes, and strengthen the baseline set. Please refer to the Revision Roadmap below.

Sincerely,
Dr. Ingrid Valmont
Editor-in-Chief (meta-reviewer)

---

## Consensus and Disagreement Map

### Points of Consensus (3+ reviewers agree)

| Issue | Reviewers | Classification |
|-------|-----------|---------------|
| Gain not attributed to semantics (missing controls) | R1, R2, R3, R4, DA | CONSENSUS-4/5 |
| Cost accounting, Table 2 mismatch | R1, DA (R3 partly) | CONSENSUS-3 |
| Baselines weak / copied; RTFS-Net absent | R1, R2, DA | CONSENSUS-3 |
| Overclaimed wording | R1, R4, DA | CONSENSUS-3 |
| Inconsistencies | R1, R4, DA | CONSENSUS-3 |
| Thin novelty / insight | R2, R4, DA | CONSENSUS-3 |

### Points of Disagreement

| Issue | For | Against | Arbitration |
|-------|-----|---------|-------------|
| Robustness to missing visual input as a strength | R3 | R4, DA | §4.5.1 itself says missing cues "substantially degrade" performance; the paper's claim "maintains strong robustness" (§1) is overstated; the relative advantage of stage 2 may still hold (figures unverifiable). R3 weighted down |
| Overall: lean accept vs reject | R3 (4) | R1, R2, R4 (3), DA (2) | Evidence on controls and cost favours the lower ratings |

### Score Spread Discussion
No dimension exceeds the 20-point spread flag (max Experimental Validation 18: R3 62 vs DA 44). R3's higher scores rest on the broad-coverage reading of the experiments; R1 and the DA scored the missing controls. The EIC adopts the lower view, as the controls were verified missing.

### Devil's Advocate Highlights

| Issue ID | Severity | Issue | Raised by Others? | Ruling | Resolvable by |
|----------|----------|-------|-------------------|--------|---------------|
| DA-M1 | MAJOR | Gain unattributed | Yes (R1, R2, R3, R4) | n/a | New experiments |
| DA-M2 | MAJOR | Cost / DM mismatch | Yes (R1) | n/a | Measurement + matched rows |
| DA-M3 | MAJOR | Claim distortion | Yes (R1, R4) | n/a | Rewording |
| DA-M4 | MAJOR | Table 3 comparison | Yes (R1, R2) | n/a | New baselines |
| DA-M5 | MAJOR | LRS3 DM; variance | Partly (R1) | n/a | Seeds, explanation |

---

## Revision Roadmap

### Priority 1 — Required (Must Fix)
*Verified issues that undermine a main claim; no DA-CRITICAL was upheld.*

| # | Issue | Source IDs | Location | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|----------|---------------|--------|--------------------|
| P1-1 | Attribution of the gain to AVSR semantics vs generic two-pass refinement / extra training | R1-W1, DA-M1, R2-W1, R4-W1 | §3.1, §4.2, Table 1, 4, 7 | No-video two-pass; non-AVSR second encoder; coarse model trained +200 epochs; two-pass IIANet/AV-CrossNet; report on LRS2-2Mix and 4Mix | High; ≈ 4 trainings ≈ 1–2 weeks on 8×A100 | Partly (the cheapest 1–2 controls) |
| P1-2 | Full inference cost and like-for-like comparison for the efficiency claim | R1-W2, DA-M2 | Table 2, Table 6, Table 1, §4.4.2 | End-to-end params/MACs/latency/memory for both passes and both AVSR branches; count pretrained encoders for baselines; matched DM/non-DM rows; soften "efficiency performance trade-off" | Low (< 1 GPU-day) | Yes |
| P1-3 | Narrow or correct overclaims and numbers | R1-ERR-2/5, DA-M3, R4-W2 | Abstract, §1, §4.4.1, §4.4.3, §4.5.1 | Reword "necessity" and "maintains strong robustness"; define the 10% WER baseline; give per-dataset DM gains; quantify "relative gain" | Low | Yes |

### Priority 2 — Strongly Suggested (Should Fix)

| # | Issue | Source IDs | Suggested Fix | Effort | Rebuttal-feasible? |
|---|-------|-----------|---------------|--------|--------------------|
| P2-1 | Baselines: mark copied vs retrained; add RTFS-Net, IIANet/CTCNet/AV-CrossNet to Table 3; state the variant; Auto-AVSR/test overlap | R1-W4, R2-W2, DA-M4 | Retrain on Table 3 data; add rows | High (≈ 1 week) | Partly |
| P2-2 | Variance / seeds; explain LRS3 DM coarse regression | R1-W5, DA-M5 | 3 seeds on LRS2-2Mix, or bootstrap CIs | Medium (≈ 3× training) / Low for bootstrap | Partly |
| P2-3 | Component ablations: MST single-branch at H = 96; SP vs attention fusion; state Table 6 setting | R1-W3 | Two ablations; clarify Table 6 | Medium (2–3 GPU-days) | Yes |
| P2-4 | Citation fixes and related work on iterative/cascaded separation; verify DPCL++ | R2-W3, R2-W1 | Correct [5], [10], [30]; add paragraph; cite TDANet (ICLR 2023), SepReformer `[verify]` | Low | Yes |
| P2-5 | Representation-level evidence for "more discriminative / speaker-aware" L̂ | R2-W4, R4-W1 | Probe for speaker/content on L vs L̂ | Medium | Yes |
| P2-6 | Reproducibility: training procedure, frozen components, SP for N speakers, code | R1-W6, R4-W3 | Pseudo-algorithm, SP formula, release code | Low–Medium | Yes |

### Priority 3 — Nice to Fix (Optional)

| # | Issue | Source | Suggestion |
|---|-------|--------|-----------|
| N1 | Deployment: real-time factor, causal variant, real recordings | R3-W1 | Report RTF; small real-recording test or limitation |
| N2 | Unchallenged assumptions: non-block degradation, speaker-count mismatch | R3-W2 | One extra stress test |
| N3 | Impact/limitations statement; covert-capture framing; consent/demographics | R3-W3, R4 | Add a paragraph |
| N4 | Cross-field baselines: joint separation-recognition; generative refiner | R3-W4 | One refiner baseline |
| N5 | Output-WER recogniser, mixture and oracle WER; Auto-AVSR SI-SDRi per front end | R1 Q4, DA-m4 | Add to Table 5 |
| N6 | Minor: Table 4 header, Eq. 1 "Y1", naming, Table 2 duplicated time, H = 192 latency | R1, DA-m1 | Proofread |

---

## Estimated Revision Effort
- Priority 1: 3 items; ≈ 1–2 weeks (dominated by P1-1 controls); P1-2 and P1-3 take days.
- Priority 2: 6 items; ≈ 1–2 weeks of compute plus writing.
- Priority 3: 6 items; ≈ 2–3 days.
- **Total estimated revision time**: ≈ 3–4 weeks including retraining baselines.

*No Post-Review Analysis (Gap Scout) was requested.*
