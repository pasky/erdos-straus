# Two distinct traps and a three-component shift obstruction

Result: at 101641 the seeds O=(p,p,p,p) and T=(p,b,pb,pb) lie in disjoint closed pair-move components with no merge, while a nested seed reaches a triple. At c=715, p=3117161329, no ES triple contains K=(p+715)/4.   Label: CERTIFIED (closures, paths, first in the six Mordell classes); PROVED (universal-seed moves, block-seed classification, fixed-K obstruction)
Scope: only the seed family named. “First” means within the Mordell-class primes. Nothing about ES.
Review: cross-lab (Opus) `data/z74/xreview/REVIEW_Z72PHASE_OPUS.md` (P17–P19 CORRECT)
Triage: METHOD-CX
STATUS delta: none
*(§0 block: z74 Opus xreview fix)*

**CERTIFIED (first simultaneous trap in the six Mordell classes).** On every such prime define `O=(p,p,p,p)` and `T=(p,b,pb,pb)`, `b=(p+2)/3`; `1/b+2/(pb)=3/p` independent of any ES solution. At the prime **101641** (`p≡1 mod 840`, `h=50821` prime) these seeds are in *disjoint* closed components without a mergeable pair. Hence no congruence invariant can prove that these two seeds cannot simultaneously fail at a nonsquare. *(z74 Opus xreview fix, clearer: no argument of any kind can show that one of O, T always reaches a merge at a nonsquare.)* This does not quantify over all imaginable seeds.

| seed | vertices | nonloop edges | nonempty BFS layers | first even |
|---|---:|---:|---|---:|
| O |20|47|1,1,1,5,4,8|5|
| T |65|306|1,13,11,26,7,5,1,1|2|

Both closure lists are independently checked by counting *every* pair representation on each slice (71 and 318 slices respectively), verifying all rational sums and proving connectivity. All 277 smaller primes in the six classes have a saved path to a merge from O or T (`pretrap_paths.json`). An independent reader checks only the path endpoints, exact sums and unchanged two denominators at every step; missing states or factorization cutoffs in the search cannot invalidate those paths. Thus **first** means first in this population, not first among all integers. `two_seed_scan.csv` is the original, capped discovery run, *not* the minimality certificate. T alone already has a closed six-vertex trap at 1009 (first hard prime), layers `1,4,1`, all denominators odd. At 14281, T escapes in four moves (O fails).

**PROVED (why the other obvious second seed fails).** For `p≡1 mod 4` put `h=(p+1)/2`, `a=(h+1)/2`. The universal seed `(a,pa,pa,pa)` is always in O, by these five pair moves (unordered):

```
(p,p,p,p) → (h,ph,p,p) → (h,h,ph,ph) → (h,h,pa,pha)
           → (a,ha,pa,pha) → (a,pa,pa,pa).
```

This also classifies all one-stage canonical block seeds: partition the four copies into blocks of size k, replace each `k/p` by `1/b_k+(k−1)/(p b_k)` written with k unit terms, `b_k=(p+k−1)/k`. Singleton and 2-block changes stay in O. The partitions `2+1+1, 2+2, 4` therefore stay in O; only `3+1` introduces T. The simultaneous trap obstructs **this entire family**.

**Analytic inspection of 14281.** The two mandatory initial forward moves are the two `p,p` splits above. For the root, `2/p` has just two unordered splits since `p` is an odd prime. At depth one the only possibly new alternatives apart from these are the mixed pairs `(h,p)` and `(p,ph)`. Both have reduced denominator `v=ph`, with numerators `21422` and `7142`. Among the 27 divisors of `v²` (`h=37·193`), the unique `d≤v` with `d≡−v mod u` is respectively `h²` and `p`; these give the original pairs. The same rigidity holds at 101641 (`u=152462,50822`, `h` prime, only 9 divisors). Later parity is not constant: even denominators do occur. The full orbit certificates, not a parity extrapolation, prove nonescape.

**Beyond the double trap (positive).** Nest the ternary block on the three equal denominators of `(a,pa,pa,pa)`: put `q=pa`, `b'=(q+2)/3`, start at `(a,b',qb',qb')`. All integral throughout the hard classes; this is not an ES-derived seed. At 101641 there is an **eight-move path** from it to a merge giving the triple `(25434,27214380,307344088620)`. The saved paths also succeed at 1009 and 14281 (2 and 5 moves). Verified rationally step by step in `nested_paths.json`. No claim of shortest depth from the nested seed or universal success. Together the three seeds suffice up to and including the first two-seed trap.

## The user's fixed K, including non-Type-II residuals

**PROVED.** Put `p=3117161329`, `q=2729`, `r=285559`, `K=qr=779290511`, `c=4K−p=715`. All three variables `p,q,r` are distinct primes. In component order `5,11,13`, the residue vectors are

```
q = (−1,  1, −1),   r = (−1, −1, 1),   p = (−1, 7, 9).
```

The ratios `r`, `q`, `qr` give `−1` on component pairs `(5,11)`, `(5,13)`, `(11,13)` respectively. But for `q^i r^j` to be `−1` modulo 11 and 13 needs both j and i odd: its sign modulo 5 is then **positive**. This is an obstruction in the generated subgroup even before bounding i,j.

Now an *arbitrary* ES triple containing K would require `1/y+1/z=c/v` with `v=pqr`. The fraction is reduced and `(cy−v)(cz−v)=v²`. Hence a divisor `d|v²` must satisfy `d/v≡−1 mod c`. Thus `d/v=p^k q^i r^j` with **all** `i,j,k∈{−1,0,1}`. Modulo 11, `7^k` must lie in `{1,−1}`; neither 7 nor its inverse is a sign, forcing `k=0`. The parity contradiction applies. So **no original ES triple contains this K**. The argument also works for any distinct primes q,r in these same residue classes if `4qr−715` is prime (no infinitude claimed). A separate check tries all 27 divisors of `v²`, confirming zero hits. At a different shift, `c=11`, an actual triple for the same prime is `(779290335,221553301293526860,68016863497112746020)`.

Replay from repository root:

```
(ulimit -v 1500000; timeout 120 uv run --no-sync python scripts/z74_checks.py)
(ulimit -v 1500000; timeout 120 uv run --no-sync python scripts/z74_first_trap.py --audit)
```

`--nested` on the first command repeats the capped exploratory nested path search. Negative answers from its pruned edges would not be certificates. No external model used.
