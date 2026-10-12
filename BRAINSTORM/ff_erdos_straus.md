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

## 3. Experiments (scripts/bs_ff_es.py, bs_ff_check.py, bs_ff_squares.py)

Decision procedure = Lemma 1.3 (complete); cross-checked against an independent brute force over
(X, Y) with Z solved from the equation (q = 5, 7; n = 2, 3; all agree, all witnesses verified by
`A·XYZ = P(XY+YZ+ZX)`).

**3.1 A = t, fraction of irreducible P of degree n failing ES_q(t, P)** (EVIDENCE):

| q \ n | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| 5 | 2/10 | 2/40 | 1/150 | 0/624 | 0/2580 |
| 7 | 6/21 | 21/112 | 25/588 | | |
| 11 | 31/55 | 114/440 | | | |
| 13 | 51/78 | 231/728 | | | |
| 17 | 102/136 | 693/1632 | | | |
| 19 | 127/171 | 1075/2280 | | | |

Both regimes are visible: failures grow with q at fixed n (Theorem 2.1) and disappear with n at
fixed q (the honest analogue of ES). Last failure for q = 5: P = t⁴ + t² + 2t + 2.

**3.2 Odd-square test (B5/T1 analogue).** For P = M² (M monic irreducible, A = t) *every* M with
deg M ≥ 2 tested has both Type I and Type II solutions (Type I/II = P divides exactly one/two
denominators): q = 5, deg M = 2: 10/10 have Type II; q = 7, deg M = 2: 15/21; deg M = 3: 97/112
(q = 7 ≡ 3 mod 4 included). **The odd-square obstruction (ET Prop 1.6) has no analogue here.**

*Reason (PROVED sketch, via the Type II chart `A·abd = P + e, a + b = ce`, f := A·acd − 1,
ef = P + A·a²d).* At P = M², M² ≡ −A·a²d (mod f) forces (−Ad / f) = 1. In Z the contradiction comes
from f ≡ −1 (mod 4d), f > 0, which fixes (−1/f) = −1 through the residue of f mod 4. In F_q[t]
reciprocity for monic f, g reads (g/f)(f/g) = (−1)^{((q−1)/2)·deg f·deg g}, and (−1/f) =
(−1)^{((q−1)/2)·deg f}: the "sign at infinity" is carried by **degree parity**, which no congruence
f ≡ −1 (mod Ad) controls. One finds (−Ad/f) = (−1)^{((q−1)/2)((1+deg f)(1+deg Ad)−1)}: never an
obstruction for q ≡ 1 (mod 4); for q ≡ 3 (mod 4) only the sub-family deg f odd or deg(Ad) odd is
obstructed. The analogue of "4" in the obstruction is the infinite place, not the numerator A.

## 4. Covering (Theorem C analogue): does the missing T1 obstruction allow a covering proof?

Since squares are not obstructed in F_q[t], Theorem C's argument (a family covering a square class
would solve ES at m², contradiction) does not transfer. Question: can finitely many congruence
families prove ES_q(A) for all P of large degree (a genuine function-field theorem)? Answer: no —
a different, *size* obstruction survives.

**Proposition 4.1 (PROVED, elementary; char ≥ 5, A monic, deg A = k ≥ 1).** Call a family *linear*
if E is fixed and each of a, b is one of a₀, P·a₀, X/a₀, PX/a₀ with a₀ fixed (X = (P+E)/A); these
are exactly the e-slice data that are polynomial of degree ≤ 1 in P (E = AX − P has degree < n,
so it cannot depend on P linearly). The validity set of a linear family is a union of congruence
classes mod W_F = A·lcm(a₀,b₀)·E. No linear family is valid on the class P ≡ 1 (mod W_F).

