# FOREST_DEEP_FABLE — a certificate edge in every forest F_p: what is forced, what is not (z48, slug forestfable)

**ES is not solved here. No infinite case of ES for primes is claimed.** Labels as in DISCOVERIES.md (PROVED / CONDITIONAL on … /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment). Scripts `scripts/z48_forestfable_*`, data `data/z48_forestfable/`.
Target of the task: prove that for every large prime p ≡ 1 (mod 4) the forest F_p has a certificate edge (hence ES(p)),
ideally with H₄(p) ≤ polylog(p), allowing OAI-003 (quasi-RH 7/8) or GRH as labelled hypotheses.

## 0. Summary (Assessment unless labelled)

1. **The converse "bichromatic ⟹ certificate" was already a theorem** (DEDEKIND_ES Thm 4.5 via Rademacher's congruence and a
   512-cell check, plus LOWER_TAIL_ASTRA Lemma 2.2). The brief listed it as unproved; it is not. §1 gives a self-contained
   **hand proof by quadratic reciprocity alone** (four cases, no Dedekind sums, no computer), valid for every odd n ≡ 1 (mod 4)
   with Jacobi symbols; CERTIFIED on all 34 580 998 edges at the 332 180 primes p ≡ 1 (4) below 10⁷ and 87.6 million edges
   at the 719 781 primes p ≡ 1 (24) below 10⁸ (Theorem A).
2. **The colour of an edge is a function of its two endpoints mod 8 (Theorem B, PROVED).** For p ≡ 1 (mod 8) an edge {u, v}
   is monochromatic iff {u mod 8, v mod 8} ∈ {{1,1},{1,5},{5,5},{1,2},{5,6},{2,3},{3,6}}. Hence **every edge with an
   endpoint ≡ 0 (mod 4) or ≡ −p (mod 8) is a certificate**, whatever the colours. This is the vertex-coordinate form of a
   2-adic law the campaign already had in level coordinates (Legendre levels t′ ≡ −p (8), BRAINSTORM/z1_legendre_levels)
   and in frieze coordinates (opposite vertex o ≡ 7 (8), BRAINSTORM/y5_transport_is_ptolemy); Lemma P collects all three.
3. **Consequence (Corollary C, PROVED): for prime p ≡ 1 (mod 8), ES(p) holds as soon as p + v has a divisor ≡ −1 (mod v)
   for some v ≡ 0 (mod 4) or v ≡ 7 (mod 8), with explicit unit fractions.** The first family is López's Type-A line; the
   second is its *twin*. Both are sign-free divisor conditions on one shifted integer; both are T1-exact (Theorem E: at
   odd squares m² the integer m² + v never has such a divisor). CERTIFIED: López's line alone fails at exactly 193, 2521,
   66529 and the twin alone only at 3361 among p ≡ 1 (24) ≤ 10⁸; **the union never fails there**, and the least such
   vertex is ≤ 116 for all p ≡ 1 (24) ≤ 10⁸ (attained at 3361 and 76441). This is a two-line target of the same kind as
   (★) ∪ López (SYNTHESIS_SPARKS9 Cor 1.2), with both halves on the same integers p + v; it is not a theorem.
4. **Covering form (PROVED, §3).** ES₅(p) ⟺ p mod A ∈ G_A for some A ≥ 2, where G_A ⊂ ℤ/A is the explicit p-independent set
   {−d : d | A+1, d < A, (−d/A_odd) = −1}. The least QNR, GRH, quasi-RH enter only through the *colour half* of G_A; the
   *shadow half* {−d : d | A+1} is where B1 lives: p ≡ 1 (mod lcm(1..X)) is uncovered by every A ≤ X (so A_min, H₄ ≫ log p
   i.o. by Linnik, elementary). EVIDENCE: the uncovered density decays like exp(−(log X)²/4) (sieve dimension ≍ log X).
5. **No mechanism forcing a bichromatic component was found, and §5 says exactly why each candidate stops.** The discrete
   IVT needs two opposite-coloured vertices in one component; every pair of candidate vertices (1 and a QNR; two small
   vertices; the largest component; a QNR vertex v ≡ 7 (8) found by GRH/003) is joined only through divisor events of
   *one* shifted integer p + v in *one* class mod v — B2 in its cleanest form. Under 003 the least QNR r(p) ≪ log⁸p is a
   QNR *vertex*; it attaches to a parent with CRT density (log r)/r, and 2521-type primes (r isolated) exist i.o. under
   Dickson (ASTRA Thm 5.1). Nothing in 003/GRH controls the divisors of p + v. The exact gap is stated in §6.
6. **Verdict: PARTIAL (clean negative with structural by-products). Promise for the stated target: 1/5.** The target
   "H₄(p) ≤ polylog(p) for all p" remains CONJECTURE (EVIDENCE to 10⁸: H₄ ≤ 1.40 (log p)²; u_min ≤ 25; the least vertex of
   the sign-free union ≤ 116). Everything new here is dictionary and census; the lower tail is untouched.

## 1. Setting and the exact dictionary

Throughout p is a prime, p ≡ 1 (mod 4); F_p has vertices 1, …, p+2 and the edge {u, v} (u ≠ v) iff uv | p + u + v. For an
edge put t = (p+u+v)/(uv), so p = tuv − u − v, and the two *numerators* A := tu − 1 = (p+u)/v, A* := tv − 1 = (p+v)/u, with
AA* = tp + 1. The five *pentagon quantities* of the edge are (t, u, v, A, A*) (= (m, c, s, h, h′) of FRIEZE_ES). Colour
χ(x) = (x/p). Facts used below (all PROVED in the repo: LOWER_TAIL_ASTRA Lemma 2.1–2.2, FOREST_H4 §1): F_p is a forest;
gcd(u, v) = 1 for every edge with p > 3; v | p + u and u | p + v; A ≡ −1 (mod u), A* ≡ −1 (mod v); A ≡ u/v (mod p), so
χ(u)χ(v) = (A/p) = (A*/p); the smaller endpoint satisfies (u − 1)² ≤ p + 1; vertex 1 is adjacent exactly to the divisors
≥ 2 of p + 1; every vertex above √(p+1) + 1 is a leaf. A *certificate* is an edge with 4 dividing one of t, u, v, A, A*;
the five explicit solutions are those of the PR-B note (§5 item 4) and DEDEKIND_ES Thm 4.5.

**Theorem A (bichromatic ⟺ certificate; PROVED, elementary).** Let n ≡ 1 (mod 4) be odd and {u, v} an edge of F_n with
gcd(uv, n) = 1 and gcd(u, v) = 1 (automatic at primes n = p > 3). Then, with Jacobi symbols,
  (uv/n) = −1  ⟺  4 | t or 4 | u or 4 | v or 4 | tu − 1 or 4 | tv − 1.

