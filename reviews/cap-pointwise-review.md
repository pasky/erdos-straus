# R238 — hostile review #1 of O236 CAP_POINTWISE.md (cap-pointwise)

Reviewer: R238 (side-agent/review-cap-pointwise). Reviewed: CAP_POINTWISE.md at commit c5c0f217 (+ memos z12_*, report O236).
From-scratch scripts: scripts/review_r238_*.py. Status: IN PROGRESS.

## Summary verdicts
(filled in as the review proceeds)

### Definition / loophole check (EXPONENT_CAP Def 1.1)
Def 1.1 (EXPONENT_CAP l.28–30) has **no mute-set parameter at all**: ES^{(y,e)}(n) asks for x, y ∈ ℤ_{>0}, z ∈ ℚ_{>0},
den z = q², q odd, gcd(q, n) = 1, rad q | y, v_ℓ(q) ≤ e. The allowed denominator primes are solution-dependent *by
definition* (FROBENIUS_FIRING Def 4.1 says so explicitly). "Mute set S := primes of x" in Thm 1.1 is therefore only a
proof device, and the constructed triple must (and does) satisfy rad q | **y** — not merely | x. Re-derived: for
s | Q one has s | K, q ≡ −n (mod s), gq = n + 4Q² ≡ n ⇒ g ≡ −1 (mod s) ⇒ s | (g+1)/4 | y. No loophole: the statement is
exactly as meaningful as Def 1.1. Two honest caveats (not defects of O236, but worth one sentence in the doc):
(α) Thm 1.1 makes ES^{(y,∞)} = ES^{(y)} **elementary** for every odd n (no BV, no sieve); FROBENIUS_FIRING Thm 4.2's
linear-sieve proof is superseded — this should be said explicitly (Defect m4).
(β) With e as large as n^{50308} the relaxation is extremely weak; the author already says so (§5 last line). Fine.

