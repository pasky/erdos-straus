# OAI_METHOD_142 — the derandomisation in OpenAI family 142, and whether it can construct an ES witness

*Wave z48, slug `oai142`, 2026-10-28. **ES is not solved here or anywhere.** Labels as in `DISCOVERIES.md`: PROVED /
CONDITIONAL (on what) / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Everything attributed to 142, 029 or 003 is
**CLAIMED (OpenAI release, unrefereed)**; 142 and 029 have no located Lean formalisation (`OAI_DUMP_IMPACT.md` §1.1).
Script `scripts/z48_oai142_dictionary.py`; output `data/z48_oai142/summary.txt`.*

**Verdict: NEGATIVE, clean.** 142 removes randomness in two ways. (a) It finds **auxiliary primes** ℓ whose Frobenius
in an explicit Kummer field K(p^{1/q})/K, K = ℚ(μ_{12q}), is non-trivial. This is a positive-density Chebotarev event,
and a uniform Hecke zero-free strip (029 Thm 1.2) forces it below poly(n log p). (b) It then uses **algebraic forced
separation**: a tournament count for an even number of roots, and a λ-adic lattice valuation on superelliptic
Jacobians for an odd number. That second step detects an object, a factorisation, that exists a priori.

For ES, the analogous candidate set is the primes ℓ = 4uC − 1 with success ℓ | p + u. It transfers only through its
**bounded-index layers**. Index-m Frobenius information at ℓ proves the m-th-power-numerator relaxation
4/p = g^m/(uBC) + 1/(pBC) + 1/(puC) (Prop 2.1). At prime (★) moduli the only layer that cannot be avoided by choosing
the candidate is index 2, the quadratic/BM layer, which is already free. Odd-index layers exist, but they are
avoidable: pick ℓ with gcd(m, ℓ−1) = 1. Cap 0 needs index ℓ^{1−o(1)} at the certified prime ℓ. The standard
explicit-formula calculus certifies index only up to about ℓ^{δ/2}, which is ℓ^{1/4} under GRH (§2.3, Assessment). That missing step
is exactly B2, in the form already isolated in `FROBENIUS_FIRING.md` Remark 2.5. 142's algebraic forcing has no ES
analogue, because ES has no a-priori object whose existence is guaranteed (§2.4). The A5 converse closes only up to that
same layer: ES → QNR → square-numerator ES, with the class inside the BM coset lost (§3).

**Promise for an ES route: 0/5.** As documentation, the 142 anatomy and the index dictionary rate 1/5. They tell a
reader exactly why "deterministic polynomial factorisation / QNR in P" does not move ES.

---

## 1. What 142 does (CLAIMED; source `preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/build/sections/`)

### 1.1 Statement and architecture

**Thm 1.1 (00-introduction.tex).** There is a uniform deterministic algorithm that factors a dense f ∈ 𝔽_p[x] of degree n
completely in O(((n+1)⌈log₂p⌉)^{10¹²}) bit operations, with no randomness, no factoring oracle and no GRH.

**Thm 1.2 (reduction).** Put B = 20 + (n+1)(L+1). For p > B^{200000}, given for each prime q ≤ n one **auxiliary prime**

  ℓ_q ∉ {2, 3, p, q},  ℓ_q ≡ 1 (mod 12q),  p^{(ℓ_q−1)/q} ≢ 1 (mod ℓ_q)   [p is not a q-th power mod ℓ_q],

the factorisation is computed in O((B + max ℓ_q)^C) bit operations. This step is unconditional and purely algebraic.
The only analytic input is §10, which shows ℓ_q ≤ c₀B^{2·10⁷}. Small p ≤ B^{200000} is handled by brute force, which is
polynomial there.

### 1.2 What replaces each random choice

