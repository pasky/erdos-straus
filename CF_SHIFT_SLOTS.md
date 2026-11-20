# Principal continued-fraction shifts tested as actual denominators

```
Result: the CF-shift menu first misses at p=176401=420²+1 (79th prime 1 mod 840), even expanded; for period one the dual at 3 always fails and the direct works iff (m/2)²+1 has a prime 5 mod 12; exact full-split test for c=4Q_i−1.
Label: CERTIFIED (176401; the 78 smaller hits) | PROVED (period-one criterion, support obstruction, full-split test) | CONDITIONAL on Schinzel H (infinitely many period-one misses)
Scope: the specified CF menu only; 176401 satisfies ES. ES is OPEN.
Review: cross-model, data/z74/xreview/REVIEW_SHIFTS_OPUS.md (ACCEPT-WITH-FIXES; no gap) (z74 Opus xreview fix)
Triage: METHOD-CX
STATUS delta: none
```

**CERTIFIED least miss:** `p=176401=420²+1`, the 79th prime `1 mod 840`. Use the initial state and one complete period of `√p` as in `Z52D_PELLCYCLE.md` (S expansion only). For each complete denominator `Q` take the largest odd part of each positive `Q,Q−1,Q+1,4Q−1`; retain `c≡3 mod 4` prime to `p`, necessary for the two slots to be integral. **No sign, root, or prime-shift filter.** Here the only periodic state is `(P,Q,a)=(420,1,840)`, and the menu is `{3}`. Even expanding the rule to use `aQ` and `a` in place of `Q` gives only `{3,419,839,1679,3359}` and all five miss. The smaller 78 primes each have a certified hit on the narrower menu. This is not a forest test: that earlier experiment asked whether a *component meeting a root* contained a bichromatic edge, not whether a specified ES denominator completed.

**Exact test.** At `s=K=(p+c)/4` the residual is `c/H` with `H=pK`, and at `s=pN`, `N=(pc+1)/4`, it is `c/H` with `H=N`. In either case `gcd(c,H)=1`; a hit is equivalent to `t|H²`, `t≤H`, `t≡−H mod c`, since `(cy−H)(cz−H)=H²`. Replay checks `4syz=p(sy+sz+yz)` for each returned hit. This tests unrestricted direct completion, not just Type II. At the first miss `K=44101` prime, `N=13·10177`, all factors `1 mod 3` including `p`.

**Exact period-one criterion (PROVED).** For `p=m²+1≡1 mod 840` prime, `420|m` and `Q=1` throughout. The dual at 3 *always* fails: `N=3(m/2)²+1` is odd, prime to 3, and every prime `r|N` satisfies `(-3/r)=1`, hence `r≡1 mod 3`. The direct slot works **iff** `(m/2)²+1` has a prime divisor `5 mod 12`: all its prime divisors are `1 mod 4`, and the signed products from `pK` hit `−1 mod 3` iff there is a `2 mod 3` factor. Thus the short-period failure isn't an artifact of stopping a CF search early. Conditional on Schinzel H it occurs infinitely often for the narrow menu: take both `p=(420t)²+1` and `K=(210t)²+1` prime (distinct irreducible quadratics, admissible at `t=0`).

**Raw support obstruction (PROVED; overlap with known CT).** For an odd prime `r|Q_i` the identity `p=P_i²+Q_{i−1}Q_i` gives `(p/r)=1` (if `r|P_i` it would divide `p`, impossible since `Q_i<2√p<p` on the reduced cycle). Hence `(r/p)=1`, and also `(2/p)=1`. This applies even to a nonprincipal form denominator satisfying the same unit-square congruence. In particular **every prime factor**, not just the product or the full `Q_i`, is positive. `POINTWISE_SIZE.md` §2, Lemma CT(a), already says that *each* `p`-free denominator of any positive prime solution must have a negative prime factor; `HARDNESS_MAP.md` A2 also gives `(AB/p)=−1` for normalized Type II. Taking arbitrary subsets, powers, or products from any number of the `Q_i` supports cannot supply such a denominator or `AB`. Odd-part shifts dividing `Q_i` also cannot be root-eligible when `3 mod 4`: `p` is already a unit square there. This last remark alone is **not** a no-sign slot obstruction.

**Additive repair with an exact complement test (PROVED).** For the distinct choice `c=4Q_i−1`, the actual first slot is `K=(p−1)/4+Q_i`. Even modulo **this c** each odd `r|Q_i` has Jacobi `(r/c)=(−c/r)=1`; at 2, `2|Q_i` gives `c≡7 mod 8`. There is no negative anchor among those primes in either sense. Instead take any positive `r|gcd(Q_i,(p−1)/4)`, retain it in the factorization of `K`, and take the **whole complementary divisor** `b=K/r`. The split works iff `c|r+b`, equivalently

```
16r² + 4P_i² + Q_{i−1} ≡ 0 mod c.
```

Indeed `r` is a unit mod `c`, so `r²+K≡0` is the test; use `4K=p+c` and `4p≡4P_i²+Q_{i−1}`. It supplies the actual unit root `2r` of `−p` modulo `c`. With `g=gcd(r,b)`, take `A=r/g,B=b/g,D=g²,E=(A+B)/c` (integral since `g` is a unit mod `c`). The triple is `(K,pADE,pBDE)`. Here **the complementary divisor `b` itself has `(b/p)=−1`**: `K≡c/4 mod p` gives `(K/p)=(p/c)=−1` by the unit root, and `(r/p)=1` by CF support. Thus some prime in `b` lies outside *all* CF denominator supports. This is sharp only for the specified full split; it is not necessary for an unrestricted hit.

|p|i; `P_i,Q_i,Q_prev`|`r,b`|negative prime in b|actual triple|
|---:|---|---|---:|---|
|7561|64; 82,27,31|3,639|71|1917,136098,28988874|
|12601|15; 111,8,35|2,1579|1579|3158,1285302,1014745929|

**First-step control.** At `m=⌊√p⌋`, `c=4Q₁−1`, `4p≡4m²+1 mod c`. Eligibility is local at *each* prime of `c`: e.g. `p=3361` gives `c=447` with `−p` nonsquare mod 3. A sufficient positive relation is `c|4m²+5`, equivalent to `c|p+1`: then `v=K(p+1)/c` gives the original triple `(K,v,pv)`. At identical first `Q₁=57,c=227`, `p=12601` misses both slots, whereas `p=1317961` meets this criterion (`m=1148`) and hits direct. These are applications of ordinary fixed-slot identities to CF-selected rows, not proofs that the period forces a good additive shift.

Replay: `(ulimit -v 800000; timeout 45 uv run --offline --no-project python scripts/cf_shift_slots.py)`. No statement about ordinary squares, numerator 8, composite inputs or the restricted (★)/gstar counts follows from this prime-slot test.
