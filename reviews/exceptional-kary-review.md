# Hostile review: EXCEPTIONAL_KARY.md (task O7), commit 666598b

Reviewer: side-agent/review-kary. Scope: Thm 2.5 (Lemmas 2.1–2.4, Cor 2.6),
§3 constants, Thm 4.1, Lemmas 4.2–4.3, Thm 4.5 (headline). Independent
brute-force code: `scripts/review_kary_bruteforce.py` (written from scratch,
not derived from `kary_check.py`), output `data/kary/review_bruteforce.txt`.

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects numbered D1, D2, …

## Items

### 1. Lemma 2.2 (locality) and the symmetrisation of Lemma 2.3 — SOUND

* On a frozen ω, `y^ρ_ℓ ∈ {c_ℓ, y_ℓ}` depends on `ρ_ℓ` alone (and only for
  ℓ ∈ R). Hence each `f_T(y^ρ_T)` is a function of `ρ_{T∩R}`, `|T∩R| ≤ d`,
  i.e. multilinear of degree ≤ d. No sign condition on the `f_T` is needed
  (majorant terms have real coefficients `a_i`; only `f = Σ f_T ≥ 0` is
  used, and `g_ω ≥ 0` pointwise because `y^ρ` is a point of `Ω_V`).
  Locality is in the right coordinates: replacement is coordinatewise, so
  T-dependence stays T-dependence. The worry "is f still d-local after
  replacement" does not arise: R is frozen and `ρ_ℓ` touches only `y^ρ_ℓ`.
* Symmetrisation: averaging `g∘π` over `Sym(R)` fixes `g(1_R)` (the
  all-ones corner is permutation-invariant) and the `Bern(t)^R` mean
  (exchangeable law); it preserves nonnegativity (average of nonnegative
  functions) and degree (`avg ρ^S = C(K,|S|)/C(n,|S|)`). The resulting
  `Q(K)` is ≥ 0 on `{0..n}` and has degree ≤ min(d, n) on that set.
* Lagrange step: `Q(n) = Σ_y ℓ_y(n)Q(y) ≤ Σ|ℓ_y(n)|Q(y) ≤ max(|ℓ_y(n)|/ψ(y))·Σ_{k}ψ(k)Q(k)`
  uses `Q ≥ 0` at all k (nodes and non-nodes). Direction is right: it upper
  bounds the corner value `f(y)` (σ side) by the bulk mean (thinned side).
  `B ≥ 1` always (`Σℓ_y(n) = 1`, `Σψ ≤ 1`), so `Φ ≥ 0` as Thm 4.1 needs.

### 2. Lemma 2.3 constant, (2.1), (3.1), §3 — SOUND

* Used at the right point and in the right direction: Thm 2.5 needs an
  upper bound on the corner `g(1_R) = f(y)` (σ-side value) by the
  `Bern(t)` bulk (thinned side, which Lemma 2.4 then dominates by ν). That
  is exactly what Lemma 2.3 gives. No lower bound on `E_σ f` is ever needed.
* Checked by hand: case (ii) (`C(n,i) ≥ n^i/(i!e^i)`, `(1−t)^n ≥ e^{−1.151nt}`
  for `t ≤ 1/4`), case (iii) (`|ℓ_i(n)| ≤ (2en/(dh))^d`, `h ≥ ½√(m₀/d)`
  ⇒ `≤ (4e√(n/(td)))^d`), and the passage to (3.1) in all three cases.
  The case-(ii) step `n^{d−i}/(d−i)! ≤ (2e)^d t^{−(d−i)}` uses `n ≤ 2d/t`; fine.
* Independent numerics (`scripts/review_kary_B_check.py`): for
  `n ≤ 14`, `t ∈ {.01,.03,.1,.2,.25}`, `d ≤ 4`: LP optimum `B* ≤` Lagrange-min
  B (ratio max 1.0, equality when n ≤ d), `max(log B − (2.1)) = −6.47`,
  `max(log B − (3.1)) = −8.95`. Random nonnegative degree-d multilinear g
  (literal products and squares), 3000 draws, `n ≤ 9`:
  `max g(1)/(B*·E g) = 1.0000000000000004` (tight, never exceeded).
