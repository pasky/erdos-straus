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

### Pointwise form (end of §2) — SOUND
Proof of Thm 2.1(b) indeed uses only the single m (one prime p): odd r | A ⇒ r | p + u ⇒ r splits in F by hypothesis.
No genericity needed in the pointwise form (the hypothesis "F splits every odd prime of p + u" replaces it). ✓

### §3 EVIDENCE (pointwise genus cleanness, residual shrink) — SOUND (reproduced), two reporting remarks
* From scratch (`review_r228_genus.py`: sympy factorisation, admissible F decided by a DIRECT character test in
  Gal(ℚ(ζ_{8u})/ℚ) — not by the Cor 2.3 table —, own t-clean test): per-prime (N, N₋, Ncl, Nfl, Nflm) on
  p ∈ (10⁵, 1.1·10⁵) (422 primes, 55 326 words, 4 924 flagged beyond clean) and p ∈ (5·10⁶, 5.01·10⁶) (312 primes,
  66 852 words, 5 602 flagged): **identical to z2_hardness.c prime by prime; 0 flagged words with χ = −1.**
* z2_hardness.c rerun on (10⁵, 10⁶): totals 5 570 014 / 432 677 / 481 272 / 0, as stated.
* Residuals recomputed with my own cell/residual code (`review_r228_resid.py`, on the z2_hardness output validated above):
  every quoted number reproduced ([10,17) −0.0235 → −0.0014; [17,30) −0.0193 → −0.0149; [30,100) −0.0093 → −0.0059;
  [100,300) −0.0045 → −0.0025; ≥300 +0.0022 → +0.0013; [5,10) → −0.0359 ± 0.0062; K0 = 24 → −0.058).
* Remarks (MINOR, D5): (i) "40–50 %" holds for [30, 300); [17, 30) is only 23 %, [10, 17) 94 % — say "21–94 % by bin,
  ≈ 40 % in the two best-populated bins". (ii) Unreported small bins: K0 = 1 overshoots (−0.0081 → **+0.0159 ± 0.0083**,
  flagged fraction residual +0.021) and K0 ∈ [2, 5) does not move (−0.0112 → −0.0110). Both should be in the table: the
  K0 = 1 overshoot says that at K0 = 1 the genus flag over-corrects, i.e. it is not a calibrated "explanation" there.

### §4.1 Galois form of ES-five — SOUND (restatement of Thm 2.1(i)/(ii) for odd A; σ_N in §4.2 is defined only when N is
prime to the conductor of Σ_u — for even N and u ≢ 3 (4) "σ_N" needs the odd part; MINOR wording).

### §4.2 Lemma (single-level forcing) — group statement SOUND; its application is Assessment, not PROVED (D3, MAJOR label)
* The lemma: x ≠ 1 forced by s ⟺ x = s. Proof re-done: "⇐" take the whole multiset; "⇒" the multiset {s} has sub-products
  1 and s only. ✓ Trivial but correct. |Gal(Σ_M/ℚ)| = 2 for M ∈ {1, 2, 3, 4} ✓ (ℚ(i), ℚ(√−2), ℚ(√−3), ℚ(i)). t = 3:
  odd A ≡ 2 (3) ⇒ χ = (−3/A) = (A/3) = −1 ✓; forced iff v₂(3p + 1) odd ✓ (odd part ≡ (−1)^e mod 3).
* **D3 (MAJOR, label).** The step from the lemma to "the only χ = −1 word a congruence condition on N(m) can force is
  A = N" and to "every deterministic mechanism working level by level is a congruence covering" needs REALISABILITY:
  for every m-class in which σ_N(m) ≠ c_∞ one must exhibit m in the class whose prime factors of N(m) have a Frobenius
  multiset avoiding c_∞ in all sub-products (e.g. N(m) = r × primes with trivial symbol). That is a
  Chebotarev-in-polynomial-values / almost-prime statement for m² + K with prescribed Frobenius of every factor — not
  proved anywhere in the document (and not known in this strength). Moreover "mechanism" is undefined (a mechanism could
  use sizes of divisors, several levels at once, or the actual integer N(m)). Repair: keep "Lemma 4.2 (PROVED)" for the
  group statement only; label the two consequences "Assessment (heuristic: assumes every Frobenius pattern compatible
  with σ_N is realised in every class)". The "Thm 2.2 / B1" reference should read "NEAR_SQUARE Thm 2.2 / B1" (this
  document has no Thm 2.2) — MINOR.

### §4.3 E1–E4 — correctly labelled (iteration log + Assessment); algebra re-checked
* E1: p + u = (m + a)(m + b) for u = (a + b)m + ab − k ✓. a = 0, b = 1: v ≡ −k(k + 1) (mod m − k) ✓. "v < m" is not
  quite right (A ≥ u − 1 gives only v ≤ m(m + 1)/(m − k − 1) ≈ m + k + 2), but the next candidate 2(m − k) − k(k + 1)
  exceeds that bound once m > k² + 4k + 3, so the conclusion (v = m − k² − 2k, finitely many m) stands — MINOR.
* E2: (r/p) = (k/r) for r | m ✓; r(js − k) = k + s with s = (r + 1)/t gives r ≤ k + s, s ≈ k/j ⇒ bounded r ✓.
* E3: u ≡ −(c² + k) (mod A) and u | A + 1 ⇒ u = A − c² − k with u | c² + k + 1 (or bounded A when u > A) ✓.
* E4: the density-0 statement is CRT-exact (∏(1 − |G_r|/r) → 0 since Σ τ(r + 1)/r ≍ log² R, Titchmarsh) ✓;
  Z_k^□ (NEAR_SQUARE: m² + k a local square everywhere) has (p/r) = +1 for all r, while G_r needs (p/r) = (−u/r) = −1 ✓.
* The overall "Conclusion for goal 4" is labelled Assessment ✓; with D3 it should not lean on Lemma 4.2 as if proved.
