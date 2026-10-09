# Effective DI Theorem 2 at ∞ (T-A)

This is a quantitative proof, not just an effectiveness assessment. References are journal pages of DI.
Only the trace identities and Weil's bound are arithmetic/spectral black boxes. Several literal intermediate
claims in DI need the repairs recorded below. No assertion of the asymptotic formula (5.2) is needed.

## 1. Statement and constants

Use DI's orthonormal bases and Fourier coefficients (1.7), (1.15), (1.17), pp. 225–227;
`σ∞ = 1`, `μ(∞) = 1/q`, and `S∞∞(m,n;c) = S(m,n;c)` for `c ∈ qℕ` (pp. 223–224).
For `q ≥ 1`, `K ≥ 1`, `N ≥ 1/2`, and complex `a` supported on `N < n ≤ 2N`, each of

* `H = Σ_{2≤k≤K, k even} (k−1)!/(4π)^{k−1} Σ_j |Σ_n a_n n^{−(k−1)/2} ψ_jk(∞,n)|²`,
* `M = Σ_{|κ_j|≤K} |Σ_n a_n ρ_j∞(n)|²/cosh(πκ_j)`,
* `E = Σ_cusps b ∫_{−K}^K |Σ_n a_n n^{ir} φ_b∞n(1/2+ir)|² dr`

is at most `K_T2(δ)(K² + q⁻¹N^{1+δ})‖a‖²`, for `0 < δ ≤ 1/10`.
The exceptional parameters are included in M. An explicit, deliberately extravagant choice is

`A = 2^{10000}`, `s = δ/16`, `p = ⌊2/s⌋`,
`D(s) = (8/s)^{4·2^{4/s}}`, `R_p = 2^{100(p+1)}(p!)⁴`,
`P(s) = A R_p D(s)²(1+1/s)⁴`, `G(s) = (1+1/s)^{1/s}`,
`K_T2(δ) = A⁴ P(s)² G(s)²(1+1/s)⁴ ≤ exp(exp(100/δ))`.

All constants below are numerical. A single occurrence of A in a bound generously dominates the
fixed numerical factors in that step; it is not an unspecified implied constant. In particular there
is no level-dependent test function. The cutoff is exactly Lemma 1.3 of EXCEPTIONAL_TYPEI_LOGLOG3.md.
We first work with `N ≥ 1`; all arguments also allow the closed interval `[N,2N]`.

## 2. Arithmetic and Proposition 3

**1. Weil and elementary sums (DI (1.25), (2.17), pp. 229, 243).**
Write `B(θ,c) = Σ_{m,n} b_m conjugate(b_n) S(m,n;c)e(2θ√(mn)/c)`.
Weil and the row-sum bound give
`|B(θ,c)| ≤ 2τ(c)² c^{1/2}N‖b‖²`.
Indeed, expand a gcd bound over divisors of c and use
`#{n ∈ [N,2N]: d|n} ≤ 3N/d` when this set is nonempty; changing 2 to 3 covers closed endpoints.
For the original half-open interval the factor 2 suffices. We use 3 henceforth.
Lemma 1.1 gives `τ(c)^j ≤ D(s)c^s` for `j ≤ 4`.
Other sums used below, with their constants, are
`Σ_{h≤N}(h,c)/h ≤ τ(c)(1+log N)`,
`1+log N ≤ (1+1/s)N^s`, `Σ_{q|c}c^{−1−s} ≤ q⁻¹(1+1/s)`.
The first follows from `(h,c) ≤ Σ_{d|c,d|h} d`; the others follow by integration or Lemma 1.2.
For `X>0`, `a>1`, also
`Σ_{q|c,c>X}c^{−a} ≤ (1+1/(a−1))q⁻¹X^{1−a}` and
`Σ_{q|c,c≤X}c^{−1/2} ≤ 2q⁻¹√X`.
These inequalities remain valid when the indicated sums are empty.

