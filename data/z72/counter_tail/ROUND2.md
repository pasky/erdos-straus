# A structural shift-15 test and a closed four-unit orbit

Result: an exact criterion for shift 15 at p ≡ 1 (16) (and the ⟨2⟩-index-2 mechanism). The pair-move orbit of (p,p,p,p) at p=14281 is closed (92 vertices) with no mergeable pair, although 4/14281 has a triple.   Label: PROVED (shift-15 criterion); CERTIFIED (c15 sample, closed orbit, census to 20000)
Scope: rules out universal merge-reachability from the four-equal start; nothing about other starts or ES.
Review: cross-lab (Opus) `data/z74/xreview/REVIEW_Z72PHASE_OPUS.md` (P16–P18 CORRECT; own generator and BFS)
Triage: METHOD-CX
STATUS delta: none
*(§0 block: z74 Opus xreview fix)*

**PROVED — exact shift-15 obstruction.** Suppose `p≡1 mod 16` and `gcd(p,15)=1`. Put `K=(p+15)/4=4Q`, `H=<2>={1,2,4,8}` in `(Z/15)*`. The following are equivalent:

* a coprime `AB|K` with `15|A+B` exists, without a support cap;
* one exists with `ω(AB)≤2`;
* some prime divisor `q|Q` lies in `{7,11,13,14}` modulo 15, i.e. outside `H`.

If every factor lies in `H`, then `A/B∈H` and cannot be `−1`. Otherwise `q∈−H` since `H` has index 2 and `−1∉H`. Choose `j∈[−2,2]` with `q·2^j=−1 mod 15`; the residue cycle has length 4. Split the ratio `q·2^j` into its coprime numerator and denominator: their product divides `4q|K`. In particular the criterion uses *individual* primes of `Q`, not the character of the product (which can hide an even number of exceptional factors). No fourth prime-tuple condition is needed.

**Mechanism.** More generally for an odd shift `c` coprime to `K`, suppose `H=<2> mod c` has index 2 and omits `−1`. If `2^v|K` and `2v+1≥ord_c(2)`, the same argument shows: every successful shift has a witness of support ≤2, and failure is exactly that all prime divisors of `K` lie in `H`. This also covers `c=7` when `2|K`. It does not cover general shifts: for example `<2> mod 31` has index 6, so being outside it need not mean being in `−H`.

**CERTIFIED (finite).** The criterion reproduced all 797 misses and 1,251 hits at shift 15 in the previous cluster. A fresh consecutive sample of 2,048 three-prime-filter targets above `6·10^18` (same `L`, both `p,h` prime) had exactly 823 structural misses at 15, including 540 with composite `Q`. All 823 therefore miss `3,7,11,15` even **without** the support cap, but admit small-support hits later: median first shift 23, max 119. The independent original-fraction check ran on all 2,048; divisor-by-divisor first-shift rechecks ran for all six above 63. Full factor lists, hits and denominators in `c15.csv`. No larger record and no unrestricted counterexample.

## The starting orbit is not a route for every hard prime

**CERTIFIED finite obstruction.** `p=14281≡1 mod 840`, `h=7141=37·193`. Under *all* positive-integer pair replacements preserving the sum of their two unit fractions, the unordered starting state `(p,p,p,p)` has a component of **92 vertices, 641 nonloop edges, and no mergeable pair**. Its exact breadth-first layer sizes are `1,1,1,17,52,20`. All nine vertices with any even denominator are in layer 5. Yet `4/14281=1/3572+1/8054484+1/76517598`. Thus this rules out universal reachability of a merge from the four-equal starting point, not ES, nor reachability from other starts.

Completeness: for reduced pair sum `u/v`, every positive replacement has `(ux−v)(uy−v)=v²`, both factors positive and `≡−v mod u`. Every positive divisor `d|v²` with this residue works since `v` is a unit mod `u`; both orders are permitted, then identify permutations. Mergeability is exactly `u=1`. BFS uses depth ≤16, ≤6000 states (one rerun at ≤20000), and pair-sum denominator ≤90 bits. No cap was reached in the closed-component certificate. Capped runs never imply failure.

Independent closure audit (`closed14281.csv`): group listed quadruples by two *unchanged* denominators. For each of the 355 slices, independently count oriented divisors of `v²` in the required residue by modular convolution on the prime factors, correcting for a diagonal solution. The counts equal the number of listed complementary pairs for every slice. Check every original four-term equality with exact rationals, rule out `u=1` on every pair, and check connectivity and every depth in the induced slice graph. This certifies closure without relying on the neighbor generator, a denominator cutoff, or an ES assumption.

**CERTIFIED census.** All 53 primes in the six Mordell classes up to 20,000: 52 have reachable merges; only 14281 is closed without one. First-even vs first-merge depth gap among the hits: 18 simultaneous, 30 one move later, one two later, two three later, one four later (`p=16921`: 5→9). A pair of odd denominators cannot merge (even sum, odd product), but reaching even denominators need not lead to a merge at all. Rows in `four_orbit.csv`; `states` at a hit is the number visited through its first qualifying BFS layer, **not** the size of the full component. Sample falsifier controls (depth cap 8, state cap 1000): F1 odd squares 9,25,49 reach merges at depth 1,2,2; F2 10156800001 bit-capped (undecided); F3 57,105 both merge at depth 1; F4 409 merges at depth 5, 9601 reaches state cap, then merges at depth 7 in the main census. Merging requires no prime-specific premise.

```
(ulimit -v 1500000; timeout 120 uv run --no-sync python scripts/z73_c15.py)
(ulimit -v 1500000; timeout 120 uv run --no-sync python scripts/z73_four_orbit.py)
(ulimit -v 1500000; timeout 120 uv run --no-sync python scripts/z73_orbit_audit.py)
```

Add `--generate` to the last command to regenerate the closure list before its independent audit. No models launched; side branch only.
