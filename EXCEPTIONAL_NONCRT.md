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
