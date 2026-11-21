Result: Every prime r≥83 and r=73 has positive sterile measure; at r=17 both endpoints avoid P through depth 16 and Q through odd level 39.            Label: PROVED (measure, rel. SE §3.1, z78/z79 and BBR); CERTIFIED (endpoints, four-index P and rational-walk Q engines, independently checked below)
Scope: Finite endpoint record and an effective all-level restriction on d for Q, not all-depth sterility. The positive-measure threshold is now 83, with 73 also cleared (PROVED relative to the z78/z79 integer ledger, BBR and SE §3.1). ES in ℕ is open; sterility is a barrier to finite linear coverings.
Review: cross-model (`data/z80/xreview/REVIEW_R17_WALK_OPUS.md`, all stages replayed, decisive P₁₁ windows independently counted, independent Q search and separate P search with different cutoffs)
Triage: RECORD
STATUS delta: Every prime r≥83, and r=73, has positive sterile measure; 79 and the primes 17..71 remain open. At 17 the two points survive through depth 16 (Q alone through 39), not every depth. Retain the inherited libm qualification for r≥919 only.

## An effective rational descent outside the integral sector

**PROVED (relative to the Q identities in `../z78/R17_ENDPOINT.md` and `../z79/R17_ALLDEPTH.md`).** With the smaller side called a, (p,q)=(1,5) or (5,1), F=17^k and h=c(pa+qb)/F, every Q hit solves

    pa²+qb²+h=Vab,      V=4dh−6,     ad≤(F+1)/2.

There is no assumption on V mod 5. Put X=√p a and Y=√q b. A root reflection replaces X by S Y−X or Y by S X−Y, S=V/√5. The new coordinate is positive by the product of roots. Work with the **unweighted rational** coordinates underneath; a move introduces at most the fixed divisor 5, and only every other move divides by 5. If the larger weighted coordinate exceeds S/2 times the smaller, reflect that larger one. It strictly decreases and the same coordinate cannot be reduced again immediately. If neither coordinate reduces, stop. We do not require termination of this walk.

After i successive reductions the individual denominators divide 5^ceil(i/2) and their product divides 5^i: the successive *new* coordinate denominators divide 5,5,25,25,… in the worse orientation, and the other coordinate is one step older. If the walk stops by step m, the minimal-pair proof of z79 continues to hold over positive rationals: h≥(V/2−√5)ab at the stopped pair. Its product ab≥5^(−m). Hence 2d≤5^m+6 (also immediate if V/2≤√5).

Otherwise there are at least m+1 successive strict reductions. Write x₀,x₁,… for the alternating weighted coordinates, with x₀ the initial larger coordinate and x₂ its reflection. For i=1,…,m, xᵢ>(S/2)xᵢ₊₁. Now x₁ is the smaller initial weighted coordinate, so x₁≤√5 a≤3(F+1)/(2d), and xₘ₊₁≥5^(−ceil(m/2)). Consequently for d≥2,

    (4d−6)^(2m) · 4d² ≤ 9(F+1)² · 20^m · 5^(2ceil(m/2)).

Thus any d violating both bounds is excluded, **at every depth**. Taking m of order √log F gives an effective d≤exp(O(√log F)): the stopping bound has this size, and taking 2m-th roots in the other bound gives O(F^(1/m)) for d≥3. This conclusion is uniform in h and covers the previously unrestricted sector 5∤V. It does not bound F itself.

**CERTIFIED (`scripts/z80_qwalk.py`).** Minimise the resulting integer cutoff over m=1..19 (and the trivial ad cutoff). For each d and orientation Newton-lift the two roots of 4pa²d≡−q mod F. Only their positive representatives can satisfy 2ad≤F+1. For each such a, let s=4ad and G=4a²d+1=ef. Since f≡−F mod s, e≡−F⁻¹ mod s and G<s², one of the two factors is its least positive representative. Try both cases and test the original identities and units. Thus even the unknown primality of a large cofactor is immaterial. At k=17 the cutoff is 7815 rather than √((F+1)/2); at k=39 it is 507267. Full output `data/z80/crush2/qwalk.txt`, including the nonempty r=13 control. This proves a finite absence of Q hits, not a measure estimate in a cylinder.

## Two factor-free P index sectors

