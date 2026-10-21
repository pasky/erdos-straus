# DELTA_TRANSPORT — a dyadic folding move, and the quotient that blocks it

## 0. Summary

**Assessment.** Distance one has an exact marked normal form, not just a scalar defect. It records an overflowing prime ℓ, its original exponent b, coprime integers u,v with vℓ(u)=b+1, and a quotient a=(u+v)/m. **PROVED:** for numerator 4, an overflow at 2 with **a=1** folds to a zero-distance window m′=v, with explicit positive integer denominators. This is a real cross-window transport, and its automatic divisibility is genuinely different for 4 and 8: 4|u follows from b≥1, whereas 8|u does not. At 8/131 the analogous source has u=4,v=9,m=13 and fails exactly this extra bit. But a=1 is essential: the same construction at a>1 produces a certificate for **an**, with a denominator coprime to a, so it cannot be scaled back. **CERTIFIED:** among all 2,166 distance-one windows of the 143 primes p≡1 (24), p≤10,000, folding handles 250; adding a least-residue re-splitting move handles 296 in total. Thirty-five of the 143 primes have no edge under either move. All 47 composite minimum-one controls have mixed/scaled ES solutions, but no shaped target. No global transport theorem follows.

**Verdict: PARTIAL. Promise: 1/5.** The restricted folding lemma works; universal availability of this move is already false. The remaining programme needs new moves or a class-sensitive all-window input at B2. **ES remains open.**

## 1. Setup, scope, and prior work

**Attribution / Assessment.** The starting lead is `BREADTH_Z45.md` §5, following `BRAINSTORM/z45_prime_t1_dual.md` §5 and `OVERFLOW_DISTANCE.md`. The z46 review (`reviews/z46-depth-review.md` §3) validates the distinction between total overflow and the square cap, the complete composite minima, and the genuine sibling controls. We read the mandatory FRONTIER and brainstorm index, CAP_POINTWISE, FORCED_WINDOW, TWO_POWER_LADDER, POWER_LADDER_ES, and the ledger statements (J)32/(J)57. Repository searches for overflow/transport, one-extra-exponent, and re-splitting locate the preceding overflow work, the old cap geometry, `BRAINSTORM/graph_cayley_moves.md`, and `BRAINSTORM/z28_espectrum_share.md`. The folding identity below is elementary and a specialization of the known five-slot word dictionary; its formulation as a **marked distance-one transport**, the quotient obstruction, and its measured coverage are the increment. No external-priority claim is made.

**Definition.** For gcd(B,M)=1, factor B=∏ℓᵇ and let

    δ(B²,M,−B) = min Σℓ (cℓ−2bℓ)⁺,

where cℓ≥0 and ∏ℓᶜℓ≡−B (mod M). An empty minimum is ∞. At numerator k, a **shaped window** has

    m=kK−n>0,  gcd(m,n)=1,  K=(n+m)/k,
    δm(k,n)=δ(K²,m,−K).

Our primary numerator-4 box is m≤n, exactly as in OVERFLOW_DISTANCE. Here and in the shaped numerator-8 controls n is odd, so gcd(k,n)=1 and all factors of K are units modulo m and n. A zero gives a Type-II-shaped solution. For k=4 the zero search is complete in this box (indeed 3m≤n+4 at every zero); positive-distance windows are still scanned through n.

**Definition.** Complete residual searches, necessary for genuine failures, instead take

    n/k < x ≤ 3n/k,
    (kx−n)/(nx)=A/B in lowest terms,
    δres,x=δ(B²,A,−B).

Global residual minimum zero is equivalent to a three-unit-fraction representation. This is not the shaped invariant: B usually contains n as well as x. We do **not** apply a shaped-window transport to residual data merely because their δ values agree.

**PROVED / recalled.** At k=4 and n an odd square, every admissible shaped window has δ=∞, by the odd character χ₋ₘ which is +1 on every prime of K and −1 on −K (`OVERFLOW_DISTANCE` §1.2). Mixed/scaled solutions at squares are not excluded. At (2113,43), δ=1 while the same-window square cap is ∞; no square-cap argument is used below.

**Assessment, correcting the premise.** Distance one does **not** mean that the divisor image misses only one residue. At (2113,43), the bounded image has 15 elements in a generated group of order 42: it misses 27 residues. Only the distance of the specified target is one.

## 2. Precise questions

