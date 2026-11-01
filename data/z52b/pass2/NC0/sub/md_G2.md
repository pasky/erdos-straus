# G2 — interesting items (batch NC0, pass 2)

## Z0896 — signed sibling 4/n = 1/x + 1/y − 1/z: count fingerprint (interesting)
**What.** S(p) = #{(x,y,z): x ≤ y, z ≤ p², 1/x + 1/y − 1/z = 4/p}, all primes p ≡ 1 (mod 4), p ≤ 2·10⁵ (8977 primes).
Exact method: for fixed x, c = 4x − p, d = px, the equation is (d − cy)(cz + d) = d²; m = d − cy runs over divisors of d²
(x < p/2). Brute-force check on p ≤ 37 passes.
**Numbers.**
- S(p) ≥ 1 for every p in the range (0 zeros); S/log²p median 1.32 (p~150), 2.02 (p~1.5e4), 2.25 (p~1.5e5).
- Fit log(S+1) ~ (1, log p, loglog p, α·log L_Q(χ_p)), Q = 31: α_S = +0.330 (R²-gain 0.424); ES count U on the same primes: α_U = −0.297 (R²-gain 0.487).
  Q = 2..100 give the same sign and α (α_S ∈ [0.288, 0.331]; α_U ∈ [−0.306, −0.292]).
- Spearman(residual_S, residual_U) = −0.59 (growth removed); −0.34 after the χ_31 regressor (p ≈ 3e-247).
**Reproduce.** `gcc -O2 -o z0896 scripts/z52d_p2_NC0_Z0896.c && ./z0896 200000 > Z0896_S_2e5.txt` (≈9 min, 1 core; the
i128 version is required, the 64-bit version overflows for p·x > 4·10⁹); then `uv run --with numpy --with sympy --with scipy python scripts/z52d_p2_NC0_Z0896_fit.py`.
Data: data/z52b/pass2/NC0/sub/Z0896_fit.json, Z0896_S_2e5.txt.
**Next.** Vary the z-cap (p^{1.5}, p^3) and split by p mod 8 to test whether the opposite-sign χ_p law and the residual anticorrelation survive.

## Z0961 — partial Spearman of the U-residual with ord_p(10)/(p−1) (interesting)
**What.** Residual of log(U+1) on (1, log p, loglog p) against ord_p(10)/(p−1), 8966 primes p ≡ 1 (mod 4), 101 ≤ p ≤ 2·10⁵.
**Numbers.**
- Raw Spearman +0.132 (p ≈ 4e-36).
- Partial given (2/p), (5/p): +0.135 (p ≈ 8e-38); shuffled-within-sample null: mean 0.000, sd 0.010 (200 shuffles).
- Partial given all quadratic symbols (q/p), q ≤ 47 (15 covariates): +0.068 (p ≈ 1e-10) — the signal is not carried by quadratic characters.
- Index i = (p−1)/ord_p(10) classes, mean residual: i=1: +0.038 (3362 primes); i=2: +0.016; i=3: −0.053 (592); i=4: +0.082 (1305); i=6: −0.088 (290); i=8: −0.205 (273); i=12: +0.038 (203).
- Family check: partial given (2/p),(5/p) for ord_p(2): +0.120; for ord_p(3): +0.363 (p ≈ 1e-277). Within p ≡ 1 (mod 8): +0.188; within p ≡ 5 (mod 8): +0.085.
**Interpretation.** Multiplicative orders of small numbers are controlled by higher power-residue symbols (Chebotarev), so the residual dependence on index(10) points at higher-character structure rather than at (2/p),(5/p). This is a candidate higher-character signature only; the U-residual model itself is the lfit-style regression (Q ≤ 1000).
**Reproduce.** `uv run --with numpy --with sympy --with scipy python scripts/z52d_p2_NC0_Z0961.py` (uses data/z52b/raw/f4_all_30000.txt and pr_20001_200000.txt).
**Next.** Add mod-840 fixed effects and quartic/octic residue symbols of 10 (and of 3) as controls; if the partial stays ≥ 0.05, write it up as a higher-character signature (FRONTIER §2.1).
