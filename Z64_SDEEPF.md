# Z64_SDEEPF — tryhard lane on conjecture (S): length-3 words with Jacobi symbol −1

Lane: SDEEPF, wave z64. Fresh/unprimed (no FRONTIER, no Z5*/Z6*, no HJ_DEEP/DEDEKIND_ES/BRAINSTORM read).
Scripts: `scripts/z64_sdeepf_*`; data: `data/z64/sdeepf/`.

## §0 Statement and mandatory falsifiers

**(S).** n ≡ 1 (mod 4), n not a square. A *length-3 word* of n is A = tu − 1 with integers t, u, v ≥ 2,
tuv − u − v = n, gcd(A, n) = 1. Claim: if n has a word, it has one with Jacobi symbol (A/n) = −1.

Falsifiers to be answered at the end (§F):
* **F1** odd squares n = m²: every argument must break there; identify the step.
* **F2** sub-family arguments (fixed parity of t, u, v, A) must be screened on `data/z58/screens/r8_zeros_1e10.txt`
  and `star_prime_zeros.txt`.
* **F3** composites: say whether primality is used.
* **F4** the 14 primes of `star_prime_zeros.txt` and the 38 of `gstar_zeros.txt` satisfy (S) — verify.

Status key: PROVED / CONDITIONAL (on what) / CERTIFIED (computation) / EVIDENCE.

**Summary of results (no proof of (S); no HOT LEAD).**
* Thm 2.1 (PROVED; a REDISCOVERY in a new compact form — per cross-model review it is DEDEKIND_ES Thm 4.5/§8.1,
  cf. FOREST_DEEP_FABLE Thm A, FOREST_CONNECTIVITY Thm 2.1, LOWERTAIL_ROUND2_FABLE Thm 1, z1_legendre_levels
  Prop 1; only the one-product form is new): for a word (t,u,v) of n ≡ 1 (4), (A/n) = −1 ⇔ 8 | (n+t)(n+u+v).
  So (S) is a purely 2-adic statement about the solutions of n + u + v = tuv (verified on all 4.1·10⁹ words
  of n ≤ 10⁸).
* Thm 3.1 (PROVED): (S) for n ≡ 5 (8) [word (3,3,(n+3)/8)], n ≡ 2 (3) [((n+7)/12, 4, 3)], n ≡ 3 (9)
  [((n+15)/36, 3, 12)].
* Thm 3.6 (PROVED given Thm 2.1 + CERTIFIED): Mordell-type covering — (S) holds for all non-square n ≡ 1 (4)
  outside 28 explicit classes mod 840 (the 24 odd-square classes, which no finite covering can ever remove
  since each contains squares, Cor. 2.2; plus four classes with n ≡ 6 (7)); 57 explicit words, two
  covering checkers.
* Thm 4.1 (PROVED given Landau): counterexamples to (S) up to x number ≪ x/√log x; Thm 4.2 (given a
  textbook sieve bound): ≪_B x (log x)^{−B} for every B.
* §5: why the remaining classes are ES-hard (words are sparse "divisor-in-a-residue-class" objects; the
  only global input is the non-triviality of (·/n), which no finite covering or fixed-level family can use).

## §1 Setup and basic identities (PROVED)

Throughout n ≡ 1 (mod 4), t, u, v ≥ 2, n = tuv − u − v, A := tu − 1, B := tv − 1.

**Lemma 1.1.** (a) A·B = tn + 1. (b) n = vA − u, n = uB − v. (c) gcd(A, n) = gcd(B, n) = 1 automatically,
and (A/n) = (B/n). (d) A ≡ B ≡ −1 (mod t), A ≡ −1 (mod u), B ≡ −1 (mod v).
(e) If A is odd then (A/n) = (−t/A) = (−u/A).

*Proof.* (a) (tu−1)(tv−1) = t(tuv − u − v) + 1. (b) vA − u = tuv − v − u. (c) By (a) AB ≡ 1 (mod n), so
(AB/n) = 1 and neither factor shares a prime with n. (d) Immediate from the definitions and (a)
(AB ≡ 1 ≡ (−1)(−1) mod t). (e) Jacobi reciprocity with n ≡ 1 (mod 4) gives (A/n) = (n/A). From (a),
tn ≡ −1 (mod A), so n ≡ −t^{−1} ≡ −t·(t^{−1})² (mod A), whence (n/A) = (−t/A); and tu ≡ 1 (mod A) gives
t^{−1} ≡ u, so also (n/A) = (−u/A). ∎

Three equivalent parametrisations of the words of n (all PROVED by Lemma 1.1, inverse maps obvious):
* (W_t) a level t ≥ 2 and a factorisation tn + 1 = A·B with A ≡ B ≡ −1 (mod t), A, B ≥ 2t − 1;
* (W_u) a letter u ≥ 2 and a divisor A | n + u with A ≡ −1 (mod u), 2u − 1 ≤ A ≤ (n + u)/2;
* (W_A) a denominator A ≥ 3 such that r := (−n mod A) satisfies 2 ≤ r ≤ (A+1)/2, r | A + 1, and
  A ≤ (n + r)/2 (then u = r, t = (A+1)/r, v = (n+r)/A).
Continued-fraction reading (not needed later): n/A = v − 1/(t − 1/u), i.e. A is the denominator of a
Hirzebruch–Jung expansion of length exactly 3 of a fraction n/A; (W_A) says the words are exactly these A.

## §2 The Jacobi symbol of a word is 2-adically local (PROVED)

**Theorem 2.1 (local criterion; PROVED here independently — priority: this is in substance DEDEKIND_ES
Thm 4.5 ("(A/n) = −1 ⟺ 4 divides one of t, u, v, A, A*") and §8.1, with elementary proofs in
FOREST_DEEP_FABLE Thm A and FOREST_CONNECTIVITY Thm 2.1, the coordinate form in LOWERTAIL_ROUND2_FABLE Thm 1
and the t ≡ −n (8) piece in z1_legendre_levels Prop 1; the lane was unprimed and rediscovered it. New here:
only the one-product formulation 8 | (n+t)·tuv and its self-contained case proof.)** Let n ≡ 1 (mod 4) and
(t, u, v) a length-3 word of n, A = tu − 1. Then

  (A/n) = −1  ⇔  8 | (n + t)(n + u + v)  ⇔  8 | t·u·v·(n + t).

