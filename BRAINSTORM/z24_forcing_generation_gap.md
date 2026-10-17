# z24_forcing_generation_gap — forced generators stop at log q, generation starts at log q·log log q (O252; FORCED_WINDOW §5)

**Idea.** Plug "every element of F_q^* is a short product of small primes" (Erdős–Rényi / Bach / Konyagin–Shparlinski) into a
window whose K is forced (CRT) to contain all primes ≤ y.
**Result.** (a) Forcing: P(y) | K_q costs q ≳ P(y) for a positive proportion of p, so y ≤ (1 + o(1)) log q. (b) GRH ⇒ every
element of F_q^* is ∏_{s ≤ C log⁴q} s^{±1,0} (Prop 5.1, PROVED rel. GRH). (c) GRH for Dedekind zeta functions + Lagarias–Odlyzko ⇒ for each odd ℓ, i.o. primes
q ≡ 3 (4) have all primes ≤ c_ℓ log q log log q ℓ-th powers (Prop 5.2): no all-q generation statement holds at the forcing scale.
(d) Pigeonhole: with k generators some ψ ≠ 1 has all ‖θ‖ < N^{−1} once |U| > N^k (Prop 1.3) — genericity must be measured at
the Diophantine scale 1/L, i.e. lattice balance (z24_balanced_primes_W).
**Barrier screen.** Subgroup level is already free (forced parity, CAP_POINTWISE Thm 1.1: −1 lies in every odd-index subgroup),
so Kummer/Chebotarev obstructions only kill covering, not the target; the box level is Diophantine, not Frobenius.
**Label.** PROVED (a, d), PROVED rel. GRH (b), CONDITIONAL on GRH (c).
