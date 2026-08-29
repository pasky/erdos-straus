# UNIT D19-BLIND: truncated witness tails and effectivity

## B1. Definitions and status

Fix the multiplier identity of Lemma 16.1.  For a prime denominator \(p\), define
\[
 W(p):=\min\{k\ell:\ k\ell\equiv3\pmod4,\ (k\ell+1)/4=uvw,
                    \ pv\equiv-u\pmod {k\ell}\},                 \tag{B1.1}
\]
where the minimum is over positive integral data, and put \(W(p)=\infty\) if
there are no such data.  Thus a hit in a §39 atom of multiplier \(k\) and
large prime coordinate \(\ell\) proves \(W(p)\leq k\ell\).  The converse is
neither asserted nor needed.

I use the following two parameter choices.  Floors have no effect below.

* **Logarithmic-multiplier scale.**  Let \(t=t_a(T)\) be the largest large
  real number for which
  \[
       X=e^t,\qquad K=\lfloor t^5\rfloor,\qquad KX\leq T.          \tag{B1.2}
  \]
  Then \(t=\log T-5\log\log T+O(1)\), \(\log K\asymp\log t\).
* **Power-multiplier scale.**  Fix once and for all
  \(0<\kappa<1/240\), and put
  \[
       t={\log T\over1+\kappa},\qquad X=e^t,\qquad
       K=\lfloor X^\kappa\rfloor.                              \tag{B1.3}
  \]
  Again \(KX\leq T\).

All constants below may depend on \(\kappa\), but not on \(N,T\).

**Status convention.**  B2 is a derivation from Lemma 16.3 and the §39
c-free/Bonferroni machinery, but not from Theorem 34.8.  B3 additionally
uses Theorem 34.8.  The parameter rebalancing and implications are proved
here.  The resulting tail statements inherit the repository's
**CLAIMED/PROVISIONAL** status for Lemma 16.3/§39, and B3 also inherits the
provisional referee status of Theorem 34.8.  The effectivity repair in B4
does not upgrade those proof-review labels.

## B2. Variant (a): truncation using only Lemma 16.3 supply

### B2.1 Statement

**Proposition B2.1 (logarithmic-multiplier witness tail; derived,
CLAIMED/PROVISIONAL).**  There are constants \(c,C,T_0>0\) such that, uniformly
for \(T\geq T_0\) and
\[
             \log N\geq C t^3\log K,                         \tag{B2.1}
\]
with \(t,K\) from (B1.2),
\[
 \#\{p\leq N:p\hbox{ prime},\ W(p)>T\}
       \ll N\exp\{-c t^2\log K\}.                           \tag{B2.2}
\]
Equivalently, after changing absolute constants, the exact asymptotic
window and tail shape are
\[
 \boxed{\quad
  C(\log T)^3\log\log T\leq\log N,
  \qquad
  \#\{p\leq N:W(p)>T\}
   \ll N e^{-c(\log T)^2\log\log T}.
 \quad}                                                       \tag{B2.3}
\]
Thus the largest permitted scale is
\[
 \log T\ll\left({\log N\over\log\log N}\right)^{1/3}.       \tag{B2.4}
\]
At its top, (B2.2) has saving
\((\log N)^{2/3}(\log\log N)^{1/3}\), the §16 scale.

### B2.2 Atom mass and conditioning

Use the c-free atoms (39.2)--(39.4), now with \(K=t^5\), without the
Theorem-34.8 congestion pruning.  The hypotheses behind the box estimates
hold: at the lowest dyadic prime block, \(z\geq X^{1/12}\), while
\(H^2=K^{20}=t^{100}=o(X^{1/12})\).  Also \(K\leq(\log X)^5\), exactly the
range of Lemma 16.3.

Lemma 39.2's upper profile (which uses Shiu and Brun--Titchmarsh, not
Theorem 34.8) gives the factorial-moment scale
\[
 \mu:=t^2\sum_{k\leq K,\ k\equiv1(4)}{\varphi(k)^2\over k^3}
      \asymp t^2\log K\asymp t^2\log t.                     \tag{B2.5}
\]
Set
\[
        y=B\mu,
        \qquad S_y(n)={\bf1}_{(n,P_y)=1},                    \tag{B2.6}
\]
where \(B\) is a sufficiently large fixed constant.  For large \(t\),
\(2\leq y<K<X^{1/2}\), so the conditioning does not touch any large prime
coordinate \(\ell\).

