# AGENT_REPORT_O242 — the sibling conjecture: positional input at q = 3 and r = 17 (SIBLING.md)

Branch side-agent/sibling-conj (merged side-agent/sterile-diophantine and side-agent/review-sterile-dioph for reading).
Main file SIBLING.md; memos BRAINSTORM/z17_{perkey,poisson,window,uniform}.md; scripts scripts/z17_*; data data/z17/.
ES is not solved; no infinite case of ES or ES_q is claimed; **the sibling conjecture (SD Conj 3.3), Conjecture 0.2 and r = 17
sterility are NOT proved.**

## SHARP
1. **Uniform multiplicity on the r-generic line (Conjecture 4.2, EVIDENCE).** For every prime 17 ≤ r ≤ 61 (complete to
   depth 4), r = 19, 23 (depth 6), r = 17 (depth 8): from depth 4 on an alive parent never holds more than **3** boxes of the
   next level (≤ 5 at depth 3), for every r. With SD Lemma 3.1 the bound "≤ 3" (even "≤ r − 1") for one r gives sterile
   r-generic points with dim ≥ log(r−3)/log r. STERILE_LOWER proves sterility for r ≥ 2^{21.44} and shows level 1 leaves room
   exactly for r ≥ 17 (r ≤ 13: every non-residue cell covered at level 1, re-derived here). So **one uniform multiplicity
   statement would give sterile points for every prime r ≥ 17 — a sharp threshold at 17.** It is a B2-type pointwise bound
   (Type II points with a/b in a thin class), on average true for L ≥ 4 (ET exponent: r^{0.6−0.2L} per class).
2. **Counts do not localise (Prop 3.1, PROVED for route bounds).** Inside a cylinder of depth n, every route-type bound
   (SP Lemma 1.6 routes + sharp divisor bounds + the localised Bezout route) is ≥ 3^{2s/5} at the Elsholtz–Tao point, so it
   controls balls inside V only from level (5 + o(1))n on — the same threshold as the global bound. Answer to R248 D3 in
   quantitative form: counts *could* suffice globally (exponent 2/5 < 1/2), but the window (n, 5n] inside the cylinders that
   Lemma 3.1 visits needs positional input; with certified constants a depth-n cylinder needs complete control to depth
   ≈ 40 + 4.5n.
3. **The q = 3 sibling data are Poisson (EVIDENCE + calibration).** Sibling pairs among all balls/boxes match b(b−1)/2/#parents
   at q = 3 (depth ≤ 9) and r = 17 (depth ≤ 7); independent placement predicts 0.145 full alive parents over depths 3–9
   (P(none) 0.86) — so SD's "never 3 children" is weak evidence by itself — but ≤ 10⁻³ beyond depth 9.

