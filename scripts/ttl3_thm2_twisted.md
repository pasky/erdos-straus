# T-E: effective twisted spectral large sieve at ∞

**Status:** quantitative transfer of `ttl3_thm2_effective.md` (T-A), relative to its scalar analytic
estimates, the exact twisted trace identities, and the explicit Weil hypothesis (W) below.
Drappeau's Lemma 4.2 supplies (W) with unspecified absolute constants: it does **not** supply their
numerical values. Thus the formula below is explicit in those constants, not an unconditional
numerical certificate extracted from Drappeau alone. No character-dependent analytic constant remains.
Checked Dr pp. 9–14 (including rendered formulas), DI pp. 225–227, 257–261, and `ttl3_nebentypus.md`.

## 1. Statement, conventions, black boxes

Let `r|L`, let χ modulo r be even (not necessarily primitive), and use `σ∞=Id`, `μ(∞)=1/L`.
For `K≥1`, `N≥1/2`, `0<δ≤1/10`, and a supported on `N<n≤2N` (equally closed `[N,2N]`; R121B repair, m2), each of the following is bounded by

`K_LSχ(δ) (K² + √r L⁻¹ N^{1+δ}) ‖a‖₂²`.                                            (LSχ)

Use Dr §4.1.2 orthonormal bases and Fourier coefficients, and put `b_f(n)=√n ρ_f∞(n)`:

* `Hχ = Σ_{2≤k≤K, k even} Γ(k) Σ_{f∈B_k(L,χ)} |Σ_n a_n b_f(n)|²`.
* `Mχ,± = Σ_{f∈B(L,χ), |t_f|≤K} |Σ_n a_n √n ρ_f∞(±n)|²/cosh(πt_f)`.
* `Eχ,± = Σ_{b singular} ∫_{−K}^K |Σ_n a_n √n ρ_b∞(±n,t)|² dt/cosh(πt)`.

The Maaß sum includes exceptional parameters; there is no sum over characters. The continuous sum
runs over **χ-singular** cusps, with the standard Eisenstein normalization, not arbitrary rescalings.
In DI normalization the three quantities are respectively `4πHχ`, `4Mχ,+`, and `Eχ,+`;
the constant below also covers these. Indeed `W_{0,it}(4πny)=2√(ny)K_it(2πny)`;
for Eisenstein coefficients use `|Γ(1/2+it)|²=π/cosh(πt)`. The holomorphic conversion follows from
`ψ_f(n)=(4πn)^{k/2}ρ_f∞(n)`.

Our arithmetic convention is exactly Dr (4.2), including its easily missed conjugation:

`Sχ(m,n;c)=Σ_{d mod c,*} conjugate(χ(d)) e((m d̄+n d)/c)`, `L|c`.

Here `d̄d≡1 (mod c)`. With the opposite convention replace χ by its conjugate everywhere.
The precise accepted twisted Weil black box is: for absolute `C_W≥1`, `B_W≥0`, uniformly in
`r|c`, χ modulo r, and integral m,n,

`|Sχ(m,n;c)| ≤ C_W τ(c)^{B_W} (m,n,c)^{1/2} (cr)^{1/2}`.                            (W)

Dr Lemma 4.2 states exactly this dependence on the **modulus** `q₀=r`, with `≪` and `τ(c)^{O(1)}`.
It is `√r`, not r, `r^ε`, or a hidden level loss. One may induce from the primitive conductor f
and use `√f≤√r` instead. No primitivity or squarefreeness is used here.
Dr's preceding paragraph cites prime-modulus Weil via Knightly–Li, Theorem 9.3, and prime-power
arguments via IK §12.3. I have **not verified Knightly–Li's theorem itself** and do not assert the
suggested explicit `2^{ω(c)}` formula, nor assign numerical values to `C_W,B_W` on that basis.
The exact identities accepted are the standard twisted Petersson and weight-zero pre-Kuznetsov
identities underlying Dr (4.26), (4.27), with their convergence conventions. There is a fixed
normalization issue: with Dr (4.7) and his stated Petersson norm, the standard Petersson right side
is `4πΓ(k−1)√(mn)Σ_f ρ_f(m)conjugate(ρ_f(n))`; rendered (4.26) prints `4Γ(k−1)` instead.
Use the standard identity, not that literal factor. This does not change the large-sieve dependence;
the numerical margin covers it. Selberg's general congruence-subgroup 3/16 theorem is another
permitted black box (Step 9).

## 2. Explicit constant

With A, the cutoff, and growing-order integration-by-parts bound taken from T-A, define

`A=2^{10000}`, `s=δ/16`, `p=⌊2/s⌋`, `b=max(4,⌈B_W+1⌉)`,
`D_b(s)=(2b/s)^{b·2^{b/s}}`, `R_p=2^{100(p+1)}(p!)⁴`,
`Pχ(s)=A C_W R_p D_b(s)²(1+1/s)⁴`, `G(s)=(1+1/s)^{1/s}`,
`K_LSχ(δ)=2^{20} A⁴ Pχ(s)² G(s)²(1+1/s)⁴`.

Thus a convenient explicit envelope is

