# POINTWISE_MORDELL13E — is x** = x(2,15) sterile? Complete enumeration by ES level (task O107)

Status: work in progress (side agent O107, branch `side-agent/xss-sterility`). Labels as in DISCOVERIES.md.
Builds on POINTWISE_MORDELL13B.md (§1 Lemma 1.1/1.2, §2 Cor. 2.5, §4 engine), POINTWISE_MORDELL13C.md (§3, §5).

Notation as in 13B: `T={11,13}`, `x** = x(2,15)` (`x_11=2`, `x_13=15`, `x_q=1` for q∉T). A *box* is
`(fam, M_T, r mod M_T)` of a T-generic datum; x** lies in the class iff `r≡2 (11^{v_11(M_T)})` and
`r≡15 (13^{v_13(M_T)})` (13B Lemma 1.1, CRT).

## 0. Baseline: all ES levels ≤ 4·10⁷ (CERTIFIED, 13B engine)

`scripts/m13e_boxtest.py 2 15 R` over the 13B/13C engine output (R = all 32 T-units `1<N≤4·10⁷` plus
`N=11⁴13⁴`; 229963 boxes): **0 boxes contain x\*\***. Positive control: the same test at x* = (2,2) returns
exactly the two data of 13B Thm 3.1 (II3 (8,33,11999), I2 (125,88,11999); re-found at four levels by the
non-canonical inversion).

## 1. A faster complete ES engine (m13e_es) and the per-level test

*Engine.* `scripts/m13e_es.c N [xlo xhi]` lists all `(x,y)` of ordered solutions `x≤y≤z` of `4/N=1/x+1/y+1/z`
with `x` in the given part of `(N/4,3N/4]`. Method of `m13b_es.c` (13B §4): `r/s=(4x−N)/(Nx)` reduced, `y=(D+s)/r` for
the divisors `D≤s` of `s²` with `D≡−s (mod r)`, `y≥x`. Changes: segmented sieve (no `O(N)` memory), 128-bit `s, D`,
and the congruence is solved by meet-in-the-middle (since `gcd(r,s)=1`, every `D | s²` is a unit mod r; split
the primes of s into two groups with balanced divisor counts; hash the group-1 residues `d₁ mod r`, scan the group-2
values `−s·d₂⁻¹ mod r`). `z` is not printed; `scripts/m13e_inv.py` recomputes `z=1/(4/N−1/x−1/y)` exactly and
aborts unless it is an integer `≥y`. It also aborts unless the chunk files tile `(N/4,3N/4]` (completion lines).
Then it applies the validated 13B inversion (`m13b_invert.cands/boxes_of`, Lemmas 2.1–2.4) and tests every box
against x** and x*. Speed: ≈1.1 µs per x at `N≈3·10⁷` (9× faster than m13b_es).
*Validation.* (i) Output identical (as sets of `(x,y)`) to `m13b_es` for N = 11, 121, 143, 1331, 1859, 2197, 24167,
371293, 32166277. (ii) At N = 32166277 the box set is identical to the 13B/13C engine output (25116 boxes).
(iii) At N = 1859 the two x* data are re-found. Chunked and unchunked runs agree.
