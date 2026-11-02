# Z54_HCKILL — kill side of the HC hierarchy: HC(p) > X infinitely often without Dickson

**ES is OPEN.** Nothing here proves or disproves it. All results are internal (internally reviewed only).
Lane: HCKILL (wave z54, gap 3, kill side). Scripts `scripts/z54_hckill_*`, data `data/z54/hckill/`.

## 0. Verdict first: **strengthened (conditional) + narrowed**; the unconditional kill is not reached

Notation. For p ≡ 1 (mod 8), 𝒞 = {x ≥ 4 : 4 | x or x ≡ 7 (mod 8)} = {4, 7, 8, 12, 15, 16, 20, 23, 24, …}. Line x
*fires* if N_x^e = p + x or N_x^l = xp + 1 has a divisor ≡ −1 (mod x). HC(p) is the least firing x
(LOWERTAIL_ROUND2_FABLE §3.1, Z53_HCSHIFTS §1); ES₅(p) ⟺ HC(p) < ∞. S = {n ≥ 1 : every prime factor of n is ≡ 1 (mod 4)};
𝒫 = {primes ≡ 3 (mod 4)}.

**Target K(X)** (kill at window X): infinitely many primes p ≡ 1 (mod 8) with HC(p) > X. Before this lane: K(X) for each
fixed X CONDITIONAL on Dickson (FABLE Prop 3.3(a), 1 + 2|𝒞 ∩ [4,X]| linear forms simultaneously prime); growing
X ≍ log p/log log p CONDITIONAL on a non-standard uniform Bateman–Horn bound (HCSHIFTS Prop W2). Unconditionally: nothing.

**What this lane proves.**
1. **Exact reduction (Lemma 1.1, PROVED).** K(4) = K(5) = K(6) ⟺ **P(4,15)**: infinitely many primes p ≡ 1 (8) with
   p + 4 ∈ S and 4p + 1 ∈ S. Every K(X), X ≥ 4, implies P(4,15). "HC unbounded" therefore needs, at the very least, a
   prime with two *half-dimensional* shift conditions. P(4,15) is not in the literature found (§4; closest: Nath–Xie
   2025, p − 1 a sum of two squares and Ω(p + 2) ≤ 11). Exactly the lines x ∈ {4, 8, 12, 24} (x | 24) are pure
   subgroup ("confinement") conditions; the other lines are anatomy events (Lemma 1.2).
2. **Near-square kill family (Theorem Q, PROVED; infinitude CONDITIONAL on Bunyakovsky for ONE polynomial).** Every prime
   p = 5m² + 1 with 4 | m has HC(p) ≥ 7. So K(4) follows from Bunyakovsky for f(k) = 720k² + 1 alone, instead of
   Dickson for three linear forms. CERTIFIED on all 5 719 such primes ≤ 10¹².
3. **The algebraic (quadratic-family) mechanism is classified and walled (§2, PROVED except where marked).**
   * Two-variable quadratic families confine at most one window integer identically (Prop F6). So no K(4) from
     prime-producing binary forms (Iwaniec/Friedlander–Iwaniec-type input) by this route.
   * One-variable quadratic families p = (y² + δ)/(4a): line 4 ⟺ a rational conic (infinitely many families, Thm Q is
     one); lines {4, 7} ⟺ points of an elliptic curve E₇ of conductor 735, rank 1 (CERTIFIED, PARI 2-descent), but every
     real-admissible point among the first 9 multiples fails integrality (EVIDENCE); lines {4, 7, 8} ⟺ points on four
     curves of genus 17, hence **finitely many families (PROVED relative to Faltings)**. No family confines a prime line
     q ≡ 7 (8) with q ∤ δ (Prop F5), so no single family certifies a growing window.
4. **Sieve-tractability ledger (§3).**
   * **K(4) is sieve-tractable at level ≈ 1 (Theorem E, CONDITIONAL on EH(θ₀) for an absolute θ₀ < 1):**
     #{p ≤ x : p ≡ 1 (8), HC(p) > 4} ≫ x/(log x)², the true order (matches FABLE Thm 3.2's upper bound). The proof
     needs no parity-breaking beyond PNT in progressions: a linear sieve on (p + 4)(4p + 1) by 𝒫 to z = x^{1/2−η}, plus
     Iwaniec's two-large-primes trick (bad configurations are O(η^{3/2}) against an O(η) main term).
   * **With Bombieri–Vinogradov (θ = 1/2)** the same sieve proves only the shadow (Prop A, PROVED rel. BV): ≫ x/(log x)²
     primes p ≡ 1 (8) with (p + 4)(4p + 1) free of 𝒫-primes below x^ζ, any fixed ζ < 1/4. Closing the gap needs either
     level θ₀ (deficit θ₀ − 1/2; best known for CRT-coherent residue systems: 1/2 + 7/300, Polymath8a, smooth moduli)
     or an asymptotic count of switched configurations p + 4 = q₁q₂m, i.e. prime detection in a switched sequence
     (parity-type) (Assessment).
   * **K(7) is not reached by confinement sieves even under EH** (Assessment, scoped): four half-dimensional
     conditions give sieve dimension 2, the integers must be sifted to ≈ x^{1/2}, and level 1 gives s = 2 < β₂
     (DHR β₂ = 4.266, Λ²Λ⁻ β₂ = 4.516; Franze, arXiv:1012.3809, Table 1).
