Result: Round-2 cross-lab hostile review of `notes/z78/R17_PUSH.md` §§8–11 and `R17_R2EXACT.md` (commits `27422564e..681be8afe`). I found no mathematical error in the round-2 finite ledger or in the integer tails. The r≥293 sterile-line threshold stands. All load-bearing finite inputs at the binding prime 293 were replayed byte-identically or reproduced by independent code. Three replay and documentation gaps need fixing before promotion. One of them, the `qSpecial` generator, is load-bearing at 293.
Label: Assessment (review). Reviewer: **Claude Opus (Anthropic)**, running as a Claude Code subagent. No other model was called. There were no provider, auth or quota errors.
Scope: The math of §8 (P and Q integer tails) and of the §9 Legendre/convergent P₇ reduction. A line-by-line code check of `z78_r2{ledger,scale,tail,qtail,qfine,layers,dyad,local,shift,q5shift,cf,p7exact,exact7,highnear,near,neare}` and `z78_r2replay.sh`. Independent replays at 293 and on samples (§3). §§1–7 (round 1) and the inherited `packed`, round-1 `layer`/`p7` tables and z76/z77 lemmas were not re-derived, beyond confirming that they are integer-only.
Triage proposal: RECORD stands at **r≥293** (on [293,919) libm-free and relative to BBR; above 919, round 1 with its libm condition). Promotion requires fixing R2-F1, the missing `qSpecial` generator. The fix is cheap, and §3.4 below already gives a reconstruction.
STATUS delta: As the author proposes ("every prime r≥293"). Label: "PROVED (computer-assisted; on 293≤r<919 integer/rational relative to BBR 2012 Thm 1.2 and the z76/z77 lemmas; r≥919 as round 1, including the SE/ZL libm condition)".

# 1. Verdict

* **Theorem.** "Every prime 293≤r<919 passes the strict rational test." I checked every finite bounding route used at the binding prime 293 and found each one mathematically valid.
* **Ledger.** The ledger reproduces exactly:
  * total 495867 ppm;
  * exact margin 2427.203 ppm;
  * per-level P: 1, 138508, 97314, 32177, 14650, 5892, 3402, 1285, 369, then `globalP` at 5534, 4878, 4299, 137, … ppm;
  * finite Q 12779 ppm, P tail 7 ppm, Q tail 1354 ppm.
* **Inputs replayed independently.**
  * Exact depth-3 rows for **all 95 primes 293..911**, using the round-1 reviewer engine.
  * Exact P₇ new-cell counts at **all 9 primes whose pass depends on them**, using a new engine of mine.
  * The P₉ shift sieve at 293.
  * The `local` K=9, 11 and 13 rows at 293.
  * The scale rows 148–320.
  * The near-miss table `Pexact.tsv`.
  * The `qSpecial` value, reconstructed from shifts and `qlarge`.
* **Margin at 293 is thin.** 2427 ppm is 0.49% of the nonsquare mass. It rests on three specific inputs:

| input removed | change at 293 | other primes that then fail |
|---|---|---|
| exact P₇ (`exact7`) | P₇ 1 → 106956 ppm; margin −104069 | 307, 311, 313, 317, 331, 359, 367, 383 |
| `qSpecial` Q₅ row | margin −9390 | none |
| P₉ 128-bit sieve (`p9`) | fails | 307, 311, 313, 317, 331, 349, 359, 397, 401, 419, 431, 439, 479 |

  This is why R2-F1 and the P₇ replay matter.

# 2. Findings

**R2-F1 (replay gap, load-bearing): `data/z78/r2/qSpecial/bound.txt` has no committed generator and no replay stage.**
* What exists: `z78_r2q5shift.c` produces `shifts.txt`, which replays byte-identically. Nothing in the repository turns it into `bound.txt=24910840831`.
* What the note says: §10 only says "uses §4's two independent shift cuts … and `qlarge` for the complement".
* Reconstruction (`scripts/z78_r2xr_qspecial.py`, output `r2_qspecial_reconstruct.txt`): bound = min over j,l∈{0..3} of

      smallE[j] + **2**·smallF[l] + qlarge(r⁵, cut·2^j, cut·2^l),   with cut = ⌈r^{5/3}⌉².

  This reproduces 24910840831 exactly, at (j,l)=(1,2).
