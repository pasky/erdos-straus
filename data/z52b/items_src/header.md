# z52b lane `fingerprint` — data fingerprinting of Erdős–Straus-derived sequences

ES is OPEN. Nothing here proves or disproves it. This lane is breadth-first: items were filtered only for obvious
nonsense; no barrier-checklist evaluation was done.

{{SUMMARY}}

## Method
* Computed (scripts `scripts/z52b_fingerprint_*`, raw data `data/z52b/raw/`, large word table git-ignored):
  - exact solution counts for 4/n = 1/x+1/y+1/z (x ≤ y ≤ z) for **all n ≤ 30 000** and **all primes ≤ 2·10⁵**:
    U (unordered), D (distinct), O (ordered), min max-denominator, largest/smallest x, number of distinct x,
    k₁/k₂ = number of solutions with exactly one/two denominators divisible by n, least common denominator
    (`z52b_fingerprint_count.c`);
  - the same for m/n with **m = 5..48 at all primes ≤ 10⁵** and m = 5..13 at all n ≤ 4000;
  - a word sieve n = tuv − u − v for **all n ≤ 3·10⁶**: all words W, I3 (t,u,v ≥ 3), the (★) count R (t ∈ 4ℤ), the
    U-certificate count Uv, and "some coordinate in 4ℤ ∪ (8ℤ − n)" ESC (`z52b_fingerprint_words.c`); reproduces the
    campaign's 114 I3 zeros (max 2 433 600), the 12 R-zeros ≤ 3·10⁶ and the six U failures ≤ 10⁶;
  - ~50 classical invariants at the ≈ 9 000 primes p ≡ 1 (4), 100 < p < 2·10⁵ (class numbers h(−4p), h(−8p), h(−3p),
    h(p), regulator, L(1,χ_p), L(1,χ_{−4p}), CF period of √p, least QNR, least primitive root, ord_p 2, Legendre
    symbols, a_p of 11a1/37a1/32a1, Ramanujan τ, divisor functions of p±k, smoothness of p−1) via cypari2, with
    Spearman correlations against residuals of log(count+1) after regressing on log p, log log p
    (`z52b_fingerprint_classical.py`, output `data/z52b/classical_corr.{json,txt}`), and truncated-Euler-product fits
    (`z52b_fingerprint_lfit.py`, `data/z52b/lfit.json`);
  - ≈ 260 OEIS lookups of the sequences and transforms (records, positions, parities, differences, zero sets), cached in
    `data/z52b/oeis_cache.json`, results `data/z52b/oeis_hits{,2}.json` (OEIS "no match" is itself recorded).
* Items = every match, every suggestive correlation, every suggestive non-match, plus "compute X and check Y" items that
  were not run. Confidence = confidence that the item is not nonsense, not that it helps.

## Coverage notes / what I did NOT get to
{{COVERAGE}}

Item count: {{COUNT}}. Tag histogram (top 45): {{TAGS}}
