# CONJECTURE_S_MODEL — bracketing certificate survival in the prime-Haar model

**Status: IN PROGRESS (z49 round 3, slug `sexp`).** ES is open; nothing here bears on ES existence directly.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / Assessment.

## 0. Summary (to be updated)

* §2: **PROVED modulo the fundamental lemma of sieve theory.**
  * δ(H) ≤ exp(−c L²), the sharp order (Thm 2.1). This improves the L²/(log L)² of the rough-pair route. The method
    conditions on all small-prime coordinates and keeps endpoints with a bounded smooth part. The conditional mass is
    then ≍ L² **uniformly in the small residues**.
  * For the covering coordinate, P(A_min > H) ≤ exp(−c L²/log L) (Thm 2.6).
* §3 (target): the reverse direction δ(H) ≥ exp(−L^{2+o(1)}) via non-adaptive class-of-one conditioning plus a
  β-weighted local lemma, reduced to a pointwise load hypothesis.

## 1. Model, events, and the colour

Logs are natural. H → ∞, L = log H. The **prime-Haar model**: n ranges over the profinite units with the product of
Haar measures, conditioned on n ≡ 1 (mod 24). Coordinates X_ℓ = n mod ℓ^∞ are independent: uniform units for ℓ ≥ 5,
uniform on 1 + 8ℤ₂ for ℓ = 2, and uniform on 1 + 3ℤ₃ for ℓ = 3.

For coprime 1 ≤ a < v ≤ H, the edge event is E_{a,v} = {n ≡ −a−v (mod av)}. The edge is a **certificate** when
(av/n) = −1 (Theorem A). δ(H) = P(no certificate edge with v ≤ H), as in FOREST_H4 Prop 5.1 (prime-Haar,
n ≡ 1 (24)).

**Lemma 1.1 (PROVED; colour is p-independent for odd pairs).** Let a, v be odd and coprime, and let n ≡ 1 (mod 8)
lie in E_{a,v}. Then (av/n) = −1 iff a and v are not both ≡ 1 (mod 4).

*Proof.* (2/n) = 1, and reciprocity for n ≡ 1 (4) gives (av/n) = (n/av) = ((−a−v)/a)((−a−v)/v) = ((−v)/a)((−a)/v).
That equals (−1/a)(−1/v)(v/a)(a/v) = (−1)^{(a−1)/2+(v−1)/2+(a−1)(v−1)/4}. The value is +1 for (1,1) mod 4 and −1 in
the other three cases. ∎

So on n ≡ 1 (24) the certificate events restricted to odd pairs are **a fixed subfamily** of the edge events: no
extra condition on n is imposed, and the 2-adic coordinate drops out entirely.

## 2. Upper bound on survival: δ(H) ≤ exp(−c L²)

**Theorem 2.1 (PROVED modulo the fundamental lemma of sieve theory).** There are absolute c > 0 and H₀ such that for
H ≥ H₀

    −log δ(H) ≥ c (log H)².

The joint survival δ_joint(H) ≤ δ(H) obeys the same bound. The only external input is the fundamental lemma
(Friedlander–Iwaniec, *Opera de Cribro*, Lemma 6.3 / Cor. 6.10), used exactly as in paper/es-subexp-note.tex, Lemma
"Mass": a lower bound for Y-rough numbers in a progression to a small modulus. The combinatorial input is the atomic
Janson inequality, paper/es-subexp-note.tex Theorem "Janson-type inequality for atomic events" (internally proved;
restated in §2.1).

**Comparison.** This improves I3_DEEP_ASTRA Thm 8.4's exponent from L²/(log L)² to L². That theorem is for a
different (interior-word) family, but its rough-pair proof transfers verbatim to certificates by Lemma 1.1 and gives
only L²/(log L)². The (log Y)² loss there comes from roughness. Here it is removed by **conditioning on all small-prime
coordinates** and letting endpoints carry a bounded smooth part. The key point is that the conditional mass is ≍ L²
**uniformly in the small-prime residues**, including the class of one. So no small-prime conditioning (the cheap
escape route of §3) can bring the mass of events with a large rough part below order L².

### 2.1 The atomic Janson inequality (restated)

Let (X_i) be independent coordinates. An atomic event fixes finitely many coordinates to single values. Two events
*conflict* if they prescribe different values on a common coordinate. They *share a bit* if they have a common
coordinate and agree on all common coordinates. Let 𝓕 be a finite indexed family of atomic events, and suppose:

* P(E) ≤ 1/8 for every E;
* Σ_{E' conflicting with E} P(E') ≤ 1/8 for every E.

