# Second independent hostile cross-lab review: `notes/z79/ANALYTIC_PUSH.md`, §§2, 5–6, 8 (Opus 2)

Reviewer: Claude Opus (Anthropic). The author is GPT-6.2 Astra (OpenAI), so this is a cross-lab review.
Scope: the pointwise upper bounds for $R_M(n)=\#\{a,b,d\ge1: Mabd-a-b=n\}$:
* §2: $13/41$;
* §§5–6: $25/79$ (classical), $999/3157$ (Bourgain) and $6801/21497$ (TY Lemma 1.1 plus the B-transform);
* §8: the uniform-numerator bound (12) and the EPC-conditional $D^{4/13}$.

I also checked the interfaces with the twice-reviewed z78 §§7 and 13.

**Independence.** I read none of `data/z79/xreview/REVIEW_ANALYTIC_PUSH*_OPUS.md` until I had finished the audit, run my own scripts and fixed the verdict below. The comparison in §6 was written after that.

**Repository writes.** This file only. No commits. Scratch scripts are in `/tmp/opus2_6801/`.

## 1. Verdict

**ACCEPT.** I found no FATAL and no MAJOR defect. The MINOR items in §5 are all citation, wording or presentation fixes; none changes any exponent.

What is accepted:
* $R(n)\ll_\epsilon n^{6801/21497+\epsilon}$, i.e. $\approx n^{0.316370}$. This is PROVED relative to the z78 §§7, 13 reduction, Weil, uniform stationary phase (used twice), the divisor bound, the second derivative test and Trudgian–Yang Lemma 1.1 with the B-process.
* The fallbacks:
  * $999/3157$, needing only Bourgain's $(13/84,55/84)$;
  * $25/79$, with no exponent-pair input.

  Both beat $13/41$, and $13/41$ itself is correct.
* §8 (12), $R_M(n)\ll_\epsilon n^\epsilon[1+\min\{n^\theta M^{1-5\theta},(n/M^2)^{1/3}\}]$, holds for each of the three values of $\theta$.
* The EPC-conditional $R_M(n)\ll_\epsilon n^\epsilon(1+D^{4/13})$ is correct as stated: it is conditional and covers all $M$.

Together with the Round-2 Opus review, this is the second independent cross-lab review of §§5–6, so the STATUS gate's "two reviews for a claimed improvement of a published record" is met for the $6801/21497$ row. External priority is still unverified.

## 2. Line-by-line audit

### 2.1 Interface with z78 §§7, 13, and the squared budget (2)
* **Periodic shift plus Cauchy.** For each $(Q,\ell)$ this gives $|\sum_x G z|^2\le (WN/H^2)\sum_x|\sum_{i\le H}z(x+iQ)|^2$, using $\sum_{x\bmod Q}|G|^2\ll Q^2$ over $O(W/Q)$ periods.
* **Expanding the square.** The diagonal gives $NW\cdot W/H$ and the shifts give $NW\cdot H^{-1}\sum_h E_h$. Positivity is used *before* the conductor set is enlarged, which is correct.
* **Budget.** The identity $NW\,X^{\gamma-j}=X^{2t}$ is exactly $j=2(r+\gamma-t)$.
* **Pooling over $\ell$** (§5). The triangle inequality in $\ell$ and then Cauchy give
  $(L^{-1}\sum_\ell|A_{Q,\ell}|)^2\le n^\delta L^{-1}\sum_\ell|A_{Q,\ell}|^2$.
  The mean over $\ell$ is therefore legitimately kept. The dyad weight $(E/L)(S/H)$ gives the LP form $2(x-j+e-l)+\gamma+\hat y+b_0\le2(\gamma-j)$, which I re-derived.
* **The trace has already gone.** $E_{h,\ell}$ depends on $\ell$ only through the phase of $z_Q$, so no signed cancellation across arithmetic traces is used.

