# z37 — Question R, ZQ and ES-five are one problem: "a structured numerator set is not inside the residues" (O267)

## Idea
Reduce Question R (thin Γ ⊆ Ψ, δ near 1) to a statement of ES shape.

## Literature
RS Prop 2.2, Lemma 3.4, Lemma 4.1; ZAREMBA_TRANSFER §4 (ZQ_M); DEDEKIND Cor 4.6 (λ(p) ≤ 3).

## Content (QUESTION_R Prop 2.1, 2.2; PROVED)
For Γ̃ ⊆ Γ₁(4)_{≥0}, Γ⁺ = Γ̃ ∩ Ψ, seed with (x/y) = −1: R⁺(n) = (R(n) + R_σ(n))/2, R_σ(n) = −Σ_{a ∈ G(n)} (a/n); n is a
Γ⁺-denominator ⟺ some Γ̃-numerator over n is a Jacobi non-residue. Ladder by |G(n)|: RS fat (≍ n, PROVED via PV) >
Thm A (> p/2, pigeonhole) > Question R (n^{2δ−1}) > ZQ_M (n^{2w_M−1}) > ES-five (log² n). Euler-product main terms are
positive at admissible squares, so the true main term carries 1 − ∏_p 1[n ∈ ℚ_p^{×2}]; the twisted term lives at
denominators q | n (far minor arcs). CONJECTURE R-main: R⁺(n) ≈ (1/2)c𝔖(n)n^{2δ−1}(1 − 1_□-class(n)).

## Barrier screen
B2/B3/B5: Question R has the same structure as ES at power scale; reciprocity is invisible to expansion and major arcs.
B6: pointwise vs density-one — density one for Γ⁺ follows from BK-type theorems if they apply to Γ̃ (squares have
density zero), so the content of Question R is purely pointwise.

## Cheap numerics
None needed (structural); RS's own data (Conj 2.15, 2.22) is the evidence.

## Assessment
PROVED reduction + CONJECTURE R-main. The useful output is the precise location: Question R is a QNR-in-Cantor-set
problem, i.e. the χ-twisted Zaremba problem with a Ψ-alphabet.
