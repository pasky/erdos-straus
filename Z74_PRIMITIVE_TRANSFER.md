# Primitive pairs in one-slot ES transfers

```
Result: exact primitive-pair criterion and sharp ceiling p≤Q(Q+r)/(4r)+1 for lower one-slot transfers; infinite Dirichlet families in both directions inside 1 mod 840 with unbounded j, p/Q and k; exact upper-direction test.
Label: PROVED (criteria, ceilings, families via Dirichlet) | CERTIFIED (examples, (Q,p)=(18,23) minimum j=2)
Scope: one-slot transfers only; the target progressions are ET congruence classes (ET Prop. 1.9), not new coverage. ES is OPEN.
Review: cross-model, data/z74/xreview/REVIEW_SHIFTS_OPUS.md (ACCEPT-WITH-FIXES; no gap) (z74 Opus xreview fix)
Triage: METHOD-CX
STATUS delta: none
```

**PROVED.** Write `p>Q` for an odd prime, `p∤k`, and keep two slots after scaling a donor for `4/Q` by `k`. There are infinite ordinary-prime transfers in **both** directions, even inside `1 mod 840`. The lower direction does not force `j=1`, nor an absolute bound on `j` or `p/Q`. None of the infinite target progressions below is new coverage beyond Elsholtz–Tao (ET).

## Lower direction: a sharp ceiling and an exact fixed-Q maximum

For `p<kQ` the obstruction in `Z74_ONE_SLOT.md` forces two donor denominators divisible by `p`, one of them changed. Briefly, if the changed `u` were prime to `p`, put `u/Q=r/t` in lowest terms. Then `v=kpQr/(pt+4(kQ−p)r)`; its positive denominator is coprime to `pr`, hence divides `kQ`, but exceeds it. The donor identity mod `p` forces a second multiple, while three multiples contribute at most `3/p`.

Write the donor `(x,gA,gB)`, `A≤B`, `gcd(A,B)=1`. Then `Q/4<x≤pQ/(4p−2Q)<Q/2`. Put `T=4x−Q`, `a/b=T/(Qx)` in lowest terms. The donor identity becomes `agAB=b(A+B)`, hence **`AB|b`, `a|A+B`, `g=(b/AB)(A+B)/a`**. Since `p>Q>x,T`, neither `a` nor `b` is divisible by `p`. Thus `p|g` iff `ap|A+B`; in `A+B=pj`, the integer `j` is a multiple of `a`, not necessarily 1. All the displayed pair conditions are sufficient as well as necessary.

Set `r=4−(Q mod 4)` in `{1,2,3,4}`, `x₀=(Q+r)/4`. Using `A+B≤AB+1` gives

```
p ≤ (A+B)/a ≤ (b+1)/a ≤ Qx/(4x−Q)+1 ≤ Q(Q+r)/(4r)+1.
```

The last function decreases strictly in `x`. In particular `p/Q≤Q/(4r)+1/4+1/Q`. The endpoint, before imposing primality, requires and suffices for the donor shape `x=x₀, a=1, A=1, B=b, p=b+1` (assuming the stated `p>Q` and prime). Thus the large donor denominators are `p,p(p−1)`. **The ceiling is attained even with repair**: `Q=23,p=139,x=6`, donor `(6,139,19182)`, `k=35`, replacement `v=42` for the last slot. This is attained sharpness, not a claim of infinitely many primes at the quadratic endpoint. In the top half of a *fixed row*, `p>(b/2+2)/a` forces `(A,B)=(1,b)` and `j=a`: otherwise `AB` is a proper divisor or `2≤A≤√b` and `A+B≤2+b/2`; also `2ap>b+1`.

**Exact alternative, including integrality of the repair for arbitrary k.** For each integer `Q/4<x<Q/2` enumerate `P|b`, `A|P`, `A≤B=P/A`, `gcd(A,B)=1`. The quadratic-root version simply tests if `(pj)²−4P` is a nonnegative square of the correct parity. More cheaply factor `(A+B)/a` if integral and take each prime divisor `p>Q`. Compute `g` as above. For each retained `y=gA` or `gB`, write `1/x+1/y=c/e` in lowest terms. The target condition, with unknown `k,v`, is exactly

```
(4ek−pc)(4v−p)=p²c.
```

Try every positive factor pair `(l,m)` of `p²c`; keep integral `k=(l+pc)/(4e), v=(m+p)/4` with `kQ>p, p∤k`. Positivity of both factors follows from the target identity, and expansion proves sufficiency. The largest prime retained (or an empty set) is the **exact sharp fixed-Q answer**, without guessing a bound on `k`. The factor-pair step alone works for either sign on any specified pair of donor slots. **CERTIFIED:** at `(Q,p)=(18,23)` the only possible `x` are `5,6,7`, with `(a,b)=(1,45),(1,18),(5,63)`. The only pair passing `ap|A+B` is `(1,45)` in the first row. So even *minimizing* over donors gives `j=2`. Changing `3·2070` to `10` works.

## Lower direction: unbounded j and p/Q on hard-class primes

**PROVED construction.** Choose positive `j≡7 mod 840` and a prime `s≡11 mod 840`, `s>j`. Put `D=sj−1`. Take primes `p` satisfying