(The two right-hand sides agree because n + u + v = tuv.) In particular (A/n) depends only on
(t, u, v) mod 8, and the words with (A/n) = −1 ("good words") are exactly those in the classes

| t mod 4 | good iff |
|---|---|
| 0 | always |
| 2 | u ≡ 0 or v ≡ 0 (mod 4) (equivalently: u or v ≡ 0 or 3 mod 4, see proof) |
| 1 | u ≡ 0 or v ≡ 0 (mod 4) |
| 3 | u or v even; or u, v odd and tn ≡ 7 (mod 8) (⇔ 8 | n + t) |

*Proof.* Write C := (n + t)·t·u·v. Since n is odd, u + v ≡ tuv + 1 (mod 2); we split into cases.

**Case I: t even.** Then u + v is odd, so exactly one of u, v is even, and A, B are odd. By Lemma 1.1(e),
(A/n) = (−t/A). Write t = 2^k t' with t' odd, k ≥ 1. Then (−t/A) = (−1/A)(2/A)^k(t'/A). Since
A ≡ −1 (mod t'), reciprocity gives (t'/A) = (A/t')(−1)^{(A−1)(t'−1)/4} = (−1/t')(−1)^{(A−1)(t'−1)/4}
= (−1)^{((t'−1)/2)(1 + (A−1)/2)} = (−1)^{(t'−1)(A+1)/4}, and A + 1 = tu = 2^k t' u.
* k ≥ 3: A ≡ −1 (mod 8), so (2/A) = 1, (−1/A) = −1, (t'/A) = (−1)^{((t'−1)/2)·2^{k−1}t'u} = 1. Hence
  (A/n) = −1. Also 8 | t | C. ✓
* k = 2: A ≡ 3 (mod 4), (−1/A) = −1, (2/A)² = 1, (t'/A) = 1 (exponent ((t'−1)/2)·2t'u even). So
  (A/n) = −1. And C = (n+t)·4t'·uv with uv even, so 8 | C. ✓
