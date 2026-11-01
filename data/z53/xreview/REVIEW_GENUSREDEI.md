# Cross-model hostile review — GENUSREDEI

Reviewed `side-agent/z53-genusredei` at `ac73f7ae98ca9d44b5ed97084df901fb4f3569e1`.
**Verdict: ACCEPT-WITH-FIXES.** The main conditional realisation theorem survives independent proof checking; some concluding claims do not. ES remains OPEN.

## Per-claim assessment

| Claim | Classification | Independent check / qualification |
|---|---|---|
| Lemma 3.1, L1 | CORRECT | Exact valuations make the integer quotient L/s constant mod T; no cancellation of a nonunit is used. |
| Lemma 3.1, L2 | CORRECT-WITH-FIX | Multiplicativity and Frobenius give the stated law. Replace the malformed `y^{p/n}` explanation by `σ(y^{1/n}) ≡ (y^{1/n})^p (mod 𝔓)`, then divide by the root. |
| Lemma 3.1, L3–L5 | CORRECT | Reduce p modulo each factor, use p ≡ 1 (4), reduce the other line via its resultant, then apply reciprocity. The B-bound ensures all denominators and symbols are units. |
| JRT, conditional on HC | CORRECT | Re-derived Steps 1–5, including the intersection and abelianisation computations; details below. This is not an unconditional theorem. |
| Corollary 4.1 | CORRECT-WITH-FIX | Its iff follows from JRT. In the explanatory sentence listing the remaining class constraints, retain L5 as well as L1/L3/L4: fixed mutual symbols also constrain classes mod 4. |
| Theorem U | CORRECT | Fixed chosen primes and CRT lifts give exact divisibility. The compatible fibre product with Q(ζ_W) has a nonempty conjugacy-stable set; Chebotarev supplies a positive-density subset. No primality of residual cofactors is needed. |
| Proposition D | CORRECT | For example r = 13 satisfies the stated datum conditions with M = 3600. The one-factor realisation is precisely a cousin-prime assertion in that progression. This is a hardness implication, not an equivalence with all of Dickson. |
| Corollary F | CORRECT | The singleton configuration is compatible: Jacobi symbols of actual, possibly nonsquarefree rough integers establish L3/L5. JRT supplies simultaneous prime cofactors; the converse uses actual divisors. The signed version uses exponents −1,0,1 for the last prime. |
| Proposition 5.4(a) | CORRECT | Coprimality excludes factors of αβm; −αβ is a nonzero square modulo every factor. For the stated ES lines, the negative-discriminant character is odd. Keep the oddness/coprimality restrictions. |
| Proposition 5.4(b) | CORRECT | αm²+c² = γL and gcd(m,c)=1 give (−α/ℓ)=1 for the specified odd factors. For odd prime p on p+4d, all factors are odd; the asserted mod-4 obstruction follows. |
| Lemma P | CORRECT | Every nonempty proper subset map from the product-one twist group onto H has equal fibres; the union bound is strictly smaller than the whole group. This concerns unsigned subset products and formal class data. |
| Corollary P″ | CORRECT | Reduction of unit groups is surjective; lift square twists, take the final lift as inverse product, and preserve all quadratic characters and mod-4 classes. JRT then applies. Keep the event-present, non-B1, size-bound, squarefree and HC hypotheses. |
| §6.1 free-model evidence | REPRODUCED | All five principal runs agree numerically. These are descriptive, correlated diagnostics, not a proof of absence of hidden laws. |
| §6.2 census | REPRODUCED | 17,932 instances, zero violations, 12 projected configurations. The boolean fourth-power flags merge the two nonresidue symbols ±i; this is not an exhaustive census of full D2 configurations. |
| §6.3 census | REPRODUCED | Exact scan and level histogram agree, including the R category. The subsequent identification of missing information with the odd-order part is WRONG. |
| “Narrowed”; §§7–12 closure language | CORRECT-WITH-FIX | Fixed-family forcing from Π alone is exactly B1 under HC. This does not prohibit forcing from prescribed factor decorations, or classify all possible growing-family arguments as counting arguments. |

## Proof audit of the conditional core

