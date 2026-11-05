# Z58_MORDELL — Mordell's classes for (★): sterile 1-points, the genus blind spot, and no algebraic use of x² + 840y² (narrowed)

Status: z58 lane MORDELL (brief `z52bbriefs/z58_lanes.md` §MORDELL, rules `z52bbriefs/z53_depth.md` with z53 → z58).
Internal. One hostile internal review was applied (§8, `data/z58/mordell/internal_review.md`: 1 FATAL, 6 MAJOR, 5 MINOR).
**ES is OPEN; nothing here proves or disproves ES, (★) or (MS).** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE /
CONJECTURE / Assessment. Scripts `scripts/z58_mordell_*`, data `data/z58/mordell/` (< 1 MB, README there).
Verdict: **narrowed** (no HOT LEAD).

Notation.
* R(n) = #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n}.
* For d ≡ 3 (mod 4), H_d = {−k mod d : k | (d+1)/4}. By Z57_SYNTH Lemma A.1, R(n) = #{d : n mod d ∈ H_d}.
* K_{u,B} := {n ≡ −(u + B) (mod 4uB)}: the fixed-(u,B) family, every n ≥ 1 in it has the solution
  (u, B, (n + u + B)/(4uB)).
* 𝔐 = {1, 121, 169, 289, 361, 529} = the unit squares of (ℤ/840)^×.
* M_gen = the genus part of R (Z56_FAMDESIGN §1): M_gen(p) = Σ_{(o,e)} 2(s(q)/φ(q))·1[−p(o+e) ∈ ((ℤ/q)^×)²], q = 4oe,
  over the pairs with 4oe − o − e ≤ p. X = R − M_gen, L = log p, c_V = 5/(4π²) ≈ 0.12665.
* A *profinite point* is x ∈ ℤ̂^×. "x ∈ H_d" means x mod d ∈ H_d, and similarly for K_{u,B}.
* x is *H-sterile* if it lies in no H_d, *B-sterile* if it lies in no K_{u,B}, and *(★)-sterile* if both.

## 0. Summary

1. **Lemma P (PROVED).** A one-parameter polynomial (★) family (U, B, C polynomial in t with 4UBC − U − B = a + Mt) has
   two constant coordinates. So the finite (★) "Mordell-type case splits" are exactly finite unions of classes H_d and
   K_{u,B}.
2. **Theorems S1, S3 and Corollary S2 (PROVED; CERTIFIED cross-checks).** Let x_{ℓ,R} be the point that is R at ℓ and 1
   at every other prime.
   * S1: exact criterion for H-sterility.
   * S3: a K_{u,B}-hit forces v_ℓ(4uB) = 1 and R ≥ (2ℓ − 1)/3.
   * Hence x_{ℓ,R} is (★)-sterile for every 1 ≤ R ≤ (ℓ − 1)/2.
   * S2: no finite (★) case split covers any class {p ≡ 1 (mod M), p ≡ R (mod ℓ)} with ℓ ∤ M and R a non-residue
     ≤ (ℓ − 1)/2. Infinitely many primes there escape every finite menu.
   * This applies to the class 1 mod 840 only. The other five Mordell classes need points with non-trivial 5-/7-adic
     entries; they are **open** (H-menu EVIDENCE only).
   * The review's counterexample shows the H-menu alone is not the right notion: x_{11,7} is H-sterile, yet every
     p ≡ 1 (1680), p ≡ 7 (11) lies in K_{4,11}.
3. **Lemma O (PROVED, cutoff version).** At a common cutoff X, the genus sum M_gen,X(p) is the same function of
   ((p/q))_{11 ≤ q} on all six Mordell classes. The six classes are separated only by characters of order ≥ 3 (the
   quartic character mod 5, the cubic mod 7).
   * Assessment: the class-to-class differences inside 𝔐 are therefore X-effects. This is a reading, not a theorem
     about prime statistics.
   * Data on [10⁷, 10⁸]: class means of R/L² are 0.1199 (class 1) … 0.1279 (class 529); the Mordell mean is 0.1246, the
     non-Mordell mean 0.1662 (EVIDENCE).
4. **Sterile non-residues behave much more like residues than like hit non-residues (EVIDENCE).**
   * At q = 5, 7 (all primes ≡ 1 (4)): the sterile non-residues 2 mod 5 and 3 mod 7 have mean R/L² 0.152 and 0.156,
     in the residue range 0.150–0.175. The hit non-residues have 0.165–0.187 and essentially no low-R primes.
   * Inside 𝔐 at ℓ = 11, …, 23 (label = 1-point status for the full menu): sterile-non-residue means are 0.1209–0.1242
     against residue means 0.1174–0.1229 and hit means 0.1329–0.1412. Sterile sits 0.0007–0.0064 above QR (measurable)
     but 0.009–0.019 below hit.
   * Primes with R ≤ 4: about 2–3 per 10⁴ in QR, 0–2.3 in sterile, 0–1.0 in hit classes.
   * The genus variable (the quadratic character) cannot see this split.
5. **"L6(0) holds on 𝔐" is largely the genus term's blind spot (CERTIFIED numbers + Assessment).**
   * All 9 Mordell-class (★)-zeros have M_gen < c_V L² (ratio 0.084–0.115), so L6(0) holds *at these zeros*.
   * Six of the seven L6(0) violators of SYNTH §2.3 lie in classes mod 840 (241, 409, 577) where p is a sterile
     non-residue mod 7 and/or 5.
