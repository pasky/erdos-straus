# EXCEPTIONAL_LARGESIEVE6 — the soft-pivotal lemma (task O71)

Status: **in progress** (agent O71, branch `side-agent/soft-pivotal`).
Labels as in `DISCOVERIES.md`. Notation: LS4 = `EXCEPTIONAL_LARGESIEVE4.md`,
LS5 = `EXCEPTIONAL_LARGESIEVE5.md` (all their notation is used: Setting 2.0
of LS5 = truncated forbidding, `Y = Σ_q w_q p̃_q`, `σ_tilt`, `Z`; LS4
Lemma 1.1, Thm 4.2, Lemma 5.1, (A\*)), LS3, K2 as there. `β = (log N)^{−1/4}`,
`z = exp((log N)^{1/4})`, `w_ℓ = (Kℓ^{−γ})^{2β}`.

## 0. Plan and summary (updated as the work proceeds)

| item | statement | label |
|---|---|---|
| Lemma 1.1 | **global prefactors in (A\*) are free**: `|σ̂| ≤ Λ·Π Kℓ^{−γ}` costs only `2β log Λ` in the Rényi bound | PROVED (trivial) |
| Cor 1.2 | hence the tilt normalisation `Z^{−1} ≤ (4/3)e^{8m_c/3}` costs `≤ 6βm_c`: LS4 Thm 4.2 holds with (A\*) for `σ_tilt` **with prefactor `Z^{−1}`**, and LS4 Lemma 5.1 / Thm 5.2 transfer to `σ_tilt` (repairing the LS5 caution R67 M3 at the level of normalisation) | PROVED (implication; inputs as LS4 Thm 4.2) |

## 1. Global prefactors are free

**Lemma 1.1 (PROVED).** Let σ be a probability on `ℤ/M_r`, `0 < β ≤ 1/2`,
`w_ℓ ∈ [0,1]`, `Λ ≥ 1`, and suppose

    |σ̂(θ)|^{2β} ≤ Λ^{2β} Π_{ℓ∈supp θ} w_ℓ      for every θ ≠ 0.

Then `𝓡_{2+2β}(σ) ≤ Λ^{2β} E_T 𝓡_2(σ_T)` (T as in LS4 Lemma 1.1).

*Proof.* With `P_S = Σ_{supp θ=S}|σ̂(θ)|² ≥ 0` (`P_∅ = 1`):
`𝓡_{2+2β} = 1 + Σ_{S≠∅}Σ_{supp θ=S}|σ̂|²|σ̂|^{2β} ≤ 1 + Λ^{2β}Σ_{S≠∅}w_SP_S
≤ Λ^{2β}Σ_S w_SP_S`, and `Σ_S w_SP_S = E_T𝓡_2(σ_T)` (LS4 Lemma 1.1). ∎

So (A\*) in LS4 Thm 4.2 may be weakened to

> **(A\*_Λ)** for c off the exceptional event and every θ ≠ 0 with z-rough
> denominator: `|σ̂_c(θ)| ≤ Λ_c · Π_{ℓ∈supp θ} K ℓ^{−γ}`,

at the additive cost `2β·log Λ_c` in `log 𝓡_{2+2β}(σ_c)`. Since
`2β = 2(log N)^{−1/4}`, a prefactor as large as `Λ_c = e^{O(m_c)}` (even
`N^{1/2}`) is harmless: it costs `O(βm_c)` (resp. `(log N)^{3/4}`).

**Corollary 1.2 (tilted law with prefactor; PROVED as an implication,
inputs as LS4 Thm 4.2 with LS5 Setting 2.0).** In LS4 Thm 4.2 take
`σ_c = σ_tilt,c` (LS5 Prop 2.1) and replace (A\*) by (A\*_Λ) with
`Λ_c = Λ'·Z_c^{−1}`, `Λ' ≥ 1` a constant. Then the conclusion of LS4
Thm 4.2 holds with `512J` replaced by `C·J` and an extra `2β log Λ'`.
Moreover LS4 Lemma 5.1 holds for `σ = Q'Φ/E_{Q'}Φ` with any `Φ ≥ 0` that
depends on the path only through the activated sets `F_q`, `F̃_q` and
membership in 𝒜 (in particular `Φ = 1_𝒜 e^{−2Y}`), in the form

    |σ̂(θ)| ≤ (‖Φ‖_∞ / E_{Q'}Φ) · Π_{ℓ∈S} 4U(R_ℓ)/(1−δ_ℓ),

so LS4 Thm 5.2 and Cor 5.3 hold verbatim for the tilted law.

*Proof.* Off the exceptional event `Q'_c(𝒜_c) ≥ 3/4`, so LS5 Prop 2.1 gives
`log E_T𝓡_2 ≤ 6m_c + 1` and `Z_c ≥ (3/4)e^{−8m_c/3}`. By Lemma 1.1,
`log 𝓡_{2+2β}(σ_c) ≤ 6m_c + 1 + 2β(log Λ' + 8m_c/3 + log(4/3)) ≤ 7m_c + 2
+ 2β log Λ'` for N large; LS3 Thm 1.1 and `m_c ≤ 32J` conclude as in LS4
Thm 4.2. For Lemma 5.1: its proof uses `1_G` only through (i) the pinned
representation `σ(x_S = v) = E_{Q'}[Φ]^{−1}E_{coins}[Φ(path(v))Π_{ℓ∈S}
k_ℓ(v_ℓ|past)]`, valid for any `Φ ≥ 0`, (ii) `0 ≤ Φ·Π|Ω_ℓ|k_ℓ ≤
‖Φ‖_∞Π(1−δ_ℓ)^{−1}`, and (iii) the fact that if `v_ℓ, v'_ℓ ∉ R_ℓ` the two
corner paths have identical activated sets, truncations, coin decisions
and avoider membership (LS4 proof, unchanged under truncated forbidding:
`F̃_ℓ` is a function of `F_ℓ`), hence identical Φ. In Thm 5.2 the factor
`Q'(G)^{−1} ≤ 2` becomes `Z_c^{−1}`, absorbed by Lemma 1.1. ∎

*Remark.* LS5 (Caution, R67 M3) noted that the pinned bound for the tilt
carries `Z^{−1}`, exponentially large in `m_c`, and that the tilt can make
an individual Fourier coefficient large. Both are true, and both are
harmless for the Hölder route: (A\*) is used only through Lemma 1.1, where a
prefactor enters raised to the power `2β`. What stays relevant is the
**product** structure `Π_{ℓ∈S}Kℓ^{−γ}`; the soft-pivotal lemma below may
therefore bound all tilt factors by 1 pointwise (no tilt-bias estimate is
needed).
