# Hostile review — Z58 WILDCARD

**Verdict: mathematical lemmas and census engine pass; revise the interpretation before acceptance. ES remains OPEN.** No counterexample to the bounded census claims was found. Several claims outside the lemmas are stronger than their proofs/data, including a false F4 description and an invalid general-n conductor assertion.

Reviewed the working-tree memo (already modified when review began), all six `scripts/z58_wildcard_*` files, and every wildcard data file. Memo SHA-256: `bdc5933f6e105b55f3c29419b9b775884b24764f1d5f33eff79ba6a7845e6988`. Locations below refer to that version. Only this review file is added; no memo/script edits or commits. All shell runs used `ulimit -v 4000000` and `timeout` ≤ 240 seconds; at most two concurrent processes. Independent exhaustive enumeration stopped at n = 100000. The full large censuses were audited, not independently rerun.

## Required fixes

1. **SERIOUS — F4 incorrectly calls all screen primes c = 1 zeros.** `Z58_WILDCARD.md:26`, and the inference at `:243–246`. Only the 14 full-(★) zeros have that property. The 38 G*-zeros include 37, with the c = 1 solution `(a,b,c,d)=(1,2,1,5)`; all 12 R8 screen primes have positive R4 (e.g. R4(10156800001)=56, `Z57_SYNTH.md:171`). Fix “Those primes” to “the 14 (★)-zero primes.” Further, these finite examples require c ≥ 2 only for a statement covering them. They do not logically force a proof of (MS-II), whose threshold is 10^17, to use c ≥ 2. State that as the lane's proposed strategy, not a consequence of F4.

2. **SERIOUS — the F1/general-n conductor claim is false.** Memo `:23, :211–218`: the primitive conductor of `χ_u=(−nu/·)` need not contain the squarefree kernel s(n). Odd prime factors shared by s(n) and u can cancel. Take n=4545=505·3² and u=505: `−nu=−1515²`, whose primitive quadratic character has conductor 4, not one divisible by 505. The theorem cited is for primes p with p ∤ u; it does not prove the quoted general-n assertion. Fix F1 by quoting the prime-domain theorem accurately, and explicitly require an odd prime of s(n) outside u for the analogous nonprincipality argument. Keep the proposed composite genus analysis heuristic. Also “T1 is the only obstruction” must say “apart from the explicitly excluded 4545.”

3. **SERIOUS — an upper-bound sieve does not give the stated two-sided density.** Memo `:198–207`, especially `:200`: `#(S3 ∩ [1,X])/X ≍ (log X)^−3/2` does not follow from a “standard upper-bound sieve.” For primes ℓ ≡ 3 mod 4 other than 3, the three linear forms exclude three distinct residue classes; this supports sieve dimension 3/2 and an upper bound `≪ X/(log X)^(3/2)`. No matching lower bound is supplied. Fix to the upper bound, with a proof/reference, and label the matching order conjectural/heuristic. The inclusion itself is sound, on the odd-positive domain; in fact squares ⊂ S3, so adding “squares ∪” is redundant.

4. **SERIOUS — the claimed model “mean” is from a different population, and the tail fit is selected.** Memo `:116–136`; `z58_wildcard_ladder.py:5–14,30–43`; `z58_wildcard_ladder2.py:14–35`. Counts/λ use every second prime p ≡ 1 mod 4 near 10^6, while zero-rate denominators use all odd primes, or all QR-mod-105 primes without a mod-4 restriction. The 227-prime restricted mean still has p ≡ 1 mod 4; the restricted rate includes p ≡ 3 mod 4, all of which are deterministically solved for K=4 by Lemma 4.4(a). This is not the actual (MS-II) population either. Also both fits discard every bin with fewer than three zeros, including zero bins; the memo does not disclose this outcome-dependent selection. Fix by matching the mean/rate populations (preferably the actual Mordell classes), or explicitly call λL³ a cross-population proxy. Disclose the z ≥ 3 rule, use an appropriate count likelihood including zero bins or report sensitivity, and label the Poisson numbers conditional on an unvalidated model rather than significance tests. The numerical fit outputs themselves reproduce exactly.

