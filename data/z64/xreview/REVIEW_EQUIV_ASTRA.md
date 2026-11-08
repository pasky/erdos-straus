# Retro cross-model review — Z64_EQUIV (Astra)

Reviewed merged `Z64_EQUIV.md` at `311454873`, including `data/z64/equiv/sources/` and the prior Opus review.
**ES remains OPEN. Verdict: ACCEPT-WITH-FIXES.** E1–E10 re-derive with the domains below; the remaining fixes concern
scope, a Hurwitz count overclaim, and screening language. This is not an audit of the full SWZ proof.

## Per-claim audit

| Claim | Classification | Independent derivation / exact domain |
|---|---|---|
| E1, k-Frobenius | CORRECT | For each prime p, existential coprime positive generating **pair** (u,B), k=4C−1≥3. The representation count is for that supplied pair, not an intrinsic invariant of its semigroup; generators 1 are allowed. gcd(u,B) divides p and cannot equal p by the size bound. Beck–Robins Thm 3 gives the claimed maximum. |
| E2, stacky line | CORRECT | Over ℂ, existential positive coprime u,B and C≥1: Pic ℙ(u,B)=ℤ, ω=O(−u−B), π*O(1)=O(uB). Equality of line bundles is precisely p=4CuB−u−B; E1 supplies coprimality at primes. |
| E3 / Lemma A | CORRECT-WITH-FIX | For every odd n≥5, all three statements are equivalent. Riemann–Hurwitz proves (c)⇒(b); uniformization, Selberg and the normal core prove (b)⇒(c). The signature analysis below closes (b)⇒(a). The unqualified 6888 bound is false, not the equivalence. |
| Lemma A corollary | CORRECT | At primes p≡1 mod 4 the two-term case is impossible, and the only primes in the sporadic list are 23,47≡3 mod 4. Thus only triangle signatures occur. |
| E4, diagonal lct | CORRECT | Every integer n≥5: Kollár (16.1) is min(1,1/a+1/b+1/c); 4/n<1 removes truncation. Exponents are existential positive integers. |
| E5, pretzel / Seifert | CORRECT | For positive integers n,x,y,z, det P=xy+yz+zx and absolute rational Euler number=Σ1/x. Multiplying by n gives the exact Egyptian equation. No prime hypothesis needed. |
| E6, length-three plumbing / sign | CORRECT | Primes p≡1 mod 4, 0<q<p. The determinant is p=tuv−u−v and cofactor A=tu−1; linking is ±A/p. The sign ambiguity has Legendre symbol +1 precisely in the stated prime class. The target is W∧S, not the vacuous implication S alone. |
| E6, AMP non-minimality | CORRECT | For u,B≥2 and prime p (necessarily odd here), only configuration (a), a −4 vertex, survives: C=1 or 4∈{u,B}. (d) needs both ends 2, making p even; all other configurations require a forbidden middle weight or more vertices. Read the actual diagram, not only its text layer. |
| E6, relaxation T | CORRECT | At p≡5 mod 8, p/2=[[(p+1)/2,2]] and (2/p)=−1. This supplies a length-two filling without a length-three certificate. |
| E7, critical polynomial / sign | CORRECT | W is exactly the ≥2-letter determinant image. A unit 2×2 minor makes the cokernel cyclic; gcd(tu−1,n)=gcd(tu−1,u)=1, so e₁ generates and has value A/n. Changing generator multiplies A by a unit square. Identification with W∧S is restricted to non-square n≡1 mod 4. |
| E7, CONV-II / U₇ | CORRECT | Formal endpoints may equal 1. 4abcd−a−b=cn is exactly K(a,4cd,b)=cn. The corrected U₇ statement is at n itself: K(x,g,z)=n, 8 divides xg. Setting f=xg−1 recovers the divisor condition (if g=1, the least residue is 1 rather than x, still a divisor). |
| E8, matrix / torus | CORRECT-WITH-FIX | For n≥1 the matrix product and its inverse parameterization agree. The last torus clause must explicitly retain upper-right entry n, c∈4ℕ and a,d≥1. Those give trace≥6. The bare Anosov/marked-torsion condition is false as an equivalence; see fix 1. |
| E9, ray class | CORRECT | For each fixed C,n≥1, (4Cu−1)(4CB−1)=4Cn+1. A divisor ≡−1 and its cofactor recover positive u,B. All factors are units modulo 4C; multiplicative Artin symbols translate exactly to complex conjugation. |
| E10, ideal divisors | CORRECT | For each prime p≡1 mod 4 and fixed c≥1, O_K=ℤ[√−p]. The odd norm 4c²p+1 avoids ramification. Primitivity excludes inert factors and simultaneous conjugate factors, so ideal divisors correspond bijectively to integer divisors, with their norms. |
| E11 / Lemma F | CORRECT-WITH-FIX | Lcm and CRT arguments work at odd primes (nonvacuous cases p≥5); at 2 the statement of **three branch points** fails. With this domain repair the implication chain and genus formula hold. |
| Lemma R / type-I observation | CORRECT | Re-derived 3v−2=m², F(2,m²+2)=m², and the five toric ratios for xᵃyᵇ(x+y³). The inequalities make the last ratio minimal, and the allowed intervals cover n≥6. The type-I observation is a tautology; the four-type classification is only Assessment. |
| §5.1 sign census | CORRECT / AGREES | Exact rerun reproduces 362852 Dedekind checks, 9913628 word checks, and 20 negative mod-4 cells, with zero failures. This confirms a sign dictionary, not existence. |
| Hurwitz precedent citations | CORRECT, count caveat | SWZ's claimed theorem and mechanism, EKS's composite obstruction, and Petronio's norm-family statements match the originals. The claimed O(1) count for rigid genus-zero data is not justified by these statements; see fix 2. |
| Lemma H | CORRECT, CONDITIONAL | For every family compatible at every degree, the asserted equivalence for **all** primes p≡1 mod 4 fails at 409: SWZ makes its datum realizable, while complete enumeration gives R(409)=0. It does not exclude an equivalence restricted to the large-prime MS domain. |
| E12–E14 / global verdict | Labels HONEST | Quoted, not newly proved. No new forcing theorem emerges. “Narrowed; no HOT LEAD” survives; the classification is not an impossibility theorem for all future transfers. |

