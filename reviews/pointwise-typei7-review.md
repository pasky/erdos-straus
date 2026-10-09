# R109 — hostile review of POINTWISE_TYPEI7.md (O109, 2-adic closeness to `w = 9`)

Reviewer: side agent R109 (branch `side-agent/review-typei7`), merged `side-agent/sign-point-2adic`.
From-scratch scripts (no author code imported): `scripts/review_typei7_check.py` (certificate checker straight
from the TYPEI2 §0/§3 definition, Thm 2.1/2.4/Rem 2.1(b)/Comp 2.5 numerics), `scripts/review_typei7_lemma11.py`
(direct divisor enumeration of `N = 1+4ck²`, `ck ≤ X`, and brute-force test of Lemma 1.1 / (1.2)). Second-engine
re-runs of grid cells with R89's `review_typei4_jsearch.c` (independent of the author's `typei4_lb.c`).

## Summary verdicts

| Claim | Verdict |
|---|---|
| Criterion (top), Lemma 1.1, (1.2), cofactor clause | SOUND |
| Thm 2.1 (unbounded closeness, `F = 7^s+2^i`) | SOUND |
| Remark 2.1(a),(b) | SOUND |
| Comp 2.2 | SOUND (replayed from scratch) |
| Cor 2.3 (covered part open dense) | SOUND; one MINOR overstatement in the "upgrades Prop 4.1" sentence |
| Thm 2.4 (`F = 71^ν`, `k = 2^γ`) | SOUND |
| Comp 2.5 | SOUND (rows ν = 1, 3, 7, 15, 143 replayed; `ν` and closeness for all m = 4..14 replayed) |
| Comp 3.1 / Cor 3.2 / Comp 3.4 | SOUND as CERTIFIED-once-replayed; see §3 below for the extra second-engine cells |
| Obs 3.3, §4 (labels EVIDENCE / Assessment) | SOUND (numbers re-derived) |
| §5 labels | SOUND-AFTER-REPAIRS (MINOR wording, applied) |

No FATAL or MAJOR defect found.

## 1. Criterion and Lemma 1.1

Re-derived from TYPEI2 (2.2) + §3. At `x̂_w` the odd components are `±1`, so `(c,k,F)` is a certificate iff
`F | 1+4ck²`, `F ≡ −1 (mod c'k')`, `F ≡ 1 (mod 7^{v_7(ck)})`, `F ≡ −w (mod 2^{v_2(4ck)})`, `(F,4ck)=1`, `v_7(c)` odd.
Only the last congruence and `v_2(4ck) = 2+α+γ = t` depend on the split `α+2γ = L`; `N` depends on `L` only. So
"some split" ⟺ minimal `t = 2+⌈L/2⌉` (`γ = ⌊L/2⌋`). ✔

`e ≡ F (mod n)` (both `≡ −1` mod `c'k'`, both `≡ 1` mod `7^{a+b}`, and `e ≡ F^{−1}`), and
`e ≡ F^{−1} (mod 2^{L+2})` with `v_2(1−F²) = 1+3 = 4` for `F ≡ 7 (16)`, so `v_2(e−F) = 4` (`L ≥ 3`). ✔
Identity: `(G−9)² + 16nδ(G−9) − 1 = G(G−18+16nδ) + 80 − 144nδ`, and LHS `= 2^{L+2}c_ok_o²`, hence
`G(G−18+16nδ) = −16E` with `E = 5 − 9nδ − 2^{L−2}c_ok_o²`. ✔ `16 | G` ⇒ `v_2(G−18+16nδ) = 1`. ✔
(Also `E ≠ 0`, since both factors on the left are non-zero — implicit, harmless.)
(1.2): `⌈L/2⌉−1 ≤ L−2` for `L ≥ 2` ✔; `5·9^{−1} ≡ 285 (2^9)`, `≡ 797 (2^{10})` ✔ (script).
Cofactor: `δ ↦ −δ` ✔.

*Numerical (from scratch).* `review_typei7_lemma11.py 400000`: direct divisor enumeration finds 64 oriented fibre
certificates (`L ∈ {11,14,16,18,21,27}`, 9 distinct `(L,b,{F,e})`). For each: `v_2(F+9) = 3+v_2(E)` and the cofactor
version; for **every** split the direct TYPEI2 test `cert_at(c,k,F,9)` agrees with the congruence mod `2^{t−3}`; and
for every `1 ≤ j ≤ L−2`, `v_2(F+9) ≥ j+3 ⟺ nδ ≡ 5·9^{−1} (2^j)` (so the positive side of the "iff" is exercised at
small `j`). 1442 checks, 0 failures. All 9 pairs occur in the author's complete `typei4_lb` lists of the same cell.

