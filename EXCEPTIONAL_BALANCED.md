# EXCEPTIONAL_BALANCED — can balanced moduli beat the 3/4 sieve limit? (task a3)

Status: **checkpoint (outcome (C), partial).** Labels follow
`DISCOVERIES.md`. PROVED means proved here and checked internally only.

## 0. Status at a glance

| item | statement | label |
|---|---|---|
| Lemma 2.1 | η-gapped moduli (`P(M) ≥ P₂(M)^{1+η}`, `P(M) > w₀`) satisfy (U) for windows of log-ratio 1+η | PROVED |
| Lemma 2.2 | ET Prop 2.4 without `p ≤ 1/4`: heavy coordinates cost `−log(1−p_i)` each | PROVED |
| Thm 2.3 | sequential bound (2.1) for gapped families, given (NDE) | PROVED given (NDE) |
| Lemma 2.4 | window masses `m_j ≪ (1+B)³s_j³` for (η,B)-gapped ℛ(M)-families | PROVED |
| Thm 2.5 | `S_λ ≤ C K^{1/4}(1+B)^{3/4} η^{−1}λ^{3/4} + Kλ^{3/4} + O(η^{−1}log λ·(log λ+log K))` | CONDITIONAL on H_light(K) |
| Lemma 4.1 | `F_ℓ(n) = {−r/k mod ℓ : (4srk−1)/ℓ = q ∈ 𝒬_ℓ, q \| nk+r}` | PROVED |
| Lemma 4.2 | counting gives (★_δ) iff B < 1; vacuous for B ≥ 1 | PROVED |
| Prop 4.3 | `sup_n \|F_ℓ(n)\| ≥ y^{1/5−o(1)}`, `y = ℓ^{1/(1+η)}` (reachability not checked) | PROVED (uses Linnik/Xylouris) |
| Prop 4.4 | (E_δ) ⇒ (★_δ) ⇒ H_light(O(1)) ⇒ cap `≪ η^{−1}λ^{3/4}` for (η,B)-gapped families | PROVED (weak-ε form only sketched) |
| §3 | real system: `K = E_seq p/E_U p ∈ [0.52, 1]`; `p(h) ≲ 4ℓ^{−1/2}`; balanced classes add no LP saving at level ≤ 2 and lose to matched-mass singles; η-twin classes have ≈ 0.2 effective void mass among real primes; greedy sup of `\|F_ℓ\|` ≈ π(y) | EVIDENCE |

**Verdict so far.** Neither (A) nor (B) is proved.
* Balanced moduli whose two top primes are separated (η-gapped) are
  reduced to one arithmetic extremal statement, (E_δ).
* η-twin moduli (top two primes within log-ratio 1+η) are the open core.
  They carry `≫_η (log x)³` supply (ET Lemma 3.8). They are untouched by
  any proof here.
* All numerics lean towards (A), i.e. that balanced moduli do not beat
  3/4. They are taken at toy scales only.

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
forces `P₂ = P`. Fix `w₀ ≥ 3` and `0 < η < 1` (strict, so that a window
spans less than a factor 2 in cost; review D3). M is **η-gapped** if
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
* **Dominant moduli are gapped.** If `P(M) ≥ M^{1/(1+C)}` and
  `P(M) > w₀`, then `P₂ ≤ M/P ≤ P^C`. So M is η-gapped for every
  `η ≤ min(η₀, 1/C − 1)`, where `η₀ < 1` is fixed. Moduli with
  `P(M) ≤ w₀` are w₀-smooth and excluded (review D1).
* **Some balanced moduli are gapped, but not the twin ones.** Take
  `M = kℓ₁ℓ₂` with `P(k) < ℓ₁`, `ℓ₂ ≥ ℓ₁^{1+η}` and `kℓ₁ ≥ ℓ₂`. This
  forces `k ≥ ℓ₁^η`, so k is not small. Then M is
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
* an admissible small-residue set `R ⊆ ℤ/Q₀`. Examples are `R = ℤ/Q₀` or
  a selector `{(c, P_{w₀}) = 1}`. The avoider set is
  `𝒜(𝔊) ∩ {n mod Q₀ ∈ R}`, and `Q_seq` starts uniform on R. There are no
  pure small-modulus forced conditions, since every gapped modulus has
  `P(M) > w₀`; forced classes with w₀-smooth modulus are outside 𝔊 by
  definition.

By Lemma 2.1, 𝔊 is a system in the sense of ET §2.6 with ℓ(C) = P(M_C).
Let `Q_seq`, `F_ℓ(h)` and `p_ℓ(h)` be as there. Call a history h
*reachable* if `Q_seq(h) > 0`.

**(NDE) No dead ends.** `p_ℓ(h) < 1` for every reachable h at window j and
every `ℓ ∈ W_j`.

