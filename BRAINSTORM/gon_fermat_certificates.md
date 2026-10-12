# Brainstorm O148(a): Minkowski / Blichfeldt / star bodies — "Fermat certificates" for ES

ES is not solved; nothing here proves any case of it. Labels as in DISCOVERIES.md.

## 1. Idea

Geometry of numbers (GoN) is the one classical technique that proves *pointwise* existence for every prime
with no congruence covering and no main-term-vs-error comparison. Prototype (Fermat via Thue/Minkowski):
p ≡ 1 (4), i² ≡ −1 (p), Λ = {(u,v): u ≡ iv (p)} has covolume p; the disc u²+v² < 2p has area 2πp > 4p, so
Minkowski gives 0 ≠ (u,v) ∈ Λ with u²+v² ≡ 0 (p) and 0 < u²+v² < 2p, hence u²+v² = p.

Abstract shape (**Fermat certificate**): a lattice Λ(p) ⊂ ℤᵏ defined by congruences modulo M(p), possibly
using roots of polynomial congruences mod p (non-polynomial in p!); a body R(p) (convex symmetric, or a star
body with known critical determinant, or an inhomogeneous region with known inhomogeneous minimum); a
polynomial F with F(Λ) ⊂ t + Mℤ; and a size bound on R making "F ≡ t (M)" into "F = t", and "F = t" a witness.

Why this is worth screening: it escapes two barriers *in principle*.
* **B1 (Thms M/C).** Fermat's theorem is not a congruence covering, and √−1 mod p is not a polynomial
  function of p. Theorem M's procedures (ring ops, floor division, factorisations) do not include "take a
  modular square root"; POINTWISE_SIZE §4 item 1 lists such oscillating archimedean tests as E2 (outside scope).
* **B3 (scale).** Prop 2.3 constrains certificates "count ≥ M − error". Minkowski is exact (≥ 1 point once
  vol ≥ 2ᵏ covol) with main term M = vol/(2ᵏ covol) ≍ 1 ≤ p^{o(1)}. The scale constraint *allows* it.

So the question is whether some ES slice has the Fermat shape. What would be needed:
**(F-ES)** a lattice Λ(p), a body R(p), and a map W with W(Λ(p) ∩ R(p) ∖ 0) ⊂ {ES witnesses of p}, with vol(R)
≥ 2ᵏ covol(Λ) (or a star-body/inhomogeneous analogue).

## 2. Literature anchor (from memory unless marked)

Minkowski convex body theorem, Blichfeldt, van der Corput (#(Λ∩R) ≥ 2⌊vol R/(2ᵏ covol)⌋+1), Hurwitz/Markov
(|xy| ≤ Δ/√5 for a nonzero lattice point, star body, critical determinant), Minkowski's 2-dim inhomogeneous theorem
(|x₁x₂| ≤ Δ/4 on every coset), Minkowski's conjecture on products of inhomogeneous forms (McMullen, JAMS 18 (2005)
for n ≤ 6 via closed A-orbits; later n ≤ 9 by Hans-Gill–Raka–Sehmi and others — from memory, unverified).
Ankeny's GoN proof of the three-squares theorem (Proc. AMS 1957) uses Dirichlet's theorem as extra input.
The GoN proofs of representation theorems (two, four squares; x²+ny² for idoneal n) work exactly in one-class
genera: Minkowski bounds the norm of an ideal *in each class*; it says nothing about which class.

## 3. Barrier screen

