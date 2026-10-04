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

### 2.2 Fourier mass controls the high-level Walsh tail

Take a prime-slice system (ET-file §1) and a majorant ν (any moduli: higher
prime powers, non-slice primes, arbitrary residues). Restrict 𝒫 to the
slice primes dividing some `d_i`; this keeps ν ≥ 1 on the new (larger)
avoider set, by the CRT modification argument of ET-file Step 0, provided
`|F_ℓ(c)| < ℓ` for every ℓ. So 𝒫 is finite.

For `c ∈ R` put `x_ℓ(n) = 1[n mod ℓ ∈ F_ℓ(c)]`, `y_ℓ = x_ℓ − p_ℓ(c)`, and
`ν_c(x) = E[ν(n) | n ≡ c (Q₀), x(n) = x]`. By CRT, given `n ≡ c (Q₀)` the
`x_ℓ` are independent `Bern(p_ℓ(c))`. Expand `ν_c = Σ_S d_S(c) y^S`.

For `S ⊆ 𝒫` let `Θ_S` be the set of frequencies
`θ = a/Q₀ + Σ_{ℓ∈S} h_ℓ/ℓ (mod 1)` with `a mod Q₀` arbitrary and every
`h_ℓ ≢ 0 (mod ℓ)`. Put `A_S(ν) = Σ_{θ∈Θ_S} |ν̂(θ)|`. Since `(ℓ, Q₀) = 1`
and the ℓ are distinct primes, the sets Θ_S are pairwise disjoint and
`0 ∉ Θ_S` for S ≠ ∅. Hence

    Σ_{S≠∅} A_S(ν) ≤ R_1(ν) = Σ_{θ≠0} |ν̂(θ)| ≤ R_w(ν)   (w ≥ 1).     (2.2)

**Lemma 2.2 (PROVED).** For every `c ∈ R` and `S ≠ ∅`,

    |d_S(c)| · Π_{ℓ∈S} p_ℓ(c)(1 − p_ℓ(c)) ≤ A_S(ν) · Π_{ℓ∈S} p_ℓ(c).

*Proof.* By orthogonality and the tower property,
`d_S(c)·Π_S p_ℓ(1−p_ℓ) = E[ν_c y^S] = E[ν(n) y^S(n) | n ≡ c (Q₀)]
= Q₀·E_n[ν(n) g(n)]`, where `g(n) = 1[n ≡ c (Q₀)]·Π_{ℓ∈S} y_ℓ(n mod ℓ)`.
By CRT g is a product of functions of `n mod Q₀` and of `n mod ℓ`
(ℓ ∈ S). The first factor has Fourier coefficients `e(−ac/Q₀)/Q₀` at
`a/Q₀`. The factor `y_ℓ` has mean 0, so its coefficients live at `h/ℓ`
with `h ≢ 0`, where they equal `1̂_{F_ℓ(c)}(h)`, of modulus
`≤ |F_ℓ(c)|/ℓ = p_ℓ(c)`. So ĝ is supported on Θ_S with
`|ĝ(θ)| ≤ Q₀⁻¹ Π_S p_ℓ(c)`. Parseval, `E[νg] = Σ_θ ν̂(θ)·conj(ĝ(θ))`,
gives the claim. ∎

Consequently, if `p_ℓ(c) ≤ 1/4`, the tails of Prop. 2.1 for `f = ν_c` obey

    r₀(c) ≤ Σ_{s(S)>λ} A_S Π_S (4/3)p_ℓ(c),   r₁(c) ≤ Σ_{s(S)>λ} A_S Π_S 2p_ℓ(c).   (2.3)

So with weights `s_ℓ := log(1/(2p_ℓ⁺))`, `p_ℓ⁺ = max_{c∈R} p_ℓ(c)`, both
tails are `≤ e^{−λ} R_1(ν)` for every c.

### 2.3 The cap

**Theorem 2.3 (sieve limit with per-frequency rounding; PROVED).** Take a
prime-slice system with `p_ℓ(c) ≤ 1/4` for all ℓ ∈ 𝒫, c ∈ R, and a
majorant ν of *arbitrary* level. Use the weights `s_ℓ = log(1/(2p_ℓ⁺))`
(so `s_ℓ ≥ log 2`), and write `Φ̄(λ, α)` for the right-hand side of
ET-file (2.4) minus `log(Q₀/|R|)`, computed with these weights:
`Φ̄ = 19αλ + C₄ Σ_{s_ℓ≤λ} p̄_ℓ e^{−αs_ℓ} + G(75+log(2+λ/s_*)) + (G/2)log(16μ̄+16)`.
Then for all λ ≥ s_*, α > 0,

    Eν ≥ (|R|/Q₀) · [ (1 − ε) e^{−Φ̄(λ,α)} − 2ε ],                    (2.4)

    ε = ε_λ(ν) := Σ_{S: s(S)>λ} A_S(ν) e^{−s(S)} ≤ e^{−λ} R_1(ν).

Only the Fourier mass of ν at frequencies of *level above λ* enters; the
low-level Fourier mass is unrestricted.

*Proof.* `Eν = Q₀⁻¹ Σ_c E[ν_c] ≥ (|R|/Q₀) avg_{c∈R} E ν_c` (ν ≥ 0).
For c ∈ R, `ν_c ≥ 0` and `ν_c(0) ≥ 1` (the event `{c} × {x = 0}` lies in
𝒜 and has positive probability). Apply Prop. 2.1 in the fibre, with the
fibre probabilities `p_ℓ(c)` and the c-independent weights `s_ℓ`; by (2.3)
`r₀(c), r₁(c) ≤ ε`. Average over c and use Jensen for the convex `e^{−Φ}`,
exactly as in ET-file Thm 2.5 (Φ_c is affine in the `p_ℓ(c)` except for
the concave log term). ∎

