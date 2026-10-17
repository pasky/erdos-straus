# z24_level_dichotomy — cap 0 is a level-≥-2 event in the window, cap ≥ 1 is not (O252; FORCED_WINDOW §2)

**Idea.** Locate B2 in window language: what congruence does a certificate impose, on which variable, at which level?
**Result (PROVED, elementary; ET Type II in window coordinates).** A cap-0 certificate δ at window m is a coprime pair
(u, v) = (∏_{δ>0} s^δ, ∏_{δ<0} s^{−δ}) with uv | K_m and m | u + v; then m is the least positive residue of −p mod 4uv and
4uv ≥ 2m. Conversely every coprime (u, v) with (−p mod 4uv) | u + v gives one (FORCED_WINDOW Prop 2.1). Read in m (p fixed):
level ≥ 2 — beyond EH and beyond the Friedlander–Granville range. Read in p (window fixed): level ≤ 1 + o(1) — this is why
almost-all theorems exist (B6 made quantitative). Cap e ≥ 1 decouples: the one-prime witness at q | s^j + 1 needs only
p ≡ −q (mod 4s), p ≢ −q (mod s²), modulus 4s² while q can be ≈ s^j (Prop 2.2) — level < 1, sieve-accessible.
**Barrier screen.** This is B2/B6 itself, not a way around them; it explains why every provable pointwise/almost-all result is
at cap ≥ 1 and why "cap ≤ 1 for all p" is not "cap 0 up to an error".
**Label.** PROVED (elementary). Spark: is there a cap-0 family whose certificate modulus is < window (level < 1 in m)? By the
proposition: no — u + v ≥ m forces 4uv ≥ 2m for every cap-0 certificate.
