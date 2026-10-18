# POWER_LADDER_ES — the k-th power relaxation ladder ES_(k) (task O276; relay of O274 SHARP 1 / spark 1)

**ES is not solved; nothing below proves ES or an infinite case of ES.** Everything below is about relaxations.

## 0. Iteration log
* v0 (brief's question): is the cube rung ES_{Q³} (4/p = 1/x + 1/y + Q³/z, Q free) provable pointwise by a cubic
  analogue of ES^□'s one-Dirichlet-prime argument (cubic residue symbol, r ≡ 1 (3))?
* v1 (making the definition exact, §1): "Q³/z with z unrestricted" is vacuous (any numerator divides a cube), so the
  third term must be in lowest terms: the denominator of z is a k-th power. This is the parity normalisation of
  UNIT_ORBIT_ES §1 with 2 replaced by k.
* v2 (construction-first, §2): no cubic reciprocity is needed — the rung collapses. For odd k, ES_(k) is a FINITE
  CONGRUENCE COVERING (mod 4): 4/n = 1/(2x) + 1/(2x) + Q^k/(nx), 4x = n + Q^k, Q ≡ −n (mod 4). T1 dies (odd squares
  and cubes are solved with Type I shape). For even k the rung is ES^□ again (one Dirichlet prime, T1 intact).
* v3: the O274 §3.2 index calibration ("only k = 2 is provable; k ≥ 3 needs equidistribution") is therefore wrong in
  its conclusion; the correct calibration is the index of k-th powers in (ℤ/4)^× (and (ℤ/3)^×), §3.

## 1. Definitions (exact)

**Definition 1.1.** For k ≥ 1 and n ≥ 2 let
`ES_(k)(n):  4/n = 1/x + 1/y + 1/z,  x, y ∈ ℤ_{>0},  z ∈ ℚ_{>0},  den(z) = Q^k with Q odd, gcd(Q, n) = 1.`
Equivalently 4/n = 1/x + 1/y + Q^k/Z with x, y, Z ∈ ℤ_{>0}, **gcd(Q, Z) = 1**, Q odd, gcd(Q, n) = 1; equivalently
v_q(z) ∈ kℤ for every prime q with v_q(z) < 0, and such q are odd and prime to n.
* ES_(1) = "third denominator any odd integer prime to n"; ES_(2) = ES^□ of (J)28 (SYNTHESIS_SPARKS2 §2);
  ES = the per-solution intersection (Q = 1).
* Monotonicity: ES ⊂ ES_(k) ⊂ ES_(j) whenever j | k. The ladder is the divisibility lattice, not a chain:
  ES_(2) and ES_(3) are incomparable, both contain ES_(6).

**Remark 1.2 (why "lowest terms" is forced).** Without gcd(Q, Z) = 1 the rung is independent of k: a positive
rational A/B (lowest terms) equals Q^k/Z for some Z ∈ ℤ iff A | Q^k, and A | rad(A)^k. So "4/n − 1/x − 1/y has
numerator dividing a k-th power" = "numerator odd and prime to n", the same for all k.

**Remark 1.3 (target-coset reading).** In the fixed-modulus-4 shot family (UNIT_ORBIT_ES Prop 2.1 with Q² → Q^k,
§2.2 below) the event is "n + 4Q^k has a divisor g ≡ 3 (mod 4)" with Q free; mod a prime g this asks
−n/4 ∈ (F_g^×)^k, a coset of the k-th powers of index gcd(k, g − 1). That index — not [ (ℤ/4U)^× : k-th powers ]
for a large pooled U — is what decides the rung (§3).
