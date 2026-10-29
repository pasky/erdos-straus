# EXSET_FUNCTION_FIELD — the U exceptional set over F_q[T]: large q, fixed q, and what transfers (wave z51, lane 1c)

Status: in progress (z51 lane 1c, Opus). ES is OPEN; nothing here proves or disproves ES or any infinite case of it.
Labels as in DISCOVERIES.md (PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment).
Brief: `../z51briefs/1c_opus_ffield.md`; context `../z5{0,1}briefs/CONTEXT.md`. Scripts `scripts/z51_ffield_*`,
data `data/z51_ffield/`. Prior function-field work: FUNCTIONFIELD_ES*.md, FF_*.md, DRINFELD_ES.md (they study
ES_q(A, P) with a polynomial numerator A; this document studies the numerator-free U union and its exceptional set).

## 0. Summary

| # | Claim | Label | § |
|---|---|---|---|
| 1 | Normalisation: (placeholder) | | §1 |
| 2 | T1 over F_q[T]: (placeholder) | | §1 |
| 3 | Numerics / controls: (placeholder) | | §2 |
| 4 | Large q, fixed n: (placeholder) | | §3 |
| 5 | Fixed q, n → ∞: (placeholder) | | §4 |
| 6 | Transfer to ℤ: (placeholder) | | §5 |
| 7 | Reviews: (placeholder) | | §6 |

## 1. The analogue

### 1.1 Setting and the reciprocity facts used

q = p^r odd, R = F_q[T], χ the quadratic character of F_q^*, ε := χ(−1) = (−1)^{(q−1)/2}. "Positive" means monic
(Hayes' sign). For B monic and a ∈ R coprime to B, (a/B) is the Jacobi symbol (multiplicative in a and in B; for
B = P prime, (a/P) = a^{(|P|−1)/2} mod P, |P| = q^{deg P}). Standard facts (Rosen, *Number theory in function fields*,
Thm 3.3 and Prop 3.2–3.5):

* (R1) a, B monic coprime: (a/B)(B/a) = ε^{deg a · deg B}.
* (R2) c ∈ F_q^*: (c/B) = χ(c)^{deg B}.

So the quadratic-reciprocity defect of F_q[T] lives at the place ∞, and is measured by degree parities and leading
coefficients. Over ℤ it lives at 2 and ∞ (the "2-adic layer" of U: v ∈ 4ℤ ∪ (8ℤ − n)). This is the dictionary
entry the brief asks for: **the 2-adic layer of U becomes the ∞-adic layer of F_q[T]: degree parity (and, if one
allowed it, the square class of the leading coefficient).**

### 1.2 Words, shapes, and the definition of U_q

Let f be monic of degree n ≥ 2. A *word* of f is a triple (t, u, v) of monic polynomials with f = tuv − u − v. Its
*shape* is (s, a, b) = (deg t, deg u, deg v); f is monic of degree n iff s + a + b = n, s + b ≥ 1 and s + a ≥ 1
(the excluded shapes have t = v = 1 or t = u = 1 and give f = −1). The identities of the integer forest hold verbatim:

  f + v = u·A,  f + u = v·A′,  tf + 1 = A·A′,  where A := tv − 1, A′ := tu − 1.                       (1.1)

Conversely, if v is monic and A is a monic divisor of f + v of degree ≥ 1 with A ≡ −1 (mod v), then
t := (A + 1)/v and u := (f + v)/A are monic and (t, u, v) is a word; deg t = deg A − deg v.

**Lemma 1.1 (colour at ∞; PROVED).** Let v be monic, A monic of degree ≥ 1, A ≡ −1 (mod v). Then
(−v/A) = ε^{(deg A + 1)(deg v + 1) − 1}. In particular, for q ≡ 3 (mod 4): (−v/A) = −1 ⟺ deg A or deg v is odd ⟺
deg t or deg v is odd; for q ≡ 1 (mod 4): (−v/A) = +1 always.

*Proof.* gcd(A, v) = 1. By (R2), (−1/A) = ε^{deg A}; by (R1), (v/A) = ε^{deg A deg v}(A/v), and A ≡ −1 (mod v)
gives (A/v) = (−1/v) = ε^{deg v} (also for v = 1). Multiply: exponent deg A + deg A deg v + deg v. For the last
equivalence: deg A = deg t + deg v, and "deg A, deg v both even" ⟺ "deg t, deg v both even". ∎

