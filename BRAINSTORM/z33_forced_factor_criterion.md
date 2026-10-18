# z33_forced_factor_criterion — the strongest forced-factor lemma, the exact criterion, and the point n = 1 (O263; §3)

**Idea.** "N ≡ a ∉ H ⟹ a prime factor ∉ H"; choose d so that many forced factors fall in useful cosets; then zero-sum.
**Literature.** LONGSHOT_PIGEONHOLE Thm 2.2 (small factors + one opaque cofactor fail for a positive proportion in every
e-slice); POINTWISE_SIZE Thm C; JOINT_BUDGET Prop 4.3 ("mod divisors of p − 1, p looks like 1").
**Result (PROVED).** Lemma 3.1: the product formula is the only constraint; every multiset with the right product is
realisable (incl. N prime). Prop 3.2: E is forced by (p mod M) iff −1 ∈ Σ(s) ∪ Σ(s)·[L] (s = B-smooth part, L opaque).
§3.3: certificates from forced small factors are exactly the ET Type II classes d | (w + 1)/4, p ≡ −4d (mod w). Thm 3.4:
for every (B, D) the forced rule on all four lines fails at every prime p ≡ 1 (mod M): there N becomes the integer of
"p = 1" (1 + 4d, c + 1, (1 + e)/4) and none of these has a divisor ≡ −1 (resp. a + b ≡ 0 (mod e)).
**Barrier screen.** B1 exactly; T1 automatically (forced ⟹ actual, which fails at squares).
**Cheap numerics.** §7: F₁₀ certifies 98.1 % of primes ≤ 10⁶ (levels ≤ 200), F₃₀ 99.89 %; Haar failure density 1.8 % / 0.22 %;
the excluded class p ≡ 1 (M) is never certified (Thm 3.4).
**Assessment.** (R272 repair, attribution) the classical p ≡ 1 (mod M) obstruction (JOINT_BUDGET Prop 4.3, B1_LINE §4) in
forced-factor language — an analogue of, not a specialisation of, LONGSHOT Thm 2.2 / POINTWISE_SIZE Thm C; low novelty.