6. **M2, the representation p = x² + 840y² (Prop C1, PROVED).** A global polynomial (★) certificate for x² + 840y² has
   two constant coordinates, hence is a fixed-modulus congruence condition on p. Global polynomial identities in the
   coordinates (x, y) add nothing beyond p's residue class. Other uses of (x, y) are not excluded.
7. **Coverings at 840·ℓ (CERTIFIED, bounded menus).**
   * ES menu: 34 / 40 / 52 uncovered classes at 9240 / 10920 / 14280, of which 4 are non-squares at each level.
   * Full one-parameter (★) menu: 11 classes mod 840 (the p ≡ 1 (8) half of the 22 left by the H-menu alone); 44 of
     the 60 Mordell lifts mod 9240.

## 0′. MANDATORY FALSIFIER TABLE (committed at checkpoint 1; updated after review)

Here M1 means finite (★) case splits and sterility (§§2–4), and M2 means certificates built from the coordinates of
p = x² + 840y² (§5). Neither mechanism claims positivity. Both are scoped no-goes plus a descriptive/structural
reading, so the screens test the honesty of the scope rather than a proof.

| screen | M1 (Lemma P, Thms S1/S3, Cor S2, §3 reading) | M2 (Prop C1) |
|---|---|---|
| **F1 odd squares** | Squares lie in no H_d (Jacobi, SYNTH A.1(b)) and in no K_{u,B} (since R(m²) = 0). S1/S3 exhibit *non-square* (★)-sterile points, so the no-go goes strictly beyond T1. | *Some* odd squares in 𝔐-classes have representations with y ≠ 0 (29² = 1 + 840·1²); not all do (11² = 121 has none). Prop C1 reduces global polynomial certificates to congruence certificates, which contain no squares. Uniqueness of the representation is *one* conceivable primality input, but it is not a primality characterisation: 122089 = 11²·1009 has a single representation 143² + 840·11² (review). |
| **F2 C-even sub-line** | A no-go only strengthens on a sub-family: (★)-sterile points are sterile for the C-even sub-menu. The descriptive reading does not separate C parity. The four Mordell R₈-zeros above 10¹⁰ have (n_p, p mod n_p) = (23, 10), (19, 3), (29, 10), (13, 5); all four 1-points are (★)-sterile. | No positivity argument; nothing to separate. |
| **F3 composites** | Coverings are blind to primality: sterile points are limits of composites and primes alike. That is why Cor S2 holds. | Composites with one or with several representations both exist; no rule was built. |
| **F4 known zeros** | All 14 (★)-zeros lie in the 11 classes mod 840 uncovered by the full one-parameter (★) menu, as they must; all 38 𝔊*-zeros lie in the 22 H-menu survivors. All 9 Mordell (★)-zeros have (n_p, p mod n_p) at a (★)-sterile 1-point residue. No positivity is claimed. | Not applicable (no rule). |

**No HOT LEAD.**

## 1. Precise statements attacked

**(MS)** (Z57_SYNTH §1.1): every prime p > 10¹⁷ with p mod 840 ∈ 𝔐 has R(p) ≥ 1.

**Q1 (finite case split).** For ℓ ≥ 11 prime, r ∈ 𝔐 and R a non-residue mod ℓ: is Σ(r, ℓ, R) := {p ≡ r (840),
p ≡ R (ℓ)} contained (for all large p) in a finite union of one-parameter (★) families?
* By Lemma P these families are the classes H_d and K_{u,B}, all clopen in ℤ̂.
* A clopen avoidance argument plus Dirichlet shows: a (★)-sterile point in the unit part of the closure of Σ forces
  infinitely many primes of Σ outside any finite menu (Cor S2).
* A "yes" would remove Σ from (MS) by a Mordell-type identity; a "no" is a scoped no-go.

**Q2 (structure).**
* Which small-d hit classes does the 840-structure close?
* What does it do to M_gen and to X?
* Why is the uniform diagnostic L6(0) violated only off 𝔐?

**Q3 (M2).** Can the representation p = x² + 840y² of a Mordell prime be turned into a (★) witness?

*Why not already closed.*
* For the full ES identity menu, Q1 is the POINTWISE_MORDELL / MORDELL13B–E line (`CAMPAIGN_SUMMARY.md` §(H)34).
* For HC certificates (a larger family), `Z55_HCF.md` T3.1 / C3.2 proves sterility of x_{ℓ,R} for R < (ℓ − 1)/3.
* `Z56_FAMTRY.md` Prop 2.2 handles R = 1.
* NONCONG_LIFTS Thm 2.6 handles R = 2 for the fixed-slice ES witness classes (and its R267 repair notes that
  x_{11,2} ∈ {n ≡ 79 (mod 143)} for the full ES menu).
* The exact (★) answer at 1-points (both menus), the class-by-class data on sterility, and Q3 have no prior memo. For
  Q3, git grep finds only the observation itself (`ES_CONNECTIONS_TODO.md` Z0935).

## 2. Q1: (★)-sterility of the 1-points

**Lemma P (PROVED).** Let a, M be integers, M ≥ 1. If U, B, C ∈ ℚ[t] \ {0} satisfy 4UBC − U − B = a + Mt identically,
then two of U, B, C are constant.
*Proof.* Let the degrees be α, β, γ.
* If two of them are positive, the top part of 4UBC (degree α + β + γ ≥ 2) exceeds the degrees of U + B and of a + Mt,
  a contradiction. ∎
