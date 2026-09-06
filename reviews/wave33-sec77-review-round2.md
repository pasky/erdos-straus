DEFECTIVE

Reviewed repaired source commit `f202c82f3b2756b166cc1537b9568f6e9107494c`. The principal round-1 arithmetic errors are fixed. In particular, (77.5), Lemma 77.10(ii), the typed progression count, and the truncated constant now survive scrutiny. However, several repairs stop before the downstream claims that contradicted them; the revised fibre description also remains mathematically false.

## Round-1 items

1. **REPAIRED** — Positivity is present; the invertibility argument is valid, and the second alternative correctly requires the parameter swap.
2. **REPAIRED** — The generated subgroup always contains −1 in the stated branch; −p can lie outside it, as the retained regression demonstrates.
3. **REPAIRED** — The positive, inclusive progression domain gives floor(p/(4ab))+1; independent enumeration gives 58 at p=409.
4. **PARTIALLY** — Unit restrictions, typed multiplicity, the constant, and the truncated proposition are correct, but Assessment 77.9′ still attributes mean C₀ to untruncated H; the empirical averaging domain also needs correction.
5. **REPAIRED** — The transformation now uses genuine homogeneous plane coordinates and gives the stated affine involution.
6. **REPAIRED** — The common-resolution/log-ring extension argument is legitimate; maximality is honestly conditional on the identified standard input, although its bibliographic locator remains unverified.
7. **PARTIALLY** — Proposition 77.9(i) now contains only the valid fibre identity, but the Assessment retains an unqualified prohibition on polynomial main terms without transfer.
8. **PARTIALLY** — The surface-automorphism scope is corrected, but the punctured fibre is not a Gₘ-torsor and the displayed single congruence does not characterize its integral points.
9. **PARTIALLY** — The named Lemma 17.2 families, character-coset distinction, and local valuation statement are repaired; §77.7 repeats the old unqualified small-prime claim and methodological necessities.
10. **REPAIRED** — Five class-number-one values, an explicitly interpretive class-group paragraph, and a separately flagged Burgess citation replace the previous overclaims; the norm-divisor discussion must be read with the Type-I normalization p∤k.
11. **REPAIRED** — The false m|c assertion is removed; denominator divisibility is the correct descent condition.
12. **REPAIRED** — The advertised finite domains now test all divisor hits, positive (77.5) hits, independently enumerated progression objects, and generated subgroups; the (77.5) reconstruction checks use exact integer equations rather than Fraction, which is sufficient.
13. **REPAIRED** — Both endpoints are included and the renamed Type-I domain is accurately stated; counts are now 443/712.
14. **PARTIALLY** — Typing resolves the uniqueness defect, but Lemma 77.2 still does not explicitly distinguish its unrestricted tuples from the coprime canonical tuples of Theorem 17.1.
15. **REPAIRED** — Both omitted divisibility cases are addressed; the no-equal-denominators result and the odd-fixed-point exclusion on this finite solution set are correct.
16. **REPAIRED** — Eighteen is the correct number of non-permutation elements.

## Remaining and new defects

### A. MEDIUM — The unproved untruncated mean reappears immediately after its disclaimer

**Quote, notes.md:31023–31024:** “Proving |Ωₚ|>0 is proving H(p)>0, a statement of mean C₀ — worse than polylogarithmic.”

Proposition 77.9(iii) now correctly proves only the fixed-cutoff means and explicitly says the untruncated mean requires an unsupplied tail estimate. The Assessment immediately uses precisely that unsupplied conclusion. If “statement of mean C₀” instead means the indicator of H>0, that is a different quantity and is not established either. An Assessment label does not resolve this contradiction.

**Minimal repair:** say “a positivity question for H, whose fixed-cutoff means tend to C₀(A)” and omit any conclusion requiring the mean of untruncated H. Alternatively actually supply the uniform tail estimate. This is a surviving part of item 4, not a defect in the new formula (77.8).

### B. MEDIUM — The repaired fibre is neither the stated torsor nor the stated integral model

**Quote, notes.md:30840–30844:** “the fibre is the punctured split conic … a Gₘ-torsor whose relevant integral points (those with qy−px≡−px (q)) are finitely many divisor pairs …”.

