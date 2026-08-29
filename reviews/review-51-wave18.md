# Wave-18 hostile review of §51

**Base reviewed:** `8641cfe` plus the two explicitly marked wave-18 repairs in
§51.  **Method:** maximum-severity adversarial replay.  **Overall verdict:**
**SOUND-AFTER-REPAIRS**.  I found one major literal-scope overclaim and one
moderate effectivity-proof omission.  Both are repaired in `notes.md`.  I found
no counterexample to the mathematical prime-tail claims.  The cubic tail and
the repaired-chain effectivity claim must retain their existing
**CLAIMED/PROVISIONAL** labels.

## Claim-by-claim verdicts

1. **Definition of `W(p)` — CONFIRMED.**  Equations (51.1)–(51.2) at
   `notes.md:18420-18430` minimize exactly the modulus `kℓ` in Lemma 16.1.
   Since `(kℓ+1)/4` is coprime to `kℓ`, `v^{-1}` exists.  The definition
   correctly permits composite `ℓ`, permits integer `p`, and makes no
   finiteness assertion.  `W(p)≤T` therefore gives a Type-II representation,
   while the proof is free to use only prime `ℓ`.

2. **Lemma 51.1 — CONFIRMED.**  I replayed the parameter replacement
   `t^3 -> μ=t^2 log K` through the residue profile, all factorial moments,
   bad-fibre estimate, conditioned void, even Bonferroni tail, and rounding
   ledger (`notes.md:18454-18534`).  The actual scales are
   `y=Bμ`, `r=Θ(μ)`, moment base `Cμ`, void `exp(-cμ)`, and coefficient/modulus
   ledger `exp(O(μt))`.  The hypotheses `log K << t` and canonical-box supply
   make `y<X^(1/2)` and `log |A_X|=O(t)` valid.  No line needs `μ=t^3`.
   This confirms only the parameterized replay at §39's existing provisional
   review status.

3. **Theorem 51.2 — CONFIRMED-AFTER-REPAIR-NEEDED, REPAIR APPLIED.**
   With `X=T^(1/2)`:
   - `K=(log X)^5` gives `μ asymp (log T)^2 log log T` and
     `μt asymp (log T)^3 log log T`, exactly (51.12)–(51.13).
   - `K=X^κ` gives `μ asymp_κ (log T)^3` and
     `μt asymp_κ (log T)^4`, exactly (51.14)–(51.15).
   - `KX≤T` in both choices, and the cubic floor condition at the lowest
     dyadic block is precisely `κ<1/240`.

   The displayed sets originally omitted “`p` prime”, even though `W` had
   just been defined for all integers and the proof uses `S_y(p)=1` only for
   primes.  That was a literal all-integer overclaim.  The exact repair at
   `notes.md:18536-18541` restricts every set in Theorem 51.2 and Corollary
   51.3 to primes.  After that repair, variant (1) is unconditional in the
   no-unproved-hypothesis sense but inherits §39 review status; variant (2)
   still inherits Theorem 34.8 and is correctly labelled
   **CLAIMED/PROVISIONAL**.

4. **Corollary 51.3 and `H_MOD(A)` — CONFIRMED-AFTER-REPAIR-NEEDED, REPAIR
   APPLIED.**  Substitution `T=(log N)^A` gives (51.17) and (51.18), including
   the fixed powers of `A`.  The theorem windows are automatic for fixed
   `A`.  For the varying cutoff, primes in `[N^(1/2),N]` have
   `(log p)^A >= 2^{-A}(log N)^A`; the lower half is negligible against either
   stated bound.  `H_MOD(A)` is explicitly unproved and only implies eventual
   prime solvability.  The prime-scope repair above also repairs the
   corollary's formerly ambiguous displayed sets.

5. **Lemma 51.4 — CONFIRMED-AFTER-REPAIR-NEEDED, REPAIR APPLIED.**  The
   effective excluded-conductor Bombieri–Vinogradov form is standard and the
   max over reduced residues is the right form.  The original sketch did not
   pay for all small primitive conductors induced into all multiples, and its
   pointwise `ψ` statement did not by itself justify a dyadic `π` statement:
   independently applying it at `x` and `2x` could select different Page
   conductors.  The repair at `notes.md:18692-18717` supplies the missing
   count
   
   `sum_{q≤Q,r|q} 1/φ(q) << log(2Q)/φ(r)`,
   
   sums the at most `φ(r)` primitive characters for every
   `r≤R=(log x)^B0`, records the effective
   `exp(-c sqrt(log x))` saving, treats conductor 4 directly, and chooses one
   Page conductor for the whole dyadic interval before partial summation.
   This is enough to absorb all `(log x)^O(1)` small-conductor and induction
   multiplicities.  The remaining large-conductor Vaughan-identity/large-
   sieve step is genuinely the standard BV proof.

   **Citation caveat:** `notes.md:18682-18687` cites only Davenport chapters,
   without edition, theorem number, or a checked source containing the exact
   excluded-conductor dyadic/max-residue formulation.  The repaired dependency
   sketch closes the mathematical bookkeeping, but publication should add a
   precise bibliographic citation or present this as a derived standard
   variant rather than as a verbatim cited theorem.