**Theorem 2.3 (PROVED, given (NDE)).** Every majorant ν of level λ of
`𝒜(𝔊)` satisfies

    log(1/Eν) ≤ log(Q₀/|R|) + Σ_j E_{Q_seq}[ Φ_j^{light}(H_{<j}) + Σ_{ℓ∈W_j, log ℓ≤λ, p_ℓ(H)>1/4} −log(1−p_ℓ(H_{<j})) ].   (2.1)

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
the transition are defined. The R-term `log(Q₀/|R|)` is ET (2.6)
verbatim. It vanishes for `R = ℤ/Q₀`, and it is `log log w₀ + O(1)` for the
selector. ∎

For a selector R, ET Lemma 2.8 is used with
`P(c ≡ a_C (q_C) | R) ≤ 1/φ(q_C)`, as in ET Cor 3.6. This is why the
window masses of §2.4 carry the weight M/φ(M) (review D2).

So the cost of dropping ET's counting bound is concentrated in two
`Q_seq`-expectations:
* the **heavy charge**, the last sum in (2.1);
* the **light profile** `E_{Q_seq} p_ℓ(H)` inside `Φ_j^{light}`.

§2.5 shows that if both are controlled, the windows sum to `C(η)λ^{3/4}`.
§2.6 records where controlling them fails.

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

**Hypothesis H_light(K)** (for an (η,B)-gapped family with B fixed, and
level λ). All three parts hold:
* (i) (NDE) holds;
* (ii) *cubic window bound*: for every j with `s_j ≤ λ`,
  `E_{Q_seq} Σ_{ℓ∈W_j, light} p_ℓ(H_{<j}) ≤ K·((1+B)s_j)³`;
* (iii) the total heavy charge in (2.1) is at most `K·λ^{3/4}`.

(Review D4: an earlier version had `K·m_j` in (ii), with `m_j` the
unweighted uniform window mass. What (★_δ) delivers via ET Lemma 2.8 is a
γ-weighted mass, and the comparison with `m_j` is not proved. The proof
below uses (ii) only through a cubic bound, so the cubic form is the
correct one. By Lemma 2.4, `m_j ≤ C₆'(2(1+B)s_j)³`, so the old form implies
the new one.)

**Lemma 2.5a (band count; PROVED).** In ET Prop 2.4, G may be taken to be
the number of *nonempty* bands `B_g`, and `log(2+λ/s_*)` may be replaced by
`log(2+λ/s_min)`.

*Proof.* Step 0 of Prop 2.4 discards empty bands. Every G-dependence in
Steps 3–5 is over nonempty bands:
* `|c_j| ≤ 2^G` in Lemma 2.3 (one coordinate per band);
* `|Λ| ≤ (1+λ/s_*)^G`;
* the sums over g. ∎

**Theorem 2.5 (PROVED, given H_light(K)).** Every majorant ν of level
`λ ≥ s₀` of an (η,B)-gapped ℛ(M)-family satisfies

    log(1/Eν) ≤ C·K^{1/4}(1+B)^{3/4}·η^{−1}·λ^{3/4} + K·λ^{3/4} + O(η^{−1} log λ·(log λ + log K)),

with an absolute constant C, for each fixed B. So `C(η) ≪ η^{−1}`, an
upper bound only (review D5). The O-term also hides a `log(1+B)`.

*Proof.* Start from (2.1).
* *One band per window.* Costs in `W_j` lie in `(s_j, (1+η)s_j]` and
  `1+η < 2`. So each window has one nonempty band, and `G = 1` by
  Lemma 2.5a.
  Hence the error terms of `Φ_j` are
  `75 + log(2+λ/s_j) + ½log(16μ_j+16)`.
* *Bounding E log μ_j.* By concavity and H_light(ii),
  `E log(16μ_j+16) ≤ log(16K((1+B)s_j)³+16)`. So the error terms are
  `O(log λ + log K + log(1+B))` per window.
* *Number of windows.* There are at most `1 + 2 log λ/η` windows with
  `s_j ≤ λ`.
* *Main term.* By H_light(ii), window j costs at most
  `inf_α[19αλ + X_j e^{−αs_j}]` with `X_j = C₄K c_B s_j³` and
  `c_B = (1+B)³`. This infimum is
  `≤ min{X_j, (19λ/s_j)(1+log⁺(X_j s_j/19λ))}`. Put
  `s* = (19λ/(C₄Kc_B))^{1/4}`. Two sums:
  * windows with `s_j ≤ s*` contribute
    `Σ X_j ≤ X(s*)/(1−(1+η)^{−3}) ≤ 2X(s*)/η = 38λ/(ηs*)`;
  * windows above `s*`: the k-th has `s_j/s* ∈ ((1+η)^k, (1+η)^{k+1}]`,
    so it contributes at most `(19λ/s*)(1+η)^{−k}(1+4(k+1)log(1+η))`.
    The sum is `≤ (19λ/s*)[(1+η)/η + 4(1+η)²/η] ≤ (19λ/s*)·18/η`
    (review D3a; an earlier version wrongly had `4k` and `10/η`).
  
  The total is `≤ 380λ/(ηs*)`, which is the first term. ∎

