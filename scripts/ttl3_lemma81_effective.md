# Effective DI Lemma 8.1 and the preliminary bound for Theorem 7

**Status:** proved relative to the stipulated Theorem 2, Theorem 14, exact Kuznetsov identity,
and Selberg's `0 < σ = iκ ≤ 1/4`. Constants below are deliberately very wasteful.
DI page numbers refer to the journal. Two uniformity statements in the earlier Assessment
need repair, as does the support bookkeeping in the printed proof.

## 1. Statements and constants

Let `0 < δ ≤ 1/10`, `e = δ/4`, and set

`D(e) = (2/e)^{2^{1/e}}`, `A = 2^{16384}`,

`K₁(δ) = A δ⁻² [1 + K_T2(e) + D(e)K14(e)]`,

`c(δ) = A δ⁻² [1 + K_T2(e)]`.

For the definition of `S` and `S*` in LOGLOG3 §2, these constants give

**(P1)** `S*(Q,Y,N) ≤ K₁(δ)(QNY)^δ(Q + N + Y)N`;

**(P2)** `S(Q,Y,N,0;I) ≤ c(δ)∫ S(πNY/Q,Y,N,t;I)dt/(1+t⁴)`
`                         + c(δ)(YN)^δ(Q + N + NY/Q)N`.

Here `Q,Y,N ≥ 1`, `I = (N,N₁]`, `N₁ ≤ 2N`. If `πNY/Q < 1`, the right-hand `S`
requires the natural extension of its defining finite level sum to positive `Q`.
Alternatively, in this range the error term alone bounds the left side; thus no evaluation
of an out-of-domain `S` is needed. This is a minor domain correction to LOGLOG3's formulation.
For real `N`, use `‖1_I‖² ≤ 2N`, not necessarily `≤ N`.

## 2. Fixed cutoffs and numerical transform estimates

**2.1. Cutoffs.** Use the explicit `η` of LOGLOG3 Lemma 1.3 and put

`Ψ(u) = η(3u−2)`, `φ(x) = Ψ(Yx)`, `f(q) = η(q/Q)`.

Thus `supp Ψ ⊂ [11/12,17/12]`, `Ψ = 1` on `[1,4/3]`, and
`supp f ⊂ [3Q/4,9Q/4]`, `f = 1` on `[Q,2Q]`.
Replacing DI's pictured plateau by this narrower one is permissible and important.
For `D_x = x∂_x`, all supremum and `dx/x` integral norms of
`D_x^j Ψ`, `D_x^j η`, `0 ≤ j ≤ 12`, are less than `H = 2^{512}`.
This follows directly from `8e^{16}36^j(j!)²`, the affine chain rule, and
`D_x^j = Σ_{a≤j} {j\brace a}x^a∂_x^a`, using `{j\brace a} ≤ j^j`.
These bounds are absolute, independent of every problem parameter.

**2.2. Transform ledger.** Write `φ_t(x) = x^{it}φ(x)`, `L_Y = 1+log Y`,
and `B = 2^{2048}`. For `Y ≥ Y_abs = 2^{32}` the following bounds hold:

(a) `|φ̂_t(r)| ≤ B(1+|t|)^4 L_Y(1+|r|)⁻⁴`, `r ∈ ℝ`;

(b) `|φ̃_t(l)| ≤ B(1+l)⁻⁴`, for positive odd integers `l`;

(c) `φ̂(−iσ)/cos(πσ) ≥ Y^{2σ}/64`, `0 < σ ≤ 1/4`;

(d) `|φ̂_t(−iσ)| ≤ B Y^{2e}L_Y`, `0 < σ ≤ e`;

(e) for `e < σ ≤ 1/4`,

`φ̂_t(−iσ) = [π4^σ/(2sin(πσ)Γ(1−2σ))] φ*(2σ−it) + R_σ(t)`,

`|R_σ(t)| ≤ B/e`, `|φ*(2σ−it)| ≤ 2Y^{2σ}`,

where `φ*(s) = ∫ φ(x)x^{−s}dx/x`. No constant here depends on `Q,c,N,δ`;
the displayed `e⁻¹` and `Y^{2e}` are the only split-dependent factors.

Here are quantitative derivations, including the delicate origin. DI (1.21)–(1.23),
p. 228, define

