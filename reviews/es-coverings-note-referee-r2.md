# Referee report R98 — es-coverings-note, post-referee additions (round 2)

Scope: §4.6 (O91, from PT4 = POINTWISE_TYPEI4.md), Lemma 3.6 paragraph, TYPEI5 (not yet in paper),
§5.3 (O96, from PM13B = POINTWISE_MORDELL13B.md: Prop 5.4, Comp 5.5, Conj 5.6), abstract/intro/open problems;
POINTWISE_MORDELL13B.md §5 post-review extension (x** to e ≤ 1e9).

Status: round 1 complete; all repairs applied by the referee (marked "(R98 repair)" in the paper and in POINTWISE_MORDELL13B.md).
**No FATAL or MAJOR defect.** Seven MINOR defects D1–D7.

## Verdicts

(see per-claim sections below; summary table at the end)

### A. §4.6 (O91; source PT4 = POINTWISE_TYPEI4.md, reviewed R89)

**A1. Definition of fibre certificate / δ odd (para. before Prop 4.12).** SOUND. Re-derived: at `x̂_w` with
`t≥6`, `F≡−w (2^t)` and `w≡9 (16)` ⇔ `F≡7 (16)`; `e≡F^{-1} (2^{L+2})`, `F≡7 (16)` ⇒ `F^{-1}≡F+16 (32)` ⇒
`v_2(e−F)=4`; odd parts `e≡F (n)`. Symmetry `F↔e` (needed for "oriented so that δ>0"): `e≡7^{-1}≡7 (16)`,
and `e` satisfies the same odd congruences, so `(c,k,e)` is again a fibre certificate ✓.

**A2. Prop 4.12 (Pell form).** Forward direction SOUND (re-derived: `A²−(8nδ)²=Fe=1+2^{L+2}c_ok_o²`,
`A²=1+64k_o²c_o(c_oδ²+2^{L−4})`; `v_2(A−1)=1`, `v_2(A+1)=5`; `c'k'²|A+1`, `7^{a+2b}‖`-part in `A−1`;
`F=A−8c'k'D=8c'k'g−1`; `c'gh−P_1=2^{L−4}7^{a+2b}` ⇔ `P_1(16c'P_1k'²−1)=7^{a+2b}M`). Converse SOUND-AFTER-REPAIRS
(defect D1: the converse must assume `L≥7`, since "fibre certificate" is only defined for `L≥7`; with `L=5,6`
the produced triple has `F≡7 (16)` but `t` may be `5`, and Prop 4.10 says no such certificate exists anyway).
R89's "X odd" repair is present (`k'` odd) ✓.

**A3. Lemma 3.1/Cor 3.2 transcription ("With T=2^{L−4} and y:=c'gδ …").** SOUND. Re-derived from (1.2):
`P_1=c'g(g+2D)−K = c'g²+7^{a+b}(2y−T7^b)`; `P_1(4c'gk'−1)=7^{a+b}(T7^b−y)` with `4c'gk'−1≥3` gives `y<T7^b`
and `P_1|z` (`7∤P_1`); case `2y>T7^b`: `7^{a+b}<P_1≤z<T7^b/2`; case `2y<T7^b`: `7^{a+b}≤7^{a+b}(T7^b−2y)<c'g²≤y²<T²7^{2b}/4`.
`g>0` from `c'gh=P_1+K>0`.

