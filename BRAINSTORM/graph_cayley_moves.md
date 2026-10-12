# BRAINSTORM — moves on the ES solution set: the Cayley cubic, chord–tangent dynamics, and why no move reaches primes (O150, angle a)

Labels as in DISCOVERIES.md. Scripts: `scripts/bs_graph_cayley.py` (integer chords and tangents between ES points).

## 1. Idea

Let S = {(n,x,y,z) ∈ ℕ⁴ : 4/n = 1/x + 1/y + 1/z}. Put `X = (X₀,X₁,X₂,X₃) = (−n, 4x, 4y, 4z)`. Then
`Σ 1/Xᵢ = 0`, i.e. `σ₃(X) = 0`, which is Cayley's 4-nodal cubic surface 𝒞 ⊂ ℙ³. So S is the set of integral
points of the affine cone over 𝒞 in one sign region with a level-4 condition (folklore: ET Remark 2.10, BL §2.1,
LITERATURE_2026 row "Cayley cubic"). For a prime p:

**Lemma A.0 (PROVED, elementary).** ES(p) ⟺ some primitive integral point of 𝒞 has sign type (−,+,+,+),
`X₀ = −p`, and `X₁ ≡ X₂ ≡ X₃ ≡ 0 (mod 4)`. Representations `1/p = 1/X₁+1/X₂+1/X₃` with no level condition
always exist (`(2p,3p,6p)`), so all of ES is the level-4 condition.
*Proof.* A solution gives the point `(−p,4x,4y,4z)/g`, where g divides p. If g = p, then p | x, y, z, so
`4 = 1/x′+1/y′+1/z′`, which is impossible. Hence g = 1. The converse is immediate. ∎

The "dynamical" idea: find a set 𝓜 of moves (maps or correspondences on S, or on 𝒞(ℚ)) with
1. ES-admissibility preserved (positivity and level 4), and
2. the n-coordinate not merely multiplied, so that primes can be reached.

Then ask whether the orbit of a finite seed set hits every prime (connectivity/expansion). To prove ES, a move
system would have to satisfy (1), (2) and a reachability statement independent of ES itself.

## 2. Literature anchor

* The Cayley cubic, its 9 lines and the universal torsor `Xᵢ = ε y_j y_k y_l z_ij z_ik z_il` are in Heath-Brown,
  "The density of rational points on Cayley's cubic surface" (2003), Lemma 1, with N(B) ≍ B(log B)⁶. ET Type I/II
  are torsor coordinates (ET Remark 2.10). Both are checked in the campaign's LITERATURE_2026 and
  LITERATURE_AUTOMORPHIC.
* The chord–tangent ("secant/tangent", Segre–Manin) process on cubic surfaces: Manin, *Cubic Forms*, Ch. II.
  Siksek, "On the number of Mordell–Weil generators for cubic surfaces", J. Number Theory 132 (2012), shows that
  one point generates X(ℚ) for smooth cubic surfaces with a rational skew pair of lines. From memory, unverified;
  𝒞 is singular, so it does not apply literally.
* Bir(𝒞) ≅ Bir(ℙ²) (the Cremona group) via `Xᵢ ↦ 1/Xᵢ`, which maps 𝒞 birationally to the plane `Σuᵢ = 0`.
  This is classical.

## 3. The four classes of moves, and what each one does

**(M1) Scaling / Hecke multiplication.** `(n,x,y,z) ↦ (kn,kx,ky,kz)`, together with the Hecke-type translations
of POINTWISE_SPECTRAL Lemma 2.2. These move along the divisibility order, so they never reach a prime from a
smaller n.

**(M2) Parameter translations in ET's coordinates.** Type II: `p = (4abcd − a − b)/c`. Moving d ↦ d+1 sends p to
p + 4ab, and similarly for the other Type I/II coordinates. These moves are affine in n. The orbit of one seed under
any finite set of them lies in a finite union of ET congruence classes. → **B1** (Theorems M/C; Mordell's
square-class obstruction for bounded parameters is unconditional). Allowing unbounded parameters is ET's own
parametrisation: the orbit is all of S and the move graph carries no information (B2 lottery).

**(M3) Birational automorphisms.** Bir(𝒞) is the Cremona group. It acts transitively on 𝒞(ℚ) minus lower-dimensional
sets, so "connectivity" is automatic and content-free. Positivity and level 4 are not preserved by any nontrivial
element of bounded degree that we know of; level 4 is a congruence condition, so preserving it is a
congruence-subgroup condition (→ B1 for bounded degree).

**(M4) Chord–tangent (Manin) moves.** For P, Q ∈ 𝒞, the third point of the line PQ is
`R = B·P − A·Q`, where `A = ∇σ₃(P)·Q` and `B = ∇σ₃(Q)·P`. This is quadratic in the coordinates, and
`n(R) = −R₀` is not a multiple of n(P) or n(Q). So it is the one natural move with property (2).

**Theorem A.1 (PROVED; real-geometric).** Let Ω ⊂ 𝒞(ℝ) be the set of real points with no zero coordinate and
sign type (1,3), i.e. exactly one coordinate of a different sign from the others. This set contains all positive ES
points. Let L ⊂ ℙ³ be a real line not contained in 𝒞 and meeting 𝒞 in three distinct real points. Then at most two
of them lie in Ω.

