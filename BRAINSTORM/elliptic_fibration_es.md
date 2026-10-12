# Elliptic curves inside the ES surface: the s-pencil, rank jumps, Heegner points (O143, memo 3)

Labels as in DISCOVERIES.md. Script: `scripts/bs_cubic_elliptic.py` (point counts, discriminant, a chord–tangent
torsion test on all 441 positive solutions of 4/p, 5 ≤ p < 120).

## 1. Idea
Which genus-1 curves sit inside the ES surface, and could a rank, Heegner-point or Gross–Zagier argument produce
an ES point for every prime? The natural genus-1 family is the pencil of plane sections not through the node P:
`E_{n,s} = U_n ∩ {u₁+u₂+u₃ = s}`. We determine it exactly.

## 2. Exact structure (PROVED unless labelled)

**P1 (the pencil is one n-independent family).** In s-coordinates S_i = 1/u_i, the fibre is
`C_N : (x+y+z)(xy+yz+zx) = N·xyz`, where `N = 4s/n = (u₁+u₂+u₃)(1/u₁+1/u₂+1/u₃)`.
So the ES elliptic curves do not depend on n: **every ES point of every n is a positive rational point on one of
the curves C_N, N ∈ ℚ, N ≥ 9 (AM–HM).** The integer n enters only through the denominator of N and through
integrality. The family C_N is classical: "(x+y+z)(1/x+1/y+1/z) = N" (Bremner–Guy–Nowakowski, Math. Comp. 1993,
from memory, not re-verified).
* Weierstrass model `E_N : Y² = X(X² + (N²−6N−3)X + 16N)`. This is from memory; check (1) confirms
  #C_N(𝔽_q) = #E_N(𝔽_q) for 6 values of N and 7 primes q, so the two curves are at least isogenous.
* `Δ(E_N) = 4096·N²(N−9)(N−1)³` (check (2)).

**P2 (singular fibres, Mordell–Weil).** The pencil is a rational elliptic surface with base points at the three
points at infinity C_N ∩ {x+y+z = 0}. Its singular fibres:

| N | type | geometry on the ES surface |
|---|---|---|
| 0 | I₂ | the plane through the node P: nodal cubic + exceptional curve |
| 1 | I₃ | the triangle of lines M₁ + M₂ + M₃ |
| 9 | I₁ | the AM–HM point u₁ = u₂ = u₃ |
| ∞ | I₆ | the boundary triangle through the nodes Q₁, Q₂, Q₃ |

Euler numbers 2 + 3 + 1 + 6 = 12. Shioda–Tate gives MW rank = 8 − (1 + 2 + 0 + 5) = **0**: the generic fibre has
only torsion. The six points (1:0:0), (0:1:0), (0:0:1), (1:−1:0), (1:0:−1), (0:1:−1) form a ℤ/6. That ℤ/6 is the
full torsion of this I₆I₃I₂I₁ configuration is from memory (Oguiso–Shioda list), consistent with the computed
orders 6, 6, 2, 3, 3.
**Consequence:** no section, i.e. no rational curve meeting every fibre once, carries ES points. **Every ES point
is a sporadic point of its own fibre.**

**P3 (ES points are rank-jump points).**
* (PROVED) The transposition y ↔ z is an involution of C_N with fixed points (those with y = z), hence of the form
  P ↦ T − P; it fixes the torsion point (1:0:0), so T = 2·(1:0:0) is torsion. A point with two equal u_i satisfies
  2P = T and is therefore torsion.
* (PROVED) For p ≡ 1 (mod 4), 4/p = 2/x + 1/z has no solution. If p ∤ x: z = px/(4x−2p) and
  gcd(4x−2p, x) | 2 force (2x − p) | p, so x = (p+1)/2 and z = p(p+1)/4, which needs p ≡ 3 (mod 4). If x = pk:
  z = pk/(4k−2) forces (2k−1) | p, so k = (p+1)/2, and then z = k/2 needs k even, again p ≡ 3 (mod 4).
* (EVIDENCE) In all 441 solutions with p < 120, a point is torsion (order ≤ 12, tested by chord–tangent) **iff**
  two u_i coincide (28 points, all with p ≡ 3 (mod 4)). So every ES point of a prime p ≡ 1 (mod 4), and in
  particular of the hard core p ≡ 1 (24), is a non-torsion point. It witnesses **rank E_N(ℚ) ≥ 1 at N = 4s/p**.
  This is unconditional for each such point once non-torsion is checked; general non-torsion is not proved here,
  since it would need excluding ℤ/12 and ℤ/2 × ℤ/6 torsion at the special N.

**P4 (integrality = being far from torsion).** u₁ = nS/(4x) as a function on C_N has its poles at C_N ∩ {x = 0}
\ {S = 0} = {(0:1:0), (0:0:1)}, both torsion points; similarly for u₂, u₃. Hence the ES points of n on C_N are the
points P ∈ C_N(ℚ) that are **q-adically far from the six torsion points at every q ∤ n**, apart from the bounded
allowance n/4 (an S-integrality condition on E_N \ E_N[tors]). For fixed (N, n) these points are finite in number
by Siegel. The condition is a congruence "P ≢ T (mod q^k)" whose moduli are the coordinates of P: the elliptic
form of B2.