**Question Q1.** What extra marked information distinguishes a radius-one witness that transports from one that does not? In particular, is an overflow at 2 enough, or must one control its quotient a?

**Question Q2.** In a graph whose edges are explicit, arithmetically justified moves, does every distance-one window have an edge to a zero? More weakly, does every eligible prime have at least one such source? The graph must be specified before measuring it: connecting a source to any zero found by a separate ES search would be circular as a transport mechanism.

**Question Q3.** Can CAP_POINTWISE's nonresidue forcing, or the numerator-4 Fano/χ-fibre fact, force the hypotheses of a successful move? The two proposed moves below answer Q2 negatively in their precise scope, not for every conceivable transport graph.

## 3. Mathematics and computation

### 3.1 Exact classification of the radius-one boundary

**Lemma 3.1 (PROVED).** Suppose the bounded divisor image of B² does not contain −B modulo M. Then δ=1 iff there is a prime ℓ|B, b=vℓ(B), and

    d=ℓ^(2b+1) e,   e | (B/ℓᵇ)²,   d≡−B (mod M).

These are **all** the minimum-cost exponent vectors. For each, write d/B=u/v in lowest terms. Then

    gcd(u,v)=1,  vℓ(u)=b+1,  ℓ∤v,
    T=uv/ℓ | B,  h=B/T,  ℓ∤h,
    u+v=aM,  a≥1,  gcd(a,uv)=1.                       (1)

Conversely, the stated d-form with its congruence has cost one; without the no-zero hypothesis it proves only δ≤1.

*Proof.* A sum of nonnegative integral excesses equals one precisely when one coordinate is 2b+1 and every other coordinate is within its budget. In the quotient d/B, its ℓ-coordinate is b+1; at every other prime its absolute exponent is at most the exponent in B. Thus uv/ℓ divides B, with the exact full ℓ-adic valuation b, so ℓ∤h. Coprimality of B and M gives M|u+v. A common divisor of a and u or v would divide both u and v. ∎

**Consequences (PROVED).** The overflowing exponent **2b+1 is always odd**, irrespective of the prime ℓ. The prime need not be 2; b need not be odd. The elementary set test is

    −B ∈ (⋃ℓ ℓ·S) \ S,   S={d mod M : d|B²}.

This tests radius one without computing higher distances. The marked list (1), rather than just this membership, is needed for transport.

**PROVED / dictionary.** For a shaped window, (1) gives

    K=h uv/ℓ,   m=(u+v)/a,   an=(ka h/ℓ)uv−u−v,       (2)
    k/n = 1/K + 1/(nK a/v) + ℓ/(n v h a).             (3)

The second denominator is integral; the last summand is reduced at ℓ because gcd(ℓ,nvha)=1. Thus the rational third denominator has denominator exactly ℓ. Equations (2)–(3) follow by substituting kK−n=m and combining the last two fractions. They recover OVERFLOW_DISTANCE's valuation interpretation with the quotient a exposed.

### 3.2 The transport that really works: dyadic folding at a=1

**Theorem 3.2 (PROVED, general conditional identity).** In (1)–(2), assume

    ℓ | k,   k | u,   a=1.

Set t=kh/ℓ. Then the window m′=v has a zero-distance witness, explicitly

    K′=(n+v)/k = (u/k)(tv−1),
    (x′,y′,z′) = ((u/k)(tv−1), n t u/k, n t u(tv−1)/k).       (4)

All three denominators are positive integers. This is a strict window descent: m′=v<u+v=m.

*Proof.* Equation (2) is n=tuv−u−v, so n+v=u(tv−1). The hypothesis k|u makes K′ integral; positivity follows from n+v>0. Also gcd(v,n)=1 because v|K and gcd(K,n)=1. The factor tv−1 divides K′ and is −1 modulo v. Therefore the ratio certificate (tv−1)/1 has product dividing K′ and sum tv divisible by v. The standard zero-window reconstruction gives (4). Directly,

    1/x′ + 1/y′ + 1/z′
      = k/[u(tv−1)] + kv/[n u(tv−1)] = k/n.

This proves the claim, including integrality and the actual target certificate, without searching its divisors. ∎

**Corollary 3.3 (PROVED, the numerator-4 automatic step).** For k=4, **every** distance-one witness with overflowing prime 2 and a=1 transports by (4). Indeed b≥1 implies v₂(u)=b+1≥2, so 4|u, and 2|4. Here h is odd, t=2h, and the denominators are

    x′=u(2hv−1)/4,  y′=nhu/2,  z′=nhu(2hv−1)/2.

