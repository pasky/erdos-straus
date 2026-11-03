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

**Results.**
1. **Exact reduction (Lemma 1.1, PROVED).** K(4) = K(5) = K(6) ⟺ **P(4,15)**: infinitely many primes p ≡ 1 (8) with
   p + 4 ∈ S and 4p + 1 ∈ S. Every K(X), X ≥ 4, implies P(4,15), so "HC unbounded" needs at least a prime with two
   *half-dimensional* shift conditions. Exactly the lines x | 24 (in 𝒞: 4, 8, 12, 24) are pure subgroup
   ("confinement") conditions; the other lines are confinement-or-anatomy events (Lemma 1.2, PROVED). P(4,15) is the
   S-refined "hyperbolic prime number theorem" of the determinant-15 shell (Remark 1.3, PROVED identity), the analogue of
   Friedlander–Iwaniec's det-1 problem Σ Λ(n)r(n−2)r(n+2) (Acta Math. 202 (2009)).
2. **Near-square kill family (Theorem Q, PROVED; infinitude CONDITIONAL on Bunyakovsky for one polynomial).** Every prime
   p = 5m² + 1 with 4 | m has HC(p) ≥ 7. So K(4) follows from Bunyakovsky for f(k) = 720k² + 1 alone. CERTIFIED on all
   5 719 such primes ≤ 10¹².
3. **Algebraic (quadratic-family) confinement: classification of formal shapes (§2).**
   * Two-variable quadratic polynomials: at most one window integer can be confined identically on a full-rank lattice coset
     (Prop F6, PROVED; scoped to quadratic F; it does not cover x² + y⁴-type or other constructions).
   * One-variable families p = (y² + δ)/(4a): the formal square-class conditions for line 4 form a rational conic
     (PROVED; Theorem Q is one integral-admissible point); for lines {4, 7} an elliptic curve E₇ of conductor 735 and
     rank 1 (CERTIFIED by PARI 2-descent bounds [1, 1]); none of 17 sampled ratios (|n| ≤ 16, torsion translates;
     not a height-minimality certificate) gives an integral family
     (EVIDENCE); for lines {4, 7, 8} four curves of genus 17, hence **finitely many formal ratios (a : δ)** (PROVED,
     Faltings). Existence of any admissible family beyond X = 4 is undetermined. No family confines a prime line
     q ≡ 7 (8) with q ∤ δ (Prop F5, PROVED), so no single quadratic family certifies a growing window.
4. **Sieve ledger (§3).**
   * **Theorem E (CONDITIONAL on EH(θ₀) for some absolute θ₀ < 1; FI-2009-type):**
     #{p ≤ x : p ≡ 1 (8), HC(p) > 4} ≫ x/(log x)², the order of FABLE Thm 3.2's unconditional upper bound. Input: PNT
     in progressions at level θ₀ only. Method: linear sieve on (p + 4)(4p + 1) by 𝒫 to z = x^{1/2−η}, plus the
     two-large-primes trick (bad configurations O(η^{3/2}) against an O(η) main term). It follows the template of
     Friedlander–Iwaniec's Theorem 4 (which they prove for r(p−2)r(p+2) under the same kind of hypothesis); the S-refined
     statement for (p + 4, 4p + 1) was not located in the literature (Assessment).
   * **With Bombieri–Vinogradov** this implementation proves only the shadow Prop A (PROVED rel. BV): ≫ x/(log x)²
     primes p ≡ 1 (8) with (p + 4)(4p + 1) free of 𝒫-primes below x^ζ, any fixed 0 < ζ < 1/4. Closing the gap in this
     implementation needs level θ₀ (deficit θ₀ − 1/2; Polymath8a reaches 1/2 + 7/300 only for smooth squarefree moduli)
     or an asymptotic count of switched configurations p + 4 = q₁q₂m, i.e. prime detection in a switched sequence
     (parity-type) (Assessment). A two-component semi-linear vector sieve needs θ > cosh²(1/2) = 1.2715 (PROVED
     arithmetic of the sieve functions).
   * **K(7):** the direct confinement-sieve implementation gives no lower bound even at level 1: four half-dimensional
     conditions, dimension 2, sifting to ≈ x^{1/2} means s = 2 < β₂ (DHR 4.266, Λ²Λ⁻ 4.516; Franze arXiv:1012.3809,
     Table 1) (Assessment, scoped to that implementation).
5. **EVIDENCE (§5).** Exact counts of HC > 4 primes to 10¹¹ (CERTIFIED) follow the half-dimensional prediction
   C·∫₂^x dt/(log t·√(log(t+4) log(4t+1))), C = 4K²𝔖 = 0.4110 (CONJECTURE for the asymptotic): ratio 0.81 → 0.966 from 10⁵
   to 10¹¹.

**Bottom line of the verdict (Assessment).** K(4) now rests on EH(θ₀) (a standard conjecture, in place of Dickson), or
on Bunyakovsky for one quadratic. For arbitrary fixed X ≥ 7 Dickson remains the recorded conditional route. Unconditional
K(4) is equivalent to an S-refined two-shift prime theorem not located in the literature (closest unconditional:
Nath–Xie 2025, p − 1 a sum of two squares and Ω(p + 2) ≤ 11; closest conditional: Friedlander–Iwaniec 2009), and is
not reached by the BV-level sieves analysed here. No positive step toward ES; the value is a cleaner price list for kills.

## 0.1 Why this is not already closed

The only kill mechanism on record makes every window integer "constant × prime" (Dickson). HCSHIFTS Thm W walls that
mechanism at X ≍ log p for fixed families; its scope remark leaves **subgroup confinement** (HCSHIFTS Lemma C(a))
explicitly open: a line does not fire if all prime factors of its integers lie in a subgroup H ∌ −1 of (ℤ/x)^×. This
lane attacks K(X) through confinement, (i) algebraically (norm-form identities need no primality of window integers) and
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
are ≡ 1 (mod 8)), so D = −x′ ≡ 1 (mod 8) is a fundamental discriminant with |D| | x, χ_D is odd and χ_D(2) = +1 (for 4 | x the window
integers are odd, so χ₋₄(2) = 0 is irrelevant). All
divisors d of N then have χ(d) = 1 ≠ −1 = χ(−1). (c) If G has an element h of odd order r > 1, put g = −h: g^r = −1,
g ≠ −1; a prime ℓ ≡ g (mod x) (Dirichlet) is the required N (divisor classes 1, g). Otherwise G is a 2-group of
exponent ≥ 4; take h of order 4. If h² = −1, N = ℓ ≡ h works (classes 1, h). If h² ≠ −1, take distinct primes
ℓ₁ ≡ h, ℓ₂ ≡ −h (h ≠ −h as −1 ≠ 1). The divisor classes are 1, h, −h, −h², and none is −1: h = −1 or −h = −1
contradicts ord h = 4, and −h² = −1 means h² = 1. But H_N ∋ h·(−h)⁻¹ = −1. ∎