### 2.2 §2 ($13/41$)
* **Phase difference.** The phase of $z(x+hQ)\bar z(x)$ is exactly $X\ell h/(t^2-(hQ/2)^2)$ with $t=x+hQ/2$. This gives $T=X|\ell|h/W^2$, $Y=T/W$ and $s=(hQ/(2W))^2$. Poisson over $\mathbb Z+hQ/2$ produces the midpoint sign $e(mhQ/2)$, which is constant on each parity class of $Q$.
* **Order of inequalities.** Cauchy in $m$ over $O(Y)$ terms, then van der Corput in $Q$ with shift $2k$, $K\le N$ and weights $1-k/K$. The per-$m$ right-hand sides are real (sums of translated squares), so summing over $m$ before taking absolute values is valid.
* **Normalisation.** $E_h\le1+\sqrt{WY}D^{1/2}$, as stated.
* **Second derivative.** $F_{Q,k}=T(s_1-s_0)g(u)$ with $s_1-s_0=h^2k(Q+k)/W^2$, so $T(s_1-s_0)\asymp ZNk$ with $Z=Yh^2/W$. Since $\partial_u^2 G_s(u,0)=(4/9)2^{-4/3}u^{-2/3}>0$, we get $F''\asymp ZNk/Y^2$.
* **Derivative test and optimisation.** Titchmarsh Thm 5.9 gives $D\ll K^{-1}+(ZNK)^{1/2}/Y+(ZNK)^{-1/2}$. I recomputed $K_0=(Y^2/(ZN))^{1/3}$ and all five terms of (4).
* **Clipping.** $K_0<1\iff WY<h^2N$, in which case the trivial $\sqrt{WY}$ is at most the first term. $K_0>N\iff ZN^4<Y^2$, in which case the middle term is dominated by $N^{-1/2}$.
* **LP.** The four exponents are right. At vertex 1, $t/r\ge13/2$ gives $t=13/41$.

### 2.3 §5: signed pooling and midpoint signs
* I re-derived (5) from $(\sum_{\ell,m}|\sum_Q c|)^2\le EY\cdot(N/K)[EYN+\sum_I EINY\,D_I]$. The van der Corput constant is common to all $(\ell,m)$ because the supports in $Q$ coincide.
* The midpoint factors cancel exactly: $e(mh(Q+2k)/2-mhQ/2)=e(mhk)=1$. The second Poisson transform is therefore over integer $\nu$. Even without the cancellation, an integer linear phase in $m$ would only shift $\nu$ by an integer.

### 2.4 The two stationary phases (re-derived independently; high-precision check in `sp_check.py`)
**First phase.**
* $G_s=(y^2-s)^{-2}$ by the envelope theorem; numerically the relative error is $10^{-61}$.
* $y_s=(2/3)y^{-1}$, so $G_{ss}(u,0)=2y^{-6}-(8/3)y^{-6}=-u^2/6$.
* Hence $g=au^{4/3}-(s_0+s_1)u^2/12+O(\sigma^2)$ with $a=2^{-4/3}$. At 60 digits the ratios to the closed forms equal 1.

**Second phase.**
* From $g_0'=w$ we get $u_*=(3w/(4a))^3$. The critical value is $-(w/4)(3w/(4a))^3$, and $(1/4)(3/(4a))^3=(a/3)(3/(4a))^4=27/16=c$.
* The first-order perturbation by $-\varepsilon u^2$ gives $-B_0\varepsilon u_*^2$, which is the stated $c'$-term with $c'=(3/(4a))^6/48$.
* sympy confirms the following symbolically:
  * $T(s_1-s_0)=B_0$ and $w=\nu W/(h^2p_0)$;
  * $B_0w^4=X|\ell|\nu^4/(h^5p_0^3)$;
  * the sixth-power term $=X|\ell|\nu^6[Q^2+(Q+2k)^2]/(48h^7p_0^5)$;
  * $V_0=h^2U_0/W$, and $\Phi_0=-cBw_4(U_0/p_0)^3$ depends on $(Q,k)$ only through $p_0$;
  * the sextic term equals $B\sigma w_6$ times a smooth function of the row variables.
