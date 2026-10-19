# OVERFLOW_DISTANCE — total overflow is not the square-denominator cap

## 0. Summary

**Assessment.** The z45 overflow distance is a useful, computable grading of a specified divisor fibre, but it must not be identified with the existing exponent cap. We fix its original positive-exponent ℓ¹ definition, use a finite, complete Type-II window box, prove its exact denominator interpretation, and separate it from the square-cap hierarchy. **PROVED:** at the actual prime/window `(p,m,K)=(2113,43,539)`, the distance is **1**, while the CAP_DOWN Type-II square cap at that same window is **infinite**. This is a parity-sensitive budget obstruction, not a kernel-character obstruction. **CERTIFIED:** all 9,732 primes `p≡1 (24)` through 10⁶ and 1,000 sampled primes below 10⁸ have finite-box minimum 0; among 7,668 odd nonsquare composites through 20,000, the minima are `0:7615, 1:47, 2:6`. All four tested numerator-8 controls and all 27 nontrivially budget-obstructed numerator-15 failures have complete-residual minimum **1**, so distance-one-to-zero transport fails very robustly. The known nonresidue-window mechanism gives a growing bound, not an absolute bound. No new pointwise bounded-distance theorem for every prime is obtained.

**Verdict: PARTIAL — the exact open implication is a bounded, target-specific overflow hit in a growing finite window family; even distance one does not supply a transport to zero. Promise: 1/5. ES remains open.**

**New / old / failed / open.** New campaign content: the same-window separation at 2113, the exact denominator-size interpretation, and the finite-box composite/PW15 distance census. Old ingredients: Cayley distance and character duality (z45), forced nonresidue windows and all growing cap bounds (CAP_POINTWISE/CAP_DOWN), and the rank-one obstruction. Failed construction: identify distance one with square cap one, then remove the overflow by local-global or pigeonhole. Open: a constant bound for the finite-box minimum at all primes. This is a diagnostic and a precise question, not progress on the ES lower tail.

## 1. Setup and prior work

**Attribution / Assessment.** Read BREADTH_Z45 in full; BRAINSTORM/z45_prime_t1_dual in full, especially §§1,2,5; CAP_POINTWISE, FORCED_WINDOW Proposition 2.1, LONGSHOT_PIGEONHOLE Theorem 2.2, CLASS_FORCING, TWO_POWER_LADDER, POWER_LADDER_ES, and reviews/z45-breadth-review §6. FRONTIER §7.3 asks for the divisor class inside the allowed character coset; §7.13 already asks for bounded caps. Repository searches for “overflow distance”, “overflow-distance”, “odd overflow”, “cap infinite”, and the `2113/43/539` example locate the z45 definition, CAP_DOWN's precise exponent restrictions, CAP_BOUNDED, and the earlier lattice work. We claim no novelty for finite abelian duality, shortest paths, valuation cancellation, or the distinction between a subgroup and a bounded exponent box. The displayed 2113 example was not found in that search.

### 1.1 One invariant, with the budget included in its input

**Definition.** Let `M≥1`, `gcd(r,M)=1`, and factor the unit part of `N` as

`N_unit = ∏ ℓ_i^{e_i}`,

omitting factors dividing M. Put

`S_e = {∏ ℓ_i^{j_i} mod M : 0≤j_i≤e_i}`,

`δ(N,M,r) = min {Σ_i (j_i−e_i)⁺ : j_i≥0, ∏ℓ_i^{j_i}≡r (M)}`,

with the minimum of the empty set equal to ∞. For `M=1` the trivial group gives δ=0. **S_e is a bounded product set, not usually a multiplicatively closed set.** Its multiplicative closure is the subgroup `H=⟨ℓ_i⟩`.

