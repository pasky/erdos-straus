import Std
/- LLM-written proofs checked by Lean 4.34.1 (core Std; no Mathlib).
Ten short algebraic/congruence components extracted from PROVED ledger entries.
Scope is precisely the statements below, NOT their parent analytic/geometric theorems.
-/

-- DISCOVERIES.md:629, master identity, denominators cleared.
theorem master_cleared (t u v n : Int) :
    t*u*v-u-v=n ↔ t*u*v=n+u+v := by omega

-- DISCOVERIES.md:1662, Lemma 1.1 pair form of (★).
theorem star_pair (u b c p : Int) (h : 4*u*b*c-u-b=p) :
    (4*c*u-1)*(4*c*b-1)=4*c*p+1 := by grind

-- DISCOVERIES.md:1662, Lemma 1.1 divisor/SL₂ form.
theorem star_determinant (u b c p : Int) (h : 4*u*b*c-u-b=p) :
    (4*c*u-1)*b-u=p := by grind

-- DISCOVERIES.md:1554, common-shift divisibility core of gcd lemma.
-- Any common divisor divides j-j'; instantiate d = gcd(jp+1,j'p+1).
theorem common_shift_divisor (d j k p : Int)
    (hj : d ∣ j*p+1) (hk : d ∣ k*p+1) : d ∣ j-k := by
  obtain ⟨a, ha⟩ := hj
  obtain ⟨b, hb⟩ := hk
  refine ⟨j*b-k*a, ?_⟩
  grind

-- DISCOVERIES.md:1362, 4^s+105 window gap.
theorem window105_gap (u : Int) :
    4*(64*(u^3+1))-(256*u^3+105)=151 := by grind

-- DISCOVERIES.md:1362, cyclotomic budget factorisation.
theorem window105_factor (u : Int) :
    64*u^3+2*u^2-2*u+66=2*(32*u+33)*(u^2-u+1) := by grind

-- DISCOVERIES.md:1362, integrality congruence in the window.
theorem window105_integral (u : Int) (h : u % 151 = 32) :
    (32*u+33) % 151 = 0 := by omega

-- DISCOVERIES.md:1404, Sophie-Germain factorisation used in Theorem B/C.
theorem sophie_germain (x : Int) :
    4*x^4+1=(2*x^2+2*x+1)*(2*x^2-2*x+1) := by grind

-- DISCOVERIES.md:1631, Lemmas C/D: modular equality plus short interval
-- forces the first positive multiple, stated using a divisibility witness.
theorem short_multiple (p w : Int) (hp : 0 < p) (hw : 0 < w)
    (hsmall : w < 2*p) (hdiv : p ∣ w) : w=p := by
  obtain ⟨k, hk⟩ := hdiv
  have hkpos : 0 < k := by
    apply Classical.byContradiction
    intro hneg
    have hnon : k ≤ 0 := by omega
    have hm := Int.mul_nonpos_of_nonneg_of_nonpos (a := p) (b := k) (by omega) hnon
    omega
  have hklt : k < 2 := by
    apply Classical.byContradiction
    intro hge
    have hm := Int.mul_le_mul_of_nonneg_left (a := 2) (b := k) (c := p) (by omega) (by omega)
    omega
  have : k = 1 := by omega
  subst k
  simpa using hk

-- DISCOVERIES.md:862, Lemma 2.1 parity obstruction, cleared ES equation:
-- for odd n the parity equation excludes 2 or 3 odd denominators.
theorem es_parity (n x y z : Int) (hn : n % 2 = 1)
    (h : 4*x*y*z=n*(x*y+y*z+z*x)) :
    (x%2=0 ∧ y%2=0 ∧ z%2=0) ∨
    (x%2=1 ∧ y%2=0 ∧ z%2=0) ∨
    (x%2=0 ∧ y%2=1 ∧ z%2=0) ∨
    (x%2=0 ∧ y%2=0 ∧ z%2=1) := by
  have he := congrArg (fun a : Int => a % 2) h
  have hx : x%2=0 ∨ x%2=1 := by omega
  have hy : y%2=0 ∨ y%2=1 := by omega
  have hz : z%2=0 ∨ z%2=1 := by omega
  rcases hx with hx | hx <;> rcases hy with hy | hy <;> rcases hz with hz | hz <;>
    simp [Int.mul_emod, Int.add_emod, hn, hx, hy, hz] at he <;> omega

#print axioms master_cleared
#print axioms star_pair
#print axioms star_determinant
#print axioms common_shift_divisor
#print axioms window105_gap
#print axioms window105_factor
#print axioms window105_integral
#print axioms sophie_germain
#print axioms short_multiple
#print axioms es_parity
