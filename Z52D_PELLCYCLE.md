# Z52D_PELLCYCLE — Pell / reduction-cycle data of √p as roots in the word forest (cluster C4 = A03)

ES is OPEN. Labels: PROVED / CONDITIONAL (on what) / CERTIFIED (computer) / EVIDENCE / CONJECTURE / Assessment.
All results are internally reviewed only. Brief: `z52bbriefs/depth_z52d.md`, lane PELLCYCLE. The cluster is rank_O C4
(`data/z52d/avenue/rank_O/RANKING_O.md` §C) = rank_A A03 (`rank_A/RANKING_A.md`). Its members are Z0596, Z0465, Z1298, Z0385,
Z1687, Z1048 and Z0378. The cited FRONTIER entry is §7.2 (Astra's open question) and §3 "Rooted constructions …
Does NOT rule out: … Pell or class-group cycle data".

## 0. Verdict in one paragraph

**C4 is dead as stated (principal-cycle data of √p used as forest roots), CONDITIONAL on Hypothesis H.** Under H there are
infinitely many primes p = m² + 1 ≡ 1 (mod 24) (m = 60t, five quadratics prime) at which every component of F_p meeting the
full principal-cycle data of √p and of (1+√p)/2 is monochromatic (Theorem 1.1). The data cover:
* all P_k, Q_k and partial quotients;
* all convergent numerators and denominators ≤ p + 2;
* the unit coordinates {t, u, t ± 2, u + 2} of ε_p.

**Unconditionally** (Prop 1.6), at every prime p = m² + 1 with 60 | m, all these roots except 1, 2, 4 are isolated vertices.
There the Pell cycle adds nothing to the fixed roots {1, 2, 4}. Note that (J)106's Dickson families never reach p = m² + 1;
freezing 1, 2, 4 there is exactly what Theorem 1.1 does under H.

The computation on the brief's families plus controls gives (CERTIFIED counts; rates are EVIDENCE):
* Per root, a cycle element is **statistically indistinguishable from a random vertex of the same size** at the
  0.1–0.4 pp level. The paired difference is −0.09 ± 0.08 pp over 356 primes. The pool is mostly controls; the 16 hard
  primes alone give no power.
* The Dickson family 2521 + 9240a is no harder than its class-matched controls.
* At long periods the cycle wins only by multiplicity: hundreds of roots at a ~2 % per-root rate.

Over all 1.44 M primes p ≡ 1 (8) < 10⁸, CR(R0) fails at 98 primes, at a rate that does not decay, including periods in the
thousands. CR(R3) fails at 6 primes, all of period ≤ 5. Size-matched random root sets fail about equally often (§3.4).

The only p-dependent survivor is the all-cycles (class-group) root set. It contains every a < √p with p a square mod a
(Prop 2.4) and never failed below 2·10⁷. That is FRONTIER §7.2's generic growing-root question, not a Pell mechanism.
Verdict: **dead** (CONDITIONAL on H), with the narrowing above. ES is open.

## 1. The near-square lemma (rank_O decisive test 1)

### 1.1 Definitions

* **Forest.** F_p has vertices {1, …, p + 2}, and u ≠ v are joined iff uv | p + u + v. Colour χ_p(v) = (v/p). For p ≡ 1 (4),
  a bichromatic edge is exactly a five-slice ES certificate (`LOWER_TAIL_ASTRA.md` Lemmas 2.1, 2.2; FRONTIER §3).
* **Cycle data (Def 1.1).** Run the continued-fraction algorithm on x₀ = (P₀ + √p)/Q₀ with Q₀ | p − P₀²:
  a_k = ⌊x_k⌋, P_{k+1} = a_kQ_k − P_k, Q_{k+1} = (p − P_{k+1}²)/Q_k. The run is pre-period plus one full period. Two
  expansions are used: **S** = √p, (P₀, Q₀) = (0, 1), and **W** = ω = (1 + √p)/2, (P₀, Q₀) = (1, 2). For p ≡ 1 (4) and P_k > 0,
  Q_k > 0, the convergents satisfy A_{k−1}² − pB_{k−1}² = (−1)^k Q_k (S case). So the Q_k are exactly the "CF norms"
  |P² − pQ²| of the member rows (Z0596 uses this notation, with P/Q denoting a convergent).
* **Full-cycle root sets (Def 1.2).** All sets are intersected with [1, p + 2], with 0 and p removed:
  * R0(p) = {P_k, Q_k of S}, the brief's "each P_k, Q_k of √p (whole cycle)";
  * R1 = R0 ∪ {a_k of S};
  * R2 = R1 ∪ {P_k, Q_k, a_k of W};
  * R3 = R2 ∪ {convergent numerators and denominators ≤ p + 2 of S and of W}. Convergents are monotone, so only finitely many
    are ≤ p + 2.
  * **Unit data.** U(p) = {t, u, t ± 2, u ± 2} ∩ [1, p + 2], where ε_p = (t + u√p)/2 is the fundamental unit (Z0465's
    recipe, recast as forest roots). At p = m² + 1, u − 2 = 0 is dropped. U is used only in §1; at long-period primes t and
    u exceed p + 2.
* **Cycle-root statement CR(R).** For every prime p ≡ 1 (mod 4), p > p₀, some component of F_p that meets R(p) contains a
  bichromatic edge. This is the missing theorem of Z0596 and Z1298, in forest form.
* **What is excluded.** The cycle-centre two-squares route ((J)3, p = a² + b² as a binary-form certificate) is not used.
  Cycle elements enter only as forest roots.

### 1.2 Lemmas

**Lemma 1.2 (neighbours; PROVED, elementary).** Let p be prime, 1 ≤ u, v ≤ p + 2, u ≠ v, p ∤ uv.
1. {u, v} is an edge ⟺ v | p + u and u | p + v. In that case gcd(u, v) = 1.
2. If v > u ≥ 2 is a neighbour of u, then w := (p + u)/v is an integer with w ≡ −1 (mod u). Hence w ≥ u − 1 and u² − 1 ≤ p + u.
3. If u ≥ 2 and u² − 1 > p + u, the only possible neighbour of u is r_u := (−p mod u). It is a neighbour iff r_u > 0 and
   r_u | p + u.
4. If v > u ≥ 2 is a neighbour and p ≡ c (mod u) with 1 ≤ c < u, then v = au − c and w = bu − 1 with integers a, b ≥ 1, and
   (au − c)(bu − 1) = p + u.

*Proof.*
1. (⇒) Both u and v divide uv, hence p + u + v, and so v | p + u and u | p + v. Any common divisor g of u and v divides
   p + u − u = p, and g ≤ p + 2 with p ∤ u, so g = 1. (⇐) u | p + u + v and v | p + u + v, with gcd(u, v) = 1 (same argument).
2. By 1, v | p + u and u | p + v, so v ≡ −p (mod u). Then vw = p + u ≡ p (mod u) gives −pw ≡ p (mod u). Since gcd(p, u) = 1,
   w ≡ −1 (mod u). As w ≥ 1, w ≥ u − 1. Then p + u = vw ≥ (u + 1)(u − 1).
3. By 2 there is no larger neighbour. A smaller neighbour r satisfies u | p + r, so r ≡ −p (mod u) and r = r_u. Conversely
   u | p + r_u always holds, and r_u | p + u is the remaining condition of 1. The gcd is automatic: gcd(r_u, u) = gcd(p, u) = 1.
4. v ≡ −p ≡ −c (mod u) and v + c > 0, so v = au − c with a ≥ 1. Also w ≡ −1 (mod u) and w ≥ 1, so w = bu − 1 with b ≥ 1. ∎

(1 and 3 are `LOWER_TAIL_ASTRA` Lemma 2.1 restated. 2 and 4 are the small bookkeeping used below.)

**Lemma 1.3 (every edge has a small endpoint; PROVED).** If {u, v} is an edge with u < v, then u(u − 1) ≤ p + 1, so
u < √p + 1.
*Proof.* uv ≤ p + u + v gives (u − 1)(v − 1) ≤ p + 1, and v − 1 ≥ u. ∎

**Lemma 1.4 (cycle data at p = m² + 1; PROVED).** Let m ≥ 4 be even, p = m² + 1 (not necessarily prime), k = m/2.
* (S) √p = [m; 2m, 2m, …]: rows (P, Q, a) = (0, 1, m), then the period (m, 1, 2m).
* (W) ω = (1 + √p)/2 has pre-period (1, 2, k) and period (m − 1, m, 1), (1, m, 1), (m − 1, 2, m − 1). So ω = [k; 1, 1, m − 1, …].
* For 4 | m and m ≥ 8:
  * R3(p) = {1, 2, k, k + 1, m − 1, m, m + 1, 2m − 1, 2m, 2m + 1, 4m};
  * ε_p = m + √p, i.e. (t, u) = (2m, 2), and U(p) = {2, 4, 2m − 2, 2m, 2m + 2}.

*Proof.* Throughout, m < √p < m + 1.

(S) a₀ = m. x₁ = 1/(√p − m) = (√p + m)/(p − m²) = √p + m, so (P, Q) = (m, 1) and a₁ = 2m. Then x₂ = 1/(√p − m) = x₁.

(W)
* a₀ = ⌊(1 + √p)/2⌋ = k, since k + ½ < ω < k + 1.
* x₁ = 2/(√p − (m − 1)) = 2(√p + m − 1)/(p − (m − 1)²) = (√p + m − 1)/m, because p − (m − 1)² = 2m. Since
  2m − 1 < √p + m − 1 < 2m, a₁ = 1.
* x₂ = 1/(x₁ − 1) = m/(√p − 1) = (√p + 1)/m, because p − 1 = m². Here m + 1 < √p + 1 < m + 2 and m ≥ 3, so a₂ = 1.
* x₃ = m/(√p − (m − 1)) = (√p + m − 1)/2. It lies in (m − ½, m), so a₃ = m − 1.
* x₄ = 2/(√p − (m − 1)) = x₁.

Convergents. S gives (A, B) = (m, 1), (2m² + 1, 2m), (4m³ + 3m, 4m² + 1), …; only m, 1 and 2m are ≤ p + 2 = m² + 3. W gives:
* numerators k, k + 1, m + 1, m² + k, …, so k, k + 1 and m + 1 are ≤ p + 2 (m² + k > m² + 3 for k ≥ 4);
* denominators 1, 1, 2, 2m − 1, 2m + 1, 4m, 4m² − 2m + 1, …, so 1, 2, 2m − 1, 2m + 1 and 4m are ≤ p + 2.

Collecting S and W gives R3. Unit: (m + √p)(m − √p) = −1, so ε = m + √p is a unit of norm −1. It is fundamental in
ℤ[(1 + √p)/2]. For a unit η = (a + b√p)/2 > 1 we have a, b > 0 and b√p = η ∓ η⁻¹, which increases with η, so a unit in
(1, ε) would have 1 ≤ b < 2, i.e. b = 1. That needs a² = p ± 4 = m² + 5 or m² − 3, and neither is a square for m ≥ 4,
because (m − 1)² < m² − 3 < m² < m² + 5 < (m + 1)². ∎

(CERTIFIED: `scripts/z52d_pellcycle_nearsquare.py` part (a) checks S, W and R3 ∪ U for every even m ∈ [4, 20000]; 0 mismatches.)

### 1.3 The theorem

**Theorem 1.1 (CONDITIONAL on Schinzel's Hypothesis H for five quadratics).** Let t ≥ 1, m = 60t, p = m² + 1, and suppose the
five numbers

f₀ = 3600t² + 1 = p, f₁ = 1800t² + 1 = (p + 1)/2, f₂ = 1200t² + 1 = (p + 2)/3, f₃ = 900t² + 1 = (p + 3)/4,
f₄ = 720t² + 1 = (p + 4)/5

are all prime. Then p ≡ 1 (mod 24), and **every component of F_p that meets R3(p) ∪ U(p) is monochromatic**. The
component of {1, 2} is the eight-vertex component of `LOWER_TAIL_ASTRA` Thm 3.1, with all vertices quadratic residues. Every
other element of R3 ∪ U is an isolated vertex. Hypothesis H applies: the f_i are irreducible (ct² + 1 with c > 0), have
positive leading coefficients, and ∏f_i(0) = 1, so the product has no fixed prime divisor. So H gives infinitely many such t,
and CR(R) fails for every R ⊆ R3 ∪ U. For R ⊆ R3 alone, f₄ is not needed: it is used only for the root 4 ∈ U.
Equivalently, CR(R3 ∪ U) implies that H fails for (f₀, …, f₄), and CR(R3) implies that it fails for (f₀, …, f₃).

*Proof.* Put k = m/2 = 30t and K = k + 1. All roots listed below are > 4 except 1, 2, 4. They are coprime to p, since they
are < p + 2 and ≠ p.

1. **Roots 1, 2.** p = 24k′ + 1 with k′ = 150t², and r = 12k′ + 1 = f₁, s = 8k′ + 1 = f₂, w = 6k′ + 1 = f₃ are prime. By
   `LOWER_TAIL_ASTRA` Thm 3.1, the component of 1 is {1, 2, 3, r, 2r, s, 3s, 2w}, all residues mod p. It contains the root 2.
2. **Root 4.** Any neighbour v of 4 satisfies v | p + 4 = 5f₄ and v ≡ −p ≡ 3 (mod 4) (Lemma 1.2.1). The divisors 1, 5, f₄
   and 5f₄ are all ≡ 1 (mod 4), since f₄ = 720t² + 1. So 4 is isolated.
3. **u = m** (p ≡ 1 mod m).
   * Parent r = m − 1. Since p + m = m² + m + 1 ≡ 3 (mod m − 1), r | p + m forces m − 1 | 3. False.
   * Children (Lemma 1.2.4 with c = 1): (am − 1)(bm − 1) = m² + m + 1, i.e. m(ab − 1) = a + b + 1. ab = 1 is impossible. If
     ab ≥ 2, then a + b ≤ ab + 1 gives m ≤ (ab + 2)/(ab − 1) ≤ 4. False.
4. **u = k** (p = 4k² + 1 ≡ 1 mod k).
   * Parent r = k − 1. Since p + k ≡ 6 (mod k − 1), it would need k − 1 | 6. False.
   * Children: (ak − 1)(bk − 1) = 4k² + k + 1 gives k(ab − 4) = a + b + 1. So ab ≥ 5 and k ≤ (ab + 2)/(ab − 4) ≤ 7. False.
5. **u = K = k + 1.** Here p = 4K² − 8K + 5 ≡ 5 (mod K) (K ≥ 31) and p + K = 4K² − 7K + 5.
   * Parent r = K − 5. Since p + K ≡ 70 (mod K − 5), it would need K − 5 | 70. K = 30t + 1 gives K − 5 ∈ {26, 56} for
     t = 1, 2, and K − 5 > 70 for t ≥ 3. Neither 26 nor 56 divides 70.
   * Children: (aK − 5)(bK − 1) = p + K gives K(ab − 4) = a + 5b − 7.
   * If ab ≤ 3, the left side is ≤ −31 while the right side is ≥ −1.
   * If ab = 4, then a + 5b ∈ {21, 12, 9}, never 7.
   * If ab ≥ 5, then 30(ab − 4) − (a + 5b − 7) ≥ 0. Check the three cases: b = 1, a ≥ 5 gives 29a − 118 > 0; a = 1, b ≥ 5
     gives 25b − 114 > 0; and a, b ≥ 2 with ab ≥ 6 uses a + 5b ≤ 3ab to give ≥ 27ab − 113 > 0. So K ≤ 30. False.
6. **u = U := m − 1.** Here p ≡ 2 (mod U) and p + U = U² + 3U + 2.
   * Parent r = U − 2 would need U − 2 | 12. False, since U ≥ 59.
   * Children: (aU − 2)(bU − 1) = p + U gives U(ab − 1) = a + 2b + 3. ab = 1 gives 0 = 6. If ab ≥ 2, then
     a + 2b + 3 ≤ 8(ab − 1) gives U ≤ 8. Check: b = 1 gives 7a − 13 > 0; a = 1 gives 6b − 12 ≥ 0; a, b ≥ 2 gives
     6.5ab − 11 > 0. False.
7. **Large roots u ≥ m + 1:** m + 1, 2m − 2, 2m − 1, 2m, 2m + 1, 2m + 2, 4m. Here u² − u ≥ (m + 1)m > m² + 2 = p + 1, so
   Lemma 1.2.3 applies and only r_u needs checking. For each root the residue of p, the parent, and the congruence that
   r_u | p + u would force are:

   | u | p mod u | r_u | r_u ∣ p + u would force |
   |---|---|---|---|
   | m + 1 | 2 | m − 1 | p + u = m² + m + 2 ≡ 4, so m − 1 \| 4 |
   | 2m | 1 (m even) | 2m − 1 | p + u = (m + 1)², 4(m + 1)² = (2m + 2)² ≡ 9, gcd(2m − 1, 4) = 1, so 2m − 1 \| 9 |
   | 4m | 1 (4 \| m) | 4m − 1 | 16(p + u) = (4m)² + 16·4m + 16 ≡ 33, so 4m − 1 \| 33 |
   | 2m − 1 = 4k − 1 | k + 1 | 3k − 2 | 9(p + u) = 4(3k)² + 12(3k) ≡ 40, gcd(3k − 2, 9) = 1, so 3k − 2 \| 40 |
   | 2m + 1 = 4k + 1 | 3k + 2 | k − 1 | p + u = 4k² + 4k + 2 ≡ 10, so k − 1 \| 10 |
   | 2m + 2 = 4k + 2 | 2k + 3 | 2k − 1 | p + u = 4k² + 4k + 3 ≡ 1 + 2 + 3 = 6, so 2k − 1 \| 6 |
   | 2m − 2 = 4k − 2 | 2k + 1 | 2k − 3 | p + u = 4k² + 4k − 1 ≡ 9 + 6 − 1 = 14, so 2k − 3 \| 14 |

   (Residues: 4k² + 1 = k(4k − 1) + k + 1 = k(4k + 1) − k + 1 = k(4k + 2) − 2k + 1 = k(4k − 2) + 2k + 1.) With m ≥ 60 and
   k ≥ 30, every forced divisibility is false.

Hence every element of R3 ∪ U other than 1, 2, 4 is an isolated vertex. Components meeting R3 ∪ U are therefore comp(1),
{4} and singletons, and all are monochromatic. ∎

**Proposition 1.6 (unconditional part; PROVED).** For every prime p = m² + 1 with 60 | m, the elements of R3(p) ∪ U(p) other
than 1, 2, 4 are isolated vertices of F_p. So at each such prime, some component meeting R3 ∪ U is bichromatic iff some
component meeting {1, 2, 4} is: the cycle contributes nothing beyond these fixed roots. (Only 60 | m is proved. For 12 | m
the statement fails at p = 1297 = 36² + 1, where the root k + 1 = 19 has the edge {14, 19}, which happens to be
monochromatic. The §1.3 census found no large-root hit for 12 | m ≤ 120000.)
*Proof.* Steps 3–7 above use only that p = m² + 1 is prime and 60 | m: primality gives gcd(u, p) = 1 in Lemma 1.2, and
60 | m gives m ≥ 60, 4 | m, k = 30t and K = 30t + 1. ∎

**CERTIFIED checks** (`scripts/z52d_pellcycle_nearsquare.py 20000 6`, output `data/z52d/pellcycle/nearsquare_check.txt`):
* (b) For all 333 values m ≡ 0 (60), m ≤ 20000, and all 11 roots u ∉ {1, 2, 4} (3,663 pairs), the vertex u is isolated in
  F_{m²+1}. Primality of m² + 1 is not needed for the isolation, since gcd(u, m² + 1) = 1 was checked.
* (c) The first six H-instances are t = 13 900, 63 863, 73 808, 154 086, 161 504, 168 149, i.e.
  p = 695 556 000 001, 14 682 537 968 401, 19 611 435 110 401, 85 472 983 425 601, 93 900 751 257 601, 101 786 710 323 601.
  At each, brute force confirms:
  * every R3 ∪ U component is monochromatic;
  * comp(1) is exactly the Thm 3.1 set;
  * F_p has bichromatic edges elsewhere, e.g. {7, 34} at p = 19 611 435 110 401. ES is not contradicted.

**Unconditional examples** (CERTIFIED; `scripts/z52d_pellcycle_nsrate.py 120000`, `data/z52d/pellcycle/nearsquare_rate.txt`).
There are 1,330 primes p = m² + 1 with 12 | m ≤ 120 000. At 8 of them every component meeting R3 ∪ U is monochromatic:
1 299 601, 33 177 601, 476 985 601, 973 440 001, 2 134 440 001, 2 813 241 601, 4 292 870 401, 11 833 088 401. At all 1,330
primes, a large cycle root never lies in a bichromatic component; the outcome is decided by the components of 1, 2, 4.

### 1.4 Remarks on scope

* **p = m² + 4 is not a hard family.** m must be odd, so p ≡ 5 (mod 8) and (2/p) = −1. The root Q₀ = 1 of every cycle has
  the edge {1, 2} (2 | p + 3), which is bichromatic. So CR(R0) holds trivially at all such p, and rank_O's "m² + 1 or m² + 4"
  should read "m² + 1".
* **Other hard near-square shapes.** Consider short-period (Richaud–Degert-type) primes p = m² + r with r | 4m, −m < r ≤ m,
  and p ≡ 1 (24). Then m is even, r is odd with r | m, 3 | m, and r ≡ 1 (24) if 4 | m, r ≡ 13 (24) if m ≡ 2 (4) (elementary,
  from p mod 3 and 8). Theorem 1.1 handles r = 1. Other r (13, −11, 25, …) should yield to the same casework, but this is
  not done here.
* **Why the lemma kills the route.** For p = m² + 1 the cycle is a fixed polynomial recipe in m, as rank_O predicted. So it is
  a (J)106-type frozen root set on a thin family that H populates. This is not covered by B1 Thm C, whose scope is
  procedures run on an arbitrary p in a congruence class; here the family is quadratic.

## 2. What the cycle is, and why it either is tiny or is everything

**Lemma 2.1 (CF norms are residues; PROVED, = (J)84 Prop 4.2 in forest language).** For p ≡ 1 (8), every Q_k of S and of W
has χ_p(Q_k) = +1.
*Proof.* Q_kQ_{k−1} = p − P_k², and gcd(P_k, Q_k) = 1: a common factor g gives g | p, while P_k < √p. So p ≡ P_k² (mod Q_k),
hence (p/q) = 1 for every odd prime q | Q_k. Since p ≡ 1 (mod 8), Jacobi reciprocity and (2/p) = 1 give
(Q_k/p) = (Q_k,odd/p) = (p/Q_k,odd) = 1. ∎
So the Q-half of R0 is monochromatic +1, and a hit needs a non-residue elsewhere in the component.

**Prop 2.4 (all cycles; (a), (b) PROVED).**
* (a) The reduced irrationals x = (P + √p)/Q with Q | p − P², Q > 0, x > 1, −1 < x̄ < 0 fall into finitely many purely
  periodic CF cycles. The S cycle and the W cycle are two of them; call their number c(p).
* (b) Every a with 1 ≤ a < √p for which x² ≡ p (mod a) is solvable is the Q of some reduced irrational, so it lies in the
  union of all cycles.
* (c) If c(p) = 2, then S(p) := {a < √p : p □ mod a} ⊆ R2(p).

*Proof of (b).* Let x₀² ≡ p (mod a). The interval (√p − a, √p) has length a and irrational endpoints, so it contains exactly
a consecutive integers and hence some b ≡ x₀ (mod a). Then 0 < b < √p, a | p − b², and x = (b + √p)/a satisfies x > 1 (as
b + √p > a) and x̄ = (b − √p)/a ∈ (−1, 0). (a) is standard: x ↦ 1/(x − ⌊x⌋) permutes the finite set of reduced irrationals.
(c) follows from (b). ∎

(c(p) is presumably the number of wide classes of forms of discriminant 4p plus that of discriminant p. This is not proved
here and not used: below, "c(p) = 2" means only that S and W are all the cycles, and the "class number one" reading is an
interpretation.) EVIDENCE (`scripts/z52d_pellcycle_cycles.py`, `data/z52d/pellcycle/cycles_table.md`):

| p | c(p) | period S / W | \|S(p)\| | share of S(p) in R0 | in R2 |
|---:|---:|---|---:|---:|---:|
| (★)-zeros ≤ 10⁶ except 577 (409, 5569, …, 712321), plus 2521, 3361 | 2 | 21/27 … 1867/1865 | 15 … 521 | 0.53–0.63 | 1.000 |
| 577 = 24² + 1 | 14 | 1/3 | 16 | 0.062 | 0.188 |
| 1297 = 36² + 1 | 22 | 1/3 | 22 | 0.045 | 0.136 |
| 1 299 601 = 1140² + 1 | 714 | 1/3 | 654 | 0.002 | 0.005 |

**Reading (Assessment).** The principal cycle interpolates between two extremes, and neither helps:
* When c(p) = 2 (all reduced irrationals lie in S or W), R2 already contains every a < √p with p a square mod a. By Lemma 1.3 every edge has its
  smaller endpoint below √p + 1, so "a cycle root has a bichromatic component" is then nearly a restatement of ES₅ restricted
  to split small endpoints.
* At near-squares (large class number, regulator ≍ log p), the cycle is a bounded polynomial recipe, and Theorem 1.1 kills
  it under H.

Nothing about the CF dynamics was used in either case. The cycle enters only as a set of integers of size ≤ 2√p.

## 3. The falsifier computation (rank_A + rank_O decisive test 2)

### 3.1 Setup

* **Library.** `scripts/z52d_pellcycle_lib.py`.
  * `root_sets` implements Def 1.2.
  * `explore(p, u, depth, cap)` does BFS in F_p: parent via Lemma 1.2.3, children among divisors of p + u, and only for
    u² − 1 ≤ p + u (Lemma 1.2.2). It stops at the first bichromatic edge (**hit**), when the component is exhausted
    (**mono**), or at `cap` = 10⁵ vertices (**censored**).
  * Depth-2 means a bichromatic edge on a path of length ≤ 2 from the root.
* **Finite bound for the enumeration (rank_A's request; PROVED).**
  * A component is enumerated exactly, by factoring p + u only at its vertices with u² − u ≤ p + 1 (Lemma 1.2.2). All other
    vertices are leaves with a known parent.
  * Depth is O(log p) (`LOWER_TAIL_ASTRA` Lemma 4.1, Fibonacci growth along increasing paths).
  * Edges have smaller endpoint < √p + 1 (Lemma 1.3), and there are no big-integer vertices, since vertices are ≤ p + 2.
  * Convergents > p + 2 are not vertices; R3 drops them by definition.
* **Census.** `scripts/z52d_pellcycle_census.py OUT 60 3 5 [shard nshard]`, 12 shards, merged to
  `data/z52d/pellcycle/census.jsonl`; tables from `scripts/z52d_pellcycle_analyze.py` in
  `data/z52d/pellcycle/census_tables.md`. Families:
  * **Z:** the 14 (★)-zeros ≤ 10¹⁰ (409 … 8 813 281).
  * **N:** 2521, 3361.
  * **D:** the first 59 primes p = 2521 + 9240a > 2521 with (p + 11)/12 prime (30 241 … 6 368 881), the family of
    `LOWER_TAIL_ASTRA` Thm 5.1.
  * **C24:** 221 size-matched controls: for each Z/N/D prime, up to three random primes ≡ 1 (24) within ±10 % (seeded, not
    reused). The search finds fewer than three near the smallest test primes, giving 221 rather than 225.
  * **CD:** 60 Dickson-class controls: p ≡ 2521 (9240) with (p + 11)/12 composite, nearest to each D prime.
  * **H:** the six H-instances of §1.3.
* **Baselines (per root u ≥ 8;** roots < 8 are fixed roots and are reported separately).
  * K = 5 draws per root, uniform from [⌈0.8u⌉, ⌊1.25u⌋] ("size").
  * The same, conditioned on χ_p(draw) = χ_p(u) ("size+colour"). This baseline matters because the Q-roots are all residues
    (Lemma 2.1).
  * The random root set replaces every root ≥ 8 by its draw.

### 3.2 Results (CERTIFIED counts; rates are EVIDENCE)

Root set R0, the brief's "each P_k, Q_k of √p":

| family | #p | mean \|R0\| | primes with a hit, depth 2 | primes with a hit, full component | censored | per-root hit rate, full: cycle / size / size+colour | depth 2: cycle / size / size+colour |
|---|---:|---:|---:|---:|---:|---|---|
| Z ∪ N | 16 | 572 | 15/16 | 16/16 | 0 | 1.61 / 1.52 / 1.54 % | 1.20 / 1.29 / 1.22 % |
| D | 59 | 909 | 58/59 | 59/59 | 0 | 1.66 / 1.71 / 1.48 % | 1.54 / 1.62 / 1.36 % |
| C24 | 221 | 759 | 221/221 | 221/221 | 0 | 2.19 / 2.29 / 2.06 % | 1.99 / 2.15 / 1.86 % |
| CD | 60 | 952 | 59/60 | 60/60 | 0 | 1.76 / 1.80 / 1.53 % | 1.61 / 1.72 / 1.41 % |
| H | 6 | 2 | 0/6 | **0/6** | 0 | — | — |

R3 behaves the same way: per-root rates are cycle / size / size+colour 1.73/1.73/1.70 % (Z∪N), 2.04/2.08/1.94 % (D),
2.78/2.88/2.77 % (C24) and 2.11/2.22/2.01 % (CD); H gives 0/6.

The paired per-prime difference "cycle rate − baseline rate", mean ± s.e. over the 356 non-H primes, is:

| root set | vs size, full | vs size+colour, full | vs size, depth 2 | vs size+colour, depth 2 |
|---|---:|---:|---:|---:|
| R0 | −0.09 ± 0.08 pp | +0.22 ± 0.07 pp | −0.17 ± 0.07 pp | +0.23 ± 0.06 pp |
| R3 | −0.12 ± 0.06 pp | +0.03 ± 0.06 pp | −0.18 ± 0.06 pp | +0.04 ± 0.06 pp |

* **Per element, cycle roots are statistically indistinguishable from random roots at the ≈ 0.1–0.4 pp level** (base rate
  1.5–3 %). Effects at ≥ 2σ are:
  * R0 vs size+colour: +0.22 ± 0.07 pp, and +0.37 ± 0.12 pp within D. This is plausibly the Q-roots being split integers
    rather than mere residues.
  * R0 vs size at depth 2: −0.17 ± 0.07 pp.
  * R3 vs size: −0.12 ± 0.06 pp (full) and −0.18 ± 0.06 pp (depth 2).
  * R3 vs size+colour: +0.20 ± 0.06 pp in D and +0.16 ± 0.06 pp in CD.

  The signs go both ways and the sizes are ≤ 0.4 pp, i.e. ≤ 20 % relative. None of this is a mechanism. **Power caveat:** on
  the hard primes themselves (Z ∪ N, 16 primes) the paired s.e. is ≈ 1 pp on a 1.6 % base, so the test there has
  essentially no power. The pooled statement rests mostly on the 59 D primes and 281 controls.
* **The Dickson family is not special for the cycle.**
  * D has the same per-root rate as its class-matched controls CD: 1.66 vs 1.76 % (R0).
  * Both are lower than C24 (2.19 %). D and CD share p ≡ 2521 (mod 9240), i.e. p ≡ 1 (mod 840) and p ≡ 2 (mod 11), and this
    class, not the Dickson factor (p + 11)/12 or the cycle, is the likely source of the depression (Assessment; not
    separated by a p ≡ 1 (840)-only control).
  * Thm 5.1's mechanism (ℓ(p) = 11 isolated) is invisible to the cycle, which hits at every D prime.
* **Per prime, the cycle wins at long periods only by multiplicity.** All 356 non-H primes have a full-component hit with R0.
  A random root set of the same sizes also hits, with P = 0.990–1.000. This P is inflated because the random sets keep the
  cycle's roots < 8.
  * At the (★)-zeros the R0 hits are few: e.g. 7 of 243 roots at 83 449, 10 of 1118 at 1 726 201, 9 of 1047 at 1 724 209.
  * At 83 449, 1 726 201 and 5 212 561 no root < 8 is in a bichromatic component, so the hit comes from large cycle roots.
    The size-matched random large roots also hit at all three, in 5 of 5 draws each, with 38/1195, 54/5570 and 72/9155
    root-level hits.
* **Censoring:** 0 censored roots at cap 10⁵. Components are tiny: F_p has few edges, 77 per prime on average for p ≤ 10⁶
  (`LOWER_TAIL_ASTRA` §6).

### 3.3 The 577 case

577 = 24² + 1 is a (★)-zero and a near-square: R3 = {1, 2, 12, 13, 23, 24, 25, 47, 48, 49, 96}. Every root ≥ 12 is isolated.
The only R3 hit is through the component of 1, which contains the edge {3, 29} with (29/577) = −1. Here p + 1 = 2·17² is not
of the Thm 3.1 shape. With U added, the root 4 also hits ({4, 83}). So 577 is saved by the fixed roots 1 and 4, as
Prop 1.6's mechanism predicts (24 is not divisible by 60, but the large roots are isolated here as well).

### 3.4 Complete failure census of CR(R0), CR(R3)

`scripts/z52d_pellcycle_failcensus.py`, all primes p ≡ 1 (8) < 10⁸, in chunks of 4·10⁶, with output in
`data/z52d/pellcycle/fail/`. Primes p ≡ 5 (8) succeed automatically, by the edge {1, 2} from the root Q₀ = 1.

**Cycle failures (CERTIFIED).** Over 1,439,970 primes p ≡ 1 (8) < 10⁸, with 0 censored roots:
* **CR(R0) fails at 98 primes.** Per 2·10⁷ window the counts are 34, 16, 14, 19, 15, so the rate does not visibly decay
  beyond 2·10⁷.
  * The first are 19 441, 63 361, 93 601, 429 529, 539 401, 696 361, 928 561, 1 202 041, 1 299 601, ….
  * R0 failures are **not** confined to short periods: 1 847 401 (period 199, |R0| = 186), 28 845 721 (1357, 1039) and
    32 676 361 (2929, 2051) all fail. The median of period/√p over the failures is 0.028; the maximum is 0.51.
* **CR(R3) fails at 6 primes:**

  | p | period of √p | shape |
  |---|---:|---|
  | 429 529 | 5 | short period |
  | 1 299 601 | 1 | 1140² + 1 |
  | 11 516 521 | 5 | short period |
  | 33 177 601 | 1 | 5760² + 1 |
  | 76 737 601 | 1 | 8760² + 1 |
  | 84 272 401 | 1 | 9180² + 1 |

  All four near-squares have 60 | m, as in Theorem 1.1. They were re-verified with the corrected convergent routine (see
  below). At 76 737 601 and 84 272 401 the unit root 4 ∈ U rescues, so they are not in the R3 ∪ U list of §1.3.

**Random control (CERTIFIED counts).** `scripts/z52d_pellcycle_randfail.py` builds, at every prime, the same census for the
random root set that keeps roots < 8 and replaces each root u ≥ 8 by one uniform draw from [⌈0.8u⌉, ⌊1.25u⌋]. Data are in
`data/z52d/pellcycle/randfail/`. Over p ≡ 1 (8) < 4·10⁷:

| range | primes | cycle R0 fails | random-R0 fails | cycle R3 fails | random-R3 fails |
|---|---:|---:|---:|---:|---:|
| [0, 4)·10⁶ | 70,695 | 17 | 11 | 2 | 2 |
| [4, 8)·10⁶ | 64,043 | 5 | 4 | 0 | 1 |
| [8, 12)·10⁶ | 62,146 | 3 | 3 | 1 | 1 |
| [12, 16)·10⁶ | 60,649 | 5 | 5 | 0 | 0 |
| [16, 20)·10⁶ | 59,944 | 4 | 3 | 0 | 0 |
| [20, 24)·10⁶ | 59,036 | 3 | 3 | 0 | 0 |
| [24, 28)·10⁶ | 58,614 | 2 | 4 | 0 | 0 |
| [28, 32)·10⁶ | 58,132 | 5 | 1 | 0 | 0 |
| [32, 36)·10⁶ | 57,477 | 5 | 3 | 1 | 1 |
| [36, 40)·10⁶ | 57,364 | 1 | 2 | 0 | 0 |
| **total < 4·10⁷** | 608,100 | **50** | **39** | **4** | **5** |

The cycle fails about as often as a random set of the same sizes: 50 vs 39 for R0, a difference of about 1.2σ treating both
as Poisson, and 4 vs 5 for R3. It is not more robust, which is the point at issue.

**Selection caveat and class bias (EVIDENCE).**
* At the R0-failing primes themselves, a fresh random set fails less often. The 100-draw failure counts
  (`scripts/z52d_pellcycle_failrand.py`, `data/z52d/pellcycle/failrand_table.md`) range from 0/100 at 28 237 801,
  28 845 721 and 32 676 361 to 40/100 at 3 819 481. These primes were selected for cycle failure, so that comparison is
  biased.
* Those long-period failures have many cycles: c(p) = 18, 22, 18, 10 at 1 847 401, 28 237 801, 28 845 721, 32 676 361. The
  √p cycle covers only 13–25 % of S(p).
* To test whether cycle membership is anti-correlated with lying in a bichromatic component,
  `scripts/z52d_pellcycle_classbias.py 10⁶ 10⁷ 400 11` (`data/z52d/pellcycle/classbias.txt`) uses 400 random primes
  p ≡ 1 (8) in [10⁶, 10⁷].
  * Of the 9,948 split vertices ≤ √p in bichromatic components, 5,519 are √p-cycle Q-values against 5,275.5 expected from
    the per-prime coverage, a ratio of 1.046.
  * For split vertices in monochromatic non-trivial components the ratio is 0.946.
  * So there is no anti-correlation. There is a weak positive association of ≈ 5 % relative, matching the +0.2 pp of §3.2.
    It is far from a mechanism.

**Implementation note (review fix).** The first version of `root_sets` generated convergents over pre-period + two periods
only. This misses convergents ≤ p + 2 at p = 5; the reviewer found no other p < 4·10⁵ affected. The routine now runs until
A_k, B_k > p + 2. The census (§3.2) was rerun with the fixed code and is bit-identical. The 6 R3 failures above were
rechecked with it; the failure census itself ran with the old routine, which can only miss roots, so R3 failures can only
be over-counted, and all 6 survive the recheck.

### 3.5 The all-cycles (class-group) root set

`scripts/z52d_pellcycle_allcycles.py 1 20000000` (`data/z52d/pellcycle/allcycles_2e7.txt`) roots at every a ∈ S(p), which
by Prop 2.4(b) lies in the union of all cycles. Over the 317,477 primes p ≡ 1 (8) < 2·10⁷ there are 0 failures, and at most
28 elements of S(p), in increasing order, are tried before the first hit (p = 19 231 801). This is EVIDENCE that the
all-classes version behaves like the HC(p)-type small-root statement of FRONTIER §7.2: it is a growing root set,
p-dependent through "p □ mod a", and not a Pell/CF mechanism.

## 4. Verdict for the cluster

**Dead (CONDITIONAL on H) for the C4 missing theorem as posed, i.e. principal-cycle data used as forest roots.** The
computation (EVIDENCE) finds no forest information in the cycle beyond size, colour and multiplicity, at the ≤ 0.4 pp level.
What survives is no longer C4.

* **Z0596, Z1298** ("some element of the principal reduction cycle yields a bichromatic edge, for every p > p₀"): false i.o.
  under H, for every root set R ⊆ R3 ∪ U (Thm 1.1). Unconditionally, it fails at the explicit primes of §1.3 and §3.4, but
  those are finitely many and so do not refute the "p > p₀" form without H.
  * Z0596's alternative "an ambiguous form in the cycle" is covered as a root: ambiguous rows are cycle rows, and their
    P, Q lie in R0. It is not covered as a two-squares certificate, which is the dead (J)3 route and is excluded.
  * Z1298's variant "the automorphism orbit of a slice's indefinite binary form" concerns a different form, not the √p
    cycle, and is not treated here.
* **Z0465** (unit recipe Φ(t, u)): covered only in rank_O's forest-root recasting, where U ⊆ R3 ∪ U in Thm 1.1.
  * Z0465's own missing theorem uses Φ(t, u) as an e-slice parameter (e ≡ −p mod 4) or as a divisor class of 4Cp + 1. At
    p = m² + 1 with 60 | m, all of {2m, 2, 2m ± 2, 4} are even. So that recipe is vacuous there (no e ≡ 3 (4) arises) rather
    than refuted by Thm 1.1.
  * Assessment: other fixed recipes in the cycle data at p = m² + 1 (m², m ± 2, 3m, …) are fixed polynomial menus in m and
    presumably fall to the same casework, but only the 14 listed roots are proved.
* **Z0385** (Legendre-type descent): Assessment. Thm 1.1 shows the forced object at near-squares is (1, m, 2m) plus the
  ω-cycle. Its "factorisation" is p + 1 = 2f₁, p + 2 = 3f₂, …. These are exactly the Dickson-frozen shifts. No descent
  closes there.
* **Z1687, Z1048, Z0378:** unchanged (already known-false / B2 in the avenue rows).
* **Narrowed survivor.** p-dependent root sets of growing size that are not a fixed recipe in the near-square parameter. The
  only cycle-flavoured one is the all-classes set ⊇ S(p) (Prop 2.4). It never failed below 2·10⁷, but it is the HC-type
  question of §7.2 restricted to split roots, and Pell structure plays no role in it.

## 5. Proposed FRONTIER changes (do not edit FRONTIER here)

* **§3 "Rooted constructions …", "Does NOT rule out".** Replace "growing/p-dependent roots, Pell or class-group cycle data" with:
  "growing p-dependent roots. *Principal-cycle (Pell) data used as forest roots is ruled out under Hypothesis H* (CF/Pell
  data used as other coordinates, e.g. e-slice windows or divisor classes, is a separate question): at infinitely many near-square
  primes p = m² + 1 (m = 60t, five quadratics prime) every component meeting the full principal cycles of √p and (1+√p)/2 —
  all P_k, Q_k, a_k, all convergents ≤ p + 2, and the unit coordinates — is monochromatic (`Z52D_PELLCYCLE.md` Thm 1.1); and
  unconditionally at every prime m² + 1 with 60 | m the cycle roots other than 1, 2, 4 are isolated (Prop 1.6). The union of
  *all* reduction cycles contains every a < √p with p □ mod a (Prop 2.4) and is a generic growing root set, not excluded."
* **§7.2, sentence "Open: can p-dependent roots, or full reduction-cycle / Pell / class-group data, force a bichromatic
  edge".** Replace with: "Open: can p-dependent growing root sets force a bichromatic edge? (Principal reduction-cycle / Pell
  data used as roots cannot, under H: `Z52D_PELLCYCLE.md` Thm 1.1; per root they are statistically indistinguishable from
  random vertices of the same size at the ±0.1–0.4 pp level, EVIDENCE pooled mostly over controls, §3.2.)"
* **§6 dead ends, one line.** "Pell / reduction-cycle roots in F_p → near-square primes m² + 1 freeze the cycle to a polynomial
  recipe; dead under H → Z52D_PELLCYCLE."

## 6. Bottom line

The C4 question was whether the reduction cycle of √p, a canonical object that exists at every prime, could be the
p-dependent root source that (J)106 leaves open. It cannot:
* **At near-square primes** p = m² + 1 the cycle is a fixed polynomial recipe in m. When 60 | m, every cycle root ≥ 5 is
  provably isolated (Prop 1.6). Under Hypothesis H the remaining roots 1, 2, 4 can be frozen into a monochromatic component simultaneously. So
  infinitely many hard primes (≡ 1 mod 24) defeat every principal-cycle root (Thm 1.1).
* **At long-period primes** each cycle element is statistically indistinguishable from a random vertex of the same size
  (paired difference −0.09 ± 0.08 pp over 356 primes, mostly controls; the 16 hard primes alone have no power). The cycle
  succeeds there only because it contains hundreds of candidates. When S and W are the only cycles, it already contains
  every split a < √p.
* **The Dickson family** 2521 + 9240a is neither helped nor hurt beyond its residue class.

So the cycle is a size/multiplicity device, not an arithmetic mechanism. The only p-dependent survivor (all classes) is
FRONTIER §7.2's generic growing-root question. ES remains open.

## 7. Reproduction

```
ulimit -v 4000000
timeout 900  uv run --with sympy python scripts/z52d_pellcycle_nearsquare.py 20000 6     # Lemma 1.4, Prop 1.6, Thm 1.1 instances
timeout 1800 uv run --with sympy python scripts/z52d_pellcycle_nsrate.py 120000 data/z52d/pellcycle/nearsquare_rate.txt
for i in $(seq 0 11); do timeout 7200 uv run --with sympy python scripts/z52d_pellcycle_census.py \
   /tmp/pcshards/census_$i.jsonl 60 3 5 $i 12 & done; wait   # then cat shards > data/z52d/pellcycle/census.jsonl
timeout 60   uv run python scripts/z52d_pellcycle_analyze.py data/z52d/pellcycle/census.jsonl
timeout 900  uv run --with sympy python scripts/z52d_pellcycle_cycles.py 409 577 1297 2521 3361 5569 9601 23929 83449 102001 329617 712321 1299601
timeout 3600 uv run --with sympy python scripts/z52d_pellcycle_failcensus.py LO HI 0 1 OUT        # chunks of 4e6 up to 1e8
timeout 3000 uv run --with sympy python scripts/z52d_pellcycle_allcycles.py 1 20000000
timeout 5400 uv run --with sympy python scripts/z52d_pellcycle_randfail.py LO HI OUT          # chunks of 4e6 up to 4e7
timeout 1800 uv run --with sympy python scripts/z52d_pellcycle_failrand.py 100 19441 93601 1847401 3819481 13503121 17358961 26120161 28237801 28845721 32676361 36647041
timeout 1800 uv run --with sympy python scripts/z52d_pellcycle_classbias.py 1000000 10000000 400 11
```
(Run from `scripts/` or with `PYTHONPATH=scripts`; scripts import `z52d_pellcycle_lib`.)

## 8. Review

Round 1: a hostile reviewer subagent rechecked every proof step by hand and recomputed key numbers with independent code. It
found no fatal problems. Theorem 1.1, Prop 1.6, Lemmas 1.2–1.4, 2.1 and Prop 2.4 were confirmed; the six H-instances,
1 299 601, 577, the c(p) table and four census rows were recomputed and match. It raised five major and thirteen minor
points, and all have been fixed:
* §0 wrongly said R0 fails only at short periods. It does not, and §3.4 now gives the full census with a random control.
* "every cycle root ≥ 5 is isolated" needs 60 | m, as the counterexample at p = 1297 shows. This is now stated.
* The Z0465 coverage was overclaimed. It is now scoped to forest roots, with the original e-slice recipe noted as vacuous at
  m = 60t.
* The FRONTIER text is scoped to "used as forest roots".
* §3.2 statistics were restated accurately, with the ≥ 2σ effects listed and the power caveat on the hard primes added.
* Minor fixes:
  * the bound u² − u ≤ p + 1;
  * the C24 count;
  * the §2 table label;
  * U = u ± 2;
  * the convergent routine (affects p = 5 only; the census was rerun bit-identically);
  * Prop 1.6 restated per prime, plus the "CR ⇒ ¬H" form;
  * the (J)106/Dickson remark;
  * the Dickson-depression attribution is now an Assessment;
  * the unit proof expanded;
  * f₄ is needed only for the root 4;
  * the c(p)/class-number reading labelled as interpretation;
  * the inflated P(any hit) noted;
  * the 577 root 4;
  * the ambiguous-form / slice-form scope in §4.

REVIEW_ROUND2
