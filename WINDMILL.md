# Windmill / parity search for Erdős–Straus (wave: windmill)

**Status: no parity proof found. Erdős–Straus is not solved here.**
This file records a search for a Zagier-"windmill"-style argument: a finite
set `S(p)` with an involution `σ` having an odd number of fixed points, and a
second involution `τ` whose fixed points yield positive solutions of
`4/p=1/x+1/y+1/z`. Labels: **PROVED**, **EVIDENCE** (finite computation),
**HEURISTIC**, **CONJECTURE**. Throughout `p≡1 (mod 24)` is prime,
`t=(p-1)/4`, `f(p)` is the number of unordered positive solutions.

Code: `scripts/windmill_*.{cpp,py}`. Data were regenerated in `/tmp/wm/`
(see §6 for replay).

## 0. Summary

1. **Reduction (PROVED, §1).** Any argument of the requested shape produces an
   explicit weight `w ≥ 0` on positive solutions with `Σ w(sol)` odd for every
   p. With `w≡1` this would say `f(p)` is odd; that is false (`f(97)=8`,
   `f(193)=6`). So the whole question is whether some *explicit* weighted count
   of positive solutions is odd for every p.
2. **No generalising weight among the tested candidates (EVIDENCE, §3).** The
   sample is the 732 primes `p≡1 (24)` below `6·10^4`. No GF(2) combination of
   the 114 basic features, nor of the 338 derived-quantity features, has an
   always-odd count, even on these finite data. With all 6,555 pairwise ANDs of
   the basic features, which outnumber the primes, interpolation is possible. A
   386-term combination is odd on all 732 primes. But combinations fitted on a
   training prefix predict the held-out primes at chance (43–49% odd). So no
   *generalising* law was found. The parities of `f`, `f_I`, and `f_II` showed no
   usable correlation with 93 arithmetic invariants of p: the best single
   agreement was 55%, and no GF(2) combination fits even the training half. The
   invariants include Legendre and quartic symbols, `x²+32y²`
   representability, and bits of `h(-4p)`, `h(-8p)`, `h(-3p)`, and others.
   Parities of 27 global signed-graph counts have marginal odd frequencies of
   45–56% (§3.3). These are marginal frequencies only; no independence test
   was made. Note that `Vpos=f`.
3. **Structural obstructions (PROVED, §2).**
   (a) The integral affine maps (`AGL_4(ℤ)`) preserving the Type II
   polynomial `k(4abc-p)-a-b` up to a constant form a group of order 4. On positive
   tuples only the swap `a↔b` survives. So no windmill whose pieces are
   integral affine maps preserving the equation identically exists in this
   model. Pieces that preserve the equation only on the finite point set are
   not excluded. In Zagier's
   argument, by contrast, every piece lies in the infinite group
   `O(x²+4yz)(ℤ)`.
   (b) In every fibre of the refactor fibration, the only integrality-preserving
   *regular automorphism* is divisor complementation (notes §77 (c)).
   Arbitrary set-theoretic involutions of the divisor set are not excluded. Its fixed points are the central divisors
   `D=±s`, which never lie in the positive class `-s (mod r)`. The odd object in
   each fibre is the zero-denominator point `D=-s` or the
   central divisor `D=s`. Consequently fibrewise parity certifies only **mixed-sign**
   vertices, never positive ones: the positive class is the "−1 coset" of
   the central class.
   (c) The only signed vertices with a repeated denominator are the seed
   `(t,-2pt,-2pt)` and `(2t,2t,-pt)`. So coordinate permutations have exactly
   two non-free orbits, both nonpositive.
4. **Generalised windmill identities do not reach ES moduli (EVIDENCE, §2.4).**
   We tested `m≤40` on odd, non-square `n<6000` prime to `m`. The parity
   identity `#{n=x²+my²}≡#{n=UV,U<V,U≡V (m)}` holds exactly only for
   `m=3,4,8,12,24`, the `m≥3` dividing 24. These are the moduli whose unit
   group has exponent 2. Among ES moduli `q=4x-p≡3 (4)`, only `q=3` is of
   this kind, and there the Type II condition is a congruence event (notes §6).
