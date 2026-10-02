# Hostile review — EXCEPTIONAL_BALANCED.md (task a3, branch side-agent/balanced-moduli-2)

Reviewer: side agent (review-balanced). Subject files brought in verbatim from
`side-agent/balanced-moduli-2`: `EXCEPTIONAL_BALANCED.md` (EB),
`reviews/agent-reports/AGENT_REPORT_A3.md`, `scripts/balanced_*.py|cpp`,
`data/balanced/`. Context: `EXCEPTIONAL_THETA.md` (ET).

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects numbered
D1, D2, … with severity (CRITICAL / MAJOR / MINOR / COSMETIC).

## Verdict summary

| # | item | EB label | verdict | defects |
|---|---|---|---|---|
| 1 | Lemma 2.1 (gapped ⇒ (U)) | PROVED | **SOUND** | D1 (cosmetic) |
| 2 | Lemma 2.2 (heavy coordinates) | PROVED | **SOUND** | — |
| 3 | Thm 2.3 (sequential bound, given (NDE)) | PROVED given (NDE) | **SOUND** | D2 (minor, R = ℤ/Q₀ scope) |
| 4 | Lemma 2.4 (window masses) | PROVED | **SOUND** | — |
| 5 | Thm 2.5 (cap under H_light) | CONDITIONAL | **SOUND-AFTER-REPAIRS** | D3, D3a (minor), **D4 (major)**, D5 |
| 6 | Lemma 4.1 (D = sr²) | PROVED | **SOUND** | — |
| 7 | Lemma 4.2 (counting iff B < 1) | PROVED | **SOUND** | D6 (minor wording) |
| 8 | Prop 4.3 (sup ≥ y^{1/5−o(1)}) | PROVED | **SOUND-AFTER-REPAIRS** | D7, D8 (minor), **D9 (major, framing)** |
| 9 | Prop 4.4 (E_δ ⇒ ★_δ ⇒ H_light ⇒ cap) | PROVED (weak form sketched) | main chain **SOUND-AFTER-REPAIRS**; weak-ε form **DEFECTIVE as labelled** | D10, D11 (minor), **D12-W (major)** |
| 10 | EVIDENCE §3, §4.3 | EVIDENCE | **SOUND-AFTER-REPAIRS** | **D13, D15 (major)**, D14, D16, D17 (minor), D18 |
| 11 | §0 verdict / scope | — | **SOUND-AFTER-REPAIRS** | D19 (minor) |

