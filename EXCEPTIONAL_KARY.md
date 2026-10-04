# EXCEPTIONAL_KARY — the k-ary comparison inequality (task O7)

Status: **checkpoint (awaiting parent review; one internal hostile review, O7-1, applied).** Labels follow `DISCOVERIES.md`. PROVED means proved
here and checked internally only. Notation follows `EXCEPTIONAL_TWIN.md`
(ETw), `EXCEPTIONAL_THETA.md` (ET).

## 0. Summary

| item | statement | label |
|---|---|---|
| §1 | coupled sequential process `(c, y)`: draw `c_ℓ ~ ν_ℓ`; at a light ℓ with `c_ℓ` activated, replace it by a fresh draw off the activated set. The law of y is ETw's sequential σ | definition |
| Lemma 2.1 | σ avoids every pattern with a light top; conditional densities `≤ (1−δ)^{−1}` | PROVED (standard) |
| Lemma 2.2 | on a frozen path, `ρ ↦ f(y^ρ)` (replace on `{ρ=1}∩R`) has degree ≤ d | PROVED |
| Lemma 2.3, (2.1), (3.1) | binomial extrapolation `g(1) ≤ B(n,t,d)·E_{Bern(t)} g` for nonneg degree-d g; explicit bounds | PROVED |
| Lemma 2.4 | thinned law vs ν, with weight `exp(−(4/3)tM)` | PROVED |
| **Thm 2.5** | **k-ary comparison for σ, any arity, no incident-weight hypothesis:** `E_ν f ≥ E[e^{−Φ}f(y)]`, `Φ = log B(n,t,d) + (4/3)tM` | PROVED |
| Cor 2.6 | mean cost `≤ d log(C₀(E M + 4d)/d) + O(d)` | PROVED |
| Remark 2.8 | the *unweighted* mean-mass comparison is false without incident-weight bounds (example) | PROVED |
| Thm 4.1 | sequential sieve limit with random step costs (S_w) | PROVED |
| Lemmas 4.2, 4.3 | inflation, moments, leak: ETw Lemmas 2.2, 2.6, 4.0, 2.1′ apply verbatim | PROVED |
| **Thm 4.5** | **`S_λ ≪_B λ^{3/4}` for every family of ℛ(M)-classes with `M ≤ P(M)^{1+B}`, twins/prime powers/any shape, unconditionally** | PROVED |
| ETw Conj 6.4, unweighted form | — | OPEN, no longer needed (§5) |
| ETw Conj 4.5_r (H_MS form) | — | OPEN, not needed for 3/4 |
| `kary_check.py` | Thm 2.5 by exhaustive enumeration + LP, 100 random systems (unary/binary/ternary): weighted value ≤ 1 | EVIDENCE |

ETw Conjecture 6.4 asks for a k-ary analogue of ET Prop 2.4 for the
sequential law σ. We prove it in a **weighted** form (Theorem 2.5): the
step cost is a random variable whose *mean* is
`d(O(1) + log⁺(E M/d))`, E M the mean activated mass. The proof needs no
incident-weight hypothesis, no Markov removal and no sparsity. Its
ingredients are a coupling of σ with ν, extrapolation in independent
replacement coins on a frozen path, and a one-dimensional extrapolation
lemma for binomial laws. Since the sequential sieve limit accepts random
step costs (Theorem 4.1), only first moments of the block masses enter.
Consequence (Theorem 4.5): **the 3/4 cap holds for all bounded-B
ℛ(M)-families, twin moduli included, with no hypothesis and no `log λ`.**
The unweighted form of Conj 6.4 stays open; without its incident-weight
hypothesis it is false (Remark 2.8).

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

**The coupled sequential process.** Coordinates are processed in order;
the state before ℓ is `(c_i, y_i)_{i<ℓ}`. An **activation rule** assigns
to each state a set `F_ℓ ⊆ Ω_ℓ` (so `F_ℓ` is known before ℓ is drawn);
`p_ℓ = ν_ℓ(F_ℓ)`. Draw `c_ℓ ~ ν_ℓ` independently of the past. Call ℓ
**light** if `p_ℓ ≤ δ_ℓ`.
* If ℓ is light and `c_ℓ ∈ F_ℓ` (ℓ is **replaced**, ℓ ∈ R), draw `y_ℓ`
  from `ν_ℓ(· | Ω_ℓ ∖ F_ℓ)`, independently of `c_ℓ`.
