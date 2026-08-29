# Wave 15: independent re-derivation and audit of Theorem 34.8

## Scope and protocol note

I treated only Lemmas 16.1--16.3, the setup of §34, and the statement of Theorem 34.8 as inputs to the derivation below. There is a line-number ambiguity in the assigned blind window: the requested `notes.md` range through line 11110 itself contains the printed proof of Lemma 34.7, although the instructions separately say to read only its statement. I independently reconstructed the moment argument below from the definition of the incidence. While fetching the end of the theorem statement, I also saw the opening paragraph of the printed proof of Theorem 34.8; no later part of that proof was read before this derivation was written. This is therefore an independent mathematical derivation with that limited protocol disclosure, not a claim of literal zero exposure.

Throughout, fix \(0<\kappa<1/240\), let \(X^{1/2}\le x\le X\), \(K_0\le K\le X^\kappa\), \(H=K^{10}\), \(z=x^{1/6}\), and let \(\mathcal J\subseteq\{k\le K:k\equiv1\pmod4\}\) contain 1. Put
\[
 h(\mathcal J)=\sum_{k\in\mathcal J}\frac{\varphi(k)}{k^2},\qquad
 r(u,v)=r_{\mathcal J}(u,v;c)=\#\{k\in\mathcal J:k\mid u+cv\},
\]
where \(c\) is reduced modulo \(24L_{\mathcal J}\). In particular, \((c,k)=1\) for every \(k\in\mathcal J\), and
\[
 h(\mathcal J)\ge \varphi(1)=1.                                      \tag{B15.1}
\]
The latter elementary point is essential for uniform pruning over arbitrary subfamilies.

## Phase 1: proof from the stated inputs

### 1. Source-level check of the short-interval input

Shiu's Theorem 1 (`sources/shiu-1980.pdf`, p. 163) applies to a nonnegative multiplicative \(F\) in his class \(M\): for some fixed \(A_1\), \(F(p^j)\le A_1^j\), and for every \(\epsilon>0\), \(F(n)\ll_\epsilon n^\epsilon\). For fixed \(0<\alpha,\beta<1/2\), its interval and modulus hypotheses are
\[
 q<y^{1-\alpha},\qquad x_0^\beta<y\le x_0,
\]
for the interval \(x_0-y<n\le x_0\), and the residue must be reduced modulo \(q\). Its conclusion is
\[
 \sum_{\substack{x_0-y<n\le x_0\\n\equiv a\pmod q}}F(n)
 \ll \frac{y}{\varphi(q)\log x_0}
 \exp\!\left\{\sum_{\substack{p\le x_0\\p\nmid q}}\frac{F(p)}p\right\}.       \tag{B15.2}
\]
For a campaign box \((U,(1+\eta)U]\), take \(x_0=(1+\eta)U\), \(y=\eta U\), with fixed \(\eta\). Choosing, for example, \(\alpha=\beta=1/4\), both source conditions hold for all sufficiently large \(U\), because
\[
 q=k\le K<U^{1/10}<(\eta U)^{3/4},\qquad ((1+\eta)U)^{1/4}<\eta U.       \tag{B15.3}
\]
Thus the campaign's much weaker-looking assertion “fixed relative length and \(k<U^{1/10}\)” is safely inside Shiu's actual range. The often quoted sufficient condition \(q\le U^{1/2}\) is also safe after fixing any \(\alpha<1/2\) and taking \(U\) large; it is not a replacement for checking (B15.3).

The two functions used here satisfy the source hypotheses:

* \(F(n)=t^{\omega(n)}\), fixed \(1<t<2\): \(F(p^j)=t\le t^j\), and \(F(n)\le\tau(n)^{\log_2t}\ll_{t,\epsilon}n^\epsilon\).
* \(F(n)=n/\varphi(n)\): \(F(p^j)=p/(p-1)\le2\le2^j\), and \(F(n)\ll\log\log(3n)\ll_\epsilon n^\epsilon\).

The relevant residue is \(-cv\pmod k\) (or symmetrically \(-c^{-1}u\pmod k\)); it is reduced because \((v,k)=1\) and \((c,k)=1\). All constants are independent of the residue and hence of \(c\). Nair--Tenenbaum (`sources/nair-tenenbaum-1998.pdf`, p. 119) accurately restates the Shiu short-sum framework and develops a stronger polynomial-value theorem, but no Nair--Tenenbaum result is needed in this proof.