**Definition 1.2 (U_q; the analogue of U).** Let q ≡ 3 (mod 4). A word (t, u, v) of f is a *U-witness* if
deg u ≥ 1 and (deg t or deg v is odd). U_q(f) holds if f has a U-witness. Equivalently: some monic v (necessarily
deg v < n) has a monic divisor A ≡ −1 (mod v) of f + v, 1 ≤ deg A < n, with deg A or deg v odd.
*Dictionary.* Over ℤ: n + v = u·A with A ≡ −1 (mod v), 1 < A < n + v (so u ≥ 2), and v ∈ 4ℤ ∪ (8ℤ − n) — the
endpoint classes at which the 2-adic data force (−v/A) = −1 (Theorem B / Theorem E of z48). Here the ∞-adic data
force it: "v ≡ 0 (mod 4)" ↦ "deg v odd" (forces the colour whatever A is), the second line ↦ "deg A odd".
W_U(f) := number of U-witnesses (ordered triples).

**Theorem 1.3 (T1 over F_q[T]; PROVED).** q ≡ 3 (mod 4). If f = g² with g monic, U_q(f) fails.

*Proof.* Let (t, u, v) be a U-witness, A = tv − 1. Then A | g² + v and gcd(A, v) = 1. For a prime P | A we have
P ∤ v, hence P ∤ g, and −v ≡ g² (mod P), so (−v/P) = 1. Therefore (−v/A) = 1, contradicting Lemma 1.1. ∎

So every forbidden configuration is a quadratic-non-residue event: a U-witness with divisor A forces (f/A) = −1,
exactly as over ℤ ("all forbidden classes are QNRs mod ℓ").

**Definition 1.4 (prime-modulus family).** For a monic prime A, F(A) := {−v mod A : v monic, v | A + 1,
(deg A or deg v odd)}, w(A) := |F(A)|. Every class in F(A) is a non-residue mod A (Lemma 1.1). If deg A < n and
f mod A ∈ F(A), then U_q(f) (the word (t, u, v) with t = (A+1)/v, u = (f+v)/A has deg u ≥ 1). Distinct v | A + 1
give distinct residues except v = 1 and v = A + 1 (both give −1, admissible iff deg A is odd), so
w(A) = τ(A+1) − 1 for deg A odd and w(A) = #{v | A+1 monic, deg v odd} for deg A even.
Large-q mass: as q → ∞, for each k ≤ a the average over primes A of degree a of the number of monic degree-k
divisors of A + 1 tends to 1, so the average of w(A) tends to a (a odd) resp. a/2 (a even), and Σ_{deg A = a} w(A)/q^a → 1 (a odd), 1/2 (a even), so
Σ_{deg A ≤ z} w(A)/|A| → (3/4) z + O(1): the analogue of Σ_{ℓ≤z} w(ℓ)/ℓ ~ C_V log z has C_V^{FF} = 3/4 per unit
of degree (Assessment for fixed q: the F_q[T] Titchmarsh divisor sum changes the constant, not the shape).

**Definition 1.5 (ES₅-analogue).** A word with gcd(u, v) = 1 is *bichromatic* if (uv/f) = −1; ES₅,q(f) holds if f
has a bichromatic word. **Lemma 1.6 (PROVED).** For a word of shape (s, a, b) with gcd(u, v) = 1,
(uv/f) = ε^{s(a+b) + ab}. *Proof.* gcd(u, f) = gcd(u, v) = 1 since f ≡ −v (mod u). By (R1),
(u/f) = ε^{an}(f/u) = ε^{an}(−v/u) = ε^{an + a}(v/u), similarly (v/f) = ε^{bn + b}(u/v), and (v/u)(u/v) = ε^{ab}.
The exponent (a + b)(n + 1) + ab with n = s + a + b is ≡ s(a + b) + ab (mod 2). ∎
Squares have no bichromatic word ((uv/g²) = 1). *Difference from ℤ.* Over ℤ, Theorem A makes "U-witness" a
sub-case of "bichromatic" (both symbols are −1 on certificate words). Over F_q[T] the two symbols (f/A) and (uv/f)
are different functions of the shape: e.g. shape (0, 2, 1) is a U-witness but (uv/f) = +1. Both unions are
T1-obstructed; they are no longer nested. This document studies U_q.

### 1.3 Why monic and q ≡ 3 (mod 4): the two degenerate normalisations

**Proposition 1.7 (PROVED).** (i) q ≡ 1 (mod 4), monic words: by Lemma 1.1 the colour is never forced, so the
analogue of U is empty and T1 has no content.
(ii) *Leading coefficients free.* Let q be odd and allow the shift v to be any nonzero polynomial (A still monic),
with the colour condition (−v/A) = −1 read off at ∞, i.e. χ(−lc v)^{deg A} ε^{deg v (deg A + 1)} = −1 (the same
computation as Lemma 1.1, now with (R2) for lc v). Call this U′_q. Squares still fail U′_q (same proof as Thm 1.3).
But if q > (n + 1)², every monic non-square f of degree n ≥ 2 satisfies U′_q. Hence the exceptional set of U′_q is
*exactly* the squares, for every n < √q − 1.

