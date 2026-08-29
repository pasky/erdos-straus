# Wave 16 hostile review: §48 conspiracy depth

## Verdict

**SOUND-AFTER-REPAIRS.**  The moving-genus theorem and the residue-one escape theorem survive complete re-derivation.  The fixed-divisor classification is exact for its formally stated shape.  I found no theorem-level gap.  I repaired one false row identification, tightened the informational register, and corrected the verifier-scope description.

## Graded checklist

| # | Grade | Finding |
|---:|:---|:---|
| 1 | **CONFIRMED** | The box has 111 slices, exactly 80 have forced core, and the remaining 31 are exactly the rows in (48.5).  Block `(au)` reproduces every `G/E/P` count and all §44 aggregates under the raw-slice conventions of `(aq)`. |
| 2 | **REPAIRED** | Theorem 48.1 is correct.  Its genus condition forces one half of the hard residue classes, not exactly the full vanishing set; the scope sentence now says this unambiguously.  Completeness is claimed only inside `ck<=30`, where a positive progression for each of the 31 other slices proves it. |
| 3 | **REPAIRED** | The definition of `D`, admissibility boundary, `D=ck_min-1`, census, and records are correct.  Growth and `w*` correlation language is now explicitly measured/informational and does not claim support for a growth law. |
| 4 | **REPAIRED** | Theorem 48.4 is a complete classification of the explicitly defined fixed-`d` shape.  All prime-`d` instances are old Lemma 29.2 supply.  The claim that §35.4 supplied “the same row” was false and is repaired in §§44 and 48; it supplies the same progression through a different row and slice. |
| 5 | **CONFIRMED** | Theorem 48.5 follows from a sharp factor-size contradiction and covers every bounded-full-modulus system of fixed divisors, including composite divisors.  It says nothing about moving divisors or actual vanishing. |
| 6 | **REPAIRED** | The 15/385 result is consistent with §44: it means `D>=30`, not `D=111`.  All finite censuses are computational, the depth equivalence remains bookkeeping, and the last empirical-support wording was removed. |
| 7 | **REPAIRED** | `(au)` is streamed and comfortably below the requested default runtime.  The text now accurately says the optional path also extends fixed-guarantee row replays, not only the depth scan. |

## 1. The 31-slice census

Counting by product gives

\[
 \#\{(c,k):ck\le30\}=\sum_{c\le30}\left\lfloor{30\over c}\right\rfloor=111.
\]

The values of `c<=30` whose squarefree core is in `{1,2,3,6}` are

\[
1,2,3,4,6,8,9,12,16,18,24,25,27.
\]

Their slice count is

\[
30+15+10+7+5+3+3+2+1+1+1+1+1=80.
\]

The complement is therefore exactly 31 slices.  Listed by `k`, it is:

- `k=1`: `c=5,7,10,11,13,14,15,17,19,20,21,22,23,26,28,29,30`;
- `k=2`: `c=5,7,10,11,13,14,15`;
- `k=3`: `c=5,7,10`;
- `k=4`: `c=5,7`;
- `k=5,6`: `c=5`.

This matches (48.5) exactly.  For these rows, `(au)` reproduces the displayed `(G,E,P)` triples.  In table order they are

```
(185,35,165) (182,148,55) (185,128,72) (181,92,112)
(188,146,51) (182,117,86) (185,163,37) (186,117,82)
(181,155,49) (185,149,51) (182,159,44) (181,184,20)
(173,173,39) (188,130,67) (182,189,14) (189,136,60)
(185,168,32) (185,108,92) (182,176,27) (185,155,45)
(181,145,59) (188,165,32) (182,155,48) (185,178,22)
(185,163,37) (182,166,37) (185,163,37) (185,136,64)
(182,186,17) (185,140,60) (185,174,26).
```

Every row sums to 385.  The vanishing-frequency bin counts are exactly `1,4,14,10,2`.  Adding the 80 universal zeros reproduces §44's histogram, cutoff counts, and 15 full-box conspiracies.

