# MENU_STERILITY — sterility is menu-relative (task O240, spark relay Z9)

Status: O240 work in progress (unreviewed). **ES is not solved here, and no infinite case of ES for primes is claimed.**
Labels as in DISCOVERIES.md. Memos `BRAINSTORM/z15_*.md`; scripts `scripts/z15_*`.
Builds on SYNTHESIS_SPARKS6 (O238, Thm 1.1: ES for all 4^s + 105), EXPONENT_COVERING ((J)22 Thm 1.2/1.4, Cor 1.5),
NEAR_SQUARE ((J)55 Lemmas 1.1/1.3, Thm 2.2, 3.3, 3.4), POINTWISE_BINARYFORM ((J)3 Thm 3.2, §4.1), CAP_DOWN (Lemma 1.1 windows).

## 0. Iteration log
(I1) Reading. Every B1 barrier in the list is proved by the same two-step mechanism: (a) a *pointwise witness*
(NEAR_SQUARE Lemma 1.1/1.3: every Type I/II solution of odd n carries D with (D/n) = −1), (b) a *gluing statement* that
the parameter set of the menu item contains points where (D/n) = +1 is forced (actual odd squares: Schinzel, (J)3,
Thm 3.3; or Hilbert reciprocity in the parameter algebra: Thm 3.4). Step (a) is menu-independent. Step (b) is where the
menu enters: it is a statement about the *parameter algebra* A = ℚ[u]/(φ) of the family n = φ(u).
(I2) Plan: generalise Thm 3.4 to every φ (§1, "witness reciprocity"), identify the sterile set of a one-parameter menu as a
2-descent object of the double cover w² = φ(u) (§2), read O238's 105 point and the near-square sets through it (§3),
then attack the uncoverable Proth family 3·2^m + 1 of (J)22 with root menus (§4), and the (J)54 prime points (§5).
(I3) Framing repair (orchestrator, R246 D2 on O238): no point of Λ₁₀₅ was ever shown sterile for ET/divisor classes, so the
105 theorem is NOT an instance of "a sterile point dissolved". The test cases must be PROVED sterile points: (T-a) μ = 0 of
c·2^s + 1 with c + 1 = 4^i (EXPONENT_COVERING Cor 1.5; e.g. 3·2^s + 1), and the c₀·4^s + k, c₀ + k = 4^j families of (J)68;
(T-b) the (J)54 sterile Mordell points. "Sterile" below is always relative to an explicitly named menu.

## 1. Witness reciprocity for one-parameter menus (Theorem A)

Setting. φ ∈ ℤ[u] squarefree, positive leading coefficient, deg φ ≥ 1; A := ℚ[u]/(φ) (an étale algebra, product of number
fields), θ := class of u. A *Type I/II polynomial family for n = φ(u) on the class C = {u ≡ g mod T}* is (a, …, f) ∈ ℚ[u]⁶
on Σᴵ_{φ(u)} resp. Σᴵᴵ_{φ(u)} identically, with positive integer values at all large u ∈ C (NEAR_SQUARE §2 with m ↦ u).
Witness: D = −d (Type I) resp. D = f (Type II); by NEAR_SQUARE Lemmas 1.1/1.3, (D(u)/φ(u)) = −1 at every large u ∈ C
with φ(u) ≡ 1 (mod 8) (Jacobi symbol; for n ≡ 1 (8) the Kronecker (−4d/n) equals (−d/n)).
The menu M₁[φ] := all such families (any degree, any class). M₁[linear] = ET classes (polynomial in n).

**Definition (descent-sterile set).** Ster(φ) := the set of u* ∈ Ẑ such that (i) φ(u*) ∈ Ẑ^× and φ(u*) ≡ 1 (mod 8);
(ii) there is a totally positive γ ∈ A^× (positive at every real place of A) with γ·(u* − θ) ∈ (A ⊗ ℚ_ℓ)^{×2} for every prime ℓ.

