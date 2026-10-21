# Family 029

CLAIMED (OAI dump, unrefereed); verbatim source excerpts follow.

## preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/primitive-roots-all-integer-bases.pdf

Source: preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/01-introduction.tex
```tex
\begin{theorem}\label{thm:primitive-root}\label{thm:main}
For every admissible integer $a$, there are constants $c_a>0$ and
$x_a\ge2$ such that, for every real $x\ge x_a$,
\[
 \#\{p\text{ prime}:x<p<2x,\ p\nmid a,\ \ord_p(a)=p-1\}
       \ge c_a\frac{x}{(\log x)^2}.
\]
\end{theorem}
\begin{theorem}\label{thm:hecke-zero-free}
Let $F$ be a cyclotomic number field containing $\mu_{12}$.
For every finite-order Hecke character $\eta$ of $F$, the meromorphic
continuation of $L_F(s,\eta)$ has no zeros in
\[
 \re s>1-10^{-6}.
\]
\end{theorem}
```

Source: preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/01a-reduction.tex
```tex
\begin{proposition}[Primes with controlled predecessors]
\label{prop:controlled}\label{prop:prime-reservoir}
Let $M$ be a fixed positive multiple of $8$, let $c\in\{2,4\}$, and let
$u$ be an integer satisfying
\begin{equation}
 (u,M)=1,\qquad c\mid u-1,\qquad
 \left(\frac{u-1}{c},\frac Mc\right)=1.
 \label{alg:progression-conditions}
\end{equation}
For every sufficiently large real $x$, there are
$\gg_{M,c,u}x/L^2$ distinct primes $p\in(x,2x)$ satisfying
\begin{equation}
 p\equiv u\pmod M,\qquad p-1=crQ,
 \qquad Q>x^{0.9}\ \text{prime},
 \label{eq:controlled-predecessor}
\end{equation}
where $r$ is a positive integer all of whose prime divisors lie in
\[
 \bigl(\exp(L^{0.1}),\exp(L^{0.3})\bigr).
\]
\end{proposition}
\begin{proposition}[Uniform bound for complete splitting]
\label{prop:splitting}
Fix an integer $a$ with $|a|>1$, and put $\delta_0=10^{-6}$.
For all sufficiently large real $x$ and all primes $q$ sufficiently
large in terms of $a$, with $q\le\exp(L^{0.3})$, one has
\begin{equation}
 \#\{p\text{ prime}:x<p\le2x,\ p\text{ splits completely in }K_q\}
 \ll_a \frac{x}{q(q-1)L}+x^{1-\delta_0}.
 \label{eq:uniform-splitting}
\end{equation}
The implied constant and the threshold for $x$ are independent of $q$.
For $a=2$, every prime $q\ge5$ is allowed, with absolute constants and
an absolute threshold for $x$.
\end{proposition}
```

Source: preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026/build/sections/08-type-ii.tex
```tex
\begin{theorem}[One-sided marked Type II estimate]\label{thm:marked-type-ii}
Fix \(\delta,C,D_*>0\) and \(q\in(0,1)\).  Suppose
\(H_m,H_n\ge x^\delta\) and \(X=H_mH_n\asymp x\).  Let \(F\) satisfy
\(|F(h)|\le1\) and \(F(ph)=F(h)\) for every prime in the groups
defined in \Cref{eq:marked-prime-groups}.  Let \(\alpha_m\) be supported on an
arbitrary interval in \([H_m,2H_m]\), where it has the value
\[
 \alpha_m=m^{iv}\left(\one_{m\text{ prime}}
       -\frac{\one_{P^-(m)>W}}{V(W)\log m}\right),
 \qquad |v|\le L^C.
\]
Let \(\beta_n\) be supported on \(W\)-rough integers in \([H_n,2H_n]\),
with \(|\beta_n|\le L^C\).  If \(K\) is sufficiently large in terms of
\(\delta,C,D_*,q\), then
\begin{equation}\label{eq:marked-type-ii}
 \left|\sum_{m,n}\alpha_m\beta_n F(mn-1)\mathcal W(mn-1)\right|
       \ll X L^{-D_*}.
\end{equation}
The required lower bound on \(K\) is independent of the particular
\(a_i\).  The implicit constant and the threshold for \(x\) may depend
on all the fixed parameters, including the \(a_i\).
\end{theorem}
```

## preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/simultaneous-primitive-roots-conditional-lower-bound-prime-bases.pdf

Source: preprints/Simultaneous-primitive-roots-a-conditional-lower-bound-for-prime-bases-October-4-2026/build/sections/01-introduction.tex
```tex
\begin{theorem}\label{thm:main}
Assume Inputs~\ref{input:hecke}, \ref{input:marked},
\ref{input:block}, and~\ref{input:density}.  Let \(k\ge1\) and let
\(q_1,\ldots,q_k\) be distinct positive primes.  There are constants
\(c_{\mathbf q}>0\) and \(x_{\mathbf q}>1\) such that, for every real
\(x\ge x_{\mathbf q}\), at least
\[
        c_{\mathbf q}\frac{x}{(\log x)^2}
\]
primes \(p\in(x,2x)\) satisfy
\[
        p\nmid q_1\cdots q_k,
        \qquad
        \ord_p(q_i)=p-1\quad(1\le i\le k).
\]
\end{theorem}
```
