# z37 — The missing input for Question R: a χ-twisted gluing count (Hypothesis TG); window 3/8 vs 1/18 (O267)

## Idea
State exactly what Shkredov/Zhang would need to prove Question R, and measure how far known tools are.

## Literature
Shkredov arXiv:2603.14116 Cor 16, (151); Zhang arXiv:2605.02518 Thm 3.6 (both unrefereed); Weil/Salié bounds for
incomplete mixed sums; Burgess; ZAREMBA_TRANSFER §4 (window conflict 1/8 vs 1/18), R276.

## Content (QUESTION_R §2 items 1–4; Assessment)
For a glued residue c with full word P·M·S, P, S ∈ Ψ: σ(M) = −(c/n). So "middle inside Γ⁺" ⟺ a sign condition on c (for finitely generated Γ an alphabet constraint remains), and
the main term vanishing at squares needs TG: Σ_{c ∈ A∩B^{−1}} (c/n) = o(|A||B|/n) for non-square n, A, B = Λ ∔ [N].
Expansion holds at n = m² too, so it cannot give TG. Below N = n^{1/2} a box I × J has on average < 1 solution of ab ≡ 1 —
the χ-values typically sit on isolated points and Burgess is not directly applicable; above it, boxwise Weil/Salié
needs N ≥ n^{3/4}, ε ≥ 3/8, versus the middle-window constraint ε < 1/18 (a threshold of this method, not a universal
barrier). (Corrects ZAREMBA §4's 1/8, which presumed the
character could be summed along gluing intervals.)

## Barrier screen
T1: TG is false at squares by design — the minimal square-sensitive input. B3: even with TG, the conclusion is at
numerator-set size n^{1−O(κ)}, nowhere near ES.

## Cheap numerics
None (the conjecture is about all sets of the given shape).

## Assessment
Precise open hypothesis (TG) + Assessment of the window. CONDITIONAL "TG + preprints transported to Γ̃ ⇒ Question R"
is a proof sketch only (transport of Shkredov's middle-window step to Ψ-alphabets not checked).
