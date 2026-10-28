# Hostile cross-model review: LOWERTAIL_ROUND2_FABLE

**Verdict: SOUND-AFTER-REPAIRS.** No fatal defect found in Theorems 1, 2.1, 2.3, 3.2 or the repaired Dickson constructions. There are false or unsupported statements in the accompanying interpretations; they should not be carried into the campaign synthesis. This is modest structural/computational progress, not progress on a single-prime lower bound.

Reviewed `LOWERTAIL_ROUND2_FABLE.md`, its seven `scripts/z49_ltfable2_*` files and relevant data in worktree `erdos-straus-claude-agent-worktree-0041`, branch `side-agent/z49-ltfable2`, at commit **9f91249a**. Read both wave briefs and checked the relevant preceding forest/lower-tail results. This review is independent of the author's internal review. No literature-priority claim is verified.

## Findings requiring repair

### Fatal

None found. In particular, the modular-rank computation **can prove** the stated universal non-identity theorem; this is not an illicit extrapolation from a census.

### Major

1. **§1.3 contains a false composite-square divisor statement.** The quoted assertion that `m²+u` has no divisor `v ≡ −m² (mod u)` for `u ∈ C` is false without a coprimality restriction. Take `m=7`, `u=7`, `v=7`: `7 | 49+7` and `7 ≡ −49 (mod 7)`. But `(49+7+7)/49` is not integral. The two divisibilities do not imply `uv | n+u+v` when `gcd(u,v)>1`.
   - **Repair:** use the exact numerator version: `m²+u` has no divisor **A ≡ −1 (mod u)**. This is precisely the predecessor's Theorem E and needs no coprimality. Alternatively, restrict the endpoint-divisor statement to `gcd(u,v)=1`.
   - Corollary 1.2's actual conclusion `N₋(m²)=0` and the six empty coordinate lines remain sound. The error is in the claimed equivalent arithmetic restatement, not in T1.

2. **§1.4 conflates a nonprincipal ambient character with nontriviality on the signed-word set.** The sentence “on D(n) for non-square n the character is non-trivial” is not established. For nonsquare n the Jacobi character is nonprincipal on the *whole unit group*; this does not show that it takes −1 among the numerators of the restricted signed words. The latter is a separate existence statement. Lemma 1.4 only evaluates words already present, and the example at 105 proves a separation, not a theorem for every nonsquare.
   - **Repair:** say that the *ambient* character is nonprincipal, while whether its −1 set meets the positive-word set is the ES₅ question. Delete any blanket assertion that it already meets D(n), unless supplying an additional proof.
   - Keep the negative-word sign table and the 105 example: both check out. Be explicit that the character here is evaluated at the numerator `d`/`A`, not at potentially nonunit endpoints.

3. **§0 item 5 overclaims the windowed-genus conclusion, contradicting §5.2.** “(Gε) restricted to polylog moduli is heuristically false” does not follow just from windowed `R_Y=0` infinitely often. One must establish or heuristically model `M_gen,Y>0` on the same exceptional sequence. §5.2 correctly identifies this missing joint statement. Its subsequent “any proof of it must use pairs [beyond the large scale]” is likewise not a consequence for a *windowed relative inequality*: that inequality can read `0≥0`.
   - **Repair:** state only that the calibration obstructs a polylog-window **certificate-positivity** argument. A windowed relative inequality needs a separate positive-main-term assertion before the obstruction applies. A full inequality with the conditional log-square genus lower bound would force actual witnesses; the large-witness conclusion then remains conditional on that lower bound and heuristic calibration.

4. **§6(d) is not a proved obstruction to character methods.** Proposition 4.2 proves that one chosen presentation contains no explicit Dirichlet-character test. It does not bar “any use of GRH/003 through a character condition on the certificate.” The very same certificate has the equivalent character description in Theorem 1, and congruence indicators have exact character expansions. A change of presentation cannot prove analytic irrelevance.
   - **Repair:** remove (d) from “what is barred (PROVED/CONDITIONAL).” Retain the narrower Assessment already made in §4: no transfer from the *listed known consequences* of GRH/OAI-003 to covering positivity is supplied. The character-free reformulation is correct, but is not a new no-go theorem.

### Minor / precision

