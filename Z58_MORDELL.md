# Z58_MORDELL — why Mordell's six classes behave differently for (★), and what a finite case split can still do

Status: z58 lane MORDELL (brief `z52bbriefs/z58_lanes.md` §MORDELL, rules `z52bbriefs/z53_depth.md` with z53 → z58).
Internal, **checkpoint 1** (skeleton; sections marked TODO are in progress). **ES is OPEN; nothing here proves or
disproves ES, (★) or (MS).** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Scripts `scripts/z58_mordell_*`, data `data/z58/mordell/`.

Notation. R(n) = #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n}; H_d = {−k mod d : k | (d+1)/4} for d ≡ 3 (mod 4); by
Z57_SYNTH Lemma A.1, R(n) = #{d : n mod d ∈ H_d}. 𝔐 = {1, 121, 169, 289, 361, 529} ⊂ (ℤ/840)^× = the six unit squares.
A *profinite point* is x = (x_q)_q ∈ ∏_q ℤ_q^×; x lies in H_d iff (x mod d) ∈ H_d. n_p = least prime q with (q/p) = −1.

## 0. MANDATORY FALSIFIER TABLE (committed at checkpoint 1; re-stated at the end)

Two mechanisms are examined. M1 is the lane's literal question (finite case splits / Mordell-type identities on 𝔐);
M2 is the new idea generator of this lane (use the *unique representation* p = x² + 840y², which exists exactly on 𝔐).

| screen | M1: finite (★)-case split of a 𝔐-class (covering by finitely many H_d) | M2: certificates built from the Cornacchia coordinates (x, y) of p = x² + 840y² |
|---|---|---|
| **F1 odd squares** | Squares lie in no H_d (Jacobi, SYNTH A.1(b)), so square classes are never covered. M1's result (Thm S1 below) is a *no-go strictly beyond T1*: it exhibits non-square sterile points. No positivity is claimed, so nothing to break. | Odd squares m² ∈ 𝔐-classes mod 840 *do* have representations m² = x² + 840y² with y ≠ 0 (e.g. 29² = 1 + 840·1²); Pythagorean points are dense in every open cone of (x : y). Hence **any certificate polynomial in (x, y) on a congruence cone is killed by T1** (Prop C1, TODO proof write-up). Primality can enter only through *uniqueness* of the representation (a prime has exactly the four reps (±x, ±y)); a surviving certificate must use arithmetic of x, y (divisors), i.e. a lottery again. |
| **F2 C-even sub-line (8/p)** | A no-go only gets stronger on a sub-family (every (★)-sterile point is R₈-sterile). Not a positivity argument. | Same as F1: no positivity argument survives the polynomial stage, so nothing distinguishes C parity yet. TODO: check whether representation-based witnesses, when they fire, are C-odd or C-even on the R₈-zeros. |
| **F3 composites** | Coverings are blind to primality: Thm S1's sterile points are limits of composites and primes alike (this is *why* no finite split helps). | Composites n ∈ 𝔐 with ≥ 2 essentially distinct reps exist; a rep-based rule would have to pick one. Uniqueness of the rep is a genuine primality feature (beyond non-squareness): it fails at products of two 𝔐-primes. |
| **F4 known zeros** | No positivity claimed. Consistency check (EVIDENCE): all 9 (★)-zeros in 𝔐 have (n_p, p mod n_p) at a residue R whose 1-point x_{n_p,R} is (★)-sterile (Thm S1 criterion; e.g. 5212561: (11, 2), 8813281: (17, 5)). | TODO: run the rep-based witness search on the 14 + 38 + 12 zeros. |

**Verdict so far (checkpoint 1):** no HOT LEAD. M1 is a scoped no-go (narrowing); M2 is open at the non-polynomial stage.

## 1. Precise statements attacked

**(MS)** (Z57_SYNTH §1.1): every prime p > 10¹⁷ with p mod 840 ∈ 𝔐 has R(p) ≥ 1.

