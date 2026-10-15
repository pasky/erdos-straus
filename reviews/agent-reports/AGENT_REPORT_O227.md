# AGENT_REPORT_O227 — Conjecture 0.2 at q = 3: the thirds corner versus x*_c (FF_THIRDS_CORNER.md)

Branch side-agent/ff-thirds-corner. Main file FF_THIRDS_CORNER.md; scripts scripts/zt_*; logs data/zt_*.
ES is not solved; no infinite case of ES or ES_q is claimed. Conjecture 0.2 is NOT proved.

## SHARP
1. **Liouville lemma (PROVED, one line).** From E·C₁ = g'T^{s−1} + w₁: a tuple covers x_u at level N iff −w₁/C₁
   approximates u T-adically to order N + 1. For a polynomial u (degree h) this forces max(a − 1, b − 1 + h) ≥ N + 1 or
   an exact identity w₁ = −uC₁. At x*_c (h = 1) the exact case dies by 2 ≠ 0, so **every covering tuple is lopsided:
   max(a − 1, b) ≥ ⌈s/2⌉ + 1. The thirds corner (+0.167 super-critical exponent) and every cyclotomic tuple provably
   miss x*_c** (goal 1 answered by a degree argument, not by Frobenius). Second constraint (Cor 3.2): max(z + 2a − 2, t − 1) ≥ N + 1.
2. **Covering = rational T-adic approximation by "tuple rationals" −w₁/C₁** (dictionary, PROVED content). Generic points
   are reached by balanced tuples (exponent 3/2); polynomial/low-height points have Liouville exponent 1 and are reachable
   only by lopsided or exact tuples. So x*_c IS special in its cylinder (corrects FUNCTIONFIELD_ES3 §3 Assessment).
