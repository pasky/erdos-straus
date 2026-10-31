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
2. (a + 1)(b + 1) = ab + (a + 1) + (b + 1) gives 4C · 4Cuv = 4C (n + u + v), so n + u + v = 4Cuv (C ≠ 0).
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

end ES
