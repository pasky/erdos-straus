# z54 HCKILL — independent hostile cross-review

Reviewed `side-agent/z54-hckill` at `cd4345366f4452292b5134a23bd487aa5aaef492`.
**Verdict: ACCEPT-WITH-FIXES.** The conditional K(4) theorem survives; one algebraic converse is false literally but has a local repair. ES remains OPEN.

## Per-claim findings

| Claim | Classification | Independent check / limitation |
|---|---|---|
| Lemma 1.1; K(4)=K(5)=K(6) | CORRECT | An odd integer has a 3-mod-4 divisor iff it has a 3-mod-4 prime factor; the window contains only line 4. |
| Lemma 1.2(a–c) | CORRECT | Exponent-2 groups give exactly subset products. The odd-character constructions and the odd-order/order-4 counterexamples work. “Largest” means maximum cardinality. |
| Remark 1.3 | CORRECT | Substitution gives determinant 15 and norm 16p+34; the stated lattice congruences make the inverse integral. S means primitive representations, not arbitrary sums of squares. |
| Theorem Q; Bunyakovsky implication | CORRECT | Primitive norms m²+1 and (2m)²+1 exclude inert primes; primality forces 3 divides m. The polynomial 720k²+1 is irreducible with no fixed prime divisor. |
| F1 necessity and generic-prime sufficiency | CORRECT-WITH-FIX | Chebotarev plus CRT proves equality of the *primitive inducing* characters. Equality as characters modulo x requires induction, which changes values at primes dividing x. |
| F1 final local “iff” | WRONG as written | It omits primes dividing x but not the conductor, where the induced character is zero. Explicit counterexample below; repair does not affect Theorem E. |
| F2 | CORRECT | Solve δ+16a=U² and δ+a=W²; positivity gives 1<abs(U/W)<4. The examples and the integrality obstruction check. |
| F3 | CORRECT / CERTIFIED agrees | The two square classes, quartic and elliptic model check; PARI gives rank bounds [1,1], conductor 735, torsion C₂×C₂. The 17 sampled ratios have 7 real-admissible points, all locally obstructed. |
| F4 | CORRECT | Four independent quadratic extensions, eight disjoint simple branch points, degree 16: 2g−2=−32+64, g=17. Faltings gives finitely many ratios, not a finite list or nonexistence. |
| F5 | CORRECT | δ+4aq in q times rational squares has positive odd q-adic valuation, hence q divides δ. Only confinement by this fixed family is excluded for a growing window. |
| F6 | CORRECT | Completing the square leaves at most one zero constant; every other nonsingular binary form represents the required nonzero residue over each good finite field. CRT meets a full-rank coset. |
| EH formulation; Theorem E | CORRECT (CONDITIONAL) | Ordinary EH suffices. Full sieve audit below; no generalized EH, shifted-prime distribution or Type II hypothesis is hidden. |
| Proposition A | CORRECT relative to BV | Weighted BV errors are absorbed by choosing the logarithmic loss in D; s tends to 1/(2ζ)>2. For ζ<1/8 use the general positive linear-sieve f, not its restricted explicit formula. |
| Vector-sieve threshold | CORRECT | Half-dimensional f/F=arccosh(sqrt(s)); concavity gives θ>cosh²(1/2)=1.2715403174. This is an obstruction to the stated allocation, not all methods. |
| K(7) ledger | CORRECT as Assessment | Four half-dimensional restrictions give dimension 2; s=2 is below the quoted limits. This does not rule out other EH arguments or the anatomy alternative. |
| Census, family, constants, controls | AGREEMENT | Reproduction details below; none establishes an asymptotic or infinitude. |
| Labels and final verdict | CORRECT-WITH-FIX | “Strengthened (conditional) + narrowed” follows. Keep the FI analogy separate from a direct citation proving the new pair; fix F1 and “smallest ratios”. No ES overclaim found. |

## Priority audit: ordinary EH and every step of Theorem E

1. **Exact hypothesis.** For fixed θ<1 the memo assumes, for each A>0,
   Σ(q≤x^θ) max((c,q)=1) abs(π(x;q,c)−li(x)/φ(q)) ≪(A,θ) x(log x)^(−A).
   Ford [S2, (7.6), Conj. 7.3] states standard EH with an additional maximum over y≤x; that version directly implies this one. The memo only needs the endpoint x. Full EH implies the required fixed θ₀; no endpoint θ=1 estimate is asserted.
   FI [S1, pp. 2–3] instead uses ψ, max over y, and Q=x^(θ−ε). Do not call the fixed-exponent versions literally identical: allow a small exponent margin when translating. Existence of some sufficient θ₀<1 is unaffected.