5. Define `SB_all` using **cells admissible for the current p modulo 8**. Literally quantifying over all 120 certificate cells in the combined 160-cell system makes the hypothesis impossible: half the cells have the wrong output residue. SE's phrase “admissible at p” should also be made explicit. The intended implications are correct after this clarification.
6. Theorem 1's invocation of `FOREST_DEEP_FABLE` Theorem A omits its extra hypotheses only harmlessly: `gcd(u,v)|n` makes endpoint coprimality automatic; the sole coprime diagonal word is `(n+2,1,1)`, which is noncertifying. State this, or cite `FOREST_CONNECTIVITY` Theorem 2.1 / `FOREST_DEEP_ASTRA` Theorem 2.1, which already cover words directly.
7. `W(p)≥15` needs `p>5` (`W(5)=11`). This does not affect any eventual implication. Likewise, the summary/§6 claim of vanishing HC survival at “every fixed X” needs **X≥4**; on `p≡1 (8)`, survival is 1 for X<4.
8. Fix the coefficient quantifier in §4: ε is a fixed positive constant, not the p-dependent expression `κc/(3/π²+o(1))`. State that any fixed `0<ε<κcπ²/3` works eventually.
9. Theorem 2.3 rules out constant-coefficient homogeneous linear relations in the stated count dictionary. It does not rule out all interior-word transports or explain why none exists. The formal scope paragraph is good; keep the earlier “none is forced” remark within that scope.
10. Conjecture 3.4 is a reasonable *candidate*, not a derived extreme-value law. “Weakest natural member” is especially misleading when §3.5 itself lists the weaker, equally one-coordinate bound `HC≤(log p)^A` for A>1. “Mechanism-independent heuristic” is unsupported. Compatibility with the H₄ calibration is not positive evidence for the specific scale `log p`.
11. The square-reciprocity obstruction is not supplied by `p mod 8` alone. Squares and primes can have the same mod-8 class; the tied integers' divisor structure still distinguishes them. “Only place the quadratic character enters” is acceptable as syntactic bookkeeping, not as an account of all arithmetic dependence.
12. §0's “every quantitative member of the hierarchy is ES₅ plus a size statement” must say **every ES-sufficient quantitative member**. The table also includes W_log, I3_log and unaccompanied SB_int, which it correctly does not claim imply ES₅.

## Claim-by-claim audit

### Theorem 1 and Corollaries 1.1–1.2

**Sound**, subject to the localized wording repairs above.

The new reverse implication is valid. For `4|A=tu−1`, with no coordinate already divisible by 4, t and u are odd. If `A=0 (8)` or v is even, `n=vA−u` gives `u=−n (8)`. Otherwise `A=4 (8)`, v odd, `tu=5 (8)` and `n=4−u (8)`; since `n=1 (4)`, only `u=3,7 (8)` remain, and each gives `t=−n (8)`. The symmetric numerator is identical. Forward implications are the elementary valuation pigeonhole: a product divisible by 8 has a factor divisible by 4.

Corollary 1.1 does not lose positivity or integrality. In its level branch, `d=−1 (t)` and `d|(tn+1)` imply the cofactor is also −1 modulo t. Here `t∈C_n` ensures `t≥3`, so both endpoint coordinates are positive integers. The endpoint branch retains the full divisibility `uv|n+u+v`. At prime p the extra gcd restriction in the displayed covering loses no word: a common endpoint divisor divides p, and both endpoints divisible by p are impossible for p>3.

Corollary 1.2 is exactly the imported endpoint and level reciprocity obstructions, restated through Theorem 1. It is not an independent new explanation of T1.

### Lemma 1.4 and Theorem 2.1 / Corollary 2.2

**Sound formulas.** For odd d, `d|(tn+1)` ensures `gcd(d,n)=gcd(d,t)=1`; reciprocity gives `(d/n)=(−t/d)`. Because `d=1 (t_odd)`, the displayed signs follow. For `4|t`, either the 2-exponent is even or `d=1 (8)`, and the sign is indeed +1. No odd-d conclusion should be extended to even d without additional bookkeeping.

The free enumeration covers the four endpoint-1/2 families and the two level-1/2 families with endpoints ≥3. The three stated overlaps are the only endpoint-family overlaps for odd n; subtract them only when they are in the certificate set, or use a set union as the implementation does. It is a correct filtered version of the old free-word formula, not a new count mechanism. Corollary 2.2 is the predecessor's index-two multiplicative-subgroup criterion.

The example `105=11·3·3+3+3`, `(34/105)=−1`, while all 11 positive words are free and noncertifying, is correct.

### Theorem 2.3: computation really is a proof

**Sound, independently certified.** Over Q the 160 columns have rank at most 84 because of endpoint exchange. A rank-84 minor nonzero modulo a prime is a nonzero integer minor; hence the rational rank is at least 84. Any relation valid for *all* primes holds on these finitely many rows, proving the asserted universal statement. In each output residue class the same argument gives rank 42 among 80 columns. This does not require proving that a census is representative.

I inspected both the word enumerator and modular elimination. The C enumeration is complete because the smaller endpoint satisfies `(u−1)²≤n+1`; all candidates are rechecked against the full word equation. The original NumPy arithmetic is exact here: all modular entries are below `2³¹−1`, so products and subtraction fit signed 64-bit integers.

