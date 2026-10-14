# R212 — hostile review of O212 FOUR_SPECIFIC.md (+ BRAINSTORM/y4_*.md, AGENT_REPORT_O212)

Reviewer worktree branch `side-agent/review-four-specific`, merged `side-agent/four-specific` at c82ebf63.
From-scratch scripts: `scripts/review_r212_*.{py,c}` (none of the author's `y4_*` code reused).

## Summary verdicts
(filled in as the review proceeds; see per-claim sections)

| claim | verdict |
|---|---|
| Prop 1.1 / Cor 1.2 (T1 ⟺ M ≡ 0, 3 mod 4; M^□ at non-squares for all M) | SOUND (one sign typo in memo, D1) |
| 7/p failure-free to 10⁸, T1-bearing; S₇(p) = ∅ at 10 primes; Type II of 7 fails 9×; 11/37 | SOUND (independently re-verified to 10⁸) |
| Lemma 2.1 + census of §2 (S₄^{odd}, S₈, squares, composite list, one-odd halves) | SOUND (re-verified ≤ 10⁶ / 2·10⁵) |

---

## C1. Prop 1.1 / Cor 1.2 — T1-bearing numerators

**Re-derivation.** Write ψ(g) = (−M/g) (Jacobi, g odd > 0, g ≡ −1 mod M, so gcd(g, M) = 1).
* M ≡ 3 (4): ψ(g) = (−1/g)(M/g) = (−1/g)·(g/M)·(−1)^{((M−1)/2)((g−1)/2)} = (−1/g)·(−1/M)·(−1/g) = (−1/M) = −1. ✓
* M ≡ 0 (4): O208 (∗) — re-checked: (4/g)=1, 8 | M ⇒ g ≡ 7 (8), odd ℓ | M gives (ℓ/g) = 1, (−1/g) = −1. ✓
* M ≡ 1 (4): ψ(g) = (−1/g)(−1/M) = (−1/g); odd g ≡ −1 (M) are g = 2Mi − 1, and g ≡ 3 or 1 (mod 4) as i is even or odd. Non-constant. ✓ (M = 9, 25: still fine since (9/g) = 1.)
* M = 2M′ ≡ 2 (4): g ≡ −1 (mod 2M′) leaves g mod 8 free (M′ odd); (M′/g) depends only on g mod 4·M′ through g mod 4 and g mod M′, while (−2/g) is 1 at g ≡ 1 and −1 at g ≡ 5 (mod 8). Non-constant. ✓
The set {g : ψ(g) = s} is a union of coprime classes mod 4M (ψ is 4M-periodic), so Dirichlet gives primes in either sign class when ψ is non-constant.

**Cor 1.2 (a), M^□ at odd non-squares n prime to M, every M ≥ 3.** Fix g mod 4M in the class −1 (mod M); (−M/g) =: s is then fixed. (n/g) = (n₀/g) = (g/n₀)·ε(g mod 4) with n₀ > 1 odd squarefree, gcd(n₀, 4M) = 1, so CRT + non-triviality of (·/n₀) + Dirichlet give a prime g ∤ 2n with **(n/g) = s = (−M/g)**, i.e. (−Mn/g) = 1, −n/M ≡ σ² (g). Q ≡ ±σ (g), Q odd, Q prime to n (CRT), Lemma 1.0 ⇒ M^□(n). ✓ SOUND.
*Note:* the memo `y4_t1_numerators` Cor 2(a) writes "(n/g) = −(−M/g)" — wrong sign (D1). The FOUR_SPECIFIC text only says "(Dirichlet)", so the main document is unaffected.

**Cor 1.2 (b), T1 for odd g when M ≡ 0, 3 (4).** Every prime ℓ | k² + MQ² (k² odd, gcd(k, M) = gcd(Q, k) = 1) with ℓ odd has ℓ ∤ MQ and (−M/ℓ) = 1, so every odd divisor g has (−M/g) = 1, contradicting ψ ≡ −1. ✓. Even-g remark: an even g ≡ −1 (mod M) needs M odd; for −M a discriminant the Kronecker symbol χ_{−M} is a character mod M (even when −M is non-fundamental, e.g. M = 27), χ_{−M}(−1) = −1, χ_{−M}(2) = +1 iff M ≡ 7 (8); hence even g are impossible for M ≡ 7 (8) and possible for M ≡ 3 (8) (M = 3: g = 2 | 25 + 3). ✓

**Converse (no T1 for M ≡ 1, 2 mod 4), explicit shots at odd squares** (prime g ≡ −1 (M) with (−M/g) = +1, Lemma 1.0
recomputed and verified in exact rationals, den(z) an odd square prime to n):
* M = 5, g = 29, n = 49, Q = 5: 5/49 = 1/11 + 1/294 + 25/3234.
* M = 9, g = 17, n = 49, Q = 15: 9/49 = 1/19 + 1/98 + 225/1862.
* M = 6, g = 5, n = 49, Q = 1: 6/49 = 1/10 + 1/49 + 1/490 (here even a genuine unit-fraction solution).
* M = 10, g = 19, n = 9, Q = 1: 10/9 = 1/1 + 1/18 + 1/18.
In `review_r212_t1.py` (3) this is done for every M ≡ 1, 2 (mod 4), 5 ≤ M ≤ 38, at 11 odd squares each: all succeed.

**Numerics (from scratch, `scripts/review_r212_t1.py`, < 1 s).**
(1) Jacobi constancy of (−M/g) on odd g ≡ −1 (M), g < 40M, for M = 3..80: constant −1 exactly for M ≡ 0, 3 (4); 0 mismatches.
(2) Brute force odd squares k ≤ 59, Q ≤ 29, all g ≡ −1 (M): odd-g shots = 0 exactly for M ≡ 0, 3 (4) (M = 3..40); even-g
shots occur exactly for M ≡ 3 (8) (3, 11, 19, 27, 35) and odd M ≡ 1 (4) — matches the memo's statement.
(4) Cor 1.2(a) construction carried out and verified for all M = 3..30, odd non-squares n < 400 prime to M (4275 cases).
(5) 11/37 = 1/8 + 1/148 + 49/296: exact identity ✓ (unit-fraction insolubility checked in C2).

**Verdict C1: SOUND.** The label PROVED is right; it is elementary and (as the author says) folklore-level — the
"discriminant" reformulation is just "χ_{−M} has modulus M and is odd". Minor presentational point (D2): Cor 1.2's "for
M ≡ 1, 2 (mod 4) the relaxation holds at squares too" should say "*the shot mechanism* reaches every odd square prime to
M"; M^□ itself holds at most odd squares for *every* M by non-shot solutions (SYNTHESIS_SPARKS3 Rem (o): 8/9).

---

## C2. The control numerator 7; 3, 5, 6; 11/37 (§1 last line, §5, y4_seven_control)

**Source of "failure-free ≤ 10⁸".** It is the MODEL_SPECIFIC §1 census ((J)32, `ms_census.c`, `data/ms/prime_fail_1e8.txt`,
reviewed by R197), not a new O212 computation. I re-did it from scratch.

**Own exact solver** `scripts/review_r212_census.c`: complete search x ∈ (p/M, 3p/M], A = Mx − p, B = px reduced by the gcd,
(A′y − B′)(A′z − B′) = B′², all divisors d ≤ B′ of B′² with d ≡ −B′ (mod A′), every hit re-verified in 128-bit
(Mxyz = p(yz + xz + xy)); x < p for M ≥ 4 so a solution is Type I iff p divides exactly one of y, z, Type II iff p | y, z.
Calibration: M = 8 fails exactly at {3, 11, 17, 131, 241} (≤ 10³, and Type I fails exactly there, as in MODEL_SPECIFIC);
M = 9: {5, 11, 19}; M = 10: {3, 7, 11, 43, 61, 67, 181}; M = 11 fails at 37 (≤ 10³: 2 failures) — all ≤ 10⁶ and matching
the MODEL_SPECIFIC table.

| M | range (primes p ∤ M) | failures | Type-I-free primes | Type-II-free primes |
|---|---|---|---|---|
| 3 | ≤ 10⁶ | 0 (trivial) | — | — |
| 4 | ≤ 10⁸ | 0 | 0 | 0 |
| 5 | ≤ 10⁸ | 0 | 0 | 0 |
| 6 | ≤ 10⁸ | 0 | 0 | 13 |
| 7 | ≤ 10⁸ (5 761 453 primes, 11 s) | **0** | **0** | **9**: 3, 31, 43, 127, 211, 421, 463, 631, 12601 |

So "7/p failure-free to 10⁸" ✓, "Type I of 7 never fails (≤ 10⁶)" ✓ (in fact ≤ 10⁸), "Type II fails 9 times" ✓ (same
9 primes, and none further to 10⁸). T1-bearing: C1 (M = 7 ≡ 7 mod 8, T1 for all g). The list "T1-bearing and failure-free
to 10⁸: 3, 4, 7" is consistent with the MODEL_SPECIFIC table (8, 11, 12, 15, 16, 19, 20, 23, 24 all fail; 23 only
checked to 10⁷ but fails at 31771) plus PW §6 (every m ∈ [16, 30000], m ≠ 19, has a failing prime in (m², 2m²)); for
T1-bearing M > 30000 nothing is known, so the statement should read "among M ≤ 30000" (D3, MINOR).

