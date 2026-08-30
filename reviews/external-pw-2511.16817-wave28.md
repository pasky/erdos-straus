# External review: Pomerance–Weingartner, arXiv:2511.16817v2 (wave 28)

**Artifact:** `sources/pomerance-weingartner-2511.16817/` (current arXiv v2,
25 pages, fetched 2026-08-30).  **Method:** full PDF read, including the
Type-I/Type-II parametrizations, the proofs of Theorems 1.1--1.4, the
explicit estimates, and the bibliography.  This is a literature and priority
audit, not an independent proof of the paper's analytic estimates.

## Verdict

The paper does **not** displace any of the campaign's three provisional
priority positions.  At `m=4` it repeats Vaughan's `2/3` logarithmic exponent,
not a larger one.  Its general-`m` Theorem 1.3 is exactly the
Pomerance--Weingartner benchmark already transcribed in Section 43, so the
formal crossover with **CLAIMED/PROVISIONAL** Theorem 43.12 does not change.
It neither formulates a minimal witness modulus nor states a witness-modulus
tail or an effectivity theorem, and it does not cite Dahan.

There is no conflict between its large-`m` exceptional-prime constructions
and Theorem 43.12/Section 55.  The constructed primes live at
`log p = m^(1/3+o(1))` (or `log p = O(log m)` in the explicit theorem), while
the campaign's fixed-gap range starts at
`log N >= m^(1/(3-epsilon))`, a strictly larger power.  The precise exponent
gap is recorded below.

A source-control anomaly explains why the benchmark was already familiar:
`sources/pomerance-weingartner-2025.pdf` is the November 2025 version of this
same arXiv paper, not a different Pomerance--Weingartner paper.  Wave 28
archives v2.  Theorem 1.3 and the priority conclusions are unchanged between
the two versions.

## Statements extracted from the paper

### 1. Explicit-in-`m` Vaughan bound

Quote first.  Theorem 1.3 states:

> “There is an absolute positive constant C such that for each pair m, N
> with 4 <= m <= log^2 N the number of n <= N with m/n not the sum of 3
> unit fractions is at most N/exp(C log^(2/3)(N)/phi(m)^(1/3)).”

(Pomerance--Weingartner, Theorem 1.3, p. 2.)  Thus, with `L=log N`, the
published exponent scale is

`P(m,N) = L^(2/3)/phi(m)^(1/3) = (L^2/phi(m))^(1/3)`,

uniformly on the stated range `4 <= m <= L^2`; `C` is absolute.  The theorem
counts **all integer denominators** `n <= N`, not only primes.

On effectivity, the exact wording is only “There is an absolute positive
constant C” (Theorem 1.3, p. 2).  The paper does not say “effective,”
“computable,” or give a threshold or value for `C`.  Lemma 4.1's lower bound
says “We now use the Bombieri--Vinogradov theorem” (p. 9), while the upper
bound uses Brun--Titchmarsh (pp. 8--9), and the denominator-side step says
“We now employ the large sieve” (p. 10).  Therefore the paper's effectivity
status is **not asserted**, rather than proved ineffective.  This agrees with
the campaign's Section 51.9 audit.

### 2. The lower exceptional-prime construction

Theorem 1.1 itself says:

> “For each epsilon > 0 there is a bound m(epsilon) such that for each
> m >= m(epsilon) there is some n > exp(m^(1/3-epsilon)) with m/n not the
> sum of 3 unit fractions.”

(Theorem 1.1, p. 2.)  This statement does not call `n` prime.  The proof is
stronger.  Theorem 3.1 says:

> “There is a constant c > 0, such that for every integer m >= 8, there are
> more than exp{c phi(m)^(1/3)/(log m)^(2/3)} primes p for which (3.1) has
> no solution in natural numbers x,y,z.”

(Theorem 3.1, p. 6.)  Its proof chooses

`N = exp{(phi(m)/(C log^2 m))^(1/3)}`

