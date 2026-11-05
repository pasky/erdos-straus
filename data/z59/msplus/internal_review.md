# Internal hostile review — Z59_MSPLUS.md (memo at commit 803f068d)

Reviewer scope: every proof step and every number I could recompute. All computations used `ulimit -v 4000000` and
timeout ≤ 1800 s. Scratch code: `/tmp/z59rev/` (not committed). One new artefact is committed next to this file:
`review_g3/` (the pre-registered "3 ∣ n only" OOS row, which the memo never ran; see M2).

## A. What I independently verified (no action needed)

* **Theorem 1 proof.** I checked every step: swapping the sums; the CRT compatibility a ≡ −(u+B) (mod g) with
  g = gcd(4uB, Q); the O(1)-per-pair error, summed over ≪ X log X pairs; the hyperbola sum with periodic weights,
  (f̄/2)log²Y + O_Q(log Y); the cut-off error; and the normalisation f = [cons]·g/4, which gives f̄ = 𝔖/4 and the
  mean (𝔖/8)log²X. The odd-q case split (1−1/q)² + (2/q)[q∤a] + (1/q)[q∣a] and the 2-adic argument (factor 1 for every
  k ≥ 2) are both correct.
* **Exact local enumeration (own code).** E[[cons]·g] over (u, B) mod Q gives:
  * 2-adic factor 1 for k = 2..5 (R) and for k = 2..6 (R₈, with g = gcd(8uB, Q));
  * σ₃ = 10/9 | 7/9, σ₅ = 26/25 | 21/25, σ₇ = 50/49 | 43/49, σ₁₁ = 122/121 | 111/121;
  * Remark 2.1 for 3^e (e ≤ 3), 5^e (e ≤ 2), 7² (q ∣ a vs q ∤ a only).
  Remark 2.3 holds: with the normalisation 1/8 the R₈ leading constant is exactly half.
* **Numerical mean check (own sieve, exact R and R₈ for n ≤ 1.3·10⁷, about 2 s).** I took window means over non-square
  n ≡ 1 (4) and fitted a + b/L + c/L² to mean/L². The intercept a matches 𝔖/8: unit 0.1473 vs 0.1474, g3 0.1034 vs
  0.1032, g7 0.1242 vs 0.1268. The small groups match within 5–10 % (noisy). R₈/R is 0.44–0.47 at 10⁷, which is
  consistent with ½ plus second-order terms.
* `means_1e9.txt` bin 35 matches the §2 table exactly. The P𝔐/P-unit ratio is 0.790 observed and 0.844 modelled ✓.
* **Lemma 2.0, Lemma 4.1, Lemma 5.1: correct.**
  * Lemma 4.1:
    * s₀ ≡ 1 (4) because t is odd.
    * (s/ℓ) = (ℓ/s₀).
    * χ₋₄·(·/s₀) is non-principal, which gives density ¼.
    * (−s⁻¹/ℓ) = 1, so there are 2 roots.
    * The witness checks: 4·B·(ℓ+1)/4 − 1 − B = Bℓ − 1 = sm².
    * The sieve product goes to 0.
  * Lemma 5.1 is a direct division.
