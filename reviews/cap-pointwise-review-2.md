# R239 — hostile review #2 of O236 (CAP_POINTWISE.md), round 1

Reviewer: R239 (independent; no edits to author's files in round 1). Scripts: `scripts/review_r239_*.py`.
Status: IN PROGRESS.

## Summary verdicts
(filled in per claim below)

## Claim-by-claim

### C1. Definition check / "mute-set loophole" (brief item 1) — SOUND (no loophole)
EXPONENT_CAP Def 1.1 ((J)34) contains **no mute set at all**: ES^{(y,e)}(n) asks for 4/n = 1/x+1/y+1/z, x,y ∈ ℤ_{>0},
z ∈ ℚ_{>0}, and every ℓ with v_ℓ(z) < 0 must satisfy ℓ ∤ 2n, ℓ | y, v_ℓ(z) even, v_ℓ(z) ≥ −2e. The allowed denominator
primes are solution-dependent *by definition* (FROBENIUS_FIRING Def 4.1 says so explicitly: "the allowed denominators
depend on the solution"). So "S := primes of x" is not a definitional choice the author makes; it is a construction device.
Moreover I re-derived that it is FORCED: if ℓ | den z and ℓ | y then from 1/z = (4xy − nx − ny)/(nxy) one gets
ℓ | 4xy − nx − ny ⇒ ℓ | nx ⇒ ℓ | x (ℓ ∤ n). **Every** ES^{(y,e)} solution has its denominator primes inside
gcd(x, y); so "mute primes = primes of x" is the general shape, not a loophole. Hence the statement e*(n) < q is
exactly the statement about the object defined in (J)34, neither trivialised nor strengthened.
Meaningfulness (Assessment): ES^{(y,e)} with e ≍ n^{O(1)} (or (log n)² under GRH) is a weak relaxation of ES; the
author says so (§5 last line). No overclaim found.

### C2. Thm 1.1 (prime window) — SOUND
Re-derived line by line:
* q + n ≡ 4 (mod 8) ⇒ K odd, q ≡ 3 (mod 4) (n ≡ 1 (4)). gcd(K, qn) = 1 as written. ✓
* (−K/q) = (−n/q) (as 4K ≡ n, 4 a square) = (−1/q)(n/q) = −(q/n) = +1 (Jacobi reciprocity, n ≡ 1 (4), n > 0). So
  (K/q) = −1, some s₀ | K is a non-residue; F_q^* cyclic of order 2u, u odd; ord(s₀) even ⇒ −1 = s₀^{ord/2} ∈ H. ✓
* −K ∈ H is a square ⇒ its order o | u odd ⇒ (−K)^{(o+1)/2} ∈ H is a square root of −K. ✓ Reduce exponents mod ord_q(s)
  ⇒ 0 ≤ a_s ≤ ord_q(s) − 1 ≤ q − 2. ✓
* Direct identity check (mine): 1/K + 4/(n(g+1)) + 4Q²/(nK(g+1)) = 4/n ⟺ n(g+1) + 4Q² = 4Kg ⟺ n + 4Q² = qg. ✓
  (holds for ANY Q with q | n + 4Q²).
* g ≡ 3 (4) (n + 4Q² ≡ 1, q ≡ 3); s | K ⇒ q ≡ −n (s) ⇒ gq ≡ n ⇒ g ≡ −1 (s). ✓ So v_s(g+1) ≥ 1 for every s | Q,
  and Prop 1.2's criterion with e = max a_s − 1 holds. e ≤ q − 3. ✓
* Q odd, gcd(Q, n) = 1, den z = Q₁² odd, coprime to n, rad Q₁ | rad Q | K... and | (g+1)/4 | y. ✓
Numerically confirmed from scratch (C8 below).
Small slack (not a defect): a_s ≤ ord_q(s) − 1 and in fact a_s ≤ ord_q(s²)·… one can take a_s < ord_q(s); with
b_s = v_s(K) ≥ 1 the true cap is ≤ q − 3 (Lemma 3.1). Fine.

### C3. Thm 1.1′ (composite windows) and its Remark — SOUND
G = ∏ (ℤ/q_i^{k_i})^*, each cyclic of order q_i^{k_i−1}(q_i − 1) = 2·odd (q_i ≡ 3 (4)), so G = E × U, E = 2-torsion
= {±1}^r, and the E-component of an element is read off by the Legendre symbols mod q_i. (K/q_i) = (n/q_i) = (q_i/n) = −1
for all i ⇒ E-component of K is (−1,…,−1) = image of −1 ∈ G; K^{ord(u)} = −1 ∈ H. Rest as C2. a_s < ord_m(s) | λ(m) ⇒
e ≤ λ(m) − 2. ✓ Remark: m ≡ 3 (4) is a product of an odd number of primes ≡ 3 (4); if none were ≡ 4 − n (mod 8),
all would be ≡ the other class c and m ≡ c^{odd} = c ≢ 4 − n (8). So some prime factor q_i ≤ m satisfies (i)–(iii);
least composite window ≥ q*. ✓

### C4. Cor 1.2 (all odd n) and the T1 reconciliation — SOUND (one MINOR wording issue, D3)
(a) standard. (b) n non-square with all primes ≡ 1 (4): n₀ > 1, χ = (·/n₀) non-principal, so the required class mod
8 rad n exists (Dirichlet). (c) n = a²: (q/n) = (q/a)² = 1 for q ∤ n, so (iii) never holds at n — "no window at an odd
square" is a trivial consequence of the Jacobi symbol and is consistent with FROBENIUS_FIRING Thm 4.2(b)/T1. Cor 1.2(c)
does not contradict it because the solution is a *scaled* p-solution, which is not Type II at every prime of a.
Scaling re-checked: q ≢ −p (mod ℓ) for ℓ | a, ℓ ≠ p, plus p ∤ K (p | K ⇒ p | q), gives gcd(K, n) = 1, hence
gcd(Q₁, k) = 1, den(kz) = Q₁², rad Q₁ | y | ky, ℓ ∤ 2n, exponents unchanged. ✓ Class exists: ℓ ≡ 1 (4) ⇒ ℓ ≥ 5,
two excluded residues 0, −p mod ℓ. ✓ (Using any p | a, p ≡ 1 (4).)

### C5. Thm 1.3 (size of q*(n)) and the cited theorems — SOUND-AFTER-REPAIRS (citation MINORs D1, D2; improvement D3)
* Field and discriminant: n₀ ≡ 1 (4) squarefree > 1 (all primes ≡ 1 (4)), L = ℚ(ζ₈, √n₀), [L:ℚ] = 8 (√n₀ ∉ ℚ(ζ₈)
  since n₀ is odd > 1). Characters: 1, χ_{−4}, χ_8, χ_{−8}, χ_{n₀}, χ_{−4}χ_{n₀}, χ_8χ_{n₀}, χ_{−8}χ_{n₀}, conductors
  1, 4, 8, 8, n₀, 4n₀, 8n₀, 8n₀ (gcd(n₀, 8) = 1). Conductor–discriminant: d_L = 2^{16} n₀⁴. ✓
* (i)–(iii) ⟺ q unramified with one Frobenius: q mod 8 is Frob on ℚ(ζ₈); (q/n) = (q/n₀) (q ∤ n automatic, q ≡ 3 (4))
  = (n₀/q) (n₀ ≡ 1 (4)) is Frob on ℚ(√n₀). One element of Gal(L/ℚ) ≅ (ℤ/2)³. ✓
* **Ahn–Kwon: VERIFIED from the primary text** (arXiv:1807.00508v1, downloaded to `sources/r239/`; = Ann. Inst. Fourier
  69 (2019) 1411–1458): "Theorem 1. For every finite extension K of ℚ, every finite Galois extension L (≠ ℚ) of K …
  every conjugacy class C of G, there exists a prime ideal p in P(C) [unramified, degree one over ℚ, Frobenius C]
  which satisfies N p ≤ d_L^{A₁} with A₁ = 12577." Abstract: "without any restriction". With K = ℚ this is exactly
  what is used. 12577·16 = 201232, 12577·4 = 50308; e* ≤ q − 3 < d_L^{12577} ≤ 2^{201232} n^{50308}. ✓ (Numbering:
  arXiv says "Theorem 1", author writes "Thm 1.1" — check the journal version; trivial.)
* Linnik–Xylouris (b): Xylouris' L = 5 (Bonn dissertation 2011) — NOT accessed by me; the exponent-5 statement is the
  standard citation and the effectivity of Linnik's implied constant is classical. Fine at "relative to cited theorems".
  Note the modulus can be 8n₀ (the conditions only see q mod 8 and q mod n₀) — e* ≪ n₀⁵; harmless.
* (c) GRH: **Bach–Sorenson** — primary text not accessible to me (AMS PDF behind bot-check; the CS tech-report
  #1180 link I found is a different paper). The abstract (fetched from ams.org) confirms: E/K abelian, ERH, degree-1
  prime with Frobenius σ and Np ≤ (1+o(1))(log Δ + 2n)²; for K = ℚ, p ≤ (1+o(1))(log Δ)²; explicit versions exist.
  The explicit form (4 log d_L + 2.5 n_L + 5)² is confirmed by a *secondary* source: Ahn–Kwon §1 ("Bach and Sorenson
  ([4]) … If GRH holds, then for any class C of G there is a prime p in K of degree 1 over ℚ with [L/K, p] = C and
  N p ≤ (4 log d_L + 2.5 n_L + 5)²"). Theorem number "5.1" unverified. Arithmetic: 4(16 log 2 + 4 log n₀) + 20 + 5 =
  16 log n₀ + 69.36 ≤ 16 log n + 70. ✓ L/ℚ is abelian, so even the abelian-only version applies.
* Citation defect: the GRH (log d_L)² theorem is **Lagarias–Odlyzko 1977** (Durham proceedings, "Effective versions of
  the Chebotarev density theorem"), not Lagarias–Montgomery–Odlyzko Invent. Math. 54 (1979), which is the
  UNCONDITIONAL d_L^{A} bound (Ahn–Kwon §1, Theorems I and II). See D1.
* Case (c) (odd squares): the author's restriction "under GRH only the Linnik-type bound" is unnecessary — see D3:
  applying Thm 1.1 to d := n/p (non-square, squarefree kernel p) and scaling by k = p removes all exclusions, so all
  three bounds of Thm 1.3 hold for odd squares with n₀ replaced by p.

### C6. Lemma 3.1 (cap = max_s (a_s − b_s)⁺) and Lemma 2.1 — SOUND
g + 1 = (n + 4Q² + m)/m = 4(K + Q²)/m, s ∤ 2m ⇒ σ_s = v_s(K + Q²) = min(b_s, 2a_s) if b_s ≠ 2a_s, ≥ b_s if equal.
Prop 1.2: v_s(Q₁) = (a_s − σ_s)⁺ = 0 if 2a_s ≤ b_s, = a_s − b_s if 2a_s > b_s (then a_s > b_s ⟺ …; when b_s < 2a_s ≤ 2b_s
the value (a_s − b_s)⁺ = 0, consistent). rad Q₁ | (g+1)/4 since σ_s = b_s ≥ 1 there. ✓ Cap 0 ⟺ Q | K. ✓
Lemma 2.1 is a restatement of Lemma 3.1 for the shot family at the window (correctly so scoped; the author's own
p = 241 example, which I re-checked exactly: 4/241 = 1/63 + 1/1446 + 1/30366, shows general Type II windows are wider).
Numerically: in all 39 760 exact checks below, the measured cap of the rebuilt solution (from den z) equals the
predicted max (a_s − b_s)⁺ of the minimising Q.

### C7. Numerics of §3/§4 — SOUND (all reproduced exactly, from scratch)
`scripts/review_r239_windows.py 1000000 1000 200` (own Jacobi, own sieve, own subgroup search, own exact Def 1.1
checker; no author code) → `data/review_r239_windows_1e6.txt`, 13 s:
* 39 175 primes p ≡ 1 (4) ≤ 10⁶; record q* = 227 at p = 867 793; max q*/log²p = 2.8353 at p = 4349 (q* = 199). ✓
* min cap at q*: 0: 24 266, 1: 9012, 2: 2448, 3: 912, 4: 699, 5: 998, …, max 41 at p = 575 717 (q* = 167). ✓
* the proof's own construction (−K)^{(o+1)/2} written in ⟨S⟩ with 0 ≤ a_s < ord_q(s): group step never failed,
  and its bound max a_s − 1 ≤ q − 3 held for every p. ✓
* best cap over Thm 1.1′ windows m ≤ 1000: 0: 32 043, 1: 6887, 2: 238, 3: 7 ✓; prime windows only: 0: 31 850,
  1: 7063, 2: 255, 3: 7 ✓. (Extra: over ALL odd m ≡ 4 − p (8), m ≤ 1000, incl. prime factors ≡ 1 (4): 0: 34 933,
  1: 4184, 2: 57, 3: 1.)
* exact Def 1.1 checks: 39 760 solutions (every q*-solution + every 200th best-window solution), all pass.
`scripts/review_r239_composite_squares.py 200000 100000000` → `data/review_r239_composite_squares.txt`:
* all 49 776 odd non-squares n ≡ 1 (4) ≤ 2·10⁵: least window ≤ 263 (n = 4701), min cap at it ≤ 55 (n = 37 933,
  q = 223), each solution exact-checked. ✓ (matches §4 bullet)
* 1073 odd squares a² ≤ 10⁸ with all primes ≡ 1 (4): no window at a² (T1 ✓), and the D3 route (Thm 1.1 at d = a²/p,
  scale by p) produces an exact ES^{(y,e)}(a²) solution in every case (worst q = 199).