**A4. Computation 4.13 (any-height bound).** SOUND; the lists are now reproduced by a THIRD complete engine.
`scripts/review_r98_fibre.c L b` (written from scratch from A3; every hit is re-verified from the definition:
`Fe=1+2^{L+2}c'7^{a+2b}X²`, `F≡−1 (c'X)`, `F≡1 (7^{a+b})`, `F≡e≡7 (16)`), validated for completeness against a
height-bounded brute force from the definition (`scripts/review_r98_fibre_brute.py 16 101 41`: all 7 brute-force
fibre certificates with `L≤16`, `b≤1`, `a∈{1,3}`, `c'≤101`, `k'≤41` appear in the engine output, nothing else in that box).
Full ranges of Comp 4.13 run (logs below): `L=7..10, b≤7`: 0 hits; `L=11..22, b≤3`: exactly the paper's list
`(11,0),(13,1),(14,0)×2,(14,3),(16,0)×3,(18,0),(18,1),(19,0)×2,(20,0)×4,(21,0),(22,1)×2`;
`L=23..26, b≤1` (in order `(23,0),(23,1),…,(26,1)`): 6,0,2,1,3,2,3,0 = 17; `L=23,24, b=2`: 0, 0 — all exactly as stated. Max of `max(v_2(F+9),v_2(e+9))` is 10 (at `L=26`,
`F=9165815`), `≤8` for `L≤25`; always `<2+⌈L/2⌉` ✓. Hence the sentence "The remaining ranges rest on one engine"
is now obsolete (defect D2; also R92's engine already covered `L=7..10`, `b≤9`, TYPEI5 T1).

**A5. Remark 4.14 (scope).** SOUND. `(42,32,71)`: `α=1,a=1,c'=3,γ=5`, `L=11`, `t=8`, `172033=71·2423`,
`−71≡185 (256)`, `v_2(80)=4`, `v_2(2432)=7`, both `<8` ✓. Labels: falsity statement CERTIFIED, consequence
Assessment ✓ (R89 D7 incorporated).

**A6. Lemma 3.6 paragraph (L=7 tower).** Mathematically SOUND as a transcription of PT4 Lemma 3.6
(R89-reviewed; I re-checked the `λ=0` exclusion, which survives even for `7|j`). But OUTDATED (defect D3):
TYPEI5 Lemma 3.1 shows `λ∈ℤ` without `7∤j` (mod `u`: `ρP_1≡j`, `mP_1≡j²`, `7∤P_1`), TYPEI5 Lemma 3.6 shows case
A empty at `L≤10`, and TYPEI5 Thm 3.7 reduces `L=7..10` to the single regime (v). The sentences "and the case
`7|j`, remain open" and "The method should apply verbatim to `L=8,9,10`, but this has not been carried out" and
Problem 2's "(at `L=7`: gaps `j≥2` and `7|j` …)" are superseded.


### B. TYPEI5 (POINTWISE_TYPEI5.md, reviewed R92) — not yet in the paper

Re-derived Lemma 1.1 (Lehmer minimality) line by line: `G={A+4B√d}` is a group, `α²∈G`, `α²=ν_0^m`;
`m≥3` gives a smaller solution `αν_0^{-1}∈(1,α)`; `m=2` forces `P` square (as `Q≡7,15 (16)`), hence all `u`
even; so `m=1`. `L_n≡n (7)` (`s²=1+r²≡1`), `L_7≡7 (49)`, multiplicativity `L_{mn}(α)=L_n(α)L_m(α^n)` and the
`7^r n'` descent are correct. **SOUND.** Consequence (Cor 1.2): `7^b=u_1(P,Q)`, i.e. for given
`(a,c',δ,P_1)` at most one `b`, and the certificate unit is `ε_f` or `ε_f²`. Theorem 3.7 (summary): a certificate at
`x̂_9` of level `7…10` needs `v_7(k)≥8` (two complete engines: `typei4_lb`, `review_typei5_relax`; `≥10` by the
latter alone), `c_oδ>10⁶` (`typei5_dmod`, replayed in R92), `2y<T7^b`, and lies in regime (v) of Prop 3.3
(regimes (ii),(iii) empty by a complete computation reproduced in R92, (i),(iv) and case A by hand). I accept R92's
verdicts (no FATAL/MAJOR). My own fibre engine (A4) independently confirms `b≤7` at `L=7..10` (third engine) —
and `b=8` (0 hits at `L=7,8,9,10`, `logs/r98_fibre_b8.log`), so `v_7(k)≥9` now rests on two complete engines (R92, R98).

**Should it be added?** Yes. Without it §4.6 and Problem 2 misstate the open part (the `7|j` exception is already
closed, and `L=8,9,10` have been treated). Drafted paragraph (applied, see Repairs): Lemma 1.1 as a PROVED
statement with a 3-line proof sketch, and Theorem 3.7 as a summary with mixed label (PROVED + CERTIFIED), replacing
the last two sentences of the Lemma 3.6 paragraph and updating Problem 2.

### C. §5.3 (O96; source PM13B = POINTWISE_MORDELL13B.md, reviewed R95)

**C1. Prop 5.4 (x* covered).** **SOUND.** Verified from scratch from ET Prop 1.9's statement (checked against
`sources/elsholtz-tao-1107.1010.pdf`, p. 8: II3 class `−4a²d−e mod 4ade`, `(4ad,e)=1`; I2 class
`{−f mod 4ac}∩{−c/a mod f}`, `(4ac,f)=1` — the paper's table matches ET exactly) by
`scripts/review_r98_prop54.py`: `M=12670944=2⁵·3·11·13²·71`, `r=12650497`, `r≡1 (6816)`, `r≡2 (1859)`,
the CRT lift of `x*` equals `r`; `(1056,11999)=1`; the I2 class `(125,88,11999)` (modulus `527956000`) contains the CRT
lift of `x*`; `p=12650497` is prime, `p≡2 (11), (13)`; the II3 coordinates of the paper's table
(`c=(n+4a²d+e)/4ade`, `b=ce−a`, `π^{II}=(abd,acdn,bcdn)`) give exactly `(3165624, 3339731208, 5005839614391)` and
`4/p` is reproduced in exact rationals. The "equivalently" list in the proof is correct (`4(ad)'=96`,
`4a²d+1=8449=71·119`, `2a²d+1=4225=25·13²`, `e+2=11·1091`). My search engine (D below) also re-finds the II3
datum `(8,33,11999)` as the unique II3/I3/I1/II2 datum with `e≤10⁵` at `x*` (positive control).

**C2. Comp 5.5 (x** search ranges).** Correct as a transcription of PM13B Comp 5.1, but OUTDATED (defect D4): PM13B
Comp 5.3 extends II3/I3/I1/II2 to `e,f≤10⁹`. The claim "these ranges impose no restriction on the `{11,13}`-part of
the modulus" is correct for the `10⁸` ranges (PM13B, R95) and remains correct at `10⁹`
(R98: `v_q(ad)≤v_q(e+u_q)≤8` for `e≤10⁹`, so `v_q(a_T²d_T)≤16<20`; for II2 `a_Td_T∣(f+1)/4≤2.5·10⁸`
gives `v_q(a_Td_T)≤8`), but this argument for `10⁹` is not written anywhere (defect D7).

**C3. Conj 5.6.** Label EVIDENCE-only is correct; the hedging ("support is weak", warning from `x*`) is
appropriate. Defect D5: "four orders of magnitude" becomes "almost five" with the `10⁹` extension.

**C4. Other §5.3 text.** "the enumeration with `N≤4·10⁷` leaves 15 of 143 subcells uncovered" is literally true;
the Data paragraph correctly flags these counts as upper bounds. `x**∈Σ_13` (main): `x**≡1 (24)`, squares mod 5, 7,
`15≡2` a non-residue mod 13 ✓; `(2/11)=−1` so the corollary-type consequence for `(p/11)=(p/13)=−1` applies ✓.

### D. POINTWISE_MORDELL13B §5 post-review extension (x** to e ≤ 10⁹)

**D-i. Completeness of `m13b_target.c` (audited line by line).** SOUND. For each `e≡3 (4)` it enumerates all T-free
`a'd'∣(e+1)/4`, solves `g∣4λa'²d'+1` over the full table `λ=11^i13^j`, `i,j≤E` (sorted table + binary search,
returns *all* matching `(i,j)`, not one discrete log), forbids `q∣λ` when `q∣e`, and tests every split `λ=a_T²d_T`
against the box conditions (II3: `e≡−u_q (q^{v_q(ad)})`, `q^{v_q(e)}∣u_q+4a²d`; I3: `u_q²+4a²d`; I1: `B∣4a²d+1`;
II2 with T in `ad`: `a_Td_T∣(e+1)/(4a'd')`, no condition at `λ`). The exclusions `B>1` (II2) and `(I||J)` (I1) only
drop data with ES level `N=1`, impossible since `4/1=1/x+1/y+1/z` has no solution (PM13B Lemmas 2.1/2.3 with
`N=1`: `4amjd=a+m+j` has no positive solution). II2 with T-free `ad` is literally II3 with `λ=1` ✓. Arithmetic: `a²d`
mod `q^16` and `13^16<2^64`, products in `u128` ✓. The cap `E=20` is vacuous at `10⁹` (C2). The engine's validation
against the complete §4 engine at box centres is a recall check, not a completeness proof; completeness rests on the
construction, which I accept.

**D-ii. Logs.** `logs/o95_xss_{A,B,gap1,gap2}.log` all end in `# done … hits=0`; ranges inferred from the progress
markers (`2^24`-spaced) are consistent with `(10⁸,5.5·10⁸]`, `(5.5·10⁸,10⁹]`, `(3·10⁷,6.5·10⁷]`, `(6.5·10⁷,10⁸]`.
Defect D6: the logs do not record the command line (point, `E`, `X0`), and the gap logs contain each run twice.

**D-iii. Independent search (from-scratch code).** `scripts/review_r98_xss.c u11 u13 X` (my own derivation of the
membership conditions directly from the ET class definitions by CRT, no discrete logs: for each `e≤X` all
`a'd'∣(e+1)/4` and all T-exponents with `v_q(ad)≤v_q(e+u_q)`; II2: all `ad∣(e+1)/4`; no cap on the T-level).
Validation against direct class membership (CRT lift + ET class test), `scripts/review_r98_xss_validate.py`:
42 points (incl. `x*`, `x**`), `a,d≤24/30`, `e≤1200/1500`: 176 brute-force memberships, engine output identical
on every point (`logs/r98_xss_validate.log` + first run, 0 mismatches). Positive control: at `x*` the engine
finds exactly II3 `(8,33,11999)` for `e≤10⁵`. **Result at `x**=x(2,15)`: 0 data of II3/I3/I1/II2 with `e,f≤10⁷`**
(`logs/r98_xss_2_15_1e7.log`, 6.3·10⁸ parameter tuples tested), **and none with `e,f≤10⁸`** (`logs/r98_xss_2_15_1e8.log`, 8.3·10⁹ tuples, 211 s). So the II2 range `(3·10⁷,10⁸]` and all four families to `10⁸` are now confirmed by an independent engine. **And none with `e,f≤10⁹`** (`logs/r98_xss_2_15_1e9.log`, 1.06·10¹¹ tuples, 43 min): PM13B Comp 5.3 is now reproduced in full by an independent engine.

## Defects

**D1 (MINOR) — Prop 4.12, converse.** "Fibre certificate" is defined only for `L≥7`; the converse did not say so.
Repair (applied): "Conversely, for `L≥7`, every solution …".

**D2 (MINOR) — Comp 4.13, provenance.** "The remaining ranges rest on one engine" is obsolete: R92's engine covers
`L≤10, b≤9`, and R98's from-scratch engine (`review_r98_fibre.c`) reproduces every range of Comp 4.13 exactly
(36 certificates, identical `(L,b)` multiplicities, `max v_2=10` at `L=26`). Repair (applied): replaced by the
statement of the two further engines.

**D3 (MINOR, content) — §4.6 last paragraph and Problem 2 outdated; TYPEI5 missing.** "the case `7|j` remain[s] open",
"The method should apply verbatim to `L=8,9,10`, but this has not been carried out", and Problem 2's "(at `L=7`: gaps
`j≥2` and `7|j` …)" are superseded by TYPEI5 (Lemma 3.1: `λ∈ℤ` for all `j`, all `L≥5`; Lemma 3.6: case A empty at `L≤10`;
Prop 3.3 / Comp 3.4: only regime (v) remains; Lemma 1.1: minimal unit, `b` determined by `(a,c',δ,P_1)`; Cor 2.3:
`c_oδ>10⁶`). The paper's Assessment "linear forms in logarithms are more likely to help than reciprocity" also contradicts
PT5's Assessment (moving two-parameter family of fields; LFL for a fixed recurrence does not apply directly).
Repair (applied): added the `λ`-integrality sentence, Proposition 4.15 (= PT5 Lemma 1.1/Cor 1.2, PROVED, with sketch),
the `typei5_dmod` sentence, Theorem 4.16 (= PT5 Thm 3.7 with per-item labels), a paragraph on regime (v) replacing the
LFL Assessment, an updated Problem 2, a sentence in the Results bullet for `r=7`, and `\bibitem{PT5}`.

