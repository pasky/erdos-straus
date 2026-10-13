# Windmills beyond finite menus: reduction theory, genus theory, Legendre-type parity (O164)

**Status: ES is not solved here.** Labels as in DISCOVERIES.md. Scripts `scripts/wr_*`.
Brief: `/tmp/es-briefs/full_t164.txt` (SPARK phase, CONSTRUCT). Predecessors: INVOLUTION_ES.md, INVOLUTION_ES2.md,
WINDMILL.md, BRAINSTORM/invol_*.md, DISCOVERIES (J)2.

## 1. Zagier's windmill is the dihedral symmetry of Conway rivers (dictionary)

Notation. For a non-square discriminant D > 0 let `Y(D) = {[a,b,c] ∈ ℤ³ : a > 0 > c, b² − 4ac = D}` (Conway's
*simple* forms, i.e. the edges of the topograph separating a positive from a negative value, with an orientation).
Zagier's set `X(p) = {(x,y,z) ∈ ℤ³_{>0} : x² + 4yz = p}` is identified with `{φ ∈ Y(p) : b > 0}` via
`(x,y,z) ↦ φ = [y, x, −z]`. The river step is the 2-piece map
`R[a,b,c] = [a+b+c, b+2c, c]` if `a+b+c > 0`, else `[a, b+2a, a+b+c]` (walk one edge along the river; `a+b+c ≠ 0`
since D is not a square). σ = swap `y ↔ z` (= `[a,b,c] ↦ [−c,b,−a]`), ζ = Zagier's 3-piece windmill.

**Observation 1.1 (algebra, PROVED by direct substitution).** Each piece of ζ is `φ ↦ −φ∘g` for an explicit
`g ∈ GL₂(ℤ)`; e.g. on `x < y − z`, `ζ(φ) = −φ∘g` with basis `(e₂, e₂ − e₁)`. Likewise `σ(φ) = −φ∘(e₂, e₁)`.
So ζ and σ map a form to an equivalent form of its *negative*; they never leave the topograph of φ up to sign.

**Computation 1.2 (CERTIFIED for all primes p ≡ 1 (4), p ≤ 1300; `scripts/wr_zagier_river.py 1300`).**
(i) The R-orbits on `Y(p)` are exactly the rivers (one per narrow class; `#orbits = h⁺(p)`), with period `L_C`.
(ii) The rotation `ζ∘σ` on `X(p)` has exactly `h⁺(p)` cycles, in bijection with the classes, of lengths `L_C/2`.
(iii) ζ maps the cycle of class C onto the cycle of the class `C⁻¹`; only the principal class is self-paired
(p prime, so h⁺(p) is odd and the principal class is the only ambiguous one).
Example p = 1297: h⁺ = 11, river lengths `[22,22,22,22,26,26,34,34,42,42,74]`, ζσ-cycles `[11,…,37]`.

**Reading (dictionary; PROVED given 1.2's structure, elementary).** ζ and σ both conjugate the rotation ρ = ζσ to
its inverse (`σρσ = σζ = ρ⁻¹`, same for ζ). Hence on each ρ-cycle they act as reflections of a polygon, or swap
two cycles. Paired classes `C ≠ C⁻¹` are swapped (no fixed points). The principal cycle has odd length
`L_1/2` (because `|X(p)| = Σ_C L_C/2` and the non-principal terms pair up), so each of ζ, σ has exactly **one**
fixed point on it. ζ's is the principal form `[1,1,−(p−1)/4]`; σ's is `[a,b,−a]`, i.e. `p = b² + 4a²`.
So Zagier's proof is the statement *"the principal river has odd half-period, and the reflection σ of an odd
polygon has a fixed vertex"* — this is H. J. S. Smith's (1855) palindromic-continuant proof and Legendre's
period-parity argument in topograph language. (I make no claim of novelty for this dictionary; it is the
folklore "Zagier = reduction" observation, here checked mechanically.)

**Consequence for the ES programme.** The windmill mechanism has three ingredients:
(W1) a finite set carrying a "rotation" whose cycles are classes (reduction cycles / rivers);
(W2) an involution pairing a class with its inverse, so that only **ambiguous** classes contribute fixed points;
(W3) an anchor that makes one ambiguous cycle odd (here: the principal form, the ζ-fixed point).
The fixed points of reflections of ambiguous cycles are *ambiguous / symmetric forms*: `[a,b,−a]`
(sums of two squares) or `a | b` (factorisations of D; Gauss: `#ambiguous classes = 2^{μ−1}`).
The ES question becomes: find D (built from p and a parameter) and a reflection whose fixed points on a
forced-odd cycle are ES certificates. §2 onwards.
