# Unit R, phase 2: blind parallel construction

## Blindness attestation and read log

This file was written in clone `/tmp/es-unitR14` at base
`c489912bc704abb17af44c19ee830a3cb7421140`.  Before this file's first commit I
read only the task brief, `notes.md` lines 2715--3239 (all of §16), and
`notes.md` lines 10741--11303 (all of §34).  I located those ranges by matching
section headings.  I did not open §39 or its source range, nor inspect
`verify.py` block `(al)`.  The mandatory baseline run printed block `(al)`'s
one-line results, but I did not read its implementation.  The baseline was
green.

This is an independent derivation from Lemmas 16.1--16.3, Theorems 16.4--16.5,
Lemma 34.7, Theorem 34.8, and the seven statement skeletons in the brief.
Constants below may depend on the fixed `kappa`, but not on `X,k,g,a,c,y` in
the displayed ranges.

Put `t=log X`.  Dyadic blocks are disjoint, and there are `O(t)` of them.
The harmless endpoint conventions do not affect any estimate.

## S1: forced classes and the fibre coupling

Let `A=(k,ell,u,v)` be an atom and put

    w=(k ell+1)/(4uv).

This is a positive integer.  The hypotheses give `(v,k ell)=1`: it is assumed
for `k`, and every divisor of `(k ell+1)/4` is prime to `ell`.  If `n` hits
`E_A`, then `nv == -u (mod k ell)`.  Lemma 16.1, with the factorization
`(k ell+1)/4=uvw`, gives a three-unit-fraction representation of `4/n`.
Therefore every exceptional `n` avoids every atom event.

If `c == n (mod 24 L_K)`, then in particular `c == n (mod k)`.  A hit gives
`nv+u == 0 (mod k)`, hence

    k | u+cv.

This proves S1.

## S2: distinct prime coordinates and exact intersections

Fix `ell` and suppose two atoms give the same class modulo `ell`.  Then
`ell | uv'-u'v`.  In their common dyadic block, `u,v,u',v' <= x^(1/6)`, so

    |uv'-u'v| < 2 x^(1/3) < ell

for all sufficiently large blocks (the factor 2 is harmless; the sharper
one-sided comparison follows by bounding each product by `x^(1/3)`).  Thus
the difference is zero.  Reducedness `(u,v)=(u',v')=1` gives the same ordered
pair `(u,v)=(u',v')`.

If their multipliers differ, the common `uv` divides both
`(k ell+1)/4` and `(k' ell+1)/4`, hence divides `(k-k')/4`; but
`uv>H^2>K>|k-k'|/4`, a contradiction.  Thus `k=k'`, and the atoms are equal.
Consequently all atom classes at a fixed `ell` are distinct.

Two distinct compatible events therefore cannot have the same `ell`: their
reductions modulo that prime would have to agree.  For a compatible ordered
set, the `ell_i` are distinct, exceed `K`, and divide none of the `k_i`.
Its lcm is

    lcm(k_1,...,k_j) product_i ell_i.

CRT gives one residue modulo this lcm, so its probability in the uniform CRT
space is its reciprocal.  This proves S2.

## S3: residue-resolved and total mass

### An independent residue-resolved box bound

I use Shiu's theorem, but organize the residue condition through reduced
classes modulo `k`, rather than by inserting a divisor expansion.  Let
`g|k`, `(a,g)=1`, and let `I=(U,(1+eta)U]`, `J=(V,(1+eta)V]`, with fixed
`eta>0` and `U,V>H=K^10`.  Set `F(n)=n/phi(n)`.  Dropping only `(u,v)=1`
(which is legitimate for an upper bound), the desired weighted box sum is,
up to an `eta`-constant,

    (UV)^(-1) sum F(u)F(v),

where `(uv,k)=1` and `u == -av (mod g)`.