* k = 1 (t ≡ 2 mod 4): (A−1)/2 = t'u − 1, A² − 1 = (A−1)(A+1) = 4t'u(t'u − 1), so (2/A) =
  (−1)^{t'u(t'u−1)/2}, and (t'/A) = (−1)^{((t'−1)/2)·t'u} = (−1)^{u(t'−1)/2}. Thus
  (A/n) = (−1)^E with E = (t'u − 1) + t'u(t'u − 1)/2 + u(t'−1)/2.
  – u ≡ 0 (4): E ≡ 1 + 0 + 0, so (A/n) = −1; and 4 | u, 2 | t give 8 | C. ✓
  – u ≡ 2 (4): t'u − 1 odd; t'u/2 odd so t'u(t'u−1)/2 odd; (u/2)(t'−1) even. E even, (A/n) = +1.
    Here v is odd, n + t odd, so v₂(C) = v₂(t) + v₂(u) = 2: 8 ∤ C. ✓
  – u odd (v even): E ≡ (t'u−1)/2 + (t'−1)/2 ≡ t'(u+1)/2 − 1 (mod 2). If u ≡ 1 (4), (u+1)/2 is odd and
    E is even: (A/n) = +1; if u ≡ 3 (4), E is odd: (A/n) = −1. On the other side, n ≡ 2t'uv − u − v ≡
    −u − v (mod 4) (as v is even, 2t'uv ≡ 0 mod 4), so u + v ≡ 3 (mod 4): u ≡ 1 ⇒ v ≡ 2 (4), v₂(C) = 2, 8 ∤ C;
    u ≡ 3 ⇒ v ≡ 0 (4), 8 | C. ✓
  This also shows the parenthetical equivalence in the table row t ≡ 2 (4).

**Case II: t odd, exactly one of u, v even.** By symmetry of the statement in u, v (Lemma 1.1(c):
(A/n) = (B/n)) we may assume u even, v odd; then A is odd and (A/n) = (−t/A) with A ≡ −1 (mod t).
Reciprocity: (−t/A) = (−1)^{(A−1)/2}(A/t)(−1)^{(A−1)(t−1)/4} = (−1)^{(A−1)/2 + (t−1)/2 + (A−1)(t−1)/4}
= (−1)^{(a+1)(b+1) − 1} with a = (A−1)/2, b = (t−1)/2, i.e. (A/n) = −(−1)^{(A+1)(t+1)/4} = −(−1)^{tu(t+1)/4}.
So (A/n) = −1 ⇔ 8 | tu(t+1) ⇔ 8 | u(t+1). Now C = (n+t)·tuv and t, v are odd, so 8 | C ⇔ 8 | u(n+t).
Since n ≡ 1 (mod 4), n + t ≡ t + 1 (mod 4), both even. If 4 | u both conditions hold; if u ≡ 2 (4) both
reduce to 4 | t + 1 ⇔ 4 | n + t. ✓

**Case III: t, u, v all odd.** Then n ≡ tuv − u − v (mod 4); if t ≡ 1 (4) this is uv − u − v =
(u−1)(v−1) − 1 ≡ −1 (mod 4), contradicting n ≡ 1 (4). So t ≡ 3 (mod 4), tn + 1 ≡ 0 (mod 4), and A, B are
both even. Write A = 2^j A', B = 2^l B' with A', B' odd, j, l ≥ 1, j + l = v₂(tn+1). Then
(A/n) = (2/n)^j (A'/n) = (2/n)^j (n/A') = (2/n)^j (−t/A') (as A' | tn + 1, cf. Lemma 1.1(e)). From
A ≡ −1 (mod t): A' ≡ −2^{−j} (mod t). With t ≡ 3 (mod 4):
(−t/A') = (−1)^{(A'−1)/2}·(A'/t)·(−1)^{(A'−1)(t−1)/4} = (A'/t) = (−2^{−j}/t) = (−1/t)(2/t)^j = −(2/t)^j.
Hence (A/n) = −(2/(nt))^j, and (A/n) = −1 ⇔ j even or nt ≡ ±1 (mod 8) ⇔ j even or nt ≡ 7 (mod 8).
If nt ≡ 3 (mod 8) then tn + 1 ≡ 4 (mod 8), j = l = 1, so (A/n) = +1. Therefore (A/n) = −1 ⇔ nt ≡ 7 (mod 8)
⇔ t ≡ −n (mod 8) (as n² ≡ 1 mod 8) ⇔ 8 | n + t ⇔ 8 | C (tuv odd). ✓

The table is the case list re-read: t ≡ 0 (4) is Case I with k ≥ 2; t ≡ 2 (4) is Case I, k = 1; t ≡ 1 (4)
is Case II (Case III impossible), where 8 | u(n+t) with v₂(n+t) = 1 forces 4 | u (or 4 | v by symmetry);
t ≡ 3 (4) is Case II (8 | u(n+t) automatic as 4 | n + t and u even) or Case III. ∎

**Numerical check (CERTIFIED).** `scripts/z64_sdeepf_classify.py 30000` (direct Jacobi, Python):
318 476 words, 0 mismatches with the table. `scripts/z64_sdeepf_crit8.c 20000000` (direct Jacobi, C):
674 224 160 words of all n ≤ 2·10⁷, 0 mismatches with 8 | (n+t)(n+u+v); every non-square n ≤ 2·10⁷
with a word has a good word (so (S) holds to 2·10⁷, consistent with the 10⁹ claim in the brief); no square
has a good word (data/z64/sdeepf/crit8_2e7.txt).

**Corollary 2.2 (F1 in advance; PROVED).** For odd m the equation m² + u + v = tuv has no solution with
t, u, v ≥ 2 and 8 | (m² + t)·tuv — e.g. none with 4 | t, none with 4 | u, none with t ≡ 3 (4) and u even.
(Jacobi symbols modulo m² are +1.) This is where non-squareness enters any use of Theorem 2.1: for a
non-square n the character (·/n) is non-trivial, and (S) asks for a word in the GOOD classes.

## §3 Proved cases of (S) and the families that are always good

**Theorem 3.1 (PROVED; (b) is prior: the same word and sign appear in bsG_primes_trivial / DISCOVERIES
Prop 8.1 (per cross-model review); (a) is the classical easy case; (c) appears to be new).** (S) holds for
every n ≡ 1 (mod 4) with n ≡ 5 (mod 8), or n ≡ 2 (mod 3), or n ≡ 3 (mod 9). Explicitly:
* (a) n ≡ 5 (mod 8), n ≥ 13: (t, u, v) = (3, 3, (n+3)/8) is a word (9(n+3)/8 − 3 − (n+3)/8 = n) with
  A = 8, and (8/n) = (2/n)³ = (2/n) = −1 because n ≡ 5 (mod 8). (n = 5 has no word at all.)
* (b) n ≡ 2 (mod 3) (so n ≡ 5 mod 12), n ≥ 17: (t, u, v) = ((n+7)/12, 4, 3) is a word
  (12t − 7 = n) with A = 4t − 1 = (n+4)/3. Here A ≡ 3 (mod 4) (n + 4 ≡ 9 mod 12) and A | n + 4, so
  (A/n) = (n/A) = (−4/A) = (−1/A) = −1. (n = 5: t = 1, not a word; vacuous.)
* (c) n ≡ 3 (mod 9) (so n ≡ 21 mod 36), n ≥ 57: (t, u, v) = ((n+15)/36, 3, 12) is a word (36t − 15 = n)
  with B = tv − 1 = 12t − 1 ≡ 3 (mod 4), B | n + 12 (Lemma 1.1(b)), so (B/n) = (n/B) = (−12/B) = (−3/B) = −1
  because B ≡ 2 (mod 3); and (A/n) = (B/n) by Lemma 1.1(c). (The remaining n = 21 of the class is handled by (a):
  21 ≡ 5 (mod 8), word (3, 3, 3); the displayed (c) word has t = 1 there.)
All witnesses are direct; none needs Theorem 2.1, and none uses primality (F3) — (a) uses only
n ≡ 5 (8), (b) n ≡ 2 (3), (c) 3 ∥ n: each excludes squares (F1).
So (S) is open only for **n ≡ 1 (mod 24)** and for **n ≡ 9 (mod 24) with n ≢ 3 (mod 9)**, i.e. for
n ≡ 1, 9, 25, 33, 49 (mod 72).

**Proposition 3.1′ (universal words of fixed denominator; PROVED).** Let A ≥ 3 be odd, u | A + 1 with
2 ≤ u ≤ (A+1)/2 and (−u/A) = −1. Then every n ≡ 1 (mod 4) with n ≡ −u (mod A) and n ≥ 2A − u has the good
word ((A+1)/u, u, (n+u)/A). (Lemma 1.1(e).) Examples: A = 5, u ∈ {2, 3}: n ≡ 3, 2 (mod 5); A = 7, u ∈ {2, 4}:
n ≡ 5, 3 (mod 7); A = 11, u ∈ {3, 4}: n ≡ 8, 7 (mod 11); A = 13, u ∈ {2, 7}: n ≡ 11, 6 (mod 13). The class
n ≡ 6 (mod 7) (where (7/n) = −1) is NOT of this form for A = 7 (it would need u = 1); among denominators
A ≡ 0 (mod 7) the first universal word inside n ≡ 6 (mod 7) is A = 63, u = 8: n ≡ 55 (mod 63).

**Proposition 3.2 (the "4 | u" family is always good; PROVED).** Let u ≡ 0 (mod 4), v ≡ 3 (mod 4), and
n ≡ −(u+v) (mod uv) with n ≥ 2uv − u − v. Then t := (n+u+v)/(uv) ≥ 2 is an integer, (t, u, v) is a
word, and (A/n) = −1 for A = tu − 1.
*Proof.* Integrality and t ≥ 2 are the hypotheses. A ≡ −1 (mod u), so 4 | A + 1, A ≡ 3 (mod 4), and
A | n + u (Lemma 1.1(b)), hence (A/n) = (n/A) = (−u/A) = (−1/A)(u/A) = −(u/A). Write u = 2^k u', k ≥ 2:
(u'/A) = (−1)^{((u'−1)/2)((A+1)/2)} = 1 since (A+1)/2 is even; (2/A)^k = 1 since either k is even or
k ≥ 3 and then A ≡ −1 (mod 8). So (A/n) = −1. ∎
(The parity v ≡ 3 (4) is forced: n ≡ −u − v ≡ −v (mod 4) must be 1.) Equivalent "divisor" form:
*if n + u (u ≡ 0 mod 4) has a divisor A ≡ −1 (mod u) with 2u − 1 ≤ A ≤ (n+u)/2, (S) holds for n.*
By the symmetry u ↔ v the same holds with the roles of u and v exchanged, and by Theorem 2.1 the same
is true for the "4 | t" family: any factorisation tn + 1 = AB, A ≡ B ≡ −1 (mod t), A, B ≥ 2t − 1, with
4 | t gives a good word.

