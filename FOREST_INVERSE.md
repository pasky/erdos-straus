# FOREST_INVERSE — square-exactness as an inverse problem: composites, the QNR witness, and global identities (z49, lane (a), Fable, slug `forestinv`)

**ES is open. Nothing here proves or disproves ES, ES₅, or the inverse theorem for primes or for any natural class of
composites.** Labels: PROVED / CONDITIONAL (on what) / CERTIFIED (exact finite computation) / EVIDENCE / CONJECTURE /
Assessment. Scripts `scripts/z49_forestinv_*`, data `data/z49_forestinv/`. Inherits FOREST_DEEP_FABLE (FDF),
FOREST_DEEP_ASTRA (FDA), FOREST_CONNECTIVITY (FC), LOWER_TAIL_ASTRA (LTA), DEDEKIND_ES (DK), the z48/z49 CONTEXT files and
the parent's z49 census (`data/z49_main/`). Two hostile deep-mode review passes (`reviews/z49-forestinv-review.md`, 27
findings; `reviews/z49-forestinv-review2.md`, 13 residual findings) and a cross-model review (Astra,
`reviews/z49-forestinv-xreview.md`, SOUND with four minors) were folded in; §9 lists what they changed.

## 0. Verdict first

**Target.** The z49 census says the T1-exact two-line union U(n) — some word of n has an endpoint ≡ 0 (mod 4) or
≡ −n (mod 8) — fails, among n ≡ 1 (mod 4) up to 10⁹, exactly at the odd squares and at 105, 2961, 3985, 25305, 111969,
978145. Theorem E (FDF) proves the square half. The brief asks for the *inverse*: non-square ⟹ U(n), first for natural
classes of composites, then by a "QNR witness ⟹ U-witness" mechanism, then by global prime-sensitive identities, else a
barrier theorem. (In ES₅ form the inverse statement is DK Conjecture SQ₅: λ(n) ≤ 3 ⟺ n non-square, n ≠ 105.)

**Outcome: an unsuccessful mechanism search. No natural class of composites is proved; no QNR-to-witness mechanism
exists in the forms tried; no identity with a positive length-3 term was found. Promise for the inverse theorem by any
route tried here: 1/5.** What is retained, with labels:

1. **PROVED, narrow.** Theorem E′ (§2.1): every U-witness numerator A at any n ≡ 1 (mod 4) is coprime to n and has
   Jacobi symbol (A/n) = −1 (2-part included, both classes mod 8, boundary A = 2 only at v = 3, n ≡ 5 (8)) — the Jacobi
   form of FDF Theorem E at composite n. Lemma 2.3: the words of n are the disjoint union, over g | n, of the lifts
   (t′/g, gu′, gv′) of the coprime-endpoint words (t′, u′, v′) of n/g with g | t′ (the gcd-indexed form of DK §8.3's
   scaling map). Lemma 2.4: a vertex v with g = gcd(v, n) is word-incident iff n/g + v/g has a divisor ≡ −1 (mod v).
   Theorem 2.6 (a classification, not a non-existence statement): in two *free* variables (a, b), the nonzero
   polynomial solutions of TUV − U − V = ab are exactly the two shapes with both endpoints constant, or one endpoint and
   the level constant — with positive integer constants, congruence families in n = ab; this completes the partial
   coefficient comparison of DK §9.2 to all polynomial shapes and corrects its assertion that the constant-endpoint
   shape is impossible ((T, U, V) = (ab + 2, 1, 1) is one). Props 4.2–4.3: for a fixed odd non-square modulus
   A ≥ 17 the set of n witnessed by A is ≤ τ(A+1) − 1 classes mod A inside the φ(A)/2 QNR classes, so some QNR class mod A
   is never witnessed by A.
2. **PROVED, trivial, on request of the brief.** U holds on explicit divisibility-relation families of composites
   n ≡ 1 (mod 8) (Lemma 2.5, Prop 2.8), e.g. n = ab with a ≡ 7 (8), a ∣ b + 2 (diagonal word, which even gives 8/n), or
   a ≡ 5 (8), b = 2a + 3 (the review's family a(2a+3), a coprime word; more generally (a+1) ∣ (b−1) with
   (b−1)/(a+1) ≡ 2 (mod 4)). In each case the word can also be written in terms of a divisor of n + v alone (Prop 2.8);
   whether a factor relation can force an incidence that the shifted-divisor description does not make visible is not
   decided here.
3. **CERTIFIED (§3).** All 9 ≤ n ≡ 1 (mod 8) ≤ 10⁸: U holds at all 1 439 970 primes, fails at all 4 999 odd squares > 1 and at
   exactly the six composites. The coprime union U_cop fails at 0 primes, 0 of the 4 272 030 composites coprime to 105,
   and 436 composites, all divisible by 3 or 5 (427 by 3). In [10⁹, 10¹⁰], over the 10 713 960 non-square n with 105 ∣ n,
   U_cop fails 119 times and U never; 89 of the 119 are rescued by the line v = 7 (a lifted word of n/7).
4. **EVIDENCE (§3.3–3.4), model not theorem.** In samples of 400, per-line fire rates vary with n mod 24 and with the
   small primes dividing n, with no visible dependence on primality (primes and composites in the same class differ by at
   most ≈ 0.012); the elementary fact behind this is that a prime q ∣ n never divides n + v on a coprime line and removes
   the lines q ∣ v from the coprime union. The six sporadic failures are all divisible by 3 or 5 and have least QNR
   r(n) ∈ {11, 11, 13, 13, 17, 37}; among the 46 U_cop failures with 3 ∣ n and gcd(n, 35) = 1, P(r ≥ 11) = 0.80 against a
   baseline 0.25 for that class. Near-squareness is only weakly enriched (median relative distance 0.227 vs 0.250).
   Assessment: the data are consistent with a loaded lottery (fewer tickets, worse odds) and do not single out a
   near-square or Linnik/Dickson-shadow mechanism; this is a correlation, not an exclusion.
5. **No mechanism from the QNR witness (§4).** U's definition contains no character; Theorem E′ makes the character a
   consequence at every witness. What remains is the shadow condition n mod A ∈ S_A = {−v : v ∣ A+1, v ∈ V}; the n
   witnessed by moduli with a given odd part A′ have natural density ≪ A′^{ε−1} (≪ A′^{ε−1+o(1)} relative to the QNR
   population). This does not prove that QNR information is useless for *finding* a witness; it
   says that no attachment implication is available from it here, and that the fixed-modulus converse of E′ is false.
   Forest moves (Vieta, Ptolemy, full remainder tree) are cited dead.
