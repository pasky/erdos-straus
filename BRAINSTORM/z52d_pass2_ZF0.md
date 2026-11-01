# z52d Pass 2 — batch ZF0 (finisher: residual needs-compute + Pass-1 stubs), 61 items

- Counts: nothing 57, covered 2 (Z2078, Z2320), interesting 2 (Z2834, Z2797), needs-compute 0, skipped 0. Lint: 0 flagged.
- Interesting: **Z2834**, S_{3861,4}: Br(S)/Br(Q) = (Z/2)², and neither class obstructs a positive-integral adelic point, so the empty fibre is a positivity/finite-region effect rather than a Brauer–Manin obstruction. **Z2797**, BALANCED_LATTICE: norm-aware transference improves the CONDITIONAL cap exponents 13/2 → 6 and 9/2 → 4. Both still need an independent review.
- Heavy compute redone at scale: Z0759 R(2^k−1) exact for k ≤ 61, Z0932 A400619 reproduced through 1.2·10¹¹, Z1790 C-form census 10¹⁰–5·10¹⁰ with a 3–5× sieve, Z0779 segmented word sieve to 5·10⁹ plus a window at 10¹⁰, Z0687 L(1,χ)-ranked U calibration.
- 28 sub-worker `interesting` labels were relabelled `nothing` by the coordinator when their own summaries reported a clean negative or an expected answer; the reason is written into each record's `not_done`, and the list is in scripts/z52d_p2_ZF0_merge.py.
- Detailed per-item memos: BRAINSTORM/z52d_pass2_ZF0_part{1..7}.md (sub-shards); part 0 (coordinator: Z0687, Z0759, Z0779, Z0932, Z1790) is recorded below.

Sub-shards (deep-mode subagents, all finished): part1 Z0307 Z0873 Z2780 Z2875 Z1901 Z0984; part2 Z3167 Z1597 Z3019 Z1721
Z0916 Z2819; part3 Z0016 Z0076 Z0272 Z0524 Z3063 Z2708 Z2860 Z2834 Z2814; part4 Z2806 Z2825 Z2836 Z2843 Z2845 Z2851 Z2867
Z2881 Z2266; part5 Z2078 Z2082 Z2303 Z2320 Z2389 Z2399 Z2403 Z2408 Z2412; part6 Z2431 Z2561 Z2620 Z2901 Z3135 Z2797 Z1340
Z2727 Z2743; part7 Z1227 Z1391 Z1434 Z1518 Z1776 Z1878 Z1890 Z2539. Merge: `python3 scripts/z52d_p2_ZF0_merge.py`.

## Interesting items

### Z2834 — S_{3861,4}(ℕ) = ∅ is not a Brauer–Manin obstruction
The full derivation is in part3.md §Z2834. In short: S: 4xyz − n(xy+yz+zx) = 4 with n = 3861; Δ = n³+16 = 31·167·857·12973.
- Pic(S̄) = ℤ with sign action of Q(√Δ), so Br₁/Br(Q) = ℤ/2 via B = (Δ, d).
- A residue/purity computation adds A = (−q, −d), giving Br(S)/Br(Q) = (ℤ/2)².
- Explicit local integral points (invariants (½,0) at ∞, (½,½) at 2, (0,½) at 31, 0 elsewhere) give a positive-integral adelic point orthogonal to both classes.
- The complete positive search is empty (scripts/z52_bank_pencil.c).
- Status: the Brauer-group derivation is PROVED-as-written but not independently reviewed. Next: a deep review of the transcendental part (A); then test whether the "expected number of positive points" heuristic for the bounded region x ∈ [966, 2896] makes the empty fibre unsurprising.
- Reproduce: `uv run --with sympy python scripts/z52d_p2_ZF0_Z2834_local.py`.

### Z2797 — better transference constants for BALANCED_LATTICE
The full argument is in part6.md §Z2797.
- Banaszczyk's ℓ∞/ℓ¹ Gaussian transference (cube vs. cross-polytope) gives L_min = O(k√log k)/Δ, instead of the k^{3/2}/Δ that Prop 1.3 gets from the Euclidean route.
- Consequences: Thm 4.1 (GRH+EQ) e*(p) ≤ (log₂p)^{6+o(1)} instead of 13/2; Thm 4.2 (GRH+S) (log₂p)^{4+o(1)} instead of 9/2. Both remain CONDITIONAL.
- The finite caps from exact dual minima improve 4385 → 3710 (q = 237971) and 1205 → 775 (q = 423883).
- Next: review; then update BALANCED_LATTICE.md if it is confirmed.

## Coordinator items (part 0) — reproduction
- **Z0759** (nothing): `gcc -O2 scripts/z52d_p2_ZF0_Z0759_Rmersenne.c -lm -o rm; ./rm 2 61`.
  - R(2^k−1) = 0 exactly for k ∈ {2,3,4,5,7,8,13}, and R > 0 for 14 ≤ k ≤ 61 (CERTIFIED).
  - PROVED: u or v ∈ {1,2} ∪ {2^i+1 : i ≡ k mod 2} is impossible for Mersenne n.
  - Controls (n + 840j) get 23 % of R from that set; Mersenne R averages 0.70 × the control mean.
- **Z0932** (nothing): `scripts/z52d_p2_ZF0_Z0932_minx.c`.
  - Scanned all primes < 1.2·10¹¹; the records match A400619/A400620 through (119945383009, 111).
  - U(8803369) = 140 is the 2nd lowest of 41 primes in the same class mod 840.
- **Z0687** (nothing): L(1,χ_p) ranking of the 6587 primes ≡ 1 mod 360360 below 10¹⁰.
  - U on 17 class members: Spearman(L, U/log³p) = −0.77.
  - lcm(1..19)+1 is typical for its L.
- **Z1790** (nothing): there is no CUDA GPU on this machine.
  - The exponent-2 sieve for C ≤ 3 gives identical output to the trial-division census, 3–5× faster.
  - The census was extended to 5·10¹⁰: all primes have a C-form certificate; max Cmin = 3632 at 35848375369.
- **Z0779** (nothing): segmented word sieve (`scripts/z52d_p2_ZF0_Z0779_segwords.c`).
  - Exact against the reference counter; complete to 5·10⁹ plus the window [10¹⁰, 1.05·10¹⁰).
  - No new zeros. min R per dyadic bin rises 2 → 12.