**Proposition 3.3 (prime-factor criteria for n ≡ 1 mod 8; PROVED; items (1), (3), (5) are prior =
FOREST_CONNECTIVITY Prop 3.1(iii), per cross-model review).** Let n ≡ 1 (mod 8) be a non-square.
(S) holds for n as soon as one of the following happens:
1. n + 4 has a prime factor q ≡ 3 (mod 4), q ≥ 7. [word ((q+1)/4, 4, (n+4)/q); Prop. 3.2; q ≠ n+4 since
   n + 4 ≡ 1 mod 4.]
2. 4n + 1 has a prime factor q ≡ 3 (mod 4), q ≥ 7, with 4n + 1 ≠ 3q. [t = 4, A = q, B = (4n+1)/q ≡ 3 (4),
   B ≥ 7; Theorem 2.1 row t ≡ 0 (4), or directly (q/n) = (n/q) = (−4^{-1}/q) = (−1/q) = −1.]
3. n + 2 has a prime factor q ≡ 5 or 7 (mod 8). [q ≠ n + 2 automatically, as n + 2 ≡ 3 (mod 8); u = 2,
   A = q, t = (q+1)/2, v = (n+2)/q ≥ 3; (q/n) = (n/q) = (−2/q) = −1.]
4. 2n + 1 has a prime factor q ≡ 5 or 7 (mod 8). [q ≠ 2n + 1 automatically (2n + 1 ≡ 3 mod 8); t = 2,
   A = q, B = (2n+1)/q ≥ 3; same symbol.]
5. n + 3 has a prime factor q ≡ 2 (mod 3), q ≥ 5. [u = 3, A = q, t = (q+1)/3, v = (n+3)/q ≥ 4 (4 | n+3);
   (q/n) = (n/q) = (−3/q) = −1.]
6. 3n + 1 has a prime factor q ≡ 2 (mod 3), q ≥ 5. [t = 3, A = q, B = (3n+1)/q; since 4 | 3n + 1 (n ≡ 1 mod 8)
   and q is odd, 4 | B, and B ≡ 2 (3) excludes B = 4, so B ≥ 8; (q/n) = (n/q) = (−3^{-1}/q) = (−3/q) = −1.]
7. More generally, for any k ≥ 1: n + 4k has a prime factor q ≡ −1 (mod 4k) with 8k − 1 ≤ q < n + 4k
   [Prop. 3.2 with u = 4k, A = q]; or 4kn + 1 has a prime factor q ≡ −1 (mod 4k) with
   8k − 1 ≤ q ≤ (4kn+1)/(8k−1) [t = 4k, Theorem 2.1].
*Proof.* Each bracket exhibits a word (check t, u, v ≥ 2 as indicated) and evaluates its symbol by
Lemma 1.1(e) (n ≡ −u (mod A), resp. tn ≡ −1 (mod A)) and the supplementary laws. ∎

