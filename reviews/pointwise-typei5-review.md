# Hostile review R92 of POINTWISE_TYPEI5.md (task O92)

Reviewer: side agent R92 (branch `side-agent/review-typei5`). Reviewed: `side-agent/lfl-sign-point` up to `853e4de`
(incl. Lemma 3.6 case A, Theorem 3.7). From-scratch scripts: `scripts/review_typei5_*`.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 1.1 (Lehmer minimality) | SOUND (MINOR wording: L1, L2) |
| Cor 1.2 (`k ∈ {1,2,4}`; engine complete) | SOUND, can be sharpened to `k ∈ {1,2}` (L3) |
| Lemma 2.1 + `typei5_dmod` filter | SOUND (code audited; agrees exactly with independent exact engine) |
| Comp 2.2 / Cor 2.3 (`L=7..10`, `c_oδ ≤ 10⁶`) | CERTIFIED: replayed (0 survivors ×4) |
| Comp 1.3 (`L=5..24`, `c_oδ ≤ 3000`) | CERTIFIED: reproduced by independent exact engine (same 8 certificates) |
| Lemma 3.1 (`λ ∈ ℤ` without `7∤j`) | SOUND; closes R89-S2 |
| Lemma 3.2 (H), (Lin) | SOUND (sympy from scratch) |
| Prop 3.3 (i)–(v) | SOUND (MINOR P1, P2) |
| Comp 3.4 (regimes (ii),(iii) empty at `L=7..10`, all `b`) | CERTIFIED: independently reproduced with own engines + positive controls (MINOR C1) |
| Lemma 3.6 (case A empty, `L ≤ 10`) | SOUND (MINOR A1) |
| Theorem 3.7 (only regime (v), `b ≥ 8`, `c_oδ > 10⁶` remain) | SOUND (MINOR T1, T2) |

**Overall: no FATAL or MAJOR defect.** The labels are justified. The only open part at `L = 7..10` is regime (v), and the
document states this honestly. Defects: L1, L2, L3, P1, P2, C1, A1, T1 (all MINOR).

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
  - `L = 13..26`, `c_oδ ≤ 6000`: 22 484 fields and exactly 10 certificates. The list is identical to the 10 survivors of
    `typei5_dmod 13 26 6000`, including the TYPEI4 `L = 14` pair `(c_o,δ) = (21,173), (707,5)` and a new `L = 26` one
    `(21,131)`. All have `k = 1` and `b ≤ 1`.
  So on these ranges the filter drops no certificate, and its only survivors are genuine certificates.
* **Replay of Comp 2.2 (10⁶)**: `typei5_dmod L L 1000000` for `L = 7, 8, 9, 10` gives 426 697 fields each, 2.02/2.02/1.52/1.90·10¹⁰
  CF steps, **0 survivors each**, matching the author. Comp 2.2 / Cor 2.3 are therefore **CERTIFIED (replayed)**, with the
  filter validated against an independent exact engine on the smaller ranges above.
* Cor 2.3 (combination with TYPEI4 Cor 3.5) ✓ as a logical statement. The label is fine once the 10⁶ runs are replayed.

## Lemma 3.1 — SOUND (fixes R89-S2)

Re-derived. TYPEI4 Lemma 3.1(iii) with `y = c'gδ` gives `mP_1 = y² − 2·7^a m u j`. Since `T/2 ∈ ℤ` (`L ≥ 5`), we have
`ρP_1 = Tu/2 + j ≡ j` and `y ≡ −j (mod u)`, so `(ρj − m)P_1 ≡ j² − j² = 0`, and `7 ∤ P_1`. The hypothesis `7 ∤ j` is not used ✓.
This closes the `7 | j` gap of TYPEI4 Lemma 3.6 (R89-S2). Note: TYPEI4 Lemma 3.6's other claims ("`λ` even", `λ ≥ 0`) were
proved with `7∤j` only through integrality. Their proofs are otherwise independent of `7 ∤ j`, so the whole Lemma 3.6 now holds for all `j`.

## Lemma 3.2 (H), (Lin) — SOUND

`scripts/review_typei5_identities.py` (sympy, from scratch):
`ρ(y² − 2Wmuj) − m(Tu/2+j) = −(u/4)·[ρΔ − 2λ(Tu+2j)]` identically after `m = ρj − λu`. This is (H). (Lin) is exactly what you get from substituting
`m = λ[u(2Tj−Δ)+4j²]/Δ` into the definition of `Δ`. `Δ ≠ 0` is automatic when `λ ≠ 0` (since `ρ ≥ 1` in (H)) ✓.

## Proposition 3.3 — SOUND (MINOR remarks P1, P2)

All five regimes re-derived by hand; the algebra was checked in sympy (same script):
* (i) ✓. `j | T²u ⇒ j = 7^r`. If `r < b` then `7 | 8Wρj + 6T`, which fails both for `r ≥ 1` and for `r = 0`, `b ≥ 1` (here `7 | W`).
  Hence `T(T−6) = 8·7^{a+b}ρ`, and `2^k ≢ 6 (mod 7)`.
