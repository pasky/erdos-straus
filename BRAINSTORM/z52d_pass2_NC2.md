# z52d Pass 2 — batch NC2 (81 items): summary

Counts (final verdicts): covered 3, interesting 4, needs-compute 3, nothing 71. Total 81 = batch input.
Interesting: Z1999 (Euler family n^2+n+41 has lower R(p) than residue-matched controls, MW p=7e-4; mechanism: 4p+1=(2n+1)^2+164), Z2624 (I3 small-t census: t<=20 covers 99341/99999 n<=1e5), Z2658 (within-prime QR vs QNR d-invariant sums differ, sign test p=4.8e-4), Z2720 (Klein-sail vertex-count premise fails on the HJ-digit proxy).
Needs-compute (blocked, not run): Z2539 (Lean installed at ~/.elan/bin, not run), Z2552 (no GPU), Z2729 (no Brandt/Sage/Magma).
Process: three rounds. Round 1 (4 workers) and round 2 (4 workers) were rejected as too thin in places; round 3 reran five items (Z1968, Z1999, Z2000, Z2485, Z2658) with explicit definitions. Coordinator downgraded Z1973, Z1978 (reformulations) and Z2535 (benchmark) from interesting to nothing. Round-3 kernel bug (intercept omitted) found and fixed in Z1968. Per-item lines: data/z52b/pass2/outcome_NC2.jsonl (latest round wins).
Caveat: many `nothing` verdicts are proxy tests of ill-posed items (e.g. Z1972, Z2143, Z2541, Z2554, Z2600); see each record's not_done.

---

## Z1999 — Euler family n^2+n+41 vs residue-matched controls (round 3)
- Exact R(p) = # ordered divisor pairs of 4p+1 with both factors = 3 mod 4.
- Family: 2067 primes n^2+n+41 =1 mod 4, n<10^4 (max p ~ 10^8); controls: 2067 primes =1 mod 4 stratified on p mod 840.
- Family mean R 7.38, median 4; controls mean 8.73, median 6; Mann-Whitney p = 7.2e-4.
- Mechanism (Assessment): 4p+1 = (2n+1)^2 + 164, so each prime divisor q of 4p+1 satisfies (-41/q)=1 (split in Q(sqrt -41)); this biases the divisor-residue statistic R counts.
- Reproduce: uv run --with numpy --with sympy --with scipy python scripts/z52d_p2_NC2_Z1999_r3.py; data data/z52b/pass2/NC2/Z1999/metrics.json.
- Not done: multi-seed controls; comparison with n^2+n+17 / n^2+n+11.

# NC2 Pass 2 round-2 worker W3 — noteworthy finite result

## Z2624: small-t I3 frequency census

For the fixed event `E_t(n) := exists u,v >= 3: n=tuv-u-v`, exact enumeration for `2 <= n <= 100000` and `3 <= t <= 20` finds 1,432,634 ordered `(t,u,v)` representations. The union of represented n is 99,341 of 99,999 integers (99.342%); 658 have no witness with t≤20. Per-t representation counts are in `data/z52b/pass2/NC2/Z2624/i3_counts.txt`. This is a bounded calibration of the proposed small-group event, not evidence about the full n≤10^9 goal or a proof.

Reproduce with `ulimit -v 8000000; timeout 60s uv run python scripts/z52d_p2_NC2_Z2624_r2.py`; the script enumerates the exact formula `n=(tu-1)v-u` and reports per-t counts, distinct coverage, and uncovered count. The search bounds u using `n >= (3t-1)u-3` and v using `n<=100000`.

# z52d Pass-2 round 2 — NC2 part 4

## Z2720 — Klein sail vertex-count premise fails on the HJ proxy

Fixed the item’s cone convention through the repo’s HJ expansion `p/A = [[b₁,…,bᵣ]]`; used “geometric HJ vertices” in the stated digit sense (digits ≥3) as the computable proxy, explicitly not a convex-hull sail. On all 4,960 QNR pairs `(A,p)` with prime `p ≡ 1 (mod 4)`, `p ≤ 499`, the HJ length-three count was 428, while the digit-≥3 count is different; for example `13/5 = [[3,3,2]]` has length 3 but only two digits ≥3, and `13/2 = [[7,2]]` has length 2 but one such digit. This falsifies equality between length and the item’s proposed count under this proxy, but does not settle the cone orientation / sail correspondence.

Reproduce: `ulimit -v 8000000; timeout 300s uv run --with numpy --with sympy python scripts/z52d_p2_NC2_r2_metrics.py`; see `data/z52b/pass2/NC2/Z2720/metrics.json`.

## Z2658 — within-prime QR vs QNR d-invariant sums (round 3)
- S(p,A) = sum_i d(L(p,A),i) (Ozsvath-Szabo recursion, closed form at q=1), length-3 A, primes 5<=p<2000.
- Normalised S/p^2, within each prime: QR mean 0.00862, QNR mean 0.00561; QR larger for 87 of 133 primes; sign test p=4.8e-4.
- Reproduce: uv run --with numpy --with scipy python scripts/z52d_p2_NC2_Z2658_r3_norm.py; data data/z52b/pass2/NC2/Z2658/norm.json.
- Next: check whether S(p,A) is affine in the Dedekind sum s(A,p) (then covered by DEDEKIND_ES.md); if not, new.
