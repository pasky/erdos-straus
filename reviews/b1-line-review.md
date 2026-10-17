# R270 — hostile review of O259 (B1_LINE.md, the b = 1 line)

Reviewer: side-agent/review-b1-line. Scope: B1_LINE.md, BRAINSTORM/z29_*.md, scripts/z29_*, logs/z29_*, sources/lit2026f López
excerpts, AGENT_REPORT_O259. All numerical checks below use FROM-SCRATCH code `scripts/review_r270_*` (author scripts not reused).

## Summary verdicts
(filled in as the review proceeds)

## Claim-by-claim

### C1. Lemma 1.1 (mutual-shift form) — SOUND
Re-derived. b = 1 ⟺ a(4cd − 1) = cn + 1. With w = 4cd − 1: 4d(cn + 1) ≡ n + 4d (mod w), gcd(4d, w) = 1, so w | cn + 1 ⟺
w | n + 4d; put g = (n + 4d)/w. Then n + g + 4d = g(w + 1) = 4cd·g, i.e. (g·4d)·c = n + g + 4d: st | n + s + t with
{s, t} = {g, 4d} and quotient c. Converse: n odd ⇒ not both even (else n + s + t odd, st even), so exactly one is ≡ 0 (4)
and it is D = 4d; w := (n + s + t)/g − 1 = (n + D)/g ∈ ℤ, and w | n + D ⇒ w | cn + 1 gives a ∈ ℤ. Odd coordinate
T ≡ −n ≡ 3 (4) (from S | n + T, 4 | S). Coprimality for n = p prime: a common prime divides n, so it is p and s, t ≥ p,
then st ≥ p·max(s,t) > p + s + t (p ≥ 5) — correct (the "s, t < p" wording in the proof is just a paraphrase).
Completeness bound: st ≤ n + s + t ⟺ (s − 1)(t − 1) ≤ n + 1 ⇒ min(s, t) ≤ 1 + √(n + 1). ✓. And st | n + s + t ⟺
(t | n + s and s | (n + s)/t + 1). ✓. Consequences used by the census: s ≡ 1, 2 (4) never occur as a coordinate; s = 1
never occurs either (needs 4 | t | p + 1 ≡ 2 (4)). My engine does NOT use any of these mod-4 consequences (it tests
4 | st and st | p + s + t literally), so agreement below is also a check of them.

### C2. Census, b = 1 line (§2.1) — SOUND (≤ 10¹⁰ independently reproduced; 10¹¹ see below)
Engine `scripts/review_r270_engine.c` (different algorithm from z29_census.c: no factor tables at all).
Phase A: sieve the segment by all residue classes p ≡ −(s + t) (mod st) over the 196 918 useful pairs with st ≤ 3·10⁵,
4 | st. Phase B (only for primes not hit in A): exhaustive over s ≤ 1 + √(p + 1); for each s enumerate the two
arithmetic progressions t ≡ −p (mod s), t ≤ √(p + s) and u ≡ −1 (mod s), u ≤ √(p + s) (t = (p + s)/u), testing
4 | st, st | p + s + t literally. (Complete: any divisor t of p + s has t or (p + s)/t ≤ √(p + s); st | p + s + t forces
t ≡ −p and u ≡ −1 (mod s).)
Results (`logs/review_r270_eng_a.txt`, `_b.txt`): ≤ 5·10⁹: 117 474 981 primes p ≡ 1 (4), failures exactly 193, 2521, 66529;
(5·10⁹, 10¹⁰]: 110 048 294 primes, 0 failures. Sum 227 523 275 = author's figure; ≤ 10⁸ subtotal 2 880 504 = author's;
≤ 10⁶ gives 39 175 + 39 322 (≡ 3 (4)) + 1 = 78 498 = π(10⁶). Runtime 2 × 2.6 min.

## Defects