## Results (labels)
* PROVED: Lemma 1.1 (function-field Lenstra per key: ≤ 2 balls per (m', g', s, a) in a parent — the modulus T^N m'g' always
  satisfies 3 deg Q > deg(1 + T^s m'g'²)); Lemma 1.2 (≤ 6 P-boxes per (c, d) in a class mod r^{L−1}, r ≤ 17); Prop 1.3
  (Case B balls invariant under u ↦ u(−T), u ↦ 1/u, ι(u) = 1/u(−T); T ↦ −T is a symmetry because of OA's parity law);
  Prop 3.1 (window (n, 5n]); Cor 4.1 (pair-count forms: Π_N ≤ 2 for N ≥ 9 ⟹ Conj 0.2 on X_c; Π_N = 0 eventually ⟹
  dim ≥ log₃2; r = 17 analogues); consequence of Conj 4.2.
* EVIDENCE: §2 tables; siblings never share a key (14 pairs, q = 3); Case A balls break the inversion symmetry (24 of 172
  balls, all Case A, have no ball at 1/u); child digits of ball centres uniform (no "digit law"); r-landscape.
* CONJECTURE: 4.2 (uniform multiplicity). Assessment: higher root-product laws (wild symbols) give no tuple-free constraint.

## Replay
```
python3 scripts/z17_ffpairs.py data/z16/balls_d9.txt                    # data/z17/ffpairs_d9.txt
PYTHONPATH=scripts uv run python scripts/z17_ffsibkeys.py /tmp/fc17.txt 9 # census from bsE_famcount 3 2 17 print (O241 replay); ~5 min
python3 scripts/z17_iota.py data/z16/balls_d9.txt ; python3 scripts/z17_poisson.py
scripts/z17_rrun.sh 19 6 /tmp/z17r19 ; python3 scripts/z17_rtree.py /tmp/z17r19 6 19   # ~10 min; r = 23 ~1 h (K = 11)
for r in 5 7 11 13 29 31 37 41 43 47 53 59 61; do scripts/z17_rrun.sh $r 4 /tmp/l$r; python3 scripts/z17_rtree.py /tmp/l$r 4 $r; done
python3 scripts/z17_zpairs.py DIR 7 5        # DIR = O241's r = 17 box directory (see AGENT_REPORT_O241 replay)
```
z17_penum.py reproduces data/m17b/p5, p7, p9 at r = 17; the level-1 survivors (17: {5, 7}, 19: {2, 3, 10, 13}, 23: {5, 14})
agree with STERILE_LOWER Comp. 4.1 (independent engine).

## r = 17 depth 8 (completed after the checkpoint)
EVIDENCE, complete: **D_P(15) = 2881** P-data at K = 15 (new exact count; D_P(13) = 1463; M17D's measure route would need
≤ 2.5·17⁶ ≈ 6·10⁷), stored as `data/z17/p15_r17.txt.gz` (sha256 `42b1a566…`). Engine: z17_penum.py regimes e, ad (≈ 10 h) +
the new `scripts/z17_penum2.py` (regimes ac, cd with rebalanced thresholds Xcd = 1.1·10⁶, Xac = 21864493 — cover inequality
asserted — sharded 15 + 9 ways, per-chunk progress and checkpointing; ≈ 2.5 h on 24 processes; validated by reproducing
data/m17b p9, p11 exactly with a non-default split). Tree (`data/z17/rtree17_d8.txt`): depth 8 in C₅ = C₇ has 326 new boxes,
**every alive parent holds ≤ 1**, alive fraction 0.67712. 17-ary maxima at depths 2–8: 4, 4, 2, 2, 2, 1, 1.
Replay: `ZR=17 z17_penum.py 15 e ad`; `ZR=17 z17_penum2.py 15 {ac|cd} 69841226 1100000 S j OUT` for all j < S; sort -u the union;
`z17_rtree.py DIR 8 17` with DIR = data/m17b p1..p13 + p15 + O241's Q/U k ≤ 7.

## What did not work / limits
* Pair correlation (S1): no structure beyond counts in the data; per-key Lenstra bounds the wrong quantity (keys vary).
* Symmetries: involutions fixing a parent have a fixed child, so they never forbid a full triple.
* Higher reciprocity laws: tame laws only see E(0); wild laws bring in v₁.
* Localised counting: Prop 3.1.

## Sparks (not pursued)
* S1' Uniform multiplicity at depth 2 alone (level-2 boxes in a cell < r for all r ≥ 17) is a statement about Type II points
  of 4/r³ landing in one cell; maybe provable via the explicit structure of Σ^II_{r³} (small N-points), and it is the only
  place where the data come close (14 of 47 at r = 47).
* S2' The dilation (λa, λb, λc, λ^{−2}d) produces repeated boxes (seen in both r = 17 clustered parents): count boxes by
  primitive data only; multiplicity per class of *primitive* data may have a cleaner bound.
* S3' Case A breaks u ↦ 1/u at q = 3 while all ℤ box types are inversion-closed: is there a missing "Case A⁻¹" family type in
  the FF model, or is the asymmetry genuine? (If missing, coverage at q = 3 is underestimated.)
* S4' Poisson model with the true ball-count growth suggests proving Π_N ≤ 2 via a *second-moment* count restricted to
  pairs inside alive parents at the 3^{d/2} scale — needs a pair-count version of SS Cor 4.2 with exponent < 1/4 per level.