`K_LSχ(δ) ≤ exp(exp(B/δ))`, `B=400+64b+16 log(2+C_W)`.

This is deliberately much looser than T-A's `100`. The only replacements in its constant formula
are `D→D_b`, `P→Pχ`, and the fixed normalization/endpoint margin `2^{20}`. In particular **√r is
not inserted in Pχ**. Lemma 1.1 gives `τ(c)^j≤D_b(s)c^s` for every `j≤b`.
For example `p!≤p^p` gives
`log K_LSχ ≤ 10⁶+(10⁵/s)log(2/s)+4b·2^{b/s}log(2b/s)+2log C_W`.
For `s≤1/160`, this is at most `exp((25+4b+log(2+C_W))/s)`, which gives the displayed B.

## 3. Transfer ledger: every step of T-A

**Step 1 — Weil, gcd row sums, modulus sums.** Replace S by Sχ. The gcd row-sum calculation gives
`|Bχ(θ,c)|≤3 C_W τ(c)^{B_W+1} √r c^{1/2} N ‖b‖²`, where
`Bχ(θ,c)=Σ_{m,n}b_m conjugate(b_n)Sχ(m,n;c)e(2θ√(mn)/c)`.
Use `D_b` instead of D. Every elementary divisor/harmonic sum is unchanged, and the moduli are
`c∈Lℕ`, so replace q by L in every modulus-sum estimate. No factor counting singular cusps occurs:
the trace formula already contains their **total** positive continuous contribution.

**Step 2 — exercise (5.1).** Unchanged: the residue large sieve and Gaussian orthogonality contain
no character. Their constant is still 100. This is a bound on additive sums, not a twisted Weil use.

**Step 3 — Mellin separation, Dr Lemma 4.6 second bound.** Opening Sχ introduces only a unit
`conjugate(χ(d))` in the residue sum. Triangle inequality, Cauchy–Schwarz, and the permutations
`d↦d̄` remove it. The cutoff, two derivatives, Mellin bounds, and dyadic t-sums are identical:
`|Bχ(θ,c)|≤A(c+N+√(θcN))‖b‖²`. There is **no √r** here.

**Step 4 — Poisson off resonance.** For clarity, apply Cauchy–Schwarz in m to Bχ and open the two
residue sums, using δ for d and `α=δ̄`. The expanded expression has the factors
`conjugate(χ(δ₁))χ(δ₂)e((n₁δ₁−n₂δ₂)/c)` and phase
`(α₁−α₂)t/c + 2θ(√n₁−√n₂)√t/c` in the smooth m-sum.
These are Dr (4.22)'s factors `conjugate(χ(r₁))χ(r₂)` specialized to ∞ (dummy indices may differ).
For nonresonant Poisson frequency u, `|(α₁−α₂)/c−u|≥1/c`; the character is independent of t.
Consequently T-A's support check `4(√2−1)/√3<31/32`, reciprocal-derivative bounds, and all p
integrations by parts survive literally. The error is still `Σ_{u≠a}|f̂(u)|≤4R_p/c` for
`c≤N^{1−s}`. Bounding the character product in absolute value costs exactly 1.

**Step 5 — resonance.** Resonance means `α₁≡α₂ (mod c)`, hence `δ₁≡δ₂ (mod c)` because inversion
permutes units. Since `r|c`, their character values agree and
`conjugate(χ(δ₁))χ(δ₂)=1`. The remaining residue sum is the **ordinary Ramanujan sum**
`Σ_{δ mod c,*}e((n₁−n₂)δ/c)`, bounded by `(n₁−n₂,c)`.
It is not a twisted Ramanujan sum and incurs neither a Gauss-sum nor a conductor loss.
Thus T-A's bound on `|B|²`, including its `R_p cN` error, and the completion for
`N^{1−s}<c<N` are unchanged. In particular
`|Bχ(θ,c)|≤Pχ(s) θ^{−1/2} c^{1/2}N^{1/2+s}‖b‖²` for `0<θ<2`, `c<N`.
Here Pχ is a harmless enlargement of a constant independent even of (W).
Classical reality/symmetry must **not** be assumed: for even χ,
`conjugate(Sχ(m,n;c))=S_conjugate(χ)(m,n;c)` and
`Sχ(n,m;c)=S_conjugate(χ)(m,n;c)`.
Conjugating the whole quadratic form and coefficients therefore handles negative phases with the
same constants, uniformly over χ. Also `Sχ(−m,−n;c)=Sχ(m,n;c)`. These facts justify the sine/cosine
kernels and both signs of Fourier coefficients. Only Lemma 4.6's `λ=0` case is needed here.

**Step 6 — holomorphic Petersson.** Use Dr (4.26); even χ gives precisely the even weights `k≥2`.
There is no weight-one issue. Multiply by `(k−1)e^{−(k−1)/K}` and sum. The diagonal is the same
numerical multiple of `D_K≤2K²`, independent of r, χ, L. The Bessel kernel `E_K`, its ξ-weight,
angular splitting, and Δ choices are exactly T-A's. Only the `c>N²` Weil range acquires √r.
One may upper-bound all three **off-diagonal** ranges by √r times their old majorants, obtaining
`|Fχ(c)|≤A Pχ(s) √r c^{−s}N^{1+5s}‖a‖²`.
Summing `L|c` and removing the exponential spectral weight gives, up to the already reserved fixed
normalization factor, `A²Pχ(s)(1+1/s)(K²+√r L⁻¹N^{1+5s})‖a‖²`.
The diagonal must not be multiplied by √r. T-A's correction of DI's 2s to 3s remains necessary.

