# Hostile cross-lab review (Claude Opus) of `notes/z80/EXTREME.md` and `data/z80/extreme/`

Reviewed commit: `c72d66110` (only commit in `main..`), author lane GPT-6.2 Astra.
I did not edit any author file and committed nothing. My scripts are `scripts/z80_xr_opus_*`; my outputs are in
`data/z80/xreview/`. All runs were serial, with `ulimit -v 6000000`, `timeout ≤ 1800`, offline `uv`. Temporary binaries
in `/tmp` have been deleted.

## Verdict (short)
* **§1 theorem (smooth smallest denominator, almost all p): PROVED rel. ET's parametrisation. I found no gap.** I
  re-derived every step: the reverse incidence, the 2nd moment, the polynomial divisor bound, Rankin and the quantifiers.
  It is modest in strength and its triage is missing (fix F1).
* **The individual R₈ zero p = 6,955,940,568,721: CONFIRMED** by three independent engines of mine plus the earlier
  z76 Opus verifier. It is prime, R = 42 (21 unordered), R₈ = 0, and the 8/p certificate holds. The record is fit to
  promote.
* **ET table (16 rows), word tables (25 rows), panel windows (44 primes), audit minima and the EVIDENCE fit: every value
  I checked reproduced exactly** with own-code engines (coverage below). The note now overstates nothing about
  coverage. It **understates** it: the high ET rows now have two fully independent counts.
* **AP tables**: one author engine, sound by inspection. My independent slice re-checks found no extra zero (coverage
  below). The tables are not fully independently replayed.
* Heuristic material is correctly labelled EVIDENCE/Assessment. The form fixes F1–F8 below are owed, all minor apart
  from F1 and F2.

**Recommendation:** promote the R₈ floor (STATUS §1F), with the corrected delta in F7. Record §1 as a scoped PROVED
almost-all structural result (BARRIER-SCOPED / FRONTIER §6 line, or an Assessment-level FRONTIER sentence), not as a
STATUS headline. External priority remains unverified (I had no network).

---

## 1. §1 theorem: hostile proof check

**Parametrisation.** Type I gives (x,y,z) = (acd, bcd, pabd), with c | a+b, e = (a+b)/c, pe+1 = 4abd and
f = 4acd − p. Then ef = 4a²d+1 and bf = ap+c. Type II gives (abd, pacd, pbcd), with ce = a+b, p = 4abd − e,
f = 4acd − 1. Then ef = 4a²d + p and bf = pc + a. I re-derived all of these identities. With a ≤ b, x is the smallest
coordinate in both types: c ≤ pb in I, and b < pc in II because 4abcd ≥ a+2b. In I, given (a,c,d) with acd = x, a
divisor f of 4a²d+1 fixes p = 4x − f, then e and b. In II, given (a,b,d), a divisor e of a+b fixes c and p. So (1) is a
valid majorant **indexed by x**. The direction needed is solution ⇒ some tuple, which holds.
* Numerical sanity (`scripts/z80_xr_opus_reverse.py`, `reverse_sanity.txt`): over all primes ≤ 3000 there are 27,221
  sorted witnesses and 0 violations of tally(x) ≤ w(x).
* I could not open ET offline, so the proposition numbers (2.2, 2.6, 2.8, 2.11) are unverified. Completeness of the
  canonical gcd(a,b) = 1 enumeration is confirmed empirically, because my ET-free direct count equals `et.csv` on all 16
  rows (§3 below).

**Second moment Σ_{x≤Z} w(x)² ≪ Z log^C Z.** These steps are all correct:
* w² ≤ 2(ΣI)² + 2(ΣII)²;
* Cauchy over the factorisations costs τ₃(x);
* a second Cauchy over triples gives Σ τ₃(x)³ ≤ Σ τ₂₇ ≪ Z log²⁶ Z. Note τ₃(p^e)³ = C(e+2,2)³ ≤ C(e+26,26), with
  equality at e = 1.