*Proof.* Write u = 2^a u′, v = 2^b v′ with u′, v′ odd; at most one of a, b is positive. For odd x, y put
ε(x, y) := (−1)^{(x−1)/2 + (y−1)/2 + (x−1)(y−1)/4}, which is −1 iff x ≡ 3 or y ≡ 3 (mod 4). Since n ≡ 1 (mod 4), Jacobi
reciprocity gives (u′/n) = (n/u′), and u′ | n + v gives (n/u′) = (−v/u′); likewise for v′. Hence
  (uv/n) = (2/n)^{a+b} (−1/u′)(−1/v′)(v/u′)(u/v′) = (2/n)^{a+b} (2/u′)^b (2/v′)^a ε(u′, v′).   (1.1)
*Case 1: u, v odd.* (uv/n) = ε(u, v). If u ≡ v ≡ 1 (4): n + u + v ≡ 3, uv ≡ 1, so t ≡ 3 (mod 4) and tu − 1 ≡ tv − 1 ≡ 2:
no slot, symbol +1. If u ≡ 1, v ≡ 3: n + u + v ≡ 1, uv ≡ 3, t ≡ 3, tv − 1 ≡ 0 (mod 4): slot, symbol −1. u ≡ 3, v ≡ 1
is symmetric (slot tu − 1); u ≡ v ≡ 3: n + u + v ≡ 3, uv ≡ 1, t ≡ 3, tu − 1 ≡ 0: slot, symbol −1.
*Case 2: 4 | u (a ≥ 2), v odd.* The slot 4 | u holds; we show the symbol is −1. From u | n + v, v ≡ −n ≡ 3 (mod 4), so
ε(u′, v) = −1. If a = 2 the 2-power factors are squares; if a ≥ 3 then n ≡ −v (mod 8) and (2/n) = (2/−v) = (2/v), so
(2/n)^a (2/v)^a = 1. Hence (uv/n) = −1. The case 4 | v is symmetric.
*Case 3: u = 2u′ (a = 1), v odd.* Here 4 ∤ u, 4 ∤ v, tu − 1 is odd, so the slots are 4 | t and 4 | tv − 1, and (1.1) reads
(uv/n) = (2/n)(2/v) ε(u′, v). Reduce n = tuv − u − v = 2tu′v − 2u′ − v modulo 8 and use n ≡ 1 (mod 4).
 (i) t ≡ 0 (mod 4): n ≡ −2u′ − v (mod 8), and n ≡ 1 (mod 4) forces v ≡ 1 (mod 4). For (u′ mod 4, v mod 8) =
   (1,1), (3,1), (1,5), (3,5) one gets n ≡ 5, 1, 1, 5 (mod 8), and (2/n)(2/v)ε = (−1)(1)(1), (1)(1)(−1), (1)(−1)(1),
   (−1)(−1)(−1), i.e. −1 in all four cases; the slot 4 | t holds.
 (ii) t ≡ 2 (mod 4): n ≡ 4 − 2u′ − v (mod 8), again v ≡ 1 (mod 4); the same four cases give n ≡ 1, 5, 5, 1 (mod 8) and
   (2/n)(2/v)ε = +1 in each; no slot (tv ≡ 2 (mod 4)).
 (iii) t odd: n ≡ 2u′(tv − 1) − v (mod 8) with tv − 1 even, so n ≡ 1 (mod 4) forces v ≡ 3 (mod 4), ε(u′, v) = −1, and the
   slot is 4 | tv − 1 ⟺ t ≡ 3 (mod 4). If t ≡ 3: tv ≡ 1 (mod 4), so n ≡ −v (mod 8), (2/n) = (2/v), symbol −1, slot holds.
   If t ≡ 1: tv ≡ 3 (mod 4), n ≡ 4 − v (mod 8); v ≡ 3 gives n ≡ 1, (2/n)(2/v)ε = (1)(−1)(−1) = +1; v ≡ 7 gives n ≡ 5,
   (−1)(1)(−1) = +1; no slot.
*Case 4: v even, u odd* is Case 3 with the roles of u and v exchanged (both (1.1) and the slot set are symmetric). ∎

CERTIFIED (`scripts/z48_forestfable_converse.py`): formula (1.1) evaluated from residues mod 8 agrees with the slot
predicate on all 160 admissible cells of (ℤ/8)³, and Euler's criterion agrees with the slot predicate on all 10 307 edges
with p < 5000; the C scan (`z48_forestfable_scan.c`) reports `viol_slot = 0` on every edge to 10⁷ (all p ≡ 1 (4)) and to
10⁸ (p ≡ 1 (24)). The edge totals to 10⁶ (3 028 437 edges, 1 964 805 bichromatic at 39 175 primes) reproduce the
LOWER_TAIL_ASTRA census exactly with an independent implementation (edges enumerated by the smaller endpoint, divisors of
p + u from a smallest-prime-factor sieve).

## 2. The 2-adic classification of edges

**Theorem B (endpoint classes; PROVED).** Let p ≡ 1 (mod 8) be prime and {u, v} an edge of F_p. Then {u, v} is
monochromatic iff the unordered pair {u mod 8, v mod 8} is one of
  {1,1}, {1,5}, {5,5}, {1,2}, {5,6}, {2,3}, {3,6}.
For p ≡ 5 (mod 8) the list is {1,1}, {1,5}, {5,5}, {1,6}, {2,5}, {2,7}, {6,7}. In particular, for every prime p ≡ 1 (4):
**every edge with an endpoint ≡ 0 (mod 4), and every edge with an endpoint ≡ −p (mod 8), is a certificate.**

*Proof.* Read off the cases of Theorem A. Case 1: monochromatic iff u ≡ v ≡ 1 (mod 4). Case 2: never. Case 3 (u ≡ 2
(mod 4), v odd), p ≡ 1 (mod 8): if v ≡ 1 (mod 4) then t is even and p + u + v ≡ tuv (mod 8) decides t mod 4: the pairs
(u, v) ≡ (2,1), (6,5) (mod 8) give p + u + v ≡ 4, so t ≡ 2 (mod 4) and the edge is monochromatic; (2,5), (6,1) give
p + u + v ≡ 0 (mod 8), t ≡ 0 (mod 4), certificate. If v ≡ 3 (mod 4) then t is odd and p ≡ −v or 4 − v (mod 8) according
as t ≡ 3 or 1 (mod 4); with p ≡ 1 (mod 8) this is v ≡ 7 (t ≡ 3, certificate) or v ≡ 3 (t ≡ 1, monochromatic). The
p ≡ 5 (mod 8) list is obtained in the same way (v ≡ 3 ↔ 7, and the parity of (p + u + v)/4 flips). ∎

