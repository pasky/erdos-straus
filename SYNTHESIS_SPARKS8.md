# SYNTHESIS_SPARKS8 — cross-combinations of wave AA ((J)84–(J)87, relays O256/O257) (task O258, synthesis VIII)

Status: O258 checkpoint 1 (unreviewed). **ES is not solved here, and no infinite case of ES for primes is claimed.** Labels as
in DISCOVERIES.md. Memos `BRAINSTORM/s8_*.md`; scripts `scripts/s8_*` (`s8_lines.c` = census engine, `s8_check_b1.py` =
independent brute-force checker); logs `logs/s8_*` (tiny).

Notation. Type II (ET): c n + a + b = 4abcd, (x, y, z) = (abd, acdn, bcdn). Window m := 4abd − n = (a + b)/c, K_m := (n + m)/4.
Lines (one-parameter sub-families of Type II): **b = 1 line** (cn + a + 1 = 4acd), **c = 1 line** (n + a + b = 4abd; this is
PARITY_AUDIT's (★)), **d = 1 line** (LATTICE_MEETING's meeting locus).

## 0. Iteration log
(I1) Mandatory (i), least residue × height-dependent target. Wrote the single-p event in four equivalent coordinates (window,
twisted modular hyperbola, Kloosterman fraction, mutual shift pairs; §1). Construction attempts: (1) Minkowski/Thue on the
hyperbola — Thue produces points of the twisted hyperbola Xε ≡ u (p) of uncontrolled height; ES needs a height-dependent
class (barrier hypothesis it meets: "target fixed in advance"). (2) DFI 1997 — its bilinear Kloosterman-fraction bounds ARE
uniform in the numerator a = p (so "fixed p" is not the obstruction); what fails is volume: the ES indicator has expected
count O(1) per dyadic box, so any equidistribution statement must save the full box volume (Lemma 1.5). (3) Piecewise
linearity of y ↦ (−p mod y) (continued-fraction structure) linearises the least residue on each interval (p/(k+1), p/k] and
returns exactly ET's window form (Prop 1.4). All three return to B2; recorded as a precise "what fails" (§1.6).
(I2) Mandatory (ii), support-1 lottery. Checked the brief's form: s | jp + 1, s ≡ 3j − 1 (4j) is the b = 1 line with a = s prime
(and forces j even unless s = 2). Found the **b = 1 duality** (Prop 1.3): b = 1 ⟺ some mutual shift pair (g, D) of p has
4 | D. Census (§2): **the b = 1 line fails at exactly three primes p ≡ 1 (4) ≤ 10⁸ — 193, 2521, 66529 —** and the c = 1 line at
14 primes ≤ 10⁷ and none in (10⁷, 10⁸]; the two lines never fail together ≤ 10⁸ (EVIDENCE). Per-j events are pairwise
independent to within 0.4 % on average (max ratio 1.27); joint all-j failure is 1.5 × the independence prediction. A
deterministic forcing of one j would have to be 4-specific: the k = 8 analogue of the two-line union fails at 34 primes < 8000,
including 131 and 241.
(I3) Mandatory (iii), forced windows × T1 adversary: §3.
(I4) Mandatory (iv), positivity × signed slices: §4.
(I5) Own: profinite proximity to the T1 point 1 (smooth p − 1) as a hardness coordinate (s8_profinite_proximity).

## 1. Deep item 1: one event, four coordinates (mandatory (i))

**Definition 1.1.** For n ≥ 1, the set of *mutual shift pairs* is MP(n) := {(x, y) ∈ ℤ²_{≥1} : x | n + y, y | n + x, xy | n + x + y};
N(x, y) := (n + x + y)/(xy). (If gcd(x, y) = 1 the last condition follows from the first two.)

