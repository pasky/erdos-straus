# z44_tes_ladder — the order-3 variant separates T1's order from the shot index (O276)

## Idea
Over ℤ, ord(T1) = 2 coincides with the unavoidable 2-part of the shot index gcd(k, g − 1) (g ≡ 3 (4)). Over ℤ[ω]
(TES, order-3 T1₃) the two separate: T1₃ ⟺ 3 | k, shot index even ⟺ 2 | k.

## Literature
SYNTHESIS_SPARKS2 §3 (Prop 3.1 shots, Lemma 3.2 cubic mute lemma, Thm 3.3 T1₃, Thm 3.5 TES^{□₃}); TWISTED_T1 §3.
Cubic reciprocity: Ireland–Rosen, *A Classical Introduction to Modern Number Theory*, Ch. 9.

## Barrier screen
TES_(2) has no T1₃ yet no finite covering by fixed shot primes (CRT on quadratic classes) — a counterexample, inside
shot families, to reading B5 as "no T1 ⟹ covering". Whether another identity family covers TES_(2) is OPEN.

## Cheap numerics
`scripts/z44_tes_ladder.py 3000` (fixed g = −8 + ω, N = 73; exact in O): k = 1 fires 412/412 primes and 412/412 cubes;
k = 2 fires 209/412 and 209/412; k = 3 fires 134/412 primes, 0/412 cubes (T1₃).

## Assessment
PROVED (bits, POWER_LADDER_ES §6) + EVIDENCE (table). Sharp calibration: ES's k-ladder is flat because 2 = ord(T1) =
2-part of every shot index; an order-d variant has a 2-dimensional ladder (k mod d, k mod 2).