*Proof of (ii).* f is not a constant times a square (a monic f = c·h² forces c square). Weil:
|Σ_{y∈F_q} χ(f(y))| ≤ (n − 1)√q. With at most n zeros, #{y : χ(f(y)) = −1} ≥ (q − n − (n−1)√q)/2 > 0 for
q > (n+1)². Take such y, A := T − y, v := −f(y) ∈ F_q^*. Then A | f + v, A ≡ −1 (mod v) (v is a unit),
deg((f+v)/A) = n − 1 ≥ 1, and the colour is χ(−lc v)^1 = χ(f(y)) = −1. ∎

*Reading.* The q − 1 unit shifts carry free quadratic-character data at ∞ ("Frobenius firing", FF_MUTE §§5, 7), and
one Weil sum turns them into a witness. Over ℤ the unit group is {±1} and positivity leaves no unit shift, so U′ has no
integer analogue; a result proved through U′ says nothing about ℤ. With monic shifts (positivity), there is a
single unit shift v = 1, and the mass per shape becomes q-independent (§3.1). **We therefore fix: q ≡ 3 (mod 4), all
of t, u, v, A monic** — the only normalisation among these with a nonempty colour layer, T1, and an integer-like
mass. (Assessment: this restores the T1 obstruction that BRAINSTORM/ff_erdos_straus.md §5 found absent for
ES_q(A, P) with a polynomial numerator; there the 2-adic layer was mapped to a finite place.)

## 2. Numerics and controls

Engine `scripts/z51_ffield_enum.c` (C; p prime \u2261 3 mod 4): enumerates, for every shape, all q^n monic triples
(t, u, v), forms f = tuv \u2212 u \u2212 v, and counts W_U(f) for all q^n monic f of degree n (optionally the ES\u2085-analogue,
with a gcd test). It also enumerates all squares. Raw output `data/z51_ffield/enum.txt`, `es5_q3.txt`; the failing
non-squares at q = 3 are listed in `data/z51_ffield/fail_q3_n*.txt`.

