# z52d avenue — batch P04 (100 items) summary
ES is OPEN. Rows: `out_P04.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source.

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 40 | 0 | 0 | 0 | 40 |
| known-false | 30 | 0 | 0 | 0 | 30 |
| circular | 23 | 0 | 0 | 0 | 23 |
| unclear | 5 | 0 | 1 | 0 | 6 |
| open-plausible | 0 | 1 | 0 | 0 | 1 | (Z2921 = PILOT Z2609's involution question)
Novelty: 0 → 67, 1 → 33, 2 → 0. The batch is mostly calibration/infrastructure (41 rows: OEIS anchors, checkers, search tooling, census hygiene) and translation-lane dictionaries.

**Plausibility ≥ 2 AND novelty ≥ 1:** one item; it is calibration only.
* **Z0022** (FF Zaremba / λ ≤ 3 over F_q[T]): *for every irreducible P of large degree, some A has Artin-CF length ≤ 3 with the ES₅ sign condition.* A doable FF computation (deg ≤ 10 over F₃, F₅) after verifying the Niederreiter/Friesen FF-Zaremba statements; no ES yield (FF→ℤ transfer is blocked, (J)30).

**Recurring missing theorems**
1. *One tied divisor event / ES-strength single family at each p* (B2): Z0858, Z0860, Z0937, Z0777, Z2770, Z1468, Z3098, Z1783(b), Z2692, Z1976, Z1273, Z2746. Three items turn out to be **known families**:
   Z0858 (x | z) ⊇ López's b = 1 line, Z0860 (x | y) ⊇ the Type I a = 1 slice / X_slice, Z0937 (A287116) = "no ET Type II N-point" (details below).
2. *ES₅ existence over words; the per-word sign is already (A/p)* (dictionaries: determinants, Pfaffians, Tutte, dimers, LGV, Dedekind sums, tangles): Z2677, Z2763, Z2767, Z2784, Z2869, Z2659, Z2762, Z1486, Z0236, Z2324, Z1399.
3. *Size/zero-sum forcing of −1 among the divisors of one integer* (Kneser, Olson, EGZ/Kemnitz, DdS–H, Stepanov, Huang): Z1595, Z1598, Z2414, Z2428, Z2435, Z2595, Z1601; Z3006 is the 2-quotient (genus) layer, already pointwise free.
   Forcing needs ω(4Cp+1) ≫ √φ(4C), so it can only act at levels C ≲ (log log p)²; a uniform prime-tuples heuristic predicts infinitely many all-almost-prime failures there.
4. *Single-p count or equidistribution at a polylog target* (B3): Z1157, Z2501, Z2684, Z1339, Z2721, Z1892, Z2308, Z1498, Z2242.
5. *Finite congruence/identity covering* (B1): Z1114, Z2084, Z2263, Z1061, Z1321, Z2151, Z3008, Z1018; Z0462 is the obstruction-side counterpart (no AP of failures, by (D)30).
6. *Parity/M5*: Z1696, Z2921, Z0681, Z2330 (S₃ parity is vacuous on p ≡ 1 (4): O(p) = 6U(p)).

**New structural facts from this pass** (each a 1-line proof + check; scripts `scripts/z52d_avenue_P04_*.py`)
* Z0858: the ET Type II b = 1 slice (ad, acdn, cdn) is lcm-closed (all 1510 solutions at p ≡ 1 (4) < 3000 checked).
  So the x | z family contains López's line. With Pass 1 (193 and 66529 rescued), x | z fails at **exactly 2521 among primes ≤ 10¹¹**, inheriting B1_LINE §3.
* Z0860: Type I a = 1 solutions (bdn, cd, bcd) have sorted x | y (13 529 solutions at p < 2·10⁴; every prime p ≡ 1 (4) has one).
  So "x | y never fails" is explained by the I1 slice / X_slice (CONDITIONAL_ES §1, §6).
* Z0937: Dubickas–Novikas/A287116 (n = 4M − d, ab | M, d | a + b) is exactly ET Type II with e = d (CONDITIONAL_ES Lemma 1.2).
  Its finiteness is the Type II half of SQ, not a new route.

**Corrections to inputs and to a tempting shortcut**
* Z1500: Pass 1 refuted "square discriminant ⇒ finite automorph group" with a counterexample over ℚ, but the lemma is TRUE over ℤ (split forms have no Pell units). The item's reading ("no orbit dynamics on (★)") stands.
* POINTWISE_OMEGA13's W(p) bounds the witness modulus M = 4uC − 1, not the level C. Small levels with large u are not excluded.
  Polylog *level* windows are the open HC-type target (FRONTIER §7.2). Rows Z1783, Z2414, Z2428, Z2595 and Z3098 were written with this distinction. Z1468 assumed I3 proved; it is CERTIFIED to 10⁹ only (§7.17).

**Assessment.** No P04 item points at a proof architecture outside the repo's B1/B2/B3/T1 map. The useful outputs are the three identifications above (sub-families = known lines) and the forcing-confinement remark for item cluster 3. None has an ES yield.
