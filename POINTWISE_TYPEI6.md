# Regime (v) at the sign point `x̂_9` (task O99)

Status: side agent O99 (branch `side-agent/regime-v-units`), checkpoint report `reviews/agent-reports/AGENT_REPORT_O99.md`. Hostile review R99 (`reviews/pointwise-typei6-review.md`): no FATAL/MAJOR; minors D1–D7 applied by the reviewer.
Builds on POINTWISE_TYPEI4.md (Prop 1.2, Cor 1.4, Lemma 3.1) and POINTWISE_TYPEI5.md (Lemma 1.1, Cor 1.2,
Lemmas 3.1–3.2, Prop 3.3, Thm 3.7). Notation as there: a fibre certificate of level `L` is

```
16·P·X² − Q·u² = 1,  u = 7^b,  P = c'P_1,  Q = 7^a Q_1,  P_1Q_1 = M := c_oδ² + T,  T = 2^{L−4},
c_o = 7^a c',  d = PQ = c_o M,  m := c'δ²,  y := c'gδ,  g := 4P_1X − 7^a uδ,
case B: j := Tu/2 − y > 0,  ρ := (Tu/2 + j)/P_1 ∈ ℤ,  λ := (ρj − m)/u ∈ ℤ,
σ := 8·7^a m j + 4Tj − T²u  (= Δ − 2Tj of TYPEI5),  κ := 8·7^a λ.
```

Regime (v) of TYPEI5 Prop 3.3 is `λ ≥ 1`, `σ ≥ 1`.

## 1. The gap parameters are norms (PROVED)

**Lemma 1.1 (PROVED; exact identities, all `L ≥ 5`, case B; valid for any positive integer `u` — not necessarily a power of 7 — and any solution of `16PX² − Qu² = 1` in the notation of (1.1); R99 repair D5, applied by reviewer).**
(a) `8j − μu = −32·c'δP_1X`, where `μ := 8c_oδ² + 4T`.
(b) `ω := 4j² − uσ = 4mP_1` (so `ω ≥ 4` always; this is the quadratic form `4j² − μju + T²u²` of discriminant `64δ²d`).
(c) `σ = 4λP_1 − 2Tj`. Hence **regime (v) ⟺ `2λP_1 > Tj` ⟺ `j² > mP_1`**, regime (iii) ⟺ `0 < 2λP_1 < Tj`.
(d) `j = uθ − δ√P/ζ` with `θ := (T/2)(√d − c_oδ)/(√d + c_oδ)` and `ζ := 4X√P + u√Q` (the certificate unit, `ζ² = ν_0`).
*Proof.* (a) `j = Tu/2 − c'δ(4P_1X − 7^auδ) = Tu/2 − 4c'δP_1X + 7^a m u`; multiply by 8 and subtract `μu`.
(b) `16ω = 64j² − 16μju + 16T²u²` (expand `σ`; note `8·7^am = 8c_oδ² = μ − 4T`) `= (8j − μu)² − (μ² − 16T²)u²`, and
`μ² − 16T² = 64c_oδ²(c_oδ² + T) = 64δ²d`. By (a), `16ω = 64δ²(16c'²P_1²X² − d u²) = 64δ²c'P_1(16PX² − Qu²) = 64δ²c'P_1`,
i.e. `ω = 4mP_1`. (c) `uσ = 4j² − 4mP_1` by (b); and `4j(ρP_1) − 4P_1(ρj − m) = 4mP_1` with `ρP_1 = Tu/2 + j`, i.e.
`4j² + 2Tuj − 4λuP_1 = 4mP_1`; comparing, `uσ = u(4λP_1 − 2Tj)`. The equivalences: `σ > 0 ⟺ 2λP_1 > Tj`, and by (b)
`σ > 0 ⟺ j² > mP_1`. (d) `ζ^{−1} = 4X√P − u√Q`, so `4PX = √P(u√Q + ζ^{−1})` and `c'g = 4PX − c_oδu = u(√d − c_oδ) + √P/ζ`; hence
`j = Tu/2 − δc'g = Tu/2 − uδ(√d − c_oδ) − δ√P/ζ`, and `δ(√d − c_oδ) = δc_oT/(√d + c_oδ)` gives
`T/2 − δ(√d − c_oδ) = (T/2)(√d − c_oδ)/(√d + c_oδ) = θ`. ∎