6. **Global identities (§5).** The HJ dictionary, BHK, Rademacher and Σ_{a<p/4}(a/p) = h(−4p)/2 are verified. The colour
   is digit-local (DK Cor 4.1); cylinder (initial-digit) conditions are intervals of q, so every cylinder-weighted identity
   is an interval character sum (Prop 5.3), e.g. QNRs outnumber QRs by h(−4p)/2 among q with first digit 3 or 4; the
   length-3 part of any finitely-supported cylinder weight is a fixed finite root set (Thm 5.4), whose bichromatic part
   vanishes infinitely often CONDITIONAL on Dickson (LTA Thm 3.2). This is a corollary of the fixed-root theorem, not a
   new obstruction, and it says nothing about the signed (monochromatic) short-word mass.
7. **Barrier (§6).** The only barrier-type results *proved* here are Theorem 2.6 (every polynomial identity in free
   factors has one of two constant-coordinate shapes) and Props 4.2–4.3 (no fixed-modulus converse). The statement "any
   factorisation-driven mechanism must go through the lifted lines", which an earlier draft announced, is **false** (the
   review's coprime family a(2a+3)); it is withdrawn.

## 1. Setting

n ≡ 1 (mod 4) odd. A *word* of n is (t, u, v) ∈ ℕ³ with n = tuv − u − v; numerators A := tu − 1 = (n+u)/v,
A* := tv − 1 = (n+v)/u, AA* = tn + 1. Words with u = 1, t = 1, or u = v are allowed. (For prime p these are the edges of
F_p, including the loop at vertex 1; for composite n the diagonal words (t, u, u) are loops not present in the loop-free
forest of FC/FDA — at n = 1545 the vertex 15 carries the word (7, 15, 15) and no other. Throughout, "v is word-incident"
means "v is an endpoint of some word"; this coincides with forest non-isolation except at loops.) Put c := −n mod 8 ∈
{7, 3} and V = V(n) := {v ≥ 1 : 4 ∣ v or v ≡ c (mod 8)}. **U(n)** := some word of n has an endpoint in V. Vertex form
(FDF Cor C): v ∈ V is word-incident ⟺ n + v has a divisor A ≡ −1 (mod v); then u = (n+v)/A, t = (A+1)/v, and the word
carries an explicit 4/n identity (`z49_forestinv_words.py` checks it with exact fractions for every witness it prints).
**U_cop(n)** := some such witness has v ⊥ n (⟺ gcd(u, v) = 1, Lemma 2.3).

