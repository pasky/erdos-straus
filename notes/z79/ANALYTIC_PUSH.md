## §0

Result: For every integer $n\ge2$, $R(n)\ll_\epsilon n^{13/41+\epsilon}$. Label: PROVED (rel. the z78 positive conductor enlargement, Weil, uniform stationary phase and the classical second derivative test).
Scope: Ordered positive words $4abd-a-b=n$, and the uniform numerator version in §2; upper bound only. No improvement to the ES or word exceptional-set exponents, no smaller pointwise cap scale, no full Type II count. ES in ℕ is open. External priority unverified.
Review: cross-model (`data/z79/xreview/REVIEW_ANALYTIC_PUSH_OPUS.md`, OpenAI author, independent Claude Opus reviewer; accepted §2 and the scoped §§1, 3 with form fixes incorporated).
Triage: RECORD (§2); §1 BARRIER-SCOPED and §3 NULL, no separate STATUS entries for those sections.
STATUS delta: In the pointwise upper-side row replace $46/145$ by $13/41$ (saving $1/5945$); in its uniform version replace the analytic term by $n^{13/41}M^{-11/41}$. The new proof uses z78 §§7, 13 but does not depend on the §14 occupancy proof. At export propagate the same exponent to the ES₅ ordered native word upper bound and to the $N_2$ comparison (still no saving when $U\asymp n^{1/4}$), as in z78 §13 and FRONTIER §3/§7. No change to the other analytic rows.

### 1. Exceptional sets: optimizing rather than truncating a Selberg square

**PROVED (rel. finite product orthogonality; one band only).** The following is an explicit test even of *optimally chosen*, possibly highly nonseparable Selberg coefficients. Condition on a CRT fibre where the pivot hits $X_i$ are independent Bernoullis of probabilities $0<p_i\le p_*<1$. Allow any family $\mathcal D$ of supports closed under taking subsets, including the empty set. Among all multilinear polynomials $P$ in the hits supported on $\mathcal D$ with $P(0)=1$, the least model expectation of $|P|^2$ is exactly

$$\bigg(\sum_{D\in\mathcal D}\prod_{i\in D}\frac{p_i}{1-p_i}\bigg)^{-1}.$$

Indeed the standardized centred products are an orthonormal basis of this space, by independence and triangular change of basis. Their squared evaluations at zero are the summands. Cauchy on coefficients gives the lower bound, and taking coefficients proportional to the conjugate evaluations gives equality. The same floor holds for sums of squares normalized by $\sum_j|P_j(0)|^2=1$. This is the classical mechanism behind Selberg's denominator; not a new unconditional exceptional-set theorem.

If the pivots have log-size $\asymp t$ and *each support* is limited to log-product $O(\lambda)$, $\lambda=\log N$, its size is at most $k=\lfloor C\lambda/t\rfloor$. Grant exact evaluation of the square (even its cross terms), with no interval error. Under a supply $\sum p_i\ll t^d$ the negative log of the optimal mean is at most $O(\lambda^{d/(d+1)})$, **even allowing $k\ll\sum p_i$**. In fact with $a=\sum p_i/(1-p_i)\ll t^d$ the denominator is $\le\sum_{j\le k}a^j/j!$. For $t\le\lambda^{1/(d+1)}$ use $e^a$; for larger $t=z\lambda^{1/(d+1)}$ use $\sum_{j\le k}a^j/j!\le e^{s a}s^{-k}$ with $s=\min(1,k/a)$ for $k\ge1$. This gives $O(\lambda^{d/(d+1)}(1+\log z)/z)$ in the log (or use monotonicity in $a,k$ before optimizing); $k=0$ is immediate. Thus replacing Bonferroni by a quadratic or fourth moment or an optimized Selberg square evaluated solely in this product law and band is not the missing gain. The membership of particular schemes requires the named hypotheses, in particular $p_*<1$ uniformly. No lower bound on true exceptions or on general moment/dispersion methods follows.