MINOR m1 (no repair needed). Lemma 1.1 lists "`nδ` odd" as a hypothesis; the proof never uses it (only `16 | 16nδ`).
Harmless.

## 2. Theorem 2.1, Remark 2.1, Comp 2.2

Every step re-derived: `49` generates `1+16ℤ_2` (`v_2(48) = 4`), so `{7^s : s odd}` is dense in `7+16ℤ_2` ✔;
`ord_{7^j}(2) = 3·7^{j−1}` (checked `j ≤ 4`; `2³ = 8 ≢ 1 (49)`) ✔; `F = 7^s+2^i ≡ 2^i ≡ 1 (mod 7^{b+1})` as
`s = 2b+1 ≥ b+1` ✔; `c' = (F+1)/8` odd, prime to 7 and to `F` ✔; `N = 1+2^{L+2}7^s c' ≡ 1−2^{L−1+i} (mod F)` ✔.
`v_7(c) = 1` odd ⇒ `sf(c) ∉ {1,2,3,6}` ✔; `L ≥ 7` ⇒ it is a fibre certificate in the TYPEI4 sense ✔.

*From scratch* (`review_typei7_check.py`, direct TYPEI2-definition checker `cert_at`): `m = 4`: `(s,i,F,c',L) =
(1,6,71,9,30)`, `ord_71(2) = 35`; `m = 5`: `(3,21,2097495,262187,93184)`, `ord_F(2) = 93204`, `v_2(F+9) = 5`.
Both are certificates at `x̂_{−F}` for two splits each and again at level `L + ord_F(2)`; neither is at `x̂_9`.
For `m = 6,7,8` the construction gives `s = 7`, `i = 1029`, `F ≈ 2^{1030}` with `v_2(F+9) = 8`, `F ≡ 1 (7^4)`,
`F ≡ 7 (16)` (`L` not computed, as the author says; existence of `L` only needs `F` odd). Matches Comp 2.2.

Remark 2.1(b): only `F | N` depends on `L`, through `2^L mod F` ✔; `e ≡ F^{−1} (2^{L+2})` ⇒ `v_2(e+9) = v_2(9F+1)` once
`L+2 > v_2(9F+1)` ✔; levels with `L+2 ≤ v_2(9F+1)` also satisfy `2+⌈L/2⌉ ≤ v_2(9F+1)`, so the finiteness clause
covers both roles ✔. Replayed for `(c_o,k_o,F) = (21,1,71)` at `L = 11, 46, 81, 116`: certificate each time,
`v_2(e+9) = 7 = v_2(9·71+1)` constant ✔. (Brute force also finds `(c_o,k_o,F) = (7,1,71)` at `L = 27`, i.e.
`c = 14, k = 8192`, closeness 7 via `e = 52930935` — consistent with the `(27,0)` row.)

The claim "answers the open question of TYPEI4 §5" is correct: §5 asks whether `max v_2(f+9)` over fibre
certificates is bounded; Thm 2.1 gives `v_2(F+9) ≥ m` for each `m`. (TYPEI4 Assess. 4.2(d) had already observed
closeness 14 at `f = 212983`; the novelty is the proof of unboundedness.)

MINOR m2 (wording, not repaired). "sterility of `x̂_9` … cannot be proved by any test that sees `w` only modulo a
fixed `2^j`" — the precise PROVED content is: for every `j`, the statement "every `x̂_w` with `w ≡ 9 (2^j)` is
sterile" is false. As in R89 D7, "any test" is not a mathematical object. Suggested: add "(i.e. for every `j` the
ball `w ≡ 9 (mod 2^j)` of `Φ` contains covered points)". I leave the author's sentence, since it is immediately
followed by the precise statement "no 2-adic neighbourhood of 9 in `Φ` is sterile".

## 3. Cor 2.3, Thm 2.4, Comp 2.5

Cor 2.3: `Cl(κ) ∩ Φ` is clopen in `Φ` (the 2-adic condition is `w ≡ −F (2^t)`, the others are `w`-independent),
so `C_Φ` is open; density is Thm 2.1's construction with target `−w_0 ≡ 7 (16)` ✔. Sterile part = complement of an
open dense set ⇒ closed nowhere dense ✔. "Positive measure if TYPEI3 is right" correctly labelled Assessment.

MINOR m3 (repaired). "This upgrades TYPEI4 Prop 4.1 (levels 11–22, `w` only mod 16) to all depths." Prop 4.1 is a
**per-level** statement; Cor 2.3 is about the union over all levels and says nothing at a fixed level (at fixed
`(L,b)` there are finitely many certificates, so a fixed-level test modulo a large `2^j` is not excluded). Repair:
"This is the all-depth analogue (over all levels together) of TYPEI4 Prop 4.1 (fixed levels 11–22, `w` mod 16)".