* **Certified values, two independent engines:** a brute-force sieve and a new divisor-based single-n code
  (R = 2·Σ_u #{d ∣ n+u : d ≡ −1 (4u), d < (n+u)/u}, cross-checked against brute force on 150 random n). Results:
  * R(45) = 2, R(101) = 6, R(517) = 4, R(4545) = 0, R(24 253) = 32, R(12 538 801) = 0, with
    12 538 801 = 517·24 253 = 11·47·79·307.
  * Also R = 0 for 8 813 281, 17 401 609, 29 210 401 and 9 919 520 121.
* **§5.3 table, recomputed from `zeros_1e10.txt.gz`** (50 499 lines; 49 999 odd squares; 500 non-squares, 14 P + 486 C):
  * (MS): 9, last 8 813 281.
  * (MS⁺): 27 = 9 P + 18 C, last 17 401 609.
  * (MS⁺₁₀₅): 38, last 29 210 401.
  * Rough versions (prime factors strictly > y): y = 11 gives 30 / 17 401 609; y = 43 gives 21 / 17 401 609;
    y = 47 gives 19 / 8 813 281.
  * All non-squares: 500, last 9 919 520 121. Every entry ✓.
* **§3.3 table and the [10⁹, 10¹⁰] counts.** Per-decade, per-group zero counts recomputed from the z58 list match the
  zerofit file and the memo: 261 in-sample zeros; 42 in [10⁹, 10¹⁰] = 11/18/6/4/2/1; 105 ∣ n gives 27 on [10⁶, 10⁸]
  and 11 on [10⁹, 10¹⁰]. Every predicted number quoted in §3.2–3.5 and §5.3 matches `zerofit_1e9.txt` and
  `zerofit_beta0.txt`:
  * A and B coefficients;
  * 5.51/4.36/1.09 and 6.05/4.80/1.32;
  * 15.8/7.83/1.78;
  * 10.85, 4.84, 1.63, 0.52 and 12.0, 4.05, 1.22;
  * 𝔐 2.55e-3 and 1.69e-4; PM 1.3e-4; Cunit 1.42e-3; β=0 𝔐 4.0e-4;
  * totals 20.8 / 2.85e-3 / 4.3e-3.
* **OOS data.** There are 17 Z lines (9 + 2 + 2 + 4 + 0), all statuses exit=0.
  * Every one of the 17 zeros has R = 0 by my independent engine. All are non-squares in the stated classes.
  * The class lists are correct: 12 classes for 15 ∣ n, 7 ∤ n; 8 classes for 21 ∣ n, 5 ∤ n.
  * The S-line counts equal (#n in classes) − (#odd squares in classes), so squares are excluded.
  * Engine completeness cross-check: I ran `z59_msplus_cdec.c` myself on (10⁶, 10¹⁰] for 105∣n, 15∣n 7∤n, 21∣n 5∤n
    and 3∣n-only. The zero sets equal the z58 LOGIC zero sets exactly (48 / 87 / 55 / 76).
* **Pre-registration.**
  * `git show 85a4fa37:Z59_MSPLUS.md` contains the table 5.51/6.05, 4.36/4.80, 1.09/1.32, 0.57/0.83 and
    3.7e-4/2.6e-3, committed 16:23:23.
  * The first OOS result file (g105) has mtime 16:27:51 and is committed in 27e9a3d4; the rest are in 803f068d.
  * So the predictions precede the results ✓. I cannot verify that the *run* started after 16:23, only that the
    results were produced after the commit.
* **Structured search (§4.3).** I re-verified all 460 000 output lines. For every non-square input I checked:
  * 4uBC − u − B = n with u, B, C ≥ 1, and mu equals the stated modulus (4uB or 4uC−1);
  * n mod 840 ∈ 𝔐 and 10¹¹ < n < 4·10¹⁸;
  * 0 UNK, 0 failures, max mu = 211 403.

  The distinct counts match EVAL: 99 220, 24 378, 86 330, 50 000, 49 992 non-square (49 998 distinct incl. 6 squares).
  The six squares are p² for primes p and are UNK at LIM 10⁷.

  The generator logic gives 𝔐 and non-squares:
  * sm2 and deadsq: s ∈ 𝔐 times a unit square;
  * msq: m² + 840t with gcd(m, 210) = 1;
  * dead: CRT plus an assert;
  * semi: an inM filter.

  `dec.c` is correct (d-form and 4uB-form witnesses, 128-bit re-verification, B = 0 rejected by verify).
* **§6 census: now complete.** As of 17:20 all 18 chunks (10¹¹, 10¹²] have exit=0 and 0 zeros.
  * Totals: 1 046 544 177 primes + 5 381 870 962 non-square composites = 6 428 415 139.
  * This equals 6·9·10¹¹/840 minus the 156 291 odd squares coprime to 105, so it is complete.
  * The stale exit=126 status for 85–90e10 has been overwritten by exit=0.

## B. Findings

### MAJOR

**M1 (§1, §6, §7 verdict, FRONTIER text, bottom line: "(MS⁺) CERTIFIED to 10¹²").**
* At the memo commit 803f068d, three chunks were not done:
  * 85–90e10 had a committed status **exit=126**;
  * 90–95e10 and 95–100e10 were empty.
* §6 itself says "Progress at writing: (10¹¹, 4·10¹¹]" and "Final numbers in §8", but §8 has no numbers. So the
  CERTIFIED-10¹² claim was made before the data existed, and §6 contradicts §1 and §7.
* The chunks have since finished cleanly (see A), so the claim is now true. But the memo and repo are inconsistent:
  three chunk files and two status files are uncommitted or modified.
* *Fix:*
  * commit the census files;
  * rewrite §6 with the final totals (1 046 544 177 P + 5 381 870 962 C, 0 zeros, all 18 chunks exit=0);
  * drop the dangling "§8" reference;
  * never label a range CERTIFIED before every chunk status is exit=0.

**M2 (§3.4 "passed", §7 "passed a pre-registered out-of-sample test", FRONTIER "It passed", bottom line "a correctly
pre-registered decade").** The pass is overclaimed.
* No pass/fail criterion was pre-registered in 85a4fa37, so "passed" is a post-hoc judgement.
* Poisson tails (computed):
  * total 17 vs 12.17 (B): p = 0.11; vs 10.96 (A): p = 0.055;
  * 21∣n row 4 vs 1.32: p = 0.045 (A: 0.025);
  * the β = 0 fit over-predicts, with P(X ≤ 17 | 25.4) = 0.05;
  * the held-out (not pre-registered) [10⁹, 10¹⁰] decade, 42 vs 28.2 (B), has p = 0.009 (A: 0.0045).
* So in two consecutive decades the law under-predicts by ≈ 1.4–1.5×, and the free-β and β = 0 fits bracket the data
  only marginally. That is "right order of magnitude and group ranking", not a passed test.
* Two pre-registered rows are missing from §3.4: "3 ∣ n only" (0.57/0.83) and "𝔐 composites" (3.7e-4/2.6e-3).
  * The OOS script defines `C3` but never runs it.
  * I ran it (`review_g3/`, 3 chunks, exit=0): **1 zero, 10 234 561 689 = 3²·11·23·4 494 757** (R = 0 confirmed
    independently), against 0.57/0.83 predicted. This is consistent.
  * The 𝔐-composite row is 0 observed (z58 census) against 2.6e-3.
* *Fix:*
  * report all five pre-registered rows (new total for the four count rows: 18 vs 11.5 (A) / 13.0 (B));
  * state that there was no pre-set criterion and give the p-values;
  * replace "passed" with "matched order of magnitude and group ranking; under-predicted the total by ≈ 1.4× (p ≈ 0.1
    under B, 0.05 under A); 21∣n row 3× high";
  * apply the same change in FRONTIER text and the bottom line.

**M3 (§5.2 first bullet).** The bullet says "Primality is used in (MS) only through 'no small prime factor' … an
argument for (MS) that uses primality only via 'n has no prime factor ≤ y(n)' proves (R⁺_y) on 𝔐 at no extra cost".
* This is logically wrong and contradicts F1. Rough odd squares p² with p > y have R = 0, so no correct argument can
  use primality *only* through roughness. Such an argument would prove R(p²) ≥ 1.
* The bottom line ("no small prime factor *plus non-squareness*") has the correct version, so the memo is internally
  inconsistent. The "at no extra cost" sentence supports the target-choice recommendation.
* *Fix:* "primality enters through roughness (Lemma 2.0) **and** non-squareness (the Jacobi structure, T1); an
  argument that uses only these two proves (R⁺_y)". The bottom line's "show that primality matters only through …"
  should become "are consistent (census to 10¹⁰) with …".

**M4 (§7 "Narrowed (scoped, PROVED) … so 'reduce to primes' or 'reduce from primes' proofs are unavailable";
bottom line "admits no 'reduce to primes' argument").** These are non-sequiturs carrying a PROVED label.
* Lemma 5.1 and the CERTIFIED examples show only that the *unconditional* product, divisor and q²-scaling closures
  fail.
* Lemma 5.1 itself is a *conditional* closure (a solution with b ∣ C lifts to bn). Reductions conditioned on the shape
  of the witness are not excluded.
* *Fix:*
  * relabel as Assessment;
  * say "naive (unconditional) closure-based reductions fail";
  * likewise "cannot be a proof route" for the means mechanism (F1/F2) is a meta-argument, so it should be
    labelled Assessment, not PROVED.

### MINOR

**m1 (§3.4).** The memo says "The 16 zeros are listed", but the OOS files contain **17** (9 + 4 + 4, the memo's own
table). Fix the number.

**m2 (§4, "Data" paragraph).** The claim "for every non-square s ≡ 1 (4), s < 3000, at most 2 odd m … out of 924–1741
values of m" is **false as stated**.
* s = 33 has zeros at m = 7, 35, 45, and s = 105 at m = 1, 11, 57: 3 each.
* The number of odd m with sm² ≤ 10¹⁰ ranges over 913–22 361 for this s-set, so "924–1741" matches no natural reading.
  It is 932–1574 if s ∈ 𝔐, and then the maximum number of zeros is 1.
* No script backs the paragraph. (The q² inheritance counts are fine: 1, 1, 0, 2, 0 for q = 3, 5, 7, 11, 13.)
* *Fix:* restate the claim for the set actually computed, and commit the script.

**m3 (Lemma 4.1 reading; §7; FRONTIER "There is no twisted-T1 family for (★) (PROVED)").**
* The lemma proves density 0 of zeros in {sm²}. It does not exclude an infinite thin subfamily, e.g. m restricted to a
  sieve-thin set avoiding the hit classes.
* "Any infinite non-square zero family must have a growing square-free core or no square structure at all" is
  therefore an overclaim.
* *Fix:* "no positive-density twisted-T1 family".

**m4 (Prop 2.2, last bullet).** "For non-𝔐 unit classes c₁ is up to +0.43 (a = 13)" is false. `coef840.txt` gives
unit classes with c₁ = 0.887 (a = 89) and **2.202 (a = 209, 629)**, i.e. n ≡ −1 (mod 105). Fix the number. The
interpretation (n ≡ −r with small r) actually supports the c₁ heuristic.

**m5 (F3; §3.3 bold "within a factor ≈ 1.5").** This holds only for the four large groups (g3, g15, g21, g105).
Counter-examples:
* in-sample: g5 dec8 3/0.94, g7 dec8 2/0.31 (6.5×), P𝔐 dec6 4/0.6;
* held-out: g35 2/0.31, g7 1/0.06;
* OOS: 21∣n 4/1.32.

Fix: scope the sentence to the large groups.

**m6 (§3.2 "rare because m is large, not because of any rigid structure"; §7 "a pseudo-square effect").**
* Model B's own depth dummies are a structural effect of up to e^{2.05} ≈ 8×.
* The 4 𝔐-prime zeros of [10⁶, 10⁷) (1 724 209, 1 726 201, 5 212 561, 8 813 281) have Jacobi depth k = 13, 19, 11, 17.
  These are ordinary depths already inside the model, so the "pseudo-square" attribution is unsupported.
* *Fix:* relabel the 𝔐-prime excess as unexplained (hypothesis), and drop "not because of any rigid structure".

**m7 (Model B, `zerofit_1e9.txt`).** The k > 47 dummy is −24.9 ± 1.2·10⁶ because there are no events. The extrapolated
predictions therefore give ≈ 0 zero-probability to the deepest pseudo-squares.
* This is exactly the LOGIC Thm 6.2 danger class, and it contradicts the monotone trend of the other dummies.
* The numerical effect on the quoted tails is small (≈ 2⁻¹¹ of 𝔐), but the model is mis-specified there.
* *Fix:* pool k > 47 with 29–47 and refit (or report the effect).

**m8 (Cor 1.1(iii), labelled PROVED).** The step "the leading mean in any class stays ≫ L²/log L" applies Thm 1 with Q
growing with X. Thm 1's error is O_Q, not uniform. What is proved is a bound on the constant 𝔖 only, which is all
§3.5 needs. *Fix:* rephrase (iii) as a statement about 𝔖_Q(n).

**m9 (reproducibility of semi_2).** `semi_2.txt.gz` contains 6 squares p², but the committed generator has
`if p == q … continue` (present since its only commit 85a4fa37) and cannot emit p². The status files read "exit=0 0"
(2 fields), while the committed 3-stage pipeline prints 3. So the data came from an uncommitted earlier
generator/runner. *Fix:* say so in §4.3/F1, or regenerate. The F1 "T1 control" is then a by-product of a bug.

**m10 (§1 R⁺_y).** "For y ≤ 43 the threshold must be 17 401 609" is wrong for y < 11. For y = 7 (factors > 7) the last
zero is 29 210 401, and for y < 7 the 3∣n zeros run to 9.9·10⁹. *Fix:* "for 11 ≤ y ≤ 43".

**m11 (claims without artefacts).**
* The negative-binomial "under-predicts by 10–100" has no script or output.
* "The engine reproduces the z58 LOGIC zero counts … (27) … (11)" has no saved output. I reproduced it, with exact
  set equality, on (10⁶, 10¹⁰] for four groups.
* "The residual 1–11 % comes from primes q ≥ 11": at leading order q ≥ 11 contributes only ∏(1 + 1/q²) ≈ 1.02 for
  primes, so most of the 11 % must be second-order. This is unverified.

*Fix:* commit the artefacts or label as unverified.

### NIT

* **n1:** F2 says the R₈ rate is "≈ 5×" at 𝔐-primes. §3.5's 5× is over all primes ≡ 1 (4) (12 / 2.2·10⁷). Only 4 of
  the 12 are in 𝔐 (10 301 993 881, 10 529 331 121, 10 532 106 649, 10 868 474 401), and the excess there is larger.
  Align the wording.
* **n2:** In §3.4 the [10⁹, 10¹⁰] line has "𝔐 0 / 0.02"; the file gives 0.0242 + 0.0017 = 0.026. That decade is
  "held-out", not blind out-of-sample: the z58 list predates the model design.
* **n3:** §4.3 says "m ≥ 58" but EVAL's min is 57.6. It says "49 992 distinct" where EVAL has distinct = 49 998, of
  which 49 992 are non-square.
* **n4:** There is a heading "### 4.3" with no 4.1/4.2. §6 refers to "Final numbers in §8", but §8 has none.
* **n5:** `z59_msplus_oos.sh` has a dead placeholder `C21` containing 231 (≡ 3 mod 4) and 861 (> 840). `C3` is defined
  but unused.
* **n6:** "(MS⁺₁₀₅) contains (MS⁺)" holds only modulo the finite range (17.4M, 29.2M] in 𝔐, which the census
  covers. "At least as good a target" is a judgement call for a strictly stronger statement; say so.
* **n7:** Lemma 4.1 should say "positive" non-square s.

## C. Overall verdict

* **Mathematics (PROVED parts) is sound.** Theorem 1, Remarks 2.1/2.3, Lemma 2.0, Lemma 4.1 and Lemma 5.1 are correct,
  and I verified them independently both numerically and by exact enumeration.
* **CERTIFIED numbers check out.** This covers the §5.3 thresholds, the closure examples, the OOS zeros (independently
  confirmed as zeros, and the engine cross-validated against z58 on (10⁶, 10¹⁰]) and the structured-search witnesses.
  The 10¹² census is now actually complete with 0 zeros, but it is uncommitted and §6 is stale (M1).
* **Overclaims to fix are in the statistical framing and the verdict text:**
  * "passed" the pre-registered test (M2);
  * the primality-only-via-roughness logic (M3);
  * "PROVED" no-reduction claims (M4);
  * "no twisted-T1 family" without density qualifier (m3);
  * "within 1.5×" (m5).
* The memo nowhere claims ES or (MS)/(MS⁺) is proved; the open status is stated correctly.
* After the four MAJOR fixes the headline verdict, "narrowed / strengthened as target choice; no HOT LEAD", is
  appropriate.

**Recommendation: ACCEPT WITH REVISIONS (M1–M4 required before any FRONTIER text is applied).**
