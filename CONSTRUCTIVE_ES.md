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

## 2. The bijection with supersingular 2-isogenies, and the exact ES dictionary

Write 𝔊⁻_p (resp. 𝔊⁺_p) for the set of isometry classes of positive classical ternary lattices of determinant p
anisotropic (resp. isotropic) at p, i.e. with C₀(L) ⊂ B_{p,∞} (resp. ⊂ B_{2,∞}). Each is a single genus (the p-adic class
⟨1, a, pb⟩ is fixed by (−ab/p) = ∓1, the 2-adic class by the determinant and the Hasse invariant via Lemma 1.1).

**Theorem 2.1 (PROVED; CERTIFIED class counts).** L ↦ E(L) is a bijection
𝔊⁻_p ⟷ {isomorphism classes of Eichler orders of level 2 in B_{p,∞}} ⟷ X₀(2)^{ss}(𝔽̄_p) / ⟨Frob_p, w₂⟩,
with inverse E ↦ E^{ev} = C₀(L). Moreover L(E) ≅ (E⁰)^#(p): the dual of the trace-zero lattice E⁰ = {x ∈ E : trd x = 0}
(form nrd, bilinear ⟨x, y⟩ = trd(xȳ)/2), rescaled by p. Likewise 𝔊⁺_p ⟷ Eichler orders of level p in B_{2,∞}.
*Proof.* Injectivity and well-definedness: Thm 1.2(a),(c) (E(L) is canonical, and L ≅ L′ ⟺ C₀(L) ≅ C₀(L′) by
Gross–Lucianovic: twisted-similarity classes of ternary forms ⟷ isomorphism classes of Gorenstein orders; for positive
forms of equal determinant twisted similarity is isometry up to sign). Surjectivity: let E be Eichler of level 2 in
B_{p,∞}; E^{ev} is an order (locally at 2 it is ℤ₂ + J(E₂)), of discrd 4p. Every order of discrd 4p is Gorenstein: its
Gross–Lucianovic form q has N(q) = 4p, and q = c·q′ would give c³ | 4p, so c = 1. Hence E^{ev} = C₀(q) with N(q) = 4p.
Since all Eichler orders of level 2 are locally conjugate, E^{ev} ⊗ ℤ₂ ≅ C₀(L_w ⊗ ℤ₂) for any certificate word w (Thm
1.2(c)), so q ⊗ ℤ₂ is twisted-similar to a classical form; twisted similarity q ↦ u·det(g)⁻¹·q∘g preserves "classical"
(even cross terms), so q is classical with Gram of determinant N/4 = p, positive after a sign; C₀ ⊂ B_{p,∞} gives
anisotropy at p. Then E(L) = E by uniqueness in Thm 1.2(a). The Deuring correspondence sends (E, C), C ⊂ E[2] of order 2,
to End(E, C) = {x ∈ End E : x(C) ⊂ C}, an Eichler order of level 2; every such order arises, and End(E, C) ≅ End(E′, C′)
iff (E′, C′) is in the ⟨Frob_p, w₂⟩-orbit of (E, C) (Frob_p: conjugate data; w₂: (E/C, E[2]/C), the same order seen from
the other endpoint). Finally C₀(L)⁰ = E⁰ (trace-zero elements of E have even trace), and C₀(L)⁰ has Gram adj(G) = p·G⁻¹
in the basis dual to e₁, e₂, e₃ (cofactor computation below), so L ≅ (E⁰)^#(p). ∎
CERTIFIED (`scripts/ce_classes.py` canonical Minkowski forms; `scripts/ce_ss2.py`: supersingular j over 𝔽_{p²}, the three
2-torsion x-coordinates of the canonical model, Vélu for w₂): |𝔊⁻_p| = #(X₀(2)^{ss}/⟨Frob, w₂⟩) for p = 37, 61, 73, 97,
109, 157, 181, 193 (values 4, 6, 7, 9, 9, 14, 15, 15; p ≡ 1 mod 12 so that j = 0, 1728 are ordinary).