For the fourth powers:
* **τ(a+b)⁴:** sum over the larger dyadic side, Σ_{m≤4V} τ(m)⁴ ≪ V log¹⁵ V, uniform in the fixed side.
* **τ(4a²d+1)⁴:** the free variable c contributes only its box length. In the larger of a and d the polynomial is
  4dv²+1 or 4a²v+1, of size ≪ V³.
  * Root counts are uniform in the fixed coefficient: 0 at q = 2 or at q dividing the coefficient, at most 2 otherwise.
    This holds modulo every q^j, because the discriminant 16d is prime to q (Hensel).
  * The greedy block argument needs at most 3 primes > V and O(1) blocks. That gives τ⁴ ≪ max_block τ(h)^k with
    h | P(v), h ≤ V.
  * Counting gives ρ(h)(V/h+1) ≤ 2ρ(h)V/h.
  * The Euler product is polylog, uniformly.
* There are O(log³ Z) boxes. The moment claim is **PROVED**.
* Numerically, Σ w²/(Z log⁴ Z) climbs slowly, from 52 to 85 over Z = 281…2251. The polylog power C is large; the
  theorem only needs some C.

**Transfer and Rankin.**
* Σ_{x∈S} w(x) ≤ |S|^{1/2}(Σ_{x≤2X} w²)^{1/2} holds, and x ≤ 3p/4 < 2X.
* Rankin with s = 1 − log u/(2 log Y) gives (2X)^s = 2X·exp(−(u/2)log u (1+o(1))).
  * With u = K log₂X/log₃X this is exp(−(K/2 + o_K(1)) log₂X), because log₄/log₃ → 0.
  * Σ_{q≤Y} q^{−s} ≤ √e(log₂Y + O(1)) + √u(log log u + O(1)). The first part is the "O(1)·log₂X" in the note, about
    1.65·log₂X. The second part is o(log₂X).
  * Higher prime powers cost O(1) since 2s ≥ 3/2.
* So |S| ≤ X(log X)^{−K/2+1.65+o(1)}. Witness count ≪ X(log X)^{−K/4+0.83+C/2+o(1)}. K > 4A + 2C + 4 suffices.
* Exceptional primes ≤ witnesses. Y = X^{log₃X/(K log₂X)}, so c_A = 1/K. **Correct.**

**Quantifiers.**
* The statement is "outside O_A(X/log^A X) primes p ∈ (X,2X], *every* solution has P⁺(x) > Y". This is what is proved.
  It is a statement about solutions at almost all p. It is not per-p, says nothing about infinitely many p in either
  direction, and gives no positivity at any p.
* The note correctly says that S may be adversarial on the whole dyadic interval but is not p-dependent.
* "Relative density one in 1 (840)": A = 2 gives o(π(X;840,1)). Correct.
* Nonvacuity: if a prime q ≡ 2 (3) divides x₀ = (p+3)/4, then (1,q,(q+1)/3,x₀/q) gives e = 3 and p = 4x₀ − 3. I
  checked this.
  * The converse argument also holds: the factor 3y − px₀ ≡ 2 (3) must divide (px₀)², which is impossible if every prime
    factor is 1 (3).
  * The density of p avoiding a finite list of such q tends to Π(1 − 1/(q−1)) → 0. Correct.
* exp((log p)^κ) for every κ < 1 follows from X^{c log₃/log₂}. Correct.

**Dual B(x) and order statistic.** Both are correct.
* B(x) = least B with at most one prime factor > B, and that one ≤ B². Hence √P⁺ ≤ B ≤ ⌈√x⌉.
* For the second-largest ET coordinate: bf = ap + c in I and ef = 4a²d + p in II. This gives h ≥ min(√p, (p/4)^{1/3}).
* No energy inequality, large sieve or growing-modulus transfer is used anywhere, as the note says. The ingredients are
  only Cauchy, divisor moments and Rankin.

