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

## 2. The generating function and the one-step monotonicity conjecture

**Why G.** If `G_F(λ) ≤ 1` for weights `λ_v := 2^{log m_v/𝓛}` (`m_v` = the
modulus that coordinate v contributes), then for every τ

```
Σ_{U: log m_U > τ} ‖F^{=U}‖²  ≤  2^{−τ/𝓛}·G_F(λ)  ≤  2^{−τ/𝓛},     m_U := ∏_{v∈U} m_v.
```

So the Efron–Stein truncation of `F^{(j)}` at modulus `e^τ` has ℓ²-error
`≤ e^{−3S}/(100m²(S+1))` (O8 EL) as soon as `τ ≥ 𝓛·log₂(100m²(S+1)e^{3S})
≍ 𝓛(S+k𝓛)`. This is a **modulus-weighted** EL, with no bit factor b and no
width factor k: compare O8 Lemma 6.1, `log(modulus) ≍ k·b·k_0·𝓛 ≍ k𝓛²S`.
Uniform weights `λ_v=2^{1/k}` give ESW-type coordinate tails
`energy(F;t) ≤ 2^{−t/k}G_F`.

**Single events.** For a cylinder C on support E (`π=P(C)`):
`G_{1_C}(λ) = π·∏_{v∈E}(λ_v−(λ_v−1)/q_v) ≤ π·w_E` and
`G_{1−1_C} = 1−2π+G_{1_C} ≤ 1−π(2−w_E)`. So `w_E≤2` is exactly the threshold
for `G≤1` (O9 Lemma 4.1's disjoint systems: `G=∏_i(1−π_i(2−w̃_i))`).

**Useful identities (PROVED, standard).** (i) `G_F = Σ_V ∏_{v∈V}(λ_v−1)·‖L_VF‖²`.
(ii) With `h=1−F`: `G_F = 1−2E h+G_h`, so `G_F≤1 ⟺ G_h ≤ 2E h`.
(iii) `G_F = E_x[F(x)·(ΛF)(x)]`, and `ΛF(x)` is the "probability" of no event
under the signed product measure `ν_x` with `ν_x(x_v)=λ_v−(λ_v−1)/q_v`,
`ν_x(b)=−(λ_v−1)/q_v` (`b≠x_v`). (iv) For `λ_v∈[1,2]`,
`Λ = E_V[⊗_{v∈V}(2I−E_v)]`, V random with `P(v∈V)=λ_v−1` independently,
i.e. G at general weights is an average of G at weights `{1,2}` (random
restrictions).

**Conjecture MONO (EVIDENCE, no counterexample found).** For every
single-value system with good-indicator F and every further cylinder A
(weight `w_A`), `G_{F(1−A)}(λ) ≤ G_F(λ)·(1+P(A)(w_A−2)_+)`.

Consequences (if MONO holds): by induction from `G_1=1`,

```
(C-exp)  G_F(λ) ≤ ∏_E (1+P(E)(w_E−2)_+) ≤ exp(Σ_E P(E)(w_E−2)_+),
(C-1)    G_F(λ) ≤ 1  whenever every event has w_E ≤ 2.
```

Evidence (`scripts/omega10_*.py`, exact Efron–Stein on `[q]^n`, `q≤5`, `n≤8`):
* `omega10_mono.py`: 2000 random (system, A, λ) triples, `λ_v∈[1,2]` and
  `[1,3]`: max of `G_{F(1−A)}/(G_F(1+P(A)(w_A−2)_+)) − 1` is `0` (attained
  when A is redundant).
* `omega10_cexp.py`: 1600 random systems incl. full coincidence systems
  (`X_i=X_j=c`, all pairs and values), `λ_v∈[1,3]`: C-exp never violated.
* `omega10_bool.py`, `omega10_gen.py` (hill-climbing for max `G_F` with
  `λ^k=2`, q=2 up to n=10 and q≤6): the maximiser is always a single event.
* C-1 is false beyond its range: q=2, k=1, `λ=4`, OR of n literals:
  `G_F=(5/4)^n`. And the **pointwise** versions fail
  (`omega10_pointwise.py`: `ΛF(x)≥−1` on bad x fails), so any proof must
  average over x.
* A natural generalisation is false: for `ψ=g·F` (bad for one system, good
  for another, disjoint supports) `G_ψ=G_g G_F` may exceed `E[ψ w_min]`.
