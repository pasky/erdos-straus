# Hostile review R92 of POINTWISE_TYPEI5.md (task O92)

Reviewer: side agent R92 (branch `side-agent/review-typei5`). Reviewed: `side-agent/lfl-sign-point` up to `853e4de`
(incl. Lemma 3.6 case A, Theorem 3.7). From-scratch scripts: `scripts/review_typei5_*`.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (Lehmer minimality) | SOUND (MINOR wording: L1, L2) |
| Cor 1.2 (`k ∈ {1,2,4}`; engine complete) | SOUND, can be sharpened to `k ∈ {1,2}` (L3) |
| (filled in below) | |

## Lemma 1.1 — SOUND

Re-derived line by line.
* (a) The ratio `η/η'` has norm 1 and the shape `A + 4B√d` ✓; `α·G` has the shape ✓; positive solutions ↔ elements `> 1`
  of `αG` (with the conjugation `√Q ↦ −√Q`, `η^{-1} = 4X√P − u√Q`) ✓; `u√Q = (η−η^{-1})/2` increasing ✓.
  `m ≥ 3` ⇒ `αν_0^{-1} ∈ (1,α)` ✓. `m = 1` ⇒ positive solutions `α^n`, `n` odd ✓.
  `m = 2`: `α, α^{-1} ∈ ℚ(√d)` ⇒ `√P ∈ ℚ(√d)` ⇒ `P` or `Q` is a perfect square. `P = p²` ⇒ all `u = 4Bp` even ✓.
  `Q = q²` is excluded since `u` odd forces `Q ≡ −u^{-2} ≡ 7, 15 (mod 16)` — not by "`Q ≠ 1/k²`" (see L2).
* (b) integrality, (c) `L_n ≡ n (mod 7)`, (d) `L_7 = 7s⁶+35s⁴r²+21s²r⁴+r⁶ ≡ 7 (mod 49)`, (e) `L_{mn}(α) = L_n(α)L_m(α^n)`,
  `L_m ≥ m s^{m−1} > 1`, (f) the descent `n = 7^r n'` — all ✓. (f) uses `L_{7^r}(α^{n'})` integral, true by (b) applied to
  the solution `α^{n'}`.
* From scratch (`scripts/review_typei5_lehmer.py`):
  (1) all solutions with `u ≤ 2·10⁴` for `P ≤ 40`, `7 | Q ≤ 280` (15 solvable systems, 6 with ≥ 2 solutions in range):
  the solution set is exactly `{α^n}` (exact powering), `u_n/u_1 ≡ n (mod 7)`, 7-power `u` only at `n = 1`.
  (3) 1148 systems **constructed** to contain a solution with `u = 7^b` (`b ≤ 3`, `X ≤ 60`, `Q ≤ 2·10⁴`): the brute-force
  search over all smaller `u' < 7^b` finds no solution in any of them, so the 7-power solution is minimal, as claimed.

Defects:
* **L1 (MINOR)**, Lemma 1.1(a): "`G` … is infinite cyclic". `G = {A+4B√d : A²−16dB²=1}` contains `−1`, so it is `{±1} × ℤ`.
  Repair: write `G_+ := G ∩ (0,∞)` (infinite cyclic, generator `ν_0`). Only positive elements are used afterwards.
* **L2 (MINOR)**, Lemma 1.1(a), `m = 2`: "`√P = p ∈ ℤ` (`√P ∈ ℚ(√d)`, `Q ≠ 1/k²`)" is garbled. Correct statement: `√P ∈ ℚ(√d)`
  means `P` is a square or `Q` is a square. `Q` square is impossible when some `u` is odd (`Qu² ≡ −1 (mod 16)` gives
  `Q ≡ 7,15 (mod 16)`). Repair: replace with this sentence.

## Corollary 1.2 — SOUND (sharpening L3)

* Hypotheses ✓: `v_7(d) = a` odd ⇒ `d` is not a square; `u = 7^b` odd; `7 | Q`. The step from Lemma 1.1 to "`α² = ν_0`" is
  `m = 1` ✓.