**2. An explicit proof of the exercise (5.1), p. 255.**
For `T>0`, enlarge the reduced residue sum to all residues and majorize the interval integral by
`e∫_ℝ exp(−(t/T)²)dt`. Orthogonality and the Gaussian Fourier transform give a matrix supported on
`m ≡ n (mod c)` with entries `e√π cT exp(−T²log²(m/n)/4)`.
Since `|log(m/n)| ≥ |m−n|/(2N)`, its absolute row sums are at most
`e√π cT[1+2Σ_{h≥1} exp(−(Tch/(4N))²)] ≤ 100(cT+N)`.
Thus (5.1) holds with 100, without a logarithm, and with no dependence on q or any tolerance.

**3. Mellin separation (DI p. 256, (1.26)).**
Insert the fixed η at `√(mn)/N`; on `Re z=1` its Mellin transform is
`M(1+it)=∫η(x)e(2θNx/c)x^{it}dx`.
The elementary second-derivative integral estimate, applied on `[3/4,9/4]`, and two integrations
by parts outside `|t| ≤ 32πθN/c+1`, give respectively
`|M(1+it)| ≤ 2^{200}(1+|t|)^{−1/2}` and `|M(1+it)| ≤ 2^{200}|t|^{−2}`.
For completeness the estimates use `f''(x)=−t/x²` in the first case; in the second,
`|f'(x)| ≥ |t|/5` and `|f^{(j)}(x)| ≤ 4^j(j−1)!|t|`, for `j=2,3`.
The usual second-derivative estimate follows by removing `|f'|≤√|t|` (length at most
`11/√|t|`) and integrating once on its two complementary intervals.
The norms of η through order 2 are below `2^{40}`, so the stated numerical bounds suffice.
Apply Step 2 to the separated sums, use Cauchy–Schwarz for the two residue permutations,
and sum dyadic t-intervals. The sums of `2^{−j/2}` and `2^{−j}` are below 4 and 2.
This proves `|B(θ,c)| ≤ A(c+N+√(θcN))‖b‖²` for every `θ>0`.
Only the fixed η, its first two derivatives, and the displayed numerical constants occur here.

**4. Growing-order integration by parts (DI p. 257).**
For `c ≤ N^{1−s}` and `0<θ<2`, Cauchy–Schwarz, the definition of S, and Poisson give DI's
`f̂(u)=∫η(t/N)e((a−u)t+b√t)dt`, where `a=(α₁−α₂)/c`,
`b=2θ(√m₁−√m₂)/c`. If `u≠a`, then `|a−u|≥1/c` and, on the actual support,
`|b/(2√t)|/|a−u| ≤ 4(√2−1)/√3 < 31/32`.
This support check matters: the larger unspecified support printed in DI does not justify its
claimed derivative separation. Our η does.
With `x=t/N`, divide the phase derivative by `N|a−u|`. Its reciprocal g has
`‖g^{(j)}‖∞ ≤ 2^{20(j+1)}j!`: Cauchy's estimate on complex discs of radius `2⁻¹²`
works because the above separation remains at least `1/64` there.
Expanding p applications of `v ↦ (gv)'` produces at most `(p+1)!` terms. The total derivative
order is p, the products of derivative factorials are at most `(p!)²`, and
`‖η^{(j)}‖∞ ≤ 8e¹⁶·36^j(j!)²`. Consequently
`|f̂(u)| ≤ R_p N(N|a−u|)^{−p}` and
`Σ_{u≠a}|f̂(u)| ≤ 4R_p N(c/N)^p ≤ 4R_p/c`.
The last inequality uses `sp ≥ 2−s` and `c ≤ N^{1−s}`; no hidden constant depends on p.