**Sanity check (dominant case).** For dominant moduli (`B = C < 1`), the
counting bound of ET Cor 3.6 gives `p* ≤ ℓ^{−δ}`. With `w₀ ≥ 4^{1/δ}`
there are no heavy coordinates, and (NDE) holds trivially.

Part (ii) holds as follows. ET Lemma 2.8 with `p* ≤ ℓ'^{−δ}` bounds the
Q_seq-profile by the γ-weighted mass. The γ-weighted Shiu argument of ET
Cor 3.6 bounds that by a cubic window bound. That argument does not use
`q ≤ ℓ^C`; it needs only `h(p) ≤ 1/(p−1) + 3p^{−δ}` and `w₀^{−δ} ≤ 1/2`.

Theorem 2.5 therefore reproduces Cor 3.6, with an explicit η^{−1}.

### 2.6 Where the proof stops: the single gap H_light

§§2.1–2.5 are proved. For each fixed B, route 2 therefore reduces to
**H_light(K)** with `K = (log λ)^{O(1)}`, for (η,B)-gapped families with
`B ≥ 1` (the balanced gapped ones). Gapped moduli with `log M/log P(M)`
unbounded are not covered: there is no summation over B (review D19).
Where and why the ET argument fails:

1. **Counting fails, necessarily.** ET Cor 3.6 bounds `p_ℓ(h)` for every
   history h by counting conditions with largest prime ℓ:
   `Σ_{q≤ℓ^C}|ℛ(qℓ)| = ℓ^{C+o(1)}`. A balanced gapped M has cofactor
   `q = M/P(M) ≥ P(M)`. So the count is `≥ ℓ^{1+o(1)}`, which is
   compatible with `F_ℓ(h) = ℤ/ℓ`. This is a property of balance itself,
   not of the windows.
2. **Adversarial histories are not excluded.** Take pairwise coprime
   cofactors `q_i` built from earlier-window primes, with
   `D_i | ((q_iℓ+1)/4)²` and distinct values `−4D_i mod ℓ`. CRT gives
   histories with `n ≡ −4D_i (mod q_i)` for all i at once. Such a history
   activates many classes at ℓ. Whether it can also avoid every
   earlier-window condition (be *reachable*) is **not decided** here. So
   heavy coordinates, and even dead ends, are not ruled out.
3. **Averaging does not fix it cheaply** (HEURISTIC). Under U the hit probability is
   tiny, `E_U p_ℓ ≍ s³/ℓ`. But (2.1) needs `Q_seq`-expectations, and
   `dQ_seq/dU = Π(1−p_{ℓ'}(h))^{−1}` along the history. Changing measure
   by Cauchy–Schwarz costs `E_{Q_seq}Π(1−p)^{−1} ≈ e^{(total mass)}`,
   which is `e^{λ³}`. That is useless.
4. **A sup bound weaker than ℓ^{−δ} does not suffice** (HEURISTIC). If
   only `p* ≤ 1/2` is known, the profile inflation `Π_{ℓ'|q}(1−p*)^{−1}`
   can be as large as `2^{ω(q)}`. The weight `2^{ω(q)}τ(A²)` heuristically
   has a quartic mean, which would suggest exponent 4/5, not 3/4.

**Sufficient condition (★_δ).** `p_ℓ(h) ≤ ℓ^{−δ}` for every reachable h,
every window and every `ℓ > w₀`, with `w₀ = w₀(δ) ≥ 4^{1/δ}` (review D10).
Under (★_δ):
* there are no heavy coordinates, and (NDE) holds;
* ET Lemma 2.8 and the γ-weighted Shiu argument of ET Cor 3.6 give the
  cubic window bound H_light(ii) with `K = O_δ(1)` (see the sanity check
  in §2.5).

So Theorem 2.5 yields `S_λ ≪_{δ,B} η^{−1}λ^{3/4}` for each fixed B.
(★_δ) holds for `B < 1`; for `B ≥ 1` it is open (item 2). The numerics of
§3.1 suggest that w₀ must grow with X when B is unrestricted (review
D13).

**Status of route 2.**
* η-gapped moduli with `M ≤ P(M)^{1+B}` (B fixed) are covered with
  `C(η) ≪ η^{−1}`, conditionally on the
  **named gap H_light** (or the stronger (★_δ)), a statement about
  sequentially conditioned CRT histories only.
* The η-twin moduli are not touched by route 2 at all. For every
  `η > 0` they carry `≫_η (log x)³` supply (ET Lemma 3.8).
* Even unconditionally, route 2 cannot settle the decision problem of
  §1; at best it isolates η-twin windows.

Next candidates: route 3, the local boost inequality inside a window, which
would handle η-twin conditions; or a direct attack on H_light via
reachability (item 2).

## 3. Numerics on the real forced-class system (route 8; all EVIDENCE)

