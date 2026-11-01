import ES.Basic
import Mathlib

/-!
# Z1894: ES for every `3·2^s + 1` (MENU_STERILITY.md Theorem C, (J)74/(J)75) — Lean formalisation

Erdős–Straus (ES) is OPEN. This file formalises one *thin family* theorem of the repository:
**for every `s : ℕ`, `4/(3·2^s+1)` is a sum of three unit fractions** (`MENU_STERILITY.md` §4, Theorem C; PROVED there,
computer-assisted, hand-checkable). Nothing about primes in general follows.

`ESProp` is `ES.ESProp` from `ES/Basic.lean` (4xyz = n(xy + yz + zx), x, y, z > 0).

## Proof structure (as in MENU_STERILITY Theorem C)
* `ES_of_dvd`: ES(q) and q ∣ n ⟹ ES(n) (scale the solution).
* `window` (CAP_DOWN Lemma 1.1): if `n + m = 4K`, `K² = d e`, `m y₀ = K + d`, `m z₀ = e + K`, then
  `(K, n y₀, n z₀)` solves ES(n).
* `sg_window` (Theorem C(a), the Sophie-Germain window m = 11): for X = Y + 1 with X mod 11 ∈ {2,…,9},
  n = 48X⁴ + 1, K = 3 f₊ f₋ (f± = 2X² ± 2X + 1, 4X⁴ + 1 = f₊f₋), d = f₊^b f₋^c with (b, c) from the table.
* ET/divisor classes (Theorem C(b)): s ≡ 1 (3): 7 ∣ n; s ≡ 2 (3): n ≡ 6 (7); s ≡ 1 (4): n ≡ 7 (15);
  s ≡ 2 (4): n ≡ 13 (15); s ≡ 3 (4): 5 ∣ n; s ≡ 24 (60): 61 ∣ n; s = 0: n = 4.
* `proth3`: the case split on s (mod 3, mod 4, X = 2^j mod 11).
-/

namespace ESProth3

open ES (ESProp)

/-- Scaling: a solution for `q` gives one for every multiple `n = q k`, `k > 0`. -/
theorem ES_of_dvd {q n : ℕ} (h : ESProp q) (hd : q ∣ n) (hn : 0 < n) : ESProp n := by
  obtain ⟨x, y, z, hx, hy, hz, e⟩ := h
  obtain ⟨k, rfl⟩ := hd
  have hk : 0 < k := by
    rcases Nat.eq_zero_or_pos k with rfl | hk
    · simp at hn
    · exact hk
  refine ⟨x * k, y * k, z * k, by positivity, by positivity, by positivity, ?_⟩
  have : 4 * (x * k) * (y * k) * (z * k) = (4 * x * y * z) * k ^ 3 := by ring
  rw [this, e]; ring

/-- The window lemma (CAP_DOWN Lemma 1.1): `x = K`, `y = n y₀`, `z = n z₀`. -/
theorem window {n m K d e y₀ z₀ : ℕ} (hn : 0 < n) (hm : 0 < m) (hK : n + m = 4 * K) (hde : K * K = d * e)
    (hy : m * y₀ = K + d) (hz : m * z₀ = e + K) (hK0 : 0 < K) (hy0 : 0 < y₀) (hz0 : 0 < z₀) : ESProp n := by
  refine ⟨K, n * y₀, n * z₀, hK0, by positivity, by positivity, ?_⟩
  -- key: m y₀ z₀ = K (y₀ + z₀), obtained after multiplying by m
  have key : m * (y₀ * z₀) = K * (y₀ + z₀) := by
    have h2 : m * (m * (y₀ * z₀)) = m * (K * (y₀ + z₀)) := by
      have : m * (m * (y₀ * z₀)) = (m * y₀) * (m * z₀) := by ring
      rw [this, hy, hz]
      have : m * (K * (y₀ + z₀)) = K * (m * y₀) + K * (m * z₀) := by ring
      rw [this, hy, hz]
      nlinarith [hde]
    exact Nat.eq_of_mul_eq_mul_left hm h2
  have : 4 * K * (n * y₀) * (n * z₀) = n * n * ((n + m) * (y₀ * z₀)) := by rw [hK]; ring
  rw [this]
  have : (n + m) * (y₀ * z₀) = n * (y₀ * z₀) + K * (y₀ + z₀) := by rw [add_mul, key]
  rw [this]; ring

