# y8_three_squares_sq — an exception-free SQ for all odd n: "every path lattice embeds in ℤ³ ⟺ n is a square" (O217)

## Idea
SQ₅ (CONJECTURE, (J)13/(J)15) has the exception 105 and lives on n ≡ 1 (4). Replace "χ(w) = −1" by the condition
TWO_FIBRES Thm A makes natural for composite n: **w is ℤ³-embeddable** (n·G_w is a Gram matrix of three integer
vectors) ⟺ Diff(T_w) = {2} ⟺ (−A/ℓ) = +1 for every odd prime ℓ with v_ℓ(n) odd.

**CONJECTURE 3SQ.** For odd n ≥ 1: every word of X_n is ℤ³-embeddable ⟺ n is a perfect square.
* ⇐ is TWO_FIBRES Thm B (PROVED). For n = p prime, 3SQ(p) ⟺ ES-five(p) (Thm A). For n ≡ 3 (4) it is trivial:
  (n + 2, 1, 1) has A = n + 1, and some ℓ ≡ 3 (4) has odd exponent with (−A/ℓ) = (−1/ℓ) = −1. More generally
  (PROVED) the word (1, 2, n + 2) (A = 1) is non-embeddable whenever an odd-exponent prime of n is ≡ 3 (mod 4).
* 105 is NOT an exception: its 11 words all have χ = +1 but every one is ramified at two odd primes ({3,7} or
  {5,7}), so none embeds. SQ₅'s lone exception is an artefact of measuring the product of the local signs
  instead of the signs themselves.

## Literature
Lorenzini (arXiv:2311.06367, Ex. 6.2(a)) for the A₃ exceptional list; Eichler/O'Meara §91 for maximal lattices;
campaign: HJ_DEEP (J)15, TWO_FIBRES Thm A/B, DIFF_DEEP (J)13.

## Barrier screen
T1: built in (⇐ is Thm B). B2: at primes it IS ES-five, so it inherits the full lottery; for composite n it is a
union over the odd-exponent primes ℓ of divisor-in-class events, so strictly easier. B1: after the elementary words (A = 1 kills odd-exponent primes ≡ 3 (4); A = 2, i.e. (1, 3, (n+3)/2), kills
≡ 5 (8)), what remains is n all of whose odd-exponent primes are ≡ 1 (8) — possibly several (R-O217: no reduction
to a single prime ℓ is proved); Mordell-type congruence data
cannot cover it (same as ES). Not a route to ES, but the correct exception-free formulation of SQ on all odd n.

## Cheap numerics (`scripts/y8_embed_sq.c`)
All odd n ≤ 10⁶: **0 non-squares with every word embeddable; 0 squares with a non-embeddable word.**
(105: 11 words, all non-embeddable; 525 = 3·5²·7: 23 of 27 non-embeddable.)

## Assessment
CONJECTURE (EVIDENCE to 10⁶, exception-free) + PROVED pieces. SHARP (formulation): SQ in its three-squares form has
no exceptions; it equals ES-five at primes and T1 at squares.
