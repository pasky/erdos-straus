# s5_gcd_sides — the sign of a word is the ψ-parity of the common part of two side numbers (own idea, O230)

## Idea
Following s5_three_sides, look at how the side numbers interact rather than at one side at a time.

## Lemma G (PROVED, one line)
For a word (t, u, v) of X_p:
* gcd(tp + 1, p + u) = A;
* gcd(tp + 1, p + v) = B;
* gcd(p + u, p + v) = gcd(Av, Bu).

*Proof.* gcd(tp + 1, p + u) = gcd(tp + 1 − t(p + u), p + u) = gcd(1 − tu, p + u) = gcd(A, p + u) = A, since A | p + u. ∎

So χ(w) = ψ(gcd(N_t, N_u)). Conversely, every pair (t, u) with tu − 1 | p + u is a word. **ES-five(p) ⟺ ∃ t, u ≥ 1:
gcd(tp + 1, p + u) = tu − 1 and that gcd is ψ-odd** (p ≡ 1 mod 4).

## Reading: a two-moving-modulus problem
* N_t ranges over the progression {tp + 1} with step p, and N_u over {p + u} with step 1. A word is a coincidence
  "the gcd of the t-th term of one progression and the u-th term of the other is exactly tu − 1".
* The identity behind it is (tp + 1) − t(p + u) = −A.
* This is the integer-lattice form of the (J)40 Ptolemy relation through the vertex A.

## Barrier screen
* B2: the modulus tu − 1 is part of the solution, in its purest form.
* T1 (p = m²): ψ ≡ 1, so every gcd is ψ-even.
* B4: a gcd-coincidence across two growing families is joint factorisation (hatch H-A). Here it is exactly ES, so
  nothing has been gained.

## Cheap numerics
`scripts/s5_gcd_check.py` checks Lemma G and the equivalence on all words of primes p ≡ 1 (4), p < 1500 (5 464 words, 0 violations; every such prime has a ψ-odd gcd).

## Assessment
PROVED, a dictionary only. It is a clean way to state the joint-factorisation hatch H-A for ES: the sign lives in the
gcd of two side numbers, and each side's total ψ-parity is known ((N_t/p) = 1, (N_u/p) = (u/p)). No forcing follows.
**H-A in this form needs a mechanism making gcd(tp + 1, p + u) large and ψ-odd simultaneously. No such mechanism is
known.**
