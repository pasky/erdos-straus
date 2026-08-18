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
unconditional theorem

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

* **Over-dispersion.**  Unconditioned second moments fail: heuristically
  (local densities; sizes not proved here) E T₀ ≍ (log N)/w but
  E T₀² ≍ (log N)³/w², so Paley–Zygmund alone would give only
  P(T₀ > 0) ≫ 1/log N — the classic Erdős/Ford divisor-concentration
  phenomenon.  Conditioning on the factor count is essential.

* **The k! wall for naive moment transfer.**  Reproducing the marked
  moments of Lemma 12.5 to order 2K, K ≍ log log N, via
  Bombieri–Vinogradov costs a tuple-multiplicity (2K)! =
  exp(2(1+o(1)) L log L), while BV saves only (log N)^{−A} = e^{−AL} for
  fixed A.  Since log L → ∞, fixed-level BV cannot pay for growing-order
  moments by itself.  This multiplicity accounting is elementary but is a
  back-of-envelope obstruction, not a nonexistence theorem; it explains
  why the §12.5 demand resists the standard toolchain.

The weakened, fixed-order form.  Let A_k = {p ≤ N : ω(n_w(p)) = k} and
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

The whole of this subsection is a **schematic research program**, not a
proof: H1–H3 are stated targets, their model values are defined by the
iid-residue model, and the implication chain above is only as strong as
those inputs.  Both H1 and H2 are **fixed-order** statements: sums of
#{p : lcm(d₁,d₂) | n_w(p), ω(n_w(p)) = k} over pairs of divisors below
level N^{1/2} — i.e. Selberg–Delange/Sathe-type asymptotics along shifted
primes in progressions, on average over the progression modulus (a
Bombieri–Vinogradov flavor for ω-restricted shifted primes).  The
character-sum side is expected to be benign: the nonprincipal
contributions should be controlled by L(1,χ)-size Euler products,
O(log w) each, against a main term of size (log N)^{c}/h (heuristic
sizing, not proved).  The hard part is the joint (AP-average ×
ω-restriction × primality) uniformity.  This is the sharpened Phase-2
gap: **two fixed-order BV-average Sathe–Selberg asymptotics (H1, H2),
plus their w-joint version (H3), would imply every θ < 1**.  Nothing
beyond fixed second order is demanded by the target — that is the
reduction; proving H1–H3 is the successor project.

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
