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

### Lemma 1.3 (e-slice criterion over F_q[t]; PROVED). char ≥ 5, A monic of degree k ≥ 1.
ES_q(A, P) holds iff there are a monic X of degree n − k and monic a, b | PX with
`E := AX − P` dividing a + b and lc(a + b) = lc(E).
(Note lc(a+b) = 1 if deg a ≠ deg b and = 2 if deg a = deg b, so lc(E) ∈ {1, 2} is necessary.)

*Proof.* By Lemma 1.1 the dominant denominator X has degree n − k, and `A/P − 1/X = E/(PX)`.
(⇐) put κ = (a+b)/E (monic), Y = κPX/a, Z = κPX/b; then 1/Y + 1/Z = (a+b)/(κPX) = E/(PX).
(⇒) if 1/Y + 1/Z = E/N (N = PX), let g = gcd(Y,Z) monic, Y = gy, Z = gz; then N(y+z) = Egyz and
gcd(yz, y+z) = 1 give yz | N; with L = N/(yz), a := Ly, b := Lz divide N and a + b = Eg, lc(g) = 1. ∎

## 2. The large-q regime: the analogue is FALSE for most P

### Theorem 2.1 (PROVED, elementary). char F_q ≥ 5, A monic of degree k ≥ 1, n > k. Then
`#{P monic of degree n : ES_q(A, P)} ≤ 2·D(2n)³·q^{n−k} ≤ 2·64^n·q^{n−k}`,
where D(m) ≤ 2^m bounds the number of monic divisors of a polynomial of degree ≤ m. Since there are
≥ (q^n − 2q^{n/2})/n irreducibles of degree n, **for fixed n and k the proportion of irreducible P of
degree n with ES_q(A, P) tends to 0 as q → ∞.**

*Proof.* Count triples (X, a, b) of Lemma 1.3; each determines P = AX − E once E is determined.
Case 1 (P ∤ a, P ∤ b, so a, b | X; the case P | a, P | b reduces to it since E is coprime to P):
E = (a+b)/κ with κ a monic divisor of a + b and lc(E) = lc(a+b). At most q^{n−k} choices of X,
D² of (a,b), D of κ. Case 2 (a = Pa₁, a₁ | X, b | X): P ≡ AX (mod E), so E | AXa₁ + b, a nonzero
polynomial of degree ≤ 2n, and lc(E) = lc(a + b) = 1; at most q^{n−k}·D²·D(2n) choices. ∎

*Meaning.* The fixed-P solution set is the F_q-point set of a variety in the coefficients whose
expected dimension is −k (unknowns α+β+γ+δ = n−k+γ, equations n+γ in the Type II chart
`A·abcd = a + b + Pc`). Lang–Weil therefore has nothing positive-dimensional to count at fixed P,
and the q → ∞ limit (Katz / Bary-Soroker-type equidistribution of factorisation types) is precisely
the regime where the analogue **fails**. The true analogue of "p → ∞" is q fixed, n → ∞, where the
expected number of solutions is ≍ poly(n)·q^{−k} — the analogue of log³p (B2's lottery), not a
positive-dimensional family. Consequence: any correct ES_q(A) has threshold n₀(q,k) ≥ c·k·log q.
