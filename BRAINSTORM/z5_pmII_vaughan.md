# z5_pmII_vaughan — PM-II for almost all primes, and why 3361 is ≡ 1 (mod 84) (O229; CAP_GROWING §2)

**ES is not solved here.**

## Idea
PM-II (BRIDGE_WORLDS §5, CONJECTURE): every prime p ≠ 3361 has a Type II certificate with prime modulus h
(4cd | h + 1, h | p + 4c²d). Vaughan's large sieve uses exactly such certificates.

## Literature
Vaughan 1970; Pomerance–Weingartner Thm 1.3; paper/vaughan-loglog-note.tex (its loglog gain uses composite moduli kℓ).

## Result
Lemma (PROVED): Vaughan's class n ≡ −uv^{−1} (mod ℓ), uvw = (ℓ+1)/4, is n ≡ −4u²w — a prime-modulus certificate with
(c, d, h) = (u, w, ℓ). Hence **#{p ≤ N : PM-II fails} ≪ N exp(−c(log N)^{2/3})** (PROVED relative to Vaughan).
Covering moduli: among h ≡ 3 (4) ≤ 20 000 only h = 3, 7 have firing classes containing all non-residues
(`scripts/z5_pm_cover.py`), so a PM-II failure is ≡ 1 (mod 12) and a QR mod 7 (3361 ≡ 1 mod 3360 = 2⁵·3·5·7).

## Barrier screen
Pointwise PM-II ⇒ Type II-ES at all p ≠ 3361: B2/B3/B6 verbatim. The average theorem is B6-safe. The loglog note's
multiplier trick needs composite h, so it does not transfer.

## Cheap numerics
z5_pm_cover.py (above). Census and the exception list are in BRIDGE_WORLDS §5 / y3_primemod_census.

## Assessment
PROVED (corollary-level). Answers goal (2)'s "almost-all with explicit exceptional set"; no structural reason for
p > 3361 found (none can be had without solving Type II-ES pointwise).
