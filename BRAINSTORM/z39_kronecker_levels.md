# z39_kronecker_levels — each ES level is a Kronecker theta quotient at a torsion point (O269)

**ES is not solved here.** Labels as in DISCOVERIES.md. Deep version: METAPLECTIC_ES.md §1 (Thm K, Cor K1).

## Idea
The level-t ES words tuv − u − v = n are the positive quadrant of the split indefinite "theta series"
Σ q^{tuv−u−v}. Split quadrant sums are exactly what Kronecker's double-series identity evaluates: find the modular
object behind each level and see where the log² main term and T1 sit.

## Result (PROVED, classical input)
With X = q^{t−1}, Q = q^t, θ(x) = (x;Q)(Q/x;Q):
Σ_{u,v≥2} q^{tuv−u−v} − Σ_{r,s≥0} q^{trs+r+s} = q^{t−2}[(Q;Q)²θ(X²)/θ(X)² − (1+X)/(1−X)].
The theta quotient is (up to the Jacobi exponential normalisation, not carried out; the raw series has a −q^{2−t}
term) Kronecker's F_{τ'}(z,z) = θ'(0)θ(2z)/θ(z)² at τ' = tτ, z = (t−1)τ'/t (a t-torsion point). PROVED (R280 repair, D1):
q^{t−2}·(theta quotient) has coefficients exactly (D⁻_t − D⁺_t)(tn + 1) = −(2/φ(t))Σ_{χ odd}σ_χ(tn + 1) (weight-1
Eisenstein data), and the boundary series q^{t−2}(1+X)/(1−X) has coefficients β_t(n) = 2·1[(t−1) | (n+1)] − 1[n = t−2]. The partner quadrant plus the ES quadrant is the
even-character divisor sum = coefficients of a weight-0 Maass Eisenstein series at s = ½. Per level:
R_t(n) = ½(D⁻ + D⁺)(tn+1) + ½(D⁻ − D⁺)(tn+1) − β_t(n), every term a Dirichlet-character divisor sum (no cusp
forms). Novelty (R280 D2): classical identity; the coefficient content (divisors ≡ −1 mod t of tn + 1) is the
standing campaign reformulation; new only as a q-series packaging in the campaign.

## Literature
Kronecker (1881); A. Weil, *Elliptic functions according to Eisenstein and Kronecker* (1976) Ch. VIII; D. Zagier,
"Periods of modular forms and Jacobi theta functions", Invent. Math. 104 (1991) 449–465, §3; L. Borisov–P. Gunnells,
"Toric varieties and modular forms", Invent. Math. 144 (2001) 297–325 (weight-r forms on Γ₁(l) from rank-r fans,
built from Kronecker-type quotients at torsion points; title corrected per R280 D10); section pointers not re-checked; Hickerson–Mortenson, Proc. LMS 109 (2014) (Hecke-type double sums; ours is the degenerate split case
a = c = 0 with no Appell–Lerch/mock part).

## Barrier screen
* (J)39 Thm 2.2 (no finite sum of holomorphic forms): consistent — R is an *infinite* sum over levels of mixed
  weight-0/weight-1 Eisenstein data; each level is modular, the sum is not (B2: the level t is a solution coordinate).
* B3 (R280 repair, D4): only after removing the trivial divisors 1, N at every level (a non-modular renormalisation of
  total size ≍ n) does the even part carry the log² and the odd part average ≈ 0 — elementary equidistribution of
  non-trivial divisors between ±1 mod t, not an automorphic fact. Robust point: no cusp form at any level, so a
  "main Eisenstein term + cusp bound" argument has nothing to bound.
* T1/B5: D⁻_t(tm² + 1) = 0 for 4 | t, all m (classical); in even/odd language E_t + O_t = 0 (a relabelling, Cor K1.1).
* B2 / red team Thm 2.2: per level this is the {t}-fibre (a single divisor-in-class event at tn+1); Eisenstein-only
  is the automorphic form of Thm 2.2(ii) ("only congruence/genus data").
* B1, B4, B6, Thm 9.1, Prop 10.3: not engaged (no covering, no averaging over n, no finite menu).

## Cheap numerics
`scripts/z39_kronecker.py` (identity at t ≤ 6 numerically, coefficient form t ≤ 30, n ≤ 1500: 0 failures);
`scripts/z39_split.py` (size split at primes ≈ 10⁵ and odd squares).

## Assessment
Identity and coefficient formula PROVED (classical ingredients, new to the campaign); modular reading Assessment. Explains *where* log² and T1 live; gives no
existence mechanism. Promise 1/5 as a route; useful as the correct automorphic normal form of R(n).
