# Wave 17 hostile review: §50 conditional slice routes

## Verdict

**SOUND-AFTER-REPAIRS.**  The prime-factor reduction is exact, including the moving genus sign, raw/primitive boundary, and all size conditions.  The conditional implication survives complete re-derivation.  I found no theorem-level gap.  I repaired the quantifiers and a false “weakest hypothesis” description of `H_SPF(A)`, a malformed product in Theorem 50.5, and the omitted prime qualifier in (50.12).

## Graded checklist

| # | Grade | Finding |
|---:|:---|:---|
| 1 | **CONFIRMED** | A prime factor `q` in the displayed grade is itself a literal target divisor.  Admissibility forces `q` prime to `4ck` and to `p`; its complement has the same grade.  The reconstructed positive row satisfies the Type-I equation and unit-fraction identity exactly. |
| 2 | **CONFIRMED** | The good set is exactly the singleton `{-p mod 4ck}` when `chi_s(p)=-1`, and empty when `chi_s(p)=+1`.  There is no missed two-element-subgroup alternative: `N/q` is target-grade iff `q` is target-grade. |
| 3 | **CONFIRMED** | The reduction needs only raw slice positivity.  A prime target divisor need not give coprime `a,b`; this does not invalidate the solution.  The `p=241` example explicitly exercises this boundary. |
| 4 | **CONFIRMED** | No unmentioned divisor-size window is needed once `(c,k)` is admissible.  Under `H_SPF(A)`, the log-power bound implies every condition in `B_p` for sufficiently large `p`. |
| 5 | **REPAIRED** | `H_SPF(A)` now fixes `A` before quantifying `p_0(A)`.  The text no longer calls the log-bounded statement logically weakest: removing its log bound gives a strictly weaker one-prime sufficient hypothesis. |
| 6 | **CONFIRMED** | Bateman–Horn, GRH/Chebotarev, Elliott–Halberstam, Linnik, smooth-value, least-nonresidue, and Duke audits identify real quantifier or projector gaps and do not claim logical independence. |
| 7 | **REPAIRED** | Theorem 50.5's malformed prime product is corrected.  Equation (50.12) now explicitly sums over primes, as required for its `log log Z` asymptotic and `1/8` constant. |
| 8 | **CONFIRMED** | Block `(aw)` reproduces all 385 minima and comparisons, is streamed, and gates the 1,181-prime extension behind `ES_FULL_SCAN=1`.  The full verifier and isolated optional scan pass. |

## 1. Reduction to the last symbol

Let

\[
h=4ck,\qquad N=p^2+4ck^2=p^2+hk,
\]

with `(c,k) in B_p`.  Then `(p,ck)=1`, so `(N,h)=1`.  Any prime `q|N` therefore satisfies

\[
q\nmid 2ck,
\]

and `q != p`, since `N=4ck^2 != 0 (mod p)`.  Thus every inverse used modulo `h` exists.  This also excludes the possible edge cases `q=2`, `q|ck`, and `q=p` without extra hypotheses.

Write `c=s t^2`, with `s` squarefree.  For every prime `q|N`,

\[
\bigl(p(2tk)^{-1}\bigr)^2=-s\pmod q,
\]

so the primitive genus character satisfies `chi_s(q)=1`.  Every prime factor lies in `K_s(h)`.  The target grade has

\[
\chi_s(-p)=\chi_s(-1)\chi_s(p)=-\chi_s(p).
\]

Consequently

\[
\mathcal G_p(c,k)=\{-p\pmod h\}\cap K_s(h)
=
\begin{cases}
\{-p\pmod h\},&\chi_s(p)=-1,\\
\varnothing,&\chi_s(p)=+1.
\end{cases}
\]

This exactly handles the §48 trap.  A purported good prime cannot exist on a genus-forced slice.  Conversely, on an active slice the genus condition alone is not enough: the one literal target grade is still required.

Suppose now `q|N` and `q=-p (mod h)`.  Put `e=N/q`.  Since `N=p^2 (mod h)`,

\[
e=Nq^{-1}=p^2(-p)^{-1}=-p\pmod h.
\]

The complementary-divisor condition has no extra branch.  In fact, for any unit grade `r=q mod h`,

\[
N/q=-p\pmod h\iff p^2r^{-1}=-p\pmod h\iff r=-p\pmod h.
\]

Thus neither “`q` or `N/q`” nor a two-element subgroup enlarges the good set.  A product of other prime factors may still hit the target, but that is a different, weaker divisor mechanism; §50 correctly calls its prime event sufficient rather than necessary.

Define

\[
a={p+q\over h},\qquad b={p+e\over h}.
\]

Both are positive integers.  Substituting `q=ha-p`, `e=hb-p` into `qe=N=p^2+hk` gives

\[
h^2ab-hp(a+b)=hk,
\]

hence

