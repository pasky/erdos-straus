# Wave-21 hostile review: §56 congruence ceilings and extremal census

**Base reviewed:** `34c5605` (wave-21 content commit `ffb4645`).  **Overall verdict:** **SOUND-AFTER-MINIMAL-SCOPE-REPAIRS.**  I found no break in Theorem 56.1, Theorem 56.2, either exponential constant, or the finite census.  The two proofs survive nonreduced integer classes, awkward shared factors, finite exceptional prefixes, and the exact hypotheses of Corollary 52.2.  The largest original risk was not a theorem failure but a quantifier trap: an eventual certificate does not by itself certify the least prime in its class.  The corollary already said “selects a certified prime,” and §54's actual classes certify every prime; I made the requirement explicit so the generic-recipe prose cannot be read more broadly.

This verdict does not independently re-prove the beta-sieve input in Theorem 52.1.  I replayed Corollary 52.2 from its stated log-saving and prime-number-theorem comparison, and then replayed every §56 specialization into it.

## Claim verdicts

| Claim | Verdict | Hostile finding |
|---|---|---|
| Theorem 56.1, exact divisibility | **CONFIRMED** | For every prime `ℓ≤T`, `ℓ≡3 (mod 4)`, the literal Lemma-16.1 datum is `k=1`, `A=(ℓ+1)/4`, `(u,v,w)=(1,A,1)`.  Since `4A≡1 (mod ℓ)`, `nA≡-1` is exactly `n≡-4 (mod ℓ)`.  Therefore `W(n)≤ℓ`. |
| Theorem 56.1, CRT/Dirichlet step | **CONFIRMED** | If `ℓ∤Q`, then `(Q,ℓ)=1`, so the joint class exists even when `Q` is even or `a mod Q` is nonreduced.  The integer proof needs no reducedness.  In the prime proof, reducedness modulo `Q` and `-4≠0 (mod ℓ)` makes the joint class reduced modulo `Qℓ`; infinitely many Dirichlet primes outrun both “sufficiently large” thresholds. |
| Theorem 56.1, constant and effectivity | **CONFIRMED** | Summing `log ℓ` gives `θ(T;4,3)=(1/2+o(1))T`.  This is the fixed progression modulo 4, so the epsilon threshold is effective.  For `T<3` the product is empty and the assertion is vacuous. |
| Relation to Theorem 33.1 and limitation | **CONFIRMED** | The mechanism is literally Theorem 33.1's `D=1`, `-4 mod ℓ` cylinder argument.  §56 adds eventual-class and prime-bearing versions.  The text correctly withholds an `lcm(1,…,T)` lower bound: when a composite modulus shares coordinates with `Q`, compatibility on the common gcd can fail. |
| Theorem 56.2, class bookkeeping | **CONFIRMED** | For each prime `5≤ℓ≤T` omitted from `Q`, choose a nonzero nonresidue `b mod ℓ`.  Since `24|Q`, `Qℓ` is a multiple of `lcm(24,4ℓ)=24ℓ`; the joint class is reduced and restricts to a valid base class for Theorem 52.1. |
| Theorem 56.2, character sign | **CONFIRMED** | On the refinement, `p≡1 (mod 4)` and `p≡b (mod ℓ)`.  Whether the fundamental discriminant is `-ℓ` or `-4ℓ`, the factor 4 is invisible and quadratic reciprocity gives `χ_ℓ(p)=(-ℓ/p)=(p/ℓ)=-1`. |
| Theorem 56.2, Corollary 52.2 use | **CONFIRMED** | The fixed slice `(c,k)=(ℓ,1)` has squarefree core `ℓ∉{1,2,3,6}`, is admissible beyond a finite bound, and is in the unforced sign.  Corollary 52.2 applies to the reduced refinement modulo `Qℓ` and supplies arbitrarily large primes with `M_{ℓ,1}(p)>0`, contradicting the original eventual certificate.  Quantifiers align. |
| Theorem 56.2, forced cores and constant | **CONFIRMED** | Only prime cores `s=ℓ`, via the `k=1` slices, are needed.  They force every prime `5≤ℓ≤T` into `Q`, yielding exactly `log Q≥θ(T)-log 6=T+o(T)`.  A generic all-squarefree-core conductor lemma is not stated or needed. |
| Additive/primitivity issue | **CONFIRMED BY DIRECT SPECIALIZATION** | The proof does not rely on an unstated claim about a multiplicative subgroup or a primitive character being constant on an additive coset.  For a prime core the only omitted odd conductor coordinate is exhibited directly by `(56.6)`.  Thus absence of a general primitivity lemma is not a gap in the theorem proved. |
| Congruence/Linnik corollary | **CONFIRMED AFTER SCOPE CLARIFICATION** | From `log Q=(α+o(1))T` and `p≤Q^{L+o(1)}`, `T≥(1+o(1))log p/(αL)`.  The ceiling gives `α≥1/2` or `α≥1`; §54 has `α=1`.  The added sentence at `notes.md:20915-20918` prevents a least-prime theorem from being misapplied to the finite exceptional prefix permitted by the certificate definition. |
| GRH sentence | **CONFIRMED, CONDITIONAL** | The standard GRH bound `p≪(φ(Q)log Q)^2` permits exponent `2+ε`; with §54's `α=1` all-prime certificates this gives `(1/2-ε)log p` after renaming epsilon.  The text labels this conditional and keeps `(56.2)`, `(56.5)` unconditional. |
| Assessment 56.2a | **CONFIRMED, SCOPED** | The wall is expressly limited to a uniform complete class plus modulus `exp(Θ(T))` plus a generic least-prime theorem.  It does not claim that every lower-bound method, every congruence-informed sieve, or every accidental small first prime is capped. |
| Computational 56.3 (`W`) | **CONFIRMED** | Moduli are enumerated increasingly through 3000.  Lemma 18.1 makes each class set complete, so `next(...)` returns the exact minimum and cannot skip a smaller witness.  All displayed records, counts, maxima, and natural-log normalizations replay. |
| Computational 56.4 (`ck_pr`, `D`) | **CONFIRMED AFTER MEMORY-WORDING REPAIR** | Product order makes the first hit exact.  The genus skip is exact on hard primes; each surviving norm is factored once for the current `(p,c,k)`; the exponent box includes all capped divisor exponents.  The original prose incorrectly said only unresolved maps and fixed record data were retained, although two per-prime minima maps and the hard-prime tuple remain resident.  `notes.md:21055-21059` now states the actual linear memory. |
| Numbering and hygiene | **CONFIRMED AFTER POINTER REPAIR** | Tags `(56.1)–(56.16)` are unique and sequential; theorem/computational labels do not collide.  Cross-references 16.1, 18.1, 33.1, 48.2, 50.9, 51.1, 52.2, and 54.1/54.3 say what §56 claims.  The former bare `*(wave-21 pointer)*` pointed nowhere; `notes.md:21081-21083` now states the unchanged pointwise scope. |

