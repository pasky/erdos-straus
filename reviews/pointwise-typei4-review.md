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

### Cor 1.4 / Remark 1.6 (reduced equation, dictionary) — SOUND
Re-derived: `c'gh−P_1=16c'P_1²X²−c'7^{2a+2b}δ²−P_1`, and `K+c'D²=7^{a+2b}(2^{L−4}+c'7^aδ²)=7^{a+2b}M`, so (1.2) ⇔
`P_1(16c'P_1X²−1)=7^{a+2b}M`; with `7∤P_1` (true as `7∤M`) this is (1.1) ✓. Dictionary: `8nδ=8c'XD`, so
`F=A−8nδ=32c'P_1X²−8c'XD−1=8c'Xg−1`, `e=8c'Xh−1` ✓; `J=8g`, `J'=8h`, `u=c'JJ'−Λ=64(c'gh−K)=64P_1` ✓ (TYPEI2 (2.1)).
The finiteness bounds after Cor 1.4 (`(4c'g−1)P_1<K`, `h(8c'g−1)≤8K+g`) re-derived ✓ (they are per `(L,a,b)`).
"`a=1` is the weakest split" ✓: for fixed `s=a+2b`, `a+b=s−b` is minimal at `b=(s−1)/2`.
All of (1.1), (1.2), Remark 1.6, Lemma 3.1(i)–(iv) were checked by `scripts/review_typei4_identities.py` on every
fibre certificate obtained by **brute-force factorisation from the definition** (`L≤18`, `a≤5`, `b≤2`,
`c',k'≤101`): 8 fibre certificates (levels 11,13,14,14,16,16,16,18 — exactly the author's ones in that box), 0 failures,
none at levels 5–10, 12, 15, 17.

### Lemma 3.1 / Cor 3.2 (finiteness per (L,b), all a, all heights) — SOUND
Re-derived line by line: `K−c'gD=7^{a+b}z` ✓; `P_1(4c'gX−1)=7^{a+b}z`, `4c'gX−1≥3` ⇒ (i) ✓, `7∤P_1` ⇒ (ii) ✓;
(iii) `P_1=c'g(g+2D)−K` ✓; (iv) case `2y>T7^b`: `7^{a+b}<P_1≤z<T7^b/2` ✓; case `2y<T7^b`:
`7^{a+b}≤7^{a+b}(T7^b−2y)<c'g²≤y²<T²7^{2b}/4` ✓ (uses `δ≥1`, `c'≥1`); `2y≠T7^b` ✓ (`y` odd, `T` even).
Cor 3.2: the search over `(y=c'gδ, a)` with `P_1` from (iii) and `X` from (ii) is complete: (ii) and (iii) together
force `g+2D=4P_1X+D`, i.e. `g=4P_1X−D`, so every output is a genuine solution of (1.2) ✓.
**Independent re-derivation (different route).** In TYPEI2 (2.1) coordinates, with `m=c'Jδ`, `R=2^{L−2}7^b`,
`V=7^{a+b}` I get `u=c'J²+16V(m−R)` and `u·(F−1)=16V(2R−m)`; hence `m<2R`; `m≠R` for `L≥7` (else `J|16Vδ` with
`v_2(J)=L−2>4`); and `16V<R²` (case `m<R`: `16V<c'J²≤m²`; case `m>R`: `16V<u≤16(2R−m)` using `V|F−1`). This uses
the 7-adic sign `F≡1 (7^{a+b})` instead of `7∤P_1`, does not assume `8|J`, and gives a weaker but sufficient bound
(`7^a<T²7^b`, vs. the author's `7^a<T²7^b/4`). It is implemented in `scripts/review_typei4_jsearch.c`.
**MINOR (D4)**: AGENT_REPORT_O89 item 3 writes the bound as "`7^a<2^{2L−10}7^b`"; that is the `2y<T7^b` case only,
which is the max of the two — fine, but say "max of the two cases".

### Prop 3.3 (L=7, 7∤k, by hand) — SOUND
`T=8`, `b=0`: case `2y>8` needs `7^a<4` — impossible, so the sub-case `y=5,7` is in fact vacuous by (iv) already
(the author's extra argument `P_1≥15>z` is also correct). Case `y∈{1,3}`: `P_1≤y²−14(4−y)<0` ✓.
