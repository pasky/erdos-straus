# y1_cerednik_swap — Cerednik–Drinfeld / Ribet: the two fibres of X₀(2p) are the two trees of the Shimura curve X^{2p} (O209)

## Idea (brief item (b))
O205: χ = −1 words live at singular points of X₀(2p)_{𝔽_p} (Eichler level 2 in B_{p,∞}), χ = +1 words at singular points
of X₀(2p)_{𝔽₂} (Eichler level p in B_{2,∞}). Is there an interchange/level-raising/JL transfer that *forces* a word into
the char-p fibre unless n is a square?

**Dictionary C1 (Assessment; standard Cerednik–Drinfeld + Ribet).** Let X^{2p} be the Shimura curve of the indefinite
algebra of discriminant 2p (maximal order). Cerednik–Drinfeld: X^{2p} ⊗ ℚ_ℓ is a Mumford curve for ℓ ∈ {2, p}, with dual
graph of the special fibre Γ_ℓ\𝒯_ℓ, where Γ₂ ⊂ (B_{p,∞} ⊗ ℤ[1/2])^× acts on the 3-regular tree 𝒯₂ and Γ_p ⊂
(B_{2,∞} ⊗ ℤ[1/p])^× = (Hurwitz order)[1/p]^× acts on the (p + 1)-regular tree 𝒯_p (invariants at ℓ and ∞ swapped).
Edges of Γ₂\𝒯₂ = Eichler orders of level 2 in B_{p,∞} = singular points of X₀(2p)_{𝔽_p}; edges of Γ_p\𝒯_p = Eichler orders
of level p in B_{2,∞} = singular points of X₀(2p)_{𝔽₂} (Ribet's bimodule: the character groups of J₀(2p) at p and of
J^{2p} at 2 are built on the same edge set, and symmetrically). So:
* **χ = −1 words = path-shaped edges of the 2-adic tree quotient (the supersingular 2-isogeny graph, CONSTRUCTIVE (J)35);**
* **χ = +1 words = path-shaped edges of the p-adic tree quotient by the Hurwitz group**, a quotient with 2 vertices
  (class number one) and ≈ (p + 1)/12 edges = P¹(𝔽_p)/A₄ — made explicit in y1_hurwitz_lift H4 (conic over 𝔽_p mod the cube group).
The swap X₀(2p) ↔ X^{2p} exchanges "which fibre is the tree of which algebra", so the two signs of ES are the two
**p-adic/2-adic uniformisations** of one Shimura curve. T1 (n = m²): no prime fibre at all; every word is a Hurwitz edge.

**Screen of the "forcing" hope (PROVED negative facts).**
(F1) Jacquet–Langlands/Ribet act on ℤ[edges] as Hecke modules; the words are a *subset* of edges carrying extra data
(special endomorphisms i, j with ⟨i, j⟩ = 1 and level-t ring condition). Existence of a member of a subset is not a
Hecke-module statement (B2; DIFF_DEEP: "∃ curve" is vacuous; CONSTRUCTIVE §5: the χ = ±1 Hecke modules share no cusp
eigenvalue at 5 primes, so transfers carry only the main term).
(F2) Level raising (Ribet) produces congruences between forms of level p and 2p (or 2 and 2p) when a_p ≡ ±(p + 1); it is a
statement about eigenforms mod ℓ, not about which edges carry path data. No existence of a χ = −1 word follows (B6: it holds
or fails uniformly in families of p where ES-five is known by Mordell certificates).
(F3) Mass bookkeeping (Assessment): Eichler masses are (p − 1)/4 (level 2 in B_{p,∞}) and (p + 1)/12 (level p in B_{2,∞}),
ratio → 3 — the same 3 : 1 as the cell ratio 240 : 80 of Lemma 2.1 (O205). But per class of p mod 8 the census ratio
Σ N₋/Σ N₊ over primes ≤ 10⁶ is 1.55, 2.25, 2.12, 5.42 (p ≡ 1, 3, 5, 7), so the words are **not** mass-equidistributed
fibrewise; the split is 2-adic (cells), as Thm 1.1 of CHI_FLIP says.

## Literature
Cerednik (1976), Drinfeld (1976); Boutot–Carayol, *Uniformisation p-adique des courbes de Shimura* (Astérisque 196–197,
1991); Ribet, *On modular representations of Gal(ℚ̄/ℚ) arising from modular forms*, Invent. Math. 100 (1990) (§4 bimodule);
Kurihara (1979) for the dual graphs; Lubotzky–Phillips–Sarnak (1988) for Hurwitz quaternions acting on 𝒯_p.

## Barrier screen
B2 (subset of edges), B6 (Hecke/JL statements are uniform in families), T1 respected (squares: Hurwitz side only).
Thm 2.2 (O205): any modular object built on edge sets is holomorphic-modular in the level aspect, not in n.

## Cheap numerics
`scripts/y1_conic_orbits.py` (H4): #(P¹(𝔽_p)/S₄-orbits on the conic) = #𝔊⁺_p for 9 of 10 primes ≤ 109 (onto, not always
injective). Census ratios above (`scripts/si_census.c` 10⁶).

## Assessment
Dictionary (Assessment-level, standard inputs); the forcing hope is screened negative (F1–F3). Its useful by-product is the
asymmetry: the χ = +1 tree has the class-number-one Hurwitz group (explicit), the χ = −1 tree does not. Promise 1/5.
