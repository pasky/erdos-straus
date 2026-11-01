# ZF0 part 2 — actual level, slice and fingerprint computations

Completed: 6 items; 4 interesting, 2 nothing, 0 covered/deferred/skipped.
Interesting: Z3167, Z1597, Z1721, Z2819.
Nothing after substantive tests: Z0916, Z3019.
Coverage: level census to 10⁸; minimal-u and e-slices to 10⁷; Kloosterman to 10⁶; level factor/hypergraph census to 10⁵.
ES remains OPEN; failure of the (★) subfamily is not failure of ES.

All logarithms below are natural. Computations use primes p ≡ 1 (mod 4), unless specified. JSON outcomes: `data/z52b/pass2/ZF0_part2.jsonl`. Exact integer enumerations are labelled CERTIFIED (computer), numerical correlations/fits EVIDENCE, and interpretations Assessment.

## Z3167 — least level, including infinite values

**Premise correction (PROVED algebra; CERTIFIED census).** A least level need not exist: the (★) family is only a subfamily of Type II. Set K(p)=∞ when R(p)=0. Enumerate

`p = 4Cab − a − b`, `1 ≤ a ≤ b`, `a+b ≡ 3 (mod 4)`.

The C-level sieve is exhaustive through C=4096. For every remaining prime, an independent search over **all** `4a²−2a ≤ p` factors `p+a` and checks every divisor `d ≡ −1 (mod 4a)` with `(p+a)/d ≥ a`. It returns `C=(d+1)/(4a)` and `b=(p+a)/d`. Thus the remaining zeros are not censored at 4096. Positivity and odd p give ab≥2, so every certificate has `C ≤ (p+3)/8`.

| p bound | primes | K=∞ | max finite K | first maximizer | max finite K in six Mordell classes |
|---:|---:|---:|---:|---:|---:|
| 10² | 11 | 0 | 5 | 37 | no such primes |
| 10³ | 80 | 2 | 20 | 157 | no such primes |
| 10⁴ | 609 | 4 | 40 | 4789 | 14 |
| 10⁵ | 4783 | 6 | 557 | 98017 | 149 |
| 10⁶ | 39175 | 9 | 23105 | 184837 | 4016 |
| 10⁷ | 332180 | 14 | 23105 | 184837 | 4016 |
| 10⁸ | 2880504 | 14 | 41027 | 85664329 | 41027 |

The hard residues are {1,121,169,289,361,529} modulo 840. The 14 infinities are
409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561, 8813281, agreeing with `FRONTIER.md` §2.1 / `B1_LINE.md` §3.6.

At p=184837 the only least-level witness found is `(a,b,C)=(1,2,23105)`: K actually reaches the absolute boundary `(p+3)/8`. This was missed by the earlier C≤20000 follow-up. At 85664329 the new finite maximum is 41027.

**EVIDENCE, not an asymptotic law.** OLS `log(max finite K through B) = intercept + A log log B` gives A=7.326107, R²=.90509 over seven decade endpoints 10²,…,10⁸. Removing the first endpoint gives A=8.983774 (six points); using 10⁴,…,10⁸ gives A=10.486924 (five). These nested, jump-dominated maxima are not independent observations; neither R² nor the slope is evidence for a uniform polylog theorem. In particular, fitting finite values cannot erase K=∞.

**Repository hard list.** All 14 distinct entries of `data/lsa/hard.txt` were checked, not just the new census tail. In increasing p order their K values are:
`2521:11, 5569:∞, 21169:2, 43969:1, 132721:2, 471241:1, 583801:1, 1092961:5, 2451289:6, 4889641:1, 5101441:6, 8628481:11, 20322481:12, 37117609:2`.
Independent SymPy divisor enumeration checks 43 selected tail/record/hard inputs and all 609 eligible primes through 10⁴. Data: `ZF0/Z3167/{decades,records,tail}.csv`, `analysis.json`.

**Assessment.** Interesting because the original finite-level premise is false and the bounded pass1 scan hid a boundary-sized finite outlier. A lower bound on short levels would have to change the certificate family or explicitly handle the empty fibers.

## Z1597 — a valid uniform small-prime bound, not full Turán–Kubilius

### Explicit bound (PROVED)

Let X≥1 be an integer, z≥1, and let P be the primes q≤z with q∤4p. Put

`S(C)=Σ_{q∈P} 1[q | 4pC+1]`, `A=Σ_{q∈P} 1/q`, `m=|P|`.

