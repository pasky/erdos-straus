# z15_witness_descent — sterility of one-parameter menus is a 2-descent condition (O240)

## Idea
Every Type I/II polynomial family on n = φ(u) carries a witness D(u) with (D/φ(u)) = −1 (NEAR_SQUARE Lemmas 1.1/1.3). With
A = ℚ[u]/(φ), α = D(θ), Hilbert reciprocity in A turns (D(u)/φ(u)) into Π_{v∈S∪∞}(α, u − θ)_v — the evaluation of the
quaternion (Brauer) class cor(α, u − θ) on the double cover C_φ: w² = φ(u). (The Brauer/2-descent reading is interpretation — Assessment; R252 D6.) Sterile points of the menu M₁[φ] therefore
contain the adelic points whose descent class u* − θ is globally a totally positive γ⁻¹ times local squares
(MENU_STERILITY Theorem A, PROVED). Special cases: Schinzel (deg 1), Thm 3.4 (deg 2, γ = 1); integer T1 points with φ(u₀) > 1 are not unit points and
stay with NEAR_SQUARE Thm 3.3 (R-O240 repair).
## Literature
Two-cover descent / fake 2-Selmer sets: N. Bruin, M. Stoll, Math. Comp. 78 (2009) 2347–2370; descent and Brauer–Manin:
A. Skorobogatov, *Torsors and rational points* (CUP 2001). Mordell/Schinzel on polynomial ES identities via ET (2013) p. 7–8.
## Barrier screen
B1 is *explained*, not broken: the theorem says which points each one-parameter menu cannot reach. T1: only integer points with φ(u₀) = 1 are built in
(γ = 1/(u₀ − θ)); odd squares φ(u₀) > 1 stay with NEAR_SQUARE Thm 3.3 (R251 D5, applied by R252). B5/B6 irrelevant (family statements). Thm 9.1/Prop 10.3: the witness is a ray-class (not genus)
object in A; nothing about single primes.
## Cheap numerics
`scripts/z15_twoadic_mu0.py 3 7`: at μ = 0 of 3·2^s + 1 the class θ(θ − ρ) is not a 2-adic square for e = 3, 5, 7, so
Theorem A does not certify sterility there. The algebra relevant to Theorem C is the Sophie-Germain one, φ = 48X⁴ + 1
(η = 2θ, 3η⁴ + 1 = 0): η(η − 1) is not a square in ℚ₂(η) (PARI, `scripts/review_r251_thmA_2adic.py`; R251 D7, applied by R252),
as Theorem A + Theorem B require — and indeed Theorem C (memo z15_proth_sophie_germain) covers it.
## Assessment
PROVED (⊇, unit locus). Whether Ster(φ) is the full sterile set on the φ-unit locus of M₁[φ] (the analogue of CONJECTURE Y10-S) is open; for genus ≥ 2
(deg φ ≥ 5) Bruin–Stoll fake Selmer sets are often empty, which would predict *no* T1-type obstruction for such menus.
