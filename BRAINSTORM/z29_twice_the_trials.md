# z29_twice_the_trials — why the b = 1 line is far more robust than (★) (O259; B1_LINE §3.1)

**Idea.** O258 asked why "p + 4d has a divisor ≡ −1 (4d)" fails 3 times ≤ 10⁸ while (★) fails 14 times. The suspects were
forced levels / genus structure / variance.
**Literature.** PARITY_AUDIT Lemma 2.1 ((★) incidence count R(p), main term (log p)²/8); López 2404.01508 Thms 4, 7 (Types A/B).
**Result (PROVED + EVIDENCE).** Lemma 3.1: N₁(p) = #{(c, d) : 4cd − 1 | p + 4d}. Every incidence is a distinct solution, with
main term (log p)²/8. (★)'s R(p) has the same main term, but its incidences come in swapped pairs (u, B) ↔ (B, u) that give
the same solution. So (★) has (log p)²/16 distinct trials, half as many. With Prop 1.4 (b = 1 is exposed only on p ≡ 1 (24),
(★) on p ≡ 1 (8)) this accounts for the gap. Data: N₁/N_{c1} = 1.67 → 1.85 from 10⁶ to 10¹² (consistent with 2; not proved). Smooth-(p − 1) classes
depress both lines by the same 16–20 %. The genus/forced-level structure is the same for both (Lemma 1.2), so it does not
discriminate.
**Barrier screen.** B3: this is a statement about the main term of a polylog lottery, not a mechanism. B6: averages over p.
T1/105: both lines fail there; nothing changes.
**Cheap numerics.** `logs/z29_classes.txt` (14 class samples, 10⁶–10¹²); `logs/z29_model.txt`.
**Assessment.** PROVED (main terms, the swap involution) + EVIDENCE (ratios). The answer to O258 spark 1 is mundane:
**twice the trials, half the exposure.** No hidden 4-adic robustness.
