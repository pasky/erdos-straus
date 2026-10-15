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

### Cor 1.2 (all odd n) — SOUND (one wording defect, M1)
(a) 4/ℓ = 4/(ℓ+1) + 4/(ℓ(ℓ+1)) checked; scaling preserves ES. (b) fine. (c) Re-derived: gcd(K, a) = 1 because
ℓ | K ⟺ q ≡ −p (mod ℓ) (excluded) and p ∤ K; so den(kz) = den(z) = Q₁², Q₁ prime to n, rad Q₁ | y | ky. The
exclusions are needed (if ℓ | Q₁ and ℓ | k, v_ℓ(kz) could stay negative with ℓ | n). Classes exist since ℓ ≥ 5.
**T1 reconciliation:** Thm 1.1 never fires at a² ((q/a²) = 1), confirmed (0 windows at odd squares ≤ 2·10⁵);
the scaled solution from p | a has x = kK with v_p(x) = 2v_p(a) − 1, i.e. it is NOT of Type I/II shape at every prime
of a, so UNIT_ORBIT_ES Cor 1.2 / FROBENIUS_FIRING Thm 4.2(b) are not contradicted (they are shape statements). From
scratch: 58 odd squares a² ≤ 2·10⁵ in case (c), scaled solution checked against Def 1.1 at n = a², cap preserved.

### Thm 1.3 — SOUND-AFTER-REPAIRS (defect M1: “squarefree kernel”)
*Field and discriminant.* With n₀ the squarefree **part** (n = n₀f²) and all primes of n ≡ 1 (4), n₀ ≡ 1 (4),
L = ℚ(i, √2, √n₀) has group (ℤ/2)³, characters χ₁, χ₋₄, χ₈, χ₋₈, χ_{n₀}, χ_{−4n₀}, χ_{8n₀}, χ_{−8n₀}
of conductors 1, 4, 8, 8, n₀, 4n₀, 8n₀, 8n₀; conductor–discriminant: d_L = 2^{2+3+3+2+3+3} n₀⁴ = 2^{16}n₀⁴ ✓.
(i)–(iii) ⟺ q unramified with one Frobenius element (q mod 8 on ℚ(ζ₈); (n₀/q) = (q/n₀) = (q/n) = −1 on √n₀;
q ∤ n automatic as q ≡ 3 (4)) ✓. **But the text defines n₀ := “squarefree kernel” (= rad n in standard usage), for
which (q/n) = (q/n₀) is false** (n = 5²·13: (q/n) = (q/13) ≠ (q/65)). Defect M1.
*Ahn–Kwon — CHECKED against the primary text* (Ann. Inst. Fourier 69 (2019) no. 3, 1411–1458, numdam PDF
downloaded to /tmp): Theorem 1.1: “For every finite extension K of ℚ, every finite Galois extension L (≠ ℚ) of K with
Galois group G, and every conjugacy class C of G, there exists a prime ideal p in P(C) which satisfies N_{K/ℚ}p ≤
d_L^{A₁} with A₁ = 12577”, P(C) = unramified degree-one primes of K with Frobenius C. With K = ℚ this is exactly what
is used. Arithmetic: (2^{16}n⁴)^{12577} = 2^{201232}n^{50308} ✓.
*Bach–Sorenson — primary text NOT accessible* (AMS/Butler links returned HTML). Secondary confirmation: Ahn–Kwon
(p. 1412) quote it as “If GRH holds, then for any class C of G there is a prime p in K of degree 1 over ℚ with
Frobenius C and N p ≤ (4 log d_L + 2.5 n_L + 5)²”, matching O236; the theorem number “5.1” is unverified. Arithmetic:
4(16 log 2 + 4 log n₀) + 20 + 5 = 16 log n₀ + 69.36 ≤ 16 log n + 70 ✓ (n_L = 8). Oesterlé 70(log d_L)² also quoted by
Ahn–Kwon ✓.
*Linnik–Xylouris:* exponent 5 is Xylouris' Bonn dissertation (2011) — not accessed here, standard citation; effectivity
of Linnik's theorem is standard ✓. Class choice mod 8·rad(n) re-derived ✓ (needs n₀ = squarefree part again, M1).
*Scope:* GRH and Ahn–Kwon bounds only for non-squares — correctly restricted in §1.3, but §5 item 1 says “q*(n) is a
least prime in one Chebotarev class of ℚ(i, √2, √n) for every odd n > 1”, false for squares (Defect m1).

