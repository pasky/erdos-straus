# Hostile cross-lab review of `notes/z80/R17_CRUSH.md` (commit 655521c6e)

**Reviewer.** Claude (Anthropic), running as a Claude Code subagent. The harness calls this the "Opus" cross-lab
review. I cannot read an exact model version string from inside the session, so I do not attest to one. The author
lane is GPT-6.2 Astra.

**Verdict.** In every stage I replayed, re-derived or re-implemented, I found **no soundness defect**. There are form
defects, and two of them must be fixed before export:

1. The documented replay command does nothing.
2. The route attribution in the ledger table is wrong.

On the evidence below, the claim "positive sterile measure on the r-generic line for every prime r ≥ 89" holds. It is
PROVED relative to the inherited z78/z79 lemmas and engines, and it is computer-assisted. It says nothing about ES in ℕ.

## 1. Coverage: what was actually done

| stage | author replay (byte-diff vs certificate) | independent re-implementation | ground-truth / falsifier |
|---|---|---|---|
| `prefix` (z80_pshift.c, 10 primes, e<2²⁹) | ✔ identical | ✔ `scripts/z80_xr_pshift.c`, all 10 rows × 30 cumulative columns identical | ✔ truth mode, below |
| `cf` (z78_r2cf.c, 7 primes, e≥2²⁹) | ✔ identical | ✔ `scripts/z80_xr_cf.c`, all 7 counts identical | ✔ brute force, below |
| `q`: qs (z78_r2q5shift) + qboth (z80_qboth.c) | ✔ identical (27+27 rows) | ✔ qboth in `scripts/z80_xr_qboth.py` (Python, exact ints); identical at 13,17,19,23 and all 10 primes 89..139 | ✔ exact enumeration, below |
| `shifts` (z79_shiftwide J=28, 31) | ✔ identical (11.6 min) | ✘ (reviewed z79 engine) | — |
| `runs` (z79_runs via runtables, 17..97) | ✔ identical (4.6 min) | ✘ (reviewed z79 engine) | — |
| `ledger` (z80_crush.py, checks, SHA256) | ✔ identical; checks pass; manifest OK | partial: ablation harness `scripts/z80_xr_ablate.py` mirrors the combiner | r=13, below |

I did **not** re-derive or re-implement the following inherited components:
* the z78/z79 combiner internals: `packed`/`interval`/`fixed`/`tsum` annulus bounds, `globalP`, the scale/tail
  envelopes, the split route and `qnorm`;
* the `z79_runs.c` and `z79_shiftwide.c` internals;
* the z78 Q₅ small-e/small-f compression in `z78_r2q5shift.c`.

These carry their own earlier Opus reviews. Here they are only replayed at new parameters: runs at r = 89, 97 and
shiftwide at J = 31 for 17..127.

## 2. Form defects

**F1 (must fix): the documented replay is a no-op.** The note says "From the repository root:
`bash scripts/z80_crush_replay.sh`". That command exits with status 2 in 5 ms and does nothing. The cause is
`for stage in ${1:-'prefix cf q shifts runs ledger'}`: the quotes inside the default stop word splitting, so the single
stage `"prefix cf q shifts runs ledger"` falls through to `*) exit 2`. I confirmed this both with a bash test and by
running the script. Passing stages explicitly (`bash scripts/z80_crush_replay.sh prefix`, …) works, and I used that
for every replay above.

Fix: `for stage in ${1:-prefix cf q shifts runs ledger}`, or use an array. Until it is fixed, the note's claim
"Every generated stage is diffed…" is false for the documented invocation.

**F2 (must fix): the route column misattributes the load.** I ablated each input in turn
(`scripts/z80_xr_ablate.py DROP r…`). The table gives the resulting margins in ppm and lists the stages that are
load-bearing at each prime.

