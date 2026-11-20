import ES.Basic

/-!
# Proth core progressions from a negative doubling orbit

`core_of_doubling` proves the arithmetic conclusion of Theorem 1 of
`notes/z78/PROTH_ALLM.md` §1, using `h ∣ 2^b + 1` for `2^b ≡ −1 (mod h)`.
For example `proth_four_pow_core` applies at every `h = 4^i+1`, `i ≥ 1`.
The construction works by divisibility of successive odd binomials, without
factoring any polynomials. It does not give ES at all exponents for those
multipliers in general and does not formalize the noncovering conclusion.
Separately, `proth63` checks the all-exponent result for the first multiplier.
-/

namespace ESProthCore
open ES (ESProp)
open scoped BigOperators

/-- L1. A divisor word with `4 ∣ tv−1` gives the positive triple
`(ADn, uD, AuD)`, where `t=(A+1)/u`, `v=(n+u)/A`, `D=(tv−1)/4`.
No separate interiority hypothesis on `t,v` is needed. -/
theorem es_of_word {n u A : ℕ} (hn : 0 < n) (hu : 0 < u) (hA : 0 < A)
    (hav : A ∣ n + u) (htu : u ∣ A + 1)
    (h4 : 4 ∣ ((A + 1) / u) * ((n + u) / A) - 1) : ESProp n := by
  let t := (A + 1) / u
  let v := (n + u) / A
  have ht : t * u = A + 1 := Nat.div_mul_cancel htu
  have hv : v * A = n + u := Nat.div_mul_cancel hav
  have htv : t * v * u = n + u + v := by
    calc t * v * u = v * (t * u) := by ring
         _ = _ := by rw [ht, Nat.mul_add, hv, Nat.mul_one]
  have hgt : 1 < t * v := by
    by_contra! he
    have e : t * v * u ≤ u := by simpa using Nat.mul_le_mul_right u he
    rw [htv] at e
    exact (Nat.not_le_of_lt (lt_of_lt_of_le (by omega : u < n + u) (Nat.le_add_right _ _))) e
  obtain ⟨D, hD⟩ := h4
  change t * v - 1 = 4 * D at hD
  have hDpos : 0 < D := by omega
  have hDv : 4 * D * u = n + v := by
    have e : t * v = 4 * D + 1 := by omega
    rw [e, Nat.add_mul, Nat.one_mul] at htv
    omega
  have key : 4 * D * u * A = n * A + n + u := by
    rw [hDv, Nat.add_mul, hv]; omega
  refine ⟨A * D * n, u * D, A * u * D, by positivity, by positivity, by positivity, ?_⟩
  calc 4 * (A * D * n) * (u * D) * (A * u * D) =
        n * (A * u * D ^ 2) * (4 * D * u * A) := by ring
       _ = _ := by rw [key]; ring

/-- L2. `2 ∏ (1+2^(2^j))` is `−1` modulo the Mersenne modulus.
The statement uses divisibility to avoid truncated subtraction at `−1`. -/
theorem telescoping_neg_one {h b : ℕ} (hb : h ∣ 2 ^ b + 1) :
    2 ^ h - 1 ∣ 2 * (∏ j ∈ Finset.range b, (2 ^ (2 ^ j) + 1 : ℕ)) + 1 := by
  change 2 ^ h - 1 ∣ 2 * (∏ j ∈ Finset.range b, Nat.fermatNumber j) + 1
  rw [Nat.prod_fermatNumber, Nat.fermatNumber]
  have hp : 0 < (2 : ℕ) ^ (2 ^ b) := by positivity
  have e : 2 * (2 ^ (2 ^ b) + 1 - 2) + 1 = 2 ^ (2 ^ b + 1) - 1 := by
    rw [pow_succ]; omega
  rw [e, Nat.dvd_iff_mod_eq_zero, Nat.pow_sub_one_mod_pow_sub_one, Nat.mod_eq_zero_of_dvd hb]
  decide