**Proposition 1.2 (Type II = mutual shift pairs with a 2-adic quotient condition; PROVED, ET reparametrised).** For odd n,
Type II solutions (a, b, c, d) of 4/n correspond bijectively to triples (c, (x, y)) with (x, y) ∈ MP(cn) and 4c | N(x, y), via
(x, y) = (a, b), d = N/(4c). In particular
* the c = 1 line ⟺ ∃ (x, y) ∈ MP(n) with 4 | N(x, y);
* the d = 1 line ⟺ ∃ c, (x, y) ∈ MP(cn) with N = 4c;
* the b = 1 line ⟺ ∃ c: cn + 1 has a divisor w ≡ −1 (mod 4c) with w ≤ (cn + 1)/2 (x = (cn + 1)/w, y = 1).
*Proof.* cn + a + b = 4abcd says exactly ab·4cd = cn + a + b; this gives a | cn + b, b | cn + a and N = 4cd. Conversely N = 4cd with
d ≥ 1 integral reverses it. For b = 1: a(4cd − 1) = cn + 1. ∎

**Proposition 1.3 (b = 1 duality; PROVED).** For n ≡ 1 (mod 4): the b = 1 line holds ⟺ ∃ (g, D) ∈ MP(n) with 4 | D. Explicitly
(a, 1, c, d) ↦ (g, D) = ((n + 4d)/(4cd − 1), 4d), with N(g, D) = c; inverse (g, D = 4d) ↦ c := N(g, D), a := (cn + 1)/(4cd − 1).
Equivalently: **b = 1 ⟺ ∃ d ≥ 1: n + 4d has a divisor ≡ −1 (mod 4d)** (other than n + 4d itself).
*Proof.* w := 4cd − 1 divides cn + 1, hence divides 4d(cn + 1) − n·w = n + 4d; put g := (n + 4d)/w. Then g(4cd − 1) = n + 4d, i.e.
4cdg = n + g + 4d: so g | n + 4d, 4d | n + g, and N(g, 4d) = c. Conversely, from 4dgN = n + g + 4d put c := N, w := (n + 4d)/g =
4cd − 1; since 4cd ≡ 1 (mod w), c(n + 4d) ≡ cn + 1 (mod w), so a := (cn + 1)/w ∈ ℤ_{≥1}. The divisor form: w | n + 4d with
w ≡ −1 (4d) is the pair (g, 4d); w ≠ n + 4d as n + 4d ≡ n ≢ −1 (mod 4). ∎
(Checked: `s8_lines census` decides both forms completely for all p ≡ 1 (4) ≤ 10⁶: 0 mismatches.)
*Reading.* The two lines b = 1 and c = 1 are the two 2-adic faces of the one set MP(p): **b = 1 ⟺ some pair has a coordinate
≡ 0 (4); c = 1 ⟺ some pair has quotient ≡ 0 (4).** For p odd and (x, y) ∈ MP(p) coprime, at most one coordinate is even and if both
are odd then N is odd (xyN = p + x + y). So b = 1 ∪ c = 1 fails ⟺ every pair of MP(p) with an even coordinate x has v₂(x) = 1
and v₂(N) ≤ 1. T1 (PROVED, by ET Prop 1.6): for n = m² every pair of MP(m²) has this shape.

**Proposition 1.4 (piecewise-linear least residue returns the window form; PROVED).** For y ∈ I_k := (n/(k+1), n/k], (−n mod y) =
(k + 1)y − n. Hence the pairs (x, y) ∈ MP(n) with x < y and y ∈ I_k are exactly x = (k + 1)y − n with x | k + 2 (if n is
prime and x < n); writing s := k + 1: **MP(p) ∩ {x < y} ↔ {(x, s) : x | s + 1, s | p + x}**, y = (p + x)/s, N = (s + 1)/x.
*Proof.* On I_k, 0 ≤ (k+1)y − n < y. If x = (k+1)y − n divides n + y then x | (k+1)(n + y) − x = (k + 2)n; as x < y ≤ n and n = p
prime, x | k + 2. Conversely x | k + 2 gives gcd(x, k + 1) = 1 and x | (k + 2)n − ... i.e. x | (k+1)(n + y), hence x | n + y; and
y | n + x as n + x = (k + 1)y. N = (n + x + y)/(xy) = (s + 1)y/(xy). ∎
*Reading.* The continued-fraction (Farey) structure of y ↦ −p mod y is exactly piecewise linear, and linearising returns ET's
window form "s | p + x, x | s + 1" — the divisor-in-a-moving-class event (B2). No information is gained or lost.

