# Family 023

CLAIMED (OAI dump, unrefereed); verbatim source excerpts follow.

## preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf

Source: preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/paper.tex
```tex
\begin{theorem}[First moment over primary primes]\label{thm:main}
As $X\longrightarrow\infty$,
\begin{equation}\label{eq:main}
 \sum_{\substack{N\pi\le X\\\pi\equiv1\pmod3\ \mathrm{prime}}}G(\pi)
 =\frac65c_*\frac{X^{5/6}}{\log X}
   +o\!\left(\frac{X^{5/6}}{\log X}\right).
\end{equation}
The sum is over all primary primes in $\mathcal O$.
\end{theorem}
```

Source: preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex
```tex
\begin{theorem}[Comparison in each fixed angular mode]
\label{thm:angular}
For every fixed integer $\ell$,
\begin{equation}
 \sum_{\substack{N\pi\le X\\\pi\equiv1\pmod3\ \mathrm{prime}}}
 \theta_\ell(\pi)\bigl(G(\pi)-c_*N(\pi)^{-1/6}\bigr)
 =o_\ell\!\left(\frac{X^{5/6}}{\log X}\right).
 \label{eq:angular-comparison}
\end{equation}
In particular, for every fixed nonzero integer $\ell$,
\begin{equation}
 \sum_{\substack{N\pi\le X\\\pi\equiv1\pmod3\ \mathrm{prime}}}
       \theta_\ell(\pi)G(\pi)
 =o_\ell\!\left(\frac{X^{5/6}}{\log X}\right).
 \label{eq:angular-cancellation}
\end{equation}
\end{theorem}
```

Source: preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/background-type1.tex
```tex
\begin{theorem}[Heath-Brown's cubic large sieve]
\label{thm:cls}
Let $A,B\ge1$, and let $(u_b)$ be supported on primary squarefree
elements with $Nb\asymp B$. Then, for every $\epsilon>0$,
\[
 \sum_{Na\asymp A}\mu^2(a)
 \left|\sum_b u_b\chi_a(b)\right|^2
 \ll_\epsilon (AB)^\epsilon
 \bigl(A+B+(AB)^{2/3}\bigr)\sum_b|u_b|^2.
\]
The same assertion holds with upper cutoffs in place of dyads.
\end{theorem}
\begin{theorem}[Level Voronoi formula, the required form]
\label{thm:voronoi-background}
Let $r$ be primary and squarefree, and let $W$ be smooth and compactly
supported in $(0,\infty)$. Put $R=Nr$ and
$A_0=(2\pi)^{5/3}/(3^{7/2}\Gamma(2/3))$.
The completed sum
\[
 \mathcal C_r(V;W)=
 \sum_{\substack{d,u\\(d,r)=1}}|d|G(ur)
             W\left(\frac{N(ud^3)}{V}\right)
\]
has main term
$A_0\mathcal MW(5/6)V^{5/6}\varphi(r)R^{-7/6}$.
Its remaining term is
\[
 \frac{R^{1/2}}{3^{7/2}(2\pi)^2}
 \sum_{\substack{0\ne\nu\in\lambda^{-1}\mathcal O, d\\(d,r)=1}}
 \frac{a_r(\nu)b_r(\nu)}{N\nu\,(Nd)^{5/2}}
 \check W\left(\frac{(2\pi)^4N(d^3\nu)V}{R^2}\right),
\]
where, for sufficiently small $\sigma>0$,
\[
 \check W(v)=\frac{1}{2\pi i}\int_{(-\sigma)}v^z
 \frac{\Gamma(5/6-z)\Gamma(7/6-z)}
      {\Gamma(z-1/6)\Gamma(z+1/6)}\mathcal MW(z)\,dz.
\]
The coefficients depend only on $r$ and $\nu$, independently of $V$
and $W$. They vanish outside representations
\[
 \nu=\lambda^j\zeta h w(h')^3,\quad j\ge-1,\quad
 h,h'\mid r^\infty,\quad (w,r)=1,\quad \mu^2(hw)=1,
\]
where $h,h',w$ are primary and $\zeta$ is a unit.
On this support, they are
\[
 a_r(\nu)=a^\star(\lambda^{-3}\nu),\qquad
 b_r(\nu)=\mu\left(\frac{r}{(\lambda\nu,r)}\right)
          \frac{\varphi(r)}{\varphi\left(r/(\lambda\nu,r)\right)},
\]
where $a^\star$ is the theta coefficient in
\cite[Equation (5.74)]{DR2024}; the second formula is its
Equation (5.68). The index $\lambda^{-3}\nu$ is the one supplied
by its coefficient identity (5.79).
They satisfy
\[
 |a_r(\nu)|\ll 3^{\max(j,0)/3}|h'|,
 \qquad |b_r(\nu)|\le N((\lambda\nu,r)).
\]
In particular, if $V,V^{-1},R\ll X^{C_0}$ for fixed $C_0$, $W$ is
supported in a fixed compact subinterval of $(0,\infty)$, and each
fixed derivative bound is at most a fixed logarithmic power, then
\begin{equation}
 \mathcal C_r(V;W)=
 A_0\mathcal MW(5/6)V^{5/6}\frac{\varphi(r)}{R^{7/6}}
 +O_\epsilon(X^\epsilon R^{1/2}).
 \label{eq:voronoi}
\end{equation}
\end{theorem}
\begin{theorem}[The metaplectic mean-square input]
\label{thm:hb-height}
For primary squarefree $r$, the Dirichlet series
\[
 f_r(s)=\sum_u G(ru)(Nu)^{-s},\qquad \operatorname{Re}s>1,
\]
continues meromorphically to $\operatorname{Re}s>1/2$, with at most
a simple pole at $5/6$. It has polynomial growth in closed strips
there, away from its pole. For sufficiently small $\epsilon>0$ and
every $T\ge1$,
\begin{equation}
 \int_{-T}^T|f_r(1/2+\epsilon+it)|^2dt
 \ll_\epsilon (Nr)^{1/2+4\epsilon}T^2.
 \label{eq:hb-mean-square}
\end{equation}
Its residue $\rho_r$ satisfies $|\rho_r|\ll (Nr)^{-1/6}$.
\end{theorem}
```

## Lean scope page (verbatim)
# Patterson's first moment for cubic Gauss sums

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [An unconditional first moment for cubic Gauss sums](../../preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf)

## Scope

Patterson's first-moment conjecture concerns the average of normalized cubic Gauss sums over primary Eisenstein primes. The formalization proves the sharp-cutoff asymptotic with main term $\frac65c_*X^{5/6}/\log X$, where $c_*=(2\pi)^{2/3}/(3\Gamma(2/3))$. It also proves the corresponding angular comparison for every integer Fourier mode and cancellation of order $o(X^{5/6}/\log X)$ for each fixed nonzero mode. All primary Eisenstein primes are included, without an extra conjectural premise.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Patterson first moment and angular cancellation | [PattersonFirstMoment.lean](../ComparatorChallenges/PattersonFirstMoment.lean) |
