# bsA_selling_sandpile — length-3 HJ words as Selling-reduced ternary lattices and 4-vertex multigraphs (O174)

## Idea
Read the HJ word through its plumbing lattice instead of the lens space. For n/A = [[v,t,u]] the plumbing (Goeritz)
Gram matrix is the tridiagonal `G = [[v,−1,0],[−1,t,−1],[0,−1,u]]`, det G = tuv − u − v = n. This is Greene's
*linear lattice* Λ(n,A). Three dictionaries follow.

**D1 (Selling reduction, PROVED by direct computation).** Put e₀ = −(e₁+e₂+e₃). Then (e₁,e₂,e₃,e₀) is an
**obtuse superbase** of Λ: all e_i·e_j ≤ 0 for i ≠ j, with Selling parameters (conorms, Conway, *The Sensual
(Quadratic) Form*, Lecture 4) p₀₁ = v−1, p₀₂ = t−2, p₀₃ = u−1, p₁₂ = 1, p₂₃ = 1, p₁₃ = 0.
**D2 (Kirchhoff / sandpile, PROVED).** A Selling-reduced integral ternary lattice is the reduced Laplacian of the
multigraph on {0,1,2,3} with p_ij parallel edges. So a length-3 word is the **4-vertex multigraph** "hub 0 joined to a
path 1–2–3 by v−1, t−2, u−1 parallel edges". Its spanning-tree number is n, and its sandpile (critical) group is
Λ*/Λ ≅ ℤ/n when that group is cyclic (always so when n is prime). Every positive integral ternary lattice is of this form for some
weighted K₄ (Selling reduction works over ℤ).
**D3 (genus, PROVED for n = p prime).** The discriminant form of Λ (equivalently the sandpile monodromy pairing
of Bosch–Lorenzini / Shokrieh) is ⟨A*/p⟩ on ℤ/p, and its square class is (A/p). For odd positive ternary lattices
of determinant p, the p-adic genus symbol has exactly two values, distinguished by this class. So
**five-slice ES(p) (p ≡ 1 (8), interior) ⟺ the non-square p-adic genus G⁻(p) contains a linear lattice
⟺ some 4-vertex "hub + path" multigraph with p spanning trees has non-square sandpile pairing.**
At n = m², Thm 4.5 is about the Jacobi symbol, not the genus. Both discriminant classes exist at m², but the Jacobi
symbol (A/m²) is always +1, and that is all the slices see. So the genus reading is literally right only at primes.

## Literature
Selling (1874) / Conway–Sloane, *Low-dimensional lattices VI: Voronoi reduction of three-dimensional lattices* (Proc.
R. Soc. A 1992; from memory): obtuse superbases, conorms. Greene, *Lattices, graphs, and Conway mutation* (Invent.
Math. 2013; from memory): graph lattices, linear lattices. Bosch–Lorenzini (2002) and Shokrieh (2010) on the monodromy
pairing of graphs (from memory). Clancy–Kaplan–Leake–Payne–Wood, J. Algebraic Combin. 2015: Cohen–Lenstra-type
heuristics for sandpile groups *with pairing* of random graphs (from memory). None of these was checked from the source.

## Barrier screen
* The genus G⁻(p) is never empty, but it has ≍ p classes (Siegel mass formula, from memory). Only ≍ log²p of them are
  linear. "The genus contains a linear class" is therefore the polylog lottery (B3), not a genus statement.
* Intrinsically: Λ is linear with middle vector e₂ iff e₂·Λ = ℤ and the binary lattice e₂^⊥ (determinant tp) has the
  gluing shape forced by e₁, e₃. This is a binary form of discriminant ≍ −4tp with a prescribed representation.
  It is exactly the Type II Heegner dictionary ((I)4, POINTWISE_TYPEII_SPECTRAL) with t in the level, so **B2**.
* Prop 8.3 / T1. Local and spinor conditions are blind to the linear shape, and the shape is what carries ES.
  The genus symbol is the sign layer (always available), and linearity is the class layer.
* Siegel–Weil-type averages over the genus (B6) count linear lattices with weight 1/|Aut|, i.e. the average of |L₃|.

## Cheap numerics
`scripts/bsA_selling.py 4` checks D1–D3 for all v,t,u ≤ 12 (0 failures). A by-product (EVIDENCE): among *all* K₄
multigraphs with edge weights ≤ 4 and prime tree number p ≡ 1 (4), 840 have non-square pairing and 108 square
(89 %). The bias is a small-weight cell effect, as in DK §8.1. General K₄ shapes carry no ES meaning. Only the
"hub + path" shape (p₁₃ = 0, p₁₂ = p₂₃ = 1) is a certificate.

## Assessment
New precise dictionary (PROVED): ES five-slice ⟺ a sandpile/genus statement about one degenerate Voronoi type of
ternary lattices. It turns the HJ picture into lattice/graph language, where "random graph sandpile pairings"
(CKLPW) supply the heuristic of DK §10.2. But the degenerate Selling type is a class-level condition. It reduces
to Type II Heegner points (B2). Promise 1/5. Spark: ask whether other *degenerate Voronoi types* (other zero/one patterns
of conorms) encode the remaining ES slices. Selling flips do not help, since they change the superbase of a *fixed*
lattice. Moves between classes of G⁻(p) are Kneser q-neighbours (Hecke operators), so "a neighbour walk from a
known class reaches a linear class" is again a lottery on the ≍ p-vertex neighbour graph. Not checked.