For a relevant fixed x, put A=px and X=qy−A. The complete hyperbola XY=A² is Gₘ. The fibre inside Uₚ° removes X=−A, corresponding to y=z=0. It is therefore Gₘ minus a point, equivalently P¹ minus three points, not a Gₘ-torsor. Over an algebraic closure a Gₘ-torsor is Gₘ, whose smooth completion has only two missing points.

Furthermore, the divisor-pair model needs BOTH X≡−A and Y≡−A modulo q. One congruence does not generally imply the other when the fixed denominator is divisible by p. Explicitly, take p=5, x=20, q=75, A=100, and (X,Y)=(125,80). Then XY=10000=A² and X≡−100 mod 75, but Y is not congruent to −100. Reconstruction gives y=3 and z=12/5, not an integral point. These are positive values, so signs do not explain the failure.

**Minimal repair:** distinguish the complete hyperbola from its punctured open fibre; require both congruences and positivity for solution points. Restrict any swap-only statement to the specified regular automorphisms and positive solution points, not arbitrary permutations of a finite set. The global S₄ theorem itself is unaffected.

### C. HIGH — The final wall-map repeats arithmetic and methodological overclaims that the repairs were meant to remove

**Quotes:**

- notes.md:31185–31187: “the small-prime part of t+s is the useless self-part s whenever 4t+1≡1 (mod L); the hit must come from the large prime factors of t+s”.
- notes.md:31165–31166: “A proof therefore has to turn the existence of non-residues into a divisor in a moving coset”.
- notes.md:31092–31095: “factorisations are unrelated beyond the character constraints … i.e. from an argument of the almost-all type”.
- Assessment 77.9′: “A polynomial main term without a transfer is a polylogarithmic main term multiplied by a trivially counted factor.”

The first quotation drops the valuation qualification carefully added earlier. At L=24, p=73, t=18, s=2, the window is 20: its part supported on primes dividing L/4=6 is 4, whereas the corresponding part of s is 2.

The assertion about where a two-target hit must come from is also false literally. At p=97, L=24, q=7, s=2, x=t+s=26, one has −p≡1 mod 7. The ratio u/v=1/1 already hits the Type-I target; it uses no prime factor of x at all. Formula (77.3) gives the exact solution (26,35308,364). The necessary non-residue in reconstructed Type-I parameters does not imply that a nontrivial ratio of large prime factors must furnish the hit.

Likewise, a necessary signature of an existing witness does not prescribe the order or method of every possible proof. No theorem here forces a cross-window argument to be almost-all, or a polynomial main term to be a trivially inflated polylogarithmic one. Those categorical assertions persist despite the nearby “known methods” qualifications and final impossibility disclaimer.

**Minimal repair:** propagate the precise valuation statement to §77.7; distinguish the existence of a non-residue parameter from the factors used in a ratio witness; replace the methodological necessities by observations about the particular approaches examined. Proposition 77.9(i) should not be used as evidence for them. These are surviving parts of items 7 and 9.

### D. LOW — The new empirical mean has an unstated exclusion of n=1

**Quote, notes.md:30996:** “empirical mean over n<4000: 0.4715”.

The progression in the proposition is positive n≡1 mod 4. But verify.py:15904 uses `range(5, Ns, 4)`, excluding n=1. Independent exact rational summation gives:

- C₀(30) = 0.4721847725869118.
- Mean over 5≤n<4000, n≡1 mod 4: 0.4715200944852169, rounding to 0.4715.
- Mean over 1≤n<4000, n≡1 mod 4: 0.4710485743907317, rounding to 0.4710.

Here H₃₀(1)=0; including it changes the denominator from 999 to 1000.

**Minimal repair:** specify 5≤n<4000 in the empirical sentence, or include n=1 in the code and print 0.4710. The asymptotic constant is unaffected.

### E. LOW — Canonical versus unrestricted tuple terminology remains unfinished

**Quote, notes.md:30667–30668:** “Type II data of Theorem 17.1(i)” and “Type I data of Theorem 17.1(ii)”.

The divisor construction does not impose the canonical coprimality condition. For example p=29, a=k=2, D=15 gives (a,b,c,k)=(2,4,1,2), not a coprime canonical tuple. Theorem 17.1(i) itself expressly allows dropping coprimality for the solution identity, so this is a terminology/scope problem, not a failure of reconstruction. The requested distinction has nevertheless not been added.

**Minimal repair:** say “unrestricted positive parameter data satisfying the identity; canonical data are obtained by re-decomposition as in Theorem 17.1”.

