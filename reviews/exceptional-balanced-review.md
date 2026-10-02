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