* The factor 2 on the small-f column is the z77 §5 inversion factor: the small-f range is enumerated in the a≤b orientation. It is **mandatory**. Without it the value would be 23783140794. The value can be reproduced **only** with this factor. But neither the C code nor the note says the f column is single-orientation.
* Fix:
  * commit the combiner (my script can be adopted verbatim);
  * add a `qspecial` stage: `B q5shift qshift; $R/qshift.bin 293 293 3 | diff - $R/qSpecial/shifts.txt; P scripts/…qspecial.py 293 | diff - …`;
  * add one sentence to §10: "small-f column counted for a≤b, doubled in the combiner (z77 §5)".

**R2-F2 (replay hygiene; no wrong number found).**
* `z78_r2replay.sh` sets `P(){ timeout 1700 …}`. This contradicts the repository rule and the note's own "timeout ≤1600s". Use 1600.
* Three stages write into committed files instead of diffing:
  * `exact7`: `z78_r2exact7.py` rewrites `exact7/{r}.txt`. The `read` happens first, so the test is still valid, but a failure leaves a modified tracked file.
  * `near`: `z78_r2neare.py` rewrites `near/E{L}.txt`, and the output of `z78_r2near.py` is printed but never compared.
  * `ledger`: `z78_r2report.py` rewrites `ledger.tsv`/`small.tsv`; only `summary.txt` is diffed.
* Fix: write to a temporary directory and `diff`. For `near`, use `P scripts/z78_r2near.py | diff - $R/near/Pexact.tsv`; I ran this and it is identical.
* Files with no generator:
  * `near/Pwitness.tsv`: I checked all three witnesses by hand (equations, units, v=3).
  * `log16.txt`: verified, all 512 entries equal `bit_length(i^16)−1`.
  * Add one-liners for both.

**R2-F3 (documentation of scope and dependencies).**
* §9 says the strip of covered parents is from stored lists "through 211". For 223..389, `z78_r2exact7.py` strips via `z78_r2exact` dumps instead. State this, and note that exact P₇ exists only for r≤389.
* §10 should list which inputs are load-bearing (table in §1).
* `small.tsv` covers only r≤211, while §10 says "at **each** small prime". The failures 223..283 are only in `ledger.tsv`. Reword.
* §7 still reads as a live theorem: "r≥919", "767 pass; largest failing prime 911", and an "Assessment — single next step" that round 2 has now done. Mark its heading "round 1; finite interval superseded by §10".
* `R17_R2EXACT.md` still says "Review: none". It can now cite this file, which gives a full-range independent replay (§3.1).

**R2-F4 (robustness, no current error): uncomputed table entries default to 0.**
* `z78_r2local.c` `capk[][][]` and `z78_r2layers.c` `caps[][][]` are static, so uncomputed entries are 0. A 0 means "chunk diameter 2^0 already has ≤ l−1 divisors", which is not true in general.
* `layers.c`: every index it uses lies inside the computed ranges.
  * v₃ = B + 2c + d + 6 ≤ 3B − 2·cut + 6 < 3B + 20.
  * All divisor exponents are ≤ 2B + 10.
* `local.c`: the cofactor lower exponent `lf` can exceed the computed f-range 16(2b−jmin+12) once jmin>12. There the stored 0 is **conservative**:
  * the computed v-range satisfies v ≤ 16(3b−2jmin+12), so lf > v/2;
  * with lf > v/2, every l has a>0 at h=0, so the true capk is ≥0.
  * So no bound is understated, but this rests on an unstated inequality.
* Fix: initialise both tables to −1, or assert the computed ranges. Also, the comment says "8-bit mantissas" while the code and note use 9 bits.

**R2-F5 (one-line justification missing): the P tail mixes rows.**
* At the first N≥2^320, the ledger multiplies `globalP(N)` by the **320-row** ratio r^(−4/320).
* `globalP` is a minimum over all scale rows with N≥2^B. That is valid only because all such rows (148/180/240/320) have G/B ≥ 2/320. For r<2^96, N<2^340<2^512 there, so rows 512/800 can never enter.
* As written, the code would be unsound if a slower-decaying row were admissible at that N.
* Fix: add this sentence. Rows 512 and 800 are computed but never used.

