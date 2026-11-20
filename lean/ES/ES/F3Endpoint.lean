import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Algebra.Polynomial.Monic
import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

/-! The endpoint elimination of `notes/z78/F3_CONJ.md`, §6. The inputs from the
preceding tuple theory and its two differential estimates are hypotheses. -/
namespace ES.F3Endpoint

/-- Equation (6.1), before specializing either the characteristic or `T`. -/
theorem key_identity {R : Type*} [CommRing R]
    (T p q u κ m x M H W S J : R) (δ b N : ℕ)
    (hMW : M * W = T^δ * S * J + κ*q) (hMH : M * H = q*T^b + J)
    (hXS : p*x*S = T^(b+1)*W - q*H) (hM : M = m*x)
    (hu : p*q = u) (hN : δ+b=N) :
    p*M*W + T^δ*q*m*H^2 = κ*u + T^N*(T*m*H*W-u*S) := by
  subst M; subst u; subst N
  rw [pow_add]; rw [pow_succ] at hXS
  linear_combination p*hMW - p*T^δ*S*hMH + T^δ*m*H*hXS

open Polynomial
abbrev Poly := Polynomial (ZMod 3)
local notation "T" => (X : Poly)
local notation "U" => (1 + T)

private theorem degU : (U).natDegree = 1 := by simp [add_comm (1 : Poly) T]

/-- The only equal-degree cancellation issue is `1+1 ≠ 0` in F₃. -/
private theorem degSum (A B : Poly) (hA : A.Monic) (hB : B.Monic) :
    (A+B).natDegree = max A.natDegree B.natDegree := by
  rcases lt_trichotomy A.natDegree B.natDegree with h | h | h
  · rw [natDegree_add_eq_right_of_natDegree_lt h, max_eq_right h.le]
  · rw [h, max_self]
    apply le_antisymm ((natDegree_add_le A B).trans (by omega))
    apply le_natDegree_of_ne_zero
    rw [coeff_add, ← h, hA.coeff_natDegree, h, hB.coeff_natDegree]
    decide
  · rw [natDegree_add_eq_left_of_natDegree_lt h, max_eq_left h.le]

/-- Read the top coefficient of (6.1), with `A=pMW`, `B=T^δ q m H²`. -/
private theorem carry_one (A B low carry : Poly) (N : ℕ)
    (hA : A.Monic) (hB : B.Monic) (hlow : low.natDegree < B.natDegree)
    (ha : A.natDegree ≤ N) (hb : B.natDegree < N)
    (hid : A+B = low + T^N * carry) : A.natDegree = N ∧ carry = 1 := by
  have hsum := degSum A B hA hB
  have hbig : low.natDegree < (A+B).natDegree := by omega
  have hdif := natDegree_sub_eq_left_of_natDegree_lt hbig
  have hh : (A+B)-low = T^N*carry := by linear_combination hid
  rw [hh] at hdif
  have hn : carry ≠ 0 := by
    intro hz; simp [hz] at hdif; omega
  rw [natDegree_X_pow_mul N hn] at hdif
  have htop : A.natDegree=N := by omega
  refine ⟨htop, ?_⟩
  have hc : carry.natDegree=0 := by omega
  have he := congrArg (fun f : Poly => f.coeff N) hid
  simp only [coeff_add, coeff_X_pow_mul', le_refl, if_true, Nat.sub_self] at he
  rw [coeff_eq_zero_of_natDegree_lt hb, coeff_eq_zero_of_natDegree_lt (by omega : low.natDegree < N),
    ← htop, hA.coeff_natDegree] at he
  exact (eq_C_of_natDegree_eq_zero hc).trans (by rw [show carry.coeff 0 = 1 by simpa using he.symm, C_1])

#print axioms key_identity
end ES.F3Endpoint
