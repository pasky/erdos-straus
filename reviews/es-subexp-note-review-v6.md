# Referee report R77 — `paper/es-subexp-note.tex` v6 (branch `side-agent/subexp-paper-v6`)

Referee: R77 (hostile). Scope: everything new/changed in v6 per `AGENT_REPORT_O77.md` (C1–C7).
Base: merged `side-agent/subexp-paper-v6` (tip `ca58456`) into the referee branch.

## Compilation
`pdflatex` ×2 (+bibtex) in a scratch dir: 61 pp., 0 undefined references/citations, 0 overfull boxes,
no errors. **OK.**

## Per-claim verdicts (filled in incrementally)

### Lemma 12.3 (quantitative transfer) — SOUND
Re-derived case by case against the proof of Thm 6.1 (lines ≈1340–1440):
* Case 0: `S ≥ (1 − 1/400 − 1/200)μx/φ(Q)` (R₁ ≤ 1/400, middle sum ≤ 1/200). ≥ 1/3. ✓
* Exceptional, χ₁ not in support: middle sum ≤ min(u,1)/200 ≤ 1/200; same bound. ✓
* Case B: `1 − 1/2 − 1/200 − 1/400 = 0.4925 ≥ 1/3`. ✓
* Case A: `S ≥ 0.98λ'μx/φ(Q)`, `λ' ≥ min(u,1)/2`, `u ≥ 16(1−β₁) ≥ 2a` with
  `a = 8c₂⁻¹q₁^{-1/2}(log q₁)^{-2}` (q₁ ≥ 3 as χ₁ is a real primitive non-principal character, so Thm 5.x
  applies). Then `0.98·min(2a,1)/2 ≥ min(a,1)/3` in both sub-cases (2a ≤ 1: 0.98a ≥ a/3; 2a > 1: 0.49 ≥ 1/3). ✓
* "q₁ | Q ⇔ Case A": real primitive conductor is `2^e f'` (e ∈ {0,2,3}, f' odd squarefree) and 8 | Q, so
  `f₂ = 1 ⇔ q₁ | Q`. ✓ (the paper only states ⇐-direction in the parenthetical; both hold.)
* Counting step: terms with `B(p) > 0` satisfy `B(p) ≤ 1[W(p)>T] ≤ 1`, so each positive term ≤ log x;
  negative terms only help. ✓
The constant 8 in λ is conservative (16 would also work); harmless.
