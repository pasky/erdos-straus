# R268 — hostile review of O258 SYNTHESIS_SPARKS8 (synthesis VIII)

Reviewer: R268 side agent. Status: IN PROGRESS. Scripts: `scripts/review_r268_*.py` (from scratch; author scripts not reused).

## Summary verdicts
(filled in as checks complete)

## Defects
(numbered below)

---
## Claim A — SHARP census (§2.4, Conj. 2.5 evidence): **SOUND** (independently reproduced to 10⁸ in full)

**Re-derivation (reviewer's own "t-form", different from both the author's window and divisor forms).** From
c p + a + 1 = 4acd: w := 4cd − 1 | cp + 1 ⇒ w | 4d(cp + 1) − p·w = p + 4d; put g := (p + 4d)/w, so g(4cd − 1) = p + 4d, i.e.
4d(cg − 1) = p + g. With t := cg − 1: **b = 1 line ⟺ ∃ t ≥ 1, g | t + 1, 4t | p + g** (c = (t+1)/g, d = (p+g)/(4t), and
a = (cp+1)/w is integral because c(p + 4d) ≡ cp + 1 (mod w)). For p = 4i + 1 this is: g ≡ 3 (4) and i ≡ −(g+1)/4 (mod t), and
d ≥ 1 is automatic. Completeness: g ≤ t + 1 and 4t ≤ p + g give **t ≤ (p + 1)/3**, and since g < 4t, g must be the least residue
of −p mod 4t, so the per-p decision is O(p) trivial operations. (The author's bounds m ≤ (p + 4)/3 for the window form and
d ≤ (p + 3)/8 for the divisor form were also re-derived: the window bound from 4a ≤ p + m ≤ p + a + 1; the divisor bound from
g ≡ 3 (4), hence g ≥ 3, and 3(4d − 1) ≤ p + 4d. Both are correct.)
c = 1 line: p = 4i + 1, a + b ≡ 3 (4), i ≡ −(a+b+1)/4 (mod ab); per-p completeness via a ≤ b ⇒ a(4a − 2) ≤ p, b | p + a.

**Engine** `scripts/review_r268_census.py` (numpy residue-class sieve over all p at once for t ≤ T₀ and ab ≤ T₀, then a
complete per-p decision for the primes the sieve leaves). Logs `logs/review_r268_census_1e7.txt`, `logs/review_r268_census_1e8.txt`.
* **Full independent run to 10⁸** (13 s, T₀ = 5·10⁴): 2 880 504 primes p ≡ 1 (4) ≤ 10⁸ (= 332 180 + 2 548 324, matching the
  author's two logs). b = 1 failures **exactly {193, 2521, 66529}**; c = 1 failures **exactly the 14 primes 409, 577, 5569, 9601,
  23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281** (9 of them ≤ 10⁶); intersection **empty**.
* `scripts/review_r268_brute.py` (log `logs/review_r268_brute.txt`): pure triple loop over (a, c, d) vs t-form, all n ≡ 1 (4),
  5 ≤ n < 300: 0 existence mismatches; (c, d)-enumeration finds 0 solutions at 193, 2521, 66529 (and agrees with the t-form count
  at the neighbours 197, 2549, 66541: 5, 13, 13).
* `scripts/review_r268_spot.py` (log `logs/review_r268_spot.txt`): 400 random primes p ≡ 1 (4) in (10⁷, 10⁸]: explicit b = 1 and
  c = 1 witnesses found by a third method (factor p + 4d, resp. divisors of p + a) and verified in exact rationals
  4/p = 1/x + 1/y + 1/z. At each of the 3 b = 1 failures an explicit c = 1 witness, and at each of the 14 c = 1 failures an
  explicit b = 1 witness, verified exactly (e.g. 66529: (a, b, d) = (5, 26, 128) on c = 1; 8813281: (a, c, d) = (1111585, 14, 2)
  on b = 1).
* T1 / 105 controls: both lines fail at every odd square 9, …, 529 and at 105 (confirmed).
* k = 8 analogue (c n + a + 1 = 8acd; n + a + b = 8abd), own code: over **all primes 5 ≤ p < 8000**: b = 1 fails at 60, both
  fail at 34 incl. 131 and 241 — **matches** (the count is 61 / 35 if p = 3 is included; see defect m1).