and concludes that most primes in `(N/2,N]` have neither type of solution
(pp. 7--8).  The line after the proof explicitly derives Theorem 1.1 using
“more than exp(m^(1/3-epsilon)) primes p” (p. 8).  Hence the witnesses
actually produced for Theorem 1.1 are prime, even though primality is omitted
from its headline.

The obstruction is not one fixed congruence class.  First the paper proves
that for prime `p` with `p` not dividing `m`, every solution is, up to
permutation, Type I or Type II (definition and observation, p. 3).  Its exact
necessary-and-sufficient prime parametrizations give:

> Type I: `p == -f (mod mad)`, with `f | ma^2 d + 1`.

(Corollary 2.2 as used in Theorem 3.1, p. 6.)

> Type II: `p == -e (mod mab)`, with `e | a+b`.

(Corollary 2.4 as used in Theorem 3.1, p. 7.)

Brun--Titchmarsh bounds the union of the Type-I admitting classes; a parallel
count bounds the Type-II admitting classes.  Most primes in the selected
dyadic interval avoid both unions (pp. 6--8).  Thus their “congruence
obstruction” is avoidance of every parametrized **solution-admitting** class,
not a residue class alleged to forbid solutions by itself.  This is the
Elsholtz--Tao Type-I/Type-II counting route generalized from `m=4` (Theorem
3.1, p. 6).

### 3. Numerically explicit exceptional prime

Theorem 1.2 states:

> “For each integer m >= 6.52 x 10^9 there is a prime p in (m^2,2m^2) for
> which m/p is not the sum of 3 unit fractions.”

(Theorem 1.2, p. 2.)  Here primality is part of the theorem.  The proof uses
the same complete prime-denominator Type-I/Type-II split: Proposition 7.5
bounds Type-I-representable primes by `698 N^(4/3)/m^(7/6)` (p. 20),
Corollary 9.1 bounds Type-II-representable primes by
`(1/10)N^(4/3)m^(-7/6)` (p. 23), and the elementary explicit lower bound for
primes in `(N/2,N]`, with `N=2m^2`, exceeds their sum once
`m >= 6.52 x 10^9` (Theorem 1.2 proof, p. 23).  The empirical statement is
not a theorem: Section 6 verifies the claim for `m in [16,30000]` except
`m=19` and conjectures it for every `m >= 20` (p. 12).

### 4. Every description of Vaughan in the paper

The full set of substantive Vaughan descriptions is short:

1. > “A result of Vaughan is that for each m, most n's have m/n
   > representable; we make the dependence on m in this result explicit.”

   (Abstract, p. 1.)
2. > “In 1970, Vaughan [13] gave the upper bound
   > N/exp(c log^(2/3) N) for a positive constant c.”

   (Introduction, p. 2.)
3. > “Exploiting the large sieve, the proof is largely derivative of
   > Vaughan's theorem in [13].”

   (Immediately after Theorem 1.3, p. 2.)
4. > “Our proof largely follows the argument in Vaughan [13].”

   (Opening of Section 4, p. 8.)
5. > “As shown in [13] for each p there are at least f(p) residue classes
   > mod p such that if n lies in one of them, then m/n is a sum of 3 unit
   > fractions.”

   (Section 4, after (4.1), p. 8.)

The next sentence supplies the route: “The strategy is to use the large sieve
to show that the number of n <= N lying outside of these f(p) residue classes
mod p for each p is bounded above by the bound in Theorem 1.3” (Section 4,
p. 8).  Lemma 4.1 proves
`sum_{p<=x} f(p)/p asymp (log x)^2/phi(m)` (pp. 8--9); the large-sieve product
is optimized with `log X asymp phi(m)^(1/3)(log N)^(1/3)` (pp. 10--11).
This is fresh secondary evidence for both Vaughan's statement and route, but
it is not a substitute for a direct reading of the still-inaccessible 1970
paper.

### 5. `m=4`, `m=5`, and the `j`-fraction theorem

