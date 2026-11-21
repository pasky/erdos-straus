Result: The sufficient threshold for positive sterile measure on the r-generic line falls from 149 to 89.            Label: PROVED (rel. SE §3.1, z78/z79 ledger lemmas including BBR, computer-assisted)
Scope: Ten additional primes; the 17 gap primes from 17 through 83 remain unresolved by this test. This is a barrier to finite ET linear coverings, not a result on ES in ℕ, which is open.
Review: none (cross-review owed)
Triage: RECORD
STATUS delta: Replace the sufficient threshold by 89; retain the inherited high-range qualifications and the finite-depth qualification for the two endpoints at 17.

## The short-shift charge

**PROVED (relative to PL's divisor parameterisation).** Put N=r⁹, M=(N+e)/4. Unit shifts have gcd(M,e)=1. Each oriented centre has h=Ma/b dividing M² and h≡−M mod e; inversion interchanges h and M²/h. Split M=gy greedily, g≤e. Every divisor h of M² admits a split h=uv with u|g², v|y², even when g and y share a prime. Either u≤g or the complement g²/u≤g. It therefore suffices to count both orientations for every admissible split with u≤g. For each v, the least positive representative of −M/v mod e is the only possible u in [1,g]; test divisibility into g². Enumerate the residues via M/v=(g/y)(y²/v) modulo e, using one inverse per shift. At e≤32 charge τ(M²) instead. This is an **upper bound**, not an exact marginal union. In particular the two possible orientations may coincide after reduction at native depth.

**CERTIFIED (z80_pshift.c).** The prefix ends at e<2²⁹. The largest array uses one uint32 per shift position (512 MiB at this cut); there is no r⁵ bitmap. Up to the ceiling cube root of the largest M, remove all prime factors with multiplicity block by block. The other prime sieve runs prime-segment first, writing one prime exceeding that root and ≤√maxM at each multiple. The remaining cofactor has at most two prime factors; a composite one necessarily has a recorded divisor, even if a second write overwrote the first. Division then recovers both. For seven primes the complementary e≥2²⁹ charge comes from z78's Legendre-convergent scan through floor((N/E+1)/2) in acd. Both orientations are charged for each matching record. Rejecting a dead first digit is valid because the live level-one set is inverse-stable. Other rows use the reviewed large-shift determinant. The tabulated prefix is also a seed for z79's disjoint annulus propagation.

## The Q₅ charge

**PROVED (relative to z77's Q identities).** For e≥E and f≥T, write w=c²d; 4w(ef−1)=(F+f)² and f≤F+2. Here E=T=ceil(F^(1/3))²≤F/2. The maximum of (F+f)²/f on [T,F+2] is at T: the function is f+2F+F²/f and T(F+2)≤F². The other factor f/(Ef−1) decreases. Thus w≤floor((F+T)²/(4(ET−1))). At fixed c,d discard square or zero −d modulo r, and repeatedly clip the f ceiling using f≤(1+(F+h)²/(4w))/E when f≤h. On short progressions test f|V=F²+4w, ef=4a²d+1 and ordering. Otherwise extract g|V, g≤u=4cd by small primes; for each divisor of V/g the remaining divisor of g has at most one choice in the prescribed unit class modulo u. Each leftover prime factor above 251 costs at most two divisor choices per copy. Minimise with progression length; double for the inverse. Add z78's small-e charge and twice its small-f charge. No subtraction of estimated overlaps or assumption of independence. At r≤53 retain the inherited exact depth-five union, not an extra Q₅ subtraction.

## Ledger

**CERTIFIED (z80_crush.py, relative to z79 tables).** Use the unchanged z79 run recurrence at additional primes, and the existing prime-power prefix sieve at more r,k pairs. All charges on new primes and tail comparisons use integers and rationals. At r≥149 or r=137 the old verdicts are preserved; beyond 283 invoke z78/z79 with their original dependencies. The old and new columns below are signed floors of a lower bound in ppm, not estimates of coverage. A failed ledger can saturate its finite-P live mass at zero; its negative margin is then not the improvement sufficient to pass. `data/z80/crush/ledger.txt` lists the P₇, depth-five, remaining finite P, finite Q, P-tail and Q-tail charges rounded up individually before the final margin column (which is calculated before rounding).

|r|old|new|route used on passes|
|--:|--:|--:|:--|
|17|-975562|-975562|not cleared|
|19|-764848|-764848|not cleared|
|23|-491155|-491155|not cleared|
|29|-372262|-372262|not cleared|
|31|-241654|-241654|not cleared|
|37|-175613|-175613|not cleared|
|41|-147290|-147290|not cleared|
|43|-105935|-105935|not cleared|
|47|-89051|-89051|not cleared|
|53|-91858|-91858|not cleared|
|59|-374875|-76737|not cleared|
|61|-315053|-63824|not cleared|
|67|-292607|-53850|not cleared|
|71|-306216|-62806|not cleared|
|73|-240213|-53762|not cleared|
|79|-242900|-48417|not cleared|
|83|-219299|-37363|not cleared|
|89|-175426|15841|prefix + CF + finite layers|
|97|-146992|81279|prefix + CF + finite layers|
|101|-143330|29845|prefix + CF + finite layers|
|103|-149703|24911|prefix + CF + finite layers|
|107|-139771|47249|prefix + CF + finite layers|
|109|-123969|29839|prefix + CF + finite layers|
|113|-116264|86690|prefix + CF + finite layers|
|127|-102405|55602|prefix + determinant + Q₅|
|131|-20061|62912|prefix + determinant + Q₅|
|139|-11317|60669|prefix + determinant + Q₅|

## Falsifier table and replay

| Screen | Result |
|---|---|
| Single-13 generic line | CERTIFIED (stored z78 native lists): all six nonsquares covered at depth one. |
| Two-prime x* | CERTIFIED (II3 arithmetic check): residue 12650497 modulo 12670944 hits the point with both 11- and 13-components 2. Distinct from the single-13 test. |
| Regression | CERTIFIED (z80_crush_checks.py): reconstruct the four z78 native marginal counts at 17..53 and retain all 28 previous passes. |

**Replay.** From the repository root: `bash scripts/z80_crush_replay.sh`. Every generated stage is diffed against the compact certificate. The ledger-only option checks the inherited z79 verdicts, falsifiers and SHA-256 manifest; it does not regenerate the C stages. Independent-check scope: inherited z78/z79 controls only pending cross-review of the new stages.

**Assessment (17).** The test gives no positive local mass at 17. Survival of the point at a finite depth is not all-depth survival of its cylinder. No improvement of the point depth is asserted by the ledger.
