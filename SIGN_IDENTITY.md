# SIGN_IDENTITY — exact identities for the ES sign N₋(n) (task O205, wave Y-b)

Status: in progress (O205). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on CHI_FLIP.md (χ = −ε₂(Q_w)), CONSTRUCTIVE_ES.md (Eichler orders of level 2), MODEL_SPECIFIC.md Thm 3.1,
KUDLA_ES/DIFF_DEEP/LDP_DEEP ((J)13, (J)16–18), GROWING_IDENTITIES (J)10, EXACT_FORMULA (I)5, STRONG_APPROX_ES Thm 9.1.
Scripts `scripts/si_*`.

Notation (as CHI_FLIP). Word w = (t, u, v) ∈ ℤ³_{≥1}, K(w) = tuv − u − v = n odd; A = tu − 1, A* = tv − 1,
AA* = tn + 1; χ(w) = (−A/n); G_w = [[v, −1, 0], [−1, t, −1], [0, −1, u]], det n. X_n = all positive words.
N_±(n) = #{w ∈ X_n : χ(w) = ±1}, S(n) = N₊ − N₋. SQ₅ (CONJECTURE): N₋(n) > 0 ⟺ n odd non-square, n ≠ 105.
Fingerprints: N₋(m²) = 0; N₋(105) = 0; N₊(n) = 0 at 38 values n ≡ 3 (4) ≤ 10⁶ (15, 311, 455, 495, …).

## 0. Iteration log
(I1) Setup: enumerator `scripts/si_census.c` with several weightings (§1).