**Controls (CERTIFIED for the listed (q, n)).**
* T1: every square fails U_q in every run (sqfailU = #squares, e.g. 2187/2187 at (3, 14), 6859/6859 at (19, 6)).
* Mass identity: the mean of W_U is exactly the number of U-shapes in every run (\u00a73.1, Prop 3.1 below).
* Numerator-8 / hard-prime / R-zero controls: not applicable (no integer n is an input here); the transfer
  question for them is addressed in \u00a75.

**Table 2.1 (CERTIFIED). Non-square exceptional set of U_q, # and fraction of all q^n monic f of degree n.**

| q \\ n | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 0 | 5 | 6 | 6 | 21 | 3 | 21 | **0** | 12 | **0** | 7 | **0** | 3 | **0** |
| 7 | .286 | .184 | .0787 | .0179 | .0098 | 6.5e\u22124 | 5.4e\u22124 | | | | | | | |
| 11 | | .174 | .0751 | .0119 | .0062 | 2.6e\u22124 | | | | | | | | |
| 19 | | .175 | .0776 | .0103 | .0044 | | | | | | | | | |
| 31 | | .181 | .0778 | .0101 | | | | | | | | | | |
| 59 | | .195 | .0805 | | | | | | | | | | | |
| 191 | | .2007 | | | | | | | | | | | | |

(q = 3 row: counts; other rows: fractions. Number of U-shapes m(n) = 2, 3, 7, 9, 15, 18, 26, 30, 40, 45, 57, 63, 77,
84 for n = 2..15; m(n) = 3n\u00b2/8 + O(n).)

Two regimes are visible, and they behave oppositely.

1. **Fixed n, q \u2192 \u221e: the exceptional fraction converges to a positive constant.** n = 3: 0.1745 (q = 19), 0.1911
   (43), 0.2006 (179), 0.2007 (191); the limit is 29/144 = 0.20139 (\u00a73.3). n = 5: 0.0103, 0.0104, 0.0101 at
   q = 19, 23, 31. The fixed-n large-q exceptional set is a *positive proportion* of all f, not O(q^{n\u2212c}).
2. **Fixed q = 3, n \u2192 \u221e: the non-square exceptional set dies out**, exactly as over \u2124 (where U fails only at the odd
   squares and six integers \u2264 978145 up to 10\u2079): 0 non-square failures at n = 9, 11, 13, 15 (out of 3^n), and
   12, 7, 3 at n = 10, 12, 14, against 243, 729, 2187 squares. The failing non-squares are not \u221e-adically close to
   squares: the polynomial part g of \u221af has deg(f \u2212 g\u00b2) = n/2 \u2212 1 or n/2 \u2212 2 for all of them (n = 6..14).

ES\u2085-analogue (q = 3, n = 5..12): non-square failures 114, 75, 660, 321, 3872, 1368, 21903, 5974 \u2014 far more than U_q
at odd n, where only \u2248 n\u00b2/8 shapes are bichromatic; squares fail in all runs. Not pursued further.

The point of the two regimes: the large-q limit keeps the *mass* fixed (m(n) \u2248 3n\u00b2/8 expected witnesses, independent of
q, \u00a73.1), so it cannot be a depth breaker in the sense of the brief; the fixed-q limit grows the mass like n\u00b2 =
(log_q N)\u00b2, as over \u2124 (log\u00b2 N), and there the exceptional set behaves like the integer one.

## 3. Large q, fixed n

Notation: M_d = monic polynomials of degree d (an affine space A^d over F_q via the non-leading coefficients);
\u03a3_n = set of U-shapes (s, a, b): s + a + b = n, a \u2265 1, s + b \u2265 1, (s or b odd); m(n) := |\u03a3_n|;
for a shape \u03c3 = (s, a, b) the *word map* \u03c6_\u03c3 : M_s \u00d7 M_a \u00d7 M_b \u2192 M_n, (t, u, v) \u21a6 tuv \u2212 u \u2212 v;
W_\u03c3(f) := #\u03c6_\u03c3^{\u22121}(f)(F_q), so W_U = \u03a3_{\u03c3 \u2208 \u03a3_n} W_\u03c3; \u03b4_q(n) := #{f \u2208 M_n(F_q) : W_U(f) = 0}/q^n.

### 3.1 The mass is a shape count, independent of q

**Proposition 3.1 (PROVED).** For every q \u2261 3 (mod 4) and n \u2265 2, q^{\u2212n} \u03a3_f W_U(f) = m(n) exactly, and
m(n) = 3n\u00b2/8 + O(n) (m(n) = 2, 3, 7, 9, 15, 18, 26, 30, 40, 45 for n = 2..11).

*Proof.* The domain of \u03c6_\u03c3 has q^s q^a q^b = q^n points and every point maps into M_n, so \u03a3_f W_\u03c3(f) = q^n. Counting
shapes: among pairs (s, b) with s + b \u2264 n \u2212 1, (s, b) \u2260 (0, 0), a fraction 3/4 + O(1/n) has s or b odd. \u220e

This is the exact analogue of "mass \u224d log\u00b2 N" for U over \u2124, with log N replaced by n = log_q N. It does not grow
with q. The large-q limit is therefore a *fixed-mass* limit.

### 3.2 The word maps are finite, flat, generically \u00e9tale, of degree n!/(s!a!b!)

**Lemma 3.2 (PROVED; any characteristic).** For every shape (s, a, b) with s + a + b = n, s + b \u2265 1, s + a \u2265 1,
\u03c6_\u03c3 : A^n \u2192 A^n is finite and flat of degree D_\u03c3 = n!/(s! a! b!), and generically \u00e9tale.

*Proof.* Give the coefficient of T^{d\u2212i} of a monic polynomial of degree d the weight i. The coefficient y_i of T^{n\u2212i}
of tuv is weighted-homogeneous of weight i in the coefficients x of (t, u, v); the coefficient of T^{n\u2212i} in u + v has
weight \u2264 i \u2212 min(s + b, s + a) < i (the leading 1 of u sits at weight n \u2212 a = s + b \u2265 1). So \u03c6_\u03c3 = h + l with
h(t, u, v) = tuv weighted-homogeneous and l of lower weight in each component. The common zero set of h is {0}
(tuv = T^n forces t = T^s, u = T^a, v = T^b by unique factorisation). Hence h is a homogeneous system of parameters,
k[x] is free over k[h] of rank \u220f_i i / \u220f_j wt(x_j) = n!/(s!a!b!) (Hilbert series), and by the weight filtration
(gr k[\u03c6] = k[h]) a homogeneous k[h]-basis of k[x] lifts to a k[\u03c6]-basis: \u03c6 is finite and flat of degree D_\u03c3. The
Jacobian determinant of \u03c6 has top-weight part the Jacobian of h, and h is \u00e9tale at any (t, u, v) with t, u, v
pairwise coprime (if \u03b4t\u00b7uv + t\u00b7\u03b4u\u00b7v + tu\u00b7\u03b4v = 0 with deg \u03b4t < s etc., reduce mod t, u, v: \u03b4t = \u03b4u = \u03b4v = 0).
So the Jacobian of \u03c6 is not identically zero and \u03c6 is generically \u00e9tale (separable) in every characteristic. \u220e

So the generic fibre X_\u03c3 of \u03c6_\u03c3 is a set of D_\u03c3 geometric points. Let L_n be the compositum of the function fields
of all word maps of degree n (all non-degenerate shapes, U or not) over K = F_q(y_1, \u2026, y_n), \u03a9_n its Galois
closure, G_n = Gal(\u03a9_n/K) and G_n^geo = Gal(\u03a9_n F\u0304_q / F\u0304_q(y)). G_n acts on \u2294_\u03c3 X_\u03c3. Let B_n \u2282 A^n be the union
of the branch loci (a proper closed subset of degree bounded in terms of n). For f \u2208 (A^n \u2216 B_n)(F_q), W_\u03c3(f) is the
number of fixed points of Frob_f on X_\u03c3 (\u03c6_\u03c3 is finite \u00e9tale over f and its source is normal).

### 3.3 The large-q limit exists and is a Chebotarev statistic

**Theorem 3.3 (PROVED, given the Chebotarev density theorem for finite \u00e9tale Galois covers of open subsets of
A^n_{F_q}, with error O(q^{n\u22121/2}) and implied constant depending only on the complexity of the cover \u2014 Lang\u2013Weil;
e.g. Fried\u2013Jarden, *Field Arithmetic*, Prop. 6.4.8 and \u00a76.4; Serre, *Lectures on N_X(p)*, \u00a79).** Let
Der_n := {g \u2208 G_n : g has no fixed point on X_\u03c3 for every \u03c3 \u2208 \u03a3_n}. Then

  \u03b4_q(n) = |Der_n \u2229 Frob_q G_n^geo| / |G_n^geo| + O_n(q^{\u22121/2}),

with the O_n-constant independent of q. By Lemma 3.4 below, G_n = G_n^geo, so the main term is |Der_n|/|G_n|.

*Proof.* Chebotarev applied to \u03a9_n over A^n \u2216 B_n, summed over the conjugacy classes contained in Der_n; the points of
B_n(F_q) number O_n(q^{n\u22121}). The complexity of \u03a9_n (degree \u2264 \u220f D_\u03c3!, equations of degree bounded in n with integer
coefficients) is bounded in terms of n only. \u220e

G_n may depend on p = char F_q (for p \u2264 some p\u2080(n)); for p > p\u2080(n) it equals the characteristic-0 monodromy group.

### 3.4 The boundary of the word maps: a copy of S_n, and no constant field extension

**Lemma 3.4 (PROVED; any odd q).** G_n = G_n^geo, and G_n contains a subgroup S \u2245 S_n acting on each X_\u03c3
(\u03c3 = (s, a, b)) as S_n acts on ordered set partitions of {1, \u2026, n} into blocks of sizes s, a, b.

*Proof.* (Degeneration to the top-weight map.) For c \u2208 F_q(\u03bc)^*, c = 1/\u03bc, let S_c act on monic polynomials of degree
d by (S_c g)(T) = c^d g(T/c), and S_c^{(n)} on polynomials of degree \u2264 n by g \u21a6 c^n g(T/c). Then
\u03c6_\u03c3(S_c t, S_c u, S_c v) = S_c^{(n)}(\u03c6^\u03bc_\u03c3(t, u, v)) with \u03c6^\u03bc_\u03c3(t, u, v) := tuv \u2212 \u03bc^{s+b} u \u2212 \u03bc^{s+a} v.
So over F_q(\u03bc, y) the cover {\u03c6^\u03bc_\u03c3 = y} is the base change of {\u03c6_\u03c3 = y\u2032} along the purely transcendental extension
F_q(y\u2032) \u2282 F_q(y\u2032, \u03bc) = F_q(\u03bc, y), y\u2032 = S^{(n)}_{1/\u03bc} y; the Galois group of the compositum and its constant field are
unchanged. The family \u03a6_\u03c3 = {(\u03bc, w) \u21a6 (\u03bc, \u03c6^\u03bc_\u03c3(w))} is finite flat over A^1 \u00d7 A^n (the proof of Lemma 3.2 with
\u03bc of weight 0), and its fibre at \u03bc = 0 is the top map (t, u, v) \u21a6 tuv, which is \u00e9tale over {y : disc y \u2260 0}. So
the generic point \u03be of the divisor {\u03bc = 0} (residue field F_q(y)) is unramified in every K(X_\u03c3), hence in \u03a9_n. For a
place \ud835\udd13 | \u03be of \u03a9_n the decomposition group D_\ud835\udd13 \u2245 Gal(\u03ba(\ud835\udd13)/F_q(y)), and its action on X_\u03c3 is the Galois action on
the special fibre {tuv = y} = ordered (s, a, b)-partitions of the roots of y. \u03ba(\ud835\udd13) is generated by the residue
fields of these special fibres; the U-shape (0, n \u2212 1, 1) contributes F_q(y)(one root of y), so \u03ba(\ud835\udd13) is the
splitting field of the generic polynomial, with group S_n and constant field F_q. Hence D_\ud835\udd13 \u2245 S_n acts as stated.
Constants of \u03a9_n inject into \u03ba(\ud835\udd13), whose constant field is F_q; so \u03a9_n \u2229 F\u0304_q = F_q and G_n = G_n^geo. \u220e

### 3.5 The fixed-n target of the brief is false: a positive proportion of non-squares fail

**Theorem 3.5 (PROVED, given Chebotarev as in Thm 3.3).** For every n \u2265 2 there are c_n > 0 and C_n such that for
every odd q,

  #{f \u2208 M_n(F_q) : f has no word of any shape other than (n, 0, 0)} \u2265 c_n q^n \u2212 C_n q^{n\u22121/2},

with c_n \u2265 1/\u220f_\u03c3 D_\u03c3! (product over all non-degenerate shapes). In particular, for q \u2261 3 (mod 4),
#{f non-square : U_q(f) fails} \u2265 c_n q^n \u2212 C_n q^{n\u22121/2} \u2212 q^{n/2}: **for fixed n the non-square exceptional set
of U_q is a positive proportion of all f as q \u2192 \u221e, so no bound O(q^{n\u2212c}) (nor o(q^n)) holds.** The same holds for
the ES\u2085-analogue and for every union of word shapes.

*Proof.* Let g\u2080 \u2208 S \u2264 G_n be the element acting as an n-cycle on the roots (Lemma 3.4). An n-cycle fixes no ordered
set partition with at least two non-empty blocks, and every non-degenerate shape other than (n, 0, 0) has at least two
non-empty blocks. So g\u2080 is fixed-point-free on every such X_\u03c3. Its conjugacy class C has |C|/|G_n| \u2265 1/|G_n| \u2265
1/\u220f D_\u03c3!, and Chebotarev (G_n = G_n^geo, so every class occurs for every q) gives #{f \u2209 B_n : Frob_f \u2208 C} \u2265
(|C|/|G_n|)q^n \u2212 C_n q^{n\u22121/2}; such f have no rational point in any fibre. Squares number q^{n/2}. \u220e

*Reading.* The forest of a typical f is empty with probability bounded below in the large-q limit; the frozen
element is the boundary n-cycle ("f irreducible at the cusp"). Nothing like this happens over \u2124, where the mass
log\u00b2 N grows. The brief's Goal 1 ("O(q^{n\u2212c}) at fixed n") is false for U_q; in the lc-free normalisation U\u2032_q it
is true for a trivial reason (Prop 1.7(ii)). Neither is a depth statement.

### 3.6 The q = \u221e model: the limit densities match independent Poisson shapes

**n = 3 (EVIDENCE + computation).** U-shapes: (0, 2, 1), (1, 2, 0) (both: "f + 1 has a root") and (1, 1, 1). For
(1, 1, 1), t = T \u2212 x, u = T \u2212 \u03b1, v = T \u2212 \u03b2: matching coefficients gives
x\u00b3 + c\u2082x\u00b2 + (c\u2081 + 3)x + c\u2080 + c\u2082 = 0, i.e. f(x) + 3x + c\u2082 = 0, and then \u03b1, \u03b2 are the roots of
Z\u00b2 + (c\u2082 + x)Z + c\u2081 + 2 + x(c\u2082 + x), discriminant \u0394(x) = \u22123x\u00b2 \u2212 2c\u2082x + c\u2082\u00b2 \u2212 4c\u2081 \u2212 8. So W_{(1,1,1)}(f) =
\u03a3_{x: f(x)+3x+c\u2082=0} (1 + \u03c7(\u0394(x))), the monodromy of (1,1,1) is inside C\u2082 \u2240 S\u2083 (order 48, derangement proportion
29/48), and if it is all of C\u2082 \u2240 S\u2083 and linearly disjoint from the S\u2083 of f + 1 (derangement proportion 1/3), then
\u03b4_\u221e(3) = 29/144 = 0.20139. Observed (Table 2.1): 0.2004, 0.2006, 0.2007, 0.2014 at q = 163, 179, 191, 167.

**General n (EVIDENCE).** Model: shapes with s = 0, a = 0 or b = 0 are governed by the factorisation of f + 1
(f + 1 = (u\u22121)(v\u22121), resp. u(t\u22121), resp. v(t\u22121)); U-failure forces f + 1 irreducible (n odd) resp. all irreducible
factors of f + 1 of even degree (n even), probabilities p_f(n) = 1/n resp. binom(n, n/2)/2^n. Genuine shapes
(s, a, b \u2265 1), grouped in u \u2194 v pairs, are treated as independent Poisson variables of mean 1 (a \u2260 b) or 1/2
(a = b); total mean M_g(n) = 0, .5, 1.5, 3, 4.5, 7.5, 9, 14, 15, 22.5 for n = 2..11, M_g(n) \u2248 n\u00b2/4 (n odd),
3n\u00b2/16 (n even). Prediction \u03b4_\u221e(n) \u2248 p_f(n) e^{\u2212M_g(n)}:

| n | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|
| model | 0.5 | 0.2022 | 0.0837 | 0.00996 | 0.00347 | 7.9e\u22125 |
| largest q run | 0.5 (exact) | 0.2007 (q=191) | 0.0805 (q=59, rising) | 0.0101 (q=31) | 0.0044 (q=19, falling) | 2.6e\u22124 (q=11, falling) |

**Conjecture 3.6 (big monodromy for word maps; CONJECTURE, EVIDENCE above).** For p > p\u2080(n), G_n is large enough
that |Der_n|/|G_n| = p_f(n) e^{\u2212M_g(n)}(1 + o(1)), in particular \u03b4_\u221e(n) = exp(\u2212(c + o(1))n\u00b2) with c = 1/4 (n odd),
3/16 (n even).

Conjecture 3.6 is the precise sense in which "monodromy supplies independence of many divisor events at one
polynomial": all q^d shifts of degree d live in *one* cover \u03c6_\u03c3 (so no uniformity in the number of shifts is needed
\u2014 the shifts are integrated into the geometry), and independence *between* shapes is the statement that G_n is
close to a product. Proving it needs ramification data of the \u03c6_\u03c3 (e.g. pairwise distinct branch divisors \u21d2 linear
disjointness, by purity and simple connectivity of A^n in characteristic 0); not attempted beyond n = 3.