**Assessment.** For cubic ES supply and quadratic word supply compare `paper/sieve-limits-note.tex`, `EXSET_BEYOND_CRT.md`, `notes/z75/ANALYTIC_PUSH2.md` and z78 §10. The above test grants *more* than replacing BV by EH, or a constant level gain on smooth moduli: changing $C$ cannot change the power. In the interval transfer there is also the independent cost of summing rounding errors over atom tuples; the obstruction is not just a BV error term. The full $3/4$ estimate was claimed earlier by Kandukoori–Ramesh–Kumar Thm 1; the internal note shares this architecture but differs in details. We have no deduction from standard EH/BFI alone improving $3/4$ or $2/3$. A dispersion result addressing the exceptional population itself (for example the common character bias in `EXSET_CHAR_FORCING.md` §5), rather than changing a level in the product calculation, would be a different input.

### 2. Pointwise words: a short second conductor difference

**PROVED (rel. the inputs in §0).** For integers $n\ge2, M\ge1$, put $R_M(n)=\#\{a,b,d\ge1:Mabd-a-b=n\}$, so $R=R_4$. Then

$$ R_M(n)\ll_\epsilon n^\epsilon\min\{n^{13/41}M^{-11/41},(n/M)^{1/3}\}. \tag{1}$$

We avoid the arc count in z78 §14 altogether. The second difference is taken in the **enlarged conductor** $Q$, not between unrelated trace functions. Its dual curvature is smaller by the shift/conductor ratio than in an unrestricted square. There is no exponent pair or monomial-spacing input.

**Reduction (PROVED rel. `notes/z78/ANALYTIC_WILD.md` §§7, 13).** Set $X=n/M$. On a dyadic block $a\asymp U\le V\asymp b,d\asymp W$ (up to endpoint symmetry), $UVW\asymp X$. Fixing any one variable costs $O_\epsilon(n^\epsilon)$ by divisors, so the fibre bound is $n^\epsilon\min(U,V,W)$; see §13 there, including bounded $X$. Use detector primes in $(P,2P]$, write $N=P^2$ **only in this section**, $L=MNW/V$. The non-oscillatory terms cost $O_\epsilon(n^\epsilon(1+V/P+V/(MN)+V/(MW)))$. We recall precisely the squared budget for the rest: up to $n^{O(\delta)+\epsilon}$, for each $1\le |\ell|\le L n^\delta$ it suffices to bound

$$ NW\left(W/H+H^{-1}\sum_{1\le h<H}E_h\right). \tag{2}$$

Here $HN\ll W$ and $E_h$ is the absolute value of a *signed* $N^{-1}\sum_{N\le Q\le4N}\sum_x z_Q(x+hQ)\overline{z_Q(x)}$. Specifically the $Q=pp'$ trace has already disappeared: periodic shifting by $Q$ and Cauchy bound its squared weighted sum by $(NW/H^2)\sum_x|\sum_{i\le H}z_Q(x+iQ)|^2$, a nonnegative quantity that may be averaged over all conductors at log-squared cost. Then expand in $i$ to obtain (2). The primal reciprocal phase (cycles rather than radians) in $z_Q$ is $-\ell X/(Qx)$, with smooth weight on $x\asymp W$ and bounded scaled derivatives, including when $\ell/L$ is large by Schwartz decay. The frequency sum has the $1/L$ normalization. This uses the local Weil/zero-mode bounds of z78 (also at primes dividing $M$), not an estimate for arbitrary mock trace products in a mixed-$c$ Cauchy norm.

**Exact dual phase (PROVED rel. stationary phase).** For fixed $h,\ell$ take $A=X|\ell|h$, $Y=A/W^3$, $T=WY$, $s=(hQ/(2W))^2$. Up to conjugation, Poisson in $x+hQ/2$ gives the stationary phase $T G(u,s)$, $u=m/Y$, where

$$G(u,s)=(y^2-s)^{-1}+uy,\qquad \partial_y[(y^2-s)^{-1}+uy]=0.$$

Here $y$ denotes the positive stationary point in the fixed compact range corresponding to $u\in[c_1,c_2]\subset(0,\infty)$, including a neighbourhood of the weight support. More precisely use z78 §7 (Hörmander, *Analysis of Linear Partial Differential Operators I*, Thm 7.7.5): off band the sum of errors is negligible by integration by parts ($T$ grows by a fixed power even at the smallest frequency); in band the error $O(W/T)$ per $m$ totals $O(1)$ when $Y\gg1$. If the band has no integer, only the off-band bound is needed. The remaining contribution after triangle in $m$ and splitting $Q$ by parity is bounded by a sum of two expressions