*Reading (Assessment).* Lines 4, 8, 12, 24 are pure half-dimensional "Landau" conditions; every other line is a *union* of a
confinement condition and anatomy events (few prime factors whose subset products miss −1). For kills, confinement is
the sufficient condition one can try to force; for each line it costs one half-dimension per window integer.

**Remark 1.3 (PROVED identity; the hyperbolic form).** For p prime, let Λ₄ = {M = (P −R; T Q) ∈ M₂(ℤ) :
P + Q ≡ R + T ≡ 0 (mod 4)}. The map (x, y, u, v) ↦ (P, Q, R, T) = (2x − u, 2x + u, 2y + v, 2y − v) is a bijection from
{x² + y² = p + 4, u² + v² = 4p + 1} onto {M ∈ Λ₄ : det M = PQ + RT = 15, ‖M‖² = 16p + 34}, with inverse x = (P+Q)/4,
y = (R+T)/4, u = (Q−P)/2, v = (R−T)/2. (Check: ‖M‖² ± 2 det M = (P ± Q)² + (R ± T)², giving 16(p + 4) and 4(4p + 1).)
So r(p + 4)r(4p + 1) counts integral points of the determinant-15 shell at height 16p + 34, and P(4,15) is the
S-refined (primitive-representation) version of a "hyperbolic prime number theorem" for that shell. Friedlander–Iwaniec
(Acta Math. 202 (2009) 1–19, Thms 3–4) treat the det-1 shell, Σ_{n≤x} Λ(n)r(n−2)r(n+2) ≍ x under their hypothesis A(θ)
for some θ < 1 sufficiently close to 1 (statements read from the published PDF text).

## 2. The algebraic mechanism: quadratic confinement families

### 2.1 Theorem Q (PROVED; the near-square kill family)

**Theorem Q.** Let m ≡ 0 (mod 4) and suppose p = 5m² + 1 is prime. Then p ≡ 1 (mod 8), 12 | m, and HC(p) ≥ 7. Hence
K(4) holds CONDITIONAL on the Bunyakovsky conjecture for the single polynomial f(k) = 720k² + 1.

*Proof.* p + 4 = 5(m² + 1) and 4p + 1 = 5((2m)² + 1). For m even, m² + 1 and (2m)² + 1 are odd sums of two coprime
squares, so each prime factor ℓ satisfies (−1/ℓ) = 1, ℓ ≡ 1 (mod 4); and 5 ≡ 1 (mod 4). So p + 4, 4p + 1 ∈ S and line 4
does not fire (Lemma 1.1). 4 | m gives 16 | 5m², p ≡ 1 (mod 8). If 3 ∤ m then 5m² + 1 ≡ 0 (mod 3), impossible for a
prime p > 3; so 12 | m and p = f(m/12). f is irreducible with f(0) = 1 (no fixed prime divisor). ∎

CONDITIONAL on Bateman–Horn for f: the family gives ≍ √x/log x primes p ≤ x with HC(p) > 4.

CERTIFIED (`data/z54/hckill/fam_5m2p1_hc_1e12.txt`; generator `scripts/z54_hckill_famgen.py`; engine
`scripts/z53_hcshifts_hc.c list 128 4096`, reviewed in z53; the internal reviewer regenerated and re-ran all members
byte-identically): all 5 719 primes p = 80s² + 1 ≤ 10¹² have HC(p) ≥ 7; distribution HC = 7: 5 117, 8: 481,
12: 94, 15: 21, 16: 1, 20: 4, 23: 1.
EVIDENCE: the HC = 7 share (89.5 %) is close to P(HC = 7 | HC > 4) = 89.3 % in the z49 census to 10⁸, but the tails
differ (HC ≥ 15: 0.47 % in the family vs 1.32 % in that census; different ranges of p), so no "generic beyond line 4"
claim is made.

*Reading (Assessment).* 5p = (5m)² + 5: a near-square family. The mechanism is the T1 confinement (HCSHIFTS Lemma C(d))
deformed off the squares, in the direction FRONTIER §4 item 15 calls hardest. For X = 4 the Dickson route (FABLE
Prop 3.3(a)) needs p, (p + 4)/5, (4p + 1)/5 simultaneously prime; its Hardy–Littlewood density x/(log x)³ is a
CONJECTURE. Theorem Q needs one quadratic and gives (under Bateman–Horn) only √x/log x members. Neither hypothesis is
known to imply the other.

### 2.2 One-variable quadratic families: classification of formal shapes

Every integer-valued quadratic with positive leading coefficient and negative discriminant is, after an affine change of
variable, p = (y² + δ)/(4a) with integers a, δ ≥ 1 and y in a progression (4ap = y² + δ). Then
  4a(p + x) = y² + (δ + 4ax),  4ax(xp + 1) = (xy)² + x(xδ + 4a).
**Definition.** The family *confines line x* on a nonempty union 𝒴 of residue classes of y if (i) p(y) ∈ ℤ and
p(y) ≡ 1 (mod 8) and gcd(p(y), x) = 1 for y ∈ 𝒴 (so both window integers are coprime to x, as they are at every prime
p > x), and (ii) there are odd real characters χ_e, χ_l mod x such that for every y ∈ 𝒴 every prime factor ℓ of N_x^e(y)
has χ_e(ℓ) = 1 and every prime factor of N_x^l(y) has χ_l(ℓ) = 1. (Then no divisor is ≡ −1 (mod x). This is confinement
on all values, not only prime ones.) fd(−n) denotes the fundamental discriminant of −n; for |D| | x, χ_D^{(x)} denotes
χ_D induced to modulus x (zero at primes dividing x).

