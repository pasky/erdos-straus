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

## 3. Candidate (b): prime-only majorants

A *prime majorant* is ν (finite combination of classes) with ν ≥ 0 at all
primes and ν ≥ 1 at all primes of 𝒜; the bound is `Σ_{p≤N} ν(p)`.

**Lemma 3.1 (PROVED).** Let L be a common period of ν containing Q₀ and the
(finitely many) relevant slice primes, and assume
`|F_ℓ(c) ∖ {0}| < ℓ − 1` for all ℓ, c. Then ν is a prime majorant iff
ν ≥ 0 on every reduced class mod L and ν ≥ 1 on every reduced class mod L
contained in 𝒜.

*Proof.* Dirichlet: every reduced class mod L contains infinitely many
primes, and ν, 𝒜 are L-periodic (after the Step-0 reduction of ET-file,
which needs a unit residue outside `F_ℓ(c)`; that is the hypothesis). ∎

So the LP for prime majorants is the ET-file LP for the measure
`E*` = uniform on `(ℤ/L)^×`. By CRT, under E* the coordinates
`n mod Q₀` (uniform on `(ℤ/Q₀)^×`) and `n mod ℓ` (uniform on `(ℤ/ℓ)^×`)
are independent. Put `R* = R ∩ (ℤ/Q₀)^×` and
`p*_ℓ(c) = |F_ℓ(c) ∖ {0}|/(ℓ−1)`.

**Theorem 3.2 (PROVED).** ET-file Theorem 2.5 holds for prime majorants with
E, R, Q₀, p_ℓ(c) replaced by E*, R*, φ(Q₀), p*_ℓ(c) (and the hypothesis
`|F_ℓ(c)∖{0}| ≤ (ℓ−1)/4`). ET-file Lemma 2.9 (coefficient budget ⇒
level) also holds for E*, with the mean increase `a_i/φ(d'_i)` in place of
`a_i/d'_i`, i.e. an extra factor `max d'/φ(d') ≪ log λ`.

*Proof.* The proof of Thm 2.5 uses only: a product measure across the CRT
coordinates; fibres `c ∈ R`; hit indicators independent Bernoulli with
parameters `p_ℓ(c) ≤ 1/4`; and `{c} × {x = 0} ⊆ 𝒜` with positive measure.
All four hold for E* with the starred data. ∎

For the families of ET-file Cor 3.4, `p*_ℓ(c) ≤ (ℓ/(ℓ−1)) p_ℓ(c)`, so the
profile `Σ p̄*_ℓ ℓ^{−α}` is the same up to a factor `1 + O(1/ℓ₀)`, and the
cap `C(log N)^{3/4}` at level `A log N` is unchanged.

**Theorem 3.3 (primality is worth at most a factor λ^{O(1)}; PROVED).** Let
ν be an *integer* majorant (≥ 0 on ℤ) that is ≥ 1 only on `𝒜 ∩ 𝒫_z`, where
`𝒫_z = {n : (n, P(z)) = 1}` with `z ≤ e^λ` (this is how a sieve detects
primes). Then ν is a majorant of the prime-slice system obtained by adding
the class `0` to every `F_ℓ(c)`, ℓ ≤ z (and adding each prime ℓ ≤ z not
yet in 𝒫 as a slice prime with `F_ℓ = {0}`; the primes ℓ < 5, where
`1/ℓ > 1/4`, are put into the selector, as in the 3/4 note). Its
Theorem 2.5 bound
increases by at most

    C₄ Σ_{ℓ≤z} ℓ^{−1−α} + (G/2)·log(1 + log log z + O(1))
      ≤ C₄ (log(1/α) + O(1)) + O(log²λ).

With `α = λ^{−1/4}` this is `O(log²λ)`: the cap
`C(log N)^{3/4}` becomes `C(log N)^{3/4} + O((log log N)²)`.

*Proof.* `𝒜 ∩ 𝒫_z` is exactly the avoider set of the augmented system;
the new probabilities are `p_ℓ + 1/ℓ` (class 0 is not a forced class of
the families, since those classes are units mod ℓ; if it were, nothing
changes). Plug into (2.4). ∎

**Remark 3.4 (where the level comes from; Assessment for the second
bullet).**
* The final bound of a prime-majorant argument is
  `Σ_i a_i π(N; d_i, b_i) = π(N)·E*ν + Σ_i a_i E(N; d_i, b_i)`, where
  `E(N;d,b) = π(N;d,b) − π(N)/φ(d)` for reduced b. The main term is capped by
  Theorem 3.2 at level λ. Every known or conjectured equidistribution input
  (Siegel–Walfisz, BV, BDH, EH, GRH) controls `E(N;d,b)` only for
  `d ≤ N^{O(1)}`; for `d > N`, `π(N;d,b) ∈ {0,1}` and, short of knowing
  which classes contain a prime `≤ N`, the term costs `|a_i|`, which is
  the Lemma 2.9 situation. So prime majorants live at level `N^{O(1)}`.
