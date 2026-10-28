# FOREST_DEEP_ASTRA — cut edges in the pruned remainder tree

**Status: PARTIAL. ES remains open.** This is a single-target attempt to force a bichromatic component of the word forest, not a survey of ES methods. The direct reciprocity converse is proved below. The attempted forcing mechanism is developed through the full remainder tree, its quotient blocks, and its first split divisor fibre. It does **not** prove certificate existence at every sufficiently large prime, even assuming GRH or OAI-003.

**Assessment: promise 1/5 for this forcing route.** The useful output is a self-contained converse, an exact description of what remainder descent loses, and a Dickson-conditional obstruction to the most promising greedy repair. The negative results have explicit scopes; they do not rule out a global forcing theorem.

Labels: **PROVED** means a complete argument here, sometimes relative to the stated classical input; **CONDITIONAL** names its additional hypothesis; **CERTIFIED** means an exact finite computation checked by distinct algorithms; **EVIDENCE** is an interpretation of those computations; **CONJECTURE** means unproved. All results are internal and unrefereed.

## 1. Target, scope, and what was already known

Let p ≡ 1 (mod 4) be prime, χ(a) = (a/p), and join distinct positive integers u < v when

    p = tuv − u − v,             t ∈ ℕ.

The resulting forest F_p has all its non-isolated vertices in [1,p+2]. Call an edge good when a slot in

    {t, u, v, tu−1, tv−1}

is divisible by 4. Write H₄(p) for the least larger endpoint of a good edge, with value ∞ if there is none. Write ES₅ for existence of such an edge. Only **ES₅ ⇒ ES** is used; the converse ES ⇒ ES₅ is not established.

**Prior-result audit.** The requested converse is not wholly unproved in the supplied repository: `DEDEKIND_ES.md`, Theorem 4.5, proves it for interior HJ words using Dedekind sums and a finite mod-8 table; `LOWER_TAIL_ASTRA.md` and `FOREST_H4.md` cite the extension to forest edges. Section 2 gives a direct quadratic-reciprocity proof covering every edge, without Dedekind sums or a computer-assisted table. It is an alternative proof, not a claim to discover the equivalence.

Read completely: the z48 `CONTEXT.md`, `FRONTIER.md`, `BREADTH_Z45.md`, the PR-B main note and both supplements, `OAI_DUMP_IMPACT.md`, and the five task-specific notes. The other independent attack was not consulted or coordinated with.

**Assessment: attack chosen.** Instead of expanding the component of 1, retain *every* negative remainder pointer first. This gives a connected tree with many forced colour changes. Then ask whether a colour change must survive the exact divisibility pruning. The successive attempted repairs were:

1. use the abundance of virtual cuts;
2. descend through their quotient blocks;
3. choose the first split fibre, which is guaranteed below the least nonresidue;
4. continue through successive split fibres;
5. seek a component-count or colour-balance contradiction if none survives.

The same target is maintained throughout. Each loss is made explicit below.

## 2. Direct reciprocity proof of certificate ⇔ bichromatic edge

### Theorem 2.1 — the complete elementary sign law (PROVED)

Let n ≡ 1 (mod 4), n > 1, and let positive t,u,v satisfy n = tuv−u−v with gcd(n,uv)=1. Then gcd(u,v)=1 and

    (uv/n) = −1  ⇔  4 divides at least one of t,u,v,tu−1,tv−1.       (2.1)

More explicitly:

* If u,v are odd, the sign is +1 precisely when u ≡ v ≡ 1 (mod 4).
* If one endpoint is divisible by 4, the sign is −1.
* If the even endpoint is 2 modulo 4, the sign is +1 precisely when t ≡ 1 or 2 (mod 4).

This includes t=1 and endpoints equal to 1 whenever the equation permits them.

**Proof.** A common divisor of u,v divides n, so the unit hypothesis gives gcd(u,v)=1. Put ε(x) = (2/x) = (−1)^((x²−1)/8) for odd x.

**Both endpoints odd.** Reciprocity, n ≡ 1 (4), n ≡ −v (u), and n ≡ −u (v) give

    (uv/n) = (−v/u)(−u/v)
            = (−1)^[α+β+αβ],
    α = (u−1)/2 mod 2,       β = (v−1)/2 mod 2.

Thus the sign is positive only when α=β=0. The word equation modulo 4 forces t ≡ 3 (4). If both endpoints are 1 modulo 4, no slot is 0 modulo 4. If an endpoint is 3 modulo 4, its product with t is 1 modulo 4, so the corresponding slot tu−1 or tv−1 is divisible by 4.