**PROVED (z45 §5, recalled with proof).** δ is the directed Cayley distance from S_e to r with multiplication by one ℓ_i costing one. Split a vector j into its bounded part `min(j,e)` and its excess: this gives a path of exactly its overflow cost. Conversely a path from a bounded vector produces a vector with overflow no greater than path length. Thus δ=0 iff an actual divisor hits the target; δ=∞ iff `r∉H`, equivalently iff a character trivial on all ℓ_i is nontrivial on r. The last equivalence is character separation in the finite abelian quotient G/H. Multi-source BFS uses at most M states and `O(M·ω(N))` graph work, after computing S_e; computing S_e by bounded products costs `O(M Σ(e_i+1))`. Alternatively reduce each j_i modulo `ord_M(ℓ_i)`: this never increases its cost, so the minimisation is finite. A reachable target is at distance at most `|H|−1`.

**Assessment.** “Character-allowed” here means allowed by **all kernel-annihilating characters of this fibre**, not merely the one Bright–Loughran character, not the full genus approximation, and not existence of a BM-orthogonal adelic point on U_n. Other characters can already obstruct a BM-allowed fibre. Finite δ strengthens subgroup admissibility by measuring a budget defect, but does not supply an arithmetic theorem controlling that defect.

### 1.2 Primary arithmetic instantiation: the finite Type-II window box

**Definition.** For odd `n>1`, use windows

`𝒲(n) = {1≤m≤n : m≡−n (4), gcd(m,n)=1}`, `K=(n+m)/4`,

and define

`δ_m(n)=δ(K²,m,−K)`, `Δ_II(n)=min_{m∈𝒲(n)} δ_m(n)`.

Thus the budget is `e_ℓ=2v_ℓ(K)`. We also distinguish the unrestricted minimum `Δ_II,∞`, with no upper bound on m. A minimum over `m≤L<n` is a *truncated minimum*, not Δ_II unless it is zero or a separate lower bound is supplied.

**PROVED (dictionary; CAP_DOWN Lemma 1.1 at zero overflow).** A divisor `d|K²`, `d≡−K (m)`, gives

`A=(K+d)/m`, `(x,y,z)=(K,nA,nKA/d)`.

All are positive integers: since `gcd(d,m)=1`, d divides KA. The identity is

`4/n = 1/K + 1/(nA) + d/(nKA)`.

Moreover `gcd(K,n)=1`, and n divides y,z. Conversely any Type-II-shaped solution with `x=K`, `y=nY`, `z=nZ` gives `(mY−K)(mZ−K)=K²`, so δ_m=0. Its window obeys `m/K=1/Y+1/Z≤2`, hence `m≤n`. Therefore Δ_II=0 iff this Type-II locus is inhabited. It implies ES, but **is not equivalent to all of ES**, even for a prime unless one assumes Type-II sufficiency. At a composite the distinction is particularly important.

**PROVED (sharper zero-search ceiling).** Every zero-distance window satisfies `3m≤n+4`. Write `d/K=u/v` in lowest terms. The exponent ranges imply `uv|K`, and `m|u+v`. Thus `m≤u+v≤uv+1≤K+1`, giving the bound. This is FORCED_WINDOW Proposition 2.1's least-residue geometry, and it is used only to shorten the zero search. **Positive-distance windows are still searched through m=n.**

**PROVED (T1 at every distance).** At `n=a²` odd and every admissible m, the odd quadratic character `χ_{−m}` is 1 on all primes of K and −1 on `−K`. For an odd prime ℓ|K, `−m≡a² (ℓ)` is a nonzero square; if `2|K`, then `m≡7 (8)` and `χ_{−m}(2)=1`. Since K is generated by these primes, `χ_{−m}(−K)=−1`. Thus `δ_m(a²)=∞` and both Δ minima are ∞. The same argument applies to Type-I side integers `(a²m+1)/4`: for an odd factor ℓ, `−m≡a⁻² (ℓ)`, and the 2-part is identical. This is the known T1 proof in the new notation, not a new square obstruction.

