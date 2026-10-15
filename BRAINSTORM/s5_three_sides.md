# s5_three_sides — every word sits on three side numbers; near-square hardness is mostly three-side cleanliness (O230)

## Idea
Combination (i) of the O230 brief ((J)48 ℤ³ side × (J)53/(J)55 near-square deformation), read on the divisor side.
A word w = (t, u, v) of X_p (tuv − u − v = p) has A = tu − 1, B = tv − 1 and three **side numbers**

  N_t = tp + 1 = A·B,  N_u = p + u = A·v,  N_v = p + v = B·u.

(J)53/(J)55 used only N_t ("clean levels"). R225's partial "u-side T1" hinted at N_u. Here the three sides are treated
symmetrically. Combination (i) asked for an explicit ℤ³ embedding. Its side-number shadow is the observation that each
side number is primitively represented by a binary form of determinant equal to the side variable. This gives three
deformation mechanisms, not one.

## Lemma S (PROVED, elementary)
Let p ≡ 1 (mod 4) be prime and ψ(r) = (r/p).
(a) χ(w) = (−A/p) = ψ(A) = ψ(B).
(b) For an odd prime r | N_X, X ∈ {t, u, v}, we have r ≠ p and ψ(r) = (−X/r). On the u-side, p ≡ −u (mod r) and
reciprocity gives (r/p) = (p/r) = (−u/r). On the t-side, tp ≡ −1 gives (p/r) = (−t/r).
(c) Call side X *clean* if every prime factor r of N_X, including 2, has ψ(r) = +1. Then χ(w) = +1 for every word whose
X-coordinate is that value, because A | N_t, N_u and B | N_t, N_v.
*Proof.* (a) AB = tp + 1 ≡ 1 (mod p). (b) r | p + u with r = p would force p | u, and then v(tp − 1) = 2p: there are
no such words for p > 3. The rest is quadratic reciprocity. (c) ψ is completely multiplicative. ∎

## Side deformations (PROVED, elementary)
Let p = m² + K.
* t-side ((J)53): if tK + 1 = c² with gcd(m, c) = 1, then N_t = t·m² + c², and every odd prime factor r of N_t has
  (−t/r) = +1.
* u-side (new form): if u(K + u) is a perfect square and gcd(m, K + u) = 1, then N_u = m² + (K + u). Every odd prime
  factor r of N_u has (−(K + u)/r) = 1 and (u(K + u)/r) = 1, hence (−u/r) = +1. (r ∤ m(K + u) by the gcd condition, and
  r ∤ u since r ∤ p.) The v-side is the same with v in place of u.
* For p ≡ 1 (mod 8) the prime 2 is harmless (ψ(2) = 1), so these sides are fully clean.
* The u-side condition u(K + u) = □ means u = d·a², K = d(b² − a²). There are finitely many such u for each K, about
  τ(K) of them, versus infinitely many t-side levels (a Pell-type family). For K = 24: u ∈ {1, 3, 8, 25}, t ∈ {1, 2, 5,
  7, 12, …}.
* R225's mechanism "K + u = s²" is a different sub-case: it uses χ = (−u/A) with every prime factor of A ≡ 1 (mod 4).
  The two overlap at u = 1.
* The ℤ³ reading (Assessment). In each case the side number is the norm of an explicit element of an imaginary
  quadratic order, with ℚ(√−t) on the t-side and ℚ(√−u) on the u-side. This is the binary shadow of (J)48's ternary
  embedding: Thm A needs |x × y|² = tp, and the deformation hands over a representation of N_t. No canonical
  *non-embeddable* lattice comes out of the unclean levels. Whether an unclean side yields a χ = −1 word is still the
  B2 event "some sub-product ≡ −1 (mod X) with odd ψ-parity".

## Literature
Genus theory / quadratic reciprocity only. The t-side is THREE_SQUARES Lemma 1.4 and NEAR_SQUARE Prop 4.1. R225 had the
u-side idea in the narrower form K + u = s². The symmetric three-side form and the census below are new to the campaign.

## Barrier screen
* B5/T1: at n = m², every side is clean (K = 0: u·u = □ and t·0 + 1 = 1), so this is T1 deformed on all three sides.
* B2: cleanliness only ever forces χ = +1. It explains hardness and never produces a certificate. That is the expected
  direction (anti-existence) and a steering fact, not a route.
