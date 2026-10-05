# Hostile review R27b — EXCEPTIONAL_LARGESIEVE2.md §§8–9 (checkpoint 3 of O27)

Reviewer: side agent `review-ls2b`. Scope: §§8–9 only (Lemma 8.1, Props 8.2,
8.4, Lemma 8.3, Thm 8.5 + Consequences, Thm 9.1, Prop 9.2, §9 Status).
Reviewed at `side-agent/ls-escapes` @ 519aab5. From-scratch scripts:
`scripts/review_ls2b_*.py`. (Work in progress; verdict table filled in as
checks complete.)

## Verdicts

| claim | verdict |
|---|---|
| Lemma 8.1 | SOUND |
| Prop 8.2(a) | SOUND |
| Prop 8.2(b) | SOUND-AFTER-REPAIRS (m1: needs `\ell'_i \ge 36`) |
| Lemma 8.3 | (pending) |
| Prop 8.4 | (pending) |
| Thm 8.5 | (pending) |
| Thm 8.5 Consequences 1–3 | (pending) |
| Thm 9.1 | (pending) |
| Prop 9.2 | (pending) |
| §9 Status / "Open precisely" | (pending) |

## Line-by-line notes

**Lemma 8.1.** Re-derived. Gale/Hall for a transportation problem with
equal totals (1 = 1): feasible iff `|R|/ℓ ≤ |N(R)|/ℓ'` for all row sets R ✓.
C(R) = columns y with `β(y) ∈ ∩_{α∈α(R)}(B − α)`. Two arcs `B−α₁, B−α₂`
(open, length 2η, centres at circular distance ≥ 2η) are disjoint ✓. If all
pairwise distances are < 2η ≤ 1/4, α(R) lies in an arc of length < 2η (all
points lie within 2η < 1/2 of any one of them, so the configuration is
“linear” and has diameter < 2η) — the doc says “otherwise α(R) lies in an
arc of length < 2η” without this one-line justification (trivial, noted
only). Point counts `≤ 2ηℓ+1`, `≤ 2ηℓ'+1` ✓; `4η + 1/ℓ + 1/ℓ' ≤ 1/2 + 2/5 < 1` ✓.
CRT phase decomposition `na/D ≡ nau/ℓ + nav/ℓ'` with `uℓ'+vℓ = 1` ✓.
*From scratch* (`review_ls2b_gale.py`): direct transportation-LP
feasibility (not via the author's reduction) for all pairs of primes in
[5,47], 6 random a each, both orders, η ∈ {1/8,1/9,1/10,1/20}: 3744 cases,
0 failures. A scan of η upward finds the first infeasible case only at
η ≈ 0.36 (ℓ,ℓ' = 5,7), so the hypothesis η ≤ 1/8 has a large margin.

## Defects

**Prop 8.2(a).** Re-derived. Level is W-rough level over *distinct* primes,
so a modulus of level `≤ λ < L_i` is not divisible by both `ℓ_i, ℓ'_i`
(prime powers do not help it) ✓. μ = ⊗μ_i on the digits mod `D_i`, other
digits (incl. higher powers of `ℓ_i`, W-smooth part, foreign primes)
uniform and independent: the law of `n mod d` is then uniform for every
allowed d ✓, so `E_μ = E_U` on `V_𝒟` and `E_Uν = E_μν ≥ 1` ✓. μ itself is a
comparison measure with S = 0 directly (no LP duality or K2 input needed;
the band family is not a K2 mixture, and the doc rightly does not invoke
K2 Thm 5.1 here) ✓.
*From scratch* (`review_ls2b_lp.py`): K = 2 band families
(`Q = 5005`, three prime pairings × 3 random `(a₁,a₂)`, η = 1/8), exact LP
for the best majorant in the span of class indicators mod
`{ℓ_1ℓ_2, ℓ_1ℓ'_2, ℓ'_1ℓ_2, ℓ'_1ℓ'_2}` (the maximal allowed moduli): value
**1.000000** in all 9 cases, although the density of 𝒜 is ≈ 0.56–0.58.
Control: allowing `D_1` drops the LP value to 0.74–0.77, so the LP is
not trivially stuck at 1.

**Prop 8.2(b).** Re-derived against EK §1–2 (Thm 2.5, Cor 2.6, Lemma 2.1).
Averaging over non-band digits keeps `ν ≥ 0`, `ν ≥ 1` on 𝒜 (𝒜 depends
only on band digits) and the mean ✓; a term of level `≤ λ` contains
`< d` band primes when all exceed `e^{λ/d}` ✓ (so "at most d" holds with
room). Patterns are the binary pairs with top `ℓ'_i`; at `ℓ_i` the
activated set is empty ✓. Light: `p_{ℓ'_i} ≤ (2ηℓ'_i+1)/ℓ'_i = 2η + 1/ℓ'_i`,
and with η = 1/9 this is `≤ 1/4` **only if `ℓ'_i ≥ 36`** — not among the
stated hypotheses (`ℓ > max(W, e^{λ/d})`); it holds if `W ≥ 36`, which is
true for K2's `W₀` but is never said (defect m1). Then all tops light,
σ ⊂ 𝒜 a.s. (EK Lemma 2.1(1)), `M ≤ K/4` pathwise, Cor 2.6 with
`m̄ = K/4`, and Jensen `E e^{−Φ} ≥ e^{−EΦ}` give exactly the stated bound ✓.
Note (b) is not used by Thm 8.5.

**Lemma 8.3.** Re-derived. Fejér: `F_R(z) = (R+1)^{−1}(sin π(R+1)z/sin πz)² ≤
1/(4(R+1)z²)` from `sin πz ≥ 2z` ✓. For `t ∈ J`, `‖t − 1/2‖ ≥ η` so the
distance to supp I is `≥ η/2` ✓; `G(t) ≤ η·max F ≤ 1/((R+1)η) < η/4` as
`R ≥ 4/η²` ✓. `∫P² = (1+η/4)² − 2(1+η/4)η + ∫G²`; the doc drops the
`−η²/2` term (harmless) ✓; `1 − η/2 + η²/16 ≤ 1 − η/3` for η ≤ 8/3 ✓.
*From scratch* (`review_ls2b_ls.py`): P built from its Fourier coefficients
`c_m = (1+η/4)δ_{m0} − Î(m)(1 − |m|/(R+1))`; on a 2·10⁵-point grid
min_J P = 1.029 / 1.026 / 1.012 and Σc_m² = 0.926 / 0.935 / 0.973 for
η = 1/8, 1/9, 1/20 (claimed ≤ 0.958, 0.963, 0.983) ✓. P > 0 everywhere
(min ≈ η/4 + small), so the product g of Prop 8.4 is ≥ 0 and ≥ 1 on 𝒜.

**Prop 8.4.** Re-derived. Balanced base-(2R+1) digits: `{Σm_iβ_i}` =
`Ξ^{−1}{−(Ξ−1)/2,…,(Ξ−1)/2}`, spacing `1/Ξ` also across 0 ≡ 1 ✓;
perturbation `≤ KRε = 1/(4Ξ)` per point gives spacing `≥ 1/(2Ξ)` ✓. Window
for `a_i`: length `2εD_i ≥ 8` ✓; ≤ 2 of 4 consecutive integers are killed by
ℓ, ℓ' ≥ 5 ✓. `m_i a_i/D_i` with `|m_i| ≤ R < ℓ_i` keeps denominator `D_i`, so
every nonzero frequency has denominator `Π_{i∈T}D_i` ✓. MV with
`N − 1 + δ^{−1} ≤ N + 2N/3` ✓; LS axioms: `w = 3/(5N) ≤ 1/N` (Fact 1.1),
`Σw ≤ (N/3)·3/(5N) = 1/5 ≤ 1` (Fact 4.0) ✓. Dual: `g = Π_iP(nθ_i)`,
`Σ|γ|² = (Σ|c_m|²)^K` (distinct points) ✓. CRT-admissibility (LS §1
definition, `L ≤ F_w(π)` for **every** π ∈ P(𝒜)): for any such π,
`1 ≤ E_πg = Σγ_θπ̂(θ) ≤ (Σ|γ|²/w)^{1/2}F_w(π)^{1/2}`, so
`L = w/Σ|γ|²` is admissible ✓ — the bound uses residues only, not the
short interval. (Equivalently g itself is a nonnegative majorant of 𝒜 of
mean `c₀^K < 1` at level `Σ L_i`: the escape is a pure level phenomenon.)
*From scratch*: K = 1, 2 instances with η = 1/9, R = 324, `N = 3Ξ`, primes
just above `(16KRN)^{1/2}` (D_i ≈ 1.3·10¹⁰ for K = 2): coprime `a_i`
found in the ε-window, min gap·Ξ = 0.9999 (claim ≥ 1/2), `|𝒜∩[1,N]|` =
1515 / 764 902 below the bounds 3035 / 1 842 358, and `g ≥ 1.026` /
`1.053` on 2000 sampled points of 𝒜 ✓. (At K ≤ 2 the bound exceeds N, as
expected; a positive saving needs K ≥ 14, i.e. `N ≥ 3·649¹⁴ ≈ 10^{39.8}`.)

**Thm 8.5.** Quantifiers re-checked. Order: λ ≥ 1 and N ≥ N₀ arbitrary,
then the family (K, R, η fixed functions of N; primes depending on λ, N, W).
N₀ is absolute (needs K ≥ 14 for a positive saving, and `−o(1)` absorbs
`⌊·⌋` and `log(5/3)`); c = 1/(27 log 649) = 0.00572 is absolute ✓;
`(1−1/27)^K ≤ e^{−K/27}` ✓. Bullet 1 needs `L_i > λ` ✓ (`ℓ,ℓ' > e^{λ/2}`);
bullet 2 needs `D_i ≥ 16KRΞ` ✓ (`ℓ,ℓ' > (16KRN)^{1/2}`), and every nonzero
frequency has level `≥ min L_i > λ` ✓. Both bullets concern the **same**
family; the LS bound is CRT-admissible in the exact LS §1 sense (not a
short-interval artefact), and the comparison side is the full LP optimum
(Prop 8.2(a): `E_Uν ≥ 1` for every level-λ majorant). So the escape is
genuine: no argument whose only inputs are "a comparison measure at level
λ" + Facts 1.1/4.0 + duality can cap CRT-admissible large sieves whose
frequencies have level > λ. Density remark: exponent
`log(9/7)/log 649 = 0.0388` ✓, `0.00572` ✓.

**Thm 8.5 Consequences.** (1) ✓: `E_πP(nθ_i) = Σ_m c_mπ̂(mθ_i) ≥ 1`,
`c₀ = ∫P ≤ (∫P²)^{1/2} < 1`, so some `0 < |m| ≤ R` has
`|π̂(mθ_i)| ≥ (1−c₀)/Σ_{m≠0}|c_m|`; `mθ_i` has denominator `D_i` (as
`R < ℓ_i`), level `L_i`; Prop 5.2 needs (a) at level `2λ'`, so `λ' < L_i/2`
and (b) is violated at level `L_i > λ'` ✓. (2) The (Sp) sentence is stated
as a fact "by the divisor bounds of K2 §3", but K2 §3 proves only *total*
first moments `𝔐(y) ≪ (log y)³…`; the per-D restricted sum is not written
anywhere, and "for every D … ≤ D^{−1+o(1)}" is false as literally read for
small D (the `(log N)^{O(1)}` factor is not `D^{o(1)}` when D is bounded).
It is only needed for D of level `> λ ≥ log N`, where it is plausible
(defect m2). (3) labelled Assessment ✓.

**Thm 9.1.** Re-derived. Prefix `q°`: the prefix before the last step is
`< N`, hence level `≤ log N`; the last step adds one prime `≤ e^{Λ₀}` (level
counts distinct primes once) ✓; a W-smooth part `≥ N` gives level 0 ✓.
`coll_q ≤ max_b π(b mod q) ≤ max_b π(b mod q°) ≤ e^S/q°` (q° | q, q° ∈ 𝒟) ✓.
𝒮_<: `|H_c|²` is a real combination of class indicators mod
`lcm(q,q')`, `q,q' ∈ 𝒮_<`, level `≤ 2log N` ✓; Lemma 4.1 for `K_< ≤ K`
(pointwise, w ≥ 0) with the same h ✓. Summation: the 𝒮_≥ part is
`≤ e^S W_≥/N`, the 𝒮_< part `≤ D_u^< + e^S(h + W_</N)`, total
`≤ D_u + e^S(h + W_K/N)` ✓ (the doc's write-up "w̃^<_θ ≤ h + W_</N" then
"W_K" is right only because `W_< + W_≥ = W_K`; fine). Final algebra:
`2W_K − h = 2(W_K−h) + h` and `h ≤ Nh` ✓. The case `D(π) ≤ h` makes
the kernel bound void ✓.
*From scratch* (`review_ls2b_kernel.py`): the proof uses only (1.1) for
the given π, so I tested the inequality chain for **arbitrary** A ⊂ ℤ/13860
and arbitrary π on A, with S computed exactly by LP as the best constant
in (1.1) over the 𝒟 of the proof, and random kernels (moduli | 13860,
some ≥ N, N ∈ {6,…,40}): 23 nontrivial trials, all satisfy both
`D(π) − h ≤ (W_K−h)/N + e^S(h + W_K/N)` and the stated B-bound (min slack
ratio 4.4). ✓
*Hypothesis bookkeeping:* "no hypothesis on the levels of the kernel
moduli" is true, but the theorem does need every **prime** of the kernel
moduli to be `≤ e^{Λ₀}` (§9 preamble), and λ grows with Λ₀; the summary
table omits this (defect m3). Remark (not a defect; possible
strengthening): kernel primes not dividing `M₀` can be removed from the
hypothesis — 𝒜 is invariant under those digits, so the LP-dual π may be
averaged to be uniform on them, and then `π(b mod q) = π(b mod q_{M₀})/(q/q_{M₀})`.

**Prop 9.2.** Re-derived. T-rough q avoids the base; `n mod ℓ^v` is a
function of `y_ℓ` (or a uniform lift), so EK Lemma 2.1(2) gives
`q·σ(b mod q) ≤ Π_{ℓ|q}(1−ℓ^{−1/2})^{−1} ≤ e^{2ω(q)T^{−1/2}} ≤ e^{2T^{−1/4}}` ✓;
`1+χ²_q = qΣσ(b)² ≤ q·max σ(b)` ✓. Conditioning: `1+χ²(π) ≤ (1+χ²(σ))(1−𝔏)^{−2}`,
`(1−x)^{−2} ≤ 1+4x` on `[0,1/4]` ✓; `𝔏 ≤ C(log T)^cT^{−1/4}` is Thm 4.3's
W-uniform estimate with W = T ✓ (T ≥ W₀). `X ≤ ε_T D_u`, LS Lemma 6.1 and
LS Thm 6.2 (checked against LS §6) give the stated bound ✓. Unconditional
as claimed (no K2 Thm 5.1) ✓.

**§9 Status / "Open precisely".** Band-family remark: correct
conclusion, but the stated route ("once every `L_i > 2log N + Λ₀`, e.g.
ℓ ∈ [N³,2N³]") only works if Λ₀ (which bounds the *kernel* primes too)
is ≈ 3 log N, i.e. it silently restricts the kernels to primes ≤ 2N³.
For "every kernel with h = 0" one should argue directly: `𝒮_< = ∅`, each
`q°` contains no prime ≥ N before its last step, hence at most one band
prime, so `μ` of Prop 8.2(a) (uniform on foreign digits) has
`μ(b mod q°) = 1/q°` and `B ≥ N` (defect m4). "Open precisely" omits
(i) Prop 9.2's hypothesis `ω(q) ≤ T^{1/4}` (T-rough kernels with
`ω(q) > T^{1/4}` are covered by neither 9.1 nor 9.2 when the factor is
large), (ii) that the closed side rests on K2 Thm 5.1/KARY3 (conditional)
and on family primes `≤ N^{O(1)}` (defect m5).
