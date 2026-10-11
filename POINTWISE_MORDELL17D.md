# POINTWISE_MORDELL17D — the r = 17 P-count: no-go quantified, rational points, pointwise certification (task O139)

Status: O139 (branch `side-agent/r17-sterile`), in progress, unreviewed. Builds on POINTWISE_MORDELL17.md (= M17),
POINTWISE_MORDELL17B.md (= M17B), POINTWISE_MORDELL17C.md (= M17C) and their reviews. Labels as in DISCOVERIES.md.
Notation as in M17: cell `C_5 = {u ∈ ℤ_17^× : u ≡ 5 (17)}`; a P-datum of level `L` is an N-point `(a,b,c,d)` of
`Σ^II_N`, `N = 17^K`, `K = 2L−1`, `17 ∤ cd` (both orders of `(a,b)`), with box `−f (mod 17^L)`, `f = 4acd−1`;
a Q-datum of level `k` is an N-point of `Σ^I_F`, `F = 17^k` (k odd), `17 ∤ e`, with boxes `−4a²d`, `−4b²d (mod F)`.
By M17B Lemma 1.1 the union of all boxes of the seven ET families meeting `C_5` is the union of the P- and Q-boxes.
Throughout `W = 17^L`, so `W² = 17N`.

## 0. Outcome in one paragraph

No unconditional sterile point. §1 quantifies, exactly, how far an explicit ET-type count is from closing the
cell-wide measure criterion (Assessment, with an exact computation): even an explicit `D_P(K) ≤ 11·17^{0.4K}` with no
log factor would need exact data through K = 19; with one log factor through K = 35. §2 (PROVED) treats a single
*rational* point `u`: membership in a box of level `L` becomes a lattice condition `qa − pb = zW`, the resonant part
`z = 0` (rays) is excluded for `u = −2/3` at every level by congruences, `u = 5` has no rays at all, and covering data
with `z ≠ 0` are forced into thin, explicitly enumerable families. §3 uses this for a pointwise certification far
beyond the cell-wide range. §4 states the sharpened conditional theorem with its exact remaining gap.

## 1. The cell-wide measure route: compactness and the quantitative no-go

**Lemma 1.1 (compactness; PROVED).** `C_5` contains a sterile point iff for every `L` the boxes of level `≤ L` do not
cover `C_5`. *Proof.* The set of points of `C_5` in no box of level `≤ L` is clopen (a finite union of boxes is
clopen); these sets decrease in `L`; a decreasing sequence of nonempty compact sets has nonempty intersection, and a
point of the intersection lies in no box. The converse is trivial. ∎
So the measure criterion (M17 Thm 4.1, M17B Thm 4.1, M17C Lemma 1.1) is a sufficient, not a necessary, condition: any
argument showing that each finite level leaves a gap suffices. The measure bound is just the only uniform tool we have.

**Computation 1.2 (how C* grows with the exact range; arithmetic).** If the cumulative hypothesis (H_P^cum) of M17C
Lemma 1.1 is only required for `K ≥ K₀` (all data with `K < K₀` exact and the base still `ρ ≥ ρ₂ = 961421/1419857`),
the admissible constant is `C*(K₀) = (ρ − T_Q)/(2·(16/17)·Σ_{K≥K₀ odd} 17^{θK+(1−K)/2})`, i.e. it grows by
`17^{1−2θ}` per two steps of `K` (factor 1.76 at θ = 0.4). `scripts/m17d_nogo.py` (part a):

| K₀ | 15 | 17 | 19 | 21 | 23 | 25 | 27 | 29 | 31 |
|---|---|---|---|---|---|---|---|---|---|
| θ = 0.35 | 29.25 | 68.44 | 160.1 | 374.6 | 876.4 | 2050 | 4797 | 1.12·10⁴ | 2.63·10⁴ |
| θ = 0.40 | 2.64 | 4.652 | 8.199 | 14.45 | 25.46 | 44.88 | 79.09 | 139.4 | 245.6 |
| θ = 0.45 | 0.1798 | 0.2387 | 0.3169 | 0.4207 | 0.5586 | 0.7415 | 0.9844 | 1.307 | 1.735 |