$$\frac{W}{N\sqrt T}\sum_{m\asymp Y}\left|\sum_{Q\ \mathrm{of\ one\ parity}} b(m/Y,Q/N)e(TG(m/Y,s_Q))\right|. \tag{3}$$

The midpoint sign $e(mhQ/2)$ is constant across the fixed parity for each $m$. The amplitude includes the stationary Jacobian; it has bounded modulus and bounded $u$-derivative uniformly by implicit differentiation on the compact band, with $HN/W=o(1)$. This does not require a bounded quartic residual. We use $e(x)=\exp(2\pi i x)$.

**Correlation estimate (PROVED rel. classical van der Corput).** Write $Z=Yh^2/W$. For any $1\le K\le N$ (integer), Cauchy in $m$ in (3), then the finite shift inequality in the conductor index of a fixed parity (shift $2k$, $1\le k<K$), bounds $E_h$ by $O(1)+O(\sqrt{WY}\,D^{1/2})$ with

$$ D\ll K^{-1}+\frac1{KNY}\sum_{1\le k<K}\sum_{Q}\left|\sum_m b_{Q,k}(m/Y)e(F_{Q,k}(m))\right|,\quad F_{Q,k}=T[G(u,s_{Q+2k})-G(u,s_Q)]. $$

Only $Q,Q+2k$ in the same conductor interval are included. To see the normalization, the shift bound for each $m$ costs $O(N^2/K)$ on the diagonal and $O(N/K)$ times the sum over $k$ of the correlations; **sum the real correlations over $m$ before taking absolute values** (retain their weights $1-k/K$). This is legitimate directly by expanding the nonnegative translated square, not by summing individual absolute-value bounds for each $m$. Each $b_{Q,k}$ is a product of two amplitudes of (3), with total variation $O(1)$ in $m$.

At $s=0$, $y=(2/u)^{1/3}$, $G_s=(y^2-s)^{-2}$ by stationarity. Consequently $G_{uus}(u,0)=(4/9)2^{-4/3}u^{-2/3}$ is positive and bounded away from zero on the compact band. By smoothness this persists for $s=o(1)$ uniformly. The fundamental theorem of calculus in $s$, with $s_{Q+2k}-s_Q\asymp h^2Nk/W^2$, now gives

$$F''_{Q,k}(m)\asymp ZNk/Y^2>0.$$

This is for the **exact** phase difference, not a differentiated pointwise asymptotic or an assumption of cancellation between different arcs. Use Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., Thm 5.9, p.104 (statement also checked in `data/z55/xreview/REVIEW_TDO.md`): on intervals of length $D_0\ge1$ with $\lambda\le F''\le c\lambda$, one has $O_c(D_0\sqrt\lambda+1/\sqrt\lambda)$. Subintervals of length $<1$ cost $O(1)$; for $Y\gg1$ this is absorbed by $\sqrt{ZNk}+Y/\sqrt{ZNk}$ by AM–GM. Partial summation gives the same latter bound with the weights. Therefore, summing $k^{\pm1/2}$, then taking square roots,

$$ E_h\ll 1+\sqrt{WY}\{K^{-1/2}+(ZNK)^{1/4}Y^{-1/2}+(ZNK)^{-1/4}\}. $$

Clip $K_0=(Y^2/(ZN))^{1/3}$ to $[1,N]$ and round within a constant factor. If $K_0<1$ use the trivial $1+\sqrt{WY}$ (already paid by the first optimized term); if $K_0>N$ pay the upper-endpoint terms. We obtain uniformly, also with just the nonstationary error for sufficiently small $Y$,

$$ E_h\ll 1+(WYh)^{1/3}N^{1/6}+W^{2/3}Y^{1/6}h^{-1/3}N^{-1/6}+ (WY/N)^{1/2}+W^{3/4}Y^{1/4}h^{-1/2}N^{-1/2}. \tag{4} $$

