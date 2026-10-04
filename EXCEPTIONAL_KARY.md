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

## 2. The comparison theorem

**Lemma 2.1 (avoidance, inflation; PROVED).**
1. Every pattern whose top is light avoids `y`: if `top(C) = ℓ` is light
   then `y_{T_C} ≠ a_C`. Hence `y ∉ 𝒜` only through heavy tops, and
   `P(y ∉ 𝒜) ≤ Σ_ℓ E[p̃_ℓ 1{p̃_ℓ > δ_ℓ}]`.
2. Given the state before ℓ, `y_ℓ ~ ν_ℓ(·|Ω_ℓ∖F̃_ℓ)` if ℓ is light and
   `y_ℓ ~ ν_ℓ` otherwise. In particular, for every `S ⊆ V` and `b ∈ Ω_S`,
   `σ̃(y_S = b) ≤ Π_{ℓ∈S}(1−δ_ℓ)^{−1} ν(b)`.

*Proof.* 1. For every ℓ, `y_ℓ ∈ {c_ℓ}` or `y_ℓ ∉ F̃_ℓ`; for light ℓ in
fact `y_ℓ ∉ F̃_ℓ` (if `c_ℓ ∉ F̃_ℓ` then `y_ℓ = c_ℓ`). If `y_{T_C} = a_C`
with `top(C) = ℓ`, then `z = y_{T_C∖ℓ}` lies in `Π{c_i, y_i}`, so
`y_ℓ ∈ F̃_ℓ`; hence ℓ is heavy. At a heavy ℓ, `y_ℓ = c_ℓ ~ ν_ℓ` is
independent of the past, and the patterns completed by `y` at ℓ form a
subset of `F̃_ℓ`, so the hit probability is `≤ p̃_ℓ`.
2. If ℓ is light, `P(y_ℓ = a | past) = ν_ℓ(a)1{a∉F̃} + p̃_ℓ ν_ℓ(a)1{a∉F̃}/(1−p̃_ℓ)
= ν_ℓ(a)1{a∉F̃}/(1−p̃_ℓ)`. The bound for `y_S` follows by the chain rule,
taking conditional expectations from the last element of S downwards
(the coordinates outside S integrate to 1). ∎

**Interpolation coins.** Fix a path ω. For `ρ ∈ {0,1}^V` put

    y^ρ_ℓ = y_ℓ   if ℓ ∈ R and ρ_ℓ = 1,      y^ρ_ℓ = c_ℓ   otherwise.

So `y^0 = c` and `y^1 = y`. The point of the phantom activations is that
**R does not depend on ρ**: it is a function of ω alone, because `F̃_ℓ`
uses both `c_i` and `y_i`.

**Lemma 2.2 (locality; PROVED).** For fixed ω and a d-local `f ≥ 0`, the
function `g_ω(ρ) = f(y^ρ)` is nonnegative and multilinear of degree ≤ d in
`ρ_R`, and does not depend on `ρ_{V∖R}`.

*Proof.* `y^ρ_ℓ` depends on `ρ_ℓ` only. So `f_T(y^ρ_T)` is a function of
`ρ_{T∩R}`, and `|T| ≤ d`. ∎

**Lemma 2.3 (binomial extrapolation; PROVED).** Let `n ≥ 0`, `0 < t ≤ 1/4`,
`d ≥ 0`, and let `g ≥ 0` on `{0,1}^n` be multilinear of degree ≤ d. Then
`g(1,…,1) ≤ B(n,t,d) · E_{ρ~Bern(t)^n} g(ρ)`, where

    B(n,t,d) = min_Y max_{y∈Y} |ℓ^Y_y(n)| / ψ(y),   ψ = Bin(n,t),

over node sets `Y ⊆ {0,…,n}` with `|Y| = min(d,n)+1`, `ℓ^Y_y` the Lagrange
basis. Moreover

    log B(n,t,d) ≤ d·log(4e³(n+1)/t) + ½ log(16nt + 16).            (2.1)