No primality of n or m is needed; the shaped coprimality assumptions suffice. The source cannot exist at an odd square, by T1. It also cannot exist at a Type-II-free composite.

**PROVED / hand checks.** At n=73, m=15, K=22, the one-extra-2 divisor d=8 gives (u,v,a,h)=(4,11,1,1), and

    4/73 = 1/21 + 1/146 + 1/3066.

The target window is 11. At the forced **prime** source (n,m,K)=(409,31,110), d=200 gives (u,v,a,h)=(20,11,1,1), and the target is

    4/409 = 1/105 + 1/4090 + 1/85890.

Thus the mechanism is not confined to composite windows or to primes where (★) succeeds.

**Where 4, rather than 8, enters (PROVED).** At k=8 the same proof requires v₂(u)≥3, equivalently b≥2. A distance-one overflow with b=1 supplies only v₂(u)=2. At 8/131, the shaped window

    m=13, K=18, d=8, (ℓ,b,u,v,a,h)=(2,1,4,9,1,1)

has δ=1 and the exact identity

    8/131 = 1/18 + 1/262 + 2/1179.

The proposed target would have m′=9 and K′=(131+9)/8=35/2: **not an integer**. Its integer word is 131=4·4·9−4−9. Its five slots t,u,v,tu−1,tv−1 are 4,4,9,15,35: there are 4-divisible slots, but no 8-divisible slot. This is precisely the extra dyadic bit of (J)32/(J)57, not an appeal to “4 is a square.”

**Scope / Assessment.** The conditional identity is numerator-uniform; **its availability is not**. For k=15, an overflowing 2 does not even make t=15h/2 integral. An overflowing 3 or 5 makes t integral but does not force 15|u. More generally k=ℓˢ has the automatic budget condition b+1≥s. Thus this is not uniqueness of 4 among every conceivable numerator (9 has a similar conditional folding); it is a concrete, exact separation of 4 from 8 in the requested dyadic class. No false uniform existence law is asserted.

### 3.3 The quotient obstruction: Fano supplies a certificate for an

**Proposition 3.4 (PROVED).** At numerator 4, let ℓ=2 but allow arbitrary a. Then a and h are odd and

    an=tuv−u−v,   t=2ah≡2 (mod 4),   4|u,   v odd.     (5)

The five-slot word is automatically a numerator-4 certificate for **an**, via its u-slot. However its first denominator

    X=(u/4)(2ahv−1)

satisfies gcd(X,a)=1. If a>1, dividing this solution's denominators by a cannot yield an integral solution for n.

*Proof.* Since u is even and v,m odd, u+v=am forces a odd. Exactness of the overflowing 2 gives h odd. The word identity is (2), and (4)'s word calculation now applies to N=an. Since gcd(a,u)=1 and 2ahv−1≡−1 (mod a), also gcd(a,X)=1. ∎

**PROVED / example.** At (n,m,K)=(193,39,58), d=6728 yields

    (ℓ,b,u,v,a,h)=(2,1,116,1,3,1),
    4/193 = 1/58 + 1/33582 + 2/579.

The word is 579=6·116·1−116−1. Folding gives the solution (145,100746,503730) for 4/579; its first denominator is not divisible by 3. Nevertheless 193 has a zero elsewhere, at m=7. “Overflow prime 2 alone gives this descent” is therefore false.

**Assessment, Fano audit.** In (5), t has 2-adic valuation one, u has valuation at least two, and the other three slots are odd. The 4-divisible slot is the u-slot; the pigeonhole content of (J)57 is already visibly satisfied. What it certifies is the integer **an**. It supplies no additional divisibility by a for descent to n. This is an explicit location of the obstruction, rather than an unspecified failure to exploit the Fano theorem.

**Assessment, reciprocity audit.** CAP_POINTWISE forces −1 into the subgroup generated by primes of K, not into a face with a=1. Its principal odd-support construction at p≡1 (8) chooses q≡3 (8), so K is odd: it cannot produce an overflow at 2 at all. Even-K prime windows have q≡7 (8); the broader nonresidue group argument can still work there, as at 409/31, but does not control a or the bounded exponent vector. TWO_POWER_LADDER gives no class or quotient control beyond this parity information. POWER_LADDER_ES's free-Q ladder cannot remove a while keeping n, support, and the finite window box fixed.

### 3.4 Dropping the overflow and re-splitting: a precise B2 move

