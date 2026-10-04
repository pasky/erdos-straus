# EXCEPTIONAL_NONCRT — can a non-CRT input beat θ = 3/4? (task O11)

Status: **in progress.** Labels follow `DISCOVERIES.md`. PROVED means proved
in this file, internal checks only, not refereed.

Notation as in `EXCEPTIONAL_THETA.md` (ET-file below): prime-slice system
`(Q₀, 𝒫, R, F_ℓ(c))`, avoider set `𝒜`, `p_ℓ(c) = |F_ℓ(c)|/ℓ`,
`p̄_ℓ = avg_{c∈R} p_ℓ(c)`. A *majorant* is a finite real combination
`ν(n) = Σ_i a_i 1[n ≡ b_i (mod d_i)]` with `ν ≥ 0` on ℤ and `ν ≥ 1` on 𝒜.
`Eν` is its mean over a common period `Q_tot`, and `ν̂(θ) = E_n ν(n)e(−nθ)`
for `θ ∈ (1/Q_tot)ℤ/ℤ`, so `ν(n) = Σ_θ ν̂(θ)e(nθ)` and `ν̂(0) = Eν`.

## 1. The three candidates, made precise

The ET-file caps (Thm 2.5, 2.7, Lemma 2.9) apply to bounds of the shape

    #(𝒜 ∩ [1,N]) ≤ Σ_{n≤N} ν(n) ≤ N·Eν + Σ_i |a_i|.              (1.1)

The task names three ways out.

**(a) Signed rounding.** Exactly,

    Σ_{n≤N} ν(n) − N·Eν = Σ_{θ≠0} ν̂(θ) S_N(θ),   S_N(θ) = Σ_{n≤N} e(nθ),   (1.2)

and `|S_N(θ)| ≤ min(N, 1/(2‖θ‖))`. All cancellation *inside one
frequency* — sums of `a_i e(−b_iθ)` over the classes of a modulus, i.e.
Gauss, Kloosterman, Ramanujan or divisor-exponential sums over the
forced classes — is already inside `ν̂(θ)`. We call

    R_w(ν) = Σ_{θ≠0} |ν̂(θ)|·w(θ),   any weight w ≥ 1,             (1.3)

a **per-frequency rounding bound**. With `w(θ) = min(N, 1/(2‖θ‖))` it is a
valid bound for (1.2). Since every class indicator has
`Σ_θ |1̂[·≡b (d)](θ)| = 1`, one has `R_1(ν) ≤ Σ_i|a_i|`, so (1.3) with w=1
is never worse than (1.1) and can be much better (e.g.
`Σ_{b mod d} 1[n≡b (d)] = 1` has `Σ|a_i| = d`, `R_1 = 0`). The only
cancellation (1.3) does not capture is cancellation *between different
frequencies* in (1.2); a bound using that is a bound for
`Σ_{n≤N}ν(n)` by other means (see §2.4).

**(b) Prime-only majorants.** ν need only be ≥ 0 on primes and ≥ 1 on the
primes of 𝒜; the count is `Σ_{p≤N} ν(p)`, evaluated with prime
equidistribution (Siegel–Walfisz, Bombieri–Vinogradov, BDH).

**(c) Moment / variance methods.** For a finite witness family 𝒲 let
`f(n) = #{W ∈ 𝒲 : n ∈ W}` (each W a residue class). Bound
`#{n ≤ N : f(n) = 0}` by `Σ_n P(f(n))` for a polynomial P with
`P ≥ 0` on ℤ_{≥0} and `P(0) ≥ 1` (Chebyshev/Turán–Kubilius is
`P(x) = (1 − x/m)²`), and evaluate the moments
`Σ_n f(n)^j` either by CRT or by counting tuples of solutions directly.

## 2. Candidate (a): per-frequency signed rounding cannot beat 3/4

### 2.1 A Boolean sieve limit with a high-level tail

