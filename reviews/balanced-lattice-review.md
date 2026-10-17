# R269 — hostile review of O256 (BALANCED_LATTICE.md, checkpoint 1 incl. R-O256 repairs 1–9)

Reviewer: R269 side agent (branch side-agent/review-balanced-lattice, merged side-agent/balanced-lattice at a5cf0e51).
Scope: BALANCED_LATTICE.md §§1–7, memos BRAINSTORM/z27_*.md, scripts/z27_{dual,eqcheck}.py, data/z27/, AGENT_REPORT_O256.md.
From-scratch scripts: scripts/review_r269_*.py (none reuse the author's code). Sources/ contains none of Banaszczyk 1993,
Serre 1981, Schinzel 1977: citation checks below are from the reviewer's knowledge of the statements and are flagged as such.

## Summary verdicts (filled in claim by claim)

| claim | verdict | notes |
|---|---|---|
| Lemma 1.1 (Λ*/ℤ^S ≅ Ĥ) | SOUND | re-derived; also checked numerically with an LLL dual basis built from an independent kernel computation (no characters used): λ₁^{(1)}(Λ*) = min(1, 𝔻_min) in 70/70 non-degenerate samples |
| Prop 1.3 (transference) | SOUND | constants re-derived: lower bound exact; upper uses μ_∞ ≤ μ₂, Banaszczyk μ₂λ₁^{(2)}(Λ*) ≤ k/2 (his formal bound, valid for every k, no o(1)), λ₁^{(2)} ≥ λ₁^{(1)}/√k. Discrete consequences via FORCED_WINDOW Prop 4.1(i)/(ii) correct. Numerics: μ_∞·min(1,𝔻) ∈ [0.51, 0.96] (k = 3) and [0.62, 1.11] (k = 4) against the proved window [0.5, k^{3/2}/2]; D1, D2 |
| Cor 1.4 | SOUND-AFTER-REPAIRS | (a), (c) correct; (b) is an "⟺ up to k^{O(1)}" whose two directions carry different constants (D3) |

## Defects

**D1 (MINOR) — Prop 1.3 proof, citation "Banaszczyk, Math. Ann. 296 (1993), Thm 2.1".** The PDF is not in sources/ (not
accessible to me). The inequality used, μ(L)λ₁(L*) ≤ n/2 (Euclidean), is indeed the bound Banaszczyk proves formally (the
sharper (1/(2π) + o(1))n is remarked at the end of his paper; cf. Miller–Stephens-Davidowitz, arXiv 1907.09020, Thm 1.1 and the
remark after it). To my recollection the μ·λ₁* statement is his Thm 2.2 (Thm 2.1 being λ_iλ*_{n−i+1} ≤ n); pages 625–635(6).
*Repair:* cite "Banaszczyk 1993, the covering-radius transference bound μ(L)λ₁(L*) ≤ n/2" without a theorem number, or
verify the number. No mathematical consequence.

**D2 (MINOR, informative) — Prop 1.3 constant k^{3/2}.** From-scratch check (scripts/review_r269_transference.py; data in
data/review_r269/transference_k{3,4}.txt: μ_∞ on a 1/m-grid, 𝔻_min by exact integer arithmetic, λ₁^{(1)}(Λ*) from an
LLL-reduced dual basis, L_min by exact sumset covering) finds no violation of any inequality in Prop 1.3 / Cor 1.4(a), and
μ_∞·𝔻_min ≤ 1.11 in all 70 samples, i.e. the k^{3/2}/2 = 2.6 (k = 3), 4.0 (k = 4) upper constant is never close to attained.
The 3/2 in the exponents 13/2 and 9/2 (Thm 4.1/4.2) comes entirely from this ℓ²-detour; an ℓ^∞/ℓ¹ transference with an O(k log k)
or better constant would lower it. Not a defect of correctness; Remark (1) after Thm 4.1 already says "not optimised".

**D3 (MINOR) — Cor 1.4(b).** "balanced at the random-lattice scale (L_min ≤ k^{O(1)}N^{1/k}) ⟺ (up to k^{O(1)}) no ψ ≠ 1 has
𝔻_S(ψ) ≤ N^{−1/k}k^{−C}": the two directions hold with different constants. *Repair:* state as two implications:
𝔻_min ≥ k^{−C}N^{−1/k} ⇒ L_min ≤ ⌈k^{C+3/2}N^{1/k}⌉; L_min ≤ k^{C}N^{1/k} ⇒ 𝔻_min ≥ 1/(L_min + 1) ≥ k^{−C}N^{−1/k}/2
(and 𝔻_min ≤ (k!/N)^{1/k} always, by (a)).
