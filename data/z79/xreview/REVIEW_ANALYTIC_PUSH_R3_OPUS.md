<code-review reviewer="anthropic/claude-opus-5-5" mode="smart" since="9f5e9ccf0">
A separate reviewer subagent was asked to review the changes in `git log 9f5e9ccf0..`. Its request and review follow.

Request: review changes since 9f5e9ccf0 carefully (both form and substance) - analyze, critique, debate and challenge

Additionally (this augments, and must not weaken or replace, the baseline review above): Hostile cross-lab Round-3 review of notes/z79/ANALYTIC_PUSH.md and scripts/z79_analytic_r3.py, especially §§7–8, GPT-6.2 Astra lane. Check signed Plancherel, transforms/normalizations, Fejer, sharp effective-volume restriction and EPC conditional argument, LP scope including edge cases, R_M constants and arithmetic. No repo writes or side agents; Python only via ulimit -v 6000000; timeout 180 uv run --offline --no-project python. Return full verdict and all fixes.

Commit log:
commit 5413743eed2eaaa15fccaec99482ab0edab72bbf
Author: Petr Baudis <pasky@ucw.cz>
Date:   Sat Nov 21 14:41:38 2026 +0100

    Keep the signed shift norm and recover an M factor in effective volume

 data/z79/analytic_r3_lp.txt |  7 +++++++
 notes/z79/ANALYTIC_PUSH.md  | 51 ++++++++++++++++++++++++++++++++++++++++-----
 scripts/z79_analytic_r3.py  | 42 +++++++++++++++++++++++++++++++++++++
 3 files changed, 95 insertions(+), 5 deletions(-)

Review:
**Verdict: accept the substance of §§7–8. No mathematical gap found. Six form fixes are needed before export, all wording or labelling, none to the mathematics.** The §§7–8 cross-review is still owed and is correctly marked so in §0. I made no repo writes; my scratch scripts are in `/tmp`.

## What I checked independently
- **The replay reproduces.** `scripts/z79_analytic_r3.py` under ulimit/timeout gives output byte-identical to `data/z79/analytic_r3_lp.txt`.
- **Signed Plancherel (9) holds.** I re-derived it by hand: the positive-sign discrete transform is the sum of ẑ(b−ξ), the shift multiplies by e(−iQξ), ξ=(a+u)/Q and c≡−a (mod Q). μ_H has mass 1. A numeric test (W=40, Q=7, H=5, C=3000, smooth bump times chirp) gives LHS = RHS to a relative error of 7·10⁻¹³.
- **The transform and normalisation in (10) hold.** With T=C/(QW) and J=C/W²:
  - the phase is −T[v⁻¹+((j−u)/J)v], with critical point v*=((j−u)/J)^{−1/2} and critical value −2√(C(j−u))/Q;
  - the amplitude W·T^{−1/2} gives the prefactor W²/(TQ);
  - the error in one class is (1+J/Q)·W·T^{−3/2} = O(T^{−1/2}), using T=WJ/Q and J/Q ≥ 1;
  - the main term is O(√T), so the additive error in the square is O(1).
- **(11) and the Fejér step hold.** The u-derivative of (11) is a√C/J^{3/2} = aW/J. The tail bound μ_H(|u|>A/H) ≤ 1/(2A) follows from |D_H(u)| ≤ 1/(2|u|). At the 6/19 vertex, in units of r, W=6, J=8, Q=H=2, Y=4, so the coherent offsets are |a| up to exponent 4 and √(WY/H) = W/H = 4. All of this checks.
- **The fibre and effective-volume bound in §8 holds.** s = Mdk−n ≡ −n (mod M), so there are O(1+V/M) choices of s, each with τ((n+s)/M) pairs (d,k). This cuts both the detector diagonal and the fibre bound. Everything else in §§2, 5–6 already depended on V only through V/M:
  - L = MNW/V = NW/B′;
  - the zero modes are V/(MN) and V/(MW);
  - the 1/L normalisation is V/(MWQ).

  So the base-D LP is exactly the R2 LP with ŷ gaining +μ and l losing μ. At μ=0 it is literally R2's μ=0 check. At μ=1/3 it coincides with R2's e=l corner. The affine box-over-triangle argument is sound: every test is jointly affine in (μ, α, β, γ, x, e, i), and the box sides are affine in the base.
  - A brute-force run (n ≤ 3·10⁵, M from 4 to 1000) gives R_M(n)/(1+D^{1/3}) ≤ 4.4.
  - A random-interior sweep of the new LP, written from the note's formulas rather than the script's, found no violation.
