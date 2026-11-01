# HCSHIFTS — independent hostile cross-review

**Reviewed:** `side-agent/z53-hcshifts` at `0019a94483c8d1eb13bd30e83b549e3e18d23067`.
**Verdict: ACCEPT-WITH-FIXES.** The elementary results survive; several advertised consequences do not follow as written.
“Narrowed” is justified only for the specified certification procedures and windows. ES and the polylog HC target remain OPEN.
No theorem about the actual extremal HC scale follows from the stochastic model.

## Per-claim audit

| Claim | Classification | Independent finding |
|---|---|---|
| §1 coordinate-line encoding | CORRECT | Endpoint: d=tx−1 divides p+x and v=(p+x)/d. Level: d and (xp+1)/d are both −1 mod x and recover u,v. The imported coordinate predicate gives HC. |
| §1 congruence/rough split; shift privacy | CORRECT | Smooth valuations and N modulo xs determine nonsplitting residues. The three gcd bounds follow by subtraction; primes >X² cannot occur twice. “Private” must retain this threshold. |
| Theorem W, stated fixed-X theorem | CORRECT | The five proof steps work, including polynomial factors, fixed signed constants, and the least-member exception; see derivation below. |
| W ⇒ no actual HC>(4+ε)log p members infinitely often | GAP | W bounds the window X that the displayed factorisation certifies, not HC(p) from above. A fixed window proves only HC>X; it says nothing about additional misses beyond X. |
| W2, conditional existence | CORRECT | Admissibility, k≤3X/4+3, log Q≤(1+o(1))X, singular-series lower bound and UBH application all suffice. UBH is explicitly nonstandard. |
| W2 BH first-hit calculation | CORRECT-WITH-FIX | The leading 4/3 heuristic survives, but its assertion log Q∼X is false: log Q∼5X/6. This changes only the lower-order O(X) term. |
| W3(i),(ii), Linnik and GRH constants | CORRECT | Valuations force smooth part x+1; nonsplitting would require x−1 dividing x+1. External Linnik/GRH citations checked below. |
| W3 ⇒ every proof of T must use rough-splitting certificates | GAP | W3 excludes nonsplitting only for x≤X=O(log p), whereas T allows x≤(log p)^A. For A>1 its certificate may lie outside the excluded window. |
| H4 ⇒ both divisor and cofactor large | CORRECT relative to imported H4 | For x≤(log p)^A<H, small numerator contradicts A_min>H. A small endpoint cofactor gives an edge with both endpoints ≤H; a small level cofactor is another numerator. Upstream H4 energy lemma is not re-proved here. |
| Remark 3.1, PROVED portion | CORRECT | Reverse the divisor sum; each residue class contributes at least floor(X/d). Levels use p invertible mod d. Removing one maximal valuation per prime gives the stated smooth-product bound. |
| Lemma C(a)–(c′) | CORRECT | Subgroup products exclude −1; the product N lies in that subgroup. Mod 4 handles even x; for q≡7 mod 8 the nonsquares are exactly elements of even order. |
| Lemma C(d),(e) | CORRECT | The negative discriminant −x defines an odd character modulo x; every prime factor of the square lines has value +1. At q=7 the three divisors m,2m,4m cover the nonsquare coset. |
| §3.2 subcritical g and critical boundary | CORRECT within 𝔐 | Poisson truncation/tilting gives g; the critical accumulated cost is at least a constant times e^λ√λ. A=2log 2 is allowed, not excluded. |
| §3.2 almost-sure lower scale | CORRECT within 𝔐× | Success probabilities p^(−o(1)) and independent primes give P^(1−o(1)) successes almost surely (concentration on dyadic intervals). Cross-prime independence is essential here. |
| §3.2 “predominantly τ≳φ(x)” | WRONG as model interpretation | At a terminal critical-scale line, the saturated part contributes only O(λ^(−1/2)) of hits. Tilted ω is 2λ−O(√λ), so many hits have τ/x exponentially small in √λ. |
| L1, L3 and rough-splitting sample trend | EVIDENCE agrees | Recomputed endpoints of the sample range and all committed L1 aggregate reductions; details below. Neither proves a uniform-in-p tail law. |
| L2 headline “held-out … ±20% for X≤16” | WRONG numerical summary | The held-out ratio at 10¹³, X=15 is 1.53, not within 20%. Separate endpoint/level results are a different, in-sample experiment. |
| CERTIFIED W3 and hard-prime data | CORRECT on rerun | Ten W3 primes and all 166 hard-prime rows reproduced; independent PARI enumeration also agrees on HC and counts at HC. |
| Overall “narrowed”; proposed FRONTIER text | CORRECT-WITH-FIX | Keep the scoped barriers and labelled model, remove universal proof requirements and strengthen the quantifier caveats before promotion. |

