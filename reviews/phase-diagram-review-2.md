# Hostile review #2 of PHASE_DIAGRAM.md (O204) — R210, round 1

Reviewer: R210 (independent; R209's review not read before this file was written). Document reviewed:
PHASE_DIAGRAM.md as merged from `side-agent/phase-diagram`. From-scratch scripts: `scripts/review_pd2_*.py`
(no reuse of `scripts/pd_*`). No edits to PHASE_DIAGRAM.md in this round.

## Summary verdicts (filled in claim by claim)

| Claim | Verdict |
|---|---|
| Prop 1.1 (normal form) + D-face | SOUND (MINOR m1) |
| Thm 2.1 (k-wall, band, sharpness, equality family) | SOUND — re-derived; 348 shots reproduced; 0 violations among 231 ES^{[2]} shots (of 5.6·10⁶ shots, Q ≤ 10⁵) |
| Consequence "is ES^{(y,1)} now a finite search?" | NO — every slice finite, the band is unbounded; R200 M1 stands (m2: say so explicitly) |
| Prop 3.1 (a), (b); Cor 3.2 | SOUND (MINOR m3, m4); e ≤ 1 / e = 2 EVIDENCE reproduced exactly |
| Prop 4.1 identity | SOUND; θ readings SOUND-AFTER-REPAIRS (m5 attribution, m6 θ is an infimum) |
| Thm 5.1 | SOUND-AFTER-REPAIRS (m7 quantifiers, m8 squares, m9 Step 4 shift, m13 Remark 2) — sieve uniformity, BV level, Siegel zeros all OK |
| §6 B1 statement | SOUND, needlessly weak (m10); lead-in overclaims (m11) |
| §6 class-layer conditional | SOUND |
| T1 per cell | SOUND (m12 label) |
| Labels overall | FAIR; no FATAL, no MAJOR |

**Bottom line.** No FATAL and no MAJOR defect. The new theorem (Thm 2.1(a)) is correct, sharp and elementary; the
sieve theorem (Thm 5.1) is correct relative to BV + Iwaniec, with presentation repairs. The main interpretive risk is
reading "both slicings finite" as "ES^{(y,1)} is a finite search": it is not, and the document (to its credit) never
says it is — but the §3 Reading and the verdict should say so in one sentence (m2).

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

### Thm 5.1 (ES^{(y,e)} with e ≤ y^{(2+o(1))log₃y/(A log₂y)}) — SOUND-AFTER-REPAIRS (m7 quantifiers, m8 squares, m9 Step 4)

Checked line by line; no FATAL or MAJOR gap found.
* **Choice of S, k.** log P = Σ_{s ≤ s_k} log s ~ s_k ~ k log k, so P ≤ (log x)^A maximal gives k log k ~ A log₂x,
  k ~ A log₂x/log₃x ✓ (fixed A; n removes O_n(1) primes). k ≥ 4 for x ≥ x₀(A) (A = 1 needs log x ≥ 1155, i.e.
  x ≳ 10^{502}; `review_pd2_thm51.py`). M = 4 rad(n)P ≤ 4n(log x)^A ✓.
* **Step 1, uniformity in M.** d | (r−1)/2 with d odd squarefree, gcd(d, M) = 1, plus r ≡ a (M), is ONE class mod Md
  (CRT; r odd automatic) ✓; distinct d ⇒ distinct moduli Md ≤ x^{1/2}/log^β x ✓, so Σ_d|r_d| is bounded by the
  BV sum over all q in that range, applied at x and x/2 ✓. BV is a statement summed over all moduli, so it is
  automatically uniform in M; the d = 1 term (modulus M itself) is inside the sum, so no separate Siegel–Walfisz
  input is needed for the main term ✓. Exceptional zeros: BV is unconditional (ineffective via Siegel) and the
  total error x/log^{2A+10}x is far below the main term x/(φ(M) log²x) ≥ x/(4n log^{A+2}x) — this comparison, not
  BV's level, is what caps P at (log x)^{O(1)}, as Remark (1) says ✓. Iwaniec's lower bound needs only the
  dimension-1 axiom ∏_{w≤ℓ<z}(1 − g(ℓ))^{−1} ≤ (log z/log w)(1 + K/log w); setting g(ℓ) = 0 for ℓ | M only
  decreases the product, so K is absolute ✓, and V(z) ≥ ∏_{3≤ℓ<z}(1 − 1/(ℓ−1)) ≫ 1/log z absolutely ✓.
  s = log D/log z = (½ log x − O(A log₂x))/((¼ − ε)log x) → 2/(1−4ε) ≈ 2.083, f(s) ≈ 0.137 > 0 ✓. Primes of M
  never divide (r−1)/2 (r ≡ 3 (4); a_ℓ ≢ 1; a ≡ −1 ≢ 1 mod s) ✓.
* **Step 2.** (s/r) = 1 for r ≡ −1 (s), r ≡ 3 (4) (incl. s = 3) ✓; nontrivial index of Γ_r in the odd-order group
  (F_r^*)² has a prime factor ≥ z ✓. Pigeonhole count explicit in k: (2B'+1)^k(B' log P/log(x/2) + 1) ≤ 6^k Y^{1+1/k}·2 log P
  for large x (as written without the /log(x/2) the "2" should be "3" — immaterial) ✓; 6^k = (log x)^{o(1)} ✓.
* **Step 3.** ℤ^k/Λ_r ≅ ⟨s_i²⟩ = (F_r^*)² (squaring bijective on odd order), det = (r−1)/2 ✓; (2B+1)^k(2B log P + 1)
  ≤ (3B)^{k+1} log P for B log P ≥ 1 ✓; with the stated B this is ≤ x log P/log^{A+5}x = o(x/log^{A+3}x) ✓
  (numerically the margin is exactly log²x, as designed).
* **Step 4.** Minkowski II for the cube: λ₁⋯λ_k ≤ det ✓; λ_k ≤ x/B^{k−1} ✓; covering radius ≤ ½Σλ_i ≤ kλ_k ✓.
  The text "Q := ∏ s_i^{a_i+L} … satisfies Q² ≡ −n/4" is only right if the class represented is that of
  (−n/4)·P^{−2L}, as EXPONENT_CAP Thm 3.2 does explicitly ("As there" hides it) — m9. Overflow exponent
  ≤ v_s(Q) ≤ 2L ✓; s | (r+1)/4 | y ✓; den z = Q₁² with Q odd ✓.
* **Final arithmetic.** 2L ≤ 2k·6^{k}·log^{A+5}x·x^{2/(k+1)} ✓ (B ≥ half its unfloored value); log of the prefactor
  is O(A log₂x) = o(log x·log₃x/log₂x) ✓; y ∈ [x/8, nx/2] and the exponent function is slowly varying, so the
  conversion x → y costs only the o(1) ✓. `review_pd2_thm51.py` confirms log e/log x ≈ 2/(k+1) → 0 along
  x = 10^{10^4} … 10^{10^{64}} (e.g. A = 2: 0.225, 0.143, 0.087, 0.053, 0.031), i.e. the theorem is a genuine but
  very slow improvement over y^δ.
* **Quantifiers (m7).** "has a solution with e ≤ y^{(2+o(1))…}" is not a meaningful statement about one solution.
  What the proof gives: for all A ≥ 1, η > 0, odd n there is x₀ such that for every x ≥ x₀ some solution has
  x/8 ≤ y ≤ nx and e ≤ y^{(2+η)log₃y/(A log₂y)}. The "In particular" clause (fixed ε) is meaningful as stated.
* **Squares (m8).** The scaling reduction for n = m² must run the prime-divisor case with S prime to the WHOLE n
  (FROBENIUS 4.2(c) says so), but Thm 5.1 defines S as "the first k odd primes not dividing n" with n then being the
  divisor; if some s ∈ S divides n/p, scaling by t = n/p can leave s | den z with s | n, violating Def 4.1. Repair:
  "S = first k odd primes not dividing the original n" (the proof needs nothing more).
* Remark (2) (Gallagher range, "exceptional conductor avoided by the choice of S"): Assessment; note the exceptional
  conductor may divide 4 rad(n), which S cannot avoid — soften to "if the exceptional modulus can be avoided".

### §6 B1 statement — SOUND but needlessly weak (m10); lead-in overclaims (m11)

The argument is correct, and it never uses that u is a non-residue: g′ | 1 + 4Q² ⇒ g′ ≡ 1 (4), r^a ≡ 1 (4) ⇒ g ≡ 1 (4)
for every unit u. `review_pd2_b1.py 400 60 3000000`: no point x(u), r ∈ {5, 13, 17, 29}, ANY unit u, lies in any shot
class with g ≤ 400; the shot classes with g ≤ 60 leave uncovered primes in every reduced class mod 5 and mod 13,
residues included (e.g. least uncovered p ≡ 1 (5) is 57 271; p ≡ 4 (5): 10 399). Lead-in "Covering proofs are
excluded for every cell" is broader than the bold statement, which concerns shot identities only (Type I or
other parametric identities are not covered by the argument).