5. **EVIDENCE (§5).** Exact counts of HC > 4 primes to 10¹¹ follow the half-dimensional heuristic C·∫dt/(log t)² with
   C = 4K²𝔖 = 0.4110, ratio 0.81 → 0.966 from 10⁵ to 10¹¹.

**Bottom line of the verdict.** The kill side is now: K(4) CONDITIONAL on EH (a standard conjecture, replacing
Dickson), or on Bunyakovsky for one quadratic; K(X ≥ 7) still needs Dickson-type input; unconditional K(4) is equivalent
to a two-shift half-dimensional prime theorem that is not in the literature and is out of reach of BV-level sieves
(Assessment). No positive step toward ES; the value is a cleaner map of what kills cost.

## 0.1 Why this is not already closed

The only kill mechanism on record makes every window integer "constant × prime" (Dickson). HCSHIFTS Thm W walls that
mechanism at X ≍ log p for fixed families, and its scope remark leaves **subgroup confinement** (HCSHIFTS Lemma C(a))
explicitly open: a line does not fire if all prime factors of its integer lie in a subgroup H ∌ −1 of (ℤ/x)^×. This lane
attacks K(X) through confinement, (i) algebraically (norm-form identities need no primality of window integers) and
(ii) analytically (sieve). Neither appears in FRONTIER §6 or the closed list.

## 1. Exact reductions

**Lemma 1.1 (PROVED).** Let p be prime. Then p ≡ 1 (mod 8) and HC(p) > 4 ⟺ p ≡ 1 (mod 8), p + 4 ∈ S and 4p + 1 ∈ S.
Since 𝒞 ∩ [4, 6] = {4}, K(4) = K(5) = K(6) = P(4,15), and K(X) ⟹ P(4,15) for every X ≥ 4.

*Proof.* FABLE §3.1: for p ≡ 1 (8), line 4 fires iff p + 4 or 4p + 1 has a divisor ≡ 3 (mod 4). Both are odd. An odd N
has a divisor ≡ 3 (mod 4) iff it has a prime factor ≡ 3 (mod 4), since the class 1 (mod 4) is multiplicatively closed;
so line 4 does not fire iff p + 4, 4p + 1 ∈ S. ∎

**Lemma 1.2 (PROVED; which lines are subgroup conditions).** Let x ∈ 𝒞, N ≥ 1 with gcd(N, x) = 1, G = (ℤ/x)^×, and H_N the
subgroup of G generated by the classes of the prime factors of N.
* (a) If G has exponent 2 (⟺ x | 24; in 𝒞: x ∈ {4, 8, 12, 24}), then N has a divisor ≡ −1 (mod x) ⟺ −1 ∈ H_N. So
  "line x does not fire on N" is *exactly* "all prime factors of N lie in a subgroup avoiding −1".
* (b) For every x ∈ 𝒞 there is an odd real character χ mod x (χ(−1) = −1); if every prime factor ℓ of N has χ(ℓ) = 1,
  no divisor of N is ≡ −1 (mod x) (HCSHIFTS Lemma C(a)). For x ≡ 7 (8) one can take χ = χ_D with D = −(squarefree part
  of x) ≡ 1 (mod 8), so χ(2) = +1 (needed because N_x^e, N_x^l are then even). Index-2 subgroups are the largest
  subgroups avoiding −1 (H ∩ {±1} = 1 forces [G : H] ≥ 2).
* (c) If G does not have exponent 2, "no divisor ≡ −1" is strictly weaker than "−1 ∉ H_N": there is N, a product of at
  most two primes, with −1 ∈ H_N but no divisor ≡ −1.

*Proof.* (a) With g² = 1 for all g, the residues of the divisors of N are exactly the products of subsets of the
prime-factor classes (exponents matter only mod 2), i.e. the F₂-span of those classes, which is H_N. (b) If 4 | x take
χ₋₄. If x ≡ 7 (8), then x ≡ 3 (mod 4) has a prime factor ≡ 3 (mod 4) and its squarefree part x′ ≡ 7 (mod 8) (odd squares
are ≡ 1 (mod 8)), so D = −x′ ≡ 1 (mod 8) is a fundamental discriminant with |D| | x, χ_D is odd and χ_D(2) = +1. All
divisors d of N then have χ(d) = 1 ≠ −1 = χ(−1). (c) If G has an element h of odd order r > 1, put g = −h: g^r = −1,
g ≠ −1; a prime ℓ ≡ g (mod x) (Dirichlet) is the required N (divisor classes 1, g). Otherwise G is a 2-group of
exponent ≥ 4; take h of order 4. If h² = −1, N = ℓ ≡ h works (classes 1, h). If h² ≠ −1, take distinct primes
ℓ₁ ≡ h, ℓ₂ ≡ −h (h ≠ −h as −1 ≠ 1). The divisor classes are 1, h, −h, −h², and none is −1: h = −1 or −h = −1
contradicts ord h = 4, and −h² = −1 means h² = 1. But H_N ∋ h·(−h)⁻¹ = −1. ∎

