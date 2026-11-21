# Second independent hostile review (Claude Opus, "Opus2"): `ANALYTIC_WILD.md` §14, $R(n)\ll_\epsilon n^{46/145+\epsilon}$, and θ = 46/145 in (12)

Reviewer: Claude Opus (Anthropic). The author is GPT-6.2 Astra, so this is a cross-lab review. It is independent: I did
not open `REVIEW_ANALYTIC_WILD_R4_OPUS.md` until §§1–6 below and the verdict were written.
Audited: `notes/z78/ANALYTIC_WILD.md` §0, §§7–8, §§11–14 (state at 14d32c799), `scripts/z78_analytic_r4.py` and
`data/z78/analytic_r4_lp.txt`. §15 is outside the scope of this review.

## Verdict: **ACCEPT** (minor wording fixes only)

I found no FATAL or MAJOR defect. I re-derived every constant, power and LP constraint of §14 from the raw scales. An
independent script that assumes no monotonicity reproduces the exponent exactly: slack 0 at the binding vertex, a failure
at $46/145-10^{-4}$, and a pass at $46/145+10^{-4}$. The uniform-numerator statement (12) with θ = 46/145 also holds, and
the margin needed to absorb $\epsilon,\delta$ is uniform in μ.

The five things I attacked hardest all hold:
* small $S$;
* small $Y$ (including the $Y^{-1/6}$ in the fifth term);
* $D<1$ intervals;
* the $h$-interval length;
* the cross-$h$ Abel and Hölder step.

With R4_OPUS this gives §14 its two independent cross-lab reviews, as AGENTS §3 requires. External priority is still
unverified. ES is open.

## 1. Interfaces with §§7–8 and §§11–13

**Target.** I checked $|\sum_xGz|^2\ll W^2N/H+WN\cdot H^{-1}\sum_{h<H}E_h$.
* Taking $j=2(r+\gamma-t)$ makes the diagonal exact.
* The off-diagonal target is $2t-\gamma-2r=\gamma-j$.
* The $O(1)$ terms need $\gamma+2r\le 2t$. This is the script's `g+2*r<=2*t`.

**Scales.**
* $Y=n|\ell|h/(4W^3)$, so $Y_{\max}=n^d$ with $d=1-\beta+2r+j-2\gamma$, using $|\ell|\le NW/V\cdot n^\delta$.
* $T=WY$, $\sigma=hQ/(2W)\asymp SN/W$ and $Z=YS^2/W$.

**$\xi$ is exact.** From the §12 expansion, $T\,y_0^{-4}\sigma^2$ with $y_0=(2Y/m)^{1/3}$ gives
$\xi=Y^{-1/3}m^{4/3}h^2/(2^{4/3}\cdot4W)$. Because $Y\propto h$ at fixed $\ell$, this is $\xi=c\,h^{5/3}m^{4/3}$ with
$c=c(n,\ell,W)$ independent of $(h,m)$. It agrees with §7's $\xi_m=Ah^2/(4W^4)(m/2Y)^{4/3}$. The $Q^2$ coefficient
receives no $\sigma^4$ contamination.

**ζ.** $T\cdot\frac13y_0^{-6}\sigma^4=m^2h^4/(192\,YW^3)=m^2h^3/(48n|\ell|)$. Hence $|\zeta|=c'h^3m^2$, and
$c'c^{-3/2}h^{1/2}\xi^{3/2}=c'h^{1/2}h^{5/2}m^2$ ✓. Both $c$ and $c'$ are constant on the whole $(h,m)$ block at fixed
$\ell$. The sign of ζ is fixed once $\ell>0$ (conjugate otherwise).

**$\xi\asymp Z$ and the stationary band.** These are inherited unchanged. The band $m\asymp Y_h$ moves with $h$ by at most a
factor of 2 within a dyadic block, and that is harmless.

**Parity.** For odd $h$ the dual sign depends only on $m$ and on the parity class of $Q$. It is pulled out before the
absolute value in $m$ ✓.

**§13.** With base $X=n/M$, $A=X|\ell|h$ and $L=MNW/V$, the only change is $d\to d_*=1+\mu-\beta+2r+j-2\gamma$. The
quantities $c$ and $c'$ change but stay $(h,m)$-independent.

