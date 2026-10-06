# AGENT_REPORT O85 — verify.py blocks (dw)–(dz)

Branch `side-agent/verify-blocks-7`. Full `verify.py` (2 threads, `--with scipy --with mpmath`,
`ulimit -v 8000000`): **all checks passed**, 5 min 38 s wall; new blocks ≈ 31 s total.

| block | document | content (reviewers' from-scratch code preferred) | s |
|---|---|---|---|
| (dw) | POINTWISE_TYPEI3 | R72 `review_typei3_fs.c` at (7,9), f < 10⁸: 3 571 429 f, 0 certificates; R72 engine (re-verified by `review_typei3_check.py`) = `review_typei3_naive.c` certificate sets at the 13 sign points of R72 item 1 (sizes 3,0,14,0,0,0,0,0,8,3,0,1,0; (14,2,15) at (7,1)); R72 `vieta.py` (L5.1 general B, Cor 5.2, P5.3) and `level6.py 25` (P5.4/5.5); inline L1.1 (i)–(iii) + L1.2 on all certificates ck ≤ 3000 at w = 1, 17, −7, 25, L1.1 converse on small tuples, P5.4 mod-16 cycle, P5.5 mod-32 period check (D ∈ {7,15,23,31}) | 15.6 |
| (dx) | POINTWISE_MORDELL | Thm 3.1: both certificates in full via R80 `review_mordell_check.py` (loaded) + own integrality test; exceptions exactly {112561} / six residues; every class used; 2513 end-to-end ES solutions at the least prime of each covered class; 3.1(c) = {112561, 352801}, 592801 covered; Comp 4.1 at M ≤ 3·10⁴ (R80 point engine) and rigid level 11²13² (R80 rigid engine), each with a positive control (13-generic point ∈ II2 (9,2,143)) | 9.6 |
| (dy) | EXCEPTIONAL_WEIGHTS | L3.2 exhaustive, all F ∋ 0, ℓ ≤ 29 (510 064 sets; min ratio 21.3), inline cmath for all F, ℓ ≤ 13; R81 L3.1/Thm 3.3 chain; [scipy] Selberg Φ_K, L2.0, Thm 2.1 chain + L1.2 primal/dual brackets on 10 R81 toys | 2.7 |
| (dz) | POINTWISE_MN3 | R82 `atoms.py` (422 083 atoms, M ≤ 10⁵), `lemma11.py` (m=5, q₀=8: 4125; m=6, q₀=9: 2174 atoms, exact), `et35.py` (N ≤ 1000, m = 5, 7); inline from (M,D): L2.1 identities, m/N identity, ET bounds on 155 665 atoms (m = 5, 6, 7) | 3.5 |

POINTWISE_MORDELL17 is not on main → skipped.

## Finding for the parent (MINOR, POINTWISE_MORDELL §0 / R80 checker)
* §0 says that with the family parameters fixed, "x,y,z are polynomials of degree ≤ 2 in n with positive
  coefficients". That is false for I2 (x has degree 3), I3 (x has degree 4) and II3 (z has degree 3). All
  coefficients are still ≥ 0 and the values at n = 1 are > 0, so the positivity conclusion (B = 1) stands.
  (dx) checks this for all 153 certificate coordinates.
* R80's from-scratch `review_mordell_check.py::covers` tests integrality only at s = 0, 1, 2 ("degree ≤ 2").
  For degree-3/4 coordinates that is not a proof of integrality on t + Lℤ. The author's `mordell_check.py`
  uses the true degree, so Theorem 3.1 was correctly certified. (dx) tests s = 0..4 and asserts that R80's
  test agrees with this on every (target, class) pair. It does, so Theorem 3.1 is unaffected. Suggested
  fix: one sentence in §0, and `range(5)` in `review_mordell_check.py`.

Commits: one per block, plus a docstring commit, plus a STATUS/report commit.