**Bottom line.** The mathematics of §2 (Lemmas 2.1, 2.2, 2.4, Thm 2.3) and
Lemmas 4.1–4.2 is correct. The "verbatim" reuse of ET Thm 2.7 with Lemma 2.2 in
the induction step is legitimate under (NDE). Thm 2.5 is correct up to
constants, after restating H_light(ii) as a cubic window bound (D4). Without
that restatement, the chain (★_δ) ⇒ H_light(O_δ(1)) does not literally hold.
Prop 4.3 is correct, but its witnesses are *dominant* moduli, so it is no
evidence about the balanced content of (E_δ) (D9). The weak-ε form of Prop 4.4
is unproved and has a concrete gap (D12-W). Two numerical readings are
contradicted by the committed data or by a controlled re-run: heavy p(h) at
ℓ ∈ [128,512) for X = 10⁶ (D13), and the "twin ≈ 0.2, redundant" result, which
is an ordering artefact (D15). No CRITICAL defect: nothing labelled PROVED is
false as a mathematical statement, except the sketched weak form, which is
parenthetically flagged.

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
`γ(M) ≥ Π_{ℓ'|M, ℓ'>w₀}(1+ℓ'^{−δ})` grows without bound over M with many primes
slightly above w₀, and m_j has no proved lower bound (Lemma 2.4 is
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

### Item 6 — Lemma 4.1 (D = sr² parametrisation). Verdict: **SOUND**

* `g(sr²) = sr`: `⌈(v_p(s)+2v_p(r))/2⌉ = v_p(r)+v_p(s)` since `v_p(s) ∈ {0,1}`. ✓
  `D | A² ⇔ g(D) | A` (ET Lemma 3.2's remark). ✓ The map
  `(q, D) ↔ (s, r, k)` with `k = A_q/(sr)` is a bijection. ✓
* (1) Any common divisor of q and k, of q and r, or of ℓ and k divides
  `4srk − qℓ = 1`. ✓
* (2) `k(n+4sr²) = nk + r·4srk = nk + r(qℓ+1) ≡ nk + r (mod q)`, and k is a unit mod q. ✓
* (3) `4sr²·k = r(qℓ+1) ≡ r (mod ℓ)`, and ℓ ∤ k. ✓
* Membership `q ∈ 𝒬_ℓ` ⇒ `qℓ` is η-gapped with top prime ℓ: `P(q) ≤ y = ℓ^{1/(1+η)} < ℓ`. ✓
  The history fixes `n mod q`: q's primes > w₀ satisfy
  `log ℓ' ≤ log ℓ/(1+η) ≤ s_j`, so they lie in earlier windows, and its
  w₀-smooth part divides Q₀. So `p_ℓ(h) = |F_ℓ(n)|/ℓ` for any representative n. ✓

No defects.

### Item 7 — Lemma 4.2 ("counting works iff B < 1"). Verdict: **SOUND** (wording)

* The union bound and `τ(A_q²) ≤ X^{o(1)}` are correct. For an (η,B)-gapped
  family `q ≤ ℓ^B`, so `X^{o(1)} = ℓ^{o(1)}` and `|F_ℓ| ≤ ℓ^{B+o(1)}`, giving (★_δ)
  for `δ < 1−B` and `ℓ > w₀(δ,B)`. ✓
* Size claim: `p₁p₂ ∈ (ℓ, y²]` gives ≫ `y²/log²y` cofactors, half of them with
  `qℓ ≡ 3 (4)`. Each `M = p₁p₂ℓ` is balanced (`p₁p₂ > ℓ`) and gapped. ✓

**D6 (MINOR, wording of "iff" and of the B ≥ 1 witness).** "(★_δ) iff B < 1"
is a statement about the counting *method*, not about (★_δ). The text says so
("Then the bound is vacuous"), but the §0 table entry "counting gives (★_δ) iff
B < 1" should say "the counting bound gives (★_δ) iff B < 1". Also, the
witness `q = p₁p₂ ≤ y²` lies in an (η,B)-gapped family only if
`B ≥ 2/(1+η)`. For `1 ≤ B < 2/(1+η)`, vacuity follows instead from
`Ψ(ℓ^B, y) ≫_{η,B} ℓ^B ≥ ℓ` (Dickman). Fix: cite that.

### Item 8 — Proposition 4.3 (sup_n |F_ℓ(n)| ≥ y^{1/5−o(1)}). Verdict: **SOUND-AFTER-REPAIRS**

Proof re-checked.
* Step 1. `gcd(−ℓ^{−1}, 4k) = 1` and `k ≠ ℓ`, so Linnik applies. `q_k ≪ (4k)^L ≤ y`
  for `K = c₀y^{1/L}`. `q_kℓ ≡ −1 (mod 4)` ⇒ `qℓ ≡ 3 (4)` and `4k | q_kℓ+1`,
  i.e. `k | A_{q_k}`. `P(q_k) = q_k ≤ y` and `q_kℓ ≤ yℓ ≤ X`, so `q_k ∈ 𝒬_ℓ`. ✓
* Step 2. `D_k = A/k` divides A, hence A². `4D_k·k = 4A ≡ 1 (mod ℓ)`, so the value
  is `−k^{−1}`, and these are distinct for distinct primes `k < ℓ`. ✓
* Step 3. Two pairs sharing the prime `q` would need `n ≡ −4D_k ≡ −4D_{k'} (mod q)`
  simultaneously, so keeping one k per q is necessary as well as sufficient. ✓
  Distinct primes q_k are coprime. ✓
* Step 4 (CRT). Every kept pair is active at n. ✓ The constructed n is not
  claimed to be reachable, and the caveat says so. ✓

**D7 (MINOR, citation).** "Linnik's theorem with exponent 5, Xylouris 2011":
Xylouris 2011 (Acta Arith. 150) gives L ≤ 5.2 (5.18). L = 5 is in his 2018 Bonn
thesis. Fix: cite correctly, or state the result as `y^{1/L−o(1)}` for any
admissible Linnik exponent L. The argument is exponent-agnostic.

**D8 (MINOR, display + loss factor).** The display
"`|F_ℓ(n)| ≥ π(2K) − π(K) − O(1) over log(ℓX)`" is garbled, and the loss factor
is mis-stated. One prime q serves at most `#{k > K prime : k | A_q} ≤ log A_q/log K
≤ log(ℓy)/log K = O_η(1)` values. So the loss is O(1), not `log X`. As written,
with a huge X, the `−o(1)` in the exponent is not justified. With the correct
count it is (and it is independent of X). Fix: `|F_ℓ(n)| ≫_η (π(2K)−π(K))`.
Also, "typical value `E_U p_ℓ ≍ (log ℓ)^{O(1)}/ℓ`" has only the upper bound
proved. Write `≤`.

**D9 (MAJOR, interpretation/framing of §4.3–4.4).** The cofactors used are
primes `q_k ≤ y < ℓ`. So every modulus `q_kℓ` has `P(M) = ℓ > √M`. It is **not
balanced**: it is dominant, with `C = 1/(1+η)` and `B = 1/(1+η) < 1`, i.e. the
regime where Lemma 4.2 already *proves* (★_δ). Prop 4.3 therefore exhibits a
phenomenon of the dominant subfamily (consistent with
`y^{1/5} ≤ ℓ^{B+o(1)}`), not a balanced obstruction. The same holds for the
heuristic "all primes q ≤ y, each its own value, gives |F_ℓ| ≍ π(y)". The
claims "(★_δ) holds exactly for `δ < η/(1+η)`, and it is sharp there" (§4.3)
and "Exactly there, (E_δ) itself is expected to fail" (§4.4 item 3) rest on
this prime-cofactor heuristic. They say nothing about whether the
*balanced/composite* cofactors (the B ≥ 1 content of (E_δ)) can do better. Note
also that sharpness at `δ = η/(1+η)` is not proved: only `y^{1/5}` is. Fix:
(i) state that Prop 4.3's witnesses are dominant moduli, so its lower bound
holds already for B < 1; (ii) relabel "sharp there" as HEURISTIC; (iii) the
open part of (E_δ) is whether composite y-smooth cofactors `q ∈ (ℓ, ℓ^B]` can
push `sup |F_ℓ|` above `π(y)ℓ^{o(1)}`, and §4 provides no information on that.
(See also D12 on the numerics, where the one outlier is a q = 1 effect.)

### Item 9 — Proposition 4.4 ((E_δ) ⇒ (★_δ) ⇒ H_light ⇒ cap). Verdict: **SOUND-AFTER-REPAIRS** (main chain); weak-ε form **DEFECTIVE as labelled**

Main chain.
* (E_δ) ⇒ (★_δ): Lemma 4.1 identifies `F_ℓ(h)` with the (s,r,k)-set at any
  representative n. A subfamily gives a subset. ✓
* (★_δ) ⇒ (NDE) ✓. (★_δ) ⇒ no heavy coordinates **only if `ℓ^{−δ} ≤ 1/4` for
  all ℓ > w₀, i.e. `w₀ ≥ 4^{1/δ}`** (D10).
* (★_δ) ⇒ H_light(ii) holds only in the corrected, cubic form of D4. That form
  follows from ET Lemma 2.8 (with `p* ≤ ℓ'^{−δ}`) and the γ-weighted Lemma 3.1 of
  ET Cor 3.6. I checked that the latter does not use `q ≤ ℓ^C`. It needs
  `h(p) ≤ 1/(p−1) + 3p^{−δ}`, which holds for p > w₀ once `w₀^{−δ} ≤ 1/2`.
  The window bound then follows from `M ≤ e^{(1+B)(1+η)s_j}`, so
  constant `O_δ(1)`. ✓ after D4.
* Then Thm 2.5 applies, with heavy charge 0. ✓

**D10 (MINOR, Prop 4.4 / §2.6).** "Under (★_δ) there are no heavy coordinates"
needs `w₀ ≥ 4^{1/δ}` (and `w₀^{−δ} ≤ 1/2` for the γ-Shiu step). Fix: state
`w₀ = w₀(δ)`.

**D11 (MINOR, statement of (E_δ)).** (E_δ) is stated with 𝒬_ℓ defined by `qℓ ≤ X`
only. But Thm 2.5 and Prop 4.4 are for (η,B)-gapped families, i.e. `q ≤ ℓ^B`,
and X = e^{O(λ)} may be far larger than `ℓ^{1+B}` at small ℓ. The X-version is
strictly stronger than what is used, and its truth for `ℓ ≪ log X` is a
different question. Fix: define `𝒬_ℓ^{(B)} = {q ∈ 𝒬_ℓ : q ≤ ℓ^B}` and state
(E_δ) for it.

**D12-W (MAJOR, labelling of the weak-ε form).** The weak form ("`p ≤ ε` ⇒ cap
`λ^{3/4+O(ε)}`") sits inside a proposition labelled PROVED, with "only
sketched" as a parenthesis (also in §0 and in AGENT_REPORT_A3). The sketch also
has a concrete gap. With `h(p) = e^{cε}−1 ≍ ε` **not decaying in p**, the
large-divisor range of the Lemma 3.1 / Cor 3.6 argument
(`d > x^{1/2}`, bounded by `x^{o(1)}Σ h(d)(x/d+1)`) is no longer `o(x)`:
`Σ_{d≤x} h(d)` is `≍ x(log x)^{O(ε)−1}`, times `x^{1/10}` from the trivial τ
bound. Cor 3.6 needed `Σ h(d)d^{−1+δ/2} < ∞`, which fails here. And
"Euler factors change by `1+O(ε)/p`" controls only the Shiu range. The claim is
plausible (e.g. via a two-variable Nair–Tenenbaum/Henriot bound on
`τ(A²)·(1+O(ε))^{ω(4A−1)}`), but it is not proved. Fix: move the weak form out
of Prop 4.4 and label it CONJECTURE/SKETCH with the large-divisor gap stated.
The same goes for §2.6 item 4's "quartic mean ⇒ exponent 4/5", which is
unlabelled heuristic.

### Item 10 — EVIDENCE sections (§3, §4.3 numerics): labels and replay. Verdict: **SOUND-AFTER-REPAIRS** (labels fine; three readings misreport the data)

*Labels.* §3 is headed "all EVIDENCE". The §0 table and the A3 report mark it
EVIDENCE. The §4.3 numerics are marked EVIDENCE. The LP is declared
floating-point and uncertified. ✓ Unlabelled heuristics remain in §2.6 items 3–4
and §4.4 "Why the obvious proof attempts fail". They are argued informally and
should carry a HEURISTIC tag (COSMETIC, D18).

*Replays run here* (`ulimit -v 8e6`, outputs in /tmp, compared with committed data):

| replay | result |
|---|---|
| `i 100000 200 0.25` | byte-identical to `part_i_X1e5.txt` (data lines) |
| `steer 100000 101,…,503 10` | same numbers as `steer_X1e5.txt`, but that file is in an **older format** without the reach/free/π(y) columns used in §4.3 (see D17) |
| `ii 7,11,13,19 3`, `ii 7,11,19,23 3`, `ii 11,13,17,19 3` | match §3.2 to 3 decimals |
| `balanced_void 4000 1e12 3e10` | identical to `void_primes_Q4000.txt`; table values recomputed ✓ |
| `ii 7,11,13,17,19 2` | identical to `part_ii_S7_11_13_17_19.txt` |
| `i 1000000 20 0.25` | identical to `part_i_X1e6.txt` (data lines; ≈ 15 min here) |
| order-swap void variant (reviewer's) | `data/review_balanced/void_order_Q4000.txt` (D15) |

So every committed number replays exactly. The defects below concern the
*readings* of the data, not the data.

**D13 (MAJOR, §3.1 Reading, "`p(h) > 1/4` occurs only for top primes p < 128").**
This is false for the data in `part_i_X1e6.txt`. For the union over all types
(the quantity that enters (★_δ)/H_light, since F_ℓ is the union), the X = 10⁶
"all" rows give:
* `[128,256)`: max p(h) = 0.329, and 15.4% of sampled histories are heavy;
* `[256,512)`: max p(h) = 0.259, and 0.2% are heavy.

At X = 10⁵ the same bands give 2.7% and 0%. So the heavy region **moves up with
X**, which is what one expects: the cofactor count at fixed ℓ grows with X when
B is unrestricted. This is the trend that matters for H_light (w₀ cannot be a
fixed constant for unbounded B), and the reading hides it. The §3.1 table shows
only per-type twin/gapB rows, never the union. Fix: report the "all" rows,
correct the sentence, and state the trend.

**D14 (MINOR).** "K < 1 in every band and type (range 0.52–1.00)": the data
range is 0.48–1.00 (`[2048,4096) gapM` at X=10⁵: 0.48; `[32,64) all` at X=10⁶: 0.49).

**D15 (MAJOR, §3.3 Reading + §0 table, "η-twin classes have ≈ 0.2 effective void
mass … the twin part is strongly redundant").** This is an **order artefact**:
twin classes are always added *last*, after dom and gapped. I ran a variant
(`scripts/review_balanced_void_order.cpp`, data
`data/review_balanced/void_order_Q4000.txt`, same 1,085,136,872 primes). It adds
a family dom+twin, so both orders can be compared:

| Q' | twin added to dom | gapped added to dom+twin | gapped added to dom | twin added last (EB) |
|---:|---:|---:|---:|---:|
| 275 | 0.42 | 0.62 | 0.73 | 0.17 |
| 606 | 0.45 | 0.52 | 0.63 | 0.20 |
| 1333 | 0.47 | 0.49 | 0.59 | 0.22 |
| 2253 | 0.49 | 0.47 | 0.58 | 0.22 |
| 4000 | 0.52 | 0.50 | 0.54 | 0.42 |

(Entries are Δ(−log void)/Δ(mass).) For Q' ≥ 1333, twin classes added directly
to dom are as efficient per unit mass as gapped classes added last. "Strongly
redundant" is unsupported. The 0.2 measures the overlap with the gapped family,
not a property of twin classes. Fix: withdraw the reading, or report both
orders. The only defensible statement is that each non-dominant family yields
about 0.5 per unit mass when added to dom, and less when added after the other.

**D16 (MINOR, §3.2 mislabel "Composite moduli here are … balanced and mostly
η-twin").** A two-prime modulus pq is never balanced (`P = max(p,q) > √(pq)`).
In all four windows the balanced conditions are exactly the 3-prime ones
(1463, 1771, 2431, 3059, 4199, 4807, and the 4-prime 19019). The m = 2 gain 0.035 for {11,13,17,19}
therefore comes with non-balanced pair moduli (143, 187, 247, 323) in the family.
For {7,11,19,23}, every prime is ≡ 3 (4), so there are **no** pair conditions at
all. Some pairs are η-gapped at η = 1/4 (91 = 7·13: log13/log7 = 1.32). Fix: rename
D+B → "D + composite", and split the gain into pairs vs. triples. The LP
methodology itself (dual of §1 route 1, uniform m-marginals) is correct.

**D17 (MINOR, §4.3 numerics table).** (a) For ℓ = 101 the table says reach = 13.
The committed run and my replay (same seed) give 14 = 0.1386·101, consistent with
§3.1's best p(h) = 0.139. (b) The run also covers ℓ = 151 (19 vs π(y) = 16) and
ℓ = 503 (**80** vs π(y) = 34), but the table silently omits both. The 503 excess
comes from the cofactor q = 1: `A = 126`, so `τ(A²) = 45` values are active for
every n. The π(y) heuristic ignores this `ℓ^{o(1)}` baseline, which is not small at
toy scale. (c) The adversary counts all types, dom included, so "tracks π(y)" is
not a balanced statement (cf. D9). (d) The committed `steer_X1e5.txt` predates
the reach/free/π(y) output, so the table is not backed by committed data. Fix:
regenerate the data file, report all six ℓ, and give `τ(A_1²)` separately.

### Item 11 — §0 verdict and scope claims. Verdict: **SOUND-AFTER-REPAIRS**

* "Neither (A) nor (B) is proved", "η-twin moduli are untouched", and "numerics
  at toy scales" are all accurate. ✓
* **D19 (MINOR, scope overstatement).** "Balanced moduli whose two top primes are
  separated (η-gapped) are reduced to one arithmetic extremal statement, (E_δ)."
  Thm 2.5 and Prop 4.4 cover only **(η,B)-gapped families with B fixed**
  (`M ≤ P(M)^{1+B}`), with constant `(1+B)^{3/4}`. Gapped moduli with
  `log M/log P(M)` unbounded (within moduli ≤ e^{O(λ)}) are not covered. No
  dyadic-in-B summation is given. Also, w₀ must grow with δ (D10), and
  numerically with X (D13). Fix: add "for each fixed B" to §0, §2.6 and the A3
  report.
* The §1 claim that ET's profile bound holds for all of 𝔉 is correct, since
  ET Lemma 3.1 is unrestricted in M. ✓
* AGENT_REPORT_A3 mirrors EB faithfully. It inherits D4, D9, D12-W, D13, D15
  and D19 (its EVIDENCE bullet repeats "η-twin ≈ 0.2" and "p > 1/4 only for
  ℓ < 128").