2. **CRT and weights.** Roots are units, with ν(3)=1 and ν(ℓ)=2 otherwise on 𝒫. Thus φ(8d)=4φ(d), X=li(x)/4 and g(d)=ν(d)/φ(d) are correct, including the shared root at 3.
   Write E(q) for the endpoint maximal error. The required remainder is bounded by Σ(d<D)6^ω(d)E(8d). Cauchy gives its square ≤(Σ E(8d))(Σ 36^ω(d)E(8d)).
   The trivial E(8d)≪x/φ(8d), and Σ μ²(d)36^ω(d)/φ(d)≪(log D)^36, turn arbitrary logarithmic savings in ordinary EH into the weighted saving. All moduli 8d are ≤x^θ. There is no stronger divisor-weighted conjecture.
3. **Linear-sieve hypotheses.** 0≤g(ℓ)≤1/2. Mertens/PNT in the fixed progression 3 mod 4 gives the required product ratio with exponent **1**, not 1/2: two roots on half the primes. Use its O(1/log w) remainder, not merely a harmonic-sum O(1).
   [S3, (3.4), Lemma 3.6] supplies the general product-condition beta sieve; β(1)=2. This covers these non-pointwise densities (a theorem restricted to g(ℓ)=1/ℓ+O(ℓ⁻²) would not suffice).
4. **Positive lower bound.** s=(1−η)/(1/2−η)+o(1) lies in (2,2.25+o(1)]. The linear f(s)=2e^γ log(s−1)/s is ≫η, while XV(z)≍x/log²x, uniformly for 0<η≤1/10 once x is sufficiently large depending on η. Hence c₁η x/log²x is justified.
5. **Survivor structure.** Each N is 1 mod 4 and ≤4x+1<z³. Its inert prime factors have even total multiplicity, so a bad N has exactly two, including possible equality q₁=q₂. The residual m belongs to S and is ≤5x^(2η). Nothing assumes squarefreeness.
6. **Upper sieve on the switched variable.** Keeping k≥q₁ ensures Y≥z≥x^0.4. For the endpoint case the forbidden roots come from k, mq₁k−4, and 4mq₁k−15 (the last only at inert primes). The relevant prime values exceed w=x^0.01; the other shift was already sifted to z.
   At 2 there is one root, at 3 two, at split ℓ not dividing m two, at inert ℓ≥7 three, and at ℓ dividing m one. Thus no local obstruction is overlooked. Since q₁>w, it causes no coefficient exception.
   The product-condition upper sieve has dimension at most **5/2**, uniformly in m,q₁: deleting roots at divisors of m only improves its product-ratio axiom. [S2, Thm 2.4] even gives an error O(w log²w), using abs(r_d)≤3^ω(d), negligible against Y/log^(5/2)x. The memo's larger level Y^(1/2) also works.
   Relative to the generic Euler product, each ℓ dividing m contributes (ℓ−1)/(ℓ−2)≤1+2/ℓ, since ℓ≥5. Consequently the bound Y h(m)/log^(5/2)x is uniform, with constants independent of η.
7. **Half-dimensional saving.** Σ(m≤M,m∈S)h(m)/m≪sqrt(log M), by its Euler factors 1+1/ℓ+O(ℓ⁻²) on split primes. With M=5x^(2η) this is ≪sqrt(η log x), not a bound losing an η-dependent constant.
   The inert-prime reciprocal sum from z to C sqrt(x) is (1/2)log((1/2)/(1/2−η))+o(1)≪η. Their product gives C₂η^(3/2)x/log²x. Both factors of η are essential and are present.
8. **Level case and subtraction.** Set k=k₀+4j so mq₁k≡1 mod 4; sieve k, (mq₁k−1)/4, (mq₁k+15)/4. Odd-prime root counts are identical; the interval scale changes only by an absolute factor. Use C sqrt(x), e.g. C=3, for its q₁ bound to include sqrt(4x+1).
   Therefore both bad sets have the stated uniform bound, and choosing η₀=min(1/10,(c₁/(4C₂))²) leaves a positive main term. **K(4) under standard EH survives this audit.**

## Required fixes, in priority order