*Consequence.* The fixed coordinates give:
* (U, C) fixed: n ≡ −U (mod 4UC − 1), i.e. a class of H_{4UC−1};
* (B, C) fixed: the mirror, again a class of H_d;
* (U, B) fixed: K_{U,B}.
So the integral positive one-parameter (★) families are exactly the classes H_d and K_{u,B}.

For an odd prime ℓ and 1 ≤ R ≤ ℓ − 1, x_{ℓ,R} denotes the point with x_ℓ = R and x_q = 1 for q ≠ ℓ. It lies in the
closure of {p ≡ 1 (mod M), p ≡ R (mod ℓ)} for every M with ℓ ∤ M.

**Theorem S1 (H-menu; PROVED).** x_{ℓ,R} lies in some H_d iff one of the following holds:
* **(direct)** ℓ ≡ 3 (mod 4) and (ℓ − R) | (ℓ + 1)/4; then d = ℓ.
* **(j-family)** there is j ≥ 1 with D_j := ℓj − (j + 1)R ≥ 1, D_j | ℓ + j + 1 and 4 | (ℓ + j + 1)/D_j. Put
  C := (ℓ + j + 1)/(4D_j) and t := (4CR + 1)/ℓ (an integer, see step 7), and require m := 4C − t to be prime to ℓ.
  Then d = ℓm.
  * Necessarily j ≤ (ℓ + 4R + 1)/(4(ℓ − R) − 1), because 4D_j ≤ ℓ + j + 1.

In particular x_{ℓ,R} is H-sterile for every 1 ≤ R ≤ (ℓ − 1)/2.

*Proof.* Suppose x := x_{ℓ,R} ∈ H_d. Then x ≡ −k (mod d) with k | (d + 1)/4; write d + 1 = 4kC and d = ℓ^a m with ℓ ∤ m.
1. *a = 0 is impossible.* Then −k ≡ 1 (mod d), and 1 ≤ k < d forces k = d − 1 > (d + 1)/4.
2. *Reduction.* Mod m: 4kC ≡ 1 and k ≡ −1 give m | 4C + 1. Mod ℓ^a: 4kC ≡ 1 and k ≡ −R give ℓ^a | 4CR + 1. Put
   t := (4CR + 1)/ℓ^a ∈ ℕ.
   * Conversely, let a ≥ 1, C ≥ 1 and m ≥ 1 with ℓ ∤ m, m | 4C + 1, ℓ^a | 4CR + 1 and 4C | ℓ^a m + 1. Then
     k := (ℓ^a m + 1)/(4C) satisfies k ≡ −1 (mod m) and k ≡ −R (mod ℓ^a). So x ∈ H_d with d = ℓ^a m = 4kC − 1.
3. *The shape of m.* Since ℓ^a t = 4CR + 1 ≡ 1 (mod 4C), the condition 4C | ℓ^a m + 1 is equivalent to m ≡ −t (mod 4C).
   * R ≤ ℓ − 1 gives t ≤ (4C(ℓ − 1) + 1)/ℓ < 4C. With 1 ≤ m ≤ 4C + 1, either m = 4C − t, or t = 4C − 1 and
     m ∈ {1, 4C + 1}.
   * If m = 4C − t, then m | 4C + 1 ⟺ (4C − t) | (t + 1), because 4C + 1 = (4C − t) + (t + 1). So t + 1 = j(4C − t)
     for some j ≥ 1.
4. *a ≥ 2 is impossible.* Here t ≤ (4C(ℓ − 1) + 1)/ℓ² ≤ 8C/9 + 1/9, since (ℓ − 1)/ℓ² ≤ 2/9.
   * Then 2t + 1 ≤ 16C/9 + 11/9 < 4C, so 4C − t > t + 1 and no j exists.
   * Also t < 4C − 1.
5. *a = 1.* If t = 4C − 1, then 4C(ℓ − R) = ℓ + 1. This is the direct condition: m = 1 gives d = ℓ and k = ℓ − R.
   * Otherwise t = (4Cj − 1)/(j + 1), and ℓt = 4CR + 1 becomes 4C·D_j = ℓ + j + 1: the j-family.
   * If ℓ | m, then v_ℓ(d) ≥ 2, which step 4 excludes.
6. *Small R.* If R ≤ (ℓ − 1)/2, then t ≤ (2C(ℓ − 1) + 1)/ℓ < 2C, so t + 1 ≤ 2C < 4C − t (no j), and t = 4C − 1 is
   impossible. With steps 1 and 4, no d exists.
7. *Converse integrality (review finding 9).* From 4CD_j = ℓ + j + 1 we get (j + 1)(4CR + 1) = ℓ(4Cj − 1).
   * Suppose ℓ | j + 1, say j + 1 = hℓ, and put δ = ℓ − R ≥ 1. Then 4C(hδ − 1) = h + 1 with hδ > 1.
   * For δ = 1 (so h ≥ 2) the left side is ≥ 4(h − 1) > h + 1; for δ ≥ 2 it is ≥ 8h − 4 > h + 1. Contradiction.
   * So ℓ ∤ j + 1, t = (4CR + 1)/ℓ is an integer, m = 4C − t = (4C + 1)/(j + 1) > 0 divides 4C + 1, and step 2's
     converse applies. ∎