**Proposition 3.5 (PROVED).** In a numerator-4 radius-one configuration let T=uv/ℓ and let r be the least nonnegative residue of −n modulo 4T. For any coprime U,V with UV=T, if

    r>0,  gcd(r,n)=1,  r | U+V,                       (6)

there is a zero at window r, with

    Kᵣ=(n+r)/4,
    (x,y,z)=(Kᵣ, n(Kᵣ/U)(U+V)/r, n(Kᵣ/V)(U+V)/r).

Whenever it succeeds from a genuine distance-one source, r<m.

*Proof.* T|K makes m≡−n (mod 4T), and r gives T|Kᵣ. Condition (6) is precisely the ratio-divisor certificate. Since m=r+j4T, one has r≤m. Equality would give a zero at the source, a contradiction. ∎

**Definition.** The **drop** move uses only U=u/ℓ,V=v. The **repartition** move tries all coprime factorizations UV=T, without introducing new factors. Both retain a known product from the source. They are constructive sufficient moves, not a claim that (6) is forced.

**Proposition 3.6 (PROVED, no cheap dyadic drop).** If ℓ=2 or 3, neither drop nor repartition can succeed at a genuine distance-one numerator-4 source.

*Proof.* Put w=u/ℓ, so T=wv. Then

    m≤u+v=ℓw+v≤ℓwv+1=ℓT+1<4T.

The final strict inequality holds for ℓ=2,3 here since T≥ℓᵇ≥ℓ. Thus r=m. Every proposed repartition would be a zero at the source, impossible. More explicitly, a drop would require m to divide both ℓw+v and w+v, hence m|(ℓ−1)w. Since gcd(m,w)=1 and m≡−n≡3 (4) for our prime inputs, m≥3 and cannot divide 1 or 2. The r=m argument also covers the general admissible numerator-4 windows whenever a radius-one source exists. ∎

**PROVED / example with an odd overflowing prime.** At n=769, m=351, K=280, d=98000, the marks are (ℓ,b,u,v,a,h)=(5,1,350,1,1,4). Then T=70, r=71, and r|70+1. The drop move gives

    4/769 = 1/210 + 1/2307 + 1/161490.

The overflow prime need not divide the numerator for this second move. But (6) is FORCED_WINDOW Proposition 2.1's least-residue event, not a new theorem controlling it.

**PROVED, another elementary failed move.** Multiplying or dividing the first denominator K by an overflowing prime cannot by itself give a shaped zero in the numerator-4 box at odd n≥3. Dividing gives K/ℓ≤n/4, so the residual is not positive. Multiplying gives K′=ℓK>n/2, whereas every shaped zero has K′≤(n+1)/3. These inequalities rule out these two literal scaling moves, not arbitrary changes involving the other denominators. Multiplying all denominators by ℓ changes n to ℓn and is likewise not fixed-n transport.

### 3.5 Directed graph and complete finite computations

**Definition / protocol.** At fixed n the graph has all admissible shaped windows in the stated box as vertices. From each radius-one source we include every folding edge of Theorem 3.2, the drop edge, and one successful repartition edge for each marked witness if available. All targets have distance zero and strictly smaller m. Hence longer paths add nothing to this particular graph. We do not add an edge merely because some unrelated zero is known. On residual fibres we record profiles only, not shaped graph edges.

**CERTIFIED.** `z47_delta_transport_scan.py` enumerates the complete lists in Lemma 3.1. A separate engine, `z47_delta_transport_verify.py`, builds bounded residue sets and tests radius one by multiplying a bounded residue by one generator. It independently checks **every fibre**, including omitted non-radius-one fibres, in all stated populations; reconstructs all witness valuations; independently checks the graph's edge conditions; and checks exact rational identities. It verifies 3,175 recorded radius-one fibres, 3,953 marked witnesses, and 365 labelled edges (including repeated inputs between populations). Data size is about 126 KB. The count “not radius one” is **not** a count of infinite distance: we deliberately do not recompute larger distances.

| shaped population | inputs | fibres | δ=0 | δ=1 | has a 2-overflow | drop/repartition source windows | folding source windows | union with an edge |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| all p≡1 (24), p≤10,000; m≤p | 143 | 171,732 | 1,283 | 2,166 | 487 | 46 / 46 | 250 | 296 |
| all 47 z46 minimum-one composites; m≤n | 47 | 41,168 | 0 | 223 | 51 | 0 / 0 | 0 | 0 |
| 23 fixtures; m≤min(n,511) | 23 | 2,813 | 233 | 277 | 72 | 0 / 0 | 20 | 20 |
| k=8, n=11,17,131,241; m≤n | 4 | 49 | 0 | 7 | 3 | 0 / 0 | 0 | 0 |

