# FORESTCLASS cross-model hostile review

**Verdict: ACCEPT-WITH-FIXES.** The mathematical verdict **Narrowed** is supported, not “dead”.
Reviewed `side-agent/z53-forestclass` at `ff90c123fc5c99b2d9264b4e874abcf2825730b3`.
The core theorems survive independent re-derivation and computation. Remaining fixes concern scope and interpretation.
ES remains OPEN; neither the conditional failures nor the finite successes decide ES or an all-prime root conjecture.

## Per-claim audit

| Claim | Classification | Independent check / limitation |
|---|---|---|
| §1 forest, neighbour criterion, endpoint bound | CORRECT | A larger vertex v has only possible smaller neighbour −p mod v; a cycle's largest vertex is impossible. Cofactor substitution gives the stated divisor condition. `(u−1)(v−1) ≤ p+1` gives the small-endpoint bound. |
| §1 SM / reduced forms, SM colour, SMN genus | CORRECT | Center a square root b modulo a; `c=(p+b²)/a ≥ a` for a≤√p. Discriminant −4p is fundamental, hence forms are primitive. Reciprocity gives the displayed colour; two genera follow from Gauss genus theory. Boundary restrictions are essential and are now stated. |
| §1 SP / all-cycle interpretation | CORRECT | For a<√p, choose P congruent to a square root in `(√p−a,√p)`; then `(P+√p)/a` is reduced. This establishes inclusion in the ordered union, not identity with one real class group. The memo's imprimitive/cutoff caveats are appropriate. |
| Theorem 1 | CORRECT, CONDITIONAL on Dickson | Full admissibility, character, component and isolation derivations checked below. No growing-menu conclusion follows. |
| Corollary 1.1(a)–(e) | CORRECT-WITH-FIX | Listed menus are covered, including powers of the specifically chosen prime-5 ideal. The closing parenthesis reintroduces unqualified “a split class”; restrict it to that ideal. |
| Proposition 2(i)–(ii) | CORRECT | At most `2^{ω(a)+1}=p^{o(1)}` reduced forms share a first coefficient; Siegel supplies `h(−4p) ≫ε p^{1/2−ε}`. This counts the FULL negative-discriminant minimum set, not truncated SM, SMN or SP. Fixed finite recipes cannot enumerate it. |
| Proposition 2(iii) | CORRECT | Square predicates depend on p mod a; reciprocity, including the 2-part, gives colour dependence mod 8a. The restriction on X relative to both primes' cutoffs is necessary and present. |
| Lemma G(1)–(4) | CORRECT | Character orthogonality gives the coset count; every real-character Euler factor is e+1, 0 or 1. Divisor parity vectors realize precisely the factor-generated span. For a∈SM all character coefficients are +1, giving the fair-share inequality. No converse is implied. |
| Proposition 3(i)–(iii) | CORRECT | `AC=p+b²`, `A≡−1 mod b²` is exactly the edge condition. Forms are primitive; neither A nor C is divisible by p. Mod p the form has rank one, so all nonzero represented values have the same Legendre symbol. Reciprocity gives the parity rule. |
| Proposition 3(iv) | CORRECT | For `0<b²<a`, the candidate parent is b². Exact divisibility reduces to `b² | a(c+1)`, then to `b² | c+1` since gcd(a,b)=1. The p=269 exclusion is correct. |
| Census / verified instances | AGREES on rerun scope below | Exact 10⁷ census and all listed failure/instance checks pass. I do not claim to have independently regenerated the entire 10⁸ census. |
| Genus-conditioned enrichment | CORRECT descriptive EVIDENCE; interpretation needs fix | All 24 tabulated ratios reproduce. Ratios 0.930–1.081 are point estimates, not a demonstrated ±10% detection threshold or a bound on all class-group effects. |
| Density / HC / “no mechanism found” assessments | ACCEPTABLE with scope fixes | No HC equivalence is established or now claimed. CRT density examples are valid; fixed-discriminant density heuristics do not furnish uniform estimates in growing p. |

## Theorem 1 re-derivation

1. With H,K fixed, the divisor-sum exclusion is O(H+K^{3/2}√q), hence smaller than (q−1)/2 for sufficiently large primes q≡3 mod4. The forbidden B therefore misses some non-residue c.
2. Every prime factor of 1+x is ≤Y and is not q; its exponent is below eℓ. Thus both linear-form coefficients are integral.
3. For ℓ≤Y, ℓ≠q, slopes vanish and constants equal 1 modulo ℓ. For q, c≠0 and the exclusions c≠−i ensure every constant is nonzero.
4. For ℓ>Y each form forbids one residue, and there are at most Y forms. Hence admissibility holds. Positive primitive forms are distinct (their intercept/slope ratios are `(p₀+x)/Q`, versus p₀/Q). Dickson applies; discard finitely many small p if needed.
5. Reciprocity gives χp(ℓ)=1 for ℓ≤Y other than q, and χp(q)=−1. Since K<q, numbers ≤Kq have q-adic exponent at most one; precisely q,2q,…,Kq are non-residues.
6. The three factorizations at 1,2,3 give exactly the eight-vertex residue component of LTA Theorem 3.1. Its five large vertices have only the displayed parents; no unexplored branch remains.
7. For 4≤i≤H, `Li≡1 mod i`, so a candidate divisor has residue e with e|i+1. The only possible e≡−1 is i−1, which cannot divide i+1.
8. At qj, divisors e alone cannot be −1 mod qj; divisors eL would force ec≡−1 mod q, explicitly excluded in B. These vertices are isolated.
9. Corollary: below q, SM=T and SP is the entire interval. Among the first K non-residues, SMN consists exactly of qs with s∈T. Genus minima are 1,q; ambiguous minima 1,2. Since 2 ramifies, 3 is inert and 5 splits, the least split prime is 5. A power of one ideal above 5 has primitive norm 5^k; centering its b yields a reduced form when 5^k≤√p. This is the specific orbit proved covered.

