# Wave 15 hostile review: §44 slice conspiracies

## Verdict

**SOUND-AFTER-REPAIRS.**  The proved core is correct: Theorems 44.1 and 44.2, Corollary 44.3, and Lemma 44.4 survive independent re-derivation, and the finite census reproduces exactly.  I found no MAJOR or BROKEN claim.  The original text did, however, omit the primitive/raw distinction and two admissibility edge cases, skip one needed invertibility statement in Theorem 44.2, present a previously proved progression without exact provenance, and leave the §36 `k=1`/single-slice relation implicit.  These are repaired in place and marked `(wave-15 review repair)`.

## Graded checklist

| # | Grade | Result |
|---|---|---|
| 1 | **REPAIRED** | The raw slice criterion (44.4) is exact in both directions for `(c,k) in B_p`.  Added the distinct primitive criterion, a raw-positive/primitive-zero example, and the failure of the divisor-grade test outside admissibility. |
| 2 | **REPAIRED** | The `{1,2,3,6}` theorem is sound for every square factor and every `k`.  Added the omitted proof that every norm prime is coprime to `tk` and made the projection from `4st^2k` to `4s` explicit. |
| 3 | **REPAIRED** | `(5,1)` is unconditionally positive for every prime `p = 97 (mod 120)` via the forced divisor `D=3`.  Added that this is exactly Theorem 35.4's `c=5,D=3` branch and that the same prime progression was already covered by Lemma 16.1. |
| 4 | **CONFIRMED** | `193` and `1033` are hard primes congruent modulo `840`, but their two-slice joint-vanishing statuses differ.  All four relevant slice values were independently recomputed. |
| 5 | **REPAIRED** | The `15/385`, `111`, and cutoff/histogram data reproduce.  Added the exact hard-prime convention and admissibility of all census slices; softened the code's “independent” description because both enumerations start from the same factorization. |
| 6 | **REPAIRED** | No no-witness claim occurs.  Added `T_{k=1}=sum_c M_{c,1}`, distinguished the Type-I audit from §17.5(a)'s Type-II count, and tied the ray error explicitly to §36.4's Hurwitz failure. |
| 7 | **REPAIRED** | Proved, Computational, and Assessment labels are now honest.  The only pointwise progression is explicitly identified as old supply, not a new advance toward Erdős--Straus. |

## 1. Exact slice criterion

Fix an admissible `(c,k)`, put `h=4ck`, `N=p^2+4ck^2`, and start from the Type-I equation

\[
 p(a+b)=k(4abc-1).
\]

With `D=4ack-p` and `E=4bck-p`, direct expansion gives

\[
 DE=16abc^2k^2-4pck(a+b)+p^2=p^2+4ck^2=N,
\]

and both `D` and `E` are `-p (mod h)`.  Conversely, if `D|N` and `D=-p (mod h)`, admissibility gives `(N,h)=1`; hence `D` is a unit and

\[
 E=N/D\equiv p^2(-p)^{-1}\equiv-p\pmod h.
\]

Thus `a=(D+p)/h` and `b=(E+p)/h` are positive integers, and reversing the displayed factorization recovers the Type-I equation.  This proves both directions and fixes the sign: the grade is **`-p mod 4ck`**, not `+p`; after projection to `4c` it remains `-p`.

Factoring `N=prod ell_j^{e_j}`, positive divisors are in bijection with exponent vectors `0<=u_j<=e_j`.  Therefore the raw ordered slice is exactly

\[
 M_{c,k}(p)=\#\{D|N:D\equiv-p\pmod h\},
\]

and vanishes exactly when no bounded exponent vector has target product grade.  Since every divisor is a unit modulo `h`, full Dirichlet-character orthogonality gives (44.3), including all imprimitive characters.  This is Theorem 36.1's raw summand.

The primitive summand is different:

\[
 M^*_{c,k}(p)=\sum_{D\text{ target}}\sum_{g|a_D,\,g|b_D}\mu(g)
 =\#\{D\text{ target}:(a_D,b_D)=1\}.
\]