**One endpoint even.** By symmetry write u=2ᵃw with w odd, a≥1, and v odd. The same reciprocity calculation gives

    (uv/n) = ε(n)ᵃ ε(v)ᵃ (−1)^[α+β+αβ],
    α = (w−1)/2 mod 2,       β = (v−1)/2 mod 2.                  (2.2)

If a≥2, reduction modulo 4 forces v ≡ 3 (4), so the last sign is −1. When a is even the ε factors cancel by their exponent. When a is odd, a≥3 and n ≡ −v (8), so ε(n)=ε(v). The sign is therefore −1, as required by 4|u.

It remains to consider a=1. If t=2k is even, n ≡ 1 (4) forces v ≡ 1 (4). Modulo 8,

    n ≡ 4k−v−2w,
    ε(n)ε(v) = (−1)^[k+(w+1)/2].

Combining this with the last factor (−1)^((w−1)/2) in (2.2) gives (uv/n)=(−1)^(k+1). Thus t ≡ 0 (4) gives sign −1 and t ≡ 2 (4) gives +1. Only the former has a 4-divisible slot.

If t=2k+1 is odd, v ≡ 3 (4). Now n+v=2w(tv−1) is 4 modulo 8 for t ≡ 1 (4), and 0 modulo 8 for t ≡ 3 (4). Hence ε(n)ε(v)=(−1)^(k+1), while the last factor in (2.2) is −1. The sign is (−1)^k. In the negative case t ≡ v ≡ 3 (4), so 4|tv−1. In the positive case tv−1 ≡ 2 (4), and all five slots miss 0 modulo 4. This proves all cases. ∎

**PROVED equivalent cell description.** The non-certificate triples (t,u,v), modulo 4, are exactly

    (1,2,3), (1,3,2), (2,1,2), (2,2,1), (3,1,1).

These are the five cells already recorded in `DEDEKIND_ES.md` §8.1. The proof above explains them rather than assuming the table.

### Corollary 2.2 — the graph bridge, including boundaries (PROVED)

The endpoint bound is elementary: for u≥2, (u−1)(v−1)≤p+1 gives v≤p+2; for u=1, (t−1)v=p+1 gives v≤p+1. At a prime p>3 every non-diagonal edge has unit endpoints: if p divides one endpoint it divides both, and this bound leaves no distinct such pair. Thus Theorem 2.1 applies to every edge. Moreover

    (tu−1)v = p+u,      (tu−1)(tv−1)=tp+1,
    χ(tu−1)=χ(u)χ(v).

Consequently

    good edge ⇔ opposite endpoint colours
              ⇔ some component contains both colours.             (2.3)

The last equivalence is the discrete intermediate-value statement on a tree path. No component is assumed connected to 1.

For completeness, the explicit ES triples are:

| divisible slot | denominators |
|---|---|
| t=4C | (uvC, pvC, puC) |
| u=4d | (d(tv−1), ptd, ptd(tv−1)) |
| tv−1=4m | (mu, mu(tu−1), pm(tu−1)) |

The other two slots are obtained by interchanging u,v. All factors are positive, and cross-multiplication verifies each identity.

**PROVED control scope.** For an odd square n, every unit endpoint has Jacobi colour +1, so (2.1) produces no unit-endpoint certificate. It does not silently classify nonunit edges. Their absence of 4-slots is checked separately by the existing square suite. The five displayed identities have numerator-k analogues when the corresponding slot is divisible by k, but the character equivalence (2.1) is special to 4, not 8.

## 3. The connected tree before pruning

### Proposition 3.1 — full remainder tree and exact pruning (PROVED)

On V={1,…,p−1}, put

    a_v = (−p mod v),          q_v = ceil(p/v),          v≥2.

Then 1≤a_v<v and p=q_vv−a_v. All arrows v→a_v form a rooted tree T_p with root 1. The induced forest F_p[V] retains exactly the arrows satisfying

    a_v | q_v+1.                                                   (3.1)

Its edge label is t=(q_v+1)/a_v. Every component root other than 1 is precisely a vertex whose arrow was deleted.

**Proof.** Primality excludes remainder zero for 1<v<p. Strict descent terminates at 1, so the graph is a tree. For u=a_v,

    p+u+v = (q_v+1)v,