**CERTIFIED.** Among the 2,517 prime-census marked witnesses, overflow primes include 2 (531 witnesses), 3 (434), 5 (353), 7 (222), and many others up to 761. The original b is odd in 2,167 and even in 350. Thus neither the prime nor the original exponent parity is universal. The 487 prime windows admitting 2-overflow divide into 250 with a=1 and 237 without; only the former fold. The 46 repartition-success windows are the same 46 windows already handled by drop in this census; repartition adds no extra covered source here, not a theorem that it never helps.

**CERTIFIED, answer to the graph question.** Only 296/2166 ≈13.67% of prime radius-one source windows have an edge. All 143 primes have radius-one sources; only 99 have a folding source and only 108 have any edge in this graph. Thus **35 primes already disprove universal source availability for this move dictionary**. In particular 193 has five radius-one windows and no edge; 2113 has fifteen and no edge; 2521 has fifteen and no edge. These are complete m≤p assertions. All have zeros elsewhere. A theorem forcing the present move at every prime would be false, not merely unproved.

**CERTIFIED, real failures on the same complete residual invariant.**

| residual population | fibres | δ=0 | δ=1 | δ=1 with a 2-overflow | marked witnesses | b odd / b even |
|---|---:|---:|---:|---:|---:|---:|
| 4/n, n=11,17,131,241,2113,3985 | 3,248 | 144 | 293 | 36 | 435 | 408 / 27 |
| 8/n, n=11,17,131,241 | 100 | 0 | 24 | 3 | 42 | 42 / 0 |
| 15/n, the 27 z46 minimum-one failures | 8,857 | 0 | 185 | 34 | 268 | 251 / 17 |

**CERTIFIED / interpretation.** The four numerator-8 rows have respectively 2,2,13,7 radius-one residual fibres. At 8/241 all eleven marked radius-one witnesses overflow odd primes (five overflow 241 itself); there is no shaped radius-one window in our m≤n box at 241. At 8/17 there is likewise no shaped radius-one window, despite two residual ones. This is why the full residual and shaped comparisons must remain separate. The fifteen-numerator failures have even and odd overflow primes and both parities of b; even “overflow at 2 with a=1” occurs in three residual fibres. There is no scalar/parity feature here which distinguishes all successes from failures.

**CERTIFIED / separating feature, with its exact limitation.** The **foldable shaped mark** (ℓ|k, k|u, a=1) occurs at numerator 4 and cannot occur at an actual k/n failure, by Theorem 3.2. In numerator 8's observed shaped dyadic a=1 sources, b=1, so precisely the missing 8|u blocks it. This separates a useful class of successful source configurations, not every 4/n source. The 47 composites have no such marks either; their different route is scaling, below. We found no universal local fibre-profile separator for the union of prime and composite 4/n successes versus the sibling failures.

### 3.6 All 47 composites really satisfy ES, outside these shapes

**CERTIFIED, with elementary proofs of the identities.** Exactly 42 of the 47 minimum-one composites are divisible by 3. The other five are

    1705, 3985, 4585, 6265, 12145,

all divisible by 5. For n=3s use

    4/n = 1/s + 1/(4s) + 1/(12s),

and for n=5s use

    4/n = 1/(2s) + 1/(4s) + 1/(20s).

The numerators sum to 4/3 and 4/5 before scaling. Every denominator has gcd>1 with n because s>1, so none of these displayed solutions is Type I or Type II under the coprimality-sensitive definitions in FRONTIER. The data record all 47 exact triples. Examples: 93→(31,124,372), 3985→(1594,3188,15940).

**Assessment.** These composites do not support a Type-II δ≤1⇒δ=0 transport: they refute it. They do satisfy unrestricted ES by mixed/scaled shapes. Replacing the target by “some unrestricted ES solution” makes composite descent legal, but breaks the claimed equivalence with zero of the shaped invariant and requires a separate prime argument.

### 3.7 Test primes, near-squares, and the old parity separator

**CERTIFIED.** Every named (★)-failure prime, 193/2521/66529, 3361, and 5101441 has an explicitly checked zero target. The first-zero windows reproduced here include

    193→7, 409→7, 2521→23, 66529→31,
    3361→3, 5101441→19, 8803369→107.