Raw vanishing implies primitive vanishing, but not conversely.  The repaired example `(p,c,k)=(241,7,3)` has `N=58333`, target `11 mod 84`, and target divisors `11,5303`; they give `(a,b)=(3,66),(66,3)`, so `M=2` and `M*=0`.  This also agrees with §36.5: Elsholtz--Tao's canonical count is the primitive mass, while the campaign's raw mass includes dilations.

Admissibility cannot be dropped.  If `p|ck`, `-p` is not a unit, complement preservation and character orthogonality fail.  At `(3,1,3)`, `D=9` has the nominal target grade modulo 12 but its complement does not, and no row results.  Independently, the defining equation excludes `p|k` by `4abc-1>a+b`; once `p` does not divide `k`, reduction modulo `p` excludes `p|c`.  Hence §44's criterion is exact precisely on the stated `B_p` domain.

The root-progressions (44.5)--(44.7) are also equivalent in both directions: `d|N` is exactly `p^2=-4ck^2 (mod d)`, while the target grade is exactly `p=-d (mod h)`.  For an eligible `p`, the first congruence forces `(d,h)=1`, so `(2k)^{-1} mod d` exists.  No finiteness or positivity is smuggled into this infinite union.

## 2. Wrong-grade quartet

Write `c=st^2`, with `s` squarefree.  For every rational prime `ell|N`, admissibility gives `ell` coprime to `2stk`: if `ell|stk`, then `N=p^2 (mod ell)` is nonzero.  Hence

\[
 (p(2tk)^{-1})^2\equiv-s\pmod\ell,
\]

so the Kronecker character `psi_s(ell)=(-s/ell)` is `+1`.  Multiplicativity puts every divisor of `N` in the kernel.  The complete unit computations are

| `s` | modulus | kernel of `(-s/.)` | projected target for hard `p` |
|---:|---:|---|---:|
| 1 | 4 | `{1}` | `3` |
| 2 | 8 | `{1,3}` | `7` |
| 3 | 12 | `{1,7}` | `11` |
| 6 | 24 | `{1,5,7,11}` | `23` |

A hard prime is `1 mod 24`, hence `1 mod 4s` in all four cases.  Any full target `D=-p (mod 4st^2k)` would project to `-1 mod 4s`, outside the kernel.  The square factor `t^2` and `k` therefore introduce no assumption: they disappear only after a valid projection, and exclusion at the projected modulus is sufficient.  This proves all four cores, for arbitrary `t,k` subject to admissibility.

For `ck<=30`, the core contributions are `42,19,13,6` for `s=1,2,3,6`, totaling 80.  Block `(aq)` checks every norm prime's Kronecker value and asserts zero target divisors for every one of these 80 slices and all 385 census primes: zero finite exceptions.

## 3. The `(5,1)` progression

Let `p=97 (mod 120)`.  Then `p=1 (mod 3)` and `p=17 (mod 20)`, so

\[
 3\mid p^2+20,\qquad 3\equiv-p\pmod {20}.
\]

Thus the explicit divisor `D=3` exists for every prime in the progression; no unproved factorization assumption is present.  Its complement gives

\[
 a=(p+3)/20,\qquad b=(p^2+3p+20)/60,
\]

and direct substitution recovers the Type-I equation with `(c,k)=(5,1)`.  The class is `97`, not `1`, modulo 120, so it is fully consistent with §17.3's square-class escape.

This is not new identity supply.  It is exactly Theorem 35.4's already-proved `c=5,D=3` branch.  It also lies on an already-covered Type-II progression: Lemma 16.1 with `k ell=15`, `(u,v,w)=(1,2,2)` forces `p=7 (mod 15)`; intersecting with `p=1 (mod 24)` is exactly `p=97 (mod 120)`.  §44 now states both facts.

## 4. Two-slice counterexample

The relevant fixed modulus on the hard-prime domain is

\[
 \operatorname{lcm}(24,4\cdot5,4\cdot7)=840.
\]

The factor 24 is the hard-domain restriction; the two ray moduli alone have lcm 140.  Both `193` and `1033` are `1 mod 24`, and `1033-193=840`.  Independent exact recomputation gave