**Assessment.** An invariant that is zero iff **unrestricted ES(n)** holds cannot simultaneously be infinite at every odd square: scaled/mixed solutions at squares exist. We keep T1 by explicitly retaining the Type-II shape. Likewise `e*(a²)` in CAP_POINTWISE can be zero or finite by scaling, whereas Δ_II(a²)=∞; these are different minima over different families.

## 2. Precise questions

**CONJECTURE D1 (finite-box target, not proved).** For every prime `p≡1 (24)`, `Δ_II(p)≤1`.

**CONJECTURE DB (weaker, not proved).** Some absolute D satisfies `Δ_II(p)≤D` for every prime `p≡1 (24)`.

**Assessment.** Neither follows from the known growing cap bounds merely by changing notation. Conversely D1 would not prove ES without a further theorem removing its possibly nonzero overflow. The prime census is not independent evidence for D1: it just reproduces the stronger, already verified Type-II assertion Δ_II=0.

**Question (transport).** Does a numerator-4, prime-specific arithmetic property convert a distance-one window into some zero-distance window? A claim at the **same** window is false at 2113; a claim uniformly over numerators is false at 8/131 and 8/241; a Type-II claim for all odd nonsquares is false at 93 and 3985. Only a substantially more specific, cross-window prime argument remains open.

## 3. Mathematics and experiments

### 3.1 What δ actually measures: denominator prime factors with multiplicity

**PROVED (valuation interpretation).** Fix n,m,K as above, and any `d=∏ℓ^{c_ℓ}` supported on K with `d≡−K (m)`. Use the same formula `(K,nA,nKA/d)` but now allow z rational. Then

`den(z)=∏_{ℓ|K} ℓ^{(c_ℓ−2b_ℓ)⁺}`, where `b_ℓ=v_ℓ(K)`.

In particular

`δ_m(n) = min Ω(den(z))`

in this specific self-supported Type-II rational family. The minimum counts prime factors with multiplicity, **not logarithmic height**. A distance-one witness has a prime denominator, possibly the prime 2.

*Proof.* Since `gcd(nK,m)=1` and `gcd(n,K)=1`, for ℓ|K we have
`v_ℓ(A)=v_ℓ(K+d)`. If `c_ℓ≠b_ℓ` this is `min(c_ℓ,b_ℓ)`; if equal it is at least b_ℓ. Subtracting c_ℓ from `v_ℓ(nKA)` yields exactly the displayed negative valuations. No other prime can divide the rational denominator. Every overflow prime divides both K and A, so `rad(den z)|gcd(x,y)`. Conversely the cost of the exponent vector is Ω of that denominator. ∎

**PROVED (comparison with the old cap; not equality).** The CAP_DOWN/CAP_POINTWISE square-denominator subfamily imposes

- `c₂≤2b₂`;
- for odd ℓ, either `c_ℓ≤2b_ℓ`, or `c_ℓ=2b_ℓ+2a_ℓ` with `a_ℓ≥1`;
- cap `e=max a_ℓ`.

Consequently a window certificate of cap e supported on k overflowing odd primes implies `δ_m≤2ke`. A square-shot certificate of CAP_POINTWISE is an even smaller subfamily, requiring every c_ℓ even. These implications concern **the actual window certificate**, not merely the global number e*(n). No converse bound on the same-window square cap follows from δ, even when δ=1, as the next proposition proves.

### 3.2 An actual prime fibre at distance one and infinite square cap

**PROVED (same-window separation).** Let `p=2113`, `m=43`, `K=539=7²·11`. Then

`δ_43(2113)=1`, but `cap_43(2113)=∞`

for the CAP_DOWN Lemma-1.1 family, allowing arbitrary exponents of **both** available odd primes. This is not merely failure of the square-shot subfamily.

*Proof.* Modulo 43, `ord(7)=6`, `7³=−1`, and `ord(11)=7`. Their subgroups intersect trivially, and together generate all 42 units. The target is

`−K = 7⁵·11` in `C₆×C₇`.

