# z38_numerator8_control — the 8/n control for any H⁻-type argument (O268)

**Idea.** Brief's soundness check: the analogous split for 8/n must FAIL at 131 and 241 (Pomerance–Weingartner Table 1).

**Result.** The Brauer character on the 8/n c = 1 line 8uBC = n + u + B is again χ_{−4uB} (BL Rem 1.10; checked on 6 210 hits for
m = 8, 12, 16, `scripts/z38_typeII_check.py`). M_BM^{(8)} ≈ 0.067L² (half of 4/n); the line fails at 835 primes ≤ 10⁶ (largest
992 903), incl. 131 (M_BM = 0.56) and 241 (0.46) (`z38_mbm.c` with K = 8). So the H⁻ analogue fails there, as it must.

**Barrier screen.** The BM layer is numerator-blind, so a proof of H⁻ cannot be: it must be accurate at the scale of the main
term itself (≈ 0.5 at 131, 241) — B3. T1: same vanishing at squares for every numerator.

**Cheap numerics.** As above.

**Assessment.** EVIDENCE/control: the framework passes the k = 8 test (no false prediction), and confirms that the BM layer carries
no model-specific positivity.
