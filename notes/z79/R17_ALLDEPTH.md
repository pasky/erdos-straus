Result: The r-generic line has positive sterile measure for every prime r ≥ 241, and also for 233.            Label: PROVED (rel. SE reduction, z78 integer ledger lemmas and BBR, computer-assisted; inherited theorem above 283)
Scope: A sufficient threshold for avoiding the seven ET families, not a sharp threshold, an all-depth theorem for 17 or a resolution of ES in ℕ.
Review: none (cross-review owed)
Triage: RECORD
STATUS delta: Replace “sterile Mordell threshold 293” by “sterile points for all primes r ≥ 241 and also r=233; 45 primes below 241 remain in the old gap”. Retain z78's dependencies outside the new interval.

## Positive measure: exact comparison

**PROVED (rel. `../z78/R17_PUSH.md` §§5,8–10).** Give a residue modulo W mass 1/W. Start with the exact complement of L1, P3, Q3, P5 inside the nonsquares. For K odd, P has N=r^K, W=r^((K+1)/2), 4abd=N+e, a+b=ce; Q has F=r^k, 4abd=Fe+1, a+b=ce and modulus F. Both orientations are used. P's first centre is 1−4acd, Q's is −4a²d; swapping a,b takes inverses. We only count unit parameters. Positive remaining mass suffices by SE §3.1. For r≥293 invoke z78, including its original high-range libm qualification for r≥919. No libm-based bound is used **on the newly certified primes**.

**CERTIFIED (integer ledger).** `data/z79/ledger.txt` gives r, exact initial mass, P7, P9, later finite P, finite Q starting at Q5, P and Q infinite tails (positive charges rounded UP in ppm), signed margin rounded DOWN in ppm, and selected early routes. Below 59 the P9 column includes Q5 by exact union and the finite-Q column starts at Q7. A loss may saturate at the available mass: later zero charges then do not indicate zero box counts. The minimum margin in the new terminal run is at **263**, not at the least prime 241:

| r | initial | P7 | P9 | later P | finite Q | tails P,Q | margin (ppm floor) |
|---:|---:|---:|---:|---:|---:|---:|---:|
|233|4846700/12649337|2|131760|195782|35221|9,2774|17614|
|239|3108688/13651919|2|130844|96867|19427|9,2524|−21959|
|241|6110104/13997521|1|128285|193351|31412|9,2530|80927|
|263|5725990/18191447|1|112705|164706|31247|8,1893|4205|
|283|7630628/22665187|1|105220|150248|26326|8,1491|53375|

**PROVED (finite P layer).** Unlike a multiplicity bound one can impose squarefree d on *every* datum in the ledger: absorb a square factor h² of d by multiplying a,b,c by h, leaving e, acd and both centres unchanged (h is a unit). Use this normalization on the large-shift determinant side only, without additionally demanding primitive a,c. In each z78 fixed-pair rectangle with d fixed as part of the pair, count admissible d by the exact 4,9,25 wheel before paying per pair. When d varies, keep its full interval. The grid spacing is x→x+max(1,⌊x/7⌋). For the evaluation determinant on ℓ indices in diameter D, the Vandermonde bound improves from D^s to D^s/2^g, s=ℓ(ℓ−1)/2, g=binom(⌊ℓ/2⌋,2)+binom(⌈ℓ/2⌉,2): split at the interval midpoint, count same-half pairs, and use convexity. Apply this in both forward and applicable unit reverse routes. Thus a chunk of diameter 2^k is admissible if 16ks < mℓ lb − binom(m+1,2) v +16g, with lb,v outward sixteenth-bit logs as in z78. Take the minimum with the unmodified z78 bounds. Code `z79_player.c`.