An honest divisor of K² has 7-exponent in `[0,4]`, so it misses exponent 5 modulo 6 regardless of the 11-exponent. Adding one 7 gives `d=7⁵·11=184877`, proving δ=1. At any square cap the permitted 7-exponents are `[0,4]` together with the even integers ≥6; their residues modulo 6 are still only `{0,1,2,3,4}`. The 11-component cannot change this quotient. Thus no cap works. The explicit rational identity is

`4/2113 = 1/539 + 1/9111256 + 7/185944`.

**R-z46 repair (denominator convention):** the rational third denominator is `z=185944/7`, so `den(z)=7`; the summand itself is `7/185944`. Also `7|539` and `7|9111256`. ∎

**Assessment.** This is the most important correction to the proposed interpolation: “extra exponent” and “square denominator-root cap” are not interchangeable. The fibre is unforced: `(K/43)=+1`. CAP_POINTWISE promises finite square cap at **forced** prime windows, so no old theorem is contradicted. Even in the present example H is the entire group, while a budget-sensitive character of its C₆ quotient excludes every square-cap vector. Thus **cap=∞ need not mean kernel-character obstruction**, although δ=∞ does by definition. One cannot require both of those infinity interpretations from the literal existing cap hierarchy.

**CERTIFIED additional toy.** At the forced window `(n,m,K)=(31121,43,7791)`, δ=1 and square cap=1. The z45 Siegel memo already proves the zero-distance hole there. At `(3985,19)` δ=2 and square cap=1, whereas at `(3985,39)` δ=1 via the **even** overflow prime 2. These distinguish total overflow, square parity, and the restriction excluding 2.

### 3.3 What can actually be proved pointwise

**PROVED (one nonresidue gives a total-overflow bound; old mechanism).** If `n≡1 (4)` and q is prime with `q≡3 (4)`, `q∤n`, `(n/q)=−1`, then

`δ_q(n) ≤ (q−3)/2`.

*Proof.* `K=(n+q)/4` has `(K/q)=−1`. Some prime s|K occurs to an odd exponent b and satisfies `(s/q)=−1`. Write `o=ord_q(s)`; since `q−1=2·odd`, o/2 is odd and `s^{o/2}=−1`. Take `d=K s^{o/2}`. Its cost is `max(0,o/2−b)≤(q−3)/2`. The proof allows s=2; unlike square caps, total overflow places no restriction at 2. ∎

**PROVED relative to Pollack's theorem, finite box.** For every prime `p≡1 (4)`,

`Δ_II(p) ≤ floor((p−5)/4)`.

Input: Pollack, *The least prime quadratic nonresidue in a prescribed residue class mod 4*, J. Number Theory 187 (2018), 403–414, Theorem 1, as checked and used in CAP_DOWN Corollary 2.2: there is such a q with `q≤(p+1)/2`. Therefore q is in our **finite** box, and the preceding bound applies. The theorem's attribution and effective scope are taken from that repository source, not a fresh literature verification.

**Assessment / priority.** For `p≡1 (8)` this uses exactly the one-prime cap witness underlying `e*(p)≤(p−5)/8`; multiplying its root-cap cost by two gives the displayed total cost. It is **not a new cap improvement**. It does show precisely that the finite-box minimum is finite at every prime without assuming ES. The elementary graph bound alone would give a weaker O(p) bound once such a q is known.

**PROVED relative to CAP_POINTWISE Theorem 1.3(b), unrestricted windows.** For odd nonsquares `n≡1 (4)`, the same Dirichlet/Linnik construction gives

`Δ_II,∞(n) ≪ rad(n)^5`.

One chooses a reduced class modulo `8 rad(n)` prescribing the required nonresidue and q modulo 8, and invokes Linnik with exponent 5 (Xylouris, 2011, as cited there). **This statement is not a finite-box bound for all composites:** the supplied q can exceed n. At squares the shaped minimum is ∞, unlike the global scaled cap.

