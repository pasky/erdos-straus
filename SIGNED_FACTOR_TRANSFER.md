# Moving the factor from a failed shift 11

**Result.** Keeping `AB=f` never works. Even keeping `f | K=ABD` is impossible if `4f≥33h+11`. Moving instead to `K=3h(f+1)` gives a **proved sufficient condition** at the variable shift `12h+11`, including a root for composite shifts. It is not a universal repair. At `h=1` there is an exact obstruction at the successor shift 23.

Assume throughout that `p≡1 mod 840` is prime and the direct slot fails at eligible 11. By `SIGNED_TWO_SHIFTS.md`, `p=12fh−11`, `f` prime of class `p=2 or 6 mod 11`, and all prime factors of `h` are `1 mod 11`. Thus `f≥13` (Q is odd), `gcd(f,h)=1`. The sign really is forced: `(f/p)=(−11/f)=(f/11)=−1` by reciprocity. This alone does not put `f` in any denominator.

## Keeping the factor: lossless bounds (PROVED)

Use the normalized Type II equations `p+c=4ABD`, `A+B=cE`, `gcd(A,B)=1`, all positive. The triple is `(K,pADE,pBDE)`. Since `c≤A+B≤AB+1≤K+1`, `3c≤p+4`. If `AB=f` then `c≤f+1` and `c=11+4f(D−3h)>0` force `D=3h,c=11`, already a miss. Likewise for `AB=h>1` (`h≥23`). At `h=1`, the tempting `c=4f−1` itself exceeds the shift bound; `4f+1` is not `3 mod 4`.

More generally take `wv=fh`, `w=f` or `w=h>1`. For `w|K`, positivity and the bound give

```
c=11+4wj,     0≤j<v,     K=w(3v+j).
```

The exact remaining test is a coprime split `AB|K` with `c|A+B` (equivalently a divisor `t|K²`, `t≤K`, `t≡−K mod c`). Thus the interval is not a heuristic cutoff; `j=0` is known to fail.

**Large-f obstruction.** Suppose `4f≥33h+11`, `w=f`, `j≥1`. If `f|D` then `c≤AB+1≤3h+j+1<c`. Otherwise swap sides to write `A=fa`, `aBD=3h+j`. Now `c | 4jB−11a` since `4jf=c−11`. Both `4jB` and `11a` are less than `c`: `B≤3h+j<4h≤f` and `11a≤33h+11j≤4fj`. Thus `4jB=11a` and `cE=fa+B` gives `a=4jE`, `B=11E`. Coprimality forces `E=1`. This would give `3h=j(44D−1)`, impossible: all divisors of `3h` are `1 or 3 mod 11`, never `−1`. ∎

## Changing the shift (PROVED; examples CERTIFIED)

* **Retain `h`, increment `f`:** set `c=12h+11`, `K=3h(f+1)`. If `12 | f+1` and **`c | f−98`**, take `a=(f+1)/12`, `b=9h`, `D₀=4`. Then `abD₀=K` and `12(a+b)=f−98+9c`. Since `gcd(12,c)=1`, `c|a+b`. Normalize by `g=gcd(a,b)` to `(A,B,D)=(a/g,b/g,4g²)`: `gcd(b,c)=1` since `gcd(h,11)=1`, so division preserves the shift congruence. Moreover `−p≡−4K≡(4a)² mod c` with a unit root. At the joint failure `p=2044561`, `f=2543,h=67,c=815`, this gives `(A,B,D,E)=(212,603,4,1)`. No assertion that the hypotheses force primes or follow from failure at 11.
* **Move from the factors into their difference:** at the joint failure `p=76441`, `f=277,h=23`, *neither* factor can be retained in `K` (complete interval tests). Yet `c=(f−h)/2=127` gives `(17,1126,1,9)`, again with a unit root (`D=1`). Conversely retaining `f` sometimes works: `p=206641`, `f=17,h=1013`, `c=4f+11=79`, `(85,152,4,3)`.
* **Boundary:** at the joint failure `p=1711921`, `f=431,h=331`, neither retained factor nor `12h+11` gives a Type II witness. *All* new positive `3 mod 4` divisors of `4f−1,4f+1,|f−h|,f+h` are `3,15,23,75,115,127,575,1723`; not one works even in either unrestricted slot of `SIGNED_TWO_SHIFTS.md`. This falsifies that specific menu, not all data-dependent choices.

