# AGENT_REPORT_O208 — Synthesis III over (J)13–(J)38 (branch side-agent/synthesis-three)

Deliverables: `SYNTHESIS_SPARKS3.md` (deep file), 9 memos `BRAINSTORM/s3_*.md` (indexed in BRAINSTORM/README.md),
scripts `scripts/s3_*.py` (all < 15 s). ES is not solved; no infinite case of ES is claimed.

## SHARP:
**Numerator-blindness barrier (SYNTHESIS_SPARKS3 Thm 1.1 + Cor 2.1).** Replace 4 by any M ≡ 0 (mod 4) in the shot
identity (g | n + MQ², g ≡ −1 mod M ⇒ M/n = 1/x + 1/y + 1/z, den z | Q²). Then:
* **M^□(n) is a theorem at every odd non-square n prime to M** (one Dirichlet prime; the key fact is (−M/g) = −1 for
  every odd g ≡ −1 (mod M)), and T1 holds exactly: no M-shot at odd squares. PROVED, elementary.
* But M/p FAILS at 278 known pairs (M ∈ {8, 12, 16, 20, 24}; Pomerance–Weingartner / MODEL_SPECIFIC census), all of
  which have explicit M^□ certificates, and also M^{(S)} certificates with the fixed mute set S = {3, 5, 7, 11}.
  Smallest example: **8/131 = 1/20 + 1/131 + 9/2620**, while 8/131 has no unit-fraction solution and no BM obstruction.
* The same blindness holds over ℤ[ω] (TES^{□₃} is true at all 16 TES failures: (J)28 Thm 3.5 + (J)31; checked to
  N ≤ 27000) and over F_q[T] ((J)30 vs (J)4/(J)26).
* Consequence: every (E1) transport and every (E2) finite mechanism must use an input that is FALSE for the numerator 8.
  Shot identities, overflow duality, T1/BM/Diff-parity, box finiteness, sieves, composition/Vieta and class-group
  pigeonhole are numerator-uniform, so none of them can be that input. The only clean 4-specific input known is the
  numerator-free χ-fibre (S₄ = {χ = −1}, (J)32), which funnels both exits into SQ₅/(S).
* By-product: a **falsification harness** beyond odd squares — 8/n at 131, 241; TES at N(π) = 7, 13, 19, …; ES_q
  failures in F_q[T]. These are places where every local, BM, sieve and relaxation input holds and the exact finite
  search fails. All earlier barrier tests used only odd squares.

## Other results (each in a memo)
* s3_box_bit (PROVED): for a prime g ≡ 3 (mod 4), a □-shot at g exists ⟺ (p/g) = −1, and every Type II ES certificate
  at modulus g forces (p/g) = −1. Numerically the box fires in 9.5% of the (p/g) = −1 pairs and in 0/85939 of the
  others. So the □ relaxation is exactly the sign layer; n ↔ nd slicing relabels the box, and n ↦ nQ₁² enlarges the
  overflow.
* s3_eps_mu_sieve (PROVED): 4tj − 1 | nj + t ⟺ 4tj − 1 | n + 4t². The (J)23 sieve shot and the (J)38 ES slot are
  therefore the same shot with Q = t, and the ES side forces Q small.
* s3_min_scale (EVIDENCE to 10⁷): h_min ≤ 0.81 log³p (max 2495); the Dirichlet □-prime is ≤ 1.46 log²p. Both searches
  end at polylog scale, so the finiteness of the O(p²) box is not the operative difference; the type of firing
  condition is (character versus divisor box).
* s3_lll_lenstra (PROVED relative to Lenstra 1984): at most 11 certificates per Lenstra-regime line. 58% of certificate
  pairs lie there, with ≤ 1 per line observed. LLL decides; it does not produce existence.
* s3_isogeny_mixing (PROVED, elementary): expander mixing needs |S|, |T| > 8N/9, but certificate edges touch
  ≪ p^{1/3+o(1)} vertices. Certificates are spectrally invisible.
* s3_words_parity: σ has the unique fixed word (n+2, 1, 1), and χ is σ-invariant, so #χ=−1 words is even at
  p ≡ 1 (4). The parity of χ = −1 orbits is uniform in every class mod 8 (no parity law).
* s3_vphi_ringmaps (PROVED): there is no ring map ℤ[φ] → ℤ, and not even one to ℤ/2. Galois averaging gives
  8/n = Σ Tr/N, which is a B2 condition.
* s3_order3_numerator: in the TES normalisation, an "SQ₅₃" and a χ₃-fibre slice theorem cannot both hold (logic +
  the 16 failures).
* Not redone: (J)36 × (J)37 is already MARKOFF_ES Prop 7.1(b).

## Labels / caveats for the reviewer
* Thm 1.1 is PROVED from Dirichlet + quadratic reciprocity only. It is triple-checked: all primes < 10⁶ and all odd
  non-squares < 10⁵ for each M ∈ {4, 8, …, 24} (`s3_mbox_check.py`), and odd squares for T1.
* The fixed-S version (M^{(S)}, Gupta–Murty with r ≡ −1 mod M) is an **Assessment (routine transfer, not re-derived)**
  plus EVIDENCE on the 278 failing pairs. Points to check: (r−1)/2 is odd for r ≡ 7 (8), and squares equal 4th powers
  for r ≡ 3 (4).
* Cor 2.1's "which tools are numerator-uniform" is an item-by-item Assessment, not a formal theorem. The formal content
  is the single implication failure R_8(131) ∧ ¬(8/131).
* Lenstra / Coppersmith–Howgrave-Graham–Nagaraj are cited from memory, not checked against the PDFs.
* The FF failure example (q = 5, A = T, degree ≤ 4) is quoted from (J)4.

## Sparks (not pursued)
1. Build the ℤ[ω] word/character machinery for TES and test whether a χ₃-fibre slice theorem exists. If it does, the
   16 failures give non-cube primes where the cubic character is constant on words: a concrete "SQ₅₃ is false".
2. Classify ALL numerators m (not only 4 | m) for which the relaxed variant is a theorem while m/n has failures. For odd m
   the relaxation loses T1 (no fixed (−1/g)); are 9, 13, 15 also "blind"?
3. Run the harness on the existing PARTIAL hatches (H-A growing families, ray-class Remark 10.4): which of them are
   numerator-uniform, and hence dead by Cor 2.1?
4. h_min(p) ≪ log³p? The max ratio 0.81 to 10⁷ suggests an explicit CONJECTURE with the Bach-type scale log² × log.
5. The one-odd half (β) as a second 4-specific target: characterise which cube points (c, d, j) give one-odd solutions,
   and whether one-odd ⟺ some χ-condition.