*Proof.* Parametrise L by the circle ℙ¹(ℝ) and write `Xᵢ = ℓᵢ(s,t)` for linear forms ℓᵢ.
* No ℓᵢ vanishes identically. Otherwise all of L ∩ 𝒞 lies in a coordinate plane, and Ω has no points there.
* First assume general position: the four roots rᵢ of the ℓᵢ are distinct. They cut the circle into four arcs.
* Crossing rᵢ flips the sign of ℓᵢ only. Once round the circle, every sign flips, which is the projective
  identification. So the numbers of negative signs on consecutive arcs are k, k±1, … The two arcs of odd parity have
  type 1, and the two of even parity have type 0 or 2.
* On an arc, `h = Σ 1/ℓᵢ` has the same zeros as σ₃ (ℓᵢ ≠ 0 there). Near the starting endpoint r_a, h → (sign of ℓ_a
  on the arc)·∞. Near the ending endpoint r_b, h → (sign of ℓ_b on the arc)·∞. So the number of zeros on an arc is
  odd iff these two signs differ.
* On a type-0 arc all ℓᵢ have one sign, so h ≠ 0 there.
* Enumerating all 2⁴ initial sign vectors gives the arc parities. With three roots in total, the type-1 arcs carry
  at most 2 of them in every case.
* Lines not in general position can be perturbed to general position with the three distinct transversal
  intersection points moving continuously and staying in the open set Ω. ∎

The finite enumeration is `scripts/bs_graph_arcs.py` (exhaustive over the 16 sign vectors; every admissible root distribution has ≤ 2 roots on type-1 arcs). There is also a convexity
proof for the case where both points have the same special index: in the chart X₀ = −1, `Σ_{i≥1} 1/xᵢ − 1` is
strictly convex on the open orthant, so it has at most two zeros there.

**Corollary A.2 (PROVED).** Take two distinct positive solutions P, Q (of any n, n′) whose line is not in 𝒞 and
whose third point R is distinct from both. Then R is a *signed* solution of type (2,2), or it has a zero coordinate.
So chords never produce a positive solution from two positive ones.

The tangent case (P = Q) is EVIDENCE only: 10⁵ random real tangent sections, all of type 2. The general-position
argument with multiplicity would need the double root split into two real roots, and this was not written out.

**Corollary A.3 (PROVED, from A.1).** Fix a positive seed P₀ of any n₀. Every positive ES point R for p, off the
lines through P₀, is the chord-image `chord(P₀, Q)` of the signed point Q = third point of line P₀R. So "ES(p) is
reached in one chord move from P₀" is a bijective restatement of ES(p) via signed points of *other* N. Signed
points are abundant (LONGSHOT_PIGEONHOLE Lemma 1.3), but which signed point lands on N = p is a divisor event:
`n(R) = −(B·P₀ − A·Q)₀` must equal p up to the content. → B2.

## 4. Experiments (`scripts/bs_graph_cayley.py`; tiny outputs)

* All 363 primitive positive ES points with n ≤ 30: 65 703 chords. 60 316 have type (2,2), 5 387 lie on a
  coordinate plane, and **0 are positive**, as Cor A.2 predicts.
* Real random chords between Ω-points with arbitrary special indices, and tangent sections (10⁵ each): third points
  of type 2 only.
* Mixed chords, with P one of the 247 positive points with n ≤ 20 and Q one of the 5 985 signed points with n ≤ 20
  (one negative denominator): 501 461 ES points and 972 556 level-free positive points. Of the ES points, 1 136 have
  prime N. So mixed chords do reach primes, but with no control over which N arises.
* The 16-case arc table (Theorem A.1): in every case the type-1 arcs carry ≤ 2 of the 3 roots.

## 5. Barrier screen

* **B1.** Bounded-word orbits of M2/M4 from finitely many seeds are either finite unions of polynomial/congruence
  families or finite sets, so Theorem M/C apply. M2 orbits are ET classes; Mordell's square-class obstruction is
  unconditional.
* **B2.** M4 with a signed point is the only non-multiplicative positive-producing move (A.2/A.3). Whether it hits
  N = p is "an integer quadratic in Q's coordinates equals p up to content", the lottery restated.
* **B3/B4.** Count: if moves raise height polynomially, the depth-k orbit up to height X has (log X)^{O(1)}
  elements, which is too few for primes. If they do not (M3, or unbounded M2), there is no counting content.
* **B5 (odd squares).** At n = m², positive primitive level-4 points with N = m² do not exist (ET Prop 1.6; ES(m²) is
  realised only by imprimitive points of content m). A move system claiming to hit every N would have to be false
  at N = m². For M4 this is exactly the step "some signed Q lands on N", which is the step that fails at m².
* **B6.** Not applicable (no averaging used).
* **Graph-theoretic properties** (components, degrees, spectral gap) of any graph whose vertices are solved n
  cannot force a new vertex. Forcing needs moves (correspondences) defined independently of solvability, and the
  classes M1–M4 exhaust the natural ones. Large-n spectral computations were therefore not run: they would only
  measure ES's own counting function.

## 6. Viability Assessment

**COLLAPSES** to B1 (M1, M2, bounded M3) and B2 (M4) at the step "a move produces a positive point with prescribed
N".

By-product: **Theorem A.1 / Cor A.2 (PROVED; real-geometric).** No line meets the positive (type-(1,3)) real
locus of the Cayley cubic in three distinct points, so chord–tangent moves never close up on positive Egyptian
solutions. Every positive solution arises from a positive seed only through a signed point. This explains
structurally why the chord–tangent ("Mordell–Weil") dynamics of the ES surface gives no positivity mechanism. As far
as I know it is not in the literature, but it is elementary, so novelty is unverified and probably minor. It applies
equally to 1/n, m/n and any positive unit-fraction triple, since it uses only the sign region.
