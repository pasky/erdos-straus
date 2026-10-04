# AGENT REPORT O17 — large-sieve limit for forced-class mixtures (checkpoint 1)

Branch `side-agent/largesieve-limit`. Deliverables: `EXCEPTIONAL_LARGESIEVE.md`,
`scripts/ls_duality_check.py` (Replay ~10 s, `uv run --with cvxpy --with numpy`).

## Results

1. **Exact duality (Thm 2.1, Cor 2.2; PROVED).** For any frequency set Θ and
   weights, the best *CRT-admissible* large-sieve denominator (a lower bound
   valid for every probability law on 𝒜) is `F*_w = 1/m_w`, where
   `m_w = min Σ|γ_θ|²/w_θ` over `g = Σγ_θ e(−nθ)` with `Re g ≥ 1` on 𝒜
   (von Neumann minimax). Every N-large-sieve system has `w_θ ≤ 1/N`, so
   every such bound is `≥ N·E|g*|²`. `|g*|²` is a nonnegative CRT majorant
   (Selberg square) whose moduli are lcm's of two frequency denominators.
2. **Cap for all mixtures (Thm 3.1, Cor 3.2; PROVED, Case A via ElT Prop 1.4
   as in KARY2).** With KARY2 Thm 5.1: any CRT-admissible large sieve —
   Montgomery/MV/weighted, Farey with prime, prime-power or composite
   moduli, forced classes used in any form, fibrewise over `Q₀ ≤ N/2` —
   saves `≤ Cλ^{3/4}(log λ)^{3/4}`, `λ = λ(Q₀) + 2λ_Θ` (W-rough levels).
   With polynomial denominators: `≤ C(log N)^{3/4}(log log N)^{3/4}`, and
   `C_B(log N)^{3/4}` for bounded B. No rounding/coefficient-sum term is
   needed, because the large sieve's `N + δ^{−1}` already contains N.
3. **Prime slices, any frequencies (Thm 4.1, Cor 4.2, Rem 4.4; PROVED).**
   Fourier–Rankin bound via a product measure, Hausdorff–Young in the
   small coordinate, and Hölder with the trace bound `Σw_θ ≤ 1`: no level
   condition at all (sparse rationals with huge denominators included).
   ET Cor 3.4 families: `≤ C(log N)^{3/4} + log(P/φ(P))`.
4. **Key question (§5).** Prime moduli: `S_c(Q)` ≤ exp(Rankin functional),
   tautologically. Composite moduli: the small-prime-conditioned Euler
   product does **not** dominate (Example 5.2: twin ℛ(ℓℓ')-classes give an
   empty prime-local system but `F* ≥ 1 + g`). The dominating functional is
   the top-prime sequential (KARY) one, reached through duality.
5. **Gallagher's larger sieve (Thm 6.2, Cor 6.3; PROVED).** Kernel form with
   any moduli: saving `≤ log(1 + N·X(π)/(W−h))`, X a χ² functional of the
   mod-q marginals of any π on 𝒜. Gallagher (Λ weights): `≤ X(π) + O(1)`;
   `O(1)` on ET Cor 3.4 prime slices.

## Exact remaining escape (§7)

* (E1) frequencies of super-polynomial level (`λ_Θ ≥ (log N)^{1+ε}`) against
  multi-large-prime classes; closing it needs (H_LS): a law on 𝒜 with
  `log Σ_θ|π̂|^{2+2β} ≪ (log N)^{3/4}polylog`. CONJECTURE.
* (E2) larger sieve over mixtures; needs (H_Gal) (near-uniform prime-power
  marginals of some law on 𝒜). Open. The squares give only the QRs mod ℓ.
* (E3) non-CRT interval information; (E4) KARY2's inherited exclusions.

## Review status

One internal deep self-review (`review` tool, since 9940611). Its defects are
all applied:
* weighted-sequence remark restricted to comparable weights;
* `Q₀ ≤ N/2` restored throughout;
* the general kernel separated from the Gallagher corollary;
* prime-slice claims tied to the ET Cor 3.4 hypotheses;
* script hardened (solver status and tolerance asserts, sparse frequency
  sets, degenerate F* = 0 case);
* Example 5.2 numerics described as analogues.

The reviewer confirmed Thm 2.1, Facts 1.1/4.0, the Thm 3.1 level count, the
Thm 4.1 constants, Ex 5.2, and Lemma 6.1/Thm 6.2/Cor 6.3. No hostile review
by the parent yet.

## For the parent

* Suggested ledger entry: (D)19, the large sieve over forced-class mixtures
  capped at 3/4 (Thm 3.1), PROVED internal. This would supersede the "large
  sieve beyond prime slices" exclusion in (D)18 / KARY2 §6, except for (E1)
  and (E2).
* I did not touch STATUS.md or DISCOVERIES.md.