**CONDITIONAL on GRH, using the Chebotarev estimate in CAP_POINTWISE Theorem 1.3(c).** For primes `p≡1 (24)`, a forced prime window satisfies `q≪(log p)²`; hence `Δ_II(p)≪(log p)²` for sufficiently large p, when q≤p. The quoted explicit input is `q≤B(p)=(16 log p+70)²`, giving `Δ_II(p)≤(B(p)−3)/2` whenever `B(p)≤p` (in particular for p≥10⁶). The Bach–Sorenson constant is **second-hand / memory-level here**, exactly as flagged in CAP_POINTWISE; we do not promote it to a newly verified explicit theorem. The robust statement is the O(log²p) GRH bound. None of these arguments bounds Δ_II by an absolute constant.

**PROVED (rank-one toy; old cap sharpness in this metric).** For `K=s^b`, odd `m≥3`, and `gcd(s,m)=1`, let `o=ord_m(s)`. If o is odd, δ=∞. If o is even **and** `s^{o/2}=−1 (m)`, then

`δ(K²,m,−K)=max(0,o/2−b)`.

If o is even but its unique order-two element is not −1 in the ambient group, δ=∞. For prime m the displayed condition is automatic. Indeed the target exponents are `j≡b+o/2 (o)`; the smallest nonnegative representative lies in `[0,2b]` iff `b≥o/2`, otherwise its excess is o/2−b. This proves unbounded finite distances at individual fibres, and explains the record δ=32 at `(p,q,K)=(73417,67,18371)`.

**CONDITIONAL on Dickson; not a new obstruction theorem.** Individual **prime-input** fibres can have arbitrarily large δ. Fix a prime `q≡19 (24)` and a primitive-root class for s modulo q, together with `s≡5 (6)`. The two linear forms s and `p=4s−q` on this progression are admissible: at 2,3,q neither vanishes, and at any other prime at most two classes are forbidden. Dickson gives infinitely many prime pairs; then p≡1 (24), K=s, and δ=(q−3)/2. This is CAP_DOWN Proposition 4.1's rank-one sharpness, not a statement about the minimum over all windows. Other windows can, and in tested examples do, have δ=0.

### 3.4 Complete finite-box census and genuine failures

**Protocol.** `scripts/z46_overflow_delta_scan.py` factors one K or residual denominator at a time and uses integer residues and BFS. The primary box is always `m≤n`. For primes a zero found by m≤1000 settles the full minimum exactly. For composites, if the small menu has no zero, **all possible zero windows** are exhausted using `3m≤n+4`; for a putative minimum 2, every window through n is searched to exclude 1. No missing zero is inferred from a truncated scan. Memory is O(M) for one fibre, plus a 10⁶-byte primality sieve, never a product of fibre and group arrays.

**CERTIFIED primary results.** A second engine, `z46_overflow_delta_verify.py`, uses factor-at-a-time weighted min-plus convolution on permutation cycles for distances, and direct Y,Z denominator enumeration for zero witnesses and all 53 composite Type-II failures. It agrees on all 10,732 prime rows and all 7,668 composite minima.

| population | count | distribution of Δ_II | scope |
|---|---:|---|---|
| all primes p≡1 (24), p≤10⁶ | 9,732 | 0: 9,732 | exhaustive |
| primes p≡1 (24), 10⁶<p<10⁸ | 1,000 | 0: 1,000 | seed 46031; 500 each in (10⁶,10⁷), (10⁷,10⁸) |
| all odd nonsquare composites 3≤n≤20,000 | 7,668 | 0: 7,615; 1: 47; 2: 6 | exhaustive |
| odd squares a², 3≤a≤999 | 499 | ∞: 499 | theorem; 201,958 Type-I/II character-fibre checks for m≤1000 |

The six composites with Δ_II=2 are **21,57,105,165,345,561**. The complete 47-value distance-one list is in `scan.json`. In particular **Δ_II(93)=Δ_II(3985)=1**, but neither has any Type-II solution. For 93, the window m=7 has K=25 and d=5⁵, giving

`4/93 = 1/25 + 1/41850 + 5/1674`.

