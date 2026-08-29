# Blind general-m construction (wave 16, frozen before comparison)

> **Blindness attestation.** This derivation was made without reading `notes.md`
> §43, any `reviews/` file mentioning sec43, any `UNIT_REPORT*.md`, the
> `PROJECT.md` Outcome 19 block, or `paper/`.  This is a self-attestation,
> enforced by the task instruction and the read log below; it is not
> cryptographic and cannot prove what was or was not seen outside this session.
>
> Exact commands used to read `notes.md` before the freeze:
>
> ```sh
> cd /tmp/es-unitJ16 && grep -n '^## 39' notes.md && grep -n '^## 40' notes.md
> cd /tmp/es-unitJ16 && sed -n '2715,3240p' notes.md
> cd /tmp/es-unitJ16 && sed -n '10741,11340p' notes.md
> cd /tmp/es-unitJ16 && sed -n '12913,13465p' notes.md
> ```
>
> I also read all of `sources/pw.txt`, in the explicit ranges 1–500,
> 501–1000, 1001–1500, and 1501–1970.  No forbidden source was read.

Here and below \(m\geq4\),
\[
 E_m(N)=\#\{n\leq N:m/n\text{ is not a sum of three positive unit
 fractions}\},\qquad L=\log N,
\]
and constants are absolute unless a displayed uniformity parameter says
otherwise.  The conclusions concern positive denominators; permutation or
repetition of the three denominators is harmless.

## S1. The uniform multiplier identity

**Proposition S1 (exact identity).**  Let \(k,\ell,m\) be positive integers.
The §16 identity has the same form for numerator \(m\) exactly when
\[
                         k\ell\equiv-1\pmod m.                 \tag{S1.1}
\]
Put \(A=(k\ell+1)/m\).  For every factorization \(A=uvw\) and every
\(n>0\) such that
\[
                         nv\equiv-u\pmod {k\ell},              \tag{S1.2}
\]
let \(s=(nv+u)/(k\ell)\).  Then
\[
 {m\over n}={1\over suw}+{1\over nsvw}+{1\over nuvw}.          \tag{S1.3}
\]
Moreover
\[
 (m,k\ell)=(A,k\ell)=(uvw,k\ell)=1,                            \tag{S1.4}
\]
so (S1.2) is the reduced class \(n\equiv-uv^{-1}\pmod{k\ell}\).

*Proof.*  The proposed right side has numerator
\[
 nv+u+s=s(k\ell+1)=msuvw
\]
over \(nsuvw\), proving (S1.3).  Integrality of \(A\) is exactly (S1.1).
That congruence also gives \((m,k\ell)=1\).  If \(d\mid A,k\ell\), then
\(d\mid mA-k\ell=1\), proving the rest of (S1.4).  Conversely, an identity
of this form for every factorization requires \(k\ell+1=muvw\), hence
(S1.1). ∎

Thus \((\ell,m)=1\), and for each such \(\ell\) the multiplier is thinned to
one reduced progression
\[
                         k\equiv-\ell^{-1}\pmod m.             \tag{S1.5}
\]
There is no parity condition, primality condition on \(n\), or additional
coprimality hypothesis hidden in the identity.

## S2. Supply, local factors, and the harmonic lattice

Two Euler factors recur.  Define
\[
 \eta _1(m)={1\over\zeta(2)}\prod_{p\mid m}{p\over p+1},       \tag{S2.1}
\]
\[
 C_2=\prod_p(1-p^{-1})\left(1+{p-1\over p^2}\right),\qquad
 \eta _2(m)=C_2\prod_{p\mid m}
             \left(1+{p-1\over p^2}\right)^{-1}.              \tag{S2.2}
\]
The products converge after the displayed zeta-pole extraction.  Numerically
\(C_2=0.428249\ldots\).  Uniformly in \(m\),
\[
                         \eta _1(m)\asymp\eta _2(m),           \tag{S2.3}
\]
because their ratio is an absolute constant times
\(\prod_{p\mid m}(1-1/(p(p+1)))\), a product bounded above and below.

