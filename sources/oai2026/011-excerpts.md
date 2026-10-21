# Family 011

CLAIMED (OAI dump, unrefereed); verbatim source excerpts follow.

## preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/paper.pdf

Source: preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/build/sections/00-introduction.tex
```tex
\begin{theorem}\label{thm:totient}
For every real $\eps>0$, there are infinitely many positive integers
$n$ such that
\[
 g(n)>n^{1-\eps}.
\]
\end{theorem}
\begin{theorem}\label{thm:smooth}
For every fixed $0<\delta<1/4$, as $x\to\infty$,
\begin{equation}\label{eq:main-smooth}
 \#\{p:\ p\text{ prime},\ 2x<p\le5x,
                   \ P^+(p-1)\le x^\delta\}
 \ge x^{1-o(1)}.
\end{equation}
The quantity $o(1)$ may depend on $\delta$.
\end{theorem}
```

Source: preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/build/sections/01-preliminaries.tex
```tex
\begin{theorem}[Siegel--Walfisz]\label{thm:sw}
For fixed $A,C>0$, uniformly for $(a,r)=1$ and
$1\le r\le(\log y)^C$,
\[
 \#\{p\le y:p\equiv a\pmod r\}
 =\frac{\Li(y)}{\varphi(r)}
  +O_{A,C}\!\left(\frac{y}{(\log y)^A}\right).
\]
The constants, which need not be effective, are independent of $y,a,r$.
\end{theorem}
\begin{theorem}[Multiplicative large sieve]\label{thm:large-sieve}
Let $I$ be a real interval of length $H$, let $a_n$ be complex numbers
supported on $I\cap\Z$, and let $R\ge1$. Then
\[
 \sum_{r\le R}\frac r{\varphi(r)}
 \sum_{\chi\bmod r}^{*}
 \left|\sum_{n\in I\cap\Z}a_n\chi(n)\right|^2
 \ll (H+1+R^2)\sum_n|a_n|^2,
\]
where the asterisk restricts the sum to primitive Dirichlet characters.
\end{theorem}
```

Source: preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/build/sections/02-transference.tex
```tex
\begin{theorem}[Local transference]\label{thm:transference}
For every fixed $E>0$ there is $E_{\rm id}>0$, depending only on
$E$ and the fixed data in \Cref{def:prime-groups}, with the following
property.  Assume
\begin{equation}\label{eq:ideal-norm-hypothesis}
 \sup_{\Theta\in\R}\norm{\mathcal T(\Theta)}\le L^{-E_{\rm id}}.
\end{equation}
Then, for every sufficiently large fixed $J$, where the lower
bound on $J$ may also depend on $m,C_1$, put
\[
 R=\lceil L^{0.52}\rceil,\qquad N=2R.
\]
For every fixed $\gamma>0$ and $I=[X,2X)$ with
$x^\gamma\le X\le x^{1/\gamma}$, one has
\begin{equation}\label{eq:transference-moment}
 \frac1{|I\cap\Z|}\sum_{n\in I\cap\Z}
 \langle u_n,(\mathcal A\mathcal A^*)^Ru_n\rangle
 \le L^{-EN},
\end{equation}
for all sufficiently large $x$.  Here $u_n$ is one on every
physical state at position $n$ and zero elsewhere.  The threshold
for $x$ may depend on all fixed parameters, including $J,C_2,
\gamma$, and the bound is uniform subject to these parameters
and \Cref{eq:ideal-norm-hypothesis}.  No bound on $\zeta$ is needed
apart from the assumed ideal estimate.
\end{theorem}
```