Then, with μ = Σ P(E) and Δ = Σ_{unordered pairs sharing a bit} P(E∩E'),

    −log P(no E occurs) ≥ μ − e^{1/3} Δ.

The proof (loc. cit.) orders the family and never uses distinctness. An identical pair shares a bit and contributes
P(E) to Δ, so indexed families with repetitions are allowed.

### 2.2 Parameters and the family

Fix Y = L⁹ and S₀ = H^{1/400}. Call s *small* if it is Y-smooth and gcd(s,6) = 1. Call r *rough* if it is squarefree
with all prime factors > Y. The family 𝓕 consists of pairs (u,v) = (s₁r₁, s₂r₂) such that:

* s₁, s₂ ≤ S₀ are small and coprime;
* r₁, r₂ are rough and coprime;
* H^{1/16} ≤ u ≤ H^{1/8}, H^{1/2} ≤ v ≤ H, and u ≡ 3 (mod 4).

Then u, v are odd and coprime with u < v. By Lemma 1.1 every such edge is a certificate, so δ(H) ≤ P(no E_{u,v},
(u,v) ∈ 𝓕). The decomposition u = s₁r₁ is unique (s₁ = Y-smooth part), so 𝓕 is a set of pairs.

### 2.3 Conditioning on the small coordinates

Let z denote the values of all coordinates X_ℓ, ℓ ≤ Y (including 2 and 3). For p > Y split X_p into its first digit
x_p = n mod p, uniform on (ℤ/p)^*, and its independent higher digits. Given z, the event E_{u,v} is

    E_{u,v} ∩ {z} = [z ≡ −u−v (mod s₁s₂)] · {x_p ≡ −u−v (mod p) for all p | r₁r₂}.

Call (u,v) **live at z** if the bracket holds. Equivalently, since z is a unit at every ℓ | s₁s₂,

    r₁ ≡ α := −z·s₁^{−1} (mod s₂),       r₂ ≡ γ := −z·s₂^{−1} (mod s₁).                      (2.1)

For a live pair the conditional event is atomic on the coordinates x_p, p | R := r₁r₂, with probability
P(E | z) = 1/φ(R). Since δ(H) ≤ E_z P(no event | z), it suffices to prove, **uniformly in z**:

    μ(z) ≥ c₁L²,     the Janson hypotheses hold,     Δ(z) = o(1).                           (2.2)

Facts used: (F1) rough R ≤ H² has ω(R) ≤ 2L/log Y, hence φ(R) ≥ R/2 for large H. (F2) For a progression x ≡ c
(mod q), Σ_{x∈[X,2X]} 1/x ≤ 1/q + 1/X, and Σ_{x∈[X₀,X₁]} 1/x ≤ (2 + log(X₁/X₀))/q if X₀ ≥ q. (F3) Σ_{s small} 1/s
≤ C log Y, and #{s ≤ S₀} ≤ S₀.

### 2.4 Mass, uniformly in z

**Lemma 2.2 (PROVED modulo the fundamental lemma).** μ(z) ≥ c₁ L² for every z.

*Proof.* Put V(Y) = ∏_{p≤Y}(1 − 1/p) ≍ 1/log Y.

First, rough numbers in progressions. Let q be Y-smooth with q ≤ 4S₀, c a unit mod q, and X ≥ H^{1/20}. Sift the
progression r ≡ c (q), r ∈ (X, 2X], by the primes p ≤ Y with p ∤ q. Use level Y^s with s = log L, so
Y^s = H^{o(1)}. The fundamental lemma gives at least

    (X/q) ∏_{p≤Y, p∤q}(1−1/p) (1 − o(1)) = (X/φ(q)) V(Y) (1 − o(1))

Y-rough elements, because every prime factor of q is ≤ Y. Multiples of p² with p > Y number at most
2X/(qY) + √(2X) = o(X V(Y)/q), since X/q ≥ H^{1/20−1/400}/4 is much larger than √X. Coprimality to a fixed rough
m ≤ H² removes at most ω(m)(2X/(qY) + 1) = o(X V(Y)/q). So the count of admissible r is at least
(X/(2φ(q)))V(Y).

Now fix small coprime s₁, s₂ ≤ S₀, and impose (2.1) together with the class r₁ ≡ 3s₁^{−1} (mod 4). Then r₁ runs over
a class mod q₁ = 4s₂, through log₂-many dyadic blocks covering [H^{1/16}/s₁, H^{1/8}/s₁]. For each such r₁, r₂ runs
over a class mod s₁ in [H^{1/2}/s₂, H/s₂], coprime to r₁. Partial summation over the blocks gives

    Σ 1/(r₁r₂) ≥ c₂ L² V(Y)² / (φ(s₁)φ(s₂)).

Here φ(q₁) = 2φ(s₂), and the log-lengths of the ranges are L/16 and L/2.

Finally sum over (s₁, s₂), using 1/φ(R) ≥ 1/R:

    Σ_{s₁s₂ = m ≤ S₀, coprime} 1/(s₁s₂) ≥ Σ_{m ≤ S₀, m squarefree small} 2^{ω(m)}/m ≥ ∏_{5≤p≤Y}(1 + 2/p) − T,

with Rankin tail T ≤ S₀^{−1/log Y} ∏_{p≤Y}(1 + 2e/p) = exp(−L/(3600 log L)) (log Y)^{O(1)} = o(1). The product
is ≫ (log Y)², which cancels V(Y)². ∎

### 2.5 The local hypotheses

**Lemma 2.3 (PROVED).** Uniformly in z and in primes p > Y,

    w_p(z) := Σ_{E live at z, p | R_E} P(E|z) ≤ C L²(log Y)²/p + H^{−1/30}.

Consequently every live E has P(E|z) ≤ 2H^{−1/2} and Σ_{E' conflicting with E} P(E'|z) ≤ Σ_{p|R_E} w_p(z)
= O(L³ log Y/Y) = o(1). So the hypotheses of §2.1 hold for large H.

*Proof.* Use P ≤ 2/(r₁r₂) by (F1).

Case p | r₁, r₁ = px with x ≡ class (mod s₂) by (2.1). The r₂-sum is over a class mod s₁ starting at H^{1/2}/S₀ ≥
s₁, so by (F2) it is ≤ (2+L)/s₁.

* If p ≤ H^{1/16}/S₀², then x ≥ S₀ ≥ s₂ and the x-sum is ≤ (2+L)/s₂. Summing over s₁, s₂ with (F3) gives
  ≤ 2(2+L)²(C log Y)²/p.
* If p > H^{1/16}/S₀², bound the x-sum by 1 + L and sum s₂ trivially (≤ S₀ terms). This gives
  ≤ 2(1+L)(2+L) C log Y · S₀ / p ≤ H^{−1/16+3/400}.

Case p | r₂ is the same with the roles swapped. The r₁-range starts at H^{1/16}/S₀ ≥ s₂. The threshold is
p ≤ H^{1/2}/S₀². ∎

### 2.6 The pair sum

**Lemma 2.4 (PROVED).** Δ(z) ≪ L⁴(log Y)⁴/Y + L⁸ H^{−1/16+6/400} = o(1), uniformly in z.

*Proof.* Let E = (u,v), E' = (u',v') be distinct live pairs sharing a bit. Label them so that v' ≥ v. Put

    g = (r₁,r₁'),  h = (r₂,r₂'),  j = (r₁,r₂'),  k = (r₂,r₁'),  D = ghjk > 1.

By squarefreeness and r₁ ⊥ r₂, r₁' ⊥ r₂', these are pairwise coprime. Write

    r₁ = gja,  r₂ = hkb,  r₁' = gkc,  r₂' = hjd,

so that lcm(R,R') = D·abcd and P(E∩E'|z) ≤ 2/(D·abcd).

*Shared modulus.* Compatibility means D | (u+v) − (u'+v').

* If the sums differ, D ≤ 2v' + 2H^{1/8} ≤ 4V', where v' ∈ [V', 2V'].
* If the sums agree, then u ≠ u' (else E = E'). h divides both v and v', so h divides v−v' = u'−u, and
  h ≤ H^{1/8}. Also gjk ≤ uu' ≤ H^{1/4}. Hence D ≤ H^{3/8} ≤ V'.