* (ii) ✓. `m > |λ|u` and `P_1 ≥ 1` give `8W|λ|j < T²`. Then (Lin) with `Δ = −x`, `κ = −K_1` gives `u(Kx − E) = x² + 6Tjx + 4K_1j³`,
  with `K = T² − K_1j > 0` (sympy ✓). The constant `K²N(E/K) = E² + 6TjEK + 4K_1j³K²` is correct.
* (iii) ✓. Sign: the RHS is `< 0` because `0 < Δ < 2Tj`, hence `g > 0` and `Wλs < T³/4`. `R := g³N(sT²/g) = κs³(4T³ − sκ)²`
  (sympy ✓, so it also equals the author's other form). The polynomial division `g³N(j) − R = (gj − sT²)·q(j)` has
  `q ∈ ℤ[s,T,κ][j]` (sympy ✓). That integrality is what makes `(gj − sT²) | R` legitimate. It is implicit in the text.
* (iv) ✓. (Lin) gives `−2j(T³u − 4T²j − 2κj²) = 0`, so `T²(T−4) = 16·7^{a+b}λ` and `7 | T−4`, i.e. `L ≡ 0 (mod 3)`. At `L = 9`:
  `7^{a+b}λ = 1792 = 7·256`, so `a = 1`, `b = 0` ✓.
* (v) ✓. `ρ > λu/j` (from `m > 0`) and (H) give `σ < 4j²/u`. The displayed identity `κjωσ = (2Tj+σ)[(2Tj−σ)² − ωT²]` holds (sympy ✓).
* **P1 (MINOR)**, (v): the displayed divisibility constant `4κσ³T⁶ + (2T³+σκ)σ³κ(6T³+σκ)` equals `κσ³(4T³+σκ)²` (sympy ✓).
  It is `−g'³N_v(−σT²/g')`, i.e. the sign is flipped relative to (iii). That is harmless for divisibility, but write the factored form `κσ³(4T³+σκ)²`.
* **P2 (MINOR)**, (iii)/(v): say explicitly that the quotient `g²q(j)` has integer coefficients (see above). Otherwise
  "`(gj − sT²) | R`" reads as if `gcd(g, gj − sT²) = 1` were assumed.
* Label: PROVED is appropriate. The "Interpretation" paragraph is correctly labelled Assessment.

## Computation 3.4 — SOUND (independently reproduced)

From-scratch implementation from my own derivation (I did not read or reuse `typei5_regimes.py`):
* Regime (ii), `scripts/review_typei5_regimes.py`. For every `(a, λ<0, j)` with `8·7^a|λ|j < T²` and every `b` up to a
  rigorous bound (`u ≤ N(x_max)`, `x_max = (C+E)/K`), it solves the quadratic `x² + (6Tj − uK)x + 4K_1j³ + uE = 0` exactly.
  Cases: 1 / 5 / 35 / 189 at `L = 7/8/9/10`. 7-power solutions of (Lin): 0 / 0 / 2 / 4. All of them have `b ≤ 1` and all fail
  integrality of `ρ`, of `P_1`, or positivity.
* Regime (iii), `scripts/review_typei5_reg3.c`. For every `(a,λ,s)` with `7^aλs < T³/4`, it enumerates all divisors `e` of
  `R = κs³(4T³−sκ)²` with `e ≡ −sT² (mod g)` and `j` odd, and tests `N(j)/e ∈ 7^ℤ` modulo two 61-bit moduli. A genuine solution
  always passes, and `b ≤ 400` is asserted per case. Survivors are verified exactly. Divisor counts: 28 200 / 963 240 /
  26 784 792 / 582 233 076 (the author has 28 320 / 9.6·10⁵ / 2.7·10⁷ / 5.8·10⁸; the small difference at `L = 7` is presumably
  a `≤`/`<` boundary convention and harmless). Survivors: 0 / 0 / 2 / 4. All have `u ∈ {1, 7, 343}` and all fail the full
  conditions (non-integral `ρ` or `P_1`, or `X` even).
* Positive controls. Run with the target `u = 4003` (`L = 7`) resp. `u = 293` (`L = 9`) instead of 7-powers, the regime-(iii)
  engine finds exactly the relaxed regime-(iii) solutions `(a,λ,s,j) = (1,2,8,31)` resp. `(1,2,440,73)`. With `u = 293` at
  `L = 7` (a regime-(v) solution) it correctly finds nothing.
* The full conditions (`m = c'δ²`, `y = c'gδ`, TYPEI4 Lemma 3.1(iii), `X` odd and prime to 7, `7 ∤ P_1`) are re-implemented in
  `full_check`.
* Relaxed brute force `scripts/review_typei5_relax.c` (TYPEI4 Cor 3.2 with `7^b` replaced by an arbitrary odd `u`; own loops), with
  `u ≤ 6001 / 4001 / 2001 / 2001` at `L = 7/8/9/10`: 2 / 0 / 6 / 2 solutions, i.e. `L=7`: `u = 293, 4003`; `L=9`: `u = 5` (×3),
  `37, 293, 1853`; `L=10`: `u = 293, 1159`. `scripts/review_typei5_classify.py` classifies them exactly as the author does:
  4003 → (iii), 293(L7) → (v); `L=9`: 5 → (ii) and case A ×2, 37 → (ii), 293 → (iii), 1853 → (v); `L=10`: 1159 → (ii), 293 → (v).
  In all 8 case-B solutions (H), (Lin) and the bound of the regime hold, and (iii) satisfies `e | R`.
* **C1 (MINOR)**, §3, after Lemma 3.2: "Checked on all 9 relaxed solutions … at `L = 7, 9, 10`". My brute force gives 10 in the
  same ranges: 8 in case B and 2 in case A. Repair: state the count per case.
* Regime (iv): re-derived. Empty unless `L ≡ 0 (mod 3)`. At `L = 9` it forces `(a,b,λ) = (1,0,256)`, which is covered by TYPEI4 ✓.

## Lemma 3.6 (case A empty at `L ≤ 10`) — SOUND (MINOR A1)

Re-derived line by line:
* `P_1 = c'g² + 2·7^a uJ`, and `P_1 | z = Tu/2 − J > 0` (TYPEI4 L3.1(i)), so `2·7^a uJ < Tu/2`, i.e. `J < T/(4·7^a)` ✓.
  `L = 7, 8`: none. `L = 9`: `J = 1`, `a = 1`.
* **A1 (MINOR)**: at `L = 10` the bound only gives `J < 64/28`, i.e. `J ∈ {1, 2}`, and `a = 1`. `J = 2` is excluded because
  `J = y − Tu/2` is odd (`y` odd, `T/2` even for `L ≥ 6`), but the text never says so. Repair: add "(`J` is odd since `y` is odd
  and `Tu/2` is even)".
