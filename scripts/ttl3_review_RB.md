# Hostile referee report RB — effective DI Theorem 14

Reviewed `scripts/ttl3_thm14_effective.md` and LOGLOG3 Proposition 6.1.
Checked the DI scan at journal pp. 225–230, 234–235, 261–262, 264–270,
275–276. This is a review **relative to the stipulated level-one Theorem 2**;
it does not certify the separate derivation of its constant.

**Verdict: no FATAL or MAJOR finding.** The displayed K14 and the stronger
U-form survive this audit. Two MINOR presentation corrections appear below.
I independently checked the transform and summation calculations rather than
accepting the large powers of two as substitutes for the necessary exponents.

## 1. Transform replacement (§2)

The repaired K representation is correct:
`∫₀∞ cos(x sinh ξ)cos(2rξ)dξ = cosh(πr)K_{2ir}(x)`.
Shifting the exponential representation to ±iπ/2 gives this identity;
one should first damp/regularize, as the note specifies. After integrating
against f, integration by parts makes the ξ integral absolutely convergent.
The factors 4/π and π/(2i) in DI (1.23), (1.22) fit the allowance.
The inner integral is bounded by H log 8 and by
`H(log 8+7/8)/(X|phase frequency|)`, so the stated 3 and 14 are safe.
Integrating the min bounds at sinh ξ=0 or sin ξ=0 gives precisely the
permitted logarithm for large X; for small X the K integral gives log(1/X).
There is no missing cosh or small-real-r singularity in the repaired proof.

Three integrations by parts give exactly
`F(s) = [s(s−1)(s−2)]⁻¹ ∫ f'''(x)x^(2−s)dx`.
On Re s=−3 the numerator bound is
`H X³(8⁶−1)/6 < 2^18 H X³`.
At Re s=0,−2 the analogous constants are `(8³−1)/3` and `(8⁵−1)/5`,
both below 2^15. All integration orders are fixed.

The crossed nonholomorphic poles are exactly `±2ir, −2±2ir`.
The normalized residues cost respectively `O(r^(−1/2))` and
`O(r^(−3/2))` before multiplication by F; thus the claimed residue powers
`r^(−7/2), X²r^(−9/2)` are correct. Since X≤r, these fit `2^21 H r^(−5/2)`.
The Γ identity using Q is exact. For K the hyperbolic ratio is even ≤1,
since `cosh(π(t/2+r))cosh(π(t/2−r)) ≥ cosh²(πr)`.
For J the ratio is ≤4 for r≥4, as asserted.
On |t|≤r, Q factors ≥r²/32 and the Mellin denominator dominates
`(1+t²)^(3/2)`; outside, one Q is ≥r²/8, the denominator ≥r³,
and the integral of the other reciprocal Q is ≤32.
Including the kernel's 2^6, these bounds fit 2^24 r^(−4).
Multiplication by 2^18 and the trace-transform factors stays below 2^50.
For holomorphic order r≥4 no poles are crossed, and the four-factor
modulus estimate is valid. No Stirling constant is required.

**MINOR 1 — holomorphic quotient wording.** The Gamma quotient is not
literally the reciprocal of four factors: writing z=(r−3+it)/2, it equals
`[Γ(z)/Γ(conj z)] / [conj z(conj z+1)(conj z+2)(conj z+3)]`.
The omitted factor has modulus one. Repair: say its *modulus* equals the
reciprocal product of the four factor moduli. The estimate and K14 do not change.

## 2. Spectral assembly (§3)

Theorem 2 (1.28) has exactly the holomorphic factorial/4π normalization
needed on p. 267; the order r=k−1 requires cutoff k≤T+1, absorbed in 16.
Splitting [U,2U) into pieces of (U/2,U] and (U,2U] costs at most two
in each quadratic sieve. U=1 is legitimate because Theorem 2 allows L=1/2.
Cauchy–Schwarz gives the claimed `(T+A)(T+B)` bound, linear in K_T2.
The tail block endpoint is 2^(j+1)R, not 2^jR; its extra factor ≤4
is harmless within 2^70. The geometric sums are 3.414214 and 4/3,
and `R^(−5/2)+X³R^(−4) ≤ 2/(1+X)` is valid for R=4+X.
DI pp. 261–262 proves λ₁≥3π²/2: there is no exceptional cusp spectrum.
The constant eigenfunction has zero nonzero Fourier coefficients.