**Lemma 1.3 (PROVED; the system in the variables `(a, u, ρ, P_1, λ)`).** In case B,
`2·7^aT(Tρ + 2λ)u² − (8·7^aTρ²P_1 + κρP_1 + 4T²)u + P_1(8·7^aρ³P_1 + 6Tρ − 4λ) = 0`.
*Proof.* Substitute `j = ρP_1 − Tu/2`, `m = ρj − λu` into `4λP_1 = 8·7^amj + 6Tj − T²u` (Lemma 1.1(c)) and expand. ∎
In particular `u | P_1(8·7^aρ³P_1 + 6Tρ − 4λ)` — the mod-`u` shadow of the system (all of `j ≡ ρP_1`, `m ≡ ρ²P_1`
mod `u` follow from Lemma 3.1 of TYPEI5).

*Check.* `scripts/typei6_identities.py` verifies (a)–(d) (and Lemma 1.3 below) exactly / to 50 digits on all
29 relaxed solutions of `typei5_relax` (`L = 7` to `u ≤ 6001`; `L = 8, 9, 10` to `u ≤ 2001`; `L = 11, 12, 13` to `u ≤ 401`;
21 in case B).

*Remark 1.2 (regime (v) is genuinely inhabited above `L = 10`).* The `L = 13`, `b = 1` fibre certificate of TYPEI4 Comp 3.4,
`(c',g,δ,P_1,X) = (79,19,1,1,17)`, `u = 7`, has `j = 291`, `λ = 86582`, `σ = 48344`: it lies in **regime (v)**.
So no argument that closes regime (v) can be uniform in `L`; it must use `T ≤ 64` (as Lemma 3.6 / Prop 3.3(iv) of TYPEI5 do).

## 2. There is no polynomial unit in `δ`: the Richaud–Degert route is closed for `L ≥ 7` (PROVED)

Idea (1) of the brief: find the fundamental unit of `d(δ) = c_o²δ² + c_oT` as a polynomial in `δ` (Richaud–Degert /
Yokoi type) and solve `u_1 = 7^b` 7-adically. The following shows that no such polynomial unit exists.