## Lemma A and decisive recomputations

For χ=4/n−1∈(−1,0), h≥2 is impossible. At h=1, r=1 requires n=4m, and r=0 or r≥2 cannot work.
At h=0, r≤2 and r≥6 are impossible; r=3 is ES. For r=5, either four cone orders are 2 (n=4m),
or the last pair is (3,3),(3,4),(3,5), giving n=24,48,120: no odd n.
For r=4, (2,2,a,b) gives a two-term representation, split into three terms. Otherwise set s=Σ₁³1/mᵢ−1.
If s>0, the first triple is (2,3,3),(2,3,4),(2,3,5) and n<4/s; if s=0, n=4m₄ is even;
if s<0, m₁≤3,m₂≤5,m₃≤11 and m₄<−1/s. These are genuinely exhaustive bounds, without a numerical cutoff.
The independent enumeration gives exactly {15,21,23,39,45,47,75,95,105,111,115,117,119,165,273},
and explicitly verifies a three-term representation for each. The s<0 maximum is 6888 at (2,3,7,41).

Reproduction: `scripts/xrev_retro_equiv_astra.py` uses exact rational arithmetic and bounded searches.
Existing `z64_equiv_checks.py`, `z64_equiv_orbifold.py 100000000`, `z64_equiv_signclass.py 20000 300000`,
and `z64_equiv_wsquares.py` were rerun; all four outputs match their committed data byte-for-byte.
That includes 805 Frobenius, 10632 matrix, 1998 cyclic-cover and 53518 critical-matrix checks, all zero failures.
Every shell command used `ulimit -v 4000000` and a timeout ≤1800 seconds. No large census is inferred from a small sample.

## Source verification