*Proof.* Average g over `Sym(n)`. This changes neither `g(1)` nor the
`Bern(t)^n` mean, and the average is `Q(K)`, `K = Σρ_i`, with Q a polynomial
of degree ≤ d (the average of `ρ^S` is `C(K,|S|)/C(n,|S|)`), `Q ≥ 0` on
`{0..n}`. Lagrange interpolation at Y gives
`Q(n) = Σ_y ℓ_y(n)Q(y) ≤ max_y(|ℓ_y(n)|/ψ(y))·Σ_y ψ(y)Q(y) ≤ B·E Q(K)`.
(2.1) is proved in §3. ∎

**Lemma 2.4 (thinned law; PROVED).** Fix `M₀ ≥ 4`, put
`t(ω) = 1/(M(ω) + M₀)` and `W(ω) = (1 + M(ω)/M₀)^{−4/3}`. Let τ be the law
of `y^ρ` when ω is drawn from the process and, given ω, `ρ ~ Bern(t(ω))^V`.
Then for every x,

    E_ω[ W(ω) · P_ρ(y^ρ = x | ω) ] ≤ ν(x).

*Proof.* Let `M_{≤ℓ} = Σ_{i≤ℓ, i light} p̃_i`, which is known before ℓ is
drawn, and `t_ℓ = 1/(M_{≤ℓ} + M₀) ≥ t(ω)`. Since at a replaced ℓ the two
events `c_ℓ = x_ℓ` and `y_ℓ = x_ℓ` cannot both hold (`c_ℓ ∈ F̃`, `y_ℓ ∉ F̃`),

    P_ρ(y^ρ = x | ω) ≤ Π_ℓ φ_ℓ,   φ_ℓ = 1{c_ℓ = x_ℓ} + t_ℓ 1{ℓ ∈ R, y_ℓ = x_ℓ}.

Given the past, `c_ℓ` and the fresh draw are independent, so
`E[φ_ℓ | past] ≤ ν_ℓ(x_ℓ) + t_ℓ p̃_ℓ ν_ℓ(x_ℓ)/(1−p̃_ℓ) ≤ ν_ℓ(x_ℓ) D_ℓ`, with
`D_ℓ = 1 + (4/3) t_ℓ p̃_ℓ 1{ℓ light}` known before ℓ. Hence
`Z = Π_ℓ φ_ℓ/(ν_ℓ(x_ℓ)D_ℓ)` has `E Z ≤ 1` (a product of adapted factors
with conditional means ≤ 1). Pathwise,
`log Π D_ℓ ≤ (4/3)Σ_ℓ p̃_ℓ/(M_{≤ℓ}+M₀) ≤ (4/3)∫_0^M dx/(x+M₀)`, so
`W·Π D_ℓ ≤ 1`. Therefore `E[W Π φ_ℓ] = ν(x) E[W Z Π D_ℓ] ≤ ν(x)`. ∎

**Theorem 2.5 (weighted k-ary comparison; PROVED).** In the setting of §1,
for every d-local `f ≥ 0`,

    E_ν f ≥ E_ω[ e^{−Φ(ω)} f(y) ],
    Φ(ω) = log B(n(ω), t(ω), d) + (4/3) log(1 + M(ω)/M₀),

with `t(ω) = 1/(M(ω)+M₀)`, `M₀ ≥ 4`. Consequently, by (2.1) and Jensen,

    E_ω Φ ≤ d·log(4e³(E n + 1)(E M + M₀)) + ½log(16 E n + 16) + (4/3)log(1 + E M/M₀),

and `E n = E M` (each light ℓ is replaced with conditional probability
`p̃_ℓ`).

*Proof.* By Lemmas 2.2 and 2.3 with `t = t(ω)`,
`f(y) = g_ω(1_R) ≤ B(n,t,d) E_ρ g_ω(ρ)`. Multiply by `W(ω)` and take
`E_ω`: `E_ω[e^{−Φ} f(y)] ≤ E_ω[W E_ρ f(y^ρ)] = Σ_x f(x) E_ω[W P(y^ρ = x|ω)]
≤ Σ_x f(x)ν(x)` by Lemma 2.4 and `f ≥ 0`. For the moment bound,
`log B ≤ d log(4e³(n+1)(M+M₀)) + ½log(16n/(M+M₀)·… )`; use (2.1) with
`nt ≤ n`, and concavity of log. ∎

