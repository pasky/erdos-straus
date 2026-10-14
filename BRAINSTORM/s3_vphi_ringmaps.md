# s3_vphi_ringmaps — (J)21 V_φ unit orbits × (J)25 finite box × (J)17 degree-2 accident: transports out of ℤ[φ]

**Combines:** (J)21 (V_φ: 4/n = 1/x + 1/y + 1/z over ℤ[φ], solvable at every prime under GRH via shots
a_k = n + 4φ^{2k+1}), (J)25 (ES over ℤ is a finite search), (J)17 (corestriction: every class over every number field
corestricts to Br ℚ ⊕ ⟨α⟩).

## Idea
(E1) "transport V_φ certificates back to ℤ" by an algebraic operation: a ring map, Galois averaging, norm or trace.

## Results (PROVED, elementary)
1. There is no ring homomorphism ℤ[φ] → ℤ (x² = x + 1 has no integer root); ring maps to ℤ/m exist iff x² − x − 1 has a
   root mod m. So ring-map transports output solutions of 4/n ≡ 1/x + 1/y + 1/z in ℤ/m only — local data, which ES
   already has everywhere (genus layer).
2. Galois conjugation maps V_φ solutions to solutions with the σ-sign conditions swapped; the averaged identity is
   8/n = Σ_i Tr(x_i)/N(x_i), three fractions with numerators Tr(x_i) — a unit-fraction representation only if
   Tr(x_i) | N(x_i) for all i, i.e. a divisor condition (B2) on norms of the orbit elements.
3. Norms do not preserve the additive equation. Every unit-orbit shot a_k = n + 4φ^{2k+1} (k ∈ ℤ) is irrational, so the
   orbit never meets ℤ: the unit orbit itself contains no ℤ-shot (ℤ's unit group is ±1, (J)23 M1).

## Literature
T1_TEMPLATE (O183); LDP_DEEP bsD_brauer_cores (corestriction).

## Barrier screen
Items 1–3 constrain only the operations examined. (J)17's corestriction theorem concerns Brauer classes evaluated on
local points; reading it as a statement about arbitrary Galois-equivariant transports of solutions would be an
extrapolation (Assessment only; R-O208 #7). B2 for item 2.

## Cheap numerics
None needed (statements are identities); the script-free check: x² − x − 1 has no root mod 2 (1, −1 both ≠ 0), so even
the reduction to ℤ/2 — where the numerator 4 and the wild partner live — does not exist.

## Assessment
PROVED negative for ring maps, Galois averaging and norms (not for all conceivable algebraic transports); ℤ[φ] is "not reducible to ℤ" at the prime 2, which is exactly where the
anchor/partner structure of (J)19 sits. Promise 0.
