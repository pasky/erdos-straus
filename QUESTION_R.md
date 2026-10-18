# QUESTION_R — thin-orbit local–global with a reciprocity obstruction (Rickards–Stange) as a model for ES (O267)

Status: working file (spark relay on O266 SHARP 1). **ES is not solved here or anywhere; no infinite case of ES is claimed.**
Labels as in DISCOVERIES.md. Preprints (Shkredov arXiv:2603.14116, Zhang arXiv:2605.02518) are unrefereed: every use is
CONDITIONAL. Scripts `scripts/z37_*`; memos `BRAINSTORM/z37_*.md`.

Notation (DEDEKIND_ES, ZAREMBA_TRANSFER). n odd, n ≡ 1 (4). A length-3 word w = (t, u, v) ∈ ℤ³_{≥2} with
tuv − u − v = n; A = tu − 1, A* = tv − 1, AA* = tn + 1 =: N_t, n/A = [[v, t, u]]; χ(w) := (A/n) (Jacobi).
N₋(n) := #{w : χ(w) = −1} (= the five-slice count, DEDEKIND Thm 4.5); a₀, a_T as in DEDEKIND §4.4.
RS = Rickards–Stange arXiv:2401.01860v3 (Duke 2025); Ψ = {γ ∈ Γ₁(4)_{≥0} : (a/b) = 1}, Ψ₁ = ⟨R, L⁴⟩,
R = [[1,1],[0,1]], L = [[1,0],[1,1]].

## 0. Iteration log
* cp0: merged O266 (side-agent/zaremba-transfer); read ZAREMBA_TRANSFER, RS (full PDF, §§2–5), DEDEKIND_ES §§1–4,
  THREE_SQUARES / NEAR_SQUARE (clean levels, coin model, open spark S2 = residual near-square gradient on unclean levels).
  Literature search (2024–26 citers of RS): §6.
