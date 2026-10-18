# s9_disproof_class_layer — a structured ES failure family (Ghosh–Sarnak style) cannot come from any level's quadratic layer (O271, own; O268 spark 1)

## Idea
Markoff surfaces have infinitely many integral Hasse failures at the same (log)² main-term scale, many explained by reciprocity
(Ghosh–Sarnak; Loughran–Mitankin; Colliot-Thélène–Wei–Xu). O268 spark 1 asks for an ES analogue. In level coordinates every
reciprocity-type obstruction attached to a quadratic field ℚ(√−t) acts through χ_{−t}; Prop 2.2 of SYNTHESIS_SPARKS9 says the
χ_{−t}-layer is solvable at every non-square. Make the consequence precise.

## Literature
Ghosh–Sarnak, Invent. Math. 229 (2022); Loughran–Mitankin, *Integral Hasse principle and strong approximation for Markoff
surfaces*, IMRN (2021) (from memory; via O268/(J)100); Bright–Loughran Thm 1.8 (no BM obstruction to ES for n ≥ 2);
DISPROOF_AVENUES (J)97 ("prime T1" needed).

## Statement (PROVED, from SYNTHESIS_SPARKS9 Prop 2.1–2.2)
Call a set 𝒩 of odd integers *quadratically obstructed at level t* if for every n ∈ 𝒩 every prime factor of tn + 1 splits in
ℚ(√−t) (the only way the χ_{−t}-layer can vanish). If n is quadratically obstructed at every level 4 | t ≤ T, and T ≥ 4ℓ(n) where ℓ(n) is the least prime with
(n/ℓ) = −1 (ℓ(n) = ∞ for squares), then n is a perfect square — by Prop 2.2 a non-square has a witness level t ≤ 4ℓ(n) with an
inert prime factor. In particular a set obstructed at ALL levels consists of squares only.
Hence a structured family of ES (★)-failures at non-squares must be invisible to all χ_{−t}: at each level the prime factors of
tn + 1 include inert ones, and the failure is purely in the class position inside the coset {χ_{−t} = −1}. This is the level
form of BL Thm 1.8 and of (J)97's "prime T1 = global correlation of ≍ log³p divisor events".

## Barrier screen
Disproof side: rules out reciprocity-type (quadratic-character) structured failures; leaves only higher-order-character
conspiracies (cubic and higher characters mod t). T1: squares are exactly the quadratically obstructed set. Numerator check: for
8/n the same statement holds with 8 | t, yet 131, 241 fail — so numerator-8 failures are class-layer events too (consistent).

## Cheap numerics
`scripts/s9_level_bm.py` (0 witness failures among 99 776 non-squares; squares fully obstructed).

## Assessment
PROVED (elementary) no-go for quadratic/reciprocity-type disproof families in level coordinates; complements BL Thm 1.8 (which
is the rational-point/BM statement). Spark: test whether cubic characters mod t (t with 3 | φ(t)) can be simultaneously biased
for a structured family — the only remaining "algebraic" disproof shape. No route to ES.
