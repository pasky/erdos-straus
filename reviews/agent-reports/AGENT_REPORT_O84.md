# AGENT REPORT O84: housekeeping (WINDOW3 count, LS6 toy tolerance, full verify)

Branch `side-agent/housekeeping-window3-ls6`. No mathematical labels were changed.

## (1) POINTWISE_WINDOW3 §3: 197 vs 195 window configurations (commit 60fcf4d)
Both counts are correct. They count different sets.
* `window3_model.window_configs(e, 0)` (ε=0.1, K=8) returns **197** configurations, using the
  combinatorial criterion "min cell sum < 1". `window3_rcheck.py 0.1 8 0.5` reports this number,
  and so does the §2.2 table (`parity 0 configs 197`). The table entry stays as it is.
* `window3_lp.py build()` also drops cells with `mu < 1e-14·max mu`. That removes two
  configurations: (4,0,1,0,0,1,0,0) (min cell sum 0.99952, quadrature mass 1.8e-18) and
  (5,1,2,0,0,0,0,0) (0.98901, 9.2e-17). Their cells only touch Σ=1 at a corner. This leaves
  **195** LP columns, and 195² = 38025 joint columns. A rerun gives rows 89 (two-window) and
  0.48929 for the one-window LP.
* The §3 sentence now reads "Window configs 195 (LP columns; joint 195² = 38025), rows 89". A
  following line explains the 197/195 difference. I removed the parent's "unreconciled" note.
  verify.py was not changed; it does not assert the count.

## (2) scripts/review_ls6_exact_toy.py tolerance (commit 90f0d2c)
I added an absolute slack of `+ 1e-12` to the four bound asserts: (2.1), Prop 2.2, (4.1) and
Thm 5.1. Before this change, `run(3,(2,3,5,7),8)` failed with lhs = 8e-17 against pin = 0. The
same happens for seed 4 on that pool. In every pin = 0 case, lhs is a float zero, ≤ 9e-16. In
all other cases lhs is about 0.1–1, so the check still has real force.
* After the fix, seeds 1–4 pass on pool (2,3,5,7) and on pool (2,3,5).
* **Effect on verify.py (dp): none.** It only uses seed 2 on (2,3,5,7) and seeds 1–4 on
  (2,3,5), where no pin = 0 case occurs.
* One caution: if (dp) is ever extended to seeds 3 or 4 on (2,3,5,7), its `lhs/p42` ratio would
  divide by zero. Those cases would need to be filtered out (`p42 > 0`).

## (3) Full verify.py
I ran `OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 timeout 1800 uv run --with scipy --with mpmath
python verify.py` under `ulimit -v 8000000`. It finished with rc = 0 and printed **"all checks
passed"**: 5:32 wall, 554 MB peak RSS, no skips. No block failed, so nothing else needed fixing.
