# z52b pass 1 — batch H04 (25 items, Z1456 … Z1653)

**Summary.** nothing 15 · covered 9 · needs-compute 1 (Z1546 Lean) · interesting 0 · skipped 0.
No item was promoted to a depth lane. Outcomes: `data/z52b/pass1/outcome_H04.jsonl`; scripts `scripts/z52b_p1_H04_*`;
data `data/z52b/pass1/H04/`. ES is OPEN; nothing here proves any case of it.
Most useful by-products (all small): Type I square-d slices are empty at p ≡ 1 (4) (Z1482, kills the premises of Z1482/Z1550);
the per-level failure model needs the product constraint (Z1533); 76 % of (★) level failures are subgroup obstructions (Z1595).

## By-products worth remembering (none rises to `interesting`)

* **Z1482 — Type I with square d is empty (PROVED, one line).** For a prime p ≡ 1 (mod 4) and d = s², every divisor of
  p² + 4c²d = p² + (2cs)² is ≡ 1 (mod 4) (gcd(p, 2cs) ∈ {1, p} and p ≡ 1 (4)), while the Type I condition needs
  f ≡ −p ≡ 3 (mod 4). So a Type I certificate needs a prime q ≡ 3 (4) with (d/q) = −1. Brute force: 0 hits in 24 687
  (p < 3000, c < 40, d ∈ {1, 4, 9}) tests, versus 202 of 211 primes hit with d ∈ {2, 3, 5, 6, 7}
  (`scripts/z52b_p1_H04_typeI_dsq.py`). This also voids Z1550's proposed first step (p + 2ci in ℤ[i]).
* **Z1533 — per-level failure model.** For C ≤ 30 and the 108 397 primes p ≡ 1 (4) in [10⁸, 1.04·10⁸], the empirical
  P(no d | 4Cp+1, d ≡ −1 mod 4C) is 0.206 (C = 1), 0.426 (C = 2), …, 0.938 (C = 30). Two models use the true factorisation
  shapes: with i.i.d. uniform classes the model is far too optimistic (0.157, 0.271, …, 0.829). With classes conditioned on
  product ≡ 1 it matches within ±0.03 for C ≥ 2. Using integers n instead of primes gives more failures (0.286 at C = 1).
  Reproduce: `gcc -O2 scripts/z52b_p1_H04_pdmodel.c -o pd && ./pd 100000000 4000000 30`
  (`data/z52b/pass1/H04/pdmodel.txt`).
* **Z1595 — anatomy of (★) level failures.** At 200 Mordell-hard primes just above 10⁶, with C ≤ 100, there are 18 834
  failures. In 76 % of them −1 ∉ ⟨classes of the prime factors of 4Cp+1⟩, and in 24 % −1 lies in that subgroup but not in
  the divisor set. The Kneser stabiliser is trivial in 84 % (`scripts/z52b_p1_H04_kneser.py`).
* **Z1526 — the integer C-form statement is false.** Exact R(n) for n ≤ 2·10⁷ (`scripts/z52b_p1_H04_rstar.c`, 2 s) gives
  860 odd non-squares with R = 0 (836 of them composite). Curiosity, n ≡ 3 (4) so ES-trivial: the prime zeros
  ≡ 3 (mod 4) include the Mersenne primes 3, 7, 31, 127, 8191.
* **Z1488.** There is no square-class or quartic family obstruction for (★): over 86 families k·m², k·m⁴ (k ≤ 200) we see 7
  zeros against 5.7 expected. The 14 (★) prime failures ≤ 2·10⁷ have (2/p)₄ = +1 in 9 of 14 cases.
* **Z1583.** Primitive Pythagorean pairs miss 3/4 of the (u, v) classes mod 840 for 2-adic reasons. Unit multiples
  k(u, v, w) hit all of them, so T1 points occur in every (u, v)-congruence region. A degree count (sketch) reduces ET
  Type II identities polynomial in (u, v) to congruences on n = u² + v².
* **Z1650.** Across the 273 Mordell-hard primes ≤ 10⁵, the parities of f, f_I and f_II behave like coin flips. No hard
  prime has a solution with y = z or x = y.
