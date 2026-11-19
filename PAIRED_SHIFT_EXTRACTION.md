# What can be extracted after a double miss at 11?

**Verdict.** Not a divisor supported on the four proposed linear forms, even if arbitrary powers and products are allowed as the next shift. There are genuine rescues by the distinguished prime of `Q`, but no forcing by that prime alone. Below are a growing-prime family and a separate nonlinear identity; neither proves a pointwise rescue.

### The gcds and a finite falsifier (PROVED / CERTIFIED)

Use the two windows of `SIGNED_TWO_SHIFTS.md`. Write `Q=(p+11)/12`, `R=11Q−10`, `D=(p+121)/2=6Q+55`. Since `Q≡R≡1 mod 70` and `Q≠0 mod 11` for eligible p, `gcd(Q,R)=gcd(Q,D)=1`, and `gcd(R,D)|19` (use `11D−6R=665=5·7·19`). **Even 19 cannot be shared on a double miss:** its class 8 mod 11 is neither a square nor one of the exceptional pair 2,6 in the dual-failure classification. Finally `11p+121=132Q` is no new cofactor. If `q` is the distinguished prime of `Q`, then `(p/q)=(−11/q)=(q/11)=−1`; thus `q` itself is root-eligible exactly when `q≡3 mod 4`. Eligibility is not completion.

At `p=2521`, `(Q,R,D)=(211,2311,1321)` are primes. The complete **root-eligible** successful shifts are direct `{23,55,1583,13495}`, dual empty. None is supported on `{2,3,11,211,2311,1321}`, the union of the supports of `p+11,11p+1,p+121,11p+121`. This includes the eligible distinguished prime 211 and every self-product, not only squarefree shifts. The replay below enumerates sorted triples without a shift cutoff: `p/4<x≤3p/4`, `h=px,c=4x−p`, `max(x,⌊h/c⌋+1)≤y≤⌊2h/c⌋`, `z=hy/(cy−h)` integral. These bounds follow from positivity and ordering. Read both shifts from **all** slots. Here 55 does use the *unshared* constant prime 5. Adding all determinant primes does not repair the rule: at `p=12601`, `(Q,R,D)=(1051,11551,6361)` are primes, again a double miss. Adjoin `{2,3,5,7,11,19}` (all prime factors of all nonzero pairwise determinants of the four forms) to their support. The complete supported successes, **before eligibility**, are direct `{3,27}`, dual `{95,735}`. All four have `(p/d)=+1`, so even the weaker Jacobi-negative version fails.

### A two-sided neighbour on unbounded primes (PROVED, with a conditional strengthening)

Choose `a=38`, a prime `q>38`, `b=q−a`, and `p=4abt−q`. If `4a²t≡11 mod q`, then `q|p+11` and

```
4/p = 1/(abt) + 1/(pat) + 1/(pbt).
```

This follows by `a+b=q`; the direct witness is the **ratio** `a/b≡−1 mod q`. At `q=431,t=162,p=9676801`, both 11-windows fail: `Q=431·1871` of classes 2,1 and `R=8870401` prime of class 1. No ordinary divisor of `p(p+431)/4` is `−1 mod 431`; the signed ratios that hit are exactly `38/393` and its inverse (replay). Thus this is not the earlier single-prime-divisor density criterion, even with “prime” replaced by “divisor”. For fixed q it *is* an ET congruence, not a new type of ES solution.

**Unboundedness.** For any `B≥431`, set `M=12·840·11`, `L` the product of primes ≤B not dividing M. Choose by Dirichlet a prime `q>B`, `q≡431 mod M, q≡−1 mod L`. Choose `t≡162 mod M, t≡0 mod L`, and choose `t mod q²` to give `H=(p+11)/(12q)≡1 mod q` (the coefficient `4ab` is a unit there). Along this progression `p` is a positive-leading primitive linear form: at primes of M it equals the seed residue, at primes of L it is 1, at q it is −11, and at other primes of `4ab` it is −q. Dirichlet gives infinitely many prime p. They are `1 mod 840`, `2 mod 11`; `Q` has **no prime divisor ≤B** (at primes of M it has the seed residues, all units; at primes of L it is 1). The root-eligible shift q succeeds. Thus no bounded menu of prime divisors of Q accounts for these neighbour certificates. Double failure at 11 is **not** inferred on this unconditional infinite prime family.

**Conditional on Dickson for three linear forms:** in the very same progression one can take `p,H,R` all prime. Then `Q=qH`, `H≡R≡1 mod 11`, so *both* 11-windows fail and q is the unique distinguished prime. For admissibility, at primes of M the H-residues are the seed residues (q is a unit there), likewise R. At primes of L, `Q=R=1` and H is a unit. At q, `H=1`, `R=−10`. An unhandled prime dividing `4ab` must divide b (`2,19` handled), hence `q≡38` there: the only possible zeros of `p+11` or `11p+1` divide `27` or `417=3·139`, already handled. Every remaining prime is >3 and excludes at most three residues. The forms have distinct roots in the p coordinate `0,−11,−1/11`. This does not say no other ET congruence works on these primes.

### A non-congruence subfamily (PROVED for integers; CERTIFIED prime seed)

At `p=20210401`, `Q=79·21319`, `R=23·805487`; the latter three primes are all 1 mod 11, so both windows fail. At `q=79` the dual denominator uses `N=(pq+1)/4=362210·2·551`; `2+551=7q`. No prime factor of N is `−1 mod q`. This example lies on an infinite Pell orbit with **both the input and the neighbour varying on a fixed line**. Put `c=255828, T=362210, A=49T−c, n=cq−11`. Seek `N=(nq+1)/4=T ab` with `a+b=7q`. Writing `s=b−a` gives the exact conic

```
T s²=A q²+11q−1,     (2Aq+11)²−AT(2s)²=121+4A.
```

The seed is `(q,s)=(79,549)`. `D'=AT=6335944661020` lies strictly between `2517130²` and `2517131²`. Multiply the seed norm element by successive powers of a positive norm-one Pell unit >1 congruent to 1 in `(Z[√D'] / (4A·9240))` (take a power in this finite unit group). Then `q,s` remain integral in their seed classes mod 9240; `q→∞` and `s/q→√(A/T)<7`. For all sufficiently large iterates `a=(7q−s)/2,b=(7q+s)/2` are positive integers. The explicit dual triple is `(nN,7Ta,7Tb)` since `1/(7Ta)+1/(7Tb)=q/N`. This identity requires an actual square discriminant as q varies, not merely the condition `q|n+11`. The orbit grows geometrically, not in an arithmetic progression. No primality of later iterates, distinguished-prime condition, continued 11-misses, or disjointness from other ET covers is asserted.

**Steering.** The missing input is a relation forcing factors on *both sides* of `a+b=kq` in one of the new windows for a given p. The gcd and eligibility cannot supply it. Odd squares are excluded by the nonsquare class 2 mod 11 in the families; the integer identity needs no primality. Nothing here transfers to numerator 8 or infers a window hit from a restricted count.

Replay: `(ulimit -v 800000; timeout 30 uv run --no-project python scripts/paired_shift_extraction.py)`.