This is a direct numerator-4 counterexample to nonsquare-composite distance-one-to-zero transport. It is not a counterexample to ES, since 93 has mixed/scaled solutions. The earlier `BRAINSTORM/s7_typeII_free_controls` had already identified the Type-II failure set; the increment is its graded distance profile.

**CERTIFIED first-forced-window distribution.** Let q be the least prime `q≡3 (4)` with `(p/q)=−1`. Across the 9,732 primes, δ_q has histogram

`0:8596, 1:431, 2:413, 3:76, 4:20, 5:8, 6:18, 7:1, 8:148, 9:2, 10:2, 20:13, 32:4`.

Thus the least **forced** window is often far from the least successful window. The maximum is 32, first at p=73417, q=67; yet that prime already has a zero at m=3. The least zero-window record through 10⁶ is m=63 at p=87481. In the 1,000-prime larger sample the first-forced maximum is 20 at p=13298041,q=43; every sampled prime has a zero by m=31. These are finite statistics, not a bounded-window conjecture.

**CERTIFIED screens.** All 2,370 Mordell-hard primes in the census have Δ_II=0; their first-forced distances are zero in 1,915 cases and positive in 455. The deterministic near-square stratum `min(p−floor(√p)²,ceil(√p)²−p)≤24` contains 475 primes: all minima zero, first-forced distances zero in 414 cases, maximum 32. All 14 (★)-failure primes and 193,2521,66529 have Type-II zeros here, as do 3361 and 5101441. Selected first zero windows are `193→7, 409→7, 2521→23, 66529→31, 3361→3, 5101441→19, 8803369→107`. A prime **window m** is not the different prime-modulus certificate notion PM-II in FRONTIER; the m=3 witness at 3361 does not contradict that screen.

### 3.5 Numerators 8 and 15: the same invariant on a complete residual search

**Definition.** For numerator k and denominator n, take every integer `n/k<x≤3n/k`, reduce

`(kx−n)/(nx)=a/b`, `gcd(a,b)=1`,

and set `δ_x^res(k,n)=δ(b²,a,−b)`. Let Δ_res be the minimum over these finitely many x; an empty range has minimum ∞. This is the **same function δ**, with a different, explicitly named arithmetic family. It is not the Type-II invariant and need not be infinite at squares.

**PROVED (zero distance needs no sorted-height caveat for existence).** `Δ_res(k,n)=0` iff k/n has a positive three-unit-fraction representation. If `d|b²`, `d≡−b (a)`, then

`y=(b+d)/a`, `z=(b+b²/d)/a`

are positive integers and give the representation with this x. The complementary congruence follows from coprimality. We need **not** impose `y≥x` or sort the resulting triple. Conversely a sorted solution has its smallest denominator in the displayed x-range and yields such a divisor. Therefore the z45 “height-only” category matters for sorted fibre counts, **not** for existence of a representation with that chosen x or for the global zero-distance minimum. This corrects a caveat in the proposed δ≤1 target; it changes none of z45's actual failure rows, which had no height-only fibres.

**CERTIFIED minima.** All four tested numerator-8 controls have Δ_res=1. **R-z46 repair (control scope):** these are `n=11,17,131,241`, not the full numerator-8 exception list; PW Table 1 also lists `n=1,2,3`. Of the 32 PW numerator-15 entries, four (`n=1,2,3,4`) have empty x-range, `n=8` has its only fibre kernel-obstructed, and **every other one of the 27 failures has Δ_res=1**. The verification engine independently constructs one extra-prime divisor and checks the rational identity in each of these 31 distance-one failures. Zero absence agrees with z45's complete, independently reviewed classifications.

| k/n | fibres | δ=∞ | δ=1 | other positive finite | maximum finite δ |
|---|---:|---:|---:|---:|---:|
| 8/11 | 3 | 1 | 2 | 0 | 1 |
| 8/17 | 4 | 1 | 2 | 1 | 3 |
| 8/131 | 33 | 6 | 13 | 14 | 18 |
| 8/241 | 60 | 26 | 7 | 27 | 19 |
| all 32 PW15 entries | 8,858 | 2,504 | 185 | 6,169 | 547 |

