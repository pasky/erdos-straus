# s5_cm_frobenius — Frob = c_∞ twisted by √p: certificates are primes splitting completely in a CM field (combination (iv))

## Idea
(J)50 shows that h ≡ −1 (mod M) ⟺ Frob_h = c_∞ in ℚ(ζ_M). (J)44 separates the (h+1)-world (divisors) from the
(h−1)-world (p). (J)33 makes certificates edges of the supersingular 2-isogeny graph. The brief asks for a Chebotarev
statement in a family of fields indexed by h. The natural family turns out to be indexed by the slot modulus M, with
the certificate condition a single Frobenius class.

## Prop C (PROVED, elementary)
Let p ≡ 1 (mod 4) be prime, M ≥ 3, K_M = ℚ(ζ_M, √p) (p ∤ M), and g = (c_∞ on ζ_M, −1 on √p) ∈ Gal(K_M/ℚ).
(a) F_M := K_M^{⟨g⟩} = ℚ(ζ_M)⁺(√(p(θ² − 4))), with θ = ζ_M + ζ_M⁻¹. It is a **CM field** with maximal real subfield
ℚ(ζ_M)⁺, because p(θ² − 4) = p(ζ − ζ⁻¹)² is totally negative.
(b) A prime h ∤ pM satisfies h ≡ −1 (mod M) and (h/p) = −1 ⟺ Frob_h = g ⟺ h splits completely in F_M but not in
ℚ(ζ_M)⁺(√p).
(c) Hence, with M = 4cd: a prime-modulus Type II certificate of p ((J)44/(J)50, PM-II) is a prime h | p + 4c²d that
splits completely in the CM field F_{4cd} and is inert in ℚ(√p). The inertness is automatic for a certificate
(R227 repair D12: because h | p + 4c²d and h ≡ −1 (mod 4d) give (p/h) = (−d/h) = −1, BRIDGE_WORLDS Thm (i); so the √p
twist adds nothing to (J)50, and (c) is only "⟹" — "⟸" needs h | p + 4c²d).
(d) M = 4 gives F₄ = ℚ(√−p). This recovers the genus statement at level 4: h ≡ 3 (mod 4) with (h/p) = −1 ⟺ h splits in
ℚ(√−p), h ≡ 3 (4), i.e. h lies in the non-principal genus of discriminant −4p.

*Proof.* √p·(ζ − ζ⁻¹) is fixed by g, and its square is p(θ² − 4), which is negative at every real embedding of ℚ(ζ)⁺
since |θ| < 2. The index is [K_M : F_M] = 2. (b) is the definition of Frobenius plus quadratic reciprocity ((h/p) =
(p/h) is the action on √p). ∎

## The "Chebotarev in a family" reading and why it stops
* Density of primes with Frob = g is 1/(2φ(M)) (Chebotarev, all M uniformly in the abelian case).
* A certificate needs such a prime to *divide the specific number p + 4c²d* (with p + 4c²d ≡ p (mod 4cd)). That is B2:
  the Frobenius class is fixed, but the prime must come from a moving finite set.
* Averaged over p, this gives the ET-type main term (B6).
* At fixed p, the family {F_{4cd}} is a tower of CM fields with growing conductor. A "Chebotarev with a divisibility
  constraint" at one integer is exactly the divisor lottery.
* The supersingular reading ((J)33/(J)35): h splitting completely in a CM field whose real part is ℚ(ζ_M)⁺ is an
  embedding condition for CM orders into B_{p,∞}. It is the same statement in the quaternion language, with no new
  input.
* Torsion ((J)44 Thm 3.1): every homomorphism from the (h+1)-world into F_h^* lands in ±1. In F_M this is the statement
  that g has order 2, so the only "transport" between the CM side and p is the single bit (h/p). This matches Prop C(c).

## Literature
Class field theory of cyclotomic and quadratic fields. The fixed field of complex conjugation twisted by a quadratic
character is a standard CM construction (e.g. Washington, *Cyclotomic Fields*, §4). (J)50 has the untwisted case.

## Barrier screen
* B2: fixed class, moving integer.
* B6: Chebotarev averages.
* T1: at p = m², √p ∈ ℚ, so g is not an element of Gal(K_M/ℚ) = Gal(ℚ(ζ_M)/ℚ). The "twisted conjugation" does not
  exist, and Prop C(c) is vacuous: there are no certificates. **T1 = the twist collapses**, a clean restatement.
* B5 respected.

## Cheap numerics
`scripts/s5_cm_check.py` checks the following.
* (b) for M ∈ {4, 8, 12}, where F₄ = ℚ(√−p), F₈ = ℚ(√2, √−2p) and F₁₂ = ℚ(√3, √−p), so complete splitting is a pair of
  Legendre conditions. Primes p ≡ 1 (mod 4) < 3000 and h < 5000 give 422 000 checks with 0 mismatches.
* (c) on 1 723 prime-modulus Type II certificates (c, d < 60, h < 4000): 0 with (h/p) ≠ −1.

## Assessment
PROVED dictionary (Prop C). The T1 reading "the twisted conjugation g ceases to exist at squares" is clean, but it is
a reformulation of (h/m²) = 1. No existence mechanism: B2.
