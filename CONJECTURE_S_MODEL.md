# CONJECTURE_S_MODEL — bracketing certificate survival in the prime-Haar model

**Status: PARTIAL (z49 round 3, slug `sexp`).** Conjecture S is PROVED on the upper side; on the lower side it is CONDITIONAL. ES is open; nothing here bears on ES existence directly.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / Assessment.

## 0. Summary

Write L = log H. δ(H) is the prime-Haar certificate survival, n ≡ 1 (24) (FOREST_H4 Prop 5.1).

| statement | label |
|---|---|
| −log δ(H) ≥ c L² (Thm 2.1) | **PROVED** modulo the fundamental lemma; uses the internally proved atomic Janson inequality |
| −log P(A_min > H) ≥ c L²/log L (Thm 2.6) | **PROVED** modulo the fundamental lemma |
| −log δ(H) ≤ C L³(log L)^C (Thm 3.4) | **CONDITIONAL** on the first-term hypothesis FT (§3.4) |
| −log δ(H) ≤ C L²(log L)^C (Thm 3.5), hence **Conjecture S in the model** | **CONDITIONAL** on FT_β (§3.6) |
| −log δ(H) ≤ C L⁶ log L | unconditional status quo (H4_NOT_POLYLOG), unchanged |
| H₄(p) > exp((log p)^κ) i.o. for κ < 1/3 (Cor 5.1) | **CONDITIONAL** on FT, relative to (G) and the internal energy lemma; this route cannot exceed 1/3 |
| −ln δ ≈ 0.64·E N_H, with E N_H ≍ L² (§4) | **EVIDENCE** |

**New ideas.**

* **Upper bound.** Condition on *all* small-prime coordinates, and allow endpoints with a bounded smooth part. The
  conditional mass of rough-supported certificate events is ≍ L² **uniformly in the small residues**, including
  the class of one. So no small-prime conditioning can buy survival cheaply, and Janson applies fibrewise. This
  removes the (log L)² roughness loss of the I3 §8.4 route.
* **Colour.** For n ≡ 1 (8), an odd pair is a certificate iff its endpoints are not both ≡ 1 (4) (Lemma 1.1). The
  2-adic coordinate drops out.
* **Lower bound.** A *non-adaptive* class of one Q(Y) = ∏_{ℓ≤Y} ℓ^{k_ℓ}, with every free modulus ≥ Y, costs ≈ Y
  instead of ℒ²S♯. The residual mass is PROVED ≪ L² polylog. Loads from the smaller endpoint are PROVED pointwise via
  Shiu's theorem.

**Consequence for actual primes (PROVED).** For each fixed large H, the density of primes p ≡ 1 (24) with
H₄(p) > H is ≤ exp(−c(log H)²). This replaces the (log H)^{−1/2} of FOREST_H4 Thm 3.5. It says nothing about H
growing with p.

**Exact remaining gap.** FT is a pointwise-in-ℓ first-term bound on the larger-endpoint loads. In its hardest
instance it is the equidistribution mod ℓ of A − (B^{−1} mod A) over smooth A, B. It is numerically comfortable:
the non-adaptive LLL certificate holds at H = 10⁵ with Y ≈ L³. It is unproved. FT_β additionally needs shifted
multiplicative weights β^{ω(v)}.

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

## 3. Lower bound on survival: non-adaptive class of one

The aim is to replace the adaptive quarantine of H4_NOT_POLYLOG Lemma 4, with its cost log Q ≪ ℒ²S♯ and S♯ ≍ L³–L⁴,
by a **fixed** class of one whose cost is ≈ Y. Large primes are never conditioned, so the only inflation is
Y-smooth. The price is that the local lemma must hold **pointwise** at every free coordinate.

### 3.1 The conditioning and its exact probabilities

For Y ≥ 9 and each prime ℓ ≤ Y, let ℓ^{k_ℓ} be the largest power of ℓ below Y. Raise k₂ to at least 3 and k₃ to at
least 1. Put

    Q = Q(Y) = ∏_{ℓ≤Y} ℓ^{k_ℓ},       log Q ≤ π(Y) log Y + 3 = (1+o(1)) Y.

Condition on n ≡ 1 (mod Q). This costs φ(24)/φ(Q) relative to n ≡ 1 (24). The free coordinates c are:

* X_ℓ for each prime ℓ > Y, with modulus m_c = ℓ;
* for each ℓ ≤ Y, the block of digits of n beyond ℓ^{k_ℓ}, with modulus m_c = ℓ^{k_ℓ+1} ≥ Y.