**Proposition 2.1 (PROVED).** Fix `c_o` odd and `T = 2^{L−4}`, and put `η := c_oδ + √d`, so `N(η) = −c_oT`.
(a) The elements `x + y√d` with `x, y ∈ ℚ[δ]` (`δ` an indeterminate) and norm `1` are exactly `±ε_*^n`, `n ∈ ℤ`, where
`ε_* := η²/(c_oT) = (2c_oδ² + T + 2δ√d)/T`.
(b) If `L ≥ 7`, then for every odd integer `δ` and every `n ≠ 0`, `ε_*^n` is **not** an algebraic integer.
(c) (Schinzel 1961, cited) For `L ≥ 7`, the period length of the continued fraction of `√d(δ)` is unbounded along every
arithmetic progression `δ ≡ δ_0 (mod N)` (`δ_0` odd); for `L ≤ 6` it is bounded.
Hence for `L ≥ 7` the unit `ν_0` of a certificate is never given by a polynomial formula in `δ` on any
arithmetic progression of `δ` (at fixed `c_o`), and the same holds with the roles of `c_o` and `δ` exchanged
(at fixed `δ`, `d = δ²c_o² + Tc_o` is quadratic in `c_o`; by the same degree argument the units of `ℚ[c_o][√d]` are
`ℚ^×·ξ^ℤ` with `ξ := δc_o + T/(2δ) + √d`, `N(ξ) = T²/(4δ²)`, so the norm-1 ones are `±(2δξ/T)^n` and `2δξ/T = ε_*` is the
same element; (b) applies verbatim). Idea (1) cannot work as stated.
*Proof.* (a) In `ℚ((1/δ))`, `√d = c_oδ·(1 + T/(c_oδ²))^{1/2} = c_oδ + T/(2δ) + …`; the two embeddings `√d ↦ ±(this series)` of
`R := ℚ[δ][√d]` give two degree maps `deg_±`, additive on products, with `deg_+(ξ) + deg_−(ξ) = deg N(ξ)`. On the unit group
`R^×` (norms are nonzero constants) `deg_+` is a homomorphism to `ℤ`. Its kernel: if `deg_±(ξ) ≤ 0`, then
`x = (ξ + ξ')/2` is a polynomial of degree `≤ 0` and `y√d = (ξ − ξ')/2` has degree `≤ 0`, but `deg(y√d) = deg y + 1 ≥ 1`
unless `y = 0`; so the kernel is `ℚ^×`. `η` is a unit (`N(η) = −c_oT`) with `deg_+(η) = 1` (and `deg_−(η) = −1`), so the
image is `ℤ` and `R^× = ℚ^×·η^ℤ`. Finally `N(rη^k) = r²(−c_oT)^k = 1` forces `k = 2n` even (for odd `k` the right side
would be `r²·(negative)`), and `r = ±(c_oT)^{−n}`.
(b) `d ≡ 1 (mod 8)` (`L ≥ 7`), so `√d ∈ ℤ_2`; fix an embedding `K(√d) → ℚ_2`. Then `x_± := c_oδ ± √d ∈ ℤ_2` satisfy
`x_+ + x_− = 2c_oδ` (`v_2 = 1`) and `x_+x_− = −c_oT` (`v_2 = L − 4 ≥ 3`), so one of them has `v_2 = 1` and the other
`v_2 = L − 5`. Under the embedding where `v_2(η) = 1`, `v_2(ε_*^n) = n(2 − (L − 4)) = n(6 − L) < 0` for `n > 0`; under the
conjugate one it is `n(2(L−5) − (L−4)) = n(L − 6)`, `< 0` for `n < 0`. An algebraic integer has `v_2 ≥ 0` in every
embedding. ∎ (For `L = 5, 6`, `ε_*` is integral: `ε_* = c_oδ² + 1 + δ√d` resp. `(c_oδ² + 2 + δ√d)/2` with `d ≡ 5 (mod 8)`; this is the
Richaud–Degert case of TYPEI4 Remark 1.2(b). R99 repair D6, applied by reviewer: the earlier valuation bookkeeping does not apply at `L = 5`, where 2 ramifies.)
(c) Schinzel's criterion: for `f(t) = A²t² + Bt + C`, `Δ = B² − 4A²C ≠ 0`, the period of `√f(t)` is bounded iff
`Δ | 4·gcd(2A², B)²`. With `δ = δ_0 + Nt`: `A = c_oN`, `B = 2c_o²δ_0N`, `Δ = −4c_o³TN²`, `gcd(2A², B) = 2c_o²N·gcd(N, δ_0)`, and
the criterion reads `T | 4c_o·gcd(N,δ_0)²`, i.e. `T ≤ 4` (`c_o`, `δ_0` odd). ∎

*Check (EVIDENCE for (c)).* `scripts/typei6_period.py`: for `c_o ∈ {7, 21}`, odd `δ < 4002`, the maximal period is 2 (`L = 5`),
10 (`L = 6`), and 4610…60052, growing with `δ` (`L = 7, 8, 10`).

*Scope (Assessment).* Prop 2.1 excludes polynomial units along lines in the `(c_o, δ)`-plane. Along higher-degree curves
`(c_o(t), δ(t))` the polynomial `d(t)` has degree ≥ 4 and polynomial Pell solutions can exist for special curves; but they
would cover only thin subsets of the two-parameter family, so they could not close regime (v) by themselves.

## 3. Regime (v) is the "large unit" regime; under abc it is finite (PROVED / CONDITIONAL)