| `p,c,k` | factorization of `N` | target | target divisors | `M` |
|---|---|---:|---|---:|
| `193,5,1` | `3^2*41*101` | `7 mod 20` | none | 0 |
| `193,7,1` | `37277` prime | `3 mod 28` | none | 0 |
| `1033,5,1` | `3*67*5309` | `7 mod 20` | `67,15927` | 2 |
| `1033,7,1` | `37*151*191` | `3 mod 28` | none | 0 |

Thus joint vanishing is true at 193 and false at 1033 in the same class modulo 840.  The lemma correctly limits its conclusion to this natural fixed modulus and does not claim failure for every larger modulus.

## 5. Census and computation

Block `(aq)` uses exactly the raw formula of Theorems 36.1/44.1.  For each norm it builds the residue coefficient box and a literal divisor list from the same exact factorization, checks equality of the target counts, and reconstructs every surviving `(a,b,c,k)` row.  It does not apply the primitive Möbius filter, which is correct because `M_{c,k}` is raw.

“Hard prime” in this campaign census means exactly prime `p=1 (mod 24)`, not “no easy witness.”  There are 385 below 30000.  All 111 pairs `ck<=30` are admissible for all of them: `p>=73`, `k<=30<=2p/3`, `4ck<=120<2p+k`, and `p` is coprime to `ck`.

The mandatory full run

```text
uv run --with sympy,numpy,scipy python verify.py
```

ended `all checks passed` in 79.53 seconds with maximum resident memory 327084 KB.  Its `(aq)` output exactly reproduced:

* `(hard primes, slices, forced cores) = (385,111,80)`;
* cutoff all-zero counts `(385,220,161,63,41,30,15)`;
* 15 depth-111 primes, exactly the list in (44.18);
* the complete histogram in (44.17).

An isolated replay of the streamed `(aq)` algorithm took 1.512 seconds and 61988 KB.  It stores one factorization/divisor fibre at a time plus 385 small vanishing sets; no dense Cartesian allocation occurs.  Heavy `ES_FULL_SCAN` branches were not enabled in the required default full run.

Exact spot-checks at conspiracy prime 2521:

* `(5,1)`: `N=6355461=3*7*127*2383`, target `19 mod 20`; factor grades generate only `{1,3,7,9}`.
* `(7,1)`: `N=6355469=2269*2801`, both factors are `1 mod 28`, target `27`.
* `(5,2)`: `N=6355521=3^2*23*30703`, target `39 mod 40`; exact divisor enumeration finds none.

All three masses are zero, including two non-quartet cores and two different `k` values.

## 6. Register and prior-section consistency

Theorem 36.3's `T_{k=1}` is **not** the `(1,1)` slice.  Precisely,

\[
 T_{k=1}(p)=\sum_{c:(c,1)\in B_p}M_{c,1}(p).
\]

Because every term is nonnegative, its zero at 2521 means every `k=1` slice vanishes for every admissible `c`.  The §44 box result is stronger in a different direction: every slice of every `k` with `ck<=30` vanishes.  The twelve ordered Type-I rows at 2521 are therefore consistent; exact enumeration puts them outside that box (the least `ck` is 38, and none has `k=1`).

The GRH discussion is properly an Assessment.  It supplies a quantitative Type-I analogue of §17.5(a), not a re-analysis of that subsection's Type-II count (17.4).  The exact principal mass is only `p^{o(1)}`, while even an extra, non-GRH square-root cancellation assumption across `Theta(p)` fibres leaves `p^{1/2+o(1)}` error.  For one fixed slice, GRH has no standard pointwise control over a selected coefficient in the divisor Euler product of one moving norm.  This sharpens rather than contradicts §17.5.  It also leaves §36.4 intact: Hurwitz--Kronecker mass is weighted and unprojected, while the nonprincipal term retains precisely the omitted moving ray grade.

No sentence turns slice vanishing into failure of witness existence.  The census explicitly coexists with known Type-I rows at 2521, and the repaired progression paragraph says its pointwise positivity was already known.  Theorem/Corollary/Lemma labels are reserved for exact arguments, finite data remain Computational, and GRH/quantitative extrapolations remain Assessments.

## Final grade

**SOUND-AFTER-REPAIRS.**  No theorem downgrade and no wave-15 Review flag are required.
