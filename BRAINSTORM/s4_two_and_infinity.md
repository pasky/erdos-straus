# s4_two_and_infinity — the numerator lives at 2, positivity lives at ∞, and the algebra coupling exactly {2, ∞} is Hamilton's: (J)49 × (J)32 × (J)48 (O218)

**ES is not solved here.** Labels as in DISCOVERIES.md. Cross-combination asked for in O218 (3): "full T1 only for 4
(J)49 × χ-fibre (J)32", with the archimedean bit of s4_three_bits_meta.

## Idea
Separate the places. For M ≥ 1 let Ω₂^{(M)} be the M-slice region (M | A, B, t, u or v) on X_n (MODEL_SPECIFIC
Lemma 3.0: M-slices of positive words give M/n). The three-bit law (s4_three_bits_meta) is numerator-free:
ε_∞ = positivity, ε_n = χ, ε₂ = membership in Ω₂^{(4)}.

## Statements
**T1-place lemma (PROVED, elementary).** (a) If 4 | M then Ω₂^{(M)} ⊆ Ω₂^{(4)} (M | x ⟹ 4 | x), so every positive
M-certificate has χ = −1 and full T1 for M is inherited from 4 — this is the one-line reason behind (J)49 SHARP 2
(which proves it via ET §4, d ↦ hd); (b) Ω₂^{(M)} = Ω₂^{(4)} ∩ {positive} ⟺ M = 4 among 4 | M ((J)32 Thm 3.1(a,b),
CERTIFIED there); (c) for 4 ∤ M the M-slices are not contained in Ω₂^{(4)} and full T1 fails for M ∈ {3, 5, 6, 7, 11,
19} ((J)49, CERTIFIED there).
**Consequence (PROVED from (a)–(b) and L1).** The archimedean bit is *the same for every numerator* (D does not depend
on M); all numerator-specificity is 2-adic. "4-specific" ((J)41) and "archimedean" (this wave) are therefore two
different places, and an input that is both must *couple 2 and ∞*. Over ℚ the coupling of exactly {2, ∞} is the
Hilbert symbol (−1, −1)₂ = (−1, −1)_∞ = −1, i.e. **the Hamilton quaternions B_{2,∞}** — which is precisely the C₀ of
every non-certificate positive word (CHI_FLIP Cor 1.3) and the ℤ³ model of (J)48.
So: **ES-five(p) ⟺ not every positive path lattice of det p is "Hamiltonian"** (C₀ ≅ B_{2,∞} ⟺ embeds as a Gram
of integer vectors, TWO_FIBRES Thm A) — the 4-specific archimedean input is exactly the Hurwitz order's class
number one, already exploited by (J)48.

## Construction attempts
1. *Hurwitz factorisation.* Hurwitz quaternions have unique factorisation up to units/metacommutation (Conway–Smith,
   *On quaternions and octonions*, Ch. 5). A non-Hamiltonian word is one whose binary T_w is not the Gram of two
   Lipschitz/Hurwitz-pure vectors; since ℤ³ has class number one, "T_w is represented" is decided by local densities,
   i.e. by the 2-adic bit itself — circular (no information beyond ε₂). (Assessment.)
2. *Count on the Hamilton side.* N₊(p) (Hamiltonian words) and |X_p| are both word counts, not representation numbers;
   Siegel's exact formula for r(I₃, T_w) does not count words. Sign dominance N₊ ≤ N₋ is false ((J)48). Dead.
3. *Harness.* The coupling statement is 4-specific by construction (for 8: Ω₂^{(8)} ⊊ Ω₂^{(4)}, and 8/131, 8/241 have
   χ = −1 words but no 8-slice ((J)32)), and holds for 7 trivially vacuously (no χ-fibre). It passes the harness
   because it is a reformulation.

## Barrier screen
T1: built in. B2: the words are the lottery. (J)41 numerator-blindness: passed (4-specific). Nothing new forced.

## Cheap numerics
None new: (b), (c) are (J)32/(J)49 certificates; L1 from `scripts/s4_signed_nadic.py`.

## Assessment
A clean place-by-place synthesis (PROVED parts are elementary): numerator ↔ 2, positivity ↔ ∞, and their unique
coupling over ℚ is the Hamilton algebra; a working ES input must be a statement about Hurwitz-side lattices at p
(non-embeddability of some path lattice in ℤ³) — which is TWO_FIBRES Thm A, a dictionary with no forcing. Promise 1/5.
