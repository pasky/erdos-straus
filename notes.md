# The Erdős–Straus conjecture: a serious attempt, and an honest map of the wall

*Working notes, 2026-08-16. Companion computations: `verify.py` (runs in ~13 s).*

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
fixed-order tilts.  Neither increment is claimed here.

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
remaining named route beyond Vaughan's 2/3.

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
∎  (The three substitution computations are replayed symbolically in
`verify.py (p)`.)

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
(z₀ may be a product of primes all exceeding p).  Either way the grant is
useless: p's criterion consults these numbers only through their divisor
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
variety, and §10.5 rules out every known mechanism for one.

**Audit conclusion (assessment).**  These three obvious
minimal-counterexample routes yield no known transfer: solvability
propagates upward through multiplication (Lemma 1.1) and sideways along
harvested class structures, and no general construction linking p's
criterion to the solvability of smaller integers is available.  Cleverer
transfers remain unexcluded — that is exactly the open P4 slot — but the
naive attempts are now executed rather than presumed.

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
\(M_0=24L_K=\exp(K(1+o(1)))\), hence only requires \(K\le(1-\epsilon)L\)
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

Using only \(L_K\le\exp(K(1+o(1)))\) gives the coarser budget
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
realized bound.

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
\(k\ge2\).  Grouped by Case-B minimal \(q\), the primes having a \(k=1\)
witness give:

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