`(aq)` counts the raw slice using both multiplicity-bearing grade coefficients and literal divisors from one exact factorization.  `(au)` independently rebuilds the exponent-bounded residue set; discarding multiplicity is valid because §48 asks only whether the target coefficient is zero.  It then reconstructs the §44 aggregates from the 31 residual zero sets plus the proved 80 deterministic zeros.  The raw/primitive distinction is therefore handled correctly.

## 2. The moving-genus theorem

Let `c=s t^2`, with `s` squarefree, and let `f=|Delta_s|` be the conductor of the primitive quadratic character of `Q(sqrt(-s))`.  For an admissible slice, every prime `ell` dividing

\[
N=p^2+4s(tk)^2
\]

is odd and prime to `stk`: otherwise admissibility gives `N=p^2 != 0 (mod ell)`.  Hence

\[
\left(p(2tk)^{-1}\right)^2\equiv-s\pmod\ell,
\]

so `chi_s(ell)=1`.  Complete multiplicativity gives `chi_s(D)=1` for every divisor `D|N`, including all exponent choices.

The conductor divides `4s`, hence divides the target modulus `4ck`.  A target divisor would satisfy `D=-p (mod 4ck)` and therefore

\[
\chi_s(D)=\chi_s(-p)=\chi_s(-1)\chi_s(p)=-\chi_s(p),
\]

because `Delta_s<0` makes the character odd.  Thus `chi_s(p)=1` contradicts the existence of a target divisor.  This proves (48.2) directly from (44.4), with no unbounded-exponent or subgroup relaxation.

For the residue-class classification, put `m=lcm(24,f)` and restrict `chi_s` to

\[
H=\{u\in(\mathbb Z/m\mathbb Z)^*:u=1\pmod {24}\}.
\]

It is trivial on `H` exactly when the primitive character is induced modulo 24, equivalently `f|24`.  The negative fundamental discriminants with conductor dividing 24 are

\[
-4,-8,-3,-24,
\]

corresponding respectively to `s=1,2,3,6`.  Otherwise the restriction is a nonprincipal quadratic character, so exactly half of `H` has value `+1`; Dirichlet/PNT in the finitely many reduced classes gives relative density `1/2`.  Primes dividing `s` are both finite and inadmissible.

This theorem is sufficient, not a global classification of all identically vanishing slices.  The exact completeness claim is only for `ck<=30`: each nonuniversal row in (48.5) has an explicit reduced fixed-divisor progression with infinitely many prime members, so none of those 31 can vanish identically.  The census has zero exceptions to the genus implication.

## 3. Depth and finite growth

The set `U_p(B)` is monotone in the integer boundary `B` and intersects the exact admissible set `B_p`; it does not silently count formal slices outside Theorem 36.1.  If the first positive unforced product is `n`, all boundaries through `n-1` vanish and boundary `n` fails, so

\[
D(p)=n-1=ck_{min}(p)-1.
\]

If no positive admissible unforced slice exists, both quantities are infinite.  Products `1,2,3,4` contain only forced cores, giving the deliberate convention `D>=4`.

The histogram in (48.11), nine record jumps in (48.12), dyadic table, and optional records `(55441,82)` and `(92401,102)` all reproduce.  The 15 primes with 111 vanishing slices in §44 have first positive products

```
38,67,77,34,59,38,34,42,38,39,44,35,42,31,59
```

in the order of (44.18), hence `D` from 30 through 76.  This exactly resolves the apparent “111-depth” naming conflict.

Pearson `0.525121`, tied-rank Spearman `0.568502`, and every grouped mean/max in (48.14) recompute.  They are descriptive measurements on 385 primes, not evidence for a population correlation or any logarithmic growth law.  The finite record ratios likewise discriminate between no candidate scales.

## 4. Fixed-divisor classification

Fix `h=4ck` and `d` coprime to `h`.  On a reduced hard class `r mod L`, where `L=lcm(24,h,d)`, a specified `d` is a target divisor for every member exactly when

\[
r=1\pmod {24},\qquad r=-d\pmod h,\qquad r^2=-4ck^2\pmod d.
\]

The last congruence is exactly `d|(p^2+4ck^2)` and the middle congruence is exactly the target grade.  This proves necessity as well as sufficiency within the stated fixed-`d` shape.  If `e=N/d`, then `e=-p (mod h)` because `N=p^2 (mod h)`, and