No finding affects any committed number.

# 3. Independent checks (all reproducible; one compute process at a time, `ulimit -v 2000000`, each chunk < 1600 s)

## 3.1 Exact depth-3 union, full range

`scripts/z78_r2xr_rows.sh lo hi out` runs the round-1 reviewer engine `z78_xr_exact.c` (Pollard–Brent; its own splits; no code shared with `z78_r2exact.c`).
* Over 293..911, all **95/95** rows of `r2exact/rows.tsv` agree in L1/P3/Q3/P5 (`r2_rows_replay.tsv`).
* At 293 the result is 50/186/372/614, and the live fraction is 8186020/25153757 = 325439.257 ppm, matching the ledger.

## 3.2 Exact P₇, by a new independent method

`scripts/z78_r2xr_p7.c` uses no continued fractions. It works in two parts.
* **Small shifts, e<E′.** Its own segmented sieve, with primes up to √M, fully factors M; then it enumerates all a≤b with ab|M.
* **Large shifts, e≥E′.** For t=acd≤T′ and each divisor c of t, the only candidate is a ≡ −Nc mod f, since a ≤ t/c < f. This is elementary and avoids Legendre's criterion.
* **New cells.** These are counted against the depth-3 alive bitmap dumped by `scripts/z78_r2xr_exact3dump.c` (the round-1 engine plus a dump). The driver is `scripts/z78_r2xr_p7run.sh`.
* **Validation.** At r=17 the distinct set equals the 392 M17B P₇ centres for E′=64, 4096 and 100000.
* **Results.** At the 9 primes where P₇ is load-bearing (293, 307, 311, 313, 317, 331, 359, 367, 383), the distinct and new counts equal the `exact7` rows exactly, using the splits E′=2^27 and 2^28, which differ from the author's (`r2_p7_independent.tsv`).

I also checked the §9 proof directly:
* gcd(b,c) | a, and rescaling (a,b,c,d)→(a/g,b/g,c/g,dg²) preserves t, e, the order and the centre;
* 0 < b/c − N/f = a/(cf) < 1/(2c²) ⟺ 2ac < 4acd − 1, which holds for all d≥1;
* the upper convergents are exactly the odd-index ones, with a = r_k;
* the `break` after the first hit per t is harmless, because the centre pair depends only on f;
* N%f=0 forces f to be a power of r, so its digit is filtered;
* T = ⌊(⌊N/E⌋+1)/2⌋.
* `z78_r2p7exact.c` covers e<E and the CF scan covers e≥E, so the two are complementary.

## 3.3 P₉ shift sieve (`z78_r2shift.c`)

* Byte-identical replay of `p9/z293.txt` (93 s).
* Proof check:
  * The absorbed copies in g form a prefix of the prime-ordered copy list. So does g₂, which is capped at 2^63. Since E < 2^63, g's prefix ⊆ g₂'s prefix, hence G·X | M in the absorb branch. The `assert(s==G)` in the c=1 branch is therefore sound.
  * The explicit pieces h₁ ∈ {1, x, x²} follow from M = g·x with gcd(g,x)=1.
  * x² maps to piece 1 by h ↔ M²/h, keeping the class −M.
  * For piece x, h₀ ≡ −g, and the only candidate ≤ g is e−g.
  * The remaining pieces number ≤ 3^Ω − 3; the rough primes are ≥ 65537 = Y+1.
  * Saturation happens at the whole level only.
  * Overflow: c·mult·R ≤ 4374·mod < 2^64, given the `mod` assert.
* Per-shift check (`scripts/z78_r2xr_shiftcheck.py`): it builds a patched copy that prints every per-e charge and checks #{h|M², h≡−M (mod e)} ≤ charge.
  * 293 K=9 (all e<2^10 plus 1500 random e<2^20): no violation.
  * 311 K=11, e<2^24: no violation.
  * 479 K=7, e<2^24: no violation.
  * In all three, the totals match the file prefixes (`r2_shiftcheck.txt`).

## 3.4 Q₅ special row (`z78_r2q5shift.c`)

* `shifts.txt` replays byte-identically.
* Proof check:
  * The strides are F (small e) and 1 (small f).
  * The start index is −M·stride⁻¹ mod p.
  * The rough primes are > 32768.
  * Mult is 1 or 2 according to whether G² ≤ e.