Fetched and read the originals, independently of the prior review and the source notes:
- [SWZ 2609.20572v1](https://arxiv.org/pdf/2609.20572v1): abstract, Thm 1.1, Lemma 2.5, Thm 4.8 and introduction; the quotes and odd-p lifting restriction match. This verifies attribution, **not** correctness of the entire unrefereed proof.
- [EKS 1984](https://courses.mai.liu.se/GU/TA1022/Edmonds-Branched%20coverings.pdf): pp. 774,786–787, Prop 5.7. Re-derived its obstruction: transitivity forces the (b+1)-cycle to meet every a-cycle, one twice; the product's two cycle lengths are nonzero modulo a, excluding [a,a(b−1)].
- [Petronio](https://www.numdam.org/item/10.5802/wbln.34.pdf): Prop 1.18 and Thms 3.13–3.14. The two-square family requires d≡1 mod 4; the memo correctly restricts the prime claim.
- [Wang et al. 2512.06545](https://arxiv.org/pdf/2512.06545): the abstract/introduction report all primes <32. I verified the citation, not their full computation.
- [Chenakkod–Faraco–Gupta 2103.01580v4](https://arxiv.org/pdf/2103.01580v4), Cor 9.6: all but one profile have at most one nontrivial cycle. This upgrades Lemma H's stated pure-cycle subcase from V2 to direct verification.
- [AMP 2208.02586v2](https://arxiv.org/pdf/2208.02586v2), Thm 1.1 **page image**; [Beck–Robins](https://arxiv.org/pdf/math/0204037), Thm 3; [Kollár](https://arxiv.org/pdf/0805.0756), (15.5),(16.1); [Lorenzini](https://arxiv.org/pdf/2311.06367), Ex. 6.2(a), Prop 6.3: match the uses above.
- [Agol's MO comment](https://mathoverflow.net/questions/267209#comment660603_267209), fetched through StackExchange's API: the attribution is now correct.
Other §3.1 precedent citations are not independently re-audited here and do not support a new conclusion in this review.

## Required fixes, priority order

1. **Make remaining domains explicit.** In E8 retain the positivity/entry restrictions in the final torus statement:
   γ=[[-1,9],[4,−37]] is Anosov, has upper-right entry 9 and negates (1/4,0), but R(9)=0.
   Restrict E11/Lemma F to odd primes (or p≥5): at p=2, (u,B,C)=(1,1,1), indices (1,2,2) give only TWO branch points.
   Keep E1's generating-pair convention and the prime-only domains of E1/E2/E10 when discussing composite screens.
2. **Repair Hurwitz quantitative and analogy claims.** Three fixed branch values / genus-zero rigidity does not imply O(1) realizations.
   For p=4a+1 prime, the genus-zero passport ([3ᵃ,1ᵃ⁺¹],[2²ᵃ,1],[p]) has Catalan(a) realizations:
   subdivide each edge of a rooted plane full binary tree by a white bivalent vertex and add a white root leaf.
   The unique white leaf recovers the root; the dessins have no automorphisms. Catalan(a) grows without bound along these primes.
   Delete the broad O(1) assertion or restrict it to the specifically justified Euclidean prime family; no general P2 pass follows.
   Replace “ES's square failures” and “ES's exact prime/composite shape”: ES itself has no square obstruction;
   the restricted certificate predicates do, and R(p) even has exceptional primes. The Hurwitz shape is an analogy, not an identity.
3. **Scope the 6888 bound to s<0 sporadic signatures.** “Every r=4 value is ≤6888” is false:
   n=4q−1 and signature (2,2,q,nq) give unbounded odd n (q=2000 gives n=7999).
   Even excluding (2,2,*,*), the s=0 family (2,3,6,m) gives unbounded even n=4m. Correct the script docstring too.
4. **Qualify F3 and blanket inheritance.** W holds at 284 of the 285 supplied composite R-zeros, but fails at 105.
   Thus the W relaxation is blind on most of that screen, not literally all of it. An equivalence inherits a screen only
   inside its proved domain and for its own target; prime-only E1/E2/E10 are not established composite equivalences.

## Falsifier-table audit

F1: the square obstruction belongs to the restricted predicates/sign condition, not ES. Lemma R genuinely supplies blind relaxations.
F2: the numerator-8 orbifold analogue is valid for odd n≥9: independent exhaustive exceptional-signature enumeration gives
{39,45,47,87,93,95,105,165,195,215,225,231,235,237,239}, all admitting three terms; r=5 again gives only even n.
The 8/131 three-term stratum is empty, while lct(x¹⁶y¹²(x³+y⁵))=8/131 by Kollár (15.5), confirming that cell directly.
The AMP locus does not uniformly select C parity. F3: the 105 qualification above is required.
F4: R(409)=0 directly certifies Lemma H's mismatch. Type-I tools still require the absent certificate; they supply no existence proof.
I used the 12/285/14/38 screen files as supplied; I did not rerun their full large-range generation. No verdict here depends on their exact totals.

**ACCEPT-WITH-FIXES.** Retain the ten algebraic/geometric dictionaries and the conditional Lemma H; repair the explicit
scope/count overclaims before propagating this memo. The negative research verdict remains justified. No ES proof results.