\[
d=ha-p,\quad e=hb-p,\quad de=p^2+hk
\]

expands to `p(a+b)=k(4abc-1)`.  Refinements to multiples of `L` add no other fixed-`d` guarantees.

For prime `d=q`, this is precisely Lemma 29.2 plus `p=1 (mod 24)`: the norm congruence has the two roots in (48.18) iff `(-4c|q)=1`.  Thus every prime-divisor instance in (48.5) and (48.19) is known §29 supply; no instance is advertised as new.  Composite `d` is included by Theorem 48.4 and was already implicit in the full root progression (44.5).

Three independent spot checks, each at multiple primes:

| `(c,k,d;r mod M)` | primes checked | exact target data |
|:---|:---|:---|
| `(5,1,3;97 mod 120)` | `97,337,457` | at `97`: `N=3*3143`, `-p=3 mod 20`, `(a,b)=(5,162)`; at `337`: `e=37863`, `(17,1910)` |
| `(7,1,11;73 mod 1848)` | `73,3769,11161` | at `73`: `N=11*487`, `-p=11 mod 28`, `(3,20)`; at `3769`: `e=1291399`, `(135,46256)` |
| `(10,2,7;1273 mod 1680)` | `2953,7993,11353` | at `2953`: `N=7*1245767`, `-p=7 mod 80`, `(37,15609)`; at `7993`: `e=9126887`, `(100,114186)` |

All reconstructed rows satisfy the defining Type-I equation exactly.

The repaired §35 dictionary matters: at `p=97`, Theorem 35.4's `c=5,D=3` branch gives `(a,b,c,k)=(1,34,5,5)`, while Corollary 44.3 gives `(5,162,5,1)`.  They are different rows and slices sharing the same fixed divisor and hard progression.  The Type-II multiplier identity in §16 supplies that progression by another representation; it does not turn these Type-I rows into one row.

## 5. Residue-one escape

Assume a fixed-divisor class contained `1 mod L`.  Its target condition gives

\[
d=-1\pmod h,
\]

and its norm condition gives `d|(1+4ck^2)=1+hk`.  Put `e=(1+hk)/d`.  Since the norm is `1 mod h`, also `e=-1 mod h`.  Positivity forces

\[
d,e\ge h-1,
\]

but

\[
(h-1)^2-(1+hk)=h(h-k-2),\qquad
h-k-2=k(4c-1)-2\ge1.
\]

Thus `de=1+hk` is strictly smaller than its forced lower bound.  This contradiction covers every positive `d`, prime or composite, and uses no unproved distribution input.

If `L<=Q`, then `h<=Q` and `d<=Q`, so only finitely many triples occur.  The class `1 mod Lambda_Q` reduces to residue one modulo every such `L`, misses every guarantee, and is reduced; Dirichlet gives infinitely many primes in it.  This is the exact §17.3-style compactness wall for preassigned fixed divisors.  It neither proves those primes have vanishing slices nor excludes divisors chosen from each prime's moving norm.

## 6. Register and validation

No line now promotes vanishing to nonsolvability, non-guarantee to vanishing, or finite census data to pointwise progress.  Proposition 48.6 is explicitly a bookkeeping equivalence with the open Type-I strengthening.  The Type-II exceptional-set results in §§16/39 are correctly denied any consequence for `ck_min`; §29 supplies classes but no joint coverage theorem.

Validation performed in the review clone:

- required full command: `uv run --with sympy,numpy,scipy python verify.py` — all checks passed, 113.48 s, 329868 KB peak RSS;
- isolated default `(au)`: all checks passed, 2.63 s, 107264 KB process peak RSS;
- isolated `ES_FULL_SCAN=1` `(au)`: all 1,181 primes and maximum `D=102` passed, 2.08 s, 101372 KB process peak RSS;
- `(au)` keeps one residue set of size at most `4ck` per norm, boolean hit-cache entries, and small per-prime maps; it forms no prime-by-slice dense numeric array;
- `verify.py` was not changed; final AST and control-byte checks pass, and repository hygiene is clean after the review commit.
