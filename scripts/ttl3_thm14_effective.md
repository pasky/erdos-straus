# Effective DI Theorem 14, relative only to level-one Theorem 2

All page numbers below are journal pages. The scan was checked at pp. 228–230,
234–235, 261–262, 264–270 and 275–276. Write `e(x)=exp(2πix)`.

## 1. Statement

Assume each of DI (1.28)–(1.30), at level one, has constant
`K_T2(t) ≥ 1` in `K_T2(t)(K²+L^{1+t})‖a‖²`, for `K≥1, L≥1/2`.
Then, for `C,M,N≥1` and `0<δ≤1/10`, the following admissible constant is

`K14(δ) = 2^1200 (1+K_T2(δ)) (1+6/δ)^3`:

`Σ_{1≤c≤C} |Σ_{1≤m≤M} Σ_{1≤n≤N} S(m,n;c)| ≤ K14(δ)(CMN)^δ C(C+MN)`,

and in fact the U-form (R121B repair, m3): `Σ_{1≤c≤C} U(c;M,N) ≤ K14(δ)(CMN)^δ C(C+MN)`, real `M,N ≥ 1`, with
`U(c;M,N) = Σ*_{d mod c}|Σ_{m≤M}e(md/c)||Σ_{n≤N}e(nd̄/c)|` — §5's first step (DI p. 276, first line) majorises U(c),
not only `|ΣΣS|`, and every later step bounds that majorant.

In particular, if `K_T2(δ)≤exp(exp(B₂/δ))`, `B₂≥1`, then
`K14(δ)≤exp(exp((B₂+1)/δ))`. No divisor-bound constant is necessary:
the Ramanujan terms admit an elementary *mean* divisor bound.
The deliberately large numerical prefactor below uses a fixed-order variant
of Lemma 7.1, rather than assigning a number to DI's unspecified constants.
Only the permitted trace identities and the stipulated spectral sieve are
spectral black boxes. The bound is also valid when M,N are nonintegral.

## 2. Proof and constant ledger

### 1. A specified modulus majorant (DI p. 276)

Use the probability density `ρ` constructed in toolkit Lemma 1.3 and put
`χ = 1_[15/16,33/16] * (4ρ(4·))`.
Then `0≤χ≤1`, `χ=1` on `[1,2]`, and `supp χ⊂[7/8,17/8]`.
The proof of that lemma gives, for `0≤j≤7`,
`‖χ^(j)‖∞ ≤ 32e^16 144^j(j!)² < 2^120`.
These are fixed derivative orders, not orders depending on δ.
Set `g_D(c)=χ(c/D)`, for `D≥1`. It majorizes `[D,2D]` and
`|g_D^(j)|≤2^120 D^(−j)`. Its support lies below `3D`.

### 2. The real-spectrum transform estimate, with numerical constants

DI Lemma 7.1, pp. 264–267, uses a contour of real part `−1` and at most
**two** integrations by parts to prove (7.2)–(7.4). There is no δ in this
argument. We need only the regular spectrum, and only smoothing parameter
`Y=1`. To avoid an unnumbered Stirling constant, the following slightly
stronger smoothness assumption gives a directly numerical substitute.

If `supp f⊂[X,8X]` and `‖f^(j)‖∞≤H X^(−j)` for `0≤j≤3`, then each applicable
transform in (1.21)–(1.23) satisfies

`|transform(r)| ≤ 2^50 H (1+|log X|)/(1+X)` for all real r,

`|transform(r)| ≤ 2^50 H (r^(−5/2)+X³r^(−4))` for `r≥4+X`.

For the holomorphic transform r is a positive integer. These statements
hold for complex f as well. Here are details bounding the numerical costs.
For K use the correctly normalized representation
`cosh(πr)K_{2ir}(x)=∫₀^∞ cos(x sinh ξ)cos(2rξ)dξ`;
it follows by shifting the exponential representation by `±iπ/2`, with
an initial damping and then a limit. This repairs the missing cosh factor
in DI's first displayed transform calculation on p. 264.
The other representations are on pp. 264–265. One integration by parts
bounds the inner integral by `H min(3,14/(X sinh ξ))` for K,
`H min(3,14/(X cosh ξ))` for the nonholomorphic J transform,
or `H min(3,14/(X|sin ξ|))` for the holomorphic transform.
Integration in ξ gives the first assertion with `2^10`, hence with `2^50`.