* B1/B6: the deformations are polynomial families in m, so they are covered by (J)55 Thm 2.2 at the level of
  coverings.

## Cheap numerics (EVIDENCE)
`scripts/s5_sides.c` gives the per-prime counts N, N₋, N_t-clean, N_{u/v}-clean and N_any-clean, and checks that no
χ = −1 word lies on a clean side. `scripts/s5_sides_hardness.py` gives within-adelic-cell residuals by
K0 = p − ⌊√p⌋².
* There are 0 violations of Lemma S(c) over all 169 410 primes p ≡ 1 (mod 4) in (10⁵, 5·10⁶) (32 947 010 ordered words).
  The (10⁵, 10⁶) totals reproduce ns_census exactly (5 570 014 words, 432 677 on t-clean levels).
* Words on clean sides: 2 307 928 on t-clean sides, 3 536 930 on u/v-clean sides, 4 252 984 on any clean side (13 %).
  **The u/v-sides force more words than the t-side does.**
* Within-cell residual of the χ = −1 fraction, for primes in (10⁵, 5·10⁶) with cells = (p mod 8, (r/p) for r ≤ 13,
  lnr) refined by p mod 9 and p mod 16 (384 cells):

| K0 | n | N₋/N | after removing t-clean | after removing any clean side |
|---|---|---|---|---|
| [1,5) | 367 | −0.035 | −0.011 | −0.009 |
| [5,10) | 308 | −0.042 | −0.035 | −0.033 |
| [10,17) | 512 | −0.043 | −0.022 | −0.007 |
| [17,30) | 925 | −0.038 | −0.024 | −0.013 |
| [30,100) | 4 648 | −0.018 | −0.011 | −0.005 |
| [100,300) | 13 703 | −0.011 | −0.0065 | −0.0021 |
| ≥ 300 | 148 947 | +0.0021 | +0.0013 | +0.0005 |
| K0 = 16 | 187 | −0.060 | −0.027 | +0.008 |
| K0 = 24 | 105 | −0.169 | −0.082 | +0.014 |
| K0 = 8 | 97 | −0.094 | −0.071 | −0.074 |

  The naive standard errors are about 0.003 for the small bins and 0.0005 for [100, 300). They ignore the estimation of
  cell means and the multiple bins.
* With the coarser cells (no mod 9/16) the K0 = 8 residual is −0.137 rather than −0.094. Part of the K0 = 8 effect is
  3-adic: p = m² + 8 forces 3 | m and p ≡ 8 (mod 9). Refining further (mod 25, 49; 74 040 cells) shrinks every residual
  through singleton cells, so that run is not interpretable.

## Assessment
* PROVED: Lemma S and the three side deformations.
* EVIDENCE:
  * Exact three-side cleanliness removes about 70–80 % of the residual near-square depletion of χ = −1 words for
    10 ≤ K0 < 300, and all of it at K0 = 16 and 24. This roughly halves what (J)53/(J)55 left as "beyond clean
    levels" (R225 spark S2).
  * K0 = 8 (and, weaker, 4, 12, 28) keeps a depletion after both refinements.
  * Follow-up test (`scripts/s5_defect.c`, same 169 410 primes). A side is *square-defect* if every prime r with
    ψ(r) = −1 divides it to an even power (and at least one does).
    * Generic square-defect sides are **not** depleted: the χ = −1 rate is 0.743 on them versus 0.755 on generic sides
      (primes with K0 ≥ 300). So the naive "square-defect" conjecture is REFUTED as a general mechanism.
    * At K0 = 8, 45 % of all words lie on square-defect sides (11 % elsewhere), and their χ = −1 rate is 0.485 versus
      0.784 on the remaining unclean sides. So **the K0 = 8 depletion is the defective deformation**.
    * Mechanism. Primality forces 3 | m, so the u = 1 side (u(K + u) = 9) and the t-sides with 8t + 1 = c², t ≡ 1 (mod 9),
      are clean apart from an exact factor 9 = 3², with ψ(3) = −1. A χ = −1 word on such a side needs 3 ‖ A.
    * CONJECTURE D: deformations with g = gcd > 1 deplete; generic square-defect sides do not. The data above
      supports it at K0 = 8 only, and it is untested elsewhere.
* This is a hardness explanation, not an existence mechanism (B2).