These are **existence controls**, not transport edges unless a proved move supplies them. Among the 23 fixture inputs (the 20 z46 fixtures plus 2113,31121,3985), only 20 of 277 radius-one windows below 512 have an edge. At 3361 the source m=119,K=870,d=33640 has (u,v,a,h)=(116,3,1,5) and folds to m′=3 and (841,974690,28266010), one of FRONTIER's two Type-II solutions. No split-slice or PM-II assertion is inferred from this window label.

**PROVED / exact old example.** At 2113/43 the sole radius-one mark is

    (ℓ,b,d,u,v,a,h)=(7,2,184877,343,1,8,11).

Folding is unavailable (7∤4); drop/repartition have T=49 and r=43, so cannot reach a zero. The bounded image consists of five 7-powers times three 11-powers modulo 43, giving 15 distinct residues; the full group has order 42. The earlier infinite-square-cap separation remains intact.

**CERTIFIED, diagnostic only.** The prime census contains 27 Mordell-hard inputs, with 329 radius-one sources and 42 sources having an edge. Its 62 near-square inputs, defined by distance ≤24 to the nearest square, have 788 radius-one sources and 106 with an edge. These finite tests supply no near-square forcing theorem. Exact odd squares have no shaped radius-one sources by the character proof, so our source-conditioned moves are not counterexamples to T1.

## 4. FRONTIER §4 checklist

**Assessment throughout.** PASS means that the stated partial theorem respects a screen, not that a full proof of ES is provided.

| # | status | reason |
|---:|---|---|
| 1 | PASS | At an odd square every shaped fibre has δ=∞. The source hypothesis is false. Composite scaling is explicitly outside Type I/II. The character obstruction, not a local-solubility claim, establishes this failure. |
| 2 | PASS restricted move | At 8/131 the dyadic a=1 source has u=4, so the target K′=35/2 is not integral. All four real controls have zero residual hits and no valid shaped edges. At 241 the radius-one sources are residual, not shaped. |
| 3 | PASS scoped; FAIL uniform upgrade | Conditional algebra works for k with ℓ|k and k|u; the automatic k|u step at (k,ℓ)=(4,2) fails at (8,2). No k-uniform transport availability is claimed; 15/n controls refute scalar/parity-only availability. |
| 4 | **FAIL globally** | Repartition retains the tied least-residue event (−n mod 4T)|(U+V). Folding removes that event only after a=1 and the specific exponent mark are supplied; no theorem forces them, and this move dictionary already misses primes. |
| 5 | PASS | n stays fixed in every actual graph edge. The an word is deliberately identified as a failed fixed-n transport when a>1. No average over n is used for existence. |
| 6 | N.A. | No main-term/error estimate. The census is not a power-size supply argument. |
| 7 | PASS | No two-sided asymptotic is asserted. |
| 8 | FAIL as a universal recipe | The full growing box is scanned, but the displayed finite move dictionary does not cover it. A new growing arithmetic input would be required; a fixed window menu is not proposed. |
| 9 | **FAIL at the forcing step** | Reciprocity forces subgroup access, not a=1, the marked exponent face, or the exact class in (6). |
| 10 | PASS | No pooling or collision of private large primes across shifts. Repartition uses only one source's actual factors. |
| 11 | N.A. | All moves and identities are positive; no signed reflection. |
| 12 | PASS locally; **FAIL globally** | Theorem 3.2 is an actual cap-zero transport with finite target. Its availability is not free; the flat power ladder supplies none of the missing marks. |
| 13 | PASS | No BM/local-global sufficiency is used. Fano supplies a slot on an existing word, not its existence or descent from an to n. |
| 14 | PASS diagnostic; FAIL universal dictionary | All requested primes retain true zero targets. The graph fails completely already at 193, 2113,2521 in their full boxes. It does produce the known non-split Type-II target at 3361. |
| 15 | PASS diagnostic | Exact squares are excluded by T1; the Mordell and near-square strata are explicitly measured. No inferred universal escape. |
| 16 | N.A. | No transfer from a thin factorization family to primes. |
| 17 | PASS computation; FAIL forcing | Every actual factor is retained. No theorem controls the large factors' residues or produces the marked source; no transparent coset-covering claim. |

## 5. New-theory sketch: marked boundary transport and its quotient

