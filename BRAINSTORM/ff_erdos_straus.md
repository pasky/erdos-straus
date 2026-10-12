# BRAINSTORM: Erdős–Straus over F_q[t] (O140, angle a)

Status: in progress. Scripts: `scripts/bs_ff_*.py`.

## 1. Idea — finding the faithful analogue

Setting. q odd, R = F_q[t], P monic irreducible of degree n. "Positivity" at the infinite
place is modelled by the sign function sgn = leading coefficient (Hayes' sign-normalisation):
the positive cone is the set of **monic** polynomials. (Without a sign condition ES is trivial
already over Z — Bradford–Ionascu (arXiv:1405.4025, §1, eq. (2)) note `4/(4k+1) = 1/k − 1/(k(4k+1))`
— and over F_q[t] likewise; so a positivity condition is mandatory for a faithful analogue.)

**ES_q(A, P)**: there are monic X, Y, Z ∈ R with `A/P = 1/X + 1/Y + 1/Z`, where A is a fixed
monic polynomial of degree k (the analogue of the numerator 4), or a unit u (k = 0).

### Lemma 1.1 (dominant denominator; PROVED, elementary). Let char F_q ≥ 5 and A monic of degree k ≥ 0
(or A = u a unit, k = 0). In every monic solution exactly one denominator, say X, has the minimal
degree, and deg X = n − k; moreover lc(A) ∈ {1,2,3}·lc(P) is forced in the unit case.

*Proof.* Let d1 ≤ d2 ≤ d3 be the degrees. The coefficient of t^{−d1} in the Laurent expansion at ∞ of
`1/X+1/Y+1/Z` is the number (1, 2 or 3) of denominators of degree d1, which is nonzero in F_q when
char ≥ 5. So the sum has exact degree −d1 and leading coefficient 1, 2 or 3; comparing with
A/P (degree k − n, leading coefficient lc(A) = 1 for monic A) gives d1 = n − k and, for monic A,
exactly one denominator of degree d1. ∎

### Proposition 1.2 (the unit numerator degenerates; PROVED). char F_q ≥ 5, u ∈ F_q^*.
(i) If u ∈ {1, 2, 3} then ES_q(u, P) holds for every monic P:
`1/P = 1/(P+1) + 1/(P(P+1))` (all monic), split once more for u = 1; `2/P = 1/P + 1/(P+1) + 1/(P(P+1))`;
`3/P = 1/P+1/P+1/P`.
(ii) If u ∉ {1,2,3} (in particular **u = 4**) then ES_q(u, P) fails for every P (Lemma 1.1).

So "4/P" with monic denominators is *false for every P* in char ≥ 5 and trivial in char 3 (4 = 1).
The reason is exactly archimedean: in R, `4/n` forces denominators *smaller* than n
(x > n/4), and "4 > 3" is what makes the problem non-trivial; under the ultrametric |·|_∞ three
monic unit fractions can only produce leading coefficients 1, 2, 3 and never "overshoot".
The faithful analogue therefore needs a numerator A of positive degree k (denominators shrink by
q^k, the analogue of x ≍ n/4):

**Definition (faithful analogue).** ES_q(A): for monic A of degree k ≥ 1, every monic irreducible P
of large degree (P ∤ A) satisfies ES_q(A, P).