1. **Repair F1's character convention and local iff before recording it as PROVED.** Take x=20, a=5, δ=39600. Then δ+4ax=200² and x(xδ+4a)=3980², so both primitive characters are χ₋₄ and the listed conductor tests pass.
   Integrality forces y=10t; p=5t²+1980 is 1 mod 8 for odd t. For odd t with 199 not dividing t, p+20=5(t²+400) and 20p+1=(10t)²+199² both lie in S. These classes avoid every exceptional prime with χ₋₄≠1 in F1's stated test.
   Nevertheless p+20 is always divisible by 5, and **every character modulo 20 is zero at 5**, so no such family satisfies the literal definition. At t=1 the shifts are 2005=5·401 and 39701=29·37².
   Preserve the definition by inducing χ_D to modulus x, enlarging the exceptional set to primes dividing 2axgD, and testing the induced character; equivalently impose coprimality of both window integers to x in addition to the existing primitive-character tests. This excludes the counterexample. F2–F5 at lines 4,7,8 and Theorem E are unchanged.
2. **Make sieve citations precise.** Replace “Thm 8.4/2.2, as commonly cited” by verified statements with the product-condition hypotheses, such as [S3, Lemma 3.6] and [S2, Thm 2.4]. Record the uniformity and local counts in audit items 6–7. The original HR numbering was not independently verified.
3. **Minor wording.** State dependence on fixed θ in EH; distinguish FI's weighted theorem from this independently proved adaptation; replace “17 smallest ratios” by “17 ratios sampled from abs(n)≤16 and torsion translates”. The enumeration is not a height-minimality certificate. Specify a full-rank lattice coset in F6: CRT needs this, and restricting a nondegenerate quadratic to a rank-one coset can recover Theorem Q.

## Reproduction and evidence

All shell executions used `ulimit -v 6000000` and explicit timeouts; the independent checker bounds PARI's stack at 128 MB. No dense pairwise arrays were used.
- Recompiled and reran the branch census through **10¹¹**: 295, 2226, 16125, 125059, 986400, 7962940, **65618311**, all agree. The saved source output additionally has timing lines, so whole-file `cmp` differs only at that suffix. Independent direct factorization through 10⁶ gives 295 and 2226.
- Regenerated all **5719** family primes through 10¹² and reran the HC engine; both outputs match the source files byte-for-byte. HC distribution: 7:5117, 8:481, 12:94, 15:21, 16:1, 20:4, 23:1. All nine listed control-prime HC values agree.
- Independently enumerated E₇ without treating unfactored cofactors as primes. The 7 real ratios have inert obstruction witnesses 19,31,19,1123,1483,3,19; all four square-class conditions were checked by exact rational-square tests. Confirmed 3H=(−1440,31200), height 0.3445890384, and genus 17.
- Independent Euler products through 10⁷ give K=0.3271293674, 𝔖=0.9602399388, C=0.4110350193. Shifted-integral ratios at 10⁵,10¹⁰,10¹¹ are 0.811258,0.962270,0.965984. These are heuristic comparisons, not proofs of the proposed constant.
- Reproducible independent checker: `scripts/z54_xrev_hckill_check.py` (run command in its docstring). The branch census/family engines were extracted into `/tmp/xrev_HCKILL`, not changed.

## Sources actually inspected

[S1] [Friedlander–Iwaniec, Acta Math. 202 (2009), published PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6709-11511_2009_Article_33.pdf): pp. 2–5, §§6–7 and Appendix B. Confirms A(θ), Theorems 3–4, the primitive indicator, divisor-weight removal, and the two-large-primes mechanism; not a theorem for this exact pair.
[S2] [Kevin Ford, Sieve Methods lecture notes (2023)](https://ford126.web.illinois.edu/sieve2023.pdf): product axiom (Ω), Thm 2.4 (uniform upper sieve), (7.6) and Conj. 7.3 (ordinary EH).
[S3] [Nath–Xie, arXiv:2501.16723](https://arxiv.org/html/2501.16723): Thm 1.1, (3.4), Lemma 3.6, Prop. 3.10, §5; confirms both beta-sieve dimensions and the quoted half-dimensional functions. [Tao's linear-sieve notes](https://terrytao.wordpress.com/2015/01/29/254a-supplement-5-the-linear-sieve-and-chens-theorem-optional/) independently confirm f(s), but their pointwise density hypothesis is not the needed general formulation.
[S4] [Franze, arXiv:1012.3809, Table 1](https://arxiv.org/pdf/1012.3809): dimension-2 limits 4.266 and 4.516 agree.
[S5] [Sedunova, arXiv:2609.28200, abstract](https://arxiv.org/abs/2609.28200): recent hyperbolic-shell work concerns squarefree/almost-prime distances, not an unconditional prime two-shift theorem. The memo's literature absence statement remains coverage-limited, not a certified impossibility claim.

**Disposition:** accept the conditional K(4) result and the narrowed hierarchy after these fixes; do not record F1's current local converse verbatim. No unconditional K(4), no K(7) from this sieve, and no advance toward proving ES are established.
