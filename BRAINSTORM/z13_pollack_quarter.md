# z13_pollack_quarter — e*(n) ≪ n₀^{1/4+ε} for n ≡ 1 (mod 8) (O237)

**Idea.** Least prime with prescribed values of several quadratic characters: Pollack IJNT 2014 Thm 1.4 (detector
forms ξ ∈ ℤ[X], bound W^{1/4}f^ε, W = product of conductors in ξ±; Burgess + Vinogradov–Linnik; ineffective).
**Result (PROVED rel. Pollack).** ξ = (1−χ₋₄)(1−χ_{n₀}): W = 4n₀ ⇒ e*(n) ≪_ε n₀^{1/4+ε} (n ≡ 1 (8), non-square);
n ≡ 5 (8): ξ = (1−χ₋₄)(1+χ₈)(1−χ_{n₀}), W = 256n₀² ⇒ n₀^{1/2+ε}. Odd squares a²: p^{1/4+ε} via d = n/p if some
p | a is ≡ 1 (8), else p^{1/2+ε}. (O236: rad(n)^5 effective.) (R242 repair) Effective/explicit: e*(p) ≤ (p−5)/8 for primes p ≡ 1 (8), and
e*(a²) ≤ (p−5)/8 if p | a, p ≡ 1 (8) (CAP_DOWN Cor 2.2, via Pollack JNT 187 (2018) Thm 1).
**Barrier for n ≡ 5 (8).** The bad windows' forced non-residue is 2 itself (usable only when ord_q(2)/2 ≤ v₂(K), e.g. always at q = 3 — R243 repair; no exponent gain); any detector excluding them has two
conductor-n₀ characters in ξ± (equivalently a 2-dim Burgess problem χ(a² − 2b²) needing side n₀^{1/8}, while available bounds are nontrivial only from side n₀^{1/4} — R242 repair). Assessment.
**Label.** PROVED (relative to Pollack Thm 1.4, read from the author's PDF) / Assessment for the barrier.
