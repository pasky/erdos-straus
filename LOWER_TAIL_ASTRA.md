# LOWER_TAIL_ASTRA — O275: single-integer lower-tail attack

**Status: construction phase. ES is not solved.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE; interpretations are Assessment. Work is confined to `side-agent/lower-tail-astra`.

## 0. Reading and attack contract

Read STATUS.md's current headlines, DISCOVERIES.md (J)84–104, BM_CORRECTED_COUNT, SINGLE_P_COUNT, METAPLECTIC_ES, SYNTHESIS_SPARKS9, TWO_POWER_LADDER, CLASS_FORCING, B2_ACROSS_FIELDS, both 20261018 advisory-board memos, CONDITIONAL_ES, DISPROOF_AVENUES.

The unconditional BM main term is not the missing ingredient. Nor does a positive mean prove occupancy at one prime. I will not re-propose the boards' killed counting, bounded-reciprocity, norm-trap, or fixed-menu descent mechanisms.

### Construction queue (Assessment, not claims)

1. **Euclidean remainder dynamics at one p.** Enlarge the length-three word set to a power-size set of residue pairs; seek a primality-sensitive descent or collision whose boundary contains a good word. The enlargement must not silently count multiples of p, and the final map need not have bounded fibres. This targets M1b/M5 rather than a main-term driver (B3).
2. **Local-to-global failure rigidity.** If all positive word targets fail, derive an invariant of the *actual* division table, rather than prescribing independent factorisations at finitely many levels. The board left an inverse-theorem gate open; no claimed result is imported from that gate.
3. **Canonical real-quadratic data.** Use the full reduction cycle, not a finite list of polynomial recipes. JOINT_BUDGET Prop 4.2 only proves the resulting norm windows are not Jacobi-forced; it does not exclude a global cycle argument.

Each attempt must identify its exact missing implication, distinguish the two-line union from full ES, and retain odd-square and numerator-8 controls. No all-prime claim will be reported without exhaustive checks through 10^6 and independent certificate reconstructions.

## 1. Starting object

Use positive words `tuv − u − v = n`. Their two-line union for numerator k is exactly the presence of a coordinate divisible by k (SYNTHESIS_SPARKS9 Cor 1.2). The full five-slice condition for n ≡ 1 (4) adds `4 | tu−1` or `4 | tv−1` and is the negative Jacobi-sign fibre (DEDEKIND_ES Thm 4.5).

A new mechanism must force a good word, not merely a nonempty word set, a nonempty genus fibre, or reachability inside an already nonempty good fibre.

## 2. The arithmetic word forest

**Definition.** For n ≥ 1 let F_n have vertex set {1,…,n+2}. Distinct u,v are joined when `uv | n+u+v`. Label the edge by `t=(n+u+v)/(uv)`. Loops are deliberately omitted. This graph is an exact encoding of unordered positive words, except the diagonal words.

**Lemma 2.1 (PROVED, elementary).** F_n is a forest. For v>1 its only possible smaller neighbour is `r_v = (−n mod v)` in {0,…,v−1}. It is an actual neighbour precisely when r_v>0 and `v r_v | n+v+r_v`. If gcd(v,n)=1, the second condition is equivalent to `r_v | n+v`.

*Proof.* Any neighbour u<v satisfies u ≡ −n (mod v), hence u=r_v. A cycle's largest vertex would have two smaller neighbours, impossible. When gcd(v,n)=1, gcd(v,r_v)=1, and v already divides n+v+r_v; the product divisibility is therefore equivalent to r_v dividing n+v. ∎

The vertex bound is complete: if 2≤u≤v, then `n≥uv−u−v`, so `v≤(n+u)/(u−1)≤n+2`; if u=1 then t≥2 and v≤n+1. A diagonal word has u=v dividing n. At prime p>3 the only diagonal word is (t,u,v)=(p+2,1,1), whose sign is positive. Thus no good prime word is lost.

**Lemma 2.2 (PROVED).** Restrict to vertices coprime to odd n and colour v by `χ_n(v)=(v/n)`. On an edge put A=tu−1. Then

`(A/n) = χ_n(u)χ_n(v)`.

Consequently, for n≡1 (4), a bichromatic edge is exactly a five-slice certificate (the five-slice sign theorem is DEDEKIND_ES Thm 4.5). Along any tree path v₀,…,v_h, the product of edge signs is `χ_n(v₀)χ_n(v_h)`.

*Proof.* `Av=n+u`, so A≡uv⁻¹ (mod n); the Jacobi identity follows. The path product telescopes. ∎

**Construction target (not proved).** A non-residue in the component rooted at 1 forces a bichromatic edge without estimating its count. More generally, any independently forced pair of opposite-coloured vertices in one component suffices. This is weaker than demanding expansion, but stronger than mere existence of a good edge somewhere. We will test it before using it as a conjecture.