5. **SERIOUS — model compatibility is promoted into structural exclusivity.** Memo `:134–136, :233–238, :259–260, :274`. Zero observations with a model expectation 0.81 establish compatibility, not that K=4 and K=8 “differ only through the mean count,” nor that every argument avoiding that mean/complete moduli would apply equally to K=8. Even on Mordell classes there are other arithmetic distinctions: f=11 is permitted for K=4, forbidden for K=8, is not complete, and covers p=4201 ≡ 1 mod 840 via `(1,382,1,3)`. Fix to “the restricted diagnostic is consistent with mean-count scaling; no mechanism distinguishing the numerators was found.” A genuinely K-uniform proof must respect the observed K=8 zeros, but universality cannot be inferred merely from not mentioning the proposed explanatory variables. The general extrapolation caveat is welcome but does not repair these categorical sentences.

6. **SERIOUS — “only numerator 4 has complete moduli” is not the cited theorem.** Memo `:127–129, :233–234`. `Z57_BFII` Proposition 3.1 proves completeness of 3,7,15 for K=4, finiteness of the K=4 complete moduli, and a census of them below 4000; it does not classify all moduli for all K. Fix to “the three exhibited moduli 3,7,15 are complete only for numerator 4.” Their deterministic coverage is correct (asymptotic density 7/8 among primes, excluding the finite ramified exceptions), but a global no-other-K theorem requires a separate proof.

7. **SERIOUS — bounded positivity is repeatedly written as eventual/unbounded positivity.** Memo `:8–10, :24–25, :164–166, :270–274`. “Both parity halves eventually positive,” “no prime zero,” and “numerator-8 analogue is clean beyond 1.24·10^6” need their tested upper endpoints and the odd-nonsquare restriction. Otherwise the last claim is false literally because squares are zeros forever, and all three assert an unproved infinite-range conclusion. Use “no odd-nonsquare zero in (1239315,10^9]” and “no odd prime zero ≤10^10”; state eventual positivity as conjectural. Likewise “primality is used only through gcd(n,15)=1” is an empirical conjecture formulation, not an established proof mechanism.

8. **SERIOUS — unconditional divisor inheritance is not Lemma 4.2.** Memo F3 `:25` and consequences `:164–166, :219, :267`. The bijections are correct, but lifting from n to nk requires a solution at n with k | c (part a), or k | d (inverse of part b). Positivity does not generally pass to multiples: N_II(5)>0 but N_II(4545)=0 although 5 | 4545. Preserve the divisibility condition wherever inheritance is summarized. Coprimality does exclude these lifts, so that census remains a useful diagnostic; it does not measure an unconditional closure property.

## Smaller corrections

9. **MINOR — restricted fitted x-range is about 45.4, not 55.** Memo `:136`: 54.9253 is the all-prime fit's maximum x; the QR-restricted fit's maximum is 45.4074. Fix that number. The reported 4.04·10^−5 is the restricted model's decade-4 contribution, and the displayed script sums only through decade 7; describe an infinite tail as an additional extrapolation, not a computed tail certificate.

10. **MINOR — K24 twist exclusion misses p=3.** `z58_wildcard_ladder.py:2,25,39`; `z58_wildcard_ladder2.py:30`. Excluding only p=K/4 fails to remove the s=3 twist when K=24. For prime n, the structural exclusion is an odd prime dividing K/4. Fix the filter accordingly. This changes the K24 decade-0 diagnostic, not either reported fit (which starts at decade 2), and does not change the census's legitimate total of 3740 prime zeros.

11. **MINOR — census's “max least witness” excludes LATE cases.** `z58_wildcard_census.c:59–68`. The maximum is over successful bitmap hits only. In the K4 [10^8,10^9) file the summary says 19403 despite an n needing f>20000. The memo handles that particular late case correctly, but the generic output label is misleading. Say “maximum least witness among hits ≤FMAX”; an exact fallback returns some witness, not necessarily the least. Histograms intentionally omit f in [200,1000), and `cumfrac` includes square/zero inputs in its denominator; document this if reused.

12. **MINOR — scope/threshold wording in §1 and §5.** Memo `:44–51, :229–238`: the predicate N_II(p)>0 is certified below 10^10, not the conjecture quantified over p>10^17. The finite exception set in CONV-II(K) is conjecturally finite for K=8 and 12 too; “EVIDENCE only for K≥16” is misleading. The 3.6·10^4, 2·10^6, etc. sequence is of last **observed prime** zeros, not last zeros of all n; K12 has infinitely many twisted-square zeros. With statements p>P the necessary condition is P ≥ 35569, not P>35569. A finite ladder alone does not prove thresholds grow without bound over all K; if needed, the elementary fact K>n+2 ⇒ N^(K)(n)=0 supplies that obstruction.

