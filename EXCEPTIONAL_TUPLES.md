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
largest y with `μ_y ≤ K/e²`, and `η_K := e^{−K/e²}/K`. If
TC(N; K, y_K, η_K) holds, then

    E(N) ≤ (e + 2) N e^{−K/e²}.

Moreover `log y_K ≍ K^{1/2}` by (1.3).

*Proof.* `0 ∉ 𝓡(ℓ)` (since `(D, ℓ) = 1` for `D | A²`), so `p_ℓ < 1`, and
`μ_{y_K} > K/e² − 1`. Hence `Π(1−p_ℓ) ≤ e^{−μ} < e^{1−K/e²}`, and
`e_K(p) ≤ μ^K/K! ≤ (eμ/K)^K ≤ e^{−K}`, and `Kη_K = e^{−K/e²}`. Insert in
Theorem 2.1 and (1.1). ∎

**Corollary 2.3 (CONDITIONAL on TC_θ).** For θ ∈ (0,1) let *TC_θ* be the
statement: for all large N, TC(N; K_N, y_{K_N}, η_{K_N}) holds with
`K_N = 2⌈(log N)^θ⌉`. Under TC_θ,

    E(N) ≤ N exp(−(2/e² − o(1)) (log N)^θ).

In particular **TC_θ for some θ > 3/4 implies the θ > 3/4 target.** ∎

**Proposition 2.4 (the trivial range; PROVED).** TC(N; K, y, η) holds with
`η = (Σ_{ℓ∈𝒫_y} F(ℓ))^K / N` whenever `Σ_ℓ F(ℓ) ≥ 1`. Consequently
TC(N; K, y_K, η_K) holds unconditionally for `K ≤ c₀(log N)^{2/3}`, and
Corollary 2.2 gives `E(N) ≪ N exp(−c(log N)^{2/3})`.

*Proof.* By Lemma 1.2, `|S_j − N e_j(p)| ≤ #{j-sets of classes with
distinct primes} = e_j(F) ≤ (ΣF)^j/j! ≤ (ΣF)^K`. By (1.3),
`Σ_{ℓ≤y}F(ℓ) ≤ y μ_y ≤ C y (log y)²`, and `(log y_K)² ≤ K/(ce²)`. So
`(ΣF)^K ≤ N η_K` as soon as `K(C₁K^{1/2} + log C + 2 log K + 1) ≤ log N`,
which holds for `K ≤ c₀(log N)^{2/3}`. ∎

This is Brun's pure sieve; it recovers the 2/3 exponent (without the
`(log log N)^{1/3}` of DISCOVERIES (A)6). It calibrates the framework:
TC is a *theorem* exactly as long as the order-K tuples have total
"termwise" error `≤ N η_K`, i.e. `K log y_K ≲ log N`, and its content
for θ > 2/3 is aggregate cancellation among tuples above modulus N.

**Remarks.**
1. *Where TC_θ lives.* The tuples carrying `e_K(p)` have
   `log Π ℓ_i ≈ K·⟨log ℓ⟩_p ≍ K log y_K ≍ K^{3/2} = (log N)^{3θ/2}` (the
   p-weighted mean of log ℓ over `𝒫_y` is `≍ log y` by (1.3)). For
   θ > 3/4 the combined moduli are `exp((log N)^{9/8+})`: super-polynomial
   in N, though each `ℓ_i ≤ y_K = N^{o(1)}` and each shift `4D_i < y_K²`.
   (Assessment; §5 checks the split numerically.)
2. *Precision.* `e_j(p)` peaks near `j ≈ μ ≈ K/e²` at size `≈ e^{μ}`. So
   (2.1) with `η = η_K` asks for relative precision `≈ e^{−2K/e²}/K`
   in the peak moments: `N^{−o(1)}`, far weaker than a power saving, but
   for growing order K. The alternating sum cancels from `e^{μ}` to `e^{−μ}`.
3. *Composite moduli.* With all moduli `M ≤ y` (cubic mass, notes Thm
   18.2) the trivial range becomes `K ≲ (log N)^{3/4}`: the 3/4 note's
   architecture (Bonferroni degree ≍ saving, atoms of size
   `exp(s^{1/3})`). We use the prime family because CRT independence makes
   Theorem 2.1 exact. Nothing below needs composite moduli.

## 3. No-go: correlation input of order k saves at most ≍ k log log N

