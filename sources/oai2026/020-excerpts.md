# Family 020

CLAIMED (OAI dump, unrefereed); verbatim source excerpts follow.

## preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/manuscript.pdf

Source: preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/build/sections/01-introduction.tex
```tex
\begin{theorem}\label{thm:density}
Let $f\in\Z[x]$ be irreducible over $\Q$, of degree $d$ with
$4\le d\le8$, and put $k=d-2$. If \eqref{eq:local-admissibility} holds,
then
\[
 S_{f,k}(X)=c_{f,k}X+o_f(X),\qquad
 c_{f,k}=\prod_p\left(1-\frac{\rho_f(p^k)}{p^k}\right)>0.
\]
No primitivity or sign condition on the leading coefficient is required.
\end{theorem}
```

Source: preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/build/sections/03-affine-counting.tex
```tex
\begin{theorem}\label{thm:affine-counting}
Fix integers $1\le r\le N$, a degree bound $e_0$, a constant $C$, positive coordinate
weights $\omega_l$, and positive numbers $\delta_1,\ldots,\delta_r$.
For $X\ge2$, let $S\subseteq\Z^N$ satisfy
\[
 |z_l|\le C X^{\omega_l}\quad(z\in S),
\]
and suppose $S$ lies on an algebraic set $Z$ of degree at most $e_0$
and dimension at most $r$.  Assume the following uniform alternative.
For every fixed degree bound $e$, each irreducible subvariety
$A\subseteq Z$ defined over $\Q$, of degree at most $e$ and dimension
$h>0$, meeting $S$, satisfies either
\begin{equation}\label{eq:affine-exception}
 |S\cap A|\ll_{e,\alpha} X^\alpha
 \quad\text{for every fixed }\alpha>0,
\end{equation}
or
\begin{equation}\label{eq:affine-hilbert-input}
 H_A(T)\ge \frac{T^h}{h!\delta_h^h}-C_eT^{h-1}
 \quad(T\ge1).
\end{equation}
The constants in these alternatives are uniform in $X,Z,S,A$.
Put $E_h=\max_{h\le s\le r}\delta_s$.  Then, for every $\eps>0$,
\begin{equation}\label{eq:affine-counting-conclusion}
 |S|\ll_\eps X^{E_1+\cdots+E_r+\eps}.
\end{equation}
The implied constant depends only on the fixed data and the uniform
constants in the hypotheses.  In particular, no bound on the
coefficients initially defining $Z$ is required.
\end{theorem}
```

## Lean scope page (verbatim)
# Squarefree quartics and power-free polynomial values

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Squarefree values of quartics and power-free values of polynomials](../../preprints/Squarefree-values-of-quartics-and-power-free-values-of-polynomials-September-24-2026/manuscript.pdf)

## Scope

The formalized result proves positive-density power-free values for every integer polynomial $f$ irreducible over $\mathbb Q$ of degree $d\ge4$. Put $k=d-2$ and assume no prime $k$th power divides every value of $f$. Then the number of positive integers $n\le X$ for which $f(n)$ is $k$-free is $c_fX+o_f(X)$, where $c_f>0$ is the convergent product of local factors. Negative values are allowed and zero is excluded. No monicity, primitivity, or coefficient-height restriction is imposed.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Positive density of power-free polynomial values | [PowerFreeValues.lean](../ComparatorChallenges/PowerFreeValues.lean) |