**Theorem A (witness reciprocity; PROVED).** No family of M₁[φ] has a class C whose closure in Ẑ meets Ster(φ).
*Proof.* Let D = D̃/g with D̃ ∈ ℤ[u], g ∈ ℕ, and α := D̃(θ) ∈ A. If α is a zero divisor, a non-constant common factor h of
D̃ and φ gives h(u) | gcd(D̃(u), φ(u)) with |h(u)| > 1 for large u; as g is fixed, h(u)/gcd(h(u), g^∞) > 1 for large u still
divides gcd(D(u)·g, n), so (D/n) = 0 ≠ −1; hence α ∈ A^×. Let u* ∈ Ster(φ) ∩
closure(C) with its γ, and let S be a finite set of primes containing 2, the primes of g, lc(φ), disc(φ), the conductor
of the order ℤ[1/lc(φ)][θ] away from lc(φ) (R-O240 repair: ℤ[θ] need not be an order), and all primes below places where α or γ is not a unit. Pick u ∈ C, u larger than every real
root of φ, with u ≡ u* modulo a high power of every ℓ ∈ S (possible by CRT as u* ∈ closure(C)); then φ(u) ≡ φ(u*) is
prime to S, φ(u) ≡ 1 (8), and (u − θ)/(u* − θ) ∈ (A ⊗ ℚ_ℓ)^{×2} for ℓ ∈ S (u* − θ is invertible in A ⊗ ℚ_ℓ as φ(u*) ≠ 0;
squares are open). For a prime q ∉ S, q | φ(u): u − θ is integral at the places 𝔮 | q, v_q(φ(u)) = Σ_{𝔮|q} f_𝔮 v_𝔮(u − θ),
and (X/q)^{f_𝔮} = (X/𝔮) for X ∈ ℤ prime to q. As D̃(u) ≡ α (mod 𝔮) when 𝔮 | u − θ, and q ∤ D̃(u) (else (D/n) = 0),
  (D̃(u)/φ(u)) = Π_{𝔮∉S} (α/𝔮)^{v_𝔮(u−θ)} = Π_{𝔮∉S} (α, u−θ)_𝔮 = Π_{v∈S∪∞} (α, u−θ)_v = Π_{v∈S∪∞} (α, γ(u−θ))_v,
using the tame-symbol formula at 𝔮 ∉ S, Hilbert reciprocity in each component field, and Π_v (α, γ)_v = 1 with
(α, γ)_𝔮 = 1 for 𝔮 ∉ S. At v | ℓ ∈ S, γ(u − θ) is a square; at real v, γ > 0 and u − θ > 0. Hence (D̃(u)/φ(u)) = +1;
the same computation with α = g gives (g/φ(u)) = +1, so (D(u)/φ(u)) = +1, contradicting −1. ∎

Special cases (all previously proved separately; Theorem A unifies them):
* φ = qu + r (ET classes): A = ℚ, γ = q·(square) turns (ii) into "φ(u*) is a profinite unit square" — Schinzel/Mordell
  (ET p. 7–8) and EXPONENT_COVERING Thm 1.2, Sq^× ⊂ S.
* An integer u₀ larger than every real root with φ(u₀) = 1: γ := (u₀ − θ)⁻¹ is totally positive, so u₀ ∈ Ster(φ). (R-O240 repair:
  an integer T1 point with φ(u₀) an odd square > 1 is NOT a unit point, hence not in Ster(φ); it is obstructed by NEAR_SQUARE
  Thm 3.3 directly — the "largest real root" there plays the role of total positivity of γ here.)
* φ = m² − j: γ = 1 gives NEAR_SQUARE Thm 3.4 (Z_K⁺); Theorem A adds the twists by totally positive γ.
* Two variables: the same computation with A = the norm-form algebra is the mechanism behind POINTWISE_BINARYFORM §4.1.

## 4. Test case (T-a): the PROVED-sterile point μ = 0 of 3·2^s + 1

Recall (EXPONENT_COVERING Cor 1.5, PROVED): for n_s = 3·2^s + 1 the limit point ν(0) (n ≡ 4 at every odd ℓ, n ≡ 1 at 2) is a
profinite unit square, so no finite set of ET/divisor classes covers {n_s : s ≡ 0 (mod L)} for any L.

