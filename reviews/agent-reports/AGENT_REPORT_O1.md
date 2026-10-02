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
2. **Capped distortion (Thm 2.3).** Following
   Balister–Bollobás–Morris–Sahasrabudhe–Tiba, the sequential measure
   conditions only where `p_ℓ(h) ≤ ℓ^{−1/2}`. Heavy hits leak. The leak is
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
