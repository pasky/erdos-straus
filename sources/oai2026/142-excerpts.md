# Family 142

CLAIMED (OAI dump, unrefereed); verbatim source excerpts follow.

## preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/Deterministic-Polynomial-Factorization-over-Prime-Fields.pdf

Source: preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/build/sections/00-introduction.tex
```tex
\begin{theorem}\label{thm:factorization}
There is a uniform deterministic algorithm that, given a prime $p$ in
binary and a nonzero dense polynomial $f\in\Fp[x]$ of degree $n$, outputs
its leading coefficient and its distinct monic irreducible factors with
their multiplicities in
\[
 O\bigl(((n+1)\lceil\log_2p\rceil)^{10^{12}}\bigr)
\]
bit operations, with absolute implied constant. A constant polynomial
returns an empty factor list. The algorithm uses no randomness,
integer-factorization oracle, primitive-root oracle, or GRH assumption.
\end{theorem}
\begin{theorem}\label{thm:reduction}
There is a uniform deterministic algorithm with the following guarantee.
Its input is a prime $p$ and a nonzero dense polynomial $f\in\Fp[x]$.
If $p>B^{200000}$ and $n\ge2$, its input also includes one auxiliary
prime $\ell_q$ satisfying \eqref{eq:auxiliary} for each prime $q\le n$.
It outputs the complete factorization of $f$, including multiplicities.
Let $E=\max(2,\max_q\ell_q)$, with $E=2$ when no auxiliary primes are
required. For an absolute constant $C$, the algorithm uses
$O((B+E)^C)$ bit operations. It uses neither randomness nor an integer
factorization or primitive-root oracle.
\end{theorem}
```

Source: preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/build/sections/03-norms.tex
```tex
\begin{theorem}[Promised norm solver]\label{norm:solve}
Let $k$ be an explicitly represented finite field of characteristic $p$,
let $q$ be an odd prime, and suppose that a primitive $q$th root of unity
$\zeta\in k$ and a generator of the full $q$-primary subgroup of $k^*$
are given.  Let $F\in k[X]$ be monic and square-free, of positive degree
$N$ divisible by $q$.  Put
\[
 K_0=k(X),\qquad
 \mathcal L=K_0[Y]/(Y^q-F),\qquad \rho(Y)=\zeta Y.
\]
Let $G\in K_0^*$, write $D$ for the maximum of its reduced numerator
and denominator degrees, and assume
\begin{equation}\label{norm:characteristic}
 p>(N+2D+1)^2.
\end{equation}
If $G$ belongs to $\operatorname{Norm}_{\mathcal L/K_0}(\mathcal L^*)$, a deterministic
algorithm constructs $h\in \mathcal L^*$ with
\[
 \prod_{j=0}^{q-1}\rho^j(h)=G.
\]
Its bit complexity, and the degrees of the rational coefficients of
$h$ in the basis $1,Y,\ldots,Y^{q-1}$, are bounded by fixed polynomials
in $q,N,D$, and $\log|k|$.  It uses no polynomial factorization oracle.
Its field-dependent branches use only zero tests, so the algorithm
admits the simultaneous execution of Lemma~\ref{ff:simultaneous}.
\end{theorem}
```

Source: preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/build/sections/10-analytic.tex
```tex
\begin{theorem}[\cite{OpenAIPrimitive26}, Theorem~1.2]\label{analytic:hecke}
For every cyclotomic number field $K$ containing the twelfth roots of
unity, and every finite-order Hecke character $\chi$ of $K$, the Hecke
$L$-function $L_K(s,\chi)$ has no zero in
\[
 \Re s>1-\delta,\qquad \delta=10^{-6}.
\]
The principal character is included, with its pole at $s=1$ permitted.
There is no restriction on conductor or imaginary part.
\end{theorem}
```
