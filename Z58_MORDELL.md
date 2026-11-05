# Z58_MORDELL — Mordell's classes for (★): the right variable is (★)-sterility, not the quadratic character (narrowed)

Status: z58 lane MORDELL (brief `z52bbriefs/z58_lanes.md` §MORDELL, rules `z52bbriefs/z53_depth.md` with z53 → z58).
Internal, internally reviewed only (§8). **ES is OPEN; nothing here proves or disproves ES, (★) or (MS).** Labels:
PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z58_mordell_*`, data
`data/z58/mordell/` (< 1 MB). Verdict: **narrowed** (no HOT LEAD).

Notation. R(n) = #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n}; for d ≡ 3 (mod 4), H_d = {−k mod d : k | (d+1)/4}; by
Z57_SYNTH Lemma A.1, R(n) = #{d ≡ 3 (4), d ≥ 3 : n mod d ∈ H_d}. 𝔐 = {1, 121, 169, 289, 361, 529} = the six unit
squares of (ℤ/840)^×. M_gen = genus part of R (Z56_FAMDESIGN §1: M_gen(p) = Σ_{(o,e)} 2(s(q)/φ(q))·1[−p(o+e) ∈
((ℤ/q)^×)²], q = 4oe), X = R − M_gen, L = log p, c_V = 5/(4π²) ≈ 0.12665. A *profinite point* is x ∈ ∏_q ℤ_q^×; it
lies in H_d iff x mod d ∈ H_d. A point lying in no H_d is *(★)-sterile*.

## 0. Summary

1. **Thm S1 (PROVED; CERTIFIED cross-check).** Exact criterion for the (★)-sterility of the points x_{ℓ,R} (R at ℓ, 1
   at every other prime). In particular x_{ℓ,R} is sterile for **every** 1 ≤ R ≤ (ℓ − 1)/2, and only a few residues
   per ℓ are not sterile. Cor S2: no finite family of (★) certificates covers any class {p ≡ 1 (mod M), p ≡ R (mod ℓ)}
   with R in the sterile set; so no Mordell-type finite case split shrinks (MS) on these classes. This sharpens, for
   (★), `Z55_HCF.md` C3.2 (HC certificates, R < (ℓ − 1)/3) and `Z56_FAMTRY.md` Prop 2.2 (R = 1).
2. **Lemma O (PROVED).** M_gen(p) depends on p only through the quadratic characters (p/q), q ≥ 11, by one and the
   same function on all six Mordell classes. So **every difference between the six classes lives in X**, i.e. in
   characters of order ≥ 3 (the quartic character mod 5 and the cubic character mod 7). Data: class means of R/L² on
   [10⁷, 10⁸] range over 0.1199 (class 1) … 0.1279 (class 529), against 0.164 off 𝔐 (EVIDENCE).
3. **The (★)-hard set is larger than 𝔐 and is cut out by sterility (EVIDENCE, strong).**
   * The (★)-uncovered classes mod 840 are 22 (𝔐★ ⊋ 𝔐), namely p ≡ 1 (3), p mod 5 ∈ {1, 2, 4},
     p mod 7 ∈ {1, 2, 3, 4} (two exceptions), p ≡ 1 or 5 (8) (CERTIFIED).
   * The non-residues 2 mod 5 and 3 mod 7 are exactly the Thm S1-sterile ones.
   * All 14 (★)-zeros and all 38 𝔊*-zeros lie in 𝔐★.
   * Within 𝔐, at ℓ = 11, …, 23, Thm-S1-sterile non-residue classes behave like residue classes. Mean R/L² there is
     0.119–0.132; the hit non-residue classes have 0.128–0.152. Among ≈ 1.6·10⁵ Mordell primes in [10⁷, 10⁸] with
     p mod ℓ in a hit class, the number with R(p) ≤ 4 is 0 or 1 for each ℓ.
   * **The genus (quadratic-character) variable is the wrong one: hardness follows (★)-sterility.**
4. **"L6 holds on 𝔐" is an artifact (CERTIFIED numbers + Assessment).** All 9 Mordell-class (★)-zeros have
   M_gen < c_V L² (M_gen/L² ∈ [0.084, 0.115]), so the η = 0 diagnostic L6(0), X ≥ −c_V L², holds *at zeros*.
   * Six of the seven L6(0) violators of Z57_SYNTH §2.3 sit in the sterile non-residue classes 3 mod 7 or 2 mod 5,
     where M_gen (which only sees (p/7), (p/5)) credits the average non-residue mass. The seventh is p ≡ 2 (3).
   * Unconditional samples near 10⁸ give mean M_gen/L² of 0.127 on 𝔐 (46 % of the sample below c_V) and 0.154 off 𝔐
     (none below c_V).
5. **M2 — the representation p = x² + 840y² as an input (PROVED no-go at the algebraic stage).**
   * p ∈ 𝔐 ⟺ p = x² + 840y² (840 is idoneal; classical).
   * Prop C1: every polynomial (★)-certificate (U, B, C) ∈ ℚ[x, y]³ for x² + 840y² (indeed for any binary quadratic
     with ℚ-irreducible top form) has two constant coordinates. So it is a fixed-modulus congruence certificate, which
     depends on p mod m only.
   * The representation can therefore enter only through arithmetic (divisors) of x, y, i.e. a B2 lottery, or through
     non-abelian Frobenius data, which are inert on finite witness sets ((J)96).
6. **ES identity coverings at 840·ℓ (prior, recomputed).** The ET-shaped menu leaves 34 / 40 / 52 classes uncovered at
   9240 / 10920 / 14280. All the squares are uncovered, plus 4 non-squares at each level (2041, 2521, 3361, 5161
   mod 9240) (CERTIFIED). This is the y7 / POINTWISE_MORDELL line, not redone further.

## 0′. MANDATORY FALSIFIER TABLE (as committed at checkpoint 1, updated with results)

M1 = finite (★)-case splits of 𝔐-classes / sterility (§§2–4); M2 = Cornacchia-coordinate certificates (§5). Neither
mechanism claims positivity; both are scoped no-goes plus a structural explanation, so the screens test whether the
*explanation* is consistent rather than whether a proof survives.

| screen | M1 (Thm S1, Cor S2, §3 explanation) | M2 (Prop C1) |
|---|---|---|
| **F1 odd squares** | Squares lie in no H_d (Jacobi, SYNTH A.1(b)). Thm S1 adds *non-square* sterile points: the no-go goes strictly beyond T1. The §3 explanation puts squares and sterile non-residues in one "hard" class. Squares are its extreme case (sterile at every prime). | Odd squares in 𝔐-classes have representations with y ≠ 0 (29² = 1 + 840·1²). Prop C1 makes this moot: polynomial certificates are congruence certificates, which never contain squares. Primality could only enter through *uniqueness* of the representation (a prime has exactly (±x, ±y)); no rule using it was found. |
| **F2 C-even sub-line** | A no-go only strengthens on a sub-family: every (★)-sterile point is R₈-sterile. The sterility explanation does not separate C odd from C even. Of the four Mordell R₈-zeros above 10¹⁰, (n_p, p mod n_p) = (23, 10), (19, 3), (29, 10), (13, 5); all four are Thm-S1-sterile (§3.4). | No positivity argument survives Prop C1, so nothing to separate. |
| **F3 composites** | Coverings are blind to primality: sterile points are limits of composites and primes alike. That is *why* Cor S2 holds. The 285 composite zeros are consistent with it. | Composites in 𝔐 with several representations exist (e.g. products of two 𝔐-primes); a representation-based rule would have to choose one. |
| **F4 known zeros** | All 14 (★)-zeros and all 38 𝔊*-zeros are in the (★)-uncovered set 𝔐★ mod 840 (§3.4). All 9 Mordell (★)-zeros have (n_p, p mod n_p) at a Thm-S1-sterile residue. No positivity is claimed, so nothing to break. | Not applicable (no rule). |

**No HOT LEAD.**

## 1. Precise statements attacked

**(MS)** (Z57_SYNTH §1.1): every prime p > 10¹⁷ with p mod 840 ∈ 𝔐 has R(p) ≥ 1.

**Q1 (finite case split).** Let ℓ ≥ 11 be prime, r ∈ 𝔐 and R a non-residue mod ℓ. Is Σ(r, ℓ, R) := {p ≡ r (840),
p ≡ R (ℓ)} covered by finitely many hit classes H_d? By compactness this holds iff the closure of Σ in ℤ̂^× contains no
(★)-sterile point. A "yes" removes Σ from (MS) by a Mordell-type identity; a "no" is a scoped no-go.

**Q2 (structure).** Which small-d hit classes does the 840-structure close? What does it do to M_gen and to X? Why is the
uniform diagnostic L6(0) violated only off 𝔐?

**Q3 (M2).** Can the unique representation p = x² + 840y² of a Mordell prime be turned into a (★) witness?

*Why not already closed.*
* For the full ES identity menu, Q1 is the POINTWISE_MORDELL / MORDELL13B–E line (`CAMPAIGN_SUMMARY.md` §(H)34;
  r = 13 handled by a tree certificate outside 35 459 classes).
* For HC certificates, `Z55_HCF.md` T3.1 / C3.2 covers R < (ℓ − 1)/3.
* The *exact* (★)-sterile set at the 1-points, the class-by-class role of sterility in the data, and Q3 have no prior
  memo. For Q3, git grep finds only the observation itself (`ES_CONNECTIONS_TODO.md` Z0935, "yield none").

## 2. Q1: exact (★)-sterility of the 1-points

For an odd prime ℓ and an integer 1 ≤ R ≤ ℓ − 1, x_{ℓ,R} denotes the point with x_ℓ = R and x_q = 1 for q ≠ ℓ. It lies
in the closure of {p ≡ 1 (mod M), p ≡ R (mod ℓ)} for every M coprime to ℓ.

**Theorem S1 (PROVED).** x_{ℓ,R} lies in some H_d iff one of the following holds:
* **(direct)** ℓ ≡ 3 (mod 4) and (ℓ − R) | (ℓ + 1)/4; then d = ℓ.
* **(j-family)** there is j ≥ 1 with D_j := ℓj − (j + 1)R ≥ 1, D_j | ℓ + j + 1 and 4 | (ℓ + j + 1)/D_j, such that, with
  C := (ℓ + j + 1)/(4D_j) and t := (4CR + 1)/ℓ (then an integer), m := 4C − t is prime to ℓ. Then d = ℓm.

In particular, **x_{ℓ,R} is (★)-sterile for every 1 ≤ R ≤ (ℓ − 1)/2.**

*Proof.* Suppose x := x_{ℓ,R} ∈ H_d. Then x ≡ −k (mod d) with k | (d + 1)/4; write d + 1 = 4kC and d = ℓ^a m with ℓ ∤ m.
1. *a = 0 is impossible.* Then −k ≡ 1 (mod d), and 1 ≤ k < d forces k = d − 1 > (d + 1)/4.
2. *Reduction.* Mod m: 4kC ≡ 1 and k ≡ −1 give m | 4C + 1. Mod ℓ^a: 4kC ≡ 1 and k ≡ −R give ℓ^a | 4CR + 1. Put
   t := (4CR + 1)/ℓ^a ∈ ℕ.
   * Conversely, let a ≥ 1, C ≥ 1 and m with ℓ ∤ m, m | 4C + 1, ℓ^a | 4CR + 1 and 4C | ℓ^a m + 1. Then
     k := (ℓ^a m + 1)/(4C) satisfies k ≡ −1 (mod m) and k ≡ −R (mod ℓ^a). So x ∈ H_d with d = ℓ^a m = 4kC − 1.
3. *The shape of m.* Since ℓ^a t = 4CR + 1 ≡ 1 (mod 4C), the condition 4C | ℓ^a m + 1 is equivalent to m ≡ −t (mod 4C).
   * R ≤ ℓ − 1 gives t < 4C. With 1 ≤ m ≤ 4C + 1, either m = 4C − t, or t = 4C − 1 and m ∈ {1, 4C + 1}.
   * If m = 4C − t, then m | 4C + 1 ⟺ (4C − t) | (t + 1), because 4C + 1 = (4C − t) + (t + 1). So t + 1 = j(4C − t)
     for some j ≥ 1.
4. *a ≥ 2 is impossible.* Here t ≤ (4C(ℓ − 1) + 1)/ℓ² ≤ 8C/9 + 1/9, since (ℓ − 1)/ℓ² ≤ 2/9 for ℓ ≥ 3.
   * Then 2t + 1 ≤ 16C/9 + 11/9 < 4C (C ≥ 1), i.e. 4C − t > t + 1, so no j exists.
   * Also t ≤ 8C/9 + 1/9 < 4C − 1, so t ≠ 4C − 1.
5. *a = 1.* If t = 4C − 1, then ℓ(4C − 1) = 4CR + 1, i.e. 4C(ℓ − R) = ℓ + 1. This is exactly the direct condition
   (m = 1: d = ℓ, k = ℓ − R; m = 4C + 1 is a second hit under the same condition).
   * Otherwise t = (4Cj − 1)/(j + 1), and ℓt = 4CR + 1 becomes 4C·D_j = ℓ + j + 1. This is the j-family. The condition
     ℓ ∤ m is part of the decomposition; if ℓ | m, then v_ℓ(d) ≥ 2 and step 4 excludes it.
6. *Small R.* If R ≤ (ℓ − 1)/2, then t = (4CR + 1)/ℓ ≤ 2C − (2C − 1)/ℓ < 2C.
   * So 4C − t > 2C ≥ t + 1, which excludes the j-family.
   * And t = 4C − 1 > 2C is impossible.
   * Together with steps 1 and 4, no d exists. ∎

**Corollary S2 (PROVED, from S1 + compactness + Dirichlet).** Let ℓ be an odd prime, M ≥ 1 with ℓ ∤ M, and R a
non-residue mod ℓ such that x_{ℓ,R} is sterile (e.g. any non-residue R ≤ (ℓ − 1)/2). Then every finite union U of hit
classes H_d misses infinitely many primes p ≡ 1 (mod M), p ≡ R (mod ℓ).
*Proof.* U is clopen in ℤ̂ and x_{ℓ,R} ∉ U. So some basic neighbourhood of x_{ℓ,R}, a unit class c mod ℓ^b·M′ with
M | M′, ℓ ∤ M′, c ≡ 1 (M), c ≡ R (ℓ), is disjoint from U. Dirichlet gives infinitely many primes in it. ∎
(With M = 840: no finite (★) case split removes {p ≡ 1 (840), p ≡ R (ℓ)} from (MS).)

*Checks.*
* CERTIFIED: criterion = brute force for every odd prime ℓ < 60 and every R, testing all d ≤ 3·10⁴ (0 mismatches;
  `scripts/z58_mordell_sterile2.py 30000 60`, `data/z58/mordell/sterile2_d3e4.txt`).
* The direct CRT test to d ≤ 10⁵ (`z58_mordell_sterile1.py 100000 48`) finds no hit with R ≤ (ℓ − 1)/2.
* Example: ℓ = 13, R ∈ {8, 11} are hit at d = 39 = 3·13 (for R = 8: j = 2, C = 2, t = 5, m = 3).
* The number of non-sterile residues per ℓ is 2, 2, 1, 3, 4, 3, 4, 3, 2, 3, 6, 5, 5 for ℓ = 11, 13, …, 59 (criterion of
  S1). All of them are non-residues > ℓ/2, e.g. {8, 10} for ℓ = 11 and {17, 20, 21, 22} for ℓ = 23.

*The other five Mordell classes (EVIDENCE).* Take the points with x_5 = r mod 5, x_7 = r mod 7 (5-/7-adic squares),
x_ℓ = R and 1 elsewhere. Brute force with d ≤ 3·10⁴ leaves, per class, between 7/14 and 24/29 of the non-residues
unhit, from 2/5 (ℓ = 11) up to 24/29 (ℓ = 59) (same file). Proving sterility there needs the S1 analysis with the 3-, 5- and 7-parts of d; it was
not done.

*Novelty (Assessment).* Prior results cover R = 1 (FAMTRY Prop 2.2), R < (ℓ − 1)/3 for the larger HC family (HCF), and
R = 2 for the ES witness classes (NONCONG_LIFTS Thm 2.6). S1 is the exact (★) answer at 1-points: a small, clean
increment. It is still B1 (a covering statement).

## 3. Q2: what the 840-structure does

### 3.1 Closing of small d (PROVED; known in substance)

**Lemma G0.** If p ≡ 1 (mod 4) is prime and p ∈ H_d, then (d/p) = −1. So d has a prime factor q with (q/p) = −1 to an
odd power.
*Proof.* SYNTH A.1(b) gives (p/d) = −1 (Jacobi), and reciprocity gives (p/d) = (d/p) for p ≡ 1 (4). ∎
On 𝔐, (q/p) = 1 for q = 3, 5, 7, and d is odd. So **every 7-smooth d is closed and every witness has d ≥ n_p ≥ 11**.

**Lemma G (genus split at q | d; PROVED).** Let q be an odd prime, d ≡ 3 (mod 4) with q | d, N := (d + 1)/4, and
S_q(N) := Σ_{k | N} (k/q) ≥ 0. Then #{h ∈ H_d : (h/q) = ε} = (τ(N) + ε(−1/q)S_q(N))/2 for ε = ±1.
*Proof.* h = −k with k | N, so (h/q) = (−1/q)(k/q); q ∤ N since 4N ≡ 1 (mod q). Hence #{k | N : (k/q) = η} =
(τ(N) + ηS_q(N))/2. Here S_q(N) ≥ 0 because it is multiplicative with factors 1 + χ(ℓ) + … + χ(ℓ)^e ≥ 0. ∎
*Reading.* For p with (p/q) = +1, only the (h/q) = +1 half of H_d is available.
* That half is the smaller one at q = 3 and q = 7 ((−1/q) = −1), and the larger one at q = 5.
* The imbalance is S_q(N), whose mean over N is L(1, (·/q)), against τ(N) ≍ log N. It is a relative 1/log effect,
  consistent with the 1/L class term of `RESIDUE_HARDNESS.md` (which is prior and more complete).

### 3.2 Lemma O: the six classes differ only in X (PROVED)

**Lemma O.** There is a function Φ(X; ε) of a real X and a sign vector ε = (ε_q)_{q ≥ 11 prime} with
M_gen(p) = Φ(p; ((p/q))_{q ≥ 11}) for every prime p with p mod 840 ∈ 𝔐, the same Φ for all six classes (X enters only
through the summation range 4oe − o − e ≤ X).
*Proof.* By Z56_FAMDESIGN §1, M_gen(p) = Σ_{(o,e)} W(o, e) with W = 2(s(q)/φ(q))·1[−p(o + e) is a square unit mod
4oe], where s(q) does not depend on p. Whether pa (a a unit) is a square mod Q = 4oe depends only on the class of p in
(ℤ/Q)^×/((ℤ/Q)^×)². By CRT that class is determined by p mod 8 (only through the 2-adic square class) and by (p/q) for
the odd primes q | Q. Every r ∈ 𝔐 is ≡ 1 (8) and a square mod 3, 5 and 7. So for p ∈ 𝔐 the only data entering are
(p/q), q ≥ 11. ∎
Consequences:
* Under equidistribution of primes in classes mod 840·Q, the conditional law of M_gen given p mod 840 = r is the same for
  the six r ∈ 𝔐.
* So all class-to-class differences inside 𝔐 come from X.
* The characters of (ℤ/840)^× that separate the six classes are exactly those nontrivial on the squares, i.e. of order
  ≥ 3: the quartic character mod 5 (separating 1 from 4) and the cubic character mod 7 (separating 1, 2, 4).

*Data (EVIDENCE; `scripts/z58_mordell_classstats.c`, `data/z58/mordell/classstats_1e8.txt`).* Exact R(p) for all
primes p ≡ 1 (4) ≤ 10⁸ (sieve enumeration of all triples, as in SYNTH's engine). Mean R/L² on [10⁷, 10⁸], about 26 500
primes per class:
* 𝔐 classes: 1: 0.1199, 361: 0.1227, 121: 0.1236, 289: 0.1266, 169: 0.1272, 529: 0.1279. The eight lowest of the 96
  classes are these six plus 337 (0.1261) and 577 (0.1280), both in 𝔐★ (§3.4).
* Non-Mordell average: 0.164.
* The spread inside 𝔐 (0.008) is large compared with the sampling error of a class mean. The R/L² standard deviation
  was not computed. If it is ≤ 0.05, the standard error is ≈ 0.0003, so the spread is ≫ noise (Assessment).
* The p ≡ 1 (mod 5) classes (1, 361, 121) are the harder half. By Lemma O this is an X (order ≥ 3) effect, the
  "p ≡ 1 (mod q)" effect of RESIDUE_HARDNESS Lemma 2.
* Zeros ≤ 10⁸ by class (all p ≡ 1 (4)): class 1 has 3, 361 has 3, 529 has 2, 289 has 1, 121 and 169 have 0. These counts
  are too small to rank the classes.

### 3.3 Marginal class effects mod 3, 5, 7 (EVIDENCE; same data, all primes p ≡ 1 (4); means over [10⁷, 10⁸], zero and R ≤ 4 counts over p ≤ 10⁸)

| p mod q | mean R/L² | zeros ≤ 10⁸ | #R ≤ 4 |
|---|---|---|---|
| 3: 1 / 2 | 0.148 / 0.179 | 14 / 0 | 268 / 5 |
| 5: 1, 4 (QR) / 2 (QNR, S1-sterile) / 3 (QNR, hit at d = 15) | 0.162, 0.175 / **0.152** / 0.165 | 7, 5 / **2** / 0 | 108, 108 / **52** / 5 |
| 7: 1, 2, 4 (QR) / 3 (QNR, S1-sterile) / 5, 6 (QNR, in H_7) | 0.150, 0.152, 0.158 / **0.156** / 0.179, 0.187 | 4, 1, 5 / **4** / 0, 0 | 91, 66, 55 / **55** / 3, 3 |

The sterile non-residue (2 mod 5, 3 mod 7) behaves like a residue class, and the hit non-residues are "easy". A genus
(quadratic-character) model treats all non-residues mod q alike and is blind to this.

### 3.4 Inside 𝔐: sterile vs hit non-residues at ℓ = 11, …, 23 (EVIDENCE)

`scripts/z58_mordell_bymod.py` (output `data/z58/mordell/bymod_1e7_1e8.txt`): 158 955 Mordell-class primes in
[10⁷, 10⁸], split by p mod ℓ. The label is the Thm S1 status of the 1-point (exact for class 1, a proxy for the other
five).

| ℓ | mean R/L², QR classes | QNR, S1-sterile | QNR, hit | #R ≤ 4 in hit classes |
|---|---|---|---|---|
| 11 | 0.114–0.120 | 0.119–0.128 (R = 2, 6, 7) | 0.141, 0.149 (R = 8, 10) | 0 of 31 927 |
| 13 | 0.119–0.126 | 0.119–0.127 (R = 2, 5, 6, 7) | 0.137, 0.143 (R = 8, 11) | 0 of 26 623 |
| 17 | 0.120–0.127 | 0.121–0.132 (7 classes) | 0.133 (R = 11) | 0 of 9 945 |
| 19 | 0.118–0.124 | 0.120–0.127 (6 classes) | 0.128–0.152 (R = 14, 15, 18) | 1 of 26 488 |
| 23 | 0.119–0.122 | 0.120–0.124 (7 classes) | 0.138–0.150 (R = 17, 20, 21, 22) | 0 of 28 911 |

* So within 𝔐 the low-R primes avoid the hit non-residue classes completely.
* The sterile non-residue classes are statistically indistinguishable from the residue classes in mean, and they carry
  low-R primes at the same rate.
* The 4 Mordell R₈-zeros above 10¹⁰ and all 9 Mordell (★)-zeros have (n_p, p mod n_p) at an S1-sterile residue (CERTIFIED
  lookups, `scripts/z58_mordell_sterile1.py` table).

**The (★)-hard set mod 840 (CERTIFIED).** `scripts/z58_mordell_cover.py 840 star` lists the 22 classes mod 840
(≡ 1 mod 4) that contain no complete hit class of a modulus d | 840:
1, 37, 109, 121, 157, 169, 241, 289, 337, 361, 409, 421, 457, 529, 541, 577, 589, 661, 709, 757, 781, 829.
* These are all classes with p ≡ 1 (3), p mod 5 ∈ {1, 2, 4} and p mod 7 ∈ {1, 2, 3, 4}, except the two with
  (p mod 5, p mod 7) = (2, 4), which are covered by d = 35.
* All 14 (★)-zeros and all 38 𝔊*-zeros lie in this set. For the (★)-zeros this is forced; for the 𝔊*-zeros it is a
  consistency check.
* Five (★)-zeros lie in 𝔐★ \ 𝔐 (classes 409, 577, 337, 241), i.e. at the sterile non-residues 3 mod 7 or 2 mod 5.
  This is the structural reason why 5 of the 14 zeros are outside Mordell's classes.

### 3.5 Why L6(0) "holds on 𝔐 and fails off 𝔐" (CERTIFIED numbers, Assessment reading)

Recall that L6(0) at p means X(p) ≥ −c_V L², i.e. R(p) ≥ M_gen(p) − c_V L². It is vacuous wherever M_gen(p) < c_V L².
* **At zeros.** `scripts/z56_famdesign_mgen.c` (audited in z56) on the 34 distinct (★)- and 𝔊*-zeros above 10³
  (`data/z58/mordell/mgen_zeros.txt`):
  * every Mordell-class (★)-zero has M_gen/L² ∈ [0.084, 0.115] < c_V, so L6(0) holds at all nine of them;
  * 18 of the 20 Mordell 𝔊*-zeros also have M_gen < c_V L² (exceptions 1 105 441 and 564 661 441);
  * the non-Mordell zeros above 10³ mostly have M_gen > c_V L² (13 of 14; exception 23 929).
* **Unconditional samples near 10⁸** (`mgen_mordell_sample_5e7_1e8.txt`: every 900th Mordell prime ≤ 10⁸, keeping
  those > 5·10⁷, 96 primes; `mgen_nonmordell_sample_5e7_1e8.txt`: random non-Mordell primes ≡ 1 (4), see file for the count completed):
  * on 𝔐, M_gen/L² ∈ [0.109, 0.140], mean 0.127, 46 % below c_V;
  * off 𝔐 (first 32 primes), mean 0.154 and none below c_V.
* **The violators.** Six of the seven L6(0) violators of SYNTH §2.3 (classes 241, 577, 409, 241, 577, 409) lie in
  𝔐★ \ 𝔐, at the sterile non-residues 3 mod 7 and/or 2 mod 5. There M_gen sees only (p/7) = −1 or (p/5) = −1 and credits
  the non-residue average, while §3.3 shows that these classes carry residue-class mass. The seventh, 12 252 497 ≡ 257,
  is p ≡ 2 (3) with R = 8.

*Reading (Assessment).* The η = 0 diagnostic is not evidence that X behaves better on 𝔐. On 𝔐 the 840 characters
contribute no genus mass, so M_gen is lower and the diagnostic is often vacuous, even at zeros. Off 𝔐 the genus term
over-credits sterile non-residue classes, so hard primes there violate it. A uniform lower bound for X stated against a
genus main term inherits this blind spot. The relevant local variable is (★)-sterility, which the genus term cannot
see.

## 4. Q1 numerically: (★) and ES coverings at 840·ℓ (CERTIFIED)

`scripts/z58_mordell_cover.py L {star|es}` marks every unit class mod L that lies in a complete hit class of a modulus
dividing L: for (★) the classes H_d, d | L; for ES the ET-shaped families of `BRAINSTORM/y7_mordell_levels.md`.
Unit classes are counted only when ≡ 1 (mod 4).

| L | ES menu: uncovered (squares + non-squares) | (★) menu: uncovered Mordell lifts (of all), non-squares among them |
|---|---|---|
| 840 | 6 (6 + 0) | 6 of 6, 0 |
| 9240 = 840·11 | 34 (30 + 4: 2041, 2521, 3361, 5161) | 48 of 60, 18 |
| 10920 = 840·13 | 40 (36 + 4) | 58 of 72, 22 |
| 14280 = 840·17 | 52 (48 + 4) | 88 of 96, 40 |
| 15960 = 840·19 | — | 90 of 108, 36 |
| 19320 = 840·23 | — | 108 of 132, 42 |

* The ES column reproduces y7 (34 at 9240).
* For the ES non-square classes mod 9240, refining by one further prime factor q ∈ {2, 3, 5, 7, 11, 13, 17, 19}
  (`z58_mordell_refine.py`) never covers all lifts. These lie on the sterile-point line of POINTWISE_MORDELL and
  NONCONG_LIFTS Thm 2.6 (x_{11,2}). Prior work; not pushed.
* For (★), the Mordell lifts covered at 840ℓ are just those with p mod ℓ in the hit set. That is 12 of 30 non-square
  lifts at ℓ = 11.
* Consistent with Cor S2, (★) case splits remove only a ≈ τ((ℓ + 1)/4)/ℓ-type fraction per prime. The rest of each
  non-residue fibre contains sterile points.

## 5. Q3 / M2: the representation p = x² + 840y²

*Fact (classical; numerically re-verified in the campaign to 10⁶, `ES_CONNECTIONS_TODO.md` Z0935).* 840 is idoneal, so a
prime p is x² + 840y² iff p mod 840 ∈ 𝔐. Then (x, y) is unique up to signs. (x, y) mod q carries Frobenius data of the ring
class field of conductor q of ℚ(√−210), which is non-abelian over ℚ.

**Proposition C1 (PROVED).** Let f ∈ ℤ[x, y] have degree 2 with top form f₂ irreducible over ℚ (e.g. f = x² + 840y²).
If U, B, C ∈ ℚ[x, y] \ {0} satisfy 4UBC − U − B = f identically, then at least two of U, B, C are constants.
Consequently the certificate is valid at an integer point iff f(x, y) lies in a fixed residue class:
* f ≡ −U (mod 4UC − 1) if U, C are constant;
* f ≡ −(U + B) (mod 4UB) if U, B are constant;
* f ≡ −B (mod 4BC − 1) if B, C are constant.
Such a certificate is a congruence condition on p = f(x, y).
*Proof.* Let α, β, γ be the degrees of U, B, C. The top homogeneous part of 4UBC is 4U_αB_βC_γ ≠ 0, of degree
α + β + γ. The top part of U + B has degree ≤ max(α, β), and f has degree 2.
* If α + β + γ > max(α, β, 2), the degree-(α+β+γ) part of the identity reads 4U_αB_βC_γ = 0, a contradiction. So
  α + β + γ ≤ max(α, β, 2).
* If α + β + γ = 2 and two of the degrees equal 1 (the third 0), then the degree-2 part reads 4U_αB_βC_γ = f₂, because
  U + B has degree ≤ 1. That is a product of two rational linear forms, contradicting irreducibility.
* In every remaining case at least two degrees are 0:
  * α + β + γ ≤ 1 leaves at least two zeros;
  * α + β + γ = 2 with a single positive degree;
  * α + β + γ = max(α, β) > 2 forces γ = 0 and min(α, β) = 0.
* The three congruence forms follow by solving the identity for the non-constant coordinate. ∎

*Reading.*
* Algebraically the representation adds nothing beyond p's residue class. So the polynomial stage of M2 is exactly B1:
  T1 for square classes, Thm S1 / Cor S2 for sterile non-square classes.
* Two non-polynomial uses remain:
  * the Frobenius data (x, y) mod q, which are fixed finite non-abelian data, inert on finite witness sets by (J)96;
  * the arithmetic of x and y (divisors of x ± ky, of y, …), which is a divisor-in-class lottery on integers of size
    ≤ √p, i.e. B2.
* No candidate rule was found worth testing on the zeros (F4 not applicable).

## 6. Verdict

**Narrowed.**
* Killed as scoped theorems:
  * finite (★) case splits on the sterile non-residue fibres of every Mordell class (Thm S1, Cor S2 for class 1;
    EVIDENCE for the other five);
  * algebraic use of the Mordell representation (Prop C1).
* Explained (EVIDENCE + PROVED Lemmas G0, G, O):
  * the six classes differ only in X;
  * the hard local set for (★) is cut out by sterility, not by quadratic residuosity;
  * the apparent "L6 holds on 𝔐" is the genus term's blind spot, not better behaviour of X.
* What survives:
  * (MS) itself;
  * any argument that uses the *large* prime factors of p + u or 4Cp + 1 (B2);
  * sterility-aware main terms. A local-density main term built from the actual hit classes, as in RESIDUE_HARDNESS,
    instead of from genus characters would at least not over-credit sterile non-residues. This is a main-term repair,
    not a positivity mechanism.

*Falsifier table re-stated:* §0′ (unchanged in substance from checkpoint 1; F2/F4 now filled with data). No HOT LEAD.

*Proposed FRONTIER text (do not edit FRONTIER here).*
* §2.4 / §4 item 15 addendum: "Mordell's classes for (★) (Z58_MORDELL). The genus term M_gen is the same function of
  ((p/q))_{q ≥ 11} on all six classes (Lemma O, PROVED), so class differences inside 𝔐 are order-≥3 effects in X
  (class 1 hardest). The (★)-hard set mod 840 is 22 classes: 𝔐 plus the Thm-S1-sterile non-residues 2 mod 5 and
  3 mod 7. It contains all 14 (★)-zeros and 38 𝔊*-zeros. Within 𝔐, sterile non-residue classes mod ℓ = 11–23 behave like
  residue classes, and hit classes carry no low-R primes (EVIDENCE). L6(0) holds at all nine Mordell (★)-zeros
  (M_gen < c_V L² there), and 6 of its 7 violators lie at sterile non-residues: the diagnostic measures the genus
  term's blind spot (Assessment)."
* §6 (closed): "(z58) Finite (★) case splits of {p ≡ 1 (M), p ≡ R (ℓ)} for x_{ℓ,R}-sterile R, e.g. every non-residue
  R ≤ (ℓ − 1)/2 → Z58_MORDELL Thm S1 / Cor S2 (PROVED; exact criterion). Algebraic use of p = x² + 840y² → Prop C1
  (PROVED: polynomial certificates are congruence certificates). Not covered: points of the other five classes
  (EVIDENCE only), non-polynomial use of (x, y)."

*Bottom line.* Mordell's six classes are hard for (★) because they are sterile at 3, 5 and 7 simultaneously, but they
are not special: sterile non-residue classes (2 mod 5, 3 mod 7, and their analogues at every ℓ) are just as hard, and
the genus term cannot tell them apart from easy non-residues. That explains the class statistics, the five
off-Mordell zeros and the L6(0) pattern. It gives no route to (MS). Every finite refinement is blocked by sterile
points (Thm S1), and the Mordell representation p = x² + 840y² carries no algebraic information beyond congruences
(Prop C1). B2 did not move.

## 7. Reproduction

* `uv run --with numpy python scripts/z58_mordell_cover.py L es|star`
* `python scripts/z58_mordell_refine.py 9240 es 2 3 5 7 11 13 17 19` (run from `scripts/`)
* `uv run --with sympy python scripts/z58_mordell_sterile1.py 100000 48`
* `uv run --with sympy python scripts/z58_mordell_sterile2.py 30000 60`
* `gcc -O2 -o /tmp/z58cs scripts/z58_mordell_classstats.c -lm && /tmp/z58cs 100000000 /tmp/mprimes.txt`
  (≈ 40 s, ≈ 300 MB)
* `uv run --with sympy python scripts/z58_mordell_bymod.py /tmp/mprimes.txt 1e7`
* M_gen: `gcc -O2 -o /tmp/z56mgen scripts/z56_famdesign_mgen.c -lm; /tmp/z56mgen < primes` (≈ 4.5 s per prime near
  10⁸)

All commands were run under `ulimit -v 4000000` and `timeout` ≤ 1800.

## 8. Internal review

TODO (hostile reviewer subagent).
