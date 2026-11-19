**Paper type**: analysis  
**Weights**: Technical Rigor 0.25, Clarity & Presentation 0.10, Novelty & Originality 0.20, Significance & Impact 0.20, Experimental Validation 0.15, Reproducibility 0.05, Ethical Compliance 0.05

#### Reviewer weights (EIC, internal)

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| T1 (Learning-with-noisy-labels specialist) | 4 | 0.85 | 1.00 | 18% |
| T2 (Dataset distillation researcher) | 4 | 0.85 | 1.00 | 18% |
| T3 (Learning-theory reviewer (memorization and generalization under label noise)) | 4 | 0.85 | 1.00 | 18% |
| T4 (Evaluation and protocol methodologist) | 4 | 0.85 | 1.00 | 18% |
| T5 (Data-centric ML researcher (coreset selection and data pruning)) | 3 | 0.70 | 1.00 | 15% |
| T6 (Privacy and trustworthy-ML researcher) | 3 | 0.70 | 1.00 | 15% |

*No EIC quality weights given yet: the EIC assessment uses confidence only. Add `eic_weight` (0.5-1.5) per reviewer after the EIC's meta-review.*

#### Official scores and EIC assessment

| Dimension | T1 (Learning-with-noisy-labels specialist) | T2 (Dataset distillation researcher) | T3 (Learning-theory reviewer (memorization and generalization under label noise)) | T4 (Evaluation and protocol methodologist) | T5 (Data-centric ML researcher (coreset selection and data pruning)) | T6 (Privacy and trustworthy-ML researcher) | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 40 | 46 | 32 | 34 | 42 | 40 | 39.0 | 38.9 | 14 |
| Clarity & Presentation | 52 | 56 | 48 | 46 | 52 | 54 | 51.3 | 51.2 | 10 |
| Novelty & Originality | 45 | 50 | 44 | 45 | 42 | 46 | 45.3 | 45.4 | 8 |
| Significance & Impact | 38 | 46 | 38 | 40 | 40 | 40 | 40.3 | 40.4 | 8 |
| Experimental Validation | 30 | 45 | 38 | 34 | 40 | 40 | 37.8 | 37.7 | 15 |
| Reproducibility | 42 | 48 | 40 | 35 | 45 | 45 | 42.5 | 42.3 | 13 |
| Ethical Compliance | 58 | 60 | 55 | 48 | 58 | 45 | 54.0 | 54.2 | 15 |
| **Composite** | 41.3 | 48.5 | 39.7 | 39.4 | 43.2 | 43.1 | **42.5** | **42.5** | |
| Pool position (P%) | 15 | 30 | 15 | 15 | 22 | 22 | | | |

#### Ratings (the decision's starting point)

**Official reviewer ratings (Overall 1-6)**: T1 (Learning-with-noisy-labels specialist) 2, T2 (Dataset distillation researcher) 3, T3 (Learning-theory reviewer (memorization and generalization under label noise)) 2, T4 (Evaluation and protocol methodologist) 2, T5 (Data-centric ML researcher (coreset selection and data pruning)) 2, T6 (Privacy and trustworthy-ML researcher) 2 → official mean **2.17**  
**EIC-weighted rating** (internal): **2.18** (+0.01 vs. official) → starting point **2 (Reject)**

⚠ = spread > 20 points: discuss this disagreement in the decision.

**Composite cross-check (0-100)**: official 42.5 → 2 · EIC-weighted 42.5 → 2 (+0.0 vs. official)  
**Decision ceiling**: none (no upheld DA-CRITICAL issue). The EIC's decision starts from the EIC-weighted rating and may depart from it in either direction, with a written reason.
#### Ledger mode: aspect-weighted average (iclr)

| Reviewer type | Aspect | Aspect share | Weight |
|---|---|---|---|
| T1 (Learning-with-noisy-labels specialist) | experimental_validation | 14% | 0.169 |
| T2 (Dataset distillation researcher) | novelty | 20% | 0.247 |
| T3 (Learning-theory reviewer (memorization and generalization under label noise)) | technical_rigor | 28% | 0.169 |
| T4 (Evaluation and protocol methodologist) | technical_rigor | 28% | 0.169 |
| T5 (Data-centric ML researcher (coreset selection and data pruning)) | significance | 20% | 0.124 |
| T6 (Privacy and trustworthy-ML researcher) | significance | 20% | 0.124 |

**Final rating (aspect-weighted mean)**: **2.25** → **2 (Reject)** · plain mean 2.17 · weighted pool position 20.4
### Cross-Venue Outlook

| Venue | Venue-weighted composite | Bar offset | Venue shift | Band → with DA cap | Venue recommendation | Venue sub-scores | Scale status |
|---|---|---|---|---|---|---|---|
| ICLR (2026) | 42.3 | +0 | +0 | 2 → 2 | 2 on {0,2,4,6,8,10} (3 on {1,3,5,6,8,10}) | Soundness 1, Presentation 2, Contribution 1 | secondary |

Emphasis weights are this skill's heuristics, not official venue weights. Scale status: official / confirmed / secondary / assumed / unpublished (see references/venue_profiles.md). Upheld DA-CRITICAL caps apply to every venue.

- **ICLR**: Soundness/Presentation/Contribution 1-4 and Confidence 1-5 are long-standing. Overall rating reported as {0,2,4,6,8,10} for ICLR 2026; earlier cycles used {1,3,5,6,8,10}. Both are shown.
