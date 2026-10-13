# R195 — independent hostile review of FF_MUTE.md (O195)

Reviewer: R195 side agent (independent of the author's self-review in reviews/synthesis-two-hostile-review.md).
Document reviewed: FF_MUTE.md at merge of side-agent/ff-mute (commit 2f212a84 + parent repairs e60d4352).
From-scratch scripts: `scripts/review_fm_*.py` (own GF(q) incl. q = 4, 8, 9, own F_q[T] arithmetic, own power-residue
symbols by direct exponentiation; nothing imported from `fm_*`).

(in progress)

## Summary verdicts

* **Prop 2.1 (mute shot identity): SOUND.** Re-derived: Ef = P + AQ², f ≡ −1 (mod A) ⇒ A | P + E; the key relation
  X + Q² = E(f+1)/A gives 1/Y + 1/z = E/(PX) = A/P − 1/X. Degrees deg X = 2deg Q − d, deg Y = n + d − k,
  deg z = n − k, all monic (lc(P)=lc(X)=lc(f+1)=lc(A)=lc(Q)=1; f + 1 monic needs d ≥ 1, true in char 2 as well).
  Parity: AfX = P(f+1) + AQ² and s ∤ f (s | f, s | Q ⇒ s | P), so v_s(X) = σ when σ < 2c and v_s(z) = 2σ − 2c;
  if σ ≥ 2c, v_s(z) = v_s(X) + σ − 2c ≥ 0. Type II shape: gcd(f, P) = 1 ⇒ P ∤ E ⇒ P ∤ X. The low-shot variant
  (deg AQ² < n) also re-derived: E monic of degree n − d, X of degree n − k, deg z = 2n − 2k + d − 2deg Q > n − k.
  Numerically: every monic divisor f ≡ −1 (mod A) of random shots P + A s^{2j} (P composite allowed, both degree
  regimes), q ∈ {2, 3, 4, 5, 7, 8, 9}: identity, monicity, NC with min degree exactly n − k, parity, Type II shape
  (P prime): 0 failures (`review_fm_signs.py`, data/review_fm/signs_*.txt).
* **Cor 2.2: SOUND.** z = P·X·(f+1)/(A·Q²) with A | f + 1 and gcd(A, Q) = 1, so the only possible denominators
  are s | Q, and v_s(z) ≥ 0 ⇔ σ ≥ c in both parity cases. Checked on the same shots (0 mismatches of
  "z ∈ R ⇔ f ≡ −1 mod AQ").
* **Lemma 3.1: SOUND.** (R/f)^* cyclic of order q^d − 1; ⟨s²⟩ = squares; j₀ shifted by multiples of q^d − 1
  (any multiple of ord(s²) would do). Uses f ∤ M (so f ≠ P, s and gcd(f, P) = 1) — stated.
* **Lemma 3.2: SOUND.** Re-derived: (−1/f) = ε^d since 1 + q + … + q^{d−1} ≡ d (mod 2); (P/f) = ε^{nd}(f/P);
  (A/f) = ε^{kd}(f/A) (multiplicativity over the prime factors of A) and (f/A) = (−1/A) = ε^k. Hence
  (−PA/f) = ε^{d(1+n+k)+k}(f/P) = 1 ⇔ (f/P) = τ. ℓ-part: (s/f)_ℓ = (−1)^{((q−1)/ℓ)hd}(f/s)_ℓ, and the sign is 1
  for odd ℓ (q odd) and in char 2. Checked by direct exponentiation, without reciprocity, for
  q ∈ {2, 3, 4, 5, 7, 8, 9} (incl. ℓ = 3 at q = 4, 7; ℓ = 7 at q = 8; ℓ = 2 at q = 9 where ε = +1):
  ≈ 1100 random (A, P, s, f), 0 mismatches.
* **Lemma 3.3: SOUND.** −Σ_{deg F=d}Λ(F)χ(F) = Σ α_i^d over ≤ D' − 1 inverse roots of modulus ≤ √q; prime powers
  contribute ≤ Σ_{e ≤ d/2} q^e ≤ q^{⌊d/2⌋}·q/(q−1) ≤ 2q^{d/2}. Lower bound for dπ_q(d) likewise.
* **Lemma 3.4: SOUND.** Root-counting injection f ↦ its d roots in F_{q^d} (f ≠ s ⇒ s(α) ≠ 0), orthogonality, and
  Weil for the separable (h distinct roots) monic s — not an ℓ-th power since squarefree with h ≥ 1. The i = 0 term
  is ≤ q^d; the (ℓ−1)/ℓ factor is dropped (harmless).

## Defects

## Checks performed