13. **MINOR — provenance/reproduction polish.** Memo `:5, :108, :160, :280–298`: the directory contains 13,552,210 bytes before this review, not ≈9 MB; the 1821-prime sample is every second eligible prime, not the complete interval; “hostile review applied” precedes an empty review record. Include the `ladder2.py` reproduction command and persist the small scaling/fallback validation rather than reporting an otherwise undocumented run. Runtimes (34 seconds; 10 seconds–15 minutes) have no timing artifact in this directory and were not independently checked. Existing checkpoint commit `40c1af69` does substantiate the checkpoint/falsifier-table provenance.

14. **MINOR — CLI portability and fail-closed behavior.** `z58_wildcard_census.c:33–44` and `z58_wildcard_count.c:11–13`: validate argc, positive K divisible by 4, nonnegative FMAX, allocation success, and range limits; document/assert 64-bit `long`. The supplied commands are valid on this LP64 host, but the code is not a general portable u64 program (histogram/tested counters exceed 32-bit long). No incorrect decision or overflow was found in the stated runs.

## Proof audit — OK

**OK — definitions and §1 logical implications.** The denominator identity is exact. For primes, gcd(abd,p)=1 is automatic: otherwise all three Egyptian denominators are multiples of p, giving 4 as a sum of three positive unit fractions, impossible. `(MS) ⇒ (MS-II)` and `(MS-II) + Mordell + Salez ⇒ ES` have the stated conditional scope. CONV-II and CONV-II-15 are properly conjectures, not consequences of the census. The r-spectrum counterexample in §2 is valid, though distinguishing the spectrum symbol from scalar R(n) would improve notation.

**OK — Lemma 4.1.** Multiplication/division of d by k is an inverse pair between exactly the stated domains. Thus the numerator-8 family counts the d-even solutions of the numerator-4 family, including ordered multiplicities. The c=1 restriction agrees with Z57_SYNTH Lemma 2.1.

**OK — Lemma 4.2, both bijections.** For (a), at N=nk, setting c'=kc and d'=d/k preserves the left-hand side and changes Nc to nc'; conversely c'/k is integral exactly on the target's k|c' slice. For (b), divide the original equation by k: the left-hand side is `4(a/k)(b/k)c(kd)` and the right-hand side `a/k+b/k+nc`. Conversely multiply a,b by k and divide d by k. Positivity and both slice conditions are preserved. No missing gcd assumption. The ensuing lifting claims require the slice hypotheses, as noted above.

**OK — Lemma 4.3, including both gcd cases.** Put h=K/4. Since f=4hacd−1, gcd(hac,f)=1. The reciprocity lemma gives `(hac/f)=(h/f)=1`, hence `(ac/f)=1`. The witness identity `bf=cn+a` gives `−n≡ac^−1 mod f`, a unit, so `(n/f)=−1` because f≡3 mod4. If n=sm² with odd s|h, then f≡−1 mod4s, hence `(s/f)=1`; when gcd(m,f)=1 this gives `(n/f)=1`, contradiction. If a prime ℓ divides both m and f, the witness equation forces ℓ|a, contrary to gcd(a,f)=1. Thus the twist obstruction is proved; the lemma does not prove that these are the only possible infinite zero families.

**OK — Lemma 4.4.** Part (a) is the displayed substitution (also coprime to n). For part (b) one can make all three reconstructions explicit:

- `(a,c)=(1,1)`: f|n+1, f≡3 mod4 gives d=(f+1)/4, b=(n+1)/f.
- `(a,d)=(1,1)`: f|n+4, f≡3 mod4 gives c=(f+1)/4; `(cn+1)/f` is integral since `4(cn+1)=n(f+1)+4` and gcd(4,f)=1.
- `(c,d)=(1,1)`: f|4n+1, f≡3 mod4 gives a=(f+1)/4; `4(n+a)=4n+1+f` is divisible by f, hence b=(n+a)/f is integral.