Reveal all multiplier coordinates as in Lemma 39.5 and write
\[
 \mathcal J_c=\{k\leq K:k\equiv1\pmod4,(k,c)=1\},\qquad
 Z(c)=\sum_{y<p\leq K,\ p\mid L_K,\ p\mid c}{1\over p}.      \tag{B2.7}
\]
Conditional on \(S_y=1\), the remaining prime coordinates are independent,
and
\[
 \mathbb E e^{yZ}
   =\prod_{y<p\leq K,\ p\mid L_K}
        \left(1-{1\over p}+{e^{y/p}\over p}\right)
   \leq \exp\left(Cy\sum_{p>y}p^{-2}\right)=e^{O(1)}.       \tag{B2.8}
\]
Hence \(\Pr(Z>\eta)\leq e^{-\eta y+O(1)}\).  The elementary estimate
\[
 \sum_{k\leq K,\ p\mid k}{\varphi(k)\over k^2}
       \ll {\log K\over p}                                  \tag{B2.9}
\]
and a union bound show that, for small fixed \(\eta\),
\[
 Z(c)\leq\eta\quad\Longrightarrow\quad
 h(\mathcal J_c)\gg\log K.                                 \tag{B2.10}
\]
The member \(1\) is always present and \((c,L_{\mathcal J_c})=1\).
Lemma 16.3, applied to this data-dependent but otherwise arbitrary
subfamily, supplies in its canonical dyadic boxes
\[
 \sum_{X^{1/2}<\ell\leq X}{f_c(\ell)\over\ell}
       \gg t^2h(\mathcal J_c)\gg\mu.                         \tag{B2.11}
\]
Lemma 39.1 makes the relevant \(\ell\)-coordinates distinct.  Therefore
\[
 \Pr(H_X=0\mid c)\leq
   \prod_\ell(1-f_c(\ell)/\ell)\leq e^{-c\mu}               \tag{B2.12}
\]
on the good multiplier fibres.  Combining (B2.8), (B2.12), and
\(y=B\mu\) gives
\[
       \Pr(H_X=0\mid S_y=1)\leq e^{-c\mu}.                  \tag{B2.13}
\]
This is exactly Lemma 39.5 with \(t^3\) replaced by \(\mu=t^2\log K\).
No use of Theorem 34.8 has occurred.

### B2.3 Factorial moments, Bonferroni degree, and ledger

The consistency calculation (39.14)--(39.19) is unchanged.  Lemma 39.3
now gives, at each newly inserted atom,
\[
 Ct^2\sum_{k\leq K}{\varphi(k)^2\over k^3}q_y(k)
     \prod_{p\mid(k,R),\ p>y}{p\over p-1}
       \ll Ct^2\log K\ll C\mu.                              \tag{B2.14}
\]
Thus for every \(m\geq1\),
\[
        \mathbb E(H_X)_m\leq(C\mu)^m.                       \tag{B2.15}
\]
Take \(r\) to be the least even integer at least \(D\mu\), with \(D\)
large.  The same Bonferroni identity gives
\[
 \mathbb E\{S_yQ_r(H_X)\}
 \leq e^{-c_1\mu}+{(C\mu)^{r+1}\over(r+1)!}
 \leq e^{-c\mu}.                                           \tag{B2.16}
\]

The numerical ledgers are as follows.

* The selector has degree \(\pi(y)=O(\mu/\log\mu)\) and
  \(\log P_y=O(y)=O(\mu)\).
* The atom count satisfies \(\log|\mathcal A_X|=O(t)\).
* Every nonzero term is one congruence class, and its modulus is at most
  \(P_y(KX)^r\).  Therefore
  \[
    \log d_{\rm term}\leq O(y)+r(t+\log K)=O(\mu t),         \tag{B2.17}
  \]
  since \(\log K=o(t)\).
