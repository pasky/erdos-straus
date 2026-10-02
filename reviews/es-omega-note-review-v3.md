# Referee report: paper/es-omega-note.tex v3 (side-agent/omega-gpair @ 9eb1d03)

Hostile journal-referee pass. Checked against POINTWISE_OMEGA3 / OMEGA2 /
OMEGA at the same commit. Sections are written and committed one by one.

## §0 Repairs from review-2 (POINTWISE_OMEGA3 review-2) — APPLIED

`git diff bbe13d0 9eb1d03 -- POINTWISE_OMEGA2.md POINTWISE_OMEGA3.md`:
* D1 (two definitions of t): Setting 3.0 now refers to `t(Ŝ)` under
  *Constants*. ✓
* D2 (level-2 error budget): `L_2` is now least with
  `4^{L_2+1}≥200k𝔐_3e^{Λ_2+3Ŝ_{≥2}}`, with `Λ_2:=16(S_1+δH_2)+16e^{98}S_2`,
  so every level contributes `≤P(all)/(100k)`. ✓ (Check: induced level-2
  singles `≤δ|P_i|≤δH_2`, degrees ≤δ, so Lemma 2.1 with z=16 gives Λ_2. ✓)
* D3 (Ω(r)≤k−1): Thm 5.2's proof now applies Thm 5.1 with `k':=max(k−1,3)`
  levels and `|𝓑|≤(k−1)S*/c_{k'}`. ✓
* 2a (fixed-slot encoding) and 2b (simplicity not needed) added to O2
  Lemma 10.2's proof. ✓ Additionally merged identical induced events in
  Thm 5.1 (harmless; consistent with 2b).
