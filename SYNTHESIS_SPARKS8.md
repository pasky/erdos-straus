# SYNTHESIS_SPARKS8 — cross-combinations of wave AA ((J)84–(J)87, relays O256/O257) (task O258, synthesis VIII)

Status: O258 checkpoint 1; hostile review R268 (`reviews/synthesis-eight-review.md`): no FATAL, MAJOR M1–M4, minors; repairs
applied by the reviewer, marked (R268 repair). **Prior art (R268 repair, M4): M. A. López, arXiv:2404.01508 — Type A = the b = 1
line, his Thm 7 = the divisor form of Prop 1.3, the Type-A exceptions 193, 2521, 66529, and his Conjecture 1 = "b = 1 ∪ c = 1 never
fails" (checked there to 104 729).** Status otherwise: **ES is not solved here, and no infinite case of ES for primes is claimed.** Labels as
in DISCOVERIES.md. Memos `BRAINSTORM/s8_*.md`; scripts `scripts/s8_*` (`s8_lines.c` = census engine, `s8_check_b1.py` =
independent brute-force checker); logs `logs/s8_*` (tiny).

Notation. Type II (ET): c n + a + b = 4abcd, (x, y, z) = (abd, acdn, bcdn). Window m := 4abd − n = (a + b)/c, K_m := (n + m)/4.
Lines (one-parameter sub-families of Type II): **b = 1 line** (cn + a + 1 = 4acd), **c = 1 line** (n + a + b = 4abd; this is
PARITY_AUDIT's (★)), **d = 1 line** (LATTICE_MEETING's meeting locus).

