# UNIT A15 report

- Added §43, “General numerators: the multiplier identity is m-uniform and the exceptional-set machinery transfers.”
- Lemma 43.1 (proved): the multiplier identity holds for every integer numerator `m >= 3`.
- Lemma 43.2 (proved): exact multiplier-thinning factors are `eta_1(m)=prod p/(p+1)` and `eta_2(m)=prod p^2/(p^2+p-1)`.
- Lemma 43.3 (proved): the §16 class mass transfers with the explicit factor `eta_1(m)/phi(m)`.
- Theorem 43.4: complete internal Layer-1 proof, externally CLAIMED/PROVISIONAL; saving coefficient `(eta_1(m)/phi(m))^(1/3)`.
- Layer-1 uniformity: primes for `m <= (log N)^(2-epsilon)`, all denominators for `m <= (log N)^(1-epsilon)` via the divisor/semigroup transfer.
- Lemma 43.5 (proved): c-free coupling, deduplication, distinct large-prime coordinates, and CRT density are unchanged.
- Lemma 43.6 gives the general-m §39 mass profile and the exact `eta_2(m)/phi(m)` atom mass.
- Provisional Theorem 43.7 threads `muv` through the pruned cubic prime slice; it inherits Theorem 34.8.
- Theorem 43.8 is CLAIMED/PROVISIONAL: `E_m(N) << N exp(-c eta_1(m)(log N)^(3/4)/phi(m))`.
- Layer 2 is stated uniformly and nontrivially for `m <= (log N)^(3/4-epsilon)`.
- Failure log 43.9 declines an unaudited m-dependent Bonferroni retuning and any short per-residue equidistribution claim.
- PW Theorem 1.3 is transcribed as (43.32); the exact crossover is (43.34), reducing to `phi(m) <= (log N)^(1/8)` when fixed local factors are suppressed.
- Added `verify.py (ap)`: 364 exact identity checks, an `m=5` atom census, and informational local-factor numerics.
- Full `uv run --with sympy,numpy,scipy python verify.py` passes; AST, whitespace, and control-byte checks pass.
