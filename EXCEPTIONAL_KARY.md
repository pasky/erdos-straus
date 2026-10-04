# EXCEPTIONAL_KARY — the k-ary comparison inequality (task O7)

Status: **in progress.** Labels follow `DISCOVERIES.md`. PROVED means proved
here and checked internally only. Notation follows `EXCEPTIONAL_TWIN.md`
(ETw), `EXCEPTIONAL_THETA.md` (ET).

## 0. Summary (draft)

Conjecture 6.4 of ETw asks for a k-ary analogue of ET Prop 2.4 for the
*plain* sequential law σ. We do not settle it for σ itself. We prove the
same weak `d·log(mass)` comparison for a slight modification σ̃ of σ, the
**phantom-sequential law**: at each coordinate it also avoids completions
of the *discarded* draws at earlier replaced coordinates. The proof needs
no incident-weight hypothesis, no Markov removal, and no sparsity. Its two
ingredients are a coupling in which the replaced set does not depend on the
interpolation coins, and a one-dimensional extrapolation lemma for
binomial laws. The cost is path-dependent, so only first moments of the
window masses enter.

## 1. Setting

* `V` a finite ordered set of coordinates; `y_ℓ ∈ Ω_ℓ` (finite);
  `ν = ⊗ν_ℓ` a product law.
* A family 𝒞 of **patterns** `C = (T_C, a_C)`, `T_C ⊆ V`, `a_C ∈ Ω_{T_C}`.
  `top(C) = max T_C`. Arity `|T_C| ≤ r`; unary patterns allowed.
  `𝒜 = {y : y_{T_C} ≠ a_C for all C}`.
* `f` is **d-local** if `f = Σ_T f_T` with `f_T` a function of `y_T` and
  `|T| ≤ d`. (λ-level functions on a window with costs `> s` are d-local
  with `d = ⌊λ/s⌋`.)
* Thresholds `δ_ℓ ∈ (0, 1/4]`.

**The phantom-sequential process.** Coordinates are processed in order.
The state before ℓ is `(c_i, y_i)_{i<ℓ}`. Put

    F̃_ℓ = { a ∈ Ω_ℓ : ∃ C, top(C) = ℓ, ∃ z ∈ Π_{i ∈ T_C∖ℓ} {c_i, y_i}, (z, a) = a_C },
    p̃_ℓ = ν_ℓ(F̃_ℓ).

Draw `c_ℓ ~ ν_ℓ` independently of the past. Call ℓ **light** if
`p̃_ℓ ≤ δ_ℓ`.
* If ℓ is light and `c_ℓ ∈ F̃_ℓ` (ℓ is **replaced**, ℓ ∈ R), draw `y_ℓ` from
  `ν_ℓ(· | Ω_ℓ ∖ F̃_ℓ)`, independently of `c_ℓ`.
* Otherwise `y_ℓ = c_ℓ`.

σ̃ is the law of `y`. It differs from the plain sequential law σ of ETw
Conj 6.4 only in the **phantom activations**: completions of `c_i` at
earlier *replaced* coordinates i, where `c_i ≠ y_i`. Without replaced
coordinates among the earlier ones, `F̃_ℓ` is exactly the activated set of σ.

Write `ω = (c, y)` for the whole path, `M(ω) = Σ_{ℓ light} p̃_ℓ` (the
light activated mass) and `n(ω) = |R|`.
