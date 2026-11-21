## §0
Result: At selected primes of prescribed least nonresidue q, every good word and both moduli of every Type II solution need an odd-valuation prime factor exponentially large in a power of q, although a (★) solution exists. Label: PROVED (rel. fixed-modulus prime distribution, Mertens, Brun–Titchmarsh, ET parametrisation and quadratic ideal factorisation for D below; elementary for A,C, BGK/Dickman–de Bruijn/Pólya–Vinogradov/Burgess for B; infinitude in C CONDITIONAL on Dickson).
Scope: Positive relative density inside a finite sign profile for each large q in D, not a height bound in p or a Type I assertion. Exact reverse basin at each prime p≡1 (8); forward saturation at large p with ordₚ(2)≥p^δ for fixed δ>0. A trap for adjoining negative prime factors of p+x and moving between words that retain any one letter. No existence of a *reciprocal* bichromatic pair follows. ES, (S), U₇ and (MS⁺₁₀₅) remain open.
Review: cross-model (`data/z80/xreview/REVIEW_ES_JUGULAR_OPUS.md`, Claude Opus; accepted A–C and censuses, scope/label and replay fixes applied).
Triage: BARRIER-SCOPED
STATUS delta: none

# The cofactor walk: what it can reach, and what it cannot force

**Assessment / screening.** Keep p fixed. Use the character to select actual factors, not to approximate the count of words. The distinction in §§1–3 is between walking on a divisibility arrow and having its reverse at the *same* pair. Items 1–3 and 14 of FRONTIER §4 are screened in the table below. Items 4,5,9: arrows use divisors of this individual shift but do not force the class for the reverse arrow. No relaxation-to-ES, BM or signed-word transfer (11–13), counting asymptotic or finite menu (6–8), factor sharing or large-factor covering (10,17), or model/Brauer obstruction (18–19) is used. The explicit family in §3 kills a method; it is not a thin-family proof transferred to arbitrary p, including near squares (15–16).

## 1. A directed descent without negative shifts

**Theorem A (PROVED, elementary).** Let p≡1 mod 8 be prime, χ the Legendre symbol and q the least positive nonresidue. On the nonresidues in [1,p−1] draw an arrow x→d whenever d divides p+x. There is a directed path from x to q **if and only if x is odd or p+x is composite**. Only positive shifts are used, without imposing any reverse divisibility. The theorem is about existence of a path, not greedy descent in size or running time.

**Proof.** Since χ(2)=1, q is an odd prime. Write [a] for the representative in [1,p−1] of a nonzero field element. First consider the orbit of an odd seed under multiplication modulo p by powers of 2. The odd representatives in it are mutually reachable: x↦(p+x)/2^{ν₂(p+x)} is exactly the first return to the odd representatives under repeated modular halving. This is a permutation cycle on those representatives of the given orbit, including the possibility of a singleton. Every even representative e in the orbit is reachable as well: choose j minimal with 2^j e>p, so 2^j e−p is an odd representative in the orbit and has an arrow to e. This does **not** promise a return from e.

For a fixed odd nonresidue seed let C be the union of the doubling orbits whose odd part (i.e. some odd representative) is reachable. All elements of C are reachable. If z∈C and d<p is a nonresidue divisor of z or of p+z then d∈C: for p+z take its odd divisor d/2^{ν₂(d)} and use the arrow from z. For z itself, the odd representative 2^j z−p in its orbit, with j minimal so 2^j z>p, has that odd divisor of its shift. This proves the assertion for composite d, not just primes. Let H={h:hC=C} be the multiplicative stabilizer in the field. It contains 2 and consists of residues.

Here is the covering step. If H contains 1,…,m−1 and 2, for 2≤m<p, every coset zH has a representative y<2p/m. Among 0,[z],… ,[(m−1)z] on the circle of circumference p two consecutive points have gap ≤p/m. Their difference gives [kz]=d or p−d with 1≤k<m, 0<d≤p/m. In the former case take y=d. In the latter, double d to D in (p/m,2p/m) (strict since p prime and 1<m<p), and take s=⌊p/D⌋. Then 1≤s<m and y=p−sD is positive, <2p/m and in zH. Thus the orientation of the small gap costs a factor two, exactly what the single shift +p permits.