**Prop F1 (PROVED).** (⇒) If the family confines line x on some 𝒴, then D_e := fd(−(δ + 4ax)) and D_l := fd(−x(xδ + 4a))
satisfy |D| | x, χ_e = χ_{D_e}^{(x)}, χ_l = χ_{D_l}^{(x)} (equality of primitive inducing characters, induced to
modulus x), and D ≡ 1 (mod 8) when x ≡ 7 (mod 8). (⇐) Conversely, if these conditions hold, then for y in the family every
prime ℓ ∤ 2axgD (g as below) dividing N_x^∗ has χ_D^{(x)}(ℓ) = 1; the family confines line x on 𝒴 iff 𝒴 can be chosen
(nonempty, with (i), including gcd(p(y), x) = 1) to avoid the finitely many classes of y for which a prime ℓ | 2axgD with
χ_D^{(x)}(ℓ) ≠ 1 divides N_x^∗. (Cross-review counterexample to the earlier wording without induction/coprimality:
x = 20, a = 5, δ = 39600, y = 10t, p = 5t² + 1980: both primitive characters are χ₋₄ and the old test passed, but
5 | p + 20 always and every character mod 20 vanishes at 5. With (i) such shapes are excluded; F2–F5 at lines 4, 7, 8 and
Theorem E are unaffected.)
*Proof.* (⇐) δ + 4ax = |D_e|g² with 2g ∈ ℤ, so 16a(p + x) = (2y)² + |D_e|(2g)². A prime ℓ ∤ 2agD_e dividing p + x has
D_e ≡ (2y/2g)² (mod ℓ), so χ_{D_e}(ℓ) = 1, and χ_{D_e}^{(x)}(ℓ) = 1 when also ℓ ∤ x; χ_{D_e}^{(x)} is a character mod x
(|D_e| | x) and odd (D_e < 0). Primes dividing x are kept out of N_x^∗ by gcd(p(y), x) = 1. For x ≡ 7 (8),
N_x^e is even and 2 must satisfy χ(2) = 1, i.e. D_e ≡ 1 (mod 8). The remaining primes are the stated local conditions.
Level line: the same with 4ax(xp + 1) = (xy)² + x(xδ + 4a). (⇒) Suppose χ_e ≠ χ_{D_e} as characters on primes. Both are
real, so by Chebotarev in the biquadratic field infinitely many primes ℓ have χ_{D_e}(ℓ) = 1, χ_e(ℓ) = −1. For such ℓ not
dividing 2a·(numerators/denominators)·(modulus of 𝒴), y² ≡ −(δ + 4ax) (mod ℓ) has two solutions, which meet every class
of 𝒴 by CRT; then ℓ | N_x^e(y) with χ_e(ℓ) = −1, a contradiction. So the primitive character inducing χ_e is χ_{D_e},
whose conductor |D_e| must therefore divide x, and χ_e = χ_{D_e}^{(x)},
and the 2-adic condition is forced as in (⇐). Same for the level line. ∎

**Prop F2 (PROVED; line 4, formal).** If the family confines line 4, then, up to a common rational square factor,
(a, δ) = (U² − W², 16W² − U²)/15 with U, W ∈ ℚ, 1 < |U/W| < 4.
*Proof.* For x = 4 the only allowed D is −4, and fd(−n) = −4 iff n ∈ ℚ^{×2} (n > 0). So δ + 16a = U² and
4(4δ + 4a) ∈ ℚ^{×2}, i.e. δ + a = W². Solve; a, δ > 0 iff 1 < |U/W| < 4. ∎
Not every such point gives a family: e.g. (U, W) = (3, 1) gives (a, δ) = (120, 105) (after scaling), and
y² + 105 ≡ 0 (mod 480) is impossible mod 4. Theorem Q is (U, W) = (2, 1): (a, δ) = (5²/15)·(3, 12) = (5, 20), y = 40s,
p = 80s² + 1. `scripts/z54_hckill_fam4.py` lists integral-admissible shapes with p ≡ 1 (8), e.g. (a, δ) = (5, 116):
p = 1280t² + 128t + 9, with t-classes where 7 | y or 11 | y excluded (local conditions of F1; for these, δ + a = 11²,
δ + 16a = 14², so 4a(p + 4) = y² + 14² and a(4p + 1) = y² + 11²).

**Prop F3 (lines {4, 7}; formal reduction PROVED, rank CERTIFIED).** With (a, δ) as in F2, `scripts/z54_hckill_genus.py`
gives δ + 28a = (9U² − 4W²)/5 and 7(7δ + 4a) = 7(36W² − U²)/5 (exact symbolic identities). The only allowed D for x = 7
is −7, so the formal line-7 conditions are 9U² − 4W² ∈ 35ℚ^{×2} and 36W² − U² ∈ 5ℚ^{×2}. Parametrising the second conic
through (U, W, r) = (4, 1, 2) by U/W = 4(5m² − 5m − 1)/(5m² + 1) turns the first into
  E₇ : Y² = 7(m − 1)(5m − 7)(5m + 1)(7m + 1),
a curve of genus 1 with rational points, an elliptic curve of conductor 735 with torsion ℤ/2 × ℤ/2 and **rank 1**
(PARI `ellrank` bounds [1, 1]). ellrank's point (−1440, 31200) on the model [0, 532, 0, −1599360, 553190400] equals 3H
for H = (480, −4320); `ellsaturation` (all primes ≤ 100) returns H, ĥ(H) = 0.3446. So infinitely many formal ratios
(a : δ) satisfy the line-4 and line-7 square-class conditions.
EVIDENCE (`data/z54/hckill/e7_points.txt`, `scripts/z54_hckill_e7group.py`): the points nH + T, |n| ≤ 16, T torsion,
give 17 distinct ratios; 10 fail the real condition 1 < U/W < 4, and each of the other 7 gives an a with an odd prime
factor ℓ < 10⁶, ℓ ∤ δ, with (−δ/ℓ) = −1 (e.g. ℓ = 19 for the smallest, (a, δ) = (2109, 5460); others 3, 31, 1123,
1483, …). Since δ + a = W_eff² (an integer square after scaling), ℓ | a gives δ ≡ W_eff² (mod ℓ), so these are primes
ℓ ≡ 3 (mod 4) (ℓ ∤ W_eff); then 4a | y² + δ is impossible and the shape gives no integers. (The script's line-7 recheck
uses partial factorisation and is unreliable for the 100+-digit numbers; E₇ membership holds by construction. A first
run enumerated only multiples of 3H; corrected.) No simple congruence obstruction is visible: the necessary condition
A′ ≡ 1 (mod 4) for A′ = (U² − W²) stripped of 2, 3, 5 holds at the real points n = −9, −13, −17 and fails at the
other real points with |n| ≤ 20 (`scripts/z54_hckill_e7mod.py`, `e7_mod.txt`). Whether any point of E₇ is integral-admissible
is undetermined.
Assessment: a ∝ (U − W)(U + W) would need both factors free of such primes, heuristically probability ≍ (ĥn²)⁻¹ at the
n-th point, a convergent sum — so finitely many, possibly none.