* Cor 2.6's Jensen: `x ↦ log(a + √(bx))` and `x ↦ log(22tx+22)` are concave,
  `E n = E M` is exact (each light ℓ is replaced w.p. `p_ℓ` given the past).
  SOUND.

### 3. Lemma 2.4 (thinned law, supermartingale) — SOUND

* `P_ρ(y^ρ_ℓ = x_ℓ | ω) = (1−t)1{c_ℓ=x_ℓ} + t1{y_ℓ=x_ℓ} ≤ φ_ℓ` holds even
  without the disjointness remark. The filtration is `𝒢_ℓ = σ(c_i, y_i : i ≤ ℓ)`.
  `F_ℓ`, `p_ℓ`, "light", `D_ℓ` are `𝒢_{ℓ−1}`-measurable; `c_ℓ` and the
  fresh draw are independent of `𝒢_{ℓ−1}`. So
  `E[φ_ℓ | 𝒢_{ℓ−1}] = ν_ℓ(x_ℓ) + t·1{light}·p_ℓ·ν_ℓ(x_ℓ)1{x_ℓ∉F_ℓ}/(1−p_ℓ) ≤ ν_ℓ(x_ℓ)D_ℓ`.
* Reviewer's question (3), "is '`F_ℓ` known before ℓ' enough when activated
  sets depend on earlier *replaced* coordinates?": yes. The proof never
  needs the intermediate points `y^ρ` to be paths, nor R to be independent
  of anything; it needs only predictability of `F_ℓ` w.r.t. 𝒢, which holds
  for the plain rule (`F_ℓ = F_ℓ(h, y_{<ℓ})`), the phantom rule, and in fact
  for **any** rule `F_ℓ = F_ℓ(c_{<ℓ}, y_{<ℓ})`. The interpolation coins ρ
  are drawn after the whole path, so there is no feedback from ρ into R.
* t must be deterministic (not path-dependent) for `Π D_ℓ ≤ e^{(4/3)tM}`
  with the same t as in the corner bound. In §4, `t_j(h)` is a function of
  the block history only: fine. (Remark 2.7's path-dependent t is a separate
  argument; it is used only in the checks, not in §4. Not reviewed in detail.)
* Brute force: Lemma 2.4's inequality `max_x E[W P_ρ(y^ρ=x|ω)]/ν(x) ≤ 1`
  is asserted exactly (all paths, all ρ) in every run of item 6 below,
  including arbitrary full-state rules. No violation.

### 4. Theorem 2.5 assembly and Cor 2.6 — SOUND

* `f(y) = g_ω(1_R) ≤ B(n(ω),t,d)·E_ρ g_ω(ρ)` pathwise (items 1–2); multiply
  by `W(ω)/B(n(ω),t,d) = e^{−Φ(ω)}` (path-dependent, fine: it is a pathwise
  inequality); `E_ω[W E_ρ f(y^ρ)] = Σ_x f(x) E_ω[W P_ρ(y^ρ=x|ω)] ≤ Σ_x f(x)ν(x)`
  uses `f ≥ 0` and Lemma 2.4. No step needs `E_σ f` or a lower bound on it.
* What is proved is the **weighted** inequality `E_ν f ≥ E_ω[e^{−Φ}f(y)]`,
  not `E_ν f ≥ e^{−c}E_σ f`. The paper is explicit about this (Remark 2.8)
  and the counterexample there is correct (checked: `E_σ f/E_ν f = μ/(3/4)`,
  f has degree 3, all activations light at `p = δ = 1/4`).
* Cor 2.6: `t = d/(m̄+4d) ≤ 1/4`; `t·E n ≤ d`; `√(E n/(td)) ≤ (m̄+4d)/d`;
  `(4/3)tEM ≤ (4/3)d`. Correct.

### 5. Theorem 4.1 (random step costs) — SOUND