/-- The doubling hypothesis holds identically at `h=4^i+1`, with `b=2i`. -/
theorem telescoping_four_pow (i : ℕ) :
    2 ^ (4 ^ i + 1) - 1 ∣ 2 * (∏ j ∈ Finset.range (2 * i), (2 ^ (2 ^ j) + 1 : ℕ)) + 1 := by
  apply telescoping_neg_one
  rw [pow_mul]; exact dvd_refl _

/-! ### Building a divisor by successive odd exponent extensions

Only divisibility of binomials at integer arguments is needed: a selected
quotient times the previous divisor divides the new binomial. Thus there is
no coprimality assumption on different cyclotomic values.
-/

private abbrev H (h : ℕ) := 2 ^ h - 1
private abbrev R (h : ℕ) := ZMod (H h)
private abbrev Y (h a : ℕ) : R h := 2 ^ a + 1

private theorem period_two (h : ℕ) : (2 : R h) ^ h = 1 := by
  have hp : 1 ≤ (2 : ℕ) ^ h := Nat.one_le_pow _ _ (by decide)
  have eq : 2 ^ h = H h + 1 := by dsimp [H]; omega
  have := congrArg (Nat.cast : ℕ → R h) eq
  simpa using this

/-- Bounded odd representative of any residue, when the modulus is odd. -/
private theorem odd_rep {h : ℕ} (ho : Odd h) (x : ZMod h) :
    ∃ d : ℕ, Odd d ∧ d ≤ 2 * h ∧ (d : ZMod h) = x := by
  have : NeZero h := ⟨ho.pos.ne'⟩
  have hl := x.val_lt
  rcases Nat.even_or_odd x.val with he | he
  · exact ⟨x.val + h, he.add_odd ho, by omega, by simp⟩
  · exact ⟨x.val, he, by omega, by simp⟩

private theorem steer {h e a : ℕ} (ho : Odd h) (he : IsUnit (e : ZMod h)) :
    ∃ d : ℕ, Odd d ∧ d ≤ 2 * h ∧ (↑(e * d) : ZMod h) = a := by
  obtain ⟨d, hd, hb, eq⟩ := odd_rep ho ((↑he.unit⁻¹ : ZMod h) * a)
  refine ⟨d, hd, hb, ?_⟩
  rw [Nat.cast_mul, eq, ← mul_assoc]
  have hv : (e : ZMod h) * (↑he.unit⁻¹ : ZMod h) = 1 := by
    simpa only [he.unit_spec] using Units.mul_inv he.unit
  rw [hv, one_mul]

private def Reach (h : ℕ) (z : R h) : Prop :=
  ∃ E : ℕ, Odd E ∧ IsUnit (E : ZMod h) ∧ ∀ X : ℕ, (X : R h) = 2 → (X : ZMod 16) = 0 →
    ∃ A : ℕ, A ∣ X ^ E + 1 ∧ (A : R h) = z ∧ (A : ZMod 16) = 1

private theorem reach_one (h : ℕ) : Reach h 1 := by
  refine ⟨1, odd_one, by simp, fun X _ _ => ⟨1, one_dvd _, by simp, by simp⟩⟩