CERTIFIED: the C scan evaluates this predicate (both p mod 8 classes) on every edge: `viol_classB = 0` to 10⁷ and 10⁸.
The numbers of monochromatic edges to 10⁷ in the three classes (both ≡ 1 (4); {1,2}/{5,6}; {2,3}/{3,6}) are
574 553 / 1 284 352 / 1 198 761 for p ≡ 1 (24), 6 257 933 / 13 779 852 / 12 933 385 for p ≡ 1 (24) ≤ 10⁸ — all three
classes are populated at comparable rates, so no class is "accidental".

**Lemma P (pentagon classes; PROVED).** For a prime p ≡ 1 (4) and an edge with pentagon quantities (t, u, v, A, A*), write
t′ for t with all factors 4 removed. The edge is a certificate whenever
 (i) one of t, u, v, A, A* is ≡ 0 (mod 4) [the five slots themselves];
 (ii) u, v or t′ is ≡ −p (mod 8);
 (iii) A or A* is ≡ 7 (mod 8).
*Proof.* (i) is the definition. (ii) for u, v is Theorem B; for t′ it is BRAINSTORM/z1_legendre_levels Prop 1 (Legendre
levels), and also follows from (A/p) = (−t/A) for odd A (since A | tp + 1 gives p ≡ −t⁻¹ (mod A)) by the computation in
(iii) with t in place of u; for even A the factor (2/p)^{v₂(A)} is why the condition is t′ ≡ −p rather than 7 (mod 8).
(iii) A ≡ 7 (mod 8) is odd, A ≡ −1 (mod u), A | p + u. So (A/p) = (p/A) = (−u/A) = −(u/A) (as (−1/A) = −1), and with
u = 2^a u′: (u/A) = (2/A)^a (u′/A) = (u′/A) = (A/u′)(−1)^{(A−1)(u′−1)/4} = (−1/u′)(−1/u′) = 1 (using (2/A) = 1, A ≡ −1
(mod u′), A ≡ 3 (mod 4)). Hence (A/p) = −1, and Theorem A gives a slot. Same for A* with v. ∎
CERTIFIED (`scripts/z48_forestfable_pentagon.py`, `pentagon_30000.txt`; all 71 036 edges at the primes p ≡ 1 (4) below 30 000): for each position q ∈ {t′, u, v, A, A*} and each p mod 8, the classes
q ≡ 0 (4) are all-certificate, q ≡ −p (8) is all-certificate for u, v, t′, and 7 (8) is all-certificate for A, A* in both
p-classes, while the remaining classes (e.g. u ≡ 3 (8) at p ≡ 1 (8), A ≡ 3 (8)) are mixed. This is y5's law "certificate
⟺ the opposite vertex of the even edge is ≡ 7 (8)" read position by position; nothing here is new as a 2-adic fact.

**Corollary C (two sign-free vertex lines; PROVED, explicit).** Let p ≡ 1 (mod 8) be prime, v ≥ 4 with v ≡ 0 (mod 4) or
v ≡ 7 (mod 8), and suppose A | p + v with A ≡ −1 (mod v), 1 < A < p + v. Put y = (p + v)/A and t = (A + 1)/v. Then {v, y}
is a certificate edge of F_p, and explicitly:
 * if v = 4d: 4/p = 1/(d·A*) + 1/(ptd) + 1/(ptd·A*) with A* = (p + y)/v = ty − 1 (slot 4 | v);
 * if v ≡ 7 (mod 8): p + v ≡ 0 (mod 8) and A·y = p + v, so 4 | A or 4 | y. If y = 4d: 4/p = 1/(dA) + 1/(ptd) + 1/(ptdA)
   (slot 4 | y). Otherwise 4 | A = tv − 1 =: 4m and 4/p = 1/(my) + 1/(my·A*) + 1/(pm·A*) with A* = ty − 1 (slot 4 | tv − 1).
*Proof.* y ≡ −p (mod v) because A ≡ −1 (mod v) and Ay = p + v; so {v, y} is an edge (v | p + y and y | p + v, coprime).
Theorem B makes it a certificate; the slot bookkeeping is as stated (for v ≡ 7 (8): v₂(A) + v₂(y) = v₂(p + v) ≥ 3, and if
v₂(y) ≤ 1 then v₂(A) ≥ 2). The three identities are the standard slot formulas; e.g. 1/(dA) + 1/(ptd) + 1/(ptdA) =
(pt + A + 1)/(ptdA) = t(p + v)/(ptdA) = y/(pd) = 4/p. ∎
(For p ≡ 5 (mod 8) replace 7 by 3.) The first bullet is López's Type-A line "p + 4d has a divisor ≡ −1 (mod 4d)"
(SYNTHESIS_SPARKS8, B1_LINE); the second is new as a stated line, although it is contained in y5's position P_c.

**Theorem E (the twin line is T1-exact; PROVED, elementary).** Let m be odd, v ≡ 7 (mod 8) or v ≡ 0 (mod 4), gcd(v, m) = 1.
Then m² + v has no divisor A ≡ −1 (mod v) with A > 1.
*Proof.* Suppose A | m² + v, A ≡ −1 (mod v), A = 2^a A′ with A′ odd. If A′ = 1 then 2^a ≡ −1 (mod v), so (2/v)^a = (−1/v);
for v ≡ 7 (8) this is 1 = −1, and for 4 | v it is impossible (−1 is odd). So A′ > 1, and gcd(A′, m) = 1 (a common prime
would divide v). From A′ | m² + v: (−v/A′) = (m²/A′) = +1. From A′ ≡ −2^{−a} (mod v) and reciprocity (v ≡ 3 (mod 4) when
v ≡ 7 (8)): (−v/A′) = (−1/A′)(A′/v)(−1)^{(A′−1)(v−1)/4} = (A′/v) = (−1/v)(2/v)^{−a} = −1, contradiction. For 4 | v the known
argument (FRONTIER B5: m² + u has no divisor ≡ −1 (mod 4u)) applies. ∎
CERTIFIED: at the 499 odd squares 9 ≤ m² ≤ 10⁶ (17 372 edges, as in the Astra census), no vertex ≡ 0 (4) or ≡ 7 (8) is
non-isolated in F_{m²} (`scan_squares_1e6.txt`, columns E0, E7; this covers non-coprime v as well, which Theorem E does not
claim); directly (`z48_forestfable_thmE.py`), 0 counterexamples over all odd m ≤ 1001, v ≤ 3000. The same proof with u in
place of v shows that the numerator class A ≡ 7 (8) of Lemma P(iii) is T1-exact (same script, 0 counterexamples).

