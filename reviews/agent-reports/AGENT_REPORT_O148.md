# AGENT REPORT O148 — brainstorm: geometry of numbers / lattice reduction / matroid angles

Branch `side-agent/bs-geom-numbers`. Three memos, three scripts (`scripts/bs_gon_*.py`, each under 10 s). ES is
not solved; no case of it is claimed. No memo is LIVE.

**(a) `BRAINSTORM/gon_fermat_certificates.md` — Minkowski / Blichfeldt / star bodies / inhomogeneous minima.**
Verdict: **COLLAPSES to B2** at the step "F ≡ t (mod M) ⇒ F = t". GoN is worth recording because it passes B1 and
B3 in principle. Fermat-type certificates prove exact existence with main term ≍ 1, so the scale constraint
allows them, and modular square roots are not Theorem-M operations. The strongest reason for the collapse is
Lemma 3.1 (PROVED, elementary; symbolic check plus a brute-force bijection check for p < 60). Every ES slice is a
*level set of a split rational binary form*, XY = N_θ(p), on a product coset. The full cubic, too, is
XYZ = n²(X+Y+Z+2n) on (−n,−n,−n)+4ℤ³. On such rational product cosets the inhomogeneous minima of Minkowski or
McMullen type are attained at the trivial centred point. Turning a congruence into an equality then needs a known
divisor of N, which is B2 verbatim. The anisotropic encodings (CM torus, Heegner forms, B_{p,∞}) ask for the
factorisation of a specific element, not for an ideal class, so GoN's one-class-genus mechanism never engages.
Odd-square refinement: the GoN step holds at m², so the conversion step must extract a quadratic non-residue
(Lemma CT), and a norm-form value p = F(w) does not encode one. One gap is flagged honestly: the claim that
"Fermat + bounded post-processing lies inside Theorem C" needs Theorem C for quadratic P. It is not proved here
(Assessment).

**(b) `BRAINSTORM/gon_lll_relation_lattice.md` — LLL / Coppersmith / Lenstra, and the relation-lattice
(matroid) view.**
* (b1) **COLLAPSES**: Coppersmith's lattice gives "root ⇒ root of h", never the converse. Lenstra (≤ 11 divisors
  in a class once s > n^{1/3}; verified) and Coppersmith–Howgrave-Graham–Nagaraj give only multiplicity upper
  bounds.
* (b2) **PARTIAL (sharp reformulation)**. ES slice e ⟺ an explicit coset t₀ + L_e of the relation lattice of
  N's prime factors in (ℤ/e)^* meets the exponent box ∏[−v_ℓ, v_ℓ]. The coset exists iff −1 ∈ H_e, a
  subgroup-membership (matroid/genus) half. That half is PROVED for every prime p ≡ 1 (4), via Type II prime
  slices q ≡ 3 (4) with (q/p) = −1. It is exactly the step that fails at odd squares. The remaining box half is an
  ℓ^∞ inhomogeneous lattice problem. Its only GoN criteria (volume, Kannan–Lovász) need ω(N) ≳ log e, which is
  B4; its probabilistic version is B2's lottery.
* EVIDENCE (8 hard primes near 10⁸, e ≤ 3000): membership holds in a stable 45–60 % of slices. Given
  membership, the box condition decays from ≈ 85 % to ≈ 5 % as e grows. At odd squares 0 slices pass membership.
  The genus prediction for prime e is asserted in code.
* Caveat: whether the least such q satisfies q < p/3 unconditionally was not checked.

**(c) `BRAINSTORM/gon_incidence_kloosterman.md` — incidences, sum-product, Siegel/Thue, Kloosterman boxes,
small-exponent moduli.**
* Verdict: every sub-idea **COLLAPSES**, each with its step named.
* The strongest reason is the Kloosterman-box computation. Weil makes hyperbola points 4abd ≡ 1 (p) plentiful in
  every large box. The ES condition e | a+b, however, has a moving modulus e ≈ 4abd/p, with expectation only O(1)
  per dyadic box, and genus kills it at odd squares.
* EVIDENCE at p = 20161: 6·10⁶ hyperbola points but only 38 Type I witnesses. About 99 % of boxes with ≥ 100
  hyperbola points are empty, and the witness rate is ≈ 0.03 per box. This is B3/H-A.
* Sum-product needs a specific element with k = 2 from a non-subgroup set (B4). Siegel/Thue are linear while the
  target is bilinear plus divisibility (B2). Incidence theorems give only upper bounds.
* Small-exponent moduli make the box free only for e = 3, a fixed slice (B2 Thm 2.2(iii)).
* By-products (PROVED, elementary, folklore-level): Type I ⟺ (4abd−1) | p(a+b); Type II ⟺ (−p mod 4ab) divides
  a+b, a fractional-part form.

**Overall.** The cluster's exact by-products are Lemma 3.1, the XYZ form of the cubic, the two-half decomposition
with the membership half proved for all primes, and the compact divisibility forms. All are elementary and of
modest novelty. The one structural insight the parent may want to keep is that GoN is *not* excluded by B1/B3:
what excludes it is that every ES slice is a split rational form, where GoN has no content.