This is the separated-endpoint argument of I3 §8.4.

*Congruences.* Liveness (2.1) puts a in one class mod s₂, b mod s₁, c mod s₂', d mod s₁'. Agreement at the primes
of D adds:

* v ≡ v' (mod g), and u ≡ v' (mod k): given a, b, these put d in one class mod gk;
* u ≡ u' (mod h), and v ≡ u' (mod j): these put c in one class mod hj.

By CRT, c lies in one class mod hj·s₂' and d in one class mod gk·s₁'.

*Summation.* Fix dyadic boxes u ∈ [U,2U], etc. (O(L⁴) boxes), the four small parts, and (g,h,j,k). By (F2):

* the a-sum is ≤ 1/s₂ + s₁gj/U, and the b-sum is ≤ 1/s₁ + s₂hk/V;
* the c-sum is ≤ 1/(hjs₂') + s₁'gk/U', and the d-sum is ≤ 1/(gks₁') + s₂'hj/V'.

The product of the c- and d-sums is ≤ 1/(D s₁'s₂') + 1/U' + 1/V' + s₁'s₂'D/(U'V'). Since D ≤ 4V', this is
≤ 1/(Ds₁'s₂') + ε with ε = 12S₀²H^{−1/16}.

The product of the a- and b-sums is 1/(s₁s₂) + hk/V + gj/U + s₁s₂D/(UV). This is ≤ 9, using gj ≤ 2U/s₁ and
hk ≤ 2V/s₂. Its last three terms, multiplied by 1/D, are ≤ 1/V + 1/U + S₀²/(UV) ≤ 3S₀²H^{−1/16}, because
hk, gj ≤ D. So the configuration contributes at most

    2/(D² s₁s₂s₁'s₂') + 6S₀²H^{−1/16}/(D s₁'s₂') + 18ε/D.

