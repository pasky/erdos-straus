# z52b pass 1 — batch U08 (207 untried §2 items), redo pass per pass1_U_fix.md

- Outcomes (207, one line each): nothing 102, covered 65, interesting 4 (Z0143, Z0809, Z1778, Z2989), needs-compute 15, skipped 21. Records: data/z52b/pass1/outcome_U08.jsonl.
- Skipped (21) are restatements or meta items, except Z1144 and Z1295, which are under-specified (no residue graph / no chart named in the item); flagged for the author.
- Needs-compute (15) are each >30 min compute or >1 h coding (Walnut, Lean, prover runs, SAT, QUBO, LP, S-unit, PD-model, fan graph, involution graph, F_3[T] exceptions), with a spelled-out test.
- Lookups were done by web search (arXiv API rate-limited): ES = Erdős Problem #242 (OPEN); Koenigsmann "Defining ℤ in ℚ" (Annals); Bel'tyukov–Lipshitz decidability of the existential theory of (ℕ,+,|); Campos et al. diagonal Ramsey (2023); Keevash designs; Chatterjee nonlinear LD; Katz–Sarnak; EKL; Kleban–Özlük and Knauf spin chains.

## Z1778 / Z2545 / Z1213 / Z3058 — small good divisors (interesting)

**Setup.** For primes p ≡ 1 (mod 4) with p ∈ [10^6, 10^7] and [10^8, 10^9] (60 random primes each) and C ≤ 50, N = 4Cp+1 is fully factored and the good divisors (d | N, d > 1, d ≡ −1 mod 4C) are listed.

**Observed (EVIDENCE).**
* Every sampled prime (60/60 in both decades) has a good divisor composed only of primes ≤ 10^3 (C ≤ 50); same with primes ≤ 10^4.
* The minimal good divisor scales like a power of N: median log10 d_min / log10 N = 0.294 (first decade) and 0.265 (second). So d_min ≈ N^0.27–0.29 ≈ p^0.28.
* Fraction of successes with d_min ≤ 10^4: 0.94 and 0.76.
* Factor-smoothness (Z1213): 80% and 75% of the prime factors q of these N have q − 1 1000-smooth.
* Timing (Z3058): the C ≤ 50 linear scan with full factorisation takes 0.3–0.6 ms per prime near 10^12, 10^14, 10^16 (average C tried 2.1, 1.3, 1.2).

**Why it matters (Assessment).** The data suggest a trial-division-type search with a fixed bound finds solutions at p ~ 10^9, but the minimal divisor exponent ≈ 0.28 means the required factor size grows polynomially in p. At p ~ 10^100 that is ~10^28, beyond ECM. So the factoring-free question (Z2545) has a clear quantitative answer at small p and a scaling question at large p.

**Next.** Measure the minimal-divisor exponent at p ~ 10^12–10^15 (full factorisation feasible) and check whether it stays near 0.28.

**Reproduce.** `uv run --with numpy --with sympy --with scipy --with scikit-learn python scripts/z52b_p1_U08_redo.py smallf` → data/z52b/pass1/U08/redo_smallf.json.

## Z2989 — prime factors of (p+e)/4 avoid squares mod e (interesting, weak)

**Setup.** e prime ≡ 3 (mod 4), 5 ≤ e ≤ 199; p ≤ 2·10^4 with p ≡ −e (mod 4); N_e = (p+e)/4; for each distinct prime factor q ≠ e of N_e, record whether q is a QR mod e.

**Observed (EVIDENCE).** 48.4% QR over 65211 factors (−8σ against an i.i.d. null). Restricted to q > 100: 47.2% over 12291 factors (−6.2σ).

**Caveat.** Windows for the same p overlap across the various e, so the effective sample is smaller and the σ values are optimistic. The bias is also weak (2–3 percentage points).

**Next.** One e per p (random), and a control in which q runs over prime factors of random integers in the same range.

**Reproduce.** `uv run --with sympy --with numpy python scripts/z52b_p1_U08_final.py` → data/z52b/pass1/U08/final.json.

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