| r | full | −prefix | −cf | −qboth | −runs | −shift31 | −shift | load-bearing |
|---|---|---|---|---|---|---|---|---|
| 89 | 15841 | −34635 | −7731 | −124949 | −34635 | −34635 | 15841 | prefix, cf, Q₅, runs, shift31 |
| 97 | 81279 | −29778 | 43862 | −35935 | 12366 | 25613 | = | prefix, Q₅ |
| 101 | 29845 | −24202 | −612 | −89283 | = | −22194 | = | prefix, cf, Q₅, shift31 |
| 103 | 24911 | −22229 | −9439 | −102563 | = | −22229 | = | prefix, cf, Q₅, shift31 |
| 107 | 47249 | −23830 | 6262 | −68691 | = | 1609 | = | prefix, Q₅ |
| 109 | 29839 | −21609 | −13259 | −72521 | = | −14804 | = | prefix, cf, Q₅, shift31 |
| 113 | 86690 | −18286 | 32325 | −11288 | = | 43934 | = | prefix, Q₅ |
| 127 | 55602 | −11578 | = | −33098 | = | 30359 | = | prefix, Q₅ |
| 131 | 62912 | 532 | = | 42319 | = | = | = | none singly (prefix OR Q₅) |
| 139 | 60669 | 5954 | = | 43398 | = | = | = | none singly (prefix OR Q₅) |

(The −qboth column also drops the qs pairing, as in `z80_crush.py`.)

Corrections the note needs:
* Q₅ (qboth) is load-bearing at **every** prime from 89 to 127, yet the routes for 89..113 omit it.
* CF is not needed at 97, 107 or 113.
* The K=11,13 short prefix to 2³¹ (`shift31`) is needed at 89, 101, 103 and 109 but is not named as such.
* The J=28 `shift.txt` rows are not needed for any new pass.
* At 131 and 139, prefix and Q₅ are each individually redundant.

**F3 (minor).** Several statements lack file pointers ("PL's divisor parameterisation", "SE §3.1", "II3",
"z77's Q identities"), which AGENTS §3 requires. The weakest new margin (89, 15841 ppm) is not stated in the prose.