* Prime inputs are also *weaker* in the error term. The method needs
  `|Σ a_i E(N;d_i,b_i)| ≤ π(N) e^{−(log N)^θ}`. BV and BDH save only
  `(log N)^{−A}` on average; Siegel–Walfisz (ineffective) and the
  Vinogradov–Korobov zero-free region save at most
  `exp{−c(log N)^{3/5}(log log N)^{−1/5}}` even for d = 1. Unconditionally,
  no asymptotic prime count is known with the relative accuracy
  `exp{−(log N)^{3/4}}` that the *current* 3/4 bound already has. The 3/4
  note avoids this by sieving the integers (it bounds `E(N) ≥ E_pr(N)`).
  Under GRH, `E(N;d,b) ≪ N^{1/2}log²N` and Theorem 3.2 is the binding
  constraint.

So restricting to primes, by Dirichlet-measure (Thm 3.2) or by an extra
sieve (Thm 3.3), changes the LP limit only by `O((log log N)²)` in the
saving. **Candidate (b) cannot beat 3/4**, for any level `N^{O(1)}` —
hence for BV (level ½), BDH, Elliott–Halberstam, or any level-`N^A`
equidistribution hypothesis.

## 4. Candidate (c): moment and variance methods

Fix a finite witness family 𝒲 of residue classes and put
`f(n) = Σ_{W∈𝒲} 1_W(n)`, so `𝒜_𝒲 = {f = 0}`.

**Proposition 4.1 (moment bounds are CRT majorants; PROVED).** Let P be a
real polynomial with `P ≥ 0` on ℤ_{≥0} and `P(0) ≥ 1`. Then `ν = P∘f` is a
majorant of 𝒜_𝒲 in the sense of §1 (ν ≥ 0 on ℤ, ν ≥ 1 on 𝒜_𝒲), and
expanding `f^j` into j-fold intersections of classes writes ν as a finite
combination of class indicators. Hence every bound
`#{n≤N: f(n)=0} ≤ Σ_{n≤N} P(f(n))` whose moments are evaluated as
`N·(CRT density) + error` with a per-frequency error bound (2.5) is
covered by Theorem 2.3 / Cor 2.4–2.5; with prime moments
`Σ_{p≤N} P(f(p))` it is covered by Theorem 3.2. *Proof.* `f(n) ∈ ℤ_{≥0}`
for every n ∈ ℤ. ∎

So, for forced-class witness families satisfying Cor 2.5's hypotheses,
**no moment method of any order, with any polynomial, beats 3/4 if its
moments are evaluated through the CRT density plus a per-frequency error
term.** (Chebyshev/Turán–Kubilius is the case `P(x) = (1 − x/m)²`.)

**Proposition 4.2 (degree cap; PROVED).** In a prime-slice system with
`p_ℓ(c) ≤ 1/4`, let `μ̄ = Σ_ℓ p̄_ℓ`. If `deg P ≤ k` and every class of 𝒲
is a slice class (modulus `q₀ℓ`, `q₀ | Q₀`), then for every α > 0

    log(1/E[P∘f]) ≤ log(Q₀/|R|) + 19αk + C₄ e^{−α} μ̄ + 75 + log(2+k) + ½log(16μ̄+16).

Choosing `e^{α} = max(e, C₄μ̄/(19k))` gives saving
`≤ 19k(1 + log⁺(C₄μ̄/(19k))) + O(log(μ̄+k)) + log(Q₀/|R|)`.

*Proof.* Given `n ≡ c (Q₀)`, `f = Σ_ℓ φ_ℓ(n mod ℓ)` with φ_ℓ ≥ 0
supported on `F_ℓ(c)`. So `P(f)` is a sum of terms each depending on at
most k slice coordinates, and so is `ν_c = E[P(f) | c, x]` (by
independence of the coordinates). Apply ET-file Prop. 2.4 with all weights
`s_ℓ = 1` and level λ = k (one band, G = 1), and average over c as in
Thm 2.5. ∎

*Consequence.* With witness moduli `≤ N^{O(1)}` the cubic supply gives
`μ̄ ≪ (log N)³`, so a degree-k method saves `O(k log log N)`. The second
moment (k = 2) saves `O(log log N)`: at best a power of log N, i.e.
θ = 0. To save `(log N)^θ` one needs moments of order
`k ≫ (log N)^θ/log log N`, and for θ > 3/4 Cor 2.5 says the CRT
evaluation of those moments fails: their high-level Fourier mass must be
superpolynomial.

