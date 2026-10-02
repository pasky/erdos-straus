# EXCEPTIONAL_BALANCED — can balanced moduli beat the 3/4 sieve limit? (task a3)

Status: **in progress.** Nothing in this file is proved unless a later
section says so. Labels follow `DISCOVERIES.md`.

Notation as in `EXCEPTIONAL_THETA.md` (ET): `L = log N`, λ = level,
`P(M) ≥ P₂(M) ≥ …` the prime factors of M in decreasing order.

## 1. Setup and the decision problem

**Forced classes.** The family 𝔉 consists of all Case-B classes
`−4D (mod M)`, `M ≡ 3 (4)`, `D | ((M+1)/4)²` (ET Lemma 18.1 / ℛ(M)), the
(a,D)-classes `−(4D+a) (mod 4a·g(D))` (ET Lemma 3.2), and the Case-A classes
`−m^{−1} (mod 4g(d))`, `m | 4d+1` (ET §3). Every member is forced: no n ≥ 1 in
it is an ES exception. The avoider set of a subfamily 𝔊 ⊆ 𝔉 is
`𝒜(𝔊) = {n : n lies in no class of 𝔊}` (plus an admissible small-residue
set R, as in ET §1).

**Dominant vs balanced.** Fix `0 < C < 1`. A modulus M is *dominant* if
`P(M) ≥ M^{1/(1+C)}`; ET Cor 3.6 covers families of dominant moduli only.
M is *balanced* if `P(M) ≤ M^{1/2}`. The intermediate band
`M^{1/2} < P(M) < M^{1/(1+C)}` is also uncovered (constants blow up as C→1).
The *balanced subsystem* 𝔅 ⊆ 𝔉 is the set of classes with balanced modulus.
A finer split used below: M is *η-gapped* if `P(M) ≥ P₂(M)^{1+η}`, and
*η-twin* otherwise (top two primes within log-ratio 1+η). Lemma 3.8 of ET
shows η-twin balanced moduli carry `≫_η (log x)³` supply for every fixed η.

**Majorant class 𝓜_λ(𝒜).** Finite combinations
`ν(n) = Σ_i a_i·1[n ≡ b_i (mod d_i)]` with ν ≥ 0 on all of ℤ, ν ≥ 1 on 𝒜,
and level `Σ_{ℓ | d_i, ℓ > w₀} log ℓ ≤ λ` for every i. Saving
`S_λ(𝒜) = sup_ν log(1/Eν)`, Eν the CRT mean. As in ET Lemma 2.9, a final
bound `N·Eν + Σ|a_i|` with `Σ|a_i| < N` and family primes `≤ N^{O(1)}`
reduces to level `λ ≤ (A+1)·L + S`. The relevant regime is λ ≍ L.

**Benchmark.** For dominant families, ET Thm 2.5/2.7 give
`S_λ ≤ C·inf_α [αλ + Σ_C P(C)·M_C^{−α}] + O(log²λ) ≪ λ^{3/4}`, using the
cubic profile `Σ_C P(C) M_C^{−α} ≪ α^{−3}` (ET Lemmas 3.1, 3.2, 3.7). The
profile bound already holds for *all* of 𝔉, balanced included. Only the
*sieve-limit step* is missing for balanced moduli. ET calls the missing
statement H_MS (general majorants) and H_MS^{Sel} (Λ² majorants).

**The decision problem.** Is `S_λ(𝒜(𝔉')) ≪ λ^{3/4}·(log λ)^{O(1)}` for every
subfamily 𝔉' ⊆ 𝔉 with moduli ≤ e^{O(λ)}, balanced moduli included?

* **(A) No — balanced moduli cannot help.** Prove the bound above for all
  of 𝓜_λ. Then 3/4 is sharp for every nonnegative CRT majorant of forced
  classes with polynomially bounded moduli. A weaker (A) proves it for a
  named subclass, e.g. Λ² majorants or polynomials in fired-condition counts.
* **(B) Yes.** Exhibit balanced conditions plus a majorant whose saving
  beats `C·λ^{3/4}` by a factor `→ ∞`, even `(log log N)^c`, proved at
  hostile-review standard.
* **(C) Reduction.** Name one inequality I such that I ⇒ (A) and ¬I ⇒ (B),
  or as close to both directions as can be proved. Test I numerically on the
  real forced-class system, sampling balanced moduli (the ET deadly-value
  numerics sampled dominant moduli only).

**Candidate routes (one line each; none attempted yet).**
1. *LP duality.* `S_λ(𝒜) = −log max{σ(𝒜) : σ a probability measure whose
   level-λ marginals are uniform}`; (A) asks to construct such σ.