**D4 (MINOR) — Comp 5.5 outdated.** PM13B Comp 5.3 extends II3/I3/I1/II2 at `x**` to `e,f≤10⁹`; the paper stopped at
`10⁸` / `3·10⁷`, and "one engine per family group" understated the replication (R95 reproduced II3/I3/I1 to `10⁸`).
Repair (applied): Comp 5.5 restated with `10⁹`, engine names and replication scopes (R95: II3/I3/I1 `≤10⁸`; R98: all
four families `≤10⁹`, i.e. the whole P/Q range is now two-engine; I2/II1/I4 remain one engine).

**D5 (MINOR) — after Conj 5.6.** "four orders of magnitude further in `e`" → "almost five" (`10⁹/1.2·10⁴≈8·10⁴`).
Repair applied.

**D6 (MINOR) — PM13B §5 log provenance.** `logs/o95_xss_*.log` do not record the point, `X0` or the command line; the gap
logs contain each run twice. The ranges are only inferable from the `2^24` progress markers. Repair (applied in the md): a
provenance note. Suggested for future runs: echo the full command line into the log.

**D7 (MINOR) — PM13B Comp 5.3 / paper Comp 5.5: "no restriction on the T-part" at `10⁹` was not argued.** The vacuity
argument of R95 was for `10⁸` (`v_q(ad)≤7`). Re-derived for `10⁹`: `v_q(ad)≤v_q(e+u_q)≤8` (II3/I3/I1), `v_q(a_Td_T)≤8`
(II2), so `v_q(λ)≤16<E=20`. Repair (applied in md and paper).

