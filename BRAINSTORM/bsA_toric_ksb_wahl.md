# bsA_toric_ksb_wahl — cyclic quotient singularities: QNR certificates are never T-singularities (O174)

## Idea
n/A = [[v,t,u]] ⟺ the cyclic quotient surface singularity X = (1/n)(1,A) has a minimal resolution with a chain of
three rational curves of self-intersection −v, −t, −u (DK 1.2). Look for algebraic-geometry theorems about
singularities that would force a *short resolution* with a *non-square* local class group pairing.

**K1 (local class group; PROVED, standard).** Cl(X, x) ≅ H₁(link) ≅ ℤ/n, with the discriminant pairing ⟨A*/n⟩ of the
resolution lattice. For n = p prime, the singularities 1/p(1,A) and 1/p(1,A′) have isometric class-group pairings
⟺ AA′ is a square mod p (this is a statement about forms on ℤ/p, not about the singularity's analytic type). So the
ES sign is the isometry class of the class-group pairing, i.e. the Wu-square (bsA_wu_rokhlin_sign).
**K2 (T-singularities at prime index; PROVED from the KSB classification).** Kollár–Shepherd-Barron (Invent. Math. 91
(1988) 299; EuDML record verified) define the T-singularities as 1/(dm²)(1, dma − 1). Every ℚ-Gorenstein smoothable cyclic
quotient singularity is of this type. At prime index p = dm² one has m = 1, d = p, so A ≡ −1: these are just the A_{p−1} = [[2,…,2]]
singularities, with (−1/p) = +1 for p ≡ 1 (4). **So for p ≡ 1 (4) no ES certificate singularity is ℚ-Gorenstein
smoothable**, and the certificates lie outside the KSB/Wahl world, which is the algebro-geometric home of squares
(Wahl singularities 1/m²(1, ma − 1) have rational-ball Milnor fibres; Lisca's fillings, bsA_lens_homotopy_surgery P3).
**K3 (deformations).** By Christophersen–Stevens, the components of the reduced versal deformation of 1/n(1,A)
correspond to zero continued fractions [[k₁,…,k_e]] = 0 with k_i ≤ a_i, where n/(n−A) = [[a₁,…,a_e]] is the dual
(from memory). For a length-3 word the dual is [[2^{v−2}, 3, 2^{t−3}, 3, 2^{u−2}]] (DK §2, for t ≥ 3). So the deformation
theory sees the long dual string, a Catalan-type count of polygon triangulations (Conway–Coxeter, farey_chain_frieze).
I know no deformation invariant that sees (A/n).

## Literature
KSB 1988 (verified record). Wahl, *Smoothings of normal surface singularities* (Topology 1981; from memory).
Christophersen (1991), Stevens (1991) (from memory). Lisca 2007 (verified). Riemenschneider duality (classical).

## Barrier screen
* Same pattern as topology: classification theorems (KSB, Wahl, Lisca, Greene) describe special subsets of
  the square/QR side (e.g. at prime index the only T-singularity is A_{p−1}; the QR singularity 1/17(1,4) is not a
  T-singularity). The ES certificates lie in the complement of these subsets (K2). A complement statement gives no existence.
* The sign is congruence data (B1). Short resolution = B2 divisor event.
* T1: consistent. At n = m² the T/Wahl world is non-empty, but ES needs Jacobi −1, which is absent.

## Cheap numerics
None needed beyond DK (dictionary items). K2 is an elementary consequence of the KSB form.

## Assessment
Dictionary plus a precise "complement" statement (K2, PROVED relative to KSB). No mechanism. Promise 0/5.
