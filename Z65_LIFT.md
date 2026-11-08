# Z65_LIFT — characteristic-p construction + lifting for ES certificates (wave z65, lane LIFT). Verdict: DEAD as a construction route (two scoped theorems); no HOT LEAD

**ES is OPEN.** Nothing here proves or disproves ES, (MS) or any case of them. Labels: PROVED / CONDITIONAL (on what) /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal, unrefereed. Brief: `z52bbriefs/z65_lanes.md` §LIFT (+ z58
common rules, z53 depth brief). Scripts `scripts/z65_lift_*`, data `data/z65/lift/` (sources: `data/z65/lift/src/`,
PDFs/text of the arXiv versions read, accessed 2026-11-08). Checkpoint 1 (Theorem G + pre-registered kill tests):
commit 4c2ebc54d.

## 0. Bottom line

1. **SWZ's mechanism, extracted (§2, ✔ from arXiv:2609.20572v1).** Prime-degree Hurwitz existence is proved by building,
   over k = F̄_p, a *special stable G-map* with G ≤ S_p (p ∥ |G|, regular P = C_p, N(P) = P ⋊ F_p^×), and lifting it
   with Wewers's theorem. Primality enters in four places: the residue characteristic; Henrio's moment theorem (the
   parts of Λ ⊢ p are units of F_p with zero total and no zero proper sub-sum); C_{S_p}(P) = P (faithful tail
   characters); v_p(p!) = 1. The *discrete* data (profiles, hence σ_j = (r_j − 1)/(p − 1)) are given; char p is used
   to solve a *continuous* existence problem over F̄_p.
2. **Theorem G (PROVED; §3).** For a prime p ≥ 5, p ≡ 1 (4): an ES curve at p (Lemma A: (X, G) in char 0 with
   |G|(p − 4) = p(2g − 2)) has potentially good reduction at p **only if p ≡ 2 (mod 3)** and X/G has Mordell's signature
   ((p+1)/3, p, p(p+1)/3); conversely those exist. Hence "build a smooth curve with automorphisms in char p and lift
   it" (any Oort-type lifting theorem) yields exactly Mordell's p ≡ 2 (3) identity, and **every ES curve at every
   p ≡ 1 (mod 12) — all of 𝔐 — has bad reduction at p.** The proof is a Weierstrass-preparation fixed-point count
   (Lemmas G1–G3) plus p-adic valuations. Numerator-k version (Theorem G_k) identical: only (p+1)/(k−1)-identities.
3. **The bad-reduction branch (SWZ's actual engine) is order-transparent (§4, Prop O, PROVED from Raynaud–Wewers).**
   The signature of any lift is read off the char-p datum (tame indices on primitive tails, p × tame index of the
   central cover at wild points). So a char-p construction can only *realise* an ES triple supplied as input. Char-0
   realisation of any triple is already free (Riemann existence), so this is type I (Z64_EQUIV §5). Two sharper
   facts:
   * **Prop E.** Every abelian (in particular every cyclic, hence every Lemma-F (★)-) ES cover with bad reduction has
     *exceptional* stable reduction (σ = 1), outside the scope of Wewers's lifting theorem.
   * **Lemma S.** No Galois closure of a degree-p cover — SWZ's object class — is an ES cover.
4. **Where ES's prime/composite (T1) information lives (§5).** In SWZ the hard, prime-sensitive part is the
   *realisation of fixed discrete data*, and the geometry sees primality there. In ES, realisation is free at every n
   (squares included) and the whole content is the *discrete datum* (the triple). Lifting theorems preserve discrete
   data. So the mechanism is T1-blind by construction: at n = m² every geometric step succeeds and only "choose the
   triple" fails.

   **Precise missing lemma (§5.3):** an ES/(★)-equivalent *realisation* problem whose discrete data are fixed by p and
   whose realisability fails at squares — a "Hurwitz problem for (★)". None is known; the natural candidates are
   screened there.
5. **KT1 passed, KT2 fired (route DEAD as construction), KT3 passed** (§6). No HOT LEAD.

## 1. Mandatory falsifier table (final)

The mechanism under test: build in characteristic p an object Ω (curve with automorphisms; special G-deformation datum
/ stable G-map) and lift it to characteristic 0 so that the lift is an ES certificate at p via Lemma A of Z64_EQUIV.

| screen | behaviour |
|---|---|
| **F1 odd squares** | ES holds at m², so F1 bites only on (★)/Type II sub-statements. Every lift's signature is *read off* the char-p datum (Prop O; Theorem G's cluster count). So a (★)-certificate at m² would have to be present as input data, and none exists by T1. The geometric steps (curve, deformation datum, lifting) succeed for every triple at every n. **The mechanism is T1-blind**: it uses neither primality nor non-squareness except through "characteristic = p". The good-reduction branch produces only Mordell's identity with p = 3m − 1, which never fires at m² (squares are ≡ 0, 1 mod 3). |
| **F2 C-even / numerator 8** | Theorem G_k (§3.4) is numerator-uniform: for k/p the good-reduction survivors are exactly the identity (m, p, pm), (k − 1)m = p + 1 (KT3: k = 8, all primes ≤ 1500, CERTIFIED; plus the spherical sporadic (2, 2, 7) at p = 7). Prop O and Lemma S are numerator-blind. Nothing distinguishes C odd from C even. |
| **F3 composites** | The residue characteristic is prime by definition. At composite n the mechanism is undefined except through a prime factor ℓ \| n, where ES is inherited anyway. Primality enters only as "the characteristic", so it cannot see the 285 composite R-zeros, Z₇ or 4545. |
| **F4 known zeros** | All 14 (★)-zero primes and all 𝔐 primes are ≡ 1 (mod 3) (checked from `star_prime_zeros.txt`). By Theorem G every ES certificate there has bad reduction. The good-reduction branch "proves" ES only at p ≡ 2 (3), where Mordell already does, so it proves nothing false at the zeros. The bad-reduction branch proves nothing by itself (type I). |

