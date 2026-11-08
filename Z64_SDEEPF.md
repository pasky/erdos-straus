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

**Theorem 2.1 (local criterion).** Let n ≡ 1 (mod 4) and (t, u, v) a length-3 word of n, A = tu − 1. Then

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
    E is even: (A/n) = +1; if u ≡ 3 (4), E is odd: (A/n) = −1. On the other side, n ≡ 2uv − u − v ≡
    −u − v (mod 4) (as 2uv ≡ 0 mod 4), so u + v ≡ 3 (mod 4): u ≡ 1 ⇒ v ≡ 2 (4), v₂(C) = 2, 8 ∤ C;
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
