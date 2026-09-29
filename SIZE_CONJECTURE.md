# Large sterile components: evidence against the size conjecture (dead hubs)

Status labels: **PROVED** = written proof here (plus a numerical check
script); **CERTIFIED** = an exact, exhaustive finite computation whose
output is re-verified by an independent checker; **EVIDENCE** = finite data
or heuristic; **CONJECTURE** = open statement.

Setting as in SIGNED_REFACTOR.md: `p=4t+1` prime, vertices are signed
solutions of `4/p=1/x+1/y+1/z`, edges join triples sharing a denominator;
Type I/II = one/two p-divisible denominators; the Type I chart is
`x=t+a`, `m=ph-t`, `e=(4a-1)h-a | (t+a)^2`, positive iff `a,h>=1`.
The **size conjecture** (SIGNED_REFACTOR §8(ii)) asked: every component with
more than `K(p)=O(log p)` vertices contains an all-positive vertex.

## 0. Verdict (short)

1. **The size conjecture fails at every scale tested, with any small
   constant; as an asymptotic `O(log p)` statement it is NOT disproved.**
   An explicit construction ("dead hubs", §3) produces sterile
   (positive-free) components of size about `3^r/2` at primes with
   `log p ~ r log r`. The hub fibre is exact (Lemma B, PROVED); sterility of
   the whole component needs a finite list of "residual checks", verified by
   exhaustive search for each instance (122 of 126 guarded instances passed,
   §3.4). If a positive proportion of the family is sterile (a heuristic,
   §3.5), sterile sizes reach `exp(c log p/log log p)`, beyond any power of
   `log p`.
   **CERTIFIED** examples (entire components exhausted, independently re-checked):

   | p | sterile component | `ln p` | size / `ln p` |
   |---|---|---|---|
   | 165426666927637 | 398 | 32.7 | 12 |
   | 475041241432047253 | 3469 | 40.7 | 85 |
   | 2192882958603411108997 | 3407 | 49.1 | 69 |
   | 1960717994383909 (random p, natural) | 339 | 35.2 | 9.6 |
   | 274159709010072908384347957 | **30035** | 61.9 | **485** |

   An `O(log p)` statement with an unspecified constant cannot be refuted by
   finitely many p. What the certificates refute is every version with
   `K(p) <= 480 ln p` at the tested primes, and in particular the use of such
   a statement as a lever (item 2). Proving sterility of an *infinite* family
   (and primality of its p) is open (§3.5).
2. **Sterile components can be larger than the seed component.** At
   `p=274159709010072908384347957` the certified sterile component has 30035
   vertices, the certified seed component 10155 (both exhausted; the seed
   component does contain 2811 positive vertices). In 13 of 14 such
   primes tried the sterile hub component was larger than the seed
   component. So *no* size threshold, and no BGS-style "one giant
   component + small rest" statement with the seed as the giant, can force
   positivity in the seed component.
3. Variants also fail: certified sterile components with **243 distinct Type I
   buckets**, and with **146 failing positive-capable denominators ("tests")**,
   come from the same method (§3.6). Size-type invariants do not see the arithmetic that makes
   the seed escape.
4. For random p the maximal sterile size grows slowly, but faster than
   `C log p`: the mean per-prime maximum fits `(log2 p)^2/50` from `2^14`
   to `10^15` (§2), and a *random* prime `p=1960717994383909` already has a
   certified 339-vertex sterile component. Nearly every large sterile
   component is a "hub" around a **negative-quadrant** denominator (anchor
   `x=t-k`, or Type I bucket `h=-c`), exactly the mechanism the construction
   amplifies. For typical p the seed component is the unique giant (§2).
5. **Proved lemmas** (§4): negative-quadrant fibres are nonpositive (A); exact
   dead-hub fibre (B); descent identity and Type II bucket structure (C);
   sign-flip exits (E): an anchor `t+a`, `a>=1`, having a prime factor
   `l = -1 (mod 4a-1)`, or a bucket `h>=1` whose `m=ph-t` has such a factor mod
   `4h-1`, has an empty fibre or a positive vertex. The specific
   component-size congruences tested (§5) do not hold.

## 1. Tools (all exact)