5. **The natural odd set sees ES with weight 6 (PROVED, §2.5).** The set
   `S_{112}` of solutions of `1/x+1/y+2/z=4/p` is always odd, but its z-even
   part is exactly `6f(p)`. Every always-odd set found in a zoo of
   ES-flavoured sets (§3.5) is explained by a central or ambiguous fixed
   point that is not a positive ES object. No handshake subgraph (§3.4) and no
   GF(2) component law (§3.6) gives more. **Verdict: no proof from the constructions tried (§5).**
6. **By-product (PROVED, §2.7, Theorem 7).** Every p-free denominator outside
   `[1,2t]` lies in at most one signed vertex. This closes the case `2t<z<p`
   that SIGNED_REFACTOR §5 left at "at most two". The mixed case reduces to a
   Vieta quadratic whose discriminant would need `-k` to be a square modulo
   `4kλ-1`, which the Jacobi symbol forbids. So all graph edges pass
   through small p-free or p-divisible denominators.

## 1. The reduction lemma

**Lemma 1 (PROVED).** Let `S` be finite and let `σ,τ` be involutions of `S` with
`|Fix σ|` odd. Let `Φ: Fix τ → P(p)` be a map to the set of positive
solutions. Then `Σ_{v∈P(p)} |Φ^{-1}(v)| ≡ 1 (mod 2)`; in particular `P(p)≠∅`.

*Proof.* `|S| ≡ |Fix σ| ≡ |Fix τ| (mod 2)`. ∎

The content of such an argument is therefore the weight
`w(v)=|Φ^{-1}(v)|`. The same holds for the "chain" form of Zagier's proof: the
`⟨σ,τ⟩` orbit of the unique σ-fixed point is a path ending at a τ-fixed point. It also holds for
matching formulations on the signed refactor graph. Let a matching cover a
component `C` except the seed, and let a second matching cover the nonpositive vertices of `C`. Then
`|C|` is odd, and `C` contains a positive vertex. But `|C|` is odd for only 187 of 385
seed components (§3.3). One needs a canonically chosen odd subset.

**Corollary.** No such argument has `Fix τ` in bijection with unordered
positive solutions: `f(p)` is odd for about half of all p (`f(97)=8`). The same holds for
the sets of Type I or Type II solutions, and for every λ-multiplicity count
from the `(a,b,c,k)` parametrisation (§3.1).

## 2. Structural obstructions

### 2.1 No windmill in the four-parameter model

Type II solutions are `(x,y,z)=(abc, pkbc, pkac)` with
`E:=k(4abc-p)-a-b=0`. Type I solutions are `(pabc,kbc,kac)` with
`k(4abc-1)=p(a+b)`.

**Proposition 2 (PROVED).** Let `g(v)=Av+β` with `A∈GL_4(ℤ)`, `β∈ℤ⁴`, and
suppose `E∘g=λE` for a constant `λ≠0`. Then `g` is the identity, the swap `a↔b`,
`(a,b,c,k)↦(-a,-b,c,-k)`, or their composition. The same holds for the Type I polynomial.

*Proof.* The quartic part `4abck` must be preserved up to λ. By unique
factorisation in `ℚ[a,b,c,k]`, `A` permutes the four coordinate forms up
to scalars. Integrality and invertibility over ℤ make those scalars `ε_i=±1`,
so `λ=∏ε_i=±1`. A translation `β≠0` would create a cubic monomial such as
`β_a·bck`, but E has no cubic part. The linear part `-pk-a-b` must go to
`λ(-pk-a-b)`. If k were sent to `±a` or `±b`, the coefficient `p` would
have to equal `±1`, and E has no linear c-term. Hence k is fixed with sign λ.
Then `{a,b}` is preserved with sign λ, and c is fixed with sign
`λ/λ³=1`. ∎

Over `ℚ` there are more symmetries, for example
`(a,b,c,k)↦(2a,2b,c/4,2k)`, with `E∘g=2E`, and for Type II
`(a,b,c,k)↦(pk,b,c,a/p)`. They do not preserve the lattice.

Zagier's pieces preserve `x²+4yz`, whose integral orthogonal group is
infinite. The four-parameter ES surface is multilinear, with degree one in each
variable. It has no Vieta involutions, and by Proposition 2 no integral
affine symmetry beyond the swap and the sign change. Hence no windmill exists
whose pieces are integral affine maps preserving `E` identically, uniformly in
p. A piece need only preserve the finite point set on its region. That weaker
possibility is not excluded by this argument. This complements the finite `S_4` automorphism group of the projective
surface (notes §77.2), which concerns regular automorphisms rather than
piecewise-affine ones.

