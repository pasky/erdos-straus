# bsG_short_block — consecutive integers n + 2, n + 3, …: the least outer letter x*(n) (O180)

## Idea
(W)(n) ⟺ some x ≥ 2 has a divisor d ≡ −1 (mod x) of n + x with 2x − 1 ≤ d ≤ (n+x)/2. The brief asks whether a block of consecutive integers
can avoid this deterministically. Measure the first hit x*(n) := min outer letter.

## Results (LORENZINI_W §5)
* EVIDENCE: **x*(n) ≤ 12 for every n < 10⁸ outside E_W.** The records are 17:3, 51:4, 126:6, 1379:12. At [10⁷, 10⁸) the counts with x* > X
  for X = 2…10 are 5 096 879, 198 815, 17 577, 1 405, 169, 17, 8, 3, 1.
* Heuristic exponent: m has no divisor ≡ −1 (mod x) with density (log m)^{−δ_x}, where δ_x = 1 − |H_x|/φ(x) and H_x is a largest subgroup of (Z/x)^× not containing −1.
  For example δ₂ = 1, δ₃ = δ₄ = 1/2, δ₅ = 3/4. This leads to CONJECTURE x*(n) ≪ log n / log log n.
* PROVED negative: for any X, D, all n ≡ −1 (mod lcm(d ≤ D)) have no admissible divisor ≤ D of n + x for any x ≤ X. A block argument must use
  large prime factors.
* PROVED positive (cheap): x* ≤ 3 on every prime p ≡ 1 (4), p ≥ 13 (LORENZINI_W Prop 8.1). The hard inputs are n ≡ 3, 9, 11 (12) with n + 2 prime.

## Literature
Prime k-tuples / Dickson. Consecutive sums of two squares (infinitely many triples; Hooley-type counts). Sieve dimension of "no divisor in a class"
(Wirsing/Delange mean values of multiplicative functions).

## Barrier screen
B1 (fixed moduli fail: sterile set). B6 (averages). A proof that blocks cannot all fail needs a lower bound for simultaneous prime-like events.
That is the parity barrier in the opposite direction: H-B.

## Cheap numerics
`scripts/bsG_xstar.c 10⁸` (1 min), `scripts/bsG_primes.c 10⁸`.

## Assessment
EVIDENCE + CONJECTURE. A sharp, testable law; it suggests (W) is "very true" (12 consecutive integers suffice to 10⁸). No route to a proof.
Promise for (W) 1/5, for ES 0 (ES needs (S), not (W)).