* `scripts/signed_components.cpp` - complete enumeration of the graph for
  `p<2^31` (x in `[1,2t]`, divisors of `x^2` filtered by residue class
  mod `4x-p`, segmented sieve, OpenMP, `__int128`), union-find components,
  `--dump S` (sterile components of size >= S), `--query D`, `--path D`
  (shortest path from the fibre of D to a positive vertex). Runs in 1.9 s at
  `p=10^8`, ~40 s near `2^31` (16 threads).
  `scripts/signed_components_check.py`: agrees with the Python complete
  enumerator (`pointwise_incidence`) on vertex counts, seed component and full
  sterile histograms for 34 primes, and every dumped sterile component is
  re-exhausted by the lazy BFS.
* `scripts/pointwise_fibres_big.py` - lazy exact oracle for any p (tested to
  `~10^28`): fresh factorizations by FLINT with **every prime factor proved**
  (`fmpz.is_prime()==1`); Type I buckets by an exact C interval scan
  (`typei_scan.c`) or by a meet-in-the-middle divisor search using the
  symmetric-chart identity `e | x^2 <=> e | m^2` and `gcd(m,4h-1)=1`;
  general divisor fibres also by meet-in-the-middle. Budget failures raise
  `IncompleteSearch`; never a verdict. Check: `pointwise_fibres_big_check.py`
  (every bucket of complete graphs at 8 primes, both Type I methods; sterile
  components re-exhausted at 4 primes).
* `scripts/sterile_certificate_make.py` / `sterile_certificate_check.py` -
  certificates `data/sterile/certs/*.json.gz`. The checker verifies each
  triple exactly, nonpositivity, connectivity, and **closure**: every
  denominator's full fibre (recomputed; anchors by the independent §3
  incidence enumeration *and* the meet-in-the-middle divisor method; Type I
  buckets by scan-or-MITM *and* by a second implementation sharing no
  enumeration code - the generic full square-divisor fibre of
  `pointwise_fibres.FibreOracle`, or a size-pruned DFS over divisors of `m^2`)
  lies inside the set. Closure + connectivity = an entire component. Only
  the factorizations (FLINT, primes proved) are common to both methods. In
  the seed certificate 11 of 3099 Type I buckets exceeded both second-method
  budgets and were checked by MITM alone; all other certificates have every
  Type I bucket checked twice. Type II and outer p-free fibres use the
  factorization-free tests of SIGNED_REFACTOR §5 (single method, validated
  against complete graphs).
* Surveys: `sterile_survey.py` (complete enumeration over primes),
  `sterile_stats.py`, `sterile_anatomy.py`, `sterile_diameter.py`,
  `sterile_tests_count.py`, `component_congruences.py`; construction search
  `sterile_hub_family.py`; lemma checks `size_conjecture_check.py`.

## 2. Random primes: growth law and anatomy (EVIDENCE)

Complete enumeration of **all** primes `p=1 (mod 4)` below `2·10^6`, plus
random samples at larger scales (`data/sterile/*.jsonl[.gz]`).

Complete enumeration (every component of every sampled prime; `signed_components.cpp`):

| `log2 p` range | primes | max sterile | mean of per-p max | frac. with max>=8 | min seed share | mean # sterile comps |
|---|---|---|---|---|---|---|
| [14,15) | 805 (all) | 16 | 4.15 | 0.06 | 0.58 | 76 |
| [16,17) | 2837 (all) | 32 | 5.28 | 0.14 | 0.54 | 131 |
| [18,19) | 10186 (all) | 34 | 6.60 | 0.29 | 0.48 | 210 |
| [20,21) | 33464 (all `<2·10^6`) | 76 | 8.01 | 0.46 | 0.41 | 315 |
| [22,23) | 2826 (sample) | 50 | 9.73 | 0.65 | 0.41 | 457 |
| [25,26) | 941 (sample) | 51 | 12.23 | 0.86 | 0.37 | 747 |
| [28,29) | 300 (sample) | 50 | 15.91 | 0.98 | 0.36 | 1140 |
| [30,31) | 64 (sample) | 40 | 16.08 | 0.98 | 0.36 | 1445 |

