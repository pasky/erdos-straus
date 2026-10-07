# Hostile review R89 of POINTWISE_TYPEI4.md (task O89)

Reviewer: side agent R89 (branch `side-agent/review-typei4`). Reviewed commit: `e40ba74` (merged).
From-scratch scripts: `scripts/review_typei4_*`. Status: round 1 complete.

## Summary verdicts

| claim | verdict |
|---|---|
| Lemma 1.1 (fibre certificates, δ odd) | SOUND (D1 minor misstatement) |
| Prop 1.2 (Pell form, (1.1)) | forward SOUND; converse SOUND-AFTER-REPAIRS (D2: add `X` odd); RD remark: D3 |
| Cor 1.4 / Remark 1.6 (reduced equation, dictionary to TYPEI2 (2.1)) | SOUND |
| Lemma 3.1, Cor 3.2 (finite per `(L,b)`, all `a`, all heights) | SOUND (re-derived; independent alternative bound found) |
| Prop 3.3 (`L=7`, `7∤k`) | SOUND |
| Comp 2.1 / 3.4, Cor 3.5 (CERTIFIED, any height) | SOUND on every range I replayed with an independent complete engine (table below; all results identical); remaining ranges single-engine (D5) |
| Example (42,32,71) | SOUND |
| Prop 4.1 (scope) | mathematically SOUND; label "PROVED" should be reformulated (D7) |
| "34 level-7 near misses are not fibre certificates" / Obs 1.3 | SOUND (independent enumerator: 17 pairs = 34 divisors, all `≡15 (16)`) |
| Obs 1.5 / 4.2(d) (fundamental unit; EVIDENCE) | label correct; confirmed on all 33 hits of my complete search |
| §4 Assessments | acceptable as Assessments (D8: cite BHV in 4.2(c)) |

No FATAL or MAJOR defect found. Defects: D1–D8, all MINOR.

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