**Assessment of strength.** The first moment alone (max w ≤ x^{O(1/log log x)}) gives only P⁺(x) > exp((log₂X)^{2+o(1)})
or so. The second moment is what reaches exp((log X)^{1−o(1)}), so the argument is not vacuous. But this is a union-bound
statement. "Obstruction" in the commit title means an obstruction to *smooth-x witness strategies* (for example
factor-base searches). It is not an obstruction to ES, and the triage should say so (F1).

## 2. The R₈ zero 6,955,940,568,721: independent verification

| check | engine (own code unless noted) | result |
|---|---|---|
| primality | trial division by all primes ≤ ⌊√p⌋ = 2,637,411 (C), PARI `isprime`, and the z76 Opus verifier | prime |
| p − 1 | PARI | 2⁴·3·5·11·13·23·8812127 ✓ |
| R, R₈ by shifted factors | `z80_xr_opus_words.c`: segmented sieve factorisation of p+u for all u with ku² − 2u ≤ p, every divisor f ≡ −1 (ku), B > u | 21 unordered (R = 42), **R₈ = 0** |
| full word census | same program, a different partition from both author engines (minimal letter; t-minimal case by direct u-loop, not factoring tp+1) | (R,R₈,U₇,ES₅,HJmin,words) = (42,0,58,250,17,469) ✓ |
| second word engine | `z80_xr_opus_words_pari.py` (PARI divisors of p+u and tp+1) | identical ✓ |
| exhaustive R₈ in AP window | `z80_xr_opus_apcheck.c` (MR-12 primality, own 3-case exhaustive loops) | the only zero in 361 (840) ∩ [6.9559·10¹², 6.956·10¹²] (17,577 primes) |
| earlier cross-lab verifier | `scripts/z76_disproof_opus_verify_r8.py` (sieve + direct-C partial) | k = 4: 21/42, first (4,59,7368581111); k = 8: 0 ✓ |
| 8/p certificate | exact Fractions | 1/(abd) + 1/(pacd) + 1/(pbcd) = 8/p for (2,434856320039,247,1) ✓ |
| class | — | p ≡ 361 (840) ∈ 𝔐, p ≡ 7921 (9240) |

The z76 AP engine, re-run on the same window, also reports exactly this MISS.

My word engine was validated against a naive triple loop for all n ≡ 1 (4), 9 ≤ n ≤ 1397 (348 n, prime and composite):
0 mismatches. My two R₈-zero engines agree on all 231 R₈-zero primes p ≡ 1 (4) in (5, 2·10⁵].

## 3. Tables: independent coverage

* **`et.csv`, all 16 rows**, checked with `z80_xr_opus_direct.c`. This is a direct, ET-free enumeration: for each
  x ∈ (p/4, 3p/4] take h = p^iδ with δ | x². I note that i = 2 is impossible since δ ≤ x/p < 1. Every solution is
  checked and classified by the number of multiples of p.
  * The columns I, II, distinct, ordered, min_x, min_gap and min_P⁺ are **identical on all 16 rows**, up to
    p = 898,716,289 (5.7 min) (`direct_et.csv`).
  * min_H2 was not independently checked. It is not load-bearing, and its lower bound is proved.
  * This upgrades the note's "coverage of the high rows rests on the ET engine": there are now two independent full
    counts throughout.
* **Small primes**: I re-counted all 3,244 primes < 30000 with the direct engine. They are identical to the repository
  `f4_all_30000.txt`.
  * The decade minima reproduce exactly: 1 @2, 4 @13, 6 @193, 9 @2521, and 9/log³2521 = 0.018731.
  * The record-list decade minima follow from `et.csv`, which is now verified.
* **External checks**:
  * A073101: strict counts at the odd primes ≤ 23 match. The audit list is a genuine OEIS cache
    (`data/z52b/oeis_cache.json`; offset checked, a(2) = 0).
  * Both 8/131 and 8/241 have no representation by my own Fraction search.
* **`words.csv`, 23 rows**: all six columns are identical with my C engine (`words_opus.csv`). R = 2·R4pairs and
  R₈ = 2·R8pairs on every row.