* The total absolute coefficient sum is at most
  \[
    2^{\pi(y)}\sum_{j\leq r}{|\mathcal A_X|\choose j},
    \qquad
    \log\sum|c_{\rm term}|=O(rt)=O(\mu t).                 \tag{B2.18}
  \]

Counting each congruence class in \([1,N]\) incurs \(O(1)\).  Conditions
(B2.17)--(B2.18) are absorbed, including the target factor \(e^{-c\mu}\),
as soon as
\[
        \log N\geq C\mu t=Ct^3\log K,                       \tag{B2.19}
\]
which proves the asserted window.  If \(p>y\) and \(W(p)>T\), then
\(S_y(p)=1\), and it hits no atom because every atom has
\(k\ell\leq KX\leq T\).  Hence the majorant counts it.  The \(O(y)\)
omitted primes are absorbed by the right side of (B2.2), proving the result.

### B2.4 Polylogarithmic and pointwise consequences

For every fixed \(A>0\), \(T=(\log N)^A\) lies well inside (B2.3), and
\[
 \#\{p\leq N:W(p)>(\log N)^A\}
   \ll_A N\exp\{-c_A(\log\log N)^2\log\log\log N\}.         \tag{B2.20}
\]

A pointwise hypothesis is much stronger: if, for some fixed \(A\), every
sufficiently large prime satisfies \(W(p)\leq(\log p)^A\), then the left
side of (B2.20) is actually \(O_A(1)\).  It gives a three-unit-fraction
representation for every sufficiently large prime.  After checking the
finite remaining primes, scaling a representation along a prime divisor
settles every integer denominator.  The average tail bounds do not imply
this pointwise assertion.

## B3. Variant (b): Theorem-34.8 cubic supply

**Proposition B3.1 (power-multiplier witness tail; derived,
CLAIMED/PROVISIONAL).**  Fix \(0<\kappa<1/240\).  There are effective-shape
constants \(c_\kappa,C_\kappa,T_0>0\) such that, uniformly for
\[
                  T\geq T_0,\qquad
                  \log N\geq C_\kappa(\log T)^4,             \tag{B3.1}
\]
we have
\[
 \boxed{\quad
 \#\{p\leq N:p\hbox{ prime},\ W(p)>T\}
      \ll_\kappa N\exp\{-c_\kappa(\log T)^3\}.
 \quad}                                                       \tag{B3.2}
\]
Equivalently, the top of the uniform window is
\(\log T\ll_\kappa(\log N)^{1/4}\).

Here are all parameter steps.  Use (B1.3), so that \(\log K=\kappa t+O(1)\)
and Theorem 34.8 gives, uniformly in every reduced surviving multiplier
fibre,
\[
                  \mu\asymp t^2\log K\asymp t^3.            \tag{B3.3}
\]
The geometric condition at the lowest block is precisely
\[
       z\geq X^{1/12}>K^{20}=X^{20\kappa},                  \tag{B3.4}
\]
which explains the strict bound \(\kappa<1/240\).

Take
\[
                y=B t^3,\qquad r=D_Bt^3.                    \tag{B3.5}
\]
Then \(y<X^{1/2}\), and in fact \(y<K\), for all sufficiently large \(t\).
The bad-fibre Chernoff cost is \(e^{-\eta y+O(1)}\), Theorem 34.8 applied
to \(\mathcal J_c\) gives the good-fibre void \(e^{-ct^3}\), and the
factorial moments satisfy
\[
                 \mathbb E(H_X)_m\leq(Ct^3)^m.              \tag{B3.6}
\]
Bonferroni therefore gives CRT mean \(e^{-ct^3}\).  The complete finite
ledger is
\[
 \begin{split}
  \deg&\leq r+\pi(y)=O(t^3),\\
  \log d_{\rm term}&\leq O(y)+r(t+\log K)=O(t^4),\\
  \log\sum|c_{\rm term}|&=O(rt)=O(t^4).                     \tag{B3.7}
 \end{split}
\]
Thus \(\log N\geq C t^4\) absorbs every rounding error.  Since
\(KX\leq T\), the same no-hit argument as in B2 proves (B3.2), with
\(t=(1+\kappa)^{-1}\log T\).

