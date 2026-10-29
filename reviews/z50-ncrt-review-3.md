# z50 ncrt — Astra hostile review 3

Reviewed all of `EXSET_BEYOND_CRT.md` at `b869d03621062d1f77ff75b2aff2a4b75982e6bb`, both previous reviews, K2 Theorem 5.1/Corollary 6.1, LS2 Lemma 1.1, the note's atom definition and Theorem 7.2 expansion, and both Round-4 scripts. Sections 1–7 are context, not a fresh audit of their analytic inputs.

**Overall: MAJOR revision. The exact-covering obstruction survives. The claimed exhaustion of certification mechanisms does not.** R4.1 genuinely handles arbitrarily expensive finite covers of cheap progressions. R4.4 genuinely separates the note's collective atom family from finite word coverings. But R4.0's exclusion is false, R4.2 drops a remainder-cost hypothesis, and R4.5's necessary witness rule wrongly excludes endpoint words with `u=1`—including U-words. The Dickson sketch also fails to establish admissibility. These have concrete repairs; none refutes the reviewed word-class cap or the prime exceptional-set theorem.

| Requested item | Verdict |
|---|---|
| (1) R4.0 / Type II exclusion | **MAJOR** |
| (2) R4.1 / level lowering | **SOUND** for the theorem; **MAJOR** for R4.2's approximate-cover transfer |
| (3) R4.3 | **SOUND-WITH-REPAIRS** |
| (4) R4.4 | **SOUND**, relative to the stated dependencies; its following interpretation needs repair |
| (5) R4.5 / R4.6 | **MAJOR**, repairable witness and admissibility gaps; uniform cost claim needs hypotheses |
| (6) §8.6 / labels / numerics | **MAJOR** |

## 1. R4.0: a definition is not an exclusion theorem

**R3-1 — False necessity and false uniform non-certification, lines 634–638, 716–718, 770.** The tuple `(4cd,a,b)` represents `cn`, so that *same tuple* represents positive `n` iff `c=1`, not iff one of `a,b,c` equals 1. When `a=1` or `b=1`, the table supplies a different word of n. Those are sufficient reparameterizations, not an exhaustive classification of all possible ones.

Nor does the definition of ES5/U prevent a Type-II family with all three parameters at least 2 from implying the existence of a certificate word, uniformly on a progression. Here is a counterexample even with pairwise coprime `a,b,c`:

```
n = 269 + 444j,   (a,b,c,d) = (17+28j, 4, 7, 1),   j >= 0.
4abcd = a+b+cn.
(t,u,v) = (1, 91+148j, 4) is a U-word of n.
```

Both adjacent factors are >1 and the endpoint 4 is divisible by 4. Thus this entire progression, inside `n=1 mod4`, has the displayed all-parameters->1 Type-II solutions and a uniform U certificate. This is not an artifact of nonprimitive scaling.

**Repair:** retain only: “A bare Type-II solution is not, without an additional transformation or argument, a certificate word of n. The exhibited tuple is a word of cn; the table gives sufficient special-case transformations.” Delete “never,” “only,” and the claim that all alternative identities are excluded by definition. Proving an existential property can use a different identity or a nonconstructive argument; the final witness being a word does not classify the possible proofs.

This repair is compatible with R4.4: some Type-II progressions can be word-covered while the entire large atom family cannot be.

## 2. R4.1: the main exact-covering result is sound

I tried the listed failure modes; they do not break this theorem.

* **Level:** K2's level is the maximum, over individual summands, of the sum of logs of distinct primes >W dividing that summand's modulus. Concatenating the expansion of `nu` with the indicators `1_rho` gives level **at most** `max(lambda,lambda_R)`. One must not expand everything into classes modulo the common period. Cancellation can lower level; equality is unnecessary.
* **Eventual containment:** a finite union of classes and C have a common period. A missing residue has arbitrarily large positive representatives. Thus containment above an onset is periodic containment. For U, use the underlying congruence classes of the eventual-U witnesses; their validity prefixes are a separate exceptional-count issue.
* **Majorization:** a point of `A(F')` avoids F's selectors. If it belongs to an F-progression, coverage puts it in a remainder; otherwise it belongs to `A(F)`. Thus `nu + sum 1_rho >= 1` there. Global nonnegativity is preserved.
* **Arbitrary covering moduli:** Corollary 2.5, like K2 Theorem 5.1, really allows arbitrary family moduli. The covering family need not have polynomial primes, bounded depth, bounded total period, or a modulus ratio bound for this mean-cap application.
* **Two levels and multipliers:** any finite tree of periodic subcovers flattens to a finite word cover. Prime factors introduced by multipliers cause no additional restriction. This does not cover an infinite tree, an interval-only cover, or a prime-only cover.

