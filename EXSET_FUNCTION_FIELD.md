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

(placeholder)

## 4. Fixed q, n → ∞

(placeholder)

## 5. Transfer to ℤ

(placeholder)

## 6. Hostile reviews

(placeholder)
