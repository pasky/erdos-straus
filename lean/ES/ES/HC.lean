import ES.Basic

/-!
# Coordinate-form certificates, the statistic HC, Theorem Q and the HC ≤ 8 words (wave z56, lane LEAN)

**ES is OPEN.** Nothing here proves it. This file formalises four elementary repo statements:

* (a) `LOWERTAIL_ROUND2_FABLE.md` §1.1 Theorem 1 (both directions of the 2-adic equivalence "slot ⟺ coordinate
  in 𝒞_n", no coprimality) together with the five slot formulas (explicit 4/n identities), hence
  "coordinate-form certificate ⟹ ES"; and `Z53_UPPER.md` Lemma 1.1 lines (U) and (T) (a coordinate c of a word ⟺
  a divisor ≡ −1 (mod c) of n + c, resp. of cn + 1).
* (b) `Z54_HCKILL.md` §2.1 Theorem Q: if 4 ∣ m and p = 5m² + 1 is prime, then p ≡ 1 (8), 12 ∣ m and HC(p) ≥ 7.
* (c) `Z54_HCKILL.md` §1 Lemma 1.1: for n ≡ 1 (8), HC(n) > 4 ⟺ n + 4 ∈ S and 4n + 1 ∈ S
  (S = positive integers all of whose prime factors are ≡ 1 (mod 4)). Primality of n is not needed.
* (d) `Z54_UPPER2.md` §3 Proposition 3.1 (a)–(c): HC(p) = 3 for p ≡ 5 (8); the six explicit words for p ≡ 1 (8);
  HC(p) ≤ 8 for primes p > 7, p ≡ 1 (8), p ≢ 1, 121, 169, 289, 361, 529 (mod 840).

## Definitions (Lean ↔ paper)

* `Word n t u v`: t, u, v ≥ 1 and tuv = n + u + v (i.e. tuv − u − v = n). A = tu − 1, A* = tv − 1.
* `InC n x`: x ∈ 𝒞_n, i.e. 4 ∣ x or x ≡ −n (mod 8) (FABLE §1.1; for n ≡ 1 (8) this is 4ℕ ∪ (8ℕ + 7)).
* `Slot t u v`: 4 divides one of t, u, v, tu − 1, tv − 1 (the five slots).
* `IsCoord n x`: x is a coordinate (t, u or v) of some word of n.
* `HCle n X`: some x ≤ X lies in 𝒞_n and is a coordinate of a word of n, i.e. HC(n) ≤ X
  (FABLE §3.1: HC(n) = least coordinate in 𝒞_n of any word). So "HC(n) > X" is `¬ HCle n X` and
  "HC(n) = X" is `HCle n X ∧ ¬ HCle n (X - 1)`.
* `S N`: N > 0 and every prime factor of N is ≡ 1 (mod 4).

## Paper proofs, in the order the Lean proofs follow

**Word identities.** For a word, tu ≥ 1, tv ≥ 1; put A + 1 = tu, B + 1 = tv. Then A·v = n + u
(since tuv − v = n + u) and A·B = tn + 1 (since (A+1)(B+1) = t·tuv = t(n + u + v) = tn + (A+1) + (B+1)).
A, B ≥ 1 when n ≥ 1 (A = 0 would give 0 = n + u).

**Five slot formulas (`ES_of_slot`).** n ≥ 1.
1. t = 4s: (x, y, z) = (suv, nsu, nsv): 4xyz − n(xy+yz+zx) = n²s²uv(4suv − n − u − v) = 0.
2. v = 4w: (wA, nwt, nwtA): 4xyz − n(…) = n²w²tA(4wtA − 1 − nt − A) = n²w²tA(t(4wA − n − u) + (tu − A − 1)) = 0.
3. u = 4w: case 2 for the word (t, v, u).
4. A = 4a: (av, avB, naB): 4xyz − n(…) = na²vB(4avB − v − nB − n) = na²vB(v(4aB − tn − 1) + n(tv − B − 1)) = 0.
5. B = 4a: case 4 for the word (t, v, u).
All x, y, z are positive (s, w, a ≥ 1 as t, u, v, A, B ≥ 1).

**Theorem 1 (`slot_iff_coord`).** Every quantity involved (n ≡ tuv − u − v, A, B, the slot and 𝒞 predicates)
depends only on t, u, v mod 8, and n mod 8 ∈ {1, 5}. So the equivalence is a finite check over (ℤ/8)³
(`core8`, by `decide`; FABLE's "160 admissible cells, 120 certificate cells, 0 mismatches"). The hand proof
(⇐): u ≡ −n (8) ⟹ 8 ∣ n + u = vA ⟹ 4 ∣ v or 4 ∣ A; t ≡ −n (8) ⟹ 8 ∣ tn + 1 = AB ⟹ 4 ∣ A or 4 ∣ B.

**Lines (U)/(T) (`coordU_iff`, `coordT_iff`).** (U): (t, c, v) is a word ⟺ (tc − 1)v = n + c; given d ∣ n + c with
c ∣ d + 1, take t = (d+1)/c, v = (n+c)/d. (T): (c, u, v) word ⟺ (cu − 1)(cv − 1) = cn + 1; given d ∣ cn + 1 with
d + 1 = cu, the cofactor e satisfies (d+1)e = cue and de = cn + 1, so e + 1 = c(ue − n) and v = (e+1)/c;
then c·(cuv) = (d+1)(e+1) = c(n + u + v).

**Divisors and S.** If every prime factor of N ≠ 0 is ≡ 1 (4), every divisor of N is ≡ 1 (4) (induction on
the factorisation of the divisor). An odd N has a divisor ≡ 3 (4) iff N ∉ S: (⇒) previous sentence; (⇐) a prime
factor q ≢ 1 (4) is odd, so q ≡ 3 (4).

**Lemma 1.1 (`HC_gt_four_iff`).** For n ≡ 1 (8): 𝒞_n ∩ [1, 4] = {4} and 0 is no coordinate, so HC(n) ≤ 4 ⟺ 4 is
a coordinate ⟺ (U)/(T) with c = 4 ⟺ n + 4 or 4n + 1 has a divisor ≡ 3 (4); both are odd; apply the previous lemma.

**Theorem Q (`theoremQ`).** m = 4k ⟹ p = 80k² + 1 ≡ 1 (8). If 3 ∤ m then m² ≡ 1 (3), so 3 ∣ p, p = 3, impossible.
p + 4 = 5(m² + 1), 4p + 1 = 5((2m)² + 1); every prime factor q of j² + 1 with j even is odd and has −1 a square
mod q, so q ≢ 3 (4) (mathlib `ZMod.mod_four_ne_three_of_sq_eq_neg_one`), i.e. q ≡ 1 (4); and S is
multiplicative and contains 5. By Lemma 1.1, HC(p) > 4; 𝒞_p ∩ [5, 6] = ∅, so HC(p) > 6.

**Prop 3.1.** Each word is checked by expanding tuv − u − v (linear in v once t, u are numerals), the stated
congruence giving integrality (`omega`). (c) is a CRT statement mod 840 (`omega`).
-/

namespace ESHC

open ES (ESProp)

/-- A word of `n`: positive `t, u, v` with `tuv − u − v = n`. -/
def Word (n t u v : ℕ) : Prop := 0 < t ∧ 0 < u ∧ 0 < v ∧ t * u * v = n + u + v

/-- `x ∈ 𝒞_n`: `x ≡ 0 (mod 4)` or `x ≡ −n (mod 8)`. -/
def InC (n x : ℕ) : Prop := 4 ∣ x ∨ (x + n) % 8 = 0

/-- The five slots of a word: `4` divides `t`, `u`, `v`, `A = tu − 1` or `A* = tv − 1`. -/
def Slot (t u v : ℕ) : Prop := 4 ∣ t ∨ 4 ∣ u ∨ 4 ∣ v ∨ 4 ∣ t * u - 1 ∨ 4 ∣ t * v - 1

/-- `x` is a coordinate (level `t` or endpoint `u`, `v`) of some word of `n`. -/
def IsCoord (n x : ℕ) : Prop := ∃ t u v, Word n t u v ∧ (t = x ∨ u = x ∨ v = x)

/-- `HC(n) ≤ X`: some `x ≤ X` in `𝒞_n` is a coordinate of a word of `n`. -/
def HCle (n X : ℕ) : Prop := ∃ x, x ≤ X ∧ InC n x ∧ IsCoord n x

/-- `S`: positive integers all of whose prime factors are `≡ 1 (mod 4)`. -/
def S (N : ℕ) : Prop := 0 < N ∧ ∀ q, q.Prime → q ∣ N → q % 4 = 1

/-- Line `x` fires: `n + x` or `xn + 1` has a divisor `≡ −1 (mod x)` (HCKILL §0, Z53_UPPER L1.1). -/
def Fires (n x : ℕ) : Prop := (∃ d, d ∣ n + x ∧ x ∣ d + 1) ∨ (∃ d, d ∣ x * n + 1 ∧ x ∣ d + 1)

/-! ### Word identities -/

theorem Word.symm {n t u v : ℕ} (h : Word n t u v) : Word n t v u := by
  obtain ⟨ht, hu, hv, e⟩ := h
  exact ⟨ht, hv, hu, by rw [mul_right_comm]; omega⟩

/-- `A := tu − 1` satisfies `A + 1 = tu` and `A·v = n + u`. -/
theorem Word.numer {n t u v : ℕ} (h : Word n t u v) : t * u = (t * u - 1) + 1 ∧ (t * u - 1) * v = n + u := by
  obtain ⟨ht, hu, hv, e⟩ := h
  have h1 : 1 ≤ t * u := Nat.one_le_iff_ne_zero.mpr (by positivity)
  refine ⟨by omega, ?_⟩
  rw [Nat.sub_mul, one_mul, e]; omega

/-- `A·A* = tn + 1`. -/
theorem Word.numer_mul {n t u v : ℕ} (h : Word n t u v) : (t * u - 1) * (t * v - 1) = t * n + 1 := by
  obtain ⟨hA1, -⟩ := h.numer
  obtain ⟨hB1, -⟩ := h.symm.numer
  obtain ⟨-, -, -, e⟩ := h
  set A := t * u - 1
  set B := t * v - 1
  have : (A + 1) * (B + 1) = t * (n + u + v) := by rw [← hA1, ← hB1, ← e]; ring
  zify at this hA1 hB1 ⊢
  linear_combination this + hA1 + hB1

theorem Word.numer_pos {n t u v : ℕ} (hn : 0 < n) (h : Word n t u v) : 0 < t * u - 1 := by
  obtain ⟨-, h2⟩ := h.numer
  rcases Nat.eq_zero_or_pos (t * u - 1) with h0 | h0
  · rw [h0] at h2; omega
  · exact h0

/-! ### (a) The five slot formulas: a slot gives an explicit `4/n` identity -/

theorem ES_of_four_dvd_t {n t u v : ℕ} (hw : Word n t u v) (ht : 4 ∣ t) (hn : 0 < n) : ESProp n := by
  obtain ⟨s, rfl⟩ := ht
  obtain ⟨ht0, hu, hv, e⟩ := hw
  have hs : 0 < s := by omega
  refine ⟨s * u * v, n * s * u, n * s * v, by positivity, by positivity, by positivity, ?_⟩
  zify at e ⊢
  linear_combination (n ^ 2 * s ^ 2 * u * v : ℤ) * e

theorem ES_of_four_dvd_v {n t u v : ℕ} (hw : Word n t u v) (hv4 : 4 ∣ v) (hn : 0 < n) : ESProp n := by
  have hA0 := hw.numer_pos hn
  obtain ⟨hA1, hAv⟩ := hw.numer
  obtain ⟨ht, hu, hv, -⟩ := hw
  set A := t * u - 1
  obtain ⟨w, rfl⟩ := hv4
  have hw0 : 0 < w := by omega
  refine ⟨w * A, n * w * t, n * w * t * A, by positivity, by positivity, by positivity, ?_⟩
  zify at hA1 hAv ⊢
  linear_combination (n ^ 2 * w ^ 2 * t ^ 2 * A : ℤ) * hAv + (n ^ 2 * w ^ 2 * t * A : ℤ) * hA1

theorem ES_of_four_dvd_numer {n t u v : ℕ} (hw : Word n t u v) (hA4 : 4 ∣ t * u - 1) (hn : 0 < n) :
    ESProp n := by
  have hA0 := hw.numer_pos hn
  have hB0 := hw.symm.numer_pos hn
  have hAB := hw.numer_mul
  obtain ⟨hB1, -⟩ := hw.symm.numer
  obtain ⟨ht, hu, hv, -⟩ := hw
  set A := t * u - 1
  set B := t * v - 1
  obtain ⟨a, ha⟩ := hA4
  rw [ha] at hAB hA0
  have ha0 : 0 < a := by omega
  refine ⟨a * v, a * v * B, n * a * B, by positivity, by positivity, by positivity, ?_⟩
  zify at hAB hB1 ⊢
  linear_combination (n * a ^ 2 * v ^ 2 * B : ℤ) * hAB + (n ^ 2 * a ^ 2 * v * B : ℤ) * hB1

/-- **Five slot formulas.** A word of `n ≥ 1` with a slot yields `ESProp n` explicitly. -/
theorem ES_of_slot {n t u v : ℕ} (hn : 0 < n) (hw : Word n t u v) (hs : Slot t u v) : ESProp n := by
  rcases hs with h | h | h | h | h
  · exact ES_of_four_dvd_t hw h hn
  · exact ES_of_four_dvd_v hw.symm h hn
  · exact ES_of_four_dvd_v hw h hn
  · exact ES_of_four_dvd_numer hw h hn
  · exact ES_of_four_dvd_numer hw.symm h hn

/-! ### (a) Theorem 1: slot ⟺ coordinate in `𝒞_n` (any `n ≡ 1 (mod 4)`, no coprimality) -/

/-- The finite 2-adic core of Theorem 1, over `(ℤ/8)³`. -/
theorem core8 : ∀ T U V : ZMod 8, (T * U * V - U - V = 1 ∨ T * U * V - U - V = 5) →
    (((T = 0 ∨ T = 4) ∨ (U = 0 ∨ U = 4) ∨ (V = 0 ∨ V = 4) ∨ (T * U - 1 = 0 ∨ T * U - 1 = 4) ∨
        (T * V - 1 = 0 ∨ T * V - 1 = 4)) ↔
      (((T = 0 ∨ T = 4) ∨ T + (T * U * V - U - V) = 0) ∨ ((U = 0 ∨ U = 4) ∨ U + (T * U * V - U - V) = 0) ∨
        ((V = 0 ∨ V = 4) ∨ V + (T * U * V - U - V) = 0))) := by
  decide

theorem four_dvd_iff_zmod (x : ℕ) : 4 ∣ x ↔ ((x : ZMod 8) = 0 ∨ (x : ZMod 8) = 4) := by
  rw [show (4 : ZMod 8) = ((4 : ℕ) : ZMod 8) by norm_num, show (0 : ZMod 8) = ((0 : ℕ) : ZMod 8) by norm_num,
    ZMod.natCast_eq_natCast_iff', ZMod.natCast_eq_natCast_iff']
  omega

theorem InC_iff_zmod (n x : ℕ) :
    InC n x ↔ (((x : ZMod 8) = 0 ∨ (x : ZMod 8) = 4) ∨ (x : ZMod 8) + n = 0) := by
  unfold InC
  rw [four_dvd_iff_zmod, ← Nat.cast_add, ZMod.natCast_eq_zero_iff (x + n) 8, Nat.dvd_iff_mod_eq_zero]

theorem mod4_iff_zmod (n : ℕ) : n % 4 = 1 ↔ ((n : ZMod 8) = 1 ∨ (n : ZMod 8) = 5) := by
  rw [show (1 : ZMod 8) = ((1 : ℕ) : ZMod 8) by norm_num, show (5 : ZMod 8) = ((5 : ℕ) : ZMod 8) by norm_num,
    ZMod.natCast_eq_natCast_iff', ZMod.natCast_eq_natCast_iff']
  omega

/-- **Theorem 1 (LOWERTAIL_ROUND2_FABLE §1.1), both directions, no coprimality.** For `n ≡ 1 (mod 4)` and a word
`(t, u, v)` of `n`: one of the five slots holds iff some coordinate lies in `𝒞_n`. -/
theorem slot_iff_coord {n t u v : ℕ} (hn : n % 4 = 1) (hw : Word n t u v) :
    Slot t u v ↔ (InC n t ∨ InC n u ∨ InC n v) := by
  have hA1 := hw.numer.1
  have hB1 := hw.symm.numer.1
  obtain ⟨ht, hu, hv, e⟩ := hw
  have hN : (n : ZMod 8) = (t : ZMod 8) * u * v - u - v := by
    have := congrArg (Nat.cast : ℕ → ZMod 8) e
    push_cast at this
    linear_combination -this
  have hA : ((t * u - 1 : ℕ) : ZMod 8) = (t : ZMod 8) * u - 1 := by
    rw [Nat.cast_sub (by omega), Nat.cast_mul, Nat.cast_one]
  have hB : ((t * v - 1 : ℕ) : ZMod 8) = (t : ZMod 8) * v - 1 := by
    rw [Nat.cast_sub (by omega), Nat.cast_mul, Nat.cast_one]
  rw [mod4_iff_zmod, hN] at hn
  unfold Slot
  rw [InC_iff_zmod, InC_iff_zmod, InC_iff_zmod, four_dvd_iff_zmod, four_dvd_iff_zmod, four_dvd_iff_zmod,
    four_dvd_iff_zmod, four_dvd_iff_zmod, hA, hB, hN]
  exact core8 _ _ _ hn

/-- **Coordinate-form certificate ⟹ ES.** For `n ≡ 1 (mod 4)`, a word with a coordinate in `𝒞_n`. -/
theorem ES_of_coord {n t u v : ℕ} (hn : n % 4 = 1) (hw : Word n t u v) (hc : InC n t ∨ InC n u ∨ InC n v) :
    ESProp n :=
  ES_of_slot (by omega) hw ((slot_iff_coord hn hw).mpr hc)

theorem ES_of_isCoord {n x : ℕ} (hn : n % 4 = 1) (hx : InC n x) (h : IsCoord n x) : ESProp n := by
  obtain ⟨t, u, v, hw, rfl | rfl | rfl⟩ := h
  · exact ES_of_coord hn hw (Or.inl hx)
  · exact ES_of_coord hn hw (Or.inr (Or.inl hx))
  · exact ES_of_coord hn hw (Or.inr (Or.inr hx))

/-- `HC(n) < ∞ ⟹ ES(n)` for `n ≡ 1 (mod 4)`. -/
theorem ES_of_HCle {n X : ℕ} (hn : n % 4 = 1) (h : HCle n X) : ESProp n := by
  obtain ⟨x, -, hx, hc⟩ := h
  exact ES_of_isCoord hn hx hc

/-! ### (a) Z53_UPPER Lemma 1.1: the coordinate lines (U) and (T) -/

/-- **Line (U).** `c` is the `u`-coordinate of a word of `n` iff `n + c` has a divisor `d ≡ −1 (mod c)`. -/
theorem coordU_iff (n c : ℕ) : (∃ t v, Word n t c v) ↔ ∃ d, d ∣ n + c ∧ c ∣ d + 1 := by
  constructor
  · rintro ⟨t, v, hw⟩
    obtain ⟨h1, h2⟩ := hw.numer
    exact ⟨t * c - 1, ⟨v, h2.symm⟩, ⟨t, by rw [← h1, mul_comm]⟩⟩
  · rintro ⟨d, ⟨v, hv⟩, ⟨t, ht⟩⟩
    have hc : 0 < c := by rcases Nat.eq_zero_or_pos c with rfl | h <;> simp_all
    have hv0 : 0 < v := by rcases Nat.eq_zero_or_pos v with rfl | h <;> simp_all
    have ht0 : 0 < t := by rcases Nat.eq_zero_or_pos t with rfl | h <;> simp_all
    refine ⟨t, v, ht0, hc, hv0, ?_⟩
    calc t * c * v = (d + 1) * v := by rw [ht, mul_comm c t]
      _ = n + c + v := by rw [add_mul, one_mul, ← hv]

/-- **Line (T).** `c` is the level of a word of `n` iff `cn + 1` has a divisor `d ≡ −1 (mod c)`. -/
theorem coordT_iff (n c : ℕ) : (∃ u v, Word n c u v) ↔ ∃ d, d ∣ c * n + 1 ∧ c ∣ d + 1 := by
  constructor
  · rintro ⟨u, v, hw⟩
    have h1 := hw.numer.1
    exact ⟨c * u - 1, ⟨c * v - 1, by rw [hw.numer_mul]⟩, ⟨u, h1.symm⟩⟩
  · rintro ⟨d, ⟨e, he⟩, ⟨u, hu⟩⟩
    have hc : 0 < c := by rcases Nat.eq_zero_or_pos c with rfl | h <;> simp_all
    -- `c ∣ e + 1`
    have key : c * n + (e + 1) = c * (u * e) := by
      calc c * n + (e + 1) = d * e + e := by rw [← he]; ring
        _ = c * (u * e) := by rw [← mul_assoc, ← hu]; ring
    obtain ⟨v, hv⟩ : c ∣ e + 1 := (Nat.dvd_add_right (dvd_mul_right _ _)).mp (key ▸ dvd_mul_right _ _)
    have hu0 : 0 < u := by rcases Nat.eq_zero_or_pos u with rfl | h <;> simp_all
    have hv0 : 0 < v := by rcases Nat.eq_zero_or_pos v with rfl | h <;> simp_all
    refine ⟨u, v, hc, hu0, hv0, ?_⟩
    have h2 : c * (c * u * v) = c * (n + u + v) := by
      have : (d + 1) * (e + 1) + 1 = d * e + (d + 1) + (e + 1) := by ring
      rw [hu, hv, ← he] at this
      zify at this ⊢
      linear_combination this
    exact Nat.eq_of_mul_eq_mul_left hc h2

/-- `x` is a coordinate of a word of `n` iff line `x` fires. -/
theorem isCoord_iff_fires (n x : ℕ) : IsCoord n x ↔ Fires n x := by
  unfold IsCoord Fires
  rw [← coordU_iff, ← coordT_iff]
  constructor
  · rintro ⟨t, u, v, hw, rfl | rfl | rfl⟩
    · exact Or.inr ⟨u, v, hw⟩
    · exact Or.inl ⟨t, v, hw⟩
    · exact Or.inl ⟨t, u, hw.symm⟩
  · rintro (⟨t, v, hw⟩ | ⟨u, v, hw⟩)
    · exact ⟨t, x, v, hw, Or.inr (Or.inl rfl)⟩
    · exact ⟨x, u, v, hw, Or.inl rfl⟩

/-- **Line form of the certificate ⟹ ES** (U): `c ∈ 𝒞_n`, `d ∣ n + c`, `d ≡ −1 (mod c)`. -/
theorem ES_of_lineU {n c d : ℕ} (hn : n % 4 = 1) (hc : InC n c) (hd : d ∣ n + c) (hdc : c ∣ d + 1) :
    ESProp n := by
  obtain ⟨t, v, hw⟩ := (coordU_iff n c).mpr ⟨d, hd, hdc⟩
  exact ES_of_coord hn hw (Or.inr (Or.inl hc))

/-- **Line form of the certificate ⟹ ES** (T): `c ∈ 𝒞_n`, `d ∣ cn + 1`, `d ≡ −1 (mod c)`. -/
theorem ES_of_lineT {n c d : ℕ} (hn : n % 4 = 1) (hc : InC n c) (hd : d ∣ c * n + 1) (hdc : c ∣ d + 1) :
    ESProp n := by
  obtain ⟨u, v, hw⟩ := (coordT_iff n c).mpr ⟨d, hd, hdc⟩
  exact ES_of_coord hn hw (Or.inl hc)

/-! ### Divisors ≡ 3 (mod 4) and the set `S` -/

/-- If every prime factor of `N ≠ 0` is `≡ 1 (mod 4)`, so is every divisor. -/
theorem dvd_mod_four_of_S {N : ℕ} (hS : S N) : ∀ d, d ∣ N → d % 4 = 1 := by
  intro d
  induction d using Nat.recOnMul with
  | zero => intro h; have := Nat.eq_zero_of_zero_dvd h; have := hS.1; omega
  | one => intro _; rfl
  | prime q hq => exact hS.2 q hq
  | mul a b iha ihb =>
    intro h
    have ha := iha (dvd_trans (dvd_mul_right a b) h)
    have hb := ihb (dvd_trans (dvd_mul_left b a) h)
    rw [Nat.mul_mod, ha, hb]

/-- An odd `N` has a divisor `≡ 3 (mod 4)` iff `N ∉ S`. -/
theorem exists_dvd_three_iff {N : ℕ} (hN : N % 2 = 1) : (∃ d, d ∣ N ∧ d % 4 = 3) ↔ ¬ S N := by
  constructor
  · rintro ⟨d, hd, h3⟩ hS
    have := dvd_mod_four_of_S hS d hd
    omega
  · intro hS
    have hN0 : 0 < N := by omega
    have : ∃ q, q.Prime ∧ q ∣ N ∧ q % 4 ≠ 1 := by
      by_contra hc
      push Not at hc
      exact hS ⟨hN0, hc⟩
    obtain ⟨q, hq, hqN, hq1⟩ := this
    refine ⟨q, hqN, ?_⟩
    rcases hq.eq_two_or_odd with rfl | hodd
    · omega
    · omega

theorem S_mul {a b : ℕ} (ha : S a) (hb : S b) : S (a * b) := by
  refine ⟨Nat.mul_pos ha.1 hb.1, fun q hq hd => ?_⟩
  rcases (Nat.Prime.dvd_mul hq).mp hd with h | h
  · exact ha.2 q hq h
  · exact hb.2 q hq h

theorem S_five : S 5 := by
  refine ⟨by norm_num, fun q hq hd => ?_⟩
  rw [(Nat.prime_dvd_prime_iff_eq hq (by norm_num)).mp hd]

/-- `j² + 1 ∈ S` for even `j` (sum of two coprime squares, odd). -/
theorem S_sq_add_one {j : ℕ} (hj : 2 ∣ j) : S (j ^ 2 + 1) := by
  refine ⟨by positivity, fun q hq hd => ?_⟩
  have := Fact.mk hq
  have h3 : q % 4 ≠ 3 := by
    apply ZMod.mod_four_ne_three_of_sq_eq_neg_one (y := (j : ZMod q))
    have : ((j ^ 2 + 1 : ℕ) : ZMod q) = 0 := (ZMod.natCast_eq_zero_iff _ _).mpr hd
    push_cast at this
    linear_combination this
  rcases hq.eq_two_or_odd with rfl | hodd
  · exfalso
    obtain ⟨k, rfl⟩ := hj
    have : (2 * k) ^ 2 + 1 = 2 * (2 * k ^ 2) + 1 := by ring
    omega
  · omega

/-! ### (c) HCKILL Lemma 1.1 and small values of HC -/

theorem not_isCoord_zero (n : ℕ) : ¬ IsCoord n 0 := by
  rintro ⟨t, u, v, ⟨ht, hu, hv, -⟩, rfl | rfl | rfl⟩ <;> omega

/-- For `n ≡ 1 (mod 8)`, `𝒞_n ∩ [1, 6] = {4}`. -/
theorem InC_small {n x : ℕ} (hn : n % 8 = 1) (hx0 : 0 < x) (hx : x ≤ 6) (h : InC n x) : x = 4 := by
  unfold InC at h
  omega

/-- For `n ≡ 1 (mod 8)`, `HC(n) ≤ 6 ⟺ HC(n) ≤ 4 ⟺` line 4 fires. -/
theorem HCle_six_iff {n : ℕ} (hn : n % 8 = 1) : HCle n 6 ↔ IsCoord n 4 := by
  constructor
  · rintro ⟨x, hx, hC, hc⟩
    rcases Nat.eq_zero_or_pos x with rfl | hx0
    · exact absurd hc (not_isCoord_zero n)
    · rwa [← InC_small hn hx0 hx hC]
  · intro h
    exact ⟨4, by norm_num, Or.inl (dvd_refl 4), h⟩

theorem HCle_four_iff {n : ℕ} (hn : n % 8 = 1) : HCle n 4 ↔ IsCoord n 4 := by
  rw [← HCle_six_iff hn]
  constructor
  · rintro ⟨x, hx, h⟩; exact ⟨x, by omega, h⟩
  · rintro ⟨x, hx, hC, hc⟩
    rcases Nat.eq_zero_or_pos x with rfl | hx0
    · exact absurd hc (not_isCoord_zero n)
    · exact ⟨x, by rw [InC_small hn hx0 hx hC], hC, hc⟩

/-- **HCKILL Lemma 1.1.** For `n ≡ 1 (mod 8)` (prime or not): `HC(n) > 4 ⟺ n + 4 ∈ S ∧ 4n + 1 ∈ S`. -/
theorem HC_gt_four_iff {n : ℕ} (hn : n % 8 = 1) : ¬ HCle n 4 ↔ (S (n + 4) ∧ S (4 * n + 1)) := by
  rw [HCle_four_iff hn, isCoord_iff_fires]
  unfold Fires
  have e1 : (∃ d, d ∣ n + 4 ∧ 4 ∣ d + 1) ↔ ∃ d, d ∣ n + 4 ∧ d % 4 = 3 := by
    constructor <;> rintro ⟨d, h1, h2⟩ <;> exact ⟨d, h1, by omega⟩
  have e2 : (∃ d, d ∣ 4 * n + 1 ∧ 4 ∣ d + 1) ↔ ∃ d, d ∣ 4 * n + 1 ∧ d % 4 = 3 := by
    constructor <;> rintro ⟨d, h1, h2⟩ <;> exact ⟨d, h1, by omega⟩
  rw [e1, e2, exists_dvd_three_iff (by omega), exists_dvd_three_iff (by omega)]
  tauto

/-- `HC(n) ≥ 3` for every `n ≡ 1 (mod 4)` (`1, 2 ∉ 𝒞_n`; Z53_UPPER Prop 2.1(i)). -/
theorem HC_gt_two {n : ℕ} (hn : n % 4 = 1) : ¬ HCle n 2 := by
  rintro ⟨x, hx, hC, hc⟩
  rcases Nat.eq_zero_or_pos x with rfl | hx0
  · exact not_isCoord_zero n hc
  · unfold InC at hC; omega

/-- `HC(n) ≥ 4` for every `n ≡ 1 (mod 8)`. -/
theorem HC_gt_three {n : ℕ} (hn : n % 8 = 1) : ¬ HCle n 3 := by
  rintro ⟨x, hx, hC, hc⟩
  rcases Nat.eq_zero_or_pos x with rfl | hx0
  · exact not_isCoord_zero n hc
  · unfold InC at hC; omega

/-! ### (b) Theorem Q -/

/-- **Theorem Q (Z54_HCKILL §2.1).** If `4 ∣ m` and `p = 5m² + 1` is prime, then `p ≡ 1 (mod 8)`, `12 ∣ m`, and
`HC(p) ≥ 7` (i.e. `¬ HC(p) ≤ 6`): `p + 4` and `4p + 1` lie in `S`, so line 4 does not fire. -/
theorem theoremQ {m p : ℕ} (hm : 4 ∣ m) (hp : p = 5 * m ^ 2 + 1) (hprime : p.Prime) :
    p % 8 = 1 ∧ 12 ∣ m ∧ S (p + 4) ∧ S (4 * p + 1) ∧ ¬ HCle p 6 := by
  have h8 : p % 8 = 1 := by
    obtain ⟨k, rfl⟩ := hm
    have : p = 8 * (10 * k ^ 2) + 1 := by rw [hp]; ring
    omega
  have h3 : 3 ∣ m := by
    by_contra h3
    have hm3 : m % 3 = 1 ∨ m % 3 = 2 := by omega
    have hsq : m ^ 2 % 3 = 1 := by
      rcases hm3 with h | h <;> simp [Nat.pow_mod, h]
    have hp3 : 3 ∣ p := by rw [hp]; omega
    have := (Nat.prime_dvd_prime_iff_eq (by norm_num) hprime).mp hp3
    rcases Nat.eq_zero_or_pos m with rfl | hm0
    · simp at hsq
    · have : 1 ≤ m ^ 2 := Nat.one_le_pow _ _ hm0
      omega
  have h12 : 12 ∣ m := Nat.Coprime.mul_dvd_of_dvd_of_dvd (by norm_num) h3 hm
  have hS1 : S (p + 4) := by
    have : p + 4 = 5 * (m ^ 2 + 1) := by rw [hp]; ring
    rw [this]
    exact S_mul S_five (S_sq_add_one (dvd_trans (by norm_num) hm))
  have hS2 : S (4 * p + 1) := by
    have : 4 * p + 1 = 5 * ((2 * m) ^ 2 + 1) := by rw [hp]; ring
    rw [this]
    exact S_mul S_five (S_sq_add_one (dvd_mul_right 2 m))
  refine ⟨h8, h12, hS1, hS2, ?_⟩
  rw [HCle_six_iff h8, ← HCle_four_iff h8]
  exact (HC_gt_four_iff h8).mpr ⟨hS1, hS2⟩

/-- Theorem Q in ES terms: such `p` have no certificate with a coordinate `≤ 6` in `𝒞_p`; in particular the
C-form with `C = 1` (`4p + 1 = ab`, `a ≡ b ≡ 3 (mod 4)`) fails at `p`. -/
theorem theoremQ_no_line4 {m p : ℕ} (hm : 4 ∣ m) (hp : p = 5 * m ^ 2 + 1) (hprime : p.Prime) :
    ¬ IsCoord p 4 := by
  obtain ⟨h8, -, -, -, h⟩ := theoremQ hm hp hprime
  rwa [HCle_six_iff h8] at h

/-! ### (d) Z54_UPPER2 Proposition 3.1 -/

/-- (a) `p ≡ 5 (mod 8)`: the word `(1, 3, (p+3)/2)`, and `HC(p) = 3`. -/
theorem prop31a {p : ℕ} (hp : p % 8 = 5) : Word p 1 3 ((p + 3) / 2) ∧ HCle p 3 ∧ ¬ HCle p 2 := by
  have hw : Word p 1 3 ((p + 3) / 2) := ⟨by norm_num, by norm_num, by omega, by omega⟩
  exact ⟨hw, ⟨3, le_refl 3, Or.inr (by omega), ⟨1, 3, _, hw, Or.inr (Or.inl rfl)⟩⟩, HC_gt_two (by omega)⟩

theorem prop31b_mod3_2 {p : ℕ} (h8 : p % 8 = 1) (h : p % 3 = 2) :
    Word p 1 4 ((p + 4) / 3) ∧ HCle p 4 ∧ ¬ HCle p 3 := by
  have hw : Word p 1 4 ((p + 4) / 3) := ⟨by norm_num, by norm_num, by omega, by omega⟩
  exact ⟨hw, ⟨4, le_refl 4, Or.inl (dvd_refl 4), ⟨1, 4, _, hw, Or.inr (Or.inl rfl)⟩⟩, HC_gt_three h8⟩

theorem prop31b_mod7_3 {p : ℕ} (h8 : p % 8 = 1) (h : p % 7 = 3) :
    Word p 2 4 ((p + 4) / 7) ∧ HCle p 4 ∧ ¬ HCle p 3 := by
  have hw : Word p 2 4 ((p + 4) / 7) := ⟨by norm_num, by norm_num, by omega, by omega⟩
  exact ⟨hw, ⟨4, le_refl 4, Or.inl (dvd_refl 4), ⟨2, 4, _, hw, Or.inr (Or.inl rfl)⟩⟩, HC_gt_three h8⟩

theorem prop31b_mod7_5 {p : ℕ} (h8 : p % 8 = 1) (h : p % 7 = 5) :
    Word p 4 2 (((4 * p + 1) / 7 + 1) / 4) ∧ HCle p 4 ∧ ¬ HCle p 3 := by
  have hw : Word p 4 2 (((4 * p + 1) / 7 + 1) / 4) := ⟨by norm_num, by norm_num, by omega, by omega⟩
  exact ⟨hw, ⟨4, le_refl 4, Or.inl (dvd_refl 4), ⟨4, 2, _, hw, Or.inl rfl⟩⟩, HC_gt_three h8⟩

theorem prop31b_mod5_3 {p : ℕ} (h8 : p % 8 = 1) (h : p % 5 = 3) :
    Word p 3 7 ((p + 7) / 20) ∧ HCle p 7 := by
  have hw : Word p 3 7 ((p + 7) / 20) := ⟨by norm_num, by norm_num, by omega, by omega⟩
  exact ⟨hw, ⟨7, le_refl 7, Or.inr (by omega), ⟨3, 7, _, hw, Or.inr (Or.inl rfl)⟩⟩⟩

theorem prop31b_mod5_2 {p : ℕ} (h8 : p % 8 = 1) (h : p % 5 = 2) :
    Word p 7 3 (((7 * p + 1) / 20 + 1) / 7) ∧ HCle p 7 := by
  have hw : Word p 7 3 (((7 * p + 1) / 20 + 1) / 7) := ⟨by norm_num, by norm_num, by omega, by omega⟩
  exact ⟨hw, ⟨7, le_refl 7, Or.inr (by omega), ⟨7, 3, _, hw, Or.inl rfl⟩⟩⟩

theorem prop31b_mod7_6 {p : ℕ} (h8 : p % 8 = 1) (h : p % 7 = 6) :
    Word p 1 8 ((p + 8) / 7) ∧ HCle p 8 := by
  have hw : Word p 1 8 ((p + 8) / 7) := ⟨by norm_num, by norm_num, by omega, by omega⟩
  exact ⟨hw, ⟨8, le_refl 8, Or.inl (by norm_num), ⟨1, 8, _, hw, Or.inr (Or.inl rfl)⟩⟩⟩

theorem HCle_mono {n X Y : ℕ} (hXY : X ≤ Y) (h : HCle n X) : HCle n Y := by
  obtain ⟨x, hx, h⟩ := h
  exact ⟨x, le_trans hx hXY, h⟩

/-- **Prop 3.1(b), summary.** `p ≡ 1 (mod 8)` and `p` a quadratic non-residue mod 3, 5 or 7 ⟹ `HC(p) ≤ 8`.
(No primality needed.) -/
theorem HC_le_eight_of_nonresidue {p : ℕ} (h8 : p % 8 = 1)
    (h : p % 3 = 2 ∨ p % 5 = 2 ∨ p % 5 = 3 ∨ p % 7 = 3 ∨ p % 7 = 5 ∨ p % 7 = 6) : HCle p 8 := by
  rcases h with h | h | h | h | h | h
  · exact HCle_mono (by norm_num) (prop31b_mod3_2 h8 h).2.1
  · exact HCle_mono (by norm_num) (prop31b_mod5_2 h8 h).2
  · exact HCle_mono (by norm_num) (prop31b_mod5_3 h8 h).2
  · exact HCle_mono (by norm_num) (prop31b_mod7_3 h8 h).2.1
  · exact HCle_mono (by norm_num) (prop31b_mod7_5 h8 h).2.1
  · exact (prop31b_mod7_6 h8 h).2

set_option maxRecDepth 100000 in
/-- CRT core of Prop 3.1(c): residues mod 840. -/
theorem cls840 : ∀ r : Fin 840, r.val % 8 = 1 → r.val % 3 ≠ 0 → r.val % 5 ≠ 0 → r.val % 7 ≠ 0 →
    (r.val ≠ 1 ∧ r.val ≠ 121 ∧ r.val ≠ 169 ∧ r.val ≠ 289 ∧ r.val ≠ 361 ∧ r.val ≠ 529) →
    (r.val % 3 = 2 ∨ r.val % 5 = 2 ∨ r.val % 5 = 3 ∨ r.val % 7 = 3 ∨ r.val % 7 = 5 ∨ r.val % 7 = 6) := by
  decide

/-- **Prop 3.1(c).** For every prime `p > 7`, `p ≡ 1 (mod 4)`, outside the classes `1, 121, 169, 289, 361, 529`
(mod 840): `HC(p) ≤ 8` (and hence ES holds at `p`, via `ES_of_HCle`). -/
theorem prop31c {p : ℕ} (hprime : p.Prime) (h7 : 7 < p) (h4 : p % 4 = 1)
    (hcl : p % 840 ≠ 1 ∧ p % 840 ≠ 121 ∧ p % 840 ≠ 169 ∧ p % 840 ≠ 289 ∧ p % 840 ≠ 361 ∧ p % 840 ≠ 529) :
    HCle p 8 := by
  have hcop : ∀ q, q.Prime → q ∣ p → q = p := fun q hq hd =>
    (Nat.prime_dvd_prime_iff_eq hq hprime).mp hd
  have h3 : p % 3 ≠ 0 := fun h => by
    have := hcop 3 (by norm_num) (Nat.dvd_of_mod_eq_zero h); omega
  have h5 : p % 5 ≠ 0 := fun h => by
    have := hcop 5 (by norm_num) (Nat.dvd_of_mod_eq_zero h); omega
  have h7' : p % 7 ≠ 0 := fun h => by
    have := hcop 7 (by norm_num) (Nat.dvd_of_mod_eq_zero h); omega
  rcases (show p % 8 = 5 ∨ p % 8 = 1 by omega) with h8 | h8
  · exact HCle_mono (by norm_num) (prop31a h8).2.1
  · have m8 : p % 840 % 8 = p % 8 := Nat.mod_mod_of_dvd p (by norm_num)
    have m3 : p % 840 % 3 = p % 3 := Nat.mod_mod_of_dvd p (by norm_num)
    have m5 : p % 840 % 5 = p % 5 := Nat.mod_mod_of_dvd p (by norm_num)
    have m7 : p % 840 % 7 = p % 7 := Nat.mod_mod_of_dvd p (by norm_num)
    have := cls840 ⟨p % 840, Nat.mod_lt _ (by norm_num)⟩ (by rw [m8, h8]) (by rw [m3]; exact h3)
      (by rw [m5]; exact h5) (by rw [m7]; exact h7') hcl
    rw [m3, m5, m7] at this
    exact HC_le_eight_of_nonresidue h8 this

set_option maxRecDepth 100000 in
/-- The six excluded classes mod 840 are exactly the `p ≡ 1 (mod 8)` that are quadratic residues mod 3, 5, 7
(and coprime to 105). -/
theorem prop31c_classes : ∀ r : Fin 840,
    ((r.val = 1 ∨ r.val = 121 ∨ r.val = 169 ∨ r.val = 289 ∨ r.val = 361 ∨ r.val = 529) ↔
      (r.val % 8 = 1 ∧ r.val % 3 = 1 ∧ (r.val % 5 = 1 ∨ r.val % 5 = 4) ∧
        (r.val % 7 = 1 ∨ r.val % 7 = 2 ∨ r.val % 7 = 4))) := by
  decide

end ESHC
