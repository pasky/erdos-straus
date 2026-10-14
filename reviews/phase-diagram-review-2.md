# Hostile review #2 of PHASE_DIAGRAM.md (O204) — R210, round 1

Reviewer: R210 (independent; R209's review not read before this file was written). Document reviewed:
PHASE_DIAGRAM.md as merged from `side-agent/phase-diagram`. From-scratch scripts: `scripts/review_pd2_*.py`
(no reuse of `scripts/pd_*`). No edits to PHASE_DIAGRAM.md in this round.

## Summary verdicts (filled in claim by claim)

| Claim | Verdict |
|---|---|
| Prop 1.1 (normal form) + D-face | SOUND (one MINOR wording point, m1) |
| Thm 2.1 (k-wall, band, sharpness) | SOUND |
| Consequence "ES^{(y,1)} finite search?" | NOT claimed by the doc; R200 M1 stands (see §2 below; MINOR m2 on wording) |

## Claim-by-claim

### Prop 1.1 (normal form k(4ab − n) = b + aQ₁²) and the D-face — SOUND

Re-derived by hand. Forward: with j' = (m + n)/Q₀ ∈ 4ℤ (Prop 1.3) and b = j'/4, Prop 1.3(a) reads
4aD = 4kn + 4b with D = 4kb − Q₁², i.e. a(4kb − Q₁²) = kn + b ⟺ k(4ab − n) = b + aQ₁². Converse: with
m = 4ab − n and km = b + aQ₁²: (4ak − 1)m = 4a·km − m = 4ab + 4a²Q₁² − 4ab + n = n + 4a²Q₁² ✓; and
gcd(aQ₁, ak) = a·gcd(Q₁, k) = a ✓. Mute rungs: under gcd(Q, n) = 1 and gcd(Q₁, k) = 1, rad Q₁ | y = nak ⟺
rad Q₁ | a, and den z = Q₁² | y² ⟺ Q₁ | a ✓. ES line Q₁ = 1 is 4abk = a + b + nk, the d = 1 slice of Type II ✓.
D-face: a = λt (Q₁ = t | a): k(4λtb − n) = b + λt³ ✓. Side conditions: gcd(b, n) = 1 is automatic for shots
(4Q₀b = m + n and gcd(m, n) | gcd(4Q², n) = 1), m is odd, m ≡ −n (mod b), and
4b(b + λt³) = 4b² + t²(m + n) ≡ nt² + 4b² (mod m) ✓. Both self-review counterexamples (n = 9; n = 61) verified by hand.
The (Y2) example n = 13: 13 + 4·25² = 2513 = 7·359, K = 90, Q₀ = 5, Q₁ = 5, k = 18 ✓.
Numerics (`review_pd2_brute.py 61 100001`: direct enumeration of all shots Q ≤ 10⁵ odd, ES^{[2]} decided by
den z | y² on the exact solution, not via Q₁ | Q₀): 5 617 435 shots, 231 ES^{[2]}; identity (1.1),
gcd(Q₁, k) = 1, den z = Q₁² hold in all 231.

### Thm 2.1 (second archimedean wall) — SOUND

(a) Re-derived: Q₁ | Q₀ ⇒ g = 4kQ₀ − 1 ≡ −1 (mod 4kQ₁), so g ≥ 4kQ₁ − 1, and Dg = 4k²n + Q₁² mod Q₁ gives
D ≡ −4k²n, so Q₁ | D + 4k²n > 0 and D ≥ Q₁ − 4k²n. If Q₁ > 4k²n:
(Q₁ − 4k²n)(4kQ₁ − 1) ≤ 4k²n + Q₁² ⟺ (4k − 1)Q₁² ≤ (16k³n + 1)Q₁ ✓ (the 4k²n terms cancel exactly). The case
Q₁ ≤ 4k²n and the identity 16k³n + 1 = (4k − 1)(4k²n + kn) + kn + 1 ✓; W(k) ≤ 6k²n ✓ (k = 1: 16n + 1 ≤ 18n).
(b) Re-checked against EXPONENT_CAP Thm 2.1's proof: the branch kj ≥ 2Q₁² gives Q₀ ≤ 2n/j + 1/(2k) ≤ (n+1)/2
(j ≥ 4), so Q₁ | Q₀ ⇒ Q₁ ≤ (n+1)/2; otherwise k ≤ kj/4 < Q₁²/2 ✓. No hidden hypothesis (gcd(Q, n) = 1 is not used).
Band and "both slicings finite": fixed k ⇒ Q₁ ≤ W(k) ⇒ finitely many (Q₁, D); fixed Q₁ ⇒ g bounded ✓.
Sharpness: (n, k, Q₁) = (3, 2, 55): 48 + 3025 = 3073 = 7·439, Q₀ = 55 ✓. Family n ≡ 2 (mod 3):
(4n+1)(64n+1) = 256n² + 68n + 1 = 9(4n) + (16n+1)² ✓; D ≡ 3 (mod 4) ⟺ n ≡ 2 (mod 3) ✓; Q₀ = Q₁ ✓. The aside
Q₁ = 4n + 3, D = 3: Q₀ = (4n+3)(n+1)/3, so Q₁ | Q₀ ✓ (n ≡ 2 mod 3).
Numerics (`review_pd2_wall.py 101 6 20000`, duality-face enumeration with Q₁ up to 3·W(k), exact solution
check): 348 ES^{[2]} shots, all with Q₁ ≤ 1.3W(k) (none in (1.3W, 3W]), zero violations — the author's 348
reproduced; the author's "12 skipped" equals my count of gcd(Q₀, n) > 1 with gcd(Q₁, n) = 1 (46 if Q₁ is
not pre-filtered; convention only). Equality family verified exactly for all 3 333 n ≡ 5 (mod 6) < 2·10⁴ (Q₁
squarefree in 2 698), and the Q₁ = 4n + 3 family likewise. `review_pd2_brute.py 61 100001`: 0 violations of (a)
or (b) among 231 ES^{[2]} shots; max Q₁/W(k) = 1.0000, max k/Q₁² = 0.4360 at (29, 126, 17) — both author
figures reproduced.

