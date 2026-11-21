import ES.ProthCore

/-! A quadratic transfer for EVERY multiplier `k ≡ 15 (mod 16)`.
`u=k-1`, `z=t*u-1`, with `t=8i+7`. Then `n=k*(z²-1)+1` has
an interior word with `v=k*z`, and a positive ES triple. The CRT
square-unit-closure assertion of the paper is not formalized here. -/
namespace ESProthQuadratic
open ES (ESProp)
open ESProthCore (InteriorGoodWord es_of_word)

theorem quadratic_transfer (j i : ℕ) :
    let u := 16*j+14
    let k := u+1
    let t := 8*i+7
    let z := t*u-1
    let n := k*(z^2-1)+1
    InteriorGoodWord n u ∧ ESProp n := by
  intro u k t z n
  let v := k*z
  have hu : 2 ≤ u := by dsimp [u]; omega
  have ht : 2 ≤ t := by dsimp [t]; omega
  have htu : 4 ≤ t*u := by simpa using Nat.mul_le_mul ht hu
  have hz : 2 ≤ z := by dsimp [z]; omega
  have hzp : z+1 = t*u := by dsimp [z]; omega
  have hz2 : 1 ≤ z^2 := by nlinarith
  have hnk : n+u = z*v := by
    have e : z^2-1+1=z^2 := by omega
    calc n+u = k*((z^2-1)+1) := by dsimp [n,k]; ring
         _ = z*v := by rw [e]; dsimp [v]; ring
  have hv : 2 ≤ v := by dsimp [v,k]; nlinarith
  have ur : u%8=6 := by dsimp [u]; omega
  have tr : t%8=7 := by dsimp [t]; omega
  have zr : z%8=1 := by
    have e := congrArg (· % 8) hzp
    rw [Nat.mul_mod, tr, ur] at e; omega
  have vr : v%8=7 := by
    dsimp [v,k]; rw [Nat.mul_mod, zr]; omega
  have nr : n%8=1 := by
    have e := congrArg (· % 8) hnk
    rw [Nat.mul_mod, zr, vr] at e; omega
  have hn : 0<n := by dsimp [n]; omega
  constructor
  · refine ⟨t,v,ht,hu,hv,?_,by omega⟩
    rw [hnk, ← hzp]; ring
  · have hdiv : z ∣ n+u := ⟨v,hnk⟩
    have hdiv' : u ∣ z+1 := ⟨t,by rw [hzp,Nat.mul_comm]⟩
    apply es_of_word hn (by omega) (by omega) hdiv hdiv'
    rw [hzp, hnk, Nat.mul_div_cancel _ (by omega : 0<u), Nat.mul_div_cancel_left _ (by omega : 0<z)]
    have e := Nat.mul_mod t v 8
    rw [tr,vr] at e; omega

#print axioms quadratic_transfer
end ESProthQuadratic