*Reading.* Lines 4, 8, 12, 24 are pure half-dimensional "Landau" conditions; every other line is a *union* of a
confinement condition and anatomy events (few prime factors whose subset products miss −1). For kills, confinement is
the sufficient condition one can try to force; for each line it costs one half-dimension per window integer.

## 2. The algebraic mechanism: quadratic confinement families

### 2.1 Theorem Q (PROVED; the near-square kill family)

**Theorem Q.** Let m ≡ 0 (mod 4) and suppose p = 5m² + 1 is prime. Then p ≡ 1 (mod 8), 12 | m, and HC(p) ≥ 7. Hence
K(4) holds CONDITIONAL on the Bunyakovsky conjecture for the single polynomial f(k) = 720k² + 1, and under the
Bateman–Horn conjecture for f, #{p ≤ x : HC(p) > 4} ≫ √x/log x from this family alone.

*Proof.* p + 4 = 5(m² + 1) and 4p + 1 = 5((2m)² + 1). For m even, m² + 1 and (2m)² + 1 are odd sums of two coprime
squares, so each prime factor ℓ satisfies (−1/ℓ) = 1, ℓ ≡ 1 (mod 4); and 5 ≡ 1 (mod 4). So p + 4, 4p + 1 ∈ S and line 4
does not fire (Lemma 1.1). 4 | m gives 16 | 5m², p ≡ 1 (mod 8). If 3 ∤ m then 5m² + 1 ≡ 0 (mod 3), impossible for a
prime p > 3; so 12 | m and p = f(m/12). f is irreducible with f(0) = 1 (no fixed prime divisor). ∎

CERTIFIED (`data/z54/hckill/fam_5m2p1_hc_1e12.txt`; engine `scripts/z53_hcshifts_hc.c list 128 4096`, reviewed in z53):
all 5 719 primes p = 80s² + 1 ≤ 10¹² have HC(p) ≥ 7; distribution HC = 7: 5 117, 8: 481, 12: 94, 15: 21, 16: 1,
20: 4, 23: 1. The share HC = 7 (89.5 %) matches P(HC = 7 | HC > 4) = 111 635/125 059 = 89.3 % in the z49 census to 10⁸:
beyond line 4 the family behaves like generic HC > 4 primes (EVIDENCE).

*Reading.* 5p = (5m)² + 5: the family is a near-square family, and the mechanism is literally the T1 confinement
(HCSHIFTS Lemma C(d)) deformed off the squares, in the direction FRONTIER §4 item 15 calls hardest. Compared with
FABLE Prop 3.3(a) for X = 4 (Dickson for p, (p+4)/5, (4p+1)/5 simultaneously, density x/(log x)³), Theorem Q needs one
quadratic but yields only √x/log x members. The two hypotheses are incomparable special cases of Schinzel's H.

### 2.2 The general one-variable family and its classification

Every integer-valued quadratic polynomial with positive leading coefficient and negative discriminant is, after an affine
change of variable, p = (y² + δ)/(4a) with integers a, δ ≥ 1, y in an arithmetic progression (4ap = y² + δ). Then
  4a(p + x) = y² + (δ + 4ax),  4ax(xp + 1) = (xy)² + x(xδ + 4a).
Say the family **confines line x** if there is a finite set B of primes and a nonempty union of residue classes of y on
which every prime factor ℓ ∉ B of N_x^e and N_x^l satisfies χ(ℓ) = 1 for an odd real character χ mod x, and the primes
in B do not divide N_x^∗ (so no divisor ≡ −1 (mod x)). Write fd(−n) for the fundamental discriminant of −n.

**Prop F1 (PROVED).** Line x is confined iff D_e := fd(−(δ + 4ax)) and D_l := fd(−x(xδ + 4a)) satisfy |D| | x, with
D ≡ 1 (mod 8) when x ≡ 7 (mod 8), and the finitely many local conditions at the primes dividing 2a·D·(the square
cofactors) are compatible (a nonempty set of classes of y).
*Proof.* (⇐) δ + 4ax = |D_e|g² with 2g ∈ ℤ, so 16a(p + x) = (2y)² + |D_e|(2g)²; a prime ℓ ∤ 2agD_e dividing p + x has
D_e ≡ (2y/2g)² (mod ℓ), so χ_{D_e}(ℓ) = 1, and χ_{D_e} is an odd character mod x because |D_e| | x and D_e < 0. The finitely
many remaining primes are handled by excluding residue classes of y (and ℓ = 2 by D ≡ 1 (mod 8) when N is even).
Same for the level line. (⇒) If χ ≠ χ_{D_e} (as characters on primes), then χχ_{D_e} is a nontrivial character, and by
Chebotarev for the biquadratic field infinitely many primes ℓ have χ_{D_e}(ℓ) = 1, χ(ℓ) = −1; each such ℓ ∤ 2a·(…)
divides y² + (δ + 4ax) for two classes of y mod ℓ, which meet every residue class of the family modulus by CRT. So χ = χ_{D_e},
i.e. the conductor |D_e| divides x. ∎

