# z13_even_windows — the 2-adic repair of the self-generated mute window (O237)

**Idea.** O236 imposed K = (n+q)/4 odd (square shot d = Q², Q odd). Allow K = 2^t K′ even and use the general Type II
divisor d = 2^t·Q′² (odd 2-exponent allowed, ≤ 2t: no 2-adic denominator).
**Result (PROVED, CAP_DOWN Lemma 1.1, Thm 1.2, Prop 1.3).** Every prime q ≡ 3 (4), (q/n) = −1 is a forced (always firing) window
unless n ≡ 5, q ≡ 3 (mod 8) and v₂(n+q) is odd. Explicit witness d = K·s^{ord_q(s)/2} (s | K′ a non-residue with odd
exponent) — cap ≤ (q−3)/4, sharp at a single window (Prop 4.1(a)). For n ≡ 1 (8): all q ≡ 3 (4) fire.
(R242 repair) Excluded windows are not forced but mostly still fire (≈ 97 % in R242's scan; e.g. n = 5, q = 67 is dead).
(R243 repair) In the excluded case d = K·2^{ord_q(2)/2} gives cap 0 whenever ord_q(2)/2 ≤ v₂(K); q = 3 always fires (d = 2K).
**Why it matters.** It turns the accepted Frobenius set into {χ₋₄ = χ_{n₀} = −1}, whose Pollack detector has W = 4n₀
(exponent 1/4) — see z13_pollack_quarter.
**Label.** PROVED; numerics EVIDENCE (all p ≤ 10⁶ exact).