So every free coordinate has m_c ≥ Y.

**Lemma 3.1 (PROVED; exact form).** Let a < v be coprime, and write A = gcd(a,Q), B = gcd(v,Q), and
φ_Q(m) := φ(m)/φ(gcd(m,Q)).

* E_{a,v} is compatible with n ≡ 1 (Q) iff A | v+1 and B | a+1 ("live").
* If live, P_Q(E_{a,v}) = 1/(φ_Q(a)φ_Q(v)) ≤ (C log L)² AB/(av).
* Its support is the set of coordinates c with m_c | av, which is nonempty unless (a,v) ∈ {(1,2),(2,3)}. These two
  edges are not certificates.

*Proof.* By CRT, n ≡ −a (mod v) and n ≡ −v (mod a) are independent. Given n ≡ 1 (mod B), the first holds with
conditional probability [B | a+1]·φ(B)/φ(v), and similarly for the second. Use m/φ(m) ≪ log log m. The last claim
is H4_NOT_POLYLOG Lemma 2, since an empty support means av | Q and av | 1+a+v. ∎

### 3.2 Residual mass (PROVED)

**Lemma 3.2.** S(Y) := Σ_{live E} P_Q(E) ≪ (log L)² L² log Y.

*Proof.* This is the I3 Lemma 8.2 argument. Fix a. For each B | gcd(a+1, Q), the live v satisfy v ≡ 0 (B) and
v ≡ −1 (A). That is one class mod m = AB, and m | a+v+1.

The first member v_* > a therefore satisfies m ≤ a + v_* + 1 ≤ 2v_*. So

    m Σ_v 1/v ≤ m/v_* + log(H/a) ≤ 2 + L.

Hence Σ_v AB/(av) ≤ (2+L)τ_Q(a+1)/a, where τ_Q(n) := #{d | n : d | Q}. Finally

    Σ_{a≤H} τ_Q(a+1)/a ≤ Σ_{B Y-smooth} Σ_{a≡−1 (B)} 1/a ≪ L log Y,

since a ≡ −1 (B) forces a ≥ B−1. ∎

### 3.3 Loads from the smaller endpoint (PROVED relative to Shiu's theorem)

For a coordinate c with modulus q = m_c, write w_c = w_c^{(a)} + w_c^{(v)}. The first part sums P_Q(E) over live E
with q | a. The second sums over live E with q | v.

**Lemma 3.3.** Uniformly in c,

    w_c^{(a)} ≪ (log L)² L² log Y / q + q^{−1/2}.

*Proof.* Write a = qx. The argument of Lemma 3.2 (sum over v first) gives

    w_c^{(a)} ≤ (C log L)² (2+L) q^{−1} T(q),       T(q) := Σ_{x≤H/q} τ_Q(qx+1)/x.

Apply Shiu's Brun–Titchmarsh theorem for multiplicative functions (P. Shiu, *J. reine angew. Math.* 313 (1980),
161–170, Theorem 1) to F = τ_Q. This F satisfies F(p^j) ≤ j+1 and F(n) ≪_ε n^ε, with F(p) = 2 for p ≤ Y and 1
otherwise. The implied constant depends only on these bounds.