| randomised step (Berlekamp / Cantor–Zassenhaus) | 142's deterministic replacement | input that forces success |
|---|---|---|
| random a: gcd(F, (T−a)^{(p−1)/2} − 1) splits F | **auxiliary prime ℓ_q** found by upward search | Chebotarev in M = K(p^{1/q})/K with uniform strip (§1.3) |
| a random QNR / random element of the q-primary part | **Gaussian-period field** U_q = 𝔽_p[T]/(Φ_ℓ)^{H_q} (H_q = q-th powers mod ℓ). It is a field of degree q *because* Frob_p acts on (ℤ/ℓ)^*/H_q by the non-trivial class of p (01-table.tex, Lemma table:degreeq). Eigenvector equations u^{Q} = ζ_q u then give **q-primary generators ω_q** by linear algebra | the auxiliary prime, plus factoring Φ_q of degree q − 1 < N (induction on degree) |
| random separator for N even | **tournament** on ordered root pairs: orient (i, j) by the 2-adic discrete log of (x_i − x_j)^t relative to ω₂. Opposite pairs differ by 2^{s−1}. The row counts c_i sum to N(N−1)/2, so they cannot all equal (N−1)/2 when N is even (02-finite-fields.tex, Prop ff:even-split) | an integer count identity (pigeonhole) |
| random separator for N odd | curve Y^q = F(X), λ = 1 − σ on the Jacobian. Lift [P_i − ∞₀] through λ^m, m = 1 + (q−1)v_q(N). Label tests t = 1..m; if all labels agree at every level, Ne would lie in λ^mΛ, contradicting Ne ∈ λ^{m−1}Λ ∖ λ^mΛ (05-geometry.tex, Prop geom:separation). Norm equations are solved through maximal orders of a split cyclic algebra (03-norms.tex) | a lattice-valuation obstruction (algebraic) |

**Fact 1.3 (PROVED, standard).** For q = 2 the non-square produced is the auxiliary prime itself, up to a square.
The solution v of v^p = −v in U₂ is λ·g, where g is the quadratic Gauss sum (g^p = (p/ℓ)g = −g, and the
(−1)-eigenspace of Frobenius on U₂ is one-dimensional). Hence c = v² = λ²g² = λ²ℓ, since ℓ ≡ 1 (mod 4). By reciprocity
(ℓ/p) = (p/ℓ) = −1. So the q = 2 branch is just "search primes ℓ ≡ 1 (24) until (ℓ/p) = −1". That is a fixed-density
Dirichlet detector of conductor 24p, density 1/16, and 003 alone already bounds it by ≪ (log p)⁸
(`OAI_DUMP_IMPACT.md` §2.1).

### 1.3 How the auxiliary primes are forced (10-analytic.tex, Prop analytic:auxiliary)

Let K = ℚ(μ_{12q}) and M = K(p^{1/q}). M/K is cyclic of degree q (X^q − p is Eisenstein above p), so
ζ_M = ∏_{χ} L_K(s, χ) over the q characters of Gal(M/K). 029 Thm 1.2 gives every L_K(s, χ) the zero-free region
Re s > 1 − 10⁻⁶, and ζ_K too, uniformly in K ⊇ μ₁₂. A smoothed explicit formula gives
Ψ_M(x) = xΦ(1) + O(x^{1−δ}(log D_M + d_M)), with log D_M + d_M ≪ B³. Then

  Ψ_K(x) − q⁻¹Ψ_M(x) = (1 − q⁻¹)xΦ(1) + O(x^{1−δ}B³).

A degree-one prime of K over a non-auxiliary ℓ splits completely in M, so its contribution **cancels exactly**. Prime
powers, higher residue degree and the ramified primes over 2, 3, p, q together give O([K:ℚ]√x log²x). Hence an auxiliary
prime exists in (x, 2x] once x = T·B^{2·10⁷}. Three features matter for §2:

1. The success event is a **Frobenius condition on the candidate ℓ in one fixed field M**, determined by p. Its density
   is 1 − 1/q among degree-one primes of K, i.e. (1 − 1/q)/φ(12q) among rational primes. So there are infinitely
   many successes, of positive density.
2. **Reciprocity is what makes the sum over candidates an L-function sum.** The q-th power residue symbol (p/𝔩)_q is the
   Artin symbol of 𝔩 in M/K. So Σ_ℓ χ_ℓ(p), a sum over moduli at the fixed point p, becomes a prime sum of a fixed Hecke
   character of K. This works only because the order q is the same for all ℓ.