and uv divides this expression exactly when u divides q_v+1. Each vertex has at most one smaller neighbour. ∎

**PROVED boundary reduction.** In the full F_p, vertex p is isolated; p+1 is a leaf attached to 1; p+2 is a leaf attached to 2. The latter two edges are monochromatic, since χ(p+1)=χ(1) and χ(p+2)=χ(2). Thus no certificate is lost by working on V. In particular H₄≤p−1 **if** a certificate exists.

**PROVED contraction identity.** If ρ(v) is the minimum vertex of v's actual component, contracting F_p[V] inside T_p produces another tree. Its vertices are the actual roots. For each root v>1 its parent is ρ(a_v)<v. If E is the number of retained edges, there are

    p−1−E components,       p−2−E deleted arrows.

This is an exact quotient tree, not an expander or a graph with cycle holonomy.

**Assessment: first obstruction.** A nonresidue certainly has a colour-changing arrow on its path to 1 in T_p. But that arrow may have been deleted. The discrete IVT proves a cut in T_p, not a cut in F_p. Contracting the retained components does not fix this: a nonconstant two-colouring on the quotient tree is perfectly consistent.

## 4. A large supply of virtual cuts — and their exact loss

### Proposition 4.1 — quotient-block cut identity (PROVED)

For every virtual arrow v→a_v,

    χ(a_v)χ(v)=χ(q_v).                                             (4.1)

Indeed q_vv≡a_v (p). Hence the entire block where ceil(p/v)=q consists of cuts if χ(q)=−1, and of non-cuts if χ(q)=+1.

The total number J(p) of virtual cuts is exactly

    J(p) = Σ_{2≤q≤p−1, χ(q)=−1}
           [ floor((p−1)/(q−1)) − floor((p−1)/q) ].                (4.2)

Terms for unattained quotients have zero width. The formula simply counts the integer interval p/q < v < p/(q−1); equality p/q is impossible here unless q=p, which is not in the sum.

Let r=r(p) be the least nonresidue. The q=r block alone gives

    J(p) ≥ floor((p−1)/(r−1)) − floor((p−1)/r)
         ≥ (p−1)/(r(r−1)) − 1.                                   (4.3)

**CONDITIONAL on OAI-003 (quasi-RH 7/8).** Since r≪log⁸p, (4.3) gives J(p)≫p/log¹⁶p for sufficiently large p. **CONDITIONAL on GRH**, r≪log²p gives J(p)≫p/log⁴p. These are genuine pointwise, power-size supplies of *virtual* cuts. They are not estimates for certificate counts.

### Proposition 4.2 — only the bottom of a block can survive (PROVED)

Fix an attained q≥2 and put a₀=(−p mod q), so 1≤a₀<q. Within its quotient block the possible parents are

    a = qv−p = a₀, a₀+q, a₀+2q, … .

A retained arrow requires a|q+1, hence a≤q+1. Consequently the only possibilities are

    a=a₀ with a₀|q+1;
    a=q+1 when a₀=1.                                             (4.4)

The second is the t=1 boundary. In both cases the additional ordering condition a<v must hold. If a₀ does not divide q+1, the **entire** block is deleted.

**Assessment: why the power-size source does not help.** A block of length about p/q² can contain only one ordinary survivor, plus one boundary survivor. Almost all its cuts fail the elementary size requirement a≤q+1 before any subtle divisibility issue arises. Counting a huge source and expecting a positive retained proportion is invalid. Formula (4.4) is also the old HJ test in different coordinates: a nonresidue q needs (−p mod q)|q+1. The calculation identifies the precise collapse; it does not evade it.

### Proposition 4.3 — an infinite completely deleted cut block (PROVED, relative to Dirichlet)

There are infinitely many primes

    p ≡ 9601 (mod 120120)

with r(p)=13. At every such prime a₀=(−p mod 13)=6, and 6∤14. Thus the whole q=13 block, containing

    floor((p−1)/12) − floor((p−1)/13) = p/156 + O(1)

opposite-coloured virtual arrows, has **zero** retained arrows.

**Proof.** The progression fixes the characters of 2,3,5,7,11 at +1 and that of 13 at −1, as at 9601. Multiplicativity proves r=13. The residue modulo 13 is 7, so a₀=6; apply Proposition 4.2. The progression is reduced, so Dirichlet gives infinitely many primes. ∎

