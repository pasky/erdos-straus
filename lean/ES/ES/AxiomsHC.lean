import ES.HC

/-! Axiom audit for `ES.HC` (wave z56; expected: only `propext`, `Classical.choice`, `Quot.sound`). -/
#print axioms ESHC.ES_of_slot
#print axioms ESHC.core8
#print axioms ESHC.slot_iff_coord
#print axioms ESHC.ES_of_coord
#print axioms ESHC.ES_of_isCoord
#print axioms ESHC.ES_of_HCle
#print axioms ESHC.ES5_iff_HC_finite
#print axioms ESHC.coordU_iff
#print axioms ESHC.coordT_iff
#print axioms ESHC.isCoord_iff_fires
#print axioms ESHC.ES_of_lineU
#print axioms ESHC.ES_of_lineT
#print axioms ESHC.dvd_mod_four_of_S
#print axioms ESHC.exists_dvd_three_iff
#print axioms ESHC.S_sq_add_one
#print axioms ESHC.HC_gt_four_iff
#print axioms ESHC.HC_gt_two
#print axioms ESHC.HC_gt_three
#print axioms ESHC.theoremQ
#print axioms ESHC.theoremQ_no_line4
#print axioms ESHC.prop31a
#print axioms ESHC.prop31b_mod3_2
#print axioms ESHC.prop31b_mod7_3
#print axioms ESHC.prop31b_mod7_5
#print axioms ESHC.prop31b_mod5_3
#print axioms ESHC.prop31b_mod5_2
#print axioms ESHC.prop31b_mod7_6
#print axioms ESHC.HC_le_eight_of_nonresidue
#print axioms ESHC.cls840
#print axioms ESHC.prop31c
#print axioms ESHC.prop31c_classes

/-! Sanity examples. -/
-- FABLE §1.5: p = 193 has the word (7, 2, 15) with level 7 ≡ −193 (mod 8); Theorem 1 + slot formulas give ES(193).
example : ESHC.Word 193 7 2 15 := by unfold ESHC.Word; decide
example : ES.ESProp 193 :=
  ESHC.ES_of_coord (t := 7) (u := 2) (v := 15) (by norm_num) (by unfold ESHC.Word; decide) (Or.inl (by unfold ESHC.InC; decide))
-- Theorem Q at its least member m = 36, p = 6481 = 5·36² + 1: HC(6481) ≥ 7.
example : ¬ ESHC.HCle 6481 6 := (ESHC.theoremQ (m := 36) (by norm_num) (by norm_num) (by norm_num)).2.2.2.2
-- Lemma 1.1 needs no primality: n = 9 ≡ 1 (8), 13 and 37 are primes ≡ 1 (4), so HC(9) > 4.
example : ¬ ESHC.HCle 9 4 := by
  rw [ESHC.HC_gt_four_iff (by norm_num)]
  refine ⟨⟨by norm_num, fun q hq hd => ?_⟩, ⟨by norm_num, fun q hq hd => ?_⟩⟩
  · rw [(Nat.prime_dvd_prime_iff_eq hq (by norm_num)).mp hd]
  · rw [(Nat.prime_dvd_prime_iff_eq hq (by norm_num)).mp hd]