**5. The resonant term and completion of (1.27), pp. 256–257.**
If `u=a`, the residue pairs coincide. Summing the remaining residue gives the Ramanujan sum
`|S(0,m₁−m₂;c)| ≤ (m₁−m₂,c)`.
For `h=m₁−m₂≠0`, one integration by parts gives
`|f̂(a)| ≤ 2^{50} min(N,cN/(θ|h|))`; for h=0 use `2N`.
Here `√m₁−√m₂=h/(√m₁+√m₂)`, and the derivative of √t has one sign.
Cauchy–Schwarz for shifts of b and Step 1 now give
`|B|² ≤ 2^{100}[R_p cN + θ⁻¹cN τ(c)(1+log N)]‖b‖⁴`.
In the first term the two residue sums have at most `c²` terms and
`(Σ|b_m|)² ≤ 2N‖b‖²`; this explains why the nonresonant error is `cN`, not `c²N`.
Since `c<N`, replace `τ(c)(1+log N)` by `D(s)(1+1/s)N^{2s}`.
Taking square roots proves
`|B(θ,c)| ≤ P(s) θ^{−1/2} c^{1/2}N^{1/2+s}‖b‖²`.
For `N^{1−s}<c<N`, Step 3 gives the same bound (with room to spare).
This proves the required effective Proposition 3. Negative phases follow by conjugation and
interchanging m,n, since classical S is real and symmetric.

## 3. Holomorphic spectrum

**6. Kernel and the Δ split (DI (5.3)–(5.5), pp. 258–259).**
Petersson (4.4), summed with `e^{−(k−1)/K}(k−1)`, has diagonal
`D_K=Σ_{l≥1}(2l−1)e^{−(2l−1)/K} ≤ 2K²` and off-diagonal `πΣ_{q|c}F(c)/c`.
Its exact kernel is
`E_K(x)=½sinh(2/K)∫₀¹ ξxJ₀(ξx)[cosh²(1/K)−ξ²]^{−3/2}dξ`.
This identity can be checked by inserting the power series for J₀ and integrating, or by the
absolutely convergent Bessel generating series with parameter `e^{−1/K}`; it introduces no bound.
Set `D₀(c,N)=c^{1/2}N` for `c>N²`, `c` for `N≤c≤N²`, and `√(cN)` for `c<N`.
Steps 1, 3, 5 imply, for `0<ξ,cos v≤1`,
`|B(ξcos v,c)| ≤ 3P(s)(ξcos v)^{−1/2}(cN)^s D₀(c,N)‖b‖²`.
Split the angular J₀ integral at Δ and integrate the remaining part once, exactly as on p. 258.
Writing `w(ξ)=sinh(2/K)[cosh²(1/K)−ξ²]^{−3/2}`, the bounds needed are
`∫₀¹w(ξ)ξ^{1/2}dξ ≤ 32`, `∫₀¹w(ξ)ξ^{−1/2}dξ ≤ 32`,
`∫₀^Δ(cos v)^{−1/2}dv ≤ 4Δ`, `∫_Δ^{π/2}√(cos v)/sin²v dv ≤ 4/Δ`.
The ξ bounds follow by splitting at 1/2 and using `∫₀¹w(ξ)ξdξ=2e^{−1/K}≤2`.
For `Δ≤1` the boundary term is also at most `4/Δ`; at `Δ=π/2` it is exactly zero.
Factors √(mn) in the first kernel are separated into coefficients, costing at most `2N`.
Thus the three pieces together are bounded by
`A P(s)(cN)^s D₀(c,N)(ΔN/c+Δ⁻¹)‖a‖²` when `Δ≤1`.
For `Δ=π/2` only the first term is present.
Choose `Δ=√(c/N)` if `c<N`, otherwise `π/2`. This yields
`|F(c)| ≤ A P(s)c^{−s}N^{1+5s}‖a‖²` for `s<1/4`.
Indeed for `c<N` the exponent needed is `1+3s`; for `N≤c≤N²` it is `1+5s`;
for `c>N²` use `c^{2s−1/2}≤N^{4s−1}`.
Summing with Step 1 and removing the exponential weight (cost at most e for `k≤K`) proves
`H ≤ A²P(s)(1+1/s)(K²+q⁻¹N^{1+5s})‖a‖²`.

## 4. Real Maaß spectrum, continuous spectrum, then exceptions

