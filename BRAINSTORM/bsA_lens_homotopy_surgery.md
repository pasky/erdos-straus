# bsA_lens_homotopy_surgery — lens-space reading: homotopy type, knot surgery, 2-bridge knots, Matveev complexity (O174)

## Idea
DEDEKIND_ES 5.2: n/A = [[v,t,u]] ⟺ L(n,A) bounds the negative-definite linear plumbing of three spheres with Euler
numbers −v, −t, −u. The plumbing *existence* is free (every lens space has its HJ plumbing). The content is the
**length**, together with the **square class of the linking form**. I looked for topology theorems that speak to the pair
(short plumbing, non-square linking form).

**P1 (homotopy dictionary; PROVED from the classical Whitehead theorem).** L(p,q) ≃ L(p,q′) (homotopy equivalent) iff
qq′ ≡ ±k² (mod p) (Whitehead 1941; classical, from memory). For p ≡ 1 (4) prime, −1 is a square, so
(A/p) = −1 ⟺ L(p,A) is not homotopy equivalent to L(p,1) = S³_p(unknot). Hence
**five-slice ES(p), p ≡ 1 (8): some lens space of order p that is *not* homotopy-equivalent to L(p,1) bounds a linear
plumbing of ≤ 3 spheres** (≤ 2 spheres = boundary case λ = 2).
*Scope.* At n = m² the reading breaks down. For example, −1 is a square mod 25, so L(25,A) with A a non-square mod 25
is not homotopy equivalent to L(25,1). Yet all five slices vanish at 25, because Jacobi (A/25) = +1. **ES sees only
the Jacobi symbol, which is strictly coarser than homotopy type at composite n.** This is T1 in topological
clothing: the slices are blind to the homotopy information at squares.

**P2 (knot surgery; PROVED, standard linking-form argument).** If L(p,A) = Y_{±p}(K) for a knot K in an integral
homology sphere Y, the meridian generates H₁ with self-linking ±1/p. So A is ± a square (Greene's necessary
condition; Greene, Ann. Math. 177 (2013) 449, arXiv:1010.6257). For p ≡ 1 (4) and (A/p) = −1, **L(p,A) is never
p-surgery on a knot in any ℤHS³.** So the ES certificates are the short-plumbing lens spaces that lie *outside* the
whole Berge/changemaker world (Greene's changemaker theorem classifies the QR side completely), and the theorem
classifying the QR side is silent on the QNR side.

**P3 (2-bridge knots).** L(p,A) = Σ₂(K(p/A)), and K(p/A) bounds the plumbing of three unknotted twisted bands (v, t, u
half-twists). Its Goeritz matrix is the tridiagonal G of bsA_selling_sandpile. The class (A/p) is an invariant of
K up to mirror (Schubert: K(p/A) ≅ K(p/A′) iff A′ ≡ A^{±1} (p), mirror A ↦ −A). So five-slice ES(p) ⟺ **some 2-bridge
knot of determinant p with non-square Goeritz class has a 3-band plumbing surface.** Lisca (G&T 11 (2007) 429,
verified) classifies lens spaces bounding ℚHB⁴s and slice 2-bridge knots. These need p = m², a metabolic linking
form. This is the topological home of squares, but its condition (metabolic) differs from Jacobi +1, so it is not T1.

**P4 (Matveev complexity).** By memo bsA_farey_lnr_pigeonhole Lemma 2, r(p/A) + r(p/(p−A)) = S(p,A) := Σ a_i. Matveev's
upper bound c(L(p,q)) ≤ S(p,q) − 3 is sharp in proven cases (Jaco–Rubinstein–Tillmann, J. Topology 2009, p even; from
memory). So the HJ lengths of a lens space and of its orientation reverse L(p,−A) add up to complexity + 3. A short
plumbing (r = 3) has r′ = c(L) + 0 when the conjectured equality holds. ES five-slice ⟺ a QNR lens space whose complexity is
almost entirely carried by the reversed plumbing.

## Literature
Greene 2013 (abstract verified); Lisca 2007 (Thm 1.2 verified); Whitehead/Reidemeister classification of lens spaces
(classical); Jaco–Rubinstein–Tillmann (from memory); Schubert 1956 (classical).

## Barrier screen
* Gauge/Floer results (Greene, Lisca, Heegaard Floer d-invariants) are **obstructions**. They forbid surgeries and
  fillings and assert no existence of short plumbings. P2 places the certificates in the region they do not cover.
* The square class is congruence data on A (B1), and the length is the B2 divisor event. No topological existence
  theorem about *short* plumbings with a *prescribed homotopy type* is known to me. The homotopy type of a lens space
  of order p is one bit, (A/p), and the shortness is arithmetic.
* T1: P1 makes precise that ES is blind to homotopy at squares (Jacobi vs ± square class).

## Cheap numerics
P1 scope check (inline enumeration with `bsA_hjlen.hj_direct`). The length-3 words with numerator m² whose A is a
non-square mod m, i.e. whose lens space is *not* homotopy equivalent to L(m²,1):
* n = 25: 2 of 4 (A = 3, 17);
* n = 169: 4 of 10;
* n = 289: 6 of 8;
* n = 841: 8 of 16.

So at squares there are plenty of short-plumbing lens spaces with the "wrong" homotopy type. None is an ES
certificate, since the Jacobi symbol is +1. This confirms the scope statement in P1.

## Assessment
Precise dictionaries (PROVED relative to classical theorems): ES five-slice = "a non-L(p,1)-homotopy-type lens space
of order p with a ≤ 3-sphere linear plumbing". The certificates lie exactly where Greene's realization theorem says
nothing. The topology framing adds an explanation of why T1 is "coarser than homotopy". It offers no existence
mechanism. Promise 0–1/5.