## Additional new verifier fragility

At verify.py:15976–15978, `if (-p) % q not in H: ... assert not hit` asserts absence of BOTH targets from absence of only −p from the subgroup. This happens to hold for the single occurrence in the visited sample, so it is not a failing assertion on the advertised domain. It is not a valid general implication.

Counterexample: p=1609, x=407=11·37, q=19. This is another hard-class prime, and

    Rat_19(407) = H = {1,7,8,11,12,18},     −p mod 19 = 6.

Thus −p is outside H but −1 is hit, already by 37≡−1 mod 19. The replay does not visit this window because it stops at an earlier success.

Replace the assertion by `assert (-p) % q not in R`, or explicitly label the stronger assertion as a sample-specific observation and add this counterexample as a complementary regression. Lemma 77.10(ii), as repaired in the text, does NOT make this erroneous implication.

## Checked and found correct

- **Invertibility and renaming in (77.5):** writing k=pj gives E=4acj−1 with gcd(j,E)=1. Multiplication by j turns E|(4a²c+1) into E|(a+j), contradicting 0<a+j<E. Conversely, D|(pa+k) with p|k also gives E|(a+j) directly. Thus both directions are valid; this is not merely a cosmetic insertion of positivity.
- **The subgroup claim:** q≡3 mod 4 implies q−1 has exactly one factor of 2. A nonsquare therefore has even order; the generated subgroup contains the unique involution −1. This would require care for q≡1 mod 4, but that is not the lemma's setting.
- **The constant and distinct classes:** a+b≤2ab<4ab, so every counted divisor is genuinely below the modulus. Within each type, d↦−d and d↦−d⁻¹ are injective on the admissible unit divisors. Overlaps BETWEEN types must be counted twice because witnesses are typed. The contribution is (1/M)·(2τ₃*)·(4/M)=2τ₃*/(4a²b²). For convergence, the elementary bound τ(a+b)≪ε(a+b)^ε with 0<ε<1 gives an absolutely convergent double series. No untruncated Cesàro interchange is needed for this assertion.
- **The extension argument:** the graph of an open automorphism and a boundary resolution supply the common smooth compactification, with the same open subset under both morphisms. For a blowup at a boundary point lying on r=1 or 2 components, K_X+E=π*(K+D)+(2−r)F. The extra divisor is effective exceptional, so the pullback identifications of logarithmic section spaces preserve products. This also explains the required naturality of the cited invariance, rather than merely equality of dimensions. The resulting graded automorphism of the polynomial section ring acts through GL₃ on degree one and hence PGL₃ on Proj. Its Proj action agrees with the original map on V and therefore preserves D. The S₄ maximality conclusion is sound; no new geometric counterexample was found.
- **Independent numerical checks:** all 1181 hard primes below 10⁵ give 1149 first witness windows satisfying Lemma 77.11, with largest first modulus 31. A separate divisor-ratio enumeration reproduces 183 F1 failures, one −p subgroup exclusion, and 455 visited windows. Direct progression enumeration gives 58 objects/22 typed witnesses at p=409 and 32 objects/14 typed witnesses at p=97, with a,b≤60.
- **Independent exact reconstructions:** for p<800 and a,c,k≤25, all 810 first-alternative and 923 positive second-alternative (77.5) hits reconstruct positive integer denominators and sum exactly to 4/p using Fraction arithmetic.
- **Labels:** the repaired numbered algebraic assertions survive, with Theorem 77.4(iii)'s cited input explicitly disclosed. The remaining substantive problems occur in geometric consequences and Assessments; those labels do not validate false arithmetic or unsupported universal necessities.

Only `check_by`, not the full verifier, was executed. It passes in about 1.4 seconds and prints: 59 prime reconstructions; 1262 brute solutions; 1183 Lemma-77.2 hits; 1070 (77.5) hits; 2847 τ images; group order 24; signature counts 443/712; 647 free S₃ orbits; 688 pigeonhole instances; mean/constant 0.4715/0.4722; Ω₄₀₉=58; F1=183; subgroup exclusions=1; windows=455. Independent scripts were streaming, bounded to approximately 1 GB address space and at most 120 seconds. One initial script stopped on a SymPy Boolean/integer type error; correcting that bookkeeping error produced the successful independent counts reported here.

No source files were edited. The conclusion “no pointwise mechanism found” remains defensible; the stronger claims identified above still require repair.