Consequently exact level lowering is indeed already included in the mean cap. This is a substantive positive result, not just a repetition of the word first-moment estimate. Add the usual `L>=lambda_0` convention, or replace L by `max(lambda,lambda_R,lambda_0)`.

Two explanatory qualifications: LS2's comparison measure serves all tests in a **specified finite span** simultaneously, not an unspecified infinite universe of test moduli; and the assertion `A(F') subset A(F)` is for **exact** covers, not general approximate ones. The direct proof already handles approximate covers correctly.

### R3-2 — R4.2 loses the remainder cost and uses the wrong projection

Lines 670–672 assume only `delta_R <= exp(-S)/2`, not a bound on `lambda_R`. R4.1 depends on `max(lambda,lambda_R)`. An arbitrarily small Haar remainder with enormous level gives no saving cap at level `log N`. Indeed R4.3(c) supplies arbitrarily small finite periodic remainders for **every** progression, without saying their levels are affordable. Small density alone cannot close universe exhaustion.

Also “run K2 Cor 6.1 on nu'” is not justified by the stated polynomial-prime hypothesis on **F**. The family majorized by nu' is **F'**, whose word classes may have arbitrarily large primes. Nor is a bound on the coefficient sum of nu' supplied: adding many remainder indicators can increase it enormously.

**Repair for exact covers:** project/coarsen **nu on the period of F first**, preserving majorization of `A(F)` and using F's polynomial-prime bound. Then apply R4.1 to that coarsened majorant. No polynomial-prime restriction on F' is needed. This proves the advertised exact-cover M1 consequence.

**Repair for approximate covers:** require, uniformly at the target saving S, a covering with

```
delta_R <= exp(-S)/2,
lambda_R <= C0 (log N + S).
```

Coarsen the original nu to additive mean error at most `exp(-S)`, at level `O_A(log N+S)`, then add the remainder indicators and apply R4.1. This avoids charging their coefficient count in the original evaluation. Alternatively state a low-level version with `lambda_R=O(lambda)` and `delta_R<=E nu`, as §8.6(2) already does. For M2 retain its explicit denominator restriction; L1/C need their respective level/admissibility hypotheses as well. Do not claim the approximate-cover M1 result from density alone.

## 3. R4.3: compactness, squares, Haar nullity, and size

**(a) SOUND.** A finite cover is equivalent to missing the closed profinite avoider set, by compactness and density of C in its closure. Work consistently in the stated `1 mod4` component (or explicitly intersect all C with it).

**(b) SOUND.** An appropriate modular square root gives infinitely many positive odd squares in the progression, by adding multiples of a common modulus to the root. They violate ES5 and hence U. This is a sufficient obstruction; unit-square compatibility is not asserted to classify all nonforcing progressions.

**(c) SOUND.** The classes `-4 mod q`, `q=3 mod4`, have endpoint word parameters `((q+1)/4,4)` and are eventual-U classes. The possible initial U degeneracy is harmless under the adopted definition. Conditional on `n=1 mod4`, the odd-prime coordinates remain independent. The product `prod(1-1/q)` vanishes by divergence of reciprocal primes in that progression. This last analytic fact should be cited; mere infinitude of those primes would not suffice.

**(d) SOUND with an onset clarification.** For a fixed T only finitely many distinct classes of modulus <=T exist. Their complement in C is nonempty and periodic unless C has a finite cover. Restrict its infinitely many positive members to `n>=n0(C)` before saying they have P-words. Each grouping of each such certificate has a preserving refinement of modulus <=8 times its grouping modulus, so

```
T/8 < min(uv,tv-1,tu-1) <= (2n+4)^(2/3).
```

The displayed lower bound for n follows. No bound on the common period is needed.

**R3-3 — Delete the unsupported sentence after the proposition, lines 702–704.** Haar nullity proves approximability with density tending to zero; it does not prove that the remainder “has no low-level description.” Some C are already finitely covered, and cheap approximate remainders are precisely what R4.5 aims to construct. Replace this with: “Compactness/Haar nullity alone gives no useful upper bound on the remainder level.”

## 4. R4.4: the collective contradiction works

The note's actual expansion has term moduli

```
lcm(d, k_A*l_A : A in B),  d | P_y,  |B| <= r.
```

Therefore their rough level is at most `log P_y + r log(KX)=O(t^4)`, since `y=Bt^3` and `r=O(t^3)`. In particular the enormous conditioning period `L_K` is **not** a term modulus forced into the expansion. Theorem 7.2 supplies the Haar bound `E nu_X <= exp(-c_a t^3)`.

The selector issue is handled correctly: nu_X equals 1 on the **whole** periodic avoider of the atoms **plus** `0 mod p`, `p<=y`, and is globally nonnegative. It need not majorize nonrough atom avoiders. Corollary 2.5 allows precisely these selectors. No prime-only inference or integer-counting error estimate is used in the contradiction.

If all atoms were finitely word-covered, the same nu_X would majorize the covering-word avoider plus selectors. The resulting inequality

```
c_a t^3 <= O(t^(8/3) (log t)^(2/3))
```

is impossible for all sufficiently large t. **This is SOUND relative to the two stated inputs.** If only covers on `1 mod4` are intended, specify that restriction: adjoining the certificate class `3 mod4` and the selector `0 mod2` restricts the covering avoider to that component, and the same argument works.

**R3-4 — Preserve the quantifiers.** For each sufficiently large X, **at least one** atom in that finite family lacks a finite ES5-word cover. This does not say that every ratio atom lacks such a cover, that no ratio atom is U/ES5-forcing, or that the noncoverable atoms are not forcing by a noncompact argument. The “cannot certify U or ES5 / no analogue” interpretation after the proof exceeds this result and repeats R3-1.

## 5. R4.5: the prime-pattern argument is repairable, but the printed rule is false

### What checks out

`gcd((a+v)/D,M/D)=1` is correct: at each prime at least one residual valuation is zero. Thus `m=r' mod M'` is reduced.

For a nonempty exact valuation vector write `P_j=prod p^j_p`. Necessarily `(P_j,M')=1`; otherwise a prime of M' would divide m. Consequently

```
m_j = r' P_j^(-1) mod M',   (m_j,V)=1.
```

For each compatible unit rho modulo V, CRT yields a **reduced** residue class modulo `lcm(M',V)`. Dirichlet gives arbitrarily large primes q in it, excluding the finitely many primes dividing D_j. This explicitly justifies the Dirichlet step. A valuation vector alone is generally a finite union of progressions, not one progression; the additional rho refinement resolves this harmless wording issue.

For fixed `delta|D_j`, the proposed congruence transport is correct:

* `A=delta`: t is fixed and `u=(D_j/delta)m_j`.
* `A=delta*m_j`: u is fixed and `t=(delta*m_j+1)/v`; its value modulo 4 depends only on `m_j mod4v`.

All ES5 slot data and U endpoint data are determined by `m_j mod8v`. Primality is needed to **find** the witness pattern, not to use it subsequently. Take a sufficiently large representative when needed for U's inequalities, and retain the eventual-word convention. The subprogression is **contained in** the corresponding standard word class; it need not equal that word class, because C can impose extra congruences.

### R3-5 — “Proper divisor,” delta<D_j, wrongly excludes valid U and ES5 words

U requires `tu-1,tv-1>1`, **not** `u,v>1`. ES5 also permits `u=1`. Thus `A=n+v=D_j*q`, with `delta=D_j`, is allowed.

An ES5 counterexample is `C=5 mod8`, `v=2`: every member has the word `((n+3)/2,1,2)`, with t divisible by 4. Here `D=1`, m is odd, and `D_j=1`. Neither branch of the printed delta rule can produce a witness.

More decisively, a **U** counterexample lies inside the author's own census ranges:

```
C = 89 mod120,   v=15,
n=89+120k,   (t,u,v)=(7+8k,1,15),   k>=0.
```

The endpoint `15=-n mod8`; both adjacent factors exceed 1. At `n=89`, `D=8`, `M'=15`, `m=q=13`, `D_j=8`. Among divisors of `D_j*q=104`, the **only** A with `A=-1 mod15` is A=104. It requires `delta=D_j=8`, explicitly forbidden at line 740. There is no fixed delta branch and no proper variable-delta branch. The same residue pattern has arbitrarily large Dirichlet primes, so this is not an onset exception.

**Repair:** enumerate both `A=delta` and `A=delta*q` for **all** `delta|D_j`, including `delta=D_j`, and test the actual slot/nondegeneracy conditions. Allow A=1 in the general enumeration and discard it only when the target/domain conditions really exclude it. Delete “is proper.” The corrected transport proves the intended approximate-cover statement. The numerical code's `uword_at` and `decide` also wrongly require a proper divisor: they are sufficient searches, not complete decision procedures. Their zero-failure run cannot verify the missing necessity direction.

### R3-6 — Tail density is correct; the uniform cost inference is not stated correctly

For `p|M'` the proposed tail is empty. For `p` not dividing M', exactly one progression-index residue modulo `p^(J+1)` lies in the tail, so its density is

```
1/(M*p^(J+1)) <= 2^(-J-1)/M.
```

Summing gives the claimed (looser) density bound. The tail class has modulus `M*p^(J+1)`. Therefore under the actual K2 level definition its level is at most

```
level(M) + 1[p>W and p does not divide M] log p,
```

**independent of J**. This is stronger and more informative than the displayed logarithmic-modulus bound. Repeated prime powers do not incur repeated K2 level charges.

But “hence lambda_R=O(lambda) after taking J=lambda” needs a uniform hypothesis. Lambda is the **majorant's** level, not `log M` or `log v`. The family can contain progressions of much higher level than nu, and endpoints v can grow arbitrarily with the outer parameter. For a finite family a valid bound is

```
lambda_R <= max_C (level(M_C) + max_{p|8v_C, p>W, p not dividing M_C} log p).
```

The maximum over an empty set contributes zero. Supply a uniform O(lambda) bound on this quantity (or an O(log N+S) bound for R4.2), and choose J large enough for the **total** remainder density across the family. Merely setting J=lambda does not control an unrestricted number of progressions either.

For a fixed progression and fixed endpoint the constants are fixed; that is not automatically a uniform theorem about an expanding forcing universe. State the dependence rather than calling all single-shift mechanisms uniformly capped without qualification.

### R3-7 — R4.6's residue splitting does not establish Dickson admissibility

Splitting residue classes cannot make a fixed divisor of the product disappear unless it is extracted from the affected forms. For example, take `C=1 mod12` and endpoints `{8,20,32}`. With `n=1+12k` and the stated initial gcd normalizations, the forms are

```
4k+3,  4k+7,  4k+11.
```

They are individually primitive, but their product is always divisible by 3. None of the endpoints is divisible by 3. Thus the prescribed valuation splitting at primes dividing `prod 8v` does not handle 3. Splitting n modulo 3 does nothing on C; even splitting k modulo 3 leaves one of the displayed forms always divisible by 3. They cannot all be large primes on any piece. Dickson does not assert otherwise.

**Repair:** enlarge the bad-prime set to include all primes <= the number of forms (a slightly larger cutoff is harmless), and split the **exact valuations of every normalized form at those primes**, not just residues of n. Extract those prime powers, with high-valuation tails paid explicitly. On the remaining compatible pieces the residual forms are units at the bad primes. Prove individual primitivity after refinement; at a larger prime at most one root per nonconstant primitive linear form rules out a fixed divisor of the product. Then apply Dickson to the residual forms, with the prescribed residue patterns, and use the corrected R4.5 transport. Account for the additional tails and their levels. Until that argument is written, retain “conditional strategy,” not a proved conditional proposition from the present sketch.

## 6. §8.6: scope and labels

**R3-8 — The final exclusion remains too strong.** Replace it by the following supported conclusion:

> Exact finite word coverings, without any covering-modulus or depth restriction, cannot improve the specified whole-avoider CRT mean cap. Approximate coverings inherit that cap when their total remainder density and level satisfy the stated uniform bounds. The note's complete large atom family cannot consist entirely of finite word coverings. Single-shift forcing admits a repaired prime-pattern reduction; bounded-shift forcing has a conditional route requiring an admissibility argument.

In particular:

* “Only possible escape” must be restricted to the specified periodic whole-avoider architecture. Interval-only certificates, prime-only majorants, non-CRT evaluation, and other doors retained in §§1–7 have not disappeared.
* Noncompactness means failure of a **finite exact** cover. It is not equivalent to failure of a **cheap approximate** cover. R4.3(d) gives a necessary property of a noncoverable forcing progression, not a classification of all possible proofs as B2-type input.
* The claimed necessity of “unboundedly many shifts” is not unconditional: even the bounded-shift reduction is conditional and currently incomplete. Moreover noncompactness alone does not imply unbounded shifts; R4.5 seeks only an approximate cover, not an exact one.
* “The one genuinely archimedean forcing principle available” is a research assessment, not an exhaustion theorem. A proof by a different identity is not excluded by the target's definition.
* A mean cap does **not** literally bound the raw class inventory of every covering-certified universe by a quadratic first moment. For example take all subdivisions of one word class: at each refinement modulus the densities sum to the original class's density; summing over arbitrarily many refinements makes the inventory arbitrarily large, despite exact coverage by one word class. All subdivisions of `17 mod24` at moduli `24*2^j` already give divergent smooth-modulus inventory. What is excluded is an **effective** cubic-supply construction producing the required small-mean, low-level majorant—not redundant cubic or larger supply as a counting statistic.

**Numerical labels:** the finite outputs are reproducible, but “decision procedure confirmed” is false because the rule has false negatives (R3-5). Call it a sufficient-certificate census until repaired. The dyadic maxima for `305 mod808` are 7,5,37,11,39,49,111,90,450; these are maxima over separate disjoint bins, not a monotone cumulative maximum. They are compatible with noncompactness but do not establish unbounded growth or forcing. Retain **EVIDENCE**, explicitly heuristic. The `17 mod24` example is independently finitely covered by `E(1,4)=2 mod3` with the usual U onset, not just by sampled behavior.

## 7. Reproduction and independent check

All runs used `ulimit -v 4000000`, explicit 90/120-second timeouts, and `uv run python`. I inspected both scripts first. They stream small-integer divisor searches; no dense geometry/array or unbounded Cartesian allocation is involved.

* `scripts/z50_ncrt_r4.py 100000 1000`: reproduced 1,830 candidates, 182 accepted pairs, and **209,190** checked integers with zero failures of its restricted sufficient U search. The second cutoff was deliberately 1,000, skipping the expensive unrelated full-word enumeration; I do not claim to reproduce its 60,000 second phase.
* `scripts/z50_ncrt_r4b.py 305 808 512000 3000`: reproduced all nine quoted maxima and zero missing witnesses below the search cutoff.
* Independent `/tmp/z50_ncrt_review3_check.py`, importing no campaign code: on moduli `{16,32,48,80,88,104,144,176}`, endpoints 1–24 and `100<=n<1200`, transported **6,890 U** and **10,853 ES5** prime-model witnesses to the corresponding possibly composite residual arguments, checking full predicates with zero failures. This test includes `delta=D_j` and is not a test of the incorrect proper-divisor restriction.
* Independently verified 100 members each of the U and ES5 boundary counterexamples and 100 members of the primitive Type-II/U progression; verified the R4.6 product obstruction; and checked the finite Haar avoider fraction for q=3,7,11,19, conditional on `1 mod4`, as **2160/4389 = 720/1463**, equal to `prod(1-1/q)`.

Logs: `/tmp/z50_ncrt_review3_{r4,r4b,check}.log`. The independent script and logs stay outside the repository; only this review is committed.

**Decision:** preserve R4.1's exact-cover theorem and R4.4's collective separation. Repair the Landau witness boundary and conditional admissibility proof, and restore explicit cost/uniformity hypotheses. Do not label the resulting work an exhaustion of all U/ES5 certification mechanisms or an unconditional exclusion of bounded-shift alternatives.
