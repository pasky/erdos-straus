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

## 2. What Frobenius at a supersingular prime can see: the cyclotomic collapse (PROVED)

**Proposition 2.1 (supersingular Frobenius is cyclotomic, ℓ odd).** Let E/ℚ be any elliptic curve (CM or not),
h ≥ 5 a prime of good supersingular reduction (a_h(E) = 0), ℓ an odd prime ≠ h, and
ρ = ρ_{E,ℓ^∞} : G_ℚ → GL₂(ℤ_ℓ). Then ρ(Frob_h) is GL₂(ℤ_ℓ)-conjugate to the companion matrix
`F_h = [[0, −h], [1, 0]]`. Hence for every GL₂(ℤ_ℓ)-conjugation-stable set C ⊂ GL₂(ℤ_ℓ), the truth of
"ρ(Frob_h) ∈ C" at supersingular h is a function of h ∈ ℤ_ℓ^* alone, i.e. of Frob_h in ℚ(ζ_{ℓ^∞}).
*Proof.* The characteristic polynomial of F := ρ(Frob_h) is x² − a_h x + h = x² + h. Its discriminant −4h is a unit
in ℤ_ℓ, so F mod ℓ has two distinct eigenvalues over F̄_ℓ and is not scalar; pick v ∈ ℤ_ℓ² whose reduction is not an
eigenvector of F mod ℓ. Then (v, Fv) is a basis of ℤ_ℓ² (its determinant is a unit), and in it F has matrix
[[0, −det F], [1, tr F]] = F_h. ∎
(ℓ = 2: F mod 2 can be scalar — exactly when E[2] ⊂ E(F_h) — so the 2-adic class carries the extra datum of the
2-torsion field; for E_0 this is Lemma 1.1.)

**Corollary 2.2 (what the torsion tower says about divisors of h + 1).** At a supersingular h ≥ 5 every "torsion"
statement — m | #E(F_{h^r}) for any r, the isomorphism type of E(F_{h^r}), the order of the largest F_h-rational
cyclic subgroup of ℓ-power order, the Galois module E[m] ⊗ F_h — is determined by h modulo (powers of) every odd
ℓ together with the 2-adic class of ρ(Frob_h). In particular, on the supersingular locus, "the ES modulus condition
4cd | h + 1 = #E(F_h)" (Prop 1.2) is the cyclotomic condition Frob_h|ℚ(ζ_{4cd}) = complex conjugation, for EVERY
curve, CM or not, and no choice of curve, level, or tower of division fields changes this.
*Proof.* E[m](F̄_h) as a Frob-module is ρ_{E,m}(Frob_h), determined up to GL₂(ℤ/m)-conjugacy by Prop 2.1 at odd ℓ;
the listed invariants are conjugation-invariant. ∎
*Scope.* This is the sharp form of FROBENIUS_FIRING (F2) "no gain from non-abelian torsion fields": not only do
the conditions have moving level, they are literally cyclotomic on the supersingular locus. The only GL₂-type data
NOT covered by Prop 2.1 are (i) the supersingularity condition a_h = 0 itself (for non-CM E a Haar-null condition,
§3) and (ii) conditions that are not GL₂-conjugation-stable: Kummer/position data of global points
(ℚ(E[m], m⁻¹P), with group inside E[m] ⋊ GL₂(ℤ/m)), and coordinate/Lie values (Prop 1.2(b)), which are not
Galois-theoretic at h at all.

**Proposition 2.3 (the per-modulus flip lands in det; PROVED).** Fix h ≡ 3 (mod 4). For primes p ≡ 1 (mod 4), let
π_p ∈ ℤ[i] be a prime above p. Then E_0 : y² = x³ − x has ρ_{E_0,h}(Frob_p) = multiplication by a unit multiple
u·π_p on E_0[h] ≅ ℤ[i]/h = F_{h²} (u ∈ ℤ[i]^*), and
`(p, h) ∈ Fire_II ⟺ −N_{F_{h²}/F_h}(ρ_{E_0,h}(Frob_p)) ∈ Box(k) ⟺ −det ρ_{E_0,h}(Frob_p) ∈ Box(k).`
The "torus part" π_p/π̄_p ∈ T(F_h) (the norm-one torus, of order h + 1 = 4k, where the divisors of k live as
subgroup orders) is invisible to firing: firing depends on Frob_p only through the cyclotomic quotient ℚ(ζ_h).
*Proof.* Deuring: Frob_p acts on the Tate module of a CM curve by the Hecke character value, a generator of the
prime above p (for E_0: the primary associate of π_p up to the quartic twist character, a unit); E_0[h] is a
free ℤ[i]/h-module of rank 1 and h inert makes ℤ[i]/h = F_{h²}, whose norm to F_h is the determinant. Firing:
FIXED_MODULUS_SHOTS Thm 3.1, and N(uπ_p) = p. ∎
*Reading (Assessment).* The ES box is a subset of the SPLIT torus F_h^* (where p lives) generated by the integer
divisors of #T(F_h)/4, T the NON-SPLIT torus (where the divisors of h + 1 live as orders). F_{h²}^* contains
both, and they meet in {±1}; the CM Frobenius π_p mod h has a component in each, and ES reads only the split one.
The box is the image of the subgroup lattice of the cyclic group T(F_h) (or of 2E_0(F_h) ≅ ℤ/k) under "order ↦ the integer order, reduced
mod h" — a map from a lattice of subgroups of one torus into the other torus that is not a homomorphism of any
algebraic structure (it uses the archimedean integer |A|, cf. Prop 1.2(b)).