private theorem extend {h a b : ℕ} {w z : R h} (ho : Odd h) (hw : Reach h w)
    (ha : IsUnit (a : ZMod h)) (hb : IsUnit (b : ZMod h))
    (hy : IsUnit (Y h a)) (hz : z * Y h a = w * Y h b) : Reach h z := by
  obtain ⟨E, hoE, huE, hE⟩ := hw
  obtain ⟨d, hd, _, ed⟩ := steer (a := a) ho huE
  obtain ⟨f, hf, _, ef⟩ := steer (a := b) ho (ed ▸ ha : IsUnit (↑(E * d) : ZMod h))
  refine ⟨E * d * f, (hoE.mul hd).mul hf, ef ▸ hb, ?_⟩
  intro X hX h16
  obtain ⟨A, hA, hAw, hA16⟩ := hE X hX h16
  have bin (v m : ℕ) (hm : Odd m) : X ^ v + 1 ∣ X ^ (v * m) + 1 := by
    simpa [pow_mul] using hm.nat_add_dvd_pow_add_pow (X ^ v) 1
  obtain ⟨q, hq⟩ := bin (E * d) f hf
  refine ⟨A * q, ?_, ?_, ?_⟩
  · rw [hq]; exact mul_dvd_mul (hA.trans (bin E d hd)) (dvd_refl q)
  · have eval {k l : ℕ} (eq : (k : ZMod h) = l) : ((X ^ k + 1 : ℕ) : R h) = Y h l := by
      push_cast; rw [hX, pow_eq_pow_of_modEq ((ZMod.natCast_eq_natCast_iff ..).mp eq) (period_two h)]
    have eq := congrArg (Nat.cast : ℕ → R h) hq
    rw [Nat.cast_mul, eval ed, eval ef] at eq
    rw [Nat.cast_mul, hAw]; apply hy.mul_right_cancel
    rw [mul_assoc, mul_comm (q : R h), ← eq, ← hz]
  · have eq := congrArg (Nat.cast : ℕ → ZMod 16) hq
    push_cast at eq ⊢
    have hne := ((hoE.mul hd).mul hf).pos.ne'
    have hne' := (hoE.mul hd).pos.ne'
    simpa [hA16, h16, hne, hne', eq_comm] using eq

private theorem three_unit {h : ℕ} (ho : Odd h) : IsUnit (3 : R h) := by
  apply (ZMod.isUnit_iff_coprime 3 (H h)).2
  apply Nat.prime_three.coprime_iff_not_dvd.mpr
  intro hd
  have eq := (ZMod.natCast_eq_zero_iff _ _).2 hd
  have hp : 1 ≤ (2 : ℕ) ^ h := Nat.one_le_pow _ _ (by decide)
  change ((2 ^ h - 1 : ℕ) : ZMod 3) = 0 at eq
  rw [Nat.cast_sub hp, Nat.cast_pow, Nat.cast_ofNat, Nat.cast_one,
    show (2 : ZMod 3) = -1 by decide, ho.neg_one_pow] at eq
  exact (by decide : (-1 - 1 : ZMod 3) ≠ 0) eq

/-- At unit indices every `Y_a` can be appended to a reachable product:
first append `Y₃/Y₁=3`, then multiply by `Y_a/Y₁`. -/
private theorem append_Y {h a : ℕ} {w : R h} (ho : Odd h) (h3 : IsUnit (3 : ZMod h))
    (ha : IsUnit (a : ZMod h)) (hw : Reach h w) : Reach h (w * Y h a) := by
  have h1 : Y h 1 = 3 := by norm_num [Y]
  have hy : IsUnit (Y h 1) := h1 ▸ three_unit ho
  have hw3 : Reach h (w * 3) := by
    apply extend (a := 1) (b := 3) ho hw (by simp) (by simpa using h3) hy
    norm_num [Y]; ring
  apply extend (a := 1) (b := a) ho hw3 (by simp) ha hy
  rw [h1]; ring

private theorem reach_neg_one {h b : ℕ} (hh : 1 ≤ h) (ho : Odd h)
    (h3 : IsUnit (3 : ZMod h)) (hb : h ∣ 2 ^ b + 1) : Reach h (-1) := by
  -- Y₁/Y_{−1}=2, where the negative index is represented by h−1.
  have ei : ((h - 1 : ℕ) : ZMod h) = -1 := by simp [Nat.cast_sub hh]
  have ey : (2 : R h) * Y h (h - 1) = 3 := by
    have ep : (2 : R h) ^ (h - 1) * 2 = 1 := by
      rw [← pow_succ, Nat.sub_add_cancel hh, period_two]
    dsimp [Y]; linear_combination ep
  have h2 : Reach h 2 := by
    apply extend (a := h - 1) (b := 1) ho (reach_one h) (by simp [ei]) (by simp)
      (isUnit_of_mul_isUnit_right (ey ▸ three_unit ho : IsUnit ((2 : R h) * Y h (h - 1))))
    norm_num [Y] at ey ⊢; exact ey
  have hu2 : IsUnit (2 : ZMod h) := (ZMod.isUnit_iff_coprime 2 h).2 (Nat.coprime_two_left.2 ho)
  have prod (k : ℕ) : Reach h (2 * ∏ j ∈ Finset.range k, Y h (2 ^ j)) := by
    induction k with
    | zero => simpa using h2
    | succ k ih =>
      rw [Finset.prod_range_succ, ← mul_assoc]
      exact append_Y ho h3 (by push_cast; exact hu2.pow _) ih
  have key := (ZMod.natCast_eq_zero_iff _ _).2 (telescoping_neg_one hb)
  push_cast at key
  have eq : (2 * ∏ j ∈ Finset.range b, Y h (2 ^ j)) = -1 := by
    apply eq_neg_of_add_eq_zero_left; exact key
  exact eq ▸ prod b

private theorem cast_two_pow_zero {r l : ℕ} (hl : l ≤ r) : ((2 ^ r : ℕ) : ZMod (2 ^ l)) = 0 :=
  (ZMod.natCast_eq_zero_iff ..).2 (pow_dvd_pow 2 hl)

/-- Lift a single reachable residue to a divisor on *all* positive multiples of
one period. Include `(2h)!` in the period. Its odd factors supply an odd
steering multiplier after removing the full dyadic part of the exponent. -/
private theorem periodic_divisor {h : ℕ} {z : R h} (ho : Odd h) (hz : Reach h z) :
    ∃ P > 0, 4 ∣ P ∧ ∀ s : ℕ, 0 < s → P ∣ s →
      ∃ A : ℕ, A ∣ 2 ^ s + 1 ∧ (A : R h) = z ∧ (A : ZMod 16) = 1 := by
  obtain ⟨E, hoE, _, hE⟩ := hz
  let F := (2 * h).factorial
  have hF : 0 < F := Nat.factorial_pos _
  have hp := hoE.pos
  refine ⟨4 * (E * F), by positivity, dvd_mul_right .., ?_⟩
  intro s hs hd
  obtain ⟨k, hk⟩ := hd
  have hk0 : k ≠ 0 := by rintro rfl; simp_all
  obtain ⟨v, m, hm, hvm⟩ := Nat.exists_eq_two_pow_mul_odd (Nat.mul_ne_zero hF.ne' hk0)
  let B := 4 * 2 ^ v
  have hu : IsUnit (2 : ZMod h) := (ZMod.isUnit_iff_coprime 2 h).2 (Nat.coprime_two_left.2 ho)
  have hB : IsUnit (B : ZMod h) := by
    dsimp [B]; push_cast; exact (by convert hu.mul hu using 1; norm_num : IsUnit (4 : ZMod h)).mul (hu.pow v)
  obtain ⟨d, hod, hdle, heq⟩ := steer (a := 1) ho hB
  have hdF : d ∣ F := Nat.dvd_factorial hod.pos hdle
  have hdm : d ∣ m := by
    apply ((Nat.coprime_two_right.2 hod).pow_right v).dvd_of_dvd_mul_left
    rw [← hvm]; exact dvd_mul_of_dvd_left hdF k
  obtain ⟨q, hq⟩ := hdm
  have hoq : Odd q := Nat.Odd.of_mul_right (hq ▸ hm : Odd (d * q))
  let r := B * d
  have hr : 4 ≤ r := by
    dsimp [r, B]; have hv : 1 ≤ (2 : ℕ) ^ v := Nat.one_le_pow _ _ (by decide)
    exact le_trans (by omega : 4 ≤ 4 * 2 ^ v) (Nat.le_mul_of_pos_right _ hod.pos)
  have hx : ((2 ^ r : ℕ) : R h) = 2 := by
    push_cast
    simpa using pow_eq_pow_of_modEq ((ZMod.natCast_eq_natCast_iff ..).mp heq) (period_two h)
  obtain ⟨A, hA, hAz, h16⟩ := hE (2 ^ r) hx (cast_two_pow_zero (l := 4) hr)
  have eq : s = r * E * q := by
    calc s = 4 * E * (F * k) := by rw [hk]; ring
         _ = _ := by rw [hvm, hq]; dsimp [r, B]; ring
  refine ⟨A, hA.trans ?_, hAz, h16⟩
  rw [eq, pow_mul (2 : ℕ) (r * E) q, pow_mul (2 : ℕ) r E]
  simpa using hoq.nat_add_dvd_pow_add_pow ((2 ^ r) ^ E) 1

/-- Interior word with the sufficient goodness condition `8 ∣ n+t`. -/
def InteriorGoodWord (n u : ℕ) : Prop :=
  ∃ t v : ℕ, 2 ≤ t ∧ 2 ≤ u ∧ 2 ≤ v ∧ n + u + v = t * u * v ∧ 8 ∣ n + t

/-- The core progression conclusion; it is not an all-exponents result. -/
def Core (h : ℕ) : Prop :=
  ∃ P > 0, ∀ s : ℕ, 0 < s → P ∣ s →
    let u := 2 * (2 ^ h - 1)
    let n := (u + 1) * 2 ^ s + 1
    InteriorGoodWord n u ∧ ESProp n

private theorem word_of_core_divisor {h s A : ℕ} (hh : 4 ≤ h) (hs : 4 ≤ s)
    (hd : A ∣ 2 ^ s + 1) (hz : (A : R h) = -1) (h16 : (A : ZMod 16) = 1) :
    let u := 2 * H h
    let n := (u + 1) * 2 ^ s + 1
    InteriorGoodWord n u ∧ ESProp n := by
  intro u n
  have hH : 1 ≤ H h := by
    have e := Nat.pow_le_pow_right (by decide : 0 < 2) hh
    dsimp [H]; omega
  have hu : 2 ≤ u := by dsimp [u]; omega
  have hn : 0 < n := by dsimp [n]; positivity
  have hA : 0 < A := Nat.pos_of_dvd_of_pos hd (by positivity)
  have hA1 : H h ∣ A + 1 := (ZMod.natCast_eq_zero_iff ..).1 (by push_cast; rw [hz]; simp)
  have hp : 1 ≤ (2 : ℕ) ^ h := Nat.one_le_pow _ _ (by decide)
  have hHr : (H h : ZMod 16) = -1 := by
    rw [H, Nat.cast_sub hp, cast_two_pow_zero (l := 4) hh]; simp
  have Hu : (u : ZMod 16) = 14 := by
    dsimp [u]; push_cast; rw [hHr]; decide
  have Hr : H h % 16 = 15 := (ZMod.natCast_eq_natCast_iff' (H h) 15 16).mp (by rw [hHr]; decide)
  have Ar : A % 16 = 1 := (ZMod.natCast_eq_natCast_iff' A 1 16).mp (by simpa only [Nat.cast_one] using h16)
  have htu : u ∣ A + 1 := (Nat.coprime_two_left.2 (Nat.odd_iff.2 (by omega : H h % 2 = 1))).mul_dvd_of_dvd_of_dvd
    (by omega) hA1
  have hav : A ∣ n + u := by
    have e : n + u = (2 ^ s + 1) * (u + 1) := by dsimp [n]; ring
    rw [e]; exact dvd_mul_of_dvd_left hd _
  let t := (A + 1) / u
  let v := (n + u) / A
  have ht : t * u = A + 1 := Nat.div_mul_cancel htu
  have hv : A * v = n + u := by rw [Nat.mul_comm]; exact Nat.div_mul_cancel hav
  have ur : u % 16 = 14 := (ZMod.natCast_eq_natCast_iff' u 14 16).mp Hu
  have nr : n % 16 = 1 := by
    apply (ZMod.natCast_eq_natCast_iff' n 1 16).mp
    dsimp [n]; rw [Nat.cast_add, Nat.cast_mul, cast_two_pow_zero (l := 4) hs]; simp
  have tr : t % 8 = 7 := by
    have e := congrArg (· % 16) ht
    change t * u % 16 = (A + 1) % 16 at e
    rw [Nat.mul_mod, ur, Nat.add_mod, Ar] at e; omega
  have vr : v % 8 = 7 := by
    have e := congrArg (· % 16) hv
    change A * v % 16 = (n + u) % 16 at e
    rw [Nat.mul_mod, Ar, Nat.add_mod, nr, ur] at e; omega
  constructor
  · refine ⟨t, v, by have := Nat.mod_le t 8; omega, hu, by have := Nat.mod_le v 8; omega, ?_, by omega⟩
    rw [ht, ← hv]; ring
  · apply es_of_word hn (by omega) hA hav htu
    change 4 ∣ t * v - 1
    have e := Nat.mul_mod t v 8
    rw [tr, vr] at e; omega

/-- The arithmetic core of `PROTH_ALLM` §1, Theorem 1: every positive
multiple of a common period has an interior good word and satisfies ES. -/
theorem core_of_doubling {h b : ℕ} (hh : 5 ≤ h) (ho : Odd h)
    (h3 : Nat.Coprime 3 h) (hb : h ∣ 2 ^ b + 1) : Core h := by
  obtain ⟨P, hP, h4, hw⟩ := periodic_divisor ho (reach_neg_one (by omega) ho
    ((ZMod.isUnit_iff_coprime ..).2 h3) hb)
  refine ⟨P, hP, fun s hs hd => ?_⟩
  obtain ⟨A, ha, hz, h16⟩ := hw s hs hd
  exact word_of_core_divisor (by omega) (Nat.le_of_dvd hs (h4.trans hd)) ha hz h16

/-- In particular the core exists for the unbounded family `h = 4^i+1`, i ≥ 1. -/
theorem core_four_pow {i : ℕ} (hi : 1 ≤ i) : Core (4 ^ i + 1) := by
  apply core_of_doubling (b := 2 * i)
  · have := Nat.pow_le_pow_right (by decide : 0 < 4) hi; omega
  · exact ((by decide : Even 4).pow_of_ne_zero (by omega : i ≠ 0)).add_one
  · apply Nat.prime_three.coprime_iff_not_dvd.mpr
    have eq : 4 ^ i + 1 ≡ 1 ^ i + 1 [MOD 3] := ((by decide : 4 ≡ 1 [MOD 3]).pow i).add_right 1
    simp [Nat.ModEq] at eq; omega
  · rw [pow_mul]; exact dvd_refl _

/-- ES-only projection, in the notation `k = 2^(h+1)−1` of the family. -/
theorem proth_four_pow_core {i : ℕ} (hi : 1 ≤ i) :
    let h := 4 ^ i + 1
    ∃ P > 0, ∀ s : ℕ, 0 < s → P ∣ s → ESProp ((2 ^ (h + 1) - 1) * 2 ^ s + 1) := by
  intro h
  obtain ⟨P, hp, hall⟩ := core_four_pow hi
  refine ⟨P, hp, fun s hs hd => ?_⟩
  have hp2 : 0 < (2 : ℕ) ^ h := by positivity
  have e : 2 ^ (h + 1) - 1 = 2 * (2 ^ h - 1) + 1 := by rw [pow_succ]; omega
  rw [e]; exact (hall s hs hd).2

#print axioms proth_four_pow_core
#print axioms core_four_pow
#print axioms core_of_doubling
#print axioms es_of_word
#print axioms telescoping_neg_one
#print axioms telescoping_four_pow

/-! ### All exponents for the first multiplier (h=5, k=63)

This additional theorem is `EXP_OPEN.md` §§2–3. The moving cubic on `24 ∣ s`
is separate from the abstract progression theorem. The 18 fixed signatures
are from `data/z19/cert63_et.json`; both the polynomial triples and coverage
are checked by the kernel.
-/

private abbrev modulus63 : ℕ := 19032425900237469720

private structure Row63 where
  m : ℕ
  r : ℕ
  dvd : m ∣ modulus63
  cert : ∀ k : ℕ, 0 < m * k + r → ESProp (m * k + r)

private def menu63 : List Row63 := [
  ⟨5, 0, by decide, fun k hk => by
    have : 0 < k := by omega
    refine ⟨2 * k, 4 * k, 20 * k,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨15, 7, by decide, fun k _ => by
    refine ⟨2 + 4 * k, 28 + 60 * k, 28 + 116 * k + 120 * k ^ 2,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨15, 13, by decide, fun k _ => by
    refine ⟨4 + 4 * k, 52 + 60 * k, 26 + 56 * k + 30 * k ^ 2,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨119, 57, by decide, fun k _ => by
    refine ⟨15 + 30 * k, 1710 + 3570 * k, 342 + 1398 * k + 1428 * k ^ 2,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨39, 34, by decide, fun k _ => by
    refine ⟨10 + 10 * k, 340 + 390 * k, 68 + 146 * k + 78 * k ^ 2,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨19, 18, by decide, fun k _ => by
    refine ⟨5 + 5 * k, 90 + 95 * k, 90 + 185 * k + 95 * k ^ 2,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨584, 545, by decide, fun k _ => by
    refine ⟨1113980 + 2387246 * k + 1278960 * k ^ 2, 146 + 146 * k, 2044 + 4234 * k + 2190 * k ^ 2,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨11, 0, by decide, fun k hk => by
    have : 0 < k := by omega
    refine ⟨3 * k, 34 * k, 1122 * k,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨11, 8, by decide, fun k _ => by
    refine ⟨3 + 3 * k, 24 + 33 * k, 8 + 19 * k + 11 * k ^ 2,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨11, 7, by decide, fun k _ => by
    refine ⟨2 + 3 * k, 21 + 33 * k, 42 + 129 * k + 99 * k ^ 2,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨29, 0, by decide, fun k hk => by
    have : 0 < k := by omega
    refine ⟨8 * k, 78 * k, 9048 * k,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨87, 43, by decide, fun k _ => by
    refine ⟨11 + 22 * k, 946 + 1914 * k, 946 + 3806 * k + 3828 * k ^ 2,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨127, 0, by decide, fun k hk => by
    have : 0 < k := by omega
    refine ⟨32 * k, 4065 * k, 16520160 * k,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨127, 126, by decide, fun k _ => by
    refine ⟨32 + 32 * k, 4032 + 4064 * k, 4032 + 8096 * k + 4064 * k ^ 2,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨344, 321, by decide, fun k _ => by
    refine ⟨386484 + 828266 * k + 443760 * k ^ 2, 86 + 86 * k, 1204 + 2494 * k + 1290 * k ^ 2,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨1016, 1001, by decide, fun k _ => by
    refine ⟨254 + 254 * k, 17017 + 34289 * k + 17272 * k ^ 2, 4322318 + 8709406 * k + 4387088 * k ^ 2,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨5620, 5109, by decide, fun k _ => by
    refine ⟨71781450 + 157920595 * k + 86857100 * k ^ 2, 1405 + 1405 * k, 14050 + 29505 * k + 15455 * k ^ 2,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩,
  ⟨51944, 22553, by decide, fun k _ => by
    refine ⟨890121804 + 6134789834 * k + 14093757744 * k ^ 2 + 10792716544 * k ^ 3, 5676 + 12986 * k, 848562 + 3893951 * k + 4467184 * k ^ 2,
      by positivity, by positivity, by positivity, ?_⟩
    ring⟩]

private abbrev n63 (s : ℕ) := 63 * 2 ^ s + 1

private def hit63 (s : ℕ) : Bool := menu63.any fun row => n63 s % row.m == row.r

private theorem transport63 {s e : ℕ} (he : hit63 e = true)
    (hc : n63 s ≡ n63 e [MOD modulus63]) : ESProp (n63 s) := by
  obtain ⟨row, _, hr⟩ := List.any_eq_true.mp he
  have hr' : n63 s % row.m = row.r := Eq.trans (hc.of_dvd row.dvd) (beq_iff_eq.mp hr)
  have eq := Nat.div_add_mod (n63 s) row.m
  rw [hr'] at eq
  have hp : 0 < row.m * (n63 s / row.m) + row.r := by rw [eq]; positivity
  simpa only [eq] using row.cert _ hp

private theorem scaled_period {x a m : ℕ} (hx : x * a ≡ x [MOD m]) (q : ℕ) :
    x * a ^ q ≡ x [MOD m] := by
  induction q with
  | zero => simp [Nat.ModEq]
  | succ q ih => rw [pow_succ, ← mul_assoc]; exact (ih.mul_right a).trans hx

set_option exponentiation.threshold 4096 in
private theorem periodic63 (s : ℕ) : n63 (s + 3) ≡ n63 (s % 2520 + 3) [MOD modulus63] := by
  let q := s / 2520
  let r := s % 2520
  have e : s + 3 = 3 + 2520 * q + r := by dsimp [q, r]; omega
  have hx := scaled_period (by decide : 2 ^ 3 * 2 ^ 2520 ≡ 2 ^ 3 [MOD modulus63]) q
  apply Nat.ModEq.add_right; apply Nat.ModEq.mul_left
  rw [e, pow_add, pow_add, pow_mul]
  change _ ≡ 2 ^ (r + 3) [MOD modulus63]; rw [add_comm r, pow_add]; exact hx.mul_right _

-- Split the 2520 checks into small blocks so kernel reduction stays shallow.
set_option exponentiation.threshold 4096 in
set_option maxRecDepth 8192 in
set_option maxHeartbeats 4000000 in
private theorem covered63 : ∀ a : Fin 42, ∀ b : Fin 60,
    let e := 60 * a.val + b.val + 3
    24 ∣ e ∨ hit63 e = true := by decide

private theorem cubic63 (k : ℕ) : ESProp (63 * (340 * k + 256) ^ 3 + 1) := by
  let n := 63 * (340 * k + 256) ^ 3 + 1
  let b := 3109291 + 12387831 * k + 16451580 * k ^ 2 + 7282800 * k ^ 3
  let c := 16 + 21 * k
  refine ⟨5 * b * 17, 5 * c * 17 * n, b * c * 17 * n, by dsimp [b]; positivity,
    by dsimp [c,n]; positivity, by dsimp [b,c,n]; positivity, ?_⟩
  dsimp [b, c, n]; ring

private theorem core63 {s : ℕ} (hs : 0 < s) (hd : 24 ∣ s) : ESProp (n63 s) := by
  obtain ⟨q, hq⟩ := hd
  obtain ⟨j, rfl⟩ := Nat.exists_eq_succ_of_ne_zero (by omega : q ≠ 0)
  have eq : 256 ^ (j + 1) % 340 = 256 := by
    have := scaled_period (by decide : 256 * 256 ≡ 256 [MOD 340]) j
    simpa [pow_succ', Nat.ModEq] using this
  let y := 256 ^ (j + 1)
  have ey : 340 * (y / 340) + 256 = y := by dsimp [y]; omega
  have en : n63 s = 63 * y ^ 3 + 1 := by
    dsimp [n63, y]; rw [hq, show 24 * (j + 1) = 8 * (j + 1) * 3 by ring, pow_mul, pow_mul]
    norm_num
  rw [en, ← ey]; exact cubic63 _

/-- The first multiplier in the four-power core family is also closed on
*all* exponents, by the independent cubic and the 18 fixed classes. -/
theorem proth63 (s : ℕ) : ESProp (63 * 2 ^ s + 1) := by
  rcases Nat.lt_or_ge s 3 with h | h
  · interval_cases s
    · exact ⟨32, 64, 64, by decide, by decide, by decide, by decide⟩
    all_goals exact transport63 (s := _) (e := _) (by decide) (Nat.ModEq.refl _)
  · let d := s - 3
    have eq : s = d + 3 := by dsimp [d]; omega
    rw [eq]
    let r := d % 2520
    have hr : r < 2520 := Nat.mod_lt _ (by decide)
    obtain hc | hc := covered63 ⟨r / 60, by omega⟩ ⟨r % 60, Nat.mod_lt _ (by decide)⟩
    · apply core63 (by omega); change 24 ∣ 60 * (r / 60) + r % 60 + 3 at hc
      dsimp [r] at hc; omega
    · change hit63 (60 * (r / 60) + r % 60 + 3) = true at hc
      rw [Nat.div_add_mod] at hc
      exact transport63 hc (periodic63 d)

#print axioms proth63
end ESProthCore