Source: preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/build/sections/03-ideal-kernels.tex
```tex
\begin{theorem}[Construction of the residual ideal operator]
\label{thm:ideal}
Fix $E_{\rm id}>0$ and a fixed frequency exponent $C_4\geq0$.
There are fixed integers $m,J_0$ and a fixed constant $C_1$, depending
only on these parameters, $\ell$, and the prime-group bounds, with the
following property.  For every fixed $J\geq J_0$, there is a family
consisting of the raw pattern
\[
 C_g=\varnothing\quad\hbox{for every }g,\qquad K_0=1,
\]
and signed comparison patterns satisfying
\[
 C_g=\varnothing\ (g\in\mathcal S),\qquad
 |C_g|\leq m\ (g\in\mathcal B),\qquad
 \sum_\nu\sup|K_\nu|\leq L^{C_1},
\]
such that the symmetrized ideal operator of \Cref{sec:transference}
satisfies
\begin{equation}\label{eq:ideal-small-norm}
 \sup_{\Theta\in\R,\ |\zeta|\leq L^{C_4}}
 \norm{\mathcal T(\Theta)}_{2\to2}\leq L^{-E_{\rm id}}
\end{equation}
for sufficiently large $x$.  The coefficients and the family are
independent of $\Theta$ and of the individual value of $\zeta$.
Their defining parameters are independent of $J$; $J$ only supplies
the available shared slots.  The threshold for $x$ may depend on $J$.

More precisely, designate $m$ of the first $J$ slots in each big group
as probes, and split the big groups into two blocks. Each comparison
frees nonempty sets $A$ and $B$ of designated probes in the respective
blocks, and its coefficient has the form
\begin{equation}\label{eq:ideal-comparison-coefficient}
 -(-1)^{|A|+|B|}\mathcal K_A(D_A,X_A)
                         \mathcal K_B(D_B,X_B).
\end{equation}
Here $D_A,D_B$ are the products of the free labels used to form $D$,
$X_A$ is the product of the target labels in $A$, and $X_B$ the
product of the input labels in $B$.  These coefficients use no
shared labels and none of the last $\ell$ labels.  Each kernel is
a finite sum of products of matched log-cell indicators and pairs of
Dirichlet characters of conductor bounded by a fixed power of $L$.
\end{theorem}
```

Source: preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/build/sections/04-shifted-correlations.tex
```tex
\begin{theorem}[Lifted shift cancellation]\label{thm:shift}
Fix all the group and endpoint bounds above. Fix $D_0,C>0$ and a fixed
compact interval $[c_\Psi,C_\Psi]\subset(0,\infty)$. Suppose
$0<|k|\leq L^C$ is integral, $xL^{-C}\leq Z\leq xL^C$,
$|a_1|,|a_2|\leq L^C$, and $\Psi$ is supported in that interval with
$\|\Psi^{(j)}\|_\infty\ll_j L^{C(j+1)}$ for every $j\geq0$.
There exists a fixed $B$, depending only on these bounds and $D_0$,
such that \Cref{eq:discrepancy} implies
\begin{equation}\label{eq:shift-bound}
 \sum_{\substack{z>0\\z+k>0}}
 \frac{\Psi(z/Z)}z\,z^{ia_1}(z+k)^{ia_2}
       \overline{F_0(z)}G_0(z+k)W_\ell(z)W_\ell(z+k)
       \ll L^{-D_0}.
\end{equation}
The bound is uniform over the indicated sequences, intervals, characters,
frequencies, and cutoffs. It also holds when the discrepancy-bearing
endpoint or its coefficients have been conjugated.
\end{theorem}
```

Source: preprints/Weighted-Dilation-Graphs-Smooth-Shifted-Primes-and-Totient-Fibers-September-24-2026/build/sections/05-type-ii.tex
```tex
\begin{theorem}[Type II]\label{thm:typeii}
Fix $D_*>0$, $b_*>0$, and $C>0$, and require
$\eta_*<b_*/4$ in \Cref{eq:typeii-rough-slot}. Let $U,V$ be dyadic
scales satisfying
\[
 UV\asymp x,\qquad x^{b_*}\leq U,V\leq x^{1-b_*}.
\]
Let $\Psi$ be a fixed smooth function with compact support in a fixed
compact subinterval of $(0,\infty)$. Suppose that
$\abs{\alpha_m},\abs{\beta_n}\leq L^C$, and that $\alpha_m=0$ unless
$\Pminus(m)>W$. There is a fixed exponent $B$, depending only on these
data and the fixed group and band constants, such that the discrepancy
hypothesis in \Cref{eq:discrepancy} on $\alpha$ implies
\begin{equation}\label{eq:typeii-bound}
 \sum_{\substack{m\asymp U,\ n\asymp V,\ u\geq1\\mn=2u+1}}
      A(u)\Psi(u/x)\alpha_m\beta_n
       \ll xL^{-D_*}.
\end{equation}
Here the sequence to which the discrepancy hypothesis is applied includes
the actual restriction $m\asymp U$ and any additional interval restriction
on $m$. Explicitly, for that restricted sequence one requires
\[
 \left|\sum_{m\in I}\frac{\alpha_m\chi(m)m^{it}}m\right|
       \leq L^{-B}
 \quad\left(I\subset[1,x^2],\quad
       \operatorname{mod}(\chi)\leq L^B,\quad |t|\leq L^B\right).
\]
There is no discrepancy hypothesis on $\beta$. The constants are uniform
over the sequences, scales, and interval restrictions satisfying these
conditions.
\end{theorem}
```

## preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/paper.pdf

Source: preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/build/sections/01-introduction.tex
```tex
\begin{theorem}\label{thm:main}
For every fixed $k\ge1$ and every bounded continuous function
$F:[0,1]^k\to\R$,
\begin{equation}\label{eq:main-law}
 \lim_{x\to\infty}\frac1{\pi(x)-1}
     \sum_{\substack{3\le p\le x\\p\text{ prime}}}
       F\bigl(V_1(p),\ldots,V_k(p)\bigr)
 =\E F(L_1,\ldots,L_k).
\end{equation}
The limit holds through all real $x$ and uses ordinary equal
weighting of the primes.
\end{theorem}
```

Source: preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/build/sections/03-determinant.tex
```tex
\begin{theorem}[One-sided marked Type II estimate]\label{thm:type-II}
Fix $\delta,C,D_*>0$ and $q\in(0,1)$.  Suppose
$H_m,H_n\geq x^\delta$ and $X=H_mH_n\asymp x$.  Let $F$ satisfy
$|F(h)|\leq1$ and $F(ph)=F(h)$ for every prime in the groups
\eqref{det:bands}.  Let $\alpha_m$ be supported on an arbitrary
interval in $[H_m,2H_m]$, where it has the value
\[
 \alpha_m=m^{iv}\left(\1_{m\text{ prime}}
       -\frac{\1_{m\text{ rough}}}{V(W)\log m}\right),
 \qquad |v|\leq L^C.
\]
Let $\beta_n$ be supported on rough integers in $[H_n,2H_n]$, with
$|\beta_n|\leq L^C$.  If $K$ is sufficiently large in terms of
$\delta,C,D_*,q$, then
\begin{equation}\label{eq:type-II}
 \left|\sum_{m,n}\alpha_m\beta_n F(mn-1)\mathcal W(mn-1)\right|
       \ll X L^{-D_*}.
\end{equation}
The required lower bound on $K$ is independent of the particular
$a_i$.  The implicit constant and the threshold for $x$ may depend on
all the fixed parameters, including the $a_i$.
\end{theorem}
```

Source: preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/build/sections/06-correlations.tex
```tex
\begin{theorem}[Two-sided correlation]\label{thm:two-sided}
Fix $d\geq1$, $\eps>0$, and intervals $I_1,\ldots,I_d$ whose lower
endpoints are at least $x^\eps$ and whose upper endpoints have product
at most $x^{1-\eps}$.  Let $\mathbf l=(l_1,\ldots,l_d)$ run over
ordered tuples of distinct primes with $l_i\in I_i$, and put
\begin{equation}\label{cor:centered-core}
 l:=l_1\cdots l_d,\qquad
 C_x:=\sum_{\mathbf l}\frac1l,\qquad
 F_x(n):=\mathcal W(n)
       \left(\sum_{\mathbf l}\1_{l\mid n}-C_x\right).
\end{equation}
Suppose $G(n)=G(n_*)$ and
$|G(n)|\leq L^C\tau(n_*)^C$, for fixed $C$.  For every fixed smooth
compactly supported $\Psi:(0,\infty)\to\C$ and every fixed $A>0$,
\begin{equation}\label{eq:two-sided}
 \sum_{w\geq1}\frac{\Psi(w/x)}w
       F_x(w)G(w+1)W_1(w)W_1(w+1)\ll_A L^{-A}.
\end{equation}
The constants and sufficiently-large-$x$ threshold may depend on all
the fixed data, including the fixed inert bands, but the estimate is
uniform over the active groups and slot intervals satisfying the stated
bounds.  The slots have no joint restriction other than distinctness.
\end{theorem}
```

Source: preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026/build/sections/07-extraction.tex
```tex
\begin{theorem}[Interior prime statistic]\label{thm:interior}
For every nonnegative $\Phi\in C_c^\infty((0,\infty))$,
\begin{equation}\label{eq:interior}
 \sum_{p\text{ prime}}\Phi((p-1)/x)
                   \bigl(f_x(p-1)-C_x\bigr)=o(x/\log x).
\end{equation}
The limit holds through all real $x\to\infty$ for the slot
intervals just described.
\end{theorem}
```

## preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/paper.pdf

Source: preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/build/main.tex
```tex
\begin{theorem}\label{thm:main}
There are infinitely many primes $p$ such that $p-1$ is squarefree
and $\Omega(p-1)$ is even. In particular, there are infinitely many
such primes under either convention for counting prime factors.
\end{theorem}
```

Source: preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/build/sections/03-shifted.tex
```tex
\begin{theorem}[Twisted prime-slot correlation]\label{sh:correlation}
Let $F,G$ have the form \eqref{sh:core}, with possibly different
coefficients, characters, intervals, and frequencies, subject to fixed
bounds as above.  For every fixed $D_0>0$ there is a fixed $B>0$ with
the following property.  Suppose that the sequence $\alpha$ in $F$
satisfies
\begin{equation}\label{sh:discrepancy}
 \left|\sum_{m\in I}\alpha_m\chi(m)m^{-1+it}\right|\leq L^{-B}
 \quad\left(
 \begin{array}{l}
 I\subset[1,x^2]\text{ an interval},\\
 \operatorname{mod}(\chi)\leq L^B,\quad |t|\leq L^B
 \end{array}\right).
\end{equation}
There is no discrepancy requirement on $G$.  Uniformly for
$xL^{-C}\leq Z\leq xL^C$, integers $0<|k|\leq L^C$,
$|a_1|,|a_2|\leq L^C$, and smooth functions $\psi$ supported in a
fixed compact subinterval of $(0,\infty)$ with
$\|\psi^{(j)}\|_\infty\ll_j L^{C(j+1)}$, one has
\begin{equation}\label{sh:correlation-bound}
 \sum_{\substack{z>0\\z+k>0}}\frac{\psi(z/Z)}z
 z^{ia_1}(z+k)^{ia_2}\overline{F(z)}G(z+k)
 W_\ell(z)W_\ell(z+k)\varepsilon(z)\varepsilon(z+k)
 \ll L^{-D_0}.
\end{equation}
The exponent $B$ depends only on $D_0$ and the displayed fixed data.
\end{theorem}
```

Source: preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/build/sections/05-type-ii.tex
```tex
\begin{theorem}[Type II distribution]\label{ti:distribution}
Fix $D_*,b_*,C>0$. Let $U,V$ be dyadic scales such that
\[
 UV\asymp x,\qquad x^{b_*}\le U,V\le x^{1-b_*},
\]
and let $K\subset[U,2U)$ and $J\subset[V,2V)$ be intervals. Suppose
$|\alpha_m|,|\beta_n|\le L^C$ and $\alpha_m=0$ unless
$P^-(m)>W$. There is a fixed $B$, depending only on these fixed data
and on the fixed weight and cutoff data, for which the following holds.
Assume that the sequence $\alpha_m\1_{m\in K}$ satisfies
\eqref{sh:discrepancy}; explicitly, assume
\begin{equation}\label{ti:actual-discrepancy}
 \left|\sum_{m\in I}\alpha_m\1_{m\in K}
                    \chi(m)m^{-1+it}\right|\le L^{-B}
 \quad\left(
 \begin{array}{c}
 I\subset[1,x^2]\text{ an interval},\\
 \operatorname{mod}(\chi)\le L^B,\quad |t|\le L^B
 \end{array}\right).
\end{equation}
Then
\begin{equation}\label{ti:bound}
 \sum_{\substack{m\in K,\ n\in J,\ u\ge1\\mn=2u+1}}
       \alpha_m\beta_n A(u)\Psi(u/x)
       \ll xL^{-D_*}.
\end{equation}
The estimate is uniform in the intervals and coefficient sequences
satisfying these assumptions. No discrepancy or smoothness assumption is
imposed on $\beta$.
\end{theorem}
```

Source: preprints/Prime-Predecessors-with-an-Even-Number-of-Prime-Factors-September-17-2026/build/sections/06-congruences.tex
```tex
\begin{theorem}[Congruence distribution]\label{cg:distribution}
For every fixed $0<\vartheta<1/2$ and $D>0$,
\[
 \sum_{\substack{d\le x^\vartheta\\d\ {\rm odd\ and\ squarefree}}}
       |r(d)|\ll_{\vartheta,D}xL^{-D}+X_A L^{-18}.
\]
The constants may depend on the fixed weight geometry and $\Psi$,
but not on any later proxy precision. No effective bound on the
threshold for $x$ is asserted.
\end{theorem}
```
