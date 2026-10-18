# z37 — Question R, ZQ and ES-five are one problem: "a structured numerator set is not inside the residues" (O267)

## Idea
Reduce Question R (thin Γ ⊆ Ψ, δ near 1) to a statement of ES shape.

## Literature
RS Prop 2.2, Lemma 3.4, Lemma 4.1; ZAREMBA_TRANSFER §4 (ZQ_M); DEDEKIND Cor 4.6 (λ(p) ≤ 3).

## Content (QUESTION_R Prop 2.1, 2.2; PROVED)
For Γ̃ ⊆ Γ₁(4)_{≥0}, Γ⁺ = Γ̃ ∩ Ψ (not in general RS's finitely generated Γ'_n), seed (x, y) with y odd, (x/y) = −1: R⁺(n) = (R(n) + R_σ(n))/2, R_σ(n) = −Σ_{a ∈ G(n)} (a/n); n is a
Γ⁺-denominator ⟺ some Γ̃-numerator over n is a Jacobi non-residue. Ladder by |G(n)|: RS fat (≍ n, PROVED via PV) >
Thm A (> p/2, pigeonhole) > Question R (n^{2δ−1}) > ZQ_M (n^{2w_M−1}) > ES-five (log² n). If squares are congruence-admissible (RS Def 2.4), Euler-product main terms are positive there, so a correct main term
needs a factor vanishing at squares (natural candidate 1 − ∏_p 1[n ∈ ℚ_p^{×2}]); where the twisted term sits in a
circle method is an unproved Assessment. CONJECTURE R-main: R⁺(n) ≈ (1/2)c𝔖(n)n^{2δ−1}(1 − 1_□-class(n)).

## Barrier screen
B2/B3/B5: Question R has the same structure as ES at power scale; reciprocity is invisible to expansion and major arcs.
B6: pointwise vs density-one — a density-one version would be consistent with the obstruction (squares have density
zero); whether BK-type theorems give it for Γ⁺ is not checked (Γ⁺ need not be finitely generated).

## Cheap numerics
None needed (structural); RS's own data (Conj 2.15, 2.22) is the evidence.

## Assessment
PROVED reduction (for Γ⁺; for finitely generated Γ ⊆ Ψ an extra alphabet constraint remains) + CONJECTURE R-main. The useful output is the precise location: Question R is a QNR-in-Cantor-set
problem, i.e. the χ-twisted Zaremba problem with a Ψ-alphabet.