Theorem 2.1 used order K and saved `≍ K`. This section shows that this is
optimal up to `log log N`, even if all information below modulus
`N^{O(1)}` is used as well, as long as the hypotheses assert CRT main
terms. Bounded order k is useless for θ > 3/4.

Setting: a prime-slice system (ET §1: small modulus Q₀, admissible set R,
finite slice-prime set 𝒫, forbidden sets `F_ℓ(c)`), with
`p_ℓ(c) ≤ 1/4` and `|F_ℓ(c)| < ℓ` for all `ℓ ∈ 𝒫`, `c ∈ R`. A *majorant*
is `ν = Σ_i a_i 1[n ≡ b_i (mod d_i)]` with `ν ≥ 0` on ℤ and `ν ≥ 1` on the
whole avoider set 𝒜. Put `T_i = {ℓ ∈ 𝒫 : ℓ | d_i}`.

**Definition 3.0.** ν is *(λ₀, k)-mixed* if every term i satisfies
`Σ_{ℓ∈T_i} log ℓ ≤ λ₀` (level ≤ λ₀) **or** `|T_i| ≤ k` (order ≤ k).

Examples. A k-point correlation `1[n ∈ W_1 ∩ … ∩ W_k]` of slice classes
has order ≤ k, whatever its modulus. So `P∘f` with `deg P ≤ k`, Bonferroni
truncations of degree k, Theorem 2.1's majorant (K = k), and any of these
plus an arbitrary CRT majorant of level ≤ λ₀ are (λ₀, k)-mixed.

**Theorem 3.1 (PROVED).** Let ν be (λ₀, k)-mixed, `k ≥ 1`. Let `L₀ > 0`,
weights `s_ℓ = min(log ℓ, L₀)`, `s_* = min_𝒫 s_ℓ`, `λ = max(λ₀, kL₀) ≥ s_*`,
`G = ⌊log₂(λ/s_*)⌋ + 1`, `μ̄ = Σ_{ℓ∈𝒫} p̄_ℓ`. For every α > 0,

    log(1/Eν) ≤ log(Q₀/|R|) + 19αλ
                + C₄ [ Σ_{ℓ∈𝒫, log ℓ≤L₀} p̄_ℓ ℓ^{−α} + e^{−αL₀} Σ_{ℓ∈𝒫, log ℓ>L₀} p̄_ℓ ]
                + G(75 + log(2+λ/s_*)) + (G/2) log(16μ̄+16).          (3.1)

*Proof.* ET Theorem 2.5's proof, with ET Proposition 2.4 applied to the
weights `s_ℓ` instead of `log ℓ` (Prop 2.4 allows arbitrary weights
`s_i ≥ s_* > 0`; NC Thm 2.3 does the same with other weights). Condition
on `c = n mod Q₀ ∈ R`. The hit indicators `x_ℓ`, ℓ ∈ 𝒫, are independent
`Bern(p_ℓ(c))`, and `ν_c = E[ν | c, x]` is a sum of terms depending on
`x_{T_i}` only. Each term has weighted level
`Σ_{T_i} s_ℓ ≤ min(Σ_{T_i} log ℓ, |T_i| L₀) ≤ λ`, by the mixed condition.
So `ν_c` is λ-level for these weights, `ν_c ≥ 0`, and `ν_c(0) ≥ 1` (the
event `{c} × {x = 0}` lies in 𝒜 and has positive probability). All
`s_ℓ ≤ L₀ ≤ λ`, so Prop 2.4 needs `p_ℓ(c) ≤ 1/4` for all ℓ ∈ 𝒫, which is
assumed, and its mass is μ̄ (averaged). Prop 2.4 gives (2.3) in each
fibre with `Σ p_ℓ(c) e^{−αs_ℓ}`. The weights do not depend on c, so the
fibre bound is affine in `(p_ℓ(c))_ℓ` up to the concave log term; average
over c ∈ R by Jensen exactly as in ET Thm 2.5, and use
`Eν ≥ (|R|/Q₀) avg_{c∈R} Eν_c`. Finally `e^{−αs_ℓ}` is `ℓ^{−α}` if
`log ℓ ≤ L₀` and `e^{−αL₀}` otherwise. ∎