### Prop 4.1 (Type I) — SOUND, and stronger than stated (m3)
(a) re-derived (pk′ ≡ −1 mod s; reciprocity with k′ ≡ 3 (4); p ≡ 1 (4)). (b) re-derived. **The hypothesis a | y is not
needed:** for any y with x = pa, z = ay/D, D = k′y − a; any prime t | D must divide ay (else t | den z, t ∤ y), and
t | y ⇒ t | a; also 2 | D ⇒ 2 | a. So D is a product of primes of a, a residue mod k′ under (b)'s hypotheses, while
D ≡ −a ≡ −4⁻¹ (mod k′) is a non-residue. From scratch (`scripts/review_r238_typeI.py 400 60 20000`, ALL y ≤ 2·10⁴, not
only a | y): 612 symbol identities, 0 violations; 95 predicted-empty windows, 0 Def-1.1 solutions (matches O236).

### Numerics — SOUND (all reproduced exactly by independent code)
`review_r238_scan.py 1000000` (data/review_r238_scan_1e6.txt): 39 175 primes; q* ≤ 227 at p = 867 793; top q*/log²p
= 2.835 (4349, 199), 2.734 (29), 2.702 (5), 2.543 (2221) ✓; cap-at-q* histogram identical to O236's (0: 24 266,
1: 9012, 2: 2448, 3: 912, 4: 699, 5: 998, …), max 41 at p = 575 717 (q* = 167) ✓; every solution exact.
`review_r238_best.py 1000000 1000` (data/review_r238_best_1e6.txt, 45 216 exact checks): prime windows 0: 31 850,
1: 7063, 2: 255, 3: 7 ✓; Thm 1.1′ windows 0: 32 043, 1: 6887, 2: 238, 3: 7 ✓ (max 3, worst p = 2221, m = 239).
Extra: allowing *all* m ≡ 4 − p (8), gcd(m, p) = 1 (not only Thm 1.1′ shapes) gives 0: 34 933, 1: 4184, 2: 57,
3: 1 — O236's “prime and composite” means Thm 1.1′ windows only (m2). Composite n: all 49 776 non-squares
n ≡ 1 (4) ≤ 2·10⁵ checked exactly, worst cap at least window 55 (n = 37 933, q = 223) ✓.

### Remarks 1.4 / 1.5 (barriers, novelty) — SOUND as Assessment
B6: one prime of a Chebotarev class suffices, no averaging ✓. B3: nothing counted ✓. B2: g = (n + 4Q²)/q is
solution-dependent; EXPONENT_CAP Thm 2.1 is a theorem, so automatically respected. Novelty: the subgroup step is
verbatim POINTWISE_SIZE Cor 8.3(b) (“prime factors of x generate a subgroup containing −1 iff some is a non-residue
mod p”); the new content is (1) noting (x/q) = −1 always holds at a prime non-residue window, so the subgroup level
always fires, and (2) reading the exponent budget as the cap. Honestly described. It does supersede FROBENIUS_FIRING
Thm 4.2's sieve proof of ES^{(y)} (m4) and CAP_INTERPOLATION's “no unconditional bound known”.

## Defects
(numbered; FATAL / MAJOR / MINOR)