**Theorem B (an exponential class through a proved sterile point; PROVED, symbolic).** For every integer X ≡ 4 or 6 (mod 11)
put n := 48X⁴ + 1. Then
  4/n = 1/(3(4X⁴ + 1)) + 11/(6n(2X² − 2X + 1)(X² + X + 2)) + 11/(2n(4X⁴ + 1)(X² + X + 2)),
with all three denominators positive integers. Taking X = 2^{(s−4)/4}: ES holds for every n_s = 3·2^s + 1 with
**s ≡ 0 or 12 (mod 40)**, s ≥ 4. In particular the class s ≡ 0 (mod 40) — a neighbourhood of the ET/divisor-sterile point
μ = 0 — is covered by ONE exponential class.
*Proof.* Identity: sympy `simplify` = 0 (`scripts/z15_proth_identity.py`); by hand it is CAP_DOWN Lemma 1.1 at the window
m = 11 = 4·3·1⁴ − 1 with K = (n + 11)/4 = 3(4X⁴ + 1) = 3(2X² + 2X + 1)(2X² − 2X + 1) (Sophie Germain / Aurifeuille) and
d = 9(2X² − 2X + 1), A = (K + d)/11 = 6(2X² − 2X + 1)(X² + X + 2)/11. Integrality: X² + X + 2 ≡ 0 (mod 11) ⟺ X ≡ 4, 6 (mod 11)
(disc −7 ≡ 2²). 2^{(s−4)/4} ≡ 6 = 2⁹ (mod 11) ⟺ (s − 4)/4 ≡ 9 (mod 10) ⟺ s ≡ 0 (mod 40); ≡ 4 = 2² ⟺ s ≡ 12 (mod 40). ∎
*Why it is not a contradiction.* The class {s ≡ 0 (40)} is the n-congruence class n ≡ 4 (mod 2⁴⁰ − 1), n ≡ 1 (mod 16),
which contains odd squares; Schinzel/Thm 1.2 forbid identities *polynomial in n* there. The identity is polynomial in
X = ((n − 1)/48)^{1/4}. In Theorem A terms: φ(X) = 48X⁴ + 1, X* = 1/2 at odd ℓ, X* = 0 at 2; X* is the rational point
(1/2, 2) of w² = φ(X) at odd places glued with the rational point (0, 1) at 2, and the witness algebra pairs non-trivially
with that glued adelic point (the pairing reduces to the places above 2).
*T1 control.* 3·2^s + 1 is a square only for s = 0, 3, 4 (4, 25, 49); none lies in the class. Exact numeric re-check of the solution
for all s ≡ 0, 12 (mod 40), s ≤ 4000 (`z15_proth_identity.py`).