**Corollary 3.2 (ES prime-slice families; PROVED).** Take a family as in
ET Corollary 3.4 (forced classes of notes Lemma 16.1 or ET Lemma 3.2, or
Case-A classes via ET Lemma 3.7; moduli `q₀ℓ`, `q₀ ≤ ℓ^C`, C < 1;
selector R with parameter P; `ℓ ≥ ℓ₀(C)`), with all slice primes
`ℓ ≤ N^A`. Every (A log N, k)-mixed majorant ν, `1 ≤ k`, satisfies

    log(1/Eν) ≤ C₉(A,C) [ (log N)^{3/4} + k log log N ] + log(P/φ(P)).   (3.2)

*Proof.* ET Cor 3.4's proof gives `p_ℓ⁺ ≤ 1/4`,
`log(Q₀/|R|) ≤ log(P/φ(P))` after the selector average, and the mass
bound `Σ_ℓ p̄_ℓ ℓ^{−β} ≤ C min(β,1)^{−3}` (ET Lemmas 3.1, 3.2, 3.7; for β ≥ 1
use `ℓ^{−β} ≤ ℓ^{−1}`). With `β = 1/log x` this gives
`Σ_{ℓ≤x} p̄_ℓ ≤ C'(log x)³`, so `μ̄ ≤ C'(A log N)³`. Put `λ₀ = A log N`,
`L₀ = λ₀/k` (so λ = λ₀) and `α = max(λ₀^{−1/4}, 3k log(A log N)/λ₀)`.
In (3.1):
* `19αλ₀ ≤ 19λ₀^{3/4} + 57 k log(A log N)`;
* the first mass sum is `≤ C min(α,1)^{−3} ≤ C λ₀^{3/4}` (as `α ≥ λ₀^{−1/4}`);
* `αL₀ ≥ 3 log(A log N)`, so the second is `≤ (A log N)^{−3}·C'(A log N)³ = C'`;
* `s_* ≥ min(log ℓ₀, λ₀/k)`, so `G = O(log(k + log N))` and the G-terms
  are `O(log²(k + log N)) = O((log N)^{3/4} + k)`. ∎

**Corollary 3.3 (order needed; PROVED).** Consider any method that bounds
`#(𝒜 ∩ [1,N]) ≤ B` through a (A log N, k)-mixed majorant ν of a
Cor 3.2 family, with `B ≥ ½ N·Eν`. (This holds whenever the method's
evaluation of `Σ_{n≤N} ν(n)` asserts the CRT main term `N·Eν` up to an
error of at most half of it, e.g. via any hypothesis of the form
"order-j correlation sums equal their CRT predictions up to small
error", j ≤ k, together with any evaluation of the terms of level
`≤ A log N`.) Then its saving `log(N/B)` is at most
`C₉[(log N)^{3/4} + k log log N] + log(P/φ(P)) + log 2`. Hence:
* bounded k (any fixed order; e.g. pair or triple correlations of
  witnesses, however precise) cannot give θ > 3/4;
* a saving `(log N)^θ` with θ > 3/4 needs `k ≥ c(log N)^θ/log log N`.

Together with Corollary 2.2 (order K = 2⌈(log N)^θ⌉ suffices for the
prime family): **the correlation order needed for saving `(log N)^θ` is
`(log N)^θ` up to a factor `log log N`, in both directions.** ∎

**Corollary 3.4 (all K2 families, weaker; PROVED from K2 Thm 5.1).** Let
𝔊 be any finite K2 family (ℛ(M)-, (a,D)-, Case-A, selector classes, any
moduli). Let ν be a majorant of 𝒜(𝔊) each of whose terms is an
intersection of at most k classes of modulus `≤ N^A`, or has level
`≤ A log N`. Then ν has K2 level `≤ kA log N`, so
`log(1/Eν) ≤ C(kA log N)^{3/4}(log(kA log N))^{3/4}`. Bounded k gives
no θ > 3/4; saving `(log N)^θ` needs `k ≥ (log N)^{4θ/3−1−o(1)}`. ∎

*Gap.* For composite-moduli families, k between `(log N)^{4θ/3−1}` and
`(log N)^θ/log log N` is excluded only for prime-slice families
(Cor 3.3). Closing it needs K2 Thm 5.1 with truncated weights
`min(log ℓ, L₀)` (open; not attempted).

## 4. Comparison with known correlation results

### 4.1 Two structural facts about the hypothesis

