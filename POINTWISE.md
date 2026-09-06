# Pointwise restart: constructions, not another exceptional-set estimate

**Erdős–Straus is not solved here.** I checked the complete criteria and the
latest pointwise hunt (§77), then tried constructions on auxiliary spaces
that its automorphism and finite-covering arguments do not exclude. Two
concrete constructions survive the tests below; neither has a termination
or positivity proof. No novelty or improvement of the verification frontier
is claimed. The experiment is about these restricted constructions, not
about checking ES beyond its already much larger verified range.

## 1. Start from a signed solution and refactor

For a prime `p = 4t+1`, an input-defined starting point is

\[
  4/p=1/t+1/(-2pt)+1/(-2pt).
\]

Make a graph of **all sorted signed integral solutions**, excluding zero
denominators; join two triples when they share a denominator. Fixing `x`
and reducing `4/p-1/x=r/s`, with `s>0`, gives the exact refactor move

\[
 (ry-s)(rz-s)=s^2,\qquad
 y=(D+s)/r,\quad z=(s^2/D+s)/r.
\]

Enumerate signed divisors `D` of `s²`, retain integral, nonzero `y,z`.
These are integral correspondences, not regular automorphisms: §77's
finite automorphism group does **not** rule them out.

**Finiteness proof.** Every signed solution has a positive denominator
`x ≤ 3p/4`: otherwise even the sum of its positive terms is less than
`4/p`. Each such `x` has a finite divisor fibre. Also `r≠0`, since
`x=p/4` is not an integer. Thus the entire graph is finite and exhaustible,
without assuming ES or a bound on the other denominators.

**Surviving sufficient conjecture:** the component of the displayed seed
always contains an all-positive vertex. This would give an algorithm
starting from every input prime, rather than from an already known positive
solution. Finiteness alone does not imply it.

An exact three-move path at `p=297049` is

```text
(-44118905676, -44118905676, 74262)
(-551488103244, -22978593612, 74262)
(-551488103244, 74269, 815884956)
(74269, 817093966, 3678095251134446)
```

Consecutive rows share a denominator; every row sums reciprocally to
`4/297049`. Complete enumeration gives **1143 signed vertices, 67 positive
vertices, and shortest seed-to-positive distance 3**. In particular, a
universal two-move claim is false.

Connectivity is not a shortcut: at the hard prime `97`, the component
sizes and positive counts are `(114,8), (1,0), (1,0)`. Some signed vertices
are completely isolated. Even monotone sign repair fails: at `p=73`,
`(-6643,28,52)` has exactly one neighbor, `(-6643,-1638,18)`. Escaping it
requires **increasing** the number of negative denominators. Both vertices
are seed-reachable, and a three-edge escape from the former reaches
`(20,210,30660)`. Maximizing the least positive denominator fails as well:
`(-1314,36,36)` and `(-97236,36,37)` form a lexicographic plateau. These
are failures of specific proofs, not a sterile seed-component example.

The missing step is a structural reason that the **seed component**, rather
than an arbitrary component, must reach positivity.

## 2. Choose windows using reduced quadratic forms

Let `[A,B,C]` run over primitive reduced positive definite forms of
discriminant `-4p`, with `|B|≤A≤C` and the usual nonnegative boundary sign.
For each coefficient `A`, take only the first multiple of `A` above `p/4`:

\[
 x_A=A\left(\left\lfloor\frac{p}{4A}\right\rfloor+1\right),
 \qquad q_A=4x_A-p.
\]

Here `A≤√(4p/3)`, `0<q_A<4A`, and `x_A<p` for the primes in question.
Test whether a positive divisor `d|x_A²` satisfies either

\[
 d\equiv-x_A\pmod{q_A}\quad\text{or}\quad
 d\equiv-px_A\pmod{q_A}.                                  \tag{1}
\]

**The certificate implication is proved.** In the first case the positive
integral denominators are

