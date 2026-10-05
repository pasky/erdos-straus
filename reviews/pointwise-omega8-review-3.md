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
* From-scratch numerics (`scripts/review_o8c_spectral.py` →
  `data/review_o8c/spectral.txt`). Part A: 36 random DNF/p cases on 5–7
  bits, exhaustive over all restrictions with exact decision-tree depth:
  restriction identity exact (error 0), `Σp^{|S|}|f̂(S)| ≤ E‖f̂_ρ‖₁ ≤ E2^{DT}`
  and `‖f̂_ρ‖₁ ≤ 2^{DT(f_ρ)}` pointwise hold in all cases. Part B: q-ary toy
  (3 coordinates on [3], 2-bit encoding with non-uniform fibres), pulled-back
  Fourier truncations at d∈{2,3,5}, 24 cases: every χ̃_S satisfies |χ̃_S|≤1,
  depends only on the blocks touched by S and never on supp E_j; Jensen
  `E_{π*}(F−g)² ≤ E(F̃−g̃)²` holds; `B≤F` pointwise; cell-expanded
  `M_1(B) ≤ 1+m+2m²L+m³L²` (L = truncated ℓ¹ norm). No failures.

### Working notes, §6.4 counterexample (re-derived + numerics)

* Masses: per-coordinate `(N−1)/q ≤ q^{−1/2}`, total `C(N,2)/q ≤ 1/2`. Correct.
* Adversary argument re-derived: with the N−s fixed values distinct, answering
  each query with a value distinct from all fixed and earlier answers
  (possible since N+s<q) leaves f_ρ non-constant until the last query
  (last free coordinate can still hit or avoid). So `DT_q(f_ρ)=s`. Exact
  minimax DT_q (`scripts/review_o8c_counterex.py` → `data/review_o8c/counterex.txt`)
  confirms `DT_q(f_ρ)=s` for q∈{9,16,25}, all s tested.
* Quantitative failure: with `p=1/(4C')`, `Pr_ρ[DT_q ≥ pN/2] ≈ 0.61` for
  q=10⁴…10⁸ while `(C'(2p+max w_ℓ))^{s_0}` is 10^{−3.5}…10^{−376}. The
  counterexample is valid **after a constant fix** (defect m3: with the
  doc's `p=1/(2C)` and k=2 the hypothetical bound `(Cpk)^s` equals 1).
* ES level weights of f_ρ (exact, q=49…144): W^{=1} dominates and W^{=r}
  decays in r (e.g. q=49,s=4: 1.0e−1, 1.2e−1, 8.2e−2, 1.4e−2, 1.7e−3 for
  r=0…4, r=0 being the squared mean). So the example is plausibly
  consistent with ESW, but the doc's justification is too weak (m4):
  `Pr[f_ρ=1] ≲ Ns/q ≈ p` at the typical `s≍pN` is a constant, not "nearly
  constant"; and `W^{≥1} ≤ Pr[f_ρ=1]` says nothing about the
  geometric decay in s that ESW demands for s≥2.

### Working notes, §6.1 ledger and Thm 6.3

* Ledger rows re-derived with `z=𝓛²`, `k≍𝓛/log𝓛`, `b≈2log₂T`,
  `S≤S*≪𝓛⁴log𝓛`: `w=kb≍𝓛²/log𝓛`; `k_0≍S+log m≍S*`; `t=2C_Hwk_0≍𝓛⁶`;
  Lemma 3.2 gives `log M_1≍t𝓛≍𝓛⁷`; `log max d_i≤(3k+2t)𝓛≍𝓛⁷`;
  `log Q_Π≤(π(z)+64k²S*)𝓛+4≍𝓛⁷/log𝓛`; `K≍𝓛⁷`, `log p≍𝓛¹⁴`. All correct.
* PO Thm 4.1 uses `K=1+log(M_1/μ)`, `log x ≥ C_1K·max(log Z,K)`. With
  Lemma 6.1, `μ≥0.99δ≥0.99e^{−2.2S}`: `K ≤ 3log m+2d log(4C_Hw)+2.2S+6`
  (1+4+log(1/0.99)<6). `d=4C_Hwk_0=2t≪𝓛⁶`, `log(4C_Hw)≪log𝓛`,
  `log m≤(k+2)𝓛≪𝓛²`: `K≪𝓛⁶log𝓛`. Moduli on `≤3k+2(d−1)` primes:
  `log Z≤log Q_Π+2(3k+2d+1)𝓛≪𝓛⁷`. `log p≪𝓛¹³log𝓛`, which inverts to
  `𝓛≫(log p/log log p)^{1/13}`. Correct. The gain is real: Lemma 3.2's
  `log M_1≍t𝓛` becomes `≍t log𝓛`; `log Z` is unchanged in order (d=2t).
* Lemma 3.3 (twist) uses only `E[F−B]≤EF/100`, `w_ℓ≤1/(64k)` and that B is
  a cell combination whose ψ-twist equals `E[Bψ]`; all unchanged. (I) and the
  class-of-one argument do not see u_j. So Thm 6.3 inherits §§3–4 verbatim.
* **Lemma 6.2 does not exist** in the document (§6.1 item 2 cites it; there
  is no §6.2/§6.3 heading either). This matters for the "ESW ⇒ 1/11"
  claim: see M1.
