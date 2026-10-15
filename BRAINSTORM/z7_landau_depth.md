# z7_landau_depth — the Landau depth K(p) and a Dickson-conditional "no bounded family" theorem for U (O231)

## Idea
K(p) := max{K : p + s and sp + 1 are clean ∀ s ≤ K}. On the bounded-min families, U and N₋ are both governed by K(p).
Question: can K(p) be bounded (which would make U provable by finitely many families), or is it unbounded?

## Results (UNFORCED_WORDS §3)
* K(p) < q(p), the least non-residue prime (PROVED, trivial): ψ(p + q) = ψ(q) = −1. So K(p) ≪ p^{1/(4√e)+ε}
  (Burgess). This is the only unconditional upper bound.
* **Thm 3.2 (CONDITIONAL on Dickson).** For every K there are infinitely many primes p ≡ 1 (8) with K(p) ≥ K. At them
  every word with min(t, u, v) ≤ K is forced. So no proof of CONJECTURE U (or ES-five) can use bounded-min words
  only. This is the U-analogue of B2 (redteam-automorphic-2 Thm 2.2) and of SPARKS4 §2.4.
* Numerics: the K histogram to 3·10⁷ (max 10, at p = 21 746 761). The least min of an unforced word is K(p) + 1 at
  most primes (always for K ∈ {2, 3, 6, 7, 9, 10}). The excess is ≤ 9 otherwise.

## Literature
* Dickson's conjecture (Dickson 1904).
* Unconditional analogues for one form: primes p with p − 1 = x² + y² (Linnik 1960, dispersion method) and Iwaniec's
  half-dimensional sieve (Iwaniec, Acta Arith. 21 (1972) 203–234). They give infinitely many p with *one* clean side
  of the needed type. Several simultaneous half-dimensional conditions on shifted primes are open (Assessment).
* Burgess (Proc. LMS 1962) for q(p).

## Barrier screen
This is a barrier result. Hypotheses a U-proof must violate: boundedness of the family. The escape is H-A (a growing
family Θ(p)). T1: squares have K = ∞, consistent.

## Cheap numerics
`scripts/z7_depth.c 9 30000000 3` (all primes ≡ 1 (8) < 3·10⁷; histogram in UNFORCED_WORDS §3).

## Assessment
CONDITIONAL theorem + EVIDENCE. Negative with exact scope. It pins down that U needs unbounded families, exactly as
ES-five does.
