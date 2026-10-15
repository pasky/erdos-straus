# z9_heegner_layers — Frobenius layer t of G_p = supersingular reduction of the CM points of discriminant −4tp on X₀(2); certificate edges = ray-class condition there (O233)

## Idea
Combine z9_frobenius_layers (a path edge with middle letter t lies in layer t: its Eichler order contains ε, ε² = −tp) with
the Gross–Zagier picture of CM points reducing at a ramified prime. In characteristic 0, (E, C) with an embedding
ℤ[√−tp] ↪ End(E, C) is a CM point (Heegner-type point) of X₀(2) of discriminant −4tp. Since p ramifies in ℚ(√−tp), its reduction at
the prime above p is supersingular (R234 repair: needs p ∤ t). So layer t is the image of these CM points, and the path condition becomes a condition on
the CM point. This puts CONSTRUCTIVE_ES ((J)35) and WINDMILL_REDUCTION's ℤ[√−tp] class-group framework (Prop 10.3) on one object.

**Dictionary (PROVED parts as marked).**
(a) (PROVED, algebra.) For a word w = (t, u, v) with χ = −1, inside E = E(L_w): ε = −(1 + ij) has ε² = −tp (CONSTRUCTIVE_ES Cor 3.2).
Also j ⊥ ε (trd(εj̄) = 0), nrd j = A, and i = (1 + ε)j/A. *Check:* j⁻¹ = −j/A, so i = −(1 + ε)j⁻¹ = (1 + ε)j/A. Then
trd(i) = 0 ⟺ trd(εj) = 0, and nrd i = (1 + tp)A/A² = A*.
Converse (review repair: the earlier "iff" dropped the level-t ring condition and was false, e.g. (t, u, v) = (3, 1, 7), p = 13,
with i, j replaced by −i, −j): by CONSTRUCTIVE_ES Cor 2.2(iv), applied to the curve E of the edge, a certificate needs ε with
ε² = −tp, a trace-zero j ⊥ ε with nrd j = A, A | tp + 1, A ≡ −1 (mod t), i = (1 + ε)j/A integral, **and** the level-t ring
condition (1 − i)(1 − j) ∈ t·End E. That condition is not implied by the others. Cor 2.2(iv) is existential over curves, so
this is a sufficient condition attached to a given edge, not an established edge-wise equivalence.
(R234 repair: the sign-flip example is only a data-level failure — the edge is still a certificate via (i, j). Edge-wise: for t = 1
and t an odd prime the conditions without the ring condition already imply a certificate on the edge (sign lemma: for odd ℓ, mod ℓ,
ī ~ diag(1, −1), j̄ = [[−1, y], [z, 1]] with yz = 0, so (1 − i)(1 − j) or (1 + i)(1 + j) ≡ 0; (i, j) ↦ (−i, −j) fixes ε). In general they
do not: p = 61, L = ⟨1⟩ ⊥ [[7, −3], [−3, 10]] (not a path class), t = 4, A = 7, ε = 2ε₁ imprimitive; with ε primitive, failures at
t = 8, 12, 15 (p = 41, t = 15, A = 14; p = 109, t = 12, A = 11). Code: scripts/review_r234_heegner.py.)
(b) (Standard, cited: Deuring lifting; Gross 1987 §§3–4; Gross–Zagier, "On singular moduli".) Pairs ((E, C), ε) with ε ∈ End(E, C),
ε² = −tp, are reductions of CM points of X₀(2) by orders containing ℤ[√−tp]. The weighted count over all edges equals the
optimal-embedding count, an Eichler class-number expression ≍ h(−4tp) (up to bounded local factors at 2 and t; R234 repair: plus the non-optimal terms Σ_{f² | 4tp} h(−4tp/f²)).
(c) (Assessment, matches WINDMILL Prop 10.3's setting.) Write E ⊃ ℤ[ε] ⊕ ℤ[ε]j as in B = K ⊕ Kj, K = ℚ(√−tp). Then the CM point
carries an ideal class 𝔞 ∈ Cl(ℤ[√−tp]) (the class of the ℤ[ε]-module structure), and the condition in (a) reads:
**𝔞 contains an ideal of norm A ≡ −1 (mod t) dividing tp + 1, with the complementary norm A* = (tp + 1)/A.** (R234 repair: given j,
the binary lattice E ∩ ℚ(ε)j trivially represents A; the content is the unproved identification of its class with the CM point's
ideal class.) This is exactly the
residue condition of WINDMILL Prop 10.3 (as a necessary condition; together with the level-t ring condition of (a) it is the certificate condition), which a class function sees only through the genus character (·/ℓ), ℓ | t.

So **the global object on which a "global Fano" would have to act is, layer by layer, the set of CM points of discriminant
−4tp on X₀(2) mod p. The condition to force is a ray-class (mod t) condition on their ideal classes.** The layer itself is
deterministic and class-number sized. The certificate inside it is Prop 10.3's residue event.

## Literature
Gross, "Heights and special values of L-series" (1987), §§1–4 (supersingular reduction of CM points, Brandt matrices);
Gross–Zagier, "On singular moduli" (1985) (reduction at primes dividing the discriminant); Deuring lifting; Elkies,
"Supersingular primes for elliptic curves over real number fields" (reduction of CM points at ramified primes);
WINDMILL_REDUCTION Prop 10.3 + Remark 10.4 (ray classes see the full condition); y1_heegner_level_t (a different Heegner
reading: discriminants −4A, −4A* on X₀(t)).

## Barrier screen
B2 exactly: the modulus t of the ray-class condition is the layer index, which is part of the solution. Prop 10.3: the CM
points of a layer are equidistributed in the genus (Duke/Iwaniec-type equidistribution of Heegner points across
supersingular points as tp → ∞, Michel 2004), and equidistribution sees the genus shadow only. Remark 10.4: a mechanism on ray
classes mod t would see the condition, and here the ray class is attached to a CM point on a modular curve. That is an H-A/H-D
hatch with a concrete object: the action of Gal(ray class field mod t of ℚ(√−tp)) on the layer-t CM points (not pursued;
the field changes with t, which is the moving-modulus problem again). T1: at m² there are no supersingular
reductions (no B_{m²,∞}).

## Cheap numerics
None new. z9_frobenius_layers' table is the layer-1/2 instance (layers 1, 2 = spine, loops; all 9489 edges p ≤ 2000).

## Assessment
Dictionary entry (Assessment, with the algebra in (a) PROVED). It identifies the "global" home of certificates as Heegner-type
CM points on X₀(2) of discriminants −4tp, reduced at the ramified prime p, with a ray-class condition mod t. That is the
cleanest formulation found here of where a global Fano would have to live. It is a precise target for H-A/H-D (ray-class /
Galois data of CM points), not a mechanism. Promise 1/5 (a mechanism would need to control ray classes mod a *varying* t
at fixed p, which no known equidistribution or reciprocity statement does).
