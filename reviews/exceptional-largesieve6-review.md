# Hostile review R71 of EXCEPTIONAL_LARGESIEVE6.md (LS6, agent O71)

Reviewer: R71 (branch `side-agent/review-ls6`). Reviewed: LS6 as merged from
`side-agent/soft-pivotal` at 0f417ad. ES is not solved; (A\*) is not proved.
From-scratch scripts: `scripts/review_ls6_*.py`.

## Verdicts per claim (filled in as the review proceeds)

| claim | verdict |
|---|---|
| Lemma 1.1 | SOUND |
| Cor 1.2 | SOUND (see notes) |

## Notes per claim

### Lemma 1.1 (prefactors are free)
Re-derived: LS4 defines `𝓡_{p'}(σ) = Σ_θ|σ̂(θ)|^{p'}`; with `P_S ≥ 0`,
`w_∅ = 1`, `Λ ≥ 1` the chain `1 + Λ^{2β}Σ_{S≠∅}w_SP_S ≤ Λ^{2β}Σ_Sw_SP_S`
is correct, and `Σ_S w_SP_S = E_T𝓡_2(σ_T)` is LS4 Lemma 1.1's identity.
Arithmetic of the remark: `2β·½log N = (log N)^{3/4}` ✓.
Script `scripts/review_ls6_lemma11.py` (exact enumeration on ℤ/210, 40
random laws/weights, Λ taken minimal): inequality holds, max LHS/RHS 0.59.

### Cor 1.2 (tilted law inherits LS4 Thm 4.2, Lemma 5.1, Thm 5.2, Cor 5.3)
Re-derived: LS5 Prop 2.1 with `Q'_c(𝒜_c) ≥ 3/4` gives `Z_c ≥ (3/4)e^{−8m_c/3}`
and `log E_T𝓡_2 ≤ 16m_c/3 + 2log(4/3) ≤ 6m_c + 1` ✓. Adding
`2β(log Λ' + 8m_c/3 + log(4/3))` gives `≤ 7m_c + 2 + 2β log Λ'` once
`16β/3 ≤ 1` ✓; with `m_c ≤ 32J`, `224J ≤ 512J` ✓.
Lemma 5.1 transfer: LS4's proof uses `1_G` only via (i) pinned
representation (valid for any `Φ ≥ 0`), (ii) `‖Φ‖_∞` bound, (iii)
non-pivotality when `v_ℓ, v'_ℓ ∉ R_ℓ`. For `Φ = 1_𝒜e^{−2Y}`, (iii) needs
every `p̃_q` (q ∈ 𝒫, including q = ℓ and q < ℓ) to agree on the two corner
paths: q < ℓ trivially; q ≥ ℓ because no class through ℓ is matched (its
ℓ-residue lies in R_ℓ) and `F̃_q` is a function of `F_q` (truncated
forbidding). ✓. The resulting `Z^{−1}` prefactor is exactly what Lemma 1.1
absorbs. This does not contradict R67 M3's example (that example compares
the tilted coefficient with the *untilted* prefactor `Q'(G)^{−1}`; the
present bound carries `Z^{−1}`).

### Lemma 2.1, Prop 2.2 (soft-pivotal bound)
Re-derived. (2.1): `E_v[χ_θΦ] = E_{v,v'}[χ_θ(v)Σ_A(−1)^{|A|}Φ(v^A)]` since for
A ≠ ∅ the coordinates `v_A` are independent of `v^A` and `E χ_ℓ = 0`; the
coin rule realises `U(·|Ω_q∖F̃_q)` exactly (`P(a) = (1/|Ω|)(1 + p̃/(1−p̃))`) ✓.
Leibniz (a) is the standard discrete product rule; (c): `D_ℓψ ≡ 0` off
pivots, `|D_ℓ(F∘u)| ≤ LΔ(u)`, `D_{T∖ℓ}` costs `2^{|T|−1}` ✓. Constants:
`g = (1−p̃)^{−1}` on `[0,1/2]` has Lipschitz 4 ⇒ `2^{|T|−1}·4Δ = 2^{|T|}·2Δ` ✓;
`φ_q` Lipschitz `2w_q` ⇒ `2^{|T|}w_qΔ_q` ✓; idle factors ≤ 1 except
`g_ℓ ≤ 2` ⇒ `2^{|S|}` ✓. Grouping maps by partitions and dropping
injectivity only increases ✓. `Δ_q ≤ Σ_C q^{−v_q(G_C)}` over varying
top-q classes: `F_q(A)ΔF_q(A')` is covered by residue sets of classes
matched off-top on exactly one side; truncation is 1-Lipschitz ✓.
(The pinned factor table uses `1_𝒜 = Π_{q∉S}λ_qΠ_{ℓ∈S}h_ℓ` on corners —
correct because off S the coin rule guarantees `x_q ∉ F̃_q`.)
