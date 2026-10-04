# Second hostile review: EXCEPTIONAL_KARY.md (headline Thm 4.5)

Reviewer: side-agent/review-kary-2. Subject: branch `side-agent/kary-comparison`
at `e35bf60` (includes Lemma 4.2′). First review:
`side-agent/review-kary:reviews/exceptional-kary-review.md` (all SOUND, ETw
inputs taken on trust). This review re-derives the ETw inputs from scratch,
re-derives KARY Thm 2.5 / Thm 4.1, and sanity-checks the headline.

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects numbered E1, E2, …
(E-prefix to avoid clashing with the first review's D-numbers.)

## Part 1 — ETw inputs, re-derived, and their use in KARY

### 1.1 ETw Lemma 1.3 (QR base) and Lemma 1.1 / Cor 1.2 — SOUND

* Lemma 1.1 re-derived: `A = (M+1)/4`, `gcd(A,M) = gcd(A,4A−1) = 1`; `D = sr²`,
  `D | A² ⇔ sr | A` (s squarefree), so `4s | M+1`. `(−4D|M) = (−1|M)(s|M) = −(s|M)`.
  For odd s, `M ≡ −1 (mod 4s)` gives `(M|s) = (−1|s)` and reciprocity with
  `(M−1)/2` odd gives `(s|M) = (−1|s)(−1)^{(s−1)/2} = 1`. For `s = 2s'`,
  `8 | M+1` ⇒ `(2|M) = 1`. Hence `(−4D|M) = −1`. Correct.
* Cor 1.2: n a nonzero QR at every `p | M` ⇒ `(n|M) = 1 ≠ (−4D|M)`. W-smooth
  Case-B moduli are odd, so only odd `p ≤ W` matter; `R_W` imposes exactly that.
* Lemma 1.3(2): the factor at odd `p^e ∥ Q₀` keeps `p^{e−1}(p−1)/2` of `p^e`
  residues; at `p = 2` nothing is imposed. `log(Q₀/|R_W|) = Σ_{3≤p≤W} log(2p/(p−1))`,
  independent of Q₀ and of the family. (3): a single class mod `p^e` has
  probability `≤ 2/(p^{e−1}(p−1)) = γ(p)/p^e`. CRT product ⇒ independence.
* Use in KARY: base term `O_B(1)` once `W = W₀(B)` is fixed; (R1) for the
  W-smooth classes; (R2) feeds Γ. Q₀ may be arbitrarily large (powers of small
  primes from the family's W-smooth parts) without affecting either. Within
  hypotheses.

### 1.2 ETw Lemma 2.2 (inflation) under KARY's law — SOUND

* Re-derived: for `m = Π p^e`, `Q'(n ≡ a mod m) = E[Π_p 1{n ≡ a mod p^e}]`.
  Peel coordinates from the last in the processing order: given everything
  earlier, the base factor is `≤ γ(p)/p^e` (R2, independence across p), and
  a coordinate `ℓ > W` has conditional law uniform on `Ω_ℓ ∖ F_ℓ` with
  `|F_ℓ|/ℓ^{E_ℓ} ≤ δ_ℓ` (light) or uniform (heavy). A class mod `ℓ^e`
  (`e ≤ E_ℓ`) is a union of `ℓ^{E_ℓ−e}` points, so its conditional
  probability is `≤ (1−δ_ℓ)^{−1}ℓ^{−e}` pointwise in the past. Product bound.
* KARY Lemma 2.1(2) gives exactly this conditional law for the plain rule
  (`P(y_ℓ=a | past) = ν_ℓ(a)1{a∉F_ℓ}/(1−p_ℓ)` when light). The c's do not
  enter the y-history, so the chain rule is over y alone. `δ_ℓ = ℓ^{−1/2} ≤ 1/4`
  needs `W ≥ 16` (ETw §2.3 assumes it; `W₀(B) ≥ 16` implicit — fine).
* γ′(ℓ) = (1−ℓ^{−1/2})^{−1} for ℓ > W (the decaying form; O7-1 repair present).

### 1.3 ETw Lemma 2.1′ (leak) and KARY Lemma 4.3 — SOUND

* Re-derived: a final history outside 𝒜 satisfies some class C. Pure-small C
  are excluded by (R1). Otherwise C is decided at its top prime ℓ (all
  cofactor primes are smaller, hence earlier in the increasing order; the
  W-smooth part is in the base; the top requirement mod `ℓ^v` is one
  coordinate mod `ℓ^{E_ℓ}`). When ℓ is processed, the other requirements are
  already met, so `y_ℓ` lies in the completing set `⊆ F_ℓ`. Light ℓ: impossible
  (`y_ℓ ∉ F_ℓ`). Heavy ℓ: `y_ℓ = c_ℓ` uniform, hit probability `p_ℓ` given the
  past. Union bound: `𝔏 ≤ Σ_ℓ E[p_ℓ 1{p_ℓ > δ_ℓ}]`.
* This covers all four block types of Thm 4.5 uniformly, including the
  singletons above `e^λ`: those must still condition at light ℓ (else the
  leak bound fails), and they do; their cost is 0 because f is constant in
  `y_ℓ`, not because σ = U. KARY's text ("singletons above `e^λ` (cost 0)")
  is correct but terse; ETw Cor 4.3 says the same.
* Cor 2.5 arithmetic: Markov `E[p1{p>δ}] ≤ E p²/δ`; with ε = 1/4,
  `Σ_{ℓ>W} ℓ^{1/2}·Cℓ^{−7/4} = CΣℓ^{−5/4} ≪ W^{−1/4}`. Uniform in the family
  and in λ because C(ε,B) is W-free (item 1.4).

### 1.4 ETw Lemma 2.4 / Lemma 4.0 (second moment, prime-power tops) — SOUND

* Re-derived. Write each modulus with top ℓ as `M = qℓ^v`, `(q,ℓ)=1`,
  `q ≤ ℓ^{1+B−v} ≤ ℓ^B`. The class `−4D (mod M)` contributes to `F_ℓ` only if
  `n ≡ −4D (mod q)` (all primes of q precede ℓ), and then contributes one class
  mod `ℓ^v`. So pointwise `p_ℓ ≤ Σ_v ℓ^{−v}N_{ℓ,v}(n)`. Expand `N²` over pairs
  of pairs; a compatible pair is one class mod `m = lcm(q,q')`, probability
  `≤ Γ(m)/m ≤ 3^{ω(m)}/m` (item 1.2; `γ(2)=1`, `γ(3)=3`, `γ(p) ≤ 5/2` for odd
  `5 ≤ p ≤ W`, `γ′(ℓ) ≤ 4/3` above W). `#{(q,q'): lcm = m} = τ(m²)` (2e+1 choices
  per `p^e ∥ m`). `τ(A_q²) ≤ C_ε ℓ^{ε/4}` since `A_q ≤ ℓ^{1+B}`. Euler product
  `Π_{p≤ℓ^{2B}}(1 + 9/p + O(p^{−2})) ≪ (2B log ℓ)^9`. Minkowski over v. The
  constant is **W-free** (only `Γ ≤ 3^ω` enters), which is what lets W₀(B) be
  chosen afterwards.
* Use in KARY (Lemma 4.2(3)): needs (a) item 1.2 for lcm's of cofactors —
  holds for KARY's law; (b) `p_ℓ` is the density of classes decided at ℓ —
  holds because in-block cofactor primes precede ℓ in the increasing order.
  ETw's "any order compatible with the sequential construction" is satisfied.
  Note the bound is pointwise in the full y-history, so KARY's in-block
  dependence (which ETw's windows lacked) is irrelevant.

### 1.5 ETw Lemma 2.6 → KARY Lemma 4.2′ (first moment on dyadic blocks) — SOUND

* Step 1 re-derived as in 1.4 with one class: `E 1{active} ≤ Γ(q)/q`, and
  `ℓ^{−v}Γ(q)/q ≤ Γ(M)/M` because `γ′ ≥ 1`; `≤ τ(A_M²)` values of D. Light mass
  `M_V ≤ Σ_{ℓ∈V} p_ℓ`.
* Step 2 is ET Lemma 3.1 / Cor 3.6 with `h(p) = γ′(p) − 1`: `h(2) = 0`,
  `h(3) = 2`, `h(p) ≤ 3/2` for `5 ≤ p ≤ W`, `h(ℓ) ≤ (4/3)ℓ^{−1/2}` above W. The two
  convergence conditions (Shiu range `Σ h(e)/φ(e) < ∞`; large divisors
  `Σ h(e)e^{−3/4} < ∞`) hold, with constant `K₀(W)` (a finite Euler product
  over `p ≤ W`, so `(log W)^{O(1)}`). This analytic mean value is an ET input,
  not an ETw one; it is window-free and B-free, and was reviewed with ET. I
  did not re-derive Shiu's theorem.
* Step 3 re-checked: `Σ_{M≤X} τΓ/M = S(X)/X + ∫_1^X S(x)x^{−2}dx ≤
  K₀(log²(X+2) + log³(X+2))`; `log X = 2(1+B)s ≥ 2log W ≥ 5.5` gives the
  factor 1.3 (`1.01³·(1+1/5) ≈ 1.24`). Dropping `P(M) ∈ V` is a valid upper
  bound (nonnegative terms). `M ≤ P(M)^{1+B} ≤ e^{2(1+B)s}`. Correct.
* Hypotheses: ETw Lemma 2.6 was stated for η-windows with `s_j ≤ λ`; the
  restriction `s_j ≤ λ` is not used in its proof, and Lemma 4.2′ restates the
  bound for any `V ⊆ (e^s, e^{2s}]`, `s ≥ log W`. Thm 4.5 has `s ≥ s₁ > 2log W`.

### 1.6 ETw Prop 4.1 (singletons below `e^{λ^{1/4}}`) — SOUND

* Re-derived: for any `f ≥ 0` (no level needed), `E_U f = (1−p)E_{U|F^c} f +
  pE_{U|F} f ≥ (1−p)E_σ f` at a light ℓ; at a heavy ℓ, σ = U and Φ = 0. So
  (S) with `Φ = −log(1−p_ℓ(h)) ≤ (4/3)p_ℓ(h)` (p ≤ 1/4). Summing
  `E p_ℓ` over `W < ℓ ≤ e^{s₁}` by Lemma 4.2′'s Steps 1–3 with
  `X = e^{(1+B)s₁}`: `≤ K′((1+B)s₁)³ = K′(1+B)³λ^{3/4}`; ×4/3 ×2.
* Use in KARY: deterministic-cost (S) is an (S_w) with `Π = σ`, `Φ` a
  function of h. Needs `s₁ > log W`: KARY takes `s₁ > 2 log W`. Fine.

### 1.7 ETw Lemma 4.2 / Cor 4.3 (top block `(e^{λ/2}, e^λ]`) — SOUND

* Lemma 4.2 re-derived: `E_U f = c₀`; `E_σ g_ℓ = E_U[(g_ℓ + m_ℓ)(r_ℓ − 1)] ≤
  ε_ℓ m_ℓ` (the review variant), and `Σ m_ℓ ≤ c₀` from `f ≥ 0` at the
  coordinatewise minimiser. Only the one-coordinate marginals of σ matter, so
  any dependence structure inside the block (KARY's k-ary activations) is
  allowed.
* Cor 4.3: two primes `> e^{λ/2}` cannot both occur in a term of level λ, so
  f has the linear form. Marginal density of the in-block sequential capped
  law `≤ (1−δ_ℓ)^{−1} ≤ 1 + 2δ_ℓ`, `δ_ℓ ≤ e^{−λ/4}`. Cost `2log(1+3e^{−λ/4})`.
  Needs `λ/2 > log W`: implied by `s₁ > 2log W`.
* KARY uses the plain rule's law there (light/heavy by total activated
  density). Same marginal bound. Within hypotheses.

### 1.8 ETw Thm 2.3′ (abstract step + leak), as generalised by KARY Thm 4.1 — SOUND

* Re-derived the ETw part: `g_j(h) = E_U[ν | H_{<j} = h]`; under U the block
  residues are independent of h and of each other, and each term
  `1[n ≡ b (mod d)]` of ν factorises by CRT, so `f(y) = g_{j+1}(h,y)` is a sum
  of functions of `y_{T∩V_j}` with `Σ_{ℓ∈T∩V_j} log ℓ ≤ λ`. Majorant digits
  finer than `ℓ^{E_ℓ}` and primes outside the family are integrated out by U
  and do not break this. `f ≥ 0` **on all of** `Ω_{V_j}` because ν ≥ 0 on all
  residues (every residue is hit by integers). This global nonnegativity is
  essential for KARY Thm 2.5, whose interpolation points `y^ρ` are arbitrary
  points of `Ω_{V_j}`; it holds.
* Conclusion: `Eν ≥ (|R|/Q₀)avg_{c∈R}g_1(c)` uses only `g_1 ≥ 0` off R.
* Locality in dyadic blocks: primes of `V_i` have `log ℓ > s`, so
  `|T ∩ V_i| < λ/s`, hence `≤ ⌊λ/s⌋ = d_i`. Correct.

## Part 2 — KARY Thm 2.5 and Thm 4.1, re-derived independently

### 2.1 Thm 2.5 (weighted k-ary comparison) — SOUND

Re-derived without reading the first review's argument:
* Corner bound. On a frozen path ω, `y^ρ_ℓ ∈ {c_ℓ, y_ℓ}` is selected by `ρ_ℓ`
  alone, so `g(ρ) = f(y^ρ)` is a nonnegative function on `{0,1}^R`, multilinear
  of degree ≤ d (each `f_T` sees `ρ_{T∩R}`). Averaging over `Sym(R)` keeps
  `g(1)` and `E_{Bern(t)}g`; the average is `Q(K)` with `deg Q ≤ d`, `Q ≥ 0` on
  `{0..n}`. Lagrange at any `min(d,n)+1` nodes and `Q ≥ 0` at **every** k
  give `g(1) = Q(n) ≤ max_y(|ℓ_y(n)|/ψ(y))·E Q(K)`. Direction: upper bound on
  the σ-side value by the thinned bulk. Correct.
* Thinned law (Lemma 2.4), the crux. Fix x. `P_ρ(y^ρ = x | ω) = Π_ℓ π_ℓ`
  with `π_ℓ = (1−t)1{c_ℓ=x_ℓ} + t1{y_ℓ=x_ℓ}` on R and `1{c_ℓ = x_ℓ}` off R; so
  `π_ℓ ≤ φ_ℓ`. Given `𝒢_{ℓ−1}` (all of `(c,y)_{<ℓ}`), `F_ℓ`, `p_ℓ`, "light" and
  `D_ℓ` are known; `c_ℓ ~ ν_ℓ` and the fresh draw are independent of `𝒢_{ℓ−1}`
  and of each other. `E[φ_ℓ|𝒢_{ℓ−1}] = ν_ℓ(x_ℓ)(1 + 1{light}t p_ℓ1{x_ℓ∉F_ℓ}/(1−p_ℓ))
  ≤ ν_ℓ(x_ℓ)D_ℓ`. The normalised product is a nonnegative supermartingale, so
  `E[Πφ_ℓ/(ν_ℓ(x_ℓ)D_ℓ)] ≤ 1`, and `W·ΠD_ℓ ≤ 1` pathwise because t is
  deterministic. Correct. Only predictability of `F_ℓ` is used; the rule may
  depend on anything in `𝒢_{ℓ−1}`.
* Assembly: multiply the pathwise corner bound by `W/B ≥ 0`, take `E_ω`, swap
  sums (`f ≥ 0`), apply Lemma 2.4 pointwise in x. No unweighted ratio
  `E_σ f/E_ν f` appears. Correct.
* Cor 2.6: `E n = E M` exact (replacement probability `1{light}p_ℓ` given the
  past); the (3.1) bound is concave in n after `max ≤ sum`; Jensen; with
  `t = d/(m̄+4d) ≤ 1/4`. Correct. I did not redo §3's constants beyond spot
  checks; the first review did, and my item-3 script uses exact Lagrange B.

### 2.2 Thm 4.1 (random step costs) — SOUND; the induction is linear in `e^{−Φ}` in the right direction

* Induction claim: `g_j(h) ≥ G_j(h) := E_{Q'}[1_𝒜 e^{−Σ_{i≥j}Φ_i} | H_{<j}=h]`,
  for **every** h (G is defined through the kernels, so Q′-null h are fine).
* Step: `g_j(h) = E_U f`, `f = g_{j+1}(h,·) ≥ 0` λ-level (item 1.8).
  (S_w): `E_U f ≥ E_ω[e^{−Φ_j(h,ω)} f(Y_j)]` — the cost Φ_j does **not** depend
  on f (it is `log B(n,t,d) + (4/3)tM`, t fixed by h), which is what lets one
  apply it to the unknown `f = g_{j+1}(h,·)`. Then IH pointwise
  `f(Y_j) ≥ G_{j+1}(h,Y_j)`, multiplied by `e^{−Φ_j} ≥ 0`: monotone, correct
  direction. Finally `E_ω[e^{−Φ_j}G_{j+1}(h,Y_j)] = G_j(h)` because later
  kernels see `ω_j` only through `Y_j` (the c's and coins are discarded).
  The weight stays **inside** the expectation; nothing is pulled out as
  `e^{−EΦ}` until the very end.
* The only nonlinear step: `E[1_𝒜e^{−S}] ≥ Q′(𝒜)exp(−E[S|𝒜]) ≥ ½e^{−2ES}`
  (convexity of `e^{−x}`; `S ≥ 0`, `Q′(𝒜) ≥ ½`). Correlations between
  `Φ_j` and later blocks or 1_𝒜 are harmless: they are all under one
  expectation.
* `S ≥ 0` requires `B(n,t,d) ≥ 1`, true (`Σ_yℓ_y(n) = 1`, `Σ_yψ(y) ≤ 1` ⇒
  max ratio ≥ 1) but **not stated** in KARY → defect E1 (minor).
* Thm 4.5's use: `E_{Q'}Φ_i ≤ E_{Q'}F(E[M_{V_i}|H_{<i}]) ≤ F(E_{Q'}M_{V_i})`, F
  concave increasing; and `E_{Q'}E[M|H] = E_{Q'}M` with the same law. Correct.
  Also `d ↦ d·log(C₀(a/d+4))` is increasing, so using `d ≤ λ/s` outside and
  `d ≥ λ/(2s)` inside the log is legitimate.

### 2.3 Independent end-to-end toy test of Thm 4.1 ∘ Thm 2.5 (EVIDENCE)

The first review tested Thm 2.5 for one block. Untested so far: the
**composition** with random, history-dependent `t_j(h)` and costs across
blocks, patterns straddling blocks, and leak through heavy coordinates.
`scripts/review2_kary_pipeline.py` (from scratch): 6 coordinates in two blocks
of 3, alphabets 2–3, random unary/binary/ternary patterns (some straddling),
cap 1/4, plain rule; exact path enumeration; per-block `d_j`, `t_1`,
`t_2(h) = d_2/(E[M_2|h]+4d_2)`, exact Lagrange `B`. It solves
`LP = min{E_ν f : f ≥ 0, f ≥ 1_𝒜, f = Σ f_T, |T∩V_j| ≤ d_j}` and compares with
`E_{Q′}[1_𝒜 e^{−Φ₁−Φ₂}]` (the claim of Thm 4.1's induction at j = 1), and
checks `log(1/LP) ≤ log 2 + 2EΦ` when `Q′(𝒜) ≥ ½`.

| run | cases | max RHS/LP | Φ/2 violates | no-M-term violates |
|---|---|---|---|---|
| sparse (60 seeds × d ∈ {(1,1),(2,1),(2,2)}) | 180 | 0.9964 | 142 | 115 |
| dense (same) | 180 (12 with 𝒜 = ∅) | 1.0000 | 5 | 3 |

No violation; Jensen form holds in all 186 cases with `Q′(𝒜) ≥ ½`. The test
has power: halving Φ or dropping `(4/3)tM` is violated in most sparse cases.
Outputs `data/kary/review2_pipeline_{sparse,dense}.txt`.

## Part 3 — Theorem 4.5 and consistency with earlier results

### 3.1 Theorem 4.5 assembly — SOUND (minor E2)

* Blocks: singletons `(W, e^{s₁}]` (1.6), dyadic sequential blocks on
  `(e^{s₁}, e^{λ/2}]` (2.1–2.2 with 1.4–1.5), one linear block `(e^{λ/2}, e^λ]`
  (1.7), singletons above `e^λ` (cost 0, conditioning kept for the leak,
  1.3). Increasing order; every class decided at its top prime; leak ≤ ½ at
  `W₀(B)` (1.3–1.4). Base `O_B(1)` (1.1).
* Dyadic cost: `E M_{V_i} ≤ K₁s³`, `d_i ∈ [λ/(2s), λ/s]`,
  `(EM+4d)/d ≤ 2K₁16^i + 4`, so `EΦ_i ≤ (λ^{3/4}/2^i)(c₁ + i log 16) + O(log λ)`;
  `O(log λ)` blocks ⇒ `≪_B λ^{3/4} + O(log²λ)`. Re-done; correct.
* All constants are uniform in the family (W₀, K, C(ε,B) depend on B, W
  only; Q₀ drops out). No dependence on the number of primes in a block:
  Thm 2.5's cost sees only `n` and `M`, never `|V|` or the arity.
* **E2 (minor, wording).** "`0 ≤ i ≤ I`, `2^I s₁ < λ/2`" should say I is the
  *largest* such index, so that the blocks cover `(e^{s₁}, e^{λ/2}]`. Implicit;
  no effect on the bound.

### 3.2 Consistency with earlier results — no contradiction

* **EB Prop 4.3** (`sup_n p_ℓ(n) ≥ ℓ^{−1+1/(L(1+η))−o(1)}`): a supremum. KARY
  uses only `E M` (first moment) and `E p_ℓ²` (leak). Huge activations at rare
  histories are heavy, leak, and are charged to Lemma 4.0's second moment,
  exactly as in ETw Thm 2.7 (already merged, reviewed). Consistent.
* **ET Lemma 3.8** (same-scale balanced moduli carry `≫ (log x)³`): KARY does
  not claim twins are cheap. Lemma 4.2′ sums *all* moduli, twins included,
  and the cubic mass `K₁s³` enters the dyadic cost through `log(s⁴/λ)` — the
  same entry point as the unary mass in ET/ETw. Consistent; it is precisely
  why the logarithmic dependence on mass is what matters.
* **ETw §4.3 remark** ("no bound `1+O(max p)` for ≥ 2 primes per term"):
  KARY's step costs `d·log(M/d)`, not `O(max p)`. Consistent.
* **ETw §6.4 dense toys** (sequential σ has `log C*` above the void) and
  **Remark 2.8**: these concern the *unweighted* ratio `E_σf/E_νf`; KARY proves
  only the weighted inequality and shows the unweighted mean-mass form is
  false in general. Consistent.
* **TW2/TW3** (Λ² cap `≪ L^{3/4}(log L)^{O(1)}` for ≤ 2 large primes, fixed
  B): KARY's Thm 4.5 is stronger on that class (all nonnegative CRT
  majorants, any number of primes, no log). Not a contradiction; it makes
  that line redundant for fixed B (TW2/TW3 still have value as an
  independent route and for the explicit Λ² structure).
* **ETw Thm 2.7 / 4.4** (`η^{−1}λ^{3/4}`): KARY removes the `η^{−1}` because
  resolvedness, hence η-windows, are no longer needed; dyadic blocks suffice.
  An improvement, not a conflict.
* No earlier file proves a *lower* bound on `S_λ` larger than `λ^{3/4}` for
  any bounded-B ℛ(M)-family (checked STATUS, DISCOVERIES, ET, EB, ETw,
  NONCRT); the 3/4 note's own majorant reaches θ = 3/4, so the cap is
  attained, not beaten.

### 3.3 Why the earlier obstacles were not real (one paragraph)

ETw believed the η-twin range needed Conj 6.4 because it looked for an
*unweighted* step inequality `E_σ f ≤ e^{Φ(h)}E_U f` with a cost fixed by the
history, and the only extrapolation tool available (ET Prop 2.4) symmetrises
over the *physical* hit indicators, which are independent only when every
condition is unary in the block; k-ary activations make later hits depend on
earlier residues, so that symmetry is lost (ETw §4.5 route 5), and the
alternatives (finer windows, over-conditioning, voids, Markov removal plus
incident-weight sparsity) all paid something proportional to the twin mass.
KARY sidesteps both points. It couples σ with an unconditioned product draw c
and extrapolates along *artificial* i.i.d. replacement coins on a frozen path,
where symmetry holds by construction and the degree bound is just d-locality.
The price of the adaptivity is absorbed in a pathwise weight `e^{−(4/3)tM}`
controlled by a supermartingale, which needs only that each activated set is
known before its coordinate is drawn. The resulting cost is random, and the
unweighted form is genuinely false (Remark 2.8). But the sequential sieve
limit never needed a deterministic cost: its downward induction is linear in
the weight, and only the final Jensen step averages it. So `E Φ`, i.e. the
mean mass, suffices. The mass is already cubic and controlled by first
moments for all moduli, twins or not. The obstacles were artefacts of asking
for a pointwise-in-history, unweighted comparison, not features of k-ary
conditioning.

## Defects

* **E1 (minor, missing line).** Thm 4.1 assumes `Φ_j ≥ 0`; the sequential
  instance never states `B(n,t,d) ≥ 1`. One line: `Σ_y ℓ_y(n) = 1` and
  `Σ_y ψ(y) ≤ 1` give `max_y|ℓ_y(n)|/ψ(y) ≥ 1`.
* **E2 (minor, wording).** Thm 4.5: I is the largest index with `2^I s₁ < λ/2`.
* **E3 (bookkeeping, not a defect of KARY).** On merge, STATUS.md (η-twins
  "open core"), DISCOVERIES (D)13, ETw §5 "Not covered" item 1 and §6
  (Conj 6.4 / Prop 6.5 "needed") and the TW2/TW3 status lines become stale.
  The headline's θ-reading still rests on ET Lemma 2.9's hypotheses (slice
  primes `≤ N^{O(1)}`, `Σ|a_i| < N`), on fixed B, and on ℛ(M)-only families
  (no (a,D)/Case-A mixtures); KARY states these, and STATUS should too.

## Overall verdict

| item | verdict |
|---|---|
| 1.1 QR base (ETw L1.1, C1.2, L1.3) | SOUND |
| 1.2 inflation (ETw L2.2) | SOUND |
| 1.3 leak (ETw L2.1′, C2.5; KARY L4.3) | SOUND |
| 1.4 second moment (ETw L2.4, L4.0) | SOUND |
| 1.5 first moment (ETw L2.6; KARY L4.2′) | SOUND (uses ET L3.1, not re-derived) |
| 1.6 singletons (ETw P4.1) | SOUND |
| 1.7 top block (ETw L4.2, C4.3) | SOUND |
| 1.8 abstract step (ETw T2.3′) | SOUND |
| 2.1 KARY Thm 2.5, Cor 2.6 | SOUND |
| 2.2 KARY Thm 4.1 (random costs) | SOUND-AFTER-REPAIRS (E1, one line) |
| 3.1 KARY Thm 4.5 | SOUND-AFTER-REPAIRS (E2, wording) |
| 3.2 consistency | no contradiction found |

**Headline: Theorem 4.5 is correct.** For each fixed B, every family of
ℛ(M)-classes with `M ≤ P(M)^{1+B}` (plus W-smooth classes) has
`S_λ ≪_B λ^{3/4}` for all nonnegative CRT majorants, unconditionally. E1–E2
are presentational; no mathematical repair is needed.
