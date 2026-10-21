# Family 028

CLAIMED (OAI dump, unrefereed); verbatim source excerpts follow.

## preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf

Source: preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex
```tex
\begin{theorem}[One-step coverage transfer]\label{thm:transfer}
Use the signed coordinates and the experiment just defined, with
integers $1\le s\le k$ and $n\ge1$. Let
\[
 0<\tau\le3/8,\quad 0<\delta\le1/64,\quad
 \tau'=\tau+4\delta,\quad 0<\beta'\le\beta<1,
 \quad 0<\eta\le1,\quad 0\le\eta'\le1.
\]
Suppose that at every $a$ in the support of $A$, all but a fraction at
most $\eta'$ of the signed coordinates have $(\tau',\beta')$ coverage
for $\phi_c(y(a)+h_1)$ under the law conditional on $A=a$.
Assume also
\begin{align}
 \E_S H(F_S(Y))&\ge(1-\epsilon)s\overline L,
 &H(\calH)&\le\kappa s\overline L,\label{eq:transfer-entropy}\\
 \eta'&\le\eta\delta/100,
 &\epsilon+\kappa&\le\eta\delta\beta'/16,\label{eq:transfer-budget}
\end{align}
where $\epsilon,\kappa\ge0$. Finally, for every coordinate size $p=p_j$,
assume
\begin{align}
 p\exp(-\delta^2np^{-\beta}/2)&\le\delta/100,
 &\delta^{-1}&<p^{\beta'/2},\label{eq:transfer-size}\\
 \log(2e/\delta)&\le(\beta'/4)\log T.\label{eq:transfer-log}
\end{align}
Then all but a fraction at most $\eta$ of the coordinates have
$(\tau,\beta)$ coverage for $\phi_c(Z)$.
\end{theorem}
```

Source: preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/main.tex
```tex
\begin{theorem}[Uniform component bound]\label{thm:main}\label{cor:uniform}
For every finite real $D$ there is a finite $B_D$ such that every
connected component of $G_D$ has at most $B_D$ vertices.
The bound is independent of the starting prime and includes primes on
the coordinate axes. Consequently every sequence of distinct Gaussian
primes whose successive distances are at most $D$ has at most $B_D$ terms.
\end{theorem}
\begin{theorem}[Finite sieve obstruction]\label{thm:sieve}
For every $D\ge1$ there is a finite set $\mathcal P_D$ of rational
primes congruent to $1$ modulo $4$ such that $\mathcal A(\mathcal P_D)$
contains no infinite sequence of distinct points with successive distances
at most $D$. The set $\mathcal P_D$ depends only on $D$.
\end{theorem}
```

## Lean scope page (verbatim)
# Uniformly bounded components of Gaussian-prime graphs

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Bounded-Step Walks on Gaussian Primes](../../preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf)

## Scope

The Gaussian moat problem asks whether an infinite walk through distinct Gaussian primes can have bounded step lengths. The formalized result gives a negative answer for every real step bound $D$. More strongly, one finite bound depending only on $D$ limits the size of every connected component of the bounded-step graph and the length of every injective bounded-step walk. Axis primes and all associates are included. No explicit function of $D$ is supplied.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Uniform bounds for bounded-step Gaussian-prime walks | [GaussianMoat.lean](../ComparatorChallenges/GaussianMoat.lean) |