## Theorem 56.1 replay and attempted breaks

For `ℓ≡3 (mod 4)`, put `A=(ℓ+1)/4`.  The eligibility check is exact even at the bottom endpoint: with `k=1`, `kℓ≡3 (mod 4)`, and `uvw=A` for `(1,A,1)`.  Lemma 16.1 asks

```text
n v ≡ -u (mod kℓ),
```

which becomes `nA≡-1 (mod ℓ)`.  Since `4A=ℓ+1`, `A^{-1}≡4`; hence the class is `-4 mod ℓ`, not `-A`, `-4^{-1}`, or a formal divisor class lacking a tuple.

Attempted breaks:

- **`Q` even or sharing factors with 4:** irrelevant; `ℓ` is odd and the contradiction assumes `ℓ∤Q`, so CRT uses coprime moduli `Q,ℓ`.
- **All-integer `(a,Q)>1`:** the joint integer class remains solvable and infinite.  Reducedness is nowhere needed on this branch.
- **Prime class reduced only modulo `Q`:** the joint residue is a unit at every prime dividing `Q` and is `-4`, a unit, at `ℓ`; it is reduced modulo `Qℓ`.
- **Finite exceptional prefixes on either certificate:** the joint integer class and the Dirichlet prime progression are unbounded, so an element can be chosen past the threshold.
- **`T<3`:** no eligible `ℓ`; `P_3(T)=1` and `θ(T;4,3)=0`.
- **Uniformity:** the `o(1)` is only as `T→∞` in one fixed arithmetic progression, independent of `a,Q`; the effective `T_ε` is therefore uniform over certificates.

The final limitation is necessary.  For composite `M`, the joint system is controlled by `(Q,M)`, and a certificate may occupy a coset incompatible with the chosen harvested class.  The prime-coordinate proof cannot silently be multiplied into a full `lcm(1,…,T)` requirement.