**Why the first searches missed it (PROVED obstruction for the naive window menu).** Prop 4.1. Let c + 1 = 4^i, n_s = c·2^s + 1,
and let a constant-window Lemma-1.1 class (window m ≡ 3 (4), atoms = factors in ℤ[U] of K(U) = (n + m)/4, U = 2^{(s−j)/e},
divisor d = λ·Πatoms^{k}) contain a neighbourhood of μ = 0. Then m ≡ 3 (mod 8) and v₂(d(ρ)) is odd, where ρ = 2^{−j/e}.
*Proof.* The class contains all s ≡ 0 (mod L) for some L; it requires e | s − j, so (taking e | L) e | j and ρ = 2^{−j/e} is
rational (R-O240 repair: made explicit; the same holds for SG with 4 | s − j − 2, ρ = 2^{−(j+2)/4}). Taking s ≡ 0 modulo
L·ord_m(2)·(odd part of the class modulus)^∞, U → ρ in every ℤ_q, q odd: hence U ≡ ρ (mod m), n ≡ c + 1 = 4^i (mod m),
K ≡ 4^{i−1}, d(U) ≡ d(ρ) (mod m). The odd primes of the rational d(ρ) all divide N₀ := 4^i + m: atom values f(ρ) ∈ ℤ[1/2] have
product (with multiplicity, times the content) K(ρ) = N₀/4; an odd prime q of λ (numerator or denominator) divides K(U) on the
whole class, so either q divides the content of K(U) (then q | K(ρ)) or q divides the class modulus and U → ρ q-adically, so again
q | K(ρ). For an odd prime q | N₀,
−m ≡ 4^i is a square mod q, so (q/m) = (−m/q) = 1 (Jacobi reciprocity, m ≡ 3 (4)). Hence (d(ρ)/m) = (2/m)^{v₂(d(ρ))},
while d ≡ −K forces (d/m) = (−1/m) = −1. ∎ So windows m ≡ 7 (mod 8) (all m = c·2^j w − 1 with j ≥ 3, the shapes searched by
`z15_proth_mu0.py`: 0 hits) are dead at μ = 0; j = 2 (m ≡ 3 (8)) needs an algebraic factorisation of 2^{s−2} + w with
s ≡ 0, which the cyclotomic shapes (e | j) cannot give but Sophie Germain 4X⁴ + t⁴ (s − 2 ≡ 2 (4)) does, with
v₂(f±(1/2)) = −1 odd. Theorem B is the first such window (t = 1).

