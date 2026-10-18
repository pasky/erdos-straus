# R287 — hostile review of POWER_LADDER_ES.md (O276, k-th power relaxation ladder)

Reviewer branch side-agent/review-power-ladder (merged side-agent/power-ladder-es @ 32fa2bfc). All checks below are
from-scratch (scripts/review_r287_*.py, logs/review_r287_*.txt); the author's scripts were read only to learn the
TES 2-primary normalisation convention.

## Summary verdicts (filled in progressively)

| Claim | Verdict |
|---|---|
| Def 1.1 / Remark 1.2 (exact definition, lowest terms forced) | (pending) |
| Thm 2.1 / Cor 2.2 (odd k: mod-4 covering, T1 dead) | (pending) |
| Thm 2.3 / Lemma 2.4 / Cor 2.5 (even k = ES^□; all n) | (pending) |
| Prop 3.1 (index formula; repair of (J)107 §3.2) | (pending) |
| §4 cap relation | (pending) |
| Thm 5.1 / CERTIFIED / Prop 5.2 (one mute prime) | (pending) |
| §6 TES_(k) bits + EVIDENCE table | (pending) |
| §7 fixed shot r = 3, 11 | (pending) |
| §2.3 / §7 numerics | (pending) |

## Numerical reproduction (from scratch)
* `scripts/review_r287_flat.py 1000000` (42 s, `logs/review_r287_flat_1e6.txt`): own implementation, exact Fraction check of
  4/n = 1/x + 1/y + 1/z, den z recomputed and tested to be Q^k (Q odd, gcd(Q, n) = 1), shape recomputed from valuations.
  * odd k = 1, 3, 5, 7 (Thm 2.1): all 78 497 odd primes ≤ 10⁶, 499 odd squares, 49 odd cubes: OK, Type I at every prime
    of n in all 79 045 cases, max Q over primes = 3.
  * even k = 2, 4, 6, 8, 12 (Thm 2.3): all primes p ≡ 1 (4) ≤ 10⁶ solved with Type II shape both by the first firing
    r ≡ 3 (4) and by the theorem's r ((p/r) = −1, r ≢ 1 mod odd primes of k). Max theorem-r: 131 (k = 2, 4, 8), 251
    (k = 6, 12) — matches the author's 131 / 251. (First-firing r for k = 6 can be ≡ 1 (3) when −p/4 happens to be a
    cube: max 191.)
  * T1 control: 0 shots fire at the first 200 odd squares × 200 primes r ≡ 3 (4) for k = 2, 4, 6.
  * §7 fixed shots (k, r) = (3, 3), (3, 11), (5, 3), (5, 23), plus (7, 3), (9, 11): every prime/odd square/odd cube ≤ 10⁶
    prime to r solved, Type II everywhere. (My max Q differs from the author's (23 vs 11 for r = 3) only because I do not
    exclude squares divisible by 11; immaterial.)
* `scripts/review_r287_tes.py 3000` (`logs/review_r287_tes.txt`): own ℤ[ω] arithmetic; table of §6 reproduced exactly
  (k = 1: 412/412 primes and cubes; k = 2: 209/412 both; k = 3: 134/412 primes, 0/412 cubes), all Type II, and the
  firing set agrees exactly with the criterion "−n/18 ∈ (F₇₃^×)^k" (ω ↦ 8). Lowest terms gcd(Q, Z) = 1 verified;
  a = (g + ω²)/9 = −1 for g = −8 + ω. All class primes g ≡ 10 + ω (18) with N(g) ≤ 3000 have N(g) ≡ 1 (18).