If m is a residue and every coset has such a representative, take any x∈C and apply the bound to (x/m)H. Then my<2p and [my]∈C. Since y is a nonresidue divisor of either [my] or p+[my], it lies in C. By H-invariance x/m∈C; finiteness upgrades inclusion to equality, hence m∈H. Inducting proves {1,…,q−1}⊂H. For m=q apply the same covering to (x/q)H but now take **q itself** as the negative divisor of my=qy, not y. Thus q∈C. Finally, if p+x is composite and x even, its odd prime factors include a nonresidue by multiplicativity. This factor is ≤(p+x)/3<p since p+x is odd and composite. From it the odd-seed result applies. Conversely, if x is even and p+x is prime, x≠q and neither divisor of p+x lies among the vertices, so x has no out-arrow. ∎

**Corollary (PROVED).** Every negative endpoint of an interior bichromatic word can reach q by those arrows: p+x=(tx−1)v is composite. Consequently a reverse search of the one-way graph from q contains a negative endpoint of *every* such word. The reverse basin omits only even prime-shift sinks, so this does **not** localize the witnesses: it is essentially the whole negative half. No existence of a word, reversal of those paths, or reduction to a smaller ES input follows.

## 2. When composite recursion saturates the negative half

**Theorem B (PROVED rel. Bourgain–Glibichuk–Konyagin, Fourier completion, Dickman–de Bruijn, Pólya–Vinogradov and Burgess).** Fix δ>0. At all sufficiently large primes p≡1 (8) with ordₚ(2)≥p^δ, *every* odd negative seed reaches *every* negative vertex, including the even ones as endpoints. Neither a diameter estimate nor an assertion that all p meet the order hypothesis is intended. In fact the hypothesis with any 0<δ<1/2 misses o(π(X)) primes up to X: the exceptions divide ∏_{k≤X^δ}(2^k−1), whose logarithm is O(X^{2δ}).

Use the same C and H. The only covering input needed to adjoin a residue m to H was that each coset of H has least representative <2p/m. Since |H|≥p^δ, the BGK prime-field subgroup exponential sum bound is ≤|H|p^{−η} at every nonzero frequency for some η(δ)>0, unchanged under translation by a multiplicative coset representative. Fourier completion against an initial interval of length B gives count B|H|/p+O(|H|p^{−η}log p). Hence for a fixed 0<γ<min(η,1), B=⌊p^{1−γ}⌋ works. This puts **all** residues m≤p^γ in H at the fixed p. In particular H contains the squares of all primes ≤p^{γ/2}. The integers up to p−1 smooth to that bound have positive lower density (Dickman–de Bruijn at fixed parameter); their squares have at most two preimages each mod p, so |H|≫δ p (constant depending on δ). Its index is now bounded. Gauss sums give a coset discrepancy O(√p log p) by multiplicative character orthogonality and Pólya–Vinogradov; B=⌊p^{2/3}⌋ now suffices. Thus H contains every residue m≤p^{1/3}. If H were proper inside the squares, a coset in the squares disjoint from H would have positive bounded-below density in [1,p^{1/3}]: expand its indicator in the bounded number of characters, and apply Burgess to that interval (e.g. r=4 gives a power saving). For r=4 the error is Oε(p^{21/64+ε}), smaller than the main term of order p^{1/3}. Contradiction. Hence H is the squares, and C, a nonempty union of H-cosets contained in the negative half, equals that half. ∎

**Assessment.** This is pointwise on the stated order range. The many arrows are not putative ES certificates. Only reciprocal arrows at opposite signs and with the interior inequalities give (S); they cannot be counted by the BGK step. In fact every arrow used *inside* C above has equal signs.

## 3. The prime-only recursion can freeze even at an existing word

**Theorem C (PROVED conditionally for infinitude, on Dickson; finite instance CERTIFIED).** At p=113035442521, q=17 is the least nonresidue. If at each visited prime x one adjoins **all negative prime factors** of p+x, the closure from q is exactly {17,607717433}. There is an actual interior word there. Even allowing a move that keeps just **one numerical letter in any position whatsoever** and replaces the others by arbitrary positive interior letters, the word is isolated up to outer reversal. Under Dickson this happens infinitely often with an outer letter growing linearly in p.

Take j≥0 and r=1231553+3063060j with the five primes

    r,  p=186r−17,  S=(11r−1)/6,  L=(31r−1)/2,  K=527r−48.

The progression has p≡1 (840·11·13), r≡5 (17) and r≡2 (9). The least nonresidue is 17 by reciprocity, since p≡−5 mod 17 is nonsquare. Since 186=2·3·31 and (p/31)=(−17/31)=1, all primes dividing 186 are residues at p. Thus p+17=186r forces χ(r)=−1; p+r=17·6S forces χ(S)=+1. These give exactly the stated prime successors for large r.