## Proof checks and repairs

**W.** For each odd ℓ≤floor(X/4)+1 choose one sufficiently large q so every factor's prime quotient exceeds ℓ.
Since p>ℓ, some x=4k≤X has x≡−p mod ℓ. Divisibility of p+x forces ℓ into c or a fixed C_i.
The same factor then divides every family's p′+x, so p′ has the same residue modulo ℓ.
CRT fixes p modulo Π_X; a nonleast positive member exceeds Π_X. PNT gives log Π_X∼X/4.
This establishes the window-size statement, not a bound on the actual HC of those members.

**W2.** The forms have constant term 1 and distinct slopes in disjoint ranges below/equal/above Q.
For ℓ≤2k, each singular factor is ≥1/ℓ, costing O(k) in its logarithm.
For ℓ>2k, factors are ≥1−k²/ℓ², with total logarithmic loss O(k).
Taking log S=C₂X log X leaves log(expected count)≥(C₂−3/4+o(1))X log X−O(X)>0.
Since p≥Q+1→∞ and log p≤(C₂+o(1))X log X, the asserted conditional lower bound follows.
For the incorrect equality about Q: primes ≡1,5,7 mod 8 occur up to X+O(1), but primes ≡3 mod 8 only up to (X+1)/3.
Prime powers contribute o(X). PNT in these fixed progressions gives log Q=(3/4+1/12+o(1))X=5X/6+o(X).
Direct lcm computations give log Q/X=0.829367, 0.835530, 0.833940 for X=10³,10⁴,10⁵.