* **Remainder.** For $w\in\{0.6,1,1.4\}$ and $(s_1-s_0)/s_0\in\{0,0.5,1\}$, the ratio remainder$/\sigma^2$ converges as $\sigma\to0$ (for example $-0.5339\to-0.5262$, and $-1148\to-1017$). So the remainder is $O(\sigma^2)$ uniformly on the compact band. The constant grows steeply with $w$ but is absolute on a fixed band. $g''(u_*)>0$ throughout.
* **In-context test** (`poisson_ctx.py`). I summed $\sum_m\omega(m/Y)e(B_0g(m/Y))$ directly, with $\omega$ a smooth bump, and compared it with the $\nu$-sum of the stationary-phase predictions at $Y=3000$–$6000$, $B_0=4\cdot10^4$–$1.5\cdot10^5$ and $B\sigma$ up to $82$:

  | prediction used | discrepancy |
  |---|---|
  | exact critical value | $\le5\cdot10^{-4}$ |
  | formula (6) | $0.07$–$0.87$, consistent with $O(B\sigma^2)$ at $B\sigma^2\approx0.005$–$0.06$ |
  | quartic term only | $\approx10$–$13$ |

  The first row confirms the sign conventions and the extended-by-zero amplitude. The last row shows the sextic term is genuinely required and is correctly computed.
* **Errors.** The nonstationary and Hörmander errors, $O((1+B/Y)B^{-3/2})=O(B^{-1/2})$ after normalisation, are correct.

### 2.5 Farey bound (7), bins, Fourier and divisor step, kernel
* **(7).** Fix the reduced fraction on the smaller-height side. The partner fraction then lies in an $O(\eta)$ interval of $\gg D^{-2}$-spaced fractions. The lifting multiplicity is $EV_0/(D_1D_2)$, giving $A_0+\eta A_0D_1D_2\le A_0+\eta A_0^2$ per dyad.
  Brute force (`farey.py`; $E,V_0$ up to 400/200, $a_0=4,6$, $\eta=10^{-1}$ to $10^{-7}$ and $0$): count$/(A_0+\eta A_0^2)\le1.00$ throughout.
* **Bin freezing.** The residual $B\sigma|\delta|\psi\le B\sigma/J\le1$ has bounded row derivatives. The frozen term depends only on the row and the bin.
* **Fourier separation.** A smooth extension to a larger rectangle gives summable sample-dependent coefficients (three derivatives suffice in 2D). Hard cutoffs and parity stay in the row weights, and the sample set is a full rectangle independent of the rows.
* **Divisor step.** $|\alpha'_{p_0}|\le\tau(p_0)$ since $k\mid p_0$ fixes $Q$; brute-force check for $p_0\le6\cdot10^4$.
* **Cauchy in $p_0$.** It is done with the positive extension of the squared column sum. I re-derived the normalisation $D_I\ll B^{-1/2}+(V_0/\sqrt B)(JA_0^{-2}\sum_i\sum_{a,b\in i}|\mathcal K|)^{1/2}$ and checked it against the trivial bound.
* **Kernel.** $|\mathcal K(d)|\le\Lambda_1+\min(1,(B|d|)^{-1/2})$:
  * the exponent pair covers $B|d|\gtrsim U_0$;
  * the second derivative test covers $B|d|\lesssim U_0$.
* **Large-bin and decreasing-kernel terms.**
  * For $|d|\ge1/J$: $(J/A_0^2)(A_0+A_0^2/J)\Lambda\le J/A_0+\Lambda$, so the cross term $(J/A_0)\Lambda$ is kept correctly.
  * For $|d|<1/J$: the per-dyad cost is $J\eta\min(1,(B\eta)^{-1/2})\le(J/B)^{1/2}$, with the grouped bottom dyad also handled.
  * Hence (8).

