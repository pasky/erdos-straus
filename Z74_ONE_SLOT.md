# When can a smaller ES triple be scaled and repaired in one slot?

```
Result: when p=kQ−d, d>0, p∤kQ, a one-slot repair of a k-scaled 4/Q donor is possible only if p already divides the changed slot and exactly one other slot (p>Q); hence no fixed polynomial donor works.
Label: PROVED (gate, polynomial no-go) | CERTIFIED (k=3 census; no one-slot transfer at the three joint 11-misses up to 5·10^4)
Scope: one specified induction rule (lower direction d>0); says nothing about other ES solutions at p. ES is OPEN.
Review: cross-model, data/z74/xreview/REVIEW_SHIFTS_OPUS.md (ACCEPT-WITH-FIXES; no gap) (z74 Opus xreview fix)
Triage: BARRIER-SCOPED
STATUS delta: none
```

**PROVED (directional obstruction).** Let `p` be an odd prime, `Q,k` positive, `p∤kQ`, and `d=kQ−p>0`. Take an arbitrary positive solution `(x,y,u)` to `4/Q`. Scale all three denominators by `k` and keep `kx,ky` fixed. If changing only `ku` to a positive integer `v` gives `4/p`, then **p already divides the donor denominator u**. In fact `p` also divides at least one of the other two donor denominators. This is about a specified induction rule, not about arbitrary solutions for `p`.

Indeed, subtraction fixes `1/v=1/(ku)+4d/(kpQ)`. Put `g=gcd(Q,u)`, `t=Q/g`, `r=u/g`. Then

```
v = kpQr / (pt+4dr).
```

If `p∤u`, the positive denominator `h=pt+4dr` is coprime to both `p` and `r`: use `p∤4d`, `gcd(t,r)=1`. Integrality implies `h|kQ`. But `h≥p+4d>p+d=kQ`. This contradiction uses the direction of the correction. Next reduce the donor equation `4xyu=Q(xy+xu+yu)` modulo `p`; since `p|u` and `p∤Q`, `p|xy`. Not all three donor denominators are divisible by `p` if `p>Q`: they would each be ≥p, giving `4/Q≤3/p`. Thus in that case precisely two donor slots already contain the prime one wanted to introduce.

**Consequence (no fixed polynomial donor).** At fixed `k,d>0`, no fixed triple of positive rational-polynomial formulas in `p` for `4/Q` (`Q=(p+d)/k`) can supply one-slot repairs at infinitely many primes. Indeed `p|u(p)` on an infinite set forces `u(0)=0` by clearing a constant coefficient denominator. But over the real interval `[0,∞)` each of the three polynomials is everywhere positive: they are eventually positive, and on their common positive component the identity bounds each below by `(p+d)/(4k)>0`, so the component has no finite endpoint there. In particular `u(0)>0`. The same argument applies to a finite menu; an adaptive factorization or a truly nonpolynomial donor is not ruled out. This does not use any assumption that the target class contains squares.

**Exhaustive arithmetic test.** To search for a donor without any cutoff on denominators, put `A=pQ`. A successful `u` must satisfy `h=A+4du | kA²` (multiply `h | kuA` by `4d` and subtract a multiple of `h`). For each positive divisor of `kA²` with `u=(h−A)/(4d)` positive integral, test `h|kuA` itself; the multiplied condition alone is not sufficient. Reduce `4/Q−1/u=c/b` to lowest terms. Its two positive unit fractions correspond exactly to divisors `t | b²`, `t≤b`, `t≡−b mod c`, via `(cx−b)(cy−b)=b²`.

There is an independent donor-first check for `p>Q`. Let `x` be the unique donor denominator prime to `p`. Since the other two are ≥p, one necessarily has

```
Q/4 < x ≤ pQ/(4p−2Q).
```

For each such `x`, splitting the reduced residual `p(4x−Q)/(Qx)=1/a+1/b` gives exactly the donors `(x,pa,pb)`. Try replacing each of `kpa,kpb` in turn. This is much less work than enumerating all triples for `Q` at large inputs; it still tests all possible one-slot transfers in this direction.

`uv run --offline --no-project python scripts/z74_single_retune.py` (z74 Opus xreview fix: was `uv run --no-sync`) checks the two enumerations against each other for 1,078 pairs (`2≤Q≤71`, `Q<p<3Q`, `k=3`, prime to `4kQ`), with five positive pairs. For instance the donor `(5,46,2070)` gives `4/18`; scaling by 3 and replacing `6210` by `10` gives `(15,138,10)` for `4/23`. So the prime-divisibility obstruction does not assert impossibility.

**At shift 11.** Set `k=12,d=11` as in `SIGNED_TWO_SHIFTS.md`. On primes `1 mod 840` up to 50,000 that fail both tests at eligible 11, the exhaustive donor-first search finds **no** one-slot transfer: the full list is `(p,Q)=(2521,211),(12601,1051),(31081,2591)`. Other methods do solve these primes. The first two terms of a donor are not free simply because the donor is known to exist, and `p∤ku` does not become `p|v` by a positive reciprocal correction in this setting.
