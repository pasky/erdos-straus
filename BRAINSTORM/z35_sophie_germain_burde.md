# z35_sophie_germain_burde — square levels d = k², Burde's rational quartic reciprocity (O263 spark 4) (O265)

## Idea
At d = k², −4d = −4k² and −4 = (1 + i)⁴, so for ℓ | p + 4k², ℓ ≡ 1 (4): (p/ℓ)_4 = (k/ℓ). Burde turns this into
(ℓ/p)_4 = (k/ℓ)·((a c_ℓ − b e_ℓ)/ℓ) (ℓ = c_ℓ² + e_ℓ²). Does that give a p-side constraint forcing a witness ≡ −1 (mod 4k²)?

## Literature
Burde (1969); CLASS_FORCING Prop 5.1(c) (Sophie-Germain exception); (J)74/(J)80 (thin families using x⁴ + 4y⁴).

## Barrier screen
Every factor of the product formula involves the unknown ℓ (its quartic symbol mod p and its Gaussian angle relative to π), and
the class −1 mod k² beyond its quadratic shadow lies in G² — so no p-only constraint (MODP_RECIPROCITY Prop 4.1). χ-shadow.

## Cheap numerics
`scripts/z35_sg_levels.py 1000000 100 400`: both identities hold on 32 837 triples. Square levels hit more often (1.07 % vs
0.85–0.91 %), explained by Σ_c 1/φ(4cd − 1) (ratio 1.19 predicted, 1.22 observed): at d = k², witnesses 4j²k² − 1 =
(2jk − 1)(2jk + 1) factor algebraically. Quartic data of p do not modulate level hit rates (z35_nonabelian_inert_or_complete).

## Assessment
PROVED (law) + EVIDENCE. Spark 4 closes negatively; the Sophie-Germain effect at square levels is an algebraic factorisation of
the witness (B1-level), not of p.