*Proof.* Validity needs A·lcm(a₀,b₀) | P + E, so E ≡ −1 (mod A·lcm(a₀,b₀)), whence E = −1 or
deg E ≥ k + deg lcm(a₀,b₀). E = −1 is excluded since lc(E) ∈ {1,2}. Mod E, a and b are
u·P^i with i ∈ {0,1,2} and u ∈ {a₀, A⁻¹a₀⁻¹} (using X ≡ A⁻¹P mod E); at P ≡ 1 (mod E) the condition
E | a + b becomes E | u_a + u_b, i.e. E divides one of a₀+b₀, 1 + A·a₀b₀ (up to the fixed unit
factor A⁻¹a₀⁻¹ resp. A⁻¹b₀⁻¹), or A⁻¹(a₀⁻¹+b₀⁻¹) — i.e. a₀+b₀ again. deg(a₀+b₀) ≤ deg lcm < deg E kills
the first and third. For E | 1 + A·a₀b₀ =: E·E′: reducing mod A·lcm(a₀,b₀) gives E′ ≡ −1 as well,
so deg E + deg E′ ≥ 2k + 2·deg lcm(a₀,b₀) > k + deg a₀ + deg b₀ unless E′ is a unit; E′ = −1 makes
lc(E) = −1. ∎

This is word for word the Z argument for n ≡ 1 (mod 4·lcm): e ≡ −1 forces e > a + b. **So the
covering core "P ≡ 1 modulo everything" survives in F_q[t] by positivity/size alone, independently
of the quadratic (odd-square) obstruction.** Script `bs_ff_cover.py` (fixed-data families only,
W = t·∏ linear primes): q = 5 covers 809/1024 unit classes, q = 7 covers 201155/279936; the
uncovered set contains the class 1 and is *not* the square classes (EVIDENCE that the quadratic
pattern of Mordell's 840-table has no analogue; fixed-data families are too weak to say more).

## 5. Barrier screen

* **B1** (coverings/identities): §4 — the class P ≡ 1 is uncoverable in F_q[t] too (size argument).
  So no finite-covering proof of ES_q(A) exists; the function-field world does not escape B1.
* **B2** (divisor lottery): Lemma 1.3 is literally the e-slice form; for fixed q the expected number
  of solutions is ≍ poly(n)·q^{−k} (analogue of log³p). Weil/RH for curves supplies unconditional
  GRH for all characters mod E, but GRH-type input is already known not to suffice (CONDITIONAL_ES,
  (I)2) — function fields only make that hypothesis a theorem, they do not change the reduction.
* **B3** (scale): the q → ∞ regime is the only place where function-field methods (Lang–Weil,
  Katz equidistribution, Bary-Soroker) give pointwise statements at a fixed P; there the solution
  variety at fixed P has expected dimension −k and Theorem 2.1 shows the analogue is *false* for
  most P. Main term q^{−k}·poly(n) → 0: the scale constraint in its sharpest form.
* **B5/T1**: absent in F_q[t] (§3.2) — the reason is that quadratic reciprocity's infinite-place twist
  is degree parity, not a residue mod the numerator. Consequence for transfer: any proof of ES_q(A)
  that uses Type I/II solutions at squares cannot transfer to Z, because at odd squares the Z
  statement is false; so the function-field analogue is the *wrong* model for the T1 step.
* **B6/T7**: the q → ∞ statements are averages over P (factorisation-type equidistribution);
  at a single P they give nothing (and Theorem 2.1 says the pointwise statement is false there).
* **B4** (pigeonhole): no new input; the same small-prime-factor covering issue applies to X.

## 6. Viability Assessment: **PARTIAL** (no route to ES; sharp structural by-products)

Collapses to B2/B3 at the step "pointwise count at fixed P": the only regime with pointwise
function-field technology (q → ∞) is where the analogue is false (Thm 2.1).
By-products: Prop 1.2 (unit numerators degenerate: 4/P with monic denominators is impossible in
char ≥ 5 — "4 > 3" is archimedean), Lemma 1.3, **Theorem 2.1** (PROVED: ES_q(A,P) fails for a
proportion → 1 of P as q → ∞, n fixed), Prop 4.1 (PROVED: the class P ≡ 1 obstructs coverings by
size alone), and the T1-absence (EVIDENCE + PROVED reciprocity computation, modulo the transfer of
ET's Type II chart to F_q[t], which is gcd algebra but was not re-verified line by line).
Next step if anyone pursues it: decide whether ES_q(t) holds for *all* n ≥ 5 at q = 5 (data: 0
failures at n = 5, 6) — a function-field ES "theorem" would still need the lottery solved.