### 2.2 Fibre involutions fix only central divisors

Fix a denominator `x` of a signed vertex, and write `4/p-1/x=r/s`, `s>0`.
The fibre is the set of signed divisors `D|s²` with `D≡-s (mod r)`,
`D≠-s`, modulo `D↔s²/D` (SIGNED_REFACTOR §1), with `r/s` in lowest terms.
notes §77 (c) shows that `D↔s²/D` is the only nontrivial *regular automorphism*
of the punctured fibre that preserves integrality. This does not classify
arbitrary set-theoretic involutions of the finite divisor set.

**Lemma 3 (PROVED).** Suppose `r≥3` and `x>p/4`, so `r=4x-p>0` for p-free x. Put
`N^±=#{D>0: D|s², D≡∓s (mod r)}`. Then `N^+` is even, `N^-` is odd, the
fibre has `N^+/2` positive vertices, and it has `(N^--1)/2` vertices with exactly one
negative denominator.

*Proof.* Complementation preserves both classes because `(±s)²=s²`. Its
unique positive fixed point `D=s` lies in class `+s`, not in `-s`, since
`r∤2s`. Positive D in class `-s` gives `y,z>0`. A negative divisor `-D` with
`D≡s` gives `y=(s-D)/r` and `z=(s-s²/D)/r` of opposite signs, or a zero denominator when
`D=s`. ∎

Thus the odd member of every fibre is the central divisor. It is degenerate,
and its class is the *mixed* class. The positive class is its negative. This is the
fibre-level form of the recurring "−1 obstruction" (notes §6 Lemma 6.1 and
C17 in DISCOVERIES.md).

In anchor coordinates `q=4x-p`, the classes of `d|x²` are the following.
Type II is `d≡-x`. Type I anchored at x is `d≡-1/4`. The complement of Type I
is `d≡-4x²`. Complementation pairs the last two with each other, which is the swap
of the two p-free coordinates. So it has no fixed points and imposes no
fibre-level parity.

### 2.3 Repeated denominators

**Lemma 4 (PROVED).** The signed vertices with two equal denominators are
exactly `(t,-2pt,-2pt)` and `(2t,2t,-pt)`.

*Proof.* If `2/x+1/z=4/p` with `p∤x`, then `z=px/(2(2x-p))`. Since
`gcd(2x-p,x)=1`, `2x-p∈{±1,±p}`. Only `x=2t` gives an integer, `z=-pt`.
If instead the repeated coordinate is `pm`, then `x=pm/(2(2m-1))`, so
`2m-1∈{±1,±p}` with m even. Only `m=-2t` works, giving `x=t`. ∎

Every other orbit of `S_3` on ordered signed vertices is free. Hence any
parity must come from a non-permutation involution.

### 2.4 Windmill-type parity identities for moduli m≤40 (EVIDENCE)

The Zagier windmill proves
`#{n=x²+4y²}≡#{n=UV: U<V, U≡V (mod 4)} (mod 2)`. The analogous statement for
modulus `m` would be the natural route to parity laws for divisors of
`s²` in classes mod `q=4x-p`. Squares must be excluded: at `n=9`, `m=4`, the left side is 0
and the right side is 1. For `n<4000` odd, non-square, and prime to `m`, this is the
agreement rate:

| m | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| agreement | .62 | .81 | 1 | 1 | .72 | .88 | .73 | 1 | .74 | .72 | .77 | 1 |

Extending to `m≤40` and `n<6000`, the identity is exact exactly for
`m∈{3,4,8,12,24}`. These are the `m≥3` with `m|24`, whose unit group mod m
has exponent 2. The ES moduli `q=4x-p` range over all integers `≡3 (mod 4)`.
Only `q=3` is of this kind, and there witness existence is already a
congruence event (notes §6).

### 2.5 Coefficient patterns: the natural odd set sees ES with weight 6

Windmill parity usually comes from a symmetric "trivial" point. For
`4/p=Σ c_i/x_i` with `Σc_i=4`, the point `x_i=p` exists, whereas ES has
`Σc_i=3` and no such point. The closest odd set is