At the top of (B3.1), \(t\asymp(\log N)^{1/4}\), so (B3.2) becomes
\[
             N\exp\{-c(\log N)^{3/4}\}.                     \tag{B3.8}
\]
Every exceptional prime has \(W(p)=\infty\), and Theorem 16.5's semigroup
transfer then recovers exactly the conclusion and exponent of Theorem 39.7.

For every fixed \(A>0\), the polylogarithmic specialization is
\[
 \#\{p\leq N:W(p)>(\log N)^A\}
       \ll_{A,\kappa}N\exp\{-c_{A,\kappa}(\log\log N)^3\}.    \tag{B3.9}
\]
The pointwise interpretation is the same as in B2.4.

## B4. Effectivity audit and repair

### B4.1 Audit table

Here “ineffective” means that the displayed all-moduli theorem, as invoked
through its textbook proof, has an uncomputed threshold or constant because
of Siegel's theorem.  It does not mean conditional.

| Ingredient | Audit | Exact reason |
|---|---|---|
| Lemma 16.2, box count (16.4)--(16.5a) | elementary and effective | Möbius inversion, interval counts, and explicit boundary errors only. |
| Lemma 16.2, Shiu (16.5b)--(16.5g) | effective-classical | Shiu's Brun--Titchmarsh theorem for fixed functions/relative interval, plus effective Mertens estimates.  No variable-character prime number theorem is used. |
| Lemma 16.2, low-\(\omega\) Rankin tail and (16.6) | effective | Rankin is elementary; the fixed progression \(1\pmod4\) can be handled with fixed \(\chi_4\), with effective constants. |
| Lemma 16.3, distinctness and upper bound | elementary/effective-classical | Determinant argument and Brun--Titchmarsh. |
| Lemma 16.3, lower bound | **ineffective as written** | The exact culprit is the arbitrary-saving Bombieri--Vinogradov invocation after (16.9a): “take \(R=C_D+10\) and the corresponding ... constant.”  Its standard small-conductor input is Siegel--Walfisz. |
| Lemma 34.7 and pruning (34.20) | elementary/effective | A second incidence moment from the box count and Markov's inequality. |
| Theorem 34.8 lower prime slice | **ineffective as written** | The line after (34.21), “ordinary Bombieri--Vinogradov, with a fixed saving ...”, has the same small-conductor issue.  The range is \(4H^2<q=4uv\leq4x^{1/3}\). |
| Lemma 39.1 | elementary/effective | Divisibility, determinant, CRT. |
| Lemma 39.2 upper profile | effective-classical | Shiu plus Brun--Titchmarsh. |
| Lemma 39.2 lower profile | **ineffective as written** | Its fixed-\(k\) Bombieri--Vinogradov sentence still averages moduli \(4uv\) and still contains induced characters of small conductor.  Removing the factor \(K\) does not remove Siegel sensitivity. |
| Lemmas 39.3--39.4 | effective, given the upper profile | Euler products and factorial-moment induction. |
| Lemma 39.5 | inherits ineffectivity | Chernoff and (39.26) are effective; the good-fibre lower mass invokes Theorem 34.8. |
| Theorems 39.6--39.7 | inherit ineffectivity as written | Bonferroni, CRT counting, and semigroup transfer are effective; their class-supply input is not. |
| Theorem 16.4 | inherits ineffectivity | The larger-sieve/Rankin calculation is effective, and Chebyshev suffices for \(\log L_K\ll K\); Lemma 16.3's lower mass is the only Siegel-sensitive input. |
| Theorem 16.5 | inherits ineffectivity | Rankin's semigroup argument is effective once an effective prime theorem with an effective starting point is supplied. |
| B2 and B3 tails | inherit ineffectivity as written | Only through the same lower class-supply uses.  Their conditioning, moments, ledger, and truncation are effective. |

The fact that all actual progression moduli \(q=4uv\) can be polynomially
large does **not** remove the issue: characters modulo a large \(q\) can be
induced by a primitive character of very small conductor.