**S₇(p) = ∅ at 10 primes ≤ 10⁵.** Own complete word enumerator `scripts/review_r212_slices.c` (t = 1: (u−1)(v−1) = n+1;
t = 2: (2u−1)(2v−1) = 2n+1; t ≥ 3, u ≤ v; slice solutions rebuilt from the Lemma 3.0 formulas and verified exactly):
S₇(p) = ∅ exactly at **43, 127, 211, 421, 463, 631, 967, 4201, 9661, 12601** (10 primes, last 12601) ✓. Calibration: m = 4: 0,
m = 5: 0, m = 6: 25 (p ∤ 6), m = 8: 23 (last 83449) — all equal MODEL_SPECIFIC §3. 7/p is solvable at all ten ✓.
*Observation (new, harmless):* 7 of the 10 S₇-empty primes (43, 127, 211, 421, 463, 631, 12601) are exactly the 7/p Type-II
failures > 31. The "282/386 mixed feature classes" test was not re-run (it is a finite feature test, labelled as such).

**11/37.** 11/37 = 1/8 + 1/148 + 49/296 holds exactly; den 296/49 → den(z) = 49 = 7², odd square prime to 37 ✓ (M^□).
`review_r212_census 11 0 37`: complete search, **no** solution of 11/37 in unit fractions ✓. 11 ≡ 3 (mod 8): even g are
possible, but this shot uses g = 43 odd ✓ (43 ≡ −1 mod 11, 43 | 37 + 11·196 = 2193 = 43·51 ✓).
"11/37 < 3, so not a trivial size failure" ✓.

