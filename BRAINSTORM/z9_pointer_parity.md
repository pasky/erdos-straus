# z9_pointer_parity — global parity/degree laws for certificate edges on G_p/Frob: none (O233)

## Idea
O224's Fano pigeonhole lives inside one word: the 2 even pentagon classes and the 2 isotropic classes meet on the 3-point
line W, so a pentagon vector always points at an endpoint of the Eichler edge. "Global Fano" asks for a pigeonhole one level
up, over the graph. Every path edge carries a pointer to one or both endpoints, and every vertex sees its 3 edges as the 3 points of the
conic {q ≡ 0} in ℙ(F/2F), with the radical as nucleus (local Fano structure at vertices, §1 of GLOBAL_FANO). Candidates for a
forcing law: (a) parity of the number P(p) of path classes; (b) the number of odd-degree vertices of the path subgraph H_p;
(c) the pointer digraph (path edge → pointed endpoint): sources, sinks, in-degree parities.

## Literature
Handshake lemma; Brandt matrices B(2) = adjacency of G_p (Pizer 1980; Gross 1987); y1_reciprocal_parity (N₋ mod 8 is
equidistributed), y2_parity_involution (#F₋(p) even, the only involution on words is reversal), invol_windmill_signature.

## Barrier screen
A parity law of type (a)/(b) would be an H-E exact identity. The available involutions on certificates are word reversal
(already quotiented out: a class is reversal-invariant), w₂ (it swaps the endpoints and fixes the edge class) and Frobenius
(already quotiented out). None of them has an odd number of fixed points on the certificate set. The global inputs that are
exactly computable (mass (p−1)/24, tr B(2), the layer masses of z9_frobenius_layers) are form-class data. Prop 10.3: they see
the genus shadow of the path condition, never the residue condition ±1 that defines a path edge (z1_glue_square_roots). So a forcing law of this kind would have to be numerically visible
as a fixed residue of P(p). It is not (below). T1 is vacuous: at odd squares the graph does not exist.

## Cheap numerics (EVIDENCE; `scripts/z9_stats.py`, `data/z9/stats_p1mod4_1e4.txt`, all 609 primes p ≡ 1 (4), p ≤ 10⁴)
* P(p) even for 47.6 % of primes: no parity law. The minimum is P(p) ≥ 1 throughout (ES-five holds there, as known).
* H_p has no odd-degree vertex at 3 primes (5, 13, 2521; all path classes there are loops), so (b) forces nothing even in principle.
* Pointer digraph: classes whose words point at both endpoints occur at most primes, but not at all (none at 17 primes, e.g. 37, 193, 421).
  There is no sink or source law.
* The only robust structural regularity found is the loop enrichment. It is explained exactly by z9_frobenius_layers Lemma 1 (letters are small,
  so path edges sit in layers 1, 2).

## Assessment
Negative, EVIDENCE to 10⁴ plus the structural reason (every exactly computable global count is genus-level data). A global
pigeonhole would need a finite structure on the edge set whose size beats the number of non-path edges. The path set is
≍ log² p on average out of ≍ p/16 edges, so no pigeonhole of bounded size can reach it. Promise 0/5.
