# z11_label_cantor — mixed points as label points: CRT of squares (O235)

**Idea.** Let P = integer square points of 4^x + k (k = 105: {2, 3, 4, −2}). A *label point* σ ∈ Π_ℓ P puts an integer
square point in every ℓ-adic component of the exponent. O232's mixed point μ* is the label point (4 off 3, −2 at 3).
**Lemma (EXP_NEAR_SQUARE Lemma 1.2, PROVED).** At σ-pure primes (all ℓ | ord_q(4) with one label x) ν(σ) ≡ s_x²; a modulus
built from pure primes sees a unit square (CRT of squares) and lies in no ET class. Only σ-mixed primes (or q | s_x) cover.
The divisor classes D_q of the square points depend only on ℓ | ord_q(4) — a label point switches them off by giving those
ℓ another label (D₁₉ needs μ₃ ≡ 4 mod 9, D₄₁ needs μ₂, μ₅ ≡ −2, …).
**Result (CERTIFIED, replayed by z11_check_cantor.py).** The binary set Π_ℓ{4, −2} of k = 105 is covered by 10 classes
with period support in {2, 3, 5, 11, 17, 19, 29, 47}. The quaternary set Π_ℓ{4, −2, 2, 3}: 4 uncovered patterns of 4^11 at
ℓ ≤ 31; the label tree (z11_cantor_tree.py) does not close at QMAX 10⁶ (survivors ×3 per prime beyond ℓ ≈ 41).
**Barrier screen.** Not a barrier; a structural description of where B1-type coverings get expensive over Ẑ.
**Assessment.** PROVED lemma + CERTIFIED binary core; quaternary core open (EVIDENCE: no sterile label point found).