**CERTIFIED examples.** At 2521 the least-QNR block q=11 has 23 cuts and no survivors; at 9601 the q=13 block has 62 cuts and no survivors. The independent tree checker verifies (4.2) and all surviving-edge alternatives (4.4) on 5,575,032 vertices. It also checks 99 prime examples of the displayed progression (the four sampled vertices per large block are spot-checks, not an exhaustive scan of those blocks).

**Scope.** This refutes retention in the least-nonresidue block and any fixed positive-fraction retention rule for every nonresidue block. It does **not** refute survival in some other block. It is compatible with H₄≪log²p.

## 5. Adaptive repair: the first split fibre

The previous failure suggests moving the *smaller* endpoint rather than insisting on q=r or v=r.

### Definition and Proposition 5.1 (PROVED)

Define

    B(p) = min{ b≥1 : p+b has a prime factor ℓ with χ(ℓ)=−1 }.

Then

    1 ≤ B(p) < r(p).                                              (5.1)

For b=B(p), χ(b)=+1, and every nonresidue divisor d of p+b satisfies b<d<p. Consequently B(p) is also the least root having an opposite-coloured child in the full tree T_p.

**Proof.** Take a=(−p mod r), with 1≤a<r. The integer p+a is divisible by the nonresidue prime r, proving B≤a<r. Every integer up to B is a residue. Thus any nonresidue divisor d exceeds B. Since χ(p+B)=χ(B)=+1, its complementary divisor is also a nonresidue and exceeds B. In particular d≤(p+B)/2<p. Conversely, below B all prime factors of p+b are residues, and χ(b)=+1, so no opposite-coloured virtual child exists. ∎

A virtual child d at root b becomes an actual neighbour exactly when

    d | p+b,       d ≡ −p (mod b).                                (5.2)

Thus the first split fibre gives a certificate precisely when at least one of its negative divisors has the residue in (5.2). This is already a finite exact test of a *single* prescribed integer.

### Proposition 5.2 — the first four roots always fire (PROVED)

If B(p)≤4, the first split fibre supplies a certificate. In fact

    H₄(p) ≤ floor(sqrt(p+B(p))).                                  (5.3)

**Proof.** At b=1 the class condition is empty. At b=2 all divisors of p+2 are odd and hence are in the required class. For b=3, B<r implies χ(2)=χ(3)=+1, so p≡1 (24). The number p+3 is divisible by 4. Choose a negative prime divisor ℓ>3. If ℓ≡2 (3), use it; otherwise use 2ℓ, which is still a negative divisor and is 2 modulo 3. This is the desired class −p. For b=4, p+4 is odd, and any negative prime divisor ℓ obeys

    χ(ℓ)=(p/ℓ)=(−4/ℓ)=(−1/ℓ),

so ℓ≡3 (4), again the desired class. In each of these four cases p≡1 (b), and the complement of the chosen negative divisor is negative and in the same required class. Choose the smaller of the pair. It still exceeds b because b<r, and gives (5.3). ∎

**Assessment: why this was worth pursuing.** B is guaranteed to be small under the permitted hypotheses, and the earliest four possibilities really do force attachment. This is stronger than “there exists a small nonresidue” as a usable construction. However it is not a polylog H₄ theorem: even (5.3) is a square-root endpoint bound, and B can exceed 4.

### The first failure is not a numerical accident

**CERTIFIED at p=9601.** Here r=13, B=6, and

| b | factorization of p+b | characters of its prime factors |
|---:|---|---|
| 1 | 2·4801 | all + |
| 2 | 3²·11·97 | all + |
| 3 | 2²·7⁴ | all + |
| 4 | 5·17·113 | all + |
| 5 | 2·3·1601 | all + |
| 6 | 13·739 | both − |

Both negative divisors at b=6 are 1 modulo 6, whereas the required class is 5 modulo 6. Indeed **every** divisor of p+6 is 1 modulo 6, so vertex 6 is isolated in the actual forest. The first successful smaller root is 9, with the edge {9,155}; the height minimum is instead {13,19}, t=39. These two minima must not be conflated.

### Theorem 5.3 — persistent first-split failure (CONDITIONAL on Dickson)

Infinitely many primes satisfy simultaneously

    r(p)=13,       B(p)=6,       vertex 6 is isolated in F_p.       (5.4)

**Proof.** Put c_i=9601+i, 1≤i≤6, and

    M = 6·lcm(24,c₁,…,c₆)
      = 784961803025427901713840.

Consider the seven positive linear forms

    p(k)=9601+Mk,          L_i(k)=1+(M/c_i)k.

