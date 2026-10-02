# AGENT_REPORT_O1 — (E_δ), heavy coordinates, η-twin windows (checkpoint 1)

Branch: `side-agent/twin-windows`. Deliverable: `EXCEPTIONAL_TWIN.md`
(scripts `scripts/twin_*.py`, data `data/twin/`).

## Headline

**(E_δ) is bypassed, not settled.** The (η,B)-gapped part of the balanced
door is now unconditional (Theorem 2.7): `S_λ ≪_B η^{−1}λ^{3/4}` for every
fixed B, with no (E_δ), (★_δ), H_light or (NDE).

Two new ingredients:
1. **QR base (Lemma 1.1, 1.3).** Every Case-B class `−4D (mod M)` has
   Jacobi symbol −1 (classical Mordell obstruction). So the *product*
   measure "n a nonzero square mod every odd p ≤ W" lives on avoiders of
   all W-smooth classes. It costs `π(W) log 2` and inflates later
   probabilities by only `2p/(p−1)` per prime, instead of ET's
   `L' = e^{O(W^{1+C})}`.
2. **Capped distortion (Thm 2.3).** This is a variant of the distortion
   method of Hough (2015) and Balister–Bollobás–Morris–Sahasrabudhe–Tiba
   (arXiv:1811.03547). In BBMST heavy fibres are capped-distorted, and the
   result bounds the uncovered density. Here the sequential measure
   conditions fully where `p_ℓ(h) ≤ ℓ^{−1/2}` and leaves heavy coordinates
   uniform; heavy hits leak. The leak is
   bounded by a second moment, `E p_ℓ² ≪ ℓ^{−2+ε}` (Lemma 2.4). This needs
   only divisor bounds, and with the QR base it is uniform in W. So the
   leak is `≪ W^{−1/4}` (Cor 2.5). The caps give ET Cor 3.6's inflation
   structure for free (Lemma 2.6).

**η-twin.** All classes (twin, ≥ 3 primes per window, prime-power top
included) are harmless with top prime `≤ e^{λ^{1/4}}` (singleton windows;
cost = void, Prop 4.1) or `> e^{λ/2}` (one-prime-per-term window
inequality, Lemma 4.2 / Cor 4.3). Lemma 4.0 extends the second moment to
prime-power tops. Theorem 4.4 combines these with Theorem 2.7. The residual
is *unresolved* moduli (last window contains ≥ 2 of their primes, or a
prime power) with top prime in `(e^{λ^{1/4}}, e^{λ/2}]`. It is reduced to
one family of named inequalities, Conjecture 4.5_r: an r-ary window
inequality, `r ≤ (1+B)(1+η)`, the local boost. The 2-prime case alone is
not enough once `(1+B)(1+η) ≥ 3`. §4.5 says why splitting,
over-conditioning, leak, void and the linear lemma stall there; that
discussion is mostly HEURISTIC.

**(E_δ) itself (§3).** OPEN. New: the u-form (Lemma 3.1), a Legendre-sign
constraint (Lemma 3.2), and an entropy heuristic predicting
`sup ≈ π(y)ℓ^{o(1)}`.

**Global (§5).** Not settled. 3/4 is now proved sharp (internally) for
ℛ(M)-families with `M ≤ P(M)^{1+B}`, for each fixed B, except for
unresolved moduli in the middle range. This assumes ET Lemma 2.9's
hypotheses (slice primes ≤ N^{O(1)}, rounding budget Σ|a_i| < N). Also open:
uniformity in B, and (a,D)/Case-A classes for balanced moduli.

## Labels

PROVED: Lemma 1.1–1.3, Lemma 2.1, 2.2, Thm 2.3, Lemma 2.4, Cor 2.5,
Lemma 2.6, Thm 2.7, Lemma 3.1, 3.2, Lemma 4.0, Prop 4.1, Lemma 4.2,
Cor 4.3, Thm 4.4.
EVIDENCE: §2.4. With theorem-compatible caps `min(1/4, p^{−0.2})` at
X = 10⁵ (full system, twin included), the leak is 100% at W = 30, 46% at
W = 100 and 0 at W = 300. Looser caps (not theorem-compatible) give
0.06–0.07 at W = 30.
HEURISTIC: Heur 3.3, §4.5 items 1–4. OPEN: (E_δ), Conj 4.5_r.

## Self-review (reviewer subagent, deep mode) and repairs

The reviewer found Theorem 2.7 sound: Thm 2.3, Lemma 2.4/Cor 2.5 and
Lemma 2.6 all check out. Defects and repairs:
* HIGH: a binary conjecture does not cover moduli with ≥ 3 primes in the
  last window (`101·103·109`). Repaired: the residual is now defined via
  "window-resolved", and the conjecture is r-ary (4.5_r).
* MEDIUM: prime-power tops were not handled by (U) "verbatim". Repaired:
  §4.1 adds the prime-power interface (full-fibre conditioning) and
  Lemma 4.0 (second moment with `M = qℓ^v`).
* MEDIUM: Lemma 3.1's inverse form needs `gcd(n, q) = 1`. Repaired.
* MEDIUM: the κ = 0.2 runs violate the cap `δ ≤ 1/4`. Repaired: labelled,
  and theorem-compatible runs added.
* MEDIUM: the quadratic-test observation had wrong algebra. Removed.
* MEDIUM: failure analysis overstated. Requalified as HEURISTIC.
* MEDIUM: the global level conversion omitted ET Lemma 2.9's hypotheses.
  Restored.
