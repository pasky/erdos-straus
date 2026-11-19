# What can be kept when transferring a positive triple from Q to p?

**One replacement (PROVED).** Let `p` be an odd prime, `k,Q≥1`, `p∤kQ`, and `d=kQ−p>0`. Scale a donor ES triple for `Q` by `k`, keeping two entries. Replacing `ku` must give the unique value

`1/v=1/(ku)+4d/(pkQ)`, so `v=kp rQ/h`, where `h=pt+4dr`, `t=Q/g`, `r=u/g`, `g=gcd(Q,u)`.

If `p∤u`, then `gcd(h,r)=1` because `gcd(t,r)=1` and `p∤r`; also `p∤h` since `p∤4dr`. An integer `v` would force `h|kQ`, but `h≥p+4d>p+d=kQ`. Thus `p|u`. In fact some *other* donor entry must also be divisible by `p`: reduce the cleared donor identity modulo `p`, using `p∤Q`. The gate is necessary, not claimed sufficient.

**Polynomial donors (PROVED).** Fix positive `k,d`. No fixed triple of rational polynomials in `T=p` (equivalently in `Q=(T+d)/k`) can donate with just one replacement for infinitely many such primes, even allowing the replaced index to vary. Indeed the donor equation holds identically after clearing. On `T>−d` the region with all three polynomials positive is both open and closed: there each is at least `(T+d)/(4k)`, so no boundary point in that interval has a zero. It is nonempty, hence contains `T=0`. Each polynomial has nonzero constant term. Clearing their common coefficient denominator `M` gives integer polynomials `F_i`; for all but finitely many primes `p`, none of `F_i(p)≡F_i(0) mod p` vanish and `p∤M`, contradicting the gate. This also excludes a finite menu, not an unbounded collection of families.

**Two replacements (exact test).** Keeping `kx` instead requires that each of `(n,s)=(Q,x),(p,kx)` have a two-term residual. Reduce `(4s−n)/(ns)=a/b>0` to lowest terms. All unordered completions are given exactly by

`u | b², 1≤u≤b, u≡−b mod a;    y=(u+b)/a, z=(b²/u+b)/a`.

Indeed `(ay−b)(az−b)=b²`; conversely `u` is a unit mod `a` and the congruence supplies both divisibilities (at `a=1` they are automatic). For a least denominator `s` the **exact candidate interval** is `⌊n/4⌋+1≤s≤⌊3n/4⌋`; also require `s≤y` after completion. If both shared entries must be least, then `⌊Q/4⌋+1≤x≤⌊3p/(4k)⌋`, e.g. `53..157` and `263..787` for the two requested cases. If the shared term need not be least, enumerate sorted donors in the first interval and test **all three** donor entries, not just the smallest.

**A tied test for the least donor (PROVED).** Take the specific shift `k=12,d=11` and `Q≡3 mod 4`. Write `Q=4x−1`, so `p=48x−23`. The donor always has the triple `(x,2Qx,2Qx)`. The target with shared denominator `12x` has residual `23/b`, `b=12px`, with `23∤b` (a prime `p=48x−23` cannot equal 23). Its completion exists **iff some prime factor of x is a nonresidue mod 23**. To see this, the test is that a signed divisor `u/b` attain `−1 mod 23`, with each prime exponent ranging from `−v_q(b)` to `+v_q(b)`. Interchanging `u` and `b²/u` handles the size constraint. Since `p≡2x mod 23` and `2,3` are squares mod 23, absence of a nonresidue factor in `x` makes every ratio a square, unlike `−1`. Conversely take one nonsquare factor of `x`. The reserved factors `12=2²·3` have signed ratios covering **all** squares: `2` has order 11, `3=2^(−3) mod 23`, and `i−3j` with `|i|≤2, |j|≤1` covers `−5..5`. These exponents correct the chosen factor to `−1`. This conditional transfer is the target's mod-23 test with an automatic donor, not a consequence of `ES(Q)` alone.

**CERTIFIED full donor/target intersections**, `k=12,d=11`. The script enumerates actual integer pairs by the divisor bound, no size cutoff. The listed `x` can occur anywhere in the donor; every listed positive hit can in fact be least in both triples. No donor below has any entry divisible by `p`.

| `p` | `Q` | sorted donors | distinct slot values | all shared `x` |
|---:|---:|---:|---:|:---|
| 193 | 17 | 4 | 9 | none |
| 2521 | 211 | 30 | 63 | 53 |
| 3361 | 281 | 17 | 39 | none |
| 12601 | 1051 | 58 | 122 | 263, 264 |
| 31081 | 2591 | 192 | 386 | 649, 650, 660 |

At 2521 the shared 636 gives `(636,69748,131876031)`; at 12601, `(3156,1729488,7264426096)` and `(3168,562254,340078207392)` work. Here `53` and `263` are nonsquares mod 23. But `31081` is a **joint 11-miss in the hard class** (`Q=2591` prime, `R=3·9497`, both factors squares mod 11); its least possible donor `x=648=2³3⁴` fails the exact factor test. Other shared terms there do work. Conversely `3361≡1 mod 840` refutes unrestricted two-slot transfer even allowing every donor, but is not a joint 11-miss. `193` is a joint 11-miss (`Q=17`, `R=3·59`) with *no* shared term, but not in the hard class. These negatives do not settle whether **some** shared term always exists under both filters simultaneously.

Reproduce: `uv run --offline --no-project python scripts/shared_scaled_slot.py`.
