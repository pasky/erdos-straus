# Z53_FORESTCLASS — class-group roots in the word forest F_p (FRONTIER §7.2)

ES is OPEN. Nothing here proves or disproves ES, ES₅ or any all-prime statement. Labels: PROVED / CONDITIONAL (on what) /
CERTIFIED (computer) / EVIDENCE / CONJECTURE / Assessment. All results are internally reviewed only (§9).
Brief: `z52bbriefs/z53_depth.md`, lane FORESTCLASS (`z52bbriefs/z53_lanes.md`). Scripts `scripts/z53_forestclass_*`,
data `data/z53/forestclass/` (2.3 MB).

## 0. Verdict in one paragraph

**Narrowed.** Class-group data of discriminants ±4p (in the precise congruence-filter form of §1), used as roots of the
forest F_p, splits into the parts below. No mechanism beyond the genus layer was found in any of them; that is a finding,
not an impossibility theorem.
* **Bounded class-group menus die (Theorem 1, CONDITIONAL on Dickson).** For all H ≥ 3, K ≥ 1, infinitely many primes
  p ≡ 1 (24) have every component meeting {1, …, H} ∪ {the K least quadratic non-residues} monochromatic. The family makes
  ℓ(p) = q a prime ≡ 3 (4). So the menu contains: the two genus minima and the ambiguous-form minima of Cl(−4p); the
  first K′ elements, in increasing order, of SM, of SMN and of SP (the first distinct Q-values of the ordered union of all
  cycles); and the first powers 5, 25, … of the class of a prime ideal above 5. These are the covered menus (Cor 1.1).
  Arbitrary bounded functions of class-group data, other p-dependent split classes, and prefixes of each individual
  real cycle are not covered. This extends LOWER_TAIL_ASTRA Thms 3.2 + 5.1 from one non-residue root to K non-residue
  roots plus H fixed roots at once. It does not subsume LOWERTAIL_ROUND2_FABLE Prop 3.3 (level coordinates, many
  words). Verified instances exist, including ones at which every Dickson form is prime.
* **The full set of reduced-form minima of −4p is not freezable, and the root sets are congruence filters (Prop 2,
  PROVED rel. Siegel).** The reduced forms of −4p have ≥ h(−4p)p^{−o(1)} = p^{1/2−o(1)} distinct minima, so no fixed
  finite list of polynomial-valued roots enumerates them along a polynomial family (an E1/E2-type escape from B1). But
  membership of a fixed a in SM, SP, SMN is a function of p mod 8a. A growing class-group root statement is therefore a
  growing-window statement on a congruence filter (Assessment: of the HC/window type of §7.2, though not equivalent to
  HC, which also uses level coordinates).
* **Lemma G (PROVED): class-group roots carry no genus obstruction.** A vertex a has a neighbour only if the genus class
  of −p mod a lies in the span of the genus classes of the prime factors of p + a. For a ∈ SM (−p a square mod a) this
  never obstructs: the target coset gets at least its fair share τ(p+a)/[G:G²] of divisors. (The converse fails: non-SM
  vertices are often unobstructed too.) Genus counts at all vertices of 4 800 random primes at 10⁹–10¹² show (EVIDENCE):
  * 37 % of non-SM vertices are genus-obstructed, against 0 % of SM vertices;
  * SM raises the chance of being non-isolated by ×1.14–1.35, and of lying in a bichromatic component by ×1.19–1.41
    (stratified by colour, a mod 8 and size);
  * conditioning on the genus count drops these ratios to 0.93–1.08.

  So the measured advantage of SM roots is consistent with a pure genus explanation. The genus-conditioned MH point
  estimates lie between 0.930 and 1.081; no confidence interval or detection threshold is established, so a larger effect
  in another statistic or root selection is not excluded. The class inside the coset is B2.
* **Class-group data of −4p are forest data at the square vertices (Prop 3, PROVED dictionary).** The neighbours of
  b² are the forms (A, 2b, C) of discriminant −4p with A ≡ −1 (mod b²), and the edge colour is the genus character.
  Square roots are the weakest root family measured (668 failures ≤ 10⁸).