* Otherwise `y_ℓ = c_ℓ`.

Two rules matter.
* **Plain** (the law σ of ETw Conj 6.4 and Lemma 2.1′):
  `F_ℓ = F_ℓ(y_{<ℓ}) = {a : ∃C, top(C) = ℓ, (y_{T_C∖ℓ}, a) = a_C}`.
  The law of y is σ; the c's are an explicit coupling with ν.
* **Phantom:** `F̃_ℓ = {a : ∃C, top(C) = ℓ, ∃z ∈ Π_{i∈T_C∖ℓ}{c_i, y_i}, (z,a) = a_C}`.
  (An earlier draft used this rule; review O7-1 observed that §2 never
  needs it. It is kept only as a remark.)

Write `ω = (c, y)` for the whole path, `M(ω) = Σ_{ℓ light} p_ℓ` (the
light activated mass) and `n(ω) = |R|`. The law of y is written σ.

## 2. The comparison theorem

**Lemma 2.1 (avoidance, inflation; PROVED).** For any activation rule:
1. *(plain and phantom rules)* if `top(C) = ℓ` is light then
   `y_{T_C} ≠ a_C`. Hence `y ∉ 𝒜` only through heavy tops, and
   `P(y ∉ 𝒜) ≤ Σ_ℓ E[p_ℓ 1{p_ℓ > δ_ℓ}]`.
2. Given the state before ℓ, `y_ℓ ~ ν_ℓ(·|Ω_ℓ∖F_ℓ)` if ℓ is light and
   `y_ℓ ~ ν_ℓ` otherwise. In particular, for every `S ⊆ V` and `b ∈ Ω_S`,
   `σ(y_S = b) ≤ Π_{ℓ∈S}(1−δ_ℓ)^{−1} ν(b)`.

*Proof.* 1. For light ℓ, `y_ℓ ∉ F_ℓ` (if `c_ℓ ∉ F_ℓ` then `y_ℓ = c_ℓ`).
Both rules contain `F_ℓ(y_{<ℓ})`, so a completion of C by y at a light top
is impossible. At a heavy ℓ, `y_ℓ = c_ℓ ~ ν_ℓ` is independent of the past
and the completed patterns lie in `F_ℓ(y_{<ℓ}) ⊆ F_ℓ`.
2. If ℓ is light, `P(y_ℓ = a | past) = ν_ℓ(a)1{a∉F_ℓ} + p_ℓ ν_ℓ(a)1{a∉F_ℓ}/(1−p_ℓ)
= ν_ℓ(a)1{a∉F_ℓ}/(1−p_ℓ)`. The bound for `y_S` follows by the chain rule,
taking conditional expectations from the last element of S downwards
(the coordinates outside S integrate to 1). ∎

**Interpolation coins.** *Freeze* a whole path ω. For `ρ ∈ {0,1}^V` put

    y^ρ_ℓ = y_ℓ   if ℓ ∈ R and ρ_ℓ = 1,      y^ρ_ℓ = c_ℓ   otherwise.

So `y^0 = c` and `y^1 = y`. R is a function of the frozen path, not of ρ;
the intermediate points `y^ρ` need not be paths of the process, and nothing
below requires them to be.

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
basis, for `d ≥ 1`; and `B(n,t,0) := 1` (for d = 0, g is constant). Moreover

    log B(n,t,d) ≤ d·log(4e³(n+1)/t) + ½ log(16nt + 16).            (2.1)

*Proof.* Average g over `Sym(n)`. This changes neither `g(1)` nor the
`Bern(t)^n` mean, and the average is `Q(K)`, `K = Σρ_i`, with Q a polynomial
of degree ≤ d (the average of `ρ^S` is `C(K,|S|)/C(n,|S|)`), `Q ≥ 0` on
`{0..n}`. Lagrange interpolation at a minimising Y gives
`Q(n) = Σ_y ℓ_y(n)Q(y) ≤ max_y(|ℓ_y(n)|/ψ(y))·Σ_y ψ(y)Q(y) ≤ B·E Q(K)`.
(2.1) is proved in §3. ∎

