# The energy switching lemma: suppression and a generating-function route (task O38)

Task O38 (branch `esw-suppression`). Labels as in the house rules. ES is not
touched; nothing below bears on whether `W(p)<∞`. Notation: PO =
`POINTWISE_OMEGA.md`, O2, O8, O9 likewise; `𝓛=log T`.

**Status: work in progress (not reviewed).**

## 0. Notation

A *single-value system* on a product space `Ω=∏_v[q_v]` (uniform measure):
events `E` (cylinders) fixing `X_v=c_E(v)` for `v∈supp E`; `A_E=1_E`;
`h:=1[some event occurs]`, `F:=1−h`; `w_E:=∏_{v∈supp E}λ_v` for weights
`λ_v≥1`. Efron–Stein decomposition `f=Σ_U f^{=U}`, `L_v:=I−E_v`,
`L_V:=∏_{v∈V}L_v` (so `L_Vf=Σ_{U⊇V}f^{=U}`), and

```
Λ = Λ_λ := ⊗_v (I + (λ_v−1)L_v),     G_f(λ) := ⟨f,Λf⟩ = Σ_U (∏_{v∈U}λ_v)·‖f^{=U}‖².
```

`G` is the *energy generating function*: if all `λ_v=λ`, then
`energy(f;t) ≤ G_f(λ)·λ^{−(t+1)}`, and with weights,
`Σ_{U: Σ_{v∈U}log λ_v > τ}‖f^{=U}‖² ≤ e^{−τ}G_f(λ)`.

## 1. Independent check of O9 §4 (Lemma 4.1, Cor 4.2)

*Lemma 4.1: correct.* `F^{=U}=∏_i(1−A_i)^{=U∩E_i}` holds for disjoint
supports (and `F^{=U}=0` if U meets no support only when U≠∅ contains an
unused coordinate — harmless). `‖A_i^{=E_i}‖²=∏_{ℓ}q^{−1}(1−q^{−1})` is right
(A_i is a product of independent literal indicators). The limit is a lower
bound obtained by truncating to finitely many j, so no interchange issue.

*Cor 4.2, bullet 1: correct* (Choi: median of `Po(S)` is `≥S−log 2`, so
`Pr[Po(S)≥S−1]≥1/2`). Vacuous for `S<1`.

*Cor 4.2, bullet 2: correct as a necessary condition, slightly mis-described.*
EL is `energy(F^{(j)};t) ≤ e^{−3S}/(100m²(S+1))`; in the limit `q→∞` with S
fixed, `m=S/π→∞`, so EL becomes *stronger* than `Pr[Po(S)>t/k] ≤ e^{−2S}`
(it eventually fails for every `t<km`). The derived `t ≥ (c_*−o(1))kS`,
`c_*≈3.59`, is therefore a valid necessary condition. (`c_*log c_*−c_*+1=2`
checked: `c_*=3.5911`.)

*Cor 4.2, the "1/6 ceiling": arithmetic slip and a scope caveat.*
1. With `z=𝓛²`, `k=𝓛/(2log𝓛)`, `S*≍𝓛^4log𝓛`: `kS*·log z ≍ 𝓛^5log𝓛` and
   `kS*·𝓛 ≍ 𝓛^6` (not `𝓛^6/log𝓛`). The conclusion "1/6" is unaffected.
2. The floor counts **coordinates** at cost `≤𝓛` each (O9 Thm 2.2:
   `log Z ≤ log Q_Π+2(3k+2d+1)𝓛`). The true cost of a junta set U is
   `Σ_{ℓ∈U}log(modulus used at ℓ)`. In the ES system an event with support
   `supp E` is a class mod its rough part `r_E ≤ T`, so the lower-bound
   juntas of Lemma 4.1 (unions of j event supports) cost
   `≤Σ log r_E ≤ j𝓛`, not `jk𝓛`. Lemma 4.1 then gives the floor
   `≍S·𝓛` for the *modulus* (if the junta function only reads `X_ℓ` to the
   precision the events use), i.e. `≍𝓛^5log𝓛` under ET, not `𝓛^6`.
   So "1/6 is the ceiling" is right for arguments that charge every junta
   coordinate `≍𝓛` (as ESW in coordinate count does); an argument with
   **modulus-weighted** energy tails could in principle go below
   (towards 1/5, if also `log Q_Π≪𝓛^5`). §2 below is such an argument.
   (Precision refinement: units mod `ℓ^a` ≅ units mod ℓ × `(ℤ/ℓ)^{a−1}` by
   base-ℓ digits, and the Haar measure is the product measure, so an event
   fixing `X_ℓ mod ℓ^b` is single-value on the first b digit coordinates;
   each digit coordinate costs `log ℓ`.)

No error affecting O9 §§1–3 or the statements of Lemma 4.1 was found.