**Lemma 2.3 (pure-character lines; PROVED).** For prime p ≡ 1 (mod 24), the line u (edges with smaller endpoint u) carries a
certificate iff: u = 1: (p+1)/2 has a prime factor ≡ 3 (mod 4); u = 2: p + 2 has a prime factor ≡ 5 or 7 (mod 8); u = 3:
(p+3)/4 has a prime factor ≡ 2 (mod 3); u = 4: p + 4 has a prime factor ≡ 3 (mod 4); u = 7: the odd part of p + 7 has a
prime factor that is a quadratic non-residue mod 7; u = 15: the odd part of p + 15 has a prime factor ℓ with (ℓ/3)(ℓ/5) = −1.
*Proof.* u = 1, 2, 3: the children of u are the divisors v of p + u in the class −p (mod u); by Theorem B the edge is a
certificate iff v mod 8 ∉ {1, 5, 2} (u = 1), ∉ {1, 3} (u = 2), ∉ {2, 6} (u = 3). Writing p + 1 = 2m, p + 2 = 3m′ (odd),
p + 3 = 4m″ (m″ odd), the admissible v are d, 2d (d | m), resp. odd divisors of p + 2, resp. d, 2d, 4d (d | m″, d ≡ 2 (3) for
d, 4d and d ≡ 1 (3) for 2d), and the condition becomes "some divisor of m is ≡ 3 (mod 4)", "some divisor of p + 2 is ≡ 5, 7
(mod 8)", "some divisor of m″ is ≡ 2 (mod 3)"; since the complementary classes {1 (4)}, {1, 3 (8)}, {1 (3)} are closed under
multiplication, this holds iff a prime factor lies in the forbidden class. u = 4, 7, 15: by Corollary C the line certifies iff
p + u has a divisor ≡ −1 (mod u); for u = 4 this is a divisor ≡ 3 (mod 4) of the odd number p + 4; for u = 7, 15 the divisors
are 2^a d with d | odd part and 0 ≤ a ≤ v₂(p + u) ≥ 3, and since ord_u(2) ≤ 4 the classes 2^{−a} exhaust ⟨2⟩, which is the
kernel of the Kronecker character χ_{−u} (index 2, as ord₇(2) = 3, ord₁₅(2) = 4); so a divisor ≡ −1 exists iff some d | odd
part has χ_{−u}(d) = −1 iff some prime factor has. ∎
So each of these lines fails exactly when a shifted integer is (up to a fixed small factor) a norm from an imaginary quadratic
order of discriminant −4, −8, −3, −4, −7, −15 — a character condition on one integer, with failure "probability"
≍ (log p)^{−1/2}; CERTIFIED failure rates 25–45 % each (§4.2). Lines u ≥ 5 in the classes 1, 2, 3, 5, 6 (mod 8) and the
López/twin lines with ord_u(2) < φ(u)/2 are genuine residue-class (not character) conditions.

*Numerator-8 control.* The analogue of López's line for 8/n is "some vertex ≡ 0 (mod 8) is non-isolated" (SYNTHESIS_SPARKS9
Cor 1.2, b = 1 line); CERTIFIED: at n = 17, 241 (8/n unsolvable, Lean L9901) no vertex ≡ 0 (8) is non-isolated, while the
4/n lines of Corollary C fire (E0 = E7 = 1). The twin line has **no** numerator-8 analogue: its proof uses (2/v) = (2/p)
through the Legendre symbol (v/p), which certifies 4/p (Theorem A) and nothing for 8/p. So Corollary C is 4-specific in the
sense of FRONTIER §4 line 2.

## 3. The covering form, and what GRH / quasi-RH can see of it

**Proposition 3.1 (covering form; PROVED).** For a prime p ≡ 1 (mod 8):
  ES₅(p) ⟺ ∃ A ≥ 2 with p mod A ∈ G_A,   G_A := {−d (mod A) : d | A + 1, 1 ≤ d < A, (−d/A_odd) = −1},
where A_odd is the odd part of A. (For p ≡ 5 (mod 8) multiply the symbol by (−1)^{v₂(A)}.)
*Proof.* A bichromatic edge {u, v} of level t ≥ 2 has numerator A = tu − 1 > u with A | p + u, so u is the least positive
residue of −p modulo A and u | A + 1 = tu; its colour is (A/p) = (2/p)^{v₂(A)}(p/A_odd) = (−d/A_odd) with d = u (Jacobi
reciprocity, p ≡ 1 (4), p ≡ −d (mod A_odd)). The level-1 edges {d+1, (p+1)/d + 1} have A = d | p + 1, i.e. the residue
p ≡ −1 (mod A), already produced by the edge {1, (p+1)/A} (the elements d = 1 and d = A + 1 of D(A+1) give the same residue).
Conversely p ≡ −d (mod A) with d | A + 1, d < A, gives the edge {d, (p+d)/A} of level t = (A+1)/d ≥ 2, whose colour is
(A/p). ∎
This is LOWER_TAIL_FABLE §2.8 (the Legendre/HJ form) made p-independent on the modulus side: the sets G_A do not depend
on p. Explicitly (PROVED by the computation in Lemma P): for odd A ≡ 7 (mod 8), G_A = {−d : d | A+1, d < A} is the
*full* divisor shadow; for odd A ≡ 3 (mod 8) it is the sub-shadow with v₂(d) even; for odd A ≡ 1 (mod 4) it is the d with
(2/A)^{v₂(d)}(−1/d_odd) = −1; for even A the symbol (−d/A_odd) with d odd. Small cases: G₂ = G₃ = G₄ = ∅ at p ≡ 1 (24),
G₅ = {2, 3}, G₇ = {3, 5, 6}, G₉ = ∅ (squares never certify), G₁₁ = {7, 8, 10}, G₁₃ = {7, 11}, G₁₅ = {7, 11, 13, 14}:
Mordell's classes mod 5 and 7 are exactly A = 5, 7 (`cover.txt` lists G_A for A ≤ 40).

**Proposition 3.2 (B1 and Linnik in covering language; PROVED).** (a) For every X, the class p ≡ 1 (mod lcm(8, 1, …, X)) is
disjoint from ∪_{A ≤ X} {p : p mod A ∈ G_A}; thus no finite part of the covering covers all primes. (b) Consequently, for
every X there are primes p ≡ 1 (24) with A_min(p) > X and H₄(p) > X, and by Linnik's theorem such p exist below
lcm(1..X)^{L} ≤ e^{C X}; hence A_min(p) ≥ c log p and H₄(p) ≥ c log p for infinitely many p, unconditionally. (The
Graham–Ringrose transfer in FOREST_H4 gives the stronger H₄ ≫ log p log log log p i.o.; (b) is only elementary.)
*Proof.* (a) p ≡ 1 (mod A) lies in G_A iff −d ≡ 1 (mod A) for some d | A + 1, d < A, i.e. d = A − 1 | A + 1, i.e. A ∈ {2, 3},
and G₂ = G₃ = ∅ for p ≡ 1 (24). (b) For p ≡ 1 (mod lcm(1..X)) and u < v ≤ X: v | p + u ⟺ v = u + 1, and then u | p + v
⟺ u | 2, so the only edges inside [1, X] are {1, 2}, {2, 3}, both monochromatic. ∎