\[
p(a+b)=hab-k=k(4abc-1).
\]

Over the common denominator `pabck`,

\[
{1\over ack}+{1\over bck}+{1\over pabc}
={pb+pa+k\over pabck}={4\over p}.
\]

Admissibility gives `p` prime to `ck`, while reduction of the Type-I equation modulo `p` gives `4abc=1 (mod p)`.  Therefore `p` divides exactly the third displayed denominator.  This is a literal Type-I solution.

The §44 Möbius boundary causes no loss.  The selected prime `q` is a raw target divisor and gives a raw row.  It may have `(a,b)>1`, in which case its primitive slice coefficient can be zero, but the row still proves the unit-fraction identity.  Theorem 17.1's canonical re-decomposition is optional, not an omitted premise.

There is likewise no hidden inequality on `q` or `e`.  Membership in `B_p` supplies

\[
k\le 2p/3,\qquad 4ck\le 2p+k,
\]

which are the complete slice-size conditions in §36.  Under `ck<=(log p)^A`, sufficiently large `p` has `ck<p`, `3k<=2p`, and `4ck<=2p+k`, as used in Theorem 50.2.  The proof therefore legitimately derives admissibility rather than assuming it silently.

Finally, this is exactly §29's prime Type-I class in moving-factor form.  If `q` is fixed first, `q|N` gives the two roots modulo `q`, and `q=-p (mod h)` gives (50.8).  Section 50 changes the quantifier order; it does not change the class.

## 2. The conditional hypothesis

After repair, `H_SPF(A)` has the unambiguous quantifiers

\[
\exists A>0\ \exists p_0(A)\ \forall p>p_0(A),\ p=1\pmod{24},\
\exists c,k,q
\]

with `c,k>0`, `q` prime, and the three conditions in (50.7).  For fixed proposed constants and `p`, the event is finite and decidable: there are finitely many pairs with `ck<=(log p)^A`, and each norm has a finite factorization.  No bound on `q` is needed because automatically `q<=N`.

The implication is exactly “all sufficiently large hard primes,” not all primes.  No finite computation for `p<=p_0` is claimed.  The statement is stronger than arbitrary slice positivity and stronger than the same prime event without the log-power bound.  It is not logically ordered with GRH or Bateman–Horn; the audit correctly says their standard forms do not supply it rather than claiming an independence theorem.

## 3. Three exact instances

The following were recomputed independently from exact factorizations.  “Target divisors” is the literal §44 divisor list in grade `-p mod h`.

| `(p,c,k)` | `h`; factorization of `N` | target grade and target divisors | good prime(s); genus | reconstructed row |
|:---|:---|:---|:---|:---|
| `(73,7,1)` | `28`; `5357=11*487` | `11`; `{11,487}` | `11,487`; `chi_7(73)=-1` | from `q=11`: `(a,b)=(3,20)`, `73(3+20)=1679=4*3*20*7-1` |
| `(241,7,3)` | `84`; `58333=11*5303` | `11`; `{11,5303}` | `11,5303`; `chi_7(241)=-1` | from `q=11`: `(a,b)=(3,66)`, gcd `3`, and both sides are `16629` |
| `(23689,33,2)` | `264`; `561169249=23*313*77951` | `71`; `{7199,77951}` | `77951`; `chi_33(23689)=-1` | `e=7199`, `(a,b)=(385,117)`, and both sides are `11891878` |

In every row `q mod h=e mod h=-p mod h`, and exact rational arithmetic gives

\[
{1\over ack}+{1\over bck}+{1\over pabc}={4\over p}.
\]

The middle row is the critical primitivity regression: `q` is prime and the raw slice is positive, but `(a,b)=3`.  The last row also shows why the target-divisor law is broader than the good-prime law: the composite target divisor `7199=23*313` is in the grade although neither constituent prime is.

## 4. Census audit

Default `(aw)` finds all 385 values before its product guard `128`.  The exact minimum distribution is

```
5:156  7:30  10:36  11:35  13:13  14:15  17:16  19:4
21:15  22:9  23:6  26:10  28:4  29:3  31:1  33:2
34:3  35:1  37:1  38:4  39:2  42:5  43:1  46:1
55:2  62:1  66:4  67:1  69:1  70:1  77:1  78:1
```

The strict records are

```
(73,7), (193,10), (241,21), (1201,34),
(2521,38), (4729,66), (7489,70), (9601,78).
```

The unrestricted and prime-factor minima agree for `311/385`; the prime minimum is larger for `74/385`.  The largest gap is `55` at `p=23689`, where `ck_min=11` but `ck_pr=66`, with `(c,k,q)=(33,2,77951)`.  These values match (50.19)–(50.20) exactly.

