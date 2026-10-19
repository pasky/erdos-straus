# Z45 — interlacing, stability and the arithmetic word forest

## 0. Summary

**Assessment.** Three natural non-counting encodings give three different obstructions, not one blanket impossibility result. MSS signings of the word forest form an interlacing family, but **every member is exactly the same polynomial**: a forest's edge signs are removable by diagonal conjugation. Filtering to certificate edges restores arithmetic sensitivity, but its real-rooted polynomial has a nonzero root precisely when the desired edge already exists. Divisor-residue projection, in contrast, actually destroys real stability: at the hard prime 2521 the only occupied (★) level has rank polynomial `z²+z⁴`; at the squarefree level `4·1097+1=3·7·11·19`, projection sends the stable product `∏(1+z_i)` to `e₁+e₃`, whose diagonal is `4z+4z³`. A third, character-matrix encoding has real-rooted leaves but a non-real-rooted expectation. These are exact obstructions to the displayed constructions, not to all future interlacing arguments. All seven requested primes, six odd squares, and numerator 8 at 131 and 241 are computed exactly. **ES is not solved.**

**Verdict: PARTIAL — the direct signing mechanism is arithmetically blind, and the direct divisor-sector mechanism loses stability; an arithmetic-sensitive growing-level interlacing lift remains unspecified. Promise: 1/5.**

**Assessment / provenance.** Read FRONTIER §§2–4,6–7, the brainstorm index, `polynomial_method.md` including its errata, `invol_windmill_signature.md`, `METAPLECTIC_ES.md`, `SINGLE_P_COUNT.md` §1 and `LOWER_TAIL_ASTRA.md`. Repository-wide `git grep` for interlacing, Heilmann, Lee–Yang, real stability, hyperbolic polynomials, strongly Rayleigh and Pólya-frequency found no prior substantive treatment; the “total positivity” hits concerned an unrelated arithmetic matrix. The graph, divisor dictionary, quadratic sign and theta quotient are prior campaign results. Gauge removal, parity-filter instability and the interlacing criterion are classical elementary facts; the contribution is their precise application and arithmetic counterexamples here, not a claim of external novelty.

## 1. Precise dictionary

### 1.1 Divisor sectors

**Definition.** Let `k` be divisible by 4, `t=kC`, `N=tn+1=∏q_i^{a_i}`, and put

`D_{t,r}(n; z_1,…,z_s) = Σ_{0≤b_i≤a_i, ∏q_i^{b_i}≡r (t)} ∏z_i^{b_i}`.

Write `d_t(n)=D_{t,−1}(n;1,…,1)` and `P_{t,n}(z)=D_{t,−1}(n;z,…,z)`. Here degree is the number of prime factors with multiplicity, not the size of a divisor.

**PROVED (elementary; dictionary already in SINGLE_P_COUNT Lemma 1.1).**

`R_k(n):=#{(u,v,C)≥1 : ku v C−u−v=n}=Σ_{C≤(n+2)/k} d_{kC}(n)`.

Indeed `(tu−1)(tv−1)=tn+1`; a divisor `d≡−1 (t)` recovers `u=(d+1)/t` and `v=(N/d+1)/t`. The bound follows from `t=(n+u+v)/(uv)≤n+2`. For odd n and 4|k there is no diagonal u=v, since `n=tu²−2u` would be even. Thus `R_k` counts twice the corresponding unordered edges. For k=4 this is exactly FRONTIER's R; positivity is sufficient for ES, not equivalent to full ES.

**PROVED.** A triple produces

`k/n = 1/(uvC)+1/(nvC)+1/(nuC)`.

Consequently `R_8(131)=R_8(241)=0` is a necessary control, but a zero of this subfamily alone would not prove the full numerator-8 impossibility.

**Definition / PROVED.** A real polynomial is real stable if it has no zero with all variables in the upper half-plane; allow the zero polynomial as a degenerate output of a stability-preserving operator. In the squarefree case the unrestricted divisor polynomial is the stable product `∏(1+z_i)`. Exact class extraction is the linear coefficient selector

`Π_r(z^b)=1[∏q_i^{b_i}≡r (t)]z^b`.

