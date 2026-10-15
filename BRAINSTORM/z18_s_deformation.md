# z18_s_deformation — polynomial-in-s coefficients decouple integrality from positivity (O245)

## Idea
Allow parameters P(s, 2^{s/D}), P ∈ ℚ[s, Y]. Near μ = 0, s → 0 in Ẑ, so integrality depends only on P(0, 1), P(0, 0)
(Lemma 2.1), while positivity is decided as s → ∞. This would evade every positivity-based obstruction (Lemma 2.3,
Thm 4.1, O239's magnitude bound which needs positive relation terms).
Rung 2 stays closed (R-O245 reviewer argument, PROVED for Type II): slice-wise Thm 4.1 gives f mod n = F(s),
(4bcd − 1) mod n = G(s) in ℚ[s] with F·G = 1, so both are constants and the fixed-character contradiction survives.
## Literature
None found; closest: Sierpiński-type coverings with exponential parameters (EXPONENT_COVERING §0).
## Barrier screen
Theorem A's proof does not obviously transfer (the bad set S(s) depends on s). Polynomiality in s is the catch: windows need
m(s) | a + b coefficientwise in Y (impossible for SG pieces), the SG Type II needs ac constant in s (freezes t).
## Cheap numerics
None (algebraic argument, MENU_LADDER §8).
## Assessment
Assessment: closed for windows and SG; open in general (does a shape variety contain a polynomial curve from an integral
non-positive point into the positive region?). Spark.
