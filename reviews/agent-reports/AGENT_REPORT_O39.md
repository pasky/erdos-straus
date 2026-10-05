# AGENT_REPORT_O39 — Chen–Wu switching for two windows (branch `side-agent/window-switching`)

Deliverable: `POINTWISE_WINDOW3.md` (§§1–8), scripts `scripts/window3_*.py`, Wu 2004/2008 archived
in `sources/window3/`. Merged `side-agent/window-parity` first (as instructed); POINTWISE_WINDOW2.md
untouched.

## Answer to O39
**No.** In a faithful version of the WINDOW2 model, Type-I data at level 1/2 + both parities +
Chen-type switched upper bounds do not prove `a_min(p)≥11` for any hard prime, unless the
switched bounds are within a factor ≈2–2.5 of the truth *uniformly over every family a switched
sieve can bound*. The best switched constants that exist are ≥4 at BV level (≈3.91 with Chen's
double sieve, 3.3996 only for twin primes with BFI-type levels). No unconditional proof skeleton
was written (goal 3 not reached). The obstruction is recorded as a precise numerical gap.

## Main findings (labels as in the file)
1. **R29-M4 repaired (§2).** The continuum heuristic law is product-form and parity-blind to
   ≤0.3% already at ε=0.1. The 87% spread R29 saw came from WINDOW2's point-mass binning. With the
   cell-integrated law, r(S)∈[0.99999,1.00001] and |r_even−r_odd|≤2.7e-3 (EVIDENCE, quadrature).
   With this law the one-window value at θ=1/2 is 0.4893 (cert, ε=0.1, K=8). WINDOW2 had 0.744.
2. **Faithful switching constraint (§1, §3).** A real switched sieve on `n_q=m·r` bounds
   *aggregates* over the other window's configuration. Per-configuration caps are not available.
   Marginal caps (SW_K) need K*∈(1.07,1.1), i.e. an essentially perfect upper bound.
   Mechanism: the fake inflates "window q' clean, window q has two bad primes" by ≈2.2×.
3. **Families that also sift the other window (§4).** Real constants, from composing the linear and
   semi-linear upper sieves: K(ζ)=4 (ζ=ε), then 8.1–14.7. Even with a uniform K for *every*
   family (prefix Z, including ζ=1), positivity needs K*∈(2,2.5) on (ε,K)=(0.1,8). Fakes at
   K=4, 3, 2.5 are verified in 50-digit floating point (Prop 8.1; EVIDENCE, not interval arithmetic).
   The composed constants are worse than the trivial `4/P(no bad point<ζ)`≤8.4 from the marginal cap.
   Real constants are ≥3.9 either way.
4. **R29-M2 answered (§6–7).** Adding good-prime Type-I rows with the good part's conditional law
   *frozen* gives large positive values (0.31 with no switching). That is an artefact of freezing.
   In the full two-type model (bad and good points both free), the LP values are *identical* to
   the bad-only ones for one window on three grids. For two windows the K=4 fake persists and K=2
   gives 0.411 ((0.15,6)).
5. **Robustness (§8).** The K=4/K=2.5 fakes persist on (0.1,10), (0.1,12) and (0.07,9). With
   "outer" visibility, which gives *more* information than reality, fakes persist at K=4 and 3.
   At K=2.5 that variant gives 0.023, so its threshold is (2.5,3]. With K=4 switching, the Type-I level would have to exceed 0.6 (positivity at 0.65).
6. **Constants (§5)**, checked in Wu 2004 §1 (archived): 4 = BV + linear sieve
   (Bombieri–Davenport); 3.9171 (Chen) and 3.91045 (Wu) by the double sieve; twins 3.3996 (Wu,
   needs well-factorable level >1/2 at a fixed residue); ≥2 for any sieve at level 1 (parity).

## Caveats / honest scope
* All model statements are for discrete grids. The continuum threshold is EVIDENCE only.
  Uniform-K threshold: (2,2.5) on (0.1,8); ≤2.5 on (0.1,10), (0.1,12) and (0.07,9). At
  (0.1,12) the K=2 value is ≤0.0574 (stalled CG, an upper bound only). Outer visibility:
  (2.5,3]. Extrapolated continuum K*∈[2,3] (Assessment). It sits just above the
  parity constant 2. The gap to 4 is a factor ≥1.3.
* Positive LP values in the switched LPs are primal-only (the duals are not certified because
  tiny-μ columns blow up the penalty). Only the fakes (value 0) are high-precision verified,
  and only at (0.1,8).
* Scope of "switching": the marginal and prefix/subset families of §1 and §4 only. Other
  Chen-type inequalities are not modelled, and no exhaustiveness is claimed (self-review).
  K=4 as the baseline for the convolution sequences is an Assessment.
* "Model" = Type-I + parity + switched-family upper bounds. Type-II/bilinear information beyond
  switching, and levels >1/2, are outside it (route (ii) is closed as in WINDOW2 §4).
* The semi-linear upper function F_{1/2} is derived from the f quoted in Teräväinen (6.4) via
  the β-sieve delay equations. It was not read in a primary source.

## Self-review (reviewer subagent, deep) applied
Overclaims were narrowed: no exhaustiveness for switching; K=4 is an Assessment; "CERTIFIED" is
now "50-digit verified"; (0.1,12) K=2 is an upper bound only; the H marginal holds up to grid
error, not exactly; the composed K(ζ) is worse than the trivial 4/P; "every constant ≥4" now
reads "≥3.9"; the outer-visibility wording is fixed.

## Not done
(0.05,10) did not finish in 4 h. (0.07,9) K=2 is still running at checkpoint (`data/window3/runs_c.jsonl`). No dual certificates for the positive side. No "all Z"
families beyond 6 cells at K<4. The full two-type model was not run beyond (0.15,6) (size).