2. *Gapped windows.* ET Thm 2.7 with windows of log-ratio 1+η should cover
   η-gapped moduli at a cost `η^{−O(1)}`, isolating η-twin moduli as the
   whole problem.
3. *Local boost inequality.* Replace ET Prop 2.4 inside one window by
   `E[G | 𝒜_W] ≤ e^{Φ_W}·E[G]` for nonnegative λ-level G. The sequential
   induction then composes windows with η-twin conditions inside them.
4. *Linear windows.* Windows with `log ℓ > λ/2` see at most one prime per
   term. A marginal-inflation lemma for sparse systems should make them
   cost O(1), so conditions beyond the level are harmless.
5. *Matching dominance.* In the sparse regime, only disjoint (matching)
   configurations of fired conditions have non-negligible moments. A pair
   then costs its full modulus, which is the H_MS heuristic. Make this
   rigorous for count-polynomial majorants.
6. *Λ² route.* Prove H_MS^{Sel} (`Ξ_𝒜(α) ≪ α^{−3}·polylog`) for 𝔉 via
   Janson-type two-sided void estimates, after conditioning on small primes.
7. *Product converse.* If an η-twin window system admits local savings above
   its Rankin value, products over disjoint windows give a global majorant
   with the summed saving. This is the (¬I ⇒ B) direction.
8. *Real-system numerics.* Measure, for balanced moduli, the partner masses
   `m_b`, the deadly values, `S_sq`, and the per-prime local mass `M_ℓ`
   (the sparsity parameter of routes 3–5).

## 2. Route 2: η-gapped moduli

Goal: a version of ET Thm 2.7 with windows of log-ratio 1+η, giving
`S_λ ≤ C(η)·λ^{3/4}` for families of η-gapped moduli. This would leave the
η-twin moduli as the whole problem.

**Conventions.** `P₂(M) := P(M/P(M))`, and `P₂(1) := 1`. So `P(M)² | M`
forces `P₂ = P`. Fix `w₀ ≥ 3` and `0 < η ≤ 1`. M is **η-gapped** if
`P(M) > w₀` and `P(M) ≥ P₂(M)^{1+η}`. Put `s₀ = log w₀` and
`s_j = s₀(1+η)^{j−1}`. The windows are

    W_j = {ℓ prime : s_j < log ℓ ≤ s_{j+1}},   j ≥ 1.

Every prime `> w₀` lies in exactly one window. Primes `≤ w₀` go into the
small modulus Q₀, as in ET Thm 2.7.

### 2.1 Separation

**Lemma 2.1 (gapped ⇒ (U); PROVED).** Let M be η-gapped and `ℓ = P(M)`.
1. ℓ divides M exactly once.
2. Every prime `ℓ' | M/ℓ` with `ℓ' > w₀` lies in a window strictly before
   the window of ℓ.

Hence a family of η-gapped classes satisfies hypothesis (U) of ET Thm 2.7
for the windows `W_j`, with `ℓ(C) = P(M_C)`.

*Proof.*
1. If `ℓ² | M`, then `P₂(M) = ℓ`, and `ℓ ≥ ℓ^{1+η}` is false.
2. Let `ℓ' ∈ W_j`. Then `log ℓ' > s_j`. Since ℓ' divides M/ℓ, we have
   `log ℓ ≥ (1+η) log P₂(M) ≥ (1+η) log ℓ' > (1+η)s_j = s_{j+1}`. So ℓ lies
   in some `W_{j'}` with `j' > j`. ∎

*Scope.*
* **Dominant moduli are gapped.** If `P(M) ≥ M^{1/(1+C)}`, then
  `P₂ ≤ M/P ≤ P^C`, so M is η-gapped with `η = 1/C − 1`.
* **Some balanced moduli are gapped, but not the twin ones.** Take
  `M = kℓ₁ℓ₂` with k small, `ℓ₂ ≥ ℓ₁^{1+η}` and `kℓ₁ ≥ ℓ₂`. Then M is
  balanced and η-gapped. The same-scale pairs of ET Lemma 3.8 are η-twin
  for every `η > η_{3.8}`, and their supply is not covered here.
* **The new feature.** For a gapped balanced M, the cofactor `q = M/P(M)`
  exceeds `P(M)`. ET Cor 3.6 relies on `q ≤ ℓ^C` in two places, so
  §§2.2–2.3 must replace both:
  * the counting bound `p_ℓ(h) ≤ ℓ^{C−1+o(1)} ≤ 1/4`, valid for every
    history h;
  * the inflation factors `(1−p*)^{−1}` of ET Lemma 2.8.

