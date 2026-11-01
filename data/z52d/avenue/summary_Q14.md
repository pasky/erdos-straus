# z52d avenue — batch Q14 (113 items) summary
ES is OPEN. `out_Q14.jsonl`. Rows are Assessments unless they cite PROVED/CERTIFIED. Batch: 3 tools items, 37 ES₅/HJ-word
"translate" items, 13 thin-orbit/dynamics "upgrades", 16 triangle-group/topology analogues, 44 lattice/geometry/algorithmic/fingerprint leads. 31 rows are calibration-only.

**Status × plausibility** (columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| circular | 46 | 0 | 0 | 0 | 46 |
| known-true (gap named) | 0 | 0 | 0 | 36 | 36 |
| known-false | 18 | 0 | 0 | 0 | 18 |
| unclear | 5 | 3 | 0 | 0 | 8 |
| open-plausible | 0 | 1 | 2 | 1 | 4 |
| harder-than-open (corrected Apollonian local–global) | 1 | 0 | 0 | 0 | 1 |
Novelty: 0 → 41, 1 → 69, 2 → 3 (Z2799, Z1898, Z1991). Every plausibility-3 row is a calibration lemma or a main term (yield none).

**Plausibility ≥ 2 AND novelty ≥ 1 with any yield beyond calibration**
* **Z2995** (plausibility 2): *for 15·2^s + 1, a recursion (u,B,C)_s ↦ (u,B,C)_{s+k} on certificates, valid in each class of s mod k.* Thin family only; recurs with P00 Z3189.
* Z2601 (almost all via greedy dynamics) is already implied by Vaughan (B6). Z2799 (ES analogue for Hecke groups, novelty 2) and the other rows
  with plausibility ≥ 2 and novelty ≥ 1 (Z2837, Z2880, Z3084, Z3162, Z0157, Z0168, Z1917, Z2347, …) are calibration only, with yield none.

**Recurring missing theorems**
1. *ES₅ restated* (λ(p) ≤ 3 with a QNR, S₃(p) ⊄ QR; circular): Z2653, Z2662, Z2682, Z2690, Z2722, Z2723, Z2750, Z2751, Z2787, Z2789, Z2800, Z2801, Z2803, Z2876, Z2836, Z2987, Z2993, Z2998, Z3173.
   The cancellation tools in Z2723, Z2889, Z2998, Z3173 need |S_L(p)| ≥ p^δ (M1a), which gives only the λ(p) ≪ log p relaxation.
2. *Main term / counting in growing regions* (DRS/EM, area, dimension; B3): Z2826, Z2996, Z0551, Z1908, Z3052, Z0247, Z1348.
3. *Fixed menus / identity families / quasi-polynomials* (B1, known-false under H): Z2805, Z2897, Z2861, Z1118, Z1689, Z1103, Z1104, Z1979, Z2828, Z0975, Z2670.
4. *Upward-only transport* (monoid tN + 1 and conjugation orbits; the downward step is the divisor event): Z2846, Z2847, Z2861, Z0280, Z2673, Z3150.
5. *Geometry of numbers / Minkowski* (symmetric bodies give signed points, B4): Z0444, Z1436, Z0188, Z1750, Z1909.
6. *Lattice/Coppersmith algorithms* (find, never prove existence): Z1014, Z1397, Z1767, Z1777, Z1780, Z2016, Z1211.
7. *Triangle-group/topology dictionaries* (restatement or calibration): Z0153, Z0154, Z0157–Z0160, Z0168–Z0173, Z0186, Z1930, Z1991, Z1994, Z2347, Z2348.

**New in this pass** (scripts `scripts/z52d_avenue_Q14_*.py`, timeout 60–90 s)
* **Z0954 (PROVED, elementary; CERTIFIED for p ≡ 1 (4) < 2500): every solution of 4/p has z/x ≥ (3/4)√p and z ≥ p^{3/2}/2.**
  (Type II: 4b − a = p forces y′z′ ≥ p/4; Type I: the factor prime to p divides x′². Data: min z/x ≥ 2.02√p.) Kills balanced/bounded-height routes; explains Q03 Z0644.
* **Z0897 (PROVED):** solutions with denominators in arithmetic or geometric progression exist only for 4 | n (2-adic descent), so never at odd n.
* **Z2880 (EVIDENCE, 107 214 words):** the ES sign is a function of γ_w mod 8 but not mod 4, and not a conjugacy-class function on SL₂(ℤ/8) or SL₂(ℤ/16).
* **Z2673:** Kirby blow-down sends formal words to length-2 HJ chains of the same p/A (K(c,1,s) = K(c−1, s−1)). **Z2800:** the ES sign (A/p) is the linking-form class of L(p,A).

**Corrections.** Z1917: (★)-failures ≡ 1 (24) is forced, not 'interesting': (★) holds identically at p ≡ 5 (8) (u = 1, B = 2) and p ≡ 2 (3) (u = C = 1).
Z2662: Pass 1's Legendre-split table is a selection artefact. Z2751: no uncertainty-principle contradiction exists (singletons ⊆ QR).
**Assessment.** Nothing in Q14 escapes B1/B2/B3/B6/M1a; the ES₅ cluster collapses onto ES₅ itself. Z2995 duplicates P00 Z3189. Main output: the √p imbalance lemma.
