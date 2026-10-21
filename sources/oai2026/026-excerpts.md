# Family 026

CLAIMED (OAI dump, unrefereed); verbatim source excerpts follow.

## preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/main.pdf

Source: preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/build/sections/01-introduction.tex
```tex
\begin{theorem}\label{thm:main}
For every fixed real $C>0$, there are constants $c(C)>0$ and $N_0(C)$
such that, for every integer $N\ge N_0(C)$,
\[
 \#\{1\le n\le N:p_{n+1}-p_n>C\log p_n\}\ge c(C)N.
\]
\end{theorem}
```

## Lean scope page (verbatim)
# Positive lower density of large prime gaps

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Positive lower density of large prime gaps](../../preprints/Positive-lower-density-of-large-prime-gaps-September-25-2026/main.pdf)

## Scope

The formalized supplement proves that the indices $n$ for which $p_n/n<p_{n+1}/(n+1)$ have positive lower asymptotic density, where $p_n$ is the $n$th prime. Thus the normalized prime sequence has a positive-density set of increases. This is the prime-ratio corollary associated with the paper's theorem on a positive lower density of large prime gaps.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Positive lower density of prime-ratio increases | [PrimeGaps.lean](../ComparatorChallenges/PrimeGaps.lean) |
