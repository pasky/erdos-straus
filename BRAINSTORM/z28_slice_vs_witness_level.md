# z28_slice_vs_witness_level — which lifts escape the T1 adversary (O257; NONCONG_LIFTS §1)

**Idea.** Classify lifts "source witness w′ at q ↦ witness at p" by the information about p they use. A lift that is
congruence-mediated of level M(w′) and valid for every prime in the class of p mod M forces k a b | M and p ≢ □ (mod M).
If M depends only on the slice σ(w′) (bounded), O253 Cor 3.3 applies; the only escape is a level that grows with the
*size* d′ of the source solution (witness-level), whose validity is then a divisor event of N_θ(p) with modulus built
from d′ — B2. Polynomial lifts (output polynomial in p on a class) are Schinzel identities and collapse to slice
level; archimedean lifts (polynomials in ⌊√p⌋) have a ℚ(√j)-adic T1 adversary (NEAR_SQUARE Thm 3.4).
**Literature.** Mordell 1969 / Schinzel, Funct. Approx. 28 (2000) (no polynomial identity on a square class); ET
arXiv:1107.1010 Prop 1.6 and p. 8; campaign T1 = DISCOVERIES (C)2/(C)7; O253 Thm 3.1–Cor 3.3.
**Barrier screen.** B1: slice-level and polynomial lifts are B1 objects (PROVED collapse). B2: witness-level lifts are
B2 by construction. T1: Thm 1.2(ii) is T1 in local form (classical). B5/B6: n/a. (J)41: all statements hold for every
4 | k (full T1), so the dichotomy is numerator-blind — the escape it isolates is not 4-specific.
**Cheap numerics.** Consistency asserted in `scripts/z28_matched.py`: every determined lift found (20 365 at Mordell
primes ≤ 10⁵) is visible; none contradicts Thm 1.2.
**Assessment.** PROVED (Thm 1.2 elementary + classical T1; Prop 1.3 cites Schinzel). A precise map, not a route:
"non-congruential" = "the level grows with the size of the source solution" = B2.