### B4.2 Induced-character bookkeeping

**Lemma B4.1 (one primitive character across large moduli).**  Fix a
primitive character \(\chi^*\) of conductor \(r\).  For each multiple
\(q\) of \(r\), exactly one character modulo \(q\) is induced by
\(\chi^*\); for \(q\) not divisible by \(r\), there is none.  Consequently
there are at most \(\lfloor Q/r\rfloor\) such induced characters among all
moduli \(q\leq Q\).  Moreover
\[
 \sum_{\substack{q\leq Q\\r\mid q}}{1\over\varphi(q)}
       \leq {C\log(2Q/r)\over\varphi(r)}.                   \tag{B4.1}
\]
If \(\chi_q\) is the induced character, then uniformly for \(u\leq x\),
\[
       \psi(u,\chi_q)=\psi(u,\chi^*)+O(\omega(q)\log x).     \tag{B4.2}
\]

*Proof.*  Restriction to integers coprime to \(q\) uniquely defines the
induced character, proving the first assertions.  Since
\(\varphi(rm)\geq\varphi(r)\varphi(m)\),
\[
 \sum_{r\mid q\leq Q}{1\over\varphi(q)}
 \leq{1\over\varphi(r)}\sum_{m\leq Q/r}{1\over\varphi(m)}.
\]
The identity
\[
 {n\over\varphi(n)}=\sum_{d\mid n}{\mu^2(d)\over\varphi(d)}
\]
shows, after writing \(n=dm\), that the last sum is at most
\(C\log(2Q/r)\), because
\(\sum_d\mu^2(d)/(d\varphi(d))<\infty\).  Finally the two \(\psi\)-sums
differ only at prime powers whose prime divides \(q\) but not \(r\); for
each such prime their total \(\Lambda\)-weight up to \(x\) is at most
\(\log x\).  This proves (B4.2). \(\square\)

In the max-residue orthogonality formula, (B4.1)--(B4.2) show that a real
zero \(\beta\) of \(L(s,\chi^*)\) can cost, in \(\psi\)-form,
\[
       \gg {x^\beta\log(2Q/r)\over\varphi(r)}                \tag{B4.3}
\]
across its induced moduli (and the same divided by \(\log x\) in
\(\pi\)-form).  A lower cutoff \(q\geq x^\delta\) does not create a power
saving: there are about \(Q/r\) induced moduli, while each residue error has
the compensating \(1/\varphi(q)\) factor.  This is why the polynomial lower
bound \(4uv>4K^{20}\), even when \(K=X^\kappa\), does not by itself make
(16.9a) or (34.21) effective.

### B4.3 Effective exceptional-modulus Bombieri--Vinogradov

The following is the precise effective-classical replacement needed here.

**Lemma B4.2 (effective dyadic BV with one divisor deleted).**  For every
fixed \(A>0\), there are effectively computable \(B,D,C,X_0\) such that,
for each \(X\geq X_0\), there is either no exceptional conductor or one
primitive real conductor
\[
       r_X\leq(\log X)^D                                    \tag{B4.4}
\]
with the following property.  Simultaneously for all dyadic
\(X^{1/2}\leq x\leq X\) and
\(Q\leq x^{1/2}/(\log x)^B\),
\[
 \sum_{\substack{q\leq Q\\r_X\nmid q}}
  \max_{(a,q)=1}\left|\pi(2x;q,a)-\pi(x;q,a)
       -{\operatorname {li}(2x)-\operatorname {li}(x)\over\varphi(q)}
                  \right|
       \leq {Cx\over(\log x)^A}.                            \tag{B4.5}
\]
If there is no exception, interpret the divisibility restriction as empty.
The possible conductor can be required to exceed any fixed constant, by
effectively treating the finitely many smaller primitive characters.