### 2. Power-sized extension of the harmonic lattice estimate

Partition \((H,z]\) into fixed-ratio boxes \(I=(U,(1+\eta)U]\), \(J=(V,(1+\eta)V]\). For fixed \(k\), Möbius inversion of \((u,v)=1\), followed by counting the unique reduced class \(u\equiv-cv\pmod k\), gives
\[
 \#\{(u,v)\in I\times J:(u,v)=(uv,k)=1,\ k\mid u+cv\}
 =\eta^2UV\frac{\varphi(k)}{k^2}P(k)
 +O((U+V)\tau(k)\log(2UV)),                                \tag{B15.4}
\]
where \(P(k)=\prod_{p\nmid k}(1-p^{-2})\asymp1\). The calculation is pointwise in every reduced \(c\).

After division by \(UV\) and summation over boxes, with \(L=\log(z/H)\), the boundary contribution for one \(k\) is
\[
 O\!\left(\frac{\tau(k)\log z\,L}{H}\right).               \tag{B15.5}
\]
The main term is \(\asymp (\varphi(k)/k^2)L^2\). Since \(z>H^2\) implies \(L>\tfrac12\log z\), and \(k^2/\varphi(k)\le k\tau(k)\), \(\tau(k)\le2\sqrt{k}\), the error/main ratio is \(O(K^2/H)=O(K^{-8})\). This calculation does not require \(K\) to be polylogarithmic.

Applying (B15.2) successively in the two variables after dropping only \((u,v)=1\) gives, exactly as dictated by its Euler factors,
\[
 \sum^*\frac{t^{\omega(u)+\omega(v)}}{uv}
 \ll_t \frac{\varphi(k)}{k^2}L^2(\log z)^{2(t-1)},           \tag{B15.6}
\]
and
\[
 \sum^*\frac1{\varphi(u)\varphi(v)}
 \ll \frac{\varphi(k)}{k^2}L^2.                            \tag{B15.7}
\]
Here \(\sum^*\) has the conditions in (B15.4). To check uniformity in \(k\), the quotient of the two Shiu local factors and \(1/\varphi(k)\) by \(\varphi(k)/k^2\) is
\[
 \frac{k^2}{\varphi(k)^2}\exp\{-2\sum_{p\mid k}b_p\},
\]
with \(b_p=t/p\) or \(1/(p-1)\). Its logarithm has nonpositive or cancelling linear terms in \(1/p\), and an absolutely summable \(O_t(p^{-2})\) remainder. It is therefore bounded independently of \(k\).

Rankin's inequality in (B15.6), using \((u,v)=1\), gives
\[
 \sum^*_{\omega(uv)>D\log\log z}\frac1{uv}
 \ll \frac{\varphi(k)}{k^2}L^2
 (\log z)^{2(t-1)-D\log t}.                                 \tag{B15.8}
\]
Fix \(t=3/2\) and then a fixed integer \(D\) making the exponent negative. Enlarging \(K_0\) if needed leaves a fixed positive proportion of (B15.4)'s harmonic main term. Consequently, whenever \(z>K^{20}\),
\[
 \sum_{k\in\mathcal J}\sum_{\substack{H<u,v\le z\\(u,v)=(uv,k)=1\\k\mid u+cv\\\omega(uv)\le D\log\log X}}
 \frac1{uv}\asymp(\log z)^2h(\mathcal J),                  \tag{B15.9}
\]
with the corresponding upper bound (B15.7). Replacing \(\log\log z\) by the larger campaign cutoff \(\log\log X\) is harmless.

At the lowest allowed \(x\),
\[
 z\ge X^{1/12},\qquad K^{20}\le X^{20\kappa},
\]
and \(20\kappa<1/12\). Hence \(z>K^{20}\) uniformly for sufficiently large \(X\), and \(L\asymp\log z\). This simultaneously validates the box error and the Shiu modulus condition for power-sized \(K\).

### 3. Independent second-incidence-moment lemma

Expand the square of \(r(u,v)\). For each \(k,k'\in\mathcal J\), put \(d=[k,k']\le K^2\). The two divisibilities are equivalent to \(d\mid u+cv\), and \((c,d)=1\). Moreover, under \((u,v)=1\), this congruence itself forces \((uv,d)=1\): a prime dividing one of \(u,v\) and \(d\) would, using \((c,d)=1\), divide the other.

