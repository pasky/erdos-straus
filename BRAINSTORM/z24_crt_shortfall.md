# z24_crt_shortfall — forced budgets vs the windows they force (O252; FORCED_WINDOW §3)

**Idea (brief).** Choose the window so that K is smooth / divisible by many small primes to large powers: huge exponent budget.
**Result (PROVED).** Covering a window m at cap e needs F_e(K) = ∏(2b_s + 1 + e) ≥ φ(m)/2, and F_e(n) ≤ (e+1)^{ω(n)}τ(n²) =
exp((1 + o(1)) log(3(e+1)) log n/log log n) (uniform in e). Hence windows p^θ ≤ m ≤ 3p need 3(e + 1) ≥ (log p)^{θ−o(1)}; cap-0 covering windows have
m ≤ p^{O(1/log log p)} (Thm 3.1). These bound COVERING only; a single hit (e.g. K prime ≡ −1 (mod m)) is unconstrained. CRT in an interval of h windows gives K with ω ≥ (1+o(1)) log h/log log h; box ≥ window iff
log(e + 3) ≳ log log h (cap ≍ log log p at h = polylog) — matching the covering barrier (log₂p)^{1−o(1)} of CAP_INTERPOLATION
Prop 4.1 from the constructive side. For cap-0 covering at a CRT window m ≍ h the forced part falls short by the factor ≍ log₃p in ω(K) (Cor 3.3).
**Barrier screen.** B3/B4: forced budgets are logarithmic in the modulus they cost (τ(M²) = M^{o(1)}); exponent depth is useless
(2b+1 grows linearly while s^b grows exponentially). Smooth shifted primes (y = x^{0.28}; Lichtman's theorem is for a fixed shift) do not supply boxes of window size.
**Numerics.** Least cap-0 windows use |δ| = 1 in 90–97 % and support ≤ 2 in 91–99 % (z24_least_window): budgets are not used.
**Label.** PROVED (Thm 3.1, 3.2) + Assessment (random-model count (log p)^{A − (α log α − α + 1)}, max ≈ (log p)² at α = 3).