*Hostile slip I made and corrected:* my first script draft added μ to $\log Y$ **and** to $\log L$. That double count
appears to break $R_M$ for μ ≥ 1/15. It is my error: μ enters only through $L$, exactly as the note says.

## 2. Common bins and (13)

**Bin count.** The value $N^4|\zeta|\asymp T\sigma^4\asymp WY(SN/W)^4=YS^4N^4/W^3=Z(SN^2/W)^2$, which is the same quantity ✓.
Width-one bins in this value are $O(J)$ in number.

**Freezing.** At the midpoint, $|(\zeta-\zeta_i)Q^4|\le 256\cdot\frac12$, and $Q\partial_Q$ of the residual is also $O(1)$. The
sextic remainder satisfies $T\sigma^6\asymp T(SN/W)^6\ll1$, and its scaled derivative is likewise bounded (§12 smooth
remainders) ✓.

**Order of operations.** These steps are all legitimate, in this order:
* For each $h$: $E_h\le \frac{W}{N\sqrt{T_h}}\sum_m|\sum_Q w_{hm}(Q/N)e(\text{res}_{hm})e(\zeta_iQ^4+\xi_{hm}Q^2)|+O(1)$.
* Abel in $Q$ with the common partial sums $S_{hm}(u)=\sum_{N\le Q\le u,\ \text{parity}}e(\zeta_iQ^4+\xi_{hm}Q^2)$ gives
  $\sum_{hm}|\cdot|\ll\sum_{hm}|S_{hm}(4N)|+N^{-1}\!\int\!\sum_{hm}|S_{hm}(u)|\,du$. This uses
  $\sup|w|+N\sup|\partial_Q(w\,e(\text{res}))|\ll1$.
* Hölder over the $O(SY)$ pairs is applied at each fixed $u$.

**Fourth moment.** For bin $i$, $S^2=\sum_{s\le32N^2}b_se(\xi s)$, where $b_s$ sums the common unimodular weights
$e(\zeta_i(Q_1^4+Q_2^4))$ and has $|b_s|\le r_2(s)\le4\tau(s)$. Greedy colouring of $\{\xi_{hm}\}_{\rm bin\ i}$ into $O(D_i)$ classes
that are each $N^{-2}$-separated, followed by Montgomery–Vaughan, gives $\ll D_iN^{4+\epsilon}$ uniformly in $u$. No extra
factor arises: $D_i$ is exactly the colouring degree. Summing over bins gives $N^{4+\epsilon}\sum_iD_i$.

**Prefactor.**
$S^{-1}\cdot\frac{W}{N\sqrt{WY}}(SY)^{3/4}N^{1+\epsilon}(\sum_iD_i)^{1/4}=W^{1/2}Y^{1/4}(S^{-1}\sum_iD_i)^{1/4}$. This is (13),
with every power of $S,Y,W,N$ checked. $T$ enters only through $\sqrt{T}=\sqrt{WY}$. The individually maximizing arcs need
not coincide, and the argument never uses them jointly ✓.

## 3. Occupancy (14), all cases

**Case $Z\ll1$.** $J-1=Z(SN^2/W)^2\ll1$, so there are $O(1)$ bins and $O(1)$ values of $v$. Per $h$ the §7 spacing
($\partial_m\xi\asymp Z/Y$) gives $O(1+\Delta)$ values, so $S^{-1}\sum D_i\ll1+\Delta$ ✓.

**The $h$-interval for $Z\gg1$, at fixed $(i,v)$.** Write $G(h,\xi)=N^4c'c^{-3/2}h^{1/2}\xi^{3/2}\asymp J-1$.
* $\partial_hG=G/(2h)\asymp(J-1)/S$.
* $\partial_\xi G=\frac32G/\xi\asymp(J-1)/Z$.

Replacing ξ by $v+\eta$ (arc length $N^{-2}$) shifts $G$ by
$O((J-1)/(ZN^2))=O\big((SN^2/W)^2N^{-2}\big)=O((SN/W)^2)$. This is an **identity**, not just a bound. It is also
$\le O(N^{-2})$ because $SN^2/W\ll1$. In particular it is $\ll1$.

**Hostile check on the worry raised in the brief.** The case $SN^2/W\ll1$ only makes this smaller. There is no trap,
because $J/(ZN^2)\le1/(ZN^2)+(SN/W)^2$.