**Theorem S3 (B-menu; PROVED).** If x_{ℓ,R} ∈ K_{u,B}, then v_ℓ(4uB) = 1 and R ≥ (2ℓ − 1)/3. In particular x_{ℓ,R}
is B-sterile for R ≤ (ℓ − 1)/2. (R = 1 is excluded separately: no K_{u,B} contains the point 1, since
4uB > u + B + 1.)
*Proof.* Put S = u + B, a = v_ℓ(4uB) and w = 4uB/ℓ^a.
* x ∈ K_{u,B} means x ≡ −S modulo 4uB. Since x is 1 away from ℓ, this is: w | S + 1 and ℓ^a | S + R.
  * a = 0 is impossible: then 4uB | S + 1 ≤ 4uB − 2.
  * Put s := (S + 1)/w ∈ ℕ, so that 4uBs = ℓ^a(S + 1). This relation is symmetric in u and B.
* *ℓ divides both u and B.* Then ℓ | S, so ℓ | R; impossible.
* *v_ℓ(B) = a ≥ 1, ℓ ∤ u* (the case v_ℓ(u) = a is symmetric). Write B = ℓ^aB′. Then 4uB′s = S + 1, and
  ℓ^a | S + R gives u ≡ −R (mod ℓ^a), so u ≥ ℓ^a − R. Also B′(4us − ℓ^a) = u + 1.
  * If 4us − ℓ^a ≤ 0, the left side is ≤ 0 < u + 1, impossible.
  * So 4u − ℓ^a ≤ 4us − ℓ^a ≤ u + 1, i.e. u ≤ (ℓ^a + 1)/3.
  * Combined with u ≥ ℓ^a − R this gives R ≥ (2ℓ^a − 1)/3.
  * Since R ≤ ℓ − 1, this forces a = 1 and R ≥ (2ℓ − 1)/3. ∎

**Corollary S2 (PROVED, from P, S1, S3 and Dirichlet).** Let ℓ be an odd prime, M ≥ 1 with ℓ ∤ M, and R a non-residue
mod ℓ with x_{ℓ,R} (★)-sterile (e.g. any non-residue R ≤ (ℓ − 1)/2). Then every finite union U of classes H_d and
K_{u,B} misses infinitely many primes p ≡ 1 (mod M), p ≡ R (mod ℓ).
*Proof.* U is a finite union of residue classes, hence clopen, and x_{ℓ,R} ∉ U. So some unit class c mod ℓ^b·M′ around
x_{ℓ,R} (with M | M′, ℓ ∤ M′, c ≡ 1 (M), c ≡ R (ℓ)) is disjoint from U. Dirichlet gives infinitely many primes in it. ∎
With M = 840 and ℓ ≥ 11: no finite (★) case split removes {p ≡ 1 (840), p ≡ R (ℓ)} from (MS), for any non-residue
R ≤ (ℓ − 1)/2.

*Checks (CERTIFIED, bounded).*
* S1 criterion against brute force for every odd ℓ < 60 and every R, testing all d ≤ 3·10⁴: 0 mismatches
  (`z58_mordell_sterile2.py 30000 60`, `sterile2_d3e4.txt`). The review independently reran it and checked the
  criterion with the exact j bound for all odd ℓ < 1000.
* S3 against an exhaustive (a ≤ 2) parametrised enumeration and a direct scan of all pairs with 4uB ≤ 2·10⁵, for
  ℓ < 60: 0 violations, and no residue missed by the enumeration (`z58_mordell_sterileB.py 60 2 200000`,
  `sterileB.txt`).
* Non-sterile 1-point residues (H ∪ B), all of them non-residues > ℓ/2:
  * ℓ = 11: {7, 8, 10};
  * ℓ = 13: {8, 11};
  * ℓ = 17: {11, 12};
  * ℓ = 19: {14, 15, 18};
  * ℓ = 23: {15, 17, 20, 21, 22}.
  The review's counterexample is (4, 11) ∈ K at ℓ = 11, R = 7 = (2ℓ − 1)/3, the S3 boundary.

*The other five Mordell classes (open).*
* Their natural points have x_5 ∈ {1, 4} and x_7 ∈ {1, 2, 4} as well. For the **H-menu only**, brute force with
  d ≤ 3·10⁴ leaves between 2/5 (ℓ = 11) and 7/8 (ℓ = 17) of the non-residues unhit (`sterile2_d3e4.txt`; EVIDENCE).
* The B-menu and proofs were not done there. Q1 for r ≠ 1 is open.

*Novelty (Assessment).* S1 + S3 give the exact (★) answer at the 1-points: a small, clean increment over FAMTRY (R = 1),
HCF (R < (ℓ − 1)/3, larger family, hence a stronger statement on its range) and NONCONG (R = 2, fixed-slice ES witness
classes). It is a covering statement (B1).

## 3. Q2: what the 840-structure does

### 3.1 Closing of small d (PROVED; known in substance)

**Lemma G0.** If p ≡ 1 (mod 4) is prime and p ∈ H_d, then (d/p) = −1. So d has a prime factor q with (q/p) = −1 to an
odd power.
*Proof.* SYNTH A.1(b) gives (p/d) = −1 (Jacobi), and reciprocity gives (p/d) = (d/p) for p ≡ 1 (4). ∎
On 𝔐, (q/p) = 1 for q = 3, 5, 7, and d is odd, so every 7-smooth d is closed and every H-witness has d ≥ n_p ≥ 11.

