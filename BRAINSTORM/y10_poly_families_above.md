# y10_poly_families_above — ET's polynomial-solvability theory in the variable m, for p = m² + k (O221)

## Idea
ET Prop 1.9 classifies residue classes n ≡ r (q) solvable by polynomials in n; its last case dies because
p² + 4c²d is irreducible over ℝ. For the quadratic family n = m² + k the quartic (m² + k)² + 4c²d *can* split over ℚ
(Aurifeuille/Sophie Germain; e.g. k = 1: (m² + 1)² + 8 = (m² + 2m + 3)(m² − 2m + 3)), so genuinely new families
exist (Type I with f = m² + 2m + 3, c = 1, d = 2 is valid for m ≡ 2 (mod 4): 4/37 = 1/22 + 1/16 + 1/6512 at m = 6).
Question: can polynomial families in m reach the locally-square m (where congruence families provably cannot)?

## Result (NEAR_SQUARE §1–2)
* Lemma 1.1/1.3 (PROVED): every Type I solution has witness (d/n) = −1, every Type II solution (f/n) = −1 (and (de/n) = −1 when gcd(n, 2ad) = 1; R-O221)
  (n ≡ 1 mod 4) — ET Prop 1.6's mechanism in bare form; checked on 1 561 solutions of primes < 800.
* Thm 2.2 (PROVED): for k > 0 every Type I/II polynomial family has a witness ≡ constant (mod m² + k), hence a fixed
  character of n, hence its class avoids Z_k^□ = {m ∈ Ẑ : m² + k ∈ (Ẑ^odd)²} (non-empty iff k ≡ 0, 1, 5 mod 8).
  Every escaping shape dies by the positive-definiteness of x² + ky² at a real point. The new quartic families exist
  but are non-escaping (they live where (−4d/n) = −1).

## Literature
ET (arXiv 1107.1010) §10 Prop 1.9 and Prop 1.6; Schinzel / Mordell (polynomial identities in n, cited there);
POINTWISE_BINARYFORM (J)3 (two-variable forms, all directions) — the one-variable quadratic family is outside its scope.

## Barrier screen
B1: this IS a B1 statement, extended from linear families in n to quadratic families in m: for k > 0, polynomial
families are no stronger than congruences at the locally-square m. T1: k = 0 is ET Prop 1.6. B5: the vanishing at
squares deforms to the vanishing of *escaping* families for k > 0. Nothing here says anything at a single p (B6).

## Cheap numerics
`scripts/ns_polyfam.py K 3`: escaping families with integral classes: 0 for k = 1, 16, 24; 80/161/263 algebraic candidates (76/97/111 with computed classes, verified) for
k = −8, −15, −24. `scripts/ns_witness_check.py 800`: 0 failures.

## Assessment
PROVED negative theorem with exact scope (Type I/II families with ET-parametrised polynomial coordinates; families
given only as (x, y, z) ∈ ℚ[m]³ reduce to this when infinitely many n(m) in the class are prime — Bunyakovsky).
The sign k > 0 vs k < 0 is the whole story: see y10_below_squares.