$G(\cdot,v+\eta)$ is monotone, so the admissible $h$ form a single interval of length $O(S/(J-1))$ when $J-1\gg1$, and the
whole block otherwise. Wrapping arcs are handled by a lifted centre ✓.

**The $m$-window.** $m=f(h)\,(1+O(1/(ZN^2)))$ with $f(h)=c^{-3/4}(v+\eta)^{3/4}h^{-5/4}\asymp Y$. The width is
$O(Y/(ZN^2))=O(\Delta)$ ✓.

**Trivial branch** ($\Delta\gg1$, or $Y\ge S^3$).
* The count is $\sum_{i,v}(|I_{iv}|+1)(1+\Delta)\ll(ZS+JZ)(1+\Delta)$.
* This becomes $Z(1+\Delta)$ after dividing by $S$, since $J\ll S$ (from $(J-1)B/S\ll1$, $B\ge1$).
* That is $\ll Y/N^2$ when $\Delta\gg1$, and $\ll Z(Y/S^3)^{1/7}$ when $Y\ge S^3$ ✓.

**Erdős–Turán branch** ($\Delta<c_0$, $Y<S^3$).
* Each $h$ has at most one $m$, and the condition is $\|f(h)\|\le C\Delta$.
* $f'''=-\frac{585}{64}c^{-3/4}(v+\eta)^{3/4}h^{-17/4}$, so $|lf'''|\asymp lY/S^3$.
* The comparability ratio is $2^{17/4}$, independent of $v,l,h$.
* Titchmarsh Thm 5.11 needs only $b-a\ge1$ and a fixed ratio. For $|I|<1$ the count is $O(1)$, and this
  produces the $JZ\log B/S$ term.

The sum over $l\le B$ with weights $1/l$ gives:
* the $D\lambda^{1/6}$ part: $|I|(BY/S^3)^{1/6}$;
* the $D^{1/2}\lambda^{-1/6}$ part: $|I|^{1/2}(S^3/Y)^{1/6}\sum l^{-7/6}\ll (S/J)^{1/2}S^{1/2}Y^{-1/6}$.

Multiplying by the $O(JZ)$ intervals and dividing by $S$ gives $J^{1/2}ZY^{-1/6}$, **exactly as claimed**. The $l$-sum
converges, and $D<1$ intervals are already counted in $JZ/S$.

**Balance.** $B=(S^3/Y)^{1/7}\le S^{3/7}$. The term $JZ/S\ll Z/B$ holds because $J/S\le 1/S+(J-1)/S\ll1/B$ ✓.

## 4. LP: all five exponents, every regime

Fix $\ell=n^\lambda$ and $S=n^s$. Then $y=1+\lambda+s-3\gamma$ (for μ = 0), $z=y+2s-\gamma$, $\log\Delta=\gamma-2s-4r$ and
$\log(J-1)=\gamma+y+4(s+2r-\gamma)$. Including the weight $S/H$, the five terms of (13)×(14) have exponents:

| term of (14) | exponent of $(S/H)W^{1/2}Y^{1/4}(\cdot)^{1/4}$ | coeff. of $y$ | coeff. of $s$ |
|---|---|---|---|
| 1 | $\gamma/2+y/4+s-j$ | 1/4 | 1 |
| Δ | $3\gamma/4+y/4+s/2-r-j$ | 1/4 | 1/2 |
| $Y/N^2$ | $\gamma/2+y/2-r+s-j$ | 1/2 | 1 |
| $Z(Y/S^3)^{1/7}$ | $\gamma/4+15y/28+39s/28-j$ | 15/28 | 39/28 |
| $J^{1/2}ZY^{-1/6}$, $J\asymp1$ | $\gamma/4+11y/24+3s/2-j$ | 11/24 | 3/2 |
| same, $J\asymp J-1$ | $7y/12+2s+r-\gamma/8-j$ | 7/12 | 2 |

**Small $S$ and small $Y$ cannot hurt.** Every coefficient is positive, so the maximum is at $s=j$, $\lambda=\lambda_{\max}$
($y=d$). In particular, the $Y^{-1/6}$ in the fifth term is outweighed by $Y^{1/4}\cdot Z^{1/4}\ni Y^{1/4+1/4}$; the net is
$Y^{11/24}$.

