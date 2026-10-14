# y3_lucas_dickson_trace — Lucas/Lehmer ranks, Dickson polynomials, trace and Cayley maps as bridges (O211 (b))

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
TORSION_FIRING Thm 3.1 kills homomorphic bridges T(F_h) → F_h^*. Classical non-homomorphic maps from the norm-1 torus
T = μ_{h+1} ⊂ F_{h²}^* to F_h: trace u ↦ u + u⁻¹ (Dickson/Chebyshev: D_n(u + u⁻¹) = uⁿ + u⁻ⁿ), Cayley transform
u ↦ i(u + 1)/(u − 1) (a bijection T ≅ P¹(F_h) minus nothing: "cotangents"), additive shift u ↦ 1 − u (cyclotomic
units), Lucas sequences (U_n = (αⁿ − βⁿ)/(α − β), α/β ∈ T when ((P² − 4Q)/h) = −1; rank of apparition | h + 1).
Which of these sees "a divisor of h + 1 in a residue class" AND p?

## Dictionary entries (PROVED, elementary)
* Lucas: for (D/h) = −1 the rank r(h) of U(P,Q) divides h + 1; Type II at h on slice (c,d) ⟺ h | p + 4c²d and
  some U(P,Q) with (D/h) = −1 has r(h) | ... with 4cd | h + 1 — the latter is automatic data of h (choose α/β a
  generator of T): Lucas ranks encode "4cd | h + 1" but not the residue condition. Primitive prime divisors of
  U_{4cd}(P,Q) with (D/h) = −1 are ≡ −1 (mod 4cd) (Carmichael/Bilu–Hanrot–Voutier) — Euclidean classes, see
  y3_euclid_schur_forcing; they divide U_{4cd}, not p + 4c²d (B2).
* Dickson/trace: μ_m ⊂ T ↦ roots of Ψ_m (min. poly. of 2cos 2π/m) in F_h; D_c'(2) = c² (Chebyshev T_c'(1) = c²), so
  4c²d ≡ 4d·D_c'(2): Type II ⟺ −p ≡ 4d·D_c'(2) (mod h).
* Cayley: μ_m ↦ {cot(πk/m)} ⊂ F_h; Σ_{k=1}^{c−1} csc²(πk/c) = (c² − 1)/3 holds in F_h, so 4c²d = 4d(1 + 3Σcsc²).

## The unifying statement: Galois-descent collapse (PROVED)
**Prop G.** Let m | h + 1, K = ℚ(ζ_m)⁺, and 𝔥 a prime of K above h. (i) h splits completely in K, so reduction gives
φ(m)/2 ring homomorphisms ρ_𝔥 : O_K → F_h, and every algebraic quantity built from μ_m ⊂ T(F_h) by field operations
that is invariant under ζ ↦ ζ^h = ζ⁻¹ is ρ_𝔥(α) for some α ∈ K (independent of h once the formula is fixed).
(ii) If the quantity is defined over ℚ (invariant under all of Gal(ℚ(ζ_m)/ℚ), e.g. any symmetric function of a
subgroup μ_c, a cardinality, a Gauss-sum modulus, a cyclotomic number), then α ∈ ℚ and its residue is that of a fixed
rational number r(m): **the bridge transports exactly the box** (Type II: −p ≡ r = 4c²d).
*Proof.* (i) Frob_𝔥 acts on ζ_m as ζ ↦ ζ^h = ζ⁻¹, i.e. complex conjugation, which is trivial on K; quantities
fixed by ζ ↦ ζ⁻¹ lie in O_K[1/m] and reduction is a ring map. (ii) Galois-invariant elements of ℚ(ζ_m) are rational. ∎
**Iteration (violate "defined over ℚ").** Non-rational α ∈ O_K give conditions "−p ≡ ρ_𝔥(α)", i.e. h | N_{K/ℚ}(p + α)
with h ≡ −1 (m): a *cyclotomic generalisation* of the Type II divisor form (α = 4c²d is the rational case). It does not
imply ES (a certificate needs α rational of the form 4c²d) — but it is the natural home of a "Frobenius = complex
conjugation" mechanism: such h are exactly the primes splitting completely in K but inert in ℚ(ζ_m)/K. The ES problem
is the rational section of this; the rational section is where the moving-modulus/archimedean condition lives.

## Barrier screen
B2 (every entry requires h | p + 4c²d for h attached to the solution); Prop G(ii) is Thm 3.1's companion: homomorphic
bridges see a sign, Galois-invariant algebraic bridges see a fixed rational (the box). T1: none of these maps sees the
square class beyond the Legendre symbol (pd/h) = −1 (y3_semiprimitive_collapse Prop 1.2(ii)).

## Cheap numerics
Covered by scripts/y3_gauss.py (check (4): ∏(1 − ζ) = c; 0 failures, h ≤ 83); Chebyshev/cosecant identities are
polynomial identities over ℤ[1/6] and hold in F_h for h > 3.

## Assessment
COLLAPSES to the box (PROVED, Prop G). Clean by-product: **two-sided classification of bridges between the (h+1)-
and (h−1)-worlds** — homomorphisms: ±1 (Thm 3.1); algebraic Galois-equivariant maps: O_K → F_h with K = ℚ(ζ_m)⁺,
whose ℚ-rational part is the box. Anything sharper must be non-algebraic in μ_m (archimedean: sizes) — the content
of B2/B3.