For each reduced `v mod k`, the allowed `u` occupy exactly `phi(k)/phi(g)`
reduced classes modulo `k`: reduction `(Z/kZ)^* -> (Z/gZ)^*` is surjective
and all fibres have that size.  Shiu on each such class gives

    sum_{u in I, u == -av (g), (u,k)=1} F(u)
      << U/[phi(g) log U]
         exp(sum_{p<=2U,p not| k} 1/(p-1)).                 (R.1)

Summing Shiu over all reduced classes for `v` gives

    sum_{v in J,(v,k)=1} F(v)
      << V/log V exp(sum_{p<=2V,p not| k} 1/(p-1)).          (R.2)

The modulus hypothesis is uniform in the whole power range because
`k<=K<U^(1/10),V^(1/10)`.  Mertens and

    exp(-1/(p-1)) <= 1-1/p

show that (R.1)--(R.2), after division by `UV`, are at most

    C/phi(g) product_{p|k}(1-1/p)^2
      = C phi(k)^2/[phi(g)k^2].                              (R.3)

The constant is absolute for fixed `eta` and uniform for every `k<=X^kappa`,
`g|k`, and reduced `a`; in particular, no `tau(k)` or hidden
`log log k` factor occurs.  Summing the `O(t)^2` geometric box pairs gives

    sum_{H<u,v<=z, (uv,k)=1, u+av == 0 (g)} 1/[phi(u)phi(v)]
      << t^2 phi(k)^2/[phi(g)k^2].                           (R.4)

Retaining `(u,v)=1` and the low-omega cutoff only decreases this upper bound.
This is the danger-zone D-a estimate.

### From boxes to atom masses

For fixed `(k,u,v)` in a block, the primes lie in
`ell == -k^(-1) (mod 4uv)`, and `4uv<=4x^(1/3)`.  Brun--Titchmarsh gives

    sum_{x<ell<=2x, progression} 1/ell
      << 1/[phi(4uv) log x]
      << 1/[phi(u)phi(v)t].                                  (R.5)

The atom class modulo `g` is `a` exactly when `u+av == 0 (mod g)`.
Equations (R.4)--(R.5), the outside factor `1/k`, and `O(t)` blocks yield

    W_{k,a}(g) << t^2 phi(k)^2/[phi(g)k^3].                  (R.6)

For total mass at fixed `k`, the unconditioned box density is
`asymp (phi(k)/k)^2`: Mobius inversion for `(u,v)=1` contributes
`product_{p not|k}(1-p^-2)`, bounded above and below absolutely.  The same
fixed-function Rankin argument as Lemma 16.2 removes the high-omega tail.
For this one fixed `k`, progression multiplicity at a modulus is at most
`2^omega(uv)=(log X)^O(1)`, independently of the power-sized number of
multipliers.  Ordinary Bombieri--Vinogradov therefore turns the box main
term into actual prime mass.  Together with (R.5), this proves

    W_k asymp t^2 phi(k)^2/k^3,                              (R.7)

uniformly in `k<=K`.  This argument does not use the maximum multiplicity
over all multipliers.

Finally, §16 gives
`sum_{k<=K,k=1(4)} phi(k)/k^2 asymp log K`.  Weighted Cauchy and
`sum_{k<=K,k=1(4)}1/k asymp log K` imply

    sum_{k<=K,k=1(4)} phi(k)^2/k^3 asymp log K.

Since `log K asymp t`, (R.7) gives `mu_X asymp t^3`.  This proves S3.

## S4: conditioned factorial moments

Let a compatible ordered set of previous atoms fix a reduced residue modulo

    L=lcm(k_1,...,k_j)

on the multiplier coordinates.  Its prime coordinates are distinct.  Take
a new atom `A=(k,ell,u,v)`, with `ell` new, and write
`p^e || k`, `p^f || L`.  Conditional on the previous events and on
`(n,P_y)=1`, its exact local cost at `p` is

    f>=e:                  1,
    0<f<e:                 p^(-(e-f)),
    f=0 and p<=y:          1/phi(p^e),
    f=0 and p>y:           p^(-e),                             (R.8)

