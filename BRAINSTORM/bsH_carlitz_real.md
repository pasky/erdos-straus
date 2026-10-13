# bsH_carlitz_real — the A.4 loophole over F_q(T): Carlitz real subfields have odd degree, −1 sits in an inertia group of order q − 1 (O181)

**ES is not solved here.** DRINFELD_ES.md §4 remark. Script `scripts/bsH_descent.py` (part 3).

## Idea
Over F_q(T) the role of ℚ(ζ_M) is played by the Carlitz field K_M (Gal = (R/M)^*); inertia at ∞ is F_q^* (Hayes),
so the "complex conjugation" −1 is the order-2 element of a cyclic inertia group of order q − 1. The real subfield
K_M⁺ has degree Φ(M)/(q − 1), often odd — the A.4.2 obstruction (r even) disappears.
## Literature
Hayes 1974 (Carlitz cyclotomic fields), Rosen Ch. 12 (K_M, K_M⁺, inertia at ∞ = F_q^*).
## Analysis (PROVED, elementary)
[K_M⁺ : F] = (q^d − 1)/(q − 1) ≡ d (mod 2) for M irreducible of degree d; = q^{e−1} (odd) for M = T^e. Over
K_M⁺ the condition f ≡ −1 is Art_{K_M/K_M⁺}(𝔞) = −1 ∈ F_q^*, whose quadratic shadow is trivial when q ≡ 1 (4)
(−1 a square) — consistent with no T1 for q ≡ 1 (4). Norm descent: Prop 4.2 of DRINFELD_ES applies verbatim
(certificates for P·R_r).
## Barrier screen
Same death as bsH_odd_descent; the parity obstruction is gone but the certificate does not descend.
## Cheap numerics
Parity table for q ∈ {3,…,13}, d, e ≤ 8 confirms the formulas.
## Assessment
Dictionary only; closed. Promise 0–1.