Suppose all are prime, with k sufficiently large. Then p+i=c_iL_i and L_i≡1 (6). The progression fixes the character of every prime factor of every c_i, and of every prime ≤13. In particular r(p)=13. Also

    χ_p(L_i)=χ_p(i)χ_p(c_i)=+1.

For i≤5 all prime factors of c_i are residues, so no earlier fibre splits. For i=6, c₆=13·739 has two negative prime factors, both 1 modulo 6, and L₆ is a positive-colour prime also 1 modulo 6. Hence B=6 and every divisor of p+6 is 1 modulo 6; vertex 6 has no neighbour.

The forms are distinct and primitive. At every prime ℓ≠9601, k=0 avoids divisibility of all seven forms. At ℓ=9601, M is invertible and at most seven residue classes are excluded, fewer than 9601. The family is admissible. Dickson supplies infinitely many simultaneous prime values. ∎

**Scope.** This disproves the proposed eventual “first split fibre fires” statement, conditional on Dickson. It does not disprove ES or eventual survival among *all* fibres. The construction has fixed small r, so improving least-nonresidue bounds cannot remove this obstruction.

## 6. Can successive split fibres force escape?

Define C(p) to be the least vertex incident to a certificate, equivalently the least smaller endpoint of a good edge. Define K(p) as the number of roots b≤C(p) having an opposite-coloured **larger** child in T_p. These are virtual split fibres, allowing the root itself to be negative after b≥r. When certificates exist,

    B(p) ≤ C(p) < H₄(p),       K(p)≥1.

**PROVED caution.** After B, “has a nonresidue divisor” and “has an opposite-coloured larger child” are not interchangeable. At a negative root a residue child is the relevant one. The scanner makes this distinction.

**CERTIFIED escalation failure.** At p=4437721,

    r=11, B=9, C=22, H₄=31, K=8.

The first seven virtual split roots are

    9, 10, 11, 13, 17, 18, 20;

none has an opposite-coloured actual neighbour. Root 22 finally has the certificate {22,31}, t=6507. The factorization and divisor lists for all eight fibres are retained in `analysis.json`. Thus “the next split fibre”, or even “one of the first seven”, is not a universal escape rule. Here C=2r; an actual certificate need not have its smaller endpoint below the least nonresidue.

At p=1726201, B=6 but C=22, with six virtual split fibres before the first hit. At p=4962049, B=16 fails and C=17 succeeds, while H₄=247 is achieved at a different root, 181.

### Theorem 6.1 — finite root-incidence patterns repeat (CONDITIONAL on Dickson)

Fix a prime p₀≡1 (4) and 1≤h≤p₀−2. There are infinitely many primes p≡1 (4) for which, for every i≤h:

1. the presence/absence of a nonresidue prime factor in p+i is the same as at p₀+i;
2. the presence/absence of an opposite-coloured actual neighbour of i is the same as at p₀;
3. every fixed opposite-coloured larger virtual child of i at p₀ is still such a child at p.

One may additionally require r(p)=r(p₀).

**Proof.** Let L=lcm(1,…,h), c_i=p₀+i, and take M divisible by 8L·lcm(c₁,…,c_h). To preserve r as well, multiply M by lcm(1,…,r(p₀)); this does not introduce the prime p₀. We have gcd(M,p₀)=1. Apply Dickson to

    p=p₀+Mk,         L_i=1+(M/c_i)k,       1≤i≤h.

At primes other than p₀ use k=0. At p₀ the excluded classes are exactly 0 and −iM⁻¹, 1≤i≤h, so fewer than p₀ classes are excluded. Thus the family is admissible. Take the simultaneous prime values sufficiently large that each L_i exceeds all c_j.

Every divisor of p+i=c_iL_i is d or dL_i with d|c_i. The fixed congruences preserve χ_p(i), χ_p(d), and χ_p(c_i) at their p₀-values. Since χ_{p₀}(c_i)=χ_{p₀}(i),

    χ_p(L_i)=χ_p(i)χ_p(c_i)=+1.

Also L_i≡1 (i), and p≡p₀ (i). Therefore both new divisors have the same colour and residue modulo i as d. The neighbour condition i|p+v is unchanged. Removing a possible loop at i=1 cannot affect opposite colours. This proves (1) and (2). A former larger virtual child d remains a divisor of p+i, retains its colour, and remains >i, proving (3). Prescribing the small-prime characters through r fixes the least nonresidue. ∎