**Lemma 2.4 (thinned law; PROVED).** Fix `t ∈ (0, 1/4]` and put
`W(ω) = exp(−(4/3) t M(ω))`. Let τ be the law of `y^ρ` when ω is drawn
from the process and, given ω, `ρ ~ Bern(t)^V`. Then for every x,

    E_ω[ W(ω) · P_ρ(y^ρ = x | ω) ] ≤ ν(x).

*Proof.* At a replaced ℓ the events `c_ℓ = x_ℓ` and `y_ℓ = x_ℓ` cannot
both hold (`c_ℓ ∈ F_ℓ ∌ y_ℓ`). Hence

    P_ρ(y^ρ = x | ω) ≤ Π_ℓ φ_ℓ,   φ_ℓ = 1{c_ℓ = x_ℓ} + t·1{ℓ ∈ R, y_ℓ = x_ℓ}.

Given the past, `c_ℓ` and the fresh draw are independent, so
`E[φ_ℓ | past] = ν_ℓ(x_ℓ) + 1{ℓ light}·t p_ℓ ν_ℓ(x_ℓ)1{x_ℓ∉F_ℓ}/(1−p_ℓ) ≤ ν_ℓ(x_ℓ)D_ℓ`
with `D_ℓ = 1 + (4/3)t p_ℓ 1{ℓ light}` (as `p_ℓ ≤ δ_ℓ ≤ 1/4`), which is
known before ℓ. So
`Z = Π_ℓ φ_ℓ/(ν_ℓ(x_ℓ)D_ℓ)` is a product of adapted factors with
conditional means ≤ 1, and `E Z ≤ 1` (if `ν(x) = 0` both sides vanish).
Pathwise `Π_ℓ D_ℓ ≤ exp((4/3)tM) = 1/W`. Therefore
`E[W Π φ_ℓ] = ν(x)·E[W Π D_ℓ · Z] ≤ ν(x)`. ∎

**Theorem 2.5 (weighted k-ary comparison; PROVED).** In the setting of §1,
for every `t ∈ (0, 1/4]` and every d-local `f ≥ 0`,

    E_ν f ≥ E_ω[ e^{−Φ(ω)} f(y) ],     Φ(ω) = log B(n(ω), t, d) + (4/3)·t·M(ω).

*Proof.* By Lemmas 2.2 and 2.3, `f(y) = g_ω(1_R) ≤ B(n,t,d)·E_ρ g_ω(ρ)`.
Multiply by `W(ω)/B(n,t,d)` and take `E_ω`:
`E_ω[e^{−Φ}f(y)] ≤ E_ω[W E_ρ f(y^ρ)] = Σ_x f(x)·E_ω[W P_ρ(y^ρ = x|ω)] ≤ E_ν f`
by Lemma 2.4 and `f ≥ 0`. ∎

**Corollary 2.6 (mean cost; PROVED).** Let `d ≥ 1`, let `m̄ ≥ E M` and take
`t = d/(m̄ + 4d)`. Then `E n = E M` and

    E_ω Φ ≤ d·log(C₀(m̄ + 4d)/d) + (4/3)d + ½log(22d + 22) + 3,   C₀ = 4e^{4.31}.

*Proof.* Each light ℓ is replaced with conditional probability `p_ℓ`, so
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
`Σ_{ℓ light} p_ℓ/(M_{≤ℓ}+M₀) ≤ log(1+M/M₀)`. The cost is then
`≈ d·log((n+1)(M+M₀))`, weaker by a log factor but with no choice of t.
The checks below use this variant.

**Remark 2.8 (weighted vs unweighted; review O7-1).** Theorem 2.5 bounds
`E[e^{−Φ}f(y)]`, and Corollary 2.6 bounds `EΦ`; neither bounds
`log(E_σ f/E_ν f)` by the *mean* mass, and no such bound holds in general.
Example (review): a trigger X with `P(X=1) = ε`, m coordinates `Z_i` with
`P(Z_i=1) = 1/4`, patterns `(X,Z_i) = (1,1)`, `μ = m/4`, `ε = 1/μ`. Every
activated set is light, `E M = εμ = 1`, but the 3-local
`f = X(ΣZ_i − μ)²` has `E_σ f/E_ν f = μ/(1−1/4) → ∞`. Here the incident
weight of `(X,1)` is `≈ 1`, so ETw Conj 6.4 (which assumes incident weights
`≤ θ₀`) is not contradicted. An unweighted bound does follow from pathwise
bounds: if `M ≤ M̄` and `n ≤ n̄` on every path, Theorem 2.5 gives
`log(E_σ f/E_ν f) ≤ sup_ω Φ`. The sieve application needs only the
weighted form, because Theorem 4.1 accepts random step costs.