* **L3 (MINOR, sharpening)**: `k ∈ {1,2}`, not just `{1,2,4}`. For odd `d`, a norm-±1 unit `x + y√d` has `x + y` odd, so `xy`
  is even and `ε² = (x²+dy²) + 2xy√d` has `4 | 2xy`. So `(ℤ[√d]/4)^×/(ℤ/4)^×` (order 4) has exponent 2. From scratch:
  over all 1473 odd non-square `d ≤ 3000`, `k = 1` occurs 915 times, `k = 2` 558 times, and `k = 4` never. The author's claim is
  true but weaker than necessary; the engine completeness ("`mmax ≥ 4`") holds a fortiori (`mmax ≥ 2` suffices).
  `typei4_dgraded.py` uses `fund(d)` = least `x > 1` with `x² − dy² = 1` in `ℤ[√d]`, i.e. exactly `ε_f`, so the
  completeness transfer is valid.
* Comp 1.3 relies on the replay of `typei4_dgraded.py 5 24 3000 6`; see the §2 checks below (my own engine).

## Lemma 2.1, `typei5_dmod`, Comp 2.2 / Cor 2.3 — SOUND (CERTIFIED part replayed, cross-checked on small range)

* Lemma 2.1 re-derived: `α² = (16PX²+Qu²) + 8Xu√d = (2Qu²+1) + 8Xu√d`. `A = 32PX² − 1 ≡ −1 (mod 32)` follows directly from (1.1),
  without citing TYPEI4 Prop 1.2. `B = 8Xu ≡ 8 (mod 16)` (`Xu` odd). `v_7(B) = b` (`7∤X`). `v_7(A−1) = v_7(2·7^aQ_1·7^{2b}) = a+2b`
  (`7∤Q_1`, since `Q_1 | M ≡ T (mod 7)`). `(A−1)/(2·7^{a+2b}) = Q_1 | M` ✓.
* Code audit of `scripts/typei5_dmod.c`. The CF loop stops at the first `q = 1`. Then `p1/q1` is the convergent of index
  `per−1`, with `p²−dq² = (−1)^per`, and it is squared when `per` is odd ✓. The residues mod `2^64` (wrap-around) and mod `7^22`
  (u128 mulmod) are exact ✓. `ν_0` is the least power with `4 | B` (by L3 that is `k ≤ 2`) ✓. Each test is only a
  **necessary** condition. Edge cases: `v_7(B) ≥ 22` gives `B7 = 0`, `vB := 22`, and the run then requires `vA ≥ 22`, which a
  genuine certificate meets. If `a+2vB ≥ 22`, it also requires `vA ≥ 22` (necessary). The `Q_1` filter compares
  `Q_1 mod 7^{22−sh}` with all divisors `q_1` of `M` and with `M/q_1`. That is necessary and exact when `7^{22−sh} > M`. If `sh > 18`,
  the field is flagged `WEAK` and not filtered. Overflow: `d ≤ 10^{12} + 64·10^6`, and `m²`, `q·a` stay below `2^63` ✓. Loop range:
  `c_o` odd with `v_7(c_o)` odd, `δ` odd, `c_oδ ≤ CD`, which covers all fibre certificates oriented with `δ > 0` ✓.
  **No soundness defect found.**
* From-scratch exact engine `scripts/review_typei5_engine.py`. It uses big-integer `ε_f` and `ν_0`, then for **every** divisor
  `P_1 | M` it tests exactly whether `A+1 = 32c'P_1X²`, `A−1 = 2·7^aQ_1u²`, with `X` odd, `7∤X`, `u = 7^b`. Results:
  - `L = 5..24`, `c_oδ ≤ 3000`: exactly the 8 certificates of Comp 1.3/2.2. They are identical to `typei5_dmod 5 24 3000`
    (same `(L,c_o,δ)`, same `b`, `k = 1` in all).
  - `L = 7..12`, `c_oδ ≤ 10⁴`: 16 980 fields, exactly 1 certificate (`L = 11`, `c_o = 21`, `δ = 7`). `typei5_dmod 7 12 10000`
    has the same single survivor. **No certificate at `L = 7..10`.**
  - `L = 13..26`, `c_oδ ≤ 6000`: see below.
  So on these ranges the filter drops no certificate, and its only survivors are genuine certificates.
* Replay of the 10⁶ runs (Comp 2.2, last bullet): not replayed in full (4 × 15 min). Partial replay: see below.
* Cor 2.3 (combination with TYPEI4 Cor 3.5) ✓ as a logical statement. The label is fine once the 10⁶ runs are replayed.