Thm 2.4 (re-derived and replayed): `71 ≡ 7 (16)`, `v_2(71²−1) = v_2(5040) = 4` ✔; `ord_71(2) = 35` ✔,
`2^{70} ≡ 143`, `2^{35} ≡ 72 (mod 71²)`, `ord_{71²}(2) = 2485 = 35·71` ✔ ⇒ `ord_{71^ν}(2) = 35·71^{ν−1}` ✔;
`(2/71) = 1` (71 ≡ 7 (8)) so `⟨2⟩` = squares ✔; `(−7/71) = (−1/71)(7/71) = (−1)(−1) = 1` and `7·2^{29} ≡ −1 (71)` ✔.
Certificate conditions ✔ (`71 ∤ c'` since `8c' ≡ 1 (71)`).

Comp 2.5 replay (own code, sympy `discrete_log`, modular verification `F | 1+2^{L+2}·7c'`, (2.2)):
least odd `ν` and `v_2(71^ν+9)` for `m = 4..14` agree with the table (`ν = 1,3,7,15,15,15,15,143,399,399,399`,
closeness `4,5,6,10,10,10,10,11,14,14,14`, bits `7,19,44,93,…,880,2454`); least `L`: `ν=1: 30`, `ν=3: 109685`,
`ν=7: 419119864270` exactly as stated; `ν = 15`: `L` has 91 bits, `ν = 143`: 879 bits (stated "≈2^91", "≈2^879";
precisely `2^90 ≤ L < 2^91`, `2^878 ≤ L < 2^879` — fine as orders of magnitude). `ν = 399` not replayed.

## 4. Comp 3.1 / Cor 3.2 / Comp 3.4

* Grid arithmetic: `2^{L−4}7^b ≤ 2^{28}` gives exactly `L_max(b) = 32,29,26,23,20,17,15,12,9` for `b = 0..8`
  (none for `b ≥ 9` as `L ≥ 7`) — 26+23+20+17+14+11+9+6+3 = 129 cells ✔ (the replay's `28.01` tolerance changes no
  cell). The author's `/tmp/t7` has 129 `lb` files and 129 completion records.
* Table: counts sum to 67 ✔; every margin `t_min − max` re-computed ✔; Obs 3.3 ("≥ 4 for `L ≥ 16`, ≥ 10 for
  `L ≥ 28`") ✔; consistent with TYPEI4 Comp 3.4 on `L ≤ 26` ✔. 62 distinct `(L,b,{F,e})` in the lb files ✔.
* Independent height-bounded check: direct divisor enumeration (`ck ≤ 4·10^5`) finds 9 distinct divisor pairs in
  cells `(11,0),(14,0),(16,0),(18,0),(21,0),(27,0)`; all 9 are in the author's lists, closenesses agree.
* Second engine (`review_typei4_jsearch.c`, R89, run by me): see §4a for the cells re-run.
* §4 heuristic: `Σ 2^{5−t_min} = 0.593` over the 67 certificates ✔, `L ≥ 27` part `0.0089` (31 certificates) ✔,
  tail `10·2·Σ_{j≥17}2^{3−j} = 2.4·10^{−3}` ✔. Hensel remark: the derivative `32c'X²P_1−1` is odd ✔ (local only; the
  label Assessment is right).

MINOR m4 (bookkeeping, repaired below after my re-runs). Comp 3.4's list of single-engine cells is incomplete:
(i) TYPEI4 Cor 3.5 already flagged `L = 7,8, b = 7` and `L = 9,10, b = 6,7` as single-engine (R89's `jsearch` covered
`L ≤ 8, b ≤ 6` and `L ≤ 10, b ≤ 5` only); (ii) `b = 8, L = 7–9` are **new** grid cells (TYPEI4 had `b ≤ 7`) and are
missing from both the "new relative to TYPEI4" list of Cor 3.2 and the single-engine list of Comp 3.4.

### 4a. Second-engine re-runs by R109 (`review_typei4_jsearch.c`, `gcc -O2`, `ulimit -v 8000000`)

Compared with the author's table (all these cells empty except `(14,3)`):

| cells | result | time |
|---|---|---|
| `(14,3)` | 1 hit: `c'=5, k'=226697, F=281104279, e=49335587512359`, `v_2(F+9)=5`, `v_2(e+9)=4` — = table row | 2 s |
| `b=2`: `L=19,20,21,24` | 0 hits each | 9–540 s |
| `b=3`: `L=18,19` | 0 | 37 s, 2.3 min |
| `b=4`: `L=11–15` | 0 | ≤ 1 min |
| `b=5`: `L=11,12,13` | 0 | ≤ 1 min |
| `b=6`: `L=11,12` | 0 | 1.5, 3.7 min |
| `b=7`: `L=11` | 0 | 15 min |

All agree with Comp 3.1 / Cor 3.2.