\[
 S_{112}(p)=\{(x,y,z)\in\mathbb Z_{>0}^3:\ 1/x+1/y+2/z=4/p\},
 \qquad (x,y)\ \text{ordered}.
\]

**Proposition 5 (PROVED).** `S_{112}(p)` is finite and has odd cardinality.
Its elements with z even number exactly `6f(p)`.

*Proof.* Finiteness: one of `1/x,1/y,2/z` is at least `4/(3p)`, so
`x≤3p/4`, `y≤3p/4`, or `z≤3p/2`. Fix that variable. The rest is
`a/b=1/u+c/v` with `c∈{1,2}`, i.e. `(au-b)(av-cb)=cb²`, which has finitely
many positive solutions. Parity: the swap `x↔y` fixes exactly the
solutions of `1/x+1/z=2/p`,
i.e. `(2x-p)(2z-p)=p²`. These are `(p,p)`, `((p+1)/2, p(p+1)/2)`, and
`(p(p+1)/2,(p+1)/2)`: three points, all with z odd (`(p+1)/2` is odd since `p≡1 (4)`). For z even,
`(x,y,z)↦{x,y,z/2}` is an ES solution with a marked coordinate `z/2` and an
ordered pair `(x,y)`. ES coordinates are distinct (Lemma 4 / notes Lemma
77.13), so each unordered solution arises exactly `3·2` times. ∎

So the natural odd set contains ES only with the symmetric weight 6, and
its odd part lives entirely in the z-odd (non-ES) half. The map
`(x,y,z)↦(x,z/2,2y)` is a free involution on the z-even half, and there is
no natural map mixing z-parities. The same happens for 4-term
representations. The ordered count is odd because of `(p,p,p,p)`, which
is not mergeable into ES because `2/p` is not a unit fraction. ES-derived
4-tuples again come with full `S_3` multiplicity.

### 2.6 ES is the discriminant-zero case of Borwein–Choi

Borwein–Choi (`xy+yz+zx=n`) work through forms `[x+z,2z,y+z]` of
discriminant `-4n`, where class-group and genus theory apply. The ES fibre
equations are exactly the discriminant-zero case. For Type II,
`(qY-x)(qZ-x)=x²`, and the form `[qY-x,2x,qZ-x]` has discriminant 0. For
Type I, `(mX-z₀)(mY-z₀)=z₀²`. At discriminant 0 the class group
degenerates to the divisor lattice of a square, whose only involution is
complementation (§2.2). This is why no class-number parity is available
fibre by fibre. The c=1 slice of Type II can be read at nonzero
discriminant (`[U,4a,W]`, disc `-4p`, §4), but the ES condition
`U≡-1 (mod 4a)` is then a cusp congruence, not a class condition.

### 2.7 Rigidity: Type I leaves and private large p-free denominators

**Lemma 6 (PROVED).** `(2t,2t,-pt)` is the only signed Type I vertex whose
two p-free denominators both lie in `[1,2t]`.

*Proof.* If `m>0`, the vertex is positive, so `1/x+1/y<4/p`. But
`1/x+1/y≥1/t>4/p`, a contradiction. So `m<0`. If both p-free
denominators are at most t, then `1/x+1/y≥8/(p-1)>5/p≥4/p+1/(p|m|)`,
again impossible. So write `x=t+a` with `1≤a≤t` and `m=ph-t`, `h≤0`, and
put `e=(4a-1)h-a<0`. The other p-free denominator is
`y=(t+a)(p|h|+t)/((4a-1)|h|+a)`. For `h=0`, `y=t+t²/a≤2t` forces `a=t`.
For `|h|=H≥1`, `(t+a)(4t+1)-(8at-2t)=4t(t-a)+3t+a>0` and
`t(t+a)≥2ta`, so `y>2t`. ∎

**Theorem 7 (PROVED).** Let `p=4t+1` be prime. Every p-free denominator
`z` outside `[1,2t]` occurs in at most one signed vertex.

SIGNED_REFACTOR §5 proved this for `z<0` and `z≥p`, and proved at most two
vertices for `2t<z<p`. We now close the remaining case `2t<z<p`.

*Setup.* Every vertex containing z is of Type I, because a Type II vertex
has only one p-free denominator and that one is at most `2t`. The other
p-free denominator x satisfies `1≤x≤2t` (SIGNED_REFACTOR §3). Use the
symmetric chart anchored at z:

* `A=4z-p`, with `4t+3≤A≤3p-4`;
* `m=(pH+1)/4` for the p-divisible denominator `pm`, where `H=4h-1`;
* `e=(AH-1)/4`, with `e|z²` and `Hz=m+e`.

Then `x=zm/e=Hz²/e-z`. Put `f=z²/e`, a signed divisor of `z²`. Using
`AH=4e+1`, this gives

\[
  x+z=Hf,\qquad A(x+z)=4z^2+f .                               \tag{2.7a}
\]

The vertex is positive exactly when `h≥1`, i.e. `H≥3`. Then `f>0` and
`f≤(x+z)/3≤2t`. Otherwise `H≤-1` and `f<0`.

*Two vertices.* Suppose vertices 1 and 2 share z, with `x₁≠x₂`. Distinct
vertices at z have distinct h, hence distinct x by (2.7a). By (2.7a),
`f₂-f₁=A(x₂-x₁)`.

* **Both positive.** Then `0<f₁,f₂≤2t<A`, which is impossible.
* **Mixed.** Let P be the positive vertex and N the nonpositive one.
  Then `f_P>0>f_N`, so `x_P>x_N`. Since `|f_N|≤x_N+z≤6t` and `f_P≤2t`,
  we get `A(x_P-x_N)≤8t<2A`, so `x_P=x_N+1` and `f_P=f_N+A`. It follows
  that `|f_N|=A-f_P≥2t+3`. If `H_N≤-5`, then `|f_N|≤6t/5`, a
  contradiction. So `H_N=-1`, i.e. `h=0` and `m=-t`. The vertex N is
  therefore `(x_N,z,-pt)` with `1/x_N+1/z=1/t`.

  Write `x_N=t+d` and `z=t+u` with `du=t²` and `d<t<u`. Parametrise
  `d=λα²`, `u=λβ²`, `t=λαβ` with `α<β`, and put `γ=β-α`. Then (2.7a) gives

  \[
   f_P=f_N+A=3u-2t-d-1=\lambda\gamma(4\alpha+3\gamma)-1=\lambda\gamma(4\beta-\gamma)-1,
  \]
  \[
   x_P+z=\lambda(\alpha+\beta)^2+1=:w+1,\qquad z^2=\lambda\beta^2 w .
  \]

  The positive vertex needs `f_P|z²` and `f_P|x_P+z=w+1`. Then
  `gcd(f_P,w)=1`, so `f_P|λβ²`. Since `f_P≡-1 (mod λ)`, in fact
  `f_P|β²`. Write `β²=k f_P` with `k≥1`. This says that β is a root of

  \[
   \beta^2-4k\lambda\gamma\,\beta+k(\lambda\gamma^2+1)=0 .
  \]

  The quarter-discriminant `k(λγ²M-1)` must then be a square `s²`, where
  `M=4kλ-1≥3`. So `s²≡-k (mod M)`. But `(-k|M)=-(k|M)=-1`:

  * if `k=2^j k'` with `k'` odd and `j≥1`, then `M≡7 (mod 8)`, so
    `(2|M)=1`;
  * `(k'|M)=(M|k')(-1)^{(k'-1)/2}=(-1|k')(-1)^{(k'-1)/2}=1`, because
    `M≡-1 (mod k')` and `(M-1)/2` is odd;
  * `gcd(k,M)=1`.

  A Jacobi symbol of `-1` excludes a square. This is a contradiction.
* **Both nonpositive.** Here SIGNED_REFACTOR §5 applies. Directly: from
  `|f₁|=|f₂|+A≥4t+4`, as above `H₁=-1`, and then
  `|f₂|=x₁+z-A(x₂-x₁)≤x₁+z-A=2t+d-3u+1<1`, which is impossible.

∎

The derivation was checked on data. All 8,695 vertices with `2t<z<p` at
the 385 primes below `3·10^4` satisfy (2.7a), with `f|z²`, `H≡3 (4)`,
`4m=pH+1` and `1≤x≤2t`. The factorisation-free mixed-case scan
`scripts/windmill_singleton.cpp` finds no candidate. It runs over **all**
`t≤2.5·10^6`, not only those with `4t+1` prime, so it covers every
`p≤10^7`. It enumerates the divisor pairs `d<t<u` of `t²` with
`u-t≤(d+1)/2`, which is necessary for `H_P≥3`. That is 2,939,478 pairs, and
none satisfies the two divisibilities. This is consistent with the proof.