**Prop F4 (lines {4, 7, 8}; PROVED, using Faltings).** Line 8 allows D ∈ {−4, −8}; its formal conditions are
15(31U² − 16W²) ∈ ε₁ℚ^{×2} and 15(31W² − U²) ∈ ε₂ℚ^{×2}, ε₁, ε₂ ∈ {1, 2} (from δ + 32a = (31U² − 16W²)/15 and
8(8δ + 4a) = 32(31W² − U²)/15). For each (ε₁, ε₂), the four conditions of lines 7, 8 define a (ℤ/2)⁴-cover of
P¹_{U:W} branched exactly at the 8 distinct simple zeros U/W ∈ {±2/3, ±6, ±4/√31, ±√31} of the four squarefree, pairwise
coprime binary forms (no branching at ∞, even degrees), so no nonempty product of them is a square and the cover is
geometrically irreducible; Riemann–Hurwitz gives 2g − 2 = 16·(−2) + 8·8, **g = 17** (`genus_check.txt`). By Faltings
each of the four curves has finitely many rational points. Hence by F1(⇒) **only finitely many ratios (a : δ) can confine
all lines of 𝒞 ∩ [4, X] for any X ≥ 8.** Their existence and maximal reach are undetermined. ∎

**Prop F5 (PROVED; no growing window from one family).** If a family confines line q for a prime q ≡ 7 (mod 8), then
q | δ. *Proof.* By F1(⇒), χ_e is the only odd real character mod q, χ₋q, so δ + 4aq ∈ qℚ^{×2} has odd q-adic valuation, q | δ + 4aq ≡ δ (mod q). ∎ So a fixed family confines only finitely many prime
lines q ≡ 7 (8), and no single quadratic family certifies HC > X for all X (its members may have larger HC by chance).

### 2.3 Two variables (Prop F6, PROVED; scoped)

**Prop F6.** Let F(s, t) ∈ ℚ[s, t] be quadratic with nondegenerate quadratic part, and N_i = λ_iF + μ_i (λ_i, μ_i ∈ ℚ^×)
affine functions of F with μ_i/λ_i pairwise distinct (e.g. p + x and xp + 1 for x ∈ 𝒞). Then at most one N_i has the
property "every prime factor ℓ outside a finite set satisfies χ_i(ℓ) = 1 for some real χ_i ≠ 1, for all (s, t) in a
full-rank lattice coset" (full rank is needed for the CRT step; restricting F to a rank-one coset is a one-variable
family and can recover Theorem Q).
*Proof.* Complete squares: F = Q(s′, t′) + c with Q a nondegenerate binary quadratic form and s′, t′ affine in s, t. Then
N_i = λ_i(Q + e_i), e_i = c + μ_i/λ_i, and e_i = 0 for at most one i. For e_i ≠ 0 and every prime ℓ not dividing
2·disc(Q)·e_i·(all denominators/numerators)·(coset modulus), Q(s′, t′) ≡ −e_i (mod ℓ) is solvable (a nondegenerate
binary quadratic form over 𝔽_ℓ represents every nonzero element), the solutions meet the coset by CRT, so ℓ divides some
value of N_i; infinitely many such ℓ have χ_i(ℓ) = −1. ∎
*Scope.* Even the one exceptional N_i (e_i = 0, a form value) is confined only at primitive points, not on a full coset
(an inert prime can divide both coordinates). F6 covers only quadratic F; it says nothing about Friedlander–Iwaniec
x² + y⁴-type polynomials, higher-degree or multi-variable constructions. Within its scope, two window integers cannot be
confined by one two-variable quadratic, so Theorem Q-type kills need a one-variable quadratic (hence Bunyakovsky).

## 3. Sieve analysis: which steps are tractable

Hypothesis **EH(θ)** (θ < 1 fixed): for every A, Σ_{q ≤ x^θ} max_{(c,q)=1} |π(x; q, c) − li(x)/φ(q)| ≪_{A,θ} x/(log x)^A.
BV gives EH(1/2 − ε); the standard Elliott–Halberstam conjecture (e.g. Ford's notes, (7.6), Conj. 7.3, with an extra max
over y ≤ x) implies EH(θ) for every fixed θ < 1. FI 2009's A(θ) is the ψ-version with max over y ≤ x at Q = x^{θ−ε};
translating between the fixed-exponent versions needs a small exponent margin, which does not affect "some θ₀ < 1".

### 3.1 Theorem E (CONDITIONAL on EH(1 − η₀) for an absolute η₀ > 0)

**Theorem E.** There is an absolute η₀ ∈ (0, 1/10] such that EH(1 − η₀) implies
  #{p ≤ x : p ≡ 1 (mod 8), p + 4 ∈ S, 4p + 1 ∈ S} ≫ x/(log x)²  (x ≥ x₀).
In particular K(4), with ≫ x/(log x)² primes p ≤ x having HC(p) ≥ 7: the order of FABLE Thm 3.2's upper bound.

*Proof.* Fix η ∈ (0, 1/10] (chosen in Step 5), θ = 1 − η, z = x^{1/2−η}, D = x^θ/8.

*Step 1 (sieve setup).* Sift 𝒜 = {(p + 4)(4p + 1) : p ≤ x, p ≡ 1 (8)} by 𝒫_z = {ℓ ∈ 𝒫 : ℓ < z}. For squarefree d composed
of 𝒫-primes let R(d) = {b mod d : (b + 4)(4b + 1) ≡ 0}; |R(ℓ)| = ν(ℓ) = 2 for ℓ ∈ 𝒫 ∖ {3} (the roots −4 and −4⁻¹
coincide iff ℓ | 15) and ν(3) = 1; every root is a unit mod ℓ. Then
  |𝒜_d| = Σ_{b ∈ R(d)} π(x; 8d, c_b) = g(d)·X + r_d,  X = li(x)/4,  g(d) = ν(d)/φ(d),
