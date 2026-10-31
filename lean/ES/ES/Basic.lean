import Mathlib

/-!
# Z1546: the C-form certificate ⟹ Erdős–Straus, and the square obstruction T1

Erdős–Straus (ES) is OPEN. Nothing here proves it; this file formalises two small, self-contained facts used
throughout the repository.

## Repository statements being formalised

* C-form (`BRAINSTORM/z52b_free_fable.md:67`, item 152 at `:389`): "4Cp + 1 = ab with a ≡ b ≡ −1 (mod 4C)
  (equivalently the word p = 4Cuv − u − v) … it gives x = Cuv, y = pCv, z = pCu". Here it is stated for an
  arbitrary natural n in place of p, in divisor form: `a ∣ 4Cn + 1` and `4C ∣ a + 1` (the cofactor b then
  automatically satisfies `4C ∣ b + 1`, Lemma `cofactor_dvd`).
* T1 for the C-form (`BRAINSTORM/z52b_free_fable.md:202` item, line `:489`; `FRONTIER.md:241`;
  `PARITY_AUDIT.md:214` Lemma 3.2): no square n = m² has a C-form certificate; equivalently (shifted form) for every
  u ≥ 1, m² + u has no divisor f ≡ −1 (mod 4u). Oddness of m is not needed (as `PARITY_AUDIT.md:214` already notes).
* QNR lemma (`BRAINSTORM/z52b_free_fable.md:489`): every C-form divisor a satisfies (n/a) = −1 (Jacobi), hence
  (a/n) = −1 when n ≡ 1 (mod 4).

## Paper proof, in the exact steps the Lean code follows