*Proof.*  Choose a fixed large power \(Z=(\log X)^D\).  The effective
Landau--Page theorem says that among primitive characters of conductor at
most \(Z\), at most one real character has a zero in the exceptional
zero-free strip.  Delete every modulus divisible by its conductor.  A
character modulo a remaining modulus cannot be induced by that exceptional
character, by Lemma B4.1.  The standard proof of Bombieri--Vinogradov now
has effective inputs throughout: the effective zero-free region and explicit
formula give the required Siegel--Walfisz-strength estimate for every
remaining primitive conductor at most \(Z\), and the large-sieve/Vaughan
identity estimates handle primitive conductors above \(Z\).  Choosing
\(B,D\) in the usual order in terms of \(A\) gives the effective
\(\psi\)-version, uniformly in the endpoint; partial summation gives
(B4.5).

One application of Landau--Page at the top scale \(X\), rather than a new
application in each block, is legitimate because
\(\log x\asymp\log X\) throughout \([X^{1/2},X]\).  It also proves that
the same \(r_X\) works in every dyadic block.  If one instead selected an
exception separately in each block, the deleted family could change with
the block; that is unnecessary and would obscure uniformity.  Finally, for
the finitely many conductors below a fixed \(R_0\), numerical isolation of
their zeros gives an effective positive distance from 1 and an effective
starting point. \(\square\)

This proof uses Landau--Page, the effective zero-free region, Vaughan's
identity, and the large sieve as effective classical inputs; it does not
claim they are elementary.  Lemma B4.1 supplies the induced-character step
which is sometimes hidden inside the phrase “delete the exceptional
modulus.”

### B4.4 The deletion-tolerance lemma

The remaining question is whether deleting every progression modulus
\(4uv\) divisible by \(r_X\) destroys the §16 mass.  It does not.

**Lemma B4.3 (uniform exceptional-divisor deletion in the harmonic box).**
Increase the fixed low-\(\omega\) constant \(D\), if necessary.  In the
setup of Lemma 16.2, uniformly in the reduced fibre \(c\), every admissible
\(k\), every subfamily \(\mathcal J\) containing 1, and every integer
\(r\geq3\) with \(r\nmid4\),
\[
 \sum_{k\in\mathcal J}
 \sum_{\substack{H<u,v\leq z,\ (u,v)=(uv,k)=1\\
                  u+cv\equiv0\ (k),\ r\nmid4uv\\
                  \omega(uv)\leq D\log\log z}}{1\over uv}
       \gg (\log z)^2h(\mathcal J).                         \tag{B4.6}
\]
All constants and the starting point are effective and independent of
\(r,c,\mathcal J\).  The same assertion is true pointwise for one \(k\),
with right side
\(\gg(\varphi(k)/k^2)(\log z)^2\).

*Proof.*  Since \(r\nmid4\), choose a prime \(p\) for which
\(v_p(r)>v_p(4)\).  It is enough to retain pairs with \(p\nmid uv\).  If
\(p\mid k\), every original pair already has \(p\nmid uv\).  Suppose
\(p\nmid k\).

Repeat the multiplicative-box proof of (16.4), but require both variables
to be nonzero modulo \(p\).  After Möbius inversion, \((d,kp)=1\).  For
one fixed reduced \(b\pmod k\), the admissible \(a\)'s are the progression
\(a\equiv-cb\pmod k\) with its one zero class modulo \(p\) removed; interval
counting gives its expected factor \(1-1/p\) with \(O(1)\) error.  Counting
\(b\)'s coprime to \(kp\) gives the other factor \(1-1/p\), with
\(O(\tau(kp))\) error.  Since \(\tau(kp)\leq2\tau(k)\), summing over \(d\)
gives, uniformly even when \(p\) is larger than the box,
\[
 \#\{(u,v)\in I\times J:\text{old conditions},\ p\nmid uv\}
 =\eta^2UV{\varphi(k)\over k^2}P(k){p-1\over p+1}
   +O((U+V)\tau(kp)\log(2UV)).                              \tag{B4.7}
\]
Indeed the local-factor ratio is
\[
 { (1-1/p)^2\over1-1/p^2}={p-1\over p+1}\geq{1\over3}.      \tag{B4.8}
\]
The boundary aggregation is the same as (16.5), up to an absolute factor,
and \(H=K^{10}\) absorbs it pointwise in \(k\).  Therefore the unrestricted
harmonic mass with \(p\nmid uv\) is at least a fixed positive fraction of
(16.5a), uniformly in \(p\).