Sum over the small parts, and over the at most 4^{ω(D)} quadruples with product D. The main term is

    Σ_D (2·4^{ω(D)}/D²) (C log Y)⁴ ≪ (log Y)⁴/Y,

using Σ_{D>1 rough} 4^{ω(D)}/D² ≤ exp(Σ_{p>Y}4/p²) − 1 ≪ 1/Y. The remaining terms are

    ≪ S₀⁴(H^{−1/16} + ε) Σ_{D≤4H} 4^{ω(D)}/D ≪ L⁴ S₀⁶ H^{−1/16}.

Multiply by the O(L⁴) boxes. ∎

### 2.7 Proof of Theorem 2.1

For every z, §2.1 together with Lemmas 2.2–2.4 gives

    −log P(no event of 𝓕 | z) ≥ c₁L² − e^{1/3}·o(1).

Average over z. ∎

**Remarks (Assessment).**

1. *Why conditioning beats roughness.* Fix the small coordinates, even to the class of one. For each pair of
   smooth parts (s₁,s₂), the liveness constraint (2.1) is a single class for (r₁ mod s₂, r₂ mod s₁). It removes
   exactly a 1/(φ(s₁)φ(s₂)) share of the rough mass. Summing over s restores the factor (log Y)² that roughness
   costs. Bounding s ≤ S₀ = H^{1/400} keeps the rough parts long compared with the moduli, so no first-term
   effects occur.
2. *The 2-adic coordinate.* It never enters: the family uses odd endpoints and gcd(s,6) = 1, and Lemma 1.1 makes
   the colour a property of (u mod 4, v mod 4) once n ≡ 1 (mod 8).
3. *Constant.* The proof gives an unspecified c, far below the empirical 0.32 (§4). It uses only a separated
   sub-box of log-area L²/32 and a quarter of the colour classes.
4. *Why the upper bound on δ is easy but the lower bound is not.* Janson needs only that the conditional mass is
   ≍ L² for every z. A lower bound on δ has to exhibit one z of probability exp(−L^{2+o(1)}) whose conditional
   system satisfies a local lemma **pointwise in every large prime** (§3).

### 2.8 The covering coordinate A_min

Use the H4_NOT_POLYLOG definitions:

    G_A = {−d mod A : d | A+1, d < A, (−d/A_odd) = −1},     A_min(p) = min{A : p mod A ∈ G_A}.

The event is C_{A,d} = {n ≡ −d (mod A)}.

**Lemma 2.5 (PROVED).** Let A ≡ 3 (mod 4), let d be odd, and let d | A+1. Then (−d/A) = −1.

*Proof.*

* (−1/A) = −1.
* (d/A) = (A/d)(−1)^{(d−1)(A−1)/4} = (A/d)(−1)^{(d−1)/2}, since (A−1)/2 is odd.
* (A/d) = (−1/d) = (−1)^{(d−1)/2}, since A ≡ −1 (mod d).

The product is −1. ∎

**Theorem 2.6 (PROVED modulo the fundamental lemma).** In the prime-Haar model,

    −log P(A_min > H) ≥ c L²/log L.

*Proof.* Take Y = L⁹ and N₀ = L². The family consists of the pairs (A,d) with:

* A squarefree and Y-rough, H^{1/2} ≤ A ≤ H, A ≡ 3 (mod 4);
* d odd, N₀ ≤ d ≤ H^{1/10}, d | A+1.