### 3.7 What large q can and cannot give in terms of N = q^n (depth accounting)

(a) **Fixed n (PROVED by Thm 3.5).** No saving at all: the exceptional set is \u2265 c_n N.
(b) **The error term is a half-power of q, not of N.** Theorem 3.3 has error O_n(q^{n\u22121/2}) = O_n(N^{1\u22121/(2n)}).
Even if the main term vanished, Lang\u2013Weil-type input saves q^{1/2} = N^{1/(2n)}: never a fixed power of N once n
grows, and it cannot see the square floor q^{n/2} (G5) for n \u2265 2.
(c) **Hybrid regime n \u2192 \u221e, q \u2265 q\u2080(n) (Assessment).** Suppose Conjecture 3.6 and an effective Chebotarev with
error \u2264 E_n q^{n\u22121/2}. Resolving \u03b4 \u2248 e^{\u2212m}, m \u2248 n\u00b2/4, needs q^{1/2} \u2265 E_n e^{m}. Since \u03b4 \u2265 1/|G_n| (Thm 3.5),
|G_n| \u2265 e^m. If E_n is as small as poly(|G_n|), i.e. log E_n \u224d m (cost O(1) per event), then log q \u226b m \u224d n\u00b2,
log N = n log q \u226b n\u00b3, and the saving is m \u224d (log N)^{2/3}. If the cost per shape is its fibre degree, log E_n \u224d
\u03a3_\u03c3 log D_\u03c3 \u224d n\u00b7m (D_\u03c3 \u2248 3^n), then log q \u226b n\u00b3, log N \u226b n\u2074, and the saving is m \u224d (log N)^{1/2}: **exactly the
\u221a(log N) depth barrier of G1, re-encoded as "number of events \u00d7 log(complexity per event) \u2264 log q"** (over \u2124:
"number of events \u00d7 log(modulus per event) \u2264 level log N"). Either way: no power saving from the large-q route.
(d) **What would break depth (Assessment).** An estimate with error C^{n\u00b7O(1)} q^{n/2} (square-root cancellation in all
n dimensions, i.e. cohomology concentrated in the middle degree) for the joint indicator of \u224d n\u00b2 shape events, with
complexity C^{O(n)} *independent of the number of events*. Purity alone does not suffice: with complexity \u220f D_\u03c3 the
budget (n/2) log q affords only \u2248 log q/(2 log 3) events per degree \u2014 bounded at fixed q (\u00a74.3).