**Lemma 3.1 (PROVED).** In case B, with `θ`, `ζ`, `μ` as in Lemma 1.1,
`σ = 4uθ² − μδ√P/ζ` (exactly). Consequently in regime (v) (`σ ≥ 1`):
(a) `uX > 16c_o³δ⁷/T⁴`; (b) `c := 16PX² = Qu² + 1 > 64c_o³δ⁷√d/T⁴ ≥ 64c_o⁴δ⁸/T⁴`;
(c) asymptotically `u ≳ 8c_oδ³√P/T²` (`u` is at least of order `d^{1/2}·δ²√P/T²`); exactly, `u² > 64c_o³δ⁷P/(T⁴√d) − 1/Q`, i.e.
`u ≳ 8c_oδ³√P/(T²τ^{1/4})` with `τ := 1 + T/(c_oδ²)` (R99 repair D3, applied by reviewer).
*Proof.* `σ = μj − T²u` (as `8·7^am = μ − 4T`); insert `j = uθ − δ√P/ζ` (Lemma 1.1(d)) and use
`μθ − T² = T²ψ² = 4θ²`, `ψ := (√d − c_oδ)/(√d + c_oδ)`, `θ = Tψ/2`. Indeed `θ = T²c_o/(2(√d + c_oδ)²)` and
`c_oμ − 2(√d + c_oδ)² = 2(√d − c_oδ)²` (both sides expand with `(√d ± c_oδ)² = 2c_o²δ² + c_oT ± 2c_oδ√d`), so
`μθ − T² = T²(c_oμ − 2(√d + c_oδ)²)/(2(√d + c_oδ)²) = T²ψ²`.
(a) `σ > 0` gives `4uθ²ζ > μδ√P`; use `θ < T²/(8c_oδ²)` (as `(√d + c_oδ)² > 4c_o²δ²`), `ζ < 8X√P` (as `u√Q < 4X√P`),
`μ > 8c_oδ²`. (b) `u < 4X√(P/Q)` and (a) give `X² > 4c_o³δ⁷√(Q/P)/T⁴ = 4c_o³δ⁷Q/(T⁴√d)`; multiply by `16P`, `PQ = d`.
(c) from (b) with `c ≈ 4Qu²`. ∎
(Checked numerically: the identity to 40 digits and (a), (b) on all relaxed regime-(v) rows, `scripts/typei6_identities.py`.)

*Interpretation.* By (b) the certificate unit `ν_0 = A + 8Xu√d` satisfies `ν_0 > A = 2c − 1 > 128c_o⁴δ⁸/T⁴ − 1 ≈ 128d²δ⁴/T⁴` (R99 repair D2, applied by reviewer); regimes (ii)/(iii) are the units
below this size. Regime (v) is therefore **not a degenerate corner but the generic case** (a typical fundamental unit has
size `exp(≍√d)`); closing it unconditionally means showing that `u_1(d)` (TYPEI5 Cor 1.2) is never a power of 7 for the
large-unit fields of the family — a statement about the fundamental units of a two-parameter family of real quadratic
fields, of the same kind as "the Pell `y`-coefficient is never a prime power", for which no unconditional method is known
(Assessment).

