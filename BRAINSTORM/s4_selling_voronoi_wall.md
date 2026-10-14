# s4_selling_voronoi_wall — reduction theory (positivity) on the χ = −1 genus: path forms are Selling-reduced lattices on a Voronoi wall with two unit conorms (O218)

**ES is not solved here.** Labels as in DISCOVERIES.md. Notation as in s4_three_bits_meta.

## Idea
Goal (2), "geometry of numbers that genuinely uses positivity": the classical positivity-only tool for ternary forms
is Selling/Voronoi reduction — every positive definite ternary lattice has an *obtuse superbase* e₀ + e₁ + e₂ + e₃ = 0,
e_i·e_j ≤ 0, and Q = Σ_{i<j} p_ij (x_i − x_j)² with conorms p_ij = −e_i·e_j ≥ 0 (Selling 1874; Conway–Sloane,
*Low-dimensional lattices VI*, Proc. R. Soc. A 436 (1992)). Indefinite forms have no such reduction. Ask what the ES
certificate lattices look like in this canonical positivity coordinate.

## Dictionary (PROVED, algebra; invariance CERTIFIED numerically)
**Lemma S.** For a positive word (t, u, v) with t ≥ 2, the path form satisfies, with x₀ = 0,
  Q_w = (x₁ − x₂)² + (x₂ − x₃)² + 0·(x₁ − x₃)² + (v − 1)x₁² + (t − 2)x₂² + (u − 1)x₃²,
i.e. (e₁, e₂, e₃) is part of an obtuse superbase with conorms **p₁₂ = p₂₃ = 1, p₁₃ = 0**, p₀₁ = v − 1, p₀₂ = t − 2,
p₀₃ = u − 1 (all ≥ 0). Conversely any obtuse superbase with a face (p₁₂, p₂₃, p₁₃) = (1, 1, 0) is a path basis of a
positive word (t, u, v) = (p₀₂ + 2, p₀₃ + 1, p₀₁ + 1). *(Expand; the converse reads the same identity backwards.)*
(t = 1 words are the boundary p₀₂ = −1, not obtuse; they are the formal/boundary words of HJ_DEEP.)

Hence, with CONSTRUCTIVE_ES Thm 2.1 / CHI_FLIP Cor 1.3 at n = p:
**ES-five(p) (interior, t ≥ 2) ⟺ some lattice of the χ = −1 genus G₋(p) (Eichler level 2 in B_{p,∞}) has an obtuse
superbase with a face of conorms (1, 1, 0).** Since the conorm function (with the 7th conorm, always 0) is a lattice
invariant (Conway–Sloane VI, from memory; checked below: 3000 random GL₃(ℤ)-conjugates Selling-reduced back to the
multiset {0, 0, 1, 1, v − 1, t − 2, u − 1}, 0 mismatches), certificate lattices carry **two zero conorms**: their
Voronoi cell is *not* the generic truncated octahedron (the 2-zero type is the hexa-rhombic dodecahedron in CS VI's
list, quoted from memory). So **ES-five certificates are lattices lying on a Voronoi wall** of the reduction domain,
with two further conorms pinned to 1.

## Construction attempts (barrier as steering wheel)
1. *Force a genus member onto the wall.* The genus G₋(p) has ≍ p classes (mass formula); the wall-with-unit-conorms
   lattices of det p are the ≍ log²p positive words. Tools that move inside a genus: ℓ-neighbours (Kneser). The
   ℓ-neighbour graph is connected because Spin is *non-compact at ℓ* — the auxiliary finite place replaces the
   compact ∞ (this is the c_∞-imitation of y3_frob_infinity in lattice form). It is a Ramanujan-type expander, so it
   reaches every class in O(log p) steps, but expander mixing does not force hitting a set of relative size
   p^{−1+o(1)} (s3_isogeny_mixing, (J)41). B2 in the form "target set is thin".
2. *Use the wall itself.* A lattice on the wall p₁₃ = 0 has two obtuse superbases (Selling flip across the wall).
   Flipping preserves the lattice, hence its genus, hence χ (χ is a genus function of Q_w, CHI_FLIP Thm 1.1). So
   whatever word the flipped superbase gives (if it again has a (1,1,0) face) has the same sign: no sign change
   (PROVED for the sign; which word it is was not checked — possibly a frieze symmetry, unverified).
3. *Minimal-conorm statements.* Is there a positivity theorem "every genus of det p contains a lattice with two
   conorms ≤ 1"? The conorms of the 2-adically *anisotropic*-type genus G₊(p) model (TWO_FIBRES Thm A: sublattices
   of ℤ³) — e.g. ℤ³ itself has conorms {0,0,0,0,1,1,1} — suggest wall lattices are common on the χ = +1 side; the
   question for G₋(p) is the thin-set lottery of (J)45 restated. No theorem of this type is known; it would imply
   SQ₅-five, so it is at least as hard (Assessment).

## Barrier screen
B2/B3: the conorm pattern is a bijective re-parametrisation of X_p (Lemma S), so the lottery is unchanged (thin
target in a genus of ≍ p classes). T1: at odd squares G₋(m²) is empty (CHI_FLIP: ε₂ forced), so the statement is
T1-correct; the reduction theory itself is numerator-blind but *positivity-using* — the first tool in this wave that
genuinely needs definiteness and still collapses, because it locates the solution set rather than forcing it.
Harness: 8/n has slices at m = 8 inside {χ = −1}: their wall lattices are those with p₀₂ + 2 ≡ 0 (8) or similar
congruence refinements — membership is not a genus function for 8 ((J)32), consistent.

## Cheap numerics
`scripts/s4_selling.py 3000`: identity failures 0, Selling-reduced conorm multiset mismatches 0 (3000 random words
t ∈ [2,40], u, v ∈ [1,40], random unimodular conjugation).

## Assessment
New exact dictionary (PROVED for Lemma S; the lattice-invariance of conorms is classical): *ES certificates are
the Selling-reduced χ = −1 lattices on the Voronoi wall with two unit conorms.* It is the cleanest statement that
the certificate set is a reduction-theory (archimedean) object, but it locates rather than forces (COLLAPSES to the
(J)45 thin-set lottery, B2). Promise 1/5. Spark: Voronoi-wall lattices in a genus ↔ lattices with a sublattice
⟨e₁, e₃⟩ orthogonal pair + a vector of inner products (−1, −1): a "representation of a fixed decorated binary"
question that Siegel–Weil could count (main term only, B3).