Finally (16.5h), with \(D\) chosen a little larger, makes the entire
high-\(\omega\) mass less than, say, one sixth of (16.5a).  Subtracting it
from the at-least-one-third mass in (B4.8) leaves a fixed positive fraction.
Summing the pointwise result over an arbitrary \(\mathcal J\) proves
(B4.6). \(\square\)

There is an unavoidable exception to the literal phrase “uniformly for all
\(r\geq3\)”: if \(r=4\), every modulus \(4uv\) is divisible by \(r\), so
no deletion-tolerance statement is possible.  This is harmless for the
repair.  Treat the finitely many small primitive characters effectively in
Lemma B4.2 and arrange that a possible \(r_X\) exceeds, say, 8.  In
particular \(r_X\nmid4\).  Lemma B4.3 then applies.  It also covers \(r=8\):
retaining odd \(uv\) leaves the uniform local fraction \(1/3\).

The lemma is genuinely uniform in the subfamily and fibre: (B4.7) is
pointwise in each \(k,c\), and no averaging over \(c\) or over
\(\mathcal J\) occurs.

### B4.5 Repairing every class-supply use

Apply Lemma B4.2 once at the outer scale \(X\), and in every canonical box
retain only triples with \(r_X\nmid4uv\).

1. **Lemma 16.3.**  Lemma B4.3 leaves a fixed fraction of its harmonic main
   term.  The modulus multiplicity remains polylogarithmic.  Equation
   (B4.5), with \(A\) larger than that multiplicity exponent, evaluates all
   retained prime progressions effectively.  Hence both halves of (16.8),
   including the original unpruned \(f_c\), have effective constants: the
   retained classes are a subset of those counted by \(f_c\).
2. **Theorem 34.8.**  Begin with the deletion-surviving mass.  Lemma 34.7
   bounds all high-incidence mass by \(o(1)\) of the original mass, with an
   effective rate \(O(1/\log X)\); hence it is also eventually less than
   half of the fixed surviving mass.  On the remaining low-congestion
   triples, (34.21) is polylogarithmic and effective (B4.5) applies.  Thus
   (34.18)--(34.19) acquire effective constants.
3. **Section 39.**  For lower estimates, use the same fixed, c-free
   subfamily with \(r_X\nmid4uv\).  Upper profiles and factorial moments can
   only decrease when atoms are removed.  Lemma B4.3 is pointwise in every
   \(k\) and every \(c\), so Theorem 34.8 remains uniform for the
   data-dependent \(\mathcal J_c\).  The conditioned void is therefore
   effective.  All later Chernoff, Bonferroni, coefficient-ledger, CRT, and
   semigroup constants are effective.

**Effectivity perimeter.**  Subject to their stated proof-review status, the
repair makes Lemma 16.3, Theorems 16.4--16.5, Theorem 34.8, Lemma 39.2's
lower half, Theorems 39.6--39.7, and B2--B3 fully effective in the usual
analytic sense: there is a computable threshold and computable constants.
No Siegel-zero dependence remains.  This does **not** provide conveniently
small numerical constants, and it does not turn the repository's
CLAIMED/PROVISIONAL theorems into externally checked theorems.  Without the
deletion repair, the corresponding arbitrary-saving BV lines remain
ineffective as written.

## B5. Comparison with Pomerance--Weingartner §4

