# R228 — hostile review of O225 (NEAR_SQUARE_EXIST.md, checkpoint 1)

**Repairs applied** (author quiet, no new commits on side-agent/near-square-exist after 305cf029): D1–D8 applied directly in
NEAR_SQUARE_EXIST.md, each marked "(R228 repair …)" / "(R228 …)", including the R228 proof of the u ≡ 1 (4) even-A case in
Remark 2.4; AGENT_REPORT_O225 aligned on D1/D2/D3 only (its §5/Sparks wording of S3 is already cautious).

Reviewer: R228 side agent (branch side-agent/review-near-square, merged side-agent/near-square-exist at 305cf029).
From-scratch scripts: `scripts/review_r228_*.py` (none reuses the author's `z2_*`). ES is not solved; nothing below changes that.

**Overall: no FATAL defect.** The mathematics of Prop 1.1, Thm 2.1, Cor 2.2/2.3 and §5.1 is correct and every checkable
number reproduced with independent code. Four MAJOR defects: a definitional one that makes the k ≡ 1 (4) case vacuous
(D1), an even-A overclaim it hid (D2), a PROVED label on a heuristic consequence (D3), and a false side-statement about
congruence coverage at ℓ = 11, 13 (D4). Bonus: the u ≡ 1 (4) even-A case the author left as EVIDENCE is PROVED below.

## Verdict summary

| claim | verdict |
|---|---|
| Prop 1.1 (u-side T1, all u) | SOUND |
| Thm 2.1 (sign-field criterion) | SOUND-AFTER-REPAIRS (D1: genericity must ignore the prime 2) |
| Cor 2.2 (t-side: tk + 1 = □) | SOUND (odd A; after D1) |
| Cor 2.3 (u-side table) | SOUND (table = direct criterion on 12 000 levels; after D1) |
| Remark 2.4 (even A) | SOUND only for k ≡ 0 (4); false for k ≡ 1 (4) under repaired genericity (D2); u ≡ 1 (4) gap closed by R228 proof |
| Pointwise form | SOUND |
| §3 EVIDENCE | SOUND (prime-by-prime match on two subranges; residuals reproduced); D5 reporting |
| §4.1 | SOUND |
| Lemma 4.2 | group statement SOUND; consequences are Assessment, not PROVED (D3) |
| §4.3 E1–E4 | correctly labelled; algebra checked (minor slip in E1) |
| §5.1 3-parameter family | SOUND (sympy, incl. converse) |
| §5.2 inert-prime observation | GAP (D4 false "ℓ ≤ 13 covered"; D7 overstatement) |
| Novelty | real but modest: p-independent sign field Σ_M; cite (J)50 §3, O230 Prop C (D6) |

## Defects (each with location and repair)
* **D1 (MAJOR)** §2 "Call m generic if gcd(m, b) = 1": for k ≡ 1 (4) every odd level has no generic m (m even, b even),
  so (b) and Remark 2.4 are vacuous there and the "iff" of Thm 2.1/Cor 2.2/2.3 is literally false (50/100 u-levels,
  40/80 t-levels at k = 1 and k = 9). Repair: "generic ⟺ m and b have no common odd prime"; the proof of (b) is unchanged.
* **D2 (MAJOR)** Remark 2.4 and AGENT_REPORT ("even A: t-side fully"): with D1's repair, even-A χ = −1 words occur on
  sign-clean odd levels for k ≡ 1 (4): t-side k = 1, t = 3, p = 37, word (3, 1, 19), A = 2; u-side k = 9, u = 3, p = 109,
  word (1, 3, 56), A = 2. Repair: restrict Remark 2.4 to k ≡ 0 (4) and state the k ≡ 1 (4) counterexamples; add the
  R228 proof for u ≡ 1 (4) (K odd), so for k ≡ 0 (4) the u-side classification covers all words.
* **D3 (MAJOR, label)** §4.2: the lemma is PROVED; "only A = N can be forced" and "every level-by-level mechanism is a
  congruence covering" need realisability of Frobenius patterns of the factors of N(m) in every class (unproved) and a
  definition of "mechanism". Relabel those consequences Assessment.
* **D4 (MAJOR)** §5.2 "For ℓ ≤ 13 classical congruence families cover these classes": known only for ℓ ∈ {3, 5, 7};
  open at 11, 13 (M13B Thm 3.1 leaves 6 classes; M13E's x** survives), conditional at 17. Repair as in §5.2 below.
* **D5 (MINOR)** §3: "40–50 %" → bin-dependent (23 % at [17, 30), ≈ 40 % at [30, 300), 94 % at [10, 17)); report the
  K0 = 1 overshoot (→ +0.016 ± 0.008) and the unmoved K0 ∈ [2, 5).
* **D6 (MINOR)** §2 Reading / §4.1: cite (J)50 §3 (BRIDGE_WORLDS: genus failure ⟺ odd quadratic character trivial on all
  q | M) and O230 Prop C next to "Frob = c_∞".
* **D7 (MINOR)** §5.2 "'⊆' … requires polynomial families in m to cover classes that no congruence family in n covers"
  → "may require" (sterile points of (J)54 are not shown to lie in the closure of {m² − j}).
* **D8 (MINOR, assorted)** E1 "v < m" → "v ≤ m + k + 2, and for m > k² + 4k + 3 only v = m − k² − 2k"; §4.2 "Thm 2.2 / B1"
  → "NEAR_SQUARE Thm 2.2 / B1"; §4.2 σ_N needs N prime to the conductor (use the odd part); §5.1 "Every (1,0,1) Λ = 1
  family" → "with f non-constant"; Thm 2.1(a) can be strengthened to "χ = −1 words at the level for a density-1 set of m"
  (CRT), worth saying since it sharpens "Chebotarev lottery".

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

### §5.1 Type I (1,0,1), Λ = 1 parametrisation — SOUND (verified symbolically)
`review_r228_family.py` (sympy): with n = m² − j, c = −α n(x), a = λ(m − x) + α, d = (m − x)/(4cλ) − 1/(4α²):
f = 4acd − n ≡ κ(m − x) identically with κ = α/λ + λn(x)/α − 2x; na + c and 4a²d + 1 vanish at m = x, so are divisible
by f in ℚ[m] ✓. Converse ("every (1,0,1) Λ = 1 family is of this form"): solving [m²]f = 0, (4a²d + 1)(x) = 0,
(na + c)(x) = 0 for a linear d, constant c returns exactly the stated c and d (unique solution); f(x) = 0 then holds
automatically ✓. (This presupposes f linear with a root x ∈ ℚ; the degenerate case f constant is not covered by "every"
— MINOR, say "with f non-constant".) The "only finitely many 5.1-families through a given solution" degree-count claim
is not proved (stated in a NOT DONE paragraph; fine).

### §5.2 inert-prime observation — GAP (D4, MAJOR: a false side-statement) + overstatement
* Correct part: at inert ℓ, j is a non-residue, ℓ ∤ n(m), and (NEAR_SQUARE Thm 3.4 Remark (i)) m ∈ Z_K⁺ at ℓ ⟺ n(m) is
  an ℓ-adic square ⟺ n(m) is a QR mod ℓ ✓. (J)54 (STERILE_EXPLICIT Thm 3.4) is quoted correctly: for primes r ≥ 2³² no
  finite set of ET Prop 1.9 classes covers all large primes with least non-residue r.
* **D4 (MAJOR).** "For ℓ ≤ 13 classical congruence families cover these classes" is FALSE as a statement of known
  fact for ℓ = 11, 13 (both inert for j = 8). Mordell's 840 theorem covers non-residues at 3, 5, 7 only; for 13 the
  campaign's own POINTWISE_MORDELL13B Thm 3.1 leaves 6 classes mod 720720 uncovered among (p/13) = −1, and
  POINTWISE_MORDELL13E (CERTIFIED) shows x** survives every ET class of T-level ≤ 161050 — a candidate sterile point
  with (p/11) = (p/13) = −1; r = 17 is CONDITIONAL (M17). Repair: "for ℓ ∈ {3, 5, 7} (Mordell 840) classical congruence
  families cover these classes; at ℓ = 11, 13, 17 coverage is open (M13B/E, M17), and for ℓ ≥ 2³² it provably fails
  ((J)54)". This strengthens the author's own caveat: "⊆" at inert ℓ is already delicate at ℓ = 11, 13.
* Overstatement (MINOR): "'⊆' at large inert ℓ *requires* polynomial families in m to cover classes that no congruence
  family in n covers" does not follow. (J)54's sterile points live on the r-generic line in n-space; the values
  n = m² − j with m ∈ Z_K⁺ at all primes ≠ ℓ form a thinner set, and nobody has shown that its closure contains a sterile
  point, i.e. congruence families might still cover all n of the form m² − j there. Say "may require … unless the
  sterile points of (J)54 avoid the closure of {m² − j}"; the report's Spark S3 already phrases it as a question.
* §5.3 (inconclusive 17-adic test): correctly labelled; not rechecked (no claim to check).

### Novelty (Assessment)
* Frob = c_∞ for admissibility is (J)50 (BRIDGE_WORLDS §3: "h ≡ −1 (mod m) ⟺ Frob_h = c_∞"; Type II ⟺ a sub-product of
  the primes of M has symbol c_∞; on 2-group slices "failure ⟺ some odd quadratic character mod 4cd is 1 on all q | M" —
  which is the pointwise genus form in another guise: odd character = imaginary F). O230 Prop C encodes the sign by
  adjoining √p (p-dependent field K_M = ℚ(ζ_M, √p), Frob = c_∞σ_p). O225's genuinely new ingredient is to encode the sign by
  √−M instead, via the reciprocity (r/p) = (−M/r) valid for r | p + u (resp. tp + 1): the sign field Σ_M is
  p-independent, which is exactly what makes a family statement (F vs Σ_M, Chebotarev in the fixed field FΣ_M) possible.
  The proofs are classical genus/class-field theory of abelian fields; Cor 2.2/2.3 are new explicit computations in that
  frame and Remark 2.4 (u ≡ 3) plus the R228 proof for u ≡ 1 complete the u-side for k ≡ 0 (4). The text should cite
  (J)50 §3 and O230 Prop C next to "the Frob = c_∞ of (J)50" (MINOR, D6).
* "the obstruction is always … positivity once more ((J)52)" is a reading (Assessment), fine as worded.
* Not rechecked: the sentence "most of [the new u-levels] are not clean in the sense of THREE_SQUARES" (plausible, untested).
