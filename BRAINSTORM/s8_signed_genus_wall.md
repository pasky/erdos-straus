# s8_signed_genus_wall — positivity is the genus wall; no |d|-preserving signed→positive move (O258; §4)

**Idea.** Mandatory (iv): signed Type I slices d = −w² split, (p − 2cw)(p + 2cw). Is there a Vieta or reflection move from a
split signed point to a positive point?
**Literature.** JOINT_BUDGET Remark 1.2; (J)52 three-bit law (χ·s_∞ = −1); ET Prop 1.6; (J)5 Prop 10.3 (χ-shadow).
**Barrier screen.** Lemma 4.1 (PROVED): d > 0 ⟹ (d/p) = −1, while d < 0 ⟹ (|d|/p) = +1. A move keeping |d| (or its square class)
cannot cross. The Type I equations are linear in each variable, so there is no Vieta involution. Signed points exist at odd
squares (T1 side); positive ones never do.
**Cheap numerics.** `s8_genus_checks.py`: 1934 positive and 2816 signed points (p < 3000); the only exceptions are 9 degenerate
p | d cases. Odd squares 9 … 441 have 2–13 signed points and 0 positive ones.
**Assessment.** PROVED obstruction (classical in substance); spark 2 of O254 closed negatively.