**Proposition 1.5 (twisted modular hyperbolas; PROVED, ET reparametrised).** For u ≥ 1 let H_u := {(X, ε) ∈ ℤ²_{≥1} : Xε ≡ u
(mod p)} and call c := (Xε − u)/p the *height* of a point. Then
  ES-Type-II(p) ⟺ ∃ u ≥ 1 and a point (X, ε) ∈ H_u of height c ≥ 1 with X ≡ −1 (mod 4cu),
via (a, b, c, d) = (u, ε, c, (X + 1)/(4cu)). Equivalently: ∃ c, u: cp + u has a divisor ≡ −1 (mod 4cu); and on the single
hyperbola XY ≡ 1 (mod 4p): ∃ (X, Y) with C := (XY − 1)/(4p), C = c²d, X ≡ Y ≡ −1 (mod 4cd) (the brief's form is c = 1).
*Proof.* cp + u + ε = 4cuεd ⟺ (4cud − 1)ε = cp + u; put X = 4cud − 1. For the last form, (4cdu − 1)(4cdv − 1) = 4c²dp + 1. ∎
*What Thue/Minkowski would need, and what fails (Assessment with a PROVED core).* Thue's lemma and Minkowski's theorem act on
lattices (linear congruences x ≡ ρy). H_u is a hyperbola, not a lattice. At a fixed height c its points are the factorisations
of the one integer cp + u, and points of small height always exist (X = 1). The ES class X ≡ −1 (mod 4cu) changes with the
height. Pigeonhole on H_u controls size (hence an upper bound on the height), never the exact height, and the class is
attached to the exact height. The barrier hypothesis that ES violates is "the target class is fixed before the point is
chosen".

**Lemma 1.6 (O(1) points per dyadic box; PROVED, elementary — the volume form of B3).** For X, Y ≥ 1 with XY ≤ p, the Haar
expectation (p uniform in a residue class modulo lcm of all xy) of #{(x, y) ∈ MP(p) : x ~ X, y ~ Y, gcd(x, y) = 1} is
Σ 1/(xy) ≍ 1 (each pair imposes p ≡ −x − y (mod xy)). Consequently any completion (Fourier) count of the box is
  (1/(XY)) Σ_{(h,k) ≠ 0} S(h, k),   S = a complete exponential sum of length ≍ XY,
and even square-root cancellation in every S(h, k) separately leaves an error ≍ (XY)^{1/2} ≫ 1 = the main term. A nontrivial
count at one p needs cancellation *across* frequencies, i.e. beyond square root.
*Proof.* The density statement is CRT. For the completion: there are ≍ XY nonzero frequency pairs, each |S| ≤ (XY)^{1/2+o(1)}
at best, normalised by 1/(XY); summing trivially over frequencies gives (XY)^{1/2+o(1)}. ∎
*DFI 1997 (Duke–Friedlander–Iwaniec, Invent. Math. 128, "Bilinear forms with Kloosterman fractions").* Their bound for
Σ α_m β_n e(a·m̄/n) is uniform in the numerator a, so a fixed p is NOT the obstruction (contrary to a natural guess). They
save a power over the trivial bound ‖α‖‖β‖(MN)^{1/2} for one frequency, i.e. at the level of a single S(h, k). Lemma 1.6 says
the ES count needs a saving of the full factor (XY)^{1/2} beyond that, summed over all ≍ XY frequencies. DFI-type input
therefore enters only through averages over p or over residues a (the (J)87 table), never at one p.

**1.7 Answer to mandatory (i) (Assessment).** The single-p problem is ONE statement in four equivalent coordinates (window
least residue, twisted hyperbola with height-dependent class, Kloosterman fraction X̄/(4p) within ≍ 1/(uX) of 1/(4u),
mutual shift pairs with a 2-adic quotient condition). Each tool reaches a different wall:
| tool | hypothesis it needs | ES violates it because |
|---|---|---|
| Minkowski / Thue | lattice (linear congruence), fixed target | H_u is a hyperbola; class depends on the height (Prop 1.5) |
| DFI / Weil / Kloosterman | main term ≫ completion error | O(1) per box; even √-cancellation leaves (XY)^{1/2} (Lemma 1.6) |
| continued fractions / Farey | real-number target | piecewise linearity returns ET's window form (Prop 1.4) |
| inhomogeneous GoN (covering radius) | fixed modulus, covering | covering needs subpower windows ((J)85 Thm 3.1) |
No route from (i) survives; this re-confirms (J)85/(J)87 with exact failure points, not a new obstruction theorem.

## 2. Deep item 2: the b = 1 line — the support-1 lottery made exact (mandatory (ii))

**2.1 The brief's form (PROVED).** "∃ j, prime s | jp + 1 with s ≡ 3j − 1 (mod 4j)" is the b = 1 line with a = s prime and
c = j: cp + s + 1 = 4scd ⟺ (jp + 1)/s = 4jd − 1 ≡ −1 (mod 4j), and for p ≡ 1 (4) this is equivalent to s ≡ 3j − 1 (mod 4j) (since
jp + 1 ≡ j + 1 (mod 4j)). For odd j, 3j − 1 is even, so s = 2: **odd-prime support-1 certificates have j even.** (Data: Fp_j has
failure rate exactly 1 for odd j ≥ 3, `logs/s8_perj_1e6.txt`.) Via Prop 1.3 the same line reads: **∃ d ≥ 1: p + 4d has a
divisor ≡ −1 (mod 4d)** — (J)6's (★), R(p) = #{(j, f) : f | p + j, f ≡ −1 (4j)}, with the shift j replaced by 4j. (★) itself
is the c = 1 line.

**Lemma 2.2 (visibility and forced levels of the b = 1 line; PROVED, Jacobi).** Let p ≡ 1 (4) and gcd(d, p) = 1.
(a) If w | p + 4d and w ≡ −1 (mod 4d), then (w/p) = −1: the divisor carries a T1-visible prime.
(b) χ_{−4d}(p + 4d) = (d/p). So at every level d with (d/p) = −1 the integer p + 4d has an odd number of prime factors ℓ with
χ_{−4d}(ℓ) = −1. These *forced levels* are exactly the non-residues d mod p, a set of density 1/2 in d (least element
≪ p^{1/(4√e)+ε} by Burgess, ≪ log²p on GRH). Forcing supplies the parity χ_{−4d}(w) = −1, not the class w ≡ −1 (mod 4d).
*Proof.* (b) χ_{−4d} has modulus dividing 4d, so χ_{−4d}(p + 4d) = χ_{−4d}(p) = (−4d/p) = (d/p) (p ≡ 1 (4)). (a) w | cp + 1 with
c = (w + 1)/(4d) (Prop 1.3). Jacobi: (−cp/w) = 1, so (p/w) = (−c/w). Write c = 2^e c′. Then (−1/w) = −1 (w ≡ 3 (4)), and
(c′/w) = (w/c′)(−1)^{(c′−1)/2} = (−1/c′)(−1)^{(c′−1)/2} = 1 (w ≡ −1 (c′), (w − 1)/2 odd). If e ≥ 1 then w ≡ 7 (8) and (2/w) = 1.
So (p/w) = −1, and (w/p) = (p/w) as p ≡ 1 (4). ∎

**Lemma 2.3 (privacy of large primes across j; PROVED).** gcd(jp + 1, j′p + 1) divides j − j′. Hence a prime ℓ > J divides at
most one of jp + 1 (j ≤ J). The same holds for p + 4d, d ≤ D, with ℓ > 4D: gcd(p + 4d, p + 4d′) | 4(d − d′).
*Proof.* j′(jp + 1) − j(j′p + 1) = j′ − j. ∎
*Reading.* Any pigeonhole across j (or d) can only collide primes ℓ ≤ J. Such a collision is a congruence on p mod ℓ (ℓ | jp + 1
⟺ j ≡ −p̄ (ℓ)), so it is B1 data, blind at the T1 point. The large prime factors that make the lottery succeed are private to a
single jp + 1. A deterministic mechanism forcing one j must therefore produce a divisor of ONE integer jp + 1 in the class
−1 (mod 4j): B2, with no cross-j leverage. This is the exact sense in which "pigeonhole across j" is void.

**2.4 Census (EVIDENCE; `s8_lines.c`, complete decisions for every window m ≤ (p + 4)/3; independent brute force
`s8_check_b1.py` at the failures and at T1/105; 0 mismatches between window and divisor forms ≤ 10⁶).**
| event (p ≡ 1 (4)) | failures ≤ 10⁶ | failures ≤ 10⁸ | notes |
|---|---|---|---|
| full Type II | 0 | 0 (≤ 10⁸) | max least window 63 (≤ 10⁶) |
| **b = 1 line** | **3: 193, 2521, 66529** | **the same 3** | last failure 66529; max least window 327 |
| c = 1 line = (★) | 9 | 14 (≤ 10⁷: 409, …, 8 813 281), none in (10⁷, 10⁸] | as PARITY_AUDIT |
| support-1 prime s (z24) | 752 | — | j even forced (2.1) |
| D-form, prime divisor | 123 | — | |
| b = 1 ∪ c = 1 | **0** | **0** | the failure sets are disjoint |
T1: all six events fail at 9, 25, 49, 81, 121, 169, 225, 289, 361, 441, 529 (and at 105, which is composite).
Per-j (b = 1 line at c = j, all 39 175 primes ≤ 10⁶, j ≤ 24): failure rates 0.128 (j = 1), 0.389, 0.474, 0.523 (j = 4), …,
0.907 (j = 24). Pairwise joint-failure/product ratio has mean 1.004 and max 1.27 (j = 1, 4). All 24 fail at 10 primes, against
6.6 predicted by independence: near-independence, with a mild shared tail (the QR-richness factor of s7_lvalue_proxy).
All three b = 1 failures have p − 1 11-smooth (192 = 2⁶·3, 2520 = 2³·3²·5·7, 66528 = 2⁵·3³·7·11). Only 1292 of the 2.88·10⁶
primes p ≡ 1 (4) ≤ 10⁸ have this property; see s8_profinite_proximity for what this does and does not mean.

**Conjecture 2.5 (b = 1 line; CONJECTURE, EVIDENCE to 10⁸).** For every prime p ≡ 1 (mod 4), p ∉ {193, 2521, 66529}, there is
d ≥ 1 such that p + 4d has a divisor ≡ −1 (mod 4d); equivalently 4/p = 1/(ad) + 1/(acdp) + 1/(cdp) for some a, c, d ≥ 1.
*Status and limits (Assessment).* It is stronger than ES at primes p ≡ 1 (4), so it is at least as hard. It fails at odd
squares (T1) and at 105, so a proof must use primality. Its numerator-8 analogue fails at 60 primes < 8000; the union of the
two k = 8 lines fails at 34 primes < 8000, including 131 and 241 (`s8_check_b1.line_counts_k`). Any proof must therefore be
4-specific. Value: it confines the ES lottery for p ≡ 1 (4) to ONE shift family {p + 4d}. The heuristic count is ≍ log²p
(means 16 at p ≈ 2·10⁴ and 20 at p ≈ 2·10⁶ in the Mordell classes). Failure is then a polylog lottery, as for (★), but with
much better constants in range.