6. **Lemma 51.5 — CONFIRMED.**  I replayed both ranges and both intersections.
   For each primitive real conductor other than 4, choose an odd `p|r`, or
   `p=2` for `r=8`.  Then `p∤uv` implies `r∤4uv`.  For fixed `k`:
   - if `p|k`, deletion costs nothing because `(uv,k)=1`;
   - if `p∤k` and `p≤Ck`, CRT modulo `kp` changes the coprime-pair local
     factor by exactly `(p-1)/(p+1)≥1/3`;
   - if `p>Ck`, the discarded weighted main term is at most `O(1/(pk))`
     versus `asymp φ(k)/k^2`, a ratio
     `O(k/(pφ(k)))=O(1/C)`, and the `H=K^10` boundary is uniformly negligible.

   These are pointwise-in-`k` estimates, so an adversarial subfamily or fibre
   cannot average away the retained fraction.  Choosing the Rankin cutoff
   constant `D` so the low-omega tail is smaller than half that fraction, and
   then subtracting Lemma 34.7's `o(1)` original mass, leaves a fixed positive
   fraction after both low-omega and low-congestion pruning.  The proof at
   `notes.md:18722-18770` is compressed, but its asserted uniformity survives
   the replay.

7. **Theorem 51.6 and its perimeter — CONFIRMED-AFTER-REPAIR-NEEDED, REPAIR
   APPLIED.**  Once Lemma 51.4 is repaired, every dyadic block can select its
   own possible exceptional conductor, Lemma 51.5 retains a uniform box mass,
   and the original class family inherits the effective lower bound from the
   retained subfamily.  The exceptional conductor need not remain fixed as
   the scale changes.

   The scope caveat at `notes.md:18788-18795` is exact.  Lemma 39.5 invokes
   Theorem 34.8 only through the class mass (34.18), in (39.27): it takes the
   good retained classes, forms a product over their distinct prime
   coordinates, and obtains `exp(-c t^3)`.  Theorem 39.4 is an upper-moment
   argument; Theorem 39.6 uses that moment, the void, and exact class counting.
   None uses Theorem 34.8's separate all-low-congestion-triples absolute-error
   `o(1)` sentence.  Theorem 16.4 uses (16.8) plus an elementary larger sieve;
   Theorem 16.5 is an effective partial-summation/Rankin semigroup transfer.
   The §39 `N`-side is finite Bonferroni algebra and exact integer congruence-
   class counting.  I found no hidden Siegel–Walfisz input outside the repaired
   supply side.

8. **PW comparison and window dictionary — CONFIRMED.**  I checked PW §4 in
   `sources/pomerance-weingartner-2025.pdf`.  Its Lemma 4.1 proves square-log
   class mass, explicitly uses Bombieri–Vinogradov for the lower bound after a
   polylogarithmic multiplicity bound, and then uses the larger-sieve Rankin
   truncation.  Stopping at prime modulus `T` gives mass `(log T)^2` and the
   window `log N >= C(log T)^3`.  Section 51's choice `X=T^(1/2)` changes only
   constants and adds the real factors `log K asymp log log T` or
   `log K asymp log T`.  At the cubic top,
   `T=exp(alpha(log N)^(1/4))`, (51.15) is exactly the prime part of (39.35)
   up to constants.  The text fairly credits PW and explicitly disclaims a
   direct Vaughan audit.

