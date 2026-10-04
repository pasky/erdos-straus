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

**Lemma 2.4 (thinned law; PROVED).** Fix `t ∈ (0, 1/4]` and put
`W(ω) = exp(−(4/3) t M(ω))`. Let τ be the law of `y^ρ` when ω is drawn
from the process and, given ω, `ρ ~ Bern(t)^V`. Then for every x,

    E_ω[ W(ω) · P_ρ(y^ρ = x | ω) ] ≤ ν(x).

*Proof.* At a replaced ℓ the events `c_ℓ = x_ℓ` and `y_ℓ = x_ℓ` cannot
both hold (`c_ℓ ∈ F̃_ℓ ∌ y_ℓ`). Hence

    P_ρ(y^ρ = x | ω) ≤ Π_ℓ φ_ℓ,   φ_ℓ = 1{c_ℓ = x_ℓ} + t·1{ℓ ∈ R, y_ℓ = x_ℓ}.

Given the past, `c_ℓ` and the fresh draw are independent, so
`E[φ_ℓ | past] = ν_ℓ(x_ℓ) + t p̃_ℓ ν_ℓ(x_ℓ)1{x_ℓ∉F̃_ℓ}/(1−p̃_ℓ) ≤ ν_ℓ(x_ℓ)D_ℓ`
with `D_ℓ = 1 + (4/3)t p̃_ℓ 1{ℓ light}`, which is known before ℓ. So
`Z = Π_ℓ φ_ℓ/(ν_ℓ(x_ℓ)D_ℓ)` is a product of adapted factors with
conditional means ≤ 1, and `E Z ≤ 1` (if `ν(x) = 0` both sides vanish).
Pathwise `Π_ℓ D_ℓ ≤ exp((4/3)tM) = 1/W`. Therefore
`E[W Π φ_ℓ] = ν(x)·E[W Π D_ℓ · Z] ≤ ν(x)`. ∎

**Theorem 2.5 (weighted k-ary comparison; PROVED).** In the setting of §1,
for every `t ∈ (0, 1/4]` and every d-local `f ≥ 0`,

    E_ν f ≥ E_ω[ e^{−Φ(ω)} f(y) ],     Φ(ω) = log B(n(ω), t, d) + (4/3)·t·M(ω).

*Proof.* By Lemmas 2.2 and 2.3, `f(y) = g_ω(1_R) ≤ B(n,t,d)·E_ρ g_ω(ρ)`.
Multiply by `W(ω)` and take `E_ω`:
`E_ω[e^{−Φ}f(y)] ≤ E_ω[W E_ρ f(y^ρ)] = Σ_x f(x)·E_ω[W P_ρ(y^ρ = x|ω)] ≤ E_ν f`
by Lemma 2.4 and `f ≥ 0`. ∎

**Corollary 2.6 (mean cost; PROVED).** Let `d ≥ 1`, let `m̄ ≥ E M` and take
`t = d/(m̄ + 4d)`. Then `E n = E M` and

    E_ω Φ ≤ d·log(C₀(m̄ + 4d)/d) + (4/3)d + ½log(22d + 22) + 3,   C₀ = 4e^{4.31}.

*Proof.* Each light ℓ is replaced with conditional probability `p̃_ℓ`, so
`E n = E M`. §3 gives, in all cases,
`log B(n,t,d) ≤ d·log(C₁·max(1/t, √(n/(td)))) + ½log(22nt + 22) + 3`, `C₁ = 2e^{4.31}` (3.1).
Bound the max by the sum, use concavity of `log`, `√·` and Jensen:
`E log B ≤ d log(C₁(1/t + √(E n/(td)))) + ½log(22tE n + 22) + 3`.
With this t, `1/t = (m̄+4d)/d`, `√(E n/(td)) ≤ (m̄+4d)/d`, `t E n ≤ d`, and
`(4/3)t E M ≤ (4/3)d`. ∎

So the cost is `d(O(1) + log⁺(E M/d))`, the form of ET Prop 2.4 / EB
Thm 2.5 for unary systems, now for any arity and with only the *mean* mass.

**Remark 2.7 (scale-free variant).** One may also take the path-dependent
`t(ω) = 1/(M(ω)+M₀)`, `M₀ ≥ 4`, with weight `(1+M/M₀)^{−4/3}`: in the
proof of Lemma 2.4 use `t_ℓ = 1/(M_{≤ℓ}+M₀) ≥ t(ω)`, where `M_{≤ℓ}` is the
light mass up to and including ℓ, and
`Σ_ℓ p̃_ℓ/(M_{≤ℓ}+M₀) ≤ log(1+M/M₀)`. The cost is then
`≈ d·log((n+1)(M+M₀))`, weaker by a log factor but with no choice of t.
The checks below use this variant.

The unweighted form follows when M and n are bounded: if `M ≤ M̄` and
`n ≤ n̄` on every path, then by (2.1)
`log(E_σ̃ f/E_ν f) ≤ d·log(4e³(n̄+1)(M̄+M₀)) + ½log(16n̄+16) + (4/3)log(1+M̄/M₀)`,
i.e. `≪ d log(2+M̄) + log(2+n̄)` when `n̄ ≍ M̄`. This is the shape of ETw
Conjecture 6.4, for σ̃ in place of σ. The weighted form is stronger and
is what §4 uses: it needs no bound on M, only its mean.