Script: `scripts/balanced_numerics.py`. The system is the full Case-B family
ℛ(M) for `M ≡ 3 (4)`, `M ≤ X`. Moduli are typed by `P = P(M)`,
`P₂ = P(M/P)` and `η = 1/4`:
* `dom`: `P ≥ M^{2/3}`;
* `gapM`: gapped with `√M < P < M^{2/3}`;
* `gapB`: gapped and balanced (`P ≤ √M`);
* `twin`: `P < P₂^{1+η}`.

### 3.1 Sequential hit probabilities p_ℓ(h): does (★_δ) / H_light look true?

**Method.** Draw histories from `Q_seq` with singleton windows. Primes are
taken in increasing order. At p, the residue `n mod p^e` is uniform among
residues completing no condition with top prime p. This is ET §2.6 with
one prime per window, a finer ordering than §2's η-windows. Record
`p_p(h) = |F_p(h)|/p^e`, split by type.

*Steered histories* are a greedy adversary. The path stays in the support
of `Q_seq`, so it is reachable by construction. At each earlier prime it
chooses the allowed residue that keeps the most distinct target values at ℓ
alive. This gives a lower bound for `sup_h p_ℓ(h)`.

Data: `data/balanced/part_i_X1e5.txt` (200 histories),
`part_i_X1e6.txt` (20 histories), `steer_X1e5.txt`.

**Per dyadic band of top primes, X = 10⁶ (twin and gapB rows):**

| band | type | Σ M_p (uniform) | Σ E_seq p | K = ratio | max_h p(h) | max p(h)·√p |
|---|---|---:|---:|---:|---:|---:|
| [32,64) | twin | 1.280 | 0.785 | 0.61 | 0.281 | 1.84 |
| [64,128) | twin | 1.797 | 1.226 | 0.68 | 0.195 | 1.78 |
| [128,256) | twin | 1.667 | 1.297 | 0.78 | 0.137 | 1.57 |
| [256,512) | twin | 1.348 | 1.112 | 0.82 | 0.072 | 1.20 |
| [512,1024) | twin | 0.959 | 0.860 | 0.90 | 0.032 | 0.85 |
| [128,256) | gapB | 1.532 | 1.007 | 0.66 | 0.130 | 1.49 |
| [256,512) | gapB | 1.336 | 0.941 | 0.70 | 0.068 | 1.11 |

**Union over all types** (the quantity that enters (★_δ)/H_light, since
`F_ℓ` is a union; review D13):

| band | X | Σ M_p | Σ E_seq p | K | max_h p(h) | max p(h)·√p | frac(p(h) > 1/4) |
|---|---|---:|---:|---:|---:|---:|---:|
| [128,256) | 10⁵ | 5.418 | 3.523 | 0.65 | 0.317 | 4.10 | 2.7% |
| [128,256) | 10⁶ | 7.172 | 4.485 | 0.63 | 0.329 | 4.33 | 15.4% |
| [256,512) | 10⁵ | 5.412 | 3.814 | 0.70 | 0.232 | 4.22 | 0% |
| [256,512) | 10⁶ | 7.779 | 5.226 | 0.67 | 0.259 | 4.28 | 0.2% |
| [512,1024) | 10⁶ | 7.412 | 5.343 | 0.72 | 0.161 | 4.33 | 0% |

Across X = 10⁵ and 10⁶, all bands and types:
* `K` ranges over 0.48–1.00, so sequential conditioning *deflates* the
  profile, as in ET §5.3(iii) (review D14 corrected the range).