9. **Computational 51.7 and merge hygiene — CONFIRMED.**  I ran
   `uv run --with sympy,numpy,scipy python verify.py` in the foreground with a
   300-second timeout; every block through `(ay)` passed.  Block `(ax)` at
   `verify.py:8961-9121` returned tails `(226,19,0,0)`, maximum `279`, the
   exact period-39,215 inclusion–exclusion regression, and all deletion toys.
   Its nested loops enumerate every ordered factorization `uvw=(M+1)/4`:
   every `u|A`, every `v|(A/u)`, and the forced cofactor `w`.  Sets deduplicate
   classes correctly.  Because `k=1, ℓ=M` realizes the complete Lemma-16.1
   class set for every `M≡3 mod 4`, and every tested prime has a found minimum
   below 3000, the computed minima (including maximum 279) are the true `W`
   values for the tested primes, not merely upper bounds from an incomplete
   harvest.  The section's “in that truncated family” wording is conservative,
   not a conflation.

   A byte scan found zero forbidden control bytes and zero carriage returns in
   §51.  `git diff --check` passed.  Tags (51.1)–(51.27) occur exactly once and
   consecutively; §52 starts at (52.1).  I found no eaten-backslash token.  The
   targets (16.7), (16.8), (34.18), (34.21), (39.25), (39.27), and (39.31)
   say exactly what §51 attributes to them.

## Mandatory quantifier chains and breaks

### Theorem 51.2(2)

**Full chain.**  For every fixed real `κ` with `0<κ<1/240`, there exist
positive, effectively computable constants `C_κ`, `c_κ`, an implied-constant
`A_κ`, and an effective bounded-range threshold `T_0(κ)` such that, for every
real `T≥3` and every `N` satisfying

`log N ≥ C_κ(1+(log T)^4)`, 

the number of **primes** `p≤N` with `W(p)>T` is at most

`A_κ N exp(-c_κ(log T)^3)`.

The constants may depend on `κ` and on the fixed constants in Theorem 34.8,
§39's profile/moment bounds, and the effective BV repair; they do not depend
on `T`, `N`, a dyadic block, a multiplier subfamily, or a fibre.  Inside the
proof, for every dyadic block and every surviving data-dependent subfamily
`J_c`, the class-supply constants are uniform; `r_x` may depend on that block
but deletion tolerance is uniform in every possible `r_x`.

**Break attempts.**

- **`κ -> 0`:** then `K=X^κ` takes arbitrarily long to exceed `K_0`, and the
  mass constant is proportional to `κ`.  No break: the theorem fixes `κ`
  first and permits every constant and bounded threshold to depend on it.
- **`κ -> 1/240`:** in the lowest block,
  `z≥X^(1/12)` while `H^2=K^20≈X^(20κ)`.  Strict `κ<1/240` gives the needed
  margin.  Equality would break the floor argument and is correctly excluded.
- **Top of the window:** with `t=(1/2)log T`, the hypothesis is
  `log N >= C_κ t^4`; hence `T≤exp(c_κ'(log N)^(1/4))`.  The ledger is
  `exp(O(t^4))` and the tail exponent is `Θ(t^3)`, so neither is silently
  evaluated outside its range.
- **Bounded `T`:** asymptotic box supply is unavailable, but enlarging the
  implied constant gives the trivial bound.  This dependence is allowed.

**Outcome:** no break; claim confirmed at its inherited provisional status.

### Lemma 51.4

**Full chain.**  For every `A>0`, there exist effectively computable
`B=B(A)`, `C=C(A)`, `x_0=x_0(A)`, and a chosen small-conductor exponent
`B_0=B_0(A)` such that, for every `x≥x_0`, one may choose either no conductor
or one primitive real conductor `r_x≥3`, `r_x!=4`, depending on the dyadic
scale but not on `q`, `a`, or the partial-summation point `y∈[x,2x]`, with the
following uniform property: for every `Q≤x^(1/2)/(log x)^B`, the sum over all
`q≤Q` not divisible by `r_x`, with the maximum over every reduced residue
`a mod q`, is at most `Cx/(log x)^A`.  The same one `r_x` controls the dyadic
`π` difference.  If there is no Page character the divisibility restriction
is absent.

**Break attempts.**

- **Many imprimitive lifts of a small conductor:** for each primitive
  conductor `r`, the total lift weight is
  `<<log(2Q)/φ(r)`, not `Q/r`; multiplying by at most `φ(r)` primitive
  characters and summing `r≤(log x)^B0` is still only a fixed log power.
  The effective `exp(-c sqrt(log x))` nonexceptional saving wins.
- **Two endpoint conductors:** applying a pointwise theorem separately at
  `x` and `2x` could delete two conductors.  This was a real proof omission.
  The wave-18 repair selects Page once at `2x` and proves a uniform
  `[x,2x]` estimate before partial summation.