Repeating the elementary box count (B15.4) with modulus \(d\), and using it only as an upper bound, gives
\[
 \sum_{\substack{H<u,v\le z\\(u,v)=1\\d\mid u+cv}}\frac1{uv}
 \ll \frac{\varphi(d)}{d^2}(\log z)^2
     +\frac{\tau(d)(\log z)^2}{H}.                          \tag{B15.10}
\]
The second term follows because \(\sum_U U^{-1}=O(H^{-1})\) and there are \(O(\log(z/H))\) boxes in the other variable.

Since \(1/[k,k']=(k,k')/(kk')\),
\[
 \sum_{k,k'\le K}\frac{\varphi([k,k'])}{[k,k']^2}
 \le \sum_{k,k'\le K}\frac{(k,k')}{kk'}
 \ll (1+\log K)^3.                                         \tag{B15.11}
\]
For example, expand \((k,k')=\sum_{e\mid k,e\mid k'}\varphi(e)\); the right side is at most
\(\sum_{e\le K}e^{-1}(1+\log(K/e))^2\). Also \(\tau([k,k'])\le2\sqrt{[k,k']}\le2K\), so summing the boundary terms in (B15.10) over at most \(K^2\) pairs costs
\[
 O\!\left(\frac{K^3}{H}(\log z)^2\right)=O(K^{-7}(\log z)^2).
\]
Thus, uniformly in \(c\) and in the subfamily,
\[
 \sum_{\substack{H<u,v\le z\\(u,v)=1}}\frac{r(u,v)^2}{uv}
 \ll(\log z)^2(1+\log K)^3.                                \tag{B15.12}
\]
This proves the required Lemma-34.7-type input without Shiu or any distribution theorem.

### 4. Congestion pruning preserves the main mass

Let \(T_X=(\log X)^4\). On a pair with \((u,v)=1\), every counted incidence automatically has \((uv,k)=1\), as above. Therefore the harmonic mass of all high-congestion triple incidences, even before imposing the low-\(\omega\) restriction, is
\[
 \begin{aligned}
 M_{\rm bad}
 &\le \sum_{H<u,v\le z}\frac{r(u,v)\mathbf1_{r(u,v)>T_X}}{uv}\\
 &\le \frac1{T_X}\sum_{H<u,v\le z}\frac{r(u,v)^2}{uv}\\
 &\ll \frac{(\log z)^2(1+\log K)^3}{(\log X)^4}
 =o((\log z)^2h(\mathcal J)).                              \tag{B15.13}
 \end{aligned}
\]
The last little-oh is uniform: \(K\le X^\kappa\) makes the ratio \(O_\kappa(1/\log X)\), and (B15.1) supplies \(h(\mathcal J)\ge1\). Combining (B15.9) and (B15.13), low-congestion, low-\(\omega\) triples retain mass
\[
 \sum_{\rm good}\frac1{uv}\asymp(\log z)^2h(\mathcal J).  \tag{B15.14}
\]

### 5. Bombieri--Vinogradov with the actual multiplicity

For a good triple, set \(q=4uv\). Then
\[
 q\le4z^2=4x^{1/3},
\]
which lies below \(x^{1/2}/(\log x)^A\) for every fixed \(A\), once \(x\) is large. For fixed \(q\), coprimality allows each prime-power factor of \(q/4=uv\) to be assigned wholly to either \(u\) or \(v\), so there are at most \(2^{\omega(uv)}\) ordered pairs. For each ordered pair, the number of admitted \(k\)'s is at most \(r(u,v)\le T_X\). Hence
\[
 W_{\rm good}(q)\le2^{\omega(uv)}T_X
 \le(\log X)^{D\log2+4}.                                   \tag{B15.15}
\]
This bound is independent of whether different \(k\)'s yield the same residue. Applying the standard Bombieri--Vinogradov theorem with a fixed logarithmic saving larger than \(D\log2+4\), and using \(\log x\asymp\log X\), gives
\[
 \sum_{\rm good}|E(x;4uv,-k^{-1})|
 \le(\log X)^{D\log2+4}
 \sum_{q\le4x^{1/3}}\max_{(a,q)=1}|E(x;q,a)|
 =o(x\log x\,h(\mathcal J)).                              \tag{B15.16}
\]
Here \((k,4uv)=1\), so the progression is reduced. The fixed-log-power multiplier is fully absorbable because Bombieri--Vinogradov offers any prescribed fixed log saving. Uniformity in \(c\) follows because BV maximizes over the residue; \(c\) only selects the triples and (B15.15) controls that selection pointwise.

### 6. From triple-prime incidences to distinct classes

In a dyadic prime interval \((x,2x]\), use the canonical lower boxes \(H<u,v\le z=x^{1/6}\). The progression
\[
 \ell\equiv-k^{-1}\pmod{4uv}                                \tag{B15.17}
\]
is reduced, forces \(\ell\equiv3\pmod4\), and is equivalent to \(uv\mid(k\ell+1)/4\). Its prime-count main term, summed over good triples, is at least
\[
 \frac{\operatorname{li}(2x)-\operatorname{li}(x)}4
 \sum_{\rm good}\frac1{uv}
 \gg x\log x\,h(\mathcal J).                              \tag{B15.18}
\]
Subtracting (B15.16) leaves the same order of positive mass.

No prime \(\ell\) is double-counted as a class. A collision between \((k,u,v)\) and \((k',u',v')\) gives \(\ell\mid uv'-u'v\), while
\(|uv'-u'v|<z^2=x^{1/3}<\ell\). Thus the determinant is zero, and reducedness gives \((u,v)=(u',v')\). If \(k\ne k'\), the common \(uv\) divides both \((k\ell+1)/4\) and \((k'\ell+1)/4\), hence divides \((k-k')/4\), impossible because
\[
 uv>H^2=K^{20}>K>|k-k'|/4.                                 \tag{B15.19}
\]
Thus even when the same prime appears for many triples, it contributes that many genuinely distinct Lemma-16.1 residue classes. Therefore (B15.18) is a lower bound for \(\sum_{x<\ell\le2x}f_c^{\rm good}(\ell)\), and
\[
 \sum_{x<\ell\le2x}\frac{f_c^{\rm good}(\ell)}\ell
 \gg \log x\,h(\mathcal J).                               \tag{B15.20}
\]
Summing the \(\asymp\log X\) dyadic intervals from \(X^{1/2}\) to \(X\) yields the lower half of
\[
 \sum_{X^{1/2}<\ell\le X}\frac{f_c^{\rm good}(\ell)}\ell
 \asymp(\log X)^2h(\mathcal J).                            \tag{B15.21}
\]

For the upper half, discard pruning and low \(\omega\). On \((x,2x]\), enlarge to \(u,v\le(2x)^{1/3}\). Brun--Titchmarsh applies to \(4uv\ll x^{2/3}\), with denominator \(\gg\log x\). The power-sized version of (B15.7), valid since \((2x)^{1/3}>K^{20}\), gives
\[
 \sum_{x<\ell\le2x} f_c^{\rm good}(\ell)
 \ll\frac{x}{\log x}\sum_{k,u,v}\frac1{\varphi(u)\varphi(v)}
 \ll x\log x\,h(\mathcal J).                              \tag{B15.22}
\]
Dyadic summation proves the upper half of (B15.21). Finally, for \(K=X^\kappa\) and the full family, the elementary estimate \(h(\mathcal K(K))\asymp\log K\asymp\log X\) turns (B15.21) into (34.19).

This completes my pre-comparison derivation of Theorem 34.8.

## Phase 2: comparison with the printed proof

The following grades use **REPAIRED** only for exposition/bookkeeping gaps; no repaired row changes a quantifier, range, or mathematical conclusion.

| Printed step | Grade | Audit |
|---|---|---|
| Lemma 34.7: expand \(r^2\), replace two divisibilities by \([k,k']\mid u+cv\) | CONFIRMED | Since \([k,k']\mid L_{\mathcal J}\), \((c,[k,k'])=1\); the congruence plus \((u,v)=1\) also forces \((uv,[k,k'])=1\). |
| (34.15): box main term and boundary | CONFIRMED | Direct summation gives \(\varphi(d)d^{-2}(\log z)^2+O(\tau(d)(\log z)^2/H)\), uniformly for \(d\le K^2\). No relative asymptotic for modulus \(d\) is being assumed. |
| (34.16): lcm-density sum | CONFIRMED | \(\varphi([k,k'])/[k,k']^2\le(k,k')/(kk')\), whose double sum is \(O((1+\log K)^3)\). |
| Lemma 34.7 boundary total | CONFIRMED | \(\tau([k,k'])\le2K\), so at most \(K^2\) pairs cost \(O(K^3(\log z)^2/H)=O(K^{-7}(\log z)^2)\). |
| Opening of Theorem 34.8: extend Lemma 16.2 to \(K\le X^\kappa\) | REPAIRED | The argument is correct. I added Shiu's actual source inequalities and a legal fixed choice \(\alpha=\beta=1/4\). The box error remains relative \(O(K^2/H)=O(K^{-8})\); Shiu only needs modulus \(k\), and \(k<K<U^{1/10}\) is far inside its range. |
| Lowest-block restriction \(\kappa<1/240\) | CONFIRMED | \(z\ge X^{1/12}\), while \(K^{20}\le X^{20\kappa}\); strict \(20\kappa<1/12\) gives \(z>K^{20}\) uniformly. It also gives \(\log(z/H)\asymp\log z\). |
| Pruning (34.20) | REPAIRED | The displayed Markov/Cauchy bound is exactly (B15.13). I made explicit that the theorem's required \(1\in\mathcal J\) gives \(h(\mathcal J)\ge1\), so the little-oh is uniform even for a one-element subfamily. |
| Multiplicity (34.21) | CONFIRMED | For each product \(uv\), coprimality gives at most \(2^{\omega(uv)}\) ordered allocations and pruning gives at most \(T_X\) multipliers per allocation. There is no residual factor \(K\). |
| Bombieri--Vinogradov error | REPAIRED | The printed sentence was compressed. I added \(q=4uv\le4x^{1/3}\), grouping by \(q\), maximization over reduced classes, and absorption of \((\log X)^{D\log2+4}\) by a larger fixed BV log saving. This is uniform in \(c\). |
| Dyadic lower bound and repeated prime \(\ell\) | REPAIRED | The lower proof uses \(u,v\le x^{1/6}\). I added the determinant bound \(|uv'-u'v|<x^{1/3}<\ell\) before invoking the cross-multiplier inequality \(uv>H^2>K\). Thus one \(\ell\) occurring for several triples supplies several distinct classes; it is not overcounted. |
| Brun--Titchmarsh upper bound | CONFIRMED | Enlarge to \(u,v\le(2x)^{1/3}\), so \(4uv\ll x^{2/3}\) and the BT denominator is \(\gg\log x\); (B15.7) gives \(O(x\log x\,h)\) per block. |
| (34.18)--(34.19) | CONFIRMED | There are \(\asymp\log X\) blocks, each lower and upper reciprocal mass is of order \(\log x\,h\), and the full family has \(h\asymp\log K\asymp\log X\). |

### Uniformity in \(c\)

There are only four appearances of \(c\). First, the lattice and incidence box counts use a reduced residue modulo \(k\) or \([k,k']\), uniformly. Second, Shiu is uniform in its reduced progression class. Third, pruning uses the pointwise incidence moment. Fourth, BV takes the maximum over all reduced residue classes and only uses \(c\) to select triples. No estimate averages over \(c\), and every constant is uniform for \((c,24L_{\mathcal J})=1\).

## Phase 3: §39 inheritance audit

### (a) Quantifiers for the data-dependent subfamily

After conditioning on the multiplier coordinates in Lemma 39.5, define
\[
 \mathcal J_c=\{k\le K:k\equiv1\pmod4,\ (k,c)=1\}.
\]
For every realized \(c\), this is a legitimate deterministic input to Theorem 34.8:

1. \(\mathcal J_c\subseteq\mathcal K(K)\).
2. \(1\in\mathcal J_c\), since \((1,c)=1\). This is exactly the hypothesis used in (34.20) to ensure \(h(\mathcal J_c)\ge1\).
3. Conditioning by \(S_y=1\), with \(y>3\), makes \((c,24)=1\).
4. If a prime \(p\mid L_{\mathcal J_c}\), some \(k\in\mathcal J_c\) is divisible by \(p\), so \((k,c)=1\) implies \(p\nmid c\). Hence \((c,L_{\mathcal J_c})=1\), including all prime powers in the lcm.
5. Reducing the revealed class modulo \(24L_K\) to one modulo \(24L_{\mathcal J_c}\) therefore supplies exactly the reduced \(c\) quantified in Theorem 34.8.

The theorem is uniform over *every* such \((c,\mathcal J)\); it does not require \(\mathcal J\) to be selected independently of \(c\). Thus data dependence after conditioning causes no quantifier reversal. Claim (a) is **CONFIRMED**.

### (b) Canonical-box and c-free inheritance

The statement (34.18) names all good Lemma-16.3 classes, but its lower proof uses, block by block, precisely
\[
 \ell\in(x,2x],\qquad H<u,v\le x^{1/6},
\]
with (39.3), then prunes only by \(r_{\mathcal J_c}(u,v;c)\le T_X\). These are exactly the canonical boxes (39.2), not mass imported from the larger cutoff \(u,v\le\ell^{1/3}\).

Every retained triple is an atom of the c-free unpruned family \(\mathcal A_X\): it has an allowed multiplier, the same canonical cutoffs, low \(\omega\), and \(4uv\mid k\ell+1\). In the fixed multiplier fibre \(c\), the active condition gives
\[
 c\equiv-uv^{-1}\pmod k,
\]
so the atom cylinder's \(k\)-coordinate is already the revealed coordinate and its remaining restriction is exactly the class \(-uv^{-1}\pmod\ell\) counted by \(f_c^{\rm good}(\ell)\). Lemma 16.3/39.1 distinctness makes those \(f_c^{\rm good}(\ell)\) genuinely distinct classes. Since \(\ell>K\), the prime coordinates are absent from \(L_K\) and independent after revealing the multiplier coordinates. Therefore
\[
 \Pr(H_X=0\mid c)
 \le\prod_\ell\left(1-\frac{f_c^{\rm good}(\ell)}\ell\right)
 \le\exp\left\{-\sum_\ell\frac{f_c^{\rm good}(\ell)}\ell\right\},
\]
and the inherited canonical-box lower proof supplies
\(\sum f_c^{\rm good}(\ell)/\ell\gg t^2h(\mathcal J_c)\). Claim (b) is **CONFIRMED**.

### (c) Lower bound for \(h(\mathcal J_c)\)

The condition \(S_y=1\) removes every prime \(p\le y\) from \(c\). A multiplier is omitted from \(\mathcal J_c\) only if it is divisible by some prime \(p>y\) with \(p\mid c\) and \(p\mid L_K\). For each such prime,
\[
 \sum_{\substack{k\le K\\p\mid k}}\frac{\varphi(k)}{k^2}
 \ll\frac{\log K}{p};                                      \tag{B15.23}
\]
indeed, writing \(k=pm\) and using \(\varphi(pm)\le p\varphi(m)\) reduces this to \(p^{-1}\sum_{m\le K/p}\varphi(m)/m^2\ll(\log K)/p\). Dropping the condition \(k\equiv1\pmod4\) only enlarges the sum.

Hence the union bound and \(h(\mathcal K(K))\ge c_0\log K\) give
\[
 h(\mathcal J_c)
 \ge c_0\log K-C\log K
   \sum_{\substack{y<p\le K\\p\mid L_K,\ p\mid c}}\frac1p
 =(c_0-CZ(c))\log K.                                      \tag{B15.24}
\]
Choosing the fixed \(\eta<c_0/(2C)\) gives \(h(\mathcal J_c)\ge c_1\log K\) whenever \(Z(c)\le\eta\). Primes not dividing \(L_K\) exclude no multiplier and are correctly absent from \(Z\). Prime powers cause no extra loss because coprimality is already decided by the underlying prime. Claim (c) is **CONFIRMED**.

Combining (a)--(c), the good canonical atoms give conditional mass
\[
 t^2h(\mathcal J_c)\gg t^2\log K\asymp t^3
\]
on every fibre with \(Z(c)\le\eta\). The exceptional set of other fibres is paid by (39.25). Thus the specific Theorem-34.8-to-Lemma-39.5 inheritance asserted in §39.7 item 2 is complete.

## Final verdict: CONFIRMED-AFTER-REPAIRS

I independently obtain Theorem 34.8 with all stated uniform quantifiers. The power-sized box errors are negligible because \(H=K^{10}\); Shiu's actual 1980 interval and modulus hypotheses survive with wide margin; the incidence second moment makes the discarded first moment uniformly \(o((\log z)^2h(\mathcal J))\); and the low-congestion multiplicity is only a fixed log power at BV level \(x^{1/3}\). The same-prime distinctness and both halves of (34.18)--(34.19) also close. The §39 data-dependent-subfamily, canonical-box, and \(h(\mathcal J_c)\) inheritance chain is valid. I found no mathematical break, but repaired three compressed pieces of §34 exposition (source-level Shiu hypotheses, the uniform role of \(1\in\mathcal J\), and explicit BV/canonical-box deduplication). This remains an internal check and does not upgrade the campaign's CLAIMED/PROVISIONAL register.