**What the hypotheses can see.** Write G_A = S_A ∩ Q_A with S_A := {−d : d | A+1, d < A} (the *shadow*, p-independent and
sign-free) and Q_A := {r : (r/A_odd)(2/p)^{v₂(A)} = −1} (the *colour*, half of (ℤ/A)^×). GRH and OAI-003 are statements about
characters: they locate A with p mod A ∈ Q_A (a QNR modulus A ≤ (log p)² resp. (log p)⁸), and even a prime A ≡ 7 (8) that
is a QNR mod p (fixed-density detector). They say nothing about p mod A ∈ S_A, which is the statement "A | p + d for some
d | A + 1", i.e. a divisor of the single integer p + d in the class −1 (mod d). For the sign-free lines of Corollary C the
colour half is *automatic* (G_A ⊇ S_A ∩ {A ≡ 7 (8)} etc.), so there the hypotheses contribute nothing at all. This is
checklist line 9 ("class, not parity") in its sharpest form: the quadratic layer of every G_A is free, the shadow layer is B2.

**EVIDENCE (the sieve dimension of the covering; `z48_forestfable_cover.py`, `cover.txt`).** Let δ_A(X) be the density of
classes p mod lcm(8, 1..X), p ≡ 1 (24), coprime to lcm, not covered by any A ≤ X (exact enumeration for X ≤ 18, 10⁵ random
classes beyond). Then
  X = 8, 16, 32, 64, 128, 256, 400:  −log δ_A(X) = 1.38, 1.92, 2.94, 4.10, 5.64, 7.25, 8.57;  (log X)²/4 = 1.08, 1.92, 3.00, 4.32, 5.89, 7.69, 8.97,
while the first-moment sieve sum s(X) = Σ_{A ≤ X} P(p mod A ∈ G_A) is 1.0, 2.1, 4.0, 6.2, 9.0, 12.4, 14.8 (strong positive
dependence between A and its multiples). So the covering has *superlinear sieve dimension* — the expected number of hits
below X grows like (log X)²/4 — and the random-class heuristic predicts P(A_min(p) > X) ≈ exp(−(log X)²/4), i.e. an extreme
scale A_min ≲ exp(2√log p). CERTIFIED to 10⁸ (p ≡ 1 (24)): max A_min = 1214 at p = 5 516 281, max A_min/(log p)² = 5.04 (so A_min is far below exp(2√log p) ≈ 5·10³
at that height, consistent with the heuristic but not a test of it).
For comparison the endpoint truncation (FOREST_H4 Prop 5.1) has δ(16) = 0.135 and the H₄ extremes are ≤ 1.40 (log p)².
Assessment: the two truncations are different coordinates of one lottery; neither law is a theorem, and the (log X)²/4
fit is a fit, not a derivation.

## 4. Census (CERTIFIED computations; EVIDENCE for every trend)

`scripts/z48_forestfable_scan.c` enumerates every edge of F_p by its smaller endpoint u ≤ √(p+1)+2 (divisors of p + u in the
class −p (mod u) from a smallest-prime-factor sieve; the edge predicate uv | p + u + v is re-checked on every candidate),
computes colours by the Jacobi algorithm, the five-slot predicate, Theorem B's predicate, components by union–find over the
non-isolated vertices, and per-prime statistics: r (least QNR), W (edges), B (bichromatic edges), H₄, u_min (least smaller
endpoint of a bichromatic edge), t_min, A_min, v07min (least non-isolated vertex ≡ 0 (4) or 7 (8)), ℓ_min (least prime
numerator of a bichromatic edge), family flags and word counts, component data. Runs: all p ≡ 1 (4) ≤ 10⁷ (40 s), all p ≡ 1
(24) ≤ 10⁸ (13 min), odd squares ≤ 10⁶, and the explicit list 17, 241, 193, 2521, 3361. Memory: 0.4 GB (sieve to 10⁸).
`z48_forestfable_analyze.py` produces `analysis_*.txt`; `z48_forestfable_show.py p` prints one forest.

**4.1 Dictionary checks.** `viol_slot = viol_classB = 0` on all 34 580 998 edges (p ≡ 1 (4) ≤ 10⁷) and all 87 575 674 edges
(p ≡ 1 (24) ≤ 10⁸). No prime has B = 0 (ES₅ holds throughout; not new).

**4.2 Which sign-free sub-families fail, and how often (p ≡ 1 (24)).**

| family (all words in it are certificates) | fails ≤ 10⁷ (82 887 primes) | fails ≤ 10⁸ (719 781 primes) | first failures | mean words/(log p)² |
|---|---:|---:|---|---:|
| endpoint ≡ 0 (4) [López, both orientations] | 3 | 3 | 193, 2521, 66529 | — |
| endpoint ≡ 7 (8) [twin] | 1 | 1 | 3361 | — |
| **endpoint ≡ 0 (4) or 7 (8)** (Cor C) | **0** | **0** | — | 0.18 |
| coordinate t, u or v ≡ 0 (4) [(★) ∪ López, SPARKS9 Cor 1.2] | 0 | 0 | — | 0.17 |
| Legendre level t′ ≡ 7 (8) [z1] | 10 (p ≡ 1 (8)) | 10 | 73, 1201, 1489, 9649, 21169, 23041, 44641, 1105441, 1911121, 2922529 | 0.08 |
| numerator A or A* ≡ 0 (4) or 7 (8) [y5 P_h + Type I] | 0 | 0 | — | 0.24 |
| endpoint ≡ 3 (8) with partner ≢ 2 (4) | 54 | 59 | 193, 313, 1201, … | — |
| both endpoints odd, not both ≡ 1 (4) | 147 | 177 | 73, 193, 313, 409, … | — |
| the six pure-character lines u ∈ {1,2,3,4,7,15} together | 898 | 5 281 | 1201, 3889, 5209, 9601, … | — |
| … plus the pure levels t ∈ {2,3,4,7,15} | 59 | 332 | 83449, 121081, … | — |
| prime numerator (ℓ_min < ∞) | 0 | 0 | — | — |
| all bichromatic edges | 0 | 0 | — | 0.25–0.28 |