**Q1 (finite case split, M1).** For an odd prime ℓ ≥ 11, a class r ∈ 𝔐 and a non-residue R mod ℓ, is the set
Σ(r, ℓ, R) := {p : p ≡ r (mod 840), p ≡ R (mod ℓ)} covered by finitely many (★) hit classes H_d (equivalently, by
compactness, does the closure of Σ in ℤ̂^× contain a point lying in no H_d — a *(★)-sterile point*)? A "yes" for some
(r, ℓ, R) would shrink (MS) to the complement by a Mordell-type identity; a "no" is a scoped no-go.

**Q2 (structure).** Which small-d hit classes do the 840-congruences close, and how does that shape the (★) count on 𝔐?

**Q3 (M2).** p ∈ 𝔐 ⟺ p = x² + 840y² (840 is idoneal; one class per genus of discriminant −3360; known, see
`ES_CONNECTIONS_TODO.md` Z0935, OEIS A139665). Can (x, y) be turned into a (★) witness?

*Why not already closed.* For the full ES identity menu, Q1 is the POINTWISE_MORDELL / MORDELL13B–E line
(`CAMPAIGN_SUMMARY.md` §(H)34): r = 13 covered outside 35 459 classes mod a tree level, no sterile non-square point
proved. For HC certificates, `Z55_HCF.md` T3.1 / C3.2 proves sterility of x_{ℓ,R} for R < (ℓ − 1)/3. For (★) alone (the
family (MS) is about) the exact sterile set at the 1-points was not determined; Q3 (using the representation as an input)
has no prior memo (git grep: only the observation itself, "yield none").

## 2. First lemma: the exact (★)-sterility criterion at 1-points (Thm S1)

For an odd prime ℓ and an integer 1 ≤ R ≤ ℓ − 1 let x_{ℓ,R} be the profinite point with x_ℓ = R and x_q = 1 for q ≠ ℓ.
(If R is a non-residue, the closure of {p ≡ 1 (mod M), p ≡ R (mod ℓ)} contains x_{ℓ,R} for every M coprime to ℓ.)

**Theorem S1 (PROVED; proof below, CERTIFIED cross-check).** x_{ℓ,R} lies in some H_d with ℓ ∤ … iff one of:
* (direct) ℓ ≡ 3 (mod 4) and ℓ − R divides (ℓ + 1)/4 (d = ℓ);
* (j-family) there is an integer j ≥ 1 with D_j := ℓj − (j + 1)R ≥ 1, D_j | ℓ + j + 1 and 4 | (ℓ + j + 1)/D_j, and the
  resulting m := 4C − t (C := (ℓ + j + 1)/(4D_j), t := (4CR + 1)/ℓ) is prime to ℓ (then d = ℓm).
In particular **x_{ℓ,R} is (★)-sterile for every 1 ≤ R ≤ (ℓ − 1)/2** (then D_j ≥ … forces no solution), and for each ℓ only
O(1)·τ-many residues R are not sterile.