**Global optimization (PROVED rel. (2)–(4)).** In the analytic range $0\le\mu=\log M/\log X\le1/3$ (large $X$), set $\theta=13/41$, $t=\theta+(1-3\theta)\mu$. Write $\alpha,\beta,\gamma$ for block exponents of $U,V,W$ to base $X$, normalizing their sum to 1 up to $O(1/\log X)$. Use fibres when any is below $t$. On the remaining triangle put $r=\beta-t$, $j=2(r+\gamma-t)$, $P=X^r\log^3(2n)$, $H=\lceil X^j\rceil$. Then $W/H$ in (2) fits, the exponent of $N$ is $2r+o(1)$, and the maximum $Y$ has exponent at most $d=1+\mu-\beta+2r+j-2\gamma$ plus $O(\delta)+o(1)$. After bounding $Y$ by its maximum and averaging $h^{\pm1/3},h^{-1/2}$ (costs $O(H^{\pm1/3}),O(H^{-1/2})$ respectively), the exponents in (4) besides 0 are

$$ (\gamma+d+j+r)/3,\quad (4\gamma+d-2j-2r)/6,\quad (\gamma+d)/2-r,\quad (3\gamma+d-2j-4r)/4.$$

All must fit $\gamma-j$ in (2). At $\mu=0$, $\alpha=\gamma=t,\beta=1-2t$ one has $d=4r,j=2r$, so the first term requires $(t+7r)/3\le t-2r$, precisely $t/r\ge13/2$. The other three slacks here are $1/41,1/82,5/164$. The exact vertex certificate `scripts/z79_analytic_push.py` checks these four inequalities, the constant, $\gamma>j+2r$ for short shifts, $1>2\gamma$ for polynomial growth of $T$, $\mu+2r+\gamma-\beta\ge0$ for $L\gg1$, and the two zero modes. It checks all three vertices (even without $\alpha\le\beta$) at $\mu=0$, and the coalesced vertex at $\mu=1/3$. Affineness of all inequalities and of the vertices in $\mu$ suffices on the whole region. Strict margins absorb log factors where needed; weak bounds permit $n^{O(\delta)+o(1)}$, with $\delta$ chosen after $\epsilon$, $X\le n\le X^{4/3}$. Dyadic summation gives $X^t=X^\theta M^{1-3\theta}$ up to $n^\epsilon$. For $M>X^{1/3}$, $X^{1/3}\le X^\theta M^{1-3\theta}$ and fibres alone suffice (no solutions for $X<1/6$). This proves (1). In particular this improves $46/145$ by exactly $1/5945$, not past $3/10$.

### 3. Cap: what single planting buys at polynomial height

**PROVED (rel. z75 Gallagher–Linnik dichotomy, z78 parity packet and Minkowski II).** In the hard radical branch $R=\operatorname{rad}(n)$ (all prime factors $1\bmod8$), use two disjoint blocks of the first $2k$ primes $3\bmod4$. Put $D_i=4\prod_{v\in S_i}v$, $Q=R\max D_i$, $X=Q^A$ with the sufficiently large effective absolute $A$ of `notes/z75/ANALYTIC_BREAK.md` §3. Impose the unit class $q=-R\bmod D_i$ and $(q/R)=-1$. The full z75 §3 Gallagher argument applies without any imposed valuations at $v^2$ or $v^3$: the character expansion still has norm one and individual coefficients of modulus $1/(2\varphi(D_i))$, and the optional twist is by the **whole** primitive $\chi_R$. Disjointness away from 4 leaves only the harmful common exception $\chi_{-4}\chi_R$ (positive coefficient). In the absence of a harmful exception one block therefore has $\gg X/(\varphi(D_i)\log X)$ admissible primes. A count of one least prime would not suffice.

