import ES.Basic

/-! Axiom audit (expected: only `propext`, `Classical.choice`, `Quot.sound`). -/
#print axioms ES.ESProp_iff_rat
#print axioms ES.cofactor_dvd
#print axioms ES.cform_ES
#print axioms ES.cform_ES_rat
#print axioms ES.jacobi_C_of_dvd_succ
#print axioms ES.jacobi_n_of_cform
#print axioms ES.no_cform_square
#print axioms ES.no_shifted_square
#print axioms ES.jacobi_a_of_cform
#print axioms ES.cform_iff_shifted
#print axioms ES.no_typeII_square
#print axioms ES.no_typeI_square
#print axioms ES.ES_of_primes_one_mod_four
#print axioms ES.ES_of_cform_primes

/-! Sanity examples. -/
-- C-form example: n = 13, C = 1: 4·13+1 = 53 is prime ≡ 1 (mod 4) → no; C = 2: 105 = 7·15, 7 ≡ 15 ≡ −1 (mod 8).
example : ES.CForm 13 2 7 := by unfold ES.CForm; decide
example : ES.ESProp 13 := ES.cform_ES (show ES.CForm 13 2 7 by unfold ES.CForm; decide)
-- The coprimality hypothesis of `no_typeI_square` cannot be dropped: m = 2, c = d = 1, f = 4.
example : 4 ∣ (2 ^ 2) ^ 2 + 4 * 1 ^ 2 * 1 ∧ 4 * 1 * 1 ∣ 4 + 2 ^ 2 := by decide
-- … not even at odd squares: m = 3, c = 1, d = 3, f = 3 (3 ∣ 81 + 12 = 93, 12 ∣ 3 + 9).
example : 3 ∣ (3 ^ 2) ^ 2 + 4 * 1 ^ 2 * 3 ∧ 4 * 1 * 3 ∣ 3 + 3 ^ 2 := by decide