**Lemma A (`jacobi_C_of_dvd_succ`).** If 4C ∣ a + 1 (C, a ∈ ℕ) then J(C | a) = 1.
1. C ≠ 0 (else a + 1 = 0), and a % 4 = 3, so a is odd.
2. Write C = 2^k · C' with C' odd. J(C | a) = J(2 | a)^k · J(C' | a)  (multiplicativity in the top argument).
3. J(2 | a)^k = 1: if k = 0 trivially; if k ≥ 1 then 8 ∣ 4C ∣ a + 1, so a % 8 = 7 and J(2 | a) = χ₈(a) = 1.
4. Reciprocity (both odd): J(C' | a) = qrSign(a, C') · J(a | C'), where qrSign(a, C') = J(χ₄(a) | C') = J(−1 | C')
   since a ≡ 3 (mod 4).
5. C' ∣ a + 1, so a ≡ −1 (mod C') and J(a | C') = J(−1 | C').
6. J(C' | a) = J(−1 | C')² = 1 since gcd(−1, C') = 1.

**Lemma B (`jacobi_n_of_cform`, the QNR lemma).** If a ∣ 4Cn + 1 and 4C ∣ a + 1 then J(n | a) = −1.
1. a % 4 = 3 (as in A.1), so J(−1 | a) = χ₄(a) = −1.
2. 4Cn ≡ −1 (mod a), so J(4Cn | a) = J(−1 | a) = −1.
3. J(4Cn | a) = J(2 | a)² · J(C | a) · J(n | a) = 1 · 1 · J(n | a) (gcd(2, a) = 1; Lemma A).

**Theorem T1 (`no_cform_square`).** For all m, C, a: ¬ (a ∣ 4Cm² + 1 ∧ 4C ∣ a + 1).
  By Lemma B, J(m² | a) = −1; but J(m² | a) = J(m | a)² ∈ {0, 1}.

**Theorem T1, shifted form (`no_shifted_square`).** For all m, u, f: ¬ (f ∣ m² + u ∧ 4u ∣ f + 1).
  m² ≡ −u (mod f), so J(m | f)² = J(m² | f) = J(−u | f) = J(−1 | f) · J(u | f) = (−1) · 1 (Lemma A with C = u).

**Theorem (`cform_ES`).** If a ∣ 4Cn + 1 and 4C ∣ a + 1 then ES(n) with x = Cuv, y = nCv, z = nCu, where
a + 1 = 4Cu, b + 1 = 4Cv, ab = 4Cn + 1.
1. 4C ∣ b + 1: 4C · (ub) = (a + 1) b = (4Cn + 1) + b, so 4C ∣ 4Cn + (b + 1).
2. (a + 1)(b + 1) + 1 = ab + (a + 1) + (b + 1) gives 4C · 4Cuv = 4C (n + u + v), so n + u + v = 4Cuv (C ≠ 0).
3. u, v ≥ 1 (a + 1, b + 1 > 0), C ≥ 1, and n ≥ 1 (n = 0 would give u + v = 4Cuv ≥ 4uv > u + v).
4. 4xyz − n(xy + yz + zx) = n²C²uv · (4Cuv − (n + u + v)) = 0.
-/

namespace ES

/-- The Erdős–Straus property of `n`: `4/n = 1/x + 1/y + 1/z` in positive integers, cleared of denominators. -/
def ESProp (n : ℕ) : Prop :=
  ∃ x y z : ℕ, 0 < x ∧ 0 < y ∧ 0 < z ∧ 4 * x * y * z = n * (x * y + y * z + z * x)

/-- The Erdős–Straus conjecture (OPEN). Stated only; not proved here. -/
def ErdosStraus : Prop := ∀ n : ℕ, 2 ≤ n → ESProp n

/-- The cleared form is equivalent to the rational identity `4/n = 1/x + 1/y + 1/z` (for `n > 0`). -/
theorem ESProp_iff_rat (n : ℕ) (hn : 0 < n) :
    ESProp n ↔ ∃ x y z : ℕ, 0 < x ∧ 0 < y ∧ 0 < z ∧
      (4 : ℚ) / n = 1 / x + 1 / y + 1 / z := by
  constructor
  · rintro ⟨x, y, z, hx, hy, hz, h⟩
    refine ⟨x, y, z, hx, hy, hz, ?_⟩
    have hq : (4 : ℚ) * x * y * z = n * (x * y + y * z + z * x) := by exact_mod_cast h
    field_simp
    linear_combination hq
  · rintro ⟨x, y, z, hx, hy, hz, h⟩
    refine ⟨x, y, z, hx, hy, hz, ?_⟩
    have hn' : (n : ℚ) ≠ 0 := by positivity
    have hx' : (x : ℚ) ≠ 0 := by positivity
    have hy' : (y : ℚ) ≠ 0 := by positivity
    have hz' : (z : ℚ) ≠ 0 := by positivity
    field_simp at h
    exact_mod_cast (by linear_combination h : (4 : ℚ) * x * y * z = n * (x * y + y * z + z * x))

/-- A C-form certificate for `n` (divisor form): `a ∣ 4Cn + 1` with `a ≡ −1 (mod 4C)`.
(`BRAINSTORM/z52b_free_fable.md:67`: `4Cp + 1 = ab`, `a ≡ b ≡ −1 (mod 4C)`; see `cofactor_dvd` for `b`.) -/
def CForm (n C a : ℕ) : Prop := a ∣ 4 * C * n + 1 ∧ 4 * C ∣ a + 1

/-- The cofactor `b = (4Cn+1)/a` of a C-form divisor is also `≡ −1 (mod 4C)`. -/
theorem cofactor_dvd {n C a b : ℕ} (hab : 4 * C * n + 1 = a * b) (ha : 4 * C ∣ a + 1) :
    4 * C ∣ b + 1 := by
  obtain ⟨u, hu⟩ := ha
  have h : 4 * C * n + (b + 1) = 4 * C * (u * b) := by
    calc 4 * C * n + (b + 1) = (a + 1) * b + 1 - 1 + 1 - 1 := by rw [add_mul, ← hab]; omega
      _ = 4 * C * (u * b) := by rw [hu]; simp [mul_assoc]
  exact (Nat.dvd_add_right (dvd_mul_right _ _)).mp (h ▸ dvd_mul_right _ _)

/-! ### Part (a): C-form ⟹ ES -/

/-- **C-form ⟹ ES (explicit).** From `a ∣ 4Cn+1`, `a + 1 = 4Cu`, `(4Cn+1)/a + 1 = 4Cv`, the triple
`x = Cuv, y = nCv, z = nCu` solves `4xyz = n(xy+yz+zx)` in positive integers. -/
theorem cform_ES {n C a : ℕ} (h : CForm n C a) : ESProp n := by
  obtain ⟨⟨b, hab⟩, ha⟩ := h
  have hb := cofactor_dvd hab ha
  obtain ⟨u, hu⟩ := ha
  obtain ⟨v, hv⟩ := hb
  have hC : C ≠ 0 := by rintro rfl; omega
  have hu0 : u ≠ 0 := by rintro rfl; omega
  have hv0 : v ≠ 0 := by rintro rfl; omega
  -- step 2: n + u + v = 4Cuv
  have key : n + u + v = 4 * C * u * v := by
    have h1 : (4 * C) * (n + u + v) = (4 * C) * (4 * C * u * v) := by
      have e : (a + 1) * (b + 1) + 1 = a * b + (a + 1) + (b + 1) := by ring
      rw [hu, hv, ← hab] at e
      zify at e ⊢
      linear_combination -e
    exact Nat.eq_of_mul_eq_mul_left (by omega) h1
  have hn0 : n ≠ 0 := by
    rintro rfl
    have : 1 ≤ C := Nat.one_le_iff_ne_zero.mpr hC
    have : 1 ≤ u := Nat.one_le_iff_ne_zero.mpr hu0
    have : 1 ≤ v := Nat.one_le_iff_ne_zero.mpr hv0
    nlinarith [Nat.mul_le_mul this this]
  refine ⟨C * u * v, n * C * v, n * C * u, by positivity, by positivity, by positivity, ?_⟩
  -- step 4
  calc 4 * (C * u * v) * (n * C * v) * (n * C * u)
      = n * C ^ 2 * u * v * n * (4 * C * u * v) := by ring
    _ = n * C ^ 2 * u * v * n * (n + u + v) := by rw [key]
    _ = n * (C * u * v * (n * C * v) + n * C * v * (n * C * u) + n * C * u * (C * u * v)) := by ring

/-- The same, as the rational identity `4/n = 1/x + 1/y + 1/z`. -/
theorem cform_ES_rat {n C a : ℕ} (h : CForm n C a) :
    0 < n ∧ ∃ x y z : ℕ, 0 < x ∧ 0 < y ∧ 0 < z ∧ (4 : ℚ) / n = 1 / x + 1 / y + 1 / z := by
  have hn : 0 < n := by
    obtain ⟨x, y, z, hx, hy, hz, e⟩ := cform_ES h
    rcases Nat.eq_zero_or_pos n with rfl | hn
    · simp at e; omega
    · exact hn
  exact ⟨hn, (ESProp_iff_rat n hn).mp (cform_ES h)⟩

/-- A C-form certificate for `n` forces `4C ≤ n + 2` (`BRAINSTORM/z45_euler_systems.md:126`, Lemma 3.1),
so for each `n` only finitely many `C` (and divisors `a`) need checking. -/
theorem cform_C_bound {n C a : ℕ} (h : CForm n C a) : 4 * C ≤ n + 2 := by
  obtain ⟨⟨b, hab⟩, ha⟩ := h
  have hb := cofactor_dvd hab ha
  obtain ⟨u, hu⟩ := ha
  obtain ⟨v, hv⟩ := hb
  have hC : C ≠ 0 := by rintro rfl; omega
  have hu1 : 1 ≤ u := Nat.one_le_iff_ne_zero.mpr (by rintro rfl; omega)
  have hv1 : 1 ≤ v := Nat.one_le_iff_ne_zero.mpr (by rintro rfl; omega)
  have key : n + u + v = 4 * C * u * v := by
    have h1 : (4 * C) * (n + u + v) = (4 * C) * (4 * C * u * v) := by
      have e : (a + 1) * (b + 1) + 1 = a * b + (a + 1) + (b + 1) := by ring
      rw [hu, hv, ← hab] at e
      zify at e ⊢
      linear_combination -e
    exact Nat.eq_of_mul_eq_mul_left (by omega) h1
  -- 4Cuv − u − v ≥ 4C − 2 for u, v ≥ 1, C ≥ 1
  have hC1 : 1 ≤ C := Nat.one_le_iff_ne_zero.mpr hC
  nlinarith [Nat.mul_le_mul hu1 hv1, Nat.mul_le_mul (Nat.mul_le_mul hC1 hu1) hv1]

/-! ### Part (b): the Jacobi-symbol obstruction T1 -/

/-- **Lemma A.** If `4C ∣ a + 1` then `J(C | a) = 1`. -/
theorem jacobi_C_of_dvd_succ {C a : ℕ} (h : 4 * C ∣ a + 1) : jacobiSym C a = 1 := by
  -- step 1
  have hC : C ≠ 0 := by rintro rfl; simp at h
  have ha4 : a % 4 = 3 := by have := (dvd_mul_right 4 C).trans h; omega
  have hao : Odd a := Nat.odd_iff.mpr (by omega)
  -- step 2
  obtain ⟨k, C', hC'o, rfl⟩ := Nat.exists_eq_two_pow_mul_odd hC
  have hsplit : jacobiSym ((2 ^ k * C' : ℕ) : ℤ) a = jacobiSym 2 a ^ k * jacobiSym C' a := by
    push_cast; rw [jacobiSym.mul_left, jacobiSym.pow_left]
  rw [hsplit]
  -- step 3
  have h2 : jacobiSym 2 a ^ k = 1 := by
    rcases Nat.eq_zero_or_pos k with rfl | hk
    · simp
    · have h8 : 8 ∣ a + 1 := by
        have : 8 ∣ 4 * (2 ^ k * C') := by
          obtain ⟨j, rfl⟩ : ∃ j, k = j + 1 := ⟨k - 1, by omega⟩
          exact ⟨2 ^ j * C', by ring⟩
        exact this.trans h
      have ha8 : a % 8 = 7 := by omega
      have ha2 : a % 2 = 1 := by omega
      rw [jacobiSym.at_two hao, ZMod.χ₈_nat_eq_if_mod_eight]
      simp [ha8, ha2]
  -- steps 4–6
  have hC'4 : C' ∣ 4 * (2 ^ k * C') := ⟨4 * 2 ^ k, by ring⟩
  have hC'dvd : C' ∣ a + 1 := hC'4.trans h
  have hsign : qrSign a C' = jacobiSym (-1) C' := by
    rw [qrSign, ZMod.χ₄_nat_three_mod_four ha4]
  have hmod : jacobiSym a C' = jacobiSym (-1) C' := by
    apply jacobiSym.mod_left'
    have : ((a : ℤ)) ≡ -1 [ZMOD C'] := by
      apply Int.modEq_iff_dvd.mpr
      have : (C' : ℤ) ∣ (a + 1 : ℕ) := Int.natCast_dvd_natCast.mpr hC'dvd
      have e : (-1 : ℤ) - a = -((a + 1 : ℕ) : ℤ) := by push_cast; ring
      rw [e]; exact this.neg_right
    exact this
  rw [h2, one_mul, jacobiSym.quadratic_reciprocity' hC'o hao, hsign, hmod, ← sq]
  exact jacobiSym.sq_one (by simp)

/-- `a ≡ 3 (mod 4)` whenever `4C ∣ a + 1`. -/
theorem mod_four_of_dvd_succ {C a : ℕ} (h : 4 * C ∣ a + 1) : a % 4 = 3 := by
  have := (dvd_mul_right 4 C).trans h; omega

/-- **Lemma B (QNR lemma).** Every C-form divisor `a` of `4Cn + 1` has `J(n | a) = −1`
(`BRAINSTORM/z52b_free_fable.md:489`). -/
theorem jacobi_n_of_cform {n C a : ℕ} (h : CForm n C a) : jacobiSym n a = -1 := by
  obtain ⟨hdiv, h4⟩ := h
  -- step 1
  have ha4 := mod_four_of_dvd_succ h4
  have hao : Odd a := Nat.odd_iff.mpr (by omega)
  have hneg : jacobiSym (-1) a = -1 := by
    rw [jacobiSym.at_neg_one hao, ZMod.χ₄_nat_three_mod_four ha4]
  -- step 2
  have hcong : jacobiSym ((4 * C * n : ℕ) : ℤ) a = jacobiSym (-1) a := by
    apply jacobiSym.mod_left'
    have : ((4 * C * n : ℕ) : ℤ) ≡ -1 [ZMOD a] := by
      apply Int.modEq_iff_dvd.mpr
      have : (a : ℤ) ∣ (4 * C * n + 1 : ℕ) := Int.natCast_dvd_natCast.mpr hdiv
      have e : (-1 : ℤ) - ((4 * C * n : ℕ) : ℤ) = -((4 * C * n + 1 : ℕ) : ℤ) := by push_cast; ring
      rw [e]; exact this.neg_right
    exact this
  -- step 3
  have hsplit : jacobiSym ((4 * C * n : ℕ) : ℤ) a = jacobiSym (2 ^ 2) a * jacobiSym C a * jacobiSym n a := by
    rw [show ((4 * C * n : ℕ) : ℤ) = 2 ^ 2 * C * n by push_cast; ring, jacobiSym.mul_left,
      jacobiSym.mul_left]
  have h22 : jacobiSym (2 ^ 2) a = 1 := by
    apply jacobiSym.sq_one'
    have : Nat.gcd 2 a = 1 := (Nat.coprime_two_left).mpr hao
    exact_mod_cast this
  rw [hsplit, h22, jacobi_C_of_dvd_succ h4, hneg] at hcong
  simpa using hcong

/-- A Jacobi symbol at a square top is never `−1`. -/
theorem jacobi_sq_ne_neg_one (m : ℤ) (b : ℕ) : jacobiSym (m ^ 2) b ≠ -1 := by
  rw [jacobiSym.pow_left]
  rcases jacobiSym.trichotomy m b with h | h | h <;> rw [h] <;> norm_num

/-- **T1 for the C-form.** No square `n = m²` (odd or even) has a C-form certificate, for any `C`. -/
theorem no_cform_square (m C a : ℕ) : ¬ CForm (m ^ 2) C a := by
  intro h
  have := jacobi_n_of_cform h
  push_cast at this
  exact jacobi_sq_ne_neg_one m a this

/-- **T1, shifted form** (`FRONTIER.md:241`, `PARITY_AUDIT.md:214` Lemma 3.2): for every `u`, `m² + u` has no
divisor `f ≡ −1 (mod 4u)`. -/
theorem no_shifted_square (m u f : ℕ) : ¬ (f ∣ m ^ 2 + u ∧ 4 * u ∣ f + 1) := by
  rintro ⟨hdiv, h4⟩
  have hf4 := mod_four_of_dvd_succ h4
  have hfo : Odd f := Nat.odd_iff.mpr (by omega)
  have hcong : jacobiSym ((m : ℤ) ^ 2) f = jacobiSym (-1 * u) f := by
    apply jacobiSym.mod_left'
    have : ((m : ℤ) ^ 2) ≡ -1 * u [ZMOD f] := by
      apply Int.modEq_iff_dvd.mpr
      have : (f : ℤ) ∣ (m ^ 2 + u : ℕ) := Int.natCast_dvd_natCast.mpr hdiv
      have e : (-1 * u : ℤ) - (m : ℤ) ^ 2 = -((m ^ 2 + u : ℕ) : ℤ) := by push_cast; ring
      rw [e]; exact this.neg_right
    exact this
  rw [jacobiSym.mul_left, jacobiSym.at_neg_one hfo, ZMod.χ₄_nat_three_mod_four hf4,
    jacobi_C_of_dvd_succ h4] at hcong
  exact jacobi_sq_ne_neg_one m f (by simpa using hcong)

/-- QNR lemma, reciprocal form: for `n ≡ 1 (mod 4)` every C-form divisor `a` has `J(a | n) = −1`
(for prime `n = p`: `a` is a quadratic non-residue mod `p`). -/
theorem jacobi_a_of_cform {n C a : ℕ} (hn : n % 4 = 1) (h : CForm n C a) : jacobiSym a n = -1 := by
  have hao : Odd a := Nat.odd_iff.mpr (by have := mod_four_of_dvd_succ h.2; omega)
  rw [← jacobiSym.quadratic_reciprocity_one_mod_four hn hao]
  exact jacobi_n_of_cform h

/-! ### C-form ⟺ shifted form -/

/-- The C-form and the shifted ("p + u has a divisor ≡ −1 (mod 4u)") form are equivalent, for `n ≥ 1`
(`BRAINSTORM/z52b_free_fable.md:36`). -/
theorem cform_iff_shifted (n : ℕ) (hn : 0 < n) :
    (∃ C a, CForm n C a) ↔ ∃ u f, f ∣ n + u ∧ 4 * u ∣ f + 1 := by
  constructor
  · rintro ⟨C, a, ⟨b, hab⟩, ha⟩
    have hb := cofactor_dvd hab ha
    obtain ⟨u, hu⟩ := ha
    obtain ⟨v, hv⟩ := hb
    have hC : C ≠ 0 := by rintro rfl; omega
    have key : n + u + v = 4 * C * u * v := by
      have h1 : (4 * C) * (n + u + v) = (4 * C) * (4 * C * u * v) := by
        have e : (a + 1) * (b + 1) + 1 = a * b + (a + 1) + (b + 1) := by ring
        rw [hu, hv, ← hab] at e
        zify at e ⊢
        linear_combination -e
      exact Nat.eq_of_mul_eq_mul_left (by omega) h1
    -- n + u = v * a, and a + 1 = 4uC
    refine ⟨u, a, ⟨v, ?_⟩, ⟨C, by rw [hu]; ring⟩⟩
    zify at key hu ⊢
    linear_combination key - v * hu
  · rintro ⟨u, f, ⟨v, hv⟩, ⟨C, hC⟩⟩
    -- 4Cn + 1 = f (4Cv − 1)
    refine ⟨C, f, ⟨4 * C * v - 1, ?_⟩, ⟨u, by rw [hC]; ring⟩⟩
    have hC0 : C ≠ 0 := by rintro rfl; simp at hC
    have hv1 : v ≠ 0 := by rintro rfl; simp at hv; omega
    have hv0 : 1 ≤ 4 * C * v := Nat.one_le_iff_ne_zero.mpr (by positivity)
    zify [hv0]
    zify at hv hC
    linear_combination (4 * C : ℤ) * hv + hC

/-! ### Extension: T1 for the full Type II and Type I divisor forms (`FRONTIER.md:44`)

Paper proofs.
* Type II: f ∣ 4c²d·m² + 1, 4cd ∣ f + 1. Then 4c²dm² ≡ −1 (mod f), so
  −1 = J(−1 | f) = J((2cm)²·d | f) = J(2cm | f)² · J(d | f) = J(2cm | f)² ∈ {0, 1}  (Lemma A with C = d).
* Type I: f ∣ m⁴ + 4c²d, 4cd ∣ f + m², gcd(f, m) = 1. Then m and f are odd (4 ∣ f + m²).
  (i) f ≡ m²(4d − 1) (mod 4d) and J(−d | ·) is 4d-periodic on odd numbers (`jacobiSym.mod_right`), so
      J(−d | f) = J(−d | m²(4d−1)) = J(−d | m)² · J(−1 | 4d−1) · J(d | 4d−1) = −J(−d | m)² ∈ {0, −1}.
  (ii) m⁴ ≡ −d·(2c)² (mod f), so 1 = J(m | f)⁴ = J(−d | f) · J(2c | f)², forcing J(−d | f) = 1. Contradiction.
  Without gcd(f, m) = 1 the statement is false, even for odd m (m = 3, c = 1, d = 3, f = 3: 3 ∣ 93, 12 ∣ 3 + 9;
  also m = 2, c = d = 1, f = 4); this matches the
  R290 repair at `FRONTIER.md:42` (Type I/II for composite n need coprimality).
The equivalence of these divisor forms with Elsholtz–Tao Type I/II solutions is NOT formalised here. -/

/-- **T1 for the Type II divisor form** (`FRONTIER.md:44`, generalising `no_cform_square`, which is `c = 1`):
no `f ≡ −1 (mod 4cd)` divides `4c²d·m² + 1`. -/
theorem no_typeII_square (m c d f : ℕ) : ¬ (f ∣ 4 * c ^ 2 * d * m ^ 2 + 1 ∧ 4 * c * d ∣ f + 1) := by
  rintro ⟨hdiv, h4⟩
  have hf4 := mod_four_of_dvd_succ (C := c * d) (by rw [← mul_assoc]; exact h4)
  have hfo : Odd f := Nat.odd_iff.mpr (by omega)
  have hd : jacobiSym d f = 1 := jacobi_C_of_dvd_succ (dvd_trans (⟨c, by ring⟩ : 4 * d ∣ 4 * c * d) h4)
  have hcong : jacobiSym (((2 * c * m : ℕ) : ℤ) ^ 2 * d) f = jacobiSym (-1) f := by
    apply jacobiSym.mod_left'
    have : (((2 * c * m : ℕ) : ℤ) ^ 2 * d) ≡ -1 [ZMOD f] := by
      apply Int.modEq_iff_dvd.mpr
      have : (f : ℤ) ∣ (4 * c ^ 2 * d * m ^ 2 + 1 : ℕ) := Int.natCast_dvd_natCast.mpr hdiv
      have e : (-1 : ℤ) - ((2 * c * m : ℕ) : ℤ) ^ 2 * d = -((4 * c ^ 2 * d * m ^ 2 + 1 : ℕ) : ℤ) := by
        push_cast; ring
      rw [e]; exact this.neg_right
    exact this
  rw [jacobiSym.mul_left, hd, mul_one, jacobiSym.at_neg_one hfo, ZMod.χ₄_nat_three_mod_four hf4] at hcong
  exact jacobi_sq_ne_neg_one _ f hcong

/-- **T1 for the Type I divisor form** (`FRONTIER.md:44`), at squares, under `gcd(f, m) = 1`:
no `f ≡ −m² (mod 4cd)` coprime to `m` divides `m⁴ + 4c²d`. -/
theorem no_typeI_square (m c d f : ℕ) (hcop : Nat.Coprime f m) :
    ¬ (f ∣ (m ^ 2) ^ 2 + 4 * c ^ 2 * d ∧ 4 * c * d ∣ f + m ^ 2) := by
  rintro ⟨hdiv, h4⟩
  -- parity
  have h4' : 4 ∣ f + m ^ 2 := dvd_trans (⟨c * d, by ring⟩ : 4 ∣ 4 * c * d) h4
  have hmo : Odd m := by
    rcases Nat.even_or_odd m with he | ho
    · exfalso
      have hf2 : 2 ∣ f := by
        have h2m : 2 ∣ m ^ 2 := (even_iff_two_dvd.mp he).trans (Dvd.intro_left _ (by ring))
        exact (Nat.dvd_add_left h2m).mp (dvd_trans (⟨2, by ring⟩ : 2 ∣ 4) h4')
      have := Nat.dvd_gcd hf2 (even_iff_two_dvd.mp he)
      rw [hcop] at this; omega
    · exact ho
  have hfo : Odd f := by
    rcases Nat.even_or_odd f with he | ho
    · exfalso
      have h2 : 2 ∣ m ^ 2 := (Nat.dvd_add_right (even_iff_two_dvd.mp he)).mp
        (dvd_trans (⟨2, by ring⟩ : 2 ∣ 4) h4')
      have : ¬ 2 ∣ m ^ 2 := by rw [← even_iff_two_dvd]; exact Nat.not_even_iff_odd.mpr (hmo.pow)
      exact this h2
    · exact ho
  have hd0 : d ≠ 0 := by
    have := hfo.pos
    rintro rfl; simp at h4; omega
  -- (ii): J(−d | f) = 1
  have hJm : jacobiSym m f ^ 4 = 1 := by
    have h2 : jacobiSym m f ^ 2 = 1 := jacobiSym.sq_one (by
      rw [Int.gcd_natCast_natCast]; exact hcop.symm)
    calc jacobiSym m f ^ 4 = (jacobiSym m f ^ 2) ^ 2 := by ring
      _ = 1 := by rw [h2]; norm_num
  have hcong : jacobiSym ((m : ℤ) ^ 4) f = jacobiSym (-(d : ℤ) * ((2 * c : ℕ) : ℤ) ^ 2) f := by
    apply jacobiSym.mod_left'
    have : ((m : ℤ) ^ 4) ≡ -(d : ℤ) * ((2 * c : ℕ) : ℤ) ^ 2 [ZMOD f] := by
      apply Int.modEq_iff_dvd.mpr
      have : (f : ℤ) ∣ ((m ^ 2) ^ 2 + 4 * c ^ 2 * d : ℕ) := Int.natCast_dvd_natCast.mpr hdiv
      have e : -(d : ℤ) * ((2 * c : ℕ) : ℤ) ^ 2 - (m : ℤ) ^ 4 = -(((m ^ 2) ^ 2 + 4 * c ^ 2 * d : ℕ) : ℤ) := by
        push_cast; ring
      rw [e]; exact this.neg_right
    exact this
  rw [jacobiSym.pow_left, hJm, jacobiSym.mul_left, jacobiSym.pow_left] at hcong
  have hii : jacobiSym (-(d : ℤ)) f = 1 := by
    rcases jacobiSym.trichotomy (-(d : ℤ)) f with h | h | h <;>
      rcases jacobiSym.trichotomy ((2 * c : ℕ) : ℤ) f with h' | h' | h' <;>
      rw [h, h'] at hcong <;> norm_num at hcong <;> exact h
  -- (i): J(−d | f) = −J(−d | m)²
  have hg : f % (4 * d) = (m ^ 2 * (4 * d - 1)) % (4 * d) := by
    have h4d : 4 * d ∣ f + m ^ 2 := dvd_trans (⟨c, by ring⟩ : 4 * d ∣ 4 * c * d) h4
    have hd1 : 1 ≤ 4 * d := by omega
    have e : m ^ 2 * (4 * d - 1) + m ^ 2 = 4 * d * m ^ 2 := by
      rw [Nat.mul_sub, mul_one, Nat.sub_add_cancel (Nat.le_mul_of_pos_right _ (by omega))]; ring
    have h1 : f ≡ m ^ 2 * (4 * d - 1) [MOD 4 * d] := by
      apply Nat.ModEq.add_right_cancel' (m ^ 2)
      rw [e]
      exact (Nat.modEq_zero_iff_dvd.mpr h4d).trans (Nat.modEq_zero_iff_dvd.mpr ⟨m ^ 2, rfl⟩).symm
    exact h1
  have hgo : Odd (m ^ 2 * (4 * d - 1)) := hmo.pow.mul (Nat.odd_iff.mpr (by omega))
  have hJf : jacobiSym (-(d : ℤ)) f = jacobiSym (-(d : ℤ)) (m ^ 2 * (4 * d - 1)) := by
    rw [jacobiSym.mod_right _ hfo, jacobiSym.mod_right _ hgo]
    simp only [Int.natAbs_neg, Int.natAbs_natCast]
    rw [hg]
  have hm0 : NeZero (m ^ 2) := ⟨by have := hmo.pos; positivity⟩
  have hq0 : NeZero (4 * d - 1) := ⟨by omega⟩
  have hq : jacobiSym (-(d : ℤ)) (4 * d - 1) = -1 := by
    have hqo : Odd (4 * d - 1) := Nat.odd_iff.mpr (by omega)
    have hq4 : (4 * d - 1) % 4 = 3 := by omega
    rw [neg_eq_neg_one_mul, jacobiSym.mul_left, jacobiSym.at_neg_one hqo,
      ZMod.χ₄_nat_three_mod_four hq4, jacobi_C_of_dvd_succ (by rw [Nat.sub_add_cancel (by omega)])]
    norm_num
  rw [jacobiSym.mul_right, jacobiSym.pow_right, hq, hii] at hJf
  rcases jacobiSym.trichotomy (-(d : ℤ)) m with h | h | h <;> rw [h] at hJf <;> norm_num at hJf

/-! ### Optional: the standard reduction of ES to primes `p ≡ 1 (mod 4)` -/

/-- ES is inherited by multiples: a solution for `n` scales to one for `k * n`. -/
theorem ESProp_mul {n : ℕ} (k : ℕ) (hk : 0 < k) (h : ESProp n) : ESProp (k * n) := by
  obtain ⟨x, y, z, hx, hy, hz, e⟩ := h
  refine ⟨k * x, k * y, k * z, by positivity, by positivity, by positivity, ?_⟩
  calc 4 * (k * x) * (k * y) * (k * z) = k ^ 3 * (4 * x * y * z) := by ring
    _ = k ^ 3 * (n * (x * y + y * z + z * x)) := by rw [e]
    _ = _ := by ring

theorem ESProp_two : ESProp 2 := ⟨1, 2, 2, by norm_num, by norm_num, by norm_num, by norm_num⟩

/-- `n ≡ 3 (mod 4)`: `4/n = 1/(t+1) + 1/(2n(t+1)) + 1/(2n(t+1))`, `n = 4t + 3`. -/
theorem ESProp_three_mod_four {n : ℕ} (h : n % 4 = 3) : ESProp n := by
  obtain ⟨t, rfl⟩ : ∃ t, n = 4 * t + 3 := ⟨n / 4, by omega⟩
  refine ⟨t + 1, 2 * (4 * t + 3) * (t + 1), 2 * (4 * t + 3) * (t + 1),
    by positivity, by positivity, by positivity, ?_⟩
  ring

/-- **Reduction.** ES for every prime `p ≡ 1 (mod 4)` implies the full Erdős–Straus conjecture. -/
theorem ES_of_primes_one_mod_four (h : ∀ p, p.Prime → p % 4 = 1 → ESProp p) : ErdosStraus := by
  intro n hn
  have hp := Nat.minFac_prime (show n ≠ 1 by omega)
  obtain ⟨k, hk⟩ := Nat.minFac_dvd n
  have hk0 : 0 < k := by
    rcases Nat.eq_zero_or_pos k with rfl | hk0
    · omega
    · exact hk0
  rw [hk, mul_comm]
  apply ESProp_mul k hk0
  rcases hp.eq_two_or_odd with h2 | hodd
  · rw [h2]; exact ESProp_two
  · have : n.minFac % 4 = 1 ∨ n.minFac % 4 = 3 := by omega
    rcases this with h1 | h3
    · exact h _ hp h1
    · exact ESProp_three_mod_four h3

/-- C-form at every prime `p ≡ 1 (mod 4)` would imply ES. **VACUOUS: the hypothesis is FALSE.** By
`cform_C_bound` a certificate for p needs C ≤ (p+2)/4, and the exhaustive search over that range finds none for
p = 409 (`BRAINSTORM/z45_euler_systems.md:126,170–183`; also `BRAINSTORM/z52b_free_fable.md:485`). The search is a
computation and is not formalised here. Kept only as a formal record; the useful reduction is `ES_of_primes_one_mod_four`. -/
theorem ES_of_cform_primes (h : ∀ p, p.Prime → p % 4 = 1 → ∃ C a, CForm p C a) : ErdosStraus :=
  ES_of_primes_one_mod_four fun p hp hp4 => by
    obtain ⟨C, a, hc⟩ := h p hp hp4
    exact cform_ES hc

end ES