**Lemma 3.1 (every ES slice is a split rational binary problem; PROVED, elementary).** In ET coordinates
(Type I: pe+1 = 4abd, a+b = ce; Type II: p+e = 4abd, a+b = ce), fixing (c,d):
Type I ⟺ XY = p²+4c²d with X = 4acd−p, Y = 4bcd−p; Type II ⟺ XY = 4c²dp+1 with X = 4acd−1, Y = 4bcd−1.
Fixing e: Type T ⟺ ab | N_e^T, a ≡ −b (e) (LONGSHOT_PIGEONHOLE Lemma 1.1). In all cases the target set is
{v in a coset of a full-rank sublattice of ℤ² : L₁(v)L₂(v) = N} with L₁, L₂ rational linear forms and N a
specific integer — a *level set of a split (isotropic) form*, not a sublevel set.
*Proof.* Type I: p(a+b) = pce = c(4abd−1), so (4acd−p)(4bcd−p) = 16abc²d² − 4c²d(4abd−1) + p² = p² + 4c²d.
Type II: c(p+e) = 4abcd gives cp = 4abcd − (a+b), so (4acd−1)(4bcd−1) = 4cd(4abcd−a−b) + 1 = 4c²dp + 1.
Conversely X, Y in the cosets with XY = N give back (a,b) and the ET equations (divide by 4cd). The
standard ET computation (redteam-2 Lemma 2.1, POINTWISE_SPECTRAL Lemma 2.1, TYPEII_SPECTRAL); checked
symbolically in `scripts/bs_gon_split.py`. ∎

*Remark (the full cubic as a product of three linear forms; PROVED by expansion).* With X = 4x−n, Y = 4y−n,
Z = 4z−n: 4/n = 1/x+1/y+1/z ⟺ **XYZ = n²(X+Y+Z+2n)**, X,Y,Z ≡ −n (4), X,Y,Z > −n (check: n = 5,
(x,y,z) = (2,4,20) gives 3·11·75 = 2475 = 25·99). This is the Davenport/Minkowski-conjecture shape "product of
three linear forms" — but again on the *rational* product coset (−n,−n,−n)+4ℤ³ (det 64), where the dimension-3
inhomogeneous theorem (|XYZ| ≤ 64/8 = 8 somewhere on the coset) is satisfied by the trivial centred point and
says nothing; and the target is an *equation* coupling XYZ to X+Y+Z, not a sublevel set. Unlike Markoff-type
cubics, the equation is linear in each variable, so there are no Vieta involutions and no infinite automorphism
orbits for strong-approximation/orbit methods to use (consistent with GEOMETRY_ES Thm 3.1).

Consequences for (F-ES):
* **The GoN step carries no information on split rational targets.** Minkowski / van der Corput / Hurwitz /
  Minkowski-inhomogeneous produce points with |L₁L₂| *small* (≤ Δ/4 on a coset of determinant Δ). To turn
  "L₁L₂ ≡ N (mod M)" into "L₁L₂ = N" one needs |L₁L₂ − N| < M on R; but L₁L₂ ≡ N mod a modulus M ≫ 1 that is
  *independent of the unknown* is only available if one already fixes a residue of X modulo a divisor-sized
  modulus, i.e. a divisor of N (Λ = {X ≡ X₀ (N)} with X₀ | N). The "Fermat" step then reads "N has a divisor
  in a class" — B2 verbatim. For rational lattices the inhomogeneous minimum of XY on a coset of qℤ² is
  attained by the trivial point (smallest centred representatives — the coset is a product, so |XY| = |X|·|Y|
is minimised coordinatewise), so McMullen-type theorems are idle.
* **vol/covol.** The thickened target {|XY − N| ≤ ½, 1 ≤ X ≤ Y} has area ≍ log N; the coset (−p,−p)+4cdℤ²
  has covolume 16c²d². Expected count log p/(c²d²) per (c,d)-slice; summed over admissible slices this is ET's
  ≍ log³p mass (ET Thm 1.1, via the extra divisor sums) — polylog, and no single slice has vol/covol ≫ 1 except
  the bounded set c,d ≪ (log p)^{1/2}, where the "volume" is a hyperbola (measure zero; only a thickening has
  area), so Minkowski does not apply at all. **Assessment: (F-ES) has no candidate with a split form.**
