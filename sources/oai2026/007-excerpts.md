# Family 007

CLAIMED (OAI dump, unrefereed); verbatim source excerpts follow.

## preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/final.pdf

Source: preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/introduction.tex
```tex
\begin{theorem}[A logarithmic saving for affine Liouville correlations]
\label{thm:q-affine}
There is an absolute constant \(c>0\) such that, for every fixed choice
of integers \(a_1,a_2\ge1\) and \(b_1,b_2\ge0\) with
\(a_1b_2-a_2b_1\ne0\), there is a constant
\(C_{a_1,a_2,b_1,b_2}\) for which
\[
 \left|\sum_{1\le n\le X}
       \lambda(a_1n+b_1)\lambda(a_2n+b_2)\right|
 \le C_{a_1,a_2,b_1,b_2}\frac{X}{(\log X)^c}
 \qquad(X\ge3).
\]
The cutoff \(X\) may be any real number. No coprimality condition is
imposed on the coefficients.
\end{theorem}
\begin{theorem}[Binary corrected Elliott]\label{thm:elliott}
Let \(f_1,f_2:\N\to\mathbb D\) be multiplicative, and suppose that
at least one satisfies \eqref{eq:unp}. For every fixed pair of distinct
nonnegative integers \(h_1,h_2\),
\[
 \frac1N\sum_{n=1}^N f_1(n+h_1)f_2(n+h_2)\longrightarrow0
 \qquad(N\longrightarrow\infty,\ N\in\N).
\]
\end{theorem}
```

Source: preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/qualitative/analytic-transfer.tex
```tex
\begin{theorem}[Averaged short exponential sums]\label{thm:mrt}
Let $X\ge D\ge10$ and let $b\colon\N\to\C$ be a $1$-bounded
multiplicative function. With
$Q=\min((\log X)^{1/125},(\log D)^5)$, one has
\begin{equation}\label{eq:mrt-input}
 \begin{split}
 \sup_{\alpha\in\T}\int_0^X
 \left|\sum_{y<m\le y+D}b(m)\mathrm e(\alpha m)\right|\,dy
 \ll DX\left(
 e^{-\mathcal M(b;X,Q)/20}
 +\frac{\log\log D}{\log D}
 +\frac1{(\log X)^{1/700}}\right).
 \end{split}
\end{equation}
The implied constant is absolute.
\end{theorem}
```

Source: preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/qualitative/paths.tex
```tex
\begin{theorem}[High trace]\label{thm:high-trace}
For the divisor family, cutoffs, and kernels of
\Cref{sec:graph-setup}, the periodic set $Y$ in
\Cref{def:primitive-specification} satisfies, as $B\to\infty$,
\begin{align}
 \Pbb(n\notin Y)&\le P_0^{-1+o(1)},\label{eq:deleted-density}\\
 \sum_{\boldsymbol d}
 \left|\E K_{\boldsymbol d}(n)
       \prod_{j=0}^{\ell}\1_Y(n+b_j)\right|
   &\le B^{-(1+c_*)\ell}.\label{eq:high-trace}
\end{align}
The sum is over all closed lines of length $\ell$.  The asymptotic
bounds are uniform over the admissible divisor families and cutoffs,
with $h,\tau,C_0,T$ fixed.
\end{theorem}
```

Source: preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/quantitative/03-analytic.tex
```tex
\begin{theorem}[Matom\"aki--Radziwi\l\l--Tao,
\cite{MRT15}, Theorem~1.3]\label{q:MRT-short}
For every pair of real numbers $10\le H\le Z$,
\[
 \sup_{\alpha\in\mathbb R}
 \int_0^Z
 \left|\sum_{x\le n\le x+H}\lambda(n)\mathrm e(\alpha n)\right|\,dx
 \ll HZ\left(\frac{\log\log H}{\log H}
                  +(\log Z)^{-1/700}\right),
\]
with an absolute implied constant. The supremum is outside the integral.
\end{theorem}
```

Source: preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/build/quantitative/04-paths-trace.tex
```tex
\begin{theorem}[The nonbacktracking moment]\label{q:trace}
There is an absolute constant $C_2$ such that
\begin{equation}\label{q:trace-bound}
 \E\|H^k\|_{\mathrm{HS}}^2
 \le\bigl[K(C_2\sqrt W)^J\bigr]^{2k}.
\end{equation}
The norm is the unnormalized Hilbert--Schmidt norm.  The same estimate,
after increasing $C_2$ absolutely, holds when block origins are averaged
over any integer interval of length at least $\exp(\tfrac12L^A)$.
The threshold for $L$ may depend on the fixed data.
\end{theorem}
```

## Lean scope page (verbatim)
# Ordinary two-point correlations and the corrected Elliott conjecture

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Ordinary two-point correlations of multiplicative functions](../../preprints/Ordinary-two-point-correlations-of-multiplicative-functions-September-24-2026/final.pdf)

## Scope

The formalization proves ordinary two-point cancellation for multiplicative functions. For the Liouville function on every fixed pair of nonproportional affine forms, the correlation sum up to $X$ is $O(X/(\log X)^c)$ for an absolute $c>0$, with the implied constant depending on the forms.

For two one-bounded multiplicative functions, if at least one is uniformly nonpretentious against all Dirichlet-character twists with frequency $|t|\le N$, then their shifted and nonproportional affine correlation sums divided by $N$ tend to zero. These are ordinary averages, with no logarithmic averaging.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Ordinary Elliott cancellation under uniform nonpretentiousness | [OrdinaryElliott.lean](../ComparatorChallenges/OrdinaryElliott.lean) |
| Ordinary Liouville and multiplicative two-point correlations | [OrdinaryTwoPointCorrelations.lean](../ComparatorChallenges/OrdinaryTwoPointCorrelations.lean) |