**MINOR 2 — signs deserve an explicit sentence.** The stipulated sieve is
written for positive n, while the opposite-sign trace formula uses ρ_j(−n).
At level one choose a Maaß basis diagonalizing reflection z↦−conj z;
then ρ_j(−n)=±ρ_j(n), so the same quadratic sieve applies with no cost.
Also `S(−m,−n;c)=S(m,n;c)` and `S(−m,n;c)=S(m,−n;c)` by d↦−d.
Adding these facts explicitly closes the sign bookkeeping in §§3 and 7.
This is an elementary symmetry justification, not a new spectral input.

## 3. Fourier separation (§4)

The lower x endpoint is `(28π/17)√(UV)/D`; the upper/lower ratio is
`(17/7)²<8`. The factor c in h correctly removes Kuznetsov's 1/c.
Seven derivatives suffice (two per Fourier variable and three in x).
In scaled variables the composed map is `(17/7)√(ab)/z`, with a,b≥7/8,
z≥1. It is analytic on the indicated radius-1/32 polydiscs and bounded
by 16 there. Products of derivative bounds of total order ≤7 fit 2^80;
three cutoff bounds, product/chain terms and support size fit 2^500,
hence certainly 2^1000. No D,U,V or δ is concealed in these allowances.
The Fourier integral contributes 16, and
`(1+X+√U)(1+X+√V)/(1+X) ≤ (4+28π/17)√(UV) < 10√(UV)`.
Together with `1+|log X|≤3+log(DUV)`, this verifies B9 and its D√(UV) scale.

## 4. Majorants, zero modes, tails, and U-form (§§5–7)

For M≤4, f_M=M and M≤1+4log M. For M>4 its mean is
`4+4log(M/4)` and its distributional second derivative has total variation
exactly 2M² (including the periodic endpoint). The stated Fourier bounds
and absolute convergence follow. Coefficient positivity is neither true
in general nor used.
In fact the proof majorizes U(c) itself by
`Σ*_d f_M(d/c)f_N(d̄/c) = Σ_{m,n} a_m b_n S(m,n;c) ≥ 0`.
Multiplying by g_D≥0 preserves this inequality. Thus LOGLOG3's U-form is
valid, as is domination of character-twisted sums by |χ(d)|≤1.

For zero frequencies, `Σ_k min(1,(z/k)²)≤3z` and the divisor rearrangement
give `Σ_{n≥1}|a_n|(n,c)≤3L_M Mτ(c)`. The mean divisor bound, mixed-sign
factor two, and `L_M L_N≤4(1+log(DMN))²` justify the stated 2^10 allowance.
For dyadic tails let p=1+α and q=2^(−1+α), α≤1/20. The lower sum is ≤2M^p,
the upper sum ≤M^p/(1−q), and its logarithmic moment is
`≤(log 2)M^p/(1−q)² < 4M^p`. Hence both asserted bounds (5 and 4) hold
uniformly for nonintegral M. The double log sum is
`≤[25(3+log(DMN))+40](MN)^p ≤128(1+log(DMN))(MN)^p`.
All four sign quadrants therefore fit 2^1093. The bounds are absolutely
summable blockwise; no application to a single non-dyadic sequence occurs.

## 5. Final constant (§8)

Log absorption spends δ/2, and `(MN)^(δ/2)` spends at most another δ/2.
The sums of D and D² cost respectively 2 and 4/3, with no log C.
Even allowing the zero modes and all endpoint factors leaves over 100
powers of two below the claimed 2^1200 allowance. The final conversion
from K_T2≤exp(exp(B₂/δ)) to class E(B₂+1) is valid for δ≤1/10, B₂≥1.
No additional dependence on δ,C,M,N or a divisor-bound constant was found.
As independent sanity checks, a memory-light stdlib calculation with
`uv run --no-project python` checked the cutoff allowance (log₂≈102.871),
the spectral series, and sampled dyadic moments/scaling; these checks
support, but do not replace, the uniform inequalities established above.
