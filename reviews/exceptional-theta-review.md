# Hostile review: EXCEPTIONAL_THETA.md (branch side-agent/theta-beyond-34)

Reviewer: side-agent review-theta-2 (restart of the interrupted first review).
Subject files imported verbatim from `side-agent/theta-beyond-34`:
EXCEPTIONAL_THETA.md, AGENT_REPORT_A2.md, scripts/theta_*.py, data/theta/.
Literature assessment reused from the first reviewer: `reviews/theta-lit-notes.md`
(verdict: apparently new; no prior source found).

Status: COMPLETE (all five items).

## Summary of verdicts

| # | item | verdict |
|---|---|---|
| 1 | Theorem 2.5 (+ Lemmas 2.1–2.3, Prop 2.4) | **SOUND** (presentation repairs T1–T4) |
| 2 | Theorem 2.7, Lemma 2.8 (+ proof of Cor 3.6) | **SOUND** (cosmetic S1–S2) |
| 3 | scope of Cor 3.4–3.6 | **SOUND-AFTER-REPAIRS**: SC1, a major *interpretive* defect, with a proved repair (Lemma R); SC2 minor |
| 4 | Lemma 3.7, Lemma 3.8, Thm 5.5 (+ Cor 5.6, Prop 5.7) | **SOUND** (L1 minor, about an out-of-scope label) |
| 5 | §4 accounting (Lemmas 4.1–4.4), summary/report consistency | **SOUND-AFTER-REPAIRS** (SC1 rewording, A1–A3 minor) |

**Bottom line.** The mathematics holds up:
* Theorem 2.5's lower bound on the mean of *every* nonnegative level-λ
  majorant;
* its sequential extension;
* the profile lemmas;
* H_A3 via Elsholtz–Tao Prop 1.4, which I verified against the source,
  including the k-range;
* the balanced-supply lemma;
* the Λ² theorem.

The independent exact LPs agree with every intermediate inequality of the
proofs:
* CRT LP = average of the fibre Boolean LPs in 54/54 instances;
* the Prop 2.4 chain holds in 51/51 instances;
* the sequential chain holds in 32/32 instances;
* the Λ² chain holds in 25/25 instances.

**The one substantive issue (SC1).** The ceiling is proved for majorants
of bounded *level*. The 3/4 note's real constraint is its *coefficient
sum* `T_abs ≤ N^{1/2}`; its modulus bound is explicitly "not necessary".
The §0 Verdict even omits the level hypothesis.

Lemma R (proved in item 3) repairs this. Any majorant with coefficient sum
T yields one of level `Λ₀ + log T + log(1/Eν)` with at most twice the
mean, where Λ₀ is the log of the largest slice prime. So "3/4 is sharp"
holds for every architecture whose final bound is `N·Eν + Σ|a_i|`, with
family moduli ≤ N^{O(1)}. Families with slice primes beyond N^{O(1)}
remain formally outside.

**Numbered defects.**

| defect | severity | location |
|---|---|---|
| T1 | minor | O(log²λ) claim |
| T2 | minor | truncated μ̄ |
| T3 | cosmetic | Jensen chain |
| T4 | cosmetic | z ≥ 4 |
| S1 | minor | Q₀ size in Cor 3.6 |
| S2 | cosmetic | s_j undefined |
| SC1 | MAJOR, interpretive | level vs coefficient budget |
| SC2 | minor | LL R-term |
| L1 | minor | Case-A reduction label |
| A1 | minor | Lemma 4.3 reason |
| A2 | minor | "constants only" direction |
| A3 | minor | report wording |

Each entry below carries location, quote and fix.

**Code (reviewer's own, no shared code with the subject's scripts).**
* `scripts/review_theta_lp.py` (Parts A/B/C);
* `scripts/review_theta_seq.py`;
* `scripts/review_theta_selberg.py`.

Outputs are in `data/theta/review_*.txt`. Replay with
`PYTHONPATH=scripts uv run --with scipy[ --with sympy] python <script>`.
Part A takes about 1.5 h at one core; the rest take minutes.

## Item 1 — Theorem 2.5 (with Lemmas 2.1–2.3, Proposition 2.4)

**Verdict: SOUND** (presentation repairs T1–T4 only; none load-bearing).

### 1.1 Direction of the inequality

The goal is a *lower* bound on `min{Eν : ν ≥ 0 on ℤ, ν ≥ 1 on 𝒜, level ≤ λ}`.
The proof is primal: for an arbitrary feasible ν it exhibits
`1 ≤ ν_c(0) ≤ (bounded constant)·E ν_c`. The interpolation functional
`Q ↦ Σ_j c_j (⊗_g I_{j_g} Q)(0)` with Lagrange weights is exactly a
dual-feasible certificate: it reproduces Q(0) on the whole span and is
dominated by `B·(probability measure)` on the support. So the direction is
right. No minimax or strong-duality step is used, so no duality-gap issue
can arise.

### 1.2 Line-by-line check

* **Lemma 2.1.** MacWilliams–Sloane Ch. 10 Lemma 7 gives
  `C(z,y) ≥ (8y(1−y/z))^{−1/2} e^{zH(y/z)}`. Combined with `D ≤ χ²` and
  `1/(1−q) ≤ 4/3`, this gives the stated bound. Checked.