Beyond `2^31`, `scripts/sterile_hub_scan.py` runs the exact lazy BFS from all
negative-quadrant hubs `x=t-k`, `h=-c` (`k,c<=60`, explorations capped at
5000 vertices) of 48 random primes per scale and records the largest
component proved sterile. This is a **lower bound** for the per-p maximum.
Matched validation (same parameters, the first 64 primes of the `2^28`
complete sample): it equals the complete maximum for 48/64 primes, mean
15.3 vs 16.2 (`hubscan_validate_2e28_K60.jsonl`). An independent random
sample of 48 primes near `2^28` gave hub-scan mean 11.9 (sampling
variation plus 29 capped explorations), so the scan can undershoot.

| scale | mean of hub-scan max | largest found |
|---|---|---|
| `p~2^28` (48 other primes) | 11.9 | 22 |
| `p~10^12` | 27.6 | 80 |
| `p~10^15` | 56.4 | **339** (CERTIFIED, `p=1960717994383909`) |
| `p~10^18` | >=54 (213 hubs hit the 5000-vertex cap) | 157 |

The 339-vertex component at the *random* prime `p=1960717994383909` is a
natural dead hub: `x=t-47=2·5·11^2·13·41·313·1019·2383`, `tau(x^2)=10935`,
filtered modulo `4·47+1=189`.

* **Growth law (EVIDENCE).** The mean per-prime maximum is consistent with
  `(log2 p)^2/50` (5.1, 8.0, 12.5, 15.7, 32.8, 50.8 predicted at
  `log2 p = 16,20,25,28,40.5,50.4`, vs 5.3, 8.0, 12.2, 15.9, >=27.6, >=56.4
  observed); a pure `C log p` law with fixed C fits worse (slope per doubling
  rises from 0.6 to 1.0 and beyond). The aggregate size histogram decays
  roughly geometrically for small sizes with a heavier tail; the number of
  sterile components per prime grows like `p^{0.2}`. Heuristically, the
  maximum is governed by the largest filtered divisor count
  `tau((t-k)^2)/phi(4k+1)` among dead-looking hubs, which is polylogarithmic
  for typical p but unbounded by any polylog for adversarial p (§3).
* **Typical p, BGS-like picture (EVIDENCE).** For all 78416 primes of the
  complete surveys up to `2^25` the seed component is the largest component,
  and every other component has at most 0.16 of its size (0.05 at `2^30`).
  The seed's share of all vertices declines slowly (0.58 -> 0.36), so the
  old ">= 58%" observation does not persist. This typical-p dichotomy is
  destroyed at adversarial p (§3.4).
* **Anatomy.** Every dumped sterile component (size >= 12, `p<2·10^6`) has
  a hub: the denominator shared by most vertices. In 6181 of 6658 it is a
  negative-quadrant denominator: a p-free anchor `x=t+a` with `a<=0` (5011)
  or a Type I bucket with `h<=0` (1170); only 386 hubs are anchors with
  `a>=1` and 91 buckets with `h>=1`. Negative-quadrant fibres are exactly those
  of Lemma A, whose entire fibre is
  nonpositive; e.g. the 43-vertex component at `p=663557` is the fibre of
  `x=t-3` (31 vertices) plus 12 satellites. Diameters are small (<= 8).
* No component-size congruence (§5).

## 3. Dead hubs: the construction

### 3.1 The hub fibre (Lemma B, PROVED in §4)

Fix `k>=2`, `M=4k+1`, and let `x=t-k>=1` have **all prime factors
`= 1 (mod M)`**. Then the fibre of x is exactly

\[
 V_d=\Bigl(x,\;-\frac{p(x-d)}{M},\;\frac{p\,x(x-d)}{Md}\Bigr),
 \qquad d\mid x^2,\ d<x,
\]

`(tau(x^2)-1)/2` Type II vertices, all nonpositive, and none of them is Type I.
(So x is automatically not in the `-pt` hub fibre of the seed.)

### 3.2 Where the spokes lead (Lemma C, PROVED)

