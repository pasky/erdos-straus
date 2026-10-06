# R72 — hostile review of POINTWISE_TYPEI3.md (task O72)

Reviewer: side agent R72 (branch `side-agent/review-typei3`), merged author branch
`side-agent/sign-point-sterility` (incl. Prop 5.5 / Remark 5.6). From-scratch code:
`scripts/review_typei3_fs.c` (f-graded engine), `scripts/review_typei3_naive.c` (definition-only brute
force, no Lemma 1.1), `scripts/review_typei3_check.py` (exact verifier/converter).

Status: in progress (verdicts below are filled in claim by claim).

## Verdicts

### Lemma 1.1 (small-divisor reduction) — SOUND
Re-derived. With `c=2^α7^a c'`, `k=2^γ7^b k'`: `4ck²=2^{2+α+2γ}7^{a+2b}c'k'²=2^{t+γ}·7^{v+b}m'k'`, so (iii)
is exactly `f|N`. `N≡1 (mod 4ck)` makes `e≡F^{-1}`, and `(−x̂)^{-1}` has components `−1, 1, −w^{-1}`
at `m'`, `7^v`, `2^t`, giving (i), (ii). Converse: `f|N` ⇒ `(f,4ck)=1`; in the e-role `N/f≡f^{-1}` lands
in the `−x̂` class. `a≥1` odd ⇒ `7|sf(c)`. Both roles force `f≡1 (7)` and `f≡−w (4)` (odd `w` is its own
inverse mod 4), so the engines' progression filter `f≡f₀ (mod 4r)` loses nothing.
Search criterion: `γ≥0 ⇔ t≤s`, `γ≤t−2 ⇔ t≥⌈(s+2)/2⌉`; correct. Finiteness only for finite role depth
(the author's restriction after the self-review is correct; my engine reproduces the abort at
`(r,w,f)=(7,−15,15)`).

Lemma 2.1 of TYPEI2 (only `v_7(c)` odd can occur at `x̂`) is used implicitly to restrict the search.
Independent check: the naive search with **no** parity filter (`… all`, any `c` with `sf(c)∉{1,2,3,6}`,
`ck≤10⁵`, divisor ≤1000) finds no certificate with `v_r(c)` even at `(7,9),(7,25),(23,9),(7,1)`.

### Lemma 1.2 (height constant) — SOUND
`7|c ⇒ 4ck²=4(ck)²/c≤4X²/7`, `√(1+A²)<A+1`. So a certificate with `min(F,e)≥Y` has
`ck>(Y−1)√7/2=1.32288(Y−1)`. For r: `√r/2` = 2.3979 (23), 2.7839 (31), 3.4278 (47); the stated
`2.39/2.78/3.42·10¹¹` are correct, conservative roundings. Note the constant uses only `r|c` (c≥r), which
holds for every certificate at `x̂` by Lemma 2.1 of TYPEI2.

### Computation 2.1 / Cor 2.3 (f-graded searches) — see "Independent computations" below.
