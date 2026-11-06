# z60 MS105 — random locally-square non-squares n = x² + kP_y (Jacobi depth > y), y ∈ {47, 59, 71, 79, 83}
Inputs `scripts/z60_ms105_locsq_gen.py 100` (seed 60106): 100 per y with P_y = 8·∏_{3≤q≤y} q, k < 400 (n up to ~4·10^35),
plus 100 same-size controls in 𝔐 per y.  Decider `scripts/z60_ms105_dec128.c 10000000` (count of d-form hits d ≤ 10^7).
Result: no UNK.  Mean hits (d ≤ 10^7): LS 27.4–29.0 vs controls 32.2–33.9; min 12 vs 13; geometric-mean first hit
213–362 (≥ y by Jacobi) vs 39–54.
