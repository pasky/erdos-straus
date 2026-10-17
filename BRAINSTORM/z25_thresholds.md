# z25 memo 5 — what an amplification law would have to look like (O253)

Verdict: Deliverable-1 theorems (PROVED, AMPLIFY_EXCEPTION §1). Promise n/a (criterion).

* Counting: contradiction iff for every c > 0, limsup F(N) e^{c(log N)^{2/3}}/N = ∞ (published c unspecified);
  strictly stronger than contradicting Σ_{P_E} 1/p < ∞.
* Iterated laws: fixed branching b and outputs ≥ p^{1+ε} give (log N)^{O(1)} — never suffices (σ-closed prime
  models consistent with all known facts). Linear scale: b successors in (p, Ap], in-degree ≤ r suffices iff
  b ≥ rA. Additive: one forced exception in every (p, p + f(p)] suffices iff f = e^{o((log p)^{2/3})} along a
  sequence ((log p)^{3/4} with the internal bound).
* Composites: counted at full weight by Vaughan; from one seed they are powers of p₀ or force new exceptional
  primes; composite → prime conversion loses a log.
* Disjunctive blocks: hitting-set number ≥ #blocks/max multiplicity.
So a sufficient law must force exceptions that are *dense at their own scale* — the opposite of the isolated
exceptions seen in every numerator model (memo 3).