1. Chosen-factor congruences have coprime moduli and nonzero residues; Dirichlet selects distinct primes outside the ramification set. Reciprocity supplies the reverse prescribed symbols.
2. Varying the lift of p modulo ℓ² varies L(p)/ℓ bijectively modulo ℓ. This both ensures exact divisibility and sets the same-line chosen–last symbol.
3. Over K₀ = Q(ζ_n), valuations at distinct chosen primes show independence of their Kummer classes. Any nontrivial Kummer intermediate extension ramifies at some chosen prime, whereas Ω does not. Thus Ω ∩ K = K₀.
4. In the fibre-product Galois group, cyclotomic conjugation sends v to v^u. For odd n, u = 2 kills V in the abelianisation; for even n, u = −1 kills V². The surviving quadratic fields give exactly Ω_tot^ab = Ω^ab(√ℓ_x). This rules out the hidden abelian compatibility obstruction.
5. The conductor of that field divides W. Compatibility on Ω^ab is the datum condition; on each √ℓ_x it is exactly L3. The HC conjugacy-class formulation permits choosing a prime above p with Frobenius exactly σ₀.
6. All residual forms are integral and positive-slope. At q ≤ B and chosen ℓ they are constant nonzero modulo q. At every other q their at most r+1 roots cannot cover F_q, since q > B ≥ r+1. Substitution k = mj preserves this admissibility.
7. Product laws determine last classes and symbols. L4 determines last–chosen cross-line symbols; reciprocity then supplies chosen–last symbols, and L4 finally determines last–last symbols. No unspecified mutual symbol remains.
8. U uses the same construction without demanding prime residual forms. F uses the singleton specialisation. P″ uses square lifts preserving all five laws. None needs an unproved extra independence assertion beyond the explicitly assumed HC.

Checked the cited internal source `CLASS_FORCING.md`, Proposition 3.2 and corrected §6: the abstract forcing criterion and the stated HC compatibility hypothesis match. HC is explicitly a hypothesis, not a cited published theorem. The speculative Iwaniec/governing-field remarks are not premises of the accepted results and are not independently certified here.

## Recomputations

All executions used `ulimit -v 6000000`, a CPU limit, and explicit `timeout`; extracted source/data lived in `/tmp/xrev_GENUSREDEI`.
Compiled `z53_genusredei_freemodel.c` with `gcc -O2 -Wall -Wextra ... -lm`. Ran:

- `P 10000000 12000000 15 15 0` and the same with model `1`: 61,812 primes; stratum sums 100.3 and 101.4; L3 0/2,760,681, L2 0/1,848,806.
- `P 100000000 104000000 15 15 1`: 108,397 primes; stratum sum 123.9; L3 0/5,199,388, L2 0/3,242,096.
- `S 1000000 400000000 15 15 1`: 9,500 squares, zero events on every retained line; output byte-identical.
- `N 1000000 400000000 15 15 1`: 13,220 primes; stratum sum 1283.2; L3 0/618,052.
- Via `uv run --with sympy`, `z53_genusredei_configcensus.py 3000000`: output byte-identical, counts 1010–1225 and 2169–2328 as reported.
- `z53_genusredei_twistscan.py 100 10000000 10400000`: output byte-identical; 12,370 primes, 84 without B1, 23 all-protected, one eventless; R=1, P2=85, P2x=173, Q=89, U=0.
- `z53_genusredei_twistlevels.py` on that rerun: output byte-identical; 75/89 Q levels at C=1,2,3,6 and 258 protected levels.

Other free-model diffs consist only of a newly printed zero-valued gcd-exclusion line and, for the uniform run, `MODEL=0` in the header. No numerical discrepancy. The separate test-prime probability summary was not rerun and is not needed for this verdict.

## Required fixes, in priority order

1. **Correct the surviving odd-part conflation (§6.3).** Replace “elsewhere the odd-order part ... is the irreducible input” with “information beyond the quadratic quotient, potentially higher 2-primary or odd-order information, can be necessary.” Independently checked the memo's own example: p=1901, t=32, N=60833=127·479. Classes (31,31) have the event; the product-preserving square twist (23,7), using (9,25), does not. The entire unit group is a 2-group; its odd-order part is trivial. Thus the existing reading is false, not merely unproved.
2. **Preserve the conditioning distinction in §§8/11/12.** A no-go for Π-only forcing does not mean factor decorations cannot force the event. Independently checked p=73, p+4=7·11: both (ℓ/73)=−1; with B=5 the smooth part is 1 and g=1 mod4, so B1 does not force the event, but those decorations force both factors to be 3 mod4 by L3. The memo itself recognises this exception earlier. Carry it into the bottom line, and explicitly retain the squarefree domain there.
3. **Do not promote sufficient bounds or methodological assessments to necessity claims.** “Only where G² is small” must mean outside the precise P/P″ inequality, with its k and |Σ(s)| dependence, not an absolute restriction on levels. The 75/89 statistic is sample-specific. JRT does not prove every remaining growing-family mechanism must be counting rather than algebraic; label that proposed direction Assessment. Likewise the §1 “PROVED, §5.4” bullet's universal exclusion of extra Frobenius laws depends on HC/JRT, not on the square-law proof.
4. **Local clarity repairs.** Fix the Frobenius formula in L2; retain L5 in Corollary 4.1's abbreviated list; call the 12 census bins projected configurations. Keep Lemma P/P″ explicitly about unsigned events unless a separate signed twisting argument is supplied. Replace the stale calibrated-χ² wording in generated output if those outputs are republished.

**Disposition:** record the elementary laws, U, D and formal P, and the explicitly conditional JRT/F/P″ with their stated scopes. “Narrowed” is justified; blanket closure of decorated-factor forcing or of all algebraic growing-family routes is not.
