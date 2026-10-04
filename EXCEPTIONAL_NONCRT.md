# EXCEPTIONAL_NONCRT — can a non-CRT input beat θ = 3/4? (task O11)

Status: **checkpoint 1 (O11).** No θ > 3/4. Three candidate non-CRT
inputs are formalised and capped by proved theorems; the residue is stated
exactly. Labels follow `DISCOVERIES.md`. PROVED means proved in this file,
internal checks only, not refereed.

## 0. Summary

| item | statement | label |
|---|---|---|
| Prop 2.1 | Boolean sieve limit for majorants of **arbitrary level**: `Ef ≥ (1−r₀)e^{−Φ} − 2r₁`, where r₀, r₁ are the biased-Walsh tails above level λ | PROVED |
| Lemma 2.2 | the Walsh coefficient at slice set S is bounded by the Fourier ℓ¹ mass `A_S` of ν on the frequency set Θ_S: `|d_S|Π p(1−p) ≤ A_S Π p` | PROVED (+ exact numerical check) |
| Thm 2.3, Cor 2.4–2.5 | **per-frequency signed rounding is capped at 3/4**: any bound `N·Eν + Σ_{θ≠0}|ν̂(θ)|w(θ)` with w ≥ 1 (this contains Σ|a_i|, the sawtooth bound, and all Gauss/Kloosterman/divisor-exponential-sum cancellation within a frequency) saves `≤ C(log N)^{3/4}` for the ET-file Cor 3.4 families. Only the Fourier mass above level λ matters, and **no bound on the size of the slice primes is needed** (removes ET-file §6.1 item 7 for prime-slice families) | PROVED |
| §2.5 | weights < 1: for smooth windows, Q₀ = 1 and hit-pattern majorants, capped under an equidistribution conjecture (H_eq) (2.6); exact `|S_N|` and general majorants open | CONDITIONAL / open |
| Thm 3.2, 3.3 | **prime-only majorants**: same LP limit (Dirichlet measure), and detecting primality by a sieve adds `O((log log N)²)` to the saving; BV/BDH/EH/GRH-level inputs cannot beat 3/4 | PROVED |
| Rem 3.4 | unconditional prime error terms are weaker than the integer count at relative accuracy `e^{−(log N)^{3/4}}` | Assessment |
| Prop 4.1, 4.2 | **moment/variance methods** are CRT majorants (so capped by Thm 2.3/3.2 when CRT-evaluated); a degree-k moment method saves `O(k log log N)`, so Chebyshev/second moment gives θ = 0 | PROVED |
| §5 | toy LP (8 primes): Fourier-ℓ¹ budget ≈ coefficient budget × 4–8 | EVIDENCE (toy model) |

**Verdict.** None of (a), (b), (c), in the natural formalisations above,
beats θ = 3/4. What remains is (§6): cancellation *between* frequencies
(a direct count of `Σ_{n≤N}ν(n)`), per-frequency bounds with weights below
1 for non-hit-pattern majorants, and non-CRT counting of
`(log N)^{3/4+δ}`-fold correlations of ES solutions.

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
valid bound for (1.2). `R_1` (w ≡ 1) is in general *not* a valid bound,
but it is ≤ every R_w with w ≥ 1, and Theorem 2.3 below only uses
`R_1 ≤ (rounding bound)`. Every class indicator has
`Σ_θ |1̂[·≡b (d)](θ)| = 1`, so `R_1(ν) ≤ Σ_i|a_i|`, and `R_1` can be much
smaller (e.g.
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
Jensen and Step 5 as in ET-file, and `E_w E_u h_w = E h ≤ r₁`. (If
r₀ ≥ 1, (2.1) is implied by `E f ≥ 0`; coordinates with `p_i = 0` are
discarded first, as in ET-file Step 0.) ∎

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
(so `s_ℓ ≥ log 2`; take `s_* = log 2`), and write `Φ̄(λ, α)` for the right-hand side of
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
the concave log term). If ε ≥ 1/3 the right side of (2.4) is ≤ 0 and
there is nothing to prove; otherwise each fibre bound is
`(1−ε)e^{−Φ_c} − 2ε` and Jensen applies to the first term. ∎

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
  limit, as far as squares show, is far below the 3/4 scale: the avoider
  set contains the squares coprime to the selector (`W(m²) = +∞`,
  DISCOVERIES (C)12), about `√N/log log N` of them. No method is known;
  Theorem 2.3 says any such argument must
  beat the CRT mean, by the following dichotomy (a restatement of
  (2.4), nothing more). For any majorant ν and any λ, **either**
  `ε_λ(ν) > e^{−Φ̄(λ)}/4` (the Fourier mass above level λ is not small),
  **or** `Eν ≥ (|R|/Q₀)e^{−Φ̄(λ)}/4`, in which case a saving beyond
  `Φ̄(λ) + O(1)` requires `Σ_{n≤N}ν(n) ≪ N·Eν·e^{−(excess)}`, i.e. the
  interval [1,N] must carry far less ν-mass than its CRT share.
  Squares alone give no set-level obstruction to such a count below θ = 1;
  whether some other obstruction exists is not examined here.