* Per-shift check (`scripts/z78_r2xr_q5check.py`), 3000 sampled shifts across both modes:
  * the class counts are taken in class −M mod e for small e, and in class −1/4 mod f for small f;
  * no violations.
* Combination: see R2-F1.

## 3.5 `local` (K=9, 11, 13 at 293)

* Byte-identical.
* Proof checks:
  * `lg` gives a lower and an upper bound on 16·log₂, using 9-bit mantissas and `lo[a+1]+1`.
  * The V upper exponents (additive a, and +1) are each covered by one extra sixteenth.
  * The (a,d) cofactor is exactly e, so e ≤ V/f is used correctly for the bucket.
  * The cofactor index diameter is ≤ V·w/f_min², with rev = 2^⌈h/16⌉+1.
  * For (a,c), only the length is used.
  * The suffix sums over the e-bucket are correct for "e ≥ 2^j".

## 3.6 `layers.c` (round-2 finite, H=1)

* Exponents:
  * V bounds B+2, B+c+2 and B+2c+d+6;
  * f ≥ 2^(s+1);
  * cofactor lower bounds B−s−6 (using N ≥ 2^(B−1), f < 2^(s+5)) and B+2c+d−s−4;
  * position counts ≤ 2^(max(0, v+w−2f)+1);
  * hist key h = B−s ≥ log₂ e.
* `dyad.py` sums and reverses consistently with the ledger's `(j0, list)` format.

## 3.7 Integer tails (§8)

* **P (`z78_r2scale.c`, `z78_r2tail.py`).** I re-derived the following:
  * the box constraints s ≤ B−J and 2x_a + x_d ≤ B;
  * the dividends N+4a²d ≤ 3N ≤ S^(B+2), Nc+a ≤ S^(B+C+1) and 4Nc²d+1 ≤ S^(B+2C+D+3);
  * the cofactor lower bounds;
  * the chunk count ⌈n/(⌊S^u⌋+1)⌉ ≤ (K+1)S^max(0,w−u), valid for real S;
  * the small-side band 2τ(M)[1+2⌈√(M/t)/t⌉] ≤ (6+4S^((B−3i)/2))τ(M), with the 4τ(M) band for e ≥ N^{1/3} (z77);
  * BBR with H ≤ S^l/4+1 consecutive M: 1.528⌈m^{1/3}⌉ ≤ 2N^{1/3} and log N + 2 ≤ (B+2)(S/2)²;
  * the growth bookkeeping in `rate`;
  * normalised decay (S/2)^(−G);
  * `globalP` rounding (`rootup−1` in the denominator).

  The scale rows 148–320 replay byte-identically. A worked check at 293: the first N≥2^320 is at k=41, and coef₃₂₀ × geom gives 7 ppm.
* **Q (`z78_r2qtail.py`).** Re-derived:
  * acd ≤ F (a≤b), so min(ad,ac,cd) ≤ F^{2/3};
  * f·b = Fa+c and f(4bcd−F) = F²+4c²d;
  * the ℓ=3, m=1 chunks give ≤2 divisors each, with ≤ 1+V^{1/3}/(4g) chunks per octave;
  * octaves: f ≤ F+2, so bins ≤ log₂F+2 ≤ b+2;
  * the prefactor log-derivative is ≤ 3/ln F ≤ 1/12 for F ≥ 2^79 (the code starts at bit length 80, i.e. F ≥ 2^79, consistent with §10);
  * at 293, k=11 gives 1354 ppm.
* **Integer only.** No libm or float enters `z78_r2ledger.py` or its imports. `z78_bbr` uses ⌈694·bits/1000⌉ ≥ ln m. `Decimal` is imported in `z76_lift` but not used on these paths.

## 3.8 Ledger nesting (`z78_r2ledger.py`)

