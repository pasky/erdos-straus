# z25 memo 4 — is p ∈ E ⟹ p² ∈ E? (O253)

Verdict: OPEN, 4-specific, low value (Prop 3.4). Promise 1/5.

* W(p²) = p·W(p) ∪ {mixed solutions, valuation pattern (2,1,0)} (ET Prop 1.6 removes Type I/II of p²).
* Mixed solutions come from m ≡ 3 (4), z = (p² + m)/4, A, B′ | z, A + pB′ ≡ 0 (mod m): divisor events of the
  quadratic numbers (p² + m)/4. Reciprocity kills m = 3 for p ≡ 1 (3) (all ℓ | p² + 3 have ℓ ≡ 1 (3)), the same
  mechanism as Mordell's identities — so small m are dead and the rest is a B2 lottery.
* In k = 8 the law is false (8/121 = 1/18 + 1/99 + 1/2178). Even if true for k = 4 it gives only {p₀^k}, log N.
Spark: the m-reciprocity filter for (p² + m)/4 is a clean analogue of Mordell's classes for p²; a "Mordell
theorem for squares of primes" (which m are dead for p ∈ 𝓜) is a small, checkable side question.