### 2.5 The scope limit of Theorem 2.3: weights below 1 (open)

Theorem 2.3 needs a rounding bound that dominates `R_1 = Σ_{θ≠0}|ν̂(θ)|`,
i.e. weight `w(θ) ≥ 1` at every nonzero frequency. This covers `Σ|a_i|`,
the sawtooth bound `min(N, 1/(2‖θ‖))`, and any Weil/Kloosterman/Gauss
bound for `ν̂(θ)` inserted into either. It does **not** cover:
* the *exact* sharp weight `|S_N(θ)| = |sin πNθ / sin πθ|`, which is < 1
  when `‖Nθ‖` is small;
* *smooth windows* `Σ_n Φ(n/N)ν(n)`, whose weight
  `|W_N(θ)| ≈ N|Φ̂(N‖θ‖)|` is `O(N^{−A})` for `‖θ‖ ≥ N^{−1+ε}`.

For a smooth window, a single class of modulus `d > N` still costs O(1)
(about `d/N` frequencies within `1/N` of 0, each `|ν̂| = 1/d`, weight
≈ N), so smoothing gains nothing class by class. A gain needs the
high-level Fourier mass of ν to *avoid the 1/N-neighbourhood of 0*.

*Reduction for hit-pattern majorants (PROVED, routine).* If ν is a function
of `(n mod Q₀, x(n))` — Bonferroni, Selberg Λ² in the x-variables, and
every `P∘f` of §4 whose slices carry multiplicity one — then for Q₀ = 1, `ν̂(Σ_S h_ℓ/ℓ) = d_S Π_S 1̂_{F_ℓ}(h_ℓ)`,
so the shape of ν̂ on each Θ_S is fixed by the classes. The smooth
rounding is then `Σ_S |d_S| M_S` with
`M_S = Σ_{h} Π_S |1̂_{F_ℓ}(h_ℓ)|·|W_N(Σ_S h_ℓ/ℓ)|`, and the proof of
Theorem 2.3 goes through (with weights `log(3/(8p_ℓ⁺))` in place of
`log(1/(2p_ℓ⁺))`) provided

    M_S ≥ e^{−o(λ)} · Π_{ℓ∈S} (1 − p_ℓ)   for every S with s(S) > λ.     (2.6)

Indeed then `|d_S| Π_S 2p_ℓ ≤ e^{o(λ)} |d_S| M_S Π_S (8/3)p_ℓ`, and the
tails r₀, r₁ are `≤ e^{−λ+o(λ)}·R_Φ`. The total mass of the measure
`Σ_h Π|1̂_F(h_ℓ)| δ_{Σh_ℓ/ℓ}` is `A_S = Π a_ℓ ≥ Π(1−p_ℓ)`, and
`∫_0^1 |W_N| ≍ 1`; so (2.6) says this measure is not depleted, beyond a
factor `e^{−o(λ)}`, in the `1/N`-neighbourhood of 0. That is an
equidistribution statement for sums of reciprocals `Σ h_ℓ/ℓ` weighted by
the Fourier transforms of the forced classes, at denominators
`Π_S ℓ ≥ e^{λ}`. **(2.6) is CONJECTURE (H_eq)**; it
is not proved here. If it holds, smooth windows do not help hit-pattern
majorants. General (non-hit-pattern) majorants can reshape ν̂ inside Θ_S,
so they stay outside even under (H_eq).

