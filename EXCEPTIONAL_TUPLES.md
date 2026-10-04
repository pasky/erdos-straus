# EXCEPTIONAL_TUPLES — the tuple-count / witness-correlation door (task O21)

Status: **work in progress (O21).** Labels follow `DISCOVERIES.md`. PROVED
means proved in this file (internal checks only, not refereed). No θ > 3/4
is claimed unconditionally. ES is not solved.

Notation: `ET` = `EXCEPTIONAL_THETA.md`, `NC` = `EXCEPTIONAL_NONCRT.md`,
`K2` = `EXCEPTIONAL_KARY2.md`, `IF` = `EXCEPTIONAL_INTERFREQ.md` (branch
`side-agent/interfreq`), `ElT` = Elsholtz–Tao arXiv:1107.1010.
`E(N) = #{n ≤ N : 4/n = 1/x+1/y+1/z has no solution in positive integers}`.

## 1. Witness correlations of order k

### 1.1 Definitions

A *witness family* 𝒲 is a finite set of residue classes `W = (b_W mod d_W)`
such that every positive integer in W has an ES solution. The basic
example: for `M ≡ 3 (mod 4)`, `A = (M+1)/4`, the classes of

    𝓡(M) = {−4D mod M : D | A²}                     (notes Lemma 18.1)

are forced (notes Lemma 16.1: no condition on n beyond n ≥ 1). Hence for
every witness family

    E(N) ≤ #{n ≤ N : f_𝒲(n) = 0},    f_𝒲(n) := Σ_{W∈𝒲} 1_W(n).     (1.1)

**Definition 1.1 (k-point witness correlation).** For `T ⊆ 𝒲` put

    C_T(N) = #{n ≤ N : n ∈ W for all W ∈ T},
    δ_T    = density in ℤ of ∩_{W∈T} W  (= 0, or 1/lcm_{W∈T} d_W by CRT),
    E_T(N) = C_T(N) − N δ_T.

The *order-k correlation sum* and its *CRT prediction* are

    S_k(N) = Σ_{|T|=k} C_T(N) = Σ_{n≤N} binom(f_𝒲(n), k),
    m_k    = Σ_{|T|=k} δ_T    = E_CRT binom(f_𝒲, k),                 (1.2)

where E_CRT is the uniform average over one common period. T is *above
modulus N* if `δ_T > 0` and `lcm_T d_W > N`; then `C_T(N) ∈ {0,1}` while
`Nδ_T < 1`.

**Lemma 1.2 (termwise bound; PROVED, trivial).** `|E_T(N)| ≤ 1` for every T,
hence `|S_k(N) − N m_k| ≤ #{T : |T| = k, δ_T > 0}`.

*Proof.* A nonempty ∩_T W is one class mod `q = lcm_T d_W`, and
`|#{n ≤ N : n ≡ b (q)} − N/q| ≤ 1`. ∎

The **tuple-count door** (IF §3.3, NC §6 (c′)) is the hope that
`Σ_T c_T E_T(N)` is far smaller than `Σ_T |c_T|` for the coefficients `c_T`
of some majorant, in a range where most of the CRT mass sits on T above
modulus N. Order-k correlation sums are the simplest such sums
(`c_T = 1` on `|T| = k`).

### 1.2 The prime family and its shift form

Let `𝒫_y = {ℓ prime : ℓ ≤ y, ℓ ≡ 3 (mod 4)}`, `F(ℓ) = |𝓡(ℓ)|`,
`p_ℓ = F(ℓ)/ℓ`, and the *prime family* `𝒲_y = {classes of 𝓡(ℓ) : ℓ ∈ 𝒫_y}`.
Classes with the same ℓ are disjoint, so

    f_y(n) := f_{𝒲_y}(n) = Σ_{ℓ∈𝒫_y} x_ℓ(n),   x_ℓ(n) = 1[n mod ℓ ∈ 𝓡(ℓ)],