For the second assertion use the Mellin–Barnes formulae on pp. 265–267,
shift instead to `Re s=−3`, and integrate the Mellin transform of f three
times. With `F(s)=∫f(x)x^(−s)dx/x`, this gives
`|F(−3+it)| ≤ 2^18 H X³/|s(s−1)(s−2)|`.
The only nonholomorphic residues crossed are at `s=±2ir,−2±2ir`.
Their total is at most
`2^20 H(r^(−7/2)+X²r^(−9/2)) ≤ 2^21 H r^(−5/2)`.
This follows directly from `|Γ(iv)|²=π/(v sinh πv)`, the Gamma recurrence,
and `|F(−2k±2ir)|≤2^15 H X^(2k)/(2r)^3`, `k=0,1`.

For completeness the remaining Gamma integrals have a simple uniform
bound, so no asymptotic Stirling constant is concealed here. Put
`Q(v)=sqrt((v²+1/4)(v²+9/4)) ≥ (1+|v|)²/8`.
The identity `|Γ(−3/2+iv)|²=π/(cosh(πv) Q(v)²)` bounds the K-transform
kernel, including its cosh factor, and the J-transform kernel, including
its sinh factor, by
`2^6/[Q(t/2+r)Q(t/2−r)]`.
For J use the same identity and recurrence for the denominator Gamma;
the remaining exponential ratio is ≤4 by `||t/2+r|−|t/2−r||≤2r`.
After division by `|s(s−1)(s−2)|`, each integral is ≤`2^24 r^(−4)`:
on `|t|≤r` both Q factors are ≥`r²/32` and
`∫(1+t²)^(−3/2)dt=2`; on either remaining half-line one Q factor is
≥`r²/8`, the Mellin denominator is ≥`r³`, and the reciprocal of the
other Q has integral ≤32. These bounds are valid for `r≥4`.
For the holomorphic transform the Gamma quotient on this line is the
reciprocal of four consecutive factors starting at `(r−3+it)/2`;
its modulus is ≤`2^16(r+|t|)^(−4)`, and there are no crossed poles for `r≥4`.
Combining `2^18`, `2^24`, the factors in (1.21)–(1.23), and the residues
is smaller than `2^50`. All contour shifts and all derivative orders
in this numerical replacement are fixed independently of δ,X,H.

### 3. Theorem 8 at level one: the spectral split (pp. 267–268)

DI chooses `R₁=1+X`, `R₂=1+max(X,Y)`; hence with `Y=1` there is no
middle range except a bounded interval when `X<1`. Our replacement above
uses `R=4+X`, an enlargement by at most a factor four.
Let `A=U^((1+δ)/2)`, `B=V^((1+δ)/2)` and `L(X)=1+|log X|`.
Cauchy–Schwarz and the three assumed sieves bound the combined spectral
mass up to T by `16K_T2(δ)(T+A)(T+B)‖a‖₂‖b‖₂`.
The factor 16 includes the trace normalizations and interval endpoints:
`[U,2U)` can be split between `(U/2,U]` and `(U,2U]`.
For `U=1` the first interval has parameter `1/2`, allowed in DI Theorem 2.

Use the first transform bound below R, the second on
`[2^jR,2^(j+1)R)`, and `(2^jR+A)≤2^j(R+A)`.
The two tail series are bounded by
`Σ2^(−j/2)<4` and `Σ2^(−2j)=4/3`.
Also `R^(−5/2)+X³R^(−4)≤2/(1+X)`.
The resulting bilinear trace bound is

`2^70 H K_T2(δ) L(X)/(1+X) (1+X+A)(1+X+B) ‖a‖₂‖b‖₂`.  (B8)