provided the prescribed residues agree modulo `p^min(e,f)`; otherwise the
cost is zero.  The first two lines explicitly include unequal prime-power
exponents.  The new `ell` costs `1/ell`, since `ell>y`, is absent from all
previous multipliers, and is a new prime coordinate.

Put `g=(k,L)`.  Multiplying (R.8) by `k` shows that the conditional
probability is

    C(k,L;y)/(k ell),
    C(k,L;y)=g product_{p|k, p not|L, p<=y} p/(p-1),          (R.9)

when the atom class agrees with the old reduced class modulo `g`.
Thus S3 bounds the sum of conditional probabilities of all possible new
atoms at this fixed `k` by

    Ct^2 C(k,L;y) phi(k)^2/[phi(g)k^3].                      (R.10)

Here is the collapse-versus-consistency cancellation prime by prime.  Apart
from `1/k`, a prime dividing `k` contributes

    p|L:                  (1-1/p),
    p not|L and p<=y:     (1-1/p),
    p not|L and p>y:      (1-1/p)^2.                         (R.11)

Indeed `g/phi(g)` cancels exactly one of the two totient factors on collapsed
coordinates, while rough conditioning cancels one on a new small-prime
coordinate.  Every factor in (R.11) is at most one.  Therefore the final
Euler/harmonic bound is simply

    sum_{k<=K,k=1(4)} C(k,L;y)phi(k)^2/[phi(g)k^3]
      <= sum_{k<=K}1/k << log K << t.                        (R.12)

The estimate is uniform in `L`, all exponent patterns, and `y`.  Starting
with the empty set and adjoining atoms successively, incompatible tuples
contribute zero and (R.10)--(R.12) give at most `Ct^3` for each next atom.
Repeated atoms are excluded in the falling factorial, and S2 excludes a
repeated prime coordinate.  Hence

    E((H_X)_m | (n,P_y)=1) <= (Ct^3)^m

for every `m>=1`.  This proves S4 and addresses D-b.

## S5: void probability by multiplier fibres

Direct Janson is not useful here: atoms sharing multiplier coordinates
produce a dependency sum of the same quadratic order as the square of the
mass.  Instead condition further on

    c=n (mod 24L_K).

For a rough fibre define

    J(c)={k<=K:k=1 (4), (k,c)=1},
    h(c)=sum_{k in J(c)} phi(k)/k^2.

It contains 1, and `c` is reduced modulo `24L_{J(c)}`.  In this fibre, the
atoms satisfying `k|u+cv` have their multiplier coordinate automatically
met.  At a fixed `ell` their remaining classes are distinct by S2, and the
coordinates for distinct `ell` are independent.  Theorem 34.8 supplies a
low-congestion subfamily, contained in the present atom family, whose mass is
`>=c t^2h(c)`.  Therefore, fibrewise,

    Pr(H_X=0 | rough,c) <= exp(-c t^2 h(c)).                 (R.13)

It remains to average fibres without discarding a merely polynomial bad set.
Put `w_k=phi(k)/k^2`, `h_0=sum_k w_k asymp log K`, and

    A_p=sum_{k<=K,k=1(4),p|k}w_k << (log K)/p.

The union bound inside the exponent gives

    h(c)>=h_0-sum_{p|c,p>y} A_p.                             (R.14)

Under rough conditioning, the indicators `1_{p|c}`, `y<p<=K`, are independent
and have means `1/p`.  With `lambda=ct^2`, choose `y=Bt^3`, with fixed `B`
large enough that `lambda A_p=O(t^3/p)` is uniformly small.  Then

    E exp(lambda sum_{p|c,p>y}A_p)
      = product_{y<p<=K}[1+(exp(lambda A_p)-1)/p]
      <= exp(C lambda log K sum_{p>y}p^-2)=O(1).             (R.15)

Combining (R.13)--(R.15) and `log K asymp t` gives

    Pr(H_X=0 | (n,P_y)=1) <= exp(-ct^3).

