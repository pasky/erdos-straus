# z45_prime_t1_dual — dual certificates, subgroup obstructions, and budget holes

## 0. Summary

**Assessment.** Real failures admit useful *partial* character explanations, but the character-kernel explanation is provably incomplete on almost every failure tested. At 8/131, only 6 of the 33 complete first-denominator fibres admit any kernel-separating character; the other 27 fail solely because available prime exponents are too small. No single quadratic kernel character kills more than one fibre. This does **not** make the failures incompressible: a bounded-image quartic character modulo 5 explains four fibres, and an exact quotient-congruence certificate exists fibre by fibre. We distinguish these two notions of duality, correct the proposed compatibility premise (T1's varying characters are not a projectively compatible family), and give a scoped no-prime-T1 theorem: at every prime, an unrestricted residual window defeats **all** kernel-annihilating characters simultaneously. This last theorem does not put that window in the finite ES box. All 53 supplied numerical failures are reproduced; rooted forest failures are distinguished from actual five-slice failure.

**Verdict: PARTIAL — the missing implication is from unbounded subgroup escape to bounded-exponent, height-admissible escape. Promise: 1/5. ES remains open.**

**Attribution / novelty audit (Assessment).** Read FRONTIER §§2–7, BRAINSTORM index, DISPROOF_AVENUES, CLASS_FORCING §§1–2, PARITY_AUDIT §0, LOWER_TAIL_ASTRA, and z38_numerator8_control. Searches for “dual certificate”, “prime T1”, “Farkas”, and the failure lists located z32_prime_T1, s9_disproof_class_layer, z27_pretentious_dual, CAP_POINTWISE and CLASS_FORCING. Subgroup versus exponent-budget separation is already central there. The increment here is the explicit dual hierarchy, minimum-quotient/conductor audit on real failures, and the measured obstruction decomposition—not a new existence mechanism or a new general character-duality theorem.

## 1. Exact dictionary and definitions

### 1.1 Finite primal searches

**PROVED (elementary, classical two-unit-fraction factorisation).** For a sorted solution of m/n, write x ≤ y ≤ z. Then

`n/m < x ≤ 3n/m`.

Reduce `(mx−n)/(nx)=a/b`, with gcd(a,b)=1. The remaining equation is equivalent to

`(ay−b)(az−b)=b²`.

Thus the x-fibre succeeds precisely when a divisor d of b² satisfies

`d ≡ −b (mod a),  d ≤ b,  (d+b)/a ≥ x`.

Indeed set y=(d+b)/a and z=(b²/d+b)/a. The complementary divisor has the same required residue because gcd(a,b)=1. Conversely a sorted solution gives such a d. This works also at composite n, so it genuinely decides all 32 PW numerator-15 exceptions, not only Type I/II shapes. Modulus a=1 is allowed; its group is trivial.

**PROVED (range calculations).** Our other complete searches are:

* (★): `N=n+u, M=4u, r=−1`, for positive u with `4u²−2u ≤ n`. Swap u,B in `n=4uBC−u−B` to get u≤B, whence this bound. Any residue hit gives a valid (★) triple, even if its chosen u is not the smaller coordinate.
* b=1: `N=n+4d, M=4d, r=−1`, with d≤(n+3)/8, requiring the divisor w<N. For n≡1 mod4, N itself cannot have the target residue. A proper target divisor has odd cofactor ≥3; hence `n+4d ≥ 3(4d−1)`. This proves completeness of the range.

These are different slicings with different fibre counts. None of the tables below counts the hypothetical ≍log³p successful ES events; it counts all fibres in an explicit finite search.

### 1.2 Three levels of dual certificate

**Definition.** For unit target r in G=(Z/MZ)*, strip the prime factors of N that divide M; they cannot occur in a target divisor. Write the remaining integer as ∏ℓ_i^{e_i}, and put

`S_e = {∏ ℓ_i^{j_i} mod M : 0≤j_i≤e_i}`,  `H = ⟨ℓ_i mod M⟩`.

1. A **kernel-character dual** is a character ψ of G with ψ(ℓ_i)=1 for every i but ψ(r)≠1. Its proof is independent of the exponent budget. A global kernel dual assigns such a certificate to every fibre in the specified search.
2. A **bounded-image character dual** has `ψ(r) ∉ ∏_i {1,ψ(ℓ_i),…,ψ(ℓ_i)^{e_i}}`. It need not annihilate the generators. Several characters can be used jointly, retaining the same exponent vector across them; testing each character separately loses this correlation.
3. A **quotient-congruence dual** consists of f|M and the finite reachable residue sets modulo f showing `r mod f ∉ S_e mod f`. We minimise f exactly. A height certificate can additionally exclude all residue hits by the inequalities in §1.1. Together, these yield a complete finite proof system, but not automatically a short one.

**PROVED (elementary finite abelian duality).** A kernel-character dual exists iff r∉H. If r∈H, every character trivial on the generators is trivial on r, so **no number of such characters helps**. If r∉H, decompose the nontrivial element rH in the finite abelian group G/H into cyclic coordinates and take a character nontrivial on one nonzero coordinate. One character suffices.

**PROVED (finite certificate mechanism).** Starting with S₀={1}, compute `S_i=⋃_{j=0}^{e_i} ℓ_i^j S_{i−1}`. Listing these sets and checking that the target is absent is a locally verifiable dual certificate at one fixed n. It is the reachability-cut version of a finite infeasibility certificate. No appeal to Farkas' lemma is needed; an LP relaxation can lose the integral exponent constraints. Taking f=M is complete for residue nonexistence. Therefore existence of this broader kind of dual is just failure of the corresponding divisor search, not an explanation of why failure occurs.

**Definition (measured simplicity, not Kolmogorov complexity).** We record the least conductor of a *quadratic* kernel separator; if no quadratic separator exists but r∉H, the smallest reduction modulus supporting any kernel separator; and, independently, the smallest f|M separating the bounded divisor image. These are exact minima in the stated classes. We do **not** claim a globally shortest proof, or a minimum number of arbitrary bounded-image characters. In quadratic rows the reported conductor is not asserted minimal among characters of every order.

### 1.3 T1 is an instance—but not of literal projective compatibility

**PROVED (T1 in the kernel-dual language).** In the Type I/II e-slices for an odd square n=m², e≡−n≡3 mod4. The integers to factor are respectively `(ne+1)/4` and `(n+e)/4`, and the target is the ratio −1 modulo e. The primitive/imprimitive odd quadratic character `χ_{−e}` is 1 on every relevant unit prime factor of either integer, and is −1 on the target. In the actual Type II locus gcd(e,n)=1 follows from the denominator prime to n, so all its slice factors are units; Type I has gcd(ne+1,e)=1 automatically. For an odd prime ℓ dividing the Type II integer, `−e≡m² mod ℓ`; for Type I, `−e≡m^{-2} mod ℓ`. These are unit squares. If 2 divides the slice integer, m²≡1 mod8 forces e≡7 mod8, so χ_{−e}(2)=1 as well. Ratios of divisors remain in the kernel. Thus the same reciprocity rule kills all these fibres. The necessity of the e-slice conditions is the ET dictionary in FRONTIER; this reproduces ET Proposition 1.6, not a new T1 proof claim. It says nothing against mixed/scaled ES solutions at squares.

**PROVED (compatibility correction).** Suppose “compatible” literally means ψ_{M'}=ψ_M pulled back under reduction whenever M|M', for all positive M divisible by 4. Every ψ_M must then be induced from ψ₄. There are only the trivial family and the χ_{−4} family. T1's side characters χ_{−4u} do **not** satisfy this: χ_{−4}(3)=−1 whereas χ_{−8}(3)=+1. The appropriate notion is a *single reciprocity formula producing different characters*, not one projectively compatible Dirichlet character. This distinction is essential before attempting a no-prime-T1 classification.

## 2. What the mechanism can do at one prime

**PROVED.** Everything in §1 is pointwise, including subgroup computation and the bounded residue-set proof. The input includes the actual factorisations at the prescribed n. There is no average over primes, levels, or residues. The expense is that the number of fibres and their moduli grow with n.

**PROVED (scoped no-prime-T1 theorem, relative only to Dirichlet's theorem on primes in reduced progressions).** Let p be an odd prime, and m a positive integer coprime to p. In the *unbounded* residual family `x>p/m`, there is a fibre which admits no kernel-character dual of any order, nor a family of them.

*Proof.* Choose a prime q satisfying `q≡−p (mod m)` and `(p/q)=−1`. Such q exist: fix a compatible odd class modulo lcm(4,m); the additional free nonzero class modulo p can prescribe the Legendre symbol via quadratic reciprocity, since p∤m. CRT gives a reduced progression, and Dirichlet supplies q. Set x=(p+q)/m. Then `(mx−p)/(px)=q/(px)` is reduced, since q∤px. In G=(Z/qZ)* the prime p is one of the generators of H=⟨prime factors of px⟩. As p is a quadratic nonresidue, its order is even, so its powers contain −1. Consequently `−px∈H`, and §1.2 excludes every kernel-annihilating character. ∎

**Assessment / exact scope.** The m=4 group argument is already present, in stronger constructive cap language, in CAP_POINTWISE Theorem 1.1 and POINTWISE_SIZE's window argument. The formulation here extends the *negative conclusion about all kernel characters* to any coprime numerator. It does not require q to lie below 2p, and therefore does not guarantee x≤3p/m. It also supplies unlimited prime powers rather than divisors of (px)². Removing either caveat is nontrivial. In particular this theorem is consistent with 8/131 and 15/137. It is **not** a theorem that every finite-box prime dual is impossible.

**PROVED relative to the cited repository result.** SYNTHESIS_SPARKS9 Proposition 2.2 already excludes the single BL character as an all-level obstruction at every nonsquare. The theorem here concerns arbitrary-order *kernel* characters at a suitable residual window; it must not be misreported as a new proof of that older result, or as excluding budget-sensitive characters.

## 3. Exact experiments and hand-checkable examples

### 3.1 Protocol and validation

**CERTIFIED (exact finite computations).** `z45_prime_t1_dual_scan.py` exhausts all relevant fibres for the 4 numerator-8 failures, all 32 numerator-15 entries in Pomerance–Weingartner, *Exceptions to the Erdős–Straus–Schinzel conjecture*, November 20, 2025, Table 1 (`sources/pw.txt`), all 14 (★) failures, and all three b=1 failures. Each gets a nearby successful prime control, selected reproducibly with seed 45017; the two line controls match n mod24. Controls for composite/small numerator-15 failures are not matched composite denominators, and some tiny controls are not close in relative size.

Rows are classified **Q** (quadratic kernel separator), **H** (higher-order kernel separator but no quadratic one), **B** (target in H, absent from the bounded divisor image), or **hit/height**. All failure rows are Q/H/B; none needs a height-only exclusion. Minimal quadratic conductors enumerate all negative fundamental discriminants dividing the modulus. Since the target is −1 or −b with b generated by the factors, every kernel separator must be odd; positive fundamental discriminants cannot help.

**CERTIFIED validation.** A separate direct y-loop agrees with the factorisation decision on all 297 inputs m∈{4,8,15}, 1≤n<100. Seven odd-square (★) fixtures have every fibre quadratically killed. A separate multi-source graph search and direct divisor enumeration verify subgroup obstruction and minimum quotient on all four numerator-8 failures, (★) at 409, and 15/8. Hand computations below check both a budget hole and a genuinely quartic separator. These are finite exact results; the inference “failures look like lottery failures” remains only Assessment.

**Reproducibility.** Runs use `ulimit -v 2000000; timeout 240 uv run --with python-flint python scripts/z45_prime_t1_dual_scan.py`; the report uses `uv run python`, and the independent toy uses `timeout 30 uv run --with python-flint python scripts/z45_prime_t1_dual_toy.py` under a 1 GB address-space cap. No Cartesian-product arrays; factor lists, bounded divisor lists and subgroup sets are processed one fibre at a time. Raw failure rows, summaries, controls' aggregate statistics, forest components and toy output are under `data/z45_prime_t1_dual/`.

### 3.2 Full numerator failures

**CERTIFIED.** For numerator 8:

| n | complete x-fibres | Q | H | B | best single quadratic kernel character | successful control: hit/Q/H/B/height |
|---|---:|---:|---:|---:|---|---|
| 11 | 3 | 1 | 0 | 2 | χ₋₇: 1 | 19: 2/0/0/2/1 |
| 17 | 4 | 1 | 0 | 3 | χ₋₁₅: 1 | 29: 1/1/0/5/0 |
| 131 | 33 | 6 | 0 | 27 | six distinct characters, 1 each | 149: 6/6/0/24/1 |
| 241 | 60 | 26 | 0 | 34 | χ₋₁₅: 3 | 251: 5/10/1/47/0 |

At 131 the six quadratic conductors are 31,47,71,79,23,87, at x=28,34,43,46,48,49 respectively. Thus **even infinitely many kernel characters cannot account for the other 27 fibres**. The 33 fibres contain 1,077 raw divisors of their b² integers; the six Q fibres contain 204. These are different counts from sorted candidate triples.

**PROVED / hand-checkable budget hole at 8/131.** At x=17,

`8/131−1/17 = 5/2227`,  `2227=17·131`.

Modulo 5, the available divisors of 2227² have residues `{1,2,4}`, whereas −2227≡3. But 17≡2 generates all of (Z/5Z)*. A kernel dual is impossible; one extra factor of 17 reaches 2³=3. A faithful quartic character modulo 5 *does* separate the bounded images. This is a short **budget-sensitive** explanation, not evidence of incompressibility. The same quotient modulo 5 kills x=17,22,37,47: four of the 33 fibres. This is why “no single kernel character” must not be upgraded to “no character explanation”.

**CERTIFIED.** The smallest quotient-congruence certificates at 131 use 27 distinct moduli for 33 fibres. The sum of their binary lengths is 195 bits, versus 234 bits for the original moduli; at 241 the corresponding figures are 46 distinct moduli and 385 versus 477 bits. These count modulus fields **only**, not a whole certificate's length or the factorisation input. They demonstrate some compression but no universal tiny modulus.

**CERTIFIED.** All numerator-15 failures, with counts Q/H/B and the maximum coverage of a single quadratic kernel character (ties choose smallest conductor):

| n | Q/H/B | best character: covered fibres |
|---|---|---|
| 1,2,3,4 | 0/0/0 each | no x possible; 15/n>3 |
| 8 | 1/0/0 | −7: 1 |
| 16 | 1/0/1 | −7: 1 |
| 17 | 0/0/2 | none |
| 19 | 0/0/2 | none |
| 23 | 2/0/1 | −7: 1 |
| 31 | 1/0/3 | −11: 1 |
| 34 | 0/0/4 | none |
| 47 | 1/0/5 | −11: 1 |
| 53 | 3/0/4 | −7: 1 |
| 61 | 2/0/6 | −52: 1 |
| 79 | 4/0/6 | −43: 1 |
| 113 | 6/0/9 | −7: 2 |
| 122 | 2/0/14 | −52: 1 |
| 137 | 6/1/11 | −7: 1 |
| 151 | 7/0/13 | −7: 1 |
| 197 | 8/0/18 | −7: 2 |
| 226 | 8/0/22 | −7: 4 |
| 233 | 9/0/22 | −7: 4 |
| 271 | 7/1/28 | −43: 1 |
| 541 | 24/0/48 | −7: 6 |
| 1103 | 46/1/100 | −7: 11 |
| 1171 | 51/1/104 | −7: 13 |
| 1367 | 54/1/127 | −7: 13 |
| 4201 | 161/9/390 | −7: 35 |
| 6301 | 266/1/573 | −7: 53 |
| 12601 | 441/30/1209 | −7: 103 |
| 16831 | 535/32/1677 | −11: 69 |
| 20521 | 740/41/1955 | −7: 163 |

**PROVED / positive structured example.** 15/8 really has a one-character explanation: x must be 1, leaving 7/8; powers of 2 modulo 7 lie in {1,2,4}, while −8≡6. χ₋₇ kills the only fibre. Of the 32 failures, four are empty by the real bound, this one has a complete kernel dual, and the other **27 have no complete kernel dual in our class** (CERTIFIED). Thus a blanket “all sibling failures are unstructured” conclusion is false.

### 3.3 Line failures: a character layer survives, but never explains everything

**CERTIFIED.** Every supplied line failure has B>0, so none has a complete kernel-character dual, of any conductor or order, in these complete searches.

| (★) n | Q/H/B | largest single quadratic coverage |
|---|---|---:|
| 409 | 8/0/2 | 3 (−8) |
| 577 | 8/0/4 | 4 (−4) |
| 5569 | 28/1/8 | 10 (−4) |
| 9601 | 33/1/15 | 12 (−4) |
| 23929 | 46/1/30 | 17 (−4) |
| 83449 | 99/3/42 | 31 (−4) |
| 102001 | 102/4/53 | 25 (−4) |
| 329617 | 172/9/106 | 52 (−4) |
| 712321 | 282/8/132 | 76 (−4) |
| 1134241 | 310/15/207 | 92 (−4) |
| 1724209 | 421/17/218 | 121 (−4) |
| 1726201 | 416/16/225 | 114 (−4) |
| 5212561 | 720/33/388 | 188 (−4) |
| 8813281 | 911/22/551 | 242 (−4) |
| b=1: 193 | 16/0/8 | 12 (−4) |
| b=1: 2521 | 238/4/73 | 136 (−4) |
| b=1: 66529 | 6440/99/1777 | 3090 (−4) |

**PROVED / examples.** At (★), n=409,u=4, N=413=7·59 and M=16. Its divisor residues are {1,7,11,13}, missing 15; but `7·59²≡15 mod16`. This is an exponent-budget failure, not any subgroup obstruction. At n=5569,u=13, strip the unusable factor 2 from N=5582=2·2791. Modulo 13, 2791≡9 generates {1,3,9}, missing −1. The quartic character defined by χ(2)=i kills this fibre: 9=2⁸ has character 1 and −1=2⁶ has character −1. No quadratic kernel character works; the minimum all-order separating reduction modulus is 13. Thus higher-order characters really occur, rather than being ruled out by BL's order-two Brauer group.

**CERTIFIED, controls aggregated; Assessment, interpretation.** Counts across all tests:

| family | failures Q/H/B | successful controls Q/H/B | controls' hit/height |
|---|---|---|---|
| full 8 | 34/0/66 | 17/1/78 | 14/2 |
| full 15 | 2386/118/6354 | 1123/192/7533 | 156/9 |
| (★) | 3556/130/1981 | 3233/144/2169 | 147/0 |
| b=1 | 6694/103/1858 | 6081/181/2481 | 20/0 |

Failures often have more Q fibres, but budget holes dominate full numerator failures and remain numerous in both lines. The simplest fixed character does not sharply distinguish failures: at the largest (★) failure χ₋₄ covers 242 fibres, versus 244 at its successful control 8975377; at b=1, 3090 versus 3123 at control 67273. This is a selected small sample, dominated in pooled tables by large inputs, with only one control per failure. It does **not** establish random independence, a zero law, or absence of another compressible invariant. It does establish the concrete inadequacy of kernel duals on these individual inputs.

### 3.4 Forest failures: scope matters

**CERTIFIED.** We recompute the first 16 root-1 failures listed in LOWER_TAIL_ASTRA, its eight four-prime fixtures, and the six least-nonresidue-root failures. At 409, comp(1) has 15 vertices and 14 edges, all Legendre colour +1; there are four good edges elsewhere. At each of 12721,16921,19441,24481,49681,61561,104161,229321, comp(1) has exactly eight vertices and seven edges, all colour +1. These have 12,8,9,12,15,21,17,30 good edges elsewhere, respectively. At 1201,2521,3361,5569,7561,9769 the chosen least-nonresidue vertex is isolated. Such failures have a very short component/colour certificate, but **not** a global ES dual.

**PROVED relative to LOWER_TAIL_ASTRA Theorems 3.1 and 5.1.** The four-prime factorisation pattern proves complete root-component sterility; the two-prime pattern at 2521 proves isolation of the least nonresidue. These are genuine structured explanations, already known in the repository, not lottery-only failures. Their infinite occurrence is CONDITIONAL on Dickson, not used in our finite checks.

**CERTIFIED.** Full five-slice failure at 105 has five non-diagonal word edges and no good edge; four lie in comp(1), and one has nonunit endpoints. Thus a unit-vertex Jacobi-colour certificate alone is not a proof for all words at 105. Direct slot testing handles that edge; diagonal words must also be checked (for 105 the only diagonal word is u=v=1,t=107, also bad). At 169 the full five-slice failure is T1. Successful controls 433 and 1249 have 12 and 3 good edges in comp(1), respectively. There are **no actual five-slice prime failures in the cited census**; rooted failures must not be described as such.

**CERTIFIED (additional screens).** (★) at 3361 has one hit fibre among 29, and at 5101441 seven among 1129. Nearby-square fixtures 113=11²−8,137=11²+16,233=15²+8,241=15²+16,281=17²−8,433=21²−8,449=21²+8 all have (★) hits. These small checks support no general near-square theorem.

## 4. FRONTIER §4 screening checklist

Statuses concern the proposed dual programme, not a claim to prove ES. **Assessment throughout**, with references to proved/certified steps above.

| # | status | reason |
|---:|---|---|
| 1 | PASS | T1 is the varying χ₋ₑ kernel rule; the prime escape theorem uses a nonresidue, impossible at a square. Mixed solutions are outside its scope. |
| 2 | PASS | All four full numerator-8 failures are reproduced; unbounded subgroup escape does not assert bounded solvability. |
| 3 | PASS | No numerator-uniform existence or transport law is asserted. Generic dual bookkeeping is permitted to certify genuine failures. |
| 4 | **FAIL** | Moduli a,4u,4d still move with the fibre. Minimum quotient and exponent-budget certificates compute B2; they do not overcome it. |
| 5 | PASS | All decisions are at fixed n. Controls are comparisons only; Dirichlet varies q at fixed p. |
| 6 | N.A. | No main-term/error existence argument, nor power-size final count. |
| 7 | PASS | No two-sided asymptotic or error estimate is proposed. |
| 8 | **FAIL for a bounded-rule upgrade** | The known short shadow/component rules use congruences and specified factorisations. Our complete computation grows with n; it supplies no new uniform rule. |
| 9 | **FAIL for kernel-only sufficiency** | Arbitrary characters detect subgroup exclusion, but target∈H need not mean target∈S_e. Budget-sensitive duals retain exactly the missing class information. |
| 10 | PASS | No pooling of prime factors from different shifts. |
| 11 | N.A. | No signed-to-positive reflection. |
| 12 | **FAIL for the theorem-to-ES upgrade** | Unbounded subgroup escape supplies neither x≤3p/m nor available exponents. No transport theorem is hidden. |
| 13 | PASS | No BM shortcut. Higher fibre characters are not asserted to extend to Br(U_n). |
| 14 | PASS | All 14 and all three line failures checked; 3361 and 5101441 retain actual hits. Rooted failures are kept distinct. |
| 15 | PASS as a diagnostic only | Odd-square controls and explicit small near-square primes are tested; no universal rigidity inference. |
| 16 | N.A. | No thin-family transfer. |
| 17 | PASS as bookkeeping only | Every actual prime factor is used, large ones included. No transparent small-factor covering theorem is claimed. |

## 5. New-theory sketch: a graded dual of the exponent budget

**Definition.** For one fibre define its **overflow distance**

`δ(N,M,r) = min Σ_i max(0,j_i−e_i)`

over nonnegative exponents with `∏ℓ_i^{j_i}≡r modM`; set δ=∞ if none exists. This is a concrete refinement of the existing cap/box viewpoint, not a claim to invent Cayley-graph distance.

**PROVED.** δ=∞ iff a kernel-character dual exists; δ=0 iff the bounded divisor residue is attained. More precisely δ is the directed Cayley distance from S_e to r, with multiplication by each ℓ_i costing one. Split each exponent j_i into min(j_i,e_i) and its excess to prove one inequality; any starting bounded product followed by k multiplications has total overflow at most k, proving the other. Multi-source BFS on at most |G| residues computes δ with O(|G|·ω(N)) work and O(|G|) memory. The unreachable set supplies a kernel obstruction; the distance labels supply a finite budget-sensitive dual proving a positive δ.

**CONJECTURE (a first weak finite-box target, not an ES solution).** For every prime p≡1 mod4, some residual fibre of 4/p with `p/4<x≤3p/4` has δ≤1. This is weaker than ES, which would supply δ=0 together with the height test. No theorem here proves this conjecture, and existing ES verification provides its numerical support automatically; it is not independent evidence. Its purpose is to ask for a *finite-box* improvement over the unbounded subgroup theorem without pretending to have reached cap zero. A height filter must still be retained even at δ=0 in a selected fibre.

**CERTIFIED toy tests.** Among the 27 finite-distance fibres at 8/131, thirteen have δ=1, one δ=2, four δ=3, and the remaining nine have δ in {4,5,5,6,9,10,13,15,18}. The six other fibres have δ=∞. At 8/241, seven fibres have δ=1, 27 have larger finite distance (maximum 19), and 26 have δ=∞. At (★),409, the eight Q fibres have δ=∞ and the remaining two have δ=1,2. At 15/8 the sole fibre has δ=∞. Hence the toy hierarchy genuinely separates global character obstruction, one-exponent near misses, and larger budget holes.

**Assessment / theory needed.** A useful next theorem would bound this finite-box overflow distance or classify simultaneous positive-distance profiles from arithmetic data smaller than the full residue tables. Even δ≤1 would not explain the numerator-4/nonfailure distinction: the failing numerator-8 examples already have distance-one fibres. The unresolved ES step is to force distance zero **and** the height inequalities, not merely to rule out a compatible character family. The broader bounded-image dual system is complete but can be as expensive as the primal search; a compression/inverse theorem for it is entirely open here.

## 6. Verdict, BL, and next steps

**PROVED relative to Bright–Loughran, *Brauer–Manin obstruction for Erdős–Straus surfaces*, Theorems 1.6 and 1.8 (statements checked in DISPROOF_AVENUES).** For n≥2 the positive integral adelic Brauer–Manin set is nonempty and Br(U_n)/Br(Q)≅Z/2. Thus a genuine 4/p failure cannot be certified by a BM obstruction on the whole surface. This does not forbid the explicitly observed quartic fibre certificate, a character on a ray group attached to one fibre, a bounded-exponent proof, or a non-BM integral failure. Such characters need not glue to a global Brauer class. Nor is T1 an obstruction to all ES solutions at odd squares: it obstructs the specified Type I/II loci. The wording in older disproof notes that calls squares “BM-obstructed points” must be read with that restriction, not as contradicting BL's theorem for n≥2.

**Assessment.** A structured prime failure remains logically possible, but “it must have a short prime T1” is a heuristic expectation, not a proved necessity. Finite search could in principle certify a failure without any short invariant. What we can now exclude exactly is a complete kernel-character explanation for every named prime line failure and all four numerator-8 failures. We cannot exclude bounded-image characters or another arithmetic compression of the budget holes.

**Final verdict: PARTIAL; promise 1/5.** Kernel-only instantiations COLLAPSE at r∈H but r∉S_e; the unrestricted no-prime-T1 theorem stops at B2/B-fin, before both the exponent and height budgets. The full dual programme is not disproved.

**Concrete next steps (Assessment).** First, optimise bounded-image character certificates for 8/131 and 15/20521, rather than merely kernel characters, and compare with many controls matched in modulus cells and size. Second, test a precisely bounded finite-window δ≤1 statement on composite nonsquares that fail Type II, not just primes where ES already supplies δ=0. Third, any suggested “one invariant” should be checked for actual compatibility/gluing and for whether its proof size includes the factorisations; otherwise it merely renames the exhaustive search.