**F4 (cosmetic).**
* `z80_pshift.c` contains a thinking-aloud comment ("third residue has no candidate … ? No: always test
  independently").
* `z80_qboth.c` says "a pointwise divisor cap is supplied by caller separately below". No such caller-side cap exists;
  the in-code `cap` is the bound.
* The untracked scratch directory `data/z80/r17tmp/` (binaries and logs) should be removed or ignored.

**F5 (scope sentence, recommended).** The note says the 17 primes 17..83 are "unresolved by this test", but it does
not say why. I ran the decisive new stages there: author `z80_pshift` J=29 plus my CF at E=2²⁹ for 59..83
(`scripts/z80_xr_extend.py`; this is an experiment, not a certificate). P9 then falls to 2–26 ppm, but every margin is
**unchanged** (e.g. 83 stays at −37363). P11+ charges saturate the whole post-P7 live mass (at 59, P9+later P =
151836 ppm = live after P7). The binding layer below 89 is therefore P≥11, not P9 or Q₅. The note should say so,
because it tells the next lane where to work.

## 3. Substance: re-derivations

**Short-shift charge.** Setting: 4abd = N+e, a+b = ce, M = abd, unit parameters.
* **Centres are functions of h.** Put h = a²d. Then M²/h = b²d and h ≡ −M (mod e), because a ≡ −b. Since 4acd·e =
  4h+4M, the centre 1−4acd = 1−4(h+M)/e is a function of (e, h). So #centres(e) ≤ #H_e, where
  H_e = {h | M² : h ≡ −M mod e}. H_e is closed under h ↦ M²/h.
* **Splits.** For any factorisation M = gy, put u = gcd(h, g²). Then v = h/u divides y² even when g and y share
  primes, because gcd(h/u, g²/u) = 1.
* **Orientation.** If u > g, the complement of M²/h is g²/u < g. So every inversion pair has a member with a split
  u ≤ g, and #H_e ≤ 2·#{(u,v)}.
* **One candidate per v.** Since gcd(v,e) = 1, u ≡ −M/v (mod e). For g < e this leaves at most one u ∈ [1,g]. g = e
  forces e = 1, which falls in the e ≤ 32 branch, where τ(M²) is charged.
* **Units.** r | e makes some parameter non-unit, so the skip is valid. gcd(M,e) | N = r⁹, so unit e gives gcd 1.
* **Factorisation.** Y is minimal with Y³ > hi. After removing primes ≤ Y, the cofactor has at most 2 prime factors.
  A composite cofactor has its smaller factor in (Y, ⌊√hi⌋], and the big-prime sieve covers exactly that range, so it
  is recorded. The residue enumeration (key·p mod e), the three-residue special case and all overflows were checked:
  e < 2²⁹, products < 2⁵⁸, and √hi < 2³² fits uint32.
* **Result.** Valid upper bound.

**Truth tests.** My re-implementation has a truth mode. For every e it enumerates all genuine unit tuples and also
H_e, and asserts #centres ≤ #H ≤ bound. It was run at:
* r=13, K=9, J=22;
* r=13, K=7, J=20;
* r=17, K=9, J=20;
* r=89, K=9, J=17;
* r=139, K=9, J=16.

There was **no violation**. #centres = #H in every case; for example, at 89 the bound is 3550 against a truth of 1462.

**End-to-end check at 17..53.** z79 has exact P9 depth-five counts there (`data/z79/low/rows.txt`). Author prefix(2²⁹)
plus CF(≥2²⁹) is ≥ the exact P9 at all ten primes; for example, at 17 it is 2112 against 108.

**CF large-shift count.**
* **Range.** t = acd ≤ ad·2b/e = (N/e+1)/2, so t ≤ ⌊(⌊N/E⌋+1)/2⌋.
* **Legendre.** bf − cN = a with f = 4t−1. The error |N/f − b/c| = a/(cf) is < 1/(2c²) because 2ac < 4acd−1, so b/c is
  a convergent of N/f. A non-primitive tuple with g = gcd(b,c) reduces to (a/g, b/g, c/g, g²d), which has the same t,
  e and centres and stays unit.
* **Break after the first hit per t is valid.** The two orientation centres multiply to 1 + 4c²dN ≡ 1 (mod N), so the
  partner centre is (1−4t)⁻¹, which is unique.
* **Dead-digit rejection.** For all 13 primes checked, I confirmed that squares ∪ P1 ∪ Q1 is inverse-stable mod r.
  Per hit, my CF also checks that both orientation digits agree (0 mismatches over all 7 primes) and asserts
  A·B ≡ 1 mod W.
* **Independence of my CF.** It tests every convergent with the sign computed explicitly and does not rely on parity
  bookkeeping.
* **Brute force.** Exhaustive (a,c,d) enumeration agrees exactly with both CF implementations at: (13,9,2²⁰),
  (17,9,2²²), (19,9,2²²), (89,9,2⁴⁰), (13,7,2¹²) and (113,9,2⁴²).

**Q₅ both-large charge.** Setting: 4abd = Fe+1, a+b = ce, f = 4acd−F, a ≤ b.
* **Basic identities.** e(4acd−F) = 4a²d+1, so ef = 4a²d+1. Then 4w(ef−1) = (4acd)² = (F+f)². From a ≤ b,
  ef ≤ Fe+2, so f ≤ F+2.
* **w ceiling.** Write w = (F+f)²/(4(ef−1)) ≤ A(f)B(f), with A = f+2F+F²/f and B = f/(Ef−1) decreasing. A(T) ≥ A(F+2)
  is equivalent to F² ≥ T(F+2), which holds for T ≤ F/2. So wmax = ⌊(F+T)²/(4(ET−1))⌋.
* **Clipping.** Ef ≤ 1 + (F+h)²/(4w); the floors compose correctly.
* **Divisibility.** f | V = F²+4w and gcd(f, 4cd) = 1. The split f = f₁f₂ with f₁ | g ≤ u leaves at most one f₁ per
  f₂, giving τ(V/g). Leftover primes are > 251, so the 252-division loop overcounts Ω and τ ≤ 2^Ω. Absorbing y into g
  when y ≤ u/g is valid.
* **Short-progression path.** It counts only genuine tuples: b = ce−a gives 4abd = Fe+1 identically.
* **Region partition.** The partition (e<E | e≥E,f<T | both large) is in the a ≤ b orientation, consistent with
  qs = e + 2f.
* **Result.** Valid.

Exact counts, using `scripts/z80_xr_qboth.py`:
* **Method.** GNU `factor` on every V and a full divisor scan. Per (c,d) the script asserts 2·exact ≤ charge and that
  every exact f ≤ the clipped h.
* **Outcome.** No violation at 13, 17, 19, 23 or any of 89..139.
* **The w ceiling lemma, empirically.** Scanning to 4·wmax at 13..23 finds 0 solutions beyond wmax.
* **The bound is very loose.** The exact both-large counts (×2) are 140, 120, 186, 198, 208, 120, 168, 256, 180 and
  222 for 89, 97, 101, 103, 107, 109, 113, 127, 131 and 139. The charges are 1.6·10⁷ to 1.1·10⁸.
* **Recommendation, not a defect.** Replace qboth by this exact enumeration: it takes 1–5 min per prime and gains
  roughly 2–3k ppm per prime. It cannot rescue 83 (F5).

**Ledger combiner.**
* The new rows enter only as minima with existing bounds:
  * prefix enters spbig/seeds, where v[j] is the cumulative count for e < 2^j;
  * CF enters as the fine-grid large-shift count at j = 29;
  * runs enter by min-merge, padded with the trivial W;
  * Q₅ enters as qLocal = min(old, qboth + e + 2f).
* In `cost()`, the large-shift charge at a cut E may use the minimum over cuts t ≤ E, which is valid because e ≥ E is
  a subset of e ≥ t.
* No overlaps are subtracted and there is no independence assumption; all costs are Fractions. The ppm columns are
  ceilings and the margin is a floor of the exact value.
* **Margin stability.** Margins at r = 137 and at 149..283 are unchanged from z79, and the old passes are retained.

## 4. Falsifier r = 13

* **Ledger.** At r = 13, union.tsv gives l1 = 1014 = 6·13², so all six nonsquare digits are covered, which matches the
  inverse-stability check. The initial live mass is exactly 0. The z80 combiner returns a margin of −2427694 ppm, so
  nothing is certified. This is the correct behaviour. At ledger level the test is necessarily weak (it fails at
  init = 0), so the informative r=13 content is stage-level.
* **Stages.** At r = 13 the prefix bound is ≥ truth (948 ≥ 426 at K=9, J=22; 590 ≥ 268 at K=7). CF equals brute force,
  with **0 live t**, consistent with every digit being dead. qboth's charge 2796 is ≥ 2·exact = 24, and nothing lies
  beyond wmax.
* **Conclusion.** No stage manufactures live mass where none exists, and no stage under-counts genuine tuples.
* **Two-prime x\* control.** The II3 control in `z80_crush_checks.py` is pure residue arithmetic. It passes, and I
  did not re-derive its provenance (z78 endpoint §5).

## 5. Debate points / residual risk

* **Unreviewed new parameter ranges.** The decisive charges now also rest on two reviewed engines used at parameters
  never used before. One is z79_runs at r = 89, 97, needed at 89. The other is z79_shiftwide at J = 31 for K = 11, 13
  at 17..127, needed at 89, 101, 103 and 109. Both replay byte-identically, and their input asserts cover these r. They
  were not independently re-implemented here. A second reviewer should target `shift31` at 89 and 109, which have the
  smallest margins (−34635 and −14804 without it).
* **Smallest margins.** 89 (15841 ppm), 103 (24911) and 109 (29839) are robust to ppm rounding but rest on the full
  stack of inherited envelopes, the high tails and the libm qualification at r ≥ 919.
* **Inherited Q₅ compression.** The small-e and ×2 small-f Q₅ compressions (qs) are inherited z78 logic and were only
  replayed.
* **STATUS wording.** The STATUS delta should read "every prime r ≥ 89", keeping the r ≥ 919 libm qualification and the
  depth-14 qualification at 17. It should also drop "+137".

Reproduce (from repo root; all writes are under scripts/z80_xr_*, data/z80/xreview):

```
bash scripts/z80_crush_replay.sh prefix   # likewise cf, q, shifts, runs, ledger
gcc -O2 -o /tmp/xps scripts/z80_xr_pshift.c && /tmp/xps 89 9 29            # [truth] for small J
gcc -O2 -o /tmp/xcf scripts/z80_xr_cf.c && /tmp/xcf 89 9 536870912 DIGITS [brute]
uv run --offline --no-project python -B scripts/z80_xr_qboth.py 89 5 [wfactor]
uv run --offline --no-project python -B scripts/z80_xr_ablate.py cf 89 101
```
