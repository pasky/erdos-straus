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
  simp only [coeff_add, coeff_X_pow_mul', le_refl, ite_true, Nat.sub_self] at he
  rw [coeff_eq_zero_of_natDegree_lt hb, coeff_eq_zero_of_natDegree_lt (by omega : low.natDegree < N),
    ← htop, hA.coeff_natDegree] at he
  exact (eq_C_of_natDegree_eq_zero hc).trans (by rw [show carry.coeff 0 = 1 by simpa using he.symm, C_1])

private theorem close_endpoint (m W J g : Poly) (b : ℕ)
    (hm : m ≠ 0) (hW : W ≠ 0) (hJ : J ≠ 0) (w : W.natDegree = 2)
    (companion : U*g*J = T^b*W + 1)
    (eq63 : m*W*(T*(T^3-U*W)*J-U) = T^3*J+U) : False := by
  let Δ := T^3-U*W
  by_cases hc : Δ.natDegree = 0
  · have hconst := eq_C_of_natDegree_eq_zero hc
    have atRoot := congrArg (eval (-1 : ZMod 3)) hconst
    change eval (-1) (T^3-U*W) = eval (-1) (C (Δ.coeff 0)) at atRoot
    simp at atRoot
    have hprod : U*W = T^3+1 := by
      change T^3-U*W = C (Δ.coeff 0) at hconst
      rw [← atRoot] at hconst
      simp at hconst
      linear_combination -hconst
    have hcub : U^3 = T^3+1 := by rw [add_pow_char]; ring
    have hu : U ≠ 0 := fun he => by simpa [he] using degU
    have hw2 : W = U^2 := mul_left_cancel₀ hu (by rw [hprod, ← hcub]; ring)
    have he := congrArg (eval (-1 : ZMod 3)) companion
    simp [hw2] at he
  · have hΔ : Δ ≠ 0 := by intro e; simp [e] at hc
    have lhsDeg : (T*Δ*J).natDegree = 1+Δ.natDegree+J.natDegree := by
      rw [natDegree_mul (mul_ne_zero X_ne_zero hΔ) hJ, natDegree_mul X_ne_zero hΔ, natDegree_X]
    have hbr := natDegree_sub_eq_left_of_natDegree_lt
      (by rw [lhsDeg, degU]; omega : (U).natDegree < (T*Δ*J).natDegree)
    have hn : T*Δ*J-U ≠ 0 := by intro he; rw [he, natDegree_zero, lhsDeg] at hbr; omega
    have hd := congrArg natDegree eq63
    change (m*W*(T*Δ*J-U)).natDegree = (T^3*J+U).natDegree at hd
    have hr := natDegree_X_pow_mul 3 hJ
    rw [natDegree_mul (mul_ne_zero hm hW) hn, natDegree_mul hm hW, hbr, lhsDeg, w,
      natDegree_add_eq_left_of_natDegree_lt (by rw [degU, hr]; omega), hr] at hd
    omega

/-- No tuple in the two `c=1` orientations can satisfy the identities and
natural-degree data of §§1–3. This is §6 for the large-level case, not the
upstream parametrisation, bounded-determinant theorem, or compactness step.
`x` is the short side, not the polynomial indeterminate `T`. -/
theorem no_covering_endpoint (p q κ m x M H W S J g : Poly) (δ b N : ℕ)
    (orient : (p=1 ∧ q=U ∧ κ=1) ∨ (p=U ∧ q=1 ∧ κ= -1))
    (mp : p.Monic) (mq : q.Monic) (mm : m.Monic) (mM : M.Monic)
    (mH : H.Monic) (mW : W.Monic) (hJ : J ≠ 0) (_hW0 : W.eval 0 ≠ 0)
    (hM : M=m*x) (hMW : M*W=T^δ*S*J+κ*q) (hMH : M*H=q*T^b+J)
    (hXS : p*x*S=T^(b+1)*W-q*H) (hcomp : p*g*J=T^b*W-κ*H)
    (hN : δ+b=N) (hδ : δ=3 ∨ δ=4)
    (hshort : N+1 ≤ M.natDegree+x.natDegree+p.natDegree)
    (hd : M.natDegree ≤ b+q.natDegree) (hw : W.natDegree ≤ 1+p.natDegree)
    (hH : H.natDegree+M.natDegree=b+q.natDegree) : False := by
  have hu : p*q=U := by rcases orient with ⟨rfl,rfl,_⟩ | ⟨rfl,rfl,_⟩ <;> simp
  have hpq : p.natDegree+q.natDegree=1 := by
    rcases orient with ⟨rfl,rfl,_⟩ | ⟨rfl,rfl,_⟩ <;> simp
  have hlow : (κ*U).natDegree=1 := by
    rcases orient with ⟨_,_,rfl⟩ | ⟨_,_,rfl⟩ <;>
      simp only [one_mul, neg_one_mul, natDegree_neg, degU]
  have hdn : M.natDegree = m.natDegree+x.natDegree := by
    have hx : x ≠ 0 := by intro he; exact mM.ne_zero (by simp [hM,he])
    rw [hM, natDegree_mul mm.ne_zero hx]
  let A := p*M*W
  let B := T^δ*q*m*H^2
  have hA : A.Monic := (mp.mul mM).mul mW
  have hB : B.Monic := (((monic_X_pow δ).mul mq).mul mm).mul (mH.pow 2)
  have da : A.natDegree = p.natDegree+M.natDegree+W.natDegree := by
    dsimp [A]; rw [(mp.mul mM).natDegree_mul mW, mp.natDegree_mul mM]
  have db : B.natDegree = δ+q.natDegree+m.natDegree+2*H.natDegree := by
    dsimp [B]; rw [(((monic_X_pow δ).mul mq).mul mm).natDegree_mul (mH.pow 2),
      ((monic_X_pow δ).mul mq).natDegree_mul mm, (monic_X_pow δ).natDegree_mul mq,
      natDegree_X_pow, natDegree_pow]
  obtain ⟨htop,hcarry⟩ := carry_one A B (κ*U) _ N hA hB (by omega) (by omega) (by omega)
    (key_identity T p q U κ m x M H W S J δ b N hMW hMH hXS hM hu hN)
  -- The degree equality forces the unique B endpoint, including H = 1.
  have hp : p.natDegree=1 := by omega
  have hthree : δ=3 := by omega
  have hmb : M.natDegree=b := by omega
  have htwo : W.natDegree=2 := by omega
  have hOne : H=1 := eq_one_of_monic_natDegree_zero mH (by omega)
  obtain ⟨rfl,rfl,rfl⟩ : p=U ∧ q=1 ∧ κ= -1 := by
    rcases orient with ⟨rfl,_,_⟩ | h
    · simp at hp
    · exact h
  subst H; subst δ
  simp only [mul_one, one_mul, sub_neg_eq_add] at hMH hXS hcomp hcarry hMW
  rw [pow_succ] at hXS
  have hx : x=T*W*J+1 := by
    rw [hM] at hMH
    linear_combination T*W*hMH - x*hcarry - hXS
  apply close_endpoint m W J g b mm.ne_zero mW.ne_zero hJ htwo hcomp
  rw [hM, hx] at hMW
  linear_combination -U*hMW + T^3*J*hcarry

#print axioms no_covering_endpoint
#print axioms key_identity
end ES.F3Endpoint