```
p≡1 mod 840,       jp≡−1 mod 4s²D.
```

There are infinitely many: `gcd(j,4s²D)=1`, `gcd(840,4s²D)=8`, and `j≡−1 mod 8`, so CRT gives a unit progression and Dirichlet applies. Define `x=(jp+1)/(4s)`, `Q=4x−j`; in particular `sD|x`. For all sufficiently large such primes (`p∤s`):

```
donor     (x, px/s, pxQ/D),          k=s²,
target    (s²x, spx, s²x/D).
```

The sum of the last two donor reciprocals is `(sQ+D)/(pxQ)=j/(xQ)`, and the target identity follows from `4s²x=sjp+s`. Here `p/Q→s/j>1` while `kQ>p`; the replacement is strict. The two donor multiples have primitive pair `(D,sQ)` up to sorting: `gcd(D,sQ)=1` since `Q≡−j mod D`. Their sum is exactly `jp`. Vary `s` for an arbitrarily large limiting ratio, and vary `j` for arbitrarily large primitive sums relative to `p`. This latter statement concerns the exhibited donors, not a growing lower bound for the minimum over *all* donors. Example `j=7,s=11`: the progression is `3636361 mod 3862320`; its first positive term is prime, with `Q=2314041`, `x=578512`, replacement `921052`.

**PROVED construction with k growing along a single progression.** Take `p≡178081 mod 209160` prime (a unit class `1 mod 840`), `x=(9p+1)/83`, `Q=4x−2`, `k=(p+83)/36`. The congruences are `9p≡−1 mod 83`, `p≡−83 mod 36`, and `18|Q` since `83Q=36p−162`. The retained donor pair `(x,9px)` sums in reciprocals to `83/(9p)`; the changed slot is `u=pQ/18` because `4/Q−83/(9p)=18/(pQ)`. After scaling, `v=9k`: the target sum is `(83+p)/(9pk)=4/p`. Thus `k→∞`, `Q<p<kQ` for all sufficiently large members. This varies the shift as well; it does not contradict the fixed-`k,d` lower obstruction. Both lower infinite constructions use the stated hypothesis `d=kQ−p>0`, not an extra requirement `d<Q`: neither establishes an infinite lower transfer from the *nearest* larger multiple.

## Upper direction: what u/Q actually decides

**PROVED.** Let `p=kQ+d`, `d>0`, and reduce `u/Q=r/t`. Now `h=pt−4dr` must be positive and `v=kpQr/h`. If `p∤u`, then `gcd(h,pr)=1` and the **exact test** is `h>0` and `h|kQ`. For such a success put `m=kQ/h`. Then

```
u/Q = [p−(p−d)/(mt)]/(4d),
(p+d)/(8d) ≤ u/Q < p/(4d).
```

Indeed `mt=1` would give `r/t=1/4`, impossible in a positive triple. The lower endpoint is attained: `p=7,k=2,d=1,Q=3`, donor `(2,2,3)` and replacement `v=14` for the last slot. The interval tests magnitude, not the divisor condition. If `p|u`, use `h|kpQr` without cancelling `p`. These statements do not assume a smallest donor slot.

**PROVED fixed-(k,d) family.** For every prime `p≡24361 mod 101640` sufficiently large (a unit class `1 mod 840`), put `R=(3p+1)/4`, `Q=(p−161)/2`. Here `11|R` and `484|Q` by `p≡161 mod 968`. Take

```
donor     (2R/11, 2R, QR/484),       k=2, d=161,
target    (4R/11, 4R, pR).
```

One way to obtain the donor rather than guess it is to choose the retained pair so its sum is `6/R`; the residual is `484/(QR)` since `4R−6Q=484`. The target sum is `3/R+1/(pR)=4/p`. Thus the selected slot is prime to `p`, `u/Q=(3p+1)/1936`, and the replacement is strictly larger, as required. Example `p=126001`, `Q=62920`: replace `2·12285130` by `11907220501`.

**PROVED failure of interval-only selection.** Take `p=13,k=2,Q=6,d=1`, donor `(2,12,12)`. The slot `u=12` has `u/Q=2` in `[14/8,13/4)`, but `h=5` does not divide `12`. The slot `u=18` of the different donor `(2,9,18)` has `h=1` and succeeds at the same input.

**Scope / falsifiers.** The displayed target triples are polynomial identities on finer progressions, hence ET territory (ET Prop. 1.9); in the upper example the split `3/R=11/(4R)+1/(4R)` is just Type I. The extra assertion here is compatibility with an integer donor and a signed one-slot repair. There is no demonstrated coverage outside known identities or on a whole square class. F1: the classical square-class obstruction to polynomial identities applies on the full moduli, not just mod 840. For explicit checks, `j=7,s=11` gives `p≡8 mod 19`, the growing-`k` family gives `9p≡−1 mod 83`, and the upper family gives `p≡7 mod 11`; each is nonsquare there. F2: no numerator-8 conclusion. F3: reciprocal identities survive integral composite substitutions, but the prime-slot necessity and Dirichlet assertions are prime statements. F4: no theorem about restricted (★), gstar or numerator-8 counts; no positivity of any of these counts is used.

Replay: `(ulimit -v 800000; timeout 90 uv run --no-project python scripts/z74_primitive_transfer.py)`.