with c_b ≡ 1 (8), ≡ b (d), and |r_d| ≤ ν(d)·max_c|π(x; 8d, c) − li(x)/φ(8d)|. Since ν(d) ≤ 2^{ω(d)}, Cauchy–Schwarz with the
trivial bound max_c|…| ≪ x/φ(q) and EH(θ) give Σ_{d < D} μ²(d)3^{ω(d)}|r_d| ≪_A x/(log x)^A. The density satisfies the
linear (κ = 1) sieve axioms: 0 ≤ g(ℓ) ≤ 1/2, and ∏_{w ≤ ℓ < z, ℓ ∈ 𝒫}(1 − g(ℓ))⁻¹ = (log z/log w)(1 + O(1/log w)) since
∏_{ℓ ∈ 𝒫, ℓ < y}(1 − 1/ℓ)² = c/log y·(1 + O(1/log y)) (Mertens' product in the progression 3 mod 4; exponent 1 because
there are two roots on half the primes).

*Step 2 (lower bound).* The beta (Rosser–Iwaniec) linear sieve under the product-condition axiom
∏_{w≤ℓ<z}(1 − g(ℓ))⁻¹ ≤ (log z/log w)^κ(1 + K/log w), κ = 1, β = 2 (as stated in Nath–Xie, arXiv:2501.16723, (3.4) and
Lemma 3.6, verified by the cross-review; the Jurkat–Richert theorem of Halberstam–Richert's book is the classical form,
theorem numbering not independently verified) gives, for s = log D/log z ≥ 2,
  S(𝒜, 𝒫, z) ≥ X·V(z)·(f(s) − o(1)) − Σ_{d<D, d|P(z)} 3^{ω(d)}|r_d|,  f(s) = 2e^γ log(s − 1)/s (2 ≤ s ≤ 4),
V(z) = ∏_{ℓ ∈ 𝒫_z}(1 − g(ℓ)) ≍ 1/log x. Here s = (1 − η)/(1/2 − η) + o(1) = 2 + 2η/(1 − 2η) + o(1), so s − 2 ≥ 2η and
f(s) ≥ e^γ(s − 2)/s ≥ (2e^γ/3)η (log(1 + u) ≥ u/2 for 0 ≤ u ≤ 1). Hence S(𝒜, 𝒫, z) ≥ c₁η·x/(log x)², c₁ > 0 absolute,
for x ≥ x₀(η).

*Step 3 (survivors).* Let p be counted and N ∈ {p + 4, 4p + 1}. Then N ≡ 1 (mod 4), so N has an even number of
𝒫-prime factors (with multiplicity), all ≥ z; and N ≤ 4x + 1 < z³ (η ≤ 1/10, x large). So either N ∈ S, or
N = q₁q₂m with q₁ ≤ q₂ in 𝒫, q₁ ≥ z, m ∈ S, m ≤ (4x + 1)/z² ≤ 5x^{2η}. Hence #target ≥ S(𝒜, 𝒫, z) − |Bᵉ| − |Bˡ|, Bᵉ (resp.
Bˡ) the counted p with p + 4 (resp. 4p + 1) of the second shape.

*Step 4 (bad configurations; unconditional).* Bᵉ: each p ∈ Bᵉ gives a triple (m, q₁, k) with m ∈ S, m ≤ 5x^{2η},
q₁ ∈ 𝒫, z ≤ q₁ ≤ k ≤ Y := (x + 4)/(mq₁), k (= q₂) prime, mq₁k − 4 (= p) prime, and 4mq₁k − 15 (= 4p + 1) free of
𝒫-primes below z. Only pairs with Y ≥ q₁ occur, and then Y ≥ z ≥ x^{0.4}. For fixed (m, q₁) sift the integers
k ∈ [q₁, Y] by the primes ℓ < w := x^{1/100} at k ≡ 0, at k ≡ 4(mq₁)⁻¹ (ℓ ∤ 2mq₁), and, for ℓ ∈ 𝒫, ℓ ∤ 15mq₁, at
k ≡ 15(4mq₁)⁻¹: at most 3 classes, fewer than ℓ for every ℓ, sieve dimension ≤ 5/2. All three quantities exceed w on
the triples counted (k ≥ q₁ ≥ z > w; p ≥ k; 4p + 1 has no 𝒫-prime below z > w), so every such k survives. The
upper-bound sieve for an interval of integers under the product-condition axiom of dimension ≤ 5/2 (K. Ford, *Sieve
Methods* lecture notes 2023, Thm 2.4, verified by the cross-review: uniform in the coefficients, remainder
O(w log²w) using |r_d| ≤ 3^{ω(d)}, negligible against Y(log x)^{−5/2}; deleting roots at ℓ | m only improves the axiom),
with constants depending only on the dimension, gives
  #k ≪ Y∏_{ℓ<w}(1 − ω(ℓ)/ℓ) ≪ Y·h(m)·(log x)^{−5/2},  h(m) = ∏_{ℓ | m}(1 + 2/ℓ)
(only ℓ | m change ω, since q₁ > w; the ℓ | m are ≡ 1 (mod 4), ℓ ≥ 5, and contribute (ℓ − 1)/(ℓ − 2) ≤ 1 + 2/ℓ relative
to the generic factor; local root counts: one at 2, two at 3, two at split ℓ ∤ m, three at inert ℓ ≥ 7, one at ℓ | m).
Summing,
  |Bᵉ| ≪ x(log x)^{−5/2}·Σ_{m ∈ S, m ≤ 5x^{2η}} h(m)/m·Σ_{q ∈ 𝒫, z ≤ q ≤ 3√x} 1/q.
The q-sum is (1/2)log((1/2)/(1/2 − η)) + o(1) ≤ 2η. The m-sum is ≤ ∏_{ℓ ≡ 1 (4), ℓ ≤ 5x^{2η}}(1 + (1 + 2/ℓ)/(ℓ − 1))
≪ (log x^{2η})^{1/2} ≪ (η log x)^{1/2} (x ≥ x₀(η)). So |Bᵉ| ≤ C₂η^{3/2}x/(log x)², C₂ absolute. Bˡ is identical with
4p + 1 = mq₁k: k runs over the class mq₁k ≡ 1 (mod 4) (substitute k = k₀ + 4j), p = (mq₁k − 1)/4 prime and
p + 4 = (mq₁k + 15)/4 sifted; ranges m ≤ 5x^{2η}, z ≤ q₁ ≤ k ≤ (4x + 1)/(mq₁).

