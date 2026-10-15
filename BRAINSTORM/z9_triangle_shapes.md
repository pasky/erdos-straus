# z9_triangle_shapes — the other near-orthogonal shape (cyclic plumbings) in 𝔊⁻_p is a decoupled lottery (O233)

## Idea
Path classes are the near-orthogonal classes with off-diagonal pattern (−1, 0, −1) (CONSTRUCTIVE_ES 5.3). A positive ternary class
with all |off-diagonals| ≤ 1 and determinant p has, up to trivial cases, exactly one more shape: the **triangle** (cyclic
plumbing) Gram [[a, e, e], [e, b, e], [e, e, c]], e = ±1, with det abc − a − b − c ± 2 = p. Construction attempt for a global
mechanism: widen the target from "path class" to "near-orthogonal class" and look for a link triangle ⟹ path (a basis change
or a 2-isogeny step). If such a link existed, triangle existence (a different divisor problem: (ab − 1)c = p + a + b ∓ 2)
would feed ES-five.

## Literature
Neumann's plumbing calculus (cyclic plumbings bound torus bundles; linear plumbings bound lens spaces, the CONSTRUCTIVE_ES §4
reading of words); Conway–Sloane, *Low-dimensional lattices VI* (Voronoi/Selling reduction, obtuse superbases: a
triangle Gram is a superbase with conorms 1, 1, 1 and three others).

## Barrier screen
A triangle word gives (ab − 1)(ac − 1) = ap + (a + 1)² (sign −), not the tp + 1 = AA* structure. So no five-slice
identity and no Fano pigeonhole attach to it, and a χ = −1 triangle class certifies only if it is also a path class.
B2: triangle existence is again "p + a + b ∓ 2 has a divisor ≡ −1 mod a, with modulus part of the solution". T1: at m²
there is no 𝔊⁻.

## Cheap numerics (EVIDENCE; `scripts/z9_triangle.py 5 5000`)
All 329 primes p ≡ 1 (4), 5 ≤ p ≤ 5000:
* 327 have a χ = −1 triangle class; the two exceptions (109, 229) have none at all.
* At 312 some triangle class is not a path class.
* At **47 primes the χ = −1 triangle classes exist but none is a path class** (first ones: 61, 181, 349, 421, 541).
So the triangle shape and the path shape are decoupled. Widening the target to "near-orthogonal" adds a separate lottery
that does not certify ES.

## Assessment
Negative. The only certificate shape is the path. Its near-orthogonal sibling is neither forced by it nor forces it at the level of classes (this rules out same-class conversion, not every conceivable triangle → path mechanism).
Promise 0/5.