* `max_h p(h)·√p ≤ 4.4`.
* **Heavy histories (`p(h) > 1/4`) occur at top primes up to 512 at
  X = 10⁶.** In [128,256) they rise from 2.7% to 15.4% of sampled histories
  as X goes from 10⁵ to 10⁶. The union mass per prime also grows with X,
  since more cofactors enter at fixed ℓ. (An earlier version said "only
  for p < 128"; that is false for X = 10⁶, review D13.)

**Steered (adversarial) histories.** See §4.3 for the regenerated data
(review D17). At small primes the adversary reaches p(h) = 0.84 at p = 31
and 0.62 at p = 47 (X = 10⁶), against typical values near 0.3–0.4. So
heavy reachable histories exist at small primes.

**Reading (corrected).**
* At fixed X, `p_ℓ(h) ≲ 4.4ℓ^{−1/2}` on sampled histories.
* The heavy region moves **up with X**. With B unrestricted (all moduli
  ≤ X), a fixed w₀ cannot work. This is consistent with the per-prime
  union mass growing with the number of cofactors.
* For a fixed B (the setting of Thm 2.5), the data neither confirm nor
  refute (★_δ): `B = log X/log ℓ − 1` is not held fixed across these
  runs. The earlier "consistent with (★_δ) for δ ≈ 1/2 above w₀ ≈ 128" is
  withdrawn.
* Caveats:
  * the scales are tiny;
  * the adversary is greedy and weak;
  * singleton windows differ from η-windows.

### 3.2 Exact LP: best level-m majorant, dominant vs dominant + composite

**Method.** Take a set S of 4–5 primes of similar size. The space is
`ℤ/Q`, `Q = ΠS`, exactly. The conditions are all classes ℛ(M) for
squarefree `M | Q` with `M ≡ 3 (4)`. Four families:
* **D:** prime moduli only. These are dominant.
* **D+pairs:** adds the two-prime moduli. A two-prime modulus pq is
  **never balanced** (`P > √(pq)`). Within one window it is η-twin or
  η-gapped, e.g. 91 = 7·13 is gapped at η = 1/4.
* **D+composite:** all moduli. The **balanced** ones are exactly those with
  ≥ 3 primes: 1463, 1771, 2431, 3059, 4199, 4807, 19019, … For
  S = {7,11,19,23}, every prime is ≡ 3 (4), so there are no pair conditions
  at all. (Review D16: an earlier version called all composites "balanced".)
* **D+S (matched-mass control):** D, plus, for each composite condition of
  mass w, `round(w·P)` fresh random residues at its top prime P.

Level m means every term depends on at most m of the primes. The LP is
the dual form of §1 route 1, solved with HiGHS-IPM in floating point,
uncertified. Data: `data/balanced/part_ii_S*.txt`.

**Savings `−log(LP optimum)`** (void = `−log P(𝒜)`):

| S | family | mass | void | m=1 | m=2 | m=3 |
|---|---|---:|---:|---:|---:|---:|
| 7,11,13,19 | D | 0.859 | 1.050 | 0.560 | 0.999 | 1.050 |
| | D+pairs | 1.082 | 1.246 | 0.560 | 0.999 | 1.206 |
| | D+composite | 1.102 | 1.253 | 0.560 | 0.999 | 1.206 |
| | D+S | 1.066 | 1.282 | 0.560 | 1.081 | 1.263 |
| 7,11,19,23 | D (= D+pairs) | 1.250 | 1.546 | 0.560 | 1.208 | 1.502 |
| | D+composite | 1.287 | 1.563 | 0.560 | 1.208 | 1.502 |
| | D+S | 1.347 | 1.685 | 0.571 | 1.253 | 1.613 |
| 11,13,17,19 | D | 0.431 | 0.490 | 0.318 | 0.490 | 0.490 |
| | D+pairs | 0.665 | 0.709 | 0.318 | 0.525 | 0.691 |
| | D+composite | 0.707 | 0.741 | 0.318 | 0.525 | 0.691 |
| | D+S | 0.749 | 0.852 | 0.318 | 0.807 | 0.847 |
| 7,11,13,17,19 | D | 0.859 | 1.050 | 0.560 | 0.999 | — |
| | D+composite | 1.426 | 1.501 | 0.560 | 0.999 | — |
| | D+S | 1.354 | 1.619 | 0.560 | 1.125 | — |

(m = 3 on five primes is out of reach: the IPM normal matrix is dense,
with about 5·10⁴ rows. D+pairs was not rerun on five primes.)

**Reading (corrected).**
1. **Pairs (non-balanced, mostly η-twin).** They add nothing at m = 1.
   They add 0 or +0.035 at m = 2, where they are already visible, and
   gain at m = 3.
2. **Genuinely balanced (≥ 3-prime) classes.** On top of D+pairs they add
   **0** at every m ≤ 3 in all three 4-prime windows. The ≥ 3-prime
   moduli have cost about 3·log p, so at m ≤ 3 this is close to the
   visibility threshold. The test is weak.
3. **The control does better.** Single-prime conditions of matched mass
   beat the composite ones at every m ≥ 2 (S = {11,13,17,19}, m = 2:
   +0.317 vs +0.035). This fits "a multi-prime condition costs its full
   modulus".

Caveat: these are toy sizes in a dense regime (mass ~1, primes < 25).
The asymptotic sparse regime is not probed. This is weak evidence, and
mostly about η-twin *pairs*, not balanced moduli.

### 3.3 Void probabilities among real primes, both orders

**Method.** `scripts/balanced_void.cpp` runs over all 1,085,136,872 primes
in `[10¹², 10¹² + 3·10¹⁰)`. It uses four families of classes ℛ(M) with
`M ≤ Q'`:
* **dom:** `P ≥ M^{2/3}`;
* **dom+gap:** dom plus the η-gapped moduli (η = 1/4);
* **dom+twin:** dom plus the η-twin moduli;
* **all.**

Entries are `Δ(−log void)/Δμ_pr`, the effective void per unit of added
prime-conditioned mass, in **both orders** (review D15). Data:
`data/balanced/void_primes_Q4000.txt`. The numbers match the reviewer's
independent variant.

| Q' | twin added to dom | gap added to dom+twin | gap added to dom | twin added to dom+gap |
|---:|---:|---:|---:|---:|
| 275 | 0.42 | 0.62 | 0.73 | 0.17 |
| 606 | 0.45 | 0.52 | 0.63 | 0.20 |
| 1333 | 0.47 | 0.49 | 0.59 | 0.22 |
| 2253 | 0.49 | 0.47 | 0.58 | 0.22 |
| 4000 | 0.52 | 0.50 | 0.54 | 0.42 (3 primes; noise) |

For comparison, dom alone has `−log void / mass → 1.00`.

**Reading (corrected).**
* Added directly to dom, the η-twin classes yield ≈ 0.45–0.5 per unit
  mass. For Q' ≥ 1333 this matches the gapped classes.
* Each non-dominant family yields less when added after the other:
  ≈ 0.2 for twin, ≈ 0.5 for gap.
* So twin and gapped classes overlap each other, and both overlap dom.
  The twin family is **not** specially redundant. The earlier
  "η-twin ≈ 0.2, strongly redundant" was an ordering artefact and is
  **withdrawn** (review D15).
* The defensible statement: non-dominant classes give about half their
  mass in void when added to the dominant system. Dominant classes give
  about all of it.
* Caveat: `Q' ≤ 4000`, so twin top primes are ≤ 63, and only one prime
  range is tested. The void caps every sieve; it is not a majorant
  saving.

## 4. Attempt on (★_δ) for B ≥ 1

Setting of §2 (ℛ(M)-grouping). Fix a window prime ℓ and level data:
* `X` bounds the moduli;
* `y := ℓ^{1/(1+η)}` bounds the cofactor primes;
* the *admissible cofactors* are
  `𝒬_ℓ = {q ≥ 1 : qℓ ≡ 3 (4), qℓ ≤ X, P(q) ≤ y}`, and for a fixed B,
  `𝒬_ℓ^{(B)} = {q ∈ 𝒬_ℓ : q ≤ ℓ^B}` (the (η,B)-gapped cofactors; review
  D11). Primes ≤ w₀ may divide q, and their residues belong to the free
  small coordinate.
* The *balanced* cofactors are those with `q ≥ ℓ`, i.e. `P(qℓ) ≤ √(qℓ)`.
  Cofactors `q < ℓ` give dominant-type moduli.

A history determines `n mod q` for every `q ∈ 𝒬_ℓ`, and

    F_ℓ(n) = { −4D mod ℓ : q ∈ 𝒬_ℓ, D | A_q², q | n + 4D },   A_q := (qℓ+1)/4.

So `p_ℓ(h) = |F_ℓ(n)|/ℓ` for any integer n representing h. (★_δ) asks for
`|F_ℓ(n)| ≤ ℓ^{1−δ}` on reachable histories.

### 4.1 The (s, r, k) parametrization

**Lemma 4.1 (PROVED).** Write `D = s r²` with s squarefree, so that
`g(D) = sr`. Then `D | A_q²` iff `A_q = s r k` for some integer k ≥ 1.
For such a triple:
1. `gcd(k, q) = gcd(r, q) = 1` and `ℓ ∤ k`;
2. `q | n + 4D` iff `q | nk + r`;
3. `−4D ≡ −r·k^{−1} (mod ℓ)`.

Hence

    F_ℓ(n) = { −r k^{−1} mod ℓ : s, r, k ≥ 1, s squarefree, q := (4srk−1)/ℓ ∈ 𝒬_ℓ, q | nk + r }.

*Proof.* `v_p(D) ≤ 2v_p(A)` iff `⌈v_p(D)/2⌉ ≤ v_p(A)`. So `D | A²` iff
`g(D) | A`, and `g(sr²) = sr`. From `4srk = qℓ + 1`:
* every common divisor of q with k, r, or with ℓ and k, divides 1, which
  gives (1);
* modulo q, `4sr²·k = r·(4srk) ≡ r`, so `k(n + 4D) ≡ nk + r (mod q)`; since
  k is a unit mod q, this gives (2);
* modulo ℓ, `4srk ≡ 1`, so `4sr² ≡ r k^{−1}`, which gives (3). ∎

So a value at ℓ depends only on the ratio `r/k mod ℓ`. A class is switched
on by the single congruence `nk + r ≡ 0 (mod q)` (the POINTWISE_OMEGA
`D = sr²` trick).

### 4.2 Counting works exactly when B < 1

**Lemma 4.2 (PROVED).** For every integer n,

    |F_ℓ(n)| ≤ Σ_{q∈𝒬_ℓ} #{D | A_q² : q | n+4D} ≤ Σ_{q∈𝒬_ℓ} τ(A_q²) ≤ |𝒬_ℓ| · X^{o(1)}.

So `p_ℓ(h) ≤ |𝒬_ℓ|·X^{o(1)}/ℓ` for every history, reachable or not.
* For (η,B)-gapped families with `B < 1`, `|𝒬_ℓ| ≤ ℓ^B`, so (★_δ) holds
  with any `δ < 1−B`. This is ET Cor 3.6's argument.
* For `B ≥ 1`, `|𝒬_ℓ^{(B)}| ≥ ℓ^{1+o(1)}`, so the bound is vacuous.

So the *counting bound* gives (★_δ) iff B < 1. This is a statement about
the method, not about (★_δ) (review D6).

*Proof.* The first inequality is the union bound over (q, D). Then use
`τ(A²) ≤ X^{o(1)}`, which is `ℓ^{o(1)}` when `q ≤ ℓ^B`. For the size
claim: `|𝒬_ℓ^{(B)}| ≍ Ψ(ℓ^B, y)/2 ≫_{η,B} ℓ^B` by Dickman, since
`log ℓ^B/log y = B(1+η)` is bounded. ∎

For a fixed q, at most `τ(A_q²) = ℓ^{o(1)}` values are ever active,
whatever n is. So the whole difficulty is *how many cofactors q can be
active at once with distinct values*. That is a maximum over n, a
CSP-type extremal problem, and not a counting problem.

### 4.3 The supremum is far above the average

**Proposition 4.3 (PROVED, given Linnik's theorem with some exponent L;
L ≤ 5.2 by Xylouris 2011, L = 5 in his 2018 thesis; review D7).** Assume
`X ≥ ℓy`, and let `K = c₀ y^{1/L}` with c₀ small. Then some integer n has

    |F_ℓ(n)| ≫_η π(2K) − π(K),   so   sup_n p_ℓ(n) ≥ ℓ^{−1 + 1/(L(1+η)) − o(1)}.

The typical value is `E_U p_ℓ ≤ (log ℓ)^{O(1)}/ℓ` (only the upper bound is
proved).

**Framing (review D9).** The witnesses are prime cofactors `q_k ≤ y < ℓ`.
So every modulus `q_kℓ` is *dominant*, not balanced: `P(M) = ℓ > √M`, with
`B = 1/(1+η) < 1`. That is the regime where Lemma 4.2 already proves
(★_δ). Prop 4.3 therefore shows only that the supremum exceeds the
average. It is **no evidence** about the balanced content of (E_δ), which
lives in the composite cofactors `q ∈ [ℓ, ℓ^B]`.

*Proof.*
1. *A prime cofactor for each k.* For each prime `k ∈ (K, 2K]`, `k ≠ ℓ`,
   Linnik gives a prime `q_k ≡ −ℓ^{−1} (mod 4k)` with
   `q_k ≪ k^L ≤ y`. Then `4k | q_kℓ+1`, so `k | A_{q_k}`, and
   `q_k ∈ 𝒬_ℓ` because `q_kℓ ≤ yℓ ≤ X`.
2. *A distinct value for each k.* Put `D_k := A_{q_k}/k`, a divisor of
   `A_{q_k}²`. By Lemma 4.1(3), or directly from `4A ≡ 1 (mod ℓ)`,
   `−4D_k ≡ −k^{−1} (mod ℓ)`. These values are distinct for distinct
   `k < ℓ`.
3. *Distinct cofactors.* Two kept pairs sharing a prime q would need
   `n ≡ −4D_k ≡ −4D_{k'} (mod q)`, so we keep one k per prime q_k. One q
   serves at most `#{k > K prime : k | A_q} ≤ log A_q/log K ≤
   log(ℓy)/log K = O_η(1)` values of k. This leaves `≫_η π(2K)−π(K)` pairs
   with distinct primes q_k and distinct values (review D8).
4. *A single n.* By CRT, some n has `n ≡ −4D_k (mod q_k)` for every kept
   k. All the kept pairs are active at this n. ∎

**Caveats.**
* The construction ignores reachability. The constructed n need not avoid
  the earlier conditions.
* HEURISTIC: the same construction with *all* primes `q ≤ y`, each
  carrying its own value, gives `|F_ℓ(n)| ≍ π(y)`. This too is
  dominant-type.

**Numerics (EVIDENCE).** `balanced_numerics.py steer` runs a greedy
adversary, with reachability enforced ("reach") or ignored ("free"),
X = 10⁵, η = 1/4, `y = min(ℓ^{0.8}, X/ℓ)`:

| ℓ | 101 | 211 | 307 | 401 |
|---|---:|---:|---:|---:|
| distinct values, reach | 13 | 15 | 21 | 31 |
| distinct values, free | 13 | 16 | 21 | 36 |
| π(y) | 12 | 20 | 25 | 30 |

So the greedy supremum tracks `π(y)` (a weak adversary, lower bounds
only). Reachability costs almost nothing. If `sup ≍ π(y)·ℓ^{o(1)}` is the
truth, (★_δ) holds exactly for `δ < η/(1+η)`, and it is sharp there.

### 4.4 Reduction: the remaining gap is an extremal arithmetic problem

**Gap (E_δ) (named; open for B ≥ 1).** Fix B. For every window prime
`ℓ > w₀` and **every** integer n,

    #{ −r k^{−1} mod ℓ : (4srk−1)/ℓ = q ∈ 𝒬_ℓ^{(B)}, q | nk + r } ≤ ℓ^{1−δ}.

**Proposition 4.4 (PROVED).** Fix B, and let `w₀ = w₀(δ) ≥ 4^{1/δ}`.
(E_δ) for `𝒬_ℓ^{(B)}` implies (★_δ) for every (η,B)-gapped subfamily.
Hence it implies H_light(O_δ(1)), with (ii) in the cubic form of §2.5, and
so Theorem 2.5's cap `S_λ ≪_{δ,B} η^{−1}λ^{3/4}`.

*Proof.* By Lemma 4.1, (E_δ) bounds `|F_ℓ(n)|` for every integer n, so in
particular on every reachable history; a subfamily gives a subset. Then:
* `ℓ^{−δ} ≤ 1/4` for `ℓ > w₀` gives no heavy coordinates and (NDE);
* the sanity check of §2.5 gives the cubic window bound H_light(ii) with
  `K = O_δ(1)`. ∎

**Conjecture 4.4W (weak form; SKETCH, not proved; review D12-W).** If only
`p_ℓ(h) ≤ ε` is known for all `ℓ > w₀`, then the cap is `λ^{3/4+O(ε)}`.

*Sketch and its gap.* The profile inflation is `≤ (1−ε)^{−ω(q)}`. Write
`e^{cεω(q)} = Σ_{d|q} h(d)` with `h(p) = e^{cε}−1 ≍ ε`. In the Shiu range
(`d ≤ x^{1/2}`), the Euler factors change by `1 + O(ε)/p`, so the pole
order rises by `O(ε)`. **Gap:** h does not decay in p. So the large-divisor
range `d > x^{1/2}` of ET Lemma 3.1 / Cor 3.6 is no longer `o(x)`:
`Σ_{d≤x} h(d) ≍ x(log x)^{O(ε)−1}`, against a trivial `x^{1/10}` from τ.
ET Cor 3.6 needed `Σ h(d)d^{−1+δ/2} < ∞`, which fails here. A
two-variable mean-value bound (Nair–Tenenbaum/Henriot type) for
`τ(A²)(1+O(ε))^{ω(4A−1)}` would plausibly close this gap.

**What is known about (E_δ).**
* Counting proves it for B < 1 (Lemma 4.2), i.e. for the dominant
  cofactors `q < ℓ^{B'}`, `B' < 1`.
* Prop 4.3 shows the supremum is at least `y^{1/L−o(1)}`. Its witnesses
  are dominant (prime) cofactors.
* **Nothing is known** about whether composite cofactors `q ∈ [ℓ, ℓ^B]`
  (the balanced content) can push `sup|F_ℓ|` above `π(y)ℓ^{o(1)}`. The
  §4.3 numerics count all types and do not isolate this. The claim
  "(★_δ) holds exactly for `δ < η/(1+η)`" is HEURISTIC; only `y^{1/L}` is
  proved.

**Why the obvious proof attempts fail** (HEURISTIC discussion; review D18).
1. *Coprimality.* Two active triples with distinct values and common
   factor `g = gcd(q,q')` need `g | rk'−r'k`. This forces near-coprimality
   only when r and k are small. But r and k range up to `A_q ≈ qℓ/4`. Small
   r and k give at most `R²` values anyway.
2. *Largest-prime injection.* Map each active q to `P(q)`. The q's with
   `P(q) > R²` contribute at most `π(y)` values. The `R²`-smooth q's still
   number `≍ ρ(B/ε)·ℓ^B ≥ ℓ` when `R² = ℓ^ε`. So the count is not killed.
3. *Averaging over histories (the "steering is rare" route).* Theorem 2.3
   needs `Q_seq`-expectations. Q_seq reweights U by
   `dQ_seq/dU = Π_p (1−p_p(h))^{−1}`. This weight is controlled only
   through sup bounds at the smaller primes p | q, i.e. through (★) at
   lower scales again.
   * A bootstrap over scales (assume (★_δ) below ℓ, deduce it at ℓ) would
     need U-tails `U(|F_ℓ| ≥ ℓ^{1−δ}) ≤ exp(−ℓ^{1−δ}/log ℓ)`.
   * Histories that fix the residues at about π(y) primes already have
     U-probability `≥ e^{−O(y)}`. Whether some of them are heavy is
     exactly the balanced question above.
   * So the averaged route was **not carried out**. The heuristic
     suggests it is no easier than (E_δ), not that it is borderline at a
     proved threshold. (An earlier version claimed a borderline at
     `δ = η/(1+η)`; that rested on the dominant-type construction, review
     D9.)

**Status of step 4.** (★_δ) for `B ≥ 1` is **not proved**. For each fixed
B it is reduced to the purely arithmetic extremal statement (E_δ) on
`𝒬_ℓ^{(B)}`. Reachability, Q_seq and sieve structure are gone from that
statement. The open content is the composite (balanced) cofactors. No
evidence collected here bears specifically on them (review D9, D17), and
§3.1's union data show heavy histories moving up with X (review D13).