* Minor fixes: `(1+2B log ℓ)^9`; partial prime powers in Lemma 2.2;
  the "non-residue" remark in §2.4 corrected (it needs `(n|q) = 1`); the
  top-window cost doubled; a lower bound on λ in Thm 4.4; "primes 31–255";
  the Jacobi script exit status.

## Where a hostile reviewer should look first

* Thm 2.3, the induction step: f̃ is λ-level in the light indicators
  after averaging out the heavy ones, and the final Jensen step with
  `Q'(𝒜) ≥ 1/2`.
* Lemma 2.4: the uniformity in W of `E N_ℓ²` (the Γ ≤ 3^ω bound and the
  τ(A_q²) ≤ ℓ^{ε} bound, which needs B fixed).
* Lemma 2.6: transplanting ET Cor 3.6's γ-weighted Lemma 3.1 to the weight
  Γ (h(p) ≤ 2 for p ≤ W; h(ℓ) ≤ 2ℓ^{−1/2} above).
* Cor 4.3: Lemma 4.2 is applied to f as a function of residues (not hit
  indicators), with σ the in-window sequential capped law.

## Decision needed from parent

Should the next step attack Conjecture 4.5 directly (a binary version of
ET Prop 2.4), or first make the B-dependence explicit? The latter is
needed to cover moduli with `log M/log P(M) → ∞`.

## Hostile review (side-agent/review-twin) repairs, T1–T8, S1

All items were graded SOUND or SOUND-AFTER-REPAIRS; Thm 2.3, Lemma 2.4 and
Thm 2.7 were graded SOUND. Repairs:
* T1: BBMST/Hough citation, and the variant stated precisely.
* T2: N_ℓ is over the full Q' history.
* T3: Remark 2.5′ (caps `min(1/4, ℓ^{−κ})`).
* T4: the W = 300 run shows only that the leak bound is attainable at toy
  scale; the κ = 0.5 run is saved.
* **T5:** Theorem 2.3′ (abstract sequential step) and Lemma 2.1′ (leak for
  in-block orders); Thm 4.4 now cites these.
* T6: W₀(B) uses Lemma 4.0's constant.
* T7: λ-range for the θ-statement.
* T8: the caps cover their families separately.
* S1: Remark 1.4 (square base), with an (a,D)/Case-A check script.

# Checkpoint 2 — attack on Conjecture 4.5_r (§6)

**Outcome: reduced, not proved.** Conjecture 4.5_r is reduced to a
sharper, arithmetic-free gap, and a weaker form is shown to suffice for
the exponent question.

* Lemma 6.1 (PROVED): ET Prop 2.4 holds for *soft* unary conditions, so
  any product law with densities `≤ (1−p_ℓ)^{−1}` is reached at cost Φ(p).
* Lemma 6.2 (PROVED): step inequalities compose. A block step therefore
  splits into a unary step (Lemma 6.1) and a k-ary comparison step.
* Lemma 6.3 (PROVED): Markov removal of residues with incident k-ary
  weight > θ. The cost is a constant-factor increase of the cubic unary
  profile; afterwards the k-ary system is locally sparse.
* **Conjecture 6.4 (OPEN, the sharpened gap).** For a product law ν and
  hard k-ary constraints with incident weights ≤ θ₀, the sequential capped
  conditioning σ satisfies `E_σ f ≤ exp(C_r[d log(2+μ_{≥2}) + 1]) E_ν f`
  for λ-level f ≥ 0. No arithmetic, no unary sieve.
* Prop 6.5 (PROVED): Conj 6.4 implies `S_λ ≪_B η^{−1}λ^{3/4} log λ` for
  *all* ℛ(M)-families with `M ≤ P(M)^{1+B}`, twins included. So 6.4 alone
  would settle the exponent question for fixed B (up to `log λ`).
* Evidence (§6.4, weak, toy scale): exact window LPs at m ≤ 6, L = 5. With
  σ uniform on the avoid set, binary constraints extract a smaller share of
  their void than unary constraints of equal mass at the same d. A caveat
  that matters: with the *sequential* σ, dense toys give `log C*` above the
  void. So 6.4 needs the caps and the sparsity hypothesis, and the choice of
  σ is part of the problem.
* Remark 6.5 (PROVED, small): ET Thm 5.5 (the Λ² cap) holds with any σ̃
  on A, giving `saving ≤ αλ/2 + log E_S[1 + χ²(σ̃_S‖U_S)]`. This is the
  tool for ET's fibre-term obstruction; no bound for the real system.

**Why no proof.** ET Prop 2.4's proof (thinning, symmetrisation within
bands, interpolation in band counts) needs independent coordinates. With
k-ary constraints there is nothing to symmetrise. The obvious substitutes
fail:
* the truncated density certificate `P_{≤d}(dσ/dν)` blows up at
  configurations with many hits, already for unary constraints at d = 2;
* pointwise domination of all d-marginals does not imply junta domination,
  because majorant terms can be signed;
* the exponential-moment form of the Λ² collision bound is dominated by
  rare histories.

**Suggested next step.** Attack Conjecture 6.4 for r = 2 in the sparse
regime directly: a "binary Prop 2.4", perhaps by symmetrising over the
residue alphabets (the structure is one-hot per prime), or via the Λ²
collision functional with a tilted σ̃ as an intermediate (H_MS^{Sel}
first).