`scripts/kary_check.py` tests Theorem 2.5 (constant `t = d/(EM+4d)`) and
Remark 2.7, for the plain and the phantom rule, on 100 random small
systems (unary, binary and ternary patterns, d ≤ 3, up to 8 coordinates).
Every path of the process is enumerated exhaustively; the LPs are solved
in floating point (HiGHS). The weighted LP value is always ≤ 1 (asserted
with tolerance 10⁻⁷), with the optimal one-dimensional constant `B*` in Φ
(`B* ≤ B`, so this is a stronger test). EVIDENCE only; the proof is above.
Outputs: `data/kary/check_*.txt`.

## 3. Proof of (2.1)

For `d = 0` see the definition. Let `d ≥ 1`, `m₀ = nt ≤ n/4`.

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

**Sequential step.** `V_j` a block whose primes satisfy `log ℓ > s`, so
λ-level functions are d-local with `d = ⌊λ/s⌋`. Given h, the patterns are
the classes with top prime in `V_j` whose requirements outside `V_j` are
met by h; their requirements inside `V_j` form a pattern on the block
coordinates (a residue class mod `ℓ^v` at ℓ is a union of single values of
`ℤ/ℓ^{E_ℓ}`, so cylinder patterns reduce to §1). `Π_j(h)` is the law of the
path ω of the plain rule in increasing order with `ν = U` and caps
`δ_ℓ = ℓ^{−1/2}`; `Y_j = y`; `Φ_j` is the Φ of Theorem 2.5 with
`t = t_j(h) = d/(E[M|h] + 4d)` (fixed before the block is drawn). (S_w) is
Theorem 2.5. The law of `Y_j` is exactly ETw's in-block sequential capped
law (Lemma 2.1′ with light/heavy decided by the total activated density,
as in ETw Conj 4.5_r and 6.4).

### 4.2 Inflation, moments, leak

Fix `B ≥ 0` and work in ETw §§2–4: QR base `R_W`, prime-power coordinates,
caps `δ_ℓ = ℓ^{−1/2}`, `Γ(m) = Π_{p|m}γ'(p)` with **`γ'(ℓ) = (1−ℓ^{−1/2})^{−1}`**
for `ℓ > W` (ETw Lemma 2.2; the decay `γ'(ℓ)−1 ≪ ℓ^{−1/2}` is what ETw
Lemma 2.6 needs). A sequential block `V` has its primes in
`(e^{s}, e^{2s}]`.

**Lemma 4.2 (PROVED).** With sequential steps in some blocks:
1. (inflation) ETw Lemma 2.2 holds for `Q'`;
2. (first moment) `E_{Q'} M_V ≤ Σ_{M: P(M)∈V} τ(A_M²)Γ(M)/M ≤ K(W,B)(2(1+B)s)³`,
   K as in ETw Lemma 2.6;
3. (second moment) `E_{Q'} p_ℓ² ≤ C(ε,B)(2+B)²ℓ^{−2+ε}` for every `ℓ > W`
   (ETw Lemma 4.0).

*Proof.* 1. Chain rule: by Lemma 2.1(2), given the past, `y_ℓ` has
density `≤ (1−δ_ℓ)^{−1}` w.r.t. U on `ℤ/ℓ^{E_ℓ}`. 2. A class with top ℓ,
`M = qℓ^v`, adds at most `ℓ^{−v}` to `p_ℓ`, and only if its requirement mod q is met
by the y-history; by 1 this has probability `≤ Γ(q)/q`; sum over `≤ τ(A_M²)`
values of D and over M (partial summation of ETw Lemma 2.6 over
`M ≤ e^{2(1+B)s}`). 3. The proof of ETw Lemma 4.0 uses only 1 (for lcm's of
cofactors) and the fact that p_ℓ is a density of classes decided at ℓ. ∎

