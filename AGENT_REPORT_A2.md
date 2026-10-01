# AGENT_REPORT_A2 — exceptional-set exponent beyond 3/4 (task a2)

Branch: `side-agent/theta-beyond-34`. Main deliverable: `EXCEPTIONAL_THETA.md`.

## Outcome

**(B): an obstruction map. There is no θ > 3/4.**

The core is a new rigorous "sieve-limit" theorem. It converts the
mass-and-budget heuristic of the 3/4 note's ceiling section, `θ = B/(B+1)`,
into a proved statement for a precisely scoped class of architectures. It
also makes rigorous, for avoid-events of product systems, the LP-duality
statement that notes Assessment 75.7 called missing.

Labels: PROVED means internal proof only, with novelty unchecked. It may be
folklore in spirit; no source was found.

## Main results

### Theorem 2.5 (sieve limit for prime-slice CRT systems; PROVED)

Setting: conditions are independent across large primes ℓ once a small
residue c is fixed. Let ν be any nonnegative majorant of the avoider set,
built from congruence classes whose slice primes have total log at most λ.
Then

    log(1/Eν) ≤ log(Q₀/|R|) + 19αλ + C₄ Σ_ℓ p̄_ℓ ℓ^{−α} + O(log²λ)   for every α > 0.

The proof has three parts:
1. **Thinning:** `x = u∘w`.
2. **Band symmetrisation:** this reduces f to a polynomial in band counts,
   with multidegree in a weighted lower set.
3. **Interpolation:** the combination technique on lower sets, plus a
   binomial Lagrange-node lemma. The node lemma comes with explicit
   constants and is checked numerically.

### Theorem 2.7 (sequential windows; PROVED)

This extends Theorem 2.5 to systems where large primes are shared between
the multiplier parts of some conditions and the slice primes of others. It
needs only that each condition has a unique prime in its last window.

### Corollaries 3.4 and 3.6 (PROVED)

Consider any family of Case-B forced classes, in either grouping
(multiplier classes −4D mod M, or a-frame classes −(4D+a) mod 4a·g(D)).
Suppose every modulus has a dominant prime `P(M) ≥ M^{1/(1+C)}` for some
C < 1. Then:
* every level-`N^A` majorant (Bonferroni, Brun, Selberg, anything) saves at
  most `C(A,C)(log N)^{3/4}`;
* so does the Montgomery large sieve.

So **3/4 is sharp and no `(log log N)^ε` gain is possible** in this class.
The class contains Vaughan, PW, the 2/3-loglog note and the 3/4 note. The
profile input is Lemma 3.1, `Σ τ(A²)M/φ(M) ≪ x log²x`, proved via Shiu.

### Exact accounting (Lemmas 4.1–4.4; PROVED)

* In both campaign proofs the binding inequality is the pair
  (supply profile, level).
* Bonferroni depth (`r ≥ μ−2√μ` is forced), the BV level (EH changes
  constants only) and the selector are not binding.
* The 2/3-loglog note is sharp for its architecture: `h(𝒦) ≪ log log L_𝒦`
  with `L_𝒦 ≤ N` (Cor 3.5).

### Levers (table in §5.0)

* **Closed:** cost per condition / mass weighting; beyond-identity supply
  (the exact criterion `−1∈Rat_a` *is* the a-frame forced-class family,
  Lemma 3.2); both Case-B groupings; Bonferroni→Selberg; the ET first
  moment (consistent with B = 3).
* **Case A:** closed only conditionally, on the weighted divisor bound
  **H_A3**. Its unweighted form is numerically supported, but not proved.
* **Halász / multiplicative:** a non-multiplicativity counterexample is
  PROVED. The joint route is a model Assessment only (entropy θ* ≈ 0.52).
  It is *not* closed.
* **Open door:** H_MS for **balanced moduli** (no dominant prime, about 31%
  of supply), and multipliers far beyond the slice prime. A concrete next
  step is in §5.6: the same-scale pair-condition toy LP.

## Evidence (numerical, labelled)

* **H_EM, complete-system void among real primes.** Tested on all
  4,045,501,204 primes in `[10¹², 10¹²+1.12·10¹¹)`. The ratio
  `−log P(void)/mass` falls from 1.39 to about 0.80 for Q ≤ 4000. There is
  no super-cubic effective mass; the classes clump.
* **Exchangeable LP.** In the tested cases, the floating-point LP optimum
  agrees with the Selberg square-majorant value to within 0.01 in −log.
  This is uncertified.
* **Reduction steps of Prop 2.4.** Brute-force LP on 40 random
  non-exchangeable instances; 0 violations.
* **Node lemma.** 99 cases; 0 violations.

## Self-review

A deep reviewer subagent ran on the first draft (verdict: "substantial
repairs needed"). All findings were applied:
* nonempty-fibre hypothesis added to Thm 2.5;
* the R-term made explicit as an uncontrolled saving;
* the universal two-sided Ψ claim removed (Ψ is one-sided in general);
* Cor 3.4 restricted to slice-only conditions with a selector admissible
  set;
* coprimality added to the Lemma 3.2 converse (counterexample p=5, q=15,
  D=25);
* Case A made conditional on a *weighted* H_A3;
* Halász downgraded to Assessment;
* the false lcm lower bound deleted;
* `log⁺` added in Lemma 4.1;
* the Christoffel wording corrected (square majorants only; counterexample
  `(k−1)(k−2)/2` for Poisson(1/2));
* the script issues fixed.

Theorem 2.7 and Cor 3.6 were added *after* that review. They need a fresh
hostile check: the induction in §2.6, Lemma 2.8, and the per-window
summation in Cor 3.6.

## Files

* `EXCEPTIONAL_THETA.md`
* `scripts/theta_sieve_limit.py`
* `scripts/theta_reduction_check.py`
* `scripts/theta_profile.py`
* `scripts/theta_void_primes.cpp`
* `data/theta/{profile.txt, void_primes_Q4000.txt}`
* Replay commands: §7 of the md.

Nothing was touched in `main`, `notes.md` or the sibling repos. No ledger
edits were made; suggested `DISCOVERIES.md` entries are for the parent to
decide:
* (D) new: Thm 2.5, Thm 2.7, Cor 3.4/3.6 (walls with exact scope);
* (E) new: H_MS, H_A3, H_EM.

Stopping here for parent review.