`scripts/kary_check.py` tests Theorem 2.5 (constant t = d/(EM+4d)) and Remark 2.7 by exact LP on 100 random small
systems (unary, binary and ternary patterns, d ≤ 3, up to 8 coordinates,
every path of the process enumerated). The weighted LP value is always
≤ 1, as the theorem requires, with the optimal one-dimensional constant
`B*` in Φ (`B* ≤ B`, so this is a stronger test). EVIDENCE only; the proof
is above. Outputs: `data/kary/check_*.txt`.

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

**The unified form (3.1).** `log B(n,t,d) ≤ d·log(C₁·max(1/t, √(n/(td)))) + ½log(22nt+22) + 3`,
`C₁ = 2e^{4.31}`. In case (i), `t^{−d}`. In case (iii), the bound above is
`d·log(4e^{4/3}√(n/(td))) + 2.92 + ½log(22m₀)`. In case (ii) use `n ≤ 2d/t`:
`n^{d−i}/(d−i)! ≤ (2d)^{d−i}t^{−(d−i)}/(d−i)! ≤ (2e)^d t^{−(d−i)}` (the map
`x ↦ (2ed/x)^x` increases on `(0, d]`), so every ratio is `≤ (2e^{4.31}/t)^d`.

Case (iii) is the sharp regime: the main term is `(d/2)log(n/(td))`, half
of (2.1). `scripts/kary_b21_check.py` evaluates the three node sets exactly
(log-space) on 7128 triples `(n,t,d)`, `n ≤ 10⁵`, `t ≥ 10⁻⁴`, `d ≤ 12`. The
largest value of `log B − (2.1)` is −5.66. It also confirms `B* ≤ B` against
the LP optimum for small n.

## 4. Application: the 3/4 cap for all ℛ(M)-families with M ≤ P(M)^{1+B}

### 4.1 Sequential steps with random costs

**Theorem 4.1 (weighted abstract sequential sieve limit; PROVED).** Take
the setting of ETw Theorem 2.3′ (base `Q₀`, R with (R1)–(R2), coordinates
`y_ℓ = n mod ℓ^{E_ℓ}`, ordered blocks `V_1,…,V_J`). Suppose that for each
block j and history h there are an auxiliary probability law `Π_j(h)` on
paths ω, a map `ω ↦ Y_j(h,ω) ∈ Ω_{V_j}` and a cost `Φ_j(h,ω) ≥ 0` with

* (S_w) for every λ-level `f ≥ 0` on `Ω_{V_j}`:
  `E_U f ≥ E_{ω~Π_j(h)}[ e^{−Φ_j(h,ω)} f(Y_j(h,ω)) ]`.

Let `Q'` be the law of the history built from the base (uniform on R) by
drawing, at each block, `ω_j ~ Π_j(H_{<j})` and appending `Y_j`. If
`𝔏 = Q'(final history ∉ 𝒜) ≤ 1/2`, every majorant ν of level λ satisfies

    log(1/Eν) ≤ log(Q₀/|R|) + log 2 + 2 Σ_j E_{Q'} Φ_j(H_{<j}, ω_j).

*Proof.* Let `g_j(h) = E_U[ν | H_{<j} = h]`. We show by downward induction
`g_j(h) ≥ E_{Q'}[1_𝒜 e^{−Σ_{i≥j}Φ_i} | H_{<j} = h]`. For `j = J+1` this is
`g_{J+1} ≥ 1_𝒜`. Given h, `f(y) = g_{j+1}(h,y)` is λ-level and `≥ 0`
(ETw Theorem 2.3′ proof). By (S_w) and the induction hypothesis at
`(h, Y_j)`,
`g_j(h) ≥ E_ω[e^{−Φ_j} E_{Q'}[1_𝒜 e^{−Σ_{i>j}Φ_i} | H_{<j+1} = (h,Y_j)]]`.
Under `Q'` the blocks after j depend on `ω_j` only through `Y_j`, so the
right side is the claim at j. The conclusion is the Jensen step of ETw
Theorem 2.3, with `S = Σ_jΦ_j ≥ 0`. ∎

Every step (S) of ETw is an (S_w) with a deterministic cost. The new
instance is:

**Phantom step.** `V_j` a block whose primes satisfy `log ℓ > s`, so
λ-level functions are d-local with `d = ⌊λ/s⌋`. Given h, the patterns are
the classes with top prime in `V_j` whose requirements outside `V_j` are
met by h; their requirements inside `V_j` form a pattern on the block
coordinates (a residue class mod `ℓ^v` at ℓ is a union of single values of
`ℤ/ℓ^{E_ℓ}`, so cylinder patterns reduce to §1). `Π_j(h)` is the law of the
phantom-sequential path ω in increasing order with `ν = U` and caps
`δ_ℓ = ℓ^{−1/2}`, `Y_j = y`, and `Φ_j` is the Φ of Theorem 2.5 with
`t = t_j(h) = d/(E[M|h] + 4d)`. (S_w) is Theorem 2.5.
