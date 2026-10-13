# bsC_arithmetic_topology — T1 and the ES ray condition as linking numbers (Morishita's knots-and-primes) (O176)

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
In arithmetic topology (Mazur, Kapranov–Reznikov, Morishita) Spec ℤ is a 3-manifold, primes are knots, the Legendre
symbol (ℓ/q) is the mod-2 linking number lk₂(ℓ, q) and quadratic reciprocity is the symmetry of linking; the residue
ℓ mod q is lk_{q−1}(ℓ, q) ∈ ℤ/(q−1) (linking in the (q−1)-cyclic cover). Translate the O172 dictionary:
* **T1 / Diff-parity** = a *mod-2 linking identity*: for a certificate, Σ_{ℓ | n, v_ℓ(n) odd} lk₂(ℓ, "−d") ≡ 1 (Type I)
  — the product formula is "a knot bounds a surface, so its total linking with a boundary is 0" (Hilbert reciprocity ↔
  Gauss linking integral). At n = m² every knot appears an even number of times: total linking 0 ≠ 1.
* **ES ray condition** `f ≡ −1 (mod M)`: for each q^k ∥ M, `lk_{φ(q^k)}(f, q) = lk(−1, q)`: a *full* (not mod-2)
  linking condition of the sub-link f ⊂ N = 1 + 4c²dp with the link M = 4cd; f is a sub-link (divisor) of N.
So: ES Type II ⟺ the link of N contains a sub-link whose ℤ/φ(M)-valued linking vector with the knots of M is that of
"−1". Parity (mod-2 linking) is reciprocity-computable; higher linking is not (no reciprocity for ℤ/k-linking of rational
primes beyond power-residue reciprocity in ℚ(ζ_k)).

## Literature
Morishita, *Knots and Primes* (Universitext, 2nd ed. 2024), Ch. 4 (linking numbers and Legendre symbols), Ch. 8
(Milnor invariants and Rédei symbols); Kapranov, *Analogies between the Langlands correspondence and topological QFT*
(1995); Mazur, *Remarks on the Alexander polynomial* (1963–64 notes).

## Barrier screen
* **bsC_parity_quadratic_only Prop 1** is the topological statement "mod-2 linking is all that reciprocity gives over any
  base": the ES ray condition needs ℤ/φ(M)-linking; it is mod-2 only for M | 24.
* **B2**: the sub-link (divisor) is chosen, and its linking class mod M is the moving-modulus event.
* Higher Milnor invariants (Rédei triple symbols) are non-abelian but still ℤ/2-valued and computed for fixed triples
  of primes: nonab_frobenius_redei (BRAINSTORM, H-D) already screened Rédei-type gating (polynomial gating collapses).
* **T1**: built in (mod-2 linking identity).

## Cheap numerics
None (pure dictionary; every statement is a restatement of a Legendre/Dirichlet-character identity).

## Assessment
**Dictionary only (relabelling; Assessment).** It gives a vivid picture of *why* T1 is cheap (parity of linking) and
ES is not (full ℤ/φ(M)-linking of a chosen sub-link), but no theorem of arithmetic topology produces sub-links with
prescribed higher linking. Promise 0.