### Consequence: is ES^{(y,1)} now a FINITE search? — NO; R200 M1 is NOT superseded

Thm 2.1 bounds each fixed-k and each fixed-Q₁ slice, but the band √(Q₁/(6n)) ≤ k < Q₁²/2 is unbounded, so it
gives no bound on g (or Q₁, or k) in terms of n alone. Concretely, ES^{[2]} shots of a fixed n sit at growing
(k, Q₁): n = 3 has (Q₁, k, g) = (1, 2, 7), (55, 2, 439), (101, 232, 93 727), (289, 2 984, 3 449 503) up to Q ≤ 10⁵;
n = 41 has 23 shots with Q₁ up to 307, k up to 1 969 (`review_pd2_brute.py`; counts keep rising when Q_max goes
3·10³ → 10⁵ for almost every n). Combined with GROWING_MUTE R201 m3 (every ES^{[2]} point with μ² − n non-square
lies on an infinite Pell orbit, A = 2k and B = Q₁ → ∞ together — consistent with the band), the ES^{[2]} search
for one n is a countable union of finite slices with no global bound. For ES^{(y,1)} (squarefree Q₁) the same holds
pending squarefreeness on orbits. Precisely: **R200 M1 ("ES^{(y,e)}, bounded e, growing S: OPEN, not a finite
search") stands for e = 1**; what is new is only that the search is confined to the band, i.e. both coordinates
must grow together (log k ∈ [½ log Q₁ − O(log n), 2 log Q₁]). The document itself never claims a global
finite search (§6 "union of finite searches in both directions" is correct), but see m2.

### Prop 3.1 (k = 1 slice) and Cor 3.2 — SOUND (MINOR m3, m4)

(a) Re-derived. k = 1 shots of overflow Q₁ are Prop 1.3's converse at k = 1: g | 4n + Q₁², and the congruence
D ≡ −Q₁² (mod 4) is automatic for g ≡ 3 (mod 4) and Q₁ odd (D·g ≡ 1 mod 4) ✓; Q₀ = (g+1)/4, Q = Q₀Q₁.
The sieve: class a mod M = 4 rad(n)∏S with a ≡ 3 (4), a ≡ −1 (s), a_ℓ ∉ {0, ±1} (ℓ | n), quadratic character at
one ℓ₀ of odd exponent fixed so that (n/r) = −1 (for n ≡ 1 (4): (r/n) = −1; for n ≡ 3 (4) and r ≡ 3 (4):
(r/n) = +1 — the doc's "condition on the Jacobi symbol (r/n)" covers both) ✓. Residue counting outside
{0, ±1}: ℓ ≡ 1 (4): (ℓ−5)/2 residues, (ℓ−1)/2 non-residues; ℓ ≡ 3 (4): (ℓ−3)/2 of each ✓ (ℓ = 7: {2,4} / {3,5}).
Lemma 2.2 of UNIT_ORBIT (re-read) needs only a ≡ 3 (4), gcd(a, M) = 1, a ≢ 1 (ℓ) for odd ℓ | M ✓ — so excluding
−1 is free, as claimed. (s/r) = 1 for r ≡ −1 (s), r ≡ 3 (4) as in FROBENIUS Thm 4.2 ✓; Γ_r = (F_r^*)² ∋ −4n
(since (−4n/r) = (−1/r)(n/r) = 1) ✓; square root inside the odd-order group lies in Γ_r, exponents ≥ 0 ✓;
r ≢ −1 (ℓ) ⇒ gcd(Q₀, n) = 1 ✓; rad Q₁ | ∏S | (r+1)/4 = Q₀ ✓. Also checked: for k = 1 one has
z = n(n + Q₀Q₁²)/(gQ₁²), so den z is odd even when Q₀ is even (Prop 1.2 is stated for Q odd; no gap here).
The restriction gcd(n, 15) = 1 is sufficient, not necessary at 5 (5 | n is a problem only if 5 must serve as ℓ₀
with a residue prescribed) — harmless.
(b) = Thm 2.1(a) at k = 1 ✓; n = 59: 16·59 + 1 = 945, /3 = 315 = 3²·5·7 ✓.
Cor 3.2: infinitude for ES^□ (Dirichlet: r ≡ 3 (4), (−n/r) = 1, r ≢ −1 (ℓ | n), then lift Q₁ mod r to an odd
integer prime to n by CRT) and for ES^{(y)} (the sieve gives ≫ x/log²x − o(x/log²x) → ∞ good r) ✓; distinct g
force Q₁ → ∞ by g ≤ 2nQ₁²(n + Q₁²) ✓.
EVIDENCE reproduced from scratch (`review_pd2_k1.py A 200000 13 17 29 37 97 101`, sympy factorisation,
exact solutions, den z = Q₁², rad Q₁ | y): e ≤ 1 counts/max 0/–, 5/91, 6/155, 0/–, 2/79, 13/431 and e = 2
(cube-free, non-squarefree) maxima 185 761, 120 409, 152 881, 194 271, 165 649, 192 721 with exactly the
author's bit-length sets — **identical to the document**. One-mute-prime evidence (`review_pd2_k1.py B 100000 30`):
every prime 5 ≤ p < 10⁵ has a ≤ 17 with a k = 1 shot of overflow 3^a (histogram 0: 7125, 1: 781, 2: 603, 3: 333,
…, 15: 1, 17: 1); the shot convention gcd(Q₀, p) = 1 never forced a larger a. (Range 10⁵ only, not 10⁶.)

### Prop 4.1 (one family for all caps) — SOUND as an identity; θ-readings need scoping (MINOR m5, m6)

Re-derived: MR ≡ 1 (g), so M^{2e}(4k²n + R^{2e}) ≡ 4k²nM^{2e} + 1 = N_e (g), gcd(M, g) = 1 ✓; D ≡ −R^{2e} (4k) ✓;
Prop 1.3 converse (gcd(R^e, k) = 1) gives Q₀ = λR; gcd(λR^{e+1}, kλR) = λR·gcd(R^e, k) = λR ✓; M^{e+1} = 2λX_e ✓.
e = 0 gives all ES shots (take R = 1, λ = Q₀) ✓; e = 1 gives all ES^{[2]} shots (R = Q₁, λ = Q₀/Q₁; gcd(Q₁, 2kn) = 1
is automatic) ✓. `review_pd2_theta.py 61 3 6 151`: equivalence on 237 432 tuples (e ≤ 3), 423 shots with
den z = R^{2e} exactly; examples n = 13 (N_e/g = 17 479, D = 11) and n = 113 (Q₀ = 15) ✓.
Citations: CHN (eprint 2004/339 abstract, accessed): for s ≥ N^α, α > 1/4, gcd(r, s) = 1, #{d | N, d ≡ r (s)}
= O((α − 1/4)^{−3/2}); **the same abstract credits Lenstra with the bound O((α − 1/4)^{−2}) already in this range**,
so the N^{1/4} threshold is Lenstra's (1984), CHN improved the exponent and made it constructive (m5). Lenstra 1984
(≤ 11 for s > N^{1/3}): not re-accessed, consistent with R200's check. Neither theorem gives existence; the doc
uses them only as regime labels (Assessment) ✓, and correctly disclaims deriving the k-wall from CHN.
θ: numerically log M/log N_e = 0.245/0.165 at k = 10⁶, λ = 1 (e = 1/2), but 0.486/0.247 at k = 1, λ = 10³⁰ —
i.e. the e-cell is not "at" θ = 1/(2e+2): that is the infimum over the face, and ES ⊂ ES^{[2]} itself sits at θ = ½
on the same face (m6).