**No HOT LEAD.**

## 2. Precise statements; SWZ's mechanism

### 2.1 Statements (labels as stated)
* **ES(p) and Lemma A** (Z64_EQUIV E3, PROVED there). For a prime p ≡ 1 (mod 4), ES(p) ⟺ there is a compact Riemann
  surface X of genus g ≥ 2 and a finite G ≤ Aut(X) with |G|(p − 4) = p(2g − 2). Moreover every such (X, G) has
  X/G ≅ P¹ with exactly three cone points, of orders (x, y, z) with 1/x + 1/y + 1/z = 4/p (Z64_EQUIV, Corollary to
  Lemma A). Call (X, G) an **ES curve at p** and (x, y, z) its **signature**. Everything is algebraic and defined over
  Q̄, so we may work over Q̄_p or ℂ_p.
* **Mechanism (Ch-ES).** Construct Ω over k = F̄_p and lift. Two branches:
  * **(GR) good reduction.** Ω is a smooth projective curve X_k with a faithful G-action. The lift is a smooth
    relative curve over a mixed-characteristic DVR R with G-action (lifting theorems: Grothendieck tame; Sekiguchi–
    Oort–Suwa, Green–Matignon, Obus–Wewers + Pop for cyclic G; Bouw–Wewers for D_p).
  * **(BR) bad reduction.** Ω is a special stable G-map / special G-deformation datum (Raynaud 1999, Wewers 2003). The
    lift is a three-point G-cover whose stable reduction is Ω (Wewers JAMS 2003 Thm 3; SWZ Thm 4.8).
* **Brief's questions.** (1) SWZ's mechanism; (2) can (GR)/(BR) produce ES certificates, and where does T1 bite;
  (3) a theorem, a precise obstruction, or a precise missing lemma.

**Why not already closed.** Z64_EQUIV Lemma H (conditional on SWZ) shows only that prime-degree *realisability* carries
no (★) information. It does not test the *mechanism* on the ES dictionary rows. `git grep` finds no prior repo
analysis of reduction types of ES covers: 0 hits for "potentially good", "Oort" (in this sense), "deformation datum"
or "Wewers" outside Z64_EQUIV's precedent row and its source file.

### 2.2 SWZ step by step (✔ read in `data/z65/lift/src/swz.txt`)
* **M1 (reduction to three branch values; §3).** Every compatible prime-degree datum is reduced to three-point data
  by EKS fusion (Prop 3.1 = EKS Lemma 4.2, Cor 4.4, Lemma 4.5, Props 5.2–5.3; Lemma 3.3). Odd degree is used in the
  fusion cases.
* **M2 (primitive tails from Henrio moments; §5).** For Λ = (e_1, …, e_r) ⊢ p, 2 ≤ r ≤ p − 1, Henrio's moment
  criterion (Thm 5.1, citing Henrio Def 3.14, Prop 3.16(b)) gives distinct a_j ∈ F̄_p with Σ e_j a_j^q = 0 for
  1 ≤ q ≤ r − 2. **Here primality is used**: e_j ∈ F_p^×, Σ e_j = p ≡ 0, and no proper sub-sum vanishes, because proper
  sub-sums lie strictly between 0 and p.

  Then P_Λ = ∏(y − a_j)^{e_j} satisfies P_Λ′ = c∏(y − a_j)^{e_j − 1} (Lemma 5.3). So P_Λ is a degree-p cover
  P¹ → P¹ with only two branch values: Λ over 0 and a totally wild point over ∞. In characteristic 0 this is
  impossible by Riemann–Hurwitz; wild ramification absorbs the missing branching.

  Its Galois closure is a special primitive tail with inertia P ⋊ C_{m_Λ} and σ = h/m = (r − 1)/(p − 1)
  (Lemma 5.5, via the local different formula, Lemma 5.4). Lemma 5.4 also uses C_{S_p}(P) = P to make the
  character faithful.
* **M3 (central logarithmic datum, §7; new tail, §6).** A cyclic cover Z → P¹ of degree m | p − 1 with Kummer
  exponents a_j, and a Cartier-fixed logarithmic differential with prescribed divisor (Def 7.1, citing Wewers ENS 2003
  Def 3.1). The numerical constraint is the vanishing-cycle identity Σσ_j (+ new tail) = 1 with denominators dividing
  p − 1, which is exactly compatibility (1.1).
* **M4 (assembly and lifting, §8, Thm 4.8).** The tails are aligned inside one G ≤ S_p containing a common regular
  P = C_p (Lemma 8.1, using N_{S_p}(P) = P ⋊ F_p^×, Lemma 2.5, and v_p(p!) = 1). Wewers's lifting theorem
  (JAMS 2003 Thm 3 / Cor 4.6) then gives a characteristic-0 three-point G-cover. Tame inertia on primitive tails is
  preserved (Lemma 4.7).