More precisely in this ordinary/harmless case, take $u_0=A\log R$, $k=\lfloor2\sqrt{u_0/\log u_0}\rfloor$. Both blocks have $\log D_i=k\log k+O(k\log\log k)$ by fixed-modulus PNT; $u=\log X\sim u_0$. The z78 §4 log-height deletion and parity packet (the negative carrier may lie inside $S_i$) give log-cap $\log(1+e^*(n))\le 2u/(k+1)+\log D_i+O(k+\log u)\le(2+o(1))\sqrt{u\log u}$. At the same $A$ a cubic-modulus absolute-deletion budget with main-term prime supply would instead have optimized coefficient $2\sqrt3$ in $u$-units (minimize $2/b+3b/2$). These are constants of numerical certificates at the indicated height, **not** a numerical absolute constant for Gallagher's theorem or for all inputs. In the harmful exceptional case apply the original z75 §2 alternative (with its original small-nonresidue cutoff): either Linnik's planted carrier already gives $\log(1+e^*)=O(\sqrt{u\log u})$, or the exceptional prime count loses a factor at worst $\exp(-O(\sqrt{u\log u}))$. The same sup-norm deletion and packet then still give $O(\sqrt{u\log u})$, without the leading constant. The packet only gives a rational last denominator with odd square reduced denominator, root coprime to $R$ and supported on the second denominator. Scaling from $R$ to $n$ preserves the cap. Nonhard radicals have a classical cap-zero factor.

**Assessment.** Thus single planting ports, but does not on its own remove the unconditional $\sqrt{\log\log R}$ factor. At GRH height the ordinary absolute-deletion budget has the same cost in $u=\log X$, with $u\sim2\log_2 R$ instead. The uniform relative-deletion estimate in z78 §15 remains missing; polynomial-height Gallagher equidistributes primes, not the prime divisors of short-relation differences. No uniform improvement to either cap scale here.

### 4. Falsifier Table and FRONTIER §4 checklist

|Screen|Test and outcome (CERTIFIED finite checks / Assessment of scope)|
|---|---|
|F1: odd squares|Direct $R_4=0$ for odd squares $3^2$ through $79^2$. (1) is one-sided; §3 does not require a negative Jacobi symbol at an unreduced square.|
|F2: numerator 8|Direct $R_8(131)=R_8(241)=0$; the full three-positive-integer numerator-eight failures there are controls from FRONTIER §4, not inferred from $R_8$. At $1,590,284,203,561$ the archived independent word check `data/z76/disproof/comp/pycheck.txt` has $R_8=0$, but $R_4>0$. No numerator-eight positivity is predicted.|
|F3: composites|Direct $R_4(4545)=0$ and no $U_7$ hit at any of $105,1465,3865,4545,10305,12145,39361,67425$. Upper bounds and capped radical scaling do not fill these holes.|
|F4: known (★)-zeros|Direct $R_4=0$ at all 14 prime controls $409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281$, also at composite $17401609$. No lower tail at a fixed prime inferred.|

**CERTIFIED (single new finite replay; not a census):** `ulimit -v 6000000; timeout 180 uv run --offline --no-project python scripts/z79_analytic_push.py` → `data/z79/analytic_push.txt`. The word test uses $a\le b$, hence $Ma^2\le n+2a$, then enumerates the smaller of $d,b$ by $(Mad-1)b=n+a$. The $U_7$ test checks $f=7\bmod8$, $r=-n\bmod f$, $0<r\mid f+1$ up to $2n+1$ (beyond this $r=f-n>(f+1)/2$ and $r<f+1$; this is the divisor-target definition of $U_7$ in `Z60_LOPEZ.md` §2, not a test for full ES). The trillion-scale control is cited, not rerun.

**Assessment (remaining FRONTIER §4 screens).** For items 3–7: no numerator transport of solutions, no untied positive main term, no pointwise assertion from an average over input primes. In (2) the input is fixed, the averages are over detector primes, Fourier index, conductor, shift and dual index; (4) uses absolute upper bounds. For items 8–13: neither residue-shape forcing, parity-to-class inference, off-shift pooling of prime factors, sign reflection, transport from a relaxation, nor a Brauer–Manin local-global assertion is used. For items 14–19: the controls above allow near-squares and Mordell classes without exception; there is no thin-family transfer, bounded-factor cover of a target, external-PID logic or new étale obstruction.

**Assessment (Round 2 target, not an estimate).** In the binding block of (4), $K\asymp N^{3/4}$, $Y\asymp N^2$ in exponent arithmetic. After a second Poisson transform in $m$, the length at shift $k\asymp K$ is $ZNk/Y$; the leading dual phase is quartic in that integer (Legendre transform of $m^{4/3}$). The second derivative bound counts these critical points in absolute value. Keep their signs and the $Q,k$ average instead: this targets the only equality in the $M=4$ LP. It does not require assuming independence of the floor bins and is not yet an estimate.
