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
strictly-lowering but non-total inverses.

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
cited as plausible merely from the cubic first moment.

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
the correct label is: **H_PF false-looking, open**.

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
clustering lower bound, and leaves the full-system label unchanged.

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
moving factors of \(4c_1c_2\) into \(K'\) are not classified.)  No
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
corrections and general rational maps remain outside this closure.  No
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
* The argument gives no single cutoff \(Y=L^{3-o(1)}\): pushing (24.24)
  toward cubic size loses both the desired subcubic density and the
  \(N=e^{\Theta(L^4)}\) transfer.  No replacement that exploits overlap
  among the large-\(R\) sets \(B_p\) was found.

### 24.6 Verdict after wave 7

**Assessment 24.10.**  H_PF remains **false-looking, open**.  The status did
not change to a refutation: Theorem 24.8 concerns a proper subsystem, and
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
sieve mass and not a one-modulus symbol certificate.

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
(23.8), independently recast in Lemma 25.6 below, gives

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
rechecking its row counts.  `verify.py (x)` hard-codes all rows for
73, 193, and 241, audits (25.1), the factorizations, parity data, gcds, and
all eleven complete counts.

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
_1b_1,
_2a_2,
_2b_2                              \tag{25.4}
\]

and the ten quadratic values obtained by multiplying each degree-two
monomial by the remaining factor \(g\).  This is the concrete coordinate
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

*Proof.*  Bézout gives independent \(\alpha,eta\) representing \(A\) and
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

All source identities and output factors are replayed end to end in
`verify.py (x)`.  The seven other primes resist this stated finite box.
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
 P-p_2=4C(A+B-1)-2>0.
\]

In the boundary case,
\(p_1=4C-2\), \(p_2=4C(B-1)-B\), and
\(P-p_2=4C-1>0\).  Positivity follows from
\(4xy-x-y\geq2xy\) for positive \(x,y\). ∎

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
modulus carrying \(v_2\geq4\).  None of the eleven remains a resister to the
full degree-\(\leq2\) classification.

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
`ES_FULL_SCAN=1` it replays the complete one-million row; the measured run
used about 85 seconds and 63 MiB.  The default block takes well below 15
seconds.

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
\(p\).  All finite computations in this section are replayed independently in
`verify.py (y)`.

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

Thus modulo the full target modulus \(4cK_\sigma\), the class is
\(P_\sigma+4c(R_\sigma\bmod K_\sigma)\); it depends on the coordinates and
has no source-only simplification.  Universally it is only
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
\(C\equiv-4c_1c_2\pmod m\).  This is an exact finite inverse test for
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
these transfer systems.  A two-case induction would still require a theorem
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
The measurements are **informational**.

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

For the launching cutoff \(Y_0=L^{3-\epsilon}\), the exact missing statement
is

\[
 { |\{n\leq N:n\in\mathcal C_{Y_0},\ \text{no hit with }R>Y_0\}|
       \over |[1,N]\cap\mathcal C_{Y_0}| }
 \geq \exp\{-o(L^3)\},\qquad \log N\asymp L^4.             \tag{27.3}
\]

Together with Theorem 24.8, (27.3) would give
\(|{\rm Av}_X(N)|\geq N\exp\{-o(L^3)\}\), contradicting H_PF's
\(N\exp(-cL^3)\) majorant mean for large \(X\).  This is a conditional
probability for the **same** prime coordinates, not a multiplication of two
independent avoidance estimates.

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

As \(|G_p|/p<3/4\), the CRT product is bounded below by the exponential of
minus a constant times (27.10).  Odd Bonferroni truncation has degree
\(O(H\log L+L^2)\).  With \(W=\sum|G_p|\leq H\pi(X)+\sum F(p)\), its total
rounding error is

\[
 \exp\{O((H\log L+L^2)L)\}=\exp\{o(L^4)\},                 \tag{27.11}
\]

by (27.6).  It is negligible against \(N\) times the CRT product when
\(\log N\geq L^4\).  This proves (27.7).  Finally
\(H\ll Y\log(2Y)\) gives (27.8). \(\square\)

The new part of (27.7) beyond a direct range extension is modest but useful:
a hybrid direct-forbidding step completely removes the class \(M=q\).  The
class that defeats the continuation below is therefore genuinely composite,
not the prime slice already pinned by Theorem 24.4.

### 27.3 Local lemma, Suen, and cluster expansion: exact failure point

**Attempt 27.2 (failed as an unconditional full extension).**  On the
conditioned product space, use the atoms (27.4), with probabilities (27.5),
and connect atoms whose moduli share a prime.  Before conditioning, the
pair-count neighborhood charge at a fixed prime \(q\) is

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

There is an even earlier defect if one uses (27.2) literally: small primes
\(q\equiv1\pmod4\), such as 5, remain free, so their shared-prime
neighborhoods retain cubic-scale charge.  A clean quarantine is available.
Fixing

\[
 n\equiv0\pmod p\quad\hbox{for every prime }p\leq z          \tag{27.13}
\]

costs \(\exp\{-\vartheta(z)\}=\exp\{-O(z)\}\), and makes every event whose
modulus has a prime factor at most \(z\) impossible, because \((M,D)=1\).
All surviving moduli are \(z\)-rough, all their prime coordinates exceed
\(z\), and their conditional atomic probabilities are exactly \(1/M\).
This is a genuine improvement over conditioning only the primes
\(3\pmod4\).

The expected upper-sieve saving for rough moduli is one factor \(1/\log z\).
Accordingly the rough pair-charge benchmark is