`φ̃(l)=∫J_l(x)φ(x)dx/x`,
`φ̂_print(r)=π/(2i sinh πr)∫[J_{2ir}(x)−J_{−2ir}(x)]φ(x)dx/x`,
`φ̌(r)=(4/π)cosh(πr)∫K_{2ir}(x)φ(x)dx/x`.

Only the first two occur in the same-sign formula (1.19); no estimate for `φ̌` is used.
**Sign convention:** (8.1) has `πi/(2sinh πκ)`, the negative of printed (1.22).
Throughout this note `φ̂ := −φ̂_print`, the convention with the positive exceptional
main term used in §8. This does not require assuming an erratum to the exact identity:
in (8.7) its exceptional side then equals the *negative* arithmetic side plus error;
the second trace formula introduces the same minus, and the two cancel. For (P1)
the arithmetic side is taken in absolute value anyway.
Use the absolutely convergent series

`J_ν(x) = (x/2)^ν Σ_{k≥0} (−x²/4)^k/[k!Γ(k+1+ν)]`.

For `|Re ν| ≤ 1/2`, the factors `|k+ν| ≥ k/2` bound the series tails by
exponential series. On `ν ∈ [−1/2,1/2]`, differentiation costs at most
`2+2log(k+1)+|log(x/2)|`, since `|ψ(u)| ≤ 2` for `1/2 ≤ u ≤ 3/2`
and `ψ(u+k)=ψ(u)+Σ_{h<k}(u+h)⁻¹`.
Consequently the exceptional kernel's remainder after its `k=0` term is at most
`2^{16}x^{2−2σ}(1+|log(x/2)|)` for `0<x≤1`, uniformly down to `σ=0`.
The subtraction of the two orders is essential: divide their difference by `σ`
*after* applying the mean-value theorem, not before bounding each term.
After integration this remainder is at most `2^{20}L_Y Y⁻³ᐟ²`.
The same cancellation for real `|r|≤1` gives a main kernel bound
`2^{16}(1+|log(x/2)|)` and a remainder bound `2^{16}x²(1+|log(x/2)|)`.
For example the needed order derivatives on `ν ∈ i[−2,2]` follow from
`ψ(1+ν)=−γ+Σ_{h≥1}ν/[h(h+ν)]` and
`|Γ(1+2ir)|²=2πr/sinh(2πr)`; the stated `2^{16}` comfortably bounds these factors.

For `r≥1` that gamma identity and the same series bound the normalized Bessel
kernel by `2^8 r⁻¹ᐟ²`. Its differential equation is
`(D_x²+x²)kernel = −4r² kernel`. Moving this operator twice onto `φ_t`
costs at most `2^{32}H(1+|t|)^4`; boundaries vanish. This proves (a), including
summable spectral decay, rather than stopping at DI's weaker (8.2).
The integer-order series gives
`|J_l(x)| ≤ e(x/2)^l/l!` for `x≤2`, proving (b).
For completeness the remainder in (8.1), with this fixed `φ`, satisfies
`|error(κ)| ≤ B/(1+|κ|²)` on the real and exceptional spectra, uniformly in `Y`.
For real `r≥1`, the `k≥1` series has an extra factor `r⁻¹`; one integration by
parts in `(x/2)^{±2ir}` gives `r⁻⁵ᐟ²`, with cost at most `2^{32}H`.
The estimates just given treat `|r|≤1` and the exceptional segment. In particular
there is no pole at `κ=0` hidden in this error term.

To check positivity, the exceptional main kernel is

`π/[2sin(πσ)] · [(x/2)^{−2σ}/Γ(1−2σ) − (x/2)^{2σ}/Γ(1+2σ)]`.

The ratio of the second bracket term to the first is at most
`exp(−4σ[log(2/x)−2])`; also `Γ(1−2σ) ≤ 2`.
For our `Y`, `log(2/x)−2 ≥ 1` and `2/x ≥ Y` throughout the support.
Use `sin(πσ) ≤ πσ` and `1−exp(−4σ) ≥ 4σ(1−e⁻¹)`.
Integrating over `[1/Y,4/(3Y)]` gives a main term larger than `Y^{2σ}/8`.
The remainder `2^{20}L_Y Y⁻³ᐟ² < 1/64` proves (c).
The same difference estimate gives (d), even with the factor `x^{it}`.
For (e), discard the decaying main term and the remainder:
`sin(πσ) ≥ 2σ`, `1/Γ(1±2σ) ≤ 2`, so their cost is at most `B/e`.
The Mellin bound follows directly by integrating `u^{−2σ}Ψ(u)`.

