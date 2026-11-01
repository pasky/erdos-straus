# Z53_FORESTCLASS — class-group roots in the word forest F_p (FRONTIER §7.2)

ES is OPEN. Nothing here proves or disproves ES, ES₅ or any all-prime statement. Labels: PROVED / CONDITIONAL (on what) /
CERTIFIED (computer) / EVIDENCE / CONJECTURE / Assessment. All results are internally reviewed only.
Brief: `z52bbriefs/z53_depth.md`, lane FORESTCLASS (`z52bbriefs/z53_lanes.md`). Scripts `scripts/z53_forestclass_*`,
data `data/z53/forestclass/`.

**Status: CHECKPOINT 1 (skeleton).**

## 0. Setting and notation

* F_p: vertices 1, …, p + 2; u ≠ v adjacent iff uv | p + u + v. It is a forest; every edge {u < v} has u(u − 1) ≤ p + 1;
  for gcd(x, p) = 1 the neighbours of x are exactly v = (p + x)/D with D | p + x, D ≡ −1 (mod x), v ≠ x
  (`LOWER_TAIL_ASTRA.md` Lemma 2.1, `Z52D_PELLCYCLE.md` Lemmas 1.2–1.3, `FOREST_INVERSE.md` Cor C).
  Colour χ_p(v) = (v/p); for p ≡ 1 (4) a bichromatic edge is exactly a five-slice certificate (ES₅).
* Class-group root sets (all intersected with [1, √p + 1], which contains every small endpoint of an edge):
  * **SM(p)** = {a : −p is a square mod a} = the first coefficients a ≤ √p of the reduced forms (a, 2b, c) of
    discriminant −4p (one reduced form per class of Cl(−4p));
  * **SP(p)** = {a : p is a square mod a} = the Q-values ≤ √p of the union of all reduction cycles of discriminant 4p
    (`Z52D_PELLCYCLE.md` Prop 2.4, its "all-cycles" set);
  * **SMN(p)** = SM ∩ {χ_p = −1}: minima of reduced forms in the non-principal genus of Cl(−4p) (for odd a,
    χ_p(a) = χ_{−4}(a), the genus character);
  * **SQ** = perfect squares b² (the vertices whose forest neighbourhood *is* class-group data, Prop 3 below);
  * controls: ALL (every vertex) and NR (all non-residues).
* A root set R *hits* at p if some a ∈ R lies in a component of F_p containing a bichromatic edge; depth-d hit if the
  bichromatic edge is within d edges of a (the edge itself counts as 1).

## 1. Statements attacked (precise; labels)

**(S1) Class-group root statement CG_R** (R ∈ {SM, SP, SMN, SQ}): for every prime p ≡ 1 (mod 8), p > p₀, R(p) hits
(with unrestricted exploration; variants: depth ≤ 1, ≤ 2). (For p ≡ 5 (8) every set hits at the root 1 via the edge
{1, 2}.) CONJECTURE-shaped targets; tested CERTIFIED to 10⁸ and on hard primes / samples (§4).

**(S2) Kill target.** For which *bounded* class-group menus (ambiguous forms, genus minima, the K least reduced-form
minima of each genus, the first K elements of the orbit of a prime-ideal class, the K least non-residues) does
Dickson/H force every component meeting the menu to be monochromatic infinitely often? (Theorem 1 below: all of them.)

**(S3) Escape / dictionary.** Is full class-group data quasi-polynomial on any polynomial family (it is not:
Prop 2), and which part of the forest is *determined* by class-group data (exactly the square vertices: Prop 3)?

## 2. Why this is not already closed

Closed: fixed root sets {1..H} (LTA Thm 3.2), the single least-non-residue root (LTA Thm 5.1), the principal-cycle menu
R3 ∪ U (PELLCYCLE Thm 1.1), bounded coordinate lines (LOWERTAIL_ROUND2_FABLE Prop 3.3). PELLCYCLE §3.5/§4 explicitly
left open "the all-cycles (class-group) root set" (0 failures to 2·10⁷) and "arbitrary functions of cycle data". The
class groups of ±4p are p-dependent objects of size p^{1/2±o(1)} (Siegel), not frozen at near-squares (unlike the
principal cycle at m² + 1), so neither B1 Thm M nor the PELLCYCLE freezing applies to them as a whole; and SMN supplies
canonical *non-residue* roots, the thing LTA's root-1 menu lacks.

## 3. First results (checkpoint)

**Theorem 1 (CONDITIONAL on Dickson; proof drafted, §5).** For all H ≥ 3, K ≥ 1 there are infinitely many primes
p ≡ 1 (mod 24) at which every component of F_p meeting {1, …, H} ∪ {the K least quadratic non-residues mod p} is
monochromatic. The construction makes ℓ(p) = q a prime ≡ 3 (mod 4) and every other prime < qK + 2 a residue, so the
menu contains: the ambiguous forms' minima 1, 2; both genus minima 1, q of Cl(−4p); the least elements of SM, SP up to
H; the least elements q·s (s ≤ K, −1 □ mod s) of SMN; the first orbit elements ℓ, ℓ², … (ℓ^k ≤ H) of a split prime
ideal class. So every *bounded* class-group root menu of these types fails i.o. under Dickson. Extends LTA Thms
3.2 + 5.1 (K = 1, no H) to K non-residue roots plus fixed roots.

**First falsifier (CERTIFIED, census of all 165 976 primes p ≡ 1 (8) ≤ 10⁷; engine cross-checked against an
independent brute force on 1 607 n, 0 mismatches):**

| root set | full-component failures ≤ 10⁷ | depth ≤ 2 failures | depth ≤ 1 failures |
|---|---:|---:|---:|
| ALL | 0 | 0 | 0 |
| SP (all cycles of 4p) | 0 | 0 | 0 |
| SM (reduced forms of −4p) | **1** (p = 19441) | 1 | 6 |
| SMN (non-principal genus of −4p) | **34** (193, 457, 1873, 2377, 2521, 3361, 9601, …, 9451513) | 34 | 37 |
| SQ (squares) | 176 | 1007 | 3510 |

So the class-group root statement is *false at finite p* for SM (19441) and SMN (34 primes, also 2521 and 3361), and
SP's success comes from its small, congruence-determined elements (4, 8, 3, … ∈ SP whenever p ≡ 1 mod 24), which
Theorem 1 freezes. Census 10⁷–10⁸ running.

## 4. Plan
* Proof of Theorem 1 in full + CERTIFIED instances (small H, K) with whole-forest verification.
* Prop 2 (escape, PROVED rel. Siegel): |CGmin(p)| ≥ h(−4p)·p^{−o(1)}; no finite union of polynomial form families covers
  more than O(1) classes along a polynomial family.
* Prop 3 (dictionary, PROVED): neighbours of the square vertex b² ↔ forms (A, 2b, C) of discriminant −4p with
  A ≡ −1 (mod b²); the edge colour is the genus character; for general a ∈ SM the neighbourhood of a is factorisation
  data of p + a = a(c + 1) − b², which is *not* class-group data of −4p.
* Stratified per-root enrichment (does SM/SP membership raise the chance of lying in a bichromatic component beyond
  colour, a mod 8 and size?), 10⁸ census, samples at 10⁹–10¹², hard primes, near-square and odd-square controls.
