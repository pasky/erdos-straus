# y2 — Signed friezes and Farey distance: T1 lives exactly in positivity (O210)

Labels as in DISCOVERIES.md. **ES is not solved.** Item (e): Farey-graph distances / SL₂-tilings.

## Idea
Drop positivity. Integral (tame, signed) pentagon friezes at N are signed words (c, m, s) ∈ (ℤ∖0)³ with K = N, i.e.
Farey paths ∞ → c → c − 1/m → N/h′ of length 3 with arbitrary turns. N/A is at Farey distance ≤ 3 from ∞ via the
side (0, ∞) (geodesic integer continued fractions: Beardon–Hockman–Short, Michigan Math. J. 61 (2012), from memory).
The vertex-fan identities still hold, with signs, so a quiddity 4w gives 4/N = ±1/x ± 1/y ± 1/z.

## Results
* **Signed friezes have no T1 (PROVED, R208: the signed word (4, −(M² + 3)/4, −1) has N = M² and quiddity 4 for every
  odd M ≥ 3; the box search below is a check).** `scripts/y2_signed.py 40`: among 159 836 signed words (letters
  in [−40, 40], N odd), every odd square 9, 25, 49, …, 625, … has a signed pentagon frieze with a quiddity ≡ 0 (mod 4).
  Signed Egyptian representations of 4/M² exist trivially, so this is expected.
* **Where the proof of the even-edge law uses positivity (PROVED by inspection of FRIEZE_ES Thm 1.2).** Positivity is
  used only in the reciprocity steps: (x/y)(y/x) = (−1)^{(x−1)(y−1)/4} needs x, y > 0, and (−1/·) and (2/·) are taken
  at positive odd moduli (h, s, m, h″). With a negative cluster variable, each reciprocity step picks up the
  Hilbert symbol (x, y)_∞, which is the archimedean factor. So **T1 = the archimedean local factor of Hilbert
  reciprocity, entering through the positivity of the frieze.** This matches (J)13 (T1 = Diff-parity/Hilbert
  reciprocity for the incoherent ternary collection) in frieze language.
* **Consequence for SVZ (y2_farey_complex_lifting).** SVZ lift mod-n friezes to *tame integral* friezes, with signs
  allowed. Their theory cannot see T1, because T1 needs positivity. This is a second explanation of the F₄-blindness.
* Positive-word law re-checked on the positive part of the box: 0 failures.

## Iteration
* *Try:* use signed friezes plus a "sign-fixing" move (flip the orientation of one Farey step). A single flip changes
  one archimedean Hilbert symbol and hence the Jacobi side, so it cannot be done while keeping both the word positive and
  the sign. Dead, for the same reason as the CHI_FLIP "no classical move flips the sign".
* *Try:* Farey distance ≤ 3 (all signs) as a weaker certificate. It does not give ES (signs in the Egyptian fraction).

## Literature
Beardon–Hockman–Short, *Geodesic continued fractions* (2012), from memory. SVZ arXiv:2312.12953 (verified).
Bessenrodt–Holm–Jørgensen, *All SL₂-tilings come from infinite triangulations* (Adv. Math. 2017; seen in search).

## Barrier screen
T1/B5: located precisely at the archimedean factor, i.e. positivity. Any mechanism that does not use positivity of
all five cluster variables (tame/SL₂-tiling theory, finite-ring friezes, mod-n Farey complexes) is T1-blind and so
cannot prove ES.

## Assessment
PROVED (by inspection) + EVIDENCE. Useful steering: **a frieze-theoretic ES proof must use the positivity of the
frieze in an essential, archimedean way.** Promise 0/5 as a route; 2/5 as a screen.
