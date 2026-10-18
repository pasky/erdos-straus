# z35_modp_least_residue — the b = 1 line in mod-p coordinates and the residue-symbol content of a certificate (O265)

## Idea
Swap moduli (O263 spark 1): write the b = 1 line so that p is the modulus and the parameters are small, and ask which part of
the decisive condition is a power-residue condition mod π | p. Result (MODP_RECIPROCITY Prop 1.1/1.2): the line is one equation
4md − g = p, g | m + 1 (the height-one solution of 4md ≡ g (mod p)); equivalently "the least residue −p mod 4m divides m + 1".
Quadratic symbols of all certificate data are Jacobi symbols among the parameters (T1 sign, forced); quartic symbols are
functions of (a, b) modulo the parameters (Gauss–Dirichlet–Burde) — genuine Gaussian data, but outputs, not criteria.

## Literature
López, arXiv:2404.01508 (Type A = b = 1); (J)85 least-residue windows; Burde, J. reine angew. Math. 238 (1969) (rational
quartic reciprocity); Ireland–Rosen Ch. 9; Lemmermeyer, *Reciprocity Laws* (2000) Ch. 5–6.

## Barrier screen
B2: the condition is the height-one equation — additive, not a power class. B1: bounded m is a congruence on p. T1: the quadratic
part is the T1 sign. B5 consistent (squares: no certificate). Numerator 8: the dictionary is 4-specific only through 4m; the
same least-residue form exists for k/p — numerator-blind (as expected of a dictionary).

## Cheap numerics
`scripts/z35_checks.py`: the (d, w) and (m, g) sets coincide for 1125 primes < 2·10⁴; (w/p) = −1 and (w/p)_4(g/p)_4 = (2/p)(d/p)_4
on 2716 certificates; Burde on 2158 pairs; `scripts/z35_quartic_function.py`: (q/p)_4 is a function of (a, b) mod (4q, 8q).

## Assessment
PROVED dictionary (elementary). No power-residue reformulation of the target exists: the target is an arithmetic progression in
[1, p), power classes are multiplicative cosets. Closes goal (1) negatively.
