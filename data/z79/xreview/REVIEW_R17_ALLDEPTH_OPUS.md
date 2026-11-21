# Cross-lab hostile review: `notes/z79/R17_ALLDEPTH.md` and `scripts/z79_*` at dcfcc2cc2

Reviewer: Claude Opus (subagent). Scope: the single commit `main..dcfcc2cc2`. I replayed everything, ran independent checks of
the lemmas and code, and did ablations. Constraints observed: writes only under `data/z79/xreview/`, `ulimit -v 2000000`,
timeouts ≤1750 s, `uv run --offline --no-project python -B`, no side agents.

## Verdict

**Sound as far as I can check. Recommend acceptance as PROVED (computer-assisted, rel. z78/BBR), with cross-review still owed
from the other lab (Astra) per AGENTS §3. This is one independent hostile review, not the full gate.** The new threshold
statement (positive sterile measure for every prime r≥241, and for r=233) holds conditional on the inherited z78 inputs, which
I did not re-audit here. All five replay stages reproduce byte-for-byte. The tightest prime, 263, was cross-checked with an
independent engine and a per-box brute force. No soundness defect found. There are several presentation and scoping issues
(below); fix them before export. None changes the result.

## 1. Replays (all byte-identical, no diff output)

| stage | time | result |
|---|---|---|
| `ledger` | 9 s | matches `data/z79/ledger.txt`; the awk check passes: 10 primes (233, 241…283) have positive floor margin |
| `layer` (k=7…17) | 91 s | matches all six `layer/*.txt` |
| `p7` (223…283) | 7 min | matches all 14 `p7new/*.txt` |
| `low` (17…53) | 3.6 min | matches `low/rows.txt`, including the M17B assertion at 17 |
| `q5` | 19 s | matches `q5shift.txt` |

Logs: `replay_*.log`.

## 2. What is load-bearing (ablation, `ablate.py`, `ablate2.py`)

Margins in ppm for r = 233, 241, 251, 257, 263, 269, 271, 277, 281, 283:

* base: 17615, 80928, 28821, 43709, **4205**, 37545, 74921, 21191, 132609, 53376. The exact rational margin at 263 is
  4205.45 ppm, about 1.3 % of the live mass. This is thin.
* without any z79 layer table: 7 of the 10 primes fail. Removing only k=9, k=11 or k=13 also breaks 263.
* without the p7new rows: 9 of the 10 primes fail.
* player without the **4/9/25 squarefree wheel**: 263 fails, at −33146 ppm.
* player without the **Vandermonde midpoint gain**: 263 fails, at −25276 ppm.
* player without the **Minkowski line bound**: no change at any certified prime.
* **Split/τ long-shift route**: it never wins at a certified prime. The routes chosen at every level are exact (k=7), then
  det (k=9…23), then global.
* **q5shift**: it is not load-bearing. Its 14 primes are 163…239 without 233, and all of them fail anyway.

So the new theorem rests on three things: the p7new counts, the squarefree normalisation, and the Vandermonde gain. The
Minkowski row bound, the split route and the Q5 rows are correct but decorative for the theorem. The note should say so
(see §6).

## 3. Audit of the load-bearing lemmas

**Squarefree normalisation.** Replace d→d/h², a→ah, b→bh, c→ch, where h² divides d and h is prime to r. This preserves:

* 4abd = N+e, a+b = ce, t = acd, both centres, a≤b, and e (so the cutoff bucket is unchanged);
* 2a²d≤N and t≤(N/e+1)/2, so the normalised tuple stays inside the player loop bounds;
* the unit filters.

The box count is a bound on centres, so restricting the d-in-pair routes to wheel-admissible d is valid. The d-varying
route (m=1) correctly keeps the full interval. The `sf()` wheel counter was checked against brute force (20000 random
intervals). ✓

**Vandermonde gain.** I reconstructed PL §3. Take the polynomials V^{m−k}(Z−z₀)^k for k<m and Z^{k−m}(Z−z₀)^m for k≥m.
They have degrees 0…ℓ−1, so the determinant is *exactly* ±V^{binom(m+1,2)}·∏_{i<j}(Z_j−Z_i), and row i is divisible by
f_i^m. The plain product of differences therefore enters, and the midpoint split is legitimate:

* same-half pairs have differences ≤D/2;
* the same-half pair count h(h−1)/2+(ℓ−h)(ℓ−1−h)/2 is convex in h and minimal at h=⌊ℓ/2⌋.