/-- Explicit small solutions. -/
theorem ES4 : ESProp 4 := ⟨2, 3, 6, by norm_num, by norm_num, by norm_num, by norm_num⟩
theorem ES5 : ESProp 5 := ⟨2, 4, 20, by norm_num, by norm_num, by norm_num, by norm_num⟩
theorem ES7 : ESProp 7 := ⟨2, 15, 210, by norm_num, by norm_num, by norm_num, by norm_num⟩
theorem ES61 : ESProp 61 := ⟨16, 326, 159088, by norm_num, by norm_num, by norm_num, by norm_num⟩

/-- ET class n ≡ 6 (mod 7): `(2(n+1)/7, 2n, 2n(n+1)/7)`. -/
theorem ES_mod7_6 (k : ℕ) : ESProp (7 * k + 6) := by
  refine ⟨2 * (k + 1), 2 * (7 * k + 6), 2 * (7 * k + 6) * (k + 1), by positivity, by positivity, by positivity, ?_⟩
  ring

/-- ET class n ≡ 7 (mod 15): `((4n+2)/15, 4n, 4n(2n+1)/15)`. -/
theorem ES_mod15_7 (k : ℕ) : ESProp (15 * k + 7) := by
  refine ⟨4 * k + 2, 4 * (15 * k + 7), 4 * (15 * k + 7) * (2 * k + 1), by positivity, by positivity, by positivity, ?_⟩
  ring

/-- ET class n ≡ 13 (mod 15): `((4n+8)/15, 4n, 2n(n+2)/15)`. -/
theorem ES_mod15_13 (k : ℕ) : ESProp (15 * k + 13) := by
  refine ⟨4 * (k + 1), 4 * (15 * k + 13), 2 * (15 * k + 13) * (k + 1), by positivity, by positivity, by positivity, ?_⟩
  ring

/-! ### The Sophie-Germain window m = 11 (Theorem C(a)) -/

/-- `f₊(X) = 2X² + 2X + 1`. With `X = Y + 1`, `f₋(X) = 2X² − 2X + 1 = f₊(Y)`. -/
def fp (X : ℕ) : ℕ := 2 * X ^ 2 + 2 * X + 1

theorem sophie_germain (Y : ℕ) : 4 * (Y + 1) ^ 4 + 1 = fp (Y + 1) * fp Y := by unfold fp; ring

theorem fp_pos (X : ℕ) : 0 < fp X := by unfold fp; positivity

/-- One window rule: `d = f₊^b f₋^c`, `e = 9 f₊^(2-b) f₋^(2-c)`, valid when `11 ∣ K + d` and `11 ∣ e + K`. -/
theorem sg_rule (Y b c : ℕ) (hb : b ≤ 2) (hc : c ≤ 2)
    (h1 : 11 ∣ 3 * fp (Y + 1) * fp Y + fp (Y + 1) ^ b * fp Y ^ c)
    (h2 : 11 ∣ 9 * fp (Y + 1) ^ (2 - b) * fp Y ^ (2 - c) + 3 * fp (Y + 1) * fp Y) :
    ESProp (48 * (Y + 1) ^ 4 + 1) := by
  obtain ⟨y₀, hy⟩ := h1
  obtain ⟨z₀, hz⟩ := h2
  have hP := fp_pos (Y + 1)
  have hM := fp_pos Y
  have hK0 : 0 < 3 * fp (Y + 1) * fp Y := by positivity
  apply window (m := 11) (K := 3 * fp (Y + 1) * fp Y) (d := fp (Y + 1) ^ b * fp Y ^ c)
    (e := 9 * fp (Y + 1) ^ (2 - b) * fp Y ^ (2 - c)) (y₀ := y₀) (z₀ := z₀) (by positivity) (by norm_num)
  · have := sophie_germain Y; nlinarith [this]
  · have eb : fp (Y + 1) ^ 2 = fp (Y + 1) ^ b * fp (Y + 1) ^ (2 - b) := by
      rw [← pow_add]; congr 1; omega
    have ec : fp Y ^ 2 = fp Y ^ c * fp Y ^ (2 - c) := by
      rw [← pow_add]; congr 1; omega
    calc 3 * fp (Y + 1) * fp Y * (3 * fp (Y + 1) * fp Y) = 9 * fp (Y + 1) ^ 2 * fp Y ^ 2 := by ring
      _ = 9 * (fp (Y + 1) ^ b * fp (Y + 1) ^ (2 - b)) * (fp Y ^ c * fp Y ^ (2 - c)) := by rw [← eb, ← ec]
      _ = _ := by ring
  · omega
  · omega
  · exact hK0
  · rcases Nat.eq_zero_or_pos y₀ with h0 | h0
    · subst h0; have : 0 < fp (Y + 1) ^ b * fp Y ^ c := by positivity
      omega
    · exact h0
  · rcases Nat.eq_zero_or_pos z₀ with h0 | h0
    · subst h0; omega
    · exact h0