For a spoke `V_d` write `mu=(x-d)/M`, `n=x mu/d`. If `n>=2t` the bucket `pn`
is `{V_d}` (privacy, SIGNED_REFACTOR §5). The bucket `-p mu` consists of the
Type II vertices given by signed divisors `D | mu^2` with `D = d (mod 4mu+1)`,
at most two in total; `D=d` is `V_d`. If `d | x` and `w=x/d = 1 (mod 4)`,
the second one is always present: it is the **descent vertex**

\[
 D_d=\Bigl(x-d,\;-\frac{p(x-d)}{M},\;-\frac{p(w-1)}{4}\Bigr),
\]

whose p-free anchor `x-d=d(w-1)` is again `< t`, so its whole fibre is
nonpositive (Lemma A). Numerically, *every* live spoke of the unguarded hubs
was of this form.

### 3.3 The guard

Descents with small d lead to anchors `x-d` with small modulus `M+4d`, whose
fibres are large and may escape. Choose all prime factors `= 1 (mod 4M)`
except one "guard" prime `q0 = 1 (mod M)`, `q0 = 3 (mod 4)`, `q0 ~ 10^4`.
Then `w | x`, `w = 1 (mod 4)` forces `q0 ∤ w`, so every descent has
`d >= q0`, and the descent anchors have moduli `>= 4q0`. In the typical
outcome the component is **exactly** the hub plus the `2^r-1` descents:

\[
 |C| = \frac{3^{r+1}-1}{2} + 2^r - 1
\]

for x = q0 times r primes (e.g. 30035 = 29524 + 511 at r=9).

### 3.4 Results (CERTIFIED where certificates exist; otherwise exhaustive lazy BFS)

All runs: `k=2` (`M=9`), exact lazy BFS to exhaustion (`STERILE`) or to a
positive vertex (`FOUND`); `data/sterile/hubs/*.jsonl`.

| family | r | hub fibre | sterile / tried | component size | p range |
|---|---|---|---|---|---|
| unguarded, primes = 1 mod 9 | 6 | 364 | 7/32 (+3 unknown) | 397-442 | 6e12-3e16 |
| unguarded | 7 | 1093 | 3/32 | 1175-1183 | 4e15-2e18 |
| unguarded | 8 | 3280 | 1/32 | 3469 | 6e16-2e18 |
| guarded, q0~10^4 | 5 | 364 | 31/32 | 395-397 | 1e15-2e18 |
| guarded | 6 | 1093 | 32/32 | 1156-1161 | 5e17-2e18 |
| guarded | 7 | 3280 | 15/16 | 3407-3415 | 4e20-3e23 |
| guarded | 8 | 9841 | 14/16 | 10096-10098 | 1e23-2e25 |
| guarded, sparse t (tau(t^2)<=9) | 7 | 3280 | 16/16 | 3407-3408 | 4e20-6e22 |
| guarded, sparse t | 9 | 29524 | 14/14 | 30035-30039 | 2e26-1e28 |

(`k=3`, `M=13` gives the same picture.) For the sparse-t runs the entire
seed component was also exhausted: sizes 6032-22605 at r=7 and 9431-78704 at
r=9; **the sterile component exceeded the seed component in 13 of the 14
r=9 cases.** Certificates: `data/sterile/certs/` (the r=9 prime has both a
sterile and a seed certificate).

```sh
PYTHONPATH=scripts uv run --with python-flint python scripts/sterile_certificate_check.py data/sterile/certs/*.json.gz
```

### 3.5 Growth law and what is not proved

With the r smallest admissible primes, `log p ~ r log r`, so the family has
size `~3^r = exp((log 3+o(1)) log p / log log p)` **provided** its members are
sterile and `p=4(x+k)+1` is prime for suitable choices. Neither is proved:

* primality of `4(x+k)+1` over products of primes in progressions is a
  standard heuristic, unproved for this thin set;