**CONDITIONAL consequence.** Applying the theorem at p₀=4437721 with h=22 gives infinitely many primes with r=11, C=22 and K≥8. Extra virtual split fibres can appear, so equality K=8 is **not** asserted. At p₀=9601, h=6, it gives the first-split obstruction in a more general form.

**Assessment and limitation.** This repetition lemma is an extension of the repository's Dickson shadow construction to a seed prime's *coloured root-incidence pattern*. It preserves unrestricted neighbour existence at each fixed root, not merely small endpoint tests. It does **not** preserve entire components or prove that arbitrary numbers of successive split fibres can be blocked. In particular, it does not refute a growing-root theorem or H₄≪polylog(p). When a seed certificate is among the preserved incidences, its fixed endpoints also remain certificates, so these repetitions are not an adversarial large-H₄ construction.

## 7. What Euclidean/continued-fraction descent actually retains

**PROVED local identities.** A virtual arrow corresponds to p=qv−a. If q>a as well, complementary factorization exchanges v and q and gives another virtual arrow q→a. Its survival conditions are respectively

    a | q+1,           a | v+1.

They are not equivalent in general. If the first holds, q≡−1 (a), whereas v≡−p (a); complementary factorization preserves an actual edge at a only when the second congruence also holds. In particular p≡1 (a) makes the two conditions equivalent, but does not produce their first occurrence.

**PROVED actual-path recurrence (prior result, rechecked).** Along an increasing actual path x<y<z, both neighbours of y are −p modulo y, so

    z=ky+x,        k≥1.

Thus the reversed path reads like an ordinary Euclidean remainder chain and has Fibonacci growth. The *unpruned* next remainder, however, is (−p mod x), not y mod x. To extend an actual descent at x one must still check its own divisibility gate. Continued-fraction structure describes retained paths; it does not ensure the next arrow is retained.

**Assessment: failed defect descent.** Writing q+1=ta+s at a missing arrow gives

    p−sv = tav−a−v.

If s>0, even when t>0 and p−sv>0 this is a word at a different integer, not at p; if either positivity condition fails it is not a positive word at all. Neither the primality hypothesis nor the Legendre colouring is preserved. This is exactly where an attempted Euclidean correction ceased to be a fixed-p argument. No decrease of s that preserves p and forces another cut was found. Factoring q+1 instead merely reintroduces the divisors in (4.4).

**Assessment: exact CF obstruction.** The quotient test a₀|q+1 is the condition that a negative numerator q has an HJ expansion of length at most three, up to the usual boundaries. A full Euclidean expansion always exists, but shortening it to length three is precisely what remains unproved. This attempt supplies no transport from a long negative CF word to a short one.

## 8. Global counting and colour identities

### Proposition 8.1 — exact identities, without a positivity conclusion (PROVED)

Let E be the edge set of F_p[V], let its components be T, and let r_T be the minimum vertex of T. Put m_T=#{v∈T:χ(v)≠χ(r_T)}. Then

    Σ_T χ(r_T)(|T|−2m_T)=0,                                      (8.1)
    Σ_{uv∈E}(χ(u)−χ(v))² = 4·#{bichromatic edges}.                 (8.2)

Equation (8.1) is the complete character sum Σ_{v=1}^{p−1}χ(v)=0 regrouped by components. Equation (8.2) is immediate edge by edge.

If every component were monochromatic, (8.1) would become

    Σ_{positive roots}|T| = Σ_{negative roots}|T| = (p−1)/2.

This is consistent: neither side has a proven size obstruction. The degree identity for the negative induced forest is likewise

    #cut edges = Σ_{χ(v)=−1}deg(v) − (p−1) + 2·c₋,

where c₋ is the number of components induced on the negative vertices, including isolated vertices. It contains no forced positive term beyond the cut count itself.

**Assessment: why edge totals and spectra did not close the proof.** A forest on p−1 vertices whose two colour classes are both nonempty can have p−3 edges with no cut. The observed actual forest has only tens or hundreds of edges at these primes; its many isolated vertices absorb global character balance. A positive spectral gap cannot be applied to a disconnected graph. The exact energy (8.2) is a useful detector but is not independently positive. No arithmetic identity was found that bounds the component colour imbalance or forces that energy away from zero.