To check arbitrary slot changes use p+x=(tx−1)v for an outer x, and (tu−1)(tv−1)=tp+1 for a middle t. At outer 17 a neighbor must be ≡5 (17). No divisor of 186 has that residue; the only divisor of 186 that is ≡1 (17) is 1. Thus v=r alone works, t=11. At outer r the other endpoint u obeys u=(p+r)/(tr−1)≤(p+r)/(2r−1)<100 for r>1000; r|p+u requires u=17. At middle 11 the number 11p+1=1116 S has just the complementary pair with factors ≡−1 (11), since among the divisors of 1116 only 186 is ≡−1 and the total is ≡1. At middle 17 similarly 17p+1=6K and no divisor of 6 is −1 (17). At outer 11 one has p+11=12L≡1 (11), with no divisor of 12 in −1 (11). Finally at middle r, uv=186+(u+v−17)/r. Since u,v≥2 give u+v≤uv, we have uv≤186r/(r−1)<187 for r>1000. As |u+v−17|<r, this requires simultaneously uv=186 and u+v=17, impossible. Both endpoints of the only word are negative. It is not an ES certificate from the sign test.

The five affine forms are primitive with distinct positive slopes and nonproportional coefficient pairs (printed below in the replay). For primes >5 each nonconstant reduction excludes at most one residue and primitive constant reductions exclude none. For 2,3,5 the progression step of every form is divisible by the prime and each constant is a unit, as directly checked from the five pairs. Dickson now applies. At j=198 all five are prime by trial division through the square root. This is different from merely isolating a small root in the forest (`Z53_FORESTCLASS.md`): the two negative prime-factor successors are forced indefinitely, and the existing word has no all-slot escape even at the moving letter.

## 4. Falsifier Table and replay

|Screen|A (including corollary), B and C|
|---|---|
|F1 odd squares|A/B have no negative unit seed; the field coset proof is inapplicable. C requires χ(17)=−1, impossible for a square Jacobi denominator.|
|F2: 8/131, 8/241, R₈ at 1590284203561|A/B concern one-way divisibility, **not** an 8- or 4-specific point. 131 is outside 1 mod 8; at 241 and at the large control, a saturated walk would not furnish any reciprocal word, much less one on the even-C line. C has a neutral word only, no numerator implication. The conversion of an actual negative interior word to ES uses the five 4-slots (`DEDEKIND_ES.md`, Thm 4.5), not an 8-slot rule.|
|F3: 4545 and Z₇={105,1465,3865,4545,10305,12145,39361,67425}|All outside the prime hypotheses; in particular the prime-field gap argument does not establish the result for nonunits. No U₇ or Type II existence assertion at these composites.|
|F4: all fourteen (★)-zero primes 409…8813281, composite 17401609|A gives paths wherever its prime/congruence hypotheses hold, B only under its order and size hypotheses. Neither implies even (S) existence; the corollary starts with a word, not a c=1 witness. None meets the C construction (j≥0, r≥1231553). 17401609 is not prime.|

**CERTIFIED (finite only; Opus independently checked the basin to 10⁷ and the span to 10⁵, in addition to full byte-for-byte replays).** For all 3426 primes ≡1 (840) up to 10⁷, enumerate the prime-factor closure from q and test all interior outer stars in it. For factors of p+x alone this misses 454 primes, first 7561. Even adjoining negative primes from p−x misses three, first 21841 (162 visited), last 1726201. An independent question: can formal multiplicativity alone identify the squareclass of q as an F₂-sum of the endpoint products of interior edges? Yes at 3199/3426, including 3361 with no endpoint q, but not at 2521. These are rational squareclasses. Since χ(tu−1)=χ(uv) from p+u=(tu−1)v, a formal sum equal to [q] forces some word to have χ(tu−1)=−1. The 227 failures of the formal sum are not failures of (S). Enumeration fixes a least letter k with k³−2k≤p, factors p+k and kp+1 for its two possible roles, and removes outer reversals. The tests are not premises for A/B. No global failure of (S) was found or is claimed.

```
ulimit -v 6000000
timeout 1800 uv run --offline --no-project python -B scripts/z80_square_span.py 10000000
timeout 1800 uv run --offline --no-project python -B scripts/z80_cofactor.py 10000000
timeout 600 uv run --offline --no-project python -B scripts/z80_jugular_trap.py
```

Outputs: `data/z80/jugular/{span,basin,trap}.txt`. **Assessment / next test.** Reverse reachability alone does not distinguish endpoints from almost all non-endpoints. A sharper candidate is to test which first-return paths from a residue to the negative half have their *first* sign-changing arrow reciprocated; A/B give no such return. A criterion involving a reciprocal arrow rather than still larger basins is needed.

