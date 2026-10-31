# z52b pass 1 — batch U08 (207 untried §2 items)

- Outcomes (207): nothing 23, covered 56, interesting 2 (Z0143, Z0809), needs-compute 31, skipped 95. Records: data/z52b/pass1/outcome_U08.jsonl.
- Interesting, Z0143: the one-square sibling 4/n = 1/x+1/y+1/z² splits by p mod 4. All 87 primes p≡3 (4) ≤ 1000 are solvable (first z ≤ 474), but 37 of 80 primes p≡1 (4) ≤ 1000 have no solution with z ≤ 600, and 20 of them none with z ≤ 4000. The solvable p≡1 (4) have z ≤ 26 (median 12). Section §Z0143 below.
- Interesting, Z0809: the log-residual of U(p) against log log p is non-normal (skew −0.89, excess kurtosis 1.48); P(U≤20) is 0.52% observed vs 0.10% normal. Section §Z0809 below.
- Checked and nothing: Z0716 (nx ≈ U/2.05, not log p), Z0290 (prime-type denominator world empty for p ≡ 1 (4), 5 < p ≤ 3000, except p = 5), Z0203 (a ≤ 7 representable at all primes ≤ 1500), Z0333 (Poisson thinning under-predicts failures ~2× from denominator sharing), Z0862 (exception list 71, 191, 21169 confirmed), Z0304 (F_q squares fail only at q = 3), Z2604 (no Sarnak-type correlation, z = 1.0).
- Covered (56): the catalog items (Z0397–Z0429) are in the catalog lane; the statistics items are in the fingerprint and dividing lanes (e.g. Z0833 = fingerprint #162, Z0847 = #178). Z1272 is the existing Z0866 list (13, 37, 97, 181, …), reproduced here.

Scripts: scripts/z52b_p1_U08_{enum,stats,corr,sq1,sq1_scan,sq1_checks,moments,outcomes}.py. Data: data/z52b/pass1/U08/ (< 1 MB).
The f4 data used here: data/z52b/raw/f4_all_30000.txt (column 1 = U(n), validated against the enumerator for 211 primes: 0 mismatches).

## Z0143 — one square denominator: a p mod 4 split (interesting)

**Setup.** Decide whether 4/n = 1/x + 1/y + 1/z² has a positive-integer solution, for n ≤ 1000. For fixed z the rest is a two-term problem a/b = 1/x+1/y with a = 4z²−n, b = nz², solved either by brute force on x (Fraction arithmetic, x in (1/r, 2/r]) or by divisors of b² (the (ax−b)(ay−b)=b² method); the two agree (checked on n = 17, 29, 41, 149, 151, 163, 211, 5, 13, 37, 53).

**Observed (EVIDENCE; reproduce with the commands below).**
* All 87 primes p≡3 (mod 4), p ≤ 1000 (3 included) are solvable; first z: median 12, max 474 (z ≤ 600 search).
* 43 of 80 primes p≡1 (mod 4), p ≤ 1000 are solvable with first z ≤ 26 (median 12); 37 have no solution with z ≤ 600.
* The 20 failing primes checked to z ≤ 4000 (17, 29, 41, 73, 89, 101, 109, 149, 173, 197, 241, 269, 277, 281, 421, 433, 449, 461, 577, 593) have none. Over n ≤ 1000 there are 48 failures in total: 37 primes ≡1 (mod 4), 11 composites, and no prime ≡3 (mod 4).
* No congruence explains the split at this scale: failure rate by p mod 8 is 0.51 (p≡1 mod 8) vs 0.42 (p≡5 mod 8); by p mod 12, 0.36 vs 0.55; by (2/p),(3/p) between 0.32 and 0.57; by (5/p) 0.40 vs 0.56.

**Why this might matter (Assessment).** The same 1 mod 4 vs 3 mod 4 split is the one ES itself lives on (Mordell's hard classes are 1 mod 4), and the z-search finds solutions quickly whenever they exist for p≡1 (4). A clean obstruction for the failing primes would be a provable one-square sibling; a local (Hilbert-symbol) obstruction for the conic-bundle 4xyz² = n(yz²+xz²+xy) at the failing primes is the natural first test. It is not yet known to be a genuine obstruction: z ≤ 4000 is a finite search.

**Next (depth lane).** Test local solvability (Hilbert symbols / Brauer–Manin for the z-fibration) at p = 17, 29, 41; if locally solvable everywhere, test larger z (z ≤ 10^5 with the two-term divisor method).

**Reproduce.**
```
uv run --with sympy python scripts/z52b_p1_U08_sq1_scan.py      # n ≤ 1000, z ≤ 600 (brute force)
uv run --with sympy python scripts/z52b_p1_U08_sq1.py           # n ≤ 300 failures, z ≤ 3000
uv run --with sympy python scripts/z52b_p1_U08_sq1_checks.py    # z ≤ 4000 for 20 failures; first-z split; residue rates
```
Outputs: data/z52b/pass1/U08/z0143_{scan,unsolved_ext,checks}.json.

## Z0809 — U(p) is not lognormal in the lower tail (interesting)

**Setup.** U(p) = #solutions of 4/p, primes p ≡ 1 (mod 4), 1000 < p ≤ 30000 (n = 1531), from data/z52b/raw/f4_all_30000.txt. Residual r = log U − (a + b log log p).

**Observed (EVIDENCE).** Slope b = 2.83 on log log p; residual sd 0.327; skew −0.89; excess kurtosis 1.48. Lower tail: P(U≤5) = 0 observed and 0 normal-predicted; P(U≤10) = 0.065% observed vs 0.0% normal; P(U≤20) = 0.52% observed vs 0.10% normal. Minimum U = 9 at p = 2521.

**Caveat.** The residual is against log log p only (no character features), so the skew may partly be the known character structure of U (fingerprint lane). The next step removes that fit first.

**Assessment.** A heavy lower tail on the log scale is the feature that makes 'finitely many exceptions' heuristics fragile (Z0883 shows window minima are otherwise consistent with a crude Gumbel scale to within 0.2 in log).

**Reproduce.** `uv run --with numpy --with sympy python scripts/z52b_p1_U08_stats.py` → data/z52b/pass1/U08/stats.json.