There is **no exceptional term**. DI's proof of Theorem 3, pp. 261–262,
gives `λ₁≥3π²/2>1/4`, hence `θ₁=0`. Only this consequence is used;
Selberg's weaker level-varying gap is not a substitute here.

### 4. The needed version of Theorem 9; Fourier separation (pp. 269–270)

For arbitrary coefficients supported on positive integers `[U,2U)` and
`[V,2V)`, `U,V≥1`, we prove

`|Σ_{m,n,c} a_m b_n g_D(c)S(m,±n;c)|`
`≤ 2^1080 K_T2(δ) D√(UV)(UV)^(δ/2)(3+log(DUV)) ‖a‖₂‖b‖₂`.  (B9)

This is enough; the stronger C-only ε-loss printed in (1.52) is not needed.
To account for the `1/c` in Kuznetsov, apply DI's separation to
`h(u,v,c)=cχ(c/D)χ(u/U)χ(v/V)`.
Write `h(u,v,4π√(uv)/x)=∫∫G(t₁,t₂;x)e(t₁u+t₂v)dt₁dt₂` and put
`X=(28π/17)√(UV)/D`. The x support lies in `[X,8X]`, since its endpoint
ratio is `(17/7)²<8`. Integration twice or zero times in each Fourier
variable gives, for `0≤j≤3`,

`|∂ₓ^jG|≤2^1000 DUV X^(−j) w(Ut₁)w(Vt₂)`,
`w(t)=min(1,|t|^(−2))`, `∫w=4`.

Here is a crude check on this absolute derivative allowance. At most seven
derivatives occur in total. Each of the three cutoff factors contributes
at most `2^120`. In dimensionless variables the map `4π√(uv)/xD` and its
products of derivatives through order seven have bound `2^80`: Cauchy's
estimate on polydiscs of radius `1/32` gives `16·32^k k!` for one derivative,
and products have total order ≤7. The chain/product rule contributes fewer
than `2^40` terms, and the support area and linear c factor cost less than
`2^10`. Thus even `2^500` suffices; `2^1000` is a generous allowance.

Apply (B8) to G and integrate; `∫∫UV w(Ut₁)w(Vt₂)dt₁dt₂=16`, exactly the
integral on p. 270. Since `κ=28π/17<6`, `X=κ√(UV)/D`,
`(1+X+√U)(1+X+√V)/(1+X)≤10√(UV)` and
`L(X)≤3+log(DUV)`.
Moreover the replacement of √U,√V by A,B costs at most `(UV)^(δ/2)`.
These inequalities prove (B9), with the stated numerical allowance.

### 5. Fourier majorants, including small M (Lemma 8.2, pp. 275–276)

Let `f_M(ξ)=min(M,2/‖ξ‖)`, periodically extended, and `a_m=f̂_M(m)`.
DI's pointwise majorization followed by its absolutely convergent Fourier
expansion gives (8.14), a **nonnegative real** right side for each c.
Write `L_M=1+4log M`. Then
`|a_m|≤L_M`, and `|a_m|≤(M/m)²` for `m≠0`.
For `1≤M≤4` the function is constant M, so these statements also hold.
For `M>4`, direct integration gives `a₀=4+4log(M/4)≤L_M`.
The distributional second derivative has total variation `2M²` (including
both corners and the periodic endpoint). Thus
`|a_m|≤2M²/(2πm)²≤(M/m)²`.
This supplies the justification for DI's piecewise-smooth integrations by
parts and for every Fourier rearrangement. The coefficients are real/even,
but need not be nonnegative; we do not take their positivity for granted.

### 6. Zero frequencies: no pointwise divisor bound (p. 276)

