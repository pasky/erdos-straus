# z52d Pass-2 round 2 — NC2 part 4

## Z2720 — Klein sail vertex-count premise fails on the HJ proxy

Fixed the item’s cone convention through the repo’s HJ expansion `p/A = [[b₁,…,bᵣ]]`; used “geometric HJ vertices” in the stated digit sense (digits ≥3) as the computable proxy, explicitly not a convex-hull sail. On all 4,960 QNR pairs `(A,p)` with prime `p ≡ 1 (mod 4)`, `p ≤ 499`, the HJ length-three count was 428, while the digit-≥3 count is different; for example `13/5 = [[3,3,2]]` has length 3 but only two digits ≥3, and `13/2 = [[7,2]]` has length 2 but one such digit. This falsifies equality between length and the item’s proposed count under this proxy, but does not settle the cone orientation / sail correspondence.

Reproduce: `ulimit -v 8000000; timeout 300s uv run --with numpy --with sympy python scripts/z52d_p2_NC2_r2_metrics.py`; see `data/z52b/pass2/NC2/Z2720/metrics.json`.