* **`wordfactor.csv`, the two extra rows** (1.16·10¹⁶, 1.97·10¹⁷): identical with my PARI engine (`words_pari_big.csv`).
  These rows now have two implementations, although the algorithm family is the same as `wordfactor.py` (factor n+u and
  tn+1).
* **`panel.csv`** (`z80_xr_opus_panel.py`, `panel_check.txt`):
  * all 72 rows: factorisations re-multiplied, factors proven prime, primality flag and first inert prime checked, with
    0 mismatches;
  * 52 distinct A002189 entries, 24 of them prime; both entries above 10²⁴ are composite;
  * **1024-window I/II counts on all 44 prime rows** (24 record primes and the 20 sq/ct): a different method from the
    author's (ET factorisations of x with g = 4x − p, deduplicated triple sets), identical everywhere. Examples:
    (434, 259) at 1.36·10²²; (892, 585) and (1608, 882) at k = 24; (620, 380) and (764, 453) at k = 18.
* **Controls**: with my own engine, R = R₈ = 0 at all 14 `star_prime_zeros` primes and at 17401609, and U₇ = 0 at all
  eight Z₇. The 4545 Type II claim and the F1 odd-square strict counts were not re-checked by me.
* **EVIDENCE fit**: from my direct counts, the fibre has 29 primes, c = 0.047381, φ = 1.48054, m = 1.24027, and
  log₁₀P₀(10¹⁸) = −1181.24. Held-out obs/pred is 0.544–1.273. All identical.
  * The tangent slope 3(c/m)log²(10¹⁸) is about 196.9 > 190. The integer-sum loss is about 10^{15.7}, within the
    claimed ≤ 19 orders.
  * The clump model (Fano 2m − 1) is internally consistent, and the normalisation of f is right: sorted, unordered
    counts, not ET's ordered f = 6(I+II), which would carry a deterministic ×6 clump.
  * Note that the fit spans p ∈ [10³, 3·10⁴] and the extrapolated λ is about 70× larger. The label EVIDENCE with
    "not an extrapolated certificate" is adequate.

## 4. AP tables (`ap361.txt`, `ap9240.txt`)

**Engine inspection** (`z76_disproof_ap.c` with `z75_push2_prime_ap.c`). I found it sound.
* Its congruences n ≡ −u−v (8uv) and n ≡ −u (8uv−1) produce genuine positive witnesses, since n ≫ the moduli.
* The late scan f ≡ 7 (8), u = f − n mod f, u | (f+1)/8 is a valid witness test.
* `exact()` loops over all 6 role orders with the smallest letter up to the cube bound. It asserts rather than skips an
  out-of-order third letter, which is safe because the runs completed.
* The headers match the table: 8,214,285,714 and 1,451,267,943 slots; 6,662 and 2,872 hard primes; misses 1 and 0.
* All 6,661 + 2,872 H-lines satisfy 8ubc − u − b = n (author audit). I re-read the engine but did not replay the whole
  range.

**Independent slice re-check**, an exhaustive R₈ test of every prime in the slices with my own engine (`apcheck_*.txt`):

| progression | slices | primes tested | own-exhaustive | zeros |
|---|---|---:|---:|---:|
| 361 (840) | [3.1, 3.13]·10¹², [6.9559, 6.956]·10¹², [9.98, 10.0]·10¹² | 8,929,777 | 71,093 | 1 (the record) |
| 1 (9240) | [1.590284203562, 1.790284203562]·10¹², [1.485, 1.5]·10¹³ | 6,274,909 | 66,127 | 0 |