(K₀ = 15 reproduces M17C's row 3.) Exact enumeration of all P-data costs `≍ 17^{0.4K}` factorisations (M17B §2: K = 13
took 1.5 h); K = 15 is within reach (est. ≈ 15 h on 2 cores), K = 17 is not. So raising the cell-wide `N₀` by
enumeration buys at most one more column.

**Computation 1.3 (explicit ET-type bounds would need exact data far beyond reach; Assessment on top of exact
arithmetic).** Suppose an explicit bound `D_P(K) ≤ A·17^{θK}·(K ln 17)^B` were proved for all `K ≥ K₀`. The least odd
`K₀` for which M17B Thm 4.1 then applies (`T_P + T_Q < ρ₂`, pointwise form, base ρ₂ kept although it would shrink) is
(`m17d_nogo.py` part b):

| (θ, B) \ A | 1 | 11 | 44 | 1000 |
|---|---|---|---|---|
| (0.40, 0) | 15 | 21 | 27 | 37 |
| (0.40, 1) | 29 | 37 | 43 | 55 |
| (0.40, 2) | 47 | 57 | 63 | 75 |
| (0.45, 1) | 65 | 85 | 95 | 119 |
| (0.45, 2) | 111 | 129 | 141 | 165 |

Interpretation (Assessment). ET's cover (M17B Lemma 2.1) has three pair regimes, each with `≥ X ln X` parameter pairs
(`X = N^{2/5}`) and at least one divisor-in-class count per pair (Lenstra's constant 11 where it applies), plus an
`e`-regime whose best conceivable explicit bound is a short-interval `τ₃` average `≫ X (ln N)²` (M17C §3). So the most
optimistic explicit outcome of that method is around `(θ,B,A) = (0.4, 1–2, ≥ 11)`, which needs exact data through
`K ≈ 37–57` (`N ≈ 10^{46}–10^{70}`), against the reachable `K ≤ 15`. Larger θ makes it worse, not better, because the
weight `17^{−K/2}` then decays only like `17^{−(1/2−θ)K}`. **The cell-wide measure route needs a bound on `D_P` with
essentially no logarithmic loss and constant ≲ 1.5 at θ = 0.4. That is stronger than ET's theorem (`N^{2/5+o(1)}`, with
non-explicit `o(1)`), and no known method gives it.** This makes the qualitative remarks of M17C §3 quantitative. It is
not a theorem about all methods.

## 2. A single rational point: lattice form, rays, thin families (PROVED)

Fix `u = −p/q ∈ C_5` with `p, q ∈ ℤ`, `q ≥ 1`, `gcd(p,q) = 1`, `17 ∤ pq`. For the cell `C_7` use `1/u` (M17 Lemma 1.1).

**Lemma 2.1 (membership = a lattice condition).** (i) *P.* `u` lies in the box `−f (mod W)` of a P-datum `(a,b,c,d)`
of level `L` iff `17 ∤ b` and `qa ≡ pb (mod W)`. (ii) *Q.* `u` lies in the box `−4a²d (mod F)` of a Q-datum of level
`k` iff `qa ≡ pb (mod F)`, iff `4a²d ≡ p/q (mod F)`. (The second box of a datum is the first box of the reflected datum
`(b,a,c,d)`, which is again a datum; so "all boxes" = "first boxes of all data, both orders".)
*Proof.* (i) If `17 | b`, then `4abcd = a+b+Nc` gives `17 | a`, so `f ≡ −1` and the box is `≡ 1 (mod 17)`, outside
`C_5`. Otherwise `bf = cN + a ≡ a (mod W)` (ET (2.20); `2L−1 ≥ L`), so `−f ≡ −a/b`, and `−a/b ≡ −p/q ⟺ qa ≡ pb`.
(ii) `4abd = eF + 1` (M17C Lemma 2.1(i)) gives `17 ∤ ab` and `4a²d ≡ a/b (mod F)`. ∎