**Theorem 3.2 (CONDITIONAL on abc).** Suppose `c < K·rad(abc)^{1+ε}` for all coprime `a + b = c` (fixed `0 < ε < 1/7`,
`K = K_ε`). Then every fibre certificate of level `L` in regime (v) satisfies
`δ^{2−6ε}·7^{a(1−3ε)}·P^{(1−7ε)/2} < K·(3.5τ)^{1+ε}·(T²/8)^{1−ε}`, `τ := 1 + T/(c_oδ²)`.
In particular, **under abc there are only finitely many fibre certificates of each level `L`** (all regimes), and their
number and size are bounded in terms of `(K_ε, ε, L)`.
*Proof.* Apply abc to `1 + Qu² = 16PX² = c`: `rad = rad(2·7·Q_1PX) ≤ 14PXQ_1` (`u = 7^b`, `Q = 7^aQ_1`), and
`X = √(c/16P)`, `PQ_1 = d/7^a` give `rad ≤ (7/2)(d/7^a)√(c/P)`. Hence `c^{(1−ε)/2} < K(3.5d/7^a)^{1+ε}P^{−(1+ε)/2}`.
Insert Lemma 3.1(b), `c > 64c_o⁴δ⁸/T⁴`, and `d = c_o²δ²τ`: `(8/T²)^{1−ε}c_o^{2−2ε}δ^{4−4ε} < K(3.5τ)^{1+ε}c_o^{2+2ε}δ^{2+2ε}·
7^{−a(1+ε)}P^{−(1+ε)/2}`; finally `c_o^{4ε} = 7^{4aε}c'^{4ε} ≤ 7^{4aε}P^{4ε}`. The bound fixes `δ`, `a`, `P ≥ c'`,
hence `c_o` and `d`, to a finite set; each `d` has finitely many splittings `PQ` and each carries at most one `b`
(TYPEI5 Lemma 1.1). Regimes (i)–(iv) are finite at each `L` unconditionally (TYPEI5 Prop 3.3). Case A is finite at each `L` unconditionally
(TYPEI5 Lemma 3.6 covers only `L ≤ 10`; general `L`, R99 repair D1, applied by reviewer): `P_1 = c'g² + 2·7^auJ ≤ ρP_1 = Tu/2 − J`
gives `J < T/(4·7^a)`, `ρ < T/(4·7^aJ)`; with `G := c'g`, `G | Tu/2 + J` and `4G | 1 + 7^auρ` give `G | 7^aρJ − T/2 ≠ 0`, so `G < T`;
then `c'g² = u(T/(2ρ) − 2·7^aJ) − J/ρ ≤ G²` with the bracket `≥ 1/(2ρ)`, so `u ≤ 2ρ(G² + J) < T³`. ∎

*Remarks.* (i) The abc input is exactly the 7-power: for general `u` the radical is `≍ c` and nothing follows; abc turns
"`u = 7^b`" into "`u ≪ d^{1/2+O(ε)}/7^a`" (small unit), contradicting Lemma 3.1(c).
(ii) Effectivity: in the idealised limit `ε → 0`, `K = 1` (a heuristic idealisation, not a form of abc: `1 + 8 = 9` violates `c < rad`; R99 repair D4, applied by reviewer), the bound reads `49^aδ⁴P < 49T⁴τ²/256`, which forces
`c_oδ ≤ 7^aPδ < 7T⁴τ²/256 ≤ 4.6·10⁵τ²` even at `L = 10` (`δ = 1`, `a = 1` is the worst case), and either `τ ≤ 1.2` or
`c_oδ ≤ c_oδ² < 5T`; so `c_oδ < 6.7·10⁵` — inside Cor 2.3 of TYPEI5 (`c_oδ ≤ 10⁶`, all `b`),
so levels 7–10 would be empty. With any *published* explicit abc conjecture (these are conjectures, not results; Baker 2004: `c < (6/5)N(log N)^ω/ω!`; or `c < N^{7/4}`)
the constant is far too large (or the exponent `> 8/7`), so **emptiness of levels 7–10 is not obtained conditionally on
any standard explicit abc** (Assessment). Theorem 3.2 is a finiteness statement only.
(iii) Theorem 3.2 does not touch sterility of `x̂_9` (unbounded `L`).

## 4. A per-`b` engine for regime (v) from the size condition (CERTIFIED once replayed)

Lemma 3.1(b) turns regime (v) into a *lower* bound on the unit, i.e. an *upper* bound on the field for fixed `b`:
`Qu² + 1 > 64c_o⁴δ⁸/T⁴` with `Q = d/P` gives

```
P·(64c_o⁴δ⁸ − T⁴) < u²·d·T⁴,     d = c_o(c_oδ² + T),  P = c'P_1,  u = 7^b,                          (4.1)
```

so `49^a c'³δ⁶P_1 ≲ u²T⁴/64`. The number of `(a, c', δ)` is `≍ (u²T⁴)^{1/3}`, far below the `≍ T·7^b·(divisors)` of the
TYPEI4 Cor 3.2 search, and every candidate needs only a divisor `P_1 | M` below the bound (4.1).

