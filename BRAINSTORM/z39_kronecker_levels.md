# z39_kronecker_levels — each ES level is a Kronecker theta quotient at a torsion point (O269)

**ES is not solved here.** Labels as in DISCOVERIES.md. Deep version: METAPLECTIC_ES.md §1 (Thm K, Cor K1).

## Idea
The level-t ES words tuv − u − v = n are the positive quadrant of the split indefinite "theta series"
Σ q^{tuv−u−v}. Split quadrant sums are exactly what Kronecker's double-series identity evaluates: find the modular
object behind each level and see where the log² main term and T1 sit.

## Result (PROVED, classical input)
With X = q^{t−1}, Q = q^t, θ(x) = (x;Q)(Q/x;Q):
Σ_{u,v≥2} q^{tuv−u−v} − Σ_{r,s≥0} q^{trs+r+s} = q^{t−2}[(Q;Q)²θ(X²)/θ(X)² − (1+X)/(1−X)].
The theta quotient is Kronecker's F_{τ'}(z,z) = θ'(0)θ(2z)/θ(z)² at τ' = tτ, z = (t−1)τ'/t (a t-torsion point):
a weight-1 holomorphic Eisenstein series (odd characters mod t). The partner quadrant plus the ES quadrant is the
even-character divisor sum = coefficients of a weight-0 Maass Eisenstein series at s = ½. Per level:
R_t(n) = ½E_t(tn+1) + ½O_t(tn+1) − β_t(n), no cusp forms anywhere.

## Literature
Kronecker (1881); A. Weil, *Elliptic functions according to Eisenstein and Kronecker* (1976) Ch. VIII; D. Zagier,
"Periods of modular forms and Jacobi theta functions", Invent. Math. 104 (1991) 449–465, §3; L. Borisov–P. Gunnells,
"Toric modular forms", Invent. Math. 144 (2001) 297–325 (Kronecker quotients at torsion points as weight-1 Eisenstein
series); Hickerson–Mortenson, Proc. LMS 109 (2014) (Hecke-type double sums; ours is the degenerate split case
a = c = 0 with no Appell–Lerch/mock part).

## Barrier screen
* (J)39 Thm 2.2 (no finite sum of holomorphic forms): consistent — R is an *infinite* sum over levels of mixed
  weight-0/weight-1 Eisenstein data; each level is modular, the sum is not (B2: the level t is a solution coordinate).
* B3: the log² main term is in the weight-0 non-holomorphic part (τ(N) via ∂_sE at s = ½, times Σ_t 1/φ(t)); the
  holomorphic part averages ≈ 0 at primes. A "main Eisenstein term + cusp bound" argument has nothing to bound.
* T1/B5: at squares, on every level 4 | t, the holomorphic coefficient equals minus the Maass one (Cor K1.1).
* B2 / red team Thm 2.2: per level this is the {t}-fibre (a single divisor-in-class event at tn+1); Eisenstein-only
  is the automorphic form of Thm 2.2(ii) ("only congruence/genus data").
* B1, B4, B6, Thm 9.1, Prop 10.3: not engaged (no covering, no averaging over n, no finite menu).

## Cheap numerics
`scripts/z39_kronecker.py` (identity at t ≤ 6 numerically, coefficient form t ≤ 30, n ≤ 1500: 0 failures);
`scripts/z39_split.py` (size split at primes ≈ 10⁵ and odd squares).

## Assessment
PROVED exact dictionary, new to the campaign (classical ingredients). Explains *where* log² and T1 live; gives no
existence mechanism. Promise 1/5 as a route; useful as the correct automorphic normal form of R(n).