**Lemma 1.1 (n ≡ 5 (mod 8) is trivial; PROVED).** If n ≡ 5 (mod 8) then (1, (n+3)/2, 3) is a word with endpoint 3 ∈ V and
4/n = 1/(2d) + 1/(nd) + 1/(2nd), d = (n+3)/8. (Mordell's class; CERTIFIED to 4000, `verify.py` (6).) Odd squares are ≡ 1
(mod 8), so the inverse problem is about **n ≡ 1 (mod 8), V = 4ℤ ∪ (8ℤ + 7)**.

**Prior results used (audit).** The level factorisation (tu−1)(tv−1) = tn + 1 and its divisor reconstruction:
INVOLUTION_ES (introduction), BRAINSTORM/z45_interlacing_stable §1.1, FRONTIER §2.3. The scaling map K(av′, t, au′) =
a·K(v′, at, u′) with its sign transfer: DK §8.3. Factor-endpoint and diagonal words of composites: DK §9.2. The
digit/Jacobi congruence for all lengths: DK Cor 4.1. The shadow/colour split of the covering sets and the finite-modulus
non-coverage: FDF §3. Fixed finite root sets fail i.o. under Dickson: LTA Thm 3.2. Theorem E and Cor C: FDF §2.

## 2. Structure of U at composite n (PROVED)

**2.1 Theorem E′ (every U-witness is a coprime QNR modulus; PROVED).** Let n ≡ 1 (mod 4), v ∈ V(n), A ≥ 1, A ∣ n + v,
A ≡ −1 (mod v). Then gcd(A, n) = 1, A ≠ 1, and A = 2 occurs only for v = 3, n ≡ 5 (mod 8). In all cases the Jacobi symbol
(A/n) = −1. In particular U(n) ⟹ n is not a square (Theorem E), and when n ≡ 1 (mod 8) also (n/A_odd) = −1.
*Proof.* A ≡ −1 (mod v) gives gcd(A, v) = 1; a prime dividing A and n divides (n + v) − n = v, so gcd(A, n) = 1. A = 1
forces v ∣ 2 and A = 2 forces v ∣ 3; of 1, 2, 3 only v = 3 ∈ V(n), for n ≡ 5 (mod 8), and there (2/n) = −1. Now let
A = 2^a A′ with A′ odd. Since n ≡ −v (mod A′), (n/A′) = (−v/A′). *Case v ≡ 7 (mod 8)* (n ≡ 1 (mod 8)): A′ ≡ −2^{−a}
(mod v), and FDF Theorem E's computation gives (−v/A′) = (A′/v) = (−1/v)(2/v)^{−a} = −1 (so A′ > 1), and (A/n) =
(2/n)^a (A′/n) = (n/A′) = −1 by reciprocity, n ≡ 1 (mod 4). *Case v ≡ 3 (mod 8)* (n ≡ 5 (mod 8)): v ≡ 3 (mod 4), so
(−v/A′) = (A′/v) = (−2^{−a}/v) = (−1/v)(2/v)^a = −(−1)^a, while (2/n)^a = (−1)^a; hence (A/n) = (−1)^a·(−(−1)^a) = −1,
including A′ = 1 (then 2^a ≡ −1 (mod v) forces a odd; e.g. n = 5, v = 3, A = 8, word (3, 1, 3)). *Case 4 ∣ v*, v = 2^b w, b ≥ 2, w odd: A is odd, A ≡ 3 (mod 4), and FDF's computation
gives (−v/A) = −(2/A)^b = −1 (b = 2: square; b ≥ 3: A ≡ 7 (mod 8)), whence (A/n) = (n/A) = (−v/A) = −1, in both
classes of n mod 8. ∎
CERTIFIED (`verify.py`): (5b) all 6 187 witnesses at n ≡ 1 (mod 4), n ≤ 2000 have gcd(A, n) = 1 and Jacobi (A/n) = −1;
(5) all 5 602 witnesses at n ≡ 1 (mod 8), n ≤ 4000 have gcd(A, n) = 1, A_odd > 1 and (n/A_odd) = −1; (5c) the witnesses
with A ≤ 2 at n ≡ 1 (mod 4), n ≤ 2000 are exactly {A = 2, v = 3, n ≡ 5 (8)}.
*Relation to prior work.* FDF Theorem E proves, for v ≡ 7 (mod 8) or 4 ∣ v and A ≡ −1 (mod v), that (−v/A′) = −1 and
that at n = m² this is contradictory (in the v ≡ 3 (mod 8) branch the symbol is −(−1)^a); it already establishes the
coprimality it needs. E′ only records the Jacobi value at arbitrary n ≡ 1
(mod 4), including the n ≡ 5 (mod 8) branch and the boundary. DK §9.1 states the n ≡ 1 (8) case for the length-2 line.

**2.2 Proposition (level form; PROVED; prior: INVOLUTION_ES, z45_interlacing_stable §1.1).** U(n) ⟺ ∃ t ≥ 1 and A ∣ tn + 1
with A ≡ −1 (mod t) and (A+1)/t ∈ V(n); the partner is u = (A*+1)/t, A* = (tn+1)/A ≡ −1 (mod t). *Proof.* (t, u, v) is a
word iff (tu−1)(tv−1) = tn + 1; conversely A ≡ −1 (mod t) and A ∣ tn+1 give A* ≡ −1 (mod t). ∎ CERTIFIED for n ≤ 1201
(`lemmas.py` L5). The data of the problem in this form are the integers tn + 1 and n mod 8t.

**2.3 Lemma (gcd-indexed decomposition; PROVED; prior: DK §8.3 gives the map).** For a word (t, u, v) of n let
g = gcd(u, v). Then g ∣ n and (gt, u/g, v/g) is a word of n/g with coprime endpoints; conversely every word (t′, u′, v′) of
n/g with g ∣ t′ and gcd(u′, v′) = 1 lifts to the word (t′/g, gu′, gv′) of n. Hence
  Words(n) = ⊔_{g ∣ n} { (t′/g, gu′, gv′) : (t′, u′, v′) ∈ Words_cop(n/g), g ∣ t′ },
and a V-endpoint gu′ is coprime to n iff g = 1 (gcd(u, n) = gcd(u, tuv − u − v) = gcd(u, v)).
*Proof.* n = tuv − u − v = g(tg·u′v′ − u′ − v′). ∎ CERTIFIED, n ≤ 1201 (`lemmas.py` L1).
So U(n) = U_cop(n) ∨ ⋁_{1<g∣n} [n/g has a coprime word at a level ≡ 0 (mod g) whose scaled endpoint lies in V].
Ordinary scaling of an arbitrary solution of 4/(n/g) is *not* a word of n (the "coordinate artefact" of
BRAINSTORM/apollonian_reciprocity §4 at 105); only words of n/g at levels divisible by g lift.

**2.4 Lemma (word-incidence of a vertex sharing a factor with n; PROVED).** Let g = gcd(v, n). Then v is word-incident
at n ⟺ n/g + v/g has a divisor ≡ −1 (mod v). *Proof.* A ∣ n + v = g(n/g + v/g) with gcd(A, g) = 1. ∎ CERTIFIED,
n ≤ 1201, all v ≤ n + 2 (`lemmas.py` L2). The vertex v/g at n/g needs a divisor of the same integer in the class −1
modulo the smaller modulus v/g; the condition at n implies it.

**2.5 Lemma (words with an endpoint dividing n; PROVED; prior: DK §9.2).** Let n = ab. The words of n with u = a are
exactly (t, a, a·s) with (ta − 1)·s = b + 1; (t, a, a) is a word iff a ∣ b + 2, and then ta − 1 = b + 1, tn + 1 = (b+1)².
*Proof.* v(ta − 1) = a(b + 1), gcd(ta − 1, a) = 1. ∎ CERTIFIED (`lemmas.py` L3, L4).
*Consequence (PROVED, trivial).* U(n) holds on {n = ab ≡ 1 (8) : a ≡ 7 (8), a ∣ b + 2}: then b ≡ 7 (mod 8), A = ta − 1 =
b + 1 ≡ 0 (mod 8), and with m = A/8, 8/n = 1/(ma) + 1/(maA) + 1/(nmA) (e.g. 329 = 7·47: 1/42 + 1/2016 + 1/94752).
For n ≡ 5 (mod 8) only 4 ∣ A is available. Also on {n = ab : (ta−1) ∣ b+1, 4 ∣ (b+1)/(ta−1)} and
{n = ab : (ta−1) ∣ b+1, a(b+1)/(ta−1) ≡ 7 (8)} (endpoint a·s ∈ V).

**2.6 Theorem (polynomial words in a free factorisation; PROVED; completes DK §9.2's coefficient comparison and
corrects its claim that "u, v constant" is impossible).** Let
T, U, V ∈ ℚ[a, b] be *nonzero* polynomials with T·U·V − U − V = ab identically. Then, up to swapping U and V, either
(i) U = c₁, V = c₂ are constants and T = (ab + c₁ + c₂)/(c₁c₂), or (ii) V = c and T = c′ are constants with cc′ ≠ 1 and
U = (ab + c)/(cc′ − 1).
*Proof.* Put d_X = deg X ≥ 0. Then d_T + d_U + d_V = deg(ab + U + V) ≤ max(2, d_U, d_V). If d_U, d_V ≤ 1 the right side is
exactly 2 (the ab term cannot cancel), so (d_U, d_V, d_T) ∈ {(0,0,2), (1,0,1), (0,1,1), (1,1,0)}. In (1,0,1): V = c ≠ 0 and
U ∣ ab + c, which is irreducible in ℚ[a,b] for c ≠ 0 (it is linear in a with coprime coefficients b and c), so no linear U
divides it; (0,1,1) is symmetric; in (1,1,0): T = c′ ≠ 0 and (c′U − 1)(c′V − 1) = c′ab + 1, irreducible for c′ ≠ 0, impossible
for linear factors. If max(d_U, d_V) ≥ 2, say d_U ≥ d_V and d_U ≥ 2: the right side has degree ≤ max(2, d_U) = d_U, so d_T + d_V ≤ 0, i.e. T = c′,
V = c constants, and U(cc′ − 1) = ab + c; cc′ = 1 would force ab + c = 0, so cc′ ≠ 1 and U = (ab + c)/(cc′ − 1), of degree 2
(this covers d_U ≥ 3 as well: the equation forces d_U = 2). ∎
*What it says and does not say.* The theorem allows rational and negative constants; positive words arise from
positive integer constants. With c₁, c₂ ∈ ℕ the words (i) have fixed endpoints (c₁, c₂) and exist iff c₁c₂ ∣ n + c₁ + c₂:
one congruence class of n, numerators varying with n (e.g. U = V = 1, T = n + 2, numerators n + 1, a word at every n that
never certifies). With c, c′ ∈ ℕ, cc′ > 1, the words (ii) have a fixed endpoint c and fixed level c′, partner
(n + c)/(cc′ − 1): one congruence class n ≡ −c (mod cc′ − 1), fixed numerator A = cc′ − 1 — the covering words of FDF
Prop 3.1. Whether such a word *certifies* is a separate condition on (c, c′) (e.g. c = 116, c′ = 10, partner 3, certifies at
3361 ≡ 1 (mod 840)); FRONTIER B1 says that no *finite* set of certifying congruence families covers all primes, not that a
congruence family avoids the square classes mod 840. The theorem is about polynomials in two free variables only:
rational functions (T = 1, U = a, V = a(b+1)/(a−1)), polynomial relations between the factors (b = 2a + 3), divisibility
loci ((a+1) ∣ (b−1)) and arithmetic procedures are outside its scope and *do* produce words (2.5, 2.8). It is a
classification of polynomial identities in a and b, nothing more.

**2.7 Proposition (coprime lines see n + v only; PROVED).** For v ⊥ n, v is word-incident iff −1 lies in the set of
sub-products of the multiset {ℓ mod v : ℓ ∣ n + v, with multiplicity}; and for a prime q ∣ n with q ∤ v, q ∤ n + v. ∎
(Lemma 2.4 with g = 1 and gcd(n + v, n) = gcd(v, n) = 1.) *Assessment of its weight:* small primes are the main suppliers
of divisors in the class −1 (mod v) (3 ≡ 3 (mod 4) serves v = 4; 3·5 ≡ 7 (mod 8) serves v = 8; 3 is a QNR mod 7 and 3·2 ≡ 6
serves v = 7, …); §3.3 measures the effect of removing them. No pointwise ordering of difficulty between primes and
composites follows from 2.7; the census (§3) is the only evidence for one.

**2.8 Proposition (a relation family with coprime words; PROVED, trivial).** Let n = ab with a ≡ 5 (mod 8) and
b = k(a+1) + 1. Then (1, a + 2, ak + 2) is a word of n; n ≡ 1 (mod 8) iff k ≡ 2 (mod 4), and then the endpoint a + 2 ≡ 7
(mod 8) lies in V(n), so U(n) holds; for k = 2 the endpoints are coprime (the review's family a(2a+3): 65, 377, 945, 1769,
2849, …). The same word (1, a + 2, (n+1)/(a+1) + 1) exists for every n with (a + 1) ∣ (n + 1), whether or not a ∣ n; for
n ≡ 1 (mod 8) it is an instance of the t = 1 line "n + 1 has a divisor ≡ 6 (mod 8)", which holds iff (n+1)/2 has a prime
factor ≡ 3 (mod 4) (elementary: n + 1 = 2m with m ≡ 1 (4), and 2d ≡ 6 (8) for d ∣ m iff d ≡ 3 (4); cf. FDF Lemma 2.3 for
primes ≡ 1 (24)). *Proof.* (a+2)v − (a+2) − v = (a+1)v − (a+2) with v = (n+1)/(a+1) + 1 equals n. ∎ CERTIFIED
(`lemmas.py` L6). *Reading (Assessment).* Here the relation between the factors produces the word by making n + 1
reducible with the factor a + 1 ≡ 6 (mod 8); the word is then expressible through that divisor of n + 1 alone. This
does not show that factor information is immaterial for finding or forcing such a divisor in general, and 2.6 does not
exclude relation families of other shapes; I found none that is not of this "algebraic divisor of n + v" type.

## 3. Census (CERTIFIED computations; interpretations labelled)

**3.1 All 9 ≤ n ≡ 1 (mod 8) ≤ 10⁸** (`z49_forestinv_census.c`, 40 s, 0.5 GB; the three nested loops over
u ≥ 1, t ≥ 1, v ≥ 1 enumerate every word with n ≤ N — every endpoint is ≤ n + 2 and A = tu − 1 ≤ N + u — and record per n
whether a V-endpoint word with gcd(u, v) = 1 exists, whether one with gcd(u, v) > 1 exists, and the least coprime V-endpoint;
`census_1e8_summary.txt`, `ucop_failures_1e8.txt`). The reviewer re-ran the program to 10⁷ and matched the failure list.
The parent's `z49_main_ucensus.c` uses the same loops without the gcd split, so the six failures are reproduced but not by
an independent algorithm; `z49_forestinv_single.c` (enumeration by the smaller endpoint and trial-division factoring)
is the independent check at the listed n.

| class (n ≡ 1 (8), n ≤ 10⁸) | count | U fails | U_cop fails | U only via lifted words |
|---|---:|---:|---:|---:|
| primes | 1 439 970 | 0 | 0 | 0 |
| odd squares | 4 999 | 4 999 | 4 999 | 0 |
| composite non-squares, gcd(n, 105) = 1 | 4 272 030 | 0 | 0 | 0 |
| composite non-square, 7 ∣ n only | 952 000 | 0 | 0 | 0 |
| composite non-square, 5 ∣ n only | 1 428 000 | 1 (3985) | 5 | 4 |
| composite non-square, 3 ∣ n only | 2 856 000 | 1 (111969) | 46 | 45 |
| composite non-square, 5·7 ∣ n, 3 ∤ n | 238 000 | 1 (978145) | 4 | 3 |
| composite non-square, 3·5 ∣ n, 7 ∤ n | 714 000 | 0 | 94 | 94 |
| composite non-square, 3·7 ∣ n, 5 ∤ n | 476 000 | 1 (2961) | 90 | 89 |
| composite non-square, 105 ∣ n | 119 000 | 2 (105, 25305) | 197 | 195 |

Primes: this extends FDF §4.2's "the union never fails" from p ≡ 1 (24) to all p ≡ 1 (8) ≤ 10⁸; the least V-line is ≤ 116
(at 3361) over all of them.

**Least coprime V-line, by bit length** (`census_1e8_summary.txt`; columns 3 … 9 = line in [2^{k−1}, 2^k), then ≥ 2⁹, none):

| class | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ≥ 2⁹ | none |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| primes | 1 360 631 | 68 506 | 10 188 | 626 | 19 | 0 | 0 | 0 | 0 |
| composites ⊥ 105 | 4 026 909 | 210 039 | 32 610 | 2 322 | 136 | 13 | 1 | 0 | 0 |
| 3 ∣ n only | 2 530 026 | 112 108 | 189 800 | 16 281 | 6 249 | 1 070 | 264 | 156 | 46 |
| 105 ∣ n | 56 232 | 18 149 | 30 757 | 5 839 | 4 715 | 1 639 | 707 | 765 | 197 |

EVIDENCE: the bulk distributions of primes and of composites coprime to 105 are numerically close but not identical
(first-bin frequencies 0.9449 vs 0.9426, a difference far outside binomial noise; the composite tail is slightly heavier,
reaching bit length 9). The classes with small factors have a much heavier tail: for 105 ∣ n, 765 integers have their least
coprime line ≥ 2⁹ and 197 have none; the two counts are comparable, so a long failing initial segment does not typically
mean total failure.

**3.2 The hardest class beyond 10⁹** (`z49_forestinv_single.c -scan`, 4 min): all non-square n ≡ 1 (mod 8) with 105 ∣ n in
[10⁹, 10¹⁰] — 10 713 960 integers (325 squares skipped; least QNR automatically ≥ 11): U_cop fails 119 times
(`scan_105_1e9_1e10.txt`), U never. The rescuing lifted line is v = 7 for 89 of them, v = 12 for 23, v = 15 for 4, and
20, 24, 36 once each. The U_cop failure rate falls from 1.7·10⁻³ (105 ∣ n, ≤ 10⁸) to 1.1·10⁻⁵ (10⁹–10¹⁰).
CONJECTURE (inverse theorem, U-form; DK SQ₅ is the ES₅-form): U(n) for every non-square n ≡ 1 (mod 8), n > 978145.
EVIDENCE: the parent's census to 10⁹ and this scan of the hardest class to 10¹⁰.

**3.3 Per-line fire rates by residue class** (`z49_forestinv_firerate.py`, `firerate.txt`; the first 400 integers of each
population at or above 10⁶ in the stated class; lines v ∈ V, 4 ≤ v ≤ 200, v ⊥ n; "fires" = v is word-incident):

| population | v ≡ 0 (3) | v ≡ 1 (3) | v ≡ 2 (3) | P(some line ≤ 200 fires) |
|---|---:|---:|---:|---:|
| p ≡ 1 (24) prime | 0.170 | 0.156 | 0.261 | 1.000 |
| p ≡ 17 (24) prime | 0.203 | 0.317 | 0.141 | 1.000 |
| n ≡ 1 (24) composite ⊥ 35 | 0.167 | 0.144 | 0.253 | 0.993 |
| n ≡ 17 (24) composite ⊥ 35 | 0.202 | 0.311 | 0.136 | 1.000 |
| n ≡ 9 (24) (3 ∣ n), ⊥ 35 | — | 0.145 | 0.135 | 0.995 |
| n ≡ 1 (24), 5 ∣ n, 7 ∤ n | 0.126 | 0.140 | 0.213 | 0.998 |
| 105 ∣ n | — | 0.098 | 0.100 | 0.953 |

CERTIFIED numbers (samples of 400; the quoted rates are means over ≈ 7 000–10 000 lines each); EVIDENCE for the reading:
the fire rate of a line varies with n mod 24 and with the small primes dividing n, with primes and composites in the
same class differing by at most ≈ 0.012 in these samples; lines with 3 ∣ n + v (v ≡ −n (mod 3)) fire at 0.26–0.32, the others at 0.14–0.20; for 3 ∣ n the
lines v ≡ 0 (3) are not coprime and no remaining line gets the prime 3, and all fire at ≈ 0.14; with 105 ∣ n all fire at
≈ 0.10 and 4.7 % of such n have no coprime line ≤ 200. Assessment (a model, untested beyond these samples): a composite
with small factors behaves on its coprime lines like a prime in the Mordell-hard class with the small-prime "class
adjusters" removed from every shifted integer. Nothing in this section is a theorem about any individual n.

**3.4 The six sporadic failures** (`z49_forestinv_sporadic.py`, `sporadic.txt`, `controls.txt`):

| n | factorisation | r(n) | nearest square | n mod 24 |
|---:|---|---:|---|---:|
| 105 | 3·5·7 | 11 | 10² + 5 | 9 |
| 2961 | 3²·7·47 | 11 | 54² + 45 | 9 |
| 3985 | 5·797 | 13 | 63² + 16 | 1 |
| 25305 | 3·5·7·241 | 13 | 159² + 24 | 9 |
| 111969 | 3³·11·13·29 | 17 | 335² − 256 | 9 |
| 978145 | 5·7·27947 | 37 | 989² + 24 | 1 |

(r(n) = least prime ℓ ∤ n with Jacobi (n/ℓ) = −1.) EVIDENCE: (i) all six, and all 436 U_cop failures ≤ 10⁸, are divisible by
3 or 5 (427 by 3, 300 by 5, 291 by 7, none coprime to 105); (ii) the least QNR is enriched: among the 46 U_cop failures with
3 ∣ n and gcd(n, 35) = 1, P(r ≥ 11) = 0.80 and P(r ≥ 13) = 0.48, against 0.249 and 0.135 for composite non-squares ≡ 9
(mod 24) coprime to 35 near 10⁶ (13 690 values; without the coprimality conditioning the reference is 12/35); (iii) near-
squareness is weakly enriched at most: median relative distance δ = 0.227 (uniform reference 0.250), P(δ < 0.05) = 0.119
(reference 0.100). Both (i) and (ii) are expected to lower per-line fire rates (§3.3 for (i); for (ii), a line v = 4 needs a prime factor
≡ 3 (mod 4) of n + 4, and such a factor is a QNR, hence ≥ r(n)). Assessment: the data are consistent with a loaded lottery and do not
single out a near-square or Linnik/Dickson-shadow mechanism; a shadow in the sense of FDA Thm 6.1 blocks a fixed finite
set of lines, whereas here every line is blocked, which no construction in the campaign produces. This is an
interpretation, not an exclusion theorem.

**3.5 Controls.** Odd squares: U and U_cop fail at all 4 999 odd squares 9 ≤ m² ≤ 10⁸ (Theorem E; the census prints a
`SQUARE-VIOLATION` line otherwise, and never did) and at 9, 25, …, 225 by the single-n tool. Numerator 8: at n = 17 and 241
no word has an endpoint ≡ 0 (mod 8) (`lemmas.py`), as Lean L9901 requires; the only 8/n statement made (2.5) needs a
divisor a ≡ 7 (mod 8) of n ≡ 1 (mod 8), a > 1, and never applies to a prime. Hard primes (`controls.txt`): U holds with
least V-line 7, 4, 4, 87, 116, 7, 56, 55, 8 at 193, 409, 577, 2521, 3361, 5569, 9601, 66529, 8813281. No statement about
primes is derived from composite-only facts anywhere in this document.

## 4. The non-squareness witness: no converse mechanism found

**4.1 Proposition (PROVED).** Let n ≡ 1 (mod 8). (a) Every word at a vertex v ∈ V has a slot divisible by 4, whatever
the colours: 4 ∣ v is a slot, and for v ≡ 7 (mod 8), n + v ≡ 0 (mod 8) = (tv−1)·u forces 4 ∣ tv − 1 or 4 ∣ u (FDF Thm B /
Cor C, whose slot algebra does not use primality). (b) Every U-witness numerator A satisfies (A/n) = −1 (Theorem E′). ∎
*Reading (Assessment).* U is defined without the character, and the character is forced at every witness. So a
hypothesis that supplies QNRs (GRH, OAI-003) supplies no *attachment* statement here; what it could still do — guide a
search for A among the QNR moduli — is a heuristic, and Props 4.2–4.3 measure how little of the QNR coset any one modulus
covers. This is weaker than "QNR information is unusable": no such impossibility is proved.

**4.2 Proposition (what a single modulus witnesses; PROVED).** Throughout 4.2–4.3, n ≡ 1 (mod 8) and
V = 4ℤ ∪ (8ℤ+7). Let A = 2^a A′ with A′ odd, not a square, and put
S_A := {−v mod A : v ∣ A + 1, v ∈ V}. Then (a) A is a U-witness for n iff n mod A ∈ S_A (v ≤ A + 1 and v ≡ −n (mod A)
determine v; the only possible collision in [1, A+1] is {1, A+1}, and 1 ∉ V); (b) S_A lies in the QNR coset
{r : (r/A′) = −1} (Theorem E′); (c) |S_A| ≤ τ(A+1) − 1; and the set {n : some A with odd part A′ witnesses n} has a natural density, which is
≪_ε A′^{ε−1} for every 0 < ε < 1 (relative to the population n ≡ 1 (mod 8), (n/A′) = −1, of density φ(A′)/(16A′), this
is ≪ A′^{ε−1+o(1)}).
*Proof of (c).* A witness at n ≤ X has A ≤ 2X + 1 (t = 1 gives A = v − 1 ≤ n + 1; t ≥ 2 gives v ≤ (A+1)/2 and
A ≤ n + v). So the count of witnessed n ≤ X is at most Σ_{a : 2^a A′ ≤ 2X+1} (τ(2^a A′ + 1) − 1)·(X/(2^a A′) + 1) ≤
X·Σ_a τ(2^a A′ + 1)/(2^a A′) + O(X^ε); with τ(m) ≪_ε m^ε the sum is ≪ A′^{ε−1} Σ_a 2^{a(ε−1)} ≪ A′^{ε−1}. This is an
upper-density bound; the density exists because the union over a ≤ K is periodic and the tail a > K has upper density
≤ Σ_{a>K} τ(2^a A′ + 1)/(2^a A′) → 0 as K → ∞. ∎
*Heuristic (Assessment, cf. FDF §5 M7).* A prime line ℓ ≡ 7 (mod 8) is witnessed with model probability ≍ (log ℓ)/ℓ, and
Σ_{ℓ ≤ X prime} (log ℓ)/ℓ ≍ log X: the family of QNR prime lines has ≍ log X expected hits, like any family of prime lines,
and far fewer than the ≍ log² X of all lines; the QNR property adds nothing to the count.

**4.3 Proposition (no converse of E′ at a fixed modulus; PROVED).** Let A ≥ 17 be odd and not a square. Then some class
r (mod A) with (r/A) = −1 is witnessed by A for no n ≡ r (mod A); by CRT it contains infinitely many n ≡ 1 (mod 8), all QNRs
mod A. *Proof.* The QNR classes mod A number φ(A)/2 ((·/A) is non-principal), the witnessed ones ≤ τ(A+1) − 1, and
τ(A+1) < φ(A)/2 for all A ≥ 3 except A ∈ {3, …, 12, 14, 15, 20}: CERTIFIED for A ≤ 10⁵ (`verify.py` (7)); for A > 10⁵,
τ(m) ≤ 2√m and φ(A) ≥ A/(e^γ log log A + 3/log log A) (Rosser–Schoenfeld) give 2√(A+1) < φ(A)/2. ∎
*Scope.* This refutes "convert a QNR witness into a U-witness at the same modulus". It says nothing about a modulus chosen
depending on n, nor about the union over all a of the shadows of 2^a A′.

**4.4 Forest and tree moves (Assessment, citing PROVED results).** Vieta involutions on the Fricke cubic preserve (v, t, u)
and the ES status of the word (BRAINSTORM/bsA_fricke_vieta F2); Ptolemy relations are the five relations inside one
pentagon and encode its 2-adic depth (y5_transport_is_ptolemy Lemma 1); the full remainder tree keeps at most two arrows
per quotient block (FDA Prop 4.2), its least-QNR block is deleted on an infinite progression (FDA Prop 4.3), and its first
split fibre fails i.o. under Dickson (FDA Thm 5.3). Astra's (10.1), "a virtual cut survives pruning", remains the statement
to be proved. H4_NOT_POLYLOG (PROVED on main, relative to its energy lemma): infinitely many primes p ≡ 1 (mod 840) have
no edge with larger endpoint in (3, exp((log p)^κ)] for every fixed κ < 1/12 (κ < 1/6 with (G) or GRH); this constrains
certificates with *both* endpoints small — in particular U-witnesses with both v and the cofactor u = (p+v)/A below
exp((log p)^κ) fail i.o. — and does not constrain the least V-line alone; nothing here does either.

## 5. Global identities over all q

**5.1 Dictionary (CERTIFIED, `verify.py` (1)–(4)).** For p prime: the interior words (t, u, v ≥ 2) of p correspond
bijectively to the q ∈ [1, p−1] whose negative (HJ) expansion p/q = [[b₁, b₂, b₃]] has length exactly 3, via
q = tv − 1 and (b₁, b₂, b₃) = (u, t, v) (first digit ⌈p/q⌉ = u because p/q = u − v/(tv−1) with 0 < v/(tv−1) < 1 for
t, v ≥ 2); the q of length ≤ 2 are exactly the divisors of p + 1 (words with u = 1 or t = 1 after reduction; q = 1 is
length 1). 37 primes p ≡ 1 (4) below 400, no mismatch, first digits agree. BHK: 12 s(q,p) = Σ(b_i − 3) + (q + q*)/p
(2 960 pairs); Rademacher: 12 p s(q,p) ≡ p + 1 − 2(q/p) (mod 8); Σ_{0<a<p/4}(a/p) = h(−4p)/2 with h(−4p) by counting
reduced forms (37 primes); Σ_{p/4<q<p/2}(q/p) = −h(−4p)/2 and Σ_{p/2<q<p}(q/p) = 0 (`verify.py` (8)).

**5.2 Proposition (digit-locality; PROVED; prior: DK Cor 4.1).** For odd n, q ↦ (b₁, …, b_k) is a bijection from
{q ∈ [1, n−1] : gcd(q, n) = 1} onto the sequences of integers ≥ 2 with negative continuant n; q, q* are the continuants of
(b₂, …, b_k), (b₁, …, b_{k−1}), and 2(q/n) ≡ n + 1 − nΣ(b_i − 3) − q − q* (mod 8) (DK Cor 4.1). So any "identity over all
q" Σ_q F(q, q*, digits) = G(n) is Σ_{K(b)=n} F(b) = G(n), a statement about the word-generating function; for F supported on
length 3 it is the colour-twisted word series of FRONTIER §2.3 (Thm K). ∎

**5.3 Proposition (cylinders are intervals; PROVED).** Fix digits β = (β₁, …, β_j). The q whose expansion of p/q begins with
β form the set {q : p/q ∈ J(β)} for an interval J(β) ⊂ ℝ with rational endpoints independent of p (a cylinder of the
negative-CF Gauss map), i.e. an interval of q with endpoints in p·ℚ. Hence for any j ≥ 1 and any weight w on digit patterns of length
j supported on a *fixed finite set* of patterns (with w(q) := 0 when the expansion of p/q has fewer than j digits),
Σ_q w(q)(q/p) is a finite combination of interval character sums
Σ_{q ∈ I} (q/p), I ⊂ (0, p) with endpoints in p·ℚ (explicitly, the cylinder of a prefix with HJ convergents P_j/Q_j,
P_{j−1}/Q_{j−1} is q/p ∈ [Q_j/P_j, (Q_j − Q_{j−1})/(P_j − P_{j−1})), cross-reviewer's formula). Example: first digit 3 or 4 ⟺ p/4 < q < p/2, and Σ_{p/4<q<p/2} (q/p) = −h(−4p)/2, first digit 2 contributes 0
(p ≡ 1 (mod 4)). ∎ So **QNRs outnumber QRs by h(−4p)/2 among the q with first digit 3 or 4**, and h(−4p) = p^{1/2+o(1)}
(Siegel). The first digit is the endpoint u of the word (when the length is 3), not necessarily the smaller one; the
length-3 q in (p/4, p/2) number at most τ(p+3) + τ(p+4) = p^{o(1)}, so for large p the excess is carried by expansions of
length ≥ 4.

**5.4 Theorem (cylinder-type identities and length 3).** Let j ≥ 1, let w be a weight on HJ digit patterns of length j,
supported on a fixed finite set of patterns independent of p, extended by w(q) := 0 when p/q has fewer than j digits, and
let W_sgn(p) := Σ_q w(q)(q/p) and W₃(p) its restriction to q of length ≤ 3.
(a) (PROVED) W_sgn(p) is a finite combination of interval character sums over intervals with endpoints in p·ℚ, as in 5.3.
(b) (PROVED) W₃(p) is a weighted signed count of interior words of p with endpoint u = b₁ in a fixed finite set (j = 1),
with (u, t) in a fixed finite set (j = 2), or of finitely many fixed words (j ≥ 3), plus boundary words with fixed divisor of
p + 1.
(c) (CONDITIONAL on Dickson; LTA Thm 3.2) For every finite set of vertices there are infinitely many primes p ≡ 1 (24) at
which every component meeting the set is monochromatic; at those primes every word in (b) is monochromatic, so the
bichromatic part of W₃ vanishes. Hence no identity in this class forces a non-zero bichromatic short-word count at every
prime. (The monochromatic short words can still carry signed mass: at p = 12721, with w(2) = 2, w(3) = −1, one has
W₃ = 5 while the bichromatic part is 0 — reviewer's example. For the specific two-cylinder excess of 5.3 the long
expansions carry −h(−4p)/2 + O(τ(p+1) + τ(p+3) + τ(p+4)), hence essentially all of it, unconditionally.)
*Proof.* (a) is 5.3. (b) is the dictionary 5.1 (interior words have b₁ = u; depth-2 cylinders fix (u, t), depth-3 fix the
word and hence p). (c) is the cited theorem. ∎ This is a corollary of the fixed-root theorem, recorded because the brief
asked for the barrier in theorem form; it does not bar identities whose weights have p-dependent support (e.g. w ≡ 1),
which are not cylinder-type in this sense, nor does it say anything about non-linear identities.

**5.5 Other inputs (Assessment).** Zolotarev's lemma gives (q/p) as the inversion number of x ↦ qx, which Meyer's formula
ties to 3p·s(q,p) — digit-local again. Σ_v χ(v) = 0 regrouped by components is FDA (8.1), with no positive term.
Σ_q s(q,p) = 0 and the second moment of Dedekind sums do not separate length. No candidate in this class is left; the
finite-dictionary certification of (I)5 is its computational shadow.

## 6. What is proved, what is not, and the gap

**Proved here (all narrow).** Theorem E′; Lemmas 2.3–2.5 (decomposition, non-coprime incidence, factor-endpoint words);
Theorem 2.6 (classification of polynomial identities in free factors); Props 2.7–2.8; Props 4.2–4.3 (fixed-modulus counting); Props 5.2–5.3 and
Theorem 5.4(a),(b); Theorem 5.4(c) CONDITIONAL on Dickson. Of these, 2.3, 2.5, 5.2 are bookkeeping refinements of DK §§8.3,
9.2, Cor 4.1, and 5.4(c) is a corollary of LTA Thm 3.2.

**Not proved.** The inverse theorem for any natural infinite class of composites (ω(n) ≥ k; q^{odd} ∥ n; n with a
factor ≡ 3 (mod 4) as in DK §9.2 — all reduce to a divisor of n/g + v/g in a tied class, or to the coprime lottery);
any mechanism from a QNR witness; any identity with a positive length-3 term; any barrier beyond 2.6 and 4.3. The claim
of an earlier draft that every factorisation-driven mechanism must pass through the lifted lines is withdrawn (2.8).

**Where a factorisation is needed and whether a prime is harder (Assessment on PROVED bookkeeping).** The gcd
decomposition (2.3) locates the non-coprime words as lifted words of divisors of n, which are B2 events for a divisor of
n with an enlarged modulus (2.4); coprime incidence has the shifted-divisor description (2.7); the character is forced at
every witness (E′). Neither description restricts what information may be used to force an incidence (2.8 is a case in
point). The census (§3) finds composites coprime to 105 behaving like primes and composites with small factors behaving
worse. So nothing in this document suggests that primes are the hard case *because* they are prime; they are the case
with no lifted lines and no small-factor handicap.

**Exact remaining gap, for the U-route.** For a prime p ≡ 1 (mod 8): some v ∈ 4ℤ ∪ (8ℤ+7) such that p + v has a divisor
≡ −1 (mod v), **at any scale** — and necessarily so: by H4_NOT_POLYLOG (main), for every fixed κ < 1/12 infinitely many
primes p ≡ 1 (mod 840) have no edge with larger endpoint in (3, exp((log p)^κ)], so at those primes every U-witness has
max(v, (p+v)/A) > exp((log p)^κ); the version of this gap with both v and the cofactor polylog (FDF §6) is false. U is a
*sufficient* sub-family of ES₅ (FDF §6 calls it the sign-free sufficient form); the
unrestricted target, a bichromatic edge of F_p at any scale (FDA (10.1)), is weaker and is not reduced to U here. For a
non-square composite n the gap is the same statement on the coprime lines plus "n/g + v/g has a divisor ≡ −1 (mod v)" on
the lines with gcd(v, n) = g > 1. The composite data (§3.2: 0 failures of U in the hardest class to 10¹⁰) support the
U-form inverse conjecture at composites and say nothing about primes beyond FDF §4.

## 7. Screening checklist (FRONTIER §4) for the positive statements made (2.5, 2.8, E′)

| line | status |
|---:|---|
| 1 | PASS: E′ is contradictory at squares; 2.5/2.8 need a divisor ≡ 7 (8) of n or a class condition on a divisor of n + v, never met at n = m² (Theorem E). |
| 2 | PASS: at 17, 241 no word has an endpoint ≡ 0 (8); the 8/n family of 2.5 needs a ≡ 7 (8), 1 < a ∣ n. |
| 3 | PASS: no numerator-uniform law. |
| 4 | FAIL for the inverse theorem: the tied-modulus divisor event of one integer, 2.4/2.7. |
| 5 | PASS: every statement is at fixed n; §3.3 rates are labelled EVIDENCE. |
| 6–7 | N.A. |
| 8 | 2.5/2.8 are word families (B1-type) and are labelled so; 2.6 classifies the polynomial identities in free factors (two constant-coordinate shapes). |
| 9 | The class layer is the whole problem; the character layer is forced at witnesses (E′). |
| 10–13 | N.A. |
| 14 | PASS (finite): all listed hard primes, §3.5. |
| 15 | Near-squares examined; weak enrichment only (§3.4). |
| 16–17 | N.A. / FAIL as for every covering route. |

## 8. Reproduction (≈ 10 min CPU, peak RSS 0.5 GB; `ulimit -v 8000000` throughout)

```sh
gcc -O2 -Wall -o /tmp/z49census scripts/z49_forestinv_census.c -lm
timeout 3000 /tmp/z49census 100000000 > data/z49_forestinv/ucop_failures_1e8.txt 2> data/z49_forestinv/census_1e8_summary.txt
gcc -O2 -Wall -o /tmp/z49single scripts/z49_forestinv_single.c -lm
timeout 7200 /tmp/z49single -scan 1000000000 10000000000 105 11 > data/z49_forestinv/scan_105_1e9_1e10.txt 2> data/z49_forestinv/scan_105_1e9_1e10.log
timeout 300 /tmp/z49single 193 409 577 2521 3361 5569 9601 66529 8813281 17 241 9 25 49 81 121 169 225 > data/z49_forestinv/controls.txt
timeout 1500 uv run python scripts/z49_forestinv_verify.py     # (1)–(8); exits non-zero on any failure
timeout 900 uv run python scripts/z49_forestinv_lemmas.py      # L1–L6 on all n ≡ 1 (8) ≤ 1201; numerator-8 control
timeout 900 uv run python scripts/z49_forestinv_firerate.py > data/z49_forestinv/firerate.txt
timeout 900 uv run python scripts/z49_forestinv_sporadic.py > data/z49_forestinv/sporadic.txt
uv run python scripts/z49_forestinv_words.py 105               # the U-words (none) of any n, with ES identities
```

## 9. Hostile reviews (deep mode, `reviews/z49-forestinv-review.md`, `reviews/z49-forestinv-review2.md`) and what they changed

The reviewer re-ran the 10⁷ census (exact match), the verifier, the hard primes and the sporadic list, and found no
computational defect; the defects were in the prose and in two theorems. Repairs made: (1) Theorem E′ boundary (A = 2 at
v = 3, n ≡ 5 (8)) and the withdrawn phrase "coprimality hypothesis removed"; (2)–(3) Theorem 2.6 restricted to nonzero
polynomials, proof completed, integrality and "reading" corrected (fixed endpoints vs fixed numerator; certification is
separate; B1 misquoted); (4) the "factorisation blindness" barrier and all its consequences withdrawn after the
counterexample a(2a+3), now Prop 2.8; (5) Prop 4.1(c) deleted, reading softened; (6) the (log X)²/16 heuristic corrected
to ≍ log X; (7) Prop 4.2(c) given hypotheses and the truncation argument; (8) the H₄-calibration paragraph corrected;
(9)–(13) §5 rewritten: signed sums vs QNR counts, finite support, LTA Thm 3.2 cited, interior-word dictionary with
boundary cases, dimension of the cylinder intervals; (14) prior-result audit added (INVOLUTION_ES, z45_interlacing_stable,
DK §§8.3, 9.2, Cor 4.1, FDF §3, LTA Thm 3.2); (15) n ≡ 1 (8) in the 8/n consequence; (16) "word-incident" vs
"non-isolated" (loops at composites); (17) non-square count in §3.2, parent census not independent; (18) "same" →
"close", "multiplicative" and the tail claim removed; (19) nearest squares of 105, 2961 corrected, δ defined and
scripted; (20) baseline 12/35 vs 1/4 conditioning; (21)–(22) "explained" demoted to EVIDENCE/Assessment, the deformed-T1
line-death parenthetical removed; (23) "only sense" removed, exception check scripted; (24) verifier aligned with the
prose and made to fail loudly; (25) the gap stated for the U-route with the unrestricted target separate; (26) §0 and §6
rewritten as an unsuccessful search with narrow results; (27) table bars escaped. Not changed: the census, the
hard-prime and square controls, Props 4.2–4.3, the fire-rate measurements.
**Second pass** (13 residual findings, 28–40): the "no identity in free factors" slogan replaced by "classification" in
§§0, 2.6, 6, 7 (28); the surviving exclusivity sentence in §6 and the "not a composite-specific mechanism" reading of 2.8
removed (29); 2.6's integrality/positivity restrictions and the certifying example (c, c′) = (116, 10) corrected (30);
the A′ = 1 parenthetical in E′ corrected (a odd, e.g. (3, 1, 3) at n = 5) and the FDF attribution delimited (31); n ≡ 1 (8)
put on both families in §0 and the certifying branch k ≡ 2 (4) stated in 2.8 (32); 4.2(c) stated as an existing natural
density with the truncation/tail argument and the relative normalisation (33); 5.4(c) restricted to the bichromatic
short-word count, with the reviewer's counterexample p = 12721 recorded (34); the convention w(q) = 0 for short expansions
(35); §0's QNR statistic attached to the conditioned 46-element population (36); "±0.01" → "≈ 0.012", "every" and
"not on primality" softened (37); the census domain stated as 9 ≤ n (38); `verify.py` (5) now rejects A_odd = 1 and its
docstring matches the interior dictionary (39); §0's cross-references corrected to Prop 5.3 / Thm 5.4 (40); 4.1(a) now
gives the slot algebra instead of citing a prime-only statement (reviewer's item 46).
**Cross-model review (Astra, `reviews/z49-forestinv-xreview.md` on main; verdict SOUND, four minors, independent census
engine to 10⁶ and boundary/sign checker to 4000 agreeing byte-for-byte; novelty grades 0–2/5 with Theorem 2.6 at 2/5).**
Minors applied: (1) 2.6 "completes and corrects" DK §9.2's constant-endpoint assertion; (2) `lemmas.py` now exits non-zero
on any L1–L6 failure or non-empty numerator-8 control, and `verify.py` (5c) tests equality with the expected singleton;
(3) the unused Bernoulli-number gloss in 5.3/5.4(a) replaced by the explicit cylinder interval; (4) n ≡ 1 (mod 8) stated
locally in 4.2–4.3 and "composite non-square" written in every §3.1 row. Also updated after H4_NOT_POLYLOG landed on main:
§4.4 and the gap statement in §6 now cite the proved super-polylog lower bound on both endpoints instead of the heuristic
calibration.