* Work on the enlarged space (history, ω_1, …, ω_J). Claim(j):
  `g_j(h) ≥ G_j(h) := E[1_𝒜 e^{−Σ_{i≥j}Φ_i} | H_{<j}=h]`. Step:
  `g_j(h) = E_U g_{j+1}(h,·) ≥ E_{ω~Π_j(h)}[e^{−Φ_j(h,ω)} g_{j+1}(h,Y_j)]
  ≥ E_ω[e^{−Φ_j} G_{j+1}(h,Y_j)] = G_j(h)`, the last equality because
  `Π_{j+1}, …` depend on `ω_j` only through `Y_j` (Markov in the history).
  The middle inequality uses only `e^{−Φ_j} ≥ 0`.
* Reviewer's question (4), Jensen direction: the only Jensen step is
  `E[1_𝒜 e^{−S}] ≥ Q'(𝒜)exp(−E[S1_𝒜]/Q'(𝒜)) ≥ ½e^{−2ES}` (convexity of
  `e^{−x}` on the conditional law given 𝒜, `S ≥ 0`, `Q'(𝒜) ≥ ½`). It is
  the same direction as in ETw Thm 2.3 and does not care whether S is
  random through h or through ω. `Φ_j ≥ 0` holds since `B ≥ 1`.
* No unweighted step inequality is needed anywhere downstream: Thm 2.3′
  is replaced by Thm 4.1 in its entirety. Verified that the base and
  conclusion steps of ETw Thm 2.3 are untouched by the change.

### 6. Independent brute force of Theorem 2.5 and Lemma 2.4 — no violation (EVIDENCE)

`scripts/review_kary_bruteforce.py` (written from scratch). Exact path
enumeration of the coupled process; weight
`w(x) = E_ω[e^{−Φ}1{y=x}]` with the **LP-optimal** `B*(n,t,d)` (stronger than
the paper's B); LP `max w·f` over nonnegative d-local f with `ν·f = 1` (f
parametrised by its local components, sign-free); Theorem 2.5 ⇔ value ≤ 1.
Lemma 2.4 is checked pointwise in x by exact ρ-enumeration. Both are
asserted at `t ∈ {0.02, 0.1, 0.25, d/(EM+4d)}`.

Activation rules: plain (ETw σ), phantom, **arbitrary full-state rules**
`F_ℓ = F(c_{<ℓ}, y_{<ℓ})` (strictly more adversarial than any pattern
family; the proof covers them), trigger families (Remark 2.8 type), chains,
dense ternary families with `ν(1) = 1/4 = δ` (cap boundary), N ≤ 12,
alphabets 2–3, d ≤ 3; plus hill-climbing over arbitrary rule tables
(maximise the LP value; and a variant constrained to `E M ≥ 0.6–0.8`).

| run | systems | max LP value |
|---|---|---|
| random (seed 1) | 150 | 1.0000000000000635 |
| stress (seed 6, N 7–12, `ν(1) ∈ {.1,.2,.25}`) | 22 (run stopped in an N=12, d=3 LP) | 1.00000 |
| hill-climb arbitrary rules (seeds 2, 3) | 36 climbs × 120 steps | 1.000000 |
| hill-climb, `E M ≥ 0.6–0.8` | 12 climbs × 150 steps | 0.87 |

Value exactly 1 is approached trivially (f constant, t small, no
replacement). **Power checks** (same LP, deliberately broken Φ): dropping
the `(4/3)tM` term gives values up to 1.23; using `B*(n,t,d−1)` gives up to
1.20; the unweighted ratio `max E_σ f/E_ν f` reaches 3.30. So the test
detects violations of the right size; Theorem 2.5's two ingredients are
both necessary and the stated Φ is never beaten. Outputs:
`data/kary/review_bruteforce.txt`.

### 7. Lemmas 4.2, 4.3 (ETw lemmas under the new law) — SOUND

* The law of `Y_j` under `Π_j(h)` is **exactly** ETw's in-block sequential
  capped law: under the plain rule `F_ℓ` depends on `(h, y_{<ℓ})` only, so
  the conditional law of `y_ℓ` given `(c,y)_{<ℓ}` (Lemma 2.1(2)) is a
  function of `y_{<ℓ}` and equals the conditional law given `y_{<ℓ}`. Hence
  `Q'` (history law) is literally the law ETw Lemma 2.1′ / 2.2 / 4.0 talk
  about; the c's never enter the history. (This would fail for the phantom
  rule, whose y-law is not σ; the paper correctly does not use it in §4.)