The unweighted form follows when M and n are bounded: if `M ≤ M̄` and
`n ≤ n̄` on every path, then by (2.1)
`log(E_σ̃ f/E_ν f) ≤ d·log(4e³(n̄+1)(M̄+M₀)) + ½log(16n̄+16) + (4/3)log(1+M̄/M₀)`,
i.e. `≪ d log(2+M̄) + log(2+n̄)` when `n̄ ≍ M̄`. This is the shape of ETw
Conjecture 6.4, for σ̃ in place of σ. The weighted form is stronger and
is what §4 uses: it needs no bound on M, only its mean.

`scripts/kary_check.py` tests Theorem 2.5 by exact LP on 100 random small
systems (unary, binary and ternary patterns, d ≤ 3, up to 8 coordinates,
every path of the process enumerated). The weighted LP value is always
≤ 1, as the theorem requires, with the optimal one-dimensional constant
`B*` in Φ (`B* ≤ B`, so this is a stronger test). EVIDENCE only; the proof
is above.

## 3. Proof of (2.1)

If `d = 0`, Q is constant and `B = 1`. Let `d ≥ 1`, `m₀ = nt ≤ n/4`.

*(i) n ≤ d.* Take `Y = {0,…,n}`. Then `ℓ_y(n) = 1{y = n}` and
`B ≤ 1/ψ(n) = t^{−n} ≤ t^{−d}`.

*(ii) n > d, m₀ ≤ 2d.* Take `Y = {0,…,d}`. Then
`|ℓ_i(n)| ≤ n^d/(i!(d−i)!)`. Also `C(n,i) ≥ (n/i)^i ≥ n^i/(i! e^i)` and
`(1−t)^{n} ≥ e^{−1.151 m₀} ≥ e^{−2.31d}` (as `t ≤ 1/4`). So

    |ℓ_i(n)|/ψ(i) ≤ n^{d−i} e^{i} e^{2.31d}/((d−i)! t^i) ≤ (e^{3.31} n/t)^d.

*(iii) m₀ > 2d.* Put `h = ⌊√(m₀/d)⌋ ≥ 1` (so `h ≥ ½√(m₀/d)`) and
`y_i = ⌈m₀⌉ − ⌊dh/2⌋ + ih`, `0 ≤ i ≤ d`. Then
`|y_i − m₀| ≤ dh/2 + 3/2 ≤ ½√(dm₀) + 3/2`. Since `√(dm₀) < m₀/√2`, every
node lies in `[0.64m₀, 1.36m₀ + 1.5] ⊆ [1, n−1]` (note `n ≥ 4m₀ > 8`), and
`8y_i ≤ 22m₀`. Using `m₀ > 2d ≥ 2`,
`(4/3)(y_i−m₀)²/m₀ ≤ (4/3)(d/4 + 1.5√(d/m₀) + 2.25/m₀) ≤ d/3 + 2.92`,
so ET Lemma 2.1 gives `ψ(y_i) ≥ (22m₀)^{−1/2} e^{−d/3 − 2.92}`. Next,

    |ℓ_i(n)| = Π_{j≠i}|n−y_j| / (h^d i!(d−i)!) ≤ (2n)^d/(h^d d!) ≤ (2en/(dh))^d ≤ (4e√(n/(td)))^d.

So `log B ≤ (d/2)log(16e²n/(td)) + d/3 + 2.92 + ½log(22m₀)`.

In cases (i), (ii) the bound is visibly at most (2.1), since
`e^{3.31} < 4e³`. In case (iii), (2.1) minus the bound is at least
`d(2 + ½log(nd/t) − 1/3) − 2.92 − ½log(22/16) ≥ (5/3 + ½log 36) − 3.08 > 0`,
using `n ≥ 9`, `t ≤ 1/4`, `d ≥ 1`. ∎

Case (iii) is the sharp regime: the main term is `(d/2)log(n/(td))`, half
of (2.1). `scripts/kary_b21_check.py` evaluates the three node sets exactly
(log-space) on 7128 triples `(n,t,d)`, `n ≤ 10⁵`, `t ≥ 10⁻⁴`, `d ≤ 12`. The
largest value of `log B − (2.1)` is −5.66. It also confirms `B* ≤ B` against
the LP optimum for small n.
