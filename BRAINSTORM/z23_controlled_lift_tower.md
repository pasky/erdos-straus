# z23 — controlled lifts g → gu, u ≡ 1 (mod 4h): ES propagates only downwards (O251)

## Idea
Make composition respect the slice divisibility: h | (gu+1)/4 ⟺ u ≡ 1 (mod 4h). Then all old lines k | h survive at gu,
and d_k(gu) ≡ d_k(g) (mod g). Hope: lift a near-miss at g into a hit at gu.
## Literature
LATTICE_MEETING §2.2; Dirichlet composition (Cox, *Primes of the form x² + ny²*, §3); moving-modulus hatch H-A.
## Barrier screen
Since an ES value d ≤ k < g, ES via (k, d) at gu forces ES via (k, d) at g: the controlled lifts carrying ES via (k, d) stay in the
congruence-filtered divisor set of N_{k,d} = 4k²p + d (plus u ≡ 1 mod 4h), and lifting never creates ES on an old line. New lines k′ | (gu+1)/4, k′ ∤ h, are a fresh
B2 event. B6: averaging over u says nothing at fixed p.
## Cheap numerics
None needed beyond z23_alld (the downward implication is a two-line proof). (Spot check: p = 13, g = 7, k = 2, d = 2:
lifts gu with u ≡ 1 (mod 8) carry ES iff gu | 4·4·13 + 2 = 210 — none, since 7u | 210 forces u | 30.)
## Assessment
PROVED (negative). Spark: an *upward* forcing would need u chosen so that gu | 4k²p + d — i.e. choosing u as a divisor of a
prescribed integer: the slice moves only inside one integer's divisor set. Dead for this hatch.
