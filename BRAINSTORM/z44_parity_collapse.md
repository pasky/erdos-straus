# z44_parity_collapse — the k-th power ladder ES_(k) carries one bit (O276)

## Idea
O274 spark 1: ES_(k): 4/n = 1/x + 1/y + Q^k/Z (lowest terms, Q odd prime to n). ES_(2) = ES^□ is a one-prime theorem;
is ES_(3) provable pointwise (cubic reciprocity?) or a lottery?

## Literature
Definition generalises UNIT_ORBIT_ES §1 / SYNTHESIS_SPARKS2 §2 (ES^□). Polynomial-identity coverings of ES classes:
Mordell, *Diophantine Equations* (1969) §30; Vaughan, Mathematika 17 (1970). No published k-th power variant found
(Assessment; no web search done).

## Barrier screen
B1/B5/T1: odd k has NO T1 (tame symbol a^{−w}, w odd, unconstrained) and accordingly a finite covering exists (mod 4).
Even k: T1 intact (den z is a square), no shot covering. B2: the ladder never touches "Q = 1"; it does not interpolate.
B3/B6: not used (one identity / one Dirichlet prime). Thm 9.1 / Prop 10.3: not engaged.

## Cheap numerics
`scripts/z44_ladder.py 1000000` (8 s): k = 3, 5 all primes ≤ 10⁶ with Q ≤ 3, all odd squares/cubes with Type I shape;
k = 2, 4, 6 all primes via one r (max r 131 / 131 / 251), 0 shots at odd squares; numerator 8 at 131, 241 solved.

## Assessment
PROVED (POWER_LADDER_ES Thm 2.1, 2.3, Cor 2.5): odd k ⟹ ES_(k)(n) for all n by 4x = n + Q^k, Q ≡ −n (4); even k ⟹
ES^□-like (one Dirichlet prime, T1). Every rung holds at every n ≥ 2. The "headline candidate" ES_{Q³} is true for a
trivial reason and calibrates nothing between ES^□ and ES. The O274 §3.2 index calibration is repaired (POWER_LADDER §3:
calibrate at the best single modulus, index 1 or 2).