At the corner these exponents reproduce the note's list:
* $\gamma/2+d/4$;
* $3\gamma/4+d/4-j/2-r$;
* $(\gamma+d)/2-r$;
* $\gamma/4+15d/28+11j/28$;
* $\gamma/4+11d/24+j/2+K/8$ with $K=(d+4j+8r-3\gamma)^+$. The $J\asymp J-1$ row equals this formula when $K>0$ ✓.

**Side conditions.** Each is increasing in $(y,s)$, so the corner suffices:
* $SN^2/W$: $j+4r<\gamma$.
* $(J-1)B/S$: $6d/7+24j/7+8r-3\gamma<0$, or $d+3j+8r-3\gamma<0$ when $B=1$.
* Sextic: $d+6j+12r-5\gamma<0$.
* $\sigma\ll1$: $j+2r<\gamma$.
* $T_{\min}=n^{1-2\gamma}$.
* $L\ge1$ and the zero-frequency conditions.

**Values at the binding vertex $(46,53,46)/145$.** Here $r=7$, $j=14$, $d=28$ and $K=2$ (all over 145).
* Term 4 ties exactly, from $435t/28=69/14$.
* Term 5 has slack $10/3480=1/348$.
* The sextic exponent is $-34/145$.
* $(J-1)B/S$ has exponent $-2/29$.
* $SN^2/W$ has exponent $-4/145$.
* $B>1$ there, since $3j>d$.

$272/857-46/145=18/124265$ and $1-4\theta=-39/145$ ✓.

**Convexity.** For fixed $t$ all constraints are max-affine in $(\alpha,\beta,\gamma)$. In $(\alpha,\beta,\gamma,\mu)$ they are
jointly affine. The parameter set is the hull of the three μ = 0 vertices and the apex. Testing those vertices is
therefore valid. I nonetheless also gridded the interior.

## 5. Independent replay

* The author's script output is byte-identical to `data/z78/analytic_r4_lp.txt`.
* My script (Appendix; `/tmp/opus2_46145_check.py`, Fractions) computes the bound from raw scales for each block and each
  $(\lambda,s)$ on a 13×13 grid. It takes the case branch the proof actually uses (Z≪1 / trivial / Erdős–Turán), keeps
  $JZ/S$ unabsorbed, and grids the triangle. Key output:

```
vertex (46,53,46)/145: max(term-goal)=0; sides: SN2/W -4/145, (J-1)B/S -2/29, sextic -34/145, const -32/145
vertex (46,46,53)/145: max(term-goal)=-9/290 ;  vertex (53,46,46)/145: -39/580
whole triangle (45-point grid x 13x13 (lam,s)): worst 0 at (46,53,46)/145; all strict sides < 0
t=46/145-1e-4: +0.00155 (fails);  t=46/145+1e-4: -0.00155 (passes)
R_M, t=theta+(1-3theta)mu+eta, eta=1e-3: worst term-goal in [-0.0219,-0.0064] for mu in [0,3/10]; triangle empty for t>=1/3
near apex: (worst term-goal)/eta <= -5.2 for all tested mu up to 0.999 mu*  (eta=1e-3 and 1e-4)
```

## 6. Defects

**FATAL: none. MAJOR: none.**

**MINOR**

1. **The margin sentence in §14 is wrong.** It says "Strict margins absorb the frequency cutoff", but the fourth term has
   slack exactly 0 at $t=46/145$. As in §8, the proof must be run at $t=46/145+\eta$, where the binding slack is
   $(435/28)\eta$. My replay confirms that a margin $\ge c\eta$ (with $c\approx5$) holds uniformly in μ, including near the
   μ = 1/3 apex, where terms 2–3 have zero slack at η = 0. It also confirms that the parameter triangle is empty once
   $t+\eta\ge1/3$. Suggested wording: "Run at $t=46/145+\eta$; the binding slack is $(435/28)\eta$ and all margins are
   $\gg\eta$ uniformly in μ, absorbing the cutoff, $\delta$ and logs."
2. **"$O(J/(ZN^2))=O(1)$" should be sharpened.** It is in fact $O(1/(ZN^2)+(SN/W)^2)$ (an identity), which is $\le O(N^{-2})$
   under $SN^2/W\ll1$. One line would preempt the worry that this step is delicate.
3. **The script checks vertices only at η = 0, and with ≤ on the tie.** That is logically sufficient given the convexity
   argument plus the η-run. Printing the slack at $t+\eta$ would make item 1 replayable. This is cosmetic.

