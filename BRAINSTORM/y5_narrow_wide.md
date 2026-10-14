# y5_narrow_wide — positivity is complex conjugation: the ES condition is the narrow/wide ray-class split (O213, item (d))

## Idea
O210 found that "T1 lives in positivity". y5_general_r_jacobi Thm 1 made the ∞-factor explicit:
s_∞ = (−1)^{#(K_i < 0 < K_{i+1})}. Here we locate the same archimedean bit inside the divisor formulations.

**Prop 1 (PROVED).** Fix m ≥ 1 and odd N.
* Integer words (c, m, s) with K₁, K₂ ≠ 0 and c, s of equal sign correspond to factorisations 1 + Nm = ab, with
  h = cm − 1 and h′ = ms − 1:
  * **positive words** (c, s ≥ 1): a = h, b = h′, both > 0, and **a ≡ b ≡ −1 (mod m)**;
  * **negative-pair words** (c, s ≤ −1): a = −h, b = −h′ > 1, and **a ≡ b ≡ +1 (mod m)**.
* For a negative-pair word K₁ = c < 0, K₂ = h < 0 < K₃ = N, so s_∞ = −1 and the ES sign flips:
  (h′/N) = −s₂.
* A trivial factorisation (a, b) = (1, 1 + Nm) is always in the +1 class. So negative-pair-type data exist for every N,
  apart from the degenerate c = 0. Positivity is exactly the demand that the factor lie in the class −1 instead of +1.

*Proof.* hh′ = 1 + Nm (Ptolemy); h ≡ −1 (mod m), and c = (h + 1)/m < 0 ⟺ h ≤ −1 − m. The ∞-factor is
y5_general_r_jacobi Thm 1. ∎

**Prop 2 (dictionary; relabelling).** The same split appears in the e-slice form −1 ∈ Σ_e(N) = {ab⁻¹ mod e : ab | N}.
* Σ_e(N) always contains 1.
* Under the Artin map (ℤ/e)* ≅ Gal(ℚ(ζ_e)/ℚ), the element −1 is complex conjugation c_∞.
* The wide ray class group mod e is (ℤ/e)*/{±1}, the Galois group of the maximal real subfield ℚ(ζ_e)⁺. There the
  slice condition "−1 ∈ Σ_e(N)" becomes "1 ∈ Σ_e(N)", which is trivially true.
* So **the entire ES slice condition is the kernel of narrow → wide: it asks for a divisor ratio whose Artin symbol in
  ℚ(ζ_e)/ℚ is complex conjugation**, i.e. a divisor ratio that "splits like the real place".

T1 at squares, in this language (reading, Assessment): the ratios a/b of divisors of a square-shaped N never hit c_∞. This is the product
formula once more (Hilbert reciprocity has an ∞-factor exactly because c_∞ is nontrivial in the narrow group).

## Literature
* Narrow vs wide ray class groups and the Artin map for ℚ(ζ_e): Neukirch, *Algebraic Number Theory*, VI §1.
* WINDMILL_REDUCTION ((J)5) already noted that "ray class groups mod t see it fully, which is an equivalent
  restatement". This memo specifies *which* element: the archimedean one.
* CHI_FLIP Thm 1.1 (sign = −ε₂). FRIEZE §3 (positivity).

## Barrier screen
* This is a relabelling, so B2 is unchanged: we still need one divisor ratio in a prescribed class.
* What it does say is sharper steering. Any mechanism that only sees the wide ray class group (equivalently ℚ(ζ_e)⁺,
  or real-quadratic/totally real data, or unsigned friezes) is ES-blind by construction. It must see c_∞.
* Chebotarev cannot produce divisors of a fixed N. A "complex-conjugation Chebotarev" for divisors (in the spirit of
  the Frobenius-firing programme (J)34) would be H-A.
* T1: respected (product formula).

## Cheap numerics
* The ∞-factor formula: `scripts/y5_general_r.py` (i′), 65 589 signed words, 0 failures.
* Prop 1 is the r = 3 case of that check with c, s < 0, together with the elementary residue computation.

## Assessment
PROVED dictionary, a relabelling. Its value is diagnostic. The archimedean bit that makes ES hard is the element −1
(complex conjugation) in the narrow ray class group mod e. The wide image of the slice condition is trivially true (PROVED), so an object that only sees the wide group cannot
detect it (Assessment).
This unifies:
* FRIEZE §3 (positivity),
* y5_general_r_jacobi (s_∞ = Maslov count),
* the Type I/II "f ≡ −1" congruences (which are "f ≡ c_∞").
