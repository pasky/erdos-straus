# z23 — fixed line k = forms of disc −16k²p; k | 6 is the genus regime (O251)

## Idea
On a vertical line M = 2k the Vieta partner g ↔ D = (4k²p + Y²)/g plus Y ↦ Y + tg is Gauss reduction of [g, 2Y, D]
(disc −16k²p, order of conductor 2k). Claude admissibility of the partner needs Y² ≡ 1 (mod 4k): automatic iff
(ℤ/4k)^* has exponent 2 iff k | 6. Then the "descent" is a genus-preserving walk and ES on the line is: some reduced
form [g, 2, D] with g ≡ −1 (4k) — i.e. 4k²p + 1 has a divisor ≡ −1 (mod 4k).
## Literature
Cox §2–3 (reduction, genus theory); WINDMILL_REDUCTION Prop 10.3 (t | 24 exception); Landau: integers with all prime
factors ≡ 1 (4) have density ≍ (log x)^{−1/2}.
## Barrier screen
k | 6: B1 (fixed finite set of congruence/genus conditions: k = 1 fails iff 4p + 1 has no prime factor ≡ 3 (4)).
k ∤ 6: admissibility is a ray-class (mod 4k) condition = the B2 datum. T1: no ES form at squares (Prop 1.1 Cor 1.2).
## Cheap numerics
`scripts/z23_descent.py 20000 1000`: from the least-root window shot every starting form is already reduced (1565/1565),
so the deterministic descent is the identity; `scripts/z23_cayley.py`: line k = 1 has no ES class for 55/211 primes ≤ 3000.
## Assessment
PROVED (structure) + EVIDENCE. Negative: reduction keeps the class, the class is irrelevant (Cor 1.5).