More importantly, I independently regenerated **84 witness rows** using a different `u,t` enumeration, verified primality, and eliminated using Python integers modulo **1,000,003**, not the author's modulus. This gives rank 42 in each class using primes only up to **1129** and **941**, respectively. The saved check output lists all witness primes. Thus the large 12,980-row computation is unnecessary; these two small certificates suffice.

### Theorem 3.2: upper-bound sieve

**Sound unconditional theorem, relative only to a standard proved sieve theorem.** There is no lower-bound-sieve or parity-barrier error here.

For `p=1 (8)`, coordinate 4 occurs iff either `p+4` or `4p+1` has a prime factor 3 modulo 4. In the endpoint case this can be seen directly with the numerator divisor `A=−1 (4)`; in the level case it is `d=−1 (4)`. Thus `HC>4` excludes the two nonzero roots at every prime `ℓ=3 (4), ℓ>3`, as well as the zero root needed to sieve primality. The shifted roots collide only when `ℓ|15`; 3 is explicitly omitted from the shifted sieve and 5 is not a 3-mod-4 prime. The local counts are therefore exactly as stated.

On the progression 1 modulo 8, `|A_d|=xρ(d)/(8d)+O(ρ(d))`. The dimension is 2: primes 1 modulo 4 contribute weight 1, primes 3 modulo 4 weight 3. Mertens in these fixed progressions gives the product of order `1/log²z`, not merely a heuristic density.

For an explicit way to close the remainder estimate, use Selberg weights supported on `d<z`, `z=x^{1/4}`. The remainder is bounded by

`Σ_{d<z²} μ²(d) 3^{ω(d)} |r_d| ≪ Σ_{d<z²} 9^{ω(d)} ≪ z² (log z)^8`,

which is negligible against `x/log²x`; the Selberg denominator has order `log²z`. Adding the primes ≤z is harmless. This supplies the detail hidden behind the cited upper-bound sieve. The alternative Bombieri–Vinogradov paragraph is unnecessary; no unproved conjecture is needed.

The result proves relative-density zero for `HC>X` at fixed X≥4, not a bound at every prime or an extreme-value estimate. The underlying Landau-type phenomenon was already explicit in `FOREST_CONNECTIVITY` §3 and `FOREST_DEEP_FABLE` Lemma 2.3; this particular two-polynomial quantitative bound is an incremental addition.

### Proposition 3.3: Dickson constructions

**Sound CONDITIONAL on Dickson, including repaired part (b).**

In (a), every form is 1 at s=0, giving admissibility. The factorizations and residues of the prime cofactors leave only the residue classes of divisors of x+1 modulo x; none is −1 for x≥4. This kills exactly the bounded C-coordinates, not every certificate with an arbitrary small coordinate. The document now correctly distinguishes those properties.

In (b), the CRT conditions really do put each ℓ_i to exponent exactly one in p+1 while keeping `p=1 (Q₁)`. I checked the integer coefficients, the three kinds of admissibility primes, and the no-interior-word argument. The extra radical in Q₁ is essential: it ensures every denominator-cleared slope vanishes modulo every prime dividing Q₀. At ℓ_i, even F₁ has nonzero constant 1/2; elsewhere primes exceed the number 2X of forms. The forms also have distinct roots as functions of p (0, −1, −u, −1/t, −1/2), so there is no proportional-form issue.

The monochromatic free-layer proof is valid. In particular, the t=2 endpoints really are among `{1,2,F₂,p+1}`, since `(G₁+1)/2=(p+2)/3=F₂`. The `2^{k+2}` endpoint-1 count is correct. Independent arithmetic checks cover X=4,5,8,12 and several K, and all three reported X=4 prime instances have exactly 27 window words, all free and monochromatic.

### Proposition 4.2 and hierarchy

**Correct as a dictionary and as elementary implication bookkeeping; not a new analytic barrier.** After clarifying p-admissible cells, `SB_all⇒SB_any⇒ES₅` and `SB_all⇒(★)-eventual` hold; a single positive certificate-cell count suffices. `SB_int` needs a nonempty interior, and the document correctly preserves that qualification. `SB_any` needs no log-square tail because W has an unconditional positive lower bound. Squares refute positivity statements, but do not refute relative inequalities whose main terms also vanish. Proposition 3.3(b) refutes the scoped fixed-window positivity forms, including balance with arbitrarily many window words, not inequalities with both sides zero.

The “no known implication” statements are appropriately weaker than proved non-implications. The comparison with OAI-003/GRH is an Assessment, except where §6 improperly promotes it to a barred-method theorem (finding 4).

### §5: Gε and SE

**Exact identities and stated quantitative implications are sound**, with the window caveat in finding 3.

