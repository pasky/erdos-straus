# Referee report R98 — es-coverings-note, post-referee additions (round 2)

Scope: §4.6 (O91, from PT4 = POINTWISE_TYPEI4.md), Lemma 3.6 paragraph, TYPEI5 (not yet in paper),
§5.3 (O96, from PM13B = POINTWISE_MORDELL13B.md: Prop 5.4, Comp 5.5, Conj 5.6), abstract/intro/open problems;
POINTWISE_MORDELL13B.md §5 post-review extension (x** to e ≤ 1e9).

Status: IN PROGRESS.

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


## Defects

## Repairs applied