**W3.** For every small ℓ, N≡x+1 mod ℓ^a with 0<x+1<ℓ^a fixes v_ℓ(N).
Thus N=(x+1)r, gcd(x+1,r)=1 and r≡1 mod x. If d takes none/all of r, d≡d₁ mod x with d₁|x+1.
The only possible d₁≡−1 is x−1; divisibility forces x≤3, excluded.
Here log Q_X=θ(X+1)+ψ(X+1)∼2X. Linnik bounds the least prime's log by (2L+o(1))X.
Also p≥Q_X+1, so X≤(1/2+o(1))log p: these windows cannot cover an arbitrary polylogarithmic T-window.
Verified source: [Lamzouri–Li–Soundararajan, arXiv:1309.3595](https://arxiv.org/pdf/1309.3595), §1.2, p.3,
explicitly cites Xylouris's L=5.2 and states Corollary 1.2: under GRH, P(a,q)≤(φ(q)log q)² for q>3, (a,q)=1.
These give 1/10.4 and 1/4 with the stated o(1); the optional L=5 thesis claim was not needed or independently checked.

**Model.** Put K=log₂x. Truncate E[min(1,2^ω/x)] at K and use 2^w Pr(Pois(λ)=w)=e^λ Pr(Pois(2λ)=w).
For K=κλ, 1<κ<2, both truncations have logarithmic exponent −Q(κ); multiplying by the block size gives g(κ).
Small lines cost at most O(λ) apiece (use the ω=0 atom), so they do not change that exponent.
At X=M2^(2λ), sum the linear regime over the positive-density allowed coordinates:
−log Pr(all miss)≥c E[2^ω(log X−ω log 2)_+]≍e^λ√λ. Borel–Cantelli gives the claimed upper scale.
At x=2^(2λ), however, saturated hits cost O(e^λ/(x√λ)), versus total hits ≍e^λ/x.
Direct Poisson sums give fractions with 2^ω≥x of 0.1706, 0.09245, 0.06674 for λ=20,80,160.
Replace “τ≳φ” by the weaker logarithmic-scale observation ω=(2−o(1))λ, and do not turn it into an arithmetic necessity.

## Numerical reproduction

All shell runs used `ulimit -v 6000000`, finite CPU limits, and explicit `timeout`; working files are in `/tmp/xrev_HCSHIFTS/`.
Archived the reviewed revision; compiled its C engine with `gcc -O2 -Wall` (one harmless misleading-indentation warning).
Ran `hc list 256 4096`: all 166 rows match byte-for-byte; separate PARI divisors give the same HC and certificate counts.
Ran `_linnik.py` under uv/cypari2: output matches byte-for-byte, including all 440 smooth-part line checks and HC=4 throughout.
Certificate counts are exactly 42,28,14; 60,28,100; 92,98; 104,64.
Regenerated `hc range A 600000 256 4096` for A=10⁹ and 10¹³: 1.2 million primes total, no engine failures.
At 10⁹: HC>4/8/16 counts 44066/989/56, max HC=31; HC∈[12,16] all-rough fraction rounds to 5.5%.
At 10¹³: counts 31382/358/5, max HC=23; corresponding all-rough fraction rounds to 16.7%.
Reran `_strat.py --holdout` on both: every reported ratio matches, including 0.82 at (10⁹,16) and 1.53 at (10¹³,15).
Reran `_confine.py` at 10⁹: unconfinable miss rates q=7,23,47,127 are 0,.160,.372,.695, agreeing with the memo.
Reran `_summary.py lines` on all three committed aggregate files: exact numerical agreement (only path headers differ).
This validates the reduction, not a fresh factorisation of those three 200000-prime L1 samples.
Reran `_wall.py`: forced-prime ratios .2379–.2845 at X=64…4096; contiguous maximum 1033 at X=4096.
Reran `_model.py`: λ=160 values .804,.924,.990,1.010 agree. This script integrates a φ(x)≈x surrogate, not the exact model.
Not rerun: middle three 600000-prime samples, square/near-square controls, or hard-vs-random anatomy table; they are not needed for this verdict.

## Required fixes, in priority order

1. **Major — W quantifiers:** replace “cannot exhibit infinitely many HC exceedances” by “cannot certify such a growing threshold by this fixed-window factorisation, except possibly the least member”; retain the actual-HC distinction in §§0,3.2,6.
2. **Major — W3 inference:** say a proof using coordinates within its logarithmic window must split rough parts; remove the assertion that every proof of the unrestricted polylog target must do so.
3. **Major — model interpretation:** remove the claimed predominance of τ≳φ(x) and all theorem-like statements that a proof of T must find ≳2log log p factors. Keep 𝔐× explicit for lower-scale/“iff” claims.
4. **Moderate — L2:** replace the ±20% headline by the actual held-out range 0.82–1.53, identify the sparse 16-event outlier, and distinguish held-out coordinates from in-sample separate lines.
5. **Minor — constants/scope:** correct log Q∼5X/6 (or use log Q=O(X)); restore o(1) and 1<κ<2 in the proposed FRONTIER formula, and keep “among structures examined” in the bottom-line congruence claim.

After these repairs, **ACCEPT the scoped “narrowed” memo**, not a universal Hypothesis-H obstruction or an arithmetic prediction promoted to theorem.