This proves S5 by a fibre route, including the exponentially strong averaging
which a Markov estimate would miss.  This is D-c.

## S6: Bonferroni majorant and the complete ledger

For even `r`,

    Q_r(h)=sum_{j<=r}(-1)^j C(h,j)
          =1                    if h=0,
           C(h-1,r)             if h>=1.

Thus `Q_r(h)>=1_{h=0}`.  By S1, an exceptional prime larger than
`max(K,y)` is rough and has `H_X=0`, so

    nu_X=1_rough Q_r(H_X)

is pointwise at least one there.

Moreover `C(h-1,r)<=C(h,r+1)`.  S4 and S5 give

    E(Q_r(H_X)|rough)
      <= e^(-ct^3)+(Ct^3)^(r+1)/(r+1)!.

Taking the least even `r>=D_Bt^3`, with `D_B` sufficiently large, makes the
second term `e^(-c't^3)` by Stirling.  Hence `E_CRT nu_X<=e^(-c't^3)`.

For the ledger, expand the rough indicator over divisors of `P_y`, and expand
each binomial moment as a sum over unordered atom sets of size at most `r`.
Incompatible congruences are zero; every compatible term is one residue
class modulo the relevant lcm.

* Degree: `r+pi(y)=O(t^3)`.
* Atom inventory: even the crude bound
  `M<=K X z^2 O(t)=exp(O(t))` gives `log M=O(t)`.
* Number/coefficient sum:

      2^pi(y) sum_{j<=r} C(M,j) <= exp(O(t^3)+O(r log M))
                                = exp(O(t^4)).

  Combining identical terms can only decrease this `l1` bound.
* Modulus: `log d<=theta(y)=O(t^3)` for the rough divisor, while each of at
  most `r` atom moduli has logarithm `O(t)`; hence `log d=O(t^4)`.
* Rounding: on `[1,N]`, each residue class contributes `N/d+O(1)` exactly.
  Summing the `O(1)` errors with the coefficient `l1` norm gives

      sum_{n<=N}nu_X(n)
        <= N E_CRT nu_X + exp(C_1t^4).

If `log N>=C_0t^4`, with `C_0>C_1` fixed sufficiently large, the last term is
absorbed into `N exp(-c''t^3)`.  The omitted primes at most `max(K,y)` are
also absorbed.  This proves S6 and supplies D-d's arithmetic.

## S7: optimization and semigroup transfer

Let `L=log N` and choose `t=alpha L^(1/4)`, with fixed `alpha` small enough
that `L>=C_0t^4`.  S6 gives for prime denominators

    E(N) << N exp(-c t^3)
         << N exp(-c' L^(3/4)).

For completeness, the all-denominator transfer is not just formal.  Every
prime factor of an exceptional integer is exceptional (scale a
representation by `n/p`).  Rankin's bound for that semigroup, with
`delta=eta L^(-1/4)`, is

    E_all(e^L) <= e^{(1-delta)L}
       product_{p<=e^L,p exceptional}(1-p^{-1+delta})^{-1}.

Partial summation of the prime bound is uniform because, for `u<=L`,
`delta u<=eta u^(3/4)`.  Choosing `eta` below the prime-saving constant makes
`integral exp(-(c-eta)u^(3/4))du` finite; prime-power terms are bounded as in
Theorem 16.5.  The Euler product is therefore `O(1)`, proving

    E_all(N) << N exp(-c(log N)^(3/4)).

This proves S7.

## Blind-phase verdict

I obtained complete derivations of S1--S7 from the allowed inputs.  The two
places where the skeleton alone concealed necessary quantitative work were:
(1) the exact `phi(k)^2/[phi(g)k^2]` residue-box density in (R.3), and
(2) the exponential-moment averaging of rough multiplier fibres in
(R.14)--(R.15).  I have not yet compared either step with §39.  This verdict
is only a phase-2 derivability result, not an upgrade of any claimed or
provisional theorem.
