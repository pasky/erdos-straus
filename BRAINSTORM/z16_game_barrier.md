# z16_game_barrier — Schmidt-type games cannot prove O(3, T²) ≠ ∅: fixed-radius obstacles (O241)

## Idea
FF_THIRDS_CORNER §6: the obstructed slice set U_c is the complement of T-adic balls around "tuple rationals" −w₁/C₁, i.e.
a set of points badly approximable by tuple rationals. Badly approximable sets are Schmidt-winning (Schmidt 1966), absolute
winning (McMullen 2010), and potential-game winning (Fishman–Simmons–Urbański 2018); winning sets survive countable
intersections and need only local counts. Try to make U_c winning.

## Literature
W. M. Schmidt, On badly approximable numbers and certain games, Trans. AMS 123 (1966) 178–199; C. T. McMullen, Winning sets,
quasiconformal maps and Diophantine approximation, GAFA 20 (2010) 726–740; L. Fishman, D. Simmons, M. Urbański, Diophantine
approximation and the geometry of limit sets in Gromov hyperbolic metric spaces, Mem. AMS 254 (2018) (potential game);
S. Kristensen, Badly approximable systems of linear forms over a field of formal series, J. Théor. Nombres Bordeaux 18 (2006)
421–444 (function-field Bad is winning); B. de Mathan, Approximations diophantiennes dans un corps local, Bull. SMF Mém. 21 (1970).

## Barrier screen
The failure is structural, before B1–B6: winning sets are dense (Bob opens anywhere), U_c is closed and misses the s = 4
ball, so U_c is never winning (STERILE_DIOPHANTINE Thm 2.1, PROVED). The hypothesis games need and we lack: a *shrinking
constant* — Bad = ⋃_κ Bad(κ); winning gives only ⋃_k U_c^{(k)} (balls shrunk by k digits), strictly weaker than U_c ≠ ∅.
A renormalisation Φ with Φ^{−1}(B) ⊂ shrunk tuple ball would bridge it; Frobenius (z16_frobenius) goes the wrong way.
T1/B5 not engaged (FF model). Prop 10.3/Thm 9.1: not applicable.

## Cheap numerics
None needed (the obstruction is a two-line topological fact); the covered depth-3 ball is in `data/z16/tree_d9.txt`.

## Assessment
PROVED negative (exact scope: every game whose first move is an arbitrary ball). Positive-dimension Cantor arguments are not
affected — see z16_windowed_konig.