## 7. Comparison with `REVIEW_ANALYTIC_WILD_R4_OPUS.md` (read only after §§1–6)

**Agreement.** R4_OPUS also upholds 46/145 and θ = 46/145 in (12). It re-derives the same five exponents, the slacks
($1/348$, $-34/145$, the tie, failure at $-10^{-4}$) and the convexity reduction. Its explicit $|\zeta|=m^2h^3/(48n\ell)$ matches
mine. Its form defects E1–E5 are all fixed in the current note and script:
* the label lists the fourth derivative test;
* the misattributed condition is repaired;
* the §13 ES₅ bullet says 46/145;
* Thm 5.11 carries edition and page;
* `g+2r<=2t` is commented.

**New here.**
* Full $(\lambda,s)$ gridding with case branches, rather than only the corner $S=H$. This settles the small-$S$/small-$Y$
  worry by the positive-coefficient table in §4.
* The exact identity for the ξ-replacement error.
* A uniform-in-μ margin (≥ ~5η) for the η-run.
* Defect 1 above, which R4_OPUS did not flag. It called the μ = 1/3 zero slack harmless but did not note the zero slack
  at the binding μ = 0 term against §14's "strict margins" wording.

**Disagreements.** None of substance. R4_OPUS writes the ξ-replacement error as $O(1/N^2)$ via $J\ll1+Z$. That is also
correct, and consistent with my sharper identity.

## Appendix: replay script (`/tmp/opus2_46145_check.py`)