**Scope / barrier screen.** A forest is not itself an existence argument. T1 holds identically because all unit vertices at odd squares have colour +1. The forest exists for every n and every numerator; only the five-slice interpretation is 4-specific. In particular the same sign criterion must NOT be used for 8/n. Neither B3 nor the fixed-menu involution theorem excludes a growing rooted-component argument, but a component must actually cross colours. There is no nontrivial cycle on which to apply an odd-cycle or holonomy contradiction.

## 3. A complete sterile component, and the fixed-root obstruction

The root-1 construction is false, not merely unproved. In the complete census it fails first at p=409, and at 285 primes p≡1 (4) up to 10^6. Allowing the root 2 adds nothing: {1,2} is an edge for every odd n.

**Theorem 3.1 (PROVED implication; infinite family CONDITIONAL on Dickson).** Suppose k≥1 and all four numbers

`p=24k+1, r=12k+1, s=8k+1, w=6k+1`

are prime. The entire component of 1 in F_p has exactly the seven edges

`{1,2}, {1,r}, {1,2r}, {2,3}, {2,s}, {2,3s}, {3,2w}`.

Every vertex in this component is a quadratic residue modulo p. Therefore this component contains no five-slice ES certificate, even if its exploration is unrestricted.

*Proof.* At vertex 1 the neighbours are the nontrivial divisors of p+1=2r, namely 2,r,2r. At vertex 2 they are the odd divisors of p+2=3s, namely 1,3,s,3s. At vertex 3, a neighbour must divide p+3=4w and be 2 mod 3; since w≡1 (3), the only such divisors are 2 and 2w.

The five remaining vertices are leaves. For r, a neighbour divides 3r−1 and is 1 mod r; the candidates other than 1 are r+1 and 2r+1, which fail for r>3. For s, a neighbour divides 4s−2 and is 2 mod s; the candidates s+2,2s+2,3s+2 fail for s>8 (their divisibility would require, respectively, s+2|10, 2s+2|6, or s=4). For v=2w, a neighbour divides 3v−3 and is 3 mod v; candidates v+3 and 2v+3 fail for v>9. Finally 2r=p+1 and 3s=p+2 have only neighbours 1 and 2 by the global size bound. The hypotheses give r≥13,s≥9,2w≥14.

Since p≡1 (24), both 2 and 3 are quadratic residues. Modulo p, r=1/2, s=2/3, 2w=3/2, 2r=1, and 3s=2, so all eight vertices are residues. ∎

All four linear forms take the value 1 at k=0. Their product therefore has no fixed prime divisor; they are distinct primitive positive linear forms. Dickson gives infinitely many such k. Actual examples are p=12721,16921,19441,24481,49681,61561,104161,229321. This proves failure of the rooted construction, NOT failure of ES: each example has bichromatic edges elsewhere.

**Theorem 3.2 (fixed finite roots fail; CONDITIONAL on Dickson).** For every integer H≥3 there are infinitely many primes p≡1 (24) such that every component meeting {1,…,H} is monochromatic. In particular, no fixed finite set of roots, even with *unbounded component exploration*, forces a five-slice certificate.

*Proof.* Choose M divisible by 24 and by every i(i+1), 1≤i≤H. Apply Dickson to the H+1 forms

`p=1+Mk, L_i=1+(M/(i+1))k, 1≤i≤H`.

They are admissible because they all equal 1 at k=0. Take k large enough that each prime L_i>H+1. Then p+i=(i+1)L_i and L_i≡1 (mod i). Every divisor v of p+i is d or dL_i with d|i+1, and hence v≡d (mod i). For i≥4, no divisor d|i+1 is −1 mod i: the only candidate is i−1, and i−1|i+1 would imply i−1|2. Thus vertices 4,…,H are isolated. The component of 1 (also containing 2,3) is exactly that of Theorem 3.1, with k there replaced by Mk/24, and is monochromatic. ∎

**Scope / novelty (Assessment).** This uses the campaign's familiar n=1-shadow/Dickson mechanism, not a new prime theorem. The extra conclusion is graph-theoretic closure: all branches from the chosen roots are blocked, not just a prescribed finite set of slices or a prescribed exploration depth. It excludes this particular adaptive-root strategy; growing or p-dependent roots remain open.

## 4. Paths: Fibonacci growth, but no depth-forced sign change

**Lemma 4.1 (PROVED).** On any increasing path v₀<⋯<v_h, for 1≤i<h there is a positive integer a_i with

`v_{i+1}=a_i v_i+v_{i−1}`.

Thus path vertices grow at least as Fibonacci numbers and the depth is O(log n). The ratios are ordinary continued-fraction recurrences.

*Proof.* Both neighbours of v_i are −n mod v_i, so v_i divides v_{i+1}−v_{i−1}; positivity gives a_i≥1. ∎

