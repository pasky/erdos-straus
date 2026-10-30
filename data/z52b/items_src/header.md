# z52b lane `fingerprint` — data fingerprinting of Erdős–Straus-derived sequences

ES is OPEN. Nothing here proves or disproves it. This lane is breadth-first: items were filtered only for obvious
nonsense; no barrier-checklist evaluation was done.

## Summary (read this first)

**{{COUNT}} items** (target ≥ 300), every one with a concrete first step; ~60% are backed by a computation run in
this lane (numbers quoted are from `data/z52b/*.json`), the rest are "compute X and check Y" items. Labels: everything
here is EVIDENCE/data unless a proof is given in the item (two short proofs: the isosceles law, and a partial proof
of the p | z normal form). ES remains OPEN.

**Ten items I find most exciting**
1. `fingerprint-0193` — **Normal form:** in every solution x ≤ y ≤ z of 4/p, p | z (all 21 909 solutions for p < 2500
   checked directly; share-sum check at all primes ≤ 10⁵; two of three cases proved). Explains minz(p) ≡ 0 (mod p).
2. `fingerprint-0235` (+0194, 0273) — **Isosceles law, proved:** a solution with two equal denominators exists ⟺ p ≢ 1 (mod 4)
   (via (4x−2p)(4z−p) = 2p²); for general n ⟺ n has a prime factor ≢ 1 (mod 4) (verified for all n ≤ 3000). Corollaries:
   D(p) = U(p) on the hard class, U − D = 2 and O = 6U − 6 at every p ≡ 3 (4). A fully understood 'degenerate-locus' obstruction
   on exactly the hard class — a toy model of T1.
3. `fingerprint-0195` — **lcm-closed sub-ES** (solutions with x | z, equivalently y | z) fails at **only one** prime ≤ 10⁵:
   2521 = lcm(1..10)+1, the hardest ES prime. Siblings: no-3 sub-ES fails only at 3, 241; all-squarefree only at 71, 191, 21169.
4. `fingerprint-0016`, `0227`, `0094` — **Count law:** residual log U(p) ≈ −0.30·log L(1,χ_p) (truncated at q ≈ 30) explains
   ≈ 49% of the fluctuation at ≈ 9 000 primes and holds out of sample at 10⁶ and 10⁷; F_q-point counts of the ES surface are
   p-independent, so this is **not** a singular-series effect but a Hilbert-symbol/Brauer effect — and indeed the campaign's
   BM main term M_BM predicts U(p) (residual ρ = +0.65) far better than its own (★) count R(p) (+0.10).
5. `fingerprint-0156/0157` — per-prime weights: q ≡ 2 (3) give a clean Euler factor q·β_q ≈ −0.35; q ≡ 1 (3) are cancelled
   by the shift-3 coupling p ≡ −3 (q) ⇒ (p/q) = (−3/q) (explains the '(7/p) anomaly').
6. `fingerprint-0248`, `0277` — Mordell's six square classes mod 840 are exactly the six hardest classes by count, ordered
   1 ≻ 121 ≻ 361 ≻ 169 ≻ 529 ≻ 289; n mod 840 explains 64% of the variance of log U(n); the classes = primes x² + 840y²
   (840 idoneal, A139665) — suggests an 'idoneal covering' framing.
7. `fingerprint-0182` — **Pairwise union:** (★) ∪ U, (★) ∪ I3 and U ∪ I3 each certify every non-square n ≡ 1 (4) ≤ 3·10⁶
   except 105.
8. `fingerprint-0183` — **Bounded U-certificates:** the least admissible v is ≤ 116 at every prime p ≡ 1 (4) ≤ 3·10⁶
   (records 87 at 2521, 116 at 3361, none after); compare A400619's bounded greedy shift (≤ 111 beyond 1.2·10¹¹).
9. `fingerprint-0134` (+0133) — R-zeros have small h(−4p) (12 of 14 below median, p ≈ 0.006) and large L(1,χ_p): the
   (★) line's failures sit on both twists' tails (Siegel-dichotomy relevance).
10. `fingerprint-0057`, `0055`, `0073` — divisibility-strengthened ES ladder (k | x,y,z ⟺ Schinzel 4k/p): last failures ≤ 10⁵
    241, 12 241, 83 449 (= an R-zero), … ; fail(8) ∩ fail(12) = {2, 3} ⇒ union conjecture 'every p > 3 has an all-even or
    all-3-divisible solution'.

Also notable: OEIS A400619 and A392469 (2026 entries) reproduced independently (the latter only on p ≡ 1 (24) — a possible
clarification); the predicted extreme prime lcm(1..19)+1 = 232 792 561 is hard (U = 276, below all 113 sampled primes at 10⁷
in U/log³p) but not record-hard, and there Type II beats Type I (k₁ = 47 < k₂ = 82); **negative:** no general Type I/II
complementarity (residual corr +0.70); higher-power (cubic/quartic/octic) residue characters, Rédei ranks, Gaussian angle,
non-CM a_p, Ramanujan τ, Tunnell's congruent-number combination are all null.

**Caveats.** (i) Early analyses read an incomplete prime file for (8·10⁴, 2·10⁵); every script was re-run on the complete
data and the quoted numbers re-checked (changes were ≤ 0.01 in correlations; one record list was corrected). (ii) Several
items normalise by log²p; ET's prime average is ≍ log³p (our data agree), so log² ratios are only comparable within a range.
(iii) Correlations are Spearman on residuals of log(count+1) after log p, log log p; p-values are not multiple-testing
corrected (most effects are ≥ 10σ, the small ones are labelled null).


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
* Done: everything listed under Method; 32 restricted-ES shapes at primes ≤ 10⁵; numerators 5–48; BM main term at
  p ≤ 30 000; pseudosquare / least-QNR record primes; lcm(1..19)+1; windows at 10⁶, 10⁷; OEIS text search for ES entries
  (20 found, 8 used); hard-prime arithmetic profiles.
* Not done (left as compute-and-check items): LMFDB conductor/rank comparisons, ternary-form scan (beyond Tunnell),
  Hurwitz-number fits, function-field analogues, ES₅/λ(p) five-slice counts, Ramanujan-sum expansion, per-q weights for
  other numerators, quasi-identity mining, segmented sieve beyond 3·10⁶, partitions/Kloosterman/Wilson null tests,
  A396825 b-file comparison, residual (not raw) propagation along p ↦ (p+3)/4.
* No item was evaluated against the barrier checklist (per brief). `seen:` tags only where I happened to know
  (A139665's Mordell link is in OEIS itself).

Item count: {{COUNT}}. Tag histogram (top 45): {{TAGS}}
