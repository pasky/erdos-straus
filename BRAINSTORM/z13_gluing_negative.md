# z13_gluing_negative — CRT gluing does not improve the forced one-prime witness (O237)

**Idea (spark 4).** Glue forced windows so that their exponent budgets combine and the overflow cancels.
**Result (PROVED, CAP_DOWN Prop 4.1, after self-review repair).** Forcing lives in the 2-torsion of (ℤ/m)^*; the
overflow is the odd part of a discrete log. At a composite forced window, a one-prime witness needs a prime s | K with
odd exponent and even order in every component (not guaranteed), and then has cap max{0, (lcm(o_i/2) − b)/2} ≥ each
component's (same K). One solution has one x, and K(m) = (n+m)/4 is affine in m: no multiplicative gluing of windows.
**Where B2/T1 bite.** Cap 0 = −1 ∈ Σ_m(K) (modulus part of the solution); at odd squares no Type-II window at any cap.
**Label.** PROVED (narrow scope: one-prime witness at composite windows) + Assessment (no gluing mechanism seen).
