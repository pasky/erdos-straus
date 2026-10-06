# Review R62 of EXCEPTIONAL_LARGESIEVE4.md (hostile reviewer, branch side-agent/review-ls4)

Reviewed: EXCEPTIONAL_LARGESIEVE4.md at side-agent/hrough 1314818.
From-scratch scripts: scripts/review_ls4_*.py.

## Verdicts (in progress)

| claim | verdict |
|---|---|
| Lemma 1.1 | SOUND (re-derived; brute force pending) |
| Lemma 2.1 | SOUND (re-derived) |
| Lemma 3.1 | SOUND (re-derived) |
| Prop 4.1 | pending |
| Thm 4.2 | pending |
| Lemma 5.1 | pending |
| Thm 5.2 | pending |
| Cor 5.3 | pending |

## Re-derivations

**Lemma 1.1.** Σ_{den θ | M_S}|σ̂|² = M_S Σσ_S² = E Π_{ℓ∈S}(1+h_ℓ); Möbius over
T ⊆ S gives P_S = E Π_{ℓ∈S}h_ℓ = Σ_{supp θ=S}|σ̂|² ≥ 0. Then
Σ_θ|σ̂|^{2+2β} ≤ Σ_S w_S P_S = E Π(1+w_ℓh_ℓ), and
1+wh = (1−w)+w·ℓ^E 1[x_ℓ=y_ℓ] expands to E_T 𝓡_2(σ_T). Correct; note
𝓡_p(σ)=Σ_θ|σ̂(θ)|^p incl. θ=0 (term 1), consistent with LS3.

**Lemma 2.1.** E[ℓ^E1[x=x']|past] = U(F^c∩F'^c)/((1−p)(1−p')),
η = (U(F∩F')−pp')/((1−p)(1−p')): checked. Z_ℓ=(1+wh)/(1+wη) is a
martingale-ratio density, Π(1+wη) predictable ⇒ identity. Inflation:
Σ_{a'}k'(a')(1+wh(a,a')) = 1−w+wℓ^E k'(a) ≤ 1/(1−p'): checked.

**Lemma 3.1.** Standard Efron–Stein/Walsh expansion; the B ≠ S terms die
because χ has a mean-zero factor e(c_ℓθ_ℓ) independent of the rest.
Pairing A ↔ A∪{ℓ} when ℓ not pivotal: correct (pivotality is per
realization of (c,c',π), which is what the bound uses).