The exact logarithmic coefficients are
\[
 \sum_{\substack{k\leq K\\(k,m)=1}}{\varphi(k)\over k^2}
       \sim\eta _1(m)\log K,                                  \tag{S2.4}
\]
\[
 \sum_{\substack{k\leq K\\(k,m)=1}}{\varphi(k)^2\over k^3}
       \sim\eta _2(m)\log K.                                  \tag{S2.5}
\]
For fixed \(m\) (or uniformly once the progression contains a growing
number of terms), any reduced \(a\pmod m\) has coefficient
\(\eta_i(m)/\varphi(m)\).  This progression asymptotic is not uniform when
\(m>K\); the proofs below instead use the aggregate sums (S2.4)–(S2.5),
which remain uniform for polynomially growing \(m\).  For (S2.4), expand
\(\varphi(k)/k=\sum_{d\mid k}\mu(d)/d\); the coefficient in one reduced
progression is
\[
 {1\over m}\prod_{p\nmid m}(1-p^{-2})
   ={\eta _1(m)\over\varphi(m)}.                              \tag{S2.6}
\]
For (S2.5), the local Dirichlet factor of
\((\varphi(k)/k)^2/k\) is \(1+(p-1)/p^2\).  Removing every local factor
at \(p\mid m\), then extracting the harmonic pole, gives (S2.2).
These asymptotics are uniform in the polylogarithmic ranges used below;
primes \(p>K\) dividing \(m\) change the products by \(1+o(1)\).

It is useful not to count the thinning twice.  One may either fix a reduced
\(\ell\)-class and use (S1.5), or sum all \((k,m)=1\) and count primes in
\[
                         \ell\equiv-k^{-1}\pmod {muv}.         \tag{S2.7}
\]
Summing the \(\varphi(m)\) paired \((k,\ell)\)-classes cancels one
progression factor.  The resulting total supply has one, not two, factors
\(1/\varphi(m)\).

**General harmonic-lattice lemma.**  Let
\(\mathcal J\subseteq\{k\leq K:(k,m)=1\}\) contain 1,
\(L_{\mathcal J}=\operatorname{lcm}_{k\in\mathcal J}k\),
\(H=K^{10}\), \(z>H^2\), and \((c,L_{\mathcal J})=1\).  Then the exact
conclusions of Lemma 16.2 hold:
\[
 \sum_{k\in\mathcal J}\ \sum_*{1\over uv}
       \asymp(\log z)^2h(\mathcal J),\qquad
 \sum_{k\in\mathcal J}\ \sum_*{1\over\varphi(u)\varphi(v)}
       \ll(\log z)^2h(\mathcal J),                            \tag{S2.8}
\]
where \(h(\mathcal J)=\sum_{k\in\mathcal J}\varphi(k)/k^2\), and \(*\)
means \(H<u,v\leq z\), \((u,v)=(uv,k)=1\), and
\(u+cv\equiv0\pmod k\).  A fixed positive fraction remains after
\(\omega(uv)\leq D\log\log z\).

*Reason.*  The box count, its \(O(K^2/H)\) relative boundary error, Shiu
modulus \(k<U^{1/10},V^{1/10}\), and Rankin tail do not contain \(m\).
Only the set of admitted \(k\)'s changes.  Thus the power-range version used
in Theorem 34.8 remains valid when \(z>K^{20}\).

The prime progression does contain \(m\).  Divisibility \(uv\mid
(k\ell+1)/m\) is exactly (S2.7), with modulus
\[
                              q=muv.                          \tag{S2.9}
\]
The residue is reduced by (S1.4).  In a canonical lower box
\(u,v\leq x^{1/6}\), Bombieri–Vinogradov requires
\[
 m x^{1/3}\leq{x^{1/2}\over(\log x)^A}.                      \tag{S2.10}
\]
At the bottom block \(x=X^{1/2}\), it is enough that
\(m\leq X^{1/12}/(\log X)^A\).  For the upper bound,
Brun–Titchmarsh needs \(m x^{2/3}<x^{1-o(1)}\), also automatic in all
polylogarithmic-in-\(N\) applications here.  Fixed-modulus multiplicity is
unchanged: after \(q=muv\) is fixed, \(uv=q/m\), giving at most
\(K2^{\omega(uv)}\) raw triples or
\((\log X)^{4+D\log2}\) low-congestion triples.  No divisor factor of
\(m\) appears.