(The Legendre-level failures ≤ 10⁸ extend z1's seven ≤ 10⁶; the family counts are means over the last 20 % of primes ≤ 10⁸.) Each single pure line fails at 25–45 % of
primes (a character condition on one shifted integer fails with probability ≍ (log p)^{−1/2}, but the constants are large);
the one-residue-class families fail rarely; the unions in bold never fail in range. Assessment (heuristic only): a family
whose expected number of *independent* units (lines or levels carrying a word) grows like c (log p)² has failure probability
≈ exp(−c′(log p)²), summable, so only finitely many failures are expected — this is why López, (★), the twin and the Legendre
levels each have a short finite failure list and their pairwise unions have none; the prime-numerator family has ≍ log p
units (Titchmarsh: Σ_{ℓ ≤ X} τ(ℓ+1) ~ 1.94 X, so its sieve sum is ≈ 0.97 log X) and is *critical*: EVIDENCE at p ≡ 1 (24)
≤ 10⁸, P(ℓ_min > X) = 2.5·10⁻², 4.4·10⁻³, 8.9·10⁻⁴, 8.5·10⁻⁵, 1.1·10⁻⁵ for X = 64, 256, 10³, 10⁴, 10⁵ (local exponent
1.25 → 0.9, i.e. ≈ X⁻¹; max ℓ_min = 1 386 179 at p = 98 418 601), so it should fail infinitely often but has not yet. None of this is a mechanism; it is the (★)-type lottery bookkeeping of SYNTHESIS_SPARKS9 §3 in new coordinates.

**4.3 Minima.** Over p ≡ 1 (24) ≤ 10⁸: max H₄/(log p)² = 1.391 (p = 27 344 521, H₄ = 408, r = 11); max u_min = 25
(p = 78 168 721); max t_min = 36 (p = 26 017 489); max v07min = 116, attained at p = 3361 and p = 76 441 (P(v07min > 64) =
2.6·10⁻⁵, 19 primes, none above 116); u_min ≤ 3 for 93 % and ≤ 16 for 99.99 % of primes. The hard primes:

| p | r | W | B | H₄ | u_min | t_min | A_min | ≡0(4) | ≡7(8) | comp(1) bichromatic | #components (bichromatic) |
|---:|---:|---:|---:|---:|---:|---:|---:|:-:|:-:|:-:|---:|
| 193 | 5 | 14 | 5 | 5 | 2 | 3 | 5 | no | yes | yes | 2 (2) |
| 409 | 7 | 19 | 4 | 7 | 4 | 2 | 7 | yes | yes | no | 3 (2) |
| 577 | 5 | 22 | 9 | 5 | 3 | 2 | 5 | yes | yes | yes | 4 (4) |
| 2521 | 11 | 18 | 2 | 29 | 2 | 15 | 29 | no | yes | yes | 3 (1) |
| 3361 | 11 | 23 | 4 | 29 | 3 | 7 | 29 | yes | no | yes | 3 (2) |
| 5569 | 13 | 27 | 8 | 17 | 7 | 2 | 34 | yes | yes | no | 6 (4) |
| 9601 | 13 | 26 | 4 | 19 | 9 | 2 | 37 | yes | yes | yes | 5 (3) |
| 66529 | 13 | 34 | 9 | 26 | 5 | 3 | 39 | no | yes | yes | 6 (5) |
| 83449 | 13 | 32 | 7 | 52 | 11 | 5 | 65 | yes | yes | no | 6 (4) |
| 1726201 | 19 | 38 | 11 | 95 | 22 | 2 | 593 | yes | yes | no | 19 (11) |
| 8813281 | 17 | 63 | 23 | 51 | 3 | 5 | 111 | yes | yes | yes | 27 (15) |

At 2521 the only two certificate edges are {2, 29} and {2, 87} (p + 2 = 3·29², χ(29) = (−2/29) = −1), both on line u = 2;
87 ≡ 7 (mod 8) is the twin-line witness. At 3361 the certificates are {3, 29}, {3, 116}, {5, 34}, {5, 99}; 116 ≡ 4 (mod 8) is
the López witness and no vertex ≡ 7 (8) is non-isolated. (`z48_forestfable_show.py 2521` etc. print the forests.)

**4.4 Components.** Means over the last 20 % of primes ≤ 10⁸: W = 134 = 0.40 L², B = 85 = 0.25 L², non-isolated vertices
183 = 0.55 L², components 49 = 0.15 L², bichromatic components 35 = 0.11 L², largest component 60 = 0.18 L² (it is the
component of 1 for 97.4 % of primes). "comp(1) is bichromatic" fails at 1.5 % of primes (first 409, 1201, 5569, …; the
Astra root-1 failure set), "the largest component is bichromatic" at 0.9 %, "some bichromatic edge lies in a component of
size ≥ 3" only at p = 1 726 201 (where all 11 certificate edges are isolated edges). "comp(1) bichromatic or López"
never fails ≤ 10⁸. So "some component is bichromatic" is massively overdetermined on average (≈ 35 bichromatic components),
and the whole difficulty is that each component is its own lottery (§5).

## 5. The mechanism search: what could force a bichromatic component?

The discrete intermediate-value principle is exact: on any tree path between opposite-coloured vertices some edge is
bichromatic, and by Theorem A that edge is a certificate. So ES(p) ⟸ "some component of F_p contains both colours". Each
candidate for forcing this was pushed until it met its blocking step; the step is named in every case.

**M1 — the component of 1 (root-1 construction).** Fails at 1.5 % of primes; sterile components of 8 vertices exist i.o.
under Dickson (ASTRA Thm 3.1). Blocking step: the children of a divisor d of p + 1 are the divisors of p + d in the class
1 (mod d) — a divisor event of one integer per vertex. Not repeated.

**M2 — growing roots: the least QNR r(p), or any QNR vertex found by GRH/003.** Under 003, r(p) ≪ log⁸p, so a QNR vertex
exists at polylog height (CONDITIONAL on OAI-003). Its parent a_r = −p mod r is QR, so the edge {a_r, r}, *if present*, is a
certificate. It is present iff a_r | p + r. PROVED (CRT): for a fixed vertex v the set of p for which v has a parent is the
union over a < v, gcd(a, v) = 1 of one reduced class mod av (p ≡ −a (mod v), p ≡ −v (mod a)); its density among primes is
Σ_a 1/φ(av) ≍ (log v)/v (PNT in APs). So the parent of a QNR vertex at height v ≈ log p exists with density ≈ (log log p)/log p, and ASTRA Thm 5.1 exhibits (i.o. under Dickson) primes
with r(p) = 11 isolated. The least QNR *prime* ℓ ≡ 7 (8) is also ≪ log⁸p under 003 (fixed-density detector); by Corollary C
its colour is irrelevant and the only question is whether p + ℓ has a divisor ≡ −1 (mod ℓ) — the hypotheses have no bearing
on it. Blocking step: attachment is a divisor condition on p + v (children) or on ⌈p/v⌉ + 1 (parent), untouched by any
character estimate. This is FOREST_H4 §3.2's "residual event" with the density made explicit.

**M3 — a different opposite-coloured pair.** Vertices 1, 2, 3 are always in one component (edges {1,2}, {2,3} for p ≡ 1 (6)),
all QR for p ≡ 1 (24). Vertices p+1 ~ 1 and p+2 ~ 2 are QR. A QNR vertex is in comp(1) iff its parent chain reaches 1, each
step a divisor event. The largest component is comp(1) 97 % of the time and fails as a mechanism at 0.9 % of primes.
Blocking step: there is no pair of vertices whose *connection* is forced by anything other than divisibility of shifted
integers; the forest has no cycles, so no holonomy/parity argument exists (LOWER_TAIL_ASTRA §2 scope).

**M4 — counting bichromatic edges with the forest structure (lead (b)).** Each non-root vertex v contributes exactly its
parent edge, so W(p) = #{v ≥ 2 : a_v | p + v} and B(p) = #{v : a_v | p + v, χ(a_v) ≠ χ(v)}. Grouping by the smaller
endpoint u, B(p) = Σ_u ½ Σ_{A | p+u, A ≡ −1 (u), A < (p+u)/u} (1 − (A/p)), with (A/p) given by the explicit 2-adic rules of Lemma P; on the
pure lines u ∈ {1, 2, 3, 4, 7, 15} the inner sum is a divisor sum twisted by a Kronecker character, i.e. a weight-one
Eisenstein coefficient at the shifted argument p + u (r₂((p+1)/2)/4 for u = 1, etc.). A lower bound B(p) ≥ 1 at a single p
is a positivity statement for a sum of Eisenstein coefficients along the shifts of one prime — B6/B2. Even the *sign-free*
W(p) ≫ (log p)² at every p is open: by Prop 3.2 the lines u ≤ X contribute 2 at shadow primes, so a proof must count
divisors of p + u in a tied class for u up to p^{ε} at least; no such pointwise count is known (PARITY_AUDIT Remark 3.1). No
identity constrains the cell counts of Theorem B: all three monochromatic classes and all certificate classes are
populated at comparable rates (§2), and the only exact relation is the telescoping of edge signs along paths.

**M5 — the covering system (Prop 3.1) as a sieve problem.** "Every large prime meets some G_A" is a covering statement with
p-independent residue sets of superlinear sieve dimension (§3). Finite sub-coverings fail (Prop 3.2(a)); an infinite one
needs, at each p, an A ≤ X(p) with p mod A ∈ G_A, which for A > log p/ log log p means a divisor of p + d in the class
−1 (mod d) with a prime factor above X — the lottery. The heuristic exponent (log X)²/4 says the lottery is comfortably
supercritical; the Dickson shadow says nothing below X ≈ log p/log log p can be forced. Blocking step: the class of a
divisor of ONE integer (B2), now with the two halves separated: the colour half is free (even under nothing), the shadow
half is everything.

**M6 — the sign-free two-line union of Corollary C as a target.** "p + v has a divisor ≡ −1 (mod v) for some v ≡ 0 (4) or
v ≡ 7 (8)" is implied by nothing weaker than itself; it is López's conjecture (B1_LINE: only 193, 2521, 66529 fail to 10¹¹)
with the twin line added, and the twin removes exactly those three. It is the forest-side analogue of the (★) ∪ López
union (SYNTHESIS_SPARKS9 Cor 1.2), with the advantage that both halves are conditions of the same shape on the same family
of integers p + v, v ≤ √p + 2 — so the whole of ES₅ restricted to these lines is: *among the integers p + 4, p + 7, p + 8,
p + 12, p + 15, p + 16, …, one has a divisor ≡ −1 modulo its own shift.* The witness is small in practice (v07min ≤ 116 to
10⁸). It is still a divisor-class event at one integer; no theorem controls it.

**M7 — the prime-numerator sub-family.** ES₅(p) ⟸ ∃ prime ℓ with p mod ℓ ∈ G_ℓ, i.e. (−p mod ℓ) | ℓ + 1 and (p/ℓ) = −1
(PROVED from Prop 3.1). This is the cleanest *sieve* statement: for each prime ℓ a set of ≈ τ(ℓ+1)/2 forbidden residues;
the question is whether a prime p can avoid them all for ℓ up to p. Its sieve sum is ≈ 0.97 log X (Titchmarsh constant
ζ(2)ζ(3)/ζ(6) ≈ 1.94 halved), so it is critical and presumably fails i.o. (EVIDENCE: P(ℓ_min > X) ≈ X⁻¹, §4.2; no failure to
10⁸). Even if it never failed, proving it would require the residues p mod ℓ to avoid a growing family of divisor-shadows —
again the factorisation of p + d for small d. Blocking step: B1 for ℓ ≤ log p/log log p, B2 beyond.

**M8 — Pell / class-group / cycle data, non-abelian Frobenius.** Not pursued beyond the repo's verdicts ((J)84 Prop 4.2:
Pell windows are never Jacobi-forced; (J)93/(J)96/(J)104: reciprocity forces parity, never class); in covering language
these inputs all live in the colour half Q_A, which Prop 3.1 shows is the half that is free.