Thus the proposed transfer requires stability under `Π_{−1}`, or a substitute for that operation. For nonsquarefree N even the unrestricted uniform-divisor polynomial `∏(1+z_i+⋯+z_i^{a_i})` need not be stable: `1+z+z²` is not. Replacing prime powers by labelled copies gives binomial weights and is not uniform divisor counting.

**PROVED (character orthogonality).** For squarefree N,

`D_{t,r}(z)=1/φ(t) Σ_{χ mod t} χ̄(r) ∏_i(1+χ(q_i)z_i)`.

Complex rotations and this signed/complex average are not stability-preserving operations in general. `METAPLECTIC_ES` packages the corresponding divisor-character sums in a theta quotient; it does not supply a different positive operator. Positivity of a real-q theta expression or a zero-free region for a series in q would not, without another theorem, force its individual nth coefficient to be positive.

### 1.2 Forest, cut and spectral detectors

**Definition / PROVED relative to LOWER_TAIL_ASTRA Lemmas 2.1–2.2.** Let `F_n` have vertices `1,…,n+2` and edges `{u,v}`, u<v, when `uv | n+u+v`; put `t=(n+u+v)/(uv)`. It is a forest because the unique possible smaller neighbour of v is `−n mod v`. On unit vertices set `χ_n(v)=(v/n)` and let `H_n` consist of edges with opposite signs. For n≡1 (4), these are exactly the unit-endpoint five-slice certificates. At primes p>3 all edges have unit endpoints; for p≡1 (4), therefore, `H_p≠∅` is precisely the five-slice event. Let `L_{k,n}` instead retain the edges with k|t: `|E(L_{k,n})|=R_k(n)/2`.

**PROVED.** For any forest G on V vertices,

`μ_G(x)=Σ_j (−1)^j m_j(G)x^{V−2j}=det(xI−A_G)`.

In the determinant expansion any permutation cycle of length ≥3 would require a graph cycle. The remaining transpositions are precisely matchings. Therefore all roots are real. Moreover `G≠empty-edge graph ⇔ μ_G≠x^V ⇔ λ_max(A_G)>0`, since `tr A_G²=2|E(G)|` and a nonzero symmetric adjacency matrix has a positive eigenvalue.

**PROVED.** This gives exact root-location formulations of both events:

`R_k(n)>0 ⇔ λ_max(A_{L_{k,n}})>0`,

`ES₅(p) ⇔ λ_max(A_{H_p})>0`.

But the edge filtering is already the exact arithmetic predicate. The equivalence is a dictionary, not a bound.

**PROVED.** There is also a stable determinant detector. For the Laplacian `𝓛_H`, `det(zI+𝓛_H)` has only nonpositive real zeros, for both empty and nonempty H. Its coefficient of `z^{V−1}` is `2|E(H)|`. On the unit-induced forest, `χᵀ𝓛_Fχ=4|E(H)|`. A spectral-gap argument makes this positive only after proving that χ is not constant on every connected component — exactly the missing mixed-component statement. Nonconstancy on the entire disconnected vertex set is insufficient.

## 2. What the existence theorems actually require