## Why the successor works at 2521 and 12601 (PROVED)

Shift 23 is `12h+11` when `h=1`. More generally, write `Q=fh`, `L=(Q+1)/2`. At 23, `K=6L`, `p=24L−23≡L`, `N=(23p+1)/4=6M` with `M=23L−22≡1` (residues here mod 23). Suppose 23 is eligible. Then:

* **Type II fails iff**, deleting all 1-class prime occurrences of `L`, there remains exactly one occurrence, of class 5 or 14. Unrestricted direct failure is **identical**.
* **Type I fails iff** all factors of `M` are squares mod 23, or its non-1 occurrences are exactly one 5 and one 14.

**Proof.** A signed product uses each prime with exponent of absolute value at most its valuation. Target `−1` in the signed products of `K,pK,N` tests Type II, unrestricted direct, Type I respectively. Reserve the factors 2 and 3 of 6. Their signed products are the squares `{1,2,3,4,6,8,12,13,16}`, missing just `9,18` from the square subgroup. Hence every signed nonsquare from the rest works except `−9,−18`, i.e. `14,5`, an inverse pair. In a failure every nonsquare prime occurrence must be of this pair. An additional nonidentity square prime of class `s` gives three distinct nonsquares `r,rs,r/s` with any nonsquare occurrence `r`. Three nonsquare occurrences can instead be oriented to `5³=10`, outside the pair. For `L`, the total sign is negative, so exactly one occurrence remains after deleting ones; conversely that shape misses. Allowing the extra `p≡L` still misses: the two nonsquare occurrences together give a square, singly only the same inverse pair. For `M≡1`, the count of nonsquare occurrences is even; if nonzero in a failure there are just two and their classes must cancel. The converse follows by the same parity check. ∎

In particular if `Q≡3 mod 4` and 23 is eligible, there is **always** a Type II witness: the extra 2 in `L` is a nonidentity square. At `h=1` the negative prime used here comes from `f+1`, not from reusing `f`. The exact triples below satisfy `4xyz=p(xy+xz+yz)`; independent enumeration by the smallest denominator gives 9 and 27 sorted triples respectively, **none with `f` dividing any slot**, even allowing Type I.

|p|f|A,B,D,E at 23|x,y,z|
|---:|---:|---|---|
|2521|211|2,159,2,7|636,70588,5611746|
|12601|1051|3,526,2,23|3156,1738938,304893796|

The extra hypothesis matters: `p=9565921`, `h=1`, `f=797161`, `L=398581` prime of class 14, misses in **both** families at **both** eligible primes 11 and 23.

## Bounded replay (CERTIFIED; not an existence proof)

All 3426 primes `1 mod 840` through `10⁷`. Counts are inputs, not witnesses. “Joint” means both slots fail at 11; “root” requires `−p` a unit square at the actual shift. The factor-divisor menu is exactly the one in the boundary example above.

|condition|direct failures at 11|joint failures at 11|
|---|---:|---:|
|inputs (`h>1`)|244 (59)|158 (40)|
|large-f obstruction applies|203|131|
|can retain `f` / nontrivial `h` in Type II `K`|24 / 14|18 / 9|
|23 eligible / eligible and Type II works|113 / 109|71 / 67|
|factor-divisor menu works in Type II / also root|221 / 89|141 / 53|
|`h>1`, `12h+11` works in Type II / also root|2 / 1|1 / 1|

Falsifier screens (inputs in the stated domain / total): F1 odd squares 0/50; F2 numerator-8 zeros 0/12; F3 composite zeros 0/285; F4 star/gstar 0/14, 0/38. No claim about numerator 8 or the restricted counts. Replay checks the original integer equation on every returned certificate and compares both 23 classifications with divisor enumeration at all eligible survey primes.

```
(ulimit -v 800000; timeout 90 uv run --no-project python scripts/signed_factor_transfer.py)
```

**Steering.** Treat factor retention as ruled out on the large-`f` branch, not as a missing search range. For a successor-shift argument the real unresolved case includes `h=1, L` with the single bad class above; even eligibility at two shifts does not remove it.