There is exactly one admissible C residue modulo q, and exactly one modulo qr for distinct q,r∈P. Consequently, with E denoting the average over 1≤C≤X,

`|E I_q − 1/q| ≤ 1/X`, `|E I_q I_r − 1/(qr)| ≤ 1/X`.

Expanding the square, its main term is `Σ_q (1/q−1/q²) ≤ A`. The diagonal and ordered off-diagonal counting errors total at most `m²/X`; the error in `−2A E S` is at most `2Am/X`. Therefore the fully explicit statement is

**`E (S−A)² ≤ A + (m²+2Am)/X`.**

With z=X^(1/4), m≤z and A≤m give

**`E (S−A)² ≤ A + 3/√X`.**

If A>5, then ω(4pC+1)≤5 implies S(C)≤5 and hence

**`#{C≤X: ω(4pC+1)≤5} ≤ X (A+3/√X)/(A−5)²`.**

The constants 1 and 3 are explicit, and every error estimate is uniform in p. The min of this bound and X can always be used. By the prime reciprocal-sum theorem, `A=log log X+O(1)` uniformly in prime p (only 2 and possibly p are excluded). Thus the poor fraction tends to zero uniformly as X→∞, including along any X=(log p)^a→∞. This is only O(1/log log X), **not** the proposed Brun-strength `(log log X)^5/log X`. At X=4096, z=8 and A≤1/3+1/5+1/7<1, so this explicit poor-tail bound is vacuous; the data are preasymptotic.

### Why the unrestricted full-ω assertion is false (PROVED relative to Linnik's theorem)

Fix X. Assign L distinct primes q>4X to each C=1,…,X, with no reuse, and prescribe
`p ≡ −(4C)⁻¹ (mod q)` for the primes assigned to C, together with `p ≡1 (mod4)`.
CRT gives a reduced class modulo M=4 times the product of these XL primes. Linnik's theorem supplies a prime in it with `p ≤ c M^L₀`, where c,L₀ are absolute. Choosing the first XL primes above 4X yields `log log(Xp)=O_X(log L)`, while every ω(4pC+1)≥L. Hence

`Σ_{C≤X}(ω(4pC+1)−log log(Xp))² ≥ X(L−O_X(log L))²`,

which contradicts any unrestricted uniform `≪ X log log(Xp)` bound as L→∞. This refutes the item's claim that the full function has that variance uniformly in arbitrary p merely because small-prime residue counts are uniform. **It does not refute every possible full-ω estimate restricted to a prescribed X≥(log p)^a regime.** No such restricted theorem, or explicit Brun bound, is asserted here. The elementary truncated estimate above is complete without importing either.

### Rich failures (CERTIFIED computer)

All 4783 eligible primes p≤10⁵ and all 1≤C≤4096: 19,591,168 level pairs. Factor 4Cp+1 exactly using a residue sieve in C, and test the actual divisor class. There are 104,472 rich pairs (ω≥6; 0.53326% of all pairs), of which **103,748 fail (99.30699%)**. Rich failures occur at 4768 primes. Importantly, restricting to the necessary feasible range `8C−3≤p` still gives **90,252 failures / 90,976 rich pairs (99.20419%)**; the conclusion is not just an artifact of levels too large to carry any certificate.

| C range | rich failures | rich hits |
|---|---:|---:|
| 1–64 | 158 | 91 |
| 65–256 | 1818 | 142 |
| 257–1024 | 14074 | 230 |
| 1025–4096 | 87698 | 261 |

All eleven ω=8 pairs fail, even in the feasible range. Richness is helpful relative to very poor factorizations at fixed small levels, but emphatically does not force the residue class −1. Thirty **feasible** rich failures were independently factored and all their divisors tested. Data: `ZF0/Z1597/{hist.csv,perprime.csv}` and `ZF0/Z3019/validation.json`.

**Assessment.** The uniform truncated lemma is a legitimate pointwise-in-p statement. What is missing is a residue/subset-product statement at a rich level, not the assertion that most sufficiently long families eventually contain rich integers.

## Z1721 — minimal u is small, the other coordinates need not be

