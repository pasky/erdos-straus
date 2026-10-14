# TORSION_FIRING — ES firing as point orders on CM supersingular curves (task O207, wave Y-d)

Status: in progress (O207). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on FROBENIUS_FIRING.md ((J)34; esp. §3 (F1) Heegner and (F2) supersingular-torsion dictionaries and the
no-go Prop 1.2 / Thm 1.4), FF_MUTE.md ((J)30), FIXED_MODULUS_SHOTS.md (Lemma 1.1 cube, Thm 3.1 box),
CONSTRUCTIVE_ES.md ((J)35), bsD_artin_conjugation / LDP_DEEP §A (the class −1 is complex conjugation).
Scripts `scripts/tf_*`.

Notation. p odd prime; h a prime ≡ 3 (mod 4), h ∤ p, k := (h + 1)/4; Box(k) := {c/j : c, j ≥ 1, cj | k} ⊂ F_h^*.
Type II fires at h ("(p, h) ∈ Fire_II") iff −p mod h ∈ Box(k) (FIXED_MODULUS_SHOTS Thm 3.1), equivalently iff
∃ c, d ≥ 1 with 4cd | h + 1 and h | p + 4c²d (Lemma 1.1 there: h = 4cdj − 1, h | pj + c ⟺ h | p + 4c²d).

## 0. Iteration log

(I1) The literal dictionary of the task (divisors of h + 1 = orders of subgroups of a supersingular E(F_h)) is
already FROBENIUS_FIRING (F2), dismissed there because "m | h + 1" is cyclotomic. §1 makes it exact and adds a
p-twisted version in which p itself enters the curve (2-torsion x-coordinates); §2 proves the cyclotomic collapse
for every curve (not only CM), and isolates what is NOT cyclotomic: point orders of a fixed global point (Kummer).

## 1. The exact dictionary (PROVED; checked numerically, §5)

**Lemma 1.1 (group structure).** Let h ≥ 5 be prime.
(a) If h ≡ 3 (mod 4) and h ∤ D, the curve E_D : y² = x³ + Dx has #E_D(F_h) = h + 1, and
E_D(F_h) ≅ ℤ/(h + 1) if (D/h) = +1, E_D(F_h) ≅ ℤ/2 × ℤ/((h + 1)/2) if (D/h) = −1.
In particular E_0 : y² = x³ − x has E_0(F_h) ≅ ℤ/2 × ℤ/2k and 2E_0(F_h) ≅ ℤ/k (k = (h + 1)/4).
(b) If h ≡ 2 (mod 3) and h ∤ 6B, E^B : y² = x³ + B has E^B(F_h) ≅ ℤ/(h + 1) (always cyclic).
*Proof.* (a) f(x) = x³ + Dx is odd and −1 is a non-square mod h. For each of the (h − 1)/2 pairs {x, −x}, x ≠ 0:
if f(x) ≠ 0 exactly one of f(±x) is a non-zero square (2 points); if f(x) = 0 we get (±x, 0) (2 points). With
(0, 0) and O: #E_D(F_h) = (h − 1) + 2 = h + 1. Write E(F_h) ≅ ℤ/m × ℤ/n, m | n; the Weil pairing gives
μ_m ⊂ F_h^*, so m | h − 1, and m | n gives m² | h + 1, so m | gcd(h − 1, h + 1) = 2. The 2-torsion points are
(0, 0) and (x, 0) with x² = −D: these exist iff (−D/h) = 1 iff (D/h) = −1 (as (−1/h) = −1). So m = 2 iff
(D/h) = −1. For E_0, D = −1 is a non-residue. 2E(F_h) is cyclic of order (h + 1)/4 when m = 2.
(b) x ↦ x³ is a bijection of F_h (3 ∤ h − 1), so x ↦ x³ + B is a bijection and each y gives one x: h points
plus O. The only 2-torsion point has x = (−B)^{1/3}: m is odd, m | gcd(h − 1, h + 1) ⇒ m = 1. ∎
(Standard; e.g. Silverman AEC V.4 / Waterhouse; the group-structure statement m | gcd(h − 1, h + 1) is Schoof's
lemma for supersingular curves with a_h = 0.)