## 3. Candidate (b): prime-only majorants

A *prime majorant* is ν (finite combination of classes) with ν ≥ 0 at all
primes and ν ≥ 1 at all primes of 𝒜; the bound is `Σ_{p≤N} ν(p)`.

**Lemma 3.1 (PROVED).** Let L be a common period of ν containing Q₀ and the
(finitely many) relevant slice primes, and assume
`|F_ℓ(c) ∖ {0}| < ℓ − 1` for all ℓ, c. If ν is a prime majorant, then
ν ≥ 0 on every reduced class mod L and ν ≥ 1 on every reduced class mod L
contained in 𝒜. (The converse fails only at the finitely many primes
dividing L, which are extra point constraints; they do not affect E*ν
below, and contribute `O(ω(L) max|ν|)` to `Σ_{p≤N}ν(p)`.)

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
level) also holds for E*: write `d'_i = m·s` with s the retained slice
part (level `≤ λ`, `> λ − Λ₀`) and m the rest; the E*-mean of a reduced
class mod d'_i is `1/φ(m)φ(s) ≤ 1/φ(s) ≤ e^{Λ₀−λ}·Π_{ℓ|s} ℓ/(ℓ−1)`, and the
last product is `≪ log λ` by Mertens (a set of primes with
`Σ log ℓ ≤ λ` has `Π ℓ/(ℓ−1)` at most that of the primes `≲ λ`).

*Proof.* The proof of Thm 2.5 uses only: a product measure across the CRT
coordinates; fibres `c ∈ R`; hit indicators independent Bernoulli with
parameters `p_ℓ(c) ≤ 1/4`; and `{c} × {x = 0} ⊆ 𝒜` with positive measure.
All four hold for E* with the starred data. ∎

For the families of ET-file Cor 3.4: `|F_ℓ(c)∖{0}| ≤ |F_ℓ(c)|`, and the
selector computation of Cor 3.4 holds for R* as well — c uniform on
`R* ⊆ (ℤ/Q₀)^×` projects to the uniform law on `(ℤ/q₀)^×`, so
`P(c ≡ b (q₀) | R*) ≤ 1/φ(q₀)` — giving
`p̄*_ℓ ≤ (ℓ/(ℓ−1))·Σ_{M=q₀ℓ}|𝒞(M)|(M/φ(M))/M`, the Cor 3.4 bound up to
`1 + O(1/ℓ₀)`. Also `log(φ(Q₀)/|R*|) = log(P/φ(P))` for the selector
(when P and Q₀ have the same prime factors). So the cap
`C(log N)^{3/4} + log(P/φ(P))` at level `A log N` is unchanged.

**Theorem 3.3 (primality is worth at most a factor λ^{O(1)}; PROVED).** Let
ν be an *integer* majorant (≥ 0 on ℤ) that is ≥ 1 only on `𝒜 ∩ 𝒫_z`, where
`𝒫_z = {n : (n, P(z)) = 1}` with `z ≤ e^λ` (this is how a sieve detects
primes), and assume ν has level ≤ λ *in the augmented system below*
(i.e. counting also the new slice primes ℓ ≤ z), primes dividing Q₀
are already handled by the selector, and the augmented probabilities
are ≤ 1/4. Then ν is a majorant of the prime-slice system obtained by adding
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
changes). Plug into (2.4): the profile term grows by
`C₄Σ_{ℓ≤z}ℓ^{−1−α}`, the truncated mass by `≤ log log z + O(1)` (still
`≪ λ³`), and G by `O(log λ)` (s_* may drop to log 5); the R-term is
unchanged. So the *upper bound* (2.4) on the saving grows by the
displayed amount; this is a comparison of bounds, not of optimal
savings. ∎

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
  `exp{−c(log N)^{3/5}(log log N)^{−1/5}}` (Vinogradov–Korobov type
  zero-free regions) even for a single fixed modulus d ≥ 3. Unconditionally,
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