\[
 x,\quad p(x+d)/q,\quad p(x+x^2/d)/q.
\]

In the second they are

\[
 x,\quad (px+d)/q,\quad (px+p^2x^2/d)/q.
\]

Integrality of the second cofactor follows by multiplying the divisor
congruence by its cofactor, since `gcd(px,q)=1`. The identity follows from
`(qy-px)(qz-px)=(px)²`. This proves sufficiency, **not** existence of a
successful reduced form.

**Surviving sufficient conjecture:** at least one reduced form supplies
(1) for every prime `p≡1 mod24`.

The C++ search tests **all 82,887 such primes through `10^7`**. An independent
Python checker verifies the prime list, each form, integrality, and each
exact rational identity. All pass. The largest first successful `A` is
`95`, at `p=7347169`. This is finite evidence only.

For example, `[11,6,230]` at `p=2521` gives `x=638,q=31,d=44`, hence

\[
 4/2521=1/638+1/55462+1/804199.
\]

### Why the tempting proofs do not work

* **Zagier's forced component:** on `p=r²+4st`, the involutions swapping
  `s,t` and Zagier's three-branch involution give a distinguished odd
  component. The conversion `x=s(t+1)` fails on its entire 39-vertex
  component at `1129`. Replacing this by the nearest multiple of `s`
  repairs `1129`, but the whole 121-vertex component at `14401` fails.
* **Class-group parity:** at `3049`, all four classes in the 2-primary
  subgroup are sterile: `[1,0,3049]`, `[2,2,1525]`, `[47,±20,67]`.
  Their windows are `763,764,799`. The full group has 28 classes, of which
  14 are productive. Thus useful classes can require an odd-order part.
  Failure is not a subgroup condition either: at `193`, `[11,8,19]`
  fails but its square `[2,2,97]` succeeds.
* **Intrinsic negative Pell:** the real input `X²-pY²=-1` is available for
  these primes. But extracting form coefficients from divisors of
  `H²-pK²`, with `gcd(H,K)=1`, stays in the principal genus: if an odd
  prime `r≠p` divides such a coefficient and `-p` is a square modulo `r`,
  then both `p` and `-p` are squares modulo `r`, so `r≡1 mod4`.
  The possible factor `p` is also `1 mod4`; a factor `4` is impossible.
  Hence the associated primitive form has genus character `χ_{-4}=+1`,
  invariant under reduction. At `2521` **all 16 principal-genus classes
  are sterile**; `[11,6,230]` lies in the other genus. Extending the same
  norm-divisor extraction to more Pell periods cannot repair this.

The restriction is not automatic for an arbitrary ES witness. At
`p=193,x=52,q=15`, (1) succeeds, but the only divisors `A|52` admitting
`b²≡-193 mod A` are `1,2`, both too small for `q<4A`. Reducing a larger
coefficient need not preserve a hit either: `[23,18,14]` at `p=241` has
productive window `69`, but reduces to `[14,10,19]`, whose window `70`
is sterile. A different bridge is still possible; none was proved here.

## 3. The least nonresidue is not itself a recipe

For `p=21841`, the least quadratic nonresidue is `ℓ=11`, but the minimum
canonical parameter product `ab` over **both** ES types is `134>ℓ²`.
A witness is `(a,b,c,k)=(1,134,41,1)`. Requiring `ℓ|ab` raises the minimum
to `7436`, attained by Type I `(4,1859,152,9)`.

These are exhaustive exclusions: for a fixed product `ab`, enumerate all
factor pairs and all `d|(a+b)`, and test
`p+d≡0 mod4ab` or `pd+1≡0 mod4ab`. No cutoff on `c,k`, and no character
filter, is used. Thus the necessary nonresidue signature from §77 does
not justify either proposed small-parameter construction.

There is also a genuine unbounded obstruction to one proposed local repair.
It concerns profinite integers, **not integer counterexamples to ES**.

### A single-place lemma