**PROVED (additional row bound).** In a fixed pair let divisor and complementary divisor be ui−1 and uj+v₀. From their product V, j is affine in i modulo u (expand modulo u²). For index diameters I,J>0 take an integer dual vector (h,k) with h+k·slope≡0 mod u and |h|I+|k|J≤√(2uIJ), not both zero. Minkowski's planar diamond bound gives this since the dual congruence has index u (use a limit for equality). The rectangle meets ≤1+⌊√(2IJ/u)⌋ lines hi+kj=const in that class modulo u. Each line cuts the nondegenerate hyperbola at most twice. Here I≤w and J≤Vw/f_min²; use powers of two rounded up. A singleton is covered by the direct interval route. This argument doesn't require v₀ to be a unit. No assumption that random child digits hit a box.

**PROVED (long shifts in a union of live cylinders).** Split e≥E by b/a≤H or >H with a≤b, integer H≥1. In the first part w=c²d=(N+e)(a+b)²/(4ab e²)≤(N+E)(H+1)²/(4HE²). Each actual f=4acd−1 and f*=4bcd−1 divides 4Nw+1; their negatives are the oriented centres. Thus per integer w both orientations *together* cost at most τ(4Nw+1), independent of the representations w=c²d. Use z77's pointwise τ majorant uniformly up to 4N w_max+1. For H=1 one may simply include equality in the other part. In that other part t=acd≤T=⌊(1+N/E)(1+1/H)/4⌋. The linear list 1−4t meets each depth-(D−1) parent at ≤ceil(T/r^(D−1)) children at depth D. Double over the **whole inversion-stable live set**, not over a single parent. This gives a lower-bound update max(0,(1−min(1,2ceil(T/r^(D−1))/r))A−(short+balanced)/r^D) monotone in the lower mass A. Full P/Q union at depth five when available; otherwise Q≥5 is deferred. All other maps, tail starting exponents, scale rows and exact geometric factors are as in z78 §10. No conditional discount on the high tails.

**CERTIFIED (finite inputs).** For 223..283 stream both P7 orientations from z78's segmented small-e factorization at E=3r³ and complementary Legendre-convergent search in t. Reject squares and dead first digits on the CF side; for the measure bound simply charge twice the number of printed rows, *without* claiming this is the marginal union. At P9 the improvement at large r is a cap, not an exact enumeration. For 14 primes use z78's Q5 two-shift sieve at cuts (ceil(F^(1/3)))² times 1 or 2, with the both-large complement `qlarge` and the factor two for small f. Q7 outside the exact finite tree still uses its integer envelope. The finite layer counts and high tail envelopes are not measured frequencies.

## The cylinder of 5: test, including overlaps

**CERTIFIED.** `data/z79/low/rows.txt` has r, P7 marginal, then P9 and Q5 *separately* above the live depth-four parents, their intersection, and total live depth-five cells. Exact through 53. At 17, 108+58−0 new cells, 113122/1419857 live mass. At 29 there is a genuine two-cell overlap; adding just the two cardinalities is not exact. P uses factorization below floor(sqrt(N))/3, continued fractions above; both full marginal P lists at 17 are checked against independent M17B data. Q uses the joint parametrisation with final membership tests. The first digit 5 loses 54 P and 29 Q depth-five children, but above **5 mod 17²** only 5 and 2; above **5 mod 17³** neither hits at that depth. These are exact conditional counts, not an extrapolation of proportionality. A particular surviving cylinder at depth j pays r^j times global mass for an unrestricted global tail estimate. A homogeneous linear condition on a,b has lattice index r^j but does *not* imply a 1/r^j saving on sparse divisors. Indeed z78 §2 gives deep P keys in every such cylinder. We have not bounded the conditional total below one at 17.

## Effective restrictions for the positive endpoint, not a cutoff

**PROVED (rel. z78 endpoint identities).** There is a fourth indices search for a P contact requiring only indices of size O(U^(2/5)), improving the previous O(U^(1/2)) index cutoff (not a bit-complexity claim). Here U=17^L≥10⁶, (p,q)=(1,5) or (5,1), a≤b, B=U/17, m=4d, H,J,S,Z as in `../z78/R17_ENDPOINT.md` §§1–2. Try e, J, Hd, HZ. Indeed H≪U/(ad), J≪a²d/U, and eZ≪a since e≪a in (2.1) and eZ=17HJ−(q−p)pa. Hence

    e · (HZ) · J · (Hd)² ≪ (U/d)·(a²d/U)·(U/a)² = U².