Setting of ET-file Prop. 2.4: independent `x_i ~ Bern(p_i)`, i ∈ I finite,
weights `s_i ≥ s_* > 0`, and for `S ⊆ I` the level `s(S) = Σ_{i∈S} s_i`.
Put `y_i = x_i − p_i`; the monomials `y^S = Π_{i∈S} y_i` are orthogonal, so
every f on `{0,1}^I` has a unique *biased Walsh expansion*
`f = Σ_S d_S y^S`, with `d_∅ = E f`.

**Proposition 2.1 (PROVED).** Assume `p_i ≤ 1/4` for all i. Let f ≥ 0 on
`{0,1}^I` with `f(0) ≥ 1`, and let λ ≥ s_*. Split
`f = f_lo + f_hi`, where `f_lo = Σ_{s(S)≤λ} d_S y^S`, and put

    r₀ = Σ_{s(S)>λ} |d_S| Π_{i∈S} p_i,      r₁ = Σ_{s(S)>λ} |d_S| Π_{i∈S} 2p_i(1−p_i).

Then for every α > 0, with Φ the right-hand side of ET-file (2.3),

    E f ≥ (1 − r₀)·e^{−Φ} − 2 r₁.                                   (2.1)

*Proof.* Since `|y^S(0)| = Π_S p_i` we get `f_lo(0) ≥ f(0) − r₀ ≥ 1 − r₀`.
Since `E|y_i| = 2p_i(1−p_i)` and the `y_i` are independent,
`E|f_hi| ≤ r₁`. Since `E y^S = 0` for S ≠ ∅, `E f = E f_lo`.

Let V = {i : s_i ≤ λ}. `f_lo` depends only on `x_V`. Put
`h = E[|f_hi| | x_V]`. From `f ≥ 0` we get `f_lo ≥ −|f_hi|` pointwise, and
averaging over `x_{I∖V}` gives `f_lo ≥ −h` on `{0,1}^V`, with `E h ≤ r₁`.

Now run Steps 1–4 of ET-file Prop. 2.4 on `f_lo` over the coordinates V,
carrying h along.
* Thinning `x = u∘w` (Step 2): for fixed w, `f_{lo,w}(u) = f_lo(u∘w)` is
  λ-level, `f_{lo,w}(0) = f_lo(0) ≥ 1 − r₀`, and `f_{lo,w} ≥ −h_w` with
  `h_w(u) = h(u∘w) ≥ 0`.
* Symmetrisation (Step 3): the orbit average of `f_{lo,w}` is `Q(K)` with
  `Q ∈ P_Λ`, and `Q(k) = E[f_{lo,w} | K = k]` because u is uniform on each
  orbit given K. So `Q(k) ≥ −H(k)` with `H(k) = E[h_w | K = k] ≥ 0`.
* Interpolation at 0 (Step 4) with the same node sets and weights
  `L_j(y) = Π_g ℓ^{(g)}_{y_g}(0)`, `|L_j(y)| ≤ B_j ψ(y)`. Write
  `L·Q = L·(Q+H) − L·H ≤ |L|(Q+H) + |L|H`, where `Q+H ≥ 0`. Hence

      1 − r₀ ≤ Q(0) ≤ Σ_j |c_j| B_j Σ_y ψ(y)(Q(y) + 2H(y))
             ≤ e^{Φ(w)} · (E_u f_{lo,w} + 2 E_u h_w).

  Here `e^{Φ(w)} = 2^G|Λ'| max_j Π_g B_g(j_g)` is exactly the quantity
  bounded in Step 5.
So `E_u f_{lo,w} ≥ (1−r₀)e^{−Φ(w)} − 2E_u h_w`. Average over w, use
Jensen and Step 5 as in ET-file, and `E_w E_u h_w = E h ≤ r₁`. ∎

*Remark.* For a λ-level f, `r₀ = r₁ = 0` and (2.1) is ET-file Prop. 2.4.
Prop. 2.1 lets f have arbitrary level; it only pays for the high part
through the two tail sums, which carry the factor `Π_S p_i ≤ e^{−s(S)}` if
`s_i ≤ log(1/(2p_i))`.
