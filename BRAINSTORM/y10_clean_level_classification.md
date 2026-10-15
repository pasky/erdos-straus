# y10_clean_level_classification — which levels are clean along a whole polynomial family (O221)

## Idea
R224's T1-type levels (tk + 1 = c² on p = m² + k) via 4A(tQ + 1) = t(2Am + B)² + E, E = 4A − tΔ. Level t is odd-clean
along the whole family Q(m) iff E is a perfect square (NEAR_SQUARE Prop 4.1; "only if" by Chebotarev in ℚ(√−t, √E)).
At a single prime: T1-type ⟺ tp + 1 primitively represented by the principal form x² + ty²; clean ⟺ by some form of
discriminant −4t. Every prime has T1-type levels t = (c² − 1)/(p − m²) for each square root c of 1 mod p − m².

## Literature
Genus theory / representation of integers by binary forms (Cox, *Primes of the form x² + ny²*, §2–3); Schur's theorem on
prime divisors of polynomials.

## Barrier screen
Describes where χ = +1 is forced (anti-certificates); cannot produce χ = −1 words (B2). T1: k = 0 gives every t.

## Cheap numerics
`ns_census.c` (10⁵–10⁶): clean words 432 677, of which T1-type 356 023 (82 %); 0 χ = −1 on either.

## Assessment
PROVED classification (elementary); the 82 % is EVIDENCE that the principal class dominates (small class numbers at
small t: h(−4t) = 1 for t = 1, 2, 3, 4, 7).
