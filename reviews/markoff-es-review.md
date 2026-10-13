# R202 — hostile review of O202 (MARKOFF_ES.md)

Reviewer: R202 side agent. Document reviewed: MARKOFF_ES.md as merged from `side-agent/markoff-es` (checkpoint 1),
report reviews/agent-reports/AGENT_REPORT_O202.md. From-scratch scripts: `scripts/review_mk_*.py`.
Sources fetched for this review (arXiv full texts, pdftotext): `sources/r202/{1706.06712v3,1807.10223,1808.01584,2202.07142}.{pdf,txt}`.

## Summary verdicts

(filled in claim by claim below; table at the end)

## §1 Literature — SOUND

Checked against the arXiv full texts (sources/r202/).
* GS (1706.06712v3): Thm 1.1 (compact fundamental sets F_k^± for generic k), consequence (c) h_M(k) ≪ |k|^{1/3+ε},
  (1.6) Σ h^± ∼ C_± K (log K)², (1.7) numerics θ ≈ 0.8875 for 0 < k < 6·10⁸, Thm 1.2(i) ≥ √K (log K)^{−1/2},
  Thm 1.2(ii) almost perfect, Rem 1.3(d) method (small x₁, tentacles, [BG06]/[Nie10]), (1.8) with a_jj = ±1, and the
  "F₀ reducible ⇒ full, proofs in a forthcoming paper" remark: all stated as in the text. ✔
* LM (1807.10223): Thms 1.1–1.5 and the (log B)^{−1/4} → (log B)^{−1/2} correction of GS, (ℤ/2)³ for general m,
  Prop 2.4 (Br Ū ≅ ℚ/ℤ(−1) unless Eckardt; (Br Ū)^{G} = ℤ/2): as stated. IMRN 2021 no. 18, 14086–14122 ✔.
* CTWX (1808.01584): Thm 1.1 (non-density away from any finite S, by reduction theory only), Cor 1.2 (m ≠ 0, 4) ✔.
* Dao (2202.07142v4): author **Quang-Duc Dao** (arXiv metadata and title page), JNT 254 (2024) 65–102,
  doi 10.1016/j.jnt.2023.07.007. Thm 1.3: #{k ∈ ℤ⁴, |k_i| ≤ M : ∅ ≠ U(A_ℤ)^{Br₁} ≠ U(A_ℤ)} ≍ M⁴ — i.e. algebraic-BM
  explained failures of strong approximation, as O202 says ✔. The erratum for LITERATURE_AUTOMORPHIC.md l. 408
  ("Qian Dong Dao") is correct.
* Nuance (no defect): "fullness is trivial" is even stronger than stated — the point (1, 1, D + n + 1) lies on the
  Pell conic of the fibre C = D + n + 1, which is infinite unless (D + n + 1)² − 4n is a square, so v_F(D) = ∞ for
  almost every D.
