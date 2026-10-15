# R228 — hostile review of O225 (NEAR_SQUARE_EXIST.md, checkpoint 1)

Reviewer: R228 side agent (branch side-agent/review-near-square, merged side-agent/near-square-exist at 305cf029).
From-scratch scripts: `scripts/review_r228_*.py` (none reuses the author's `z2_*`). ES is not solved; nothing below changes that.

(Verdict table and defect list at the end; written claim by claim.)

## Claim-by-claim

### Prop 1.1 (u-side T1, all u) — SOUND
Re-derived. p + u = x² + y², gcd(x, y) = 1 ⇒ 4 ∤ N and every odd prime of N is ≡ 1 (4).
* u even: N odd ⇒ every divisor ≡ 1 (4), so N ≡ 1 (4) ⇒ u ≡ 0 (4) and A = tu − 1 ≡ 3 (4) cannot divide N. No word. ✓
  (The v = u mirror is the same with A* = tv − 1.) The "too easy" worry is unfounded: the statement is genuinely
  vacuous for even u, and the author says so ("clean only vacuously"). The remark "4 | u is exactly the level where
  every word has χ = −1" is the sign table (u ≡ 0 mod 4), correct.
* u odd: N ≡ 2 (8) ⇒ u ≡ 1 (4); A odd ⇒ A ≡ 1 (4), v ≡ 2 (4), t ≡ 2 (4), A* odd; A even ⇒ A ≡ 2 (4), v ≡ 1 (4)
  (N/2 ≡ A/2 ≡ 1 mod 4), t ≡ 3 (4), A* ≡ 2 (4). None of t, u, v, A, A* is ≡ 0 (4) ⇒ χ = +1 by the DK table. ✓
* From scratch (`scripts/review_r228_prop11.py 200000`, Euler-criterion χ, own SPF sieve, coprime-two-squares test
  validated against brute force for n < 3000): 8 977 primes p ≡ 1 (4) < 2·10⁵, 1 103 693 ordered words (both
  orientations): **0 sign-table mismatches; 28 886 words with p + u a coprime two-square sum, 0 with χ = −1, 0 with
  that u even.** Agrees with the author's 10⁷ run in kind.
* Relation to R225: R225 had proved odd u only and left even u open; Prop 1.1 closes it correctly.

### Thm 2.1 (sign-field criterion) — SOUND-AFTER-REPAIRS (one MAJOR definitional defect, D1)
Re-derived line by line.
* Sign identity: t-side r | tp + 1 ⇒ p ≡ −t⁻¹ (r), (r/p) = (p/r) = (−t/r); u-side r | p + u ⇒ (r/p) = (−u/r). So
  χ(A) = (−M/A) (Jacobi). This also holds for composite n ≡ 1 (4) with χ := Jacobi (A/n) (gcd(A, n) | M and A ≡ −1 mod M
  ⇒ gcd = 1; Jacobi reciprocity) — relevant because §2's brute force runs over composite n.
* (i)/(ii): Σ_M ⊂ ℚ(ζ_{4M}), A odd and prime to M is unramified, σ_A is defined; σ_A(√−M) = (−M/A)√−M because the
  Kronecker character of ℚ(√−M) agrees with Jacobi (−M/·) on odd positive integers prime to M. ✓ So "admissible and
  χ = −1 ⟺ σ_A = c_∞|Σ_M" is correct.
* (b): odd r | A divides N(m), r ∤ ab under genericity, so (−ab/r) = 1 (a²m² ≡ −ab), r splits in F, σ_A ∈ Gal(Σ_M/F);
  c_∞ moves F. ✓ The proof only uses ODD primes r — see D1.
* (a): F, Σ_M depend on (k, side, M) only, never on m, so Chebotarev in the fixed abelian field FΣ_M (F ∩ Σ_M = ℚ since
  F is quadratic and F ⊄ Σ_M) is legitimate; r split in F gives two roots of am² + b mod r; A = r gives a word for
  EVERY m in those classes (N(m) ≥ r automatically, so "all large m" is unnecessary). ✓ Quantifier remark: by CRT the
  m avoiding the bad classes for all such r ≤ R have density ∏(1 − 2/r) → 0, so at a dirty level the χ = −1 word
  exists on a set of m of density 1 (not just "a positive density of classes"); the statement is weaker than what is
  true, not wrong. Of course this is about m, not about primes n = m² + k (Bunyakovsky), which the text does not claim.
* **D1 (MAJOR, definitional).** "Generic" is defined as gcd(m, b) = 1. For k ≡ 1 (mod 4) (incl. k = 1, 9) n ≡ 1 (4)
  forces m even, while b = k + u (u odd) resp. b = tk + 1 (t odd) is even: **there is no generic m at all** on every odd
  level. Then Thm 2.1(b) and Remark 2.4 hold vacuously there, and the "iff" of Thm 2.1 / Cor 2.2 / Cor 2.3 is literally
  FALSE (such levels are vacuously "sign-clean" while the criterion says dirty): 50 of the u ≤ 100 levels and 40 of the
  t ≤ 80 levels for k = 1 and for k = 9 (`review_r228_signfield.py`, "levels with NO m satisfying the literal gcd").
  The author's z2_classify.py with the gcd option has the same vacuity. Repair: define generic as "m and b have no
  common ODD prime" — the proof of (b) only needs that, and with this definition my brute force (below) confirms (b)
  for odd A on all those levels. But with the relaxed definition the even-A remarks break, see Remark 2.4.

### Cor 2.2, Cor 2.3 — SOUND (as statements about odd A, after D1)
* Cor 2.2 proof checked (ℚ(√c₀) ⊂ ℚ(ζ_{4t}) ⇒ sqfree(c₀) | 2 since gcd(c₀, t) = 1; c₀ = 2s² ⇒ t odd ⇒ √2 ∉ ℚ(ζ_{4t})).
  Only a necessary condition (⊂ ℚ(ζ_{4t})) is used for "⇒", fine.
* Cor 2.3 2-adic table: checked against an INDEPENDENT direct character computation (enumerate c mod 4uD with
  c ≡ 1 (u), (−u/c) = 1, test Kronecker (−D/c) = 1; no reciprocity bookkeeping) — `review_r228_cor23wide.py`:
  all k ≤ 60 × u ≤ 200 (12 000 u-levels) and k ≤ 60 × t ≤ 120 (7 200 t-levels, vs "tk + 1 = □"): **0 mismatches**.
* k = 24 lists reproduced exactly (u: 1, 3, 8, 12, 24, 25, 26, 30, 40, 48, 51, 57, 72, 74, 76, 84, 97 for u ≤ 100;
  t: 1, 2, 5, 7, 12, 15, 22, 26, 35, 40, 51, 57, 70, 77).
* Brute force (`review_r228_signfield.py 1,4,8,9,16,24 100 80 300`; χ = Jacobi(A/n), all n incl. composite, my relaxed
  genericity, every divisor of N(m) in the admissible class): **0 predicted-clean levels with an odd-A χ = −1 word**
  (k ∈ {1, 4, 8, 9, 16, 24}, u ≤ 100, t ≤ 80, m ≤ 300). Predicted-dirty levels not yet dirty at m ≤ 300: 4–13 per
  (k, side), the first suitable r being large — same phenomenon the author reports. DK table re-confirmed on all
  prime n in that run (0 mismatches).

### Remark 2.4 (even A) — SOUND only under the literal (vacuous) genericity; GAP closable for u ≡ 1 (4) (proof below)
* u ≡ 3 (4) argument re-derived: Σ_u = ℚ(ζ_u) (−u ≡ 1 mod 4), σ_{A₀}|ℚ(ζ_u) = σ_{−2^{−a}} must fix F; a even ⇒
  contradiction; a odd ⇒ 2 inert in F ⇒ K₀ ≡ 3 (8). The step "N ≡ 4 (8)" needs **K odd, i.e. k ≡ 0 (4)** (then m odd,
  f odd, N = m² + K ≡ 1 + 3 = 4 mod 8). For k ≡ 1 (4), K is even and literal genericity excludes every m — vacuous.
* With the repaired (odd-prime) genericity of D1 the even-A claims are FALSE at k ≡ 1 (4) (`review_r228_evenA.py`, prime n
  only, Euler χ cross-checked with the DK table):
  – t-side, k = 1, t = 3 (tk + 1 = 4 = □): p = 37 = 6² + 1, word (t, u, v) = (3, 1, 19), A = 2, χ = (2/37) = −1;
    190 such words at prime n, m ≤ 400 (A = 2 whenever (2/p) = −1, i.e. m ≡ 2 mod 4). Also k = 1, t = 35; k = 9, t = 11, 75.
  – u-side, k = 9, u = 3 (u ≡ 3 mod 4, K = 12, F = ℚ(√−3) ⊂ Σ_3): p = 109 = 10² + 9, word (1, 3, 56), A = 2,
    χ = (2/109) = −1; 130 such words; also u = 39, 99.
  So the report's "even A: t-side fully" holds only because those levels have no literal-generic m. **D2 (MAJOR,
  overclaim):** state Remark 2.4 (both sides) for k ≡ 0 (mod 4) (K resp. c₀ odd), and say explicitly that for k ≡ 1 (4)
  on odd levels only odd-A words are sign-clean (even-A χ = −1 words do occur, e.g. A = 2 at t = 3, k = 1).
  (For k ≡ 0 (4), t odd: tk + 1 = c² forces 8 | k, so (2/p) = +1 and Prop 4.1(a)'s prime 2 is fine — the t-side claim is
  then true, as the author says.)
