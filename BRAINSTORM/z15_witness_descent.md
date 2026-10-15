# z15_witness_descent — sterility of one-parameter menus is a 2-descent condition (O240)

## Idea
Every Type I/II polynomial family on n = φ(u) carries a witness D(u) with (D/φ(u)) = −1 (NEAR_SQUARE Lemmas 1.1/1.3). With
A = ℚ[u]/(φ), α = D(θ), Hilbert reciprocity in A turns (D(u)/φ(u)) into Π_{v∈S∪∞}(α, u − θ)_v — the evaluation of the
quaternion (Brauer) class cor(α, u − θ) on the double cover C_φ: w² = φ(u). Sterile points of the menu M₁[φ] therefore
contain the adelic points whose descent class u* − θ is globally a totally positive γ⁻¹ times local squares
(MENU_STERILITY Theorem A, PROVED). Special cases: Schinzel (deg 1), NEAR_SQUARE Thm 3.3 (integer T1 points: γ = (u₀ − θ)⁻¹,
"largest real root" = total positivity), Thm 3.4 (deg 2, γ = 1).
## Literature
Two-cover descent / fake 2-Selmer sets: N. Bruin, M. Stoll, Math. Comp. 78 (2009) 2347–2370; descent and Brauer–Manin:
A. Skorobogatov, *Torsors and rational points* (CUP 2001). Mordell/Schinzel on polynomial ES identities via ET (2013) p. 7–8.
## Barrier screen
B1 is *explained*, not broken: the theorem says which points each one-parameter menu cannot reach. T1: built in (squares
are γ = 1/(u₀ − θ)). B5/B6 irrelevant (family statements). Thm 9.1/Prop 10.3: the witness is a ray-class (not genus)
object in A; nothing about single primes.
## Cheap numerics
`scripts/z15_twoadic_mu0.py 3 7`: at μ = 0 of 3·2^s + 1 the class θ(θ − ρ) is not a 2-adic square for e = 3, 5, 7, so
Theorem A does not certify sterility there — and indeed Theorem C (memo z15_proth_sophie_germain) covers it.
## Assessment
PROVED (⊇). Whether Ster(φ) is the full sterile set of M₁[φ] (the analogue of CONJECTURE Y10-S) is open; for genus ≥ 2
(deg φ ≥ 5) Bruin–Stoll fake Selmer sets are often empty, which would predict *no* T1-type obstruction for such menus.