* **M5.** The degree-p quotient by a point stabiliser has the prescribed profiles (Lemma 2.3); descend to ℂ.

**Reading.** The discrete data (Λ_1, Λ_2, Λ_3; hence G ≤ S_p, the m_j and σ_j) are **given** by the datum. The
characteristic-p work is a **continuous** existence problem over F̄_p: points a_j solving moment equations, and a
logarithmic differential with prescribed divisor. Primality makes that problem solvable (M2) and makes the pieces fit
in one group (M4). The composite-degree failures (EKS Prop 5.7) are visible in the group theory: blocks and
imprimitivity.

## 3. Theorem G: the good-reduction branch gives only Mordell's identity

**Theorem G (PROVED, from the standard facts named in G0 and Z64_EQUIV Lemma A + Corollary, internal).** Let p ≥ 5 be a prime, p ≡ 1 (mod 4). Let K be a
characteristic-0 field complete for a discrete valuation with residue characteristic p. Let X/K be a smooth projective
geometrically connected curve and G ≤ Aut_{K̄}(X) finite with |G|(p − 4) = p(2g − 2). If X has potentially good
reduction, then p ≡ 2 (mod 3) and X/G has signature (0; m, p, pm), m = (p + 1)/3. This is the curve form of Mordell's
identity 4/p = 1/m + 1/p + 1/(pm).

Conversely, for every prime p ≡ 2 (mod 3), p ≥ 5, such (X, G) with good reduction exist. G is cyclic of order pm, and
the special fibre is z^m = y^p − y.

*Corollary (PROVED).* For every prime p ≡ 1 (mod 12) every ES curve at p has bad reduction at p. This includes every
prime in 𝔐 mod 840 and the 14 (★)-zero primes. So no Oort-type construction (a smooth char-p curve with automorphisms,
lifted equivariantly) gives ES at any p ≡ 1 (mod 12).

### 3.1 Proof

**G0 (set-up; standard).**
* After a finite extension of K and completion of the maximal unramified extension, we may assume the residue field
  k is algebraically closed and X has good reduction: there is a smooth proper model X_R over the valuation ring R.
  g ≥ 2 since p ≥ 5.
* A smooth proper model of a curve of genus ≥ 1 is its minimal regular model, hence unique. So G acts on X_R
  (uniqueness of minimal models, Lichtenbaum–Shafarevich; e.g. Liu, *Algebraic Geometry and Arithmetic Curves*
  §9.3 — V2, textbook).
* **G acts faithfully on X_k.** Suppose g ≠ 1 acts trivially on X_k. By smooth proper base change,
  H¹_ét(X_K̄, ℚ_ℓ) ≅ H¹_ét(X_k, ℚ_ℓ) G-equivariantly (ℓ ≠ p). So g acts trivially on H¹ of the characteristic-0
  curve, and the Lefschetz number is 2 − 2g < 0. But a non-trivial finite-order automorphism of a curve in
  characteristic 0 has finitely many fixed points, each of multiplicity 1, so its Lefschetz number is
  #Fix ≥ 0. Contradiction.
* For a closed point τ̃ ∈ X_k with stabiliser (= inertia, as k is algebraically closed) I ≤ G, the completed local
  ring of X_R at τ̃ is R[[Z]], with I acting R-linearly. For g ∈ I ∖ {1} put i(g) := ord_z(ḡ(z) − z). This is finite
  because the action on X_k is faithful, and a non-identity automorphism of a curve is non-trivial on every formal
  neighbourhood.
* Serre, *Local Fields* IV §1–2: I = P ⋊ C_m with P the (normal) p-Sylow and p ∤ m. Moreover i(g) = 1 for
  g ∈ I ∖ P, and i(g) ≥ 2 for g ∈ P ∖ {1}.

**Lemma G1 (fixed points; Weierstrass).** Let D be the open unit disc over ℂ_p, i.e. the points of X_K(ℂ_p) that reduce
to τ̃. Every g ∈ I ∖ {1} has exactly i(g) fixed points in D, all simple.

*Proof.* g(Z) − Z ∈ R[[Z]] reduces to ḡ(z) − z ≠ 0, of order i(g). By Weierstrass preparation it is a unit times a
distinguished polynomial of degree i(g), so it has i(g) zeros in D counted with multiplicity. At a fixed point w,
g′(w) is a root of unity (g has finite order and is linearisable at w in characteristic 0). If g′(w) = 1, g would be
the identity near w, hence everywhere. So all zeros are simple. ∎

**Lemma G2 (cluster identities).** Let τ be the image of τ̃ in X_k/G. Let c_1, …, c_s be the cone points of X_K/G whose
G-orbits meet D (the *cluster* of τ). Write e_i for their orders, π_i for the p-part of e_i, and e′_i = e_i/π_i. Then:
* (a) Σ_i (1 − 1/e′_i) = 1 − 1/m;
* (b) Σ_i (|P| m/e_i)(π_i − 1) = Σ_{g ∈ P∖1} i(g) ≥ 2(|P| − 1).

*Proof.*
* If g ∈ G fixes w ∈ D, then g fixes the specialisation τ̃, so Stab_G(w) ≤ I. Hence the G-orbit of a cone point meets
  D in exactly one I-orbit, of size |I|/e_i. Its stabilisers are conjugate cyclic groups of order e_i. Since P is the
  unique Sylow-p of I, each stabiliser meets P in its Sylow-p, of order π_i.