**Reading (Assessment).** The forest removes the colour from the problem (Corollary C: two residue classes of vertices are
all-certificate) but cannot remove the divisor condition; every path in it is a chain of "x | p + y" conditions, and the
discrete IVT only ever converts a *given* connection into a certificate. A mechanism forcing a bichromatic component would
have to force a connection, i.e. a divisor of a prescribed shifted integer in a prescribed class — which is B2 by name.

## 6. What GRH / OAI-003 buy here, and the exact remaining gap

CONDITIONAL on OAI-003 (quasi-RH 7/8), from OAI_DUMP_IMPACT §2: r(p) ≪ (log p)⁸; the least prime ℓ ≡ 7 (mod 8) with
(ℓ/p) = −1 is ≪ (log p)⁸; M_BM(p) ∼ (3/(2π²)) log²p. CONDITIONAL on GRH: the same with exponent 2 (Ankeny/Bach). Consequences
for the forest (PROVED implications): a QNR vertex and a QNR vertex ≡ 7 (8) exist at polylog height; H₄ ≥ r is consistent
with H₄ ≤ polylog; nothing more. The upper bound H₄(p) ≤ polylog(p) is equivalent (PROVED, trivial from Theorem A and the
definitions) to the following *attachment* statement, which is the exact remaining gap:

> **Gap (attachment).** For every sufficiently large prime p ≡ 1 (mod 8) there is a vertex v ≤ (log p)^{C} such that p + v has a
> divisor w ≡ −p (mod v), w ≠ v, with χ(w) ≠ χ(v) — equivalently (Theorem A) with 4 dividing one of t, v, w, (p+v)/w, (p+w)/v.
> A sign-free sufficient form (Corollary C): some v ≤ (log p)^{C} with v ≡ 0 (4) or v ≡ 7 (8) such that p + v has a divisor
> ≡ −1 (mod v).

This is one integer (p + v), one residue class (−1 mod v), a modulus tied to the integer, and a polylog family of shifts — the
B2 event verbatim, with the colour layer removed. EVIDENCE for the gap statement with C = 2: all p ≡ 1 (24) ≤ 10⁸ (H₄ ≤ 1.40
(log p)², least sign-free witness ≤ 116). CONDITIONAL on Dickson (ASTRA Thms 3.2, 5.1): the witness v cannot be
bounded, and cannot be the least QNR. Unconditionally (Prop 3.2): H₄ ≥ c log p i.o. No standard hypothesis is known to
imply the attachment statement, and this document does not change that.

## 7. Screening checklist (FRONTIER §4) for the sign-free union of Corollary C taken as a proof target

| line | status | reason |
|---:|---|---|
| 1 | PASS | T1-exact (Theorem E): at odd squares no vertex ≡ 0 (4) or 7 (8) is non-isolated; verified at all 499 squares ≤ 10⁶. |
| 2 | PASS | 4-specific: the twin line uses (2/v) = (2/p) inside (v/p); no numerator-8 analogue; at 17, 241 the 8-analogue (vertex ≡ 0 (8)) fails while the 4-lines fire. |
| 3 | PASS | No numerator-uniform law. |
| 4 | **FAIL** | "p + v has a divisor ≡ −1 (mod v)" is the tied-modulus divisor event; no theorem controls it at one p. |
| 5 | PASS as stated | Nothing is averaged; the CRT densities of §3/§5 are explicitly labelled heuristics. |
| 6 | PASS | Expected count 0.20 (log p)² words, no power-size main term. |
| 7 | PASS | No two-sided claim. |
| 8 | PASS as target / FAIL as method | The family is p-dependent and growing (v up to √p); its first log p/ log log p members are blocked by shadows (Prop 3.2). |
| 9 | **FAIL at existence** | The quadratic layer of G_A is free (Prop 3.1); the class layer (shadow) is the whole problem. |
| 10 | PASS | No pooling across shifts (each v is its own integer p + v). |
| 11–13 | N.A. / PASS | No signed detour, no relaxation transport, no BM shortcut. |
| 14 | PASS (finite) | All listed hard primes carry a witness; 193, 2521, 66529 by the twin line, 3361 by López's. |
| 15 | PASS (finite) | Near-square and Mordell-class primes are in the census. |
| 16 | N.A. | — |
| 17 | **FAIL** | A witness divisor must involve a prime factor of p + v above log p/ log log p at shadow primes; its class is uncontrolled. |

## 8. Verdict, promise, and what is retained

**Verdict: PARTIAL — a clean negative on the mechanism question, with a sharper dictionary.** Promise for the task's target
(a certificate edge for every large p, H₄ ≤ polylog): **1/5**. Retained:
* PROVED: Theorem A with an elementary reciprocity proof (the converse the brief asked for; it was already DEDEKIND_ES Thm 4.5);
  Theorem B (edge colour from endpoints mod 8); Lemma P (all-certificate pentagon classes, collecting z1/y5); Corollary C
  (two sign-free vertex lines, explicit solutions); Theorem E (T1-exactness of the twin line); Prop 3.1 (p-independent covering
  form with explicit G_A); Prop 3.2 (B1/Linnik in that form).
* CERTIFIED: independent reproduction of the forest census to 10⁶; dictionary checks on 122 million edges to 10⁷/10⁸; the
  failure lists of the sign-free families (López: 193, 2521, 66529; twin: 3361; Legendre levels: 10 primes ≤ 10⁸; union of
  López and twin: none ≤ 10⁸); the minima u_min ≤ 25, v07min ≤ 116, H₄ ≤ 1.391 (log p)² to 10⁸; the controls.
* EVIDENCE: sieve dimension of the covering ≈ (log X)²/4; the prime-numerator family is critical (P(ℓ_min > X) ≈ X⁻¹).
* CONJECTURE (new coordinates for old conjectures, not new conjectures): u_min(p) ≪ log p; v07min(p) ≪ log p;
  the attachment statement of §6 with C = 2.
* Not achieved: any pointwise mechanism; any use of GRH/003 beyond locating QNR vertices; any bound on H₄ at a prescribed p.

**Reproduction** (from the repository root; total CPU ≈ 16 min, peak RSS 0.4 GB):
```sh
ulimit -v 8000000
gcc -O2 -Wall -Wextra -o /tmp/z48scan scripts/z48_forestfable_scan.c -lm
timeout 600 /tmp/z48scan 10000000 > data/z48_forestfable/scan_1e7.txt            # all p ≡ 1 (4)
timeout 7200 /tmp/z48scan 100000000 5 24 | gzip > data/z48_forestfable/scan_1e8_mod24.txt.gz
timeout 300 /tmp/z48scan 1000000 9 0 > data/z48_forestfable/scan_squares_1e6.txt   # odd squares
/tmp/z48scan 100000 5 1 17 241 193 2521 3361                                      # controls
timeout 600 uv run python scripts/z48_forestfable_converse.py 5000
timeout 900 uv run python scripts/z48_forestfable_analyze.py data/z48_forestfable/scan_1e8_mod24.txt.gz 24
timeout 1500 uv run python scripts/z48_forestfable_cover.py 18 400 100000
uv run python scripts/z48_forestfable_show.py 2521
```
Data kept under `data/z48_forestfable/` (14 MB): `scan_1e6.txt.gz` (all 49 columns, all p ≡ 1 (4) ≤ 10⁶),
`scan_1e7_reduced.txt.gz` and `scan_1e8_mod24_reduced.txt.gz` (per-prime summary: p r W B H₄ u_min t_min A_min v07min ℓ_min,
component data, and an 11-bit flag string L0 L7 L3 Lodd LprimeA Lleg Ltuv4 LA7 c1bi maxbi bi_in_big), `scan_1e8_mod24_special.txt.gz`
(full rows of the 56 primes ≤ 10⁸ where López, the twin or the Legendre family fails or B < 10), `scan_squares_1e6.txt`,
`cover.txt`, and the `analysis_*.txt` outputs (the full-column 10⁷/10⁸ scans are regenerated by the commands above).
