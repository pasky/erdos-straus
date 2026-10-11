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
