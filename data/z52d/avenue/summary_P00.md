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

**Plausibility ≥ 2 AND novelty ≥ 1 with some proof yield** (17 others, incl. Z2598, Z2352, Z2616, are calibration/no ES yield):
* **Z0671**: *RESIDUE_HARDNESS local factor: inf_p F(p) ≥ c > 0 even at pseudosquare-type p* (main-term floor; partial, B3).
* **Z3189**: *certificates of an open thin family (15·2^s+1) follow linear recurrences on classes of s*; test BM on *proof* certificates of 3·2^s+1.
* **Z2579**: *the H-conditional no-gos (B1 Thm C, B2(iii), FORMAL_CLOSURE Thm F) hold unconditionally over F_q[T], q ≫ 1, via Bary-Soroker*. This validates the barriers; it does not prove ES.

**Recurring missing theorems**
1. *One tied divisor event / single-integer lower tail* (circular): Z0072, Z0501, Z0661, Z1373, Z1375, Z1511, Z1623, Z1624, Z2290, Z2394,
   Z3185, Z0034, Z1426, Z1470, Z0303; thinner-lottery strengthenings Z0682, Z0117, Z0200, Z0261.
2. *Union of two word lines* (circular; disjoint failures = independent lotteries): Z0757, Z0771, Z1592, Z1624. 3. *Cancellation in E(p)* (§7.1, plaus 1): Z1034, Z1855.
4. *Relaxation collapse, no transport* (B-fin): Z0052, Z0053, Z0054, Z0074, Z0087, Z0096, Z0297, Z0318, Z1505, Z2037, Z2772, Z0084, Z0171.
5. *Identity/polynomial families vs T1/B1*: Z0020, Z1585, Z0037, Z0038, Z1401, Z2352, Z2616, Z2127, Z1837.
6. *Cross-level pooling vs privacy of large primes*: Z1035, Z1072, Z3141; the precise open form is Z2818 (= §7.6, full-factor multiset).
7. *I3 model problem*: Z0754, Z0776, Z1852 (per-box Kloosterman PROVED useless), Z2777.

**New in this pass** (scripts `scripts/z52d_avenue_P00_*.py`, timeout 60)
* Z0216 (PROVED; matches all 161 stored failures < 2·10⁴): chain world x|y|z fails iff (p+1)/2 has no prime ≡ 3 (4) — Landau-type, density → 0.
* Z0052/54/87 (PROVED): ℤ[1/ℓ]-ES for **every** odd ℓ — Dirichlet prime q ≡ 3 (4), (ℓ/q) = −1 ⇒ q | 1 + ℓ^k, k = ord_q(ℓ)/2 odd.
  Z0318: k unbounded under H (sketch: ℓ, (ℓ+1)/2, Φ_{2d}(ℓ) prime) — B1 Thm C in miniature.
* Z1624 (PROVED, checked p < 3000): Type I c = 1 ⟺ ∃k: pk + 1 has a divisor ≡ −p (mod 4k) (multiplicative twin of (★)).
* Z0761: R(n) ≥ 1 for every n ≡ 5 (8) (u = 1, B = 2, C = (n+3)/8). Z1846: m² + 4 (m odd) ≡ 5 (8): trivial.
  Z0261: (★) gives xyz = p²u²B²C³ (square ⟺ C square). Z1591: C-form sign variants give only signed solutions.

**Corrections.** Z1511/28/23: (★) is a finite search (C ≲ p/4), so 409, 577, 5569, 9601 are exact zeros. Z1505: not 2-adic (every S ≠ ∅
trivialises). Z1282: 4.7× ratio = divisor inheritance. Z1591: Pass 1 summary inconsistent. Z2579: H-conditional lines are no-gos.

**Assessment.** Nothing in P00 escapes the B2 / H⁻_BM / relaxation-transport picture. Handles are main-term (Z0671), thin-family (Z3189)
or sibling barrier validation (Z2579). Cleanest gap statement: Z2818 — a provable property of the real factorisations of {4Cp+1}_C beyond CRT.
