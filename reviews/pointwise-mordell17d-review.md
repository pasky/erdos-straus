# R139 — hostile review of POINTWISE_MORDELL17D.md (O139)

Reviewer branch `side-agent/review-r17d`; author files merged from `side-agent/r17-sterile`.
From-scratch scripts: `scripts/review_r139_*.py`, `scripts/review_r139_*.c`. The author's document is not edited;
suggested repairs are marked "(R139 repair)".

## Summary verdicts (filled in claim by claim)

| claim | verdict |
|---|---|
| Lemma 1.1 (compactness) | SOUND |
| Comp 1.2 (C*(K₀) table) | SOUND (minor wording, m1, m2) |
| Comp 1.3 (least K₀ table) | SOUND (minor, m2) |
| Lemma 2.1 (membership = lattice condition) | SOUND |
| Lemma 2.2 (sizes) | SOUND (m3: "≈ (|p|+q)W/68" heuristic) |
| Lemma 2.3 (rays; mod-8 exclusion for −2/3) | SOUND (m4 wording) |
| §2 text after Lemma 2.3 (ray examples) | WRONG (M1, non-load-bearing) |
| Remark 2.4 (descent identity) | SOUND-AFTER-REPAIRS (m5: missing hypothesis 17 ∤ b; simpler proof) |
| Theorem 4.1 (localized criterion) | SOUND (m7 wording) |
| §4 constants 4.969 / 22.83 / 40.24 | SOUND (recomputed); m8 on the "×4.6 / ×8.1" reading |
| Conj. 4.2 + labels | SOUND; honest ("no unconditional sterile point") |

## Checks

**Lemma 1.1.** Re-derived. For fixed `L` there are finitely many P-data (`N = 17^{2L'−1}`, `L' ≤ L`, finitely many
ES solutions) and finitely many Q-data of level `≤ L`, and finitely many U/Q⁻¹-boxes; each box is a ball, hence
clopen; `C_5` is compact; nested nonempty compacta have nonempty intersection. Converse trivial. SOUND.

**Comp 1.2, 1.3, §4 table.** Recomputed independently (`scripts/review_r139_tables.py`, mpmath 50 digits, closed-form
geometric tails instead of truncated sums). All 27 entries of the 1.2 table, all 20 entries of the 1.3 table, the
pointwise constant 2.4845 (M17B, K ≥ 15, ρ₂) and all 12 entries of the §4 table agree with the author to the printed
precision. `T_Q(9) = 1.41057·10⁻³`, `T_Q^R(11) = 1.462·10⁻⁴`. Global box-unit constant `4.96903 = 2 × 2.48451` ✓.
Formulas checked against M17C Lemma 1.1 (weights `17^{(1−K)/2}`, Abel factor `16/17`, `NB ≤ 2D`) and against Thm 4.1
(`17^{L*−ℓ}·C·17^{θK}·17^{1−L*} = C·17^{θK+(1−K)/2}` with `ℓ = (K+1)/2`; Q: `2·17^{3k/5+1−k}`) ✓.

**Lemma 2.1.** Re-derived. (i) `4abcd = a+b+Nc`; `17 | b ⇒ 17 | a ⇒ f ≡ −1`, box `≡ 1 (17)`, outside `C_5` ✓.
Else `bf = a + Nc ≡ a (mod W)` as `2L−1 ≥ L` ✓. (ii) `4abd = eF+1` ⇒ `4a²d·b ≡ a`, `17 ∤ ab` ✓; second box
`−4b²d ≡ −1/(4a²d)`, consistent with the engine's `w ∈ {−u, −1/u}` ✓. Both Σ^II and Σ^I are symmetric in `(a,b)` ✓.
Checked by brute force (`scripts/review_r139_lemmas.py`): all ordered P-points for K = 1, 3, 5 (4, 64, 242 =
2·D_P ✓), random `u = −p/q ∈ C_5` (|p|, q ≤ 60): box membership ⇔ `17∤b ∧ qa ≡ pb (W)`, 0 failures.

**Lemma 2.2.** Re-derived (i) `4abd = N+e`, `e ≤ a+b`; (ii) needs `c ≤ a+b ≤ 2b` ✓ (`c = (a+b)/e`); (iii) ✓. Brute
check: (i) on all P-points K ≤ 5; (ii) on all Q-points k = 1, 3 enumerated with the *weaker* independent bound
`4acd ≤ 2F + c` (from `a ≤ b` only), 2 and 73 points (= D_Q(1), D_Q(3)) ✓, 0 violations.