**Proposition 4.1 (no Kubilius-type model; PROVED).** There is an absolute
`C₁` such that if `log y ≥ C₁(log N)^{1/3}`, the law of the hit vector
`x(n) = (x_ℓ(n))_{ℓ∈𝒫_y}`, n uniform in [1,N], is at total variation
distance `≥ 1 − C₁(log y)^{−2}` from the CRT product law.

*Proof.* `1 ≤ F(ℓ) ≤ τ(A²) = ℓ^{o(1)}`, so `(½) log ℓ ≤ log(1/p_ℓ) ≤ log ℓ`
for `ℓ ≥ ℓ₁`. Under the product law put `Z = Σ x_ℓ log(1/p_ℓ)`. By (1.3),
with `ε = (c/2C)^{1/2}`, `Σ_{y^ε<ℓ≤y} p_ℓ ≥ (c/2)(log y)²`, hence
`EZ ≥ c₂(log y)³`, while `Var Z ≤ Σ p_ℓ log²(1/p_ℓ) ≤ C(log y)⁴`. A pattern
x with `Z(x) ≥ EZ/2` has probability `≤ Π_{x_ℓ=1} p_ℓ = e^{−Z(x)} ≤ e^{−EZ/2}`.
The set S of patterns realised by `n ≤ N` has `|S| ≤ N`, so by Chebyshev
`P_CRT(S) ≤ N e^{−c₂(log y)³/2} + 4C/(c₂²(log y)²)`, while `P_{[1,N]}(S) = 1`.
For `C₁` large the first term is `≤ (log y)^{−2}`. ∎

