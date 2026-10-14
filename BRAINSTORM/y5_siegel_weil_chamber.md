# y5_siegel_weil_chamber — is the positive-chamber count a Siegel–Weil product with the sign at ∞? (O213, item (d), O210 spark 5)

## Idea
O210 spark 5 proposed this. The positive integral points of the A₂ cluster surface X_N : cms − c − s = N split by the
sign χ. Perhaps N₋(N) is a Siegel–Weil product of local densities whose ∞-factor carries the sign, which would
connect to KUDLA_ES (J)13.

## Analysis
1. **Words are path bases.** Word (c, m, s) ↦ path form Q_w = [[c,−1,0],[−1,m,−1],[0,−1,s]], positive definite of
   det N. χ(w) = −ε₂(Q_w) (CHI_FLIP Thm 1.1; y5_general_r_jacobi Thm 1 with r = 3). So
   N₋(N) = Σ_{genera G with ε₂ = −1} #{path bases of lattices in G}.
2. **Siegel–Weil is trivial on full-rank data (PROVED, standard).**
   * The representation number of a rank-3 form G by a rank-3 lattice L is r(L, G) = |Aut L|·[L ≅ G].
   * So the genus average Σ_{L∈gen} r(L, G)/|Aut L| / mass = 1/mass if G ∈ gen, and 0 otherwise.
   * The Siegel–Weil "product of local densities" for a basis-representation is the indicator of the genus. It carries
     no information beyond the genus label. The ∞-density is the same for every positive definite genus.
   * Hence the sign is not an ∞-factor of a Siegel–Weil product. It sits in the 2-adic genus label ε₂, and the ∞-place
     enters only through definiteness (s_∞ = 1), i.e. through the product formula. This is the same conclusion as
     (J)13 (Kudla: Diff-parity) and y5_narrow_wide.
3. **What remains is a reduction-theory lottery.** SQ₅(p) ⟺ the genus G₋(p) of ternary lattices of det p with
   ε₂ = −1 contains a lattice that admits a *path basis*. A path basis is a basis with e₁·e₂ = e₂·e₃ = −1 and
   e₁·e₃ = 0.
   * G₋(p) is non-empty for every prime p (Siegel/Hasse; T1 makes it empty at squares).
   * It has ≍ p classes: CONSTRUCTIVE_ES Thm 2.1 identifies it with X₀(2)^{ss}/⟨Frob, w₂⟩.
   * The number of words at p is ≪ p^{1/3+o(1)} ((J)26 by-product).
   * So path-basis lattices are a fraction ≪ p^{−2/3+o(1)} of the genus. Existence is "a thin subset of classes meets
     the ε₂ = −1 half": B2 in reduction-theory clothing, as already in (J)35.

## Literature
* Siegel mass formula / Siegel–Weil: Siegel (1935); Weil, *Sur la formule de Siegel* (1965); for ternary lattices
  Conway–Sloane, *Low-dimensional lattices IV: the mass formula*.
* Kudla, *Central derivatives of Eisenstein series and height pairings* (Ann. Math. 1997), incoherent collections ((J)13).
* CHI_FLIP, CONSTRUCTIVE_ES ((J)33, (J)35).

## Barrier screen
* B6: a genus-level count (Siegel) is an average over the genus, so it says nothing about the thin path-basis subset.
* B3: no main term to exploit.
* Thm 9.1 / SIGN_IDENTITY Thm 2.2 already exclude modular generating functions for N₋.
* T1: the genus G₋ at squares is empty by the product formula (the ∞-factor s_∞ = 1). That is the only place where
  "positivity" enters a Siegel-type statement.

## Cheap numerics
`scripts/y5_words_at.py N`: N = 21 841 has 34 formal words (12 with χ = −1, 2 interior). N = 1 000 033 has 133 words
(91 with χ = −1). Compare ≍ p classes in G₋(p): words are a vanishing fraction.

## Assessment
Negative (PROVED for the Siegel–Weil triviality, Assessment for the reading). The positive chamber's integral-point
count is not a Siegel–Weil product carrying the sign at ∞. Siegel–Weil on full-rank data is the genus indicator. The
sign is the 2-adic genus label, positivity enters only as definiteness in the product formula, and existence is a
reduction-theory lottery over a p^{−2/3}-thin subset of classes. Closes O210 spark 5 negatively.