## 3. Construction attempts and the scoped no-go theorems

(I2) Construction target. FF_MUTE's mechanism: a fixed finitely generated group ⟨s⟩ ⊂ ℚ^*, reduced mod r, lands in
F_r^* — the SAME group where −p/4 lives — so the firing set −A⟨s²⟩ is a large subgroup coset, Weil/Chebotarev
countable. The GL₂ analogue proposed by the task: replace ⟨s⟩ by a group of points Γ ⊂ E(F) (F a number field,
E CM, Γ global, Heegner, or depending on p) reduced mod h, whose orders divide h + 1 at supersingular h.

**Theorem 3.1 (torsion–residue orthogonality; PROVED, elementary).** Let h be an odd prime and A a finite abelian
group whose exponent divides h^s + 1 for some s ≥ 1 — e.g. any subquotient of E(F_{h^s})^r for E/F_h supersingular
with a_{h^s} = 0 (s odd), of the norm-one torus T(F_{h^s})^r, or of E[h^s + 1]^r. Then for every odd t ≥ 1,
every homomorphism ψ : A → F_{h^t}^* has image in {±1}; and every homomorphism F_{h^t}^* → A has image of order ≤ 2.
*Proof.* The image is cyclic of order dividing g := gcd(h^s + 1, h^t − 1). Modulo g, h^t ≡ 1 and h^s ≡ −1, so
h^{gcd(s,t)} ≡ ... : write e = gcd(s, t) (odd, since t is odd); s/e and t/e are coprime, and h^e has order dividing
both 2s/e (from h^s ≡ −1, i.e. (h^e)^{s/e} ≡ −1) and t/e (from (h^e)^{t/e} ≡ 1) in (ℤ/g)^*; t/e is odd and coprime
to s/e, so the order divides gcd(2s/e, t/e) = 1: h^e ≡ 1 (mod g), hence h^s ≡ 1, and with h^s ≡ −1: g | 2. ∎
**Corollary 3.2 (GL₂-mute rules collapse to a sign; PROVED).** Fix p and h (h ≡ 3 mod 4, h ∤ p) and let Γ_h ⊂ A be
any subgroup (A as in Thm 3.1, t = 1), ψ : A → F_h^* any homomorphism and S ⊂ F_h^* any set. Then
{−p ∈ ψ(Γ_h)·S} = {−p ∈ ±S} or {−p ∈ S}. So a firing rule built by transporting reduced global
points (or torus elements, Heegner points, Weil-pairing values in an odd-degree field) homomorphically to the
residue field of p is at most a factor 2 larger than the seed set S: the "mute amplification" from S to a coset of
an index-2 subgroup, which is what makes FF_MUTE Thm 3.5 work, is impossible with supersingular torsion data.
For S ⊆ −Box(k) (a sufficient rule) the firing set has ≤ 2τ₃(k) = h^{o(1)} elements, below every Weil/Chebotarev
threshold of FROBENIUS_FIRING §2.
*Proof.* Thm 3.1: ψ(Γ_h) ∈ {{1}, {±1}}. ∎
*Where the hypothesis bites (Assessment).* The mute mechanism needs the auxiliary group to share its order with
F_h^* (h − 1); supersingular torsion and the non-split torus have order h + 1, and gcd(h − 1, h + 1) = 2 is exactly
the genus/quadratic layer (the (−p/h) = (d/h) = +1 sign of Prop 1.2(b)). The Weil pairing does reach a large
multiplicative group, μ_{h+1} ⊂ F_{h²}^* — but that is T(F_h) again, which meets F_h^* (where −p lives) in {±1}.
The only bridges from the (h + 1)-world to the (h − 1)-world are therefore non-homomorphic: "order ↦ integer ↦
residue" (Box) or coordinates (Prop 1.2(b)). Both are size/integrality conditions, invisible to Galois data.