**Lemma G (PROVED).** Let q be an odd prime, d ≡ 3 (mod 4) with q | d, N := (d + 1)/4, and S_q(N) := Σ_{k|N} (k/q).
Then for ε = ±1, #{h ∈ H_d : (h/q) = ε} = (τ(N) + ε(−1/q)S_q(N))/2, and S_q(N) ≥ 0.
*Proof.* h = −k with k | N, so (h/q) = (−1/q)(k/q); q ∤ N since 4N ≡ 1 (mod q). S_q is multiplicative with local
factors 1 + χ(ℓ) + … + χ(ℓ)^e ≥ 0. ∎
*Reading.*
* For p with (p/q) = +1, only the (h/q) = +1 part of H_d is available. It is the smaller part at q = 3, 7
  ((−1/q) = −1) and the larger part at q = 5.
* The imbalance S_q(N) stays bounded on average, while τ(N) grows on average, so the effect is a relative 1/log one, in
  line with the 1/L class term of `RESIDUE_HARDNESS.md` (prior, more complete).
* The precise conditional mean of S_q(N) on the class N ≡ 4⁻¹ (mod q) is not used here.

### 3.2 Lemma O: the six classes are separated only by order-≥3 data (PROVED, cutoff version)

**Lemma O.** For X > 0 let M_gen,X(p) be the genus sum over pairs with 4oe − o − e ≤ X. There is a function Φ_X of the
signs (ε_q)_{11 ≤ q ≤ (X+1)/3}, the same for all six classes, such that M_gen,X(p) = Φ_X(((p/q))_q) for every prime
p > (X + 1)/3 with p mod 840 ∈ 𝔐. (Pairs with 4oe − o − e ≤ X have o, e ≤ (X + 1)/3; M_gen(p) = M_gen,p(p).)
*Proof.*
* Each weight W(o, e) = 2(s(q)/φ(q))·1[−p(o + e) is a square unit mod 4oe] depends on p only through the class of p in
  (ℤ/4oe)^×/squares.
* By CRT that class is determined by the 2-adic square class of p, which for units is p mod 8 (the unit squares mod 2^a,
  a ≥ 3, are exactly the units ≡ 1 (8)), and by (p/q) for the odd primes q | oe.
* Every r ∈ 𝔐 is ≡ 1 (8) and a square mod 3, 5 and 7. ∎
*Reading (Assessment, downgraded after review).*
* Lemma O does not say that M_gen has the same values or the same empirical law on the primes of the six classes: sizes
  and the joint distribution of the characters vary. So "all class differences live in X" is a heuristic reading,
  supported by the data below, not a theorem.
* The characters of (ℤ/840)^× that separate the six classes are exactly those non-trivial on the squares, i.e. of order
  ≥ 3: the quartic character mod 5 and the cubic character mod 7.

*Data (EVIDENCE; `scripts/z58_mordell_classstats.c`, `classstats_1e8.txt`; the review reproduced both files
byte-for-byte).* Exact R(p) for all primes p ≡ 1 (4) ≤ 10⁸. Mean R/L² on [10⁷, 10⁸], about 26 500 primes per class:
* Mordell classes: 1: 0.1199, 361: 0.1227, 121: 0.1236, 289: 0.1266, 169: 0.1272, 529: 0.1279. The eight lowest of the
  96 classes are these six plus 337 (0.1261) and 577 (0.1280).
* Weighted means: Mordell 0.1246, non-Mordell 0.1662.
* Per-class standard deviations of R/L² are 0.038–0.042 (review), so standard errors are ≈ 0.00025. The spread 0.008
  inside 𝔐 is ≈ 30 standard errors.
* The p ≡ 1 (mod 5) classes (1, 361, 121) form the harder half. This matches the "p ≡ 1 (mod q)" effect of
  RESIDUE_HARDNESS Lemma 2 (prior).
* Zeros ≤ 10⁸ by class: class 1 has 3, 361 has 3, 529 has 2, 289 has 1, 121 and 169 have 0. These counts are too small
  to rank the classes.

### 3.3 Marginal class effects mod 3, 5, 7 (EVIDENCE)

Primes p ≡ 1 (4), p > 7, aggregated from `classstats_1e8.txt`; means over [10⁷, 10⁸], zero and R ≤ 4 counts over
p ≤ 10⁸. "Sterile" and "hit" refer to the 1-point x_{q,R} for the full one-parameter menu.

| p mod q | mean R/L² | zeros | #R ≤ 4 |
|---|---|---|---|
| 3: 1 / 2 (hit, d = 3) | 0.148 / 0.179 | 14 / 0 | 268 / 5 |
| 5: 1, 4 (QR) / 2 (QNR, sterile) / 3 (QNR, hit at d = 15) | 0.162, 0.175 / **0.152** / 0.165 | 7, 5 / **2** / 0 | 108, 108 / **52** / 5 |
| 7: 1, 2, 4 (QR) / 3 (QNR, sterile) / 5, 6 (QNR, in H_7) | 0.150, 0.152, 0.158 / **0.156** / 0.179, 0.187 | 4, 1, 5 / **4** / 0, 0 | 91, 66, 55 / **55** / 3, 3 |

The sterile non-residue (2 mod 5, 3 mod 7) behaves like a residue class; the hit non-residues are "easy". A genus
(quadratic-character) model treats all non-residues mod q alike.

### 3.4 Inside 𝔐: sterile vs hit non-residues at ℓ = 11, …, 23 (EVIDENCE)

`scripts/z58_mordell_bymod.py`, output `bymod_1e7_1e8.txt`: 158 955 Mordell-class primes in [10⁷, 10⁸]. The label is
the 1-point status for the full menu (H ∪ B). It is exact only for class 1 and a proxy for the other five. For example,
the B-hit K_{4,11} at R = 7 mod 11 also needs p ≡ 1 (mod 16), which only half of the Mordell primes satisfy.