The inequalities
\[
 {1\over\varphi(muv)}\geq {1\over\varphi(m)uv},\qquad
 {1\over\varphi(muv)}\leq
 {1\over\varphi(m)\varphi(u)\varphi(v)}                     \tag{S2.11}
\]
(for \((u,v)=1\)) put the whole prime-supply loss at exactly order
\(1/\varphi(m)\), uniformly even when \((m,uv)>1\).  Formula (S2.11),
not the weaker \(1/(muv)\), is essential.

## S3. Layer 1: a uniform two-thirds theorem

For a fixed reduced fibre \(c\pmod{M_0}\), one may take
\[
 M_0=6mL_{K,m},\qquad
 L_{K,m}=\operatorname{lcm}\{k\leq K:(k,m)=1\}.              \tag{S3.1}
\]
The factor \(m\) is harmless but convenient; only divisibility by the
admitted \(k\)'s is logically needed.  For primes \(\ell\in(X^{1/2},X]\),
let \(f_{m,c}(\ell)\) count distinct classes from
\[
 m uv\mid k\ell+1,\quad k\mid u+cv,\quad
 H<u,v\leq\ell^{1/3},\quad (u,v)=(uv,k)=1,              \tag{S3.2}
\]
with the low-\(\omega\) cutoff.  The determinant proof from Lemma 16.3
still deduplicates.  More directly, a collision at fixed \(\ell\) first
forces the same reduced pair \((u,v)\), and then
\(k\ell\equiv-1\pmod{muv}\) fixes \(k\pmod{muv}\); since
\(muv>H^2>K\), it fixes \(k\) itself.

Equations (S2.8)–(S2.11), ordinary BV, and Brun–Titchmarsh give
\[
 \sum_{X^{1/2}<\ell\leq X}{f_{m,c}(\ell)\over\ell}
   \asymp {\eta _1(m)\over\varphi(m)}(\log X)^2\log K,       \tag{S3.3}
\]
uniformly in every reduced fibre, provided \(K\leq(\log X)^B\) for a
fixed \(B\), (S2.10) holds, and \(X\) is large uniformly in \(B\).

Set
\[
 \theta_1(m)={\eta _1(m)\over\varphi(m)}.                    \tag{S3.4}
\]
Taking \(K=\delta L\) gives \(\log M_0\leq\log m+O(K)<L/2\).
The larger-sieve Rankin truncation has mass
\(\mu_1\asymp\theta_1t^2\log L\), \(t=\log X\), and budget
\(t\mu_1\ll L\).  The optimal choice is
\[
 t\asymp\left({L\over\theta_1(m)\log L}\right)^{1/3},
 \quad
 \mu_1\asymp
 \left(\theta_1(m)L^2\log L\right)^{1/3}.                   \tag{S3.5}
\]
Therefore, uniformly for \(m\leq L^{2-\epsilon}\),
\[
 E_m^{\rm prime}(N)\ll_\epsilon
 N\exp\{-c_\epsilon
 [\eta_1(m)L^2\log L/\varphi(m)]^{1/3}\}.                   \tag{S3.6}
\]
The checks are: \(K\leq t^B\) for some fixed \(B=B(\epsilon)\),
\(\log m=o(t)\), (S2.10), \(t=o(L)\), and \(M_0<N^{1/2}\).
All have polynomial room.  The endpoint \(m=L^2\) can be approached with
slowly varying losses, but the fixed \(\epsilon\) statement is the clean
uniform theorem.

