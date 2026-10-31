import Mathlib

/-- Skeleton. -/
def ESProp (n : ℕ) : Prop :=
  ∃ x y z : ℕ, 0 < x ∧ 0 < y ∧ 0 < z ∧ 4 * x * y * z = n * (x * y + y * z + z * x)

#check @jacobiSym.quadratic_reciprocity'
#check @jacobiSym.mod_right'
#check @jacobiSym.mod_left
#check @jacobiSym.at_two
#check @jacobiSym.at_neg_one
#check @jacobiSym.mul_left
#check @jacobiSym.pow_left
#check @jacobiSym.sq_one'
#check @jacobiSym.one_left
#check @jacobiSym.eq_zero_iff
#check @Nat.exists_eq_two_pow_mul_odd
#check @jacobiSym.quadratic_reciprocity_one_mod_four
#check @jacobiSym.mod_left'
#check @ZMod.χ₄_nat_three_mod_four
#check @ZMod.χ₈_nat_eq_if_mod_eight
#check @ZMod.χ₄_nat_eq_if_mod_four