**Remark 3.4 (how the (S)-hypothesis "n has a word" is met).** Every n ≡ 1 (mod 6), n ≥ 7, has the word
((n+5)/6, 3, 2) and every n ≡ 5 (mod 12), n ≥ 17, has ((n+7)/12, 4, 3); so every prime p ≡ 1 (mod 4),
p > 5, has a word (the brief's parenthetical claim). Composites can be wordless: n = 105 is the only
non-square n ≡ 1 (4), n ≤ 2·10⁷, n ≠ 5 without a word (data/z64/sdeepf/crit8_2e7.txt and the
flags file). Note ((n+5)/6, 3, 2) for n ≡ 1 (mod 24) has t ≡ 1 (mod 4), u ≡ 3, v ≡ 2: it is a BAD word
(table row t ≡ 1: needs u or v ≡ 0 mod 4). So for n ≡ 1 (mod 24) the guaranteed word is useless.

**Proposition 3.5 (no finite covering; PROVED; prior in kind: HJ_DEEP Lemma 3.2, invol_sign_identities
Prop S, per cross-model review).** (i) Fix a finite set F of pairs (u, v). Let
M = 8·lcm{uv : (u,v) ∈ F}·6. Every non-square n ≡ 1 (mod M), n ≥ 7, has a word, but none of its words
with (u, v) ∈ F (or (v, u) ∈ F) is good. (ii) Fix A₀. Let M = 4·lcm(1, …, A₀)·6. Every non-square
n ≡ 1 (mod M) has a word, but no word of n with denominator A ≤ A₀ is good.
*Proof.* n ≡ 1 (mod 6) gives the word of Remark 3.4. (i) Key fact: *if n is a square modulo 8uv, then a
word (t, u, v) of n (if it exists) is bad.* Indeed the word exists iff uv | n + u + v, and
t = (n+u+v)/(uv) mod 8 is determined by n mod 8uv, hence so is the truth of 8 | (n+t)(n+u+v). Pick an odd square s² ≡ 1 ≡ n (mod 8uv) with s large; then
s² has the word (t', u, v) with t' ≡ t (mod 8), and by Corollary 2.2 8 ∤ (s² + t')(s² + u + v), hence
8 ∤ (n + t)(n + u + v): the word is bad by Theorem 2.1. (ii) For a word with denominator A ≤ A₀,
(A/n) as a function of odd n > 0 is periodic mod 4A | M (Kronecker symbol), so (A/n) = (A/1) = 1. ∎
Consequently any proof of (S) must use words with unbounded denominators A and unbounded (u, v)
(the classical Schinzel-type obstruction for Erdős–Straus, here in the Jacobi language). Words at a
*fixed level t* (factorisations of tn + 1) are not residue-class objects and escape this remark.

**Theorem 3.6 (Mordell-type covering for (S); PROVED, certificate CERTIFIED).** Let
  𝔈 := {1, 9, 25, 49, 81, 105, 121, 169, 225, 249, 265, 289, 321, 345, 361, 385, 441, 505, 529, 561, 585, 609,
        625, 681, 721, 729, 769, 825} ⊂ ℤ/840.
Every n ≡ 1 (mod 4) with n mod 840 ∉ 𝔈 and n ≥ 24529 has a good word given by one of 57 explicit
words (46 fixed-denominator words (A, u) with A | L := 1 441 440 = 2⁵·3²·5·7·11·13, and 11 fixed-(u, v)
words with uv | L/8; the list is printed in `data/z64/sdeepf/cover_check.txt`, a subset of the 77 words of
`cover_words_1441440.txt` found by the greedy covering). Together with the direct verification
of (S) for all n ≤ 10⁸ (`crit8_1e8.txt`), **(S) holds for every non-square n ≡ 1 (mod 4) with
n mod 840 ∉ 𝔈** — i.e. outside 28 of the 210 classes mod 840. 𝔈 contains the 24 classes of odd squares
mod 840 (necessarily: a class containing squares can never be covered by finitely many residue classes of
good words, since for any modulus L′ some sub-class mod L′ contains a large square, which has no good word
by Cor. 2.2); the remaining four
classes 265, 321, 769, 825 all have n ≡ 1 (8), n ≡ 0 or 1 (3), n ≡ 0, ±1 (5) (squares mod 8, 3, 5) and
n ≡ 6 (7) (the non-residue mod 7 not reachable by A = 7). The two other classes with this residue
pattern, 489 and 601, ARE covered (489 e.g. by (A,u) = (224, 15), (4576, 23), (13, 2), (11, 4), (u,v) = (3,3),
(6,15); 601 e.g. by (63, 8), (1287, 56), (231, 8), (u,v) = (14, 15)).
*Proof.* (1) Periodicity. For a fixed-denominator word (A, u): the class is n ≡ −u (mod A), n ≡ 1 (mod 4),
on which the word exists as soon as n ≥ 2A − u (v = (n+u)/A ≥ 2, t = (A+1)/u ≥ 2; gcd(A, n) = 1 is automatic).
Writing A = 2^a A′ (A′ odd), n ↦ (A/n) = (2/n)^a (A′/n) on odd n > 0 is periodic with period dividing 8A′
((2/n) has period 8, (A′/n) = (n/A′)(−1)^{((A′−1)/2)((n−1)/2)} has period 4A′), and 8A′ | L because A′ | L/2⁵.
For even A with a odd the value is NOT constant on the class mod A (e.g. A = 154: −1 for n ≡ 1 (8), +1 for
n ≡ 5 (8)); only the sub-classes mod lcm(A, 8) with value −1 are used. For a fixed-(u, v) word: the class is
n ≡ −(u+v) (mod uv), n ≡ 1 (mod 4); t = (n+u+v)/(uv) is an integer, t ≥ 2 iff n ≥ 2uv − u − v, and by
Theorem 2.1 goodness is 8 | (n+t)(n+u+v), which depends only on n mod 8uv, and 8uv | L. Hence on every
class n₀ (mod L) with n₀ ≡ 1 (mod 4), each listed word either does not apply, or applies with a constant
Jacobi value. (2) Computation. `scripts/z64_sdeepf_cover2.py 1441440` enumerates all such words and marks
the classes mod L on which some word is good (the Jacobi value is computed directly on representatives,
and for the (u,v)-words also cross-checked against Theorem 2.1); there are 13 742 uncovered classes mod L, all
lying over 𝔈 (a subset of the 48 048 classes mod L over 𝔈, not all of them; output `cover2_1441440.txt`). `scripts/z64_sdeepf_cover_check.py`
re-verifies with an independent covering logic (direct Jacobi evaluation on two representatives per class;
the two scripts share only the Jacobi routine, which was checked against sympy) that for each of the
312 312 classes mod L not over 𝔈 one of the listed words applies with (A/n) = −1, that 57 words suffice, and
that the word exists for n ≥ 24529 (`cover_check.txt`). The extension from the representatives to the whole
class mod L is the periodicity of (1); for the (u,v)-words this rests on Theorem 2.1 (so Theorem 3.6 is
PROVED given Theorem 2.1, which is PROVED). The 57-word list is sufficient, not minimal (e.g. (12320, 111) can be dropped, lowering the threshold).
(3) The same computation with L = 2⁵·3³·5·7²·11·13 = 30 270 240
(`cover2_30270240.txt`), with L = 2⁵·3²·5·7·11·13·17 and with L = 2⁵·3²·5·7·11·13·19 leaves exactly the
same 28 classes uncovered (coverage inside them rises, e.g. to 96 % in class 769, but never to 100 %). ∎
*Remarks.* (i) This is the (S)-analogue of Mordell's reduction of Erdős–Straus to the six classes 𝔐 =
{1, 121, 169, 289, 361, 529}; (S) is harder: the 24 odd-square classes are irreducible by any finite
covering (Prop. 3.5), and the four classes n ≡ 6 (7) above are irreducible by the 2⁵·3³·5·7²·11·13
covering as well. (ii) Why n ≡ 6 (mod 7) is delicate: it is the only non-residue class mod 7 not reached by the
denominator A = 7 (u = 2, 4 give n ≡ 5, 3 (mod 7); u = 1 is not allowed). For an n ≡ 1 (8) in such a class
that is moreover a square modulo every modulus coprime to 7, a good word must have 7 | A (else
(A/n) = (A′/n) = (n/A′) = 1), hence u ≡ −n ≡ 1 and t ≡ u^{−1} ≡ 1 (mod 7) — a sparse family (first member
A = 63, u = 8). Whether the four classes are finitely coverable is open here.
> **Update (z75):** Closed in `notes/z75/CONJS_GEN.md` Thm 2 (Opus-reviewed): all four classes `265, 321, 769, 825 (mod 840)` lie in `41 mod 56` and are covered for `n ≥ 97` by the single good word `((n+15)/56, 8, 7)` (reducing the uncovered set mod 840 to the 24 odd-square classes; Remark (i)'s no-cover statement for this note's specific `8uv | period` search remains true).
The only evidence against is the stability of
the uncovered set under the moduli 2⁵·3³·5·7²·11·13, 2⁵·3²·5·7·11·13·17 and 2⁵·3²·5·7·11·13·19 (EVIDENCE).
The growth of the minimal good denominator (`minA_mod840_2e7.txt`: 2058, 3311, 1119, 1871 in these four
classes) does NOT discriminate: the covered classes 489 and 601 show the same growth (1165, 835), because
(u,v)-words have denominators growing with n. (iii) Nothing
in the proof uses primality (F3) or non-squareness beyond the (automatic) fact that squares lie in 𝔈 (F1).

## §4 The exceptional set has density zero

Let E(x) := #{n ≤ x : n ≡ 1 (mod 4), n non-square, n has a word, n has no good word} (the set of
counterexamples to (S) up to x; conjecturally E ≡ 0, and E(10⁹) = 0 by the brief).

**Theorem 4.1 (PROVED, given the classical Landau–Wirsing count).** E(x) ≪ x/√(log x).
*Proof.* By Theorem 3.1 every n ∈ E with n ≥ 13 satisfies n ≡ 1 (mod 8). By Prop. 3.3(1), n + 4 has no
prime factor q ≡ 3 (mod 4) with q ≥ 7, i.e. n + 4 ∈ 𝒮 := {m : every prime factor of m is 3 or ≡ 1 (mod 4)}.
Let G(y) := #{m ≤ y : all prime factors of m are ≡ 1 (mod 4)}. The classical theorem (Landau 1908 for
sums of two squares; in the form needed here Wirsing, Math. Ann. 143 (1961), Satz 1, applied to the
indicator of the set of integers composed of primes ≡ 1 (mod 4), a set of primes of Dirichlet density
τ = 1/2; equivalently the Selberg–Delange method, Tenenbaum *Introduction to analytic and probabilistic
number theory*, Ch. II.6) gives G(y) ~ c·y (log y)^{−1/2}, in particular G(y) ≪ y/√(log 2y) for y ≥ 1.
Then #{m ≤ y : m ∈ 𝒮} = Σ_{e ≥ 0, 3^e ≤ y} G(y/3^e); the terms with 3^e ≤ √y contribute
≪ Σ_e (y/3^e)/√(log √y) ≪ y/√(log y), those with 3^e > √y contribute ≤ Σ_{3^e > √y} y/3^e ≪ √y.
Hence E(x) ≤ 13 + #{m ≤ x + 4 : m ∈ 𝒮} ≪ x/√(log x). ∎
(Non-squareness is not used in this proof beyond the definition of E; indeed all odd squares DO belong to
the sifted superset {n : n + 4 ∈ 𝒮} (m² + 4 is a sum of two coprime squares), which is why only an upper
bound for the exceptional set, not emptiness, can come out of this family alone. Here n + 4 ≡ 5 (mod 8),
so n + 4 lies in 𝒮 ∩ {m ≡ 1 (mod 4)}, which forces e even and is a subset of the sums of two squares, so Landau 1908
alone suffices; Wirsing is cited for the general form. 𝒮 itself is *not* a subset of the sums of two squares: 3 ∈ 𝒮 —
corrected after the Astra retro review.)

**Theorem 4.2 (PROVED modulo a standard upper-bound sieve theorem; the Astra retro review checked an equivalent source
directly — Tao, *254A Notes 4: Some sieve theory*, Corollary 19 with condition (22), copy in
`sources/lit2026/audit-tao-254a-notes4-sieve-theory.md` — and verified the distinct-root, dimension and remainder
conditions for these forms (`data/z64/xreview/REVIEW_SDEEPF_ASTRA.md`); the Halberstam–Richert theorem numbers and
Wirsing's Satz number below were not authenticated).** For every fixed K ≥ 1,
  E(x) ≪_K x (log x)^{−κ_K},  κ_K := 3 + 2 Σ_{k=2}^{K} 1/φ(4k);
since Σ 1/φ(4k) diverges, E(x) ≪_B x (log x)^{−B} for every B > 0.
*Input (the only thing assumed; e.g. Halberstam–Richert, *Sieve Methods*, Thm 2.2 (Brun) or Thm 5.2
(Selberg), with conditions (Ω₁), (Ω₂(κ)), (R) verified for linear forms as usual).* Let L₁, …, L_r be
pairwise non-proportional linear forms L_i(n) = a_i n + b_i (a_i ≥ 1), P₁, …, P_r sets of primes with
Σ_{p ≤ y, p ∈ P_i} (log p)/p = δ_i log y + O(1), and z = x^{c} with c = c(r) > 0 a sufficiently small constant. Then
  #{n ≤ x : for every i, L_i(n) has no prime factor p ∈ P_i with p ≤ z} ≪ x ∏_{i} (log x)^{−δ_i},
the implied constant depending on the forms and the sets.
*Proof of 4.2 from the input.* By Theorem 3.1 and Prop. 3.3, every n ∈ E with √x ≤ n ≤ x is counted by
the sifted set with the 2 + 2 + 2 + 2(K−1) forms and prime sets
  (n+4, P₁), (4n+1, P₁), (n+2, P₂), (2n+1, P₂), (n+3, P₃), (3n+1, P₃), and for 2 ≤ k ≤ K: (n+4k, P_{4k}),
  (4kn+1, P_{4k}),
where P₁ = {q ≡ 3 (4), q ≥ 7}, P₂ = {q ≡ 5, 7 (8)}, P₃ = {q ≡ 2 (3), q ≥ 5}, P_{4k} = {q ≡ −1 (4k),
q ≥ 8k−1}: indeed each criterion of Prop. 3.3 has a side condition (q ≠ n+4 or 4n+1 ≠ 3q, q ≠ n+2,
q ≠ 2n+1, q < n+4k, q(8k−1) ≤ 4kn+1) that is automatic for q ≤ z = x^{c} < x^{1/2}/4 and n ≥ √x (x large).
The densities are δ = 1/2, 1/2, 1/2, 1/2, 1/2, 1/2 and 1/φ(4k) twice (prime number theorem in arithmetic
progressions), so Σδ_i = 3 + 2Σ_{k=2}^K 1/φ(4k) = κ_K. Adding the ≤ √x values n < √x gives the claim. ∎
Status: depends only on a textbook sieve theorem (no conjecture). I have not re-derived the sieve
constants; the forms are distinct, so the standard verification of (Ω₂) applies (ω(p) = #{i : p ∈ P_i}
for p outside the finite set of primes dividing the leading coefficients and pairwise resultants).

**Numerics for the explicit criteria (CERTIFIED, `scripts/z64_sdeepf_escape.c`, data/z64/sdeepf/
escape_counts.txt).** Among the 1 248 419 non-square n ≡ 1 (8), n ≤ 10⁷: 36.9 % escape criterion (1),
15.3 % escape (1)–(2), 3.08 % escape (1)–(4), 0.86 % escape (1)–(6), 0.20 % escape (1)–(6) plus k ≤ 4.
The fractions decrease with x as the theorems predict (e.g. (1)–(6): 1.77 %, 1.28 %, 0.86 % at
x = 10⁵, 10⁶, 10⁷) — logarithmically slowly. Every escaping n still has a good word (crit8 run), of
course with larger (u, v, t).

## §5 What a proof of (S) must do (structural reformulation; honest assessment)

By Theorem 2.1, (S) is *equivalent* to the following purely 2-adic/divisor statement:

> **(S′)** If n ≡ 1 (mod 4) is not a square and n + u + v = tuv has a solution t, u, v ≥ 2, then it has
> one with 8 | (n + t)(n + u + v).

For n ≡ 1 (mod 8) the condition reads 8 | (t + 1)(u + v + 1). In the (W_u) parametrisation, for
n ≡ 1 (mod 8): a word (u, A | n+u, A ≡ −1 mod u) is good iff (−u/A′) = −1 where A′ is the odd part of A
(Lemma 1.1(e) plus (2/n) = 1). So (S) for n ≡ 1 (mod 8) says: *for some u, n + u has a divisor
A ≡ −1 (mod u) in the range [2u−1, (n+u)/2] whose odd part is a non-residue for the character (−u/·)* —
equivalently, **n is a quadratic non-residue modulo the odd part of some word denominator A**
((A/n) = (n/A) for odd A; for even A, (A/n) = (n/A′) when n ≡ 1 mod 8).
So (S) is a "least non-residue"-type statement restricted to the sparse set of word denominators: the
set W(n) of denominators has ≍ (log n)² elements on average (heuristic/EVIDENCE: brief + §6 counts), and a counterexample would be an n for
which (·/n) is trivial on all of W(n) — exactly the behaviour of squares (Cor. 2.2).

Why the obvious routes stop (all three observations PROVED above or classical):
1. Finite residue-class coverings (universal words, Prop. 3.1′/3.2) cannot work on classes where n is a
   square modulo the relevant moduli (Prop. 3.5) — the Jacobi-language form of Schinzel's obstruction.
   Numerically (§6) 170 of the 210 classes mod 840 have bounded minimal good denominator up to 2·10⁷
   (plausibly finitely covered), 40 do not; the worst are the classes 3 | n, n ≡ 1 (8).
2. Fixed-level families (t fixed: factorisations of tn + 1; or u fixed: divisors of n + u) give good
   words *if* a shifted/multiplied n has a prime factor in a prescribed class (Prop. 3.3: sufficient criteria only).
   In general a good word at a fixed level needs a *divisor* in a class, possibly composite: at n = 21841,
   (t, u, v) = (64, 9, 38) has A = 575, B = 2431 and Jacobi −1, yet 64n + 1 = 5²·11·13·17·23 has no prime factor
   ≡ −1 (mod 64) (Astra retro review; an earlier "exactly when" was false). For a
   *single* n nothing forces such a prime factor; on average the failure set has density (log x)^{−δ}
   (§4). Unboundedly many families → density (log x)^{−∞} (Thm 4.2), still not emptiness.
3. The Jacobi value of a word is 2-adically determined (Thm 2.1), so (Assessment, not an impossibility theorem for
   analytic methods: locality only reformulates cancellation as distribution among cells, and future cell-count
   estimates are not excluded) we found no analytic "sign cancellation" argument over words: for a given n all words could a priori sit in bad classes, and the
   only global input distinguishing n from a square is the non-triviality of (·/n), which must be
   transported to the sparse set W(n). Assessment (not a theorem): I see no Pell/Vieta-type involution on
   words (the equation is linear in each of t, u, v; for fixed t it is a divisor problem).
Conclusion (honest): I did not find a proof of (S) for the 28 classes 𝔈 mod 840 of Theorem 3.6 (24 of
which contain squares and are provably out of reach of finite coverings); the results proved here are
Theorems 2.1, 3.1, 3.6, Props. 3.1′–3.5, Thm 4.1 (given Landau), and Thm 4.2 (given a textbook sieve
bound). No HOT LEAD.

## §6 EVIDENCE (all CERTIFIED by the listed scripts; data in data/z64/sdeepf/)

* `crit8_2e7.txt`, `crit8_1e8.txt`: all 674 224 160 words of all n ≤ 2·10⁷, resp. all 4 146 720 310 words of
  all n ≤ 10⁸: criterion of Thm 2.1 exact (0 mismatches, direct Jacobi); (S) holds for every non-square
  n ≤ 10⁸ having a word (24 994 998 such n); squares never have good words.
* `flags_2e6.bin` + `z64_sdeepf_families.c` output (run log in this memo's commit message history / rerun
  `./families 2000000 25`): among 249 292 non-square n ≡ 1 (8), n ≤ 2·10⁶ with words, the number lacking a
  good word in a given sub-family: 4 | t: 472; 4 | u or 4 | v: 54 (incl. primes 193, 2521, 21841,
  66529); t ≡ 3 (4) with u or v even: 1297; t ≡ 2 (4) with u or v ≡ 3 (4): 4826; t ≡ −n (8): 477;
  u = 4 or v = 4 exactly: 85 102; t = 4: 97 861. So (F2) no single sub-family is universal, but the
  union of the "always good" families 4|t, 4|u, 4|v, t ≡ 3 (4) & uv even, t ≡ 2 (4) & (u or v ≡ 3 (4)),
  t ≡ −n (8) is the whole GOOD set and is never empty when words exist (n ≤ 2·10⁷).
* `f4_witnesses.txt`: explicit good words for all 14 primes of star_prime_zeros, all 38 of gstar_zeros,
  all 12 of r8_zeros_1e10 (found by direct Jacobi evaluation, sub-family-free search), and for 284/285
  composites of composite_zeros_le8e6 — the exception n = 105 has no word at all (vacuous for (S)).
* `escape_counts.txt`: §4 — fraction of n ≡ 1 (8) escaping the explicit criteria: 0.86 % for (1)–(6) at
  10⁷, decreasing with x.
* `cover*_*.txt`, `cover_words_1441440.txt`, `cover_check.txt`: the Theorem 3.6 covering (182/210 classes
  mod 840 covered; the 28 uncovered are 𝔈; identical with the 21× larger modulus 30 270 240). With
  fixed-denominator words alone, 170/210 — exactly the 170 classes with bounded minimal good denominator in
  the next item.
* `minA_mod840_2e7.txt`: per class r mod 840 the largest minimal good denominator. Bounded (≤ 100) for 170
  classes; largest values: r = 681: 13 967 (n = 3 561 441), 345: 9392, 225: 8039, 105: 4639, 609: 4234 —
  all with 3 | r, r ≡ 1 (8); Mordell's classes 𝔐 = {1, 121, 169, 289, 361, 529}: 1519, 1356, 905, 804,
  1154, 779. The 3 | n classes are the hardest for length-3 words (for n ≡ 9 (24) the universal word
  ((n+5)/6, 3, 2) does not exist and ((n+15)/36, 3, 12) needs 3 ∥ n).

## §F Falsifiers (re-stated)

* **F1 (odd squares).** Theorem 2.1 is valid for squares and yields Cor. 2.2: squares have no good words
  at all. Every statement proved here uses non-squareness exactly where it must: Theorem 3.1(a) via
  n ≡ 5 (8) (squares are 1 mod 8), (b) via n ≡ 2 (3), (c) via 3 ∥ n; Prop. 3.3 via the existence of a
  prime factor in a non-residue class of n+u / tn+1 (for n = m² every odd prime factor q ∤ u of m² + u has
  (−u/q) = +1, and every odd prime factor q ∤ t of tm² + 1 has (−t/q) = +1, so the hypotheses are never met; without
  the coprimality the symbol can be 0, e.g. q = 3 | 3² + 3 with (−3/3) = 0, and all primes used by Prop. 3.3 satisfy it); Thm 4.1/4.2 bound a set that
  contains the squares (upper bounds only). No argument here claims (S) for a class containing squares.
* **F2 (sub-families).** Sub-family membership was checked on the screened primes ≤ 2·10⁶ (12 of the 14
  star primes, 30 of the 38 gstar primes; `families` output, §6); for the larger screened primes and the
  r8 primes only the existence of a good word was certified (`f4_witnesses.txt`). The
  always-good sub-families 4|t, 4|u, t ≡ 3 (4)&uv even, … each miss some screened primes (e.g. 4|t misses
  409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201; "4|u or 4|v"
  misses none of the screened primes but misses the primes 193, 2521, 21841, 66529 (and 13 ≡ 5 mod 8)). No theorem above
  asserts universality of a sub-family; Theorems 3.1(a–c) are statements about residue classes with
  explicit witnesses, valid for every n in the class (the words (A,u) = (8,3) and (u,v) = (3,4) are among the 57 of Theorem 3.6 and were evaluated by direct Jacobi on representatives of every class mod L; (3,12) is not in that list and rests on its direct proof; (S) itself is verified to 10⁸).
* **F3 (composites).** Nothing uses primality. Theorem 3.1 and Props. 3.1′–3.3 hold for all n ≡ 1 (4) in
  the stated classes, composite or not; Thm 4.1/4.2 count all n. The only composite-specific phenomenon
  is wordlessness (n = 105), which makes (S) vacuous there.
* **F4.** All 14 + 38 primes satisfy (S) with explicit witnesses (`f4_witnesses.txt`), e.g. 409:
  found by the search; 564661441: (2, 7, 43435496), A = 13, (13/564661441) = −1.

## Cross-model review (data/z64/xreview/REVIEW_SDEEPF.md; verdict ACCEPT-WITH-FIXES) — fixes applied
1. Priority of Theorem 2.1 stated (DEDEKIND_ES Thm 4.5/§8.1, FOREST_DEEP_FABLE Thm A, FOREST_CONNECTIVITY
   Thm 2.1, LOWERTAIL_ROUND2_FABLE Thm 1, z1_legendre_levels Prop 1): rediscovery; only the product form is new.
2. Credits added: Thm 3.1(b) (bsG_primes_trivial / DISCOVERIES Prop 8.1), Prop 3.3(1),(3),(5)
   (FOREST_CONNECTIVITY Prop 3.1(iii)), Prop 3.5 (HJ_DEEP Lemma 3.2, invol_sign_identities Prop S).
3. §F F2: "(3,12)" removed from the "among the 57" sentence; prime 13 (≡ 5 mod 8) moved out of the n ≡ 1 (8) list.
4. Prop 3.3(6): B ≥ 8 now justified by 4 | 3n+1 ⇒ 4 | B.
5. §5 item 3: "no Pell/Vieta involutions" relabelled Assessment.
6. Thm 3.6: noted that the 57-word list is sufficient but not minimal.
Net new content per the review: Thm 3.6 (certified covering mod 840, four stubborn non-square classes ≡ 6 (7)),
Thm 3.1(c), Thms 4.1/4.2, and the compact form of Thm 2.1.

## Cross-model retro review (Astra) (data/z64/xreview/REVIEW_SDEEPF_ASTRA.md; verdict ACCEPT-WITH-FIXES) — fixes applied
The reviewer re-derived Thm 2.1 (all 1 280 mod-16 cells), Thms 3.1, 3.6, 4.1, 4.2 and Props 3.1′–3.5; reran the
crit8 census to 3·10⁶ and both covering scripts byte-identically; added an independent 57-word covering check
(`scripts/xrev_retro_sdeepf_checks.py`). Required fixes applied:
1. §5 item 2: the false "exactly when … prime factor" necessity replaced by "sufficient criteria" (counterexample
   n = 21841, (64, 9, 38); 64n + 1 has no prime factor ≡ −1 mod 64).
2. Thm 4.1 aside: 𝒮 ∩ {m ≡ 1 (mod 4)} (not 𝒮, which contains 3) is the subset of sums of two squares.
3. Thm 3.1(c): n = 21 handled by (a). Thm 3.6: "13 742 uncovered classes, all lying over 𝔈" (not all classes over 𝔈).
4. §F F1: the +1 statement restricted to odd q ∤ u (resp. q ∤ t).
5. §5 item 3 kept as Assessment, not a theorem excluding cell-count estimates; Thm 4.2's sieve input now points to
   the checked Tao 254A source and the reviewer's verification of its conditions.