### 3.8 What CRT gives in the function-field world (calibration: the integer exponents reappear)

Over F_q[T] the CRT is *exact*: for f uniform in M_n and deg M \u2264 n, f mod M is uniform. So inclusion\u2013exclusion is
exact to depth n/(modulus degree), and Bonferroni gives clean bounds with no error terms. The exponents are the
integer ones.

**Proposition 3.7 (PROVED).** Let q \u2261 3 (mod 4), \u03bc(z) := \u03a3_{deg A \u2264 z} w(A)/|A| (prime family, Def 1.4).
(a) *Prime family, every q.* For 1 \u2264 z \u2264 n \u2212 1 and every L \u2265 0 with 2Lz \u2264 n,
  #{f \u2208 M_n : f mod A \u2209 F(A) for all primes A, deg A \u2264 z} \u2264 q^n (\u220f_{deg A \u2264 z}(1 \u2212 w(A)/|A|) + \u03bc(z)^{2L+1}/(2L+1)!).
Moreover \u03bc(z) \u2265 z/16 \u2212 O(log z) uniformly in q. Hence \u03b4_q(n) \u2264 2 exp(\u2212c\u221an) for an absolute c > 0, all q, n.
(b) *U, large-q limit.* limsup_{q\u2192\u221e} \u03b4_q(n) \u2264 2 exp(\u2212c n^{2/3}) for an absolute c > 0.