**What a non-CRT moment method would need (no theorem).** Elsholtz–Tao
(Thm 1.1) evaluate first moments `Σ_{p≤N} f_{I/II}(p)` up to constants by
divisor sums, Brun–Titchmarsh and BV. They state (Remark 1.3) that higher
moments `Σ_p f(p)^k` are out of reach *because the level of the relevant
divisor sums becomes too great* — the obstruction of Cor 2.5 in their
language. A non-CRT moment method for θ > 3/4 would have to count
j-tuples of solutions sharing the same p, for all j up to
`(log N)^{3/4+δ}`, i.e. points on fibre powers of the ES surface of
dimension growing with j, with absolute error `N e^{−(log N)^θ}`. By
Prop. 4.2 nothing of bounded order can suffice. No technique for such
counts is known; this is the content of "non-CRT input" for (c).

## 5. Numerical checks

`scripts/noncrt_checks.py` (output `data/noncrt/checks_m8.txt`, ~1 min):
* **Lemma 2.2, exact.** 40 random systems (Q₀ = 3, slice primes
  5,7,11[,13], random `F_ℓ(c)`), random signed class combinations ν. For
  every fibre and every S ≠ ∅, `|E[ν y^S | c]| ≤ A_S Π_S p_ℓ(c)`. Max of
  lhs − rhs: `−1.7·10⁻¹⁷`. (Check of the lemma, not EVIDENCE for anything
  else.)
* **Toy LP (EVIDENCE, model only).** Hit-pattern model, 8 slice primes
  5…29, `|F_ℓ| ≈ ℓ^{0.35}`, full mass 1.360. Minimum of Eν over ν ≥ 0,
  ν(0) ≥ 1 with (C) class-coefficient budget B, or (F) Fourier-ℓ¹ budget
  B (exact `a_ℓ`). Savings:

  | B | 2 | 8 | 32 | 128 | 1024 | 4096 |
  |---|---|---|---|---|---|---|
  | (C) | 0.223 | 0.501 | 0.787 | 1.030 | 1.303 | 1.358 |
  | (F) | 0.370 | 0.728 | 1.064 | 1.318 | 1.360 | 1.360 |

  Per-frequency rounding acts like the coefficient budget multiplied by a
  bounded factor (≈ 4–8 here, i.e. ≈ Π f_ℓ over a typical monomial), as
  Lemma 2.2 predicts. It does not change the shape of the trade-off.

## 6. Verdict and what remains

| candidate | result | label |
|---|---|---|
| (a) signed rounding, per-frequency (Gauss/Kloosterman/divisor exponential sums over the classes) | capped at `C(log N)^{3/4}` for dominant-prime-slice families (Thm 2.3, Cor 2.4–2.5); also removes ET-file's "slice primes ≤ N^{O(1)}" proviso | PROVED |
| (a′) cancellation *between* frequencies | equivalent to counting `Σ_{n≤N}ν(n)` directly; no set-level obstruction below θ = 1 (squares give only `√N`); needs superpolynomial high-level Fourier mass (§2.4) | open; no method |
| (b) prime-only majorants (Dirichlet measure, BV/BDH/EH/GRH level) | same LP limit up to `O((log log N)²)` (Thms 3.2, 3.3) | PROVED |
| (b′) prime error terms | unconditional prime equidistribution is *weaker* than the integer count at this precision (Remark 3.4) | Assessment |
| (c) moment/variance methods, CRT-evaluated | are CRT majorants (Prop 4.1), so capped by (a)/(b); degree k saves `O(k log log N)` (Prop 4.2): Chebyshev/2nd moment gives only θ = 0 | PROVED |
| (c′) moments evaluated by counting solution tuples | would need moments of order `≥ (log N)^{3/4+δ}` with absolute error `N e^{−(log N)^θ}`; ET Remark 1.3 already calls order 2 out of reach | open; no method |

**No non-CRT input tested here beats θ = 3/4.** The three natural
formalisations are capped, by proved theorems with the exact scope above.
What is left is precise. Each remaining route must do one of two things.
* Evaluate `Σ_{n≤N}ν(n)` (or `Σ_p`) for a majorant with
  superpolynomially large Fourier mass at superpolynomial denominators,
  with cancellation across frequencies.
* Count high-order (`(log N)^{3/4+δ}`) correlations of ES solutions
  without CRT.
Neither is a known technique. The other open doors of the ET-file
(balanced moduli, the sequential world of Thm 2.7, non-selector R) are
untouched: Theorem 2.3 is proved for prime-slice systems only.

## 7. Replay

```
uv run --with scipy python scripts/noncrt_checks.py 8 > data/noncrt/checks_m8.txt   # ~1 min, < 1 GB
```