* **u ≡ 1 (4), K odd (the author's EVIDENCE case) — PROVED here (R228), offered as a repair.** Then N ≡ 2 (4), A = 2A₀,
  A₀, v odd, t = (A + 1)/u ≡ 3 (4); by the DK table χ = −1 ⟺ 4 | A* = tv − 1 ⟺ v ≡ 3 (4). Now v·A = N and A ≡ −1 (mod u)
  give v ≡ −N (mod u); F = ℚ(√−K₀) ⊂ Σ_u gives K₀ | u (Cor 2.3(a), K₀ odd squarefree) and, u ≡ 1 (4), either
  K₀ ≡ 1 or 3 (4). Every prime of v splits in F (generic m), so χ_F(v) = 1.
  – K₀ ≡ 3 (4): χ_F(v) = (v/K₀) = (−N/K₀) = (−m²/K₀) = (−1/K₀) = −1 (N ≡ m² mod K₀, gcd(m, K₀) = 1): contradiction —
    there are NO even-A words at all.
  – K₀ ≡ 1 (4): χ_F(v) = (−1/v)(v/K₀) = (−1/v)(−1/K₀) = (−1/v), so v ≡ 1 (4) and χ = +1. ∎
  Brute force agrees (`review_r228_evenA2.py`: all k ≡ 0 (4) ≤ 60, predicted-clean u ≤ 150, odd m ≤ 400, all n:
  67 levels with u ≡ 1 (4) carrying 3 065 even-A words, 18 levels with u ≡ 3 (4) carrying 840; **0 with χ = −1**).
  Hence for k ≡ 0 (4) Cor 2.3 is a classification for ALL words; suggested wording accordingly.