* sterility needs finitely many *residual checks* per prime (no extra
  divisor `D` in the spoke buckets, descent anchors and descent third
  coordinates with trivial fibres, or, if not trivial, no route to a
  positive-capable denominator). Each check is a divisor-in-residue-class
  event with modulus `>= 4q0` (descents) or `~x/M` (spoke buckets). The
  descents are `d = q0·u`, `u | x/q0`, so the naive expected number of
  extra neighbours is about `q0^{-1} sum_{u | x/q0} tau(...)/u`, and
  `sum_{u} 1/u = prod(1+1/q_i)` **grows** (slowly) with r. For a *fixed*
  guard this does not give a probability bounded below; the heuristic
  version is: let the guard grow with r, e.g. `q0 >= prod(1+1/q_i)·(log p)^A`,
  which costs only a factor `q0` (polylog) in p and leaves the
  `exp(c log p/log log p)` size law intact. Spoke-bucket failures have
  naive probability `O(3^r·tau/x)`, tending to 0. In the data a fixed guard
  `q0~10^4` sufficed up to r=9 (122/126 sterile), but this is finite evidence
  only; also a failed check need not destroy sterility, since extra
  neighbours of anchors `<t` are themselves nonpositive (Lemma A).

So: **the size conjecture is false for all practical constants, and false
asymptotically under a mild heuristic**; an unconditional disproof of the
`O(log p)` form would need an infinite family with provable residual checks.

### 3.6 Other size-type invariants fail too

* **Type I count / Type I buckets.** Take `M=13`, `k=3`, prime factors in the
  odd-order subgroup `{1,3,9}` mod 13 (it contains `k=-1/4` but not `-1`), all
  `>= 3000`, plus a guard. Then the hub fibre also has Type I vertices,
  `e=d = 3 (mod 13)`, `h=(3-d)/13<=0`, each in its own bucket. 13/16 such hubs
  (r=5, `p~10^24`) were sterile, each with ~280 Type I vertices.
  CERTIFIED: `p=691188894734138813322041`, a 409-vertex sterile component
  with **243 distinct Type I p-divisible buckets**
  (`certs/p691188894734138813322041_typeI.json.gz`).
