# z44_neutral_odd_mute — odd exponents allowed only where the local symbol is +1 (O276)

## Idea
Lemma 1.1(i) (UNIT_ORBIT_ES): an odd mute exponent w contributes inv_q = ½ iff ((−y/x)/q) = −1. Allow odd exponents
but require ((−y/x)/q) = +1 ("invariant-neutral" odd mutes). This is T1-bearing (Σ inv still ½) but strictly larger
than ES^□. Does it change the mechanism?

## Literature
UNIT_ORBIT_ES Lemma 1.1, Cor 1.2; T1_TEMPLATE Thm 2.1.

## Barrier screen
T1 intact by construction (so no covering, B5). In the modulus-4 shot family (x = (n+e)/4, y = n(r+1)/4) the extra
solutions need r | n + 4W with W = Q^k·(odd-exponent part) and a Legendre condition on −y/x mod each odd-exponent q:
the condition ties q to the certificate (B2 shape: "the modulus is part of the solution").

## Cheap numerics
None run (time); the rung contains ES^□, so pointwise existence at non-squares is already Thm 2.3 — no numerics can
distinguish it (every rung containing ES^□ is solved at every n).

## Assessment
Assessment only: a T1-bearing rung strictly between ES^□ and ES_(1) that is still trivially implied by ES^□; it adds
nothing to provability. Recorded to close the "T1-preserving odd exponent" branch: any ladder that CONTAINS ES^□ is
pointwise-trivial; only rungs inside ES^□ (box, fixed S, cap) can be informative.
