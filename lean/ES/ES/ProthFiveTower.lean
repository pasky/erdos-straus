import ES.ProthCore

namespace ESProthCore

private theorem five_lift (i : ℕ) : (5 : ℤ)^(i+1) ∣ 2^(2*5^i) + 1 := by
  induction i with
  | zero => norm_num
  | succ i ih =>
    obtain ⟨c,hc⟩ := ih
    let a := (5 : ℤ)^i
    have hx : (2 : ℤ)^(2*5^i) = 5*a*c - 1 := by
      dsimp [a]; rw [pow_succ] at hc; linarith
    refine ⟨125*a^4*c^5-125*a^3*c^4+50*a^2*c^3-10*a*c^2+c, ?_⟩
    rw [show (2*5^(i+1) : ℕ) = (2*5^i)*5 by ring, pow_mul, hx]
    dsimp [a]; rw [pow_succ (5 : ℤ) (i+1), pow_succ (5 : ℤ) i]; ring

/-- The good-word/ES core (not full exponents) on the entire 5-power tower. -/
theorem core_five_tower (i : ℕ) : Core (5^(i+1)) := by
  apply core_of_doubling (b := 2*5^i)
  · exact le_trans (by decide : 5 ≤ 5^1) (Nat.pow_le_pow_right (by decide) (by omega))
  · exact (by decide : Odd (5 : ℕ)).pow
  · exact (by decide : Nat.Coprime 3 5).pow_right _
  · exact_mod_cast five_lift i

#print axioms core_five_tower
end ESProthCore
