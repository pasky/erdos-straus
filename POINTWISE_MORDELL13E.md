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