and under E_CRT the `x_ℓ` are independent `Bern(p_ℓ)`. Hence
`m_k = e_k(p) := Σ_{|S|=k, S⊆𝒫_y} Π_{ℓ∈S} p_ℓ`, `P_CRT(f_y = 0) = Π(1−p_ℓ)`,
and the CRT mass `μ_y := Σ_{ℓ∈𝒫_y} p_ℓ` satisfies (notes Lemma 24.3)

    c(log y)² ≤ μ_y ≤ C(log y)²   (y ≥ 3).                           (1.3)

**Lemma 1.3 (shift form; PROVED).** For each ℓ ∈ 𝒫_y fix a set 𝒟_ℓ of
divisors of `A_ℓ² = ((ℓ+1)/4)²` whose residues `−4D mod ℓ` are exactly
𝓡(ℓ), each once. For `D ≥ 1` let `𝒫_y(D) = {ℓ ∈ 𝒫_y : D ∈ 𝒟_ℓ}` and
`ω_{y,D}(m) = #{ℓ ∈ 𝒫_y(D) : ℓ | m}`. Then for every n ∈ ℤ

    f_y(n) = Σ_{D ≥ 1} ω_{y,D}(n + 4D),                               (1.4)

and the order-k correlation sum is the k-point correlation of these
truncated additive functions at the shifts `4D`:

    S_k(N) = Σ_{{(ℓ_1,D_1),…,(ℓ_k,D_k)}} #{n ≤ N : ℓ_i | n + 4D_i, i ≤ k},   (1.5)

summed over k-sets with distinct `ℓ_i ∈ 𝒫_y` and `D_i ∈ 𝒟_{ℓ_i}`. All
shifts satisfy `4D < y²/4`.

*Proof.* The classes `−4D`, `D ∈ 𝒟_ℓ`, are distinct mod ℓ, so
`x_ℓ(n) = Σ_{D∈𝒟_ℓ} 1[ℓ | n + 4D]`. Summing over ℓ and regrouping by D
gives (1.4). Expanding `binom(f_y(n), k)` as the number of k-sets of hit
primes, each hit prime ℓ with its unique D, gives (1.5). Finally
`D ≤ A_ℓ² < (y+1)²/16`. ∎

So **ES witness correlations of order k are k-point correlations of
ω-type (divisor-indicator) functions along k shifts**, with each prime
`ℓ_i` small (`≤ y`) and combined modulus `Π ℓ_i`. When all `D_i` are equal
this is a single integer `n + 4D` divisible by `Π ℓ_i`; then
`Πℓ_i ≤ N + 4D`, and the count is the Kubilius-model situation (§4). The
door concerns *distinct* shifts with `Π ℓ_i ≫ N`.

## 2. A conditional implication: order-K correlations ⇒ saving ≍ K

**Hypothesis TC(N; K, y, η)** (order-K witness correlations of the prime
family). For every `1 ≤ j ≤ K`,

    | Σ_{n≤N} binom(f_y(n), j) − N e_j(p) | ≤ η N.                     (2.1)

(2.1) asserts the CRT prediction for the order-j correlation sums *in
aggregate*. It does not assert anything about an individual `C_T(N)`.

**Theorem 2.1 (PROVED).** If K is even and TC(N; K, y, η) holds, then

    #{n ≤ N : f_y(n) = 0} ≤ N ( Π_{ℓ∈𝒫_y}(1 − p_ℓ) + e_K(p) + Kη ).

