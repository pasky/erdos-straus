# FOREST_INVERSE — square-exactness as an inverse problem: composites, the QNR witness, and global identities (z49, lane (a), Fable, slug `forestinv`)

**ES is open. Nothing here proves or disproves ES, ES₅, or the inverse theorem for primes.** Labels: PROVED / CONDITIONAL
(on what) / CERTIFIED (exact finite computation) / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z49_forestinv_*`,
data `data/z49_forestinv/`. Inherits FOREST_DEEP_FABLE (FDF), FOREST_DEEP_ASTRA (FDA), FOREST_CONNECTIVITY (FC), the z48/z49
CONTEXT files, and the z49 census of the parent (`data/z49_main/`).

## 0. Verdict first

**Target.** The z49 census says the T1-exact two-line union U(n) (some word of n has an endpoint ≡ 0 (mod 4) or ≡ −n (mod 8))
fails, among n ≡ 1 (mod 4) up to 10⁹, exactly at the odd squares and at 105, 2961, 3985, 25305, 111969, 978145. Theorem E
(FDF) proves the square half. The brief asks for the *inverse*: non-square ⟹ U(n), first for composites, then via a
"QNR witness ⟹ U-witness" mechanism, then via global prime-sensitive identities, else a barrier theorem.

**Outcome: clean negative on every mechanism, with the structure of the composite case settled (PROVED) and the six sporadic
failures explained (CERTIFIED + Assessment). Promise for the inverse theorem by any route tried here: 1/5.**

1. **The composite case is not a stepping stone; it is the prime case with a handicap (PROVED, §2).** In level form, U(n)
   ⟺ some tn + 1 has a divisor A ≡ −1 (mod t) with (A+1)/t ∈ V (Prop 2.2); every U-witness is coprime to n and has Jacobi
   symbol (A/n) = −1 (Theorem E′, 2.1 — Theorem E with the coprimality hypothesis removed and both classes mod 8). The
   factorisation of n enters only through (A/n), which is a *consequence*, never a hypothesis. The words of a composite
   n decompose exactly as: words of n with coprime endpoints (the prime-type lottery on the integers n + v, v ⊥ n) ⊔
   scalings of words of proper divisors n/g at levels ≡ 0 (mod g) (Lemma 2.3). A vertex sharing a factor g with n is
   non-isolated iff n/g + v/g has a divisor ≡ −1 (mod v) — a *strictly stronger* condition than the same vertex at n/g
   (Lemma 2.4). No polynomial identity in a free factorisation (a, b) produces a word of ab except the congruence words
   (Theorem 2.6): the factorisation is algebraically invisible to the word equation.
2. **CERTIFIED (§3, all n ≡ 1 (mod 8) ≤ 10⁸; `z49_forestinv_census.c`).** U holds at all 1 439 970 primes, fails at all
   4 999 odd squares, and fails at exactly the six listed composites. The *coprime* union U_cop (witness vertex coprime to n)
   fails at 0 primes, at 0 of the 4 272 030 composites coprime to 105, and at 436 composites, every one divisible by 3 or 5;
   the failure rate is multiplicative in the small prime factors (3: 1.6·10⁻⁵; 3·5: 1.3·10⁻⁴; 3·7: 1.9·10⁻⁴; 3·5·7: 1.7·10⁻³).
   Composites coprime to 105 have the *same* least-line distribution as primes. In [10⁹, 10¹⁰], among the 10 713 960
   integers with 105 | n (the hardest class), U_cop fails 119 times and U never fails; 89 of the 119 are rescued by the
   non-coprime line v = 7 (a word of n/7 at a level ≡ 0 (mod 7)).
3. **The six sporadic non-squares are explained (Assessment on CERTIFIED numbers, §3.3).** They are not near-squares and
   not Linnik shadows. They are integers with small prime factors (3·5·7, 3²·7, 5, 3·5·7, 3³, 5·7) and large least QNR
   (11, 11, 13, 13, 17, 37). A prime q | n removes q from every shifted integer n + v on the coprime lines and removes
   the lines q | v from the coprime union; the per-line fire rate drops from 0.17–0.26 (primes) to 0.14 (3 | n) and 0.10
   (105 | n) (`firerate.txt`). The lottery is the same lottery with fewer and worse tickets.
4. **QNR witness ⟹ U-witness (§4): no mechanism, and a precise reason.** In U the quadratic character of n is never an
   input (Prop 4.1): every vertex in V certifies regardless of colour, and every witness numerator is automatically a QNR
   modulus. So GRH/OAI-003, which only locate QNRs, have *nothing to act on* in U; the whole content is the shadow
   condition n mod A ∈ S_A = {−v : v | A+1, v ∈ V}, a set of at most τ(A+1) classes inside the QNR coset, of relative
   density ≪ A^{ε−1} (Prop 4.2). Forest moves do not help: Vieta moves preserve the word (BRAINSTORM/bsA F2), Ptolemy
   relations live inside one pentagon (y5), and the full remainder tree loses every cut except the bottom of a block
   (FDA Prop 4.2). The converse of Theorem E′ is false in the only sense in which it could be a mechanism (Prop 4.3).
5. **Global identities (§5).** Verified (CERTIFIED, `z49_forestinv_verify.py`): the HJ dictionary (edges ⟺ q with
   negative-CF length ≤ 3), Barkan–Hickerson–Knuth, Rademacher's congruence, and Σ_{a<p/4}(a/p) = h(−4p)/2. Consequences
   (PROVED): the colour is *digit-local* (a function of the HJ digits alone); every "all-q" identity whose weight depends on
   a bounded initial segment of digits is an interval character sum, i.e. a combination of class numbers/L-values
   (Prop 5.2) — for instance QNRs outnumber QRs by h(−4p)/2 among q with first digit 3 or 4 — while "length ≤ 3" is a
   terminal condition on the digit sequence, not a cylinder condition, and its character sum is the twisted divisor sum of
   FRONTIER §2.3 (Thm K). Barrier (Thm 5.3): the length-3 part of any cylinder-type identity is a fixed finite root set,
   which fails infinitely often (CONDITIONAL on Dickson); the identity's positivity is carried by long expansions.
6. **Sharpest barrier proved (§6, Theorem 6.1, "factorisation blindness"):** for n ≡ 1 (mod 8), whether a vertex v ⊥ n
   is non-isolated depends only on n mod v and on the multiset of residues mod v of the prime factors (with multiplicity)
   of n + v; and a composite n = ab admits no word family polynomial in (a, b) beyond the congruence families. Hence any
   mechanism that proves the inverse theorem for a class of composites by using their factorisation must do so through
   the non-coprime (scaled) lines, i.e. must prove a *harder* divisor-class statement for a divisor of n. This is B2 for
   a smaller integer with a larger modulus.

What is **not** achieved: the inverse theorem for any natural infinite class of composites (ω(n) ≥ k, q^{odd} ∥ n, …);
any mechanism manufacturing a U-witness from a QNR witness; any identity with a positive length-3 term.

## 1. Setting

n ≡ 1 (mod 4) odd. A *word* of n is (t, u, v) ∈ ℕ³ with n = tuv − u − v; numerators A := tu − 1 = (n+u)/v, A* := tv − 1 =
(n+v)/u, AA* = tn + 1. Words with u = 1 or t = 1 are allowed (they are edges {1, v} and {d+1, (n+1)/d + 1} of F_n). Put
c := −n mod 8 ∈ {7, 3} and V = V(n) := {v ≥ 1 : 4 | v or v ≡ c (mod 8)}. **U(n)** := some word of n has an endpoint in V.
Vertex form (FDF Cor C): v ∈ V is an endpoint ⟺ n + v has a divisor A ≡ −1 (mod v); then u = (n+v)/A, t = (A+1)/v, and each
such word carries an explicit 4/n identity (slot v, or slot tv − 1 / u by 2-adic bookkeeping; `z49_forestinv_words.py`
checks the identity for every witness it prints). **U_cop(n)** := some such witness has v ⊥ n (equivalently gcd(u, v) = 1,
Lemma 2.3).

**Lemma 1.1 (n ≡ 5 (mod 8) is trivial; PROVED).** If n ≡ 5 (mod 8) then (1, (n+3)/2, 3) is a word of n with endpoint 3 ∈ V,
and 4/n = 1/(2d) + 1/(nd) + 1/(2nd), d = (n+3)/8. *Proof.* 1·((n+3)/2)·3 − (n+3)/2 − 3 = n; the identity is
(n + 2 + 1)/(2nd) = (n+3)/(2nd) = 4/n. ∎ (This is Mordell's class n ≡ 5 (mod 8); odd squares are ≡ 1 (mod 8), so the
inverse problem is only about **n ≡ 1 (mod 8), c = 7, V = 4ℤ ∪ (8ℤ + 7)**. CERTIFIED to 4000, `verify.py` (6).)

## 2. Structure of U at composite n (PROVED)

**Theorem E′ (every U-witness is a coprime QNR modulus; PROVED).** Let n ≡ 1 (mod 4), v ∈ V(n), A | n + v, A ≡ −1 (mod v),
A ≥ 1. Then gcd(A, n) = 1, A ≠ 1, 2, and the Jacobi symbol (A/n) = −1 (2-part included). In particular U(n) ⟹ n is not a
square, and U(n) ⟹ n is a quadratic non-residue modulo A_odd when n ≡ 1 (mod 8).
*Proof.* A ≡ −1 (mod v) gives gcd(A, v) = 1; a prime dividing A and n divides (n + v) − n = v, so gcd(A, n) = 1. Write
A = 2^a A′. Since n ≡ −v (mod A′), (n/A′) = (−v/A′) by multiplicativity of the Jacobi symbol in the numerator. For n ≡ 1
(mod 8): Theorem E's computation (FDF, which uses only A ≡ −1 (mod v) and v ∈ V) gives (−v/A′) = −1 with A′ > 1, and
(A/n) = (2/n)^a (A′/n) = (n/A′) = −1 by reciprocity (n ≡ 1 (mod 4)). For n ≡ 5 (mod 8) and v ≡ 3 (mod 8): A′ ≡ −2^{−a}
(mod v), v ≡ 3 (mod 4), so (−v/A′) = (A′/v) = (−2^{−a}/v) = (−1/v)(2/v)^a = −(−1)^a, and (A/n) = (2/n)^a (n/A′) =
(−1)^a · (−(−1)^a) = −1; for 4 | v the n ≡ 1 (mod 8) computation applies verbatim. If A = 1 or 2 then v | 2 or v | 3, and
neither 1, 2 nor 3 lies in V(n) except v = 3 when n ≡ 5 (mod 8), where A = 2 and (2/n) = −1 ✓. ∎
CERTIFIED: all 6 187 witnesses at n ≡ 1 (mod 4), n ≤ 2000 and all 5 602 at n ≡ 1 (mod 8), n ≤ 4000 (`verify.py` (5), (5b)).
*Reading.* The colour half of the inverse problem is free in *both* directions: V-vertices certify without any colour
hypothesis (FDF Thm B), and every witness numerator is a QNR modulus for n. Nothing about the factorisation of n is
used; nothing about it can be used through the character.

**Proposition 2.2 (level form; PROVED).** U(n) ⟺ ∃ t ≥ 1 and A | tn + 1 with A ≡ −1 (mod t) and (A+1)/t ∈ V(n). The
partner is u = (A*+1)/t with A* = (tn+1)/A, also ≡ −1 (mod t). *Proof.* (t, u, v) is a word iff (tu−1)(tv−1) = tn + 1;
set A = tv − 1. Conversely A ≡ −1 (mod t) and A | tn + 1 give A* ≡ −1 (mod t) (as AA* ≡ 1 ≡ (−1)(−1)), so u, v are
integers and n = tuv − u − v. ∎ CERTIFIED against the vertex form for n ≤ 1201 (`lemmas.py` L5).
In this form the data of the problem are the integers tn + 1 and the residue n mod 8t — identical in shape for prime
and composite n. FRONTIER §2.3 (Thm K) is the generating-function version.

**Lemma 2.3 (decomposition of the words of a composite; PROVED).** Let g = gcd(u, v) for a word (t, u, v) of n. Then
g | n, and (gt, u/g, v/g) is a word of n/g with coprime endpoints. Conversely, every word (t′, u′, v′) of n/g with g | t′
and gcd(u′, v′) = 1 lifts to the word (t′/g, gu′, gv′) of n. Hence
  Words(n) = ⊔_{g | n} { (t′/g, gu′, gv′) : (t′, u′, v′) ∈ Words_cop(n/g), g | t′ },
and a V-endpoint gu′ is coprime to n iff g = 1 (because gcd(u, n) = gcd(u, tuv − u − v) = gcd(u, v)).
*Proof.* n = tuv − u − v = g(tg u′v′ − u′ − v′). ∎ CERTIFIED for n ≤ 1201 (`lemmas.py` L1).
So U(n) = U_cop(n) ∨ ⋁_{1<g|n} [n/g has a coprime word at a level ≡ 0 (mod g) whose scaled endpoint lies in V].
The second disjunct is the ES solution of n/g *scaled by g*, but only for those words of n/g whose level is divisible by
g; ordinary scaling of an arbitrary solution of 4/(n/g) is not a word of n (the "coordinate artefact" of
BRAINSTORM/apollonian_reciprocity §4 at 105).

**Lemma 2.4 (non-coprime vertex lines are strictly harder; PROVED).** Let g = gcd(v, n). Then v is an endpoint of a word
of n ⟺ n/g + v/g has a divisor ≡ −1 (mod v). *Proof.* A | n + v = g(n/g + v/g) with gcd(A, g) = 1 (A ≡ −1 (mod v)). ∎
CERTIFIED for n ≤ 1201, all v ≤ n + 2 (`lemmas.py` L2). Compare the vertex v/g at n/g, which needs a divisor of the same
integer n/g + v/g in the class −1 modulo the *smaller* modulus v/g. So every line that shares a factor with n is a
B2 event for a divisor of n with the modulus multiplied by g.

**Lemma 2.5 (all words with an endpoint dividing n; PROVED).** Let n = ab. The words of n with u = a are exactly
(t, a, a·s) with (ta − 1)·s = b + 1; in particular (t, a, a) is a word iff a | b + 2, and then ta − 1 = b + 1 and
tn + 1 = (b+1)². *Proof.* v(ta − 1) = n + a = a(b + 1) and gcd(ta − 1, a) = 1. ∎ CERTIFIED (`lemmas.py` L3, L4).
*Consequence (PROVED, trivial).* U(n) holds on the families {n = ab : a ≡ 7 (8), a | b + 2} (word (t, a, a), slot
tu − 1 ≡ 0 (mod 8) in fact, so these n even have 8/n representable), {n = ab : (ta−1) | b+1, 4 | (b+1)/(ta−1)}, and
{n = ab : (ta−1) | b+1, a(b+1)/(ta−1) ≡ 7 (8)}. These are the only words a factorisation supplies, and each is a
divisibility relation *between* a and b, i.e. a word family in disguise (§6).

**Theorem 2.6 (no polynomial word in a free factorisation; PROVED).** Let T, U, V ∈ ℚ[a, b] satisfy T·U·V − U − V = ab
identically. Then either U, V are constants c₁, c₂ and T = (ab + c₁ + c₂)/(c₁c₂), or (up to swapping U, V) V = c, T = c′ are
constants and U = (ab + c)/(cc′ − 1). In both cases the resulting words of n = ab exist exactly on a congruence class of n
(n ≡ −c₁ − c₂ (mod c₁c₂), resp. n ≡ −c (mod cc′ − 1)) and have a fixed vertex and fixed numerator.
*Proof.* Compare degrees in ℚ[a, b]: deg T + deg U + deg V = deg(ab + U + V) ≤ max(2, deg U, deg V). If deg U, deg V ≤ 1 the
right side has degree 2, so (deg U, deg V, deg T) ∈ {(0,0,2), (1,0,1), (0,1,1), (1,1,0)}. In (1,0,1), V = c ≠ 0 and U divides
ab + c, which is irreducible (c ≠ 0), impossible for a linear U; (0,1,1) is symmetric; in (1,1,0), T = c′ and
(c′U − 1)(c′V − 1) = c′ab + 1 is irreducible, impossible. If deg U = 2 then deg V = 0 (else the left side has degree ≥ 3 > 2),
so T = c′ is constant and U(cc′ − 1) = ab + c; deg U ≥ 3 is impossible by the same degree count. ∎
*Reading.* "Use the factorisation n = ab" cannot mean an identity in a and b. Every identity family of words is a
congruence family in n alone (FRONTIER B1), the Mordell covering, which misses the square classes mod 840 and hence
infinitely many non-squares of every type.

**Proposition 2.7 (why a prime is not harder than a composite; PROVED).** For v ⊥ n, whether v is an endpoint of a word
of n depends only on the multiset {ℓ mod v : ℓ | n + v, with multiplicity} (Lemma 2.4 with g = 1); and for a prime q | n
and v ⊥ q, q ∤ n + v. Hence on every coprime line the composite n is in the position of a prime p with p + v ≢ 0 (mod q)
for every prime factor q of n. ∎
*Assessment of its weight.* Small primes are the main suppliers of divisors in the class −1 (mod v) (e.g. 3 ≡ 3 (mod 4)
serves v = 4, 3·5 ≡ 7 (mod 8) serves v = 8, 3 is a QNR mod 7 and serves v = 7, …); §3.3 measures the loss.

## 3. Census (CERTIFIED computations; interpretations labelled)

**3.1 All n ≡ 1 (mod 8) up to 10⁸** (`z49_forestinv_census.c`, 40 s, 0.5 GB; enumerates every word (t, u, v) with an
endpoint in V by the three nested loops, records per n whether a witness with gcd(u, v) = 1 exists (U_cop), whether one with
gcd(u, v) > 1 exists, and the least coprime V-endpoint; `census_1e8_summary.txt`, `ucop_failures_1e8.txt`):

| class (n ≡ 1 (8), n ≤ 10⁸) | count | U fails | U_cop fails | U only via non-coprime words |
|---|---:|---:|---:|---:|
| primes | 1 439 970 | 0 | 0 | 0 |
| odd squares | 4 999 | 4 999 | 4 999 | 0 |
| composite non-squares, gcd(n, 105) = 1 | 4 272 030 | 0 | 0 | 0 |
| composite non-squares, 7 | n only | 952 000 | 0 | 0 | 0 |
| 5 | n only | 1 428 000 | 1 (3985) | 5 | 4 |
| 3 | n only | 2 856 000 | 1 (111969) | 46 | 45 |
| 5·7 | n, 3 ∤ n | 238 000 | 1 (978145) | 4 | 3 |
| 3·5 | n, 7 ∤ n | 714 000 | 0 | 94 | 94 |
| 3·7 | n, 5 ∤ n | 476 000 | 1 (2961) | 90 | 89 |
| 105 | n | 119 000 | 2 (105, 25305) | 197 | 195 |

Independent reproduction of the parent's census below 10⁸ (six failures; the parent's program `z49_main_ucensus.c` uses
the same loops without the gcd split). The primes extend FDF §4.2's "union never fails" from p ≡ 1 (24) to all p ≡ 1 (8);
the least V-line over all such primes is ≤ 116 (3361), as before.

**Least coprime V-line, histogram by bit length** (`census_1e8_summary.txt`; columns 2 … 9 = line in [2^{k−1}, 2^k), then
≥ 2^9, then none):

| class | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ≥ 2⁹ | none |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| primes | 1 360 631 | 68 506 | 10 188 | 626 | 19 | 0 | 0 | 0 | 0 |
| composites ⊥ 105 | 4 026 909 | 210 039 | 32 610 | 2 322 | 136 | 13 | 1 | 0 | 0 |
| 3 | n only | 2 530 026 | 112 108 | 189 800 | 16 281 | 6 249 | 1 070 | 264 | 156 | 46 |
| 105 | n | 56 232 | 18 149 | 30 757 | 5 839 | 4 715 | 1 639 | 707 | 765 | 197 |

EVIDENCE: composites coprime to 105 are indistinguishable from primes (relative frequencies 0.943/0.049/0.0076/0.0005
vs 0.945/0.048/0.0071/0.0004). The classes with small factors have a heavy tail that flattens into "none": once the least
coprime line exceeds ≈ 2¹², the typical outcome is that no coprime line fires at all.

**3.2 The hardest class beyond 10⁹** (`z49_forestinv_single.c -scan`, 4 min): all n ≡ 1 (mod 8) with 105 | n in
[10⁹, 10¹⁰] (10 713 960 integers; least QNR automatically ≥ 11): U_cop fails 119 times (`scan_105_1e9_1e10.txt`), U
never fails; the non-coprime rescue line is v = 7 for 89 of them, v = 12 for 23, v = 15 for 4, and 20, 24, 36 once each.
The U_cop failure rate falls from 1.7·10⁻³ (≤ 10⁸) to 1.1·10⁻⁵ (10⁹–10¹⁰) — a lottery with ≍ log² n tickets, not a structure.
CONJECTURE (inverse theorem, composite form): U(n) for every non-square n ≡ 1 (mod 8) with n > 978145. EVIDENCE: the
census to 10⁹ (parent) and this scan of the hardest class to 10¹⁰.

**3.3 Per-line fire rates by residue class** (`z49_forestinv_firerate.py`, `firerate.txt`; 400 integers near 10⁶ per
population, lines v ∈ V, 4 ≤ v ≤ 200, v ⊥ n):

| population | v ≡ 0 (3) | v ≡ 1 (3) | v ≡ 2 (3) | P(some line ≤ 200 fires) |
|---|---:|---:|---:|---:|
| p ≡ 1 (24) prime | 0.170 | 0.156 | 0.261 | 1.000 |
| p ≡ 17 (24) prime | 0.203 | 0.317 | 0.141 | 1.000 |
| n ≡ 1 (24) composite ⊥ 35 | 0.167 | 0.144 | 0.253 | 0.993 |
| n ≡ 17 (24) composite ⊥ 35 | 0.202 | 0.311 | 0.136 | 1.000 |
| n ≡ 9 (24) (3 | n) ⊥ 35 | — | 0.145 | 0.135 | 0.995 |
| n ≡ 1 (24), 5 | n, 7 ∤ n | 0.126 | 0.140 | 0.213 | 0.998 |
| 105 | n | — | 0.098 | 0.100 | 0.953 |

CERTIFIED numbers; EVIDENCE for the reading: the fire rate of a line is governed by n mod 24 (and mod the small primes),
not by primality — composites and primes in the same class agree to the second digit; the lines on which 3 | n + v
(v ≡ −n (mod 3)) fire at 0.26–0.32, the others at 0.14–0.20; for 3 | n the lines v ≡ 0 (3) are gone and no remaining
line gets the prime 3, so all fire at 0.14; with 105 | n all fire at 0.10 and 4.7 % of such n have no coprime line ≤ 200.
Assessment: a composite with small factors is a prime in the Mordell-hard class with the small-prime "class adjusters"
removed from every shifted integer. This, and nothing else, is what distinguishes composites from primes in U.

**3.4 The six sporadic failures** (`controls.txt`, `z49_forestinv_words.py n`):

| n | factorisation | least QNR r(n) | nearest square offset | coprime lines | non-coprime lines |
|---:|---|---:|---|---|---|
| 105 | 3·5·7 | 11 | 11² − 16 | all dead | all dead |
| 2961 | 3²·7·47 | 11 | 55² − 64 | all dead | all dead |
| 3985 | 5·797 | 13 | 63² + 16 | all dead | all dead |
| 25305 | 3·5·7·241 | 13 | 159² + 24 | all dead | all dead |
| 111969 | 3³·11·13·29 | 17 | 335² − 256 | all dead | all dead |
| 978145 | 5·7·27947 | 37 | 989² + 24 | all dead | all dead |

Near-squareness is a red herring: the median relative distance to the nearest square among the 192 U_cop failures ≤ 2·10⁶
is 0.24 (uniform: 0.25), and no deformed-T1 line death (k + v = 0 or v(k+v) = □ at n = m² + k) kills more than one line
at any of the six. The operative features are (i) small prime factors (all six are divisible by 3 or 5, four by 7) and
(ii) a large least QNR (the 436 U_cop failures ≤ 10⁸ have r(n) ∈ {5: 21, 11: 111, 13: 101, 17: 90, 19: 37, 23: 27, 29: 26,
31: 9, 37: 5, 41: 3, 43: 5, 53: 1}; for a random n ≡ 9 (mod 24) the probability of r ≥ 11 is 1/4). Both features lower the
per-line fire rate (§3.3; and a line v = 4 needs a prime factor ≡ 3 (mod 4) of n + 4, all of which are QNRs, hence ≥ r(n)).
"Linnik shadow" is the wrong name: a Linnik/Dickson shadow blocks a *fixed* initial segment of lines (FDA Thm 6.1); here
*all* lines are blocked, which is only ever a lottery outcome, and the lottery is loaded by (i) and (ii).

**3.5 Controls.** Odd squares: U and U_cop fail at all 4 999 squares ≤ 10⁸ (Theorem E; `SQUARE-VIOLATION` never printed)
and at 9, 25, 49, 81, 121, 169, 225 by the single-n tool. Numerator 8: at n = 17 and 241 no word has an endpoint ≡ 0 (mod 8)
(`lemmas.py`), as Lean L9901 requires; the only 8/n statement here (Lemma 2.5: n = ab, a ≡ 7 (8), a | b+2 gives 8 | tu − 1)
needs a divisor a ≡ 7 (mod 8) of n and so never applies to a prime. Hard primes (`controls.txt`): U holds with least
V-line 7, 4, 4, 87, 116, 7, 56, 55, 8 at 193, 409, 577, 2521, 3361, 5569, 9601, 66529, 8813281. No composite-only mechanism
is claimed to say anything about primes (there is none to claim).

## 4. The non-squareness witness: why no converse mechanism exists

**Proposition 4.1 (the character is never an input of U; PROVED).** Let n ≡ 1 (mod 8). (a) Every edge of F_n at a vertex
v ∈ V is a certificate, whatever the colours (FDF Thm B; 2-adic, no character). (b) Every U-witness numerator A satisfies
(A/n) = −1 (Theorem E′). (c) Hence for any statement of the form "ℓ is a prime with (n/ℓ) = −1" (or any set of such
statements, e.g. the conclusions of GRH or OAI-003 about least QNRs), the truth of U(n) is unchanged if the statement is
replaced by its negation for all ℓ not dividing some witness. ∎
*Reading.* FDF §3 proved that the colour half of the covering sets G_A is free. Prop 4.1 is the sharper statement for U:
the colour half is *empty* — U is defined without the character, and the character appears only in the conclusion
(Theorem E′). A hypothesis that supplies QNRs supplies nothing that U can consume.

**Proposition 4.2 (what a single QNR modulus witnesses; PROVED).** For A = 2^a A′ (A′ odd) let S_A := {−v mod A : v | A + 1,
v ∈ V}. Then (a) A is a U-witness for n iff n mod A ∈ S_A; (b) S_A is contained in the QNR coset {r : (r/A′) = −1}
(Theorem E′); (c) |S_A| ≤ τ(A+1) − 1 ≪ A^ε, so among the integers n ≡ 1 (mod 8) with (n/A′) = −1 the proportion witnessed
by some A with odd part A′ is ≪ Σ_{a ≥ 0} τ(2^a A′ + 1)/(2^{a−1}φ(A′)) ≪_ε A′^{ε−1} → 0.
*Proof.* (a) is the vertex form read mod A (v ≤ A + 1 and v ≡ −n (mod A) determine v, up to v ∈ {1, A+1} which both give
the class −1). (b), (c) as stated. ∎
So a QNR witness ℓ (prime, (n/ℓ) = −1) yields a U-witness only if n lies in one of the ≤ τ(2^a ℓ + 1) shadow classes modulo
2^a ℓ — the B2 event verbatim, with the colour layer already removed. The density of these classes is (log ℓ)/ℓ; summing over
the QNR primes ℓ ≤ X gives an expected (log X)²/16 firings, the same count as for *any* family of ≍ X/log X lines: the QNR
property of ℓ buys nothing, exactly as Prop 4.1 predicts.

**Proposition 4.3 (no converse of Theorem E′ at a fixed modulus; PROVED).** Let A ≥ 17 be odd and not a perfect square.
Then there is a residue class r (mod A) with (r/A) = −1 such that A is a U-witness for no n ≡ r (mod A); by CRT the class
contains infinitely many n ≡ 1 (mod 8), all QNRs modulo A.
*Proof.* The witnessed classes mod A are S_A, |S_A| ≤ τ(A+1) − 1 (Prop 4.2(a),(c)); the QNR classes mod A number φ(A)/2
(the Jacobi symbol (·/A) is a non-principal character on (ℤ/A)^× when A is not a square). So it suffices that
τ(A+1) < φ(A)/2. For A ≥ 10⁵ this follows from τ(m) ≤ 2√m and φ(A) ≥ A/(e^γ log log A + 3/log log A)
(Rosser–Schoenfeld); for A < 10⁵ it is CERTIFIED by direct check (`sympy`, one line), the only exceptions among all A ≥ 3
being A ∈ {3, …, 12, 14, 15, 20}. ∎
*Scope.* This refutes "a QNR witness can be converted into a U-witness at its own modulus". It says nothing about
conversions at other moduli (the covering lottery of FDF §3/M5), and the union over all a of the shadows of 2^a A′ is
not controlled here.

**Forest and tree moves (Assessment, citing PROVED results).** Vieta involutions on the Fricke cubic preserve (v, t, u) and
hence the ES status of the word (BRAINSTORM/bsA_fricke_vieta F2); Ptolemy relations are the five relations inside one
pentagon (y5_transport_is_ptolemy, Lemma 1) and encode only the 2-adic depth of its even edge; the full remainder tree T_n
retains at most two arrows per quotient block (FDA Prop 4.2) and its least-QNR block is deleted entirely on an infinite
progression (FDA Prop 4.3). Astra's target form (10.1), "a virtual cut survives pruning", is therefore not a mechanism but
the statement to be proved; nothing in §2 changes that. The calibration of the z49 context (H₄ > exp((log p)^{1/2−o(1)})
infinitely often, heuristically) says the surviving cut must sometimes be far from every small vertex; Prop 4.2(c) says
each modulus contributes a vanishing fraction; together: a proof must use unboundedly many moduli at once, with no
pooling across them (SS8 Lemma 2.3) — the lottery.

## 5. Global prime-sensitive identities over all q

**5.1 Dictionary (CERTIFIED, `verify.py` (1)–(4)).** For p prime, q ∈ [1, p−1]: the negative (HJ) expansion p/q =
[[b₁, …, b_k]] has k ≤ 3 iff q = tv − 1 for a word (t, u, v) = (b₂, b₁, b₃) of p (k = 2: u = 1; k = 1: q = 1, the loop at
vertex 1); verified at all 37 primes p ≡ 1 (4) below 400 with no mismatch. BHK: 12 s(q, p) = Σ_i (b_i − 3) + (q + q*)/p
(2 960 pairs); Rademacher: 12 p s(q, p) ≡ p + 1 − 2(q/p) (mod 8); Σ_{0<a<p/4} (a/p) = h(−4p)/2 for p ≡ 1 (mod 4), with
h(−4p) computed by counting reduced forms (37 primes).

**Proposition 5.1 (digit-locality; PROVED).** The map q ↦ (b₁, …, b_k) is a bijection from {q ∈ [1, n−1] : gcd(q, n) = 1}
onto the sequences of integers ≥ 2 with negative continuant K(b₁, …, b_k) = n; q and q* are the continuants of (b₂, …, b_k)
and (b₁, …, b_{k−1}). Hence any function of (q, q*, digits) is a function of the digits, and by Rademacher + BHK so is the
Jacobi symbol (q/n): (q/n) ≡ (n + 1 − n Σ_i(b_i − 3) − q − q*)/2 (mod 4), i.e. the colour of a word is a function of its
shape (LOWERTAIL_DEEP_FABLE Lemma 1.2 and FDF Thm B are the length-3 case). Every "identity over all q" of the form
Σ_q F(q, q*, digits) = G(n) is therefore Σ_{K(b)=n} F(b) = G(n): a statement about the word-generating function
Σ_n x^n Σ_{K(b)=n} F(b), and for F supported on length ≤ 3 it is Σ_{t,u,v ≥ 2} F(u,t,v) x^{tuv−u−v} plus boundary terms —
FRONTIER §2.3 (Thm K) in the colour-twisted case. ∎

**Proposition 5.2 (cylinder identities are interval character sums; PROVED).** Fix j ≥ 1 and digits (β₁, …, β_j). The set
of q whose expansion begins with (β₁, …, β_j) is the set of q with p/q in an interval I(β) with endpoints p·(rationals
determined by β) — the cylinder set of the negative-CF Gauss map. Consequently, for any weight w depending only on the
first j digits, Σ_q w(q)(q/p) = Σ_β w(β) Σ_{q ∈ I(β)} (q/p), a finite combination of character sums over intervals with
rational endpoints, i.e. of generalised Bernoulli numbers B_{1,χψ} / class numbers (for j = 1 and β₁ ∈ {3, 4}:
Σ_{p/4 < q < p/2} (q/p) = −h(−4p)/2, so **QNRs outnumber QRs by h(−4p)/2 ≥ 1 among the q with first digit 3 or 4**, while
first digit 2 contributes 0 for p ≡ 1 (mod 4)). ∎
*What this gives and does not give.* The first-digit b₁ = u is the smaller endpoint of the word when k ≤ 3, so the h(−4p)
excess sits on the vertex lines u ∈ {3, 4} — among ≍ p/12 values of q of which only ≍ τ(p+3) + τ(p+4) have length 3. The
excess ≍ p^{1/2±o(1)} is carried by long expansions. No cylinder (initial-segment) condition can see the *end* of an
expansion.

**Theorem 5.3 (barrier for cylinder-type identities).** Let j ≥ 1 and let w(q) = w(b₁, …, b_j) be a weight depending on
the first j HJ digits of p/q and supported on finitely many digit patterns. Put W(p) := Σ_q w(q)·[(q/p) = −1] and let
W₃(p) be its restriction to q of HJ length ≤ 3.
(a) (PROVED) W(p) is a finite combination of interval character sums Σ_{q ∈ I} (q/p) with I ⊂ (0, p) having endpoints in
p·ℚ (plus the trivial count Σ_q w(q)/2), hence of generalised Bernoulli numbers B_{1,χ_pψ} with ψ of bounded conductor.
(b) (PROVED) W₃(p) is a weighted count of bichromatic words of p whose first digit b₁ = u (the endpoint on the A*-side) lies
in a fixed finite set (j = 1), or with (u, t) in a fixed finite set (j = 2), or of finitely many fixed words (j ≥ 3).
(c) (CONDITIONAL on Dickson, via LOWER_TAIL_ASTRA Thm 3.1 / FDA Thm 6.1) For every finite set of vertices there are
infinitely many primes p ≡ 1 (mod 24) at which none of them is incident to a bichromatic edge; at such primes W₃(p) = 0
while W(p) ≍ p^{1/2±o(1)} > 0 whenever its leading L-value is non-zero (always, for real characters). Hence no identity in this
class has a length-3 part that is positive at every prime, and its positivity is carried by q of length ≥ 4.
*Proof.* (a): the cylinder {q : b₁(q) = β₁, …, b_j(q) = β_j} is {q : p/q ∈ J(β)} for an interval J(β) of the negative-CF
Gauss map, i.e. an interval of q with endpoints p·(rational); the character sum over it is a Bernoulli-number expression by
Dirichlet's formula for Σ_{q ≤ αp} χ(q). (b): for a word (t, u, v) with q = tv − 1 the first digit is ⌈p/q⌉ = u since
p/q = u − v/(tv − 1) with 0 < v/(tv−1) ≤ 1 (t ≥ 2; the boundary cases t = 1, u = 1 are the shorter expansions); cylinders of
depth 2 fix (u, t), of depth 3 fix (u, t, v) and hence p. (c) is the cited theorem applied to the finite vertex set of (b). ∎
(The content is only "cylinders are intervals, length is not a cylinder condition"; it is recorded as a theorem because the
brief asked for the barrier in that form. Part (c) is as conditional as every fixed-root statement in the campaign.)

**5.4 Other prime-sensitive inputs (Assessment).** Zolotarev's lemma expresses (q/p) through the inversion number of
x ↦ qx on ℤ/p, which is Meyer's formula for 3p·s(q, p) up to elementary terms — again a digit-local quantity. The complete
sum Σ_v χ(v) = 0 is Astra's identity (8.1) regrouped by components and has no positive term (FDA §8). Dedekind sums over
all q satisfy Σ_q s(q, p) = 0, Σ_q s(q,p)² ≍ p² (Walum/Conrey et al.), neither of which separates length. There is no
candidate left in this class; the finite-dictionary certification of (I)5 (no linear relation between ES counts and 54
classical functions) is the computational shadow of the same fact.

## 6. The sharpest barrier for the mechanisms tried (PROVED)

**Theorem 6.1 (factorisation blindness of the sign-free union).** Let n ≡ 1 (mod 8).
(i) For every v ∈ V with gcd(v, n) = 1, the predicate "v is an endpoint of a word of n" is a function of the multiset of
residues modulo v of the prime factors of n + v (with multiplicity) alone; it does not depend on the factorisation of n,
and the prime factors of n do not occur among those of n + v.
(ii) For v ∈ V with g = gcd(v, n) > 1, the predicate is "n/g + v/g has a divisor ≡ −1 (mod v)" (Lemma 2.4): the same
predicate for the divisor n/g of n at the vertex v/g, with the modulus enlarged from v/g to v.
(iii) The words of n are the disjoint union over g | n of the lifts of the coprime words of n/g at levels ≡ 0 (mod g)
(Lemma 2.3); U(n) is the disjunction of the corresponding scaled-endpoint conditions.
(iv) No family of words of n = ab given by polynomials in (a, b) exists beyond the congruence families (Theorem 2.6).
(v) The quadratic character of n is never an input of U and is a function of the witness (Theorem E′, Prop 4.1).
*Proof.* (i) is Lemma 2.4 with g = 1 together with gcd(n + v, n) = gcd(v, n) = 1; (ii)–(v) are the cited statements. ∎

**Consequences for the brief's work items (Assessment on top of Theorem 6.1).**
* *Natural classes of composites.* (i) says that for the coprime lines a composite is exactly a prime in its residue class
  mod small moduli; (ii)–(iii) say the extra lines are B2 events for a *divisor* with a *larger* modulus; (iv) says no
  identity bridges a and b. Thus the inverse theorem for a class like {ω(n) ≥ k} or {q^{odd} ∥ n} would have to be proved
  by the same means as for primes, plus the handicap of §3.3. No such class is proved here, and the census says the
  classes with small factors are strictly harder, not easier. The only composite classes on which U is PROVED are
  divisibility-relation families (Lemma 2.5), which are word families in different coordinates.
* *Where a factorisation is needed and why a prime is not harder.* A factorisation is needed exactly in (ii)–(iii) — to
  define the scaled lines — and it makes each of those lines harder than the corresponding line of the divisor. For a prime
  there are no scaled lines and no handicap: among all n ≡ 1 (mod 8) in a given class mod 840, primes are the *easiest*
  population for U_cop (§3.1 histogram), tied with composites coprime to 105.
* *The six sporadics* are §3.4: loaded lotteries, lost.
* *The QNR witness* is §4: U consumes no colour information.
* *Global identities* are §5: cylinder identities see intervals of q, not lengths.

**Exact remaining gap (unchanged from FDF §6 and FDA §10, now with the composite side closed).** For a prime p ≡ 1 (mod 8):
some v ∈ 4ℤ ∪ (8ℤ+7) such that p + v has a divisor ≡ −1 (mod v); at a non-square composite the same, with the lines
v ⊥ n unchanged and the lines gcd(v, n) = g > 1 replaced by "n/g + v/g has a divisor ≡ −1 (mod v)". Nothing in the
factorisation, the character, or the digit-local identities touches the divisor class of one shifted integer. The
heuristic tail of the z49 context (survival ≈ exp(−c log² X)) is consistent with every count in §3; the composite data
of §3.2 (0 failures of U in the hardest class to 10¹⁰) are the strongest numerical support so far for the inverse
conjecture at composites, and say nothing about primes beyond what FDF §4 already says.

## 7. Screening checklist (FRONTIER §4) for the only positive statements made (Lemma 2.5 families; Theorem E′)

| line | status |
|---:|---|
| 1 | PASS: Theorem E′ fails at squares by construction ((A/n) = −1 is impossible); Lemma 2.5 needs a divisor a ≡ 7 (8) or a class condition on (b+1)/(ta−1), never satisfied at n = m² (Theorem E). |
| 2 | PASS: at 17, 241 no word has an endpoint ≡ 0 (8); the 8/n family of Lemma 2.5 needs a ≡ 7 (8), a | n, a > 1. |
| 3 | PASS: no numerator-uniform law. |
| 4 | FAIL for the inverse theorem (as expected): the tied-modulus divisor event of one integer, Theorem 6.1 (i)–(ii). |
| 5 | PASS: every statement is at fixed n; §3.3 rates are labelled EVIDENCE. |
| 6–7 | N.A. (no main term claimed). |
| 8 | Lemma 2.5 families are B1-type word families and are labelled so (Theorem 2.6). |
| 9 | PASS/explained: the class layer is the whole problem; the character layer is empty in U (Prop 4.1). |
| 10–13 | N.A. |
| 14 | PASS (finite): all listed hard primes, §3.5. |
| 15 | Near-squares examined and discarded as the explanation of the sporadics (§3.4). |
| 16–17 | N.A. / FAIL as for every covering route (the witness divisor needs large prime factors in a tied class). |

## 8. Reproduction (total ≈ 10 min CPU, peak RSS 0.5 GB; `ulimit -v 8000000` throughout)

```sh
gcc -O2 -Wall -o /tmp/z49census scripts/z49_forestinv_census.c -lm
timeout 3000 /tmp/z49census 100000000 > data/z49_forestinv/ucop_failures_1e8.txt 2> data/z49_forestinv/census_1e8_summary.txt
gcc -O2 -Wall -o /tmp/z49single scripts/z49_forestinv_single.c -lm
timeout 7200 /tmp/z49single -scan 1000000000 10000000000 105 11 > data/z49_forestinv/scan_105_1e9_1e10.txt 2> data/z49_forestinv/scan_105_1e9_1e10.log
timeout 300 /tmp/z49single 193 409 577 2521 3361 5569 9601 66529 8813281 17 241 9 25 49 81 121 169 225 > data/z49_forestinv/controls.txt
timeout 900 uv run python scripts/z49_forestinv_verify.py        # dictionary, BHK, Rademacher, h(−4p), Theorem E′, Lemma 1.1
timeout 900 uv run python scripts/z49_forestinv_lemmas.py        # Lemmas 2.2–2.5 on all n ≡ 1 (8) ≤ 1201; numerator-8 control
timeout 900 uv run python scripts/z49_forestinv_firerate.py > data/z49_forestinv/firerate.txt
uv run python scripts/z49_forestinv_words.py 105                 # print the U-words (none) of any n, with ES identities
```
`z49_forestinv_words.py` is the Python toolkit (vertex form, level form, slot identities checked with exact fractions).
Hostile review: see §9.

## 9. Hostile internal review and repairs

(filled in after the deep-mode review; see the end of the file)