* **Lemma 2.2.**
  * (2.1) uses `P ≥ 0` on Y only. Correct.
  * (a): `⌈μ'⌉ ≤ z−1` needs z ≥ 3, which holds because μ' ≥ 1 and q ≤ 1/4
    force z ≥ 4 (unstated, T4).
  * (b): exact.
  * (c): I re-derived the node bounds.
    * `W+k+1 ≤ √(kμ')` uses `k ≤ √(kμ')/4` (from k ≤ μ'/16) and
      `2 ≤ √(kμ')/4` (from kμ' ≥ 64).
    * Nodes lie in `[μ'/2, 2μ'] ⊆ [1, z−1]`, using `2qz ≤ z/2`.
    * `|ℓ_i(0)| ≤ (2μ')^k 2^k (e/k)^k (k/μ')^{k/2} = (4e√(μ'/k))^k`.
    * `16e^{2+8/3} ≈ 1703 ≤ C₁ = 16e⁶`.
  * (2.2): the Legendre step `max_k[(k/2)log(C₁μ'/k) − αks] = (C₁μ'/2e)e^{−2αs}`
    is exact, and `C₁/(2e) = 8e⁵ = C₄`. The three fallback cases are correct.
    In particular `1.151·16 = 18.4 ≤ 19`, and `C₄e^{−2} ≫ 1.151`.
* **Lemma 2.3.**
  * The telescoping `Σ_{j∈Λ}⊗Δ_{j_g}` reproduces every `x^a` with `a ∈ Λ`.
    Nestedness of nodes is not needed, because `Δ_k` kills degree < k
    exactly.
  * `|c_j| ≤ 2^G`.
  * Checked numerically with random non-nested nodes (Part C below).
* **Proposition 2.4.**
  * *Step 0.* Correct: a term containing a coordinate with `s_i > λ` would
    violate the level.
  * *Step 2 (thinning).* `x = u∘w` has the right law. `f_w(u) = f(u∘w)` is
    nonnegative, λ-level, and has `f_w(0) = f(0) ≥ 1`, because the map
    `u ↦ u∘w` sends 0 to 0.
  * *Step 3 (symmetrisation).*
    * Averaging over `Π Sym(Z_g)` preserves nonnegativity, the value at 0,
      and the mean, since the law of u is exchangeable inside each band
      (common `q_g`; this is why thinning is done first).
    * It produces a polynomial in the counts. The multidegree of `u^S`,
      `S ⊆ T`, satisfies `Σ_g j_g s_g ≤ Σ_{i∈S} s_i ≤ λ`, because
      `s_i ≥ s_g` on `B_g`.
    * Reduction modulo `Π_{i=0}^{z_g}(K_g−i)` lowers only the g-th degree,
      so the support stays in the lower set and lands in Λ'.
    * Q ≥ 0 at *every* grid point, since every count vector is realised by
      some u.

    So the level, nonnegativity and the normalisation at 0 are all
    preserved, as the task asked to verify.
  * *Step 4.* `|(⊗I)Q(0)| ≤ Π_g B_g(j_g) · Σ_{y∈grid_j} Π_g ψ_g(y_g) Q(y)
    ≤ Π_g B_g(j_g) · E Q(K)`. The second inequality uses Q ≥ 0 on the
    whole support. The product structure of the Lagrange weights makes the
    one-dimensional constants multiply. Correct.
  * *Step 5.* `Σ_g 19α j_g s_g ≤ 19αλ`.
    * `|Λ| ≤ Π_g(1+λ/s_g) ≤ (1+λ/s_*)^G`.
    * Jensen: `E f = E_w E_u f_w ≥ E_w e^{−Φ(w)} ≥ e^{−E_wΦ(w)}`.
    * `E_w q_g z_g = μ_g`, and concavity handles the log term.
    * `e^{−2αs_g} ≤ e^{−αs_i}` on `B_g`, since `s_i < 2s_g`.

    All correct.
* **Theorem 2.5 (CRT form).**
  * Given c, the coordinates `n mod ℓ^{E_ℓ}` (ℓ∈𝒫), the finer digits of
    the Q₀-primary part, and the free primes are independent (CRT). Since
    `x_ℓ` is a function of `n mod ℓ` only, conditioning on `(c,x)` keeps
    the product structure.
  * Each class indicator therefore conditions to a product of functions of
    `x_ℓ`, ℓ ∈ T_i. That is λ-level with weights `log ℓ`. Prime powers and
    free primes are harmless.
  * `ν_c(0) ≥ 1` needs `P(x=0|c) > 0`, i.e. `|F_ℓ(c)| < ℓ` for *all* ℓ,
    including invisible ℓ > e^λ. This is correctly listed as a hypothesis.
    Without it the statement is false: a fibre with no avoiders lets ν
    vanish there.
  * Jensen over c is fine: Φ_c is affine in `(p_ℓ(c))_ℓ` apart from the
    concave log term.
* **Uniformity in |𝒫|.** (2.4) depends on 𝒫 only through the truncated
  profile `Σ_{ℓ≤e^λ} p̄_ℓ ℓ^{−α}`, through `log μ̄`, and through
  `s_* = log min 𝒫`. Primes above e^λ enter only via `p_ℓ < 1`. The bound is
  uniform in |𝒫|, as claimed.

### 1.3 Independent exact-LP tests (`scripts/review_theta_lp.py`, own code)

* **Part A (CRT level).**
  * *Setup.* An exact LP over `ℤ/Q_tot` for ν in the span of all class
    indicators of slice-level ≤ λ. The small part is free.
    Configurations: Q₀ ∈ {2,3,4,6}, slice primes {5,7,11,13(,17)}, a
    prime-power coordinate 5², and a free non-slice prime 3. F_ℓ(c) is
    random with `|F_ℓ(c)| ≤ ℓ/4`, and λ ranges over log 5 … log 1001.
  * *Prediction.* The proof of Thm 2.5 shows `W_CRT ≥ (1/Q₀)Σ_{c∈R} W_bool(c)`.
    Lifting the Boolean fibre optima shows `≤`. So **equality** is the
    sharp prediction.
  * *Result.* Equality holds in every instance to 10⁻⁷
    (`data/theta/review_lp_partA.txt`). The conditioning step is therefore
    lossless, including the prime-power digits and the free primes.
  * *Theorem's bound.* (2.4), optimised over α, is always satisfied. It is
    extremely slack at these sizes: −log bound ≈ 130–430 against true
    savings ≈ 0.8–1.5, because of the additive `75G` and `C₄ = 8e⁵`. The
    theorem is asymptotic, so this is expected.
* **Part B (Proposition 2.4 chain).** 51 random multi-band weighted
  instances (n ≤ 7, p ≤ 1/4, up to 3 bands). Every inequality of the chain
  holds (`data/theta/review_lp_partB.txt`):

      W_bool ≥ E_w W_multi ≥ E_w[1/Σ_j|c_j|Π_g B_g(j_g)] ≥ e^{−E_w log Σ…} ≥ e^{−RHS(2.3)}

  * `W_multi` is the exact LP over P_{Λ'} on the count grid.
  * `B_g` is the exact `B(Y)` of the Lemma 2.2 node recipes.
  * Minimum gaps: `−2·10⁻¹⁶` and `−3·10⁻¹⁶` (rounding), then `0`, then
    `0.05`.
  * Thinning/symmetrisation loses at most 0.24 nats here. Lagrange
    interpolation loses up to ≈2 nats at these toy sizes.
* **Part C.**
  * The Lemma 2.3 identity holds to 10⁻¹¹ on 200 random lower sets with
    random non-nested nodes.
  * Lemma 2.2 (c) and (2.2) show 0 violations on 12 570 grid cases, with
    z up to 2000, q up to 1/4, k up to min(z,60), and boundary values
    `k = ⌊μ'/16⌋, ⌊μ'/16⌋+1`. The worst margin in (2.2) is 74.4 nats, i.e.
    the additive 74 is never needed in these cases.

### 1.4 Defects (item 1)

* **T1 (minor; summary table, §0, row "Thm 2.5", and the phrase
  "−O(log²λ)").**
  * *Problem.* The explicit error in (2.4) is
    `G(75+log(2+λ/s_*)) + (G/2)log(16μ̄+16)`. This is O(log²λ) only when
    `s_* ≫ 1` and `log μ̄ ≪ log λ`. In general μ̄ can be as large as
    `π(e^λ)/4`, which makes the term ≍ λ log λ. The 1.15 nats of
    `(16μ')^{1/2}` per band are genuine slack of the Lagrange method. Even
    a degree-0 band loses `½ log μ'`.
  * *Impact.* Harmless in every application, where `μ̄_λ ≪ λ³`.
  * *Fix.* Say "O(log²λ) provided μ̄ ≤ λ^{O(1)}", or keep the explicit
    form.
* **T2 (minor; Thm 2.5 statement, "Here μ̄ may be read as the truncated
  mass").** The truncated reading is the one that is proved: Step 0
  discards s_i > λ before μ is formed. Make it the definition rather than
  an aside. As stated, μ̄ is the untruncated mass, which can be infinite
  for infinite families, while the proof only needs the truncated one.
* **T3 (cosmetic; Prop 2.4 Step 5).** Write out the Jensen chain
  `E f = E_w E_u f_w ≥ E_w e^{−Φ(w)} ≥ e^{−E_wΦ(w)}`. The phrase "Jensen
  for exp and for log" is cryptic.
* **T4 (cosmetic; Lemma 2.2(a)).** Record that μ' ≥ 1 and q ≤ 1/4 give
  z ≥ 4. Otherwise `⌈μ'⌉ ≤ z−1` looks unjustified.

The literature status is unchanged from `reviews/theta-lit-notes.md`:
apparently new. My spot checks found nothing contrary. The mechanism
(Christoffel/Lagrange extremal mass, combination technique) is classical.
The weighted lower-set CRT statement is not in the sources consulted.

## Item 2 — Theorem 2.7, Lemma 2.8 (and the proof of Cor 3.6)

**Verdict: SOUND.** One minor repair (S1) and one remark (S2).

### 2.1 Theorem 2.7

* **History determines decided conditions.** Under (U), every
  requirement of a condition C other than its `ℓ(C)`-residue lies in Q₀ or
  in strictly earlier windows. So `F_ℓ(h)` is well defined from
  `H_{<j}`.
* **Base case.** `H_{<J+1}` contains `n mod Q₀` and every `n mod ℓ^{E_ℓ}`,
  with `E_ℓ ≥ e_{C,ℓ}`. This determines membership in 𝒜. So
  `g_{J+1} = E[ν | H] ≥ 1` on 𝒜-histories. Majorant terms with
  `ℓ^e, e > E_ℓ` are averaged by the conditional expectation and remain
  functions of the history. Harmless.
* **Induction step.**
  * Given `H_{<j} = h`, the digits `n mod ℓ^{E_ℓ}` (ℓ∈W_j) are independent
    and uniform. The `x_ℓ` are independent `Bern(p_ℓ(h))`.
  * `f(x) = E[g_{j+1} | h, x]` is a sum of products over
    `ℓ ∈ T_i ∩ W_j` of functions of `x_ℓ`. It is λ-level for the W_j
    weights (the level is charged afresh in every window, hence `19α_jλ`
    per window). It is ≥ 0, and `E f = g_j(h)`.
  * `{x = 0}` is exactly the event that no condition with last window j
    fires. The uniform law conditioned on `{h, x=0}` is the Q_seq
    transition, and this is the key identification. It holds because the
    excluded residues are exactly `F_ℓ(h)` and the higher digits stay
    uniform.
  * Jensen gives `f(0) ≥ exp(−E_{Q_seq}[Σ_{i>j}Φ_i | h])`.
  * Proposition 2.4 is applied to `f/f(0)` at the reachable h. The
    hypotheses `p ≤ 1/4` and `p < 1` are assumed on supp Q_seq, which
    equals `𝒜_{<j}`.

  Correct.
* **Conclusion.** The final Jensen over c and over histories is valid
  because Φ_j is affine in the `p_ℓ(h)` apart from the concave
  `log(16μ+16)`.

### 2.2 Lemma 2.8

* `E_{Q_seq} p_ℓ(H) ≤ Σ_{C: ℓ(C)=ℓ} ℓ^{−1}·Q_seq(other requirements of C)`.
  This is a union bound, since conditions can share a residue at ℓ.
* The chain rule bounds `Q_seq(n ≡ b mod ℓ'^e | past) ≤ 1/(ℓ'^e(1−p*_{ℓ'}))`.
* `P(c ≡ a_C mod q_C | c∈R)` is exact for c uniform on R.

Correct.

### 2.3 Exact-LP test (`scripts/review_theta_seq.py`, own code)

* **Setup.**
  * Q₀ = 4, R = {1,3}, windows W1 = {5,7} and W2 = {11,13}.
  * 8 random condition families of 7–13 conditions.
  * Conditions at W2 primes also fix residues modulo W1 primes (shared
    large primes) and modulo q | 4.
  * (U) is checked, and `p ≤ 1/4` is checked on every reachable history.
* **What is checked.** The exact CRT LP optimum is compared, at
  λ ∈ {log 7, log 13, log 77, log 143}, with the proof's rigorous
  intermediate, in which the exact Boolean window LPs replace
  Proposition 2.4:

      Eν ≥ Q₀⁻¹ Σ_c W_1(c) exp(E_{Q_seq}[log W_2(H) | c]) ≥ (|R|/Q₀) exp(avg_c[…]).

  Lemma 2.8's bound on `E_{Q_seq} p_ℓ` is checked per fibre.
* **Result.** All 32 instances pass (`data/theta/review_seq.txt`). The
  sequential chain loses at most 0.12 nats against the LP here. Its
  bound can exceed the void exponent `−log P(𝒜)`, which is legitimate:
  Q_seq is not the conditioned uniform law.

### 2.4 Cor 3.6 (proof re-derived)

* (U) holds for the windows `W_j = (e^{s_j}, e^{s_j/C}]`, because
  `ℓ' ≤ M/ℓ(M) ≤ ℓ^C`.
* `p*_ℓ ≤ ℓ^{C−1+o(1)}`. The o(1) comes from `|ℛ(M)| ≤ τ(A²) = M^{o(1)}`
  and from the (a,D)-multiplicity `≤ τ(G)2^{ω(G)}`.
* For the n = 1 argument I checked forcedness of the Lemma 3.2 classes
  algebraically. If `D | A_M²`, then `−4D ≡ −D/A (mod M)`. Since
  `|v_p(D) − v_p(A)| ≤ v_p(A)` for every p, the reduced fraction `u/v` of
  `D/A` has `uv | A`, so `−4D mod M ∈ ℛ(M)`.
* Then `|R|/Q₀ ≥ 1/L'`, and `P(c≡a (q_C) | R) ≤ L'/φ(q_C)`. The latter
  is also fine for non-unit a, where it is 0 or smaller.
* The γ-weighted Lemma 3.1:
  * `h(p) ≤ 1/(p−1) + 3p^{−δ}`.
  * `Σ h(d)/φ(d) < ∞`.
  * `Σ h(d)d^{−1+δ/2} < ∞`, because its Euler factors are
    `1 + O(p^{−1−δ/2})`.
  * Tail `≪ x^{1−δ/4+ε}`.

  Correct.
* Per-window sums: the cubic branch below `s ≍ λ^{1/4}`, the
  `λ^{3/4}C^k(1+k)` tail above it, and `O(log λ)` windows × `O(log²λ)`
  remainders. Correct.

### 2.5 Defects (item 2)

* **S1 (minor; Cor 3.6, "Q₀ = lcm(P_{w₀}, w₀-smooth parts of all
  moduli)").**
  * *Problem.* Q₀ is family-dependent and can be astronomically large,
    since w₀-smooth parts of moduli are unbounded. That is harmless,
    because only `|R|/Q₀ ≥ 1/L'` enters. But the sentence "The last term
    is O_C(1)" follows the definition of Q₀ and reads as if Q₀ itself were
    bounded.
  * *Fix.* Say explicitly that `Q₀/|R| ≤ L' = lcm(P_{w₀}, w₀-smooth moduli)`
    and that `L' ≤ e^{O(w₀^{1+C})}`, while Q₀ itself is unbounded.
* **S2 (cosmetic; Cor 3.6 "Per window").** `s_j` is never defined. The
  bounds `M ≤ e^{2s_j/C}` and `ℓ^{−α} ≤ e^{−αs_j}` are consistent only if
  `s_j = s₀C^{−j+1}` is the log of the *lower* endpoint of W_j. Define it.

## Item 3 — Scope of Corollaries 3.4–3.6

**Verdict: SOUND-AFTER-REPAIRS.** The corollaries are correct as literally
stated, since each carries "level λ ≤ A log N". The interpretive layer
around them (§0 Verdict, Lemma 4.1 "binding constraint", §6) drops or
misattributes that hypothesis. One repair lemma (Lemma R below, proved
here) closes most of the gap.

### 3.1 Is the 3/4 note's actual majorant literally in the class? Yes.

I checked against `paper/es-threequarter-note.tex` (§§2, 7, 8).

| requirement (§1, Cor 3.4) | 3/4 note | check |
|---|---|---|
| prime-slice system | `Q₀ = lcm(L_K, P_y)`, `𝒫 = primes in (X^{1/2}, X]`, conditions `n ≡ −uv⁻¹ (mod kℓ)` with `k | L_K` | ✓. `ℓ > X^{1/2} > K ≥ y`, so `ℓ ∤ Q₀` |
| `F_ℓ(c)` | projections mod ℓ of the atoms active in c (`k | u+cv`) | ✓ (lem:CRT) |
| `|F_ℓ(c)| ≤ ℓ/4`, `< ℓ` | `≤ z_j² ≤ ℓ^{1/3}` | ✓ |
| `q₀ ≤ ℓ^C`, C < 1 | `k ≤ X^κ ≤ ℓ^{2κ}`, 2κ < 1/120 | ✓ |
| forced classes of Lemma 16.1 | atoms are ℛ(kℓ) classes (multiplier identity) | ✓ |
| selector R | `S_y = 1[(n,P_y)=1]`, R = `{(c,P_y)=1}` | ✓ |
| ν ≥ 0 on all of ℤ | `S_y Q_r(H_X) ≥ 0` (lem:Bonferroni) | ✓ |
| ν ≥ 1 on 𝒜 | `Q_r(0) = 1`, `S_y = 1` | ✓ (on *all* avoiders, not only primes) |
| finite class combination | the expansion (termq) | ✓ |
| level | distinct atoms in a nonempty term have distinct ℓ (lem:CRT), so slice level ≤ `rt` | ✓ |
| final bound `N·Eν + rounding ≥ 0` | (transfer): `N·E_CRT ν + O(T_abs)` | ✓ |
| fibre profile | cor:fibremass upper half, uniform in all c | ✓ |

So Theorem 2.5 applies to the note's ν verbatim, for every t, κ, r, B.
The cap of Lemma 4.1 is correct.

### 3.2 Defect SC1 (MAJOR as an interpretive claim; the theorems are unaffected)

* **Location.**
  * §0 Verdict: "That world is: every condition's modulus has a prime
    factor ≥ M^{1/(1+C)}, the admissible set has bounded saving, and the
    final bound has the form N·Eν + (nonnegative rounding bound)."
  * Lemma 4.1: "the binding constraint … (level) λ ≤ A·log N".
  * The binding table: "level `r t ≲ L`".
* **The problem.**
  * In the 3/4 note the transfer `N·Eν + O(T_abs)` uses
    `#{n ≤ N : n ≡ a (q)} = N/q + O(1)` for *every* q. The note says
    explicitly that `q_max ≤ N^{1/2}` "is convenient but not necessary".
  * The constraint that actually forces `rt ≲ L` in the note is the
    coefficient budget `log T_abs ≤ ½ log N`.
  * Theorem 2.5 caps majorants of bounded *level*, not of bounded
    coefficient sum.
  * The §0 Verdict omits the level hypothesis altogether. As written it
    is therefore not implied by Thm 2.5/2.7. It would admit a
    hypothetical majorant of level ≫ log N with small coefficient sum.
  * The note itself (§9, Remark "scope of the ceiling") warns that "a
    sufficient product-tail or coefficient budget has not been proved
    necessary".
* **Repair.** The following is my lemma, with proof. It makes the
  coefficient budget imply the level hypothesis, provided the family's
  slice primes are bounded.

> **Lemma R (coefficient budget ⇒ level).** Let ν = Σ_i a_i 1[n ≡ b_i (d_i)]
> be ≥ 0 on ℤ and ≥ 1 on 𝒜, with `T = Σ|a_i|`. Assume every slice prime
> satisfies `log ℓ ≤ Λ₀`. Then for every λ there is a majorant ν' of level
> ≤ λ with `ν' ≥ ν` pointwise and `Eν' ≤ Eν + T·e^{Λ₀−λ}`. In particular,
> with `λ = Λ₀ + log T + log(1/Eν)`, we get `Eν' ≤ 2Eν`.
>
> *Proof.* Leave terms of level ≤ λ alone. Drop each term of level > λ
> with `a_i < 0`; this raises ν pointwise and costs `|a_i|/d_i ≤ |a_i|e^{−λ}`.
> For each term of level > λ with `a_i > 0`, list its slice primes in
> increasing order and keep the longest prefix of level ≤ λ. The prefix
> has level `> λ − Λ₀`. Replace `d_i` by the divisor d'_i consisting of the
> non-slice part times the kept prime powers. Since `d'_i | d_i`, we get
> `1[n≡b_i (d'_i)] ≥ 1[n≡b_i (d_i)]`, and the mean rises by at most
> `a_i/d'_i ≤ a_i e^{Λ₀−λ}`. Then ν' ≥ ν ≥ 0 and ν' ≥ 1 on 𝒜. ∎

* **Consequence.** Put Cor 3.4/3.6 together with Lemma R.
  * *Hypotheses.* The family's slice primes are ≤ N^A, and the method's
    final bound `N·Eν + Σ|a_i|` is non-trivial, so `T < N`.
  * *Bound.* The saving s satisfies
    `s ≤ log 2 + C(λ)^{3/4} + (R-term)` with `λ ≤ (A+1)log N + s`. Hence
    `s ≪_A (log N)^{3/4}`.
  * *What this covers.* This puts the 3/4 note's real constraint
    (`T_abs ≤ N^{1/2}`) inside the theorem.
* **Residual scope (state it).**
  * (i) Families with slice primes > N^{O(1)} remain formally outside.
    Lemma R needs Λ₀. I see no way to remove large-prime conditions
    without breaking majorization.
  * (ii) The rounding bound must be the absolute coefficient sum, or
    anything ≥ it. A method whose rounding bound uses *which* classes meet
    [1,N] is on the non-CRT/"signed rounding" side.
* **Fix.**
  * Add Lemma R.
  * Redefine the architecture in §0 and §6 as "final bound
    `N·Eν + Σ_i|a_i|`, family moduli ≤ N^{O(1)}". Alternatively keep
    "level ≤ A log N" explicitly in the §0 Verdict.
  * In Lemma 4.1 and the binding table, replace "(level) λ ≤ A log N" by
    "(coefficient budget) log T_abs ≤ log N, which forces λ ≲ log N via
    Lemma R".

### 3.3 What is excluded (precise list, checked against the proofs)

1. **Majorants not ≥ 0 on all of ℤ.** A majorant that is ≥ 0 only on
   [1,N] is excluded. The doc's remark that such a relaxed LP is the exact
   count is correct: level-N classes restrict to point masses on [1,N].
2. **Signed rounding.** Any bound exploiting cancellation in
   `Σ_{n≤N}ν − N·Eν`, or a rounding bound smaller than Σ|a_i| (see SC1(ii)),
   is excluded.
3. **Non-CRT inputs.** Type I/II sums, arithmetic of `x = (p+a)/4`,
   Halász: Thm 2.5 sees only the CRT law of residues. Also excluded are
   majorants that are ≥ 1 only on exceptional *primes* and use prime
   equidistribution beyond the selector coordinates. A CRT-periodic ν that
   is ≥ 1 on the exceptional primes need only be ≥ 1 on the residue cells
   they occupy. Thm 2.5 requires ≥ 1 on all of 𝒜. This is the right
   model for "sieve on the avoider set", but it should be named.
4. **Balanced moduli.** Cor 3.6 needs *every* modulus of the family to
   have `P(M) ≥ M^{1/(1+C)}` with C < 1 fixed. Excluded are families
   containing any balanced modulus (two or more comparable large primes),
   and moduli with `P(M) ∈ (M^{1/2}, M^{1/(1+C)})` for the chosen C, since
   the constants blow up as C → 1. Lemma 3.8 shows this excluded part
   carries `≫ (log x)³` supply (item 4), so the exclusion is not
   cosmetic. For Λ²-majorants only, Thm 5.5 reduces it to the open
   H_MS^{Sel}.
5. **Non-selector R.** The term `log(Q₀/|R|)` is uncontrolled.
   Pure small-modulus subsystems with large void are outside (H_MS).
   Cor 3.6 handles the w₀-smooth part only because w₀ = O_C(1).
6. **Prime-slice requirement of Cor 3.4.** Multiplier parts must avoid
   slice primes, i.e. `q₀ | Q₀`, `ℓ ∤ Q₀`. Cor 3.6 removes this, but only
   for dominant-prime moduli.
7. **Level/size.** See SC1. Level ≤ A log N is literal in Cor 3.4/3.6.
   With Lemma R it may be replaced by the coefficient budget plus slice
   primes ≤ N^{O(1)}.
8. **Large sieve.** Only the Montgomery large sieve over a slice system,
   fibre by fibre, is covered (Remark 2.6). No sequential or shared-prime
   large-sieve statement is made, and the doc says so.

### 3.4 Cor 3.5 (2/3-loglog note)

* The LL note uses `K = ⌊δ log N⌋`, `L_K ≤ N^{1/2}`, and Montgomery's
  large sieve on progressions mod L_K with `Q² ≤ N/L_K`
  (`paper/vaughan-loglog-note.tex` l. 97, 393). Remark 2.6's Rankin bound
  `S_c(Q) ≤ exp{α log Q + 2Σ p_ℓ(c)ℓ^{−α}}` (for `p_ℓ ≤ 1/2`) applies
  fibrewise. Correct.
* The claim `h(𝒦) ≤ Π_{p | lcm}(1+1/p)` looked suspicious, since
  `Σ_{k|L} 1/k` is larger. It is in fact exact for φ-weights:
  `Σ_{i≤a} φ(p^i)/p^{2i} ≤ (1−1/p)Σ_{i≥1}p^{−i} = 1/p`. Correct.
* The supremum computation `≍ λ^{2/3}h^{1/3}` is right.
* "Sharp for its architecture" means: given the note's own uniform BT
  upper bound on the fibre mass, no majorant or large sieve on that slice
  system saves more than `L^{2/3}(log L)^{1/3}`. This is the order the
  note achieves (thm:main there). Correct, with the label "given the
  notes' BT upper bounds" as stated.
* **SC2 (minor).** Cor 3.5 needs the fibre-mass upper bound
  `Σ_ℓ p_ℓ(c) ≤ A₀t²h(𝒦)` for *every* fibre c in R. The LL note proves
  it for reduced c. Non-reduced c have R-weight 0 if R is the reduced
  set, but then `log(L_K/φ(L_K)) ≍ log log K` enters as the R-term.
  * *Fix.* Mention the R-term in Lemma 4.4. It is negligible.

## Item 4 — Lemma 3.7, Lemma 3.8, Theorem 5.5 (+ Prop 5.7, Cor 5.6)

**Verdicts.**

| result | verdict |
|---|---|
| Lemma 3.7 | SOUND |
| Lemma 3.8 | SOUND |
| Theorem 5.5 | SOUND |
| Cor 5.6 | SOUND |
| Prop 5.7 | SOUND |

One minor defect (L1) and one remark (L2).

### 4.1 Lemma 3.7 and Elsholtz–Tao Prop. 1.4

* **The cited statement.** I checked it against `sources/elsholtz-tao-1107.1010.pdf`
  (p. 6 of the text and §7). Verbatim: "For any A, B > 1, and any positive
  integer k ≪ (AB)^{O(1)}, one has Σ_{a≤A}Σ_{b≤B} τ(kab²+1) ≪ AB log(A+B)
  log(1+k)." The squared variable is b.
* **The mapping.** Lemma 3.7 writes
  `4rh² = (4st²)·r'h'²`, with linear variable `a = r'`, squared variable
  `b = h'`, and `k = 4st²`. This matches ET's own use in their (8.2):
  `k = 4s²t`, with the roles of the variables swapped, since their squared
  variable is a.
* **The range of k.** For `st ≤ √x` we have `st² ≤ (st)² ≤ x`, so
  `k ≤ 4x`. Each rectangle has `AB ≥ Y/2 ≥ √x/2`. So `k ≤ 16(AB)²`, a
  fixed power, and the implied constant is uniform. The doc's
  `k ≤ 4x^{3/2} ≪ (AB)³` is a weaker but also valid bookkeeping.
* **The remaining steps.**
  * `n/φ(n) ≤ ζ(2) Σ_{d|n} 1/d`, and `Σ_{d|rh} 1/d ≤ Σ_{s|r}Σ_{t|h} 1/(st)`.
  * The dyadic hyperbola cover by `O(log Y)` rectangles with `AB ≍ Y`.
  * `Σ log(1+4st²)/(st)² < ∞`.
  * The tail `st > √x` is `≪ x^{1/2+2ε}`.
  * The γ-variant.

  All correct.
* **"Exactly the dyadic form of (3.7)".** ET (8.2) is
  `Σ_{N/2≤ad≤N} τ(4a²d+1)/φ(ad) ≪ log²N`. Multiplying by N gives the
  dyadic block of (3.7). Correct.
* **Numerics (EVIDENCE, own code).** `S(x)/(x log²x)` = 1.99, 1.88, 1.83,
  1.79 at x = 300, 10³, 3·10³, 10⁴ (`data/theta/review_lemma37.txt`).
  These are bounded and slowly decreasing.
* **L1 (minor; §3 "Case A", "This reduction is PROVED").** The claim that
  Case A of notes Theorem 3.1 reduces to the classes
  `n ≡ −m⁻¹ (mod 4g(d))`, `m | 4d+1`, is given a one-line justification
  and labelled PROVED. It is not one of the items under review, and I did
  not re-derive it. Note that a brute-force check is vacuous here, since
  ES is verified far beyond any test range. Lemma 3.7 only bounds the
  supply of these classes; whether they *are* the Case-A family rests on
  notes Thm 3.1.
  * *Fix.* Cite the exact notes lines, or add the two-line derivation.

### 4.2 Lemma 3.8

* **Ranges.**
  * `M ≤ Y^{2+4.5η} = x`.
  * `M > Y^{2+2.5η}`, so `√M ≥ Y^{1+1.25η} ≥ ℓ₂ = P(M)`: M is balanced.
  * The triple `(k,ℓ₁,ℓ₂)` is recoverable from M.
* **Classes.** `−uv⁻¹ (mod M)` lies in ℛ(M) via the multiplier identity
  with `A = (M+1)/4 = uv·w`. Distinct reduced `(u,v)` give distinct
  residues mod ℓ₂, since `|uv'−u'v| < z² < ℓ₂`.
* **Primes in progressions.** The moduli are `q = 4uv ≤ 4Y^{1/4} ≤ y^{1/4}`,
  inside the BV range. Partial summation gives an error `≪ E**_y(q)/y`.
  The τ(q)-weighted BV goes via Cauchy–Schwarz against BT. The total error
  is o(1). Correct.
* **Lattice step.** Summing eq. latlower of the 3/4 note over the φ(k)
  unit residues c (k odd) gives `(1/4)(φ(k)/k)²Λ²`. The lemma's
  requirement `z ≥ K^{20}`, with `H = K^{10}` and `K = Y^{3η}`, is exactly
  `η ≤ 1/480`. The main term needs `(a,4uv) = 1` with
  `a = −(kℓ₁)⁻¹`, which holds.
* **Totals.** `S ≫ η·log Y × log(1+η/2) × c'_η × (log Y)² ≍_η (log x)³`.
  Correct.
* **L2 (remark).** Lemma 3.8 measures the *unweighted-by-profile* supply
  `Σ|ℛ(M)|/M`. That is the right quantity for the claim "not lower order".
  The doc correctly refrains from claiming that windowing must fail; see
  its last paragraph of §3.8. No defect.

### 4.3 Theorem 5.5, Cor 5.6, Prop 5.7

* **Theorem 5.5.**
  * `P(A) ≤ E[g1_A] = ⟨g, Π_V 1_A⟩ ≤ ‖g‖‖Π_V1_A‖`.
  * `V_{λ/2} = ⊕_{c(T)≤λ/2} H_T`, because the index family is
    down-closed.
  * `Σ_{c(T)≤λ/2}‖(1_A)_T‖² ≤ e^{αλ/2}Σ_T e^{−αc(T)}‖(1_A)_T‖² = e^{αλ/2}P(A∩A'_α)`.
  * `P(A∩A') ≥ P(A)²`, because T_ρ is PSD with `(1_A)_∅ = P(A)`.

  Nonnegativity of g is *not* needed; g² ≥ 0 is automatic. Correct. The
  claim is honestly restricted to squares g². Nothing is claimed for
  general majorants on non-slice systems.
* **Cor 5.6.** A coordinate factor
  `[ρ(1−p) + (1−ρ)(1−p)²]/(1−p)² = 1 + ρp/(1−p)`. Correct.
* **Prop 5.7.** J is affine in ρ_ℓ with slope
  `|F∩F'|/ℓ − pp'`. Correct.
* **The 0.01015 example.** Recomputed: `P(C∩C') = p·(5/9)(9/25)`, and
  `Ξ = log(0.88/0.87111) = 0.01015`. Correct.
* **Numerics (own code, `scripts/review_theta_selberg.py`,
  `data/theta/review_selberg.txt`).**
  * *Theorem 5.5.* 25 random arbitrary events on `ℤ/m₁×…×ℤ/m_k`. They
    include pair and triple AND-conditions, i.e. "balanced" ones. In every
    instance:
    * the convex-QP optimum `min E g²` (g ∈ V_{λ/2}, g ≥ 1 on A) ≥ the
      projection bound `P(A)²/‖Π_V1_A‖²`;
    * that in turn ≥ `max_α e^{−αλ/2}P(A)²/P(A∩A'_α)`.
  * *Prop 5.7.* The derivative formula matches central finite differences
    to 2·10⁻¹⁰ on 10 random events at random ρ.
* **H_MS^{Sel}** is correctly labelled open. Assessment 5.8 is correctly
  labelled heuristic, and its non-negligible lower-support terms are
  disclosed.

## Item 5 — §4 accounting (Lemmas 4.1–4.4) and summary consistency

**Verdict: SOUND-AFTER-REPAIRS.** The repairs are the SC1 rewording, plus
A1–A3.

* **Lemma 4.1.**
  * The membership table of item 3.1 confirms every hypothesis.
  * The cap computation is right:
    * `α → 0` gives `C₄μ̄ ≤ Ct³`;
    * `α = (2/t)log⁺(t⁴/λ)` gives `O((λ/t)(1+log⁺(t⁴/λ)))`;
    * the peak is at `t ≍ λ^{1/4}`.
  * The R-term is `log(P_y/φ(P_y)) = log log y + O(1)`.
  * The defect is the attribution of the binding constraint to "level"
    (SC1).
* **Lemma 4.2.**
  * `Q_r(h) = C(h−1,r)`.
  * In a fibre `H_X = Σ_ℓ x_ℓ` with independent Bernoulli `x_ℓ`, since
    atoms at one ℓ have disjoint projections (lem:CRT). So `Var H ≤ μ`,
    and Chebyshev gives ≥ 3/4.

  Correct.
* **A1 (minor; Lemma 4.3).**
  * *Problem.* The "proof" re-runs the unpruned-supply theorem with
    `x^{ϑ'}`. That is a description of a construction, not a proof that
    *no* use of EH can raise the profile.
  * *Why the conclusion still holds.* There is a cleaner and fully
    rigorous reason: Lemma 3.1 bounds the *entire* identity-class supply
    by `≪ x log²x`, independently of any level of distribution. So
    Thm 2.5 caps every EH-based variant on Case-B forced classes at
    `λ^{3/4}`.
  * *Fix.* Cite Lemma 3.1 (and Lemma 3.2/3.7 for the other groupings) as
    the reason.
* **Lemma 4.4.** Correct, given Cor 3.5. See SC2 for the R-term.
* **A2 (minor; binding table and §0 "PROVED (Lemmas 4.1–4.4)").** The
  statement "Bonferroni depth … not binding: change constants only" is
  proved only in the *upper* direction: no alternative beats the cap.
  §2.5 shows by EVIDENCE only that Selberg attains it up to constants.
  * *Fix.* Label "constants only" as "cannot improve the exponent
    (PROVED)". Whether alternatives attain the same constant-order
    saving is EVIDENCE.
* **A3 (minor; AGENT_REPORT_A2.md l. 74–76).** "The class contains
  Vaughan, PW, the 2/3-loglog note and the 3/4 note." For the 3/4 note
  this is true literally (item 3.1). For Vaughan, PW and LL it is true via
  Remark 2.6, which covers Montgomery's large sieve, not a majorant.
  * *Fix.* Say so. Also add the SC1 qualification to the report's "3/4 is
    sharp" sentence.