3. The **ramified primes** (those over p, q, 2, 3) enter only in the error term, as O(log D_M), and are discarded.

### 1.4 Exactly what 142 needs from 029, and from nothing else

* 142 imports **only** 029 Thm 1.2: for every cyclotomic K ⊇ μ₁₂ and every finite-order Hecke χ of K, L_K(s, χ) ≠ 0 for
  Re s > 1 − 10⁻⁶, with no conductor or height restriction. The *uniformity of δ across the growing family* ℚ(μ_{12q}),
  q ≤ n, is essential: the paper stresses that a width deteriorating with the discriminant or height "would not give
  the bound below by the same calculation".
  142 does not use 029's Artin headline or its reservoir and splitting propositions. Those are what give the
  one-mute-prime consequence in `OAI_DUMP_IMPACT.md` §4.
* For q = 2, Dirichlet L-functions suffice, so 003 (claimed, Lean-formalized) is enough (Fact 1.3). For q ≥ 3 the field
  M is non-abelian over ℚ, and 142 needs Hecke L-functions over ℚ(μ_{12q}). That goes beyond 003, whose Hecke statement
  covers only ℚ(√−3).
* Under GRH for Hecke L-functions the reduction alone gives the theorem (142's own remark at the end of §10). So 142 is
  "deterministic factoring in P under the 029 strip", and the algebra (Thm 1.2) is GRH-free.
* Chain of trust: 142 ← 029 Thm 1.2, which extends 003's reflection/Poisson method to all cyclotomic K ⊇ μ₁₂. 029's own
  Type II input comes from 011. These are not independent corroborations (`OAI_DUMP_IMPACT.md` §1.2).

**Assessment.** The derandomisation has two kinds of forcing, and both matter for ES. *Analytic forcing* proves that a
positive-density Frobenius class contains a small prime. *Algebraic forcing* shows that a polynomial-size list of tests
must separate the components of an algebra that is **known to be a non-trivial product** (F totally split of degree
N ≥ 2). Neither is an existence theorem for a sparse arithmetic object.

## 2. The ES analogue, tried concretely

### 2.1 The candidate set and the index dictionary

**Candidate set (the prime-modulus (★) family).** For a prime p ≡ 1 (mod 4), let 𝒮 be the primes ℓ ≡ 3 (mod 4), and
call ℓ a **success** E_p(ℓ) if ℓ | p + u for some u | (ℓ+1)/4. Then C = (ℓ+1)/(4u) and B = (p+u)/ℓ give
4uBC − u − B = p. This is (★) with d = ℓ a prime divisor of 4Cp + 1 in the class −1 (mod 4C), the forest edge u ~ B with
t = 4C. Since u ≡ −p (mod ℓ) and u ≤ (ℓ+1)/4, u is determined by ℓ. Success means **p mod ℓ lies in the set
S_ℓ = {−u : u | (ℓ+1)/4}, of size τ((ℓ+1)/4) = ℓ^{o(1)} in 𝔽_ℓ^*.**

**Prop 2.1 (index-m relaxation identity; PROVED, elementary; CERTIFIED 726/726 exact `Fraction` checks, Part A).** Let
ℓ = 4uC − 1 and m ≥ 1, and suppose ℓ | p g^m + u for some integer g. Put B = (pg^m + u)/ℓ. Then 4uBC − u − B = pg^m and

  4/p = g^m/(uBC) + 1/(pBC) + 1/(puC).

The condition is solvable in g exactly when −u/p ∈ (𝔽_ℓ^*)^{m′}, with **m′ = gcd(m, ℓ−1)**. g = 1 is (★), the cap-0 event.
*Proof.* B(4uC−1) − u = pg^m; multiply the (★) identity for n = pg^m by g^m. The solvability claim holds because 𝔽_ℓ^* is
cyclic. ∎

*Novelty:* this is the A13 / `FIXED_MODULUS_SHOTS` shot shape written in (★) coordinates, and the gcd-index is
`POWER_LADDER_ES`'s i_k(g) = gcd(k, g−1). So it is repo-known in substance. The only new element is reading it as
"Frobenius index at the candidate ℓ ↔ numerator power", which is how 142's auxiliary condition maps onto ES.
*Lowest terms.* The displayed fraction need not be in lowest terms with a square numerator. Example: p = 9601,
ℓ = 23, g = 4 gives g²/(BC) = 8/20037. Theorem 2.2 below therefore chooses the lift of g.

**Consequences of m′ = gcd(m, ℓ−1).** Every (★) modulus has ℓ ≡ 3 (mod 4), so v₂(ℓ − 1) = 1.
* For odd m and a candidate with gcd(m, ℓ−1) = 1, the relaxation is solvable with no condition on p at all. Odd-index
  layers do exist when q | ℓ−1 for an odd prime q | m (e.g. ℓ = 7, m = 3, p = 5, u = 1: −u/p ≡ 4 is not a cube mod 7),
  but they can be avoided by choosing the candidate. This is `POWER_LADDER_ES` Thm 2.1 again: odd rungs are free.
* For m = 2 it is the condition (−up/ℓ) = 1. At u = 1 this reads (ℓ/p) = −1, using reciprocity and p ≡ 1 (mod 4).
* **So at prime (★) moduli the only bounded-index layer that cannot be avoided is index 2, the quadratic/BM layer.**
  029's Kummer generality (q ≥ 3) is not needed for any relaxation in this family. Composite moduli 4uC − 1 have non-cyclic unit groups and admit
  odd-order characters, but by `CLASS_FORCING.md` Thm 2.1 and `TWO_POWER_LADDER.md` those layers still force only
  character data, never the class.

**Thm 2.2 (deterministic square-numerator witness; CONDITIONAL on OAI-003 (quasi-RH 7/8), or on 142's own analytic input,
or on GRH).** (029 Thm 1.2 suffices because ζ of the abelian field ℚ(μ₁₂, √p) is a product of Hecke L-functions over
ℚ(μ₁₂) and also of the Dirichlet L-functions used below; a zero-free product of factors holomorphic in the strip (apart
from the pole of ζ at 1) has zero-free factors. This transfers the width 10⁻⁶ strip only, not a wider one.)
For every prime p ≡ 1 (mod 4) there is a prime ℓ ≡ 3 (mod 4) with (ℓ/p) = −1 and ℓ ≪ (log p)^{1/(1−θ)}. That is
(log p)⁸ under 003 (θ = 7/8), (log p)^{10⁶} under 029 Thm 1.2 alone (θ = 1 − 10⁻⁶), and (log p)² under GRH. Upward search finds it in
deterministic poly(log p) time. Put C = (ℓ+1)/4, and let g be the least positive integer that is odd, coprime to pC,
and satisfies pg² ≡ −1 (mod ℓ); g exists by CRT and g < 2ℓC·p. With B = (pg² + 1)/ℓ,

  4/p = g²/(BC) + 1/(pBC) + 1/(pC),   gcd(g, BC) = 1,

so the first term is in lowest terms with odd square numerator g², an ES^□-type witness.
*Proof.* The detector (1 − χ_{−4})(1 − χ_p)/4 has density 1/4 and conductor 4p. Apply `OAI_DUMP_IMPACT.md` (2.2)–(2.3),
whose exponent is A(θ) = 1/(1−θ), then Prop 2.1 with u = 1, m = 2. For lowest terms: a prime r | g with r | B divides
ℓB − pg² = 1, so gcd(g, B) = 1, and gcd(g, C) = 1 by choice. ∎

*Scope:* this is a relaxation of the ES^□ / A13 type, already a theorem by one Dirichlet prime. The only new feature is
the deterministic polylog bound. **CERTIFIED (Part B/D):** across 18 506 primes p ≡ 1 (24) up to 2·10⁶, the least such ℓ is
≤ 0.70(log p)². At every (★)-failure prime tested (409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321,
8813281), ℓ ≤ 31, and the lowest-terms odd-square-numerator solution of Thm 2.2 was verified exactly, including gcd(g, BC) = 1
(Part D). Part B covers ℓ for the other three R(p) = 0 primes ≤ 2·10⁶, inside its 0.70(log p)² maximum; there the lift
is guaranteed by the proof but not separately computed. Examples: 4/409 = 9/1052 + 1/430268 + 1/818, and
4/9601 = 361/904164 + 1/8680878564 + 1/57606 with g = 19 (the even lift g = 4 is rejected).
The full scans found **no (★) hit at any modulus** at those primes, so the relaxation lives where cap 0 is empty.

### 2.2 The needed non-vanishing statement

To construct an ES witness the way 142 constructs ℓ_q, one needs, for all large p:

  **(NV_ES)** Σ_{ℓ ≤ X, ℓ ≡ 3 (4)} Σ_{u | (ℓ+1)/4} 1[p ≡ −u (mod ℓ)] ≥ 1, with X = (log p)^A.

Here 1[p ≡ −u (mod ℓ)] = (1/(ℓ−1)) Σ_{χ mod ℓ} χ(p) χ̄(−u). Split the characters by order:
* **order dividing a fixed m** (in practice m = 2): by Kummer reciprocity χ_ℓ(p) is the Artin symbol of ℓ in a fixed
  field ℚ(μ_m, p^{1/m}), so 142/029/003-type strips control these sums. They yield only the relaxation (Thm 2.2).
  With 029's uniformity the order may even grow, up to poly(log p), which goes beyond the bounded orders of
  `FROBENIUS_FIRING.md` Remark 2.5. As computed below, this still does not reach ES.
* **orders not dividing m, up to ℓ − 1:** no reciprocity law turns χ_ℓ(p), for χ of order ≍ ℓ, into a Hecke character
  of one fixed field. The values would have to lie in μ_{ord χ}, which grows with ℓ. The sum over these characters is
  not an L-function sum. After orthogonality it is literally the count of divisors of p + u in a class modulo the
  candidate, which is B2. This is the "Artin problem with moving order" of `FROBENIUS_FIRING.md` Remark 2.5, now with
  142's mechanism named.

### 2.3 Where exactly it fails (the B2 step), three ways

**(F1) No sufficient Frobenius condition; PROVED, repo-known.** E_p(ℓ) forces ℓ ≤ (4p+1)/3, so the success set is
finite, while every non-empty Chebotarev set is infinite. Hence no field M (even p-dependent) and non-empty C have
"Frob_ℓ ∈ C ⇒ E_p(ℓ)" for all unramified ℓ. This is `FROBENIUS_FIRING.md` Prop 1.2, with a GRH range version in Thm 1.4.
In 142 the success set is infinite with positive density. This is the categorical difference.

**(F2) Resolution versus scale; PROVED inequality plus Assessment.**
* *Resolution (PROVED).* For ℓ ≡ 1 (mod m) and p ∤ m, Frob_ℓ in M_m = ℚ(μ_m, p^{1/m}) determines exactly the image of p
  in 𝔽_ℓ^*/(𝔽_ℓ^*)^m, by Kummer theory. A set S ⊆ 𝔽_ℓ^* is a union of cosets of (𝔽_ℓ^*)^m only if it is empty or
  |S| ≥ (ℓ−1)/m. So detecting E_p(ℓ) exactly from M_m forces m ≥ (ℓ−1)/τ((ℓ+1)/4) = ℓ^{1−o(1)}. Then
  [M_m:ℚ] ≥ mφ(m)/2 = ℓ^{2−o(1)}. (The τ divisor classes of S_ℓ are unions of single classes.)
* *Scale (Assessment; the standard explicit-formula estimate, as in 142's Prop analytic:auxiliary).* Expand the class
  indicator over the characters of the abelian M_m/ℚ(μ_m). Both the main term and the summed error then carry the
  factor 1/[M_m:ℚ], so the strip certifies a single class once x^δ ≫ log D_{M_m} + [M_m:ℚ] ≈ m² log(mp). At the
  certified prime ℓ ≤ 2x the certified index is therefore m ≲ ℓ^{δ/2}. That is ℓ^{1/4} under GRH (the familiar
  (log D)² Chebotarev scale) and ℓ^{5·10⁻⁷} at 029's δ = 10⁻⁶. ES needs m ≳ ℓ^{1−o(1)}. Even δ = 1 would give only
  ℓ^{1/2}, the trivial counting scale: a class of a group of order ≍ m² needs ≳ m² primes. **With this method a
  strip-forced Frobenius datum is coarse at the prime it certifies.** This is a statement about the method, not a
  universal ceiling: a cleverer argument could in principle certify a small ℓ in a fine class. It is the analytic face
  of M1a/B3: the expected number of exact successes with ℓ ≤ X is about log X,
  a logarithmic main term, while strip methods beat errors only against main terms ≫ X^{1−δ}. (No unconditional upper
  bound on #{ℓ ∈ (x, 2x] : E_p(ℓ)} below x^{1−δ} is proved here, so this is not a theorem about all arguments.)
* **EVIDENCE/CERTIFIED (Part C).** At p = 1 000 121, the moduli ≤ X with 142-type successes (aux, q = 2) number 9, 71,
  583 and 4 824 for X = 10³…10⁶, and the index-2 relaxation successes number 47, 311, 2 393 and 19 680. Both grow like
  X/log X. The exact successes number 7, 7, 9 and 11 (prime moduli) and 11, 15, 24 and 34 (all (★) moduli): logarithmic
  growth. At p = 409 and 8 813 281 the relaxation counts are the same order, while the exact counts are 0 at every X.

**(F3) The ramified reading (Assessment, with one PROVED identity).** Success at ℓ is "ℓ divides the prescribed integer
N = p + u (or 4Cp + 1)". For p + u not a square, these are the primes that ramify in ℚ(√(p+u)) when they divide p + u to
an odd power, and they satisfy Σ_{ℓ^k ∥ N} k log ℓ = log N (PROVED, trivial). In the 142 explicit formula exactly
these contributions form the O(log D_M) term that is discarded (§1.3, feature 3). The class condition ℓ ≡ −1 (mod 4C)
is a Frobenius condition in ℚ(μ_{4C}). ES therefore asks for **Frobenius statistics restricted to the ramification set
of another field**, a finite set of total weight log N. No density theorem addresses it. Reciprocity and genus theory
on that set give only parity: `CLASS_FORCING.md` Thm 2.1, "reciprocity forces parity, never class".

### 2.4 The algebraic forcing does not transfer

* **Tournament (even case).** The ES analogue pairs each divisor d of N = 4Cp + 1 with N/d, whose classes mod 4C are
  a and a⁻¹ (since N ≡ 1 (mod 4C)). Non-self-inverse classes pair off, so #{d | N : d² ≡ 1 (mod 4C)} ≡ τ(N) (mod 2),
  which is even for non-square N (PROVED, elementary). The forced members are d = 1 and d = N, both ≡ +1. The
  count is already satisfied by trivial divisors and says nothing about −1. This is board #3's parity-loophole closure:
  an even count may consist only of trivial members.
* **Lattice valuation (odd case).** 142's contradiction ("all labels equal ⇒ Ne ∈ λ^mΛ") uses only v_q(N) of a
  *given* non-trivially split algebra. ES "total failure" is consistent at odd squares (T1), and a symmetric labelling
  of the forest is cheap: many vertices are isolated, and under Dickson, for every fixed H, infinitely many p have every
  component meeting {1, …, H} monochromatic ((J)106, `LOWER_TAIL_ASTRA.md`; a statement about components meeting a fixed
  finite root set, not about all components). An ES analogue would need an identity that a uniform failure violates, and that identity must be
  false at m² and at 8/131 (checklist lines 1–2). 142 supplies no such identity. Its obstruction is about the size and
  valuation of an object set known to be non-trivial, not about primality versus squareness.
* **Meta-reason (Assessment).** 142 never proves that something exists. Factorisations exist trivially, and the
  algorithms only *locate* them. ES is open as an existence statement, with about log²p expected objects among about
  p log p candidates. Derandomising a search whose success probability is ≥ 1/2 per trial is a different problem
  from forcing a sparse lottery to have a winner.

### 2.5 142 as an oracle for ES search (Assessment)

142 puts all of 𝔽_p-algebra in P (CLAIMED): roots of arbitrary polynomials mod p, and hence Frob_p in number fields of
polynomial degree. The (★) events are *abelian* Frobenius conditions of p (p mod 4uB = −(u+B)), which are already
trivially computable. The non-abelian local data the oracle adds is inert on finite witness sets ((J)96). The witness
itself needs the factorisation of integers p + u or 4Cp + 1, and 142 does not factor integers (A7: even with a
factoring oracle, polylog C is the open FQ). So no arrow ES-SEARCH ≤ 𝔽_p-ALG is known, and none is suggested by 142's
method.

### 2.6 FRONTIER §4 screen of the best design (D1 with Thm 2.2)

| line | result |
|---|---|
| 1 T1 | PASS for Thm 2.2: (ℓ/p) = −1 has no solution at a square. FAIL as an ES route: the exact layer is untouched |
| 2/3 numerator 8 | Thm 2.2's index-2 shape also works for 8/n (ES^□-type relaxations hold at 8/131); it must not be transported to cap 0 |
| 4 tied modulus | **FAIL**: the class modulo the moving candidate ℓ is the non-reciprocity layer (§2.2) |
| 5 p fixed | PASS: averaging is over auxiliary ℓ with p fixed, legitimately, as in 142 |
| 6 scale | **FAIL** for cap 0: log main term against an X^{1−δ} error (F2) |
| 9 class vs parity | **FAIL**: strips give index-2, or index-polylog via 029, never class |
| 12 relaxation transport | **FAIL**: no transport g² → 1 |
| 14 test primes | Thm 2.2 succeeds at all 13 (★)-failures in range (≤ 2·10⁶, plus 8 813 281; §2.1); cap 0 is empty there |

## 3. The converse link with HARDNESS_MAP A5

* **A5 (PROVED)** stays valid: QNR-SEARCH ≤ ES-PRIME-SEARCH with one oracle call. Under 142 (via 029) or 003 the target
  is in FP (CLAIMED). Then A5 carries no hardness content: an efficient ES solver would no longer solve an open problem.
* **The round trip (PROVED arrows).** ES witness →(A5, Lemma CT)→ an index-2 datum, (ab/p) = −1 →(Thm 2.2, Prop 2.1)→
  a square-numerator witness. Composing gives ES-SEARCH → QNR → ES^□-SEARCH, all deterministic and polynomial-time
  (the second arrow CONDITIONAL on 003 / 142's input / GRH). The round trip loses exactly **the class inside the BM coset**,
  the φ(4u)/2 → 1 step of FRONTIER §7 item 3. So "QNR ⇒ ES" is not merely unproved: it is B2, by the same index count
  as §2.3 (F2).
* **What 142 adds to the complexity picture (Assessment).** If 142 holds, deterministic QNR, prime-field square roots
  (A6) and factoring polynomials over 𝔽_p are all in FP. ES-SEARCH ∈ FP then becomes a question about ES alone. It
  would follow from H₄(p) ≤ (log p)^{O(1)} with the forest scan, from FQ plus integer factoring (A7), or from any
  polylog-height witness theorem. It is equivalent to no known problem, and every route to it is B2. Small curiosity:
  142's own q = 2 auxiliary primes are ≡ 1 (mod 24), so they can never be prime (★) moduli, which are ≡ 3 (mod 4). The
  index-2 relaxation needs the other half of the residue classes, with the same strip.

## 4. Computations (CERTIFIED unless marked)

`ulimit -v 8000000; timeout 3000 uv run python scripts/z48_oai142_dictionary.py 2000000 > data/z48_oai142/summary.txt`
(about 2 s). Pure Python, one byte-sieve to 1.2·10⁷.

* Part A: Prop 2.1 checked exactly on 726 random instances, m ∈ {1, 2, 3, 4, 6}.
* Part B (18 506 primes p ≡ 1 (24), p ≤ 2·10⁶; maxima over p ≥ 10⁴):

  | quantity | max / (log p)² | at p |
  |---|---|---|
  | 142 auxiliary prime, q = 2 (ℓ ≡ 1 mod 24) | 6.36 | 187 513 (ℓ = 937) |
  | 142 auxiliary prime, q = 3 (ℓ ≡ 1 mod 36) | 5.03 | 10 753 (ℓ = 433) |
  | index-2 relaxation, Thm 2.2 (ℓ ≡ 3 mod 4) | 0.70 | 880 993 (ℓ = 131) |
  | least prime (★) modulus, when one exists | 4 515 | 1 749 073 (ℓ = 932 839) |
  | least (★) modulus, when one exists | 354 | 706 801 (m = 64 255) |

  116 primes have **no prime-modulus (★) hit at all**: 409, 577, 2377, 2521, 3361, … The 12 with R(p) = 0 are 409, 577,
  5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201. This agrees with the census in
  `BM_CORRECTED_COUNT.md` / FRONTIER §2.1.
* Part C: counts as quoted in §2.3 (F2).
* Part D: 10 (★)-failure primes with full scans to (4p+1)/3, each with its explicit square-numerator solution verified.

## 5. Verdict, promise, next steps

**Verdict.** No mechanism in 142 or its 029 dependency gives a provable deterministic search for an ES witness.
142's arithmetic input is a positive-density Frobenius event in a Kummer field over ℚ(μ_{12q}), forced by a uniform
Hecke strip. Its algebraic forcing locates objects that exist a priori. Transferred to ES, this proves exactly the
bounded-index relaxations (Prop 2.1, Thm 2.2), and at prime (★) moduli only index 2 cannot be avoided. Cap 0 fails at
one named step: the class of p modulo the candidate ℓ at resolution ℓ^{1−o(1)}, against about ℓ^{δ/2} (ℓ^{1/4} under
GRH) from the standard strip calculus (Assessment). That step is B2 (F1–F3), and it is the step `FROBENIUS_FIRING.md` Remark 2.5 identified. The A5 converse closes only
to ES^□.

**Promise: 0/5** for an ES route. As documentation, 1/5.

**What is new here versus repo-known.**
* New: the 142 anatomy (§1); reading 142's auxiliary condition as a Frobenius index at the ES candidate, so that 029's
  q ≥ 3 Kummer layers are avoidable for ES; the method-level coarseness estimate "certified index ≲ ℓ^{δ/2}"
  (Assessment); the ramified reading (F3); the tournament and lattice non-transfer (§2.4); and the A5 round trip
  ES → QNR → ES^□ with a deterministic polylog lowest-terms witness.
* Repo-known: F1 (`FROBENIUS_FIRING` Prop 1.2, Thm 1.4); Remark 2.5 (moving-order Artin problem); A13 shots and the
  gcd index (`POWER_LADDER_ES` i_k(g) = gcd(k, g−1)); one mute prime from 029 (`OAI_DUMP_IMPACT` §4).

**Next steps (ranked; none expected to change ES's status).**
1. Record a single line in HARDNESS_MAP A5 / A6: "142 ⇒ 𝔽_p-ALG ∈ FP (CLAIMED, via 029); round trip ES → QNR → ES^□
   loses exactly the class inside the BM coset (OAI_METHOD_142 §3)". Do not open an ES-search ≤ 𝔽_p-ALG line.
2. If anyone revisits "Artin with moving order": the only route not closed by F2 is the *function-field* geometric flip
   (`FROBENIUS_FIRING` §2), where the index may reach q^{d/2}. Prop 2.3 there already shows the ES box is below that
   threshold. Nothing in 142 changes this.
3. Do not spend effort auditing 142's algebra for ES purposes. Its correctness matters for complexity theory (A5/A6),
   not for ES. For ES the only OAI input of any value remains 003 (effective caps, M_BM asymptotics), and those are
   relaxations.