**CERTIFIED computer.** For every eligible p≤10⁷, scan u in increasing order up to `4u²−2u≤p`. At each u factor p+u and enumerate all divisors d satisfying `d≡−1 (mod4u)`, with `k=(p+u)/d≥u`. The corresponding level is `C=(d+1)/(4u)`. Symmetry means the globally minimal u always has k≥u; thus the search is complete. At the first successful u, retain **all** k choices and select the least k for the per-prime witness. This ordering is not the same as minimizing C.

332,180 primes, 14 empty fibers (the same list as Z3167). Finite maxima:

| bound | max minimal u | p | selected k | C |
|---:|---:|---:|---:|---:|
| 10² | 2 | 73 | 5 | 2 |
| 10³ | 4 | 337 | 11 | 2 |
| 10⁴ | 19 | 6337 | 28 | 3 |
| 10⁵ | 78 | 57457 | 185 | 1 |
| 10⁶ | 131 | 427249 | 204 | 4 |
| 10⁷ | 410 | 4160641 | 1269 | 2 |

Among the 332,166 finite cases, 292,638 have u=1. The median/90th/99th percentiles of u are 1/2/5; of selected k, 2/46/2347. The largest selected k is 904004 at `(p,u,k,C)=(9944041,3,904004,1)`, and there is only one k at that minimal u. The median selected C is 234356; its maximum is 1249997. The number of k choices at minimal u has median 4, 99th percentile 24, maximum 72. `run.txt` also records the log₂-binned distribution of **all** k choices, not just the selected k.

**EVIDENCE:** in this sample all finite minima satisfy `u ≤ 1.765009(log p)²`; the maximum ratio occurs at 4160641. This supports testing a small-*one-coordinate* envelope, not claiming it as a theorem. The unconditional algebraic bound on an existing fiber is only `u ≤ (1+√(1+4p))/4`.

**PROVED size caveat.** If all u,k,C≤H, then `p=4uCk−u−k<4H³`, so `H>(p/4)^(1/3)`. A simultaneous polylog bound for all three coordinates is impossible asymptotically even before accounting for the 14 empty fibers. Siegel's lemma applies to linear homogeneous systems, not this positive bilinear constraint. No simultaneous-height optimization was performed.

Data: `ZF0/Z1721/minu.csv.gz` stores p,u,k,C,number of k choices; `analysis.json` contains the u histogram, quantiles and records. All reported witnesses are substituted into the equation; 116 sample/record/zero rows are independently re-enumerated with SymPy.

## Z3019 — actual e-slice mining, but no hereditary predicate found

The prior citation was not coverage: `EXSET_SHIFT_DIVISORS.md` §§0–1 defines `hit_v(n+v)` and U-shift correlations, not mining `N_e=(p+e)/4` for a minimal-counterexample induction. Its only incidental “induction” reference concerns a product inequality, not descent of ES.

**CERTIFIED computer.** For every one of 332,180 eligible primes p≤10⁷, test all e=3,7,…,255 satisfying e<3p (so N_e<p) and p∤e. Enumerate prime exponent differences of N_e in [−v_q(N_e),v_q(N_e)]; a product −1 modulo e is exactly a coprime ratio a/b with ab|N_e, a+b≡0 (mod e). This is the full Type-II e-slice criterion, not the (★) subfamily. For p≡3 (mod4), the omitted e=1 is already trivial.

There are **5,834,457 successful slices**, no prime without a hit, and the largest first successful e is **107 at p=8803369**. Bit j of `ZF0/Z3019/slices.csv.gz` records the result at e=4j+3, so the file lists every tested successful e losslessly rather than only recording the minimum. No claim is made about e>255.

Six elementary intrinsic predicates were mined on N_e:

| predicate on N | failing slices | successful slices | primes with a successful such slice |
|---|---:|---:|---:|
| any N | 15424727 | 5834457 | 332180 |
| prime | 1534696 | 48867 | 44524 |
| composite | 13890031 | 5785590 | 332179 |
| square | 10601 | 4237 | 4237 |
| R(N)>0 | 15408058 | 5826705 | 332179 |
| ω(N)≥3 | 8563882 | 5232441 | 332163 |

R(N) is computed exhaustively by its integer AP parametrization, not inferred from ES verification. None of these predicates implies a hit in the required e-slice. The same smaller integer **N=5** has a hit at `(p,e)=(17,3)` (ratio 5/1≡−1 mod3), but not at `(13,7)`; R(5)>0 and ES(5) hold in both instances. Thus the bare inherited assertion “the smaller integer has a certificate” does not transfer its certificate to the new modulus. This does **not** rule out a richer e-aware inductive invariant, or an existential choice of a different e.