**Prop F2 (PROVED; line 4).** The family confines line 4 iff, up to a common rational square factor,
(a, δ) = (U² − W², 16W² − U²)/15 with U, W ∈ ℚ, 1 < |U/W| < 4.
*Proof.* Allowed D for x = 4 is only −4, and fd(−n) = −4 iff n ∈ ℚ^{×2}. So δ + 16a = U² and 4(4δ + 4a) = 16(δ + a) ∈ ℚ^{×2},
δ + a = W². Solve: 15a = U² − W², 15δ = 16W² − U²; a, δ > 0 is 1 < |U/W| < 4. ∎ Theorem Q is (U, W) = (2, 1):
(a, δ) = (5²/15)·(3, 12) = (5, 20), y = 40s, p = 80s² + 1. `scripts/z54_hckill_fam4.py` lists the smallest families with p ≡ 1 (8),
e.g. (a, δ) = (5, 116): p = 1280t² + 128t + 9 avoiding t-classes with 7 | y or 11 | y.

**Prop F3 (lines {4, 7}; PROVED reduction, CERTIFIED rank).** With (a, δ) as in F2, `scripts/z54_hckill_genus.py` gives
δ + 28a = (9U² − 4W²)/5 and 7(7δ + 4a) = 7(36W² − U²)/5. The only allowed D for x = 7 is −7, so line 7 is confined iff
9U² − 4W² ∈ 35ℚ^{×2} and 36W² − U² ∈ 5ℚ^{×2}. Parametrising the second conic through (U, W, r) = (4, 1, 2) by
U/W = 4(5m² − 5m − 1)/(5m² + 1) turns the first into
  E₇ : Y² = 7(m − 1)(5m − 7)(5m + 1)(7m + 1),
an elliptic curve (rational 2-torsion; PARI `ellfromeqn`) of conductor 735, torsion ℤ/2 × ℤ/2, **rank 1** (PARI
`ellrank` bounds [1, 1], generator (−1440, 31200) on the model [0, 532, 0, −1599360, 553190400]). So infinitely many
rational (a : δ) confine lines 4 and 7 formally. EVIDENCE (`data/z54/hckill/e7_points.txt`): the points nG + T,
|n| ≤ 9, T torsion, give 9 distinct (U : W); 4 fail the real condition 1 < U/W < 4, and each of the other 5 gives an a
with an odd prime factor ℓ ∤ δ, ℓ < 10⁶, and (−δ/ℓ) = −1 (ℓ = 31, 1123, 1483, 4507, 31307, …; by the F2 formulas
δ ≡ (tW)² (mod ℓ) for ℓ | a, so these are ℓ ≡ 3 (mod 4)). Then 4a | y² + δ is impossible: the family contains no
integers. (The script's line-7 recheck uses partial factorisation and is unreliable for the 100+-digit numbers; E₇
membership holds by construction.) Whether some point of E₇ passes all local conditions (giving a K(7)-under-Bunyakovsky family) is
open; heuristically a ∝ (U − W)(U + W) must have both factors S-like, probability ≍ (ĥn²)⁻¹ at the n-th point, a
convergent sum (Assessment: finitely many, possibly none).

**Prop F4 (lines {4, 7, 8}; PROVED relative to Faltings).** Line 8 allows D ∈ {−4, −8}; it is confined iff
15(31U² − 16W²) ∈ ε₁ℚ^{×2} and 15(31W² − U²) ∈ ε₂ℚ^{×2} for some ε₁, ε₂ ∈ {1, 2}. For each (ε₁, ε₂), the four
conditions of lines 7, 8 define a (ℤ/2)⁴-cover of P¹_{U:W} branched at the 8 distinct points U/W ∈ {±2/3, ±6, ±4/√31,
±√31} (the four binary forms are squarefree and pairwise coprime, so the cover is geometrically irreducible), and by
Riemann–Hurwitz 2g − 2 = 16·(−2) + 8·8, **g = 17**. By Faltings each of the four curves has finitely many rational
points. Hence **only finitely many (a : δ) confine all lines of 𝒞 ∩ [4, X] for any X ≥ 8.** ∎

**Prop F5 (PROVED; no growing window from one family).** If a family confines line q for a prime q ≡ 7 (mod 8), then
q | δ. *Proof.* The only odd real character mod q is χ₋q, so fd(−(δ + 4aq)) = −q, δ + 4aq ∈ qℚ^{×2}, and q | δ (if
q | a too, then q | δ directly from q | δ + 4aq). ∎ So a fixed family confines only finitely many prime lines q ≡ 7 (8),
and no single quadratic family certifies HC > X for all X. (Members may of course have larger HC by chance.)

