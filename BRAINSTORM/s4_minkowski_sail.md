# s4_minkowski_sail — Minkowski/Thue are sign-blind, the one-quadrant (Klein sail) geometry of numbers is the HJ word set, and no volume theorem exists for one quadrant (O218)

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
Geometry of numbers at a single p, with positivity. For A ∈ (ℤ/p)^*, Λ_A = {(x, y) ∈ ℤ² : x ≡ A y (mod p)}, covolume p.
**Lemma M (PROVED; the lattice form of (J)39 Lemma 1.1).** Positive vectors (c, s) ∈ Λ_A with cs | p + c + s are exactly
the length-3 words (c, m, s), m = (p + c + s)/(cs), with s·K(c, m) ≡ c, i.e. A ≡ c·s⁻¹ (mod p); the ES sign is
χ = (−cs/p) ((J)39 Lemma 1.1), a function of A (cs ≡ A s² mod p). *(From cms − c − s = p: (cm − 1)s ≡ c.)* So ES-five(p) ⟺ some Λ_A of the
right quadratic class has a vector in the open positive quadrant, under the hyperbola xy ≤ p + x + y, satisfying the
exact divisibility cs | p + c + s.

## Tools
1. **Minkowski / Thue / Siegel's lemma are sign-blind.** They produce v ∈ Λ_A ∖ 0 with |x|, |y| ≤ √p, but the body is
   centrally symmetric, so they cannot choose the quadrant: the reduced (Gauss–Lagrange) shortest vector lies in the
   positive quadrant for exactly 50.0 % of the 261 032 pairs (R219 D10d: exactly ½ is PROVED by the symmetry below) (p ≡ 1 (8) < 6000, A a QNR) — the c_∞ involution
   A ↦ −A (Λ_{−A} = reflection of Λ_A) swaps quadrants. Thue's lemma gives sums of two squares because x² + y² is
   sign-blind; ES needs a sign-sensitive product (s4_three_bits_meta).
2. **One-quadrant geometry = Klein sail = HJ.** The convex hull of Λ_A ∩ ℝ²_{>0} has boundary vertices given by the
   Hirzebruch–Jung expansion of p/A (classical toric geometry: cyclic quotient singularities; Oda, *Convex bodies and
   algebraic geometry*, §1.6). The other quadrant is HJ of p/(p − A) (Riemenschneider duality) — **c_∞ acts as
   Riemenschneider duality**. (J)9's "length-3 HJ" is "the sail of Λ_A has 3 interior boundary points".
3. **No volume theorem for one quadrant.** There is no Minkowski-type bound forcing a lattice point of covolume-p
   lattices into {x, y > 0, xy ≤ K} for K < p: Λ_{−1} = {x ≡ −y} has positive vectors only with xy ≥ p − 1. So any
   positivity-using lattice-point existence statement here must use *arithmetic of A* (here: A a QNR), i.e. it is a
   statement about the joint distribution of sails and quadratic characters — the lottery.
4. Harness: the reduced basis (±b₁, ±b₂, ±(b₁ ± b₂)) of *some* QNR A contains a word vector for every prime
   p ≡ 1 (8) < 6000 (0 failures; 1.68 % of QNR pairs). This only says some certificate word is *balanced*
   (c ≈ s ≈ √(p/m)); it is ES-five with a size restriction, not a mechanism (Assessment). Odd squares: no QNR A exists
   mod m², so the statement is vacuously T1-correct.

## Barrier screen
B2: the exact divisibility cs | p + c + s (equivalently m ∈ ℤ) is the moving modulus; the lattice only encodes the
congruence. B4/LONGSHOT_PIGEONHOLE: pigeonhole/Thue collisions = differences = signed. B1: none. T1: vacuous at
squares (no QNR).

## Cheap numerics
`scripts/s4_sail.py 6000` (≈ 1 min): output quoted in 1 and 4.

## Assessment
Dictionary (Lemma M PROVED; sail ↔ HJ classical; "c_∞ = Riemenschneider duality" a relabelling of TRANSPORT §3.2).
Symmetric geometry of numbers is positivity-blind for a structural reason (central symmetry = the c_∞ involution);
one-quadrant geometry of numbers is the HJ word set itself and has no volume principle. COLLAPSES to B2. Promise 0–1/5.