* The depth-3 exact set is a union of whole depth-3 cells and is inverse-stable. Each P_k step therefore sees a union of whole depth-(D−1) parents, and Q₅+ is subtracted only at the end.
* The conditional map is monotone in A, so evaluating it at the lower bound `lv` is valid.
* Mixing per-level unconditional and conditional minima is valid.
* `s` replacements (`packed`/`p9`/round-1 `p7`) are taken as a min of bounds on the same set e<E.
* `c0` for the round-2 p7 cut E uses only c with cutoff t ≤ E. This bounds a superset, so it is valid.
* `ex7` is an unconditional count of new cells.
* Q at depth k uses F=r^k keyed by bit length, valid on (2^(b−1), 2^b].

## 3.9 §11 (slack)

* `z78_r2near.py | diff - near/Pexact.tsv` is identical.
* v is invariant under inversion of units, and slack = L − v, with the arithmetic checked for L=1..8.
* The L=9..11 witnesses are valid tuples with v=3. The intervals [1,6], [1,7] and [1,8] follow from the §6 no-hit controls.
* The labels (CERTIFIED through 8, EVIDENCE above 8) are correctly scoped.
* `z78_r2highnear.c` puts t in the right class for each orientation (t ≡ −1 and t ≡ 1/5 mod 17^j) and enumerates all CF convergents with no break.

# 4. Debate / challenges to the author

* **The margin.** A 2427 ppm margin at the binding prime is fine for a certificate. But the "least certified prime" depends on three point inputs: `exact7` (only r≤389), `qSpecial` (only 293) and `p9` (selected primes). These were chosen *after* seeing which primes were close.
  * This is legitimate, since every input is a valid bound. But the note should say so explicitly, so that nobody reads 293 as the output of a uniform method.
  * There are **no** `exact7` rows for 223..283. Their P₇ is the bound of about 1.1e5 ppm, against about 1 ppm when exact.
  * Setting P₇=0 as a proxy, the margins become:

    | r | margin | margin with P₇=0 |
    |---:|---:|---:|
    | 271 | −122075 | −6612 |
    | 277 | −122391 | −14809 |
    | 281 | −55864 | **+64456** |
    | 283 | −122773 | −13518 |

  * So an `exact7` run at 281 would very likely certify 281 as an *isolated* prime. It does not lower the uniform threshold, because 283 still fails by about 1.4e4 ppm, mostly from P₉ and P₁₁+.
  * Recommendation: run `exact7` for 223..283 for completeness. Lowering the threshold below 293 needs exact or better-sieved P₉ (depth 5), not more tuning.
* **Is "integer-only on [293,919)" true?** It is true for the round-2 code paths. They still use the round-1 integral tables (`data/z78/layer` at b=123, 140 for 293, and `data/z78/p7` in `s7base`), which round 1 replayed. The §0 label should name them, in addition to "BBR + z76/z77 lemmas".
* **P-tail and row 320.** See R2-F5. This is not a current error, but a future edit that adds a B≤N row with smaller G/B would silently break soundness. A one-line guard would prevent it: assert G/B ≥ 2/320 for every row used at the tail start.

# 5. Files (new; no author code or master edited)

* `scripts/z78_r2xr_p7.c`, `scripts/z78_r2xr_p7new.py`, `scripts/z78_r2xr_p7run.sh`: independent exact P₇.
* `scripts/z78_r2xr_exact3dump.c`: the round-1 engine plus a depth-3 bitmap dump.
* `scripts/z78_r2xr_rows.sh`: full-range rows replay.
* `scripts/z78_r2xr_shiftcheck.py`, `scripts/z78_r2xr_shiftcheck_lib.py`, `scripts/z78_r2xr_q5check.py`: per-shift lemma checks.
* `scripts/z78_r2xr_qspecial.py`: the `qSpecial` reconstruction.
* `data/z78/xreview/r2_rows_replay.tsv`, `r2_p7_independent.tsv`, `r2_shiftcheck.txt`, `r2_qspecial_reconstruct.txt`.
* Not stored, but re-checked byte-identically in this session: `p9/z293.txt`, the `local` 293 rows (K=9, 11, 13), `qSpecial/shifts.txt`, the first four rows of `scale.txt`, and `near/Pexact.tsv`.

Replay: `bash scripts/z78_r2xr_rows.sh 293 911 out.tsv` (split it into chunks: 293–560, 561–760, 761–860 and 861–911 took 4.6, 11.2, 8.8 and 5.0 min). `bash scripts/z78_r2xr_p7run.sh r [E]` takes 4–10 min per prime.
