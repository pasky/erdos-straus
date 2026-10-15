# z1_small_prime_pigeonhole — which numerators have a forced slice? 2, 3 unconditionally, 4 on the χ-fibre, nothing else (O224)

## Idea
z1_fano_pigeonhole forces a 4-slice on every χ = −1 word by a pigeonhole in ℙ(L/2L). Ask the same at odd primes ℓ:
the pentagon gives five points of ℙ(L/ℓL), and "ℓ | entry" means the point lies on the conic Q ≡ 0 (mod ℓ) (for f, f*
the norm is nA, nA*; take ℓ ∤ n). Is there a forced meeting, and does it explain 7 (brief item (iv))?

## Literature
FOUR_SPECIFIC Prop 3.2 ({±1}-unit slices exist exactly for M ∈ {3, 4, 5, 7}), SEVEN_SIBLING Thm 3.1 (7/p for p ≢ 1 mod 105 by
identities), z1_marking_isometry Prop 3.

## Results
* ℓ = 2 (M = 2): exactly two pentagon entries are even (frieze parity), so S_2 = X_n. PROVED.
* ℓ = 3 (M = 3), 3 ∤ n: S_3 = X_n. PROVED (if 3 ∤ t, u, v, A, A*, then tu ≡ tv ≡ 2 (mod 3), so u ≡ v and n ≡ 0).
  In conic language: the 5 pentagon points always meet the 4-point conic in ℙ²(𝔽₃). Over 𝔽₃ every ternary is isotropic
  (Chevalley), so the forced meeting is unconditional. Over ℤ₂, isotropy mod 4 is a genuine condition, the Hasse sign,
  and that is why the M = 4 meeting is conditional on χ = −1.
* M = 4: forced exactly on the χ = −1 fibre (FOUR_ADIC_INPUT Thm 1.3).
* ℓ ≥ 5: the conic has ℓ + 1 points of ℓ² + ℓ + 1, and no forcing: (1, 2, 5) ∈ X_3 has pentagon (1, 2, 5, 1, 4), which avoids
  5 and 7. The S_ℓ slices split both χ-halves (MODEL_SPECIFIC Thm 3.1(c)).
* M = 8, 16, …: one further fair bit per level (z1_depth_bits). M = 6: S_6 needs a common entry divisible by 2 and 3, and
  it is not forced (S₆(p) = ∅ at 25 primes ≤ 10⁵, MODEL_SPECIFIC).
So **the only numerators whose five slices are forced by finite-field/2-adic pigeonhole are 2, 3 (trivially, all words)
and 4 (on the χ-fibre).** Among these, only 4 has a non-trivial target that is T1-sensitive. 3/n and 2/n have trivial
targets, consistent with their elementary solvability.

## Barrier screen; (iv)
Item (iv), explaining 7, is **not** achieved by this mechanism. S₇(p) = ∅ at 10 primes ≤ 10⁵ (FOUR_SPECIFIC), and 7's record is
identities (p ≢ 1 mod 105) plus the lottery ((J)49). This is consistent with (J)49's verdict that no property shared by 4
and 7 separates them from 8 and 11. B1–B6: steering only.

## Cheap numerics
`scripts/z1_marking2.py 300` (S_2, S_3 = all words for gcd(n, M) = 1; no other M ≤ 30); `scripts/z1_fano.py`.

## Assessment
PROVED classification of forced pentagon slices (elementary). This places 4 between the trivial 2, 3 (forced
unconditionally) and the non-forced ℓ ≥ 5 and 2^{k ≥ 3}. The forcing at 4 is conditional exactly on the Hasse sign. Does not
explain 7. Promise 1/5.
