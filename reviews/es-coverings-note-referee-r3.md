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

## §4.6 (TYPEI6; TYPEI5 context)

TYPEI5 material (Prop 4.15 = minunit, Thm 4.16 = L710) is unchanged since round 2 and was not re-refereed; only its
interface with the new text was checked.

| claim | verdict |
|---|---|
| Prop 4.17 (no norm-one polynomial unit, L ≥ 7; proved, sketch) | SOUND. Re-derived: units of ℚ[δ][√d] are ℚ^×η^ℤ via deg_±; N(η) = −c_oT < 0 forces even exponent; for L ≥ 7, d ≡ 1 (8), c_oδ ± √d ∈ ℤ₂ have sum of valuation 1 and product of valuation L−4, so valuations 1 and L−5; v₂(ε_*^n) = n(6−L), n(L−6). L = 5, 6 integral (R99 D6). c_o-indeterminate variant: same element (source). |
| Schinzel period remark (cited, not used) | SOUND: Δ = B² − 4A²C = −4c_o³TN², criterion Δ ∣ 4 gcd(2A²,B)² ⟺ T ∣ 4c_o gcd(N,δ₀)² ⟺ T ≤ 4 ⟺ L ≤ 6 (c_o, δ₀ odd). Original Schinzel 1961 not accessed (as in R99; via van der Poorten); the note says so. |
| Regime-(v) identity and Y > 64c_o⁴δ⁸/T⁴; unit > 128c_o⁴δ⁸/T⁴ − 1 (proved) | SOUND (TYPEI6 Lemma 3.1(b), with R99 D2: the bound is on A = 2Y − 1, and A + 8k_o√d > A). Notation check: Y = 16PX² with X = k', u = 7^b matches eq. (pell); A = 2·7^aQ_1·49^b + 1 = 2Y − 1. ✓ |
| "regimes with σ < 0 … are the units below this size" | SOUND as interpretation (contrapositive of Lemma 3.1); λ < 0 has Δ < 0 so σ < 0 there too. But **"regime (v)" is never defined in the note** (MINOR m5). |
| "typical unit exp(d^{1/2+o(1)}) ⇒ generic case" | SOUND as Assessment. |
| Thm 4.18 (conditional on abc; finiteness per level) | SOUND-AFTER-REPAIRS. Radical bound re-derived: rad(Y·Qu²) ≤ 2·7·Q_1·P·X = 3.5(d/7^a)√(Y/P). The "other regimes finite" step checked against TYPEI5 Prop 3.3: (i) λ = 0 impossible; (ii) λ < 0: 7^a∣λ∣j < T²/8 and u bounded in (a,λ,j) — finite per L; (iii) finite explicit; (iv) Δ = 2Tj: T²(T−4) = 16·7^{a+b}λ gives finitely many (a,b,λ), then j = u, y = u(T/2 − 1) and P_1 ∣ Tu − y bound everything — finite per L (I re-derived this last step; the source only states (iv) for (a,b,λ)). Case A (2y > T7^b) at general L: TYPEI6 §3 (R99 D1 repair, u < T³) — correctly cited. Hidden hypothesis: the exponent bookkeeping needs ε < 1/7 (P-exponent (1−7ε)/2 > 0); the sketch's "≪" hides this (MINOR m7). |
| "explicit abc forms do not give emptiness" (Assessment) | SOUND (TYPEI6 Rem (ii) after R99 D4). |
| Comp 4.19 (certified; L = 7–10, b ≤ 15, any height) | SOUND. Size bound P(64c_o⁴δ⁸ − T⁴) < 49^b d T⁴ follows from Y = Qu² + 1, Q = d/P. Engine scope statement matches TYPEI6 Comp 4.1/Cor 4.2 + R99 D7 (two engines except (9,15), (10,14), (10,15)). Typo-level: "for all (L,b) with L ≤ 10" should be 7 ≤ L ≤ 10 (m6). The combination with Thm 4.16 is correct (case A by (a), regimes (ii)–(iv) by (b), regime (v) by the computation). Thm 4.16(c) "v_7(k) ≥ 8" is now superseded, no pointer (m8). |
| "needs v_7(k) ≥ 16 and c_oδ > 10⁶" | SOUND (Comp 4.19 + Thm 4.16(d)). |
| naive model < 10⁻¹¹ (evidence) | SOUND as EVIDENCE: per-b predictions at b = 15 are ≈ 10⁻¹², decaying ≥ 3× per step, so the four-level tail is ≲ 2·10⁻¹² (extrapolation). |
| Abstract / intro / Problem 2 wording | SOUND. |

## Defects (no FATAL, no MAJOR)

All repairs applied in `paper/es-coverings-note.tex`, each marked "(R106 repair)" (in text or as a `%` comment).

* **m1 (MINOR, §6 after Thm 6.7).** "Conj 4.2 … would give a tail ≤ 4.2·10⁻³": true for the tail beyond (P)-level 7
  (base ρ₂, 4.17·10⁻³), not in the K ≥ 13 framework of Thm 6.7 (4.29·10⁻³ with D_P(13) = 1463 exact). *Repair:* both
  numbers stated with their base.
* **m2 (MINOR, abstract and intro r = 17 bullet).** "ET's exponent 2/5 with constant 1.497 would suffice" / "plus ET's
  exponent for Type I": the 1.497 is for the cumulative count, and the Q-hypothesis is D_Q(k) ≤ 17^{3k/5} with constant
  1 and no o(1). *Repair:* both stated.
* **m3 (MINOR, Thm 5.2 proof).** "two [checkers] by the author": the second wraps the R80 reviewer engine. Not repaired
  (harmless).
* **m4 (MINOR, Comp 5.6 extension).** The PM13C §5 provenance caveat (run logs lack command lines; R100) was dropped.
  *Repair:* one clause added.
* **m5 (MINOR, §4.6).** "regime (v)" is used four times but never defined in the note. *Repair:* defined at its first
  natural place (after Thm 4.16: λ ≥ 1, σ ≥ 1, regime (v) of TYPEI5 Prop 3.3).
* **m6 (typo, Comp 4.19).** "L ≤ 10" → "7 ≤ L ≤ 10" (review engine scope).
* **m7 (MINOR, Thm 4.18 sketch, hidden hypothesis).** The finiteness needs abc with a fixed ε < 1/7 (otherwise the
  P-exponent (1−7ε)/2 is not positive). *Repair:* stated in the sketch.
* **m8 (MINOR, Thm 4.16(c)).** "v_7(k) ≥ 8" is superseded by Comp 4.19 (≥ 16) without a pointer. *Repair:* pointer.

Build after repairs: two pdflatex passes, 29 pp, 0 overfull boxes, 0 LaTeX warnings (no undefined refs/cites); the
pre-existing underfull hbox (Prop 6.2) and underfull vboxes at page breaks remain.

## Recommendation

**Accept the O106 additions with the minor repairs above (applied).** Every new number I could check was reproduced
from scratch: Thm 6.7 thresholds (1.49791 cumulative / 1.40980 pointwise; 1.497 and 1.409 are correct floor roundings,
1.498 and 1.41 fail), T_Q, the 17C Cor 2.2 cost, D_P(13)/17^{5.2}; the MORDELL13C tree (35459 open, 136494 covered,
2140 ET triples, mass 8.4241·10⁻⁵, open moduli divide the stated product, all covered-leaf identities). Labels match
the sources after their reviews (R93, R98b, R99, R100). Not re-checked: the large engine runs themselves (Comp 4.19,
Comp 5.6 extension, D_P(13)), which rest on the cited reviews; TYPEI5 material (round 2). Schinzel 1961 not accessed.