**M1 (MAJOR, one-word repair) — "squarefree kernel" in Thm 1.3(a),(b).** CAP_POINTWISE §1 Thm 1.3(a) l.72 and (b) l.80–81
define n₀ := "squarefree kernel" (standard meaning: rad n) and assert (q/n) = (q/n₀) and L = ℚ(i, √2, √n₀). For
non-squarefree non-square n this is false (n = 5²·13 = 325: (q/325) = (q/13) ≠ (q/65)), so the Chebotarev class in
ℚ(i, √2, √rad n) does not encode (iii), and in (b) a class with (a/rad n) = −1 need not give (q/n) = −1. *Repair:* n₀ :=
squarefree **part** of n (n = n₀f², n₀ squarefree; n₀ > 1 as n is a non-square, n₀ ≡ 1 (4) in case (b)). All bounds
unchanged (n₀ ≤ n; d_L = 2^{16}n₀⁴).

**m1 (MINOR) — §5 item 1 (and AGENT_REPORT SHARP) overstates the field.** "e*(n) < q*(n) for every odd n > 1, where q*(n)
is a least prime in one Chebotarev class of ℚ(i, √2, √n)": for odd squares √n ∈ ℚ and q*(n) is defined via p | a with
non-Chebotarev exclusions (Cor 1.2(c)); for non-squares the field is ℚ(i, √2, √n₀). *Repair:* "…for every odd
non-square n, q*(n) is a least prime in one Frobenius class of ℚ(i, √2, √n₀) (n₀ the squarefree part); for odd squares
q*(n) is a least prime in one class mod 8·rad(n) (Cor 1.2(c))".

**m2 (MINOR) — §3 "windows m ≤ 1000 (prime and composite, Thm 1.1′)".** Correct numbers, but the reader may take
"composite" as all m. Allowing every m ≡ 4 − p (8), gcd(m, p) = 1 (the square-shot cap is defined for any m) gives
0: 34 933, 1: 4184, 2: 57, 3: 1 (max still 3, at p = 18 013, m = 271). *Repair:* say "Thm 1.1′ windows" and optionally add
the all-m line.

**m3 (MINOR, strengthening) — Prop 4.1(b) does not need "a | y".** Proof for arbitrary y in the Prop 4.1 section above
(D = k′y − a is supported on primes of a, D ≡ −a ≡ −4⁻¹ mod k′ a non-residue). *Repair:* drop "with a | y" from the
scope of (b) (keep the parametrisation y = aw as the description of the a | y sub-family), and the Dichotomy's
"dead at every cap" then covers every solution with x = pa. Numerically confirmed for all y ≤ 2·10⁴.

**m4 (MINOR) — consequence not stated: ES^{(y)}(n) is now elementary.** Thm 1.1 + Cor 1.2 give ES^{(y,∞)}(n) for every odd
n > 1 with a two-line proof, superseding FROBENIUS_FIRING Thm 4.2(a),(c) (linear sieve + BV, ineffective). Remark 1.5 should
say this explicitly (and that FROBENIUS_FIRING Thm 4.2(b) / T1 is a shape statement, not contradicted by Cor 1.2(c)).

**m5 (MINOR) — citation provenance.** Ahn–Kwon Thm 1.1 is now confirmed from the primary text by R238 (statement quoted
above); replace "not seen by me — parent to re-check". Bach–Sorenson: the formula (4 log d_L + 2.5n_L + 5)² is confirmed
second-hand (quoted in Ahn–Kwon p. 1412); the theorem number "5.1" remains unverified — say so.

No FATAL defect. No quantifier/uniformity problem found: the constants in Thm 1.3 are absolute (Ahn–Kwon's 12577,
Bach–Sorenson's 4, 2.5, 5 with n_L = 8 fixed), the window q depends on n only through a Frobenius class, and
the cap bound e ≤ q − 3 is uniform. No circularity: Thm 1.1 uses only reciprocity, cyclicity of F_q^*, and EXPONENT_CAP
Prop 1.2 (re-checked: den z = Q₁² verified directly by my Def-1.1 checker on 220 000+ solutions).