**PROVED, published inputs, verified in the linked full text.** Marcus–Spielman–Srivastava, *Interlacing Families I: Bipartite Ramanujan Graphs of All Degrees*, [arXiv:1304.4132v2](https://arxiv.org/html/1304.4132v2), Lemma 4.2 / Theorem 4.4: for an interlacing family there is a member with largest root **at most** that of the sum/expectation. Lemma 4.5: equal-degree positive-leading-coefficient polynomials have a common interlacer iff every convex combination is real-rooted. Their Theorem 3.6 (Godsil–Gutman) identifies the random-signing expectation with μ_G; Theorem 5.2 supplies the interlacing family. Their Theorem 3.1 quotes Heilmann–Lieb, *Theory of monomer-dimer systems*, Commun. Math. Phys. 25 (1972), Theorem 4.2: matching polynomials are real-rooted. Our forest case is proved directly above.

**Assessment.** MSS really does work at one fixed input graph: it does not need an average over p or an estimate for the number of good signings. However, it needs genuine freedom to choose an output and a useful bound on the expected polynomial. Legendre signs at a prescribed p are not free choices. Choosing another coloring, another residue multiset or another p does not give the required certificate at the original p.

**PROVED / literature context.** MSS, *Interlacing Families II*, [arXiv:1306.3969](https://arxiv.org/abs/1306.3969), concerns mixed characteristic polynomials and paving; the abstract was verified, and no additional numbered theorem from it is used here. Borcea–Brändén–Liggett, *Negative dependence and the geometry of polynomials*, JAMS 22 (2009), 521–567, [arXiv:0707.2340](https://arxiv.org/abs/0707.2340), develops strongly Rayleigh measures via stable generating polynomials; abstract verified. This does not license conditioning on an arbitrary multiplicative residue event. The counterexample in §3.2 explicitly forbids that closure claim.

**Assessment (Lee–Yang context, not an invoked theorem).** Lee–Yang circle theorems concern ferromagnetic Ising partition functions in external-field variables (classical statement recalled from memory). Zero location of a partition function summing over freely chosen spins is not a certificate concerning one prescribed spin assignment. The exact forest calculation in §3.4 is sufficient here and needs no Lee–Yang theorem. Likewise no general hyperbolicity or total-positivity theorem is assumed: the proposed real-stable rank sequence already fails the elementary real-rootedness test.

## 3. Attempts and exact results

### 3.1 The forest signing family exists — but is constant

**Lemma (PROVED; elementary gauge removal).** For every signing `s:E(F)→{±1}` of a forest there is a diagonal matrix `D_s` with entries ±1 such that `A_s=D_s A_F D_s`. Choose a root sign in each tree and recursively put `D_s(v)=s(uv)D_s(u)` along parent edges. Hence

`det(xI−A_s)=μ_F(x)` for every s.

**PROVED consequence.** Every node of the tree of partial sign assignments has the **same normalized expected polynomial** μ_F. A common interlacer exists at every node, trivially. In particular, the arithmetic signing `s(uv)=χ(u)χ(v)` gives `A_s=D_χ A_F D_χ`. This last conjugacy holds even on a graph with cycles: endpoint-product signs are always a gauge. So merely adding edges or cycles while retaining endpoint-product signs would not repair this encoding.

**Assessment.** The property that breaks is **arithmetic separation**, not real-rootedness or common interlacing. The spectrum cannot tell a negative edge from a positive edge. Replacing F by H or L_k retains real-rootedness, but makes the desired nonzero eigenvalue equivalent to the original B2 event. MSS's usual upper bound on the largest root does not supply the needed strict positive lower bound for H.

### 3.2 Exact residue projection is not stability-preserving

**Lemma (PROVED).** Let four squarefree prime factors all represent −1 in a group of order two, with total product +1. Their −1 sector is

`O₄(z_1,z_2,z_3,z_4)=e₁(z)+e₃(z)`.

It is not real stable: `O₄(i,i,i,i)=4i+4i³=0`. The input `∏(1+z_i)` is stable. Thus even a quadratic parity filter, much less arbitrary class extraction, is not a general stability preserver. The diagonal coefficient sequence `(0,4,0,4)` is not log-concave (`0²<4·4`) and therefore cannot be Pólya-frequency/total-positive in the usual coefficient sense.

**CERTIFIED, exact arithmetic instance.** `p=1097` is prime and

`4p+1=4389=3·7·11·19`.

All four factors are 3 modulo 4. Hence this exact obstruction occurs inside the ES family, not only in an abstract residue model. Its target count is 8, so instability does **not** mean arithmetic failure: it means the proposed theorem is inapplicable even to a successful slice.

**CERTIFIED, requested hard-prime instance.** At p=2521 the unique occupied (★) level is t=44:

`44p+1=110925=3²·5²·17·29`, with target divisors `{87,1275}`.

The full sector polynomial is `z_3 z_29 + z_3 z_5² z_17`, and its diagonal is `z²+z⁴`, with roots 0,0,i,−i. This non-real-rootedness is exact. By contrast at p=3361 the sole occupied level is t=20:

`20p+1=67221=3²·7·11·97`, target divisors `{99,679}`, rank polynomial `z²+z³`.

Thus some thin sectors happen to have a stable diagonal; there is no blanket assertion that every sector fails, nor that a real-rooted diagonal proves multivariate stability.

### 3.3 Divisor-choice interlacing: trivial success versus genuine failure

**PROVED.** Choose a divisor d of N uniformly and let `b_d=1[d≡−1 (t)]`. The degree-one polynomials

`f_d(x)=x−(1−b_d)`

form an interlacing family along any tree revealing prime exponents: every conditional expectation is linear. Its root at the top is

`1−d_t(n)/τ(N)`.

MSS's “root <1” criterion gives a good divisor iff `d_t(n)>0`. This avoids a main-term/error comparison only by placing the exact count in the expected root. It is a valid, tautological interlacing construction.

**PROVED.** A less tautological arithmetic matrix choice is `B_d=χ₄(d)I₂`, where `χ₄(d)=1` for d≡1 (4), −1 for d≡3 (4). Every leaf characteristic polynomial `(x−χ₄(d))²` is real-rooted. If both signs occur, their two polynomials have no common interlacer: the sole possible interlacer root would need to equal both 1 and −1. For uniform divisors,

`E_d det(xI−B_d)=x²−2a x+1`, `a=τ(N)^{-1}Σ_{d|N}χ₄(d)`.

Whenever `|a|<1` the discriminant is negative. Such a leaf family cannot be an MSS interlacing family under *any* prime-factor reveal tree, because its root expectation is already not real-rooted. Real-rooted leaves alone are not enough.

**CERTIFIED examples.** At (p,t)=(1097,4), a=0 and the expectation is `x²+1`. At (2521,44), a=1/3 and it is `x²−(2/3)x+1`; at (3361,20), a=0 and it is `x²+1`. At t=4 for each of the seven requested primes, there are no divisors 3 modulo 4, so this particular family is constant `(x−1)²` instead — another illustration of “degenerate or noninterlacing,” not a root bound forcing existence. The first degree-one expectation is `x−17/18` at (2521,44), `x−11/12` at (3361,20), and `x−3/4` at (193,8). At every unoccupied level it is `x−1`, including every k-multiple level at the R_k=0 controls.

### 3.4 Partition functions: what gets averaged away

**PROVED.** For a forest F with c components and E edges, summing over all vertex signs gives

`Z_F(a)=Σ_{σ∈{±1}^V} a^{#{uv:σ_u≠σ_v}} = 2^c(1+a)^E`.

Choose one root sign per component; the E edge disagreements are then independent binary choices. This partition function is real-rooted, and the normalized expectation is `((1+a)/2)^E`. For the *pinned arithmetic coloring* the partition function is just `a^{|E(H)|}`. Extracting that one assignment from the all-spin sum discards precisely the freedom on which the formula rests. The same all-spin expression exists at every odd square, where the arithmetic assignment has no disagreeing unit edge.

**PROVED.** Replacing matchings by independent sets is not an automatic repair. The claw `K_{1,3}` has independence polynomial `1+4z+3z²+z³`, cubic discriminant −31, hence is not real-rooted. `F_409` contains an induced claw with center 1 and leaves 2,5,10. This refutes the generic assertion “forest independence polynomials are real-rooted”; it does not assert that this induced subgraph alone determines the zeros of the univariate independence polynomial of the whole F_409.

### 3.5 Complete exact computations at the requested inputs

**CERTIFIED.** Script: `scripts/z45_interlacing_stable_check.py`; exact output: `data/z45_interlacing_stable/results.json`. There are 16 fixtures. Each complete edge set is constructed independently by the unique-parent remainder rule and by enumeration of divisors of n+u. Matching coefficients are computed by tree dynamic programming and checked against exact adjacency characteristic polynomials, including a nontrivial signing, component by component. The largest matrix is 28×28; no dense `(n+2)×(n+2)` matrix is allocated. Target divisors are independently enumerated at all occupied levels and compared to edge counts. Line certificates are checked by exact rational arithmetic. Run:

`ulimit -v 2000000; timeout 150 uv run python scripts/z45_interlacing_stable_check.py`

**CERTIFIED table.** `b=|E(H_n)|` uses unit vertices and Jacobi signs. At 131 (n≡3 mod4) it is only a sign diagnostic, **not** the five-slice equivalence. At numerator 8 neither row's b is an 8/n certificate. `R_k` is the t≡0 (k) subfamily.

| k | n | edges of F | b | R_k | all occupied t, with P_{t,n}(z) |
|---|---:|---:|---:|---:|---|
| 4 | 409 | 19 | 4 | 0 | none |
| 4 | 577 | 22 | 9 | 0 | none |
| 4 | 3361 | 23 | 4 | 2 | 20: z²+z³ |
| 4 | 193 | 14 | 5 | 4 | 8: z+z²; 20: z²+z³ |
| 4 | 2521 | 18 | 2 | 2 | 44: z²+z⁴ |
| 4 | 5569 | 27 | 8 | 0 | none |
| 4 | 9601 | 26 | 4 | 0 | none |
| 4 | 9 | 5 | 0 | 0 | none |
| 4 | 25 | 7 | 0 | 0 | none |
| 4 | 49 | 11 | 0 | 0 | none |
| 4 | 169 | 16 | 0 | 0 | none |
| 4 | 529 | 19 | 0 | 0 | none |
| 4 | 1089 | 15 | 0 | 0 | none |
| 4 | 1097 | 30 | 16 | 12 | 4: 4z+4z³; 92: z+z³; 184: z+z² |
| 8 | 131 | 21 | 7 | 0 | none |
| 8 | 241 | 15 | 6 | 0 | none |

**CERTIFIED: explicit expected signing polynomials.** Write `y=x²` and `E_s det(xI−A_s)=x^a Q(y)` on all n+2 vertices. These formulas also describe every conditional signing expectation. They are not just numerical root approximations.

| n | a | Q(y) |
|---:|---:|---|
| 409 | 395 | `(y−2)²(y²−3y+1)(y⁴−12y³+35y²−25y+5)` |
| 577 | 563 | `(y−2)²(y²−3y+1)(y⁴−15y³+72y²−126y+70)` |
| 3361 | 3351 | `(y−4)(y−2)(y⁴−17y³+90y²−184y+126)` |
| 193 | 185 | `(y−1)(y−2)(y³−11y²+21y−10)` |
| 2521 | 2511 | `(y−1)(y−2)(y⁴−15y³+66y²−100y+44)` |
| 5569 | 5553 | `(y−1)(y−3)(y−2)⁴(y³−15y²+62y−66)` |
| 9601 | 9583 | `(y−1)⁴(y²−3y+1)(y⁴−19y³+90y²−142y+64)` |
| 9 | 5 | `(y−1)(y²−4y+2)` |
| 25 | 21 | `y³−7y²+11y−4` |
| 49 | 43 | `y⁴−11y³+36y²−42y+14` |
| 169 | 161 | `(y−1)(y⁴−15y³+66y²−100y+44)` |
| 529 | 521 | `(y−2)²(y³−15y²+61y−60)` |
| 1089 | 1079 | `(y−1)²(y²−8y+6)(y²−5y+3)` |
| 1097 | 1083 | `(y−1)²(y−2)(y⁵−26y⁴+220y³−729y²+870y−324)` |
| 131 | 119 | `(y−1)(y²−4y+2)(y⁴−16y³+53y²−50y+14)` |
| 241 | 233 | `(y−2)(y⁴−13y³+50y²−68y+28)` |

**CERTIFIED: arithmetic-filtered expected polynomials.** These are again identical for all signings of the filtered forest. For the seven hard primes in the order above:

| n | μ_H(x), with y=x² |
|---:|---|
| 409 | `x^405 (y−1)(y²−3y+1)` |
| 577 | `x^571 (y−4)(y−1)(y−2)²` |
| 3361 | `x^3359 (y−2)²` |
| 193 | `x^191 (y−4)(y−1)` |
| 2521 | `x^2521 (y−2)` |
| 5569 | `x^5563 (y−1)(y−3)(y−2)²` |
| 9601 | `x^9597 (y−1)²(y−2)` |

At every tested square, `μ_H=x^{n+2}`. For the (★) line, `μ_{L_4}=x^{3361}(y−1)` at 3361, `x^{193}(y−2)` at 193, `x^{2521}(y−1)` at 2521; it is `x^{n+2}` at the other four hard primes and all squares. For numerator 8, `μ_{L_8}=x^133` at 131 and `x^243` at 241. The larger two-line test `8|t or 8|u or 8|v` also has no edges at either input. No ad hoc “8 divides tu−1” predicate is interpreted as an established certificate.

**Assessment.** The requested near-square stress is genuinely represented: 577=24²+1, 193=14²−3, 3361=58²−3 and 9601=98²−3. The mechanism is neither rescued nor uniquely broken there: gauge removal is universal, while the exact filtered occupancy distinguishes them. These fixtures do not establish any statistical near-square law.

## 4. All 17 FRONTIER screening lines

**Assessment.** PASS means that the *honest formulation* survives that screen, not that a proof exists. The unfiltered spectral shortcut has additional failures noted explicitly.

| # | Result | Reason |
|---:|---|---|
| 1 | PASS for detector; FAIL for unfiltered shortcut | On odd squares all unit χ-values are +1, H is empty, and D_{t,−1}=0 for 4|t. By contrast μ_F remains nontrivial and interlacing survives unchanged, so those properties alone cannot force a certificate. |
| 2 | PASS for detector; FAIL for blind shortcut | R_8 and the actual two-line 8-filter vanish at 131,241. The χ-cut is specifically a 4/n interpretation for n≡1 mod4; applying it to 8/241 would be false. |
| 3 | PASS with scope restriction | No numerator-uniform transport or recombination law is proposed. The underlying forest/signing theorem is uniform and therefore cannot be the missing 4-specific input. |
| 4 | **FAIL — central open implication** | The modulus is t=kC. Π_{−1} performs the tied-class test, loses stability, and has no arithmetic-sensitive replacement with a useful expected-root bound. Filtering H or L only hides the same test in a matrix entry. |
| 5 | PASS | n/p stays fixed. The only averages are over auxiliary edge signs, freely chosen spins or divisors of one fixed N; none is over p. The problem with these averages is loss of the prescribed arithmetic data, not an average-over-primes leak. |
| 6 | PASS / N.A. for error terms | No power-size main term and no main-term/error estimate is claimed. The trivial linear expectation contains the exact count, not a wrong 1/m prime-density model. |
| 7 | PASS | Only strict nonemptiness is sought; no false two-sided polylogarithmic error estimate appears. |
| 8 | PASS in scope | The complete forest and all occupied levels grow with n. This is not a fixed finite menu. Arbitrarily restricting to a bounded set of levels would restore B1. |
| 9 | **FAIL as a forcing step** | Knowing the quadratic signs is insufficient without proving an actual class-hit edge. Even parity conditioning destroys real stability, and the character-matrix expected polynomial can fail real-rootedness. No class-forcing input is supplied. |
| 10 | PASS | No collision or pooling of large factors across different shifts is used. |
| 11 | N.A. | All words and divisors are positive. No signed-to-positive reflection is attempted. Matrix edge signs are not signed ES denominators. |
| 12 | N.A. | No relaxed certificate is transported back into ES. |
| 13 | PASS in scope / no gain | No BM/local-global implication is invoked. A BM/genus restriction would still require Π_{−1} inside its allowed coset; it would not repair the displayed failure. |
| 14 | PASS as an audit | All seven requested primes are computed. Any claim “R(p)>0 for every prime” is explicitly rejected by 409,577,5569,9601. The five-slice forest succeeds at all seven. |
| 15 | PASS as a finite stress test | Explicit near-square fixtures above and six odd-square controls. No extrapolation from them is asserted. |
| 16 | PASS | No factorization available only under p=φ(u) is transferred to general p. 1097 is a counterexample to a closure assertion, not an infinite-family proof. |
| 17 | N.A. / unresolved if used for forcing | No coset-covering certificate is claimed. The computations use all prime factors. A future factor-based root bound must control large factors' actual classes; nothing here does that. |

## 5. “New theory”: residue-sector lifts, not scalar stability after projection

### 5.1 A precise object and a solved toy case

**Definition.** For a finite abelian group G and factor residues g_i, retain the group-algebra-valued polynomial

`𝒟(z)=∏_i(1+z_i[g_i])=Σ_{r∈G} D_r(z)[r]`.

A factor reveal obeys the exact positive vector recurrence

`D_r^{(j)}=D_r^{(j−1)}+z_j D_{r g_j^{-1}}^{(j−1)}`.

For prime powers replace the two-term recurrence by `Σ_{b=0}^{a_j} z_j^b D_{r g_j^{-b}}^{(j−1)}`. This is simply the divisor dynamic program in group-algebra language; no novelty claim is made for the object. The possible research question is a root/positivity invariant of the *whole sector vector* that survives the recurrence while retaining information about one sector's support.

**PROVED toy classification.** In G=C₂, suppose r factors have residue −1 and all others residue +1. The negative-sector polynomial is

`O_r(z)·∏_{g_i=+1}(1+z_i)`,

where `O_r=Σ_{|S| odd} z^S`. It is zero for r=0, real stable for r=1,2, and not real stable for any r≥3. Proof: `O₁=z₁`, `O₂=z₁+z₂`; for r≥3 specialize all but three active variables to zero. The remaining diagonal is `3z+z³`, with an upper-half-plane zero. Real specialization preserves stability or gives zero (MSS §6, Hurwitz argument), so the original cannot be stable. Under the total-product constraint N≡1 in C₂, r is even: the only nonzero stable case is r=2. At r=4 the explicit arithmetic test is 1097. The r=2 case forces a target divisor for the elementary reason that either negative factor itself hits it; no ES-strength inference is gained.

**PROVED / Assessment.** The diagonal identity

`O_r(z,…,z)=((1+z)^r−(1−z)^r)/2`

shows why a Lee–Yang-like alternative geometry might appear: its finite nonzero roots are purely imaginary (`z=i tan(πj/r)`, excluding the pole). This is not real stability and permits gaps in the coefficient sequence. It also does not prove r>0. Zero geometry of a nonzero sector cannot by itself establish that the sector was nonzero in the first place.

### 5.2 First result a useful theory would need

**CONJECTURE / research specification, not a claimed standard conjecture.** Seek a vector-valued or matrix-valued lift of the growing collection `𝒟_{t,p}`, retaining the *actual* residue labels, with: (i) an interlacing selection tree or another proved root comparison; (ii) a certificate implication from a root crossing; (iii) a bound proving that crossing at each sufficiently large prime using arithmetic information short of the target count itself; (iv) degeneracy at odd squares and the correct numerator-8 controls. If it only targets (★), the prime threshold must exclude its known failures; if it targets all five slices, its arithmetic component must use their 4-specific χ interpretation.

**Assessment.** Requirement (iii) is the exact missing implication, not something established by naming a lift. The naive conjecture “each residue sector is stable” is already false. The toy C₂ classification leaves no evidence for a scalar stability theory broad enough to contain the actual sectors. A useful replacement would have to allow unstable sectors, or assemble different levels before any projection. No such cross-level identity, common interlacer or arithmetic root bound was found. Gauge conjugacy shows that merely assembling endpoint-product signings, even with extra cycles, is insufficient.

## 6. Verdict and next steps

**Assessment — PARTIAL, promise 1/5.** The deliverable is a scoped obstruction map:

- Forest signing: real-rootedness and common interlacing both hold, but arithmetic separation fails identically by gauge conjugacy.
- Certificate-filtered matching/Laplacian polynomial: real-rootedness holds even at failure inputs; a strict nonzero-root assertion is the original occupancy problem.
- Exact divisor-residue projection: stability fails, with an actual requested hard-prime example and a squarefree prime example.
- Character-matrix divisor family: leaf real-rootedness holds but the expectation is non-real-rooted, hence no interlacing family of that form exists.
- Free-spin partition function: its zero statement averages over the object whose arithmetic value is prescribed; pinning gives back the exact edge count.

**Assessment — exact open implication.** Supply an arithmetic-sensitive expected polynomial with a proved root crossing at a fixed p, without evaluating/assuming the target divisor sector's nonemptiness. The present constructions supply no such polynomial. This is B2 in root language, not an escape from B2 and not a proof that all non-counting methods must fail.

**Assessment — concrete next steps.** Before allocating another broad search, require an explicit proposed sector-vector invariant and test it on `(2521,44)`, `(1097,4)`, the odd squares and `(k,n)=(8,241)`. If it survives, check common interlacing at every factor-reveal node, not just real-rooted leaves or one averaged polynomial. A tractable stand-alone problem is to classify stable class-sector polynomials for small finite groups and squarefree inputs; that would refine the obstruction taxonomy, not by itself advance ES. Do not rerun the already-dead generic forest-signing or arbitrary-conditioning arguments.
