# Family 182

CLAIMED (OAI dump, unrefereed); verbatim source excerpts follow.

## preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/power-saving-intersective-polynomial-differences.pdf

Source: preprints/A-power-saving-for-intersective-polynomial-differences-with-an-exponent-depending-only-on-the-degree-October-5-2026/build/manuscript/sections/introduction.tex
```tex
\begin{theorem}\label{thm:main}
For every integer $k\ge2$, there is a constant $c_k\in(0,1)$ with the
following property. For every intersective polynomial $h\in\Z[x]$ of degree
$k$ with positive leading coefficient, there are a constant $C_h\ge1$ and an
integer $N_h\ge1$ such that, whenever $N\ge N_h$ and $A\subseteq[N]$ satisfy
\[
 (A-A)\cap h(\N_+)\subseteq\{0\},
\]
one has
\[
 |A|\le C_h N^{1-c_k}.
\]
\end{theorem}
```

## preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/prime-argument-polynomial-differences.pdf

Source: preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/build/sections/introduction.tex
```tex
\begin{theorem}\label{thm:main}
Let $h\in\Z[x]$ be prime-intersective, of degree at least two and with
positive leading coefficient. There exist constants $c_h>0$ and
$C_h\ge1$ such that, for every positive integer $N$ and every
$A\subseteq[N]$,
\[
 (A-A)\cap\{h(p):p\in\mathbb P\}\subseteq\{0\}
 \quad\Longrightarrow\quad
 |A|\le C_h N^{1-c_h}.
\]
\end{theorem}
```

Source: preprints/A-Power-Saving-for-Polynomial-Differences-at-Prime-Arguments-October-5-2026/build/sections/primes.tex
```tex
\begin{theorem}[Zero-free input, {\cite[Theorem~1.1]{ZeroFree}}]
\label{thm:zero-free-input}
For every integer $b\ge1$ and every Dirichlet character $\chi$ modulo
$b$, the Dirichlet $L$-function $L(s,\chi)$ has no zero in
$\Re s>7/8$.  This includes imprimitive characters and the trivial
character of modulus $1$, whose $L$-function is $\zeta(s)$.  A pole at
$s=1$ for a principal character is allowed.
\end{theorem}
```

## preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/paper.pdf

Source: preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/build/sections/induction.tex
```tex
\begin{theorem}\label{thm:functional-decay}
There are absolute constants $a_0>0$ and $C_0<\infty$ such that, for every
positive integer $N$ and every square-difference-free set $A\subseteq[N]$,
\[
 Y(N,A)\le C_0N^{-a_0}.
\]
\end{theorem}
```

Source: preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/build/sections/introduction.tex
```tex
\begin{theorem}
\label{thm:main}
There are absolute constants $c>0$ and $C<\infty$ such that, for every
integer $N\ge1$ and every square-difference-free set $A\subseteq[N]$,
\[
 |A|\le C N^{1-c}.
\]
Equivalently, every subset of $[N]$ larger than $C N^{1-c}$ contains
distinct elements whose absolute difference is the square of a positive
integer.
\end{theorem}
```

## Lean scope page (verbatim)
# Power savings for intersective polynomial differences and prime arguments

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [A power saving for square-difference-free sets](../../preprints/A-power-saving-for-square-difference-free-sets-September-24-2026/paper.pdf)

## Scope

The formalization proves a fixed power saving for sets with no nonzero square difference. There are absolute constants $c>0$ and $C$ such that every $A\subseteq\{1,\ldots,N\}$ satisfying $a-b\ne m^2$ for all $a,b\in A$ and integers $m\ge1$ has $|A|\le C N^{1-c}$. The bound is uniform for every integer $N\ge1$.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Power saving for square-difference-free sets | [SquareDifference.lean](../ComparatorChallenges/SquareDifference.lean) |
