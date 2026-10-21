# Family 003

CLAIMED (OAI dump, unrefereed); verbatim source excerpts follow.

## preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf

Source: preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex
```tex
\begin{theorem}\label{thm:main}
Every finite-order Hecke $L$-function over
$F=\mathbb Q(\sqrt{-3})$ has no zero in $\Re s>7/8$.
The same holds for every Dirichlet $L$-function, including $\zeta(s)$.
A pole at $s=1$ for a principal character is allowed.
\end{theorem}
\begin{theorem}[The $11/12$ half-plane]
\label{thm:eleven-twelfths}
Every finite-order Hecke $L$-function over $F=\mathbb Q(\sqrt{-3})$ has no
zero in $\Re s>11/12$. The same holds for every Dirichlet $L$-function,
including $\zeta(s)$. A pole at $s=1$ for a principal character is allowed.
\end{theorem}
```

## preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf

Source: preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex
```tex
\begin{theorem}\label{thm:main}
Every finite-order Hecke $L$-function over $K$ has no zeros in the half-plane $\Rea s>11/12$. Thus every Dirichlet $L$-function, including $\zeta(s)$, has no zeros for $\Rea s>11/12$.
\end{theorem}
```

## preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf

Source: preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/build/paper.tex
```tex
\begin{theorem}\label{thm:main}
There is an absolute constant $c>0$ such that every real zero
$\beta\in(0,1)$ of every primitive nonprincipal real Dirichlet
$L$-function of conductor $q\ge3$ satisfies
\begin{equation}\label{eq:main}
 (1-\beta)\log q\ge c.
\end{equation}
\end{theorem}
```

## Lean scope page (verbatim)
# The quasi-Riemann hypothesis

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\Re(s)>7/8$](../../preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)
- [Uniform exclusion of Landau–Siegel zeros](../../preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf)

## Scope

The quasi-Riemann hypothesis asks for a fixed zero-free half-plane $\Re s>\theta$ with $\theta<1$. The formalization gives $\theta=7/8$ for the Riemann zeta function and every Dirichlet $L$-function, uniformly over all positive moduli and all characters. It also establishes the same bound for finite-order Hecke $L$-functions over $\mathbb Q(\sqrt{-3})$.

The principal-character poles at $s=1$ are excluded in the Dirichlet and Hecke statements. The paper's later applications are not included.

The formalized result gives a uniform logarithmic exclusion region for Landau–Siegel zeros. There is one constant $c>0$ such that every primitive nonprincipal real Dirichlet character of conductor $q\ge3$ and every real zero $0<\beta<1$ of its $L$-function satisfy $1-\beta\ge c/\log q$.

Both character parities are included. No explicit value of $c$ is given. This excludes real zeros in $1-c/\log q<\beta<1$, but does not rule out real zeros elsewhere in $(0,1)$.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Riemann zeta $7/8$ bound | [QuasiRiemannHypothesis.lean](../ComparatorChallenges/QuasiRiemannHypothesis.lean) |
| Dirichlet $L$-function $7/8$ bound | [DirichletSevenEighths.lean](../ComparatorChallenges/DirichletSevenEighths.lean) |
| Finite-order Hecke $L$-function $7/8$ bound | [HeckeSevenEighths.lean](../ComparatorChallenges/HeckeSevenEighths.lean) |
| Uniform real-zero gap | [SiegelZeros.lean](../ComparatorChallenges/SiegelZeros.lean) |