**Explicit gram.** For the path lattice, adj(G_w) = [[A, u, 1], [u, uv, v], [1, v, A*]] (A = tu − 1, A* = tv − 1). In C₀(L_w):
α = e₁e₂, β = e₂e₃, γ = e₁e₃ have trd α = trd β = −2, trd γ = 0, nrd α = tv, nrd β = tu, nrd γ = uv, and αβ = tγ.
So i := 1 + α, j := 1 + β are trace zero with i² = −A*, j² = −A, ij + ji = −2 (⟨i, j⟩ = 1), and
C₀(L_w) = ℤ⟨1, α, β, αβ/t⟩.

**Corollary 2.2 (ES five-slice dictionary; PROVED).** For a prime p, TFAE:
(i) p has an ES five-slice certificate (a word w ∈ X_p with χ(w) = −1; MODEL_SPECIFIC Thm 3.1, CHI_FLIP Cor 1.3);
(ii) some class of 𝔊⁻_p has a *path basis*: Gram [[v, −1, 0], [−1, t, −1], [0, −1, u]] with t, u, v ≥ 1;
(iii) some supersingular 2-isogeny (E, C) over 𝔽̄_p has (End(E, C)⁰)^#(p) with a path basis; equivalently End(E, C)⁰ has a
basis of Gram [[A, u, 1], [u, uv, v], [1, v, A*]];
(iv) some supersingular E/𝔽̄_p, some t ≥ 1 and trace-zero i, j ∈ End E satisfy
  ij + ji = −2, deg i · deg j = tp + 1, (1 − i)(1 − j) ∈ t·End E.
*Proof.* (i)⟺(ii): CHI_FLIP Cor 1.3 (any positive path lattice of det p is some L_w, letters ≥ 1 automatic: det > 0
forces t > (u + v)/(uv) > 0 once u, v ≥ 1). (ii)⟺(iii): Thm 2.1. (i)⟹(iv): take a maximal order containing C₀(L_w)
(Thm 1.2(b)), i = 1 + α, j = 1 + β; (1 − i)(1 − j) = αβ = tγ. (iv)⟹(i): put a = deg i, b = deg j. Since
(1 + a)(1 + b) = nrd((1 − i)(1 − j)) ≡ 0 (mod t²) and ab ≡ 1 (mod t), for each ℓ^k ‖ t one gets ℓ^k | 1 + a and
ℓ^k | 1 + b (if x = v_ℓ(1 + a) ≤ y = v_ℓ(1 + b) and x < k, then ℓ^x a′ + ℓ^y b′ ≡ 0 (mod ℓ^k) forces x = y, and then 2x ≥ 2k).
So v := (1 + a)/t, u := (1 + b)/t are integers and (tv − 1)(tu − 1) = tp + 1 gives tuv − u − v = p. The pure quaternions
i, j (non-commuting, since det [[a, 1], [1, b]] = tp ≠ 0) generate B_{p,∞}, and e₁e₂ ↦ i − 1, e₂e₃ ↦ j − 1 extends to an
algebra embedding C₀(L_w) ⊗ ℚ → B_{p,∞} (the structure constants of C₀ are determined by traces, norms and ⟨i, j⟩),
with e₁e₃ ↦ (i − 1)(j − 1)/t ∈ End E. So C₀(L_w) ⊂ End E ⊂ B_{p,∞}, i.e. χ(w) = −1. ∎

*Reading (Assessment).* (iv) is the five-slice analogue of DIFF_DEEP Thm 2.1 (Type II: trace-zero x, y with ⟨x, y⟩ = 1
plus a numerical divisibility); here the extra condition is a **ring condition at level t**: for odd prime ℓ | t,
i and j act on E[ℓ] as involutions (i² = −a ≡ 1) and (1 − i)(1 − j) ≡ 0 (mod ℓ) says that the −1-eigenline of j equals the
+1-eigenline of i: i and j jointly preserve a cyclic subgroup C_ℓ, acting on it by +1 and −1. As always, the quantifier
"∃ E" adds nothing (supersingular transfer): (iv) holds for some E iff a word with χ = −1 exists. The content is the
**shape**: among the ≈ p/8 classes of 𝔊⁻_p (mass (p − 1)/8·(…); Thm 2.1), the path classes are the *near-orthogonal*
ones (off-diagonal entries −1, 0, −1), of which there are ≤ |X_p| ≍ log² p on average.
