# z52d Pass 2 — batch TO7 (101 "touched" items, never worked in Pass 1)

**Summary (lint-fix round, 5 lines).**
1. Counts now: nothing 67, covered 3 (Z2813, Z2833, Z2852), interesting 3 (Z2596, Z2614, Z2639), needs-compute 28, skipped 0. Lint (`scripts/z52d_pass2_lint.py`): 0 flagged of 101.
2. Lint round: the 65 flagged items were re-run with real steps (I3 counts to 10⁷ with Poisson and first-moment checks; ES-slot word covering; word/Jacobi identities A·A*≡1 and gcd(4Cp+1,4C′p+1)|(C′−C); level-2 monoid transport; Janson/Borel–Cantelli tails; Halász, GP, entropy, spread, Schreier, Lagrange-convergent and two-term-witness checks). 28 items remain **needs-compute** with a stated estimate; they were not executed in this round.
3. Interesting: Z2596 (quotient sets contain longer geometric progressions than size-matched random sets, e.g. k=59: 23 vs 13), Z2614 (QR-richness suppresses slice successes within residue classes), Z2639 (class means over mod-840 hard classes differ by ~8–10%, not explained by R(p)).
4. Corrections recorded: the naive scaling identity F(m)=Σ P(m/k) for 4/m solutions is false (Z2878); the I3 Poisson model underpredicts exceptions (Z2637); the subgroup dichotomy in Z2713 is refuted; Z2424 θ=7/64 absent from its cited file.
5. Scripts: `scripts/z52d_p2_TO7_*` (new this round: `i3.c`, `i3stat.py`, `words.py`, `monoid*.py`, `cover.py`, `batchB*.py`, `janson.py`, `misc.py`, `lagrange_frac.py`). The I3 count binary (10 MB) is kept in /tmp, not committed.

---


## Setup and checks
- Slice engine (`scripts/z52d_p2_TO7_slices.c`): for prime p≡1 (mod 4), k≡3 (mod 4), k≤T: Type I a=1 succeeds iff some divisor b of (kp+1)/4 has b≡−1 (mod k); Type II a=1 iff some divisor b of (p+k)/4 has b≡−1 (mod k) (CONDITIONAL_ES.md Lemma 1.2 with a=1). Validation against repo facts: max minI = 367 (repo: t ≤ 367, max at p=830041 — the engine's argmax is in the same run); Type II a=1 fails at p=193 and p=2521 (repo: same two primes); 2370 hard primes ≤10⁶.
- Feature file (`scripts/z52d_p2_TO7_feat.c`): per (p,k,type): ω(M), squarefree flag, divisor-hit, −1 ∈ ⟨residues⟩, −1 ∈ subset products, largest prime factor. Consistency: divisor-hit counts reproduce nI exactly.

## Interesting items

### Z2614 — QR-richness vs slice success (Heath-Brown-type correlation)
- Quantity: R(p) = #{ℓ prime, 3≤ℓ≤47 : (ℓ/p)=1}; nI(p) = number of k≤400 (k≡3 mod 4) with a Type I a=1 slice success.
- All primes ≤10⁶: mean nI falls from 9.22 (R<5) to 8.27 (R≥11). Hard primes: 7.58 → 6.18.
- Within each Mordell-hard residue class mod 840 (r=1,169,361,529), low-R (bottom third) minus high-R (top third) mean nI = +0.57, +0.41, +0.59, +0.52 (≈200 primes per cell; ~2σ each).
- Class-adjusted OLS on hard primes p≥10³: slope on R = −0.26 per QR-prime.
- Reproduce: `scripts/z52d_p2_TO7_an1.py`, `an2.py` (within-class), `an4.py` (class-adjusted regression); data `data/z52b/pass2/TO7/slices_1e6_T400.tsv`.
- Caveat: correlation only; mechanism unknown (plausibly the number of small-prime residue classes available to prime factors of (kp+1)/4). Next: check whether the slope is explained by the local density of −p mod ℓ classes; extend to p≤10⁷.

### Z2639 — residue-class averages over Mordell-hard classes mod 840
- Mean nI (p≤10⁶): r=1: 6.21 (n=395); 121: 6.37; 169: 6.71; 289: 6.67; 361: 6.67; 529: 6.87 (n=400). CV of the six class means 3.4%; r=1 vs r=529 differs by 0.66 (SE ≈0.17).
- The difference persists after adjusting for R(p) (class coefficients change by ≤0.02 when R is added; mean R is the same across classes, 8.22–8.36).
- So the Bhargava-style "uniform in r" assumption fails at the ~8–10% level at this range. Next: check whether the gap shrinks with p (10⁵ vs 10⁶ bins) and whether it is governed by a mod 5/7 local density.
- Reproduce: `scripts/z52d_p2_TO7_an1.py` (section Z2639), `an4.py`.

## Other computations (all `nothing`; numbers in `outcome_TO7.jsonl`)
- Z2430/Z2429: exact quotient test −1∈Q vs subgroup test −1∈⟨res⟩ at hard prime slices: the subgroup test overstates by up to ×1.8 (k=19).
- Z2712/Z2713/Z2589 (4Cp+1, C≤30): subset products hit −1 for 75%→3% of primes as C grows; the claimed "avoid ⇒ subgroup" dichotomy is refuted in the data (gen&!sp = 4271 at C=7).
- Z2804: for each fixed a∈{2,…,23}, v2(ord_p a)=v2(p−1) has density ≈1/2 (it is the QNR condition); the union covers 99.92% of p≤10⁶, so fixed-A covering = least-QNR bound.
- Z2887: p=a²+b²: minI=3 for all p≡5 (mod 8) in range; the (a,b) mod 8 split is only the 2-adic class.
- Z2884: signed Thue pairs with |uv| | p+u+v: 0.14% of pairs, 1.77× the naive Σ1/|uv| heuristic.
- Z2560, Z2566, Z2565, Z2443, Z2581, Z2425/2426, Z2905: see outcome file (controls and caveats).

## Lint-round interesting item: Z2596 — longer geometric progressions in quotient sets
- Q_M={a/b mod k: ab|M} for type-II prime slices k∈{31,43,59,67} at hard primes ≤10⁶ (M≤2.5·10⁵).
- Longest distinct geometric progression inside Q_M vs a size-matched random subset of (ℤ/k)^×: k=31: 18.8 vs 15.3; k=59: 23.2 vs 13.3; k=43 (ω≤3): 4.4 vs 2.8; k=67 (ω≤3): 3.9 vs 2.6. Max ω among these slices is 5.
- Reproduce: `scripts/z52d_p2_TO7_batchB2.py Z2596`. Next: check whether the long GPs are cosets of ⟨g⟩ inside Q for k≤199.