### §6 class-layer conditional — SOUND

x² − Nz² has discriminant 4N = 16(λ²D² − n) ✓; gcd(D, 4N) = 1 (gcd(D, n) = 1, D odd) so the genus-character
criterion applies to −D ✓; one class per genus ⇒ principal genus = principal class ✓; MARKOFF Thm 4.1 turns the
primitive solution into an admissible V_n point ✓. Possible hidden hypothesis gcd(λ, n) = 1 checked and NOT
needed: for the 56 ES^{[2]} data with odd n ≤ 201, k ≤ 6, gcd(Q₁, n) = 1 but gcd(Q₀, n) > 1, den z = Q₁² is
prime to n and divides y², so they are ES^{[2]} solutions under GROWING_MUTE Def 1.0 (direct proof: for ℓ | n,
ℓ | Q₀, ℓ ∤ Q₁, v_ℓ(xy) ≥ 2v_ℓ(Q₀)). Labels (conditional; "not a standard hypothesis") are honest.

### T1 claims per cell — SOUND (one MINOR, m12)

(a) via FROBENIUS Thm 4.2(b)/UNIT_ORBIT Cor 1.2 ✓; shots at m²: m² + 4Q² coprime sum of two squares ✓ (brute
force: no ES^{[2]} shot for n = 9, 25, 49 with Q ≤ 10⁵). (b) scaling ✓. "Any proof of a bounded-cap cell must use a
non-square input" is a heuristic reading, not a theorem; label it Assessment.