That is about 0.73 % of the 361 range and about 2.6 % of the 9240 range by width. The table labels ("one AP engine;
no independent whole-interval census") are accurate. The record itself does not depend on the AP scan.

## 5. Fixes owed (form and substance)

* **F1 (triage, substance of presentation).** §0 triages the note only as RECORD, with the R₈ delta. The §1 theorem
  has no triage class.
  * Proposal: BARRIER-SCOPED / FRONTIER §6 one-liner. "PROVED rel. ET: outside O_A(X/log^A X) primes, no solution has
    X^{c_A log₃X/log₂X}-smooth smallest denominator. This rules out almost-all coverage by smooth-x witness families;
    there is no per-p statement."
  * It should not go into STATUS §1 unless the orchestrator judges it headline-worthy, and then only after an Astra-side
    second check.
  * Reword the commit/Result "obstruction" accordingly.
* **F2 (wrong wording, §3 Algorithm).** "gcd(a,b) = 1 (equivalent to triple-primitivity here …)" is misleading. The
  enumeration counts **non-primitive** triples too. For example, at p = 17 the tuple (a,b,c,d) = (1,6,1,5) gives
  (5,30,510), with gcd 5, and it is among the I = 2 solutions.
  * What the parenthetical argument shows is gcd(a,b) = 1 ⟺ gcd(a,b,c) = 1. This is the canonical representative,
    since (ga, gb, gc, d) ↦ (a, b, c, g²d) gives the same triple.
  * The counts themselves are right, as shown by the direct count.
* **F3 (unreferenced lemma).** "Lemma CT" in §3 has no file pointer, and its I/II consequences were not reviewable. Add
  the source or label it as an Assessment.
* **F4 (proof detail).** In "bf/a ≤ 5p/3" the bound c/a ≤ 1 + (p+1)/(4a²d) is needed, which follows from f ≤ 4a²d + 1.
  It should be stated. It actually gives bf/a ≤ 5(p+1)/4.
* **F5 (notation).** "Minimum additive gap exactly 3/4" means x − p/4, while `et.csv` `min_gap` is 4x − p (= 3). Say
  which one.
* **F6 (context).** "The proposed second largest h" (§1) and "the z78 endpoint" lack pointers to the proposer or file.
  The dual B(x) bound is near-trivial (it restates x ≤ 3p/4). Say so rather than presenting it as a two-sided result:
  the two sides are separated by p^{1/2} versus X^{o(1)}.
* **F7 (STATUS delta).** The proposed replacement drops the existing provenance. Suggested text: "**R₈ (C-even (★))
  threshold floor:** 12 certified prime zeros across all classes (z75–z76, z80) raise the in-𝔐 floor to
  **6,955,940,568,721** (≡ 361 (840); R = 42; full 8/p passes; author ordered-coordinate + shifted-factor checks and a
  cross-lab Opus check with three own engines; earlier floors 1,590,284,203,561, 1,511,088,831,001, …;
  `notes/z80/EXTREME.md`, `data/z80/xreview/REVIEW_EXTREME_OPUS.md`)". The orchestrator should verify the count of 12
  against z75/z76.
* **F8 (coverage statements to update).**
  * "Coverage of the high rows rests on the ET engine, not two independent full counts throughout" is superseded: all 16
    rows were independently direct-counted by this review.
  * "those two rows have one full-count engine" now has a second implementation (same algorithm family).
  * Review line: "cross-model (data/z80/xreview/REVIEW_EXTREME_OPUS.md)".
* Unverified (needs network): the ET proposition numbers, A192787 identification (consistent with z52b), and external
  priority for §1.

## 6. Replay of this review
```
gcc -O2 -o /tmp/w scripts/z80_xr_opus_words.c -lm;  /tmp/w <n...>            # words + R/R8 pairs + primality
gcc -O2 -o /tmp/d scripts/z80_xr_opus_direct.c -lm;  /tmp/d <p...>            # ET-free direct sorted counts
gcc -O2 -o /tmp/a scripts/z80_xr_opus_apcheck.c;     /tmp/a 840 361 LO HI     # exhaustive R8 on AP slice
uv run --offline --no-project --with cypari2 python -B scripts/z80_xr_opus_panel.py [n...]
uv run --offline --no-project --with cypari2 python -B scripts/z80_xr_opus_words_pari.py <n...>
uv run --offline --no-project python -B scripts/z80_xr_opus_reverse.py 3000
```
Always use `ulimit -v 6000000` and `timeout ≤ 1800`. Memory stays below 0.5 GB per run (the sieves are at most √(n+U)
bytes, in 2¹⁶ blocks).