## 3. Literature anchor
* Shioda–Tate formula and Oguiso–Shioda's classification of Mordell–Weil lattices of rational elliptic surfaces
  (from memory, unverified here).
* Siegel's theorem; Baker-type height bounds for integral points (standard).
* Gross–Zagier: ĥ(P_K) is proportional to L'(E/K, 1) (from memory).
* Lang's conjecture: ĥ(P) ≫ log|Δ_min(E)| for non-torsion P (open in general; proved for curves with integral
  j by Hindry–Silverman under abc, from memory).
* Bremner–Guy–Nowakowski on (x+y+z)(1/x+1/y+1/z) = N (from memory).
* No ES-specific elliptic literature was found (one web search, no hit).

## 4. Barrier screen
* **Integrality vs rationality (the decisive screen).** Rank or Heegner arguments produce rational points:
  generators, or Heegner points of canonical height ∝ L'(E,1)/(Ω·…), which is typically a positive power of the
  conductor (Assessment, standard heuristics). An ES point of p has naive height ≤ O(log p), since its
  coordinates (u₂u₃ : u₁u₃ : u₁u₂) are ≤ p^{O(1)}. So ĥ ≪ log p. The conductor of E_{4s/p} is p^{O(1)}, so ES
  points are **Lang-scale small points**: they sit at the conjectural *lower* limit of canonical heights. No rank,
  descent or Gross–Zagier statement controls the existence of a small point on a given curve. Siegel bounds
  integral points from above and gives no existence. (Assessment, robust.)
* **B1 (sections and identity families).** By P2 the generic MW group is torsion. Any base change N = N(t) that
  creates positive generic rank gives sections, i.e. polynomial families of rational points. Integral
  specialisations of such sections are polynomial identity families for ES. These are covered by POINTWISE_SIZE
  Thm C/M (they miss square classes / fail infinitely often under H).
* **B2.** Fix the fibre N, i.e. the sum s. The ES points on it are determined by divisor data of p-dependent
  integers (P4: the moduli are coordinates of the point). Per prime there are ≫ p² admissible fibres and
  ≍ log³p ES points, so each fibre is a lottery with expectation p^{−2+o(1)}. Any argument through a fixed finite
  set of fibres per p collapses (Thm 2.2(iii) shape).
* **B3.** Rank-1 generators would give one point per curve. Positive rank on a fibre is necessary but carries no
  main term.
* **B5 / T1.** At n = m² positive ES points exist (via ES(m)) and lie on positive-rank fibres too. Ranks, root
  numbers and Heegner data of C_N do not see whether the point is Type I/II, so the odd-square test is passed
  vacuously: nothing is produced.
* **B6 / T7.** Average-rank results over the family C_N (e.g. Bhargava-type bounds) are averages over N, i.e. over
  s and p. They say nothing for a single p.

## 5. Experiment
`scripts/bs_cubic_elliptic.py`:
* (1) 0 point-count mismatches;
* (2) Δ as above;
* (3) 441 points, torsion exactly the 28 with repeated u_i, among them none with p ≡ 1 (mod 4) (126 points).

## 6. Viability Assessment
**COLLAPSES** to integrality-vs-rationality (Lang-scale small points) and to B2 at the fixed-fibre step. The pencil
is an n-independent rational elliptic surface with I₆I₃I₂I₁ fibres and MW rank 0, so ES points are sporadic
rank-jump points, never specialisations of sections.

By-products:
* (PROVED) the fibre-type table P2 and MW rank 0;
* (PROVED) repeated-entry points are torsion; there are no repeated-entry solutions for p ≡ 1 (4);
* (EVIDENCE) the non-torsion property P3, which gives a cheap source of explicit rank ≥ 1 curves C_N. This is a
  curiosity, not a route.

Other genus-1 candidates: plane sections through P are nodal, hence genus 0. Fixing two of ET's coordinates gives
hyperbolas (redteam-2 Lemma 2.1), also genus 0. So the s-pencil, and its pencils of other hyperplanes with N
replaced by a weighted sum, is essentially the only genus-1 structure, and the screen above applies verbatim.

## Errata (triage O156/O157)

Appended by O160; the memo body above is unchanged. Source: reviews/triage-brainstorm-A.md (per-memo paragraph and
"Overclaims / mis-scopes" list). No computational counterexample is involved (scope/label corrections).

* **Under-claim in P3:** per-point non-torsion is fully PROVED for each tested point, not merely EVIDENCE: by Mazur a
  rational torsion point has order ≤ 12, so a chord–tangent check up to order 12 settles it. The memo's worry about
  ℤ/12 and ℤ/2×ℤ/6 concerns only a general proof for all p ≡ 1 (4).
