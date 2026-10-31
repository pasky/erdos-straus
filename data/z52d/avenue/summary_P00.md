# z52d avenue — batch P00 (100 items) summary
ES is OPEN. Rows: `out_P00.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source.

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named) | 4 | 1 | 3 | 34 | 42 |
| circular | 21 | 0 | 0 | 0 | 21 |
| known-false | 19 | 0 | 0 | 0 | 19 |
| open-plausible | 0 | 6 | 3 | 2 | 11 |
| unclear | 4 | 3 | 0 | 0 | 7 |
Novelty: 0 → 49, 1 → 50, 2 → 1 (Z0266, Arakelov; plaus 0, B3). Most plaus-3 rows are calibration lemmas (yield none).

**Plausibility ≥ 2 AND novelty ≥ 1 with some proof yield** (the other 17 such rows are calibration only):
* **Z0671**: *the RESIDUE_HARDNESS local factor satisfies inf_p F(p) ≥ c > 0, even at primorial-pinned/pseudosquare p* (main-term floor; partial, B3).
* **Z3189**: *on each residue class of s, certificates of an open thin family (15·2^s+1) follow linear recurrences*; first test: Berlekamp–Massey on the *proof* certificates of 3·2^s+1, 63·2^s+1 (partial, thin family only).
* **Z2579**: *the H-conditional no-gos (B1 Thm C, B2(iii), FORMAL_CLOSURE Thm F) hold unconditionally over F_q[T], q ≫ 1, via Bary-Soroker*. This validates the barriers; it does not prove ES.
* Z2598 (FF circle-method average, B6), Z2352/Z2616 (B1 re-proofs): no ES yield.

**Recurring missing theorems**
1. *One tied divisor event / single-integer lower tail* (circular): Z0072, Z0501, Z0661, Z1373, Z1375, Z1511, Z1623, Z1624, Z2290, Z2394,
   Z3185, Z0034, Z1426, Z1470, Z0303; strengthened versions (thinner lotteries): Z0682, Z0117, Z0200, Z0261.
2. *Union of two word lines* (circular; disjoint failures are what independent lotteries predict): Z0757, Z0771, Z1592, Z1624.
3. *Cancellation in E(p) at fixed p* (FRONTIER §7.1, plaus 1): Z1034 (Voronoi), Z1855 (piecewise-linear pieces).
4. *Relaxation collapse, no transport* (B-fin): Z0052, Z0053, Z0054, Z0074, Z0087, Z0096, Z0297, Z0318, Z1505, Z2037, Z2772, Z0084, Z0171.
5. *Identity/polynomial families vs T1/B1*: Z0020, Z1585, Z0037, Z0038, Z1401, Z2352, Z2616, Z2127, Z1837.
6. *Cross-level pooling vs privacy of large primes*: Z1035, Z1072, Z3141; the precise open form is Z2818 (= §7.6, full-factor multiset).
7. *I3 model problem*: Z0754, Z0776, Z1852 (per-box Kloosterman PROVED useless), Z2777.

**New in this pass** (scripts `scripts/z52d_avenue_P00_*.py`, timeout 60)
* Z0216 (PROVED + CERTIFIED to 2·10⁴): the chain world x|y|z at p ≡ 1 (4) fails iff (p+1)/2 has no prime factor ≡ 3 (4).
  This is a Landau-type set of relative density → 0, not "square class + lottery"; the criterion reproduces all 161 stored failures.
* Z0052/Z0054/Z0087 (PROVED): positive ES over ℤ[1/ℓ] for **every** odd ℓ. Proof: take one Dirichlet prime q ≡ 3 (4) with
  (ℓ/q) = −1; then k = ord_q(ℓ)/2 is odd and q | 1 + ℓ^k. Checked ℓ < 3000. Z0318: k is unbounded under Hypothesis H (sketch;
  the family is ℓ, (ℓ+1)/2, Φ_{2d}(ℓ) prime). This is B1 Thm C in miniature.
* Z1624 (PROVED, checked p < 3000): Type I with c = 1 ⟺ some pk + 1 has a divisor g ≡ −p (mod 4k). It is the multiplicative twin
  of (★): ∃u such that p + u has a divisor ≡ −1 (mod 4u).
* Z0761: R(n) ≥ 1 for every n ≡ 5 (8) (u = 1, B = 2, C = (n+3)/8). Z1846: m² + 4 (m odd) is ≡ 5 (8), so the family is trivial.
* Z0261: a (★) solution has xyz = p²u²B²C³, so it is a square iff C is a square. Z1591: the sign variants of the C-form give only signed solutions.

**Corrections to inputs.** Z1511/Z1528/Z1623: (★) is a finite search (C ≲ p/4), so 409, 577, 5569 and 9601 are exact zeros, and "search
C ≤ 10⁶" is moot. Z1505: the collapse is not 2-adic; every S ≠ ∅ trivialises. Z1282: Pass 1's 4.7× split/irreducible ratio is
mostly divisor inheritance. Z1591: the Pass 1 summary is internally inconsistent. Z2579: the repo's H-conditional lines are no-gos,
not ES proofs.

**Assessment.** No P00 item points to an architecture outside the B2 / H⁻_BM / relaxation-transport picture. The only
proof-relevant items with a visible handle are main-term-side (Z0671), thin-family (Z3189) or sibling barrier
validation (Z2579). Z2818 states the gap most cleanly: find a provable property of the actual factorisations of
{4Cp+1}_C that CRT consistency lacks.