**Computation 4.1.** `scripts/typei6_vsearch.c L b [u]`: for all odd `a`, odd `δ`, odd `c'` with `7 ∤ c'`, all divisors
`P_1 | M = c_oδ² + T` satisfying (4.1) (evaluated in long double with relative margin `10⁻⁹`; vacuous when
`64c_o⁴δ⁸ ≤ T⁴`), tests exactly (GMP) whether `(Qu² + 1)/(16P) = X²` with `X` odd, `7 ∤ X`. `M` is factored completely by a
sieve along the arithmetic progression `c' ↦ M` while the bound on `P_1` is `≥ 64`, otherwise `P_1` runs over all odd
numbers below the bound. By Lemma 3.1(b) and Prop 1.2 of TYPEI4 the output contains **every regime-(v) fibre certificate
of level `L` with `v_7(k) = b`** (it may contain other solutions of (1.1) satisfying (4.1); none occurred).
*Regression / positive controls.*
* Complete lists of `typei4_lb` for `L = 11…18`, `b ≤ 3` (10 certificates): the 5 lying in regime (v) (`(L,b) = (13,1)`,
  `(16,0)×3`, `(18,1)`) are all found, and nothing else (`scripts/typei6_regress.py`).
* Relaxed mode (`u` an arbitrary odd number instead of `7^b`): it recovers every regime-(v) relaxed solution of
  `typei5_relax` (`L = 7`, `u = 293`; `L = 9`, `u = 1853`; `L = 10`, `u = 293`; `L = 12`, `u = 27, 37`; `L = 13`, `u = 7, 29`)
  — positive controls **at the levels 7, 9, 10 themselves**.

**Result of Computation 4.1** (`L = 7, 8, 9, 10`; times on one core):

| L | b = 0…13 | b = 14 | b = 15 | solutions | heuristic expectation (Σ, b ≤ 15) |
|---|---|---|---|---|---|
| 7 | 67 s | 178 s | 636 s | 0 | 1.3·10⁻⁴ |
| 8 | 126 s | 318 s | 1282 s | 0 | 2.9·10⁻⁴ |
| 9 | 391 s | 742 s | 2876 s | 0 | 1.2·10⁻² |
| 10 | 864 s | 2441 s | 9660 s | 0 | 1.9·10⁻⁵ |

(Largest case: `L = 10`, `b = 15`: 5.5·10⁹ candidate divisors, 2644 pass the `16P`-divisibility test, 0 squares. Full stderr log:
`reviews/agent-reports/O99_vsearch_log.txt`; a first run with the pre-heuristic binary gave the same 0 counts for `b ≤ 13`.)

**Corollary 4.2 (CERTIFIED once replayed; extends TYPEI5 Thm 3.7).** There is no fibre certificate — hence no certificate
at `x̂_9` — of level `L ∈ {7, 8, 9, 10}` with `v_7(k) ≤ 15`, at any height and for any `v_7(c)`. *Proof.* Case A and regimes (ii), (iii), (iv) are excluded for all `b` (TYPEI5
Lemma 3.6, Comp 3.4, Prop 3.3(iv)); regime (v) for `b ≤ 15` by Comp 4.1 (the overlap `b ≤ 9` agrees with the TYPEI4/TYPEI5 engines). ∎
*Provenance (R99 repair D7, applied by reviewer).* Review R99 re-ran regime (v) with an independent from-scratch engine
(`scripts/review_typei6_vsearch.c`: exact GMP size test, different factoring and enumeration) for `L = 7, 8, 9, 10`,
`b = 0…13`: 0 solutions, with the same candidate counts as Comp 4.1 (one extra, slack-admitted, candidate on the author's side at
`L = 9`, `b = 12`). It also checked completeness against R92's size-free relaxed brute force (all odd `u ≤ 20001/10001/6001/4001`
at `L = 7/8/9/10`): exactly the 5 regime-(v) relaxed solutions `(L,u) = (7,293), (8,9883), (9,1853), (9,4003), (10,293)` are found
and nothing else. R99 also ran `(L,b) = (7,14), (7,15), (8,14), (8,15), (9,14)`: 0 solutions, same candidate counts. So everything in Cor 4.2 is
confirmed by two engines except `(L,b) = (9,15), (10,14), (10,15)`, which rest on Comp 4.1 alone.
So a certificate at `x̂_9` of level 7–10 needs `v_7(k) ≥ 16` and `c_oδ > 10⁶` and, by Lemma 3.1(c), `7^{v_7(k)} ≳ 8c_oδ³√P/T²`.