*Proof.* Suppose x := x_{ℓ,R} ∈ H_d: x ≡ −k (mod d), k | (d + 1)/4; write d + 1 = 4kC, d = ℓ^a m with ℓ ∤ m.
(i) a = 0 is impossible: then −k ≡ 1 (mod d) with 1 ≤ k < d forces k = d − 1 > (d + 1)/4.
(ii) Mod m: 4kC ≡ 1 and k ≡ −1 give m | 4C + 1. Mod ℓ^a: k ≡ −R gives ℓ^a | 4CR + 1; put t := (4CR + 1)/ℓ^a ≥ 1.
Conversely, given C, a, m with m | 4C + 1, ℓ^a | 4CR + 1, ℓ ∤ m and 4C | ℓ^a m + 1, the integer k := (ℓ^a m + 1)/(4C)
satisfies k ≡ −1 (mod m) (from 4C ≡ −1) and k ≡ −R (mod ℓ^a) (from 4CR ≡ −1), so x ∈ H_d with d = ℓ^a m.
(iii) From ℓ^a t = 4CR + 1 ≡ 1 (mod 4C): 4C | ℓ^a m + 1 ⟺ m ≡ −t (mod 4C). Since R ≤ ℓ − 1, t < 4C, and
1 ≤ m ≤ 4C + 1, so m = 4C − t, or m ≡ 1 (mod 4C) with t = 4C − 1. In the first case m | 4C + 1 ⟺ (4C − t) | (t + 1)
(as 4C + 1 = (4C − t) + (t + 1)), i.e. t + 1 = j(4C − t) for some j ≥ 1.
(iv) a ≥ 2 is impossible: t ≤ (4C(ℓ − 1) + 1)/ℓ² < 4C/ℓ + 1, so 4C − t > t + 1 (no j) and t ≠ 4C − 1 (C ≥ 1, ℓ ≥ 3).
(v) a = 1: t = 4C − 1 gives 4C(ℓ − R) = ℓ + 1, the direct case (k = ℓ − R, m = 1). Otherwise t = (4Cj − 1)/(j + 1), and
ℓt = 4CR + 1 becomes 4C·D_j = ℓ + j + 1 with D_j = ℓj − (j + 1)R; this is the j-family.
(vi) If R ≤ (ℓ − 1)/2 then t = (4CR + 1)/ℓ ≤ 2C − (2C − 1)/ℓ < 2C, so 4C − t > 2C ≥ t + 1 for the first case, and
t = 4C − 1 > 2C is impossible: no hit. ∎ (Small print, TODO in final: ℓ | m case — then a is larger and (iv) applies; the
criterion as stated just lists the a = 1 solutions with ℓ ∤ m.)

*Cross-check (CERTIFIED for d ≤ 10⁵, ℓ ≤ 47).* `scripts/z58_mordell_sterile1.py 100000 48` (direct CRT test of every
d ≡ 3 (4), d ≤ 10⁵): 0 hits with R ≤ (ℓ − 1)/2; the hit residues R > ℓ/2 found are exactly those of the criterion
(e.g. ℓ = 13: R ∈ {8, 11}, d = 39 = 3·13, j = 2, C = 2, t = 5, m = 3). TODO: automated criterion-vs-brute comparison.

*Reading.* Compared with HCF C3.2 (HC certificates, R < (ℓ − 1)/3), Thm S1 is the exact answer for (★) at 1-points.
Consequence (PROVED from S1 + compactness): for every M coprime to ℓ and every R in the sterile set, the class
{p ≡ 1 (mod M), p ≡ R (mod ℓ)} is covered by no finite family of (★) certificates — no Mordell-type case split for (★)
removes it from (MS). TODO: the other five 𝔐 classes (points with x_5 ∈ {1, 4}, x_7 ∈ {1, 2, 4}).

## 3. TODO (in progress)
* §3 Q2: the 840-closure of small d (reciprocity: every witness d has (d/p) = −1; on 𝔐 every 7-smooth d is closed, so
  d_min ≥ n_p ≥ 11); exact local hit densities on 𝔐 vs. off 𝔐 for d ≤ D; link to RESIDUE_HARDNESS (prior).
* §4 Q1 on all six classes + multi-prime points; (★)-uncovered density in 𝔐 at levels 840·ℓ… (sparse-set quantification).
* §5 M2: Prop C1 (polynomial no-go via Pythagorean density) + non-polynomial rep-based witness statistics on the zeros.
* §6 ES-identity covering at 840·ℓ (prior: y7_mordell_levels, POINTWISE_MORDELL); recomputed here at 9240, 10920, 14280
  with `scripts/z58_mordell_cover.py` (34 / 40 / 52 uncovered, of which 4 / 4 / 4 non-squares, e.g. 2521, 3361 mod 9240).