**Theorem C (ES for every 3·2^s + 1; PROVED, computer-assisted; certificate + independent checker).** For every s ≥ 0,
4/(3·2^s + 1) is a sum of three unit fractions.
*Proof.* (a) Sophie-Germain window-11 rules (polynomial in X = 2^{(s−4)/4}, n = 48X⁴ + 1, K = 3f₊f₋, f± = 2X² ± 2X + 1,
d = 3^a f₊^b f₋^c, x = K, y = n(K + d)/11, z = nK(K + d)/(11d)) cover every s ≡ 0, 8, 12, 16, 20, 28, 32, 36 (mod 40)
[(a,b,c) = (0,2,1), (0,0,2), (0,2,1), (0,2,0), (0,1,2), (0,2,0), (0,1,2), (0,0,2) respectively]: each is a polynomial identity
(sympy), integer-valued on the relevant class X ≡ 2^{(r−4)/4} (mod 11) (forward differences), and positive (all factors
f±, K + d are positive for real X). (b) Six ET/divisor classes (moduli 5, 7, 15, 61; `data/z15_cert_proth3_et.json`, built by
`z15_cert_proth_make.py 3 360 3000 … 0,8,12,16,20,28,32,36` with the z8/ec_cover machinery) cover every other s mod 360 (s ≥ 10);
non-divisor classes contain no odd square. (c) `z15_cert_proth_check.py` re-verifies (a), (b), coverage of all s mod 360 and an
exact solution for every s ≤ 1500 (s = 0 by brute force). ∎
*Scope / honesty.* A thin family (O(log X) members ≤ X); it contains the primes 3·2^s + 1 for s = 1, 2, 5, 6, 8, 12, 18, 30, 36,
41, 66, 189, …, but nothing about ES for primes in general follows. Its significance for the campaign is structural:
**3·2^s + 1 is PROVED to have no finite covering by ET/divisor classes (EXPONENT_COVERING Cor 1.5), yet ES holds for all of it**
by adding ONE window (m = 11) with an algebraically forced budget (the Aurifeuillean factorisation 4X⁴ + 1 = f₊f₋).
So a genuinely sterile point (unlike O238's 105, R246 D2) dissolves under the exponential-window menu. Literature: not checked
whether ES for this Proth family is recorded anywhere (likely folklore-invisible; no claim of priority).

**4.1 Other proved-sterile families (EVIDENCE; `z15_hybrid_exp.py`, `z15_tree.py`, `z15_mu0_sg.py`, `z15_rules_at.py`).**
* 7·4^s + 9 ((J)68 Lemma 3.1, ET/divisor-uncoverable at μ = 0): ET/divisor classes at L₀ = 360 leave {0, 90, 180, 200, 290};
  the Sophie-Germain window m = 19 = 7·4 − 9 (K = 7(4X⁴ + 1)) covers the μ = 0 neighbourhood s ≡ 0 (mod 90). The residue
  class s ≡ 20 (mod 90) is NOT closed: at L* = 128520 the windows SG(19), CY₃/₇/₉(103), CY₅(215) and ET classes leave 2 of
  1785 lifts (s ≡ 8570, 104960 mod 128520). Lifting these two to L* = 1413720 (×11), the window CY₁₁(19) covers 2 of the 22 lifts and ET classes
  all but 2 — again one lift of each (s ≡ 1293770, 233480 mod 1413720): self-similar stuck nodes (the supercritical branching
  of (J)68 §2), and no window with j ≤ 40, t ≤ 11, e ≤ 21 fires at s = 233480. 7·4^s + 9 is NOT decided (EVIDENCE).
* 15·2^s + 1, 63·2^s + 1, 255·2^s + 1 (EXPONENT_COVERING Cor 1.5): **no** Sophie-Germain window m = 4ct⁴ − 1 fires at μ = 0 for
  t ≤ 301 (c = 15, 63), and the polynomial-window search (`z15_polywin_root.py 240 4 1 6 1/2`) finds nothing; for c = 3 only
  t = 1 fires among t ≤ 41. Reason (PROVED, Prop 4.3 below): at μ = 0 every SG window condition is the divisibility
  m(t) = 4ct⁴ − 1 | N(t) for an explicit polynomial N of degree ≤ 8 with small coefficients; since 4ct⁴ − 1 is irreducible
  (c not a square), Res(N, m) ≠ 0 and m(t) | Res(N, m): **only finitely many t can fire**. The SG menu at μ = 0 is a finite menu.
  For c = 3: (t, a, x, y) = (1, 0, 2, 1), (1, 2, 0, 1) are the only firings with "identically zero" excluded (z15_sg_mu0_complete).
  For c = 15, 63 the exhaustive resultant bound was not completed (bounds ~10⁸ in t): EVIDENCE only.

**Prop 4.3 (finiteness of the SG menu at μ = 0; PROVED).** Let c + 1 = 4^i, c not a square. At μ = 0 of c·2^s + 1 the cap-0
Sophie-Germain window with parameter t fires iff 4ct⁴ − 1 divides N_{a,x,y}(t) := Π q^{a_q}·g₊^x g₋^y + 4^{i−1}2^{x+y}
(g± = 2t² ± 2t + 1) for some admissible exponents. m(t) = 4ct⁴ − 1 is irreducible over ℚ (t⁴ − 1/(4c) factors only if
1/(4c) is a square or −4·(fourth power)). So either m | N in ℚ[t] (a polynomial family of windows, firing for every t) or
Res(N, m) ≠ 0, and m(t) | N(t) ⟹ m(t) | Res(N, m) (Bezout over ℤ, gcd(m(t), 4c) = 1), bounding t. For c = 3 the first case
cannot occur for any c (R-O240 repair): m has the positive real root τ = (4c)^{−1/4}, and N(τ) = Πq^{a_q}g₊(τ)^x g₋(τ)^y
+ 4^{i−1}2^{x+y} > 0 since g± > 0 on ℝ; so Res(N, m) ≠ 0 always. (`z15_sg_mu0_complete.py 3` confirms for all 27 vectors.) ∎ (Derivation: near μ = 0,
X ≡ 1/2, f± ≡ g±/2, K ≡ 4^{i−1} mod m; clear the unit 2^{x+y}.)

**4.2 Reading.** For the (J)22 / (J)68 unit-square points the obstruction to ET/divisor menus is that n* is a profinite unit
square; Theorem A shows that for a root parametrisation n = φ(X) the obstruction is instead the *descent class* of X* − θ.
At μ = 0, X* is the rational point ρ = 2^{−(j+2)/4} at odd places and 0 at 2, so (Theorem A) the only possible
obstruction sits at the places of A above 2: it is (α, θ(θ − ρ))₂, and θ(θ − ρ) is NOT a 2-adic square in A ⊗ ℚ₂ for
3θ³ + 1 = 0, 3θ⁵ + 1 = 0, 3θ⁷ + 1 = 0 (`z15_twoadic_mu0.py`), so Theorem A certifies no sterility there. Whether a window with
the right witness α exists is then a finite arithmetic accident (Prop 4.3): it happens for 3·2^s + 1 (m = 11) and
7·4^s + 9 (m = 19), not (yet) for c = 15, 63, 255.

## 3. Question (3): near-square sterile sets under algebraic reparametrisation

**Prop 3.1 (NEAR_SQUARE Thm 2.2 does not extend to algebraic functions of m; PROVED).** Let k = 105 (≡ 1 mod 8, so Z_105^□ ≠ ∅).
The O238 identity (Lemma 1.0) composed with u = v² is a Type II family *polynomial in v* for n = m² + 105 with m = 16v³,
valid on v² ≡ 32 (mod 151). The closure of its parameter set meets the pull-back of Z_105^□ = {m : m² + 105 ∈ (Ẑ^odd)²}.
*Proof.* The v-space is Ẑ = Π_ℓ ℤ_ℓ (product), so it suffices to find, for every odd ℓ, v_ℓ ∈ ℤ_ℓ (with v_ℓ² ≡ 32 at ℓ = 151)
such that 256v_ℓ⁶ + 105 is a non-zero square mod ℓ (then a unit square in ℤ_ℓ); at 2, m² + 105 ≡ 1 (mod 8) for even m. For
ℓ < 400 this is checked (`z15_k105_escape.py`: no exception, ℓ = 3, 5, 7, 151 included); for ℓ ≥ 37 the genus-2 curve
w² = 256v⁶ + 105 has ≥ ℓ + 1 − 4√ℓ − 2 − 6 > 0 affine points with w ≠ 0 (Weil). ∎
So the polynomial-in-m sterile set Z_k^□ (k > 0) is not sterile for the menu "polynomial in an algebraic function of m":
the family is polynomial in v = (m/16)^{1/3}, i.e. it lives on the curve m = 16v³, and Theorem A applied to
φ(v) = 256v⁶ + 105 replaces the norm condition "m² + 105 is a square" by the descent condition on v − θ in ℚ[v]/(φ).
(Unlike Theorem C this example does not cover a *proved* sterile point of an ET menu; it refutes the naive extension of
Thm 2.2 only. The analogue for Z_K⁺ (k < 0, Thm 3.4) was not constructed: spark.)

## 5. Question (2): the (J)54 sterile Mordell points (all primes in an r-generic cylinder)

**Prop 5.1 (thin menus cannot help at positive-density targets; PROVED, elementary).** Let C ⊂ Ẑ be a residue class of units.
Any finite union of (a) one-parameter families n = φ(u) with deg φ ≥ 2, (b) exponential families c·b^s + k, (c) more
generally any sets with O(X^{1−δ}) elements ≤ X, contains a set of primes of relative density 0 in C. Hence if a finite
ET/divisor menu provably misses a neighbourhood C of a point (as at the (J)54 sterile Mordell points, all r ≥ 2³²),
adding finitely many thin items (root/exponential/window classes of Theorems B, C, O238) still misses a positive density
of the primes in C (Dirichlet). ∎
So the mechanism of Theorems B/C — the parameter lives on a thin curve where the descent class of the parameter differs
from the square class of n — is *by construction* unavailable on a positive-density set of primes. The positive-density
parametrisations of primes are norm-form/binary-form representations p = N(x) (Fermat, Hecke): there element squares
x = y² give actual squares N(y)², which are Zariski-dense in every congruence class and sector, so the old T1 argument
survives on square-compatible classes: POINTWISE_BINARYFORM Thm 3.2/Cor 3.4 (PROVED for positive definite binary quadratic
forms under its modulus hypotheses; R-O240 repair: squares are not dense in *every* class, only in square classes; higher norm
forms: Assessment). Prop 5.1 excludes finitely many thin items only; it does not classify all positive-density
parametrisations. Assessment: the natural remaining parameters defined at every prime are divisors of polynomial expressions
in p — the moving-modulus lottery B2. **Answer to (2) (PROVED for thin menus, Assessment beyond): finitely many algebraic/
exponential window families cannot cover all primes near the (J)54 points.**

## 6. Question (4): function fields
Prop 5.1 holds verbatim in F_q[T] (deg φ ≥ 2 in u ∈ F_q[T] gives q^{n/2}-sized images in degree n), so CONJECTURE 0.2's
x*_c (a covering of *all* primes P near x*_c) cannot be dissolved by thin menus either. The F_q[T] analogue of Theorems B/C
would concern a thin family (e.g. P_s = c·T^{q^s} + A, whose residues mod any M are eventually periodic in s): there
Frobenius-power families give root parameters u = T^{q^{s'}}, but x^{q} + y^{q} = (x + y)^q, so the cyclotomic/Aurifeuillean
supply of moving divisors that powered Theorem C collapses in characteristic p (Assessment; spark: Carlitz-module
"cyclotomic" factors of T^{q^s} − T would be the natural replacement).

## 7. The menu ladder (summary table)
| menu (parameter complexity) | domain | sterile set contains | status |
|---|---|---|---|
| M₀: ET/divisor classes, polynomial in n | residue classes of n | profinite unit squares Sq^× (Schinzel; EXPONENT_COVERING 1.2/1.4) | PROVED |
| M₁[φ]: polynomial in u, n = φ(u) | classes of u (thin if deg φ ≥ 2) | Ster(φ): 2-descent classes u* − θ ∈ γ·□ (Theorem A, unit locus) + integer T1 points (Thm 3.3) | PROVED (⊇); equality on the unit locus open |
| M₁, deg φ = 2 (near squares) | m-classes | Z_K⁺ (NEAR_SQUARE 3.4), Z_k^□ (2.2) | PROVED |
| M₁ ∘ algebraic (m = 16v³) | v-classes | Z_k^□ NOT sterile (Prop 3.1) | PROVED |
| M_exp: windows m = c·2^j w − k with algebraic budget (cyclotomic, Sophie Germain) | s-classes of c·b^s + k | μ = 0 of 3·2^s + 1, 7·4^s + 9 NOT sterile (Thm B, §4.1); constant windows m ≡ 7 (8) blocked at μ = 0 (Prop 4.1); SG menu finite at μ = 0 (Prop 4.3) | PROVED + EVIDENCE |
| M₂: binary/norm forms p = N(x) (positive density) | primes | element-square classes (actual squares) | PROVED d = 2 ((J)3), Assessment d ≥ 3 |
| any thin menu on positive-density prime sets | primes near (J)54 points | everything ET misses (Prop 5.1) | PROVED |
| divisor parameters (u | N_θ(p)) | all p | = B2 lottery | — |

**4.3 T1 control explains the two dead residues (PROVED).** The SG window-11 menu fires at every s ≡ 0 (mod 4) except
s ≡ 4, 24 (mod 40), i.e. X ≡ 1, −1 (mod 11). These are exactly the neighbourhoods of the integer T1 points X = ±1 of
φ(X) = 48X⁴ + 1: φ(±1) = 49 = 7² (s = 4: 3·2⁴ + 1 = 49). φ has no real root, so by NEAR_SQUARE Thm 3.3 (= Theorem A with
not via Theorem A: φ(±1) = 49 is not a unit — R-O240 repair) no Type I/II polynomial-in-X family is valid on a class containing
X = ±1 (divisor families by 7 do exist there, e.g. (2n/7, 15n/7, 30n) on X ≡ 1 (mod 7)). Numerically 48X⁴ + 1 is a square
for no X ≡ 4, 6 (mod 11), X < 2·10⁶, and for no X < 10⁵ except X = 1. These residues are handled by ET classes in Theorem C
(they are not near a unit-square point of the s-family).