## 5. Heuristic size of what remains (EVIDENCE / Assessment)

`typei6_vsearch` also accumulates, over the candidates passing the `16P`-divisibility test, the naive probability
`1/(2√Y)` that `Y = (Qu²+1)/(16P)` is a square ("heuristic expectation", stderr; no local corrections).
*Calibration* on levels where certificates exist (`L = 11…20`, `b ≤ 3`, regime (v)): predicted 4.4, actual 7
(per level: 0.03/0, 0.005/0, 0.43/1, 0.05/0, 0.47/0, 0.66/3, 0.55/0, 0.16/1, 0.44/0, 1.63/2) — right order of magnitude.
*At `L = 7, 8, 9, 10`* the predicted numbers of regime-(v) certificates with `b ≤ 15` are `1.3·10⁻⁴`, `2.9·10⁻⁴`,
`1.2·10⁻²`, `1.9·10⁻⁵` (dominated by `b ≤ 5`), and the per-`b` prediction decays by a factor ≈ 3–15 per step
(`b = 15`: `9.2·10⁻¹³`, `1.1·10⁻¹²`, `7.0·10⁻¹³`, `6.0·10⁻¹³`), so the tail `b ≥ 16` is predicted `< 10⁻¹¹`.
So the model predicts that levels 7–10 are empty, and that a certificate, if any, would have to be a structured
(non-random) solution; Prop 2.1 excludes the simplest structured source (a unit polynomial in `δ` or in `c_o`).
This is EVIDENCE only.

## 6. What remains open (precise statement)

Regime (v) at `L ∈ {7,…,10}` is closed for `v_7(k) ≤ 15` (Cor 4.2), for `c_oδ ≤ 10⁶` (TYPEI5 Cor 2.3), and
CONDITIONALLY on abc up to a finite set (Thm 3.2). What remains is exactly: *fields `d = c_o(c_oδ² + T)` with
`c_oδ > 10⁶` whose certificate unit has `u_1(d) = 7^b`, `b ≥ 16`*, which by Lemma 3.1 are large-unit fields
(`ν_0 ≳ 128c_o⁴δ⁸/T⁴`). Prop 2.1 shows the Richaud–Degert route is closed for `L ≥ 7`; Remark 1.2 shows regime (v) is
inhabited at `L = 13`, so any closing argument must use `T ≤ 64`. An unconditional closure would require controlling
the fundamental units of a two-parameter family of real quadratic fields (Assessment: beyond current methods; the
abc conjecture with small explicit constant would suffice, Thm 3.2 Remark (ii)).

## Replay

```
uv run --with mpmath python scripts/typei6_identities.py <typei5_relax outputs>   # Lemmas 1.1, 1.3, 3.1
gcc -O2 -o /tmp/relax scripts/typei5_relax.c   # /tmp/relax 7 1 6001; 8..10: 1 2001; 11..13: 1 401
uv run python scripts/typei6_period.py                                             # Prop 2.1(c) evidence
gcc -O2 -o /tmp/vsearch scripts/typei6_vsearch.c -lgmp -lm
gcc -O2 -o /tmp/lb scripts/typei4_lb.c -lm
for L in 11 12 13 14 15 16 17 18; do for b in 0 1 2 3; do /tmp/lb $L $b >> lb.txt; /tmp/vsearch $L $b >> vs.txt; done; done
uv run python scripts/typei6_regress.py lb.txt vs.txt                              # 5/5 regime-(v) found
for x in "7 293" "9 1853" "10 293" "12 27" "12 37" "13 29" "13 7"; do set -- $x; /tmp/vsearch $1 0 $2; done   # relaxed controls
for L in 7 8 9 10; do for b in $(seq 0 15); do /tmp/vsearch $L $b; done; done        # Comp 4.1: 0 solutions
```