**Lemma 2.3.** Re-derived. P: a prime `ℓ ≠ 5` dividing `e` divides `λ`, hence `N = 24λ²d − e`, so `ℓ = 17`, so
`17 | b`, excluded *as a covering datum* by 2.1(i); `e = 5^j ≡ 1,5 (8)` vs `e ≡ −N ≡ −1 (8)` ✓. Q: `ℓ | λ ⇒ ℓ | 1`;
`e + 1 ≡ 2, 6 (8)` ✓. Note `ℓ ∈ {2,3}` is covered by the same argument (`ℓ | N`). No ray data in the brute-forced
lists ✓.

**Remark 2.4.** Identity verified symbolically by the author's expansion (re-done: difference `= (qa−pb)² − 17z²N
= z²W² − 17z²N = 0` using `4abd = N+e`, `c·e = a+b`) and numerically on all P-points K ≤ 5 with random lifts
`p ≡ qa/b (W)`, `q ≤ 10⁶` (0 failures); the parenthetical (`X·N = ab(p²f* + q²f − 2pq)`, `f | 4c²dp² + 17x²`)
checked on 1530 random instances (`scripts/review_r139_paren.py`), 0 failures.

**§3 engines — code audit of the author's engines.** `m17d_pointP.c`: Part A/B split re-derived (`a > A ⇒ 4a−1 ≥ 4A+3
⇒ 4b−1 ≤ ⌊(4N+1)/(4A+3)⌋`) ✓; `ACUT = ⌊W/√68⌋` ✓; Part B bump `a += ((A−a)/W+1)W` gives the least class member `> A` ✓;
`e` unique because `4ab > a+b` ✓; skipping `17 | a` is valid (`a ≡ −ub`, `17∤b`) ✓. 128-bit: `N ≤ 17^19 < 2^79`,
`4ab ≤ 4N + O(N)`, `N % m`, `(N+e)/m` never overflow; the `4abcd = a+b+Nc` recheck wraps mod 2^128 at L ≥ 9 but is
an identity mod 2^128, so it can only abort, never drop a hit; box test reduces mod W first ✓. `m17d_pointQ.c`: loop
A/D split by `min(a,d) ≤ H` with `a > H` in loop D ✓ (a datum with `a > H` has `d < (F+1)/(2a) ≤ H`); `d`, `a` are
least residues because `ad ≤ (F+1)/2 < F` ✓; `gcd(F, 4ad) = 1` ✓; the fixed-derivative Hensel iteration gains one
digit per step and is asserted (`r² ≡ y`) ✓; two-candidate divisor rule (M17C Lemma 2.1(iv), re-derived: `s² > t`,
`gcd(t,s) = 1`) ✓; `t ≤ 2aF < 2^127` ✓. No defect found.

**§3 independent engines (R139).** `scripts/review_r139_pengine.c`: different split (by `min(a,b) ≤ B0 =
⌊(⌊√(4N+1)⌋+1)/4⌋`, which follows from `(4m−1)² ≤ (4a−1)(4b−1) ≤ 4N+1`), class representatives updated additively,
all of `a, b` in u128. `scripts/review_r139_qengine.c`: own Hensel (Newton with recomputed derivative), own
divisor-candidate code. Validation (`review_r139_pvalidate.py`, `review_r139_qvalidate.py`): P — exact *set*
equality with own brute force (L ≤ 3) and with `data/m17b/p{K}.txt` (L = 4–7) at 198 in-cell box centres + 105
random in-cell residues (+25 L=1 random), 328 tests, 0 mismatches (run for both the u64 and u128 versions).
Q — 224 tests (k = 1, 3: set equality with own brute force; k = 5, 7: hit ⇔ listed box, vs m17_enum lists),
0 mismatches.

Results for `u = 5` and `u = −2/3` (all hits = 0):
* P, L = 7: 1.98·10⁸ candidates; L = 8: 3.905·10⁹ (u = 5) and 4.210·10⁹ (u = −2/3) candidates, 0 hits
  (author: 3.9·10⁹ / 4.2·10⁹ ✓ — same search space, different traversal).
* P, L = 9 (full, reviewer engine, < 10 min per point): 7.569·10¹⁰ (u = 5) and 8.087·10¹⁰ (u = −2/3) candidates,
  0 hits (author: 7.6·10¹⁰ / 8.1·10¹⁰ ✓).
* Q, k = 9, 11, 13, 15: 0 hits; pair counts 6, 26, 29, 51 (u = 5) and 34, 11, 22, 28 (u = −2/3) — identical to the
  author's (k = 15: ≈ 35 min per point with the reviewer's slower i128 Euclid).
* Levels below the new range (reviewer re-run, not claimed as new by the author): P, L = 1–7 and Q, k = 1, 3, 5, 7
  — 0 hits for both points, consistent with the cell-wide certified lists.

**Ray examples after Lemma 2.3 (checked with the R139 engines).** The coverings of the four quoted examples are:
`−9/5`: P level 2, `(a,b,c,d) = (410,3,59,1)`, `qa − pb = 2023 = 7W` (z = 7); `−11/8`: P level 2, `(182,1,1,7)`,
z = 5; `11/9`: P level 2, `(1,78,1,16)`, `(2,156,2,4)`, `(4,312,4,1)` — `u > 0`, so by Lemma 2.3(i) it *cannot* be on a
ray; `−7/2`: Q level 5, `(a,b,c,d) = (1,202837,2,177483)` (not proportional to (7,2)). No datum of `p1–p13` lies on the
ray of any of these points (`a/b` reduced ∉ {9/5, 11/8, 7/2, 2/3, 11/9}, both orders). So none of the examples is a ray
covering; all are `z ≠ 0` coverings. See M1.

**Theorem 4.1.** Re-derived. Balls in `ℤ_17` are nested or disjoint; a box of level `≤ L*` meeting `R` contains `R ∋ u₀`;
a box of level `> L*` meeting `R` lies in `R`. U-boxes meeting `C_5` lie in P-boxes (M17 Lemma 5.2), and a P-box
containing a U-box of level `ℓ` has level `≤ ℓ`; Q⁻¹-boxes are Q-boxes of the same level. Hence "u₀ in no P/Q-box of level
`≤ L*`" (what Comp 3.4 certifies) is the right hypothesis, and countable subadditivity gives the bound. `R ⊂ C_5` for
`L* ≥ 1` ✓. Normalisation: `μ(R) = 17^{−L*}`, box of level ℓ: `17^{−ℓ}` ✓; under `(H_θ^R)` the P term is
`C·17^{θK+(1−K)/2}` and the Q term `2·17^{3k/5+1−k}` (k ≥ L*+1 odd), matching `m17d_local_tail.py` and the reviewer's
closed forms. Applied with L* = 10 the hypothesis is supplied by Comp 3.4 (P ≤ 10, Q ≤ 15 ⊇ Q ≤ 10) ✓. The criterion
is conditional on `(H_θ^R)`, which is unproved; label CONDITIONAL in §4 is honest. No circularity.

**Conjecture 4.2 / evidence.** Extrapolating M17B's increments 7.0·10⁻⁵, 1.1·10⁻⁵ (ratio ≈ 6.4/level) gives
`Σ_{ℓ>10} ≈ 7.7·10⁻⁹`, consistent with "≈ 10⁻⁸". The document correctly calls Comp 3.4 consistency evidence only (a
random point survives level ≤ 7 with probability `ρ₂ ≈ 0.68`). Labels: §0 / report state "No unconditional sterile
point" ✓; nothing is labelled PROVED that is not.

## Defects

**M1 (MAJOR, non-load-bearing; §2, the paragraph after the proof of Lemma 2.3).** "Rational points with an admissible
ray are covered (e.g. `−9/5`, `−11/8`, `11/9` are covered at level 2, `−7/2` at level 5)" is false as an illustration:
all four examples are covered by `z ≠ 0` data (list above), and `11/9 > 0` has no rays at all by the document's own
Lemma 2.3(i). `m17d_points.py` only tests box membership and never distinguishes rays from `z ≠ 0` data, so it cannot
support the sentence. This also weakens the motivation "Lemma 2.3 is what makes `−2/3` a good candidate": at low levels
the small-height rationals are knocked out by the *non-resonant* `z ≠ 0` families, exactly the ones §4/Conj. 4.2 say
cannot be controlled. *(R139 repair)* Replace by: "Every rational box centre `−a/b` is trivially on a ray, so rays
cover exactly the rational centres of boxes; the small-height rationals found covered by `m17d_points.py` (e.g.
`−9/5`, `−11/8`, `11/9` at level 2, `−7/2` at Q-level 5) are all covered by `z ≠ 0` data. Lemma 2.3 removes only
the resonant obstruction for `−2/3`; the `z ≠ 0` families remain the whole difficulty."

**m1 (MINOR; Comp 1.2).** The "ceilings" argument holds for adding exact *P* levels with the Q tail kept from
`k = 9` (as in the computation). If exact Q levels were also added, `T_Q` shrinks while `ρ` shrinks by the measure
actually removed, which can be smaller than the removed part of the hypothetical `T_Q`; the effect is ≤ `T_Q(9) =
1.4·10⁻³` relative to `ρ₂ ≈ 0.677` (≤ 0.21 %), so the table is a ceiling up to that. Also several entries are rounded
to nearest (2.64 vs exact 2.6398, 8.199 vs 8.1988, 14.45 vs 14.449), while the companion tables are floor-rounded.
*(R139 repair)* Add "(Q tail kept from k = 9; entries rounded to 4 significant digits, not floored)".

**m2 (MINOR; Comp 1.3).** The search starts at `K₀ = 15`, so the entry 15 at `(0.40, 0, A = 1)` means "≤ 15".
*(R139 repair)* footnote "15 = search floor".

**m3 (MINOR; after Lemma 2.2).** `min(a,b) ≤ (|p|+q)(N+a+b)/(4W) ≈ (|p|+q)·W/68` drops `a + b`, which can be `≍ N`
when `min(a,b)` is tiny; the correct reading is "`min(a,b) ≤ (|p|+q)(N + 2max)/(4W)`", harmless. *(R139 repair)*
replace "≈" by the exact bound or "`≲` when `max(a,b) = o(N)`".

**m4 (MINOR; Lemma 2.3(ii)).** "No P-datum ... lies on the ray": the argument excludes ray data with `17 ∤ λ`; ray data
with `17 | λ` are not excluded, only shown irrelevant (their box is `≡ 1 (17)`). *(R139 repair)* "no P-datum on the
ray has a box containing `u`".

**m5 (MINOR; Remark 2.4).** The divisibility part is stated for every N-point, but its proof (`a | N·X` ⇒ `a | X`)
needs `17 ∤ a` (equivalently `17 ∤ b`); `p1–p13` contain no datum with `17 | ab`, so the author's 6632-pair check does
not test that case (nor could the reviewer's). Simpler and complete proof under `17 ∤ b`: from `4abd = N + e`, `gcd(e, ab) | N`, and
`17 ∤ ab`, so `gcd(e, ab) = 1` and `e | (p+q)² + 68dz²` follows directly from the identity (then `ab | X` too).
*(R139 repair)* add the hypothesis `17 ∤ b` and this one-line proof.

**m6 (MINOR; §3 Validation 3.3 vs Replay).** Text says 716 test points; the Replay comment says 704. *(R139 repair)*
update the Replay comment to 716.

**m7 (MINOR; Theorem 4.1, last sentence of the statement).** "Hence (M17 Cor. 4.2) no finite set of ET Prop. 1.9
classes covers …" reads as an unconditional conclusion. *(R139 repair)* "Hence, *if the displayed sum is < 1 for some
admissible `u₀, L*`*, (M17 Cor. 4.2) …".

**m8 (MINOR; §4 Assessment (a)).** "The admissible constant at θ = 0.4 grows ×4.6 (L* = 9) resp. ×8.1 (L* = 10)" compares
a K ≥ 19/21 constant with a K ≥ 15 one. Most of the gain is the later start, not localisation: the *global* box-unit
constant with hypothesis from K ≥ 19 resp. K ≥ 21 (base ρ₂) would be 15.43 resp. 27.20 (reviewer computation), so the
localisation itself contributes ×1.48 (= 22.83/15.43 = 40.24/27.20 ≈ 1/ρ₂: base 1 instead of ρ₂, plus the tiny local
T_Q). That is exactly the document's point (pointwise exact data reach 2–3 levels further), but say so.
*(R139 repair)* add "(of which ×1/ρ₂ ≈ 1.48 is the fresh base; the rest is the later start K ≥ 2L*+1)".