## 0. Iteration log
(I1) Mandatory (i), least residue × height-dependent target. Wrote the single-p event in four equivalent coordinates (window,
twisted modular hyperbola, Kloosterman fraction, mutual shift pairs; §1). Construction attempts: (1) Minkowski/Thue on the
hyperbola — Thue produces points of the twisted hyperbola Xε ≡ u (p) of uncontrolled height; ES needs a height-dependent
class (barrier hypothesis it meets: "target fixed in advance"). (2) DFI 1997 — its bilinear Kloosterman-fraction bounds hold
for every numerator a but degrade with a, and are nontrivial with a = p only for boxes of size MN ≳ p (R268 repair M2; the
earlier "ARE uniform in a = p" was inaccurate); what fails is volume: the ES indicator has expected
count O(1) per dyadic box, so any equidistribution statement must save the full box volume (Lemma 1.5). (3) Piecewise
linearity of y ↦ (−p mod y) (continued-fraction structure) linearises the least residue on each interval (p/(k+1), p/k] and
returns exactly ET's window form (Prop 1.4). All three return to B2; recorded as a precise "what fails" (§1.6).
(I2) Mandatory (ii), support-1 lottery. Checked the brief's form: s | jp + 1, s ≡ 3j − 1 (4j) is the b = 1 line with a = s prime
(and forces j even unless s = 2). Found the **b = 1 duality** (Prop 1.3): b = 1 ⟺ some mutual shift pair (g, D) of p has
4 | D. Census (§2): **the b = 1 line fails at exactly three primes p ≡ 1 (4) ≤ 10⁸ — 193, 2521, 66529 —** and the c = 1 line at
14 primes ≤ 10⁷ and none in (10⁷, 10⁸]; the two lines never fail together ≤ 10⁸ (EVIDENCE). Per-j events are pairwise
independent to within 0.4 % on average (max ratio 1.27); joint all-j failure is 1.5 × the independence prediction. A
deterministic forcing of one j would have to be 4-specific: the k = 8 analogue of the two-line union fails at 34 primes 5 ≤ p < 8000,
including 131 and 241 (22 of them ≡ 1 (4), incl. 241; R268 repair m1).
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
* the b = 1 line ⟺ ∃ c: cn + 1 has a divisor w ≡ −1 (mod 4c) (x = (cn + 1)/w, y = 1). (R268 repair m2: the earlier side
  condition w ≤ (cn + 1)/2 was false for n ≡ 3 (4), e.g. n = 3, (a, c, d) = (1, 2, 1), and is unnecessary.)
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
and v₂(N) ≤ 1. T1 (PROVED, by the proof of ET Prop 1.6, which works for the equation cn + a + b = 4abcd without the coprimality
in ET's Type II definition; R268 repair m3 — reviewer checked: no solution at any odd square ≤ 841): for n = m² every pair of
MP(m²) has this shape.
(R268 repair M4: the divisor form is López, arXiv:2404.01508, Thm 7: "Type A ⟺ ∃ d, n: p ≡ −4d (mod 4dn − 1)".)

**Proposition 1.4 (piecewise-linear least residue returns the window form; PROVED).** For y ∈ I_k := (n/(k+1), n/k) (open at
n/k, where the least residue is 0; R268 repair m4), (−n mod y) = (k + 1)y − n. Hence the pairs (x, y) ∈ MP(n) with x < y and
y ∈ I_k are exactly x = (k + 1)y − n with x | k + 2 (if n is prime and x < n); writing s := k + 1:
**MP(p) ↔ {(x, s) : x | s + 1, s | p + x}**, y = (p + x)/s, s = (p + x)/y, N = (s + 1)/x; the pairs with x < y are those with
(s − 1)x < p. (R268 repair m4: the earlier "MP(p) ∩ {x < y} ↔ …" was wrong — the right-hand set maps onto all of MP(p); the
inverse is s = (p + x)/y, and x | s + 1 because sy ≡ −y (mod x).)
*Proof.* On I_k, 0 ≤ (k+1)y − n < y. If x = (k+1)y − n divides n + y then x | (k+1)(n + y) − x = (k + 2)n; as x < y ≤ n and n = p
prime, x | k + 2. Conversely x | k + 2 gives gcd(x, k + 1) = 1 and, as (k+1)(n + y) = (k + 2)n + x, x | (k+1)(n + y), hence x | n + y; and
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

**Lemma 1.6 (O(1) points per dyadic box; first sentence PROVED, elementary; the completion part is an Assessment — R268 repair
M1: it is a heuristic accounting of the triangle-inequality strategy, not a theorem about "any completion"; the sums S(h, k) are
not well defined since the moduli xy vary with the pair — the volume form of B3).** For X, Y ≥ 1 with XY ≤ p, the Haar
expectation (p uniform in a residue class modulo lcm of all xy) of #{(x, y) ∈ MP(p) : x ~ X, y ~ Y, gcd(x, y) = 1} is
Σ 1/(xy) ≍ 1 (each pair imposes p ≡ −x − y (mod xy)). Consequently any completion (Fourier) count of the box is
  (1/(XY)) Σ_{(h,k) ≠ 0} S(h, k),   S = a complete exponential sum of length ≍ XY,
and even square-root cancellation in every S(h, k) separately leaves an error ≍ (XY)^{1/2} ≫ 1 = the main term. A nontrivial
count at one p needs cancellation *across* frequencies, i.e. beyond square root.
*Proof.* The density statement is CRT. For the completion: there are ≍ XY nonzero frequency pairs, each |S| ≤ (XY)^{1/2+o(1)}
at best, normalised by 1/(XY); summing trivially over frequencies gives (XY)^{1/2+o(1)}. ∎
*DFI 1997 (Duke–Friedlander–Iwaniec, Invent. Math. 128, "Bilinear forms with Kloosterman fractions").* (R268 repair M2: the
earlier "uniform in the numerator a, so a fixed p is NOT the obstruction" was inaccurate.) Their bounds for Σ α_m β_n e(a·m̄/n)
hold for every a ≥ 1 but depend on a explicitly — (1 + a/MN)^{1/2} in Thm 1, (a + MN)^{3/8}(M + N)^{11/48+ε} in Thm 2 — and beat
the trivial bound ‖α‖‖β‖(MN)^{1/2} only when a ≪ MN (roughly; for a = p, M = N, Thm 2 needs MN ≥ p^{36/37+ε}). So the size of
the numerator p IS part of the obstruction for boxes with XY = o(p^{1−δ}). DFI's saving is bilinear, i.e. across the varying
moduli n — not a saving inside a single S(h, k). Lemma 1.6 says
the ES count needs a saving of the full factor (XY)^{1/2} beyond that, summed over all ≍ XY frequencies. DFI-type input
therefore enters only through averages over p or over residues a (the (J)87 table), never at one p.

**1.7 Answer to mandatory (i) (Assessment).** The single-p problem is ONE statement in four equivalent coordinates (window
least residue, twisted hyperbola with height-dependent class, Kloosterman fraction X̄/(4p) within ≍ 1/(uX) of 1/(4u),
mutual shift pairs with a 2-adic quotient condition). Each tool reaches a different wall:
| tool | hypothesis it needs | ES violates it because |
|---|---|---|
| Minkowski / Thue | lattice (linear congruence), fixed target | H_u is a hyperbola; class depends on the height (Prop 1.5) |
| DFI / Weil / Kloosterman | main term ≫ completion error; numerator a ≪ MN | O(1) per box (Lemma 1.6, Assessment part); a = p exceeds MN for every box with XY = o(p) (R268 repair M2) |
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
*Reading (Assessment; R268 repair m5).* Any pigeonhole across j (or d) can only collide primes ℓ ≤ J. Such a collision is a congruence on p mod ℓ (ℓ | jp + 1
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
squares (T1) and at the composites 33, 105, 145, so a proof must use primality. Its numerator-8 analogue fails at 60 primes
5 ≤ p < 8000; the union of the two k = 8 lines fails at 34 primes 5 ≤ p < 8000, including 131 and 241
(`s8_check_b1.line_counts_k`); restricted to the comparable class p ≡ 1 (4) the counts are 39 / 22 (241 included, 131 ≡ 3 (4)
not) (R268 repair m1). So a proof cannot be numerator-blind uniformly in p (threshold forms p > P₀(k) are not excluded; R268
repair m12). Value: it confines the ES lottery for p ≡ 1 (4) to ONE shift family {p + 4d}. The heuristic count is ≍ log²p
(R268 repair m13: random primes p ≡ 1 (4) give means 13.5, 29.7, 51.0 at p ≈ 1.5·10⁴, 1.5·10⁶, 1.5·10⁸, i.e. ≈ 0.145 log²p,
`logs/review_r268_growth.txt`; the earlier quoted 16 / 20 came from two different sub-populations).
*Attribution (R268 repair M4).* López (arXiv:2404.01508) found that 193 and 2521 are the only primes < 9000 without Type A
(= b = 1) solutions, noted 66529, and conjectured that every prime has a Type A or Type B (= c = 1) solution. Conjecture 2.5 is
the sharpening "b = 1 alone, with exactly these three exceptions", supported by the 10⁸ census. Failure is then a polylog lottery, as for (★), but with
much better constants in range.
(Lemma 2.2 checked: all 3312 D-form hits for p ≡ 1 (4) < 6000 have (w/p) = −1; at all 63 974 levels with (d/p) = −1,
χ_{−4d}(p + 4d) = −1; `logs/s8_genus_checks.txt`.)

## 3. Mandatory (iii): forced windows × the T1 adversary — one parity, two readings

**Lemma 3.1 (PROVED, Jacobi transfer of (J)83 Lemma 1.1).** Let p ≡ 1 (4), q ≡ 3 (4) a prime window, K = (p + q)/4.
(a) (K/p) = (q/p). So q is forced ⟺ K carries an odd number (with multiplicity) of T1-visible primes s (those with (s/p) = −1).
(b) Every cap-0 certificate (u, v) at q (Prop 2.1 of FORCED_WINDOW; level 4uv, uv | K, q | u + v) has (uv/p) = −1. So the level
4uv always contains a visible prime, and p is a non-square mod 4uv — whether or not q is forced.
*Proof.* (a) 4K ≡ q (mod p) gives (K/p) = (q/p). (b) u ≡ −v (mod q) gives (uv/q) = (−v²/q) = −1. Transfer ((J)83: (s/q) = (s/p)
for s | K) gives (uv/p) = −1. ∎ (Checked on all 15 498 cap-0 certificates at prime windows q < 80, p < 2·10⁴: 0 exceptions.)
*Reading — what (iii) asked.* (J)86's dictionary ("usable information sits at primes where p is a non-residue") and (J)64's
forced windows are the same Legendre parity. Forcing at q makes K supply an odd number of visible primes, and every certificate
consumes an odd number of them into its level. The window q itself is never in the level: it is the residue −p mod 4uv. So a
lift routed "through a forced window" is visible at level 4uv by construction, but the forced data (q/p) = −1 only guarantee
that visible primes exist in K. They do not choose (u, v). O257 (NONCONG_LIFTS Thm 1.2, read-only on its branch) needs, for a
determined lift at level M, that p be a non-square mod M — automatically true here — and sufficiency needs *favourable*
witnesses (its §2.4: for p in Mordell classes no complete level exists). So routing through forced windows adds no totality.
The recombination still has to pick the favourable (u, v), which is the B2 event of Prop 2.1. **Verdict (iii): no new lever;
the two channels are identical (PROVED), so neither can rescue the other.**

## 4. Mandatory (iv): positivity × signed slices — the genus wall

Type I side numbers (RT2): f | p² + 4c²d, f ≡ −p (mod 4c|d|); signed slices allow d < 0 (JOINT_BUDGET Remark 1.2).

**Lemma 4.1 (the sign flips the genus condition; PROVED, Jacobi; the χ·s_∞ three-bit law of (J)52 at Type I level).** Let
p ≡ 1 (4), gcd(p, cd) = 1, and f ≥ 1 with f | p² + 4c²d and f ≡ −p (mod 4c|d|). Then
  d > 0 ⟹ (d/p) = −1,   d < 0 ⟹ (|d|/p) = +1.
In particular positive d is never a square (Type I at d = w² is impossible), and the split signed slices d = −w² of JOINT_BUDGET
Remark 1.2 are on the "wrong" side of the wall.
*Proof.* gcd(f, 4cd) = gcd(p, 4cd) = 1. For a prime ℓ | f, ℓ | p² + 4c²d and ℓ ∤ 2cdp, so −d is a square mod ℓ:
χ_D(ℓ) = 1 for the Kronecker character χ_D, D = −4d, of modulus dividing 4|d|. Hence χ_D(f) = 1. But f ≡ −p (mod 4c|d|), so
χ_D(f) = χ_D(−1)χ_D(p) = sign(D)·(D/p). With p ≡ 1 (4), (D/p) = (−d/p) = (d/p). So d > 0 (D < 0): (d/p) = −1; d < 0: (|d|/p) = 1. ∎
(Checked: 1934 positive and 2816 signed Type I points, p < 3000, c < 5, |d| < 30; the only exceptions are the 9 degenerate p | d
cases. R268 repair m6: the reviewer's enumeration over all divisors f, with gcd(p, cd) = 1, gives 4772 positive and 10 787
signed points, 0 exceptions, and 3 to 48 signed points per odd square; the counting convention above was not recorded.)
(At odd squares 9 … 441 there are signed points (2–13 each) and no positive ones.)
**Corollary 4.2 (no reflection preserves |d|; PROVED).** A move from signed Type I points to positive ones that keeps |d|
(or its square class mod p) is impossible: it would have to change (|d|/p) from +1 to −1. Vieta jumping is unavailable
anyway: the Type I equation p(a + b) + c = 4abcd, and 4xyz = p(xy + yz + zx), are linear in each variable, so there is no
single-variable (Vieta-type) involution. (R268 repair m7: the earlier "the only involutions are coordinate permutations" was
false as stated; in reciprocal coordinates the surface is the plane X + Y + Z = 4/p, which has many birational involutions.)
*Reading (Assessment).* Positivity is not an extra constraint layered on a split algebra. It is the genus wall itself. Split
signed points live where |d| is a residue (the T1 side; they exist at odd squares), positive points where d is a non-residue.
A signed→positive transfer must multiply d by a non-residue *and* produce the divisor in the new class — B2 again, plus the
"find a non-residue" step, which is cheap (Burgess/GRH) but unhelpful by itself. **Verdict (iv): closed (PROVED obstruction for
|d|-preserving moves, no Vieta structure).** This makes O254's spark 2 precise and negative.

## 5. Own (v): profinite proximity to the T1 point 1 (EVIDENCE, weak)
AMPLIFY_EXCEPTION Thm 3.2: p ≡ □ (mod L) ⟹ no ET witness with modulus H | L. Every p is ≡ 1 = 1² (mod p − 1), so p − 1's
divisors are always invisible moduli. A large smooth part of p − 1 makes p profinitely close to the T1 point 1, not just to
the square classes. Data: (1) all three b = 1 failures have p − 1 11-smooth (above). (2) p ∈ [10⁴, 4·10⁴]: mean b = 1 / c = 1
counts 16.0 / 19.3 (11-smooth part S < 50), 13.7 / 16.5 (50 ≤ S < 500), 11.3 / 14.5 (S ≥ 500). Most of this is the known
QR-richness effect (s7_lvalue_proxy). (3) A controlled test inside the six Mordell square classes mod 840, p ∈ [10⁶, 3·10⁶],
≈ 700 primes each: class 1 has mean b = 1 count 19.63 against 20.25–20.89 for the other five square classes (a difference of about one
solution; R268 repair m11: standard errors ≈ 0.25 per class, class 1 = 19.63 ± 0.25 vs the pooled other classes 20.59 ± 0.11,
z ≈ 3.5, `logs/review_r268_proximity.txt`), and c = 1 count 23.53 against 23.96–25.10. So proximity to 1 itself, beyond squareness, costs a few
per cent. Label: EVIDENCE (weak); no mechanism claimed.

## 6. Verdict (O258 checkpoint 1)
* (i) Least residue × height-dependent target: one statement in four coordinates (Props 1.2–1.5). Each candidate tool fails at
  an identified hypothesis (§1.7 table). DFI's bounds degrade with a = p unless the box has MN ≳ p (R268 repair M2); for the
  large boxes the obstruction is the O(1)-per-box volume (Lemma 1.6, Assessment part). No route.
* (ii) Support-1 lottery = b = 1 line. Exact duality (Prop 1.3), visibility and forced levels (Lemma 2.2), privacy of large
  primes across j (Lemma 2.3: pigeonhole across j is void). **SHARP (EVIDENCE + CONJECTURE): the b = 1 line fails at exactly
  three primes ≤ 10⁸ (193, 2521, 66529), and b = 1 ∪ c = 1 never fails ≤ 10⁸.** No deterministic mechanism. Any mechanism must be
  4-specific (the k = 8 analogue fails at 131, 241, …) and must use primality (105 fails).
* (iii) Forced windows and the T1-adversary channel are the same Legendre parity (Lemma 3.1). Routing lifts through forced
  windows adds no totality.
* (iv) Positivity is the genus wall (Lemma 4.1). |d|-preserving signed→positive moves are impossible, and there is no Vieta
  structure.
* Overall: no ES progress. New content (R268 repair M4/m8): the MP(p) 2-adic reading of Props 1.2–1.3 (the divisor form of
  Prop 1.3 itself is López 2024, Thm 7), Lemma 2.2, Lemma 2.3, Lemma 3.1(b), Cor 4.2 (Lemma 4.1 is (J)52's three-bit law / the
  ET Prop 1.6 mechanism at Type I level), and the census extension to 10⁸ (López checked b = 1 ∪ c = 1 to 104 729).

## 7. Sparks (not pursued)
1. **Why is b = 1 so much more robust than (★)?** Both are "p + t has a divisor ≡ −1 (mod T)" with (t, T) = (4d, 4d) and
   (j, 4j). In the b = 1 case the forced levels are exactly the non-residues d of p (Lemma 2.2(b)), a p-global set; for (★) the
   parity at level j is a congruence on p mod j. A precise variance comparison of the two counts could explain the gap.
2. A 2-adic random model on MP(p) (§1 reading): b = 1 ∪ c = 1 fails iff every pair with an even coordinate has v₂(x) = 1 and
   v₂(N) ≤ 1. Do the "v₂(N) = 1" near-misses carry Type I or other-type solutions? An exact identity there would add a third
   line.
3. Extend the b = 1 census beyond 10⁸ with a segmented sieve, and test smooth-(p − 1) primes up to 10¹⁵ directly with bounded
   windows (cheap: about 10⁵ such primes).

## 8. Mandatory (vi) (added by the parent): is the 4-specific step a numerator-size inequality? (memo s8_numerator_size_screen)
For 4 | k, k/n = 1/x + 1/y + 1/z ⟺ 4/n = Σ 1/((k/4)x). So **the numerator-k model is ES restricted to solutions with
(k/4) | gcd(x, y, z)**; in ET coordinates the k-witnesses are the 4-witnesses with (k/4) | d (PROVED, trivial; surely
classical). At a fixed slice the k-condition differs from k = 4 only at the primes of k/4, and the size bound e ≤ a + b is
k-free. O257's inequality b₀(k − 4/g) ≤ 3 at x_{ℓ,2} is therefore the conjunction of a local condition (x ≡ 1 at the primes of
k forces e ≡ −1 (mod kab₀)) with that k-free size bound. 2-adically: the k = 4 witnesses there (R268 repair m9: not only Mordell's
(1, 6, e = 7) of Type II and Type I at ℓ = 3, but also (II, 1, 5, c = 2, e = 3) and (I, 2, 5, c = 1, e = 7) at ℓ = 5) have
d = 8/24, 8/24, 4/20, 8/40 in the 2-adic integers (x = 1): all 2-adic units, so d is odd. (J)57's 2-adic bit law and O257's size inequality are thus two readings of one
step — "d may be odd" — and neither is reciprocity. Of the screened arguments, (J)41 has no 4-specific step (its thresholds
compare p with M), and Mordell's identities use completeness (a density count). A "k-uniform + threshold P₀(k)" organisation is
strictly stronger than ES (8/p ⟹ 4/p), so it buys nothing (R268 repair m10: "at least as strong as ES"; "strictly" is unproved). In the step form, the model
exceptions (R268 repair m10: exactly 11, 17, 131, 241 among primes 5 ≤ p < 8000 — every prime with 8/p unsolvable lies among
the 34 two-line failures, and only these four of them have 8/p unsolvable; at them no solution of 4/p has all three
denominators even, `s8_even_denominators.py`) say a proof must spend its 4-specific step on v₂ of the
cofactor d. Near the T1 point this is the 2-adic shape of §1 (b = 1 ∪ c = 1 fails only where every relevant v₂ ≤ 1).
`s8_xlr_points.py` generalises Thm 2.6 to x_{ℓ,r}: the covered non-residues are those whose CRT window is small
(r ≡ −small), and coverage thins quickly in k. Assessment: not sharp; no new lever.
**Scope (R268 repair M3, following R267 D-M1 on NONCONG_LIFTS).** Thm 2.6 and the x_{ℓ,r} screen concern FIXED-SLICE witness
classes only. With ET's one-parameter polynomial families, k = 8 covers x_{3,2} (II-3 family, n ≡ 281 (mod 504); reviewer spot
check: 8/n solvable for n = 281 + 504j, j ≤ 11, least x = (n + 7)/8) and x_{5,2}, and k = 4 covers x_{11,2}. So the "4 vs every
k ≥ 8 separation at x_{ℓ,2}" and the reading "(J)57's bit law and O257's size inequality are two readings of one step" hold
for slice classes only; at the level of profinite points they are unsupported. The (k/4) | d dictionary is unaffected. The
identification with (J)57's v₂-exactly-2 evidence is an Assessment, not a proved equivalence (R268 repair m10).