**7. Gaussian identity and all four modulus ranges (DI pp. 260–261).**
Apply (4.8) with the Gaussian multiplier `t sinh(πt)e^{−(t/K)²}`. Its diagonal is a numerical
multiple of `∫t²e^{−(t/K)²}dt=√πK³/2`.
For real `|r|≤K`, the integrated H-kernel is at least `2⁻²⁰(1+|r|)`:
restrict t to `[|r|,|r|+1]` if `|r|≥1`, otherwise `[1,2]`, and use the elementary exponential
bounds for sinh and cosh. The Gaussian on these intervals is at least `e⁻⁴`.
This avoids any assertion about the lower Gaussian envelope for arbitrarily large r.
Exceptional contributions are nonnegative, so they can initially be discarded.
DI's exact Gaussian integrations and one integration by parts give
`Φ(x)=√π iK³∫₀∞ ξe^{−(Kξ)²}sinhξ sin(xcoshξ)dξ`,
`xΦ(x)=√π iK³∫₀∞ e^{−(Kξ)²}(1−ξtanhξ−2K²ξ²)cos(xcoshξ)dξ/coshξ`.
Let `F_K(c)=Σ conjugate(a_m)a_n S(m,n;c)xΦ(x)`, `x=4π√(mn)/c`.
Steps 1, 3, 5 give the following bounds, each with multiplier `A P(s)‖a‖²`:

* `c>N²`: `τ(c)²c^{−1/2}N²` (the P(s) factor is unnecessary here).
* `N<c≤N²`: `N`.
* `N/K²<c≤N`: `Ke^{−K²}N²/c + c^{−1/2}N^{3/2+s}`.
* `c≤N/K²`: `Ke^{−K²}N²/c + K²c^{1/2}N^{1/2+s}`.

Details controlling the constants: in the last two ranges split ξ at 1. On `[0,1]`,
`θ=coshξ<2`, so Step 5 applies. The two Gaussian masses are bounded by `32` and `32K²`.
On `[1,∞)`, use Step 3 and `coshξ≤e^ξ`; its first integral is at most `32Ke^{−K²}`,
and its second at most `32K³e^{−K²}`. For the latter use `c≤N/K²` to replace
`K³N` by `KN²/c`. These estimates follow from `ξ≤(ξ²+1)/2` and Gaussian integration;
all constants are independent of K. In the first two ranges the full Gaussian masses are at most 32.
The exponent of τ in the first range is bounded using D(s), not concealed in a modulus-dependent constant.
Step 1's sum formulas therefore give, with `X=N/q`,
`Σ_{q|c}|F_K(c)|/c ≤ A²P(s)(1+1/s)[KXN^{2s}+K²X²e^{−K²}]‖a‖²`.

**8. Enlargement and partial summation (DI p. 261), with explicit absorption.**
Let W(K) be the real discrete plus continuous spectral mass weighted by `1+|r|` on `|r|≤K`.
Step 7 yields `W(K) ≤ A³P(s)(1+1/s)[K³+KXN^{2s}+K²X²e^{−K²}]‖a‖²`.
W is nondecreasing; `W(K)/K` need not be. Apply this inequality at `L=K+X^s`.
For `X≥1`, `sup X exp(−X^{2s}/2) ≤ G(s)` and `Lexp(−L²/2)≤1`;
for `X<1`, use `X²≤X` directly. Also
`L³≤4(K³+X^{3s})`, `X^{3s}≤1+X`, and `X^{1+s}≤X max(1,N^s)`.
Consequently `W(K) ≤ 16A³P(s)G(s)(1+1/s)[K³+KXN^{3s}]‖a‖²`.
Stieltjes partial summation with `1/(1+r)` gives an additional numerical factor at most 8 and
`K²+XN^{3s}(1+log K)`.
If `K≤N`, use `log K≤s⁻¹N^s`; if `K>N`, write `log K=log N+log(K/N)` and use
`XN^{3s}log(K/N)≤KN^{3s}≤K²`. Thus the real and continuous conclusions hold with exponent 4s
and constant `128A³P(s)G(s)(1+1/s)²`, which is below the stated K_T2.

