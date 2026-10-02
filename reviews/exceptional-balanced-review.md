# Hostile review — EXCEPTIONAL_BALANCED.md (task a3, branch side-agent/balanced-moduli-2)

Reviewer: side agent (review-balanced). Subject files brought in verbatim from
`side-agent/balanced-moduli-2`: `EXCEPTIONAL_BALANCED.md` (EB),
`reviews/agent-reports/AGENT_REPORT_A3.md`, `scripts/balanced_*.py|cpp`,
`data/balanced/`. Context: `EXCEPTIONAL_THETA.md` (ET).

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects numbered
D1, D2, … with severity (CRITICAL / MAJOR / MINOR / COSMETIC).

## Verdict summary

(filled in as items are checked)

## Item-by-item

### Item 1 — Lemma 2.1 (η-gapped ⇒ (U)). Verdict: **SOUND** (minor scope nits)

Checked line by line.
* (1) `ℓ² | M ⇒ P(M/ℓ) = ℓ ⇒ P₂ = ℓ`, and `ℓ ≥ ℓ^{1+η}` fails for ℓ > 1. ✓.
* (2) `ℓ' | M/ℓ ⇒ ℓ' ≤ P₂`, so `log ℓ ≥ (1+η)log P₂ ≥ (1+η)log ℓ' > (1+η)s_j = s_{j+1}`;
  hence ℓ ∉ W_j and lies in a later window. ✓ Primes `≤ w₀` go to Q₀, and
  `ℓ = P(M) > w₀` gives `S(C) ≠ ∅`, `ℓ ∤ Q₀`. Together with `e_{C,ℓ} = 1`, this is
  exactly ET (U). Higher powers of earlier primes are allowed by ET §2.6. ✓