The previous census counted 213,024 p-free buckets outside `[1,2t]` below
`3·10^4`: 58,543 with `z≥p`, 8,695 with `2t<z<p`, and 145,786 with
`z<0`. All are singletons, as Theorem 7 now guarantees.

**Consequence.** Together with Lemma 6, every Type I vertex other than
`(2t,2t,-pt)` has exactly one p-free denominator in `[1,2t]`. Its other
p-free denominator is private to it, so the vertex is a leaf there.
All edges of the signed refactor graph therefore pass through p-free
denominators in `[1,2t]` or through p-divisible denominators. In
particular, every crossing between positive and nonpositive vertices
goes through a small p-free bucket or a Type I p-divisible bucket, since
(2a) forbids Type II crossings.

## 3. Catalogue of computational tests (all negative)

Data: all 732 primes `p≡1 (24)`, `p<6·10^4`. There are 52,601 unordered positive
solutions, enumerated exactly by `windmill_enum.cpp` over `p/4<x≤3p/4` and
divisors of `(px)²`. Signed data cover all 385 primes `p≡1 (24)`, `p<3·10^4`: 280,569
signed vertices, enumerated exactly by `windmill_signed.cpp` via the incidence model of
SIGNED_REFACTOR §3. The count for `p=97`, 116 vertices, matches `pointwise_incidence.py`.

### 3.1 Weighted counts of positive solutions

| family | size | result |
|---|---|---|
| basic features: type, position of p-multiples, residues mod 2,3,4,5,7,8 of each coordinate, squareness, Legendre symbols, divisibility among coordinates, gcds, `z=lcm(x,y)`, window position | 114 | GF(2) rank 71; `1` not in span |
| derived quantities `Y,Z,q or m,D,D',g,a,b,c,k,Y±Z,YZ,D±D',(4Y-1)(4Z-1),…`, per type: square, 2·square, even, 3∣, ≡1 (4), 8∣, Legendre, =1 | 338 | not in span |
| λ-multiplicity counts `N_I/2`, `N_II/2`, `N/2` of the `(a,b,c,k)` model (weight `#{λ:λ²∣c₀}`) | 3 | odd 350–380/732 |
| pairwise ANDs of basic features | 6555 | more columns than primes: a 386-term interpolant is odd on all 732 primes, but fits on training prefixes (400/500/600 primes) validate at 49%/49%/43% odd, so nothing generalises |
| non-local counts: distinct smallest, middle, largest, p-free, and p-divisible denominators; x-values with odd multiplicity; multiplicity of the minimal x | 10 | all ~50%, except obviously skewed small-value counts |
| signed character sums `Σ(x/p)`, `Σ(q/p)`, `Σ(m/p)`, `Σ(-1)^x`, … | 10 | no constant value and no constant residue mod 4 |

The only identically even columns are explained by known facts. For
example, `((Y+Z)/p)=-1` for every positive Type II solution follows from
`x(Y+Z)=qYZ` and `(q/p)=(x/p)`. The character theorem (SIGNED_REFACTOR (2a))
explains the others.

### 3.2 Invariants of p

The parities of `f`, `f_I`, and `f_II` were compared with 93 invariants:

* Legendre symbols `(ℓ/p)` for `ℓ≤43`;
* quartic symbols of 2, 3, 5, 7 and the octic symbol of 2;
* representability by `x²+ky²` for `k=16,27,32,48,64,72`;
* bits 1–4 of `h(D)` for `D=-4p,-8p,-3p,-24p,-12p,-7p,-20p`;
* `τ(t²) mod 4`, `ω(t)`, `Ω(t)`;
* p mod 5, 7, 11, 13, and 192.

The best single agreement is 55%. No GF(2) combination is solvable even on the training
half (`scripts/windmill_invariants.py`).

### 3.3 Global signed-graph counts

For all 385 primes, the parities of the following are each odd for 45–56% of primes:

* V; positive vertices, and positive vertices by type;
* vertices by number of negative entries × type;
* number of components; seed-component size, positive count, and Type I count;
* positive-bearing, sterile, and all-positive components; odd-size components;
* distinct denominators, positive denominators, and edges;
* odd buckets and odd positive buckets; positive-graph components;
* crossing pairs (positive, nonpositive), `Σ_d a_d b_d`, and mixed buckets.

The nonpositive count is also uniform mod 4. The seed component
is odd for 187/385 primes. See `windmill_signed_parity.py`.

### 3.4 Handshake arguments

A graph H on signed vertices in which the seed has odd degree and every
other nonpositive vertex has even degree would force a positive vertex.
This is more flexible than an involution, but by Lemma 1 it is still an
odd weighted count (`w=deg_H`). We took H to be the refactor edges through
a bucket class. The resulting parity is
`#{buckets d in class: a_d,b_d both odd}`, where `a_d,b_d` count positive
and nonpositive members. We tested 18 classes: sign, p-divisibility, Type
I/II label, small/mid/large p-free, the hubs, and bucket size. Classes
with no mixing are identically even:

* by (2a) for Type II;
* by Theorem 7 for large p-free buckets;
* for negative buckets, since positive vertices have only positive
  denominators.

The remaining classes are odd for 48–53% of primes. No GF(2) combination
exists (`windmill_handshake.py`).

### 3.5 A zoo of ES-flavoured sets

`windmill_zoo.py` covers 164 primes below 12000. The only always-odd sets
are explained by an obvious involution with a central or ambiguous fixed
point:

| set | parity | explanation |
|---|---|---|
| Zagier `x²+4yz=p` | always odd | control |
| reduced forms, disc `-4p` | always even | genus theory |
| reduced forms with `a≡3 (4)` | always even | non-principal genus, free inversion |
| reduced forms with `4∣b` | always odd | inversion fixes only `[1,0,p]` there |
| `{D∣x²: D≡+x (q)}` over odd-length windows | always odd | central divisor `D=x`, mixed class |
| `{D∣x²: D≡-x (q)}` over any window | always even | positive Type II, free complementation |
| `UW-4a²=p`, `U≡-1 (4a)` (c=1 Type II), with various cutoffs | 14–54% | — |
| `UW-4a²=p`, `U≡+1 (4a)` (two-negative Type II) | 51%, and 161/164 with the cutoff `a≤t/4` | cutoff artefact; nonpositive anyway |
| signed Type I chart boxes `\|h\|≤1,2,5` | 44–57% | — |
| reduced forms with `b>0`, `a≡-1 (mod b)` | 54% | — |

### 3.6 Laws holding on every component (Chen-type test)

The literature suggests Chen's Markoff theorem, that every component size
is divisible by p, as the model "size congruence". We tested it as
follows. For every component of every signed graph (`p<3·10^4`), we
recorded the parities of 20 statistics: size, positive count, Type I
count, counts by sign pattern and type, denominator classes, edges,
incidences, odd buckets, and seed membership. We then computed the GF(2)
relations holding on all components (`windmill_component_laws.py`). All
seven relations are bookkeeping identities, or consequences of Lemma 4,
Lemma 6, and the singleton-bucket evidence above. There is no
nontrivial component law. Seed-component sizes, and their nonpositive
parts, are equidistributed mod 2, 3, 4, 5, and 8.

## 4. Other mechanisms considered

* **Zagier set of p itself (`x²+4yz=p`) with a different τ.** Every
  piecewise-affine τ has a linear fixed locus, so its fixed points are representations of p by a
  binary quadratic form. These are Frobenius conditions. An ES construction from
  them would be a quadratic-form family, which notes §9.3 and Mordell's argument obstruct. A fibrewise τ on
  `⊔_x Div((p-x²)/4)` has odd fixed-point count only in the unique fibre
  `x=a`, `p=a²+4b²`. It would need an ES certificate forced by the divisors of `b²`,
  which is an unproved construction of the kind that failed in POINTWISE §2
  (1129, 14401).
* **"Relaxations" whose diagonal is ES.** An example is
  `4/p=1/(2x)+1/(2x')+1/(pY)+1/(pZ)` with τ: `x↔x'`. By Lemma 1 the fixed set is
  ES itself, with weight 1, so the relaxed count is `≡f_II` and random.
  Relaxing `D·D'=x²` to `D·D'=x·x'` either puts the diagonal on central
  divisors, which are degenerate, or needs congruences that are not symmetric under the swap.