## 5. Escaping the least nonresidue in *prime support*, not just in height

**Theorem D (PROVED rel. PNT in fixed progressions, QR, Mertens, Brun–Titchmarsh, ET's Type II parametrisation and unique factorisation of ideals in a quadratic maximal order).** Write sf for the squarefree representative modulo rational squares. For every sufficiently large prime q there is a positive-relative-density family of primes p≡1 (840) with least quadratic nonresidue q, having an interior (★) word, such that simultaneously:

* For **every** interior good word p=tuv−u−v, sf(uv) has a prime factor >exp(c q^{1/4}), for some absolute c>0.
* For **every** positive Type II parameterisation 4abd=p+e, a+b=ce, **each** of sf(4acd−1) and sf(4bcd−1) has a prime factor >exp(q^{1/15}). More generally any fixed exponent <1/14 works for sufficiently large q.

These large primes need not be nonresidues; the sign may still be carried by q. No relation between p and q beyond the conditions stated, nor any conclusion for every sufficiently large p. The prime factors required here cannot be produced merely by making both endpoints very large squares times a bounded kernel. This differs from the ET period-height and good-denominator bounds of `notes/z78/WILD_ES.md` §6 and `notes/z79/WILD_ES.md` §9; no external priority claim.

**Sign profiles.** Fix Y=exp(c q^{1/4}), and condition the prime variable on p≡1 (840), (p/l)=+1 for odd primes l≤Y other than q, (p/q)=−1. Discard p≤Y. These are compatible reduced CRT classes with fixed positive prime density for each q. Thus χ_p has the asserted least negative. On this probability space each compatible prescribed unit class mod m costs at most

    C₀ 2^{ω(m)} / φ(m)

in relative density by CRT and the prime number theorem for the fixed moduli; the constant absorbs 840. This also bounds the probability of each of finitely many tests jointly by the union bound (summing their individual costs).

**Word calculation.** A small-kernel good word requires q∣uv to odd order, since χ(uv)=−1. For fixed unordered endpoints or even ordered coprime endpoints the input test is a single class p≡−u−v (uv); coprimality holds because any common prime divides p, and both endpoints are <p. Summing the costs over all admissible u,v, without any cap on square parts, is at most

    (C/q) ∏_{l≤Y}(1+4 l/(l−1)²) · ∏_{l>Y}(1+4∑_{j≥1}1/φ(l^{2j})) ≪ (log Y)^4/q.

Indeed at each prime there are two choices of slot and the class cost contributes 2, whereas q is mandatory and its own factor can be bounded by O(1/q). Mertens controls the first product; the second is bounded uniformly. Choose c small enough for this bound to be <1/4. To justify the infinite union in prime density: for fixed q,Y the possible squarefree kernels are finite. At m=uv with Y-smooth kernel there are ≤2^{ω(m)} orientations, ≪ε m^ε. Up to X, uv≤p since t≥2 and u+v≤uv. For T<m≤√X, unconditional Brun–Titchmarsh gives an upper density bound by a constant times the convergent tail ∑_{m>T}2^{ω(m)}/φ(m); here and below such a tail is **restricted to smooth kernels**, m=s h² with s in a finite set. Division by the fixed profile density does not affect its convergence to zero. In √X<m≤X count integers by O(1+X/m) per class; summing over s h² gives o_Y(X/log X) even with the m^ε orientation factor. Take X→∞ before T→∞. This proves that the upper bound by the Euler product really applies to prime inputs, not just to a formal Haar sum.

**Full Type II calculation.** Write Z=exp(q^β), 0<β<1/14 fixed (so Z≤Y eventually). At either orientation f=4acd−1 of a positive solution, f∣cp+a, (f,c)=1. At fixed f the number of possible classes is ≤τ₃((f+1)/4)≤τ₃(f+1) for f≡3 mod 4. Also χ_p(f)=−1 by `Z57_BFII.md` Prop 2.2: (p/f)=(−ac/f)=−1 since f≡−1 (4ac). Thus Z-smooth sf(f) again requires q∣f. Put α=1/log Z. For large q the tilted Euler product satisfies

    ∑_{q|f, sf(f) Z-smooth} 4^{ω(f)} / f^{1−α} ≪ (log Z)^4/q.

Indeed q^α≤e, ∑_{k≥1}4/q^{k(1−α)}≪1/q. At l≤Z the linear term in the logarithm is 4/l^{1−α}=4/l+O(α log(l)/l); its accumulated correction is O(1) by Mertens. The higher powers have bounded mass (α≤1/4); at l>Z only even exponents occur. On a block F≤f<2F, f/φ(f)≪log log(4F), and ∑ τ₃(f+1)²/f≪(log(3F))^8 by τ₃²≤τ₉ and the elementary summatory bound for τ₉. Cauchy–Schwarz now bounds the summed class costs on this block by

    ≪ q^{−1/2} (log Z)^2 F^{−α/2} (log(3F))^4 log log(4F).

Summing F=2^j gives ≪ q^{−1/2}(log Z)^7 log log(4Z)=o(1). This estimate does not pay a fixed-modulus equidistribution error for each growing f: first use it for fixed f≤T. The following tail argument, including the large orientation, is essential.

**Large-modulus tail.** For fixed Z and primes p≤X, use BT for T<f≤√X as before, with weight τ₃(f+1)≪ε f^ε. For √X<f≤X^{3/2}, summing f^ε(1+X/f) over f=s h² still gives o_Z(X/log X). One must *not* continue this argument up to X². Orient f=4bcd−1; since a+b≤2ab, 2abd≤p. When b≤a, f<4b(a+b)d≤8abd≤4X. When b≥a, f<8b²d/e≤2X²/(a²de). Thus f>X^{3/2} implies a²de≤2√X. For each such a,d,e and kernel s the equality f=s h² gives the norm equation

    [d(2b+a)]² − des·h² = d(da²+e) = N > 0.

For a fixed triple there are O(τ(N) log(3X)) possibilities, constant independent of the real quadratic discriminant (for fixed Z). If des is square, factor the difference of squares over the integers. Otherwise the element d(2b+a)+h√(des) is in the quadratic maximal order, and its principal ideal is an integral ideal of norm N. There are at most τ(N) such ideals by prime-ideal decomposition of rational primes. Generators in our range per ideal differ by units; both conjugates are positive, the larger is polynomially bounded in X (indeed <2d(2b+a)), and the least totally positive unit >1 has trace ≥3. This gives the uniform logarithmic bound, without assuming unique factorisation of elements. Summing over O(√X log²X) triples, all with N polynomially bounded, and finitely many s, gives o_Z(X/log X). Thus the density bound applies even to a solution's *larger* f. In all these tail arguments the constant may depend arbitrarily on the fixed sign profile; no such dependence is allowed in the Euler-product estimates.

Finally there is an actual (★) witness on a relative density-one subset of the profile. For an auxiliary prime g≡3 (4), g>max(11,Y), use t=4, u=(g+1)/4, p≡−u mod g; then v=(p+u)/g≥2 eventually and χ(g)=−1 by reciprocity. The relative avoidance density for any finite such set is ∏(1−1/(g−1)), which tends to zero by the divergence of prime reciprocals in this class. Apply the two upper bounds and remove this null set. Natural relative density exists for the avoidance conditions: the fixed finite-class truncations approximate them up to a tail of upper density tending to zero (one may impose the remaining interior inequalities, automatic eventually for fixed word endpoints or valid Type II classes). ∎

**Controls for D.** F1: the profile includes (p/q)=−1; no square unit qualifies. F2: it is an avoidance theorem for selected primes >Y with Y→∞, not coverage for numerator 8 or the C-even branch; the guaranteed word has t=4. F3: only primes; excluded all Z₇ including 4545. F4: for large enough q, Y exceeds the whole panel; no positivity at the zeros is invoked. Items 4–9,15–17 of the preflight: the two density bounds sieve *against* small prime support; they do not prove a divisor class at a prescribed p. A prime larger than the threshold must actually occur, to odd valuation, on each specified object, with no maximum allowed height. This is not a power bound in p.

**CERTIFIED (same word engine as §4).** `ulimit -v 6000000; timeout 1800 uv run --offline --no-project python -B scripts/z80_kernel_budget.py 10000000` → `data/z80/jugular/kernel.txt`. At 435/3426 primes the best attainable largest prime of sf(uv) exceeds q. At q≡1 (4) none has sf(uv)=q: indeed in a coprime pair with kernel q one outer letter is a square, the other is divisible by q, giving (p/q)=(−1/q)=+1, impossible. The census sanity check is not evidence for the asymptotic exponents. As a second check on §3's scope, the trapped primes themselves have the good word u=5,t=7,v=(p+5)/34 (p≡−5 mod 34 and χ(34)=−1); the trap is strictly local to its seeds.

**Assessment: next step.** Do Type I solutions at these same primes also require a large prime in a specified squarefree kernel? A height bound for a chart does not resolve that question. For Type II the norm equation controls the tail beyond X^{3/2}; a comparable argument for the Type I modulus with two root classes is missing.