On n ≡ 1 (mod q), with n in dyadic blocks (qX'/2, qX'+1] and X' > 2q, Shiu gives

    Σ τ_Q(n) ≪ (X'q/φ(q))(log x)^{−1} exp(Σ_{p≤x} F(p)/p) ≪ X'(log Y)²(log x/log Y)/log x = X' log Y.

Blocks with X' ≤ 2q have n ≤ 2q²+1 and contribute ≪_ε q^{3ε}. If q > √H, every x is in such a block, and
τ_Q(n) ≪ H^ε ≤ q^{2ε}. Combine. ∎

### 3.4 Loads from the larger endpoint: the one unproved input

The same calculation for q | v sums first over v with a fixed. Now v ≡ 0 (mod lcm(B,q)) and v ≡ −1 (A). In terms
of s = a+v+1 this is s ≡ 0 (AB) and s ≡ a+1 (lcm(B,q)), a class modulo AB·p_c, where p_c is the prime of c. When
q = ℓ^{k+1} is a prime power, also ℓ^k | B | a+1. The harmonic sum over this class splits into two parts.

* The **long part** is ≪ L/(ABp_c) times AB. Summed over a and B it gives ≪ (log L)² L² log Y/q. For prime powers
  this uses Σ_{a ≡ −1 (ℓ^k)} τ_Q(a+1)/a ≪ k L log Y/ℓ^k.
* The **first term** is AB/s_*, where s_* = s_*(a,B;q) is the least s in the class with s ≥ a+q+1.

So, PROVED,

    w_c^{(v)} ≪ (log L)² [L² log Y/q + FT(q)],      FT(q) := Σ_{a≤H} a^{−1} Σ_{B | gcd(a+1,Q)} AB/s_*(a,B;q).

**Hypothesis FT(Y).** For every free coordinate c of Q(Y), with q = m_c,

    FT(q) ≤ L² (log L)^{C₀}/q + q^{−1/2}.

*What FT says.* For fixed (a,B), the class of s modulo p_c is determined by a, B and q. The term AB/s_* is large only
when that class happens to have a small representative above the cutoff. FT asserts that this coincidence is rare
**at every single prime**. It is an equidistribution statement for the residues (a+1)(AB)^{−1} mod ℓ, pointwise in
ℓ. This is the same "first-term" obstruction as in POINTWISE_OMEGA11 §4 and the LPL hypothesis of
POINTWISE_OMEGA13 §1, now in its simplest instance.

The known extreme case is benign. The events (d, ℓ) with d | ℓ+1 and d smooth contribute τ_Q(ℓ+1)/(ℓ−1), which is
ℓ^{−1+o(1)}. This is exactly what the data show at ℓ = 5039, 10079, 55439, 92399 (§3.7). FT allows such terms.

### 3.5 Exponent 3 + o(1) from FT

**Theorem 3.4 (CONDITIONAL on FT(Y) with Y = L³(log L)^{C}, C = C(C₀)).**

    −log δ(H) ≤ C' L³ (log L)^{C}.

*Proof.* Take x_E = 2P_Q(E) in the asymmetric local lemma, with the dependency graph "shares a free coordinate".

Lemmas 3.3–3.4 and FT give w_c ≤ log m_c/(16L) for every coordinate, since m_c ≥ Y. Every live E has
Σ_{c∈supp E} log m_c ≤ log(av) ≤ 2L. Hence the neighbourhood x-mass is ≤ Σ_{c∈supp E} 2w_c ≤ 1/4. Each x_E ≤ 1/4,
so ∏_{E'∼E}(1−x_{E'}) ≥ e^{−1/3} > 1/2 and P(E) ≤ x_E∏(1−x_{E'}).

The asymmetric LLL, as in the last paragraph of H4_NOT_POLYLOG Lemma 4, gives

    P(no event | Q) ≥ exp(−3S(Y)).

Then

    −log δ(H) ≤ log φ(Q) − log 8 + 3S(Y) ≤ (1+o(1))Y + O((log L)² L² log L).

Since all edges are avoided, all certificates are avoided. ∎

This improves the exponent 6 of H4_NOT_POLYLOG (19), and of I3 Thm 8.3, to 3. It is conditional only on FT. The
remaining extra L comes from the log-weighted threshold, which forces m_c ≳ L·(load·m_c) ≈ L³.

### 3.6 Exponent 2 + o(1): what the β-weighted local lemma needs

POINTWISE_OMEGA13 Lemma 1.1 replaces the log-weighted threshold by a constant per-coordinate threshold
η = (3/4)log β. The weights are x_E = β^{s(E)}P(E), with s(E) = |supp E| and β = 1 + 1/log L, so η ≍ 1/log L. A
coordinate then only needs w̃_c := Σ_{E∋c} β^{s(E)}P_Q(E) ≤ η. Under a load bound of the shape of Lemma 3.3, this
holds once m_c ≥ L²(log L)^{C}.

**Hypothesis FT_β(Y).** For Y = L²(log L)^{C}:

* w̃_c ≤ L²(log L)^{C₀}/m_c + m_c^{−1/2} for every free coordinate c;
* S_β(Y) := Σ_E β^{s(E)}P_Q(E) ≤ L²(log L)^{C₀}.

**Theorem 3.5 (CONDITIONAL on FT_β(Y)).**

    −log δ(H) ≤ log φ(Q) + (4/3)S_β(Y) ≤ C L²(log L)^{C}.

Together with Theorem 2.1, this gives −log δ(H) = L^{2+o(1)}. That is **Conjecture S in the prime-Haar model,
CONDITIONAL on FT_β**.

*Why FT_β is more than FT.* The weight β^{s(E)} factors as β^{ω(a'')}β^{ω(v'')} over the free parts. In Lemmas
3.2–3.3 the variable summed through s = a+v+1 is v. A multiplicative weight on v then appears at a shifted argument
β^{ω(s−a−1)}, and its pointwise size can be exp(L/(log L)²). On average it costs only e^{O(1)}, since
Σ_n β^{ω(n)}/n ≈ L^{β}. A proof would need a Shiu/Nair–Tenenbaum bound for the pair (n, n−a−1) in a progression,
uniform in the shift. That is standard in form but not supplied here, so S_β is included in the hypothesis.

### 3.7 Evidence for FT and FT_β (EVIDENCE, finite H)

`scripts/z49_sexp_loads.c` uses full class-of-one powers; `scripts/z49_sexp_lllcheck.c` uses the exact Q(Y) of
§3.1. Both enumerate **all** live coprime edges with v ≤ H, which is an upper bound for the certificate subfamily.
Output is in `data/z49_sexp/loads.txt` and `lllcheck.txt`.

* **Loads.** Uniformly over all primes ℓ > Y, and over the residual-digit coordinates:
  * max_c m_c·w_c^{(a)}/L² ≤ 0.23;
  * max_c m_c·w_c^{(v)}/L² ≤ 1.11.

  The v-side maxima sit at ℓ with ℓ+1 highly composite (18899, 65519, 92399). These are the benign τ(ℓ+1) terms of
  §3.4. Dyadic bulk values of ℓ·V(ℓ) are flat in ℓ, at ≈ 0.9–1.6 L².
* **Non-adaptive LLL verified at finite H.** At H = 10⁵ and Y = 1500 (≈ L³), max_E Σ_{c∈supp E} 2w_c = 0.239 ≤ 1/4,
  with log Q = 1509 and S = 19.6. That is a finite instance of Theorem 3.4's local-lemma condition, holding for
  every live event. At Y = 600 (≈ 4.5L²), the β-weighted per-coordinate condition holds:
  max_c w̃_c = 0.219 ≤ η = 0.257, with S_β = 40.5. At Y ≈ L² (130) both fail (5.05 and 1.20). This matches the
  predicted thresholds Y ≍ L³ and Y ≍ L²·polylog.
* **Mass.** S(Y)/L² ≈ 0.15–0.33, decreasing in Y. This is consistent with Lemma 3.2 (the log Y factor is an upper
  bound; heavier conditioning removes events).

**Assessment.** At these sizes every hypothesis is numerically comfortable. FT is an arithmetic equidistribution
statement of a kind that is usually true, but it is not proved here, and pointwise-in-ℓ bounds of this type have
resisted earlier waves (OMEGA11 §4, OMEGA13 LPL). The **unconditional** lower bound remains H4_NOT_POLYLOG's
exp(−C L⁶ log L), or exp(−C L⁶/log L) with the I3 §8.3 refinement.

## 4. Reality check against the simulation

The parent's 10⁹-sample run (`data/z49_main/h4_crt_survival.txt`) measures P(H₄ ≥ X) = δ(X−1). The table below
puts it next to the exact model first moment E N_H. `scripts/z49_sexp_firstmoment.c` computes E N_H with the
Jacobi rule (`data/z49_sexp/firstmoment.txt`). It reproduces FOREST_H4's exact-CRT values at H = 8 and 16
(1.208333, 2.723611), which were obtained by an independent slot-test enumeration.

| H = X−1 | −ln δ(H) (sim.) | E N_H (exact) | −ln δ / E N_H | −ln δ/(ln H)² |
|---:|---:|---:|---:|---:|
| 15 | 2.00 | 2.640 | 0.76 | 0.27 |
| 31 | 3.54 | 4.840 | 0.73 | 0.30 |
| 63 | 5.06 | 7.657 | 0.66 | 0.29 |
| 127 | 7.14 | 10.901 | 0.655 | 0.30 |
| 255 | 9.52 | 14.769 | 0.645 | 0.31 |
| 511 | 12.30 | 19.147 | 0.642 | 0.32 |
| 1023 | 15.42 | 24.089 | 0.640 | 0.32 |

**EVIDENCE / Assessment.**

1. The survival exponent tracks the first moment with a **stable ratio ≈ 0.64**, and E N_H/(ln H)² rises slowly
   (0.36 → 0.52 by H = 16383). This is the picture −log δ ≍ E N_H ≍ L² that Theorems 2.1 and 3.5 bracket. It is
   "sub-Poisson" by a constant factor: positive dependence between events sharing small primes makes survival
   e^{0.36 μ} times likelier than independence would.
2. The proven constant in Theorem 2.1 is far smaller than 0.64 E N_H. Only a separated sub-box is used. Within it
   the Janson bound is asymptotically Poisson (Δ = o(1)). So the true loss is the restriction to the box, not
   dependence.
3. The conditional upper bounds of §3 are wasteful by large constants and polylogs. At H = 10⁵ the finite LLL
   certificate of §3.7 gives −ln δ ≤ 1509 + 3·19.6 ≈ 1568, while extrapolation gives ≈ 42. The class of one is a
   costly survival strategy. Typical survivors do not condition at all; they are the sub-Poisson fluctuation of
   item 1.
4. The local exponent 2.2 of ln X in the simulation is compatible with L² times a slowly varying factor, e.g. the
   rising E N_H/L². It does not suggest exponent 3.

**What the model does and does not say about actual primes (Assessment).**

* PROVED (FOREST_H4 Prop 5.1): for each fixed H, δ(H) is the exact density of primes p ≡ 1 (24) with no
  certificate edge below H. Theorem 2.1 is therefore a statement about actual primes: for every fixed large H,
  the density of primes with H₄(p) > H is ≤ exp(−c log²H).
* What does **not** follow is any statement with H growing with p. That is a uniformity question about primes in
  progressions to modulus ≈ e^{O(H)}. The transfer of lower bounds needs the energy/BRW machinery (§5). Upper
  bounds on the frequency of large H₄ at growing H would need an upper-bound sieve for the class of p modulo
  lcm(1..H). That is far beyond present technology at the needed uniformity.
* The predicted extreme law, log max_{p≤x} H₄(p) ≍ (log x)^{1/2}, needs both directions uniformly in H ≈
  exp((log x)^{1/2}). Even a full proof of Conjecture S in the model would not prove it.

## 5. Transfer to primes (stretch goal)

H4_NOT_POLYLOG Lemmas 5–7b turn a Haar lower bound into primes p ≡ 1 (mod Q) avoiding all events. The input is a
graded-LLL output (Q, S) with:

* log Q ≪ the Haar exponent;
* coordinate loads ≤ c = 1/64;
* 840 | Q.

The cost is log p ≪ log Q + log D + log T (Lemma 7b, relative to (G)), with log D + log(2+K) ≪ ℒ(S+ℒ) (Lemma 5).

**Corollary 5.1 (CONDITIONAL on FT(Y), Y = L³(log L)^C; relative to (G) and the internal energy lemma, as in
H4_NOT_POLYLOG).** For every κ < 1/3 there are infinitely many primes p ≡ 1 (mod 840) with no edge
{a,v} ≠ {1,2},{2,3} with 4 ≤ v ≤ exp((log p)^κ). In particular H₄(p) > exp((log p)^κ). Via the ordinary-PNT
route (Lemma 7) the exponent is κ < 1/6. Under GRH it is κ < 1/3 without (G).

*Proof sketch, interface check.*

* Use Q = Q(Y) of §3.1. It is divisible by 840, since Y > 7.
* Shrink the constant in FT/Lemma 3.3 so that Σ_{c∈supp E} w_c ≤ 1/64 for every E. Then (7) of H4_NOT_POLYLOG
  holds, with the coordinates c in place of its digits. Coordinates are again independent prime-power digit blocks.
  The energy lemma is prime-agnostic and needs absolute moduli m_c, which is what Q(Y) provides.
* Lemma 4's conclusions (8)–(9) follow verbatim from the LLL.
* Lemma 6 needs w_{ℓ₀} ≤ c at a free odd prime ℓ₀ ∤ Q, which is again the coordinate bound.
* Then log Q ≈ Y ≈ L³ polylog and S ≪ L² polylog. Lemma 5 gives log D + log K ≪ ℒ(S+ℒ) ≈ L³ polylog. Lemma 7b
  gives log p ≪ L³ polylog, i.e. H = exp((log p)^{1/3−o(1)}). Lemma 7 squares this.

The A_min half of H4_NOT_POLYLOG Theorem 1 is not covered: §3 treats only the edge family.

**Assessment: the transfer cannot reach 1/2 by this route even if FT_β holds.** Under FT_β, log Q and S drop to
L^{2+o(1)}. But the BRW/energy minorant still costs log D ≈ ℒ·S ≈ L³, the junta term. So κ → 1/3 is the ceiling of
the present transfer. This is the same bottleneck as POINTWISE_OMEGA13 Prop 1.3(b). Reaching the heuristic 1/2 needs
a junta/minorant whose degree is ≪ S rather than ℒ·S.