**CERTIFIED illustration.** On V at 9601 there are 24 actual edges and 9576 components; the full tree has 228 virtual cuts but only four retained cuts. At 66529 there are 32 actual edges, 66496 components, 1576 virtual cuts and nine retained cuts. The boundary leaf edges explain the difference of two from full-F_p edge counts.

## 9. Computation, adversaries, and controls

### 9.1 Complete finite census (CERTIFIED)

`scripts/z48_forestastra_scan.c` constructs every edge by the progression n=tuv−u−v. A separate SPF-divisor traversal reconstructs the full edge set at every selected prime. Both agree in membership and count. Euler's criterion and an independent Jacobi routine agree on every endpoint sign; every edge is checked against Theorem 2.1 and the five slots. A third, raw-parent scan independently verifies every H₄ minimum.

The selection is all primes p≡1 (4) through 10⁶, and all p≡1 (24) through 10⁷. The union has 112330 primes and **10059389 edges**, with zero sign-law or edge-set discrepancies. This is not a random sample, and no unsuccessful search is silently censored: the graph enumeration is complete.

For the requested p≡1 (24) range alone:

| quantity, p≤10⁷ | exact count |
|---|---:|
| primes | 82887 |
| edges of full F_p | 7693645 |
| certificate/bichromatic edges | 4635979 |
| primes with no certificate | 0 |
| first split fibre fails | 206 |
| component of 1 is monochromatic | 1726 |
| C(p)≥r(p) | 20 |

The number K of virtual split fibres through the first actual hit has distribution:

| K | 1 | 2 | 3 | 4 | 5 | 6 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|
| primes | 82681 | 164 | 31 | 6 | 2 | 2 | 1 |

**EVIDENCE, not a theorem.** The first split fibre succeeds unusually often (99.75% here), but Theorem 5.3 shows why that success rate must not be promoted to eventual certainty. The data also do not justify a universal bound K≤8.

### 9.2 Required hard primes (CERTIFIED)

C is the least smaller endpoint; u is the smaller endpoint of an H₄-minimizing edge. They can differ.

| p | r | B | C | H₄ | minimizing (u,v,t) |
|---:|---:|---:|---:|---:|---|
| 193 | 5 | 2 | 2 | 5 | (2,5,20) |
| 409 | 7 | 4 | 4 | 7 | (4,7,15) |
| 577 | 5 | 3 | 3 | 5 | (3,5,39) |
| 2521 | 11 | 2 | 2 | 29 | (2,29,44) |
| 3361 | 11 | 3 | 3 | 29 | (3,29,39) |
| 5569 | 13 | 7 | 7 | 17 | (7,17,47) |
| 9601 | 13 | 6 | 9 | 19 | (13,19,39) |
| 66529 | 13 | 5 | 5 | 26 | (5,26,512) |

All their complete edge sets are independently reconstructed in Python, and the existing exact-fraction helper checks all 46 available certificate identities at them. The largest H₄ in the census is 251 at 7449289; there B=4 and C=4, although the minimizing edge is {140,251}. The maximum B is 16 at 4962049. These are finite extrema, not upper-bound evidence beyond the stated range.

### 9.3 Near-squares (CERTIFIED finite counts)

Within the same complete p≡1 (24), p≤10⁷ census, select every p=m²+k for each listed fixed k:

| k | prime instances | max H₄ | first split failures |
|---:|---:|---:|---:|
| −24 | 232 | 47 | 0 |
| −8 | 139 | 41 | 0 |
| −3 | 153 | 87 | 2 |
| 1 | 50 | 61 | 0 |
| 8 | 0 | — | — |
| 24 | 171 | 115 | 0 |

The empty +8 row is a congruence exclusion, not a successful test. **Assessment:** these modest samples say nothing about a uniform near-square lower tail.

### 9.4 Controls and independent structural checks (CERTIFIED)

* 4305 coprime unit words, including composite n and even-endpoint valuations through 8, verify the direct reciprocity cases and recover exactly the five positive mod-4 cells.
* All 386 selected small/hard primes have their full remainder trees checked in Python: 5575032 vertices; the contraction, quotient-cut sum, bottom-of-block rule, component colour balance and edge-energy identities all agree.
* Twelve actual simultaneous-prime specializations, at seeds 5, 13, 17 and 29, check all three conclusions of Theorem 6.1 and least-nonresidue preservation. They are finite checks of the implication, not evidence certifying Dickson. The largest resulting prime is 19384473629.
* The pre-existing `z43_astra_check.py` passes unchanged: 24389 edges at all odd n≤2000, 21135 exact rational identities, and all 499 odd squares through 999² (17372 edges), plus the earlier Dickson-family fixtures. These tests were reused rather than rewritten.
* At 17 and 241 the forest has respectively four and six bichromatic edges but no slot divisible by 8. Thus the numerator-4 character equivalence cannot be reused to prove the false statements 8/17 or 8/241. The 11 and 131 numerator-8 controls likewise have no 8-slot edge, but lie outside p≡1 (4).
* At the nonsquare composite 105 there is no unit mixed edge. The virtual-tree argument uses primality: for a composite input some remainders are zero and Jacobi colours can be zero. It is not a nonsquare-only proof in disguise.

