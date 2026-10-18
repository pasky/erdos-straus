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
Hence a structured family of (★)-failures at non-squares cannot be explained by the BL character χ_{−t} at all levels: at the
witness level χ_{−t} is satisfied by some prime factor. (Self-review repair: it does NOT follow that the failure is invisible to
all quadratic characters. The other real characters mod t — the genus characters of O260's M_gen — can still exclude the class −1.
Example: the (★)-failure n = 7 at t = 12: 85 = 5·17 with χ_{−12} = −1 for both factors but χ_{−4} = +1 for both, excluding 11 mod 12.)
So the statement is the level form of BL Thm 1.8 for the one Brauer character, and a disproof family must defeat the remaining
genus characters and/or higher-order characters at every level.

## Barrier screen
Disproof side: rules out failure families explained by the BL character χ_{−t} alone; leaves genus-character (other real
characters mod t) and higher-order-character conspiracies. T1: squares are exactly the quadratically obstructed set. Numerator check: for
8/n the same statement holds with 8 | t, yet 131, 241 fail — so numerator-8 failures are class-layer events too (consistent).

## Cheap numerics
`scripts/s9_level_bm.py` (0 witness failures among 99 776 non-squares; squares fully obstructed).

## Assessment
PROVED (elementary) no-go for disproof families explained by the single BL character χ_{−t} in level coordinates; complements BL Thm 1.8 (which
is the rational-point/BM statement). Spark: test whether the remaining genus characters (and cubic characters, 3 | φ(t)) can be simultaneously biased for a
structured family. No route to ES.