All reconstructed variables are positive. A prime factor ≡3 mod4 of any form therefore gives a solution even if its exponent is even; the claimed support restriction, stronger than merely “sum of two squares,” is correct. For n≡1 mod4, removing the single factor 2 from n+1 leaves (n+1)/2. The three residues of n are −1, −4, −1/4 modulo the respective primes, all nonzero squares when the primes are 1 mod4. For odd m, `(m²+1)/2=((m−1)/2)²+((m+1)/2)²` has coprime summands; the other two displayed square forms do too. The primality claims 2273, 4549, 18181 and the explicit 409 witness check out.

## Engine audit — OK in the stated range

**Target sets (`census.c:37–39,51–57`).** f≡−1 modK and ac|(f+1)/K are equivalent to a positive integral d with f=Kacd−1. Both a and c are units mod f; the bitmap marks exactly a/c. A hit makes b=(cn+a)/f a positive integer: a positive integer divisible by positive f cannot have zero quotient. No additional upper bound on b or coprimality of a,c is needed.

**Exact fallback (`:25–32`).** By symmetry take a≤b. Every solution has e=(a+b)/c a positive divisor of a+b and Kabd=n+e. Necessarily `(Ka−1)b≤n+a`. Since b≥a, this implies `Ka²≤n+2a`, exactly the outer stop condition. For fixed a the inner inequality becomes permanently false once its stop condition fires. Also `Kab>a+b` for K≥4 and positive a,b, so e is uniquely the nonzero residue `−n mod Kab` if it lies in [1,a+b]; residue zero cannot represent a valid e. Testing divisibility and setting c=(a+b)/e, d=(n+e)/(Kab) is both necessary and sufficient. There is no missed d>1 solution, off-by-one error, or asymmetric restriction affecting positivity.

**Coprime/d-odd modes.** From bf=cn+a and gcd(n,f)=1, gcd(b,n)=gcd(a,n). Thus the bitmap path's tests on a,d are sufficient; the fallback's tests on ab,d are equivalent. d-odd is checked on the individual (a,c,d) before setting a bit and again when enumerating coprime hits, so collisions in target residues cannot introduce a false allowed witness. The fallback tests the actual reconstructed d. All restrictions are symmetric under a↔b.

**Range/overflow.** On this LP64 host and K=4,…,24, n≤10^10, FMAX≤40000, accepted fallback pairs satisfy `a≤50000`, `b≤(n+1)/3`, and `Kab≤n+a+b`; the first rejected pair and first rejected a are also far below u64 overflow. Reconstruction gives `f=(cn+a)/b≤2n+1` using a≤b and c≤a+b. Hence even the signed-long `K*a*c*d−1` computation is safe. All partial products are positive and no larger than their final product. Bitmap multiplications, inverse arithmetic, square checks, segmented sieve endpoints, and counters are safe at these limits. The sieve's `q*q>=e` break is correct for half-open segments. Very large arbitrary CLI arguments are not covered by this conclusion.

**Count engine.** Its ordered a,b loops have the necessary outer bound `(K−1)a≤n+1` (set b=1 in Kab≤n+a+b), and the same exact e test. It counts ordered tuples rather than distinct Egyptian triples, as advertised. c=1 is exactly e=a+b. No counting bug found; compiler reports only misleading indentation at line 18.

## Independent computation and numerical ledger

A fresh C enumerator `/tmp/z58_hostile_enum.c` enumerated a≤b, every divisor e of a+b, and every admissible d, formed n=Kabd−e, asserted the original equation, and weighted a<b twice. It used small flat arrays through X=100000, independently of target sets and of the production residue test. Companion Python checks ran with `uv run python` (SymPy only for independent primality checks). Temporary source/results are `/tmp/z58_hostile_{enum.c,counts.txt,check.py,check.txt,extra.py,extra.txt}`.

**OK — independent exhaustive overlaps, all n odd, squares excluded:**

| mode | zeros ≤100000 | comparison |
|---|---:|---|
| K4 | 1: 4545 | exact match |
| K8 | 123 | exact match with census_K8_1e7.txt |
| K12 | 797 | exact match |
| K16 | 2359 | exact match |
| K4 coprime | 86 | exact match; all divisible by 3 or 5 |
| K4 d-odd | 8 | exact match |
| K20, primes only | 634 | exact match |
| K24, primes only | 1230 | exact match |