## Sources checked

* Read the cited local proofs in `LOWER_TAIL_ASTRA.md` (Lemmas 2.1–2.2, Theorem 3.1) and `Z52D_PELLCYCLE.md` (Prop 2.4). The imported forest facts are valid with their stated prime/unit restrictions.
* Siegel's required ineffective lower bound is stated explicitly in Olivia Beckwith, *Indivisibility of class numbers of imaginary quadratic fields*, §1: https://link.springer.com/article/10.1186/s40687-017-0109-x . Since −4p is fundamental, its hypotheses apply. Absorb the subpolynomial multiplicity using ε/2. “Relative to Siegel” means reliance on a proved theorem, not another conjecture.
* Checked Gauss genus count and assigned characters in Daniel Chong, *Quadratic Reciprocity, Genus Theory, and Primes of the Form x²+ny²*, Theorem 4.10 and its proof, pp.16–18: https://math.uchicago.edu/~may/REU2016/REUPapers/Chong.pdf . Here r=1, μ=2, so there are two genera and two ambiguous classes. The rank-one argument independently checks the assigned-character use on even represented values.

## Recomputed evidence

All shell commands used a timeout and virtual-memory limit (computations: `ulimit -v 6000000`).
Audit code: `scripts/z53_xrev_forestclass_check.py`; bounded sparse graphs, no dense vertex-pair arrays.

* **Full rerun to 10⁷:** all 165,976 primes ≡1 mod8; the summary is byte-for-byte identical to the corresponding retained block. Full failures ALL/SM/SP/NR/SMN/SQ = **0/1/0/0/34/176**; depth counts, lists and maximum ranks also agree.
* **Independent forests at 57 primes:** generated edges from divisors with the original `uv | p+u+v` test, BFS on the whole sparse graph, and general modular square roots for membership. Every size/hit/depth/first-rank entry for all six sets matches the C engine. Inputs include all **48 SMN failures**, **19441**, and all six advertised maximum-rank witnesses. SP hits at all 57; SM fails exactly at 19441 among them.
* **All 668 listed SQ failures:** reran the C engine, with zero hits at each. This confirms the listed failures, not completeness above 10⁷.
* **All 16 theorem instances:** independently explored every menu component to exhaustion. All are monochromatic; least non-residue lists agree. Recursive complete-factorization Lucas proofs establish every p, including the three >2⁶⁴, and every claimed prime Dickson form in the five all-prime instances. No reliance on probable-prime tests for these certifications.
* **Elementary dictionaries:** brute-checked Lemma G on 554 (p,a) pairs, square/form correspondence and parity on 433 incidences, and 520 reduced forms for primes p≡1 mod4 below 500. All pass.
* **Genus data:** reran the enrichment aggregation on all four retained raw genus tables. Exactly **213,838,739** obstructed vertices, **0** non-isolated; **0/94,823,144** SM and **213,838,739/574,180,858** non-SM. All 24 table entries agree, including residual extrema **0.930** and **1.081**.
* **Retained samples/controls:** independently re-aggregated all five sample files; sizes, zero failures, hit means and SM shares agree (SP at 10¹² is exactly 85.55, rounding to 85.6). Also confirmed retained outputs for 134 hard primes, 1,330 near-square primes and 5,000 odd squares. These are aggregate checks, not fresh whole-forest reruns at those scales.
* **Not regenerated:** the whole 10⁷–10⁸ census, 669-million-vertex genus sample, original 129,829-pair genus log, and comparator populations behind the quantile claim. No completeness/uncertainty guarantee for these is added by this review.

## Required fixes, in priority order

1. **Preserve the quantified scope everywhere.** In Cor 1.1's final parenthesis, change “orbit prefixes of a split class” to “orbit prefixes of the chosen prime-5 class”. In §8 replace “their bounded parts … die” by “the bounded menus enumerated in Cor 1.1 fail under Dickson”. The existing explicit exclusions elsewhere are correct; do not undermine them with these surviving blanket formulations.
2. **Do not turn the enrichment interval into a sensitivity claim.** Replace “no … effect … at the ±10% level” by “the reported genus-conditioned MH point estimates lie between 0.930 and 1.081; no confidence interval or detection threshold is established”. Common-support stratification and within-prime dependence matter. The data support consistency with a genus explanation, not exclusion of a larger effect in another statistic or root selection.
3. **Keep Prop 2's exclusion precise.** Remove or qualify §8's “non-quasi-polynomial root source” for “class groups of ±4p”: the proof excludes fixed finite value lists for the full −4p minimum set. It does not exclude polynomially indexed growing enumerations, prove a positive-discriminant analogue, or establish the same cardinality bound for truncated SM/SMN/SP.

After these scope/wording fixes, record Theorem 1 as CONDITIONAL, Props 2–3 and Lemma G as PROVED with the stated domains, and the numerical findings as finite evidence/certification. The growing-window question survives; no impossibility theorem beyond the enumerated menus is obtained.
