# AGENT REPORT O35 — verify.py blocks (cp)–(ct)

Branch `side-agent/verify-blocks`. Five new replay blocks follow the (ci)–(co) style:
self-contained code or importlib imports of the document's own script (precedent:
(ch), (ck), (cm), (co)), deterministic seeds, and assertion messages tagged by
document and lemma. Module docstring and STATUS.md bullet updated.

**Full run:** `ulimit -v 8000000; uv run --with scipy python verify.py` → exit 0,
"all checks passed", 257 s wall, 0.54 GB max RSS. The five blocks add ≈ 20 s
(timings below are from the full run).
`(cr)` uses numpy/BLAS. With `OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2` it takes 6.6 s instead of 14.4 s,
so set these on the shared machine.

| block | document | seconds | what is checked |
|---|---|---|---|
| (cp) | EXCEPTIONAL_TUPLES2 | 0.9 | Lemma 1.1 for all ℓ ≡ 3 (4) ≤ 1500: bijection (r,s,m) ↦ r²m onto div(A²); (1.1) on every residue; −1 ∈ 𝓡(ℓ); 4rs \| ℓ+1. On (y,N) = (20,50), (24,300), (32,200), (44,1000): Cor 1.2 (every hit set has all form-groups admissible); (1.3) S_j = Σ_adm C_T; Lemma 3.1 C_{T_G} = ⌊(N+1)/q_G⌋. Thm 4.1 proof identity Σ(−1)^j e_j^𝔄 = E a(H) checked in exact rationals, comparing tuple enumeration with configuration enumeration. Inadmissible configurations exist in each case and E a(H) ≠ Π(1−p), so the check is not vacuous. Also Σ(−1)^j e_j = Π(1−p) and the two-sided intermediate bound with u₁. |
| (cq) | EXCEPTIONAL_KARY3 | 1.7 | Lemma 2.1 on 166k y-smooth M ≤ 10⁹ (y = 7, 13, 23): S_y squarefull; M ≤ S_y·e^{Z log y} in integers; the dichotomy S² > K or Z ≥ u/2 on dyadic blocks; the k-indicator bound for k ≤ 6. Lemma 2.2 proof: direct tuple sum ≤ partition bound, and the c_m step. Lemma 2.3 sub-steps: τ(A²) = 1∗2^ω; q \| M ⟺ A ≡ 4⁻¹; Euler-product identity for Σ h(e)gcd(D,e)/e (exact); (1−1/p)⁻¹e^{−3/p} ≤ 1. Lemma 3.1: Γ(4rh) ≤ 8Γ(r)Γ(h). §8 regression for y = 7, 13 against data/kary3/moments.txt. |
| (cr) | EXCEPTIONAL_LARGESIEVE2 §§1–7 | 14.4 (6.6 at 2 threads) | Imports scripts/largesieve2_checks.py. Lemma 1.1: m* = 1/24 and 1/140, the dual certificate, and the second LP ≤ 1/m*. Lemma 2.2/Thm 2.4(i) on 504 Farey rows. Lemma 4.1 on check3's six kernels: the same random stream is consumed, but the cvxpy QP for D* is **not** replayed. Thm 4.3 steps on the full family plus 3 thinnings; family sizes and leaks match data/largesieve2/checks.txt. Self-contained parts: Thm 4.3 constants (unit-square χ² values, uniform reduction, (1−x)⁻² ≤ 1+4x) and Prop 6.1 brute force for N < 400. Without scipy the LP parts are skipped with a note. §§8–9 are not replayed. |
| (cs) | POINTWISE_OMEGA8 §§1–5 | 0.9 | Imports scripts/omega8_brw_check.py. Lemma 3.1 checks B ≤ F, the error identity and the E[F−B] bound. Trials: 40 at n = 6, q = 5, seed 1 (identical to the data/omega8/brw_check.txt run) and 30 at (4,3). B ≤ F and the identity also hold with arbitrary random u_j, and E[A_j e_j²] = P(E_j)·energy holds. Lemma 3.2 c_W formula against the ES truncation on 45 cases, with \|c_W\| ≤ (N+1)^t. Exponent bookkeeping (Assessment-level arithmetic, constants = 1): log(log p)/log L decreases from 16.1 to 14.21 at L = 1e30, with exponents for t and K near 6 and 7. Thm 4.4: log₂p/(L/log L) = 1.3863 = 2 log 2 in a log-space chain. |
| (ct) | POINTWISE_TYPEI | 2.0 | ck_min engine copied from R31. Lemma 1.1 dual form on 3441 (p,c,k) with p < 150. Thm 6.1: the 4 certificates cover all 12 relevant classes mod 840; all 1628 hard p < 3·10⁵ with (5\|p) = −1 have ck_min ≤ 10, = 5 when p ≡ 2 (5); ck_min(193) = 10. Census file: rows are exactly the primes p ≡ 1 (24) below 10⁷ (82887); per-n_p maxima equal the §6 C(r) lower bounds (5:10 … 43:883); 200 seeded rows and the 4 record rows are recomputed. |

**Not covered (deliberately):**
- LARGESIEVE2 §§8–9 (under review) and the cvxpy D* QP of §7(3).
- KARY3's analytic content (Shiu, ElT inputs, Thms 4.1/5.1), which has no finite check beyond the sub-steps above.
- TYPEI's long runs: C(7) ≥ 539 formal (~min) and C(11) > 3000 (~40 min).
- OMEGA8 `omega8_levels.py` toys, which the document itself says nothing rests on.

All checks are EVIDENCE/regression. None of them upgrades any status label.