For every tested norm, `(aw)` factors once, builds the exponent-capped §44 residue set, and checks each retained good prime's primality, divisibility, target grade, complementary grade, genus sign, Type-I equation, and rational identity.  It therefore verifies the implication, not merely the histogram.  Its set stores at most `4ck` residues and is discarded norm by norm.  The unresolved-prime sets, minima maps, and core cache are small.  No dense prime-by-slice array or Cartesian factor array is formed.

The optional path uses the same algorithm with guard `320`.  An isolated `ES_FULL_SCAN=1` replay finds all 1,181 hard primes below `100000`, maximum `ck_pr=282` at `p=83689`, maximum `ck_min=103`, and 1,529 checked prime-factor implications.  This confirms that the gating and guard are live rather than dead documentation.

## 5. Standard-hypothesis audit

### Bateman–Horn and smooth values

The negative assessment is fair.  Standard Bateman–Horn fixes the polynomial family and averages in its variable; it does not quantify uniformly over every external coefficient `p` in a log-sized `(c,k)` box, nor does it prescribe a factor grade of a composite value.  Moreover a prime value of `N` is `1 mod 4`, while the target divisor is `3 mod 4`, so literal prime-value success forces slice failure.  Smoothness controls factor sizes, not the bounded-exponent product of their grades.  Neither argument is a strawman against a stronger bespoke uniform conjecture; §50 explicitly identifies that stronger statement with the missing input.

### GRH and Chebotarev

The ideal translation is exact.  Chebotarev can count rational primes splitting in `Q(sqrt(-s))` or lying in a ray class, but `q|N(alpha)` asks that a prime ideal above `q` divide the one specified principal ideal `(alpha)`.  Splitting alone does not choose a divisor of `(alpha)`.  Fixing `q` converts the condition to residue classes of `p`; it does not turn the moving disjunction over factors of each `alpha` into one Frobenius condition on `p`.

The class-mass arithmetic in (50.12) is also correct after making `q` prime explicit:

\[
\sum_{ck\le L}{1\over ck}={1\over2}(\log L)^2+O(\log L),\qquad
\sum_{\substack{q\le Z\\q=3\ (4)}}{1\over q}={1\over2}\log\log Z+O(1).
\]

Multiplying these by the two-root density `1/(2ckq)` gives the constant `1/8`.  This is explicitly an upper envelope before deduplication, not a coverage theorem.

A literal joint cyclotomic implementation contains the least common multiple of all conductors through `4L` and the product of candidate primes through `Z`; the naive degree has logarithm on the `L+Z` scale.  GRH-effective main-term domination therefore restricts this direct compositum strategy to `L+Z=O(log N)`.  At `L,Z` of logarithmic size, the ideal independent-events survivor model is

\[
\exp\{-O((\log\log N)^2\log\log\log N)\}.
\]

Even granting an average sieve with `Z=N^theta` only changes the model exponent to `O((log log N)^3)`.  Multiplying by `N` leaves `N^{1-o(1)}` survivors.  This is a modest log-log gain over §17.5's `exp(-c(log log N)^2)` model, but is far weaker than the provisional §39 shape `exp(-c(log N)^{3/4})`.  Section 50 does not promote either model to a GRH-conditional exceptional-set theorem and explicitly says there is no GRH improvement to record.  It also preserves §39's `CLAIMED/PROVISIONAL` label rather than calling that bound unconditional.

### Elliott–Halberstam and Duke

Elliott–Halberstam and generalized levels of distribution average residue classes over the varying prime `p`; their standard outputs can reduce an exceptional set but do not force one factor event for each fixed `p`.  The section makes only that scope claim.

For Duke/class-group routes, the genus pairing is exact: on an active slice the `chi` and `chi*chi_s` terms agree, while on a forced slice they cancel.  Removing this one cancellation does not remove the residual ray characters.  The positive principal/genus contribution is only subpower, and GRH character estimates for interval or ideal sums do not bound the selected divisor Euler product of one norm with an error below it.  This matches §§36 and 44 and makes no silent positivity inference.

## 6. Register and validation

Every actual implication from `H_SPF` or GRH is labelled conditional and the hypothesis is labelled unproved.  Bateman–Horn/Chebotarev/EH/Duke limits are Assessments, the finite data are Computational/informational, and no sentence claims unconditional pointwise progress.  The good set incorporates §48's moving genus obstruction rather than contradicting it; the proof uses §44 raw positivity openly; and the GRH discussion engages §17.5 without upgrading its model calculations.

Validation in the review clone:

- `uv run --with sympy,numpy,scipy python verify.py`: all checks passed, 1:20.71, 330420 KB peak RSS;
- isolated `ES_FULL_SCAN=1` block `(aw)`: passed, 4.33 s, 109160 KB peak RSS;
- three independent exact instances above: all factorizations, target divisors, genus signs, equations, and rational identities passed;
- `verify.py` is unchanged; final AST, control-byte, and repository-hygiene checks pass.