Write `qa − pb = zW` (P) resp. `= zF` (Q), `z ∈ ℤ`.

**Lemma 2.2 (sizes).** (i) Every N-point of `Σ^II_N` has `4ab ≤ N + a + b`, i.e. `(4a−1)(4b−1) ≤ 4N+1`.
(ii) Every N-point of `Σ^I_F` with `a ≤ b` has `acd ≤ (F+1)/2`; in particular `ad ≤ (F+1)/2`.
(iii) If `z ≠ 0`, then `max(a,b) ≥ W/(|p|+q)` (P) resp. `≥ F/(|p|+q)` (Q).
*Proof.* (i) `4abd = N + e`, `1 ≤ e ≤ a+b`, `d ≥ 1`. (ii) Dividing `4abcd = F(a+b)+c` by `4b`:
`acd = F/4 + Fa/(4b) + c/(4b) ≤ F/2 + 1/2`, as `c ≤ a+b ≤ 2b`. (iii) `W ≤ |qa − pb| ≤ (|p|+q)·max(a,b)`. ∎
So for `z ≠ 0` a covering P-datum is *unbalanced*: `min(a,b) ≤ (|p|+q)(N+a+b)/(4W) ≈ (|p|+q)·W/68`, whereas a typical
P-datum has `a, b` anywhere in `ab ≤ N/2`.

**Lemma 2.3 (rays).** `z = 0` means `(a,b) = λ(p,q)`, `λ ≥ 1`; this needs `p > 0`, i.e. `u < 0`.
(i) For `u > 0` (e.g. `u = 5`) there are no rays.
(ii) For `u = −2/3` no P-datum and no Q-datum of any level lies on the ray. So `−2/3` lies in a box of level `L` only
through data with `z ≠ 0`.
*Proof of (ii).* P: `(a,b) = (2λ,3λ)`, `e | a+b = 5λ`, `24λ²d = N + e`. If a prime `ℓ ≠ 5` divides `e`, then `ℓ | λ`,
so `ℓ | N + e`, so `ℓ | N`, `ℓ = 17`, so `17 | λ`, excluded by Lemma 2.1(i). Hence `e = 5^j ≡ 1, 5 (mod 8)`. But
`8 | 24λ²` and `N = 17^K ≡ 1 (mod 8)` force `e ≡ −1 (mod 8)`. Q: `24λ²d = eF + 1`, `e | 5λ`; a prime `ℓ ≠ 5`
dividing `e` divides `λ` and hence `1`; so `e = 5^j`, while `eF + 1 ≡ e + 1 ≡ 0 (mod 8)`. ∎
Rays are the *resonant* part: a ray datum has centre exactly `u`, so a single one covers `u` at all higher precision of
its level. Rational points with an admissible ray are covered (e.g. `−9/5`, `−11/8`, `11/9` are covered at level 2,
`−7/2` at level 5; `scripts/m17d_points.py`). Lemma 2.3 is what makes `−2/3` a good candidate.

**Remark 2.4 (descent identity; PROVED, not used below).** For every N-point of `Σ^II_N`, `N = W²/17`, and every
`p, q` with `qa − pb = zW`: `e·[c(p²b + q²a) + 17z²] = ab·[(p+q)² + 68dz²]`. (Expand: the difference is
`(a+b)(p²b+q²a) − ab(p+q)² − 17z²·4abd + 17ez² = (qa−pb)² − 17z²N = 0`.) If moreover `qa ≡ pb (mod W)` with `z ∈ ℤ`, the
bracket on the left is divisible by `ab` (it equals `ab·(p²f* + q²f − 2pq)/N` with `f* = 4bcd−1`, and
`f | 4c²dp² + 17x²`, `x = (qf−p)/W`), so `e | (p+q)² + 68dz²`. For `z = 0` this is `e | (p+q)²`, the ray constraint.