The d-odd zeros already all occur ≤10000: **13, 301, 445, 685, 1981, 3105, 4545, 9121**. A separate literal (a,b,d) loop confirmed N_II(4545)=0 and matched exact ordered counts for 100 seeded random odd nonsquares ≤100000 other than 4545; all were positive. Both scaling bijections were also checked as complete-set equalities at seven composites for every dividing k≤11.

Production census compiled with UBSan matched every independent positivity flag through 100000 in K8, coprime-K4, and d-odd-K4 modes. FMAX=3 reproduced **6596** nonsquares on the exact path below 20000, with only zero 4545; the forced d-odd fallback below 30000 reproduced its eight zeros. `count.c` matched all six independent ordered counts at every sampled prime p≡1 mod4 ≤1000. A UBSan bitmap-only check near 10^10 produced valid independently reconstructed witnesses (no large-n brute-force enumeration).

**OK — every stored ZERO/LATE record was parsed.** All **267527 LATE** tuples satisfy the original equation and their stated f, positivity, and relevant coprime/d-odd restrictions. All ZERO and LATE prime/composite flags were independently checked with `sympy.isprime`. Aggregates agree with the memo:

- K4: only 4545 in the three files through 10^10; squares 4999 below 10^8, 34189 in [10^9,10^10); the lone middle-interval late witness is n=302812197, f=151406099.
- K4 bitmap maxima: 14111 at 92455209; 19711 in [10^9,10^10). Prime maxima 2495 at 2031121, 3359 at 281850319, 3799 at 6736278481. The 3359 versus Z57_BFII's 3263 is not a contradiction: the older witness census restricted p≡1 mod4, while 281850319≡3 mod4.
- Coprime K4: 142 zeros, last 21754425; exactly 137 divisible by 3 and the other 5 divisible by 5; all 1 mod4.
- K8: 129 nonsquare zeros, 22 prime and 107 composite; last prime 35569, last composite 1239315; no further ZERO records in the next two intervals through 10^9. Exactly the three claimed prime zeros are in Mordell classes: **1129→289, 3361→1, 35569→289 modulo 840**.
- K12: 3802 nonsquare zeros (170 prime); exactly 2887 are 3m², leaving 915; last non-twisted prime/composite 1998793 / 19156825.
- K16: 5269 nonsquare zeros, 447 prime, 4822 composite; last prime/composite 12895921 / 94165635.
- K20/K24 prime totals: 1164 / 3740; last 94965203 / 96577729.

**OK — all four Python outputs reproduce byte-for-byte:** `screens.txt`, `kernels.txt`, `ladder.txt`, `ladder2.txt`. Thus the 14/38/12 screen sizes and witness maxima 239/239/295 (K4), 1311 (K8 at the R8 screens), the 284/285 composite rescue count, the kernel counts 0/285 and 55/4822, all six sample means and both six-entry zero rows, fit coefficients, deviations, sample sizes, and 7.62/0.81 model totals agree with the supplied inputs. The approximate 2.1 restricted mean ratio is 2.14777. The 10^17 estimates are arithmetic extrapolations (full-family 3700–4540, c=1 approximately 183–260), not certified means there. The R8 comparison coefficients agree with Z57_SYNTH §2.1.

## Novelty and final assessment

**OK — no new ES proof, and target priority is acknowledged.** Z57_BFII already defines the full family, proves T1 and the slice/target forms, conjecturally targets prime positivity, and isolates 4545 through 10^7. `notes.md:22994–23006` states C_SQ′ with squares and {288,336,4545}; §61 gives the earlier bounded census to 10^6. CONV-II is the odd-domain continuation of that pre-existing target, not a new conjectural breakthrough. Lemma 4.1's c=1 case is prior; Lemma 4.4 is an elementary specialization of the prior slice identities. The new large-range census, numerator/coprime/parity diagnostics, and explicit packaging are useful contributions. The title's **“HOT TARGET, NO MECHANISM”** is acceptable as an explicitly subjective assessment, not as the brief's mechanism-level HOT LEAD. Retain the blunt “B2 unchanged” verdict, repair the scoped assertions above, and do not export the model's causal claims or unbounded positivity language to FRONTIER.
