# CONSTRUCTIVE_ES — five-slice ES certificates as Eichler orders / supersingular 2-isogenies (task O199, spark relay T)

Status: checkpoint in progress (O199). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on CHI_FLIP.md (O198, CLAIMED, under review R198: Thm 1.1, Cor 1.3), MODEL_SPECIFIC Thm 3.1, DEDEKIND_ES Thm 4.5,
DIFF_DEEP (supersingular transfer), KUDLA_ES. Scripts `scripts/ce_*` (library `ce_lib.py`: even Clifford orders,
overorders, reduced discriminants, exact arithmetic).

Notation (as in CHI_FLIP). Word w = (t, u, v) ∈ ℤ³_{≥1}, tuv − u − v = n odd; A = tu − 1, A* = tv − 1, AA* = tn + 1;
χ(w) = (−A/n). Path lattice L_w = ℤ³ with Gram G_w = [[v, −1, 0], [−1, t, −1], [0, −1, u]] (det n), classical
(B(e_i, e_j) = G_ij, Q(x) = B(x, x)). C₀(L) = even Clifford order (Gross–Lucianovic: Gorenstein, reduced discriminant
N(Q) = 4·det G). For n = p prime, ES five-slice certificate ⟺ χ(w) = −1 ⟺ C₀(L_w) ⊂ B_{p,∞} (CHI_FLIP Cor 1.3).

## 1. The overorder ladder of C₀(L): Eichler orders of level 2 (PROVED + CERTIFIED)

**Lemma 1.1 (2-adic isotropy test; PROVED, elementary).** An odd unimodular ternary ℤ₂-lattice L ≅ ⟨a₁, a₂, a₃⟩
(a_i ∈ ℤ₂^*) is isotropic ⟺ not all a_i are congruent mod 4 ⟺ Q(x) ≡ 0 (mod 4) for some primitive x. In that case
there are exactly two classes x mod 2L with Q(x) ≡ 0 (mod 4).
*Proof.* Odd unimodular ℤ₂-lattices are diagonalisable. For x primitive with odd-coordinate set S ≠ ∅,
Q(x) ≡ Σ_{i∈S} a_i (mod 4) (odd squares ≡ 1 mod 8; even coordinates contribute 0 mod 4); |S| ∈ {1, 3} gives an odd
value, so Q(x) ≡ 0 (4) ⟺ |S| = 2 with a_i ≢ a_j (4); if the residues mod 4 are not all equal exactly two pairs qualify.
The isotropy criterion depends only on a_i mod 8 (unit square classes) and is a finite Hilbert-symbol check:
CERTIFIED for all 64 triples (`scripts/ce_check_lemma11.py`, 0 failures). ∎

**Theorem 1.2 (the Eichler ladder; PROVED, with CERTIFIED numerics).** Let L be a positive classical ternary lattice of
odd determinant n, Λ = C₀(L) (discrd 4n). Then:
(a) every element of Λ has even reduced trace, and Λ has a unique overorder E(L) of index 2; E(L) has discrd 2n and
Λ = E(L)^{ev} := {x ∈ E(L) : trd x ∈ 2ℤ};
(b) if L ⊗ ℤ₂ is isotropic, E(L) ⊗ ℤ₂ is an Eichler order of level 2 in M₂(ℚ₂), contained in exactly two maximal
orders, namely C₀(L⁺₁), C₀(L⁺₂) for the two overlattices L⁺_i = L + ℤ·x_i/2 of Lemma 1.1 (on which Q is integral,
N(Q|L⁺_i) = n); if L ⊗ ℤ₂ is anisotropic, E(L) ⊗ ℤ₂ is the maximal order of the ramified algebra;
(c) for n = p prime and χ(w) = −1 (L = L_w), **E(L_w) is an Eichler order of level 2 in B_{p,∞}**; for χ(w) = +1,
E(L_w) is an Eichler order of level p in B_{2,∞}.
*Proof.* trd(e_ie_j) = 2B(e_i, e_j) and trd 1 = 2, so trd(Λ) ⊂ 2ℤ. At odd ℓ, overorders of 2-power index change
nothing, so everything is a statement about Λ₂ = C₀(L ⊗ ℤ₂), which depends only on the ℤ₂-isometry class of the
diagonalisable lattice L ⊗ ℤ₂ ≅ ⟨a₁, a₂, a₃⟩, a_i ∈ {1, 3, 5, 7}. Finite check (`scripts/ce_check_thm12.py`, exact
arithmetic on the ℤ-orders C₀(⟨a₁,a₂,a₃⟩), all 64 triples, 0 failures): unique index-2 overorder E, discrd(E) = discrd(Λ)/2,
E contains an element of odd trace (so Λ = E^{ev}, both of index 2 in E), and the 2-power overorders of minimal
discriminant are two of discrd discrd(Λ)/4 (isotropic) resp. E itself (anisotropic). An order of discrd 2 in M₂(ℚ₂)
is hereditary, i.e. Eichler of level 2; in the division algebra discrd 2 is maximal. The two maximal overorders in the
isotropic case are C₀(L⁺_i): L ⊂ L⁺_i gives C₀(L) ⊂ C₀(L⁺_i), and N(Q|L⁺_i) = N(Q|L)/4 = n.
Conceptually Λ₂ = ℤ₂ + J(E₂): for E₂ = [[ℤ₂, ℤ₂], [2ℤ₂, ℤ₂]], ℤ₂ + J(E₂) = {[[a, b], [2c, d]] : a ≡ d (2)} = {x ∈ E₂ : trd x
even}; for the ramified maximal order, ℤ₂ + πO₂ = {trd even} (trd mod π is the trace 𝔽₄ → 𝔽₂). (c) follows from
CHI_FLIP Cor 1.3 (C₀(L_w) ⊂ B_{p,∞} iff χ = −1, else ⊂ B_{2,∞}) and (b): discrd 2p, so Eichler level 2 at 2 inside
B_{p,∞}, resp. maximal at 2 and level p at p inside B_{2,∞}. ∎
CERTIFIED (`scripts/ce_test1.py`, `ce_test2.py`): every word of p ∈ {41, 73, 89, 97, 113} (151 words): unique overorder
of discrd 2p, 2E ⊂ Λ, and #maximal overorders of discrd p = 2 exactly when χ = −1 (72 words), 0 when χ = +1 (79 words).