**Prop F6 (PROVED; two variables give at most one line).** Let F(s, t) ∈ ℚ[s, t] be quadratic with nondegenerate
quadratic part, and consider the window integers N_i = λ_iF + μ_i (λ_i, μ_i ∈ ℚ^×, μ_i/λ_i pairwise distinct; e.g.
p + x and xp + 1). Then at most one N_i is confined identically on a lattice coset (in the sense above, with any real
character χ_i ≠ 1).
*Proof.* Complete squares: F = Q(s′, t′) + c with Q a nondegenerate binary form and s′, t′ affine in s, t. Then
N_i = λ_i(Q + c + μ_i/λ_i), and c + μ_i/λ_i = 0 for at most one i. For e := c + μ_i/λ_i ≠ 0 and every prime ℓ not
dividing 2·disc(Q)·e·(denominators)·(coset modulus), Q(s′, t′) ≡ −e (mod ℓ) is solvable (a nondegenerate binary
quadratic form over 𝔽_ℓ represents every nonzero element), and the solutions meet the coset by CRT. So every such ℓ divides
some value of N_i; infinitely many have χ_i(ℓ) = −1. ∎ Consequently "primes p = F(s, t)" theorems (Iwaniec's
φ(x, y) + A, Friedlander–Iwaniec) can deliver one confined window integer (e.g. p = s² + t² − 4 with p + 4 ∈ S, which is
Iwaniec's theorem), never two. K(4) by algebra needs a one-variable family, hence Bunyakovsky.

## 3. Sieve analysis: which steps are tractable

Hypothesis **EH(θ)**: for every A, Σ_{q ≤ x^θ} max_{(c,q)=1} |π(x; q, c) − li(x)/φ(q)| ≪_A x/(log x)^A. BV is EH(1/2 − ε).

### 3.1 Theorem E (CONDITIONAL on EH(θ₀) for an absolute θ₀ < 1)

**Theorem E.** There is an absolute η₀ ∈ (0, 1/10] such that EH(1 − η₀) implies
  #{p ≤ x : p ≡ 1 (mod 8), p + 4 ∈ S, 4p + 1 ∈ S} ≫ x/(log x)²  (x ≥ x₀).
In particular K(4) (HC(p) ≥ 7 for ≫ x/(log x)² primes p ≤ x), with the order of magnitude of FABLE Thm 3.2's upper bound.

*Proof.* Fix η ∈ (0, 1/10] (chosen at the end), θ = 1 − η, z = x^{1/2−η}, D = x^θ/8.

*Step 1 (sieve setup).* Sift 𝒜 = {(p + 4)(4p + 1) : p ≤ x, p ≡ 1 (8)} by 𝒫_z = {ℓ ∈ 𝒫 : ℓ < z}. For squarefree d composed
of 𝒫-primes let R(d) = {b mod d : (b + 4)(4b + 1) ≡ 0}; |R(ℓ)| = ν(ℓ) = 2 for ℓ ∈ 𝒫 ∖ {3} (the roots −4, −4⁻¹ coincide
iff ℓ | 15) and ν(3) = 1; every root is a unit mod ℓ. Then
  |𝒜_d| = Σ_{b ∈ R(d)} π(x; 8d, c_b) = g(d)·X + r_d,  X = li(x)/4,  g(d) = ν(d)/φ(d),
with c_b ≡ 1 (8), ≡ b (d), and |r_d| ≤ ν(d)·max_c|π(x; 8d, c) − li(x)/φ(8d)|. Since ν(d) ≤ 2^{ω(d)}, Cauchy–Schwarz with the
trivial bound max_c |…| ≪ x/φ(q) and EH(θ) give Σ_{d < D} μ²(d)3^{ω(d)}|r_d| ≪_A x/(log x)^A. The density g satisfies
the linear (κ = 1) sieve axiom: ∏_{w ≤ ℓ < z, ℓ ∈ 𝒫}(1 − g(ℓ))⁻¹ = (log z/log w)(1 + O(1/log w)), because
Σ_{ℓ ∈ 𝒫, ℓ < y} 2/ℓ = log log y + O(1) (Mertens in progressions mod 4), and g(ℓ) < 1.

*Step 2 (lower bound).* The Jurkat–Richert linear sieve (Halberstam–Richert, *Sieve Methods*, Thm 8.4; equivalently
Iwaniec's Rosser sieve) gives, for s = log D/log z ≥ 2,
  S(𝒜, 𝒫, z) ≥ X·V(z)·(f(s) − o(1)) − Σ_{d<D, d|P(z)} 3^{ω(d)}|r_d|,  f(s) = 2e^γ log(s − 1)/s (2 ≤ s ≤ 4),
V(z) = ∏_{ℓ ∈ 𝒫_z}(1 − g(ℓ)) ≍ 1/log x. Here s = (1 − η)/(1/2 − η) + o(1) = 2 + 2η/(1 − 2η) + o(1), so s − 2 ≥ 2η and
f(s) ≥ e^γ(s − 2)/s ≥ (2e^γ/3)η (using log(1 + u) ≥ u/2 for 0 ≤ u ≤ 1). Hence S(𝒜, 𝒫, z) ≥ c₁η·x/(log x)² with c₁ > 0
absolute, for x ≥ x₀(η).

*Step 3 (survivors).* Let p be counted, N ∈ {p + 4, 4p + 1}. Then N ≡ 1 (mod 4), so N has an even number of 𝒫-prime
factors (with multiplicity), all ≥ z; N ≤ 4x + 1 < z³; so either N ∈ S or N = q₁q₂m with q₁ ≤ q₂ in 𝒫, q₁ ≥ z, and
m ∈ S, m ≤ (4x + 1)/z² ≤ 5x^{2η}. So #target ≥ S(𝒜, 𝒫, z) − |B^e| − |B^l|, B^e (resp. B^l) the counted p with
p + 4 (resp. 4p + 1) of the second shape.

*Step 4 (bad configurations, unconditional).* For B^e fix m ∈ S, m ≤ 5x^{2η}, and q₁ ∈ 𝒫 ∩ [z, √(x + 4)]; count k ≤ Y :=
(x + 4)/(mq₁) with k prime (= q₂), mq₁k − 4 prime (= p) and 4mq₁k − 15 (= 4p + 1) free of 𝒫-primes below z₀ = x^{1/10}.
Sift k ≤ Y by ℓ < z₀ at k ≡ 0, at k ≡ 4(mq₁)⁻¹ (ℓ ∤ 2mq₁), and, for ℓ ∈ 𝒫 ∤ 15mq₁, at k ≡ 15(4mq₁)⁻¹: at most 3
classes, < ℓ for every ℓ, sieve dimension ≤ 5/2. Since Y ≥ x^{0.4} ≥ z₀⁴, the Brun/Selberg upper-bound sieve
(Halberstam–Richert Thm 2.2), uniform in the coefficients, gives count ≪ Y∏_{ℓ<z₀}(1 − ω(ℓ)/ℓ) ≪ Y·h(m)(log x)^{−5/2} with
h(m) = ∏_{ℓ | m}(1 + 2/ℓ) (only ℓ | m change ω, as q₁ > z₀; ℓ | m are ≡ 1 (mod 4)). Summing,
  |B^e| ≪ x(log x)^{−5/2}·Σ_{m ∈ S, m ≤ 5x^{2η}} h(m)/m·Σ_{z ≤ q ≤ 2√x} 1/q.
The q-sum is log((1/2)/(1/2 − η)) + o(1) ≤ 3η. The m-sum is ≤ ∏_{ℓ ≡ 1 (4), ℓ ≤ 5x^{2η}}(1 + (1 + 2/ℓ)/(ℓ − 1))
≪ (log x^{2η})^{1/2} ≤ 2(η log x)^{1/2}. So |B^e| ≤ C₂η^{3/2}x/(log x)², C₂ absolute. B^l is identical with
4p + 1 = mq₁k, k restricted to the class mq₁k ≡ 1 (mod 4), p = (mq₁k − 1)/4 prime and p + 4 = (mq₁k + 15)/4 sifted.

*Step 5.* #target ≥ (c₁η − 2C₂η^{3/2})x/(log x)². Take η₀ = min(1/10, (c₁/4C₂)²). ∎

*Remarks.* (i) EH is used only for primes in progressions with the CRT-coherent residues of (n + 4)(4n + 1); no Type II
or parity-breaking input beyond that. (ii) η₀ is not computed (it depends on c₁, C₂). (iii) The proof is Iwaniec's
semi-linear trick lifted to the linear sieve: in dimension 1/2 the main term near the sifting limit is ≍ √η against an
O(η) loss; here it is ≍ η against O(η^{3/2}). (iv) It is a density statement; no single prescribed prime is touched
(kill side: none is needed).

### 3.2 What BV gives (Prop A, PROVED rel. BV and the linear sieve)

**Prop A.** For each fixed ζ < 1/4, #{p ≤ x : p ≡ 1 (8), (p + 4)(4p + 1) has no prime factor ≡ 3 (mod 4) below x^ζ}
≫_ζ x/(log x)². At these primes line 4 can fire only through a divisor built from prime factors ≡ 3 (mod 4) of size
≥ p^ζ (at least two of them in p + 4 or in 4p + 1).
*Proof.* Steps 1–2 with D = x^{1/2}(log x)^{−B} (BV), z = x^ζ, s → 1/(2ζ) > 2, f(s) > 0. ∎

*The gap, exactly (Assessment with PROVED arithmetic).* With θ = 1/2 the linear sieve needs z < x^{1/4}, and the
survivors then include N = q₁q₂m with q₁ ∈ [x^ζ, x^{1/2}], m up to x^{1−2ζ}. In the half-dimensional model a sifted N is
in S with probability ≍ √ζ, so the target is a fraction ≍ ζ of the survivors and the bad set B is ≍ (1 − cζ) of them.
Subtraction then needs B *asymptotically* (relative error o(ζ)), and counting B means counting primes p = mq₁q₂ − 4 in a
switched sequence, i.e. prime detection: a parity-type step. Upper-bound sieves lose constant factors there. So, in this
implementation, P(4,15) needs **level θ₀ < 1 (Theorem E), against BV's 1/2**; the best level known for CRT-coherent
residue systems is 1/2 + 7/300 (Polymath8a, arXiv:1402.0811, abstract: "exponent of distribution 1/2 + 7/300", for
smooth squarefree moduli). A vector sieve (Brüdern–Fouvry) with two semi-linear components is worse: it needs
f₁/F₁ + f₂/F₂ > 1 with s₁ + s₂ = 2θ (each integer sifted to ≈ x^{1/2}). For κ = 1/2, F(s) = 2(e^γ/πs)^{1/2} and
f(s) = (e^γ/πs)^{1/2}∫₁^s dt/√(t(t−1)) on [1, 2], so f/F = log(√s + √(s−1)), concave there, and f = 0 for s ≤ 1. For
2θ ≤ 3 an s_i > 2 forces s_j < 1, so the symmetric choice is optimal and needs log(√θ + √(θ−1)) > 1/2, θ > 1.2715.
Expected route for an unconditional "one shift in S, the other almost": Nath–Xie's vector-sieve framework
(arXiv:2501.16723) with p + 4 in the semi-linear slot and 4p + 1 sifted by 𝒫 up to x^δ (Assessment; not proved here).

### 3.3 K(7) and beyond (Assessment, scoped to confinement sieves)

HC(p) > 7 needs lines 4 and 7 dead. Line 7 is not a pure subgroup condition (Lemma 1.2(c)); its sieve-tractable
sufficient condition is confinement by χ₋₇ for p + 7 and 7p + 1 (Lemma 1.2(b)), with (p/7) = 1 necessary (HCSHIFTS
Lemma C(e)). Four half-dimensional conditions give sieve dimension κ = 2, and each integer (size ≍ x) must be sifted to
≈ x^{1/2} for the two-large-primes trick. At level D = x (EH), s = 2, below every known dimension-2 sifting limit (DHR
β₂ = 4.266, Λ²Λ⁻ β₂ = 4.516; Franze, arXiv:1012.3809, Table 1, verified). Sifting only to x^{1/β₂} leaves a bad set of
proportion 1 − O(ζ²) of the survivors, again requiring asymptotic (parity-type) counts. So **K(7) is out of reach of
confinement sieves even under EH**; the anatomy route for line 7 (e.g. p + 7 = 8q with q prime) is a prime-pattern
condition (parity). Growing X adds ≈ 3X/8 half-dimensions per unit window: hopeless for sieves (Assessment). Known
conditional reaches: Dickson (fixed X), UBH (X ≍ log p/log log p), Bunyakovsky for one quadratic (X = 4; X = 7 only
if E₇ has an admissible point).

## 4. Literature (research subagent, `data/z54/hckill/lit_report.md`; coverage-limited, Assessment)

* No source found proves P(4,15) or any "prime p with two shifts both sums of two squares / in S". Not a formal
  open-problem citation.
* Closest: K. Nath, L. Xie, arXiv:2501.16723, Thm 1.1 (verified in the HTML): #{p ≤ x : p = m² + n² + 1,
  Ω(p + 2) ≤ 11} ≫ x/(log x)^{5/2}; vector sieve with a semi-linear and a linear component.
* Iwaniec, Acta Arith. 21 (1972): primes φ(x, y) + A (one shifted value a norm); exact statement not text-extracted
  (UNVERIFIED theorem numbering). Hooley: n, n + h, n + k sums of two squares for integer n (not primes).
* Polymath8a, arXiv:1402.0811 (abstract verified): level 1/2 + 7/300 for smooth moduli and CRT-coherent classes.
* Franze, arXiv:1012.3809, Table 1 (verified): sifting limits β₂ = 4.266 (DHR), 4.516 (Λ²Λ⁻).

## 5. Numerics, controls

* **Counts (CERTIFIED exact; `scripts/z54_hckill_census.c`, sieve by 𝒫-primes ≤ √(4x+1), exact by the parity argument
  of Step 3).** #{p ≤ x : p ≡ 1 (8), HC(p) > 4}: 295, 2 226, 16 125, 125 059, 986 400, 7 962 940 at x = 10⁵…10¹⁰
  and 65 618 311 at 10¹¹ (6 min) (10⁸ agrees with the z49 census 1 439 970 − 1 314 911). Ratio to x/(log x)²: 0.391,
  0.425, 0.419, 0.424, 0.424, 0.422, 0.421. Files `census_hc4_1e10.txt`, `census_hc4_1e11.txt`.
* **Heuristic constant (EVIDENCE).** Half-dimensional model: count ≈ C∫₂^x dt/(log t·√(log(t+4)·log(4t+1))) with
  C = 4K²𝔖, K² = (1/8)∏_{ℓ∈𝒫}(1 − ℓ⁻²) (S has #S(x) ~ Kx/√log x, K = 0.3271), 𝔖 = (9/8)∏_{ℓ∈𝒫, ℓ≥7}
  ℓ²(ℓ − 3)/(ℓ − 1)³ = 0.9602, C = 0.4110 (factor 4 = 16·(1/4): P(N ∈ S | N ≡ 1 (4)) = 4K/√log N for each of the two
  integers, which are ≡ 5 (8), and S splits evenly between 1 and 5 (mod 8); 1/4 = share of p ≡ 1 (8); c_ℓ =
  (1 − ν(ℓ)/(ℓ−1))/(1 − 1/ℓ)² the prime-shift correction). Observed/predicted: 0.811, 0.914, 0.922, 0.948, 0.957,
  0.962, 0.966 (10⁵…10¹¹),
  rising towards 1 as expected for half-dimensional lower-order terms. Consistent with Theorem E's order.
* **Controls.** Odd squares n = m²: m² + 4 and 4m² + 1 are primitive sums of two squares, so line 4 is confined at every
  odd square (T1; HCSHIFTS Lemma C(d)); δ = 0 is the degenerate member of Prop F2 (p = (y/2)²). The FRONTIER §4 item-14
  test primes: HC(409) = HC(577) = 4 (line 4 fires; (★)-zeros are not HC-hard), HC(193) = 7, HC(2521) = 15,
  HC(3361) = 7, HC(5569) = 7, HC(9601) = 7, HC(66529) = 8, HC(8813281) = 8 (FABLE §1.5 table): the HC > 4 ones satisfy
  Lemma 1.1 (e.g. 193 + 4 = 197, 4·193 + 1 = 773, both prime ≡ 1 (4)). Theorem Q members are near-squares (5p − 5 = (5m)²).

## 6. FRONTIER §4 hard screens (for the best idea: Theorem E / Theorem Q, kill side)

1. **T1 squares.** A kill must *hold* at squares, and does: confinement is the T1 mechanism (all lines dead at m²). Theorem
   Q deforms it to near-squares; Theorem E's sieve counts primes, so its content is the prime distribution, not anything
   false at squares. (Screen 1 constrains upper-side proofs; here it is consistent.)
2. **8/131, 8/241.** Lemma 1.1 is 4-specific (𝒞 and line 4 come from Theorem 1 of FABLE, which is 4-specific, §1.5 there).
3. **Tied modulus.** Not applicable on the kill side: confinement uses a fixed character mod x per line; the tied class
   −1 (mod x) is avoided by a character, which is exactly why kills are cheap and positivity is not.
4. **Fixed p.** Theorem Q is pointwise (HC(p) ≥ 7 at each member); infinitude is conditional. Theorem E is a density
   statement (fine for kills, useless for ES).

## 7. Proposed FRONTIER §7.2 text (do not edit FRONTIER here)

> *(z54, `Z54_HCKILL.md`; kill side.)* **K(4) ⟺ P(4,15)** (PROVED): HC(p) > 4 for p ≡ 1 (8) iff p + 4, 4p + 1 ∈ S
> (all prime factors ≡ 1 (4)); every K(X), X ≥ 4, needs this two-shift half-dimensional prime theorem, which is not in the
> literature (closest: Nath–Xie 2025). Lines x | 24 are pure subgroup conditions; the rest are anatomy events.
> **Theorem Q** (PROVED): every prime 5m² + 1 with 4 | m has HC ≥ 7, so K(4) follows from Bunyakovsky for 720k² + 1 alone
> (CERTIFIED on 5 719 primes ≤ 10¹²). Quadratic confinement families are classified: two variables confine ≤ 1 window
> integer; lines {4,7} ⟺ the rank-1 elliptic curve E₇ (no integral-admissible point found); lines {4,7,8} only finitely
> many families (genus 17, Faltings). **Theorem E** (CONDITIONAL on EH(θ₀), some absolute θ₀ < 1): ≫ x/(log x)² primes
> p ≤ x have HC(p) > 4 (true order). With BV only the shadow "no 3-mod-4 prime factor below x^{1/4−ε}" (PROVED); the gap
> is a level deficit θ₀ − 1/2 or a parity-type switched count. K(7) is out of reach of confinement sieves even under EH
> (dimension 2, s = 2 < β₂ = 4.27). Unconditional "HC unbounded" is open and needs at least P(4,15).

**Bottom line.** The kill side of the HC hierarchy is now pinned: its first rung K(4) is exactly a two-shift
half-dimensional prime problem, which follows from Elliott–Halberstam (Theorem E) or from Bunyakovsky for a single
near-square quadratic (Theorem Q), but not from any BV-level sieve in the implementations analysed; rungs X ≥ 7 still need
Dickson-type input, and the algebraic near-square mechanism saturates at X ≤ 7 (finitely many families beyond). No
unconditional HC > 4 i.o. is proved. Nothing here touches positivity at a prescribed prime; for the upper side the
lesson is that line-4-dead primes are a positive-power-of-log-density set (≍ x/(log x)², EVIDENCE + Theorem E under EH)
and include near-square families, so any proof of HC ≤ X must certify from lines ≥ 7 there.

## 8. Reproduction

* `gcc -O2 -o hc scripts/z53_hcshifts_hc.c -lm; uv run --with sympy python /tmp/fam.py 1e12 > fam_5m2p1_primes_1e12.txt`
  (generator inlined in §2.1: p = 80s² + 1 prime); `hc list 128 4096 < fam_5m2p1_primes_1e12.txt`.
* `gcc -O2 -o cens scripts/z54_hckill_census.c -lm; ./cens 1e10` (32 s).
* `uv run --with cypari2 --with sympy python scripts/z54_hckill_e7group.py 9 16` (E₇ group, points);
  `scripts/z54_hckill_e7.py 3000 64` (hyperellratpoints search); `scripts/z54_hckill_genus.py` (forms, branch points, genus);
  `scripts/z54_hckill_fam4.py 60` (line-4 families with p ≡ 1 (8)); `scripts/z54_hckill_qfam.c` (brute search, U ≤ 300:
  825 admissible line-4 families, none confines line 7).
* Every command was run with `timeout` and `ulimit -v ≤ 6 GB`.

## 9. Review log
(TODO)
