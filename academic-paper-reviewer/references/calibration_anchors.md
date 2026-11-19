# Calibration Anchors

Five reference papers with known outcomes, which fix the pool scale before a type places a paper. Every type compares the paper with the anchors before it writes its pool position (`agents/ledger_reviewer_agent.md`, Step 4). The aim is to spread the scores: without a reference point, reviewers put almost every paper in the middle of the pool, whatever they found.

The anchors are real ICLR 2026 submissions from the calibration set's training split, described without their titles. They are never papers under evaluation. Their positions come from the human ratings and the decision, on the ICLR scale (0, 2, 4, 6, 8, 10). For a venue with a different acceptance rate, keep the anchors' order and move the accept line (between C and D) to the venue's rate (`references/venue_profiles.md`).

| Anchor | Pool position | Human ratings | Outcome | Overall |
|---|---|---|---|---|
| A | about 10 | 2, 2, 2, 4 | reject | 2 |
| B | about 30 | 2, 2, 4, 4 | reject | 2–3 |
| C | about 50 | 2, 4, 4, 6 | reject | 3 |
| D | about 72 | 4, 4, 6, 6 | accept (poster) | 4 |
| E | about 88 | 4, 6, 6, 8 | accept (poster) | 5 |

## The anchors

**A. A simple observation presented as a finding (pool about 10).** An empirical paper on multimodal document understanding. Its claim is that plain text extracted from PDFs hurts model accuracy and that encoding the document's structure in a markup language helps. The evaluation is broad: four benchmarks, four models, and attention visualizations. Reviewers judged the observation already known in the field. They saw the method as prompt formatting, with no principled reason for this markup over simpler ones, and found the attention analysis shallow and the input variables poorly controlled. Broad experiments did not rescue a contribution that was too small and not new.

**B. A principle stated more strongly than its evidence (pool about 30).** A theory paper on out-of-distribution generalization. Its principle is that the simplest model consistent with the data generalizes, and it gives a clean formal framework for it. Reviewers liked the question and the formalism. They found the evidence far from the motivating setting: a toy experiment stood in for the real models the framing names, and the theory was only loosely connected to the experiments. A sound formalism whose link to the claimed phenomenon is not shown sits in the lower part of the pool.

**C. A careful, useful study without an insight (pool about 50; rejected).** A benchmark of optimizers for LLM pretraining. Many optimizers, model sizes, batch sizes and training lengths are each tuned with care, and the code is released. Reviewers valued the rigor and the practical rankings. The deciding objections were these:
- the conclusions are "A beats B in setting S" with little explanation of why;
- the scale and the context length are far below the regime the title addresses, so the conclusions may not transfer;
- some takeaways were already known.

This is the anchor for papers that are thorough and useful but fail questions 1 and 4 of the contribution check: effort and polish do not move a paper above C.

**D. A clear contribution with ordinary weaknesses (pool about 72; accepted).** A reward model and a benchmark for instruction-guided image editing. They are used to make online RL work for editing, where it did not before, with a scaling study and competitive Best-of-N and RL results. Reviewers raised real weaknesses:
- RL was shown on only one base editor;
- the benchmark was small and curated for agreement;
- the method was close to prior RL-for-generation work;
- reproducibility depends on proprietary candidate models.

It was still accepted, because the paper shows something that did not work before, now working, with the mechanism (the reward model's fidelity) measured. Those weaknesses are the ordinary ones of an accepted paper.

**E. A principled generalization that unifies known practice (pool about 88; accepted).** A theory paper on a class of function approximators built from mixtures of anisotropic bumps. They are fitted by Wasserstein–Fisher–Rao gradient flows and recover a popular rendering technique as a special case. Reviewers praised the unifying framework and the clean theory. They noted real limits: experiments only in 1D and 2D, few baselines, and a loose approximation bound. A conceptual delta that explains existing practice outweighs thin experiments.

## How to place a paper

1. **Bracket it.** Name the anchor just below the paper and the anchor just above it. For each, give the ledger IDs that make the paper better or worse than that anchor ("above C: A3 shows why the effect occurs, which C lacks; below D: R2 leaves the main claim on one setting, as in D, but without D's measured mechanism").
2. **Place it inside the bracket.** The pool position lies between the two anchors' positions. It lies outside them only when the paper is below A or above E, and then the reason is given.
3. **The middle is not a default.** A paper sits near C only when it resembles C: competent, useful, but without an insight or with conclusions that may not transfer. A paper with a fatal or unanswered major error at its core goes at or below A or B. A paper with a specific insight and only ordinary weaknesses goes at or above D. Being unsure between two anchors is never a reason to place a paper at C.
4. **Crossing the accept line needs a reason D would have.** Placing a paper above C requires an accept reason in the ledger that shows something new working or explained (the contribution check, questions 1 and 3). Thoroughness, a large benchmark or a released artifact alone never moves a paper above C.
5. **Then score.** The dimension scores follow the pool position's band (`references/quality_rubrics.md`), and Overall follows from both. Pool 10 corresponds to Overall 1–2, 30 to 2, 50 to 3, 72 to 4 and 88 to 5.

The anchors calibrate the scale. They never stand in for evidence: every bracket names ledger IDs, and a type that cannot say why the paper is above or below an anchor has not finished reading the ledger.