- **Conductor 4:** every supply modulus `4uv` is divisible by 4, so blindly
  selecting `r_x=4` would delete the entire family.  The repair treats all
  fixed conductors, including 4, effectively before selecting the unresolved
  Page conductor.
- **`r_x` changes when `x` crosses a scale:** no break.  The supply argument
  is blockwise, and Lemma 51.5 is uniform for every possible conductor.
- **Non-real characters near 1:** the effective classical zero-free region
  leaves only one possible real primitive exceptional character.  Complex
  characters require no second deletion.

**Outcome:** confirmed after the applied dependency and dyadic-uniformity
repair.  A precise external citation remains desirable.

### Lemma 51.5

**Full chain.**  There is an absolute retained fraction `δ>0`; after choosing
an absolute split constant `C` sufficiently large and the fixed low-omega
constant `D` sufficiently large, for every admissible box scale, every
`K`, every subfamily `J` containing 1, every reduced fibre `c`, and every
primitive real conductor `r!=4`, there exists one prime `p=p(r)` such that,
for every `k∈J`, the harmonic mass of admissible `(u,v)` with `p∤uv` is at
least `δ` times the uncut `k`-box mass.  The same `δ` is independent of
`r,p,k,c,J,K,z`.  After imposing `omega(uv)≤D log log X`, a positive absolute
fraction remains.  For the power-sized setup of Theorem 34.8, after also
imposing `r_J(u,v;c)≤(log X)^4`, the retained mass is still of the original
order, uniformly in `J,c`; the sufficiently-large threshold may depend on
fixed `κ` but not on the fibre or conductor.

**Break attempts.**

- **Adversarial `r` whose chosen `p` divides `k`:** deletion is then free,
  because `(uv,k)=1` already excludes `p`.
- **Transition `p≈Ck`:** below the transition the exact local retained factor
  is at least `1/3`; above it the deleted fraction is `O(1/C)`.  There is no
  uncovered middle regime.
- **Huge `p>z`:** no pair is deleted.  The direct estimate only improves.
- **Sparse family `J={1}`:** both range estimates are pointwise in `k`, so
  no averaging hypothesis is needed.
- **Fibre chosen to force `p|u` or `p|v`:** if `p∤k`, the condition
  `u+cv=0 mod k` is independent of the added nonzero conditions modulo `p`;
  CRT gives the same local factor for every `c`.  If `p|k`, deletion is free.
- **All retained pairs lie in the high-omega or high-congestion tail:** choose
  the Rankin tail below `δ/2` of original mass; Lemma 34.7 removes only
  `o(1)` of original mass.  Their union cannot consume the retained `δ`.

**Outcome:** no break; confirmed.

### Theorem 51.6

**Full chain.**  For the fixed-polylogarithmic §16 chain there exist absolute
effective class-mass and downstream constants.  For every fixed
`0<κ<1/240` in the cubic chain, there exist effective constants and
thresholds depending at most on `κ`.  For every sufficiently large supply
scale, every dyadic block, every allowed multiplier subfamily (including the
data-dependent `J_c`), and every reduced fibre, choose the block's possible
Page conductor and retain only `r_x∤4uv`.  Lemma 51.5 supplies a uniform
positive box mass and Lemma 51.4 supplies an effective progression error.
Therefore the lower class-mass conclusions (16.8) and (34.18)–(34.19) have
effective constants.  For every later `N` satisfying the relevant window,
the larger-sieve, moment, Chernoff, Bonferroni, exact class-counting, and
semigroup steps propagate those effective constants.  This assertion does
**not** quantify over or make effective the absolute-error sum on all
low-congestion triples in Theorem 34.8's first sentence.

**Break attempts.**

- **Changing `r_x` between blocks:** permitted; no downstream family must use
  one global deletion.  Each retained block is a subset of the fixed c-free
  family, and class masses add.
- **Data-dependent `J_c`:** Theorem 34.8 and Lemma 51.5 are uniform in every
  subfamily containing 1.  On good fibres, `1∈J_c` and
  `h(J_c)>>log K`, exactly as required in Lemma 39.5.
- **Hidden use of Theorem 34.8's all-triples error:** side-by-side replay of
  (34.18), Lemma 39.5, (39.27), and Theorem 39.6 found none.  Only positive
  retained class mass enters the void.
- **Hidden ineffective `N`-side input:** Theorem 16.4's lcm bound may use
  effective Chebyshev bounds; its larger sieve is elementary.  Theorem 16.5
  and the §39 all-integer transfer use partial summation and Rankin's
  inequality.  §39's interval transfer counts explicit CRT classes with an
  `O(1)` rounding error.  No prime-progression theorem appears there.