*Step 5.* #target ≥ (c₁η − 2C₂η^{3/2})x/(log x)². Take η₀ = min(1/10, (c₁/4C₂)²). ∎

*Remarks.* (i) EH is used only for primes in progressions with the CRT-coherent residues of (n + 4)(4n + 1), with
divisor weights; no Type II input beyond that. (ii) η₀ is not computed (it depends on c₁, C₂). (iii) Theorem E is an independently written adaptation of the
Friedlander–Iwaniec 2009 template, not a citation: FI prove a different, r-weighted statement for the pair (p − 2, p + 2) (their §6 replaces r by the S-indicator b on one shift and sifts by 𝒫 to √x, "because,
if n ≡ 1 (mod 4) has one prime factor from P, it must have a second one"); here both shifts carry the S-indicator, which
the linear sieve plus the η^{3/2}-vs-η comparison handles. (iv) Density statement only; no prescribed prime is touched
(on the kill side none is needed).

### 3.2 What BV gives (Prop A, PROVED rel. BV and the linear sieve)

**Prop A.** For each fixed ζ with 0 < ζ < 1/4, #{p ≤ x : p ≡ 1 (8), (p + 4)(4p + 1) has no prime factor ≡ 3 (mod 4) below
x^ζ} ≫_ζ x/(log x)². At these primes line 4 can fire only through prime factors ≡ 3 (mod 4) of size ≥ x^ζ (at least two
of them in p + 4 or in 4p + 1).
*Proof.* Steps 1–2 with D = x^{1/2}(log x)^{−B} (BV; B chosen so the weighted errors are absorbed), z = x^ζ,
s → 1/(2ζ) > 2, f(s) > 0 (for ζ < 1/8, s > 4: use the general positive linear-sieve f, not the explicit formula on
[2, 4]). ∎

*The gap in this implementation (Assessment, with PROVED sieve-function arithmetic).* With θ = 1/2 the linear sieve needs
z < x^{1/4}; the survivors then include N = q₁q₂m with q₁ ∈ [x^ζ, x^{1/2}] and m up to x^{1−2ζ}. In the half-dimensional
model a sifted N is in S with probability ≍ √ζ, so the target is a fraction ≍ ζ of the survivors and the bad set is
≍ 1 − cζ of them; subtraction would need the bad set asymptotically (relative error o(ζ)), and counting it means counting
primes p = mq₁q₂ − 4 in a switched sequence (prime detection, parity-type); upper-bound sieves lose constant factors
there. So this implementation needs level θ₀ (Theorem E) instead of 1/2. Polymath8a (arXiv:1402.0811, abstract verified)
reaches exponent 1/2 + 7/300 for smooth squarefree moduli and CRT-coherent classes; no claim is made about the best
level available for linear-sieve weights.
*Vector sieve (PROVED arithmetic).* Two semi-linear components (Brüdern–Fouvry), each integer sifted to ≈ x^{1/2}, with
levels D₁D₂ = x^θ, need f₁/F₁ + f₂/F₂ > 1 with s₁ + s₂ = 2θ. For κ = 1/2, f(s) = 0 for s ≤ 1, F(s) = 2(e^γ/πs)^{1/2} and
f(s) = (e^γ/πs)^{1/2}∫₁^s dt/√(t(t−1)) on [1, 2], so f/F = log(√s + √(s − 1)) = arccosh √s there, concave. Allocations
with some s_i ≤ 1 cannot succeed (they would need f/F > 1 for the other); for 2θ ≤ 3 the others have s_i ∈ (1, 2), where
concavity makes the symmetric choice optimal: success iff arccosh √θ > 1/2, i.e. θ > cosh²(1/2) = 1.27154.
*Expected unconditional variant (Assessment, not proved).* Nath–Xie's vector-sieve framework (arXiv:2501.16723) with
p + 4 in the semi-linear slot (S exactly) and 4p + 1 sifted by 𝒫 up to x^δ.

### 3.3 K(7) and beyond (Assessment, scoped to the direct confinement-sieve implementation)

HC(p) > 7 needs lines 4 and 7 dead. Line 7 is not a pure subgroup condition (Lemma 1.2(c)); its sieve-tractable
sufficient condition is confinement by χ₋₇ for p + 7 and 7p + 1 (Lemma 1.2(b)), with (p/7) = 1 necessary (HCSHIFTS
Lemma C(e)). Four half-dimensional conditions give sieve dimension κ = 2; to use the two-large-primes trick each integer
(size ≍ x) must be sifted to ≈ x^{1/2}, and at level D = x this is s = 2, below the dimension-2 sifting limits DHR
β₂ = 4.266 and Λ²Λ⁻ β₂ = 4.516 (Franze, arXiv:1012.3809, Table 1, verified). Sifting only to x^{1/β₂} leaves a bad set
that is most of the survivors (target fraction ≍ ζ² in the model), again requiring asymptotic, parity-type counts. So
this implementation gives no K(7) lower bound even under EH. The anatomy route for line 7 (e.g. p + 7 = 8q, q prime)
is a prime-pattern condition. For growing X there are ≈ 3X/8 lines, i.e. ≈ 3X/4 half-dimensional restrictions
(nominal dimension ≈ 3X/8): no sieve route is visible. Recorded conditional reaches: Dickson (any fixed X), UBH
(X ≍ log p/log log p), Bunyakovsky for one quadratic (X = 4; X = 7 only if E₇ has an integral-admissible point).

## 4. Literature (research subagent `data/z54/hckill/lit_report.md` + internal review; coverage-limited, Assessment)

* **Friedlander–Iwaniec, "Hyperbolic prime number theorem", Acta Math. 202 (2009) 1–19** (missed by the first sweep,
  found by the internal reviewer; statements read from the published PDF text): Thm 4, "If A(θ) holds for some θ, less
  than 1 but sufficiently close to 1", then Σ_{n≤x} r(n−2)r(n+2)Λ(n) ≍ x; the upper bound is unconditional. A(θ) is
  E(x, Q) ≪ x(log x)^{−A} at Q = x^{θ−ε} (ψ-version, max over y ≤ x). Equivalent forms: primes x₁² + x₂² + x₃² + x₄² with
  x₁x₄ − x₂x₃ = 1 (Thm 3). Their §6 uses the S-indicator b on one shift and the semi-linear sieve by 𝒫 to √x. This is
  the closest result: same conditional strength and method as Theorem E, for the det-1 shell and the pair (p − 2, p + 2),
  with r-weights on one shift. Theorem E is that template for the det-15 shell (Remark 1.3) with S on both shifts.