* **Forms of discriminant −4cp.** Type II with `c=1` is exactly a form
  `[U,4a,W]`, `UW-4a²=p`, with `U≡-1 (mod 4a)`. These forms lie in the
  non-principal genus. For `p≡1 (8)` that genus contains no ambiguous class,
  so inversion acts freely and genus theory gives only `4|h(-4p)`. The
  ES condition is a cusp congruence, not a class condition. General c needs
  discriminant `-4cp`, a different class group for each c.
* **Sperner / Chevalley–Warning / root numbers.** These are other parity or
  counting-mod-m mechanisms. They produce zero crossings, local solutions, or
  rational points. ES has none of these obstructions, and needs integral positivity.
* **Galois conjugation over `ℚ(√p)`.** Its fixed points would be rational solutions.
  The set of totally positive `O_K`-solutions is infinite, because unit twists act in each
  fibre, so no finite parity count is available.

## 5. Assessment

HEURISTIC. Positive ES certificates are divisor-class events in the
"−1 coset" of classes containing central divisors (§2.2). The natural
involutions examined here fix only central or degenerate objects: the
coordinate swap, divisor complement, and the S₃ action. Parity laws for divisors in classes mod m
exist, among the tested `m≤40`, only for `m|24` (§2.4). A windmill proof would need a new,
explicit odd weight on positive solutions. None of about 7,000 tested candidate weights
generalises beyond chance. Every always-odd set found (§3.5) is explained
by a central or ambiguous fixed point that is not a positive ES object.
The natural odd set containing ES, `S_{112}` (§2.5), sees ES only with the
symmetric weight 6. The literature is consistent with this. Jiang
(arXiv:2609.09204, Thm 5.3(iii)) shows that the ordered `f_I,f_II` are even
for `p≡1 (4)`. Bright–Loughran (Thm 1.6) show that the only Brauer class is
the character (2a), so Legendre-symbol weightings of coordinates add
nothing beyond (2a). Elsholtz (2010, §3) shows that finite windmill
partitions close only for special forms, matching §2.4.

**Verdict (after this wave):** the constructions tried here did not yield
a proof. A parity proof of ES would require an explicit weight on positive
solutions whose total is odd for every p (Lemma 1). The following did not
supply one:

* coordinate permutations (Lemma 4);
* regular fibre automorphisms, i.e. divisor complement (Lemma 3);
* ambiguous-form structure in the tested sets;
* integral affine maps preserving the four-parameter equation identically
  (Proposition 2).

Nor did any of the tested candidate weights, sets, handshake graphs, or
component laws (§3). This is not an impossibility theorem. Arbitrary
set-theoretic involutions, and pieces preserving only the finite point set,
remain unexcluded. **CONJECTURE (heuristic):** `f(p) mod 2` is
asymptotically equidistributed and uncorrelated with the Frobenius data of p. So
are the tested natural weighted variants, excluding those that are
identically even for a known reason: free swaps, (2a), and Jiang's ordered
counts.

## 6. Replay

```sh
g++ -O2 -std=c++17 scripts/windmill_enum.cpp -o /tmp/wm_enum
g++ -O2 -std=c++17 scripts/windmill_signed.cpp -o /tmp/wm_signed
mkdir -p /tmp/wm
/tmp/wm_enum 1 60000 > /tmp/wm/pos60k.txt          # ~10 s
/tmp/wm_signed 1 30000 > /tmp/wm/signed30k.txt     # ~5 s
cd scripts
uv run python windmill_parity_features.py /tmp/wm/pos60k.txt
uv run python windmill_parity_features2.py /tmp/wm/pos60k.txt
uv run python windmill_invariants.py /tmp/wm/pos60k.txt
uv run python windmill_signed_parity.py /tmp/wm/signed30k.txt
uv run python windmill_handshake.py /tmp/wm/signed30k.txt
uv run python windmill_component_laws.py /tmp/wm/signed30k.txt
uv run python windmill_zoo.py 12000                 # ~10 min
uv run python windmill_misc_checks.py            # runs lam cross nonlocal signs pairs genzag
g++ -O2 -std=c++17 windmill_singleton.cpp -o /tmp/wm_single && /tmp/wm_single 2500000 | tail -1
```