So for θ > 2/3 (where TC_θ is not a theorem) the whole hit vector on
[1,N] is far from the CRT law: [1,N] is a sample of N patterns from a
law of entropy `≍ (log y)³ ≫ log N`. TC_θ can only be a statement about
**low-complexity statistics** (here: K symmetric moments of the count).
Contrast `ω_y(n)` (class 0 mod every ℓ): its entropy is `≍ log y`, and the
Kubilius model holds in total variation up to `y = N^{1/u}`, `u → ∞`
(Kubilius; Tenenbaum, *Crible d'Ératosthène et modèle de Kubilius*, 1999,
with a bound in terms of Dickman's ρ(u)). The ES hit vector has *cubic*
entropy, which is exactly why the cubic supply helps the CRT model and
also why no TV model survives above level N.

**Proposition 4.2 (TC fails at order ≍ log N; PROVED).** If
`K ≥ (e²/2 + ε) log N` and N ≥ N₀(ε), then TC(N; K, y_K, η_K) is false.

*Proof.* Squares lie in no class of 𝓡(ℓ). Indeed, for a prime `q | A`
(A = (ℓ+1)/4) we have `ℓ ≡ −1 (mod q)`; for odd q reciprocity with
`ℓ ≡ 3 (4)` gives `(q/ℓ) = (−1)^{(q−1)/2}(ℓ/q) = (−1)^{(q−1)/2}(−1/q) = 1`,
and for q = 2, A even gives `ℓ ≡ 7 (8)`, so `(2/ℓ) = 1`. Hence `(D/ℓ) = 1`
for every `D | A²` and `(−4D/ℓ) = (−1/ℓ) = −1`: every class is a
non-residue (the Mordell/Jacobi obstruction used in K2). So
`#{n ≤ N : f_y(n) = 0} ≥ ⌊√N⌋`, which contradicts Corollary 2.2's
`(e+2)N e^{−K/e²} ≤ (e+2)N^{1/2−ε'}` for such K and large N. ∎

So TC(N; K, y_K, η_K) is a theorem for `K ≤ c₀(log N)^{2/3}`
(Prop 2.4), false for `K ≥ 4 log N` (Prop 4.2), and TC_θ for
`3/4 < θ < 1` is the open middle. It is falsifiable at every finite N by
computing K moments (§5).

### 4.2 Known divisor-type correlation results, measured against TC_θ

By Lemma 1.3, order-k witness correlations are k-point correlations of
ω-type functions along k shifts `4D_i < y²`. The requirements for
θ > 3/4 are (Cor 2.3, Cor 3.3): order `k ≳ (log N)^θ/log log N`, combined
moduli `exp((log N)^{3θ/2})` (prime family), and aggregate relative
precision `e^{−ck}` in moments of size `e^{ck}`.

| input (literature) | order / shifts | error | covers moduli above N? | verdict |
|---|---|---|---|---|
| Ingham, Estermann; Heath-Brown 1979 (`N^{5/6+ε}`); Deshouillers–Iwaniec 1982 (`N^{2/3+ε}`): `Σ τ(n)τ(n+h)` | 2, fixed h | power saving | yes (divisor switching) | order 2: Cor 3.3 ⇒ useless for θ > 3/4, however precise |
| `Σ τ(n)τ(n+h₁)τ(n+h₂)` | 3 | open pointwise; known on average over shifts (Browning 2011, Blomer 2017) | averaged | order 3: same |
| Matomäki–Radziwiłł–Tao (2019, I/II): `Σ τ_k(n)τ_l(n+h)` for almost all `h ≤ H` | 2 shifts, fixed k, l | o(1) or power saving, exceptional h | yes, averaged | bounded order; exceptional-shift sets are fatal for a fixed tuple of shifts `4D_i` |
| Tao–Teräväinen (2018–19): log-averaged correlations of 1-bounded multiplicative functions, odd-order Chowla/Elliott | fixed k shifts | o(1), logarithmic averaging | yes | bounded order, o(1) error, multiplicative 1-bounded; none of the three requirements |
| Elliott–Halberstam-type level for τ, τ₃ (Selberg/Hooley/Heath-Brown 2/3 for τ; Friedlander–Iwaniec, Heath-Brown 1/2+1/82, Fouvry–Kowalski–Michel 1/2+1/46 for τ₃) | 1 class at a time | power saving | no (moduli < N) | IF Thm 2.5 / K2: any evaluation below N/2 is capped at 3/4 |
| Granville–Soundararajan (2007), sieve proof of Erdős–Kac with moments | growing, `≪ (log log N)^{1/3}`-type | explicit | no (they take `y = N^{1/k}` so products stay ≤ N) | below N by design |
| Kubilius model (Kubilius; Tenenbaum 1999) | all orders | `ρ(u)`-type in TV | **yes** | single shift (class 0): hits are divisors of one integer ≤ N. Prop 4.1: no TV analogue for the ES hit vector once θ > 2/3 |
| Ford (2025, arXiv:2408.03803): Kubilius model for shifted primes `p + a` | all orders | TV estimate | yes | single shift again |

(Dates/precisions are as remembered from the literature and serve only to
place each result on the three axes; none is used in a proof.)

**Assessment 4.3.** No known theorem, and no standard conjecture that we
know of, supplies TC_θ for any θ > 2/3, let alone θ > 3/4.
* All divisor-correlation theorems and the standard conjectures
  (Hardy–Littlewood/Elliott/Chowla type, binary/ternary additive divisor
  problems) have a **fixed number of shifts**. By Cor 3.3 (prime-slice
  families) and Cor 3.4 (all K2 families), fixed order gives no θ > 3/4,
  even with a power-saving error and with everything below N evaluated
  exactly. This is a theorem about hypotheses that assert CRT/local-
  density main terms, which all of these do.
* Level-of-distribution statements (EH for τ_k, BV/BFI/DI) live below
  modulus N and are capped by IF Thm 2.5 / K2 Thm 5.1.
* The only known mechanism controlling *all* orders above modulus N is the
  Kubilius model, which rests on hits being divisors of a single integer.
  By Lemma 1.3 the ES hits are divisors of `~y²` different shifts, and by
  Prop 4.1 no TV model can hold. A proof of TC_θ would have to control
  K-th moments of a sum of ω-functions over `≍ y_K²` shifts (with K and
  `log y_K ≍ K^{1/2}` growing), i.e. a "Kubilius model for many shifts in
  the moment sense". We know of no result of this kind for even two
  shifts with `K → ∞` moments at relative precision `e^{−cK}`.
* Uniform-in-k conjectures (k-tuple conjectures with k growing) are not
  standard; and TC itself is false at k ≍ log N (Prop 4.2), so any such
  conjecture must stop below order log N, as TC_θ (θ < 1) does.

**Verdict on the door.** TC_θ is a *natural, falsifiable* hypothesis
(CONJECTURE, not evidence-backed beyond §5): it is a theorem up to
`θ = 2/3` (Prop 2.4), false at `θ = 1` (Prop 4.2), and for
`3/4 < θ < 1` it implies the θ target (Cor 2.3). Bounded-order
correlation input, of any precision, is useless for θ > 3/4 (Cor 3.3,
3.4). The order needed is `(log N)^θ` up to `log log N` (Cor 2.2 + Cor 3.3).