Use `|S(0,n;c)|≤(n,c)`, `S(0,0;c)=φ(c)≤c`, and
`(n,c)≤Σ_{d|c,d|n}d`. For every `z>0`,
`Σ_{k≥1}min(1,(z/k)²)≤3z` (split at k=z, or use ζ(2) when z<1).
Consequently
`Σ_{n≥1}|f̂_M(n)|(n,c)≤3L_M M τ(c)`.
The elementary mean bound is
`Σ_{c≤Z}τ(c)=Σ_{d≤Z}⌊Z/d⌋≤Z(1+log Z)`.
As `g_D≤1` and `supp g_D⊂(0,3D)`, all zero-frequency terms together are
at most
`2^10 (D²+DMN)(1+log(DMN))³`.
Here the mixed terms have their factor 2 for negative frequencies;
use `M+N≤2MN` and `L_M L_N≤4(1+log(DMN))²` (AM–GM).
No ε, individual divisor estimate, or ineffective arithmetic constant occurs.

### 7. All nonzero frequencies and their infinite tails

Split each sign into blocks `U=2^j`, `V=2^k`, `j,k≥0`.
The block norms satisfy
`‖a_U‖₂≤√U L_M min(1,(M/U)²)` and its N analogue.
Put `α=δ/2≤1/20`, `b_U=U^(1+α)min(1,(M/U)²)`.
Geometric summation below and above M gives explicitly
`Σ_U b_U≤5M^(1+α)` and
`Σ_U b_U log_+(U/M)≤4M^(1+α)`:
the upper tail ratio is at most `2^(−19/20)`, the lower tail ratio at most
`1/2`; for the logarithmic moment use `Σ_{j≥1}j q^(j−1)=(1−q)^(−2)`.
Thus the double sum of the `(3+log(DUV))` factor in (B9) is at most
`128(MN)^(1+α)(1+log(DMN))`.
With `L_M L_N≤16(1+log(DMN))²` and all four sign choices, the nonzero
contribution is at most
`2^1093 K_T2(δ) DMN (MN)^(δ/2)(1+log(DMN))³`.
This establishes absolute summability of the bounds, not an illicit
application of (1.52) to the entire non-dyadic coefficient sequences.

### 8. Absorption and the c decomposition

For `P≥1`, toolkit Lemma 1.2, or direct maximization, gives
`(1+log P)³≤(1+6/δ)³ P^(δ/2)`.
Combine Steps 6–7, using `(MN)^(δ/2)≤(DMN)^(δ/2)`.
Cover `1≤c≤C` by `[D,2D)` with `D=1,2,4,…≤C`.
Though there are `1+⌊log₂C⌋` pieces, **no logarithmic loss is required**:
`ΣD≤2C`, `ΣD²≤(4/3)C²`, and `DMN≤CMN` on each piece.
The result is bounded by the K14 stated in §1, with room to spare.
Finally `log K14≤1200log2+log2+exp(B₂/δ)+3log(1+6/δ)`;
for `B₂≥1`, `δ≤1/10` this is ≤`exp((B₂+1)/δ)`.

## 3. Gaps/caveats in a literal reading of DI

* Theorem 13's stated mixed derivative bounds (7.7) only control two
  derivatives in each original variable. Its displayed Fourier argument
  differentiates the composed c argument up to **six** times, not merely
  twice. That argument does not justify its advertised constant from (7.7)
  alone. Our product cutoff controls seven derivatives (the numerical
  transform replacement uses three), repairing this for Theorem 14.
* The stronger `C^ε`-only form (1.52) is not established here. Directly
  inserting Theorem 2 leaves the `(UV)^(δ/2)` and log factors in (B9).
  They are harmless after the explicit infinite-tail summation; silently
  treating all Fourier coefficients as one dyadic block is not justified.
* The cosh factor omitted in the K-transform calculation on p. 264 is
  restored by the oscillatory representation in Step 2; simply bounding
  the printed exponentially decaying integral would not suffice.
* The exceptional estimate (7.1), if interpreted uniformly as r→0 with an
  absolute constant, is problematic: the small-x expansion of `K_{2r}(x)`
  has coefficient `Γ(2r)`, unbounded as r→0. None of (7.1), exceptional
  contour shifts, or exceptional-spectrum induction is used here.
* The sole remaining input is the promised effective level-one K_T2.
  No numerical bound for it is asserted in this note.