| ℓ | QR: mean (se), #R≤4 per 10⁴ | QNR sterile: mean (se), per 10⁴ | QNR hit: mean (se), per 10⁴ |
|---|---|---|---|
| 11 | 0.1174 (0.00014), 3.2 | 0.1238 (0.00021), 0.0 | 0.1372 (0.00019), 1.0 |
| 13 | 0.1211 (0.00014), 3.0 | 0.1223 (0.00017), 1.1 | 0.1397 (0.00024), 0.0 |
| 17 | 0.1229 (0.00014), 2.0 | 0.1242 (0.00016), 2.3 | 0.1329 (0.00028), 0.0 |
| 19 | 0.1209 (0.00014), 2.4 | 0.1221 (0.00017), 1.9 | 0.1411 (0.00025), 0.4 |
| 23 | 0.1202 (0.00014), 2.8 | 0.1209 (0.00019), 1.8 | 0.1388 (0.00021), 0.0 |

*Reading.*
* Sterile non-residue classes sit 0.0007–0.0064 above the residue classes. This is measurable (≈ 3–25 standard errors),
  so they are *not* indistinguishable.
* But they sit 0.009–0.019 below the hit classes, so they are much closer to residue classes than to hit classes.
* Low-R primes are rarest in the hit classes: 6 of ≈ 1.6·10⁵ hit-labelled primes have R ≤ 4, five of them at the proxy
  class 7 mod 11 and one at 15 mod 19 (21 106 849, R = 4).
* So the quadratic character of p mod ℓ is a poor predictor of hardness, and the 1-point sterility label is a good one.

*Zero lookups (CERTIFIED).*
* The nine Mordell (★)-zeros have (n_p, p mod n_p) = (13, 5), (13, 7), (13, 2), (23, 19), (23, 11), (13, 6), (19, 13),
  (11, 2), (17, 5).
* The four Mordell R₈-zeros above 10¹⁰ have (23, 10), (19, 3), (29, 10), (13, 5).
* All of these are (★)-sterile 1-point residues. This is a consistency check, not an independent test.

**Uncovered classes mod 840 (CERTIFIED; `z58_mordell_cover.py 840 star|starH`).**
* With H_d, d | 840, alone, 22 classes ≡ 1 (4) are uncovered.
* Adding the K_{u,B} with 4uB | 840 removes the eleven with p ≡ 5 (8), e.g. via K_{1,2} (SYNTH / FAMTRY Prop 2.1). This
  leaves 11 classes, A_840 = {1, 121, 169, 241, 289, 337, 361, 409, 457, 529, 577}.
* A_840 consists of the classes with p ≡ 1 (24), p mod 5 ∈ {1, 2, 4} and p mod 7 ∈ {1, 2, 3, 4}, except
  (p mod 5, p mod 7) = (2, 4). That class is covered by d = 35, a joint effect of two individually sterile coordinates.
* All 14 (★)-zeros lie in A_840 (forced). All 38 𝔊*-zeros lie in the 22 H-survivors (consistency check).
* The five non-Mordell (★)-zeros lie in classes 409, 577, 337, 241: sterile non-residues 3 mod 7 or 2 mod 5. This is why
  5 of the 14 zeros lie outside Mordell's classes.

### 3.5 Why L6(0) "holds on 𝔐 and fails off 𝔐" (CERTIFIED numbers, Assessment reading)

L6(0) at p means X(p) ≥ −c_V L², i.e. R(p) ≥ M_gen(p) − c_V L². It holds automatically wherever M_gen(p) < c_V L².
* **At zeros.** `z56_famdesign_mgen.c` (audited in z56) on the 34 distinct (★)- and 𝔊*-zeros above 10³
  (`mgen_zeros.txt`):
  * all nine Mordell (★)-zeros have M_gen/L² ∈ [0.084, 0.115] < c_V, so L6(0) holds at them;
  * 18 of the 20 Mordell 𝔊*-zeros are below c_V (exceptions 1 105 441 and 564 661 441);
  * 13 of the 14 non-Mordell zeros above 10³ are above c_V (exception 23 929).
* **Samples near 10⁸** (inputs documented in the data README):
  * 96 Mordell primes: M_gen/L² ∈ [0.109, 0.140], mean 0.127, 44 of 96 below c_V;
  * 96 non-Mordell primes ≡ 1 (4): ∈ [0.133, 0.196], mean 0.153, none below c_V.
* **The violators.** Six of the seven L6(0) violators of SYNTH §2.3 (classes 241, 577, 409, 241, 577, 409) are in
  A_840 \ 𝔐: p is a sterile non-residue mod 7 (3 mod 7) and/or mod 5 (2 mod 5). M_gen sees only (p/7) = −1 or
  (p/5) = −1 there, while §3.3 shows that these classes carry roughly residue-class mass. The seventh violator,
  12 252 497 ≡ 257, is p ≡ 2 (3) with R = 8.

*Reading (Assessment).*
* The η = 0 diagnostic is not evidence that X behaves better on 𝔐. On 𝔐 the 840 characters contribute no genus mass,
  so M_gen is lower and the diagnostic is often automatically satisfied, even at zeros.
* Off 𝔐, the hard primes sit at sterile non-residues, where the genus term credits non-residue mass that the actual hit
  classes do not deliver.
* A uniform lower bound for X stated against a genus main term inherits this blind spot.

## 4. Coverings at 840·ℓ (CERTIFIED, bounded menus)