### Observation 1.3 / "the 34 level-7 near misses are not fibre certificates" — SOUND (independently confirmed)
From-scratch height-bounded enumerator `scripts/review_typei4_nm.c` (all slices `ck≤X`, CRT class of the divisor,
direct test `D|N`, `D≤√N`): at `L=7`, `ck≤10⁸`: 17 near-miss pairs with `D≡15 (16)`, **0** with `D≡7 (16)`
(17 pairs = 34 divisors, matching TYPEI3 Remark 5.6's 34). At `ck≤10⁹`, `L=7…12`: `D≡7 (16)` hits only at `L=11`
(the single pair 71·2423, under its 6 splits `α+2γ=11`); `L=8,9,10,12` have no near misses with `D≡7 (8)` at all.
(At `ck≤10⁶`, `L≤16`: fibre hits at `L=11,14,16` only, consistent with Obs 1.3.)

### Computation 2.1 / 3.4 and Cor 3.5 (CERTIFIED; no certificate at x̂_9 for L≤22, v_7(k)≤3 etc.) — SOUND (on the overlap I could replay)
Logic of Cor 3.5 re-checked: a certificate at `x̂_9` is a fibre certificate whose divisor in the F-role has
`v_2(F+9)≥t=2+L−γ≥2+⌈L/2⌉`; both members of each oriented pair are tested; levels `≤6` are TYPEI3 Cor 5.2 /
Props 5.4–5.5 (reviewed in R72); all `a` and all heights by Lemma 3.1 ✓.
**Independent complete search** (`scripts/review_typei4_jsearch.c`, J-coordinates, own bounds, see Lemma 3.1 above;
every hit re-verified with big integers against the definition by `scripts/review_typei4_verify.py`):

| range | my result | author (Comp 3.4) |
|---|---|---|
| `L=7,8`, `b≤6`; `L=9,10`, `b≤5` | 0 | 0 |
| `L=11…14`, `b≤3` | (11,0) F=71; (13,1) F=204135; (14,0) F=71, 2423; (14,3) F=281104279 | identical |
| `L=15…17`, `b≤3`; `L=18`, `b≤2` | (16,0)×3 (F=5335, 9479, 11159); (18,0) F=1639; (18,1) F=6186839; none at 15, 17 | identical |
| `L=19…22`, `b≤1` | (19,0)×2, (20,0)×4, (21,0)×1, (22,1)×2 (F=330359, 21528935); none else | identical |
| `L=23…26`, `b=0`; `L=23`, `b=1` | 6, 2, 3, 3; 0 (max `v_2=10` at L=26, F=9165815, `t_min=15`) | 6, 2, 3, 3; 0 |

In every case `max(v_2(F+9),v_2(e+9))<2+⌈L/2⌉` (max 8; `t_min≥8`), so none is a certificate at `x̂_9`.
Cross-check with the R72 f-graded engine `scripts/review_typei3_fs.c` at 12 values `w≡9 (16)` (`w=25,…,201`), all
`f<3·10⁶`: its 14 certificate rows are exactly pairs from the list above (levels 11, 13, 14, 16) ✓.
Not replayed by me (cost): `L=7,8`, `b=7`; `L=9,10`, `b=6,7`; `L=18…22`, `b=2,3`; `L=24…26` with `b≥1`, `L=23,24` with `b=2`;
they rest on the author's `typei4_lb.c` alone, though its agreement with my engine on all overlaps is strong evidence.
**D5 (MINOR, labels)**: the CERTIFIED label for Cor 3.5 is right in kind (finite computation + PROVED reduction),
but "three engines agree" (report item 4) is true only on overlaps: `typei4_pqsearch` and `typei4_dgraded` are
height-/d-bounded searches, so the **complete** ranges `L≥15` with `b=3`, `L=23–26`, and `b=4…7` at `L≤10` are
single-engine (`typei4_lb`). Repair: state per range which engines replayed it; after this review, `L≤17, b≤3`,
`L≤18, b≤2`, `L≤23, b≤1`, `L≤26, b=0`, and `L≤8, b≤6`, `L≤10, b≤5` have two independent complete engines.

### Author's engine `typei4_lb.c` (code read) — SOUND, one MINOR robustness defect
It loops over odd `y<T7^b`, all factorisations `y=c'·g·δ` (`7∤c'`; `g,δ` unrestricted odd — correct, no hidden
filter), odd `a` with exactly the two bounds of Lemma 3.1(iv) (monotone in `a`, so `break` is correct), then
(iii), `P_1|z`, `7∤P_1`, `X` from (ii), `X` odd and `7∤X`. This is exactly Cor 3.2. **D6 (MINOR)**: `e=8c'Xh−1`
and `N` are computed in signed `__int128` without overflow guard; for `L=26` the a priori ranges allow
`X≈10²²`, `h≈10²²`, so `e`, `N` can exceed 2¹²⁷ (signed overflow is UB; with wrap-around the identity test
`F·e==N` degenerates to a test mod 2¹²⁸, and `pr()` prints garbage for negative values). Only the output
stage is affected (all filters stay in range), and all actual hits have `e<10¹⁴`, so no result changes. Repair:
guard with a bit-length check or verify hits in Python (as `scripts/review_typei4_verify.py` does).

### Example (42,32,71) and Prop 4.1 (scope) — SOUND as mathematics; label should be weakened
Checked by hand: `N=1+4·42·32²=172033=71·2423`; `t=v_2(4·42·32)=8`; `m'=3|72`; `7|70`; `v_7(42)=1`;
`−71≡185 (256)`, `185≡9 (16)`; `v_2(71+9)=4`, `v_2(2423+9)=7<8`, so neither divisor serves at `w=9` ✓.
Also found independently by my `jsearch` (L=11), `nm` (all six splits of `L=11`) and the R72 engine at `w=185` ✓.
Prop 4.1's levels `{11,13,14,16,18,19,20,21,22}`: I have independently produced fibre certificates at
`11,13,14,16,18,19,20,21`; `22` too (`(22,1)×2`, identical to the author's).
**D7 (MINOR, label)**: "any argument … that uses the 2-adic component only through `w mod 16`" is not a
mathematical object, so "PROVED" is a category error. The provable content is: *for each such L, the statement
"no certificate at `x̂_w` of level L for every `w≡9 (16)`" is false* (explicit, CERTIFIED by direct verification).
Repair: state it that way, keep the "fibre-uniform arguments fail" sentence as Assessment. Same for the sentence
"for `L≤10` a fibre-uniform proof is not excluded": add "by the data `b≤7`".

### Observation 1.5 / Assessment 4.2(d) (fundamental unit) — EVIDENCE label correct; confirmed
`scripts/review_typei4_fundunit.py` (own continued-fraction code) on all 33 hits of my complete search (`L≤26`): in every case
`ε=A+8k_o√d` **is** the fundamental unit of `ℤ[√d]` (norm of the fundamental unit is +1), hence also of `O_K`
(`d≡1 (8)`: 2 splits, unit index 1). All 33 also have `a=1`. New small observation: the two `(14,0)` certificates `(c',δ)=(101,5)`,
`(3,173)` have the **same** `d=13220193` and the same unit `A=87263`; they are two different splittings `PQ=d`
of one unit — so "certificates ↔ units" is not injective (worth one sentence in Prop 1.2).
`f=212983` (4.2(d)): `f+9=2¹⁴·13` ✓; the R72 engine confirms it is a fibre divisor, with minimal `t=35`
(`(α,γ)=(0,33)`, `c'=337`, level 66), so ball radius `2^{−35}` ✓.

### Assessment 4.2 (a), (c), (e) — acceptable as Assessment
(a) From (1.1) mod 16, `QY²≡−1` and `Y²=49^b≡1`, so `Q≡15 (16)`; `PQ=d≡1 (8)` ⇒ `P≡7 (8)` ✓. Then `(2/P)=1` and
exactly one of `c',P_1` is `≡3 (4)`, so both sides of the stated identity are 1 ✓ (so "holds identically" is right).
(c) The Pell reformulation is correct: `A=32c'X²P_1−1`, `64dk_o²=E·49^b` with `E=64c'X²7^a(c'7^aδ²+T)` ✓. The
"`O(1)` solutions by primitive divisors" claim is plausible (Bilu–Hanrot–Voutier for the Lucas sequence of
`y`-coordinates) but no reference or argument is given; **D8 (MINOR)**: cite BHV (J. reine angew. Math. 539 (2001))
and spell out that 7 can be a primitive divisor of at most one index, or label the sentence Assessment explicitly.
(e) Fine as stated (`F≡3 (4)` for every fibre divisor, since `F≡7 (16)`).
