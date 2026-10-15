# z15_near_square_algebraic — Z_k^□ is not sterile for families polynomial in v with m = 16v³ (O238 spark 5) (O240)

## Idea
NEAR_SQUARE Thm 2.2: polynomial-in-m families on n = m² + k (k > 0) avoid Z_k^□. O238's class n = 256u³ + 105 with u = v²
is n = m² + 105 with m = 16v³ and is polynomial in v. Its v-closure meets the pull-back of Z_105^□ (local points at every ℓ,
Weil for ℓ ≥ 37, direct check ℓ < 400).
## Literature
NEAR_SQUARE (J)55; SYNTHESIS_SPARKS6 Lemma 1.0.
## Barrier screen
Breaks the hypothesis "polynomial in m" of Thm 2.2 (not a proved sterile point of the ET menu of 4^s + 105: R246 D2).
Theorem A gives the replacement: descent condition on v − θ in ℚ[v]/(256v⁶ + 105).
## Cheap numerics
`scripts/z15_k105_escape.py 400`: no local exception.
## Assessment
PROVED (MENU_STERILITY Prop 3.1). Spark: the k < 0 analogue (escape Z_K⁺ of Thm 3.4 with m = algebraic function).
