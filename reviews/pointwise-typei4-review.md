# Hostile review R89 of POINTWISE_TYPEI4.md (task O89)

Reviewer: side agent R89 (branch `side-agent/review-typei4`). Reviewed commit: `e40ba74` (merged).
From-scratch scripts: `scripts/review_typei4_*`. Status: in progress.

## Summary verdicts

(filled in below as each claim is checked)

## Claim-by-claim

### Lemma 1.1 (fibre certificates) — SOUND (one MINOR misstatement)
Re-derived. (i): certificate at `x̂_w` means (TYPEI2 (2.2)) `F|N`, `F≡−1 (m')`, `F≡1 (7^{a+b})`,
`F≡−w (2^t)`; with `t≥4` and `w≡9 (16)` this is `F≡7 (16)`, and conversely `w:=−F` (any lift mod `2^t`).
(ii): `N=1+2^{L+2}c_ok_o²` so `e≡F^{−1} (2^{L+2})`; at odd primes `F≡±1` so `e≡F (n)`. For odd `F`,
`F^{−1}≡F+16 (32)` ⇔ `F²≡17 (32)` ⇔ `F≡7,9 (16)`. Correct. **D1 (MINOR)**: "otherwise `F²≡1 (32)`" is false
(`F≡±3,±5 (16)` give `F²≡9,25 (32)`); the needed statement is only "otherwise `v_2(e−F)≠4`", which is true.
Repair: replace by "otherwise `v_2(F^{−1}−F)≠4`".

### Prop 1.2 (Pell form) — SOUND-AFTER-REPAIRS (forward direction SOUND; converse needs `X` odd)
Forward, re-derived line by line: `A²−((e−F)/2)²=Fe=1+2^{L+2}c_ok_o²`, `(e−F)/2=8nδ`, `n=c_ok_o` ⇒
`A²=1+64k_o²(c_o²δ²+2^{L−4}c_o)=1+64dk_o²` ✓. `d` odd needs `L≥5` ✓. `F≡7, e≡F+16 (32)` ⇒ `F+e≡30 (32)`,
`A≡15 (16)`, `v_2(A−1)=1`, `v_2(A+1)=5` ✓. Odd parts: `gcd(M,c_o)=gcd(2^{L−4},c_o)=1`, `7∤M` ✓; the whole
`c'`-part and `k'²` go to `A+1`, `7^{a+2b}` exactly to `A−1`, `M=P_1Q_1` split arbitrarily ✓. `(A+1)/2−(A−1)/2=1`
gives (1.1) ✓. Identity `A²−d(8k_o)²=1` re-checked from scratch (`scripts/review_typei4_identities.py`).
**D2 (MINOR)**: the converse ("every solution of (1.1) in positive integers with δ odd, a odd, 7∤c'X gives a fibre
certificate") omits **`X` odd**. If `X` is even, (1.1) gives `QY²≡−1 (64)`, `A≡−1 (128)`, and
`F=A−8c_oXYδ≡−1 (16)`, so the proof's "`nδ` odd ⇒ `F≡7 (16)`" fails (and `k'=X` is not the odd part of `k`).
The paper's own Cor 1.4 lists `X` odd, so nothing downstream is affected. Repair: add "`X` odd" (and "`c'` odd")
to the converse hypotheses. Also `F>0` in the converse should be stated (`A²=1+64dk_o²>(8nδ)²` ✓).
Remark (a) is fine. Remark (b): `L≥7` ⇒ `d≡1 (8)` ✓ (`c_o²δ²≡1`, `2^{L−4}c_o≡0 (8)`); `L=5`: `d≡c_o²δ²+2c_o≡3 (4)`
⇒ 2 ramifies ✓; `L=6`: `d≡1+4c_o≡5 (8)` ⇒ inert ✓. The Richaud–Degert sentence is an *Assessment* (heuristic
explanation), not a PROVED statement: "is of RD type exactly when `L≤6`" — RD type means `d=m²+r`, `r|4m`,
`−m<r≤m`; with `m=c_oδ`, `r=2^{L−4}c_o`, `r|4m` ⇔ `2^{L−4}|4δ` ⇔ `L≤6` ✓ (for this particular
representation; other representations `d=m'²+r'` are not excluded by the argument). **D3 (MINOR)**: say "this
representation is RD iff `L≤6`" or prove no other RD representation exists.