### 2.2 Heavy coordinates

ET Prop 2.4 assumes `p_i ≤ 1/4` for every i with `s_i ≤ λ`. Gapped
families cannot guarantee this for every history (§2.1, last remark).
Heavy coordinates can instead be conditioned out, at their exact void cost.

**Lemma 2.2 (Prop 2.4 with heavy coordinates; PROVED).** Take the setting
of ET Prop 2.4, but drop the assumption `p_i ≤ 1/4`; keep `p_i < 1` for
all i. Put:
* `H = {i : s_i ≤ λ, p_i > 1/4}` (heavy);
* `I' = I ∖ H` (light).

Let f be λ-level with `f ≥ 0` and `f(0) ≥ 1`. Then

    log(1/E f) ≤ RHS(2.3)[I'] + Σ_{i∈H} −log(1−p_i),

where `RHS(2.3)[I']` is the right side of ET (2.3), with μ and the
Rankin sum taken over light coordinates only.

*Proof.* The coordinates `x_H` are independent of `x_{I'}`, and f ≥ 0, so

    E f ≥ E[f·1{x_H = 0}] = Π_{i∈H}(1−p_i) · E f̃,   where f̃(x_{I'}) := f(x_{I'}, 0_H).

Restricting each term `f_T` to `x_H = 0` gives a function of `x_{T∖H}`,
so f̃ is λ-level. Also `f̃ ≥ 0` and `f̃(0) = f(0) ≥ 1`. Every light
coordinate with `s_i ≤ λ` has `p_i ≤ 1/4`, so ET Prop 2.4 applies to f̃. ∎

The bound is sharp in form. For a single heavy coordinate and the majorant
`f = 1{x_i = 0}`, the saving is exactly `−log(1−p_i)`.

### 2.3 The sequential bound for gapped families

Let 𝔊 be a finite family of η-gapped forced classes. Use the following
data:
* windows `W_j` as in §2;
* `Q₀ = lcm` of the w₀-smooth parts of all moduli of 𝔊;
* `R = ℤ/Q₀`. There are no pure small-modulus conditions, since every
  gapped modulus has `P(M) > w₀`.

By Lemma 2.1, 𝔊 is a system in the sense of ET §2.6 with ℓ(C) = P(M_C).
Let `Q_seq`, `F_ℓ(h)` and `p_ℓ(h)` be as there. Call a history h
*reachable* if `Q_seq(h) > 0`.

**(NDE) No dead ends.** `p_ℓ(h) < 1` for every reachable h at window j and
every `ℓ ∈ W_j`.

**Theorem 2.3 (PROVED, given (NDE)).** Every majorant ν of level λ of
`𝒜(𝔊)` satisfies

    log(1/Eν) ≤ Σ_j E_{Q_seq}[ Φ_j^{light}(H_{<j}) + Σ_{ℓ∈W_j, log ℓ≤λ, p_ℓ(H)>1/4} −log(1−p_ℓ(H_{<j})) ].   (2.1)

Here `Φ_j^{light}(h)` is the right side of ET (2.3) for the light
coordinates of window j (`log ℓ ≤ λ`, `p_ℓ(h) ≤ 1/4`), with `α = α_j`.
Windows with `s_j ≥ λ` contribute 0.

*Proof.* This is the proof of ET Thm 2.7 verbatim, with ET Prop 2.4
replaced by Lemma 2.2 in the induction step. That step uses only three
facts:
1. given `H_{<j} = h`, the hit indicators of window j are independent;
2. `f(x) = E[g_{j+1} | h, x]` is λ-level and ≥ 0;
3. at `x = 0` the next history has the `Q_seq` transition law.

None of these uses `p ≤ 1/4`. (NDE) gives `P(x=0 | h) > 0`, so `f(0)` and
the transition are defined. The R-term `log(Q₀/|R|)` vanishes because
`R = ℤ/Q₀`. ∎

So the cost of dropping ET's counting bound is concentrated in two
`Q_seq`-expectations:
* the **heavy charge**, the last sum in (2.1);
* the **light profile** `E_{Q_seq} p_ℓ(H)` inside `Φ_j^{light}`.

§2.4 shows that if both are controlled, the windows sum to `C(η)λ^{3/4}`.
§2.5 records where controlling them fails.

### 2.4 Window masses (uniform measure)

From here on, restrict to the ℛ(M)-grouping, i.e. classes `−4D (mod M)` of
ET Lemma 18.1. Fix `B ≥ 1`. M is **(η,B)-gapped** if it is η-gapped and
`M ≤ P(M)^{1+B}`. Every balanced gapped M has `B ≥ 1`. For dominant M,
`B = C < 1` suffices.

**Lemma 2.4 (PROVED).** For an (η,B)-gapped ℛ(M)-family and window j, put

    m_j := Σ_{M : P(M)∈W_j} |ℛ(M)|·(M/φ(M))/M.

Then `m_j ≤ C₆'·((1+B)(1+η)s_j)³`. Consequently, for every `α > 0`,

    Σ_{M : P(M)∈W_j} |ℛ(M)|(M/φ(M))/M · P(M)^{−α} ≤ C₆'·(4(1+B)s_j)³·e^{−αs_j}.

*Proof.* `P(M) ∈ W_j` gives `M ≤ P(M)^{1+B} ≤ e^{(1+B)s_{j+1}}`. Next,
`|ℛ(M)| ≤ τ(A²)` (ET (B)1). Partial summation of ET Lemma 3.1,
`S_B(x) ≪ x log²x`, gives `Σ_{M≤x} τ(A²)(M/φ(M))/M ≪ (log x)³`. The
second claim uses `P(M) > e^{s_j}` and `1+η ≤ 2`. ∎

*Remark (why not ηs_j³).* Window j has Mertens mass ≈ η, so one expects
`m_j ≍ η·s_j³`. Proving that needs the ℛ-weighted sum restricted to
`P(M) ∈ W_j`, a smooth-cofactor Shiu bound, and that bound is not
available. The cruder Lemma 2.4 costs one power of η^{−1/4} in §2.5.

### 2.5 The conditional cap

**Hypothesis H_light(K)** (for an (η,B)-gapped family and level λ). All
three parts hold:
* (NDE) holds;
* for every j with `s_j ≤ λ`, `E_{Q_seq} Σ_{ℓ∈W_j, light} p_ℓ(H_{<j}) ≤ K·m_j`;
* the total heavy charge in (2.1) is at most `K·λ^{3/4}`.

**Theorem 2.5 (PROVED, given H_light(K)).** Every majorant ν of level
`λ ≥ s₀` of an (η,B)-gapped ℛ(M)-family satisfies

    log(1/Eν) ≤ C·K^{1/4}(1+B)^{3/4}·η^{−1}·λ^{3/4} + K·λ^{3/4} + O(η^{−1} log λ·(log λ + log K)),

with an absolute constant C. So `C(η) ≍ η^{−1}`.

*Proof.* Start from (2.1).
* *One band per window.* Costs in `W_j` lie in `(s_j, (1+η)s_j]` and
  `1+η < 2`. So each window is a single band of ET Prop 2.4, with `G = 1`.
  Hence the error terms of `Φ_j` are
  `75 + log(2+λ/s_j) + ½log(16μ_j+16)`.
* *Bounding E log μ_j.* By concavity, `E log(16μ_j+16) ≤ log(16Km_j+16)`.
  So the error terms are `O(log λ + log K)` per window.
* *Number of windows.* There are at most `1 + 2 log λ/η` windows with
  `s_j ≤ λ`.
* *Main term.* By H_light and Lemma 2.4, window j costs at most
  `inf_α[19αλ + X_j e^{−αs_j}]` with `X_j = C₄K c_B s_j³` and
  `c_B = C₆'(4(1+B))³`. This infimum is
  `≤ min{X_j, (19λ/s_j)(1+log⁺(X_j s_j/19λ))}`. Put
  `s* = (19λ/(C₄Kc_B))^{1/4}`. Two sums:
  * windows with `s_j ≤ s*` contribute
    `Σ X_j ≤ X(s*)/(1−(1+η)^{−3}) ≤ 2X(s*)/η = 38λ/(ηs*)`;
  * windows above `s*` contribute
    `(19λ/s*)·Σ_{k≥0}(1+η)^{−k}(1+4k log(1+η)) ≤ (19λ/s*)·10/η`.
  
  The total is `≤ 228λ/(ηs*)`, which is the first term. ∎

**Sanity check (dominant case).** For dominant moduli (`B = C < 1`), the
counting bound of ET Cor 3.6 gives `p* ≤ ℓ^{−δ}`. So there are no heavy
coordinates and (NDE) holds trivially. Part (ii) holds in ET Lemma 2.8's
averaged form, with the γ-weight, which ET Cor 3.6 shows is still cubic.
Theorem 2.5 therefore reproduces Cor 3.6, with an explicit η^{−1}.