The semigroup transfer is uniform, not merely pointwise in fixed \(m\).
Every prime factor of an exceptional integer is exceptional, because a
representation for \(m/p\) scales by \(n/p\).  For small primes where the
uniform prime theorem is not available, take
\(U_0=\exp(C(\varphi(m)/\eta_1(m))^{1/2})\).  In the Rankin product with
\(\delta\asymp\mu_1/L\), the range \(m\leq L^{2-\epsilon}\) gives
\(\delta\log U_0=o(1)\), while allowing every prime below \(U_0\) costs
only \(\exp(O(\log\log U_0))=\exp(o(\mu_1))\).  Above \(U_0\), partial
summation uses (S3.6).  Hence (S3.6) also holds for \(E_m(N)\), with changed
constants.  Treating the small primes as an \(m\)-dependent constant would
not have proved this uniform assertion.

## S4. The general c-free atom family

Fix \(0<\kappa<1/240\), \(K=X^\kappa\), \(H=K^{10}\), and in each
canonical block \(\ell\in(x,2x]\subset(X^{1/2},X]\) put \(z=x^{1/6}\).
An atom is
\[
 A=(k,\ell,u,v),\quad k\leq K,\quad(k,m)=1,\quad
 H<u,v\leq z,                                                \tag{S4.1}
\]
\[
 \ell\text{ prime},\quad (u,v)=(uv,k)=1,\quad
 \omega(uv)\leq D\log\log X,\quad
                         muv\mid k\ell+1.                    \tag{S4.2}
\]
It denotes
\[
                         E_A=\{n:n\equiv-uv^{-1}\pmod{k\ell}\}. \tag{S4.3}
\]
Proposition S1 proves that every \(n\in E_A\) is representable.

All §39 size arguments survive unchanged.

1. If two atoms with the same \(\ell\) are compatible, reduction modulo
   \(\ell\) gives \(\ell\mid uv'-u'v\), while its absolute value is
   \(<z^2<\ell\).  Reducedness forces \((u,v)=(u',v')\).
2. With \((u,v)\) fixed, \(k\ell\equiv-1\pmod{muv}\) fixes
   \(k\pmod{muv}\).  Since \(muv>K\), the multiplier is unique.
3. Hence compatible distinct atoms have distinct \(\ell\)'s.  Also
   \(\ell>K\), so no large prime coordinate divides another multiplier.
4. For a compatible set,
   \[
   \Pr(\cap_iE_{A_i})=
    [\operatorname{lcm}(k_1,\ldots,k_j)\prod_i\ell_i]^{-1}.  \tag{S4.4}
   \]

No factor \(m\) occurs in (S4.3) or (S4.4): it thins which atoms exist, but
is not an atom modulus.  This distinction controls the final ledger.

## S5. Exact mass profile after thinning

For \(g\mid k\) and a unit \(a\pmod g\), define \(W_{k,a}(g)\) and \(W_k\)
as in §39, using (S4.1)–(S4.3).  Uniformly under (S2.10),
\[
 W_{k,a}(g)\ll {t^2\over\varphi(m)\varphi(g)}
                    {\varphi(k)^2\over k^3},\qquad
 W_k\asymp {t^2\over\varphi(m)}
                    {\varphi(k)^2\over k^3}.                \tag{S5.1}
\]
For the upper bound, repeat the residue-resolved Shiu box count and use the
upper inequality in (S2.11).  For the lower bound, fixed-\(k\) BV evaluates
(S2.7), the lower inequality in (S2.11) leaves the ordinary harmonic pair
mass, and the Rankin cutoff retains a fixed proportion.  These arguments
are uniform when primes divide both \(m\) and \(uv\); that overlap was the
main possible source of a spurious \(m/\varphi(m)\).

Consequently the c-free mass is
\[
 \mu_X=\sum_A{1\over k_A\ell_A}
   \asymp {\eta_2(m)\over\varphi(m)}t^2\log K
   \asymp \theta_2(m)t^3,\qquad
 \theta_2(m)={\eta_2(m)\over\varphi(m)}.                    \tag{S5.2}
\]
Thus \(1/\varphi(m)\) enters each \(W_k\) through the prime progression;
\(\eta_2(m)\) enters only after the aggregate \((k,m)=1\) multiplier sum.
They must not be interchanged or multiplied twice.

## S6. Factorial moments and the void

