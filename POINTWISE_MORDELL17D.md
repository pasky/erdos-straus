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

## 3. Pointwise certification (CERTIFIED, two engines vs. the certified lists)

**Algorithm 3.1 (P, level L; complete by Lemmas 2.1(i), 2.2(i)).** `scripts/m17d_pointP.c L s t AB` lists every N-point
`(a,b,c,d)` of `Σ^II_{17^{2L−1}}`, in both orders, with `17 ∤ bcd` and `a ≡ −u·b (mod W)`, `u = s/t`. Part A: `a ≤ A`
(`A ≈ W/√68`), `b ≡ −a/u (mod W)`, all `b` with `(4a−1)(4b−1) ≤ 4N+1`. Part B: `b ≤ B := ⌊(⌊(4N+1)/(4A+3)⌋+1)/4⌋`,
`a ≡ −ub`, `a > A`; a pair with `a > A` has `4b − 1 ≤ (4N+1)/(4A+3)`, so the two parts cover all pairs. Each pair is
tested exactly (`e = (−N mod 4ab)`, `1 ≤ e ≤ a+b`, `e | a+b`, `c = (a+b)/e`, `d = (N+e)/4ab`, `17 ∤ cd`; equation and
box membership rechecked in 128-bit). Work `≈ 0.24W + (W/34) ln(0.12W)` candidates; `L = 8`: 3.9·10⁹ candidates, 23 s.
(Cell-wide enumeration needs `≍ 17^{0.4K} = 17^{0.8L−0.4}` *factorisations*. That is asymptotically fewer operations,
but in practice the pointwise test reaches two to three levels further, since it needs no factoring.)

**Algorithm 3.2 (Q, level k; complete by Lemmas 2.1(ii), 2.2(ii)).** `scripts/m17d_pointQ.c k s t` lists every
N-point of `Σ^I_F` with `a ≤ b`, `17 ∤ e` and `4a²d ≡ w (mod F)`, `w ∈ {−u, −1/u}` (the second value accounts for the
reflected box). As `ad ≤ (F+1)/2`, `min(a,d) ≤ √((F+1)/2)`: for small `a`, `d` is the least residue of `w/(4a²)`;
for small `d`, `a` runs over the two square roots of `w/(4d) mod F` (Hensel). Each pair `(a,d)` has at most two data
(M17C Lemma 2.1(iv)): `f` is the least residue of `−F (mod 4ad)`, or `t/f` is the least residue of `t·(−F)^{−1}`,
`t = 4a²d+1`. Work `O(√F)` modular square roots; `k = 13` takes seconds, `k = 15` minutes.

**Validation 3.3.** `scripts/m17d_validate.py` runs both engines at every level `≤ 7` on (i) every in-cell box centre
(`C_5 ∪ C_7`) of the certified lists (all centres for levels ≤ 5, 20 per level at 6–7) and (ii) 20 random in-cell
units per level, and requires *equality* of the output with the set of listed data (P: `data/m17b/p{K}.txt`, both
orders, from two independent engines, M17B Comp. 2.2) resp. listed boxes (Q: `m17_enum`, R83-confirmed). Result:
**704 test points, 0 mismatches.** Remark 2.4's identity and divisibility were checked on all 6632 (datum, order)
pairs of `p1–p13` (0 failures).

**Computation 3.4 (CERTIFIED by Algorithms 3.1–3.2, validated as in 3.3).** For `u = 5` and for `u = −2/3`:
no P-datum of level `L ≤ L_P*` and no Q-datum of level `k ≤ 15` has a box containing `u`.
Candidates tested (P, both points): L = 8: 3.9·10⁹ / 4.2·10⁹; L = 9: 7.6·10¹⁰ / 8.1·10¹⁰ (8 min each); L = 10: 1.44·10¹² / 1.53·10¹² (≈ 3.3 h each).
Q pairs `(a,d)` reaching the divisor test: 6, 26, 29, 51 (`u = 5`) and 34, 11, 22, 28 (`u = −2/3`) at k = 9, 11, 13, 15.
`L_P* = 10`. Hence, as U ⊂ P, Q⁻¹ = Q and √Q = ∅ (M17B Lemma 1.1): **`5` and `−2/3`
lie in no box of any of the seven ET families of level ≤ 10** (and in no Q-box of level ≤ 15). By inversion the same
holds for `1/5`, `−3/2 ∈ C_7`. The cell-wide certified range is level 7 (M17B Comp. 3.1).

## 4. The sharpened conditional statement

**Theorem 4.1 (localized measure criterion; PROVED).** Let `u₀ ∈ C_5` lie in no box of level `≤ L*`, and
`R = u₀ + 17^{L*}ℤ_17`. For `ℓ > L*` let `NB^R(ℓ)` be the number of distinct boxes of level `ℓ` contained in `R`
(P-boxes of level `ℓ = (K+1)/2`, one per datum and order, and Q-boxes of level `ℓ = k`). If
`Σ_{ℓ > L*} 17^{L*−ℓ}·NB^R(ℓ) < 1`, then `R` contains a sterile point. Hence (M17 Cor. 4.2) no finite set of ET
Prop. 1.9 classes covers all sufficiently large primes `p ≡ 1 (24)` with `(p/17) = −1`, `(p/q) = 1` for `q = 5,7,11,13`.
*Proof.* A box of level `≤ L*` meeting `R` contains `R` (ultrametric balls of larger or equal radius), hence `u₀`; there
is none. A box of level `> L*` meeting `R` lies in `R`. By M17B Lemma 1.1 all boxes meeting `C_5` are P- or Q-boxes. The
union of the boxes of level `> L*` inside `R` has measure `≤ Σ 17^{−ℓ}NB^R(ℓ) < 17^{−L*} = μ(R)`. ∎

