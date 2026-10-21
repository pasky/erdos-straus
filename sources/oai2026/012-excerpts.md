# Family 012

CLAIMED (OAI dump, unrefereed); verbatim source excerpts follow.

## preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/paper.pdf

Source: preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/build/sections/introduction.tex
```tex
\begin{theorem}[Joint Dickman law]\label{thm:main}
For every fixed $a,b\in(0,1)$,
\[
 \lim_{X\to\infty}\frac1X
 \#\{2\leq n\leq X:\Pplus(n)\leq n^a,
                         \ \Pplus(n+1)\leq n^b\}
 =\rho(1/a)\rho(1/b).
\]
Here the limit is taken over all real $X$, with ordinary, unweighted
counting.
\end{theorem}
```

Source: preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/build/sections/labels.tex
```tex
\begin{theorem}[Real short-interval comparison]
\label{thm:labels-real-MR}
There is a function $r(H)$ tending to zero as $H\to\infty$ such that,
for every real multiplicative function $g:\N\to[-1,1]$ and
$2\leq H\leq X$,
\begin{equation}\label{eq:labels-real-MR}
 \frac1X\int_X^{2X}
   |\mathcal A_Hg(z)-\mathcal L_Xg|^2\,dz\leq r(H).
\end{equation}
\end{theorem}
\begin{theorem}[Complex short averages]
\label{thm:labels-complex-MRT}
For every multiplicative function $g:\N\to\C$ with $|g|\leq1$ and
$X\geq H\geq10$,
\begin{equation}\label{eq:labels-complex-quantitative}
 \frac1X\int_X^{2X}|\mathcal A_Hg(z)|^2\,dz
 \ll (1+M(g;X))e^{-M(g;X)}
       +\left(\frac{\log\log H}{\log H}\right)^2
       +(\log X)^{-1/50},
\end{equation}
with an absolute implied constant.
\end{theorem}
```

## Lean scope page (verbatim)
# Independent largest prime factors of consecutive integers

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [The joint Dickman law for consecutive integers](../../preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/paper.pdf)

## Scope

Let $P^+(n)$ be the largest prime factor of $n$. The formalization proves the joint Dickman law in ordinary natural density: for every $0<a,b<1$, the density of integers satisfying $P^+(n)\le n^a$ and $P^+(n+1)\le n^b$ tends to $\rho(1/a)\rho(1/b)$, where $\rho$ is the Dickman function.

It also proves that each of the orderings $P^+(n)<P^+(n+1)$ and $P^+(n+1)<P^+(n)$ has natural density $1/2$.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Joint Dickman law and equal ordering densities for consecutive integers | [JointDickman.lean](../ComparatorChallenges/JointDickman.lean) |