* No source found proves P(4,15) unconditionally, or any "prime p with two shifts both sums of two squares / in S"
  unconditionally. Not a formal open-problem citation.
* Closest unconditional: K. Nath, L. Xie, arXiv:2501.16723, Thm 1.1 (verified in the HTML): #{p ≤ x : p = m² + n² + 1,
  Ω(p + 2) ≤ 11} ≫ x/(log x)^{5/2}; vector sieve with a semi-linear and a linear component. Their introduction cites FI
  2009 ("Assuming the Elliott–Halberstam Conjecture … x ≪ Σ_{n≤x} Λ(n)r(n−2)r(n+2) ≪ x").
* Iwaniec, Acta Arith. 21 (1972): primes φ(x, y) + A (one shifted value a norm); theorem numbering UNVERIFIED (scan not
  text-extractable). Hooley (as reported by Cochrane–Dressler): n, n + h, n + k sums of two squares for integer n.
* Polymath8a, arXiv:1402.0811 (abstract verified): exponent 1/2 + 7/300 for smooth squarefree moduli, CRT-coherent classes.
* Franze, arXiv:1012.3809, Table 1 (verified): sifting limits β₂ = 4.266 (DHR), 4.516 (Λ²Λ⁻).

## 5. Numerics, controls

* **Counts (CERTIFIED exact; `scripts/z54_hckill_census.c`, sieve by 𝒫-primes ≤ √(4x+1), exact by the parity argument
  of Step 3).** #{p ≤ x : p ≡ 1 (8), HC(p) > 4}: 295, 2 226, 16 125, 125 059, 986 400, 7 962 940 at x = 10⁵…10¹⁰
  and 65 618 311 at 10¹¹ (6 min) (10⁸ agrees with the z49 census 1 439 970 − 1 314 911). Ratio to x/(log x)²: 0.391,
  0.425, 0.419, 0.424, 0.424, 0.422, 0.421. Files `census_hc4_1e10.txt`, `census_hc4_1e11.txt`.
* **Heuristic constant (EVIDENCE for the CONJECTURE count ~ prediction).** Half-dimensional model: count ≈ C∫₂^x dt/(log t·√(log(t+4)·log(4t+1))) with
  C = 4K²𝔖, K² = (1/8)∏_{ℓ∈𝒫}(1 − ℓ⁻²) (S has #S(x) ~ Kx/√log x, K = 0.3271), 𝔖 = (9/8)∏_{ℓ∈𝒫, ℓ≥7}
  ℓ²(ℓ − 3)/(ℓ − 1)³ = 0.9602, C = 0.4110 (factor 4 = 16·(1/4): P(N ∈ S | N ≡ 1 (4)) = 4K/√log N for each of the two
  integers, which are ≡ 5 (8), and S splits evenly between 1 and 5 (mod 8); 1/4 = share of p ≡ 1 (8); c_ℓ =
  (1 − ν(ℓ)/(ℓ−1))/(1 − 1/ℓ)² the prime-shift correction). Observed/predicted: 0.811, 0.914, 0.922, 0.948, 0.957,
  0.962, 0.966 (10⁵…10¹¹),
  rising towards 1 (half-dimensional lower-order terms). With the unshifted C∫dt/(log t)² the ratios are ≈ 0.76 → 0.94.
  Consistent with Theorem E's order. Script: inline mpmath product over ℓ < 10⁷ (`/tmp/pred.py` in the session;
  reproduced by the internal reviewer).
* **Controls (PROVED/CERTIFIED as stated).** Odd squares n = m²: m² + 4 and 4m² + 1 are primitive sums of two squares, so line 4 is confined at every
  odd square (T1; HCSHIFTS Lemma C(d)); δ = 0 is the degenerate member of Prop F2 (p = (y/2)²). The FRONTIER §4 item-14
  test primes: HC(409) = HC(577) = 4 (line 4 fires; (★)-zeros are not HC-hard), HC(193) = 7, HC(2521) = 15,
  HC(3361) = 7, HC(5569) = 7, HC(9601) = 7, HC(66529) = 8, HC(8813281) = 8 (FABLE §1.5 table): the HC > 4 ones satisfy
  Lemma 1.1 (e.g. 193 + 4 = 197, 4·193 + 1 = 773, both prime ≡ 1 (4)). Theorem Q members are near-squares (5p − 5 = (5m)²).


## 6. FRONTIER §4 hard screens (Assessment; best items: Theorem E, Theorem Q; kill side)

1. **T1 squares.** A kill should *hold* at squares, and the mechanism does: confinement is the T1 mechanism (all lines dead
   at odd m²). Theorem Q deforms it to near-squares; Theorem E's content is the distribution of primes. (Screen 1
   constrains upper-side proofs; the kill side is consistent with it.)
2. **8/131, 8/241.** Lemma 1.1 is 4-specific: 𝒞 and the line-4 criterion come from FABLE Thm 1, which is 4-specific
   (FABLE §1.5).
3. **Tied modulus.** Not applicable on the kill side: each line is avoided by a fixed character mod x, which is why kills
   are cheap while positivity is not.
4. **Fixed p.** Theorem Q is pointwise (HC(p) ≥ 7 at each member, PROVED); infinitude is CONDITIONAL. Theorem E is a
   density statement (adequate for kills, useless for ES).

## 7. Proposed FRONTIER §7.2 text (do not edit FRONTIER here)

