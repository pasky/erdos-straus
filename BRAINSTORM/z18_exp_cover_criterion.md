# z18_exp_cover_criterion — the exponential Theorem 1.4, and why "iff descent" is false per rung (O245)

## Idea
O238 spark 2 / O240 spark 6: covering of c₀b^s + k by ET + root-window classes exists iff Λ avoids ∩_D (descent sets)?
## Result (MENU_LADDER §6)
Lemma 6.1 + Theorem 6.2 (PROVED, compactness): covering exists iff every μ ∈ Λ is in a divisor class or in the clopen
validity set V_F of a positive root class; V_F is read off at the profinite point Y*(μ). Prop 6.3 (PROVED, Theorem A):
V_F avoids the descent set S_D. The converse is FALSE per rung (D = 2: Theorem 4.1) and for the z14 window menu (O239
Cor 2.8 at μ = 0 of 15·4^s + 1, where S_2 = S_4 = ∅ by Computation 1.2). Correct per-rung sterile set: S_D ∪ (positivity part)
∪ (magnitude part for finite menus).
## Literature
EXPONENT_COVERING Thm 1.4; MENU_STERILITY Theorem A, Prop 4.3.
## Barrier screen
Structural statement; B1 explained, not broken.
## Cheap numerics
z18_descent2 (S_D empty at μ = 0 for D ≥ 2); z18_crt D = 2 (0 hits).
## Assessment
PROVED (criterion and counterexamples to the naive converse). Global converse open = CONJECTURE 6.4's negation.
