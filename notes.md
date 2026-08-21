# The Erdős–Straus conjecture: a serious attempt, and an honest map of the wall

*Working notes, 2026-08-16. Companion computations: `verify.py` (runs in ~2 s).*

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
(exactly two). *(In the literature these are the Type II / Type I solutions of
Aigner and Rosati — labels from memory, possibly swapped.)*

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

### 14.4 The budget ceiling of witness stacking (assessment)

The following accounting is a calibration of *this* framework —
second-moment per-modulus factors built from multiplicative witnesses
above a floor — not a nonexistence theorem; its model assumptions are
named as they are used.  For modulus w to contribute a constant factor
δ_w ≤ 1/2, a second-moment (Paley–Zygmund) argument needs the tilted
family to cover (Z/w)×, which for iid-model residues means
h ≤ e^{(1−1/c)λ_w} (Lemma 13.7 and its signed analogue), i.e. window
mass λ_w ≥ (1−1/c)⁻¹ log h.  Mass λ above a floor u forces the window
top log v ≥ e^{λ} log u, and the moment mass is carried by witnesses
containing top-block primes (the measure ∑ log q/q is uniform in
log q), so the level consumed by modulus w is ≳ h^{1/(1−1/c)}·log u.
The total level is capped by log N (the rounding budget; with primality
it would be BV's (1/2)log N — worse, see W2).  Hence
∑_{w≤W} h_w^{1/(1−1/c)} ≲ log N, i.e. W^{1+1/(1−1/c)} ≲ log N: θ ≤ 1/3
for c = 2, θ ≤ 2/5 for c = 3, and θ → 1/2 as c → ∞ — but the signed
alphabet on squarefree window parts is c = 3 (exponents −e..e, e = 1),
and higher multiplicities have no density.  One genuine upgrade remains
inside the framework: Selberg-optimal weights supported on the closure
of the witness system would need only witness *mass* e^{λ}/h ≥ h^{ε}
(λ ≥ (1+ε)log h) rather than concentration (λ ≥ (3/2)log h), relaxing
the consumption to ∑_{w≤W} h_w ≲ log N and the cap to θ = 1/2 − o(1).
The missing piece is a support-restricted Selberg minimization — the
admissible support {v : some signed subproduct of v's primes ≡ −1
(mod w)} is not divisor-closed, so the classical diagonalization does
not apply verbatim.  Named open lemma.  Beyond 1/2, within these model
assumptions, the wall is structural: covering a group of size h with
products of primes above any floor consumes level ≥ h per modulus, and
∑_{w≤W} h_w ≍ W².  **Assessment: the joint multi-modulus route
contemplated in §13.3(3), as executed here, tops out at θ = 1/2 and
does not reach Vaughan's 2/3.**

### 14.5 The wall-map: what beating 2/3 now requires

Assessments, not theorems; each is a proof-level obstruction to the
named technology with its load-bearing computation cited.

* **(W1) Witness stacking caps at 1/2** (§14.4): group-covering forces
  level consumption ≥ h_w per modulus; budget log N; so ≤ (log N)^{1/2}
  moduli — tilt or Selberg, subsets or signed, integers or primes.

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

Status after phase eight: campaign record E(N) ≪
N exp(−(log N)^{2/5−o(1)}) (Theorem 14.4), Vaughan unbeaten; open
frontier = (i) restricted-Selberg lemma (→ θ = 1/2 exactly at the
framework ceiling), (ii) the declustering door of W3 (→ θ > 2/3, new
algebraic input required).

Numerics: `verify.py (l)` checks the signed local-factor identities
(first and second moments, all character pairs mod 7, toy window), runs
a toy integer-side stack ∑Λ² against ∏δ_w on real data
(informational), confirms Λ = 1 on witness-free integers, and
reconstructs exact unit-fraction solutions from signed witnesses via
d = na/b and Theorem 3.1(B).

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
primes through k = 20.  Thus there is nothing new from this experiment to plug
into the PW large sieve, and θ = 2/3 remains unbeaten by this unit.

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
