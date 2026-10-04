# AGENT REPORT O17 — large-sieve limit for forced-class mixtures (checkpoint 2)

Branch `side-agent/largesieve-limit`. Deliverables: `EXCEPTIONAL_LARGESIEVE.md`,
`scripts/ls_duality_check.py` (Replay ~3 s, `uv run --with cvxpy --with numpy`).

**Framing.** Thm 2.1 is standard convex duality, not claimed new. The new
step is Fact 1.1 (`w_θ ≤ 1/N`) plus the level count that feeds the large
sieve into KARY2 Thm 5.1. The constants are astronomical (`log W ≈ 10^{10}`),
so everything is asymptotic only. "Any frequencies" means any **rational**
frequencies, by definition.

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
   moduli, forced classes used in any form, multiplicative large sieve
   (Rem 2.5, Gauss sums), weighted sequences with a known `U ≥ Σa²/Σa`
   (Rem 2.4), fibrewise over `Q₀ ≤ N/2` —
   saves `≤ Cλ^{3/4}(log λ)^{3/4}`, `λ = λ(Q₀) + 2λ_Θ` (W-rough levels).
   With polynomial denominators: `≤ C(log N)^{3/4}(log log N)^{3/4}`, and
   `C_B(log N)^{3/4}` for bounded B. No rounding/coefficient-sum term is
   needed, because the large sieve's `N + δ^{−1}` already contains N.
   Status: conditional on KARY2 Thm 5.1 (internal). The 2/3 note is checked
   in the text (Rem 3.4: `Q₀ = L_K ≤ N^{2δ}`, `λ_Θ ≤ ½log N`, ℛ(kℓ)-classes,
   bounded B', hence `C(log N)^{3/4}`). Vaughan 1970 and PW §4 are covered
   only on the 2/3 note's description of them; I did not re-read them.
   Frequencies with `den θ ∤ M₀` are useless (Rem 3.3).
2a. **Prop 2.6 (PROVED).** For prime product systems `F*_1 = S(Q)`:
   Montgomery's sieve is already CRT-optimal.
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
* (E2a) Gallagher as used: needs only support bounds `|𝒜 mod ℓ^v| ≥
  ℓ^v(1−ε)` with `Σ ε log ℓ/ℓ^v ≪ (log N)^{3/4}`, i.e. non-covering of
  fibres. This is the first target; the squares give only `ε ≤ 1/2`.
  (E2b) the optimal kernel bound needs (H_Gal). Open.
* Twisted sequences (`1_A·ψ`) and LS/majorant hybrids are outside the
  definition. Hybrids are sketched only. Neither appears in the literature.
* (E3) non-CRT interval information; (E4) KARY2's inherited exclusions.

## Review status

* Internal self-review: all its defects applied (checkpoint 1).
* Hostile review `reviews/exceptional-largesieve-review.md` (branch
  `side-agent/review-largesieve`): **SOUND**. All of D1–D10 are applied:
  * D1: scope (rational frequencies; twisted/hybrid); the multiplicative
    large sieve, Rem 2.5;
  * D2: weighted sequences via U;
  * D3: the 2/3 note checked, Rem 3.4;
  * D4: W-smooth parts; frequencies reduced to `den | M₀`;
  * D5: enlarged `ℓ₀'`;
  * D6: labels; kernel admissibility defined; ET Lemma 3.8 claim marked
    heuristic;
  * D7: Ex 5.2 is useful only once `N ≳ m³/ω`;
  * D8: (E2) split;
  * D9: Prop 2.6; script docstring and timing fixed;
  * D10: framing and constants caveat.

## For the parent

* Suggested ledger entry: (D)19, the large sieve over forced-class mixtures
  capped at 3/4 (Thm 3.1), PROVED internal. This would supersede the "large
  sieve beyond prime slices" exclusion in (D)18 / KARY2 §6, except for (E1)
  and (E2).
* I did not touch STATUS.md or DISCOVERIES.md.