## Theorem 56.2 replay and attempted breaks

Fix `5≤ℓ≤T`, prime, and assume `ℓ∤Q`.  Pick a nonzero quadratic nonresidue `b mod ℓ`.  CRT gives the class `(56.6)` modulo `Qℓ`; it is reduced because `(a,Q)=1`, `(b,ℓ)=1`, and `(Q,ℓ)=1`.  Its reduction modulo

```text
Q_0 = lcm(24,4ℓ) = 24ℓ
```

satisfies all of Theorem 52.1's hypotheses for `(c,k)=(ℓ,1)`: it is `1 mod 24`, coprime to `4ℓ`, and has `χ_ℓ=-1`.  Corollary 52.2 allows any fixed reduced refinement modulo a multiple of `Q_0`; here that refinement is exactly modulo `Qℓ`.

Attempted breaks:

- **`Q` shares awkward factors with `4ℓ`:** `24|Q` already contains the full 2-adic coordinate and 3.  Under `ℓ∤Q`, the only missing coordinate is `ℓ`, so `Qℓ` is a valid multiple of `24ℓ`.
- **Fundamental conductor is `4ℓ` when `ℓ≡1 (mod 4)`:** the hard class fixes `p≡1 (mod 4)`, and `Q` contains 4.  Choosing `b` still selects either character sign on the omitted `ℓ` coordinate.
- **Slice compatibility/admissibility:** `b≠0` gives `(p,ℓ)=1`; `3≤2p` and `4ℓ≤2p+1` hold for all sufficiently large progression primes.  Corollary 52.2 already tolerates the finite inadmissible prefix.
- **Certificate threshold versus sieve asymptotic:** Corollary 52.2 says vanishing cannot contain all sufficiently large primes in the refinement.  Hence it supplies a positive slice arbitrarily far out, beyond the original certificate threshold.
- **Which cores are forced:** all prime cores `ℓ∈[5,T]`, not merely those already occurring in a small empirical box.  The fixed slice `(c,k)=(ℓ,1)` has product `ℓ≤T`.  Composite squarefree cores are unnecessary for the claimed constant.

The standard generic conductor statement mentioned in the review brief would also be a natural route: a primitive character cannot stay constant on a full compatible additive coset modulo a proper conductor gcd.  Section 56 wisely does not need that broader lemma.  Prime conductors have a single odd coordinate, and `(56.6)` directly realizes both signs, eliminating any ambiguity between additive cosets and multiplicative subgroups.

## Computational audit

### Full runs

- Full default command: `uv run --with sympy,numpy,scipy python verify.py` — **passed**, `all checks passed`, 104.73 s wall time, 333,616 KB maximum resident memory.
- Isolated `(bc)` with `ES_FULL_SCAN=1` — **passed**, 13.79 s wall time, 91,220 KB maximum resident memory.  The verifier has no block selector, so I parsed `verify.py` and executed only its global imports, `divisors_of_square`, and `check_bc`; the environment variable activated the exact full branch.  This is close to the author's 11.79 s / 109,984 KB report and well within the requested 1200-second bound.
- The isolated full branch reports 82,887 hard primes below `10^7`, 9,732 below `10^6`, 47,100 Type-I factorizations, maximum `W=2495`, maximum `ck_pr=898`, and maximum `D=217`, exactly as §56 states.

### Exact overlap checks

I ran an additional independent cross-check, not merely the fixed record assertions:

- For all 3,202 hard primes below 300,000, direct ordered-factorization class sets from block `(ax)` equal the intrinsic divisor-of-a-square class sets used by `(bc)` at every modulus through 3000.  The per-prime minima reproduce `(ax)`'s tails `226,19,0,0` and maximum 279 exactly.
- For all 1,181 hard primes below 100,000, the complete `prime_min` and `slice_min` maps produced independently by `(aw)` and `(bc)` are equal, prime by prime.  This is stronger than comparing only their overlapping record tails.

### Algorithm and regressions