**Outcome:** confirmed after the Lemma 51.4 repair.  This is effectivity
conditional on the correctness of the already provisional §34/§39 chain,
not validation of that chain.

## Attempted-breaks log (other claims)

| Target | Adversarial test | Outcome |
|---|---|---|
| Definition | Composite `ℓ`, nonprime/integer `p`, noninvertible `v` | Composite `ℓ` is allowed; `v` is automatically invertible because `v|(kℓ+1)/4`. |
| Lemma 51.1 | `y=Bμ` rather than `Bt^3`; low order `m`; `y>K`; rounding ledger | Chernoff and moment induction are parameter-free in `μ`; `y>K` only makes all multiplier primes conditioned; degree and ledger still shrink. |
| Lemma 51.1 | Compatible atoms sharing `ℓ` at general `K` | The determinant uses `u,v≤X^(1/6)` and `ℓ>X^(1/2)`; uniqueness of `k` uses `4uv>K`, built into the canonical floor. |
| Corollary | Varying cutoff near the lower half `p≤N^(1/2)` | Trivial lower-half count is absorbed; upper-half logs are comparable. |
| PW comparison | Compare `T` with §51's `X`, not with `KX` | `X=T^(1/2)` leaves room for `K`; logarithms differ only by constants, so enrichment factors remain `log log T` and `log T`. |
| Computational | Missing ordered factorizations or class duplication | Exhaustive divisor nesting enumerates all ordered `u,v,w`; set union is intentional; `k=1` is complete at fixed `M`. |
| Merge | Control bytes, carriage returns, missing TeX backslashes, duplicate tags | None found; all checks green. |

## Severity-ranked defects

1. **MAJOR — REPAIRED: theorem/corollary literally counted all integers.**
   Before the repair, (51.13), (51.15), (51.17), and (51.18) wrote only
   `{p≤N:...}` after `W` was explicitly defined for primes **or integers**.
   Lemma 51.1 and the Bonferroni selector prove only the prime count.  Exact
   repair: `notes.md:18536-18541` now imposes prime scope on every set in the
   theorem and corollary.

2. **MODERATE — REPAIRED: the effective BV sketch skipped the induced-
   character multiplicity and single-conductor dyadic quantifier.**  The old
   “same by partial summation” did not follow from a pointwise statement whose
   exceptional conductor could change with the endpoint.  Exact repair:
   `notes.md:18692-18717` adds the weighted lift count, exponential saving,
   conductor-4 treatment, and one-conductor dyadic construction.

3. **MINOR — OPEN BIBLIOGRAPHIC REPAIR: citation is not precise enough.**
   `notes.md:18682-18687` names Davenport chapters but gives no edition,
   theorem/page, and no archived source was available to verify that the
   exact max-residue, excluded-conductor, dyadic `π` formulation is stated
   there.  Add a precise checked citation, or call Lemma 51.4 a standard
   derived variant supported by the now-expanded dependency sketch.

No other defect survived the attempted breaks.

## Labels and final adjudication

After the two applied repairs, §51 is **SOUND-AFTER-REPAIRS**.  The original
prime-scope omission was an actual overclaim; it is no longer present.  I do
not find any remaining mathematical label overclaim.  In particular:

- Theorem 51.2(1) says “unconditional” only in the no-unproved-hypothesis
  sense and repeatedly retains §39's review qualification.
- Theorem 51.2(2) and its polylogarithmic specialization remain explicitly
  **CLAIMED/PROVISIONAL**.
- Theorem 51.6 remains **CLAIMED/PROVISIONAL** and correctly claims
  effectivity of the exceptional-set chain, not effective control of every
  clause of Theorem 34.8.
- Neither `H_MOD(A)` nor pointwise finiteness of `W(p)` is asserted.

**Signed review statement.**  I fully replayed the definition, both scale
specializations, the `μ`-parameterized §39 moment/Chernoff/void/Bonferroni
ledger, the exceptional-conductor deletion mass in both `p` ranges, all four
mandatory quantifier chains, the exact §34.8-to-§39.5 dependency, the PW §4
truncation, block `(ax)`, cross-references, numbering, and byte/TeX hygiene.
I checked the large-conductor Vaughan-identity/large-sieve portion of
Bombieri–Vinogradov and the underlying §34.8/§39 profile theorems
structurally against their stated hypotheses rather than re-proving those
standard or campaign-provisional analytic arguments from first principles;
my verdict therefore does not upgrade their existing provisional status.
