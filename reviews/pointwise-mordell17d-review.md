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
| Remark 2.4 (descent identity) | SOUND-AFTER-REPAIRS (m5: missing hypothesis 17 ∤ b; simpler proof) |
| §4 constants 4.969 / 22.83 / 40.24 | SOUND (recomputed) |

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