Choosing `α = max(1, log(C₄μ̄/(19k)))` gives saving
`≤ 19k(1 + log⁺(C₄μ̄/(19k))) + O(log(μ̄+k)) + log(Q₀/|R|)`.

*Proof.* Given `n ≡ c (Q₀)`, `f = Σ_ℓ φ_ℓ(n mod ℓ)` with φ_ℓ ≥ 0
supported on `F_ℓ(c)`. So `P(f)` is a sum of terms each depending on at
most k slice coordinates, and so is `ν_c = E[P(f) | c, x]` (by
independence of the coordinates). Apply ET-file Prop. 2.4 with all weights
`s_ℓ = 1` and level λ = k (one nonempty band; empty bands are discarded in
Step 0, so the G-terms are those of G = 1), and average over c as in
Thm 2.5. ∎

*Consequence (for CRT means only).* Prop. 4.2 bounds the CRT mean
`E[P∘f]`, not an interval count. With witness moduli `≤ N^{O(1)}` the cubic supply gives
`μ̄ ≪ (log N)³`, so a degree-k method saves `O(k log log N)`. The second
moment (k = 2) saves `O(log log N)`: at best a power of log N, i.e.
θ = 0. To save `(log N)^θ` one needs moments of order
`k ≫ (log N)^θ/log log N` *if the bound is the CRT mean plus an error*;
and for θ > 3/4 Cor 2.5 caps every such evaluation with a per-frequency
error bound.

**What a non-CRT moment method would need (no theorem).** Elsholtz–Tao
(Thm 1.1) evaluate first moments `Σ_{p≤N} f_{I/II}(p)` up to constants by
divisor sums, Brun–Titchmarsh and BV. They state (Remark 1.3) that higher
moments `Σ_p f(p)^k` are out of reach *because the level of the relevant
divisor sums becomes too great* — the obstruction of Cor 2.5 in their
language. A non-CRT moment method for θ > 3/4 must therefore do one of
two things: use moments of order `≥ (log N)^{3/4+δ}/log log N` and count
those j-tuples of solutions sharing the same n directly (points on fibre
powers of the ES surface, dimension growing with j) to absolute accuracy
`N e^{−(log N)^θ}`; or use lower order and show that the true moments
`Σ_{n≤N} f(n)^j` deviate from their CRT values so that `Σ_n P(f(n))` is
far below `N·E[P∘f]`. No technique for either is known.

## 5. Numerical checks

