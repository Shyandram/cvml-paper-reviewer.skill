**Paper type**: empirical  
**Weights**: Technical Rigor 0.20, Clarity & Presentation 0.10, Novelty & Originality 0.15, Significance & Impact 0.15, Experimental Validation 0.20, Reproducibility 0.10, Ethical Compliance 0.10

#### Reviewer weights (EIC, internal)

| Reviewer | Confidence | Confidence weight | EIC quality weight | Share of EIC assessment |
|---|---|---|---|---|
| T1 (Computer-use / GUI-agent specialist) | 4 | 0.85 | 1.00 | 18% |
| T2 (Agent-evaluation and experimental-design methodologist) | 4 | 0.85 | 1.00 | 18% |
| T3 (Learning-from-observation / inverse-dynamics researcher) | 4 | 0.85 | 1.00 | 18% |
| T4 (Temporal action localization / video-grounding researcher) | 4 | 0.85 | 1.00 | 18% |
| T5 (VLM pretraining and data-scaling researcher) | 3 | 0.70 | 1.00 | 15% |
| T6 (Responsible data-collection and data-governance researcher) | 3 | 0.70 | 1.00 | 15% |

*No EIC quality weights given yet: the EIC assessment uses confidence only. Add `eic_weight` (0.5-1.5) per reviewer after the EIC's meta-review.*

#### Official scores and EIC assessment

| Dimension | T1 (Computer-use / GUI-agent specialist) | T2 (Agent-evaluation and experimental-design methodologist) | T3 (Learning-from-observation / inverse-dynamics researcher) | T4 (Temporal action localization / video-grounding researcher) | T5 (VLM pretraining and data-scaling researcher) | T6 (Responsible data-collection and data-governance researcher) | Official (raw mean) | EIC assessment (weighted) | Spread |
|---|---|---|---|---|---|---|---|---|---|
| Technical Rigor | 55 | 46 | 52 | 46 | 58 | 54 | 51.8 | 51.6 | 12 |
| Clarity & Presentation | 60 | 56 | 60 | 55 | 62 | 58 | 58.5 | 58.4 | 7 |
| Novelty & Originality | 58 | 55 | 50 | 55 | 60 | 56 | 55.7 | 55.5 | 10 |
| Significance & Impact | 62 | 56 | 56 | 56 | 66 | 58 | 59.0 | 58.8 | 10 |
| Experimental Validation | 54 | 48 | 52 | 50 | 60 | 54 | 53.0 | 52.8 | 12 |
| Reproducibility | 60 | 56 | 58 | 56 | 60 | 52 | 57.0 | 57.1 | 8 |
| Ethical Compliance | 55 | 55 | 55 | 55 | 56 | 42 | 53.0 | 53.2 | 14 |
| **Composite** | 57.3 | 52.2 | 54.0 | 52.5 | 60.3 | 53.9 | **55.0** | **54.9** | |
| Pool position (P%) | 56 | 46 | 50 | 47 | 64 | 48 | | | |

#### Ratings (the decision's starting point)

**Official reviewer ratings (Overall 1-6)**: T1 (Computer-use / GUI-agent specialist) 3, T2 (Agent-evaluation and experimental-design methodologist) 3, T3 (Learning-from-observation / inverse-dynamics researcher) 3, T4 (Temporal action localization / video-grounding researcher) 3, T5 (VLM pretraining and data-scaling researcher) 4, T6 (Responsible data-collection and data-governance researcher) 3 → official mean **3.17**  
**EIC-weighted rating** (internal): **3.15** (-0.02 vs. official) → starting point **3 (Borderline Reject)**

⚠ = spread > 20 points: discuss this disagreement in the decision.

**Composite cross-check (0-100)**: official 55.0 → 3 · EIC-weighted 54.9 → 3 (-0.1 vs. official)  
**Decision ceiling**: none (no upheld DA-CRITICAL issue). The EIC's decision starts from the EIC-weighted rating and may depart from it in either direction, with a written reason.
#### Ledger mode: aspect-weighted average (iclr)

| Reviewer type | Aspect | Aspect share | Weight |
|---|---|---|---|
| T1 (Computer-use / GUI-agent specialist) | experimental_validation | 19% | 0.235 |
| T2 (Agent-evaluation and experimental-design methodologist) | technical_rigor | 23% | 0.141 |
| T3 (Learning-from-observation / inverse-dynamics researcher) | novelty | 16% | 0.194 |
| T4 (Temporal action localization / video-grounding researcher) | technical_rigor | 23% | 0.141 |
| T5 (VLM pretraining and data-scaling researcher) | significance | 16% | 0.194 |
| T6 (Responsible data-collection and data-governance researcher) | ethics | 8% | 0.094 |

**Final rating (aspect-weighted mean)**: **3.19** → **3 (Borderline Reject)** · plain mean 3.17 · weighted pool position 53.0
### Cross-Venue Outlook

| Venue | Venue-weighted composite | Bar offset | Venue shift | Band → with DA cap | Venue recommendation | Venue sub-scores | Scale status |
|---|---|---|---|---|---|---|---|
| ICLR (2026) | 54.9 | +0 | +0 | 3 → 3 | 4 on {0,2,4,6,8,10} (5 on {1,3,5,6,8,10}) | Soundness 2, Presentation 2, Contribution 2 | secondary |

Emphasis weights are this skill's heuristics, not official venue weights. Scale status: official / confirmed / secondary / assumed / unpublished (see references/venue_profiles.md). Upheld DA-CRITICAL caps apply to every venue.

- **ICLR**: Soundness/Presentation/Contribution 1-4 and Confidence 1-5 are long-standing. Overall rating reported as {0,2,4,6,8,10} for ICLR 2026; earlier cycles used {1,3,5,6,8,10}. Both are shown.