Brute force over all ℓ-subsets of {0..D} (ℓ=3,4,5,6,8, small D) confirms max∏ ≤ D^s/2^g. In the code,
`16ks < a+16g` matches the stated inequality, and rounding is outward (v up, lb down). The m=0 and a≤0 cases yield only
k=0 chunks of 2, which is trivially valid. capk entries depend only on (v,f,i), so persistence across primes is harmless.
Out-of-range entries fail closed (the bound reverts to w). ✓

**log tables.** `log16.txt` equals bit_length(i^16)−1 for all 512 entries. `lg()` upper and lower rounding was checked by
hand. ✓

**Per-box implementation test (`brute.c`, independent of the author's code).** I enumerated every a≤b P tuple with e≥2^jmin
and wheel-admissible d by direct (a,c,d) search, testing f | N+4a²d. I mapped each tuple to the player's grid box and
compared against the per-box bound z emitted by an instrumented player (`pl_box.c`). Cases: (r,K) = (17,7), (23,7), (29,7),
(17,9), (59,5), (101,5), (139,5), (263,5).

* No tuple fell in a non-enumerated box.
* No bucket violated j≥⌊log₂e⌋.
* No box count exceeded z. The ratio max is 1.0, attained on singleton boxes.

This validates the loop truncations, the hi/bucket logic and the cap arithmetic, at small sizes only.

**P7 rows.** I re-derived the completeness of `z78_r2p7exact` (small e): the divisor/allocation enumeration is exhaustive,
the residual is prime, and the ≤33-trials branch is complete. The cf side (e≥E) skips only square or L1-covered first
digits. `u.L1.tsv` is the *covered* set (`l1cov`), as required; if it were the live set the count would be an undercount.

I then re-ran the z78 Opus engine `z78_r2xr_p7.c`, which shares no code with the author, at the tightest prime 263 and at
233, with E=3r³:

* 263: small 1558 and large 463 nonsquare tuples; 2709 distinct centres, 1612 new cells. That is ≤ the charged 3510.
  1558 + 197 live-digit distinct large centres = 1755 = 3510/2, an exact match to the author's rows.
* 233: 1409 + 262 = 1671 = 3342/2, an exact match.

Note that P7 costs only 1–2 ppm. Its load-bearing role is to replace a large det/global charge.

**Long-shift split (not load-bearing, but checked).**

* The identity w=c²d=(N+e)(a+b)²/(4abe²) and the monotone bound hold.
* f and f* both divide 4Nw+1, since (4acd−1)(4bcd−1)=4c²dN+1. So a single τ covers both orientations.
* t=(1+a/b)(N+e)/(4e) gives T.
* The inverse-doubling over an inversion-stable live set is valid.
* The update is monotone in A, so it stays valid even if `live` goes negative; the `max(0,·)` of z78 is not needed.
* τ_major is pure integer.
* With H=1, cbal=0 reduces exactly to z78's T. ✓

**Minkowski row bound (not load-bearing, but checked).**

* j ≡ v₀i − (V+v₀)/u mod u, from expansion mod u².
* The dual lattice has index u.
* The diamond has area 2R²/(IJ) ≥ 4u, which gives R=√(2uIJ).
* Number of values ≤ 1+⌊√(2IJ/u)⌋; at most 2 hyperbola points per line.

A random brute force (3380 rectangles on highly composite V) found 0 violations. The code's rounding is outward and lgmod
uses lower logs. ✓

## 4. Non-certificate claims

**Q descent at 17.** The derivation checks:

* a²+5b²+h=Vab with V=4dh−6; the integral reflections when 5|V; the stopping inequalities 2a≤Vb and 10b≤Va;
* h≥(2dh−3−√5)ab, hence dh=4 and so d=1, h=4;
* the centre −(2a)² is a square (17≡1 mod 4), while 5 is a nonsquare mod 17.

d and h are fixed along the descent because V and h are invariant. Brute force over d<40, h<200, b<4000 finds solutions only
at (d,h)=(1,4). ✓

The remark "pma²+q≥F" is true but unexplained in the note. It follows from b≡−pa/q mod F and mab≡1, which give
F | pma²+q. **Add this one-line reason.**

**Four-index endpoint search.** The exponent bookkeeping is correct: e·HZ·J·(Hd)² ≪ (U/d)(a²d/U)(U/a)² = U². The listed
constants agree with z78 §6 and ENDPOINT (2.1). Two points:

* The bound e≤2p(12+|D|)a needs M≥4Cq from (2.1), which needs U≥10⁶. That is stated.
* This is an algorithmic claim with **no implementation or run**. "PROVED" is acceptable for the inequality, but the search
  itself is unexecuted. The wording "There is a fourth indices search" is garbled; it should read "a four-index search".

**Cylinder of 5 at 17.** The numbers match `low/rows.txt`: 108+58−0, 113122/17⁵, 54/29 → 5/2 → 0/0. The code computes them
as exact conditional counts above cell 5. The 29 overlap (2 cells) is real. The qualitative caveats (no 1/r^j saving,
nothing bounded below one at 17) are appropriate.

**r=13 falsifier.** Verified independently by direct Q1 search: the centres are {2,5,6,7,8,11}, i.e. all six nonsquares. ✓

## 5. Residual risks (not refuted, not checked here)

1. **Inherited z78 inputs are the dominant unaudited mass.** At 263 these are:
   * the exact depth-3 complement;
   * finite Q at 31247 ppm (z78 Q tables and qLocal);
   * the packed short-shift bound `sh`, which enters every det charge;
   * the z78 dyadic/local P layers at k≥15;
   * the 'global' P charges at k≥25, about 6000+5000+… ppm;
   * the tails at 8 and 1893 ppm.

   The z78 round-2 Opus review covered these. A defect of ≥4205 ppm in any of them would sink 263.
2. **Thin margin at 263 (4205 ppm)**, with 277 (21191) and 233 (17614) next. The statement is a rigorous bound, so the
   margin size matters only for error tolerance. Still, a second-lab replay should concentrate on 263.
3. **The per-box brute force is limited to N ≤ 263⁵.** The load-bearing tables are k=9…13 at r≈263, with N up to about
   2^105. Correctness there rests on the proof plus the code audit, not on direct testing. 128-bit ranges: N≤2^114 is
   asserted, and products such as `4*(An-1)^2*(Dn-1)` are bounded by 2a²d≤n. I found no overflow path, but I did not
   instrument it.

## 6. Form / scoping defects (fix before export)

* **Load-bearing disclosure.** State explicitly that the threshold rests on three ingredients: the wheel, the midpoint gain
  and the p7new rows. The Minkowski row bound, the H-split τ route and the 14 Q5 rows contribute nothing at the certified
  primes. At present the note presents them as part of the certificate. The phrase "For 14 primes use z78's Q5…" in
  particular suggests relevance.
* **`z79_pbudget.py` docstring.** It mentions an "optional complement of an explicit list of initial whole t-values", which
  is not implemented. Remove it.
* **Terse or cryptic phrases.** "use a limit for equality", "There is a fourth indices search", "Try e, J, Hd, HZ". Readers
  will need a sentence each.
* **STATUS delta.** It covers STATUS only. FRONTIER's "uncrossed sufficient-threshold gap 17≤r<293" also needs to become
  "17≤r<241 except 233" at export. No WAVES line yet; that is the orchestrator's job per AGENTS §2, so this is acceptable
  for a lane commit.
* **Data ordering.** `q5shift.txt` rows are unsorted. This is cosmetic.
* **Label.** "inherited theorem above 283" is correct for primes, but "≥293 (z78)" is clearer.

## 7. Suggestions (cheap margin)

* **Replace the one-level midpoint split with the sharp Fekete/Jacobi maximum.** For ℓ points on an interval of length D,
  max∏|x_i−x_j| ≈ (D/4)^s·e^{O(ℓ log ℓ)}. It is known in closed form via the discriminant of Jacobi polynomials (Stieltjes
  and Schur). Recursive bisection alone also gives more: apply the midpoint split inside each half. The sharp maximum, by
  numerical optimisation on [0,1], gives these gains: ℓ=4: 2^5.8 (vs 2^2); ℓ=6: 2^19.0 (vs 2^6); ℓ=8: 2^39.6 (vs 2^12);
  ℓ=12: 2^104 (vs 2^30). A certificate needs the rigorous closed form, not these numbers. Since the gain is load-bearing at around 30000 ppm at 263, this could plausibly push the
  threshold to 239 or lower, without new arithmetic.
* **Drop or demote the Minkowski and split routes.** Alternatively, report which (r,k) they ever win.

## Files

`ablate.py`, `ablate2.py`, `tags.py` (load-bearing analysis); `pl_{nosf,nogain,nolines,box}.c` and `layer_*` (ablated and
instrumented player); `brute.c` (per-box brute force); `checks.py` (log16, Vandermonde split, wheel); `checks2.py` (Q descent,
Minkowski); `r13.py`; `xp7/` (independent P7 at 233 and 263); `replay_*.log`.