By Lemma 2.5 each −d mod A lies in G_A. The events are atomic on x_p (p | A), with P = 1/φ(A). They are pairwise
distinct because d < A/2, and they are independent of n mod 24. Here **d need not be rough**, so only one factor
log Y is lost.

*Mass.* By the fundamental lemma in the class A ≡ −1 (mod 4d), one gets Σ_A 1/A ≥ c L V(Y)/d. Hence
μ ≥ c L² V(Y) ≫ L²/log L.

*Loads.* Write A = px with x in a class mod d.

* If p ≤ H^{0.4}, then x ≥ H^{1/10} ≥ d, so (F2) gives w_p ≤ (2/p)(2+L)Σ_d 1/d ≪ L²/p.
* If p > H^{0.4}, then w_p ≤ (2/p)(1+L)H^{1/10} ≤ H^{−0.29}.

The conflict sum is ≤ (L/log Y)(CL²/Y + H^{−0.29}) = o(1).

*Pair sum.* Write g = (A,A') > 1, A = gv, A' = gv'. Compatibility means g | d − d'. P(C∩C') ≤ 2/(gvv').

* **(a) d = d'.** Here v ≡ v' ≡ −g^{−1} (mod d) and v ≠ v'. Orient v < v', so v' ≥ v + d ≥ d. For fixed (v,d)
  the variable g runs over one class mod d with g > Y. Hence

      Δ_a ≤ Σ_d 2[1/Y + (1+L)/d](1+L)(2+L)/d ≪ L³/Y + L³/N₀ = O(L).

  This is the hub term. The cutoff d ≥ N₀ is exactly the device of paper/es-subexp-note.tex Lemma "Pair sum"(a).
* **(b) d ≠ d'.** Here Y < g ≤ H^{1/10}, so v ≥ H^{0.4} ≥ d, and the v- and v'-sums are ≤ (2+L)/d and (2+L)/d'.
  Orient d' > d, so d' ≥ d+g ≥ g. Then Σ_{d'≡d (g)} 1/d' ≤ (2+L)/g, and Δ_b ≪ L⁴ Σ_{g>Y} 1/g² ≪ L⁴/Y.

Thus μ − e^{1/3}Δ ≥ cL²/log L − O(L). ∎

**Assessment (the gap for A_min).** The z-conditioning of §2.3 would remove the remaining log L. It does not go
through as written because of the same-d hubs. With A = sGy and A' = s'Gy', the pairs C, C' with d = d' have no
saving in the larger smooth part s'. A crude bound gives Δ ≫ S₀·L²/Y. Only the edge family has this solved, because
the two endpoints carry independent congruences. Since δ_joint ≤ min(δ(H), P(A_min > H)), Theorem 2.1 already gives
the joint bound with exponent L².

### 2.9 Checks for §2 (CERTIFIED finite checks / EVIDENCE)

The independent scripts are `scripts/z49_sexp_janson_check.py` and `scripts/z49_sexp_muz.c`. Their output is in
`data/z49_sexp/janson_check.txt` and `muz.txt`.

* **CERTIFIED:**
  * Lemma 1.1 against the five-slot test and against Legendre colours: all 16,751 odd edges with v ≤ 2000 at primes
    p ≡ 1 (24) below 2·10⁵, with 0 failures (`colour_check.txt`).
  * (F2): 40,000 brute-force progression sums, 0 violations.
  * Lemma 2.5: 291,689 instances (A,d) with A ≤ 200,001, 0 failures (`cover_colour.txt`, script
    `z49_sexp_cover_colour.py`).
  * The (g,h,j,k) decomposition: pairwise coprimality, lcm(R,R') = D·abcd, compatibility ⇒ D | sum difference, and
    the equal-sum bound. 5,506 configurations, 0 violations.
  * Liveness and atomicity: exact CRT enumeration of P(E | z) = [live]/φ(R) on 3,200 (pair, z) instances, with
    small primes {2,3,5} and rough primes {7,11,13,17}, 0 violations.
* **EVIDENCE (scaled parameters):** small primes 5–13, S₀ = 200, u ∈ [100,1500], v ∈ [2·10⁴, 2·10⁶].
  * The conditional mass μ(z) is within ±4% of its z-average 0.7035 for the class of one and for 11 random z.
    The class of one gives ratio 0.989.
  * max_p p·w_p(z) stays in 5.3–9.7.
  * This is the uniformity mechanism of Lemma 2.2/2.3. The asymptotic parameters (Y = L⁹, S₀ = H^{1/400}) cannot be
    reached numerically.

## 3. Lower bound on survival — see below

## 4. Reality check against the simulation — see below