The constants are effective: H≤12U/(17·4ad), J≤(5/2)p·4a²d/U, eZ≤p(12+|q−p|)a+12qe/(4ad) with e≤2p(12+|q−p|)a. Enumerate each index up to the fifth root with those constants. For e factor (N+e)/4. For J use the paired shifted divisors in z78 §6. For Hd enumerate H,d and use the quadratic square window there; for HZ enumerate H,Z and factor BZ−qH=paS>0 for a, reconstruct b=(UH−pa)/q and test the width-<1 interval for d. Verify the unscaled equations at the end. No depth-12 no-hit census is inferred from this index bound.

**PROVED (Q congruences plus an integral descent in a subcase).** Use the orientation a+5b=FH (here a,b need not be ordered); write h=cH and m=4d. From (a+b)(a+5b)=h(mab−1) obtain

    a² + 5b² + h = Vab,        V=4dh−6.

Whenever 5|V, a↦Vb−a and b↦Va/5−b are integral reflections, both preserving this equation and positivity (by the products of roots). Reduce a+b until neither move lowers it. Then 2a≤Vb, 10b≤Va; one of a²,5b² is ≤√5 ab, the other ≤Vab/2. Hence h≥(2dh−3−√5)ab. As dh≡4 mod 5, any dh≥9 gives h>dh, impossible. At dh=4 the same bound gives h≥3, so h=4,d=1. But the Q centre −4a²d is square at 17 for d=1. Thus **no Q hit of 5 at any odd k has 5|4dcH−6**. Unlike a reduction of the F² contact alone, this uses positivity and integrality at 5 as well as the residue at 17. Without 5|V the b-reflection need not be integral. Even then, if the variables are ordered again with coefficients p,q and C=p+q, integer Va−qb=(pa²+h)/b≥1. Since h=(pa+qb)(a+b)/(mab−1)≤4Cb/(ma), if ma≥8C one gets b≤2p a². The condition holds eventually by pma²+q≥F. These are effective exclusions of parameter ranges, **not** of every hit past the Q15 cutoff. The F² congruence in z78 still has a variable square class; no reduction to fixed S-units or a bounded list of Pell equations has been shown.

## Falsifier Table

| Screen | Check and scope |
|---|---|
| r=13 | CERTIFIED (z78 level-one lists): P1∪Q1 contains 2,5,6,7,8,11, all six nonsquares. Thus **no sterile nonsquare on the single-13 generic line**, not merely failure of x=2 there. The refuted two-prime x* has x₁₁=x₁₃=2 and a different II3 witness; see z78 endpoint §5. |
| F1 odd squares | Assessment: we count complement restricted to nonsquare r-adic units. Neither a classical point at an odd square nor positivity of an integer solution count follows. |
| F2 C-even / numerator 8 | Assessment: 4 in the tuple identities is fixed. No implication about 8/131, 8/241 or its C-even sub-line. |
| F3 composites | Assessment: every sweep index is a prime, and N,F are its powers in the ET reduction. No composite R(n)>0 assertion. |
| F4 known zeros | Assessment: surviving r-adic parameters are not lower bounds for (★), Type A, or their integer witnesses. All four zero tables in `data/z58/screens` are compatible. |

**CERTIFIED (replay).** From root run `bash scripts/z79_replay.sh` (or stages `p7`, `low`, `q5`, `layer`, `ledger`). No external arithmetic package. The standalone driver regenerates new finite tables, diffs output and checks the terminal strict inequalities; reviewed z78 arithmetic lemmas and its old input files remain dependencies. **Assessment — next step:** at 239 target the 130844 ppm P9 envelope by splitting the t list by the largest prime factor of t: if p|t is large one fixed pair costs at most t/p, while the remaining integer keys are smooth. A useful bound needs to pay for both alternatives, and for the small shifts, at the same cutoff. At 17 a separate bottleneck is finite Q after Q5, not the asymptotic high tail alone.