### 2.6 Exponent-pair hypotheses
I fetched TY (arXiv 2306.05599v3) and checked the following.
* **Definition.** §1.1 (1.1)–(1.2) allows any $I=(a,b]\subseteq[N,2N]$, $f'$ near $yx^{-\sigma}$ with relative derivative error $c<1/2$ for $p\le P-1$, and $y\ge N^\sigma$. The bound is $(y/N^\sigma)^kN^\ell$.
* **Our kernel.** The phase $cBd\,U_0^3p_0^{-3}$, after conjugation, has $f'=y\,p_0^{-4}$ exactly, with $y=3|cd|BU_0^3$ and $\sigma=4$. So $y/N'^4\asymp B|d|/U_0$, and the normalised bound is $(B|d|)^\kappa U_0^{\lambda-\kappa-1}$.
* **The pairs.**
  * (1.3) with $\theta=13/84$ is Bourgain's $(13/84,55/84)$.
  * Lemma 1.1, last pair of (1.6): $(715/10238,7955/10238)$.
  * The B-transform (1.11) gives $(1418/5119,2917/5119)$; this is TY's hull vertex $k_{-4}$ in (1.14).
* **Optimality** (`hull.py`). Over the TY hull vertices $k_{-39}\dots k_{39}$, $k_{-4}$ maximises $z=(8-2\lambda)/(3+\kappa+\lambda)$ (next best is $k_{-5}$). So no other TY-known pair improves this certificate.
* **Publication.** TY is published: *Math. Comp.* 94 (2025) 1467–1502, doi:10.1090/mcom/3993. I found this by web search; I did not re-verify Lemma 1.1's proof.
* **$25/79$.** The second derivative test gives $(B|d|)^{1/2}/U_0\le B^{1/2}U_0^{-1}$ at all scales, so $25/79$ genuinely uses no exponent pair.

### 2.7 LP over the full polytope (`lp_check.py`, constraints re-derived from scratch, not copied)
**Quantities.** I wrote my own scale exponents and checked every constraint of the certificate:
* scales: $\hat y,\hat u=p+i,\hat f=\hat y+2x+\hat u-\gamma,\hat s=2(x+p-\gamma)$, $A_0=e+\hat f-\hat y$, and $J\in\{1,B\sigma\}$;
* the seven cost terms of (5), (8) and the additive 1;
* the detector, both zero modes, the $W/H$ budget, $L\ge1$, $H\ge1$ and $1\le K\le N$;
* the strict conditions $j+p<\gamma$, $2\gamma<1$ (or $<1+\mu$ in §8) and $\hat f+2\hat s<0$.

**Results.**
* **Exact check.** Rational arithmetic at the three $\mu=0$ vertices, the coalesced $\mu=1/3$ vertex and all 8 box corners: all pass for all three pairs, in both base $X$ (§6) and base $D$ (§8).
* **Strict margins.** The worst values are $\ge 2425/21497$ in absolute value (TY pair, both bases); for example $\hat f+2\hat s\le-3610/21497$.
* **Random sampling.** 150k uniform points per case over $(\mu,\alpha,\beta,\gamma,x,e,i)$: minimum slack $0$ (identities only), and no strict violation.
* **Binding.** At $\theta-10^{-6}$ the shift diagonal and the product-kernel term both go negative at the binding vertex, and nothing else does. This matches the note: the diagonal/kernel tie gives $z=(8-2\lambda)/(3+\kappa+\lambda)$ and $\theta=(8-z)/(25-3z)$, which I re-derived by hand.
* **Values.** $z=7/4,\ 281/160,\ 1951/1094$ give $\theta=25/79,\ 999/3157,\ 6801/21497$. The saving $13/41-6801/21497=620/881377$ is correct.
* **§2.** All four terms and the side conditions pass; at $13/41-10^{-6}$ the first term fails, so the threshold is sharp.
* **Weak inequalities.** The zero-slack (weak) inequalities only lose $n^{O(\delta)+o(1)}$, which goes into $\epsilon$. Only the strict side conditions need polynomial margins, and they have them.