* Inflation (ETw 2.2): conditional density `≤ (1−δ_ℓ)^{−1}` at every block
  coordinate, `δ_ℓ = ℓ^{−1/2} ≤ W^{−1/2} ≤ 1/4`. γ′ is the decaying one
  (O7-1 repair present). Lemma 4.0 is stated by ETw for "any order
  compatible with the sequential construction" and its bound
  `p_ℓ(past) ≤ Σ_v ℓ^{−v}N_{ℓ,v}(n)` is pointwise in the full history, so the
  in-block past changes nothing.
* First moment over dyadic blocks: `E_{Q'}M_V ≤ Σ_{M:P(M)∈V} τ(A_M²)Γ(M)/M`
  (light mass ≤ total mass; a class `qℓ^v` contributes `ℓ^{−v}` iff its mod-q
  requirement is met, probability `≤ Γ(q)/q` by inflation, including
  in-block primes of q). ETw Lemma 2.6's analytic input
  `Σ_{M≤x}τΓ ≪_W x log²x` is window-free, so `≪ ((1+B)2s)³` for
  `(e^s, e^{2s}]`, `2s ≤ λ`. Uniform in the family. Fine.
* Leak: every class decided at its top prime (increasing order inside
  each block; twin cofactor primes in the same block come earlier;
  prime-power tops are one coordinate mod `ℓ^{E_ℓ}`). Lemma 2.1′ +
  Lemma 4.0 + Markov give `𝔏 ≪_B W^{−1/4}` as in ETw Cor 2.5, under the
  ETw convention fixing `W₀(B)`.

### 8. Theorem 4.5 assembly (headline) — SOUND

* Blocks: singletons `(W, e^{s₁}]` (ETw Prop 4.1, cost ≪ `K'(1+B)³λ^{3/4}`),
  dyadic sequential blocks covering `(e^{s₁}, e^{λ/2}]`, one linear block
  `(e^{λ/2}, e^λ]` (ETw Cor 4.3, its (S) is a deterministic (S_w)),
  invisible singletons above `e^λ`. Increasing order, all classes decided at
  the top prime. Each step is an (S_w); Thm 4.1 applies.
* Locality: primes of `V_i` have `log ℓ > s = 2^i s₁`, and a λ-level term has
  `Σ log ℓ ≤ λ`, so `|T∩V_i| < λ/s`, d-local with `d_i = ⌊λ/s⌋ ≥ 2`
  (`s < λ/2`). Majorant terms have real coefficients; only `f ≥ 0` is used
  (item 1).
* `t_i(h) = d_i/(E[M|h]+4d_i)` is fixed given h, as Lemma 2.4 needs.
  Cor 2.6 per h then Jensen over h (`m ↦ log(C₀(m+4d)/d)` concave) gives
  `E Φ_i ≤ d_i log(C₀(E M_{V_i}+4d_i)/d_i) + (4/3)d_i + O(log λ)`.
  With `E M_{V_i} ≤ K₁s³`, `d_i ≥ λ/(2s)`: `(E M+4d)/d ≤ 2K₁16^i + 4`, so
  `E Φ_i ≤ (λ^{3/4}/2^i)(c₁(B) + i log 16) + O(log λ)`; `I ≍ log λ` blocks;
  total `≪_B λ^{3/4} + O(log²λ)`. Arithmetic re-done; correct.
* Reviewer's question (5): B fixed throughout; caps `δ_ℓ ≤ 1/4`; Lemma 2.6
  used only with upper end `≤ e^{λ}`; Prop 4.1 needs `s₁ > log W` (λ₀(B)
  ensures it). Every ETw lemma is applied inside its hypotheses.
* Sanity of the mechanism: the cost per block has the same form
  `(λ/s)(1+log(s⁴/λ))` that ETw's window bound (from ET Prop 2.4) gives in
  Thm 2.7, so the λ^{3/4} total matches the known gapped case; the gain is
  that the k-ary step now has *some* d·log(mass) bound, in mean, for an
  arbitrary pattern family. Nothing in the count is better than the
  unary/gapped case, which is reassuring rather than suspicious.
