# Simultaneous direct and dual failure for every divisor shift

**Theorem (conditional only on Dickson's conjecture for linear forms).** Fix any positive multiple T of 210. There are infinitely many primes q with `p=4Tq+1` prime such that, for **every** `D|(p−1)/4`, neither `K=(p+c)/4` nor `pN`, `N=(cp+1)/4`, occurs in a positive ES triple at p, where `c=4D−1`. The direct assertion allows unrestricted remaining denominators, not just multiples of p. No eligibility assumption on c is made.

**Window criterion.** Removing `1/K` gives `c/H` with `H=pK`; removing `1/(pN)` gives `c/H` with `H=N`. A two-term completion yields `(cy−H)(cz−H)=H²`, both factors positive. For the first factor u, `u/H≡−1 mod c`; it is a signed product of the primes of H with exponents of absolute value ≤ their multiplicities in H. Here `(c,H)=1`: `c<p` and `(4,c)=1`. Thus it suffices to exclude −1 from these signed products. When H is displayed as a product of blocks, distribute each prime's signed exponent over its occurrences in the blocks; this works **without any coprimality between blocks**.

**The simultaneous progression.** Write `d|T`, `c_d=4d−1`, `t_d=T/d`. In an indeterminate Q use the following positive-leading forms:

```
K_d(Q)=TQ+d,       N_d(Q)=c_d TQ+d,       U_d(Q)=4TQ+1−t_d   (t_d>1).
```

The last family is for the *large* dual shifts. Put `b=2+3τ(T)`, an upper bound for the number of forms including Q and `4TQ+1`. Let S consist of the primes ≤b and all primes dividing `T`, any `c_d`, or any **nonzero** `t_d−1`. Choose a positive k and set

```
m=1+2Tk,       Q₀=k+Tk²,       p₀=4TQ₀+1=m².
```

We may make Q₀ arbitrarily large with `gcd(Q₀p₀,∏_{ℓ∈S}ℓ)=1`. At `ℓ|T` take `k≡1 mod ℓ`: `Q₀≡1`, `m≡1`. At every remaining ℓ in S, `2T` is invertible and `ℓ>3`; choose `m≠0,±1 mod ℓ` and translate to k. Use CRT. Choose Q₀ so all U-values are positive.

For **each** form F from the displayed list put `a_F=F(Q₀)>0`. One has `gcd(a_F,Q₀p₀)=1`. Indeed modulo Q₀ the two fixed-shift values reduce to d, and the U-value to `1−t_d`; their prime divisors in common with Q₀ have been excluded. Modulo primes of p₀ use `4K_d=p₀+c_d`, `4N_d=c_d p₀+1`, `U_d=p₀−t_d` at the seed. All possible common primes have again been excluded. The omitted `t_d=1` form is exactly `4TQ`, which must **not** be normalized this way.

Take M a common multiple of all `a_F`, all `a_F c_d` for `F=K_d,N_d`, all `c_d`, and all primes in S, with **no further prime divisors** (e.g. the lcm). Then `(M,Q₀p₀)=1`. Substitute `Q=Q₀+Mn`. With `s_F` the slope of F,

```
F(Q)=a_F L_F(n),             L_F(n)=1+(s_F M/a_F)n.
```

All normalized forms are integral and positive-leading. For the two fixed-shift forms `L_F≡1 mod c_d`. Impose primality on Q, `4TQ+1`, and the `L_F`. Proportional normalized forms are identical (all have constant 1), so remove duplicates. None of the original F's is proportional to Q or `4TQ+1`: for the fixed-shift forms compare their nonzero values at `Q=0,−1/(4T)`, and for U use `t_d>1`. The latter two required forms are themselves nonproportional. Admissibility holds at **every** prime ℓ. At `ℓ|M`, the single choice `n=0` makes every required form a unit, even if a normalized slope is a unit and not a multiple of ℓ. At `ℓ∤M` there are at most b forbidden residues, since the normalized forms have constant 1 and the two other forms cannot vanish identically (their slopes are units since `ℓ∤4TM`). Here `ℓ>b`. This deals also with possible nonprimitive coefficients before normalization; there is no remaining fixed prime divisor. Dickson gives unbounded primes `q=Q(n),p=4Tq+1` with all these cofactors prime. Take `q>T`. The divisors of Tq are exactly `d,dq` for `d|T`.

**Fixed D=d.** The seeds `K_d(Q₀)=(m²+c_d)/4` and `N_d(Q₀)=(c_dm²+1)/4` have every prime factor of Jacobi symbol `+1` modulo `c_d`. For an odd prime r dividing either, `−c_d` is respectively `m²` or `m⁻²` mod r, a unit square (`(m,c_d)=1`). By reciprocity `(r/c_d)=(−c_d/r)=1`. If 2 divides either seed, odd `m²≡1 mod 8` gives `c_d≡7 mod 8` and `(2/c_d)=1`. The cofactor primes `L_F≡1 mod c_d` also have symbol +1. Finally p **as one prime atom** has symbol +1 since `p≡m² mod c_d` and `(m,c_d)=1`. Thus every signed product for `pK_d` and for `N_d` has symbol +1, unlike `−1` since `c_d≡3 mod 4`. In particular at `c_d=3` all prime factors of both windows are forced to be 1 mod 3; no general ES obstruction for an actual composite square input is assumed.

**Growing D=dq.** Put `c=4dq−1, t=T/d`. Modulo c one has `q≡(4d)⁻¹` and `p=4Tq+1≡t+1`. For the direct window, `H=p(T+d)q`. Its signed products therefore come from a finite list of **positive rationals independent of q**: replace q by `1/(4d)` and p by `t+1`, and keep the prime occurrences of the fixed `T+d`. This replacement respects reduction modulo c; the original factors are units there. For each reduced rational `A/B>0` on the list, reduction to −1 requires `c|A+B`, impossible for sufficiently large q.

For the dual window the exact factorization and congruence are

```
N=(cp+1)/4=dq(p−t),                 p−t=tc+1.
```

If `t>1`, we have `p−t=a_U L_U` with `a_U=U_d(Q₀)` fixed and `L_U` prime. Both are units mod c and `L_U≡a_U⁻¹ mod c`. Replace q by `1/(4d)`, this **one prime atom** `L_U` by `1/a_U`, and keep all prime occurrences of `d a_U`. Again every signed product comes from a finite list of positive rationals, so none reduces to −1 once c exceeds the largest numerator-plus-denominator. If `t=1`, then `N=dq(4Tq)=4Td q²`, and only the fixed primes of `4Td` and two copies of q occur. The same substitution works directly. All substitutions permit negative exponents because every represented factor and denominator is a unit mod c. There are finitely many d, so a single lower bound on q suffices for all of them. This proves the simultaneous assertion. ∎