**Lemma 4.3 (leak; PROVED).** In the block structure of Theorem 4.5, every
class is decided at its top prime, and
`𝔏 ≤ Σ_ℓ E[p_ℓ 1{p_ℓ > δ_ℓ}] ≪_B W^{−1/4}`. Hence `𝔏 ≤ 1/2` for
`W ≥ W₀(B)` (ETw convention after Cor 2.5).

*Proof.* In a sequential block, a class with light top is avoided and a
heavy top is hit with conditional probability `≤ p_ℓ` (Lemma 2.1(1)); this
is ETw Lemma 2.1′. Markov and Lemma 4.2(3) give
`Σ_{ℓ>W} ℓ^{1/2}·O_B(ℓ^{−7/4})`, as in ETw Cor 2.5. ∎

(With the phantom rule the same holds with extra factors `2^{r−1}` and
`4^{r−1}`, `r = ⌊2(1+B)⌋`, by bounding "met by some `z ∈ Π{c_i,y_i}`" by a
sum over letter choices; this is not needed.)

### 4.3 The cap

**Theorem 4.5 (PROVED).** Fix `B ≥ 0` and `W = W₀(B)`. There are
`λ₀(B)` and `C(B)` such that for every family 𝔊 of ℛ(M)-classes with
`M ≤ P(M)^{1+B}` (any shape: dominant, gapped, η-twin, prime-power top, any
number of primes at comparable scale), plus any W-smooth classes, every
majorant ν of level `λ ≥ λ₀(B)` satisfies

    log(1/Eν) ≤ C(B)·λ^{3/4}.

*Proof.* Put `s₁ = λ^{1/4}` (`λ₀` is such that `s₁ > 2 log W`). Blocks, in
increasing order of primes:
* singletons `{ℓ}`, `W < ℓ ≤ e^{s₁}` (ETw Prop 4.1);
* sequential blocks `V_i = {ℓ : 2^i s₁ < log ℓ ≤ 2^{i+1}s₁} ∩ (·, e^{λ/2}]`,
  `0 ≤ i ≤ I`, `2^I s₁ < λ/2`;
* one sequential block `(e^{λ/2}, e^λ]` (ETw Cor 4.3);
* singletons above `e^λ` (cost 0).
Every class is decided at its top prime, and `𝔏 ≤ 1/2` (Lemma 4.3).
Apply Theorem 4.1. Base: `O_B(1)` (ETw Lemma 1.3). Singletons:
`≤ (8/3)K'(1+B)³λ^{3/4}`. Top block: `2log(1+3e^{−λ/4})`.

Sequential block `V_i`, `s = 2^i s₁`, `d_i = ⌊λ/s⌋ ≥ λ/(2s) ≥ 1`. By
Corollary 2.6 applied for each h with `m̄ = E[M|h]`, then Jensen over h
(the map `m ↦ log(C₀(m+4d)/d)` is concave),

    E_{Q'}Φ_i ≤ d_i·log(C₀(E M_{V_i} + 4d_i)/d_i) + (4/3)d_i + ½log(22d_i+22) + 3.

By Lemma 4.2(2), `E M_{V_i} ≤ K₁(B)s³`, so
`(E M_{V_i} + 4d_i)/d_i ≤ 2K₁s⁴/λ + 4 = 2K₁·16^i + 4`. Hence
`E Φ_i ≤ (λ^{3/4}/2^i)(c₁(B) + 4i·log 2) + O(log λ)`, and

    2Σ_{i≥0} E Φ_i ≤ 2λ^{3/4} Σ_i 2^{−i}(c₁(B) + 2.78 i) + O(log²λ) ≪_B λ^{3/4}. ∎

**What this settles.** ETw §5 "Not covered" item 1 (unresolved moduli:
η-twin, prime-power top, ≥ 3 primes in a window, with top prime in
`(e^{λ^{1/4}}, e^{λ/2}]`) is removed. For every fixed B, every family of
ℛ(M)-classes with `M ≤ P(M)^{1+B}` has `S_λ ≪_B λ^{3/4}`, with no
hypothesis: Conjecture 4.5_r, Conjecture 6.4, Hyp K2, Prop 6.5's `log λ`,
the Markov removal (Lemma 6.3) and the windows' η are all unnecessary.
With ETw §5's reading of ET Lemma 2.9 (λ ≍ log N, the hypothesis needed
for every λ in the relevant range, which is automatic here since the
theorem has no family hypothesis beyond B), no such family yields an
exceptional-set exponent θ > 3/4.