*Proof.* (a) For distinct primes A_1, \u2026, A_i with \u03a3 deg A_k \u2264 n the residues f mod A_k are independent and
uniform; classes at the same prime are disjoint. So the i-th Bonferroni sum is exactly e_i(x), x_A = w(A)/|A|, for
iz \u2264 n, and P(avoid) \u2264 \u03a3_{i\u22642L}(\u22121)^i e_i(x) \u2264 \u220f(1 \u2212 x_A) + e_{2L+1}(x) (Bonferroni for the independent model).
Lower bound for \u03bc: for deg A = d odd, w(A) \u2265 #{monic v | A + 1 : deg v \u2264 k\u2080}, k\u2080 := \u230ad/2 \u2212 log_q(2d + 2)\u230b; by
the Riemann hypothesis for Dirichlet L-functions of F_q[T] (Weil; Rosen Thm 4.8),
|#{A prime, deg A = d, A \u2261 \u22121 (v)} \u2212 \u03c0_q(d)/\u03a6(v)| \u2264 (deg v + 1)q^{d/2}/d, and \u03a3_{deg v = k} 1/\u03a6(v) \u2265 1, so
\u03a3_{deg A = d} w(A)/q^d \u2265 (1/(2d))(k\u2080 + 1) \u2265 1/8 for d \u2265 d\u2080; for d even use odd deg v only (\u2265 1/16). Take
z \u2248 \u221a(n/(16e\u00b2)), 2L + 1 \u2248 n/z; U-failure implies avoidance (Def 1.4).
(b) Use only the small-modulus words: pairs (u, v) with a = deg u \u2265 1, b = deg v \u2265 1, a + b \u2264 D, s := n \u2212 a \u2212 b
with s or b odd; each gives the class f \u2261 \u2212u \u2212 v (mod uv), and a hit is a U-witness (t := (f + u + v)/(uv)).
Distinct unordered pairs give distinct classes (u + v and uv determine {u, v}). For j \u2264 n/D the j-th Bonferroni
sum S_j(q) is computed exactly by CRT: q^{\u2212deg lcm} for compatible classes, 0 for incompatible ones. Tuples with
pairwise coprime moduli contribute e_j(q^{\u2212deg M_c}); a pair sharing a prime g of degree e is compatible only if
v\u2032 (or u\u2032) lies in a prescribed class mod g, which costs a factor \u2264 max(q^{\u2212e}, q^{\u2212b\u2032}) \u2264 q^{\u22121} (here b\u2032 \u2265 1 is used;
the v = 1 classes, which are the divisors of f + 1, are exactly the ones excluded because they are not Poisson);
summing over g gives O(D\u2075/q). So S_j(q) \u2192 \u03bc_D^j/j!, \u03bc_D = \u03a3 over admissible unordered types {a, b} of (1 if a \u2260 b,
1/2 if a = b) \u2265 D\u00b2/16 \u2212 O(D). Bonferroni at 2L \u2264 n/D and D \u2248 c\u2080 n^{1/3} give the bound. \u220e

So in the q = \u221e model: **CRT (exact) gives exp(\u2212c n^{2/3}) for U and exp(\u2212c\u221an) for the prime family; the
limit densities (EVIDENCE, \u00a73.6) are exp(\u2212\u0398(n\u00b2)) and, for the prime family, exp(\u2212\u0398(n)) (Poisson).** These are
exactly the integer pictures (2/3 for U, G1's \u221a for the prime family) with log N \u21a6 n. The gap is closed in the
q = \u221e model by one object: the monodromy group G_n of the word covers (Thm 3.3), whose derangement proportion is
the true density. So the brief's question "which input supplies independence of many divisor events at one
polynomial" has a precise answer in F_q[T] at large q: **Chebotarev in the compositum of the word covers (RH for
varieties over F_q) plus the size of G_n (big monodromy, Conjecture 3.6)**. CRT sees only the abelian quotient
information of bounded conductor; G_n is non-abelian and of size \u2265 e^{\u03bc} (Thm 3.5).

## 4. Fixed q, n → ∞

(placeholder)

## 5. Transfer to ℤ

(placeholder)

## 6. Hostile reviews

(placeholder)