- **The EPC conditional holds.** Under the exponent-pair conjecture (EPC) each conductor sum is ≪ n^ε·N√W, which needs 2r+γ/2 ≤ t. That gives exactly 4/13, and no condition involves μ. The TY condition y ≥ N′² is equivalent to Y′ ≥ 1, which is guaranteed by 2γ<1. The fixed-4 version is indeed in `paper/es-count-note.tex:955`.
- **The constants and arithmetic are right.**
  - 1−5θ = −12508/21497, and the old exponent −5707/21497 is correct.
  - D^θM^{1−3θ} = n^θM^{1−5θ}.
  - n ≤ D^{5/3} in the analytic range.
  - The ET c-slice term is n^θc^{1−4θ}. Summed over c ≍ n^{1/5} it gives ≈0.463 > 2/5, so "not free" is correct.
  - The "1+" in (12) is genuinely needed (a=b=d=1 with M=n+2).

## Fixes required
1. **§8, "the sharpest M exponent … is −12508/21497" is false as worded.** θ=25/79 gives −46/79 ≈ −0.58228, which is more negative than −0.58185. The two bounds differ by a factor (n/M⁵)^{146/1698263}, and all three θ coincide at M=n^{1/5}. Suggested replacement: "With the final θ the M exponent is −12508/21497 (previously −5707/21497). In the analytic range M ≤ n^{1/5} this θ gives the smallest of the three bounds."
2. **§8 should state the base-D parameters explicitly:** P = D^r log³(2n), H = ⌈D^j⌉, K = max(1, ⌊D^{zr}⌋). At present they are only implied by "all exponents now to base D".
3. **§8's CERTIFIED line says the "§4 falsifiers are … replayed", but the r3 script replays none of them.** It should say they are unchanged and point to the replay by `scripts/z79_analytic_push.py` in §4.
4. **Triage wording.** Replace "RECORD (§§2, 5–6, 8 uniform-M only in Round 3)" with: "RECORD: §§2, 5–6 (fixed M); §8 (12) updates the uniform clause of the same STATUS row (no new row)." Under the STATUS test, the uniform-M gain belongs in that row's parenthetical only.
5. **The STATUS delta leaves an error for the export.** The current STATUS row says "no exponent-pair input". 6801/21497 uses Trudgian–Yang, and only 25/79 is free of exponent pairs. The delta should tell the export to change that clause.
6. **Notation clashes.** Rename D=n/M², which collides with the D of §2, D_I, D_H and D₀/D₁/D₂. B′ sits next to B in the same LP. T and J are silently redefined in §7. "O_P(Q/W)" collides with the prime scale P; write O_k.

## Optional improvements and debate points
- **Script readability.** Label the seven slack columns, using the names from the R2 script, and print per-vertex slacks. The output is currently anonymous and less auditable than R2's.
- **§7 and §8 are connected.** If one had P_Q ≪ W·n^ε with H ≍ W/N, the budget would become exactly 2r+γ/2 ≤ t, the EPC condition, i.e. 4/13. One sentence saying so would show that §7's missing estimate has the same strength as EPC here.
- **Novelty of §8.** The effective-volume gain is essentially an elementary congruence observation fed into an unchanged LP. It is correct, but it matters only for growing M, and the only downstream use is the ET c-slices, which still don't sum. It should not be presented as more than a refinement of the uniform clause.
- **Minor:** the §0 Result line is no longer one sentence.
</code-review>