**Proposition 1.2 (Type II firing as torsion data; PROVED).** Let p be an odd prime and h ≡ 3 (mod 4) a prime,
h ∤ p.
(a) (universal curve) (p, h) ∈ Fire_II ⟺ ∃ c, d ≥ 1 with cd | #2E_0(F_h) and h | p + 4c²d.
Equivalently: 2E_0(F_h) ≅ ℤ/k contains a subgroup of order cd with h | p + 4c²d.
(b) (p-twisted curves) For d ≥ 1 with h ∤ d put E_{pd} : y² = x³ + pd·x. Then for c ≥ 1:
h | p + 4c²d ⟺ T = (2cd, 0) ∈ E_{pd}(F_h)[2]. Whenever some such T exists, (pd/h) = −1 and
E_{pd}(F_h) ≅ ℤ/2 × ℤ/((h + 1)/2). Hence
`(p, h) ∈ Fire_II ⟺ ∃ d ≥ 1, h ∤ d, and a 2-torsion point T ∈ E_{pd}(F_h) \ {(0,0)} whose x-coordinate has an
integer representative x_T ∈ [1, h) with 2d | x_T and 2·x_T | #E_{pd}(F_h).`
For d = 1: **Type II with d = 1 fires at h iff the curve y² = x³ + px has a non-trivial F_h-rational 2-torsion
point (x_T, 0) with x_T even and 2x_T | h + 1** (then c = x_T/2).
(c) (the other twist) With (pd/h) = −1, the twist E_{−pd} : y² = x³ − pd·x has E_{−pd}(F_h) ≅ ℤ/(h + 1) cyclic.
*Proof.* (a) Lemma 1.1(a): 4cd | h + 1 ⟺ cd | k = #2E_0(F_h), and ℤ/k has a subgroup of order cd iff cd | k.
(b) x³ + pd·x at x = 2cd equals 2cd(4c²d² + pd) = 2cd²(p + 4c²d), and h ∤ 2cd when 4cd | h + 1 (then
0 < 2cd < h); in general (h ∤ 2cd assumed); so (2cd, 0) is on E_{pd} mod h iff h | p + 4c²d. Then −pd ≡ 4c²d² is a non-zero square, i.e.
(pd/h) = −1, and Lemma 1.1(a) gives the structure. For the displayed equivalence: given (c, d), x_T = 2cd < h,
2d | x_T, 2x_T = 4cd | h + 1. Conversely, x_T = 2cd with c := x_T/(2d) ≥ 1, and x_T must be the x-coordinate of
a 2-torsion point other than (0,0), i.e. x_T² ≡ −pd, i.e. h | d(p + 4c²d), i.e. h | p + 4c²d (h ∤ d).
(c) (−pd/h) = +1, Lemma 1.1(a) with D = −pd. ∎
*Reading (Assessment).* (b) puts p into the curve: the firing datum c is the (reduced) x-coordinate of a 2-torsion
point of a CM curve with CM by ℤ[i], and the ES modulus condition says that this coordinate, read as an integer,
divides the exponent (h + 1)/2 of the group. This is the box again (c is an *integer* and an *order* at the same
time); the mixed role — a field element (x-coordinate, tangent-space value) that must equal a group order — is the
recurring shape of every dictionary below.

*Check (`scripts/tf_dict.py 2000 600`, EVIDENCE for the proved statements):* Lemma 1.1 on 1994 (h, curve) cases
(h < 2000; D ∈ {±1, ±2, 3, 5, −7, 11}, B ∈ {1, 2, −3, 5, 7}; brute-force point count and exponent): 0 failures.
Prop 1.2(b): box criterion vs 2-torsion criterion on all 162 095 pairs (n, h), n an odd prime ≤ 600 or an odd
square ≤ 600, h ≡ 3 (4) prime ≤ (n + 1)(n + 5)/4, h ∤ n: 0 mismatches; every prime fires somewhere, no odd square
fires anywhere (T1).