Fair-share normalisation: `R` is the fraction `17^{1−L*}` of `C_5`. Consider
`(H_θ^R)`: `NB_P^R(K) ≤ C·17^{θK}·17^{1−L*}` for odd `K ≥ 2L*+1`, and `NB_Q^R(k) ≤ 2·17^{3k/5}·17^{1−L*}` for odd `k > L*`.
Under it the criterion reads `C·Σ_{K≥2L*+1 odd} 17^{θK+(1−K)/2} + T_Q^R < 1`. Admissible C (box units, floor-rounded,
`scripts/m17d_local_tail.py`); the first row is the global M17B criterion in the same units (`NB_P(K) ≤ C·17^{θK}`,
K ≥ 15, base ρ₂; it equals 2× the D-unit constants of M17B/M17C):

| criterion | θ = 0.30 | 0.35 | **0.40** | 0.45 |
|---|---|---|---|---|
| global, K ≥ 15 (ρ₂) | 545.9 | 55.06 | **4.969** | 0.3385 |
| local, L* = 9 (K ≥ 19) | 7792 | 445.9 | **22.83** | 0.8827 |
| local, L* = 10 (K ≥ 21) | 2.42·10⁴ | 1043 | **40.24** | 1.171 |

**What this does and does not change (Assessment).** (a) The pointwise route raises the exact range around a chosen point
by 2–3 levels for the cost of minutes to hours, which no cell-wide enumeration can do. The admissible constant at θ = 0.4
grows ×4.6 (L* = 9) resp. ×8.1 (L* = 10). (b) The price is a different hypothesis: `(H_θ^R)` asks that P-centres not
*concentrate* in `R` (at most C times the fair share), which is neither implied by nor implies (H_P). In the random
discrete-log model of M17 §6 both hold with enormous margins. (c) No counting method of §1 proves either: proving
`(H_θ^R)` needs the same `N^{2/5}`-without-log-loss count, now restricted to a residue class mod `17^{L*}`, i.e.
additionally an equidistribution statement. So **the outcome stays CONDITIONAL**. The exact remaining gap is a bound
on the number of P-boxes (ES solutions of `4/17^K` of type II, `17 ∤ cd`) whose centre `−a/b` falls in a fixed class
mod `17^{L*}`: `≤ 40.24·17^{0.4K}·17^{1−L*}` for all odd `K ≥ 21` (L* = 10), plus the Q analogue with margin.

**Conjecture 4.2 (CONJECTURE).** `u = 5` and `u = −2/3` are sterile. EVIDENCE: Computation 3.4; for `−2/3`, the
resonant ray families are excluded at every level (Lemma 2.3, PROVED), and `5` has none. In the random model the expected
number of boxes of level > 10 containing a fixed point is `≈ Σ_{ℓ>10} NB(ℓ)·17^{1−ℓ} ≈ 10⁻⁸` (extrapolating the M17B
increments 7.0·10⁻⁵, 1.1·10⁻⁵ at levels 6, 7, or the `2K³` model), so Computation 3.4 is consistency evidence rather than strong evidence. A proof for a fixed rational point
would have to exclude the `z ≠ 0` families of Lemma 2.2, which have no congruence obstruction visible: modulo any `m`
prime to 17 the condition `qa − pb = zW` is void, as `z` is free (Assessment).

## Replay

```
W=<worktree>; mkdir -p /tmp/o139 && cd /tmp/o139
python3 $W/scripts/m17d_nogo.py                                   # §1 tables (< 1 s)
gcc -O2 -o m17_enum $W/scripts/m17_enum.c
for m in Q U; do for k in 1 3 5; do ./m17_enum $m $k | sort -u > $m$k.txt; done; cp $W/data/m17b/qu7_o93/${m}7.txt .; done
cp $W/data/m17b/p*.txt .
python3 $W/scripts/m17d_points.py . 13 7 12                       # small-height rationals: covered / uncovered (§2)
gcc -O2 -o pointP $W/scripts/m17d_pointP.c; gcc -O2 -o pointQ $W/scripts/m17d_pointQ.c
python3 $W/scripts/m17d_validate.py . . 7 7 20                    # Validation 3.3: 704 points, 0 mismatches (1 min)
for u in "5 1" "-2 3"; do for k in 9 11 13 15; do ./pointQ $k $u; done; for L in 8 9 10; do ./pointP $L $u AB; done; done
#   Comp. 3.4: hits=0 everywhere; P L=9 8 min, L=10 ~3.3 h per point (parts A, B can run separately)
python3 $W/scripts/m17d_local_tail.py 9 10                        # §4 table
```