Fix an odd prime `ℓ`. Consider profiles `n_q=1` at every prime `q≠ℓ`,
and `n_ℓ=r∈Z_ℓ*` with `(r/ℓ)=-1`. Use exactly the harvested witnesses
`M=4uvw-1`, `n≡-u/v mod M`. With additive Haar measure `μ(Z_ℓ)=1`, the
set `C_ℓ` of covered profiles satisfies, for every `0<ε<1/3`,

\[
                 \mu(C_\ell)\ll_\varepsilon\ell^{-1/3+\varepsilon}.
\]

In particular, for all sufficiently large `ℓ`, a positive-measure set of
nonresidue profiles avoids **every** harvested witness, at every level.

**Proof.** Write `M=ℓ^e m`, `(ℓ,m)=1`. If `e=0`, the witness would require
`M|u+v`, impossible since `M>u+v`. Otherwise normalize `u=ga,v=gb`,
`(a,b)=1`, and put `c=g²w`. Since `m|a+b`, set `k=(a+b)/m`, `N=ℓ^e`.
Then

\[
 k(4abc-1)=N(a+b),\qquad (k,N)=1,\qquad r\equiv-a/b\pmod N.
\]

The coprimality follows because the nonresidue `r` is not `1 modℓ`.
Conversely every such tuple supplies the required cylinder. Put `A=ab`.
Quadratic reciprocity gives `(A/M)=1`, while `b≡-a mod m` gives
`(A/m)=(-1/m)`. Consequently

\[
 (-a/b\mid N)=(-1/N)(A/N)=(-1/N)(-1/m)=(-1/M)=-1.
\]

Thus only odd `e` occur. To bound their supply, let `T(N)` count these
primitive tuples with `a≤b`. The equation implies `ack≤2N/3`, so at least
one of `ac,ak,ck` is at most `(2N/3)^{2/3}`. For each fixed pair, the
remaining coordinates are determined by a positive divisor, respectively,
of

\[
 N(4a^2c+1),\qquad Na+k,\qquad N^2+4ck^2.
\]

Indeed use `D=4ack-N>0`; in the last case its cofactor is `4bck-N`.
All dividends are `O(N³)` for contributing tuples. There are
`O(N^{2/3} log N)` small-product pairs; the elementary divisor bound,
with its exponent chosen small enough to absorb this logarithm, gives
`T(N)≪_ε N^{2/3+ε}`. Each unordered tuple covers at most two cylinders
of measure `ℓ^{-e}`. Summing over odd `e` gives

\[
 \mu(C_\ell)\le\sum_{e\text{ odd}}2T(\ell^e)\ell^{-e}
 \ll_\varepsilon
 \frac{\ell^{-1/3+\varepsilon}}{1-\ell^{-2/3+2\varepsilon}}.
\]

The nonresidue units have measure `(ℓ-1)/(2ℓ)`, proving the claim. ∎

The scope matters: a nontrivial single-place profile is not an ordinary
integer. This excludes universal single-place Hensel/composition coverage
for this family, not a proof using several places or the size of `p`.

## Replay

```sh
c++ -std=c++17 -O3 -Wall -Wextra -Wconversion -Werror \
  scripts/pointwise_forms.cpp -o /tmp/es-forms
(ulimit -v 524288
 /tmp/es-forms 10000000 --certificates > /tmp/es-form-certificates.txt
 uv run python scripts/pointwise_forms_check.py --census /tmp/es-form-certificates.txt)
uv run python scripts/pointwise_refactor.py 297049
```

The census streams certificates; its sieve/root tables use about 54 MB at
`10^7`. The signed graph stores divisor lists only for one window at a time,
uses denominator buckets instead of a quadratic adjacency matrix, and caps
inputs at `300000`. The Python tests independently check the stated main
counterexamples and exact identities. The outstanding assertions are the
two explicitly labelled sufficient conjectures, not computational steps
being passed off as proofs.
