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
*Proof.* The image is cyclic of order dividing g := gcd(h^s + 1, h^t − 1). Let o be the order of h in (ℤ/g)^*:
h^t ≡ 1 gives o | t, h^{2s} ≡ 1 gives o | 2s, so o | gcd(t, 2s) = gcd(t, s) (t odd), hence o | s and h^s ≡ 1;
with h^s ≡ −1 this gives g | 2. ∎ (Numerically: gcd(h^s + 1, h^t − 1) = 2 for all odd h < 200, s ≤ 6, odd t ≤ 7.)
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

(I3) Second construction: force "4cd | ord" by an algebraic identity (the GL₂ analogue of Mordell's polynomial
identities): a family (E_b, R_b) over a curve B → 𝔸¹_t (t = p) whose point R_{b} reduced at every prime dividing the
shot value p + 4c²d has order divisible by 4cd; at supersingular such primes this gives 4cd | h + 1 for free.

**Proposition 3.3 (identity forcing is bounded by uniform boundedness; PROVED relative to Merel and to the
existence of primitive divisors of elliptic divisibility sequences).** Let F be a number field of degree D, E/F an
elliptic curve, Q ∈ E(F), m ≥ 2. Suppose m | ord(Q mod 𝔥) for all but finitely many primes 𝔥 of F (of good
reduction, Q integral at 𝔥). Then Q is a torsion point whose order is divisible by m, so E(F) has a point of order
m and m ≤ B(D) (Merel's bound); for D = 1, m ∈ {2, …, 10, 12} (Mazur), for D = 2, m ≤ 18 (Kamienny–Kenku–Momose).
Application: if a family (E_b, R_b) over B (with [ℚ(B) : ℚ(t)] = D) forces 4cd | ord(R_b mod 𝔥) at all primes
𝔥 | p + 4c²d (all p, b over t = p), then specialising at a point b₀ over t = −4c²d (where the shot value vanishes;
any prime 𝔥 | p + 4c²d has b ≡ b₀ mod 𝔥 for a suitable b₀) gives Q = R_{b₀} ∈ E_{b₀}(ℚ(b₀)) satisfying the
hypothesis (granted good reduction of the family at b₀), so 4cd ≤ B(D). **A fixed algebraic family forces only
finitely many slices (c, d)**; with D = 1: 4cd ∈ {4, 8, 12}, the moduli of Mordell's classical identities.
*Proof.* If Q has infinite order, the elliptic divisibility sequence of Q has a primitive prime divisor 𝔥_n in the
denominator of nQ for all n ≥ n₀ (Silverman 1988 over ℚ; Cheon–Hahn 1999 over number fields — citation from
memory, not re-checked); then ord(Q mod 𝔥_n) = n, and n ranging over integers prime to m gives infinitely many
𝔥 with m ∤ ord: contradiction. So Q is torsion of order n₀, and ord(Q mod 𝔥) = n₀ for all 𝔥 ∤ n₀·(bad), so
m | n₀ and (n₀/m)·Q has exact order m. Merel/Mazur/KKM. ∎
*Scope / hypothesis that would have to fail (Assessment).* (a) A FIXED family: the slice set it serves is finite,
so B2 (redteam-automorphic-2 Thm 2.2(iii), conditional on H) applies. (b) Families of degree D growing with the
slice: a point of order N on a CM curve needs [F : ℚ] ≫ φ(N)/log log N (Silverberg; Clark–Pollack — from memory),
and the family then is just ℚ(E[N])-level data, whose Frobenius at supersingular h is cyclotomic (Cor 2.2). So
torsion forcing either serves finitely many slices or reduces to the cyclotomic condition with moving level.
(c) Forcing at a SUBSET of the primes dividing the shot value (those with Frobenius in some class) is no longer an
identity: it is a Kummer condition on a non-torsion point — positive-density but not forced, the lottery.

(I4) Third construction: an infinite tower (Iwasawa ℤ_ℓ-towers, the torsion tower ℚ(E_tors), Kummer towers
ℚ(E[∞], ∞⁻¹P)), where the (J)34 hypothesis "finite L" fails. What survives?

**Proposition 3.4 (profinite extension of the (J)34 no-go; PROVED, elementary).** Let L/ℚ be Galois (possibly
infinite), G = Gal(L/ℚ) with Haar probability μ, C ⊂ G closed and conjugation-stable, and
P_C := {h unramified in L : Frob_h ⊂ C}.
(a) If C has non-empty interior, P_C has positive lower Dirichlet density. Hence if P_C ⊆ Fire(p) (finite;
FROBENIUS_FIRING Prop 1.2), then int C = ∅; if moreover C is Jordan-measurable (μ(∂C) = 0), then μ(C) = 0.
(b) If L contains an infinite abelian extension of ℚ, there exist closed conjugation-stable C with μ(C) ≥ 1 − ε and
P_C = ∅. So "positive measure" is NOT the right threshold: a sufficient tower condition can have positive measure,
but then no equidistribution theorem (Chebotarev at finite level, Serre's ℓ-adic Chebotarev for Jordan-measurable
sets, Hooley/Lenstra-type GRH theorems for Artin-type sets) can show P_C ≠ ∅ without showing P_C infinite.
*Proof.* (a) int C ⊇ gU for an open normal U = Gal(L/L_U), L_U/ℚ finite Galois; being conjugation-stable, int C
contains the full preimage of the conjugacy class of gU in Gal(L_U/ℚ), and finite Chebotarev gives density ≥
1/[L_U : ℚ]. Finiteness of Fire(p) forces int C = ∅; then C = ∂C (C closed), so Jordan-measurability gives μ(C) = 0.
(b) Every conjugacy class K maps to a single point of the infinite abelian quotient Gal(L^{ab'}/ℚ), whose fibres are
Haar-null, so μ(K) = 0. Enumerate the countably many classes K_1, K_2, … of Frobenius elements; K_i is closed, so
K_i = ∩_V K_i V over open normal V, and μ(K_i V) ↓ 0; choose V_i with μ(K_i V_i) < ε 2^{−i}. Then
C := G \ ∪_i K_i V_i is closed, conjugation-stable (each K_i V_i is), μ(C) ≥ 1 − ε, and contains no Frobenius. ∎
*Iwasawa towers specifically (PROVED).* (i) Cyclotomic ℤ_ℓ-tower: Frob_h = h ∈ 1 + ℓℤ_ℓ (ℓ odd), a cyclotomic
condition. (ii) Anticyclotomic ℤ_ℓ-tower K^{ac} of an imaginary quadratic K (Gal(K^{ac}/ℚ) ≅ ℤ_ℓ ⋊ {±1},
dihedral): for h inert in K, Frob_h restricts non-trivially to K, so its decomposition group is generated by a
reflection, of order 2: **hO_K splits completely in K^{ac}** and the tower carries no information at inert h.
(iii) Division towers ℚ(E[ℓ^∞]) of any E at supersingular h: Prop 2.1. So every ℤ_ℓ-tower attached to the CM
structure sees an inert (= supersingular) certificate prime h only through h mod ℓ^∞ — i.e. exactly the ℓ-part
of the ES modulus condition h ≡ −1 (mod 4cd), and nothing of the divisibility h | p + 4c²d.
*Which (J)34 hypothesis is violated, and what replaces it (Assessment).* (J)34 Prop 1.2 needs L finite. In a tower
the escape is int C = ∅ (necessary by (a)); then existence of a firing h must come from a DENSITY-ZERO existence
mechanism, not from equidistribution. The known such mechanisms are: Elkies' supersingular primes (a CM value
with a sign argument), primitive divisors (Zsigmondy, Bilu–Hanrot–Voutier for Lucas, Silverman for EDS), and
sign/parity of a norm (Mordell's p + 4 ≡ 3 mod 4). §3.5 screens these.

(I5) Fourth construction: the density-zero existence mechanisms named in Prop 3.4.

**Proposition 3.5 (torus version of Prop 3.3: primitive divisors couple to the shot only through roots of
unity; PROVED, Kronecker).** Let α_t, β_t be the roots of x² − P(t)x + Q(t),
P, Q algebraic functions of t of degree ≤ D over ℚ(t), and N := 4cd. Suppose the family forces "ord(α/β mod h) = N"
at the primes h | p + 4c²d by an identity, i.e. U_N(α_t, β_t) vanishes at t₀ = −4c²d while U_n(α_{t₀}, β_{t₀}) ≠ 0
for n < N (α_{t₀} ≠ β_{t₀}). Then α_{t₀}/β_{t₀} is a primitive N-th root of unity in a field of degree ≤ 2D, so
φ(N) ≤ 2D; for D = 1, N ∈ {3, 4, 6}, so 4cd = 4 (Mordell's p + 4).
*Proof.* U_N(α, β) = (α^N − β^N)/(α − β) vanishes at t₀ iff (α/β)^N = 1 (α ≠ β); minimality gives primitive order N;
[ℚ(ζ_N) : ℚ] = φ(N) ≤ [ℚ(α_{t₀}, β_{t₀}) : ℚ] ≤ 2D. ∎
So the Lucas / Bilu–Hanrot–Voutier supply of primes h ≡ ±1 (mod N) (primitive divisors of U_N, with sign
(Δ/h)), and its elliptic analogue (primitive divisors of division-polynomial values Ψ_N(a) of a CM curve, which at
inert h satisfy N | h + 1 up to the 2-part — the reason Prop 3.3 applies), are deterministic sources of primes in
the moving class −1 (mod N), **but the coupling to the shot value p + 4c²d is either an identity (Props 3.3/3.5:
bounded N) or a coincidence (a lottery, B3)**. The sign mechanism (Mordell; Elkies' supersingular-prime argument is
of the same kind: a norm value whose sign forces an inert prime factor) forces one quadratic character: as in
bsD_artin_conjugation / LDP_DEEP §A, this gives h ≡ −1 (mod M) only when (ℤ/M)^* is {±1} (M ∈ {3, 4, 6}), or over
ℚ(ζ_M)⁺ for data that are already F-rational (LDP_DEEP Prop A.4.1, the "split part" lottery).
**Elkies + torsion (Assessment).** Elkies' mechanism gives supersingular h for a non-CM E (density zero!), and a
rational N-torsion point then gives N | h + 1; but N ≤ 12 (Mazur), and h | p + 4c²d is again an identity (Prop 3.3)
or a lottery. Over ℚ, Elkies + Mazur + Mordell's sign reproduce exactly the bounded-modulus shots.

## 4. Scope of the prime-modulus dictionary, and a dictionary at p itself

**4.1 Prime moduli do not always exist (EVIDENCE, exhaustive).** Prop 1.2 and every supersingular statement above
concern a PRIME modulus h (for composite h, ℤ/h is not a field and E_0(ℤ/h) = ∏ E_0(F_{h_i}) has order
∏(h_i + 1) only if every h_i ≡ 3 (mod 4)). `scripts/tf_primemod.c P H0` (stage 1: mark p ≡ −c/j (mod h) for all
prime h ≤ H0 and cj | (h + 1)/4; stage 2: exhaustive enumeration of ALL Type II solutions of the unmarked p via
x ∈ ((p+1)/4, p/2], e = 4x − p, δ | x², modulus h = 4y′ − 1):
* **p = 3361 is the only prime 5 ≤ p ≤ 10⁷ with no Type II certificate of prime modulus.** It has exactly 4 Type
  II solutions, with moduli 99 = 3²·11, 679 = 7·97, 1159 = 19·61, 33639 = 3·11213 (cross-checked by an independent
  Python divisor search); 679 and 1159 have a prime factor ≡ 1 (mod 4), i.e. split in ℚ(i) (ordinary for E_0).
  (data/tf/primemod_1e6.txt, primemod_1e7.txt; LDP_DEEP §A.4 met 3361 too, in the cd ≤ 30 window.)
* T1 control: all 1580 odd squares ≤ 10⁷: 0 Type II solutions with gcd(x, n) = 1.
* Torsion side, independent code (`scripts/tf_torsion_side.c 10⁶ 20000`): for 78 495 of the 78 496 primes
  5 ≤ p ≤ 10⁶ a prime h ≤ 20 000 and a 2-torsion point (x_T, 0) of y² = x³ + pd·x over F_h with 2d | x_T,
  2x_T | h + 1 was found, and the resulting ES solution (Lemma 1.1 of FIXED_MODULUS_SHOTS) verified exactly in
  128-bit arithmetic; the exception is 3361 (searched to h ≤ 2·10⁵); 0 odd squares fire.
So "ES via supersingular reduction at one prime" is, in the data, ES minus one prime; any theorem must also
handle composite moduli or Type I (3361 has Type I solutions: ES holds there).

**Proposition 4.2 (the Hasse-interval dictionary at p itself; PROVED, Deuring–Waterhouse).** Let p ≥ 5 be prime.
(a) For c, d ≥ 1 with 4c²d − 1 ≤ 2√p there is an elliptic curve E/F_p with trace a_p(E) = 1 − 4c²d, hence
#E(F_p) = p + 4c²d, and: (p has a Type II certificate on the slice (c, d)) ⟺ (E(F_p) has a subgroup of order
h ≡ −1 (mod 4cd)).
(b) For 1 ≤ c ≤ 2√p + 1 there is E/F_p with a_p(E) = 1 − c, #E(F_p) = p + c, and (p has a cube point (c, d, 1)
for some d) ⟺ E(F_p) has a subgroup of order h ≡ −1 (mod 4c).
(c) c = 1 in (b) is the supersingular spine: a_p = 0, #E(F_p) = p + 1 ((J)35, CONSTRUCTIVE_ES Cor 3.3).
*Proof.* Deuring/Waterhouse: every integer a with |a| ≤ 2√p and p ∤ a is the trace of an (ordinary) curve over F_p,
and a = 0 occurs (supersingular, p ≥ 5). A finite abelian group has subgroups of every order dividing its order.
(a) is FIXED_MODULUS_SHOTS Lemma 1.1 on the (c, d) line (h | p + 4c²d, h ≡ −1 mod 4cd, any h); (b) the (c, j) line
with j = 1: h | p + c, h = 4cd − 1. ∎
**EVIDENCE (`scripts/tf_hasse.c`, all primes 5 ≤ p ≤ 10⁸, 6.8 s; data/tf/hasse_1e8.txt).** Every prime has a
certificate of type (a) or (b): (a) fails only at p = 193; (b) fails at exactly 23 primes, 7, 31, 79, 127, 199, 409,
577, 2719, 5569, 8191, 9601, 23929, 83449, 102001, 329617, 712321, 861199, 1134241, 1724209, 1726201, 5212561,
6266527, 8813281 (none in (8.9·10⁶, 10⁸]); never both. The odd squares ≤ 10⁸ (4999): 0 of either kind (T1).
So, empirically, **ES(p) is witnessed by an elliptic curve over F_p itself**: some E/F_p of trace a ≤ 0 (in the
Hasse window) has a subgroup whose order is ≡ −1 modulo 4(1 − a) (b) or modulo 4cd with 1 − a = 4c²d (a).
**Proposition 4.3 (the window (b) is the whole j = 1 face; PROVED).** For a prime p ≥ 5 the following are
equivalent: (i) (b) of Prop 4.2 holds for some c ≤ 2√p + 1; (ii) the cube has a point (c, d, 1) (any size);
(iii) for some d ≥ 1, 4dp + 1 has a divisor h ≡ −1 (mod 4d).
*Proof.* (i) ⇒ (ii) is Lemma 1.1 with j = 1, and (ii) ⇔ (iii) is Lemma 1.1's h | pj + c ⟺ h | 4dj²p + 1 with
h = 4cd − 1. (iii) ⇒ (i): N := 4dp + 1 ≡ 1 (mod 4d), so the cofactor N/h ≡ −1 (mod 4d) as well; let h₀ be the
smaller of h, N/h, so h₀ ≤ √N. Put c := (h₀ + 1)/(4d) ∈ ℤ_{≥1}: h₀ = 4cd − 1 | 4dp + 1, hence h₀ | p + c, and
c ≤ (√(4dp + 1) + 1)/(4d) < 2√p + 1. ∎ (`scripts/tf_jface.c 10⁵`: (i) and (iii) agree on all 9590 primes
5 ≤ p ≤ 10⁵, data/tf/jface_1e5.txt.) So the Hasse-window restriction in (b) costs nothing: every j = 1
certificate pairs with one inside the window — the Hasse bound |a| ≤ 2√p is the divisor-pairing bound h₀ ≤ √N.
*Reading (Assessment).* By Lenstra's theorem E(F_p) ≅ End(E)/(π − 1) (ordinary E), the subgroups stable under
End(E) are ideals above (π − 1), whose norms are the divisors of p + 1 − a split in ℚ(√(a² − 4p)); the condition
"order ≡ −1 modulo a function of the trace" again couples a group order to an arithmetic progression of moving
modulus. The window is a lottery over ≍ √p traces with ≍ log p tickets each (expected count ≍ log² p); it is
not a mechanism, but it is a natural single-field home for the ES lottery (all tickets are point counts over the
same F_p), which may be useful to the (J)35 isogeny-graph line.

## 5. Barrier screen: where each dictionary fails at odd squares, and which barrier it meets

**Proposition 5.1 (T1 inside the torsion dictionary; PROVED).** Let n be odd, d ≥ 1, h prime with
h ≡ −1 (mod 4d), h ∤ nd. Then E_{nd}(F_h) is non-cyclic (has full 2-torsion) iff (n/h) = −1. In particular for
n = m² every candidate curve E_{m²d} is cyclic at every candidate modulus, so the object of Prop 1.2(b) (a
2-torsion point T ≠ (0, 0)) does not exist: the dictionary fails at squares at the GROUP-STRUCTURE step.
*Proof.* (d/h) = +1 for h ≡ −1 (mod 4d) (the Kronecker character (d/·), d > 0, has period dividing 4d and value +1
at −1), and (−1/h) = −1. Lemma 1.1(a): non-cyclic iff (nd/h) = −1 iff (n/h) = −1; (m²/h) = +1. ∎
So the quadratic (genus) layer is exactly the 2-torsion of the supersingular group; it is the only part of the
firing condition that Galois data at h see (Thm 3.1: the overlap of the (h + 1)- and (h − 1)-worlds is {±1}), and it
is the part that kills squares. The rest (x_T read as an integer, 2x_T | h + 1) is B2.

| step / dictionary | Galois-visible content | barrier met |
|---|---|---|
| Prop 1.2 (2-torsion of E_{pd} at prime h) | (pd/h) = −1 (non-cyclicity) | T1 at the group-structure step (Prop 5.1); the integer x_T ∣ (h+1)/2 is B2 |
| Prop 2.1/Cor 2.2 (division fields, any curve) | h mod ℓ^∞ only | moving cyclotomic level (FROBENIUS_FIRING §2, Rem 2.5) |
| Thm 3.1/Cor 3.2 (Kummer / mute transport) | a sign | firing set ≤ 2τ₃(k): below every Weil/Chebotarev threshold (B3) |
| Prop 3.3/3.5 (identities) | torsion/root of unity at the shot zero | Merel/Mazur/Kronecker: finite slice set (B1/B2(iii)) |
| Prop 3.4 (towers) | int C = ∅ needed | density-zero existence only; equidistribution gives B6-type averages |
| §3.5 (sign/primitive divisors) | one quadratic character | bsD_artin_conjugation, LDP_DEEP §A (genus, T1-exact) |
| Prop 4.2/4.3 (curves over F_p) | none (a lottery over ≍ √p traces) | B3 (expected count ≍ log² p) |

## 6. Verdict (O207 checkpoint 1)

ES is not proved here, nor any infinite case. Outcome: the fallback — a scoped no-go for the GL₂ point-order
class — plus three exact dictionaries and two new numerical facts.
1. (PROVED) Exact dictionaries: Type II firing at a prime h ⟺ a 2-torsion point of y² = x³ + pd·x over F_h with
   x-coordinate 2cd and 2x_T | h + 1 (Prop 1.2); ⟺ cd | #2E_0(F_h) with h | p + 4c²d; per-modulus, firing reads
   only det = N(π_p) of the CM Frobenius of p on E_0[h] (Prop 2.3); at p itself, small-slice and j = 1 certificates
   are subgroups of order ≡ −1 (mod (1−a)/c) resp. (mod 4(1−a)) in E(F_p) for curves of trace a ≤ 0 in the Hasse window
   (Props 4.2, 4.3).
2. (PROVED) Cyclotomic collapse: at a supersingular prime the ℓ-adic Frobenius (ℓ odd) of ANY elliptic curve is the
   companion matrix of x² + h, so every torsion/group-structure condition is cyclotomic (Prop 2.1, Cor 2.2);
   ℤ_ℓ-towers attached to the CM structure (cyclotomic, anticyclotomic — inert primes split completely —, division
   towers) see a certificate prime only through h mod ℓ^∞.
3. (PROVED) Torsion–residue orthogonality (Thm 3.1): groups of exponent dividing h^s + 1 (supersingular points,
   the non-split torus, Weil-pairing values) map to F_{h^t}^* (t odd) only through {±1}. Hence the GL₂ analogue of
   the FF_MUTE mute place amplifies a firing set by at most a factor 2 (Cor 3.2). This is the precise reason the
   task's "finitely generated group of points reduced mod f" cannot play the role of ⟨s⟩: ⟨s mod f⟩ lives in the
   (f − 1)-world with p, points live in the (f + 1)-world with the divisors.
4. (PROVED rel. Merel / primitive divisors / Kronecker) Identity forcing of point orders serves finitely many slices
   (Props 3.3, 3.5); with D = 1 exactly Mordell's moduli 4cd ∈ {4, 8, 12} (resp. 4).
5. (PROVED, elementary) Profinite extension of (J)34 (Prop 3.4): in an infinite tower a sufficient Frobenius
   condition must have empty interior (and measure zero if Jordan-measurable); positive-measure sufficient
   conditions exist but are useless (no equidistribution theorem can produce a hit without producing infinitely
   many). The violated (J)34 hypothesis (finite L) only moves the problem to density-zero existence mechanisms,
   which (§3.5) are identities (bounded) or one quadratic sign (genus/T1).
6. (EVIDENCE) p = 3361 is the unique prime ≤ 10⁷ with no prime-modulus Type II certificate (so any
   "supersingular reduction at one prime" route must also handle composite moduli or Type I); every prime
   5 ≤ p ≤ 10⁸ has a Hasse-window certificate (Prop 4.2 (a) or (b)); odd squares: none (T1).