**2.3. Spectral-error rule.** Applying Theorem 2 at tolerance `e` in dyadic
spectral blocks, (a),(b) give a nonexceptional error at level `v` of at most

`B² K_T2(e)(1+|t|)^4 L_Y(1+v⁻¹N^{1+e})‖a‖²`.

Indeed `Σ_{h≥0}2^{−4h}(2^{2h+2}+v⁻¹N^{1+e}) ≤ 8(1+v⁻¹N^{1+e})`;
the numerical factors in (1.19) fit inside `B²`. Cross-products of two different
unit-modulus twists obey the same bound by Cauchy–Schwarz and Theorem 2.
At small exceptional parameters use (d) and Theorem 2 with `K=1`.
At large exceptional parameters the error in (e) is handled the same way.

## 3. Effective switching: (P2)

**3.1. First trace formula.** Apply DI (1.19) to `φ` and level `q` and sum over
`m,n ∈ I`: this is (8.7), p. 272. The regular error is bounded by §2.3 with `t=0`.
Multiply by `f(q)` and sum. Positivity (c) bounds the exceptional sum for
`Q<q≤2Q` by 64 times the weighted left side. The first error is at most
`2^{10}B² K_T2(e)L_Y(Q+N^{1+e})N`.

**3.2. Exact support.** In the double Kloosterman sum put
`C=πNY/Q`, `x=4π√(mn)/(qc)`. Our supports imply

`64C/51 ≤ c ≤ 128C/11`, hence `C<c<16C`.

Thus one can apply the second trace formula (8.8) at exactly these levels,
without enlarging the destination range. This computation is uniform in `m,n∈I`.

**3.3. Mellin separation.** In (8.9),

`χ(it)=∫f(ξ)ξ^{it}dξ/ξ=Q^{it}∫η(u)u^{it}du/u`.

Twelve integrations by parts in `log u` give
`|χ(it)| ≤ H/(1+|t|^{12})`, and also `≤ H/(1+t⁴)` (with the slack in `H`).
In particular `∫|χ(it)|(1+|t|)^4dt ≤ 2^8H`.
All these constants are independent of `δ,Q,c`; the factor `Q^{it}` has modulus one.
Insert inversion into `h(x)=f(4π√(mn)/(cx))φ(x)` *before* estimating its spectrum.
It gives the scalar `(c/4π)^{it}`, the transform `φ̂_t`, and coefficient factors
`m^{−it/2}n^{−it/2}`. Absolute convergence follows from the preceding bound and §2.3.
This also supplies the quantitative justification of (8.10), not an unsupported
large-sieve application to a transform depending on both `m` and `n`.

**3.4. Exceptional terms and errors.** Split at `σ=e`. Small parameters and all
regular/error terms contribute at most

`2^{20}B⁴H K_T2(e)e⁻¹ Y^{2e}L_Y(Q+C+N^{1+e})N`.

Here `Σ_{C<c≤16C}1 ≤16C` and `Σ_{C<c≤16C}1/c ≤1+log16<4`, also when `C<1`.
Use `L_Y ≤ (1+e⁻¹)Y^e` and `e=δ/4`: this is at most
`2^{24}B⁴H K_T2(e)e⁻²(YN)^δ(Q+C+N)N`.
For `σ>e`, (e), `cos(πσ)⁻¹≤2`, and Cauchy–Schwarz give the main term at most

`2^{12}BH e⁻¹ ∫ S(C,Y,N,u;I)du/(1+u⁴)`.

More explicitly the product is `overline{A_j(t/2)}A_j(−t/2)`; bound its modulus
by `(|A_j(t/2)|²+|A_j(−t/2)|²)/2`. Substitute `t=±2u` and use
`2/(1+16u⁴)≤2/(1+u⁴)`. This checks both twists, rather than treating the
product as a square without justification.