**PROVED (relative to the z79 four-index cover and z78's e ceiling).** Use U=17^L, B=U/17, N=UB, e₀=466 ceil(√U), M=4ad, J=(pMa+qe)/U, MH=qB+J, H=(pa+qb)/U. The z79 product bound for e·HZ·J·(Hd)² is strictly below U²/500 outside the Hd cutoff. `z80_ep_bounds.py` checks the exact rational constants separately at each L. The cuts (e,J,HZ,Hd) are (20000,50000000,20000,1000000000) at L=15 and (12000,450000000,130000,3500000000) at L=16. The e and HZ domains use the same divisor reconstructions and product-checked GNU `factor` records as z79.

* **J window.** Write K=p(qB+J₀)²/4, J₀ the cutoff. Since a≤M/4, UJ≤K/H²+qe₀. Enumerate H≤floor(√(K/(U−qe₀))) and only positive J≡−qB mod 4H in the indicated window, also J≤J₀. M is now known; enumerate e≡−N mod M, e≤e₀, testing e|pB+J, pMa=UJ−qe and all remaining divisibilities and units. No factoring of the J progression.
* **Hd window.** For v=Hd≤Y, use the z79 exact GMP two-square-root window on H v²≤pB/12. On the complement group all H above h=1+floor(pB/(12v²)) at the same v. With a₀=qB/(4v), one has a=a₀(1+e/N)(1+pa/(qb)), a≤6B(1+e/N)/(4v), b≥UH/6. Therefore 0<a−a₀≤qe₀/(4Uv)+36pB(1+e₀/N)²/(16·17·H v²)<1+pB/(6h v²). This holds for the ordered side in either orientation. Enumerate the short interval in a; then J=4va−qB, and (UJ−qe₀)/(4pa²)≤d≤(UJ−q)/(4pa²). Require d|v, recompute b using H=v/d and re-test. Even in the flat large-v regime the ceiling costs only once **per v**, not per divisor H. No floating-point root or small-root-only assumption.

**CERTIFIED (`scripts/z80_epfast.c`, `scripts/z80_ep15.c`; `data/z80/crush2/p{15,16}.txt`).** All four domains empty in both orientations. For the factor-free modes the end record has `keys,vis,hits` (J: J candidates and shift candidates; Hd: GMP pairs and grouped a candidates). Products at level 16 that exceed uint128, in particular 5N/d for tiny d, use GMP; the other division bounds are outward. The P result uses the inherited through-14 certificate, Q uses the new walk. The joint statement follows by inversion. No P17 census.

## Why the proposed tail transfer does not follow

**PROVED (obstruction to a same-cylinder, exact-level recursion, relative to `../z78/R17_PUSH.md` §2).** A live depth-j cylinder has *zero* charge from P at depth j, yet contains integer P-centres at arbitrarily large depths. Therefore no finite multiplier of its exact depth-j P charge bounds the whole future P series **in that cylinder**. In particular this falsifies a geometric recurrence starting at that actual zero and holding at every subsequent step. At 17 apply it to the cylinder of 5 at depth 14. At a prime with positive sterile measure choose a sterile point and take j arbitrarily large. This does **not** disprove an inequality between unconditioned consecutive global charges or one between positive analytical envelopes. The latter already exists beyond the z78 scale anchor: its ratios are bounded by the integer-rounded r^(−2G/320) for P and r^(−1/2) for Q. Its initial value is an envelope, not the last exact count. Nor does subtracting all pair intersections give an upper bound on a union: the two-term Bonferroni sum has the opposite sign.

**PROVED (middle-shift refinement, `scripts/z80_mid.py`).** In t≤e<2^j with t≥m^(1/3), m≥M=(N+e)/4, order a≤b. When a<t, fixing b|M gives at most one a (its class mod e), and b≥t/2. When a≥t, fixing b|M gives at most one d≤M/t²≤t in its specified unit class mod e; here t≤b≤M/t. Thus from the oriented 4τ(M) cap subtract twice the count of divisors up to floor((t−1)/2) and four times those up to t−1. In the second case the two excluded tails of the divisor list are disjoint since t²≤M. The annulus has H=(2^j−t)/4 consecutive M. Summed divisors ≤b≤H occur at least H·∑_{n≤b}1/n−b times; use a block lower sum. Use only t²≤floor(n/8) for an upper anchor n with n/2≤N≤n. This refines an envelope, not the actual hit ratio.

**PROVED (relative to the Round-1 PL prefix split and z79 large-shift and tail bounds).** `scripts/z80_fullprefix.c` exhaustively factors the consecutive M at P₁₁ for e<2³² in four disjoint 2²⁸-position windows per prime. A 2 GiB window stores one prime >cube root and ≤√max M per multiple. The remaining block arrays need <64 MiB. Unlike the P₉ engine, the dividend and residual are 128-bit throughout. A terminal prime exceeding uint64 cannot be funded in g: feed its residue into the complement walk. Compare the whole short-shift count plus the applicable z79 run charge for e≥2³² with alternative cutoffs. Use the same z79 shift engine through 2³³ (all seven) and 2³⁵ (79,71,67,61,59) at K=13,15. This certifies 83 and 73, with no new pass in a single local cylinder. Neither P₁₁ nor Q₉ is claimed enumerated exactly.

## Local ledger and remaining deficits

**CERTIFIED (relative to inherited global envelopes and depth tables; `scripts/z80_budget2.py`).** The table tests every live cylinder modulo r or r², computing its exact depth-three complement. The cylinder and its inverse have the same charge; subtract at most the whole later unconditional budget *once per pair*, not once per member. No proportional discount for sparse divisors. For 17 use the exact two-cell tree through depth 8 when better. The author-owned P₉ prefix and complementary CF rows at 59..83 (`prefix9.txt`, `cf9.txt`) are computed by `z80_pshift.c` and `z78_r2cf.c`, the latter independently matched by `z80_xr_cf.c`. All displayed margins are signed floors in ppm before truncation to zero. The global margin takes the better of the monotone live ledger and the unconditional union budget. The dominant family is the largest single uncapped-by-live budget entry, rounded up; it need not fit into the remaining live mass. The local column is the best **signed lower bound from this test**, not the true best cylinder. All fail, so all trivial nonnegative bounds tie at zero. `data/z80/crush2/local.txt` retains exact fractions for the signed global and conditional margins and the depth-14 comparison.

|r|global ppm|dominant (ppm)|best cell|conditional ppm|
|--:|--:|:--|--:|--:|
|17|-975562|P19 (949273)|5 mod 17|-26255711|
|19|-764848|P15 (1000000)|3 mod 19|-47963634|
|23|-491155|P15 (722263)|5 mod 23|-39479923|
|29|-372262|P11 (436498)|2 mod 29|-32789949|
|31|-241654|P11 (396305)|6 mod 31|-30108138|
|37|-175613|P11 (319062)|13 mod 37|-24325061|
|41|-147290|P11 (286052)|17 mod 41|-22680979|
|43|-105935|P11 (264777)|8 mod 43|-21122625|
|47|-89051|P11 (236394)|26 mod 47|-19498594|
|53|-91858|P11 (200926)|8 mod 53|-17508710|
|59|-76737|P13 (106444)|6 mod 59|-12154305|
|61|-63824|P13 (99055)|2 mod 61|-11562816|
|67|-53850|P13 (86458)|13 mod 67|-11566767|
|71|-62806|P13 (78341)|11 mod 71|-10311806|
|73|18189|P13 (81240)|11 mod 73|-9885173|
|79|-25127|P13 (67671)|12 mod 79|-8761119|
|83|19111|P13 (71190)|2 mod 83|-8771390|

**Assessment (depth-14 cell).** At 5 mod 17¹⁴ the whole cell is live through depth 14. A strict tail cost below 1 in cell units, i.e. below 1/168377826559400929 in ambient measure, suffices for some survivor. Charging half the unrestricted inverse-stable tail per cell costs 7,977,074,896,357,901 cell units rounded up before the trivial cap at 1. The inverse cell has identical costs. Positive measure would not identify which point survives. Next threshold target: at 79 P₁₃ consumes 67,671 ppm and the unsaturated deficit is 25,127 ppm.

**CERTIFIED (review §3.5, ablation).** Both new passes require the P₉ rows, the complete 2³² P₁₁ prefix, and the middle-shift band. At 73 the K=15 shift33 row is also needed. Removing all shift33 rows at 83 still gives 17 ppm; shift35 is not load-bearing. The gain is principally the deeper cut before paying the large-shift envelope. `p11.txt` columns are r, log₂ cutoff, zero-based shift offset, window width, short-shift charge. Opus replayed every inherited shift row but did not rewrite those engines. Its independent endpoint implementation used alternative partitions and 1,157 positive containment checks; the production engines now also have compile-time, synthetic positive tests for all four search modes and both Hd branches (not positive hits at level 15 or 16). The corrected ledger asserts both pass signs and independently rejects 13. The reviewer disclosed two temporary three-process overlaps in its own runs; no resource-compliance claim is made for those intervals.

**Replay.** `bash scripts/z80_crush_replay.sh all` from root; Round 2 alone `bash scripts/z80_round2_replay.sh`. Each computation is separately time- and memory-capped; the full source replay takes several such chunks. The regression includes the independent single-13 coverage and two-prime II3 falsifiers.