### 9.5 Reproduction and resource bounds

**CERTIFIED execution.** The complete 10⁷ C census with the independent full-divisor audit takes 27.72 seconds elapsed, peak RSS 284304 KiB on this machine. All commands run under an 8000000-KiB virtual-memory limit and explicit timeouts. Data are streamed or stored in O(N + selected edges) space, with a separate edge-allocation ceiling of 2 GB. No Cartesian product arrays are used. Retained data are under 20 MB.

```sh
set -euo pipefail
ulimit -v 8000000
gcc -O3 -std=c11 -Wall -Wextra -Werror scripts/z48_forestastra_scan.c -lm -o /tmp/z48_forestastra_scan
timeout 1200 /tmp/z48_forestastra_scan 10000000 audit \
  2> data/z48_forestastra/census_1e7.log | gzip -n > data/z48_forestastra/census_1e7.csv.gz
timeout 240 env PYTHONPATH=scripts uv run python scripts/z48_forestastra_check.py \
  > data/z48_forestastra/analysis.txt
timeout 180 env PYTHONPATH=scripts uv run python scripts/z43_astra_check.py \
  > data/z48_forestastra/existing_checks.txt
```

Files: this document, `scripts/z48_forestastra_scan.c`, `scripts/z48_forestastra_check.py`, and `data/z48_forestastra/`. The Python checker imports existing helpers from `scripts/z43_astra_check.py`; no existing source is modified.

## 10. Exact remaining gap and verdict

**PROVED reduction.** The desired pointwise theorem is equivalent to saying that some virtual cut survives pruning:

    ∃ 2≤v<p:
       χ(ceil(p/v))=−1,
       (−p mod v) | ceil(p/v)+1.                                 (10.1)

Equivalently, there are 1≤b<d<p with d a divisor of p+b satisfying

    d≡−p (mod b),             χ(d)=−χ(b).                         (10.2)

These are exact statements about the actual integers, not average statements. Equations (4.2) and (5.1) prove abundant virtual cuts and an early split fibre, respectively. They do **not** prove (10.1) or (10.2).

**CONDITIONAL on OAI-003 (quasi-RH 7/8).** We obtain r≪log⁸p, B<r, and ≫p/log¹⁶p virtual cuts. **CONDITIONAL on GRH**, replace the exponents 8 and 16 by 2 and 4. No inference to H₄ follows. The entire least-QNR quotient block can be deleted on an unconditional infinite progression; the first split root can be isolated infinitely often under Dickson.

**Assessment: what would genuinely advance this route.** One needs a fixed-p retention theorem using relations between *different* quotient blocks or split fibres, strong enough to force a divisor in the single residue class in (10.2). A proof that only finds more nonresidues, more virtual cuts, a longer actual path, or a positive character main term does not provide this. Even a theorem C(p)≪polylog(p) would not by itself control the larger endpoint H₄.

**Screen audit (Assessment).** T1 is respected by the unit character; numerator 8 fails exactly at the character-to-slot bridge; no thin-family result or average is promoted to pointwise existence; no two-sided asymptotic, large-prime pooling, signed reflection, or relaxation transport is used. The candidate uses growing roots, so the fixed-menu no-go does not refute it. It still fails the key screens: the tied divisor class is not forced, and the available quadratic information does not locate a divisor within that class. The explicit hard-prime and near-square tests pass only as finite computations.

**Honest verdict: PARTIAL, promise 1/5.** The required converse and the discrete-IVT bridge are now elementary and boundary-complete. The main forcing assertion remains unproved, with or without either permitted analytic hypothesis. The sustained remainder-descent attempt isolates the missing retention step and gives exact infinite-family obstructions to two tempting repairs. There is no claimed proof of ES, of eventual ES₅, or of a polylogarithmic H₄ bound.
