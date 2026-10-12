# AGENT REPORT O140 — brainstorm: function-field / polynomial-method / other-rings analogues

Branch `side-agent/bs-function-field`. Memos are in `BRAINSTORM/`, scripts are `scripts/bs_ff_*.py`.
No memo is LIVE, and ES is not solved.

**(a) `BRAINSTORM/ff_erdos_straus.md` — ES over F_q[t]: PARTIAL.** Positivity means monic denominators.
* *Unit numerators.* These degenerate (Prop 1.2, PROVED). In char ≥ 5 three monic unit fractions only
  produce leading coefficients 1, 2 or 3, so "4/P" is impossible for *every* P. The "4 > 3" difficulty
  is archimedean.
* *The faithful analogue.* The numerator is a monic A of degree k ≥ 1. Lemma 1.3 is an exact e-slice
  criterion; it is complete and was cross-checked against brute force.
* *Strongest finding: Theorem 2.1 (PROVED, elementary).* For fixed n the number of P with a solution is
  ≤ 2·64^n·q^{n−k}. So the analogue is FALSE for a proportion → 1 of P as q → ∞. The large-q regime is
  the only one with pointwise function-field technology (Lang–Weil, Katz, Bary-Soroker), and it is
  exactly where the statement fails. The fixed-P solution variety has expected dimension −k. This is B2/B3
  in their sharpest form.
* *Fixed q, n → ∞.* This is the honest analogue (EVIDENCE: q = 5, A = t has no failures at n = 5, 6). It
  is the same divisor lottery as over Z, and RH for curves only supplies the GRH-type input that is
  already known to be insufficient.
* *T1 surprise (EVIDENCE + reciprocity computation).* F_q[t] has no odd-square obstruction: M² has
  Type I and Type II solutions, for q ≡ 1 and q ≡ 3 (mod 4). The reason is that reciprocity's
  infinite-place twist is degree parity, not a residue mod A.
* *Coverings still fail (Prop 4.1, PROVED for linear families).* The class P ≡ 1 cannot be covered, for
  the same size reason as e ≡ −1 ⇒ e > a + b over Z. Function fields therefore do not escape B1 either.

**(b) `BRAINSTORM/polynomial_method.md` — COLLAPSES.**
* *Coppersmith / CHN / Lenstra.* These are upper-bound and enumeration tools with no positive main term.
* *Stepanov-style bounds.* Bounding the complementary classes needs the divisors of one integer to be
  equidistributed mod s. That runs into B4/B3.
* *Chevalley–Warning / Alon's Combinatorial Nullstellensatz / zero-sum methods.* These certify the
  *identity* element (ab⁻¹ ≡ +1), which is signed ES. Positivity needs the specific element −1, which
  requires the ratio set to cover the whole group. Deterministic covering of this kind only gives
  witness moduli ≤ C(log p)². Those moduli are below the PROVED exp(c(log p)^{1/4−}) rate, so this
  collapses to B1.
* *Thue / Minkowski.* These give representation by *some* form only, and the right form is a genus
  condition (B2).

**(c) `BRAINSTORM/other_rings.md` — PARTIAL (sharp reformulation of the crux).**
* *Lemma 3.1 (PROVED).* If e ≡ −n (mod 4) is itself a sum of two positive unit fractions, then ES(n)
  holds with no divisor lottery at all.
* *Prop 3.2 (PROVED).* Over Z[1/3], positive ES holds for every n, because 7 = 27/4 + 1/4.
* *Prop 3.3 (PROVED).* Over every real quadratic O_K with N(ε) = −1, totally positive ES holds for every
  rational n. The construction takes an inert prime ℓ ≡ 3 (mod 4) and a unit η = ε^{2j} with
  η ≡ −1 (mod ℓ). For D = 2, 3 = 1/(6−4√2) + 1/(6+4√2).
* *EVIDENCE for D = 3, 6, 7.* Exact identity checks.
* *Principle (Assessment).* ES is a genuine lottery exactly when the positive cone is discrete at
  infinity (x ≥ 1). This covers ℕ, monic F_q[t] and the Gaussian cone. Units of infinite order in the
  cone act as "universal divisors" (η, 1) of every N, and that makes ES a finite covering mod 4.
  ℕ^× = {1} supplies only (1, 1), which gives the classical n ≡ 3 (mod 4).
* *No transfer to Z.* The Z-substitute for universal divisors is the set of congruence-forced divisors,
  which is B1. At odd squares the step that fails over Z is "e ∈ 1/C + 1/C with e ≡ 3 (mod 4)".

*Caveats for the reviewer.*
* The T1 reasoning in (a) uses ET's Type II chart over F_q[t]. That is gcd algebra, but it was not
  re-derived line by line. The experiments themselves use only Lemma 1.3, which is proved.
* Literature: one search series per angle. No prior F_q[t] ES work was found. Bradford–Ionascu was
  read; the Lenstra/CHN/Olson citations are from memory.
