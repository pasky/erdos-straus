# Referee report R106 (round 3) on `paper/es-coverings-note.tex` — O106 additions

Scope: the O106 additions (branch `side-agent/coverings-note-v3`, commits bd24928..8b493e6): §4.6 TYPEI6 material
(Prop 4.17, regime-(v) inequality, Thm 4.18, Comp 4.19), §5 MORDELL13C (Thm 5.2, witness-engine counts, Comp 5.6
extension, (2,2)-cell data), §6 MORDELL17B/17C (D_P(11), D_P(13), ρ₁, Thm 6.7, Q large-c bound, discrete-log Assessment),
abstract / intro / problems. Each statement compared with the source `.md` and its review. From-scratch scripts:
`scripts/review_r106_*.py`. Repairs applied directly to the tex, marked `(R106 repair)` in comments.

## §6 (MORDELL17B / 17C)

Script: `scripts/review_r106_thm67.py` (mpmath, 40 digits; independent of `m17b_tail.py` / `m17c_tail_cum.py`).

| claim | verdict |
|---|---|
| D_P(11)=836, D_P(13)=1463, two engines, identical sets | SOUND (matches 17B Comp 2.2 after R93 m1; certified label correct) |
| ρ₁ = 16344335/24137569 = 0.677132… (certified) | SOUND (value as in 17B §3, reproduced in R93) |
| "each (P)-datum adds ≤ 2 boxes of measure 17^{(1−K)/2}, (Q) ≤ 2 of 17^{1−k}" | SOUND (17B Lemma 1.1, NB ≤ 2D) |
| Thm 6.7 (proved reduction) | SOUND. Abel summation re-derived (boundary term C·17^{1/2}·17^{(θ−1/2)K₁} → 0 because θ < 1/2; identity checked numerically on random data). Factor 32/17 = 2·16/17 correct. T_Q = 2Σ_{k≥9}17^{3k/5+1−k} = 1.410566·10⁻³ < 1.411·10⁻³. |
| C ≤ 1.497 at θ = 2/5 (cumulative) | SOUND: threshold 1.4979075 (with 1.411·10⁻³) / 1.4979085 (exact T_Q); 1.497 passes, 1.498 fails. Floor rounding correct. |
| pointwise constant 1.409 | SOUND: threshold 1.4097953; 1.409 passes, 1.41 fails (agrees with R93 M1 repair). |
| D_P(13)/17^{5.2} ≈ 6·10⁻⁴ | SOUND (5.85·10⁻⁴). |
| Conj 4.2 tail "≤ 4.2·10⁻³" | MINOR imprecision (m1 below): true only from K ≥ 15 with base ρ₂ (4.17·10⁻³); in the K ≥ 13 / ρ₁ framework of Thm 6.7 with D_P(13)=1463 exact it is 4.29·10⁻³. |
| Q large-c bound, cost 4.3·10⁻³ (proved) | SOUND (17C Lemma 2.1(iv), Cor 2.2; recomputed 4.2254·10⁻³). |
| Discrete-log Assessment additions | SOUND (class mod lcm(2, ord) PROVED as in 17C §4; E_∞ figures, median 0.05B, max ≈ B, two engines: as in 17C §4 after R98b m5; ET-cover sentence is an Assessment with an unproved premise in the source, "appears" is adequate). |
| Abstract / intro wording of Thm 6.7 | MINOR (m2): "ET's exponent for Type I" hides that the Q-hypothesis is D_Q(k) ≤ 17^{3k/5} with constant 1 and no o(1); abstract omits that the 1.497 bound is cumulative. |

## §5 (MORDELL13C)

Script: `scripts/review_r106_tree13.py` (from scratch: own ET coordinate formulas from the note's tables, exact
Fractions; partition re-derived at every split; open-leaf modulus divisibility; unit-normalised Haar mass).
Result: 171953 leaves = 136494 covered + **35459 open**; 0 identity/positivity/integrality failures (checked at
n = x, x+L, x+7L of every covered leaf, plus L ≡ 0 mod M and x ≡ r mod M); 0 partition failures; every open modulus
divides 2⁴3²5²7²·11·13·∏_{17≤ℓ≤83}ℓ; open mass **8.4241·10⁻⁵** of the six roots; per-root open counts 13986, 18070,
873, 455, 871, 1204 (as in the source). Covered leaves use 2140 distinct ET parameter triples (2188 distinct residue
classes (M, r), since I2/I3 triples can give several residues); max modulus 998844 ≤ 10⁶.

| claim | verdict |
|---|---|
| Thm 5.2 (proved by finite computation) | SOUND (reproduced; "no prime in omitted non-unit children" is the R100 repair, correct: q ≤ 83 < 112561). Label carries the dependence on Thm 4.x(b) via the proof's first line — adequate. |
| "three independent checkers (two by the author …)" | MINOR (m3): the second author checker `m13c_review_tree.py` wraps the R80 *reviewer* engine; "two by the author" is slightly generous but harmless. Not repaired. |
| witness-engine 1399 / 1499 / 1412 (evidence) | SOUND (13C §2; level L = 69604975440 = the modulus quoted just above in the note, checked). |
| "No root class closes"; open mass decays like a power (evidence) | SOUND. |
| Comp 5.6 extension (II3/I3/I1/II2 to 2·10⁹, I2/II1/I4 to 2·10⁸, one engine, caps vacuous) | SOUND-AFTER-REPAIRS (m4): matches 13C Comps 5.1/5.2 including the cap argument (v_q ≤ 9 after dropping a common factor). The source carries an R100 provenance caveat (logs do not record command line / start X0) which the note omits; one clause added. |
| "about five orders of magnitude further in e … now 2·10⁹" | SOUND (x* covered by II3 with e = 11999; 2·10⁹/1.2·10⁴ ≈ 1.7·10⁵). For the I2 side (f = 11999 vs 2·10⁸) it is four orders; the sentence says "in e", so correct as stated. |
| Comp 3.1 (2,2) cell at 11²13² exactly {2,57,79}×{15,28,54,132,145}, 15/143 (certified) | SOUND (13C Comp 3.1 + R100: 128 covered subcells confirmed independently; R100 also shows the N = 11⁴13⁴ run was unnecessary — not needed in the note). |
| "only 473761 is known to contain uncovered T-generic points for the T tested" (evidence) | SOUND (13C §3). |