**Still not covered** (unchanged from ETw §5): moduli with
`log M/log P(M)` unbounded (no summation over B; constants `W₀(B)`,
`C(B)` untracked); (a,D)- and Case-A classes mixed with ℛ(M)-classes (the
base, ETw Lemma 1.1, is proved for ℛ(M) only). Theorem 2.5 itself is
arithmetic-free, so for those families the open part is the base and the
moment lemmas, not the k-ary step.

## 5. Relation to ETw Conjecture 6.4, and what is left open

* **Conj 6.4 in its weighted form: PROVED, for the conjecture's own law σ.**
  Theorem 2.5 with the plain rule is the step inequality ETw §6 wanted, in
  the weak `d·log(mass)` form, with the mean mass and a random cost. ETw
  Prop 6.5 used Conj 6.4 only through Theorem 2.3′; Theorem 4.1 accepts the
  random cost, so Prop 6.5's conclusion holds without Conj 6.4, without
  Hyp K2 and without its `log λ` (Theorem 4.5).
* **Conj 6.4 in its unweighted form (`E_σ f ≤ e^{C(d log(2+μ)+1)}E_ν f`
  for all f, μ the total k-ary mass, incident weights `≤ θ₀`): OPEN.**
  Without the incident-weight hypothesis it is false (Remark 2.8). With it,
  Theorem 2.5 reduces it to a tail statement: a nonnegative d-local f must
  not concentrate the law σ on paths with `M ≫ μ` or `n ≫ μ`. This is no
  longer needed for the 3/4 question.
* **No incident-weight or sparsity hypothesis in Theorem 2.5.** Only the
  light caps `p_ℓ ≤ δ_ℓ ≤ 1/4` enter (the 4/3 factors and the leak). ETw's
  Markov removal (Lemma 6.3) and Hyp K2 are not used anywhere.
* **The earlier draft's "phantom" rule.** It was introduced to make the
  replaced set independent of the coins ρ. Review O7-1 observed that this
  is automatic once the whole path is frozen before interpolating: the
  intermediate points `y^ρ` need not be paths, and Lemma 2.4 uses only
  that each `F_ℓ` is known before ℓ and that the fresh draws are
  independent. The phantom rule is kept in §1 and in the checks as a
  variant; it is not used in §4.
* **Strength.** Cor 2.6 gives `d(O(1) + log⁺(E M/d))`, the weak form of
  ET Prop 2.4 with the mean mass. It is not the H_MS form of ETw Conj 4.5_r
  (a k-ary pattern costing `e^{−αΣs}`); that sharper statement is not
  needed for the 3/4 question and remains open.
* **Unary sanity check.** For unary patterns σ = ν conditioned off the
  forbidden sets at the light coordinates (heavy ones stay unconditioned),
  and Theorem 2.5 reproves ET Prop 2.4 in a weak single-band form (cost
  `≈ d log(μ/d)` against ET's `(d/2)log(μ/d)` plus band terms), by a
  different route: extrapolation in replacement coins on the hit set of an
  unconditioned draw, instead of thinning and symmetrisation of the hit
  indicators.
* In the brute-force LPs, `log C*` (unweighted, informational) for the
  phantom and the plain law differ by at most 0.036 in absolute terms
  (relative differences up to ≈ 22% among values above 0.01); see
  `data/kary/`.

## Replay

```
# Theorem 2.5 / Remark 2.7, plain and phantom rules: exhaustive path enumeration + floating-point LP,
# asserts weighted value <= 1 (each run < 40 min, < 1 GB)
cd scripts
uv run --with scipy --with numpy python kary_check.py 30 1        > ../data/kary/check_sparse_seed1.txt
uv run --with scipy --with numpy python kary_check.py 40 2 dense  > ../data/kary/check_dense_seed2.txt
uv run --with scipy --with numpy python kary_check.py 30 3 graph  > ../data/kary/check_graph_seed3.txt
# (2.1) and (3.1) for the explicit node sets of §3, 7128 triples, asserted; d = 0 case (~1 min)
uv run --with scipy --with numpy python kary_b21_check.py
```
