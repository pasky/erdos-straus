# s5_reciprocity_forcing — can a reciprocity law force χ = −1? (combinations (ii) and (iii) of O230)

## Idea
* (ii) (J)45 SHARP 2 gives a signed Hilbert-symbol/Maslov product formula for Jacobi symbols along words. (J)52 gives
  SQ_±. Is there a signed count, a topological index (Maslov, Rademacher, Dedekind sum), that a reciprocity law forces to
  be nonzero?
* (iii) (J)55 makes T1 Hilbert reciprocity in ℚ(√j), and (J)19 has an order-3 T1 over ℤ[ω]. Is there an auxiliary field
  where reciprocity forces χ = −1 ("anti-T1")?

## Prop R (PROVED, elementary; the "locality lemma")
(R227 repair D10: *local invariant of w* := a function of the genus of L_w, i.e. of the ℤ_v-isometry classes. In that
stronger form Prop R still holds: unimodular at odd ℓ ≠ p, v_p(det) = 1 so the ℤ_p-class is fixed by ε_p, and the
ℤ₂-class of an odd-determinant lattice is fixed by its Gram matrix mod 8. Individual Hilbert symbols of a
diagonalisation are not invariants (use Hasse invariants); Dedekind-sum residues count only through explicitly named
Jacobi symbols that are themselves cell functions; the theta multiplier is constant (level 4p). Non-local = class
inside the genus. The statement also holds for odd composite n with gcd(A, n) = 1, D11.)
Let p be an odd prime and w ∈ X_p(ℤ) with tuv ≠ 0, signed words allowed. Let Q_w be the ternary path form (det p).
* The local isometry classes (Q_w ⊗ ℚ_v)_v are determined by (ε₂, ε_∞), the isotropy signs at 2 and ∞, together with
  the fixed determinant.
* ε₂ is a function of w mod 8 (CHI_FLIP Cor 1.2) and ε_∞ a function of the sign vector of (t, u, v) (SPARKS4 L1).
* Hence every function Φ of the local invariants of Q_w (Hilbert symbols, Hasse invariants, Maslov/inertia indices,
  Dedekind-sum residues via Rademacher–Grosswald, theta multipliers) is a function of (w mod 8, sgn w).

*Proof.* At odd ℓ ≠ p, Q_w ⊗ ℤ_ℓ is unimodular (det p), so ε_ℓ = 1 and the class is fixed by the determinant. At p,
ε_p = χ(w), and the product formula gives ε_p = ε₂ε_∞. A ternary quadratic space over ℚ_v is determined by its determinant
and Hasse invariant. ∎

Consequence. Every "index sum" I(p) = Σ_{w ∈ W} Φ(w), over any word set W defined by sign and congruence conditions, has
the form Σ_{cells c} #(W ∩ c)·Φ(c). Asking that I(p) be nonzero, or differ from its value at a square, is asking that some
cell c with Φ(c) ≠ Φ_square(c) contains an integral point. For the certificate Φ = [χ = −1] this cell condition is
*literally* ES-five(p): a positive point in a five-slice 2-adic cell (SPARKS4 three-bit law), and for signed words it is
(R_p). **A reciprocity law can relocate the sign between places but cannot create a point in a cell.** The forcing would
need a global input that counts points, which is what (J)39 Thm 2.2 and (J)48 Prop G″ rule out in modular-form shape.

## Anti-T1 (iii)
* The analogous statement holds in each auxiliary field used so far, and there are three cases.
  * ℚ(√j) ((J)55 Thm 3.4): the family's sign is a quadratic residue symbol of ℚ(√j). Reciprocity there makes Z_K⁺
    sterile, which is the χ = +1 direction.
  * ℤ[ω] ((J)19): the cubic symbol with anchor at 3 forces the trivial value at cubes.
  * ℚ itself (three-bit law): reciprocity forces χ = −1 exactly on the five-slice cells.
* In all three, reciprocity forces the sign to a value fixed by the remaining local data. "χ = −1 forced" therefore
  means "some point lies in a cell whose other local signs multiply to −1".
* Over ℚ these cells are explicit: 4 | one of t, u, v, A, B, with the point positive. So anti-T1 exists (the five
  slices), and anti-T1 *is* the ES question. Its content is the existence of an integral point in the cell, which is B2.
* An "anti-T1 auxiliary field" in the brief's sense would need a field F and a word-family where reciprocity in F
  forces the sign to −1 on *every* point of the family. That is a polynomial covering family (B1): it exists on
  classes (Mordell's identities) and never covers everything (PSIZE Thm M/C/F, (J)55 Thm 2.2).

## Literature
Hilbert reciprocity and the classification of ternary forms (O'Meara §63). Rademacher–Grosswald, *Dedekind Sums*
(1972), Ch. 5: 12N·s(h, N) ≡ N + 1 − 2(h/N) (mod 8). Girstmair IJNT 7 (2011). These are the local formulas that Prop R
subsumes.

## Barrier screen
* T1 is respected by construction (Prop R at squares gives every cell value +1).
* B2: the remaining question is a cell-occupation question.
* (J)39/(J)48: an exact global count of cell occupations of modular type does not exist by size.
* Thm 9.1 / Prop 10.3 (main-term certificates): an index that is a main term of a count is bounded by B3.

## Cheap numerics
None is needed beyond what exists. The three-bit law (the only nontrivial input) was checked from scratch by R219
(`scripts/review_r219_threebit.py 1001`, 77 658 words, 0 violations). Prop R is a formal consequence.

## Assessment
PROVED, and a negative result with exact scope: *local-invariant indices are cell sums*. Combinations (ii) and (iii)
cannot produce forcing. The only escape is a global (non-local) invariant that sees how many points occupy a cell,
i.e. a counting/automorphic input of the kind (J)39/(J)48 bound away.