At primes dividing \(m\), the collapse-versus-consistency calculation sees
nothing: every multiplier is coprime to \(m\), so such primes divide neither
\(k\) nor the old multiplier lcm \(R\).  They have already thinned the
supply in (S5.2).

For completeness, the exact Euler statement needed in the moment induction
is the following generalization of Lemma 39.3:
\[
 \sum_{\substack{k\leq K\\(k,m)=1}}
 {\varphi(k)^2\over k^3}q_y(k)
 \prod_{\substack{p\mid(k,R)\\p>y}}{p\over p-1}
 \ll \eta_2(m)\log K.                                      \tag{S6.1}
\]
Indeed an unmodified nonconstant local mass is \((p-1)/p^2\).  Conditioning
or sharing changes it to \(1/p\), and the ratio of full local factors is
\[
 {1+1/p\over1+(p-1)/p^2}=1+O(p^{-2}).                       \tag{S6.2}
\]
The product of these ratios is uniform; at \(p\mid m\) the local factor is
simply deleted, producing exactly \(\eta_2(m)\).  Therefore, in the CRT
space conditioned by \((n,P_y)=1\),
\[
                         \mathbb E(H_X)_j\leq(C\theta_2(m)t^3)^j. \tag{S6.3}
\]
The familiar \(b_y(g)/\varphi(g)\) cancellation is unchanged at every
prime power.  In particular there is no extra \(m/\varphi(m)\), and no
\(\log\log m\) loss is needed in the moment degree.

The void needs a general-\(m\) form of Theorem 34.8.  It is not a formal
reduction to the printed \(m=4\) theorem, but its proof carries over line by
line:
\[
 \sum_{X^{1/2}<\ell\leq X}{f^{\rm good}_{m,c}(\ell)\over\ell}
 \asymp{t^2\over\varphi(m)}h(\mathcal J).                   \tag{S6.4}
\]
The box and incidence-square estimates do not change; high incidence still
costs \(T_X^{-1}(\log z)^2(1+\log K)^3\); BV uses \(q=muv\) and (S2.10);
fixed-\(q\) multiplicity is unchanged; and (S2.11) gives the matching
\(1/\varphi(m)\).  This proves (S6.4), rather than assuming a new analytic
estimate.

