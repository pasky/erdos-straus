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
2. **No such weight among ~7,000 natural candidates (EVIDENCE, §3).** For the 732 primes
   `p≡1 (24)` below `6·10^4`, GF(2) linear algebra over 114 basic features,
   338 derived-quantity features, and all 6,555 pairwise ANDs of the basic
   features gives no combination whose count is always odd. With the
   pairwise features it overfits the training primes, then predicts held-out parities at
   chance (48–49%). The parities of `f`, `f_I`, and `f_II` show no correlation with 93
   arithmetic invariants of p, including Legendre and quartic symbols, `x²+32y²`
   representability, and `h(-4p)`, `h(-8p)`, `h(-3p)` and others mod 32. They are
   also independent of 27 global signed-graph counts (§3.3).
3. **Structural obstructions (PROVED, §2).**
   (a) The affine symmetry group of the Type II equation
   `k(4abc-p)=a+b` has order 4. On positive tuples only the swap `a↔b` survives, so no
   p-uniform piecewise-affine windmill exists in this model. In Zagier's
   argument, by contrast, every piece lies in the infinite group
   `O(x²+4yz)(ℤ)`.
   (b) In every fibre of the refactor fibration, the only integral involution is
   divisor complementation. Its fixed points are the central divisors
   `D=±s`, which never lie in the positive class `-s (mod r)`. The odd object in
   each fibre is the zero-denominator point `D=-s` or the
   central divisor `D=s`. Consequently fibrewise parity certifies only **mixed-sign**
   vertices, never positive ones: the positive class is the "−1 coset" of
   the central class.
   (c) The only signed vertices with a repeated denominator are the seed
   `(t,-2pt,-2pt)` and `(2t,2t,-pt)`. So coordinate permutations have exactly
   two non-free orbits, both nonpositive.
4. **Generalised windmill identities do not reach ES moduli (EVIDENCE, §2.4).**
   Among `m≤12`, the parity identity `#{n=x²+my²}≡#{n=UV,U<V,U≡V (m)}` holds
   (for odd n prime to m, up to rare exceptions) only for `m=3,4,8` (and partly 12). These are
   the idoneal-type moduli. Parity laws for divisors in residue classes
   exist only where genus theory makes representation a congruence
   condition. There, Mordell/Schinzel-type obstructions already rule out ES identities.

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
`E:=k(4abc-p)-a-b=0`. Type I solutions are the same with `k(4abc-1)=p(a+b)`.

**Proposition 2 (PROVED).** Let `g(v)=Av+β`, `A∈GL_4(ℚ)`, and suppose
`E∘g=λE` for a constant `λ≠0`. Then `g` is the identity, the swap `a↔b`,
`(a,b,c,k)↦(-a,-b,c,-k)`, or their composition. The same holds for the Type I polynomial.

*Proof.* The quartic part `4abck` must be preserved up to λ, so `A` is
monomial (a permutation matrix times a diagonal matrix): a linear map carrying a product of four
independent linear forms to a scalar multiple of itself permutes the forms up to scalars. A
translation `β≠0` would create a cubic monomial such as `β_a·bck`, but E has no cubic
part. The linear part `-pk-a-b` must go to `λ(-pk-a-b)`. Hence `k` is fixed with
scale λ, `{a,b}` is preserved with scale λ, and `c` is fixed with scale `λ^{-2}`.
Integrality forces `λ=±1`. ∎

Zagier's pieces preserve `x²+4yz`, whose integral orthogonal group is
infinite. The four-parameter ES surface is multilinear, with degree one in each
variable. It has no Vieta involutions, and by Proposition 2 no affine symmetry
beyond the swap. A windmill whose pieces are uniform in p is therefore impossible in this
model. This complements the finite `S_4` automorphism group of the projective
surface (notes §77.2), which concerns regular automorphisms rather than
piecewise-affine ones.

### 2.2 Fibre involutions fix only central divisors

Fix a denominator `x` of a signed vertex, and write `4/p-1/x=r/s`, `s>0`.
The fibre is the set of signed divisors `D|s²` with `D≡-s (mod r)`,
`D≠-s`, modulo `D↔s²/D` (SIGNED_REFACTOR §1). notes §77 (c) shows that `D↔s²/D` is the
only nontrivial fibre automorphism preserving integrality.

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

### 2.4 Windmill identities exist only for idoneal-type moduli (EVIDENCE)

The Zagier windmill proves
`#{n=x²+4y²}≡#{n=UV: U<V, U≡V (mod 4)} (mod 2)`. The analogous statement for
modulus `m` would be the natural route to parity laws for divisors of
`s²` in classes mod `q=4x-p`. For `n<4000` odd and prime to `m`, this is the
agreement rate:

| m | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| agreement | 0* | .80 | .99 | .99 | .72 | .83 | .73 | .99 | .80 | .73 | .77 | .94 |

(*m=1: exact anti-identity.) Only `m=3,4,8`, the one-class-per-genus cases,
carry an identity. The moduli `q=4x-p` of ES range over all integers `≡3 (mod 4)`.

## 3. Catalogue of computational tests (all negative)

Data: all 732 primes `p≡1 (24)`, `p<6·10^4`. There are 53,333 unordered positive
solutions, enumerated exactly by `windmill_enum.cpp` over `p/4<x≤3p/4` and
divisors of `(px)²`. Signed data cover all 385 primes `p≡1 (24)`, `p<3·10^4`: 280,569
signed vertices, enumerated exactly by `windmill_signed.cpp` via the incidence model of
SIGNED_REFACTOR §3. The count for `p=97`, 116 vertices, matches `pointwise_incidence.py`.

### 3.1 Weighted counts of positive solutions

| family | size | result |
|---|---|---|
| basic features: type, position of p-multiples, residues mod 2,3,4,5,7,8 of each coordinate, squareness, Legendre symbols, divisibility among coordinates, gcds, `z=lcm(x,y)`, window position | 114 | column rank 99; `1` not in span |
| derived quantities `Y,Z,q or m,D,D',g,a,b,c,k,Y±Z,YZ,D±D',(4Y-1)(4Z-1),…`, per type: square, 2·square, even, 3∣, ≡1 (4), 8∣, Legendre, =1 | 338 | not in span |
| λ-multiplicity counts `N_I/2`, `N_II/2`, `N/2` of the `(a,b,c,k)` model (weight `#{λ:λ²∣c₀}`) | 3 | odd 350–380/732 |
| pairwise ANDs of basic features | 6555 | training-solvable, validation 43–49% odd |
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
"−1 coset" of classes containing central divisors (§2.2). Every natural
involution — coordinate swap, divisor complement, and the S₃ action — fixes only
central or degenerate objects. Parity laws for divisors in classes mod m
exist only for idoneal-type m (§2.4). A windmill proof would need a new,
explicit odd weight on positive solutions. None of about 7,000 candidate weights
generalises beyond chance. (Continuation below.)

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
```
