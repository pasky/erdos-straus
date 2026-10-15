# s6_mixed_points_cuberoots — a uniform reading of sterility: menus, not points (O238; mandatory (v))

## Idea
Three "sterility" phenomena of the campaign: (a) FF root-product law (FF_ODD_ABSENCE, branch side-agent/ff-odd-absence:
E(0)^s = ±1 via Weil reciprocity on P¹ for T and W/C), (b) ℤ window forcing (quadratic reciprocity puts −1 in ⟨primes of x⟩),
(c) mixed profinite points of 4^s + 105 ((J)62) and sterile Mordell points ((J)54). Proposed dictionary: each is a
reciprocity law *on the class menu*: (a) a product formula over the roots of V constrains the slice value; (b) the
product formula for the Hilbert symbol (n, q) constrains the subgroup; (c) [R245 repair: withdrawn as stated — μ* itself lies in the ET class II2 (2, 23, 919) and no sterile point on Λ₁₀₅ is known
((J)62); what (c) can say is that the ET search *stalled* near μ*, a cost statement about the menu {n mod M}]. The 105 resolution (s6_exp_classes_105) is the ℤ-analogue of (a): a factorisation
of the *moving* integer 4^r + 1 into cyclotomic pieces (the ℤ shadow of "roots of V": 4^{3g} + 1 = (4^g + 1)(4^{2g} − 4^g + 1))
whose residues are periodic — exactly what Weil reciprocity exploits over F_q[T].

## Literature
Weil reciprocity (Serre, *Algebraic Groups and Class Fields* III §4); Hilbert reciprocity; cyclotomic factorisation of
bⁿ ± 1 (Brillhart–Lehmer–Selfridge–Tuckerman–Wagstaff 1988). (J)54 STERILE_EXPLICIT, (J)56 FF_STERILE_SMALL.

## Barrier screen
For primes p no algebraic factorisation of (p + m)/4 is available (p is not a value of a fixed exponential/polynomial
in a free parameter): B2 returns. The dictionary is therefore family-level (H-A: moving modulus via algebraic factors).
T1: n = a² excluded by the global Lemma-1.1 T1 [R246 repair: AND by a congruence — (n_s/18837001) = −1 for all s ≡ 34
(mod 45), 18837001 | 4⁴⁵ − 1; only the larger cubic family u ≡ 32 (151) is congruence-wise square-compatible, e.g. at
n ≡ 59 (mod 151), a residue] — the global Lemma-1.1 T1 of CAP_DOWN §3 ((J)66; R245 repair: not new; on the family itself 4^s + 105 is a square only for s = 2, 3, 4).

## Cheap numerics
s6_expclass_pts.py: every residual (J)62 exponent ≤ 8000 tested is in an exp class. The mixed point μ* (4 at ℓ ≠ 3, −2 at
ℓ = 3) lies in s ≡ 34 (mod 45), the exp class's exact domain.

## Assessment
Dictionary (Assessment); the 105 instance PROVED. Conjecture-level spark: (J)54's sterile Mordell points over ℤ are sterile
for fixed-modulus ET menus only; on any family carrying a moving algebraic factorisation they may be non-sterile. Untested
for primes (where no such family exists) — so not an ES route.
