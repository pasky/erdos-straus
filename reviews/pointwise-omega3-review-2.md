# Second hostile review of POINTWISE_OMEGA3.md (branch side-agent/omega-gpair @ bbe13d0)

Reviewer: independent (review-omega3b). Scope: (1) from-scratch re-derivation
of O2 Lemmas 10.1, 10.2, 2.1 and hypothesis checks at every OMEGA3 use site;
(2) adversarial brute-force small systems; (3) the chain H_MIN(θ) ∀θ ⇒ W ≥
(log p)^{1/θ−ε}. Items are written and committed one by one.

## Item 1 — O2 Lemma 10.1 (private covers), re-derived. Verdict: SOUND

* (1) For P ⊆ V(x), a minimal subfamily of occurring events covering P is a
  private cover (a member without a private prime in P could be dropped).
  Distinct P are distinct summands, so `binom(N,u) ≤ G^cov_u`. `|C|≤|P|`
  because private primes are distinct elements of P. The rest is Lemma 1.2
  (checked: Lemma 1.1 Möbius identity, `|R_L| ≤ binom(2N,L) ≤
  4^{L+1}binom(N,L+1)`, the ratio computation `den−num = L²+3L+4t+2`).
* (2) `κ(U,c)≠0` forces every prime of U to be covered by events supported
  in U and occurring on c (pairing `W ↔ W∪{ℓ}`); a minimal such family is a
  private cover of U supported in U, determined by the U-coordinates, so
  `Σ_c |κ|P(c) ≤ 2^{|U|} Σ_{C priv. cover of U} P(C occurs)`. Correct for
  mixed-size events and unions of cells.
* Nothing in the proof uses event sizes or a particular base measure beyond
  independence of coordinates and "event = union of cells on its support".