### Thm 1.1 (prime window) — SOUND
Re-derived line by line. K odd (q + n ≡ 4 mod 8); gcd(K, qn) = 1; mod q, 4K ≡ n; (−n/q) = −(n/q) = −(q/n) = +1
(Jacobi reciprocity, n ≡ 1 (4), n > 0); so (K/q) = −1, some s₀ | K (odd exponent) is a non-residue, its order in the
cyclic F_q^* (order 2u, u odd) is even, so −1 ∈ H = ⟨S⟩; −K ∈ H is a square, lies in the odd-order part, hence is
the square of (−K)^{(o+1)/2} ∈ H. Shot step: g ≡ 3 (4) (n + 4Q² ≡ 1, q ≡ 3 (4)); g ≡ −1 (mod s) for s | Q (above);
cofactor (n + 4Q²)/g = q, x = K. Cap: by Prop 1.2, e = max a_s − 1 suffices and a_s ≤ ord_q(s) − 1 ≤ q − 2. Edge case
q = 3 gives e = 0 (an ES solution), consistent with ES for n ≡ 2 (mod 3).
From-scratch check (`scripts/review_r238_scan.py`, own discrete-log/backtracking builder; triple built from the
equation 1/z = 4/n − 1/x − 1/y, *not* from the author's z-formula, and tested against Def 1.1 literally): all 39 175
primes p ≡ 1 (4) ≤ 10⁶ fire at q*, Def-1.1 cap equals the box cap in every case, e ≤ q* − 3 always, 0 violations.
`scripts/review_r238_composite.py 200000`: composite n (including n with prime factors ≡ 3 (4)), see below.

### Lemma 3.1 (cap = max_s (a_s − v_s(K))⁺) — SOUND
g + 1 = 4(K + Q²)/q, σ_s = v_s(K + Q²): 2a < b ⇒ σ = 2a ≥ a ⇒ 0; 2a > b ⇒ σ = b ⇒ (a − b)⁺; 2a = b ⇒ σ ≥ b ≥ a ⇒ 0;
and 2a ≤ b ⇒ a − b ≤ 0, so the formula max_s (a_s − b_s)⁺ is uniform. Cap 0 ⟺ Q | K. Confirmed by my Def-1.1 checker
on every built solution (it computes den z directly).

### Thm 1.1′ (composite windows) — SOUND
Each (ℤ/q_i^k)^* is cyclic of order 2·odd (q_i ≡ 3 (4)), so G = E × U with E = {±1}^r; image of K in E is
((n/q_i))_i = ((q_i/n))_i = (−1,…,−1) = image of −1; K^{ord(u)} = −1 ∈ H, −K ∈ H ∩ U is a square in H. m ≡ 4 − n (8)
⇒ m ≡ 3 (4) ⇒ g ≡ 3 (4). a_s < ord_m(s) | λ(m) ⇒ e ≤ λ(m) − 2. The remark "least composite window ≥ q*" is right:
m ≡ 3 (4) needs an odd number of factors ≡ 3 (4), and if none were in the class 4 − n (mod 8) the product would be in
the other class. From-scratch: every Thm 1.1′ composite window m ≤ 300 for every non-square n ≡ 1 (4) ≤ 2·10⁴ fires
with e ≤ λ(m) − 2, solution exact (413 checks, 0 bad).

### Cor 1.2 (all odd n) \u2014 SOUND (one wording defect, M1)
(a) 4/\u2113 = 4/(\u2113+1) + 4/(\u2113(\u2113+1)) checked; scaling preserves ES. (b) fine. (c) Re-derived: gcd(K, a) = 1 because
\u2113 | K \u27fa q \u2261 \u2212p (mod \u2113) (excluded) and p \u2224 K; so den(kz) = den(z) = Q\u2081\u00b2, Q\u2081 prime to n, rad Q\u2081 | y | ky. The
exclusions are needed (if \u2113 | Q\u2081 and \u2113 | k, v_\u2113(kz) could stay negative with \u2113 | n). Classes exist since \u2113 \u2265 5.
**T1 reconciliation:** Thm 1.1 never fires at a\u00b2 ((q/a\u00b2) = 1), confirmed (0 windows at odd squares \u2264 2\u00b710\u2075);
the scaled solution from p | a has x = kK with v_p(x) = 2v_p(a) \u2212 1, i.e. it is NOT of Type I/II shape at every prime
of a, so UNIT_ORBIT_ES Cor 1.2 / FROBENIUS_FIRING Thm 4.2(b) are not contradicted (they are shape statements). From
scratch: 58 odd squares a\u00b2 \u2264 2\u00b710\u2075 in case (c), scaled solution checked against Def 1.1 at n = a\u00b2, cap preserved.

### Thm 1.3 \u2014 SOUND-AFTER-REPAIRS (defect M1: \u201csquarefree kernel\u201d)
*Field and discriminant.* With n\u2080 the squarefree **part** (n = n\u2080f\u00b2) and all primes of n \u2261 1 (4), n\u2080 \u2261 1 (4),
L = \u211a(i, \u221a2, \u221an\u2080) has group (\u2124/2)\u00b3, characters \u03c7\u2081, \u03c7\u208b\u2084, \u03c7\u2088, \u03c7\u208b\u2088, \u03c7_{n\u2080}, \u03c7_{\u22124n\u2080}, \u03c7_{8n\u2080}, \u03c7_{\u22128n\u2080}
of conductors 1, 4, 8, 8, n\u2080, 4n\u2080, 8n\u2080, 8n\u2080; conductor\u2013discriminant: d_L = 2^{2+3+3+2+3+3} n\u2080\u2074 = 2^{16}n\u2080\u2074 \u2713.
(i)\u2013(iii) \u27fa q unramified with one Frobenius element (q mod 8 on \u211a(\u03b6\u2088); (n\u2080/q) = (q/n\u2080) = (q/n) = \u22121 on \u221an\u2080;
q \u2224 n automatic as q \u2261 3 (4)) \u2713. **But the text defines n\u2080 := \u201csquarefree kernel\u201d (= rad n in standard usage), for
which (q/n) = (q/n\u2080) is false** (n = 5\u00b2\u00b713: (q/n) = (q/13) \u2260 (q/65)). Defect M1.
*Ahn\u2013Kwon \u2014 CHECKED against the primary text* (Ann. Inst. Fourier 69 (2019) no. 3, 1411\u20131458, numdam PDF
downloaded to /tmp): Theorem 1.1: \u201cFor every finite extension K of \u211a, every finite Galois extension L (\u2260 \u211a) of K with
Galois group G, and every conjugacy class C of G, there exists a prime ideal p in P(C) which satisfies N_{K/\u211a}p \u2264
d_L^{A\u2081} with A\u2081 = 12577\u201d, P(C) = unramified degree-one primes of K with Frobenius C. With K = \u211a this is exactly what
is used. Arithmetic: (2^{16}n\u2074)^{12577} = 2^{201232}n^{50308} \u2713.
*Bach\u2013Sorenson \u2014 primary text NOT accessible* (AMS/Butler links returned HTML). Secondary confirmation: Ahn\u2013Kwon
(p. 1412) quote it as \u201cIf GRH holds, then for any class C of G there is a prime p in K of degree 1 over \u211a with
Frobenius C and N p \u2264 (4 log d_L + 2.5 n_L + 5)\u00b2\u201d, matching O236; the theorem number \u201c5.1\u201d is unverified. Arithmetic:
4(16 log 2 + 4 log n\u2080) + 20 + 5 = 16 log n\u2080 + 69.36 \u2264 16 log n + 70 \u2713 (n_L = 8). Oesterl\u00e9 70(log d_L)\u00b2 also quoted by
Ahn\u2013Kwon \u2713.
*Linnik\u2013Xylouris:* exponent 5 is Xylouris' Bonn dissertation (2011) \u2014 not accessed here, standard citation; effectivity
of Linnik's theorem is standard \u2713. Class choice mod 8\u00b7rad(n) re-derived \u2713 (needs n\u2080 = squarefree part again, M1).
*Scope:* GRH and Ahn\u2013Kwon bounds only for non-squares \u2014 correctly restricted in \u00a71.3, but \u00a75 item 1 says \u201cq*(n) is a
least prime in one Chebotarev class of \u211a(i, \u221a2, \u221an) for every odd n > 1\u201d, false for squares (Defect m1).

### Prop 4.1 (Type I) \u2014 SOUND, and stronger than stated (m3)
(a) re-derived (pk\u2032 \u2261 \u22121 mod s; reciprocity with k\u2032 \u2261 3 (4); p \u2261 1 (4)). (b) re-derived. **The hypothesis a | y is not
needed:** for any y with x = pa, z = ay/D, D = k\u2032y \u2212 a; any prime t | D must divide ay (else t | den z, t \u2224 y), and
t | y \u21d2 t | a; also 2 | D \u21d2 2 | a. So D is a product of primes of a, a residue mod k\u2032 under (b)'s hypotheses, while
D \u2261 \u2212a \u2261 \u22124\u207b\u00b9 (mod k\u2032) is a non-residue. From scratch (`scripts/review_r238_typeI.py 400 60 20000`, ALL y \u2264 2\u00b710\u2074, not
only a | y): 612 symbol identities, 0 violations; 95 predicted-empty windows, 0 Def-1.1 solutions (matches O236).

### Numerics \u2014 SOUND (all reproduced exactly by independent code)
`review_r238_scan.py 1000000` (data/review_r238_scan_1e6.txt): 39 175 primes; q* \u2264 227 at p = 867 793; top q*/log\u00b2p
= 2.835 (4349, 199), 2.734 (29), 2.702 (5), 2.543 (2221) \u2713; cap-at-q* histogram identical to O236's (0: 24 266,
1: 9012, 2: 2448, 3: 912, 4: 699, 5: 998, \u2026), max 41 at p = 575 717 (q* = 167) \u2713; every solution exact.
`review_r238_best.py 1000000 1000` (data/review_r238_best_1e6.txt, 45 216 exact checks): prime windows 0: 31 850,
1: 7063, 2: 255, 3: 7 \u2713; Thm 1.1\u2032 windows 0: 32 043, 1: 6887, 2: 238, 3: 7 \u2713 (max 3, worst p = 2221, m = 239).
Extra: allowing *all* m \u2261 4 \u2212 p (8), gcd(m, p) = 1 (not only Thm 1.1\u2032 shapes) gives 0: 34 933, 1: 4184, 2: 57,
3: 1 \u2014 O236's \u201cprime and composite\u201d means Thm 1.1\u2032 windows only (m2). Composite n: all 49 776 non-squares
n \u2261 1 (4) \u2264 2\u00b710\u2075 checked exactly, worst cap at least window 55 (n = 37 933, q = 223) \u2713.

### Remarks 1.4 / 1.5 (barriers, novelty) \u2014 SOUND as Assessment
B6: one prime of a Chebotarev class suffices, no averaging \u2713. B3: nothing counted \u2713. B2: g = (n + 4Q\u00b2)/q is
solution-dependent; EXPONENT_CAP Thm 2.1 is a theorem, so automatically respected. Novelty: the subgroup step is
verbatim POINTWISE_SIZE Cor 8.3(b) (\u201cprime factors of x generate a subgroup containing \u22121 iff some is a non-residue
mod p\u201d); the new content is (1) noting (x/q) = \u22121 always holds at a prime non-residue window, so the subgroup level
always fires, and (2) reading the exponent budget as the cap. Honestly described. It does supersede FROBENIUS_FIRING
Thm 4.2's sieve proof of ES^{(y)} (m4) and CAP_INTERPOLATION's \u201cno unconditional bound known\u201d.

## Defects
(numbered; FATAL / MAJOR / MINOR)