/-- Divisibility by 11 is decided by the residue of `Y` mod 11. -/
theorem dvd11_of_mod {P : ℕ → ℕ} (hP : ∀ Y, (P Y : ZMod 11) = P (Y % 11)) {Y : ℕ}
    (h : 11 ∣ P (Y % 11)) : 11 ∣ P Y := by
  rw [← ZMod.natCast_eq_zero_iff] at h ⊢
  rw [hP Y]; exact h

theorem fp_cast (X : ℕ) : (fp X : ZMod 11) = 2 * (X : ZMod 11) ^ 2 + 2 * X + 1 := by
  unfold fp; push_cast; ring

/-- **Theorem C(a).** For `X = Y + 1 ≢ 0, ±1 (mod 11)`, ES(48X⁴ + 1). -/
theorem sg_window (Y : ℕ) (hY : (Y + 1) % 11 ≠ 0 ∧ (Y + 1) % 11 ≠ 1 ∧ (Y + 1) % 11 ≠ 10) :
    ESProp (48 * (Y + 1) ^ 4 + 1) := by
  -- residues of Y = X - 1:  X ≡ 2,3,4,5,6,7,8,9  ↔  Y ≡ 1,…,8
  have hr : Y % 11 = 1 ∨ Y % 11 = 2 ∨ Y % 11 = 3 ∨ Y % 11 = 4 ∨ Y % 11 = 5 ∨ Y % 11 = 6 ∨ Y % 11 = 7 ∨
      Y % 11 = 8 := by omega
  have hc : (Y : ZMod 11) = ((Y % 11 : ℕ) : ZMod 11) := (ZMod.natCast_mod Y 11).symm
  have T : ∀ b c : ℕ, b ≤ 2 → c ≤ 2 →
      (((3 * fp (Y + 1) * fp Y + fp (Y + 1) ^ b * fp Y ^ c : ℕ) : ZMod 11) = 0) →
      (((9 * fp (Y + 1) ^ (2 - b) * fp Y ^ (2 - c) + 3 * fp (Y + 1) * fp Y : ℕ) : ZMod 11) = 0) →
      ESProp (48 * (Y + 1) ^ 4 + 1) := by
    intro b c hb hc' h1 h2
    exact sg_rule Y b c hb hc' ((ZMod.natCast_eq_zero_iff _ _).mp h1) ((ZMod.natCast_eq_zero_iff _ _).mp h2)
  rcases hr with h | h | h | h | h | h | h | h
  -- X ≡ 2: (b,c) = (0,2)
  · refine T 0 2 (by norm_num) (by norm_num) ?_ ?_ <;>
      (push_cast [fp_cast]; rw [hc, h]; decide)
  -- X ≡ 3: (0,2)
  · refine T 0 2 (by norm_num) (by norm_num) ?_ ?_ <;>
      (push_cast [fp_cast]; rw [hc, h]; decide)
  -- X ≡ 4: (2,1)
  · refine T 2 1 (by norm_num) (by norm_num) ?_ ?_ <;>
      (push_cast [fp_cast]; rw [hc, h]; decide)
  -- X ≡ 5: (1,2)
  · refine T 1 2 (by norm_num) (by norm_num) ?_ ?_ <;>
      (push_cast [fp_cast]; rw [hc, h]; decide)
  -- X ≡ 6: (2,1)
  · refine T 2 1 (by norm_num) (by norm_num) ?_ ?_ <;>
      (push_cast [fp_cast]; rw [hc, h]; decide)
  -- X ≡ 7: (1,2)
  · refine T 1 2 (by norm_num) (by norm_num) ?_ ?_ <;>
      (push_cast [fp_cast]; rw [hc, h]; decide)
  -- X ≡ 8: (2,0)
  · refine T 2 0 (by norm_num) (by norm_num) ?_ ?_ <;>
      (push_cast [fp_cast]; rw [hc, h]; decide)
  -- X ≡ 9: (2,0)
  · refine T 2 0 (by norm_num) (by norm_num) ?_ ?_ <;>
      (push_cast [fp_cast]; rw [hc, h]; decide)

/-! ### Periodicity of `2^s` modulo small moduli -/