* For (a), count pairs (g, w) with g ∈ I ∖ P, w ∈ D and gw = w. By G1 and i(g) = 1, there are |I| − |P| of them.
  Counting by points instead gives Σ_i (|I|/e_i)(e_i − π_i). Divide by |I| = |P| m.
* For (b), count pairs with g ∈ P ∖ {1}. By points this gives Σ_i (|I|/e_i)(π_i − 1). By G1 it is Σ_{g∈P∖1} i(g),
  which is ≥ 2(|P| − 1). ∎

(G2(a) is the local "conservation of the different" (Green–Matignon's different criterion, [GM98 I 3.4] as stated in
Obus's survey arXiv:1703.01191 Prop 6.2, ✔), resolved into its tame and wild parts.)

**Lemma G3 (cluster shapes).** (i) If I = 1 the cluster is empty. (ii) If τ is tame (P = 1, m ≥ 2) the cluster is a
single cone point of order m. (iii) If τ is wild (P ≠ 1) the cluster has ≥ 2 points. If m ≥ 2, exactly one of them has
e′ = m and all others are pure p-powers (e = π ≥ p). If m = 1, all of them are pure p-powers.

*Proof.* Each non-zero term 1 − 1/e′ in (a) is ≥ 1/2, while 1 − 1/m < 1. So at most one term is non-zero; it equals
1 − 1/m, and it is present iff m ≥ 2. This gives (i) and (ii). In (iii), suppose the cluster had a single point. Then
(b) would read (|P|/π)(π − 1) < |P| ≤ 2(|P| − 1), a contradiction. ∎

**G4 (assembly).** By §2.1, X_K/G ≅ P¹ with three cone points (x, y, z), Σ1/· = 4/p, and each lies in exactly one
cluster. Since 4/p = Σ1/· forces p | lcm(x, y, z), some cone point has p | e. Its stabiliser lies in I_τ, so τ is wild.
Two wild clusters would need ≥ 4 points by G3(iii). So there is exactly one wild cluster W, with |W| ∈ {2, 3}; any
remaining point is a tame singleton of order prime to p.
* **|W| = 3.** All but at most one of x, y, z are p-powers.
  * If all three are p^{b_i}, put B = max b_i; then 4p^{B−1} = Σ p^{B − b_i}. B = 1 gives 4 = 3. B ≥ 2 gives
    #{i : b_i = B} ≡ 0 (mod p), impossible since that count is between 1 and 3 < p.
  * If exactly one, x = π m′ with m′ ≥ 2 prime to p, is not a p-power, then 1/x = 4/p − p^{−b_2} − p^{−b_3} has
    p-power denominator, so m′ | p^B: a contradiction.
* **|W| = 2, plus a tame singleton x** (p ∤ x).
  * If m = 1 both cluster points are p-powers, and 1/x = 4/p − p^{−b_1} − p^{−b_2}. Then v_p(1/x) < 0, except when
    b_1 = b_2 = 1, which gives 1/x = 2/p. Both are impossible.
  * So m ≥ 2 and the cluster is {π_1 m, p^b}. If π_1 = 1, then 1/x + 1/m = 4/p − p^{−b} has v_p < 0 while the left
    side has v_p ≥ 0. Impossible.
  * So π_1 = p^a with a ≥ 1, and 1/x = 4/p − 1/(p^a m) − 1/p^b must have v_p ≥ 0.
  * If a ≠ b, the term with exponent max(a, b) ≥ 2 is the unique term of minimal valuation, so v_p < 0. Impossible.
  * If a = b ≥ 2: 1/x = (4p^{a−1}m − m − 1)/(p^a m). The numerator is prime to m, so it is p^j with j ≤ a. It is
    ≥ (4p^{a−1} − 1)m − 1 > p^{a−1}, so j = a and m = (p^a + 1)/(4p^{a−1} − 1). But 4(p^a + 1) ≡ p + 4 modulo the
    odd number 4p^{a−1} − 1, which forces 4p^{a−1} − 1 ≤ p + 4. That is false for a ≥ 2, p ≥ 5.
  * If a = b = 1: 1/x = (3m − 1)/(pm). Since p ∤ x, p | 3m − 1. Since gcd(m, 3m − 1) = 1, 3m − 1 | p, so 3m − 1 = p
    and x = m. ∎

**Converse.** Let p ≡ 2 (mod 3) and m = (p+1)/3. Put X_k : z^m = y^p − y with G = ⟨y ↦ y + 1⟩ × ⟨z ↦ ζ_m z⟩ ≅ C_{pm}.
* X_k → X_k/G = P¹_t (t = z^m) has a wild point over t = ∞, with inertia C_{pm} and lower jump m (the Artin–Schreier
  conductor of y^p − y = z^m at z = ∞). It has a tame point over t = 0, of order m.
* g = (p − 1)(m − 1)/2, so 2g − 2 = (p − 4)(p + 1)/3 and (2g − 2)/(pm) = (p − 4)/p.
* Cyclic actions with v_p(|G|) = 1 lift (Sekiguchi–Oort–Suwa; in general Obus–Wewers + Pop: Obus survey
  arXiv:1703.01191 Thm 1.15 and §5.1, ✔; Obus–Wewers arXiv:1203.5057 ✔ abstract). The lift is an ES curve at p
  with good reduction, so by Theorem G its signature is (m, p, pm).
* Example p = 5 (check by hand): y² = x⁵ − 1 with x = 1 + ct, c⁴ ~ 5, reduces to Y² = t⁵ + āt, which is smooth of
  genus 2. ∎

### 3.2 Checks (CERTIFIED, arithmetic half; KT1)
* `scripts/z65_lift_goodred_check.py 1500 4` → `data/z65/lift/kt1_goodred_1500.txt`. All 11 800 representations
  4/p = 1/x + 1/y + 1/z for primes 5 ≤ p ≤ 1500 were tested against the cluster conditions of G3/G4, over every
  partition. The survivors are exactly the 122 Mordell triples (m, p, pm), one for each p ≡ 2 (3) in range. There are
  0 non-Mordell survivors.
* No representation in this range has p² dividing a denominator. This is consistent with the a = b ≥ 2 case of G4
  being empty; the brute force does not assume it.
* `goodred_check_400.txt`: the same at p ≤ 400, by an independent (Fraction-based) enumerator, with identical output.
* G2 on the converse example. The cluster at t = ∞ is {pm, p}; the m-point is the C_{pm}-fixed point, and the p-point
  has m preimages. (a): (1 − 1/m) + 0 = 1 − 1/m ✓. (b): (p − 1)·1 + (p − 1)·m = (p − 1)(m + 1) = (p − 1)(h + 1) with
  h = m = i(g) − 1 ✓.

### 3.3 Scope and remarks
* p ≡ 3 (mod 4) is excluded only because Lemma A then allows other signatures (4/p is a two-term fraction). ES is
  trivial there anyway.
* Theorem G is about potentially good reduction of the **curve** X: branch points may collide. Raynaud/Obus's notion of
  good reduction of the **marked cover** (branch points 0, 1, ∞ kept apart) is stronger, and fails whenever p divides
  a ramification index (Obus arXiv:1208.3909 §1, ✔). G1–G3 make this quantitative: every wild point carries a cluster
  of ≥ 2 colliding branch points.
* Novelty (Assessment): the ingredients are standard (Weierstrass preparation, Green–Matignon conservation); the
  application to ES curves and the classification are new to the repo. Folklore-adjacent.

### 3.4 Numerator k (F2; Theorem G_k, PROVED by the same proof)
Let k ≥ 4, p > k prime (so k/p < 1) with p ∤ k(k − 1)(k − 2), and (X, G) with X/G of signature (0; x, y, z), Σ1/· = k/p. If X has
potentially good reduction, then (k − 1)m = p + 1 and the signature is (m, p, pm).

*Changes to G4:*
* |W| = 3 needs k = 3.
* The a = b ≥ 2 case gives (kp^{a−1} − 1) | (p + k), which is impossible.
* π_1 = 1 or m = 1 need p | k − 1 or p | k − 2 respectively.

*KT3 (CERTIFIED).* `z65_lift_goodred_check.py 1500 8` → `kt3_goodred_num8_1500.txt`: 4 965 representations of 8/p;
the survivors are the 39 triples (m, p, pm) with 7m = p + 1, plus (2, 2, 7) at p = 7 (excluded by p ∤ k − 1; it is
spherical, Σ > 1).

## 4. The bad-reduction branch (SWZ's engine) is order-transparent

Sources ✔: Wewers, *Three point covers with bad reduction*, JAMS 16 (2003), arXiv:math/0205026v2
(`data/z65/lift/src/math_0205026.txt`); Obus arXiv:1208.3909v3.

* **Wewers Thm 2.** If p ∥ |G| and a three-point G-cover has bad reduction, then X̄ is the original component X̄₀ ≅ P¹_k
  plus tails meeting X̄₀ once each. Over X̄₀ the map is Frobenius followed by a Galois cover Z̄₀ → X̄₀. Over the tails
  the map is Galois, wild at the attachment point and tame at the specialised branch points.
* **Wewers Lemma 1.4 (Raynaud), (3)/(4).** A branch point with index n_j prime to p specialises to a primitive tail,
  and the tail cover has index **n_j** there. A branch point with index n_j = p n′_j specialises to a non-tail
  component, and Z̄_v → X̄_v has index **n′_j** there.
* **Cor 1.11 (vanishing cycles).** Σ_{prim} σ_j + Σ_{new}(σ_j − 1) = 2g_X − 2 + |B₀| = 1 for three-point covers, with
  σ_j = 0 at wild branch points and σ_j > 1 at new tails (Raynaud).
* **Def 2.1.** The *exceptional* cases are B_prim = {j₀}, B_new = ∅, σ_{j₀} = 1, and B_prim = ∅, B_new = {j₀},
  σ_{j₀} = 2.
* **Def 2.7.** A special deformation datum has σ_j < 2, σ_j ≠ 1, and exactly three σ_j < 1.
* **Thm 3.** Every special G-map lifts to a three-point G-cover.
* **Obus Lemma 3.5** (citing his Lemma 2.20/4.2 in 2012b). σ_b ∈ (1/m_G)ℤ with m_G = |N_G(P)|/|Z_G(P)|.

**Proposition O (order transparency; PROVED from Lemma 1.4).** Let p ∥ |G| (the standing hypothesis of Wewers's
paper and of SWZ Thm 4.8), let f̄ be a special G-map and f any lift (Wewers Thm 3). The signature of f is
* n_j = the tame index of the primitive-tail cover at x̄_j, for j ∈ B_prim;
* p·n′_j with n′_j = the index of Z̄₀ → X̄₀ at x̄_j, for j ∈ B_wild.

All of these are discrete invariants of f̄. Hence the (BR) branch yields an ES certificate at p iff the char-p datum
f̄ *already carries* an ES triple in these invariants. ∎

*Consequence (Assessment, made precise by Prop O).* Any three-point signature with Σ1/· < 1 is realised in
characteristic 0 by Riemann existence plus residual finiteness of triangle groups. So the (BR) branch adds no
existence power for ES: it can realise a triple that is given, and the given triple is the whole content of ES(p).
This is type I in Z64_EQUIV §5's classification, now verified for the lifting theorem itself.

**Proposition E (PROVED from Obus Lemma 3.5 + Wewers Cor 1.11).** Let f be a three-point G-cover with cyclic p-Sylow,
bad reduction, and m_G = 1 (for example G abelian). Then its stable reduction is exceptional. In particular, if G is
abelian:
* a Type II ES cover has σ_x = 1 at its tame point (exceptional case (1)), so it is not the lift of any special G-map;
* there are no abelian Type I ES covers (directly: in an abelian group, if p divides ord(a) but not ord(b), then p
  divides ord(ab)).

*Proof.*
* The σ's are integers. σ > 0 on primitive tails and σ ≥ 2 on new tails, while the sum in Cor 1.11 is 1. So either
  one primitive tail has σ = 1 and there are no new tails, or there are no primitive tails and one new tail has σ = 2.
* A Type II cover has exactly one tame point, so B_prim ≠ ∅, and the first case holds.
* A Type I cover would have two primitive tails, with sum ≥ 2. Consistently, Harvey's lcm condition already excludes
  cyclic realisations of Type I triples. ∎

So every Lemma-F (★)-cover (Z64_EQUIV E11: cyclic, order puBC, p ∥) has bad reduction *as a marked cover*. That is
automatic, since p divides a ramification index (Obus arXiv:1208.3909 §1; quantitatively G3). At p ≡ 1 (12) it has
bad reduction even as a curve (Theorem G), and in all cases its stable reduction is exceptional.

Consistency check: the Mordell covers (m, pm, p) are the Lemma-F covers with (u, B, C) = (1, m, 1). Their marked
stable reduction is exceptional (σ_x = 1; Z̄₀ is the C_m-Kummer line branched at two points), while the curve has
good reduction (Theorem G converse). The components over X̄₀ are rational and are contracted in the stable model of
the curve. There is no contradiction: the two notions of good reduction differ. Wewers's lifting theorem, and hence SWZ's engine, never reaches them. The engine needs non-abelian G
with m_G ≥ 2. For example G = PSL₂(F_q) with p ∥ |G| has m_G = 2, which forces σ_x = 1/2 and one new tail with
σ = 3/2. Any ES triple can be realised so (Macbeath generation, V2); nothing is gained.

**Lemma S (PROVED; SWZ's object class is disjoint from ES curves).** Let G ≤ S_p be the monodromy group of a
three-point degree-p cover with profiles Λ₁, Λ₂, Λ₃. Its Galois closure has signature (lcm Λ_i). It is never an ES
curve at p.

*Proof.*
* An element of S_p has order divisible by p iff it is a p-cycle.
* If no Λ_i = [p], then p ∤ lcm.
* If exactly one Λ_i = [p], then 1/lcm Λ₂ + 1/lcm Λ₃ = 3/p with p ∤ both: impossible (denominator).
* If two are [p], then 1/lcm Λ₃ = 2/p: impossible.
* Three gives 3/p ≠ 4/p.
* By Lemma A no other signature occurs at p ≡ 1 (4). ∎

**KT2 (pre-registered decision rule).** It fires: both lifting theorems that reach ES curves (Oort-type for (GR),
Wewers for (BR)) determine the lifted ramification orders from the char-p datum (G1–G3, Prop O). So (BR) is **DEAD as a
construction of ES certificates.** It would revive only if some step produced discrete data not chosen in advance; see
§5.3.

## 5. Where the mechanism uses primality, and the precise missing lemma

### 5.1 Comparison (Assessment, built on §§2–4)

| | SWZ (Hurwitz, degree p) | ES via lifting |
|---|---|---|
| discrete data | given (profiles Λ_i) | the unknown (the triple (x, y, z)) |
| char-0 realisation of given discrete data | hard (group theory: a permutation triple in S_p) | free (Riemann existence, any G) |
| what char p solves | continuous existence over F̄_p (Henrio moments, logarithmic differentials) | nothing new: lifts preserve discrete data (G1–G3, Prop O) |
| where primality acts | characteristic; F_p-units summing to 0 (M2); C_{S_p}(P) = P; v_p(p!) = 1 | characteristic only. In (GR) it forces the wild cluster shape (G3), which leaves only Mordell |
| composite / square failures | EKS 5.7: imprimitive data, seen by the group theory | T1: no triple at m², seen by nothing geometric |

### 5.2 T1 (brief item "at n = m² the construction must fail — where?")
For (★)/Type II at n = m², every geometric step is available for every candidate triple: curves, covers, deformation
data and lifts all exist for any signature with Σ < 1. The construction fails only because the triple does not exist
(T1), which is the input. So the mechanism does not "fail" at m² in any geometric step. It is input-transparent, and
any T1-sensitivity would have to be put in by hand. The (GR) branch is the one place where char p imposes something
(G3). What it imposes, p = 3m − 1, is a congruence: Mordell's identity, which never fires at squares.

### 5.3 The precise missing lemma, and screened candidates
For an SWZ-type proof one needs:

> **(H★) A realisation problem for (★).** A family of discrete data 𝒟(p), determined by p alone (e.g. branch data of
> some degree d(p) over some base orbifold), such that 𝒟(p) is realisable ⟺ (★)(p) (or ⟹ ES(p)) for primes p in 𝔐,
> and 𝒟(m²) is non-realisable by an obstruction that "sees" squareness.

Then char-p construction + lifting could attack realisability of 𝒟(p), as in SWZ. Screened candidates:
* **Degree d(p) = p:** every datum is realisable (SWZ, conditional), so it carries no information (Z64_EQUIV Lemma H).
  Galois closures never give ES (Lemma S).
* **Uniform data from the ES curve itself** (Lemma A, E13, Lemma F): the data are the triple (type I).
* **Data fixed by p via a quotient of the (★)-cover.** The cyclic Lemma-F cover C_{puBC} has degree-p quotient
  z^p = t (two branch points, trivial) and degree-uBC quotient Z̄₀ (tame, indices (uBC, BC, uC), again the triple).
  Every quotient sees either nothing or the witness.
* **Degree 4Cp + 1 with a forced block system of size d ≡ −1 (mod 4C)** (imprimitivity ↔ the divisor of the
  divisor form). This is the only shape found in which composite-degree Hurwitz obstructions (EKS-type,
  block/imprimitivity) could encode a divisor in a residue class. No datum forcing such a block size is known, and C
  is again a free parameter. Open; Assessment: unlikely, but it is the one form of (H★) not excluded here.
* **Uniform-in-p families (trivial lemma PROVED; the rest Assessment).** If 𝒟(p) is the fibre over p of a finite-type scheme over ℤ
  and "realisable" means "has an F̄_p-point", then by Chevalley the set of good p is finite or cofinite. A cofinite
  answer from a fixed family with bounded group would give polynomial-type identities, which are barred on unit-square
  classes (Elsholtz–Tao Prop 1.6, T1). So 𝒟(p) must grow with p, as SWZ's S_p does.

### 5.4 The other EQUIV rows in characteristic p (brief item (2); short)
* **E4 (lct) has a genuine char-p analogue, the F-pure threshold, and it is a T1-blind relaxation (PROVED from
  Hernández, arXiv:1112.2425 Thm 3.1, ✔).**
  * Hernández Thm 3.1: fpt(x^a + y^b + z^c) = ∑⟨1/d⟩_L + 1/p^L, where L is the last digit position (base p,
    non-terminating expansions) at which the digits of 1/a, 1/b, 1/c add without carrying.
  * For every prime p ≥ 5, take a = b = c = (p+1)/2. Then 1/d = 0.1 (p−2) … in base p, the first digits add to
    3 ≤ p − 1, and the second digits add to 3(p − 2) > p − 1. So L = 1 and fpt_p = 3/p + 1/p = **4/p**. Checked exactly for all primes 5 ≤ p < 2000
    (`scripts/z65_lift_fpt_check.py` → `data/z65/lift/fpt_check.txt`, CERTIFIED).
  * So the char-p version of "4/p is a threshold of a Brieskorn–Pham germ" holds at every prime, uniformly. Its lct
    is 6/(p+1) ≠ 4/p. fpt does not lift: fpt ≤ lct, with equality e.g. when no carrying occurs (L = ∞, for instance
    p ≡ 1 mod lcm(a, b, c)). The statement is blind to the arithmetic of ES.
  * This illustrates in one line why char-p analogues of the dictionary rows relax away the content.
* **E2 (stacky line P(u, B), O(p) ≅ ω ⊗ π*O(4C))** is a degree identity, valid verbatim in every characteristic.
  Char p adds nothing.
* **E5/E6 (Seifert manifolds, lens spaces, plumbings)** are topological; their algebraic avatars are E3/E11 (covers),
  treated above.
* **E9/E10 (ray classes, ℤ[√−p])**: reduction mod p is the Frobenius dictionary already covered by
  Z60_RAYCLASS.

## 6. Kill tests (pre-registered at checkpoint 1, commit 4c2ebc54d) — outcomes
* **KT1 (kill Theorem G): PASSED.** 0 non-Mordell survivors among 11 800 representations (p ≤ 1500); G2 checked
  exactly on the converse example. (CERTIFIED / PROVED)
* **KT2 (decision on (BR)): FIRED → DEAD as construction.** Order transparency is verified in the source (Wewers
  Lemma 1.4(3)(4), Thm 3; SWZ Lemma 4.7). (PROVED from sources)
* **KT3 (F2 twin): PASSED.** Numerator 8 shows only the identity pattern 7m = p + 1 (p ≤ 1500), and the proof
  generalises (Theorem G_k).

## 7. Verdict, proposed FRONTIER text, bottom line

**Verdict: DEAD (as a construction route), with two new scoped theorems; no HOT LEAD.** Scope: this is a statement
about the two lifting branches as constructions (Theorem G, and Prop O with the pre-registered KT2 rule). It is not a
theorem that no characteristic-p argument could bear on ES. The escape (H★) and canonical char-p objects with forced
invariants remain open (§5.3).
* **Strengthened (small, PROVED):**
  * Theorem G / G_k: ES curves have potentially good reduction at p only for Mordell's p ≡ 2 (3) signature;
  * Corollary: every ES curve at p ≡ 1 (12) (all of 𝔐, all (★)-zeros) has bad reduction;
  * Prop E: cyclic/abelian ES covers have exceptional reduction, outside Wewers lifting;
  * Lemma S: SWZ's degree-p objects are never ES curves.
* **Narrowed / dead:**
  * (GR) dead (Theorem G);
  * (BR) dead as a construction (Prop O, type I).
* **Surviving:** only (H★), an ES-equivalent realisation problem with p-determined data. No candidate is known.

**Proposed FRONTIER text (§3 or z65 block; not applied here):**
> *(z65 LIFT, `Z65_LIFT.md`; internal.)* SWZ's prime-degree Hurwitz mechanism has two parts. Discrete data are fixed;
> a continuous existence problem is solved over F̄_p (Henrio moments, primality via F_p-units with no zero sub-sum);
> the result is lifted by Wewers's theorem.
>
> Applied to ES curves (Lemma A):
> * Good reduction: an ES curve at p has potentially good reduction only for Mordell's signature
>   ((p+1)/3, p, p(p+1)/3), p ≡ 2 (3) (Theorem G; Weierstrass fixed-point count). So every ES curve at every
>   p ≡ 1 (12) has bad reduction, and Oort-type lifting yields only Mordell.
> * Bad reduction: the lifted signature is read off the char-p datum (Raynaud–Wewers), so lifting only realises a
>   given triple (type I). Cyclic (★)-covers even have exceptional reduction, outside Wewers lifting.
>
> The mechanism is T1-blind: at squares every geometric step succeeds and only the triple is missing. What is missing
> for an SWZ-type proof is (H★), a realisation problem for (★) whose data are fixed by p and which fails at squares.

**Bottom line.** Characteristic p and lifting are powerful when the hard part of a problem is to *realise* given
discrete data. SWZ's Hurwitz theorem is such a problem, and there primality is visible inside the geometry. ES is the
opposite: realisation is free at every n, and the whole difficulty is the discrete datum. Lifting theorems carry
discrete data across unchanged. The one place where char p does constrain ES curves, potentially good reduction, is now
completely classified: it is Mordell's p ≡ 2 (mod 3) identity and nothing else. So this route is dead unless someone
finds (H★), a Hurwitz-type realisation problem with p-determined data equivalent to (★). Nothing here suggests that it
exists.

## 8. Sources (✔ = read by me in the downloaded text, `data/z65/lift/src/`)
* ✔ Song–Wen–Zhang, arXiv:2609.20572v1: Thm 1.1, Lemma 2.3, 2.5, Prop 3.1, Lemma 3.3, Def 4.1–4.6, Lemma 4.7,
  Thm 4.8, Thm 5.1, Lemmas 5.2–5.5, Def 7.1, Lemma 7.2, Lemma 8.1, 8.2, §8 end, §9. Claimed, unrefereed.
* ✔ Wewers, JAMS 16 (2003), arXiv:math/0205026v2: Thms 1–3 (intro), Def 1.3, Lemma 1.4, Prop 1.10, Cor 1.11,
  Def 2.1, Prop 2.2, Def 2.7.
* ✔ Obus, *Good reduction of three-point Galois covers*, arXiv:1208.3909v3: abstract, §1, Thm 5.2, §3 (stable model,
  Lemma 3.1, 3.2, Def 3.4, Lemma 3.5, Thm 3.6).
* ✔ Obus, *Lifting of curves with automorphisms*, arXiv:1703.01191v2: Thm 1.15 (Oort conjecture, [OW14], [Pop14]),
  §5.1 (local Oort groups; SOS89 for v_p ≤ 1), Prop 6.2 (different criterion, [GM98 I 3.4]).
* ✔ (abstract/title only) Obus–Wewers arXiv:1203.5057; Pop arXiv:1203.1867.
* ✔ Hernández, *F-invariants of diagonal hypersurfaces*, arXiv:1112.2425v1: Def 2.1, 2.3, 2.5, Thm 3.1.
* V2 (textbook, not re-read): Serre *Local Fields* IV §1–2 (ramification groups, I = P ⋊ C_m, Prop 9 character
  relation); Liu §9.3 (minimal models); smooth proper base change; Lefschetz fixed-point formula; Macbeath (PSL₂
  generation; used only in a remark).

## 9. Review log
* **Hostile reviewer subagent: could not run.** Three attempts (`subagent` deep mode ×2, `review` tool ×3,
  2026-11-08) failed with "authentication token has expired". This is an infrastructure failure, not a skipped step.
  **An independent hostile review of this memo is still owed** (cross-model or re-run of the deep subagent).
* **Author's structured self-review** (`data/z65/lift/REVIEW_INTERNAL.md`, clearly labelled as such) was done in its
  place: every step of G0–G4 and G_k re-derived; Prop O/E and Lemma S re-checked against the source texts; scripts
  re-run. Fixes applied:
  1. G_k needs p > k.
  2. Prop E's consequence now separates bad reduction of the marked cover (automatic) from bad reduction of the curve
     (Theorem G, p ≡ 1 (12)), with a consistency check on the Mordell covers.
  3. Prop O states p ∥ |G| explicitly.
  4. Corollary range p ≡ 1 (12) is now used consistently.
  5. The fpt equality wording is corrected.
  6. The verdict scope is stated: two branches as constructions, not all char-p arguments.
  7. The Lemma A dependence is made explicit in Theorem G.