**Step 7 — Gaussian Maaß/Eisenstein.** Dr (4.27) with weight κ=0 has the identical H and I kernels;
χ occurs only inside Sχ. The `1/(4π)` on the continuous term is a fixed normalization factor.
Use the same Gaussian multiplier, same local lower bounds, and same two formulas for Φ.
In T-A's four ranges, with common multiplier `A Pχ(s)‖a‖²`, the majorants become

* `c>N²`: `√r τ(c)^{B_W+1}c^{−1/2}N²`.
* `N<c≤N²`: `N`.
* `N/K²<c≤N`: `Ke^{−K²}N²/c+c^{−1/2}N^{3/2+s}`.
* `c≤N/K²`: `Ke^{−K²}N²/c+K²c^{1/2}N^{1/2+s}`.

Only the first range uses (W); there its multiplier can be taken as `A C_W` instead of `A Pχ`,
so absorbing its divisor power uses the D_b already budgeted in Pχ, not an extra unbudgeted factor.
With `X=N/L` and `R=√r`, summation therefore gives
`Σ_{L|c}|F_K,χ(c)|/c ≤ A²Pχ(s)(1+1/s)[R K X N^{2s}+K²X²e^{−K²}]‖a‖²`.
Retaining the conductor-free exponential term makes the next step particularly transparent.
The spectral diagonal remains a numerical multiple of K³, not R K³.

**Step 8 — enlargement and partial summation.** Apply the bound for the nondecreasing weighted
spectral mass W at `U=K+X^s` (U is not the level). T-A's Gaussian absorption G(s) is unchanged:
`W(K)≤16A³Pχ(s)G(s)(1+1/s)[K³+R K X N^{3s}]‖a‖²`, before fixed normalization margins.
For `X≥1`, use `X≤N`, `R≥1`; for `X<1`, use `X²≤X`. No r-dependent enlargement is required.
Partial summation costs at most 8 and gives `K²+RXN^{3s}(1+log K)`.
The large-K case still works: `R/L≤1` because `r|L`, so for `K>N`,
`RXN^{3s}log(K/N)≤K N^{3s}≤K²`; `log N` costs `s⁻¹N^s` as before.
The resulting exponent is 4s. It would be incorrect to multiply the whole untwisted large-sieve
inequality by √r: that would unnecessarily destroy the uniform K² term.

**Step 9 — exceptional eigenvalues.** Selberg 3/16 applies to this space. Indeed χ(d)=1 on Γ₁(L),
so a weight-zero (Γ₀(L),χ) cusp form is a cusp form on the congruence subgroup Γ₁(L).
Finite-index restriction multiplies its norm by the index, preserves cuspidality and eigenvalue,
and introduces no constant into an eigenvalue bound. Thus `λ=1/4−σ²≥3/16`, `σ≤1/4`.
This is the general congruence-subgroup theorem, not an inference from DI's trivial-character
Γ₀(L) statement alone. Alternatively T-A's noncircular limiting proof transfers: (W) adds only a
fixed factor `C_W√r` when n,L,r are held fixed as Y→∞; divisor absorption handles B_W, and the
geometric exponent is still `1/2+v`. The real/continuous and holomorphic bounds suffice beforehand.
Now `cosh(πt_f)=cos(πσ)≥1/√2`; the same positive Gaussian lower bound on `[1,2]` applies.
Repeat Steps 7–8 including the positive exceptional atoms. No spectral-gap effectiveness constant,
Fourier-coefficient lower bound, or factor `[Γ₀(L):Γ₁(L)]` enters K_LSχ.

**Step 10 — endpoints/envelope.** Extend coefficients by zero to `[1,2]` when `1/2≤N<1`, as in
T-A, at cost less than 3. Since `5s≤δ`, the holomorphic and spectral exponents fit (LSχ).
The `2^{20}` reserve covers endpoints and the fixed Dr/DI normalization factors described above.

## 4. Remaining qualifications

* Dr's transposition sketch alone is not a numerical proof; Steps 4–5 and 7–8 above supply the
  χ-specific cancellation and conductor accounting. The scalar cutoff/kernel estimates are imported
  from T-A, not independently replaced by the word “identical”. All its stated repairs remain in force.
* The genuine missing numerical arithmetic input is a verified choice of `C_W,B_W` in (W).
  Providing it immediately makes the displayed B numerical. No unverified Knightly–Li constants
  are silently used. For squarefree odd r and `L=4dr²`, the same result holds without further changes.
* This audits weight zero/even χ at ∞, not arbitrary singular cusps, odd weight, or Lemma 4.6's
  damped `λ>0` extension. No such extension is needed for the stated large sieve.
