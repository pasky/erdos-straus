# z30_local_main_term — an explicit, T1-compatible "singular series" for (★) at one prime (O260; SINGLE_P_COUNT §3)

**Idea.** Hardy–Littlewood for Goldbach has r(N) ~ 𝔖(N)N/log²N at a single N. For (★) build the analogue pair by pair:
condition the event p ≡ −(u+B) (mod 4uB) on p mod gcd(4uB, Q) (bounded Q) and on the square class of p (genus), giving
M_Q(p); it vanishes at squares and uses only p mod Q and χ_p.
**Results (EVIDENCE).** Residual dispersion against swap-Poisson: 1.88 (M₀) → 1.375 (genus) → 1.10 (Q = 720720) on
[10⁵, 4·10⁵); but after removing exactly-reproduced small-smooth hits the non-local part is still overdispersed ≈ 1.7–1.9
(stable from Y = 30 to Y = 100). With only p mod 720720 and χ_p, the two highest-risk primes < 4·10⁵ are 577 and 409,
both failures. Main terms underestimate the mean by ≈ 10 % (an unmodelled prime singular factor).
**Iteration.** v1 "residual is Poisson after Y = 30" was a baseline artefact (exact smooth hits counted in the baseline);
corrected to the two-baseline statement.
**Barrier screen.** B6: these are statistics over p used only to calibrate the error size at one p (goal 4), not to
prove anything at one p. B3: main term polylog — unchanged. T1: passes (all 499 odd squares ≤ 10⁶: everything 0).
**Assessment.** A usable calibration tool and Conjecture 4.2's main term; not a mechanism. Spark: model the remaining
×1.8 as divisor-sharing clusters (compound Poisson over the integers p + u, 4Cp + 1).