The pair-domain restrictions make `a=−(u+B)` a unit modulo `q=4uB`. Also `u,B≤(p+1)/3<p`, so p is a unit. Squaring in G has kernel of size s(q), hence the number of twists is s(q) on a genus-allowed pair and zero otherwise; `s(q)/φ(q)=1/|G²|`. Thus the displayed formula for Gε is an exact restatement of `R≥εM_gen`, not an additional hypothesis on independently sampled data. Its “a-priori rate” is a uniform-group reference measure, not a proved distribution of the actual pairs.

Conditional on the imported fixed-zero-free-strip theorem, `M_gen≫log²p`, so Gε implies eventual ES through R. SE implies eventual star-line positivity without any tail assumption. SE plus `W≫log²p` implies the BM lower-tail target using the known BM upper bound. The genus version additionally uses the stated upper bound `M_gen≪log²p`; the note does **not** prove that bound, and correctly says so. Under SE, a p-admissible cell whose three coordinate residues avoid 1 and 2 supplies `I3≥κW`, so the equivalence of the two log-square tail assumptions is legitimate. No SE-alone ⇒ Gε inference is established.

As a separate check, direct enumeration of all unit square twists, without the author's character-factor implementation, gives:

| p | R | genus pairs | M_gen |
|---:|---:|---:|---:|
| 17 | 2 | 2 | 2 |
| 193 | 4 | 10 | 97/45 |
| 409 | 0 | 34 | 18484931/4622310 = 3.9990677821… |
| 577 | 0 | 40 | 5.3523870262… |

The numerical 4.00 at 409 is rounded, not exactly 4. These agree with the supplied census at its printed precision. I did not independently rerun the full 10⁸ census or the 8,813,281 genus-pair census; those remain the author's finite computations, whose implementations I inspected.

## Honest novelty grades

Scale: **0/5** = inherited result/bookkeeping; **1/5** = useful packaging or routine corollary; **2/5** = modest genuinely new campaign statement/certificate; **3–5/5** would require substantial new arithmetic content. These grades concern novelty, not correctness or promise of proving ES.

| Result | Grade | Reason |
|---|---:|---|
| Theorem 1 | 1/5 | Cleaner three-coordinate packaging; the numerator-slot elimination is worth recording, but follows from the already proved 2-adic law. |
| Corollary 1.1 | 1/5 | Convenient covering dictionary; no new existence input. |
| Corollary 1.2 | 0/5 | Exactly the existing endpoint/level T1 statements. |
| Lemma 1.4 | 1/5 | Routine opposite-sign reciprocity table; the 105 separation usefully prevents a wrong spin-event formulation. |
| Theorem 2.1 / Corollary 2.2 | 1/5 / 0/5 | Filtering the known free enumeration / explicitly inherited prime-factor criterion. |
| Theorem 2.3 | 2/5 | A genuine finite exact non-identity theorem for a specified dictionary; narrow but rigorous new negative information. |
| HC definition and census | 1/5 | Useful combined statistic and measurements, not a mechanism. |
| Theorem 3.2 | 1/5 | New explicit bound for this statistic, by a standard dimension-two sieve on two already understood lines. Landau-type behavior itself is not new. |
| Proposition 3.3(a) | 1/5 | Extends the existing shadow-prime construction to the chosen finite coordinate menu. |
| Proposition 3.3(b) | 2/5 | A real incremental strengthening: levels and endpoints are simultaneously sterile while the monochromatic window count is arbitrarily large. |
| Proposition 4.2 / hierarchy | 0/5 | Syntactic reformulation and elementary arrows; not a theorem excluding L-function methods. |
| Gε / SE implications | 0/5 | Exact normalization and obvious count inequalities; no new bridge from a standard conjecture. |
| Conjecture 3.4 | 1/5 | A falsifiable candidate not killed by the two-endpoint calibration; no proved or derived logarithmic scale. |

**Bottom line:** retain the coordinate form, the small exact rank certificate, the scoped sieve bound, and the repaired Dickson strengthening. Do not advertise a new spin mechanism, a new general character-method obstruction, or a disproof of windowed Gε. The fixed-prime tied-divisor lower tail remains untouched.

## Reproduction

Independent audit script: `scripts/z49_ltfable2_review_check.py`. Output: `reviews/z49-ltfable2-review-check.txt`.

```sh
ulimit -v 8000000
timeout 180 uv run python scripts/z49_ltfable2_review_check.py \
  /home/pasky/projects/math/erdos-straus-claude-agent-worktree-0041
```

The script uses streaming/small arrays, a finite rank witness, and direct small twist enumeration; it does not allocate prime-by-word or residue-by-modulus Cartesian-product arrays. It independently checks 160 cells, 21,954 positive words for `n≡1 (4), n≤2000`, 4,758 odd-numerator negative words, every requested hard prime and both numerator-8 controls, the rank witness, CRT admissibility samples and the three large repaired-family instances. All checks pass. The review's explicit square-divisor counterexample is also asserted.