**Replays.** `scripts/z79_analytic_{push,r2,r3}.py`, run under `ulimit -v 6000000; timeout 300`, reproduce `data/z79/analytic_push.txt`, `analytic_r2_lp.txt` and `analytic_r3_lp.txt` **byte-identically**.

### 2.8 §8
**Arithmetic strip.**
* $s=Mdk-n\equiv-n\pmod M$ on every detector point, so there are $O(1+V/M)$ values of $s$, each with $\tau((n+s)/M)$ pairs. Equivalently, the $(d,k)$ mass is $\sum_dV/(Md)\asymp V/M$.
* This sharpens z78 §13's lossy "mass $\ll Vn^\epsilon$". It gives the detector diagonal $(V/M)/P$ and the fibre bound $\min(U,W,1+V/M)$, so the volume is $UV_{\rm eff}W\asymp n/M^2=D$ and the bound is $n^\epsilon(1+D^{1/3})$.

**The $X$-numerator stays.** Poisson in $k$ has length $V/(Md)$, so $L=NW/V_{\rm eff}$, and the centre $k_0=n/(Md)$ gives the phase $-\ell X/(Qd)$ with $X=n/M=MD$. The only LP changes in base $D$ are therefore:
* $l=p+\gamma-\beta$;
* $\hat y=1+\mu+e+x-3\gamma$;
* the zero modes $\beta-p,\beta-\gamma\le t$ (no $\mu$);
* $T$-growth $1+\mu>2\gamma$.

**LP and exponents.** My independent LP passes for all three $\theta$ (§2.7). $D^t=D^\theta M^{1-3\theta}=n^\theta M^{1-5\theta}$, and $1-5\theta=-12508/21497$ for the final $\theta$. For $M>D^{1/3}$ we have $D^\theta M^{1-3\theta}\ge D^{1/3}$, and $n\le D^{5/3}$ in the analytic range.

**EPC argument.** Write $x=Qm+c$.
* The phase in $m$ has $f'=(\ell X/Q^2)(m+c/Q)^{-2}$, which lies in TY's class with $\sigma=2$, relative error $O(Q/W)$ and $y/N'^2\asymp Y'=\ell X/W^2\ge D^{1+\mu-2\gamma}\gg1$.
* EPC gives $(W/Q)^{1/2+\epsilon}$, and $\sum_c|G_c|\le Q^{3/2}$ then gives $|A|\ll n^\epsilon Q\sqrt W$.
* The budget $4r+\gamma\le2t$ at vertex 1 gives $t=4/13$, with no $\mu$-dependence.
* The statement is correctly labelled CONDITIONAL.

## 3. Independent verification summary
| check | tool | result |
|---|---|---|
| replays of the three z79 scripts | uv, ulimit/timeout | byte-identical to `data/z79/analytic_*` |
| $G_s,G_{ss},G_{uus}$, envelope | mpmath, 60 digits | exact to $10^{-20}$ or better |
| critical-value expansion (6), remainder $O(\sigma^2)$ | mpmath, 40 digits | ratio converges; $g''>0$ |
| (6) algebra in $X,\ell,\nu,h,p_0$; $p_0$-only quartic | sympy | all identities True |
| second Poisson, direct vs predicted | float sums, $Y\le6000$ | exact critical value $\le5\cdot10^{-4}$; (6) $O(B\sigma^2)$; quartic-only fails |
| Farey (7) | brute force | ratio $\le1.00$ |
| $|\alpha'|\le\tau$ | brute force, $p_0\le6\cdot10^4$ | pass |
| LP §2 / §6 / §8, vertices × corners | Fractions | pass, binding = diagonal + kernel |
| LP interior | 150k random points per case | no violation |
| TY hypotheses, B-transform, hull optimality | TY v3 text, exact arithmetic | pass; $k_{-4}$ is optimal over the TY hull |