Census (CERTIFIED, all 1 439 970 primes p ≡ 1 (8) ≤ 10⁸):
* SP (PELLCYCLE's all-cycles set) never fails, extending PELLCYCLE's 2·10⁷;
* SM (−p a square mod a; the reduced-form minima of −4p up to √p) fails only at **19441**;
* SMN (non-principal genus of −4p, canonical non-residue roots) fails at **48 primes** (193, 457, …, 2521, 3361, 9601, …,
  98 719 993) at a decaying rate.

Survives: growing p-dependent root windows (Assessment: the window/HC-type question of §7.2), with the class group
contributing a genus-favoured filter and nothing else that was detected.

## 1. Setting and precise statements

**Forest.** F_p has vertices 1, …, p + 2; u ≠ v are adjacent iff uv | p + u + v. Facts used (PROVED in the cited files):
* F_p is a forest.
* Every edge {u < v} has u(u − 1) ≤ p + 1, so u < √p + 1.
* For gcd(x, p) = 1 the neighbours of x are exactly v = (p + x)/D with D | p + x, D ≡ −1 (mod x), v ≠ x. Equivalently,
  v | p + x and v ≡ −p (mod x).

  Sources: `LOWER_TAIL_ASTRA.md` Lemma 2.1, `Z52D_PELLCYCLE.md` Lemmas 1.2–1.3, `FOREST_INVERSE.md` Cor C.

So x is isolated ⟺ p + x has no divisor ≡ −1 (mod x). Colour χ_p(v) = (v/p). For p ≡ 1 (4) a bichromatic edge is
exactly a five-slice certificate (LTA Lemma 2.2, DEDEKIND_ES Thm 4.5).

**Class-group root sets.** All sets are, by definition, congruence filters on the window [1, ⌊√p⌋ + 1], which contains
every small endpoint of an edge. This is exactly what the engine computes.
* **SM(p)** = {a ≤ ⌊√p⌋ + 1 : −p is a square mod a}.
  * For a ≤ √p these are exactly the first coefficients ≤ √p of the reduced forms (a, 2b, c) of discriminant −4p (one
    reduced form per class of Cl(−4p), p ≡ 1 (4)).
  * *Proof.* (a, 2b, c) has disc −4p iff ac = p + b². Given −p ≡ b² (mod a), choose |b| ≤ a/2. Then c = (p + b²)/a ≥ a
    when a ≤ √p, so the form is reduced. The converse is immediate. ∎
  * At the boundary a = ⌊√p⌋ + 1 the identification can fail (p = 41, a = 7: c = 6 < 7). Reduced minima in
    (√p, √(4p/3)] are not in the window (at p = 19441: 29 distinct minima, of which 27 are in the window). Such vertices
    are forest leaves.
* **SP(p)** = {a ≤ ⌊√p⌋ + 1 : p is a square mod a}. For a < √p these are among the Q-values of the reduced irrationals
  (P + √p)/Q, Q | p − P² (`Z52D_PELLCYCLE.md` Prop 2.4(b)), i.e. PELLCYCLE's "all-cycles" root set. These cycles
  include imprimitive forms (e.g. Q = 2 at p = 17 gives (2, 6, −4), which is twice a form of discriminant 17), so SP is
  *not* identified here with the class group of a single discriminant; it is the congruence filter.
* **SMN(p)** = SM ∩ {χ_p = −1}. For a ≤ √p these are the minima of the reduced forms in the non-principal genus.
* **SQ** = {b²}: the perfect squares (Prop 3).
* Controls: ALL (every vertex) and NR (every non-residue).

**Colour on SM (PROVED).** Let p ≡ 1 (4) and a ∈ SM. Then 4 ∤ a, because −p ≡ 3 (4) is not a square mod 4. For every
odd prime ℓ | a, (ℓ/p) = (p/ℓ) = (−1/ℓ). Hence χ_p(a) = (2/p)^{v₂(a)}·χ_{−4}(a_odd), which is the genus character of the
form. On SP with p ≡ 1 (8) the colour is identically +1 (PELLCYCLE Lemma 2.1).

**Statements attacked.**
* (S1) **CG_R** for R ∈ {SM, SP, SMN, SQ}: for every prime p ≡ 1 (8) with p > p₀, some a ∈ R(p) lies in a component of
  F_p containing a bichromatic edge. Variants restrict the bichromatic edge to depth ≤ d edges from a. (At p ≡ 5 (8)
  the edge {1, 2} is bichromatic, so ALL, SM, SP, SQ hit at the root 1 and NR, SMN at the root 2.) These are
  CONJECTURE-shaped; status in §5.
* (S2) **Kill.** Do bounded class-group menus fail infinitely often under Dickson/H with unrestricted exploration?
  Answer: yes (Theorem 1).
* (S3) **Escape and mechanism.** Is the full class-group data enumerable by a fixed polynomial recipe on a polynomial
  family? It is not (Prop 2(i)–(ii)). What does it provably control in the forest? A genus positivity at its roots
  (Lemma G) and the square vertices (Prop 3).

## 2. Why this was not already closed

Previously closed:
* fixed roots {1..H} (LTA Thm 3.2);
* the single least-non-residue root (LTA Thm 5.1);
* the principal-cycle menu R3 ∪ U (PELLCYCLE Thm 1.1);
* bounded coordinate lines (LOWERTAIL_ROUND2_FABLE Prop 3.3).

PELLCYCLE §3.5/§4 left "the all-cycles (class-group) root set" open; it had 0 failures to 2·10⁷. FRONTIER §3 lists
"class-group cycle data" under "does NOT rule out". Two features make the class group a different object from those
menus:
* the reduced forms of −4p have p^{1/2−o(1)} distinct minima at *every* p (Prop 2), and they are not frozen at
  near-squares (unlike the principal cycle at m² + 1);
* SMN supplies canonical *non-residue* roots, which the fixed-root menus lack.

Theorem 1 closes the listed bounded menus (Cor 1.1), and Props 2–3 and Lemma G locate the unbounded part.

## 3. Theorem 1: bounded class-group menus fail infinitely often (CONDITIONAL on Dickson)

**Theorem 1.** Assume Dickson's conjecture for finitely many linear forms. For all integers H ≥ 3 and K ≥ 1 there are
infinitely many primes p ≡ 1 (mod 24) such that every component of F_p meeting

  R_{H,K}(p) := {1, 2, …, H} ∪ {the K least quadratic non-residues mod p}

is monochromatic. Moreover, these p can be chosen so that the least quadratic non-residue ℓ(p) = q is a prime ≡ 3 (mod 4)
and the K least non-residues are q, 2q, …, Kq.

*Construction.*
1. Choose a prime q ≡ 3 (mod 4) with q > H + 1, q > K and (q − 1)/2 > H + Σ_{j≤K} τ(1 + qj). Such q exist since
   τ(m) ≤ 2√m makes the right side O(H + K^{3/2}q^{1/2}).
2. Let B := {q − i : 1 ≤ i ≤ H} ∪ {c : c·d ≡ −1 (mod q) for some j ≤ K and some d | 1 + qj}. Then |B| < (q − 1)/2, so
   some quadratic non-residue c mod q has c ∉ B.
3. Put Y := qK + 2 and 𝒫 := {primes ℓ ≤ Y, ℓ ≠ q}. For ℓ ∈ 𝒫 let e_ℓ := 1 + max_{1≤m≤Y} v_ℓ(m), so that ℓ^{e_ℓ} > Y.
4. Put Q₀ := ∏_{ℓ∈𝒫} ℓ^{e_ℓ}, Q := q·Q₀·rad(Q₀) and X := {1, …, H} ∪ {qj : 1 ≤ j ≤ K}.
5. Let p₀ mod Q satisfy p₀ ≡ 1 (mod Q₀rad Q₀) and p₀ ≡ c (mod q). Consider the 1 + H + K linear forms

  P(s) = p₀ + Qs,   L_x(s) = (p₀ + x)/(1 + x) + (Q/(1 + x))·s   (x ∈ X),

   so that P(s) + x = (1 + x)·L_x(s).

*Integrality.* Every prime ℓ | 1 + x lies in 𝒫:
* ℓ ≤ 1 + x ≤ Y − 1;
* q ∤ 1 + x, since 1 + x ≤ H + 1 < q for x ≤ H, and 1 + qj ≡ 1 (mod q).

Moreover v_ℓ(1 + x) < e_ℓ and p₀ + x ≡ 1 + x (mod ℓ^{e_ℓ}), so (1 + x) | p₀ + x and (1 + x) | Q.

*Admissibility.*
* (α) Let ℓ ∈ 𝒫. Then v_ℓ(Q) = e_ℓ + 1 ≥ v_ℓ(1 + x) + 2, so every slope is ≡ 0 (mod ℓ). The constants are p₀ ≡ 1 and
  L_x(0) = 1 + (Q₀rad Q₀/(1 + x))·m ≡ 1 (mod ℓ), where p₀ = 1 + Q₀rad(Q₀)m. So every form is ≡ 1 (mod ℓ) for all s.
* (β) Let ℓ = q. All slopes are ≡ 0 (mod q), and the constants are p₀ ≡ c ≢ 0 and L_x(0) ≡ (c + x)(1 + x)^{−1}. For
  x = qj this is ≡ c ≢ 0; for x = i ≤ H it is ≢ 0 because c ≠ q − i.
* (γ) Let ℓ > Y. All slopes divide powers of primes ≤ Y, so they are nonzero mod ℓ. Each of the 1 + H + K ≤ Y < ℓ forms
  therefore kills exactly one class of s mod ℓ, and some class survives.

The slopes Q and Q/(1 + x) are pairwise distinct. Dickson therefore gives infinitely many s ≥ 1 with P(s) and all
L_x(s) prime. Fix one and put p = P(s).

*Proof of the properties.* (Recall that a vertex x prime to p is isolated iff p + x has no divisor ≡ −1 (mod x).)
1. **p ≡ 1 (mod 24).** q ≥ 7, so 2, 3 ∈ 𝒫 and 16·27 | Q₀ (Y ≥ 9).
2. **Characters and least non-residues.**
   * For ℓ ∈ 𝒫, (ℓ/p) = +1: for odd ℓ by reciprocity, since p ≡ 1 (mod 4ℓ); for ℓ = 2 since p ≡ 1 (8).
   * (q/p) = (p/q) = (c/q) = −1.
   * Hence χ_p(a) = (−1)^{v_q(a)} for every a whose prime factors are ≤ Y.
   * Every a ≤ Kq < Y has this property, and since K < q, v_q(a) is odd iff q | a. So the non-residues in [1, Kq] are
     exactly q, 2q, …, Kq. These are the K least non-residues, and ℓ(p) = q.
3. **The component of 1.**
   * p + 1 = 2L₁, p + 2 = 3L₂ and p + 3 = 4L₃ with L₁, L₂, L₃ prime.
   * Writing p = 24k + 1, these are r = 12k + 1, s = 8k + 1, w = 6k + 1 of LTA Thm 3.1.
   * So comp(1) = {1, 2, 3, r, 2r, s, 3s, 2w}, all residues (LTA Thm 3.1; its proof uses only these three primalities
     and p ≡ 1 (24)).
4. **Vertices 4 ≤ i ≤ H are isolated.**
   * p + i = (1 + i)L_i with L_i a prime > 1 + i.
   * L_i − 1 = (p − 1)/(1 + i). Since p − 1 ≡ 0 (mod ℓ^{e_ℓ}) for each ℓ | i, and gcd(i, 1 + i) = 1, we get
     L_i ≡ 1 (mod i).
   * The divisors of p + i are e and eL_i with e | 1 + i, and both are ≡ e (mod i). A divisor ≡ −1 (mod i) would need
     e ≡ −1 (mod i) with e ≤ i + 1, i.e. e = i − 1 | i + 1, i.e. i ≤ 3.
5. **Vertices x = qj (j ≤ K) are isolated.**
   * p + x = (1 + x)L_x with L_x a prime > 1 + x.
   * L_x ≡ c (mod q), since 1 + qj ≡ 1 (mod q).
   * The divisor e itself would need e = qj − 1 | qj + 1, i.e. qj ≤ 3, which is impossible.
   * The divisor eL_x ≡ −1 (mod qj) would give ec ≡ −1 (mod q) with e | 1 + qj, i.e. c ∈ B, which is excluded.

So the components meeting R_{H,K}(p) are comp(1) and singletons, all monochromatic. ∎

**Corollary 1.1 (the class-group menus inside R_{H,K}; PROVED for the Theorem 1 family).** Let
T := {s ≥ 1 : −1 is a square mod s}, i.e. v₂(s) ≤ 1 and every odd prime factor ≡ 1 (4), with elements t₁ = 1 < t₂ = 2 <
t₃ = 5 < … . At the primes of Theorem 1:
* (a) SM ∩ [1, q) = T ∩ [1, q), since (−p/ℓ) = (−1/ℓ) for ℓ ∈ 𝒫 and 4 ∤ a. So the first K′ elements of SM, i.e. the K′
  smallest reduced-form minima of Cl(−4p), lie in [1, H] once t_{K′} ≤ H.
* (b) SMN ∩ [1, Kq] = {q·s : s ∈ T, s ≤ K}, because −p ≡ −c is a square mod q (q ≡ 3 (4), c a non-residue). So the first
  K′ non-principal-genus minima lie in the menu once t_{K′} ≤ K.
* (c) SP ∩ [1, q) = [1, q).
* (d) The two genus minima of Cl(−4p) are 1 and q. The ambiguous classes (p ≡ 1 (4): 2-rank 1) have reduced forms
  (1, 0, p) and (2, 2, (p + 1)/2), with minima 1 and 2.
* (e) The least split prime of ℚ(√−p) is 5. For 5^k ≤ √p the reduced form of the class [𝔩₅]^k is (5^k, 2b_k, c_k):
  𝔩₅^k is primitive of norm 5^k, and |b_k| ≤ 5^k/2 gives c_k ≥ 5^k. So the first orbit elements 5, 25, … (up to H) lie
  in the menu.

Hence each menu of the listed types (and only these are claimed) fails infinitely often under Dickson, even with
unrestricted exploration of the components. Not covered: arbitrary bounded-size functions of class-group data, prefixes
of the orbit of a p-dependent split class, prefixes of an individual real reduction cycle. (Any "first K′ positions" of SM, SP, SMN or NR, genus minima, ambiguous
forms and orbit prefixes of the chosen prime-5 class are all covered by suitable H, K.)

**Verified instances** (CERTIFIED by complete exploration; `scripts/z53_forestclass_thm1inst.py`,
`data/z53/forestclass/thm1_instances.txt`). Each instance was certified by exploring every component meeting the menu
completely and finding it monochromatic. The script does not use the literal construction above: it uses q = 11, c = 2
(with c ∉ B checked directly; step 1's inequality is sufficient, not necessary) and a smaller modulus that still imposes
the needed local conditions. So these are instances of the conclusion and of its factorisation pattern.
* With all Dickson forms prime (the theorem's hypothesis), (H, K, q, c) = (3, 1, 11, 2): p = 21 679 561, 25 061 401,
  36 814 681. With (5, 1, 11, 2): p = 13 911 395 401, 17 676 603 001.
* With the menu condition checked directly (forms not necessarily prime):
  * (8, 1): five primes ≈ 2·10¹⁰–9·10¹⁰;
  * (8, 2): p = 41 062 447 692 302 401, …;
  * (8, 3): p = 8 368 042 654 987 245 266 401, …, whose least non-residues are 11, 22, 33.

At the five (8, 1) instances ALL and SP still hit at a = 9 or 10, just outside the frozen menu; SM first hits at 10 or
17, and SMN at 19–43. So bichromatic edges exist elsewhere and ES is not contradicted.

*Scope.* This is the campaign's Dickson-shadow mechanism (LTA Thms 3.2, 5.1; DISPROOF_AVENUES Prop 3.1), now with K
non-residue roots plus H fixed roots simultaneously. It does not subsume LOWERTAIL_ROUND2_FABLE Prop 3.3, whose
conclusions concern level coordinates and many words. It says nothing about menus whose size grows with p.

## 4. The unbounded part: escape, filter, genus layer, squares

**Proposition 2 (the full set of reduced-form minima of −4p is not a bounded recipe; PROVED relative to Siegel's
theorem).** Let p ≡ 1 (4).
* (i) The first coefficients of the reduced forms of discriminant −4p take at least h(−4p)·p^{−o(1)} ≫_ε p^{1/2−ε}
  distinct values, all ≤ √(4p/3).
* (ii) Let f ∈ ℤ[s] be nonconstant, and let r₁, …, r_m ∈ ℤ[s] be finitely many root recipes. Then the recipes account for
  at most m of these minima at each prime p = f(s), while the number of minima tends to infinity. So no fixed finite
  list of polynomial-valued roots enumerates the full set (no PELLCYCLE- or LTA-type freezing of the whole set).
* (iii) For every fixed a ≥ 1, the untruncated predicates "−p is a square mod a", "p is a square mod a" and the value
  χ_p(a) are functions of p mod 8a. Hence, for X ≤ ⌊√p⌋ + 1, the sets SM(p) ∩ [1, X], SP(p) ∩ [1, X] and SMN(p) ∩ [1, X]
  are functions of p mod 8·lcm(1, …, X). The window cutoff itself depends on p, so this fails for X beyond the cutoff:
  17 ≡ 20177 (mod 20160), but 8 ∈ SP(20177) while 8 > ⌊√17⌋ + 1.

*Proof.*
* (i) Given a, a reduced form (a, 2b, c) has b ∈ (−a/2, a/2] with b² ≡ −p (mod a). There are at most 2^{ω(a)+1} such b,
  and 2^{ω(a)} = p^{o(1)} for a ≤ p. Each class has exactly one reduced form, so the number of distinct minima is
  ≥ h(−4p)/max_a 2^{ω(a)+1}. Siegel gives h(−4p) ≫_ε p^{1/2−ε}.
* (ii) Immediate from (i).
* (iii) Whether −p (or p) is a square mod a depends only on p mod a, for a ≤ X; the colour χ_p(a) of a ≤ X depends only
  on p mod 4a, by reciprocity. ∎

(No lower bound is claimed for SP, nor for the truncated sets SM, SMN: Prop 2(i) concerns the full set of reduced
minima up to √(4p/3).)

*Reading.* Prop 2(i)–(ii) is an escape from B1 of type E1/E2: the reduced forms of −4p are a p-dependent family of size
p^{1/2−o(1)}, and no fixed polynomial list enumerates them along a polynomial family. Prop 2(iii) says that *as a forest
root set* the class-group data are a congruence-filtered window. A statement "some a ∈ SM(p) ∩ [1, X(p)] lies in a
bichromatic component" is a growing-window statement restricted to the filter. (Assessment: it is of the HC/window type,
but not equivalent to FRONTIER's HC, which includes the level coordinate and whose components leave the window.)

The filter's density is not uniform in p. For fixed X, CRT and Dirichlet give p with SM ∩ [1, X] = {1, 2}, and other p
with every a ≤ X, 4 ∤ a, in SM. Heuristic (Assessment): typically the density is ≍ (log X)^{−1/2}, by a Landau–Bernays-
type count at fixed discriminant. EVIDENCE consistent with this: the SM share of *hit roots* falls from 0.256 to 0.214
across 10⁹–10¹³, close to the (log p)^{−1/2} rate. This is the share of hits, not the density of the filter.

**Lemma G (genus positivity at class-group roots; PROVED, elementary).** Let p be an odd prime and a ≥ 3 with p ∤ a. Put
N = p + a, G = (ℤ/a)^×, X = Hom(G/G², {±1}) (the real characters mod a, |X| = [G : G²]) and c ≡ −p (mod a). Note
gcd(N, a) = 1, so every divisor of N is a unit mod a.
1. **Neighbour criterion.** Every neighbour d of a satisfies d | N and d ≡ c (mod a). In particular d ∈ cG².
2. **Coset counts.** #{d | N : d ∈ cG²} = |X|^{−1} Σ_{χ∈X} χ(c)σ_χ(N), where σ_χ(N) = Σ_{d|N} χ(d) ≥ 0 for every
   χ ∈ X.
3. **Genus obstruction.** Let β : G → G/G² ≅ 𝔽₂^r. Then #{d | N : d ∈ cG²} > 0 iff β(c) lies in the span of
   {β(ℓ) : ℓ prime, ℓ | N}. If not, a is isolated ("genus-obstructed").
4. **No obstruction at SM.** If a ∈ SM, i.e. c ∈ G², then #{d | N : d ∈ G²} ≥ τ(N)/|X|: the target coset gets at least
   its fair share of divisors, and a is never genus-obstructed. If a ∉ SM, a is genus-obstructed whenever every prime
   factor of N is a square mod a.

*Proof.*
1. This is the neighbour criterion of §1.
2. Orthogonality on G/G², using χ(c)^{−1} = χ(c) for real χ. σ_χ is multiplicative, and for a prime power ℓ^e ∥ N we
   have σ_χ(ℓ^e) = Σ_{i≤e} χ(ℓ)^i, which is e + 1 or 0 or 1; so σ_χ(N) ≥ 0.
3. The image of the divisors under β is {Σ e_ℓ β(ℓ) : 0 ≤ e_ℓ ≤ v_ℓ(N)}, which equals the span (exponents 0 and 1
   suffice).
4. Take c ∈ G². Then χ(c) = 1 for every χ ∈ X, so the sum in 2 is ≥ σ_1(N) = τ(N). The last sentence is 3 with span
   {0} ∌ β(c). ∎

*Reading.* The genus/BM layer is pointwise free *on* the class-group roots. This is one-way: non-SM vertices are often
unobstructed too (p = 17, a = 4 or 5; 360 342 119 of the 574 180 858 non-SM vertices of the sample below). It is a
vertex-level analogue of (J)103 Prop 2.2. What remains at a ∈ SM is to hit the single class c inside the coset cG² of size φ(a)/[G : G²]. That is B2
(FRONTIER §4 screen 9: class, not parity), and τ(N)/|X| is far below φ(a)/|X|.

**EVIDENCE that the SM enrichment is a genus-layer effect** (`scripts/z53_forestclass_genusenrich.py`, file
`data/z53/forestclass/genusenrich_s9_s12.txt`). Data: all 6.7·10⁸ vertices a ∈ [1, √p + 1] at 4 800 random primes
p ≡ 1 (24) at 10⁹, 10¹⁰, 10¹¹, 10¹². The engine's genus counts were checked against brute force on 129 829 pairs
(n, a), with 0 mismatches.
* **Lemma G is respected.** 213 838 739 genus-obstructed vertices, of which 0 are non-isolated. They make up 37.2 % of
  the non-SM vertices and 0 % of the SM vertices.
* **SM enrichment disappears after conditioning on the genus count.** Mantel–Haenszel ratios for SM membership, with
  strata (χ_p(a), a mod 8, ⌊log₂ a⌋) without and with an extra stratum for the genus-layer expected number of neighbours
  μ = g·[G : G²]/φ(a) (two buckets per octave):

| a range | non-isolated, blind | non-isolated, genus-conditioned | in bichromatic component, blind | genus-conditioned |
|---|---:|---:|---:|---:|
| [2⁴, 2⁷) | 1.142 | 0.960 | 1.189 | 1.003 |
| [2⁷, 2¹⁰) | 1.215 | 1.014 | 1.241 | 1.049 |
| [2¹⁰, 2¹³) | 1.260 | 1.015 | 1.296 | 1.056 |
| [2¹³, 2¹⁶) | 1.323 | 1.030 | 1.373 | 1.081 |
| [2¹⁶, 2¹⁹) | 1.348 | 0.967 | 1.410 | 1.033 |
| [2¹⁹, 2²²) | 1.318 | 0.930 | 1.404 | 1.011 |

  The blind ratios agree with the 10⁷–10⁸ census (1.20–1.62; `strat_1e7_1e8.txt`). For SP the blind ratios are 0.85–0.98
  (a depletion). This is consistent with the genus picture: for a ∈ SP the target −p ≡ −s² lies in G² only when −1 does
  (v₂(a) ≤ 1 and every odd prime of a ≡ 1 (4)). Otherwise the target coset of an SP vertex is non-principal, and the
  vertex is then genus-obstructed whenever every prime factor of p + a is a square mod a (Lemma G(3)).
* No standard errors are given: vertices of one prime are dependent, and the genus buckets are coarse (factor √2).
  Assessment: the genus-conditioned MH point estimates lie between 0.930 and 1.081. They are consistent with a pure
  genus explanation. No confidence interval or detection threshold is established (common-support stratification and
  within-prime dependence matter), so this does not exclude a larger effect in another statistic or root selection.

**Proposition 3 (class-group data of −4p are forest data at square vertices; PROVED dictionary).** Let p ≡ 1 (4) be prime
and b ≥ 1 with b² ≤ p + 2.
* (i) The neighbours of the vertex b² in F_p are exactly the C ≠ b² for which some positive definite form (A, 2b, C) of
  discriminant −4p has A ≡ −1 (mod b²). The correspondence is A = (p + b²)/C.
* (ii) The colour χ_p(C) equals the genus character of the class of (A, 2b, C) (the assigned character (·/p) on values
  prime to p). So the edge {b², C} is bichromatic iff the form lies in the non-principal genus.
* (iii) For b even, every edge at b² is bichromatic. For b odd, exactly one of A, C is even, and the edge is
  bichromatic iff the odd one of A, C is ≡ 3 (mod 4).
* (iv) Let a ∈ SM with a > 1, and let (a, 2b, c) be a reduced form with b ≠ 0 and b² < a. Then r_a = −p mod a = b², so
  the only possible smaller neighbour of a is the square vertex b². The edge {b², a} exists iff b² | c + 1. (At p = 269
  the form (13, 4, 21) has b² = 4 ∤ 22, so vertex 13 has no smaller neighbour.)

*Proof.*
* (i) Write D for the cofactor (p + b²)/C. By the neighbour criterion, C is a neighbour iff C | p + b² and
  D ≡ −1 (mod b²). Then (D, 2b, C) has discriminant 4b² − 4DC = −4p. Conversely AC = p + b² for such a form.
* (ii) C and A are both values of the form, and neither is divisible by p: p | C or p | A would give p | p + b², so p | b.
  Then b² ≥ p² > p + 2, so b² would not be a vertex. By genus theory, all values of one form that are prime to p
  have the same symbol (·/p) (the assigned character for the odd prime p | D), so χ_p(C) = χ_p(A) is a class invariant.
  Finally χ_p(b²) = 1.
* (iii) Let m ∈ {A, C} be odd. Then gcd(m, b) = 1, since a common factor would divide p. Also p ≡ −b² (mod m), so
  χ_p(m) = (p/m) = (−1/m) by reciprocity (p ≡ 1 (4)). If b is even then A ≡ −1 (mod 4) is odd, and χ_p(A) = −1. If b is
  odd then p + b² ≡ 2 (mod 4), so exactly one of A, C is odd, and its residue mod 4 decides.
* (iv) −p ≡ b² (mod a) with 0 ≤ b² < a gives r_a = b². The edge exists iff b² | p + a = a(c + 1) − b², i.e. iff
  b² | a(c + 1); since gcd(a, b) = gcd(a, p) = 1, this means b² | c + 1. ∎

*Reading (Assessment).* Class-group data of −4p are the factorisations of the quadratic family p + b². The forest needs
the linear family p + a. The two meet at the square vertices. For a general a ∈ SM the neighbourhood is factorisation data of
p + a = a(c + 1) − b², i.e. of the discriminant of (a, 2b, c + 1), which is −4(p + a). That is not class-group data of
−4p. The square-vertex subforest is the weakest root family measured (§5): in that sense the class group controls the
factorisations where they help least.

## 5. Computations (CERTIFIED counts; rates EVIDENCE)

Engine `scripts/z53_forestclass_forest.c` builds the whole forest:
* segmented factorisation of p + u for u ≤ √p + 2;
* all edges from the neighbour criterion, each checked exactly (uv | n + u + v);
* union–find, bichromatic flags, and multi-source BFS depths.

For each root set it reports the size, the hits (full component, depth ≤ 1, depth ≤ 2), and the first hit with its rank.
Independent check: `scripts/z53_forestclass_bruteverify.py` (AP edge enumeration, exhaustive square tests) reproduces
every output line for all 1 607 runs (1 586 distinct n) in {odd 5..1999} ∪ {odd squares ≤ 99²} ∪ {primes ≡ 1 (4) in [2000, 12000]}, with
0 mismatches. Genus counts were also checked (Lemma G, above).

**Census, all 1 439 970 primes p ≡ 1 (8) ≤ 10⁸** (`census_1e7_summary.txt`, `census_1e7_1e8_summary.txt`). Primes
p ≡ 5 (8) all hit (at root 1, or root 2 for NR and SMN).

| root set | failures, full component | depth ≤ 2 | depth ≤ 1 | max rank of first hit (a, p) |
|---|---:|---:|---:|---|
| ALL | 0 | 0 | 0 | 25 (a = 25, p = 78 168 721) |
| SP (all cycles of 4p) | **0** | 0 | 0 | 28 (a = 32, p = 19 231 801) |
| SM (reduced forms of −4p) | **1** (19441) | 1 | 6 | 183 (a = 911, p = 4 149 601) |
| NR | 0 | 0 | 0 | 66 (a = 339, p = 41 751 889) |
| SMN (non-principal genus) | **48** | 48 | 54 | 375 (a = 4679, p = 23 544 721) |
| SQ (squares) | 668 | 4 983 | 19 583 | 94 (a = 8836, p = 81 326 281) |

* **SMN failures:**
  * ≤ 10⁷ (34): 193, 457, 1873, 2377, 2521, 3361, 9601, 12433, 19441, 27073, 42697, 62497, 129193, 198937, 219433,
    294793, 360193, 455953, 467713, 481153, 595081, 762721, 874729, 981481, 1932001, 2057113, 2178313, 3097537, 3823177,
    5552737, 5828593, 5900953, 6270793, 9451513;
  * in [10⁷, 10⁸) (14): 10049713, 12570721, 12943393, 16433113, 19306057, 20072497, 20880553, 22711753, 51703633,
    57360697, 59774233, 89954593, 93727657, 98719993.
  * Rate per prime: 2·10⁻⁴ below 10⁷, 1.1·10⁻⁵ in [10⁷, 10⁸).
  * The failures are ticket-starved (EVIDENCE, `scripts/z53_forestclass_smnquantile.py`, `smn_fail_quantiles.txt`).
    For each failure p we compute the fraction of comparators with strictly smaller |SMN(p′)|/√p′. Comparators are the
    non-failing census primes p′ ≡ 1 (8) with |p′ − p| ≤ 0.1p. Windows are clipped at 10⁸, and 193 has no comparator.
    For the other 47 failures the mean of this quantile is 0.056; 35 of the 47 lie at or below 0.05 and 38 at or below
    0.10. For |SM(p)|/√p, a proxy for h(−4p)/√p, the mean
    quantile is 0.053. Assessment: SMN fails where Cl(−4p) has few small minima, i.e. where −p is a non-square modulo
    many small primes (small L(1, χ_{−4p})). This is a loaded lottery, not a structural obstruction. It matches the
    observation that the (★)-zeros have small h(−4p) (`BRAINSTORM/z52b_fingerprint.md` item 131).
* At 19441 the bichromatic components are {7, 26, 68, …}, {20, 39, 499} and {38, 129}. They contain SP roots and
  non-residues, but no SM root.
* SP's success comes from small roots: 4, 8, 3, … are in SP whenever p ≡ 1 (24), and the maximal first-hit rank is 28.
  These are exactly what Theorem 1 freezes.

**Samples** (random p ≡ 1 (24): 3 000 at 10⁹, 1 000 at 10¹⁰, 500 at 10¹¹, 300 at 10¹², 100 at 10¹³; `out_sample_*`):
every set hits at every prime, including SMN and SQ. Mean number of hit roots per prime:

| 10^k | ALL | SM | SP | SMN | SQ | SM share of ALL |
|---|---:|---:|---:|---:|---:|---:|
| 9 | 124.0 | 31.7 | 49.6 | 19.6 | 4.5 | 0.256 |
| 10 | 155.7 | 37.7 | 60.6 | 23.8 | 4.7 | 0.242 |
| 11 | 194.4 | 44.8 | 72.8 | 28.7 | 4.9 | 0.230 |
| 12 | 236.0 | 51.5 | 85.6 | 33.0 | 5.3 | 0.218 |
| 13 | 281.8 | 60.3 | 105.7 | 39.6 | 5.4 | 0.214 |

The ALL count grows roughly like (log p)², and the SM share falls at roughly the (log p)^{−1/2} rate, so the SM count
grows roughly like (log p)^{3/2} (EVIDENCE over five decades only; Assessment: a sub-lottery, not a mechanism).

**Hard primes** (134; `hard_primes.txt`, `out_hard.txt`):
* the 14 (★)-zeros;
* 193, 2521, 3361, 66529, 5101441;
* the HC-hard 21841, 92401, 691681, 83816041, 147223441;
* PELLCYCLE's R0/R3 failures (22);
* its six H-instances up to 1.02·10¹⁴;
* the eight R3 ∪ U-failing near-squares;
* the 59 Dickson-family primes 2521 + 9240a;
* LTA's root-1 failures;
* the Theorem 1 instances at ≈ 10¹⁰.

Results: SM fails only at 19441; SP never; SMN at 193, 2521, 3361, 9601, 19441. At every PELLCYCLE H-instance (where
the whole principal-cycle menu is monochromatic) SM and SP hit at a ≤ 11, so the all-cycles filter rescues what the
principal cycle cannot. The rescuing roots are again small, congruence-determined ones.

**Controls.**
* **Odd squares.** All 5 000 odd squares m² ≤ 10 001² have 0 bichromatic edges (T1; `out_oddsquares_bi.txt`), so every
  root set "fails" there, as it must.
* **Near-squares.** All 1 330 primes m² + 1 with 12 | m ≤ 120 000: SM, SP, SMN never fail (max SMN rank 94); SQ fails at
  1 299 601.

## 6. The four FRONTIER §4 hard screens (for the surviving statement CG_SM / CG_SP)

These are consistency checks of a conjecture-shaped statement, not of a proof.
1. **T1 (odd squares). Consistent.** At n = m² every unit vertex has colour +1, so there is no bichromatic edge
   (CERTIFIED for 5 000 squares). The false-at-squares step is the colouring, not the root set. Lemma G is true at
   squares as well; Assessment: so by itself it can only be a main-term (genus) input.
2. **8/131. Not applicable.** The certificate criterion "bichromatic edge" is 4-specific (DEDEKIND_ES Thm 4.5). No
   numerator-uniform step is used, and nothing here is a proof that could transfer.
3. **Tied modulus. FAILS.** At a root a the neighbour condition is d | p + a with d ≡ −p (mod a): a divisor of one
   integer in one class, modulo the root itself. For a ∈ SM the target lies in the principal genus coset (Lemma G); for
   SP it need not. No input found here controls the class inside the coset, which is B2.
4. **Fixed p. Consistent** for the statements and theorems. The enrichment evidence of §4 is averaged over primes,
   which is fine as EVIDENCE only (B6).

## 7. Proposed FRONTIER text (not edited here)

* **§7.2, after the PELLCYCLE sentence.**

  "*(z53, `Z53_FORESTCLASS.md`.)* Class-group roots, as tested, do not escape either:
  * For all H, K infinitely many p ≡ 1 (24) have every component meeting {1..H} ∪ {K least non-residues}
    monochromatic, with ℓ(p) = q ≡ 3 (4) (Thm 1, CONDITIONAL on Dickson; verified instances). So the following bounded
    menus fail i.o., even with unrestricted exploration: the genus minima and ambiguous-form minima of Cl(−4p); the first
    K′ elements of SM = {a : −p □ mod a}, of its non-principal-genus part, and of PELLCYCLE's all-cycles set
    SP = {a : p □ mod a}; the first powers of the class of a prime above 5. Arbitrary bounded functions of class-group
    data are not covered.
  * The reduced-form minima of −4p number p^{1/2−o(1)} (Prop 2, rel. Siegel), so no fixed polynomial recipe enumerates
    them. As root sets the class-group data are congruence-filtered windows.
  * At class-group roots a ∈ SM there is never a genus obstruction to a neighbour (Lemma G, PROVED; one-way). The
    ×1.14–1.41 enrichment of SM roots falls to MH point estimates 0.930–1.081 after conditioning on genus counts
    (EVIDENCE; consistent with a genus explanation, no confidence interval or detection threshold established).
  * Class-group data of −4p are forest data at the square vertices (Prop 3).
  * CERTIFIED to 10⁸ (p ≡ 1 (8)): SP never fails, SM fails only at 19441, its non-principal-genus part at 48 primes.

  The growing-root question is thus a growing-window question with a genus-favoured filter (Assessment)."
* **§3 "Rooted constructions …", "Does NOT rule out".** Replace "class-group cycle data" by "growing (unbounded)
  class-group root sets (whose measured effect is the genus layer, Z53_FORESTCLASS Lemma G and §4) and bounded
  class-group functions other than those of Z53_FORESTCLASS Cor 1.1".
* **§6, one line.** "Bounded class-group root menus of the types in Z53_FORESTCLASS Cor 1.1 (genus and ambiguous
  minima, first K′ elements of SM, SMN, SP, K least non-residues, prefixes of the class of a prime above 5) in F_p →
  fail i.o. under Dickson → Z53_FORESTCLASS Thm 1."

## 8. Bottom line

The class groups of ±4p are the natural p-dependent root source that FRONTIER §7.2 left open. As forest roots they
behave as follows:
* the bounded menus enumerated in Cor 1.1 fail under Dickson, with K non-residue roots and H fixed roots at once
  (Theorem 1, CONDITIONAL);
* the full set of reduced-form minima of −4p cannot be enumerated by any fixed finite list of polynomial values (Prop 2,
  PROVED rel. Siegel). This does not exclude polynomially indexed growing enumerations; it does not give a
  positive-discriminant analogue; and it does not give the same cardinality bound for the truncated SM, SMN, SP.
* The one proved forest input is Lemma G: a class-group root never has a genus obstruction to having a neighbour.

The measured advantage of class-group roots is consistent with that genus layer alone (EVIDENCE: genus-conditioned
MH point estimates 0.930–1.081, no confidence interval or detection threshold established). The one place where class-group data *are* forest data, the square vertices (Prop 3), is the weakest root family.
Certified to 10⁸: the all-cycles set never fails, and the reduced-form set fails once (19441). The canonical
non-principal-genus roots fail 48 times, at a decaying rate. Nothing found supplies the class of a divisor inside its
genus coset, which is where B2 sits. The surviving question is the growing-window one (Assessment: HC-type). ES remains
open.

## 9. Reproduction and review

```
gcc -O2 -o /tmp/z53fc scripts/z53_forestclass_forest.c -lm; gcc -O2 -o /tmp/z53primes scripts/z53_forestclass_primes.c -lm
ulimit -v 6000000
/tmp/z53primes 5 10000000 4 1 | timeout 1700 /tmp/z53fc -s strat_1e7.txt > census_1e7.txt          # 2.5 min
for i in 0..8: /tmp/z53primes $((10^7*(i+1))) $((10^7*(i+2))) 8 1 | /tmp/z53fc -s strat_$i.txt > census_$i.txt
uv run python scripts/z53_forestclass_summarize.py census_*.txt
uv run --with sympy python scripts/z53_forestclass_lists.py data/z53/forestclass      # hard list + seeded samples
/tmp/z53fc -s G < data/z53/forestclass/sample_1e9.txt  (… 1e13);  uv run python scripts/z53_forestclass_genusenrich.py G.genus
uv run python scripts/z53_forestclass_bruteverify.py < list   # independent re-implementation, diff against /tmp/z53fc
Z53DBG=1 /tmp/z53fc -q < list | uv run --with sympy python scripts/z53_forestclass_genuscheck.py
uv run --with sympy python scripts/z53_forestclass_thm1inst.py H K q c NFOUND [maxtries] [dickson]
```

**Review.** A hostile deep-mode subagent reviewed the first full draft (report
`data/z53/forestclass/REVIEW_round1.md`; verdict REJECT as written, with Theorem 1 and the numbers sound). It re-derived
Theorem 1, Cor 1.1, Prop 2(i), Lemma G, the SM colour formula and Prop 3(i)–(iii), and reproduced the numbers
independently:
* its own forest checker at 11 primes, including 19441, 2521 and 3361;
* complete exploration and Lucas primality certificates for all 16 Theorem-1 instances;
* every census, sample, enrichment and quantile figure.

Its twelve findings were all applied:
1. (FATAL to the headline) "a ∈ SM ⟺ no genus obstruction" was false (p = 17, a = 4 or 5). Lemma G is now one-way
   everywhere.
2. "Only / exactly the genus layer" was replaced by "consistent with; nothing further detected". HC equivalence is now
   an Assessment.
3. SM and SP are defined as the congruence filters actually computed, with the reduced-form identification restricted to
   a ≤ √p, and the boundary, cutoff and imprimitive-cycle caveats added.
4. Prop 2(iii) is restricted to untruncated predicates and to X ≤ ⌊√p⌋ + 1, with the reviewer's counterexample.
5. Prop 2 is restricted to the full set of −4p minima; the wrong regulator remark was removed.
6. The density claim is now a heuristic, with the non-uniformity in p made explicit.
7. "Every bounded menu" was replaced by the enumerated families of Cor 1.1; the non-subsumption of FABLE Prop 3.3 is
   stated.
8. Prop 3(iv) now says "only possible parent" (counterexample p = 269, a = 13).
9. At p ≡ 5 (8), NR and SMN hit at root 2.
10. The quantile comparator population is documented.
11. 1 607 runs on 1 586 distinct inputs; SP mean at 10¹² is 85.6.
12. The instances are described as instances of the conclusion with a reduced modulus.

**Cross-model review** (`data/z53/xreview/REVIEW_FORESTCLASS.md`, audit script
`scripts/z53_xrev_forestclass_check.py`). Verdict ACCEPT-WITH-FIXES ("Narrowed" supported). The review re-derived
Theorem 1, Cor 1.1, Props 2–3 and Lemma G, and reran the census to 10⁷ byte-identically. It also built independent
forests at 57 primes (all 48 SMN failures, 19441 and the maximum-rank witnesses), reran all 668 SQ failures, gave Lucas
proofs for all 16 instances and their Dickson forms, and re-aggregated the genus and sample data; everything agreed.

Its three scope fixes were applied:
1. "Orbit prefixes of a split class" is now "of the chosen prime-5 class" (Cor 1.1), and §8 now says the bounded
   menus enumerated in Cor 1.1 fail.
2. "No effect at the ±10 % level" is now the genus-conditioned MH point estimates 0.930–1.081, with no confidence
   interval or detection threshold established (§0, §4, §7, §8).
3. §8's "non-quasi-polynomial" is removed, and Prop 2's exclusion is restated precisely: no fixed finite value lists for
   the full −4p minimum set, with no positive-discriminant analogue and no bound for the truncated sets.
