# Review 3 of POINTWISE_OMEGA8.md — §6 only (R30c, hostile)

Reviewer: side agent `review-omega8c`. Scope: §6 (6.1 ledger, Lemma 6.1,
Thm 6.3, §6.4, §6.5, Prop 6.6) of POINTWISE_OMEGA8.md as on
`side-agent/haar-primes-2`. §§1–5 were reviewed in
`pointwise-omega8-review.md` and `-review-2.md` and are taken as given
except where §6 changes their inputs.

## Summary verdicts

(in progress)

## Defects

(in progress)

### Working notes, Lemma 6.1 (re-derived)

* Restriction identity: for ρ=(I,z), S⊆I, f̂_ρ(S)=Σ_{T⊆I^c} f̂(S∪T)χ_T(z),
  so E_z f̂_ρ(S)=f̂(S). Then Σ_S p^{|S|}|f̂(S)| = Σ_S E_I[1_{S⊆I}|E_z f̂_{I,z}(S)|]
  ≤ E_ρ‖f̂_ρ‖_1. Re-derived; correct (this is Mansour's argument).
* ‖f̂_ρ‖_1 ≤ #leaves ≤ 2^{DT(f_ρ)} (|f|≤1, path indicators have spectral
  norm exactly 1). E 2^{DT} ≤ Σ_s 2^s Pr[DT≥s] ≤ Σ_s 2^{-s} = 2 with
  p=1/(4C_H w). Correct (Håstad in O'Donnell's form holds for all s≥0).
* Σ_{|S|<d}|ĝ̃(S)| ≤ p^{-(d-1)}·2 ≤ 2(4C_H w)^d. Correct.
* M_1 accounting: PO Thm 4.1 has M_1=Σ|c_i|/φ(d_i), i.e. Haar-weighted ℓ¹;
  a bounded function h of a coordinate set J, expanded over the unit cells
  on J, has M_1 = E_Haar|h| exactly. With |χ̃_S|≤1 (conditional expectation
  of a ±1 function) and h=A_iA_jA_{j'}χ̃_Sχ̃_{S'}, M_1(h) ≤ E[A_iA_jA_{j'}] ≤ 1.
  Total: 1 + m + 2m²·‖ĝ̃‖_1 + m³‖ĝ̃‖_1² ≤ 1+m+4m²X+4m³X² ≤ 10m³X²,
  X=(4C_Hw)^d, so log M_1 ≤ 3log m + 2d log(4C_Hw) + log 10 ≤ … + 4. Correct.
* Independence needed for E[A_je_j²]=P(E_j)E[(F^{(j)}−g_j)²]: g_j must be a
  function of the coordinates outside supp E_j only. True if the encoding is
  applied to F^{(j)} as a function of those coordinates (as Lemma 4.1 says).
  Not stated in Lemma 6.1 — see MINOR defect m1.
