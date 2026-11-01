# NC2 Pass 2 round-2 worker W3 — noteworthy finite result

## Z2624: small-t I3 frequency census

For the fixed event `E_t(n) := exists u,v >= 3: n=tuv-u-v`, exact enumeration for `2 <= n <= 100000` and `3 <= t <= 20` finds 1,432,634 ordered `(t,u,v)` representations. The union of represented n is 99,341 of 99,999 integers (99.342%); 658 have no witness with t≤20. Per-t representation counts are in `data/z52b/pass2/NC2/Z2624/i3_counts.txt`. This is a bounded calibration of the proposed small-group event, not evidence about the full n≤10^9 goal or a proof.

Reproduce with `ulimit -v 8000000; timeout 60s uv run python scripts/z52d_p2_NC2_Z2624_r2.py`; the script enumerates the exact formula `n=(tu-1)v-u` and reports per-t counts, distinct coverage, and uncovered count. The search bounds u using `n >= (3t-1)u-3` and v using `n<=100000`.