**3.5. Four blocks and small parameters.** Apply the result to
`(Q_l,Y_l)=(2^lQ,2^lY)`, `l=0,1,2,3`. The destination `C` stays unchanged.
The left weights dominate the desired `Y` weights and
`S(C,Y_l,N,u) ≤ 2^{l/2}S(C,Y,N,u)`; the remaining enlargement factors are at most
`4·8·8^{3e}<64²`. Replace `C` in the error by `πNY/Q`.
All coefficients fit below `Aδ⁻²[1+K_T2(e)]`.
If `1≤Y<Y_abs`, Theorem 2 directly gives the error-only bound, using
`Y^{2σ}≤Y_abs^{1/2}=2^{16}`. No switching with a changed `C` is necessary.
If `C<1` and `Y≥Y_abs`, use the main coefficient of §3.4 (which contains no
`K_T2`) and bound the destination sum by
`2K_T2(e)Y^{1/2}(16C+4N^{1+e})N`; since `Q>πNY`, its integral also fits
the asserted error. This proves the domain qualification in §1.

## 4. Effective preliminary estimate: (P1)

Apply (8.7) with the sign convention of §2, positivity, and §2.3, summing over `Q<q≤16Q`.
The error is at most `2^{12}B²K_T2(e)L_Y(Q+N^{1+e})N`.
For the Kloosterman term put `k=qc`. Its support implies `8NY<k<32NY`;
the number of representations is at most `τ(k)≤D(e)k^e` by LOGLOG3 Lemma 1.1.

For `w_k(m,n)=Ψ(4πY√(mn)/k)` on `[N,2N]²`, write `u=4πY√(mn)/k`.
Then `∂_mw=Ψ'(u)u/(2m)` and
`∂_m∂_nw=[u²Ψ''(u)+uΨ'(u)]/(4mn)`.
Consequently `|∂_m^a∂_n^bw_k|≤H N^{−a−b}`, `a,b∈{0,1}`, uniformly in `k`.
Two-variable partial summation costs at most `16H`, including conversion of
interval rectangles to four prefixes. Its variation measures are bounded by a
*common* measure (endpoint atoms and Lebesgue measure scaled by `N⁻¹,N⁻²`).
Thus one may sum absolute values over `k` before integrating and use Theorem 14
for each fixed prefix rectangle. One must not replace this by an unproved
bound for `Σ_k max_{v,w}|Σ_{m≤v,n≤w}S(m,n;k)|`.

With `K=32NY`, Theorem 14 bounds the Kloosterman contribution, including the
factor 64 from positivity, by

`2^{10}H · [D(e)K^e/(8NY)] · K14(e)(4KN²)^e K(K+4N²)`
`≤ 2^{20}H D(e)K14(e)(NY)^δ(N+Y)N`.

Indeed the powers lost are `N^{4e}Y^{2e}≤(NY)^δ`; all numerical powers of 32
and 128 fit in the displayed constant. Absorb `L_Y` in the spectral error using
`L_Y≤(1+e⁻¹)Y^e`. This proves (P1), even with `(NY)^δ` instead of `(QNY)^δ`.
For `Y<Y_abs` use the same direct Theorem-2 argument as in §3.5.

## 5. Gaps/caveats in the uncorrected argument

- DI (8.2) cannot have a `Y`-uniform constant at `r=0`: the transform grows like
  `log Y`. Retain `L_Y`, and use fourth-power spectral decay to sum Theorem 2.
- DI's positive exceptional lower bound is not justified uniformly near `Y=1`.
  The threshold and cancellation estimates in §2 repair it, including `σ→0`.
- The pictured supports `[1/2,5/2]` for both cutoffs only give
  `16C/25≤c≤32C`, not `(C,16C]`. The narrower, explicit cutoff in §2 repairs this
  without changing the recurrence or its four dyadic enlargements.
- Printed (1.22) and (8.1) have opposite signs. Our positive-transform convention
  explicitly tracks this harmless two-switch cancellation; the lower bound would
  be false for the literal transform printed in (1.22).
- No estimate here uses an unspecified `O_δ` constant. All such costs are either
  the stipulated black boxes at `δ/4`, the explicit divisor function `D(δ/4)`,
  or the displayed polynomial factors. The numerical absolute constants are
  analytic majorants, not optimized or floating-point certified constants.