**Proposition 4.2 (PROVED, relative to Dirichlet).** For every h there are infinitely many primes p≡1 (8) whose component of 1 contains an increasing path of length at least h consisting entirely of quadratic residues modulo p. Consequently long paths alone do not force a good edge on that path.

*Proof.* Start v₀=1,v₁=2, and choose an odd prime v₂≡1 (8). Inductively choose a new prime v_{i+1}>v_i with v_{i+1}≡v_{i−1} (mod v_i) and v_{i+1}≡1 (8), using Dirichlet. All odd vertices are distinct primes. Prescribe p≡1 (8) and p≡−v_{i−1} (mod v_i) at each odd vertex. Adjacent prescriptions agree because v_{i+1}≡v_{i−1} (mod v_i). CRT and Dirichlet give infinitely many prime p in the resulting unit class. At each edge both vertex divisibilities hold; their coprimality gives the word condition. Take p sufficiently large that all vertices lie in the defining range.

For v₂, reciprocity gives (v₂/p)=(−2/v₂)=1. For i≥3, since v_i,v_{i−1}≡1 (8),

`(v_i/p)=(−v_{i−1}/v_i)=(v_i/v_{i−1})=(v_{i−2}/v_{i−1})=1`

by induction and the previous vertex's prescribed sign; v₀,v₁ are residues as well. ∎

This is not an assertion that the entire component is monochromatic: other branches may contain certificates. It rules out only the proposed path-depth forcing.

## 5. Adaptive repair: use the least quadratic non-residue

The fixed-root obstruction uses p≡1 modulo small integers, so its least non-residue moves beyond the frozen roots. A genuine repair is therefore to root at the *actual least non-residue* ℓ(p), rather than at a fixed integer.

If ℓ(p) has a smaller neighbour, that edge is automatically bichromatic, since every positive integer below ℓ(p) is a residue. This criterion succeeds at 38,097 of the 39,175 primes p≡1 (4) up to 10^6. Allowing its *whole component*, including branches not through ℓ(p), still fails at 769 primes, beginning 1201,2521,3361,5569,7561,9769. This is a different failure set from the root-1 set.

**Theorem 5.1 (PROVED implication; infinitely many such primes CONDITIONAL on Dickson for two forms).** If

`p=2521+9240a, q=211+770a=(p+11)/12`

are both prime, with a≥0, then ℓ(p)=11 and vertex 11 is isolated in F_p. Thus even unrestricted exploration from the least quadratic non-residue need not yield a certificate.

*Proof.* p≡1 (24), p≡1 (5), p≡1 (7), and p≡2 (11). Hence 2,3,5,7 are residues and 11 is a non-residue; multiplicativity gives ℓ(p)=11. Any neighbour v of 11 must divide p+11=12q and satisfy v≡−p≡9 (11). But q≡2 (11), so the possible divisor residues are

`{1,2,3,4,6,12}·{1,2} mod 11 = {1,2,3,4,6,8}`,

which misses 9. The two linear forms are admissible: at primes dividing 9240=2³·3·5·7·11, the first form is a nonzero constant and the second is either a nonzero constant or excludes at most one class (at 3); at every other prime, the two forms exclude at most two classes and that prime exceeds 2. Dickson supplies infinitely many simultaneous prime values. ∎

**Assessment.** The repair violates the fixed-root hypothesis but is still blocked by an explicit actual-factorisation pattern. This does not rule out growing sets of non-residues, other canonical data, or mixed-component existence somewhere in F_p. It is not a proof against Pell/class-group methods.

## 6. Verification checkpoint

**EVIDENCE / exact finite checks.** `scripts/z43_astra_forest.c 1000000` constructs all unordered non-diagonal words by AP enumeration and independently reconstructs the same edge set by SPF divisor enumeration at every odd prime ≤10^6 and all 499 odd squares 9,…,999². Both methods agree exactly (edge membership and cardinality).

- 78,497 odd primes; 39,175 primes p≡1 (4).
- 3,028,437 edges at the latter primes; 1,964,805 have negative sign; no five-slice failures (reproduces known results, not new evidence for ES).
- Root-1 failures: 285; first 16 are 409,1201,5569,8521,8641,9649,12289,12721,12841,15241,16921,19441,23761,23929,24481,27241.
- Maximum depth over selected inputs is 7 (first attained at 7867); largest least root of a mixed-colour component is 17 (first attained at 196561).
- Every edge at odd squares fails the five-slice test; all word edges at 131 and 241 fail the numerator-8 five-slice test.

A third implementation, `scripts/z43_astra_check.py`, compares direct residue-parent enumeration and divisor enumeration for every odd n≤2000 (24,389 edges), and checks 21,135 reconstructed unit-fraction certificates in exact rational arithmetic. It independently checks all 499 odd squares (17,372 edges), and complete components at eight actual four-form prime fixtures. No mismatch.