The introduction says the exceptional count was “strongly improved, though
not recently” immediately before attributing the `2/3` bound to Vaughan
(p. 2).  The paper's own Theorem 1.3 specializes at `m=4` (and fixed `m=5`)
to the same `L^(2/3)` exponent.  It states no `m=4` all-denominator bound with
a larger logarithmic exponent.  Theorem 3.1 starts at `m>=8` (p. 6), and
Theorem 1.2 concerns very large `m`, so neither is an `m=4` or `m=5` upper
bound.  The numerical facts are verification only: Section 6 reports `m=4`
and `m=5` checked through `10^18` (pp. 12--13), and Remark 8.2 reports that
every prime below `10^13` has a Type-II solution for `m=4`, and likewise for
`m=5` except 2 and 5 (p. 21).

Theorem 1.4 says:

> “For each pair of positive integers j,k, there is a number m(j,k) such
> that for each m >= m(j,k), we have m/(km+1) not the sum of j unit
> fractions.”

(Theorem 1.4, p. 3.)  Its proof uses discreteness of sums of a fixed number
of unit fractions: Lemmas 5.1--5.2 produce a left-hand gap below `1/k`, and
`m/(km+1)` eventually lies in it (pp. 11--12).  It neither uses nor modifies
the Type-I/Type-II split, which is a complete classification only in the
three-summand prime-denominator setting (p. 3).  It therefore has no bearing
on the campaign's Type-I/Type-II witness-modulus tails.

## Reading-comprehension check of the key logic

- **Prime completeness:** the paper explicitly restricts completeness of the
  Type-I/Type-II dichotomy to prime `n`, `n` not dividing `m`, `m>=4`
  (p. 3).  Both exceptional-prime arguments work in that domain.
- **Theorem 3.1:** Corollaries 2.2 and 2.4 turn every possible solution into
  one of the two displayed congruence families.  The proof upper-bounds each
  union and selects `N` so each is `o(pi(N)-pi(N/2))` (pp. 6--8).  This
  logically yields uncovered primes, not merely primes missing one type.
- **Theorem 1.3:** (4.1) supplies many good denominator classes at each
  auxiliary prime, Lemma 4.1 gives square-log total class mass, and the large
  sieve bounds simultaneous avoidance.  The Rankin choice on pp. 10--11
  produces exactly the `L^(2/3)/phi(m)^(1/3)` scale.
- **Theorem 1.2:** Proposition 7.5 and Corollary 9.1 count the two exhaustive
  solution types in the same interval, and their sum is strictly below an
  explicit lower bound for all primes there (p. 23).

This check confirms the quantifier flow visible in the paper.  It does not
independently reprove estimate (3.3), Lemma 4.1, or the long explicit
constants in Sections 7--9.

## Priority audit against the campaign

### Theorem 39.7

**Verdict: would-be-record framing survives this source, still only
CLAIMED/PROVISIONAL.**  Pomerance--Weingartner explicitly identify Vaughan's
`N exp{-c(log N)^(2/3)}` bound and reproduce exponent `2/3` at `m=4`
(Introduction and Theorem 1.3, p. 2).  No theorem or implication in the paper
gives an `m=4` all-denominator saving with exponent greater than `2/3`.
Thus it does not anticipate Theorem 39.7's claimed `3/4` exponent.  The
paper's phrase “strongly improved, though not recently” is useful fresh
secondary state-of-art evidence, not a complete literature guarantee and not
an upgrade of Theorem 39.7's status.

### Theorem 43.12

**Verdict: benchmark and crossover unchanged.**  Theorem 1.3 is exactly
(43.32).  Let `L=log N`.  The published scale and the campaign's
**CLAIMED/PROVISIONAL** scale are

`P = L^(2/3)/phi(m)^(1/3)`,

`R = (eta_2(m)L^3/phi(m))^(1/4)`.

Direct division gives

`R/P = (eta_2(m)^3 phi(m) L)^(1/12)`;

hence formally `R>=P` exactly when
`L >= 1/(eta_2(m)^3 phi(m))`.  Below that threshold PW has the larger formal
scale; above it Theorem 43.12 does.  Unknown constants prevent a finite
numerical crossover.  PW is proved for `m<=L^2`; Theorem 43.12 is available
through each fixed-gap range `m<=L^(3-epsilon)` but remains provisional.
There is therefore no new uniform-beating claim to add and no comparison row
to change.