**Definition / Assessment.** Replace scalar δ by the **marked radius-one boundary**

    ∂₁(n;m) = {(ℓ,b,u,v,a,h) satisfying (1)–(2) and source δ=1}.

Attach two kinds of arrows: a **word-folding arrow**, whose integrality is controlled by (ℓ|k,k|u,a=1), and a **least-residue arrow** retaining T=uv/ℓ and its coprime partitions. Retain a as a separate multiplicative quotient, rather than averaging it away. This is a bookkeeping framework over known divisor boxes and words, not an established new existence theory.

**First theorem and tested toy (PROVED / CERTIFIED).** Theorem 3.2 identifies a genuine absorbing face: at numerator 4, ℓ=2,a=1 always points to δ=0 at v. Proposition 3.4 shows why the adjacent face a>1 is not a free descent: the natural word lives at an and has an a-coprime denominator. The 73/15→73/11 toy succeeds; 193/39 with a=3 fails to descend; 8/131 at m=13 fails the extra 2-adic integrality bit. The complete census tests all three behaviours rather than only selecting successes.

**Rejected first conjecture (CERTIFIED false).** “Every eligible prime has a marked source on the dyadic a=1 face, or a drop/repartition edge.” Thirty-five primes ≤10,000 refute it. Thus this must **not** be offered as the next unproved arithmetic input.

**Open implication / Assessment.** A useful extension would need a new fixed-n move from some of the surviving a>1 or odd-ℓ faces, together with a theorem that all-radius-one avoidance of the enlarged graph is incompatible with prime n. Its hypotheses must be specified and must exclude 8/131,8/241 and the numerator-15 failures. Counting many radius-one windows alone cannot suffice: 193 has five and 2113 fifteen, yet no current edge; 8/131 has thirteen complete residual ones with no target at all. No threshold or monotone potential forcing the needed mark is identified. Testing a new move on these obstructions is meaningful; conjecturing that an unspecified graph connects to a known zero is not.

## 6. Verdict and replay

**Verdict: PARTIAL, promise 1/5.** A restricted, numerator-sensitive transport is proved and independently checked: **2-overflow plus quotient a=1 folds for 4, with no further divisor search**. This is the most useful finding. It does not give free transport for every 2-overflow, and its global availability is false. The present folding/drop/repartition dictionary **COLLAPSES as an all-prime strategy**, not the entire transport programme. Beyond these moves the exact missing implication is a prime-specific, fixed-n mechanism forcing a transferable marked boundary configuration across a growing family. The remaining class/quotient forcing is B2 again.

**Concrete next steps / Assessment.** Any further move should first handle 193/39 (dyadic, a=3), 2113/43 (odd overflow and square-cap ∞), and a radius-one source at 2521 without consulting a precomputed zero. Require an explicit preservation-of-n and integrality proof. Then run it on the full four numerator-8 and 27 numerator-15 residual controls, stating which residual/shaped dictionary it uses. A new larger census without such a move has little theoretical value.

**Reproducibility (CERTIFIED executions).** All Python uses uv; both runs have a 2 GB virtual-memory bound and a five-minute timeout. Work is streamed by fibre; the verifier retains only the 3,175 radius-one records, not a Cartesian product of windows and residues. Its second census checks the missing rows as well as the saved witnesses. Existing tests already cover δ/BFS, square caps, and z46 minima; these scripts instead certify the new marked profiles and transport conditions.

```sh
ulimit -v 2000000
timeout 300 uv run --with python-flint python scripts/z47_delta_transport_scan.py
timeout 300 uv run --with python-flint python scripts/z47_delta_transport_verify.py
```

Own files: `DELTA_TRANSPORT.md`; `scripts/z47_delta_transport_{scan,verify}.py`; `data/z47_delta_transport/{fibres.jsonl.gz,scan.json,verify.json}`. No pre-existing file is changed.

## 7. External-2 folding (board #4 addendum, 2026-10-19)

**Attribution / scope.** Board `20261019-es-propagation`, argon-2, with Astra's terminology and Type-II identification and Fable's filter audit (round 3). This adds moves, not a new certificate family. At **odd K**, 2 is absent from K's support: adjoining it is an **external-2 mark**, NOT an internal δ=2 mark. In particular it does **not correct §3.3**: that section correctly describes moves restricted to primes already dividing K. Nor does testing the absence of δ=0 establish exact distance two.