* Scope bullets. "Dominant ⇒ gapped with η = 1/C−1": correct (`P ≥ P₂^{1/C}`).
  "Gapped balanced ⇒ q = M/P ≥ P": correct. "Lemma 3.8 pairs are η-twin":
  P₂ = ℓ₁ because k's primes are < Y, and `log ℓ₂/log ℓ₁ < 1+η_{3.8}`. ✓ Since
  η-twin sets are increasing in η, the supply claim "≫_η (log x)³ for every η > 0"
  follows (take η' = min(η, 1/480) in ET Lemma 3.8). ✓

**D1 (COSMETIC, §2.1 Scope).** "Dominant moduli are gapped … with `η = 1/C − 1`"
conflicts with the convention `0 < η ≤ 1` when C < 1/2, and it also needs
`P(M) > w₀`. Fix: say "η = min(1, 1/C−1); moduli with P(M) ≤ w₀ are w₀-smooth and
excluded". Similarly, "`M = kℓ₁ℓ₂` with k small, `ℓ₂ ≥ ℓ₁^{1+η}`, `kℓ₁ ≥ ℓ₂`" forces
`k ≥ ℓ₁^η`, so k is not small. Fix: drop "small".

### Item 2 — Lemma 2.2 (heavy coordinates conditioned out). Verdict: **SOUND**

* *Independence of x_H and x_{I'}.* In the Boolean setting of ET Prop 2.4 all
  x_i are independent by hypothesis. In the application (Thm 2.3 induction step),
  ET's own step gives independence of the window-j indicators given `H_{<j} = h`.
  ✓
* *E f ≥ Π_{i∈H}(1−p_i)·E f̃.* f ≥ 0 gives `E f ≥ E[f·1{x_H=0}]`, and
  independence factors this as `P(x_H=0)·E[f(x_{I'},0_H)]`. ✓
* *f̃ is λ-level.* Each `f_T(x_{T∖H}, 0_{T∩H})` depends on `x_{T∖H}` and
  `Σ_{T∖H} s_i ≤ Σ_T s_i ≤ λ`. ✓ *f̃ ≥ 0*: restriction of f ≥ 0. ✓
  *f̃(0) = f(0) ≥ 1.* ✓
* *Hypotheses of Prop 2.4 for f̃ on I'.* Every i ∈ I' with s_i ≤ λ has
  `p_i ≤ 1/4` by the definition of H. Coordinates with `s_i > λ` are never heavy,
  and they only need `p_i < 1`, which is kept. The weight floor s_* may be taken
  unchanged (a lower bound for a subset). ✓
* *Degenerate case.* If I' has no coordinate with s_i ≤ λ, f̃ is constant ≥ 1.
  The bound is then `0 + Σ_H`, which is ≤ the stated one if `RHS(2.3)[∅]` is
  read as 0. Harmless.
* *Sharpness remark.* `f = 1{x_i=0}` has `E f = 1−p_i`. ✓ (Sharp for the heavy
  part only; the light part still pays the ET overhead. "Sharp in form" is fair.)

No defects.

### Item 3 — Theorem 2.3 (sequential bound for gapped families, given (NDE)). Verdict: **SOUND** (one scope repair)

I re-read ET Thm 2.7's proof (ET l. 450–493) for every use of `p ≤ 1/4`.
* The base case, the definition of `g_j`, the λ-level property of
  `f = E[g_{j+1} | h, x]`, the identification of the law given `x = 0` with the
  Q_seq transition, and the final Jensen over c use only independence of the
  window-j indicators given h, `f ≥ 0`, and `P(x=0 | h) > 0`. None uses `p ≤ 1/4`. ✓
* The only use is "Proposition 2.4, applied to f/f(0)". Replacing it by Lemma 2.2
  gives `E f ≥ f(0)·Π_{ℓ heavy}(1−p_ℓ(h))·e^{−Φ_j^{light}(h)}`. The heavy set
  depends on h, which is harmless because the step is fibrewise. The heavy charge
  then sits inside `E_{Q_seq}[·|H_{<j}=h]` like the rest of Φ_j. No Jensen is
  applied to the (convex in p) term `−log(1−p)`, and none is needed, since (2.1)
  keeps it inside the expectation. ✓
* (NDE) is exactly ET's hypothesis "`p_ℓ(h) < 1` on the support of Q_seq",
  including for primes with `log ℓ > λ`. It is needed there too (the transition
  must be defined). ✓ ET's (U) holds by Lemma 2.1. Primes > w₀ do not divide Q₀. ✓
* "Windows with `s_j ≥ λ` contribute 0": all their primes have `log ℓ > s_j ≥ λ`. ✓

**D2 (MINOR, §2.3 "R = ℤ/Q₀").** The theorem fixes `R = ℤ/Q₀`. §1 defines the
avoider set "plus an admissible small-residue set R". A majorant of
`𝒜(𝔊) ∩ {n mod Q₀ ∈ R}` for a selector R (as in the 3/4 note, or as in ET
Cor 3.6, which folds w₀-smooth forced moduli into R) is **not** a majorant of
`𝒜(𝔊)` with R = ℤ/Q₀. So Thm 2.3 as stated does not cover selector
architectures. It also does not cover the forced classes with w₀-smooth modulus,
which gapped families exclude by definition. Yet m_j (Lemma 2.4) carries the
selector weight M/φ(M), as if a selector were intended. Fix: state Thm 2.3 for
general R with the extra term `log(Q₀/|R|)`. This is verbatim ET (2.6). In
Lemma 2.8, use `P(c ≡ a_C (q_C) | R) ≤ L'/φ(q_C)` as in ET Cor 3.6 to justify
the M/φ(M) weight.

### Item 4 — Lemma 2.4 (window masses). Verdict: **SOUND**

* `P(M) ∈ W_j`, `M ≤ P^{1+B}` ⇒ `M ≤ e^{(1+B)s_{j+1}} = e^{(1+B)(1+η)s_j}`. ✓
* `|ℛ(M)| ≤ τ(A²)` (ℛ(M) = {−4D : D | A²}). ✓ The partial summation from ET
  Lemma 3.1, `Σ_{M≤x} τ(A²)(M/φ(M))/M = S_B(x)/x + ∫_1^x S_B(t)t^{−2}dt ≪ (log 2x)³`,
  gives the first claim. `log x ≥ s₀ ≥ log 3` keeps the constant uniform. ✓
* The second claim uses `P(M)^{−α} < e^{−αs_j}` and `(1+η) ≤ 2`. The stated
  `(4(1+B)s_j)³` is looser than the available `(2(1+B)s_j)³`. Harmless.
* The remark that a smooth-cofactor Shiu bound would give `η s_j³` is correctly
  marked as not available, and it is not used.

No defects. (The mass `m_j` is an *upper* bound of the uniform profile only. That
matters for item 5, D4.)

### Item 5 — Theorem 2.5 (conditional cap under H_light(K)). Verdict: **SOUND-AFTER-REPAIRS**

Derivation re-done from (2.1).
* *One band per window.* Costs in W_j lie in `(s_j,(1+η)s_j] ⊂ [s_j, 2s_j)` for
  η < 1. ET Prop 2.4's **statement** sets `G = ⌊log₂(λ/s_*)⌋+1`. That value
  depends on λ/s_*, not on the spread of the weights. With `s_* = s_j` it is
  `≍ log(λ/s_j)`, not 1. The claim `G = 1` is true only via the **proof** of
  Prop 2.4. There, Step 0 discards empty bands, and every G-dependence comes from
  nonempty bands: `|c_j| ≤ 2^G` (Lemma 2.3 over coordinates g), `|Λ| ≤ (1+λ/s_*)^G`,
  and `Σ_g`. So "G = #nonempty bands" is a valid refinement, but it is
  undeclared (D3). Without it the error grows by one factor log λ, and the main
  term is unaffected.
* *E log μ_j.* `E log(16μ_j+16) ≤ log(16 E μ_j + 16) ≤ log(16Km_j+16)` by
  concavity and H_light(ii). ✓ With Lemma 2.4 this is
  `O(log K + log λ + log(1+B))`. The `log(1+B)` is dropped in the statement.
  This is COSMETIC, since B is fixed, but the theorem tracks B elsewhere.
* *Number of windows.* `log(1+η) ≥ η log 2` on [0,1] gives
  `#{j : s_j ≤ λ} ≤ 1 + log(λ/s₀)/(η log 2) ≤ 1 + 2η^{−1}log λ`. ✓
* *Window optimisation.* `inf_{α>0}[19αλ + X e^{−αs}] ≤ min{X, (19λ/s)(1+log⁺(Xs/19λ))}`. ✓
  With `X(s) = C₄Kc_B s³`, `X(s*)s* = 19λ`. ✓ Below s*:
  `Σ X_j ≤ X(s*)/(1−(1+η)^{−3}) ≤ (2/η)X(s*) = 38λ/(ηs*)`. ✓ (Uses
  `1−(1+η)^{−3} ≥ 3η/(1+3η) ≥ η/2`.)
* **D3a (MINOR, arithmetic, "windows above s*").** The doc bounds the k-th window
  above s* by `(19λ/s*)(1+η)^{−k}(1+4k log(1+η))`. That pairs `1/s_j ≤ (1+η)^{−k}/s*`
  (true, since `s_j/s* ≥ (1+η)^k`) with `log(s_j/s*) ≤ k log(1+η)`. The second
  is false: `s_j/s* ∈ ((1+η)^k, (1+η)^{k+1}]`, and `t ↦ (1+4log t)/t` is not
  monotone on `[1, e^{3/4}]`. Correct bound:
  `(19λ/s*)Σ_k(1+η)^{−k}(1+4(k+1)log(1+η)) ≤ (19λ/s*)·[(1+η)/η + 4(1+η)²/η] ≤ (19λ/s*)·18/η`.
  The total constant becomes `38+342 = 380` instead of 228. Only constants change.
* *Heavy charge.* At most `Kλ^{3/4}` by H_light(iii), added verbatim. ✓
* *Final form.* `λ/s* = λ^{3/4}(C₄Kc_B/19)^{1/4} ∝ K^{1/4}(1+B)^{3/4}λ^{3/4}`. ✓

**D3 (MINOR, Thm 2.5 proof, "So each window is a single band of ET Prop 2.4,
with G = 1").** As explained above, this is not what Prop 2.4 states. Fix: add a
one-line lemma: "In Prop 2.4, G may be replaced by the number of nonempty
bands `B_g`, and `log(2+λ/s_*)` by `log(2+λ/s_min)`." Also note the edge case
`η = 1`, where `(1+η)s_j = 2s_j` is not inside `[s_j,2s_j)`. Use `η < 1`, or
allow G = 2.

**D4 (MAJOR, H_light(ii) vs. what is delivered; affects the §2.5 "Sanity check",
§2.6 "(★_δ) ⇒ H_light(O_δ(1))", and Prop 4.4).** H_light(ii) asks for
`E_{Q_seq}Σ_{ℓ∈W_j} p_ℓ ≤ K·m_j`, with m_j the **unweighted** uniform window mass.
What ET Lemma 2.8 plus (★_δ) actually gives is the **γ-weighted** mass
`m_j^γ = Σ_{P(M)∈W_j} |ℛ(M)|γ(M)/M`, with `γ(M) = Π_{ℓ'|M,ℓ'>w₀}(1−ℓ'^{−δ})^{−1}`
(and a factor L' for a selector R). γ is unbounded, since
`γ ≥ (1−w₀^{−δ})^{−ω(M)}`, and m_j has no proved lower bound (Lemma 2.4 is
upper only). So `m_j^γ ≤ O_δ(1)·m_j` is **not** proved, and "H_light(O_δ(1))"
is not literally established anywhere. The doc's hedge "in γ-averaged form" names
this but never defines that form. Fortunately the proof of Thm 2.5 uses (ii) only
through `K·m_j ≤ K·C₆'(2(1+B)s_j)³`. Fix: restate H_light(ii) as
`E_{Q_seq}Σ_{ℓ∈W_j} p_ℓ ≤ K·((1+B)s_j)³`, the cubic window bound. ET Cor 3.6's
γ-weighted Shiu argument then gives it from (★_δ) with `K = O_δ(1)`. I checked
that this argument (ET l. 755–775) nowhere uses `q ≤ ℓ^C`. It needs only
`h(p) ≤ 1/(p−1)+3p^{−δ}`, i.e. `p^{−δ} ≤ 1/2` for p > w₀. After the restatement,
Thm 2.5 and the sanity check go through unchanged.

**D5 (COSMETIC).** "So `C(η) ≍ η^{−1}`" is an upper bound only. Write `C(η) ≪ η^{−1}`.