```python
"""Independent replay (Opus2) of ANALYTIC_WILD §14: derive every exponent from raw scales.
Base X=n/M, M=X^mu.  Block U,V,W = X^(a,b,g).  P=X^r, N=X^(2r), H=X^j.
For each l=X^lam (0<=lam<=lammax) and dyadic S=X^s (0<=s<=j) compute the exponent of
 (S/H) * W^{1/2} Y^{1/4} (S^{-1} sum_i D_i)^{1/4}, (S^{-1} sum D_i) from the *unabsorbed* raw
(14)-proof bound  JZ/S + 1 + Delta + Y/N^2 + Z/B + Z(BY/S^3)^{1/6} + J^{1/2} Z Y^{-1/6}  (case Z>=1),
or 1+Delta (case Z<1), or Z(1+Delta)+JZ(1+Delta)/S (trivial, Y>=S^3 or Delta>=1), taking the
case actually used by the proof.  No monotonicity is assumed: we grid over (lam,s) and the block.
"""
from fractions import Fraction as F
import itertools, sys

def exps(t, mu, a, b, g, lam, s):
    r = b - t; j = 2*(r + g - t)
    y = 1 + lam + s - 3*g                 # Y = X*l*S/W^3 (A = X l h); lam already includes mu via L
    if y < 0: return None                 # nonstationary: O(1)
    z = y + 2*s - g                       # Z = Y S^2 / W
    De = g - 2*s - 4*r                    # Delta = Y/(Z N^2) = W/(S^2 N^2)
    Jp = g + y + 4*(s + 2*r - g)          # J-1 = W Y (S N / W)^4
    J = max(0, Jp)
    YN = y - 4*r
    cands = [0, De]
    if z <= 0:
        pass                               # Z<<1: 1+Delta
    else:
        triv = [z, z+De, J+z-s, J+z+De-s]  # trivial count O(Z(1+D)) + JZ(1+D)/S
        if De >= 0 or y >= 3*s:
            cands += triv
        else:
            bb = (3*s - y)/7               # B=(S^3/Y)^{1/7}
            cands += [J+z-s, z+De, z-bb, z+(bb+y-3*s)/6, J/2+z-y/6]
    E14 = max(cands)
    tot = g/2 + y/4 + E14/4 + s - j
    side = {
        'SN2/W<1': s + 4*r - g,
        '(J-1)B/S<1': (Jp + max(0,(3*s-y)/7) - s) if Jp > -10**9 else -1,
        'B<=S': max(0,(3*s-y)/7) - s,
        'sextic': g + y + 6*(s + 2*r - g),
        'sigma<1': s + 2*r - g,
    }
    return tot, side

def block_check(t, mu, a, b, g, grid):
    r = b - t; j = 2*(r + g - t)
    lammax = mu + 2*r + g - b              # L = M N W / V
    goal = 2*t - g - 2*r                   # = g - j
    worst = -10**9; wside = {}
    for p in range(grid+1):
        lam = lammax*F(p, grid)
        for q in range(grid+1):
            s = j*F(q, grid)
            res = exps(t, mu, a, b, g, lam, s)
            if res is None: continue
            tot, side = res
            worst = max(worst, tot - goal)
            for k, v in side.items(): wside[k] = max(wside.get(k, -10**9), v)
    other = {
        'const(g+2r<=2t)': g + 2*r - 2*t,
        'T_min large (2g<1)': 2*g - 1,
        'L>=1': -(lammax),
        'zero freq V/(MN)': b - mu - 2*r - t,
        'zero freq V/(MW)': b - mu - g - t,
        'j>=0': -j, 'r>=0': -r,
    }
    return worst, wside, other

def verts(t):
    return [(t,1-2*t,t),(t,t,1-2*t),(1-2*t,t,t)]

th = F(46,145)
print('=== exact vertex + (lam,s)-grid check at t=46/145, mu=0 ===')
for v in verts(th):
    w, ws, o = block_check(th, F(0), *v, 12)
    print(v, 'max(term-goal)=', w, 'side max', {k: str(x) for k,x in ws.items()}, {k: str(x) for k,x in o.items()})

print('=== interior of triangle, grid, t=46/145 (worst term-goal over triangle) ===')
def tri_scan(t, mu, G, grid):
    worst = (-10**9, None); sidew = {}
    for i in range(G+1):
        for k in range(G+1-i):
            l3 = G - i - k
            # barycentric on vertices
            V = verts(t)
            a = (i*V[0][0] + k*V[1][0] + l3*V[2][0])/G
            b = (i*V[0][1] + k*V[1][1] + l3*V[2][1])/G
            g = (i*V[0][2] + k*V[1][2] + l3*V[2][2])/G
            w, ws, o = block_check(t, mu, a, b, g, grid)
            if w > worst[0]: worst = (w, (a,b,g))
            for kk, vv in list(ws.items()) + list(o.items()):
                if vv > sidew.get(kk, (-10**9,))[0]: sidew[kk] = (vv, (a,b,g))
    return worst, sidew
w, sw = tri_scan(th, F(0), 8, 8)
print('worst', w[0], 'at', w[1])
for k, (v, at) in sw.items(): print('  side', k, float(v), 'at', tuple(map(str,at)))

print('=== tightness: t slightly below fails, slightly above passes with margin ===')
for dt in (F(-1,10**4), F(1,10**4)):
    t = th + dt
    w, _, _ = block_check(t, F(0), *verts(t)[0], 12)
    print('t=46/145%+g' % float(dt), 'vertex1 worst term-goal', float(w))

print('=== R_M: mu grid, t=theta+(1-3theta)mu + eta, worst margins ===')
eta = F(1,1000)
NS=('const(g+2r<=2t)','L>=1','j>=0','r>=0','zero freq V/(MN)','zero freq V/(MW)','B<=S')
for mu in [F(k,30) for k in range(0,10)] + [F(1,3)-F(1,100), F(1,3)-F(1,250),F(1,3)-F(1,400),F(1,3)-F(1,1000)]:
    t = th + (1-3*th)*mu + eta
    if 3*t >= 1: print('mu',mu,'triangle empty'); continue
    w, sw = tri_scan(t, mu, 6, 6)
    strict = max(v for k,(v,_) in sw.items() if k not in NS)
    nonstrict = max(v for k,(v,_) in sw.items() if k in NS)
    print('mu', mu, 'worst term-goal %.6f' % float(w[0]), ' worst strict-side %.6f' % float(strict), ' worst nonstrict %.6f' % float(nonstrict))

print('=== exponent check for (12): X^theta M^(1-3theta) = n^theta M^(1-4theta):', 1-4*th)

print('=== near the apex: margin / eta ===')
for eta in (F(1,1000), F(1,10000)):
    mup = (F(1,3) - th - eta)/(1-3*th)
    for frac in (F(0), F(1,2), F(9,10), F(99,100), F(999,1000)):
        mu = mup*frac
        t = th + (1-3*th)*mu + eta
        w, sw = tri_scan(t, mu, 4, 6)
        print('eta',eta,'mu/mu*',frac,'worst term-goal / eta = %.4f' % float(w[0]/eta))
```