* **Anisotropic encodings** (the only shape where GoN has teeth) — candidates in the campaign:
  (i) Type I as ideal divisors of p+2c√−d in ℚ(√−d) (EXACT_FORMULA Thm 5.2): the definite form x²+dy² *already*
  represents p²+4c²d trivially; ES needs a *factorisation* of the element p+2c√−d, i.e. ideals 𝔞 ∋ p+2c√−d —
  a finite divisor list, not a class question. Moreover Type I at level d needs (−d/p) = −1 ((I)7): p is inert,
  so the field's class group carries no information about p at all.
  (ii) Type II as Heegner forms of disc −4dp ((I)4): GoN = reduction theory, giving one reduced form per class
  with A ≤ √(4dp/3). ES needs a form on the shell ⟨u,v⟩ = −1 — a Planck-width target, not a reduced-form
  condition; reduction puts *every* class in the fundamental domain, so it cannot single out the shell.
  (iii) Quaternion orders in B_{p,∞} ((I)6): Minkowski on a maximal order gives an element of reduced norm
  ≪ √p; ES needs the specific x = 2 collision 4abd − 1 = pe, again a factorisation of pe+1.
* **B5 (odd squares).** For a Fermat certificate the odd-square test splits cleanly. The GoN step itself uses
  only local data (roots mod p, residues mod M); these exist at n = m² whenever they exist mod each prime of m
  (for x²+y²: m² is primitively represented when m has a prime ≡ 1 (4)). So the step that must be FALSE at m² is
  the conversion W: "lattice point ⇒ Type I/II witness". By Lemma CT every ES denominator prime to p has a prime
  factor ℓ with (ℓ/p) = −1; hence W must read a *quadratic non-residue* off the lattice point. A norm-form value
  F(v) = p carries only data that holds equally at m².
* **Fermat + bounded post-processing is inside Theorem C (Assessment, partly proved).** If GoN outputs w with
  p = F(w) for a fixed form with essentially unique representations (e.g. u²+v²) and a bounded Theorem-M procedure
  then builds the witness from w, restrict w to a line w₀ + q·w₁: the composite is a bounded procedure on the
  polynomial input P(q) = F(w₀+qw₁). Theorem C is PROVED only for *linear* P; the extension to quadratic P is
  not proved here (square-mimicking points for P exist; the remaining step is the nondegeneracy bookkeeping).
  If it extends, every such certificate fails infinitely often under H. Representations of p by forms with many
  representations (indefinite, k ≥ 3) let GoN choose *which* w — that choice is the only non-polynomial part,
  and it is again a "which divisor/which class" choice (B2).
* **B6/T7.** No averaging enters; GoN is genuinely pointwise. Its failure here is structural, not an average leak.

## 4. Experiment

`scripts/bs_gon_split.py`: symbolic check of Lemma 3.1 (both types, both slicings) and of the claim that the
inhomogeneous minimum of XY on (−p,−p)+qℤ² is the trivial centred point, for small p, q (brute force).

## 5. Viability Assessment

**COLLAPSES to B2 at step "F ≡ t (M) ⇒ F = t".** GoN gets pointwise existence only from a norm-form/one-class
situation; every ES slice is a level set of a split rational form (Lemma 3.1), where the Fermat step needs a known
divisor of N_θ(p), and the anisotropic encodings found so far ((i)–(iii)) need a factorisation of a specific
element rather than a class datum. GoN *does* pass B1 and B3 in principle, which is worth recording: the barrier
it hits is the divisor-class reduction, not the scale constraint.
By-products: Lemma 3.1 (PROVED, elementary, folklore-level); the observation that Fermat-type certificates evade
Prop 2.3 and Theorem M's scope (Assessment, with the precise reason: exact existence with M ≍ 1, and modular
square roots are not Theorem-M operations); B5 refinement: any ES certificate must extract a quadratic
non-residue mod p (Lemma CT), which a norm-form value p = F(w) does not encode.