**Verdict C2: SOUND.** Labels (EVIDENCE/CERTIFIED for censuses) appropriate.

---

## C3-pre. §2 numerics and Lemma 2.1 (re-verified)

**Lemma 2.1, by hand.** n odd. (T) t = 4c: n ≡ u + v (2) ⇒ one of u, v even (say u); denominators uvc, ucn (even),
vcn ≡ c: one odd ⟺ c odd ⟺ v₂(t) = 2, else all even. (U) u = 4w: v odd; w odd ⇒ tnw ≡ t, wf ≡ tv − 1 ≡ t − 1, tnwf even ⇒
exactly one odd; w even ⇒ all even. (I) 4 | A ⇒ t, u odd, d = A/4: denominators A*dn, vd, A*vd; for d odd the odd ones are
those among A* = tv − 1, v, A*v that are odd; A* ≡ v + 1 (2) ⇒ exactly one ⇒ one-odd; d even ⇒ all even. (I′), (V) by
u ↔ v. ✓ PROVED.

**Census re-run** (`review_r212_slices`, `review_r212_census … odd`):
* S₄^{odd}(p) ≠ ∅ for all 78 497 primes 3 ≤ p ≤ 10⁶ ✓ (10⁷ not re-run).
* S₈(p) = ∅ (and, identically, "S₄ with an all-even slice solution" = ∅) at exactly 27 primes ≤ 10⁶: 3, 11, 17, 113, 131,
  241, 257, 353, 593, 1249, 1489, 1601, 2081, 3169, 3361, 4481, 5281, 5521, 14177, 14401, 15233, 33601, 83449, 211681,
  215297, 252001, 259201 ✓ (so the 27 at ≤ 10⁷ all lie below 2.6·10⁵).
* Odd squares ≤ 10⁶ (499): S₄ = S₈ = ∅ ✓.
* Odd composite non-squares n ≤ 2·10⁵ with S₄ ≠ ∅, S₄^{odd} = ∅: exactly 321, 4545, 5481, 8745, 9121, 13041, 25305, 57481,
  169425 ✓. (Side fact: n = 105 is the only odd composite non-square ≤ 2·10⁵ with S₄(n) = ∅.)
* One-odd ES half (solutions of 4/p with exactly one odd denominator): no failing prime ≤ 10⁶ ✓. One-odd half of 8/p
  fails exactly at 3, 11, 17, 59, 131, 241, 449 (≤ 10⁶) ✓.

---

## Defects
1. **D1 (MINOR)** `BRAINSTORM/y4_t1_numerators.md`, Cor 2(a): "(n/g) = −(−M/g)" must be "(n/g) = (−M/g)" (so that
   (−Mn/g) = 1). Repair: flip the sign.
2. **D2 (MINOR)** FOUR_SPECIFIC §1 Cor 1.2 last clause / memo Cor 2(c): "the relaxation holds at squares too" →
   "the M-shot family reaches every odd square prime to M (so the relaxation is shot-provable there)"; M^□ holds at most
   odd squares for all M anyway.
3. **D3 (MINOR)** FOUR_SPECIFIC §1 last line / memo: "T1-bearing and failure-free to 10⁸: 3, 4, 7" is a statement
   about M ≤ 24 (census) and, via PW §6, M ≤ 30000; add "(among M ≤ 30000)".