## 4. Defects
**FATAL:** none. **MAJOR:** none.

**MINOR:**
1. **Citation.** Cite the published TY, *Math. Comp.* 94 (2025) 1467–1502 (doi:10.1090/mcom/3993), alongside arXiv v3. State that the final pair is the TY hull vertex $k_{-4}$ of (1.14). Optionally add that it maximises the objective $z$ over the TY hull, so the $6801/21497$ certificate is optimal among TY-known pairs. Newer exponent-pair work after TY was not examined.
2. **§8 "two changes".** The text says only two LP expressions change. The script also, correctly, drops $\mu$ from the zero-mode tests and uses $1+\mu>2\gamma$ for $T$-growth. Mention both in the sentence, since the text otherwise states only $O(V_{\rm eff}/N+V_{\rm eff}/W)$.
3. **§5 Fourier separation.** "(>2 derivatives suffice with suitable multivariate decay)" should say "three derivatives in each row variable give absolutely summable 2D coefficients".
4. **Uniformity of the $O(B\sigma^2)$ remainder in (6).** Note that its constant depends strongly on the fixed $w$-band. Numerically remainder$/\sigma^2$ ranges from about $0.5$ at $w=0.6$ to about $10^3$ at $w=1.4$. It is absolute once the band is fixed, which is all that is used.
5. **Notation overload persists**, as flagged before:
   * $D$: correlation in §2, $D_I$, effective volume in §8;
   * $J$: bins vs prime pairs;
   * $B$: scale vs transform;
   * $\sigma$: three meanings.

   This is not a mathematical issue.

## 5. Scope check
The note claims nothing about ES positivity, exceptional sets or cap scales, and §0 says so. "No exponent-pair input" must be restricted to $25/79$ at export, as §0 already instructs. $13/41$ and §§5–6 depend on z78 §§7, 13 (twice reviewed), not on the once-reviewed z78 §14 occupancy argument. The §8 gain is a power gain only for growing $M$; it gives nothing at $M=4$ and does not sum ET $c$-slices for free. All of this is stated correctly.

## 6. Comparison with Opus Rounds 1–3 (read after the verdict above was fixed)
* **Round 1 (§2).** Same conclusion. We agree on the order of Cauchy/vdC, $G_{uus}$, $K_0$ clipping and the sharp vertex threshold $t/r=13/2$. I have nothing new to add.
* **Round 2 (§§5–6).** Same verdict, "stands, no fatal defect". We independently agree on:
  * the normalisation of (5);
  * the constants $c,c'$;
  * the Farey proof;
  * the TY hypotheses;
  * the fact that $k_{-4}$ maximises $z$ over TY's hull (Round 2 also names $k_{-5}$ as next best, which I confirm).

  Of its defects, 1 (large-bin cross term), 3 (the $e(mhk)=1$ statement) and 4 (publication status) are addressed in the current text, apart from the journal citation. I have now verified that TY is published in *Math. Comp.* My additional contributions are the in-context numerical Poisson test of (6), the tightness test at $\theta-10^{-6}$, and the observation that the remainder constant depends strongly on the band.
* **Round 3 (§8).** Same verdict, accept. We agree on the congruence strip, the $V$-only-through-$V/M$ structure, the $X$-numerator, the EPC $4/13$ argument and the arithmetic. Its fixes 1–3 (M-exponent wording, explicit base-$D$ parameters, falsifier replay wording) are incorporated in the current text. My MINOR 2 is a small residue of its fix 2.
* **No disagreement** with any earlier Opus finding. This review independently confirms Round 2 for the $6801/21497$ record and Round 3 for §8.