`scripts/z58_mordell_cover.py L {es|star|starH}` marks every unit class mod L lying in a complete class of a family with
modulus dividing L:
* `es`: the ET-shaped menu of `BRAINSTORM/y7_mordell_levels.md`;
* `star`: H_d and K_{u,B};
* `starH`: H_d only.
Only classes ≡ 1 (mod 4) are counted.

| L | ES: uncovered (squares + non-squares) | full (★): Mordell lifts uncovered (non-squares) | H only: same |
|---|---|---|---|
| 840 | 6 (6 + 0) | 6 of 6 (0) | 6 of 6 (0) |
| 9240 = 840·11 | 34 (30 + 4: 2041, 2521, 3361, 5161) | 44 of 60 (14) | 48 of 60 (18) |
| 10920 = 840·13 | 40 (36 + 4) | 54 of 72 (18) | 58 of 72 (22) |
| 14280 = 840·17 | 52 (48 + 4) | 80 of 96 (32) | 88 of 96 (40) |
| 15960 = 840·19 | — | 90 of 108 (36) | 90 of 108 (36) |
| 19320 = 840·23 | — | 108 of 132 (42) | 108 of 132 (42) |

* The ES column reproduces y7 (34 at 9240).
* For the four ES non-squares mod 9240, one further prime factor q ∈ {2, 3, 5, 7, 11, 13, 17, 19} never covers all lifts
  (`z58_mordell_refine.py`). This is a bounded menu result, not a sterility proof: for the full ES menu even x_{11,2} is
  covered (NONCONG R267, modulus 143). That line is POINTWISE_MORDELL's.
* Covered (★) lifts are not simply "p mod ℓ in the 1-point hit set": composite moduli (e.g. d = 455, 119) cover some
  sterile-labelled lifts of the classes r ≠ 1, and some hit-labelled lifts of r ≠ 1 stay uncovered at this level
  (review finding 2).

## 5. Q3 / M2: the representation p = x² + 840y²

*Fact (classical; re-verified in the campaign to 10⁶, `ES_CONNECTIONS_TODO.md` Z0935; the review checked all 2370
Mordell primes ≤ 10⁶ and found the 16 reduced forms of discriminant −3360).*
* 840 is idoneal, so a prime p is x² + 840y² iff p mod 840 ∈ 𝔐, and then (x, y) is unique up to signs.
* (x, y) mod q carries Frobenius data in ring class fields of ℚ(√−210) (non-abelian over ℚ).

**Proposition C1 (PROVED).** Let f ∈ ℤ[x, y] have degree 2 with top form f₂ irreducible over ℚ (e.g. f = x² + 840y²).
If U, B, C ∈ ℚ[x, y] \ {0} satisfy 4UBC − U − B = f identically, then at least two of U, B, C are constants.
*Proof.* Let the degrees be α, β, γ. The top homogeneous part of 4UBC is 4U_αB_βC_γ ≠ 0, of degree α + β + γ.
* If α + β + γ > max(α, β, 2), that top part must vanish: contradiction.
* If α + β + γ = 2 with two degrees equal to 1, the degree-2 part gives 4U_αB_βC_γ = f₂, a product of rational linear
  forms: contradiction.
* Every other case has two zero degrees. ∎

