# z23 — height √d: all ET parameters at once in ℚ(√−p, √d) (O251, spark)

## Idea
LATTICE_MEETING Thm 1.4: ES at slice g ⟺ some line k | h has height class Y_k with Y_k² ≡ d (mod g), d | k. The element
β = √d + 2k√−p of F_d = ℚ(√−p, √d) has relative norm N_{F_d/ℚ(√d)}(β) = d + 4k²p, so ES ⟺ for some d | k, g | d + 4k²p with g ≡ −1 (4k),
i.e. g is (the norm of) a divisor of β in F_d lying over ℚ(√d). Spark: treat all d simultaneously in the multiquadratic field
ℚ(√−p, √2, √3, √5, …) and ask whether a reciprocity law (Hilbert symbols in F_d) links the solvability for d and d′.
## Literature
ET Prop 2.6; Hilbert symbol product formula (Neukirch, ANT V.3); Rédei-type biquadratic symbols (Stevenhagen,
"Rédei reciprocity", 2018 survey) — not checked for applicability.
## Barrier screen
Each d is its own B2 event (divisor of 4k²p + d ≡ −1 mod 4k). Reciprocity relates *quadratic* symbols of
d, p, g — genus information, which Cor 1.5/Prop 10.3 show cannot decide divisor-class events. B5: at odd squares all
symbols are satisfiable yet Type II is empty. So a reciprocity link would at best correlate failures, not force success.
## Cheap numerics
`scripts/z23_rescue.py`: the 99 empty-d=1 primes are rescued at d = 2 except three (d = 3, 5, 5); that d = 2 rescues 96/99
suggests the d = 1 and d = 2 events are not strongly correlated at these p (not tested systematically). Note also
(z23_split) that non-square d need not be a square mod the slice: p = 3361's solutions all have non-split slices.
## Assessment
CONJECTURE-level spark, not pursued; B2/B5 make a forcing outcome unlikely (Assessment).
