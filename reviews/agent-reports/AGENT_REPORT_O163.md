# AGENT_REPORT_O163 — (x,y,z)-families in the binary-form obstruction (closes R159 D6)

Branch `side-agent/binaryform-xyz`. Deliverable: POINTWISE_BINARYFORM.md §8 "(O163)", plus pointer
lines in §0, §4.4(iv), §7 marked "(O163 update)". Scripts `scripts/bf2_*.py`, data `data/bf2/`.
ES is not solved; nothing here proves any case of it.

## Result (PROVED; Cor relative to Hecke exactly as Cor 3.4)
**Theorem 3.2′.** Let (x,y,z) ∈ Q[u,v]³ with 4/Q = 1/x + 1/y + 1/z identically (Q primitive positive
definite), M divisible by 8, 2D and the denominators δ (of x, y, z and of the polynomial quotients by
Q). If the family is integral on a square class C mod M, then no open cone of directions has all
three top forms positive. Hence valid points in square classes lie near finitely many directions.
**Cor 3.4′.** Finite sets of (x,y,z)-families (polynomial or rational) miss almost all primes of every
square class mod the joint modulus. No extra hypothesis compared to Thm 3.2 / Cor 3.4. So D6 is
closed in full: there is no residual case.

## Proof structure
* Lemma 8.1: shapes. Q is prime in Q[u,v]. The cases are Q | all three (never valid when
  gcd(Q(P), δ) = 1), Type I shape, or Type II shape.
* Lemma 8.2 (identities at the origin). For Type I shape, 4x̃ − 1 = Qh, so x̃(0) = 1/4,
  ord₀ y = ord₀ z = k, and z_k = −y_k when k ≥ 1. For Type II shape, if x(0) = 0 then ỹ(0) = z̃(0) = 0.
* Lemma 8.3 (pointwise descent, n = λ²w², λ an odd prime). If λ ∥ y, z, descend by λ. This gives a
  Type I/II solution for the NON-square λw². ET Prop 2.2/2.6 + Lemma 1.1 then force a Legendre
  symbol mod λ to be −1. If λ² | y, z, descend by λ² to the square w² and apply ET Prop 1.6.
* Lemma 8.4 (sieve). For a prime λ in the forced class mod M, there are square points λX ∈ C ∩ S,
  arbitrarily far out, with gcd(w, G(λX)) = 1 and λ ∤ w·H(X). Ingredients: Lemma 2.1, a
  parametrisation of Q = w² through an auxiliary point with w₀ prime to M·w₁, Dirichlet, and an
  elementary Ekedahl-type coprimality sieve, with all local densities checked positive.
* Theorem: the cases k = 0, k = 1 and k ≥ 2. For k = 1, Lemma 8.2 makes the forced symbol +1
  (Type I: −x̃y′z′ ≡ (y₁(X)/2)²; Type II: 1 − 4ỹ ≡ 1 mod λ), which is a contradiction.

Key point for the reviewer: R159's suggested route ("square points with gcd(Q(P), y(P)z(P)) = 1") is
**false as stated** whenever y(0,0) = 0. In that case gcd(u,v) divides both numbers. And 50–75% of the
square classes contain no primitive square point (bf2_sieve_check). The λ-descent + origin identities
is what closes this case.

## Checks
* `bf2_pointwise_check.py`: Lemma 8.3, all solutions for n = λ²w² ≤ 12 000. The hypotheses of (a)
  hold 1 612 times and those of (b) 688 times. The symbol is always −1. Cases (c), (d), (e) never
  occur. 0 violations.
* `bf2_sieve_check.py`: Lemma 8.4 existence for 4 forms, M ∈ {8,16,24,40}, every (square class,
  octant) pair, using G with G(0) = 0. 0 of 5 568 pairs missing. The first pass missed 411 pairs, a
  box effect that disappeared with a larger box.
* `bf2_origin_check.py`: the Lemma 8.2 algebra on formal power series and on composed families. This
  is a sanity check only, because no genuinely two-variable family with k ≥ 1 is known.
* `bf2_square_patterns.py`: gcd patterns of the n | x solutions for odd squares. One-sided
  coprimality (gcd(n,y) = 1 only) is common, so both-sided coprimality or the descent is needed.

## Points I'd like the hostile review to hit
1. Lemma 8.4 Steps 3–7. The claim that primes of k₀ divide 2Dw₀ and that w₀ | k₀; the local factors
   at ℓ | k₀, ℓ ∤ M; and the ℓ > T tail (the split point should be C·T with C ≥ box side; minor).
2. Lemma 8.3(b): reciprocity sign with F ≡ 3 (mod 4).
3. Whether "M divisible by δ" (denominators of the quotients by Q) is the right modulus hypothesis.
Labels: Lemmas 8.1–8.4 and Thm 3.2′ are PROVED. Cor 3.4′ is PROVED relative to Hecke. Novelty is
folklore-level.