## Numbered defects (all MINOR; none FATAL/MAJOR)

**m1** (Notation line 7–9 and Prop 1.1 statement). The shot datum allows any Q ≥ 1 but writes "overflow Q₁ (odd)";
Q₁ is odd only if Q is odd or v₂(Q) ≤ v₂(K) (e.g. n = 5, Q = 2, g = 3: Q₁ = 2, den z = 4). The bijection holds with
"Q₁ odd" as a restriction on the shot data. Repair: "shot data with Q₁ odd (the only ones relevant to the variants,
whose den z is odd)".

**m2** (§3 Reading "e ≤ 1: finite search, the k-wall" and "transition infinite lottery → finite search … between
e = 2 and e = 1"; §6 table "FINITE"; Verdict 2/6). These are statements about slices; the ES^{[2]}/ES^{(y,1)} search
for a single n is an unbounded union of finite slices (fixed-n examples with growing (k, Q₁): n = 3 has
(Q₁, k) = (55, 2), (101, 232), (289, 2984); GROWING_MUTE R201 m3: infinite Pell orbits). Repair: add after Thm 2.1:
"Thm 2.1 does not bound g in terms of n: the band is unbounded, and (GROWING_MUTE R201 m3) every ES^{[2]} point with
μ² − n non-square lies on an infinite Pell orbit inside it. So ES^{(y,1)}(n) remains a non-finite search and R200 M1
(bounded e, growing S: OPEN) stands; the k-wall only forces k and Q₁ to grow together." In §3 Reading say
"(e ≤ 1: finite search on the k = 1 slice)".

**m3** (§3 table, "status (k = 1 slice)" column). ES^□ "PROVED" and ES^{(y)} "PROVED" need "n non-square", and ES^{(y)}
also "gcd(n, 15) = 1" (as in Cor 3.2/† of §6). Repair: add the qualifiers or a † footnote. Optional strengthening:
the shot convention gcd(Q₀, n) = 1 is not needed for the solution (den z = Q₁² stays prime to n: for ℓ | n, ℓ | Q₀,
ℓ ∤ Q₁ one has v_ℓ(xy) ≥ 2v_ℓ(Q₀); checked on 56 cases), so dropping it from the k = 1 slice removes the need for
a_ℓ ≢ −1 and hence for gcd(n, 15) = 1 — if the author wants the slice defined without the convention.

**m4** (§6 table row ES^{(S)}: "k-slices infinite … PROVED (sieve; UNIT_ORBIT 2.4)"). UNIT_ORBIT Thm 2.4 produces
shots with k = (r+1)/(4Q₀) → ∞, not k = 1-slice points; the k = 1 infinitude for ES^{(S)} follows from Prop 3.1(a)
(ES^{(y)} with Q₁ ∈ ⟨S⟩ ⊂ ES^{(S)}), hence carries the same † (non-square, gcd(n, 15) = 1). Repair: cite Prop 3.1 and add †.

**m5** (§4 table "e = 1 … exactly the Coppersmith–Howgrave-Graham–Nagaraj threshold"; §4 Reading; Verdict 4;
report SHARP 3). The CHN abstract (eprint 2004/339, accessed) states that **Lenstra** already proved
#{d | N : d ≡ r (s)} = O((α − 1/4)^{−2}) for s ≥ N^α, α > 1/4; CHN improve to O((α − 1/4)^{−3/2}) and make it
constructive. Repair: "the N^{1/4} threshold (Lenstra 1984; constructive, sharper count: CHN 2008)".

**m6** (§4 "θ_e := 1/(2e+2)"; §6 table θ column; Verdict 4 "ES^{(y,1)} = θ ¼"; report SHARP 3). θ is not an
invariant of a cell: on the Prop 4.1 face the e = 1 family has θ ranging over [1/4, 1/2) (k fixed, λ → ∞ gives
θ → 1/2: log M/log N₁ = 0.486 at k = 1, λ = 10³⁰), and ES ⊂ ES^{[2]} (R = 1) sits at θ ≥ 1/2 on the same face;
for the proved rows θ refers to the prime-face modulus 4∏S, a different face. Repair: define "θ(cell) := infimum
of log M/log N over the face, attained along bounded λ" and say so in the table header; replace "ES^{(y,1)} = θ ¼"
by "the e = 1 face reaches down to θ = ¼"; in §6 Reading note that the proved rows' θ is the prime-face modulus
(consistent with θ_e → 0 as e → ∞).

**m7** (Thm 5.1 statement). "ES^{(y,e)}(n) has a solution with e ≤ y^{(2+o(1))…}" — o(1) over a single solution is
meaningless. Repair: "For every A ≥ 1, η > 0 and odd n > 1 there is x₀(A, η, n) such that for every x ≥ x₀ there is
a solution of ES^{(y,e)}(n) with x/8 ≤ y ≤ nx and e ≤ y^{(2+η)log₃y/(A log₂y)}."

**m8** (Thm 5.1 proof, first sentence: "squares follow from a non-square divisor by scaling"). S is defined as the
first k odd primes not dividing n, where n is then the divisor p; a prime s ∈ S dividing m²/p can remain in den z
after scaling, violating Def 4.1 (ℓ ∤ n). Repair: "run the argument for the divisor p with S the first k odd primes
not dividing the original n" (FROBENIUS 4.2(c) already requires S prime to n).

**m9** (Thm 5.1 Step 4: "Q := ∏ s_i^{a_i+L} with exponents in [0, 2L] satisfies Q² ≡ −n/4"). True only if the
represented class is that of (−n/4)·∏ s_i^{−2L} (EXPONENT_CAP Thm 3.2 says this explicitly); as written it is false.
Repair: copy the EXPONENT_CAP sentence. (Also Step 2: "·2 log P" should be "·3 log P" if the /log(x/2) factor is
dropped — immaterial.)

**m10** (§6 B1 statement, report "Results"). The proof never uses that u is a non-residue (g′ ≡ 1, r^a ≡ 1 (mod 4)
already give g ≡ 1); the statement holds for EVERY reduced class u mod r (`review_pd2_b1.py`: uncovered primes found
in all classes mod 5 and 13 for the g ≤ 60 shot classes, residues included; no x(u) in any class with g ≤ 400).
More generally it holds for every modulus all of whose prime factors are ≡ 1 (mod 4). Repair: drop "non-residue",
state the stronger form.

**m11** (§6 T1 paragraph: "Covering proofs are excluded for every cell (B1; PROVED, elementary)"). The proof covers
shot identities g | n + 4Q² only. Repair: "Covering by finitely many shot identities is excluded for every cell".

**m12** (§6 T1: "any proof of a bounded-cap cell must use a non-square input such as (n/r) = −1"). Heuristic, not
proved. Repair: mark "(Assessment)".

**m13** (Thm 5.1 Remark (2) and report Spark 1: "the exceptional conductor avoided by the choice of S"). The
exceptional modulus may divide 4 rad(n), which the choice of S cannot avoid. Repair: "provided the exceptional
modulus, if any, does not divide 4 rad(n)" or keep purely as Assessment without the mechanism claim.

## Scripts (all from scratch; none of `scripts/pd_*` reused)

* `review_pd2_brute.py NMAX QMAX` — direct shot enumeration by Q, ES^{[2]} decided by den z | y² on the exact solution;
  tests (1.1), duality, wall (a), band (b). Run: `61 100001` (5 617 435 shots, 231 ES^{[2]}, 0 violations).
* `review_pd2_wall.py NMAX KMAX FAMMAX` — duality-face enumeration to 3·W(k); equality families. Run: `101 6 20000`.
* `review_pd2_k1.py A|B …` — §3 k = 1 EVIDENCE (e ≤ 1, e = 2) and one-mute-prime histogram (p < 10⁵).
* `review_pd2_theta.py 61 3 6 151` — Prop 4.1 equivalence, shots, examples, θ along λ → ∞.
* `review_pd2_thm51.py` — Thm 5.1 exponent anatomy in log space.
* `review_pd2_b1.py 400 60 3000000` — B1 core lemma for all units u; uncovered primes per class.

Sources: CHN abstract accessed (IACR eprint 2004/339). Lenstra 1984, Iwaniec linear sieve, BV: not re-accessed;
used in their standard forms (Halberstam–Richert Thm 8.4 / Friedlander–Iwaniec Opera de Cribro Thm 11.13 as cited
in UNIT_ORBIT Lemma 2.2 R190 m6), consistent with R190/R200 checks.