**Corollary 2.4 (PROVED).** Suppose an argument bounds `#(𝒜∩[1,N])` by

    N·Eν + R_w(ν),   w ≥ 1   (any per-frequency rounding bound),     (2.5)

and the bound equals `N e^{−s}` with s ≥ 0. Then

    s ≤ Φ̄(λ_N, α) + log 4 + log(Q₀/|R|)   for every α > 0,

where `λ_N` is any λ ≥ s_* with `λ ≥ log(4N) + Φ̄(λ, α)`.

*Proof.* `R_1 ≤ R_w ≤ N e^{−s} ≤ N`, so `ε ≤ N e^{−λ} ≤ e^{−Φ̄}/4`. Then
(2.4) gives `e^{−s} ≥ Eν ≥ (|R|/Q₀)(3/4 − 1/2) e^{−Φ̄}`. ∎

Two differences from ET-file Lemma 2.9 + Cor 3.4:
* the rounding is any `Σ_{θ≠0}|ν̂(θ)|w(θ)`, not `Σ|a_i|`, which is
  never smaller (since R_1 ≤ Σ|a_i|);
* **no bound on the size of the slice primes is needed.** Large primes
  enter only through `p̄_ℓ e^{−αs_ℓ}` and through ε. This closes the
  exclusion "slice primes beyond N^{O(1)}" of ET-file §6.1 item 7 for the
  dominant-prime-slice class.

**Corollary 2.5 (the Case-B/Case-A families; PROVED).** Under the
hypotheses of ET-file Cor 3.4 (forced classes of Lemma 16.1 or 3.2, or
Case-A classes; moduli `q₀ℓ` with `q₀ ≤ ℓ^C`, C < 1; selector R;
`ℓ ≥ ℓ₀(C)`), every bound of the form (2.5) has saving

    s ≤ C₈(C) (log N)^{3/4} + log(P/φ(P)).

*Proof.* As in Cor 3.4, `|F_ℓ(c)| ≤ ℓ^{C+o(1)}`, so for `ℓ ≥ ℓ₀(C)`:
`p_ℓ⁺ ≤ 1/4` and `s_ℓ ≥ ((1−C)/2) log ℓ`. Hence
`Σ p̄_ℓ e^{−αs_ℓ} ≤ Σ p̄_ℓ ℓ^{−α'}` with `α' = α(1−C)/2`, which is
`≪ α'^{−3}` by Lemmas 3.1, 3.2 and 3.7 of the ET-file (and
`ℓ^{−α'} ≤ M^{−α'/2}` as there). With `α = λ^{−1/4}`,
`Φ̄(λ) ≤ C(C)λ^{3/4} + O(log²λ)`; the truncated mass is
`μ̄ ≤ Σ_{s_ℓ≤λ} p̄_ℓ ≪ λ³`, so the G-terms are `O(log²λ)`. Then
`λ_N = 2 log(4N)` satisfies the condition of Cor 2.4 for N ≥ N₀(C). ∎

**What this closes.** Candidate (a) in its natural form — "use the
arithmetic structure of the forced classes (Gauss/Kloosterman/divisor
exponential sums) to beat the trivial rounding `Σ|a_i|`" — is capped at
`(log N)^{3/4}`. A cancellation inside each frequency improves R_w by at
most the ratio `Σ|a_i| / R_1(ν)`, and Theorem 2.3 shows that even
`R_1(ν) < N` (with no other restriction) already forces the 3/4 cap.

### 2.4 What is left of (a)

* *Scope.* Theorem 2.3 is for prime-slice systems (the world of ET-file
  Cor 3.4). The sequential/shared-prime world of ET-file Thm 2.7/Cor 3.6
  and balanced moduli are not covered here; Lemma 2.2 uses that distinct
  slice primes give disjoint frequency sets Θ_S.
* *Inter-frequency cancellation.* The only rounding not covered by (2.5)
  uses cancellation between different θ in (1.2). By (1.2) such a bound
  is just a bound for `Σ_{n≤N} ν(n)` obtained without the CRT main term.
  That is no longer a sieve; it is a direct count. Its only *a priori*
  limit is `Σ_{n≤N}ν(n) ≥ #(𝒜 ∩ [1,N])`. For the integer avoider set this
  limit is far below the 3/4 scale: it contains the squares coprime to the
  selector (`W(m²) = +∞`, DISCOVERIES (C)12), about `√N/log log N` of
  them, and nothing forces more. So there is **no set-level obstruction**
  for θ < 1, and also no method: Theorem 2.3 says any such argument must
  control `Σ_{n≤N}ν(n)` for a majorant whose *high-level* Fourier mass is
  large: by (2.4), if `ε_λ(ν) ≤ e^{−Φ̄(λ)}/4` at some λ, the saving is
  `≤ Φ̄(λ) + O(1)`. To save `(log N)^θ` with θ > 3/4 one needs
  `ε_λ(ν) > e^{−Cλ^{3/4}}/4` for all `λ ≤ (log N)^{4θ/3}/C'`, i.e.
  Fourier mass `A_S ≳ e^{s(S) − Cλ^{3/4}}`, superpolynomial in N, at
  frequencies whose denominators are superpolynomial in N, and then a
  cancellation *among* those frequencies in (1.2).
