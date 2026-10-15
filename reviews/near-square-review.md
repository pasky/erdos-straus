# R225 — hostile review of O221 (NEAR_SQUARE.md, checkpoint 1)

Reviewer: R225 side agent (branch side-agent/review-near-square, merged side-agent/near-square at review start).
From-scratch scripts: `scripts/review_r225_*.py`. ES is not solved; nothing below changes that.

## Verdict summary (filled in claim by claim)

| claim | verdict |
|---|---|
| Lemma 1.1 (Type I witness (−4d/n) = −1) | SOUND |
| Lemma 1.3 (Type II witness (f/n) = −1; (de/n) under gcd) | SOUND |
| Prop 1.4 (Hecke reading) | SOUND-AFTER-REPAIRS (minor: the "does not factor through N(π)" clause is unproved) |

## Claim-by-claim

### Lemmas 1.1, 1.3 (witness dictionary)
Re-derived independently.
* 1.1: ef = 4a²d + 1 ⇒ f odd, every q | f has q ∤ 2ad and (2a)²d ≡ −1, so −d ≡ (2a)⁻² is a square mod q:
  Jacobi (−d/f) = 1. The Kronecker symbol χ = (−4d/·) is a character mod 4d (−4d ≡ 0 mod 4) with χ(−1) = −1 and
  χ(f) = (−d/f) for odd f > 0. 4acd = n + f ⇒ f ≡ −n (mod 4d) ⇒ 1 = χ(f) = −χ(n). No gcd hypothesis needed
  (gcd(n, d) = 1 follows since f is prime to d). Correct.
* 1.3: (2.21) ⇒ −dn ≡ (2c)⁻² mod every q | f, so (−dn/f) = 1; f = 4acd − 1 ≡ −1 (mod 4d) ⇒ (−d/f) = χ(−1) = −1 ⇒
  (n/f) = −1 = (f/n) by reciprocity (n ≡ 1 mod 4, both odd positive). The (de/n) clause: ef ≡ 4a²d (mod n), and
  gcd(e, n) = 1 follows from gcd(n, 2ad) = 1. Correct; the n = 21 counterexample to the unconditional form checks.
* From scratch (`scripts/review_r225_witness.py 400`): enumerates ALL N-points of Σᴵ_n (all odd n < 400) and Σᴵᴵ_n
  (n ≡ 1 mod 4, n < 400) in BOTH orientations (a ≤ b by enumeration with acd ≤ n, a > b via ET's reflections):
  8 501 Type I and 1 034 Type II points, 0 failures of (−4d/n) = −1, (f/n) = −1, (de/n) = −1 [gcd case]. Odd
  squares produce no points (consistent with ET Prop 1.6).

### Prop 1.4
The identity (D(m)/n) = (D(−√−k)/π)_K is immediate (ℤ[√−k]/(π) ≅ ℤ/n because N(π) = n is prime, so the
non-maximality of ℤ[√−k] is harmless; denominators of D must be prime to n — implicit). The second sentence
("if D(−√−k) ∉ ℚ·K^{×2} it … does **not** factor through N(π) = n") is asserted, not proved: the symbol is a
Hecke character of K that is not of the form ψ∘N on *all* ideals, but the claim concerns its restriction to the
thin set of principal primes (m + √−k), m in a class, and "does not factor through n" on that set needs a
Chebotarev-type argument (e.g. in K(√α, √q₁, …)) for primes of the special shape m² + k — which is a
Bunyakovsky-type statement. Not used anywhere downstream (Thm 2.2 proves the algebraic statement; Thm 3.4 needs no
escape hypothesis), so MINOR.
