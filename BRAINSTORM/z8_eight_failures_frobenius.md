# z8_eight_failures_frobenius — 8/p failures as a missed ℚ(ζ_{8u})-class inside the χ = −1 half (O232)

**Idea.** For ν = 8 the coprime slot set at level u (u ≡ 1 mod 4) is the single class A ≡ −1 (mod 8u): one half of
O225's forbidden half (the other half is A ≡ 3 mod 8, i.e. 4 ∥ the slot). 8/p fails iff every χ = −1 word of p has its
4-slot with v₂ exactly 2 — an extra "ζ₈-bit" of Frobenius that no genus/T1 mechanism controls.

**Literature.** FOUR_SPECIFIC §2 (S₄ = S₄^{odd} ⊔ S₈, Lemma 2.1: v₂ of the slot decides parity; failures 3, 11, 17, 59,
131, 241, 449 of S₈); (J)32 Lemma 2.1(b).

**Barrier screen.** B2/B6: the ζ₈-bit is a Chebotarev lottery on the same divisors; nothing forces it. T1: holds (8 ≡ 0
mod 4). The failures are consistent with a probability-½-per-word model.

**Cheap numerics.** p = 131: 21 words, 14 with a 4-slot, all slots ≡ 4 (mod 8); p = 241: 6 of 15, all ≡ 4 (mod 8)
(computed in this task). (R235 repair: 131 ≡ 3 mod 4, so its 4-slot words are those with (A/131) = +1, not the χ = −1 half;
R235 counts 22 / 16 words (t, u ≤ v) — state the word convention.) Under the ½-per-independent-word model, P(all 14 miss) ≈ 6·10⁻⁵ — but words share divisors
(A, A* are coupled; FOUR_SPECIFIC §2.1 notes a small-t bias v₂(tp + 1) = 2 for t ≡ 3 mod 8, p ≡ 1 mod 8), so the
independence model is wrong; 131 ≡ 3 (mod 8) and 241 ≡ 1 (mod 8) sit in the classes where 8 has no e ∈ {1, 3} slice.

**Assessment.** EVIDENCE/description. The sign-field picture predicts that every T1-numerator other than 4 has a
"bit beyond the sign" and hence finitely or infinitely many lottery failures; it does not decide which. No spark.