theorem pow_mod_period {a M P : ℕ} (hM : 1 < M) (h : a ^ P % M = 1) (s : ℕ) :
    a ^ s % M = a ^ (s % P) % M := by
  conv_lhs => rw [← Nat.div_add_mod s P, pow_add, pow_mul]
  rw [Nat.mul_mod, Nat.pow_mod, h, one_pow, Nat.one_mod_eq_one.mpr (by omega), one_mul, Nat.mod_mod]

/-! ### Main theorem (MENU_STERILITY Theorem C) -/

theorem proth3 (s : ℕ) : ESProp (3 * 2 ^ s + 1) := by
  have hn : 0 < 3 * 2 ^ s + 1 := by positivity
  have p7 : 2 ^ s % 7 = 2 ^ (s % 3) % 7 := pow_mod_period (by norm_num) (by norm_num) s
  have p15 : 2 ^ s % 15 = 2 ^ (s % 4) % 15 := pow_mod_period (by norm_num) (by norm_num) s
  obtain h3 | h3 | h3 : s % 3 = 0 ∨ s % 3 = 1 ∨ s % 3 = 2 := by omega
  rotate_left
  · -- s ≡ 1 (3): 7 ∣ n
    rw [h3] at p7; norm_num at p7
    exact ES_of_dvd ES7 (by omega) hn
  · -- s ≡ 2 (3): n ≡ 6 (7)
    rw [h3] at p7; norm_num at p7
    have e : 3 * 2 ^ s + 1 = 7 * ((3 * 2 ^ s + 1) / 7) + 6 := by omega
    rw [e]; exact ES_mod7_6 _
  -- s ≡ 0 (3)
  obtain h4 | h4 | h4 | h4 : s % 4 = 0 ∨ s % 4 = 1 ∨ s % 4 = 2 ∨ s % 4 = 3 := by omega
  rotate_left
  · rw [h4] at p15; norm_num at p15
    have e : 3 * 2 ^ s + 1 = 15 * ((3 * 2 ^ s + 1) / 15) + 7 := by omega
    rw [e]; exact ES_mod15_7 _
  · rw [h4] at p15; norm_num at p15
    have e : 3 * 2 ^ s + 1 = 15 * ((3 * 2 ^ s + 1) / 15) + 13 := by omega
    rw [e]; exact ES_mod15_13 _
  · rw [h4] at p15; norm_num at p15
    exact ES_of_dvd ES5 (by omega) hn
  -- s ≡ 0 (12)
  rcases Nat.eq_zero_or_pos s with hs | hs
  · subst hs; exact ES4
  obtain ⟨j, rfl⟩ : ∃ j, s = 4 * j + 4 := ⟨s / 4 - 1, by omega⟩
  have hX : 3 * 2 ^ (4 * j + 4) + 1 = 48 * (2 ^ j) ^ 4 + 1 := by ring
  have p11 : 2 ^ j % 11 = 2 ^ (j % 10) % 11 := pow_mod_period (by norm_num) (by norm_num) j
  by_cases hw : 2 ^ j % 11 ≠ 1 ∧ 2 ^ j % 11 ≠ 10
  · obtain ⟨Y, hY⟩ : ∃ Y, 2 ^ j = Y + 1 := ⟨2 ^ j - 1, by have := Nat.one_le_two_pow (n := j); omega⟩
    rw [hX, hY]
    have h0 : 2 ^ j % 11 ≠ 0 := by
      rw [p11]; have : j % 10 < 10 := Nat.mod_lt _ (by norm_num)
      interval_cases (j % 10) <;> norm_num
    exact sg_window Y ⟨by omega, by omega, by omega⟩
  · -- 2^j ≡ 1 or 10 (mod 11)  ⟹  j ≡ 0, 5 (mod 10)  ⟹  s ≡ 24 (mod 60)  ⟹  61 ∣ n
    have hj : j % 10 = 0 ∨ j % 10 = 5 := by
      rw [p11] at hw; have : j % 10 < 10 := Nat.mod_lt _ (by norm_num)
      interval_cases h : (j % 10) <;> simp_all
    have h60 : (4 * j + 4) % 60 = 24 := by omega
    have p61 : 2 ^ (4 * j + 4) % 61 = 2 ^ ((4 * j + 4) % 60) % 61 :=
      pow_mod_period (by norm_num) (by norm_num) _
    rw [h60] at p61; norm_num at p61
    exact ES_of_dvd ES61 (by omega) hn

end ESProth3
