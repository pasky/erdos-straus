# R94 — hostile review B of EXCEPTIONAL_MN.md (task O94)

Reviewer B, branch `side-agent/review-emn-b` (author files merged from `side-agent/mn-threequarter`).
Scope: EXCEPTIONAL_MN.md — Lemma 1.1–1.3, Lemma 2.1, Prop. 3.1, Cor. 3.2, Lemma 4.1–4.2, Thm 4.3,
Theorem A, Theorem B, Cor. C, Cor. D, the Pomerance–Weingartner (PW) comparison, §§7–8.
The note `paper/es-threequarter-note.tex` and EXCEPTIONAL_SHORT.md are taken as given (reviewed
elsewhere); I check only the 4 → m transfer and the new claims. PW = arXiv:2511.16817v2,
read in `sources/pw.txt` (full text available locally). Vaughan 1970: **not accessible** (see
`sources/vaughan-1970-access-log.md`); only secondary quotations checked.

## Verdict summary

| claim | verdict |
|---|---|
| Lemma 1.1 (identity `kℓ+1 = m·uvw` ⇒ class m-representable) | SOUND (re-derived; exhaustive check) |
| Def. 1.2 / Lemma 1.3 (atom family, dedup, CRT independence) | SOUND |
| §1.4 (only uses of `4` in the note; Jacobi obstruction irrelevant) | SOUND, one MINOR omission (simplified route, D1) |
| Lemma 2.1 (h_m) | SOUND (re-derived; numerics 0 failures incl. primorial m) |
| Prop. 3.1 (pruned prime slice, BV uniform in m ≤ t³, modulus muv) | SOUND (BV step written out below) |
| Cor. 3.2 (fibre mass `≍ t³/m` on reduced fibres, `≪ t³/m` on all) | SOUND; independently confirmed numerically (EVIDENCE) |
| Lemma 4.1 (void with absolute η = 1/4, y = max(2,Bs)) | SOUND |
| Lemma 4.2, Thm 4.3 (moments, Bonferroni, ledger `e^{O(ts)}`) | SOUND |
| Theorem A (`E_m(I) ≤ CH exp(−c (log H)^{3/4} m^{−1/4})`, absolute c, C) | SOUND (rel. note + SHORT) |
| m^{−1/4} bookkeeping / "no φ(m), log m loss" | SOUND |
| Theorem B, Cor. C | SOUND (rel. SHORT); caveat on prime q is correct |
| PW Thm 1.3 comparison ("beats for every m in their range") | SOUND-AFTER-REPAIRS (D2: asymptotic, not literal) |
| Cor. D (density transition `log n = m^{1/3+o(1)}`) | SOUND-AFTER-REPAIRS (D3: cite PW's *proof* range, not Thm 3.1's statement) |
| §8 literature (Vaughan "for each m") | GAP in citation only (D4) |

No FATAL or MAJOR defect found. The transfer really is `t³ → t³/m`: the two m-sensitive
factors (`1/φ(muv)` from the prime progression and `h_m ≍ (φ(m)/m) log K` from the multiplier
set) cancel to `1/m` with absolute constants, and every other step is m-blind.