`scripts/noncrt_checks.py` (output `data/noncrt/checks_m8.txt`, ~1 min):
* **Lemma 2.2, floating-point enumeration.** 40 random systems (Q₀ = 3, slice primes
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

  In this toy, per-frequency rounding acts like the coefficient budget
  multiplied by a factor ≈ 4–8 (of the order of Π f_ℓ over a typical
  monomial). Lemma 2.2 allows a factor up to `Π_S f_ℓ/(1−p_ℓ)`, which is
  not uniformly bounded but is `e^{o(level)}` for the forced-class families
  (`f_ℓ ≤ ℓ^{C+o(1)}` with C < 1 enters only through `s_ℓ`). Toy only.

## 6. Verdict and what remains

| candidate | result | label |
|---|---|---|
| (a) signed rounding, per-frequency (Gauss/Kloosterman/divisor exponential sums over the classes) | capped at `C(log N)^{3/4}` for dominant-prime-slice families (Thm 2.3, Cor 2.4–2.5); also removes ET-file's "slice primes ≤ N^{O(1)}" proviso | PROVED |
| (a″) per-frequency bounds with weight < 1 (exact `|S_N|`, smooth windows) | smooth windows, Q₀ = 1, hit-pattern majorants: capped under the equidistribution conjecture (H_eq) (2.6); exact `|S_N|`, Q₀ > 1 and general majorants open (§2.5) | CONDITIONAL / open |
| (a′) cancellation *between* frequencies | equivalent to counting `Σ_{n≤N}ν(n)` directly; squares give no set-level obstruction below θ = 1; dichotomy of §2.4: either large high-level Fourier mass or an interval count far below the CRT mean | open; no method |
| (b) prime-only majorants (Dirichlet measure, BV/BDH/EH/GRH level) | same LP limit up to `O((log log N)²)` (Thms 3.2, 3.3) | PROVED |
| (b′) prime error terms | unconditional prime equidistribution is *weaker* than the integer count at this precision (Remark 3.4) | Assessment |
| (c) moment/variance methods, CRT-evaluated | are CRT majorants (Prop 4.1), so capped by (a)/(b); degree k saves `O(k log log N)` (Prop 4.2): Chebyshev/2nd moment gives only θ = 0 | PROVED |
| (c′) moments evaluated by counting solution tuples | needs either order `≥ (log N)^{3/4+δ}/log log N` counted to absolute error `N e^{−(log N)^θ}`, or true moments deviating from CRT values (§4); ET Remark 1.3 already calls order ≥ 2 out of reach | open; no method |

**No non-CRT input tested here beats θ = 3/4.** The three natural
formalisations are capped, by proved theorems with the exact scope above.
What is left is precise. Each remaining route must do one of two things.
* Evaluate `Σ_{n≤N}ν(n)` (or `Σ_p`) directly, for a majorant with large
  high-level Fourier mass or with an interval count far below its CRT
  mean (§2.4), using cancellation across frequencies.
* Count high-order (`(log N)^{3/4+δ}`) correlations of ES solutions
  without CRT.
Neither is a known technique. The other open doors of the ET-file
(balanced moduli, the sequential world of Thm 2.7, non-selector R) are
untouched: Theorem 2.3 is proved for prime-slice systems only.

## 7. Replay

```
uv run --with scipy python scripts/noncrt_checks.py 8 > data/noncrt/checks_m8.txt   # ~1 min, < 1 GB
```

## 8. Inter-frequency cancellation: direct interval counts (follow-up 1)

### 8.1 The dichotomy, quantitatively

For a majorant ν put the **interval discrepancy**

    Δ_N(ν) = N·Eν − Σ_{n≤N} ν(n) = −Σ_{θ≠0} ν̂(θ) S_N(θ).          (8.1)

**Theorem 8.1 (PROVED; a restatement of Thm 2.3).** In the setting of
Theorem 2.3, suppose `Σ_{n≤N}ν(n) ≤ N e^{−s}`. Then for every λ ≥ s_*
and α > 0, at least one of the following holds:
* (H) `ε_λ(ν) > e^{−Φ̄(λ,α)}/4`: ν has Fourier mass above level λ of size
  `Σ_{s(S)>λ} A_S e^{−s(S)} > e^{−Φ̄}/4`;
* (D) `Δ_N(ν) ≥ N·[(|R|/(4Q₀)) e^{−Φ̄(λ,α)} − e^{−s}]`.

In particular, if `s ≥ Φ̄(λ,α) + log(8Q₀/|R|)` and (H) fails, then
`Σ_{n≤N}ν(n) ≤ N e^{−s} ≤ ½N·Eν`: the interval carries at most half of
its CRT share of ν. *Proof.* If (H) fails, (2.4) gives
`Eν ≥ (|R|/(4Q₀))e^{−Φ̄}`; subtract. ∎

For the Cor 2.5 families, `Φ̄(λ) ≤ Cλ^{3/4}`. So a direct count with
saving `s = (log N)^θ`, θ > 3/4, needs, at every level
`λ ≤ c s^{4/3}` (which is `≫ log N`): either Fourier mass `≳ e^{−Cλ^{3/4}}`
above level λ, or an interval share `≤ ½` of the CRT mean. Since the
majorant has `Eν ≥ (|R|/(4Q₀))e^{−Cλ^{3/4}}` in the second case, the
interval count must be a factor `≥ e^{s − Cλ^{3/4}}` *below* the CRT mean.

### 8.2 On [1,N], forced classes above N² are empty

**Lemma 8.2 (PROVED, from notes Thm 60.1).** Let n ≥ 1 and
`B = ⌊(n+1)/3⌋`. If n lies in a Case-B forced class of modulus M — i.e.
`M ≡ 3 (4)`, `D | ((M+1)/4)²`, `M | n + 4D` — then `M ≤ 8B² − 1`.

*Proof.* This is (60.1) ⇒ (60.9) of notes Theorem 60.1 (finite normal
form), which applies to every witness datum of every n ≥ 1. ∎

So for `M > M₀(N) := 8⌊(N+1)/3⌋²` every class of `𝓡(M)` (and every
Lemma 3.2 class, which is a subclass for n ≥ 1) misses [1,N] entirely. Its
CRT share `N|𝓡(M)|/M` is pure rounding, and `Σ_{M>M₀}|𝓡(M)|/M = ∞`.

**Corollary 8.3 (PROVED).** Let 𝒲 be any family of Case-B forced classes,
and let ν be a *hit-pattern majorant*: `ν(n) = G((1_W(n))_{W∈𝒲})` with
G ≥ 0 and `G(0) ≥ 1` (this covers Bonferroni, Selberg Λ² in the
indicators, and every `P∘f` of §4). Let 𝒲₀ be the classes of modulus
`≤ M₀(N)`, and `ν'(n) = G((1_W(n))_{W∈𝒲₀}, 0)`. Then:
* ν' is a hit-pattern majorant of the truncated avoider set `𝒜_{𝒲₀}`;
* `Σ_{n≤N} ν(n) = Σ_{n≤N} ν'(n)`.

*Proof.* The second claim is Lemma 8.2. For the first: ν' ≥ 0, and if
`n ∈ 𝒜_{𝒲₀}` then ν'(n) = G(0) ≥ 1. ∎

*Meaning.* For interval counts of hit-pattern majorants, classes of
modulus beyond `M₀ ≍ N²` give neither sieving power nor cost. The high
level λ ≫ log N that Theorem 8.1 requires must therefore come from
*products of many classes of modulus ≤ N²* — from k-fold coincidences of
witnesses on single integers n ≤ N, with `k ≥ λ/(2 log N)`. In the CRT
model those coincidences are independent. On [1,N] they are the actual
witness multiplicity, i.e. the Elsholtz–Tao `f(n)` and its correlations.
Lemma 8.2 removes the CRT mass above `M₀` from [1,N] entirely. §8.3
tests what happens between N and M₀.

### 8.3 Test: hit-count majorants on [1,N] versus CRT (EVIDENCE)

`scripts/noncrt_interval.py`, family: prime moduli `ℓ ≡ 3 (4)`,
`F_ℓ = 𝓡(ℓ)`, `H_Y(n) = #{ℓ ≤ Y : n mod ℓ ∈ F_ℓ}`. For each degree
k ≤ 10 it solves the LP `min E[P(H_Y)]` over `deg P ≤ k`,
`P ≥ 0` on `{0..80}`, `P(0) ≥ 1`. It does this twice: once for the empirical
law of H_Y on the chosen integers in [1,N] (an exact interval evaluation:
every inter-frequency cancellation is included) and once for the CRT law
(independent `Bern(|F_ℓ|/ℓ)`). Positivity is imposed only up to 80; this
relaxation helps both sides equally. Runs take ≤ 1 min each
(`data/noncrt/interval_*.txt`).

| N, set | Y | CRT mass μ | E_int H | void int | saving k=10: int / CRT |
|---|---|---|---|---|---|
| 3000, all n | 3000 | 8.01 | 7.61 | 0.0200 | 3.62 / 6.30 |
| | 8·10⁶ = M₀ | 30.47 | 9.75 | 0.0197 | 3.38 / 12.68 |
| 3000, non-squares | 3000 | 8.01 | 7.75 | 0.0020 | 4.72 / 6.30 |
| | 8·10⁶ | 30.47 | 9.93 | 0.0017 | 4.12 / 12.68 |
| 3000, primes | 3000 | 8.01 | 8.22 | 0 | 4.83 / 6.30 |
| | 8·10⁶ | 30.47 | 10.91 | 0 | 4.33 / 12.68 |
| 30000, primes | 30000 | 13.08 | 13.33 | 0.0003 | 5.18 / 8.04 |
| | 5.2·10⁶ | 28.87 | 16.96 | 0.0003 | 4.89 / 12.42 |
| | 3·10⁷ | 35.62 | 17.14 | 0.0003 | 4.88 / 13.41 |

Findings.
* For `ℓ ≤ N` the interval and the CRT agree in first moment, as they
  must, since `E_int H_N ≈ μ_N`.
* **For `ℓ ∈ (N, Y]` the interval receives only a small part of the CRT
  mass.** At N = 30000 (primes), raising Y from N to 3·10⁷ adds 22.5 to
  μ but only 3.8 to `E_int H`. The forced residues `−4D mod ℓ` avoid
  `[1,N]` (cf. Lemma 8.2, which is the extreme case).
* Consequently, at every degree 2 ≤ k ≤ 10 and every Y ≥ N, the exact
  interval value of the best hit-count majorant is **worse** than its CRT
  mean, often by a factor `e^{5}–e^{9}`. The interval saving is flat in Y
  for Y ≥ N. So for this natural family `Δ_N(ν) < 0`: the interval
  carries *more* than its CRT share. That is the opposite of branch (D)
  of Theorem 8.1.
* At small Y (≈ √N) the interval is slightly better than CRT for primes
  (3.36 vs 2.52, from the selector-like effect of primality). This is a
  bounded-level effect, inside Theorem 3.3's `O(log²λ)`.

### 8.4 A proved piece of the thinning, and the conjecture

**Proposition 8.4 (PROVED).** The number of pairs (n, (M,D)) with
`1 ≤ n ≤ N`, (M,D) a Case-B datum for n (Lemma 8.2), and *multiplier one*
(`n + 4D = M`), is at most `((N+1)/4)·Σ_{g≤(N+1)/4} τ(g)/g ≤ (N+1)(1+log N)²/4`,
uniformly in the size of M.

*Proof.* By notes (60.7)–(60.8) every datum has `D = gd`,
`(M+1)/4 = gu` with `d | g`. Multiplier one gives `n = 4g(u−d) − 1`. So
`1 ≤ n ≤ N` forces `1 ≤ u − d ≤ (N+1)/(4g)`, hence `g ≤ (N+1)/4`. Also
(g,d,u) determines (n,M,D). Count: g, then `d | g` (τ(g) ways), then
`u − d` (`≤ (N+1)/(4g)` ways). Finally `Σ_{g≤x}τ(g)/g ≤ (1+log x)²`. ∎

So on [1,N] the multiplier-one witnesses of *all* moduli together have
mean `≤ ¼(1+log N)²` per integer. (For M > N, a hit with multiplier
`a ≥ 2` needs `4D = aM − n > 2M − N > M`, i.e. a divisor D of `A²` above
`M/4 ≈ A`. Those hits are not controlled by this argument.)

**Conjecture 8.5 (interval thinning).** For the Case-B forced classes,
`(1/N) Σ_{n≤N} #{data (M,D) for n with M > N} ≪ (log N)²`. The CRT mass
of these classes up to `N^c` is `≍ (c³−1)(log N)³`.

*Assessment.* If 8.5 holds, the slice moduli above N carry only
`O((log N)²)` hit mass on [1,N]. The CRT picture, in which mass grows
cubically with the level, is then fictitious above N. So the high level
that branch (H) of Theorem 8.1 needs cannot come from large slice primes.
It can only come from products of many moduli `≤ N` (Cor 8.3 proves the
weaker cut-off `≍ N²`). This does **not** cap exact interval counts of
such products: the exact void of the moduli `≤ N` on [1,N] is
not known, and the CRT value there is `e^{−≍(log N)³}`.

### 8.5 A cap for exact interval counts of bounded degree (conditional)

**Proposition 8.6 (PROVED; Lagrange).** Let π be any probability law on
`ℤ_{≥0}`, for example the empirical law of `H(n)` on the chosen integers
in [1,N]. Let `y_0 < … < y_k` be integers ≥ 0 with `π(y_i) > 0`, and let
`ℓ_i` be the Lagrange basis at these nodes. Then every polynomial P of
degree ≤ k with `P ≥ 0` on `ℤ_{≥0}` and `P(0) ≥ 1` has

    E_π P(H) ≥ [ max_i |ℓ_i(0)| / π(y_i) ]^{−1}.

*Proof.* `1 ≤ P(0) = Σ_i ℓ_i(0)P(y_i) ≤ max_i(|ℓ_i(0)|/π(y_i))·Σ_i π(y_i)P(y_i)`. ∎

With the nodes of ET-file Lemma 2.2(c) (`k+1` points spaced
`≈ √(m/k)` within `√(km)` of `m := E_π H`), `|ℓ_i(0)| ≤ (4e√(m/k))^k`.
Hence:

**Corollary 8.7 (CONDITIONAL on the node hypothesis below).** Suppose that
on [1,N]

    (H_node(k))  π_int(y) ≥ e^{−C₀k}/√m  at the k+1 nodes above,

with `m = E_int H ≤ (log N)^{O(1)}`. Then every degree-k hit-count majorant
evaluated *exactly* on [1,N], with all inter-frequency cancellation
included, saves at most `(k/2) log(16e² m/k) + C₀k + ½ log m`. A saving
`(log N)^θ` therefore needs `k ≫ (log N)^θ / log log N`. So beating 3/4
by exact interval counts needs hit-count polynomials of degree
`≥ (log N)^{3/4+o(1)}`, i.e. control of k-fold witness coincidences on
single integers for k that large.

*Status of H_node.* It is a lower bound for the distribution of witness
counts near their mean, of local-limit type. It is not proved here. For a
Poisson-like H it holds with `C₀ = O(1)`. The witness count
behaves partly like a divisor function (ET Thm 1.8: `f(n)` is at least
`(log n)^{0.549}` for almost all n), so H_node is plausible but not
obvious. The LP values in §8.3 are the exact optimum over P of the bound
for the empirical law, so the table is a direct numerical check of the
conclusion for k ≤ 10.

### 8.6 Outcome of the follow-up

* The dichotomy is quantitative (Thm 8.1). Direct counts beating 3/4 need
  either Fourier mass `≳ e^{−Cλ^{3/4}}` above every level
  `λ ≤ c(log N)^{4θ/3}`, or an interval count a factor
  `e^{s − Cλ^{3/4}}` below the CRT mean.
* For hit-pattern majorants, classes above `M₀ ≍ N²` are inert on [1,N]
  (Cor 8.3, PROVED). Multiplier-one witnesses of all moduli have mean
  `≤ ¼(1+log N)²` (Prop 8.4, PROVED). Conjecturally all moduli above N
  carry only `O((log N)²)` (Conj 8.5).
* The natural structured family (polynomials in the forced-class hit
  count, degree ≤ 10) shows **no inter-frequency gain**. Its exact
  interval values are worse than its CRT means for every Y ≥ N, so
  `Δ_N < 0` (EVIDENCE, §8.3).
* For a named class, exact interval counts of degree-k hit-count
  majorants, there is a conditional cap. Beating 3/4 needs degree
  `≥ (log N)^{3/4+o(1)}` (Cor 8.7, conditional on H_node).
* No structured family was found with both large high-level Fourier mass
  and a favourable interval count. The door stays open only for
  majorants of degree `≥ (log N)^{3/4}` in the witness indicators, or for
  non-hit-pattern majorants (e.g. multiplicative/Halász-type weights on
  `(n+a)/4`, the a-frame route of ET-file §5.2, assessed at θ* ≈ 0.52 in
  its model).