3,416 individual slice tests are independently checked by enumerating a|N and b|N/a; no discrepancy. Outcome **nothing**: the actual mining is now done, but no hereditary implication emerges from the tested predicates.

## Z0916 — null test with actual U, all eligible primes to 10⁶

**EVIDENCE.** Unlike pass1's truncated R_K proxy, this uses the actual unordered ES count U(p). Existing exact tables cover the entire range: `data/z52b/raw/f4_all_30000.txt`, `pr_20001_200000.txt`, and `data/z52c/rh/U_counter_2e5_1e6.txt.gz`; the latter is independently audited in `RESIDUE_HARDNESS.md` §1.1.

For all 39,175 eligible primes through 10⁶, compute the inverses by `inv[x]=p−floor(p/x)inv[p mod x] mod p`, pair x with p−x, and sum `2cos(2π(x+inv[x])/p)` with compensated double summation. Thirty small primes are independently checked against direct complex sums with modular inverses. The largest observed |K/√p| is 1.99888002124, consistent with Weil's bound.

- Spearman(K,U)=+.003261389 (p=.5186).
- Spearman(K/√p,U)=+.005622556 (p=.2658).
- Within p mod840 × 100000-wide size-bin strata, demean global ranks: correlation +.007591311; 1000 within-stratum permutations give p=.145854, null SD .00528312.
- Five consecutive width-200000 bins have correlations .006564, −.004137, .009808, −.001727, −.003621.

No detectable signal for this frequency at this range; outcome **nothing**, not a theorem of independence. Numerical C computation consumed approximately 225 CPU seconds on one core. Data: `ZF0/Z0916/{input.csv,kloo.csv,analysis.json}`.

## Z2819 — full shared-prime hypergraphs and matched controls

**Audit.** `git grep Z1477 -- data/z52b/pass2` finds no completed Z1477 outcome; the only relevant reference is the Z2819 input itself. Pass1 Z1477 (`outcome_U05.jsonl`, `U05/misc.txt`) checks `gcd(4Cp+1,4C′p+1)|(C′−C)` and a common-divisor count. It does not build the requested hypergraph. A separate old Z1729 test used eight primes and q≤200; that is not the present all-prime, full shared-prime census.

**PROVED construction.** For C,C′≤G, any shared prime q divides C′−C, hence q≤G−1. Since q∤4p, its hyperedge is precisely

`H_q(p) = {1≤C≤G : C≡−(4p)⁻¹ (mod q)}`.

Retain edges of size≥2. This is the complete shared-prime hypergraph, not a small-factor approximation. Its 2-section joins C,C′ iff gcd(4Cp+1,4C′p+1)>1. This deterministic construction does **not** by itself define a probabilistic dependency graph suitable for LLL/Janson.

**CERTIFIED computer / EVIDENCE for comparisons.** G=1024, every eligible prime p≤10⁵ (4783 hypergraphs). Persist component/isolate/giant and hit-pair counts for every graph, plus explicit labelled hyperedges for the six R-zero primes and nearest same-mod840 controls. Direct gcd comparisons independently reproduce four entire graphs.

Observed co-hits on shared edges total **56,032**. A within-prime randomization preserving the hit count in each consecutive 16-level bin has expected **21,138.01927** (ratio **2.65077**). This null does not preserve fixed-level success rates. A stronger comparator estimates each level's success probability from *other* primes in the same p mod840 class and 50000-wide size bin (17–33 primes per stratum), then sums products of these leave-one-out probabilities on the target prime's edges. It predicts **46,943.181996** co-hits, ratio **1.193613**. The singleton p=5 is excluded from the latter comparator and contributes zero co-hits. Much of the first apparent clustering is therefore level/residue structure; the remainder is descriptive, without a formal significance calibration.

| zero p | giant size | range in ten nearest same-mod840 nonzero controls | isolates | control isolate range |
|---:|---:|---:|---:|---:|
| 409 | 848 | 840–862 | 174 | 162–180 |
| 577 | 854 | 843–857 | 168 | 167–179 |
| 5569 | 852 | 836–856 | 170 | 164–186 |
| 9601 | 848 | 836–867 | 172 | 151–186 |
| 23929 | 854 | 838–854 | 166 | 169–186 |
| 83449 | 846 | 841–855 | 176 | 167–179 |