* **Tests.** A positive vertex has p-free denominators `>t` and a Type I
  bucket `h>=1` or non-residue Type II labels ("positive-capable
  denominators", tests). Allowing residues `{±1,±3,±9}` mod 13 produces Type I
  spokes with `h=(3+d)/13>=1`. 2/16 such hubs were sterile; CERTIFIED:
  `p=433393973269554421280441` (`ln p = 54.4`), a 412-vertex sterile component
  containing **146 failing tests** (smallest modulus 1231)
  (`certs/p433393973269554421280441_tests.json.gz`). The tests are weak, which
  is the point: a failing test with huge modulus is cheap. Pushing r up
  should give `3^r`-many failing tests, at a lower sterility rate (untested).

So "bounded number of Type I buckets", "O(log p) Type I vertices" and
"O(log p) failing tests" are all refuted in the same practical sense.

## 4. Proved lemmas

**Lemma A (negative quadrant; PROVED).** If a p-free `1<=x<=t` or a Type I
bucket `p(ph-t)` with `h<=0` occurs in a vertex, that vertex is nonpositive.
*Proof.* `4/p-1/x=(4x-p)/(px)<0`, so the other two denominators cannot both be
positive. For `h<=0`, `m=ph-t<0`. ∎

**Lemma B (dead-hub fibre; PROVED).** Let `k>=2`, `M=4k+1`, `x=t-k>=1`, and
suppose every prime factor of x is `1 (mod M)`. Then the vertices containing
x are exactly `V_d` (§3.1), `d | x^2`, `d<x`; there are `(tau(x^2)-1)/2` of
them, all Type II and nonpositive.

*Proof.* `q=4x-p=-M`. By the exact incidence model (SIGNED_REFACTOR §3) the
vertices containing x are `(x,pm,pxm/f)` with `f=qm-x` a nonzero divisor of
`px^2`, i.e. `f=±p^j d`, `d | x^2`, `j∈{0,1}`, subject to `f = -x (mod M)`.
All divisors of `x^2`, and x itself, are `1 (mod M)`, and
`p=4x+M = 4 (mod M)`. Hence `d = 1`, `-d = -1`, `pd = 4`, `-pd = -4 (mod M)`.
The target is `-x = -1`. `+d` would need `M | 2`; `pd` needs `M | 5` (k=1);
`-pd` needs `M | 3`. Only `f=-d` survives. Then `m=(x-d)/(-M)=(d-x)/M`
(integral as `d = x = 1`), nonzero iff `d≠x`, and the third denominator is
`pxm/f = p x(x-d)/(Md)`. Since `f` is prime to p this is Type II.
Replacing d by `x^2/d` swaps the two p-divisible coordinates, so the vertices
are indexed by the pairs `{d, x^2/d}` with `d≠x`; distinct pairs give distinct
`m`-sets. Exactly one of `m, n` is negative. ∎

**Lemma C (descent; PROVED).** (i) Let `d>=1`, `w>1`, `w = 1 (mod 4)`, `x=dw`,
`M=p-4x>0` with `M | x-d`. Then `V_d` and
`D_d=(x-d, -p(x-d)/M, -p(w-1)/4)` are signed solutions sharing `-p(x-d)/M`.
(`w=1` would give zero denominators.) (ii) Under Lemma B, for a spoke
`d<x`, the bucket of `-p mu` (`mu=(x-d)/M`) consists of the
vertices `(y,-p mu, z)` with `y=(p mu+D)/K`, `K=4mu+1`, for signed p-free
`D | mu^2`, `D = d (mod K)` (and y, z nonzero); `V_d` is `D=d`; if moreover
`d | x` and `w=x/d = 1 (mod 4)`, then `D=-4d mu` gives `D_d`.

*Proof.* (i) `1/x - M/(p(x-d)) + Md/(px(x-d)) = (p-M)/(px) = 4/p`, and
`1/(d(w-1)) - M/(pd(w-1)) - 4/(p(w-1)) = (p-M-4d)/(pd(w-1)) = 4/p`; integrality:
`M | x-d`, `4 | w-1`, `w(x-d)/M` integral. (ii) With `1/y+1/z=(4mu+1)/(p mu)`
one has `(Ky-p mu)(Kz-p mu)=p^2mu^2`. The label `-(4mu+1)` of `-p mu` is
nonzero mod p (it is Type II), so for the p-free coordinate y,
`D=Ky-p mu = Ky (mod p)` is prime to p, hence `D | mu^2`. For `y=x`:
`Kx-p mu = d` (direct computation using `p=4x+M`,
`K=(p-4d)/M`), and all admissible D share its class mod K. For `D=d-Kd=-4d mu`,
`y=x-d`; `D | mu^2` iff `4d | mu = d(w-1)/M` iff `4M | w-1`. Here `M | w-1` holds automatically, because `M | d(w-1)` and `gcd(d,M)=1` under Lemma B's hypothesis (every prime of `x` is `1 (mod M)`). So the condition is `w = 1 (mod 4)`. ∎

**Lemma E (sign flip; PROVED).** Let `x=t+a`, `1<=a<=t`, `q=4a-1`, and let
`l | x` be a prime with `l = -1 (mod q)`. If x occurs in any vertex, it occurs
in a positive one. Likewise, if `h>=1`, `H=4h-1`, and `m=ph-t` has a prime
factor `l = -1 (mod H)`, then the Type I bucket `pm` is empty or contains a
positive vertex.

*Proof.* Anchor. By SIGNED_REFACTOR §3 the vertices containing x are
`(x,pm,pxm/f)` where `f=qm-x` is a nonzero divisor of `px^2` with
`f = -x (mod q)`, `m=(x+f)/q`; since `q>0`, such a vertex is positive iff
`f>0` (then `m>0`; criterion (5) there). Suppose x occurs, via some `f`. If
`f>0` we are done. Otherwise `f=-p^j d` with `j∈{0,1}`, `d | x^2`, `d>0`,
and `p^j d = x (mod q)`. Put `d'=l d` if `v_l(d)<2v_l(x)`, else `d'=d/l`
(then `v_l(d)=2v_l(x)>=2`). In both cases `d' | x^2` and, as
`l = l^{-1} = -1 (mod q)`, `d' = -d (mod q)`. Hence `f'=p^j d'>0` divides
`px^2` and `f' = -x (mod q)`, so `m'=(x+f')/q` is a positive integer and
`(x,pm',pxm'/f')` is a positive signed solution (`p ∤ m'` automatically,
by the valuation lemma of SIGNED_REFACTOR §2).

Bucket. Every vertex of the Type I bucket `pm` has chart coordinates
`(a,h)` with `x=t+a` p-free, `e=aH-h≠0`, `e | x^2`; it is positive iff
`a>=1` (as `h>=1`). For `a>=1`, `e>=3h-1>0`; for `a<=0`, `e<=-h<0`. By the
symmetric chart (SIGNED_REFACTOR §8: `Hx=m+e`, `gcd(H,e)=1`) and
`4m-pH=1` (so `gcd(m,H)=1`), a positive integer `e'` prime to H satisfies
`e' | m^2 <=> e' | (t+a')^2` whenever `e'=a'H-h`. Given a vertex with `e<0`,
flip `d=-e | m^2` to `d'=l^{±1}d | m^2` as above; then `e':=d'>0` and
`e' = -d = e = -h (mod H)`, so `a'=(e'+h)/H` is a positive integer, and
`e' | (t+a')^2`. The triple `(t+a', pm, (t+a')m/e')` is then a signed
solution with `a',h>=1`, i.e. positive (§4 there); `t+a'` is prime to p, as
otherwise all three denominators would be p-divisible (`e' | m^2` is prime
to p), contradicting §2 there. ∎

(The same argument works with `l^j = -1 (mod q)` for some `j <= v_l(x)`.)
Consequence: in a sterile component every positive-capable anchor/bucket has
no prime factor `= -1` modulo its own modulus - a classical-type
restriction, **not** a bound on size (the certified dead-hub components
contain 0, 0, 1 and 17 positive-capable denominators, all of large modulus:
the hub fibre itself has none by Lemma B, but satellites can).

Checks: `scripts/size_conjecture_check.py` (Lemma A on 181358 fibres,
Lemma E on 1442 anchors and 1387 buckets of complete graphs, Lemma B on 115
small and 48 large hubs, Lemma C(i) on 4367 random instances, Lemma C(ii):
1313 spoke buckets equal the divisor description, 291 predicted descents
present).

## 5. Congruences and a BGS-type statement

Following LITERATURE_2026 §3 (Markoff mod p: BGS giant component, W. Chen's
divisibility): over 64k primes (`p<2^23`), the seed-component size and the
total vertex count are close to equidistributed modulo 2,3,4,5,6,8,12, and
seed size is `0 mod tau(t^2)` for 1216/20000 primes vs 1184 expected at
random (`scripts/component_congruences.py`). Sterile sizes are *not*
equidistributed (about 8:1 odd:even), but only because the size histogram
is dominated by singletons and other small sizes; every residue occurs, so
there is no divisibility constraint of Chen type for sterile components.
Thus none of the tested congruences (seed size, V, or sterile sizes modulo
these m, seed size modulo `tau(t^2)`) holds; other moduli, e.g. p, are
moot since all components are far smaller than p. A
BGS-type "seed = unique giant, everything else small" statement is refuted
by §3.4 (a sterile component three times larger than the seed component).
(The signed character theorem (2a) is Bright–Loughran 2020, Thm 1.2+1.5.)

## 6. What this means for the programme

* A proof of seed reachability cannot come from "large components exit" plus
  "the seed is large": sterile components can be larger than the seed.
* What the seed has and dead hubs lack is **cheap tests**: the seed component
  always contains the Type I buckets `h=d` and anchors `t+d` for all
  `d | t^2`, in particular the modulus-3 tests `h=1`, `a=1` (SIGNED_REFACTOR §7);
  the certified guarded dead hubs contain none or only a few
  positive-capable denominators, all of large modulus (>= 4·8963-1 in the
  certificates), and the test-rich sterile hubs of §3.6 likewise only tests
  of large modulus (>= 1231). By contrast the natural 339-vertex sterile
  component at a random p has 118 failing tests, smallest modulus
  `4·645-1`. Any
  replacement statement must weigh tests by their modulus (the chance that a
  divisor of `m^2` lands in one class mod `4h-1`), which is again the
  classical ES divisor-class problem.
* **CONJECTURE (weak replacement, untested beyond this data):** every
  component containing a positive-capable denominator of modulus
  `<= (log p)^A` with "generic" factorization exits; this is essentially the
  ES heuristic, not a structural shortcut.