### Consistency with the lower exceptions

Fix a campaign range gap `0<sigma<3`.  Theorem 43.12/Section 55 requires

`m <= (log N)^(3-sigma)`, equivalently
`log N >= m^(1/(3-sigma))`.

The exact exponent gap is

`1/(3-sigma) - 1/3 = sigma/(3(3-sigma)) > 0`.

In the proof of Theorem 3.1, the exceptional primes lie below
`N_0 = exp{(phi(m)/(C log^2 m))^(1/3)}` and in fact in `(N_0/2,N_0]`
(pp. 7--8).  Thus `log p = m^(1/3+o(1))`, and

`m/(log p)^(3-sigma) = m^(sigma/3+o(1)) -> infinity`.

So those primes violate the campaign's range hypothesis for every fixed
`sigma>0`.  Equivalently, the campaign threshold has the larger power
`m^(1/3+sigma/(3(3-sigma)))`.  The explicit Theorem 1.2 primes satisfy
`log p=2 log m+O(1)`, even farther outside:
`m/(log p)^(3-sigma) -> infinity`.  **No contradiction exists.**  This is a
range separation, not an assertion that exceptional primes cannot occur
inside the campaign's range; the campaign theorem is an upper count, not a
zero-exception theorem.

### Theorems 51.2 and 51.6

**Verdict: no new witness-modulus priority impact.**  Section 4 has the
`k=1` good-class family already used in campaign Section 51.4 to extract the
weaker square-log truncated tail.  The paper itself does not define the
minimal modulus `W`, state a tail in `T`, state a polylogarithmic witness
bound, or perform exceptional-conductor deletion.  Accordingly it does not
anticipate Theorem 51.2's multiplier tails.  It also makes no computability
claim for Theorem 1.3, so it does not anticipate the record-adjacent,
**CLAIMED/PROVISIONAL** effectivity assertion in Theorem 51.6.

The bibliography on pp. 24--25 has 13 items and does not cite Benjamin Dahan
or arXiv:2608.24035.  Nothing else in it occupies the campaign's minimal
witness-modulus turf.  Chronologically, v2 predates that August 2026 arXiv
identifier.

### Repository and outcome cross-check

- Section 11.4's reconstruction of Vaughan's `f_m(q)` good classes, square-log
  mass, and large-sieve route agrees with Section 4, pp. 8--11.  V2 adds no
  primary-source access and does not validate details absent from its own
  secondary account.
- Section 39.7's priority-search note is strengthened, not settled, by the
  v2 Introduction's unchanged “strongly improved, though not recently”
  wording.  Its search-result caveat remains necessary.
- Section 43's benchmark formula and Section 55.3's truncated comparison are
  unchanged.  The exception construction adds the range-separation check,
  not a new upper-bound regime.
- Sections 51.4 and 51.9 already identify exactly what can be truncated from
  PW and exactly what PW does not claim about effectivity.  V2 supplies no
  amendment.
- `PROJECT.md` Outcome 19's PW benchmark remains accurate; its campaign-side
  exponent capsule is historical and must be read through the later,
  strengthened Theorem 43.12 comparison.  Outcome 22's PW antecedent and
  Theorem 51.6 perimeter remain accurate.  Outcome 26's general-`m` tail
  window is consistent with (68.4)--(68.5); the lower exceptions lie outside
  it.  Historical outcomes need no retroactive edit.

## Final assessment

The only priority-relevant update is evidentiary: v2 is a fresh, explicit
secondary description of Vaughan's bound, good-class construction, and
large-sieve route.  Substantively it is the same paper already serving as
the Section 43/51 benchmark.  Theorem 39.7 remains a plausible first
post-1970 exponent improvement **if** its provisional proof survives expert
review; Theorem 43.12 retains the same proved-versus-provisional comparison;
and Theorems 51.2/51.6 retain the same PW antecedent and effectivity
qualification.  No campaign theorem is promoted by this audit.