All six giant sizes lie inside their matched-control ranges. The component and isolate counts also overlap except for the small 23929 deviation (169 components versus controls 171–187). These coarse summaries do not uniformly distinguish R-zeros. This does not prove that no richer labelled-graph statistic can explain failures; a fully labelled graph carries extensive arithmetic information.

**Assessment.** Interesting because the genuine coupling has measurable co-hit structure, but using it as an independence axiom would be unjustified, and merely having a giant component does not explain the all-level failures. Data: `ZF0/Z2819/{graphs.csv,hyperedges.json,matched.csv,analysis.json}`.

## Reproduction and checks

Run from repository root. Each heavy process is single-core, under 8 GB; measured C CPU times were about 4.2 s (level census), .4 s (minimal u), 8.5 s (slices), 4.4 s (factor/hypergraph census), and 225 s (Kloosterman). Numerical Python commands should also set `OPENBLAS_NUM_THREADS=1`. Timing varies with shared-machine load. No per-item stored data directory exceeds 5 MB.

```bash
ulimit -v 8000000
export OPENBLAS_NUM_THREADS=1
# Compile each named C source with the same prefix below; -lm is harmless for all.
timeout 30s gcc -O2 -Wall scripts/z52d_p2_ZF0_Z3167_census.c -lm -o /tmp/zf0_census
timeout 1200s nice -n 10 /tmp/zf0_census 100000000 4096 data/z52b/pass2/ZF0/Z3167
# SymPy independently completes all selected hard/record/tail scans.
timeout 300s nice -n 10 uv run --with numpy --with sympy python scripts/z52d_p2_ZF0_Z3167_analyze.py

timeout 30s gcc -O2 -Wall scripts/z52d_p2_ZF0_Z1721_minu.c -lm -o /tmp/zf0_minu
set -o pipefail
timeout 1200s nice -n 10 /tmp/zf0_minu 10000000 2> data/z52b/pass2/ZF0/Z1721/run.txt | timeout 1200s gzip > data/z52b/pass2/ZF0/Z1721/minu.csv.gz
timeout 120s nice -n 10 uv run --with numpy python scripts/z52d_p2_ZF0_Z1721_analyze.py

timeout 30s gcc -O2 -Wall scripts/z52d_p2_ZF0_Z3019_slices.c -lm -o /tmp/zf0_slices
timeout 1500s nice -n 10 /tmp/zf0_slices 10000000 data/z52b/pass2/ZF0/Z3019/stats.txt | timeout 1500s gzip > data/z52b/pass2/ZF0/Z3019/slices.csv.gz

timeout 30s gcc -O2 -Wall scripts/z52d_p2_ZF0_Z1597_levels.c -lm -o /tmp/zf0_levels
timeout 300s nice -n 10 /tmp/zf0_levels data/z52b/pass2/ZF0/Z1597/perprime.csv data/z52b/pass2/ZF0/Z2819/graphs.csv /tmp/zf0_graph_hits.bin > data/z52b/pass2/ZF0/Z1597/hist.csv
timeout 30s gcc -O2 -Wall scripts/z52d_p2_ZF0_Z2819_matched.c -lm -o /tmp/zf0_matched
timeout 180s nice -n 10 /tmp/zf0_matched /tmp/zf0_graph_hits.bin > data/z52b/pass2/ZF0/Z2819/matched.csv 2> data/z52b/pass2/ZF0/Z2819/matched.txt
timeout 120s nice -n 10 uv run --with numpy --with sympy python scripts/z52d_p2_ZF0_Z2819_analyze.py

timeout 30s gcc -O2 -Wall scripts/z52d_p2_ZF0_Z0916_kloo.c -lm -o /tmp/zf0_kloo
timeout 1600s nice -n 10 /tmp/zf0_kloo < data/z52b/pass2/ZF0/Z0916/primes.txt > data/z52b/pass2/ZF0/Z0916/kloo.csv
timeout 180s nice -n 10 uv run --with numpy --with scipy python scripts/z52d_p2_ZF0_Z0916_analyze.py

timeout 180s nice -n 10 uv run --with sympy python scripts/z52d_p2_ZF0_Z3019_validate.py
```

The last check independently validates 116 minimal-u rows, 3416 slice decisions, 30 feasible rich failures and four full gcd graphs. Existing small-prime Kloosterman checks and the separate Z3167 audit provide complementary checks; no exhaustive independent re-enumeration of every large-range row is claimed.
