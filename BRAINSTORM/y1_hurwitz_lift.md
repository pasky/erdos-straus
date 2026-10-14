# y1_hurwitz_lift — the χ = +1 fibre is the cubic lattice: ES sign = (non-)embeddability of n·G_w in ℤ³ (O209)

## Idea
O205 SHARP 2: a word w = (t, u, v) ∈ X_n has Diff(T_w) = {2} (χ = +1, char-2 fibre of X₀(2p), algebra B_{2,∞}) or
Diff ∋ odd primes. The char-2 side has **class number one** (Hurwitz order H, pure part H⁰ = ℤ³ with nrd = sum of three
squares). So the χ = +1 side should have an explicit *cubic-lattice model*, and ES becomes a **non-embeddability** statement.

**Proposition H1 (PROVED; classical inputs: class number 1 of B_{2,∞} and of the genus of I₃, Eichler's maximal-lattice
theorem).** Let n be odd, w ∈ X_n, A = tu − 1, A* = tv − 1, G_w the path Gram. TFAE:
(i) Diff(T_w) = {2}, i.e. ε_ℓ(Q_w) = (−A/ℓ)^{v_ℓ(n)} = +1 for every odd ℓ (for n = p prime: χ(w) = +1);
(ii) C₀(L_w) ⊗ ℚ ≅ B_{2,∞};
(iii) ∃ x, y ∈ ℤ³ with x·x = A*, y·y = A, x·y = 1 (and then one can choose them with x × y ≡ x + y (mod t));
(iv) **n·G_w is the Gram matrix of three vectors of ℤ³**, i.e. L_w(n) ↪ I₃.
*Proof.* (i)⟺(ii): CHI_FLIP Thm 1.1 / SIGN_IDENTITY Prop 4.1(b). (ii)⇒(iii): C₀(L_w) is an order of B_{2,∞}, hence lies in
a maximal order, conjugate to H; i = 1 + e₁e₂, j = 1 + e₂e₃ go to pure quaternions of H, i.e. vectors x, y ∈ ℤ³ with
nrd = |·|², and ij + ji = −2 means x·y = 1. With z := x × y one has ij = −1 + z, so (1 − i)(1 − j) = z − x − y, which
lies in t·C₀ ⊂ tH, and its real part is 0, so z − x − y ∈ tℤ³. (iii)⇒(ii): x, y do not commute (det T_w = tn ≠ 0), so they
generate a quaternion subalgebra of H ⊗ ℚ = B_{2,∞}, which is all of it; its structure constants are fixed by T_w, so it
is ≅ ℚ⟨i, j⟩ = C₀(L_w) ⊗ ℚ. (iii)+(congruence) ⇒ (iv): γ := (z − x − y)/t ∈ ℤ³ has γ·x = −v, γ·y = −u, |γ|² = uv, so
x, y, γ span M ⊂ ℤ³ with Gram ≅ adj(G_w) = nG_w⁻¹ (det n²). Then ℤ³ ⊂ M^#, [M^# : ℤ³] = n, so nM^# ⊂ ℤ³, and the
n-multiples of the dual basis have Gram n·G_w. (iv)⇒(ii): L_w ⊗ ℚ is then similar to I₃ ⊗ ℚ, and C₀ is a similarity
invariant. ∎
**Corollary H2 (T1, integral form; PROVED).** If n = m² (odd), **every path lattice L_w of X_n is an index-m sublattice
of ℤ³**: there are a, b, c ∈ ℤ³ with |a|² = v, |b|² = t, |c|² = u, a·b = b·c = −1, a·c = 0.
*Proof.* L_w ⊗ ℚ ≅ I₃ ⊗ ℚ (det a square, C₀ = B_{2,∞}, Prop 4.1(d)); L_w lies in a maximal classical lattice; those
form one genus (Eichler; O'Meara §91), which contains I₃ and has one class. ∎
**Corollary H3 (ES-five as non-embeddability; PROVED).** For p prime: ES-five(p) ⟺ **some word w ∈ X_p has p·G_w not
realisable as a Gram matrix of integer vectors**, i.e. no a, b, c ∈ ℤ³ with |a|² = pv, |b|² = pt, |c|² = pu,
a·b = b·c = −p, a·c = 0. Equivalently: some binary path form [[tv − 1, 1], [1, tu − 1]] is **not represented by
x² + y² + z²** (Gauss's three-squares genus of determinant tp).
**Proposition H4 (the χ = +1 genus is the conic; PROVED, with a CERTIFIED count).** For p prime, the χ = +1 lattices
(det p, isotropic at p) are exactly L_ℓ = {x ∈ ℤ³ : x ≡ λℓ (mod p)} with Q = |x|²/p, for ℓ on the conic
C: x² + y² + z² ≡ 0 over 𝔽_p. *Proof.* By H1(iv) L(p) is an index-p² sublattice M ⊂ ℤ³ with all inner products ≡ 0 (p);
M mod p is totally isotropic in 𝔽_p³, so of dimension ≤ 1, and the index forces M = pℤ³ + ℤℓ̃. ∎ So 𝔊⁺_p is the image
of C(𝔽_p)/O(ℤ³) ≅ P¹(𝔽_p)/S₄ (≈ (p + 1)/24 classes) — the octahedral quotient that Deligne–Rapoport/Cerednik–Drinfeld
predict for the singular points of X₀(2p)_{𝔽₂} (X₀(p)^{ss}_{𝔽̄₂} = P¹(𝔽_p)/Aut(E_{j=0}), extended by w₂).
CERTIFIED (`scripts/y1_conic_orbits.py`): #orbits = #𝔊⁺_p (ce_classes) for p = 13, 17, 29, 37, 41, 61, 73, 97, 101;
at p = 109, 6 orbits vs 5 classes (two orbits give isometric lattices: the map is onto, not always injective).

## Literature
Gauss, *Disquisitiones* art. 278–292 (binary forms represented by x² + y² + z²; z^⊥ correspondence); Venkov (1931);
Hurwitz order, class number 1 of B_{2,∞} (Vignéras, *Arithmétique des algèbres de quaternions*, LNM 800);
O'Meara, *Introduction to Quadratic Forms*, §91 (maximal lattices form one genus), §102 (representations, one-class genus);
Siegel's mass formula for I₃; Deligne–Rapoport for the bad fibres of X₀(2p). Novelty (Assessment): the χ = +1 ⟺ Hurwitz
embedding is implicit in CONSTRUCTIVE Thm 1.2/CHI_FLIP Cor 1.3; the explicit ℤ³ forms H1(iii)/(iv), H2 and H4 are new
to the campaign (no prior hit for "three squares"/"x·y = 1" in the repo).

## Barrier screen
* **B2:** H3 is "the level-t family F_t(p) leaves Gauss's three-squares genus for some t" — a genus statement on a
  divisor-in-class family; the selection of the genus (sign) is easy, existence of a family member in it is the lottery.
* **T1:** H2 *is* T1, now as a positive geometric statement (square-det path lattices sit in ℤ³). Any proof of ES must
  use a property of p·G_w ⊂ ℤ³ that fails for G_w ⊂ ℤ³ at squares — local (Hasse at p), hence B5-safe but B2-bound.
* **B3/B6:** N₊(p) = (1/48)·#{(x, y) ∈ ℤ³ × ℤ³ : x·y = 1, |x × y|² = tp, x × y ≡ x + y (t)} (up to stabiliser
  weights) is a lattice-point count on a split quadric in ℤ⁶ with moving congruence; its average is the main term only.
* **Thm 2.2 (O205):** N₊ = Σ_{w∈X_p} r(T_w, I₃)/48 is a family-sum of Fourier coefficients of the genus-2 theta series of
  I₃ (= Siegel Eisenstein series, one class) — a family extraction, not a modular generating function.

## Cheap numerics
* `scripts/y1_three_squares.c`: (iii) ⟺ Diff = {2} on all 81 857 words of odd n ≤ 3001 (0 mismatches); χ = −1 never
  lifts; 7 824 words with χ = +1 but Diff ⊋ {2} (composite n, e.g. n = 21, (1, 2, 23): 21 = x² + y² impossible) do not
  lift; all 736 words of odd squares ≤ 2601 lift; every lifting word with n ≤ 151 has a lift with x × y ≡ x + y (t).
* `scripts/y1_z3_gram.py`: (iv) for primes, H2 for squares, and (iv) ⟺ Diff = {2} for composites, n ≤ 151 (1 970 words) and
  n ≤ 451 (see TWO_FIBRES.md), 0 failures.

## Assessment
EXACT DICTIONARY (PROVED), promise 2/5. It makes the χ = +1 fibre completely explicit (conic over 𝔽_p mod the cube
group) and turns ES-five(p) into a non-embeddability of one explicit integer matrix. It is the first point where the two
fibres become *asymmetric in a usable way*: the char-2 fibre is a class-number-one world where counting is exact (Siegel =
genus), while χ = −1 has no such model. Taken deeper in TWO_FIBRES.md.
