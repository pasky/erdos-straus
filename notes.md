# The Erdős–Straus conjecture: a serious attempt, and an honest map of the wall

*Working notes, 2026-08-16. Companion computations: `verify.py` (full run ~55 s).*

**Conjecture (Erdős–Straus, 1948).** For every integer n ≥ 2 there are positive
integers x, y, z with

    4/n = 1/x + 1/y + 1/z.

**Status (checked 2026-08-16):** open. It is problem
[#242 on erdosproblems.com](https://www.erdosproblems.com/242) (page last edited
2026-05-07, listed *Open*). Despite the 2025–26 wave of AI-assisted resolutions
of Erdős problems (Tao's Jan-2026 milestone post; Quanta 2026-08-03), #242 has no
claimed solution, partial or complete. Known landscape (from the problem page and
literature; citations below partly from memory, flagged where so):

* Verified computationally for all n up to at least 10^17 (Salez 2014; a 2025
  verification [MiDu25] extends this — exact bound not retained).
* Mordell (1969): identities cover all n except n ≡ 1², 11², 13², 17², 19², 23²
  (mod 840). Terzi (1971) extended the modulus to 120120.
* Vaughan (1970): #exceptions below N is ≪ N·exp(−c(log N)^{2/3}).
* Elsholtz–Tao (2013): counting solutions for prime n; lower bounds on average.
* Bright–Loughran (2020): **no Brauer–Manin obstruction** — no known algebraic
  mechanism by which the conjecture could be false.
* Bloom–Elsholtz (2022), Thm 1: an equivalence recasting the conjecture as a
  two-case divisor condition (same shape as the criterion derived independently
  below).
* Schinzel: no polynomial identity can cover a residue class r (mod m) when r is
  a square mod m — so covering-congruence proofs provably cannot finish the job.

Everything below is derived and proved from scratch unless marked *(cited)*.
Section 7 states exactly what is new-ish here, what is folklore, and where the
attempt stops.

---

## 1. Reductions

**Lemma 1.1 (composite reduction).** If 4/a = 1/x + 1/y + 1/z then
4/(ab) = 1/(bx) + 1/(by) + 1/(bz). Hence it suffices to prove the conjecture
for n prime, plus n = 4 (4/4 = 1/2 + 1/4 + 1/4) covering powers of 2 via the
factor 4, and 4/2 = 1 + 1/2 + 1/2·(n=2 direct). So: **odd primes p only**. ∎

**Lemma 1.2 (easy classes).** The following exact identities hold (symbolically
verified in `verify.py (e)`):

* p ≡ 3 (mod 4), h = (p+1)/4:  4/p = 1/h + 1/(2hp) + 1/(2hp).
* p ≡ 2 (mod 3), k = (p+1)/3:  4/p = 1/p + 1/k + 1/(kp).
* p ≡ 5 (mod 8), g = (p+3)/8:  4/p = 1/(2g) + 1/(pg) + 1/(2pg).

Hence the conjecture is open only for **p ≡ 1 (mod 24)**. ∎

**Lemma 1.3 (at most two denominators divisible by p).** If p | x, y, z, write
x = px′ etc.; then 4 = 1/x′ + 1/y′ + 1/z′ ≤ 3, impossible. So in any solution p
divides exactly one or exactly two of x, y, z (it divides at least one since
4xyz = p(xy + yz + zx)). ∎

We call the two cases **Case A** (exactly one multiple of p) and **Case B**
(exactly two). *(In the literature: Case A = Type I, Case B = Type II —
Aigner/Rosati labels, checked against the §17.1 parametrization.)*

## 2. The two-term lemma

**Lemma 2.1.** Let a, b be coprime positive integers. Then a/b = 1/y + 1/z has a
solution in positive integers iff b² has a divisor d with d ≡ −b (mod a); the
solutions are exactly y = (b + d)/a, z = (b + b²/d)/a over such d.

*Proof.* (⇐) Given such d, set d′ = b²/d. Since gcd(a, b) = 1, d is invertible
mod a and d′ ≡ b²(−b)^{-1} ≡ −b (mod a), so both y and z are positive integers.
Then (d + b)(d′ + b) = dd′ + b(d + d′) + b² = b(d + d′ + 2b), so
1/y + 1/z = a(d + d′ + 2b)/((d+b)(d′+b)) = a/b.
(⇒) Given a solution, 1/y < a/b gives ay − b > 0; set d = ay − b, d″ = az − b.
From ayz = b(y + z): dd″ = a²yz − ab(y+z) + b² = b², so d | b² and
d ≡ −b (mod a). ∎

## 3. The complete criterion

**Theorem 3.1.** Let p be an odd prime. Then 4/p = 1/x + 1/y + 1/z is solvable
iff at least one of the following holds:

* **(B)** there is an integer q > 0 with q ≡ −p (mod 4) and a divisor d of x²,
  where x := (p + q)/4, such that q | d + x;
* **(A)** there is an integer m > 0 with m ≡ 3p (mod 4) and a divisor d of z₀²,
  where z₀ := (pm + 1)/4, such that m | d + z₀.

Explicitly, in case (B) the solution is
( x, p(x + d)/q, p(x + x²/d)/q ), and in case (A) it is
( (z₀ + d)/m, (z₀ + z₀²/d)/m, p z₀ ).

*Proof.* By Lemma 1.3 every solution is Case A or Case B.

Case B: solutions with y = py′, z = pz′, p ∤ x. Then
4/p − 1/x = (4x − p)/(px) = (1/p)(1/y′ + 1/z′), i.e. q/x = 1/y′ + 1/z′ with
q := 4x − p > 0 (positivity forced since the left side must be positive), and
q ≡ −p (mod 4). Also gcd(q, x) = gcd(p, x) = 1 (p | x would put p in all three
denominators, excluded by Lemma 1.3). Lemma 2.1 applied to q/x gives the stated
condition and formulas, both directions. Conversely any (q, d) as in (B) yields
a valid solution by direct substitution (checked symbolically; the computation
is Lemma 2.1's). Note x ranges over all integers > p/4 as q ranges as stated.

Case A: solutions with z = pz₀, p ∤ xy. From 4xyz₀ = xy + pz₀(x + y):
xy(4z₀ − 1) = pz₀(x + y), and p ∤ xy forces p | 4z₀ − 1; write 4z₀ − 1 = pm.
Then m/z₀ = (x + y)/(xy) = 1/x + 1/y, gcd(m, z₀) = gcd(m, (pm+1)/4) = 1 since
4z₀ ≡ 1 (mod m). Lemma 2.1 gives the condition; m ≡ 3p (mod 4) is exactly
integrality of z₀ = (pm+1)/4. Both directions as before. ∎

*(This matches the shape of Bloom–Elsholtz 2022, Thm 1 — cited; derived
independently here.)*

**Empirics** (`verify.py (a)–(b)`): for every prime 3 ≤ p < 10⁵ a Case-B witness
exists with q ≤ 63; every reconstructed solution verified exactly. Worst case:
p = 87481 needs q = 63. The stubborn p = 1201 from the play session: witness
q = 23, d = 108, x = 306, giving 4/1201 = 1/306 + 1/21618 + 1/61251.

## 4. Identity families and what they cover

Fix q and d and *force* d | x² by congruences: let R₀(d) := ∏_{r^e ∥ d} r^⌈e/2⌉
(the minimal R with R | x ⇒ d | x²; note R₀ | d and d ≤ R₀²). A **guaranteed
family** is (q, d, R) with R₀(d) | R; it covers the arithmetic progression

    { p : 4 | p + q,  x ≡ 0 (mod R),  x ≡ −d (mod q) },   x = (p+q)/4,

a single class mod M = 4·lcm(R, q) when consistent. Every prime in it is
solvable by Theorem 3.1(B). Case-A families (m, d, R) are defined mirror-wise.
Two more shapes close the classical zoo:

* **F1 (two-parameter):** p = 4guv − u − v ⇒
  4/p = 1/(guv) + 1/(pgu) + 1/(pgv) (exact identity, `verify.py (e)`).
  For fixed (u, v) it covers the class p ≡ −(u+v) (mod 4uv), g free.
* **L (linear-q, d = 1):** q = (x+1)/j linear in x: jp = (4j−1)x − 1 covers
  exactly p ≡ −4 (mod 4j − 1), j free. (j = 1 is the mod-3 identity; j = 2
  covers p ≡ 3 (mod 7); j = 3 covers p ≡ 7 (mod 11), …)

Worked examples derived by hand and verified: (q=7, d=2): covers
p ≡ 41 (mod 56), e.g. 4/97 = 1/26 + 1/388 + 1/5044. (q=15, d=8, R=4): covers
p ≡ 193 (mod 240), e.g. 4/193 = 1/52 + 1/772 + 1/5018. (q=7, d=5, R=5): covers
p ≡ 113 (mod 140), e.g. 4/673 = 1/170 + 1/16825 + 1/572050.

**Empirics** (`verify.py (d)`): a finite system (constant families with q < 60,
d ≤ 100; L with j ≤ 50; F1 with u ≤ v ≤ 20) covers 9588 of the 9591 primes
below 10⁵ — misses only 61681, 67369, 87481, all in the six hard classes mod
840, and each of those still has a (non-forced) witness. This is the "identities
nibble forever but cannot finish" phenomenon, which the next section makes into
a theorem.

## 5. The obstruction: a self-contained mini-Schinzel theorem

**Theorem 5.1.** No guaranteed family (Case A or B, any padding R) covers even a
single prime p ≡ 1 (mod N), for any N divisible by the family's modulus M.

*Proof.* Let the family be (q, d, R), M = 4·lcm(R, q), and suppose some prime
p ≡ 1 (mod N), M | N, lies in the family's class c (mod M). Then c ≡ 1 (mod M).
Since the (q,d,R)-class is contained in the (q,d,R₀)-class and the moduli divide
each other, we may assume R = R₀(d), so **R | d and d ≤ R²**.

From c ≡ 1 (mod M):
- mod 4R: R | x gives 4R | 4x, so p ≡ 4x − q ≡ −q, hence q ≡ −1 (mod 4R);
  in particular q ≥ 4R − 1.
- mod q: x ≡ −d gives p ≡ −4d, hence q | 4d + 1; write t = (4d+1)/q ≥ 1.

Then t ≤ (4R² + 1)/(4R − 1) = R + (R+1)/(4R−1) < R + 1, so **t ≤ R**.
But mod 4R: since R | d, 4d ≡ 0 (mod 4R), so qt = 4d + 1 ≡ 1, and q ≡ −1 gives
t ≡ −1 (mod 4R), so **t ≥ 4R − 1 > R**. Contradiction. The Case-A computation
is verbatim with m in place of q. ∎

**Lemma 5.2 (other shapes).** F1 with parameters (u,v) covers no p ≡ 1
(mod 4uv): that would need 4uv | u + v + 1, but 0 < u + v + 1 ≤ 2uv + 1 < 4uv.
L with parameter j covers no p ≡ 1 (mod 4j−1): that would need (4j−1) | 5,
impossible as 5's divisors are 1, 5 ≢ 3 (mod 4). ∎

**Corollary 5.3.** Let S be any finite collection of families of the above
shapes and N the lcm of 4 and all their moduli. By Dirichlet there are
infinitely many primes p ≡ 1 (mod N), and by 5.1–5.2 *none* of them is covered
by any member of S. Hence no finite congruence-identity system of these shapes
can prove the conjecture. ∎

*(Schinzel's theorem — cited, not reproved here — extends this to arbitrary
polynomial identities 4/(mt + r) with r a square mod m. Theorem 5.1 is the
special case actually needed to explain the failure of every covering system in
the literature, and its proof above is elementary and self-contained.)*

## 6. Why the six classes resist: the parity mechanism

**Lemma 6.1 (Jacobi obstruction).** Let q ≡ 3 (mod 4), gcd(q, x) = 1,
x = (p+q)/4. If every prime factor r of x has Jacobi symbol (r|q) = +1, then no
divisor d of x² satisfies d ≡ −x (mod q) — the witness condition for this q
fails unconditionally.

*Proof.* All divisors d of x² then satisfy (d|q) = +1 and (x|q) = +1. But
d ≡ −x (mod q) forces (d|q) = (−1|q)(x|q) = −1, since (−1|q) = −1 for
q ≡ 3 (mod 4). ∎

**Empirics** (`verify.py (c)`): among hard-class primes p < 10⁵, of all 453
pairs (p, q) with q below the minimal witness, 92.9% are explained by Lemma 6.1
(the rest have a QNR factor but miss the exact coset).

**The q = 3 case is exactly solvable and reveals the mechanism.** For
p ≡ 2 (mod 3): x ≡ 2 (mod 3) and d = 1 works — witness *forced by congruence
alone* (this IS the classical mod-3 identity). For p ≡ 1 (mod 3): x ≡ 1 (mod 3),
the witness needs d ≡ 2 (mod 3), and such a divisor of x² exists **iff x has a
prime factor ≡ 2 (mod 3)**. But x ≡ 1 (mod 3) means the number of prime factors
of x that are ≡ 2 (mod 3) (with multiplicity) is *even* — so the generic
"exactly one" case is excluded, and the failure event "zero such factors" has
enhanced probability. Verified: for all 273 hard-class primes p < 10⁵, q = 3
has a witness iff (p+3)/4 has a prime factor ≡ 2 (mod 3) — 0 mismatches; only
32% succeed, versus the ≥ 80% naive density prediction for unconditioned
integers of that size.

**This is the conceptual unification.** A residue class of p is "easy" exactly
when the induced congruence on x forces odd QNR-multiplicity (hence a usable
divisor exists *by congruence*, giving an identity); it is "hard" exactly when p
≡ square forces even multiplicity, so witness existence degenerates from a
congruence consequence into a **factorization event** with no congruence
handle — which is Schinzel's obstruction seen mechanically. For q > 3 the
character argument only narrows d to a coset-half; hitting the exact coset needs
either forced small divisors (the identity zoo of §4) or luck (the 92.9%/7.1%
split above).

## 7. Where exactly this attempt stops

What the sections above amount to:

* **Proved from scratch:** Lemmas 1.1–1.3, 2.1, Theorem 3.1 (the complete
  solvability criterion, both directions), the identity families of §4 with
  exact symbolic verification, Theorem 5.1 + Corollary 5.3 (elementary
  obstruction theorem: no finite system of divisor-forced congruence families
  proves ES), Lemma 6.1, and the q=3 parity characterization of §6. All of this
  is essentially known to experts (Rosati, Aigner, Mordell, Schinzel,
  Bloom–Elsholtz), but the derivations here are independent and self-contained;
  I make no novelty claim beyond, possibly, the packaging of §5–§6.
* **The missing lemma** — all that separates this from a proof:

  > For every prime p ≡ 1 (mod 24) there exists q ≡ 3 (mod 4) such that the
  > divisors of x², x = (p+q)/4, meet the residue class −x (mod q)
  > (or the Case-A mirror with z₀ = (pm+1)/4 mod m).

  Empirically q ≤ 63 suffices below 10⁵ and the minimal q grows extremely
  slowly, if at all.
* **Why the missing lemma is hard, precisely:**
  1. For any *single* q (or finite set of q), Lemma 6.1 shows failure occurs on
     a set of p of positive density — the factorization of (p+q)/4 can be
     all-QR mod q. So one must play infinitely many q against each other.
  2. The failure events across q are correlated only through the factorizations
     of the numbers (p+q)/4, q = 3, 7, 11, … — an additive shift family. Proving
     that *some* member of an additive family has a prescribed multiplicative
     property, **uniformly for every p**, is exactly the type of statement
     (cf. least-nonresidue problems, smooth numbers in short APs) that current
     analytic number theory delivers only "for almost all" or "for large enough
     ... under GRH"-style. Vaughan's bound (exceptions ≪ N exp(−c(log N)^{2/3}))
     is precisely the almost-all shadow of this heuristic; it has not been
     improved to "all" in 55 years.
  3. There is no structural escape hatch to hope for on the negative side
     either: Bright–Loughran (2020) show no Brauer–Manin obstruction, and the
     heuristic solution count (Elsholtz–Tao) grows like a power of log p — the
     conjecture is "true with lots of room", which is exactly why a
     counterexample search is hopeless and why the difficulty is purely one of
     uniformity, not of truth.
* **What would constitute genuine progress** (attempted, not achieved here):
  (i) an unconditional proof that q ≤ (log p)^{O(1)} suffices — this would need
  character-sum estimates on divisor-coset hitting beyond Burgess-type
  uniformity; (ii) exploiting *joint* structure across q (the numbers (p+q)/4
  for varying q share no useful algebraic relation I could find — their pairwise
  gcds are bounded); (iii) an algebraic identity outside the divisor-forced
  shapes — ruled out for all shapes formalized here by Theorem 5.1, and for all
  polynomial shapes by Schinzel.

**Honest bottom line.** The conjecture remains open here. The concrete outputs
are: a complete, self-contained criterion (Thm 3.1); an elementary and, in this
packaging, possibly novel proof that no finite divisor-forced congruence system
can settle it (Thm 5.1/Cor 5.3); the parity-mechanism explanation of *why* the
six quadratic-residue classes mod 840 are the hard ones (§6, verified with zero
mismatches on all hard-class primes < 10⁵); and a precise, minimal statement of
the missing lemma together with the reason it sits beyond current uniformity
technology.

## 8. Second push: three attacks past the wall

Section 7 identified the missing lemma; this section records genuine attempts
to prove it, each pushed until it broke, with the break point named.

### 8.1 Quadratic-form families (attack, partial success, structural failure)

In criterion (B), fix a multiplier s ≥ 2 and ask for *both* roots at once: d,
d′ are the roots of T² − (sq − 2x)T + x², so a witness with d + d′ = sq − 2x
exists iff the discriminant qs((s−1)q − p) is a perfect square (parities match
automatically; need (s−1)q > p for positivity). Taking s ≡ 3 (mod 4), q = sf²
with f odd, the square condition becomes

    p = s(s−1)f² − h²   ⇒   4/p solvable.

**Verified** (`p = 281 = 506·1 − 15²`, s = 23: 4/281 = 1/76 + 1/1124 + 1/5339;
and the family with f = 5, h = 107 captures the stubborn p = 1201 =
506·25 − 107²). These are Aigner/Rosati-type conditions rediscovered.

**Why it cannot finish:** representability by an indefinite form is a class-
group condition, not a congruence condition — each family hits a hard class
only in a thin subset (empirically: of the s = 23 family's hits below 3000 in
p ≡ 1 (mod 24), exactly one lies in the six classes). Worse, the small-s
families die on congruence grounds before even starting: s = 3 forces
p ≢ 1 (mod 3), s = 7 likewise, s = 11 and 19 die mod 8, s = 15 dies mod 3 —
the 2-adic/3-adic obstructions of Theorem 5.1 reappear form by form. Quadratic
forms give densities, never classes; summing thin sets cannot reach "all p".

### 8.2 Reciprocity collapse (new-ish lemma, proved + verified)

**Proposition 8.1.** Let p ≡ 1 (mod 4) be prime, x > p/4, q = 4x − p (any such
q, prime or not; q ≡ 3 (mod 4)), and r an odd prime dividing x, r ≠ p. Then
the Jacobi symbols satisfy **(r|q) = (r|p)**.

*Proof.* r | x gives q ≡ −p (mod r). If r ≡ 1 (mod 4):
(r|q) = (q|r) = (−p|r) = (−1|r)(p|r) = (p|r) = (r|p), using reciprocity twice
and p ≡ 1 (mod 4). If r ≡ 3 (mod 4): (r|q) = −(q|r) (both ≡ 3 mod 4)
= −(−p|r) = −(−1)(p|r) = (p|r) = (r|p). ∎
(Verified: 38,480 triples with prime q below 3000, zero mismatches.)

Moreover (2|q) is +1 or −1 according as x is even or odd (p ≡ 1 mod 8). So:
**the entire character landscape governing Lemma 6.1, across every q
simultaneously, is dictated by which primes are quadratic residues mod p
itself** — nothing about the individual q matters. Consequences:

* A counterexample p cannot be "all Jacobi-obstructed": window elements with a
  QNR-mod-p odd factor (or odd window elements, via the factor 2) have
  character-permitted witnesses. So a counterexample must fail predominantly
  by *coset misses* — the character sieve is provably not the true wall.
* The 92.9% Jacobi-obstruction rate of §6 is a statement about p's own residue
  structure filtered through the window's factorizations.

### 8.3 Window dichotomy and the true residual problem

Since x = (p+q)/4 ranges over *all* integers > p/4 as q ranges over its
progression, the criterion becomes a statement about the block of consecutive
integers just above p/4:

**Lemma 8.2 (window dichotomy).** p is a counterexample iff for every integer
x > p/4 (q := 4x − p, and mirror Case-A conditions): no divisor of x² lies in
−x (mod q). In particular, taking d = xr: **no prime factor of any window
element x may be ≡ −1 (mod 4x − p)** — a "diagonal sieve" where consecutive
integers face conditions with growing moduli. ∎

Two hard facts about this diagonal sieve, both proved above or checkable:

1. **Prime window elements are useless.** If x = r is prime, the divisors of
   x² are {1, r, r²}, and a witness exists iff (4r − p) | (p + 4) — the L
   family again. So any proof must route through *composite* window elements
   with rich divisor sets: the conjecture genuinely lives in the
   divisor-structure of the window, not in its primes.
2. **Every finite pattern is heuristically satisfiable.** Each single condition
   ("x has no prime factor ≡ −1 mod q") holds on a positive-density set, and
   for fixed window length L the intersection has density ≈ ∏ρ over blocks —
   positive. So no fixed-L contradiction can exist: for every L there should be
   (rare) primes whose first L conditions all fail. Prediction: **the minimal
   witness q(p) is unbounded**. Data (all primes to 4·10⁵): the record minimal
   q runs 1, 3, 7, 11, 23, 31, 35, 63 at p = 3, 5, 73, 1129, 1201, 21169,
   67369, 87481 — slow growth, consistent with ≍ log-power unboundedness.

This closes the loop with Corollary 5.3 from the other side: identity systems
are exactly the *uniformly finite* proofs, and 8.3(2) predicts no uniformly
finite proof can exist because the quantity it would bound is unbounded. The
conjecture, if true, is true non-uniformly — which is why 75 years of
covering systems, forms, and almost-all analytics have not closed it.

**The residual problem, in final form.** For every prime p ≡ 1 (mod 24) there
is an x just above p/4 whose divisor lattice (of x², halved by the character
condition of 8.1 according to p's own QR structure) hits the moving coset
−x (mod 4x − p). This is a uniform divisor-equidistribution statement of
Erdős–Odlyzko–Sárközy type (divisors in residue classes), open in the required
uniformity. That — not characters, not congruences, not forms — is the wall.

## 9. Third wave: attacks 4–8

Asked "why just 3 attacks?", the honest answer was: no reason. Enumerating the
remaining surface and burning through it:

### 9.1 Attack 4 — the Case-A mirror collapses identically (proved + verified)

**Proposition 9.1.** For p ≡ 1 (mod 4) prime, m ≡ 3 (mod 4), z₀ = (pm+1)/4,
and any odd prime r | z₀ with r ≠ p, gcd(r, m) = 1: **(r|m) = (r|p)**.

*Proof.* pm ≡ −1 (mod r) gives m ≡ −p⁻¹ (mod r), and (p⁻¹|r) = (p|r). The
same two-case reciprocity computation as Prop 8.1 (m ≡ 3 (mod 4) supplies the
sign in the r ≡ 3 case). ∎ (Verified: 8,818 triples, 0 mismatches.)

So the two halves of criterion 3.1 — which looked like independent chances —
share a *single* character landscape, dictated by p alone. Case A adds new
coset-hitting opportunities (different integers z₀(m), same moduli) but no new
character mechanism. One wall, not two.

### 9.2 Attack 5 — the p-intrinsic witness law (proved + verified)

Combining 8.1/9.1 with the witness congruence d ≡ −x (mod q) and the 2-adic
bookkeeping ((2|q) = +1 iff x even, for p ≡ 1 (mod 8)):

**Proposition 9.2.** For p ≡ 1 (mod 8), every Case-B witness (q, d) at every
x satisfies **(d_odd | p) = −(x_odd | p)** where n_odd is the odd part of n.

(Verified on all 5,662 witnesses with q ≤ 63 of all 273 hard-class primes
below 10⁵: zero violations.) The whole problem is now internal to p: a witness
is a divisor of x² that p's own quadratic character regards as "opposite" to
x, landing in one exact coset. The character layer thins candidates by exactly
a factor 2, no more — the residual difficulty is pure coset-hitting, now
provably so on both halves of the criterion.

**Credit correction (added after §10):** Proposition 9.2 is not new — it is
exactly Bright–Loughran (2020) Corollary 1.3, which they show unifies
Yamamoto's (1965) reciprocity conditions. Three independent derivations
(elementary reciprocity here; Yamamoto's classical route; transcendental
Brauer classes in BL) of the same single bit — see §10.2 for why that is not a
coincidence but a completeness phenomenon.

### 9.3 Attack 6 — can quadratic-form families be bootstrapped? No: a Pell
norm-sign obstruction (new-ish, proved) + Chebotarev evasion (sketch)

§8.1's form families cover positive-density sets; could finitely many of them,
plus congruence families, cover everything? Two-part negative answer.

**(a) One-class-per-genus discriminants: the forms are forced onto the wrong
side.** For such discs, representability is equivalent to congruence
conditions, and a square class p ≡ 1 (mod 4s(s−1)·…) lies in the *principal*
genus, so +p is represented by the principal form X² − s(s−1)Y². But the
ES-family of §8.1 needs **−p** represented (p = s(s−1)f² − h², forced by
positivity of the witness pair). −p is principal-equivalent iff the Pell
equation X² − s(s−1)Y² = −1 is solvable — and it never is: s ≡ 3 (mod 4)
divides s(s−1), and X² ≡ −1 (mod s) has no solution. So **square classes are
never covered by any one-class-per-genus s-family**. The same 2-adic signature
(q ≡ 3 mod 4) that defines the criterion forces the norm-sign obstruction:
the machinery is self-blocking with remarkable consistency.
(Pell unsolvability verified for s = 3, 7, …, 31.)

**(b) Generic discriminants (class number exceeding genus number):**
representation by the *specific* form is a Frobenius condition in the ring
class field, whose non-abelian-over-ℚ part is linearly disjoint from every
cyclotomic field. So for any finite mixture of congruence families and such
form families, Chebotarev supplies infinitely many primes satisfying p ≡ 1
(mod L) *and* evading every form family's Frobenius class. *(Sketch-level:
linear disjointness and non-exhaustion of the fiber are standard but not
re-proved here — flagged.)*

**Corollary 9.3 (extension of 5.3).** No finite mixture of divisor-forced
congruence identities and s-type quadratic-form families proves the
conjecture. ∎

### 9.4 Attack 7 — the graveyard (each checked, each terminal)

* **Greedy algorithm** = the q = 3 special case of the criterion; nothing new.
* **Counting/second-moment positivity**: expected witness count over q ≤ Q
  diverges, but averages give almost-all (= Vaughan) by construction; "all"
  needs pointwise concentration that moments cannot supply. Structural ceiling.
* **Norm coexistence contradictions**: counterexample needs (p+3)/4 and
  (3p+1)/4 both Eisenstein norms with N₂ = 3N₁ − 2; pairs of norms in linear
  relation are heuristically abundant (denser than twin primes); no
  contradiction available at any finite depth (same block-satisfiability
  phenomenon as 8.3).
* **Choosing x's factorization**: fake freedom — x is determined by q; wanting
  x = r₁r₂ with r₂ ≡ −1 (mod 4r₁r₂ − p) is verbatim the original problem.
* **Signed representations** (4/p = 1/x + 1/y − 1/z is easy): no known descent
  repairs the sign; the sign is the conjecture.
* **Identity re-derivations via factoring (p+3)² etc.**: provably circular —
  they reproduce the divisor-coset condition verbatim.

### 9.5 Attack 8 — the standing structural route (geometry)

The equation 4xyz = p(xy + yz + zx) defines a singular cubic surface; the
conjecture asks for *integral* points on the affine piece. Bright–Loughran
(2020) showed the integral Brauer–Manin obstruction vanishes for this family.
So ES would follow from a strong integral local-to-global principle for such
log surfaces — conjectures in that direction exist but are far beyond reach,
and integral Hasse principles are known to fail in general without a
controlling theory. This is the one non-analytic route left standing, and it
is a route for a different decade.

### 9.6 Where the attack tree stood after wave three (superseded by §10.6)

Every elementary branch terminates at one of exactly three named walls:

1. **Uniform divisor equidistribution** (divisors of one specific x² hitting
   one moving coset — §8.3, now p-intrinsic by §9.2);
2. **The almost-all ceiling** of averaging methods (Vaughan's bound is the
   method's edge, not a lazy stop);
3. **Integral Hasse principles** for log cubic surfaces (§9.5).

Everything softer — congruences, polynomial identities, quadratic forms,
characters, greedy, signs, moments — is now provably or structurally dead,
with the obstruction mechanisms identified (Thm 5.1, Cor 9.3, Prop 9.2) rather
than merely observed. §10 executes wall 3 and shows it merges into wall 1.

## 10. Attack 8 executed: the geometry route, worked to the bottom

Source actually read this time: Bright–Loughran, *Brauer–Manin obstruction for
Erdős–Straus surfaces*, arXiv:1908.02526v2 = Bull. LMS 52 (2020) 746–761.
Their precise results, then my own computations on top of them.

### 10.1 What Bright–Loughran actually prove

Let U_n : 4u₁u₂u₃ = n(u₁u₂ + u₁u₃ + u₂u₃) ⊂ 𝔸³. ES for n ⇔ a specific case
of **strong approximation**: the adelic open set W = {positive real component}
× ∏_p U_n(ℤ_p) must meet U_n(ℚ).

* **Thm 1.1:** no Brauer–Manin obstruction to natural-number solutions, any n.
* **Thm 1.2:** for odd n, every natural-number solution satisfies
  ∏_{p|n} (−u₁/u₃, −u₂/u₃)_p = −1 (Hilbert symbols) — a *mandatory*
  reciprocity constraint (an obstruction to strong approximation at the p-adic
  places, though not to existence).
* **Thm 1.5:** integer solutions that are NOT natural give product +1. So the
  Hilbert product is precisely the algebraic shadow of *positivity* — the one
  feature separating trivial signed solvability from the open problem.
* **Thm 1.6:** Br U_n / Br ℚ = ℤ/2, generated by the (transcendental)
  quaternion class (−u₁/u₃, −u₂/u₃).

Verified numerically here (`verify` run of 2026-08-16): product = −1 on four
natural solutions including p = 1201's, product = +1 on the signed solutions
(−5,2,2), (−9,2,18). Their Cor 1.3 (prime case) is Prop 9.2 above.

### 10.2 The ceiling theorem: there is exactly one bit of structure

Thm 1.6 is the most important sentence in the paper and the least advertised.
Since the whole Brauer group is ℤ/2 and its generator's obstruction has been
computed (Thms 1.2/1.5), **every possible "reciprocity-type" necessary
condition on ES solutions is a consequence of one bit** — and that bit is
already known three ways (Yamamoto 1965; elementary reciprocity, §8–§9 here;
transcendental Brauer classes, BL). No fourth reciprocity law is waiting: the
obstruction theory of this surface is *complete and exhausted*. The factor-2
thinning of witness candidates measured in §9.2 is exactly this bit seen
analytically.

### 10.3 The geometry is p-blind

BL observe U_n ≅ U_1 over ℚ for all n (rescale u_i). All Erdős–Straus
surfaces are the *same* ℚ-surface; only the integral model varies with n. So
no invariant of the ℚ-geometry (Picard group, Brauer group, fibration
structure, …) can distinguish an easy prime from a hard one — the entire
difficulty lives in the ℤ_p-integrality conditions. The geometry contributes
its one bit (§10.2) and is then structurally silent.

### 10.4 The conic-bundle collapse: wall 3 = wall 1

Projection to the u₁-line makes U_p a conic bundle: on the surface, with
q = 4x − p (x = u₁),

    (q·u₂ − px)(q·u₃ − px) = p²x²,   with  q·u₂ − px ≡ −px (mod q),

(verified exactly on solutions for p = 97, 1201). Each fiber is a torsor of
the multiplicative group 𝔾_m (a hyperbola AB = N), and an *integral point on
the fiber* is by definition *a divisor of p²x² in the coset −px (mod q)* —
verbatim criterion 3.1. Strong approximation fails for 𝔾_m as badly as
possible (integral points of a hyperbola = divisor extraction), so the
geometric route has no soft leverage over the fibers; "prove strong
approximation for this model" is literally "prove the missing lemma of §7".
Wall 3 was never a separate wall.

### 10.5 Why no Markov-style dynamics, and why the cheat codes fail

* **Rigidity.** The ES equation is multilinear — degree 1 in each variable
  separately — so fixing two coordinates determines the third *uniquely*:
  there are no Vieta involutions, no Markov-type moves, no walks on integral
  points, no descent chains. The Ghosh–Sarnak machinery (which explains both
  the successes and the Hasse *failures* on Markov surfaces x²+y²+z² = xyz+k
  via the nonlinear group action) has nothing to act with here.
* **Schinzel's Hypothesis H does not suffice.** H (+ GRH) is the standard
  conditional cheat code for conic bundles. Attempted here: H can manufacture
  x in the window with prescribed prime-factor shapes (e.g. x = 2r, r and
  8r − p simultaneously prime). But with boundedly many prime factors,
  τ(x²) = O(1), and *each* divisor-coset hit forces a linear relation between
  r and p — e.g. x = 2r yields only 6r = p + 1, 7r = p + 2, … — i.e.
  congruence families again, which Theorem 5.1 already kills; while for x with
  many prime factors, H says nothing about where divisor *products* fall mod
  q. GRH similarly powers only the character layer — which §9.2/§10.2 show is
  the fully-understood bit. **ES does not visibly reduce even to standard
  conjectures**; this matches its 75-year survival.
* **Two-sided silence.** U_n is a log K3 surface (BL's terminology), the same
  class where integral Hasse/strong approximation *provably fails* beyond the
  Brauer–Manin obstruction infinitely often (Ghosh–Sarnak 2017/2022 for Markov
  surfaces; cf. Loughran–Mitankin). So the geometry cannot currently even rule
  out rare ES counterexamples. The rational belief in ES rests on the growth
  of solution counts (Elsholtz–Tao averages; the record-witness data of §8.3),
  which is analytic, not geometric, evidence.

### 10.6 Final state of the attack tree (supersedes §9.6)

The three walls merge. Wall 3 (geometry) = wall 1 (uniform divisor
equidistribution) by §10.4; wall 2 (the almost-all ceiling) is wall 1 attacked
on average instead of pointwise. Therefore:

> **The Erdős–Straus conjecture is exactly one open analytic statement:**
> for every prime p ≡ 1 (mod 24), some shifted value x just above p/4 has a
> divisor of x² in the single coset −x (mod 4x − p) — divisors of shifted
> integers equidistribute in one moving coset per shift, uniformly in p.
> Everything else — all identities, all quadratic forms, all reciprocity, all
> geometry — amounts to one ℤ/2 bit of structure, computed, verified, and
> provably complete (Br = ℤ/2), plus obstruction theorems (5.1, 9.3)
> explaining why nothing softer can work.

What genuine progress would look like, in order of plausibility: (i) divisor
equidistribution for *almost all* shifts with power-saving uniformity in p
(would shrink Vaughan's exceptional set); (ii) an unconditional treatment of
windows containing very smooth x (τ(x²) ≥ q many divisors — pigeonhole is
off by exactly the coset-structure factor); (iii) a structural theory of
integral points on rigid log K3 surfaces — currently nonexistent for want of
any group action. None is in reach of this session, and now I can say
precisely why.

## 11. Wave four: attacking the wall itself — an independent-method
exceptional-set bound, and a calibration of the missing uniformity

The wall (§10.6) cannot be climbed head-on in a session; but my criterion
machinery yields its own exceptional-set bounds by a route different from
Vaughan's, and — more usefully — an exact calibration of what the missing
equidistribution is *worth*.

### 11.1 New empirical input: the two halves are nearly independent

For the 273 hard-class primes < 10⁵: failure of Case B at q = 3 has rate
0.68; failure of Case A at m = 3 has rate 0.66; joint failure 0.41 vs 0.45
predicted under independence — no positive correlation (slightly favorable).
Interleaving both halves, **every hard-class prime < 10⁵ is resolved by
modulus ≤ 31** (histogram 3:162, 7:67, 11:33, 15:6, 23:4, 31:1; record
p = 21169), versus 63 for Case B alone. The adelic "one bit" (§10.2) couples
the halves globally but their factorization events decouple — the sieve sees
two independent barrels.

### 11.2 Correction: the first analytic bounds were vacuous for primes

The q = 3 implications are correct but the exceptional-set conclusions first
written here were not progress.  If f is the indicator of integers all of
whose prime factors are 1 (mod 3), a counterexample prime p, with
n = (p+3)/4, forces

    f(n) = f(3n−2) = 1,                 p = 4n−3 prime.

Consequently the two inequalities

    E(N) ≤ ∑_{n≤(N+3)/4} f(n) ≪ N/(log N)^{1/2},
    E(N) ≤ ∑_{n≤(N+3)/4} f(n)f(3n−2) ≪ N/log N

are valid.  The first uses the classical nonnegative-multiplicative mean-value
bound; the second is a fixed-two-form application of Nair–Tenenbaum Theorem 1
(or Henriot's discriminant-uniform version) to X and 3X−2.  Holowinsky's
same-slope shifted theorem is not the right citation for the latter.

But both estimates discard the condition that 4n−3 is prime.  The elementary
bound E(N) ≤ π(N) ≪ N/log N is already at least as strong.  Thus the former
"Theorems 11.1 and 11.2" are demoted to necessary-condition calculations,
not exceptional-prime theorems.  Any nontrivial criterion-route bound must
retain primality, for example by adding the affine form p itself to an upper-
bound sieve.

### 11.3 Exact slice and conditioning audit

For w ≡ 3 (mod 4), p > w, put

    x_w = (p+w)/4,       z_w = (pw+1)/4,       a_B = p/4 (mod w),
    a_A = 1/4 (mod w).

If a prime ℓ divides x_w or z_w (write the relevant residue as a), each of

    ℓ ≡ −1 (mod w)  ⇒ d = nℓ,
    ℓ ≡ −a (mod w) ⇒ d = ℓ,
    ℓ² ≡ −a (mod w) ⇒ d = ℓ²

supplies a divisor d | n² in the target class −n.  Hence failure forbids those
prime-factor classes.  The first two classes need not be distinct: in Case A
they coincide for w = 3; in Case B they coincide when p ≡ 4 (mod w).  If
p ≡ −4 (mod w), Case B already succeeds with d = 1.  For composite w the
density of one reduced class is 1/φ(w), not 1/(w−1).

Conditioning p modulo 4w fixes a_B, but does **not** make full subset-product
avoidance multiplicative.  For example modulo 7 with target −1, 8 and 15 each
avoid the target among divisors of their squares, while 120 does not.  Only
the necessary prime-class slices above are multiplicative.

For simultaneous moduli w, conditioning costs the least common multiple L,
not merely notation: the parameter intervals have length about N/L.  For
prime w ≤ W, w ≡ 3 (mod 4), log L ~ W/2.  Therefore the old heuristic that
one could condition simultaneously through W = (log N)^{1.1} is impossible
(L > N).  The Phase-2 target W ≤ (log N)^{1−ε} remains arithmetically
compatible with conditioning; proving useful joint distribution is the real
missing step.

### 11.4 What Vaughan actually does (checked via a modern reconstruction)

Vaughan's 1970 PDF remained access-blocked, so this paragraph is **cited via**
Pomerance–Weingartner (2025), §4, whose proof says explicitly that it largely
follows Vaughan.  For an auxiliary prime q ≡ −1 (mod m), set M = (q+1)/m and

    f_m(q) = floor( 1/2 · ∑_{t|M} |μ(t)| τ(M/t) )
           = floor(τ(M²)/2).

Vaughan constructs at least f_m(q) good residue classes for the denominator n
modulo q.  One form of the identity is: factor M = uvw with (u,v)=1; if
nv ≡ −u (mod q) and nv+u = kq, then

    m/n = 1/(kuw) + 1/(nkvw) + 1/(nuvw).

Pomerance–Weingartner Lemma 4.1 proves

    ∑_{q≤X} f_m(q)/q ≍ (log X)²/φ(m).

Their §4 then applies the large sieve to integers avoiding all these good
classes and uses a Rankin tail for products of auxiliary primes.  Balancing
at log X ≍ φ(m)^{1/3}(log N)^{1/3} yields

    #{n≤N : m/n is not a sum of three unit fractions}
      ≪ N exp(−C (log N)^{2/3}/φ(m)^{1/3}).

For m=4 this is Vaughan's N exp(−c(log N)^{2/3}) bound, for **all integer
denominators**, hence also for primes.  Vaughan is not implicitly proving a
growing-k shifted-correlation theorem and is not stacking the full
subset-product condition; the previous claim to that effect was wrong.  As
of Pomerance–Weingartner, no published improvement of the 2/3 exponent was
found.

### 11.5 Corrected wave-four verdict

The empirical A/B near-independence and the fixed-pair Nair–Tenenbaum
calculation survive.  No new exceptional-prime theorem survived the primality
audit.  The useful open program is narrower: retain primality in a direct
many-root upper-bound sieve for the necessary slices, and treat the full
condition by genuinely nonmultiplicative subset-product methods.  Both are
executed, as far as they close, in the next section.

## 12. Phase five: the direct many-root sieve closes Phase 1

This section keeps primality, avoids every unspecified fixed-k constant, and
then pushes the full nonmultiplicative condition to an exact Fourier barrier.
The outcome is an independent criterion-route proof of a superlogarithmic
saving.  The bound itself is weaker than Vaughan's known theorem and is not
claimed as new in the literature.

### 12.1 An explicit-k sieve with no k-dependent prefactor

**Lemma 12.1 (many-root large sieve).** Let I be an interval containing X
integers.  For every prime ℓ in a finite set P, let Ω_ℓ be a set of ν(ℓ) < ℓ
residue classes.  If S ⊂ I avoids Ω_ℓ modulo ℓ for every ℓ ∈ P, define

    V = ∏_{ℓ∈P}(1−ν(ℓ)/ℓ),
    Λ = ∑_{ℓ∈P} ν(ℓ) log ℓ/ℓ.

If Λ ≤ (log X)/4, then

    |S| ≤ 4XV.                                                   (12.1)

The constant 4 is absolute: the number of conditions appears only in the
actual local root counts ν(ℓ).

*Proof.* Put g(ℓ)=ν(ℓ)/(ℓ−ν(ℓ)), extended multiplicatively to squarefree
numbers supported on P.  For each ℓ define the mean-zero function

    ψ_ℓ(a) = g(ℓ) if a ∉ Ω_ℓ, and ψ_ℓ(a) = −1 if a ∈ Ω_ℓ.

For squarefree q supported on P, let ψ_q=∏_{ℓ|q}ψ_ℓ.  Its Fourier expansion
modulo q is supported only on primitive frequencies (each prime component has
zero constant coefficient), and Parseval gives

    ∑*_{a (mod q)} |ψ̂_q(a)|² = g(q).

For n ∈ S, ψ_q(n)=g(q).  Cauchy–Schwarz applied to the Fourier expansion
therefore gives

    ∑*_{a (mod q)} |∑_{n∈S} e(an/q)|² ≥ g(q)|S|².                (12.2)

Summing (12.2) over q≤Q and applying the analytic large sieve yields

    |S| ≤ (X+Q²)/H(Q),       H(Q)=∑_{q≤Q} g(q),                 (12.3)

where this and all following q-sums run over squarefree q supported on P.

For completeness, set Z=∑_q g(q)=∏(1+g(ℓ))=V⁻¹ and regard g(q)/Z as a
probability distribution.  A prime ℓ occurs independently with probability
ν(ℓ)/ℓ, so the expected value of log q is Λ.  If log Q≥2Λ, Markov's inequality
gives H(Q)≥Z/2.  Taking Q=X^{1/2} proves (12.1).  The only cited input is the
standard analytic large-sieve inequality; all dependence on the local
conditions is displayed. ∎

This is the explicit-k mean-value result sought in Phase 1.  It is simpler
than Nair–Tenenbaum because the conditions are literal exclusions of roots in
one parameter, not arbitrary multiplicative weights on polynomial values.

### 12.2 The criterion supplies many distinct roots

Let

    𝒲 = {w≤W : w≡3 (mod 4)},       L = lcm(𝒲),
    M = lcm(24,4L),                R=M/4.

Condition p to a reduced class r modulo M with r≡1 (mod 24), and write
p=r+Mt.  For every w in 𝒲 the two criterion values are affine forms

    B_w(t)=Rt+(r+w)/4=(p+w)/4,
    A_w(t)=wRt+(wr+1)/4=(pw+1)/4.

A counterexample forces B_w to have no prime factor in

    C_B(w,r)={−1,−r/4} (mod w)

and A_w to have no prime factor in

    C_A(w)={−1,−1/4} (mod w),                              (12.4)

with repetitions removed.  This is the d=nℓ and d=ℓ sub-family of the
necessary slices in §11.3.  The valid ℓ² slice is discarded for simplicity;
including it could improve only the constant below.  A class with
r≡−4 (mod w) has no counterexamples because d=1 works.
For every remaining class and w>3, |C_A|=2 and |C_B|≥1.

Retain primality by adding P(t)=Mt+r and excluding its zero class modulo every
sieving prime.  The relevant pairwise determinants are

    det(P,B_u)=Ru,              det(P,A_u)=R,
    det(B_u,B_v)=R(v−u)/4,      det(A_u,A_v)=R(u−v)/4,
    det(B_u,A_v)=R(1−uv)/4.                                  (12.5)

Every prime factor of R is ≤W, and the remaining factors in (12.5) have
absolute value <W².  Hence at every sieving prime ℓ>W² all active roots are
distinct.  The exact local count is therefore

    ν_r(ℓ)=1 + ∑_{w∈𝒲} [1_{ℓ mod w∈C_A(w)}
                         +1_{ℓ mod w∈C_B(w,r)}].              (12.6)

There is no discriminant loss and no hidden dependence on the roughly W
linear forms.

### 12.3 A rigorous independently-derived exceptional-set bound

**Theorem 12.2.** There is an absolute c>0 such that

    #{p≤N prime : 4/p is not representable}
       ≪ N exp(−c(log log N)²).                               (12.7)

*Proof.* By Lemma 1.2 every prime outside p≡1 (mod 24) is already solvable.
It therefore suffices to count the remaining p in a dyadic interval (T,2T].
Take W=δ log T for a sufficiently small fixed δ>0.  Since
log lcm(1,…,W)=W+o(W), M≤T^{2δ} for large T, so every conditioned parameter
interval has length X≫T^{1−2δ}.

Two elementary estimates give, uniformly in r,

    c₁ log W ≤ 1 + ∑_{w∈𝒲} (|C_A|+|C_B|)/φ(w) ≤ c₂ log W.     (12.8)

For the lower bound, restrict to w=3m with m≡1 (mod 4):

    ∑_{w∈𝒲,w>3} 1/φ(w)
      ≥ ∑_{1<m≤W/3,m≡1(4)} 1/(3m) = (1/12)log W+O(1),

and (12.4) supplies at least three classes per w.  For the upper bound use
∑_{n≤W}1/φ(n)≪log W, which follows from
n/φ(n)=∑_{d|n}μ²(d)/φ(d) after summation.

Choose

    log z = log T/(A log W),       log y = (log z)^{1/2},

with A a sufficiently large absolute constant, and sieve only y<ℓ≤z.
Siegel–Walfisz, uniformly for every w≤W, and (12.6) give, for absolute
c₂ and A chosen sufficiently large,

    ∑_{y<ℓ≤z} ν_r(ℓ)logℓ/ℓ ≤ c₂(log W)log z ≤ (log X)/4,
    ∑_{y<ℓ≤z} ν_r(ℓ)/ℓ ≫ (log W)log(log z/log y)
                         ≫ (log log T)².                       (12.9)

The uniform error per residue class is
O(exp(−c₃(log y)^{1/2})); summing O(W) classes still gives o(1).  Starting the
sieve at y is load-bearing here: it removes uncontrolled accumulated Mertens
constants from the many moduli.  Also y>W², so the distinct-root calculation
applies, and z<T, so every prime
p in the dyadic interval avoids the zero root of P.  Lemma 12.1 and
log V≤−∑ν_r(ℓ)/ℓ now bound the counterexamples in each conditioned class by

    ≪ X exp(−c(log log T)²).

There are at most φ(M) reduced classes; the sum of their parameter-interval
lengths is O(T), so conditioning costs no extra factor.  Finally sum the
dyadic estimates (the intervals below T^{1/2} contribute O(T^{1/2})). ∎

**Status and comparison.** The constant c is absolute but ineffective because
of Siegel–Walfisz.  The proof is unconditional using the standard
analytic large sieve, Siegel–Walfisz, and the prime number theorem estimate
for the least common multiple, all used in their classical ranges.  It is
independent of Vaughan's many-good-classes construction.  It is stronger than
every fixed power of 1/log N but much weaker than
exp(−c(log N)^{2/3}); thus it is genuine Phase-1 progress but not the requested
exp-type fallback.

### 12.4 Exact formulation of the full condition

Conditioning was not the missing algebraic step.  There is a cleaner centered
form which removes x from the target entirely.

**Lemma 12.3 (signed subset-product criterion).** Let w be odd and (n,w)=1.
Write n=∏ℓ^{e_ℓ}.  A divisor d|n² satisfies d≡−n (mod w) iff

    ∏_ℓ ℓ^{k_ℓ} ≡ −1 (mod w) for some −e_ℓ≤k_ℓ≤e_ℓ.          (12.10)

*Proof.* Every divisor of n² has a unique expression
 d=n∏ℓ^{k_ℓ} in the stated exponent ranges, and n is invertible modulo w. ∎

Thus for either n=B_w(p) or n=A_w(p), full failure is exactly avoidance of
−1 by the signed subset products of the prime-factor residues.  The
set-valued signed-product map is multiplicative on coprime inputs, but the
predicate "this one target is absent" is not (§11.3's 8,15,120 example).

Let G=(Z/wZ)^× and let D(n) be the set of residues of divisors of n.  Equation
(12.10) says success is equivalent to

    −1 ∈ D(n)D(n)⁻¹.

In particular, |D(n)|>|G|/2 forces success, since D(n) and −D(n) must
intersect.  This is a useful deterministic sufficient condition, but it does
not control concentration in a proper subgroup.

### 12.5 Fourier large-deviation reduction (proved) and the transfer gap

For each copy g of a prime-factor residue of n, choose an exponent
ε∈{−1,0,1} uniformly.  For a character χ of G define

    q_χ(g)=(χ(g)⁻¹+1+χ(g))/3,
    M_χ(n)=−∑_g log|q_χ(g)|,

with M_χ=∞ when a factor vanishes.  Fourier inversion of this random signed
product proves:

**Lemma 12.4.** If full failure holds, some nontrivial χ satisfies

    M_χ(n) ≤ log(|G|−1).                                      (12.11)

Indeed the probability of the target −1 is |G|⁻¹ times 1 plus the sum over
nonprincipal characters.  If ∑_{χ≠1}exp(−M_χ)<1 it is positive; the
contrapositive and pigeonhole give (12.11).  For a uniform g∈G,

    E_g |q_χ(g)|² = 5/9 if χ has order 2, and 1/3 otherwise,   (12.12)

by character orthogonality.  Equations (12.11)–(12.12) put the empirical
"factor residues mix" claim into a precise additive large-deviation form.

The random-residue model itself can be settled sharply.

**Lemma 12.5 (random signed products).** Let G be a finite abelian group of
order h, let τ have order 2, and let g₁,…,g_K be independent uniform elements
of G.  If

    T=#{ε∈{−1,0,1}^K : ∑εᵢgᵢ=τ},       t=|G[2]|,

then

    E T=(3^K−1)/h,
    E T²≤9^K/h²+2(3^K−1)/h+t5^K/h²,

and hence

    P(T>0) ≥ (3^K−1)²/[9^K+2h(3^K−1)+t5^K].                 (12.13)

*Proof.* Every nonzero coefficient vector gives a uniform sum, proving the
first identity.  For a pair of coefficient vectors, a 2×2 minor equal to ±1
makes the map G^K→G² surjective, contributing 1/h².  The proportional pairs
are d=c or d=−c; because τ=−τ, there are at most 2(3^K−1) contributions of
size 1/h.  Every remaining nonsurjective rank-two pair has each coordinate in
{(0,0),±(1,1),±(1,−1)}, at most 5^K pairs.  In the basis (1,1),(1,−1), the
fiber over (τ,τ) has relative size t/h².  Summing these upper bounds gives the
second moment, and Paley–Zygmund gives (12.13). ∎

For G=(Z/wZ)^× with w odd, t=2^{ω(w)}=w^{o(1)}.  Given ε>0, choose fixed η>0
so that (1−η)log 3>1−ε and put K=⌊(1−η)log log N⌋.  Uniformly for
h≤w≤(log N)^{1−ε}, one has 3^K/h→∞ and t(5/9)^K→0, so (12.13) tends to 1.
Thus the desired Phase-2 contraction is rigorously true in the independent
uniform-residue model, through the full target range.

What did **not** close is transferring that model to B_w(p),A_w(p) while p
remains prime.  A sufficient input would be a growing-order, residue-marked
Sathe–Selberg estimate along the prime affine form: first ensure at least K
usable distinct prime factors, then reproduce the aggregate first and second
moments in Lemma 12.5, uniformly in w and jointly for both forms.  This needs
factorial moments through order about 2K and enough uniformity to sum the 9^K
coefficient pairs.  Bombieri–Vinogradov controls each averaged divisibility
congruence up to level N^{1/2}; it does not by itself provide the required
relative high-moment estimate after the residue-product constraints and the
primality condition are imposed.

This is the exact Phase-2 stopping point.  The signed-product, Fourier, and
random-model lemmas are proved; the contraction ρ<1 for the **actual shifted
values** is not.  Therefore no bound N exp(−c(log N)^θ), for any θ>0, is
claimed from this route, and Vaughan's θ=2/3 record is not improved.
*(Superseded in part: §13 extracts an unconditional positive power θ = 1/8
from (12.11) by hard discretization; the full contraction, and every θ ≥
log 3/2, remain open there — see §13.3–13.4 for the precise ceilings.)*

---

## 13. Phase six: hard level thresholds turn the Fourier bound into a
positive power

§12.5 stopped because the contraction was only proved in a random-residue
model.  This section avoids the model entirely.  The Fourier inequality
(12.11) is discretized into **hard divisibility events** — counts of prime
factors in level sets of |q_χ| — which the many-root sieve (Lemma 12.1) can
process after conditioning on the exceptional factor patterns.  The union
cost over characters and patterns is paid explicitly, and it caps the
exponent well below Vaughan's 2/3; but it closes, and yields the
unconditional theorem (§13.5 then completes the single-modulus transfer
H1′/H2′ of §13.4)

    E(N) := #{p ≤ N prime : 4/p not representable}
          ≤ N exp(−(log N)^{1/8})            (N large).        (13.1)

This is the positive-power fallback named in the project brief: far stronger
than Theorem 12.2's exp(−c(log log N)²), independent of Vaughan's
many-good-classes construction, and still weaker than Vaughan's published
exp(−c(log N)^{2/3}).  It is **not** a literature record; it is a second,
criterion-native method that keeps primality.  §13.3 computes the ceilings
of the method; §13.4 states the sharpened residual gap.

### 13.1 Level thresholds and the rate certificate

Throughout, p ≡ 1 (mod 24) is a counterexample prime (Lemma 1.2), w ≡ 3
(mod 4), h = φ(w), G = (Z/wZ)^×, and n is either criterion half; (n,w) = 1
as before: for the B-half a common prime q | w and (p+w)/4 would divide
p = (p+w) − w, impossible for p prime > w; for the A-half, 4n = pw + 1
forces (n, w) = 1 directly.
For nontrivial χ mod w define the disjoint class sets

    S₀(χ) = {g : q_χ(g) = 0},
    S₁(χ) = {g : 1/20 < |q_χ(g)| ≤ 1/3},
    S₂(χ) = {g : 0 < |q_χ(g)| ≤ 1/20}.

**Lemma 13.1 (hard thresholds).**  Full failure at (w, n) implies that some
nontrivial χ mod w satisfies both

    (i)  n has no prime factor in S₀(χ);
    (ii) Ω₁ log 3 + Ω₂ log 20 ≤ log(h−1),

where Ω_j counts prime factors of n in S_j(χ) with multiplicity.  Both
conclusions persist a fortiori when the factors are restricted to any
subrange of primes.

*Proof.*  Take χ from Lemma 12.4, so M_χ(n) ≤ log(h−1) < ∞.  Every copy
contributes −log|q_χ| ≥ 0; copies in S₀ contribute +∞ (so there are none),
copies in S₁ at least log 3, copies in S₂ at least log 20.  Dropping copies
outside a subrange only lowers the left side of (ii). ∎

If χ has exact order d, then χ: G → μ_d is a surjective homomorphism, so
each value e(a/d) is taken on exactly h/d classes and the densities
σ_j(d) = |S_j(χ)|/h depend only on d: with v(a) = |1 + 2cos(2πa/d)|/3,

    σ₀(d) = (2/d)·1_{3|d},   σ_j(d) = #{a : v(a) ∈ range_j}/d.

For μ ≥ 0 put the tilted rate

    ρ_d(μ) = σ₀(d) + (1−3^{−μ})σ₁(d) + (1−20^{−μ})σ₂(d),

and its continuum analogue ρ_∞(μ) with the arc measures of θ ↦
|1+2cos θ|/3 (σ₁^∞ = 0.44473…, σ₂^∞ = 0.05527…, σ₀^∞ = 0).

**Rate certificate (finite closed checks; `verify.py (h)`).**  With
γ = 1/8, s₀ = 0.84, c₁ = 0.015 and μ ranging over the grid
{0, 0.01, …, 3}:

    (C1)  R(d) := max_μ [ s₀ ρ_d(μ) − μγ ] ≥ 0.099 > c₁  for all d ≥ 2;
    (C2)  R_∞  := max_μ [ s₀ ρ_∞(μ) − μγ ] = 0.1692… ≥ γ + 2c₁ + 24s₀/3000.

Each level preimage in θ is a union of at most 4 arcs (|1+2cos θ| falls
3→0 then rises 0→1 on [0, π], and is symmetric), so counting the d-th
roots of unity in those arcs gives |σ_j(d) − σ_j^∞| ≤ 8/d and hence

    R(d) ≥ R_∞ − 24 s₀/d                                       (13.2)

for every d.  The certificate checks d ≤ 3000 exactly (worst case d = 5,
R = 0.0990, from σ₁(5) = 2/5); (13.2) covers d > 3000.  Boundary values
|q| = 1/3 are placed in S₁ by the lemma; the verification code may drop
such boundary cases by floating-point strictness, which only lowers the
certified R(d) — the safe direction.

### 13.2 The positive-power theorem

**Theorem 13.2.**  For all sufficiently large N,

    E(N) ≤ N exp(−(log N)^{1/8}).

The constant threshold is ineffective (Siegel–Walfisz, as in Theorem 12.2).

*Proof.*  Set L = log log N, γ = 1/8, Y = (log N)^γ, and

    𝒲 = {w ≡ 3 (mod 4) : Y/2 < w ≤ Y},      |𝒲| = Y/8 + O(1).

Counterexamples p ≤ N^{1/2} are absorbed into the final bound; assume
p > N^{1/2}, p ≡ 1 (mod 24), and write p = 24s + 1.  For each w ∈ 𝒲 the
two criterion halves are the integer affine forms

    B_w(s) = 6s + (w+1)/4 = (p+w)/4,
    A_w(s) = 6ws + (w+1)/4 = (pw+1)/4,

together with P(s) = 24s + 1 = p.  Pairwise determinants:

    det(P, A_w) = 6,             det(P, B_w) = 6w,
    det(B_w, B_{w'}) = det(A_{w'}, A_w) = (3/2)(w'−w),
    det(B_w, A_{w'}) = (3/2)(1 − ww'),                        (13.3)

all nonzero and of absolute value ≤ 2Y².  Fix the sieve range

    y = exp(Y^{1/16}),        log z = (log N)^{1−γ}/L,

so that log log z − log log y = (1 − γ − γ/16 + o(1))L ≥ 0.85 L =: L₁ for
large N.  Mertens in arithmetic progressions with Siegel–Walfisz uniformity
(valid since every w ≤ Y = (log y)^{16}) gives, for each reduced class g
mod w,

    ∑_{y<ℓ≤z, ℓ≡g (w)} 1/ℓ = L₁'/φ(w)·(1 + o(1)),             (13.4)

with L₁' := log log z − log log y.  (13.4) follows from the Siegel–Walfisz
theorem, π(t; w, g) = li(t)/φ(w) + O(t·exp(−c√(log t))) uniformly for
w ≤ (log t)^{16}, by partial summation over (y, z]; the differenced range
kills the Mertens constants.  The accumulated error over all O(Y) moduli
and ≤ Y classes each is O(Y² exp(−c√(log y))) = o(1) because
√(log y) = exp(γL/32) beats 2γL.  Hence for any union S of classes of
density σ, the sum (13.4) over S is σ L₁'(1+o(1)) ≥ σ s₀ L with
s₀ = 0.84, for large N.

**The union.**  By Lemma 13.1, a counterexample p determines, for each of
the 2|𝒲| pairs (w, H), H ∈ {A, B}, a nontrivial character χ_{w,H} mod w
satisfying (i)–(ii) for n = H_w(p).  Fix the vector χ⃗ = (χ_{w,H}) (union
bound at the end).  For each (w,H) let a_{w,H} be the exact part of
H_w(p) supported on primes ℓ ∈ (y, z] with ℓ mod w ∈ S₁ ∪ S₂ (multiplicity
included).  By (ii),

    3^{Ω₁(a)} 20^{Ω₂(a)} ≤ h − 1,                              (13.5)

where Ω_j(a) counts the prime factors of a = a_{w,H} in S_j(χ_{w,H});
in particular Ω(a) ≤ log(h−1)/log 3 ≤ γL/log 3 and a ≤ z^{γL/\log 3}.
Call such a **admissible**.  The total conditioning modulus obeys

    ∏_{w,H} a_{w,H} ≤ z^{2|𝒲|·γL/\log 3} ≤ N^{0.03}.           (13.6)

**The cell sieve.**  Fix χ⃗ and admissible a⃗ = (a_{w,H}).  Each prime
power ℓ^e ∥ a_{w,H} forces H_w(s) ≡ 0 (mod ℓ^e), one class modulo ℓ^e
(the leading coefficients 6, 6w are units at every ℓ > y).  By CRT the
conditions pin s to at most one class modulo Q₀ := ∏_{w,H} a_{w,H} when
the a's are pairwise coprime; if two a's share a prime, the distinct-root
computation below makes the cell empty, and using the product Q₀ anyway
only weakens the upper bound.  Reparametrize s = s₀ + Q₀u.  Since s
ranges over [0, N/24), the u-interval has length X' with

    N/(24Q₀) − 1 ≤ X' ≤ N/(24Q₀) + 1,

and Q₀ ≤ N^{0.03} by (13.6), so X' = (1+o(1))·N/(24Q₀) and
log X' ≥ 0.96 log N.  Sieve with the prime set
P' = {ℓ ∈ (y, z] : ℓ ∤ 6∏a⃗}, excluding for each ℓ ∈ P':

    * the class with ℓ | P(s)  (valid: p > N^{1/2} > z is prime);
    * for each (w,H) with ℓ mod w ∈ S₀ ∪ S₁ ∪ S₂ (for χ_{w,H}): the class
      with ℓ | H_w(s) — valid because a_{w,H} already carries the **entire**
      (S₁∪S₂)-part of H_w(p) in (y,z], and S₀ has no factors at all by (i).

In the u-variable every determinant in (13.3) is multiplied by Q₀, which
is a unit modulo each ℓ ∈ P' (ℓ ∤ ∏a⃗, ℓ > y > 6); so the pairwise
distinctness of roots is preserved.  By (13.3) all determinants are
< y < ℓ and the leading coefficients are prime to ℓ, so

    ν(ℓ) = 1 + ∑_{w,H} 1_{ℓ mod w ∈ S₀∪S₁∪S₂(χ_{w,H})} < 1 + Y < ℓ.

Lemma 12.1 applies: Λ ≤ (1+Y)(log z + O(1)) ≤ (1+o(1))(log N)/L ≤
(log X')/4 since log X' ≥ 0.96 log N.  Therefore the number of
surviving u in the cell is at most 4X'V with

    log V ≤ −∑_{ℓ∈P'} ν(ℓ)/ℓ ≤ −∑_{w,H} (λ₀ + λ₁ + λ₂)(χ_{w,H}) + o(1),

where, exactly,

    λ_j(χ_{w,H}) := ∑_{y<ℓ≤z, ℓ mod w ∈ S_j(χ_{w,H})} 1/ℓ
                  = σ_j(d)·L₁'·(1+o(1))                          (13.4')

by (13.4) summed over the σ_j·h classes of S_j; the primes removed with
∏a⃗ contribute ≤ 2|𝒲|·γL·(1+Y)/y = o(1) to the middle expression, and
the discarded ℓ ∤ P(s) exclusion only strengthens V.

**Tilted pattern sum.**  Sum over admissible a⃗ at fixed χ⃗.  The sum
factorizes over (w,H).  For one pair, using the tilt μ = μ(d) ≥ 0 from the
rate certificate (d = order of χ) and (13.5),

    ∑_{a admissible} 1/a
      ≤ (h−1)^μ ∑_{supp(a) ⊂ (S₁∪S₂)∩(y,z]} 3^{−μΩ₁(a)} 20^{−μΩ₂(a)}/a
      ≤ (h−1)^μ ∏_{ℓ∈S₁∩(y,z]} (1 − 3^{−μ}/ℓ)^{−1}
                 ∏_{ℓ∈S₂∩(y,z]} (1 − 20^{−μ}/ℓ)^{−1}
      ≤ exp( μγL + 3^{−μ}λ₁ + 20^{−μ}λ₂ + o(1) ).

Combining with the V-factor for the same pair,

    e^{−λ₀−λ₁−λ₂} ∑_{a} 1/a ≤ exp(−R(d)·L·(1−o(1))),              (13.7)

using λ_j ≥ σ_j s₀ L (large N) for the negative terms and log(h−1) ≤ γL
for the positive ones.

**Character union per pair.**  G is a product of ω(w) cyclic groups (w
odd), so #{χ : χ^d = 1} ≤ d^{ω(w)} and ω(w) ≤ (1+o(1))γL/log(γL).  Split
at d* = exp(c₁L log(γL)/(2γL)) → ∞:

    * d ≤ d*: at most d*^{ω+1} = e^{(c₁/2)L(1+o(1))} characters in total,
      each contributing ≤ e^{−R(d)L(1−o(1))} ≤ e^{−c₁L(1−o(1))} by (C1);
    * d > d*: at most h − 1 ≤ e^{γL} characters, each contributing
      ≤ e^{−(R_∞ − 24s₀/d*)L(1−o(1))} ≤ e^{−(γ + 2c₁)L(1−o(1))}
      by (13.2) and (C2).

Either way the per-pair union U := ∑_{χ≠1} (13.7) obeys
U ≤ e^{−(c₁/3)L} for large N, uniformly in (w,H).

**Assembly.**  Sum 4X'V over cells at fixed χ⃗, using
X' ≤ (1+o(1))N/(24∏a) and the factorized tilted sums; then sum over χ⃗:

    E(N) ≤ N^{1/2} + (1+o(1))·(N/6) ∏_{w,H} U_{w,H}
         ≤ N exp( −2|𝒲|(c₁/3)L )
         ≤ N exp( −0.001·(log N)^{1/8} log log N )

for large N, which is ≤ N exp(−(log N)^{1/8}) once log log N ≥ 1000/c₁.  ∎

**Status.**  Unconditional modulo the stated finite certificate; inputs
are Lemma 12.1 (proved in §12.1), Lemma 12.4 (proved in §12.5), Lemma
13.1, the Siegel–Walfisz theorem via partial summation (13.4), and the
rate certificate.  On the certificate's rigor: σ₀(d) and the 1/3-level
membership are decided by **exact integer comparisons** (q_χ = 0 iff
3 | d and 3a ∈ {d, 2d}; |q| ≤ 1/3 iff d ≤ 4a ≤ 3d), so only the interior
1/20-level split relies on binary64 cosines, and there a 10⁻⁹ safety band
classifies every borderline value to the side that lowers R(d) — the
pessimistic direction; asserted margins exceed 10⁻².  The exponent 1/8 is
chosen for clean margins, not optimized; see §13.3.

### 13.3 The ceilings of this route — why 2/3 stays out of reach

Three ceilings, in increasing order of importance.

1. **Level refinement.**  Replacing the two levels (1/3, 1/20) by a fine
   partition sends the per-pair rate to its Chernoff limit
   sup_μ [(1−γ)(1 − m(μ)) − μγ] with m(μ) = ∫₀^{2π} (|1+2cos θ|/3)^μ
   dθ/2π.  The largest γ for which this exceeds γ (the character-union
   cost) is the crossover of that continuum relaxation, numerically
   estimated at γ* ≈ 0.207 by grid/quadrature in `verify.py (h)` (not a
   certified constant).  So the method of §13.2, fully optimized, proves
   every θ below ≈ 0.2 and — by the union-cost structure — no more.

2. **The pigeonhole ceiling log 3/2 ≈ 0.549.**  For any order-2 character,
   M_χ(n) = (log 3)·#{copies with χ = −1}, and this count has normal order
   (1/2)·log log n.  Hence for w ≥ (log N)^{log 3/2 + ε} the threshold
   log(h−1) in (12.11) exceeds the **typical** value of M_χ: Lemma 12.4's
   necessary condition is satisfied by almost all integers, and carries no
   information whatsoever.  (Calibration only: the normal-order claim is
   a Turán-variance computation for marked factor counts of the shifted
   values, not written out here and not used elsewhere.)  At calibration
   level, then, an argument that uses (12.11) alone — one modulus at a
   time, first moment only — loses all its information beyond
   θ = log 3/2 = 0.5493…, in particular before 2/3.  Lemma 12.5 evades
   this only via second moments of T itself — the transfer of which is
   precisely the open gap.

3. **The identity-class ceiling behind Vaughan's 2/3.**  In the
   Pomerance–Weingartner reconstruction (§11.4), the large sieve is fed
   ∑_{q≤X} f_m(q)/q ≍ (log X)² good classes and the support cost is
   Λ ≍ (log X)³; balancing Λ ≍ log N gives exp(−c(log N)^{2/3}).  In
   general, class density ∑ ν(q)/q ≍ (log X)^A yields θ = A/(A+1).
   Vaughan's A = 2 comes from τ(M²)-many divisor-pair classes per
   auxiliary prime; a proof of θ = 3/4 by the same outer argument would
   need A = 3, i.e. τ³-dense *universal* one-modulus classes, which the
   identity structure does not supply (each class comes from a
   factorization M = uvw, and their number per modulus is a divisor
   function).  Assessment, not a theorem: within the
   one-modulus-sufficient-class + large-sieve paradigm, 2/3 is a
   structural ceiling, and any improvement must use genuinely joint
   multi-modulus conditions — exactly the subset-product events whose
   transfer is the remaining gap.

### 13.4 The sharpened residual gap

§12.5 asked for a growing-order residue-marked Sathe–Selberg theorem along
the prime affine forms.  That demand can be **weakened**.  Recall (§12.4)
that for d | n, d ≡ −n (mod w) iff n/d ≡ −1 (mod w); so define, for one
half n = n_w(p) and the truncation d ≤ N^{1/4},

    T₀(n) = #{d | n : d ≡ −1 (mod w), d ≤ N^{1/4}}.

T₀ > 0 is a sufficient condition for success at (w, n) (it uses only
divisors of n, not of n²).  Two warnings, both paid for already:

* **Over-dispersion.**  Unconditioned second moments fail: by Lemmas
  13.4–13.5 below, E T₀ ≫ (log N)/h while E T₀² ≪ (log N)³/h², so
  Paley–Zygmund gives only P(T₀ > 0) ≫ 1/log N (Corollary 13.6) — the
  classic Erdős/Ford divisor-concentration phenomenon.  Conditioning on
  the factor count is essential to do better.

* **The k! wall for naive moment transfer.**  Reproducing the marked
  moments of Lemma 12.5 to order 2K, K ≍ log log N, via
  Bombieri–Vinogradov costs a tuple-multiplicity (2K)! =
  exp(2(1+o(1)) L log L), while BV saves only (log N)^{−A} = e^{−AL} for
  fixed A.  Since log L → ∞, fixed-level BV cannot pay for growing-order
  moments by itself.  This multiplicity accounting is elementary but is a
  back-of-envelope obstruction, not a nonexistence theorem; it explains
  why the §12.5 demand resists the standard toolchain.

**What the unconditioned toolchain does prove.**  The first moment, and a
second-moment upper bound, for divisor witnesses along the **actual
shifted primes** are provable today; only the conditioning is not.
Restrict to the B-half n = (p+w)/4 and to witnesses coprime to 6 (a
smaller count, still sufficient for solvability); write h = φ(w),
X = N^{1/4},

    T'(n) = #{d | n : d ≤ X, (d,6) = 1, d ≡ −1 (mod w)}.

**Lemma 13.3 (character averages are benign; proved).**  For odd w ≥ 3,
χ a nonprincipal character mod w, and every X ≥ 2,

    A_χ(X) := ∑_{d ≤ X, (d,6)=1} χ(d)/φ(d) ≪ log 6w,

with an absolute implied constant, uniformly in X.

*Proof.*  Insert 1/φ(d) = (1/d)∑_{m|d} μ²(m)/φ(m):

    A_χ(X) = ∑_{(m,6)=1} μ²(m)χ(m)/(mφ(m)) · ∑_{e ≤ X/m, (e,6)=1} χ(e)/e.

The inner summand is χ'(e)/e with χ' = χ·(principal mod 6), a
nonprincipal character to a modulus dividing 6w, so Pólya–Vinogradov
bounds its partial sums by √(6w) log 6w; splitting at E₀ = √(6w) log 6w
and summing by parts, |∑_{e≤T} χ'(e)/e| ≤ log E₀ + O(1) ≪ log 6w for
every T.  The outer sum converges absolutely to O(1). ∎

**Lemma 13.4 (unconditioned first moment; proved).**  Uniformly for
3 ≤ w ≤ (log N)^{1−ε}, w ≡ 3 (mod 4),

    ∑_{p ≤ N, p ≡ 1 (24)} T'((p+w)/4) = li(N)·(c_w + o_ε(1))·(log N)/h,

where c_w ≍ 1 with absolute constants.

*Proof.*  For (d,6) = 1, d ≡ −1 (mod w): d | (p+w)/4 together with
p ≡ 1 (mod 24) pins p to a single class modulo 24d (the 2-part is
compatible because w ≡ 3 mod 4, the 3-part because (d,3) = 1), and the
class is invertible: a common prime q | d and q | p + w would divide p,
impossible for p > w prime.  Bombieri–Vinogradov at level
24X = 24N^{1/4} ≪ N^{1/2} (one fixed class per modulus 24d) gives

    ∑_p T' = li(N) ∑_{d≤X, (d,6)=1, d≡−1(w)} 1/φ(24d) + O(N(log N)^{−3}).

Since φ(24d) = 8φ(d) for (d,24) = 1, orthogonality of characters mod w
splits the d-sum into the principal part
(1/8h)·∑_{d≤X,(d,6w)=1} 1/φ(d) = (c_w/h)·(log X)·(1 + O(log 6w/log X))
— a Mertens-type sum whose constant is bounded above and below
absolutely, the local factors at ℓ | w changing it by
exp(O(∑_{ℓ|w} 1/ℓ)) = O(1) — and at most h − 1 nonprincipal terms,
each O(log 6w)/(8h) by Lemma 13.3, so O(log 6w) in total.  The
nonprincipal-to-principal ratio is ≪ h log(6w)/log N ≤
(log N)^{−ε}·O(log log N) = o_ε(1): this is exactly where
w ≤ (log N)^{1−ε} enters.  Finally log X = (log N)/4. ∎

**Lemma 13.5 (unconditioned second moment, upper bound; proved).**
Uniformly in the same range,

    ∑_{p ≤ N, p ≡ 1 (24)} T'((p+w)/4)² ≪ N (log N)²/h².

*Proof.*  T'² = ∑_{d₁,d₂} 1_{[d₁,d₂] | n}, [d₁,d₂] ≤ X² = N^{1/2}, and
p lies in one invertible class modulo 24[d₁,d₂]; Brun–Titchmarsh gives
≪ N/(φ([d₁,d₂]) log N) per pair.  Write d_i = g e_i with g = (d₁,d₂),
(e₁,e₂) = 1; then φ([d₁,d₂]) ≥ φ(g)φ(e₁)φ(e₂) and e_i ≡ −g⁻¹ (mod w),
so

    ∑_{pairs} 1/φ([d₁,d₂])
      ≤ ∑_{g≤X} (1/φ(g)) [ ∑_{e≤X,(e,6)=1, e≡−g⁻¹(w)} 1/φ(e) ]²
      ≪ (log X)·((log X)/h + log 6w)² ≪ (log N)³/h²,

the inner sum again by orthogonality plus Lemma 13.3, the last step by
h log 6w ≪ log N. ∎

**Corollary 13.6 (the unconditioned frontier; proved).**  Uniformly for
w ≤ (log N)^{1−ε},

    #{p ≤ N, p ≡ 1 (24) : (p+w)/4 has a divisor ≡ −1 (mod w), ≤ N^{1/4}}
      ≫ li(N)/log N,

by Cauchy–Schwarz from Lemmas 13.4–13.5.  The lost factor 1/log N is
exactly the over-dispersion: the mean of T' is carried by rare
divisor-rich n, and unconditioned second moments can certify no more.
Turning ≫ 1/log N into ≥ 1 − ρ per modulus is precisely the
ω-conditioning content of H1–H2 below — that, and nothing else, is now
the open analytic input.

The conditioned targets.  Let A_k = {p ≤ N : ω(n_w(p)) = k} and
let k range over the Erdős–Kac window |k − L| ≤ C√L (Turán for shifted
primes puts all but O(C^{−2})·π(N) primes there).  Sufficient inputs:

    (H1)  E[ T₀ · 1_{A_k} ]  =  (model value)·(1 + o(1)),
    (H2)  E[ T₀² · 1_{A_k} ] =  (model value)·(1 + o(1)),

uniformly for w ≤ (log N)^{1−ε} and k in the window, where the model
values are computed from k iid uniform residues (Lemma 12.5 supplies
their asymptotics; note E[T₀²|k]/E[T₀|k]² → 1 there).  By Cauchy–Schwarz
P(T₀ > 0 ∧ A_k) ≥ E[T₀ 1_{A_k}]²/E[T₀² 1_{A_k}], so H1 + H2 give
per-modulus failure probability ≤ ρ < 1; a third, w-joint version (H3)
would stack the moduli and give every θ < 1 − ε.

**The tilted second moment removes the conditioning (proved, in the
model).**  Both H1 and H2 can be weakened further.  Tilting the counting
variable by θ^{ω(n)} suppresses the divisor-rich outliers that cause the
over-dispersion, and at θ = 1/2 the Paley–Zygmund ratio becomes 1 − o(1)
with **fixed-order** moments only:

**Lemma 13.7 (tilted subset-product moments).**  Let G be abelian of
order h, τ ∈ G, τ ≠ 1.  Let K be Poisson(λ), and given K let
g₁,…,g_K be iid uniform on G.  Put T = #{S ⊆ {1,…,K} :
∏_{i∈S} g_i = τ} and U = 2^{−K}T.  Then

    E U = (1 − e^{−λ/2})/h,
    E U² ≤ h^{−2}(1 + 3h e^{−λ/2} + h e^{−3λ/4}),

and hence, by Cauchy–Schwarz,

    P(T > 0) ≥ (1 − e^{−λ/2})² / (1 + 3h e^{−λ/2} + h e^{−3λ/4})
             = 1 − O(h e^{−λ/2} + e^{−λ/2}).

In particular P(T = 0) = o(1) whenever h ≤ e^{(1/2−ε)λ}.

*Proof.*  By orthogonality, for k fixed and χ running over characters,
E[T | K = k] = h^{−1}∑_χ χ̄(τ)·(E_g(1+χ(g)))^k = (2^k − 1)/h, since
E_g(1+χ(g)) = 2 for χ principal and 1 otherwise, and
∑_{χ≠χ₀}χ̄(τ) = −1 for τ ≠ 1.  Averaging 2^{−k}(2^k−1)/h over
K ~ Poisson(λ), with E x^K = e^{λ(x−1)}, gives E U.  For the second
moment, E[T² | K = k] = h^{−2}∑_{χ₁,χ₂} χ̄₁(τ)χ̄₂(τ)·m(χ₁,χ₂)^k where
m = E_g(1+χ₁(g))(1+χ₂(g)) = 1 + 1_{χ₁=χ₀} + 1_{χ₂=χ₀} + 1_{χ₁χ₂=χ₀}.
So m = 4 on the principal pair; m = 2 in exactly three families —
χ₁ = χ₀ ≠ χ₂, χ₂ = χ₀ ≠ χ₁, and χ₂ = χ̄₁ ≠ χ₀ — together at most 3h
pairs, each with coefficient χ̄₁(τ)χ̄₂(τ) of modulus 1; and m = 1 on the
remaining pairs, whose total coefficient is exactly
∑_{χ₁≠χ₀, χ₂∉{χ₀,χ̄₁}} χ̄₁(τ)χ̄₂(τ) = 1 − (h−1), at most h in absolute
value.  Hence

    E[T² | K = k] ≤ h^{−2}(4^k + 3h·2^k + h·1^k),

and averaging 4^{−k}·(·) over Poisson(λ) gives E U² ≤
h^{−2}(1 + 3h e^{−λ/2} + h e^{−3λ/4}).  Cauchy–Schwarz:
P(T > 0) ≥ (E U)²/E U². ∎

Three remarks.  (i) This **supersedes Lemma 12.5 at per-modulus level**:
only subset (squarefree-divisor) products are needed, not signed
exponent vectors, and only first and second tilted moments — nothing of
growing order.  (ii) The admissible range h ≤ e^{(1/2−ε)λ}, i.e.
w ≤ (log N)^{1/2−ε} after the calibration λ ≈ log log N, is narrower
than Lemma 12.5's (log N)^{1−ε} but far beyond anything reachable
before.  (iii) Numerically (verify.py (j)): at λ = 32, w = 31, the
untilted ratio is 0.0003 (over-dispersion collapse) while the tilted
ratio is 1.0000 — the cure is exact in the model.

**Revised transfer targets (supersede H1–H2 for one modulus).**  Fix a
window W = {primes ≤ exp(√(log N))} and let ω_W(n) count distinct
W-prime factors of n.  The needed inputs become

    (H1')  ∑_{p≤N, p≡1(24)} 2^{−ω_W(n)} T'(n)  =  (model)(1+o(1)),
    (H2')  ∑_{p≤N, p≡1(24)} 4^{−ω_W(n)} T'(n)² ≤  (model)(1+o(1)),

uniformly for w ≤ (log N)^{1/2−ε}, with n = (p+w)/4 and T' as above.
Both are **fixed-order and tail-controlled**: 2^{−ω_W(n)} =
∑_{m | n, m sqfree, W-smooth} (−1/2)^{ω(m)}, the m > N^{1/8} tail is
Rankin-negligible because a W-smooth m > N^{1/8} has ≥ (log N)^{1/2}/8
prime factors (so (1/2)^{ω(m)} ≤ exp(−c√(log N)) beats everything), and
the resulting Bombieri–Vinogradov moduli 24[d,m] ≤ N^{1/2} carry only
τ-bounded multiplicities — powers of log N, not the k! of the growing-
order route.  So H1'–H2' are Selberg–Delange × BV hybrid computations
with no structural wall in sight; proving them, and then the w-joint
version (H3) for stacking, is the successor unit.  With H1'–H2' alone:
per-modulus failure probability o(1) uniformly to w ≤ (log N)^{1/2−ε},
already far beyond every ceiling in §13.3 at single-modulus level.
**(Executed: §13.5 proves them, in window form — Lemmas 13.9–13.10 and
Theorem 13.11.  One structural wall did appear — the L(1,χ)-sized bias
of the small primes — and is bypassed there by flooring the window.)**

The remainder of this subsection keeps the older ω-conditioned targets
for the record; they are now a fallback formulation.  H1–H3 are stated
targets, their model values are defined by the iid-residue model, and
the implication chain is only as strong as those inputs.  Both H1 and H2
are **fixed-order** statements: sums of
#{p : lcm(d₁,d₂) | n_w(p), ω(n_w(p)) = k} over pairs of divisors below
level N^{1/2} — i.e. Selberg–Delange/Sathe-type asymptotics along shifted
primes in progressions, on average over the progression modulus (a
Bombieri–Vinogradov flavor for ω-restricted shifted primes).  The
character-sum side is benign at the unconditioned level — that is
exactly Lemma 13.3, driving Lemmas 13.4–13.5 — and its ω-restricted
analogue is plausibly benign too (heuristic there).  The hard part is the joint (AP-average ×
ω-restriction × primality) uniformity.  This is the sharpened Phase-2
gap: **two fixed-order BV-average Sathe–Selberg asymptotics (H1, H2),
plus their w-joint version (H3), would imply every θ < 1**.  Nothing
beyond fixed second order is demanded by the target — that is the
reduction; proving H1–H3 is the successor project.

### 13.5 H1′/H2′ proved: the window form of the tilted transfer

The two open inputs of §13.4 are proved here in a slightly modified
("window") form which supersedes the literal H1′/H2′ statements: it feeds
the identical Paley–Zygmund step and delivers the full per-modulus
conclusion — failure probability o(1), uniformly for w ≤ (log N)^{1/2−ε}
(Theorem 13.11).  The modification is forced by an honest obstacle,
recorded first because it is instructive.

**Why the small primes must leave the window.**  With W ⊇ {q ≤ w^{O(1)}}
as in the literal H1′ display, the second-moment character decomposition
contains, for every pair (χ₁, χ₂) of nonprincipal characters mod w with
χ₁χ₂ nonprincipal, an Euler product of shape
∏_{q∈W}(1 + (χ₁+χ₂+χ₁χ₂)(q)/O(q)).  Its modulus is
exp(O(Re ∑_q χᵢ(q)/q)) — an L(1,·)-sized quantity, as large as
(log w)^{3/4} — and there are ≈ h² such pairs against a main term that
beats each of them only by (log z)^{3/4}.  Absolute-value estimates
therefore cap the range at h² ≪ (log z/log w)^{3/4}: even after
enlarging the window top to z = exp((log N)^{1−ε/2}) this is
w ≲ (log N)^{3/8}, and for the literal H1′ window z = exp(√(log N)) it
is only w ≲ (log N)^{3/16}.  One can check the loss is carried entirely by the
primes q ≤ w^{O(1)}, because above that height Siegel–Walfisz makes every
character sum over primes cancel.  Those small primes contribute only
κ·log log N to λ = ∑_{q∈W} 1/q if deleted up to exp((log N)^κ), while
carrying all of the L(1,χ) bias.  Deleting them costs an ε-sliver of the
range and buys uniform 1+o(1) control of every nonprincipal Euler
product.  (This paragraph is a proof-level obstruction to our estimates,
not a nonexistence theorem; the fix follows.)

**Setup.**  Fix ε ∈ (0, 1/2) and put

    z₀ = exp((log N)^{ε/2}),   z = exp((log N)^{1−ε/2}),
    W = {q prime : z₀ < q ≤ z},   λ = ∑_{q∈W} 1/q,

so that, by Mertens, λ = (1−ε)·log log N + O((log N)^{−ε/2}) and
e^{−λ/2} = (log N)^{−(1−ε)/2}(1+o(1)).  For N large every q ∈ W exceeds
(log N)^{1/2} ≥ w, so q ∤ 6w automatically — all coprimality below is
free.  Fix w ≡ 3 (mod 4), 3 ≤ w ≤ (log N)^{1/2−ε}, put h = φ(w), and for
p ≡ 1 (mod 24) set n = n_w(p) = (p+w)/4.  Define

    T″(n) = #{d | n : d squarefree, all prime factors in W,
                      d ≤ X, d ≡ −1 (mod w)},        X = Y = N^{1/8},
    U(n)  = 2^{−ω_W(n)} T″(n),

where ω_W(n) = #{q ∈ W : q | n}.  T″ ≤ T′ up to the harmless truncation
change (every counted d is a divisor of n coprime to 6w), so T″ > 0
still triggers the criterion.  All implied constants below depend on ε
alone; Siegel–Walfisz makes them ineffective.

**Lemma 13.8 (window character sums cancel; proved).**  There are
c_ε > 0 and N₀(ε) such that, for all N ≥ N₀(ε), every modulus
2 < w ≤ (log N)^{1/2} and every nonprincipal character χ mod w,

    |∑_{q∈W} χ(q)/q| ≤ β = β(N) := exp(−c_ε (log N)^{ε/4}).

*Proof.*  For t ≥ z₀ we have w ≤ (log N)^{1/2} = (log z₀)^{1/ε} ≤
(log t)^{1/ε}, so Siegel–Walfisz applies with A = 1/ε:
θ(t,χ) := ∑_{q≤t} χ(q) log q ≪_ε t·exp(−c√(log t)) (the ψ-form of SW
minus the prime-power contribution O(√t log²t); Iwaniec–Kowalski §5.9).
Abel summation against 1/(t log t):

    ∑_{z₀<q≤z} χ(q)/q = [θ(t,χ)/(t log t)]_{z₀}^{z}
        + ∫_{z₀}^{z} θ(t,χ)·(log t + 1)/(t log t)² dt
      ≪ exp(−(c/2)√(log z₀)) = exp(−(c/2)(log N)^{ε/4}),

after substituting v = log t in the integral. ∎

**Lemma 13.9 (H1″ — tilted first moment along the shifted primes;
proved).**  Uniformly for w ≡ 3 (mod 4), 3 ≤ w ≤ (log N)^{1/2−ε},

    S₁ := ∑_{p≤N, p≡1 (24)} U(n_w(p))
        = (li N / 8h) · (1 + O((log N)^{−ε/2})).

*Proof.*  (1) *Expansion.*  2^{−ω_W(n)} = ∏_{q∈W, q|n}(1 − 1/2) =
∑_{m|n, m sqfree W-smooth} (−1/2)^{ω(m)}, so, with d running over
squarefree W-smooth d ≤ X, d ≡ −1 (mod w) and m over squarefree W-smooth
integers,

    S₁ = ∑_{d} ∑_{m} (−1/2)^{ω(m)} #{p ≤ N : p ≡ 1 (24), [d,m] | n}.

(2) *Tail m > Y, at the level of p.*  With η = 1/log z (so q^η ≤ e on W)
and τ_W(n) := 2^{ω_W(n)} ≥ T″(n),

    ∑_{p} τ_W(n) ∑_{m|n, m>Y} 2^{−ω(m)}
      ≤ Y^{−η} ∑_{n≤N} ∏_{q∈W, q|n} (2 + q^η)
      ≤ Y^{−η} · N ∏_{q∈W}(1 + 4/q)
      ≪ N (log N)^{4} exp(−(1/8)(log N)^{ε/2}) ≪ N (log N)^{−13},

using, for g(n) = ∏_{q|n, q∈W} C_q with constants C_q ≥ 1: g = 1 * u
with u multiplicative supported on squarefree W-smooth m, u(q) = C_q − 1,
so ∑_{n≤N} g(n) = ∑_m u(m)⌊N/m⌋ ≤ N ∏_{q∈W}(1 + (C_q−1)/q); here
C_q = 2 + q^η ≤ 2 + e, and log Y/log z = (1/8)(log N)^{ε/2}.

(3) *Bombieri–Vinogradov.*  For the retained pairs put v = [d,m], a
squarefree W-smooth modulus ≤ XY = N^{1/4}.  The conditions p ≡ 1 (24)
and v | (p+w)/4 ⟺ p ≡ −w (mod 4v) are compatible mod 4 exactly because
w ≡ 3 (mod 4), and CRT fuses them into a single class a_v mod 24v,
invertible: a_v ≡ 1 (24) handles ℓ ∈ {2,3}, and q | v gives
a_v ≡ −w ≢ 0 (q) since q > z₀ > w.  The number of pairs (d,m) with
[d,m] = v is ≤ 3^{ω(v)}.  Hence, with
E(v) := max_{(a,24v)=1} |π(N;24v,a) − li N/φ(24v)|,

    S₁ = li(N)·Σ† + O( ∑_{v ≤ N^{1/4}} 3^{ω(v)} E(v) ) + O(N(log N)^{−13}),
    Σ† := ∑_{d≤X} ∑_{m≤Y} (−1/2)^{ω(m)} / φ(24[d,m]),

and by Cauchy–Schwarz, Brun–Titchmarsh (E(v) ≪ N/φ(24v) for
24v ≤ N^{2/5}), and BV at level N^{1/2} with A = 36:

    ∑_v 3^{ω(v)} E(v) ≤ ( ∑_v 9^{ω(v)} N/φ(24v) )^{1/2}
                        ( ∑_{q≤N^{1/2}} max_a E )^{1/2}
      ≪ ( N (log N)^{10} )^{1/2} ( N (log N)^{−36} )^{1/2}
      = N (log N)^{−13}.

(4) *Completing the density sum (Rankin).*  φ(24v) = 8φ(v) for our v, so
8Σ† = ∑_{d≤X}∑_{m≤Y} (−1/2)^{ω(m)}/φ([d,m]); let Σ be the same sum with
both size caps removed.  Then

    |8Σ† − Σ| ≤ ∑_{d,m} [(d/X)^η + (m/Y)^η] 2^{−ω(m)}/φ([d,m])
      ≤ 2 exp(−(1/8)(log N)^{ε/2}) ∏_{q∈W}(1 + 6/(q−1))
      ≪ (log N)^{7} exp(−(1/8)(log N)^{ε/2}),

smaller than any power of 1/log N.

(5) *Factorization and characters.*  Detect d ≡ −1 (mod w) by
1 = (1/h)∑_χ χ(−1)χ(d) (χ(−1) = ±1); the completed (d,m)-sum then
factors over q ∈ W — each prime sits in d, in m, in both, or in neither:

    Σ = (1/h) ∑_{χ mod w} χ(−1) ∏_{q∈W} F_q(χ),
    F_q(χ) = 1 + [χ(q)(1 − 1/2) − 1/2]/(q−1)
           = 1 + (χ(q) − 1)/(2(q−1)).

For χ = χ₀: F_q ≡ 1 identically — the 2^{−ω} tilt cancels the divisor
growth *exactly*, and the principal term is 1/h with no secondary
expansion.  For χ ≠ χ₀, the factors are 1 + O(1/z₀), so

    log |∏_q F_q(χ)| = Re ∑_q (χ(q)−1)/(2q) + O(z₀^{−1/2})
                     = −λ/2 + O(β + z₀^{−1/2}),

by Lemma 13.8; hence |∏ F_q(χ)| ≤ 2e^{−λ/2} for N ≥ N₀(ε).  Therefore

    Σ = (1/h)·[1 + O(h e^{−λ/2})] = (1/h)·[1 + O((log N)^{−ε/2})],

since h e^{−λ/2} ≤ (log N)^{1/2−ε}·(log N)^{−(1−ε)/2}(1+o(1)) ≪
(log N)^{−ε/2}.  Combining (2)–(5), and noting the main term is
≫ N/(log N)^{3/2} while every error is ≪ N(log N)^{−13} or relatively
O((log N)^{−ε/2}), gives the lemma. ∎

**Lemma 13.10 (H2″ — tilted second moment; proved).**  Uniformly in the
same range,

    S₂ := ∑_{p≤N, p≡1 (24)} 4^{−ω_W(n)} T″(n)²
        = (li N / 8h²) · (1 + O((log N)^{−ε/2})).

*Proof.*  Same skeleton; only the combinatorics change.  Expand
4^{−ω_W(n)} = ∑_{m|n, sqfree W-smooth} (−3/4)^{ω(m)} and
T″² = ∑_{d₁,d₂}; the moduli become v = [d₁,d₂,m] ≤ X²Y = N^{3/8}, with
multiplicity ≤ 7^{ω(v)}.  The m-tail runs as in step (2) with
τ_W(n)² ≤ 4^{ω_W(n)} and weights (3/4)^{ω(m)} ≤ 1 (per-prime constant
C_q = 4 + 3q^η ≤ 4 + 3e, so C_q − 1 < 13, giving
N(log N)^{13}·exp(−(1/8)(log N)^{ε/2}));
the BV step as in (3) with 7 ↔ 3, 49 ↔ 9 (∏(1+49/(q−1)) ≪ (log N)^{50})
and A = 76; the Rankin completion as in (4) with per-prime constant
1 + 21e/(q−1)-type, still ≪ (log N)^{−C} for every C.  The completed
density sum factors with both class conditions detected by characters:

    Σ₂ = (1/h²) ∑_{χ₁,χ₂ mod w} χ₁(−1)χ₂(−1) ∏_{q∈W} F_q(χ₁,χ₂),
    F_q(χ₁,χ₂) = 1 + [(1+χ₁(q))(1+χ₂(q))/4 − 1]/(q−1),

(per prime, the eight (q|d₁?, q|d₂?, q|m?) options sum to
(1+χ₁)(1+χ₂)(1−3/4) over φ-normalization (q−1), minus the empty option
restored).  The character pairs fall into exactly the families of Lemma
13.7:

* (χ₀,χ₀): F_q ≡ 1 identically (the tilt again telescopes exactly);
  term 1/h².
* χ₁ = χ₀ ≠ χ₂ and mirror: (1+χ₀)(1+χ₂)/4 − 1 = (χ₂−1)/2, so
  F_q = 1 + (χ₂(q)−1)/(2(q−1)) — the first-moment factor;
  |∏| ≤ 2e^{−λ/2} as above.  2(h−1) terms.
* χ₂ = χ̄₁ ≠ χ₀: (1+χ)(1+χ̄)/4 − 1 = (Re χ − 1)/2, and Re ∑ χ(q)/q =
  O(β) again gives |∏| ≤ 2e^{−λ/2}.  h−1 terms.  (Total 3h e^{−λ/2},
  matching Lemma 13.7.)
* generic (χ₁, χ₂, χ₁χ₂ all nonprincipal): the bracket is
  (χ₁+χ₂+χ₁χ₂−3)/4, so uniformly

      ∏_q F_q = e^{−3λ/4}·e^{ζ},   |ζ| ≤ 3β/4 + O(z₀^{−1/2}) =: β′,

  and |e^{ζ} − 1| ≤ 2β′.  The signed coefficient sum over generic pairs
  is computed by inclusion–exclusion: ∑_{all} χ₁(−1)χ₂(−1) =
  (∑_χ χ(−1))² = 0 for w > 2; the three excluded families sum to 0, 0,
  and ∑_{χ₁} χ₁(−1)χ̄₁(−1) = h; their triple overlap (χ₀,χ₀)
  contributes 1 to each.  Hence ∑_{generic} χ₁(−1)χ₂(−1) = 2 − h (the
  model's 1 − (h−1)), and

      |∑_{generic} χ₁(−1)χ₂(−1) ∏ F_q|
        ≤ e^{−3λ/4}·[ h + 2β′h² ] ≪ h e^{−3λ/4},

  using β′h² ≤ β′ log N = o(1).  Note h e^{−3λ/4} ≤ h e^{−λ/2}.

Altogether Σ₂ = h^{−2}[1 + O(h e^{−λ/2})], and assembling as in Lemma
13.9 gives the claim. ∎

**Theorem 13.11 (single-modulus transfer complete; proved).**  Fix
ε ∈ (0, 1/2).  Uniformly for w ≡ 3 (mod 4), 3 ≤ w ≤ (log N)^{1/2−ε},

    #{p ≤ N : p ≡ 1 (mod 24), (p+w)/4 has no divisor ≡ −1 (mod w)}
      ≪_ε π(N)·(log N)^{−ε/2}.

In particular, for each such w all but O_ε(π(N)(log N)^{−ε/2}) of the
primes p ≤ N, p ≡ 1 (mod 24) satisfy the Erdős–Straus criterion at
modulus w: per-modulus failure probability O((log N)^{−ε/2}) = o(1),
uniformly through w ≤ (log N)^{1/2−ε} — the H1′/H2′ deliverable.

*Proof.*  U(n) > 0 iff T″(n) > 0, so Cauchy–Schwarz (Paley–Zygmund)
gives

    #{p ≤ N, p ≡ 1 (24) : T″ > 0} ≥ S₁²/S₂
      = (li N/8)·(1 + O((log N)^{−ε/2}))

by Lemmas 13.9–13.10, while #{p ≤ N : p ≡ 1 (24)} = li N/8 +
O(N e^{−c√log N}); subtracting gives the failure count, since
{no divisor ≡ −1 at all} ⊆ {T″ = 0}.  Sufficiency: if d | n with
d ≡ −1 (mod w), then D := n/d divides n | n², and n = dD forces
D ≡ −n (mod w), i.e. w | D + n.  Theorem 3.1(B) applies with q = w
(q ≡ −p (mod 4) holds: w ≡ 3, p ≡ 1 (4)) and x = n, divisor D of x²,
giving the explicit solution (n, p(n+D)/w, p(n + n²/D)/w). ∎

**Remarks.**

(i) *Model correspondence is exact.*  The three error families reproduce
Lemma 13.7's bound 1 + 3h e^{−λ/2} + h e^{−3λ/4} term by term, with λ
now the window mass (1−ε) log log N; the arithmetic tracks the iid model
to relative O(β) once the floor z₀ removes the L(1,χ)-biased primes.
The telescoping F_q(χ₀) ≡ 1 is the arithmetic image of E U = (1−e^{−λ/2})/h:
the θ = 1/2 tilt is exactly the weight at which divisor growth and
suppression cancel, so no Selberg–Delange machinery is needed at all —
the promised "Selberg–Delange × BV hybrid" degenerated into Mertens
products once the tilt was chosen right.

(ii) Constants are ineffective (Siegel–Walfisz), and depend on ε only.

(iii) *Supersession ledger.*  The literal H1′/H2′ (window down to q = 2,
all divisors ≤ N^{1/4}) were not proved and are not needed: nothing
downstream references the small primes, and the window statements feed
the same Paley–Zygmund inequality with the same conclusion.  The
obstruction paragraph above explains why the literal form resists
(h² Euler products of L(1,·) size vs a (log z)^{3/4} main term) — our
absolute-value method caps the unfloored window at w ≲ (log N)^{3/8}
(and the literal z = exp(√log N) window at w ≲ (log N)^{3/16}); the
floored window has no such cap up to (log N)^{1/2−ε}.

(iv) *Honest ledger of what this does and does not give.*  A single
modulus yields only E(N) ≪ N(log N)^{−1−ε/2} — far weaker than Theorem
13.2; the value is the uniformity in w, past every §13.3 ceiling at
single-modulus level.  The remaining open input for exponential savings
is H3, the w-joint version (stacking the ≍ (log N)^{1/2−ε} moduli); with
it this route yields every θ < 1/2 — **not** the θ < 1 of the
ω-conditioned H1–H3 of §13.4, whose range (log N)^{1−ε} remains open:
the 2^{−ω} tilt's admissible range h ≤ e^{(1/2−ε)λ} is structural
(Lemma 13.7 (ii)).  Two named increments could go further: (a) the
signed/n²-divisor variant — Lemma 12.5's ±1 exponent vectors tilted by
3^{−ω} — has model range h ≤ e^{(2/3−ε)λ}, i.e. w ≤ (log N)^{2/3−ε},
and the same window proof plausibly transfers it (the pair combinatorics
of Lemma 12.5 must be redone as local Euler factors); that would put the
stacked route at θ = 2/3 — Vaughan-equal, and the reappearance of 2/3
from a different direction is consistent with §13.3's divisor-density
ceiling A/(A+1).  (b) Beating 2/3 still needs conditioning beyond
fixed-order tilts.  Neither increment is claimed here.  For the later
integer-side resolution of stacking, see §14.

Numerics: `verify.py (k)` spot-checks the local-factor factorizations of
both density sums by full enumeration over a toy window (all characters
mod 7, floating point, defect < 10^{−12}); tracks the *uncapped* tilted
moments on real shifted-prime data at toy scale against Lemma 13.7's
model values (the d ≤ X cap is Rankin-inactive asymptotically but
vacuous at toy scale, so the capped T″ itself is not testable there;
loose brackets, informational); verifies the Paley–Zygmund inequality on
that data; and reconstructs exact unit-fraction solutions from sampled
window witnesses via Theorem 3.1(B) — the sufficiency chain is machine-
checked end to end.

---

## 14. Phase eight: stacking the moduli over the integers —
E(N) ≪ N exp(−(log N)^{2/5−o(1)})

§13.5 finished the single-modulus transfer; the remaining obstacle to an
exponential bound was H3, the joint version across moduli.  This section
proves an unconditional exponential bound with θ = 2/5 − o(1) — far
above Theorem 13.2's θ = 1/8, still below Vaughan's 2/3 — by resolving
the joint problem with two structural observations, both cheap in
hindsight and both invisible from inside §13:

* **Count integers, not primes.**  The exceptional primes can be counted
  inside a nonnegative integer-weighted sum ∑_{m≤N} Λ(m)² where Λ is a
  product of per-modulus sieve factors equal to 1 on every criterion
  failure.  Over the integers m, every congruence count is exact up to
  O(1), so there is no Bombieri–Vinogradov error floor.  This matters
  because any prime-side evaluation of an exponentially small main term
  is impossible: BV's saving is only a power of log, additive, while the
  target is exp(−(log N)^{θ}); see the wall-map (§14.5, W2).  Primality
  of the exceptional set is *not used at all* beyond the criterion
  itself — exactly as in Vaughan's own large-sieve argument.

* **Shift-coprimality makes cross-modulus correlations second-order.**
  All witness primes live above a floor u > W ≥ |w − w′|, so no prime
  q ≥ u can divide both (m+w)/4 and (m+w′)/4: q would divide
  (m+w) − (m+w′) = w − w′.  The windows overlap, so the same prime q
  serves several moduli — but *exclusively*: expansion terms that use q
  for two different shifts demand m ≡ −w and m ≡ −w′ (mod q)
  simultaneously and count exactly zero.  Compatible terms factor by
  CRT; the discrepancy between "exclusive" and "independent" is a
  per-shared-prime correction of size O(1/q²) whose marked sums have
  identically vanishing principal parts (the telescoping again), and
  the floor makes the total exclusion correction O(W⁴/u) = o(1).  H3 at
  integer level is a negligible-correlation estimate — not the hard
  transfer problem it is over the primes.

The per-modulus factors use the *signed* (n²-divisor) witnesses of Lemma
12.3 tilted at 3^{−ω} — the c = 3 alphabet — because the stack's
exponent is set by a budget in which signed witnesses are strictly
cheaper than subset witnesses (§14.4; the subset version of everything
below gives θ = 1/3 − o(1) by the same proof with 2^{−ω} in place of
3^{−ω}).

### 14.1 Setup and the master inequality

Fix ϑ ∈ (0, 1/10), put A = ⌈1/ϑ⌉, and let

    W  = (log N)^{2/5−ϑ},        𝒲 = {w ≡ 3 (mod 4) : C₀ < w ≤ W},
    u  = exp(W^{1/A}),           (so W = (log u)^{A}, and u > W)

with C₀ = C₀(ϑ) a constant fixed below.  For each w ∈ 𝒲 put h = φ(w)
and

    I_w = (u, v_w],   log v_w = K_w·log u,   K_w = ⌈C₁ h^{3(1+ϑ)/2}⌉,
    λ_w = ∑_{q ∈ I_w} 1/q = log K_w + O(1/log u),

so λ_w = (3/2)(1+ϑ) log h + O_{C₁}(1).  All windows share the floor u;
they may overlap freely (only shifts must differ).  Truncation:

    X_w = exp(λ_w² · log v_w).

For m ≡ 1 (mod 24) write n = n_w(m) = (m+w)/4.  A *signed pattern* for
w is a pair (a, b) of coprime squarefree I_w-smooth integers with
ab ≤ X_w and a·b⁻¹ ≡ −1 (mod w); a *tilt divisor* is a squarefree
I_w-smooth m′ ≤ X_w.  The sieve variable is the **finite** signed
divisor sum (truncated tilt — this is a definition, not an expansion of
a closed form)

    U_w(n) := ∑_{(a,b)} ∑_{m′ ≤ X_w} (−2/3)^{ω(m′)} · 1_{[ab, m′] | n}.

U_w need not lie in [0,1], but two properties hold.  (i) *Vanishing on
failures*: every term contains the factor 1_{ab | n} with
a·b⁻¹ ≡ −1 (mod w); if some term is nonzero then k = (+1 on primes of
a, −1 on primes of b) is a signed witness, so on witness-free n every
term is zero and U_w(n) = 0.  (ii) On typical n it tracks
3^{−ω_{I_w}(n)}·#witnesses: completing the m′-truncation recovers the
tilt identity 3^{−|P_w(n)|} = ∑_{m′|n, sqfree I_w-smooth}
(−2/3)^{ω(m′)}; the truncation is Rankin-negligible in every moment
computed below.

**Sufficiency.**  If n has a signed witness — disjoint subsets S₊, S₋
of its I_w-prime set with (∏ S₊)(∏ S₋)⁻¹ ≡ −1 (mod w) — put
a = ∏ S₊, b = ∏ S₋.  Then ab | n and d := na/b is a positive integer
dividing n² with d ≡ −n (mod w), i.e. w | d + n.  For m = p prime,
p ≡ 1 (mod 24), p > W: Theorem 3.1(B) applies with q = w (w ≡ 3 ≡ −p
(mod 4)), x = n, divisor d of x², so 4/p is representable.

Define, with θ_w ≥ 0 chosen in §14.2,

    Λ(m) = ∏_{w ∈ 𝒲} (1 − θ_w U_w(n_w(m))).

**Lemma 14.1 (master inequality).**  Every exceptional prime p ≤ N
(no representation of 4/p) with p > W satisfies Λ(p) = 1, and

    E(N) ≤ W + ∑_{m ≤ N, m ≡ 1 (24)} Λ(m)².

*Proof.*  An exceptional p is ≡ 1 (mod 24) (Lemma 1.2).  If n_w(p) had
a signed witness for some w ∈ 𝒲, the sufficiency paragraph would make
4/p representable — contradiction.  So every n_w(p) is witness-free,
U_w(n_w(p)) = 0 by property (i), and Λ(p) = 1.  Since Λ(m)² ≥ 0 for
every m, the sum over the class m ≡ 1 (24) dominates the count of such
p. ∎

### 14.2 The per-modulus factor

All densities below are over m ≡ 1 (mod 24): for squarefree v with
prime factors in I_w, the condition v | n_w(m) pins m to one class mod
24v (compatibility mod 4 is w ≡ 3 (mod 4); q > u > w makes the class
nontrivial mod each q | v), so its count on m ≤ N is N/(24v) + O(1) —
relative density exactly 1/v within the class, up to the rounding
accounted in Lemma 14.3.  Define the exact moment densities as the
period-averages of the *function* U_w and its square: with the finite
expansion of U_w² into pairs of terms,

    μ₁(w) = ∑_{(a,b)} ∑_{m′ ≤ X_w} (−2/3)^{ω(m′)} / [ab, m′],
    μ₂(w) = ∑_{(a₁,b₁),(a₂,b₂)} ∑_{m₁′, m₂′ ≤ X_w} (−2/3)^{ω(m₁′)+ω(m₂′)}
              / [a₁b₁, a₂b₂, m₁′, m₂′];

these are exactly the averages of U_w, U_w² over the full joint period,
so μ₂ ≥ μ₁² holds by Cauchy–Schwarz as an identity about a real
function, truncation and all.

**Lemma 14.2 (per-modulus factor).**  There are C₀(ϑ), C₁(ϑ) such that
uniformly for w ∈ 𝒲 and N large,

    μ₁(w) = (1/h)(1 + O(ρ_w)),   μ₂(w) = (1/h²)(1 + O(ρ_w)),
    ρ_w := h e^{−2λ_w/3} + 2^{ω(w)} e^{−4λ_w/9} + h²β(u),

with β(u) = exp(−c_A√(log u)) the Siegel–Walfisz saving of Lemma 13.8
for windows above u at moduli ≤ W = (log u)^{A}.  With C₀, C₁ large
enough (depending on ϑ), ρ_w ≤ h^{−ϑ}/C and hence, setting
θ_w := μ₁/μ₂ ∈ [h/2, 2h],

    δ_w := 1 − 2θ_wμ₁ + θ_w²μ₂ = 1 − μ₁²/μ₂ ∈ [0, C′h^{−ϑ}] ⊂ [0, 1/2].

*Proof.*  The machinery of Lemmas 13.9–13.10 with primes replaced by
the class m ≡ 1 (24) (exact densities 1/v — no φ, no BV, no prime
tails) and subsets replaced by the signed alphabet.  Steps, displaying
only the changed local computations:

(1) *Completion.*  μ₁, μ₂ differ from their cap-free completions — the
Euler-product-factorable sums with (a,b), m′ unrestricted — by Rankin
tails: with η = 1/log v_w (so q^η ≤ e on I_w), each removed cap costs
a factor exp(−log X_w/log v_w)·∏_{q∈I_w}(1 + O(1)/q) ≪
exp(−λ_w² + O(λ_w)), smaller than any fixed power of 1/h.  The
completed sums are evaluated in (2)–(3).

(2) *First moment.*  Detecting ab⁻¹ ≡ −1 (mod w) by characters, the
completed density factors over q ∈ I_w with local options
(q ∈ a / q ∈ b / neither) × (q ∈ m′ or not):

    μ₁-completed = (1/h) ∑_{χ} χ(−1) ∏_{q∈I_w} F_q(χ),
    F_q(χ) = 1 + [(χ(q) + χ̄(q) + 1)(1 − 2/3) − 1]/q
           = 1 + (χ(q) + χ̄(q) − 2)/(3q).

Principal χ: F_q ≡ 1 exactly — the 3^{−ω} tilt telescopes the signed
alphabet as 2^{−ω} telescoped subsets.  Nonprincipal χ:
log|∏F_q| = (2/3)·Re∑_{q∈I_w}χ(q)/q − (2/3)λ_w + O(1/u), and Lemma
13.8 (floor u, modulus ≤ (log u)^A) bounds the character sum by β(u):
|∏F_q(χ)| ≤ 2e^{−2λ_w/3}.  Hence μ₁ = (1/h)(1 + O(he^{−2λ_w/3} + hβ)).

(3) *Second moment.*  The pair expansion has local factors

    F_q(χ₁,χ₂) = 1 + [(1/9) ∑_{a,b ∈ {−1,0,1}} χ₁^{a}χ₂^{b}(q) − 1]/q,

again ≡ 1 at the principal pair.  With P(χ₁,χ₂) := #{(a,b) :
χ₁^{a}χ₂^{b} = χ₀} (∈ {1,3,5,9}), Lemma 13.8 gives uniformly

    ∏_q F_q(χ₁,χ₂) = e^{−(1−P/9)λ_w} (1 + O(β′)),   β′ := 9β + O(1/u).

Classification (finite, exhaustive; both χᵢ not both principal):
P = 3 ⇔ exactly one nontrivial relation among χ₁,χ₂ of the forms
χ₁ = χ₀, χ₂ = χ₀, χ₂ = χ₁, χ₂ = χ̄₁ (with the participating character
of order > 2 in the last two cases) — at most 4h pairs, each with
|∏| ≤ 2e^{−2λ_w/3}.  P = 5 ⇔ χ₂ ∈ {χ₁, χ̄₁}, χ₁ of order 2 — at most
2·2^{ω(w)} pairs (2-torsion of the character group), each
|∏| ≤ 2e^{−4λ_w/9}.  All remaining pairs are generic: P = 1,
∏ = e^{−8λ_w/9}(1+O(β′)); their signed coefficient sum over the
inclusion–exclusion of the excluded families is O(h) exactly as in
Lemma 13.10 (each family's coefficient sum is 0, 0, or ±h), so the
generic total is O((h + h²β′)e^{−8λ_w/9}).  Collecting:

    μ₂ = (1/h²)·[1 + O(he^{−2λ_w/3} + 2^{ω(w)}e^{−4λ_w/9}
                        + he^{−8λ_w/9} + h²β′)].

Since λ_w = (3/2)(1+ϑ)log h + log C₁ + O(1): he^{−2λ_w/3} ≤
C₁^{−2/3}h^{−ϑ}, 2^{ω(w)}e^{−4λ_w/9} ≤ h^{o(1)−2(1+ϑ)/3} ≤ h^{−ϑ}/C
(for h ≥ C₀-large; ω(w) ≪ log w/log log w), he^{−8λ_w/9} ≤ h^{−1/3},
and h²β′ ≤ W²β′ = o(1) uniformly.  All ≤ O(h^{−ϑ}) with constants
controlled by C₀, C₁.

(4) *Paley–Zygmund algebra.*  μ₂ ≥ μ₁² by Cauchy–Schwarz on the exact
densities (both are moments of the genuine random variable U_w under
the uniform measure on the class, up to identical completions), so
δ_w = 1 − μ₁²/μ₂ ∈ [0,1], and (2)–(3) give
μ₁²/μ₂ ≥ (1−Cρ_w)²/(1+Cρ_w) ≥ 1 − 3Cρ_w. ∎

### 14.3 Joint evaluation via exclusivity, and the theorem

**Lemma 14.3 (joint evaluation with exclusion corrections).**  Let
Ξ_w := (1 + 2θ_w X_w³)² ≥ the total |coefficient| mass of the expansion
of (1 − θ_wU_w)² (each of U_w, U_w² has at most X_w³, X_w⁶ terms, all
coefficients ≤ 1 in modulus).  Then, for N large,

    ∑_{m ≤ N, m ≡ 1 (24)} Λ(m)²
      ≤ (N/24)·2·∏_{w∈𝒲} C₅ h_w^{−ϑ} + O( ∏_{w∈𝒲} Ξ_w ).

*Proof.*  Expand Λ² = ∏_w(1 − θ_wU_w)² completely: a term is a tuple
τ = (π_w)_w, π_w a (possibly trivial) pattern from the expansion of
(1 − θ_wU_w)², with coefficient c(τ) = ∏c_w(π_w) and condition
v_w(π_w) | n_w(m) for each w, where v_w(π_w) is squarefree I_w-smooth.

*Exclusivity.*  If a prime q divides v_w(π_w) and v_{w′}(π_{w′}) for
w ≠ w′, the conditions force m ≡ −w and m ≡ −w′ (mod q), hence
q | w − w′ with 0 < |w − w′| < W < u ≤ q: impossible.  Such τ have
count exactly 0.  Call τ *compatible* if the v_w are pairwise coprime;
compatible τ pin m to a single class mod 24∏v_w (CRT; §14.2), so

    ∑_m Λ² = (N/24)·J + O(∏_w Ξ_w),
    J := ∑_{τ compatible} ∏_w c_w(π_w)/v_w(π_w).

*Exclusion correction.*  For a tuple τ let viol(τ) = {q : q divides
v_w(π_w) for ≥ 2 moduli}.  By inclusion–exclusion over finite sets Q of
primes of ∪I_w,

    J = ∑_Q (−1)^{|Q|} J_Q,   J_Q := ∑_{τ : Q ⊆ viol(τ)} ∏ c_w/v_w,

and J_∅ = ∏_w δ_w (the free sum factorizes across w by definition of
μ₁, μ₂, θ_w; the IE identity is ∑_{Q ⊆ V}(−1)^{|Q|} = 1_{V=∅} applied
to V = viol(τ), all sums finitely supported).  For Q ≠ ∅ use, for each
q ∈ Q, the exact signed identity (valid for every finite set U:
both sides are 1 for |U| ≥ 2 and 0 for |U| ≤ 1, by binomial sums)

    1_{|U| ≥ 2} = ∑_{S ⊆ U, |S| ≥ 2} (−1)^{|S|}(|S| − 1),

with U = users_τ(q) := {w : q | v_w(π_w)}.  Since "S ⊆ users_τ(q)" is
the *conjunction of forced divisibilities* q | v_w for w ∈ S, it
factors freely across moduli, and

    J_Q = ∑_{(S_q)_{q∈Q}, S_q ⊆ 𝒲, |S_q| ≥ 2}
            ∏_{q∈Q} (−1)^{|S_q|}(|S_q| − 1) · ∏_w Δ_w(marks),

where marks(w) = {q ∈ Q : w ∈ S_q} and Δ_w(M) is the w-sum restricted
to patterns whose v-part is divisible by every q ∈ M (Δ_w(∅) = δ_w;
Δ_w(M) = 0 if some q ∈ M lies outside I_w, the empty sum).  Untouched
moduli keep their *signed* δ_w.

*Marked-sum bound (safe form).*  For a nonempty finite M ⊂ I_w of
distinct primes,

    |Δ_w(M)| ≤ C₂^{|M|} · h^{2/3} · ∏_{q∈M} (1/q).

Indeed Δ_w(M) = −2θ_wμ₁^{(M)} + θ_w²μ₂^{(M)} with μ_i^{(M)} the moment
sums with the divisibility marks.  After Rankin completion (marked
tails keep a factor ∏(C/q), since a forced q retains its 1/q, and
contribute ≤ C^{|M|}h²e^{−λ²+O(λ)}∏ 1/q — below every bound claimed),
the completed marked sums factor with the local factor at each q ∈ M
replaced by (F_q − 1).  The principal (resp. principal-pair) term
vanishes identically since F_q(χ₀) = 1 = F_q(χ₀,χ₀).  For every other
character (pair), write the punctured product through the full window:

    ∏_{q∈M}(F_q−1) · ∏_{q∉M}F_q = ( ∏_{q∈I_w}F_q ) · ∏_{q∈M} (F_q−1)/F_q,

with |F_q| ≥ 1/2 for q > u and |(F_q−1)/F_q| ≤ C/q, so the full-window
size bounds of Lemma 14.2 (|∏_{I_w}F| ≤ 2e^{−(1−P/9)λ}, uniform via
Lemma 13.8; the 1+O(β′) corrections absorbed since β′ = o(1)) apply
verbatim, at the cost ∏_{q∈M}(C/q).  Every term is then bounded by
*size only* — no cancellation over the generic family is claimed for
marked sums (it is false: marks correlate with the coefficients; e.g.
q ≡ −1 (mod w) gives a marked generic coefficient sum ≍ h²/q) — with
the family counts of Lemma 14.2(3):

    |θ_w μ₁^{(M)}|  ≤ C^{|M|} h e^{−2λ/3} ∏ 1/q  ≤ C^{|M|} h^{−ϑ} ∏ 1/q,
    |θ_w²μ₂^{(M)}| ≤ C^{|M|} [h e^{−2λ/3} + 2^{ω(w)}e^{−4λ/9}
                     + h² e^{−8λ/9}] ∏ 1/q ≤ C^{|M|} h^{2/3} ∏ 1/q,

the last step from h²e^{−8λ/9} = h^{2−(4/3)(1+ϑ)} ≤ h^{2/3}.

*Assembly.*  Normalize by δ̄_w := C₅h_w^{−ϑ} ≥ max(δ_w, |Δ-scale|·…):
the ratio per touched modulus is |Δ_w(M)|/δ̄_w ≤
h^{2/3+ϑ}∏_{q∈M}(C₆/q) ≤ W·∏_{q∈M}(C₆/q).  Charging the factor W to
each (q, w)-incidence separately (safe, W ≥ 1) gives, per q, the cost
∑_{j≥2} \binom{W}{j}(j−1)(WC₆/q)^{j} ≤ 3(W²C₆/q)² for q > u ≫ W⁴.
Hence

    ∑_{Q≠∅} |J_Q| ≤ (∏_w δ̄_w)·[ ∏_{q>u} (1 + 3C₆²W⁴/q²) − 1 ]
              ≤ (∏_w δ̄_w)·[ exp( 6C₆²W⁴/u ) − 1 ]
              ≤ (∏_w δ̄_w)·C W⁴/u = (∏_w δ̄_w)·o(1),

since ∑_{q>u} q^{−2} ≤ 2/u for large u and u = exp(W^{1/A}) exceeds
every fixed power of W.  With D := ∏_wδ̄_w and |J_∅| = ∏|δ_w| ≤ D:
J ≤ J_∅ + D·o(1) ≤ D·(1 + o(1)) ≤ 2∏(C₅h_w^{−ϑ}) by Lemma 14.2, for N
large. ∎

**Theorem 14.4 (exponential bound, θ = 2/5 − o(1); proved).**  For each
fixed ϑ ∈ (0, 1/10) there is c(ϑ) > 0 such that for all large N

    E(N) ≤ N·exp(−c(ϑ)·(log N)^{2/5−ϑ}·log log N),

so in particular E(N) ≪ N exp(−(log N)^{2/5−o(1)}).  Constants
ineffective (Siegel–Walfisz).

*Proof.*  Budget for the rounding product:
log Ξ_w ≪ log h + log X_w ≪ λ_w²·K_w·log u ≪
(loglog N)²·W^{3(1+ϑ)/2}·W^{1/A}, so, summing over the ≤ W moduli,

    ∑_{w∈𝒲} log Ξ_w ≪ W^{1 + 3(1+ϑ)/2 + ϑ}·(loglog N)²
      ≤ (log N)^{(2/5−ϑ)(5/2 + 5ϑ/2)}(loglog N)² ≤ (log N)^{1−ϑ/4},

since (2/5 − ϑ)(5/2 + 5ϑ/2) = 1 − (3/2)ϑ − (5/2)ϑ² < 1 − ϑ.  So the
rounding total is exp((log N)^{1−ϑ/4}) = N^{o(1)}.  Main term, via
Lemma 14.3's product bound:

    2∏_{w∈𝒲} C₅ h_w^{−ϑ} ≤ exp(−ϑ∑_{w∈𝒲} log h_w + O(W))
      ≤ exp(−(ϑ/5)·W log W)
      = exp(−c(ϑ)·(log N)^{2/5−ϑ}·log log N)

for large N, using ∑_{w≤W, w≡3(4)} log φ(w) = (W/4)(log W)(1+o(1))
(the progression w ≡ 3 (mod 4) has density 1/4 in the integers).
Lemma 14.1 and Lemma 14.3 assemble:
E(N) ≤ W + (N/24)·exp(−c(log N)^{2/5−ϑ}loglog N) + N^{o(1)}. ∎

The subset (c = 2) version — U = 2^{−ω}T″ exactly as in §13.5, with
F_q(χ) = 1 + (χ(q)−1)/(2q) and λ_w ≥ (2+ϑ)log h, K_w ≈ h^{2+ϑ} —
yields θ = 1/3 − o(1) by the same assembly.  The signed alphabet is
strictly better here; this is the first place in the campaign where the
c = 3 structure pays concretely.

### 14.4 The budget ceiling of witness stacking (corrected assessment)

This is a calibration of *this* framework — independent-uniform residue
mixing in prime windows above a floor, support-restricted local weights, and
the finite integer-side rounding assembly — not a nonexistence theorem for
other methods.  The phase-eight second-moment factors required
λ_w ≥ (1−1/c)⁻¹log h and therefore gave θ ≤ 1/3 for c = 2 and θ ≤ 2/5
for c = 3.  Restricted weights remove that second-moment cost, so it is not
the final ceiling.

The correct remaining threshold is entropy.  If K is the Poisson number of
selected window primes and signed exponents lie in {−1,0,1}, there are at
most 3^K candidate products.  Write λ = ρ log h.  If ρ < 1/log 3, choose
ρ < b < 1/log 3.  Poisson concentration gives K ≤ b log h with probability
1−h^{−c}, while a union bound gives conditional witness probability at most
3^K/h ≤ h^{b log 3−1}.  Thus polynomial contraction in this model requires
ρ ≥ ρ₀ := 1/log 3; Lemma 14.6 and Theorem 14.9 work for every fixed
ρ > ρ₀.

A window of mass ρ log h above u has log v/log u = h^{ρ+o(1)}.  The finite
weights therefore spend h^{ρ+o(1)} (up to logarithms and the common floor
factor) at modulus w.  Stacking w ≤ W spends
∑_{w≤W}h_w^{ρ+o(1)} = W^{1+ρ+o(1)}, against budget log N.  Letting
ρ ↓ ρ₀ gives the structural supremum

    θ_* = 1/(1+ρ₀) = log 3/(1+log 3) = 0.5234946419… .

The endpoint is not claimed.  **Assessment:** under the named model and
rounding architecture, witness stacking reaches every θ < θ_* and cannot
cross θ_*; this remains below Vaughan's 2/3.  The earlier claim that every
modulus must consume at least h, and hence that 1/2 is the ceiling, was
false: signed entropy only forces h^{1/log 3+o(1)} at the threshold.

### 14.5 The wall-map: what beating 2/3 now requires

Assessments, not theorems; each is a proof-level obstruction to the
named technology with its load-bearing computation cited.

* **(W1) Witness stacking caps at θ_* = log 3/(1+log 3)** (§14.4,
  under the named model and rounding assumptions): the signed alphabet has
  3^K products, so polynomial witness probability starts at
  K ≈ (log h_w)/log 3.  A window at that entropy threshold consumes
  h_w^{1/log 3+o(1)} level; summing over w ≤ W gives
  W^{1+1/log 3+o(1)} ≤ log N.  §14.6 reaches every fixed θ < θ_*;
  the endpoint is a framework supremum, not an attained estimate.

* **(W2) No prime-side stacking by progression evaluations.**  An
  evaluation-based joint argument over primes needs progression counts
  to compound moduli with relative errors below an exponentially small
  main term; Bombieri–Vinogradov saves only fixed powers of log N,
  additively.  Within evaluation-based technology the integer-side Λ²
  device of §14.1 (inequalities with O(1) rounding instead of
  evaluations) is the exit, and primality contributes nothing.
  Vaughan's own argument also counts integers.  (Scope: this indicts
  BV-style evaluations, not every conceivable prime-side inequality.)

* **(W3) The class-mass ceiling B = 2, and the one visible door.**
  Vaughan/PW feed the large sieve ∑_{ℓ≤X} f(ℓ)/ℓ ≍ (log X)² forced
  classes (PW Lemma 4.1; f(ℓ) is τ₃-like on ℓ ≡ −1 (mod m)) and
  optimize exp(−log N/(2 log X) + c·log²X) at log X ≍ (log N)^{1/3}:
  θ = 2/3 = B/(B+1), B = 2.  Beating 2/3 in this currency means B > 2:
  more *distinct* forced classes mod a single prime ℓ.  The
  Elsholtz–Tao/PW counts say total solution mass per prime is
  (log p)³-sized (B = 3) but clusters ≍ log p solutions per class,
  realizing only (log ℓ)² distinct classes.  **The one visible door to
  θ > 2/3 is declustering: a construction giving (log ℓ)^{2+δ} distinct
  forced classes per prime ℓ.**  §5's obstruction theorem rules out
  polynomial families as the source; §13.3(3) rules out one-modulus
  divisor identities; nothing rules the door shut in general.

* **(W4) Hybrids do not add exponents** (in the combinations computed
  here).  Feeding Λ-weighted sequences into the large sieve pays
  Cauchy–Schwarz halving: #E ≤ [(N+Q²)·∑Λ⁴/S]^{1/2} carries exponent
  (Vaughan + stack)/2 < Vaughan.  Splitting the level budget between
  the two systems is likewise lossy (the LS mass is superlinear in its
  budget share).  Max, not sum: 2/3 stands against these combinations.

Status after phase eight (historical ledger): campaign record E(N) ≪
N exp(−(log N)^{2/5−o(1)}) (Theorem 14.4), Vaughan unbeaten by the
stacking technology; the two
open frontiers were (i) restricted weights toward the then-miscalculated
1/2 ceiling and (ii) the declustering door of W3 toward θ > 2/3.
Section 14.6 resolves (i) at the corrected entropy supremum θ_*; frontier
(ii) remains open.

Numerics: `verify.py (l)` checks the signed local-factor identities
(first and second moments, all character pairs mod 7, toy window), runs
a toy integer-side stack ∑Λ² against ∏δ_w on real data
(informational), confirms Λ = 1 on witness-free integers, and
reconstructs exact unit-fraction solutions from signed witnesses via
d = na/b and Theorem 3.1(B).

### 14.6 Restricted weights: exact Boolean minimum, a subset obstruction,
and the signed entropy-threshold stack

This section resolves the named support-restricted minimization, but not
in the form originally guessed.  The support issue disappears completely
under Möbius inversion on the Boolean lattice: without a size cap, the
restricted quadratic minimum is exactly the probability that the random
prime pattern is witness-free.  That identity exposes a decisive
alphabet-size distinction.  Subset witnesses do **not** have polynomially
small miss probability at λ = (1+ε)log h for every ε > 0.  Signed
witnesses already do once λ = ρ log h with ρ > 1/log 3.  The latter
suffice for the Erdős–Straus stack and improve Theorem 14.4 to every
exponent below log 3/(1+log 3).

Fix a finite prime set I, with independent Bernoulli variables X_q of
means p_q = 1/q, and identify a pattern P with {q : X_q = 1}.  Let 𝒜 be
an upward-closed family of witnessed patterns: in the subset case,
P ∈ 𝒜 iff some V ⊆ P has ∏_{q∈V}q ≡ −1 (mod w); in the signed case,
P ∈ 𝒜 iff some disjoint A,B ⊆ P have
(∏_{q∈A}q)(∏_{q∈B}q)⁻¹ ≡ −1 (mod w).  Put f(P) = 1_{P∉𝒜}.

**Lemma 14.5 (exact restricted minimum; proved).**  Let
S = 𝒜 \ {∅}.  Among real coefficients ξ_V supported on {∅} ∪ S with
ξ_∅ = 1, put

    L(P) = ∑_{V⊆P} ξ_V,       Q(ξ) = E L(P)².

Then

    min Q(ξ) = P(P∉𝒜).

The unique minimizer in function space is L = f, and its coefficients
are

    ξ_V = ∑_{T⊆V} (−1)^{|V\T|} f(T).                         (14.14)

In particular ξ_V = 0 for every nonempty witness-free V, so (14.14)
has exactly the required, non-divisor-closed support.

*Proof.*  If P is witness-free, every V ⊆ P is witness-free.  Every
admissible nonempty coefficient therefore vanishes from L(P), and
L(P) = ξ_∅ = 1.  Thus Q ≥ P(P∉𝒜).  Conversely prescribe L(P) = f(P)
for every P and invert the Boolean zeta transform; this gives (14.14).
If V is nonempty and witness-free, all T ⊆ V have f(T) = 1, so
ξ_V = (1−1)^{|V|} = 0.  Hence the coefficients are admissible and
Q = Ef² = Ef, attaining the lower bound. ∎

The identity means that no quadratic optimization can beat the actual
miss probability.  It also identifies the error in the earlier
"witness mass e^λ/h" argument for subsets.

**Lemma 14.6 (Poisson alphabet dichotomy; proved).**  Let G be a finite
abelian group of order h, let τ ≠ 1 have order 2, let K be Poisson with
mean λ, and conditional on K let g₁,…,g_K be iid uniform on G.

1. If 0 < ε < 1/log 2 − 1 and λ = (1+ε)log h + O(1), then the probability
   that no subset product equals τ is 1 − O_ε(h^{−c_ε}) for some
   c_ε > 0.
2. Suppose additionally that |G[2]| = h^{o(1)} (as for the unit groups
   used below).  For every fixed ρ > 1/log 3, if λ ≥ ρ log h, then the
   probability that no signed product ∏g_i^{e_i},
   e_i ∈ {−1,0,1}, equals τ is O_ρ(h^{−c_ρ}).

Both conclusions persist, with possibly smaller positive exponents, for
the actual prime pattern in a window I = (u,v] when all q > u > w,
∑_{q∈I}1/q = λ, and

    max_{χ≠χ₀} |∑_{q∈I} χ(q)/q| ≤ β,

provided hβ + 1/u is smaller than every fixed power under consideration.

*Proof.*  For (1), conditional on K = k, each nonempty fixed subset
product is uniform on G, so the union bound gives success probability at
most (2^k−1)/h.  Choose b with 1+ε < b < 1/log 2.  On K ≤ b log h this
is at most h^{b log 2−1}; the Poisson upper-tail Chernoff bound gives
P(K > b log h) ≤ h^{−c} because b exceeds the mean coefficient
1+ε.  This proves (1).  In particular the large value
E2^K = e^λ comes from the upper tail of K and says nothing useful about
typical covering.

For (2), condition on K = k and use Lemma 12.5.  With
T = #{e ∈ {−1,0,1}^k : ∏g_i^{e_i} = τ} and t = |G[2]|, put
A = 3^k−1.  The denominator in (12.13) is
D = 9^k+2hA+t5^k, so

    P(T=0 | K=k) ≤ 1−A²/D ≤ (D−A²)/A²
      = (2·3^k−1+2hA+t5^k)/A²
      ≪ (h+1)3^{−k} + t(5/9)^k,                            (14.15)

where A² ≥ (4/9)9^k for k ≥ 1.  Thus the first error is the
expected-pool/entropy term, including the proportional-pair contribution,
and the second is the remaining rank-two second-moment term; neither is
discarded.

Choose 1/log 3 < a < ρ.  Poisson Chernoff gives
P(K < a log h) ≤ h^{−c₀(ρ,a)} (the exponent at the smallest allowed mean
is ρ−a+a log(a/ρ)>0).  Conditional on K ≥ a log h, (14.15) gives honestly

    P(T=0 | K ≥ a log h)
      ≪ h^{1−a log 3} + h^{−a log(9/5)+o(1)}.               (14.16)

Both displayed exponents save a fixed positive power: a log 3−1 > 0,
and t = h^{o(1)} makes a log(9/5)−o(1)>0.  Adding the lower-tail bound
and shrinking the exponent proves (2).  Only the stated small-2-torsion
groups are covered; no signed claim is made here for, e.g., elementary
2-groups.

It remains to transfer the iid model to the window, and this costs no
moment calculation.  Couple each Bernoulli(1/q) variable to an
independent Poisson(1/q) variable.  If Z is Poisson(p), first couple
1_{Z≥1} to Bernoulli(p), at mismatch cost p−(1−e^{−p}) ≤ p²/2, and then
pay P(Z≥2) ≤ p²/2; the product coupling therefore fails with probability
at most ∑q^{−2} ≤ 2/u.  Conditional on the total Poisson count, its prime
labels are iid with probabilities (1/q)/λ.  The induced residue law ν
satisfies, by character orthogonality,

    ||ν − uniform_G||_TV
       ≤ (h−1)β/(2λ) ≤ hβ/(2λ).

Coupling all Poisson labels costs at most E(K)||ν−uniform||_TV ≤ hβ/2.
Thus every event probability differs from the iid uniform-Poisson model
by O(hβ + 1/u), proving the transfer. ∎

Part (1) is a genuine counterexample to the proposed **subset** lemma at
mass (1+ε)log h for small ε.  It is not a defect of Selberg
minimization: Lemma 14.5 says the optimization is already exact.  Part
(2) is the route needed by the signed Erdős–Straus stack.

We now impose the finite level required for integer-side rounding.  A
pattern V also denotes the squarefree integer ∏_{q∈V}q.

**Lemma 14.7 (finite signed weights and marked stability; proved).**
Fix ρ_+, ρ_- with ρ_+ ≥ ρ_- > 1/log 3.  Suppose I = (u,v] is a prime
window for w ≡ 3 (mod 4), h = φ(w), with

    ρ_- log h ≤ λ := ∑_{q∈I}1/q ≤ ρ_+ log h,

and the character-sum hypothesis of Lemma 14.6 with negligible hβ+1/u.
There are constants B(ρ_-,ρ_+), κ(ρ_-,ρ_+)>0 and admissible
signed-witness weights
ξ_V, supported on

    V ∈ 𝒜,       |V| ≤ L := ⌈Bλ⌉,       V ≤ R := v^L,

with ξ_∅ = 1, such that

    Q_w := E(∑_{V⊆P}ξ_V)² ≤ C_{ρ_-,ρ_+} h^{−κ}.             (14.17)

Moreover, if the multilinear expansion is

    (∑_V ξ_V x_V)² = ∑_A c_A x_A       (x_q² reduced to x_q),

then for every nonempty set M of distinct primes of I,

    |Δ_w(M)| := |∑_{A⊇M} c_A ∏_{q∈A}q^{−1}|
       ≤ 18^{|M|} h^{8ρ_+} ∏_{q∈M}q^{−1}.                  (14.18)

Finally ∑_V|ξ_V| ≤ 1+R², so the total absolute coefficient mass of the
square is at most Ξ_w := (1+R²)².

*Proof.*  Take the exact Möbius coefficients (14.14) for |V| ≤ L and
zero outside that range.  They are admissible by Lemma 14.5 and
|ξ_V| ≤ 2^{|V|}.  If K = |P| ≤ L, their zeta transform is exactly f(P).
For every P, truncated or not,

    |∑_{V⊆P}ξ_V| ≤ ∑_{V⊆P}2^{|V|} = 3^K.

Consequently Lemma 14.6(2), applied with ρ_-, gives

    Q_w ≤ P(P witness-free) + E(9^K 1_{K>L}).               (14.19)

For t > 1, independence gives

    E(9^K 1_{K>L}) ≤ t^{−L}∏_{q∈I}(1+(9t−1)/q)
       ≤ exp((9t−1)λ − L log t).

Put t = B/9 and choose B large enough that
B log(B/9)−B+1 is larger than the desired fixed constant.  The last
display is then h^{-c}; together with Lemma 14.6 it proves (14.17),
after decreasing κ.

For the marks, let F be the multilinear reduction of the square and
D_MF its iterated Boolean difference in the variables of M.  If the
remaining random pattern is Y, coefficient comparison gives the exact
identity

    Δ_w(M) = (∏_{q∈M}q^{−1}) E D_MF(Y).                     (14.20)

The difference is an alternating sum of 2^{|M|} Boolean values.  At each
such value the full pattern has size at most |Y|+|M|, so the preceding
3^K bound yields

    |D_MF(Y)| ≤ 2^{|M|}9^{|Y|+|M|} = 18^{|M|}9^{|Y|}.

Since E9^{|Y|} ≤ ∏_{q∈I}(1+8/q) ≤ e^{8λ} ≤ h^{8ρ_+},
(14.18) follows.  Finally
|ξ_V| ≤ 2^{ω(V)} ≤ V and all supported integers satisfy V ≤ R, whence
∑|ξ_V| ≤ 1+∑_{n≤R}n ≤ 1+R². ∎

This marked estimate is deliberately crude.  Unlike §14.3's local-factor
bound it uses no character cancellation, but its h-power is fixed; the
floor u will beat every such power.  Notice also that (14.20), not
E(F1_{M⊆P}), is the marked sum needed by exclusion: the mark says that
the monomial's union contains M.  This distinction prevents an invalid
positivity shortcut.

**Theorem 14.8 (the earlier 1/2 statement; proved).**  For every fixed
σ ∈ (0,1/4) there is c(σ)>0 such that, for all large N,

    E(N) ≤ N exp(−c(σ)(log N)^{1/2−σ} log log N).

This remains valid, but is superseded by Theorem 14.9 and is no longer the
campaign frontier.  It follows immediately from that theorem (with a
smaller exponent parameter if necessary).  The constants are ineffective
because of Siegel–Walfisz.

**Theorem 14.9 (restricted signed stack at the entropy exponent; proved).**
Put

    θ_* := log 3/(1+log 3) = 0.5234946419… .

For every fixed σ > 0 there is c(σ)>0 such that, for all large N,

    E(N) ≤ N exp(−c(σ)(log N)^{θ_*−σ} log log N).

Hence E(N) ≪ N exp(−(log N)^{θ_*−o(1)}).  The constants are ineffective
because of Siegel–Walfisz.  Vaughan's exponent 2/3 remains stronger than
this section's; §16 later mounts the (claimed/provisional) improvement by
the orthogonal multiplier-class route.

*Proof.*  It suffices to prove the assertion for 0 < σ < θ_*; every larger
σ follows from any one stronger case.  Put θ = θ_*−σ and
ρ₀ = 1/log 3.  Since θ < 1/(1+ρ₀), choose fixed ρ > ρ₀ and an integer
A so large that

    θ(1+ρ+1/A) < 1.                                         (14.21)

Set

    W = (log N)^θ,             𝒲 = {w ≡ 3 (mod 4): C₀ < w ≤ W},
    u = exp(W^{1/A}).

For w ∈ 𝒲, h = φ(w), choose

    K_w = ⌈C_ρ h^ρ⌉,           v_w = u^{K_w},
    I_w = (u,v_w],             L_w = ⌈Bλ_w⌉,
    λ_w = ∑_{q∈I_w}1/q,        R_w = v_w^{L_w}.

Choose fixed ρ_-,ρ_+ with ρ₀ < ρ_- < ρ < ρ_+.  Mertens gives
λ_w = log K_w+O(1/log u) = ρ log h+O_ρ(1); after increasing C₀ and
adjusting C_ρ,

    ρ_- log h ≤ λ_w ≤ ρ_+ log h.

Siegel–Walfisz in the form of Lemma 13.8, now with
w ≤ W = (log u)^A, gives β(u) = exp(−c_A√log u).  Thus Lemma 14.7
applies uniformly, and (enlarging C₀ once more) supplies local factors
L_w(n) = ∑_Vξ_{w,V}1_{V|n} with

    Q_w = E L_w² ≤ C h^{−κ} =: δ̄_w ≤ 1/2.                 (14.22)

Every nonconstant supported V contains a signed witness.  Therefore
L_w(n) = 1 whenever n is signed-witness-free.  With

    ℒ(m) = ∏_{w∈𝒲} L_w((m+w)/4),

§14.1's sufficiency argument and master inequality apply verbatim:

    E(N) ≤ W + ∑_{m≤N, m≡1 (24)} ℒ(m)².                    (14.23)

We give the joint estimate because its marked input differs from Lemma
14.3's.  Expand ℒ².  A local monomial has squarefree modulus A ⊆ I_w,
coefficient c_{w,A}, free density ∏_{q∈A}1/q, and total absolute
coefficient mass at most Ξ_w = (1+R_w²)².  As in Lemma 14.3, a prime
q > u > W cannot occur in monomials belonging to two distinct shifts:
the congruences would force q | w−w′.  Compatible tuples count by CRT,
with an O(1) rounding error per tuple.  Hence

    ∑_{m≤N,m≡1(24)}ℒ(m)² = (N/24)J + O(∏_w Ξ_w),            (14.24)

where J is the free product sum with all shared-prime tuples deleted.
Inclusion–exclusion over shared primes, using the exact user-set identity
from Lemma 14.3, expresses each correction as products of local marked
sums Δ_w(M), while untouched moduli contribute Q_w.

Let D > 8ρ_++κ be a fixed integer.  By (14.18), after normalizing by
δ̄_w, each touched modulus costs at most

    C^{|M|} W^D ∏_{q∈M}1/q.

Charge W^D once to every (q,w)-incidence.  For a fixed q the sum over
user sets of size j ≥ 2 is, since q > u exceeds every power of W,

    ∑_{j≥2} binom(|𝒲|,j)(j−1)(CW^D/q)^j
       ≪ W^{2D+2}/q².

Therefore the sum of the absolute exclusion corrections, divided by
∏δ̄_w, is

    ≪ exp(CW^{2D+2}∑_{q>u}q^{−2}) − 1
     ≪ W^{2D+2}/u = o(1).

The free term is ∏Q_w ≤ ∏δ̄_w, so (14.24) yields

    ∑_{m≤N,m≡1(24)}ℒ(m)²
      ≤ (N/24)·2∏_{w∈𝒲} C h_w^{−κ} + O(∏_wΞ_w).             (14.25)

It remains to check the rounding level.  Lemma 14.7 and the window
choices give

    ∑_{w∈𝒲}log Ξ_w ≪ ∑_w log R_w
      ≪ ∑_{w≤W} λ_w K_w log u
      ≪ W^{1+ρ+1/A} log W.

By (14.21), this is o(log N), so ∏Ξ_w = exp(o(log N)) = N^{o(1)}.
Finally

    ∏_{w∈𝒲} C h_w^{−κ}
       ≤ exp(−c_σ W log W),

using the same asymptotic
∑_{w≤W,w≡3(4)}log φ(w) = (W/4)log W(1+o(1)) as Theorem 14.4.  Substitute
this and the rounding bound into (14.23)–(14.25), and use
W = (log N)^{θ_*−σ}; both W and N^{o(1)} are smaller than the asserted
right side for large N. ∎

**Honest ledger.**  The unrestricted support identity, the subset
counterexample, the finite signed weights, their marked stability, and
every θ < θ_* stack are proved above.  No endpoint estimate at θ_* is
claimed.  The framework assessment caps this architecture at the signed
entropy threshold θ_*, not at 1/2.  Vaughan's θ = 2/3 remains stronger
than every stacking result; see §16 for the (claimed/provisional)
improvement along the class-mass axis instead.
The earlier proposed subset route at λ = (1+ε)log h is false for
ε < 1/log 2 − 1; only the signed alphabet closes the upgrade.

Numerics: `verify.py (m1)` computes the exact Möbius coefficients and
restricted minimum for **subset witnesses only**, for
w ∈ {7,11,19,23,31} and the first r ∈ {8,12,16} primes above w, using
integer probability numerators.  In every case the coefficients vanish
on nonempty subset-witness-free patterns and Q_min = P(miss) exactly.
`verify.py (m2)` separately implements signed reachability, including the
S·a^{-1} transition, and prints finite iid-Poisson miss tables centered at
1/log 3 for signed witnesses and 1/log 2 for subsets.  These are toy checks
only; their small groups do not establish an asymptotic transition, and no
numerical observation is used in the proof.

Status after phase nine: campaign record
E(N) ≪ N exp(−(log N)^{θ_*−o(1)}) (Theorem 14.9), unconditional and
Siegel–Walfisz-ineffective.  The restricted-weight frontier is closed at
the corrected entropy supremum; the declustering door of W3 is the
remaining named route beyond Vaughan's 2/3.  For the later multiplier-class
route beyond Vaughan, see §16.

## 15. The declustering door: a fixed-multiple scan shows no enlargement

This section separates two notions that initially looked identical but are not:
a criterion witness whose parameter is the auxiliary prime ℓ, and a residue
class *constructed using* ℓ.  The experiment below measures the first notion.
The explicit reconstruction matching the Vaughan/PW count uses the second and
has a criterion parameter that varies with n.  This distinction means the
finite experiment is not automatically an upper bound for all ℓ-local
identities.

### 15.1 Fixed-parameter envelope (exhaustive finite experiment)

Let ℓ ≡ 3 (mod 4) be prime.  On the only hard slice n ≡ 1 (mod 4), define a
fixed-multiple hit at n to mean an exact Theorem 3.1-form reconstruction with
q = kℓ in case B or m = kℓ in case A, for some k ≤ 20.  Compatibility forces
k ≡ 1 (mod 4), so only k = 1, 5, 9, 13, 17 can occur.  (In particular, q = ℓ
in case B is compatible with n ≡ 1, not n ≡ 3.)  Residue 0 mod ℓ is omitted:
it is irrelevant to the large sieve on target primes and is trivially
composite.

`phase0_full.py` exhausts every nonzero residue r mod ℓ in the stated ladder.
For each it tests 40 deterministic-pseudorandom n ≡ r (mod ℓ), n ≡ 1 (mod 4),
with 10^6 ≤ n ≤ 10^8.  Divisors of x² or z₀² are enumerated from exact integer
factorizations.  Because sampled n may be composite, a hit now requires both
kℓ | d+x and kℓ | x+x²/d (and the analogous two conditions with z₀).  The
original scan checked only the first divisibility; that relaxed bug was
conservative—it could add false hits but could not remove a genuine one—and
the corrected full rerun left the table unchanged.  A candidate survives only
if every tested n has a hit; for the union over k and both halves, k may vary
with n.  Thus survivors are only finite-test upper candidates, while one
failed test is an exact counterexample to that residue being universally
fixed-multiple-forced.

| ℓ | PW f(ℓ) | q=ℓ, B | m=ℓ, A | either half, some k≤20 |
|---:|---:|---:|---:|---:|
| 103 | 4 | 1 | 0 | 1 |
| 199 | 7 | 1 | 0 | 1 |
| 431 | 17 | 1 | 0 | 1 |
| 863 | 24 | 1 | 0 | 1 |
| 1699 | 7 | 1 | 0 | 1 |
| 3467 | 7 | 1 | 0 | 1 |
| 6899 | 22 | 1 | 0 | 1 |
| 13799 | 67 | 1 | 0 | 1 |

The survivor is always r = −4 (mod ℓ), and it is genuinely forced on this
hard slice: if x = (n+ℓ)/4, then x ≡ −1 (mod ℓ), so d = x² divides x² and
both ℓ | d+x and ℓ | x+x²/d = x+1.  The reconstructed identity is exact.
No A-half candidate survived these tests, and no tested k-shift added a
candidate.  The descriptive regression
log A = α + β log log ℓ therefore gives β = 0.00 with degenerate standard
error 0.00 (all eight observations equal 1); this is measured finite data, not
an asymptotic theorem.  For scale only, the same eight highly divisor-sensitive
values of f give β = 2.47 ± 1.10 (ordinary least-squares standard error), too
noisy to estimate the known average exponent 2.

The passing witness also explains why the fixed-parameter search is so narrow:
d = x² is a universal endpoint of the divisor lattice.  By contrast, the
explicit witnesses in the next lemma have d = s²w and a criterion modulus
that changes with n, so those particular witnesses do not appear in the
q = kℓ scan.  This says nothing about alternative fixed-q witnesses for the
same classes: r = −4, for example, has both the lemma's D = 1 witness and the
fixed q = ℓ, d = x² witness on the hard slice.  Fixed-q scans are therefore
not guaranteed to be an upper envelope for all ℓ-local families.

### 15.2 Independent reconstruction matching the Vaughan/PW count

Pomerance–Weingartner (PW) state the count f(ℓ) in (4.1), but do not print the
underlying unit-fraction identity, and Vaughan's paper remained inaccessible.
Lemma 15.1 is therefore an independent reconstruction whose count matches the
Vaughan/PW count, not a verification of Vaughan's own parametrization.

**Lemma 15.1 (independently reconstructed class family).**  Let ℓ ≡ 3 (mod 4)
be prime and put a = (ℓ+1)/4.  Choose a squarefree T | a and a factorization

    d₁d₂ = a/T,                    d₁ < d₂.

Put g = gcd(d₁,d₂), u = d₁/g, v = d₂/g, w = Tg², and

    D = Td₁² = u²w,              r = ℓ−4D.

Then uvw = a, 1 ≤ r < ℓ, and

    r ≡ −4Td₁² ≡ −u v⁻¹                         (mod ℓ).

For every n = r+jℓ with j ≥ 0, set

    s = v−u+jv = (nv+u)/ℓ,       q = j+1 = (s+u)/v,
    x = suw,                     d = s²w.

These are positive integers, q = 4x−n and d | x², and they give the exact
identity

    4/n = 1/(suw) + 1/(nsvw) + 1/(nuvw).

No side condition modulo 4 is needed: the formula covers every positive n in
the class, including even and composite n.  The classes so obtained are
distinct, and their number is exactly

    f(ℓ) = floor( (1/2) ∑_{T|a} μ²(T) τ(a/T) ).

*Proof.*  Since D/a = d₁/d₂ = u/v and 4a ≡ 1 (mod ℓ), the two
descriptions of the class agree.  Also D<a because d₁<d₂, so r = ℓ−4D lies
between 1 and ℓ−1.  For n=r+jℓ,

    rv+u = (ℓ−4u²w)v+u = ℓ(v−u),

which gives s=v−u+jv and then q=(s+u)/v=j+1.  In particular both are
positive.  Moreover

    4suvw = s+nv+u,
    4x = n+(s+u)/v = n+q,
    x²/d = u²w,
    d+x = sw(s+u) = qsvw,
    x+x²/d = uw(s+u) = quvw.

Thus d | x² and both reconstructed denominators are integral.  They are
nsvw and nuvw, respectively, and direct substitution proves the displayed
identity for every positive n.

It remains to count and separate the classes.  Prime by prime, every divisor
D of a² has a unique expression D = Td₁² with T squarefree and d₁ | a/T;
then d₂ = a/(Td₁).  The involution D ↦ a²/D swaps d₁ and d₂, and its unique
fixed point is D = a.  Hence d₁ < d₂ selects exactly
(τ(a²)−1)/2 divisors D<a.  Multiplicativity gives

    ∑_{T|a} μ²(T)τ(a/T) = ∏_{p^e || a} ((e+1)+e)
                         = ∏_{p^e || a}(2e+1) = τ(a²),

so the count is f(ℓ).  Finally 0 < D < a < ℓ; therefore distinct D give
distinct residues −4D mod ℓ. ∎

For ℓ = 103, a = 26 and the eligible D are 1, 2, 4, 13, giving exactly the
four classes

    r = 99, 95, 87, 51                         (mod 103).

For ℓ = 199, a = 50 and the seven pairs (D,r) are

    (1,195), (2,191), (4,183), (5,179), (10,159), (20,119), (25,99).

`verify.py (n)` regenerates f(ℓ) = 4,7,17,24,7,7,22,67 on the full ladder,
checks distinctness, and checks the closed form and unit-fraction identity for
every ℓ = 103 and ℓ = 199 class at five n-values (55 exact checks, including
even/composite n).  This independently matches PW's stated counts and
identifies where the (log ℓ)² class mass comes from: one squarefree-kernel
choice T and one divisor split d₁d₂.  Equivalently, it is the divisor set of
a², cut in half by D ↔ a²/D.

### 15.3 Door verdict

**Measured verdict: no fixed-multiple gain for the eight tested primes,
k ≤ 20, and the all-n notion on n ≡ 1 (mod 4); the full declustering door is
unclear.**  The evidence is exhaustive over all 27,452 nonzero residue classes
in those eight moduli but finite in n: after 40 sampled n-values per class,
both halves pooled, only the endpoint candidate r = −4 remains.  There is no
measured growth at all, let alone (log ℓ)^{2+δ}.  This is evidence about the
stated ladder and k-range, not a theorem for arbitrary ℓ or k.

This does **not** close “ℓ-local structure” in general.  In the explicit
reconstruction, replacing n by n+ℓ replaces s by s+v and q by q+1.  That shows
only that these explicit witnesses are not fixed-q witnesses; it does not rule
out alternative fixed-q witnesses covering the same classes.  Indeed, the
r = −4 class has both descriptions noted in §15.1.  Fixed-q scans are therefore
not guaranteed to be an upper envelope for all ℓ-local families, and their
measured smallness cannot upper-bound more general families.  No theorem here
bounds the number of all possible forced classes, and no new family with B>2
was found.

The count in Lemma 15.1 also sharpens what a successful construction must add.
T and the split d₁d₂ already enumerate every divisor of a² once; rearranging
those parameters can only recluster the same τ(a²) supply.  To beat Vaughan in
this currency one needs a genuinely additional independent parameter that
produces distinct residues (and an all-n identity), not more witnesses inside
the same residue.  The tested k-shifts supplied no such parameter on the eight
primes through k = 20 (fixed criterion modulus q = kℓ).  This verdict is
superseded in a different direction by §16: varying A_k = (kℓ+1)/4 changes
the identity family while the criterion modulus is still allowed to vary
with n, so it was not part of the fixed-q experiment above.

## 16. Multiplier classes — CLAIMED/PROVISIONAL Vaughan-beating bounds

**Status.**  The record claim is subject to external verification and priority
search; Vaughan's primary paper (1970) remains access-blocked and was checked
only through the Pomerance-Weingartner 2025 reconstruction.

### 16.1 The generalized identity

**Lemma 16.1 (multiplier identity).**  Let \(k,\ell\) be positive integers with
\(k\ell\equiv3\pmod4\), and put

    A_k=(kℓ+1)/4.

For every factorization \(A_k=uvw\) into positive integers and every positive
integer \(n\) satisfying

    nv ≡ −u (mod kℓ),

put \(s=(nv+u)/(k\ell)\).  Then \(s\) is a positive integer and

    4/n = 1/(suw) + 1/(nsvw) + 1/(nuvw).                 (16.1)

In particular every such congruence class is forced representable.  Neither
primality of \(n\) or \(\ell\), nor a parity or size condition on \(n\), is
needed.  Also \((v,k\ell)=1\), so the class may equivalently be written
\(n\equiv-u v^{-1}\pmod{k\ell}\).

*Proof.*  Integrality of \(A_k\) is the congruence hypothesis.  Since
\((A_k,k\ell)=1\), every divisor of \(A_k\), including \(v\), is invertible
modulo \(k\ell\).  The assumed congruence makes \(s\) integral, and positivity
is immediate from \(n,u,v>0\).  On the common denominator \(nsuvw\), the
numerator on the right of (16.1) is

    nv+u+s = skℓ+s = s(kℓ+1) = 4suvw.

This is the numerator of \(4/n\), proving the identity. ∎

**Machine check.**  `verify.py (o)` exhausts thousands of factorizations for
prime and composite \(\ell\), several multipliers and four representatives of
each class.  It checks (16.1) with exact rational arithmetic and explicitly
requires that the sample include even and composite \(n\).

### 16.2 Counting compatible, distinct classes

All logarithms in this section are natural.  Write

    𝒦(K) = {k ≤ K : k ≡ 1 (mod 4)},     L_K = lcm_{k∈𝒦(K)} k.

The following elementary weighted lattice estimate is used in the prime
count.  It is recorded with the uniformity needed below.

**Lemma 16.2 (harmonic congruence lattice).**  Fix \(B>0\).  There are an
absolute \(K_0\) and a constant \(D=D(B)\) such that the following holds.  Let
\(K_0\le K\le(\log z)^B\), \(H=K^{10}\), \(z>H^2\), and let
\(\mathcal J\subseteq\mathcal K(K)\) contain 1.  If \((c,L_{\mathcal J})=1\),
where \(L_{\mathcal J}={\rm lcm}_{k\in\mathcal J}k\), put

    h(𝒥) = Σ_{k∈𝒥} φ(k)/k².

Then, uniformly in \(c\) and \(\mathcal J\),

    Σ_{k∈𝒥} Σ* 1/(uv)  ≍ (log z)^2 h(𝒥),                    (16.2)
    Σ_{k∈𝒥} Σ* 1/(φ(u)φ(v)) ≪ (log z)^2 h(𝒥).               (16.3)

Here \(\Sigma^*\) is over \(H<u,v\le z\),
\((u,v)=(uv,k)=1\), \(u+cv\equiv0\pmod k\); in the lower bound in
(16.2) one may additionally impose
\(\omega(uv)\le D\log\log z\), where \(\omega\) counts distinct prime
factors.  The implied constants depend only on \(B\).

*Proof.*  We give the box calculation, including the two weighted estimates
used later.  Fix \(\eta=1/20\), and first take two full multiplicative boxes
\(I=(U,(1+\eta)U]\), \(J=(V,(1+\eta)V]\).  Möbius inversion for
\((u,v)=1\) gives a sum over \(d\mid(u,v)\), necessarily with \((d,k)=1\).
After writing \(u=da,v=db\), the remaining congruence is
\(a+cb\equiv0\pmod k\).  For each reduced \(b\pmod k\) it specifies one
reduced \(a\pmod k\), and

    #{b∈J/d:(b,k)=1} = ηV φ(k)/(dk) + O(τ(k)),
    #{a∈I/d:a≡−cb (mod k)} = ηU/(dk) + O(1).

Using the first formula and then the second (or interchanging the variables)
therefore gives

    #{(a,b)∈I/d×J/d:(ab,k)=1, a+cb≡0 (mod k)}
      = η²UV φ(k)/(d²k²) + O((U+V)τ(k)/d).

Summing with weight \(\mu(d)\), and extending the main sum past the largest
possible \(d\), costs \(O(U+V)\).  Thus, uniformly in the reduced \(c\),

    #{(u,v)∈I×J:(u,v)=(uv,k)=1, k|u+cv}
      = η²UV · φ(k)/k² · P(k)
        + O((U+V)τ(k)log(2UV)),                              (16.4)
    P(k) = ∏_{p∤k}(1−p⁻²).

This also proves directly why the main density is \(\varphi(k)/k^2\), not
merely an average over \(c\).  Notice that
\(1/\zeta(2)\le P(k)\le1\).

Cover \((H,z]\) by these boxes (enlarging the last box for an upper bound and
discarding it for a lower bound).  Put \(L=\log(z/H)\); the number of boxes is
\(\asymp_\eta L\).  After division by \(UV\), the aggregate of all boundary
errors in (16.4), for one fixed \(k\), is

    ≪ τ(k)log z · L/H.                                      (16.5)

Indeed, the sum of \(1/U\) over the geometric box endpoints is
\(O_\eta(1/H)\), and the other variable supplies \(O_\eta(L)\) boxes.
The main term is \(\asymp_\eta(\varphi(k)/k^2)L^2\).  Since \(z>H^2\),
\(\log z/L<2\); and since
\(k^2/\varphi(k)\le k\tau(k)\) and \(\tau(k)\le2\sqrt k\), the ratio of
(16.5) to the main term is at most \(C K^2/H=C K^{-8}\) for an absolute
constant \(C\).  Choose the absolute \(K_0\) large enough that
\(CK_0^{-8}\le1/2\).  The fixed floor \(H=K^{10}\) then absorbs all
box-boundary errors uniformly for every \(k\le K\), rather than only after
averaging over \(k\).  We have proved

    Σ* 1/(uv) ≍ φ(k)/k² · L²                              (16.5a)

pointwise in \(k,c\).

We next prove the weighted upper bound needed both for (16.3) and for the
\(\omega\)-tail.  We use the following precise specialization of Shiu's
Brun--Titchmarsh theorem for nonnegative multiplicative functions.  If
\(F(p^a)\le A^a\), \(F(n)\ll_\epsilon n^\epsilon\), \((r,q)=1\),
\(q\le Y^{1/2}\), and \(\eta\) is fixed, then

    Σ_{Y<n≤(1+η)Y, n≡r (mod q)} F(n)
      ≪_{A,η} ηY/(φ(q)log Y)
         exp{Σ_{p≤2Y, p∤q} F(p)/p}.                         (16.5b)

This is Shiu's theorem with interval length \(\eta Y\); its modulus condition
holds here because \(k\le K\le H^{1/10}<U^{1/2},V^{1/2}\).  For the weighted
estimate below take the nonnegative multiplicative function
\(F(n)=t^{\omega(n)}\).  Then
\(F(p^a)=t\le t^a\), while
\(F(n)\le\tau(n)^{\log_2t}\ll_{t,\epsilon}n^\epsilon\).  Thus Shiu's growth
hypothesis is satisfied, and the prime local factor is still \(F(p)=t\).
Summing (16.5b) over the \(\varphi(k)\) reduced classes also gives

    Σ_{V<v≤(1+η)V, (v,k)=1} F(v)
      ≪_{A,η} ηV/log V
         exp{Σ_{p≤2V, p∤k} F(p)/p}.                         (16.5c)

Drop only the condition \((u,v)=1\).  Apply (16.5b) to the one reduced class
\(u\equiv-cv\pmod k\) for each \(v\), and (16.5c) to the resulting
\(v\)-sum.  Mertens' theorem then gives, uniformly for \(Y\ge H\),

    exp{Σ_{p≤2Y, p∤k} t/p}/log Y
       ≪_t (log Y)^{t−1} exp{−tΣ_{p|k}1/p},
    exp{Σ_{p≤2Y, p∤k} (p/(p−1))/p}/log Y
       ≪ exp{−Σ_{p|k}1/(p−1)}.                              (16.5d)

The same formula with \(t=1\) handles \(F=1\).  No factor depending on the
prime divisors of \(k\) is being suppressed here.  In fact, in each of the
three cases the quotient of the two local factors in (16.5d), together with
\(1/\varphi(k)\), by the desired density \(\varphi(k)/k^2\) is at most

    k²/φ(k)² · exp{−2Σ_{p|k} b_p},                           (16.5e)

where respectively \(b_p=t/p,1/(p-1),1/p\).  The logarithm of (16.5e) is

    Σ_{p|k}{−2log(1−1/p)−2b_p}.

For \(b_p=t/p\) its linear term is \(2(1-t)/p\le0\); for the other two
choices the linear terms cancel.  In all cases the remainder is
\(O_t(\sum_p p^{-2})\).  Hence (16.5e) is bounded by an absolute constant
(or a constant depending only on fixed \(t\)), uniformly in \(k\).

Dividing the box estimate by \(UV\), and summing the
\(O_\eta(L^2)\) pairs of boxes, now proves the explicit estimate

    Σ* t^{ω(u)+ω(v)}/(uv)
      ≪_t φ(k)/k² · L² (log z)^{2(t−1)},       1<t<2,         (16.5f)

for every reduced \(c\) and every \(k\le K\).  Taking instead
\(F(n)=n/\varphi(n)\) is legitimate because it is multiplicative and
\(F(p^a)=p/(p-1)\); since
\(F(u)F(v)/(uv)=1/(\varphi(u)\varphi(v))\), the same calculation gives

    Σ* 1/(φ(u)φ(v)) ≪ φ(k)/k² · L².                          (16.5g)

This proves (16.3), with the required \(\varphi(k)/k^2\) retained pointwise.
Equivalently, expanding
\(n/\varphi(n)=\sum_{d\mid n}\mu^2(d)/\varphi(d)\) produces the same local
factors: the extra divisor sums are bounded by
\(\sum_d\mu^2(d)/(d\varphi(d))<\infty\); (16.5d)--(16.5e) record explicitly
why primes dividing \(k\) do not introduce a growing factor.

Finally Rankin's inequality and (16.5f) show that, for each \(k\),

    Σ*_{ω(uv)>D log log z} 1/(uv)
      ≤ t^{−D log log z} Σ* t^{ω(u)+ω(v)}/(uv)
      ≪ φ(k)/k² · L² (log z)^{2(t−1)−D log t}.               (16.5h)

Here \((u,v)=1\) gives \(\omega(uv)=\omega(u)+\omega(v)\), so Rankin's
inequality applies exactly as displayed.  Fix, for example, \(t=3/2\), and
choose the integer \(D\) so that \(D\log t>2(t-1)\).  With fixed positive
margin in this inequality, enlarge the absolute \(K_0\) if necessary; since
\(z>K^{20}\), the ratio of (16.5h) to (16.5a) is then at most \(1/2\).
Thus at least half of the latter mass remains.  Summing the pointwise
estimates over an arbitrary \(\mathcal J\) proves (16.2)--(16.3), since
\(L\asymp\log z\).  Finally,
Möbius expansion of \(\varphi(k)/k\), with the progression
\(k\equiv1\pmod4\), gives

    Σ_{k∈𝒦(K)} φ(k)/k² ≍ log K.                              (16.6)

Thus \(h(\mathcal K(K))\asymp\log K\), as used below. ∎

The restriction \(K\ge K_0\) loses nothing in Theorem 16.4, where
\(K=\lfloor\delta\log N\rfloor\) tends to infinity; Theorem 16.5 is its
semigroup corollary.

The deliberately wasteful floor \(H=K^{10}\) makes the lattice errors
uniform and also makes cross-multiplier distinctness immediate.  It costs
only \(O(\log K)\) from a logarithm of size \(\asymp\log X\).

**Lemma 16.3 (class-mass lemma).**  There are constants \(a,A>0\) and an
absolute integer \(D\) with the following property.  Let \(X\) be large,
\(K_0\le K\le(\log X)^5\), \(H=K^{10}\), and let
\(\mathcal J\subseteq\mathcal K(K)\) contain 1.  Suppose
\((c,L_{\mathcal J})=1\).  For each prime
\(\ell\equiv3\pmod4\), \(X^{1/2}<\ell\le X\), let
\(f_c(\ell)=f_{c;\mathcal J,X}(\ell)\) be the number of distinct residues
\(-uv^{-1}\pmod\ell\) arising from triples

    k∈𝒥,  H<u,v≤ℓ^{1/3},  (u,v)=1,
    uv | (kℓ+1)/4,  k | u+cv,  ω(uv)≤D log log X.             (16.7)

Then, uniformly in \(c\) and \(\mathcal J\),

    a(log X)^2 h(𝒥) ≤ Σ_{X^{1/2}<ℓ≤X} f_c(ℓ)/ℓ
                     ≤ A(log X)^2 h(𝒥).                      (16.8)

Every one of these residues is a forced class from Lemma 16.1.

*Proof: distinctness.*  Take any \(k,k'\in\mathcal J\).  A collision between
the residues belonging to \((k,u,v)\) and \((k',u',v')\) modulo \(\ell\)
gives

    ℓ | uv'−u'v,    |uv'−u'v| < ℓ^{2/3} < ℓ.

Thus \(u/v=u'/v'\), and reducedness gives \((u,v)=(u',v')\).  If
\(k\ne k'\), put \(g=(A_k,A_{k'})\).  Here

    A_k−A_{k'} = ((k−k')/4)ℓ,

where \((k-k')/4\) is an integer because \(k\equiv k'\equiv1\pmod4\).
Also \((g,\ell)=1\), since each \(A_j=(j\ell+1)/4\) is prime to \(\ell\).
It follows that \(g\mid(k-k')/4\).  On the other hand the now-common product
\(uv\) divides both \(A_k,A_{k'}\), and hence divides \(g\), whereas

    uv > H² > K > |k−k'|/4.

This is a contradiction.  For \(k=k'\), equality of the ordered pair also
fixes \(w=A_k/(uv)\).  Thus (16.7) has no duplicates for any pair \(k,k'\);
the stated honest deduplication changes nothing.

*Proof: lower bound.*  Partition \((X^{1/2},X]\) into dyadic intervals
\((x,2x]\), and fix the parameter \(B=6\) in Lemma 16.2.  In one interval
put \(z=x^{1/6}\) and retain only \(u,v\le z\).  Since
\(x\ge X^{1/2}\),

    log z ≥ (1/12)log X,    z>H² ⇔ (1/6)log x>20log K.

The latter inequality holds uniformly once \(X\) is large because
\(K\le(\log X)^5\); the same assumption gives
\(K\le(\log z)^6\) (indeed \((\log X)^5\le(\log X/12)^6\) eventually).
Thus every hypothesis of Lemma 16.2 is met.  Also \(z\le\ell^{1/3}\) for
\(\ell>x\), so these pairs satisfy the size condition in (16.7).  The
lemma supplies pairs with
\(\omega(uv)\le D(6)\log\log z\); because

    log log z = log log X + O(1),    log log z ≤ log log X,

these pairs are included after fixing the \(D\) in (16.7) to be \(D(6)\).
This explicitly reconciles the two cutoffs.

For every retained \((k,u,v)\), divisibility in (16.7) is exactly the reduced
prime progression

    ℓ ≡ −k^{-1} (mod 4uv).                                  (16.9)

It already includes \(\ell\equiv3\pmod4\), since \(k\equiv1\pmod4\), and
its modulus is

    q=4uv ≤ 4x^{1/3}.

Here is the Bombieri--Vinogradov bookkeeping.  For a prescribed \(R\), use
the standard level

    q ≤ x^{1/2}/(log x)^{A_R},
    Σ_q max_{(a,q)=1}|π(2x;q,a)−π(x;q,a)
       −(li(2x)−li(x))/φ(q)| ≪_R x/(log x)^R.

For large \(x\), every \(q\le4x^{1/3}\) lies below that level.  A fixed
\(q=4uv\) is generated by at most

    W(q) ≤ K·2^{ω(uv)}
         ≤ (log X)^{5+D log 2} = (log X)^{C_D}               (16.9a)

triples: coprimality assigns each whole prime power of \(uv\) to either \(u\)
or \(v\), giving at most \(2^{\omega(uv)}\) ordered assignments, and there
are at most \(K\) choices of \(k\).  Since
\(\log x\asymp\log X\), take \(R=C_D+10\) and the corresponding
Bombieri--Vinogradov constant \(A_R\).  Multiplying the displayed error sum
by (16.9a) gives \(O(x/(\log x)^{10})\), negligible uniformly in \(c\).
Lemma 16.2 and \(1/\varphi(4uv)\ge1/(4uv)\) give the main term

    ≫ x/log x · (log x)^2 h(𝒥) = x log x\,h(𝒥).              (16.10)

Consequently this dyadic interval contributes
\(\gg\log x\,h(\mathcal J)\) to the reciprocal sum.  There are
\(\asymp\log X\) such intervals and throughout them \(\log x\asymp\log X\),
which proves the lower half of (16.8).

*Proof: upper bound.*  On \((x,2x]\), put \(z=(2x)^{1/3}\), enlarge to
\(u,v\le z\), and drop the \(\omega\)-restriction.  The same explicit
checks give \(z>H^2\) and \(K\le(\log z)^6\) for large \(X\).  Brun--Titchmarsh
in (16.9), followed by (16.3), gives

    Σ_{x<ℓ≤2x} f_c(ℓ)
      ≪ x/log x · Σ_{k,u,v} 1/(φ(u)φ(v))
      ≪ x log x\,h(𝒥).                                      (16.11)

Here \(4uv\ll x^{2/3}\), so the Brun--Titchmarsh denominator
\(\log(x/(4uv))\) is \(\gg\log x\).  Dividing by \(x\) and summing the same
dyadic intervals proves the upper half.  This also proves the asserted
uniformity: the only appearance of \(c\) was in Lemma 16.2, which is
pointwise for every \((c,L_{\mathcal J})=1\).  Finally (16.7) says
\(A_k=uvw\) for an integer \(w>0\), and \(cv\equiv-u\pmod k\).  Lemma 16.1
supplies the forced class. ∎

This is the promised PW-Lemma-4.1-style divisor-sum argument.  For the full
family the new factor \(h(\mathcal J)\asymp\log K\) comes from (16.6).
Unlike an average-over-\(c\) heuristic, (16.8) is pointwise in every
subsequence reduced modulo \(L_{\mathcal J}\), so no unproved distributional
claim about the shifted values remains.

### 16.3 Uniformity over subsequences

Set \(M_0=24L_K\), and fix a residue \(c\pmod{M_0}\) with
\((c,M_0)=1\).  If \(n\equiv c\pmod{M_0}\), a triple counted in (16.7)
satisfies \(nv\equiv-u\pmod k\).  If in addition
\(n\equiv-uv^{-1}\pmod\ell\), then, since \((k,\ell)=1\), the two
congruences combine to

    nv ≡ −u (mod kℓ).

Thus the composite-modulus class of Lemma 16.1 becomes one genuine forbidden
class modulo \(\ell\) after passing to the subsequence.  Also
\((M_0,\ell)=1\) for \(\ell>X^{1/2}>K\), so it is one class for the
subsequence variable \((n-c)/M_0\).  The distinctness proof in Lemma 16.3
shows that the \(f_c(\ell)\) classes remain distinct after this affine change.
This checks the CRT reduction, including its often-missed \(k\)-part.

There is no bad-\(c\) tail to estimate for the prime exceptional set.  Every
prime \(n>K\) is coprime to \(M_0\), and Lemma 16.3 gives the lower mass in
(16.8) **for each such \(c\)**.  The proposed exponential-moment argument over
all residues would in fact be false without qualification: for example a
residue divisible by every prime factor of \(L_K\) has no compatible
multiplier containing those factors.  Such nonreduced residues contain no
prime \(n>K\), which is exactly why they must be removed rather than averaged
into a prime theorem.  This pointwise reduced-class argument is stronger than
any of the candidate concentration statements in the program.

### 16.4 Large sieve and the improved exponent

Recall the convention from (13.1):

    E(N) = #{p≤N prime : 4/p is not a sum of three unit fractions}.

**Theorem 16.4.**  There is an absolute constant \(c>0\) such that, for all
sufficiently large \(N\),

    E(N) ≪ N exp{−c (log N)^{2/3}(log log N)^{1/3}}.           (16.12)

*Proof.*  Choose a sufficiently small fixed \(\delta>0\), put
\(K=\lfloor\delta\log N\rfloor\), and use \(M_0=24L_K\).  For sufficiently
large \(N\), this \(K\) is at least the absolute \(K_0\) from Lemma 16.2.
Since \(L_K\) divides \({\rm lcm}(1,\ldots,K)\), the prime number theorem (the elementary
Chebyshev upper bound would suffice after reducing \(\delta\)) gives

    log M_0 ≤ (1+o(1))K,

so \(Y:=N/M_0\ge N^{1-2\delta}\).  Put

    X = exp{α (log N/log log N)^{1/3}},                       (16.13)

where \(\alpha>0\) is a sufficiently small absolute constant.  Then
\(K\le(\log X)^5\), as required in Lemma 16.3.

Fix a reduced class \(c\pmod{M_0}\).  A counterexample prime in this class
avoids the \(f_c(\ell)\) classes modulo every prime
\(X^{1/2}<\ell\le X\).  Apply the usual larger-sieve form used in PW §4 to
the interval of at most \(Y+1\) values of \((n-c)/M_0\).  With
\(Q=Y^{1/2}\), its denominator is

    S_c = Σ_{s≤Q,\ s|P} μ²(s) ∏_{ℓ|s} f_c(ℓ)/(ℓ−f_c(ℓ)),
    P   = ∏_{X^{1/2}<ℓ≤X} ℓ,

and the number left is \(O(Y/S_c)\).  Put

    G_c = ∏_{X^{1/2}<ℓ≤X} (1+f_c(ℓ)/(ℓ−f_c(ℓ))).

The elementary bound \(f_c(\ell)\le K\ell^{2/3}<\ell/2\), valid here for
large \(N\), and the upper half of (16.8) give, with
\(v=1/\log X\),

    (G_c−S_c)/G_c
      ≤ exp{−log Y/(2log X) + (e−1)Σ f_c(ℓ)/ℓ}
      ≤ exp{−log Y/(2log X) + C(log X)^2 log K}.              (16.14)

Choose \(\alpha\) in (16.13) so small that
\((\log X)^3\log K\le(\log Y)/(4C)\).  Then (16.14) is less than \(1/2\).
The lower half of (16.8) now yields

    S_c ≥ G_c/2 ≥ (1/2)exp{a(log X)^2 log K}.

This is uniform in \(c\).  Summing \(O(Y/S_c)\) over the at most \(M_0\)
reduced subsequences, and absorbing primes at most \(K\), gives

    E(N) ≪ N exp{−a(log X)^2 log K}
         ≪ N exp{−c(log N)^{2/3}(log log N)^{1/3}},

as claimed. ∎

The prime bound immediately gives the same full logarithmic strength for all
denominators; no treatment of nonreduced multiplier subsequences is needed.
The point is that exceptional integers lie in the multiplicative semigroup
generated by exceptional primes.

**Theorem 16.5 (all exceptional denominators).**  Let

    E_all(N) = #{n≤N : 4/n is not a sum of three unit fractions}.

There is an absolute \(c>0\) such that, for all sufficiently large \(N\),

    E_all(N) ≪ N exp{−c (log N)^{2/3}(log log N)^{1/3}}.      (16.15)

*Proof.*  Every prime factor of an exceptional integer \(n>1\) is itself
exceptional.  Indeed, if \(p\mid n\) and

    4/p = 1/x₁ + 1/x₂ + 1/x₃,

then scaling the three denominators gives

    4/n = 1/((n/p)x₁) + 1/((n/p)x₂) + 1/((n/p)x₃),

contrary to exceptionality of \(n\).  Thus the exceptional integers are a
subset of the multiplicative semigroup generated by exceptional primes,
where the semigroup includes the empty product \(1\).  The case \(n=1\)
contributes only \(O(1)\).

Write

    g(u)=u^{2/3}(log u)^{1/3},    x=e^L.

Fix \(x_0\ge e^e\) large enough that Theorem 16.4 gives, for every
\(x\ge x_0\),

    E(x) ≪ x exp{−c₀g(log x)}.                                (16.16)

Fix \(0<\eta<c₀\), and for large \(L\) put
\(\delta=\eta g(L)/L\), so \(0<\delta<1/4\).  Rankin's inequality over the
above multiplicative semigroup gives

    E_all(x)
      ≤ x^{1−δ} ∏_{p≤x,\ p exceptional}(1−p^{−1+δ})^{−1}.    (16.17)

Only primes at most \(x\) occur because an integer counted on the left is at
most \(x\).

We show that the Euler product in (16.17) is bounded uniformly in \(x\).
Split at the fixed \(x_0\).  The finitely many exceptional primes
\(p\le x_0\) contribute \(O(1)\), uniformly for \(0<\delta<1/4\).  Partial
summation on \([x_0,x]\), (16.16), and the endpoint estimate
\(\delta L-c₀g(L)=-(c₀-\eta)g(L)<0\) give

    Σ_{p≤x,\ p exceptional} p^{−1+δ}
      ≪ 1 + E(x)x^{−1+δ}
           + ∫_{x₀}^x E(t)t^{−2+δ}dt
      ≪ 1 + ∫_{log x₀}^L exp{δu−c₀g(u)}du.                   (16.18)

For \(u\ge\log x_0\ge e\),

    g(u)/u = u^{−1/3}(log u)^{1/3}

is decreasing.  Hence, for \(u\le L\),

    δu = η(g(L)/L)u ≤ ηg(u).

The last integral in (16.18) is therefore at most
\(\int_{\log x_0}^\infty\exp\{-(c₀-\eta)g(u)\}\,du<\infty\).  This proves
\(\sum p^{-1+\delta}=O(1)\), uniformly in \(x\).  Finally, the prime-power
terms in the logarithm of the Euler product satisfy

    Σ_{p≤x} Σ_{j≥2} p^{−j(1−δ)}/j
      ≤ Σ_p Σ_{j≥2} p^{−3j/4}/j = O(1).

Thus the product in (16.17) is \(O(1)\), and

    E_all(x) ≪ x^{1−δ}
             = x exp{−ηg(log x)},

which is (16.15).  Salez's verification through \(10^{17}\) is unnecessary
for this implication, although it can be used as a convenient finite base. ∎

**Scope and provisional verdict.**  Theorems 16.4 and 16.5 now have the same
full-strength saving
\((\log N)^{2/3}(\log\log N)^{1/3}\), respectively for prime denominators
and for all integer denominators.  They are CLAIMED/PROVISIONAL
Vaughan-beating bounds, subject to external verification and priority search;
Vaughan's primary paper (1970) remains access-blocked and was checked only
through the Pomerance-Weingartner 2025 reconstruction.  The all-integer result
is a semigroup corollary of the prime result, not an assertion that
Lemma 16.3 applies to nonreduced integer subsequences.

**Wave-13 supersession note (appended; CLAIMED/PROVISIONAL).**  Theorem 39.7
claims the stronger unconditional saving
\(\exp\{-c(\log N)^{3/4}\}\).  The present theorem remains the externally
unchecked prior benchmark until §39's three load-bearing steps receive an
independent hostile review.

## 17. The pointwise frontier: exact reformulations of "all p", the walls
that close, and what a proof would have to look like

Sections 5–16 mapped the almost-all machinery to its ceilings.  This section
attacks the remaining question — the conjecture itself, "for **every** prime
p" — by (a) reducing it to its sharpest equivalent forms, (b) proving new
obstruction theorems that close the remaining elementary pointwise routes,
and (c) auditing the pointwise-capable technologies of analytic number
theory against the problem's structure.  Labels are strict: **Theorem/Lemma**
= proved here; **Assessment** = argued under named assumptions, not proved.
*(This section was rewritten after a hostile referee round; the original
overclaims in 17.3, 17.4 and 17.6 are repaired or withdrawn below.)*

### 17.1 The four-parameter completeness theorem and the shifted-multiple
dictionary

Solutions are counted as ordered triples with the p-divisible denominators
placed last; swapping a and b swaps two same-type denominators.

**Theorem 17.1 (complete parametrization of both solution types).**  Let p be
an odd prime.

(i) **Type II (Case B; two denominators divisible by p).**  The map

    (a, b, c, k) ↦ 4/p = 1/(abc) + 1/(pack) + 1/(pbck)

is a bijection from quadruples of positive integers with gcd(a, b) = 1 and

    kp = 4abck − a − b                                         (17.1)

onto the Case-B solutions.  The criterion-3.1(B) dictionary is
q = (a+b)/k, x = abc, d = a²c.  Dropping the condition gcd(a, b) = 1 in
(17.1) still yields a valid solution by the same identity (the map is then
no longer injective).

(ii) **Type I (Case A; one denominator divisible by p).**  Likewise

    (a, b, c, k) ↦ 4/p = 1/(ack) + 1/(bck) + 1/(pabc),
    p(a + b) = k(4abc − 1),  gcd(a, b) = 1,                    (17.2)

is a bijection onto the Case-A solutions; dictionary m = (a+b)/k, z₀ = abc,
d = a²c.

(iii) **Divisor form.**  For fixed (c, k), the pairs (a, b) of positive
integers (not necessarily coprime) satisfying (17.1) correspond exactly to
the divisors D ≡ −1 (mod 4ck) of 4pck² + 1, via D = 4ack − 1; the cofactor
is then automatically (4pck²+1)/D = 4bck − 1 ≡ −1 (mod 4ck):

    (4ack − 1)(4bck − 1) = 4pck² + 1.                          (17.3)

Hence: **p is Case-B solvable ⟺ some member of the two-parameter family
{4pck² + 1 : c, k ≥ 1} has a divisor ≡ −1 (mod 4ck).**  (Coprimality of
(a, b) is immaterial here: a non-coprime pair still solves (17.1) and hence
produces a solution; its canonical re-decomposition under (i) generally
lands at a different (c, k) — e.g. p = 29, (c,k) = (1,2), D = 15 gives
(a,b) = (2,4), whose canonical form is (a,b,c,k) = (1,2,4,1).)

*Proof.* (i, ⟸)  With kp = 4abck − a − b, the three fractions have common
denominator pabck and numerator sum kp + a + b = 4abck, so they sum to 4/p.
Since a + b ≤ 2ab ≤ 2abck, (17.1) gives kp ≥ 2abck, so p ≥ 2abc > abc;
hence p ∤ abc: exactly the last two denominators are divisible by p, and
the solution is Case B.
(i, ⟹)  Let (q, d, x) be a criterion-B witness (Thm 3.1), g₀ = gcd(d, x),
a = d/g₀, c = g₀/a, b = x/(ac), k = (a + b)/q.  These are integers: for
each prime r, with α = v_r(d), ξ = v_r(x), the hypothesis d | x² gives
α ≤ 2ξ, whence v_r(a) = α − min(α, ξ) ≤ min(α, ξ) = v_r(g₀) (check the
two cases α ≤ ξ and ξ < α ≤ 2ξ), so a | g₀; v_r(b) = ξ − min(α, ξ) ≥ 0;
and min(v_r(a), v_r(b)) = 0, so gcd(a, b) = 1.  Valuation bookkeeping gives
d = a²c and x = abc; q | d + x = ac(a + b) with gcd(q, ac) = 1 (since
ac | x and gcd(q, x) = gcd(p, x) = 1), so q | a + b.  Finally
kp = k(4x − q) = 4abck − (a + b), which is (17.1), and substituting the
dictionary into Thm 3.1(B)'s reconstruction returns exactly
(abc, pack, pbck).  The two maps are mutually inverse on the stated data.
(ii)  Same valuation argument verbatim on (m, d, z₀), using
gcd(m, z₀) = 1 from the proof of Thm 3.1(A); then 4z₀ = pm + 1 gives
pmk = k(4abc − 1), i.e. (17.2) with m = (a+b)/k.  For (ii, ⟸) one needs
p ∤ k (so that m = (a+b)/k is genuinely the criterion modulus and the type
is Case A): if p | k, dividing (17.2) by p gives a + b = (k/p)(4abc − 1)
≥ 4abc − 1 ≥ 4ab − 1 ≥ 2(a + b) − 1 > a + b; contradiction.  Hence p | 4abc − 1 and p ∤ abck.
(iii)  D := 4ack − 1 ≡ −1 (mod 4ck) divides the RHS of (17.3) by
expanding with (17.1).  Conversely if D ≡ −1 (mod 4ck) divides
n := 4pck² + 1, then n ≡ 1 (mod 4ck) forces the cofactor n/D ≡ −1
(mod 4ck), so D = 4ack − 1 and n/D = 4bck − 1 with a, b ≥ 1, and
expanding (17.3) backwards gives (17.1). ∎

Machine checks: `verify.py (p)` (symbolic identities, random
reconstructions of both types, the p = 29 regression above); §19.3 verified
the decomposition (i, ⟹) on all 36,384 stored witnesses with zero failures,
and (17.3) on the same rows.  The k = 1 slice of (17.1) is the classical
family F1 of §4 (Rosati-type); the four-parameter forms match the shape of
the Elsholtz–Tao Type I/II parametrizations *(cited from memory —
flagged)*.  Six primes below 10⁵ (409, 577, 5569, 9601, 23929, 83449) have
**no** k = 1 representation at all (§19.3), so the full k-range is genuinely
needed — e.g. 409 first solves at (a,b,c,k) = (1,13,8,2):
4/409 = 1/104 + 1/6544 + 1/85072.

The window form of the k = 1 slice, used in 17.5(a): a pair (a, b),
gcd(a, b) = 1, with 4ab | p + a + b corresponds to b | p + a with cofactor
condition (p + a)/b ≡ −1 (mod 4a); so the k = 1 Case-B witness count is

    N₁(p; A) = Σ_{a ≤ A} #{ b | p + a : gcd(a,b) = 1,
                             (p + a)/b ≡ −1 (mod 4a) }.        (17.4)

### 17.2 The quadratic layer is pointwise inert

By §8.2/§9.1/§10.2, the one piece of global reciprocity structure on the
witness problem is a single quadratic bit.  One could hope to run this bit
against an exceptional p across the whole family.  It cannot be done:

**Lemma 17.2 (parity self-consistency).**  For n coprime to p let λ_p(n) =
(n | p) (Jacobi symbol), the completely multiplicative function with
λ_p(r) = (r | p) on primes r ∤ p.  Then for every prime p ≡ 1 (mod 4):

* every Case-A value z₀ = (pm + 1)/4 (m ≡ 3p (mod 4)) is coprime to p and
  satisfies λ_p(z₀) = +1;
* every member 4pck² + 1 of the Case-B family is coprime to p and satisfies
  λ_p(4pck² + 1) = +1.

I.e. the number of quadratic-nonresidue-mod-p prime factors (with
multiplicity) of every witness value in both families is **even — always,
for every p**, exceptional or not.

*Proof.*  Both values are ≡ 1 (mod p), hence coprime to p.  4z₀ = pm + 1
≡ 1 (mod p) and (4 | p) = 1, so λ_p(z₀) = (4z₀ | p) = (1 | p) = +1;
likewise for 4pck² + 1. ∎

**Consequence (assessment).**  The quadratic layer imposes *zero* pointwise
cost on a would-be exceptional p: its constraint is automatically satisfied
across the entire witness family.  This is §6's parity mechanism in final
form, and it matches the §19.2 taxonomy: per-modulus failures are 99%
local-Jacobi (F1), yet these local obstructions always assemble into a
globally self-consistent configuration.  A pointwise proof must therefore
extract its contradiction from finer-than-quadratic structure; §10.2 shows
the Brauer group supplies no further *reciprocity* class (this does not
exclude non-Brauer structure, but none is known).

### 17.3 The square-class escape theorem, and the free-component mechanism

**Theorem 17.3 (residue 1 escapes every forced class of every shape in this
document).**  No forced-solvability class of any of the following family
shapes contains any integer n ≡ 1 (mod M), where M is the family's full
progression modulus:

(a) the Case-B congruence families (q, d, R) of §4 and the Case-A mirror
families (m, d, R)  [Theorem 5.1 and its Case-A verbatim];
(b) the F1 and L families of §4  [Lemma 5.2];
(c) the multiplier classes of Lemma 16.1, i.e. the full class set
𝓡(M) = {−4D (mod M) : D | A², A = (M+1)/4} of Lemma 18.1, for every
M ≡ 3 (mod 4);
(d) the Case-A moving-c families: for positive integers (a, b, m) with
gcd(a, b) = 1, m | a + b, m ≡ 3 (mod 4), the class p ≡ −m⁻¹ (mod 4ab),
each member solvable via c = (pm+1)/(4ab), k = (a+b)/m and (17.2);
(e) the Case-B moving-c families: for positive integers (a, b, k) with
k | a + b and q := (a+b)/k ≡ 3 (mod 4), the class p ≡ −q (mod 4ab)
(members p > 4ab − q), each member solvable via c = (p+q)/(4ab) and
(17.1) — e.g. (a, b, k) = (1, 13, 2): p = 52c − 7, containing 97 and 409.

*Proof of (c).*  For A = 1 (M = 3): 4D + 1 = 5 is not divisible by 3.  Let
A ≥ 2.  Suppose D | A² and −4D ≡ 1, i.e. M | 4D + 1.  Write
4D + 1 = (4A − 1)t; reducing mod 4 gives t ≡ 3 (mod 4), so t ≥ 3 and
D ≥ (3(4A−1) − 1)/4 = 3A − 1 > A.  The cofactor D' = A²/D then satisfies
D' ≤ A²/(3A − 1) < A/2 (for A ≥ 2).  Since 4A ≡ 1 (mod M), from
4D ≡ −1 we get D ≡ −A, and multiplying D·D' = A² by 16 gives
(4D)(4D') ≡ 16A² ≡ 1, so 4D' ≡ −1 and D' ≡ −A (mod M) as well.  Hence
M | D' + A with 0 < D' + A < 3A/2 < 4A − 1 = M: contradiction. ∎

*Proof of (d).*  The family is well-defined: gcd(m, 4ab) = 1 (a prime
dividing m and ab would divide both a and b via m | a + b), and for p in
the class, c = (pm+1)/(4ab) is a positive integer with z₀ = abc,
d = a²c, m | d + z₀ = ac(a + b), giving (17.2); `verify.py (p)` replays
end-to-end examples.  Avoidance of 1: the class contains 1 iff
m ≡ −1 (mod 4ab); but 4ab − 1 > a + b ≥ m for all positive a, b (since
4ab − a − b − 1 = (4a−1)(4b−1)/4 − 5/4 ≥ 9/4 − 5/4 > 0), so
m ≡ −1 (mod 4ab) is impossible. ∎

*Proof of (e).*  For p in the class, c = (p+q)/(4ab) is a positive
integer; kp = k(4abc − q) = 4abck − (a+b) is (17.1), so p is solvable
(coprimality of (a, b) is not needed, per Thm 17.1(iii)'s remark).
Avoidance of 1: the class contains 1 iff q ≡ −1 (mod 4ab); but
q ≤ a + b < 4ab − 1 as in (d). ∎

**Corollary 17.3.1 (bounded-modulus identity systems never close).**  For
every Q there are infinitely many primes p ≡ 1 (mod 24) avoiding every
forced class of every family of shapes (a)–(e) whose progression modulus is
≤ Q: by Theorem 17.3 the single class 1 (mod lcm(24, all moduli ≤ Q))
escapes them all, and Dirichlet supplies its primes.  (Schinzel's theorem —
cited, §5 — extends the escape to *all* polynomial identity families, of
any shape; (c), (d), (e) above are the moving-parameter shapes arising in
this campaign, with self-contained proofs.)  Consequently no proof of the
conjecture can consist of finitely many forced-class families of these
shapes, and any certificate system whose reach is a finite union of such
classes inherits the same escape. ∎

**The free-component mechanism (assessment, with worked computation).**  Can
an exceptional p's own arithmetic be turned against it — moduli built from
prime factors ℓ' of its shifted values, where p's residue is known?  The
obstruction is structural.  Say ℓ' | (p+3)/4, so p ≡ −3 (mod ℓ').  A
Lemma-16.1 class mod kℓ' hits p only if its ℓ'-projection is −3, i.e.
(Lemma 18.1) −4D ≡ −3, D ≡ 3·4⁻¹ (mod ℓ'), D | A², A = (kℓ'+1)/4.  Such
(k, D) exist in abundance — but the class constrains p modulo kℓ', and
p mod k is *not* controlled by p's relation to ℓ'.  The identity supply
pins p only in full CRT components; every modulus containing one "known"
component drags in a free cofactor component in which p occupies one
compatible residue class among many.  Empirically (§11.1, §19) this is how
near-exceptional primes survive to w* = 59: each new modulus is an
independent escape chance, never a forced hit.  Self-witnessing dies at the
same compactness wall.

### 17.4 The entropy wall for oblivious coverage

Call an **oblivious box-certificate** the following data, for primes p in a
fixed congruence class: a window length T = T(p); a divisibility pattern
P = ∏_{r ≤ y} r^{a_r} with P ≤ T (guaranteeing multiples x of P in
(p/4, p/4 + T], hence criterion pairs (x, q), q = 4x − p ≤ 4T); and a
correctness argument that, for **every** assignment of residues (r mod q)
to the primes r | P consistent with the certificate's congruence data, some
divisor of P² lies in the class −x (mod q) for some designated multiple x.
(The adversary may be further constrained by the quadratic layer
(r | q) = (r | p) of Prop 8.1; the all-ones assignment below respects it.)

**Lemma 17.4.1 (box-coverage mass bound; proved).**  Let G be a finite
abelian group, ψ: G → C a surjection onto a cyclic group, and S ⊆ G with
|ψ(S)| = s.  There is an assignment of elements g₁, …, g_j ∈ G (namely:
all ψ(g_i) equal to one generator γ of C) under which the products
{∏ g_i^{e_i} : 0 ≤ e_i ≤ E_i} can meet every element of S only if

    Σ_i E_i ≥ s − 1.

*Proof.*  ψ of every product lies in {γ^e : 0 ≤ e ≤ ΣE_i}, a set of at
most ΣE_i + 1 elements of C, which must contain ψ(S). ∎

**Lemma 17.4.2 (the pinned-target corner is a §5-shape family; proved,
with an admissibility proviso).**  Suppose the all-ones assignment (every
r | P given residue 1 mod q) is admissible for the certificate class —
i.e. not excluded by the certificate's congruence data; note it satisfies
(r | q) = +1, so it is excluded in particular whenever the class pins some
(r | p) = −1 for r | P via Prop 8.1 (one important example of excluding
data, not the only conceivable one).  In that assignment every divisor of
P² is ≡ 1 (mod q); a certificate correct there must designate an x with
−x ≡ 1, i.e. q | x + 1, i.e. **q | p + 4** (from 4(x+1) = q + p + 4).
For fixed q this is a single congruence class of p — a §4 d = 1 family —
and any finite union of such classes is escaped by Cor 17.3.1. ∎

Certificate classes that pin negative quadratic data ((r | p) = −1 for
some r | P) evade this corner argument; for those, only the mass bound of
Lemma 17.4.1 applies (through any cyclic quotient of the index-2 subgroup
pattern), and the assessment below is correspondingly weaker there.

**Assessment 17.4.3 (the entropy wall).**  A certificate that does not
collapse to the pinned corner must cover, at each arising modulus q, a
target set −x·{realizable multiples} whose image in the maximal cyclic
quotient (of order λ(q), the Carmichael function) has some size s(q); by
Lemma 17.4.1 its exponent mass must be ≥ s(q) − 1, so
P ≥ 2^{(s(q)−1)/2} and T ≥ P.  Two escape routes remain, and both are
walls rather than doors:

* *Small target image.*  Keeping s(q) bounded means pinning x by further
  congruences; in the limit this is Lemma 17.4.2's corner (a congruence
  family).  Intermediate pinning still yields, in the all-ones
  configuration, a bounded set of forced congruences q | x + 1-type — a
  finite union of §5-shape classes, escaped by Cor 17.3.1.  This branch
  carries Lemma 17.4.2's proviso: it binds only certificate classes for
  which the all-ones (or an equivalent single-coset) assignment is
  admissible; classes pinning negative quadratic data are constrained only
  by the mass bound.
* *Small cyclic quotient.*  Moduli with λ(q) ≤ C log T evade the mass
  bound.  But integers with λ(q) ≤ (log q)^{O(1)} are of density q^{−1+o(1)}
  (Erdős–Pomerance–Schmutz-type counts — *cited from memory, flagged*), so
  windows are not guaranteed to contain any; forcing 4x − p to land on such
  a sparse, multiplicatively special set is itself a strong-forcing problem
  with no known mechanism (and none of the §4/§16 shapes produces it).

Conclusion (assessment, not theorem): oblivious coverage certificates with
sub-exponential windows are structurally confined to (i) congruence-family
reach — closed by Theorem 17.3 — or (ii) unproved strong forcing onto
λ-special moduli.  The original stronger claim ("no oblivious-certificate
system proves the conjecture", as a theorem) is **withdrawn**; this
assessment is what the argument actually delivers.

**Lemma 17.4.4 (Mahler measure of the exponent box; proved) and its honest
reading.**  For E ≥ 1 and D_E(θ) = Σ_{e=0}^{E} e(eθ),

    ∫₀¹ log |D_E(θ)| dθ = 0     exactly

(D_E(e(θ)) = (z^{E+1}−1)/(z−1), a quotient of products of cyclotomic
polynomials; Kronecker).  **Assessment.**  In a model where a character χ
of large order assigns the primes of P independent equidistributed phases,
log|∏_r D_{2a_r}(arg χ(r))| is a mean-zero random walk, while the principal
term is ∏(2a_r + 1); the *relative* size of nonprincipal to principal
character sums therefore decays like ∏(2a_r+1)^{−1+o(1)} for a *fixed*
nonprincipal character, typically over configurations (the o(1) absorbs
e^{O(√j)} CLT fluctuations); full residue-class equidistribution needs in
addition control of the aggregate over growing numbers of characters, which
the model does not by itself supply.  This is consistent with Lemma 12.5
and with the measured §11.1 success rates.  What the model does
not and cannot deliver is decay in the *worst* configuration — Lemma 17.4.1
— and the gap between average-case success and worst-case failure is
precisely the almost-all/exceptional-set shape of every bound in this
campaign.  (An earlier draft misread the zero drift as blocking average-case
equidistribution; the corrected reading is the one above.)

### 17.5 The pointwise-technology audit

All items are **assessments** (with computations), not theorems: for each
technology that elsewhere yields "for all n, no exceptions" statements, the
structural prerequisite it needs and the reason it is absent here.

**(a) Spectral/automorphic positivity (Duke-type).**  The k = 1 witness
count (17.4) expands, via Dirichlet characters mod 4a on the cofactor
condition, into sums of λ_χ(p + a) = Σ_{b | p+a} χ(b) — coefficients of
*Eisenstein* series (ζ(s)L(s, χ)) — with conductor 4a moving with the
shift.  Duke-type proofs of "every large n is represented" rest on: a main
term of polynomial size, cusp-form positivity (theta series), and
subconvex/power-saving errors.  Here the expected main term is
polylogarithmic in p at any polylog cutoff A (a heuristic scale, cutoff-
dependent; compare the class-mass Θ((log Q)³) of Thm 18.2 at modulus
cutoff Q — not a pointwise statement), there is no cusp component and no
theta structure (§10: rigid surface, Br = ℤ/2), and power-saving errors
against polylog main terms are unavailable in any known framework.  What
remains true: proving a pointwise asymptotic for (17.4) with error o(main)
uniformly in p would settle the conjecture — this is the analytic shape of
the residual problem, not a route currently walkable.

**(b) L-function repulsion (Linnik-type).**  Linnik's theorem gets
pointwise-in-q results from the L-function family mod q (log-free zero
density + Deuring–Heilbronn repulsion).  The failure event here — "no
divisor of any 4pck² + 1 in the moving class" — has no known encoding as a
fixed-conductor L-function family or Euler product; the character sums that
do appear (panel (a)) have moving conductors tied to the divisor structure,
and no repulsion phenomenon is known for them.  (Panel (a) shows character
L-functions do appear locally; what is missing is a *family with a zero-*
*density/repulsion theory* attached to the full event.)

**(c) Chebotarev/GRH-effective form families.**  §8.1's quadratic-form
families cover p when a Frobenius condition holds in the ring class field
of disc 4s(s−1) (degree ~ class number h₀(s); with regulator ≍ log s the
class-number formula gives h₀(s) = s^{1+o(1)}, modulo L(1, χ) factors —
heuristic normalization).  A coverage-density model of ≍ (log s)/s per s
makes Σ_s (log s)/s ≍ (log S)² diverge — consistent with "true with
room".  But controlling the *joint* distribution of Frob_p across the
family requires Chebotarev in the compositum L of the fields up to S, whose
degree is n_L ≤ ∏_{s≤S} h₀(s) = exp(Σ log h₀(s)) = exp(S^{1+o(1)})
(the product is the independence-model scale; even the quadratic subfields
alone keep n_L exponential in S^{1−o(1)});
GRH-effective Chebotarev needs √p to beat error terms of size
n_L·(polylog-discriminant data + log p) (conductor–discriminant
bookkeeping normalized per degree), hence log p ≳ S^{1+o(1)}, i.e.
S ≤ (log p)^{1−o(1)}.  The unprovable-failure probability through that
range is ∏_{s ≤ S}(1 − c log s/s) ≈ exp(−c(log S)²) ≈
exp(−c'(log log p)²) — the same shape as the campaign's unconditional
Theorem 12.2, and almost-all only.  (All constants here are model-level;
the point is the shape, which no choice of bookkeeping changes: the
compositum degree grows exponentially in S, capping S at a power of
log p, and the failure product then lives at loglog scale.)  Even under
GRH the form-family route reproduces the weakest exceptional-set bound,
not a pointwise statement.

**(d) Sieve positivity (Chen-type switching).**  Chen-type "every large n"
results sift sequences whose target events have per-element probability
≍ 1/log with polynomial sequence length — total sifted mass a positive
power of n, so that available remainder estimates (level-of-distribution
errors, polylog-sized per modulus) sit far below the main term.  Here the
witness mass is polylogarithmic at every scale: the identity-class mass at
modulus cutoff Q is Θ((log Q)³) (Thm 18.2), and per-prime solution counts
are polylog on average (Elsholtz–Tao, *cited from memory — flagged*).
Every known remainder framework (BV-type averages, large-sieve variances)
loses factors that are themselves powers of log — at or above the entire
main term — and no known sieve remainder is o(polylog) at the required
per-p uniformity.  This is an audit of existing remainder technology, not
a universal impossibility for lower-bound sieves; it is the quantitative
reason all bounds here take the shape exp(−(log)^θ): polylog mass
exponentiates to exactly that scale.

**(e) Additive-combinatorial worst-case coverage.**  Davenport/EGZ-type
guarantees need sequence lengths comparable to the group order —
Lemma 17.4.1's mass bound; through the certificate frame this route pays
exponential windows or collapses to congruence families (17.4.3).

### 17.6 Synthesis: the shape of the remaining problem

**The exact residual problem** is Theorem 3.1 with no parameter bound: for
every prime p ≡ 1 (mod 24), *some* q ≡ 3 (mod 4) or m ≡ 3 (mod 4) admits
a divisor witness.  **The natural quantitative target** (sufficient, not
known to be necessary in this strength) is:

> Prove that for every prime p ≡ 1 (mod 24) there exist a ≤ (log p)^{O(1)}
> and a divisor b of p + a with cofactor (p + a)/b ≡ −1 (mod 4a) — or the
> Case-A mirror, or the k ≥ 2 extension (17.3).  The polylog range is the
> heuristic scale at which the witness mass (17.4) reaches any prescribed
> power of log p; the data (§19: w* ≤ 59 through 10⁸) suggest the truth is
> far stronger.

**Features of any proof within the divisor-coset frame** (assessment — this
is the frame every known equivalent formulation lives in, §10.4/§10.6, but
the list is not a classification of all conceivable proofs):

* **(P1)** unboundedly many moduli, range growing with p — finite systems
  of every shape formalized here, (a)–(e), are escaped forever
  (Thm 17.3/Cor 17.3.1; Schinzel's cited theorem for all polynomial
  families);
* **(P2)** per-modulus coverage from *distributional* facts about actual
  factorizations of shifted values — worst-case combinatorics costs
  exponential windows (17.4.1/17.4.3, with 17.4.2's admissibility proviso
  for the pinned corner), and the character layer is inert (Lemma 17.2)
  with average-case-only equidistribution above it (17.4.4);
* **(P3)** distributional inputs with an *empty* exceptional set — for
  which each audited technology (17.5 a–e) lacks its structural
  prerequisite here (no cusp positivity and polylog mains; no L-function
  family with repulsion; compositum-limited Chebotarev; polylog sieve
  mass; exponential coverage cost);
* **(P4)** or a structure source outside the frame.  The one formally
  unexplored slot visible from the parametrization: a *transfer/induction
  between different primes* — by (17.1), (a, b, c, k) → (a, b, c ± 1, k)
  moves solutions between p and p' = p ± 4ab, i.e. transfers witnesses
  along the progression p' ≡ p (mod 4ab); this is exactly the mechanism
  behind the shape-(e) classes, so the naive transfer lands back in the
  harvested class supply.  The three obvious minimal-counterexample
  routes are executed in §17.7 and yield no known transfer; cleverer
  transfers remain unexcluded, with no candidate mechanism in the mapped
  landscape.

**Status of the named doors after this section.**  The identity/sieve axis
is bracketed: supply exactly cubic (Thm 18.2), realized mass log²X·log K
with the two walls H_kBV/H_PF named precisely (§18.2–18.4); within the
mass/Rankin sieve model the ceiling is exceptional-set exponent 3/4 — that
model, at full strength, still cannot prove the conjecture outright (§18.1
mass-ceiling corollary; whether some non-mass use of the class arrangement
could do better is open, cf. §18's own disclaimer).  The pointwise axis
requires (P1)–(P3) or (P4).  The conjecture is supported by everything
measurable — witness mass (log p)³-scale against a single required hit,
w* ≤ 59 through 10⁸, failure modes classified on the reported samples
(§19.2) — and by the
audit above it sits beyond each currently existing pointwise technology for
an identified structural reason.  What would move the frontier: (i) any
pointwise-uniform equidistribution theorem for divisors of shifted integers
in one moving coset, in any nontrivial range; (ii) the §18.4 inputs — H_PF
for the intrinsic full harvest, or H_kBV together with the restricted form
of H_PF (exceptional set to exp(−(log N)^{3/4}), still not "all p");
(iii) a transfer structure (P4).

### 17.7 The descent audit: the three obvious minimal-counterexample
routes yield no known transfer

Suppose p is the least exceptional prime.  Induction supplies: 4/n is
solvable for every n ≥ 2 having any prime factor < p (Lemma 1.1 lifts
solvability from the factor).  Three descent routes present themselves;
here is each, run to its end.  *(This subsection was rewritten after a
hostile referee round found the first version's shape classification
incomplete and its "no map" claims overreaching.)*

**(1) Power descent.**  Is "4/p² solvable ⟹ 4/p solvable" provable?

**Lemma 17.7.1 (complete valuation-shape classification at p²; proved).**
Let p ≥ 3 be prime, 4/p² = 1/x + 1/y + 1/z, and let (a, b, c) with
a ≥ b ≥ c be the sorted p-valuations of the denominators.  Then p | xyz
(so a ≥ 1), and exactly one of the following holds:

(i) c ≥ 1 (all divisible): dividing all three denominators by p gives a
solution of 4/p — the descending shape;

(ii) c = 0 and a > b: then necessarily a = 2, i.e. the shape is (2, 0, 0)
— which forces p² | 4X − 1 — or (2, 1, 0) — which forces p | 4X − 1 —
where X is the coprime part of the p²-denominator.  Shapes (1, 0, 0),
(1, 1, 0) and (a, b, 0) with a ≥ 3 > b are impossible;

(iii) c = 0 and a = b: then necessarily a ≥ 2, and every shape (a, a, 0),
a ≥ 2, is valuation-consistent, the constraint being v_p(X + Y) = a − 2
for the coprime parts X, Y of the two p-power denominators.

*Proof.*  Write the denominators p^aX, p^bY, p^cZ with p ∤ XYZ and clear:
4p^{a+b+c}XYZ = p²(p^{a+b}XY + p^{b+c}YZ + p^{a+c}XZ).  With c = 0 the
right side's term valuations are 2+a+b, 2+b, 2+a.  If a > b the minimum
2+b is attained by the single term p^{2+b}YZ, so equality of valuations
forces a + b = 2 + b, i.e. a = 2; then dividing by p^{2+b} leaves, for
b = 0: 4XYZ − YZ = p²X(Y+Z), i.e. YZ(4X−1) = p²X(Y+Z), so p² | 4X − 1;
for b = 1: 4XYZ = p²XY + YZ + pXZ, so p | YZ(4X−1), i.e. p | 4X − 1.
For a = b the two minimal terms can cancel: dividing by p^{2+a} needs
v_p(YZ + XZ) = v_p(Z) + v_p(X+Y) = a − 2, forcing a ≥ 2 with
v_p(X+Y) = a − 2.  For a = b = 1 this is impossible (negative valuation);
shapes (1,0,0), (1,1,0), and a ≥ 3 > b fail as shown.  If c ≥ 1, divide.
∎  (The four fixed-shape substitution reductions are replayed symbolically
in `verify.py (p)`; the (a,a,0) branch gets two numeric valuation
spot-checks there, not a symbolic verification.)

The mixed shapes occur: **4/9 = 1/9 + 1/12 + 1/4** has v₃-shape (2,1,0)
(and indeed 3 | 4·1 − 1).  For mixed-shape solutions the only map the
valuation structure offers — dividing out a common p-power — is
unavailable, so power descent is not derivable by *this* route.  We do
**not** claim no map whatsoever exists: ad-hoc replacements can
accidentally connect solutions of different denominators (from the 4/9
example, replacing 9 by 1 happens to give 4/3 = 1/1 + 1/12 + 1/4), which
is precisely why only general constructions count, and none is known.
(This shape analysis is also exactly why Theorem 3.1 is a prime-only
criterion: composite n admit the mixed shapes.)  For the record, the
one-coprime-denominator shapes carry two-term data in the modulus family
4x − p² — the direct criterion dictionary for p, keyed to 4x − p, does
not apply to them.

**(2) Window irrelevance.**  For q < 3p every Case-B window element
x = (p+q)/4 is < p, so induction grants 4/x solvable; for larger q, and
for most Case-A values z₀ = (pm+1)/4 > p, not even that is guaranteed
(z₀ may be a product of primes all exceeding p).  Either way the grant
supplies no known transfer by itself: p's criterion consults these numbers only through their divisor
residues mod 4x − p resp. m, and solvability of 4/x is a statement about
*x's own* windows, with no bearing on where divisors of x² sit mod
4x − p.  Among the formalized forced-class families (§4, §16.1,
17.3(d)–(e)) no shape converts a solution of 4/x into a witness for p;
nothing beyond those families is classified, but the surface rigidity of
§10.5 (no correspondences, no Vieta moves) removes the known mechanisms
for producing such a conversion.

**(3) Lattice transfer.**  By (17.1), (a, b, c, k) → (a, b, c ± 1, k)
transfers solutions between p and p ± 4ab — the shape-(e) class
structure, already harvested; a transfer that moved p *across* its class
mod 4ab would be a second point-generating structure on the multilinear
variety, and §10.5 rules out every known mechanism for one.  (§20
subsequently executed the full transfer hunt: the complete affine action
including the a- and b-translations (20.6), the composition monoid, and
the corrected cross-slice laws — all classified, none yielding a total
descent; see §20.5.)

**Audit conclusion (assessment).**  These three obvious
minimal-counterexample routes yield no known transfer: solvability
propagates upward through multiplication (Lemma 1.1) and sideways along
harvested class structures, and no general construction linking p's
criterion to the solvability of smaller integers is available.  Cleverer
transfers remain unexcluded — that is exactly the open P4 slot — but the
naive attempts are now executed rather than presumed.  For later nontrivial
transfer laws and the full Type-II tuple orbit, which do not close witness
existence, see §§22–26 and §30.

Numerics: `verify.py (p)` checks (17.1)/(17.2)/(17.3) symbolically, random
Type-II tuples and deterministic Type-I (moving-c) reconstructions, the
p = 29 fixed-(c,k) regression, the 409 witness, parity inertness on samples
(Lemma 17.2), the residue-1 escape of 𝓡(M) for all A ≤ 2000 (M < 8000,
Thm 17.3(c)), the Mahler integral (Lemma 17.4.4, numerically ≈ 0,
informational), the entropy-toy bound of Lemma 17.4.1 (single-generator
reachable count = Σ2a_r + 1 exactly), and the §17.7 shape algebra with the
4/9 = 1/9 + 1/12 + 1/4 example (v₃-shape (2,1,0)).

---

## 18. The full-harvest ceiling: the identity supply is cubic, and what caps the realized mass

This section separates three questions which must not be conflated: the
number of classes supplied by Lemma 16.1 when every auxiliary modulus is
allowed; the amount of that supply which Lemma 16.3 can presently prove in a
prime slice; and the cost of assembling composite-modulus exclusions into an
upper-bound sieve.  The first question has an unconditional sharp answer.  The
other two contain distinct walls.  In particular, a level bound for products
of moduli is not by itself a sieve theorem: common multiplier factors create
correlations which still have to be evaluated.

### 18.1 The unconditional cubic supply

For an integer \(M\equiv3\pmod4\), put \(A=(M+1)/4\), and let
\(\mathscr R(M)\) be the union of all Lemma-16.1 classes modulo \(M\):

    𝓡(M) = {−uv⁻¹ (mod M) : uvw=A for some u,v,w≥1},
    F(M) = |𝓡(M)|.

This definition counts a residue once.  It does not count a choice of a
factorization \(M=k\ell\).  That distinction is essential below.

**Lemma 18.1 (exact divisor description and honest deduplication; proved).**
For every \(M\equiv3\pmod4\),

    𝓡(M) = {−4D (mod M) : D | A²},                            (18.1)
    (τ(A²)−1)/2 ≤ F(M) ≤ τ(A²).                              (18.2)

The lower-bound classes can be taken to be the divisors \(D<A\), and those
classes are pairwise distinct.

*Proof.*  A factorization \(A=uvw\) gives \(D=u^2w\mid A^2\), and, because
\(4A\equiv1\pmod M\),

    −uv⁻¹ ≡ −u²w A⁻¹ ≡ −4u²w = −4D (mod M).

Conversely, write \(A=\prod p^{e_p}\) and \(D=\prod p^{d_p}\), with
\(0\le d_p\le2e_p\).  At each prime put

    ord_p(u)=⌊d_p/2⌋,   ord_p(w)=d_p−2⌊d_p/2⌋,
    ord_p(v)=e_p−ord_p(u)−ord_p(w).

The last exponent is nonnegative, and these choices give \(uvw=A\) and
\(u^2w=D\).  This proves (18.1), hence the upper bound in (18.2).
The involution \(D\mapsto A^2/D\) on the divisors of \(A^2\) has the unique
fixed point \(A\), so exactly \((\tau(A^2)-1)/2\) divisors satisfy \(D<A\).
For two such divisors, \(0<4D<M\); therefore their residues \(-4D\pmod M\)
are distinct. ∎

This also disposes of the cross-\(k\) counting issue at full harvest.  The
class set is intrinsic to \(M\).  If the same \(M\) is written as
\(k\ell=k'\ell'\), both descriptions produce the same set (18.1), and the
union is taken once.  Lemma 16.3's cross-\(k\) argument concerns a different
operation: it fixes one prime \(\ell\), varies the genuinely different moduli
\(k\ell\), and then projects their classes modulo \(\ell\) after fixing a
subsequence.

**Theorem 18.2 (full-harvest supply is exactly cubic; proved).**  As
\(Q\to\infty\),

    Σ_{M≤Q, M≡3 (4)} F(M)/M ≍ (log Q)³.                       (18.3)

More precisely, with \(\zeta(2)=\pi^2/6\),

    (1/(48ζ(2))+o(1))(log Q)³
      ≤ Σ_{M≤Q, M≡3 (4)} F(M)/M
      ≤ (1/(24ζ(2))+o(1))(log Q)³.                            (18.4)

Thus the complete Lemma-16.1 identity family has class-mass exponent
\(B=3\), neither \(B=2\) nor \(B>3\).

*Proof.*  The elementary Euler identity

    Σ_{n≥1} τ(n²)n^(−s) = ζ(s)³/ζ(2s)                       (18.5)

follows at a prime from
\(\sum_{e\ge0}(2e+1)z^e=(1-z^2)/(1-z)^3\).  For completeness, its
coefficient form is

    τ(n²) = Σ_{d²|n} μ(d) τ₃(n/d²).

The usual three-dimensional hyperbola calculation gives

    Σ_{m≤x} τ₃(m) = (1/2)x(log x)² + O(x log x).

Substitution in the coefficient identity (the \(d\)-sum is absolutely
convergent after division by \(d^2\)) gives

    Σ_{n≤x} τ(n²) = x(log x)²/(2ζ(2)) + O(x log x).           (18.6)

Partial summation now yields

    Σ_{n≤x} τ(n²)/n = (log x)³/(6ζ(2)) + O((log x)²).         (18.7)

Write \(M=4A-1\).  Since
\(1/(4A-1)=1/(4A)+O(A^{-2})\), the total contribution of the error is
bounded (use \(\tau(A^2)\ll_\epsilon A^\epsilon\)).  Apply the lower and
upper halves of (18.2) in (18.7); the subtracted \(1\) in the lower bound
contributes only \(O(\log Q)\).  This gives (18.4), hence (18.3). ∎

**Deduplication warning (proved, not notation).**  The literal double sum

    Σ_k Σ_ℓ F(kℓ)/(kℓ)                                      (18.8)

is *not equivalent* to (18.3) unless the pairs \((k,\ell)\) are first
quotiented by their product.  If \(\ell\) ranges over all integers, every
\(M\) is repeated once per admissible divisor.  If \(\ell\) is required to
be prime, some \(M\)'s are omitted and others are repeated once per
admissible prime divisor.  For example
\(231=77\cdot3=33\cdot7=21\cdot11\), and all three decompositions give the
same set (18.1).  No asymptotic for the raw repeated sum (18.8) is needed or
claimed.  The theorem answers the structural supply question for distinct
moduli and distinct classes.

**Mass-ceiling corollary (proved within the mass/Rankin sieve model).**  In a
PW-style argument with auxiliary scale \(X=e^t\), a class family of total
mass \(O(t^B)\) has Rankin-tail balance

    t^B ≲ log N/t.

Its saving is therefore at most
\(O((\log N)^{B/(B+1)})\).  Theorem 18.2 gives \(B=3\), hence \(3/4\), for
the entire Lemma-16.1 family.  This is an absolute ceiling for sieves whose
only gain is the summed identity-class mass and whose product tail is
controlled in this way.  It is not a nonexistence theorem for every possible
use of the arithmetic arrangement of the classes.

### 18.2 Which wall binds in Theorem 16.4?

Put

    L=log N,   t=log X,   r=log K.

Lemma 16.3 supplies mass

    μ ≍ t² r.                                                   (18.9)

The Rankin step (16.14) requires \(t\mu\ll L\), so

    t³r ≲ L,   μ ≲ L^(2/3) r^(1/3).                            (18.10)

These two lines account for the exponent and its logarithmic factor.

**Assessment 18.3(a) (partition cost is not the scale-binding wall; proved
arithmetic).**  The partition uses
\(M_0=24L_K=\exp(K(1+o(1)))\) (sharp constant \(\log L_K\sim2K/3\), see §34, loosening this to \(K\le\tfrac32(1-\epsilon)L\)), hence only requires \(K\le(1-\epsilon)L\)
if each subsequence is to have polynomial length.  One may instead take, for
example, \(K=L^{1/2}\): then \(K=o(L)\), while
\(r=(1/2)\log L\), and (18.10) still gives

    μ ≍ L^(2/3)(log L)^(1/3).

Thus the partition changes constants, not the displayed scale.  At the
choice \(K=\delta L\) made in Theorem 16.4 it consumes a fixed fraction of
\(L\), but the optimizing value
\(t\asymp(L/\log L)^{1/3}\) is set by (16.14), not by the condition
\(M_0<N\).

**Assessment 18.3(b) (the proved prime-slice wall is the summed
Bombieri--Vinogradov multiplicity).**  In Lemma 16.3, a modulus
\(q=4uv\) is generated by at most

    W(q) ≤ K·2^ω(uv) ≤ K(log X)^(D log 2).                    (18.11)

The proof bounds every corresponding progression error by
\(W(q)\max_a|E(x;q,a)|\) and then invokes Bombieri--Vinogradov.  Arbitrarily
large fixed logarithmic powers can be absorbed by asking for a larger
Bombieri--Vinogradov saving, but a factor \(K=X^\delta\) cannot.  This is the
precise reason for the existing hypothesis \(K\le(\log X)^5\); the exponent
5 is inessential, while “a fixed power of \(\log X\)” is essential to that
proof.

A direct Barban--Davenport--Halberstam/Cauchy--Schwarz replacement does not
repair this.  In one dyadic interval the box has \(z=x^{1/6}\), so the number
of triples is

    T ≪ x^(1/3)h(𝒥)·(log x)^O(1),

and \(\sum m(q,a)^2\le(\max m)T\), with
\(\max m\le K(\log x)^{O(1)}\).  At the small modulus level
\(q\le Q_0=x^{1/3}\), the available unconditional large-sieve
second-moment bound is of size \(x^2(\log x)^{O(1)}\), not the conjectural
small-level BDH size \(xQ_0(\log x)^{O(1)}\).  Cauchy--Schwarz therefore
gives an error of order

    x^(7/6) K^(1/2)(log x)^O(1),                              (18.12)

against a main term \(\asymp x\log x\,h(\mathcal J)\); it loses even before
\(K\) grows.  A hypothetical variance bound of size \(xQ_0\) would instead
give \(x^{5/6}K^{1/2}\) up to logarithms and would permit a small power of
\(x\).  Such a bound in this small-\(q\), residue-varying weighted setting is
not the standard BDH theorem.

For reference, the deliberately large floor \(H=K^{10}\) is not the
logarithmic wall: the proof of Lemma 16.2 continues verbatim whenever
\(z>H^2=K^{20}\).  If the prime-progression error were available for
\(K=X^\kappa\), the lowest dyadic interval in Lemma 16.3 would only require,
with its current wasteful constants, \(\kappa<1/240\).  Any fixed positive
\(\kappa\) already makes \(r\asymp t\), which is all the cubic scale needs.

**Elliott--Halberstam check (negative).**  Ordinary Elliott--Halberstam
replaces the range of the Bombieri--Vinogradov sum over \(q\); it does not
remove the multiplicity (18.11).  Here \(q\le x^{1/3}\) is already inside
the Bombieri--Vinogradov range.  Bounding the weighted sum by
\(K(\log x)^{O(1)}\sum_q\max_a|E(q,a)|\) still loses \(K\).  Thus ordinary
Elliott--Halberstam buys at most room in constants here, not the missing
\(k\)-aspect and not the exponent \(3/4\).

### 18.3 Partition-free assembly: the honest optimization

Consider the proposed integer-side Selberg/\(\Lambda^2\) assembly as a model.
Suppose it can use mass \(\mu\asymp t^2r\), and that truncating its Euler or
Selberg expansion requires degree

    J ≍ μ.                                                       (18.13)

For a term containing moduli \(k_i\ell_i\), \(i\le J\),

    lcm(k_iℓ_i:i≤J)
       ≤ lcm(k_i:i≤J)·∏ℓ_i
       ≤ min(L_K,K^J)X^J.                                     (18.14)

Consequently exact integer counting to square-root level has the honest
logarithmic budget

    min(K,Jr)+Jt ≲ L.                                         (18.15)

Using only \(L_K\le\exp(K(1+o(1)))\) (sharp: \(\exp(\tfrac23K(1+o(1)))\), §34) gives the coarser budget
\(K+Jt\lesssim L\).  The sharper \(K^J\) alternative in (18.14) matters
when \(K\) is large; it is still only a level calculation, not an evaluation
of correlated intersections.

**Assessment 18.4 (optimization under the stated assembly model; proved
arithmetic).**

* If \(K\) is at most a fixed power of \(L\), then
  \(r=O(\log L)\).  At the optimum \(t\gg r\), (18.13)--(18.15) reduce to
  \(t^3r\lesssim L\), and

      μ ≲ L^(2/3)r^(1/3)
        ≲ L^(2/3)(log L)^(1/3).                               (18.16)

  Thus a partition-free implementation does **not** improve the
  \((\log\log N)^{1/3}\) power in Theorem 16.4 when only
  polylogarithmic \(K\) is available.  A power \(2/3\) on \(\log\log N\)
  in this formula would require
  \(r\asymp(\log L)^2\), already beyond every fixed polylogarithmic range.

* If a genuine \(k\)-aspect estimate permits \(K=X^\kappa\) for fixed
  \(\kappa>0\), then \(r=\kappa t\),
  \(\mu\asymp t^3\), and the sharper form of (18.15) is
  \(J(t+r)\asymp t^4\lesssim L\).  It predicts

      t ≍ L^(1/4),   μ ≍ L^(3/4).                             (18.17)

  This reaches the supply ceiling.  The preliminary choice
  \(K=\exp(L^{1/3})\) is too large for this balance: with \(r\asymp t\)
  it spends order \(L^{4/3}\), not \(L\).  The cubic optimum is
  \(K=\exp(\Theta(L^{1/4}))\).  If one insists on the coarser
  \(e^K\) bound instead of \(K^J\), even that choice is impossible because
  it forces \(K\lesssim L\).

**Assembly gap (named and not proved away).**  Section 14's integer-side
product works because a window prime larger than every shift cannot divide
two different shifted forms; incompatible terms vanish, and the remaining
correction is second-order.  Composite moduli \(k\ell\) have the opposite
feature: different conditions deliberately share factors of their
multipliers, and a compatible intersection has density
\(1/\operatorname{lcm}(k_i\ell_i)\), which can be much larger than the
product of the individual densities.  Equations (18.14)--(18.17) control the
rounding level but do not prove the required mean-value factorization or a
Selberg quadratic-form bound.  No unconditional sharpening of Theorem 16.4
follows from the partition-free calculation alone.

### 18.4 A precise conditional route to the ceiling

The following hypotheses isolate the two missing inputs.  They are stated to
make the implication falsifiable; neither is claimed to be standard.

**Hypothesis H_kBV(κ) (weighted, residue-varying \(k\)-aspect BV).**  Fix some
\(0<\kappa<1/240\).  Uniformly for large \(X\),
\(X^{1/2}\le x\le X\), \(K\le X^\kappa\), every residue \(c\pmod{24L_{\mathcal J}}\)
with \((c,24L_{\mathcal J})=1\), and every subfamily
\(\mathcal J\subseteq\{k\le K:k\equiv1\ (4)\}\) with \(1\in\mathcal J\)
(\(L_{\mathcal J}={\rm lcm}_{k\in\mathcal J}k\), as in Lemma 16.2), put
\(H=K^{10}\), \(z=x^{1/6}\), and

    E(x;q,a)=π(2x;q,a)−π(x;q,a)
             −(li(2x)−li(x))/φ(q).

For the triples in Lemma 16.2 with
\(\omega(uv)\le D\log\log X\), assume

    Σ_{k∈𝒥} Σ* |E(x;4uv,−k⁻¹)|
       = o(x log x·h(𝒥)),                                    (H_kBV)

uniformly (the inverse and residue are modulo \(4uv\)).  This is a bilinear,
weighted progression statement with the \(k\)-aspect absorbed; ordinary BV,
BDH, and Elliott--Halberstam do not state it.

**Hypothesis H_PF (partition-free Selberg assembly for the FULL intrinsic
system; corrected after review).**  Let \(X\ge X_0\), and let the class
system be the **complete** family \(\{\mathscr R(M):M\le X,\
M\equiv3\pmod4\}\) — every class of every modulus, nothing omitted — with
\(\mu=\sum_{M\le X,\,M\equiv3(4)}F(M)/M\asymp(\log X)^3\) (Theorem 18.2).
Suppose: for \(J\ge C\mu\) and \(N\) with \(J\log X\le\tfrac12\log N\),
there is a nonnegative arithmetic majorant \(\nu\) on \([1,N]\), equal to at
least one on every integer avoiding all the classes, with normalized mean
\(N^{-1}\sum_{n\le N}\nu(n)\ll\exp(-c\mu)\), whose evaluation requires only
exact congruence counts modulo lcms of at most \(J\) of the moduli (each
lcm \(\le X^J\le N^{1/2}\), so each count carries \(O(1)\) rounding error,
and, writing T for the number of congruence-count terms in the evaluation
and assuming the coefficient sum is \(\le T\le e^{O(J)}\), the aggregate
rounding error is \(O(e^{O(J)})\ll N\exp(-c\mu)\) by the degree budget).
Constants \(c,C>0\) absolute.

*Scope warning (why the full system is essential).*  The previous draft
quantified over arbitrary finite subfamilies; that version is **false**:
the subfamily of \(D=1\) classes with \(3\mid M\) (\(n\equiv-4\pmod M\)
over \(M\equiv3\pmod{12}\)) has mass \(\asymp\log X\), yet every such class
lies inside \(n\equiv2\pmod3\), so all \(n\not\equiv2\pmod3\) — density
\(2/3\) — avoid the whole subfamily, and no majorant can have mean
\(\exp(-c\mu)\to0\).  (Even the full \(D=1\) family over all
\(M\equiv3\pmod4\) has avoider density \(\asymp(\log X)^{-1/2}\) — the
\(n+4\) free of divisors \(\equiv3\pmod4\) up to \(X\) — far above
\(\exp(-c\,\mathrm{mass})\).)  Heavy cross-\(M\) correlations are real.  H_PF is precisely the assertion that the
**complete** system's CRT spread defeats such correlations at cubic scale;
it is a genuinely open correlation hypothesis, not a standard fundamental
lemma, and — unlike the subfamily version — no counterexample is known.
(H_PF as stated is refuted — see §31; the critical-window variant
\(H_{\rm PF}'\) below remains open.)
A *restricted variant* H_PF(\(k\ell\)) asserts the same for the complete
multiplier system \(\{k\ell\le X\cdot K\}\) of §16 with lcm bound (18.14);
it is what pairs with H_kBV below.

**Lemma 18.5 (conditional cubic prime-slice mass).**  Under
H_kBV(\(\kappa\)), Lemma 16.3 extends to \(K=X^\kappa\), and for the full
\(\mathcal J\), pointwise in every reduced compatible \(c\),

    Σ_{X^(1/2)<ℓ≤X} f_c(ℓ)/ℓ ≍ (log X)³.                     (18.18)

*Proof.*  The box and Shiu estimates in Lemma 16.2 need only
\(z>K^{20}\), which follows in the lowest dyadic interval from
\(\kappa<1/240\).  Distinctness is unchanged because
\(uv>H^2>K\).  In Lemma 16.3 replace the multiplicity-times-BV error by
H_kBV.  It is negligible beside (16.10).  The upper bound still follows
from Brun--Titchmarsh and (16.3).  Finally
\(h(\mathcal K(K))\asymp\log K\asymp\log X\), giving (18.18). ∎

**Theorem 18.6 (conditional full-harvest bound).**  Under H_PF there is
\(c>0\) such that

    E_all(N) ≤ N exp(−c(log N)^(3/4)),                        (18.19)

and hence the same bound holds for prime denominators.

*Proof.*  Put \(L=\log N\), choose
\(t=\alpha L^{1/4}\), and \(X=e^t\).  Use once each of the intrinsic
classes (18.1) for every \(M\le X\), \(M\equiv3\pmod4\).  Theorem 18.2 gives
\(\mu\asymp t^3\).  Take \(J=C\mu\).  The lcm of any \(J\) selected moduli
is at most their product, hence at most \(X^J\), whose logarithm is

    J log X ≪ t³·t = α⁴L.

Choose \(\alpha\) small enough that this is at most \(L/2\).  H_PF then
bounds the avoiders by \(N\exp(-c\mu)\), which is (18.19).  Every exceptional
denominator is an avoider by Lemma 16.1. ∎

Theorem 18.6 is **CONDITIONAL on the nonstandard H_PF hypothesis**.  It uses
the intrinsic all-\(M\) supply, so it bypasses prime-slice harvesting and does
not need H_kBV.  If one insists on realizing the same cubic mass through the
restricted prime factors \(M=k\ell\), then Lemma 18.5 shows that H_kBV plus
the restricted variant H_PF(\(k\ell\)) gives the same calculation via
(18.14).  H_kBV is therefore the prime-slice harvesting wall; H_PF is the
composite-modulus assembly wall, and the latter is the sole wall for the
literal full harvest of Theorem 18.2.  Ordinary Elliott--Halberstam does not
imply H_kBV, and no level estimate alone implies H_PF.  Unconditionally,
Theorem 18.2 proves that cubic supply exists and that a mass-driven exponent
beyond \(3/4\) cannot come from Lemma 16.1, but Theorem 16.4 remains the
realized bound.  (H_PF as stated is refuted — see §31; the critical-window
variant \(H_{\rm PF}'\) below remains open.)

**Wave-13 supersession note (appended; CLAIMED/PROVISIONAL).**  Section 39
replaces H_PF by a fixed c-free restricted family and pays the honest
\(e^{O(J\log X)}\) ledger inside the critical window.  If its provisional
proof survives review, Theorem 39.7 makes (18.19) unconditional; the literal
H_PF and \(H_{\rm PF}'\) statements remain false/open exactly as printed.

**Numerical companion.**  `verify.py (q)` computes the exact union (18.1) for
every \(M\le10^5\), reports its harmonic truncations against \((\log Q)^3\),
checks the canonical half and the bounds (18.2), exhibits the threefold
cross-decomposition duplicate at \(M=231\), and checks the two level-balance
arithmetics (18.16)--(18.17).  The fitted finite-range exponent is labeled
informational; none of these computations is used as proof.

---

## 19. Computational frontier: witness-record growth to large scale, failure taxonomy, and the Type-II dictionary

Everything in this section is a finite computation, not an asymptotic result.
The search domain was **every prime** \(p<10^8\) with \(p\equiv1\pmod {24}\):
719,781 primes, ending at 99,999,721.  At each
\(w=3,7,11,\ldots\), both \(x=(p+w)/4\) and \(z_0=(pw+1)/4\) were factored;
the exact residues of divisors of their squares were tested against \(-n\pmod
w\).  A recursion enumerated divisor residues below \(\tau(n^2)=10^6\), with
a bounded subset-product residue DP above that cap (the cap was not reached in
this range).  A 100,595-hard-prime pilot through 12.3 million ran at 229,868
primes/second with 12 workers; the final scan ran at 211,045 primes/second
(2.79 s sieving plus 3.41 s witness search).  Thus the requested \(10^8\)
frontier was inexpensive on this machine; timings are calibration, not part of
the mathematical data.

### 19.1 Record growth through \(10^8\)

The strict running records for the interleaved minimum \(w^*(p)\) are

| record prime \(p\) | \(w^*(p)\) |
|---:|---:|
| 73 | 3 |
| 241 | 7 |
| 2,521 | 15 |
| 21,169 | 31 |
| 118,801 | 59 |

Here “record” means strictly larger than every earlier value in this scan.
This corrects a terminology ambiguity in §11.1: 11 and 23 are attained (first
at 3,049 and 26,161), but are not running records because 15 and 31,
respectively, occurred earlier.  The complete histogram is

| \(w^*\) | 3 | 7 | 11 | 15 | 19 | 23 | 27 | 31 | 35 | 39 | 47 | 59 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| count | 622,065 | 83,809 | 10,610 | 1,873 | 890 | 387 | 61 | 74 | 3 | 6 | 2 | 1 |

The Case-B-only hard-slice record extension is

| \(p\) | 3 | 5 | 73 | 1,129 | 1,201 | 21,169 | 67,369 | 87,481 | 1,430,641 | 8,803,369 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| minimal \(q\) | 1 | 3 | 7 | 11 | 23 | 31 | 35 | 63 | 71 | 107 |

The first two entries are the exact pre-hard baseline.  Entries thereafter are
records among the scanned \(p\equiv1\pmod {24}\) primes; the first eight agree
with §8.3's all-prime scan through \(4\cdot10^5\), but non-hard residue classes
were not rescanned to \(10^8\).

There are only five interleaved record jumps.  The purely descriptive fit
\(w=C(\log p)^\alpha\) to those jumps gives \(\alpha=2.832\) and \(C=0.0500\),
while the endpoint ratio is \(59/\log(10^8)=3.203\).  These numbers are not a
credible asymptotic exponent estimate: the maximum first reached 59 at
118,801 and then did not move over almost three further decades.  The data are
compatible with \(c\log p\), with the broader \((\log p)^{1+o(1)}\) scale or
another log-power, and with slower growth; they do not discriminate among
them.  The increase 31 to 59 does not
contradict §8.3's unbounded log-power prediction, but a finite plateau cannot
support unboundedness either.

### 19.2 Failure-mode taxonomy

For every failed pair below \(w^*\), let \(R\) be the exact bounded-exponent
residue set, \(H\) the subgroup generated without exponent caps by the prime
factors of \(n\), and \(t=-n\pmod w\).  The implementation checked independently
that \(t\in R\) is equivalent to the literal divisor witness test for every
classified pair.  The classes were made exclusive in the order F0
(gcd-degenerate), F1 (Jacobi), F2 (non-Jacobi subgroup miss), F3 (\(t\in H\)
but \(t\notin R\)), F4 (logical catch-all).  No F0 or F4 case occurred.

A fixed-seed, scale-stratified sample of 2,000 scanned primes (273, 400, 500,
827 from the four displayed scales) produced 784 failed half-pairs below
\(w^*\):

| population | pairs | F1 Jacobi | F2 subgroup | F3 box |
|---|---:|---:|---:|---:|
| random sample, both halves | 784 | 778 (99.23%) | 0 | 6 (0.77%) |
| sample, Case B only | 392 | 387 (98.72%) | 0 | 5 (1.28%) |
| sample, Case A only | 392 | 391 (99.74%) | 0 | 1 (0.26%) |
| five running-record primes | 50 | 38 (76.0%) | 1 (2.0%) | 11 (22.0%) |

By modulus in the random sample:

| \(w\) | pairs | F1 | F2 | F3 |
|---:|---:|---:|---:|---:|
| 3 | 650 | 650 | 0 | 0 |
| 7 | 92 | 92 | 0 | 0 |
| 11 | 14 | 12 | 0 | 2 |
| 15 | 14 | 14 | 0 | 0 |
| 19 | 10 | 7 | 0 | 3 |
| 23 | 2 | 2 | 0 | 0 |
| 27 | 2 | 1 | 0 | 1 |

By prime scale, F1 was 138/138 below \(10^5\), 193/196 (98.47%) on
\([10^5,10^6)\), 189/192 (98.44%) on \([10^6,10^7)\), and 258/258 on
\([10^7,10^8)\).  These are failure-pair counts, not counts of sampled primes,
and the last two 100% observations have limited denominator.  The 98.72%
Case-B figure is higher than §6's 92.9%, but the populations differ: §6 used
six classes modulo 840 and all Case-B failures below the Case-B minimum,
whereas this experiment uses \(p\equiv1\pmod {24}\) and stops at the
interleaved minimum.  It is therefore not evidence of a trend in the
percentage.  It does show that Jacobi remains dominant at large scale in this
conditioned population.  F3, the finite exponent box, carries every non-F1
random failure.  The only measured F2 case was the Case-B pair \((p,w)=
(118801,51)\); selection for record primes strongly enriches F3.

### 19.3 Type-II dictionary

For 10,000 fixed-seed random positive triples \((g,u,v)\), setting

\[
 p=4guv-u-v,\qquad q=u+v,\qquad x=guv,\qquad d=u^2g
\]

gave \(d\mid x^2\), \(q\mid d+x\), and Theorem 3.1(B)'s reconstruction
exactly returned

\[
 (x,p(x+d)/q,p(x+x^2/d)/q)=(guv,pgu,pgv).
\]

For the four-parameter direction, **all 36,384 Case-B witnesses** with
\(q\le63\) for all 1,181 primes \(p<10^5\), \(p\equiv1\pmod {24}\), were
checked (all admissible divisors \(d\), not merely the first witness).  With
\(g_0=(d,x)\), every one produced integers

\[
 a=d/g_0,\qquad c=g_0/a,\qquad b=x/(ac),\qquad k=(a+b)/q
\]

with \((a,b)=1\), \(d=a^2c\), \(x=abc\), and

\[
                 kp=4abck-a-b.                              \tag{19.1}
\]

There were zero integrality, coprimality, or identity failures.  Thus the
four-parameter form is complete on this finite witness set; this is not a
proof of criterion completeness beyond the already algebraic valuation
argument.  On the same 36,384 rows,

\[
       (4ack-1)(4bck-1)=4pck^2+1                            \tag{19.2}
\]

held exactly.  Conversely, a divisor \(D\equiv-1\pmod {4ck}\) of the
right-hand side makes both factors of this form.  The computation therefore
supports the exact dictionary

\[
 \text{Case B}\quad\Longleftrightarrow\quad
 \exists c,k:\ 4pck^2+1\text{ has a divisor }-1\pmod {4ck}.
\]

Finally, an exhaustive \(k=1\) search was made for the same 1,181 primes.  It
is enough to search \(c\le\lfloor(p+2)/4\rfloor\), since (19.1) gives
\(c=(p+a+b)/(4ab)\).  A \(k=1\) witness exists for 1,175 primes.  Their
\(c_{\min}\) has median 2, 90th percentile 4, 99th percentile 20, and maximum
557.  The exact nonzero distribution is

    1:579, 2:376, 3:88, 4:30, 5:39, 6:19, 7:2, 8:12, 9:3,
    10:1, 11:5, 12:2, 14:3, 15:1, 16:1, 18:1, 20:2, 21:1,
    23:1, 30:2, 35:1, 38:1, 45:1, 131:1, 149:1, 251:1, 557:1.

The six primes 409, 577, 5,569, 9,601, 23,929, and 83,449 have **no** \(k=1\)
witness at all (hence none with \(c\le10^4\)); their Case-B solutions require
\(k\ge2\).  Section 28.3 extends this exact census through \(10^6\).  Grouped
by Case-B minimal \(q\), the primes having a \(k=1\) witness give:

| minimal \(q\) | count | min \(c_{\min}\) | median | max |
|---:|---:|---:|---:|---:|
| 3 | 574 | 1 | 1 | 557 |
| 7 | 472 | 1 | 2 | 45 |
| 11 | 79 | 1 | 2 | 149 |
| 15 | 13 | 1 | 1 | 5 |
| 19 | 13 | 1 | 2 | 6 |
| 23 | 17 | 1 | 2 | 30 |
| 31 | 5 | 1 | 2 | 5 |
| 35 | 1 | 1 | 1 | 1 |
| 63 | 1 | 8 | 8 | 8 |

`recorddata.json` contains the full histograms, taxonomy counts, all 1,181
\((p,q_{\min},c_{\min})\) rows, timings, and 20 replay witnesses.
`frontier_compute.py` reproduces the scan.  `verify.py (r)` independently
replays 100 F1 triples, the 20 stored decompositions, (19.2) symbolically, and
ten original record-table entries.

### 19.4 Extension past \(10^8\) and the F3 microscope

The extension used a segmented sieve on \(p=24k+1\) in blocks of width
\(10^8\), retaining only aggregate counts.  A pilot on
\([10^8,2\cdot10^8)\) processed 664,109 primes at 170,260 primes per
scan-second with 82.7 MiB peak memory; before the full run this projected about 5.5
minutes to \(10^{10}\).  The measured rate fell as the factored integers grew.
The full witness search took 635.25 s, in addition to 14.49 s for sieving, at
an aggregate 88,401 primes per witness-search second.

Every prime \(p\equiv1\pmod {24}\) in \([10^8,10^{10})\) was scanned:
56,156,819 primes, ending at 9,999,999,817.  Together with §19.1 this is
56,876,600 primes below \(10^{10}\).  There was one new strict record,

| record prime \(p\) | \(w^*(p)\) |
|---:|---:|
| 2,927,257,369 | 71 |

so the 59 plateau does **not** survive to \(10^{10}\); it lasts from 118,801
to this prime, and the running maximum then remains 71 through the scan bound.
The cumulative nonzero histogram tail is

| \(w^*\) | 35 | 39 | 43 | 47 | 51 | 55 | 59 | 71 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| count | 198 | 100 | 16 | 51 | 4 | 4 | 1 | 1 |

For the microscope, a fixed-seed sample took 800 random hard primes from each
decade \([10^j,10^{j+1})\), \(j=4,\ldots,9\), then included all 147 primes
with \(w^*\ge27\) found by a dedicated rescan from \(10^4\) to \(10^8\)
(record data imply none below \(10^4\)), and
all six record primes.  After overlaps this gave 4,948 primes (sample maximum
9,990,035,233).  Every half-pair strictly below its \(w^*\) was classified:

| population | pairs | F1 Jacobi | F2 subgroup | F3 exponent box |
|---|---:|---:|---:|---:|
| stratified + enriched sample | 3,830 | 3,590 (93.73%) | 1 (0.03%) | 239 (6.24%) |
| Case B | 1,915 | 1,786 | 1 | 128 |
| Case A | 1,915 | 1,804 | 0 | 111 |

The enrichment deliberately raises the F3 fraction, so 6.24% is not an
estimate for unconditioned hard primes.  Exact min-plus residue DP gave the
following cap deficit \(\min\sum_i\max(0,e_i-2v_i(n))\):

| deficit | 1 | 2 | 3 | 7 | 8 | 20 |
|---:|---:|---:|---:|---:|---:|---:|
| F3 cases | 164 | 46 | 19 | 5 | 4 | 1 |
| fraction | 68.62% | 19.25% | 7.95% | 2.09% | 1.67% | 0.42% |

Under the stored canonical optimizer (lexicographically first optimal
exponent vector), 162 of the 164 deficit-one cases had a binding factor with
\(v_i(n)=1\) needing exponent 3 rather than the cap 2; the other two had
\(v_i(n)=2\) needing 5 rather than 4.  (Across *all* optimal choices the
choice-invariant split is: 159 cases admit only valuation-1 carriers, two
only valuation-2, and three admit mixed choices.)  Of those 164 cases, 98 allowed more than one
prime to carry an optimal one-unit excess.  Among the 66 with a unique carrier,
that carrier was the smallest factor in 44 cases, the largest in 16, and an
interior factor in 6.  Across all 239 cases the corresponding counts were 120
ambiguous, 69 uniquely smallest, 42 uniquely largest, and 8 uniquely interior.
The largest deficit was 20 at the new record's Case-B pair \((w,n)=(43,
731814353)\): \(n\) is prime and the least exponent reaching the target is 22
against cap 2.  Full factorizations, targets, canonical optimal exponents, and
all optimal carrier sets for every F3 row are stored in `recorddata.json`.

For a modulus-matched comparison, both halves of every sampled prime were
measured at each F3-bearing modulus
\(11,19,23,27,31,35,39,43,47,59\):

| class | pairs | mean \(\omega(n)\) | median \(\omega(n)\) | squarefree |
|---|---:|---:|---:|---:|
| F1 | 36,434 | 2.601 | 3 | 23,064 (63.30%) |
| F3 | 21,826 | 2.724 | 3 | 17,785 (81.49%) |
| success | 40,700 | 3.904 | 4 | 18,988 (46.65%) |

**Interpretation.**  F3 is measured to be strongly concentrated on
squarefree inputs, and its median of three distinct factors is below the
success median of four.  It does not have smaller \(\omega\) than F1 in the
modulus-matched controls, so “few distinct factors” alone does not separate
the two failure modes; missing multiplicity is the clearer signal.  A
one-unit shortage is the majority pattern, usually a prime factor of
squarefree \(n\) needing exponent 3, but 75 of 239 cases need more and the
observed deficit reaches 20.
The carrier is often non-unique and, when unique, is more often the smallest
than the largest factor, so the data reject an “always the largest factor”
rule while retaining a real squarefree/exponent-scarcity pattern.

`frontier_extension.py` reproduces the segmented extension and microscope.
`verify.py (r)` additionally recomputes the new record and replays three stored
F3 deficit rows exactly.

---

### References (partly from memory — flagged)

* Obláth 1950 (first appearance in print; conjecture attributed to Erdős).
* L. J. Mordell, *Diophantine Equations*, 1969, ch. 30 (mod-840 covering).
* D. G. Terzi 1971 (extension mod 120120). *(from problem page)*
* R. C. Vaughan, "On a problem of Erdős, Straus and Schinzel", *Mathematika*
  17 (1970), 193–198, DOI 10.1112/S0025579300002886. *(Primary PDF remained
  access-blocked; method checked through Pomerance–Weingartner §4.)*
* C. Pomerance, A. Weingartner, "Exceptions to the Erdős–Straus–Schinzel
  conjecture" (2025), arXiv:2511.16817, especially Theorem 1.3 and §4.
* H. L. Montgomery, R. C. Vaughan-style analytic large sieve: see e.g.
  H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53
  (2004), Thm 7.11 (the ∑*_{a(q)}|∑ a_n e(an/q)|² ≤ (N+Q²)∑|a_n|² form
  used in Lemma 12.1). *(standard; citation from memory, not re-checked
  against a copy — flagged)*
* Siegel–Walfisz theorem (used in (12.9) and (13.4) via partial
  summation): any standard reference, e.g. Iwaniec–Kowalski §5.9.
  *(classical; from memory — flagged)*
* M. Nair, G. Tenenbaum, "Short sums of certain arithmetic functions",
  *Acta Math.* 180 (1998), 119–144, Theorem 1.
* P. Shiu, "A Brun–Titchmarsh theorem for multiplicative functions",
  *J. Reine Angew. Math.* 313 (1980), 161–170, Theorem 1.
* A. Schinzel — quadratic-residue obstruction to polynomial identities.
  *(attribution from memory; also treated in Mordell's book)*
* C. Elsholtz, T. Tao, "Counting the number of solutions to the Erdős–Straus
  equation on unit fractions", J. Aust. Math. Soc. (2013). *(venue from memory)*
* M. Bright, D. Loughran, no Brauer–Manin obstruction (2020).
* T. Bloom, C. Elsholtz (2022), Thm 1: divisor-condition equivalence.
* Salez 2014: verification to 10^17; [MiDu25] further. *(from problem page)*
* erdosproblems.com/242 (accessed 2026-08-16, status: Open).

## 20. Frontal assault log

This section records a direct attempt at the full conjecture, with the
prime-to-prime transfer slot attacked first.  Throughout, a **witness at \((c,k)\)** means a Type-II factorization from Theorem 17.1(iii).  Put

\[
 h=4ck,\qquad L=hk=4ck^2,\qquad N_{c,k}(p)=1+Lp.
\]

Thus a witness at \((c,k)\) is exactly

\[
 N_{c,k}(p)=DE,\qquad D,E>0,\qquad D\equiv E\equiv-1\pmod h.       \tag{20.1}
\]

The key identities and finite computations of this section are replayed in
`verify.py (s)` (algebraic replays plus finite enumerations; hypotheses
such as positivity are checked on the enumerated instances, not proved by
the replay).

### 20.1 Composition/transfer hunt

#### The fixed-\((c,k)\) multiplication law

**Lemma 20.1 (proved: the exact composition monoid).**  On nonnegative
integers define

\[
        u\circ_L v=u+v+Luv.
\]

This is a commutative associative monoid with identity zero, and

\[
        N_{c,k}(u\circ_Lv)=N_{c,k}(u)N_{c,k}(v).                \tag{20.2}
\]

If \(u\) has a witness at \((c,k)\), then \(u\circ_Lv\) has one for every
\(v\geq0\), whether or not \(v\) is soluble.  More explicitly, if
\(N(u)=(ha-1)(hb-1)\), then

\[
 \begin{aligned}
 u'&=u\circ_Lv=u+vN(u),\\
 a'&=a,\qquad b'=b+kv(hb-1),
 \end{aligned}                                                   \tag{20.3}
\]

is a witness for \(u'\).

*Proof.*  Equation (20.2) is expansion.  The old factor \(D=ha-1\)
continues to divide \(N(u)N(v)\) and is still \(-1\pmod h\); its new
cofactor is

\[
 (hb-1)N(v)=h\{b+kv(hb-1)\}-1.
\]

This proves (20.3), and associativity follows either by expansion or by the
injective map \(u\mapsto N(u)\) into multiplication. ∎

This gives a genuine transfer across primes, but only along an already
harvested progression.  Since \((u,N(u))=1\), Dirichlet's theorem supplies
infinitely many primes in \(u+N(u)\mathbb Z_{\geq0}\), and every one is
soluble by (20.3).  For odd \(u\), a prime output necessarily has even
\(v\).  In particular, composing **two odd primes** at the same \((c,k)\)
can never produce a new prime: \(u\circ_Lv\) is even and greater than two.
This parity obstruction was absent from the initial semigroup suggestion.

**Lemma 20.2 (proved: divisor-set algebra and the wrong sign).**  For an
integer \(n\) coprime to \(h\), let

\[
       \Delta_h(n)=\{d\bmod h:d\mid n\}.
\]

Then \(\Delta_h(n_1n_2)=\Delta_h(n_1)\Delta_h(n_2)\), including when
\(n_1,n_2\) are not coprime.  Consequently, inside the ambient monoid
\(\mathcal M_L=\{n\ge1:n\equiv1\pmod L\}\), the set

\[
 \mathcal S_h=\{n\in\mathcal M_L:-1\in\Delta_h(n)\}
\]

is a multiplicative ideal **of \(\mathcal M_L\)**: \(n_1\in\mathcal S_h\)
and \(n_2\in\mathcal M_L\) imply \(n_1n_2\in\mathcal S_h\) (all later uses
have \(n_2=N(v)\in\mathcal M_L\)).  Its complement in \(\mathcal M_L\) is
not multiplicatively closed.
For example at \(h=L=12\), neither \(25\) nor \(49\) has a divisor
\(11\pmod {12}\), while \(25\cdot49\) does, since \(35\equiv11\pmod {12}\).

*Proof.*  At each prime, every exponent from zero through \(e_1+e_2\) splits
as a sum of exponents in the two allowed intervals; multiplication over the
primes proves the equality of divisor sets.  The ideal assertion uses the
factor \(1\in\Delta_h(n_2)\).  The displayed example proves the final
assertion. ∎

The ideal property is only **absorption**, not Gauss composition.  If
\(N_i=D_iE_i\) are two displayed witness pairs, all four balanced mixed
products

\[
 D_1D_2,\ D_1E_2,\ E_1D_2,\ E_1E_2
\]

are \(+1\pmod h\), not \(-1\).  A divisor made from an odd number of the
four displayed factors is \(-1\), but with two pairs it is one original
factor or the complement of one original factor.  Thus it merely carries
one witness unchanged through the other whole norm.  With three witness
pairs there is a positive ternary composition,

\[
 D_*=D_1D_2D_3,
 \quad E_*=E_1E_2E_3,
 \quad N(p_*)=\prod_{i=1}^3N(p_i),                             \tag{20.4}
\]

because both new factors are again \(-1\pmod h\).  This can have odd prime
output when the \(p_i\) are odd, but inversion requires the target norm to
split into three factors individually congruent to \(1\pmod L\).  It does
not address norms which are atoms in this monoid.

This is the complete explanation of the tempting “norm form” under the
suggested factor multiplication.  The change of variables
\((a,b)\mapsto(ha-1,hb-1)\) turns the binary form into the split norm
\(DE\).  Its two displayed congruence components are graded by the signs
\(\{+1,-1\}\): multiplication sends the desired negative component squared
to the positive component.  This identity supplies a split torus, not a
nonsplit quadratic ring or a class-group operation.  Negating \(D_1D_2\)
restores the residue \(-1\), but makes the factor negative.  Thus there is
no non-absorptive balanced factorwise monomial binary law preserving the
product \(N_1N_2\) (absorption itself, e.g. \(N_1N_2=D_1\cdot(E_1D_2E_2)\),
of course preserves it).  The smallest positive
correction does give a different product, and must be audited separately.

**Lemma 20.2.1 (proved: the minimal corrected binary law).**  Let
\((a_i,b_i,c,k)\), \(i=1,2\), be two parameter solutions at the same
\((c,k)\), and put

\[
 A=ha_1a_2-a_1-a_2,\qquad B=hb_1b_2-b_1-b_2.                 \tag{20.4a}
\]

Then \(A,B>0\), \(k\mid A+B\), and

\[
 P=4ABc-(A+B)/k                                               \tag{20.4b}
\]

is a positive soluble integer at \((c,k)\).  On factors this is the
non-monomial correction

\[
 hA-1=(ha_1-1)(ha_2-1)-2,\qquad
 hB-1=(hb_1-1)(hb_2-1)-2.                                    \tag{20.4c}
\]

If both input parameters \(p_1,p_2\) are odd, the canonical output \(P\) is
even.

*Proof.*  Since \(h\geq4\), \(A,B\geq h-2>0\).  Modulo \(k\), (20.4a)
gives
\(A+B\equiv-(a_1+b_1)-(a_2+b_2)\equiv0\).  Equations (20.4b–c) now give a
valid factorization and hence a solution.  For parity, write
\(D_i=ha_i-1,E_i=hb_i-1\).  As \(p_i\) is odd,
\(D_iE_i=1+Lp_i\equiv1+L\pmod {2L}\).  The corrected norm is

\[
 (D_1D_2-2)(E_1E_2-2)
 =N_1N_2-2(D_1D_2+E_1E_2)+4.
\]

Here \(N_1N_2\equiv1\pmod {2L}\), while

\[
 D_1D_2+E_1E_2-2
 =h\{h(a_1a_2+b_1b_2)-(a_1+a_2+b_1+b_2)\}
\]

is divisible by \(hk=L\).  Thus the corrected norm is
\(1\pmod {2L}\), so \(P\) is even. ∎

The parity failure can be bypassed by an affine shift: replacing
\(A\) by \(A+kt\) sends \(P\) to
\(P+t(4Bck-1)\).  Its modulus is coprime to \(P\), so Dirichlet gives
infinitely many prime outputs.  But this is exactly one of the coordinate
grids classified in Theorem 20.4 below, not a new inverse operation.  For
example, composing the \((1,1)\) witness for \(p=5\) with itself gives
\((A,B,P)=(2,12,82)\); shifting \(B\) by 33 gives
\((A,B,P)=(2,45,313)\).  Thus the multiplication-atom example 313 is
reachable by corrected composition plus an already-harvested translation,
but deciding the required shift from a target still requires its factor
pair \(7\cdot179\).

More generally, replacing (20.4c) by
\(D_1D_2-2+hr\), \(E_1E_2-2+hs\) merely replaces \((A,B)\) by
\((A+r,B+s)\); subject to positivity, the sole integrality condition is
\(r+s\equiv0\pmod k\).  These corrections range inside the same reduced-
seed grids of Theorem 20.4.  Reverse corrected composition also has no total
move: it asks simultaneously for factorizations of \(hA+1\) and \(hB+1\)
into factors \(-1\pmod h\).  In the displayed 313 witness,
\(hB+1=181\) is prime.  Hence the first non-monomial law exists, but after
full squeezing it adds no target coverage beyond the affine lattice and has
no everywhere-defined descent.

**Theorem 20.3 (proved: finite transfer seeds cannot be cofinite).**  Fix
\((c,k)\) and finitely many prime seeds \(p_1,\ldots,p_r\), each witnessed
at \((c,k)\).  Their absorption orbits

\[
       \{p_i\circ_Lt:t\geq0\}
       =\{P\ge0:P\equiv p_i\pmod {N(p_i)}\}

automatically miss infinitely many primes \(P\equiv1\pmod {24}\).

*Proof.*  Put \(M=\operatorname{lcm}(24,N(p_1),\ldots,N(p_r))\).  Every
prime \(P\equiv1\pmod M\) misses every orbit, because
\(1\not\equiv p_i\pmod {N(p_i)}\): here \(1<p_i<N(p_i)\).  Dirichlet gives
infinitely many such primes. ∎

There are witnessed norms which cannot be generated by any nontrivial fixed-
\((c,k)\) composition.  At \((c,k)=(1,1)\),

\[
       p=313,\qquad 4p+1=1253=7\cdot179

displays a witness, since both factors are \(3\pmod4\).  But \(1253\) has
no proper divisor \(1\pmod4\), so it is an atom under (20.2).  It is a
soluble prime that reverse composition cannot even enter.  The finite replay
in `verify.py (s)` finds many such atoms: among the 76 primes
\(p<5000,\ p\equiv1\pmod {24}\), the \((\text{witness},\text{monoid-atom})\) counts
are

\[
\begin{array}{c|rrrr}
(c,k)&(0,0)&(0,1)&(1,0)&(1,1)\\ \hline
(1,1)&16&24&14&22\\
(1,2)&4&46&2&24.
\end{array}
\]

This is a finite computation, not a density claim.

#### Cross-modulus products

There is also an exact composition after forgetting down to \((C,K)=(1,1)\).
Write \(w_i=c_i k_i^2\).  Then

\[
 (1+4w_1p_1)(1+4w_2p_2)=1+4P,
 \quad P=w_1p_1+w_2p_2+4w_1w_2p_1p_2.                         \tag{20.5}
\]

If the first factor has any Type-II witness, one of its factors is
\(3\pmod4\), remains a divisor of \(4P+1\), and proves that \(P\) is soluble
at \((1,1)\).  Unlike fixed-parameter composition, (20.5) can be odd for
odd \(p_1,p_2\) when \(w_1,w_2\) have opposite parity.  For example

\[
 (1+4\cdot1\cdot5)(1+4\cdot4\cdot3)=21\cdot49=4\cdot257+1,
\]

so the witnesses for \(5\) at \((1,1)\) and for \(3\) at \((1,2)\)
compose to a witness for the prime \(257\) at \((1,1)\).

The minimal correction also works across different slices after reduction
modulo 4, and unlike the same-slice law it can produce an odd prime.

**Lemma 20.3.1 (proved: corrected cross-slice prime composition).**  Given
any two Type-II witness pairs
\(N_i=D_iE_i\), possibly at different \((c_i,k_i)\), put

\[
       D=D_1D_2-2,\qquad E=E_1E_2-2,
       \qquad P=(DE-1)/4.                                    \tag{20.5a}
\]

Then \(D,E\equiv-1\pmod4\), so \(P\) is a positive integer soluble at
\((C,K)=(1,1)\).  In particular this is a genuine composition across
solutions of different primes whenever \(P\) is prime.

*Proof.*  Every Type-II witness factor is \(-1\pmod4\); hence each corrected
product is \(1-2=-1\pmod4\), and their product is \(1\pmod4\).  The
factorization \(4P+1=DE\) is Theorem 17.1(iii) at \((1,1)\). ∎

For an exact hard-prime example, use

\[
 1+16\cdot3=7\cdot7,
 \qquad 1+4\cdot59=3\cdot79.
\]

The corrected pairing gives

\[
 (7\cdot3-2)(7\cdot79-2)=19\cdot551
       =4\cdot2617+1,
\]

and \(2617\) is prime with \(2617\equiv1\pmod {24}\).  Thus the transfer
slot is not empty: two smaller solved primes really do compose to a hard
solved prime.

This still does not propagate to all primes.  Every output **as normalized
in (20.5a)** has a \((1,1)\) witness.  Reverse composition requires both
displayed factors \(D+2,E+2\) to split into old witness factors
\(3\pmod4\), and either may be prime.  In particular none of the six primes
in §19.3 which have no \(k=1\) representation can be an output under this
normalization.  Affine shifts of a corrected output again give infinitely
many primes, including hard primes after an appropriate CRT restriction,
but only inside the forced grids of Theorem 20.4.

There is a complete rescaled version, which does permit \(K>1\).

**Corollary 20.3.2 (proved: all inherited common-modulus rescalings).**  With
\(D,E\) from (20.5a), let \(H\) be any positive multiple of 4 dividing
\(\gcd(h_1,h_2)\), and put \(T=(DE-1)/H\).  For every

\[
       K\mid H/4,\qquad K\mid T,
       \qquad C=H/(4K),\qquad P=T/K,                           \tag{20.5b}
\]

\(P\) is a positive soluble integer at \((C,K)\).

*Proof.*  Both original factors are \(-1\pmod H\), so
\(D=D_1D_2-2\) and \(E=E_1E_2-2\) are also \(-1\pmod H\).  The definitions
give \(H=4CK\) and
\(DE=1+HT=1+4PCK^2\), which is (17.3). ∎

For example, the witnesses

\[
 1+16\cdot3=7\cdot7,
 \qquad 1+64\cdot41=15\cdot175
\]

have common modulus \(H=8\).  Their corrected factors are
\(103,1223\); choosing \((C,K)=(1,2)\) in (20.5b) gives

\[
       103\cdot1223=1+16\cdot7873,
\]

another hard prime composed from the smaller primes 3 and 41.  The extra
conditions in (20.5b) are exact divisibility constraints.  Reverse use still
requires the two simultaneous factorizations after adding 2, now together
with a common-modulus and square-factor synchronization.  No argument makes that inverse move total.

The exact product law (20.5) itself is absorption.  Every output of (20.5) lies in the narrow
\((1,1)\) slice, and an atomic value such as \(4\cdot313+1\) cannot arise as
a nontrivial product of factors \(1\pmod4\).  More generally one may write
the product as \(1+4PCK^2\) whenever \(CK^2\) divides \((N_1N_2-1)/4\).
An inherited divisor \(D_i\) remains a witness only when additionally
\(CK\mid(D_i+1)/4\).  These are divisibility restrictions, not a free
change of modulus, and return exactly to a forced factor class.

#### All coordinate translations

The translation \(c\mapsto c+t\) from §17.6 is not the whole affine action.
There are equally exact translations

\[
 \begin{array}{rcl}
 c\mapsto c+t&:&p\mapsto p+4ab\,t,\\
 a\mapsto a+kt&:&p\mapsto p+(4bck-1)t,\\
 b\mapsto b+kt&:&p\mapsto p+(4ack-1)t.                        \tag{20.6}
 \end{array}
\]

They can be classified completely.

**Theorem 20.4 (proved: reduced-seed classification of a fixed slice).**  For
a solution \((a,b,c,k)\), let \(a_0,b_0\in\{1,\ldots,k\}\) be the positive
residues of \(a,b\pmod k\), and write
\(a=a_0+ku, b=b_0+kv\).  Then

\[
 a_0+b_0\in\{k,2k\},
 \quad p_0=4a_0b_0c-(a_0+b_0)/k>0,                            \tag{20.7}
\]

and, with \(D_0=ha_0-1, E_0=hb_0-1\),

\[
       p=p_0+uE_0+vD_0+Luv.                                  \tag{20.8}
\]

Conversely every \(u,v\geq0\) in (20.8) is a valid parameter solution
(allowing noncoprime \(a,b\), as in Theorem 17.1(iii)).  Thus for fixed
\((c,k)\) the entire parameter solution set is the union of only \(k\)
bilinear grids,
corresponding to
\((a_0,b_0)=(r,k-r)\), \(1\leq r<k\), and \((k,k)\).

*Proof.*  The divisibility \(k\mid a+b\) gives (20.7); the only multiples of
\(k\) between 2 and \(2k\) are \(k,2k\).  Also \(p_0\geq4-2>0\).  Finally

\[
 1+Lp=(D_0+Lu)(E_0+Lv),

after which (20.8) follows by expansion.  Reversing the calculation proves
the converse. ∎

Equivalently the fixed-slice generating function is the following finite
sum of positive double \(q\)-series

\[
 \sum_{r}\sum_{u,v\geq0}
 z^{p_{0,r}+uE_{0,r}+vD_{0,r}+Luv}.                            \tag{20.9}
\]

This is the complete fixed-\((c,k)\) coordinate-grid parametrization, but
in the wrong direction for induction: it descends an **already known solution** to a reduced soluble
seed.  To decide whether a supplied prime \(p\) lies in one of the grids,
one must factor \(1+Lp\) as
\((D_0+Lu)(E_0+Lv)\), which is precisely the original divisor-coset event,
now refined modulo \(L\).  The apparent descent has no starting move on a
counterexample.

**Computational test (finite).**  Exhausting all hard primes below 5000 and
all fixed slices \(1\leq c,k\leq3\), only 12 of 76 targets are in an
absorption orbit of a smaller prime witnessed in the same slice:

\[
433,457,1753,2113,2953,3001,3433,3793,4057,4177,4561,4993.
\]

The seed search below 1000 is complete for this experiment: a nontrivial
fixed-slice transfer to \(P<5000\) has
\(P=s+t(1+Ls)>(L+1)s\geq5s\).  In particular none of
\(409,577,1201,2521\) is reached in these slices.  This does not exclude a
larger \((c,k)\), but it confirms that the exact transfer law is much sparser
than the actual solved set at this scale.

**Outcome of the transfer hunt.**  A nontrivial algebraic structure was
found and classified: split-norm multiplication, its sign grading, the
minimal corrected binary law, exact and corrected cross-modulus forgetting,
and the full affine coordinate action.  The corrected cross-slice law even
composes the smaller primes 3 and 59 to the hard prime 2617.  These laws
propagate infinitely many prime witnesses.
They do **not** prove cofiniteness: exact binary same-slice prime composition
has the wrong parity/sign, the corrected law collapses into the affine grids,
finite seed orbits are escaped by residue 1, and multiplication atoms block
reverse exact composition.  No inverse operation lowering an arbitrary
target prime was found.

### 20.2 Algorithmic and well-ordering attempts

#### Reverse composition

**Attempt (failed).**  Given \(P\), factor \(N(P)\) and choose a proper
factor \(n\equiv1\pmod L\).  Then

\[
 s=(n-1)/L,
 \qquad t=(N(P)/n-1)/L,
 \qquad P=s\circ_Lt,                                          \tag{20.10}
\]

and \(s,t<P\).  If \(s\) is a previously witnessed prime, this is a valid
well-ordering step.

**Exact failure.**  A proper factor \(1\pmod L\) need not exist, even when
\(P\) is soluble: \(P=313,(c,k)=(1,1)\) is the explicit atom above.  If such
a factor does exist, it need not encode a prime or a witnessed smaller
integer.  The size is a genuine monovariant, but the move is not total.

#### Affine reduction

**Attempt (failed).**  Starting from a quadruple, repeatedly subtract \(k\)
from \(a\) or \(b\); (20.6) strictly lowers \(p\) until the reduced seed
(20.7) is reached.

**Exact failure.**  This is a terminating algorithm on the set of
**solutions**, not on the set of input primes.  Its first step requires the
factor \(D=4ack-1\) which is the desired certificate.  Reconstructing
\(u,v\) from a bare \(p\) asks for the factorization in the sentence after
(20.9), so the proposed monovariant is circular.

#### Euclidean/continued-fraction reduction

Solving (17.1) for \(b\) gives

\[
 b={kp+a\over 4ack-1}.
\]

The following identity makes the obstruction exact:

\[
 (4ack-1)\mid(kp+a)
 \quad\Longleftrightarrow\quad
 (4ack-1)\mid(p+4a^2c),                                      \tag{20.11}
\]

because

\[
 4ac(kp+a)=p(4ack-1)+(p+4a^2c),

and \((4ac,4ack-1)=1\).  Hence, for fixed \((a,c)\), all possible \(k\)
are encoded by divisors

\[
       R\mid p+4a^2c,\qquad R\equiv-1\pmod {4ac}.             \tag{20.12}
\]

**Attempt (failed).**  Round \((kp+a)/(4ack-1)\), or apply the Euclidean
algorithm to \((p+4a^2c,4ack-1)\), and adjust \((a,c,k)\) according to the
remainders.

**Exact failure.**  Rounding gives a small *analytic* error but integrality
requires the remainder to be exactly zero.  Euclid lowers a pair of
integers, but its new pair is not generally of the form
\((p+4a'^2c',4a'c'k'-1)\) with positive parameters and the same \(p\).
Thus the parameter invariant is lost at the first nonzero remainder.  The
simple line \(a=c=1\) illustrates the issue: it succeeds exactly when
\(p+4\) has a divisor \(3\pmod4\).  It fails for \(p=97\), since
\(p+4=101\), although \(97\) is soluble at \((a,b,c,k)=(1,13,2,2)\).
Moving to another line restarts, rather than descends, the divisor search.
LLL or continued fractions control closeness only and supply no mechanism
forcing (20.12).

#### Least-counterexample induction

**Attempt (failed).**  If \(P\) is the least exceptional prime, all smaller
prime factors, and hence all smaller composite integers, are soluble.  For
\(q<3P\), the window value \(x=(P+q)/4<P\) is therefore soluble.  Try to
feed a solution of \(4/x\) back into the two-term split of \(q/x\).

**Exact failure.**  Solubility of \(4/x\) gives denominators on a different
fiber.  The required split of \(q/x\) is equivalent to a divisor of \(x^2\)
in one specified class modulo \(q\); the supplied solution of \(4/x\) gives
no such divisor.  At \(q=3\), the distinction is especially sharp:
\(4/x\) would have to possess a representation with one denominator exactly
\(x\), leaving a two-term representation of \(3/x\).  Induction guarantees
an unanchored representation only.  This is the window-irrelevance wall of
§17.7 in algorithmic form.

No attempted algorithm obtained both properties needed for a proof: a move
defined on every unsolved input and a positive integer monovariant decreased
by that move.

### 20.3 Minimal-gap pair

Several proposed auxiliary statements collapsed either to a false claim
(“every fixed norm has a nontrivial \(1\pmod L\) factor,” refuted by the
atom \(1253\)) or to the conjecture itself.  The closest unconditional
construction found is the following off-diagonal supply statement.

**Lemma 20.5 (proved: off-diagonal forced factors).**  Let \(p,k,t\geq1\),
put \(r=4kt-1\), and suppose \((p,r)=1\).  There is a unique class
\(c_0\pmod r\) such that every \(c\equiv c_0\pmod r\) satisfies

\[
       r\mid1+4pck^2,
       \qquad r\equiv-1\pmod {4k}.                            \tag{20.13}
\]

*Proof.*  The coefficient \(4pk^2\) is invertible modulo \(r\), so take
\(c_0\equiv-(4pk^2)^{-1}\pmod r\). ∎

This proves an infinite supply of factors with the correct congruence after
the factor \(c\) is omitted from the modulus.  Synchronizing the two copies
of \(c\) is the entire remaining gap:

\[
 r\equiv-1\pmod {4ck}
 \quad\Longleftrightarrow\quad c\mid t.                       \tag{20.14}
\]

If one can choose \((k,t)\) so that the least positive solution \(c_0\) in
Lemma 20.5 divides \(t\), then \(a=t/c_0\) gives
\(r=4ac_0k-1\), and (20.13) is a Type-II witness.  Conversely every
Type-II witness arises in exactly this way, because \((a,4ack-1)=1\) and

\[
 a(1+4pck^2)=pk(4ack-1)+(a+pk).                               \tag{20.15}
\]

Thus the **proved side** is unrestricted modular-inverse supply (20.13); the
**minimal named gap** is the diagonal synchronization \(c_0\mid t\).  The
pair is useful diagnostically but does not constitute progress toward a
proof: (20.14)–(20.15) show that the synchronization assertion is equivalent
to the original Type-II residual statement, not a weaker theorem smuggled
in as a lemma.

For comparison, there are unconditional representations immediately one
unit/sign away from the target.  If \(p=4n+1\), then

\[
 {4\over p}={1\over n+1}+{1\over p(n+1)}+{1\over p(n+1)}
             +{1\over p(n+1)},                               \tag{20.16}
\]

and

\[
 {4\over p}={1\over n+1}+{1\over n(n+1)}-{1\over np}.         \tag{20.17}
\]

Both are proved by one-line expansion.  Compressing (20.16) or repairing
the sign in (20.17) uniformly would prove the conjecture, but the former is
again the two-term divisor condition and the latter crosses the positivity
component isolated in §10.  They are therefore weaker minimal-gap pairs than
(20.13)–(20.15), not proof routes.

**Outcome.**  No auxiliary statement was both proved unconditionally and
shown to imply Erdős–Straus without leaving an equivalent unproved
synchronization condition.  Claiming otherwise would be a proof of the
conjecture; none was obtained.

### 20.4 Wild cards

**Generating function (attempt; no traction).**  Theorem 20.4 gives the
exact fixed-slice series (20.9), a finite sum of double \(q\)-series with
bilinear exponent.  Coefficients are nonnegative, but the series
is not a theta series of a positive quadratic form, and composition acts by
multiplication of \(1+Lp\), not addition of exponents.  No modular
transformation or cusp-form positivity was found.  Summing over \((c,k)\)
recreates the divisor-counting series already bounded by the cubic supply of
§18 rather than a coefficientwise positivity theorem.

**Divisor circle / three-distance idea (attempt; no traction).**  Writing a
prime factor of a shifted value as a rotation in
\((\mathbb Z/h\mathbb Z)^\times\) turns bounded divisor exponents into a
finite multidimensional orbit.  Three-distance phenomena control one
irrational cyclic orbit, while the adversarial case here is a product of
short cyclic arcs with arithmetic phases and a prescribed endpoint.  After
projection to a cyclic quotient this is exactly Lemma 17.4.1's exponent-mass
problem; no order on the circle is preserved by multiplication across
several generators.

**Non-monomial correspondence (unresolved slot).**  Lemma 20.2.1 is a
surviving non-monomial degree-two correction at fixed \((c,k)\), but its
general additive corrections are exactly the affine grids of Theorem 20.4,
and its inverse again asks for prescribed factorizations.  The cross-slice version (20.5a) and its common-modulus rescalings (20.5b)
survive too, but their reverse direction requires simultaneous
factorizations after adding 2 plus the explicit modulus/square-factor
synchronization.  What remains unclassified are polynomial/rational maps
outside these inherited-common-modulus constructions which change to a
nontrivial \((C,K)\) and add correction terms to the factors.  A viable map would have to preserve
positivity and the negative congruence grade while possessing an inverse
branch that lowers an arbitrary prime parameter.  The smallest corrections at fixed modulus and across a common divisor of
the input moduli do not do this.  This is
the only transfer subslot not formally closed; at the time of §20's writing
no warm candidate was visible.  (§22 subsequently executes the low-degree
search and DOES find new maps — the tensor-partition family — though with
no total inverse; see §22 for the current state.)

### 20.5 Honest outcome statement

**No proof of the Erdős–Straus conjecture was obtained.**  What was proved is:

1. the exact fixed-parameter composition monoid and its witness-absorption
   law (Lemmas 20.1–20.2), including the wrong-sign obstruction to exact
   binary Gauss composition, the valid ternary law, and the minimal corrected
   binary law (Lemma 20.2.1), which collapses into the affine grids;
2. finite transfer orbits cannot cover all hard primes (Theorem 20.3), and
   explicit witnessed monoid atoms block reverse composition;
3. the exact and corrected cross-modulus laws (20.5)/(20.5a–b), including
   the explicit prime transfers \((3,59)\mapsto2617\) and
   \((3,41)\mapsto7873\), and the complete reduced-seed classification of
   every affine coordinate transfer (Theorem 20.4);
4. the exact Euclidean divisor reduction (20.11) and the off-diagonal factor
   supply Lemma 20.5, with the missing diagonal synchronization proved
   equivalent to the Type-II residual problem.

The transfer door is colder after this audit: every natural multiplication,
minimal correction, or translation either propagates an existing forced
class, lands in the wrong sign/parity component, collapses into an affine
grid, or requires the target divisor before descent can begin.  The only
logically open transfer direction is a non-monomial cross-modulus
correspondence outside the inherited common-modulus rescalings which does
not collapse to an affine forced grid.
A next research direction, if that slot is pursued: classify low-degree
positive polynomial maps on factor pairs satisfying
\(D'E'=1+4PCK^2\) and \(D',E'\equiv-1\pmod {4CK}\) identically, modulo the
multiplication, fixed/cross-slice minimal-correction and rescaling, and
coordinate-shift maps above, then check whether any inverse branch strictly
lowers \(P\).  (To become a well-posed classification this needs the degree
bound, variable set, positivity notion, and the equivalence relation
generated by the known maps fixed in advance.)  §22 executes exactly this
program at degree two and finds the tensor-partition maps — new, with
strictly-lowering but non-total inverses.  Flexible reinterpretations, fixed
additive maps, and Type-I/cross-type laws follow in §§23, 25–26; §30 gives the
full Type-II tuple orbit.  None proves witness existence.

---

## 21. The truth of H_PF

**Verdict.**  H_PF is **false-looking, but not proved false**.  Exact
reorganization exposes strong shifted-divisor clustering, and the measured
avoidance exponent through \(X=3200\) is fitted much better by
\((\log X)^2\log\log X\) than by \((\log X)^3\).  Neither the fit nor the
reorganization is a lower-bound sieve, however.  The proved bounds in this
section leave a large gap: at the degree range relevant to H_PF they do not
supply an avoider density larger than \(\exp[-c(\log X)^3]\).  Thus Theorem
18.6 remains conditional; it must not be cited as dead, and H_PF must not be
cited as plausible merely from the cubic first moment.  (H_PF as stated is
refuted — see §31; the critical-window variant \(H_{\rm PF}'\) below remains
open.)

Write

\[
 {\rm Av}_X(N)=\{n\leq N:n\bmod M\notin\mathscr R(M)
       \text{ for every }M\leq X,\ M\equiv3\pmod4\}.
\]

For fixed \(X\), this set is periodic modulo the lcm of the participating
moduli, so its natural density \(\delta_X\) exists.

### 21.1 Exact shifted-divisor form

For \(D=\prod p^{e_p}\), define

\[
 R_0(D)=\prod_p p^{\lceil e_p/2\rceil}.                       \tag{21.1}
\]

**Lemma 21.1 (exact reorganization; proved).**  For \(A=(M+1)/4\),

\[
 D\mid A^2\quad\Longleftrightarrow\quad R_0(D)\mid A
 \quad\Longleftrightarrow\quad M\equiv-1\pmod {4R_0(D)}.     \tag{21.2}
\]

Consequently

\[
 n\notin{\rm Av}_X
 \Longleftrightarrow
 \begin{cases}
 \text{there are }D,M\geq1\text{ with }M\mid n+4D,\\
 M\leq X,\qquad M\equiv-1\pmod {4R_0(D)}.
 \end{cases}                                                  \tag{21.3}
\]

The congruence in (21.3) already implies \(M\equiv3\pmod4\).  It also
implies \(R_0(D)\leq(M+1)/4\), hence \(D\leq R_0(D)^2\leq(X+1)^2/16\);
there is no omitted tail of \(D\)'s.  Conversely every pair in (21.3) has
\(D\mid((M+1)/4)^2\), so it gives exactly a class of Lemma 18.1.  In
particular, no weaker extra congruence for nonsquarefree \(D\) has been
lost.

*Proof.*  At a prime, \(D\mid A^2\) says \(e_p\leq2v_p(A)\), which is
exactly \(\lceil e_p/2\rceil\leq v_p(A)\).  This proves (21.2).
Lemma 18.1 then turns \(n\equiv-4D\pmod M\) into (21.3), in both
directions. ∎

The fibers of (21.1) are also exact.  If \(R=\prod p^{a_p}\), then

\[
 R_0(D)=R\quad\Longleftrightarrow\quad
 D=R^2/s\quad\text{for one }s\mid\operatorname{rad}(R),       \tag{21.4}
\]

so there are \(2^{\omega(R)}\) such shifts \(D\).

### 21.2 A common quadratic escape

The finite-window data have a conspicuous contaminant: every literal square
survives every modulus.  This is not an accident.

**Lemma 21.2 (quadratic-sign lemma; proved).**  If \(M=4A-1\) and
\(D\mid A^2\), then

\[
 \left(\frac{D}{M}\right)=+1,
 \qquad
 \left(\frac{-4D}{M}\right)=-1,                              \tag{21.5}
\]

where the symbols are Jacobi symbols.  Hence every unit class in
\(\mathscr R(M)\) has Jacobi sign \(-1\).  Every \(n\) with
\((n/M)\in\{0,+1\}\) avoids \(\mathscr R(M)\), and in particular every
perfect square avoids the complete intrinsic system for every \(X\).

*Proof.*  Let \(p\) be an odd prime dividing \(A\).  Quadratic reciprocity
for a prime numerator and the odd composite denominator \(M\), followed by
\(M\equiv-1\pmod p\) and \(M\equiv3\pmod4\), gives

\[
 \left(\frac pM\right)
 =\left(\frac Mp\right)(-1)^{(p-1)(M-1)/4}
 =\left(\frac{-1}p\right)(-1)^{(p-1)/2}=1.
\]

If \(2\mid A\), then \(M\equiv7\pmod8\), so \((2/M)=1\) as well.
Multiplicativity gives \((D/M)=1\) for every divisor of \(A^2\).  Finally
\((-1/M)=-1\) because \(M\equiv3\pmod4\), and \((4/M)=1\).  All classes
are units since \((A,M)=1\). ∎

**Two rigorous lower bounds (too small to decide H_PF).**  Lemma 21.2 gives

\[
 |{\rm Av}_X(N)|\geq\lfloor\sqrt N\rfloor.                    \tag{21.6}
\]

It also gives a positive periodic set.  Put
\(L_X=\operatorname{lcm}\{M\leq X:M\equiv3\pmod4\}\).  Every unit square
modulo the odd number \(L_X\) avoids all the classes, whence

\[
 \delta_X\geq {\varphi(L_X)\over 2^{\omega(L_X)}L_X}
              \geq \exp\{-O(X/\log X)\}.                    \tag{21.7}
\]

The first expression is the proportion of unit squares prime-power by
prime-power; the last bound uses \(\omega(L_X)\leq\pi(X)\),
\(\varphi(L_X)/L_X\gg1/\log X\), and the standard
\(\pi(X)\ll X/\log X\).  This improves the single common class
\(1\pmod {L_X}\), but is still exponentially *smaller* than
\(\exp[-c(\log X)^3]\).  At H_PF's degree budget,
\(\log N\gg(\log X)^4\), (21.6) is only
\(N^{-1/2}\leq\exp[-c'(\log X)^4]\).  Thus neither construction refutes
the actual quantified hypothesis.  It does explain why counting an initial
interval with \(N\) only a few million gives a badly biased plateau.

### 21.3 What can be bounded unconditionally

The prime-modulus part of the complete system gives a genuine quadratic
exponent, with no composite-modulus assembly hypothesis.

**Theorem 21.3 (prime-slice upper bound; proved).**  There are absolute
constants \(c,C>0\) such that, for large \(X\), if

\[
 \log N\geq C(\log X)^3,                                     \tag{21.8}
\]

then

\[
 |{\rm Av}_X(N)|\ll N\exp\{-c(\log X)^2\}.                   \tag{21.9}
\]

The same statement holds for the natural density \(\delta_X\) without
(21.8).

*Proof.*  Apply Lemma 16.3 with the fixed subfamily \(\mathcal J=\{1\}\)
(and any fixed admissible ambient \(K\)).  For primes
\(X^{1/2}<\ell\leq X\), it supplies subsets
\(\mathcal C_\ell\subseteq\mathscr R(\ell)\), with
\(f(\ell)=|\mathcal C_\ell|\), such that

\[
 \sum_{X^{1/2}<\ell\leq X}{f(\ell)\over\ell}
       \asymp(\log X)^2.                                     \tag{21.10}
\]

The moduli here are distinct primes.  In the standard Selberg upper-bound
sieve put \(g(\ell)=f(\ell)/(\ell-f(\ell))\),
\(P=\prod\ell\), and

\[
 S(Q)=\sum_{s\leq Q,\ s\mid P}\mu^2(s)\prod_{\ell\mid s}g(\ell),
 \qquad Q=N^{1/2}.
\]

The usual large-sieve/Selberg inequality gives
\(|{\rm Av}_X(N)|\ll N/S(Q)\).  The untruncated Euler product
\(G=\prod(1+g(\ell))\) satisfies \(G\geq\exp(c_1(\log X)^2)\), by
(21.10); Lemma 16.3's upper half and
\(f(\ell)=\ell^{o(1)}<\ell/2\) give the corresponding upper control.
Rankin's trick with \(v=1/\log X\), exactly as in (16.14), gives

\[
 {G-S(Q)\over G}
 \leq\exp\{-{\log N\over2\log X}+C_1(\log X)^2\}.
\]

Under (21.8) this is at most \(1/2\), and (21.9) follows.  Letting \(N\)
tend to infinity at fixed \(X\), or directly using the Chinese remainder
theorem for the prime subsystem, proves the density assertion. ∎

Theorem 21.3 is the strongest unconditional conclusion obtained here.  Its
exponent is \(2\), not \(2+\delta\); it therefore does not meet the cubic
claim and is explicitly not advertised as the partial positive-power result
requested by H_PF.

### 21.4 Heuristic after the exact reorganization

This subsection is **heuristic**, not a sieve theorem.  For fixed \(D\),
(21.3) asks whether \(n+4D\) has a divisor in one progression modulo
\(4R_0(D)\).  Restricting first to prime divisors predicts an avoidance
factor whose logarithm is of size

\[
 {1\over\varphi(4R_0(D))}
 \log {\log X\over\log(4R_0(D))},                            \tag{21.11}
\]

when the right side is positive.  Equation (21.4) then leads to

\[
 \sum_{R\leq X/4}{2^{\omega(R)}\over\varphi(4R)}
       \log {\log X\over\log(4R)}.                           \tag{21.12}
\]

The elementary Euler factors give

\[
 \sum_{R\leq y}{2^{\omega(R)}\over\varphi(R)}
       \asymp(\log y)^2:                                     \tag{21.13}
\]

indeed the nonconstant part of the local factor is
\(2p/(p-1)^2=2/p+O(p^{-2})\).  Partial summation in (21.12) therefore
predicts \(\Theta((\log X)^2)\), not a cubic exponent.  The tempting
shortcut which replaces the logarithm in (21.11) by \(\log\log X\)
uniformly produces \((\log X)^2\log\log X\), but it overcounts the many
\(R\)'s close to \(X\), whose progression contains almost no eligible
primes.

Composite divisors are the unresolved part.  For one fixed shift they are
heavily clustered: at \(D=1\), the complete divisor family has mass
\(\asymp\log X\), while its avoiders have density only
\(\asymp(\log X)^{-1/2}\), as recorded in §18.4.  Treating its classes as
independent is therefore wrong by an exponential factor.  Stacking the
shifted values for all \(D\) should recover much of the loss, but no joint
lower-bound theorem is known.  The structural prediction from
(21.11)–(21.13) is an effective exponent between
\((\log X)^2\) and \((\log X)^2\log\log X\), hence
\(o((\log X)^{2+\epsilon})\) for every fixed \(\epsilon>0\).  **If that
prediction is correct, H_PF is false.**  With effective mass
\(t^2\log t\), the mass/Rankin balance is
\(t^3\log t\asymp\log N\), giving only
\((\log N)^{2/3}(\log\log N)^{1/3}\): the scale already reached by
Theorem 16.4, not \(3/4\).  This ceiling statement is conditional on the
heuristic effective mass; it is not a corollary about the true exceptional
set.

### 21.5 Exact and sampled measurements

**Exact.**  Exhausting a full period gives:

\[
\begin{array}{c|r|r|c}
X&L_X&\#\text{ avoiders in }[0,L_X)&\delta_X\\ \hline
3&3&2&0.6666667\\
7&21&8&0.3809524\\
11&231&64&0.2770563\\
15&1155&256&0.2216450\\
19&21945&4096&0.1866484\\
23&504735&57344&0.1136121\\
27&4542615&516096&0.1136121
\end{array}                                                   \tag{21.14}
\]

The new modulus \(27\) removes no survivor left by the preceding system, an
exact small-scale instance of the clustering issue.  `verify.py (t)` replays
the complete \(X=27\) period, all smaller rows, the
\(R_0\) equivalence through \(A=100\), and the Jacobi-sign theorem through
\(M<2000\).

**Measured (informational).**  To suppress the literal-square bias, 12
million independent 64-bit integers were sampled uniformly from
\([10^{14},9\cdot10^{17})\), with NumPy `default_rng(21001801)`.  Membership
was evaluated exactly for every sampled integer by constructing every set
\(\{-4D\bmod M:D\mid((M+1)/4)^2\}\).  The intervals below are 95% Wilson
binomial intervals; they describe sampling error only, not extrapolation in
\(X\) or the systematic difference between this finite window and a full
period (the latter is far too large at these \(X\)).  Thus
\(\widehat\delta_X\) below denotes the sampled-window proportion, not a
proved estimate of the natural density.

\[
\begin{array}{c|r|c|c|c|c}
X&\#\text{ survive}&\widehat\delta_X&95\%\text{ interval}
 &-\log\widehat\delta_X&\mu(X)\\ \hline
50&633186&5.27655\,10^{-2}&[.052639,.052892]&2.942&2.843\\
100&211887&1.765725\,10^{-2}&[.017583,.017732]&4.037&4.248\\
200&54255&4.52125\,10^{-3}&[.004483,.004559]&5.399&6.081\\
400&11585&9.65417\,10^{-4}&[.000948,.000983]&6.943&8.368\\
800&1740&1.45000\,10^{-4}&[.000138,.000152]&8.839&11.171\\
1600&201&1.67500\,10^{-5}&[1.459,1.923]10^{-5}&10.997&14.541\\
3200&14&1.16667\,10^{-6}&[.695,1.958]10^{-6}&13.661&18.528
\end{array}                                                   \tag{21.15}
\]

Here the last admissible modulus is respectively
\(47,99,199,399,799,1599,3199\).  The conditional shell hazards show the
correlation directly.  For successive doublings after \(50\), the increments
in \(-\log\widehat\delta\), the increments in raw class mass, and their
ratios were

\[
 (1.095,1.405,.779),\ (1.362,1.833,.743),\
 (1.544,2.287,.675),\ (1.896,2.803,.676),\
 (2.158,3.370,.640),\ (2.664,3.987,.668).                    \tag{21.16}
\]

Thus later classes remove substantially fewer conditional survivors than
\(F(M)/M\) independence predicts, though the hazard remains positive at this
range.

For scale diagnosis only, unweighted affine fits of
\(-\log\widehat\delta_X\) against the named candidate functions (each with
an intercept) have root-mean-square residuals

\[
\begin{array}{c|cccccc}
 f(X)&L\log L&L^{3/2}&L^2&L^2\log L&L^{2+\log 2}&L^3\\ \hline
 {\rm RMSE}&.391&.342&.170&.046&.077&.169
\end{array},\qquad L=\log X.                                  \tag{21.17}
\]

The normalized ratio \(-\log\widehat\delta_X/(\log X)^2\) runs only from
\(.190\) to \(.210\).  The rarest row has 14 observations, adjacent scales
are coupled, and slowly varying functions are nearly collinear on this
range.  Equation (21.17) is evidence for the
\(L^2\log L\) side, not an asymptotic determination.

**Honest endpoint.**  We now know exactly why the naive cubic first moment is
not evidence for cubic avoidance, and we have a proved common quadratic
obstruction plus the unconditional upper bound (21.9).  We do **not** have
the lower bound \(\delta_X\geq\exp[-C(\log X)^2\log\log X]\) that would
refute H_PF, nor an upper bound \(\exp[-c(\log X)^{2+\epsilon}]\) that would
support it.  Proving either is the remaining density problem.  Until then
the correct label is: **H_PF false-looking, open**.  (H_PF as stated is
refuted — see §31; the critical-window variant \(H_{\rm PF}'\) below remains
open.)

**Section 24 post-script (additive correction).**  The subset-product audit
there shows that the last ``structural prediction'' in §21.4 was too strong.
A typical shifted integer has about \((\log X)^{\log 2}\) squarefree
small-prime subset products *before* the \(M\leq X\) and coprimality filters.
Pretending that these raw products are uniform modulo every \(4R\) gives the
\((\log X)^{2+\log 2}\) uniform-model benchmark.  Its premise fails the
truncation-boundary check, so this is a toy-model output, not an
evidence-backed scale or a corrected asymptotic.  The new column in (21.17)
is nearly collinear with \(L^2\log L\) (correlation \(0.99972\)) on the
measured range and cannot distinguish the two.  Section 24 also pins the
prime subsystem two-sided when \(\log N\geq C_3(\log X)^3\), with no
restriction for natural density, proves a substantial truncated-\(R\)
clustering lower bound, and leaves the full-system label unchanged.  (H_PF
as stated is refuted — see §31; the critical-window variant \(H_{\rm PF}'\)
below remains open.)

## 22. Degree-two classification of transfer maps

This section executes the low-degree search proposed at the end of §20.  It
finds new maps, so its outcome is a discovery rather than a ``known maps
only'' no-go theorem.  The most useful new maps multiply the two input
moduli, multiply the two input values of \(k\), and have a strict descent on
their image.  That image is not all targets.

### 22.1 The search space and why the norm equation is not an extra equation

Put \(h_i=4c_i k_i\), and, when a common modulus is used, write
\(h_i=g r_i\), treating \(g,r_1,r_2\) as independent symbols.  The
**universal degree-two search space** used here consists of pairs

\[
 (D',E')\in\mathbb Z[D_1,E_1,D_2,E_2]^2,
 \qquad \max(\deg D',\deg E')\leq2,                         \tag{22.1}
\]

whose coefficients do not depend on a numerical slice.  The permitted
output moduli are

\[
 M=g^\alpha h_1^\beta h_2^\gamma,
 \quad \alpha,\beta,\gamma\geq0,
 \quad 1\leq \alpha+\beta+\gamma\leq2.                     \tag{22.2}
\]

Thus quotients such as an lcm, rational maps, and coefficients which depend
on \(h_i\) are outside this search.  This is the promised precise degree-two
slot, not a classification of arbitrary rational correspondences.  Radial
positivity means that the highest nonzero homogeneous part after the
centering below has nonnegative coefficients, not all zero.  This implies
positivity when all centered variables are scaled to infinity; every new
map actually used below is positive on the entire positive orthant.

For comparison with §20, let \(\mathcal K_{\leq2}\) be the maps obtained,
up to input/output swaps, from raw-factor projections and products, one
application of \(XY\mapsto XY-2\), integral coordinate translations, and
a common-modulus interpretation as in (20.5b), with compositions retained
only when their total degree is at most two.  A translation parameter may
be a fixed integer or an integer polynomial in the admitted inputs, but not
a quotient by a symbolic modulus; every nonconstant translated term
therefore retains an explicit factor of that modulus.  This makes
``known-generated'' an exact polynomial-map test while not artificially
restricting polynomial shifts.  Its degree-two normal forms have at most
one raw quadratic monomial in each corrected/product output coordinate;
extra monomials introduced by translations have coefficients divisible by
the relevant symbolic modulus.  Absorption by a whole second norm is degree
three and hence is absent from this slot.  This enumeration will be used
for nontriviality below.

Set

\[
 z=(u_1,v_1,u_2,v_2)
   =(D_1+1,E_1+1,D_2+1,E_2+1).                              \tag{22.3}
\]

**Theorem 22.1 (proved: complete coefficient classification at degree two).**
Let \(Q\in\mathbb Z[D_1,E_1,D_2,E_2]\) have degree at most two, and let
\(M\) be (22.2), with \(q=\alpha+\beta+\gamma\).  Then
\(Q\equiv-1\pmod M\) as a polynomial consequence of
\(D_i,E_i\equiv-1\pmod {h_i}\) if and only if

\[
 Q=-1+\sum_\nu q_\nu z^\nu,                                \tag{22.4}
\]

where every retained monomial satisfies

\[
 |\nu|\geq q,\qquad \nu_{u_1}+\nu_{v_1}\geq\beta,
 \qquad \nu_{u_2}+\nu_{v_2}\geq\gamma,
 \qquad |\nu|\leq2.                                        \tag{22.5}
\]

The coefficients \(q_\nu\) are arbitrary integers; radial positivity is the
stated sign filter on their top-degree part.  The number of free coefficients
for one output factor is

\[
\begin{array}{c|rrrrrrrrr}
M&g&h_1&h_2&g^2&gh_1&gh_2&h_1^2&h_1h_2&h_2^2\\ \hline
\#&14&9&9&10&7&7&3&4&3.
\end{array}                                                  \tag{22.6}
\]

The two factors are independent, so the pair has twice the displayed
number.  In particular, at the genuinely cross-modulus maximum
\(M=h_1h_2\), every solution is exactly

\[
 D'=-1+(u_1,v_1)R(u_2,v_2)^T,
 \qquad E'=-1+(u_1,v_1)S(u_2,v_2)^T                         \tag{22.7}
\]

for two integral \(2\times2\) matrices \(R,S\).  Nonnegative nonzero
matrices make both factors positive for all inputs.

*Proof.*  Substitute \(D_i=h_i x_i-1,E_i=h_i y_i-1\).  A centered monomial
of slice-degrees \((d_1,d_2)\) acquires
\(g^{d_1+d_2}r_1^{d_1}r_2^{d_2}\).  Divisibility by
\(M=g^q r_1^\beta r_2^\gamma\) is therefore exactly (22.5).  Distinct
monomials in the independent \(x_i,y_i,g,r_i\) cannot cancel a failed
valuation.  Counting the allowed monomials gives (22.6); for \(h_1h_2\),
only the four cross-bilinear monomials survive. ∎

This also exposes a degeneracy in the originally suggested coefficient
system.  Once \(D'=-1+F\) and \(E'=-1+G\) are each \(-1\pmod M\),

\[
 D'E'-1=FG-F-G=M T                                           \tag{22.8}
\]

identically.  Taking \(K'=1,C'=M/4,P'=T\) always supplies the norm
structure.  Thus (b) adds no nonlinear equations to (a); the exact solve is
a linear coefficient solve, not a Gröbner problem.  At \(M=h_1h_2\), a
generic raw quadratic has 15 coefficients, the congruence system has rank
11, and (22.7) is its four-parameter solution.  `verify.py (u)` replays this
`linsolve` calculation and all dimensions in (22.6).

The classification is already enough to answer the existence question:
there are infinitely many maps besides §20's maps.  For example

\[
 D'=(D_1+1)(D_2+1)-1,
 \qquad E'=(E_1+1)(E_2+1)-1,
 \qquad M=h_1h_2.                                            \tag{22.9}
\]

Its raw linear coefficients are one, not multiples of a common modulus, and
its output modulus is a product rather than a divisor of \(\gcd(h_1,h_2)\).
It is therefore not among the explicit §20 formulas (absorption, minimal
corrections, rescalings, coordinate shifts); we have not formalized a
complete generator-grammar for \(\mathcal K_{\leq2}\) with a normal-form
lemma, so "new" here means precisely "not among those explicit formulas,"
not a proved quotient by a generated equivalence.  More generally, the
nonnegative coefficient cone in (22.7) has the four centered products as
its additive atoms.  Pairing two atoms has, modulo all input/output swaps,
three support types: the same atom twice, two atoms sharing one input
coordinate, and two opposite atoms.  The first gives
\(P'=A(MA-2)\), hence no positive odd prime output; the second has a common
parameter factor, and its natural inherited-\(k\) prime outputs force that
factor to be one and reduce to a coordinate-grid rescaling.  Opposite atoms
can produce primes, but under the default \(K'=1\) they cannot reach any of
the six primes in §19.3, which have no \(k=1\) witness.

### 22.2 A new cross-modulus, cross-\(k\) composition

The source relation \(k_i\mid a_i+b_i\), which was not needed in Theorem
22.1, permits a stronger interpretation of (22.7).  Write
\(s_i=(a_i+b_i)/k_i\).  If the bilinear coefficient matrices in (22.7)
are \(R,S\), then the quotient in (22.8) is divisible by \(k_1k_2\) for
all source solutions exactly when

\[
                  R+S=\lambda
                  \begin{pmatrix}1&1\\1&1\end{pmatrix}       \tag{22.10}
\]

for an integer \(\lambda\).  Indeed, reducing successively modulo \(k_1\)
and \(k_2\) substitutes \(b_i=-a_i\); coefficient matching says all four
entries of \(R+S\) are equal.  Then

\[
 \Phi+\Psi=\lambda(a_1+b_1)(a_2+b_2)
            =\lambda k_1k_2s_1s_2.                           \tag{22.11}
\]

For nonnegative coefficients the coefficient-minimal solutions have
\(\lambda=1\): the four tensor monomials

\[
 a_1a_2,\qquad a_1b_2,\qquad b_1a_2,\qquad b_1b_2.          \tag{22.12}
\]

are partitioned into two nonempty sets, whose sums are \(A=\Phi\) and
\(B=\Psi\).  There are 14 ordered maps, seven up to output swap, and only
three under all symmetries: a \(1+3\) split, an adjacent \(2+2\) split, and
an opposite \(2+2\) split.  These are exactly the coefficient-minimal maps
with both factors nonzero.  If zero-factor layers are admitted, all 16
splits (including empty/full) form the degree-one-in-\(\lambda\) generators
of the nonnegative coefficient semigroup; every larger \(\lambda\) is an
entrywise superposition of those layers.

**Theorem 22.2 (proved: tensor-partition composition and strict descent on
its image).**  Let \((a_i,b_i,c_i,k_i)\), \(i=1,2\), be any two positive
Type-II parameter solutions, with source integers

\[
 p_i=4a_ib_ic_i-s_i>0,\qquad s_i=(a_i+b_i)/k_i.
\]

Choose any nonempty proper partition of (22.12), and let \(A,B\) be the two
sums.  Then

\[
 C=4c_1c_2,\qquad K=k_1k_2,
 \qquad P=16c_1c_2AB-s_1s_2                                \tag{22.13}
\]

is a positive Type-II solution, because

\[
 A+B=(a_1+b_1)(a_2+b_2)=K s_1s_2,
 \qquad P=4ABC-(A+B)/K.                                     \tag{22.14}
\]

On factors this is a degree-two map of form (22.7), with output modulus
\(4CK=h_1h_2\).  It is not in \(\mathcal K_{\leq2}\): a nontrivial split
has centered sums (and hence either multiple raw quadratic monomials or
unit raw linear coefficients), while the known degree-two normal forms do
not; also (20.5b) can only forget to a common divisor of the input moduli.
Finally

\[
 P\geq(4a_1b_1c_1)(4a_2b_2c_2)-s_1s_2
   =p_1p_2+p_1s_2+p_2s_1>\max(p_1,p_2).                     \tag{22.15}
\]

Thus every inverse of this map, wherever it exists, strictly lowers both
source values.

*Proof.*  Equations (22.13)--(22.14) prove the factor congruence, integrality,
and norm identity.  For a \(1+3\) split, the singleton's opposite monomial
lies in the other part, so their product already equals
\(a_1b_1a_2b_2\).  An adjacent split gives, up to symmetry,
\(AB=a_1b_1(a_2+b_2)^2\); an opposite split contains
\(a_1b_1(a_2^2+b_2^2)\) in its expansion.  Each is at least
\(a_1b_1a_2b_2\), proving (22.15).  The polynomial non-membership is the
normal-form comparison just given. ∎

For the \(1+3\) split, one explicit factor formula is

\[
\begin{aligned}
 D'&=(D_1+1)(D_2+1)-1,\\
 E'&=(D_1+1)(E_2+1)+(E_1+1)(D_2+1)
       +(E_1+1)(E_2+1)-1.                                  \tag{22.16}
\end{aligned}
\]

This gives real hard-prime transfers from smaller primes.  For example,
using source tuples in the order \((p;a,b,c,k)\),

\[
 (17;1,6,1,1),(7;1,1,2,2)\longmapsto(409;1,13,8,2),          \tag{22.17}
\]

and

\[
 (7;1,2,1,3),(1217;17,18,1,5)
       \longmapsto(23929;17,88,4,15).                        \tag{22.18}
\]

The opposite split is genuinely active too:

\[
 (73;2,5,2,1),(47;1,3,4,4)
       \longmapsto(23929;17,11,32,4),                        \tag{22.19}
\]

since \(17=2\cdot1+5\cdot3\) and
\(11=2\cdot3+5\cdot1\).  In particular, (22.18)--(22.19) reach a prime
which has no \(k=1\) representation; these are not merely outputs of the
\(K'=1\) normalization.

**Computational Search 22.3 (exact finite enumeration, not a theorem about
all primes).**  All positive parameter representations of a fixed target
\(p\) can be enumerated without a search cutoff.  Since

\[
 p=4ABC-(A+B)/K\geq4AB-A-B\geq2AB,
\]

one has \(AB\leq p/2\); also \(K\mid A+B\), and then

\[
 C={Kp+A+B\over4ABK}.                                       \tag{22.20}
\]

Enumerating (22.20) for the six no-\(k=1\) primes gives

\[
\begin{array}{c|rrrrrr}
p&409&577&5569&9601&23929&83449\\ \hline
\#\text{ ordered parameter tuples}&14&14&20&14&78&30\\
\#\text{ with }4\mid C&2&0&0&2&22&0.
\end{array}                                                  \tag{22.21}
\]

Factoring \(A,C/4,K,(A+B)/K\) and checking all 14 primitive partitions
shows that 409, 9601, and 23929 are reached from smaller prime sources;
577, 5569, and 83449 are not.  The negative three are stronger than a
failure of the primitive search: every maximal-modulus map with a natural
\(K'\mid k_1k_2\) has

\[
 C'={h_1h_2\over4K'}
    =4c_1c_2{k_1k_2\over K'},                               \tag{22.22}
\]

so it necessarily has \(4\mid C'\), while (22.21) exhausts *all* target
parameter tuples.  Hence no inverse branch in this genuinely cross-modulus
family is total.  `verify.py (u)` replays the complete bounded enumeration,
the three reachability outcomes, and the displayed examples.

The failure is proof-relevant.  Inverting a primitive map requires a target
factor pair \((A,B,C,K)\), factorizations
\(C=4c_1c_2\), \(K=k_1k_2\),
\((A+B)/K=s_1s_2\), and a compatible partition (22.12).  When those data
exist, (22.15) gives a genuine descent.  They do not exist for the three
explicit targets above, and obtaining the initial target pair from a bare
prime is still the original witness problem.  Thus this is a new partial
descent, not an induction proving Erdős--Straus.

### 22.3 The one-pair degree-three slot

There is an equally short complete coefficient solve for a single witness
pair.  Put \(u=D+1,v=E+1\).

**Theorem 22.4 (proved: univariate-pair classification through degree
three).**  Let \(Q\in\mathbb Z[D,E]\) have degree at most three.  For
\(r=1,2,3\), the congruence \(Q\equiv-1\pmod {h^r}\) follows identically
from \(D,E\equiv-1\pmod h\) if and only if

\[
 Q=-1+\sum_{r\leq i+j\leq3}q_{ij}u^iv^j.                    \tag{22.23}
\]

There are respectively 9, 7, and 4 free coefficients for one output factor.
For degree at most two the corresponding counts are 5 and 3 for output
moduli \(h,h^2\).  These are all solutions; the proof is the one-variable-
slice specialization of Theorem 22.1.  The ranks \(1,3,6\) of the raw
10-coefficient cubic systems are replayed in `verify.py (u)`.

The coefficient-minimal maximal-modulus maps are pairs of centered
monomials.  The only pair which can avoid a forced common factor for generic
coprime \(a,b>1\) is, up to swaps,

\[
 D_r'=(D+1)^r-1,\qquad E_r'=(E+1)^r-1,
 \qquad r=2,3.                                               \tag{22.24}
\]

With \(K'=1,C'=h^r/4\), their output is

\[
             P_r=h^r(ab)^r-a^r-b^r.                          \tag{22.25}
\]

For the \(p=5\) witness \((a,b,c,k)=(1,2,1,1)\), (22.25) gives
\(P_2=59\) and \(P_3=503\).  Cubing can also reach hard primes: the
\(p=103\) witness \((2,15,1,1)\) gives \(P_3=1,724,617\), which is prime
and \(1\pmod {24}\).  Squaring cannot give a hard prime: if \(P_2\) is odd,
exactly one of \(a,b\) is odd, so
\(P_2\equiv-(a^2+b^2)\in\{3,7\}\pmod8\).

There is again no total inverse.  The displayed inverse requires both
\(D'+1\) and \(E'+1\) to be perfect \(r\)-th powers, all outputs in the
\(K'=1\) interpretation have a \(k=1\) witness, and the natural maximal
moduli have \(4\mid C'\).  Either (22.21)'s no-\(k=1\) result or its three
no-\(4\mid C\) targets supplies an explicit obstruction.

**Outcome.**  The degree-two universal polynomial system (22.1)--(22.2) is
closed by Theorem 22.1, and the one-pair degree-three system by Theorem
22.4.  The answer to ``are there other maps?'' is **yes**: centered-modulus
lifts exist in an infinite coefficient family, and the tensor-partition
maps (22.13) give new cross-modulus, cross-\(k\), prime-to-prime transfers
with a strict lowering inverse on their image.  The answer to ``is the
inverse total?'' is **no for these new maximal-modulus families under the
natural \(K'\mid k_1k_2\) interpretations**: three explicit primes below
\(10^5\) have no parameter tuple with the necessary \(4\mid C\), and
inversion still starts from the target witness pair.  (Reinterpretations
moving factors of \(4c_1c_2\) into \(K'\) are not classified; see §23 for the
later classification.)  No
Erdős--Straus proof results.  Rational maps, quotient/lcm output moduli, and
modulus-dependent polynomial coefficients remain outside the precisely
fixed search space and are not claimed classified here.

---

## 23. Flexible tensor reinterpretation: the six old blockers fall, but the
image is still not total

Section 22 fixed the tensor-partition output at
\(C=4c_1c_2, K=k_1k_2\).  That normalization is unnecessarily rigid.
This section moves factors between the output coordinates \(C\) and \(K\),
classifies the exact finite inverse problem for that enlarged family, and
runs it on every hard prime through \(10^5\).  The enlargement is substantial:
all six primes which motivated §22 are now images of smaller explicit source
tuples.  Its image is not total: eleven other hard primes in the same range
have no target tuple with the necessary divisibility \(4\mid CK\), and
Lemma 23.9 closes every arbitrary-modulus reading of every higher pure tensor
on those eleven.  Modulus-dependent non-pure maps remain outside that
closure.  Labels below are strict; in particular the range statements are
computational, not theorems about all primes.

Let \(S\) denote the positive integers \(p\geq2\) possessing a positive
Type-II tuple

\[
 (a,b,c,k),\qquad s=(a+b)/k,\qquad p=4abc-s.                 \tag{23.1}
\]

Primality and \((a,b)=1\) are not part of this definition.  For any positive
integers satisfying \(k\mid a+b\) and (23.1), multiplication by \(k\) gives

\[
 kp+a+b=4abck.
\]

Thus the three fractions below have common denominator \(pabck\), numerator
\(kp+a+b=4abck\), and hence sum to \(4/p\):

\[
 {4\over p}={1\over abc}+{1\over pack}+{1\over pbck}.        \tag{23.2}
\]

No primality or coprimality is needed for this validity computation.  For
odd primes, Theorem 17.1(i) is additionally the bijection statement for the
coprime Type-II tuples.  This distinction matters below: several source
values are composite, but their displayed tuples certify their membership
in \(S\) without invoking a classical residue identity.  In particular
\((1,1,1,1)\) is a tuple for \(2\), and \((1,1,1,2)\) is a tuple for \(3\).
The value \(1\) is not usable: three positive unit fractions have sum at most
\(3\), so they cannot represent \(4/1\).

### 23.1 The flexible-\((C',K')\) composition

Take two source tuples \((a_i,b_i,c_i,k_i)\), put
\(s_i=(a_i+b_i)/k_i\), and partition the four tensor monomials

\[
 a_1a_2,\quad a_1b_2,\quad b_1a_2,\quad b_1b_2
\]

into two nonempty ordered parts with sums \(A,B\).  Write
\(\kappa=k_1k_2\).  Then

\[
 A+B=(a_1+b_1)(a_2+b_2)=\kappa s_1s_2.                      \tag{23.3}
\]

**Theorem 23.1 (proved: all factor reallocations at maximal tensor
modulus).**  For every positive integer \(K'\) satisfying

\[
 K'\mid A+B,\qquad K'\mid4c_1c_2\kappa,                    \tag{23.4}
\]

put

\[
 C'={4c_1c_2\kappa\over K'},\qquad
 P'=4ABC'-{A+B\over K'}.                                   \tag{23.5}
\]

Then \((A,B,C',K')\) is a positive Type-II tuple for the integer \(P'\).
Equivalently, if

\[
 Q=16c_1c_2AB-s_1s_2
\]

is the §22 output, then

\[
                 P'={\kappa\over K'}Q.                     \tag{23.6}
\]

*Proof.*  Conditions (23.4) make both \(C'\) and \((A+B)/K'\) positive
integers.  Substitution gives

\[
 4ABC'-{A+B\over K'}
 ={\kappa\over K'}(16c_1c_2AB-s_1s_2),
\]

which is (23.6).  The right side is positive because \(Q>0\) by Theorem
22.2; the left side is an integer.  More elementarily, every positive
quadruple satisfying (23.5) has
\(P'\geq4AB-A-B\geq2AB\geq2\).  Finally (23.5) is exactly (23.1), so the direct
common-denominator calculation preceding (23.2) gives the unit-fraction
identity. ∎

The divisibility \(K'\mid A+B\) is not cosmetic.  Equation (23.3) only says
that \(\kappa\mid A+B\); moving additional factors into \(K'\) is possible
only when those factors also divide \(s_1s_2\), and when (23.4)'s modulus
condition holds.

**Warning 23.2 (proved: §22's descent does not survive automatically).**
When \(K'>\kappa\), equation (23.6) makes the new output smaller than the
§22 output.  The inequality \(Q>\max(p_1,p_2)\) therefore says nothing about
whether \(P'>\max(p_1,p_2)\).  For example, the source tuples

\[
 (2;1,1,1,1),\qquad(75;1,4,5,1)
\]

and the singleton partition \((A,B)=(1,9)\) admit \(K'=10\), \(C'=2\).
They output

\[
 P'=4\cdot1\cdot9\cdot2-{10\over10}=71<75.
\]

Thus every inverse branch counted as a descent below is checked separately
for \(2\leq p_i<P'\); no inequality from §22 is reused.

### 23.2 Exact inverse and the circularity trap

Let \((A,B,C,K)\) be a target tuple for \(P\).  Theorem 23.1 forces

\[
 {CK\over4}=(c_1c_2)(k_1k_2).                               \tag{23.7}
\]

Consequently \(4\mid CK\) is necessary.  It is the replacement for §22's
too-strong condition \(4\mid C\).

**Lemma 23.3 (proved: exact finite inverse test).**  A target tuple
\((A,B,C,K)\) is an image under Theorem 23.1 if and only if \(4\mid CK\)
and the following finite data exist:

1. a factorization \(CK/4=\gamma\kappa\);
2. ordered splittings \(\gamma=c_1c_2\) and \(\kappa=k_1k_2\);
3. \(\kappa\mid A+B\), followed by an ordered splitting
   \((A+B)/\kappa=s_1s_2\);
4. positive splits \(a_i+b_i=k_is_i\);
5. one of the 14 ordered nonempty proper subsets of the four tensor
   monomials whose two sums are exactly \((A,B)\);
6. source values \(p_i=4a_ib_ic_i-s_i\geq2\).

It is a descending inverse exactly when the final check also gives
\(p_i<P\) for both \(i\).

*Proof.*  Necessity follows from (23.3), (23.5), and (23.7).  Conversely the
listed data are positive source tuples satisfying (23.1), and their forward
image has the prescribed \(A,B\) and
\(C'K'=4c_1c_2k_1k_2=CK\).  Taking \(K'=K\) forces \(C'=C\), hence the
output is the target. ∎

The target tuples themselves are enumerated completely by (22.20):
\(AB\leq P/2\), \(K\mid A+B\), and

\[
 C={KP+A+B\over4ABK}.                                       \tag{23.8}
\]

The inverse search used below loops over every item in Lemma 23.3.  There
are no bounds chosen experimentally.

There is a logical trap here.  Starting a purported proof with “choose a
Type-II tuple of \(P\), then invert it” has already assumed \(P\in S\).
The genuine statement needed for a proof is **forward-image totality**:
for every hard prime \(P\), there exist explicit data of Lemma 23.3 with
smaller source values whose forward image equals \(P\).  The source
memberships in \(S\) are free because the inverse data explicitly construct
the source tuples; no appeal to the conjecture, to primality of a source, or
to a possibly Type-I classical identity is needed.  The computational
inversion of a known target is therefore a diagnostic for this theorem to
hunt, not an induction proof by itself.

### 23.3 The six old blockers all fall

**Computational Search 23.4 (exact finite enumeration).**  Applying (23.8)
and Lemma 23.3 to all six primes in §19.3 gives:

\[
\begin{array}{c|rrrrrr}
P&409&577&5569&9601&23929&83449\\ \hline
\#\text{ ordered target tuples}&14&14&20&14&78&30\\
\#(4\mid C)&2&0&0&2&22&0\\
\#(4\mid CK)&4&2&10&4&42&4\\
\#\text{ ordered descending inverse branches}
 &272&48&1536&144&33768&80
\end{array}                                                  \tag{23.9}
\]

Thus the single most important first test is positive for every old blocker:
**577, 5569, and 83449 do have tuples with \(4\mid CK\)**, despite having no
tuple with \(4\mid C\).  In fact all six have descending inverses.  A simple
branch for each uses the fixed source tuple for \(2\):

\[
\begin{array}{r|c|c|c}
P&(A,B,C,K)&\text{other source }(p_2;a_2,b_2,c_2,k_2)&K/\kappa\\ \hline
409&(1,13,8,2)&(89;1,6,4,1)&2\\
577&(1,77,2,2)&(113;1,38,1,1)&2\\
5569&(1,41,34,6)&(4059;1,20,51,1)&6\\
9601&(1,173,14,2)&(2321;1,86,7,1)&2\\
23929&(1,301,20,2)&(5849;1,150,10,1)&2\\
83449&(5,39,107,4)&(36358;5,17,107,1)&4
\end{array}                                                  \tag{23.10}
\]

Here the first source is always \((2;1,1,1,1)\), \(\kappa=1\), and the
listed partition is a singleton versus the other three monomials.  Every
source value is between \(2\) and \(P-1\).  The composite values 4059 and
36358 cause no issue: their tuples in (23.10) are direct Type-II
certificates.

For an end-to-end check, the branch for 577 is

\[
 (2;1,1,1,1),\quad(113;1,38,1,1)
 \longmapsto(577;1,77,2,2),
\]

because the monomials are \(1,38,1,38\), the singleton split is
\((A,B)=(1,77)\), and \(C'K'=4\) is interpreted as \((C',K')=(2,2)\).
The three exact identities are

\[
\begin{aligned}
 {4\over2}&={1\over1}+{1\over2}+{1\over2},\\
 {4\over113}&={1\over38}+{1\over113}+{1\over4294},\\
 {4\over577}&={1\over154}+{1\over2308}+{1\over177716}.
\end{aligned}                                                \tag{23.11}
\]

`verify.py (v)` replays the complete target and inverse enumerations in
(23.9), every branch in (23.10), and (23.11) using exact rational
arithmetic.

### 23.4 Reachability through \(10^5\)

**Computational Search 23.5 (exact finite range, existential certificates
short-circuited).**  Every prime \(P\equiv1\pmod {24}\) through the stated
bound was tested.  For a success the search stops after an explicit inverse
certificate; for a failure it exhausts every target row (23.8).  The result
is

\[
\begin{array}{c|r|r|r|r}
\text{range}&\#P&\exists(4\mid CK)&\text{descending inverse}
 &\text{inverse with fixed source }2\\ \hline
P\leq10^4&143&132&132&129\\
P<10^5&1181&1170&1170&1166
\end{array}                                                  \tag{23.12}
\]

The three additional successes through \(10^4\) are 601, 5881, and 9049;
the only further one below \(10^5\) is 20641.  One explicit branch for each
is

\[
\begin{array}{r|c|c|c}
P&(A,B,C,K)&(p_1;a_1,b_1,c_1,k_1)&(p_2;a_2,b_2,c_2,k_2)\\ \hline
601&(2,19,4,3)&(5;1,2,1,1)&(65;1,6,3,1)\\
5881&(2,37,20,1)&(5;1,2,1,1)&(227;1,12,5,1)\\
9049&(1,566,4,81)&(59;1,20,1,1)&(8397;1,26,81,1)\\
20641&(17,76,4,3)&(5;1,2,1,1)&(2825;14,17,3,1)
\end{array}                                                  \tag{23.13}
\]

For the 1166 fixed-source-2 certificates below \(10^5\), the other displayed
source is prime only 139 times and is a hard prime itself only 20 times; 1027
are composite.  Its median ratio to the target is about 0.491, while the
largest observed ratio is \(73868/73897\approx0.99961\).  These statistics
depend on the deterministic first-certificate ordering and are descriptive,
not canonical.  They show both why a classical “non-hard prime” argument is
unnecessary and why there is no observed uniform contraction: the explicit
source tuple, not its residue class, certifies \(S\)-membership.  The full
row and all these descriptive statistics replay under `ES_FULL_SCAN=1`.

By default `verify.py (v)` certifies the \(10^4\) row of (23.12) in under ten
seconds and prints the command needed for the larger replay.  With
`ES_FULL_SCAN=1`, the same block recomputes the \(P<10^5\) row and its
first-certificate statistics from the exact enumerator.

### 23.5 The remaining obstruction and higher pure tensors

The eleven failures in both rows of (23.12) are

\[
 73,193,241,673,1129,1153,2473,2521,3169,3361,5281.          \tag{23.14}
\]

Every one belongs to \(S\); what fails is this composition image.  Complete
enumeration proves that **none has any target tuple with \(4\mid CK\)**.
The failure therefore occurs before tensor splitting or the source-size
test.

There is a useful exact parity form of the obstruction.

**Lemma 23.6 (proved: parity criterion for an odd target tuple).**  If
\((A,B,C,K)\) is a Type-II tuple for odd \(P\), then

\[
 v_2(K)=v_2(A+B),\qquad
 4\mid CK\ \Longleftrightarrow\ v_2(C)+v_2(A+B)\geq2.        \tag{23.15}
\]

Thus a tuple fails \(4\mid CK\) exactly when either

* \(A+B\) is odd and \(4\nmid C\), or
* \(A+B\equiv2\pmod4\) and \(C\) is odd.

*Proof.*  In \(P=4ABC-s\), \(s=(A+B)/K\) is odd because \(P\) is odd.
Hence \(v_2(A+B)=v_2(K)\), and (23.15) follows. ∎

For every parameter row of every prime in (23.14), the right side of
(23.15) is at most one.  This is a finite invariant of the complete tuple
set, not a congruence characterization of the prime alone; no residue-class
criterion selecting exactly these primes was found.

The same obstruction first closes all higher **pure maximal-modulus tensor
partitions**, including the proposed three-input extension.

**Lemma 23.7 (proved: higher-tensor divisibility no-go).**  For \(r\geq2\)
source tuples, partitioning the \(2^r\) tensor monomials at the product
modulus forces every output interpretation to satisfy

\[
 C'K'=4^{r-1}\prod_{i=1}^r c_i k_i.                          \tag{23.16}
\]

In particular three inputs force \(16\mid C'K'\), and any number of inputs
at least two forces \(4\mid C'K'\).  Hence none of (23.14) is reachable by
any such higher pure tensor.

*Proof.*  The centered input moduli are \(h_i=4c_ik_i\).  A tensor factor is
\(-1+(\prod h_i)A\), while a Type-II output factor is
\(-1+4C'K'A\).  Equating the coefficients gives
\(4C'K'=\prod h_i=4^r\prod c_ik_i\), which is (23.16). ∎

There is also a precise answer for the two simplest quotient-modulus
reinterpretations of the same centered partition.

**Lemma 23.8 (proved: quotient readings of a pure two-tensor).**  Let
\(g=(h_1,h_2)\), choose a modulus \(M\mid h_1h_2\) with \(4\mid M\), and
put \(r=h_1h_2/M\).  The factors
\(h_1h_2A-1,h_1h_2B-1\) can be read at modulus \(M\), but the target
coordinates become \((rA,rB)\).  Every

\[
 K'\mid\gcd(r(A+B),M/4),\qquad C'=M/(4K')                  \tag{23.17}
\]

gives a valid Type-II output.  For \(M=\operatorname{lcm}(h_1,h_2)\), one
has \(r=g\), which is divisible by four.  For
\(M=h_1h_2/g^2\), the interpretation is unavailable unless \(4\mid M\),
and when available \(r=g^2\), divisible by sixteen.  In either case both
target coordinates are divisible by four, so for an odd output (23.15)
forces \(4\mid CK\).  These quotient readings are valid compositions, but
cannot reach the odd primes (23.14).

*Proof.*  Since \(h_1h_2A=M(rA)\), each centered factor is \(-1\pmod M\)
and has target coordinate \(rA\), and similarly for \(B\).  Conditions
(23.17) say exactly that \(M=4C'K'\) and
\(K'\mid r(A+B)\), so (23.1) and the direct validity computation preceding
(23.2) apply.  Both input moduli are multiples of four, hence \(4\mid g\);
the two claimed values of \(r\) and the final use of (23.15) follow. ∎

*Remark.*  Oddness is necessary: two source-2 tuples, split as \((1,3)\)
and read at \(M=\operatorname{lcm}(4,4)=4\), give the even output
\((176;4,12,1,1)\), with \(CK=1\).

**Lemma 23.9 (proved: arbitrary readings of pure tensor factor pairs).**
Take \(r\geq2\) source tuples, put

\[
 H=\prod_{i=1}^r h_i,\qquad h_i=4c_i k_i,
\]

and let \((HA-1,HB-1)\) be a pure-tensor factor pair.  Any Type-II reading
of this pair at any modulus, producing \((A'',B'',C'',K'')\), satisfies

\[
 4C''K''A''=HA,\qquad 4C''K''B''=HB,
\]

and therefore the exact identity

\[
 H\gcd(A,B)=4C''K''\gcd(A'',B'').                            \tag{23.18}
\]

Consequently

\[
 v_2(4C''K'')+v_2(\gcd(A'',B''))
 =v_2(H)+v_2(\gcd(A,B))\geq4.
\]

*Proof.*  A Type-II factor pair for the target tuple is
\((4C''K''A''-1,4C''K''B''-1)\).  Equality with the given pure pair gives
the first two identities.  Taking the gcd of those identities gives
(23.18).  Finally every \(h_i\) is divisible by four, so
\(v_2(H)\geq2r\geq4\). ∎

**Corollary 23.9.1 (proved by complete finite audit: all eleven
resisters).**  No pure tensor of any order \(r\geq2\), read at any modulus,
outputs any tuple of any prime in (23.14).

*Proof.*  The complete (23.8) tuple lists for the eleven primes are audited
in `verify.py (v)`.  Every row \((A'',B'',C'',K'')\) has
\(v_2(C''K'')\leq1\), because it is a resister row, and also has
\(\gcd(A'',B'')\) odd.  Hence the left side of Lemma 23.9's valuation
identity is at most three, contradicting its lower bound of four. ∎

The arbitrary-modulus qualification is active, not cosmetic.  Take the
source tuple \((5;1,2,1,1)\) twice and split its tensor monomials into
\((A,B)=(3,6)\).  Then \(H=16\), the pure factor pair is \((47,95)\), and
\(M=24\mid16\gcd(3,6)=48\) reads it as

\[
 (A'',B'',C'',K'')=(2,4,1,6),\qquad P=31.
\]

Here \(K''=6\mid A''+B''\) and \(4\nmid C''K''\).  The product-modulus
reading instead gives \((3,6,4,1)\) of value 279.  Thus non-product readings
genuinely exceed Lemmas 23.7--23.8's scope; `verify.py (v)` checks this
example end to end.

**Assessment (scope, no overclaim).**  Lemma 23.9 closes every
arbitrary-modulus Type-II reading of a **pure tensor factor pair** on the
eleven resisters.  It does **not** classify modulus-dependent additive
corrections, which are non-pure maps, or general rational maps.  Those
families remain unclassified and could in principle evade the invariant;
(23.14) is not a no-go for every conceivable transfer map.

**Outcome.**  Moving factors from \(C\) into \(K\) is the immediate crack in
§22: it reaches all six old blockers, usually from the fixed source 2, and
empirically reaches every hard prime below \(10^5\) having any tuple with
\(4\mid CK\).  The enlarged family is nevertheless non-total.  Eleven exact
counterexamples have no such tuple, and Lemma 23.9 plus the complete odd-gcd
audit blocks every pure tensor of every order \(r\geq2\), read at any
modulus, from outputting any of their tuples.  Modulus-dependent additive
corrections and general rational maps remain outside this closure (§25 later
classifies a fixed additive subfamily, not the general family).  No
Erdős--Straus proof results; forward-image totality fails for the pure-tensor
family.

## 24. A subset-product audit and lower-bound routes for H_PF

This section returns to the density problem at the end of §21.  Put
\(L=\log X\).  Labels are deliberately strict: the prime-slice and
truncated-fiber statements below are theorems; the
\(L^{2+\log2}\) uniform-model benchmark is a toy-model output whose premise
fails the boundary check, not an evidence-backed scale.

### 24.1 Subset products: a real correction, but not a new asymptotic

**Assessment 24.1 (the subset-product correction).**  For a random shifted
integer \(y=n+4D\), the expected number of distinct primes at most \(X\)
dividing \(y\) is \(\log\log X+O(1)=\log L+O(1)\).  The Erdős--Kac typical
value therefore suggests

\[
 T_X(y):=2^{\omega_X(y)}=L^{\log2+o(1)},                     \tag{24.1}
\]

where \(\omega_X\) counts only prime factors at most \(X\).  Including
prime-power divisors alters this typical order only by an \(L^{o(1)}\) factor.
The deliberately raw uniform model ignores the eligibility filters and gives
chance

\[
 \min\{1,T_X(y)/\varphi(4R)\}.                               \tag{24.2}
\]

A filtered finite model instead counts only squarefree products \(M\leq X\)
formed without the prime \(2\) or primes dividing \(R\), equivalently with
\((M,4R)=1\).  There is no quadratic-symbol restriction forcing these
products into one coset.  Lemma 21.2 evaluates the Jacobi symbol of the
*resulting class modulo the divisor* \(M\); it does not prescribe the
residues modulo \(4R\) of the prime divisors of \(y\).

The formal sum behind the uniform-model benchmark is now clear.  The
saturated block \(\varphi(4R)\leq T=L^{\log2+o(1)}\) contains at most

\[
 \sum_{R\leq T^{1+o(1)}}2^{\omega(R)}
       =T^{1+o(1)}=L^{\log2+o(1)}                             \tag{24.3}
\]

shift events (retaining the usual harmless polylogarithmic factors).  Even
charging \(O(\log L)\), rather than one, for a saturated miss leaves this
block smaller than quadratic scale.  In the unsaturated block, (21.13)
would give

\[
 T\sum_{R\leq X/4}{2^{\omega(R)}\over\varphi(4R)}
       =L^{2+\log2+o(1)}.                                    \tag{24.4}
\]

Thus \(L^{2.693\ldots}\) is the output of the *uniform subset-product toy
model*, and remains \(o(L^3)\); it is not yet a scale supported by evidence.

The uniformity premise, however, fails a basic boundary check.  Averaged
over \(y\), the exact first moment of eligible divisors for one modulus
\(q=4R\) is

\[
 \sum_{\substack{m\leq X\\m\equiv-1\ (q)}}{1\over m}
 = {1\over q}\{\log(X/q)+O(1)\},                             \tag{24.5}
\]

with the evident one-term interpretation when \(q\) is close to \(X\).
Divisors at most \(X\) are concentrated by size, not spread uniformly over
all \(\varphi(q)\) units.  For \(q\asymp X\), almost every subset product is
smaller than the sole target \(q-1\); (24.2) misses this completely.  The
same issue persists, less starkly, well below the boundary.  Moreover the
avoidance probability is a quenched quantity and cannot be recovered from
the heavy-tailed mean divisor count alone.

**Computational 24.2 (informational).**  The deterministic experiment in
`verify.py (w)` samples large shifted integers and sums the actual
\((R,s)\)-hit indicators.  At \(X=80,160\), the raw model (24.2)
overpredicts those sums by factors \(5.11\) and \(5.67\).  After excluding
\(2\) and primes dividing \(R\), and counting only squarefree subset
products at most \(X\), the factors are still \(2.89\) and \(2.98\).  This
is not asymptotic evidence and does not isolate one correction: it conflates
the size cutoff, non-unit and coprimality exclusions, residue nonuniformity,
residue collisions among subset products, and overlap of divisor events.
It does show that the uniform model materially overpredicts after the stated
filters.  The fit in (21.17) gives root-mean-square residual \(0.077\) for
\(L^{2+\log2}\), versus \(0.046\) for \(L^2\log L\), and the two regressors
have correlation \(0.99972\).  Since \(L^{\log2}\leq4.3\) through
\(X=3200\), those data cannot see the uniform-model subset-product power.

**Assessment.**  Equations (24.1)--(24.4) identify a missing toy-model
mechanism, but (24.5) disproves its boundary premise.  The defensible
conclusion is only that \(L^{2+\log2}\) is a uniform-model benchmark, not an
evidence-backed scale.  The false-looking verdict survives; the claimed
narrow ``between \(L^2\) and \(L^2\log L\)'' structural prediction does
not.

### 24.2 The prime subsystem is exactly quadratic

For primes \(\ell\equiv3\pmod4\), write
\(f(\ell)=F(\ell)=|\mathscr R(\ell)|\), and let
\({\rm Av}^{\rm prime}_X(N)\) avoid the full sets
\(\mathscr R(\ell)\) for all such \(\ell\leq X\).

**Lemma 24.3 (full prime-class mass; proved).**  There are absolute constants
\(c,C>0\) such that

\[
 cL^2\leq\sum_{\substack{\ell\leq X\\\ell\equiv3\ (4)}}
 {F(\ell)\over\ell}\leq CL^2.                               \tag{24.6}
\]

*Proof.*  The lower bound is (21.10), because the harvested sets
\(\mathcal C_\ell\) are subsets of the full intrinsic sets.

For the upper bound put \(A=(\ell+1)/4\).  Lemma 18.1 and the local
inequality \(2e+1\leq(e+1)(e+2)/2\) give
\(F(\ell)\leq\tau(A^2)\leq\tau_3(A)\).  On a dyadic interval
\(A\asymp Y\), write every ordered factorization as \(A=abc\) and designate
one of its largest coordinates as \(c\).  By symmetry this loses at most a
factor three and gives \(ab\ll Y^{2/3}\).  For fixed \(a,b\), the prime
\(4abc-1\) lies in one reduced class modulo \(4ab\).  Brun--Titchmarsh,
uniformly in this range, gives

\[
 \#\{c:A\asymp Y,\ 4abc-1\ {\rm prime}\}
 \ll {Y\over\varphi(4ab)\log Y}.
\]

Since \(\varphi(4ab)\geq\varphi(a)\varphi(b)\) and
\(\sum_{m\leq y}1/\varphi(m)\ll\log(2y)\), summing over \(a,b\) gives

\[
 \sum_{\substack{A\asymp Y\\4A-1\ {\rm prime}}}\tau(A^2)
 \ll Y\log Y.                                                \tag{24.7}
\]

After division by \(\ell\asymp Y\), the dyadic block costs
\(O(\log Y)\).  Summing the \(O(L)\) blocks proves the upper bound in
(24.6). ∎

**Theorem 24.4 (two-sided prime-slice avoidance; proved).**  There are
absolute constants \(c_1,C_2,C_3>0\) such that, for all sufficiently large
\(X\),

\[
 N e^{-C_2L^2}\leq |{\rm Av}^{\rm prime}_X(N)|
       \leq N e^{-c_1L^2}                                    \tag{24.8}
\]

whenever \(\log N\geq C_3L^3\).  Its natural density is also
\(e^{-\Theta(L^2)}\).

*Proof.*  Distinct prime moduli are Chinese-remainder independent.  Hence
the natural density is exactly

\[
 V_X=\prod_{\substack{\ell\leq X\\\ell\equiv3\ (4)}}
       \left(1-{f(\ell)\over\ell}\right).                   \tag{24.9}
\]

Lemma 21.2 puts all \(f(\ell)\) classes among the \((\ell-1)/2\)
quadratic nonresidues, so \(f(\ell)/\ell<1/2\).  Lemma 24.3 and
\(-2u\leq\log(1-u)\leq-u\) for \(0\leq u\leq1/2\) now give
\(V_X=e^{-\Theta(L^2)}\).

For completeness, no sieve theorem with hidden growing-dimension constants
is needed to transfer the lower bound to \([1,N]\).  Put
\(a_\ell=f(\ell)/\ell\), \(\mu=\sum a_\ell\), and take the least odd
\(r\geq10\mu\).  Bonferroni gives, pointwise in the number \(h(n)\) of
violated prime conditions,

\[
 \mathbf{1}_{h(n)=0}\geq\sum_{j=0}^{r}(-1)^j{h(n)\choose j}. \tag{24.10}
\]

An intersection indexed by \(d\), a product of \(j\) primes, contains
\(\prod_{\ell\mid d}f(\ell)\) classes modulo \(d\), and therefore has
count

\[
 N\prod_{\ell\mid d}a_\ell
   +O\left(\prod_{\ell\mid d}f(\ell)\right).                \tag{24.11}
\]

The omitted main tail in (24.10) is at most
\(\sum_{j>r}\mu^j/j!\leq V_X/4\) for large \(X\).  Also (24.7), summed
dyadically, gives \(W:=\sum_{\ell\leq X}f(\ell)\ll XL\), so the total
rounding error is at most

\[
 \sum_{j\leq r}{W^j\over j!}=\exp\{O(L^3)\}.                \tag{24.12}
\]

Choosing \(C_3\) large makes (24.12) at most \(NV_X/4\).  Thus the left
side of (24.8) follows from (24.10).  The upper side is the Selberg argument
of Theorem 21.3 applied to the prime subsystem itself (or the even
Bonferroni truncation with the same bookkeeping). ∎

The theorem pins the prime subsystem at quadratic exponent, without a
\(\log\log X\) loss.  It does **not** lower-bound \({\rm Av}_X\), since
\({\rm Av}_X\subseteq{\rm Av}^{\rm prime}_X\).  It proves instead that a
cubic H_PF majorant must obtain its extra saving from composite moduli.

### 24.3 The one-shift cluster is exact

**Lemma 24.5 (the \(D=1\) family; proved).**  The integers avoiding all
classes \(n\equiv-4\pmod M\), \(M\leq X\), \(M\equiv3\pmod4\), are exactly
those for which no prime \(p\leq X\), \(p\equiv3\pmod4\), divides \(n+4\).
Their natural density is

\[
 \prod_{\substack{p\leq X\\p\equiv3\ (4)}}(1-1/p)
       \asymp L^{-1/2}.                                      \tag{24.13}
\]

The same lower bound, up to an absolute constant, holds on \([1,N]\) once
\(\log N\geq C L\log L\).

*Proof.*  A divisor \(M\equiv3\pmod4\) has a prime divisor
\(p\equiv3\pmod4\) to odd exponent, and that prime is itself a divisor at
most \(X\).  The converse takes \(M=p\).  The Chinese remainder theorem and
Mertens' theorem in the progression \(3\pmod4\) give (24.13).  For the
finite interval, odd Bonferroni truncation at degree \(O(\log L)\) has main
tail smaller than a fixed fraction of (24.13), while its total rounding
error is \(\exp\{O(L\log L)\}\), exactly as in (24.10)--(24.12). ∎

### 24.4 A scoped no-go for local quadratic certificates

The broad claim that *every* cheap congruence prescription leaves cubic
conditional first moment is false: a prescription can make selected classes
incompatible one by one.  The following statement isolates the actual
entropy wall for the natural Jacobi construction.  Write \(P^+(m)\) for the
largest prime factor of \(m\), with \(P^+(1)=1\), and

\[
 \mu_{\rm sm}(X,z)=
 \sum_{\substack{M\leq X,\ M\equiv3\ (4)\\P^+(M)\leq z}}
       {F(M)\over M}.                                        \tag{24.14}
\]

**Lemma 24.6 (smooth moduli carry negligible intrinsic mass; proved).**  For
every fixed \(B>0\), uniformly for \(2\leq z\leq L^B\),

\[
 \mu_{\rm sm}(X,z)=o(L^3).                                   \tag{24.15}
\]

*Proof.*  We use the standard Canfield--Erdős--Pomerance/de Bruijn
smooth-number upper bound (see, for example, Tenenbaum, *Introduction à la
théorie analytique et probabiliste des nombres*, III.5, Theorem 1.1 and its
corollary): for every fixed \(\delta>0\), uniformly for
\(z\geq(\log Y)^{1+\delta}\) and \(Y\geq Y_0(\delta)\),

\[
 \Psi(Y,z)\leq Y\exp\{-u\log u\,(1+o(1))\},\qquad
 u={\log Y\over\log z}.                                      \tag{24.16}
\]

In particular, throughout that range and for large \(Y\), the right side is
at most \(Y\exp\{-\tfrac12u\log u\}\).  We also use

\[
 \sum_{a\leq Y}\tau(a^2)^2\ll Y(\log(2Y))^8.                \tag{24.17}
\]

The latter follows directly from the Euler product: its prime coefficient is
\(\tau(p^2)^2=9\), so after extracting \(\zeta(s)^9\) the remaining product
converges absolutely to the right of \(1/2\); the usual convolution bound
suffices.  On a dyadic block \(Y/2<M\leq Y\), Lemma 18.1 and
Cauchy--Schwarz give

\[
 \sum_{\substack{Y/2<M\leq Y\\P^+(M)\leq z}}{F(M)\over M}
 \ll (\log(2Y))^4\{\Psi(Y,z)/Y\}^{1/2}.                     \tag{24.18}
\]

Put \(T_0=C_B(\log L)^2/\log\log L\).  The contribution of
\(M\leq e^{T_0}\) is \(O(T_0^3)=o(L^3)\) by the upper half of Theorem 18.2.
For a surviving block write \(t=\log Y\geq T_0\) and enlarge the smoothness
threshold monotonically to
\[
 y_*:=\max\{L^B,t^2\}\geq z,\qquad u_*={t\over\log y_*}.
\]
For these surviving blocks, \(t\geq T_0\) gives \(L^B\leq Y\), and
\(t^2\leq Y\) for large \(X\); hence \(y_*\leq Y\).  Also
\(y_*\geq(\log Y)^2\), so (24.16) applies with \(\delta=1\).  If
\(t^2\leq L^B\), then \(y_*=L^B\), and, for large \(X\),
\[
 \log u_* = \log t-\log(B\log L)\geq\tfrac12\log\log L,
 \qquad
 u_*\log u_*\geq {C_B\over2B}\log L.                       \tag{24.18a}
\]
Indeed the first inequality follows from
\(t\geq C_B(\log L)^2/\log\log L\).  If instead \(t^2>L^B\), then
\(y_*=t^2\), and
\[
 u_*\log u_*={t\over2\log t}
      \log\!\left({t\over2\log t}\right)
 \geq {t\over4}>{L^{B/2}\over4}\gg_B\log L.               \tag{24.18b}
\]
By smoothness monotonicity, \(\Psi(Y,z)\leq\Psi(Y,y_*)\).  Thus (24.16)
and (24.18) bound every surviving block by
\[
 \ll t^4\exp\{-\tfrac14u_*\log u_*\}\leq L^{-2}
\]
once \(C_B>48B\) is chosen sufficiently large (and then \(X\) is large).
There are \(O(L)\) blocks, whose total is \(O(L^{-1})\); together with the
initial contribution this proves (24.15). ∎

For each odd prime \(p\leq z\), consider the local condition

\[
 \left({n\over p}\right)\in\{0,+1\}.                        \tag{24.19}
\]

It has density \((p+1)/(2p)\).  Imposing (24.19) independently for all such
primes costs

\[
 \sigma_z=\prod_{3\leq p\leq z}{p+1\over2p},\qquad
 -\log\sigma_z=(\log2)\pi(z)+O(\log\log z).                 \tag{24.20}
\]

It certifies avoidance of every intrinsic class for every \(z\)-smooth
modulus: if \((n,M)=1\), then \((n/M)=+1\), and otherwise its Jacobi symbol
is zero, while Lemma 21.2 requires \(-1\).

**Theorem 24.7 (local-symbol plus first-moment no-go; proved in the stated
method class).**  Consider a lower-bound scheme which

1. imposes (24.19) for every odd prime up to a cutoff \(z\), to certify
   the moduli composed entirely of those controlled primes; and
2. treats every modulus not so certified by the unconditioned first-moment
   union bound \(\sum F(M)/M\).

If the prescription density is \(\exp\{-o(L^3)\}\), then the second step
retains \((1-o(1))\) of the cubic mass and gives no positive lower bound.
Thus no scheme in this class can refute H_PF.

*Proof.*  By (24.20), subcubic prescription cost implies
\(\pi(z)=o(L^3)\).  Since \(\pi(L^4)\gg L^3\), this gives \(z\leq L^4\)
for large \(X\).  Applying the repaired Lemma 24.6 with \(B=4\), and then
Theorem 18.2, gives

\[
 \sum_{\substack{M\leq X,\ M\equiv3\ (4)\\P^+(M)>z}}
       {F(M)\over M}
 =\sum_{\substack{M\leq X\\M\equiv3\ (4)}}{F(M)\over M}
      -o(L^3)\gg L^3.                                       \tag{24.21}
\]

The union-bound lower estimate after step 2 is therefore already negative. ∎

The scope is essential.  The theorem does not cover a prescription which
uses the actual residues of rough-modulus classes to make many of them
incompatible, nor a clustered estimate of their conditional union.  Either
would be new joint arithmetic, not the ``certify smooth, union-bound the
rest'' method ruled out here.

### 24.5 A joint construction for a growing fiber range

The \(D=1\) construction does tensor across many shifts, but only after one
keeps the exact dependence on \(R\).  Define

\[
 {\rm Av}^{(R\leq Y)}_X(N)=
 \{n\leq N:\text{no pair in (21.3) has }R_0(D)\leq Y\}.      \tag{24.22}
\]

This is a genuine part of the complete composite-modulus system, not only a
prime-modulus slice.

**Theorem 24.8 (multi-shift prime-class certificate construction; proved).**  Fix
\(\epsilon>0\).  Uniformly for sufficiently large \(X\),
\(1\leq Y\leq L^{3-\epsilon}\), and \(\log N\geq L^4\),

\[
 |{\rm Av}^{(R\leq Y)}_X(N)|
 \geq N\exp\{-C_\epsilon Y\log(2Y)\log L\}.                 \tag{24.23}
\]

The corresponding natural density satisfies the same lower bound.  In
particular, taking \(Y=L^{3-\epsilon}\) makes the exponent \(o(L^3)\).

*Proof.*  Let

\[
 \mathcal D_Y=\{(R,D):R\leq Y,\ D=R^2/s,\ s\mid\operatorname{rad}(R)\},
 \qquad H=|\mathcal D_Y|.
\]

The standard Euler-product estimate
\(\sum_{R\leq Y}2^{\omega(R)}\ll Y\log(2Y)\) gives
\(H\ll Y\log(2Y)\).  For each prime \(p\leq X\),
\(p\equiv3\pmod4\), forbid

\[
 B_p=\{-4D\pmod p:(R,D)\in\mathcal D_Y,\ p\nmid R\}.        \tag{24.24}
\]

Every element of \(B_p\) is nonzero, so
\(g(p):=|B_p|\leq\min(H,p-1)\); at least the residue zero is always
available.

Any integer avoiding all the sets (24.24) belongs to (24.22).  Indeed, a
putative hit has \(M\mid n+4D\) and \(M\equiv-1\pmod {4R}\).  Thus
\((M,R)=1\), and because \(M\equiv3\pmod4\), some prime
\(p\equiv3\pmod4\) divides \(M\) to odd exponent.  This prime is at most
\(X\), does not divide \(R\), and forces \(n\equiv-4D\pmod p\), contrary
to (24.24).

It remains to count this certificate in a short fraction of its enormous
period.  For the primes \(p\leq2H\), choose the allowed residue
\(n\equiv0\pmod p\), and let \(Q_0\) be their product.  Chebyshev's bound
gives \(\log Q_0=O(H)\).  Write \(n=Q_0m\).  At every remaining prime,
the transformed forbidden set still has size \(g(p)\leq H<p/2\), and

\[
 \mu_Y:=\sum_{2H<p\leq X}{g(p)\over p}
       \ll H\log L.                                         \tag{24.25}
\]

Odd Bonferroni truncation at degree \(r\asymp\mu_Y\), as in (24.10), leaves
at least a fixed fraction of the Euler product, which is
\(\geq\exp(-2\mu_Y)\).  If
\(W_Y=\sum g(p)\), then \(W_Y\leq H\pi(X)\), so all congruence-count
rounding errors total

\[
 \exp\{O(r\log W_Y)\}=\exp\{O(HL\log L)\}.                  \tag{24.26}
\]

For \(Y\leq L^{3-\epsilon}\), the exponent in (24.26) is \(o(L^4)\), and
so (24.26) is negligible against \(N/Q_0\) under the stated hypothesis.
Restoring the cost of \(Q_0\) proves (24.23).  Letting \(N\) run through
full periods gives the density statement directly. ∎

**Assessment 24.9 (what the construction does and does not do).**  Theorem
24.8 is a joint clustering lower bound for all \(2^{\omega(R)}\) shifts in
a growing, composite-modulus fiber range.  It is strictly stronger than the
single \(D=1\) cluster and reaches every \(R\leq L^{3-\epsilon}\) at
subcubic cost.  It does not approach the full range \(R\leq X/4\).  In the
proof, \(H\) is the number of shifts; extending the same certificate makes
both the local cost \(H\log L\) and the finite-interval rounding exponent
\(HL\log L\) exceed their budgets.  For the full range many sets \(B_p\)
are expected to contain every nonzero residue, reducing the construction to
primorial divisibility at exponential-in-\(X\) cost.

Other attempted continuations fail at equally explicit points:

* Treating the \((R,s)\) events independently assumes the false uniformity
  exposed by (24.5).
* Direct Bonferroni over all composite congruence classes has
  \(\exp\{\Theta(L^3)\}\) main degree but an uncontrolled number of residue
  intersections; the prime factorization in (24.24) is what makes the
  truncated range countable.
* The smooth Jacobi certificate leaves the cubic rough-modulus mass (24.21).
* This cutoff assessment, and the corresponding fixed-power gap description
  in Assessment 24.10, are superseded by Theorem 27.1: the same certificate's
  sharp bookkeeping reaches \(Y=L^3/(\log L)^{2+\eta}=L^{3-o(1)}\) while
  preserving both budgets.  It still does not approach the full range
  \(R\leq X/4\).

### 24.6 Verdict after wave 7

**Assessment 24.10.**  H_PF remains **false-looking, open**.  (H_PF as stated
is refuted — see §31; the critical-window variant \(H_{\rm PF}'\) below
remains open.)  The status did not change to a refutation: Theorem 24.8
concerns a proper subsystem, and
Theorem 24.4 goes in the wrong inclusion direction for lower-bounding the
full avoiders.  What did change is the map of the gap.

* The prime subsystem is now pinned at \(\exp\{-\Theta(L^2)\}\) on finite
  intervals when \(\log N\geq C_3L^3\), and with no restriction for natural
  density; composite moduli must supply every additional power needed by
  H_PF.
* The initial-cutoff Jacobi prescription followed by an unconditioned first
  moment is closed by Theorem 24.7; other local prescriptions are not.
* Joint clustering is proved through \(R\leq L^{3-\epsilon}\) for every
  fixed \(\epsilon>0\), but fibers with \(R\) beyond \(L^{3-\epsilon}\) for
  every fixed \(\epsilon\) are exactly where the argument loses control.
* The subset-product mechanism supplies the \(L^{2+\log2}\) uniform-model
  benchmark.  Its premise fails the boundary check, so it is a toy-model
  output, not an evidence-backed scale; existing data cannot distinguish it
  from \(L^2\log L\).

A refutation still requires
\(|{\rm Av}_X(N)|\geq N\exp\{-o(L^3)\}\) for the **joint full system** in
the \(\log N\asymp L^4\) regime.  The named missing input is now a
large-\(R\), multi-shift divisor-clustering lower bound, not more prime-slice
sieve mass and not a one-modulus symbol certificate.  This requirement
survives only for the stronger critical-window route \(H_{\rm PF}'\), not for
the now-complete refutation of H_PF as stated; see §31.  Section 27 later
sharpens the cutoff to \(L^{3-o(1)}\) and refines the missing input.

---

## 25. Sub-maximal transfer maps: the eleven pure-tensor resisters fall to additive maps

This section starts from the eleven primes (23.14), not from the six older
§22 blockers.  It closes the requested finite anatomy, examines the alive
sub-maximal moduli in Theorem 22.1, and extends the exact pure-tensor census
to one million.  The main positive result is not the initially proposed
shifted-factor map.  Four primes do fall to that map, but a simpler fixed
**degree-one** map at the gcd modulus reaches all eleven.  This is a genuine
non-pure escape from Lemma 23.9's 2-adic invariant.  It is still diagnostic,
not an Erdős--Straus proof: its inverse construction begins with a target
Type-II tuple.

### 25.1 Complete anatomy of the eleven targets

For a target row put

\[
 R=CK,\qquad F_A=4ACK-1,\qquad F_B=4BCK-1.
\]

Then

\[
                  F_AF_B=4PCK^2+1.                           \tag{25.1}
\]

The tables report \(R\), the two parity inputs in Lemma 23.6, the coordinate
gcd, and the complete prime factorizations of the shifted factors.  Rows are
ordered.  Here are the complete lists for the first three primes.

| \(P\) | \((A,B,C,K)\) | \(CK\) | \(v_2(C)\) | \(v_2(A+B)\) | \(\gcd(A,B)\) | \(F_A\) | \(F_B\) |
|---:|---|---:|---:|---:|---:|---|---|
|73|(1,20,1,3)|3|0|0|1|11|239|
|73|(1,21,1,2)|2|0|1|1|7|167|
|73|(2,5,2,1)|2|1|0|1|\(3\cdot5\)|\(3\cdot13\)|
|73|(5,2,2,1)|2|1|0|1|\(3\cdot13\)|\(3\cdot5\)|
|73|(20,1,1,3)|3|0|0|1|239|11|
|73|(21,1,1,2)|2|0|1|1|167|7|
|193|(2,5,5,1)|5|0|0|1|\(3\cdot13\)|\(3^2\cdot11\)|
|193|(2,13,2,1)|2|1|0|1|\(3\cdot5\)|103|
|193|(5,2,5,1)|5|0|0|1|\(3^2\cdot11\)|\(3\cdot13\)|
|193|(13,2,2,1)|2|1|0|1|103|\(3\cdot5\)|
|241|(1,21,3,2)|6|0|1|1|23|503|
|241|(1,22,3,1)|3|0|0|1|11|263|
|241|(1,62,1,9)|9|0|0|1|\(5\cdot7\)|\(23\cdot97\)|
|241|(1,69,1,2)|2|0|1|1|7|\(19\cdot29\)|
|241|(21,1,3,2)|6|0|1|1|503|23|
|241|(22,1,3,1)|3|0|0|1|263|11|
|241|(62,1,1,9)|9|0|0|1|\(23\cdot97\)|\(5\cdot7\)|
|241|(69,1,1,2)|2|0|1|1|\(19\cdot29\)|7|

For the remaining primes every row occurs with its coordinate swap.  The
following table is therefore still the complete list: “+ swap” adds
\((B,A,C,K)\), swaps \(F_A,F_B\), and leaves every other displayed datum
unchanged.

| \(P\) | representative \((A,B,C,K)\) | \(CK\) | \(v_2(C)\) | \(v_2(A+B)\) | \(\gcd(A,B)\) | \(F_A\) | \(F_B\) |
|---:|---|---:|---:|---:|---:|---|---|
|673|(1,34,5,5) + swap|25|0|0|1|\(3^2\cdot11\)|\(3\cdot11\cdot103\)|
|673|(2,5,17,1) + swap|17|0|0|1|\(3^3\cdot5\)|\(3\cdot113\)|
|673|(2,43,2,3) + swap|6|1|0|1|47|1031|
|673|(2,45,2,1) + swap|2|1|0|1|\(3\cdot5\)|359|
|673|(3,19,3,2) + swap|6|0|1|1|71|\(5\cdot7\cdot13\)|
|1129|(1,285,1,26) + swap|26|0|1|1|103|\(107\cdot277\)|
|1129|(1,308,1,3) + swap|3|0|0|1|11|\(5\cdot739\)|
|1129|(2,13,11,1) + swap|11|0|0|1|\(3\cdot29\)|571|
|1129|(2,29,5,1) + swap|5|0|0|1|\(3\cdot13\)|\(3\cdot193\)|
|1129|(3,19,5,2) + swap|10|0|1|1|\(7\cdot17\)|\(3\cdot11\cdot23\)|
|1153|(1,17,17,6) + swap|102|0|1|1|\(11\cdot37\)|\(5\cdot19\cdot73\)|
|1153|(2,5,29,1) + swap|29|0|0|1|\(3\cdot7\cdot11\)|\(3\cdot193\)|
|1153|(2,21,7,1) + swap|7|0|0|1|\(5\cdot11\)|587|
|1153|(2,73,2,5) + swap|10|1|0|1|79|\(3\cdot7\cdot139\)|
|1153|(2,77,2,1) + swap|2|1|0|1|\(3\cdot5\)|\(3\cdot5\cdot41\)|
|1153|(2,145,1,21) + swap|21|0|0|1|167|\(19\cdot641\)|
|1153|(2,165,1,1) + swap|1|0|0|1|7|659|
|1153|(5,58,1,9) + swap|9|0|0|1|179|2087|
|2473|(1,20,31,3) + swap|93|0|0|1|\(7\cdot53\)|\(43\cdot173\)|
|2473|(1,62,10,9) + swap|90|1|0|1|359|\(11\cdot2029\)|
|2473|(1,209,3,6) + swap|18|0|1|1|71|\(41\cdot367\)|
|2473|(1,212,3,3) + swap|9|0|0|1|\(5\cdot7\)|\(13\cdot587\)|
|2473|(2,5,62,1) + swap|62|1|0|1|\(3^2\cdot5\cdot11\)|\(3\cdot7\cdot59\)|
|2473|(2,45,7,1) + swap|7|0|0|1|\(5\cdot11\)|1259|
|2473|(2,165,2,1) + swap|2|1|0|1|\(3\cdot5\)|1319|
|2473|(4,31,5,5) + swap|25|0|0|1|\(3\cdot7\cdot19\)|\(3\cdot1033\)|
|2473|(5,42,3,1) + swap|3|0|0|1|59|503|
|2521|(2,29,11,1) + swap|11|0|0|1|\(3\cdot29\)|\(3\cdot5^2\cdot17\)|
|2521|(2,159,2,7) + swap|14|1|0|1|\(3\cdot37\)|\(29\cdot307\)|
|2521|(4,161,1,3) + swap|3|0|0|1|47|1931|
|3169|(1,114,7,5) + swap|35|0|0|1|139|15959|
|3169|(1,797,1,42) + swap|42|0|1|1|167|\(5\cdot61\cdot439\)|
|3169|(1,834,1,5) + swap|5|0|0|1|19|\(13\cdot1283\)|
|3169|(2,21,19,1) + swap|19|0|0|1|151|\(5\cdot11\cdot29\)|
|3169|(2,397,1,57) + swap|57|0|0|1|\(5\cdot7\cdot13\)|\(5\cdot43\cdot421\)|
|3169|(2,453,1,1) + swap|1|0|0|1|7|1811|
|3361|(1,29,29,10) + swap|290|0|1|1|\(19\cdot61\)|\(3\cdot11213\)|
|3361|(5,34,5,1) + swap|5|0|0|1|\(3^2\cdot11\)|\(7\cdot97\)|
|5281|(1,21,63,2) + swap|126|0|1|1|503|\(19\cdot557\)|
|5281|(1,38,35,1) + swap|35|0|0|1|139|\(3^3\cdot197\)|
|5281|(1,265,5,14) + swap|70|0|1|1|\(3^2\cdot31\)|\(3\cdot24733\)|
|5281|(1,278,5,1) + swap|5|0|0|1|19|\(3\cdot17\cdot109\)|
|5281|(1,1322,1,189) + swap|189|0|0|1|\(5\cdot151\)|999431|
|5281|(1,1329,1,38) + swap|38|0|1|1|151|\(13\cdot41\cdot379\)|
|5281|(1,1358,1,9) + swap|9|0|0|1|\(5\cdot7\)|\(19\cdot31\cdot83\)|
|5281|(1,1509,1,2) + swap|2|0|1|1|7|12071|
|5281|(3,63,7,6) + swap|42|0|1|3|503|\(19\cdot557\)|
|5281|(6,17,13,1) + swap|13|0|0|1|311|883|
|5281|(13,102,1,5) + swap|5|0|0|1|\(7\cdot37\)|2039|

**Computational Search 25.1 (exact finite anatomy).**  Enumeration by
(23.8), independently recast in Lemma 25.8 below, gives

\[
\begin{array}{c|rrrrrrrrrrr}
P&73&193&241&673&1129&1153&2473&2521&3169&3361&5281\\ \hline
\#\text{ ordered rows}&6&4&8&10&10&16&18&6&12&4&22\\
\#\text{ distinct }CK&2&2&4&4&5&8&9&3&6&2&10.
\end{array}                                                  \tag{25.2}
\]

There are 116 ordered rows in all.  Every row has
\(v_2(C)+v_2(A+B)\leq1\), as required by Lemma 23.6.  Every coordinate gcd
is odd; the only non-unit gcd is 3 on the two \((3,63,7,6)\) rows for 5281.
Thus the anatomy rechecks every input to Corollary 23.9.1 rather than merely
rechecking its row counts.  `verify.py (x)` hard-codes all 116 rows and every displayed anatomy cell,
including the expected factor dictionaries, and audits (25.1) and both
counts in (25.2).

### 25.2 What the sub-maximal coefficient spaces actually say

At \(M=h_1\), divide (22.4) by \(h_1\).  One output coordinate has the exact
form

\[
\begin{split}
 A'={}&\alpha a_1+\beta b_1
 +h_1(\alpha_{20}a_1^2+\alpha_{11}a_1b_1+\alpha_{02}b_1^2)\\
 &+h_2(\lambda_{aa}a_1a_2+\lambda_{ab}a_1b_2
       +\lambda_{ba}b_1a_2+\lambda_{bb}b_1b_2),              \tag{25.3}
\end{split}
\]

with nine arbitrary integer coefficients; \(B'\) has an independent copy.
The output reading has \(4C'K'=h_1\).  At \(M=g=(h_1,h_2)\), write
\(h_i=gr_i\).  The 14 generators after division by \(g\) are the four
linear values

\[
 r_1a_1,
 r_1b_1,
 r_2a_2,
 r_2b_2                             \tag{25.4}
\]

and the ten values obtained by multiplying by \(g\) each degree-two
monomial in these four weighted linear values.  Thus the original quadratic
generators retain their \(r_i\)-weights.  This is the concrete coordinate
form of the 9 and 14 entries in (22.6).

**Lemma 25.2 (proved: pointwise-expressivity lattice).**  At a fixed source
pair, the set of integers represented by one coordinate of (25.3), as its
coefficients vary, is \((a_1,b_1)\mathbb Z\).  At \(M=g\), the corresponding
set is

\[
 \delta\mathbb Z,
 \quad \delta=(r_1a_1,r_1b_1,r_2a_2,r_2b_2).                \tag{25.5}
\]

In particular, a coprime first source makes the \(h_1\) coordinate
pointwise arbitrary.  If both source pairs are coprime, then (25.5) is
\(\mathbb Z\), because \((r_1,r_2)=1\).

*Proof.*  The two linear generators in (25.3) generate
\((a_1,b_1)\mathbb Z\); every quadratic generator is already a multiple of
one of them.  The same argument reduces the gcd of all 14 evaluated
\(g\)-generators to the gcd of the four linear values in (25.4).  Coprimality
then gives the last two statements. ∎

**Lemma 25.3 (proved: target-dependent degeneracy at \(h_1\)).**  Let
\((A,B,C,K)\) be any Type-II tuple and let a source tuple
\((a_1,b_1,c_1,k_1)\) have \((a_1,b_1)=1\) and \(c_1k_1=CK\).  There are
integer coefficient pairs in (25.3) whose selected output is exactly
\((A,B,C,K)\); the second source is unnecessary.  Consequently, allowing a
fresh coefficient choice at each target reduces “reachability” to the bare
condition that \(CK\) occur as \(c_1k_1\) for a smaller source.

*Proof.*  Bézout gives independent \(\alpha,\beta\) representing \(A\) and
\(B\); set all quadratic coefficients to zero.  Then
\(h_1=4c_1k_1=4CK\), and reading at the target \((C,K)\) gives its two
shifted factors. ∎

The lemma concerns positivity at the selected point.  Signed Bézout
coefficients need not define a map positive on the whole orthant.  More
importantly, its coefficients depend on \((A,B)\).  It is therefore not one
fixed universal descent map and cannot support an induction.

**Computational Search 25.4 (exact pointwise-degeneracy test).**  Every one
of the 116 resister rows passes the bare smaller-source test for the explicit
reason

\[
 (p_1;a_1,b_1,c_1,k_1)=(4CK-2;1,1,CK,1),
 \qquad 2\leq p_1<P.                                      \tag{25.6}
\]

Thus the hit counts equal the row counts in (25.2).  This is the sharp
warning: free coefficients erase all target structure on precisely the data
where fixed coefficients matter.

### 25.3 Fixed maps: four shifted hits, then an additive sweep

Consider first the requested finite shifted box

\[
 A=a_1(1+n h_2z_2),\qquad B=b_1(1+m h_2w_2),                \tag{25.7}
\]

where \((z_2,w_2)=(a_2,b_2)\) or \((b_2,a_2)\) and
\(n,m\in\{1,2,3\}\).  These are the maps
\(u_1+n u_1u_2\), \(v_1+m v_1v_2\), or their swapped cross-pairing,
written after division by \(h_1\).  Coefficients \(-1,-2,-3\) on the cross term cannot hit a positive
coordinate: \(1-nh_2z_2\leq-3\).

The inverse is exact and finite.  Choose \(a_1\mid A,b_1\mid B\); then

\[
 {A/a_1-1\over4n}=c_2k_2z_2,
 \qquad {B/b_1-1\over4m}=c_2k_2w_2.                         \tag{25.8}
\]

Hence \(c_2k_2\) divides the gcd of the two displayed integers.  Splitting
it and \(CK=c_1k_1\), checking the two source divisibilities, and checking
\(2\leq p_i<P\) exhausts the family.

**Computational Search 25.5 (exact shifted-box inverse).**

\[
\begin{array}{c|rrrrrrrrrrr}
P&73&193&241&673&1129&1153&2473&2521&3169&3361&5281\\ \hline
\#\text{ hit ordered rows}&0&0&0&0&0&2&2&0&0&2&2\\
\#\text{ branches}&0&0&0&0&0&8&8&0&0&8&16.
\end{array}                                                  \tag{25.9}
\]

The base map \(n=m=1\), without coefficient 2 or 3, already supplies one
aligned branch for each hit prime:

\[
\begin{array}{r|c|c|c}
P&(A,B,C,K)&(p_1;a_1,b_1,c_1,k_1)&(p_2;a_2,b_2,c_2,k_2)\\ \hline
1153&(5,58,1,9)&(69;1,2,9,1)&(20;1,7,1,1)\\
2473&(5,42,3,1)&(21;1,2,3,1)&(14;1,5,1,1)\\
3361&(5,34,5,1)&(37;1,2,5,1)&(11;1,4,1,1)\\
5281&(13,102,1,5)&(113;1,6,5,1)&(41;3,4,1,1).
\end{array}                                                  \tag{25.10}
\]

All source identities and output coordinates are replayed end to end in
`verify.py (x)`; the target shifted factors are separately checked against
the hard-coded anatomy table.  The seven other primes resist this stated finite box.
There is no common mod-8 obstruction: four rows pass and the failures occur
at the compatible shifted-divisor step (25.8).  No claim is made for
coefficients outside \(\{\pm1,\pm2,\pm3\}\) or for general combinations of
the nine basis monomials.

The gcd modulus contains a much simpler family.  Define three fixed
coefficient pairs

\[
\begin{aligned}
 \Phi_{++}&=(-1+u_1+u_2,\;-1+v_1+v_2),\\
 \Phi_{1+}&=(-1+u_1,\;-1+v_1+v_2),\\
 \Phi_{+1}&=(-1+u_1+u_2,\;-1+v_1).                          \tag{25.11}
\end{aligned}
\]

These are degree one, have nonnegative coefficients, and are universally
\(-1\pmod g\).

**Theorem 25.6 (proved: fixed additive descent on the \(k=1\) slice).**  Let
\((A,B,C,1)\) be a Type-II tuple for \(P\), with
\((A,B)\ne(1,1)\).  One of the three fixed maps (25.11), at equal source
moduli \(h_1=h_2=g=4C\), outputs this tuple from two explicit source tuples
of values in \([2,P)\).

If \(A,B\geq2\), use \(\Phi_{++}\) and

\[
 (a_1,b_1,c_1,k_1)=(1,1,C,1),\qquad
 (a_2,b_2,c_2,k_2)=(A-1,B-1,C,1).                           \tag{25.12}
\]

If \(A=1<B\), use \(\Phi_{1+}\) with sources
\((1,1,C,1),(1,B-1,C,1)\); the case \(B=1<A\) is symmetric.

*Proof.*  Dividing (25.11) by \(g\) gives respectively coordinate sums or a
copied coordinate and a sum, so the output coordinates are exactly
\((A,B)\).  The common output modulus is \(4C\), and the \((C,1)\) reading
gives \(P\).  Every source is a positive Type-II tuple.  In the first case,
\(p_1=4C-2\), while

\[
 P-p_1=4C(AB-1)-A-B+2>0,
 \qquad P-p_2=4C(A+B-1)-2>0;
\]

the first inequality uses \(A,B\geq2\).  In the boundary case,
\(p_1=4C-2\), \(p_2=4C(B-1)-B\), and

\[
 P-p_1=4C(B-1)-B+1=p_2+1>0,
 \qquad P-p_2=4C-1>0.
\]

Positivity follows from \(4xy-x-y\geq2xy\) for positive \(x,y\). ∎

**Corollary 25.6.1 (proved, with finite target audit).**  Every prime in
(23.14) is a descending image of one of the three fixed maps (25.11).  One
\(k=1\) row and the resulting sources are:

\[
\begin{array}{r|c|r|r}
P&(A,B,C,1)&p_1&p_2\\ \hline
73&(2,5,2,1)&6&27\\
193&(2,5,5,1)&18&75\\
241&(1,22,3,1)&10&230\\
673&(2,5,17,1)&66&267\\
1129&(2,13,11,1)&42&515\\
1153&(2,5,29,1)&114&459\\
2473&(2,5,62,1)&246&987\\
2521&(2,29,11,1)&42&1203\\
3169&(2,21,19,1)&74&1499\\
3361&(5,34,5,1)&18&2603\\
5281&(6,17,13,1)&50&4139.
\end{array}                                                  \tag{25.13}
\]

This explains exactly how non-pure maps shed the tensor's 2-adic weight:
they add centered factors at modulus \(g\) instead of multiplying them at a
modulus carrying \(v_2\geq4\).  All eleven lie in the descending image of the degree-one \(M=g\) subfamily
of Theorem 22.1; their resistance was only to pure tensors.

**Assessment 25.7 (the proposed finite-family non-cofiniteness theorem is
not established).**  The residue-1 proof of Theorem 20.3 does not extend to
(25.11).  Its modulus \(g=4C\) varies with the source, so there is no finite
lcm of fixed output progressions.  More decisively, Theorem 25.6 says that
the image of just three fixed maps already contains **every hard prime that
has a \(k=1\) Type-II tuple**.  Proving that this image is not cofinite would
therefore require, at minimum, proving infinitely many hard primes lack such
a tuple.  Only six finite examples below \(10^5\) are known (§19.3), and the
pure tensor family reaches all six after flexible reading (§23).

Thus no degree-two ceiling theorem was proved.  The combined fixed
coefficient maps plus §23's reading schema cover every census prime through
\(10^6\) below.  They remain useless against a least counterexample: choosing
the \((A,B,C,K)\) to invert has already asserted the witness.  The exact
honest ceiling obtained here is **witness decomposition, not witness
existence**.  A residue-escape claim for arbitrary finite maps that ignores
this circularity would be false as an argument and currently unproved as a
statement.

### 25.4 Exact census through \(10^6\)

**Lemma 25.8 (proved: one-candidate tuple enumeration).**  Fix odd \(P\) and
positive \(A,B\) with \(AB\leq P/2\).  Put

\[
 C=\left\lfloor{P\over4AB}\right\rfloor+1,
 \qquad q=4ABC-P.                                           \tag{25.14}
\]

There is a Type-II row with these \(A,B\) if and only if
\(q\mid A+B\); then it is unique and \(K=(A+B)/q\).

*Proof.*  In any row, \(q=(A+B)/K\) is positive and at most \(A+B\leq2AB\).
Hence \(0<q/(4AB)\leq1/2\), forcing the unique integer (25.14).  The stated
divisibility is then exactly the condition that \(K\) be integral. ∎

This removes the divisor loop in (23.8).  The scan first tests
\(A\in\{1,2,3\}\) and \(B\leq3000\), checking the fixed-source-2 inverse
immediately.  Only 407 of 9,732 primes survive that fast phase at one
million.  For each survivor it exhausts all \(A\leq B\) with
\(AB\leq P/2\), adding the swapped row; memory is linear in one target's
row list and there is no Cartesian array.  Every claimed failure is
therefore exhaustive.

**Computational Search 25.9 (exact finite census).**

\[
\begin{array}{c|r|r|r|r|l}
\text{range}&\#P&\exists(4\mid CK)&\text{pure descending inverse}
 &\text{fixed source 2}&\text{non-fixed-source exceptions}\\ \hline
P\leq20000&267&256&256&253&601,5881,9049\\
P\leq10^6&9732&9721&9721&9717&601,5881,9049,20641.
\end{array}                                                  \tag{25.15}
\]

In both rows the complete no-\(4\mid CK\) list is exactly (23.14).  There
are **no new pure-tensor resisters through \(10^6\)**.  Adding (25.11)
reaches those eleven through their \(k=1\) rows, so the combined diagnosed
image contains all 9,732 census primes.  This is a finite computational
coverage statement, not forward-image totality for unknown primes.

`verify.py (x)` replays the \(P\leq20000\) row by default.  With
`ES_FULL_SCAN=1` it replays the complete one-million row, including the 407
fast-phase survivors.  One recorded environment-specific run used about 85
seconds and 63 MiB peak memory; these figures are measurements, not bounds.
The default block takes well below 15 seconds.

### 25.5 Rational and quotient readings

There is one clean witness-division law, but its extra hypothesis is on the
witness coordinate rather than on the output integer alone.

**Lemma 25.10 (proved: exact coordinate-supported witness division).**  If
\((A,B,C,K)\) is a Type-II tuple for \(P=tP''\) and \(t\mid C\), then

\[
             (A,B,C/t,tK)                                   \tag{25.16}
\]

is a Type-II tuple for \(P''\).

*Proof.*  Since \(t\mid C,P\), the identity
\(A+B=K(4ABC-P)\) shows \(tK\mid A+B\).  Dividing
\(P=4ABC-(A+B)/K\) by \(t\) gives (25.16).  Equivalently, (25.16) preserves
both shifted factors because \((C/t)(tK)=CK\). ∎

For example, \((6;1,1,2,1)\) divides by 2 to
\((3;1,1,1,2)\).  Divisibility \(t\mid P\) alone gives no such law.  If the
same old factor pair is to witness \(P''\) at some \((C'',K'')\), the exact
necessary norm condition is

\[
 C''K''^2=tCK^2,                                             \tag{25.17}
\]

and both old factors must additionally be \(-1\pmod{4C''K''}\).  Neither
condition follows from \(t\mid P\).  For
\((6;1,1,2,1)\) and \(t=3\), the old pair is \(7\cdot7\); (25.17) forces
the candidate modulus 24, but 7 is not \(-1\pmod{24}\).  The quotient 2
has its own tuple, not one inherited from that factor pair.

If \(d\mid(A,B)\), replacing \((A,B)\) by \((A/d,B/d)\) while multiplying
the factor modulus by \(d\) is exactly an arbitrary-modulus reading of the
same factor pair.  For pure tensors it is already covered, including its
2-adic obstruction, by Lemma 23.9.  For non-pure factor pairs the tensor
identity (23.18) is absent; (25.11) demonstrates that such maps can evade it,
but the quotient itself adds no new transfer mechanism.

**Assessment 25.11 (rational pass).**  No general law turning a witness of
\(tP\) into one of \(P\) was found beyond Lemma 25.10 and existing modulus
readings.  The obstruction is precise: divisibility of the integer does not
supply either the new shifted norm (25.17) or the stronger factor
congruences.  No genuinely new rational totality candidate emerged.

### 25.6 Outcome and failure log

**Assessment 25.12.**

* The complete target anatomy has 116 rows.  Free \(h_1\)-coefficients hit
  every one, but only by choosing coefficients from the target; this is the
  exact degeneracy, not a descent theorem.
* The finite shifted-factor box is genuinely active: 1153, 2473, 3361, and
  5281 fall; 73, 193, 241, 673, 1129, 2521, and 3169 resist that box.
* The simpler fixed additive gcd-modulus family then reaches all eleven.
  It proves decomposition of every \(k=1\) tuple, not existence of one.
* The pure-tensor resister set stays exactly the same eleven through
  \(10^6\); no new target anatomy is needed.  The augmented diagnosed image
  has no survivor in that finite range.
* The attempted finite-family noncofiniteness theorem fails at its proof
  route: source-dependent moduli defeat the fixed-lcm escape, and (25.11)
  already contains the full \(k=1\) witness set.  No noncofiniteness theorem
  is claimed.
* Witness division works when the divisor is supported in \(C\).  Mere
  divisibility of \(P\), general rational maps, and a forward construction
  of the target tuple remain open.  No Erdős--Straus proof results.

## 26. Type-I transfer theory: a corrected binary tensor and a cross-type bridge

Sections 20, 22 and 23 used only Type II.  This section develops the Type-I
side from the equation

\[
 p(a+b)=k(4abc-1),\qquad m=(a+b)/k,
 \qquad pm=4abc-1.                                           \tag{26.1}
\]

Unless a bijection is explicitly asserted, a **Type-I tuple** below means any
positive quadruple satisfying (26.1); \((a,b)=1\) is not required.  Such a
tuple gives the identity in Theorem 17.1(ii) even for a composite value of
\(p\).  The §23 base census is replayed independently in `verify.py (v)`.
`verify.py (y)` replays the Type-I computations, the full inverse (26.17),
the six-prime increment, and the final set arithmetic.

### 26.1 Divisor form and complete finite enumeration

**Theorem 26.1 (proved: exact Type-I divisor form).**  Let \(p\) be an odd
prime and put \(h=4ck\).  Positive \((a,b,c,k)\) satisfy (26.1) if and only if

\[
 (ha-p)(hb-p)=p^2+4ck^2,                                    \tag{26.2}
\]

with both displayed factors positive.  Every such tuple has
\((p,ck)=1\).  Consequently, for fixed \((c,k)\) with \((p,ck)=1\), the
ordered pairs \((a,b)\) correspond exactly to divisors

\[
 D\mid p^2+4ck^2,
 \qquad D\equiv-p\pmod {4ck},                               \tag{26.3}
\]

by

\[
 a={D+p\over4ck},\qquad
 b={{(p^2+4ck^2)/D}+p\over4ck}.                              \tag{26.4}
\]

The cofactor in (26.4) is automatically \(-p\pmod {4ck}\).  Without the
coprimality hypothesis, the exact statement requires **both** factors to be
\(-p\pmod {4ck}\); one divisor congruence alone is insufficient.

*Proof.*  Expanding the left side of (26.2) gives

\[
 16abc^2k^2-4ckp(a+b)+p^2.
\]

Equation (26.1) says \(p(a+b)=4abck-k\), so this is
\(p^2+4ck^2\).  Conversely, expansion backwards gives (26.1).  Solving
(26.1) for either variable gives

\[
 b(4ack-p)=pa+k,
 \]

and its symmetric counterpart, proving that both factors are positive.  If
\(p\mid k\), writing \(k=p\ell\) in (26.1) gives
\(a+b=\ell(4abc-1)>a+b\), a contradiction.  Thus \(p\nmid k\); reducing
(26.1) modulo \(p\) gives \(4abc\equiv1\pmod p\), so \(p\nmid abc\) and
\((p,ck)=1\).

Now \((D,h)=(p,h)=1\).  Since
\(D((p^2+4ck^2)/D)\equiv p^2\pmod h\) and \(D\equiv-p\pmod h\), multiplication
by \(D^{-1}\) makes the cofactor \(-p\pmod h\).  Equations (26.4) are therefore
positive integers and (26.2) completes the converse.  If coprimality is
removed this cancellation is invalid: \(p=3,c=1,k=3\) gives
\(p^2+4ck^2=45\), and \(D=9\equiv-3\pmod {12}\), but its cofactor \(5\) is
not \(-3\pmod {12}\).  This proves the warning. ∎

Thus the Type-I counterpart of (17.3) is

\[
 \boxed{(4ack-p)(4bck-p)=p^2+4ck^2}.                         \tag{26.5}
\]

It is a moving-grade condition: the desired divisor class is \(-p\), rather
than Type II's fixed class \(-1\).

**Lemma 26.2 (proved: complete finite enumeration).**  Every Type-I tuple of
an odd prime \(p\) satisfies

\[
             4ck\leq2p+k,
 \quad 1\leq k\leq\lfloor2p/3\rfloor,
 \quad 1\leq c\leq\left\lfloor{2p+k\over4k}\right\rfloor. \tag{26.6}
\]

Therefore the following is a complete enumeration, with no experimental
cutoff: loop over the \((c,k)\) in (26.6), discard \(p\mid ck\), factor
\(p^2+4ck^2\), and apply (26.3)--(26.4) to every positive divisor.  Filtering
\((a,b)=1\) gives exactly the canonical tuples of Theorem 17.1(ii).

*Proof.*  If \(h=4ck\leq p\), the first inequality is immediate.  If \(h>p\),
both factors in (26.2) are at least \(h-p\), so

\[
 (h-p)^2\leq p^2+4ck^2=p^2+hk.
\]

After cancellation and division by \(h>0\), this is \(h\leq2p+k\).  Since
\(c\geq1\), it gives \(3k\leq2p\), and solving it for \(c\) gives the other
bounds.  The divisor correspondence proves completeness. ∎

The case \(4ck<p\) is not treated by pretending that \(a=1\): positivity is
then \(a,b>p/(4ck)\).  The divisor loop enforces this automatically.  For
example the \(p=73\) row \((a,b,c,k)=(3,20,7,1)\) has \(4ck=28<p\) and
factors \(11\) and \(487\), on opposite sides of \(p\).

The direct small-prime reconstructions include

\[
\begin{aligned}
 {4\over7}&={1\over4}+{1\over4}+{1\over14}
       &&(1,1,2,2),\\
 {4\over17}&={1\over6}+{1\over15}+{1\over510}
       &&(2,5,3,1),\\
 {4\over73}&={1\over22}+{1\over110}+{1\over4015}
       &&(1,5,11,2).
\end{aligned}                                                \tag{26.7}
\]

For the last row, for example, \(m=3,z_0=55,d=11\), so
\(d\mid z_0^2\) and \(m\mid d+z_0\), independently matching Theorem 3.1(A).
`recorddata.json` contains only Case-B/Type-II records (its schema was
checked); there is no stored Case-A table against which to claim a larger
comparison.

### 26.2 Anatomy of the eleven Type-II tensor resisters

**Computational Search 26.3 (exact finite enumeration).**  Lemma 26.2 gives
the following complete census.  “Primitive” means \((a,b)=1\); counts are
ordered, so swapping \(a,b\) is counted.

\[
\begin{array}{r|rrrrrr}
p&\#&\#\text{ up to swap}&\#\text{ primitive}&\#m\text{ values}&\max k
 &\#(m\mid k)\\ \hline
73&8&4&8&2&4&0\\
193&8&4&8&3&10&0\\
241&10&5&8&2&3&0\\
673&26&13&24&8&34&0\\
1129&32&16&28&7&26&2\\
1153&30&15&28&9&58&0\\
2473&56&28&48&12&124&4\\
2521&12&6&12&4&11&0\\
3169&26&13&26&9&38&2\\
3361&26&13&26&9&29&0\\
5281&36&18&30&11&78&4
\end{array}                                                  \tag{26.8}
\]

Every resister therefore has Type-I structure, but not uniformly rich
structure: 73 and 193 have only four swap-pairs.  Here are the complete first
three lists.  Each line represents the displayed row and its \(a,b\) swap;
\(m=(a+b)/k\).

\[
\begin{array}{r|rrrr|r}
p&a&b&c&k&m\\ \hline
73&3&20&7&1&23\\
  &2&21&10&1&23\\
  &1&5&11&2&3\\
  &1&11&5&4&3\\ \hline
193&5&138&10&1&143\\
   &1&13&26&2&7\\
   &1&5&29&2&3\\
   &1&29&5&10&3\\ \hline
241&9&14&11&1&23\\
   &2&69&31&1&71\\
   &2&21&33&1&23\\
   &1&22&63&1&23\\
   &3&66&7&3&23
\end{array}                                                  \tag{26.9}
\]

Only the last row is nonprimitive.  As in Theorem 17.1, nonprimitive rows
still give valid identities but duplicate a canonical solution at different
\((c,k)\).

### 26.3 Brahmagupta's sign obstruction and a corrected binary law

For fixed \(c\), Brahmagupta composition gives, for \(\sigma=\pm1\),

\[
 (p_1^2+4ck_1^2)(p_2^2+4ck_2^2)
 =P_\sigma^2+4cK_\sigma^2,                                  \tag{26.10}
\]
\[
 P_\sigma=p_1p_2+\sigma4ck_1k_2,
 \qquad K_\sigma=|p_1k_2-\sigma p_2k_1|.                    \tag{26.11}
\]

This norm identity does **not** compose Type-I divisor classes.  If
\(F_i=4ck_ix_i-p_i\), where \(x_i\) is either input coordinate, then exactly

\[
 F_1F_2=P_\sigma+4cR_\sigma,                                \tag{26.12}
\]
\[
 R_\sigma=4cx_1x_2k_1k_2-p_1x_2k_2-p_2x_1k_1-\sigma k_1k_2.
\]

When \(K_\sigma>0\), modulo \(4cK_\sigma\) the class is
\(P_\sigma+4c(R_\sigma\bmod K_\sigma)\); it depends on the coordinates and
has no source-only simplification.  If it is to be read as a Type-I target,
one also requires \(P_\sigma\geq2\).  When \(K_\sigma=0\), (26.10)--(26.12)
remain valid norm identities, but there is no positive target modulus and no
reduction modulo \(K_\sigma\).  Universally the product is only
\(+P_\sigma\pmod {4c}\), while a Type-I target requires
\(-P_\sigma\pmod {4c}\).  For odd \(P_\sigma\) these grades already differ
modulo four.

The smallest example points directly at a resister.  At \(c=2\), the tuples
\((5;1,2,2,1)\) and \((13;2,9,2,1)\) give

\[
 33=3\cdot11,\quad177=3\cdot59,
 \quad33\cdot177=73^2+4\cdot2\cdot8^2=5841.                 \tag{26.13}
\]

The four balanced product residues modulo the target modulus 64 are
\(9,9,49,33\), never the required \(-73\equiv55\).  Complete enumeration
also finds no Type-I row for 73 at \((c,k)=(2,8)\).  An odd product of three
input divisor factors repairs the grade modulo four, as in §20.2, but the
new moving modulus still has the uncontrolled term in (26.12); no total
Brahmagupta divisor-pair law was found.

There is, however, a genuine parameter-level correction.

**Theorem 26.4 (proved: corrected binary Type-I tensor).**  Take two Type-I
tuples \((p_i;a_i,b_i,c_i,k_i)\) with the same

\[
 m=(a_i+b_i)/k_i.
\]

For any integer \(t\) such that

\[
 A=a_1a_2,
 \quad B=(a_1+b_1)(a_2+b_2)-A,
 \quad C=mt-4c_1c_2>0,\quad K=k_1k_2m,                       \tag{26.14}
\]

put

\[
                  P={4ABC-1\over m}.                         \tag{26.15}
\]

Then \(P\) is an integer at least two and \((A,B,C,K)\) is a Type-I tuple
for \(P\).  Input or output swaps give the other singleton partitions of the
four bilinear monomials.

*Proof.*  Modulo \(m\), \(b_i\equiv-a_i\), while (26.1) gives
\(-4a_i^2c_i\equiv1\).  Also \(B\equiv-A\) and
\(C\equiv-4c_1c_2\).  Hence

\[
 4ABC\equiv16a_1^2a_2^2c_1c_2
 =(-4a_1^2c_1)(-4a_2^2c_2)\equiv1\pmod m.
\]

This proves integrality.  Since \(A+B=k_1k_2m^2=Km\), equations
(26.14)--(26.15) give
\(P(A+B)=K(4ABC-1)\).  Finally
\(4ABC-1>A+B\geq m\), so \(P\geq2\). ∎

The negative leading correction in \(C\equiv-4c_1c_2\pmod m\) is essential.
Without it, a raw binary tensor has \(4ABC\equiv-t_0^2\pmod m\), where
\(t_0\) is the signed imbalance of its selected tensor monomials.  For a
hard prime, \(m\equiv3\pmod4\); \(-1\) is not a square modulo such an \(m\).
In particular the singleton raw tensor has the exact wrong sign.  A ternary
singleton has the right sign with \(C\equiv16c_1c_2c_3\pmod m\), but forces
the much narrower condition \(m^2\mid K\).  Theorem 26.4 is the binary sign
repair.

The law gives three descending resister transfers, all with prime sources:

\[
\begin{array}{c|c|c|c|r}
P&\text{source 1}&\text{source 2}&(A,B,C,K)&t\\ \hline
2473&(5;1,2,2,1)&(29;1,11,2,4)&(1,35,53,12)&23\\
3169&(17;1,6,5,1)&(17;2,5,3,1)&(2,47,59,7)&17\\
5281&(5;1,2,2,1)&(13;1,5,2,2)&(1,17,233,6)&83
\end{array}                                                  \tag{26.16}
\]

For example, the first row has common \(m=3\),
\(53=3\cdot23-4\cdot2\cdot2\), and
\((4\cdot1\cdot35\cdot53-1)/3=2473\).  Thus every source and target equation
is checked without assuming prior solubility.

For hostile inverse checking, a target row has
\(m=(A+B)/K\) and can be a descending image only if \(m\mid K\).  Up to
swapping \(A,B\), one then finitely enumerates

\[
 n_1n_2=A+B,\quad m\mid n_i,
 \quad a_1a_2=A,
 \quad 1\leq a_i<n_i,
 \quad b_i=n_i-a_i,
 \quad k_i=n_i/m,                                            \tag{26.17}
\]

and the residue classes \(4a_ib_ic_i\equiv1\pmod m\).  Descent bounds each
\(c_i\) by \(4a_ib_ic_i-1<mP\).  Finally one checks
\(C\equiv-4c_1c_2\pmod m\).  The reconstructed parameter is
\(t=(C+4c_1c_2)/m\): the residue check gives integrality, and positivity is
automatic from \(C,c_i>0\).  This is an exact finite inverse test for
Theorem 26.4.  On the eleven resisters, only 1129, 2473, 3169 and 5281 even
have a row with \(m\mid K\).  The 1129 rows are
\((7,11,11,6)\) and its swap, with \(m=3\); neither 7 nor 11 can be the
product \(a_1a_2\) with \(a_i<n_i\) when
\(n_1n_2=18\) and \(3\mid n_i\).  The other three are exactly the successes
in (26.16).  This proves the stated resister outcome for this law, not merely
a failed bounded search.

### 26.4 A cross-type bridge

The clean bridge does not multiply the two quadratic norms; it reinterprets
the same four coordinates.

**Theorem 26.5 (proved: same-tuple Type I to Type II transfer).**  A Type-I
tuple \((p;a,b,c,k)\), with \(m=(a+b)/k\), is a Type-II tuple on the same
coordinates for

\[
                    Q=m(p-1)+1.                              \tag{26.18}
\]

Conversely, a Type-II tuple for \(Q\) has a same-coordinate Type-I reading
if and only if \(m\mid Q-1\); its Type-I value is

\[
                    p=1+{Q-1\over m}.                        \tag{26.19}
\]

For \(m>1\), (26.18) is a strict forward increase and therefore a strict
descent when a target \(Q\) is inverted.

*Proof.*  Type I says \(4abc=pm+1\), so the Type-II value on the same tuple
is
\(4abc-m=pm+1-m=m(p-1)+1\).  Conversely a Type-II tuple says
\(4abc=Q+m\), and \((4abc-1)/m\) is integral exactly when \(m\mid Q-1\),
giving (26.19).  Both unit-fraction identities follow directly from their
parameter equations. ∎

This bridge gives four descending branches among the eleven:

\[
\begin{array}{r|r|r|c}
Q&m&p&\text{same tuple }(a,b,c,k)\\ \hline
673&7&97&(1,34,5,5)\\
1153&3&385&(1,17,17,6)\\
3361&3&1121&(1,29,29,10)\\
5281&11&481&(1,21,63,2)
\end{array}                                                  \tag{26.20}
\]

The source 385 is composite, but its displayed Type-I tuple is an explicit
certificate; no induction hypothesis is used.  For example
\(7(97-1)+1=673\), and the same tuple gives the source identity
\(4/97=1/25+1/850+1/16490\) and the target Type-II identity from (23.2).

No useful product bridge between \(4pck^2+1\) and \(p^2+4ck^2\) was found.
Their grades are respectively fixed \(-1\) and moving \(-p\), and a product
changes the former linearly in \(p\) but the latter quadratically.  Theorem
26.5 bypasses that mismatch; it does not amount to a Gauss composition of
the two divisor forms.

### 26.5 Combined payoff through \(10^4\), and the exact stopping point

**Computational Search 26.6 (exact finite range).**  The §23 Type-II flexible
tensor reaches 132 of the 143 primes \(P\equiv1\pmod {24}\),
\(P\leq10^4\), leaving the eleven in (23.14).  Complete Type-I enumeration,
the exact inverse test (26.17), and the complete Type-II tuple enumeration
for (26.19) give

\[
\begin{array}{l|l}
\text{new system}&\text{resisters reached}\\ \hline
\text{corrected binary Type I (26.14)}&2473,3169,5281\\
\text{same-tuple cross bridge (26.18)}&673,1153,3361,5281
\end{array}                                                  \tag{26.21}
\]

Their union has six primes.  Therefore the **combined** reachability count is
138 of 143, and its exact blocked set through \(10^4\) is

\[
                    \boxed{73,193,241,1129,2521}.             \tag{26.22}
\]

The set is not empty.  Every number in (26.22) nevertheless has explicit
Type-I and Type-II tuples; “blocked” means only that it is not an image of
these transfer systems.  Section 28.1 later reconciles these laws with §25's
fixed additive maps, making the combined finite blocked set empty.  A two-case
induction would still require a theorem
that every target prime has either a descending corrected-Type-I inverse, a
descending cross-type inverse, or a descending Type-II inverse.  Equations
(26.17), (26.19), and the five concrete failures show that this forward-image
totality is false for the present laws.

**Failure log and scope.**

* Brahmagupta composition proves the norm identity (26.10) but lands in the
  positive divisor grade already modulo four.  Ternary factor products fix
  that one bit, not the full moving modulus.
* Theorem 26.4 is a real binary tensor law, but its additive \(C\)-correction
  puts it on an affine grid.  Its inverse is finite and genuinely descending
  on (26.16), not total; no claim is made that it classifies arbitrary
  modulus-dependent corrections.
* Theorem 26.5 is a real cross-type descent on its image, but (26.19)'s
  divisibility condition fails on seven of the eleven and overlaps the
  binary law at 5281.
* Rational maps, non-singleton corrected tensors, and mixed products with
  additional coordinates remain unclassified.  No Erdős--Straus proof is
  claimed.


## 27. Large-\(R\) conditioning: a near-cubic cutoff, rough quarantine, and the remaining cluster wall

Put \(L=\log X\).  This section attacks the large-\(R\) remainder left by
Theorem 24.8.  Labels are strict.  The enlarged truncated-fiber certificate
and its prime-modulus hybrid are **proved**.  The local-lemma and rough-modulus
calculations stop at explicitly named estimates.  H_DC below is a
**conditional, falsifiable** void-probability hypothesis, not a theorem.
The measurements are **informational**.  (H_PF as stated is refuted — see
§31; the critical-window variant \(H_{\rm PF}'\) below remains open.)

### 27.1 The exact conditional target

Fix a cutoff \(Y\), and write

\[
 \mathcal D_Y=\{(R,R^2/s):R\leq Y,\ s\mid\operatorname{rad}(R)\},
 \qquad H_Y=|\mathcal D_Y|.
\]

For every prime \(p\leq X\), \(p\equiv3\pmod4\), put

\[
 B_p(Y)=\{-4D\pmod p:(R,D)\in\mathcal D_Y,\ p\nmid R\},
 \qquad b_p=|B_p(Y)|.                                      \tag{27.1}
\]

The particular finite-interval certificate used in the proof of Theorem
24.8 is

\[
 \mathcal C_Y=\left\{n:
 \begin{array}{ll}
 n\equiv0\pmod p,&p\leq2H_Y,\ p\equiv3\pmod4,\\
 n\pmod p\notin B_p(Y),&2H_Y<p\leq X,\ p\equiv3\pmod4
 \end{array}\right\}.                                     \tag{27.2}
\]

For the launching cutoff \(Y_0=L^{3-\epsilon}\), one sufficient
critical-window statement is

\[
 { |\{n\leq N:n\in\mathcal C_{Y_0},\ \text{no hit with }R>Y_0\}|
       \over |[1,N]\cap\mathcal C_{Y_0}| }
 \geq \exp\{-o(L^3)\},\qquad \log N\asymp L^4.             \tag{27.3}
\]

Together with Theorem 24.8, (27.3) would give
\(|{\rm Av}_X(N)|\geq N\exp\{-o(L^3)\}\), contradicting H_PF's
\(N\exp(-cL^3)\) majorant mean for large \(X\), after choosing the implied constant in
\(\log N\asymp L^4\) large enough to meet H_PF's
\(J\log X\leq\tfrac12\log N\) budget.  This is a conditional probability
for the **same** prime coordinates, not a multiplication of two independent
avoidance estimates.  A natural-density lower bound of the same subcubic
size would also refute literal H_PF; (27.3) is the stronger critical-window
route pursued here.

Here is exactly what remains random after (27.2).  In the CRT (natural-density)
probability space, the coordinates at primes \(p\equiv1\pmod4\) are still
uniform.  At a prime \(p\equiv3\pmod4\), \(p\leq2H_Y\), the residue is fixed
to zero.  At \(p>2H_Y\), it is uniform on the \(p-b_p\) residues outside
\(B_p(Y)\).  Higher \(p\)-adic digits remain uniform.  The same description
holds in a finite interval up to the congruence-count rounding errors treated
by Bonferroni in Theorem 24.8.

There is a useful exact simplification which was easy to miss.  For every
atomic event

\[
 A_{M,R,s}=\{M\mid n+4D\},\qquad
 D=R^2/s,\quad M\equiv-1\pmod {4R},                         \tag{27.4}
\]

one has \((M,R)=1\), hence \((M,D)=1\).  Thus an event whose modulus contains
a conditioned prime \(p\leq2H_Y\), \(p\equiv3\pmod4\), is **impossible**:
\(n\equiv0\pmod p\) but \(-4D\not\equiv0\pmod p\).  In particular, the
prime in question cannot divide the event's own \(R\); the congruence
\(M\equiv-1\pmod R\) rules that out.

For every remaining event, if \(M=\prod p^{a_p}\), its exact conditional
probability in the CRT space is

\[
 \Pr(A_{M,R,s}\mid\mathcal C_Y)=
 \prod_{\substack{p^{a_p}\Vert M\\p\equiv1(4)}}p^{-a_p}
 \prod_{\substack{p^{a_p}\Vert M\\p\equiv3(4)}}
 {\mathbf1_{\{-4D\bmod p\notin B_p(Y)\}}
  \over p^{a_p-1}(p-b_p)}.                                  \tag{27.5}
\]

The second product is automatically over \(p>2H_Y\); otherwise it is zero.
Two such cylinder events are independent after conditioning when their
moduli are coprime.  The honest atomic dependency graph therefore joins
moduli sharing a prime (after duplicate residue classes for one modulus are
collapsed).  Formula (27.5) also shows the conditioning problem: the
large-\(R\) residues are tested against the very sets already removed for
small \(R\).  No independent resampling of those coordinates is available.

### 27.2 A proved polylogarithmic extension and a prime hybrid

The restriction \(Y\leq L^{3-\epsilon}\) in Theorem 24.8 is not the sharp
range of its own bookkeeping.

**Theorem 27.1 (near-cubic truncated fibers plus every prime modulus;
proved).**  Let \(Y=Y(X)\), \(H=H_Y\), and suppose

\[
 H\log L=o(L^3).                                             \tag{27.6}
\]

Uniformly when \(\log N\geq L^4\), the integers which have neither

1. a hit (21.3) with \(R\leq Y\), nor
2. a hit whose modulus \(M\) is prime,

have cardinality

\[
 \geq N\exp\{-O(H\log L+L^2)\}.                             \tag{27.7}
\]

The same lower bound holds for natural density.  Since
\(H\ll Y\log(2Y)\), for every fixed \(\eta>0\) one may take

\[
 Y={L^3\over(\log L)^{2+\eta}},\qquad
 H\log L\ll {L^3\over(\log L)^\eta}=o(L^3).                 \tag{27.8}
\]

Thus the construction reaches a single cutoff \(Y=L^{3-o(1)}\), and at the
same time certifies the complete prime-modulus subsystem, at subcubic cost.
It still leaves composite moduli with \(R>Y\).

*Proof.*  Strengthen (27.2) by fixing \(n\equiv0\pmod p\) for
\(p\leq4H\), \(p\equiv3\pmod4\).  This costs \(\exp\{-O(H)\}\).  For every
larger prime \(p\equiv3\pmod4\), forbid

\[
 G_p=B_p(Y)\cup\mathscr R(p).                               \tag{27.9}
\]

Lemma 21.2 gives \(|\mathscr R(p)|=F(p)\leq(p-1)/2\), while
\(|B_p(Y)|\leq H<p/4\).  Hence \(|G_p|<3p/4\), and

\[
 \sum_{4H<p\leq X}{|G_p|\over p}
 \leq H\sum_{p\leq X}{1\over p}
       +\sum_{p\leq X}{F(p)\over p}
 \ll H\log L+L^2,                                           \tag{27.10}
\]

where the second term is Lemma 24.3.  Avoiding (27.9) certifies every
\(R\leq Y\) event exactly as in Theorem 24.8.  It also certifies every event
with prime modulus, because \(\mathscr R(p)\) is the complete intrinsic set
for that modulus.  The zero prescriptions handle all such events at
\(p\leq4H\), since \((p,D)=1\).

Let \(Q_0\) be the product of the pinned primes, put
\(\mu=\sum_{p>4H}|G_p|/p\), and set
\(V=\prod_{p>4H}(1-|G_p|/p)\).  Then
\(\log Q_0=O(H)\), \(V\geq\exp(-O(\mu))\), and the CRT main term is
\((N/Q_0)V\).  Choose the least odd \(r\geq C\mu\), with the absolute
constant \(C\) large enough that the omitted Euler tail
\(\sum_{j>r}\mu^j/j!\) is at most \(V/4\).  With
\(W=\sum|G_p|\leq H\pi(X)+\sum F(p)\), all congruence-count rounding errors
total

\[
 \exp\{O(r\log W)\}
 =\exp\{O((H\log L+L^2)L)\}=\exp\{o(L^4)\}.                \tag{27.11}
\]

By (27.6), the main term is
\((N/Q_0)V=\exp\{L^4-o(L^3)\}\) or larger, so the rounding error is
negligible even at \(\log N=L^4\).  This proves (27.7).  Finally
\(H\ll Y\log(2Y)\) gives (27.8). \(\square\)

The near-cubic range comes solely from extracting the sharp condition
\(H\log L=o(L^3)\), already latent in Theorem 24.8's bookkeeping; it uses no
new clustering arithmetic.  The hybrid direct-forbidding step adds the
\(L^2\) term and completely removes the class \(M=q\).  Thus the remaining
class for this probability space is genuinely composite, not the prime
slice already pinned by Theorem 24.4.

### 27.3 Local lemma, Suen, and cluster expansion: exact failure point

**Attempt 27.2 (failed as an unconditional full extension).**  There are
two distinct probability spaces; they cannot be combined without a new
argument.

**Route A (the \(\mathcal C_Y\)-conditioned space).**  Use the atoms (27.4)
with the exact probabilities (27.5), and connect atoms whose moduli share a
prime.  Before conditioning, the pair-count neighborhood charge at a fixed
prime \(q\) is

\[
 \begin{split}
 \Lambda_q^{\rm pair}
 &=\sum_{\substack{R>Y\,,\ (R,q)=1}}2^{\omega(R)}
   \sum_{\substack{M\leq X\\M\equiv-1\ (4R)\\q\mid M}}{1\over M}\\
 &\asymp {1\over q}\sum_{Y<R\leq X/q}{2^{\omega(R)}\over R}
                  \log {X\over qR}
 \asymp {\{\log(X/q)\}^3\over q}                           \tag{27.12}
 \end{split}
\]

for polylogarithmic \(q\) and \(Y=X^{o(1)}\), apart from the negligible
lower endpoint.  The first comparison is the harmonic sum in the unique CRT
class modulo \(4Rq\); the second uses
\(\sum_{R\leq t}2^{\omega(R)}/R\asymp(\log t)^2\).
Equation (27.12) is a **pair-mass calculation**, not a lower bound after the
residue exclusions in (27.5).  Deduplicating equal classes or proving that
many large shifts fall in \(B_q(Y)\) could reduce it; controlling precisely
that reduction is the missing clustering input.

There is an earlier defect in Route A if one uses (27.2) literally: small
primes \(q\equiv1\pmod4\), such as 5, remain free, so their shared-prime
neighborhoods retain cubic-scale charge.  Pinning (27.13) **on top of**
\(\mathcal C_Y\) makes every event having a prime factor at most \(z\)
impossible, but it does not give probability \(1/M\) to the survivors:
for primes \(p\equiv3\pmod4\) above \(z\), the inflated factors in (27.5)
remain.

**Route B (standalone all-prime quarantine).**  Discard
\(\mathcal C_Y\) and instead condition only on

\[
 n\equiv0\pmod p\quad\hbox{for every prime }p\leq z.         \tag{27.13}
\]

This costs \(\exp\{-\vartheta(z)\}=\exp\{-O(z)\}\) and makes every event
whose modulus has a prime factor at most \(z\) impossible, because
\((M,D)=1\).  Every surviving modulus is \(z\)-rough and now, on this
standalone product space, each distinct atomic class has probability exactly
\(1/M\).  All fibers and all surviving moduli, including prime moduli, must
remain in this route's local-lemma system; Theorem 27.1 has not been combined
with it.

The expected one-dimensional upper-sieve saving for rough moduli is one
factor \(1/\log z\).  Accordingly the rough pair-charge **benchmark** is

\[
 \Lambda_q^{\rm rough}\ \hbox{of benchmark size}\
       {L^3\over q\log z}.                                  \tag{27.14}
\]

At \(q\asymp z=L^3/(\log L)^{1+\eta}\), this benchmark is
\((\log L)^\eta\) and the elementary one-number neighborhood test does not
close.  This is not a no-go theorem: at
\(z=L^3/\sqrt{\log L}=o(L^3)\) the same benchmark tends to zero.  Suen's
inequality and an unweighted elementary cluster expansion still do not
supply the weighted joint lower bound needed below.

The broad-cofactor proxy class responsible for (27.12) is explicit:
composite moduli \(M=qk\), \(k>1\), with \(q>z\),
\(R\mid(qk+1)/4\), and all \(2^{\omega(R)}\) shifts.  Summing over the
unrestricted cofactor \(k\) creates the charge.  Prime moduli remain in Route
B as well, though their total mass is only quadratic.

Returning to Route A, a direct-forbidding continuation would add, at
coordinate \(q\), every residue \(-4R^2/s\) arising from the broad-cofactor
class.  No proved bound keeps that set away from all the still-available
residues.  Its exact local cost is

\[
 -\log\left(1-{|C_q\setminus B_q(Y)|\over q-b_q}\right),     \tag{27.15}
\]

which can be as large as \(\log(q-b_q)\), rather than
\(O(|C_q|/q)\).  Bounding the sum of (27.15) by \(o(L^3)\) is another form
of the missing large-\(R\) divisor-clustering theorem.  This statement is
only about Route A.

Route B resumes with a more refined, still incomplete choice
\(z=L^3/\sqrt{\log L}\) in (27.13), using prime-dependent rather than
uniform local-lemma charges.  Define

\[
 T_q(z;\mathbf a)=
 \sum_{\substack{M\leq X,\ P^-(M)>z\\q\mid M}}
 {F(M)\over M}\exp\!\left(2\sum_{r\mid M}a_r\right).        \tag{27.16}
\]

If one could prove, simultaneously and uniformly,

\[
 T_q(z;\mathbf a)\leq a_q\quad(q>z),\qquad
 \sum_{\substack{M\leq X\\P^-(M)>z}}{F(M)\over M}
   \exp\!\left(2\sum_{r\mid M}a_r\right)=o(L^3),            \tag{27.17}
\]

with \(a_q=O(L^3/(q\log z))=o(1)\), then assigning to each distinct atomic
class modulo \(M\)

\[
 x_A={1\over M}\exp\!\left(2\sum_{q\mid M}a_q\right)        \tag{27.18}
\]

would satisfy the clique-LLL criterion: its neighbor activity is at most
\(\sum_{q\mid M}a_q\), and
\(\prod_{B\sim A}(1-x_B)\geq
\exp(-2\sum_{q\mid M}a_q)\).  The second estimate in (27.17) would make the
resulting void cost subcubic.  The exponential weight is essential; the
unweighted estimates \(T_q(z;\mathbf0)\ll L^3/(q\log z)\) alone do not
control moduli having many rough prime factors.

**Exact obstruction.**  No uniform shifted-divisor sieve estimate of the
weighted form (27.17) is proved here.  Dropping the exponential weight or
replacing it by its worst-case value loses more than the subcubic budget.
A natural-density local-lemma lower bound from (27.17) would already refute
literal H_PF: for each fixed \(X\), one may pass to sufficiently long
intervals or full periods.  A finite-interval cluster-expansion transfer at
\(\log N\asymp L^4\) is the additional stronger input needed to meet the
critical-window target (27.3), not a prerequisite for refuting H_PF.
Standard one-dimensional upper-bound sieve estimates suggest the unweighted
\(1/\log z\) factor, but ordinary Brun--Titchmarsh, Bombieri--Vinogradov, and
the §17.5 pointwise tools do not state the weighted, residue-varying joint
bound (27.17), nor do they give its lower void probability.

### 27.4 A usable conditional refutation

A per-fiber hit-probability estimate is not enough: its sum is much larger
than one, so a union bound is negative.  The hypothesis must include the
joint void mechanism.

**Hypothesis H_DC(\(\eta\)) (conditional divisor-clustering void bound;
not proved).**  Fix \(\epsilon>0\) and
\(0<\eta<1-\log2\), put \(Y_0=L^{3-\epsilon}\), and condition on
\(\mathcal C_{Y_0}\) from (27.2).  Assume there are constants
\(C>0\) and \(0<c_-<c_+\), with \(c_-\) large enough for H_PF's degree
budget, such that, for all sufficiently large \(X\), every integer \(N\)
with \(c_-L^4\leq\log N\leq c_+L^4\), and every subset

\[
 \mathcal S\subseteq
 \{(R,s):Y_0<R\leq(X+1)/4,\ s\mid\operatorname{rad}(R)\},
\]

one has

\[
 \Pr_N\!\left(
 \begin{array}{c}
 \text{for every }(R,s)\in\mathcal S,\ n+4R^2/s\text{ has no}\
 \text{divisor }M\leq X\text{ with }M\equiv-1\pmod {4R}
 \end{array}
 \middle|\mathcal C_{Y_0}\right)
 \geq \exp\!\left\{-C\sum_{(R,s)\in\mathcal S}w_R\right\}. \tag{27.19}
\]

where

\[
 w_R=\min\left\{1,{L^{\log2+\eta}\over\varphi(4R)}\right\}. \tag{27.20}
\]

The probability is the literal uniform probability on \([1,N]\); thus
(27.19) includes, rather than hides, both the shared-coordinate conditioning
and the finite-interval transfer.  The full-set instance is already nearly
the conditional target (27.3); quantification over every subset strengthens
it and makes the formulation directly falsifiable.  H_DC belongs to Route
A.  The standalone Route-B estimates (27.16)--(27.18) do not mechanically
imply it; that would require a parallel weighted estimate with the inflated
probabilities (27.5), followed by a controlled finite transfer.

**Proposition 27.3 (conditional; H_DC refutes H_PF).**  Under H_DC(\(\eta\)),

\[
 |{\rm Av}_X(N)|
 \geq N\exp\{-O(L^{2+\log2+\eta})-o(L^3)\}
 =N\exp\{-o(L^3)\}                                         \tag{27.21}
\]

when \(\log N\asymp L^4\).  Consequently H_PF is false.

*Derivation.*  By (21.13), and harmless constant factors from \(4R\),

\[
 \sum_{R>Y_0}2^{\omega(R)}w_R
 \leq L^{\log2+\eta}
      \sum_{R\leq X/4}{2^{\omega(R)}\over\varphi(4R)}
 \ll L^{2+\log2+\eta}=o(L^3).                               \tag{27.22}
\]

Apply (27.19) to all remaining fibers and multiply it by the proved
subcubic lower count for \(\mathcal C_{Y_0}\).  This gives (27.21).  The
strict inequality \(\eta<1-\log2\) is exactly what makes the exponent
subcubic.  Unlike a union bound from individual probabilities, (27.19)
already supplies the required joint lower void probability. \(\square\)

**Small exact diagnostic (informational only).**  At \(X=27,Y=2\), one has
\(H=3\) and the exact period is 4,542,615.  The certificate (27.2) contains
460,800 residues.  Of the 14 remaining \((M,R,s)\) atoms, the four with
\(M=15,27\) are impossible because of the fixed coordinate \(n\equiv0\pmod
3\), exactly as predicted above; all ten others obey (27.5).  There are
211,680 certificate residues with no remaining hit, so the conditional void
probability is \(0.459375\).  With the toy weight (27.20) at \(\eta=0\), the
weight sum is 3.80956 and
\(-\log(0.459375)/3.80956=0.2042\).  This is consistent with an H_DC-type
constant at one tiny scale, but it neither probes the rough composite regime
nor supports an asymptotic claim.

### 27.5 One more doubling of sampled avoidance

**Computation 27.4 (informational, exact membership for each sampled
integer).**  A new memory-bounded run used 2.4 billion pseudorandom 64-bit
integers on \([10^{14},9\cdot10^{17})\).  Twenty-four separately seeded
`mt19937_64` streams used the unsigned-64-bit seeds
\(27006400+\mathtt{0x9e3779b97f4a7c15}\,t\pmod {2^{64}}\),
\(0\leq t<24\), and libstdc++'s rejection-based
`uniform_int_distribution<uint64_t>`.  For every \(M\equiv3\pmod4\),
\(M\leq6400\), a Boolean table stored the exact set
\(\{-4D\bmod M:D\mid((M+1)/4)^2\}\).  Each sample stopped at its first
failed modulus; recording that first modulus gives all doubling rows without
bias.  Memory was \(O(\sum_{M\leq6400}M)\), independent of sample count.

The exact source is `scripts/sample_avoidance.cpp`; it includes a 10,000-draw
small replay against a direct divisor oracle.  Each stream receives exactly
100,000,000 draws, split into ten consecutive 10,000,000-draw chunks.  The
240 raw per-chunk survivor vectors, wrapped seeds, sample sums modulo
\(2^{64}\), and mixed XOR checksums are in
`data/avoidance-sample-x6400.tsv`.  That file was reproduced on
2026-08-24 with `g++ 14.2.0-19`, C++20, libstdc++ `20250315`, and glibc 2.41;
`g++ -O3 -DNDEBUG -std=c++20 -pthread` plus the source defaults took 5.52 s
wall time, 107.18 s user time, and 8,872 KiB peak resident memory on the
recorded 24-stream run.  `verify.py (z)` compiles and runs the direct-oracle
self-test and checks the raw file by default; `ES_BIG_SAMPLE=1` regenerates
all 2.4 billion draws and compares every chunk.  Separate deterministic
seeds are not a formal independent-stream construction; the Wilson intervals
below quantify ideal independent, identically distributed sampling error
only and do not cover generator or finite-window effects.

\[
\begin{array}{c|r|c|c|c}
X&\#\text{ survive}&\widehat\delta_X&95\%\text{ Wilson interval}
 &-\log\widehat\delta_X\\ \hline
50&126504179&5.2710075\,10^{-2}&[.05270114,.05271902]&2.94295\\
100&42472324&1.7696802\,10^{-2}&[.01769153,.01770208]&4.03437\\
200&10805883&4.5024513\,10^{-3}&[.00449977,.00450513]&5.40313\\
400&2315665&9.6486042\,10^{-4}&[.00096362,.00096610]&6.94353\\
800&362699&1.5112458\,10^{-4}&[.00015063,.00015162]&8.79741\\
1600&42008&1.7503333\,10^{-5}&[1.73368,1.76715]10^{-5}&10.95312\\
3200&3854&1.6058333\,10^{-6}&[1.55593,1.65734]10^{-6}&13.34187\\
6400&274&1.1416667\,10^{-7}&[1.01425,1.28509]10^{-7}&15.98561
\end{array}                                                  \tag{27.23}
\]

The \(X=6400\) interval has 274 survivors rather than the 14 in the old
\(X=3200\) row.  The coupled \(3200\to6400\) shell adds 2.64374 to the
avoidance exponent while the exact raw class mass adds 4.65670, a ratio
0.568.  The normalized exponent at 6400 is
\(-\log\widehat\delta/(\log6400)^2=0.2081\).

Repeating the unweighted affine fits, now on all eight high-precision rows in
(27.23), gives

\[
\begin{array}{c|cccccc}
 f(X)&L\log L&L^{3/2}&L^2&L^2\log L&L^{2+\log2}&L^3\\ \hline
 {\rm RMSE}&.434&.366&.137&.057&.169&.296
\end{array}.                                                 \tag{27.24}
\]

The correlation of the \(L^2\log L\) and \(L^{2+\log2}\) regressors is
still 0.99965.  The extra doubling favors \(L^2\log L\) on this diagnostic,
but slowly varying candidates remain nearly collinear and a finite-window
sample is not the natural density.  It is evidence only, not H_DC and not a
refutation of H_PF.

### 27.6 Verdict after the large-\(R\) attempt

**Assessment 27.5.**  H_PF remains **false-looking, open**.  (H_PF as stated
is refuted — see §31; the critical-window variant \(H_{\rm PF}'\) below
remains open.)

* **Proved:** the multi-shift certificate itself reaches
  \(Y=L^3/(\log L)^{2+\eta}=L^{3-o(1)}\) at subcubic cost, improving the
  fixed-power cutoff in Theorem 24.8.  The same certificate can simultaneously
  remove every prime-modulus event, by Theorem 27.1.
* **Proved structural quarantine:** in the standalone Route-B space, fixing
  \(n\equiv0\) at every small prime makes all surviving atomic moduli rough
  and gives exact probability \(1/M\) with shared-prime dependency.  This
  costs only \(\exp\{-O(z)\}\); it is not combined with \(\mathcal C_Y\).
* **Failed continuation:** the rough pair-charge benchmark is
  \(L^3/(q\log z)\) and can diverge for subcubic choices of \(z\), but this
  benchmark is not a no-go theorem.  No weighted estimate (27.17) is proved.
  In Route A, direct local forbidding fails at the uncontrolled occupancy
  cost (27.15).
* **Sharpest remaining inputs:** the standalone weighted estimate (27.17)
  would suffice at natural density; finite cluster transfer is the extra
  critical-window goal.  Separately, H_DC (27.19) is an explicit
  \(\mathcal C_Y\)-conditioned joint void hypothesis whose full-set case
  nearly states (27.3).  These are alternatives, not equivalent statements.

Thus the status does not change.  The new unconditional gain is a
polylogarithmic extension and a prime/composite separation; the full
large-\(R\), broad-cofactor composite system remains the exact obstruction.

## 28. Reconciled transfer census, restricted-family atoms, and the forward-image residual

Sections 25 and 26 were produced independently.  Their headline censuses used
incompatible law sets: (26.22) combined §23 with the two §26 laws but omitted
the fixed additive maps (25.11).  This section fixes the register, recomputes
the union, and then asks the stronger tuple-by-tuple question.  Throughout,
**decomposition** means that an already exhibited target tuple is a descending
forward image of explicit source tuples.  It does not construct a tuple for an
arbitrary prime.  **Existence** of a target tuple, or equivalently forward
image totality from the integer alone, remains the Erdős--Straus problem.

### 28.1 One reachability standard and the corrected combined census

**Definition 28.1 (descending self-certified reachability).**  A target tuple
of value \(P\) is *reached* by a transfer branch if the branch exhibits every
source tuple explicitly, direct substitution verifies the appropriate Type-I
or Type-II equation for each source, every source value \(p_i\) satisfies

\[
                         2\leq p_i<P,                         \tag{28.1}
\]

and the fixed forward formula lands on the displayed target tuple exactly.
A value \(P\) is reached if at least one of its target tuples is reached.
Source values need not be prime, hard, or reached by some earlier branch:
their displayed tuples are their certificates.  This is precisely the
standard used for the descending inverse branches in §23.3--§23.4 and the
source rows in (25.10), (25.13), (26.16), and (26.20).  Merely finding a
target tuple is not a transfer proof; conversely, starting an inverse search
from one has already assumed witness existence.

The five values left in (26.22) are covered by Corollary 25.6.1 under this
same definition.  Here is the complete replay, now including the source
tuples rather than only their values:

\[
\begin{array}{r|c|c|c|c}
P&(A,B,C,K)&\text{map}&(p_1;a_1,b_1,c_1,k_1)&
 (p_2;a_2,b_2,c_2,k_2)\\ \hline
73&(2,5,2,1)&\Phi_{++}&(6;1,1,2,1)&(27;1,4,2,1)\\
193&(2,5,5,1)&\Phi_{++}&(18;1,1,5,1)&(75;1,4,5,1)\\
241&(1,22,3,1)&\Phi_{1+}&(10;1,1,3,1)&(230;1,21,3,1)\\
1129&(2,13,11,1)&\Phi_{++}&(42;1,1,11,1)&(515;1,12,11,1)\\
2521&(2,29,11,1)&\Phi_{++}&(42;1,1,11,1)&(1203;1,28,11,1).
\end{array}                                                   \tag{28.2}
\]

For every source row, \(k_i\mid a_i+b_i\) and
\(p_i=4a_ib_ic_i-(a_i+b_i)/k_i\); all ten values satisfy (28.1).  The common
centered modulus is \(g=4C\).  Thus \(\Phi_{++}\) adds the two coordinate
pairs, while \(\Phi_{1+}\) copies the first coordinate and adds the second:
these operations give the target rows in (28.2), whose same formula gives
exactly \(P\).  `verify.py (aa)` also checks all source and target unit-fraction
identities with exact rationals.

**Computational Search 28.2 (corrected prime-level union).**  With Definition
28.1, the combined blocked set under all §23, §25, and §26 laws is

\[
\begin{array}{c|r|r|r|l}
\text{range}&\#\{P\equiv1\ (24)\}&\text{pure tensor reached}&
 \text{combined reached}&\text{combined blocked}\\ \hline
P\leq10^4&143&132&143&\varnothing\\
P<10^5&1181&1170&1181&\varnothing\\
P\leq10^6&9732&9721&9732&\varnothing.
\end{array}                                                   \tag{28.3}
\]

The first correction is simply \(132+11=143\), not (26.22)'s \(132+6=138\):
all eleven pure-tensor resisters have the audited \(k=1\) rows (25.13), so
Theorem 25.6 reaches them.  For \(P<10^5\), §23.4 proves that the same eleven
are the only pure-tensor resisters, and (25.13) covers all eleven.  For
\(P\leq10^6\), the exact one-candidate enumeration and census (25.14)--(25.15)
prove that the pure-tensor resister set is still exactly those eleven; no
extrapolation from \(10^5\) is being made.  The eleven rows are replayed, and
30 deterministic random hard primes in \((3000,10^5)\) are independently
spot-checked in block (aa).  Block (aa) recomputes the two rows through
\(10^5\), including the flexible and fixed-source-2 tensor counts; the
million-prime pure-tensor row is recomputed only by block (x) when
`ES_FULL_SCAN=1`.  Equation (28.3) is finite **witness-decomposition
coverage**.  It is not witness existence for the next prime and is not a
proof of the conjecture.

### 28.2 Restricted-family decomposition fails, but the interior has a uniform map

The target domain in this subsection is the complete set of ordered Type-II
tuples of each hard prime.  This is the common target domain of the additive,
flexible-tensor, and bridge inverses.  A corrected Type-I tensor targets a
Type-I tuple; a Type-II tuple of a hard prime cannot simultaneously be a
Type-I tuple of the same value.  Indeed equality of the two values forces
\(m=1\) (or value 1), while \(m=1\) gives a value \(-1\pmod4\), not a hard
prime.

There is a useful extension of Theorem 25.6 away from \(K=1\).

**Theorem 28.3 (proved: fixed additive descent on the interior).**  Let
\((A,B,C,K)\) be a Type-II tuple for \(P\), put
\(m=(A+B)/K\), and suppose \(A,B\geq2\) and \(m\geq2\).  Then the fixed map
\(\Phi_{++}\), at common source and target modulus \(4CK\), is a descending
image from two explicit Type-II source tuples.  For \(K=1\), use Theorem
25.6.  For \(K\geq2\), choose any integer

\[
 \max(1,K-B+1)\leq\delta\leq\min(A-1,K-1),                  \tag{28.4}
\]

put \(\delta'=K-\delta\), and use

\[
 (\delta,\delta',C,K),\qquad
 (A-\delta,B-\delta',C,K).                                  \tag{28.5}
\]

*Proof.*  The interval (28.4) is nonempty exactly because
\(A,B\geq2\) and \(A+B=mK\geq2K\).  Both rows in (28.5) are positive; their
coordinate sums are \(K\) and \((m-1)K\), so they are valid Type-II tuples.
Their coordinatewise sum is the target, and both centered moduli equal
\(4CK\), proving the forward-map assertion.  Write
\(x=A-\delta,y=B-\delta'\).  The two source values are

\[
 p_1=4C\delta\delta'-1,
 \qquad p_2=4Cxy-(m-1).
\]

Now \(P-p_2=4C(AB-xy)-1>0\).  Also
\(AB-\delta\delta'=\delta y+\delta'x+xy\geq x+y+1
=(m-1)K+1\geq m\), so \(P-p_1>0\).  Positivity gives \(p_i\geq2\), hence
(28.1). ∎

The suggested \((1,K-1)\) move is the first admissible choice in (28.4)
when the boundary permits it.  A \((K,0)\) move is not a positive source.
Copy/add maps can avoid that zero, but their descent then depends on divisors
of \(CK\); they are not universal on the coordinate boundary.

For completeness, the inverse of all three fixed additive maps was made
finite and exact.  Put \(R=CK\).  For \(\Phi_{++}\), enumerate positive
splits \(A=a_1+a_2,B=b_1+b_2\), then
\(k_i\mid(R,a_i+b_i)\) and \(c_i=R/k_i\).  For \(\Phi_{1+}\), enumerate
\(B=b_1+b_2\), take \(k_1\mid(R,A+b_1)\), and for each \(k_2\mid R\) take
the least positive \(a_2\equiv-b_2\pmod{k_2}\); source value is increasing
in \(a_2\), so this least representative makes the test complete.  The
third map is symmetric.  Every candidate is checked against (28.1).

**Computational Search 28.4 (all target tuples for the pre-§30 law union).**
Complete Type-II tuple enumeration gives 940 ordered rows over all 46 hard
primes \(P\leq3000\).  The union of the three exact additive inverses,
flexible tensor inverse, and bridge leaves 34 rows, at 16 primes.  Up to
coordinate swap the complete restricted-family descending-atom table is

\[
\begin{array}{r|c|r@{\qquad}r|c|r}
P&(A,B,C,K)&m&P&(A,B,C,K)&m\\ \hline
241&(1,62,1,9)&7&409&(1,104,1,15)&7\\
577&(1,146,1,21)&7&601&(1,153,1,14)&11\\
937&(1,118,2,17)&7&1129&(1,285,1,26)&11\\
1249&(1,314,1,45)&7&1609&(1,202,2,29)&7\\
1657&(1,417,1,38)&11&1753&(1,440,1,63)&7\\
2089&(1,524,1,75)&7&2089&(1,528,1,23)&23\\
2281&(1,286,2,41)&7&2593&(1,650,1,93)&7\\
2617&(1,328,2,47)&7&2713&(1,681,1,62)&11\\
2953&(1,370,2,53)&7&&&
\end{array}                                                   \tag{28.6}
\]

Every row in (28.6) has a coordinate 1, \(K>1\), \(4\nmid CK\), and
\(m\nmid P-1\).  Thus it lies outside Theorem 28.3, the flexible tensor, and
the bridge; the exact additive inverse closes the remaining branches.  These
are **atoms only for this pre-§30 restricted descending law union**, not prime
blockers or intrinsic tuple-lattice obstructions: every listed prime has some
other decomposable tuple.  Section 30 adds the grid moves \(X,Y,Z\), arbitrary
admissible relabelling, and paths that need not remain below the target value.
Under that larger system every one of these 34 ordered rows is already a
direct \(X\)- or \(Y\)-descendant of a lower valid tuple and reduces to
\((1,1,1,1)\); block (aa) verifies both assertions.  For example,
\((1,62,1,9)\) at 241 has the descending predecessor
\((1,53,1,9)\) at 206 under \(Y^{-1}\).  Thus (28.6) records the boundary of
the older transfer family, not the current lattice frontier.

On a deterministic random sample of 30 hard primes between 3000 and
\(10^5\), all 1,952 Type-II rows were tested.  There are 58 restricted-family
atoms at 18 primes; again every atom has a coordinate 1, \(4\nmid CK\), and
\(m\nmid P-1\), while every sampled prime has at least one decomposable row.
This refutes decomposition completeness for the stated older family and
isolates its boundary, rather than producing a new prime-level resister
frontier.

If “every tuple” is read to include Type I as well, failure is much larger.
There are 1,830 ordered Type-I rows at the same 46 primes.  Only 44 pass the
necessary gate \(m\mid K\), and the exact corrected inverse decomposes 40;
1,790 are outside the only fixed law here whose target is Type I.  The bridge
points from a Type-I source to a Type-II target and does not change that
count.

### 28.3 The complete \(k=1\)-less census through one million

There is a fast exact test requiring no arbitrary parameter cutoff.  By
symmetry take \(A\leq B\).  From

\[
 P=4ABC-A-B
\]

one gets \(B\mid P+A\) and

\[
 {P+A\over B}=4AC-1\equiv-1\pmod{4A}.                       \tag{28.7}
\]

Conversely every divisor satisfying (28.7) reconstructs the positive integer
\(C\).  Since every tuple has \(AB\leq P/2\), it is enough to test
\(1\leq A\leq\lfloor\sqrt{P/2}\rfloor\).  Thus (28.7) is an exact finite
test per prime.

**Computational Search 28.5 (exact hard-prime census).**  Among hard primes
\(P\equiv1\pmod{24}\), the complete \(k=1\)-less list through one million is

\[
 \boxed{409,577,5569,9601,23929,83449,102001,329617,712321}. \tag{28.8}
\]

The first six reproduce §19.3; the final three are new beyond \(10^5\).
Counts by half-open decimal decade are

\[
\begin{array}{c|r|r|r}
\text{range}&\#\text{ hard primes}&\#\text{ without }k=1&\text{fraction}\\ \hline
[10,10^2)&2&0&0\\
[10^2,10^3)&12&2&0.166667\\
[10^3,10^4)&129&2&0.015504\\
[10^4,10^5)&1038&2&0.001927\\
[10^5,10^6)&8551&3&0.000351.
\end{array}                                                   \tag{28.9}
\]

After the sparse first two decades, the observed proportion thins by roughly
an order of magnitude per decade.  This is descriptive finite data, not a
density theorem.  The default block (aa) replays (28.7) through \(10^5\);
`ES_FULL_SCAN=1` extends the same code through \(10^6\).  The scan stores only
the current divisor list and the output list.

### 28.4 Forward images ranked, and the sharpened residual

Each image condition can be stated arithmetically in \(P\) alone.  This does
not remove its existential content.

* **\(I_{\rm add}(P)\): fixed additive maps.**  There is a Type-II row
  \((A,B,C,K)\) of \(P\), and positive source splits satisfying the exact
  \(R=CK\) divisor conditions preceding Search 28.4 and (28.1).  The simple
  \(\Phi_{++}\), \(K=1\) subimage is exactly the set of \(P\) having a
  \(k=1\) row with \(A,B\geq2\); the three Theorem-25.6 branches together
  are exactly the hard \(P\) having any \(k=1\) row.
* **\(I_{\rm flex}(P)\): flexible tensor.**  There is a Type-II row and the finite factor/split
  data of Lemma 23.3, including (28.1).  For the source-2 singleton branch,
  up to swaps there are positive \(a,b,c,k,C,K\) with
  \(k\mid a+b\), \(CK=4ck\), \(K\mid2(a+b)\),
  \((A,B)=(a,a+2b)\), source value
  \(q=4abc-(a+b)/k\in[2,P)\), and
  \(P=4ABC-2(a+b)/K\).  This is an explicit arithmetic shape, not a residue
  class.
* **\(I_{\rm bridge}(P)\): bridge.**  There is a Type-II row of \(P\) with
  \(m=(A+B)/K>1\) and \(m\mid P-1\).  Equivalently,
  \(ABC=(P+m)/4\), \(m\mid A+B\), and the smaller Type-I value is
  \(1+(P-1)/m\).
* **\(I_{\rm Icorr}(P)\): corrected Type I.**  There is a Type-I row of \(P\), with
  \(m=(A+B)/K\), satisfying the complete inverse data (26.17) and (28.1).
  The easy condition \(m\mid K\) is only a necessary gate, not the image:
  1129 already separates them.

The exact/specified census densities for the 1,181 hard primes below
\(10^5\), in decreasing order, are

\[
\begin{array}{l|r|r}
\text{condition}&\#P&\text{fraction}\\ \hline
\text{some exact fixed-additive branch}&1181&1.000000\\
\text{some Theorem-25.6 }k=1\text{ branch}&1175&0.994920\\
\text{full flexible-tensor inverse}&1170&0.990686\\
\text{fixed-source-2 tensor inverse}&1166&0.987299\\
\Phi_{++}\text{ on a }k=1\text{ row with }A,B\geq2&1165&0.986452\\
\text{bridge}&771&0.652837\\
\text{corrected-Type-I necessary gate }m\mid K&697&0.590178\\
\text{exact corrected-Type-I inverse}&681&0.576630.
\end{array}                                                   \tag{28.10}
\]

The \(k=1\), bridge, and Type-I rows in (28.10) are regenerated by fast exact
arithmetic predicates in block (aa); the two tensor counts are the exact
§23.4 census replayed by block (v).  The fixed-additive count is certified by
the 1,175 \(k=1\) values plus exact branches for the six values in §19.3.
The corrected-Type-I gate is enumerated without Lemma 26.2's broad loops:
write \(K=m\ell\), so \(A+B=m^2\ell\), and enumerate
\(C\equiv(4AB)^{-1}\pmod m\) under \(P=(4ABC-1)/m<10^5\); (26.17) then
distinguishes 681 exact images from the 697 gate values.

Empirically the additive image is broadest.  Structurally, however, its
condition starts by asking for a Type-II witness and so has not solved the
forward problem.  The source-2 branch is the most rigid and explicit high-
density sufficient shape, but it already has finite misses.  The bridge and
corrected-Type-I conditions are too sparse to be plausible individual
all-large-prime statements.  No audited distribution theorem makes even the
full disjunction pointwise-uniform.

Within the four pre-§30 descending transfer families, the exact residual is
their union:

> **Pre-§30 residual conjecture H_W9 (forward-image totality).**  For every prime
> \(P\equiv1\pmod{24}\), at least one of the exact predicates
> \(I_{\rm add}(P)\), \(I_{\rm flex}(P)\),
> \(I_{\rm Icorr}(P)\), or \(I_{\rm bridge}(P)\) above holds, including
> explicit positive source tuple(s) with every source value in \([2,P)\)
> and the corresponding fixed forward formula landing exactly at value
> \(P\).

A proof would prove Erdős--Straus for the hard primes directly (or after a
finite base check if H_W9 were proved only for sufficiently large \(P\)),
because every branch outputs a certified target tuple.  H_W9 is weaker than
requiring any one older family to be total, but it is **not weaker than the raw
residual problem of §17.6**.  It implies witness existence and imposes extra
decomposability; the restricted-family atoms (28.6) show that witness
existence does not imply decomposition of an arbitrary witness under those
four families.  The prime-level converse is exactly what is unknown.

Section 30 changes the decomposition system, not the existence problem.  Its
grid reduction is automatic once a hard-prime Type-II tuple has been found,
so it removes all of (28.6) as lattice atoms but supplies no tuple from the
integer \(P\).  In the §30 system the residual target is therefore raw Type-II
witness existence, not H_W9-style decomposition.  Thus the empty finite
blocked set and the 100% additive-image row in (28.10) are useful diagnostics
of the older laws, not a reduction in the proved logical hardness and not an
Erdős--Straus proof.

---

## 29. Transfer laws on the exceptional-set axis: one exact subsumption and a subcubic prime-divisor class construction

This section asks a narrower question than §§22--26: after forgetting descent
and retaining only sufficient conditions on the target integer \(P\), do the
transfer laws add fixed congruence classes with more than the cubic mass of
Theorem 18.2?  A **class** below is counted once at its displayed modulus,
as in §18.1.  Labels are strict.  In particular, the closure theorem in
§29.2 includes the complete Case-B divisor family and the *prime-divisor*
Type-I extraction; it does not silently assign congruence mass to polynomial
value sets or to the unaudited composite-divisor Type-I extraction.

### 29.1 Inventory and the exact Case-B dictionary

Put \(h=4ck\).  In the Case-B divisor form (17.3), a fixed divisor \(q\)
with

\[
 q\equiv-1\pmod h,
 \qquad q\mid4Pck^2+1                                      \tag{29.1}
\]

forces the single class

\[
 P\equiv-(4ck^2)^{-1}\pmod q.                              \tag{29.2}
\]

Here \(q\) may be composite; (29.1) makes every displayed inverse legitimate.

**Lemma 29.1 (Case-B classes are exactly the intrinsic classes; proved).**
For every \(q\equiv3\pmod4\), the union of (29.2) over all \((c,k)\) with
\(4ck\mid q+1\) is exactly \(\mathscr R(q)\) of Lemma 18.1 as a residue set.
The parameter descriptions need not be injective; multiplicity disappears
only after taking the set union.

*Proof.*  Write

\[
 A={q+1\over4}=cka.
\]

The Lemma-16.1 factorization

\[
 (u,v,w)=(a,k,c),\qquad uvw=A
\]

gives

\[
 -uv^{-1}=-ak^{-1}\equiv-(4ck^2)^{-1}\pmod q,              \tag{29.3}
\]

because \(4cka\equiv1\pmod q\).  In Lemma 18.1's divisor notation the
same class is

\[
 -4D\pmod q,\qquad D=ca^2\mid A^2,                         \tag{29.4}
\]

since \(16ck^2D=(4cka)^2\equiv1\pmod q\).  Conversely, the
prime-by-prime construction in Lemma 18.1 writes every \(D\mid A^2\) as
\(D=u^2w\) with \(uvw=A\).  Taking \((a,k,c)=(u,v,w)\) reverses
(29.3)--(29.4).  Thus the two unions agree as residue sets.  Raw \((c,k)\)
descriptions can collide; counting the union, rather than the factorizations,
gives exactly \(F(q)\). ∎

This is the requested dictionary.  In particular the apparent
\(\#\{(c,k):4ck\mid q+1\}\) gain is entirely a reparametrization of the
already deduplicated divisor set \(\{-4D:D\mid A^2\}\).  On prime \(q\),
the resulting mass is the quadratic prime slice of Lemma 24.3, not a new
additive copy of it.  Composite \(q\)'s recover the complete intrinsic
system and its cubic mass.

The Type-I divisor form behaves differently.  For fixed \((c,k)\), (26.3)
asks for a divisor

\[
 q\mid P^2+4ck^2,
 \qquad q\equiv-P\pmod h.                                  \tag{29.5}
\]

The grade now moves with \(P\).  Prime divisors nevertheless give fixed CRT
class constructions whose shape is not exhausted by the intrinsic class at
the same prime modulus.

**Lemma 29.2 (prime Type-I CRT classes; proved).**  Let \(q\nmid2ck\) be an
odd prime.  If \((-4c\mid q)=1\), let \(r_\pm\) be the two roots of
\(r^2\equiv-4ck^2\pmod q\).  Then every positive target in either
Chinese-remainder class

\[
 P\equiv r_\pm\pmod q,
 \qquad P\equiv-q\pmod h                                   \tag{29.6}
\]

modulo \(hq\) has a positive Type-I solution.  If the symbol is \(-1\),
there is no such class.  For hard targets \(P\equiv1\pmod4\), (29.6) forces
\(q\equiv3\pmod4\).

*Proof.*  Every positive member of (29.6) has \((P,ck)=1\), satisfies
\(q\mid P^2+4ck^2\), and has \(q\equiv-P\pmod h\).  The divisor algebra of
Theorem 26.1 extends verbatim beyond its stated prime-target domain here:
put \(e=(P^2+4ck^2)/q\).  Since \(q\equiv-P\pmod h\), one has
\(e\equiv-P\pmod h\), so
\[
             a={P+q\over h},\qquad b={P+e\over h}
\]
are positive integers, and direct expansion gives
\(P(a+b)=k(4abc-1)\).  Conversely a prime divisor in (29.5) supplies one of
the two roots.  Reduction modulo four gives the final assertion. ∎

These classes are not merely another notation for Lemma 29.1 at the same
prime modulus.  For example \((q,c,k)=(7,5,1)\) gives roots
\(1,6\pmod7\) and classes \(113,13\pmod{140}\).  The second projects to
\(6\pmod7\) and is subsumed by \(\mathscr R(7)=\{3,5,6\}\); the first
projects to \(1\pmod7\), which is absent from that intrinsic set.  More
strongly, no single intrinsic progression contains all of
\(113\pmod{140}\): its modulus would divide 140, the only eligible divisors
\(\equiv3\pmod4\) are 7 and 35, and
\(\mathscr R(35)=\{23,26,31,32,34\}\) does not contain
\(113\equiv8\pmod{35}\).

This novelty is only relative to the intrinsic multiplier construction.  The
exact progression \(113\pmod{140}\) already appears in §4 as the guaranteed
Case-B family \((q,d,R)=(7,5,5)\).  Its hard refinement contains 673, but
673 is itself intrinsic at modulus 15 because
\(673\equiv13\in\mathscr R(15)=\{7,11,13,14\}\).  The example therefore
shows a new class construction and local projection, not a newly covered
target or novelty relative to every earlier fixed family.  For a composite
fixed divisor \(q\), the same argument gives
\(\rho_q(-4ck^2)\) CRT classes modulo \(hq\).  Their root multiplicities
and cross-factorization collisions are not evaluated here; no claim about
the mass of that composite extraction is hidden in Theorem 29.3.

The remaining transfer laws have a different status.

* **Pure/flexible tensors (§§22--23).**  Their forward images are polynomial
  value sets with divisibility side conditions, not a family of complete
  residue classes supplied by the transfer theorem.  For example the
  fixed-source-2 singleton branch can read
  \(P=8a(a+2b)c-s\), \(s=(a+b)/k\).  If \((a,b,k)\) is frozen and only
  \(c\) varies, this is a subprogression of the pre-existing Type-II
  moving-\(c\) class for target tuple
  \((a,a+2b,2c,2k)\); it is not transfer-created supply.  With the source
  variables free it is a value-set problem, for which no density or
  bounded-fiber theorem is proved.
* **Fixed additive maps (§25).**  Theorem 25.6 starts from a target \(k=1\)
  tuple and decomposes it.  Thus its inverse condition is exactly “a
  \(k=1\) tuple exists,” already the old Type-II identity condition.  It
  supplies witness decomposition, not an additional condition forcing a
  previously unknown \(P\).
* **Corrected Type-I tensor and bridge (§26).**  Theorem 26.4 again supplies
  an image value set, with the common-\(m\) and affine-\(C\) constraints.
  The bridge condition \(m\mid Q-1\) is attached to an already existing
  tuple; freezing its coordinates gives
  \(Q=4abc-m\), exactly the old Type-II moving-\(c\) family.  Neither law
  provides a new free congruence class beyond the complete Type-I/II
  parametrizations.

**Assessment 29.2.1 (scope of the inventory).**  Polynomial images can in
principle be counted by value-set or thin-orbit methods, and selected linear
slices can be organized into old parametrized progressions.  §§22--26 prove
no such counting theorem and no bounded-multiplicity map onto primes.
Calling their images extra sieve mass would therefore count witnesses, not
distinct target classes.  This is the same circularity isolated in §§23.2
and 25.7, now applied to the exceptional-set question.

### 29.2 Mass accounting and cubic closure

Let \(t=\log X\), and let \(\mathcal A_{\rm pr}(X)\) be the **union**, at
each modulus \(4ckq\leq X\), of the hard-compatible classes (29.6) with
prime \(q\).  Duplicates from different \((c,k,q)\) descriptions are
removed before its mass is computed.  Its distinct mass is bounded by its
raw multiplicity envelope:

\[
\begin{aligned}
 \mu(\mathcal A_{\rm pr}(X))
 &\leq {1\over2}
   \sum_{\substack{q\leq X/4\\q\equiv3\ (4)\\q\ \mathrm{prime}}}{1\over q}
   \sum_{ck\leq X/(4q)}{1\over ck}                         \tag{29.7}\\
 &\leq \left({1\over8}+o(1)\right)t^2\log t
   =o(t^3).                                                  \tag{29.8}
\end{aligned}
\]

Indeed each triple has at most two roots, giving the factor
\(2/(4ckq)=1/(2ckq)\).  Also

\[
 \sum_{ck\leq Y}{1\over ck}
 =\sum_{n\leq Y}{\tau(n)\over n}
 ={1\over2}(\log Y)^2+O(\log Y),                            \tag{29.9}
\]

and Mertens' theorem in the progression \(3\pmod4\), by partial summation,
gives

\[
 \sum_{\substack{q\leq e^t\\q\equiv3\ (4)}}
 {\{t-\log q\}_+^2\over q}
 ={1\over2}t^2\log t+O(t^2).                               \tag{29.10}
\]

Equations (29.9)--(29.10) give (29.8).  The constant \(1/8\) belongs to
the deliberately larger envelope which awards two roots to every triple;
Legendre failures, hard-class incompatibility, and all deduplication only
lower it.  No matching asymptotic for the distinct Type-I union is claimed.

**Theorem 29.3 (cubic closure for the audited fixed-class supply; proved).**
Take the union of

1. every intrinsic class of Lemma 16.1 with modulus at most \(X\);
2. every fixed-\((c,k)\) Case-B divisor class with displayed modulus at most
   \(X\); and
3. every hard-compatible prime-divisor Type-I class (29.6) with modulus at
   most \(X\).

After per-modulus deduplication, its total class mass is

\[
                       \asymp(\log X)^3.                    \tag{29.11}
\]

*Proof.*  Lemma 29.1 says item 2 is exactly item 1, including all its
cross-\((c,k)\) duplicates.  Theorem 18.2 gives two-sided cubic mass for
item 1.  Equations (29.7)--(29.8) give an \(o(t^3)\) upper bound for item
3 even before deduplication against item 1.  The intrinsic lower bound and
the sum of these upper bounds prove (29.11). ∎

Here “union” is the per-displayed-modulus class-mass bookkeeping of §18.
The theorem neither evaluates cross-modulus coverage correlations nor proves
a positive Type-I mass increment after overlap with the intrinsic system.
Thus the prime Case-B back-of-the-envelope \(\tau_3\)-count contributes zero
new residues after the exact dictionary, while the prime Type-I CRT class
construction has at most \(t^2\log t\) raw-envelope mass.  It can alter finite
constants and lower-order logarithms, but it cannot change the cubic power.
The mass/Rankin balance of §18.1 therefore still has exponent ceiling
\(3/(3+1)=3/4\) for this enlarged fixed-class supply.

**Assessment 29.3.1 (what is not closed).**  A composite divisor in (29.5)
also yields fixed CRT classes.  The crude bound
\(\rho_q\leq2^{\omega(q)}\) is too wasteful to prove a cubic distinct-mass
bound after summing \((c,k,q)\), while the expected quadratic-character
cancellation and the cross-\(q\) deduplication have not been established
uniformly here.  Consequently Theorem 29.3 is not a theorem about that
composite Type-I extraction, nor about every possible organization of the
polynomial image sets.  This is the principal soft spot.  Any claim of a
supercubic family must first count *distinct* CRT classes through those two
collisions; raw root/factorization multiplicity is not such a claim.

### 29.3 Quadratic-form sieve angle (exploratory, timeboxed)

**Assessment 29.4 (standard one-fiber sieve consequences).**  Fix \((c,k)\),
put \(h=4ck\), and restrict \(P\) to a reduced residue \(a\pmod h\).  The
following uses the standard Mertens theorem in a fixed progression and the
fixed-dimension fundamental lemma only in their usual level ranges.  The
relevant prime divisors in (29.6) now satisfy

\[
 q\equiv-a\pmod h.                                         \tag{29.12}
\]

The quadratic character \((-4c\mid q)\) has conductor dividing \(4c\),
hence is constant on (29.12).  A fiber is therefore either inactive or has
two forbidden roots for every prime in that progression.  On an active
fiber,

\[
 \sum_{\substack{q\leq z\\q\equiv-a\ (h)}}{2\over q}
 ={2\over\varphi(h)}\log\log z+O_{c,k}(1).                 \tag{29.13}
\]

Thus the classical upper-bound sieve for one fixed pair has dimension
\(2/\varphi(h)\) and gives only a log-power saving, of shape

\[
 \#\{P\leq N:P\equiv a\ (h),\ P\hbox{ avoids (29.6)}\}
 \ll_{c,k}{N\over h(\log z)^{2/\varphi(h)}}                \tag{29.14}
\]

in its standard level range.  A lower-bound fundamental lemma in a fixed
fiber leaves the matching log-power order when its level hypotheses hold;
it therefore shows that this one branch alone has many avoiders, not that
those avoiders survive the other branches.  Before conditioning, “two roots
for half the primes” suggests the usual quadratic/half-dimension language;
after the mandatory grade condition is imposed, the split bit is pinned by
the same progression and (29.13) is the exact dimension statement.

**Assessment 29.4.1 (no independent exponential bound from the classical
quadratic sieve).**  Equation (29.14), even with \(z\) a power of \(N\),
is polynomial in \(\log N\), far weaker than Theorem 16.4.  Obtaining an
\(\exp\{-c(\log X)^2\}\)-type auxiliary-scale saving requires a growing
collection of \((c,k)\)'s to be assembled jointly.  Classical
half-dimension/fundamental-lemma estimates for one quadratic do not perform
that assembly: the progression (29.12) moves with \(P\), the moduli share
\(4ck\), and the same CRT class can have several parameter descriptions.
No mixed large-sieve or Selberg factorization controlling these correlations
is proved here.  In particular there is no proved multiplicative stacking
with the intrinsic system.  Such a mixed assembly is a legitimate future
question, but its nominal prime-Type-I mass is already bounded by (29.8), so
even perfect use cannot raise the cubic mass power.

### 29.4 Verdict

**Verdict 29.5 (proved part, then boundary).**

* The complete fixed-\((c,k)\) Case-B divisor supply is **exactly
  subsumed** by the intrinsic multiplier system, class for class and with
  exact cross-parameter deduplication.
* Prime-divisor Type-I conditions produce CRT class shapes with projections
  absent from the intrinsic class at the same prime modulus, but the example
  proves no newly covered target.  Their total distinct mass is at most
  \(O((\log X)^2\log\log X)=o((\log X)^3)\).
* The tensor, additive, corrected-tensor, and bridge laws produce witness
  images or reparametrize old Type-I/II classes; no new class-mass theorem
  follows from them.
* Therefore the audited enlarged fixed-class system still has exactly cubic
  mass, and the \(3/4\) conditional mass/Rankin ceiling stands.  There is no
  unconditional improvement to Theorem 16.4, and no record-bound claim.

Theorem 18.6 and H_PF need no wording change: H_PF is intentionally a
hypothesis for the complete intrinsic system, which already has the cubic
lower mass needed for the conditional \(3/4\) result.  One could formulate a
stronger mixed H_PF including (29.6), but (29.8) cannot improve its power and
no such mixed correlation hypothesis is presently justified.  (This wording
is superseded: H_PF as stated is refuted — see §31; the critical-window
variant \(H_{\rm PF}'\) below remains open.)  The remaining unclosed
exceptional-set directions are the composite Type-I CRT mass and a joint
treatment of polynomial image sets; neither is evidence for a supercubic
family without a distinct-class count.

**Numerical companion.**  `verify.py (ab)` checks Lemma 29.1 on every prime
\(q\leq3000\), including raw-versus-union counts; constructs and deduplicates
the hard-compatible Type-I CRT classes through several small cutoffs; checks
the \((7,5,1)\) non-subsumption example and exact Type-I reconstructions;
and reports the finite mass divided by its raw multiplicity mass,
\((\log X)^2\log\log X\), and \((\log X)^3\).  These truncation ratios are
informational and are not used in (29.8).


## 30. The full Type-II tuple lattice is one decorated additive orbit

This section asks a different question from witness existence.  Let

\[
 \mathscr T=\{(A,B,C,K)\in\mathbb Z_{>0}^4:K\mid A+B\},
 \qquad V(A,B,C,K)=4ABC-{A+B\over K}.                       \tag{30.1}
\]

Every member has \(V\geq2\) and is a valid Type-II tuple for its value.
Put

\[
 R=CK,\qquad g=4R,\qquad
 T_R(A,B)=gAB-A-B=K V(A,B,C,K).                              \tag{30.2}
\]

Thus a fixed centered modulus \(g\) permits many independent readings:
\(K\mid R\), \(K\mid A+B\), and \(C=R/K\).  The main result below is a
complete generation theorem for **all** of \(\mathscr T\), from the single
tuple \((1,1,1,1)\).  Its canonical path first generates a target of value
\(P\) and fourth coordinate \(K\) in its \(K=1\) reading at value \(KP\),
then relabels down to \(P\).  Thus \(KP\) is the peak of that displayed path,
not a proved minimum or an unavoidable price.  This theorem is about
decomposing an already specified lattice point.  It does not construct a
point over a specified prime.

### 30.1 The move set

#### Common-modulus addition with arbitrary source and output readings

For a tuple \(x_i=(a_i,b_i,C_i,K_i)\), write
\(D_i=g a_i-1,E_i=g b_i-1\).  The condition needed for the following maps is
only

\[
 C_1K_1=C_2K_2=R.                                           \tag{30.3}
\]

In particular \((C_1,K_1)\) and \((C_2,K_2)\) may be different readings of
the same \(g=4R\).  Define the three fixed centered-factor maps

\[
\begin{array}{c|c|c}
 &D'&E'\\ \hline
 \Phi_{++}&-1+(D_1+1)+(D_2+1)&-1+(E_1+1)+(E_2+1)\\
 \Phi_{1+}&D_1&-1+(E_1+1)+(E_2+1)\\
 \Phi_{+1}&-1+(D_1+1)+(D_2+1)&E_1.
\end{array}                                                  \tag{30.4}
\]

After division by \(g\), their output coordinate pairs are respectively

\[
 (a_1+a_2,b_1+b_2),\qquad(a_1,b_1+b_2),\qquad
 (a_1+a_2,b_1).                                              \tag{30.5}
\]

**Lemma 30.1 (proved: exact common-\(g\) composition law).**  Let \((A,B)\)
be any pair in (30.5).  For every independently chosen output reading

\[
 K'\mid R,\qquad K'\mid A+B,\qquad C'=R/K',                 \tag{30.6}
\]
(30.4) outputs the valid tuple \((A,B,C',K')\), of value

\[
 P'={T_R(A,B)\over K'}.                                     \tag{30.7}
\]

No relation among \(K_1,K_2,K'\) is required beyond source validity and
(30.6).  If \(p_i=V(x_i)\), the three numerator laws are

\[
\begin{aligned}
 T_R(a_1+a_2,b_1+b_2)
   &=K_1p_1+K_2p_2+g(a_1b_2+a_2b_1),\\
 T_R(a_1,b_1+b_2)&=K_1p_1+b_2(ga_1-1),\\
 T_R(a_1+a_2,b_1)&=K_1p_1+a_2(gb_1-1).
                                                               \tag{30.8}
\end{aligned}
\]

*Proof.*  Every factor in (30.4) is \(gA-1\) or \(gB-1\), hence is
\(-1\pmod g\).  Conditions (30.6) give the requested reading and
integrality of (30.7).  Expanding \(T_R\) gives (30.8).  For positivity,
write \(C'=R/K'\); then
\[
 P'=4ABC'-{A+B\over K'}\geq4AB-(A+B)\geq2AB\geq2.
\]
This also verifies directly that the output remains in \(\mathscr T\).
\(\square\)

This is the all-\(K\) version of Theorem 25.6.  The important extra freedom
is not a new coefficient: it is the independent divisor reading of each
source and the output at their common \(g\).

#### Grid neighbours, slice motion, and relabelling

There are four unary move schemas:

\[
\begin{array}{rcll}
 X:(A,B,C,K)&\mapsto&(A+K,B,C,K),
   &V\mapsto V+(4BCK-1),\\
 Y:(A,B,C,K)&\mapsto&(A,B+K,C,K),
   &V\mapsto V+(4ACK-1),\\
 Z:(A,B,C,K)&\mapsto&(A,B,C+1,K),
   &V\mapsto V+4AB,\\
 \mathfrak R_{K'}:(A,B,C,K)&\mapsto&(A,B,R/K',K'),
   &V\mapsto (K/K')V,
\end{array}                                                   \tag{30.9}
\]

where the relabelling move requires \(K'\mid R=CK\) and
\(K'\mid A+B\).  The last displayed quotient is integral by (30.2), even
when neither \(K\) nor \(K'\) divides the other.

**Lemma 30.2 (proved: validity and self-certifying grid complements).**  All
moves in (30.9) preserve positivity and validity.  The first three strictly
increase the value.  At fixed \((C,K)\), if
\(D=gA-1,E=gB-1\), then

\[
 X:D\mapsto D+gK,\quad V\mapsto V+E;
 \qquad
 Y:E\mapsto E+gK,\quad V\mapsto V+D.                        \tag{30.10}
\]

Thus each grid-neighbour edge carries its old complementary factor as the
exact value increment.  Its inverse is valid precisely when the coordinate
to be reduced is greater than \(K\).

*Proof.*  Divisibility by \(K\) is unchanged by adding \(K\), and by changing
\(C\).  Direct substitution gives (30.9)--(30.10).  Relabelling preserves
\(R\), and (30.2) gives its value law. \(\square\)

Take the finite set of move **schemas**

\[
 \mathcal M=\{\Phi_{++},\Phi_{1+},\Phi_{+1},X,Y,Z,\mathfrak R\}. \tag{30.11}
\]

“Finite” here means seven fixed formulas; their positive tuple arguments and
the admissible divisor \(K'\) vary.  Coordinate swap is a symmetry, not an
additional generator.  Because three schemas are binary,
\(\operatorname{Orb}_{\mathcal M}(S)\) means the least subset of \(\mathscr T\)
that contains \(S\), is closed under every admissible unary move, and is
closed under a binary schema whenever both inputs already belong to the
subset.  A binary derivation may reuse an earlier input.  This mixed-arity
closure is not an ordinary monoid action; the totality proof below in fact
uses only the four unary schemas.

Two earlier candidate moves add no lattice reach.  The §20.1 absorption law
at fixed \((C,K)\), with \(L=gK\), sends

\[
 P\mapsto P\circ_Lv=P+v+LPv,
 \qquad B\mapsto B+Kv(gB-1).                                \tag{30.12}
\]

It is exactly \(v(gB-1)\) successive \(Y\)-neighbour steps (or the swapped
version), so it is a sparse macro-edge in the same grid.  The §26.5 bridge
starts from a **Type-I** tuple and is therefore not an endomorphism of
\(\mathscr T\).  In a bipartite Type-I/Type-II graph it supplies useful
certificate edges, but every Type-II endpoint is already in the orbit proved
below.  It does not strengthen the Type-II lattice generation statement.

### 30.2 Complete generation and normal forms

For a fixed slice \((C,K)\), define

\[
 \mathcal S_{C,K}^{\rm red}=
 \{(r,K-r,C,K):1\leq r<K\}\cup\{(K,K,C,K)\}.               \tag{30.13}
\]

For the global system put simply

\[
                     \mathcal S_0=\{(1,1,1,1)\}.             \tag{30.14}
\]

**Theorem 30.3 (proved: fixed-slice and full-lattice generation).**

1. **Value-monotone fixed slices.**  Every tuple in the \((C,K)\)-slice is
   reached by \(X,Y\) from exactly one reduced seed in (30.13).  Reverse
   grid reduction is terminating and confluent.  The irreducibles are exactly
   the \(K\) seeds (30.13).
2. **The full orbit.**

   \[
                 \operatorname{Orb}_{\mathcal M}(\mathcal S_0)
                 =\mathscr T.                               \tag{30.15}
   \]

   All intermediate vertices can be kept valid.  A target
   \((A,B,C,K)\) of value \(P\), with \(R=CK\), has a canonical unary path
   from 2 to \(KP\) on which every translation strictly increases the value,
   followed by the one relabelling \(\mathfrak R_K\) to \(P\).  That path has
   peak exactly \(KP\) (ratio \(K\) over the target); no minimality claim is
   made.  For \(K=1\) the whole path is value-monotone.
3. **Global irreducibility.**  Orient relabelling toward \(K=1\), then orient
   the inverse unit additions toward \(A=B=1\), and finally orient \(Z^{-1}\)
   toward \(C=1\).  The sole irreducible is (30.14).  This prescribed reverse
   reduction terminates under the lexicographic rank
   \[
                 \bigl(\mathbf 1_{K\ne1},\ A+B+CK\bigr).
   \]
   The initial relabelling lowers its first component; every subsequent
   subtraction lowers its second.  Reverse value \(V\) is not monotone: the
   initial relabelling raises \(P\) to \(KP\) when \(K>1\).  The apparently
   trivial shapes \((1,1,C,K)\) exist only for \(K\mid2\): the \(K=2\) shape
   relabels to \((1,1,2C,1)\), and every \(K=1\) shape with \(C>1\)
   reduces by \(Z^{-1}\).

*Proof.*  Write the positive residues

\[
 A=A_0+Ku,\qquad B=B_0+Kv,
 \qquad 1\leq A_0,B_0\leq K.                                \tag{30.16}
\]

Since \(K\mid A_0+B_0\), their sum is \(K\) or
\(2K\), giving exactly (30.13).  The residues make the seed unique, and
Lemma 30.2 makes every forward step strictly value-increasing.  Equivalently,
with \(u,v\geq0\), Theorem 20.4's exact formula is

\[
 V=V_0+u(gB_0-1)+v(gA_0-1)+gKuv.                            \tag{30.17}
\]

For the global statement, first apply \(Z^{R-1}\) to reach
\((1,1,R,1)\), then \(X^{A-1}\) and \(Y^{B-1}\) to reach
\((A,B,R,1)\).  These are unit translations because this sheet has \(K=1\),
and the final value is \(T_R(A,B)=KP\).  Conditions \(K\mid R,A+B\) permit
the final relabelling to \((A,B,C,K)\).  This is an ordinary unary path; the
three binary \(\Phi\) laws are redundant extra closure operations for
(30.15).  Every translation has positive increment by Lemma 30.2.

Conversely Lemmas 30.1--30.2 show that every schema preserves membership in
\(\mathscr T\), so the orbit cannot be larger.  Reversing the displayed
construction gives the stated normal reduction and its sole endpoint; the
rank in part 3 proves termination. \(\square\)

The canonical peak can be far from optimal.  For the hard-prime tuple
\((1,20,1,3)\) of value 73, the canonical peak is 219, whereas
\[
 (1,1,1,1)\xrightarrow{Z^2}(1,1,3,1)
 \xrightarrow{Y}(1,2,3,1)
 \xrightarrow{\mathfrak R_3}(1,2,1,3)
 \xrightarrow{Y^6}(1,20,1,3)
\]
has successive values \(2,6,10,21,7,18,29,40,51,62,73\), so its peak is
only 73.  Nor is there a uniform canonical excursion factor.  For
\(K=6n+3\), the tuple \((1,7K-1,1,K)\) has
\(P=28K-11=168n+73\).  Dirichlet's theorem supplies infinitely many prime
values in this progression, all \(1\pmod{24}\); hence \(K\) and the canonical
ratio \(KP/P=K\) are unbounded even on hard-prime fibres.

There is a cleaner **reduced** orbit model.  Forget the reading and identify
the \(K=1\) tuple with the positive lattice point \((A,B,R)\).  The three
unit translations act as the free commutative monoid \(\mathbb N_0^3\),
simply transitively from \((1,1,1)\).  Over a node sits the finite divisor
fibre

\[
 \mathcal K(A,B,R)=\{K:K\mid\gcd(R,A+B)\},                  \tag{30.18}
\]

and its decoration \(K\) means the tuple \((A,B,R/K,K)\).  In this reduced
model alone, the only translation relations are commutation.  It is a
commutative grid with a divisor-fibre decoration, not a descent tree: a node
at translation depth \(d\) has
\(d!/((A-1)!(B-1)!(R-1)!)\) labelled shortest paths to it.

This is not a presentation of the full seven-schema closure.  The binary
maps need not commute in their inputs: at \(R=1\), \(\Phi_{1+}\) applied to
\((1,1,1,1),(2,1,1,1)\) gives \((1,2,1,1)\), while reversing the inputs
gives \((2,2,1,1)\).  Relabelling and sheet translation also need not
commute: from \((1,1,1,2)\), relabel-to-1 then \(X\) reaches
\((2,1,2,1)\), while \(X\) then relabel-to-1 reaches \((3,1,2,1)\).
Thus neither the mixed-arity system nor its divisor decoration is a
commutative monoid action.

The value image at exact translation depth \(d\) is explicitly

\[
 \mathcal V_d=
 \left\{{4RAB-A-B\over K}:\begin{array}{l}
 A,B,R\geq1,\ A+B+R=d+3,\\
 K\mid\gcd(R,A+B)
 \end{array}\right\}.                                      \tag{30.19}
\]

There are \({d+2\choose2}\) undecorated nodes and

\[
 \sum_{A+B+R=d+3}\tau(\gcd(R,A+B))                          \tag{30.20}
\]

decorated tuples before value collisions.  On the \(K=1\) sheet the values
range from exactly \(3d+2\) to \(\Theta(d^3)\): every translation adds at
least 3, equality is attained along \((d+1,1,1)\), while AM--GM gives the
upper bound \(4((d+3)/3)^3\), attained to leading order near the balanced
point.  Relabelling contributes the exact divisors shown in (30.19), not a
random or approximately multiplicative growth law.

**Computational Audit 30.4 (bounded construction and complete finite
value-fibre regression, not asymptotic evidence).**  `verify.py (ac)` checks
the common-\(g\) laws with independent readings, every move identity, the two
normal forms, and complete tuple lists for every hard prime through 5000.
The printed common-addition count is the number of admissible branches; the
grid count is the number of valid rows on which all moves and relabellings are
audited; and the bounded-orbit count is the number of decorated nodes
constructed.  Tuple enumeration uses Lemma 25.8, so it has no parameter
cutoff.  Every ordered tuple is explicitly relabelled to \(K=1\), reduced
coordinate by coordinate to \((1,1,R,1)\), then reduced to (30.14).  The
audit table is

\[
\begin{array}{c|r|r|r|r}
 P\leq X&\#\text{ hard primes}&\#\text{ ordered tuples}
 &\#\text{ local fixed-slice seeds seen}&\#\text{ endpoints off the global seed}\\ \hline
500&9&102&41&0\\
1000&14&182&74&0\\
2000&30&522&197&0\\
3000&46&940&359&0\\
4000&61&1402&524&0\\
5000&76&1938&717&0
\end{array}                                                  \tag{30.21}
\]

The 41, 74, 197, and later counts are distinct local normal forms (30.13)
encountered before global relabelling, not additional global endpoints.
Every one subsequently reaches (30.14).  The zero endpoint counts are
computed from the canonical reductions, but remain regressions of the proved
theorem rather than empirical extrapolation.

This also reconciles the closer atom census in §28.  Its 34 rows are atoms
only for the older one-step descending transfer union with source values in
\([2,P)\).  The §30 grid/relabel system is different and permits paths with
upward relabelling.  In fact all 34 are immediate \(X\)- or \(Y\)-descendants
of lower valid tuples: \((1,62,1,9)\) at 241, for example, has
\((1,53,1,9)\) at 206 as its \(Y^{-1}\) predecessor.  Block (aa) checks all
34 immediate predecessors and their reductions to the global seed.  Thus §30
eliminates them as lattice atoms without claiming that its moves are the same
as §28's transfer laws.  Likewise, the §20.1 multiplication atoms belonged
only to that still sparser macro-law.

### 30.3 The exact reformulation, and why it is not yet a Markoff problem

Let \(\mathrm{ES}_{II}\) denote the **Type-II strengthening** of
Erdős--Straus on the hard primes.  The exact orbit reformulation is:

> **Exact orbit reformulation (verbatim).**
> \[
> [\mathrm{ES}_{II}\text{ for hard primes}]
> \Longleftrightarrow
> [\text{every hard prime }P\text{ has some Type-II tuple}]
> \Longleftrightarrow
> [\text{for every hard prime }P,\
> V^{-1}(P)\cap\operatorname{Orb}_{\mathcal M}(\mathcal S_0)\ne\varnothing].
>                                                               \tag{30.22}
> \]

By (30.19), the exact open value-image statement is

\[
 \boxed{\quad
 \{P\text{ prime}:P\equiv1\pmod {24}\}
       \subseteq \bigcup_{d\geq0}\mathcal V_d.\quad}         \tag{30.23}
\]

This is arithmetically explicit, but substitution of \(R=CK\) shows that it
is precisely \(P=4ABC-(A+B)/K\) again.  Orbit coverage is completely proved;
**value-fibre intersection** is the conjectural part.

**Logical warning (proved from the scope of Theorems 3.1 and 17.1, not a
conjectural identification).**  The first bracket in the requested chain
cannot honestly be replaced by unrestricted
“Erdős--Straus for hard primes” using the results in this document.  A hard
prime solution may a priori be Type I or Type II; Theorem 3.1 proves the
union of the two cases, and no same-value Type-I-to-Type-II conversion theorem
has been proved.  Therefore

\[
 \mathrm{ES}_{II}\Longrightarrow\mathrm{ES},                \tag{30.24}
\]

but the converse needed for that replacement is open here.  Full
Erdős--Straus has the exact value statement

\[
 P\in V_{II}(\mathscr T)\ \cup\ V_I(\mathscr T_I),           \tag{30.25}
\]

not (30.23) alone.  Equation (30.22) is exact as written and must not be
upgraded by silently discarding Type I.  Empirically, §19 found a Case-B
witness for each of the 719,781 hard primes below \(10^8\).  Its label
“Case-B-only hard-slice” means that the search was restricted to Case B, not
that those primes were proved to have only Case-B solutions; no exhaustive
stored Case-A table was compared.

There is no hidden Vieta action.  Holding \(P\) and three of \(A,B,C,K\)
fixed makes the fourth unique:

\[
 A={KP+B\over4BCK-1},\quad
 B={KP+A\over4ACK-1},\quad
 C={KP+A+B\over4ABK},\quad
 K={A+B\over4ABC-P}.                                        \tag{30.26}
\]

Thus no coordinate occurs quadratically and there is no second root to flip.
In divisor coordinates,

\[
 (gA-1)(gB-1)=1+gKP,                                        \tag{30.27}
\]

the involution \(D\mapsto(1+gKP)/D\) merely swaps \(A,B\).  Choosing a
different factor pair requires factoring the right side, which is the
original divisor-coset search.  Flexible relabelling cannot give a second
fixed-\(P\) involution either: it changes \(P\) by \(K/K'\), and preserves
\(P\) only when \(K'=K\).  No second slice-mixing involution was found; this
is a closure of the natural root/factor-pair hunt, not a classification of
all rational self-maps.

**Technology audit (assessments; prerequisites stated, no transfer claim).**

* **Markoff / Bourgain--Gamburd--Sarnak.**  The Markoff Vieta involutions
  preserve one cubic equation and generate a non-elementary invertible action
  whose reductions modulo primes admit expansion/strong-approximation
  technology (including density-one statements in that setting).  Here the
  unary translations change \(V\), but a special binary addition can preserve
  it: \(x=(2,69,4,1)\) has value 2137, \(y=(1,22,4,1)\) has value 329, and
  \(\Phi_{++}(x,y)\) with output reading \(K'=2\) is \((3,91,2,2)\), again
  of value 2137.  This needs an auxiliary source, is not source-independent
  or shown invertible, and supplies no non-elementary fixed-fibre group.  The
  fixed-\(P\) fibre still has no second-root involution, while only the reduced
  \(K=1\) translation model is an elementary commutative grid.  The required
  source-independent, invertible fixed-fibre action is absent.
* **Markoff / Zagier counting.**  Markoff counting exploits a finite-to-one
  descent and hyperbolic tree growth.  Here shortest paths commute in
  multinomially many ways, reduced seeds vary with slices, and membership in
  one value fibre remains the factorization condition (30.27).  Quadratic
  node growth in (30.20) does not supply pointwise positivity of the value
  image.
* **Apollonian / Fuchs-type local--global work.**  Apollonian packings provide
  a thin integral orthogonal-group orbit on the fixed Descartes quadratic
  form; congruence admissibility can then be compared with orbit values.
  Our orbit is the whole decorated positive lattice, not a thin quadratic
  orbit, and Theorem 17.3 shows that local congruence classes alone miss the
  relevant square classes.  The thin-group and fixed-quadratic-form
  prerequisites are both absent.

These comparisons identify prerequisites, not impossibility theorems for all
future orbit methods.  They do rule out importing the named results merely
because (30.15) uses the word “orbit.”

### 30.4 Honest verdict

**Proved.**  The three common-\(g\) additive maps admit arbitrary independent
\((C_i,K_i)\) readings and any admissible output reading.  Fixed slices are
exactly \(K\) value-monotone bilinear grids.  Seven fixed move schemas generate
the entire positive Type-II tuple lattice from one seed, with sole global
normal-form atom \((1,1,1,1)\).  The displayed canonical path has peak \(KP\),
but lower-peak paths exist and its factor \(K\) is unbounded.  The finite audit
through 5000 finds all 1,938 ordered tuples and no endpoint off the seed.

**What it buys.**  It gives a clean normal form, the exact relations of the
reduced \(K=1\) translation grid, and the explicit level images (30.19).  It
also prevents future work from mistaking §20 multiplication atoms, §28's
restricted-family atoms, or the \(k=1\) boundary for intrinsic tuple-lattice
obstructions.

**What it does not buy.**  Because the orbit is already all of \(\mathscr T\),
(30.23) is a relabelling of the Type-II witness-existence problem, not a new
local--global mechanism.  The unary translations do not preserve prime value;
special binary additions can preserve a value but do not form a
source-independent invertible action.  Reverse reduction starts from the
tuple whose existence is sought, and may first raise \(P\) to \(KP\).  The
full-Erdős--Straus equivalence additionally retains the Type-I alternative in
(30.25).

**Exact open orbit statement.**  Prove (30.23), equivalently prove that every
prime \(P\equiv1\pmod {24}\) occurs in one of the explicit decorated-grid
value sets (30.19); or, for full Erdős--Straus without the Type-II
strengthening, prove that it occurs in the union (30.25).  No such value-image
theorem is proved here.

---

## 31. Rough shifted divisors: a weighted mean theorem and a natural-density refutation of H_PF

Put \(L=\log X\).  This section returns to the wall in §27.3.  The labels
are important: the weighted rough mean, the softened neighborhood estimate,
and the natural-density conclusion are **proved**.  The original pointwise
shape in (27.17), and the transfer to an interval with
\(\log N\asymp L^4\), are not proved.

### 31.1 The target, its difficulty class, and the source check

For a prime \(q\) let

\[
 b_q={L^3\over q\log z},\qquad
 W_{\boldsymbol a}(M)=\mathbf1_{P^-(M)>z}
       \exp\!\left(2\sum_{p\mid M}a_p\right),               \tag{31.1}
\]

where the sum is over distinct prime divisors.  The exact statement requested
in (27.17), with all quantifiers exposed, is the following.

**Target 31.1 (the original weighted estimate; still not proved in this
pointwise shape).**  Take
\(z=L^3/\sqrt{\log L}\).  There should be an absolute constant \(A>0\)
such that, for every sufficiently large \(X\), there are nonnegative numbers
\(a_q\), one for every prime \(z<q\leq X\), satisfying

\[
 a_q\leq A b_q,
 \qquad
 \sum_{\substack{M\leq X\,,\ M\equiv3(4)\,,\ P^-(M)>z\,,\ q\mid M}}
 {F(M)\over M}\exp\!\left(2\sum_{p\mid M}a_p\right)
 \leq a_q                                                   \tag{31.2}
\]

for every such \(q\), and

\[
 \sum_{\substack{M\leq X\,,\ M\equiv3(4)\,,\ P^-(M)>z}}
 {F(M)\over M}\exp\!\left(2\sum_{p\mid M}a_p\right)
 =o(L^3).                                                    \tag{31.3}
\]

The error in (31.3) is uniform for the one charge vector supplied at each
\(X\); it is not a \(q\)-dependent assertion.  Equivalently, (31.2) is
\(T_q(z;\boldsymbol a)\leq a_q\).

By Lemma 21.1, the underlying void event says, jointly for every
\(R\leq(X+1)/4\) and every \(s\mid\operatorname{rad}(R)\), that

\[
 n+4R^2/s\quad\hbox{has no divisor }M\leq X
       \quad\hbox{with }M\equiv-1\pmod {4R}.                \tag{31.4}
\]

After the standalone quarantine \(n\equiv0\pmod p\) for \(p\leq z\), only
\(z\)-rough \(M\)'s survive and every atomic probability is exactly \(1/M\).
Thus (31.2) is a weighted, shared-prime neighborhood estimate for the
**joint** shifted-divisor problem (31.4), not merely a mean theorem for one
polynomial value.  The progression modulus \(4R\), the shift \(4R^2/s\),
and the \(2^{\omega(R)}\) multiplicity all move together.  This is the exact
difficulty class.

The literature audit is as follows.

* Theorem 1 quoted in Henriot, *Nair--Tenenbaum bounds uniform with respect
  to the discriminant* (`sources/henriot-1102.1643.pdf`, pp. 1--2), says:
  for pairwise coprime irreducible \(Q_1,\ldots,Q_k\in\mathbb Z[T]\), with
  \(Q=\prod Q_j\) of degree \(g\), discriminant \(D\), and no fixed prime
  divisor, and \(F\in\mathcal M_k(A,B,\epsilon)\) with
  \(\epsilon\leq\alpha\delta/(12g^2)\), uniformly for
  \(x\geq c_0\|Q\|^\delta\) and \(x^\alpha<y\leq x\),
  \[
   \sum_{x<n\leq x+y}F(|Q_1(n)|,\ldots,|Q_k(n)|)
   \ll y\prod_{p\leq x}\left(1-\frac{\rho(p)}p\right)
   \sum_{n_1\cdots n_k\leq x}
   F(n_1,\ldots,n_k){\rho_{Q_1}(n_1)\cdots\rho_{Q_k}(n_k)
                    \over n_1\cdots n_k}.                  \tag{31.5}
  \]
  In that quoted theorem the implicit constant may depend on \(D\).
  Henriot's own Theorem 5/Corollary 2 replaces this by an explicit
  discriminant factor and constants independent of \(D\), while retaining
  the coefficient-size condition \(x\geq c_0\|Q\|^\delta\).
* The original Nair--Tenenbaum paper
  (`sources/nair-tenenbaum-1998.pdf`, Theorem 1 and Corollaries 1--2) gives
  (31.5), including an arithmetic-progression extension, for the larger
  \(\mathcal M_k\) class.  Shiu's Theorem 1
  (`sources/shiu-1980.pdf`, pp. 162--163) is its one-form ancestor: for a
  nonnegative multiplicative \(f\) in Shiu's class, reduced \(a\pmod q\),
  \(q<y^{1-\beta}\), and \(x^\alpha\leq y\leq x\), it bounds the progression
  sum by
  \(y\{\varphi(q)\log x\}^{-1}
    \exp(\sum_{p\leq x,p\nmid q}f(p)/p)\), up to a constant depending only
  on the class parameters.
* These are **upper mean-value** theorems.  The indicator that an integer has
  no divisor in one truncated progression is not multiplicative: two
  coprime values which separately have no eligible divisor can acquire one
  by multiplying divisors from the two values.  A product over forbidden
  prime factors is a valid minorant only when every bad composite divisor
  forces a prime in a fixed bad set.  That is exactly the \(D=1\) mechanism
  of Lemma 24.5; it fails for a general moving class \(-1\pmod {4R}\).
* **FLAGGED (bibliography checked only at title level; theorem details from
  memory, not invoked):** Erdős--Hall's *Proof of a conjecture about the
  distribution of divisors of integers in residue classes* and R. R. Hall's
  related residue-class papers study distribution/moments of divisors in
  fixed residue classes.  **FLAGGED (from memory):** Ford's Annals paper
  *The distribution of integers with a divisor in a given interval*, 168
  (2008), 367--433, determines the order of the one-value interval-divisor
  counting function \(H(x,y,z)\).  Their clustering technology is the right
  analogy, but no theorem from those works is asserted here to be uniform in
  the moving \(4R\), simultaneous in all shifts, conditional on (27.2), or
  weighted by the shared-prime activities in (31.2).

There is nevertheless a multiplicative **majorant** which is useful for the
rough atomic mass: \(F(M)\leq\tau(((M+1)/4)^2)\leq
\tau_3((M+1)/4)\).  It does not minorize the void.  The next two results use
it only on the upper-mean side, then let the local lemma provide the void.

### 31.2 The weighted rough mean: the second half of (27.17)

**Theorem 31.2 (weighted rough-modulus mean; proved).**  Uniformly for
\(3\leq z\leq X^{1/10}\) and nonnegative charges \(a_p\leq1\), put
\(E=\sum_{z<p\leq X}a_p/p\).  Then

\[
 \sum_{\substack{M\leq X\,,\ M\equiv3(4)}}
 {F(M)\over M}W_{\boldsymbol a}(M)
 \ll e^{CE}{L^3\over\log z}.                               \tag{31.6}
\]

In particular, if \(a_p=O(L^3/(p\log z))\) and
\(z=L^3/\sqrt{\log L}\), then \(E=o(1)\), so (31.3) holds.

*Proof.*  Write \(M=4m-1\), and define the multiplicative function

\[
 w(p^\nu)=
 \begin{cases}0,&p\leq z,\\ e^{2a_p},&p>z,
 \end{cases}
 \qquad(\nu\geq1),\qquad w(1)=1.                            \tag{31.7}
\]

The summand before division by \(M\) is at most
\(w(4m-1)\tau_3(m)\).  Apply (31.5), or Henriot's Corollary 2, to

\[
 Q_1(t)=4t-1,\qquad Q_2(t)=t,
 \qquad \mathcal F(u,v)=w(u)\tau_3(v).                     \tag{31.8}
\]

The function \(\mathcal F\) is multiplicative and belongs to a fixed
\(\mathcal M_2(A,B,\epsilon)\), uniformly in the charges.  The determinant
of the two linear forms is \(1\), so the discriminant factor is exactly
harmless.  At every odd prime the forms have two distinct roots.  Corollary
2 therefore gives, on a dyadic interval of length \(V\), an upper bound by
\(V\) times

\[
 \prod_{p\ll V}(1-2/p)(1+w(p)/p)(1+3/p)
 \ll {\log^2(2V)\over\log z}
       \exp\!\left(C\sum_{z<p\ll V}{a_p\over p}\right),    \tag{31.9}
\]

whenever the interval can contain a \(z\)-rough value.  For \(p\leq z\)
the coefficient of \(1/p\) in the logarithm is \(1\); for \(p>z\) it is
\(2+O(a_p)\).  This proves (31.9) by Mertens' estimate.  The first possible
rough value has size \(>z\), so the few lowest dyadic intervals have
\(\log V\asymp\log z\) and obey the same bound after changing the constant.
Dyadic summation and partial summation now give

\[
 \sum {F(M)W_{\boldsymbol a}(M)\over M}
 \ll {e^{CE}\over\log z}
      \left(L^2+\int_z^X{(\log t)^2\over t}\,dt\right),
\]

which is (31.6).  Finally
\(E\ll L^3\{z\log z\}^{-1}=o(1)\) for the stated charges and cutoff. ∎

This proves the global weighted line which §27.3 left open.  It does not by
itself prove a void probability: its right side still tends to infinity.

### 31.3 A softened pointwise estimate

The obstruction to applying Henriot uniformly to all of (31.2) is now very
specific.  In \(M=qk\), the relevant forms in the cofactor variable have
coefficient size \(q\).  Henriot requires the cofactor interval to have
length at least a fixed power of \(q\).  The short initial range is not
covered by (31.5), and the diagonal \(k=1\) alone would require the unproved
pointwise bound
\(F(q)=O(L^3/\log z)\) to retain \(a_q=O(b_q)\).

A maximal-order term handles that short range without damaging the global
weighted mean.  Fix a sufficiently large absolute \(C_d\), and put

\[
 u_q={\log(2q)\over q}
       \exp\!\left({C_d\log(2q)\over\log\log(3q)}\right).    \tag{31.10}
\]

**Theorem 31.3 (softened (27.17); proved).**  Let

\[
 z={L^3\log\log L\over\log L}.                              \tag{31.11}
\]

For all sufficiently large \(X\), there is an absolute \(A>0\) such that
the charges

\[
 a_q=A(b_q+u_q)\qquad(z<q\leq X,
                       \ q\text{ prime})                    \tag{31.12}
\]

satisfy

\[
 T_q(z;\boldsymbol a)\leq a_q\quad(z<q\leq X),              \tag{31.13}
\]

and

\[
 \max_{q>z}a_q=o(1),\qquad
 \sum_{z<q\leq X}{a_q\over q}=o(1),\qquad
 \sum_{\substack{M\leq X\,,\ M\equiv3(4)}}
 {F(M)\over M}W_{\boldsymbol a}(M)
 \ll {L^3\over\log z}=o(L^3).                              \tag{31.14}
\]

The same conclusion holds with
\(z=L^3g(L)/\log L\) whenever \(g(L)\to\infty\) and
\(g(L)=o(\log L)\).

*Proof.*  The standard maximal-order divisor bound gives

\[
 \tau_3(n)\leq
 \exp\!\left({C_d'\log(2n)\over\log\log(3n)}\right).        \tag{31.15}
\]

Fix \(q>z\), write \(M=qk\), and choose the unique
\(r\in\{1,3\}\) for which \(qr\equiv3\pmod4\).  With
\(k=4t+r\),

\[
 {qk+1\over4}=qt+c,\qquad c={qr+1\over4},\qquad 4c-qr=1.    \tag{31.16}
\]

Thus the cofactor and shifted factor are determinant-one linear forms.  For
\(Q(t)=(4t+r)(qt+c)\), Henriot's norm is the sum of the absolute values of
its coefficients, and here
\[
 \|Q\|=
 \begin{cases}(25q+5)/4,&r=1,\\(49q+7)/4,&r=3,
 \end{cases}
 \qquad\text{so}\qquad \|Q\|\leq13q.
\]
Also

\[
 W_{\boldsymbol a}(qk)
 \leq e^{2a_q}w(k),
 \qquad F(qk)\leq\tau_3((qk+1)/4).                          \tag{31.17}
\]

Use Henriot with the fixed choices \(\alpha=\delta=1/2\), and let \(c_0\)
be its constant in \(x\geq c_0\|Q\|^{1/2}\).  Split the cofactor sum at
\(k=C_0q^{1/2}\), where \(C_0\) is a sufficiently large fixed multiple of
\(c_0\sqrt{13}\) (for example, allowing a factor \(8\) for the change from
\(k\) to \(t\)).  Then every high-range \(t\)-block begins above
\(c_0\|Q\|^{1/2}\).  In the lower range,
(31.15), \(\sum_{k\leq y}1/k\ll\log(2y)\), and roughness give

\[
 {1\over q}\sum_{k<C_0q^{1/2}}
 {F(qk)W_{\boldsymbol a}(qk)\over k}
 \ll u_q.                                                   \tag{31.18}
\]

Indeed \(qk\ll q^{3/2}\).  From (31.12), uniformly in \(p>z\),
\(a_p=O(1/\log\log L)+p^{-1+o(1)})\).  Since a rough integer \(qk\) has at
most \(\log(qk)/\log z\) distinct prime factors, its exponential weight in
the lower range is absorbed by increasing the constant in (31.15).  This
also includes \(k=1\), the prime-modulus diagonal.

Dyadically decompose the high range in the variable \(t\) (splitting an
endpoint cofactor block into a bounded number of such intervals), so each
interval has the literal form \(x<t\leq x+y\) with
\(x^{1/2}<y\leq x\).  Apply Henriot to the two forms in (31.16) and the
multiplicative function \(w(4t+r)\tau_3(qt+c)\).  Their determinant is \(1\),
and the coefficient condition holds by the choice of \(C_0\).  Since a
composite rough cofactor has \(k>z\), the
Euler-product calculation in (31.9) gives

\[
 \sum_{V<k\leq2V}w(k)\tau_3((qk+1)/4)
 \ll V{(\log(2V))^2\over\log z}.                            \tag{31.19}
\]

The omitted local factor at \(p=q\) can only decrease this upper bound.
Dividing by \(qk\) and summing the dyadic blocks gives
\(O(L^3/(q\log z))=O(b_q)\).  Equations (31.18)--(31.19) prove
\(T_q\ll b_q+u_q\).  The implicit constant is uniform once
\(\max a_p\leq1\) and \(\sum a_p/p\leq1\), so choosing the absolute \(A\)
in (31.12) large enough closes (31.13), rather than making a circular
assumption.

For (31.14),

\[
 \sum_{q>z}{b_q\over q}\ll {L^3\over z\log z}=o(1).         \tag{31.20}
\]

For large \(q\), the exponential in (31.10) is at most \(q^{1/4}\), so

\[
 \sum_{q>z}{u_q\over q}
 \ll\sum_{n>z}{\log(2n)\over n^{7/4}}=o(1).                 \tag{31.21}
\]

The same estimates give \(\max a_q=o(1)\).  Theorem 31.2 now proves the
last assertion of (31.14).  Replacing \(\log\log L\) in (31.11) by a general
\(g(L)\) changes (31.20) to \(O(1/g(L))\) and changes nothing else. ∎

The additional \(u_q\) is the exact price of the coefficient-short range.
It is \(q^{-1+o(1)}\), so it is invisible in the Euler mean (31.14), but no
argument here proves the stronger uniform comparison \(u_q=O(b_q)\) up to
\(q=X\).  Thus Theorem 31.3 is a usable weakening, not a relabeling of the
original (27.17).

### 31.4 Natural-density lower bound and H_PF

**Theorem 31.4 (full-system natural-density lower bound; proved).**  With
\(z\) as in (31.11), the natural density of the complete avoider system
satisfies

\[
 \delta_X\geq
 \exp\!\left\{-O\!\left({L^3\log\log L\over\log L}\right)\right\}
 =\exp\{-o(L^3)\}.                                         \tag{31.22}
\]

More generally the cutoff in the last sentence of Theorem 31.3 gives
\(\delta_X\geq\exp\{-O(L^3g(L)/\log L)\}\).

*Proof.*  First impose

\[
 n\equiv0\pmod p\qquad(3\leq p\leq z,
                         \ p\text{ prime}).                 \tag{31.23}
\]

For precision, let
\(P_z=\prod_{3\leq p\leq z,\ p\text{ prime}}p\), and let \(K_X\) be the
lcm of \(P_z\) and every participating modulus.  Work on the finite uniform
probability space \(\mathbb Z/K_X\mathbb Z\), conditioned on (31.23).  The
conditioning has cost
\(P_z^{-1}=\exp\{-\vartheta(z)+O(1)\}=\exp\{-O(z)\}\).  Every atomic event whose
modulus has such a prime factor is impossible: for
\(D\mid((M+1)/4)^2\), one has \((M,D)=1\), so
\(n\equiv0\pmod p\) cannot equal \(-4D\pmod p\).  Conditional on (31.23),
each remaining distinct atomic residue class has a \(z\)-rough modulus \(M\)
coprime to \(P_z\), so its residue coordinate, including all higher
prime-power digits, remains uniform and has probability exactly \(1/M\).
Atoms with coprime moduli depend on disjoint prime coordinates and hence are
independent of the sigma-algebra generated by their nonneighbors.

Join two atoms when their moduli share a prime.  For an atom \(A\) of modulus
\(M\), set

\[
 x_A={1\over M}\exp\!\left(2\sum_{q\mid M}a_q\right).       \tag{31.24}
\]

For large \(X\), every \(x_A<1/2\): roughness gives
\(\log M\geq\omega(M)\log z\), while \(\max a_q=o(1)\).
By (31.13), its total neighbor activity is at most
\(\sum_{q\mid M}a_q\).  Hence

\[
 \prod_{B\sim A}(1-x_B)
 \geq\exp\!\left(-2\sum_{B\sim A}x_B\right)
 \geq\exp\!\left(-2\sum_{q\mid M}a_q\right),               \tag{31.25}
\]

and therefore
\(\Pr(A)=1/M\leq x_A\prod_{B\sim A}(1-x_B)\).  The
quantitative Lovász local lemma gives

\[
 \Pr(\text{no surviving atom}\mid(31.23))
 \geq\prod_A(1-x_A)
 \geq\exp\!\left(-2\sum_Ax_A\right)
 \geq\exp\{-O(L^3/\log z)\},                               \tag{31.26}
\]

where the last step is (31.14).  Multiplying by the cost of (31.23), and
using (31.11), proves (31.22). ∎

**Corollary 31.5 (H_PF is false; proved).**  Hypothesis H_PF as stated in
§18.4 is false.

*Proof with the quantifiers visible.*  Theorem 18.2 gives
\(\mu_X\geq c_0L^3\).  If H_PF held with constants \(c,C\), choose
\(J\geq C\mu_X\).  Let
\(P_X=\operatorname{lcm}\{M\leq X:M\equiv3\pmod4\}\).  For each fixed
sufficiently large \(X\), take arbitrarily large multiples \(N=mP_X\) that
satisfy \(J\log X\leq\tfrac12\log N\).  The avoider indicator is periodic
modulo \(P_X\), so on every such complete-period interval its proportion is
exactly \(\delta_X\).  Since the H_PF majorant is at least one on every
avoider, its asserted mean would therefore give

\[
 \delta_X={|\operatorname{Av}_X(N)|\over N}
 \ll e^{-c\mu_X}\leq e^{-cc_0L^3}.                         \tag{31.27}
\]

This contradicts (31.22) for all sufficiently large \(X\),
because its negative logarithm is \(o(L^3)\). ∎

This conclusion uses natural density, as §27.3 explicitly allowed.  It does
not depend on interpreting a numerical fit, and it does not assume H_DC.
Theorem 18.6 remains a formally valid implication, but its H_PF antecedent is
now disproved, so it supplies no exceptional-set bound.  Its conclusion has
not been disproved by another argument.

**Assessment 31.6 (ceiling interpretation).**  The cubic first moment of
Theorem 18.2 cannot be assembled into cubic-rate decay even in natural
density by the H_PF mechanism.  This kills the named full-harvest route to
the conditional \(3/4\) exponent and makes Theorem 16.4's
\((\log N)^{2/3}(\log\log N)^{1/3}\) scale the surviving intrinsic-system
benchmark.  This is not a theorem that no different finite-interval method
can improve Theorem 16.4; the missing transfer below is precisely why
“near the true ceiling” remains an assessment rather than a new
exceptional-set lower bound.

### 31.5 Route audit and the finite-interval residual

**Attempt audit 31.7.**

1. **Hall moments / the \(D=1\) model.**  A second moment and
   Paley--Zygmund lower-bound the probability of at least one hit; they point
   in the wrong direction for a lower bound on the void unless the first
   moment is already small.  For \(D=1\), the special factorization fact
   “\(M\equiv3\pmod4\) has a prime \(p\equiv3\pmod4\) to odd exponent”
   turns the complete divisor condition into independent local prime
   exclusions.  For many \(D\)'s this becomes the residue set \(B_p(Y)\) of
   (27.1).  The coordinate freedom in Theorem 27.1 handles all
   \(R\leq Y\); beyond it those sets can fill the available coordinate, and
   the exact uncontrolled cost is still (27.15).  No Hall-style lower-tail
   theorem was found which repairs that conditioned Route-A occupancy.
2. **Nair--Tenenbaum/Henriot.**  This route succeeds for the upper quantities
   it actually addresses.  The determinant-one forms (31.8) prove the
   weighted global mean, and (31.16), split at the coefficient threshold,
   prove the softened neighborhoods.  It does not apply to the nonmultiplicative
   no-divisor indicator and does not by itself produce a lower void.
3. **Suen / cluster expansion.**  Suen's standard useful direction is an
   upper bound for the no-event probability; it does not replace the lower
   local-lemma estimate here.  The softened charges make the ordinary
   quantitative local lemma close in the CRT product space, so no Suen gain
   is needed for natural density.  Pair information alone still does not
   control the alternating finite-interval tail.
4. **Restricted families and mass accounting.**  Restricting all prime
   factors of \(M\) to \((z,z^B]\), for fixed \(B\), lies inside the
   \(z^B\)-smooth family and hence has \(o(L^3)\) raw intrinsic mass by
   Lemma 24.6.  It cannot account for a \((1-o(1))\) portion of the cubic raw
   supply.  After quarantine, Theorem 31.2 bounds the entire rough weighted
   mass by \(O(L^3/\log z)=o(L^3)\); the issue was its dependency geometry,
   not a remaining cubic first moment.

**Hypothesis \(H_{\rm PF}'\) (critical-window variant; open).**  There are
absolute constants \(c,C>0\) and \(0<c_-<c_+\), with \(c_-\) large enough
for the degree budget, such that whenever
\[
 c_-L^4\leq\log N\leq c_+L^4,\qquad
 J\geq C\mu_X,\qquad J\log X\leq\tfrac12\log N,
\]
H_PF's complete-system majorant exists with normalized mean
\(O(e^{-c\mu_X})\).  No assertion is made outside this window.
This restricted hypothesis is **not refuted**.  It would still yield the
conclusion of Theorem 18.6 by taking
\(\log X=\alpha(\log N)^{1/4}\) with a suitable fixed \(\alpha\) and running
the same proof.  Corollary 31.5 instead takes a mean over arbitrarily huge
complete-period multiples at fixed \(X\); it supplies no count in this
critical window.

**Residual finite statement (open).**  The proof above is on the exact CRT
product space, equivalently on complete periods.  It does **not** prove

\[
 |\operatorname{Av}_X(N)|
 \geq N\exp\{-o(L^3)\}
 \qquad\text{uniformly when }\log N\asymp L^4.              \tag{31.28}
\]

On \([1,N]\), intersections of at most \(j\) congruence atoms have the CRT
main term plus an \(O(1)\) rounding error, but the local lemma does not by
itself give a degree-\(j\) polynomial whose odd truncation retains the lower
bound (31.26).  A finite transfer needs a convergent event-cluster expansion
with a quantitatively controlled tail and coefficient sum through
\(j=O(L^3)\); only then would the lcm budget \(X^j\leq N^{O(1)}\) and the
aggregate rounding errors fit inside \(\log N\asymp L^4\).  No such transfer
is proved here.  Complete periods (or sufficiently large multiples of them)
do give (31.22), which is enough for Corollary 31.5 but can have
\(\log N\) exponentially larger than the critical \(L^4\) scale.

### 31.6 Numerical companion

`verify.py (ad)` exactly enumerates every intrinsic class and every rough
atomic event for \(X\leq200\).  It checks
\(F(M)\leq\tau_3((M+1)/4)\), every determinant-one representation (31.16),
and the shared-prime sums.  For a deliberately mild finite-scale charge
\(a_q=0.02L^3/(q\log z)\), it reports the global weighted sum and both the
full and diagonal-removed neighborhood ratios to \(b_q\), as well as the
full ratio \(T_q/a_q\).  These are shape diagnostics only: at these tiny
\(X\), the displayed \(T_q/a_q>1\) confirms that the toy charge does not
verify the asymptotic local-lemma inequality.

\[
\begin{array}{c|c|r|c|c|c|c|c}
X&z&\#\{M\text{ rough}\}&S_0&S_a/(L^3/\log z)
 &\max_q T_q/b_q&\max_q T_q/a_q
 &\max_q(T_q-\text{diagonal})/b_q\\ \hline
80&3&13&2.63779&.04715&.20448&10.22399&.05730\\
120&3&20&3.36391&.05491&.15887&7.94364&.09340\\
160&5&21&3.25440&.05087&.19332&9.66620&.09144\\
200&5&27&3.71965&.05165&.29870&14.93507&.09310
\end{array}                                                 \tag{31.29}
\]

The computation supports neither an asymptotic constant nor the original
\(a_q=O(b_q)\) shape.  Its useful regression is structural: the prime
diagonal is visibly the largest finite-scale addition, exactly the term
isolated by \(u_q\) in Theorem 31.3.

## 32. Certification audit for the \(k=1\) Type-II slice, and its actual exceptional-set bound

This section distinguishes an identity which gives *some* Type-II tuple from
one which gives a tuple with Type-II multiplier \(k=1\).  The distinction
changes the available prime-modulus mass by a full logarithm.  In particular,
the quadratic prime-modulus mass in §§15, 21, and 24 is **not** a \(k=1\)
supply.  The strongest bound obtained below from a proved \(k=1\)-certifying
prime-modulus system consequently has exponent \(1/2\), not \(2/3\).

### 32.1 Exact certification dictionary

Write

\[
        M=4H-1,\qquad H=(M+1)/4.
\]

**Lemma 32.1 (the multiplier of an intrinsic witness; proved).**  Let
\(M\equiv3\pmod4\), let \(D\mid H^2\), and choose a Lemma-18.1
factorization

\[
        H=uvw,\qquad D=u^2w.
\]

Let \(P\) be a prime with \((P,H)=1\) in the intrinsic class
\(P\equiv-4D\pmod M\), and put

\[
        s={Pv+u\over M}.
\]

Then Lemma 16.1 gives the (not necessarily canonical) Type-II tuple

\[
        (a,b,c,k)=(s,u,w,v).                                  \tag{32.1}
\]

If \(g=(u,v)\), its canonical Theorem-17.1 tuple is

\[
 (a_0,b_0,c_0,k_0)=\left({s\over g},{u\over g},g^2w,{v\over g}\right),
 \qquad
 k_0={v\over g}={H\over(H,D)}.                               \tag{32.2}
\]

Consequently this particular intrinsic witness has \(k_0=1\) if and only if
\(H\mid D\).  Thus intrinsic does **not** imply \(k=1\): for example
\((P,M,D)=(409,7,1)\) gives \((117,1,1,2)\), while 409 has no \(k=1\)
tuple at all.

*Proof.*  The defining equations give

\[
 Ms=Pv+u,
 \qquad
 4suvw=s+Pv+u,
\]

so \(vP=4suwv-s-u\), which is (17.1) with (32.1).  Since
\((P,u)=1\), reducing \(Ms=Pv+u\) modulo every common divisor with \(u\)
and using \((M,u)=1\) gives \((s,u)=(v,u)=g\).  The replacement in (32.2) preserves all three unit-fraction denominators:
\[
 (s/g)(u/g)(g^2w)=suw,
 \quad P(s/g)(g^2w)(v/g)=Pswv,
 \quad P(u/g)(g^2w)(v/g)=Puwv.
\]
Moreover \((s/g,u/g)=1\), so this is exactly the canonical reduction, without
any appeal to an unstated step from Theorem 17.1.  Finally

\[
 (H,D)=(uvw,u^2w)=uw(u,v),
\]

which proves the displayed formula for \(k_0\) and its last assertion. ∎

**Corollary 32.2 (what the §15 identity certifies; proved).**  In the notation
of Lemma 15.1,

\[
 D=Td_1^2<H,
 \qquad
 k_0={H\over(H,D)}={d_2\over(d_1,d_2)}=v>1.                 \tag{32.3}
\]

Thus every *explicit witness constructed in §15* has \(k>1\), never
\(k=1\).  An entire lower progression can nevertheless coincide with one of
the uniform fixed-\((B,C)\), \(k=1\) progressions: among the
\(f(M)=(\tau(H^2)-1)/2\) distinct lower-half classes \(-4D\), \(D<H\), this
occurs exactly when

\[
                  4D\mid H.                                 \tag{32.4}
\]

Indeed a lower class \(-4D\) equals a fixed-parameter \(k=1\) class
\(-t\), \(t\mid H\), if and only if \(4D=t\).  Hence the progression-level
overlap has exactly \({\bf1}_{4\mid H}\tau(H/4)\) classes.  This does not
decide whether an individual target has an unrelated \(k=1\) tuple.  The
regression is the common intrinsic class \(3\pmod7\): its member \(17\) has
the \(k=1\) tuple \((A,B,C)=(1,6,1)\), while its member \(409\) has no
\(k=1\) tuple.  None of this changes the multiplier (32.3) of Lemma 15.1's
displayed identity.

The exact \(k=1\) part of the intrinsic system has a simpler description.

**Lemma 32.3 (the \(k=1\) class system and its two masses; proved).**  For
\(M=4H-1\), put

\[
 \mathscr K(M)=\{-t\pmod M:t\mid H\}.                       \tag{32.5}
\]

This system is complete within the intrinsic/fixed-divisor affine class
dictionary.  Every positive integer \(P\) in the class \(-t\pmod M\) has a \(k=1\)
Type-II tuple.  More explicitly, if \(P=jM-t\), \(j\geq1\), then

\[
              (A,B,C,k)=(j,t,H/t,1),
 \qquad P=4ABC-A-B.                                         \tag{32.6}
\]

The classes in (32.5) are distinct, so \(|\mathscr K(M)|=\tau(H)\).  They
are exactly the intrinsic classes represented by \(D=Ht\), \(t\mid H\),
and exactly the fixed-divisor classes from

\[
 (4AC-1)(4BC-1)=4PC+1                                      \tag{32.7}
\]

in which \(M=4BC-1\).  Equivalently, writing \(C=H/t\),

\[
 M\equiv-1\pmod {4C},\qquad
 P\equiv-(4C)^{-1}\equiv-t\pmod M.                         \tag{32.8}
\]

Conversely, any \(k=1\) tuple satisfies
\(P=A(4BC-1)-B\); taking \(M=4BC-1\), \(H=BC\), and \(t=B\) recovers one
of (32.5).  This classifies fixed-parameter affine identities in the
intrinsic dictionary, not arbitrary residue classes modulo an externally
prescribed \(M\) whose parameters may vary with the target.

The complete, generally composite-modulus system has exact asymptotic mass

\[
 \sum_{\substack{M\leq X\\M\equiv3\ (4)}}
       { |\mathscr K(M)|\over M}
   ={1\over8}(\log X)^2+O(\log X).                          \tag{32.9}
\]

Its **prime-modulus** subsystem has only linear logarithmic mass:

\[
 \sum_{\substack{\ell\leq X\\\ell\equiv3\ (4)\\\ell\ \mathrm{prime}}}
       { |\mathscr K(\ell)|\over\ell}
       \asymp\log X.                                        \tag{32.10}
\]

*Proof.*  Equation (32.6) is immediate, and distinct divisors \(t\leq H<M\)
give distinct residues.  For \(D=Ht\),
\(-4D\equiv-t\pmod M\), since \(4H\equiv1\pmod M\); Lemma 32.1 gives the
converse inside the parametrized intrinsic system.  Equations (32.7)--(32.8)
are the same calculation in Theorem 17.1(iii)'s divisor dictionary.

For (32.9), substitute \(M=4H-1\) and use

\[
 \sum_{H\leq Y}{\tau(H)\over H}
       ={1\over2}(\log Y)^2+O(\log Y),
 \qquad {1\over4H-1}={1\over4H}+O(H^{-2}).
\]

For (32.10), work dyadically.  The upper bound
\(\tau(H)\leq2\sum_{t\mid H,\ t\leq\sqrt H}1\), followed by
Brun--Titchmarsh for \(\ell\equiv-1\pmod {4t}\), gives

\[
 \sum_{x<\ell\leq2x}\tau((\ell+1)/4)\ll x.
\]

For the lower bound retain \(t\leq x^{1/3}\); Bombieri--Vinogradov and
\(\sum_{t\leq y}1/\varphi(4t)\asymp\log y\) give the reverse bound
\(\gg x\).  Thus, uniformly for large \(x\),
\[
 \sum_{\substack{x<\ell\leq2x\\\ell\equiv3\ (4)\\
                         \ell\ \mathrm{prime}}}
       \tau((\ell+1)/4)\asymp x.
\]
After division by \(\ell\asymp x\), every dyadic block has mass
\(\Theta(1)\).  In particular the exact range \(\sqrt X<\ell\leq X\) has
mass \(\Theta(\log X)\), which is the form used in Theorem 32.4.  This is
the one-divisor analogue of Lemma 24.3. ∎

This resolves the mass subtlety.  The §15/§24 prime system has
\(f(\ell)=(\tau(H^2)-1)/2\) and mass \(\asymp(\log X)^2\), but its displayed
witnesses have the multipliers (32.3).  The \(k=1\)-certifying prime system
has only \(\tau(H)\) classes and mass \(\asymp\log X\).  Quadratic mass does
reappear in (32.9), but the full collection of those moduli is not pairwise
coprime.  Its intersections are governed by lcms, which can be much smaller
than products; compositeness by itself is not the obstruction.  The
Selberg/Rankin proof of Theorem 21.3 or 24.4 therefore cannot be applied to
(32.9) by replacing the independent prime moduli with the full correlated
collection.  No sentence in §§18 or 21 calls the intrinsic system a \(k=1\)
supply; no stale-phrasing repair is needed there.

### 32.2 An unconditional bound for primes without a \(k=1\) Type-II tuple

Define

\[
 E_{II,1}(N)=\#\{P\leq N:P\text{ prime and there are no }A,B,C\geq1
                         \text{ with }P=4ABC-A-B\}.
\]

**Theorem 32.4 (proved; no literature-priority claim).**  There is an
absolute constant \(c>0\) such that, for all sufficiently large \(N\),

\[
             E_{II,1}(N)\ll
             N\exp\{-c\sqrt{\log N}\}.                      \tag{32.11}
\]

The same bound holds for all positive integers lacking a representation
\(n=4ABC-A-B\).

*Proof.*  Use the prime moduli \(X^{1/2}<\ell\leq X\),
\(\ell\equiv3\pmod4\), and forbid the \(\tau((\ell+1)/4)\) classes
(32.5).  By Lemma 32.3 their mass \(\mu\) is \(\asymp\log X\), and every
integer counted in the theorem avoids all of them.  Put

\[
 g(\ell)={|\mathscr K(\ell)|\over
                 \ell-|\mathscr K(\ell)|},\quad
 G=\prod_\ell(1+g(\ell)),\quad
 S(Q)=\sum_{\substack{s\leq Q\\s\mid\prod\ell}}
       \mu^2(s)\prod_{\ell\mid s}g(\ell),
 \qquad Q=N^{1/2}.
\]

For large \(X\), \(|\mathscr K(\ell)|=\ell^{o(1)}<\ell/2\).  The standard
Selberg upper-bound sieve gives at most \(O(N/S(Q))\) avoiders.  As in
(16.14) and Theorem 21.3, Rankin's trick with \(v=1/\log X\) gives

\[
 {G-S(Q)\over G}
 \leq\exp\left\{-{\log N\over2\log X}+C\log X\right\}.      \tag{32.12}
\]

Thus \(S(Q)\geq G/2\geq\tfrac12\exp(c_1\log X)\) whenever
\(\log N\geq C_2(\log X)^2\).  Choose
\(\log X=\alpha\sqrt{\log N}\) with a sufficiently small fixed
\(\alpha>0\).  This proves (32.11), including the stronger integer
statement. ∎

**Assessment (why the expected \(2/3\) does not follow).**  If the quadratic
mass (32.9) admitted a product-like Selberg assembly, the formal balance
\((\log X)^2\lesssim\log N/\log X\) would indeed give exponent \(2/3\).
But (32.9) comes from a full composite-modulus collection that is not
pairwise coprime, while the proved independent prime-modulus mass is (32.10).
Intersections in the full collection have density governed by lcms, not
products, and fixed-\(t\) subfamilies are visibly shifted-divisor clusters.
Proving the required composite assembly would be a new correlation theorem
of the same kind carefully withheld in §§18, 21, and 24.  Thus (32.11), with
exponent \(1/2\), is the strongest bound proved here from the independent
prime-modulus subsystem, and the present proof does not yield \(2/3\).
Nothing here rules out a selective coprime or low-correlation composite
subfamily, or a different use of the identities.

**Numerical companion (informational).**  The truncated ratios

\[
 \left({\sum_{M\leq X}|\mathscr K(M)|/M\over(\log X)^2},
       {\sum_{\ell\leq X}|\mathscr K(\ell)|/\ell\over\log X}\right)
\]

at \(X=10^2,10^3,10^4,10^5\) are respectively

\[
 (0.12035,0.36688),\ (0.11991,0.42230),\
 (0.12058,0.45885),\ (0.12115,0.48446),                    \tag{32.13}
\]

consistent with (32.9)--(32.10).  The observed \(k=1\)-less decade counts
\(0/2,2/12,2/129,2/1038,3/8551\) are also compatible with the upper-bound
shape.  For the four nonzero rows,
\(-\log(\text{fraction})/\sqrt{\log(\text{upper endpoint})}\) is
\(0.68,1.37,1.84,2.14\).  This finite monotone drift neither estimates the
unspecified constant in (32.11) nor supports a sharper exponent.

### 32.3 Exact anatomy of the nine primes through one million

The \(k=1\)-lessness was replayed independently using (28.7), with every
\(1\leq A\leq\lfloor\sqrt{P/2}\rfloor\) and every divisor of \(P+A\).
All Type-II rows were then enumerated by the complete \((A,B)\) bound, not by
a stored witness table.  The minimizing tuples below are displayed up to
\(A\leftrightarrow B\).

\[
\begin{array}{r|c|l|r@{\ }l}
P&\min k& (A,B,C)\text{ at }\min k
 &\#\text{Type-I}&(\#\text{ primitive})\\ \hline
409&2&(1,13,8),(1,21,5),(1,117,1),(7,15,1)&22&(18)\\
577&2&(1,5,29),(1,21,7),(1,77,2),(1,165,1)&22&(22)\\
5569&2&(1,141,10),(1,237,6),(9,157,1)&40&(34)\\
9601&2&(1,37,65),(1,173,14),(3,115,7),(3,835,1)&40&(34)\\
23929&2&(1,21,285),(1,53,113),(1,301,20),(1,6837,1),
       (3,19,105),(7,15,57)&196&(128)\\
83449&2&(3,211,33),(43,243,2)&70&(64)\\
102001&3&(5,232,22)&106&(82)\\
329617&2&(1,5,16481),(1,213,387),(1,9285,9),(1,43949,2),
        (5,41,402)&230&(184)\\
712321&2&(1,69,2581),(1,253,704),(1,1877,95),(1,61941,3),
        (3,499,119),(3,571,104),(13,2745,5),(153,1165,1)&150&(122)
\end{array}                                                  \tag{32.14}
\]

Type-I counts are ordered in \((A,B)\), exactly as in §26.1; “primitive”
means \((A,B)=1\).  They were independently recovered from ordered unit
fraction solutions.  For sorted denominators \(x\leq y\leq z\), the unit
fraction equation gives the complete range
\[
                         P/4<x\leq3P/4:
\]
the strict lower bound follows from \(4/P>1/x\), and the upper bound from
\(4/P\leq3/x\).  Thus the denominator scan is cutoff-free.  For every
integer \(x\) in that range, put \(q=4x-P\), \(R=Px\), and enumerate every
\(d\mid R^2\), \(d\leq R\), with
\(q\mid d+R\).  The two-term dictionary gives

\[
 y=(R+d)/q,\qquad z=(R+R^2/d)/q.
\]

Filtering \(P\nmid xy\), \(P\mid z\) gives every canonical Type-I row; with
\(h=(x,y)\), it is

\[
 A=x/h,\quad B=y/h,\quad C={zh^2\over Pxy},\quad K=h/C.
\]

Every nonprimitive §26.1 row is then obtained uniquely by
\((A,B,C,K)\mapsto(gA,gB,C/g^2,gK)\) with \(g^2\mid C\).  This is an
independent exact check of the divisor-form counts in (32.14).

For additional case anatomy, let \(Q_B(P)\) be the set of distinct criterion
moduli \(q=(A+B)/K\) among all Type-II rows, and let \(Q_A(P)\) be the
analogous \(m=(A+B)/K\) set among all Type-I rows.  The exact finite sets have
sizes and intersections

\[
\begin{array}{r|r|r|l}
P&|Q_A|&|Q_B|&Q_A\cap Q_B\\ \hline
409&5&3&\varnothing\\
577&9&6&7,39\\
5569&12&9&39,47,143\\
9601&11&6&\varnothing\\
23929&36&13&7,11,39,303\\
83449&25&10&39,191\\
102001&25&16&47,111,115\\
329617&71&20&3,107,167,21975\\
712321&49&21&35,191
\end{array}                                                  \tag{32.15}
\]

Thus none of the nine is globally Case-A-only or Case-B-only: every one has
both types.  At the finer criterion-modulus level every prime has nonempty
\(Q_A\setminus Q_B\) and \(Q_B\setminus Q_A\); seven also have a modulus
supporting both cases, while 409 and 9601 have disjoint modulus sets.

**Measured pattern.**  Eight of the nine first solve Type II at \(k=2\), but
102001 first solves at \(k=3\).  Thus “all have \(k=2\)” is already false,
while there is no monotone growth of the minimum with \(P\).  The sample is
too small for a distributional claim.

**Computational Search 32.5 (exact finite census).**  The same independent
denominator-side enumerator stops at the first Type-I row for each odd prime
\(P\leq10^5\).  It finds no Type-I-less prime among all 9,591 odd primes in
that range.  This is a finite statement only; it does not make Type I
pointwise sufficient.

`verify.py (ae)` checks Lemma 32.1 on 809 floor/parity intrinsic
factorizations (338 with \(k=1\)), checks 171 §15 instances, 1,014 direct
class identities, the (17, 409) class/target regression, and the exact
nine-prime table, then performs the Type-I-less scan through \(10^5\).  It
reproduces the four finite mass-ratio rows in (32.13); it does not
machine-check either mass asymptotic or Theorem 32.4.  The default block is
memory-bounded and runs in under ten seconds on the campaign host.

---

## 33. The critical-window transfer: cylinder and local-sieve walls

Put \(L=\log X\), and retain the complete intrinsic avoider
\({\rm Av}_X\) of §21.  This section attacks the finite-window residual
(31.28).  The conclusions are deliberately scoped.  The small-cylinder wall,
the raw residual count (together with the complete redundancy of its witnesses), the
conditional finite-transfer criterion, and the failure of prime-power tensor
factorization are **proved**.  The Moser--Tardos and classical beta-sieve
paragraphs assess only the literal implementations specified below, not every
algorithmic localization or hypergraph sieve.  The target (31.28), and hence
\(H_{\rm PF}'\), remain **OPEN**.

### 33.1 What the local lemma does not localize

There is an immediate obstruction to turning Theorem 31.4 into a union of
small-modulus classes.

**Theorem 33.1 (exact all-avoider cylinder wall; proved).**  Suppose that a
nonempty union \(\mathcal U\) of complete residue classes modulo \(Q\)
satisfies

\[
                         \mathcal U\subseteq {\rm Av}_X.     \tag{33.1}
\]

Then

\[
 \prod_{\substack{\ell\leq X\\ \ell\equiv3\ (4)\\
                   \ell\ \text{prime}}}\ell\mid Q,
 \qquad
 \log Q\geq(1/2+o(1))X.                                    \tag{33.2}
\]

In particular \(\log Q\) is not \(o(L^4)\); it is exponentially larger
than the critical-window budget.

*Proof.*  Choose one class \(a\pmod Q\) in \(\mathcal U\).  For every prime
\(\ell\equiv3\pmod4\), \(\ell\leq X\), the divisor \(D=1\) gives the
intrinsic forbidden class \(-4\pmod\ell\).  If \(\ell\nmid Q\), the Chinese
remainder theorem supplies an integer which is \(a\pmod Q\) and
\(-4\pmod\ell\).  It belongs both to the complete class in \(\mathcal U\)
and to a forbidden class, a contradiction.  Thus every such \(\ell\)
divides \(Q\).  The last estimate is the prime number theorem in the
progression \(3\pmod4\). ∎

This theorem also rules out a decomposition of the local-lemma support into
nonempty, all-avoider cylinders of modulus \(\exp\{o(L^4)\}\).  It does not
rule out a cylinder which leaves a correction family to be sieved.  That
distinction is decisive.  The prime-modulus correction has
\(\Theta(X/L)\) coordinates and total coordinate product
\(\exp\{\Theta(X)\}\), but only quadratic class mass; Theorems 24.4 and
27.1 transfer it by a degree-\(O(L^2)\) Bonferroni argument.  Thus “small
correction” can mean small sieve degree, but cannot mean small total modulus
product.

The same issue appears in a literal hybrid consisting of a certificate for
\(R\leq Y\) followed by the §31 local lemma on the remaining atoms.

**Proposition 33.2 (raw-list inflation and complete redundancy of the
witnesses; proved).**  Let \(z,Y=X^{o(1)}\), with \(z\to\infty\).  Before
removing implied atoms, the family of composite, \(z\)-rough intrinsic atoms
with \(R>Y\) contains

\[
                 \gg {X\over L\log z}                       \tag{33.3}
\]

distinct moduli \(M\asymp X\).  Consequently the logarithm of the ordinary
product of these listed moduli (with repeated prime coordinates) is

\[
                 \gg {X\over\log z}\gg L^4.               \tag{33.4}
\]

The lcm of the listed moduli also has logarithm \(\gg X/z\gg L^4\).
Nevertheless, **every atom constructed in the proof is logically implied by
a prime-modulus atom** and hence disappears under prime-modulus
deduplication.

*Proof.*  Take primes
\[
 p\in(z,2z],\quad p\equiv3\pmod4,
 \qquad
 q\in[X/(8z),X/(4z)],\quad q\equiv1\pmod4.
\]
For large \(X\), the two ranges are disjoint and \(q>z\).  The products
\(M=pq\) are distinct, \(z\)-rough, \(M\equiv3\pmod4\), and
\(X/8<M\leq X/2\).  The prime number theorem in the two progressions gives
\(\gg X/(L\log z)\) such products.  Put \(A=(M+1)/4\).  Then \(A>Y\),
and the choice \(R=A,s=1,D=A^2\) is one of the exact atoms (21.4), with
\(R>Y\).  Finally each selected modulus has logarithm \(\asymp L\), which
proves (33.4).  Every prime \(q\) in the displayed interval occurs in a
selected product, so their product divides the lcm; the prime number theorem
gives
\[
 \log\operatorname {lcm}(M:M\text{ selected})
 \geq\sum_q\log q\gg X/z.
\]
For the logical redundancy, modulo any odd \(m\) put \(A_m=(m+1)/4\).  The
maximal atom \(D=A_m^2\) is
\[
 n\equiv-4A_m^2\equiv-4^{-1}\pmod m.
\]
Thus for every selected \(M=pq\), its constructed atom implies
\(n\equiv-4^{-1}\pmod p\), which is exactly the maximal intrinsic atom for
the prime modulus \(p\). ∎

The qualification “before removing implied atoms” is therefore essential:
the entire displayed witness family, not merely part of it, is deleted by
the prime-modulus conditions.  Proposition 33.2 is only a warning that the
**literal raw list** and even its CRT lcm can be huge while its irredundant
support is not.  It gives no lower bound for a minimal residual family;
constructing a large family which survives prime-modulus and other logical
deduplication remains open.

**Assessment (standard Moser--Tardos run).**  In the vanilla implementation,
the variables are the prime-power CRT coordinates, the initial assignment is
uniform on their full product, and a violated event resamples every coordinate
in its modulus.  The expected resampling and witness-tree bounds used here do
not control the least positive representative of the resulting CRT residue.
Starting instead with a uniform integer in \([1,N]\) loses exact product
independence once a queried coordinate product exceeds \(N\).  Theorem 33.1
also excludes covering the output support by complete all-avoider cylinders
of critical-window modulus.  Consequently the standard full-product run
provides **no localization estimate proved here**.  This is not a no-go for a
non-cylinder algorithm, an output-distribution or bounded-witness argument,
or a correction-sieve adaptation; all such localization variants remain
open.

There is nevertheless **no modulus-budget no-go** for a suitably truncated
correction polynomial.  The exact missing object can be isolated as follows.
After the quarantine (31.23), transform the surviving congruences to the
integer variable left after division by \(P_z\), and denote their indicators
by \(1_A\).

**Lemma 33.3 (conditional finite-transfer criterion; proved).**  Take
\[
 z={L^3\log\log L\over\log L}
\]
as in (31.11).  Suppose there are real coefficients \(c_S\), supported on
sets of at most \(r=o(L^3)\) surviving atoms, such that

\[
 B_X(n):=\sum_S c_S\prod_{A\in S}1_A(n)
       \leq \mathbf1_{\{\text{no surviving atom at }n\}}    \tag{33.5}
\]

pointwise, and, in the exact CRT product space,

\[
 \mathbb E_{\rm CRT}B_X\geq\exp\{-o(L^3)\},
 \qquad
 \log\sum_S|c_S|=o(L^4).                                   \tag{33.6}
\]

Then, uniformly for \(\log N\asymp L^4\),

\[
 |{\rm Av}_X(N)|\geq N\exp\{-o(L^3)\}.                     \tag{33.7}
\]

*Proof.*  The quarantine costs
\(P_z=\exp\{O(z)\}=\exp\{o(L^3)\}\).  For every compatible set \(S\),
the product in (33.5) is one residue class modulo the lcm \(d_S\), so on an
interval of length \(N/P_z+O(1)\) its sum is
\(N/(P_zd_S)+O(1)\); for an incompatible set both the interval and CRT
sums vanish.  Summing (33.5) therefore gives the CRT main term with total
error at most \(\sum_S|c_S|\).  Equations (33.6) and
\(\log N\asymp L^4\) make that error negligible.  Explicitly,
\(rL=o(L^4)\), \(\log\sum_S|c_S|=o(L^4)\), and the positive CRT main term
has logarithm \(\log N-o(L^3)\).  Also
\(d_S\leq X^r=\exp\{o(L^4)\}\), so every term lies inside the advertised
degree budget. ∎

This criterion shows exactly why raw cardinality is not the final wall.  The
number \(K\) of atoms is \(\exp\{O(L)\}\), by the standard maximal-order
divisor bound.  The §31 activity is
\[
       \sum_Ax_A\ll L^3/\log z\asymp L^3/\log L.            \tag{33.8}
\]
Hence a polynomial of degree \(r=O(L^3/\log L)\) with unit-size
coefficients would have the *a priori* ledger
\(K^r=\exp\{O(L^4/\log L)\}\), which fits (33.6).  Odd Bonferroni provides
the pointwise inequality (33.5), but no estimate proved here keeps its CRT
expectation positive at that degree: compatible atoms sharing prime
coordinates can make the high factorial moments much larger than powers of
(33.8).  Conversely the LLL lower bound (31.26) is not itself a pointwise
polynomial minorant.  A convergent hypergraph-sieve or event-cluster
minorant satisfying (33.5)--(33.6) would prove the desired theorem; none is
constructed here.

### 33.2 Why the proposed Fourier product is not a product

The CRT **space** is a product over prime powers, but the complete avoider
**indicator** is not.  If \(\mathcal A\) is the atomic family, then

\[
 \mathbf1_{{\rm Av}_X}(n)
 =\prod_{A\in\mathcal A}
   \left(1-\prod_{p^e\Vert M_A}
       \mathbf1_{\{n\equiv r_A\ (p^e)\}}\right).            \tag{33.9}
\]

Each inner event factors over its coordinates.  The outer factors overlap,
so Fourier transformation turns their product into a convolution, not a
product of local Fourier transforms.

**Lemma 33.4 (explicit tensor obstruction; proved).**  Already at \(X=15\),
the complete avoider indicator modulo
\(1155=3\cdot5\cdot7\cdot11\) does not factor into functions of the four
prime coordinates.

*Proof.*  The four residues
\[
\begin{array}{c|cc|cc|c}
 n&n\bmod3&n\bmod5&n\bmod7&n\bmod11&\mathbf1_{{\rm Av}_{15}}(n)\\ \hline
231 &0&1&0&0&1\\
616 &1&1&0&0&1\\
693 &0&3&0&0&1\\
1078&1&3&0&0&0
\end{array}                                                  \tag{33.10}
\]
form a two-coordinate rectangle with the other coordinates fixed.  A tensor
product containing the first three corners must contain the fourth.  Directly,
1078 is killed by the class \(13\pmod {15}\), arising from \(D=8\mid4^2\),
while the first three residues avoid every participating modulus. ∎

Consequently a Fourier coefficient at a CRT character \(\chi\) has the
expansion

\[
 \widehat{\mathbf1_{{\rm Av}_X}}(\chi)
 =\sum_{S\subseteq\mathcal A}(-1)^{|S|}
   \mathbb E_{\rm CRT}\!\left[
      \overline\chi\prod_{A\in S}1_A\right],               \tag{33.11}
\]

which is a hypergraph partition function with a complex external field.
Theorem 31.4 controls only the untwisted, positive void probability.  Its
LLL inequalities give no absolute or signed bound for (33.11).  In
particular, the standard interval identity

\[
 |{\rm Av}_X(N)|=N\delta_X+
   \sum_{\chi\ne1}\widehat{\mathbf1_{{\rm Av}_X}}(\chi)
                         K_N(\chi)                           \tag{33.12}
\]

has no usable error estimate from the local factors, because those local
factors do not exist for the full indicator.  For the direct prime-local
certificate of Theorems 24.8 and 27.1 they do exist; its Fourier/Bonferroni
transfer is exactly the already-proved certificate, with the
\(H_Y\log L\) cost wall.

### 33.3 The weighted fundamental-lemma attempt

The softened charges in Theorem 31.3 look at first like a growing-dimensional
sieve density.  This analogy gives the correct degree budget but the wrong
main term.  Ignore the nonnegative \(u_q\) for the moment and put
\(g(q)=b_q=L^3/(q\log z)\).  Mertens' theorem gives

\[
 \sum_{z<q\leq X}b_q
 ={L^3\over\log z}
   \{\log\log X-\log\log z+O(1)\}
 =(1/3+o(1))L^3,                                             \tag{33.13}
\]

for the cutoff (31.11).  On the other hand

\[
 \sum_{w<q\leq y}b_q\log q
 \sim {L^3\over\log z}\log(y/w).                           \tag{33.14}
\]

Thus the formal sieve dimension is
\(\kappa\asymp L^3/\log z=o(L^3)\), and the available level parameter
\(s=\log N/\log X\asymp L^3\) beats it by a factor \(\asymp\log L\).
This is enough room to approximate the corresponding Euler product.  It
does not make that product large:

\[
             \prod_{z<q\leq X}(1-b_q)
             =\exp\{-\Theta(L^3)\}.                         \tag{33.15}
\]

**Calculation/Assessment 33.5 (scoped local-charge substitution).**  Make
the literal classical-sieve substitution in which the local density at
\(q\) is the §31 neighborhood charge \(a_q=A(b_q+u_q)\), or even only a
fixed positive multiple of \(b_q\), and the resulting main term is the
corresponding Euler product.  By (33.13) that product is at most
\(\exp\{-cL^3\}\), so this stated substitution does not yield (33.7).  The
fact that \(s\gg\kappa\) controls its fundamental-lemma approximation error,
not the cubic loss already present in its main term.  The \(u_q\) terms can
only increase that loss; no growing-dimension bound for their unweighted sum
is asserted here.  This calculation is not an impossibility theorem for an
undefined class of all “classical” sieve arguments.

The reason this loses the gain of Theorem 31.4 is structural.  The
neighborhood charge \(a_q\) is not the density of a set of forbidden
residues at coordinate \(q\).  It charges every hyperedge incident to
\(q\), and summing it over \(q\) counts the same composite atom at several
coordinates.  The LLL instead pays each atom once, through (33.8), and uses
the neighborhood inequalities only to control dependencies.  If one tries
to use the atom activities \(x_A\) as the sieve densities, the desired Euler
cost becomes subcubic, but classical multiplicativity disappears:
intersections of atoms sharing a prime have density \(1/\operatorname{lcm}
(M_A,M_B)\), not \(1/(M_AM_B)\).  Therefore the beta-sieve convolution and
Rosser-weight proof do not apply.

A genuinely weighted **hypergraph** fundamental lemma, with the LLL
neighborhood inequalities replacing multiplicative local densities and
with a pointwise minorant as in Lemma 33.3, would close the critical window.
Neither the ordinary fundamental lemma nor the LLL product-measure bound is
such a theorem.  This is the precise failure point of the most promising
transfer attempt.

### 33.4 Status and finite companion

**Assessment 33.6 (critical-window status).**  The estimate

\[
 |{\rm Av}_X(N)|\geq N\exp\{-o(L^3)\},
       \qquad \log N\asymp L^4,                             \tag{33.16}
\]

is not proved.  Accordingly \(H_{\rm PF}'\) is **OPEN**, and the conditional
\(3/4\) route is not settled.  At this window the unconditional full-system
bounds available here remain only

\[
 \lfloor\sqrt N\rfloor\leq |{\rm Av}_X(N)|
       \ll N\exp\{-cL^2\},                                  \tag{33.17}
\]

by Lemma 21.2 and Theorem 21.3.  The lower side is exponentially too small
on the \(L^3\) scale.  The exact route failures are:

1. an all-avoider small cylinder is impossible by Theorem 33.1; the literal
   large-\(R\) list in Proposition 33.2 is huge but all of its displayed
   witnesses are prime-implied; the standard Moser--Tardos bounds used here
   provide no localization estimate;
2. the full indicator has no prime-power Fourier product, by Lemma 33.4, so
   the desired exponential-sum bound is the original hypergraph correlation
   problem in complex form;
3. replacing the local sieve density by \(a_q\) pays cubic cost before the
   fundamental lemma starts, while replacing it by \(x_A\) loses the
   multiplicative sieve axioms.

The sharp surviving opportunity is not a larger modulus budget: the ledger
in (33.8) fits the critical window.  It is the construction of the
pointwise, low-degree hypergraph minorant in Lemma 33.3, or an equivalent
signed Fourier/cluster estimate.  No argument here rules out such a new
transfer theorem.

**Computational 33.7 (informational).**  Exact cyclic windows in complete
periods give

\[
\begin{array}{c|r|r|r|r|r}
X&P_X&|{\rm Av}_X\bmod P_X|&W&\min& W\delta_X&\max\\ \hline
15&1155&256&100&18&22.1645&27\\
15&1155&256&1000&217&221.6450&226\\
23&504735&57344&100&4&11.3612&21\\
23&504735&57344&1000&98&113.6121&128\\
23&504735&57344&10000&1110&1136.1209&1161\\
23&504735&57344&100000&11340&11361.2093&11385
\end{array}                                                  \tag{33.18}
\]

Here the minimum and maximum range over all cyclic starting points, and the
average is exactly \(W\delta_X\).  These tiny periods show both visible
short-window discrepancy and eventual averaging; they do not test the
asymptotic critical regime.  `verify.py (af)` reconstructs the two periods,
checks every entry in (33.18), checks the cyclic average identity, and
replays the non-tensor rectangle (33.10).  The block is exact and runs in
under ten seconds by default.

## 34. The prime-slice harvesting wall: a direct assault on \(H_{k\rm BV}\) — CLAIMED/PROVISIONAL

This section separates the literal error-sum hypothesis from the job for
which it was introduced.  The literal hypothesis remains open.  Its
prime-slice consequence, however, can be obtained unconditionally after a
congestion pruning which removes \(o(1)\) of the weighted box/main-term mass.
The key is to use the congruence \(k\mid u+cv\), which the multiplicity bound
(18.11) discarded.  Labels are strict: literature comparisons are
assessments; the incidence moment and the pruned prime-slice theorem are
proved internally, but the new theorem remains **CLAIMED/PROVISIONAL** until
external priority and referee checks are complete.

### 34.1 The hypothesis, all quantifiers, and its current logical role

**Hypothesis \(H_{k\rm BV}(\kappa)\) (restated, not assumed here).**  Fix one
constant \(0<\kappa<1/240\).  There is a function
\(\rho_\kappa(X)\to0\) such that the following holds for every sufficiently
large \(X\), uniformly in all the data below:

* \(X^{1/2}\leq x\leq X\) and \(K_0\leq K\leq X^\kappa\);
* \(\mathcal J\) is any subfamily of
  \(\{k\leq K:k\equiv1\pmod4\}\) containing \(1\),
  \(L_{\mathcal J}=\operatorname {lcm}_{k\in\mathcal J}k\), and
  \(h(\mathcal J)=\sum_{k\in\mathcal J}\varphi(k)/k^2\);
* \(c\pmod {24L_{\mathcal J}}\) is any reduced residue;
* \(H=K^{10}\), \(z=x^{1/6}\), and \(D\) is the fixed absolute integer in
  the low-\(\omega\) conclusion of Lemma 16.2.

Writing

\[
 E(x;q,a)=\pi(2x;q,a)-\pi(x;q,a)
       -{\operatorname {li}(2x)-\operatorname {li}(x)\over\varphi(q)},
                                                               \tag{34.1}
\]

the assertion is

\[
 \sum_{k\in\mathcal J}
 \sum_{\substack{H<u,v\leq z\\(u,v)=(uv,k)=1\\
                  u+cv\equiv0\ (k)\\
                  \omega(uv)\leq D\log\log X}}
 \left|E(x;4uv,-k^{-1})\right|
 \leq \rho_\kappa(X)x\log x\,h(\mathcal J).                 \tag{34.2}
\]

The inverse and residue in (34.2) are modulo \(4uv\).  They exist because
\(k\equiv1\pmod4\) and \((k,uv)=1\).  The two sums are literal sums over
triples, so repetitions of a modulus or even of a progression retain their
multiplicity.  The little-oh is simultaneous in \(x,K,c,\mathcal J\), not
an average over any of them.  These are exactly the quantifiers needed in
Lemma 18.5.

**Proved implication (Lemma 18.5, restated).**  If (34.2) holds, the lower
proof of Lemma 16.3 may use \(K=X^\kappa\): the box main term in each dyadic
prime interval is \(\asymp x\log x\,h(\mathcal J)\), while (34.2) is
negligible.  Distinctness and the Brun--Titchmarsh upper bound are unchanged.
For the full family,
\(h(\mathcal K(K))\asymp\log K\asymp\log X\), and hence

\[
 \sum_{X^{1/2}<\ell\leq X}{f_c(\ell)\over\ell}
       \asymp(\log X)^3                                     \tag{34.3}
\]

pointwise for every reduced compatible \(c\).  The restriction
\(\kappa<1/240\) comes only from the present floor: at the lowest dyadic
interval, \(z\geq X^{1/12}\) and Lemma 16.2 asks for
\(z>H^2=K^{20}\).

**Current dependency graph (post-Outcome 14).**

1. \(H_{k\rm BV}\) by itself gives (34.3), not an exceptional-set bound.
   The §16 partition has modulus
   \[
    24L_K=\exp((2/3+o(1))K),
   \]
   since
   \(\log L_K=\vartheta(K;4,1)+\vartheta(K/3;4,3)+o(K)
   =(2/3+o(1))K\).  This corrects the larger constant printed in (18.3a):
   requiring \(M_0\leq N^{1-\epsilon}\) permits
   \(K\leq(3/2)(1-\epsilon+o(1))\log N\), rather than the earlier constant.
   The safe upper bound and the conclusion \(K=O(\log N)\) are unchanged.
   Taking \(K=X^\kappa\) at the cubic optimum still makes that modulus far
   larger than \(N\).
2. The original all-range \(H_{\rm PF}\) is refuted by Corollary 31.5.
   Therefore the old arrow
   \(H_{k\rm BV}+H_{\rm PF}(k\ell)\Rightarrow3/4\) has a false assembly
   antecedent as stated.
3. The critical-window hypothesis \(H_{\rm PF}'\) of §31.5 remains open and,
   for the **complete intrinsic all-\(M\) system**, implies
   \(E_{\rm all}(N)\ll N\exp[-c(\log N)^{3/4}]\) without using prime slices
   or \(H_{k\rm BV}\).
4. To turn (34.3) into the same bound by the multiplier-prime route requires
   the different restricted critical-window assembly
   \(H_{\rm PF}'(k\ell;{\rm good})\), stated precisely in §34.4 for the
   complete, \(c\)-dependently pruned harvested system and the lcm budget
   (18.14).  It is not a consequence proved from the complete-system
   \(H_{\rm PF}'\), and is open.

Thus “\(H_{k\rm BV}\) plus \(H_{\rm PF}'\) gives \(3/4\)” is not literally a
current theorem: it is either redundant (complete-system
\(H_{\rm PF}'\) alone) or must use the separately named restricted variant
and its conditional implication in §34.4.

### 34.2 Technology audit: what the nearest theorems actually miss

**Source check: PW §4.**  Pomerance--Weingartner, §4 (the PDF in `sources/`),
uses Bombieri--Vinogradov only after observing that the number of triples
\((m,d,t)\) with a fixed product is \((\log x)^{O(1)}\); this produces their
Lemma 4.1 mass \(\sum f(p)/p\asymp\varphi(m)^{-1}(\log x)^2\).  Their next
step is the larger-sieve Rankin truncation.  This is exactly the pattern of
Lemma 16.3.  It validates the polylogarithmic-multiplicity mechanism, not a
power-sized extra parameter.

The remaining literature statements in this audit are **cited from memory**:
there is no BFI/Fouvry--Iwaniec/Zhang PDF in `sources/`.

**Assessment 34.1 (Bombieri--Friedlander--Iwaniec).**  The classical BFI
Theorem 10 permits \(q\leq x^{4/7-\epsilon}\) for a fixed integer residue
\(a\), after a **signed scalar** modulus weight \(\lambda_q\) is assumed
well-factorable: for every split of its level, \(\lambda\) must be a
convolution of two bounded sequences on the corresponding ranges.  This is
not a black box for (34.2), for three independent reasons.

* Our moduli already satisfy \(q=4uv\leq4x^{1/3}\), safely inside ordinary
  Bombieri--Vinogradov; extra level past \(1/2\) is not the resource missing.
* Even for a fixed \(k\), the residue \(-k^{-1}\pmod q\) moves with \(q\);
  across \(k\) there are many such residues at one \(q\).  BFI fixes one
  integer \(a\) for the entire modulus sum.
* Dualizing the absolute values in (34.2) creates arbitrary signs
  \(\epsilon_{k,u,v}\).  They are indexed by both modulus and residue, and
  the incidence \(k\mid u+cv\) couples \(k\) to both factors of \(q=4uv\).
  This is not even a scalar \(\lambda_q\) to which well-factorability can be
  applied.  No factorization of these arbitrary dual coefficients is known.

The factorization \(q=4uv\) therefore resembles BFI's raw bilinear geometry,
but the weight in \(H_{k\rm BV}\) is **not covered** by the theorem's
well-factorable-weight hypothesis.

**Assessment 34.2 (Fouvry--Iwaniec and incomplete Kloosterman sums).**  The
early Fouvry--Iwaniec dispersion method and its BFI descendants convert
structured bilinear prime sums, after Cauchy and reciprocity, into incomplete
Kloosterman sums.  That is the right local analytic species: additive
completion of the moving inverse in (34.2) produces
\(e(h\bar k/(4uv))\).  What their published fixed-residue formulations do
not supply is an \(\ell^1\) estimate after independent signs are attached to
every \((k,u,v)\), with \(k\) additionally selected by
\(k\mid u+cv\).  The missing prerequisite is not “a Kloosterman sum exists”;
it is a long or factorable average left after dualization.  Here that average
is both short and divisor-conditioned (quantified in §34.3(c)).

**Assessment 34.3 (Zhang-style smooth moduli).**  Zhang/Polymath-type
estimates gain distribution for squarefree moduli all of whose prime factors
are small, using flexible dense divisibility (some later variants improve
residue uniformity on similarly restricted coefficient classes).  The
condition \(\omega(uv)\leq D\log\log X\) says that \(uv\) has few distinct
prime factors; it does **not** say those factors are small.  A single prime
factor may be of size \(x^{1/6}\), and prime powers are allowed.  Thus
\(4uv\) is not a Zhang-smooth family.  More basically, smooth-modulus
uniformity can choose one worst residue per modulus, as ordinary BV already
does here; it does not pay for up to \(K\) separately absolute residues at
the same modulus.

**Assessment 34.4 (dispersion as a program).**  Linnik dispersion is the
only audited technology that exposes the moving inverse rather than
maximizing it away.  A viable application would have to preserve structure
in the dual signs, average the divisor incidence \(k\mid u+cv\), and handle
composite \(4uv\) through prime-power Kloosterman bounds and CRT.  None of
the quoted theorems has those three features simultaneously.  Section
34.3(c) shows that the most direct completion is quantitatively backwards;
the successful partial theorem instead removes the rare incidence
congestion before applying ordinary BV.

### 34.3 What can be proved

#### (a) Plain BV and Cauchy--Schwarz baselines

Let \(S\) denote the left side of (34.2).  Grouping only by the modulus and
using the cutoff on \(\omega(uv)\) gives the §16 bound

\[
 W(q)\leq K2^{\omega(q/4)}
       \leq K(\log X)^{D\log2}.                              \tag{34.4}
\]

Bombieri--Vinogradov with an arbitrary fixed saving \(R\) consequently gives

\[
 S\ll_R {Kx\over(\log x)^{R-D\log2}}.                        \tag{34.5}
\]

Splitting into individual \(k\)'s gives the same factor \(K\), not a better
bound.  Since \(R\) must be fixed before \(X\to\infty\), (34.5) absorbs
\(K\leq(\log X)^A\) for every fixed \(A\), but no function larger than all
fixed log powers.

For the honest second-moment baseline, the number of triples in one box is

\[
 T\ll x^{1/3}h(\mathcal J)(\log x)^{O(1)},\qquad
 \sum_{q,a}m(q,a)^2\leq W_{\max}T.                           \tag{34.6}
\]

The unconditional small-level large-sieve/BDH upper bound available at
\(Q_0=x^{1/3}\) is \(x^2(\log x)^{O(1)}\), rather than the conjectural
\(xQ_0(\log x)^{O(1)}\).  Cauchy--Schwarz therefore yields

\[
 S\ll x^{7/6}\{K h(\mathcal J)\}^{1/2}(\log x)^{O(1)}.       \tag{34.7}
\]

Against the main term \(x\log x\,h(\mathcal J)\), the polynomial loss is
\(x^{1/6}\{K/h(\mathcal J)\}^{1/2}\), up to log powers.  Thus it already
loses at \(K=1\).  A conjectural \(xQ_0\) variance would give
\(x^{5/6}\{Kh\}^{1/2}\), which is why the missing small-level variance
would permit a small power of \(x\); standard BDH does not state that bound
in this range.

#### (b) The exact polylogarithmic theorem and the prize function

**Lemma 34.5 (all fixed log powers; proved).**  For every fixed \(A>0\), the
conclusion of Lemma 16.3 holds uniformly for
\(K\leq(\log X)^A\) (with the harmless constants and BV saving allowed to
depend on \(A\)).

*Proof.*  The proof of Lemma 16.2 takes its parameter \(B>A\), and (34.5)
with \(R>A+D\log2+10\) makes the progression error negligible.  Every
other line of Lemma 16.3 is unchanged. ∎

This is the exact content of “apply BV separately for each multiplier.”  The
exponent 5 in Lemma 16.3 is inessential.  Increasing it to 500 does **not**
improve a logarithmic exponent in Theorem 16.4: if

\[
 L=\log N,\quad t=\log X,\quad r=\log K,
 \quad \mu\asymp t^2r,                                      \tag{34.8}
\]

then every fixed-polylog range has \(r\asymp\log t\), and the Rankin budget
\(t\mu\lesssim L\) gives

\[
 \mu\asymp L^{2/3}(\log L)^{1/3}.                           \tag{34.9}
\]

The §16 choice \(K\asymp L\) already attains \(r\asymp\log L\) while
remaining a fixed power of \(t\) at the optimum.  Larger fixed powers alter
constants only.

For reference, under the partition-free
\(H_{\rm PF}'(k\ell;{\rm good})\)-type assembly stated in §34.4,
the general budget while \(r\leq t\) is

\[
 t^3r\lesssim L,\qquad \mu\asymp t^2r=L/t.                  \tag{34.10}
\]

It gives the following exact incremental prizes (all conditional on that
assembly, not consequences of a prime-slice estimate alone):

* \(K=\exp((\log L)^2)\), so \(r=(\log L)^2\), gives
  \(\mu\asymp L^{2/3}(\log L)^{2/3}\).  This range is already larger than
  the §16 partition permits, since \(K\gg L\).
* If \(K=\exp(t^\beta)\), \(0<\beta<1\), then
  \(\mu\asymp L^{(2+\beta)/(3+\beta)}\).
* If \(K=X^{1/\psi(t)}\) with \(\psi(t)\to\infty\), the implicit balance is
  \(t^4/\psi(t)\asymp L\) and
  \(\mu\asymp L^{3/4}\psi(t)^{-1/4}\).  The phrase \(K=X^{o(1)}\) alone
  therefore has no single exponent; it can approach \(3/4\) with an
  arbitrary slowly varying loss.
* A fixed power \(K=X^\kappa\) has \(r=\kappa t\), budget \(t^4\lesssim L\),
  and \(\mu\asymp L^{3/4}\).

#### (c) Completion, its failure, and a low-congestion extension

**Standard completion input (cited from memory).**  For an interval \(I\)
and an integer \(h\), additive completion plus the prime-power
Weil--Estermann bound and CRT gives

\[
 \left|\sum_{k\in I,(k,q)=1}e(h\bar k/q)\right|
 \ll \tau(q)(h,q)^{1/2}q^{1/2}\log(2q).                     \tag{34.11}
\]

For composite \(q\), the complete sums are multiplicative only after the
usual CRT twists; prime powers dividing both the frequency and \(q\) produce
the factor \((h,q)^{1/2}\).  The factor 4 in \(q=4uv\) must therefore not be
treated as an unramified prime modulus.  There is in fact no literal “prime
\(4uv\)” case.

**Assessment 34.6 (direct Weil completion loses).**  Even in the easier
model with a full interval of \(k\)'s, no divisor condition, and coherent
signs, (34.11) competes with the trivial bound \(K\).  In the actual family

\[
 q=4uv>4H^2=4K^{20},\qquad {q^{1/2}\over K}>2K^9.            \tag{34.12}
\]

Thus completion is at least nine powers of \(K\) worse before its divisor
and logarithmic factors.  The condition \(k\mid u+cv\) replaces the interval
by an irregular divisor set, and dualizing (34.2) permits arbitrary signs on
that set; both changes only remove structure.  Lowering the floor within the
box proof does not fix the comparison: its boundary error needs roughly
\(H\gg K^2\), still forcing \(q^{1/2}\gg K^2\).  The elementary
completion-plus-Weil route gives no range gain over (34.5).

The failed completion points to a different use of \(k\mid u+cv\).  Define
the incidence

\[
 r_{\mathcal J}(u,v;c)
   =\#\{k\in\mathcal J:k\mid u+cv\}.                         \tag{34.13}
\]

When \((u,v)=1\) and \((c,L_{\mathcal J})=1\), the coprimality
\((uv,k)=1\) follows automatically for every counted \(k\).

**Lemma 34.7 (second incidence moment; proved).**  Let \(K\geq K_0\),
\(H=K^{10}\), \(z>H^2\), and let \(c,\mathcal J\) have the preceding
properties.  Then

\[
 \sum_{\substack{H<u,v\leq z\\(u,v)=1}}
 {r_{\mathcal J}(u,v;c)^2\over uv}
 \ll (\log z)^2(1+\log K)^3.                                \tag{34.14}
\]

The constant is absolute and the estimate is uniform in \(c\) and
\(\mathcal J\).

*Proof.*  Expand the square.  For \(k,k'\in\mathcal J\), both divisibilities
are the single congruence
\(d=[k,k']\mid u+cv\), and \((c,d)=1\).  The box calculation (16.4), now
with modulus \(d\leq K^2\), gives

\[
 \sum_{\substack{H<u,v\leq z\\(u,v)=1\\d\mid u+cv}}{1\over uv}
 \ll {\varphi(d)\over d^2}(\log z)^2
      +{\tau(d)(\log z)^2\over H}.                           \tag{34.15}
\]

Indeed, over the geometric endpoints
\[
 \sum_U U^{-1}=O(1/H),\qquad \#\{V\text{-boxes}\}=O(\log(z/H)),
\]
and the symmetric term is identical.  Thus the full boundary sum is
\(O(\tau(d)\log z\log(z/H)/H)\), which is bounded by the error in
(34.15).  For the main coefficients,

\[
 \sum_{k,k'\leq K}{\varphi([k,k'])\over[k,k']^2}
 \leq\sum_{k,k'\leq K}{(k,k')\over kk'}
 \ll(1+\log K)^3,                                           \tag{34.16}
\]

where writing \(k=da,k'=db,(a,b)=1\) reduces the last sum to
\(\sum_{d\leq K}d^{-1}(1+\log(K/d))^2\).  Finally
\(\tau([k,k'])\leq2K\), so the total boundary contribution is
\(O(K^3(\log z)^2/H)=O(K^{-7}(\log z)^2)\).  Summing (34.15) proves
(34.14). ∎

**Theorem 34.8 (unconditional pruned cubic prime slice; proved).**  Fix
\(0<\kappa<1/240\).  In the setup of \(H_{k\rm BV}(\kappa)\), impose on the
triples the additional low-congestion condition

\[
 r_{\mathcal J}(u,v;c)\leq T_X:=(\log X)^4.                 \tag{34.17}
\]

Then the sum in (34.2), restricted by (34.17), is
\(o(x\log x\,h(\mathcal J))\) **unconditionally**, uniformly in all the
quantified data.  Moreover, if \(f_c^{\rm good}(\ell)\) counts only the
distinct Lemma-16.3 classes from these low-congestion triples, then

\[
 \sum_{X^{1/2}<\ell\leq X}{f_c^{\rm good}(\ell)\over\ell}
       \asymp(\log X)^2h(\mathcal J).                        \tag{34.18}
\]

In particular, for \(K=X^\kappa\) and the full family,

\[
 \sum_{X^{1/2}<\ell\leq X}{f_c^{\rm good}(\ell)\over\ell}
       \asymp(\log X)^3                                     \tag{34.19}
\]

pointwise in every reduced compatible \(c\), without \(H_{k\rm BV}\).

*Proof.*  First note that the proof of Lemma 16.2 does not intrinsically need
\(K\) to be polylogarithmic.  Its box error is \(O(K^2/H)\) relative to the
main term.  Shiu is used on fixed-relative-length intervals with
\[
 k\leq K<U^{1/10},V^{1/10}
\]
because \(U,V>H=K^{10}\).  **(wave-15 repair)**  In the notation of
Shiu's actual Theorem 1, take the interval endpoint and length to be
\(x_0=(1+\eta)U\) and \(y_0=\eta U\), and fix, for example,
\(\alpha=\beta=1/4\).  Its source hypotheses
\(k<y_0^{1-\alpha}\) and \(x_0^\beta<y_0\) then follow (with room to spare)
from \(k<U^{1/10}\); the residue is reduced because
\((cv,k)=1\).  The fixed functions \(t^{\omega(n)}\) and
\(n/\varphi(n)\) satisfy its prime-power and subpower growth hypotheses,
and the local-factor bound (16.5e) is uniform in \(k\).  The low-\(\omega\)
Rankin estimate is therefore uniform as well.  Thus the same proof applies whenever \(z>K^{20}\), with
\(\log(z/H)\asymp\log z\).  At the lowest prime interval this holds
uniformly because \(\kappa<1/240\).

The low-\(\omega\) first moment from that extended box argument is
\(\gg(\log z)^2h(\mathcal J)\).  By Lemma 34.7, the first-moment mass of
triples failing (34.17) is at most

\[
 {1\over T_X}
 \sum_{u,v}{r_{\mathcal J}(u,v;c)^2\over uv}
 \ll { (\log z)^2(1+\log K)^3\over(\log X)^4}
 =o((\log z)^2h(\mathcal J)),                               \tag{34.20}
\]

uniformly, since \(h(\mathcal J)\geq1\) (the required member
\(1\in\mathcal J\) contributes exactly 1) and \(\log K\ll\log X\).  Hence
the retained triples have the full order of main mass.  **(wave-15 repair)**
This also identifies where the hypothesis \(1\in\mathcal J\) is needed for
uniformity over sparse subfamilies.

For fixed \(q=4uv\), coprimality permits at most
\(2^{\omega(uv)}\) ordered allocations of its prime powers to \((u,v)\).
For each allocation, (34.17) permits at most \(T_X\) choices of \(k\).
Consequently the retained multiplicity is

\[
 W_{\rm good}(q)\leq
 2^{\omega(uv)}T_X\leq(\log X)^{D\log2+4}.                  \tag{34.21}
\]

Ordinary Bombieri--Vinogradov, with a fixed saving larger than the exponent
in (34.21), now makes the restricted error sum negligible.  **(wave-15
repair)**  Indeed \(4uv\leq4z^2=4x^{1/3}\), hence lies below
\(x^{1/2}/(\log x)^A\) for every fixed \(A\), and grouping by the modulus
bounds the whole triple error sum by (34.21) times the usual BV maximum over
reduced residue classes.  Equations (34.20), Lemma 16.2, and
\(1/\varphi(4uv)\geq1/(4uv)\) give the lower main term in every dyadic
interval.  This lower argument uses the canonical boxes
\(u,v\leq z=x^{1/6}\).  If the same prime \(\ell\in(x,2x]\) occurs for two
triples, then \(|uv'-u'v|<z^2<\ell\); Lemma 16.3's determinant argument and
then \(uv>H^2>K\) prove that their classes are distinct.  Thus repeated
occurrences of \(\ell\) are legitimate distinct contributions, not a lower-
bound overcount.  Brun--Titchmarsh and the extended form of (16.3) give the
upper bound.  Summing the dyadic intervals proves (34.18), and
\(h(\mathcal K(X^\kappa))\asymp\log X\) gives (34.19). ∎

Theorem 34.8 does **not** prove literal \(H_{k\rm BV}\): (34.2) still asks
for the absolute errors of the discarded high-incidence triples.  It proves
that they carry \(o(1)\) of the weighted box/main-term mass, while the
retained **actual** prime-class mass has full cubic order.  It does not assert
that \(f_c^{\rm good}/f_c\to1\).  This is enough for Lemma 18.5's conclusion
and is strictly stronger for that application than an estimate for a sparse
set of isolated large multipliers.

### 34.4 Restricted assembly and the changed bottleneck

For completeness, the assembly statement used in the multiplier-prime route
is now made explicit.  Fix \(0<\kappa<1/240\), put \(t=\log X\),
\(K=\lfloor X^\kappa\rfloor\), \(\mathcal J=\mathcal K(K)\), and
\(M_0=24L_K\).  For each reduced \(c\pmod {M_0}\), let
\(\mathscr G_{X,c}\) be the **fixed complete family** of distinct forced
classes
\[
 n\equiv-u v^{-1}\pmod {k\ell}                              \tag{34.22}
\]
from every triple counted in Theorem 34.8: thus (16.7) holds,
\(r_{\mathcal J}(u,v;c)\leq(\log X)^4\), and no further class is omitted.
The pruning depends on the full residue \(c\), but after \(c\) is fixed the
family does not depend on \(n\).  Its conditional (prime-coordinate) mass is
\[
 \mu_{X,c}:=\sum_{X^{1/2}<\ell\leq X}{f_c^{\rm good}(\ell)\over\ell}
 \asymp t^3                                                       \tag{34.23}
\]
uniformly in every reduced \(c\), by Theorem 34.8.  This is conditional mass
inside the \(c\)-fiber, not the sum of the global densities \(1/(k\ell)\).

**Hypothesis \(H_{\rm PF}'(k\ell;{\rm good})\) (restricted, partition-free
critical-window assembly; OPEN).**  There are constants \(c_0,C>0\) and
\(0<c_-<c_+\), depending at most on \(\kappa\), with \(c_-\) large enough
for the degree budget, such that the following holds uniformly for all large
\(X\).  Whenever
\[
 c_-t^4\leq\log N\leq c_+t^4,
 \qquad J\geq C\sup_c\mu_{X,c},
 \qquad J(t+\log K)\leq\tfrac12\log N,
\]
the aggregate avoider predicate
\[
 {\bf1}_{(n,M_0)=1}
 {\bf1}_{\{n\text{ avoids every class in }
                 \mathscr G_{X,n\bmod M_0}\}}
\]
has a nonnegative majorant \(\nu_{X,N}\) on \([1,N]\), pointwise at least
the displayed predicate, with
\[
 {1\over N}\sum_{n\leq N}\nu_{X,N}(n)
 \ll \exp\{-c_0\inf_c\mu_{X,c}\}.                          \tag{34.24}
\]
The majorant is required to have a partition-free degree-\(J\) congruence
expansion, uniform simultaneously over the fixed families
\(\mathscr G_{X,c}\), whose **total** absolute coefficient sum (including
all \(c\)-dependence) is \(e^{O(J)}\).  Every term uses at most \(J\) class
moduli and is evaluated only by exact intersection counts modulo
\[
 d=\operatorname {lcm}(k_i\ell_i:i\leq J)
   \leq K^JX^J\leq N^{1/2}.
\]
Thus each finite-window count is its CRT main term plus \(O(1)\), and the
total rounding error is \(e^{O(J)}=o(N e^{-c_0\inf_c\mu_{X,c}})\).
Crucially, no hidden expansion into the \(M_0\) residue classes, and no
\(M_0\)-fold coefficient or rounding loss, is allowed.  This last requirement
is the unproved partition-free handling of the \(c\)-dependent pruning; the
hypothesis is not asserted to follow from complete-system \(H_{\rm PF}'\).

The exact restricted implication is
\[
 \boxed{\quad
  \text{Theorem 34.8}+H_{\rm PF}'(k\ell;{\rm good})
  \ \Longrightarrow\
  E_{\rm all}(N)\ll N\exp\{-c(\log N)^{3/4}\}.
 \quad}                                                       \tag{34.25}
\]
Indeed choose \(t=\alpha(\log N)^{1/4}\), with the fixed \(\alpha\) inside
the asserted critical window and small enough for the degree inequality, and
take \(J=C\sup_c\mu_{X,c}\).  Every exceptional prime \(n>K\) is coprime
to \(M_0\) and avoids \(\mathscr G_{X,n\bmod M_0}\), because every member
of that family is a Lemma-16.1 forced class.  Equations (34.23)--(34.24)
therefore give the claimed bound for exceptional primes with exponent
\(t^3\asymp(\log N)^{3/4}\); the semigroup argument of Theorem 16.5 gives
the displayed all-denominator bound.  This proves only the conditional
implication, not its open assembly antecedent.

**Provisional proved verdict.**  The unconditional prime-slice record is now
(34.19): the complete cubic order is realized after an explicit pruning
which removes \(o(1)\) of the weighted box/main-term mass and retains
cubic-order actual class mass.  The old bound \(K\leq(\log X)^A\) was a wall
of the crude maximum multiplicity (34.4), not of the class supply and not of
ordinary BV once the divisor incidence is used.  Literal \(H_{k\rm BV}\)
remains open, but it is no longer needed to realize cubic prime-slice mass.

**Exceptional-set consequence now.**  There is no unconditional improvement
to Theorem 16.4 from this theorem alone.  The existing §16 partition still
forces \(K\ll\log N\), and optimizing with \(r\leq\log\log N\) returns
\(E(N)\ll N\exp[-cL^{2/3}(\log L)^{1/3}]\).  The restricted
critical-window assembly \(H_{\rm PF}'(k\ell;{\rm good})\) combines with
Theorem 34.8 exactly as stated in (34.25); its assembly antecedent is open.
The complete-system \(H_{\rm PF}'\) would give the same bound independently.  Given Outcome 14,
paying for full \(H_{k\rm BV}\) now has little marginal value for the
\(3/4\) campaign: assembly, not prime-slice harvesting, is the exact live
bottleneck.

**Wave-13 supersession note (appended; CLAIMED/PROVISIONAL).**  Section 39
does not prove (34.24): it majorizes the smaller fixed c-free avoider which
still contains every exceptional prime, and its coefficient ledger is
\(e^{O(Jt)}\), not \(e^{O(J)}\).  Theorem 39.6 proves that this larger ledger
is absorbed by \(\log N\asymp t^4\), yielding the provisional unconditional
implication in Theorem 39.7.  The original hypothesis remains OPEN.

**Soft spots.**  Theorem 34.8 is new to this campaign and needs external
priority and referee checking, especially the power-range extension of the
Shiu/box estimates and the uniform second-moment boundary sum.  The
technology audit's BFI/Fouvry--Iwaniec/Zhang statements are from memory
because those PDFs are absent from `sources/`.  No claim is made that
\(H_{\rm PF}'(k\ell;{\rm good})\) follows from the currently stated
complete-system \(H_{\rm PF}'\).

**Numerical companion.**  `verify.py (ag)` checks the exact incidence-square
expansion behind Lemma 34.7, the congestion inequality and (34.21) on a toy
box, evaluates the actual progression errors there, and prints both the
realized Cauchy--Schwarz loss and the scale proxy from (34.7).  It also checks
small composite-modulus Kloosterman sums against the CRT/Weil envelope.  The
block is finite evidence only and runs in under ten seconds.

### 34.5 Wave-15 independent re-derivation (attestation)

This is a third internal check, not external expert review.
The reviewer independently re-derived the power-sized extension of Lemma 16.2,
including its box-boundary ratio and low-\(\omega\) Rankin tail.
The reviewer independently proved the Lemma 34.7 second incidence moment by
expanding \(r_{\mathcal J}^2\), summing the lcm densities, and paying all box
errors.
Shiu's 1980 PDF was checked directly: both interval/modulus inequalities,
the reduced-residue condition, and the two multiplicative-function hypotheses
hold in the fixed-relative-length boxes with \(H=K^{10}\).
The pruning estimate, its uniform use of \(1\in\mathcal J\), the
fixed-log-power BV multiplicity, and same-prime class distinctness were all
re-derived.
The final dyadic lower and upper assemblies for (34.18)--(34.19) were checked.
The printed §34 proof was then compared line by line; only the explicit source
hypotheses and compressed bookkeeping were repaired above.
The §39 use with the data-dependent \(\mathcal J_c\), canonical boxes, and the
lower bound for \(h(\mathcal J_c)\) was also audited separately.
Verdict: **CONFIRMED-AFTER-REPAIRS** as an internal provisional result.
The campaign's CLAIMED/PROVISIONAL register is unchanged.

## 35. Unit W: an independent-method blind pointwise attack

Sections 35.1--35.3 were developed under the blind protocol logged below;
the comparison with the rest of the campaign is deferred to §35.4.  All
coverage statements below concern the only open prime class
\(p\equiv1\pmod {24}\), unless stated otherwise.

**Blind-phase protocol log (history-bounded and self-reported).**  The source
snapshot was commit `9fef195` (2026-08-25 01:30 +0200).  The designed phase-1
allowlist was only `notes.md` §3 and §17.1.  The rest of `notes.md`,
`PROJECT.md`, `sources/`, existing campaign programs/results, and repository
text search were out of bounds; fresh scratch SymPy computations of formulas
derived in phase 1 were allowed.  The phase-1 findings were frozen in
`unit_w_blind.md` at commit `1f58c57` (01:42), then moved without
reconciliation into §35 at `6f92450` (01:44).  The self-reported point at
which the earlier waves were opened is after that commit and before the
reconciliation commit `b1d6bb5` (01:51).  Git history verifies the snapshot,
texts, commit order, and timestamps; it cannot verify what was visible on
screen or enforce the code/search isolation.  Those process and phase-timing
claims remain an explicit self-attestation, not independently audited
blindness.

### 35.1 Bounded multiplicative residues: an exact q = 3 family

**Theorem 35.1 (bounded-residue criterion and the exact q = 3 slice).**  Let
\(q\) be a positive integer, put
\(x=(p+q)/4=\prod_r r^{\alpha_r}\), where \(q\equiv-p\pmod4\), and
assume \(\gcd(x,q)=1\) (as holds when \(q<p\)).  Criterion 3.1(B) at this
fixed \(q\) is equivalent to

\[
 \prod_r r^{t_r}\equiv-1\pmod q,
 \qquad -\alpha_r\leq t_r\leq\alpha_r.                 \tag{35.1}
\]

Negative exponents in (35.1) mean inverses of the units \(r\pmod q\).
In particular:

1. if a prime factor \(r\mid x\) satisfies \(r\equiv-1\pmod q\), then this
   \(q\) solves \(p\);
2. for \(p\equiv1\pmod {24}\), \(q=3\) solves \(p\) **if and only if**
   \((p+3)/4\) has a prime factor congruent to 2 modulo 3;
3. fix any prime \(r\equiv5\pmod6\).  Every prime in the progression

\[
             p\equiv20r-3\pmod {24r}                  \tag{35.2}
\]

is solved at \(q=3\).  Each progression (35.2) contains infinitely many
primes.

*Proof.*  A divisor \(d=\prod r^{\beta_r}\) of \(x^2\) has
\(0\leq\beta_r\leq2\alpha_r\).  Dividing the congruence
\(d\equiv-x\pmod q\) by the unit \(x\) and putting
\(t_r=\beta_r-\alpha_r\) proves (35.1) in both directions.  For (1), take
\(d=xr\), which divides \(x^2\).  For (2), write \(p=24n+1\), so
\(x=6n+1\equiv1\pmod3\).  A factor \(r\equiv2\pmod3\) is itself a valid
choice of \(d\).  Conversely, if no such factor exists, every divisor of
\(x^2\) is 1 modulo 3 and cannot be \(-x\equiv2\pmod3\).  In (3), write
\(p=20r-3+24rt\).  Then \(p\equiv1\pmod {24}\) and
\(x=r(6t+5)\), so (2) applies.  Also
\(\gcd(20r-3,24r)=1\); Dirichlet's theorem gives infinitely many primes in
(35.2). ∎

**Computational 35.1.**  Exact SymPy enumeration found 9,732 primes
\(p<10^6\) in the hard class.  The q = 3 criterion covers 5,192 (53.35%).
Testing every \(q\in\{3,7,\ldots,63\}\) and every divisor of \(x^2\) covers
all 9,732.  This extends the §3 q-window check by one decade, but does not
prove that 63 remains enough.

**Assessment 35.1 (failure log).**  The exact condition is useful but not
pointwise: 4,540 tested primes fail q = 3, beginning with \(p=73\).  The
forced congruence \(x\equiv1\pmod3\) does not force any prime divisor of
\(x\) to be 2 modulo 3.  Dropping the exponent bounds in (35.1) only gives
subgroup membership in \((\mathbb Z/q\mathbb Z)^*\), a strictly weaker
local condition; it cannot manufacture the required divisor of \(x^2\).

### 35.2 Shifted factors and the split conic

**Theorem 35.2 (the a = 1 Type-II shifted-factor sieve).**  A Type-II tuple
with \(a=1\) exists if and only if there are \(c\geq1\) and a positive
integer \(D\) such that

\[
             D\mid p+4c,\qquad D\equiv-1\pmod {4c}.     \tag{35.3}
\]

Given (35.3), put

\[
 k={D+1\over4c},\qquad t={p+4c\over D},\qquad b=kt-1.  \tag{35.4}
\]

Then \(t=(b+1)/k\) and \(kp=4bck-b-1\).  It is enough to search
\(c\leq(p+2)/4\).  In particular, a prime factor congruent to 3 modulo 4
of \(p+4\) settles \(p\), and fixed \((c,k)\) settles every prime in the
compatible progression

\[
             p\equiv-4c\pmod {4ck-1}.                  \tag{35.5}
\]

*Proof.*  From an \(a=1\) tuple,
\(b+1=k(4bc-p)=kt\), and direct expansion gives
\(p+4c=t(4ck-1)\), proving necessity with \(D=4ck-1\).  Conversely,
(35.4) gives
\(p=t(4ck-1)-4c=4c(kt-1)-t=4bc-t\), which is the Type-II equation after
multiplication by \(k\).  The impossible case \(b=0\) would force
\(k=t=1\) and \(p=-1\).  Finally,
\(t=(b+1)/k\leq b+1\), so
\(p=4bc-t\geq b(4c-1)-1\geq4c-2\).  The two sufficient conditions are
(35.3) with \(c=1\), and (35.3) with \(D=4ck-1\), respectively. ∎

**Computational 35.2.**  Among the 9,732 hard primes below \(10^6\), the
bounds \(c\leq1,2,4,8,16,32,64,128\) cover respectively

\[
 4850,7824,8962,9525,9680,9719,9726,9727
\]

primes.  A complete scan through the proved bound \((p+2)/4\) leaves
exactly

\[
                    193,\quad2521,\quad66529.           \tag{35.6}
\]

Thus the tempting a = 1 strengthening is false even very low down.  The
three primes are solved by the non-a = 1 tuples

\[
 (a,b,c,k)=(2,5,5,1),\ (2,159,2,7),\ (5,832,4,27),
\]

respectively.

**Theorem 35.3 (the diagonal and the Pell degeneration).**  In any Type-II
tuple let \(h=(a+b)/k\) and \(r=b-a\).  Then

\[
 a={hk-r\over2},\quad b={hk+r\over2},\quad
 p=c(h^2k^2-r^2)-h,                                    \tag{35.7}
\]

and

\[
             (hk-r)(hk+r)={p+h\over c}.                 \tag{35.8}
\]

No hard prime has a diagonal tuple \(a=b\).

*Proof.*  Substitute \(a+b=hk\) and \(b-a=r\) into Theorem 17.1.  If
\(r=0\), (35.7) becomes \(p=h(chk^2-1)\).  For a hard prime,
\(h\equiv3\pmod4\), hence \(h\geq3\), while
\(chk^2-1\geq3\cdot1\cdot1-1=2\).  Thus this is a product of two integers
larger than one. ∎

**Computational 35.3a.**  For all 1,181 hard primes below \(10^5\), all
witnesses with \(q=h\leq63\) were reconstructed canonically and the least
\(|a-b|\) in that window was recorded.  It reaches 535 at \(p=87049\), via
\((h,a,b,c,k)=(47,38,573,1,13)\).  This statement is only about the
\(h\leq63\) window; a larger h could give a smaller offset.

**Assessment 35.2 (failure log).**  The a = 1 shifted-factor sieve reaches
99.97% below \(10^6\) and still fails pointwise at (35.6).  The geometric
route also has an exact death point: with \(p,h,c\) fixed, the apparent Pell
equation has square coefficient \(h^2\) and splits as (35.8).  There is no
Pell orbit to exploit; continued fractions or near-diagonal lattice search
returns to a finite factorization.  Precisely, a factor pair
\(UV=(p+h)/c\) reconstructs positive integral \(a,b,k\) if and only if
\(U,V\) are positive and even and \(2h\mid U+V\); then
\(a=U/2\), \(b=V/2\), \(k=(U+V)/(2h)\), and
\(r=(V-U)/2\).  The diagonal is not merely sparse but impossible, and the
bounded-offset data supply no uniform bound.

### 35.3 A Type-I divisor-cover sieve

**Theorem 35.4 (the a = 1 Type-I sieve).**  A Type-I tuple with \(a=1\)
exists if and only if there are \(c\geq1\) and a positive divisor
\(D\mid4c+1\) such that

\[
                         p\equiv-D\pmod {4c}.            \tag{35.9}
\]

The reconstruction is

\[
 k={p+D\over4c},\qquad E={4c+1\over D},\qquad
 b={pE+1\over4c}={p+k\over D}.                           \tag{35.10}
\]

For \(p\equiv1\pmod4\), necessarily \(D\equiv3\pmod4\), and it is enough
to search

\[
                         c\leq{3p+1\over8}.              \tag{35.11}
\]

For example, \(c=5\), \(4c+1=21\), and \(D=3,7\) prove unconditionally
that every prime \(p\equiv97,73\pmod {120}\), respectively, has a Type-I
solution with \(a=1\).

*Proof.*  From \(p(1+b)=k(4bc-1)\), set \(D=4ck-p\); then
\(bD=p+k\), so \(D>0\).  Theorem 17.1 gives \(p\nmid ck\), hence
\(\gcd(D,p)=1\).  Since

\[
 4c(p+k)=p(4c+1)+D,
\]

we obtain \(D\mid4c+1\), and the definition of \(D\) gives (35.9).
Conversely, (35.9) makes (35.10) integral; indeed
\(pE+1\equiv-DE+1=-4c\pmod {4c}\).  Also \(bD=p+k\), so reversing the
calculation proves the Type-I equation.  If \(p\equiv1\pmod4\), (35.9)
forces \(D\equiv3\pmod4\).  Its cofactor \(E\) is also 3 modulo 4 and at
least 3, so \(D\leq(4c+1)/3\).  Combining this with
\(p+D=4ck\geq4c\) proves (35.11).  The stated progressions are the Chinese
remainder intersections of \(p\equiv1\pmod {24}\) with
\(p\equiv-3,-7\pmod {20}\). ∎

**Computational 35.3b.**  Exact enumeration of all 82,887 hard primes below
\(10^7\) found an a = 1 Type-I witness for every one.  Divisors of
\(4c+1\) were tested in increasing c through (35.11) until a witness was
found and every resulting tuple was checked in the defining equation.  The
largest first-witness c in this range is 107,588, for \(p=8,604,961\), with
\(D=2,079\).

**Heuristic 35.3.**  For fixed c, Theorem 35.4 covers one residue class
modulo \(4c\) for each 3-mod-4 divisor of \(4c+1\).  Summing these thin,
partly dependent divisor-cover events suggests increasing aggregate
coverage and is consistent with the computation.  It does not justify
probability one for each individual p, let alone no exceptions.

**Assessment 35.3 (failure log).**  Theorem 35.4 is the strongest blind
reduction found here, but it is not a proof of pointwise existence.  It asks
for an exact divisor of a moving integer \(4c+1\), aligned with p by
(35.9).  Congruence and p-adic solutions are plentiful but do not force
that positive integral divisor.  Any finite set of c supplies only a finite
union of arithmetic progressions.  The observed \(10^7\) coverage is
therefore computational evidence for a stronger a = 1 Type-I conjecture,
not a theorem about all primes.

### 35.4 Reconciliation after opening the earlier waves

**Reconciliation 35.4 (method-by-method).**

1. **Bounded residues.**  The q = 3 equivalence in Theorem 35.1 is already
   stated in §6, including the even-nonresidue mechanism; (35.1) is its
   direct exponent-box restatement.  The progressions (35.2) are instances
   of the fixed \((q,d,R)\) Case-B families of §4 (take
   \(q=3,d=R=r\)), hence fall under the finite-family obstruction of §5 and
   the inventory in §17.3(a).  The larger \(10^6\) q-window computation is
   new data, not a new method.

2. **Shifted factors and the conic.**  Theorem 35.2 is exactly the a = 1
   specialization of the Euclidean divisor reduction (20.11)--(20.12); its
   c = 1 line is explicitly identified in §§8.3 and 20.2.  Its fixed
   progressions (35.5) are the b-translation grids of §20.4.  Section
   17.3(e) instead fixes \((a,b,k)\) and translates c, a different coordinate
   direction.  The prior campaign also already explains why continued
   fractions cannot turn near divisibility into equality (§20.2), why the
   factor norm is split rather
   than a class-group norm (§20.1), and why there is no Vieta move (§30.3).
   The coordinates (35.7)--(35.8), the proof that the exact diagonal is
   impossible for hard primes, the bounded-offset statistic, and the exact
   three-prime failure list (35.6) were not present.  They sharpen the
   failure log but do not escape the divisor wall.  This split degeneration
   is distinct from §9.3's nonsplit quadratic-form Pell obstruction.

3. **Type I.**  The ambient divisor form and complete finite Type-I search
   were already developed in §26.1.  Theorem 35.4 is a new-to-this-document
   a = 1 specialization and reorganization, not a new source of identities:
   writing \(E=(4c+1)/D\), it is exactly the §4 fixed Case-A family
   \((m,d,R)=(E,c,c)\).  Thus §5's finite-family escape applies, and the
   Type-I class accounting of §§26 and 29 supplies the surrounding theory.
   What the earlier waves did not record is that this very narrow a = 1
   slice covers every hard prime below \(10^7\), nor the exact divisor test
   and finite bound (35.9)--(35.11) that certify that statement.  The prior
   §32 audit proves only that every prime through \(10^5\) has some Type-I
   tuple, not that one can take a = 1.

**Assessment 35.4 (did the blind attack find a missed door?).**  It found one
useful missed *reduction/data point*: the a = 1 Type-I divisor-cover sieve and
its zero failures through \(10^7\).  It also found two new negative facts: the
three exact a = 1 Type-II failures below \(10^6\), and the split-conic
diagonal/Pell death.  It found no new pointwise mechanism.  Every
unconditional prime family above is an instance of the campaign's existing
Case-A/Case-B identity supply, and the strongest new computation still asks
for an exact moving divisor.  Therefore the honest reconciliation verdict is:
**new special-slice theorem and computations, new failure diagnostics, no
advance past the ten-wave pointwise wall and no proof of Erdős--Straus.**

**Verification companion.**  `verify.py (ah)` compares the q = 3 factor and
literal-divisor criteria prime by prime; checks the q-window totals, all eight
Type-II cap counts, the complete three-prime residual, and the three rescue
tuples; reconstructs the 535 maximum least-offset census; and checks all
82,887 Type-I witnesses and their maximum.  Its elapsed time is reported as
campaign-host calibration only, with no correctness assertion tied to a
machine-dependent time limit.

---

## 36. The exact ray-character mass for Type I, and why it is not a positive class-number mass

**Headline (proved statements have the displayed quantifiers).**  For every odd prime
\(p\), the complete ordered, not-necessarily-primitive Type-I count is exactly
a finite Dirichlet-character projection of the divisor masses of
\(p^2+4ck^2\), and equivalently the integral-point count on the split quadrics
\(r^2=ck(ck s^2-ps-k)\) in Theorem 36.1 below; the primitive count is the
same projection with an explicit Möbius weight and is exactly Elsholtz--Tao's
\(f_I(p)\).  For every prime \(p\equiv1\pmod4\), the entire \(c=1\)
Gaussian slice is identically zero, while the \(k=1\) slice has the exact
character formula (36.13) but already vanishes at \(p=2521\).  The classical
Hurwitz--Kronecker mass forgets precisely the moving ray-class projector that
defines Type I: two natural restorations fail at the explicit finite tests in
§36.4.  Thus this section proves an exact structured count, not positivity;
no all-prime Type-I theorem and no proof of Erdős--Straus is obtained.

### 36.1 A finite ray-character formula and the split quadric

Let \(T_I(p)\) denote the number of ordered positive quadruples
\((a,b,c,k)\) satisfying
\(p(a+b)=k(4abc-1)\), without imposing \((a,b)=1\), and let
\(T_I^*(p)\) impose \((a,b)=1\).  Put

\[
 \mathcal B_p=\left\{(c,k):1\leq k\leq\lfloor2p/3\rfloor,
  \ 1\leq c\leq\left\lfloor{2p+k\over4k}\right\rfloor,
  \ (p,ck)=1\right\},                                      \tag{36.1}
\]
\[
 h=4ck,\qquad N_{c,k}=p^2+4ck^2,
 \qquad a_D={D+p\over h},\quad b_D={{N_{c,k}/D}+p\over h}.  \tag{36.2}
\]

**Theorem 36.1 (exact ray-character and quadric mass; proved).**  For every
odd prime \(p\),

\[
 \begin{split}
 T_I(p)
 &=\sum_{(c,k)\in\mathcal B_p}{1\over\varphi(h)}
   \sum_{\chi\ ({\rm mod}\ h)}\overline{\chi(-p)}
   \sum_{D\mid N_{c,k}}\chi(D)\\
 &=\sum_{(c,k)\in\mathcal B_p}{1\over\varphi(h)}
   \sum_{\chi\ ({\rm mod}\ h)}\overline{\chi(-p)}
   \prod_{\ell^e\parallel N_{c,k}}
       (1+\chi(\ell)+\cdots+\chi(\ell)^e).                 \tag{36.3}
 \end{split}
\]

Here all Dirichlet characters modulo \(h\), including imprimitive ones, are
included.  If

\[
 w_p(D;c,k)=
 \begin{cases}
 \displaystyle\sum_{g\mid a_D,\ g\mid b_D}\mu(g),
      &D\equiv-p\pmod h,\\
 0,&D\not\equiv-p\pmod h,
 \end{cases}                                                \tag{36.4}
\]

(where the first case makes \(a_D,b_D\) integral), then the exact primitive
version is

\[
 T_I^*(p)=\sum_{(c,k)\in\mathcal B_p}{1\over\varphi(h)}
   \sum_{\chi\ ({\rm mod}\ h)}\overline{\chi(-p)}
   \sum_{D\mid N_{c,k}}\chi(D)w_p(D;c,k).                   \tag{36.5}
\]

There is also the exact integral-point expression

\[
 T_I(p)=\sum_{(c,k)\in\mathcal B_p}
 \#\left\{(s,r):
 \begin{array}{l}
 2\leq s\leq (N_{c,k}+1+2p)/h,\quad r\in\mathbb Z,\\
 r^2=ck(ck s^2-ps-k),\quad ck\mid r,\\
 |r|<ck s,\quad s\equiv r/(ck)\pmod2
 \end{array}\right\}.                                     \tag{36.6}
\]

For \(p\equiv1\pmod4\), no point in (36.6) has \(r=0\), so
\(T_I(p)\) is twice the unordered count.

*Proof.*  Theorem 26.1 and Lemma 26.2 say exactly that the desired rows are
indexed by (36.1) and by divisors
\(D\mid N_{c,k}\) with \(D\equiv-p\pmod h\).  Moreover
\((N_{c,k},h)=1\): modulo every prime dividing \(ck\), the norm is
\(p^2\), and it is odd.  Thus every divisor \(D\) is a unit modulo \(h\),
and character orthogonality gives

\[
 {\bf1}_{D\equiv-p\ (h)}={1\over\varphi(h)}
 \sum_{\chi\ ({\rm mod}\ h)}\chi(D)\overline{\chi(-p)}.
\]

Summing proves the first line of (36.3); multiplicativity in \(D\) proves
the Euler product.  The elementary identity
\({\bf1}_{(a_D,b_D)=1}=\sum_{g\mid a_D,\,g\mid b_D}\mu(g)\)
proves (36.5).

For the second description put \(s=a+b\), \(t=a-b\), and \(r=ck t\).
The Type-I equation is precisely

\[
             ck(s^2-t^2)=ps+k,
 \qquad r^2=ck(ck s^2-ps-k).                                \tag{36.7}
\]

The divisors paired with the row are
\(D=4ack-p,D'=4bck-p\), and

\[
 D+D'=hs-2p,\quad DD'=N_{c,k},\quad
 (D+D')^2-4N_{c,k}=(D-D')^2.                                \tag{36.8}
\]

Since \(D+D'\leq N_{c,k}+1\), (36.6)'s upper bound follows.  Conversely,
the divisibility, parity and strict-size conditions in (36.6) make
\(t=r/(ck)\) and \(a=(s+t)/2,b=(s-t)/2\) positive integers; (36.7)
recovers the Type-I equation.  This proves the bijection.  Finally, if
\(a=b\), parity first gives \(k=2\ell\), and
\(pa=\ell(4a^2c-1)\).  Since \((a,4a^2c-1)=1\), write
\(\ell=au\); primality forces \(u=1\) and
\(p=4a^2c-1\equiv3\pmod4\), a contradiction when
\(p\equiv1\pmod4\). ∎

There is an entirely real square-indicator reading of (36.6).  When
\(ck\mid ps+k\), put
\(W=s^2-(ps+k)/(ck)\).  The identity

\[
                  {\bf1}_{W\text{ a square}}=
                  \sum_{d\mid W}\lambda(d)                 \tag{36.9}
\]

for \(W>0\), with \(\lambda\) the Liouville function, turns (36.6), for
\(p\equiv1\pmod4\) (where \(r=0\) is impossible, so \(W>0\) on every
point), into twice a finite \((c,k,s)\)-sum of the right side of (36.9),
restricted by
\(\sqrt W<s\) and \(\sqrt W\equiv s\pmod2\).  For \(p\equiv3\pmod4\)
the diagonal \(W=0\) points must be added separately:
\(T_I(p)=2S_{W>0}+S_{W=0}\), as at \(p=3\), where
\((a,b,c,k)=(1,1,1,2)\) has \(W=0\) and \(T_I(3)=3\) is odd.  This is
exact, but it does
not make positivity easier: the square indicator has merely been written as
a cancelling divisor sum.  Geometrically (36.8) is a split hyperbola, not a
Pell conic, in agreement with §§20.1 and 35.2.

### 36.2 The \(c=1\) Gaussian slice vanishes on every hard prime

**Theorem 36.2 (Gaussian-divisor formula and complete obstruction; proved).**
For an odd prime \(p\), the \(c=1\) contribution to \(T_I(p)\) is

\[
 T_{c=1}(p)=\sum_{1\leq k\leq\lfloor2p/3\rfloor}
 \ \sum_{[\alpha]\mid p+2ki\ \text{ in }\mathbb Z[i]}
 {\bf1}_{N(\alpha)\equiv-p\pmod {4k}},                       \tag{36.10}
\]

where Gaussian divisors are taken modulo associates.  For every
\(p\equiv1\pmod4\),

\[
                         T_{c=1}(p)=0.                       \tag{36.11}
\]

Thus, within the requested hard-prime domain, the exact failure set of the
\(c=1\) sub-count is **all** primes, not a sparse exceptional set.

*Proof.*  The bound on \(k\) is (36.1) with \(c=1\), and \(p\nmid k\).
Set \(z=p+2ki\).  The Gaussian integers \(z,\bar z\) are coprime up to a
unit: an odd common Gaussian prime would force its rational prime below it
to divide both \(p\) and \(k\), while \(1+i\nmid z\).  Since
\(N(z)=p^2+4k^2\), unique factorisation now gives a bijection

\[
 \{D:D\mid N(z)\}\longleftrightarrow
 \{[\alpha]:\alpha\mid z\},\qquad D=N(\alpha).
\]

Indeed every rational prime dividing the primitive sum of two squares
splits, exactly one prime above it occurs in \(z\), and its exponent in
\(\alpha\) is the exponent selected in \(D\).  Theorem 26.1 therefore gives
(36.10).  The same argument shows that every rational prime divisor of
\(N(z)\) is \(1\pmod4\); hence every positive divisor \(D\) is
\(1\pmod4\).  But the required grade for \(p\equiv1\pmod4\) is
\(D\equiv-p\equiv3\pmod4\).  No term survives. ∎

This is the sharp outcome of the class-number-one lead.  The form
\(X^2+4Y^2\) has discriminant \(-16\) and class number one, but unique
factorisation exposes a local **wrong-grade obstruction** rather than a
positive mass.  For general \(c\), \(p^2+4ck^2\) is represented by
\(X^2+4cY^2\), of discriminant \(-16c\); ordinary form classes do not encode
the additional ray condition modulo \(4ck\), whose modulus itself contains
the represented coordinate \(k\).

### 36.3 The \(k=1\) slice is an exact character sum, but not always positive

**Theorem 36.3 (the \(k=1\) divisor/character formula; proved).**  For every
prime \(p\equiv1\pmod4\), the ordered \(k=1\) count, which is automatically
primitive, is

\[
 T_{k=1}(p)=2\sum_{1\leq a\leq p/2}
 \ \sum_{\substack{f\mid pa+1\\ f\leq p}}
       {\bf1}_{f\equiv-p\pmod {4a}}                         \tag{36.12}
\]
\[
 ={2}\sum_{1\leq a\leq p/2}{1\over\varphi(4a)}
   \sum_{\chi\ ({\rm mod}\ 4a)}\overline{\chi(-p)}
   \sum_{\substack{f\mid pa+1\\f\leq p}}\chi(f).        \tag{36.13}
\]

*Proof.*  A \(k=1\) row is primitive because a common divisor of \(a,b\)
would divide both sides of \(p(a+b)=4abc-1\), hence divide 1.  There is no
diagonal row because its left side is even and its right side odd.  Orient a
row by \(a<b\), and set \(f=4ac-p\).  Solving for \(b\) gives

\[
                         bf=pa+1.                            \tag{36.14}
\]

The inequality \(a<b\) is equivalent here to \(f\leq p\), and
\(p+f=4ac\) then gives \(a\leq p/2\).  Conversely a divisor in (36.12)
makes \(c=(p+f)/(4a)\) and \(b=(pa+1)/f\) positive integers with
\(a<b\), and reversing (36.14) proves the equation.  The factor two restores
the other orientation.  Character orthogonality gives (36.13); nonunit
\(f\)'s contribute zero on both sides because \(-p\) is a unit modulo
\(4a\). ∎

**Computational 36.1 (exact stated ranges).**  Direct generation from
(36.12) for every one of the 143 primes \(p\equiv1\pmod {24}\),
\(p<10^4\), finds exactly one zero:

\[
                              p=2521.                         \tag{36.15}
\]

The ordered \(k=1\) counts for the eleven primes in (26.8) are

\[
 4,2,8,6,8,8,20,0,8,16,18,
\]

and for the nine primes in (32.14) they are

\[
 14,14,22,16,44,24,24,72,52.
\]

Thus neither the Gaussian class-number-one slice nor the moving-discriminant
\(k=1\) slice can prove positivity by itself.  The zero in (36.15) is only a
slice failure: (26.8) gives twelve ordered Type-I rows for 2521.

### 36.4 Hurwitz--Kronecker tests: where the projector is lost

Use the convention that \(H(M)\) counts reduced, possibly imprimitive,
positive definite forms of discriminant \(-M\), with generic weight 1,
weights \(1/2\) and \(1/3\) for the square and hexagonal exceptional
classes, \(H(0)=-1/12\), and \(H(M)=0\) unless
\(M\equiv0,3\pmod4\).  For nonsquare \(n\), the classical relation is

\[
 \sum_{t\in\mathbb Z,\ t^2\leq4n}H(4n-t^2)
       =\sum_{d\mid n}\max(d,n/d).                          \tag{36.16}
\]

It is important that (36.16) is an **unprojected, weighted** divisor mass.
At a fixed Type-I slice, the actual trace \(D+D'\) in (36.8) lies on the
hyperbolic side \((D+D')^2\geq4N_{c,k}\); Hurwitz forms occupy the elliptic
side \(t^2\leq4N_{c,k}\).  Relation (36.16) bridges those sides only after
summing every divisor and weighting it by its larger cofactor.  Type I asks
instead for an unweighted divisor in one moving class
\(-p\pmod {4ck}\).

**Computational 36.2 (disciplined candidate log).**  Reduced-form enumeration
with the convention above verifies (36.16) for every nonsquare
\(2\leq n\leq40\), and at \(n=5369\).  The following two candidates, each
with the stated derivation, fail.

1. **Principal-ray deprojection.**  Dropping all nonprincipal characters in
   (36.3) suggests that each of the \(\varphi(h)\) unit classes receives
   \(1/\varphi(h)\) of the Hurwitz-weighted mass (36.16).  For
   \((p,c,k)=(73,10,1)\),
   \(N=5369=7\cdot13\cdot59\), \(h=40\), and the target divisors are
   \(7,767\).  Their weighted mass is \(1534\), whereas the full mass is
   \(13280\), whose proposed share is \(13280/\varphi(40)=830\).
   Thus the ray classes are not exactly equidistributed; the first
   nonprincipal characters cannot be discarded.

2. **Single discriminant.**  Collapsing all moving forms to the most obvious
   global discriminant suggests
   \(T_I^*(p)/2=H(4p)\).  It happens to hold at \(p=73,193\): both sides
   are 4.  It fails at the next tested value \(p=241\), where the primitive
   unordered Type-I count is 4 but \(H(964)=12\).  This test is only on
   \(p=73,193,241\); no fitted asymptotic is inferred.

No further numerical linear combinations were fitted: without a map from a
Type-I row to the proposed form classes, such fitting would be unconstrained.
The exact form-theoretic statement retained from the hunt is instead the ray
character formula (36.3)--(36.5).

### 36.5 Exact reconciliation with Elsholtz--Tao and the square test

Write an Elsholtz--Tao \(\Sigma_p^I\) sextuple as
\((a_E,b_E,c_E,d_E,e_E,f_E)\).  Their equations (2.1)--(2.9) and map
\(\pi_p^I\) give the exact dictionary

\[
 (a_E,b_E,c_E,d_E,e_E,f_E)
   =(A,B,K,C,m,4ACK-p),\qquad m={A+B\over K},                \tag{36.17}
\]
\[
 \pi_p^I=(pABC,ACK,BCK).                                    \tag{36.18}
\]

Thus their convention puts the unique \(p\)-divisible denominator first;
the campaign puts it last.  This fixed permutation changes no count.
Their reflection swaps \(A,B\), and their dilation

\[
 (A,B,K,C)\mapsto(gA,gB,gK,C/g^2),\qquad g^2\mid C,         \tag{36.19}
\]

is exactly the nonprimitive expansion recorded in §32.3.  Consequently

\[
                     f_I(p)=T_I^*(p),                        \tag{36.20}
\]

with both sides ordered in the two non-\(p\) denominators, while

\[
 T_I(p)=\sum_{(A,B,C,K)\ \text{primitive, ordered}}
             \prod_{\ell^e\parallel C}(\lfloor e/2\rfloor+1). \tag{36.21}
\]

For an odd prime, Elsholtz--Tao's total ordered count is therefore exactly
\(f(p)=3T_I^*(p)+3f_{II}(p)\): the factor 3 chooses the position of the
exceptional denominator, not an extra \(A,B\) swap.

This dictionary supplies both structural sanity checks requested here.
First, Elsholtz--Tao Proposition 1.6 proves
\(f_I(n)=f_{II}(n)=0\) for every odd perfect square \(n\).  Formula (36.3)
is deliberately a **prime-only raw-tuple formula**; extending it to composite
\(n\) while dropping the coprimality and canonical conditions would not
count \(f_I(n)\).  The Elsholtz--Tao canonical count, which agrees with
\(T_I^*(p)\) on primes by (36.20), vanishes on odd squares; so no positive
mass has been smuggled across the square-class
escape of §17.3.  Second, their Theorem 1.1 gives

\[
 N\log^2N\ll\sum_{p\leq N}T_I^*(p)
 \ll N\log^2N\log\log N,                                  \tag{36.22}
\]

which is exactly the prime-average scale required of the primitive formula
and matches the divisor-function fluctuations they note.  The full identity
supply remains subject to §18.2's cubic ceiling; (36.3) reorganizes that
supply and does not create additional mass.

### 36.6 Literature audit and positivity assessment

**Literature audit (sources actually inspected).**

* The supplied full Elsholtz--Tao arXiv:1107.1010v6 PDF was read through
  §§1--11 and the appendix.  Equations (2.1)--(2.9), Propositions 2.2--2.3,
  Lemma 2.8, Proposition 1.6, Theorem 1.1, Proposition 1.9, and the divisor
  average in §7 are the sources used above.  Proposition 1.9 classifies the
  fixed-parameter polynomial congruence families; it does not turn the
  moving ray projector in (36.3) into a fixed class.  Their Type-I upper
  bound explicitly reduces to averages of \(\tau(4a^2d+1)\), not class
  numbers.
* Yamamoto's 1965 primary J-STAGE scan (pp. 37--47) was downloaded; it is an
  image PDF and was OCR-read.  His Lemma 4 assigns Kronecker symbol \(-1\)
  to every nonempty covering in his system, and Theorem 2 concludes that
  their union contains no perfect square.  This is a quadratic-residue
  obstruction to polynomial/congruence coverings, not a positive
  class-number formula.
* Salez, arXiv:1406.6307v1, was downloaded and read.  It reproduces the
  Rosati four-parameter alternatives, proves a seven-equation polynomial
  classification, identifies which four equations were already in
  Yamamoto, and reports the computation through \(10^{17}\).  The primary
  Rosati PDF endpoint was found through EuDML/BDIM but timed out repeatedly;
  no claim here is attributed to an unread Rosati primary text.
* Elsholtz--Planitzer, arXiv:1805.02945v1, was downloaded and inspected.  Its
  relevant result is the general \(O_\epsilon(n^{3/5+\epsilon})\) bound and
  matching expected-time enumeration for fixed numerator, extending the
  Elsholtz--Tao prime bound.  No Hurwitz or class-number identity appears in
  the inspected text.

**Assessment 36.1 (positivity).**  Equations (36.3) and (36.13) are exact
character sums, but their principal terms do not dominate pointwise.  The
nonprincipal part enforces the whole moving divisor grade, as the numerical
failure \(1534\ne830\) shows.  Ordinary class groups for discriminant
\(-16c\) forget this ray datum; even discriminant \(-16\), with unique
factorisation, gives the universal hard-prime zero (36.11).  The broader
\(k=1\) character mass also has a genuine zero (36.15).  Proving
\(T_I^*(p)>0\) for every hard prime from (36.5) would itself prove the
Type-I strengthening of Erdős--Straus, and no cancellation estimate capable
of doing so is obtained here.

**Assessment 36.2 (failure log).**  The quadric lead is exact but splits back
into the original divisor pair; it supplies no Pell orbit (§§9.3, 20.1,
35.2).  Gaussian factorisation solves the \(c=1\) bookkeeping but exposes
the wrong residue grade.  The \(k=1\) ray-character sum is exact but not
positive.  The Hurwitz--Kronecker identity controls the wrong weighted,
unprojected mass, and both derived collapse candidates above fail.  Binary
composition still has §26.3's \(+p\) versus \(-p\) sign obstruction, and
bounded congruence extraction still has §17.3's square-class escape.  The
realistic endpoint is therefore the exact ray-character structure theorem
and a precise account of the missing projector, not a positivity theorem.

**Verification companion.**  `verify.py (ai)` independently regenerates the
20 stated raw and primitive counts by the cutoff-free denominator enumerator,
including the unique nonprimitive dilations; checks the quadric identities
(36.6)--(36.8) on every divisor row for every odd prime below 50 (below 100
with `ES_FULL_SCAN=1`); enumerates the literal \((s,r)\) points of (36.6)
independently of the divisor loop, and evaluates the full complex character
projection (36.3) with all \(\varphi(h)\) characters, for every odd prime
below 30, confirming both against the divisor count (including the odd
\(T_I(3)=3\) with its \(W=0\) diagonal point); evaluates the \(k=1\)
character formula (36.13) at \(p=73,193\); checks the rational-norm Gaussian
slice count and the exact \(k=1\) failure set for
all hard primes below \(10^4\); brute-counts reduced forms for (36.16); and
replays both failed class-number candidates.  The divisor generation is
streamed per \(x\); peak storage is the smallest-prime-factor array and one
\(x\)-fiber, with no Cartesian-product array.
## 37. Two-level critical-window sieve: the prime half transfers, and the composite half is a residue-resolved moment wall

**Headline (proved statements and open boundary, with quantifiers).**  A
corrected residue-set version of Lemma 33.3 is proved below: for every large
\(X\), every pointwise minorant whose terms are residue **sets** of modulus
\(\exp\{o(L^4)\}\), whose exact CRT mean is \(\exp\{-o(L^3)\}\), and whose
class-weighted coefficient ledger is \(\exp\{o(L^4)\}\), transfers uniformly
to every \(N\) with \(\log N\asymp L^4\).  The proposed two-level sieve
satisfies all of these requirements for the complete prime-modulus subsystem,
with odd degree \(O(L^2)=o(L^3)\) and mean \(\exp\{-\Theta(L^2)\}\); this is
a new accounting formulation, not a stronger result than Theorem 24.4.  For
the composite subsystem, the suggested one-common-prime \(D=1\) stars are
proved harmless, but no pointwise minorant satisfying Lemma 33.3 is
constructed and no impossibility theorem for all such minorants is proved.
The exact unproved input is a residue-resolved compatible factorial-moment
bound at order \(\Theta(L^3/\log L)\).  The §31 charges control only total
incidence at a prime and, even after granting their best \(L^3/(p\log z)\)
shape, the direct second-moment summation loses a factor \(\asymp\log L\).
Thus (33.16) and \(H_{\rm PF}'\) remain **OPEN**.

**Later status correction.**  Section 47 refutes the literal factorial-moment
bound (37.19) for the only-prime-reduced count \(H\) defined below; Proposition
37.3 remains a proved conditional implication.  Section 49 proves that the
same bound is false for the void-equivalent implication antichain as well.
(wave-17 update)

### 37.1 The corrected residue-set transfer ledger

After (31.23), write the quarantined integers as \(n=P_zm\); multiplication
by \(P_z^{-1}\) transforms every surviving atom to a congruence in \(m\).
For a set \(U\subseteq\mathbb Z/d\mathbb Z\), write
\(1_{U,d}(m)=\mathbf1_{m\bmod d\in U}\) and \(\rho(U)=|U|\).

**Lemma 37.1 (residue-set finite transfer; proved).**  Fix any specified
family \(\mathcal F_X\) of surviving atoms, and let \(I_X\) be a finite
index set.  For each \(\alpha\in I_X\), let
\(U_\alpha\subseteq\mathbb Z/d_\alpha\mathbb Z\), where \(d_\alpha\) is
a divisor of the surviving CRT period (hence is coprime to \(P_z\)), and let
\(c_\alpha\in\mathbb R\).  Suppose

\[
 B_X(m)=\sum_{\alpha\in I_X}c_\alpha1_{U_\alpha,d_\alpha}(m)
 \leq\mathbf1_{\{\text{no atom of }\mathcal F_X\text{ at }m\}} \tag{37.1}
\]

for every integer \(m\), and, in the exact CRT space,

\[
 \mathbb E_{\rm CRT}B_X\geq e^{-o(L^3)},\qquad
 \log\max_\alpha d_\alpha=o(L^4),\qquad
 \log\mathcal R_X=o(L^4),
 \quad
 \mathcal R_X:=\sum_\alpha|c_\alpha|\rho(U_\alpha).         \tag{37.2}
\]

Then, uniformly for \(c_-L^4\leq\log N\leq c_+L^4\), where
\(0<c_-<c_+\) are fixed,

\[
 |\operatorname {Av}(\mathcal F_X;N)|\geq N e^{-o(L^3)}.    \tag{37.3}
\]

In particular this is the claimed bound for \(\operatorname {Av}_X\) when
\(\mathcal F_X\) is the complete surviving family.  The modulus condition
in (37.2) records the intended critical-window
locality; the counting proof itself only needs the weighted ledger
\(\mathcal R_X\), not an unweighted number of terms.

*Proof.*  Put \(H=\lfloor N/P_z\rfloor\).  A set of \(\rho(U_\alpha)\)
classes modulo \(d_\alpha\) has

\[
 \sum_{m\leq H}1_{U_\alpha,d_\alpha}(m)
   =H{\rho(U_\alpha)\over d_\alpha}+O(\rho(U_\alpha)).     \tag{37.4}
\]

Consequently

\[
 \sum_{m\leq H}B_X(m)
   =H\mathbb E_{\rm CRT}B_X+O(\mathcal R_X).                \tag{37.5}
\]

The first term has logarithm
\(\log N-O(z)-o(L^3)=\log N-o(L^3)\), while
\(\log\mathcal R_X=o(L^4)\); since \(\log N\geq c_-L^4\),
the error is negligible.  Equation (37.1) and
\(P_z=\exp\{O(z)\}=\exp\{o(L^3)\}\) prove (37.3). \(\square\)

For an atom monomial, compatibility gives one class and incompatibility gives
the empty set, so \(\rho\leq1\) and Lemma 37.1 recovers Lemma 33.3.  The
correction is essential for a tensor factor: the rounding error for one term
is \(O(\rho(U))\), not \(O(1)\).  Thus replacing
\(\sum|c_S|\) by a residue-set coefficient sum without the factor \(\rho\)
would be false.

### 37.2 The two-level construction closes the prime side

Let \(f(\ell)=F(\ell)\) and, in the transformed \(m\)-coordinate, let
\(S_\ell=P_z^{-1}\mathscr R(\ell)\pmod\ell\).  This unit dilation preserves
cardinality and every compatibility relation.  Lemma 24.3, applied once at
\(X\) and once at a polylogarithmic argument, gives

\[
 \sum_{\substack{z<\ell\leq X\\\ell\equiv3(4)}}
 {f(\ell)\over\ell}=\Theta(L^2),
 \qquad
 \sum_{\substack{\ell\leq L^{O(1)}\\\ell\equiv3(4)}}
 {f(\ell)\over\ell}=O((\log L)^2).                         \tag{37.6}
\]

Here and below \(\ell\) is prime.  Thus quarantine removes only
\(O((\log L)^2)\), not a positive part of the quadratic prime mass.
Choose any \(h(L)\to\infty\) slowly enough that

\[
 z<Y={L^4\over h(L)}<X.                                    \tag{37.7}
\]

Put

\[
 d_0=\prod_{z<\ell\leq Y,\ \ell\equiv3(4)}\ell,
 \qquad
 U_0=\prod_{z<\ell\leq Y,\ \ell\equiv3(4)}
       ((\mathbb Z/\ell\mathbb Z)\setminus S_\ell),
 \qquad T_0=1_{U_0,d_0}.                                   \tag{37.8}
\]

The prime number theorem gives \(\log d_0=O(Y)=o(L^4)\), and
\(\log\rho(U_0)\leq\log d_0\).  The forbidden mass below \(Y\) is only
\(O((\log Y)^2)=O((\log L)^2)\), while the tail \(Y<\ell\leq X\) still
has mass \(\Theta(L^2)\).

Let \(H_P(m)\) count the tail prime atoms violated at \(m\), put
\(\mu_P=\mathbb EH_P=\Theta(L^2)\), and choose the least odd
\(r\geq8\mu_P\).  Define

\[
 Q_r(H_P)=\sum_{j=0}^r(-1)^j{H_P\choose j},
 \qquad B_P=T_0Q_r(H_P).                                   \tag{37.9}
\]

**Theorem 37.2 (prime-side two-level minorant; proved).**  For every integer
\(m\),

\[
 B_P(m)\leq\mathbf1_{\{m\text{ avoids every surviving prime atom}\}}.
                                                                    \tag{37.10}
\]

It has tail atom degree \(r=O(L^2)\), every term has modulus logarithm at
most \(\log d_0+rL=o(L^4)\), and its exact CRT mean is

\[
 \mathbb E_{\rm CRT}B_P\geq e^{-O(L^2)},                   \tag{37.11}
\]

and ledger

\[
 \log\sum_\alpha |c_\alpha|\rho(U_\alpha)=o(L^4).         \tag{37.12}
\]

Hence Lemma 37.1 transfers the lower bound
\(|\operatorname {Av}^{\rm prime}_X(N)|\geq Ne^{-O(z)-O(L^2)}
=Ne^{-o(L^3)}\)
to \(\log N\asymp L^4\): the quarantine itself costs the factor
\(P_z^{-1}=e^{-O(z)}\), which dominates the \(L^2\) prime mass.  The
sharper standalone rate \(Ne^{-O(L^2)}\) in this window is Theorem 24.4's
(whose range \(\log N\geq C_3L^3\) contains it); the present construction
is the residue-set-ledger accounting of that bound after quarantine, not an
improvement.

*Proof.*  If \(T_0=0\), the left side of (37.10) is zero.  If \(T_0=1\),
odd Bonferroni gives (37.10).  For an integer \(h\geq1\),

\[
 \sum_{j=0}^r(-1)^j{h\choose j}=-{h-1\choose r};            \tag{37.13}
\]

therefore the loss from the exact tail void is at most
\(\mathbb E{H_P\choose r+1}\).  Distinct prime coordinates are independent,
and atoms on one coordinate are disjoint, so

\[
 \mathbb E{H_P\choose r+1}
 \leq {\mu_P^{r+1}\over(r+1)!}
 \leq\left({e\mu_P\over r+1}\right)^{r+1}.                \tag{37.14}
\]

The tail Euler product is at least \(e^{-2\mu_P}\), by Lemma 21.2 and
\(-2u\leq\log(1-u)\) for \(u\leq1/2\).  The last member of (37.14), with
\(r\geq8\mu_P\), is smaller than a fixed fraction of that product.  This
proves (37.11), including the independent low tensor.

Expand only the tail factor in atom indicators.  If
\(W_P=\sum_{Y<\ell\leq X}f(\ell)\), then
\(W_P\leq K=\exp\{O(L)\}\) by (33.8)'s atom count.  Each resulting term
has at most \(\rho(U_0)\) classes, and hence

\[
 \mathcal R_X\leq\rho(U_0)\sum_{j\leq r}{W_P^j\over j!},
 \quad
 \log\mathcal R_X\leq o(L^4)+O(rL)=o(L^4).                \tag{37.15}
\]

Its modulus divides \(d_0X^r\), proving the other budgets. \(\square\)

Theorem 24.4 already proves the same prime-slice lower bound, in the larger
range \(\log N\geq C_3L^3\), by expanding all prime atoms.  Theorem 37.2 is
bankable here because it verifies the proposed residue-set ledger exactly;
it does not improve that theorem.

### 37.3 What the composite continuation would have to prove

Delete a composite atom \(A\) whenever, for some prime \(p\mid M_A\), its
transformed projection modulo \(p\) lies in \(S_p\) (equivalently, its
original projection lies in \(\mathscr R(p)\)).  Such an event is a subset
of a retained prime atom, so deleting all of them does not change the
union once the complete prime subsystem remains.  Call the residual family
\(\mathcal C^\circ\).

Condition on \(T_0=1\).  Every \(A\in\mathcal C^\circ\) fixes an allowed
residue at each low prime dividing its modulus, and hence

\[
 \Pr(A\mid T_0=1)={1\over M_A}
 \prod_{\substack{p\mid M_A\\z<p\leq Y}}
       {p\over p-f(p)}={1+o(1)\over M_A}                   \tag{37.16}
\]

uniformly in \(A\).  Indeed the maximal-order divisor bound gives
\(f(p)=p^{o(1)}\), while
\(p>z=L^{3+o(1)}\) and
\(\omega(M_A)\leq L/\log z\); thus the logarithm of the product in
(37.16) is at most \(L^{-2+o(1)}\).  The exact tensor does not create a
hidden large conditional density.

Let \(H\) count the tail prime atoms together with
\(\mathcal C^\circ\) in this conditioned space, and put

\[
                         \Lambda={L^3\over\log L}.           \tag{37.17}
\]

Equations (31.14), (33.8), and (37.16) give
\(\mathbb EH=O(\Lambda)\).  Also the unconditional full void after
quarantine is \(e^{-O(\Lambda)}\) by Theorem 31.4; dividing by
\(\Pr(T_0=1)\leq1\) shows

\[
                 \Pr(H=0\mid T_0=1)\geq e^{-O(\Lambda)}.   \tag{37.18}
\]

**Proposition 37.3 (the exact factorial-moment sufficient input; proved).**
Suppose there are fixed constants \(C,D>0\), with \(D\) sufficiently large
in terms of \(C\) and the constant in (37.18), and an even integer
\(m\in[D\Lambda,D\Lambda+2]\), such that

\[
                  \mathbb E(H)_m\leq(C\Lambda)^m.           \tag{37.19}
\]

Then the two-level sieve satisfies Lemma 37.1 with
\(r=m-1=o(L^3)\), and consequently proves (33.16).

*Proof.*  Use \(B=T_0Q_{m-1}(H)\).  It is pointwise below the full void by
odd Bonferroni.  Equations (37.13) and
\({h-1\choose m-1}\leq{h\choose m}\) give

\[
 \mathbb E(Q_{m-1}(H)\mid T_0=1)
 \geq\Pr(H=0\mid T_0=1)-{(C\Lambda)^m\over m!}.             \tag{37.20}
\]

Stirling's bound makes the second term at most
\((eC/D)^m\), which is a small fixed fraction of (37.18) when \(D\) is
large.  There are \(K=\exp\{O(L)\}\) atoms, so after multiplication by
\(T_0\), every term is a residue set with at most \(\rho(U_0)\) classes and

\[
 \operatorname {degree}=m-1=O(\Lambda)=o(L^3),\quad
 \log(\operatorname {modulus})\leq Y+O(\Lambda L)=o(L^4),
 \quad
 \log(\operatorname {ledger})\leq Y+O(\Lambda L)=o(L^4). \tag{37.21}
\]

Lemma 37.1 applies. \(\square\)

Thus only one high factorial moment, rather than a full alternating tail, is
needed.  No estimate in §§24, 27, 31, or 33 proves (37.19).  This is the
precise point at which the original two-level construction stopped.  Section
47 subsequently proves that (37.19) is false for this count \(H\), while the
proposition itself remains valid for the implication-antichain repaired count.
(wave-16 review repair)

### 37.4 Star clusters, the residue-square loss, and cluster expansions

The specific large-common-prime star proposed in the attack does **not**
break (37.19).  Fix a prime \(p>z\), and let \(\mathcal Q\) be distinct
primes \(q>z\) for which \(pq\leq X\) and \(pq\equiv3\pmod4\).  Take only
the \(D=1\) atom at every modulus \(pq\).  These atoms all prescribe
\(-4\pmod p\) and are mutually compatible.  For every \(m\geq1\), their
exact unordered star contribution is

\[
 {1\over p}\sum_{\substack{S\subseteq\mathcal Q\\|S|=m}}
       \prod_{q\in S}{1\over q}
 \leq {1\over p\,m!}
       \left(\sum_{q\in\mathcal Q}{1\over q}\right)^m
 \ll { (\log L+1)^m\over p\,m!}.                           \tag{37.22}
\]

The equality uses
\(\operatorname {lcm}(pq:q\in S)=p\prod_{q\in S}q\); the last estimate is
Mertens for primes.  In particular it remains true for
\(p\asymp X^{1/2}\), the suggested worst scale.  Since the tail prime mass
alone is \(\gg L^2\), (37.22) is far below the Poisson-sized allowance in
(37.19).  The collapse factor \(p^{m-1}\) is real, but the incident harmonic
mass paid before collapse is too small.  This calculation concerns the
\(D=1\) star; it is not a bound for all intrinsic classes at the same
moduli.

Here is the actual missing estimate.  For a high prime \(p\) and a residue
\(a\pmod p\), let

\[
 u_{p,a}=\sum_{\substack{A\in\mathcal C^\circ\\p\mid M_A\\
                         r_A\equiv a\ (p)}}
          \Pr(A\mid T_0=1),
 \qquad t_p=\sum_a u_{p,a}.                                \tag{37.23}
\]

For squarefree pairs whose moduli have gcd exactly \(p\), compatibility is
exactly equality of their \(p\)-residues, and their intersection probability
is at most \(p\) times the product of their marginals (exactly
\(p-f(p)\) times for \(z<p\leq Y\), where the \(T_0\)-conditioning
renormalizes the shared coordinate, and exactly \(p\) times for
\(p>Y\)).  Thus their pair contribution
is bounded by a sub-sum of the residue-square expression

\[
                         p\sum_{a\bmod p}u_{p,a}^2.          \tag{37.24}
\]

Theorem 31.3 controls the \(\ell^1\) incidence \(t_p\), not its distribution
among residues.  Even granting the stronger, diagonal-free idealization

\[
                         t_p\ll{\Lambda\over p},            \tag{37.25}
\]

Cauchy's worst case in (37.24), summed over high primes, gives only

\[
 \sum_{z<p\leq X}p\sum_a u_{p,a}^2
 \leq\sum_{z<p\leq X}p t_p^2
 \ll\Lambda^2\sum_{z<p\leq X}{1\over p}
 \asymp\Lambda^2\log L.                                   \tag{37.26}
\]

The actual softened charge \(a_p=A(b_p+u_p)\) is weaker than (37.25) in its
short-cofactor term.  Therefore the present charge estimates lose a growing
factor already at the pair audit.  Removing it requires a residue-dispersion
bound such as

\[
              \sum_{z<p\leq X}p\sum_a u_{p,a}^2=O(\Lambda^2),\tag{37.27}
\]

followed by higher-codegree analogues strong enough for \(m\asymp\Lambda\).
Equation (37.26) is not a counterexample to (37.27): it records the exact
factor lost by the available \(\ell^1\) information.  The small exact data
below show no growing-factor phenomenon at their scales.

The Scott--Sokal repulsive-lattice-gas correspondence does not supply the
missing pointwise step.  Its independent-set polynomial
\(Z_G(-\boldsymbol p)\) and convergent Mayer expansion control a numerical
lower bound for the void under the Lovász-local-lemma/zero-free condition
(`sources/scott-sokal-0309352.pdf`, especially §§1.1--1.2 and 4--5).  Their
monomials use independent sets of the **dependency graph** with products of
marginal activities, not the actual compatible cylinder intersections.  The
literal polynomial

\[
 \sum_{S\text{ independent in }G}(-1)^{|S|}
             \prod_{A\in S}1_A(n)                           \tag{37.28}
\]

is not a pointwise minorant: if the violated-event induced graph is the
five-vertex path, (37.28) equals
\(1-5+6-1=1\), whereas the void indicator is zero.  Truncating the Mayer
series for \(\log Z_G\), or exponentiating that truncation, likewise gives a
number in the CRT model rather than a pointwise polynomial in the event
indicators.  A one-sided surrogate exploiting the small cylinder activities
would be new; adversarial approximate-inclusion--exclusion results do not
construct it for this arithmetic measure.

### 37.5 Exact finite companion and verdict

**Computational 37.4 (exact finite scope).**  `verify.py (aj)` enumerates all
composite \(z\)-rough intrinsic atoms, merges compatible congruences by exact
CRT, and computes the elementary intersection sums

\[
 e_j=\sum_{|S|=j}\Pr\left(\bigcap_{A\in S}A\right),
 \qquad 1\leq j\leq4.                                      \tag{37.29}
\]

“Reduced” deletes every composite atom implied by a prime atom as above.  The
reported ratios are \(j!e_j/\mu^j\), where
\(\mu=\sum_A1/M_A\):

\[
\begin{array}{c|c|c|r|c|rrrr}
X&z&\text{family}&K&\mu&j=1&j=2&j=3&j=4\\ \hline
80&2&\text{raw}&42&1.10910&1&1.184&1.447&1.720\\
80&2&\text{reduced}&14&.40213&1&1.382&1.647&.978\\
120&3&\text{raw}&64&.77139&1&.894&.655&.348\\
120&3&\text{reduced}&34&.41444&1&.986&.824&.419\\
200&5&\text{raw}&55&.42975&1&.611&.191&.124\\
200&5&\text{reduced}&28&.21273&1&.499&0&0
\end{array}                                                 \tag{37.30}
\]

All entries are computed as rational numbers; the decimals are display only.
The block also checks (37.4) for residue sets and the exact pointwise
Bonferroni identity (37.13).  These finite ratios are consistent with an
absolute-base moment bound but do not test \(m\asymp L^3/\log L\) and are
not asymptotic evidence.

**Assessment 37.5 (wave verdict).**  The residue-set correction and the
prime-side minorant are proved and reusable.  The proposed common-prime
\(D=1\) clique is not the obstruction.  Section 47 supersedes the original
status of the odd-Bonferroni continuation: its required bound (37.19) is
false for the only-prime-reduced count \(H\), although Proposition 37.3
remains a valid conditional implication for the void-equivalent
implication-antichain count.  Section 49 subsequently refutes its premise for
that count too.  The currently proved §31 input stops at total prime incidence
and loses the factor in (37.26).  Weighted block truncations by largest prime
merely redistribute (37.23); without (37.27) they do not control intersections
between blocks.  The Scott--Sokal cluster expansion controls a partition
function, not the required pointwise surrogate.  No LP dual certificate or
universal low-degree lower bound was found, so no impossibility claim for all
Lemma-33.3 minorants is made.  The residue-dispersion target (37.27) and a
genuinely one-sided, closure-aware polynomial remain possible routes; the
repaired hierarchy (47.16) is false.  Thus (33.16) and \(H_{\rm PF}'\) remain
open.  (wave-17 update)

## 38. Fixed-value binary actions: a complete additive law, a disconnected fibre graph, and the multiplier-conversion failure

*Section-number note.*  This clone ends at §35.  The present section is
numbered §38 because parallel Units X and Y are assigned §§36--37.

**Headline (strict quantifiers).**  **Theorem:** for the three common-modulus
additive maps, equations (38.3)--(38.4) below are necessary and sufficient
for the output value to equal either designated input value; the two
copied-coordinate maps can never preserve their *first* input, while every
unequal tuple has an auxiliary-source realization of the already-known
coordinate-swap involution.  **Computational, exact finite range:** among all
188,374 positive Type-II tuples with value at most 5,000, there are 203,906
designated value-fixing branches, but no hard-prime fibre is connected, even
when every auxiliary of value at most 5,000 is allowed; the smaller-auxiliary
graph is also disconnected on every hard-prime fibre.  **Computational,
exact search boxes:** the sparse-rational fixed-value search found only
identity and coordinate swap, and the affine/bilinear \(k=2\to k=1\) search
found no universal coordinate formula through \(P<10^5\).  Every statement
about a fibre is conditional on that fibre already being nonempty: none
constructs a tuple over a supplied prime, and none advances the P4
minimal-counterexample descent slot.

### 38.1 Exact value-fixing law

Put

\[
 R=CK,\qquad g=4R,\qquad T_R(a,b)=gab-a-b.                  \tag{38.1}
\]

Use two independently read source tuples

\[
 x=(a,b,R/k,k),\quad p=V(x)=T_R(a,b)/k,
 \qquad
 y=(u,v,R/\ell,\ell),\quad q=V(y)=T_R(u,v)/\ell.           \tag{38.2}
\]

Thus \(k\mid(R,a+b)\) and \(\ell\mid(R,u+v)\).  The three
coordinate outputs of (30.4) are

\[
 F_{++}=(a+u,b+v),\qquad F_{1+}=(a,b+v),\qquad
 F_{+1}=(a+u,b).
\]

For any one of these pairs \((A,B)\), an output reading is admissible
exactly when \(j\mid(R,A+B)\); the output is then
\((A,B,R/j,j)\).

**Theorem 38.1 (complete value-fixing characterization for the three
additive maps; proved).**  With the source and output divisibilities just
stated, the output has value \(p\), the value of the first input, exactly in
the corresponding line

\[
\begin{array}{c|l}
 \Phi_{++}&(j-k)p=\ell q+g(av+ub),\\
 \Phi_{1+}&(j-k)p=v(ga-1),\\
 \Phi_{+1}&(j-k)p=u(gb-1).
\end{array}                                                  \tag{38.3}
\]

It has value \(q\), the value of the second input, exactly in the
corresponding line

\[
\begin{array}{c|l}
 \Phi_{++}&jq=kp+\ell q+g(av+ub),\\
 \Phi_{1+}&jq=kp+v(ga-1),\\
 \Phi_{+1}&jq=kp+u(gb-1).
\end{array}                                                  \tag{38.4}
\]

No \(\Phi_{1+}\) or \(\Phi_{+1}\) branch fixes its first input.  A
\(\Phi_{++}\) branch which fixes the first input has \(j>k\); one fixing
the second has \(j>\ell\).

*Proof.*  The three exact numerator identities are

\[
\begin{aligned}
 T_R(a+u,b+v)&=kp+\ell q+g(av+ub),\\
 T_R(a,b+v)&=kp+v(ga-1),\\
 T_R(a+u,b)&=kp+u(gb-1).                                   \tag{38.5}
\end{aligned}
\]

Equating (38.5) to \(jp\) or \(jq\) gives (38.3)--(38.4), in
both directions; admissibility of \(j\) is exactly what makes the displayed
output a tuple.  For the copied-coordinate impossibility, put
\(D=ga-1\), \(E=gb-1\).  The source factorization gives

\[
 DE=1+gkp,
 \qquad (D,kp)=(E,kp)=1.                                   \tag{38.6}
\]

If the middle line of (38.3) held, then \(D\mid j-k\).  Its positive
right side forces \(j>k\), but \(j,k\mid R\) gives
\(0<j-k<R\), whereas \(D\geq4R-1>R\), a contradiction.  The
last line is identical with \(E\).  Positivity of the right side in the
first line of (38.3) gives \(j>k\); symmetry gives the final assertion. ∎

Equation (38.3) is the requested Diophantine law behind the 2,137 example:

\[
 (2,69,4,1)\ \mathop{\Phi_{++}}\ (1,22,4,1)
      =(3,91,2,2),
 \qquad (p,q,V_{\rm out})=(2137,329,2137).                 \tag{38.7}
\]

The auxiliary value is not determined by the fixed input, or even by the
fixed input and output.  For example

\[
 (1,5,8,1)\ \mathop{\Phi_{++}}\ (2,8,8/\ell,\ell)
       =(3,13,1,8),                                        \tag{38.8}
\]

where both \(\ell=1,2\) are valid.  The fixed and output values are 154,
while the same auxiliary coordinate pair has values 502 and 251.  In
general (38.3) sees \(\ell q=T_R(u,v)\), so every admissible reading of
\((u,v)\) changes \(q\) without changing the equation.

There is an auxiliary realization of an inverse, but it is precisely the
old trivial symmetry.

**Lemma 38.2 (the swap branch and its inverse; proved).**  Every tuple
\(y=(u,v,R/\ell,\ell)\) with \(u\ne v\) has a value-preserving binary
branch to \((v,u,R/\ell,\ell)\).  If \(u>v\), take the explicit auxiliary

\[
             (v,u-v,R,1)                                   \tag{38.9}
\]

as the first source of \(\Phi_{1+}\); if \(v>u\), take
\((v-u,u,R,1)\) as the first source of \(\Phi_{+1}\).  Applying the
opposite copied-coordinate map to the swapped tuple reverses the branch.

*Proof.*  In the first case the output coordinates are
\((v,(u-v)+v)=(v,u)\); in the second they are
\(((v-u)+u,u)=(v,u)\).  Read the output at the unchanged \(\ell\).  The
auxiliaries are positive members of the Type-II lattice, and swapping the
inequality gives the reverse formula. ∎

This is source-dependent and does not produce a new self-map beyond
\(A\leftrightarrow B\).  The original branch (38.7) has no direct inverse:
every possible reverse \(\Phi\)-output would have to increase at least one
of the coordinates of \((3,91)\), whereas \((2,69)\) decreases both.
More generally \(\Phi_{++}\) branches fixing their first input are acyclic
under the strictly increasing reading \(k<j\), although copied-coordinate
branches can create reversible edges such as Lemma 38.2.

### 38.2 Complete finite fibre graph through value 5,000

**Computational 38.3 (exact range and enumeration).**  The scan contains
*every* tuple with

\[
                    2\leq V(A,B,C,K)\leq5000.              \tag{38.10}
\]

Completeness uses \(AB\leq V/2\): enumerate
\(A\leq2500\), \(B\leq5000/(2A)\), every \(K\mid A+B\), and the exact
interval of \(C\) cut out by (38.10).  This gives 188,374 ordered tuples at
4,927 represented values.  Tuples are indexed by \((V,R)\), and equations
(38.3)--(38.4) recover the other source by coordinate subtraction; no
source-pair Cartesian product is formed.

A *designated branch* records which input value is fixed.  For
\(\Phi_{++}\), whose inputs commute, the fixed input is written first.  For
the copied-coordinate maps, Theorem 38.1 says that only the second input can
be fixed.  The exact counts are

\[
\begin{array}{c|r|r}
 \text{branch}&\text{auxiliary value}\leq5000
       &\text{auxiliary value}<\text{fixed value}\\ \hline
 \Phi_{++}&3822&3076\\
 \Phi_{1+}\text{ fixing input 2}&100042&78067\\
 \Phi_{+1}\text{ fixing input 2}&100042&78067\\ \hline
 \text{total}&203906&159210.
\end{array}                                                  \tag{38.11}
\]

Thus value-fixing is common only after the asymmetric, second-input reading
is included.  With all auxiliaries, 4,895 of the 4,927 represented values
have at least one branch; 83,357 tuples (44.25%) can be the designated fixed
input and 85,333 (45.30%) appear as a designated fixed input or as an
output (auxiliary-only roles are not counted here).  Only 187 value fibres
have every tuple as a designated fixed input.  With smaller auxiliaries the
corresponding numbers are 4,813 values, 65,462 tuples (34.75%), 68,218
participants (36.21%), and 34 all-input fibres.  In particular, neither
notion holds tuple-by-tuple on every fibre.

Make an undirected graph on \(V^{-1}(P)\) by forgetting a branch's direction.
Every edge preserves

\[
                            R=CK.                            \tag{38.12}
\]

This is an immediate obstruction to transitivity across different
\(R\)-sheets.  The all-auxiliary graph has 78,601 distinct edges.  Only 18
of 4,927 fibres are connected, and five of those are singleton fibres; the
smaller-auxiliary graph has 66,773 edges and only 13 connected fibres (five
singletons).  Selected complete fibre counts are:

\[
\begin{array}{r|r|r|rrr|rrr}
P&\#V^{-1}(P)&\#R&\#\mathrm{comp}&\max&\#\mathrm{iso}
 &\#\mathrm{comp}_{<}&\max_{<}&\#\mathrm{iso}_{<}\\ \hline
73&6&2&2&4&0&3&4&2\\
241&8&4&4&2&0&6&2&4\\
409&14&6&7&4&2&14&1&14\\
577&14&7&9&2&4&13&2&12\\
1753&36&15&20&6&10&21&6&12\\
1873&18&7&11&6&8&11&6&8\\
2137&32&13&17&6&8&18&6&10\\
2161&26&8&10&8&4&12&8&8\\
3049&22&9&15&4&12&16&4&14\\
4441&50&19&32&8&26&32&8&26\\
4993&42&18&27&6&18&27&6&18.
\end{array}                                                  \tag{38.13}
\]

Here the subscript \(<\) restricts the auxiliary to smaller value.  Among
all 76 hard primes through 5,000, every fibre has some bounded-auxiliary
branch and 75 have a smaller-auxiliary branch; 1,146 of their 1,938 tuples
can be fixed inputs.  Only 12 hard-prime fibres have every tuple as a fixed
input.  Under the smaller-source restriction those numbers are 936 tuples
and two fibres.  **No one of the 76 hard-prime fibre graphs is connected**:
each has at least two \(R\)-sheets.  Of 144,796 directed nonloop edges,
132,390 have a reverse edge somewhere in the family (103,990 of 118,768 in
the smaller-source graph), largely reflecting swap and related
copied-coordinate branches; this does not overcome (38.12).

These are exact finite graph statements, not evidence that a supplied prime
has a fibre.  Even a theorem saying every *nonempty* fibre is connected would
say nothing about fibre nonemptiness.  The actual result is weaker still:
transitivity is false in the complete tested range, both with bounded and
with smaller auxiliaries.

### 38.3 Sparse-rational fixed-value hunt and the Type-I scaling family

The unrestricted phrase ``degree-two rational map'' is too large to support
an honest exhaustive claim without fixing sparsity.  The following search
box is therefore stated exactly.

**Computational 38.4 (exact sparse-rational box; no nontrivial Type-II
map).**  For each of \(A',B',C',K'\), the numerator and denominator use one
or two atoms from

\[
 A,B,C,K,AB,CK,ABC,BCK,ACK,ABK,ABCK,1.                     \tag{38.14}
\]

Every retained coefficient is a nonzero integer in \([-3,3]\).  A common
sign is removed by requiring the denominator's first coefficient to be
positive.  There are 2,448 numerator polynomials, 1,224 denominator
polynomials, and hence 2,996,352 syntactic ratios per output coordinate.
The signature join tests the full Cartesian map box without materializing
its fourth power.

Every ratio was tested for positive integral output on all 118 complete
Type-II rows over

\[
 P\in\{73,241,409,577,1153,2137,2521,3049\}.               \tag{38.15}
\]

Only two coordinate signatures survive the full tuple join:

\[
 (A,B,C,K)\mapsto(A,B,C,K),
 \qquad (A,B,C,K)\mapsto(B,A,C,K).                          \tag{38.16}
\]

Both reduce identically modulo
\(4ABCK-A-B-KP=0\); the second is the factor-pair swap already audited in
§30.3.  Any universal map in the exact box would have passed the finite test,
so (38.16) exhausts that box.  This does **not** exhaust dense polynomials,
ratios with three or more atoms, larger coefficients, target-dependent
partial maps, or arbitrary birational automorphisms.

The analogous exact search on the Type-I side used the same 2,996,352
ratios per coordinate (with lower-case variables) and all 84 complete rows
at \(P=73,193,241,673,1129\), whose row counts are \(8,8,10,26,32\).
Again only identity and \(a\leftrightarrow b\) survive as maps defined on
every tested row.  There is nevertheless one genuine partial family outside
the ``defined everywhere'' conclusion.

**Lemma 38.5 (Type-I presentation scaling; proved).**  For every positive
rational \(t\),

\[
 S_t(a,b,c,k)=(ta,tb,c/t^2,tk)                              \tag{38.17}
\]

preserves the fixed value \(P\) in
\(P(a+b)=k(4abc-1)\).  It also preserves \(ck^2\) and both divisor factors
\(4ack-P,4bck-P\).  For integral \(t\), it is an integral map on the
subfamily \(t^2\mid c\), and \(S_{1/t}\) is its inverse on the image.

*Proof.*  Both sides of the Type-I equation acquire the same factor \(t\),
while
\((ta)(c/t^2)(tk)=ack\), and similarly for \(b\). ∎

This is exactly the nonprimitive-presentation scaling already implicit in
the canonical reduction: it leaves the Type-I factor pair unchanged.  It is
a partial groupoid, not a new action among divisor pairs and not a source of
new fixed-value solutions.  No matrix action changing the represented norm
or divisor grade survived the stated search.  General Type-I rational maps
mixing \((c,k)\), and dense Type-II rational maps, remain unclassified.

### 38.4 The \(k=2\to k=1\) law hunt

A universal conversion is already incompatible with the exact nine-prime
anatomy: 409, for example, has four \(k=2\) tuples up to the
\(A\leftrightarrow B\) swap (eight ordered) and no \(k=1\) tuple.
The finite law hunt asks the weaker diagnostic question whether a small
coordinate recipe works throughout the population where both kinds exist.

**Computational 38.6 (exact \(P<10^5\) feature box; no universal recipe).**
Among hard primes \(P<10^5\), exactly 1,175 have a \(k=1\) tuple, 1,120 have
a \(k=2\) tuple, and 1,114 have both.  The latter population contains
10,624 ordered \(k=2\) source rows.  Every source and every possible
\(k=1\) target was generated by the complete \(AB\leq P/2\) enumeration.

For each proposed target coordinate \(A',B',C'\), the searched expressions
are signed sums of one or two features from

\[
                1,a,b,c,ab,ac,bc,abc,                       \tag{38.18}
\]

with each nonzero coefficient in \([-3,3]\).  There are exactly

\[
             8\cdot6+\binom82 6^2=1056                     \tag{38.19}
\]

expressions.  Requiring one fixed expression to equal the corresponding
coordinate of *some* \(k=1\) target for every one of the 10,624 sources
leaves zero candidates for \(A'\), zero for \(B'\), and zero for \(C'\).
Thus no triple exists in this box.  The default `verify.py (ak)` replays the
same zero-candidate result on the 34 \(k=2\) rows at the ten both-kind hard
primes below 1,000; `ES_FULL_SCAN=1` regenerates the full counts above.
Dense feature combinations, rational expressions, piecewise recipes, and
recipes selecting a special \(k=2\) row are outside this exact failure log.

A hypothetical genuine map from **every** \(k=2\) tuple to a same-value
\(k=1\) tuple would imply

\[
 \{P:\text{no }k=1\text{ tuple}\}
       \subseteq\{P:\text{no }k=2\text{ tuple}\}.           \tag{38.20}
\]

It would not establish either set's emptiness.  In particular it would not
improve Theorem 32.4's \(\exp(-c\sqrt{\log N})\) exceptional-set bound
without a stronger, presently unavailable bound for \(k=2\)-lessness.  The
fixed-\(k=2\) condition is another exact moving-divisor condition, not a
proved easier existence problem.  In reality the universal premise is
already refuted by the finite \(k=1\)-less examples, so (38.20) is only the
precise counterfactual implication.

### 38.5 P4 and existence assessment

**Assessment 38.7.**  The fixed-value hunt changes the §30.3 audit in one
limited way: binary addition has many fixed-value instances, and the
copied-coordinate maps realize the swap involution with an explicit
auxiliary.  It does not supply the missing Markoff-like structure.  The
graph preserves \(CK\), is nontransitive on every tested hard-prime fibre,
and its only proved everywhere-available inverse is the old coordinate
swap.  The original 2,137 edge has no direct one-branch reverse (a
multi-step directed reversal through other fibre members can exist, e.g.
\((3,91,2,2)\to(1,285,2,2)\to(2,69,4,1)\) via auxiliaries
\((1,194,4,1)\) and \((1,69,4,1)\)).  Type-I scaling merely
changes a nonprimitive presentation, while the multiplier-conversion search
is negative and a universal conversion is finitely impossible.

Most importantly, every construction starts with a tuple on the target
fibre.  Inverting a branch at that tuple is witness decomposition, not
witness existence (§23's circularity register).  None takes a bare prime
\(P\), a mixed valuation shape over \(P^2\), or an induction-supplied
solution at a smaller denominator and produces the first tuple over \(P\).
Consequently the P4 ``cleverer transfer'' slot of §17.7 remains open, with no
new candidate from this wave; no Erdős--Straus proof results.

**Verification companion.**  `verify.py (ak)` regenerates (38.10)--(38.13)
without a source Cartesian product, checks every finite branch against
(38.3)--(38.4), replays (38.7), verifies the swap construction and directed
inverse counts, checks the Type-I scaling example and the coordinate-ring
identity/swap, and reruns the bounded \(k=2\to k=1\) feature search.

---

## 39. The c-free critical-window assembly: a provisional cubic-rate majorant

This section attacks the restricted assembly in §34.4.  It does **not**
prove the literal coefficient-sum clause of
\(H_{\rm PF}'(k\ell;{\rm good})\).  Instead it removes the moving
\(c\)-family, uses one fixed unpruned atom family, and proves the weaker
ledger \(\exp\{O(J\log X)\}\).  That ledger is exactly of the same order
as the lcm budget and is still absorbed when \(\log N\geq C(\log X)^4\).
Subject to the maximum-severity caveats in §39.7, this closes the
exceptional-set implication and gives a **CLAIMED/PROVISIONAL** unconditional
\(3/4\) exponent.  All results in this section which feed that claim inherit
that provisional status pending hostile external checking.

Put
\[
 t=\log X,\qquad K=\lfloor X^\kappa\rfloor,
 \qquad H=K^{10},\qquad 0<\kappa<1/240,                    \tag{39.1}
\]
and partition \((X^{1/2},X]\) into disjoint dyadic blocks \((x,2x]\)
(truncating the two endpoint blocks).  In a block put \(z=x^{1/6}\).
Let \(\mathcal A_X\) be the following fixed **c-free** family.  An atom is
\[
 A=(k,\ell,u,v),\quad k\leq K,\ k\equiv1\pmod4,
 \quad \ell\in(x,2x]\text{ prime},\quad
 H<u,v\leq z,                                               \tag{39.2}
\]
with
\[
 (u,v)=(uv,k)=1,\
 \omega(uv)\leq D\log\log X,
 \qquad 4uv\mid k\ell+1.                                  \tag{39.3}
\]
It denotes the cylinder
\[
 E_A=\{n:n\equiv-u v^{-1}\pmod {k\ell}\}.                \tag{39.4}
\]
Here \(D\) is the fixed constant of Lemma 16.2.  The dyadic cutoff is only
a canonical subfamily of (16.7); inspection of the lower proof of Theorem
34.8, specifically (34.20)--(34.21), shows that its retained main mass is
already furnished inside these boxes.

### 39.1 Removing the moving fibre and deduplicating the atoms

**Lemma 39.1 (c-free reduction and distinct large coordinates; proved,
provisionally checked).**

1. If \(n\) is exceptional, then it avoids every atom in \(\mathcal A_X\).
   If additionally \(c\equiv n\pmod {24L_K}\), then every atom hit by \(n\)
   automatically obeys \(k\mid u+cv\).  Thus the coupling condition used to
   define \(\mathscr G_{X,c}\) is implied by the atom itself; it need not be
   built into the polynomial.
2. Distinct atoms which have a compatible intersection have distinct primes
   \(\ell\).  At a fixed \(\ell\), all atom classes modulo \(\ell\) are
   distinct.  At a fixed modulus \(k\ell\), no two ordered pairs \((u,v)\)
   produce the same class.
3. Consequently, for a compatible ordered set \(A_1,\ldots,A_j\),
   \[
    \Pr\Big(\bigcap_{i\leq j}E_{A_i}\Big)
     ={\mathbf1_{\rm compatible}\over
       \operatorname {lcm}(k_1,\ldots,k_j)\prod_{i\leq j}\ell_i}.
                                                                    \tag{39.5}
   \]

*Proof.*  Lemma 16.1 proves the first assertion.  Modulo \(k\), (39.4) says
\(u+nv\equiv0\); since \(c\equiv n\pmod k\), it also says
\(u+cv\equiv0\).

Suppose two atoms at the same \(\ell\) are compatible.  Their projections
modulo \(\ell\) agree, so
\[
 \ell\mid uv'-u'v.
\]
In the same block the absolute value is at most \(z^2=x^{1/3}<\ell\).
The same conclusion holds if two admissible cutoffs are compared across
blocks, since every \(u,v\leq X^{1/6}\), while
\(\ell>X^{1/2}>X^{1/3}\).  Hence \(uv'=u'v\), and reducedness gives
\((u,v)=(u',v')\).  (The apparent swap can agree only when \(u=v\), which
is impossible here because \((u,v)=1\) and \(u,v>H\).)  Finally
\(uv\mid(k\ell+1)/4\) is exactly
\[
 k\ell\equiv-1\pmod {4uv}.
\]
Since \((\ell,4uv)=1\), this determines \(k\pmod {4uv}\), and
\(4uv>4H^2>K\) makes the admissible \(k\) unique.  This proves both forms
of deduplication and the distinct-\(\ell\) assertion.  CRT now gives
(39.5). \(\square\)

The point of this lemma is logical as well as geometric.  The new majorant
below covers the fixed predicate
\(\mathbf1_{(n,P_y)=1}\mathbf1_{H_X(n)=0}\), where
\(H_X=\sum_{A\in\mathcal A_X}\mathbf1_{E_A}\).  It does not majorize every
avoider of the smaller, \(c\)-dependently pruned family in (34.24).  It does
majorize every exceptional prime, which is all the implication (34.25)
needs.

### 39.2 Exact mass profiles

For \(g\mid k\) and \(a\in(\mathbb Z/g\mathbb Z)^\times\), write
\[
 W_{k,a}(g)=
  \sum_{\substack{A\in\mathcal A_X\text{ with multiplier }k\\
                   -uv^{-1}\equiv a\ (g)}}{1\over k\ell},
 \qquad W_k=\sum_{A:k_A=k}{1\over k\ell}.                  \tag{39.6}
\]

**Lemma 39.2 (multiplier and residue profiles; proved, provisional).**
Uniformly for \(k\leq K\), \(k\equiv1\pmod4\), \(g\mid k\), and reduced
\(a\pmod g\),
\[
 W_{k,a}(g)\ll {t^2\over\varphi(g)}{\varphi(k)^2\over k^3},
 \qquad
 W_k\asymp t^2{\varphi(k)^2\over k^3}.                    \tag{39.7}
\]
Consequently
\[
 \mu_X:=\sum_{A\in\mathcal A_X}{1\over k_A\ell_A}
   \asymp t^2\sum_{\substack{k\leq K\\k\equiv1(4)}}
                   {\varphi(k)^2\over k^3}
   \asymp t^2\log K\asymp t^3.                            \tag{39.8}
\]
For each fixed odd prime \(p\), the share of the proxy Euler weight
\(b(k)/k=\varphi(k)^2/k^3\) carried by multipliers divisible by \(p\) is
exactly
\[
 \alpha_p={p-1\over p^2+p-1}\sim {1\over p}.              \tag{39.9}
\]
(Because (39.7) determines \(W_k\) only up to constants, (39.9) is a
statement about the proxy weight, not an exact share of the atom mass; the
moment proof below never uses \(\alpha_p\).)

*Proof.*  Here are the details which are needed later, rather than an appeal
to an average over \(c\).  (This derivation was rewritten in review; the
original appeal to “repeating (16.4)” did not carry the extra exclusions.)
Fix the block and \(k\), and put \(F(n)=n/\varphi(n)\),
\[
 q_0=\operatorname {lcm}(g,\operatorname {rad}k)\leq k.
\]
Work in multiplicative boxes \(u\asymp U\), \(v\asymp V\).  The
conditions \((uv,k)=1\) and \(-uv^{-1}\equiv a\pmod g\) restrict
\((u\bmod q_0,v\bmod q_0)\) to reduced pairs with a fixed ratio modulo
\(g\): for each of the \(\varphi(q_0)\) choices of \(v\)-class, the
\(u\)-class is determined modulo \(g\) and free at the remaining part, so
exactly \(\varphi(q_0)^2/\varphi(g)\) ordered class pairs are compatible.
Shiu's theorem for the multiplicative function \(F\), on the
fixed-relative-length interval \(u\asymp U\) in one reduced class modulo
\(q_0\) (applicable since \(q_0\leq k\leq K\) and \(U>H=K^{10}\)), gives
\[
 \sum_{u\asymp U,\ u\equiv r\ (q_0)}F(u)
 \ll {U\over\varphi(q_0)}
 \exp\Big\{-\sum_{p\mid k}{1\over p-1}\Big\}
 \asymp {U\over\varphi(q_0)}\,{\varphi(k)\over k},
\]
the last step because the logarithm of the quotient is
\(O(\sum_pp^{-2})\).  Multiplying the \(u\)- and \(v\)-class sums by the
number of compatible class pairs and dividing by \(UV\) yields, per box
pair,
\[
 \sum_{\rm box}{1\over\varphi(u)\varphi(v)}
 \ll {1\over\varphi(g)}\Big({\varphi(k)\over k}\Big)^2,
\]
and summing the \(O((\log(z/H))^2)=O(t^2)\) box pairs gives
\[
 \sum {1\over\varphi(u)\varphi(v)}
 \ll { (\log z)^2\over\varphi(g)}{\varphi(k)^2\over k^2}. \tag{39.11}
\]
For fixed \((u,v)\), Brun--Titchmarsh in the progression
\(\ell\equiv-k^{-1}\pmod {4uv}\) (modulus \(4uv\leq4x^{1/3}\), so the
logarithm in the denominator is \(\asymp\log x\)) gives
\[
 \sum_{x<\ell\leq2x,\ \ell\equiv-k^{-1}(4uv)}{1\over\ell}
 \ll {1\over\varphi(4uv)\log x},
 \qquad
 {1\over\varphi(4uv)}\ll{1\over\varphi(u)\varphi(v)}
\]
(the last since \((u,v)=1\)).  Combining with (39.11) over the boxes
proves
\[
 \sum_{A\text{ in the block}\atop k_A=k,
       -uv^{-1}\equiv a\ (g)}{1\over\ell}
 \ll {\log x\over\varphi(g)}{\varphi(k)^2\over k^2},      \tag{39.10}
\]
with an absolute constant, uniformly in \(k\leq K\), \(g\mid k\), and
reduced \(a\): no \(k^\varepsilon\), divisor, or logarithmic loss enters.
After the \(O(t)\) blocks and division by \(k\), this is the upper half of
(39.7).

For the lower half drop the ratio condition.  For one fixed \(k\), a
modulus \(4uv\) has at most \(2^{\omega(uv)}=(\log X)^{O(1)}\) ordered
allocations.  Thus ordinary Bombieri--Vinogradov, with a fixed sufficiently
large logarithmic saving, evaluates the prime progressions without the
factor \(K\): \(k\) is fixed on this line.  The low-\(\omega\) Rankin
argument of (16.5h) retains a fixed proportion uniformly.  (At a prime
\(p\mid k\) the exact coprime-pair local factor differs from
\((1-1/p)^2\) by \(1+O(p^{-2})\), so the unrestricted harmonic pair mass
is \(\asymp(\log(z/H))^2(\varphi(k)/k)^2\) uniformly.)  This gives the
matching lower bound block by block and proves (39.7).

Finally \(b(k)=(\varphi(k)/k)^2\) is multiplicative and
\(\sum b(k)/k\asymp\log K\), also after selecting \(k\equiv1\pmod4\), by
the principal/\(\chi_4\) decomposition.  At an odd prime its local factor is
\[
 1+\sum_{e\geq1}{(1-1/p)^2\over p^e}
   =1+{p-1\over p^2},                                      \tag{39.12}
\]
so the part with \(p\mid k\), divided by the full factor, is exactly
(39.9). \(\square\)

The distinction between the two masses is worth recording.  Given a reduced
fibre \(c\), an atom with multiplier \(k\) is active for one of the
\(\varphi(k)\) unit residues and then has prime-coordinate probability
\(1/\ell\).  Averaging those conditional masses produces the factor
\(1/\varphi(k)\), whereas the unconditioned cylinder has probability
\(1/(k\ell)\).  Formula (39.7), not (34.23), is therefore the correct
profile for factorial moments in the c-free CRT space.

### 39.3 Collapse versus consistency

The rough collapse bound which discards residue consistency would charge a
shared prime \(p\) by \(p\alpha_p^2\asymp1/p\), producing a false
\(\log\log K\) loss.  The required cancellation is exact at the level of a
new compatible atom.

For a cutoff \(y\), put
\[
 q_y(k)=\prod_{p\mid k,\ p\leq y}{p\over p-1},
 \qquad
 b_y(g)=\prod_{p^e\Vert g,\ p\leq y}\varphi(p^e)
         \prod_{p^e\Vert g,\ p>y}p^e.                     \tag{39.13}
\]
Condition the CRT space by \((n,P_y)=1\), where
\(P_y=\prod_{p\leq y}p\).  An atom then has probability
\(q_y(k)/(k\ell)\).  If a compatible previously selected set has
multiplier lcm \(R\), adding an atom of multiplier \(k\), with
\(g=(k,R)\), multiplies its intersection probability by
\[
 {q_y(k)\over k\ell}\,b_y(g).                              \tag{39.14}
\]
Compatibility fixes one unit residue modulo \(g\).  Lemma 39.2 says that
the atom mass in that residue is at most \(1/\varphi(g)\) of its
multiplier mass.  Thus the collapse left after summing the compatible new
atoms is
\[
 {b_y(g)\over\varphi(g)}
   =\prod_{p\mid g,\ p>y}{p\over p-1};                     \tag{39.15}
\]
small conditioned primes cancel exactly, and an unconditioned shared prime
costs only \(p/(p-1)\), not \(p\).

**Lemma 39.3 (uniform multiplier Euler bound; proved).**  Uniformly in
\(y\geq2\), every integer \(R\), and \(K\geq3\),
\[
 \sum_{\substack{k\leq K\\k\equiv1(4)}}
 {\varphi(k)^2\over k^3}q_y(k)
 \prod_{\substack{p\mid(k,R)\\p>y}}{p\over p-1}
 \ll\log K.                                                \tag{39.16}
\]

*Proof.*  It is enough to sum over all odd \(k\).  The unmodified local
nonconstant mass is \((p-1)/p^2\).  Multiplication either by \(q_y\) for
\(p\leq y\), or by \(p/(p-1)\) when \(p>y\) and \(p\mid R\), changes this
to \(1/p\).  The quotient
\[
 {1+1/p\over1+(p-1)/p^2}=1+O(p^{-2})                      \tag{39.17}
\]
has a convergent product, uniformly in the chosen set of modified primes.
The remaining harmonic Euler product is \(O(\log K)\). \(\square\)

**Theorem 39.4 (all required upper factorial moments; proved,
provisional).**  In the CRT space conditioned by \((n,P_y)=1\), for every
integer \(m\geq1\),
\[
 \mathbb E(H_X)_m\leq(Ct^3)^m,                             \tag{39.18}
\]
with \(C\) depending at most on \(\kappa\), uniformly in
\(2\leq y<X^{1/2}\).  (The upper restriction is necessary: for
\(y\geq\ell\) the coprimality conditioning would renormalize the
\(\ell\)-coordinate itself by \(\ell/(\ell-1)\), which (39.14) does not
include.  The application (39.21) has \(y=Bt^3<X^{1/2}\) for all large
\(X\).)  In particular the bound holds through every order
\(m=D_Bt^3\).

*Proof.*  Expand the ordered factorial moment into distinct compatible
atoms.  By Lemma 39.1, every admissible next atom has a new \(\ell\).
For a fixed preceding compatible set, (39.14), the residue-profile upper
bound (39.7), and (39.15) bound the sum over all possible next atoms by
\[
 Ct^2\sum_{k\leq K\atop k\equiv1(4)}
 {\varphi(k)^2\over k^3}q_y(k)
 \prod_{p\mid(k,R),\ p>y}{p\over p-1}
 \leq Ct^2\log K\leq Ct^3.                               \tag{39.19}
\]
Removing the forbidden old \(\ell\)'s only decreases this sum.  Iteration
proves (39.18). \(\square\)

At pair level this gives a sharper diagnosis than the rough attempt in the
attack brief.  For fixed \(k,k'\), \(g=(k,k')\),
\[
 \sum_{A:k_A=k}\sum_{B:k_B=k'\atop A\sim B}
 \Pr(E_A\cap E_B)
 \ll {g\over\varphi(g)}W_kW_{k'}.                          \tag{39.20}
\]
Averaging (39.20) uses
\(\alpha_p^2(p/(p-1)-1)=O(p^{-3})\), not
\(p\alpha_p^2\asymp1/p\).  Hence the pair excess is \(O(\mu_X^2)\) with
an absolute constant.  It is **not** \(o(\mu_X)\): a fixed small prime
already contributes a constant multiple of \(\mu_X^2\) to the usual
Janson dependency sum.  Therefore the proposed direct condition
\(\Delta=o(\mu)\) and the naive Janson proof fail quantitatively.  The
factorial-moment theorem survives because an absolute base \(C^m\), rather
than Poisson relative error, is enough after the separate void estimate
below.

### 39.4 The CRT void without partitioning by all of \(M_0\)

A completely unconditioned c-free void still has a quarantine floor: taking
\(n\equiv0\pmod p\) for many small \(p\)'s disables every atom whose
multiplier contains one of them.  Thus \(Q_r(H_X)\) alone cannot have cubic
mean.  The cure costs low degree.  Take
\[
 y=B t^3                                                     \tag{39.21}
\]
with a sufficiently large fixed \(B\), and multiply by the exact small-prime
coprimality selector
\[
 S_y(n)=\mathbf1_{(n,P_y)=1}
       =\sum_{d\mid P_y}\mu(d)\mathbf1_{d\mid n}.          \tag{39.22}
\]
Every exceptional prime greater than \(y\) has \(S_y=1\).  Notice that
(39.22) has degree \(\pi(y)=O(t^3/\log t)\), not the impossible degree
\(\pi(K)\).

**Lemma 39.5 (conditioned c-free void; proved, provisional).**  In the exact
CRT space,
\[
 \Pr(H_X=0\mid S_y=1)\leq e^{-c t^3}.                       \tag{39.23}
\]

*Proof.*  Reveal all multiplier coordinates.  Let \(c\) denote the resulting
class modulo \(24L_K\), \(L_K=\operatorname {lcm}\{k\leq K:k\equiv1\ (4)\}\),
and put
\[
 \mathcal J_c=\{k\leq K:k\equiv1\pmod4,\ (k,c)=1\},
 \qquad
 Z(c)=\sum_{y<p\leq K,\ p\mid L_K\atop p\mid c}{1\over p}.             \tag{39.24}
\]
(The restriction \(p\mid L_K\) makes \(Z\) well defined: a prime
\(p\equiv3\ (4)\) with \(3p>K\) divides no admissible multiplier, so it
has no CRT coordinate here and can be omitted — it removes nothing from
\(\mathcal J_c\).)  The coordinates for \(p>y\), \(p\mid L_K\), remain
independent and \(\Pr(p\mid c)=1/p\).  With the exponential parameter \(y\),
\[
 \mathbb E e^{yZ}
 \leq\exp\left\{C y\sum_{p>y}p^{-2}\right\}=e^{O(1)},
 \qquad
 \Pr(Z>\eta)\leq e^{-\eta y+O(1)}.                         \tag{39.25}
\]

Write \(h(\mathcal J)=\sum_{k\in\mathcal J}\varphi(k)/k^2\).
The elementary bounds
\[
 h(\mathcal K(K))\asymp\log K,
 \qquad
 \sum_{k\leq K,\ p\mid k}{\varphi(k)\over k^2}
       \ll {\log K\over p}                                 \tag{39.26}
\]
show by the union bound that, for a sufficiently small fixed \(\eta\),
\(Z(c)\leq\eta\) implies
\(h(\mathcal J_c)\geq c_1\log K\).  Also \(S_y=1\) makes \(c\) coprime
to 24, and by definition it is coprime to \(L_{\mathcal J_c}\).

Apply Theorem 34.8 to this arbitrary subfamily \(\mathcal J_c\).  Its lower
proof lies in the canonical boxes (39.2), and its good triples are contained
in the c-free unpruned family.  Conditional on the multiplier coordinates,
the distinct \(\ell\)-coordinates are independent by Lemma 39.1.  Therefore,
when \(Z(c)\leq\eta\),
\[
 \Pr(H_X=0\mid c)
 \leq\prod_\ell\left(1-{f^{\rm good}_c(\ell)\over\ell}\right)
 \leq\exp\{-c_2t^2h(\mathcal J_c)\}
 \leq e^{-c_3t^3}.                                         \tag{39.27}
\]
The bad multiplier coordinates cost at most
\(e^{-\eta Bt^3+O(1)}\) by (39.25).  Increasing \(B\) if necessary and
averaging (39.27) proves (39.23). \(\square\)

This is where Theorem 34.8 replaces Janson.  It supplies cubic active
prime-coordinate mass **uniformly for every reduced surviving multiplier
fibre**.  The only fibres not reduced are those which set too much
large-prime multiplier mass to zero, and (39.25) makes those fibres
exponentially rare after the polynomial-sized coprimality cutoff.

### 39.5 A low-degree majorant with the honest ledger

For even \(r\), put
\[
 Q_r(h)=\sum_{j=0}^r(-1)^j{h\choose j}.
\]
The exact identity
\[
 Q_r(0)=1,
 \qquad Q_r(h)={h-1\choose r}\geq0\quad(h\geq1)             \tag{39.28}
\]
shows that
\[
 \nu_{X}(n)=S_y(n)Q_r(H_X(n))                               \tag{39.29}
\]
is nonnegative and is at least one on every exceptional prime
\(n>\max(K,y)\).

**Theorem 39.6 (modified c-free critical-window assembly; proved,
CLAIMED/PROVISIONAL).**  There are constants \(c,C_0,D_B>0\), depending at
most on \(\kappa\), such that if \(r\) is the least even integer at least
\(D_Bt^3\), then (39.29) has exact CRT mean (here and below \(D_B\) is the
Bonferroni-degree constant, distinct from Lemma 16.2's \(\omega\)-cutoff
constant \(D\) in (39.3))
\[
 \mathbb E_{\rm CRT}\nu_X\leq e^{-ct^3}.                   \tag{39.30}
\]
Its congruence expansion has the following explicit bounds:
\[
 \begin{split}
 \text{degree}&\leq r+\pi(y)=O(t^3),\\
 \log d_{\rm term}&\leq O(y)+r(t+\log K)=O(t^4),\\
 \log\sum_{\rm terms}|c_{\rm term}|&=O(rt)=O(t^4).
 \end{split}                                                \tag{39.31}
\]
Every nonzero term is one plain congruence class.
Consequently, whenever \(\log N\geq C_0t^4\),
\[
 \sum_{n\leq N}\nu_X(n)\ll Ne^{-ct^3}.                    \tag{39.32}
\]

*Proof.*  From (39.28), for \(h\geq1\),
\({h-1\choose r}\leq {h\choose r+1}\).  Lemma 39.5 and Theorem
39.4 therefore give
\[
 \begin{split}
 \mathbb E(Q_r(H_X)\mid S_y=1)
 &\leq \Pr(H_X=0\mid S_y=1)
       +{\mathbb E((H_X)_{r+1}\mid S_y=1)\over(r+1)!}\\
 &\leq e^{-c_1t^3}+{(Ct^3)^{r+1}\over(r+1)!}
 \leq e^{-ct^3},                                           \tag{39.33}
 \end{split}
\]
when \(D_B\) is sufficiently large.  Multiplication by
\(\Pr(S_y=1)\leq1\) proves (39.30).

Expand (39.22) and the elementary symmetric polynomials in \(Q_r\).
Lemma 39.1 makes every compatible atom set use distinct \(\ell\)'s; CRT
then makes its further intersection with \(d\mid P_y\) either empty or one
class.  If \(A_X=|\mathcal A_X|\), the crude choice count from (39.2) gives
\(\log A_X=O(t)\), and hence
\[
 2^{\pi(y)}\sum_{j\leq r}{A_X\choose j}=\exp\{O(rt)\}.     \tag{39.34}
\]
The modulus is at most \(P_y(KX)^r\), proving (39.31).  On \([1,N]\),
each class count is its CRT mean times \(N\), plus \(O(1)\).  Choosing
\(C_0\) larger than the constants in (39.31) makes the aggregate rounding
error \(\exp\{O(rt)\}\) at most, say, \(N^{1/2}\), which is negligible
beside \(Ne^{-ct^3}\).  This proves (39.32). \(\square\)

The literal hypothesis (34.24) demanded coefficient sum \(e^{O(J)}\), with
\(J\asymp t^3\), and a majorant for its larger aggregate avoider predicate.
Theorem 39.6 proves neither clause: its direct Bonferroni expansion has
ledger \(e^{O(Jt)}\), and it only covers the c-free avoider (hence all
exceptional primes).  These are deliberate modifications, not suppressed
losses.  The ledger still closes because the critical window itself has
logarithmic size \(\asymp Jt\).  Thus the exact surviving hypothesis from
§34.4 is still open as stated, but is no longer needed for the exceptional
set if Theorem 39.6 survives review.

### 39.6 Exceptional denominators

**Theorem 39.7 (unconditional \(3/4\) exceptional-set bound;
CLAIMED/PROVISIONAL).**  There is a constant \(c>0\) such that
\[
 E_{\rm all}(N)\ll N\exp\{-c(\log N)^{3/4}\}.              \tag{39.35}
\]
The same bound holds for exceptional primes.

*Proof.*  Put \(L=\log N\), take \(t=\alpha L^{1/4}\), and set
\(X=e^t\).  Choose the fixed \(\alpha>0\) small enough that
\(L\geq C_0t^4\).  Lemma 39.1 and (39.29) majorize every exceptional prime
larger than \(\max(K,y)\); that omitted range is negligible.  Equations
(39.32) and \(t^3=\alpha^3L^{3/4}\) give the prime bound.  The semigroup
argument of Theorem 16.5, with
\(g(u)=u^{3/4}\), transfers the same logarithmic power from exceptional
primes to all exceptional denominators. \(\square\)

This is a record-class assertion and remains **CLAIMED/PROVISIONAL**.  No
claim of publication priority is made.  The proof uses only the already
provisional Theorem 34.8 plus the new arguments above; it does not use
\(H_{k\rm BV}\), \(H_{\rm PF}'\), or an Elliott--Halberstam hypothesis.

### 39.7 Maximum-severity review and exact status

**Self-review (three weakest steps).**

1. The new residue-resolved upper bound (39.11) must be rederived by a referee
   with every local factor present.  It needs simultaneous uniformity in
   \(k\leq X^\kappa\), every divisor \(g\mid k\), and every unit residue;
   the proof uses Brun--Titchmarsh for the upper bound, so it does not hide a
   polynomially small Bombieri--Vinogradov main term.  This is the most
   load-bearing new analytic lemma.
2. Lemma 39.5 uses Theorem 34.8 for the data-dependent subfamily
   \(\mathcal J_c\) and uses the canonical lower boxes, not merely the larger
   family in the statement of (34.18).  The quantifiers of Theorem 34.8 do
   allow every subfamily containing 1, and its proof furnishes the lower mass
   in those boxes, but this inheritance is new and needs an independent
   line-by-line check together with Theorem 34.8 itself.
3. The ordered-moment induction (39.14)--(39.19) is where lcm collapse and
   residue consistency cancel at every prime power.  A missed factor there
   would be exponentiated through \(r\asymp t^3\).  The displayed conditional
   factor is \(\varphi(p^e)\) for \(p\leq y\) and \(p^e\) for \(p>y\);
   after the \(1/\varphi(g)\) residue share, only \(p/(p-1)\) remains at an
   unconditioned shared prime.  This exact replay, including unequal
   prime-power exponents, is mandatory in external review.

**Assessment 39.8 (status).**  Internally, the quantifier chain is complete:
Theorem 34.8 is uniform in \(\mathcal J_c\); (39.25) removes the nonreduced
fibres; (39.18) controls the even Bonferroni tail; and (39.31)--(39.34) pay
the full \(e^{O(t^4)}\) coefficient ledger before selecting
\(t=\alpha(\log N)^{1/4}\).  The direct Janson proposal is rejected because
its dependency sum is \(\Theta(\mu^2)\), while the original
\(e^{O(J)}\) formulation remains open.  Theorem 39.7 should not be cited as
established outside this campaign until an independent expert has checked
the three steps above and the priority claim against the primary literature.

**Priority-search note (2026-08-29, appended after review).**  A fresh web
search (Jina) found no post-1970 improvement of Vaughan's
\(N/\exp(c(\log N)^{2/3})\) for the \(4/n\) exceptional set: the
Pomerance--Weingartner 2025 preprint (arXiv:2511.16817, = \,
`sources/pomerance-weingartner-2025.pdf`) explicitly cites Vaughan 1970 as
the state of the art (“strongly improved, though not recently”), and its
own Theorem for general \(m\) reproduces the \(1/3\)-power of
\((\log^2N/\varphi(m))\), i.e.\ the same \(2/3\) exponent at \(m=4\).
OEIS A192787 and the Wikipedia article likewise cite only Vaughan.  If
Theorem 39.7 survives external review it would therefore be the first
exponent improvement since 1970.  This is a search result, not a
literature guarantee; the CLAIMED/PROVISIONAL label stands.

**Computational 39.9 (finite companion only).**  `verify.py (al)` uses the
toy exponent \(\kappa_{\rm toy}=1/4\) and floor \(H_{\rm toy}=1\), because
the genuine \(\kappa<1/240\), \(H=K^{10}\) regime has no nontrivial small
instance.  Its atom family is an enlarged structural toy: it uses the
per-prime cutoff \(u,v\leq\ell^{1/3}\) in place of (39.2)'s dyadic-block
cutoff \(u,v\leq x^{1/6}\) (which is empty at toy scale), so it tests the
divisibility/coupling/deduplication structure of (39.2)--(39.4), not the
literal cutoffs.  It enumerates these atoms,
tests the c-coupling, deduplication, and distinct-\(\ell\) compatibility,
and computes exact \(e_j\), \(\mu^j/j!\), and the dependent-pair
\(\Delta\) for \(j\leq4\).  The table is a structural regression only; it
makes no asymptotic claim.
## 40. Residue dispersion: the regular progression tail closes, and the short-cofactor endpoint remains

Put
\[
 L=\log X,\qquad
 z={L^3\log\log L\over\log L},\qquad
 \Lambda={L^3\over\log L},
\]
and retain the notation of §37.  The labels in this section are strict.
The exact divisor/character reformulations and the regular-tail estimate are
**proved**.  The endpoint estimate (40.19), hence (37.27), is **OPEN**.
No theorem about the critical-window avoiders or \(H_{\rm PF}'\) is obtained.

### 40.1 Exact deduplicated divisor variance

For a composite, \(z\)-rough \(M\leq X\), \(M\equiv3\pmod4\), choose
one divisor representative for each distinct intrinsic class: let
\(\mathcal D(M)\) contain the least positive \(D\mid((M+1)/4)^2\) in
each fibre of
\[
                         D\longmapsto-4D\pmod M.             \tag{40.1}
\]
Delete from this set a representative when its class is implied by a
prime-modulus atom as in §37.3, and call the remaining set
\(\mathcal D^\circ(M)\).  The deletion is well defined on a fibre, since
all representatives in that fibre have the same projection modulo every
prime dividing \(M\).  This choice is bookkeeping, not a claim that all
divisors in Lemma 18.1 give distinct classes.

Let \(Y\) be the cutoff in (37.7), put \(f(q)=F(q)\) for primes
\(q\equiv3\pmod4\), and define
\[
 \kappa(M)=
 \prod_{\substack{q\mid M,\ z<q\leq Y\\q\equiv3(4)}}
                    {q\over q-f(q)}.                         \tag{40.2}
\]
Multiplication by \(P_z^{-1}\) merely dilates every residue by a unit, so
it does not change equality of two projections at a prime.  Conditional on
\(T_0=1\), every retained atom represented by \(D\in
\mathcal D^\circ(M)\) therefore has the **exact** marginal
\[
                              w_{M,D}={\kappa(M)\over M}.     \tag{40.3}
\]
For \(p\mid M\), set
\[
 n_{M,p}(a)=\#\{D\in\mathcal D^\circ(M):-4D\equiv a\pmod p\}.
                                                                    \tag{40.4}
\]

**Proposition 40.1 (exact variance identities; proved).**  The quantity on
the left of (37.27) is exactly
\[
 \begin{split}
 \mathcal V_X
 &=\sum_{z<p\leq X}p\sum_{a\bmod p}
   \left(\sum_{\substack{M\leq X,\ M\ {\rm composite},\ P^-(M)>z\\
                         M\equiv3(4),\ p\mid M}}
       {\kappa(M)\over M}n_{M,p}(a)\right)^2                 \tag{40.5}\\
 &=\sum_{z<p\leq X}p
   \sum_{\substack{M,N\ {\rm as\ above}\\p\mid(M,N)}}
   {\kappa(M)\kappa(N)\over MN}\,C_p(M,N),                 \tag{40.6}
 \end{split}
\]
where
\[
 C_p(M,N)=\#\{(D,E)\in\mathcal D^\circ(M)\times
             \mathcal D^\circ(N):D\equiv E\pmod p\}.       \tag{40.7}
\]
Writing \(M=p^e m,N=p^{e'}m'\), with \(p\nmid mm'\), changes the
coefficient in (40.6) to
\[
 {\kappa(p^em)\kappa(p^{e'}m')\over
   p^{e+e'-1}mm'}C_p(p^em,p^{e'}m').                         \tag{40.8}
\]
Thus the \(1/(pmm')\) expression in the squarefree
\(e=e'=1\) sketch is correct, but it is not the complete system: prime
powers and intrinsic-class deduplication must be retained.  In particular,
\(D=E\) is possible with \(M\ne N\).

If \(e_p(x)=e^{2\pi i x/p}\), then (40.5) also equals
\[
 \sum_{z<p\leq X}\sum_{h\bmod p}
 \left|\sum_{\substack{M\ {\rm as\ in}\ (40.5)\\p\mid M}}
 {\kappa(M)\over M}
 \sum_{D\in\mathcal D^\circ(M)}e_p(-4hD)\right|^2.          \tag{40.9}
\]
The \(h=0\) term is \(t_p^2\), not \(pt_p^2\).

*Proof.*  Formula (40.3) follows prime coordinate by prime coordinate.
At a conditioned prime \(q\), a specified allowed class modulo \(q^e\)
has conditional probability
\(q^{-e}/(1-f(q)/q)=q\{q-f(q)\}^{-1}q^{-e}\); all other surviving
coordinates remain uniform.  Summing (40.3) at a fixed projected residue
gives (40.5).  Expanding the nonnegative square gives (40.6)--(40.8), since
\(-4\) is invertible modulo \(p\).  Finally additive-character
orthogonality
\[
 {1\over p}\sum_{h\bmod p}e_p(h(D-E))=\mathbf1_{D\equiv E(p)}
\]
gives (40.9). \(\square\)

The shifted-divisor parametrization is equally exact.  By (21.4), for every
representative \(D\),
\[
 D={R^2\over s},\qquad R=R_0(D),\quad s\mid\operatorname {rad}(R),
 \qquad M=4Rk-1.                                            \tag{40.10}
\]
Consequently a pair in (40.6) is counted at \(p\) precisely when
\[
 p\mid4Rk-1, \quad p\mid4R'k'-1, \quad
 p\mid {R^2\over s}-{R'^2\over s'},                        \tag{40.11}
\]
subject to the canonical-representative and retention indicators.  This is
a divisor-pair correlation between two moving shifted values, not a
variance of the ordinary divisor function in a fixed progression.

**Lemma 40.2 (literal atom diagonal; proved).**  The part of (40.6) with
the same atom on both sides is \(O(\Lambda)\), hence
\(o(\Lambda^2)\).

*Proof.*  From (37.16), \(\kappa(M)\leq2\) for large \(X\).  For every odd
composite \(M\), the sum of its distinct prime divisors is at most \(M\).
(The one-prime case is immediate; for at least two odd primes their sum is
at most their product, and induction preserves the inequality.)  The
diagonal is therefore at most
\[
 4\sum_{M,D}{1\over M^2}\sum_{p\mid M}p
 \leq4\sum_{M,D}{1\over M}=O(L^3/\log z)=O(\Lambda),        \tag{40.12}
\]
by Theorem 31.2 with zero charges. \(\square\)

This lemma does not include different classes at one modulus or equal
integer divisors occurring at different moduli.

### 40.2 A proved endpoint reduction

For \(p\nmid4R\), let \(c_p(R)\in\{1,\ldots,p-1\}\) be the inverse of
\(4R\) modulo \(p\).  If the atom (40.10) has \(p\mid M\), then uniquely
\[
                         k=c_p(R)+jp, \qquad j\geq0.       \tag{40.13}
\]
Split its contribution to the \(p\)-residue vector into the **endpoint**
\(j=0\) and the **regular tail** \(j\geq1\); denote the corresponding
vectors by \(u^{\rm end}_{p,a}\) and \(u^{\rm reg}_{p,a}\).

**Theorem 40.3 (regular progression tails satisfy dispersion; proved).**
With the full canonical and retention restrictions allowed,
\[
 \mathcal V_X^{\rm reg}:=
 \sum_{z<p\leq X}p\sum_a(u^{\rm reg}_{p,a})^2
 \ll L^2\log L+{L^7\over z\log z}=o(\Lambda^2).             \tag{40.14}
\]

*Proof.*  Fix \(D=R^2/s\).  Dropping the canonical and retention
restrictions only enlarges its nonnegative mass.  Since \(\kappa(M)\leq2\)
and \((4Rk-1)^{-1}\ll(Rk)^{-1}\), (40.13) gives
\[
 v^{\rm reg}_{p,D}
 \leq {C\over R}\sum_{j\geq1,\ c_p(R)+jp\leq(X+1)/(4R)}
                    {1\over c_p(R)+jp}
 \leq {CL\over pR}.                                        \tag{40.15}
\]
Put \(h_D=L/R_0(D)\).  On expanding the regular square, compatibility
modulo \(p\) says \(p\mid D-E\), and hence
\[
 \mathcal V_X^{\rm reg}
 \ll\sum_{D,E}h_Dh_E
       \sum_{\substack{p>z\\p\mid D-E}}{1\over p},         \tag{40.16}
\]
where for \(D=E\) the inner sum is over all relevant primes.
The parametrization (21.4) and elementary Euler products give
\[
 \sum_Dh_D
 \leq L\sum_{R\leq X}{2^{\omega(R)}\over R}\ll L^3,
 \qquad
 \sum_Dh_D^2
 \leq L^2\sum_{R\geq1}{2^{\omega(R)}\over R^2}\ll L^2.   \tag{40.17}
\]
For \(D\ne E\), both are below \(X^2\), so the number of primes greater
than \(z\) dividing \(D-E\) is at most \(2L/\log z\).  Therefore
\[
 \sum_{\substack{p>z\\p\mid D-E}}{1\over p}
 \leq {2L\over z\log z}.
\]
For \(D=E\), Mertens' estimate gives \(O(\log L)\).  Substitution in
(40.16) proves the first inequality in (40.14).  Since
\(z\log z\asymp L^3\log\log L\) and
\(\Lambda^2=L^6/(\log L)^2\), both terms are \(o(\Lambda^2)\). \(\square\)

**Corollary 40.4 (exact remaining pair-level target; proved equivalence).**
The residue-dispersion bound (37.27) holds if and only if
\[
 \boxed{\quad
 \mathcal V_X^{\rm end}:=
 \sum_{z<p\leq X}p\sum_a(u^{\rm end}_{p,a})^2=O(\Lambda^2).
 \quad}                                                       \tag{40.18}
\]
In divisor variables this is the explicit, falsifiable estimate
\[
 \sum_{z<p\leq X}p\sum_{a\bmod p}
 \left(
  \sum_{\substack{R,s,c,q:\ s\mid\operatorname {rad}(R),\ 1\leq c<p\\
       pq=4Rc-1\leq X,\ P^-(pq)>z,\ pq\equiv3(4)\\
       R^2/s\equiv-4^{-1}a\ (p),\ q>1\ ({\rm so}\ pq\ {\rm composite}),\\
       R^2/s\ {\rm is\ the\ retained\ representative\ at}\ pq}}
       {\kappa(pq)\over pq}
 \right)^2=O(\Lambda^2).                                    \tag{40.19}
\]
Every term here has \(q>z\) (from \(z\)-roughness of the composite
\(pq\)) and \(q<4R\).  Thus (40.19) is precisely a
short-cofactor endpoint estimate.

*Proof.*  The endpoint and regular vectors have nonnegative coordinates.
Thus \(\mathcal V_X^{\rm end}\leq\mathcal V_X\), while
\(\mathcal V_X\leq2\mathcal V_X^{\rm end}+2\mathcal V_X^{\rm reg}\).
Use Theorem 40.3.  At an endpoint,
\(M=4Rc-1=pq\); composite \(z\)-roughness gives \(q>z\), and \(c<p\)
gives \(q<4R\).  Substitution of \(D=R^2/s\) gives (40.19). \(\square\)

This reduction also identifies an analogous moving short-cofactor range to
the one which forced the \(u_p\) term in Theorem 31.3 (the ranges differ:
(31.18) treats \(M/p<C_0p^{1/2}\), while (40.19) has \(M/p<4R_0(D)\);
neither contains the other).  It is not removed by the
regular divisor-density calculation.

### 40.3 What the large sieve and BDH do not supply

For comparison, Cauchy's residue-blind bound is exactly
\[
 \mathcal V_X\leq\sum_{z<p\leq X}pt_p^2.                   \tag{40.20}
\]
Even under the idealized \(t_p\ll\Lambda/p\), it yields
\[
 \Lambda^2\sum_{z<p\leq X}{1\over p}
 =\Theta(\Lambda^2\log L),                                 \tag{40.21}
\]
which reproduces (37.26).  Theorem 40.3 removes this loss from all
noninitial points of the relevant progressions; (40.19) is where residue
concentration can still realize it.

**Failure log 40.5 (standard additive large sieve).**  Formula (40.9)
looks like a large-sieve norm, but its inner sequence is
\[
 \sum_{e,m}{\kappa(p^em)\over p^em}
   \sum_{D\in\mathcal D^\circ(p^em)}e_p(-4hD).              \tag{40.22}
\]
It depends on the denominator prime \(p\) through the shifted value
\((p^em+1)/4\), the divisor set, the upper endpoint, and residual deletion.
The additive large sieve requires one common coefficient sequence evaluated
at the well-spaced fractions \(h/p\); it gives no cross-modulus inequality
for arbitrary sequences \(c_{p,D}\).  Applying it separately in each row
is exactly the Cauchy/trivial bound (40.20).

There is a second, independent scale warning.  Even for a hypothetical
common sequence supported on the possible integer divisors
\(D\leq X^2/16\), the standard estimate on \(P<p\leq2P\) is
\[
 \sum_{p\sim P}\sum_{h=1}^{p-1}
 \left|\sum_{D\leq(X+1)^2/16}c_De_p(hD)\right|^2
 \ll(P^2+X^2)\sum_D|c_D|^2.                                \tag{40.23}
\]
A composite \(z\)-rough modulus incident to \(p\) has
\(p\leq X/z\).  Hence at the largest possible prime scale the geometric
factor in (40.23), after a putative \(1/p^2\) normalization, is still
\(1+(X/P)^2\gg z^2\), not a favorable level-one factor.  Weighted divisor
structure might beat this generic bound, but (40.23) itself does not.

**Failure log 40.6 (ordinary divisor BDH).**  Barban--Davenport--Halberstam
variance theorems for a fixed divisor-like arithmetic function in residue
classes do not state (40.19).  Here the modulus \(p\) is simultaneously a
factor of \(4Rk-1\), the divisor being projected is \(R^2/s\), and the
endpoint enforces \(k=c_p(R)<p\) (equivalently \(pq=4Rc-1\) with
\(q<4R\)).  No cited theorem in this notebook gives a mean square uniform
in this coupled inverse/short-cofactor family.  Invoking “BDH for the
divisor function” without a theorem containing these quantifiers would be
a gap.  A proof or counterexample to (40.19) is the exact pair-level next
step.

### 40.4 Conditioning and the higher-codegree wall

The estimate behind (37.16) is
\[
 \max_M\log\kappa(M)
 \ll {L\over\log z}  z^{-1+o(1)}=L^{-2+o(1)},            \tag{40.24}
\]
using the maximal-order divisor bound for \(f(q)\).  Thus replacing
conditional weights by \(1/M\) is harmless at pair level.  There is,
however, an arithmetic correction to the proposed high-moment audit:
\[
 (1+L^{-2+o(1)})^\Lambda
 \leq\exp\{L^{1+o(1)}/\log L\}.                            \tag{40.25}
\]
This available bound does **not prove** a \(1+o(1)\) product comparison.  This does not kill a constant-base factorial-moment estimate: the crude
factor in (40.25) is still \(e^{o(\Lambda)}\), so it can be absorbed by a
fixed enlargement of the base in \((C\Lambda)^j\) when
\(j\asymp\Lambda\).  At conditioned low coordinates the compatibility
collapse is also \(q-f(q)\leq q\).  What is invalid is only the claimed
multiplicative \(1+o(1)\) comparison of a whole \(j\)-fold marginal
product.

For clarity, the exact remaining hierarchy is stronger than powers of
(37.27).  If \(A_1,\ldots,A_j\) are compatible retained atoms, then
\[
 \Pr\!\left(\bigcap_{i=1}^jA_i\mid T_0=1\right)
 ={1\over[ M_{A_1},\ldots,M_{A_j}]}
  \prod_{\substack{z<q\leq Y, q\equiv3(4)\\
                    q\mid[ M_{A_1},\ldots,M_{A_j}]}}
       {q\over q-f(q)}.                                     \tag{40.26}
\]
The conditioning factor in this exact intersection is at most
\[
 \exp\!\left\{O\!\left(\sum_{z<q\leq Y}{f(q)\over q}\right)\right\}
 =\exp\{O((\log Y)^2)\}=\exp\{O((\log L)^2)\}=e^{o(\Lambda)},
\]
by Lemma 24.3.  Thus an unconditioned constant-base factorial-moment bound
would transfer after changing its base; the total factor still need not be
\(1+o(1)\).  Relative to the product of the individual marginals, prime powers therefore
contribute \(q^{\sum_i v_q(M_{A_i})-\max_i v_q(M_{A_i})}\),
modified at a conditioned coordinate by the corresponding powers of
\((q-f(q))/q\).  Compatibility must also hold through the smallest shared
prime-power digit.  A prime-level pair square does not control these
multiple-prime, higher-power overlaps.

A precise sufficient hierarchy can be stated without heuristic
independence.  Here let the atoms include every event counted by \(H\),
including the tail prime atoms.  For a compatible ordered set \(S\) of
distinct atoms put
\[
 \mathcal L(S)=
 \sum_{B\notin S\atop S\cup\{B\}\ {\rm compatible}}
 {\Pr(\bigcap_{A\in S\cup\{B\}}A\mid T_0=1)
  \over
  \Pr(\bigcap_{A\in S}A\mid T_0=1)}.                        \tag{40.27}
\]
If, for every \(|S|<m\) with \(m\asymp\Lambda\), one proved
\[
                         \mathcal L(S)\leq C\Lambda,         \tag{40.28}
\]
then induction on ordered compatible tuples would give
\(\mathbb E(H)_m\leq(C'\Lambda)^m\), which is (37.19).
Single-coordinate star estimates of the form
\[
 \sum_{p>z}(p-f(p))^{j-1}\sum_a u_{p,a}^j
       \leq(C\Lambda)^j, \qquad2\leq j\leq m,           \tag{40.29}
\]
with \(f(p)=0\) off the conditioned prime subsystem, would control only
stars sharing one squarefree coordinate.  They are not sufficient for
(40.28): an atom can participate simultaneously at several primes, and
prime powers introduce the extra factors in (40.26).  No estimates
(40.28), (40.29), or an equivalent averaged multi-coordinate hierarchy are
proved here.  Section 47 subsequently refutes the literal (40.28) and the
resulting raw-\(H\) bound (37.19); §49 refutes the replacement (47.16) and
the reduced factorial-moment bound.  The one-coordinate hierarchy (40.29)
remains open.  (wave-17 update)  Therefore even a future proof of the pair endpoint
(40.19) would pass only the first test; it would not by itself activate
Proposition 37.3 for either the original count or the repaired count.

### 40.5 Exact finite companion and verdict

**Computational 40.7 (exact finite scope).**  `verify.py (am)` uses the
same composite, \(z\)-rough, prime-implied deletion convention as block
(aj), chooses the least divisor representative in (40.1), and additionally
conditions on the toy low tensor through \(Y\).  All masses and both the
ordered-pair identity (40.6) and endpoint/regular split are computed as
rational numbers.  It reports:

\[
\begin{array}{c|c|c|r|c|c|c|c|c}
X&z&Y&K&\mathcal V_X/\Lambda^2&
 \mathcal C_X/\Lambda^2&\mathcal C_X/\mathcal V_X&
 \mathcal V_X^{\rm end}/\mathcal V_X&\sum_{z<p\leq X}1/p\\ \hline
80&2&11&14&.0002902&.0006208&2.139&.858&1.269\\
120&3&13&34&.0001183&.0005121&4.328&.783&1.016\\
200&5&17&28&.0000272&.0001653&6.088&.891&.916
\end{array}                                                  \tag{40.30}
\]
Here \(\mathcal C_X=\sum_p p t_p^2\) is the exact Cauchy worst case, while
\(\Lambda^2\sum1/p\) is the idealized loss in (40.21).  The block computes
every \(t_p\) in exact rational arithmetic and prints it rounded, and
spot-checks Parseval (at \(X=200\), \(p=7\)) in the exact cyclotomic field
\(\mathbb Q(\zeta_7)\), rather than with floating-point characters.  The
endpoint dominates these toys.  None of the ratios is asymptotic evidence,
and the declining displayed values do not prove (40.19).

**Assessment 40.8 (wave-13 verdict).**  The target (37.27) has been reduced
exactly to the short-cofactor estimate (40.19), and the complementary
regular progression tail satisfies a stronger \(o(\Lambda^2)\) bound.  This
is a genuine narrowing of the pair wall, not its closure.  Standard
large-sieve and divisor-BDH statements do not contain the moving
coefficient/endpoint quantifiers, and the conditioning shortcut at
\(j\asymp\Lambda\) was arithmetically overstated.  The pair endpoint
(40.19), the one-coordinate hierarchy (40.29), (33.16), and the refutation
of \(H_{\rm PF}'\) remain **OPEN**.  Section 47 refutes the literal (40.28)
and raw-\(H\) (37.19); §49 refutes the repaired hierarchy (47.16) and the
reduced moment bound.  (wave-17 update)


## 41. Unit R: blind parallel construction and stress test of the cubic-rate chain

**Scope and status.**  This is an independent-construction datum for §39,
not a status upgrade.  In particular, Theorem 34.8 was an allowed input and
was not independently reproved here.  Theorem 39.7 remains
**CLAIMED/PROVISIONAL**, and the priority caveat in §39.7 remains unchanged.

### 41.1 Blind protocol and audit trail

Unit R cloned the repository independently and worked at base
`c489912bc704abb17af44c19ee830a3cb7421140`.  Before the blind-phase commit it
read only the task brief, all of §16 (`notes.md` lines 2715--3239 at that
commit), and all of §34 (lines 10741--11303).  It did not open §39 or inspect
`verify.py (al)`.  The required baseline run was green; its console output did
print `(al)`'s summary line, but its code was not read.  The complete blind
derivation was committed as
`347a570312f68141e364b9d385db52e6be58aa75` in `unit_r_blind.md` before §39
was opened.  Phase 3 then read §39 and the wave-13 repair commit
`41570a595f660adc3abc5cd51b7c7cc74917a0e1`.  As in §35, git history
verifies the snapshots, texts, and commit order only; it cannot verify
what was visible on screen or enforce the read isolation, so the
blind-phase claims above remain an explicit self-attestation, not
independently audited blindness.

The construction below is a condensed self-contained record of that blind
file.  Put `t=log X`; constants may depend on the fixed
`0<kappa<1/240`, but are uniform in the displayed variables.

### 41.2 Independent construction

**Proposition 41.1 (S1--S2; proved).**  Every exceptional denominator avoids
all the atoms.  An atom hit in the fibre `c=n (mod 24L_K)` obeys
`k|u+cv`.  Compatible distinct atoms have distinct large-prime coordinates,
and a compatible ordered `j`-set has probability

after CRT
\[
 {1\over [k_1,\ldots,k_j]\prod_i\ell_i}.                    \tag{41.1}
\]

*Proof.*  For an atom put `w=(k ell+1)/(4uv)`.  A hit says
`nv=-u (mod k ell)`, so Lemma 16.1 applied to
`(k ell+1)/4=uvw` gives the representation.  Reduction modulo `k`, followed
by `n=c (mod k)`, gives the coupling.

At fixed `ell`, equality of two atom classes gives
`ell|uv'-u'v`; the absolute value is at most `x^(1/3)<ell`, so reducedness
makes the ordered pairs equal.  If the multipliers differed, their common
`uv` would divide both `(k ell+1)/4` and `(k'ell+1)/4`, hence divide
`(k-k')/4`, contrary to `uv>H^2>K>|k-k'|/4`.  Thus the atoms are equal.
A compatible set can consequently use each `ell` only once.  Since
`ell_i>K` and the `ell_i` are distinct, its lcm is the denominator in
(41.1), and CRT finishes the proof.  This proves S1--S2. \(\square\)

**Proposition 41.2 (S3, including the residue-resolved box; proved).**
Uniformly for `k<=K`, `g|k`, and reduced `a (mod g)`,
\[
 W_{k,a}(g)\ll {t^2\varphi(k)^2\over\varphi(g)k^3},\qquad
 W_k\asymp {t^2\varphi(k)^2\over k^3},\qquad
 \mu_X\asymp t^3.                                           \tag{41.2}
\]

*Proof.*  The load-bearing box estimate is derived as follows.  In fixed
relative boxes `u~U,v~V`, put `F(n)=n/phi(n)` and drop only `(u,v)=1` for
the upper bound.  For each reduced `v (mod k)`, the condition
`u=-av (mod g)` selects exactly `phi(k)/phi(g)` reduced classes modulo `k`.
Shiu in those classes and, separately, in all reduced `v`-classes gives,
after division by `UV`,
\[
 {C\over\varphi(g)}
 \exp\{-2\sum_{p\mid k}(p-1)^{-1}\}
 \leq {C\over\varphi(g)}\left({\varphi(k)\over k}\right)^2. \tag{41.3}
\]
Here `k<=K<U^(1/10),V^(1/10)`, and
`exp(-1/(p-1))<=1-1/p`; hence the constant is uniform and there is no
hidden divisor or logarithmic loss.  Summing `O(t^2)` box pairs gives
\[
 \sum_{H<u,v\leq z\atop (uv,k)=1,\ u+av=0\ (g)}
 {1\over\varphi(u)\varphi(v)}
 \ll {t^2\varphi(k)^2\over\varphi(g)k^2}.                  \tag{41.4}
\]
This is the independent D-a calculation.

For fixed `(u,v)`, Brun--Titchmarsh in
`ell=-k^{-1} (mod 4uv)`, where `4uv<=4x^(1/3)`, bounds the reciprocal prime
mass by `C/(phi(u)phi(v)log x)`.  Equation (41.4), the factor `1/k`, and
`O(t)` blocks give the first estimate in (41.2).

Without the ratio condition, the pair-box density is uniformly comparable
to `(phi(k)/k)^2`; the coprimality factor over primes not dividing `k` stays
between two absolute constants.  The fixed-function Rankin argument removes
the high-omega tail.  For this fixed `k`, each progression modulus has only
`2^omega(uv)=(log X)^O(1)` allocations, so ordinary
Bombieri--Vinogradov supplies the matching lower prime mass without a factor
`K`.  This proves the estimate for `W_k`.  Finally weighted Cauchy, (16.6),
and `sum_{k<=K,k=1(4)}1/k asymp log K` give
\[
 \sum_{k\leq K,k=1(4)}{\varphi(k)^2\over k^3}\asymp\log K\asymp t,
\]
which proves the mass assertion and S3. \(\square\)

**Proposition 41.3 (S4, exact prime-power induction; proved).**  For
`2<=y<X^(1/2)` and all `m>=1`,
\[
 \mathbb E((H_X)_m\mid(n,P_y)=1)\leq(Ct^3)^m.              \tag{41.5}
\]

*Proof.*  Let previous compatible atoms fix a reduced class modulo multiplier
lcm `L`.  For a new atom with `p^e||k`, put `p^f||L`.  Conditional on the
old set and roughness, the exact local probability is
\[
\begin{array}{c|c}
 f\geq e&1\\
 0<f<e&p^{-(e-f)}\\
 f=0,\ p\leq y&1/\varphi(p^e)\\
 f=0,\ p>y&p^{-e}.
\end{array}                                                  \tag{41.6}
\]
A residue inconsistency modulo `p^min(e,f)` instead gives zero.  The new
`ell` costs `1/ell`.  Thus, with `g=(k,L)`, consistency modulo `g` leaves
\[
 {C(k,L;y)\over k\ell},\qquad
 C(k,L;y)=g\prod_{p\mid k,\ p\nmid L,\ p\leq y}{p\over p-1}. \tag{41.7}
\]
The residue profile in (41.2) bounds the sum at fixed `k`.  Prime by prime,
the factor outside the remaining `1/k` is
\[
 1-1/p\quad(p\mid L),\qquad
 1-1/p\quad(p\nmid L,p\leq y),\qquad
 (1-1/p)^2\quad(p\nmid L,p>y).                              \tag{41.8}
\]
Thus it is at most one pointwise, including all unequal exponent patterns,
and
\[
 \sum_{k\leq K}{C(k,L;y)\varphi(k)^2\over\varphi(g)k^3}
 \leq\sum_{k\leq K}{1\over k}\ll t.                       \tag{41.9}
\]
Each next atom therefore costs at most `Ct^3`.  Incompatible tuples vanish,
old atoms are excluded by the falling factorial, and Proposition 41.1 gives
a new `ell` at every step.  Iteration proves (41.5) and D-b. \(\square\)

**Proposition 41.4 (S5, conditioned void; proved).**  For a sufficiently
large fixed `B` and `y=Bt^3`,
\[
 \Pr(H_X=0\mid(n,P_y)=1)\leq e^{-ct^3}.                    \tag{41.10}
\]

*Proof.*  Reveal `c=n (mod 24L_K)` and take
\[
 \mathcal J(c)=\{k\leq K:k=1\ (4),(k,c)=1\},\qquad
 h(c)=\sum_{k\in\mathcal J(c)}{\varphi(k)\over k^2}.
\]
This is a reduced fibre containing 1.  Theorem 34.8 supplies inside the
c-free atoms a pruned active subfamily of prime-coordinate mass
`>=c t^2h(c)`.  Proposition 41.1 makes its classes at each `ell` distinct;
different `ell`-coordinates are independent.  Hence
\[
 \Pr(H_X=0\mid c,(n,P_y)=1)\leq e^{-ct^2h(c)}.             \tag{41.11}
\]

For an exponentially strong average, not a Markov bound, put
`w_k=phi(k)/k^2`, `h_0=sum w_k asymp log K`, and
\[
 A_p=\sum_{p\mid k}w_k\ll{\log K\over p}.
\]
Roughness and a union bound give
`h(c)>=h_0-sum_{p|c,p>y}A_p`.  The relevant large-prime divisibility
indicators are independent with means `1/p`.  With `lambda=ct^2`, a large
fixed `B` makes `lambda A_p=O(t^3/p)` uniformly small, and
\[
 \mathbb E\exp\{\lambda\sum_{p\mid c,p>y}A_p\}
 \leq\exp\{C\lambda\log K\sum_{p>y}p^{-2}\}=O(1).         \tag{41.12}
\]
Averaging (41.11) now gives (41.10).  This is D-c.  Direct Janson is not a
substitute: the usual dependency sum has quadratic order in the mass.
\(\square\)

**Proposition 41.5 (S6, Bonferroni and ledger; proved).**  Let `r` be the
least even integer at least `D_Bt^3`, for a sufficiently large fixed `D_B`,
and put
\[
 \nu_X=\mathbf1_{(n,P_y)=1}\sum_{j\leq r}(-1)^j{H_X\choose j}.
\]
It is at least one on every exceptional prime above `max(K,y)`, has CRT mean
at most `e^{-ct^3}`, degree `O(t^3)`, per-term modulus logarithm `O(t^4)`,
and coefficient-sum logarithm `O(t^4)`.  If `log N>=C_0t^4`, then
\[
 \sum_{n\leq N}\nu_X(n)\ll Ne^{-ct^3}.                    \tag{41.13}
\]

*Proof.*  For even `r`, the truncated sum is 1 at zero and
`C(h-1,r)>=0` at `h>=1`; it therefore majorizes the void.  Moreover
`C(h-1,r)<=C(h,r+1)`.  Propositions 41.3--41.4 and Stirling give
\[
 \mathbb E(Q_r(H_X)\mid(n,P_y)=1)
 \leq e^{-ct^3}+{(Ct^3)^{r+1}\over(r+1)!}\leq e^{-c't^3}. \tag{41.14}
\]

Expand roughness over divisors of `P_y` and each binomial into atom sets.
The crude inventory bound is `log |A_X|=O(t)`.  Consequently
\[
 2^{\pi(y)}\sum_{j\leq r}{|\mathcal A_X|\choose j}
       =\exp\{O(t^4)\}.                                    \tag{41.15}
\]
A term has at most `r+pi(y)=O(t^3)` factors and modulus dividing
`P_y(KX)^r`, whose logarithm is `O(y)+O(rt)=O(t^4)`.  Every compatible term
is one class; on `[1,N]` its count is `N/q+O(1)`.  The total rounding error is
therefore `exp(O(t^4))`, and a sufficiently large `C_0` absorbs it into the
main bound.  This is the complete D-d ledger and proves S6. \(\square\)

**Corollary 41.6 (S7; proved from the allowed inputs).**  The preceding chain
implies
\[
 E_{\rm all}(N)\ll N\exp\{-c(\log N)^{3/4}\}.              \tag{41.16}
\]

*Proof.*  Take `t=alpha(log N)^(1/4)` with fixed `alpha` small enough for the
ledger window.  Equation (41.13) gives the prime bound.  Every prime factor
of an exceptional integer is exceptional.  The Rankin semigroup proof of
Theorem 16.5 applies with `g(u)=u^(3/4)` and
`delta=eta(log N)^(-1/4)`: for `u<=log N`,
`delta u<=eta u^(3/4)`, so partial summation leaves a uniformly bounded Euler
product.  This proves S7 and (41.16). \(\square\)

### 41.3 Reconciliation with §39

The classifications concern the proofs, not the publication status.
“Same-method” means the blind route converged to the same load-bearing
mechanism, even though it was derived without seeing §39.

| item | verdict | reconciliation |
|---|---|---|
| S1 | **CONFIRMED-SAME-METHOD** | Both use Lemma 16.1 and reduce the atom congruence modulo `k`; no constant difference. |
| S2 | **CONFIRMED-SAME-METHOD** | Both use the `z^2<ell` collision bound.  Unit R proves multiplier uniqueness from the gcd of `(k ell+1)/4` and `(k'ell+1)/4`; §39 instead says the congruence determines `k (mod 4uv)`.  The arguments are equivalent. |
| S3 | **CONFIRMED-SAME-METHOD** | Both use Shiu for `F=n/phi(n)`, Brun--Titchmarsh for the upper prime mass, and fixed-`k` Bombieri--Vinogradov for the lower.  Unit R works in classes modulo `k`; repaired §39 uses `lcm(g,rad k)`.  Unit R gets (41.3) from the one-sided local inequality, while §39 records uniform comparability. |
| S4 | **CONFIRMED-SAME-METHOD** | The local table (41.6) agrees exactly with §39's `q_y(k)b_y(g)/(k ell)`.  Unit R reduces the final summand pointwise to at most `1/k`; §39 packages the same cancellation in Lemma 39.3's Euler product.  The latter is correct but stronger machinery than needed for this bound. |
| S5 | **CONFIRMED-SAME-METHOD** | Both reveal the multiplier fibre and invoke Theorem 34.8 on the surviving subfamily.  §39 splits at `Z(c)<=eta` and applies Chernoff with parameter `y`; Unit R directly averages (41.11) using the actual lost weights `A_p` and parameter `ct^2`.  Both give the same exponential order. |
| S6 | **CONFIRMED-SAME-METHOD** | The Bonferroni identity, factorial tail, term count, lcm budget, and interval rounding match.  Unit R explicitly includes `theta(y)` in the modulus ledger; this is §39's `O(y)`. |
| S7 | **CONFIRMED-SAME-METHOD** | The critical-window choice and the Theorem-16.5 semigroup transfer agree exactly. |

**Wave-13 repair comparison.**  The repair commit reports that the original
§39 residue-box paragraph omitted the extra exclusions.  Its inserted Shiu
derivation is precisely the detail Unit R independently found necessary in
D-a.  The same commit added `y<X^(1/2)`; Unit R used that restriction in the
local `ell` factor.  Its restriction of the bad-fibre sum to primes actually
supported by `L_K` is implicit in Unit R's `A_p` (which is zero unless a prime
divides an admissible multiplier).  The proxy-share scope and the `D_B`
renaming do not enter Unit R's proof.  No repaired line conflicts with the
blind construction.

**Divergences.**  There are four presentational/argument variants just listed:
the multiplier-uniqueness algebra, modulus `k` versus `lcm(g,rad k)` in Shiu,
the pointwise harmonic bound versus Lemma 39.3's Euler comparison, and direct
weighted fibre averaging versus §39's good/bad split.  They produce no
constant, quantifier, or range disagreement.  Unit R found no missing step in
the repaired §39 text and no step there that it considers false.  It regards
Lemma 39.3's Euler-product comparison as unnecessary, not erroneous.  No
parallel-construction flag is appended to §39.7.

### 41.4 Independent numerical stress

`verify.py (an)` is fresh code and does not call or reuse `(al)`.  Its
"literal" mode means the literal dyadic-block cutoff \(u,v\leq x^{1/6}\)
only; two toy substitutions remain and are disclosed here: the floor is
\(H_{\rm toy}=1\) (not \(K^{10}\), which is empty at toy scale) and the
\(\omega\)-cutoff is inactive at these sizes.  It parses
the file before running, builds these dyadic-cutoff toy atoms at `X` up to 10000,
processes one `ell` fibre at a time, and stores only a multiplier CRT state.
Thus no Cartesian atom-set array is formed.  It computes the elementary CRT
intersection sums `e_j` exactly as rational numbers through `j=6`.  The
larger `ell^(1/3)` runs are explicitly structural sparsity tests; they are not
the literal cutoff and support no asymptotic inference.  A heavier enlarged
`X=10000` moment row is behind `ES_FULL_SCAN=1`.

The literal results are
\[
\begin{array}{c|r|r|r|c|rrrrrr}
X&K&|\mathcal A|&\#\ell&\mu&
1!e_1/\mu&2!e_2/\mu^2&3!e_3/\mu^3&4!e_4/\mu^4&5!e_5/\mu^5&6!e_6/\mu^6\\\hline
3000&5&138&69&.049793&1&1.063584&1.226192&1.531647&2.033861&2.798509\\
6000&9&330&147&.062663&1&1.080129&1.279698&1.656250&2.294238&3.317229\\
10000&13&966&409&.109744&1&1.085372&1.290092&1.670174&2.318299&3.388426
\end{array}                                                  \tag{41.17}
\]
An enlarged `X=3000,K=9` family, included to exercise the prime power `9`,
has 1202 atoms on 175 primes, `mu=.697545`, and normalized moments
\[
 (1,.990097,.971991,.947383,.917846,.884716).               \tag{41.18}
\]
The literal positive high-moment excess is finite dependency evidence, not a
problem for the constant-base upper bound (41.5), and no asymptotic claim is
made from either row.

For each nontrivial `g|k` and every reduced `a (mod g)`, the block records
\[
 R_{k,g,a}=\varphi(g)W_{k,a}(g)/W_k,
\]
so the reference `1/phi(g)` profile is `R=1`:
\[
\begin{array}{c|r|r|r|r|rrrr}
\text{cutoff}&X&K&|\mathcal A|&\#(k,g,a)&\min R&\operatorname{median}R&\max R&
 \operatorname{mean}|R-1|\\\hline
\text{literal}&3000&5&138&4&0&0&4.000&1.500\\
\text{literal}&6000&9&330&4&0&.127&3.745&1.373\\
\text{literal}&10000&13&966&16&0&0&5.552&1.476\\
\text{enlarged}&3000&5&1000&4&.546&.748&1.958&.479\\
\text{enlarged}&6000&9&2874&12&.361&.905&1.832&.446\\
\text{enlarged}&10000&13&7700&24&.204&1.019&1.743&.385
\end{array}                                                  \tag{41.19}
\]
The literal boxes are too sparse to populate every residue and show isolated
large ratios.  In the denser structural stress the maximum and mean absolute
deviation decrease across these three scales; no scale-growing systematic
excess was found.  This is only a bug hunt, not evidence for (41.2).

All 14,210 atoms across the literal and enlarged stress families passed the
S1 coupling and exact multiplier identity, and every fixed-`ell` projection
was distinct.  In the four pair-scanned families, all 1,128,378 compatible
pairs had distinct `ell`-coordinates.  At the overlapping `(al)` parameters
`X=625,K=5,H_toy=1`, the independent enlarged enumerator reproduced exactly
134 atoms, 134 classes, and 34 primes.  The default block is memory-bounded
and runs in under ten seconds; the repository's full default verification is
green.

### 41.5 Overall verdict

**Independent-construction verdict: the repaired S1--S7 chain is sound from
this protocol's standpoint, with all seven statements CONFIRMED-SAME-METHOD.**
The blind derivation independently exposed the same three load-bearing needs
highlighted in §39.7: the residue-resolved Shiu estimate with full local
uniformity, prime-power collapse/consistency cancellation, and exponentially
strong removal of bad multiplier fibres.  Reconciliation found no genuine
error and numerical stress found no structural counterexample.

This verdict is deliberately limited.  The protocol treated Theorem 34.8 as
an input, did not perform a new literature-priority search, and mostly
converged to §39's method rather than supplying a wholly different proof.
It therefore adds insurance and a blind derivability record, but **does not
upgrade Theorem 39.7 beyond CLAIMED/PROVISIONAL**.
## 42. The short-cofactor endpoint is sparse in the radical root, but its moving squarefree fibres remain open

Keep the notation and the canonical/retention convention of §40.  The
labels here are strict.  The two endpoint normal forms, the absence of an
equal-shift off-diagonal, the fixed-$s$ estimate, and the bounded-polylogarithmic
prime range are **proved**.  They do not prove (40.19).  The unresolved part
is the simultaneous sum over the moving divisors
$s\mid\operatorname {rad}(R)$ at super-polylogarithmic primes; consequently
(37.27), (33.16), and the refutation of $H_{\rm PF}'$ remain **OPEN**.
Section 47 refutes raw-$H$ (37.19), and §49 refutes both its proposed
antichain hierarchy (47.16) and the corresponding reduced moment bound.
(wave-17 update)

### 42.1 Exact sparse and complement-divisor normal forms

Fix a prime $p>z$.  Since $p\mid4Rc-1$, one has $(p,4R)=1$.  For
$(p,4R)=1$ define
$q_p(R)$ to be the unique integer in $[1,4R)$ such that

$$
             p q_p(R)\equiv-1\pmod {4R}.                    \tag{42.1}
$$

Let $I_p(R,s)$ be the indicator that $(p,4R)=1$ (otherwise
$I_p(R,s)=0$ and $q_p(R)$ is left undefined), $s\mid\operatorname {rad}(R)$,
$q=q_p(R)>z$, $pq\leq X$, $pq$ is composite and $z$-rough, and
$D=R^2/s$ is the retained canonical representative at $pq$.  Conditions
such as $pq\equiv3\pmod4$ are included in this indicator.  Put
$c=(pq+1)/(4R)$.

**Proposition 42.1 (endpoint sparsity and collision normal form; proved).**
The endpoint incidences over $p$ are exactly the pairs $(R,s)$ with
$I_p(R,s)=1$.  For each such pair,

$$
 q=q_p(R),\qquad z<q<4R,\qquad 1\leq c<p,
 \qquad {z\over4}<R\leq {X+1\over4}.                       \tag{42.2}
$$

In particular, there is at most one cofactor $q$, hence at most one modulus,
for each $(p,R,s)$; there can still be as many as
$2^{\omega(R)}$ values of $s$ for one $(p,R)$.  If

$$
 K_p^{\rm end}=\sum_{R,s}I_p(R,s),
$$

then the exact count and mass are

$$
 K_p^{\rm end}=\sum_{z/4<R\leq(X+1)/4}
                   \sum_{s\mid\operatorname {rad}(R)}I_p(R,s),
 \qquad
 t_p^{\rm end}={1\over p}\sum_{R,s}I_p(R,s)
                  {\kappa(pq_p(R))\over q_p(R)}.            \tag{42.3}
$$

Equivalently, with $A=(pq+1)/4=Rc$, the complementary divisor

$$
                         e={A^2\over D}=c^2s               \tag{42.4}
$$

satisfies, modulo $p$,

$$
 D\equiv\overline {16c^2s},
 \qquad -4D\equiv-\overline {4c^2s}.                       \tag{42.5}
$$

Thus two endpoint incidences over the same $p$ collide precisely when

$$
 D\equiv D'\pmod p
 \quad\Longleftrightarrow\quad
 c^2s\equiv c'^2s'\pmod p.                                 \tag{42.6}
$$

The endpoint energy consequently has the exact expansion

$$
 \mathcal V_X^{\rm end}
 =\sum_{z<p\leq X}{1\over p}
   \sum_{i,j\in\mathcal I_p}
   {\kappa_i\kappa_j\over q_iq_j}
   \mathbf1_{c_i^2s_i\equiv c_j^2s_j\ (p)},                \tag{42.7}
$$

where $\mathcal I_p$ is the incidence set in (42.3).  If $i\ne j$
contributes to (42.7), then

$$
                  D_i\ne D_j,
 \qquad p\mid D_i-D_j\ne0.                                 \tag{42.8}
$$

*Proof.*  Equation (42.1) has exactly one representative in $[1,4R)$.
For an endpoint $pq=4Rc-1$ and $c<p$, so $q<4R$; roughness gives
$q>z$, which gives the range for $R$.  Conversely (42.1) and the
conditions in $I_p$ recover the positive integer $c=(pq+1)/(4R)<p$,
hence the endpoint.  This proves (42.2)--(42.3).  Since
$A\equiv\overline4\pmod p$, $D=A^2/(c^2s)$ gives (42.4)--(42.6).
Expanding the residue square in (40.18) gives (42.7).

Finally $D_i=D_j$ forces $R_i=R_0(D_i)=R_0(D_j)=R_j$ and then
$s_i=R_i^2/D_i=s_j$.  The uniqueness in (42.1) forces $q_i=q_j$,
hence the same modulus and the same retained atom.  Therefore distinct
incidences cannot have equal integer shifts, and (42.6) gives (42.8).
$\square$

The diagonal $i=j$ in (42.7) is a subset of Lemma 40.2 and is
$O(\Lambda)$.  The new point is that the generic possibility $D=E$ at
different moduli noted after (40.12) disappears inside the endpoint at a
fixed shared prime.  Every remaining collision is genuinely a nonzero
divisibility coincidence.

The per-root smallness does not aggregate by itself.  The weights used in
the regular proof satisfy

$$
 \sum_{z/4<R\leq X/4}\ \sum_{s\mid\operatorname {rad}(R)}{L\over R}
 =L\sum_{z/4<R\leq X/4}{2^{\omega(R)}\over R}
 \asymp L^3.                                                \tag{42.9}
$$

Here removing $R\leq z/4$ subtracts only
$O(L(\log z)^2)=o(L^3)$.  Thus $h_D<4L/z$ for each endpoint shift
is true, but there are enough radical roots to retain cubic aggregate mass.

### 42.2 A proved fixed-fibre endpoint estimate

For a fixed squarefree integer $s$, let $u^{\rm end,(s)}_{p,a}$ contain
only endpoint incidences whose parameter in (21.4) is this $s$.  This
includes the $s=1$ slice, but not the moving slice
$s=\operatorname {rad}(R)$.

**Theorem 42.2 (every fixed squarefree fibre disperses; proved).**  Uniformly
in squarefree $s$,

$$
 \sum_{z<p\leq X}p\sum_{a\bmod p}
       (u^{\rm end,(s)}_{p,a})^2
 \ll L^3+L^2\log L=o(\Lambda^2).                            \tag{42.10}
$$

Consequently, for any prescribed set $\mathcal S$ of $K$ squarefree
integers, the endpoint subfamily with $s\in\mathcal S$ has energy

$$
                         O(K^2L^3).                         \tag{42.11}
$$

In particular it satisfies the target $O(\Lambda^2)$ whenever
$K=O(L^{3/2}/\log L)$.

*Proof.*  Positivity permits the canonical and retention restrictions to be
dropped for an upper bound, and $\kappa\leq2$.  Put $Q_p=X/p$ and

$$
 B_{p,c}^{(s)}=
 \sum_{\substack{z<q\leq Q_p,\ pq\equiv-1\ (4c)\\
                  s\mid\operatorname {rad}((pq+1)/(4c))}}
                  {1\over q},
 \qquad1\leq c<p.                                         \tag{42.12}
$$

If $p\mid s$ this is empty.  Otherwise (42.5) shows that
$c\mapsto-\overline{4c^2s}$ has fibres of size at most two on
$1\leq c<p$.  Hence

$$
 p\sum_a(u^{\rm end,(s)}_{p,a})^2
 \leq {8\over p}\sum_{c<p}(B_{p,c}^{(s)})^2.              \tag{42.13}
$$

For fixed $p,c$, the $q$'s in (42.12) lie in one progression of
spacing $4c$.  Write $\ell_p=1+\log^+(Q_p/z)$.  Separate the
first term of that progression; the harmonic mass of the remaining terms
is $O(\ell_p/c)$.  The ordered off-diagonal is therefore at most the
first reciprocal, which is at most $1/z$, times this tail twice, plus the
square of the tail.  Dropping the $s$-restriction only enlarges these
positive sums, so

$$
 (B_{p,c}^{(s)})^2
 \leq\sum_{\substack{z<q\leq Q_p\\pq\equiv-1\ (4c)}}{1\over q^2}
   +O\!\left({\ell_p\over cz}+{\ell_p^2\over c^2}\right). \tag{42.14}
$$

The sum of the first terms in (42.14), after multiplication by $1/p$ and
summation over $p,c$, is $O(L^3)$.  Indeed set $M=pq$ and
$A=(M+1)/4$.  The admissible $c$'s divide $A$, and

$$
 \sum_{p,c,q}{1\over pq^2}
 \leq\sum_{\substack{M\leq X\\M\equiv3(4)}}{\tau(A)\over M^2}
                    \sum_{p\mid M}p
 \leq\sum_{\substack{M\leq X\\M\equiv3(4)}}{\tau(A)\over M}
 \ll L^3.                                                   \tag{42.15}
$$

The middle inequality is the odd-composite estimate used in (40.12), and
the last follows from $\tau(A)\leq\tau(A^2)\leq2F(M)+1$ and Theorem
18.2.  For the error terms, $Q_p>z$ forces $p<X/z$, and Mertens'
estimates give

$$
 \sum_{z<p<X/z}{1\over p}
 \left({\ell_p\log(2p)\over z}+\ell_p^2\right)
 \ll {L^2\over z}+L^2\log L.                              \tag{42.16}
$$

Equations (42.13)--(42.16) prove (42.10).  Finally
$(\sum_{s\in\mathcal S}x_s)^2\leq K\sum_sx_s^2$ and another summation
over the $K$ fibres give (42.11). $\square$

This proof is deliberately positivity-based; it does not assume
cancellation from a numerically declining energy.  It also identifies why
the fixed $s=1$ and fixed-$s$ quadratic slices are not the endpoint wall.
The moving choice $s\mid\operatorname {rad}(R)$ ranges over far more than
the number of globally fixed fibres allowed by (42.11), and cross-fibre
collisions in (42.6) receive no decay from the atom weight.

### 42.3 A proved prime range and where the logarithmic loss remains

**Proposition 42.3 (every fixed polylogarithmic prime range closes; proved).**
For every fixed $B>3$,

$$
 \sum_{z<p\leq L^B}p\sum_a(u^{\rm end}_{p,a})^2
                         =O_B(\Lambda^2).                  \tag{42.17}
$$

There are no endpoint incidences for $p>X/z$.

*Proof.*  Let $T_p(z;\boldsymbol a)$ be the weighted incidence sum in
Theorem 31.3.  The endpoint family is a retained subfamily of all distinct
intrinsic classes, its conditioning factor is at most $2$, and the weight
$W_{\boldsymbol a}$ in $T_p$ is at least one.  Therefore

$$
 t_p^{\rm end}\leq2T_p(z;\boldsymbol a)
 \leq2A(b_p+u_p).                                          \tag{42.18}
$$

Uniformly for $p\leq L^B$,

$$
 pb_p={L^3\over\log z}=O(\Lambda),
 \qquad
 pu_p=\log(2p)\exp\!\left({C_d\log(2p)\over\log\log(3p)}\right)
       =L^{o(1)}=o(\Lambda).                                \tag{42.19}
$$

Cauchy in the residue coordinate and Mertens' theorem now give

$$
 \sum_{z<p\leq L^B}p\sum_a(u^{\rm end}_{p,a})^2
 \leq C_B\Lambda^2\sum_{z<p\leq L^B}{1\over p}
 =O_B(\Lambda^2).                                          \tag{42.20}
$$

Finally $pq\leq X$ and $q>z$ imply $p<X/z$. $\square$

Thus the loss in the available residue-blind estimate is now localized to

$$
                         L^B<p\leq X/z                     \tag{42.21}
$$

for every fixed $B$.  This is not a negligible harmonic range:

$$
                  \sum_{L^B<p\leq X/z}{1\over p}
                    =\Theta(\log L).                       \tag{42.22}
$$

The unique-$q$ fact does not bound its cardinality.  For fixed $p$, as $R$
varies, (42.1) supplies a new possible $q$ each time; equivalently, for
fixed $c<p$, it supplies all

$$
 q\equiv-p^{-1}\pmod {4c},
 \qquad z<q\leq X/p,
 \qquad R={pq+1\over4c}.                                   \tag{42.23}
$$

Hence the endpoint has one cofactor per $(p,R)$, not one cofactor per $p$.

### 42.4 Character audit and exact failure points

Additive Parseval specializes to

$$
 \mathcal V_X^{\rm end}
 =\sum_{z<p\leq X}\sum_{h\bmod p}
 \left|{1\over p}
 \sum_{i\in\mathcal I_p}{\kappa_i\over q_i}
       e_p(-h\overline{4c_i^2s_i})\right|^2.                \tag{42.24}
$$

For one fixed $s$ with constant coefficients and
$\alpha\not\equiv0\pmod p$, the suggested quadratic sum is genuine:
inversion permutes $\mathbb F_p^*$ and

$$
 \left|\sum_{c=1}^{p-1}e_p(\alpha\bar c^{\,2})\right|
 =\left|\sum_{y=1}^{p-1}e_p(\alpha y^2)\right|
 \leq\sqrt p+1,                                            \tag{42.25}
$$

with the usual $O(\sqrt p\log p)$ incomplete bound by completion.  Theorem
42.2 is stronger for the needed fixed-fibre energy because positivity and
the two-to-one residue map avoid any cancellation hypothesis.

**Failure log 42.4 (the coefficients are the unresolved family).**  In the
actual sum, even before the canonical deletion, a fixed-$s$ coefficient is

$$
 \sum_{\substack{z<q\leq X/p,\ q\equiv-p^{-1}\ (4c)\\
                  s\mid\operatorname {rad}((pq+1)/(4c))}}
       {\kappa(pq)\over q},                                 \tag{42.26}
$$

(displayed relaxed: the endpoint system's full requirement is
\(P^-(q)>z\), not merely \(q>z\), so (42.26) is a majorant of the actual
coefficient — the extra terms have cofactors with a prime factor
\(\leq z\), which the endpoint system excludes), and then all
$s\mid\operatorname {rad}(R)$ are superposed.  A Gauss bound
for the unweighted complete $c$-sum does not bound a sum with these moving
nonnegative coefficients.  Replacing them by their absolute majorant before
using (42.25) discards the cancellation and returns residue-blind Cauchy.
Proving that (42.26) has sufficiently small correlation with the inverse
quadratic phase is a hybrid rough-progression/subset-divisor estimate; no
theorem cited in this notebook states it.

The range is also not uniformly long enough for completion to win.  Near
$p=X/z$, the cofactor interval $(z,X/p]$ has vanishing relative length,
and its active $c$'s are divisors of $(pq+1)/4$, not an interval of length
$\gg\sqrt p$.  At smaller fixed-polylogarithmic $p$ no cancellation is
needed by Proposition 42.3.  Thus (42.25) is an exact model calculation, not
a proof of (42.24).

**Failure log 42.5 (nonzero divisibility alone does not count the pairs).**
By (42.8), every off-diagonal collision has $p\mid D-D'\ne0$ and
$D,D'\leq(X+1)^2/16$.  Summing over possible primes for a fixed pair gives

$$
 \sum_{\substack{p>z\\p\mid D-D'}}{1\over p}
 \leq {2L\over z\log z}.                                   \tag{42.27}
$$

But after using $q,q'>z$, dropping the endpoint-incidence indicators would
leave this bound summed over
$\sum_{R\leq X}2^{\omega(R)}\asymp X\log X$ possible shifts.  That is
catastrophic, not polylogarithmic.  Keeping the indicators means counting
simultaneously (42.1) and (42.6), which is exactly the coupled endpoint
problem.  Splitting at $p>X^{2/3}$ does not turn congruence into equality:
active primes satisfy only $p\leq X/z$, while $|D-D'|$ can have size
$\asymp X^2$.  Ordinary divisor counting therefore supplies no missing
$1/\log L$ gain in the super-polylogarithmic range.

### 42.5 Exact finite companion and verdict

**Computational 42.6 (exact finite scope).**  `verify.py (ao)` independently
rebuilds the §40 toy reduced systems, then obtains every endpoint incidence
both from retained $(M,D)$ atoms and from the unique residue (42.1).  It
checks (42.5)--(42.8), the exact per-prime collision count, the mass bound
$t_p\leq\kappa_{\max}K_p/(pz)$, and endpoint Parseval in
$\mathbb Q(\zeta_7)$.  The default exact census is

$$
\begin{array}{c|c|r|l|c|c}
X&z&\sum_pK_p&(p:K_p/C_p)&\mathcal V_X^{\rm end}&
 \mathcal V_{X,\rm diag}^{\rm end}\\ \hline
80&2&25&3:5/10,\ 5:8/9,\ 7:2/0,\ 11:6/0,\ 13:4/0
 &54609/67600&49211/135200\\
120&3&59&5:14/23,\ 7:13/22,\ 11:6/0,\ 17:12/4,\ 19:14/0
 &2371407/5216450&17395877/83463200\\
200&5&51&7:11/15,\ 11:14/8,\ 13:14/4,\ 17:12/4
 &150469/781456&71765/781456
\end{array}                                                  \tag{42.28}
$$

Here $C_p$ counts unordered off-diagonal same-residue pairs; the block also
prints the trivial comparator $\binom{K_p}{2}$.  `ES_FULL_SCAN=1` extends
the same streaming, residue-bucket computation to $X=400,800$ without
forming a Cartesian incidence array.  These finite collision counts verify
the identities only; they are not evidence for an asymptotic estimate.

**Assessment 42.7 (wave-14 verdict).**  The endpoint is now exact at the
$(p,R,s)$ and complementary-divisor levels.  Its literal diagonal and every
equal-integer-shift off-diagonal are removed; every fixed squarefree fibre,
including $s=1$, is $o(\Lambda^2)$, and every fixed polylogarithmic prime
range satisfies the target.  The remaining moving-$s$ collisions at
$L^B<p\leq X/z$ are not bounded by unique-cofactor counting, nonzero
divisibility, or an unweighted quadratic Gauss sum.  (Wave-15 update:
Theorem 45.9 closes, by cell injectivity, every fibre with
$m=4c^2s\leq W_0\asymp L^3/(\log L)^2$ uniformly over the whole prime
range; the open core is the complementary range $m>W_0$.)  Therefore
(40.19) and, by Corollary 40.4, (37.27) remain **OPEN**.  Independently, even
a proof of (40.19) would still leave (33.16) and the refutation of
$H_{\rm PF}'$ **OPEN**.  Section 47 refutes the literal hierarchy (40.28)
and raw-$H$ factorial moment (37.19); §49 refutes the replacement (47.16)
and the reduced moment bound.  (wave-17 update)

## 43. General numerators: the multiplier identity is m-uniform and the exceptional-set machinery transfers

**Status and three layers.**  Throughout this section \(m\geq3\) is an
integer.  Layer 1 is a complete replay of §16 at the same internal level of
rigour; because its logarithmic factor would improve the published general-
\(m\) benchmark, its external status is still **CLAIMED/PROVISIONAL** pending
referee and priority checks.  Layer 2 inherits Theorem 34.8 and all three
maximum-severity qualifications in §39.7, and is therefore explicitly
**CLAIMED/PROVISIONAL**.  Layer 3 is a transcription and comparison with
Pomerance--Weingartner (PW) 2025.  No assertion below promotes Theorem 39.7
from its existing provisional status.

Write

\[
 E_m(N)=\#\{n\leq N:m/n\hbox{ is not a sum of three positive unit
 fractions}\}.                                             \tag{43.1}
\]

This is a property of the rational number, not of a chosen numerator and
denominator.  Thus, if \(d=(m,n)\), the statements for \(m/n\) and
\((m/d)/(n/d)\) are identical.  We nevertheless retain the unreduced pair
\((m,n)\) in (43.1), because that is the convention in PW and in the
exceptional-set count.

### 43.1 Layer 1: the identity and the fixed-polylogarithmic machine

**Lemma 43.1 (general-numerator multiplier identity; proved).**  Let
\(k,\ell\geq1\), suppose \(k\ell\equiv-1\pmod m\), and put

\[
 A={k\ell+1\over m}=uvw.                                   \tag{43.2}
\]

If \(n>0\), \(nv\equiv-u\pmod {k\ell}\), and
\(s=(nv+u)/(k\ell)\), then \(s\) is a positive integer and

\[
 {m\over n}={1\over suw}+{1\over nsvw}+{1\over nuvw}.      \tag{43.3}
\]

Moreover \((A,k\ell)=1\), so \(v\) is invertible modulo \(k\ell\).

*Proof.*  The congruences give the two integrality assertions, and positivity
is immediate.  On the common denominator \(nsuvw\), the numerator on the
right of (43.3) is
\(nv+u+s=sk\ell+s=s(k\ell+1)=smuvw\).  Finally any common divisor of
\(A\) and \(k\ell\) divides \(mA-k\ell=1\).  This also shows that no
primality, parity, or coprimality condition involving \(m\) and \(n\) was
used. \(\square\)

For a prime \(\ell\nmid m\), (43.2) forces
\(k\equiv-\ell^{-1}\pmod m\).  In particular, when \(m=4\) and
\(\ell\equiv3\pmod4\), this is precisely the old condition
\(k\equiv1\pmod4\).  It is useful to record exactly what this thinning
costs.  Put

\[
 \eta_1(m)=\prod_{p\mid m}{p\over p+1},\qquad
 \eta_2(m)=\prod_{p\mid m}{p^2\over p^2+p-1},              \tag{43.4}
\]

and

\[
 C_2=\prod_p(1-p^{-1})\left(1+{p-1\over p^2}\right)>0.     \tag{43.5}
\]

**Lemma 43.2 (exact multiplier local factors; proved).**  For fixed \(m\)
and every reduced residue \(r\pmod m\), as \(K\to\infty\),

\[
 \begin{split}
 \sum_{\substack{k\leq K\\k\equiv r\ (m)}}{\varphi(k)\over k^2}
   &\sim {\eta_1(m)\over\varphi(m)\zeta(2)}\log K,\\
 \sum_{\substack{k\leq K\\k\equiv r\ (m)}}
       {\varphi(k)^2\over k^3}
   &\sim {C_2\eta_2(m)\over\varphi(m)}\log K.             \tag{43.6}
 \end{split}
\]

After summing over the \(\varphi(m)\) reduced classes, the factors
\(1/\varphi(m)\) disappear.  Uniformly when \(\log m=O(\log K)\), the
corresponding sums with \((k,m)=1\) are, up to absolute constants depending
only on the constant in that \(O\)-term, respectively
\(\eta_1(m)\log K\) and \(\eta_2(m)\log K\).  The local products satisfy

\[
 {\varphi(m)\over m}\leq\eta_1(m)\leq
 \zeta(2){\varphi(m)\over m},\qquad
 \eta_2(m)\asymp {\varphi(m)\over m},                     \tag{43.7}
\]

with absolute constants.

*Proof.*  For the first sum use
\(\varphi(k)/k=\sum_{d\mid k}\mu(d)/d\), or equivalently the Euler
series \(\zeta(s+1)/\zeta(s+2)\).  Removing integers divisible by
\(p\mid m\) deletes the local factor \(1+1/p\), giving
\(p/(p+1)\).  Orthogonality of characters modulo \(m\) divides the
principal residue by \(\varphi(m)\); every nonprincipal series has no pole
at \(s=0\).  For the second sum put \(b(k)=(\varphi(k)/k)^2\).  Its local
harmonic factor is

\[
 1+\sum_{e\geq1}{(1-p^{-1})^2\over p^e}
   =1+{p-1\over p^2}.                                     \tag{43.8}
\]

Deleting it gives the second product in (43.4), while multiplication by
\(1-1/p\) at every prime gives (43.5).  Standard partial summation of these
absolutely convergent pole quotients proves (43.6).  The same convolution
argument, without characters, gives the stated uniform two-sided estimates
for the aggregate coprime sums.  Finally
\(\eta_1/(\varphi(m)/m)=\prod_{p\mid m}p^2/(p^2-1)\), and
\(\eta_2/(\varphi(m)/m)=
\prod_{p\mid m}p^3/(p^3-2p+1)\); both comparison products converge.
\(\square\)

**Character-uniformity clarification (wave-15 review repair).**  The
fixed-class asymptotics in (43.6) are only fixed-\(m\) statements: after
character orthogonality, the principal character supplies the displayed
pole and every nonprincipal twist is regular there.  No bound for those
regular values, effective or otherwise, is used uniformly in \(m\); in
particular a possible exceptional real character cannot affect the proof
below.  The fixed-class asymptotics are not claimed uniformly when \(m\) is
comparable with or exceeds \(K\): the class \(1\pmod m\), for example, then
retains the exceptional term \(k=1\).  The proofs below use only the
aggregate condition \((k,m)=1\), obtained directly from the nonnegative
Euler/convolution sum, not pointwise equidistribution among short classes.

The following identity is the clean way to keep the prime-progression factor
explicit.  Define the multiplicative function

\[
 F_m(p^a)=\begin{cases}1,&p\mid m,\\p/(p-1),&p\nmid m.
             \end{cases}
\]

If \((u,v)=1\), then exactly

\[
 {1\over\varphi(muv)}={F_m(u)F_m(v)\over\varphi(m)uv}.     \tag{43.9}
\]

In particular the lower box estimate may use \(F_m\geq1\), while the upper
estimate uses \(F_m(n)\leq n/\varphi(n)\), the function already treated in
(16.5b)--(16.5g).  This avoids both an erroneous extra factor \(1/m\) and
an erroneous assumption \((uv,m)=1\).

**Lemma 43.3 (general-\(m\) class mass; proved).**  Fix \(B>0\).  Let
\(K_0\leq K\leq(\log X)^B\), \(H=K^{10}\), and
\(m\leq(\log X)^B\).  Let
\(\mathcal J\subseteq\{k\leq K:(k,m)=1\}\) contain 1, put
\(h(\mathcal J)=\sum_{k\in\mathcal J}\varphi(k)/k^2\), and suppose
\((c,L_{\mathcal J})=1\).  For primes
\(X^{1/2}<\ell\leq X\), let \(f_{m,c}(\ell)\) count the distinct residues
\(-uv^{-1}\pmod\ell\) furnished by

\[
 \begin{gathered}
 k\in\mathcal J,\quad H<u,v\leq\ell^{1/3},\quad
 (u,v)=(uv,k)=1,\quad \omega(uv)\leq D\log\log X,\\
 muv\mid k\ell+1,\qquad k\mid u+cv .                       \tag{43.10}
 \end{gathered}
\]

**Notation note (wave-15 review repair).**  A stray non-TeX token before
\(H\) was deleted; no condition changed.

Then, with constants depending only on \(B\),

\[
 { (\log X)^2h(\mathcal J)\over\varphi(m)}
 \ll\sum_{X^{1/2}<\ell\leq X}{f_{m,c}(\ell)\over\ell}
 \ll { (\log X)^2h(\mathcal J)\over\varphi(m)}.            \tag{43.11}
\]

Every counted residue, together with the congruence modulo \(k\), is a
forced class from Lemma 43.1.

*Proof.*  Here is the complete change ledger from Lemmas 16.2--16.3.
For each fixed \(k\), the box congruence remains
\(u+cv\equiv0\pmod k\); hence (16.4), its boundary ratio
\(O(K^2/H)\), the low-\(\omega\) Rankin truncation, and Shiu's modulus
condition \(k<U^{1/2},V^{1/2}\) are unchanged.

**Pairing/modulus ledger (wave-15 review repair).**  The constraint
\(k\equiv-\ell^{-1}\pmod m\) is not an extra congruence on \(u,v\) inside
that fixed-\(k\) lattice count.  After \((k,u,v)\) is fixed it is carried by
the single prime progression (43.12).  Equivalently, fixing an
\(\ell\)-class would select one reduced \(k\)-class, but the proof sums the
aggregate nonnegative family \((k,m)=1\) and never invokes equidistribution
of \(k\) among short classes.

For fixed \((k,u,v)\), divisibility is the single reduced prime progression

\[
 \ell\equiv-k^{-1}\pmod {muv}.                             \tag{43.12}
\]

It is the product modulus \(muv\), not \(\operatorname {lcm}(m,uv)\),
because the condition is literally \(muv\mid k\ell+1\).  This also settles
the potentially ramified case: no assumption \((m,uv)=1\) is made, and if
one splits (43.12) into congruences modulo \(m\) and modulo \(uv\), their
compatibility is automatic because both come from divisibility by their
product.  When \(m\) is even, \((k,m)=1\) makes both \(k\) and the reduced
residue \(-k^{-1}\pmod {muv}\) odd; common powers of 2 in \(m\) and \(uv\)
are already present with their summed exponent in \(muv\).  Thus no
spurious CRT step through \(\operatorname {lcm}(4uv,m)\) occurs.

In the lower dyadic boxes \(uv\leq x^{1/3}\); since \(m\) is a fixed log
power, \(muv\) lies below the Bombieri--Vinogradov level.  A fixed modulus
has at most \(K2^{\omega(uv)}\) descriptions, exactly as in (16.9a).
Taking the BV logarithmic saving larger by \(B\) absorbs both this
multiplicity and the main-term factor \(1/\varphi(m)\).  Brun--Titchmarsh
gives the upper bound with the same modulus.  Formula (43.9), (16.2), and
(16.3) then give the two sides of (43.11).  Shiu's auxiliary modulus remains
\(k\): there is no condition \((uv,m)=1\) to encode there.  The
\(m\)-dependence is instead exactly in \(F_m\) and in the later prime
modulus \(muv\).  (This last distinction is a wave-15 review repair.)

It remains to check deduplication.  A collision at one \(\ell\) gives
\(\ell\mid uv'-u'v\), while \(|uv'-u'v|<\ell^{2/3}<\ell\); reducedness
therefore gives \((u,v)=(u',v')\).  Both atoms then say
\(k\ell\equiv k'\ell\equiv-1\pmod {muv}\).  Since
\((\ell,muv)=1\), this fixes \(k\pmod {muv}\), and
\(muv>mH^2>K\) makes \(k=k'\).  Thus neither \(z^2<\ell\) nor the
cross-multiplier size argument used \(m=4\).  Finally
\(n\equiv c\pmod {L_{\mathcal J}}\) and a hit modulo \(\ell\) combine to
\(nv\equiv-u\pmod {k\ell}\), exactly as in §16.3. \(\square\)

**Theorem 43.4 (Layer-1 exceptional set; complete internal proof,
CLAIMED/PROVISIONAL externally).**  For every fixed \(m\geq3\) there is an
absolute \(c_0>0\) such that, for all sufficiently large \(N\),

\[
 E_m(N)\ll_m N\exp\left\{-c_0
 \left({\eta_1(m)\over\varphi(m)}\right)^{1/3}
 (\log N)^{2/3}(\log\log N)^{1/3}\right\}.                 \tag{43.13}
\]

The prime-denominator and all-denominator versions of the same formula are
uniform, for every fixed \(\epsilon>0\), in the range
\(3\leq m\leq(\log N)^{2-\epsilon}\), after increasing the lower
threshold for \(N\) in terms of \(\epsilon\).  The matching all-denominator
range is a wave-16 review repair.

*Proof.*  Take \(K=\lfloor\delta\log N\rfloor\), use all
\(k\leq K\) coprime to \(m\), and put
\(M_0=\operatorname {lcm}_{k\leq K,(k,m)=1}k\).  The elementary bound
\(\log M_0\leq(1+o(1))K\) makes every reduced subsequence have length
\(N^{1-O(\delta)}\).  Apart from the \(O(\log m)\) primes dividing \(m\),
every prime denominator above \(K\) lies in one of these reduced
subsequences.  Lemmas 43.2--43.3 give, uniformly in its residue \(c\),
prime-class mass
\(\asymp\lambda_m(\log X)^2\log K\), where
\(\lambda_m=\eta_1(m)/\varphi(m)\).  The upper mass has the same factor,
by (43.9), so the Rankin truncation in the larger sieve closes with

\[
 \log X=\alpha\left({\log N\over
                   \lambda_m\log\log N}\right)^{1/3}.      \tag{43.14}
\]

Equations (16.14) and (43.11) now give the exponent in (43.13).  In the
stated uniform range, \(\log X=o(\log N)\), while \(K,m\) are fixed powers
of \(\log X\); this verifies respectively the sieve-length and
BV/Shiu level requirements.  The BV saving is chosen in terms of
\(\epsilon\), not of \(m\).

For all denominators, if \(a\mid n\) and the rational number \(m/a\) has a
three-unit-fraction representation, multiplying its three denominators by
\(n/a\) represents \(m/n\).  Hence every divisor of an exceptional \(n\)
is exceptional, and in particular every prime factor is an exceptional
prime denominator.  The Rankin--semigroup proof of Theorem 16.5 applies
with

\[
 g_m(u)=\lambda_m^{1/3}u^{2/3}(\log u)^{1/3}.               \tag{43.15}
\]

The finitely many omitted primes contribute only \(O_m(1)\) to the Euler
product.  For the uniform all-denominator transfer, put
\(\Theta_1=\varphi(m)/\eta_1(m)\asymp m\), fix the final margin
\(0<\epsilon_0<2\), choose
\(0<\epsilon'<\epsilon_0/(3-\epsilon_0)\), and, after a harmless fixed
constant enlargement, start the uniform prime estimate at
\[
 \log x_0\asymp\Theta_1^{1/(2-\epsilon')}.
\]
The Rankin parameter is
\(\delta\asymp\Theta_1^{-1/3}L^{-1/3}(\log L)^{1/3}\).  Uniformly for
\(\Theta_1\ll L^{2-\epsilon_0}\),
\[
 \delta\log x_0
 \ll L^{-1/3}(\log L)^{1/3}
       \Theta_1^{1/(2-\epsilon')-1/3}
 \ll L^{-\gamma}(\log L)^{1/3}=o(1),
 \quad
 \gamma={\epsilon_0(1+\epsilon')-3\epsilon'
          \over3(2-\epsilon')}>0.
\]
Thus all smaller primes, even if declared exceptional, cost only
\(\exp\{O(\log\Theta_1)\}\).  This is absorbed by the saving
\(\gg\Theta_1^{-1/3}L^{2/3}(\log L)^{1/3}\).  Above \(x_0\), partial
summation is uniform: (43.15) divided by its argument is decreasing, and
\(g_m(\log x_0)\) is a positive power of \(\Theta_1\) when \(m\) grows
(the bounded case is the fixed-\(m\) argument).  This proves (43.13) for
(43.1), including unreduced pairs, throughout
\(m\leq L^{2-\epsilon_0}\).  \(\square\)

**Layer-1 range correction (wave-16 review repair).**  The former
all-denominator range \(m\leq L^{1-\epsilon}\) was safe but conservative.
The displayed cutoff pays the small-prime Euler product and proves the same
\(L^{2-\epsilon}\) range as the prime theorem; no new prime-distribution
input is used.

The local factor is explicit: since \(\eta_1(m)\asymp\varphi(m)/m\), the
coefficient in (43.13) is \(\asymp m^{-1/3}\).  The logarithmic
\((\log\log N)^{1/3}\) gain over PW is the new multiplier mass; it is not
being hidden inside an \(m\)-dependent constant.

### 43.2 Layer 2: the provisional cubic transfer

Fix \(0<\kappa<1/240\), put \(t=\log X\),
\(K=\lfloor X^\kappa\rfloor\), and \(H=K^{10}\).  The general-numerator
c-free atom family consists of

\[
 A=(k,\ell,u,v),\quad k\leq K,\quad(k,m)=1,
 \quad H<u,v\leq x^{1/6},\quad x<\ell\leq2x,               \tag{43.16}
\]

with the same coprimality and low-\(\omega\) restrictions as (39.3), and

\[
 muv\mid k\ell+1,
 \qquad E_A=\{n:n\equiv-uv^{-1}\pmod {k\ell}\}.           \tag{43.17}
\]

The dyadic blocks range over \((X^{1/2},X]\).

**Lemma 43.5 (general-\(m\) c-free deduplication; proved).**  A hit of
(43.17) implies \(k\mid u+nv\), so after revealing
\(c\equiv n\pmod {L_{m,K}}\), where
\(L_{m,K}=\operatorname {lcm}_{k\leq K,(k,m)=1}k\), the coupling
\(k\mid u+cv\) is automatic.  Distinct compatible atoms have distinct
\(\ell\)'s, and a compatible set has exact density

\[
 {1\over\operatorname {lcm}(k_1,\ldots,k_j)
          \prod_{i\leq j}\ell_i}.                          \tag{43.18}
\]

*Proof.*  The coupling is reduction of (43.17) modulo \(k\).  At a common
\(\ell\), the \(z^2<\ell\) argument in Lemma 43.3 makes \((u,v)\) common;
then \(k\ell\equiv-1\pmod {muv}\), together with \(muv>K\), makes \(k\)
unique.  CRT gives (43.18).  These are exactly the two size inequalities
which were potentially sensitive to replacing 4 by \(m\), and both become
no weaker. \(\square\)

For \(g\mid k\) and a reduced \(a\pmod g\), define \(W_{k,a}(g)\) and
\(W_k\) as in (39.6), using (43.16)--(43.17).

**Lemma 43.6 (general-\(m\) mass profiles; proved at the §39.2 level,
provisional with §39).**  Uniformly for \(m\leq t^B\), with constants
allowed to depend on fixed \(B\),

\[
 W_{k,a}(g)\ll {t^2\over\varphi(m)\varphi(g)}
                  {\varphi(k)^2\over k^3},\qquad
 W_k\asymp {t^2\over\varphi(m)}{\varphi(k)^2\over k^3}.     \tag{43.19}
\]

Consequently

\[
 \mu_{m,X}:=\sum_A{1\over k_A\ell_A}
   \asymp {C_2\eta_2(m)\over\varphi(m)}t^2\log K
   \asymp {\eta_2(m)\over\varphi(m)}t^3.                   \tag{43.20}
\]

*Proof: the Shiu step in full.*  Formula (43.9) extracts
\(1/\varphi(m)\).  In boxes \(u\asymp U,v\asymp V\), set
\(q_0=\operatorname {lcm}(g,\operatorname {rad}k)\).  Since
\((k,m)=1\), the number of compatible reduced class pairs modulo \(q_0\)
is still \(\varphi(q_0)^2/\varphi(g)\).  Apply Shiu to \(F_m\): it has
\(F_m(p^a)=1\) for \(p\mid m\), \(p/(p-1)\) otherwise, is bounded above
by the old function \(n/\varphi(n)\), and \(q_0\leq k<U^{1/10},V^{1/10}\).
Thus the derivation of (39.11) gives

\[
 \sum_{\mathrm{boxes}}{F_m(u)F_m(v)\over uv}
 \ll {t^2\over\varphi(g)}\left({\varphi(k)\over k}\right)^2.\tag{43.21}
\]

Brun--Titchmarsh now uses \(muv\), not \(4uv\), and proves the upper
profile.  For the lower profile, BV applies because
\(muv\leq t^B x^{1/3}\).  Replacing \(n/\varphi(n)\) by \(F_m(n)\) changes,
at a prime \(p\mid m\), the coprime-pair Euler factor by exactly

\[
 {1+2/(p-1)\over1+2p/(p-1)^2}={p^2-1\over p^2+1}.          \tag{43.22}
\]

The product of (43.22) over any set of primes is bounded above and below by
absolute positive constants.  Hence the lower profile retains the same
\((\varphi(k)/k)^2\) order.  The low-\(\omega\) Rankin deletion and the
allocation multiplicity are unchanged.  Summing (43.19) and applying the
second formula of Lemma 43.2 proves (43.20). \(\square\)

**Provisional Theorem 43.7 (general-\(m\) pruned cubic prime slice;
inherits Theorem 34.8).**  For fixed \(B\), uniformly for \(m\leq t^B\)
and subfamilies \(\mathcal J\subseteq\{k\leq K:(k,m)=1\}\) containing 1,
with \((c,L_{\mathcal J})=1\), the low-congestion restriction
\(r_{\mathcal J}(u,v;c)\leq t^4\) leaves

**Quantifier note (wave-15 review repair).**  The omitted reduced-fibre
quantifier was restored.

\[
 \sum_{X^{1/2}<\ell\leq X}{f^{\rm good}_{m,c}(\ell)\over\ell}
 \asymp {t^2h(\mathcal J)\over\varphi(m)}.                 \tag{43.23}
\]

For the full coprime multiplier family this is
\(\asymp\eta_1(m)t^3/\varphi(m)\).

*Proof ledger.*  Lemma 34.7 is unchanged after restricting its outer set to
\((k,m)=1\): it concerns only \(k\mid u+cv\), and its lcm boundary is still
at most \(K^2\).  The high-incidence harmonic mass in (34.20) is therefore
\(o(t^2h(\mathcal J))\).  Formula (43.9) turns the retained harmonic mass
into at least \(1/\varphi(m)\) times that amount.  The retained modulus
multiplicity remains \(2^{\omega(uv)}t^4\).  Ordinary BV now runs over
\(q=muv\leq t^Bx^{1/3}\); choosing its fixed logarithmic saving larger by
\(B\) makes its error \(o(x\log x\,h(\mathcal J)/\varphi(m))\).
Distinctness is Lemma 43.5 and the upper bound is Lemma 43.6.  These are all
places where \(m\) enters the proof of Theorem 34.8.  The theorem remains
provisional because Theorem 34.8 does. \(\square\)

We next check the most dangerous combinatorial step rather than saying only
that §39 applies verbatim.  Condition on \((n,P_y)=1\), retain the definitions
of \(q_y(k)\) and \(b_y(g)\) from (39.13), and let \(R\) be the previous
multiplier lcm.  Adding a compatible atom still multiplies density by

\[
 {q_y(k)\over k\ell}b_y((k,R)).                             \tag{43.24}
\]

Compatibility fixes one unit residue modulo \(g=(k,R)\); (43.19) supplies
\(1/\varphi(g)\).  Hence, prime power by prime power,

\[
 {b_y(g)\over\varphi(g)}=
 \prod_{p\mid g,\ p>y}{p\over p-1}.                        \tag{43.25}
\]

Primes dividing \(m\) never divide \(k\), so they create no missing case in
this cancellation.  At every remaining modified prime the nonconstant local
mass \((p-1)/p^2\) again becomes \(1/p\), and the quotient is
\(1+O(p^{-2})\).  **Local-factor correction (wave-15 review repair).**
If \(p\mid m\) is unmodified, deleting its local factor contributes
\(p^2/(p^2+p-1)\), the \(p\)-factor of \(\eta_2\).  If it is modified
because \(p\leq y\) (the \(p\mid R\) case cannot occur), deletion instead
contributes \(p/(p+1)\), the smaller \(p\)-factor of \(\eta_1\).  Hence the
total deletion factor is at most \(\eta_2(m)\), not always exactly equal to
it.  This is the direction required for the following upper bound:

\[
 \sum_{\substack{k\leq K\\(k,m)=1}}
 {\varphi(k)^2\over k^3}q_y(k)
 \prod_{p\mid(k,R),\ p>y}{p\over p-1}
 \ll\eta_2(m)\log K,                                      \tag{43.26}
\]

and the ordered induction proves

\[
 \mathbb E(H_{m,X})_j\leq
 \left(C{\eta_2(m)\over\varphi(m)}t^3\right)^j
 \leq(Ct^3)^j.                                             \tag{43.27}
\]

This is the exact (39.14)--(39.15) collapse-versus-consistency replay,
including unequal prime-power exponents.

**Theorem 43.8 (Layer-2 exceptional set; CLAIMED/PROVISIONAL).**  For every
fixed \(m\geq3\), and uniformly for each fixed \(\epsilon>0\) in
\(3\leq m\leq(\log N)^{3/4-\epsilon}\),

\[
 E_m(N)\ll N\exp\left\{-c_0{\eta_1(m)\over\varphi(m)}
                         (\log N)^{3/4}\right\}.            \tag{43.28}
\]

This includes exceptional primes and all exceptional denominators, but it
inherits the provisional status of Theorems 34.8 and 39.7.

*Proof: void and ledger absorption.*  Reveal the multiplier coordinates and
use
\(\mathcal J_c=\{k\leq K:(k,m)=(k,c)=1\}\).  Its full harmonic mass is
\(\asymp\eta_1(m)\log K\).  With
\(Z(c)=\sum_{y<p\leq K,p\mid c,\ p\mid L_{m,K}}1/p\), the argument of
(39.25) gives \(\Pr(Z>C\eta_1(m))\leq
\exp\{-c\eta_1(m)y\}\).  Take, conservatively and exactly as in §39,

\[
 y=Bt^3,\qquad r=\hbox{the least even integer at least }D_Bt^3.\tag{43.29}
\]

On the good fibres, Theorem 43.7 gives active \(\ell\)-mass
\(\gg\eta_1(m)t^3/\varphi(m)\).  The bad-fibre tail is smaller, and
(43.27) controls the Bonferroni tail.  Thus

\[
 \mathbb E_{\rm CRT}\{S_yQ_r(H_{m,X})\}
 \leq\exp\left\{-c{\eta_1(m)\over\varphi(m)}t^3\right\}.    \tag{43.30}
\]

For the ledger, \(m\leq t^B\) and (43.16) give
\(\log|\mathcal A_{m,X}|=O_B(t)\).  Exactly as in
(39.31)--(39.34),

\[
 \deg=O(t^3),\quad \log d_{\rm term}=O_B(t^4),\quad
 \log\sum|c_{\rm term}|=O_B(t^4).                          \tag{43.31}
\]

This explicitly absorbs the extra \(\log m\): it is \(O_B(\log t)\) per
atom and hence smaller than the existing \(O(t)\) charge.  Choosing
\(t=\alpha(\log N)^{1/4}\) and then \(\alpha\) small makes every rounding
error negligible and proves the prime form of (43.28).  In the uniform
range the exponent tends to infinity (use
\(\eta_1(m)\asymp\varphi(m)/m\)), and \(m\leq t^{3-4\epsilon}\), so all
prime-slice uniformity assumptions hold.  For the semigroup transfer, start
the uniform prime estimate at
\(x_0=\exp\{m^{1/(3/4-\epsilon/4)}\}\).  **Uniformity correction
(wave-15 review repair).**  With
\(\delta\asymp \eta_1(m)\varphi(m)^{-1}(\log N)^{-1/4}\) and
\(m\leq(\log N)^{3/4-\epsilon}\), (43.7) gives
\[
 \delta\log x_0
 \ll (\log N)^{-\epsilon^2/(3-\epsilon)}=o(1).
\]
(The former denominator \(3/4-\epsilon/2\) makes this exponent positive
and did not justify the printed claim.)  Declaring every smaller prime
exceptional therefore costs only \(m^{O_\epsilon(1)}\), absorbed by the
\(\gg(\log N)^\epsilon\) saving.  Above \(x_0\), the prime-bound tail is
uniformly summable because
\(m^{-1}(\log x_0)^{3/4}=m^{(\epsilon/4)/(3/4-\epsilon/4)}\to\infty\).
The argument after (43.15), now with
\(g(u)=\eta_1(m)\varphi(m)^{-1}u^{3/4}\), transfers the prime result.
\(\square\)

**Failure log 43.9 (what is not being claimed).**

1. Theorem 43.8 deliberately keeps the §39 choices \(y,r\asymp t^3\).
   It remains a valid conservative replay, but the shrinking-window audit is
   now completed in Theorem 43.12 and gives a stronger provisional theorem.
2. The fixed-class asymptotic (43.6) is not uniform for \(m\gtrsim K\).
   The aggregate proof avoids this issue; it would be incorrect to infer
   pointwise per-\(\ell\)-class mass in that range.
3. The range \(m\leq(\log N)^{3/4-\epsilon}\) is the nontrivial range of
   the unoptimized replay (43.28).  The optimized theorem has the larger
   range \(m\leq(\log N)^{3-\epsilon}\); no nontrivial uniform assertion is
   made at the limiting scale \(m\asymp(\log N)^3\) or beyond.  These are
   analytic uniformity limits, not failures of the algebraic identity.

**Wave-16 provenance note (adjudicated).**  The frozen blind construction
identified a finite relative-mass inequality which removes the first
limitation above.  The complete argument, its honest range, and its inherited
provisional qualifications are stated in Theorem 43.12 after the blindness
attestation.  Theorem 43.8 is retained as the conservative direct replay,
not silently rewritten.

### 43.3 Layer 3: the PW benchmark and the two regimes

**Literature benchmark (PW 2025, Theorem 1.3, transcribed).**  There is an
absolute constant \(C>0\) such that, for every pair \(m,N\) with
\(4\leq m\leq(\log N)^2\),

\[
 E_m(N)\leq {N\over
 \exp\{C((\log N)^2/\varphi(m))^{1/3}\}}.                  \tag{43.32}
\]

Their §4 defines \(f_m(p)\) only for primes \(p\equiv-1\pmod m\), proves
\(\sum_{p\leq x}f_m(p)/p\asymp(\log x)^2/\varphi(m)\) by
Brun--Titchmarsh and Bombieri--Vinogradov, and then applies the same
larger-sieve Rankin truncation used in §16.  Thus their exponent is
\((\log N)^{2/3}/\varphi(m)^{1/3}\), with no suppressed
\(\log\log N\) factor.

**PW crossover correction (wave-16 review repair).**  For the optimized
thinned-window Layer 2 of Theorem 43.12, compare

\[
 R=\left({\eta_2(m)\over\varphi(m)}\right)^{1/4}L^{3/4}
 \quad\hbox{and}\quad
 P={L^{2/3}\over\varphi(m)^{1/3}},
 \qquad L=\log N.                                          \tag{43.33}
\]

The exact scale ratio and crossover are

\[
 {R\over P}=\{\eta_2(m)^3\varphi(m)L\}^{1/12},
 \qquad
 R\geq P\ \Longleftrightarrow\
 L^{1/12}\geq {1\over\varphi(m)^{1/3}}
                 \left({\varphi(m)\over\eta_2(m)}\right)^{1/4}
 \ \Longleftrightarrow\
 L\geq{1\over\eta_2(m)^3\varphi(m)}.                      \tag{43.34}
\]

These are exponent-scale comparisons; unknown absolute constants prevent a
literal finite crossover.  The honest regimes are now different from the
conservative replay.  Throughout the common stated domain with PW
(\(4\leq m\leq L^2\)), the provisional Layer-2 scale is larger once
(43.34) holds; for every fixed \(m\) it eventually does.  The optimized
provisional theorem is available farther, through every fixed-gap range
\(m\leq L^{3-\epsilon}\), where PW's quoted theorem is not stated once
\(m>L^2\).  At \(m\asymp L^3\) the new saving ceases to grow, so no
uniform record claim is made there or beyond.  PW is a literature theorem,
whereas Theorem 43.12 remains internally **CLAIMED/PROVISIONAL**; a larger
formal exponent does not erase that evidentiary distinction.

The Layer-1 prime and all-denominator bounds are now both uniform through
\(m\leq L^{2-\epsilon}\) (wave-16 review repair).  Relative to PW their
exponent ratio is \((\eta_1(m)\log L)^{1/3}\), so even that comparison
retains the displayed local factor rather than suppressing it.

**Computational 43.10 (finite companion only).**  `verify.py (ap)` simplifies
(43.3) symbolically and checks it with exact `Fraction` arithmetic on 364
random instances for
\(m\in\{3,5,6,7,8,12,25\}\), explicitly including even and composite
\(n\) and instances with \((m,n)>1\).  Its \(m=5\) atom census verifies
divisibility, atom-implied coupling, direct modulus-class and fixed-\(\ell\)
deduplication, the distinct-large-coordinate claim, and cases with
\((m,uv)>1\), without allocating a Cartesian array.  (wave-15 review repair)
Finally it compares finite
multiplier sums with the exact \(\eta_2(m)\) formula in (43.4).  Those
finite ratios are informational; they do not prove (43.6) or any asymptotic
theorem.

### 43.11 Wave-16 blind parallel construction (attestation)

Unit J16 independently rebuilt S1--S7 after reading only the instructed
§16, §34, §39 ranges and all of `sources/pw.txt`; its exact read commands
are logged in `blind43.md`.
The blind derivation was frozen before opening §43 or its review at commit
`a0bd2940c322cb69426cf83df7f903d563b49648`.

| item | comparison verdict |
|---|---|
| S1 identity | **CONVERGED** |
| S2 supply/local factors | **CONVERGED** on the aggregate factors and pairing (the fixed-class short-range scope is governed by §43's clarification) |
| S3 Layer 1 | **DIVERGED-MINOR** (same prime theorem; the stronger all-denominator range closes only after the post-freeze cutoff repair) |
| S4 c-free atoms | **CONVERGED** |
| S5 mass profile | **CONVERGED** |
| S6 moments/void | **DIVERGED-SUBSTANTIVE** (the thinned degrees close after the finite relative-mass inequality and the wave-15 mixed-factor correction) |
| S7 assembly/crossover | **DIVERGED-SUBSTANTIVE** (the optimized provisional exponent and range are stronger) |

The wave-15 mixed local-factor repair is correct: at conditioned
\(p\mid m\) deletion gives \(p/(p+1)\), but the upper bound (43.26) survives.
The blind file's post-freeze finite inequality and corrected semigroup
cutoffs are the inputs adjudicated below; its frozen S3 cutoff and exact
local-deletion sentence are not treated as converged.  As in §41, git records
the text, freeze, and ordering only: blindness is a self-attestation enforced
by instruction and read log, not a cryptographic or independently audited
guarantee, and this check does not upgrade §39.

**Theorem 43.12 (thinned-window Layer 2; CLAIMED/PROVISIONAL;
wave-16 review strengthening).**  Put \(L=\log N\).  For every fixed
\(\epsilon>0\), uniformly for
\(3\leq m\leq L^{3-\epsilon}\),
\[
 E_m(N)\ll_\epsilon N\exp\left\{-c_\epsilon
 \left({\eta_2(m)L^3\over\varphi(m)}\right)^{1/4}\right\}. \tag{43.35}
\]
The same formula holds for exceptional primes.  It inherits Theorem 34.8,
Theorem 43.7, and every maximum-severity qualification in §39.7; the
wave-16 adjudication changes the exponent and uniform range, not the
external status.

*Proof.*  Write
\[
 \theta_m={\eta_2(m)\over\varphi(m)},\qquad
 \Theta_m=\theta_m^{-1}\asymp m,\qquad M=\theta_mt^3.
\]
The load-bearing shrinking-window fact is finite, not an asymptotic in a
short progression.  If
\(H_m(K)=\sum_{k\leq K,(k,m)=1}\varphi(k)/k^2\), then for every prime
\(p\nmid m\),
\[
 \begin{split}
 \sum_{k\leq K,(k,m)=1,p\mid k}{\varphi(k)\over k^2}
 &=\sum_{e\geq1}{1-p^{-1}\over p^e}
   \sum_{\substack{a\leq K/p^e\\(a,pm)=1}}{\varphi(a)\over a^2}\\
 &\leq {H_m(K)\over p}.                                    \tag{43.36}
 \end{split}
\]
For \(p\mid m\) the left side is zero, so the inequality remains true.  Reveal the multiplier coordinates,
put \(\mathcal J_c=\{k\leq K:(k,m)=(k,c)=1\}\), and define \(Z(c)\) as
in the proof of Theorem 43.8.  The union bound and (43.36) give
\(h(\mathcal J_c)\geq H_m(K)(1-Z(c))\).  For \(y\geq2\), independence of
the coordinates above \(y\) gives exactly the same Chernoff calculation as
(39.25):
\[
 \mathbb E e^{yZ}\leq
 \exp\left\{Cy\sum_{p>y}p^{-2}\right\}=e^{O(1)},\qquad
 \Pr\{Z>\eta_0\}\leq e^{-\eta_0y+O(1)}                   \tag{43.37}
\]
for a fixed \(0<\eta_0<1\).  Thus the retained multiplier mass is a fixed
fraction of the actual mass \(H_m(K)\asymp\eta_1(m)\log K\); no
\(1/\eta_1(m)\) is lost.

Take \(y\) to be an integer of size \(B_0M\), with \(B_0\) a sufficiently
large absolute constant.  On \(Z\leq\eta_0\), Theorem 43.7 gives active
prime-coordinate mass
\[
 {t^2h(\mathcal J_c)\over\varphi(m)}
 \gg {\eta_1(m)\over\varphi(m)}t^3\asymp M.
\]
The good-fibre void is therefore \(e^{-cM}\), while (43.37) makes the bad
fibres at most \(e^{-cM}\) after increasing \(B_0\).  This is the full
shrinking-\(y\) quarantine audit: the constants are chosen in that order,
and \(y\sum_{p>y}p^{-2}=O(1)\) uniformly.

Equation (43.27) gives every factorial moment the base \(CM\), uniformly in
this \(y\).  Let \(r\) be the least even integer at least \(D_0M\).  For
large enough absolute \(D_0\), Stirling's formula and the even Bonferroni
identity (39.28) give
\[
 \mathbb E_{\rm CRT}\{S_yQ_r(H_{m,X})\}
 \leq e^{-cM}+{(CM)^{r+1}\over(r+1)!}
 \leq e^{-c'M}.                                            \tag{43.38}
\]
The range below makes \(M\to\infty\); a fixed even degree handles bounded
\(M\) without a growing-saving claim.

The exact expansion now has the thinned ledger
\[
 \deg=O(M),\qquad
 \log d_{\rm term}\leq O(y)+r(t+\log K)=O(Mt),\qquad
 \log\sum|c_{\rm term}|=O(rt)=O(Mt).                       \tag{43.39}
\]
Here \(\log K=\kappa t\), \(\log|\mathcal A_{m,X}|=O(t)\), and the atom
modulus is \(k\ell\), not \(mk\ell\); \(m\) selects atoms but adds no
ledger factor.  Hence finite-interval rounding is absorbed once
\[
 L\geq C_0Mt=C_0\theta_mt^4.                               \tag{43.40}
\]
Choose \(t=\alpha(L/\theta_m)^{1/4}\) with fixed sufficiently small
\(\alpha\).  Then
\[
 M\asymp\theta_m^{1/4}L^{3/4},                             \tag{43.41}
\]
which proves the prime exponent in (43.35).

All uniformity constraints have room in the stated range.  Since
\(\Theta_m\asymp m\),
\[
 {t\over L}\asymp\left({\Theta_m\over L^3}\right)^{1/4}
 \ll L^{-\epsilon/4},\qquad
 M\gg L^{\epsilon/4}.
\]
Also \(m\leq t^B\) for one fixed \(B\) (indeed \(B=4\), after harmless
absolute enlargement, suffices), so Theorems 43.6--43.7 apply; the modulus
\(muv\) remains exponentially below the BV level, \(K=e^{\kappa t}\gg m\),
\(2\leq y<X^{1/2}\), and the Lemma-39.3 Euler bound is uniform in the
smaller cutoff.  Smaller \(y\) leaves more primes unconditioned, but
(43.25)--(43.27) already sum their factors uniformly.  Finally
\(\max(m,K,y)=e^{o(L)}\), so the omitted prime range is negligible.

It remains to transfer uniformly to all denominators.  Fix the final margin
\(0<\epsilon_0<3\), choose
\(0<\epsilon'<\epsilon_0/(4-\epsilon_0)\), and, after a harmless fixed
constant enlargement which ensures \(m\leq u_0^{3-\epsilon'}\), start the
prime theorem at
\[
 u_0=\log x_0\asymp\Theta_m^{1/(3-\epsilon')}.
\]
With \(g_m(u)=\Theta_m^{-1/4}u^{3/4}\), Rankin's parameter is
\(\delta\asymp\Theta_m^{-1/4}L^{-1/4}\), and
\[
 \delta u_0
 \ll L^{-1/4}\Theta_m^{1/(3-\epsilon')-1/4}
 \ll L^{-\gamma},\qquad
 \gamma={\epsilon_0(1+\epsilon')-4\epsilon'
          \over4(3-\epsilon')}>0.                          \tag{43.42}
\]
Declaring all primes below \(x_0\) exceptional therefore costs only
\(\exp\{O(\log\Theta_m)\}=e^{o(g_m(L))}\).  Above \(x_0\), partial
summation is uniform because \(g_m(u)/u\) decreases and
\(g_m(u_0)=\Theta_m^{\epsilon'/(4(3-\epsilon'))}\) is a positive power
when \(m\) grows; bounded \(m\) is the fixed-parameter case.  The
Theorem-16.5 semigroup argument now preserves the exponent shape and proves
(43.35) for all denominators. \(\square\)

**Assessment 43.13 (wave-16 hostile-review verdict).**
**STRENGTHENING CONFIRMED**, internally and with the displayed fixed-gap
range.  The finite inequality (43.36) is the missing relative-mass input;
it validates the thinned quarantine, moment degree, \(O(\theta_mt^4)\)
ledger, range \(m\leq L^{3-\epsilon}\), and exponent in (43.35).  The
verdict does not upgrade Theorem 34.8, §39, or this theorem beyond
**CLAIMED/PROVISIONAL**.

## 44. Slice conspiracies: joint vanishing structure of the ray-character mass

**Scope and outcome.**  This section determines exactly when one raw, ordered
\((c,k)\)-summand of Theorem 36.1 vanishes and packages simultaneous
vanishing as an explicit moving-divisor locus.  It also proves a four-family
wrong-grade obstruction that strictly extends Theorem 36.2, recovers one
previously known structured progression on which a slice is always positive,
and exhibits an exact two-slice counterexample to determination by the
natural fixed ray modulus.  *(wave-15 review repair)*  The small boxes do not close: among the 385 primes
\(p\equiv1\pmod {24}\), \(p<30000\), fifteen have every slice
\(ck\leq30\) equal to zero.  These are statements about this Type-I
sub-count.  They do not assert that any prime lacks an Erdős--Straus
representation.

### 44.1 One slice: factor grades, characters, and root progressions

Fix an odd prime \(p\) and an admissible \((c,k)\in\mathcal B_p\), and write

\[
 h=4ck,\qquad N=p^2+4ck^2=\prod_{j=1}^r\ell_j^{e_j},
 \qquad G_h=(\mathbb Z/h\mathbb Z)^\times .                 \tag{44.1}
\]

The coprimality in (36.1) gives \((N,h)=1\).  In the integral group ring
\(\mathbb Z[G_h]\), put

\[
 F_{p;c,k}=\prod_{j=1}^r
  \bigl([1]+[\ell_j]+\cdots+[\ell_j^{e_j}]\bigr),\qquad
 M_{c,k}(p)=[[{-p}]]F_{p;c,k}.                              \tag{44.2}
\]

Here \([[g]]\) extracts the coefficient of the grade \(g\).  Multiplicities
are retained: two exponent vectors giving the same grade count twice.

**Theorem 44.1 (exact slice-vanishing and conspiracy criterion; proved).**
For the data above, the following integers are equal:

\[
 \begin{split}
 M_{c,k}(p)
 &=\#\{D:D\mid N,\ D\equiv-p\pmod h\}\\
 &={1\over\varphi(h)}\sum_{\chi\ ({\rm mod}\ h)}
   \overline{\chi(-p)}
   \prod_{j=1}^r(1+\chi(\ell_j)+\cdots+\chi(\ell_j)^{e_j}).
                                                               \tag{44.3}
 \end{split}
\]

This is exactly the \((c,k)\)-summand of (36.3).  In particular, that slice
vanishes at \(p\) if and only if

\[
 \boxed{\quad
 \nexists(u_1,\ldots,u_r),\quad 0\leq u_j\leq e_j,\qquad
 \prod_{j=1}^r\ell_j^{u_j}\equiv-p\pmod {4ck}.
 \quad}                                                       \tag{44.4}
\]

Thus (44.4), including the exponent bounds, is the requested factorization
condition.  In character language it says that the inverse Fourier
coefficient at grade \(-p\) in (44.3) is zero; vanishing need not come from
one character factor being zero.

**Raw/primitive and admissibility boundary (wave-15 review repair).**
Theorem 44.1 characterizes the raw summand of (36.3), not the primitive
summand of (36.5).  At a fixed admissible slice the latter is
\[
 M^*_{c,k}(p)=
 \sum_{\substack{D\mid N\\D\equiv-p\ (h)}}
 \sum_{g\mid a_D,\ g\mid b_D}\mu(g)
 =\#\{D\mid N:D\equiv-p\pmod h,\ (a_D,b_D)=1\}.             \tag{44.4a}
\]
Consequently primitive vanishing means that no target divisor gives coprime
\(a_D,b_D\), and is not equivalent to (44.4): raw vanishing implies
primitive vanishing, but not conversely.  For example
\((p,c,k)=(241,7,3)\) has target divisors \(11,5303\), giving the two raw
rows \((a,b)=(3,66),(66,3)\); hence \(M_{7,3}(241)=2\) but
\(M^*_{7,3}(241)=0\).

The admissibility hypothesis is also essential.  If \(p\mid ck\), the target
is not a unit and character orthogonality and the complementary-divisor step
used here fail; for example \((p,c,k)=(3,1,3)\) has
\(9\mid p^2+4ck^2\) and \(9\equiv-p\pmod {12}\), but it gives no row.  Such
a pair is not in \(\mathcal B_p\).  In fact no Type-I tuple has \(p\mid ck\):
if \(p\mid k\), division by \(p\) in the defining equation contradicts
\(4abc-1>a+b\), and then \(p\mid c\) is excluded by reduction modulo \(p\).
Pairs violating the size bounds in (36.1) likewise are not slices of
(36.3).

There is an equivalent progression description.  For every \(d\geq1\), let

\[
 \mathscr R_{c,k}(d)=\left\{r\pmod {\operatorname {lcm}(h,d)}:
 r\equiv-d\pmod h,\quad r^2\equiv-4ck^2\pmod d\right\}.       \tag{44.5}
\]

Then

\[
 M_{c,k}(p)>0
 \quad\Longleftrightarrow\quad
 p\in\bigcup_{d\geq1}\mathscr R_{c,k}(d).                   \tag{44.6}
\]

Any class in (44.5) containing an eligible \(p\) automatically has
\((d,h)=1\), and its second condition is equivalently
\(-c\) being the square of \(p(2k)^{-1}\) modulo \(d\).  Formula (44.6) is
an infinite union of explicit quadratic-root progressions, with the
progression modulus moving with the prospective divisor \(d\).

For a finite set \(S\) of slices, let
\(\mathcal H_S\) be the hard primes for which every member of \(S\) lies in
\(\mathcal B_p\).  Its **conspiracy locus** is therefore exactly

\[
 \mathcal C_S
 =\left\{p\in\mathcal H_S:M_{c,k}(p)=0\ \hbox{for every }(c,k)\in S\right\}
 =\mathcal H_S\cap\bigcap_{(c,k)\in S}
  \left(\mathbb Z\setminus\bigcup_{d\geq1}\mathscr R_{c,k}(d)\right).
                                                               \tag{44.7}
\]

*Proof.*  Expanding (44.2) selects exactly one exponent
\(0\leq u_j\leq e_j\) for every prime factor, hence exactly one positive
divisor of \(N\).  This proves the first line of (44.3) and (44.4).
Fourier inversion on \(G_h\) gives the second line, exactly as in Theorem
36.1.  A positive integer \(d\) is such a divisor precisely when
\(p^2+4ck^2\equiv0\pmod d\); its target grade is precisely
\(p\equiv-d\pmod h\).  These are the two conditions in (44.5), proving
(44.6), and taking simultaneous complements proves (44.7).  Finally
\(N\equiv p^2\pmod h\), so whenever \(D\) has target grade, its complementary
divisor \(N/D\) does too.  For \(p\equiv1\pmod4\) the diagonal is absent by
Theorem 36.1, and every positive slice mass is consequently even. \(\square\)

The root-progression formulation is exact but does not make the union finite.
It isolates the moving-divisor wall: replacing the actual divisors by all
quadratic roots loses the divisibility condition, while retaining it is
exactly the factorization problem for \(p^2+4ck^2\).

### 44.2 A genus-grade obstruction beyond the Gaussian slice

For a positive integer \(c\), write \(c=s t^2\), with \(s\) squarefree.

**Theorem 44.2 (the wrong-grade quartet; proved).**  Suppose
\(p\equiv1\pmod {24}\), \((p,ck)=1\), and

\[
                         s\in\{1,2,3,6\}.                    \tag{44.8}
\]

Then \(M_{c,k}(p)=0\).  Equivalently, every admissible slice whose
squarefree \(c\)-core divides 6 vanishes identically on the hard primes.
Theorem 36.2 is the subfamily \(c=1\); even the extension to every square
\(c=t^2\) is already strict.

*Proof.*  Now
\(N=p^2+4s(tk)^2\).  If a rational prime \(\ell\mid N\), then
\(\ell\nmid2stk\): divisibility by any prime factor of \(stk\) would give
\(N\equiv p^2\not\equiv0\pmod\ell\).  Thus the inverse in the following
reduction exists:

\[
 \left(p(2tk)^{-1}\right)^2\equiv-s\pmod\ell.               \tag{44.9}
\]

Thus every prime-factor grade lies in the kernel of the quadratic character
\(\psi_s(n)=\left(\frac{-s}{n}\right)\).  On the units modulo \(4s\), the
four kernels and the excluded grade are

\[
\begin{array}{c|c|c}
 s&\ker\psi_s&-1\pmod {4s}\\ \hline
 1&\{1\}&3\\
 2&\{1,3\}&7\\
 3&\{1,7\}&11\\
 6&\{1,5,7,11\}&23.
\end{array}                                                   \tag{44.10}
\]

Every divisor grade, being a product of prime-factor grades, remains in the
listed kernel.  This is the complete reduction from \(c=st^2\): projection
from the full ray modulus \(4st^2k\) to \(4s\) discards the square factor
\(t^2\) and all \(k\)-dependence, but any full target divisor would still
project to the target grade.  Since \(4s\mid24\),
\(p\equiv1\pmod {4s}\), and the target \(-p\) projects to the excluded grade
\(-1\).  It cannot occur.  *(wave-15 review repair)* \(\square\)

**Corollary 44.2.1.**  Every one of the eight slices \(ck\leq4\) vanishes on
every hard prime.  Among the 111 slices \(ck\leq30\), 80 vanish identically
by Theorem 44.2 before any factorization depending on \(p\) is inspected.
Therefore a small-box positivity argument must first remove this deterministic
wrong-grade mass; adding many such slices adds no independent chance of a
witness.

### 44.3 What fixed progressions prove, and what they do not

**Corollary 44.3 (one structured hard progression; proved).**  Every prime

\[
                         p\equiv97\pmod {120}                \tag{44.11}
\]

has a positive \((c,k)=(5,1)\) slice.  Indeed \(D=3\) divides \(p^2+20\)
and satisfies \(D\equiv-p\pmod {20}\).  The resulting ordered row and its
swap have

\[
 a={p+3\over20},\qquad b={p^2+3p+20\over60},
 \qquad c=5,\quad k=1.                                     \tag{44.12}
\]

*Proof.*  Condition (44.11) gives \(p\equiv1\pmod3\) and
\(p\equiv17\pmod {20}\).  Hence \(3\mid p^2+20\) and
\(3\equiv-p\pmod {20}\).  Theorem 44.1 gives the slice, and substituting its
complementary divisor gives (44.12). \(\square\)

**Prior-supply identification (wave-15 review repair).**  This uses the same
fixed divisor and hard progression as the \(c=5,D=3\) branch of Theorem 35.4,
but not the same row or slice: at \(p=97\), Theorem
35.4 gives \((a,b,c,k)=(1,34,5,5)\), whereas (44.12) gives
\((5,162,5,1)\).  *(wave-16 review repair)*  Moreover the same hard-prime
progression was already covered by the Type-II multiplier identity of Lemma
16.1: take
\(k\ell=15\) and \((u,v,w)=(1,2,2)\), so
\(p\equiv7\pmod {15}\); intersecting with \(p\equiv1\pmod {24}\) gives
\(p\equiv97\pmod {120}\).  Thus Corollary 44.3 proves pointwise slice
positivity but adds no new progression toward Erdős--Straus.

Consequently, for any \(S\) containing \((5,1)\), \(\mathcal C_S\) excludes
one of the four reduced hard-prime classes modulo 120.  The prime number
theorem in these fixed progressions gives the weak bound

\[
 \#\{p\leq X:p\in\mathcal C_S\}
 \leq (3/4+o(1))\#\{p\leq X:p\equiv1\pmod {24}\}.           \tag{44.13}
\]

This is an effective fixed-congruence exclusion in principle, but it is only
the old identity-family mechanism in ray language and is vastly weaker than
the campaign's exceptional-set bounds.

**Lemma 44.4 (two slices are not determined by their natural ray modulus;
proved).**  Let \(S_0=\{(5,1),(7,1)\}\).  Joint vanishing on \(S_0\) is not
a function of \(p\pmod {\operatorname {lcm}(24,20,28)}=p\pmod {840}\).
Specifically,

\[
                         193\equiv1033\pmod {840},            \tag{44.14}
\]

both slices vanish at 193, while the \((5,1)\) slice is positive at 1033.

*Proof.*  The exact factorizations are

\[
\begin{array}{c|c|c}
(p,c,k)&p^2+4ck^2&-p\pmod {4ck}\\ \hline
(193,5,1)&3^2\cdot41\cdot101&7\pmod {20}\\
(193,7,1)&37277\ \hbox{(prime)}&3\pmod {28}\\
(1033,5,1)&3\cdot67\cdot5309&7\pmod {20}.
\end{array}                                                   \tag{44.15}
\]

In the first row the divisor grades are generated by 3 modulo 20, with the
other factors graded 1, so they are \(1,3,9\), never 7.  In the second row
neither divisor 1 nor 37277 has grade 3 modulo 28.  In the last row,
\(D=67\equiv7\pmod {20}\) survives. \(\square\)

Lemma 44.4 proves only failure at the natural product of the fixed ray
moduli.  It does **not** prove that no larger congruence modulus can describe
this particular two-slice locus.  Establishing such a statement for every
modulus would require controlling factorizations in simultaneous polynomial
progressions and is not obtained here.

### 44.4 Exact finite conspiracy census

**Computational 44.5 (exact stated range, not a theorem beyond it).**
`verify.py (aq)` recomputes all 385 primes \(p<30000\) with
\(p\equiv1\pmod {24}\), and all 111 pairs \(ck\leq30\).  Here “hard” means
exactly \(p\equiv1\pmod {24}\), with no additional no-witness filter.  Every
listed pair is in \(\mathcal B_p\): the least such prime is 73, while
\(k\leq30\leq2p/3\), \(4ck\leq120<2p+k\), and \((p,ck)=1\).
*(wave-15 review repair)*
For each of the 42,735 instances the block factors \(N\), builds both the
finite grade box (44.2) and the literal-divisor list from that same exact
factorization, requires exact equality at the target grade, and reconstructs
every surviving Type-I row.  It also
checks the quadratic character in Theorem 44.2 prime factor by prime factor.
The computation is streamed one norm at a time.

The number of primes for which the entire box through a cutoff vanishes is

\[
\begin{array}{c|rrrrrrr}
 C&4&5&10&15&20&25&30\\ \hline
 \#\{(c,k):ck\leq C\}&8&10&27&45&66&87&111\\
 \#\{p:\hbox{all these slices vanish}\}&385&220&161&63&41&30&15.
\end{array}                                                   \tag{44.16}
\]

For the full \(ck\leq30\) box, the exact depth histogram is

\[
\begin{array}{c|rrrrrrrrrrrrr}
\#\hbox{ vanishing}&99&100&101&102&103&104&105&106&107&108&109&110&111\\ \hline
\#\hbox{ primes}&2&3&10&4&18&43&40&43&55&55&64&33&15.
\end{array}                                                   \tag{44.17}
\]

The maximum depth 111 is attained at

\[
\begin{split}
 2521,9601,12289,13729,15289,18481,19009,20089,21121,21169,\\
 21841,27361,27481,28921,29569.                              \tag{44.18}
\end{split}
\]

The two minimum-depth primes are 5953 and 11353, each with 99 vanishing
slices.  To make the comparison with §36 explicit,
\[
 T_{k=1}(p)=\sum_{c:(c,1)\in\mathcal B_p}M_{c,1}(p),         \tag{44.18a}
\]
so Theorem 36.3's \(k=1\) count is the sum over every admissible \(c\), not
the single \((1,1)\) slice.  Thus (36.15) already says every \(k=1\) slice
vanishes at 2521; the present census additionally finds vanishing for every
\(k\) in the box \(ck\leq30\).  This does not conflict with its twelve
ordered Type-I rows in §36: those rows occur outside this box.
*(wave-15 review repair)*

### 44.5 GRH audit and quantitative verdict

The exact Type-I \(k=1\) formula permits a parallel, more quantitative
version of the technology audit in Assessment 17.5(a); it is not the
Type-II \(k=1\) count (17.4).  *(wave-15 review repair)*
For \(1\leq a\leq p/2\), define

\[
 \begin{split}
 J_a(p)&=\#\{f:f\mid pa+1,\ f\leq p,\ (f,4a)=1\},\\
 I_a(p)&=\#\{f:f\mid pa+1,\ f\leq p,\ f\equiv-p\pmod {4a}\}.
                                                               \tag{44.19}
 \end{split}
\]

Separating the principal character in (36.13) gives the exact decomposition

\[
 T_{k=1}(p)=P_0(p)+E(p),\qquad
 P_0(p)=2\sum_{a\leq p/2}{J_a(p)\over\varphi(4a)},\qquad
 E(p)=2\sum_{a\leq p/2}\left(I_a(p)-{J_a(p)\over\varphi(4a)}\right).
                                                               \tag{44.20}
\]

The principal term is rigorously subpower.  Since \(f=1\) always contributes,
the standard reciprocal-totient estimate and the uniform divisor bound for
\(pa+1\leq p^2\) give

\[
 \log p\ll P_0(p)
 \ll \log p\,\exp\!\left(O\!\left({\log p\over\log\log p}\right)\right)
 =p^{o(1)}.                                                   \tag{44.21}
\]

Its expected scale is polylogarithmic (consistent with the average counts in
§36.5), but no fixed power of \(\log p\) is asserted pointwise.  At
\(p=2521\), (36.15) says exactly \(E(p)=-P_0(p)\): the nonprincipal
projector cancels the whole positive principal mass.

**Assessment 44.6 (GRH does not supply slice positivity through the exact
character formulas).**  Standard GRH character-sum estimates concern
intervals or averaged families.  The inner sum in (36.13) is instead over the
divisors of the single moving integer \(pa+1\), while its conductor \(4a\)
also moves.  GRH by itself gives no square-root estimate for this selected
divisor set.  Even granting, beyond that standard consequence of GRH, a
square-root cancellation across the \(A=\lfloor p/2\rfloor\) normalized
\(a\)-fibres in (44.20), with each fibre of subpower size, leaves

\[
                         E(p)=O(p^{1/2+o(1)}),                \tag{44.22}
\]

whereas (44.21) is only \(p^{o(1)}\).  Without this extra cross-fibre
cancellation, termwise use of the divisor bound gives only
\(E(p)=O(p^{1+o(1)})\).  Thus even the optimistic square-root benchmark is a
factor \(p^{1/2-o(1)}\) too large to prove positivity.  For one fixed
\((c,k)\), (44.3) is still more literal: it is a finite Euler product over
the prime factors of one value \(p^2+4ck^2\), not an interval character sum
at all; GRH does not control its target coefficient pointwise.  Nor does this
restore a Hurwitz argument: the nonprincipal term in (44.20) is ray-grade
information of exactly the kind discarded by the unprojected, weighted mass
in §36.4.  *(wave-15 review repair)*  This is the moving-divisor wall of
§17.5 sharpened with the exact §36 formula, not a claim that GRH plus some
presently unknown additional structure could never prove the conjecture.

**Assessment 44.7 (quantitative failure log).**  Equations (44.4)--(44.7)
give a characterization, not a sparse sequence: the complement of the
conspiracy locus is an infinite union whose moduli are the actual moving
divisors.  Theorem 44.2 shows that 80 of the first 111 slices are perfectly
correlated zeros, while (44.16)--(44.18) show that even the whole box has
many exact finite conspiracies.  No effective all-large-prime bound and no
new exceptional-set estimate follow.  The fixed progression (44.11) is the
only pointwise structured-prime statement retained by this slice analysis;
as noted after Corollary 44.3, it was already supplied by §§16 and 35, and
(44.13) is much weaker than §16.4 and the CLAIMED/PROVISIONAL §39.7.
*(wave-15 review repair)*  Section 16's displayed
argument uses Bombieri--Vinogradov and Brun--Titchmarsh rather than the
Siegel--Walfisz step that makes §§12--15 ineffective, so it is not labelled
ineffective; it remains provisional and has no extracted numerical
threshold.  The slice structure supplies neither an effective replacement
nor a route from almost all primes to every prime.

## 45. The moving-s endpoint against Kloosterman-fraction bilinear forms

Keep all canonical-representative and retention conventions of §§40 and 42.
This section audits the Duke--Friedlander--Iwaniec (DFI) and
Bettin--Chandee (BC) bounds with their actual coefficient quantifiers.  The
result is a proved exact Kloosterman-matrix reduction, but **not** a proof of
(40.19).  The obstruction is not merely an inconvenient range: the endpoint
coefficient is a joint matrix in the inverse variable and its modulus, whereas
DFI and BC allow arbitrary *separate* coefficient sequences.  Moreover,
(42.24) asks for the full row-by-row Fourier norm; its complete $h$-sum
undoes the saving of a scalar Kloosterman-fraction estimate.

### 45.1 Exact bilinearization and the two orientations

For a prime $p>z$, $c<p$, and squarefree $s$, define
$\mathcal Q_{p,c,s}$ to be the set of integers $q$ satisfying

$$
 \begin{gathered}
 q>1,\qquad z<q\leq X/p,\qquad P^-(q)>z,\qquad
 pq\equiv-1\pmod {4c},                                    \tag{45.1}\\
 R={pq+1\over4c}\in\mathbb Z,\qquad s\mid\operatorname {rad}(R),
 \qquad c<p,\quad q<4R,\quad pq\equiv3\pmod4,
 \end{gathered}
$$

together with the requirement that $D=R^2/s$ is the retained canonical
representative at $pq$.  Some displayed conditions follow from the others,
but they are retained to expose the whole endpoint domain.  In particular,
$pq\leq X$ and $P^-(pq)>z$ are exactly present, including possible prime
powers.  Put

$$
 G_{m,p}=\begin{cases}
 \displaystyle\sum_{q\in\mathcal Q_{p,c,s}}{\kappa(pq)\over q},
       &m=4c^2s\text{ with }s\text{ squarefree},\\
 0,&\text{otherwise}.
 \end{cases}                                               \tag{45.2}
$$

The representation $m/4=c^2s$ with $s$ squarefree is unique.  Thus (45.2)
does not conceal a second sum over $(c,s)$; it aggregates only the moving
$q$'s in (42.26), now with the roughness and retention conditions restored.

**Lemma 45.1 (exact endpoint Kloosterman matrix; proved).**  With
$\bar m$ denoting the inverse of $m$ modulo $p$,

$$
 \boxed{\quad
 \mathcal V_X^{\rm end}
 =\sum_{z<p\leq X/z}\sum_{h\bmod p}
   \left|{1\over p}\sum_{m\geq1}G_{m,p}
                  e_p(-h\bar m)\right|^2 .\quad}           \tag{45.3}
$$

The support in (45.3) satisfies

$$
 \begin{gathered}
 4\leq m=4c^2s\leq c(pq+1)<p(X+1),\qquad (m,pq)=1,\\
 z<q\leq X/p,\qquad q<4R,\qquad
 {z\over4}<R={pq+1\over4c}\leq{X+1\over4},\qquad 1\leq c<p.
                                                               \tag{45.4}
 \end{gathered}
$$

For each incidence the two exact reciprocity identities are

$$
 e_p(-h\bar m)
   =e_{pq}(-hq\,\overline m)
   =e_m(h\bar p)\,e\!\left(-{h\over mp}\right),            \tag{45.5}
$$

where the inverses in the last two expressions are taken modulo $pq$ and
$m$, respectively.

*Proof.*  Proposition 42.1 gives a bijection between endpoint incidences and
$(p,c,q,R,s)$ satisfying (45.1).  Equation (42.5) gives
$-4D\equiv-\overline{4c^2s}=-\bar m\pmod p$, while the atom mass is
$\kappa(pq)/(pq)$.  Aggregating all incidences with the same unique $(c,s)$
gives (45.2), and substitution in (42.24) gives (45.3).  The bounds in
(45.4) use $s\leq R$, $m\leq4c^2R=c(pq+1)$, (42.2), and $pq\leq X$;
$(m,pq)=1$ follows from $pq=4Rc-1$.  The first identity in (45.5) follows by
reducing $\overline m\pmod {pq}$ modulo $p$.  The second is additive
reciprocity
$\bar m/p+\bar p/m\equiv1/(mp)\pmod1$.  $\square$

The tempting ``$q$-modulus orientation'' is therefore not an alternative
bilinearization.  The valid lift has modulus $pq$ and numerator $hq$, and
reciprocity has modulus $m$, not $q$.  Although $pq\equiv-1\pmod {4R}$
gives $\bar p\equiv-q\pmod {4R}$, it does not give this congruence modulo
$m=4c^2s$ unless the extra, generally false divisibility $c^2s\mid R$ holds.
If $q$ happens to be prime, interchanging $p$ and $q$ produces a different
coordinate of the energy, and only when $c<q$ is that coordinate itself an
endpoint.  Thus neither the $M=pq$ symmetry nor the short interval for $q$
turns the phase in (45.3) into a Kloosterman fraction with modulus $q$.

The coefficient norms make the remaining issue explicit.  Write

$$
 A_p=\sum_mG_{m,p}=p\,t_p^{\rm end},\qquad
 F_p^2=\sum_mG_{m,p}^2,\qquad
 H_p={A_p^2\over F_p^2}\quad(F_p>0).                       \tag{45.6}
$$

Thus $H_p$ is the effective number of occupied $(c,s)$ cells.  If
$x_i=\kappa(pq)/q$ is an unaggregated incidence coefficient, then

$$
 0<x_i\leq {2\over z},\qquad
 \sum_i x_i^2\leq {2A_p\over z},\qquad
 1\leq H_p\leq\#\{m:G_{m,p}>0\}.                           \tag{45.7}
$$

There is no proved lower bound tending to infinity for $H_p$.  At atom
scale

$$
 {x_i\over p}={\kappa(pq)\over pq}\leq {1\over R}
 ={h_D\over L},                                            \tag{45.8}
$$

but (42.9) shows that the sum of the corresponding $h_D$ still has cubic
size.  Unlike (40.15), an endpoint has no progression-tail factor $L/p$.

For fixed $s$, let $G^{(s)}$ denote the rows of (45.2) with this $s$.
Theorem 42.2 and positivity of each residue bucket imply the genuine norm
bound

$$
 \sum_p{1\over p}\sum_m|G^{(s)}_{m,p}|^2
 \leq \mathcal V_X^{\rm end,(s)}
 \ll L^3+L^2\log L.                                       \tag{45.9}
$$

It is uniform in a *prescribed* $s$.  It gives no summable majorant when
$s=s(p,c,q)$ moves through all divisors of $\operatorname {rad}(R)$; that is
exactly the distinction between (45.9) and the matrix $G$ in (45.2).

### 45.2 The honest DFI and BC quantifiers and their scale windows

The following are the statements actually available.  They are recorded
because ``general coefficients'' means arbitrary entries of each one-variable
sequence, not arbitrary coefficients on pairs or triples.

For arbitrary complex $\alpha_m,\beta_n$ supported on
$[M/2,M]$ and $[N/2,N]$, respectively, DFI's principal estimate is
(the printed DFI convention is $(M,2M]\times(N,2N]$, an immaterial dyadic
relabelling; wave-15 review repair, checked directly against DFI Theorem 2)

$$
 \left|\sum_{\substack{m\sim M,\ n\sim N\\(m,n)=1}}
       \alpha_m\beta_n e\!\left({a\bar m\over n}\right)\right|
 \ll_\varepsilon \|\alpha\|_2\|\beta\|_2
 (|a|+MN)^{3/8}(M+N)^{11/48+\varepsilon},                 \tag{45.10}
$$

for a nonzero integral $a$ (the negative case follows by conjugation).  The
constant is uniform in $a,M,N$; $a=0$ is not covered.  There is no range
hypothesis in the theorem.  When $|a|\leq MN$, comparison with the ambient
$\ell^2$ trivial bound gives a power saving, with a fixed margin, in the true
balanced window

$$
                N^{5/6+\eta}\leq M\leq N^{6/5-\eta}.       \tag{45.11}
$$

Outside it (45.10) need not beat that trivial bound.  DFI also has a different
Poisson estimate useful in unbalanced ranges; it does not change the
coefficient-factorization or Parseval issues below.  In particular,
(45.11), not an assumed interval-length condition on the active support, is
the window of the displayed amplifier bound.

BC take arbitrary complex $\alpha_m,\beta_n,\nu_a$ on the same dyadic
$M,N$ intervals and $a\in[A/2,A]$.  For nonzero real $\vartheta$ their
Theorem 1 states

$$
 \begin{split}
 \left|\sum_{\substack{a\sim A,m\sim M,n\sim N\\(m,n)=1}}
  \nu_a\alpha_m\beta_n e\!\left(\vartheta{a\bar m\over n}\right)\right|
 &\ll_\varepsilon \|\nu\|_2\|\alpha\|_2\|\beta\|_2
 \left(1+{|\vartheta|A\over MN}\right)^{1/2}\\
 &\quad\times\left
 \{(AMN)^{7/20+\varepsilon}(M+N)^{1/4}
 +(AMN)^{3/8+\varepsilon}(AN+AM)^{1/8}\right\}.
                                                               \tag{45.12}
 \end{split}
$$

Again there is no density or balance hypothesis and the displayed factor is
the uniform dependence on $\vartheta$.  For $|\vartheta|A\leq MN$, the
first term beats the ambient $\ell^2$ bound precisely when, up to power
margins,

$$
              \max(M,N)<A^{3/2}\min(M,N)^{3/2},             \tag{45.13}
$$

and the second also requires both $M,N$ to grow.  In the formal endpoint
assignment $A=N=P$, $M=W$ (the variables are $h,p,m$), this gives a power
saving for the scalar trilinear form throughout

$$
                       P^\eta\leq W\leq P^{3-\eta}.         \tag{45.14}
$$

The sources used for (45.10) and (45.12) are archived as
`sources/dfi-1997-kloosterman-fractions.pdf` and
`sources/bettin-chandee-1502.00769.pdf`, respectively (wave-15 review
repair).  The former is the complete 21-page publisher-typeset article from
William Duke's UCLA author archive; `sources/README.md` records both exact
source URLs and SHA-256 hashes.

Endpoint scales do not force either (45.11) or (45.14).  On $p\asymp P$ the
inverse variable is $m=4c^2s$, and (45.4) permits every dyadic scale from a
constant to $\ll PX$.  The DFI window is
$P^{5/6+\eta}\leq4c^2s\leq P^{6/5-\eta}$; the broader BC scalar window is
$P^\eta\leq4c^2s\leq P^{3-\eta}$.  Neither is a condition on $p$ alone.
Even when $P\leq X^{1-\delta}$ makes the numerical $q$-interval long, the
active $c$'s divide $(pq+1)/4$ and $q$ remains inside the joint coefficient
$G_{m,p}$.  Near $P=X/z$ the interval $z<q\leq X/P$ can contain only a
vanishing relative segment.  General one-variable coefficients tolerate a
sparse support, but they do not turn this joint support into a product.

For clarity, if a standard bilinear form really has separated coefficients,
DFI improves its actual $\ell^1$ bound only if

$$
 \left({\|\alpha\|_1\over\|\alpha\|_2}\right)^2
 \left({\|\beta\|_1\over\|\beta\|_2}\right)^2
 > (|a|+MN)^{3/4}(M+N)^{11/24+2\varepsilon}.               \tag{45.15}
$$

Thus ambient interval lengths cannot replace effective coefficient support.
The endpoint analogue (45.6) can be as small as $H_p=1$ under all currently
proved fibre facts.

### 45.3 What DFI gives after an exact rank decomposition

There is a precise way to force (45.2) into DFI, and it quantifies the loss.
Let $P<p\leq2P$, $W<m\leq2W$, and let $G^{P,W}$ be the resulting finite
matrix.  Denote its nuclear norm (sum of singular values) by
$\|G^{P,W}\|_*$.  Put

$$
 Y_{p,h}^{P,W}={1\over p}\sum_{W<m\leq2W}G_{m,p}e_p(-h\bar m),
 \qquad
 E_{P,W}=\sum_{P<p\leq2P}\sum_{0\leq h<p}|Y_{p,h}^{P,W}|^2. \tag{45.16}
$$

**Lemma 45.2 (DFI consequence for the joint endpoint matrix; proved).**  For
every $\varepsilon>0$,

$$
 E_{P,W}\ll
 \sum_{P<p\leq2P}{1\over p^2}
       \left(\sum_{W<m\leq2W}G_{m,p}\right)^2
 +{\mathcal K(P,W)^2\over P}\,\|G^{P,W}\|_*^2,             \tag{45.17}
$$

where

$$
       \mathcal K(P,W)=(PW)^{3/8}(P+W)^{11/48+\varepsilon}. \tag{45.18}
$$

*Proof.*  The first term in (45.17) is exactly the $h=0$ contribution.  For
fixed $1\leq h<2P$, extend $Y_{p,h}$ by zero when $h\geq p$ and introduce
independent Rademacher signs $\epsilon_p$.  Orthogonality of the signs gives

$$
 \sum_{P<p\leq2P}|Y_{p,h}|^2
 =\mathbb E_\epsilon\left|
   \sum_{p,m}{\epsilon_p\mathbf1_{h<p}G_{m,p}\over p}
                   e_p(-h\bar m)\right|^2.                 \tag{45.19}
$$

Take a singular-value decomposition of the joint coefficient matrix inside
the absolute value.  Each rank-one term is exactly a DFI form with $a=-h$,
$m\asymp W$, and $n=p\asymp P$.  The sum of its coefficient-norm products
is the nuclear norm, and the ideal property of that norm gives
$\|G\,\operatorname {diag}(\epsilon_p\mathbf1_{h<p}/p)\|_*
\leq P^{-1}\|G\|_*$.  Since $h\leq2P\ll PW$, (45.10) gives (45.18).
Sum (45.19) over fewer than $2P$ values of $h$.  $\square$

This lemma applies the theorem rather than merely matching the phase.  It
also shows why the application does not close an endpoint range.  The fibre
input controls a Frobenius norm, while

$$
 \|G^{P,W}\|_F\leq\|G^{P,W}\|_*
 \leq \sqrt{\operatorname {rank}G^{P,W}}\,\|G^{P,W}\|_F
 \leq\sqrt{\min(2W,\pi(2P)-\pi(P))}\,\|G^{P,W}\|_F.       \tag{45.20}
$$

No proved endpoint estimate removes this rank factor.  For one fixed $s$,
(45.9) gives $\|G^{(s),P,W}\|_F^2\ll
P(L^3+L^2\log L)$, but summing its nuclear norm over moving $s$ is worse
than the $K^2$ fibre superposition already isolated in (42.11).

At the balanced scale $W=P$, $\mathcal K(P,P)=P^{47/48+O(\varepsilon)}$,
so the nonzero-frequency multiplier in (45.17) is
$P^{23/24+O(\varepsilon)}$.  Even to bound this single block by
$O(\Lambda^2)$ would require

$$
             \|G^{P,P}\|_*
        \ll \Lambda P^{-23/48+O(\varepsilon)},              \tag{45.21}
$$

which is not implied by (45.7)--(45.9).  More intrinsically, when the
$m$'s occupy distinct residues, exact Parseval gives a Frobenius contribution
$\asymp\|G\|_F^2/P$, whereas (45.17), even with rank one, gives
$P^{23/24+O(\varepsilon)}\|G\|_F^2$: it is worse by
$P^{47/24+O(\varepsilon)}$.  The scalar DFI saving $P^{1/48}$ is squared and
then overwhelmed by the $P$ complete frequencies.

BC does not repair this norm mismatch.  It bounds a scalar contraction with
coefficients $\nu_h\alpha_m\beta_p$.  The dual coefficient for the
Frobenius norm in (45.16) is an arbitrary matrix $\eta_{h,p}$, not a product
$\nu_h\beta_p$.  Decomposing it costs its nuclear norm, as large as
$\sqrt P\|\eta\|_F$.  In the optimistic balanced rank-one model, BC saves
only $P^{1/8}$ over the ambient trilinear bound, so this dual rank cost alone
exceeds the saving by $P^{3/8}$; decomposing the actual joint $G_{m,p}$ adds
a second projective-norm loss.  Consequently (45.12) supplies no bound for
the complete Parseval norm (45.3).

**Proposition 45.3 (strongest assembled closed subfamily; proved).**  Fix
$B>3$ and a prescribed set $\mathcal S$ of $K$ squarefree integers.  The
endpoint subfamily consisting of all incidences with $p\leq L^B$, together
with those having $s\in\mathcal S$, has energy

$$
                       O_B(\Lambda^2+K^2L^3).               \tag{45.22}
$$

It therefore satisfies the target when
$K=O(L^{3/2}/\log L)$.  More generally, any endpoint subfamily whose dyadic
matrices satisfy the right side of (45.17), after the
$O(L)$ Cauchy cost for its $m$-blocks, with total $O(\Lambda^2)$ also
satisfies (40.19) for that subfamily.

*Proof.*  The first assertion is Proposition 42.3 and (42.11), followed by
$(x+y)^2\leq2x^2+2y^2$ in each nonnegative residue vector.  The second is
(45.16)--(45.17), dyadic partition, and Cauchy.  $\square$

This is not a new scale range such as $p\leq X^{1-\delta}$.  The DFI/BC
audit gives no enlargement of the proved endpoint family in §42 because no
known estimate supplies (45.21), or its unbalanced analogue, for the moving
joint matrices.

### 45.4 Exact failure logs

**Failure log 45.4 (``general coefficients'' are not a general matrix).**
The exact unresolved coefficient is

$$
 G_{4c^2s,p}=
 \sum_{\substack{z<q\leq X/p,\ P^-(q)>z\\
                  pq\equiv-1\ (4c)\\
                  s\mid\operatorname {rad}((pq+1)/(4c))}}
 {\kappa(pq)\over q}\,
 \mathbf1_{\rm retained},                                 \tag{45.23}
$$

with all conditions of (45.1).  DFI would require
$G_{m,p}=\alpha_m\beta_p$; BC would require the additional $h$ coefficient
to separate as $\nu_h$.  An exact rank decomposition replaces the absent
factorization by $\|G\|_*$ and leads to (45.17).  The missing estimate is a
power-saving projective-norm bound for (45.23), for example (45.21) on
balanced blocks.  Fixed-$s$ Frobenius bounds do not imply it, and the
available inequality (45.20) loses up to
$P^{1/2+o(1)}$ on a balanced block.

**Failure log 45.5 (complete $h$ is the wrong output norm).**  DFI is a
scalar estimate uniform in one nonzero integer $h$; BC is a scalar estimate
with one separated $h$ sequence.  The endpoint asks for
$\sum_{p,h}|Y_{p,h}|^2$.  Summing the DFI estimate over all $h$ produces the
factor $P$ in (45.17).  Dualizing before BC produces an arbitrary
$(h,p)$-matrix and the $\sqrt P$ projective-norm loss.  Orthogonality cannot
be invoked a second time to claim cancellation: invoking it is exactly the
collision identity (42.7).  Any future Kloosterman-fraction input must be a
large-sieve/operator estimate for the joint coefficients (45.23), not merely
a stronger scalar bilinear form.

**Failure log 45.6 (the short cofactor is not a second modulus range).**
The remaining domain is precisely

$$
 L^B<p\leq X/z,\qquad z<q\leq X/p,\qquad P^-(q)>z,\qquad
 q<4R,\qquad pq=4Rc-1,\qquad s\mid\operatorname {rad}(R),     \tag{45.24}
$$

with moving retained $s$.  For $p$ near $X/z$ the $q$-interval can be
arbitrarily short; for $p\leq X^{1-\delta}$ it is long but still appears
inside (45.23), and the phase still has modulus $p$.  The exact reciprocity
formula (45.5) gives modulus $m$ or $pq$, never $q$.  Thus no power of room
in $X/p$ verifies a DFI/BC hypothesis or coefficient-norm condition by
itself.

### 45.5 Exact finite companion and status

**Computational 45.7 (exact finite scope).**  `verify.py (ar)` independently
rebuilds the §40 toy systems at $(X,z,Y)=(80,2,11),(120,3,13),(200,5,17)$.
It forms (45.2), checks the unique square-times-squarefree index, (45.4), and
both reciprocity identities in (45.5), and compares (45.3) with the endpoint
residue energy as an exact rational number.  It reports, for information
only, the number of incidences and occupied $(m,p)$ cells and the exact
coefficient $\ell^1$, squared $\ell^2$, unaggregated squared $\ell^2$, and
$p^{-1}$-weighted Frobenius norms.  Its default output is

$$
\begin{array}{c|c|r|r|c|c|c|c|c}
X&z&I&C&\mathcal V_X^{\rm end}&\|G\|_1&\|G\|_F^2&
 \sum_i x_i^2&\sum_pF_p^2/p\\ \hline
80&2&25&23&54609/67600&1897/260&378617/135200&
352357/135200&55711/135200\\
120&3&59&57&2371407/5216450&17286/1615&201997063/83463200&
194884603/83463200&18474697/83463200\\
200&5&51&51&150469/781456&6509/884&485259/390728&
485259/390728&71765/781456
\end{array}                                                  \tag{45.25}
$$

Here $I$ is the incidence count and $C$ the number of occupied $(m,p)$
cells.  The full-scan extension remains behind `ES_FULL_SCAN=1` and uses
residue buckets, not incidence Cartesian products.  These identities and
norms are finite checks, not asymptotic estimates.

**Assessment 45.8 (wave-15 verdict).**  The moving endpoint is exactly a
Kloosterman-fraction matrix, but not a DFI/BC bilinear or trilinear form with
separated coefficients.  Both possible reciprocity orientations have been
audited; the cofactor $q$ cannot serve as the modulus of the phase.  DFI can
be applied after singular-value decomposition, yielding the proved bound
(45.17), but its nuclear-norm and complete-frequency losses are larger by
fixed powers than its scalar saving.  BC has the same defect at the
$(h,p)$ level.  Therefore the strongest proved endpoint statement within
the DFI/BC axis remains Proposition 45.3: fixed polylogarithmic $p$ and a
controlled number of fixed $s$ fibres.  (Superseded in the review round:
Theorem 45.9 below closes every fibre with $m=4c^2s\leq W_0\asymp
L^3/(\log L)^2$ over the entire prime range, by injectivity rather than
cancellation; the open core of (45.24) is now its restriction to
$m>W_0$.)  The moving-$s$ range (45.24) with $m>W_0$, (40.19), and hence
(37.27) remain **OPEN**.  Even a future proof of (40.19) would not prove the
proposed replacement multi-coordinate hierarchy (47.16); §49 in fact
refutes that hierarchy and the reduced moment bound.  Consequently (33.16) and the
refutation of $H_{\rm PF}'$ remain **OPEN**.  Section 47 refutes the literal
(40.28) and raw-$H$ (37.19).  (wave-17 update)  This is an
internal sieve-hypothesis arc and makes no claim to prove or refute the
Erdős--Straus conjecture.

### 45.6 Review round: the small-fibre moving-$s$ closure

The wave-15 hostile review of this section found the following closure,
recorded here after independent verification.  It rests on the fact that
the endpoint relation pins the residue bucket to the *inverse of the cell
index*: by Lemma 45.1 the phase of a cell is $e_p(-h\bar m)$, so two cells
collide at $p$ exactly when $m\equiv m'\pmod p$.  No cancellation input is
used.

**Theorem 45.9 (small-fibre moving-$s$ closure; proved).**  For
$W_0\geq4$, let $\mathcal E(W_0)$ be the endpoint subfamily of all
incidences with $m=4c^2s\leq W_0$ (every $p$ in $(z,X/z]$, every $q$, $c$,
$R$, $s$ as in (45.4)), and let $\mathcal V(\mathcal E(W_0))$ be its
residue energy.  If $W_0\leq z/2$, then

$$
 \mathcal V(\mathcal E(W_0))
 =\sum_{z<p\leq X/z}{1\over p}\sum_{4\leq m\leq W_0}G_{m,p}^2
 \ll W_0\,(L^3+L^2\log L).                              \tag{45.26}
$$

In particular, with $W_0=\lfloor L^3/(\log L)^2\rfloor$ (admissible for
large $X$ since $z=L^3\log\log L/\log L$), the subfamily
$\mathcal E(W_0)$ satisfies the target of (40.19):
$\mathcal V(\mathcal E(W_0))\ll L^6/(\log L)^2=\Lambda^2$, uniformly over
the entire endpoint prime range.

*Proof.*  Every supported cell has $p\nmid m$: indeed
$4\leq m\leq W_0<p$.  If $4\leq m<m'\leq W_0$, then
$0<m'-m<W_0<p$, so $m\not\equiv m'\pmod p$, and since inversion is a
bijection of $(\mathbb Z/p\mathbb Z)^\times$, also
$\bar m\not\equiv\bar m'\pmod p$.  Hence in the expansion of (45.3)
restricted to $m\leq W_0$, orthogonality of the $h$-sum leaves no
cross-cell terms:

$$
 \sum_{h\bmod p}\left|{1\over p}\sum_{m\leq W_0}G_{m,p}
                  e_p(-h\bar m)\right|^2
 ={1\over p}\sum_{m\leq W_0}G_{m,p}^2 .
$$

This proves the first equality in (45.26).  Each $m\leq W_0$ has the
unique decomposition $m=4c^2s$ with $s$ squarefree, and $s\leq m/4\leq
W_0/4$; the cells with a common $s$ form exactly the prescribed-$s$
subfamily of (45.9).  Summing the uniform fixed-$s$ Frobenius bound (45.9)
over the at most $W_0/4$ squarefree values of $s$ gives

$$
 \sum_{z<p\leq X/z}{1\over p}\sum_{m\leq W_0}G_{m,p}^2
 \leq\sum_{s\leq W_0/4\ {\rm squarefree}}
  \sum_p{1\over p}\sum_m|G^{(s),\leq W_0}_{m,p}|^2
 \ll W_0\,(L^3+L^2\log L),
$$

which is (45.26).  The specialization uses
$W_0(L^3+L^2\log L)\ll L^6/(\log L)^2=\Lambda^2$ and
$W_0=o(z)$.  $\square$

Three remarks keep the ledger exact.  (i) The mechanism is arithmetic
injectivity of small cells, not cancellation; it is therefore insensitive
to the moving coefficients that block DFI/BC, and it closes
$\asymp L^3/(\log L)^2$ fibres where the union route of Proposition 45.3
afforded only $O(L^{3/2}/\log L)$ arbitrary fibres.  This is the widest
proved subfamily of (40.19) to date, and — unlike Proposition 42.3 — it is
uniform over the whole prime range.  (ii) It does **not** prove (40.19):
the complementary range $m=4c^2s>W_0$ (large squares $c^2$ or large
squarefree parts $s$) is untouched, and there distinct cells genuinely
collide modulo $p$.  By (45.4) the cell index reaches
$m\leq c(pq+1)$, so the remaining family is the bulk.  (iii) No new
computational block is added: at toy scale every $m$ exceeds the toy
primes, so the injectivity hypothesis $W_0<z$ has no nontrivial finite
instance; the analytic inputs ((45.3), (45.9)) are already exercised by
`verify.py (ao)` and `(ar)`.

## 46. The endpoint bulk: collision structure above the injectivity threshold

Keep the notation and all retention conventions of §§40, 42, and 45.  This
section attacks the cells $m=4c^2s>W_0$ without discarding their joint
support in $p$.  It proves a larger prefix and a large-$c$ wedge, but it does
**not** prove (40.19).  The exact residual cross-cell sum in Corollary 46.3
is the new pair-level open core.

### 46.1 Cell diagonal and progression occupancy

For any collection $\mathscr S$ of endpoint cells, let $G^{\mathscr S}_{m,p}$
be $G_{m,p}$ when the supported cell $(m,p)$ belongs to $\mathscr S$, and
zero otherwise.  Parseval in Lemma 45.1 gives the exact nonnegative form

$$
 \mathcal V(\mathscr S)
 =\sum_{z<p\leq X/z}{1\over p}
   \sum_{\substack{m,m'\in\mathscr S_p\\m\equiv m'\ (p)}}
       G_{m,p}G_{m',p}.                                    \tag{46.1}
$$

Write

$$
 \mathcal D(\mathscr S)=\sum_p{1\over p}\sum_{m\in\mathscr S_p}G_{m,p}^2,
 \qquad
 \mathcal C(\mathscr S)=\sum_p{1\over p}
   \sum_{\substack{m\ne m'\in\mathscr S_p\\m\equiv m'\ (p)}}
       G_{m,p}G_{m',p}.                                    \tag{46.2}
$$

Thus $\mathcal V=\mathcal D+\mathcal C$ exactly; the off-diagonal sum is
ordered.

**Lemma 46.1 (global cell diagonal and its large-$c$ tail; proved).**  For
$C\geq1$, let $\mathscr G_C$ consist of all endpoint cells whose unique
factorization $m=4c^2s$ has $c\geq C$.  Then

$$
 \boxed{\quad
 \mathcal D(\mathscr G_C)
 \ll {L^4\over C\log z}+{L^4\over z(\log z)^2}.
 \quad}                                                    \tag{46.3}
$$

In particular the complete cell diagonal satisfies

$$
 \mathcal D(\mathscr G_1)\ll {L^4\over\log L}
                         =o(\Lambda^2).                    \tag{46.4}
$$

This includes collisions between different cofactors $q$ aggregated into
the same $(m,p)$ cell; it is stronger than the literal-incidence diagonal
of Lemma 40.2.

*Proof.*  For fixed $(p,c,s)$, (45.1) puts every contributing $q$ in one
progression modulo $4c$.  If $q_0$ is its first member above $z$, comparison
of the remaining terms with an integral gives

$$
 \sum_{\substack{z<q\leq X/p\\q\equiv q_0\ (4c)}}{1\over q}
 \leq {1\over z}+{1\over4c}\log {X/p\over z}
 \leq {1\over z}+{L\over4c}.
$$

Since $\kappa\leq2$, this proves the pointwise cell bound

$$
                         G_{4c^2s,p}\leq {2\over z}+{L\over2c}.       \tag{46.5}
$$

Use $G^2\leq G(2/z+L/(2c))$ in the left side of (46.3), then expand one
copy of $G$.  If $i=(p,R,s,c,q)$ denotes an endpoint incidence and
$M_i=pq$, this gives

$$
 \mathcal D(\mathscr G_C)
 \leq {2\over z}\sum_{i:c_i\geq C}{\kappa_i\over M_i}
     +{L\over2}\sum_{i:c_i\geq C}{\kappa_i\over M_i c_i}. \tag{46.6}
$$

Every retained atom $(M,D)$ has at most
$\omega(M)\leq L/\log z$ endpoint orientations $p$.  The zero-charge
estimate used in (40.12) is
$\sum_{M,D}1/M\ll L^3/\log z$.  Hence the first incidence sum in (46.6) is
$O(L^4/(\log z)^2)$.

For the second sum, drop roughness, primality, endpoint, canonical, and
retention restrictions.  The parameters $R,s,c$ then only overcount, and
$4Rc-1\geq3Rc$.  Therefore

$$
 \begin{split}
 \sum_{i:c_i\geq C}{\kappa_i\over M_i c_i}
 &\ll {L\over\log z}
  \sum_{R\leq X}{2^{\omega(R)}\over R}
  \sum_{c\geq C}{1\over c^2}\\
 &\ll {L^3\over C\log z},                                 \tag{46.7}
 \end{split}
$$

using the elementary Euler-product bound
$\sum_{R\leq X}2^{\omega(R)}/R\ll L^2$.  Substitution in (46.6) proves
(46.3), and $\log z\asymp\log L$ proves (46.4). $\square$

The gain $1/C$ in (46.3) is real, but it appears only after the second
$1/c$ in (46.5) has made the $c$-sum square-summable.  It is not a
$1/C$ bound for total large-$c$ incidence mass; this distinction is used in
Failure log 46.6.

### 46.2 A larger prefix and a large-$c$ wedge

Put

$$
 W_1=\left\lfloor {zL^2\over\log L}\right\rfloor
 \asymp {L^5\log\log L\over(\log L)^2},
 \qquad W_2=\lfloor zW_1\rfloor.                           \tag{46.8}
$$

Thus $W_1/W_0\asymp L^2\log\log L$: the following result reaches well
above the injectivity threshold of Theorem 45.9.

**Theorem 46.2 (prefix and large-$c$ wedge closure; proved).**  Let
$\mathscr A(T,C)$ be the endpoint subfamily with $m\leq T$ and $c\geq C$.
For all $T,C\geq1$,

$$
 \mathcal V(\mathscr A(T,C))
 \leq\left(1+{T\over z}\right)\mathcal D(\mathscr G_C)
 \ll\left(1+{T\over z}\right)
       \left\{{L^4\over C\log z}
                    +{L^4\over z(\log z)^2}\right\}.      \tag{46.9}
$$

Consequently both

$$
 \mathcal V(\mathscr A(W_1,1))=O(\Lambda^2),
 \qquad
 \mathcal V(\mathscr A(W_2,z))=O(\Lambda^2).              \tag{46.10}
$$

*Proof.*  In one residue class modulo $p$, the interval $1\leq m\leq T$
contains at most $T/p+1$ integers, hence no more supported cells.  Cauchy's
inequality inside each occupied residue bucket and (46.1) give

$$
 \mathcal V(\mathscr A(T,C))
 \leq\sum_p{1\over p}\left(1+{T\over p}\right)
       \sum_{\substack{m\leq T\\c(m)\geq C}}G_{m,p}^2
 \leq\left(1+{T\over z}\right)\mathcal D(\mathscr G_C).
$$

Lemma 46.1 proves (46.9).  For $(T,C)=(W_1,1)$ its leading term is

$$
 {W_1\over z}{L^4\over\log z}
 \asymp {L^6\over(\log L)^2}=\Lambda^2.
$$

For $(T,C)=(W_2,z)$ it is

$$
 {W_2\over z}{L^4\over z\log z}
 \asymp W_1{L^4\over z\log L}\asymp\Lambda^2.
$$

The second term of (46.9) is smaller by at least a factor comparable with
$\log L$ in the latter specialization, and is harmless in the former.
This proves (46.10). $\square$

This is the supported-cell version of the proposed large-$m$ count.  It
uses the integer progression occupancy only after preserving the actual
Frobenius mass; no sum over the $\asymp X\log X$ possible shifts of Failure
log 42.5 occurs.

Define the proved region and its complement by

$$
 \begin{split}
 \mathscr A&=\{m\leq W_1\}\ \cup\
             \{c\geq z,\ m\leq W_2\},\\
 \mathscr B&=\{m>W_1\}\ \cap\
             \bigl(\{c<z\}\ \cup\ \{m>W_2\}\bigr).
                                                               \tag{46.11}
 \end{split}
$$

The two sets partition every endpoint cell.  By (46.10) and
$(x+y)^2\leq2x^2+2y^2$ in each residue bucket,

$$
                         \mathcal V(\mathscr A)=O(\Lambda^2).          \tag{46.12}
$$

**Corollary 46.3 (falsifiable refined open core; proved equivalence).**
The endpoint estimate (40.19) is equivalent to

$$
 \boxed{\quad
 \mathcal C_{\rm bulk}:=
 \sum_{z<p\leq X/z}{1\over p}
 \sum_{\substack{m\ne m'\in\mathscr B_p\\m\equiv m'\ (p)}}
        G_{m,p}G_{m',p}=O(\Lambda^2).
 \quad}                                                    \tag{46.13}
$$

*Proof.*  Deleting cells decreases every nonnegative residue bucket, so
$\mathcal V(\mathscr B)\leq\mathcal V_X^{\rm end}$.  Conversely,

$$
 \mathcal V_X^{\rm end}
 \leq2\mathcal V(\mathscr A)+2\mathcal V(\mathscr B).
$$

Thus (40.19) is equivalent to
$\mathcal V(\mathscr B)=O(\Lambda^2)$ by (46.12).  Equations (46.2) and
(46.4) give

$$
 \mathcal V(\mathscr B)
 =\mathcal D(\mathscr B)+\mathcal C_{\rm bulk},
 \qquad \mathcal D(\mathscr B)=o(\Lambda^2),
$$

and all terms are nonnegative.  This proves the equivalence. $\square$

Equation (46.13), rather than all $m>W_0$, is the refined pair-level
endpoint.  It contains only genuine collisions between distinct supported
cells, after the whole cell diagonal, the prefix through $W_1$, and the
specified large-$c$ wedge have been removed.

### 46.3 Dyadic collision audit and exact loss

For $W\geq1$, let $\mathscr S(W,C)$ be any supported subfamily with
$W<m\leq2W$ and $c\geq C$, and let $\mathcal C(W,C)$ denote its ordered
off-diagonal energy.

**Lemma 46.4 (supported dyadic collision second moment; proved).**  One has

$$
 \mathcal C(W,C)
 \leq {W\over z}\mathcal D(\mathscr S(W,C))
 \leq {W\over z}\mathcal D(\mathscr G_C),                 \tag{46.14}
$$

and consequently

$$
 \mathcal C(W,C)
 \ll {W\over z}\left\{{L^4\over C\log z}
                   +{L^4\over z(\log z)^2}\right\}.       \tag{46.15}
$$

The leading term in (46.15) is $O(\Lambda^2)$ for $W=O(CW_1)$;
when $1\leq C\leq z$, the second term is harmless and the full right side
is $O(\Lambda^2)$ in this range.

*Proof.*  A residue class modulo $p$ contains at most $W/p+1$ integers in
$(W,2W]$.  If a bucket has $n$ supported cells with coefficients $g_j$,
then

$$
 \left(\sum_jg_j\right)^2-\sum_jg_j^2
 \leq(n-1)\sum_jg_j^2\leq {W\over p}\sum_jg_j^2.
$$

Sum this inequality with weight $1/p$, use $p>z$, and then apply Lemma
46.1.  The last assertion follows from (46.8). $\square$

This proves the proposed $N_p(m,W)\leq W/p+1$ step with the actual jointly
supported cells.  It also pinpoints its limit.  For unrestricted $c$, its
best available right side is

$$
 \mathcal C(W,1)\ll {W\over W_1}\Lambda^2;                \tag{46.16}
$$

for $c\geq C$ with $1\leq C\leq z$ the corresponding factor is
$W/(CW_1)$.  The two boundaries $W_1$ and $zW_1=W_2$ are exactly why
(46.11) removes the ranges it does.
Above those boundaries no scale decay for
$\mathcal D(\mathscr S(W,C))$ has been proved.

**Failure log 46.5 (where the dyadic second moment stops).**  The
arithmetic-progression count itself is valid and already includes supported-
cell sparsity.  The loss occurs when $W/p$ multiplies the Frobenius norm.
The only proved scale-free estimate is (46.3); inserting it gives (46.16),
which exceeds the target in the first unrestricted block above $W_1$ and
in the first $c\geq z$ block above $W_2$.  The per-prime alternative does
not improve this: (42.18) gives
$A_p=p t_p^{\rm end}\ll\Lambda+p u_p$, and $p u_p=p^{o(1)}$ is not
uniformly polylogarithmic on the super-polylogarithmic range.  Bounds such
as $F_p^2\leq A_p^2$ therefore discard, rather than exploit, the needed
scale localization.

Partitioning all $m$ dyadically does not fix the issue.  Lemma 46.4 controls
pairs inside one block, whereas (46.13) also has pairs in different blocks.
Cauchy over the $O(L)$ blocks costs $O(L)$ and gives no decay in $W$.
Alternatively, putting all supported $m<p(X+1)$ into one progression count
allows $O(X)$ integers per residue and is catastrophic.  A successful
continuation needs a bound for the *scale-restricted* Frobenius mass or a
direct correlation estimate for the separated-block pairs; neither is
contained in (45.9), (46.3), or the scalar DFI/BC bounds.

**Failure log 46.6 (where large-$c$ thinness stops).**  The second part of
Lemma 46.1 verifies a genuine $1/C$ large-$c$ saving for cell Frobenius
mass, and Theorem 46.2 converts it into the wedge $m\leq CW_1$ in the
relevant range $1\leq C\leq z$.  The available positivity majorant for
total incidence mass is not power-small.  Indeed, after using
$M=4Rc-1\asymp Rc$, that majorant is

$$
 \sum_{R\leq X/(4C)}{2^{\omega(R)}\over R}
       \sum_{C<c\leq X/(4R)}{1\over c}
 \asymp \{\log(X/C)\}^3                                  \tag{46.17}
$$

through the broad range $C\leq X^{1-\epsilon}$, by the same elementary
Euler product behind (42.9).  For polylogarithmic $C$, the cutoff
$R<X/(4C)$ therefore removes no power of $L$; the $c$-sum is harmonic, not
square-summable.  The $1/C$ in (46.3) appears only because (46.5) contributes
an additional $1/c$.  Once collision occupancy contributes
$W/p$, that saving closes (46.15) only for $W\ll CW_1$.  Thus “large $c$
forces small $R$” proves the wedge in (46.10), but it does not control the
part of (46.13) with $m>CW_1$.  Dropping endpoint indicators and summing
(46.17) is precisely the divisor-counting failure warned against in
Failure log 42.5.

### 46.4 Exact finite corner census

**Computational 46.7 (exact rational bulk split).**  `verify.py (as)`
independently rebuilds the retained toy endpoint matrices without an
incidence Cartesian product.  At finite $(X,z)$ it uses

$$
 W_{1,{\rm toy}}=
 \max\left(4,\left\lfloor {z(\log X)^2\over\log\log X}\right\rfloor\right)
                                                               \tag{46.18}
$$

and the exact analogue of (46.11).  It partitions every residue-bucket
square into five rational corners:
$\mathcal V(\mathscr A)$, the ordered mixed $\mathscr A$--$\mathscr B$
term, $\mathcal D(\mathscr B)$, cross-cell pairs in the same anchored
block $(2^jW_1,2^{j+1}W_1]$, and cross-cell pairs in different blocks.
The five entries are asserted to resum $\mathcal V_X^{\rm end}$ exactly.
The output is

$$
\begin{array}{c|c|r|r|r|c|c|c|c|c|c}
X&z&W_1&A&B&\mathcal V(A)&\mathrm{mix}&\mathcal D(B)&
 \mathcal C_{\rm local}&\mathcal C_{\rm far}&\mathcal V_X^{\rm end}\\ \hline
80&2&25&12&11&16681/33800&5277/27040&14419/135200&0&1/80&54609/67600\\
120&3&43&28&29&735841/3338528&1062997/8346320&6819677/83463200&0&2759/109820&2371407/5216450\\
200&5&84&30&21&7635/91936&95917/1562912&29501/781456&0&3/289&150469/781456\\
400&7&140&50&34&1149696311/18401725888&13756187/445716544&2612018711/128812081216&1/832&203263/36428756&1938623889/16101510152\\
800&11&258&151&150&77161480892545741127118439/2107339042676052674803557152&198624380002352137829660547/8429356170704210699214228608&313024080491417457652016507/16858712341408421398428457216&17451321/15854098624&70610715947907451031165/7855877139519301676807296&1497652428663746795066282367/16858712341408421398428457216
\end{array}
$$

Here $A,B$ are occupied $(m,p)$ cell counts.  The first three rows are the
default run; $X=400,800$ are enabled by `ES_FULL_SCAN=1`.  The refined
cross-cell corner $\mathcal C_{\rm local}+\mathcal C_{\rm far}$ accounts
for the exact fractions $845/54609$, $8455/152994$, and $8112/150469$ of
total endpoint energy at $X=80,120,200$, respectively.  At these toy
scales most residual collisions are between separated dyadic blocks; this
is an identity check, not asymptotic evidence.

**Assessment 46.8 (wave-16 verdict).**  Supported-cell progression
occupancy and a new global cell-diagonal estimate enlarge the closed prefix
from $W_0\asymp L^3/(\log L)^2$ to
$W_1\asymp L^5\log\log L/(\log L)^2$, and also close the large-$c$ wedge
$c\geq z$, $m\leq zW_1$.  The exact equivalent remainder is the distinct-
cell collision sum (46.13).  The dyadic method loses there by the explicit
factor $W/(CW_1)$, while direct large-$c$ divisor counting retains a cubic
harmonic mass.  Therefore (40.19), (37.27), and the pair-level input to the
internal hypothesis $H_{\rm PF}'$ remain **OPEN**.  Even a future proof of
(40.19) would not by itself prove (33.16).  Section 47 refutes the literal
(40.28) and raw-$H$ (37.19); §49 refutes the replacement hierarchy (47.16)
and reduced moment bound.  (wave-17 update)  This arc neither proves nor
refutes the Erdős--Straus conjecture.
## 47. The codegree hierarchy: structure, partial theorems, and the exact remaining wall

This section gives a negative answer to the literal target (40.28).  The
prime-support decomposition is exact and its coprime part is harmless, but a
squarefree divisor cube of retained intrinsic atoms makes the equal-level
part exponentially larger than $\Lambda$.  The same cube disproves (37.19)
for the particular, only-prime-reduced count $H$ used in §37.  This refutes a
proposed sufficient mechanism, **not** $H_{\rm PF}'$ and not the
Erdős--Straus conjecture.  A complete implication reduction preserves the
void and removes this example.  Section 49 subsequently refutes the
residue-resolved hierarchy for that reduced antichain by a collective
semiprime-grid obstruction.  (wave-17 update)

### 47.1 Exact one-step structure

Let $\mathcal P_0$ be the conditioned primes in (37.8), and put
$\theta_q=q-f(q)$ for $q\in\mathcal P_0$.  For a compatible nonempty set
$S$, write

$$
 Q_S=[M_A:A\in S],\qquad r_q=v_q(Q_S),                     \tag{47.1}
$$

and let $a_S\pmod {Q_S}$ be its merged class.  For a candidate atom $B$ put
$M=M_B$, $e_q=v_q(M)$, and

$$
 w_B=\Pr(B\mid T_0=1)
 ={1\over M}\prod_{q\in\mathcal P_0,\ q\mid M}{q\over\theta_q}.
                                                                    \tag{47.2}
$$

This formula includes tail prime atoms as well as the retained composite
atoms.  Define the shared-coordinate collapse

$$
 \Gamma_S(B)=
 \prod_{q\mid(M,Q_S)}q^{\min(e_q,r_q)}
 \prod_{q\in\mathcal P_0,\ q\mid(M,Q_S)}{\theta_q\over q}. \tag{47.3}
$$

**Proposition 47.1 (exact extension formula; proved).**  If $B\notin S$ is
compatible with $S$, then

$$
 {\Pr(\bigcap_{A\in S\cup\{B\}}A\mid T_0=1)
  \over\Pr(\bigcap_{A\in S}A\mid T_0=1)}
 =w_B\Gamma_S(B)
 =\prod_q\rho_q(e_q,r_q),                                  \tag{47.4}
$$

where factors with $e_q=0$ are one and

$$
 \rho_q(e,r)=
 \begin{cases}
  1,&r>0,\ e\leq r,\\
  q^{-(e-r)},&r>0,\ e>r,\\
  q^{-e},&r=0,\ q\notin\mathcal P_0,\\
  \{q^{e-1}\theta_q\}^{-1},&r=0,\ q\in\mathcal P_0.
 \end{cases}                                               \tag{47.5}
$$

*Proof.*  Divide (40.26) for $S\cup\{B\}$ by the same formula for $S$.
An old conditioned coordinate cancels completely.  A new conditioned
coordinate contributes $q^{-e}q/\theta_q$, and an unconditioned one
contributes $q^{-e}$.  At an old coordinate only the new digits above
$q^{r_q}$ cost probability.  This is (47.5); multiplying (47.2) by
(47.3) gives the same factors. $\square$

This calculation corrects a possible misuse of the $e^{o(\Lambda)}$ factor
following (40.26).  That is a bound for one whole intersection.  In the
ratio, all conditioning factors on old coordinates cancel exactly; only
new conditioned primes occur in (47.5).

Split the candidates in (40.27) into

$$
 \begin{array}{ll}
 \mathcal B_0(S):&(M_B,Q_S)=1,\\
 \mathcal B_\leq(S):&(M_B,Q_S)>1\text{ and }e_q\leq r_q
       \text{ at every shared }q,\\
 \mathcal B_>(S):&e_q>r_q\text{ at at least one shared }q.
 \end{array}                                                \tag{47.6}
$$

Equations (47.3)--(47.4) give the exact disjoint resummation

$$
 \mathcal L(S)=\mathcal L_0(S)+\mathcal L_\leq(S)
                       +\mathcal L_>(S),\qquad
 \mathcal L_\star(S)=
 \sum_{B\in\mathcal B_\star(S),\ B\sim S}w_B\Gamma_S(B). \tag{47.7}
$$

Here $B\sim S$ means joint residue compatibility.  The coprime part is
completely controlled:

$$
 \mathcal L_0(S)=\sum_{B\in\mathcal B_0(S)}w_B
 \leq\mathbb E(H\mid T_0=1)=O(\Lambda).                   \tag{47.8}
$$

Thus goal 1(a) holds with no accumulated conditioning loss.  Goals 1(b) and
the proposed squarefree restricted hierarchy do not hold, as the next
subsection shows.  Higher new digits in $\mathcal B_>(S)$ are a genuine
additional profile problem, but they are not the first obstruction.

For reference, the literal residue profile behind (47.7) is also exact.  If
$d=(M,Q_S)$ and $N^\circ(M;d,a)$ counts retained intrinsic classes of
modulus $M$ whose projection is $a\pmod d$, then the modulus-$M$ summand is

$$
 {\kappa(M)\over M}\Gamma_S(M)
 N^\circ(M;d,a_S),                                         \tag{47.9}
$$

apart from omitting atoms already in $S$.  This is the complete-system
analogue of $W_{k,a}(g)$ in Lemma 39.2.  No bound comparable to (39.7) is
known for (47.9).  The literal ``at most $1/\varphi(d)$ of the mass'' claim
is false even finitely: after the §37 prime deletion at $(X,z)=(80,2)$,
the modulus $35$ has exactly the two retained classes $23,32\pmod {35}$,
which project to two different classes modulo $7$.  Each therefore carries
one half, not at most $1/\varphi(7)=1/6$, of that modulus's retained mass.
The obstruction below is stronger: compatibility has density one along a
large divisor sublattice.

### 47.2 A squarefree divisor cube disproves (40.28) and (37.19)

**Theorem 47.2 (nested retained-atom obstruction; proved).**  For all
sufficiently large $X$, the family counted by $H$ contains a squarefree
atom $A$ such that

$$
 \mathcal L(\{A\})\geq
 \exp\!\left(c{L\over\log L}\right).                       \tag{47.10}
$$

All terms giving (47.10) lie in $\mathcal B_\leq(\{A\})$.  Consequently
(40.28) is false, including its restrictions to squarefree selected moduli
and to selected moduli that are pairwise coprime (a singleton already
satisfies the latter condition).

Moreover, if $m\asymp\Lambda$, then for every fixed $C>0$,

$$
          \mathbb E((H)_m\mid T_0=1)>(C\Lambda)^m           \tag{47.11}
$$

for all sufficiently large $X$.  Thus the sufficient input (37.19), whose
expectation is in this conditioned space, is also false for this unreduced
$H$.

*Proof.*  Recall $Y=L^4/h(L)$ from (37.7).  Let $k$ be the largest odd
integer at most $L/(3\log(2Y))$.  The prime number theorem in the fixed
classes modulo $8$ supplies distinct primes

$$
 q\in(Y,2Y),\ q\equiv3\pmod8,
 \qquad p_1,\ldots,p_k\in(Y,2Y),\ p_i\equiv5\pmod8.        \tag{47.12}
$$

There are far more than $k\asymp L/\log L$ available primes.  Put
$M=q\prod_{i=1}^kp_i$.  Then
$M\leq(2Y)^{k+1}<X$ for large $X$.

For every odd subset $I\subseteq\{1,\ldots,k\}$ put
$M_I=q\prod_{i\in I}p_i$.  One has $M_I\equiv7\pmod8$, so
$2\mid(M_I+1)/4$ and Lemma 18.1 supplies the atom

$$
                         A_I:\quad n\equiv-8\pmod {M_I}.   \tag{47.13}
$$

It survives all reductions made in §37.3.  Indeed $q$ is the only prime
factor congruent to $3\pmod4$, and
$(-8/q)=(-1/q)(2/q)^3=+1$ because $q\equiv3\pmod8$.
Lemma 21.2 says that every intrinsic class at the prime modulus $q$ has
Legendre sign $-1$, so (47.13) is not prime-implied.  The other prime
factors are $1\pmod4$ and have no prime-modulus atom in this system.
Also $D=2$ is the least representative of its class, so canonical
representative bookkeeping does not delete it.

Take $A=A_{\{1,\ldots,k\}}$.  Its event is contained in every $A_I$:
$M_I\mid M$ and all the residues in (47.13) are the same integer.  Hence
adding any proper odd-subset atom to $\{A\}$ has conditional ratio exactly
one.  There are $2^{k-1}-1$ such atoms.  Their moduli are squarefree and all
shared exponents are equal to one, proving (47.10) and its
$\mathcal B_\leq$ assertion.

On the event $A$, at least $K=2^{k-1}$ distinct atoms counted by $H$ occur.
All their primes exceed $Y$, so $A$ is independent of $T_0$ and
$\Pr(A\mid T_0=1)=1/M$.  Therefore

$$
             \mathbb E((H)_m\mid T_0=1)\geq{(K)_m\over M}. \tag{47.14}
$$

Here $K=\exp(\Theta(L/\log L))\gg m$ and $\log M\leq L$.  Thus
$(K)_m\geq(K/2)^m$, while
$\log(C\Lambda)=O(\log L)$.  The logarithm of (47.14) minus
$m\log(C\Lambda)$ is
$\Theta(L^4/(\log L)^2)-O(L^3)-O(L)>0$.  This proves (47.11). $\square$

This is exactly where the §39.3 analogy breaks.  Lemma 39.2 averages a rich
$(u,v)$ family over each multiplier residue.  In (47.13), conditioning on
the finest atom fixes every coarser divisor atom with probability one;
there is no $1/\varphi(g)$ consistency thinning to pay for the lcm collapse.
The issue is logical redundancy, not a missing large-sieve estimate.

### 47.3 What partial hierarchy survives

**Proposition 47.3 (prime-only selected sets; proved).**  If every atom in a
compatible set $S$ is a tail prime-modulus atom, then
$\mathcal L(S)=O(\Lambda)$.

*Proof.*  Distinct compatible prime atoms use distinct primes.  A retained
composite atom sharing one of these primes has, by definition of the §37.3
deletion, a projection outside the complete intrinsic prime residue set, so
it is incompatible with the selected prime atom.  A different prime atom
on the same coordinate is also incompatible.  Every compatible new atom is
therefore coprime to $Q_S$, and (47.8) applies. $\square$

The other requested rungs do not currently survive:

* Pairwise-coprime or squarefree $S$ does not help: Theorem 47.2 uses a
  singleton squarefree $S$.  Its bad candidates are also squarefree.
* Theorem 45.9 is an unconditional quadratic-energy estimate for added
  endpoint atoms with $m=4c^2s\leq W_0$.  It gives no uniform conditional
  extension estimate after an arbitrarily finer atom has been fixed.
  The divisor cube above lies in regular, not endpoint, progressions, so it
  neither refutes nor proves a small-endpoint-only hierarchy.  That
  restricted question remains open; injectivity alone is insufficient.
* The star hierarchy (40.29) is still open.  Its $j=2$ case contains the
  open endpoint (40.19), which is being treated separately.  No proof or
  asymptotic counterexample for all $2\leq j\leq m$ is claimed here.
  Even granting every one-coordinate star estimate would not see
  Theorem 47.2, because one finest congruence simultaneously implies a
  Boolean lattice of coarser multi-coordinate congruences.

Prime powers are a separate reason that prime-level stars are insufficient.
For example the retained atoms represented by

$$
 (M,D,r)=(539,27,431),\qquad(1519,76,1215)                 \tag{47.15}
$$

share the class $39\pmod {49}$.  With $7$ conditioned, $f(7)=3$, their
relative collapse is $49(7-3)/7=28$, whereas a squarefree $7$-star records
only $7-f(7)=4$.  A higher-level corner is given by the compatible retained
atoms $(119,3,107)$ and $(539,675,534)$: the added modulus raises the shared
$7$-level from $7$ to $49$, and (47.5) charges the one genuinely new base-$7$
digit.  `verify.py (at)` checks both examples exactly.

### 47.4 The repaired wall and verdict

The natural repair is to replace the §37 family by its **implication
antichain** $\mathcal A^*$: delete an atom $A$ whenever another retained
atom $B$ satisfies $M_B\mid M_A$ and $r_A\equiv r_B\pmod {M_B}$.  Then
$A\subseteq B$, so this deletion preserves the union and hence the void.
It extends the prime-only deletion already made in §37.3.  No claim is made
here that the resulting hierarchy is true.

For this repaired family, the exact remaining estimate is the following
falsifiable statement.  There should be fixed $C,D>0$ such that, for every
large $X$, every compatible $S\subset\mathcal A^*$ with
$1\leq|S|<m$, where $m$ is an even integer in
$[D\Lambda,D\Lambda+2]$, one has

$$
 \boxed{\quad
 \sum_{B\in\mathcal A^*\setminus S\atop
       B\sim S,\ (M_B,Q_S)>1}
 w_B\Gamma_S(B)\leq C\Lambda.
 \quad}                                                     \tag{47.16}
$$

Together with (47.8), (47.16) is necessary and sufficient up to a change of
constant for the one-step bound (40.28) on $\mathcal A^*$.  Induction then
gives (37.19) for the repaired count, and Proposition 37.3 applies unchanged:
the void is identical and all degree, modulus, and ledger bounds only
improve on passing to a subfamily.

Even if the separate open pair endpoint (40.19) is granted as a black box,
(47.16) does not follow from it.  Equation (40.19) is an averaged
single-prime quadratic energy; (47.16) is uniform in the already selected
multi-coordinate class, including $|S|=1$, all simultaneous shared primes,
and all prime-power digits.  Conversely, (47.16) would subsume the needed
one-step work, so no additional unnamed ``higher moment estimate'' is being
hidden.

**Computational 47.4 (exact finite scope).**  `verify.py (at)` builds the
complete conditioned toy $H$ at $(X,z,Y)=(40,2,7)$.  It checks every
compatible $S$ through degree four and every possible extension $B$, using
exact rational CRT probabilities.  The output is

$$
\begin{array}{c|c|c|c|c|c}
K&\Lambda_{\rm toy}:=\mu&\#S\ (|S|=1,2,3,4)&
 \max\mathcal L(S)\ (|S|=1,2,3,4)&
 \max_S\mathcal L(S)/\mu&(\#\mathcal B_0,\#\mathcal B_\leq,\#\mathcal B_>)\\ \hline
28&27839083/19372210&(28,316,1868,6217)&
(6342705/3874442,295533/149017,14316/7843,421/253)&
38419290/27839083&(73548,14916,0).
\end{array}
$$

Thus this toy has $C_{\rm toy}=1.38005\ldots$; it is not asymptotic
evidence.  The block separately checks the four-atom finite divisor cube at
$M=5655$, the equal-$49$ collapse $28$, and a genuinely higher-$7$-power
extension.  With `ES_FULL_SCAN=1` it also checks all 99,362 compatible
triples of the complete reduced-composite toy at $(550,5,550)$; there are
32,184 higher-level candidate extensions.  Enumeration is compatibility
pruned and does not form a full powerset.

**Assessment 47.5 (wave-16 verdict).**  The literal codegree target (40.28)
and the raw-$H$ factorial-moment target (37.19) are **REFUTED** by a retained
squarefree divisor cube.  The coprime extension bound and the prime-only
selected-set hierarchy are proved.  The compatibility-thinning analogy from
§39 fails because the complete intrinsic family was not reduced under
composite implication.  Section 49 subsequently proves that, after the exact implication-antichain
repair, (47.16) and the reduced factorial-moment bound are **REFUTED** by a
collective semiprime-grid obstruction.  The pair endpoint (40.19), (33.16),
and $H_{\rm PF}'$ remain **OPEN**.  Nothing in this section proves or refutes
the Erdős--Straus conjecture.  (wave-17 update)
## 48. Conspiracy depth: the unforced slices, growth of the vanishing box, and guaranteed-positivity classification

**Scope and outcome.**  This section separates the 80 deterministic zeros in
(44.16) from the 31 slices which can actually fluctuate.  A quadratic genus
character forces vanishing on exactly one half of the hard prime classes for
every one of those 31 slices, while a fixed prime divisor supplies a
positive-density progression for every one; hence there is no further
identically zero slice in the box.  *(wave-16 review repair)*  The remaining
zeros are genuine misses of the moving finite exponent box.  An exact census defines and computes a robust conspiracy depth through
30,000 (and optionally 100,000), and a fixed-divisor theorem classifies all
arithmetic-progression guarantees of that shape.  Its residue-one escape is an
exact slice-language mirror of Theorem 17.3.  None of this proves that every
hard prime has a positive Type-I slice: the final equivalence is explicitly a
bookkeeping reformulation of that open strengthening.

### 48.1 The unforced genus and the complete small-box list

Write

\[
 c=st^2,\qquad s=\operatorname {sf}(c)\ \hbox{squarefree},\qquad
 \chi_s(n)=\left({\Delta_s\over n}\right),                 \tag{48.1}
\]

where \(\Delta_s<0\) is the fundamental discriminant of
\(\mathbb Q(\sqrt{-s})\).  Its conductor divides \(4s\).

**Theorem 48.1 (the moving genus obstruction; proved).**  Let
\(p\equiv1\pmod {24}\), let \((c,k)\in\mathcal B_p\), and use (48.1).
Then

\[
                  \chi_s(p)=1\quad\Longrightarrow\quad
                  M_{c,k}(p)=0.                             \tag{48.2}
\]

The restriction of \(\chi_s\) to the hard progression is identically one if
and only if

\[
                         s\in\{1,2,3,6\}.                   \tag{48.3}
\]

For every other squarefree \(s\), the hard primes with \(\chi_s(p)=1\) have
relative Dirichlet density \(1/2\) (with the finitely many ramified primes
omitted); imposing admissibility for a fixed \((c,k)\) removes only the further
finite set dividing \(ck\).  *(wave-16 review repair)*

*Proof.*  Every prime \(\ell\mid p^2+4s(tk)^2\) is odd and prime to
\(stk\), and

\[
                 \bigl(p(2tk)^{-1}\bigr)^2\equiv-s\pmod\ell.
\]

Thus \(\chi_s(\ell)=1\), and every divisor \(D\) of the norm has
\(\chi_s(D)=1\).  Because the conductor divides \(4s\mid4ck\), a target
divisor would instead have
\(\chi_s(D)=\chi_s(-p)=-\chi_s(p)\).  This proves (48.2).
The primitive quadratic character \(\chi_s\) is constant on the kernel of
reduction modulo 24 exactly when its conductor divides 24.  The negative
fundamental discriminants with this property give precisely (48.3).
Otherwise its restriction to that kernel is a nonprincipal quadratic
character, so exactly half of the compatible reduced classes have value one;
the prime number theorem in arithmetic progressions gives the density claim.
\(\square\)

Theorem 44.2 is the universal case (48.3).  Outside it, (48.2) is still a
large, \(k\)-independent source of zeros, but no longer a universal one.  On
the complementary classes \(\chi_s(p)=-1\), exact vanishing remains

\[
 \nexists D\mid p^2+4ck^2,
       \qquad D\equiv-p\pmod {4ck},                         \tag{48.4}
\]

including the exponent caps in (44.4).  Thus the residual event is a
congruence-plus-*moving-divisor* condition, not another genus bit.

**Computational 48.2 (the 31 unforced slices, exact range).**  For all 385
hard primes below 30,000, `verify.py (au)` independently recomputes the
following table.  Here \(G\) counts the genus-forced zeros (48.2), \(E\)
counts the additional exponent-box zeros on \(\chi_s(p)=-1\), and \(P\)
counts positive slices, so \(G+E+P=385\).  The last column gives the least
odd prime \(q\) for which a fixed-divisor guarantee exists and one such hard
class \(p\equiv r\pmod M\); its meaning is proved in Theorem 48.4.  The
finite minimality of \(q\), as well as the displayed class, is checked
exactly.

\[
\begin{array}{c|r|rrr|c}
(c,k)&ck&G&E&P&q:r\pmod M\\ \hline
(5,1)&5&185&35&165&3:97\ (120)\\
(7,1)&7&182&148&55&11:73\ (1848)\\
(10,1)&10&185&128&72&7:73\ (840)\\
(11,1)&11&181&92&112&3:217\ (264)\\
(13,1)&13&188&146&51&7:1657\ (2184)\\
(14,1)&14&182&117&86&23:1489\ (3864)\\
(15,1)&15&185&163&37&23:457\ (2760)\\
(17,1)&17&186&117&82&3:337\ (408)\\
(19,1)&19&181&155&49&7:601\ (3192)\\
(20,1)&20&185&149&51&7:313\ (1680)\\
(21,1)&21&182&159&44&11:409\ (1848)\\
(22,1)&22&181&184&20&23:1033\ (6072)\\
(23,1)&23&173&173&39&3:457\ (552)\\
(26,1)&26&188&130&67&7:97\ (2184)\\
(28,1)&28&182&189&14&23:3673\ (7728)\\
(29,1)&29&189&136&60&3:577\ (696)\\
(30,1)&30&185&168&32&23:337\ (2760)\\ \hline
(5,2)&10&185&108&92&7:313\ (840)\\
(7,2)&14&182&176&27&23:145\ (3864)\\
(10,2)&20&185&155&45&7:1273\ (1680)\\
(11,2)&22&181&145&59&23:769\ (6072)\\
(13,2)&26&188&165&32&7:409\ (2184)\\
(14,2)&28&182&155&48&23:3001\ (7728)\\
(15,2)&30&185&178&22&23:937\ (2760)\\ \hline
(5,3)&15&185&163&37&23:577\ (2760)\\
(7,3)&21&182&166&37&11:241\ (1848)\\
(10,3)&30&185&163&37&23:217\ (2760)\\
(5,4)&20&185&136&64&7:73\ (1680)\\
(7,4)&28&182&186&17&23:313\ (7728)\\
(5,5)&25&185&140&60&3:97\ (600)\\
(5,6)&30&185&174&26&23:1177\ (2760)
\end{array}                                                  \tag{48.5}
\]

In particular, all 31 slices have both a proved positive-density vanishing
subfamily, by Theorem 48.1, and a proved positive-density positivity
subfamily, by their displayed progression and Dirichlet's theorem.  This
proves, not merely observes, that the universal-zero classification inside
\(ck\leq30\) is exactly the 80 slices of Theorem 44.2.  There is no extra
\((c,k)\)-joint universal family in this box; in particular no special
\(k\) makes a squarefree \(c\)-core 5, 7, or 10 identically vanish.  The
genus count \(G\) is independent of \(k\), while the residual \(E\) changes
substantially with \(k\), as expected of the moving norms.

For a descriptive frequency classification, the observed vanishing
percentage \((G+E)/385\) falls in the following bands:

\[
\begin{array}{c|c|l}
\hbox{band}&\#& (c,k)\\ \hline
[50,70)\%&1&(5,1)\\
[70,80)\%&4&(11,1),(14,1),(17,1),(5,2)\\
[80,90)\%&14&(7,1),(10,1),(13,1),(19,1),(20,1),(21,1),(23,1),
 (26,1),(29,1),(10,2),(11,2),(14,2),(5,4),(5,5)\\
[90,95)\%&10&(15,1),(22,1),(30,1),(7,2),(13,2),(15,2),
 (5,3),(7,3),(10,3),(5,6)\\
[95,100]\%&2&(28,1),(7,4).
\end{array}                                                  \tag{48.6}
\]

These bins are census summaries, not limiting-density estimates.  In
particular the table does not turn the residual event \(E\) into a fixed
congruence condition; Lemma 44.4 already warns against that inference.

### 48.2 Conspiracy depth and its finite growth

For a hard prime \(p\), define the unforced box

\[
 \mathcal U_p(B)=\{(c,k)\in\mathcal B_p:ck\leq B,
              \operatorname {sf}(c)\notin\{1,2,3,6\}\}.     \tag{48.7}
\]

The **conspiracy depth** is

\[
 D(p)=\sup\{B\in\mathbb Z_{\geq0}:
          M_{c,k}(p)=0\ \hbox{for every }(c,k)\in\mathcal U_p(B)\},
                                                               \tag{48.8}
\]

with values in \(\mathbb Z_{\geq0}\cup\{\infty\}\).  This definition
intersects the genuine admissible set \(\mathcal B_p\), so it remains valid
beyond the uniform small box.  It also ignores the deterministic padding of
Theorem 44.2.  If an unforced positive slice existed at product one, the
convention would give \(D=0\); in the present hard-prime problem the first
possible unforced product is five, so every \(D(p)\geq4\).

Put

\[
 ck_{\min}(p)=\min\{ck:(c,k)\in\mathcal B_p,
       \operatorname {sf}(c)\notin\{1,2,3,6\},\ M_{c,k}(p)>0\},
                                                               \tag{48.9}
\]

with minimum \(\infty\) when the set is empty.  Product order makes the
boundary exact:

\[
 ck_{\min}(p)<\infty\quad\Longrightarrow\quad
                  D(p)=ck_{\min}(p)-1;                      \tag{48.10}
\]

if the minimum is infinite, then \(D(p)=\infty\).  There is no rounding by
the number of pairs on a product hyperbola.

**Computational 48.3 (exact depth census).**  Streaming in increasing
\(ck\), `verify.py (au)` finds a positive slice for every hard prime below
30,000 by \(ck=77\).  The complete histogram is

\[
\begin{array}{c|rrrrrrrrrrrr}
D&4&6&9&10&12&13&16&18&20&21&22&25\\
\#&165&29&30&66&13&19&18&4&6&3&2&10\\ \hline
D&27&28&30&33&34&37&38&41&43&58&66&76\\
\#&3&2&1&2&1&3&1&2&1&2&1&1
\end{array}                                                  \tag{48.11}
\]

and the strict records are

\[
\begin{array}{c|rrrrrrrrr}
p&73&193&241&769&1321&2281&2521&9601&12289\\
D(p)&6&9&10&12&20&25&37&66&76\\
w^*(p)&3&3&7&7&7&3&15&7&11.
\end{array}                                                  \tag{48.12}
\]

Thus the 15 depth-111 conspiracies in (44.18) mean \(D\geq30\), not
\(D=111\): their first positive products range from 31 through 77.  The
record holder is \(12289\), with first positive slice \((c,k)=(11,7)\).
The dyadic maxima, with natural-log comparisons evaluated at the attaining
prime, are

\[
\begin{array}{c|r|r|r|r}
[p_0,p_1)&\#p&\max D&\hbox{attained at}&D/\log p\ ;\ D/(\log p)^2\\ \hline
[64,128)&2&6&73&1.398\ ;\ .326\\
[128,256)&2&10&241&1.823\ ;\ .332\\
[256,512)&5&10&409&1.663\ ;\ .277\\
[512,1024)&6&12&769&1.806\ ;\ .272\\
[1024,2048)&16&20&1321&2.783\ ;\ .387\\
[2048,4096)&31&37&2521&4.724\ ;\ .603\\
[4096,8192)&58&27&8161&2.998\ ;\ .333\\
[8192,16384)&99&76&12289&8.071\ ;\ .857\\
[16384,30000)&166&58&29569&5.634\ ;\ .547
\end{array}                                                  \tag{48.13}
\]

This is irregular finite-range growth, not evidence for either logarithmic
scale.  The optional `ES_FULL_SCAN=1` extension covers all 1,181 hard primes
below \(10^5\): the two later depth records are \((55441,82)\) and
\((92401,102)\), and every prime has \(ck_{\min}\leq103\).  It is likewise
only a computation.

For comparison with §19, recomputation of the interleaved criterion minimum
\(w^*\) on the 385-prime overlap gives Pearson correlation \(0.525121\) and
tied-rank Spearman correlation \(0.568502\) with \(D\).  Broken down by
\(w^*\),

\[
\begin{array}{c|rrrrrr}
w^*&3&7&11&15&23&31\\
\#&304&62&14&2&2&1\\
\operatorname {mean}D&7.303&17.258&27.143&26.500&21.000&38.000\\
\max D&37&66&76&37&30&38.
\end{array}                                                  \tag{48.14}
\]

**Measured/informational only (wave-16 review repair).**  The finite-census
association is nonzero but far from an identification: \(9601\) has
\((D,w^*)=(66,7)\), while the §19 record prime \(21169\) has \((38,31)\).
The two statistics inspect different factorizations; no population
correlation or growth law is inferred.  In particular the global record
\(w^*\leq71\) through \(10^{10}\) gives no bound on \(D\).

### 48.3 Every fixed-divisor guarantee, and its residue-one escape

The infinite union in (44.6) has an exact finite component whenever its
divisor is fixed.

**Theorem 48.4 (complete fixed-divisor progression law; proved).**  Fix
\((c,k)\), put \(h=4ck\), and fix a positive integer \(d\) prime to \(h\).
Let

\[
                         L=\operatorname {lcm}(24,h,d).      \tag{48.15}
\]

A reduced class \(r\pmod L\) is a hard-prime class on which the *fixed
divisor \(d\)* guarantees \(M_{c,k}(p)>0\) if and only if

\[
 r\equiv1\pmod {24},\qquad r\equiv-d\pmod h,
 \qquad r^2\equiv-4ck^2\pmod d.                            \tag{48.16}
\]

Every prime in such a class for which \((c,k)\in\mathcal B_p\) has the
explicit row

\[
 e={p^2+4ck^2\over d},\qquad
 a={p+d\over h},\qquad b={p+e\over h},
 \qquad p(a+b)=k(4abc-1).                                  \tag{48.17}
\]

Conversely, within the proof shape “one specified \(d\) divides the norm and
has the target grade,” (48.16) is necessary.  Thus the theorem is complete
for that shape.  Classes modulo a multiple of \(L\) are guarantees exactly
when they refine one of the classes (48.16).

*Proof.*  The last congruence in (48.16) is exactly
\(d\mid p^2+4ck^2\), and the middle one is exactly
\(d\equiv-p\pmod h\).  Theorem 44.1 proves sufficiency and necessity.
Since the norm is \(p^2\pmod h\), its cofactor \(e\) has the same target
grade; (48.17) is integral and direct expansion proves its last identity.
The first congruence is precisely the hard-prime restriction. \(\square\)

For an odd prime \(d=q\nmid2ck\), the last condition has two roots exactly
when \((-4c\mid q)=1\), and one obtains the CRT classes

\[
 p\equiv-q\pmod h,
 \qquad p\equiv\pm2k\sqrt{-c}\pmod q,
 \qquad p\equiv1\pmod {24}.                                \tag{48.18}
\]

Hard compatibility forces \(q\equiv3\pmod4\), and more precisely
\(q\equiv-1\pmod{(h,24)}\), together with root compatibility when
\(q\mid24\).  Every prime-divisor class in (48.5) and (48.19) is exactly
Lemma 29.2 intersected with the hard progression; no new fixed-prime-divisor supply is
claimed.  Corollary 44.3 is \((c,k,q)=(5,1,3)\).  Theorem 35.4's
\(c=5,D=3\) branch supplies the same hard progression but a different row
and slice: at \(p=97\) it gives \((a,b,c,k)=(1,34,5,5)\), whereas
Corollary 44.3 gives \((5,162,5,1)\).  Thus the progression dictionary is
literal, but the rows must not be identified.  *(wave-16 review repair)*

**Computational 48.4a (finite prime-divisor list; wave-16 review repair).**
The complete list generated from (48.18) with \(ck\leq30\) and prime divisor
\(q\leq7\) is

\[
\begin{array}{c|l}
q& (c,k):\ r\pmod M\\ \hline
3&(5,1):97(120),\ (11,1):217(264),\ (17,1):337(408),\\
 & (23,1):457(552),\ (29,1):577(696),\ (5,5):97(600)\\
5&\varnothing\\
7&(5,1):433,673(840),\ (10,1):73,193(840),\\
 &(13,1):1657,1969(2184),\ (17,1):1081,2713(2856),\\
 &(19,1):601,1513(3192),\ (20,1):313,793(1680),\\
 &(26,1):97,1345(2184),\ (5,2):313,793(840),\\
 &(10,2):1273,1513(1680),\ (13,2):409,1033(2184),\\
 &(5,4):73,1033(1680),\ (5,5):793,1993(4200).
\end{array}                                                  \tag{48.19}
\]

This is an exact enumeration of all 30 hard-compatible classes in that
stated small-prime-divisor range, not a selection of successful examples.
`verify.py (au)` generates the list rather than trusting it, scans every
prime in each class below 30,000, and verifies \(q\), \(e\), \(a\), and
\(b\) in (48.17).  Table (48.5) extends existence to all 31 unforced slices
by allowing the least \(q\leq23\); only one class is displayed there when
two roots survive.

The progression mechanism itself has the same compactness wall as the
identity classes of §17.

**Theorem 48.5 (residue-one escape for every bounded fixed-divisor slice
system; proved).**  No class (48.16) contains the residue \(1\pmod L\).
Consequently, for every \(Q\), the union of *all* fixed-divisor slice
guarantees (48.16) with full modulus \(L\leq Q\) misses the class

\[
 p\equiv1\pmod {\Lambda_Q},\qquad
 \Lambda_Q=\operatorname {lcm}\{24,L:L\leq Q\hbox{ occurs in (48.15)}\},
                                                               \tag{48.20}
\]

which contains infinitely many primes.

*Proof.*  If residue one belonged to a guarantee, then
\(d\equiv-1\pmod h\) and \(d\mid1+4ck^2=1+hk\).  Its complementary divisor
\(e=(1+hk)/d\) would also be \(-1\pmod h\).  Hence \(d,e\geq h-1\), but

\[
 (h-1)^2-(1+hk)=h(h-k-2)>0,
 \qquad h-k-2=k(4c-1)-2\geq1,                              \tag{48.21}
\]

which is impossible.  There are only finitely many triples \((c,k,d)\) with
\(L\leq Q\), and residue one modulo their common multiple misses each
class.  Dirichlet's theorem gives infinitely many primes in (48.20).
\(\square\)

The scope is exact and limited.  Theorem 48.5 walls every finite or
bounded-modulus proof assembled from a preassigned norm divisor, including
composite \(d\); it does not wall a proof that controls the actual moving
factorization.  A prime escaping all guarantees can still have a positive
slice through a divisor depending on that prime.  Indeed (48.11) says that
most census primes do.  “Not guaranteed” must not be read as “vanishing,”
and the theorem supplies no infinite conspiracy sequence.

### 48.4 The sharp reformulation and what existing bounds do not say

**Proposition 48.6 (Type-I depth equivalence; proved bookkeeping).**  The
Type-I strengthening of Erdős--Straus on the hard primes is equivalent to

\[
             D(p)<\infty\qquad\hbox{for every prime }p\equiv1\pmod {24}.
                                                               \tag{48.22}
\]

More quantitatively, a function \(F\) gives the assertion

\[
              ck_{\min}(p)\leq F(p)\quad\hbox{for every hard }p
                                                               \tag{48.23}
\]

if and only if \(D(p)\leq F(p)-1\) (with integer floors understood).  The
natural pointwise target suggested by §§17.6 and 19 is the log-power
strengthening

\[
                 ck_{\min}(p)\leq(\log p)^A                \tag{48.24}
\]

for some absolute \(A\).  It is **OPEN**.

*Proof.*  A positive raw slice gives positive integers \(a,b,c,k\) satisfying
the Type-I equation by Theorem 36.1, and hence an Erdős--Straus
representation; coprimality of \(a,b\) is not needed for existence.
Conversely every Type-I representation has its canonical tuple in
\(\mathcal B_p\) and makes that slice positive.  Its squarefree \(c\)-core
cannot be in (48.3), by Theorem 44.2.  Thus it is counted by (48.9), and
(48.10) proves all assertions. \(\square\)

This equivalence is bookkeeping, not progress on positivity.  In particular,
no existing exceptional-set theorem in this document supplies a hidden bound
on \(ck_{\min}\):

* Lemma 16.1's multiplier classes are, through Lemma 29.1, the complete
  fixed-divisor **Type-II** (Case-B) class supply.  Theorem 16.4's
  CLAIMED/PROVISIONAL bound
  \(N\exp\{-c(\log N)^{2/3}(\log\log N)^{1/3}\}\) therefore proves that
  almost every prime gets a representation of that broader type; it does not
  construct any Type-I \((c,k)\).
* The same directional issue applies to the CLAIMED/PROVISIONAL §39
  cubic-rate assembly.  Its \(\exp\{-c(\log N)^{3/4}\}\) exceptional set is
  built from the same multiplier identities, so it has no literal
  \(ck_{\min}\) consequence either.
* Lemma 29.2 does supply Type-I slices: a class with displayed modulus
  \(4ckq\leq X\) has \(ck\leq X/(4q)\).  But §29 proves only the raw
  \(O((\log X)^2\log\log X)\) class-mass envelope and no joint coverage or
  exceptional-set theorem for those classes.  Thus that inequality cannot be
  promoted to an almost-all bound on \(ck_{\min}\).

**Informational only (wave-16 review repair).**  The finite \(a=1\) result
through \(10^7\) in §35 and the depth computations above are consistent with
(48.24), and with many competing growth laws, but do not support a growth
law.  Neither supplies an all-large-prime bound.  Proving merely
\(D(p)<\infty\) for every hard prime would already prove the Type-I
strengthening; bounding it by a log-power is a sharper
pointwise conjecture, not an implication of the campaign's present
exceptional-set estimates.

**Verification companion.**  `verify.py (au)` stores at most one residue set
of size \(4ck\) per requested norm.  It recomputes the 31 rows of (48.5),
the 80+31 split and all §44 aggregate counts, every value behind
(48.11)--(48.14), the least-prime guarantee in each row, all 30 classes in
(48.19), and the explicit divisor reconstruction (48.17).  The optional
`ES_FULL_SCAN=1` path extends the streamed prime/depth scan and the
fixed-guarantee row replays to \(10^5\).  *(wave-16 review repair)*


## 49. The implication-reduced antichain: structure, residue-resolved profiles, and the surviving hierarchy question

The implication reduction of §47.4 has an exact divisor-poset description
and preserves the void pointwise.  It also preserves every upper
first-moment and ledger bound needed in §37.  It does **not**, however,
repair the high-moment route.  Fixed-\(D\) semiprime atoms are already
maximal, remain residue-concentrated, and form complete bipartite grids.  A
matching of grid edges collectively implies every cross edge although no
one edge implies another.  This gives a new counterexample both to the
reduced one-step hierarchy (47.16) and to (37.19) for the reduced count
itself.  These are refutations of a proposed sufficient mechanism, not of
(33.16), \(H_{\rm PF}'\), or the Erdős--Straus conjecture.

### 49.1 Exact antichain structure and the void

Let \(\mathcal A^\circ_X\) denote the finite §37-retained family counted by
\(H\): the tail prime atoms and the composite atoms after the prime-implied
deletion.  Its classes are deduplicated.  For an intrinsic class
\(r\pmod M\), put

\[
 \delta_M(r)=\min\{D:D\mid A_M^2,\ -4D\equiv r\pmod M\},
 \qquad A_M={M+1\over4}.                                  \tag{49.1}
\]

Thus an atom can be written unambiguously as \((M,r)\), with
\(D=\delta_M(r)\) retained only as a canonical divisor label.

**Theorem 49.1 (exact implication criterion; proved).**  For two distinct
retained atoms,

\[
 E_{M,r}\subseteq E_{m,s}
 \quad\Longleftrightarrow\quad
 m\mid M\ \hbox{ and }\ r\equiv s\pmod m
 \quad\Longleftrightarrow\quad
 m\mid M\ \hbox{ and }\
 \delta_M(r)\equiv\delta_m(s)\pmod m.                    \tag{49.2}
\]

If \(M=tm\), the intrinsic conditions in (49.2) unpack exactly as

\[
 t\equiv1\pmod4,
 \qquad A_M=tA_m-{t-1\over4},
 \qquad D=D'+jm\quad(j\in\mathbb Z),                     \tag{49.3}
\]

where \(D\mid A_M^2\), \(D'\mid A_m^2\), and both corresponding classes
survive the §37 deletions.  There is no additional ``division by four''
condition: every participating modulus is odd, so multiplying the class
congruence by \(-4^{-1}\pmod m\) gives precisely \(D\equiv D'\pmod m\).
At one modulus, distinct retained classes are disjoint and cannot nest.

Consequently the implication antichain is exactly

\[
 \mathcal A^\dagger_X=
 \{(M,r)\in\mathcal A^\circ_X:
   \nexists\,(m,s)\in\mathcal A^\circ_X,
   \ m<M,
   \ m\mid M,
   \ s\equiv r\pmod m\}.                                 \tag{49.4}
\]

In words, its moduli are divisibility-minimal along each compatible class
tower.  This is only a partial-order statement: incomparable minimal moduli
can carry projections of the same integer class.

*Proof.*  An integer in \(E_{M,r}\) is congruent to \(r\) modulo \(M\).
This cylinder is contained in \(E_{m,s}\) exactly when reduction modulo
\(m\) is defined and equals \(s\), which is the first equivalence in
(49.2).  Since \((4,m)=1\), the second follows from (49.1).  Reducing
\(M=tm\) modulo four and comparing \(4A_M=M+1\) with \(4A_m=m+1\) gives
(49.3).  Deduplication excludes strict nesting at equal modulus, so (49.4)
is exactly the set of inclusion-maximal events. \(\square\)

**Corollary 49.2 (pointwise void identity; proved).**  If
\(H^\dagger\) counts \(\mathcal A^\dagger_X\), then on every integer and
also pointwise inside the \(T_0=1\) fibre,

\[
                  H=0\quad\Longleftrightarrow\quad H^\dagger=0.
                                                                    \tag{49.5}
\]

*Proof.*  If a deleted event is hit, (49.4) supplies a strictly larger
retained event containing it.  Repeating strictly decreases the modulus and
therefore terminates at an event in \(\mathcal A^\dagger_X\).  Thus the
unions of the two finite families are equal.  The reverse inclusion is
immediate. \(\square\)

This verifies the orientation in §47.4: the **largest events under
inclusion**, equivalently the divisibility-minimal compatible moduli, are
kept.  Keeping the finest events instead would not preserve the union.

### 49.2 What first-moment mass is actually preserved

Write \(w_A=\Pr(A\mid T_0=1)\), as in (47.2), and
\(\mu=\sum_{\mathcal A^\circ_X}w_A\),
\(\mu^\dagger=\sum_{\mathcal A^\dagger_X}w_A\).  Positivity and §37 give

\[
 \Theta(L^2)=\mu_P\leq\mu^\dagger\leq\mu=O(\Lambda),
 \qquad \Lambda={L^3\over\log L}.                         \tag{49.6}
\]

Here every tail prime atom is maximal and survives, giving the first
inequality by (37.6).  The last inequality is the actual result quoted in
§37.3; the record does **not** prove \(\mu=\Theta(\Lambda)\).  Therefore a
claim that implication reduction preserves a \(\Theta(\Lambda)\) first
moment would currently have an unproved premise.  All upper charge, degree,
modulus, and coefficient-ledger estimates only improve, while the void
probability is unchanged by (49.5).

The §47 divisor cube loses negligible mass under this reduction.  In the
notation of Theorem 47.2, put \(s=\sum_i1/p_i=o(1)\).  The surviving
singleton edges have mass \(s/q\), whereas the deleted odd subsets of size
at least three have total mass

\[
 {1\over2q}\left\{\prod_i(1+p_i^{-1})-
                         \prod_i(1-p_i^{-1})\right\}-{s\over q}
       =O\!\left({s^3\over q}\right).                     \tag{49.7}
\]

Thus that counterexample is removed at relative mass cost \(O(s^2)\).

**Failure log 49.3 (general lower mass).**  No constant-factor lower bound
\(\mu^\dagger\gg\mu\), and no asymptotic for the deleted mass, is proved.
A deleted atom can have many divisor-containers, while the available
shifted-divisor mean theorems are upper bounds and do not resolve that
multiplicity.  This missing lower bound does not affect the conclusions
below: their obstruction is carried entirely by atoms which provably
survive.

### 49.3 Residue concentration survives maximality

For a divisor \(g\) and a reduced class \(a\pmod g\), define the direct
analogue of the requested profile by

\[
 W^\dagger_{g,a}=
  \sum_{A\in\mathcal A^\dagger_X\atop
        g\mid M_A,
        r_A\equiv a\ (g)}w_A,
 \qquad
 W^\dagger_g=\sum_{a\ (g)}W^\dagger_{g,a}.                \tag{49.8}
\]

**Theorem 49.4 (uniform \(1/\varphi(g)\) profile is false; proved).**  There
is no absolute \(C\) for which

\[
       W^\dagger_{g,a}\leq {C\over\varphi(g)}W^\dagger_g  \tag{49.9}
\]

holds uniformly in \(X,g,a\).  In fact there are \(g\asymp X\) and reduced
\(a\pmod g\) for which the ratio between the two sides without \(C\) is
\(g^{1-o(1)}\).

*Proof.*  By the prime number theorem in fixed classes modulo eight, choose
primes \(q\equiv3\pmod8\) and \(p\equiv5\pmod8\), both in
\((3X^{1/2}/4,4X^{1/2}/5)\).  Then
\(X/2<M=qp<X\).  Both exceed \(z\) and \(Y\) for large \(X\).  Since
\(M\equiv7\pmod8\), \(2\mid A_M\), and the \(D=2\) atom

\[
                         n\equiv-8\pmod M                  \tag{49.10}
\]

is intrinsic.  Its projection modulo \(q\) has Legendre sign
\((-8/q)=+1\), whereas Lemma 21.2 gives sign \(-1\) for every intrinsic
prime-modulus class.  The other prime is \(1\pmod4\).  Hence (49.10)
survives the prime deletion.  Its only proper modulus divisors are
\(1,q,p\); none carries a retained atom in this class.  Theorem 49.1
therefore puts it in \(\mathcal A^\dagger_X\).

Take \(g=M\) and \(a=-8\).  As \(2M>X\), every atom counted by
\(W^\dagger_g\) has modulus exactly \(M\), and all have weight \(1/M\).
The number of such atoms is at most
\(F(M)\leq\tau(A_M^2)=M^{o(1)}\), while the bin \(a\) contains (49.10).
Consequently

\[
 {\varphi(g)W^\dagger_{g,a}\over W^\dagger_g}
 \geq {\varphi(M)\over F(M)}=M^{1-o(1)},                  \tag{49.11}
\]

which proves the assertion. \(\square\)

The same failure is visible without taking \(g\) large.  For a fixed
\(q\equiv3\pmod8\), every surviving semiprime atom
\(E_{qp,-8}\), with \(p\equiv5\pmod8\), lies in the single projection
\(-8\pmod q\).  Antichain reduction removes nested divisor cubes but cannot
remove this fixed-\(D\) slice because semiprime moduli have no eligible
proper composite divisor.  This proves concentration of the slice, not
failure of an aggregate profile restricted to small \(g\); such a restricted
or averaged estimate remains possible.  The uniform profile needed for a
literal transplant of §39.2 is nevertheless false.

### 49.4 Collective implication refutes the reduced hierarchy

The surviving fixed-\(D\) slice has a stronger consequence.  Choose distinct
primes

\[
 q_1,\ldots,q_t\equiv3\pmod8,
 \qquad p_1,\ldots,p_t\equiv5\pmod8,                      \tag{49.12}
\]

all greater than \(z\) and with every product \(q_ip_j<X\).  Every edge

\[
                  A_{ij}:\quad n\equiv-8\pmod {q_ip_j}     \tag{49.13}
\]

is a retained maximal atom by the proof of Theorem 49.4.  Thus these atoms
form a complete bipartite grid inside \(\mathcal A^\dagger_X\).

**Theorem 49.5 (collective-closure obstruction; proved).**  The repaired
hierarchy (47.16) is false.  More strongly, for every fixed \(C,D>0\), every
sufficiently large \(X\), and **every** even integer
\(m\in[D\Lambda,D\Lambda+2]\), there is a compatible, pairwise-coprime,
squarefree selected set \(S\subset\mathcal A^\dagger_X\), \(|S|<m\), for
which

\[
                         \mathcal L^\dagger(S)>C\Lambda.   \tag{49.14}
\]

The factorial-moment input itself also fails: for the same fixed \(C,D\),

\[
                 \mathbb E((H^\dagger)_m\mid T_0=1)
                         >(C\Lambda)^m                    \tag{49.15}
\]

for all sufficiently large \(X\).  (wave-17 review repair)

*Proof of the hierarchy assertion.*  Take the diagonal matching
\(S=\{A_{ii}:1\leq i\leq t\}\).  Its merged class is \(-8\) modulo

\[
                         Q_S=\prod_{i=1}^tq_ip_i.           \tag{49.16}
\]

For every \(i\ne j\), the candidate modulus \(q_ip_j\) divides \(Q_S\)
and its class is the projection of the merged class.  Proposition 47.1, or
direct event inclusion, therefore gives the exact conditional extension
ratio

\[
 {\Pr(\bigcap_{A\in S}A\cap A_{ij}\mid T_0=1)
   \over\Pr(\bigcap_{A\in S}A\mid T_0=1)}=1.              \tag{49.17}
\]

Choose \(t=m-1\).  The prime number theorem in either required class gives
\[
 \#\{z<r\leq B_DL^3:r\equiv a\pmod8\}
   =\left({B_D\over12}+o(1)\right){L^3\over\log L}
 \qquad(a=3,5),
\]
because the primes at most \(z=o(L^3)\) contribute \(o(\Lambda)\).
Thus any fixed \(B_D>12D\) supplies the primes in (49.12).  All products are
\(O_D(L^6)<X\).  The selected moduli are pairwise coprime and squarefree.
(wave-17 review repair)  The \(t(t-1)\) off-diagonal edges in (49.17) give
\(\mathcal L^\dagger(S)\geq t(t-1)>C\Lambda\).  Notice the new logical
point: no selected edge contains a cross edge, but their **intersection**
does.

For (49.15), instead put

\[
                   t=\left\lfloor {m\over2\log(2z)}\right\rfloor.  \tag{49.18}
\]

There are enough primes of each required class in \((z,2z)\): their number
is asymptotic to \(z/(4\log z)\), while (31.11) and (49.18) give a ratio
\(\asymp\log\log L\) to \(t\).  Put
\(R=\prod_iq_ip_i\) and let \(C_R\) be the event
\(n\equiv-8\pmod R\).  At every conditioned \(q_i\), the class \(-8\) is
allowed by Lemma 21.2, so

\[
 \Pr(C_R\mid T_0=1)
 ={1\over R}\prod_{q_i\leq Y}{q_i\over q_i-f(q_i)}
 \geq {1\over R}.                                         \tag{49.19}
\]

On \(C_R\), all \(t^2\) atoms (49.13) occur.  Since
\(R\leq(2z)^{2t}\), \(t^2\geq2m\) for large \(X\), and
\((u)_m\geq(u/2)^m\) for \(u\geq2m\),

\[
 \mathbb E((H^\dagger)_m\mid T_0=1)
 \geq{(t^2)_m\over R}
 \geq\left({t^2\over2}\right)^m(2z)^{-2t}.               \tag{49.20}
\]

After division by \((C\Lambda)^m\), the logarithm of the right side is at
least

\[
 m\log\!\left({t^2\over2C\Lambda}\right)-2t\log(2z).
                                                                    \tag{49.21}
\]

The second term is at most \(m\), while
\(t^2/\Lambda\gg_D\Lambda/(\log z)^2\to\infty\).  Hence (49.21) tends to
\(+\infty\), proving (49.15). \(\square\)

The smallest collective pattern is already a \(2\)-by-\(2\) square: the
compatible diagonal atoms at moduli \(q_1p_1,q_2p_2\) jointly imply the two
off-diagonal atoms, although all four are an antichain.  This is the exact
new wall configuration.  Proposition 47.3's prime-only rung remains valid.
For a singleton selected composite atom, antichain reduction does at least
remove every candidate whose whole modulus divides the selected modulus,
but no \(O(\Lambda)\) bound for all remaining singleton extensions is
claimed.  Pairwise-coprime and squarefree selected sets do not help, by
Theorem 49.5.

### 49.5 Severity audit, computation, and verdict

**Self-review 49.6 (maximum-severity checks; proved bookkeeping).**  Four
possible escapes from Theorem 49.5 have been checked explicitly.

* The inclusion orientation is the one proved in Theorem 49.1; every
  semiprime edge is inclusion-maximal, not accidentally minimal.
* The §37 prime deletion does not remove \(-8\): its sign at every
  \(q_i\equiv3\pmod8\) is opposite to all intrinsic prime classes, and a
  \(p_j\equiv1\pmod4\) has no prime atom in this system.
* Conditioning cannot thin a forced cross edge.  Its coordinates already
  occur in \(Q_S\), so (49.17) is exactly one; (49.19) also checks that the
  forcing event is compatible with \(T_0\).
* Equation (49.15), unlike failure of a sufficient one-step induction, is a
  direct lower bound for the reduced factorial moment.  It still says
  nothing adverse about the void itself, which is unchanged.

The scope boundaries are also exact.  Restricting to bounded
\(\omega(M)\) does not help these formulations, since every grid atom has
\(\omega(M)=2\).  On the other hand, the theorem does not rule out a
weighted or tilted count, a redesigned conditioning selector that makes the
grid atoms impossible, or a different pointwise minorant; any such proposal
would need a new pointwise comparison with the full void and the §37
critical-window ledger.  Simply deleting grid atoms can enlarge the void and
gives no pointwise minorant inequality without a separate collective-
redundancy proof.  Theorem 49.1 exhausts single-cylinder implication, but it
does not prove that no further
collective void-preserving reduction exists; the diagonal intersection's
containment in each cross edge does not itself make any cross edge redundant
in the union.  Thus Theorem 49.5 refutes exactly (47.16) and the ordinary
factorial moment for \(H^\dagger\), not every conceivable construction for
Lemma 33.3.  (wave-17 review repair)

**Computational 49.7 (exact finite scope).**  `verify.py (av)` implements
(49.4) by divisor enumeration, never by a full-period array.  In the
composite, fully conditioned toy \((X,z,Y)=(1000,2,1000)\), it reduces
1,042 retained atoms to 970: \(72/1042=6.91\%\) of atoms are deleted, and
the exact conditional first-moment share retained is
\(0.939936\ldots\).  Every deleted cylinder is certified to lie in a final
maximal cylinder, proving the full-space void equivalence symbolically.  The
largest normalized profile in this toy is

\[
 \max_{g,a}{\varphi(g)W^\dagger_{g,a}\over W^\dagger_g}=220
 \quad(g=943,\ \max_aW^\dagger_{g,a}/W^\dagger_g=1/4).    \tag{49.22}
\]

For the complete \((40,2,7)\) toy, implication reduction happens to delete
nothing.  Exact enumeration of every compatible selected set through size
three gives \(K=28\),
\(\Lambda_{\rm toy}=27839083/19372210\), compatible-set counts
\((28,316,1868)\), and

\[
 {\max\mathcal L^\dagger(S)\over\Lambda_{\rm toy}}
 =\left({31713525\over27839083},
         {38419290\over27839083},
         {35360520\over27839083}\right)                  \tag{49.23}
\]

for \(|S|=1,2,3\).  Finally the exact square
\((q_1,q_2;p_1,p_2)=(3,11;5,13)\) checks that selected moduli \(15,143\)
jointly force the atoms at \(39,55\), each with extension ratio one.  With
`ES_FULL_SCAN=1`, the reduction toy extends to
\((5655,5,5655)\): \(6210\to6140\) atoms and conditional mass share
\(0.992549\ldots\).  These finite fractions are diagnostics, not asymptotic
evidence.

**Assessment 49.8 (wave-17 verdict).**  The implication-antichain structure
and pointwise void preservation are proved.  Existing upper mass and ledger
bounds survive, but a \(\Theta(\Lambda)\) reduced first moment is not known.
The uniform residue profile, the repaired hierarchy (47.16), and (37.19)
for \(H^\dagger\) are all **REFUTED** by maximal fixed-\(D=2\) semiprime
grids.  The failure is collective implication by an intersection, not the
single-event nesting removed in §47.  Therefore Proposition 37.3's
odd-Bonferroni route remains unavailable even after implication reduction.
The pair endpoint (40.19), the existence of some different pointwise
minorant proving (33.16), (33.16) itself, and \(H_{\rm PF}'\) remain
**OPEN**.  Nothing here proves or refutes the Erdős--Straus conjecture.
## 50. Conditional pointwise routes through the slice frame

**Scope and verdict.**  This section isolates a one-prime-factor event which
is sufficient for a Type-I solution and states the corresponding clean
conditional theorem.  The hypothesis is deliberately labelled **bespoke and
unproved**: none of Bateman--Horn, Linnik, GRH for Dirichlet/Hecke/ray-class
L-functions, Elliott--Halberstam, or Duke-type equidistribution has this
pointwise factorization conclusion in its standard form.  The audit below
makes the quantifier failure exact.  Two proved walls sharpen §17.5 using
§§44 and 48: prime values of the norm have the wrong grade, and any bounded
collection of squarefree cores is simultaneously genus-forced on infinitely
many hard primes.  Thus the deliverable is a rigorous conditional reduction
and a map of its missing input, not an unconditional theorem and not a claim
that a standard conjecture secretly settles Erdős--Straus.

### 50.1 The good prime-factor class and the exact reduction

Fix a hard prime \(p\), an admissible slice \((c,k)\in\mathcal B_p\), and
write

\[
 c=st^2,\quad s=\operatorname {sf}(c),\qquad
 h=4ck,\qquad N=N_{c,k}=p^2+4ck^2.                         \tag{50.1}
\]

Inflate the primitive genus character \(\chi_s=(\Delta_s/\,\cdot\,)\) to
\((\mathbb Z/h\mathbb Z)^\times\); this is legitimate because its conductor
divides \(4s\mid h\).  Put

\[
 K_s(h)=\ker\chi_s,\qquad
 \mathcal G_p(c,k)=\{-p\pmod h\}\cap K_s(h).              \tag{50.2}
\]

This is the exact good class set for a *single prime factor*.  Every prime
\(q\mid N\) lies in \(K_s(h)\), by the calculation in Theorem 48.1, while

\[
 \mathcal G_p(c,k)=
 \begin{cases}
   \{-p\pmod h\},&\chi_s(p)=-1,\\
   \varnothing,&\chi_s(p)=1.
 \end{cases}                                               \tag{50.3}
\]

Indeed \(\chi_s(-1)=-1\).  Thus Theorem 48.1 is exactly the empty-good-set
case.  On an unforced class there is still only one good ray grade, not half
of the factor grades.  A split prime \(q\), or merely
\(\chi_s(q)=1\), is the **wrong kind of divisor** unless it also satisfies
\(q\equiv-p\pmod h\).

**Theorem 50.1 (one-prime-factor slice criterion; proved).**  Let \(p\) be
an odd prime and \((c,k)\in\mathcal B_p\).  If a prime \(q\) satisfies

\[
       q\mid p^2+4ck^2,
       \qquad q\pmod {4ck}\in\mathcal G_p(c,k),             \tag{50.4}
\]

then the \((c,k)\)-slice is positive and gives a Type-I Erdős--Straus
representation.  Explicitly, with

\[
 e={p^2+4ck^2\over q},\qquad
 a={p+q\over4ck},\qquad b={p+e\over4ck},                   \tag{50.5}
\]

one has \(a,b\in\mathbb Z_{>0}\) and

\[
 p(a+b)=k(4abc-1),\qquad
 {4\over p}={1\over ack}+{1\over bck}+{1\over pabc}.       \tag{50.6}
\]

Primality of \(q\) does not imply \((a,b)=1\), and no primitivity is needed
for (50.6).  For example, the good prime \(q=11\) at
\((p,c,k)=(241,7,3)\) gives \((a,b)=(3,66)\), the nonprimitive row already
recorded after (44.4a).  The canonical decomposition of Theorem 17.1(ii)
recovers a primitive Type-I tuple if one is desired.

*Proof.*  Admissibility gives \((p,ck)=1\), hence \((N,h)=1\).  In
particular \((q,h)=1\).  The grade in (50.4) says \(q\equiv-p\pmod h\), and
\(N\equiv p^2\pmod h\), so

\[
             e=Nq^{-1}\equiv p^2(-p)^{-1}\equiv-p\pmod h.
\]

This proves the integrality and positivity in (50.5).  Substitution of
\(q=ha-p\), \(e=hb-p\), and \(qe=N\), followed by cancellation of \(p^2\),
gives
\(4ck^2=h^2ab-hp(a+b)\).  Division by \(h=4ck\) is (50.6)'s first identity;
the unit-fraction identity follows over the common denominator \(pabck\).
Also \(p\nmid k\), and reduction of the first identity modulo \(p\) gives
\(4abc\equiv1\pmod p\), so exactly the denominator \(pabc\) is divisible
by \(p\).  This is Type I.  The same argument is Theorem 44.1's
complementary-divisor reconstruction, now with the sufficient divisor chosen
to be prime. \(\square\)

Here is the promised falsifiable hypothesis.  The logarithm is natural.

**Hypothesis \(H_{\rm SPF}(A)\) (slice prime factor; bespoke and unproved).**
Fix \(A>0\).  The assertion \(H_{\rm SPF}(A)\) is that there is a constant
\(p_0=p_0(A)\) such that every prime \(p>p_0\),
\(p\equiv1\pmod {24}\), admits positive integers \(c,k\) and a prime \(q\)
with

\[
 \boxed{\quad ck\leq(\log p)^A,\qquad
 q\mid p^2+4ck^2,\qquad q\equiv-p\pmod {4ck}.\quad}        \tag{50.7}
\]

This is a deliberately quantitative sufficient hypothesis, not the
logically weakest hypothesis within the one-prime-factor mechanism: deleting
the log-power bound and asking only for an admissible slice with such a prime
factor is weaker.  Within the stated log-power slice box, (50.7) puts no bound
on \(q\), prescribes no \((c,k)\), imposes no primitivity condition, and needs
no extra genus condition; the latter is automatic from (50.3).  It is
stronger than slice positivity, because a product of two or more wrong-grade
prime factors can hit the target even when no individual prime does.
Proposition 48.6 remains the weaker exact criterion without the one-prime
restriction.  *(wave-17 review repair)*

**Theorem 50.2 (conditional on \(H_{\rm SPF}(A)\); \(H_{\rm SPF}(A)\)
unproved).**  If \(H_{\rm SPF}(A)\) holds for some \(A\), then every
sufficiently large hard prime has a Type-I Erdős--Straus representation.

*Proof.*  For sufficiently large \(p\), (50.7) gives \(ck<p\),
\(3k\leq2p\), and \(4ck\leq2p+k\).  Thus \((p,ck)=1\) and
\((c,k)\in\mathcal B_p\).  The congruence in (50.7) makes \(q\) the unique
good class in (50.2), and Theorem 50.1 applies. \(\square\)

For comparison with Lemma 29.2 and (48.18), if \(q\) is fixed first then
(50.4) is exactly the pair of root progressions

\[
 p\equiv-q\pmod {4ck},\qquad
 p\equiv\pm2k\sqrt{-c}\pmod q,\qquad p\equiv1\pmod {24}.  \tag{50.8}
\]

The difference is decisive: Lemma 29.2 preassigns \(q\) and obtains a fixed
CRT class; (50.7) asks the actual factorization of the integer attached to
each \(p\) to supply some \(q\) after \(p\) is known.  Theorem 48.5 walls
every bounded-modulus collection of the former and does not wall the latter.

### 50.2 Bateman--Horn, smooth values, and least nonresidues

The most tempting prime-value formulation has exactly the wrong sign.

**Lemma 50.3 (prime norms are wrong-grade; proved).**  For a hard prime
\(p\) and any admissible \((c,k)\), if \(N_{c,k}\) is prime then the slice
vanishes.  More generally a good prime factor in (50.4) is
\(3\pmod4\), its complementary divisor is also \(3\pmod4\), and hence
\(N_{c,k}\) must be composite.

*Proof.*  The target grade is \(-p\equiv3\pmod4\), whereas
\(N_{c,k}\equiv1\pmod4\).  If \(N\) is prime, both divisors \(1,N\) have
grade \(1\pmod4\), so (44.4) misses.  Under (50.4), both \(q\) and
\(e=N/q\) have the target grade by Theorem 50.1. \(\square\)

**Assessment 50.4 (Hardy--Littlewood/Bateman--Horn).**  Standard
Bateman--Horn gives an asymptotic as a polynomial variable tends to infinity
for a *fixed* finite list of irreducible integer polynomials.  It neither
controls all external coefficients \(p\) uniformly down to a
\((\log p)^A\) interval nor prescribes a prime factor of a composite value.
Applied literally to \(p^2+4ck^2\) as a prime-value polynomial, its success
would trigger Lemma 50.3, not (50.7).  A uniform statement saying that every
coefficient \(p\) has, in a logarithmic box, a value with a factor in the
moving grade \(-p\pmod {4ck}\) would imply Theorem 50.2, but that is a
rephrasing of \(H_{\rm SPF}\), not a standard form of Bateman--Horn.
The same quantifier defect applies to Hardy--Littlewood prime tuples.

Standard conjectures on friable or smooth values also control factor sizes,
not their bounded exponent box in \((\mathbb Z/h\mathbb Z)^\times\).
Theorem 44.1 requires the actual prime-factor grades, with their exponent
caps, to generate \(-p\).  Even on \(\chi_s(p)=-1\), smoothness alone does
not say this; on \(\chi_s(p)=1\), Theorem 48.1 forbids it regardless of
smoothness.

There is also a sharp wall before factorization is considered.

**Theorem 50.5 (bounded-core genus escape; proved).**  For every fixed
\(B\), infinitely many hard primes satisfy

\[
       \chi_s(p)=1\quad\hbox{for every squarefree }s\leq B. \tag{50.9}
\]

For each such prime every admissible slice whose squarefree \(c\)-core is at
most \(B\) vanishes, for *all* \(k\).  Consequently no absolute bound for a
least active core, and no proof using only boundedly many cores with arbitrary
\(k\), can hold.

*Proof.*  Let
\(R_B=24\prod_{\substack{\ell\leq B\\ \ell\ {\rm prime}}}\ell\).
Dirichlet's theorem
gives infinitely many primes \(p\equiv1\pmod {R_B}\).  For every odd prime
\(\ell\leq B\), quadratic reciprocity and \(p\equiv1\pmod4\) give
\((\ell/p)=(p/\ell)=1\); the factor 24 gives \((2/p)=(-1/p)=1\).
Multiplicativity proves (50.9).  Theorem 48.1 then gives every asserted
slice zero.  *(wave-17 review repair)* \(\square\)

**Theorem 50.6 (conditional on GRH; GRH unproved; active slice only).**
The GRH least-quadratic-nonresidue theorem implies that every sufficiently
large hard prime \(p\) has a squarefree \(s\ll(\log p)^2\) with
\(\chi_s(p)=-1\); hence \((c,k)=(s,1)\) is an admissible unforced slice in a
logarithmic box.  This conclusion does **not** assert that the slice is
positive.

*Proof of the deduction.*  The standard Ankeny consequence of GRH gives an
integer \(n\ll(\log p)^2\) with \((n/p)=-1\).  The squarefree kernel \(s\)
of \(n\) has the same Legendre symbol and is no larger.  For
\(p\equiv1\pmod8\), \(\chi_s(p)=(-s/p)=(s/p)=-1\).  Admissibility is
automatic for large \(p\).  The residual exponent-box condition (48.4)
remains untouched. \(\square\)

Thus least-nonresidue technology supplies the missing *permission* for a
slice, but not the divisor in that slice.  Standard Linnik similarly finds a
small prime in the progression \(q\equiv-p\pmod h\), but imposes no condition
that this prime divide the fixed integer \(N_{c,k}\).  A “Linnik theorem for
the least prime in that progression which also divides
\(p^2+4ck^2\)” is exactly a bespoke version of (50.7), not an existing
Linnik hypothesis.

### 50.3 What GRH/Chebotarev says about the norm, and what it cannot say

The ideal-theoretic translation is useful because it prevents a false
Chebotarev inference.  With the notation (50.1), put

\[
 K=\mathbb Q(\sqrt{-s}),\qquad
 \alpha=p+2tk\sqrt{-s},\qquad N_{K/\mathbb Q}(\alpha)=N_{c,k}. \tag{50.10}
\]

For a prime \(q\nmid2ck\),

\[
 q\mid N_{c,k}
 \quad\Longleftrightarrow\quad
 \text{some }\mathfrak q\mid q\text{ in }K\text{ divides }(\alpha)
 \quad\Longleftrightarrow\quad
 p\equiv\pm2k\sqrt{-c}\pmod q.                            \tag{50.11}
\]

In particular \(q\) splits in \(K\), but the converse “\(q\) splits” is far
weaker: (50.11) selects one of the finitely many prime-ideal divisors of the
*specific principal ideal* \((\alpha)\).  The form
\(X^2+4cY^2\) has discriminant \(-16c\), but a prime dividing one represented
integer need not itself be represented by its principal form.  Ring-class
Chebotarev controls primes represented by form classes; it does not control
the factorization of a fixed represented integer.

The other half of (50.4), \(q\equiv-p\pmod h\), is a cyclotomic/ray
condition on the rational prime \(q\).  Combining it with (50.11) gives
exactly (50.8), a condition on **\(p\) modulo \(q\)** when \(q\) is fixed.
It is not a Frobenius condition on \(p\) in one fixed ring-class field as
\(q\) varies.  Effective Chebotarev under GRH can count either fixed class;
it cannot turn the infinite disjunction over actual divisors of
\((\alpha)\) into a pointwise factorization theorem.

There is a useful quantitative check on the tempting “many polylogarithmic
fields” heuristic.  Restrict \(ck\leq L\) and fixed candidate primes
\(q\leq Z\).  Before any deduplication, (50.8) gives at most two classes
modulo \(4ckq\), so the rectangular analogue of (29.7) is

\[
 \begin{split}
 \mu_{\rm raw}(L,Z)
 &\leq {1\over2}\sum_{ck\leq L}{1\over ck}
       \sum_{\substack{q\leq Z\\q\equiv3\ (4)\\q\ {\rm prime}}}{1\over q}\\
 &=\left({1\over8}+o(1)\right)(\log L)^2\log\log Z.
                                                               \tag{50.12}
 \end{split}
\]

The prime condition in the second sum is now explicit.
*(wave-17 review repair)*  This is a class-mass envelope, not a coverage
theorem.  There are
\(\sum_{n\leq L}\tau(n)=L\log L+O(L)\) slices, but Theorem 48.1 shows that
all \(k\)'s over one core share the same genus bit; counting them as
independent quadratic fields is already wrong.

**Assessment 50.7 (the GRH compositum wall in the slice frame).**  A literal
joint-Chebotarev implementation introduces cyclotomic conductors containing
\({\rm lcm}(1,\ldots,4L)\) and the candidate primes through \(Z\); its naive
compositum degree is exponential on the \(L+Z\) scale.  The same
GRH-effective bookkeeping as §17.5(c) therefore limits a direct compositum
to \(L+Z=O(\log N)\) when primes \(p\leq N\) are counted.  At
\(L,Z\asymp\log N\), even an *ideal independent-events model* applied to
(50.12) predicts only

\[
 \exp\{-O((\log\log N)^2\log\log\log N)\}                 \tag{50.13}
\]

for the survivor proportion.  Allowing an average sieve to take
\(Z=N^\theta\) changes the model exponent only to
\(O((\log\log N)^3)\).  Both leave \(N^{1-o(1)}\) possible survivors, not
\(N^{o(1)}\), and are much weaker in shape than the
CLAIMED/PROVISIONAL §39 bound
\(N\exp\{-c(\log N)^{3/4}\}\).  More importantly, GRH supplies no
independence theorem for these overlapping root classes, so (50.13) is an
audit ceiling, not a conditional exceptional-set theorem.  There is
therefore no GRH exceptional-set improvement to record here.

Elliott--Halberstam, its generalized forms, and Kloosterman-refined
levels of distribution alter the range in which the classes (50.8) can be
averaged over \(p\).  Their standard conclusions retain an exceptional set
and do not control the factorization of each \((\alpha)\).  Even the ideal
mass calculation with their larger \(Z\) has the second scale just described.
Thus they do not imply (50.7) in standard form.

### 50.4 Summing every active slice does not restore a Duke main term

For a product cutoff \(L\), the exact active-box mass is

\[
 T_L^-(p)=
 \sum_{\substack{ck\leq L,
 (c,k)\in\mathcal B_p\\
                   \chi_{\operatorname {sf}(c)}(p)=-1}}
 {1\over\varphi(4ck)}\sum_{\chi\ ({\rm mod}\ 4ck)}
 \overline{\chi(-p)}
 \prod_{\ell^e\parallel p^2+4ck^2}
       (1+\chi(\ell)+\cdots+\chi(\ell)^e).                 \tag{50.14}
\]

There is an exact genus pairing inside each summand.  Inflate \(\chi_s\) to
modulus \(h\).  Every factor \(\ell\mid N\) has \(\chi_s(\ell)=1\).  Hence
for an active slice, where \(\chi_s(-p)=1\),

\[
             \text{the terms indexed by }\chi
             \text{ and }\chi\chi_s\text{ are equal}.       \tag{50.15}
\]

For a genus-forced slice they are opposites and cancel, which is Theorem
48.1 in Fourier language.  Restricting to \(\chi_s(p)=-1\) therefore removes
that one cancellation but leaves every character of the residual quotient
of \(K_s(h)\).  It does not make the principal character dominant.
The principal/genus pair contributes

\[
 P_L^-(p)=
 \sum_{\substack{ck\leq L,
 (c,k)\in\mathcal B_p\\
                   \chi_{\operatorname {sf}(c)}(p)=-1}}
 {2\tau(p^2+4ck^2)\over\varphi(4ck)}
 \leq p^{o(1)}(\log L)^2\log\log(3L)                      \tag{50.16}
\]

when \(L=p^{o(1)}\).  The inequality uses the uniform divisor bound and
\(n/\varphi(n)\ll\log\log(3n)\).  It is positive when the active box is
nonempty, but the remaining ray characters can cancel it exactly.  At
\(p=2521\), for example, the active cores
\(11,17,19,22,23,29\) occur in \(ck\leq30\), yet every unforced slice in
that box vanishes (§§44.4 and 48.2).

**Assessment 50.8 (Duke/class-group GRH).**  Summing (50.14) does not create
a fixed theta series: the discriminant \(-16c\), ray modulus \(4ck\), norm
\(p^2+4ck^2\), and even the active-core selection all move.  The
Hurwitz--Kronecker identity of §36.4 restores class numbers only after
removing the ray projector and changing to a weighted all-divisor mass.
Equation (50.15) removes exactly the genus character and no other part of
that projector.  GRH for class-group or ray-class L-functions controls
prime/ideal sums, not the target coefficient of the finite Euler product of
one norm; §44.5's square-root-versus-subpower gap remains.  Therefore a
Duke-type theorem would need a new uniform equidistribution statement for
the whole moving family (50.14), with error \(o(P_L^-)\).  Such a statement
would be a genuine new hypothesis, not a consequence presently recognized
as “GRH for the relevant L-functions.”

### 50.5 Conditional frontier and census

The standard-hypothesis audit can be summarized without changing its labels:

\[
\begin{array}{c|c|c}
\text{input}&\text{standard output}&\text{missing condition}\\ \hline
\text{Bateman--Horn}&\text{prime polynomial values on average in the variable}
 &\text{a composite value with a good factor, uniformly per }p\\
\text{Linnik}&\text{a prime }q\equiv-p\pmod h&q\mid N_{c,k}\\
\text{GRH/Chebotarev}&\text{split/ray primes in fixed fields}
 &\mathfrak q\mid(\alpha)\text{ for each fixed }\alpha\\
\text{least nonresidue under GRH}&\chi_s(p)=-1
 &\text{the residual exponent-box hit}\\
\text{EH/GEH/Kloosterman}&\text{average distribution in }p
 &\text{an empty exceptional set}\\
\text{Duke/class-group GRH}&\text{unprojected or averaged form mass}
 &\text{the moving ray projector.}
\end{array}                                                  \tag{50.17}
\]

The proved obstructions are Lemma 50.3, Theorem 50.5, the complete
fixed-divisor escape Theorem 48.5, and the exact Fourier pairing
(50.15).  The claims that the named standard hypotheses stop at the middle
column are **Assessments about their standard conclusions**, not logical
independence theorems saying that GRH or Bateman--Horn cannot coexist with a
future proof of Erdős--Straus.  The present conditional frontier is exactly
(50.7): a pointwise theorem about a prime factor of a specified moving
integer.  Replacing “prime factor” by “divisor” reduces it to the open depth
criterion of Proposition 48.6.

For the finite comparison define

\[
 ck_{\rm pr}(p)=\min\{ck:(c,k)\in\mathcal B_p,
 \ \exists\hbox{ prime }q\mid p^2+4ck^2,
 \ q\equiv-p\pmod {4ck}\}.                                \tag{50.18}
\]

**Computational 50.9 (exact stated range, informational).**  `verify.py
(aw)` finds \(ck_{\rm pr}(p)\) for all 385 hard primes below \(30000\),
recomputes the complete exponent box at every tested norm, and reconstructs
(50.5)--(50.6) for every retained good-prime event.  Its distribution is

\[
\begin{array}{c|rrrrrrrrrrr}
ck_{\rm pr}&5&7&10&11&13&14&17&19&21&22&23\\
\#&156&30&36&35&13&15&16&4&15&9&6\\ \hline
ck_{\rm pr}&26&28&29&31&33&34&35&37&38&39&42\\
\#&10&4&3&1&2&3&1&1&4&2&5\\ \hline
ck_{\rm pr}&43&46&55&62&66&67&69&70&77&78&\\
\#&1&1&2&1&4&1&1&1&1&1&
\end{array}                                                  \tag{50.19}
\]

The strict records are

\[
\begin{array}{c|rrrrrrrr}
p&73&193&241&1201&2521&4729&7489&9601\\
ck_{\rm pr}&7&10&21&34&38&66&70&78.
\end{array}                                                  \tag{50.20}
\]

The prime-factor minimum equals the unrestricted slice minimum
\(ck_{\min}=D+1\) for 311 primes and is larger for 74.  The largest gap is
55, at \(p=23689\): \(ck_{\min}=11\) but \(ck_{\rm pr}=66\), witnessed by
\((c,k,q)=(33,2,77951)\).  Thus the one-prime condition is visibly
sufficient but not equivalent even in this small census.  The largest
\(ck_{\rm pr}\) is 78 at \(p=9601\), while §48's largest \(ck_{\min}\) is
77.  These finite observations support no growth law and are not evidence
for \(H_{\rm SPF}\).  With `ES_FULL_SCAN=1`, the memory-bounded scan extends
to the 1,181 hard primes below \(10^5\); its maximum is 282, at \(p=83689\),
and remains informational.

**Verification companion.**  `verify.py (aw)` factors one norm at a time and
keeps at most one residue set of size \(4ck\).  It checks admissibility,
primality and both congruences in (50.4), the complementary target grade,
the genus sign, the exact exponent-box implication, the Type-I equation and
unit-fraction identity, the complete histogram (50.19), records (50.20), and
the comparison with \(D(p)\).  The optional full scan uses the same streamed
algorithm.


## 51. The witness-modulus tail: truncated windows, the polylog corollary, and the effectivity audit

**Status.**  This section puts the exceptional-set bound and a pointwise
frontier on one statistic.  The fixed-polylogarithmic supply result below is
unconditional in the usual sense (it assumes no hypothesis) and does not use
Theorem 34.8.  Its assembly reuses Lemmas 39.1--39.5 and the Bonferroni
argument of Theorem 39.6, which the campaign labels proved internally but
provisional pending hostile external review.  It therefore retains that
review qualification.  The cubic result additionally inherits the explicitly
**CLAIMED/PROVISIONAL** Theorem 34.8.  Nothing here upgrades Theorems 34.8 or
39.7.

### 51.1 One statistic and a parameterized truncation

For a prime (or any positive integer) \(p\), define

\[
 W(p)=W_{\rm II}(p)=\min k\ell,                              \tag{51.1}
\]

where the minimum is over positive \(k,\ell,u,v,w\) such that

\[
 k\ell\equiv3\pmod4,\qquad {k\ell+1\over4}=uvw,
 \qquad p\equiv-u v^{-1}\pmod {k\ell}.                    \tag{51.2}
\]

Put \(W(p)=+\infty\) if this set is empty.  No finiteness assertion is made
in general.  Lemma 16.1 says exactly that \(W(p)\leq T\) supplies an explicit
Erdos--Straus representation through a multiplier modulus at most \(T\).
Notice that \(\ell\) is not required to be prime in this definition.  The
proof below uses only the subfamily in which it is prime.

The reusable form of the critical-window calculation is as follows.  Write
\(t=\log X\), let \(K\geq K_0\), and suppose that the canonical dyadic boxes
of (39.2)--(39.3) furnish, uniformly in every subfamily
\(\mathcal J\subseteq\{k\leq K:k\equiv1\pmod4\}\) containing 1 and every
reduced compatible fibre \(c\),

\[
 \sum_{X^{1/2}<\ell\leq X}{f_{c;\mathcal J}(\ell)\over\ell}
       \asymp t^2h(\mathcal J),
 \qquad h(\mathcal J)=\sum_{k\in\mathcal J}{\varphi(k)\over k^2}. \tag{51.3}
\]

Put

\[
 \mu=t^2\log K.                                             \tag{51.4}
\]

**Lemma 51.1 (truncated c-free assembly; proved internally, with the
provisional review status of Section 39).**  Assume (51.3), \(KX\leq T\),
\(\log K\ll t\), and

\[
             \log N\geq C\mu t.                            \tag{51.5}
\]

Then, with effective constants whenever the supply constants in (51.3) are
effective,

\[
 \#\{p\leq N:p\hbox{ prime},\ W(p)>T\}
       \ll N\exp\{-c\mu\}.                                 \tag{51.6}
\]

*Proof.*  Use the fixed c-free atoms (39.2)--(39.4), now with the displayed
\(X,K\).  Every atom has modulus \(k\ell\leq KX\leq T\), so a prime counted
on the left of (51.6) avoids every atom.  Lemma 39.1 is unchanged: its
same-prime determinant uses \(u,v\leq X^{1/6}\), and its cross-multiplier
step uses \(4uv>4H^2>K\).  Neither argument requires \(K=X^\kappa\).

The upper profile proof in Lemma 39.2 gives, without replacing \(\log K\) by
\(t\),

\[
 W_{k,a}(g)\ll {t^2\over\varphi(g)}{
                    \varphi(k)^2\over k^3}.                \tag{51.7}
\]

Equations (39.14)--(39.17) are exact CRT and Euler-factor calculations.
Consequently the induction in Theorem 39.4 gives the parameterized bound

\[
       {\mathbb E}(H_X)_m\leq(C\mu)^m                       \tag{51.8}
\]

for every \(m\geq1\).  There is no hidden lower bound on \(m\) or \(t\)
other than the fixed sufficiently-large threshold needed by the supply
estimate.  In particular this holds at every order used below.

Take \(y=B\mu\).  The proof of Lemma 39.5 also remains parameterized.  Its
Chernoff calculation gives

\[
 \Pr\{Z(c)>\eta\}\leq\exp\{-\eta B\mu+O(1)\},             \tag{51.9}
\]

and (39.26) gives
\(h(\mathcal J_c)\gg\log K\) on the complementary fibres.  Applying
(51.3) to this data-dependent \(\mathcal J_c\) gives

\[
 \Pr(H_X=0\mid S_y=1)\leq e^{-c\mu}.                       \tag{51.10}
\]

The canonical-box detail is important.  For the fixed-polylogarithmic case,
the lower proof of Lemma 16.3 partitions into dyadic \(\ell\)-blocks and
uses \(z=x^{1/6}\), exactly the boxes in (39.2).  Its low-\(\omega\) triples
are therefore contained in the c-free family.  For the cubic case this is
the explicit canonical-box sentence after (39.3) and the proof of Theorem
34.8.  Thus (51.10) does not enlarge a supply theorem beyond the boxes in
which it was proved.

Let \(r\) be the least even integer at least \(D_B\mu\), and use
\(S_yQ_r(H_X)\) as in (39.29).  Equations (51.8)--(51.10) and the same
factorial-tail argument give CRT mean \(O(e^{-c\mu})\).  The exact ledger is

\[
 \begin{split}
 \deg&=O(\mu),\\
 \log d_{\rm term}&=O(y)+O(r(t+\log K))=O(\mu t),\\
 \log\sum|c_{\rm term}|&=O(rt)=O(\mu t).                  \tag{51.11}
 \end{split}
\]

Here \(y<X^{1/2}\) for large \(X\), and the crude atom count still has
logarithm \(O(t)\).  Under (51.5), counting each resulting plain congruence
class on \([1,N]\) as its CRT mean times \(N\), plus \(O(1)\), absorbs the
whole rounding ledger.  The finitely many primes at most \(\max(K,y)\) are
also absorbed.  This proves (51.6). \(\square\)

**Theorem 51.2 (master witness-modulus tail; proved internally with the exact
status below).**  There are effectively computable positive constants such
that the following two statements hold.  Throughout this theorem and
Corollary 51.3, every set counted with the variable \(p\) is restricted to
primes.  *(wave-18 review repair: the displayed sets had omitted this scope,
while the proof uses the prime coprimality selector.)*

1. **Fixed-polylogarithmic supply, no Theorem 34.8.**  Uniformly when
   \[
    3\leq T,\qquad
    \log N\geq C\{1+(\log T)^3\log(2+\log T)\},             \tag{51.12}
   \]
   one has
   \[
    \#\{p\leq N:W(p)>T\}
      \ll N\exp\{-c(\log T)^2\log(2+\log T)\}.             \tag{51.13}
   \]
   This is unconditional and does not inherit Theorem 34.8.  It does inherit
   the campaign's provisional-review qualification on the Section 39 moment
   and Bonferroni machinery.
2. **Cubic supply.**  Fix \(0<\kappa<1/240\).  Uniformly when
   \[
     3\leq T,\qquad \log N\geq C_\kappa\{1+(\log T)^4\},    \tag{51.14}
   \]
   one has
   \[
    \#\{p\leq N:W(p)>T\}
       \ll_\kappa N\exp\{-c_\kappa(\log T)^3\}.            \tag{51.15}
   \]
   This statement inherits Theorem 34.8 and is
   **CLAIMED/PROVISIONAL**.

In particular both estimates are uniform throughout the simpler common
range

\[
             3\leq T\leq\exp\{c(\log N)^{1/4}\}.           \tag{51.16}
\]

*Proof.*  For (1), set \(X=T^{1/2}\) and
\(K=\lfloor(\log X)^5\rfloor\), with harmless fixed adjustments below the
asymptotic threshold.  Then \(KX\leq T\) for large \(T\),
\(\log K\asymp\log t\), and Lemma 16.3 supplies (51.3).  Its lower proof is
in the canonical boxes, as checked in Lemma 51.1.  Thus
\(\mu\asymp t^2\log t\), and (51.5) is precisely the scale in (51.12).
For bounded \(T\), enlarge the implied constant.

For (2), use the same \(X=T^{1/2}\) and put
\(K=\lfloor X^\kappa\rfloor\).  Then \(KX\leq T\), after another harmless
bounded adjustment, and Theorem 34.8 supplies (51.3) in the required boxes.
Now \(\mu\asymp t^3\), while (51.5) is (51.14).  Lemma 51.1 proves both
claims. \(\square\)

At \(T=\exp\{\alpha(\log N)^{1/4}\}\), (51.15) is
\(N\exp\{-c(\log N)^{3/4}\}\).  This is exactly the prime part of Theorem
39.7, up to constants; it is a consistency check, not a new record.

### 51.2 The polylogarithmic frontier

**Corollary 51.3 (polylogarithmic tails; same status as Theorem 51.2).**  For
each fixed \(A>0\),

\[
 \#\{p\leq N:W(p)>(\log N)^A\}
 \ll_A N\exp\{-c_A(\log\log N)^2\log\log\log N\},         \tag{51.17}
\]

unconditionally and without Theorem 34.8.  The cubic supply gives the
additional **CLAIMED/PROVISIONAL** estimate

\[
 \#\{p\leq N:W(p)>(\log N)^A\}
 \ll_A N\exp\{-c A^3(\log\log N)^3\}.                     \tag{51.18}
\]

The formulas are interpreted after a fixed large threshold.  The constants
in (51.17) may absorb the fixed powers of \(A\).  The same bounds hold with
the varying cutoff \((\log p)^A\): split at \(N^{1/2}\), apply the displayed
bound on the upper half with comparable logarithms, and absorb the lower
half.

Define the pointwise hypothesis

\[
 H_{\rm MOD}(A):\quad W(p)\leq(\log p)^A
       \quad\hbox{for every sufficiently large prime }p.   \tag{51.19}
\]

By Lemma 16.1, \(H_{\rm MOD}(A)\) for any \(A\) implies the Erdos--Straus
conjecture for every sufficiently large prime.  Corollary 51.3 says that its
failure set is at most triple-logarithmically sparse in the cubic version.
This does not prove that the failure set is empty.

The relation with Section 50 is exact but not an implication.  The bespoke
\(H_{\rm SPF}(A)\) is a Type-I slice-frame assertion: a prime factor of
\(p^2+4ck^2\) must occur in one specified grade with \(ck\) polylogarithmic.
The new \(H_{\rm MOD}(A)\) is the Type-II multiplier assertion (51.1).
Neither hypothesis implies the other as stated; both imply a pointwise
Erdos--Straus representation.  The unification is instead that Theorem 39.7
is the tail of the same \(W\) whose pointwise polylogarithmic boundedness
would settle all sufficiently large primes.  In that precise sense the
record and the multiplier frontier are one object, and (51.18) confines the
unresolved pointwise conspiracy to an
\(\exp\{-c(\log\log N)^3\}\) proportion, provisionally.  For the conjecture
itself, any finite bound on \(W(p)\), even an exponential one varying with
\(p\), is enough; the polylogarithmic form is what this truncated sieve
naturally measures.

### 51.3 Effectivity and the exceptional character

There is a correction to the tempting description of the first variant as
an "elementary supply" argument.  Lemma 16.2 is a box calculation plus
Shiu's Brun--Titchmarsh theorem for multiplicative functions, but the lower
bound in Lemma 16.3 explicitly invokes Bombieri--Vinogradov in (16.9)--(16.10).
It invokes neither Siegel--Walfisz separately nor prime equidistribution on
the \(N\)-side.  Brun--Titchmarsh is used for its upper bound.  Thus the
fixed-polylogarithmic variant is independent of Theorem 34.8, not independent
of Bombieri--Vinogradov.

Polynomially large moduli do not by themselves remove the possible Siegel
zero from Bombieri--Vinogradov.  A character modulo a large composite \(q\)
may be induced by a primitive character of small conductor \(r\mid q\).
The standard reduction to primitive characters therefore reintroduces small
conductors even when \(q\geq X^{20\kappa}\).  The following is the effective
form actually needed.

**Lemma 51.4 (effective Bombieri--Vinogradov away from one conductor;
standard cited input, with dependency proof sketch).**  For every \(A>0\), there are effectively
computable \(B,C,x_0\) such that, for \(x\geq x_0\) and
\(Q\leq x^{1/2}/(\log x)^B\), there is either no exceptional conductor or
one real primitive conductor \(r_x\geq3\) for which

\[
 \sum_{\substack{q\leq Q\\r_x\nmid q}}
  \max_{(a,q)=1}\left|\psi(x;q,a)-{x\over\varphi(q)}\right|
       \leq {Cx\over(\log x)^A}.                            \tag{51.20}
\]

The same statement holds for dyadic \(\pi\)-differences by effective partial
summation.

*Proof sketch with dependency ledger.*  Apply Vaughan's identity, reduce
characters modulo \(q\) to their primitive conductors, and split those
conductors at \((\log x)^{B_0}\).  The large-conductor Type I/II sums use
only the large-sieve inequality and algebraic Vaughan identity, with explicit
constants.  Landau--Page gives, effectively, at most one primitive real
character in the small-conductor range with a zero in the exceptional strip.
All other small conductors have an effective zero-free region and the
explicit formula gives more than the required logarithmic saving.  The
principal character uses the classical effective prime number theorem.
Deleting moduli divisible by the one exceptional conductor removes exactly
the imprimitive characters induced by it.  Summing the effective pieces is
the standard Bombieri--Vinogradov proof (for example the Vaughan-identity and
large-sieve treatment in Chapters 24 and 28 of Davenport's *Multiplicative
Number Theory*).

*(wave-18 review repair.)*  Here is the induced-character count suppressed in
that standard reduction.  Choose the small-conductor cutoff
\(R=(\log x)^{B_0}\).  Away from the Page character, the explicit formula is
effective and uniform for \(x\leq y\leq2x\), and gives, for primitive
\(\chi^*\) of conductor \(r\leq R\),
\[
             |\psi(y,\chi^*)|\ll y\exp\{-c\sqrt{\log x}\}.
\]
Moreover
\[
 \sum_{\substack{q\leq Q\\r\mid q}}{1\over\varphi(q)}
 \leq {1\over\varphi(r)}
       \sum_{m\leq Q/r}{1\over\varphi(m)}
 \ll {\log(2Q)\over\varphi(r)}.
\]
Since there are at most \(\varphi(r)\) primitive characters of conductor
\(r\), summing over all \(r\leq R\) costs only
\(O(R\log(2Q))\), which is absorbed by the exponential saving; the elementary
errors from induction are smaller.  The finitely many fixed conductors,
including 4, are checked effectively before Page is applied, so the selected
unresolved conductor may be taken different from 4.  For the dyadic
\(\pi\)-form, select the Page conductor once using the upper endpoint
\(2x\) and use the preceding estimate uniformly on \([x,2x]\) before
partial summation.  Thus two endpoint applications never introduce two
different deleted conductors.  This also explains why merely restricting
\(q\) to a polynomially large interval does not prove (51.20) without its
divisibility exclusion. \(\square\)

For completeness, the supply survives that exclusion.

**Lemma 51.5 (exceptional-conductor deletion tolerance; proved).**  In the
boxes of Lemma 16.2, let \(r>1\) be a primitive real character conductor.
Apart from the explicitly harmless conductor 4, there is a prime \(p\mid r\)
(or \(p=2\) when the required extra factor is the third power of 2) such that

\[
                p\nmid uv\quad\Longrightarrow\quad r\nmid4uv. \tag{51.21}
\]

Uniformly in \(c,k\), the pairs satisfying (51.21) retain a fixed positive
proportion of the harmonic box mass.  The low-\(\omega\) cutoff may be chosen
so that it and (51.21) retain a fixed positive proportion simultaneously.
The same remains true after the low-congestion pruning of Theorem 34.8.

*Proof.*  A primitive real conductor is the absolute value of a fundamental
discriminant.  If it has an odd prime factor, choose that factor.  For a pure
2-power conductor other than 4, it is 8 and one takes \(p=2\), requiring
\(uv\) odd.  Conductor 4 is fixed and its Dirichlet beta function can be
handled effectively directly; it cannot be the unresolved Landau--Page
conductor once the fixed finite conductors have been checked.  This proves
(51.21).

Fix \(k\).  If \(p\mid k\), the existing condition \((uv,k)=1\) already
imposes \(p\nmid uv\).  Suppose \(p\nmid k\).  When \(p\leq Ck\), repeat the
box count (16.4) with the additional reduced conditions modulo \(p\).  The
local proportion, after the condition \((u,v)=1\), is

\[
 { (1-1/p)^2\over1-1/p^2}={p-1\over p+1}\geq {1\over3}.    \tag{51.22}
\]

The combined modulus is at most \(Ck^2\), and the floor \(H=K^{10}\)
absorbs the resulting boundary errors uniformly.

When \(p>Ck\), count the discarded pairs with \(p\mid u\) or \(p\mid v\)
directly in each box.  Writing, for example, \(u=pa\), the congruence fixes
one class of \(a\pmod k\).  After division by the box weights its main term
is \(O(1/(pk))\), against
\(\asymp\varphi(k)/k^2\) for (16.4).  Its ratio is at most
\(O(k/(p\varphi(k)))\leq O(1/C)\); the endpoint errors sum to
\(O((\log z)^2/H)\) and are absorbed as before.  Choose \(C\) large.  The
two cases give a uniform positive retained proportion for every \(k\), hence
for every subfamily \(\mathcal J\).

In (16.5h), increasing the fixed integer \(D\) makes the low-\(\omega\)
tail any prescribed fixed fraction of the uncut mass, rather than merely the
one-half printed there.  Inclusion with (51.22) therefore retains positive
mass.  Lemma 34.7 says that high-incidence triples have \(o(1)\) of the
original mass, so deleting them as well still leaves the same order. \(\square\)

**Theorem 51.6 (effectivity of the repaired chains; proved internally,
record-adjacent and therefore CLAIMED/PROVISIONAL).**  The constants in the
class-mass conclusions (16.8), (34.18)--(34.19), Theorems 16.4 and 39.7, and
Theorem 51.2 may all be taken effectively computable.  The record statement
retains every correctness and priority qualification already attached to
Theorem 39.7.

*Proof.*  In each dyadic prime block apply Lemma 51.4, and if its exceptional
\(r_x\) exists, use only the triples with \(r_x\nmid4uv\).  Lemma 51.5 says
that these triples retain the full order of the box mass, uniformly in every
subfamily and fibre.  The retained triples are a subset of the original
class family, so they prove the original lower class-mass conclusion.  This
repairs the only potentially ineffective prime-progression input.  All later
constants are obtained by finite choices in the effective inequalities.
\(\square\)

There is one deliberately narrow caveat.  The first sentence of Theorem
34.8 also asserts an \(o(1)\) bound for the sum of absolute progression errors
over **all** low-congestion triples.  Exceptional-conductor deletion proves
its class-mass consequence (34.18) effectively, but does not make that
ancillary all-triples error sum effective as printed.  Theorem 39.7 uses the
class-mass consequence, not the ancillary assertion.  Thus Theorem 51.6 is
an effectivity theorem for the full exceptional-set chain, not an upgrade of
every clause in Theorem 34.8.

Here is the promised ingredient-by-ingredient audit.

\[
\begin{array}{c|l}
\text{ingredient}&\text{effectivity}\ \hline
16.2&\text{effective box/Mobius count; effective Shiu and Mertens bounds}\\
16.3&\text{lower bound uses BV, not elementary; effective by 51.4--51.5}\\
16.4&\text{Gallagher/PW larger sieve and Rankin truncation are elementary and effective}\\
34.7&\text{effective incidence expansion and box errors}\\
34.8&\text{Shiu and pruning effective; supply effective after 51.5; caveat above}\\
39.1&\text{finite determinant and exact CRT}\\
39.2&\text{upper profile uses effective Shiu and Brun--Titchmarsh; lower supply repairable}\\
39.3--39.4&\text{Euler factors and exact CRT moment induction}\\
39.5&\text{effective Chernoff plus the repaired uniform class supply}\\
39.6&\text{finite Bonferroni algebra and exact integer class counting}\\
39.7&\text{effective parameter choice, conditional only on the correctness of its provisional chain}\\
16.5&\text{effective partial summation and Rankin semigroup transfer.}
\end{array}                                                  \tag{51.23}
\]

Accordingly, the old belief that the current Section 16 route is necessarily
Siegel--Walfisz-ineffective is too coarse.  Earlier Sections 12--14 invoke
Siegel--Walfisz directly and are ineffective as printed.  The Section 16
supply invokes ordinary Bombieri--Vinogradov, whose textbook proof can carry
the same issue through induced small-conductor characters, but Lemmas
51.4--51.5 remove it.  Its \(N\)-side larger sieve is Gallagher's elementary
larger sieve; PW Section 4 confirms that no prime equidistribution is used
there after the class supply has been established.

### 51.4 PW truncation and frontier placement

Pomerance--Weingartner (PW) Section 4 defines \(f(\ell)\) k=1-type forced
classes, proves

\[
             \sum_{\ell\leq X}{f(\ell)\over\ell}
                    \asymp(\log X)^2                       \tag{51.24}
\]

for fixed numerator, and then applies the larger sieve.  Its lower proof of
(51.24), like Lemma 16.3, explicitly uses Bombieri--Vinogradov after bounding
the multiplicity of a product by a fixed log power; its upper proof uses
Brun--Titchmarsh.  Truncating their displayed argument at \(X=T\) gives

\[
 \#\{p\leq N:W_{\rm PW}(p)>T\}
       \ll N\exp\{-c(\log T)^2\},
 \qquad \log N\geq C(\log T)^3,                            \tag{51.25}
\]

where \(W_{\rm PW}\) measures their k=1 prime-modulus subfamily.  Since
those are Lemma-16.1 witnesses, (51.25) is also a valid weaker tail bound for
\(W\).  The effectivity repair above applies to their BV supply in the same
way.  Thus PW already contains the square-log truncated tail.  Section 51
adds the multiplier factor \(\log\log T\) using the fixed-polylogarithmic
family and the full extra \(\log T\) using the provisional cubic family; it
also makes the induced-character effectivity issue explicit.

\[
\begin{array}{c|c|c}
\text{supply}&\text{tail exponent}&\text{status}\ \hline
\text{PW k=1}&(\log T)^2&\text{proved in PW, truncation of their argument}\\
\text{Lemma 16.3 multipliers}&(\log T)^2\log\log T&
 \text{unconditional; Section 39 review qualification}\\
\text{Theorem 34.8 multipliers}&(\log T)^3&
 \text{CLAIMED/PROVISIONAL.}
\end{array}                                                  \tag{51.26}
\]

Vaughan's 1970 paper remains inaccessible in this campaign; the comparison
is with PW's modern reconstruction, not a direct audit of Vaughan.

In the frontier map, (39.35) is the tail at the largest admissible \(T\),
while \(H_{\rm MOD}\) and \(H_{\rm SPF}\) ask for pointwise polylogarithmic
witnesses in the Type-II and Type-I frames respectively.  Section 51 supplies
the interpolation and an almost-all pointwise statement.  It does not remove
a single pointwise obstruction, prove either hypothesis, or cross any wall
in Section 17.

### 51.5 Finite companion

**Computational 51.7 (exact stated range, informational).**  `verify.py (ax)`
directly harvests every Lemma-16.1 class for every
\(M\leq3000\), \(M\equiv3\pmod4\), and computes \(W(p)\) in that truncated
family for all 3,202 primes \(p<300000\), \(p\equiv1\pmod {24}\).  The
numbers with \(W(p)>T\) at \(T=25,100,400,1600\) are respectively

\[
                         226,\quad19,\quad0,\quad0.          \tag{51.27}
\]

The maximum is 279.  Continuity-corrected fits to both exponents in Theorem
51.2 have positive fitted decay constants; this is only a finite sanity
check and supports no asymptotic claim.  The block also checks exact
inclusion--exclusion against direct counting over a period 39,215 for a
six-atom toy, verifies the compatible-atom distinct-prime rule there, and
checks three toy instances of the conductor deletion for
\(r=3,5,7\).  The toy floor is relaxed because \(H=K^{10}\) makes literal
small instances empty.  No computational line is used as proof of an
asymptotic statement.
## 52. Per-slice vanishing frequency: the sieve upper bound and the empty third layer

**Scope and outcome.**  The genus obstruction of Theorem 48.1 is the last
fixed-congruence obstruction for one fixed slice.  On every reduced hard
class on which the genus permits positivity, a classical upper-bound sieve
shows that residual slice vanishing has relative density zero among the
primes, with an explicit log-power saving.  Consequently no refinement of
such a class can be an identically vanishing prime progression.  This is a
per-slice almost-all theorem, not a pointwise bound on conspiracy depth and
not a multi-slice stacking theorem.  In this section, as in §44.4, "hard"
means exactly prime and congruent to 1 modulo 24.

### 52.1 A fractional-dimensional upper-bound sieve

Fix positive integers \(c,k\), put

\[
 c=st^2,\qquad s=\operatorname {sf}(c),\qquad
 h=4ck,\qquad Q=\operatorname {lcm}(24,h).                 \tag{52.1}
\]

**Theorem 52.1 (per-slice sieve upper bound; proved).**  Suppose
\(s\notin\{1,2,3,6\}\).  Fix a reduced class \(a\pmod Q\) such that

\[
 a\equiv1\pmod {24},\qquad (a,h)=1,\qquad \chi_s(a)=-1.    \tag{52.2}
\]

Then

\[
 \#\{p\leq X:p\ {\rm prime},\ p\equiv a\pmod Q,
                    \ M_{c,k}(p)=0\}
 \ll_{c,k}{X\over(\log X)^{1+2/\varphi(h)}}.              \tag{52.3}
\]

The finitely many \(p\) for which \((c,k)\notin\mathcal B_p\) are included
in the implied constant.  The constant can be taken uniformly over the
finitely many classes \(a\pmod Q\) satisfying (52.2), which explains the
subscript \(c,k\).

*Proof.*  The contrapositive of Theorem 50.1 gives, for every admissible
\(p\) in (52.2),

\[
 M_{c,k}(p)=0\quad\Longrightarrow\quad
 p^2+4ck^2\hbox{ has no prime divisor }q\equiv-a\pmod h.   \tag{52.4}
\]

Call the primes in the class on the right **good primes**.  Exclude the
finitely many primes dividing \(Q\).  A good prime \(q\) is then odd and
prime to \(2ck\).  Since the conductor of \(\chi_s\) divides \(4s\mid h\),

\[
 \chi_s(q)=\chi_s(-a)=\chi_s(-1)\chi_s(a)=1.              \tag{52.5}
\]

For odd \(q\nmid2ck\), the definition of the fundamental discriminant gives

\[
 \left({-4ck^2\over q}\right)
 =\left({-c\over q}\right)
 =\left({-s\over q}\right)
 =\left({\Delta_s\over q}\right)=\chi_s(q)=1.             \tag{52.6}
\]

Here the factors \(4,k^2,t^2\) are nonzero squares modulo \(q\); this also
handles all 2-adic choices in \(\Delta_s\), since multiplying the radicand by
4 does not change its Legendre symbol at odd \(q\).  Thus

\[
 n^2\equiv-4ck^2\pmod q                                   \tag{52.7}
\]

has exactly two distinct, nonzero roots.  Therefore (52.4) says that a
vanishing prime avoids those two classes modulo every good \(q\).

We apply the standard upper-bound fundamental lemma of the beta sieve (or,
equivalently here, the fixed-dimensional Selberg upper-bound sieve) to

\[
 \mathcal A=\{n\leq X:n\equiv a\pmod Q\}.                 \tag{52.8}
\]

For every prime \(\ell\leq z\), \(\ell\nmid Q\), remove the class 0 modulo
\(\ell\).  At a good prime also remove the two roots in (52.7).  The three
classes there are distinct.  If \(d\) is squarefree and prime to \(Q\), and
\(\rho(d)\) is the number of removed classes modulo \(d\), the Chinese
remainder theorem gives

\[
 \#\mathcal A_d={X\rho(d)\over Qd}+O(\rho(d)),\qquad
 \rho\hbox{ multiplicative},\qquad \rho(\ell)\leq3.       \tag{52.9}
\]

In particular

\[
 \sum_{d\leq D}\mu^2(d)\rho(d)\ll D(\log D)^2.           \tag{52.10}
\]

The sieve dimension is

\[
 \kappa=1+{2\over\varphi(h)}<2.                            \tag{52.11}
\]

For completeness, the invoked upper-bound fundamental lemma says that for a
fixed dimension \(\kappa\), if the local product has the standard dimension
bound, then, for fixed sufficiently large
\(u=u(\kappa)\), \(z=D^{1/u}\),

\[
 S(\mathcal A,z)\ll_\kappa {X\over Q}V(z)
       +\sum_{d\leq D}\mu^2(d)|r_d|,
 \quad V(z)=\prod_{\ell\leq z}\left(1-{\rho(\ell)\over\ell}\right),
                                                               \tag{52.12}
\]

with \(r_d\) the remainder in (52.9).  This is the usual upper-bound half of
the beta-sieve fundamental lemma; no parity-breaking lower sieve is being
used.  Take \(D=X^{1/2}\) and this fixed \(u\).  This deliberately avoids
claiming that the endpoint sieve parameter \(\log D/\log z=2\) is adequate
for every fractional dimension; any fixed positive power \(z=X^\eta\)
provided by (52.12) gives the same log exponent.

The local product is explicit:

\[
 V(z)=\prod_{\substack{\ell\leq z\\\ell\nmid Q}}
       \left(1-{1\over\ell}\right)
 \prod_{\substack{q\leq z\\q\equiv-a\ (h)\\q\nmid Q}}
       {1-3/q\over1-1/q}.                                  \tag{52.13}
\]

Ordinary Mertens and Mertens in the fixed arithmetic progression
\(-a\pmod h\) give

\[
 \sum_{\substack{q\leq z\\q\equiv-a\ (h)}}{1\over q}
 ={1\over\varphi(h)}\log\log z+C(h,-a)+o(1),              \tag{52.14}
\]

and hence, because
\((1-3/q)/(1-1/q)=1-2/(q-1)\),

\[
 V(z)\asymp_{c,k,a}
 {1\over(\log z)^{1+2/\varphi(h)}}.                        \tag{52.15}
\]

Equations (52.10), (52.12), and \(z=X^\eta\) make the remainder and the
\(O(z)\) primes \(p\leq z\) negligible relative to the right side of
(52.3).  Every prime \(p>z\) avoids the zero classes automatically, and a
vanishing one avoids the two root classes by (52.4), so it is counted by the
sifted set.  This proves (52.3). \(\square\)

The classical analytic inputs are exactly the upper-bound fundamental lemma,
ordinary Mertens, and Mertens in one fixed reduced progression.  The latter
follows from the prime number theorem in arithmetic progressions for the
fixed modulus \(h\).  No Bombieri--Vinogradov theorem, Siegel--Walfisz
theorem, or prime level of distribution is used: primality was majorized by
sieving the zero class among the integers in (52.8).  For explicitly fixed
\((c,k,a)\), these inputs and the constants are effective in principle,
although no numerical threshold is extracted here.

### 52.2 No third congruence law, and the uniform scope

**Corollary 52.2 (the congruence-level third layer is empty; proved).**
Under Theorem 52.1's hypotheses, let \(M'\) be any fixed multiple of \(Q\),
and let \(a'\pmod {M'}\) be a **reduced** refinement of \(a\pmod Q\).  The
set

\[
 \{p:p\equiv a'\pmod {M'},\ M_{c,k}(p)=0\}                \tag{52.16}
\]

does not contain all sufficiently large primes in that progression.
Consequently no prime-bearing arithmetic progression inside an unforced
slice-class is an identically vanishing progression.

*Proof.*  The prime number theorem in the fixed reduced progression gives

\[
 \#\{p\leq X:p\equiv a'\pmod {M'}\}
 \sim {X\over\varphi(M')\log X}.                           \tag{52.17}
\]

The vanishing primes in that refinement are a subset of those in the full
class \(a\pmod Q\), so (52.3) is an upper bound for them.  Since
\((\log X)^{-2/\varphi(h)}\to0\), (52.17) eventually exceeds that bound.
Nonreduced refinements contain no infinite prime progression and are
excluded from the statement for that reason. \(\square\)

Thus Theorems 44.2 and 48.1 give the complete congruence-level vanishing
classification for every fixed slice: the cores \(1,2,3,6\) vanish on the
whole hard progression, and every other core vanishes on the genus half
\(\chi_s(p)=1\), but no arithmetic subprogression in the complementary half
can vanish identically.  The asymmetry is real: Theorem 48.4 supplies many
identically **positive** progressions by fixing a target divisor.

The fixed-slice constant in (52.3) is not suitable for simply summing over a
growing slice box.  The following is the range that the same proof supports
without pretending those constants are uniform.

**Proposition 52.3 (polylogarithmic uniformity, with an epsilon loss;
proved, ineffective).**  Fix \(\theta>0\) and \(0<\epsilon<1\).  Uniformly
for slices and reduced classes satisfying (52.1)--(52.2) and

\[
                         h\leq(\log X)^\theta,              \tag{52.18}
\]

one has, with \(Q=\operatorname {lcm}(24,h)\),

\[
 \#\{p\leq X:p\equiv a\pmod Q,\ M_{c,k}(p)=0\}
 \ll_{\theta,\epsilon}
 {X\over\varphi(Q)(\log X)^{1+2(1-\epsilon)/\varphi(h)}}.  \tag{52.19}
\]

The implied constant and threshold are ineffective.  The result holds for
every fixed polylogarithmic exponent \(\theta\), but it does not assert
uniformity for arbitrary \(h=X^{o(1)}\), and it loses the displayed
\(\epsilon\) fraction of the sparse-prime dimension.

*Proof.*  In (52.13), retain the two extra root classes only for good primes
in

\[
 y=\exp\{(\log X)^\epsilon\}<q\leq z=X^\eta,               \tag{52.20}
\]

where \(\eta>0\) is the fixed small beta-sieve exponent for the coarse
uniform dimension bound 3.  Siegel--Walfisz, with the fixed parameter
\(A=\theta/\epsilon\), applies throughout this interval because
\(h\leq(\log q)^A\).  Partial summation gives uniformly

\[
 \sum_{\substack{y<q\leq z\\q\equiv-a\ (h)}}{1\over q}
 ={1\over\varphi(h)}\{(1-\epsilon)\log\log X+O(1)\}+o(1).
                                                               \tag{52.21}
\]

Ordinary Mertens with the primes dividing \(Q\) omitted contributes
\(\ll Q/(\varphi(Q)\log z)\).  Since \(\#\mathcal A\asymp X/Q\), (52.21)
inserted into the uniform version of (52.12) gives the main term (52.19).
The elementary remainder is \(O(X^{1/2}(\log X)^2)\), and the omitted
\(p\leq z\) cost is \(O(z)\); both are uniform and are absorbed under
(52.18). \(\square\)

The new classical input in Proposition 52.3 is Siegel--Walfisz for moduli up
to a fixed power of a logarithm.  Its usual uniform constant is ineffective
because of the possible exceptional real zero.  Page--Landau theory would
make an analogous statement effective after deleting at most one exceptional
real-character modulus at each scale; no such deletion is harmless for the
all-slice statement, so (52.19) is honestly labelled ineffective.  This is
the precise uniformity available for a future stacking argument; no stacking
is performed here.

### 52.3 Computational residual structure and correlations

**Computational 52.4 (exact ranges; informational).**  `verify.py (ay)`
recomputes every prime \(p\equiv1\pmod {24}\) below 30,000, and optionally
below \(10^5\) with `ES_FULL_SCAN=1`.  Norms are processed one at a time;
each individual slice evaluation reuses one factorization, although the
independent panel, census, minimum, and correlation tests may refactor the
same norm.  No factor cache or dense prime-by-slice array is retained.
*(wave-18 review repair)*  The complete exponent box (44.4) is formed, and
no asymptotic assertion is inferred.  There are 385 and 1,181 primes in the
two ranges.

First, on the least compatible active class \(a=73\) for four slices, the
exact class counts are

\[
\begin{array}{c|c|c|c|c}
(c,k)&h&Q&\#p,\#\{M=0\}\ (30000)&\#p,\#\{M=0\}\ (10^5)\\ \hline
(5,1)&20&120&105,35&297,86\\
(7,1)&28&168&66,41&204,122\\
(10,1)&40&120&105,58&297,163\\
(13,1)&52&312&31,24&98,81
\end{array}                                                  \tag{52.22}
\]

For every good prime \(q\leq10^4\) in these four ray classes, the block
checks the two distinct roots in (52.7).  It reconstructs 50 sampled
Theorem-50.1 tuples and verifies the unit-fraction identity with exact
rational arithmetic.  The good-prime counts through 30,000 are respectively
413, 268, 208, and 141; their ratios to
\(\pi(30000)/\varphi(h)\) are all between 0.5 and 2.  Most importantly, at
every panel prime it checks the exact implication

\[
 M_{c,k}(p)=0\quad\Longrightarrow\quad
 \nexists q\mid p^2+4ck^2,
             \quad q\equiv-p\pmod {4ck}.                  \tag{52.23}
\]

For all 31 unforced slices with \(ck\leq30\), the next table gives residual
vanishing divided by the number of primes with \(\chi_s(p)=-1\).  The last
column divides the 30,000 frequency by the shape
\((\log30000)^{-2/\varphi(4ck)}\).  This removes the primality log already
present in the conditioning.  The quotient is only a finite-range scale
comparison; the theorem does not predict its constant.

\[
\begin{array}{c|c|c|c@{\qquad}c|c|c|c}
(c,k)&<30000&<10^5&\text{ratio}&(c,k)&<30000&<10^5&\text{ratio}\\ \hline
(5,1)&35/200=.175&86/603=.143&.314&(7,1)&148/203=.729&426/612=.696&1.076\\
(10,1)&128/200=.640&381/603=.632&.857&(11,1)&92/204=.451&270/611=.442&.569\\
(13,1)&146/197=.741&445/608=.732&.900&(14,1)&117/203=.576&335/612=.547&.700\\
(15,1)&163/200=.815&480/603=.796&1.091&(17,1)&117/199=.588&341/598=.570&.680\\
(19,1)&155/204=.760&458/608=.753&.865&(20,1)&149/200=.745&424/603=.703&.862\\
(21,1)&159/203=.783&459/612=.750&.951&(22,1)&184/204=.902&545/611=.892&1.014\\
(23,1)&173/212=.816&467/607=.769&.907&(26,1)&130/197=.660&411/608=.676&.727\\
(28,1)&189/203=.931&570/612=.931&1.026&(29,1)&136/196=.694&401/595=.674&.754\\
(30,1)&168/200=.840&500/603=.829&.972&(5,2)&108/200=.540&316/603=.524&.723\\
(7,2)&176/203=.867&529/612=.864&1.053&(10,2)&155/200=.775&470/603=.779&.897\\
(11,2)&145/204=.711&426/611=.697&.799&(13,2)&165/197=.838&502/608=.826&.923\\
(14,2)&155/203=.764&437/612=.714&.841&(15,2)&178/200=.890&523/603=.867&1.030\\
(5,3)&163/200=.815&476/603=.789&1.091&(7,3)&166/203=.818&492/612=.804&.993\\
(10,3)&163/200=.815&491/603=.814&.943&(5,4)&136/200=.680&413/603=.685&.787\\
(7,4)&186/203=.916&558/612=.912&1.010&(5,5)&140/200=.700&409/603=.678&.787\\
(5,6)&174/200=.870&516/603=.856&1.007&&&&
\end{array}                                                  \tag{52.24}
\]

The finite data are broadly on the displayed scale (30,000 quotients range
from .314 to 1.091), and frequencies usually decline by \(10^5\).  This is
**consistent with**, but does not prove, a log-power decay or an asymptotic
constant.

The 74 strict gaps \(ck_{\rm pr}>ck_{\min}\) below 30,000 contain 98
canonical target divisors \(D<\sqrt N\) at the minimal positive product.
Every prime factor of each \(D\) has the wrong grade individually, as it
must by the definition of the gap.  Their exact shapes are

\[
\begin{array}{c|rr|c|rr}
\text{event's available shapes}&30000&10^5&
\text{individual }D\text{ shape}&30000&10^5\\ \hline
\{\text{two distinct primes}\}&49&136&\text{two distinct primes}&68&199\\
\{\text{three-or-more factors}\}&13&44&\text{three-or-more factors}&24&93\\
\{\text{prime power}\}&2&6&\text{prime power}&6&16\\
\{\text{multi},\text{semiprime}\}&6&25&&&\\
\{\text{power},\text{semiprime}\}&2&3&&&\\
\{\text{multi},\text{power}\}&1&6&&&\\
\{\text{all three}\}&1&1&&&
\end{array}                                                  \tag{52.25}
\]

There are 221 gap events and 308 canonical divisors in the full range.  Thus
the tempting description "a product of two wrong-grade primes hits the
target" is the majority mechanism, but not the only one.  For example, at
\(p=241,(c,k)=(11,1)\), \(D=155=5\cdot31\) has target grade 23 modulo 44
while neither factor does.  At \(p=409\), the same slice uses
\(D=75=3\cdot5^2\), and at \(p=5953,(c,k)=(5,1)\), the target divisor is
the prime power \(D=27=3^3\).  Exponent caps and products of three or more
prime factors are genuine additional mechanisms.

Finally, for two slices \(A,B\), condition on both genus signs being -1 and
write

\[
 R(A,B)={\Pr(M_A=0,M_B=0)\over
                 \Pr(M_A=0)\Pr(M_B=0)}.                   \tag{52.26}
\]

The exact empirical ratios (30,000, then \(10^5\)) are

\[
\begin{array}{c|c|c@{\qquad}c|c|c}
A&B&R&A&B&R\\ \hline
(5,1)&(5,2)&.529,.577&(5,1)&(5,3)&1.017,.972\\
(7,1)&(7,2)&.974,.994&(10,1)&(10,2)&.938,.946\\
(5,1)&(7,1)&1.018,1.092&(5,1)&(10,1)&.714,.699\\
(7,1)&(11,1)&1.009,.993&(11,1)&(17,1)&1.153,1.098
\end{array}                                                  \tag{52.27}
\]

**Assessment.**  Most displayed ratios are near one after genus
conditioning, for both shared and different cores, but the two stable
anticorrelations involving \((5,1)\) rule out a blanket independence model.
The data support approximate independence as a first calibration for many,
not all, pairs.  Lemma 44.4 already proves that two-slice vanishing is not
determined by the natural ray modulus; the finite ratios add no theorem
about simultaneous factorizations or growing-dimensional stacking.

### 52.4 Walls and the remaining lower-bound question

Theorem 52.1 is an **almost-all statement for one fixed slice**.  It gives no
pointwise bound on \(D(p)\), proves no instance of \(H_{\rm SPF}\), and does
not take a union over slices.  Proposition 52.3 supplies only the uniform
input for that future problem.  The growing-dimension sieve, the availability
and dependence of the genus bits across cores, and the exponential least
common multiple created by a slice partition are all left to the planned
multi-slice stacking step.  The residue-one escapes of Theorems 17.3 and
48.5 are untouched.

**Heuristic/assessment (the lower-bound wall).**  There is no lower bound
here for residual vanishing.  If the norm \(p^2+4ck^2\) is prime, Lemma 50.3
makes the slice vanish, so whenever there is no fixed local divisor one
transparent conjectural subfamily asks simultaneously for \(p\) and
\(p^2+4ck^2\) to be prime.  Hardy--Littlewood or Bateman--Horn predicts order
\(X/(\log X)^2\) after the appropriate local factors, but an unconditional
lower bound is a prime-pair parity problem beyond standard sieves.  Some
fixed progressions have a local divisor of the norm -- for example
\(3\mid p^2+20\) when \(p\equiv73\pmod {120}\) -- so there one would instead
need a prescribed almost-prime or prime-cofactor pattern, with every factor
in a wrong grade.  That is not easier by any argument given here.

A first- or second-moment strategy for the number of good prime factors does
not automatically repair the lower bound.  Its formal first-moment scale is
\(2\log\log X/\varphi(h)\), while concentration would describe typical
positive counts rather than produce zeros.  Upper-bound sieves cannot cross
this parity barrier.  It remains open here whether every fixed unforced
slice-class contains infinitely many residual vanishers.

The proved conclusion is narrower and exact: the third layer is empty at the
**congruence level**.  After the universal core law and the moving genus bit,
residual vanishing is a factorization event of relative frequency tending to
zero on every fixed unforced class.  Its infinitude per slice is open, while
the finite census shows that it remains robust in the computed ranges.
