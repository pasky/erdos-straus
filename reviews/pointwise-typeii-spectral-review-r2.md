# R128b — hostile review of O128 round 2 (`POINTWISE_TYPEII_SPECTRAL.md` §§7–10, `AGENT_REPORT_O128b.md`)

Reviewer: R128b side agent (branch `side-agent/review-typeii-r2`), merged `side-agent/typeii-spectral` @ a6eb39ca.
From-scratch scripts: `scripts/review_r128b_*.py` (no author code reused). Per the brief, repairs are applied
directly in the author's document and marked "(R128b repair)".

## Summary verdicts

| Claim | Verdict |
|---|---|
| R128 D1–D8 repairs (§§0–6) | SOUND-AFTER-REPAIRS (D6 left one stale "slowly widening" in §0; fixed) |
| Prop 7.1 (Gram data, converse) | SOUND |
| Prop 7.2 (Pell form) + "unusually small units" remark | SOUND (identity); remark MINOR overreach |
| (filled in below as checked) | |

## Defects

(numbered as found)

- **E1 (MINOR, leftover of R128 D6)** §0 bullet "§5 (EVIDENCE …)": "normalised lower tail `R ≈ 0.28` and slowly
  widening". D6 asked to soften "widening"; §5 now says "flat to slowly decreasing" but §0 was not updated.
  Repair (applied): "flat to slowly decreasing".
- **E2 (MINOR, overreach in a PROVED section)** Prop 7.2, last sentence: "a small unit forces … near-maximal class
  number of ℚ(√D')". `T + 2c√D'` has size ≈ 4c√D' for *every* Pell solution with `y = 2c`; it is "small" only when
  c is small, and c ranges up to ≈ p/2 (Prop 8.1: `2cd − 1 ≤ p`). For c ≍ p it gives `log ε ≪ log p`-type bounds
  only via `D' ≥ dp`, i.e. nothing beyond `h ≫ √D' L(1,χ)/log(c√D')`; "near-maximal" also needs a lower bound for
  `L(1,χ)` (Siegel, ineffective) and the class-number formula is for the order `ℤ[√D']`, not the field.
  Repair (applied): label the remark Assessment and add "for c ≤ p^{o(1)}; the class number is that of the order
  ℤ[√D']".

## Claim-by-claim

### R128 D1–D8
Checked the text at each "(R128 repair Dk)" marker. D1 (§1), D2 (§1 table remark, §0), D3 (Prop 2.5), D4 (Lemma
6.1, §6(ii), §0), D5 (§3), D7, D8 (§4.4) are applied as requested. D6 applied in §5 but not in §0 (E1).

### Prop 7.1
Re-derived: `q(Q) = 16a²d² − 4f·de = 4d(4a²d − ef) = −4dp` (form 2: `ef − 4a²d = p`); `b(Q,S_c) = 2·4ad·2c − 4f·1
− 4·0·de = 4(4acd − f) = 4`; Gram (w.r.t. q) `[[−4dp, 4],[4, 4c²]]` ↔ binary form `4(−dp x² + xy + c²y²)`,
`disc T₀ = 1 + 4c²dp` ✓. Converse: `b = 4` ⇔ `A = cB − 1`; `A > 0` ⇒ `B ≥ 1` ⇒ `a = B/4d ≥ 1`; `q < 0, A > 0` ⇒
`C > 0` ⇒ `e ≥ 1`; then `b := ce − a = (cp + a)/(4acd − 1) ≥ 1` and `4abcd = a + b + pc` (direct). ✓
Verified from scratch (`review_r128b_lattice.py`) for all Type II quadruples of primes p < 300.

### Prop 7.2
`(T − 2cdm)(T + 2cdm) = f'f = 1 + 4c²dp` ⇒ `T² − 4c²(d²m² + dp) = 1` ✓. Converse: `s = (T+1)/2cd`,
`a = (s+m)/2`, `b = (s−m)/2 ≥ 1` by parity and `|m| < s`; `(4acd−1)(4bcd−1) = T² − 4c²d²m² = 1 + 4c²dp` ✓
(form 3 without the gcd condition, as stated). Verified numerically (same script). Remark: E2.