**Proposition 7.1 (PROVED).** Let positive integers satisfy

    k ≡ 0 (4), m = kK−n > 0, gcd(m,n)=1,
    s ∈ {2,4}, K = huv/s, gcd(u,v)=1, hv odd,
    k | u, u+v = am, a ≥ 1.

Put t=kh/s and qₐ=n−(a−1)m=tuv−u−v. If qₐ>0, then

    X = (u/k)(tv−1), Y = qₐtu/k, Z = qₐtu(tv−1)/k

are positive integers representing k/qₐ, with zero-distance target window v. At a=1 this is a fixed-n fold and v<m.

*Proof.* qₐ+v=u(tv−1)>0, and direct addition gives

    1/X + 1/Y + 1/Z = k/[u(tv−1)] + kv/[qₐu(tv−1)] = k/qₐ.

Also gcd(v,qₐ)=gcd(v,u)=1. The divisor tv−1 of X is −1 modulo v, giving a zero-window ratio certificate; explicitly D=X(tv−1) divides X² and D≡−X (mod v). At a=1, v<u+v=m. ∎

**PROVED, the additional odd-t case.** For k=s=4, t=h is odd and v₂(u)=v₂(K)+2, so 4|u is automatic, including odd K. The marked integer D₀=Ku/v=hu²/4 satisfies D₀|4K² and D₀≡−K (mod m). When K is odd it introduces the external prime 2. When K is even its 2-exponent exceeds that in K² by two, but the *minimum* internal distance need not be two. The old s=2 case has t=2h and v₂(u)=v₂(K)+1, with even K. For p≡1 (8), odd K means m≡3 (8).

**PROVED numerator-8 control.** With k=8,s=4 and K odd, u has exactly two factors of 2, whereas t=2h and tv−1 is odd; X is a half-integer. A genuine control is n=241, m=39, K=35, (u,v,h,a)=(4,35,1,1): D₀=4 is an external mark, but X=(241+35)/8=69/2. Thus this automatic folding fails at 8/241. The earlier internal-overflow failure at 8/131 remains unchanged. At numerator 4, an a=1 source cannot occur at an odd square: its folded output has gcd(n,X)=1 and n|Y,Z, contradicting T1.

**PROVED quotient behaviour, not exceptional-set propagation.** At a>1 the *unscaled* construction solves qₐ, provided it is positive, not n. Alternatively multiplying the original equation by a gives an=(at)uv−u−v, hence a fold for an; its first denominator (u/4)(atv−1) is coprime to a, so cannot be divided by a when a>1. Neither operation repairs fixed-n descent. At the old source (n,m,K)=(193,39,58), (s,u,v,h,a)=(2,116,1,1,3), the unscaled word is 115=2·116·1−116−1 and

    4/115 = 1/29 + 1/6670 + 1/6670.

This coexists with §3.3's different fold for 4/579; it is not a solution transport back to 193.

**CERTIFIED independent census.** `scripts/z48_closure_verify.py` enumerates words by u and divisors of p+u, rather than either seat's m- or K-loop. For all 143 primes p≡1 (24), p≤10⁴, m≤p, it checks the absence of a source zero and verifies all **542** marked identities:

| move | source fibres | primes covered |
|---|---:|---:|
| old s=2, t≡2 (4) | 250 | 99 |
| added s=4, t odd (either parity of K) | 281 | 111 |
| union | — | **131** |
| added case restricted to odd K | — | **93** |

The union gains 32 primes, but still misses 193,313,1009,1201,1321,1873,2161,2521,2833,3313,4513,5689. Dropping the no-zero exclusion filter gives **137/143** for the union word family. The filter is not a source-forcing mechanism. Examples include 433 at (m,K,u,v,t)=(27,115,4,23,5), and 2113 at (167,570,152,15,1). These counts concern folding alone, not the old folding-plus-repartition count 108.

**PROVED dictionary / Assessment.** At numerator 4 every folded target for N=qₐ has the existing ET-II parameters

    (a,b,c,d,e) = (1,tv−1,t,u/4,v),
    a+b=ce, 4abd=N+e, (X,Y,Z)=(abd,Nacd,Nbcd).

Thus the output belongs to the **a=1 Type II** family (the a here is an ET parameter, not the source quotient). Global availability is still a B2 divisor-class problem. **Verdict: PARTIAL, promise 1/5; no new (P)/(G) route.** Replay and data: `PROPAGATION_CLOSURE.md`, `data/z48_closure/{folds,summary}.json`.
