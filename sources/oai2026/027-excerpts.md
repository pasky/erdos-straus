# Family 027

CLAIMED (OAI dump, unrefereed); verbatim source excerpts follow.

## preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/paper.pdf

Source: preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/build/sections/diagrams.tex
```tex
\begin{theorem}[Diagram density]\label{thm:diagram-density}
For every surface diagram $D$ with ranks at most $r$ and prescribed
scalar puncture monodromies in $F$, its integral solutions over $R$
are Zariski dense in $\mathcal S(D)$.
\end{theorem}
```

Source: preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/build/sections/introduction.tex
```tex
\begin{theorem}\label{thm:main}
Let $X$ be a smooth connected complex algebraic curve and let $r\geq1$.
For prescribed quasi-unipotent conjugacy classes $C_1,\ldots,C_s$ as above,
let $K\subset\C$ be a number field containing their eigenvalues. There is
a finite extension $L/K$ such that
\[
 M_r(X)(\cO_L)\cap Y(\C)
\]
is Zariski dense in $Y$, and hence in every irreducible component of $Y$.
The same conclusion holds when only the characteristic polynomial of
each boundary monodromy is prescribed, with all its roots roots of unity.
It also holds for the entire character variety without boundary
conditions; in that case one may take $K=\Q$.

For the relative statements and for projective $X$, one may take distinct
primes $p,q>r$ and
\begin{equation}\label{eq:main-field}
 F=K(\sqrt2,\zeta_{pq}),\qquad
 L=F\bigl(\zeta_r,\{u^{1/r}:u\in\cO_F^\times\}\bigr),
\end{equation}
where $\zeta_m$ denotes a primitive $m$th root of unity. In the projective
case there are no boundary conditions and $K=\Q$.
\end{theorem}
```

## Lean scope page (verbatim)
# Potential integral density on curve character varieties

The following describes the scope of the Lean formalization related to the following accompanying paper(s):

- [Integral points on character varieties of curves](../../preprints/Integral-points-on-character-varieties-of-curves-September-25-2026/paper.pdf)

## Scope

The integral-density question asks whether integral points become Zariski dense in every component of a curve character variety after one finite extension of the number field. The linked formalization proves a supporting compatibility result for its marked-surface construction. Given a proper diagram with finitely many vertices, a chosen seam with maximal adjacent facet rank and a positive-genus parent, puncture data, an existing solution over a field, and a chosen boundary occurrence, the produced marked values satisfy every seam equation.

This is conditional compatibility of the produced solution. Potential integral density, including the prescribed-boundary and all-component conclusions, remains outside the selected statement.

## Comparator links

| Result | Comparator statement |
| --- | --- |
| Compatibility of the produced marked solution with every seam equation | [CharacterVarietiesAllSeamsSupport.lean](../ComparatorChallenges/CharacterVarietiesAllSeamsSupport.lean) |