\[
 \Lambda_q^{\rm rough}\ \hbox{of size}\
       {L^3\over q\log z}.                                  \tag{27.14}
\]

This exposes the sharp edge of the uniform-charge LLL attempt.  At the
original \(Y=L^{3-\epsilon}\), \(H\asymp Y\log Y\), putting \(z\asymp H\)
in (27.14) still gives
\(L^\epsilon/(\log L)^2\to\infty\).  At the near-cubic cutoff (27.8), it
gives \((\log L)^\eta\to\infty\).  Thus the one-number neighborhood bound
needed by the elementary asymmetric LLL still diverges exactly when the
certificate cost is subcubic.  Suen's inequality does not supply the needed
lower void bound, and the elementary cluster expansion has the same
nonconvergent absolute neighborhood sum.

The responsible proxy class is explicit: broad-cofactor composite moduli
\(M=qk\), \(k>1\), with \(q>z\),
\(R\mid(qk+1)/4\), and all \(2^{\omega(R)}\) shifts.  Fixed prime modulus
\(M=q\) is already handled in Theorem 27.1.  Summing over the unrestricted
cofactor \(k\) is what creates (27.12).  A second direct-forbidding hybrid
would add, at coordinate \(q\), every residue \(-4R^2/s\) arising from this
class.  No proved bound keeps that set away from all the available nonzero
residues.  Its exact local cost

\[
 -\log\left(1-{|C_q\setminus B_q(Y)|\over q-b_q}\right)      \tag{27.15}
\]

can therefore be as large as \(\log(q-b_q)\), rather than
\(O(|C_q|/q)\).  Bounding the sum of (27.15) by \(o(L^3)\) is another form
of the missing large-\(R\) divisor-clustering theorem, not a consequence of
the cubic first moment.

A more refined, still incomplete route is to take, for example,
\(z=L^3/\sqrt{\log L}=o(L^3)\) in (27.13), and use prime-dependent rather
than uniform LLL charges.  Define

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
weighted form (27.17), and no finite-interval cluster-expansion transfer for
it at \(\log N\asymp L^4\), is proved here.  Dropping the exponential weight
or replacing it by its worst-case value loses more than the subcubic budget.
This is the precise point at which the promising all-prime quarantine stops.
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
\(\mathcal C_{Y_0}\) from (27.2).  For every subset \(\mathcal S\) of the
remaining fibers \((R,s)\), \(R>Y_0\), uniformly for
\(\log N\asymp L^4\), assume

\[
 \Pr_N\!\left(
 \begin{array}{c}
 n+4R^2/s\text{ has no divisor }M\leq X,\\
 M\equiv-1\pmod {4R},\quad (R,s)\in\mathcal S
 \end{array}
 \middle|\mathcal C_{Y_0}\right)
 \geq \exp\!\left\{-C\sum_{(R,s)\in\mathcal S}w_R\right\}, \tag{27.19}
\]

where

\[
 w_R=\min\left\{1,{L^{\log2+\eta}\over\varphi(4R)}\right\}. \tag{27.20}
\]

The probability is the literal uniform probability on \([1,N]\); thus
(27.19) includes, rather than hides, both the shared-coordinate conditioning
and the finite-interval transfer.  Quantification over every subset makes it
falsifiable and gives substantially more content than simply asserting the
full-system conclusion.  A proof of the weighted clique estimates
(27.16)--(27.18), plus a controlled finite cluster expansion, is one concrete
way H_DC could follow.

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
integers, uniform on \([10^{14},9\cdot10^{17})\).  Twenty-four separately seeded
`mt19937_64` streams used seeds
\(27006400+\mathtt{0x9e3779b97f4a7c15}\,t\), \(0\leq t<24\), and the C++
standard rejection-based `uniform_int_distribution`.  For every
\(M\equiv3\pmod4\), \(M\leq6400\), a Boolean table stored the exact set
\(\{-4D\bmod M:D\mid((M+1)/4)^2\}\).  Each sample stopped at its first
failed modulus; recording that first modulus gives all doubling rows without
bias.  Memory was \(O(\sum_{M\leq6400}M)\), independent of sample count.

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

**Assessment 27.5.**  H_PF remains **false-looking, open**.

* **Proved:** the multi-shift certificate itself reaches
  \(Y=L^3/(\log L)^{2+\eta}=L^{3-o(1)}\) at subcubic cost, improving the
  fixed-power cutoff in Theorem 24.8.  The same certificate can simultaneously
  remove every prime-modulus event, by Theorem 27.1.
* **Proved structural quarantine:** fixing \(n\equiv0\) at every small prime
  makes all surviving atomic moduli rough and restores exact probability
  \(1/M\) with shared-prime dependency.  This costs only \(\exp\{-O(z)\}\).
* **Failed continuation:** after the full small-prime quarantine, the
  elementary LLL neighborhood benchmark for the broad-cofactor composite
  class is still \(L^3/(q\log z)\); at every subcubic near-critical cutoff it
  diverges.  Direct local forbidding fails at the unbounded occupancy cost
  (27.15).
* **Sharpest remaining input:** a weighted rough-modulus, multi-shift
  divisor-clustering estimate such as (27.17), together with its finite
  cluster-expansion transfer; equivalently, the explicit joint void bound
  H_DC (27.19).  Individual divisor probabilities, an unweighted rough
  first moment, or another prime-slice estimate do not suffice.

Thus the status does not change.  The new unconditional gain is a
polylogarithmic extension and a prime/composite separation; the full
large-\(R\), broad-cofactor composite system remains the exact obstruction.