**9. Exceptional spectrum: a noncircular repair of the Gaussian positivity issue.**
For imaginary r approaching `i/2`, the lower bound for the integrated H itself in Step 7 is NOT
uniform. First prove `|Im κ_j|≤1/4` by DI §6.2, using only the real/continuous and holomorphic
results already established, not the exceptional conclusion of Theorem 2.
Here are sufficient details of this limiting argument. In (1.19), take `m=n` and `φ(x)=η(Yx)`.
Weil and Step 1 give `|geometric side|≤C(n,v)Y^{1/2+v}` for `0<v≤1/10`, where one may take
`C(n,v)=100(100n)^{1+v}(2/v)^{2^{1/v}}`.
The Bessel series and four integrations by parts in log x give
`|φ̂(r)|≤A(1+log Y)(1+|r|)^{−9/2}` for real r and
`|φ̃(k−1)|≤A(2/Y)^{k−1}/Γ(k)` for even `k≥2`, `Y≥10`.
These constants use only the first four derivatives of η. The log factor allows r=0.
(The gamma modulus here follows exactly from `|Γ(1+it)|²=πt/sinh(πt)`.)
The real/continuous bounds with a fixed tolerance, say 1/10, and the holomorphic bound therefore
make their total contribution `O_{n,q}(1+log Y)`.
For each exceptional `κ=−iσ`, the leading term of the same Bessel series has a common sign and
`|φ̂(κ)|≥c(σ)Y^{2σ}` for all sufficiently large Y; there are finitely many such κ at fixed q.
In fact (1.22) as printed gives a negative sign, while p. 263 uses the opposite convention;
only the common sign is needed: take the absolute value of the entire exceptional sum.
Choose a nonzero positive-index Fourier coefficient, let Y tend to infinity, and then let v tend to zero.
This proves `σ≤1/4`. No bound on that coefficient or on a convergence threshold enters our constant.
Now `cos(πσ)≥1/√2`; restricting the Gaussian integral to `[1,2]` proves the same `2⁻²⁰`
lower bound as in Step 7, with weight `1+σ`. Repeat Steps 7–8 including these positive atoms.
This establishes M including exceptions, without circularly invoking the full Theorem 2.

**10. Endpoint and numerical envelope.**
For `1/2≤N<1`, extend the coefficients by zero to `[1,2]`, use the closed-interval proof at N=1,
and multiply its bound by at most `2^{1+δ}<3`. The unused margin in K_T2 covers this.
Since `5s≤δ`, both spectral exponents obtained above are admissible.
Using `p!≤p^p`, the explicit formula satisfies
`log K_T2 ≤ 10⁶ + (10⁵/s)log(2/s) + 20·2^{4/s}log(8/s) ≤ exp(6/s)`
for `s≤1/160`. Thus `K_T2≤exp(exp(96/δ))≤exp(exp(100/δ))`.

## Gaps/caveats

* No unresolved tolerance-dependent constant remains at ∞; this does not audit arbitrary cusps or characters.
* DI p. 257's derivative separation needs the actual cutoff support checked; Step 4 supplies that check.
* DI p. 259 prints `(cN)^sN ≤ c^{−s}N^{1+2s}` for `c<N`; the valid exponent is 3s.
  Its final 5s estimate survives unchanged. “By Proposition 2” there refers to Proposition 3.
* The diagonal `D_K=K²/2+O(1)` cannot uniformly be replaced by `K²/2+O(q⁻¹N^{1+ε})` as in (5.2).
  Retaining `D_K≤2K²` repairs the large-sieve proof, which needs no such asymptotic.
* The Gaussian lower estimate and the monotonicity sentence on pp. 260–261 must be restricted/rephrased
  as in Steps 7–9. In particular, the exceptional case requires the noncircular gap argument above.
  The opposite signs for the transform in (1.22) and on p. 263 do not affect that limiting argument.
* The limiting Selberg argument uses constants depending on fixed n,q,σ only to determine an exponent;
  none is imported into K_T2. Exact trace identities include their usual convergence interpretation.