Not defects (checked): Prop 5.4 (C1); Remark 4.14 numbers; the fibre definition/orientation (A1); the Lemma 3.1
transcription (A3); the Conj 5.6 label; `x**∈Σ_13`; abstract (consistent after O96; no change needed).

## Summary table

| claim | verdict |
|---|---|
| fibre certificate definition, δ odd (§4.6) | SOUND |
| Prop 4.12 (Pell form) | forward SOUND; converse SOUND-AFTER-REPAIRS (D1) |
| Lemma 3.1/Cor 3.2 transcription | SOUND |
| Comp 4.13 (any-height bound) | SOUND; now three complete engines on all ranges (D2) |
| Remark 4.14 (scope) | SOUND |
| Lemma 3.6 paragraph | SOUND but outdated (D3) → repaired with TYPEI5 |
| TYPEI5 Lemma 1.1 / Thm 3.7 | SOUND (R92 + R98 re-derivation); added as Prop 4.15 / Thm 4.16 |
| Prop 5.4 (x* covered) | SOUND (verified from scratch from ET Prop 1.9) |
| Comp 5.5 (x** ranges) | SOUND-AFTER-REPAIRS (D4, D7) |
| Conj 5.6 | label correct (EVIDENCE only); D5 wording |
| PM13B §5 1e9 extension (`m13b_target` completeness) | SOUND (audited); independent from-scratch search to `10⁹`: 0 hits; D6 provenance |
| abstract / intro / open problems | consistent after repairs (D3: Problem 2, Results bullet) |

## Repairs applied

All in commits on `side-agent/referee-coverings-r2`; paper recompiled twice: no undefined references, no overfull boxes
(the one underfull `\hbox` at the PM17 proposition pre-exists).
* paper §4.6: D1, D2, D3 (new Prop 4.15, Thm 4.16, regime-(v) paragraph); Problem 2; Results bullet; PT5 bibitem;
  acknowledgements list `PT5`, `PM13B`.
* paper §5.3: D4/D7 (Comp 5.5), D5.
* POINTWISE_MORDELL13B.md §5: status line, D6, D7, R98 independent check.

## Scripts and logs (R98)
* `scripts/review_r98_fibre.c`, `scripts/review_r98_fibre_brute.py`; `logs/r98_fibre_{A,B,b8}.log`.
* `scripts/review_r98_xss.c`, `scripts/review_r98_xss_validate.py`; `logs/r98_xss_validate.log`,
  `logs/r98_xss_2_15_1e{7,8,9}.log`.
* `scripts/review_r98_prop54.py` (Prop 5.4).