- `modulus_classes` is built in strictly increasing eligible `M`; early exit therefore cannot miss a lower `W`.  A later modulus above the cap cannot lower a witness already at most 3000.
- The Type-I loops are in increasing product `n=ck`.  All divisor pairs at a fixed product are checked before advancing, so recorded minima and `D=ck_min-1` are exact.
- The Euler test skips exactly `χ_s(p)=+1` on hard primes.  Core values `1,2,3,6` are deterministically forced and correctly omitted.
- `exponent_box_hit` forms every residue generated by exponents `0,…,e_q`; its set has size at most `4ck`.  Factorizations and residue sets are discarded per norm.
- Persistent Type-I output state is `O(#hard primes)`, not constant: hard-prime tuple, two unresolved sets, two minima maps, and a small core cache.  There is no prime-by-slice table or Cartesian product.
- Counts, record tuples, rounded natural-log maxima, guard endpoints, and factorization counts are all hard assertions.  The `INFO` prefix is used only for fitted/normalized summaries, and §56 calls those finite informational maxima rather than asymptotics.

## Severity-ranked defects

1. **Moderate overclaim risk, repaired — eventual-certificate/least-prime quantifiers.**  A generic least-prime theorem can return one of the finitely many primes excluded by an eventual certificate definition.  The original words “selects a certified prime” technically assumed this away, and §54's actual residue-one classes certify every prime, but the surrounding recipe language could invite the invalid automatic inference.  `notes.md:20915-20918` now states the requirement.
2. **Low factual memory overclaim, repaired.**  The original §56.4 said the block retained only unresolved maps and fixed record data.  It actually retains every resolved `prime_min` and `slice_min` value plus the hard-prime tuple.  The corrected statement gives the true linear bound without weakening the important no-dense-table claim (`notes.md:21055-21059`).
3. **Low cross-reference hygiene, repaired in §56.**  There were no `*(wave-21 pointer)*` sentences in §§51 or 54; their existing wave-20 pointers to §54 are accurate.  The sole wave-21 label was a dangling tag at the end of §56.  It now says explicitly that §56 changes only the certificate-architecture perimeter, not the pointwise frontiers (`notes.md:21081-21083`).
4. **Low inherited repository hygiene, not caused by §56.**  `paper/espaper.log` is a tracked 200 KB build artifact from commit `7c4a70a`.  Wave 21 adds no tracked runtime/build artifact; I did not alter unrelated paper history.

No unrepaired §56 correctness defect remains.

## Overclaim scan

- “Ceiling” means a lower bound on the modulus required by a complete-class certificate, not an upper bound on `W(p)` or `ck_min(p)` and not a universal no-go theorem.
- The Type-II constant is only `1/2`; §56 explicitly declines to infer 1 or the full least common multiple.
- The Type-I constant 1 uses exactly the prime cores and Corollary 52.2.  It does not claim a new multi-slice sieve or a pointwise Type-I theorem.
- “Optimal logarithmic order” is confined to certificate plus generic least-prime arguments.  Assessment 56.2a leaves noncongruence certificates, congruence-informed non-complete constructions, and accidentally small primes outside the wall.
- The GRH consequence is visibly conditional.  The modulus ceilings and effective epsilon thresholds are unconditional.
- The censuses are exact only in displayed finite ranges.  The isolated jump to `W=2495` is explicitly denied any growth-law or tail-density interpretation.
- The middle `A≲2` panel is labelled a finite normalization window, not a theorem, conjecture, trend, or upper frontier.
- The repaired final sentence prevents §56's architecture result from being mistaken for progress on the still-open pointwise `A≥1` range.

## Validation and scope signature

**Replayed directly:** Lemma-16.1 datum `(56.3)`; Lemma-18.1 class identification; all integer/prime CRT and reducedness cases; bottom endpoint and epsilon uniformity; Type-I conductor coordinate, reciprocity sign, modulus compatibility, admissibility, and quantifier alignment; exact prime-core count and theta constants; Linnik algebra; GRH exponent bookkeeping; all `(bc)` loops, records, normalizations, full-scan data, and prior-block overlaps; numbering, control bytes, and cross-references.

**Structural/inherited only:** Theorem 52.1's standard beta-sieve upper bound, Corollary 52.2's resulting fixed-slice log saving, the cited effective forms of the prime number theorem and Linnik's theorem, and the standard GRH least-prime estimate.  I checked their hypotheses and deductions at every §56 use; I did not reconstruct those external analytic proofs from first principles.

Final validation after repairs:

```text
uv run --with sympy,numpy,scipy python verify.py
```

The post-repair rerun passed in 103.80 s with 334,504 KB peak RSS.  `git diff --check` passed, and `notes.md`, `verify.py`, `UNIT_REPORT_J21.md`, and this review contain zero control bytes.