> *(z54, `Z54_HCKILL.md`; kill side.)* **K(4) ⟺ P(4,15)** (PROVED): for p ≡ 1 (8), HC(p) > 4 iff p + 4, 4p + 1 ∈ S (all
> prime factors ≡ 1 (4)); every kill K(X), X ≥ 4, implies this S-refined two-shift prime statement, the det-15 analogue
> of Friedlander–Iwaniec's hyperbolic prime number theorem. Lines x | 24 are pure subgroup conditions; the others are
> confinement-or-anatomy events. **Theorem Q** (PROVED): every prime 5m² + 1 with 4 | m has HC ≥ 7, so K(4) follows
> from Bunyakovsky for 720k² + 1 alone (CERTIFIED on 5 719 primes ≤ 10¹²). Formal quadratic confinement shapes: a
> two-variable quadratic confines at most one window integer; lines {4,7} ↔ the rank-1 elliptic curve E₇ (no integral
> shape among 17 sampled ratios, EVIDENCE); lines {4,7,8} ↔ genus-17 curves, finitely many ratios (Faltings); existence
> beyond X = 4 undetermined. **Theorem E** (CONDITIONAL on EH(1 − η₀), some absolute η₀ > 0; FI-2009 template):
> ≫ x/(log x)² primes p ≤ x have HC(p) > 4 (true order). With BV the same sieve gives only "no 3-mod-4 prime factor
> below x^ζ, ζ < 1/4" (PROVED); in that implementation the gap is a level deficit or a parity-type switched count. The
> direct confinement sieve gives no K(7) bound even at level 1 (dimension 2, s = 2 < β₂ ≈ 4.27). Unconditional
> "HC unbounded" remains open and needs at least P(4,15); for fixed X ≥ 7, Dickson is still the recorded route.

**Bottom line (Assessment).** The first rung of the HC kill hierarchy, K(4), is exactly an S-refined two-shift prime
problem, a det-15 "hyperbolic prime number theorem". It follows from an Elliott–Halberstam-type level θ₀ < 1
(Theorem E, Friedlander–Iwaniec's template) or from Bunyakovsky for one near-square quadratic (Theorem Q), but not from
the BV-level sieves analysed. For X ≥ 7 the recorded route is still Dickson. The algebraic near-square mechanism leaves
only finitely many formal shapes beyond X = 7, and none is known to be realisable beyond X = 4. No unconditional
HC > 4 i.o. is proved, and nothing here touches positivity at a prescribed prime. For the upper side: line-4-dead
primes have count ≍ x/(log x)² (EVIDENCE; lower bound under EH by Theorem E) and include near-square families, so any
proof of HC ≤ X must certify from lines ≥ 7 at those primes.

## 8. Reproduction (every command was run under `timeout` and `ulimit -v ≤ 6000000`)

* `uv run --with sympy python scripts/z54_hckill_famgen.py 1000000000000 > data/z54/hckill/fam_5m2p1_primes_1e12.txt`;
  `gcc -O2 -o hc scripts/z53_hcshifts_hc.c -lm; ./hc list 128 4096 < …primes_1e12.txt > …/fam_5m2p1_hc_1e12.txt`.
* `gcc -O2 -o cens scripts/z54_hckill_census.c -lm; ./cens 10000000000` (32 s), `./cens 100000000000` (6 min).
* `uv run --with cypari2 --with sympy python scripts/z54_hckill_e7group.py 9 16` (E₇ points);
  `uv run --with cypari2 python scripts/z54_hckill_e7.py 3000 64` (hyperellratpoints search, height 3000);
  `uv run --with sympy python scripts/z54_hckill_genus.py` (forms, branch points, genus);
  `uv run --with sympy python scripts/z54_hckill_fam4.py 60` (integral-admissible line-4 shapes with p ≡ 1 (8));
  `gcc -O2 scripts/z54_hckill_qfam.c -o qfam; ./qfam 300 64 1` (825 integral-admissible formal line-4 shapes with
  U ≤ 300; none satisfies the formal line-7 conditions).
* Heuristic constant: inline mpmath script recorded in §5 (product over ℓ < 10⁷).

## 9. Review log

* **Internal hostile review** (deep-mode subagent; report `data/z54/hckill/internal_review.md`): verdict "major
  revision, no FATAL". It re-verified Lemmas 1.1–1.2, Theorem Q (all 5 719 members re-run byte-identically), the F2–F5
  algebra, E₇ (conductor 735, rank bounds [1, 1], torsion C₂ × C₂), genus 17, the census to 10¹¹, the constant
  C = 0.4110 and the test-prime HC values. Fixes applied: (1) confinement definition with separate endpoint/level
  characters, integrality and p ≡ 1 (8) built in, exceptional primes allowed when χ = +1; (2) F2–F4 restated as
  classifications of *formal* square-class shapes (example (120, 105) of a non-integral shape); (3) F6's false Iwaniec
  example removed, scope narrowed (primitive points, quadratic F only); (4) Theorem E Step 4 repaired (k ≥ q₁ retained,
  Y ≥ z, auxiliary cutoff w = x^{1/100}, level Y^{1/2}); (5) **Friedlander–Iwaniec 2009 added**; Theorem E presented
  as their template, novelty claim reduced; (6) scope of Faltings/K(7)/Dickson statements weakened; (7) labels split;
  (8) 𝒫 q-sum factor 1/2; (9) E₇ ratio count corrected (and, after the review, the enumeration redone with the
  saturated generator H, G = 3H: 17 ratios); (10) "infinite-order point", W_eff; (11) the predicted
  integral is the shifted-log one; (12) no "generic tail" claim for the family; (13) half-dimension count; (14) vector
  sieve optimality argument, threshold cosh²(1/2); (15) Dickson infinitude vs HL density separated; (16) "formal shapes";
  (17) 0 < ζ; (18) generator script checked in.
* **Cross-model review** (`data/z54/xreview/REVIEW_HCKILL.md`, checker `scripts/z54_xrev_hckill_check.py`): verdict
  ACCEPT-WITH-FIXES. It audited Theorem E step by step under ordinary EH (survives), re-ran the census to 10¹¹, the
  family, the HC controls and E₇/genus independently (all agree). Fixes applied: (1) **F1's local converse was false as
  written** (counterexample x = 20, a = 5, δ = 39600: primes dividing x but not the conductor); repaired by inducing χ_D
  to modulus x, adding 2axgD to the exceptional primes and requiring gcd(p(y), x) = 1 in the definition; F2–F5 and
  Theorem E unaffected; (2) sieve citations replaced by verified product-condition statements (Nath–Xie (3.4)/Lemma 3.6;
  Ford's notes Thm 2.4), with the local root counts and uniformity recorded; Mertens exponent 1 made explicit;
  (3) EH(θ) stated for fixed θ with its relation to standard EH and FI's A(θ); Theorem E marked as an independent
  adaptation, not FI's theorem; "17 sampled ratios" (not smallest); F6 requires a full-rank coset; q₁-range 3√x;
  Prop A remark for ζ < 1/8.