Reveal multiplier coordinates and let
\(\mathcal J_c=\{k\leq K:(k,m)=1,(k,c)=1\}\).  The total proxy mass is
\(h(\mathcal K_m)\sim\eta_1(m)\log K\).  A prime \(p\nmid m\) carries
local share \(1/(p+1)\ll1/p\); primes dividing \(m\) carry zero share.
The same exponential-tail proof as §39 therefore gives, after conditioning
all primes \(p\leq y\),
\[
 \Pr\{h(\mathcal J_c)<c\eta_1(m)\log K\}\leq e^{-c'y}.       \tag{S6.5}
\]
Take \(y=B\theta_2(m)t^3\).  By (S2.3), (S6.4)–(S6.5) imply
\[
             \Pr(H_X=0\mid(n,P_y)=1)\leq
             \exp\{-c\theta_2(m)t^3\}.                      \tag{S6.6}
\]
For \(r\) the least even integer above \(D\theta_2(m)t^3\), (S6.3) and
Bonferroni give the nonnegative majorant
\[
 S_y(n)Q_r(H_X(n)),\qquad
 \mathbb E_{\rm CRT}S_yQ_r(H_X)\leq e^{-c\theta_2(m)t^3}.   \tag{S6.7}
\]
Its honest ledger is
\[
 \deg=O(\theta_2t^3),\quad
 \log d_{\rm term}=O(\theta_2t^4),\quad
 \log\sum|c_{\rm term}|=O(\theta_2t^4).                    \tag{S6.8}
\]
If \(\theta_2t^3<1\), take a fixed even degree instead; the estimate is then
only constant-strength.  The record range below has
\(\theta_2t^3\to\infty\).

This closes S6.  The precise non-elementary inputs are standard Shiu,
Bombieri–Vinogradov, and Brun–Titchmarsh in the ranges displayed above; no
new distribution hypothesis is left open.

## S7. Final assembly, ranges, and PW crossover

From (S6.7)–(S6.8), finite-interval rounding is absorbed when
\[
                         \theta_2(m)t^4\leq cL.              \tag{S7.1}
\]
Optimizing, rather than fixing an \(m\)-independent window, gives
\[
 t\asymp(L/\theta_2(m))^{1/4},\qquad
 \theta_2t^3\asymp \theta_2(m)^{1/4}L^{3/4}.                \tag{S7.2}
\]
Hence
\[
 \boxed{E_m^{\rm prime}(N)\ll
 N\exp\{-c[\eta_2(m)L^3/\varphi(m)]^{1/4}\}.}              \tag{S7.3}
\]
The same bound holds for all denominators.  Uniformly, put
\(\Theta_m=\varphi(m)/\eta_2(m)\).  The prime proof has room whenever
\(\Theta_m\leq L^{3-\epsilon}\): then \(t=o(L)\), \(K,\ell,m\) have the
required ordering, (S2.10) has exponential room, \(y<X^{1/2}\), and the
omitted range below \(\max(m,K,y)\) is negligible.  For semigroup transfer,
allow all primes below \(U_0=\exp(C\Theta_m^{1/3})\).  With
\(\delta\asymp\theta_2^{1/4}L^{-1/4}\),
\[
                  \delta\log U_0\ll\Theta_m^{1/12}L^{-1/4}=o(1), \tag{S7.4}
\]
and their Euler-product cost is \(e^{O(\log\Theta_m)}=e^{o(\mu)}\).
Partial summation handles the larger exceptional primes.  Thus (S7.3) is
uniform for all denominators in the stated \(\Theta_m\leq L^{3-\epsilon}\)
window, in particular throughout each of
\(m\leq L^{1-\epsilon}\) and \(m\leq L^{3/4-\epsilon}\).

A weaker but sometimes cleaner choice \(t=\alpha L^{1/4}\) gives
\(\exp\{-c\theta_2(m)L^{3/4}\}\), meaningful uniformly for
\(m\leq L^{3/4-\epsilon}\).  This is valid but is not the optimized
\(m\)-dependence in (S7.3).  No constraint in the atom, BV, moment, ledger,
or semigroup calculation forces this weaker choice.

PW's Theorem 1.3 has exponent scale
\[
                         P=(L^2/\varphi(m))^{1/3}.            \tag{S7.5}
\]
Layer 1 improves it by the factor
\[
                         (\eta_1(m)\log L)^{1/3};             \tag{S7.6}
\]
the scale crossover is \(\log L=1/\eta_1(m)\), ignoring the unknown
absolute theorem constants.  The optimized Layer-2 exponent \(R\) satisfies
\[
 {R\over P}=
 \bigl(\eta_2(m)^3\varphi(m)L\bigr)^{1/12}.                  \tag{S7.7}
\]
Thus its scale crossover is
\[
                         L={1\over\eta_2(m)^3\varphi(m)}.     \tag{S7.8}
\]
For orientation, the right side is about 12.43 for \(m=4\), 4.97 for
\(m=5\), and 22.70 for \(m=6\); constants in the two theorems prevent these
from being literal numerical thresholds.  Asymptotically the new exponent
wins throughout the common uniformity range.

## Three likeliest failure points

1. **Residue profile with overlapping \(m\) and \(uv\).**  The two sides of
   (S2.11) must be carried in the correct directions through the
   residue-resolved Shiu count.  Replacing \(\varphi(muv)\) by
   \(\varphi(m)\varphi(u)\varphi(v)\) as an equality would give a false
   local factor.
2. **Preservation of \(\eta_2(m)\) in high factorial moments.**  A crude
   use of the unrestricted Euler bound loses \(1/\eta_2(m)\) in every
   moment.  Equation (S6.1), including deleted local factors at every
   \(p\mid m\), is required before choosing the degree and optimizing the
   window.
3. **Uniform semigroup transfer.**  A fixed-\(m\) “finite small primes”
   argument is not uniform.  The explicit thresholds and checks in
   (S3.6) and (S7.4) are needed; omitting them can turn a prime theorem into
   an unjustified all-denominator theorem.
