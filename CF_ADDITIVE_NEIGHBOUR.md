# Adjacent complete denominators: an additive escape, not a factor transfer

**Positive rule (proved).** Take an ordinary continued-fraction row of `√p`, with `r=Q_{i−1}, q=Q_i, P=P_i`, so `p=P²+rq`. For `h=±1` put `A=q+h>0`, `f=4A−1`. The **exact** test for this A with `D=E=1` is

```
f | 4P²+(1−4h)(r+1)+4h .
```

Indeed the right side is `4(p+A)` modulo f by `4q≡1−4h`. Thus `B=(p+A)/f` is a positive integer exactly when the test passes. It gives `p=4AB−A−B` and the full positive triple `(AB,pA,pB)` since multiplying its reciprocal sum by `pAB` gives `p+A+B=4AB`. No sign-only or forest hit is substituted for the divisibility. At `p=20161≡1 mod 840` row 101 is `(P,r,q)=(81,85,160)`; take `h=−1`. This yields `(A,B)=(159,32)` and the triple `(5088,3205599,645152)`. The new factor `53|159` is a nonresidue at p (equivalently use `(32/p)=(3/p)=1` and the Type-II pair sign). The old factors of 160 and 85 cannot do this.

**Force the rule, not just a successful test.** Here is an unbounded family on which the additive neighbour and the CF row both have predetermined roles. For every nonnegative `j` put

```
s=84+137·3360·13j,   f=(2s²−1)/137,   m=120f+s,
q=(f−3)/4,           n=m²+q,           A=q+1.
```

At `j=0`, `f=103`; along the progression it stays an integer `≡103 mod (3360·13)`. Thus `q≡25 mod (840·13)` and `n≡154853161 mod (840·13)`, in particular `n≡1 mod 840`. As `0<q<2m+1`, `m=⌊√n⌋` and **the actual first complete denominator is q**. Now `f=4A−1` divides `2m²−1` by construction, hence `4n+1=4m²+f−2` and `4(n+A)=(4n+1)+f` are divisible by f. Since f is odd, `B=(n+A)/f` completes the identity above for every j. The neighbour `A` grows and contains the fixed prime 13, which is genuinely negative at **every prime instance**: `n≡8 mod 13` is a nonsquare there. At `j=0`, `n=154853161` is prime, `A=26, B=1503429`. This is an unconditional family of integers, with a certified ordinary prime seed, **not** an infinitude claim for prime values of a quartic. The certificate is the classical Type-II identity; the extra content is forcing its divisor directly from `Q₁+1` on a family where `Q₁` itself has only positive prime factors at prime inputs.

**Why transfer fails (proved).** For primes `p≡1 mod 8`, every odd prime `l` dividing a primitive nonzero norm `|u²−pv²|`, `gcd(u,v)=1`, `p∤u`, has `l∤uvp` and `(l/p)=(p/l)=1`, since `p≡(u/v)² mod l`. The prime 2 also has positive symbol. In particular for `Q_i|p−P_i²` with `0<P_i<√p`, **every prime factor** has positive symbol, not merely their product. This argument applies to any reduced cycle furnishing that same divisibility (exclude ramified factors if allowing nonreduced, arbitrary starting data). Products, arbitrary powers, divisors, and pooling across cycles cannot introduce a negative prime. By CT / `HARDNESS_MAP.md` A3 none can be the *entire support* of any p-free denominator. By A2 neither normalized pair product can have such support, regardless of D,E. This does not prohibit a Q-factor appearing alongside an outside nonresidue. For the opposite norm `u²+pv²` the formula for odd divisors is instead `(l/p)=(−1/l)`; a `3 mod 4` factor gives negative sign, but its existence and the full ES divisibility are not automatic.

**Raw size audit.** With `A=q,B=r,D≥1` the exact necessary and sufficient arithmetic test for the displayed normalization `p=4ABD−(A+B)/E` is `δ=4Drq−p>0` and `δ|(r+q)` (then `E=(r+q)/δ`). For the full identity the denominators are `(ABD,pADE,pBDE)`. In a reduced row, both q and its complementary r lie strictly between `√p−P` and `√p+P`: the complete quotient exceeds 1 and its conjugate lies in `(−1,0)`, then use `rq=(√p−P)(√p+P)`. Hence `(q−(√p−P))(q−(√p+P))<0` gives `q+r<2√p`. In particular

```
0 < δ=(4D−1)p−4DP² ≤ q+r < 2√p.
```

For `D=1`, `sqrt((3p−2√p)/4)<P<√(3p/4)`. Even passing the size test is not enough: at `p=1201`, `(P,r,q)=(30,43,7)`, `δ=3≤50` but `3∤50`. At `p=m²+1` the principal period has `q=r=1`; the size bound already fails at D=1 for `p>4`. Independently, `(qr/p)=(−P²/p)=1` for *all* `p≡1 mod 4`, before or after removing a common square; A2 excludes the raw pair for both types. If a putative nonprimitive Type-II identity is considered, normalizing by `g=gcd(A,B)` replaces `(A,B,D,E)` by `(A/g,B/g,Dg²,E/g)` when `g|E`; even without assuming that divisibility, its two p-scaled denominators have product `AB(DE)²`, so the same pair-character obstruction applies whenever p divides neither A,B,D,E. In the raw case `D,E<p` follows from the exact test and `q+r<2√p` for `p≥5` (`4Dqr≤p+q+r`).

**Overlap.** `Z52D_PELLCYCLE.md` Prop. 2.4 already uses `p` square modulo reduced denominators; the factor-sign observation above is its elementary reciprocity consequence combined with CT, not a new statement about distribution of cycle roots. That note's conditional forest obstruction concerns components seeded by the cycle, not this shifted-denominator certificate. The successful identity makes no pointwise claim for all primes. No forest or transfer scan is used for its proof.