* `ρ = z/P_1 < (Tu/2)/(14u) = T/28 < 3`, and `ρ` is odd (`z` odd), so `ρ = 1` ✓. `c'g² = Ku − 1` ✓. `X = (1+7u)/(4G)` (since
  `7^{a+b}z/P_1 = 7uρ`) ✓. `G | 7(Tu/2+1) − (T/2)(7u+1) = 7 − T/2 ∈ {−9, −25}` ✓. Then `c'g² ≤ G²` gives `u ≤ 41` (`L=9`: `2u−1 ≤ 81`;
  `L=10`: `18u−1 ≤ 625`) ✓. `u = 7`: `4 ∤ 50` ✓. `u = 1`: `G = 1`, `K = 2`, so `X = 2` is even ✓. (`g` is odd because `g = 4P_1X − D`
  with `D` odd, so `G` is odd ✓.)
* The proof never uses `u = 7^b` before the last line, so it also bounds **relaxed** case-A solutions at `L = 9, 10` by `u ≤ 41`.
  My relaxed brute force (`u ≤ 2001`) finds exactly the two `L = 9`, `u = 5` solutions, with `ρ = 1` and `G ∈ {3, 9}`, which
  divide `9` ✓. None at `L = 10` ✓.
* §4's remark ("case A is a small finite check at every `L`") is correct. `J`, `a` and `ρ < T/(4·7^aJ)` are bounded. Also
  `G | 7^aρJ − T/2 ≠ 0`, and `c'g² = (Tu/2 − J)/ρ − 2·7^auJ ≤ G²` bounds `u` (the coefficient `T/(2ρ) − 2·7^aJ` of `u` is
  nonzero by 7-adic valuation and must be positive). It is not labelled as a theorem, which is fine.

## Theorem 3.7 — SOUND as a summary (MINOR T1, T2)

The case split is exhaustive: case A/B (`2y ≠ Tu` by parity). In case B, `λ <0, =0, >0` and `Δ <, =, > 2Tj`. Cases A, (i), (iv)
are excluded by hand. (ii) and (iii) are excluded by Comp 3.4, which I reproduced independently for all `b`. That leaves regime
(v). Exactly this remains: **regime (v) at `L = 7..10` with `v_7(k) ≥ 8` and `c_oδ > 10⁶`**.
* **T1 (MINOR, provenance)**: "`v_7(k) ≥ 8` (TYPEI4 Cor 3.5)" inherits R89-D5. At `L = 7,8, b = 7` and `L = 9,10, b = 6,7`,
  TYPEI4 Cor 3.5 rests on `typei4_lb` alone. Since TYPEI5 now excludes regimes (ii)–(iv) and case A for **all** `b` (here
  independently replicated), only the regime-(v) part of those `(L,b)` slices depends on the single engine. Repair: mention
  this in the theorem, or replicate `typei4_lb` on those slices restricted to regime (v).
* **T2 (MINOR, label)**: "PROVED + CERTIFIED once replayed". The CERTIFIED inputs are Cor 2.3 (10⁶ dmod runs) and Comp 3.4. The
  status of my replays is in the summary table. The theorem is a summary of exclusions and claims nothing about regime (v) beyond
  the per-`(σ,a,λ)` finiteness, so it does not overclaim.
