# s9_no_fixed_integer — can R(n) be repackaged as a weighted divisor sum of ONE integer, so that Dirichlet/Hecke positivity applies? (O271, mandatory (ii))

## Idea
The brief: rearrange the exact formula R(n) = Σ_t[½E_t(tn+1) + ½O_t(tn+1) − β_t(n)] (O269 Thm K) as Σ_{d|F(n)} w(d) over the divisors of
a fixed integer or a short family, so that the lower tail becomes positivity of an explicit Dirichlet-series coefficient (e.g.
coefficients of ζ(s)L(s, χ) or of products of L-functions, which are ≥ 0 by Hecke/representation theory).

## Literature
O269 Thm K; (J)89 Lemma 2.3 (gcd(jp + 1, j′p + 1) | j − j′; large primes private to one shift); Dirichlet's class-number
formula Σ_{d|N} χ_D(d) = R_D(N)/w_D; (J)39/(J)48 (no holomorphic modular generating function by size).

## Analysis
* Two exact dual forms exist: R(n) = Σ_t #{d | tn + 1 : d ≡ −1 (t), size} and R(n) = Σ_u #{e | n + u : e ≡ −1 (u), size}. Both run
  over moving families of pairwise almost-coprime integers (gcd | t − t′, resp. u − u′). A divisor sum of one F(n) reproducing R(n)
  needs every prime factor of every tn + 1 that can occur in a certificate to divide F(n): F(n) ≥ lcm over ≍ n levels,
  astronomically large; its divisor sum restricted by w is R(n) restated (Assessment; B2).
* Positivity of explicit coefficients: the only positive coefficient sequences in sight are σ_χ(N) for real χ (= R_D(N)/w ≥ 0,
  representation numbers). In R_t they enter with a MINUS sign: D⁻_t ≤ (τ − σ_{χ_{−t}})/2 (SYNTHESIS_SPARKS9 Prop 2.1); for
  φ(t) = 2 exactly D⁻ = (τ − σ_χ)/2 (O269 C6). So ES at a level is the *failure* of N to be a norm-type number; Hecke positivity
  (lower bounds for R_D) bounds ES counts from above. The sign of the needed inequality is wrong for every Eisenstein/theta input.
* Products of L-functions: Σ_t over levels has no Euler product in t (the levels are additive data tn + 1), so "coefficient of
  an L-function product at one integer" never arises; the only multiplicative object is each τ_χ(tn + 1) separately.

## Barrier screen
B2 (moving integers), (J)39/(J)48 (size: no modular object), T1 (O269 Cor K1: E_t + O_t = 0 at squares, so any positivity
statement must use O_t with sign), Thm 9.1 (no fixed-level Eisenstein identity certifies Type I/II counts). Numerator: for k/n the
same packaging with k | t; positivity inputs cannot distinguish 4 from 8.

## Cheap numerics
None beyond `scripts/s9_level_bm.py` (the χ_{−t} layer is already positive at every non-square, so positivity theorems for it are moot).

## Assessment
Negative (Assessment, with the PROVED inequality of Prop 2.1): there is no fixed-integer packaging, and the explicit positive
coefficients available (representation numbers) enter with the wrong sign. Closes (ii)'s "Dirichlet coefficient positivity" hope.