PW attach to each auxiliary prime \(q\equiv-1\pmod m\) a set of at least
\(f_m(q)\) forced residue classes modulo \(q\).  Define
\[
 W_{\rm PW}(n)=\min\{q:\ n\text{ lies in one of these }f_m(q)
                    \text{ classes modulo }q\}.             \tag{B5.1}
\]
Truncating their proof at auxiliary primes \(q\leq T\), Lemma 4.1 gives
\[
            \mu_{\rm PW}(T):=\sum_{q\leq T}{f_m(q)\over q}
                 \asymp{(\log T)^2\over\varphi(m)}.          \tag{B5.2}
\]
This is uniform only in the range stated in that lemma,
\(m\leq(\log T)^{O(1)}\), with the fixed exponent implicit in the constants.
Their Rankin estimate for the truncated larger-sieve denominator is
\[
 {G-S\over G}\leq
 \exp\left\{-{\log N\over2\log T}
       +C{(\log T)^2\over\varphi(m)}\right\}.                \tag{B5.3}
\]
Consequently, whenever
\[
          T\leq N^{1/2},\qquad
          \log N\geq C{(\log T)^3\over\varphi(m)},           \tag{B5.4}
\]
their own argument, without optimization, gives
\[
 \boxed{\quad
 \#\{n\leq N:W_{\rm PW}(n)>T\}
   \ll N\exp\left\{-c{(\log T)^2\over\varphi(m)}\right\}.
 \quad}                                                       \tag{B5.5}
\]
For fixed \(m=4\), this is the window
\(\log T\ll(\log N)^{1/3}\) and the tail
\(N e^{-c(\log T)^2}\).  At the top it is Vaughan/PW's
\(N e^{-c(\log N)^{2/3}}\).  For \(T=(\log N)^A\), it gives
\[
       N\exp\{-c_{A,m}(\log\log N)^2\}.                      \tag{B5.6}
\]
Compared with B2, PW have no multiplier harmonic factor \(\log K\), so
their polylogarithmic witness tail lacks the extra
\(\log\log\log N\).  Compared with B3, they have quadratic rather than
cubic mass.

The analytic inputs in PW §4 are: divisor inequalities and harmonic divisor
sums; Brun--Titchmarsh for the upper half of Lemma 4.1; Bombieri--Vinogradov
for the lower half at progression moduli
\[
             mdt\leq m x^{1/3},\qquad d,t\leq x^{1/6};       \tag{B5.7}
\]
and the elementary larger sieve plus Rankin truncation.  Only the BV lower
bound is Siegel-sensitive.  Thus, under the same textbook interpretation as
B4, their chain is **ineffective as printed**.

For fixed \(m=4\), the Landau--Page deletion repair works just as above:
a possible large exceptional conductor does not divide \(m\), and deleting
pairs with \(r_X\mid dt\) leaves a constant fraction of the harmonic
\((d,t)\)-mass.  Hence the classical \(m=4\) tail can be made effective.
For PW's uniform theorem in varying \(m\), there is an extra perimeter: the
exceptional conductor may divide \(m\), in which case every modulus \(mdt\)
is deleted and this simple tolerance argument gives no mass.  An effective
uniform-in-\(m\) version therefore needs either an explicit exceptional-term
analysis or a stated exclusion; it does not follow merely by observing that
\(mdt\) can be large.

## B6. Self-assessment

1. **Most attackable analytic assertion:** Lemma B4.2 packages the standard
   effective exceptional-modulus version of Bombieri--Vinogradov.  A hostile
   reviewer should check the exact textbook formulation of Landau--Page and
   the endpoint-maximal BV theorem, especially that one top-scale conductor
   works uniformly over all dyadic \(x\in[X^{1/2},X]\).
2. **Deletion lemma:** the local ratio \((p-1)/(p+1)\) and the claim that the
   box boundary remains uniform for arbitrarily large \(p\) should be
   replayed line by line.  The proof uses “one progression modulo \(k\)
   minus its zero class modulo \(p\),” not a crude enumeration of \(p\)
   residue classes; a hidden factor \(p\) here would break uniformity.
3. **Inherited weak point, not repaired here:** B3 still depends on Theorem
   34.8 being uniform in the data-dependent \(\mathcal J_c\), and both B2
   and B3 depend on the §39 residue-profile/factorial-moment cancellation.
   Effectivity does not validate those provisional steps.
4. **PW perimeter:** the assertion that fixed-\(m\) harmonic mass tolerates
   deleting \(r_X\mid dt\) is straightforward by the same local-factor
   argument, but I did not re-prove a full PW lemma with all \(\Omega(dt)\)
   cutoffs.  It should not be used for their varying-\(m\) theorem when
   \(r_X\mid m\).
