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
D̃ and φ gives h(u) | gcd(D̃(u), φ(u)) with |h(u)| > 1 for large u, so (D/n) = 0 ≠ −1; hence α ∈ A^×. Let u* ∈ Ster(φ) ∩
closure(C) with its γ, and let S be a finite set of primes containing 2, the primes of g, lc(φ), disc(φ), the index of
ℤ[θ] in the maximal order, and all primes below places where α or γ is not a unit. Pick u ∈ C, u larger than every real
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
* An integer u₀ larger than every real root with φ(u₀) an odd square: γ := (u₀ − θ)⁻¹ is totally positive, so u₀ ∈ Ster(φ)
  whenever φ(u₀) ≡ 1 (8) — NEAR_SQUARE Thm 3.3 (the "largest real root" of Lemma 3.2 is exactly total positivity of γ).
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
*T1 control.* 3·2^s + 1 is a square only for s = 0, 3 (25); neither lies in the class. Exact numeric re-check of the solution
for all s ≡ 0, 12 (mod 40), s ≤ 4000 (`z15_proth_identity.py`).

**Why the first searches missed it (PROVED obstruction for the naive window menu).** Prop 4.1. Let c + 1 = 4^i, n_s = c·2^s + 1,
and let a constant-window Lemma-1.1 class (window m ≡ 3 (4), atoms = factors in ℤ[U] of K(U) = (n + m)/4, U = 2^{(s−j)/e},
divisor d = λ·Πatoms^{k}) contain a neighbourhood of μ = 0. Then m ≡ 3 (mod 8) and v₂(d(ρ)) is odd, where ρ = 2^{−j/e}.
*Proof.* Near μ = 0, U ≡ ρ (mod m) and n ≡ c + 1 = 4^i (mod m), so K ≡ 4^{i−1}, and d(U) ≡ d(ρ) (mod m), a rational number
whose odd primes all divide N₀ := 4^i + m (they divide K(U) on the class, hence K(ρ) = N₀/4). For an odd prime q | N₀,
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
  1785 lifts (s ≡ 8570, 104960 mod 128520); single firing windows there have periods 99, 1329, 7158 (not pursued further).
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
never occurs (`z15_sg_mu0_complete.py 3`, all 81 exponent vectors). ∎ (Derivation: near μ = 0,
X ≡ 1/2, f± ≡ g±/2, K ≡ 4^{i−1} mod m; clear the unit 2^{x+y}.)

**4.2 Reading.** For the (J)22 / (J)68 unit-square points the obstruction to ET/divisor menus is that n* is a profinite unit
square; Theorem A shows that for a root parametrisation n = φ(X) the obstruction is instead the *descent class* of X* − θ.
At μ = 0, X* is the rational point ρ = 2^{−(j+2)/4} at odd places and 0 at 2, so (Theorem A) the only possible
obstruction sits at the places of A above 2: it is (α, θ(θ − ρ))₂, and θ(θ − ρ) is NOT a 2-adic square in A ⊗ ℚ₂ for
3θ³ + 1 = 0, 3θ⁵ + 1 = 0, 3θ⁷ + 1 = 0 (`z15_twoadic_mu0.py`), so Theorem A certifies no sterility there. Whether a window with
the right witness α exists is then a finite arithmetic accident (Prop 4.3): it happens for 3·2^s + 1 (m = 11) and
7·4^s + 9 (m = 19), not (yet) for c = 15, 63, 255.