*Arithmetic corollary (with the review's hypotheses).* Suppose the two constant coordinates are positive integers and the
triple is a positive-integer solution at some point where f > 0. Then validity at an integer point with f(x, y) > 0 is
the congruence:
* f ≡ −U (mod 4UC − 1) if U, C are constant;
* f ≡ −(U + B) (mod 4UB) if U, B are constant;
* f ≡ −B (mod 4BC − 1) if B, C are constant.
Each is a fixed residue class of p = f(x, y). With non-integral or non-positive constants there may be no valid points
at all, e.g. U = C = −1, B = (f − 1)/3 is an identity but no certificate.

*Reading (scope corrected after review).*
* *Global polynomial* certificates in the coordinates (x, y), and finite menus of them, add nothing beyond p's residue
  class, so they fall under T1 / Lemma P / Cor S2.
* Not excluded: rational or piecewise formulas on selected domains, constructions using divisors of expressions in x and
  y, and uses of the Frobenius data (x, y) mod q. Fixed finite non-abelian Frobenius data are inert on finite witness
  sets by (J)96; the divisor routes look like B2 lotteries on integers of size ≤ √p (Assessment).
* No candidate rule was found worth testing on the zeros.

## 6. Verdict

**Narrowed.**
* Scoped theorems:
  * Lemma P (one-parameter (★) families are the classes H_d and K_{u,B});
  * Thms S1 / S3 and Cor S2: no finite (★) case split covers {p ≡ 1 (M), p ≡ R (ℓ)} for (★)-sterile R, which includes
    every non-residue R ≤ (ℓ − 1)/2. This covers class 1 mod 840; the other five classes are open;
  * Prop C1: global polynomial certificates in the representation coordinates reduce to congruences.
* Descriptive / structural (PROVED lemmas G0, G, O plus EVIDENCE and Assessment):
  * the six classes are separated only by order-≥3 data;
  * the low-R primes avoid hit non-residue classes;
  * sterile non-residues behave much more like residues than like hit non-residues;
  * the apparent "L6(0) holds on 𝔐" is largely the genus term's blind spot.
* Prior work credited: RESIDUE_HARDNESS (full-residue class effects, class 1 hardest), HCF / FAMTRY / NONCONG (sterile
  points for other families), y7 / POINTWISE_MORDELL (ES coverings).
* What survives:
  * (MS) itself;
  * arguments using the large prime factors of p + u or 4Cp + 1 (B2);
  * main terms that know the actual hit classes (a local-density main term as in RESIDUE_HARDNESS, rather than a genus
    term). This would remove the L6 blind spot, but it is a main-term repair, not a positivity mechanism.

*Falsifier table re-stated:* §0′ (updated after review; no HOT LEAD).

*Proposed FRONTIER text (do not edit FRONTIER here).*
* §4 item 15 addendum: "(z58, Z58_MORDELL) Inside 𝔐 the genus sum is the same function of ((p/q))_{q ≥ 11} on all six
  classes at a common cutoff (Lemma O). The six classes are separated only by order-≥3 characters; class 1 is hardest
  (prior: RESIDUE_HARDNESS).
  * The one-parameter (★) menu leaves 11 classes mod 840: 𝔐 plus the sterile non-residues 2 mod 5 and 3 mod 7. They
    contain all 14 (★)-zeros.
  * Inside 𝔐 at ℓ = 11–23, sterile non-residue classes are much closer to residue classes than to hit classes, and
    low-R primes avoid hit classes (EVIDENCE).
  * L6(0) holds at all nine Mordell (★)-zeros (M_gen < c_V L²), and 6 of its 7 violators lie at sterile non-residues,
    so the diagnostic reflects the genus term's blind spot (Assessment)."
* §6 (closed): "(z58) Finite (★) case splits by one-parameter families (exactly the H_d and K_{u,B} classes, Lemma P)
  on {p ≡ 1 (M), p ≡ R (ℓ)} with x_{ℓ,R} (★)-sterile, e.g. every non-residue R ≤ (ℓ − 1)/2 → Z58_MORDELL Thms S1/S3,
  Cor S2 (PROVED). Global polynomial certificates in the coordinates of p = x² + 840y² → Prop C1 (PROVED: congruences
  only). Not covered: the other five Mordell classes, non-polynomial uses of (x, y)."

*Bottom line.* Mordell's six classes are hard for (★) because they are squares at 3, 5 and 7 at once. In the data,
however, the sterile non-residue classes (2 mod 5, 3 mod 7, and their analogues at each ℓ) are nearly as hard. The genus
term cannot tell them from easy non-residues. This accounts for the five off-Mordell zeros and for the L6(0) pattern.
It gives no route to (MS):
* finite (★) refinements of class 1 are blocked by sterile 1-points (S1/S3);
* the Mordell representation carries no information beyond congruences for global polynomial certificates (C1).
B2 did not move.

## 7. Reproduction

All commands were run under `ulimit -v 4000000` and `timeout` ≤ 1800, from the repository root.
* `uv run --with numpy python scripts/z58_mordell_cover.py L es|star|starH`
* `cd scripts && uv run --with numpy python z58_mordell_refine.py 9240 es 2 3 5 7 11 13 17 19`
* `uv run --with sympy python scripts/z58_mordell_sterile1.py 100000 48`
* `uv run --with sympy python scripts/z58_mordell_sterile2.py 30000 60`
* `uv run --with sympy python scripts/z58_mordell_sterileB.py 60 2 200000`
* `gcc -O2 -o /tmp/z58cs scripts/z58_mordell_classstats.c -lm && /tmp/z58cs 100000000 /tmp/mprimes.txt` (≈ 40 s,
  ≈ 300 MB)
* `uv run --with sympy python scripts/z58_mordell_bymod.py /tmp/mprimes.txt 1e7`
* M_gen: `gcc -O2 -o /tmp/z56mgen scripts/z56_famdesign_mgen.c -lm; /tmp/z56mgen < primes` (≈ 4.5 s per prime near
  10⁸). Input lists are described in `data/z58/mordell/README.md`.

## 8. Internal review

A hostile reviewer (`data/z58/mordell/internal_review.md`) found 1 FATAL, 6 MAJOR and 5 MINOR issues. All were addressed
in this version:
1. **FATAL.** S1 covers only the H-menu, and x_{11,7} lies in K_{4,11}. Fixed by Lemma P (the full one-parameter menu
   is H ∪ K), Theorem S3 (B-sterility for R ≤ (ℓ − 1)/2), and the restatement of S2 for the full menu. Old claims
   about "every finite refinement" were removed.
2. **Other five classes.** Now stated as open. The false fibre identification and the τ((ℓ + 1)/4)/ℓ claim in §4 were
   removed.
3. **Lemma O.** Restated with a cutoff; its statistical consequence was downgraded to Assessment.
4. **"Indistinguishable" / "avoid completely".** Replaced by group means with standard errors, and the exception
   21 106 849 is reported.
5. **The 22-class set.** It is the H-menu set; the full menu leaves 11 classes. The joint-coordinate exception (d = 35)
   is discussed.
6. **C1.** Integrality/positivity hypotheses were added, and the scope was restricted to global polynomial
   certificates.
7. **NONCONG.** Credited as fixed-slice, with the R267 note.
8. **Numbers.** Corrected: non-Mordell mean 0.1662; the M_gen sample is now frozen at 96; the ranges 2/5–7/8.
9. **S1 converse integrality** and the exact j bound were added.
10. **Lemma G** mean aside: corrected.
11. **Falsifier-table M2 claims:** corrected.
12. **Provenance:** data README added; nonexistent script reference removed; reproduction paths fixed. "Closure"
    now means the unit part of the closure in Cor S2's proof (stated via an explicit neighbourhood).

No second review pass was run.
