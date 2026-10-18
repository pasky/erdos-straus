# z36 — What the 2026 Zaremba method really needs: density, not just a power count (O266 memo 1)

## Idea
Extract the exact quantitative input of the pointwise Zaremba proofs (Shkredov arXiv:2603.14116v2; X. Zhang
arXiv:2605.02518v2) so that any ES transfer can be screened by one number. Details: ZAREMBA_TRANSFER.md §1.

## Literature (read in the arXiv PDFs, 2026-10-18)
* Shkredov Lemma 13 (Cantor structure Z_M(t) = ⊔ intervals of length ≥ q/t²), Cor 16 (|A ∩ B^{−1}| = |A||B|/q +
  O(√(|A||B|)N^{−κ}) for A, B = Λ ∔ [N]), §5.1 (t = q^{1/2−ε}, N = q^{2ε}, condition (132)–(133) ε ≫ 1/M), (151)/(156)
  ε < 1/18, Appendix (158) M = 22000 for primes, κ ≥ 2^{−1656}.
* Zhang Thm 3.6 ((a + 2j)(b + 2j) ≡ 1, j ≤ N = q^{2τ}; main term φ(q)|A||B|N/q², error q^ε|A||B|N^{1−η}), (3.8) τη > 1/M,
  Remark 1.3 ("Lowering this bound to 5 … requires a new idea"), Remark 1.4 (q-dependent generating set, |S| ≈ q^{2τ}).

## The threshold (Assessment from the sources)
Main term beats error iff |A|N^{κ} ≫ q (Shk (132)) with |A| ≍ q·t^{2w−2}: ε ≳ (1−w)/(2(κ+1−w)); the middle-window analysis
needs ε ≤ ε₀ = 1/18. Together: **1 − w ≤ κ/8** (16(1 − w) ≤ 2κ at ε = 1/18), i.e. the half sets must have density ≥ q^{−O(κ)}.
The campaign's barrier M1 ("power-size main term") is too weak a description: Zaremba with M = 5 has a power count
q^{0.67} and is still out of reach. Sharpened: **M1⁺ — the two glued sets have density q^{−o_κ(1)} at the gluing scale.**

## Barrier screen
B3 (scale): ES-five has effective dimension w = 1/2 exactly (|S_{≤3} ∩ [scale t]| ≍ p/t); the threshold needs
w ≥ 1 − O(κ). B6: the method is pointwise (no average), so B6 is not the issue; B2 is not the issue in CF coordinates
(fixed modulus p, DEDEKIND_ES Cor 4.6); the issue is purely M1⁺ + the character (memo z36_chi_twist_window). T1: the
method holds at squares (Zhang: all q), so it cannot by itself prove any rung of the ES ladder (all rungs fail at m²).

## Cheap numerics
None needed (source extraction). Effective dimensions of ES-ladder rungs: memo z36_hj_cantor_dimension.

## Assessment
PROVED-from-sources reading (labels: the preprints are unrefereed). Value: a one-number screen for any CF transfer.