**Label qualification.** The four numerator-8 distance profiles reproduce the already independent z45 divisor/BFS toy and are CERTIFIED. The PW15 **minima** are independently checked as just described; the entire positive-distance histogram and its maximum 547 are **EVIDENCE (one new full-distance engine)**, not a second independent certification of every distance. Its obstruction counts `2,504=2,386+118` and 6,354 finite budget holes agree with the old quadratic/higher/budget census. At 15/20521, 31 of 2,736 fibres have distance one, while 781 have infinite distance.

**PROVED / hand check.** At 8/131, x=17 gives `a=5`, `b=2227=17·131`. Bounded divisor residues are `{1,2,4}`, missing −b≡3. One extra 17 gives `d=17³`, and

`8/131 = 1/17 + 1/1428 + 17/11004`.

The genuine numerator-8 failure remains: this is not three reciprocal integers. The added prime is tied to both first and second denominators. Hence neither “no kernel dual” nor “one extra exponent suffices” distinguishes ES from the real sibling failures.

## 4. FRONTIER §4 checklist

**Assessment throughout.** PASS means the stated diagnostic respects a screen, not that an ES proof passes it.

| # | status | exact reason |
|---:|---|---|
| 1 | PASS | χ₋ₘ kills every Type-I/II square fibre at every overflow; scaled/mixed solutions are excluded from the primary family. |
| 2 | PASS diagnostic; FAIL transport | 8/131 and 8/241 have Δ_res=1, never 0. Thus a numerator-blind one-to-zero implication is false. |
| 3 | FAIL for a uniform positive law | The bookkeeping is numerator-uniform; a zero-forcing theorem cannot be. All 27 budget-obstructed PW15 failures also have minimum one. |
| 4 | FAIL | Modulus m=4K−n remains tied to the factored integer. Positive δ removes no divisor-class requirement at zero. |
| 5 | PASS | n is fixed in all existence arguments; Dirichlet/Pollack varies the auxiliary q. No across-n average is used to recover a prescribed n. |
| 6 | N.A. | No main-term/error claim or power-size final-object count. BFS complexity is not a solution main term. |
| 7 | PASS | Only upper bounds on distance and one-sided existence targets; no forbidden two-sided asymptotic. |
| 8 | PASS definition; FAIL fixed-menu upgrade | The finite box grows with n. An absolute window menu remains barred; no conjecture asserts one. |
| 9 | FAIL as an existence mechanism | Kernel escape gives δ finite, not zero. The 2113 C₆ quotient demonstrates budget-sensitive class information beyond the subgroup. |
| 10 | PASS | No products or large-prime collisions are pooled across different K. |
| 11 | N.A. | All reconstructed terms are positive; no reflection from signed solutions. |
| 12 | FAIL | A distance-one witness has a rational third denominator; neither square-cap repair nor transport to cap zero is supplied. |
| 13 | PASS diagnostic; FAIL shortcut | Fibre character admissibility is explicitly distinguished from BM on U_n; the free BM layer does not bound δ. |
| 14 | PASS | All named (★)/b=1 failures, 3361 and 5101441 are tested, with no false assertion that one line suffices. |
| 15 | PASS diagnostic | All Mordell-hard primes and the stated near-square stratum are included; exact squares are infinitely distant. |
| 16 | N.A. | No transfer from Sophie-Germain or another thin family. |
| 17 | PASS computation; FAIL covering route | The computation uses every factor, large ones included. No theorem controls their residues. LONGSHOT_PIGEONHOLE Thm 2.2 still blocks the specified transparent full-coset covering arguments, not single-target hits. |

## 5. New-theory sketch: an overflow profile with parity retained

