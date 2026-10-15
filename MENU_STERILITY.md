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
