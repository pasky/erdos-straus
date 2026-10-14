# y5_mod16_shadow — is there a second-order T1 shadow mod 16/32? (O213, brief item (c), O210 spark 4)

## Idea
At odd squares every word has o ≡ 3 (8), i.e. ee′ ≡ 4 (8) (T1). Is there more? Does the joint law of
(edge position, o mod 16 or 32, e/2 mod 8, e′/2 mod 8) have cells that are empty at squares but populated at
non-squares in the same class of N mod 32? Such cells would be a second-order obstruction, i.e. a refinement of T1.

## Literature
FRIEZE_ES §1–2; CHI_FLIP Thm 1.1 (the sign is one 2-adic Hasse invariant); memo y5_general_r_jacobi Thm 1.

## Barrier screen / theory
Heuristic expectation (Assessment): **no**.
* Every N ≡ 1 (8) is a 2-adic square. So squares and non-squares in a class mod 2^k are indistinguishable at 2.
* By y5_general_r_jacobi Thm 1 the only global constraint linking the 2-adic data of a word to N is the product
  formula, which pins one bit (s₂ = ∏_{ℓ|N}(…)).
* At squares all odd-prime factors are trivial, so s₂ = 1. Any further 2-adic datum is not constrained by any
  reciprocity law. A finer obstruction would need another global invariant of the path form, e.g. the spinor genus.
  For a positive ternary of odd determinant, the spinor genus adds no 2-adic constraint beyond the Hasse invariant
  (Assessment, not proved here).

## Cheap numerics (`scripts/y5_mod16.py 100000`, log `logs/y5_mod16.txt`; EVIDENCE)
All formal words with odd N ≤ 10⁵, N ≡ 1 (8): about 8 000 square words and 475 000 non-square words of sign +1, split
by N mod 32.
* At (position, o mod 16) and (position, o mod 32) resolution: **no cell is empty at squares and populated at
  non-squares**, in any class of N mod 32.
* At full resolution (80 cells per class), 5 of 320 cells are empty at squares. Each has expected square count ≈ 2
  (Poisson P(0) ≈ 0.1–0.15), consistent with sampling. At X = 3·10⁴ there were 17 such cells, so the count shrinks
  with X.
* The frequencies of the (position, o mod 16) cells at squares and at non-squares agree to within about 0.04.

## Assessment
EVIDENCE (negative): no second-order T1 shadow mod 32 in the frieze data. T1 is exactly one bit (the Hasse
invariant at 2). This closes O210 spark 4 negatively, at the level of evidence, with a heuristic explanation.