*Proof.* For an integer `f ≥ 1`, `Σ_{j=0}^K (−1)^j binom(f,j) =
(−1)^K binom(f−1,K)` (induction on K via Pascal's rule); for `f = 0` the
sum is 1. With K even the sum is therefore `≥ 1[f = 0]` for every `f ≥ 0`.
Put `f = f_y(n)` and sum over `n ≤ N`: since `S_0 = N = N e_0`,

    #{f_y = 0} ≤ Σ_{j=0}^K (−1)^j S_j(N) ≤ N Σ_{j=0}^K (−1)^j e_j(p) + KηN.

Under the CRT law the same identity gives
`Σ_j (−1)^j e_j(p) = P(f=0) + E[1_{f≥1} binom(f−1,K)] ≤ Π(1−p_ℓ) + E binom(f,K)
= Π(1−p_ℓ) + e_K(p)`. ∎

**Corollary 2.2 (PROVED).** Let `K ≥ 2` be even and let `y_K` be the
largest y with `μ_y ≤ K/e²`. If TC(N; K, y_K, e^{−K}) holds, then

    E(N) ≤ (K + 4) N e^{−K/e²}.

Moreover `log y_K ≍ K^{1/2}` by (1.3).

*Proof.* `0 ∉ 𝓡(ℓ)` (since `(D, ℓ) = 1` for `D | A²`), so `p_ℓ < 1`, and
`μ_{y_K} > K/e² − 1`. Hence `Π(1−p_ℓ) ≤ e^{−μ} < e^{1−K/e²}`, and
`e_K(p) ≤ μ^K/K! ≤ (eμ/K)^K ≤ e^{−K}`. Insert in Theorem 2.1 and (1.1). ∎

**Corollary 2.3 (CONDITIONAL on TC_θ).** For θ ∈ (0,1) let *TC_θ* be the
statement: for all large N, TC(N; K_N, y_{K_N}, e^{−K_N}) holds with
`K_N = 2⌈(log N)^θ⌉`. Under TC_θ,

    E(N) ≤ N exp(−(2/e² − o(1)) (log N)^θ).

In particular **TC_θ for some θ > 3/4 implies the θ > 3/4 target.** ∎

**Proposition 2.4 (the trivial range; PROVED).** TC(N; K, y, η) holds with
`η = (Σ_{ℓ∈𝒫_y} F(ℓ))^K / N` whenever `Σ_ℓ F(ℓ) ≥ 1`. Consequently
TC(N; K, y_K, e^{−K}) holds unconditionally for `K ≤ c₀(log N)^{2/3}`, and
Corollary 2.2 gives `E(N) ≪ N exp(−c(log N)^{2/3})`.

*Proof.* By Lemma 1.2, `|S_j − N e_j(p)| ≤ #{j-sets of classes with
distinct primes} = e_j(F) ≤ (ΣF)^j/j! ≤ (ΣF)^K`. By (1.3),
`Σ_{ℓ≤y}F(ℓ) ≤ y μ_y ≤ C y (log y)²`, and `(log y_K)² ≤ K/(ce²)`. So
`(ΣF)^K ≤ N e^{−K}` as soon as `K(C₁K^{1/2} + log C + 2 log K + 1) ≤ log N`,
which holds for `K ≤ c₀(log N)^{2/3}`. ∎

This is Brun's pure sieve; it recovers the 2/3 exponent (without the
`(log log N)^{1/3}` of DISCOVERIES (A)6). It calibrates the framework:
TC is a *theorem* exactly as long as the order-K tuples have total
"termwise" error `≤ N e^{−K}`, i.e. `K log y_K ≲ log N`, and its content
for θ > 2/3 is aggregate cancellation among tuples above modulus N.

**Remarks.**
1. *Where TC_θ lives.* The tuples carrying `e_K(p)` have
   `log Π ℓ_i ≈ K·⟨log ℓ⟩_p ≍ K log y_K ≍ K^{3/2} = (log N)^{3θ/2}` (the
   p-weighted mean of log ℓ over `𝒫_y` is `≍ log y` by (1.3)). For
   θ > 3/4 the combined moduli are `exp((log N)^{9/8+})`: super-polynomial
   in N, though each `ℓ_i ≤ y_K = N^{o(1)}` and each shift `4D_i < y_K²`.
   (Assessment; §5 checks the split numerically.)
2. *Precision.* `e_j(p)` peaks near `j ≈ μ ≈ K/e²` at size `≈ e^{μ}`. So
   (2.1) with `η = e^{−K}` asks for relative precision `≈ e^{−(1+e^{−2})K}`
   in the peak moments: `N^{−o(1)}`, far weaker than a power saving, but
   for growing order K. The alternating sum cancels from `e^{μ}` to `e^{−μ}`.
3. *Composite moduli.* With all moduli `M ≤ y` (cubic mass, notes Thm
   18.2) the trivial range becomes `K ≲ (log N)^{3/4}`: the 3/4 note's
   architecture (Bonferroni degree ≍ saving, atoms of size
   `exp(s^{1/3})`). We use the prime family because CRT independence makes
   Theorem 2.1 exact. Nothing below needs composite moduli.
