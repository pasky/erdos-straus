# Review R34a (reviewer 1 of 2): POINTWISE_OMEGA9.md — Theorem 1.1 (linear transfer)

Reviewer: side-agent/review-omega9a. Reviewed: branch `side-agent/omega9-exponent` at `9a21ffc`.
Scope: Thm 1.1 line by line, the quotation of (G) = MV III Thm 28.19, Cases 0/A/B, final inequality.
From-scratch scripts: `scripts/review_o9a_*.py`.

## Summary verdicts
(filled in at the end)

## 1. The quotation of (G) (MV III Thm 28.19, pp. 229–232 of the archived PDF)

Checked against `sources/omega9/montgomery-mnt3.pdf` (pdftotext; the SHA-256 in the README was
not re-verified by me beyond the file being the one present in the branch).

MV III Thm 28.19 (Gallagher), verbatim content: there are constants `c ≥ 1`, `κ_0 ≥ 3` such that if
`κ ≥ κ_0` is a constant and `1 < Q^{6c} ≤ x`, then
`Σ_{q≤Q} Σ*_{χ mod q} |ϑ(x;χ) − E_0(χ)x| ≪ x exp(−log x/(κ log Q)) + (log x/log Q)^2 x Q^{-1}`,
unless `F(s,Q)=∏_{q≤Q}∏*_χ L(s,χ)` (28.89) has an exceptional real zero `β_1` with
`1−β_1 < 1/(κ log Q)`, in which case the term of `χ_1` is replaced by `ϑ(x;χ_1)+x^{β_1}/β_1` and
the RHS by `(1−β_1)(log x)[x exp(−log x/log Q) + x log x/(Q log Q)]`.

* Author's transcription (OMEGA9 §1, "Cited input (G)"): **matches**, including the repaired
  exceptional RHS (prefactor `(1−β_1)log x` multiplying both terms; `exp(−log x/log Q)` without κ).
  The sum ranges over `q ≤ Q` including `q=1` (trivial character mod 1, `E_0=1`), as the author says.
* "unique, real" exceptional character: not in the theorem statement itself, but supplied by MV's
  "Exceptional Zero Statement" (28.61)–(28.62), p. 216 (at most one zero with `Re s > 1−c_1/log T`,
  real, χ_1 quadratic). OK provided `κ ≥ 1/c_1` — which MV's choice `κ_0 = 3max(c, c_1, …)` does
  NOT obviously ensure (c_1 vs 1/c_1); see minor m1.
* Page bound: MV (28.62) gives `1/(c_2 q_1^{1/2}(log q_1)^2) ≤ δ_1`, as quoted. OK.
* Effectivity: the statement does not say "effective", but §28.7 (p. 217) explicitly states that the
  setup is chosen to keep c_1 computable "especially in connection with bounding the least prime";
  all inputs (28.14, 28.15, 28.62) are effective. The author's "absolute effective" is acceptable.
* Uniformity in κ: the implied constant is uniform for κ ≥ κ_0 (proof: `c/κ' ≤ 1`). The author fixes
  κ, so no issue.
* Source quality: MV III is an unpublished course draft and its proof of 28.19 has visible internal
  slips (minor m2). The statement is the standard Gallagher (1970) Thm 7 shape; the original was not
  obtained by the author nor by me. Label "PROVED modulo (G)" is the right one.

**Verdict on (i): SOUND** (quotation exact, modulo minors m1, m2).