3. **Complete level-by-level search is now ~3^N per level instead of ~3^{2N}** (Prop 2.1: the small side M = m'w₁ forces
   g', E, w₁ in case 1 — in closed Bezout form Z = T^{−N} mod M, E = cT^{N+1}Z − (1 + cT), Prop 5.1). Result: **no Case B
   tuple covers x*_c at any level N ≤ 20 (k = 2, both c)**, and none at N ≤ 18 for k = 3; previously N ≤ 8 (k = 2), 7 (k = 3).
4. **Leading coefficient = archimedean sign** (Assessment, analogy with (J)55): exact (structured, periodic) coverings of
   polynomial points need lc(u) = −1; at lc(u) = −1 x*_{−1} is saved only by 2 ≠ 0 (T ≡ 1 mod T − 1), the same bit that
   makes characteristic 2 covered. q = 3, A = T is covered because depth-1 cylinders make Liouville vacuous and the exact
   families E = −u(0) ∈ {1, 2} exhaust F₃^*.

## Replay
```
gcc -O2 -o /tmp/zt_lop scripts/zt_lop.c
/tmp/zt_lop 3 2 3 20 1,1   # and 1,2; k = 3: /tmp/zt_lop 3 3 4 18 1,c   (N = 20: ~1 h per c)
gcc -O2 -o /tmp/fc scripts/bsE_famcount.c -lm && /tmp/fc 3 2 17 print > /tmp/fc.txt
PYTHONPATH=scripts uv run python scripts/zt_liouville.py /tmp/fc.txt 4
PYTHONPATH=scripts uv run python scripts/zt_lemma31.py /tmp/fc.txt 4
PYTHONPATH=scripts uv run python scripts/zt_lop_xcheck.py /tmp/fc.txt /tmp/zt_lop 8 4
PYTHONPATH=scripts uv run python scripts/zt_bezout_check.py
scripts/zt_ctl.sh /tmp/zt_lop 12 4 > /tmp/ctl.txt && PYTHONPATH=scripts uv run python scripts/zt_calib.py /tmp/ctl.txt 5
uv run --with python-flint python scripts/zt_cyclo.py 200000
cd scripts && uv run python zt_rate_lop.py 1,2,3 60
```

## Results (labels)
* Lemma 1.1, Lemma 1.2, Cor 1.3, Prop 1.4 (exact tuples at polynomial points: need lc u = −1 and a discrete-log condition
  T^{s−2} ≡ −v₁ mod u), Prop 2.1 (complete search), Lemma 3.1 (covering ⟺ m'w₁² + uv₁ ≡ 0 mod T^{N+1}), Cor 3.2, Prop 5.1:
  PROVED. Checks: census (bsE_famcount s ≤ 17, 348 tuples) — Lemma 1.2 at 80 polynomial points: 0 violations; Lemma 3.1 on
  27 840 (tuple, u) pairs: 0 mismatches; zt_lop vs census at all 80 polynomial points of degree ≤ 4, levels 3..8: identical;
  Prop 5.1 identities on 3000 random cases.
* x*_c uncovered at all levels 3 ≤ N ≤ 20 (k = 2, both c) and 4 ≤ N ≤ 18 (k = 3): EVIDENCE (complete search, one code beyond level 8, census
  cross-checked to level 8). With Case A (ES2 theorem): no linear family of level ≤ 20 is valid at x*_c (k = 2). Level 21 exceeded the 8 h budget (c = 1 killed; c = 2 was still running at R247 review time; (R247 repair) the c = 2 log through N = 20 is now committed as data/zt_lop_xstar_c2.txt).
* Cyclotomic tuples (h = 2, 3 exhaustive, h = 4 sampled): max depth of agreement with −(1 + cT) is 4 / 13 / 10 against the
  required 6 / 15 / 42 (EVIDENCE, consistent with Cor 1.3).
* Lottery model at polynomial points (Assessment) calibrated on 52 polynomial points of degree 2..4, levels 5..12 (EVIDENCE):
  model 2.9 vs 2 unstructured hits; levels 6..12: 1.5 vs 0 (with O226's parity law z ≡ t ≡ s mod 2; without it 5.2 / 2.8)
  — consistent within the large Poisson error (R247 repair; formerly "right order, slightly conservative"). At x*_c the model is ≈ 3·10⁻³ per c
  over levels 3..17, decaying ≈ ×1/3 per level; extrapolated mass beyond level 20 ≈ 10⁻⁷. Generic points: λ_N ≈ 0.1 per level.
* Route bounds restricted to the patterns allowed at x*_c (§7, grid EVIDENCE): q = 3 exponent +0.167 → exactly 0.000 (critical
  on a 2-dimensional part of the face b = 1/2 and on segments of t = 1/2; (R247 repair) formerly "at a degenerate corner where
  true counts are polynomial", which was false).

## What did not work / limits
* No structural proof of Conjecture 0.2: after both Liouville constraints the residual condition (Prop 5.1) is a
  structureless divisibility "E_M | T^{s−2} + m'w₁²" for ≈ 3^{N−2} Euclid-determined E_M per level — a lottery with
  exponentially small odds, not an obstruction. Localising the measure argument near x*_c does not help (tail gets worse).
* O(3, T²) ≠ ∅ remains CONJECTURE (strong EVIDENCE + calibrated heuristic).
* Case A at polynomial points other than x*_c was not examined (controls are Case B only).

## Sparks (not pursued)
* Diophantine-approximation framing: O ∩ slice = complement of T-adic balls around tuple rationals; is there a positive-
  Hausdorff-dimension set of "badly approximable by tuple rationals" points provable via a Cantor/Schmidt-game argument
  using only counts of lopsided tuples?
* ℤ face: small-integer points u on the r-generic line of (J)26/(J)54 — Liouville forces lopsided ET divisors f ≥ r^{N+1} − |u|;
  sign of u decides exact families. Could give explicit sterile Mordell points with u ∈ ℤ.
* Higher-degree polynomial points: the periodic structured families at lc(u) = −1 (discrete-log in (F₃[T]/u)^*) — classify
  which polynomial points are covered; conjecture: all lc(u) = +1 polynomial points not covered at level ≤ 5 are sterile.
* O226's parity law (z ≡ t ≡ s mod 2) is now in the model (it improved calibration); a higher T-adic-digit version of its root-product law might cut the case-1 candidates or give a non-lottery obstruction at x*_c.
* zt_lop case 2 enumerates (M, v₁, K) naively (≈ N·3^{N} inner steps); a divisor-based loop would make level 22–23 feasible.
