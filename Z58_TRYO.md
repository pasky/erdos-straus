# Z58_TRYO — tryhard lane O on (★): 4uBC − u − B = p

Status: WORK IN PROGRESS (first commit). No proof of the full statement.

## §0 Falsifier ledger (stated at first commit; re-stated at the end)

Attack chosen: (A) reduce (★) to "∃ u, B ≥ 1 with 4uB | p + u + B" and to a *character-kernel criterion*
(failure ⟺ for every u an odd character mod 4u kills every prime factor of p + u); (B) try to cover the
primes p ∈ 𝔐 by "one non-residue prime q" identities (least-quadratic-non-residue route); (C) prove the strongest
honest weaker statement (almost all primes) by a large sieve on shifted primes.

* (F1) odd squares n = m². In (A) the witness character for n = m² is ψ_u = (−4u/·) for every u; for primes the
  Legendre identity (q/p) = (−4u/q) on q | p+u holds but ψ_u is a character mod 4up, not mod 4u, so it is no
  witness. In (C) the sieve step "p ≡ −u (mod q) for a positive proportion 1/(q−1) of primes p" is where primality
  enters; for n = m² the class −u mod q (q ≡ −1 mod 4u) is a non-square, so the sieve removes NOTHING and gives
  no bound — consistent.
* (F2) C-even only. (C) proves an almost-all statement; restricted to C even it is still an almost-all statement
  (true, consistent with 12 exceptions in [10^10, 1.1·10^10]). No claim about every p is made from C-even data.
* (F3) 285 composites: (C) is a statement about primes only (density); nothing proved about individual n.
* (F4) 14 prime zeros up to 8 813 281: route (B) is KILLED by them (see §3): for every prime q ∈ [5, 47] some (★)-zero
  p is a non-residue mod q, so no finite family of congruence identities covers "p non-residue mod q".
  (C) asserts nothing for individual p — consistent.

Verdict so far: no HOT LEAD.
