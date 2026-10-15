# R235 — hostile review #1 of O232 (SIGN_FIELDS.md, BRAINSTORM/z8_*.md, data/z8/)

Reviewer: R235 (side-agent/review-sign-fields). Merged side-agent/sign-fields at 069d5e83 (README conflict resolved by
keeping both sides). From-scratch scripts: `scripts/review_r235_cert.py` (certificate checker, sympy, no ec_cert/z8
imports), `scripts/review_r235_brute.py` (independent ES solver via (ay − d)(az − d) = d²), further `scripts/review_r235_*.py`.

## Summary verdicts
(filled in progressively; see sections below)

| claim | verdict |
|---|---|
| Thm 1.3 (ES for all 4^s + k, nine k) | SOUND (label PROVED, computer-assisted, justified) |

## 1. Theorem 1.3 — headline

**Independent checker** (`scripts/review_r235_cert.py 300`). Semantics re-derived from the JSON: n_s = 4^s + c,
class (M, r), x, y, z ∈ ℚ[n] given low-degree-first. For every class of all nine certificates:
1. 4xyz − n(xy + yz + zx) = 0 in ℚ[n] (sympy expansion): all 30 classes pass.
2. Integrality: with D = lcm of coefficient denominators, D·p ∈ ℤ[n] and D·p(n) mod D is D-periodic in n, so
   checking n = r + Mt for t < D/gcd(D, M) is exhaustive (different method from ec_cert's finite differences): pass.
3. Positivity: largest real root R of each coordinate (sympy real_roots), positive leading coefficients; class used only
   when n > R, else falls back to brute force: pass.
4. Periodicity (re-derived): write M = 2^e M′. For s ≥ ⌈e/2⌉, 4^s ≡ 0 (mod 2^e) so n_s ≡ c (mod 2^e); and
   n_{s+L} − n_s = 4^s(4^L − 1) ≡ 0 (mod M′) iff M′ | 4^L − 1 (checked: pow(4, L, M′) = 1). Hence n_s mod M depends only
   on s mod L for s ≥ S₀ = max⌈e/2⌉ (S₀ = 1 for k = 225 because of M = 2716 = 4·679, else 0). Coverage of the L residues
   from S₀ on: pass; redundant direct check n_s ≡ n_{s+L} ≡ n_{s+7L} (mod M): pass.
5. Exact integer verification of a class solution for every s ≤ 300: pass. Only s = 0, k = 225 (n = 226, even) needed
   brute force: (57, 6442, 41492922).
6. Independent brute force (no certificate) for s ≤ 20 for all 13 offsets k ≡ 9 (mod 24), k ≤ 297
   (`review_r235_brute.py 20`): all solvable.
The author's checker `ec_cert.py` (run with MMAX = 600) also passes all nine — consistent with the claim.

**T1 / square control.** Squares in the families come from (a − 2^s)(a + 2^s) = k. Complete list (s ≥ 0):
k = 9: s = 2, 25 = 5²; k = 57: s = 3, 121 = 11²; k = 129: s = 6, 4225 = 65²; k = 153: s = 2, 169 = 13²;
k = 201: s = 5, 1225 = 35²; k = 225: s = 3, 289 = 17²; none for k = 81, 177, 249. My checker confirms each of these is
covered by a **divisor class** D_q with q | a (D₅, D₁₁, D₅, D₁₃, D₅, D₁₇ respectively) — real solutions obtained by
scaling ES(q), not a polynomial ET family "solving" a square (which would contradict Mordell/Schinzel). No non-D class
contains a square member (the ec_cert T1 test to s < 20000 also passes). Note that k = 81 is a square but 4^s + 81 is never
a square (factor pairs (1,81), (3,27) give 2^{s+1} ∈ {80, 24}).

**Mordell-hard members.** Recomputed residues mod 840 for s ≥ 2: k = 57: s ≡ 3 (6) → 121; 153: s ≡ 2 (6) → 169;
177: s ≡ 5 (6) → 361; 225: s ≡ 3 (6) → 289, s ≡ 0 (6) → 121; k = 9, 81, 129, 201, 249: no hard members. Matches §1.3.
**Survey list.** k ≡ 9 (mod 24), k ≤ 300: 9, 33, …, 297 = 13 offsets; 9 certified + 4 OPEN — consistent.

Verdict Thm 1.3: **SOUND**. Defects are presentational only (see D1, D2 below).

## Defects
**D1 (MINOR, presentation/novelty; SIGN_FIELDS §1 Thm 1.3 and AGENT_REPORT headline).** Five of the nine offsets
(k = 9, 81, 129, 201, 249) have **no** member in Mordell's six classes mod 840 for s ≥ 2, so ES for them is an immediate
corollary of Mordell's classical mod-840 theorem (plus s = 0, 1 by hand); the certificates just re-encode that. Of the
other four, the hard-class members are for k = 153 *all* multiples of 13 (4² + 153 = 13², ord₁₃4 = 6) and for k = 225 the
s ≡ 3 (6) ones are multiples of 17 — divisor classes. The genuinely non-classical content is: k = 57 (s ≡ 9 mod 30, class
mod 2015), k = 177 (s ≡ 5 mod 6, class mod 39), k = 225 (s ≡ 0 mod 6 via mod 39, s ≡ 9, 21 mod 24 via mod 2019, 2716).
Repair: state in Thm 1.3 that for k ∈ {9, 81, 129, 201, 249} the result is Mordell's theorem, and headline the four
offsets with hard-class members.