**Definition / Assessment.** A useful refinement is not another k-th-power ladder but a **joint overflow profile**: for each congruent exponent vector c retain its defect vector `(c_ℓ−2b_ℓ)⁺`, its total mass, its parity at each prime, and whether it uses 2. The primary δ minimises total mass. The existing square cap minimises half the maximum defect on the face “all defects even, defect at 2 zero.” These are different optimisations of the same finite-periodic arithmetic exponent set. This is a reorganisation of known budget geometry, not a claim to invent a general theory of semigroup distances.

**PROVED (first toy theorem).** At a rank-one prime window the total-distance profile is exactly the formula in §3.3; the square-cap face can be empty despite finite total distance. More generally the C₆×C₇ example at 2113 has its nearest target on the odd-defect face and no point anywhere on the square-cap face. The verification script checks 264 rank-one cases and that direct-product example exactly. A parity-blind scalar potential cannot certify square-cap descent there.

**CONJECTURE / required arithmetic input.** D1 is the first genuinely new pointwise target for this grading: find a window in the finite box with total defect at most one for every prime p≡1 (24). A useful inverse theorem would turn simultaneous holes of radius one in **all** these actual factorisation boxes into a square/composite obstruction. Abstract Cayley graphs cannot do this: rank-one fibres have arbitrarily large holes, and actual composite inputs realise simultaneous minimum 2. Such an inverse theorem must use the changing integers `(p+m)/4`, not just their abstract groups or quadratic signs. No candidate arithmetic input proving it is identified here.

**Assessment (why the power-ladder flattening does not settle this).** POWER_LADDER_ES proves all free-Q k-th-power predicates by choosing a convenient auxiliary modulus and allowing unrestricted prime support/size. Here the support is prescribed by K, `rad(den z)|gcd(x,y)`, and the primary window is in a fixed finite box at n. Those conditions are exactly absent from its constructions; §4 of that memo already warns that tied caps do not flatten with the free power ladder. Thus δ is a genuinely nonconstant **fibre diagnostic**, as the census and toy theorem show. It is not proved to be a genuinely new difficulty level between the global truth of ES and the already proved relaxations. The square-cap comparison prevents the stronger claim that it is just the old cap renamed, but supplies no bounded-distance theorem.

## 6. Verdict and replay

**Verdict: PARTIAL, promise 1/5.** The scalar distance is well defined, computable, T1-exact on the stated shapes, and quantitatively separates character obstruction from exponent shortage. The finite-box prime bound is polynomial unconditionally and polylogarithmic under GRH by **existing** forced-window machinery. No absolute bound D is proved. Identifying this distance with the square cap **COLLAPSES at 2113/43**; upgrading distance one to zero by a numerator-uniform or nonsquare-Type-II local-global rule **COLLAPSES on the certified failures**. A prime-specific, numerator-4 cross-window transport is not disproved, but remains B2/B-fin rather than a developed method.

**Concrete next steps / Assessment.** First test any proposed descent on the 2113 parity profile, 93 and 3985, and the 31 real numerator failures with minimum one; these already distinguish the logical claims. If studying D1, work with radius-one **all-window** holes, rather than more prime samples with known zero witnesses. Any claimed theorem must state its window-height bound and whether it controls total overflow, even overflow, or maximum root exponent. Further census extension alone will not establish such a theorem.

**Reproducibility (CERTIFIED executions; Python via uv).**

```
ulimit -v 2000000
timeout 300 uv run --with python-flint python scripts/z46_overflow_delta_scan.py scan
timeout 300 uv run --with python-flint python scripts/z46_overflow_delta_scan.py controls
timeout 180 uv run --with python-flint python scripts/z46_overflow_delta_verify.py
```

Files: this memo; the two scripts; `data/z46_overflow_delta/{primes.csv.gz,prime_samples.csv.gz,composites.csv.gz,scan.json,failures.json.gz,verify.json}` (less than 1 MB total). The verifier reads the pre-existing, reviewed z45 failure records without changing them. All primary minima and the new same-window separation pass independent arithmetic checks. No existing repository file is modified.
