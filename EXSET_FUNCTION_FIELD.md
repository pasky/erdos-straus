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

Conversely, if v is monic and A is a monic divisor of f + v with 1 ≤ deg A < n and A ≡ −1 (mod v), then
deg v ≤ deg A < n, t := (A + 1)/v and u := (f + v)/A are monic, and (t, u, v) is a word; deg t = deg A − deg v.
(The degree bound matters: v = f + 2, A = f + 1 satisfies the other conditions but gives u = 2, not monic; R1 repair.)

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
Large-q mass (fixed a and z, then q → ∞): for A generic monic of degree a the pair (A, A + 1) has Galois group
S_a × S_a over F_q(coefficients) (Chebotarev for the joint factorisation, as in the large-q Titchmarsh divisor
problem of Andrade–Bary-Soroker–Rudnick, Phil. Trans. R. Soc. A 373 (2015), App. A), so among primes A of degree a
the average number of monic degree-k divisors of A + 1 tends to 1 for each 0 ≤ k ≤ a. Hence the average of w(A)
tends to a (a odd) resp. a/2 (a even), Σ_{deg A = a} w(A)/q^a → 1 (a odd), 1/2 (a even), and
Σ_{deg A ≤ z} w(A)/|A| → (3/4) z + O(1) for each fixed z: the analogue of Σ_{ℓ≤z} w(ℓ)/ℓ ~ C_V log z has
C_V^{FF} = 3/4 per unit of degree. At fixed q the constant changes (q = 3: ≈ 1.03, §4.2; Assessment).

**Definition 1.5 (ES₅-analogue).** A word with gcd(u, v) = 1 is *bichromatic* if (uv/f) = −1; ES₅,q(f) holds if f
has a bichromatic word. **Lemma 1.6 (PROVED).** For a word of shape (s, a, b) with gcd(u, v) = 1,
(uv/f) = ε^{s(a+b) + ab}. *Proof.* gcd(u, f) = gcd(u, v) = 1 since f ≡ −v (mod u). By (R1),
(u/f) = ε^{an}(f/u) = ε^{an}(−v/u) = ε^{an + a}(v/u), similarly (v/f) = ε^{bn + b}(u/v), and (v/u)(u/v) = ε^{ab}.
The exponent (a + b)(n + 1) + ab with n = s + a + b is ≡ s(a + b) + ab (mod 2). ∎
Squares have no bichromatic word ((uv/g²) = 1).
**Corollary 1.6′ (PROVED; R1 repair of a false non-nesting claim).** ES₅,q(f) ⇒ U_q(f). *Proof.* If s(a+b) + ab is
odd: for s even, a and b are both odd, so (t, u, v) is a U-witness (a ≥ 1, b odd); for s odd, one of a, b is odd,
hence ≥ 1, and (t, u, v) or (t, v, u) is a U-witness (s odd). ∎ The inclusion is strict (q = 3, n = 3: 5 U-failures
against 18 ES₅-failures). *Difference from ℤ.* Over ℤ the nesting goes the other way: Theorem A makes every U-witness
bichromatic, so U ⇒ ES₅. Over F_q[T] a single U-witness need not be bichromatic (shape (0, 2, 1) has (uv/f) = +1 when
gcd(u, v) = 1), because the two symbols (f/A) and (uv/f) are different functions of the shape. Both unions are
T1-obstructed. This document studies U_q.

### 1.3 Why monic and q ≡ 3 (mod 4): the two degenerate normalisations

**Proposition 1.7 (PROVED).** (i) q ≡ 1 (mod 4), monic words: by Lemma 1.1 the colour is never forced, so the
analogue of U is empty and T1 has no content.
(ii) *Leading coefficients free.* Let q be odd and allow the shift v to be any nonzero polynomial (A still monic),
with the colour condition (−v/A) = −1 read off at ∞, i.e. χ(−lc v)^{deg A} ε^{deg v (deg A + 1)} = −1 (the same
computation as Lemma 1.1, now with (R2) for lc v). Call this U′_q. Squares still fail U′_q (same proof as Thm 1.3).
U′_q keeps the degree bounds of Definition 1.2 (1 ≤ deg A < n, deg v < n). If q > (n + 1)², every monic non-square f
of degree n ≥ 2 satisfies U′_q. Hence the exceptional set of U′_q is *exactly* the squares whenever n < √q − 1 (a
sufficient condition, not a necessary one).

*Proof of (ii).* f is not a constant times a square (a monic f = c·h² forces c square). Weil:
|Σ_{y∈F_q} χ(f(y))| ≤ (n − 1)√q. With at most n zeros, #{y : χ(f(y)) = −1} ≥ (q − n − (n−1)√q)/2 > 0 for
q > (n+1)². Take such y, A := T − y, v := −f(y) ∈ F_q^*. Then A | f + v, A ≡ −1 (mod v) (v is a unit),
deg((f+v)/A) = n − 1 ≥ 1, and the colour is χ(−lc v)^1 = χ(f(y)) = −1. ∎

*Reading.* The q − 1 unit shifts carry free quadratic-character data at ∞ ("Frobenius firing", FF_MUTE §§5, 7), and
one Weil sum turns them into a witness. Over ℤ the unit group is {±1} and positivity leaves only the single unit 1 (which
carries no square-class data), so U′ has no integer analogue; a result proved through U′ says nothing about ℤ. With monic shifts (positivity), there is a
single unit shift v = 1, and the mass per shape becomes q-independent (§3.1). **We therefore fix: q ≡ 3 (mod 4), all
of t, u, v, A monic** — among the normalisations compared here, the only one with a nonempty colour layer, T1, and
an integer-like mass. (Assessment: this restores the T1 obstruction that BRAINSTORM/ff_erdos_straus.md §5 found absent for
ES_q(A, P) with a polynomial numerator; there the 2-adic layer was mapped to a finite place.)

## 2. Numerics and controls

Engine `scripts/z51_ffield_enum.c` (C; p prime ≡ 3 mod 4): enumerates, for every shape, all q^n monic triples
(t, u, v), forms f = tuv − u − v, and counts W_U(f) for all q^n monic f of degree n (optionally the ES₅-analogue,
with a gcd test). It also enumerates all squares. Raw output `data/z51_ffield/enum.txt`, `es5_q3.txt`; the failing
non-squares at q = 3 are listed in `data/z51_ffield/fail_q3_n*.txt`. Every entry of Table 2.1 is reproduced by a
line of `enum.txt` (re-run after R1 flagged missing provenance). Independent re-implementations: the Python word
enumerator `scripts/z51_ffield_check.py`, and the R1 reviewer's divisor-table brute force
`reviews/z51_ffield_r1_brute.py` (different algorithm: for each f and each shift v it tests the actual divisors of
f + v), which agree with the C engine for q = 3, 7 and n = 2..5.

**Controls (CERTIFIED for the listed (q, n)).**
* T1: every square fails U_q in every run (sqfailU = #squares, e.g. 2187/2187 at (3, 14), 6859/6859 at (19, 6)).
* Mass identity: the mean of W_U is exactly the number of U-shapes in every run (§3.1, Prop 3.1 below).
* Numerator-8 / hard-prime / R-zero controls: not applicable (no integer n is an input here); the transfer
  question for them is addressed in §5.

**Table 2.1 (CERTIFIED). Non-square exceptional set of U_q, # and fraction of all q^n monic f of degree n.**

| q \\ n | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 | 0 | 5 | 6 | 6 | 21 | 3 | 21 | **0** | 12 | **0** | 7 | **0** | 3 | **0** |
| 7 | .286* | .184 | .0787 | .0179 | .0098 | 6.5e−4 | 5.4e−4 | | | | | | | |
| 11 | | .174 | .0751 | .0119 | .0062 | 2.6e−4 | | | | | | | | |
| 19 | | .175 | .0776 | .0103 | .0044 | | | | | | | | | |
| 31 | | .181 | .0778 | .0101 | | | | | | | | | | |
| 59 | | .195 | .0805 | | | | | | | | | | | |
| 191 | | .2007 | | | | | | | | | | | | |

(q = 3 row: counts; other rows: fractions. *n = 2 exactly: U_q(f) ⟺ f + 1 has a root, so the non-square failure
fraction is (q − 3)/(2q), limit 1/2. Number of U-shapes m(n) = 2, 3, 7, 9, 15, 18, 26, 30, 40, 45, 57, 63, 77, 84
for n = 2..15.)

Two regimes are visible, and they behave oppositely.

1. **Fixed n, q → ∞: the exceptional fraction converges to a positive constant.** n = 3: 0.1745 (q = 19), 0.1911
   (43), 0.2001 (163), 0.2006 (179), 0.2007 (191). The value 29/144 = 0.20139 is the prediction of §3.6 *if* the
   n = 3 monodromy is the full product S₃ × (C₂ ≀ S₃) (not proved). n = 5: 0.0103, 0.0104, 0.0101 at q = 19, 23, 31.
   Theorem 3.5 proves that the fixed-n large-q exceptional set is a *positive proportion* of all f, not O(q^{n−c}).
2. **Fixed q = 3, n growing: the non-square exceptional set thins out** (EVIDENCE to n = 15; that it is eventually
   empty is a conjecture suggested by the data, not a consequence of it), as over ℤ (where U fails only at the odd
   squares and six integers ≤ 978145 up to 10⁹): 0 non-square failures at n = 9, 11, 13, 15 (out of 3^n), and
   12, 7, 3 at n = 10, 12, 14, against 243, 729, 2187 squares. For the even-degree failures, the polynomial part g
   of √f has deg(f − g²) = 1 (6×), 2 (15×) at n = 6; 2 (6×), 3 (15×) at n = 8; 3 (9×), 4 (3×) at n = 10;
   3 (7×) at n = 12; 6 (3×) at n = 14 (R1 corrected table). Since deg(f − g²) ≤ n/2 − 1 holds for every monic f
   of even degree, these values show no special ∞-adic proximity to squares.

ES₅-analogue (q = 3, n = 5..12): non-square failures 114, 75, 660, 321, 3872, 1368, 21903, 5974. These contain the
U_q failures (Cor 1.6′) and are far more numerous at odd n, where only ≈ n²/8 shapes are bichromatic. Squares fail
in all runs. Not pursued further.

The point of the two regimes: the large-q limit keeps the *mass* fixed (m(n) ≈ 3n²/8 expected witnesses, independent of
q, §3.1), so it cannot be a depth breaker in the sense of the brief; the fixed-q limit grows the mass like n² =
(log_q N)², as over ℤ (log² N), and there the exceptional set behaves like the integer one.

## 3. Large q, fixed n

Notation: M_d = monic polynomials of degree d (an affine space A^d over F_q via the non-leading coefficients);
Σ_n = set of U-shapes (s, a, b): s + a + b = n, a ≥ 1, s + b ≥ 1, (s or b odd); m(n) := |Σ_n|;
for a shape σ = (s, a, b) the *word map* φ_σ : M_s × M_a × M_b → M_n, (t, u, v) ↦ tuv − u − v;
W_σ(f) := #φ_σ^{−1}(f)(F_q), so W_U = Σ_{σ ∈ Σ_n} W_σ; δ_q(n) := #{f ∈ M_n(F_q) : W_U(f) = 0}/q^n.

### 3.1 The mass is a shape count, independent of q

**Proposition 3.1 (PROVED).** For every q ≡ 3 (mod 4) and n ≥ 2, q^{−n} Σ_f W_U(f) = m(n) exactly, and
m(n) = 3n²/8 + O(n) (m(n) = 2, 3, 7, 9, 15, 18, 26, 30, 40, 45 for n = 2..11).

*Proof.* The domain of φ_σ has q^s q^a q^b = q^n points and every point maps into M_n, so Σ_f W_σ(f) = q^n.
Shapes ↔ pairs (s, b) with s + b ≤ n − 1, minus those with s and b both even (including (0, 0)):
m(n) = n(n+1)/2 − (k+1)(k+2)/2 with k = ⌊(n−1)/2⌋ (exact formula from R1). ∎

This is the exact analogue of "mass ≍ log² N" for U over ℤ, with log N replaced by n = log_q N. It does not grow
with q. The large-q limit is therefore a *fixed-mass* limit.

### 3.2 The word maps are finite, flat, generically étale, of degree n!/(s!a!b!)

**Lemma 3.2 (PROVED; any characteristic).** For every shape (s, a, b) with s + a + b = n, s + b ≥ 1, s + a ≥ 1,
φ_σ : A^n → A^n is finite and flat of degree D_σ = n!/(s! a! b!), and generically étale.

*Proof.* Give the coefficient of T^{d−i} of a monic polynomial of degree d the weight i. The coefficient y_i of T^{n−i}
of tuv is weighted-homogeneous of weight i in the coefficients x of (t, u, v); the coefficient of T^{n−i} in u + v has
source weight i − (s + b) (from u) resp. i − (s + a) (from v), both < i (e.g. the leading 1 of u contributes source
weight 0 to the target coefficient y_{s+b}, s + b ≥ 1). So φ_σ = h + l with
h(t, u, v) = tuv weighted-homogeneous and l of lower weight in each component. The common zero set of h is {0}
(tuv = T^n forces t = T^s, u = T^a, v = T^b by unique factorisation). Hence h is a homogeneous system of parameters,
k[x] is free over k[h] of rank ∏_i i / ∏_j wt(x_j) = n!/(s!a!b!) (Hilbert series), and by the weight filtration
(gr k[φ] = k[h]) a homogeneous k[h]-basis of k[x] lifts to a k[φ]-basis: φ is finite and flat of degree D_σ. The
Jacobian determinant of φ has top-weight part the Jacobian of h, and h is étale at any (t, u, v) with t, u, v
pairwise coprime (if δt·uv + t·δu·v + tu·δv = 0 with deg δt < s etc., reduce mod t, u, v: δt = δu = δv = 0).
So the Jacobian of φ is not identically zero and φ is generically étale (separable) in every characteristic. ∎

So the generic fibre X_σ of φ_σ is a set of D_σ geometric points. Let L_n be the compositum of the function fields
of all word maps of degree n (all non-degenerate shapes, U or not) over K = F_q(y_1, …, y_n), Ω_n its Galois
closure, G_n = Gal(Ω_n/K) and G_n^geo = Gal(Ω_n F̄_q / F̄_q(y)). G_n acts on ⊔_σ X_σ. Let B_n ⊂ A^n be the union
of the branch loci (a proper closed subset of degree bounded in terms of n). For f ∈ (A^n ∖ B_n)(F_q), W_σ(f) is the
number of fixed points of Frob_f on X_σ (φ_σ is finite étale over f and its source is normal).

### 3.3 The large-q limit in each characteristic is a Chebotarev statistic

**Theorem 3.3 (PROVED, given the Chebotarev density theorem for finite étale Galois covers of open subsets of
A^n_{F_q} with error O(q^{n−1/2}) and constant depending only on the complexity of the defining equations — Lang–Weil
applied to the twists of the cover; e.g. Andrade–Bary-Soroker–Rudnick, Phil. Trans. R. Soc. A 373 (2015), App. A,
Thm A.4; Fried–Jarden, *Field Arithmetic*, §6.4 for the curve case).** Fix n and a prime p ≡ 3 (mod 4). Let G_{n,p}
be the group of §3.2 in characteristic p, Der_{n,p} := {g ∈ G_{n,p} : g has no fixed point on X_σ for every
σ ∈ Σ_n}, ρ_{n,p} := |Der_{n,p}|/|G_{n,p}|. Then for q = p^r ≡ 3 (mod 4),

  δ_q(n) = ρ_{n,p} + O_n(q^{−1/2}),

with the O_n-constant independent of p and r (main term: by Lemma 3.4 G_{n,p} = G_{n,p}^geo, so no Frobenius-coset
restriction). For p > p₀(n), G_{n,p} is the characteristic-0 monodromy group and ρ_{n,p} = ρ_n is a single stable
value; a single limit over *all* q would need ρ_{n,p} = ρ_n also for the finitely many small p (not proved; R1 repair).

*Proof.* Chebotarev applied to Ω_n over A^n ∖ B_n, summed over the conjugacy classes contained in Der_{n,p}; the
points of B_n(F_q) number O_n(q^{n−1}). Uniformity in p: the word maps are given by bounded-degree equations over ℤ;
the Galois closure is a connected component of a bounded fibre power minus diagonals and branch locus, so it and its
twists have complexity bounded in terms of n, and Lang–Weil applies uniformly (the field degree alone would not
suffice; the bounded equations do). ∎

### 3.4 The boundary of the word maps: a copy of S_n, and no constant field extension

**Lemma 3.4 (PROVED; any odd q).** G_n = G_n^geo, and G_n contains a subgroup S ≅ S_n acting on each X_σ
(σ = (s, a, b)) as S_n acts on ordered set partitions of {1, …, n} into blocks of sizes s, a, b.

*Proof.* (Degeneration to the top-weight map.) For c ∈ F_q(μ)^*, c = 1/μ, let S_c act on monic polynomials of degree
d by (S_c g)(T) = c^d g(T/c), and S_c^{(n)} on polynomials of degree ≤ n by g ↦ c^n g(T/c). Then
φ_σ(S_c t, S_c u, S_c v) = S_c^{(n)}(φ^μ_σ(t, u, v)) with φ^μ_σ(t, u, v) := tuv − μ^{s+b} u − μ^{s+a} v.
So over F_q(μ, y) the cover {φ^μ_σ = y} is the base change of {φ_σ = y′} along the purely transcendental extension
F_q(y′) ⊂ F_q(y′, μ) = F_q(μ, y), y′ = S^{(n)}_{1/μ} y; the Galois group of the compositum and its constant field are
unchanged. The family Φ_σ = {(μ, w) ↦ (μ, φ^μ_σ(w))} is finite flat over A^1 × A^n (the proof of Lemma 3.2 with
μ of weight 0), and its fibre at μ = 0 is the top map (t, u, v) ↦ tuv, which is étale over {y : disc y ≠ 0}. So
the generic point ξ of the divisor {μ = 0} (residue field F_q(y)) is unramified in every K(X_σ), hence in Ω_n. For a
place 𝔓 | ξ of Ω_n the decomposition group D_𝔓 ≅ Gal(κ(𝔓)/F_q(y)), and its action on X_σ is the Galois action on
the special fibre {tuv = y} = ordered (s, a, b)-partitions of the roots of y. κ(𝔓) is generated by the residue
fields of these special fibres; the U-shape (0, n − 1, 1) contributes F_q(y)(one root of y), so κ(𝔓) is the
splitting field of the generic polynomial, with group S_n and constant field F_q. Hence D_𝔓 ≅ S_n acts as stated.
(Over the henselisation of F_q(y)[μ]_(μ) the whole finite flat algebra of each Φ_σ is étale, because its special fibre
is étale over the generic point; finite étale algebras are stable under compositum and Galois closure, so every
place of Ω_n over ξ is unramified and the decomposition action is the residue action on the special fibre.)
Constants of Ω_n inject into κ(𝔓), whose constant field is F_q; so Ω_n ∩ F̄_q = F_q and G_n = G_n^geo. ∎

### 3.5 The fixed-n target of the brief is false: a positive proportion of non-squares fail

**Theorem 3.5 (PROVED, given Chebotarev as in Thm 3.3).** For every n ≥ 2 there are c_n > 0 and C_n such that for
every odd q,

  #{f ∈ M_n(F_q) : f has no nontrivial word, i.e. none of any shape other than (n, 0, 0)} ≥ c_n q^n − C_n q^{n−1/2},

with c_n ≥ 1/∏_σ D_σ! (product over all non-degenerate shapes). The right side is positive only for q ≥ q₀(n); for
small q it says nothing (e.g. (q, n) = (3, 9) has no U-failure at all). In particular, for q ≡ 3 (mod 4),
#{f non-square : U_q(f) fails} ≥ c_n q^n − C_n q^{n−1/2} − q^{n/2} (squares: q^{n/2} for n even, none for n odd):
**for fixed n and q ≥ q₀(n), the non-square exceptional set of U_q is a positive proportion of all f, so no bound
O(q^{n−c}) (nor o(q^n)) holds as q → ∞.** The same holds for the ES₅-analogue and for every union of word shapes
that excludes the trivial shape (n, 0, 0) (every f has the trivial word (f + 2, 1, 1)).

*Proof.* Let g₀ ∈ S ≤ G_n be the element acting as an n-cycle on the roots (Lemma 3.4). An n-cycle fixes no ordered
set partition with at least two non-empty blocks (blocks are ordered, so equal block sizes do not help), and every
non-degenerate shape other than (n, 0, 0) has at least two non-empty blocks. So g₀ is fixed-point-free on every such
X_σ. Its conjugacy class C has |C|/|G_n| ≥ 1/|G_n| ≥ 1/∏ D_σ!. Since G_n = G_n^geo, C lies in the Frobenius coset
for every q (it is arithmetically permitted), and Chebotarev gives #{f ∉ B_n : Frob_f ∈ C} ≥ (|C|/|G_n|)q^n −
C_n q^{n−1/2}; such f have no rational point in any fibre. ∎

**Corollary 3.5′ (primes; PROVED, same hypotheses).** Adjoin the splitting field of f to Ω_n. Under the scaling of
Lemma 3.4 it is unchanged (y′ = S^{(n)}_{1/μ}y has roots μ^{−1}·(roots of y)), so the boundary copy S ≅ S_n acts on
the roots of f itself, and g₀ acts on them as an n-cycle. Hence, for q ≥ q₀(n), at least c′_n q^n − C′_n q^{n−1/2}
polynomials f — all of them irreducible — have no nontrivial word: **at fixed n and large q, a positive proportion of prime polynomials fail U_q** (and
ES₅,q). Primality does not help in the large-q regime (contrast the Linnik-confinement door T2 over ℤ, where
primality is what escapes the square floor).

*Reading.* The forest of a typical f is empty with probability bounded below in the large-q limit; the frozen
element is the boundary n-cycle ("f irreducible at the cusp"). Nothing like this happens over ℤ, where the mass
log² N grows. The brief's Goal 1 ("O(q^{n−c}) at fixed n") is false for U_q; in the lc-free normalisation U′_q it
is true for a trivial reason (Prop 1.7(ii)). Neither is a depth statement.

### 3.6 A Poisson heuristic for ρ_n, and finite-q comparisons

**n = 3 (EVIDENCE + computation).** U-shapes: (0, 2, 1), (1, 2, 0) (both: "f + 1 has a root") and (1, 1, 1). For
(1, 1, 1), t = T − x, u = T − α, v = T − β: matching coefficients gives
x³ + c₂x² + (c₁ + 3)x + c₀ + c₂ = 0, i.e. f(x) + 3x + c₂ = 0, and then α, β are the roots of
Z² + (c₂ + x)Z + c₁ + 2 + x(c₂ + x), discriminant Δ(x) = −3x² − 2c₂x + c₂² − 4c₁ − 8. So W_{(1,1,1)}(f) =
Σ_{x: f(x)+3x+c₂=0} (1 + χ(Δ(x))), the monodromy of (1,1,1) is inside C₂ ≀ S₃ (order 48, derangement proportion
29/48), and if it is all of C₂ ≀ S₃ and linearly disjoint from the S₃ of f + 1 (derangement proportion 1/3), then
ρ_3 = 29/144 = 0.20139 (CONDITIONAL on these two monodromy statements, which are not proved here; 29 = 1 + 3·4 + 2·8
derangements of C₂ ≀ S₃, checked by R1). Observed (Table 2.1): 0.2001, 0.2006, 0.2007, 0.2014 at q = 163, 179, 191,
167.

**General n (EVIDENCE).** Model: shapes with s = 0, a = 0 or b = 0 are governed by the factorisation of f + 1
(f + 1 = (u−1)(v−1), resp. u(t−1), resp. v(t−1)); U-failure forces f + 1 irreducible (n odd) resp. all irreducible
factors of f + 1 of even degree (n even), probabilities p_f(n) = 1/n resp. binom(n, n/2)/2^n. Genuine shapes
(s, a, b ≥ 1), grouped in u ↔ v pairs, are treated as independent Poisson variables of mean 1 (a ≠ b) or 1/2
(a = b); total mean M_g(n) = 0, .5, 1.5, 3, 4.5, 7.5, 9, 14, 15, 22.5 for n = 2..11, M_g(n) ≈ n²/4 (n odd),
3n²/16 (n even). Prediction δ_∞(n) ≈ p_f(n) e^{−M_g(n)}:

| n | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|
| model | 0.5 | 0.2022 | 0.0837 | 0.00996 | 0.00347 | 7.9e−5 |
| largest q run | limit 1/2 (proved) | 0.2007 (q=191) | 0.0805 (q=59, rising) | 0.0101 (q=31) | 0.0044 (q=19, falling) | 2.6e−4 (q=11, falling) |

**Independence test (CERTIFIED; `scripts/z51_ffield_joint.c`, `data/z51_ffield/joint.txt`).** Group the genuine
shapes into unordered classes c = {(s, a, b), (s, b, a)} (identical fibres) and record W_c(f) for all f. Ratio of
P(all W_c = 0) to ∏_c P(W_c = 0), and of P(all W_c = 0 and the f + 1 condition) to the product with P(f + 1 cond):

| n (classes) | q | ratio (genuine) | ratio (with f + 1) | (ratio − 1)·q |
|---|---|---|---|---|
| 4 (2) | 11 / 43 / 59 | 1.078 / 0.999 / 1.003 | 1.228 / 0.998 / 1.002 | 0.9 / −0.04 / 0.15 |
| 5 (4) | 11 / 23 / 31 | 1.215 / 1.098 / 1.064 | 1.454 / 1.157 / 1.094 | 2.4 / 2.3 / 2.0 |
| 6 (6) | 11 / 19 | 1.769 / 1.329 | 2.427 / 1.488 | 8.5 / 6.3 |

The defect decays like C(n)/q, and pairwise E[W_c W_d] → E[W_c]E[W_d] (e.g. 2.0021 vs 2 at (43, 4)). So the
compositum behaves like a direct product of the class groups and the S_n of f + 1, up to lower-dimensional
corrections. *Why CRT cannot prove this and what exactly is missing.* For two classes with moduli A, A′ (the smaller
of the two divisors in (1.1), degree ≤ (n+1)/2) and deg A + deg A′ ≤ n, the fibre product X_c ×_Y X_d is birational
to {(word data, coprime)} × A^{n − deg A − deg A′}, which is irreducible (non-coprime data give dimension ≤ n − 1);
this is the CRT computation. For k events of total modulus degree > n the class intersection holds at most one f,
and the k-fold fibre product is a codimension-(Σ deg − n) subvariety of the parameter space whose irreducibility is
exactly the missing statement.

**Conjecture 3.6 (big monodromy for word maps; CONJECTURE, EVIDENCE above).** In stable characteristic
(p > p₀(n)), ρ_n = exp(−(c + o(1))n²) as n → ∞ through each parity, with c = 1/4 (n odd), 3/16 (n even). (Stronger
form, also conjectural: ρ_n = p_f(n)e^{−M_g(n)+o(1)}; the n ≤ 7 data do not distinguish these, and at n = 7 the
q = 11 value is still 3× the model.)

Conjecture 3.6 is the precise sense in which "monodromy supplies independence of many divisor events at one
polynomial": all q^d shifts of degree d live in *one* cover φ_σ (so no uniformity in the number of shifts is needed
— the shifts are integrated into the geometry), and independence *between* shapes is the statement that G_n is
close to a product. Proving it needs ramification data of the φ_σ. A sufficient criterion for the product structure:
the sets of codimension-one branch components of the *Galois closures* of the classes (and of f + 1) are pairwise
disjoint (then, by Zariski–Nagata purity and simple connectivity of A^n over ℂ, each closure meets the compositum of
the others in K). Merely distinct branch divisors do not suffice (R1: K(√x, √y) and K(√x, √z) share K(√x)). Not
attempted beyond the computations above.

### 3.7 What large q can and cannot give in terms of N = q^n (depth accounting)

(a) **Fixed n (PROVED by Thm 3.5).** For q ≥ q₀(n) no saving at all: the exceptional set is ≥ c_n N/2.
(b) **The error term is a half-power of q, not of N (PROVED, elementary).** Theorem 3.3 has error
O_n(q^{n−1/2}) = O_n(N^{1−1/(2n)}). Even if the main term vanished, this input saves q^{1/2} = N^{1/(2n)}: never a
fixed power of N once n grows, and for even n ≥ 2 it cannot resolve the square floor q^{n/2} (G5).
(c) **Hybrid regime n → ∞, q ≥ q₀(n): conditional budget analogies (Assessment, not theorems).** Suppose the main
density is ρ_n = e^{−m_n} and an effective Chebotarev bound has relative error E_n q^{−1/2}. The large-q route
certifies ρ_n at size q only if (1/2) log q − log E_n − m_n → +∞. (Note ρ_n ≥ 1/|G_n| holds for the limiting group
density, not for δ_q(n): (q, n) = (3, 9) has δ = 0.) Two illustrative cost models, at the least admissible q:
  * log E_n = O(n²) (O(1) cost per shape; an *additional* assumption — log |G_n| ≥ m_n gives only a lower bound):
    log q ≍ n², log N = n log q ≍ n³, saving m_n ≍ (log N)^{2/3} at best;
  * log E_n ≍ Σ_σ log D_σ ≍ n³ (cost ≈ fibre degree per shape; unproved model): log q ≍ n³, log N ≍ n⁴, saving
    m_n ≍ (log N)^{1/2} at best.
For larger q these are upper bounds on what m_n can supply. In the second model the integer depth barrier of G1
reappears as "number of events × log(complexity per event) ≲ log q" (over ℤ: "number of events × log(modulus per
event) ≲ level log N") — an analogy, not an impossibility theorem for large-q methods.
(d) **A proposed direction (Assessment).** A depth breaker would need, for the joint indicator of ≍ n² shape events, a
separately stated cancellation hypothesis: error exp(O(n))·q^{n/2} (vanishing of the trace-function cohomology
outside the middle degree), with the exponential constant controlled relative to q and complexity independent of the
number of events. Purity alone does not give this. With complexity ∏ D_σ ≈ 3^{nk} for k interior shape events, the
budget (n/2) log q allows k ≲ log q/(2 log 3) events *in total* — bounded at fixed q (§4.3).

### 3.8 What CRT gives in the function-field world (calibration: the integer exponents reappear)

Over F_q[T] the CRT is *exact*: for f uniform in M_n and deg M ≤ n, f mod M is uniform. So inclusion–exclusion is
exact to depth n/(modulus degree), and Bonferroni gives clean bounds with no error terms. The exponents are the
integer ones.

**Proposition 3.7.** Let q ≡ 3 (mod 4), μ(z) := Σ_{deg A ≤ z} w(A)/|A| (prime family, Def 1.4).
(a) *Prime family, every q (PROVED).* For any set 𝒞 of prime-family classes with moduli of degree ≤ z ≤ n − 1, of
total mass μ_𝒞 := Σ_{c ∈ 𝒞} q^{−deg M_c}, and every L ≥ 0 with 2Lz ≤ n,
  #{f ∈ M_n : f in no class of 𝒞} ≤ q^n (∏_{A}(1 − x_A) + μ_𝒞^{2L+1}/(2L+1)!),  x_A := mass of 𝒞 at the prime A.
Moreover μ(z) ≥ z/16 − O(1) uniformly in q. Hence δ_q(n) ≤ C exp(−√n/16) for an absolute C, all q ≡ 3 (mod 4), n.
(b) *U, large-q limit (CONDITIONAL on Lemma C2 below; the reduction is PROVED).* limsup_{q→∞} δ_q(n) ≤
2 exp(−c n^{2/3}) for an absolute c > 0.

*Proof.* (a) For distinct primes A_1, …, A_i with Σ deg A_k ≤ n the residues f mod A_k are independent and
uniform; classes at the same prime are disjoint. So the i-th Bonferroni sum is exactly e_i(x) for iz ≤ n, and
P(avoid 𝒞) ≤ Σ_{i≤2L}(−1)^i e_i(x) ≤ ∏(1 − x_A) + e_{2L+1}(x) (Bonferroni for the independent model) ≤
∏(1 − x_A) + μ_𝒞^{2L+1}/(2L+1)!. Lower bound for μ: for deg A = d odd (all v admissible), w(A) ≥ #{monic v | A + 1 :
deg v ≤ k₀} with k₀ := ⌊d/2 − log_q(2C₀(d + 1))⌋ (these residues −v are distinct), where C₀ is the absolute constant
in the Riemann-hypothesis bound for primes in progressions (Weil; Rosen Thm 4.8):
|#{A prime, deg A = d, A ≡ −1 (v)} − π_q(d)/Φ(v)| ≤ C₀(deg v + 1)q^{d/2}/d. With Σ_{deg v = k} 1/Φ(v) ≥ 1 and
π_q(d) ≥ (q^d − 2q^{d/2})/d this gives Σ_{deg v = k} #{A : v | A+1} ≥ q^d/(2d) for 0 ≤ k ≤ k₀ and d ≥ d₀ (absolute),
hence Σ_{deg A = d} w(A)/q^d ≥ (k₀ + 1)/(2d) ≥ 1/8; for d even use odd deg v ≤ k₀ only (≥ 1/16 − o(1)). Degrees
d < d₀ are dropped (k₀ < 0 is possible there). So μ(z) ≥ z/16 − O(1). *Trimming (R1 repair):* every single class has
mass ≤ q^{−1}, so we can choose 𝒞 ⊂ prime family (degrees ≤ z) with z/16 − O(1) ≤ μ_𝒞 ≤ z/16. Take z := ⌊√n⌋,
2L + 1 := largest odd number ≤ n/z: then e·μ_𝒞/(2L + 1) ≤ 1/2 for n ≥ n₀, so the remainder is ≤ 2^{−(2L+1)} ≤
2^{−√n + 2}, and ∏(1 − x_A) ≤ e^{−μ_𝒞} ≤ C e^{−√n/16}. U-failure implies avoidance (Def 1.4).
(b) Use only the small-modulus words: pairs (u, v) with a = deg u ≥ 1, b = deg v ≥ 1, a + b ≤ D, s := n − a − b
with s or b odd; each gives the class f ≡ −u − v (mod uv), and a hit is a U-witness (t := (f + u + v)/(uv)).
Distinct unordered pairs give distinct classes (u + v and uv determine {u, v}). For j ≤ n/D the j-th Bonferroni
sum S_j(q) is computed exactly by CRT: q^{−deg lcm} for compatible classes, 0 for incompatible ones.
*Coprime part.* Tuples with pairwise coprime moduli contribute e_j(q^{−deg M_c}) minus the product mass of
non-coprime tuples; the latter is ≤ binom(j, 2) μ_D^{j−2} Σ_P (Σ_{c : P | M_c} q^{−deg M_c})² ≤ binom(j,2) μ_D^{j−2}
Σ_{e ≤ D} (q^e/e)(2D² q^{−e})² = O_{D,j}(1/q). So the coprime part tends to μ_D^j/j!.
*Non-coprime part (reduction, PROVED).* Every f has at most B(n) := Σ_σ D_σ words (fibres of finite flat maps of
degree D_σ), so the non-coprime compatible j-tuples contribute at most B(n)^j·P_f(E_2), where E_2 = "f has two
distinct small-modulus witness words whose moduli have a common root".
**Lemma C2 (CONDITIONAL input; Assessment that it holds).** For fixed n and D with 2D ≤ n, P_f(E_2) → 0 as q → ∞.
Equivalently (finite flat maps, bounded complexity): for each pair of small shapes, the locus of pairs of distinct
words with a common root of their moduli has dimension ≤ n − 1 in the fibre product. *Why it should hold:* on a
stratum where uv and u′v′ share a factor g, compatibility requires g | (u + v − u′ − v′); with b, b′ ≥ 1 the free
cofactors make this a nontrivial condition, which costs a factor ≤ max(q^{−deg g}, q^{−b′}) ≤ q^{−1} when the shared
factor involves only part of uv; the remaining case u′v′ | uv needs a polynomial identity among complementary
divisors which fails unless {u′, v′} = {u, v}. The case analysis was checked for the patterns listed, not for all
overlap patterns (R1: "supply a cluster/overlap-counting lemma"); the v = 1 classes (divisors of f + 1) are excluded
precisely because for them compatibility is automatic (r ≡ −1 always).
Given Lemma C2, S_j(q) → μ_D^j/j!, μ_D = Σ over admissible unordered types {a, b} of (1 if a ≠ b, 1/2 if a = b) ≥
D²/16 − O(D), and Bonferroni at 2L ≤ n/D with D ≈ c₀ n^{1/3} gives the bound. ∎

So in the q = ∞ model: **CRT (exact) gives exp(−c√n) for the prime family (PROVED, every q) and exp(−c n^{2/3}) for
U (given Lemma C2); the limit densities are, by the Poisson heuristic and the data of §3.6, exp(−Θ(n²)) and, for the
prime family, exp(−Θ(n)).** These are
exactly the integer pictures (2/3 for U, G1's √ for the prime family) with log N ↦ n. The gap is closed in the
q = ∞ model by one object: the monodromy group G_n of the word covers (Thm 3.3), whose derangement proportion is
the true density. So the brief's question "which input supplies independence of many divisor events at one
polynomial" has a precise answer in F_q[T] at large q: **Chebotarev in the compositum of the word covers (RH for
varieties over F_q) plus the size of G_n (big monodromy, Conjecture 3.6)**. CRT sees only the abelian quotient
information of bounded conductor; G_n is non-abelian, and |G_n| ≥ 1/ρ_n ≥ c·e^{√n/16} (Thm 3.5 with Prop 3.7(a)).

## 4. Fixed q, n → ∞

### 4.1 The data look like ℤ

Table 2.1, q = 3: the non-square exceptional set is 5, 6, 6, 21, 3, 21, 0, 12, 0, 7, 0, 3, 0 for n = 3..15, against
3^{⌊n/2⌋} squares. Odd n ≥ 9: none (EVIDENCE to n = 15, N = 3^15 ≈ 1.4·10^7). Even n: decreasing. This is the
integer census pattern (squares plus six sporadic exceptions ≤ 978145 up to 10^9). Contrast with the q = ∞ model
value p_f(n)e^{−M_g(n)} of §3.6: at (q, n) = (3, 10) it predicts 0.004 exceptions, but there are 12; small q has
*more* sporadic failures at even n than the Poisson model, and none at odd n ≥ 9. Some have no word at all
(q = 3: 15 wordless f at n = 8, 3 at n = 10; `scripts/z51_ffield_check.py`).

### 4.2 RLD-U over F_q[T]: numerically as plausible as over ℤ

**Conjecture 4.1 (FF-RLD-U; CONJECTURE).** For fixed q ≡ 3 (mod 4) and s > 1, with z = n/s,
#{f ∈ M_n non-square avoiding F(A) for all primes A, deg A ≤ z} ≤ e^{C(q,s)} q^n ∏_{deg A ≤ z}(1 − w(A)/|A|).

**Table 4.1 (CERTIFIED; `scripts/z51_ffield_rld.c`, `data/z51_ffield/rld.txt`). Ratio sifted/(q^n·Mertens), q = 3.**

| n | z ≈ n/2 | z ≈ n/1.5 | z = n − 1 |
|---|---|---|---|
| 10 | 1.43 (z=5) | 6.52 (z=8; s = 1.25) / 2.13 (z=6) | 23.2 |
| 12 | 1.31 (z=6) | 3.17 (z=8) | 34.1 |
| 14 | 1.51 (z=7) | 3.19 (z=9) | 53.5 |
| 15 | 1.15 / 1.46 (z=7 / 8) | 2.64 (z=10) | 10.7 |

At fixed s the ratio stays O(1) (≈ 1.2–1.5 at s = 2, ≈ 2.6–3.2 at s = 1.5) and grows as s → 1: the same shape as
the integer RLD-U evidence (EXSET_ARITH_JANSON_OPUS §5.5). The prime-family mass at q = 3 is μ(z) = 1.00, 1.67,
2.85, 3.59, 5.02, 5.77, 7.27, 8.06, 9.61, 10.41, 11.98, 12.79, 14.38, 15.19 (z = 1..14): ≈ 1.03 per degree (odd
degrees ≈ 1.4, even ≈ 0.75). Consequence (CONDITIONAL on Conj 4.1, as C1 Cor 6.1): #{non-square failures} ≤
e^{C} 3^{n(1 − 1.03/(s log 3)) + o(n)}, below the square floor 3^{n/2} for s < 1.87.

So in a world where the Riemann hypothesis for every Dirichlet L-function is a theorem (Weil) and the CRT is exact
up to level n, RLD-U is still open and still numerically true. **Assessment: neither RH nor level-1 distribution is
the missing input for RLD-U.** This is the F_q[T] face of (D)15/22: termwise RH for a character expansion of the sieve
pays the ℓ¹ mass of the expansion, ∏_A(1 + w(A)); and a single residue class modulo M with deg M > n contains at most
one f of degree n, so RH cannot extend the exact level n of §3.8 for the class events themselves.

### 4.3 What can be proved at fixed q

* Prop 3.7(a) (PROVED, every q ≡ 3 mod 4): δ_q(n) ≤ C exp(−√n/16). This is the G1 value with log N ↦ n.
* (PROVED, trivial) U-failure forces all irreducible factors of f + 1 to have even degree (n even; shapes (0, a, b)
  with b odd) resp. f + 1 irreducible (n odd), so δ_q(n) ≪ n^{−1/2} resp. ≤ 1/n + O(q^{−n/2}) — one Landau-type event.
* That is the strongest fixed-q statement this lane proves. A U_q-analogue of the 2/3 bound (Vaughan / I3 §8.8 type)
  should transfer with the large sieve over F_q[T], but at fixed q the non-coprime terms of §3.8(b) are O(1), not
  O(1/q), and need the integer machinery; not attempted (it would re-derive the CRT exponent).

**Why "Weil bounds for products of many characters with loss O(k)" do not give FF-RLD-U (Assessment; the proved
ingredients are named).**
(i) *Rank one vs high rank.* Square-root cancellation with loss linear in k exists for products of rank-one trace
functions: Σ_{c∈F_q} ∏_{i≤k} χ(P_i(c)) ≤ (Σ deg P_i)√q (Weil). This is the engine of Carmon–Rudnick (Chowla, large q)
and of Sawin–Shusterman, who turn μ(r + s^p) into a quadratic character in s via Pellet's formula
μ(g) = (−1)^{deg g}χ(disc g) (in characteristic p, (s^p)′ = 0). Their k-point Chowla (Ann. Math. 196 (2022),
Thm 1.3) needs q > p²k²e², i.e. k < √q/(pe): **at fixed q the number of controlled shifts is bounded, and at q = p
prime it is zero.** The U data that are rank one are exactly the colours (f/A) = χ(Res(A, f)): they detect
non-squareness (every non-square f has an inert prime of degree ≤ 2 log_q n + O(1), by RH for y² = f) but not
witnesses. A U-event of shape σ is the trace function of φ_{σ*}Q̄_ℓ, of generic rank D_σ = n!/(s!a!b!) (Lemma 3.2),
and a joint indicator of k shape events has rank up to ∏ D_σ: complexity multiplies.
(ii) *Budget.* A sum over M_n whose cohomology is concentrated in the middle degree has error ≲ (rank)·C^n·q^{n/2}.
To stay below the main term q^n e^{−μ} with rank ≈ 3^{nk} for k shape events needs k ≲ log q/(2 log 3) — bounded
at fixed q, while RLD-U at level z = n/s needs ≈ μ(z) ≍ n events. So **depth × log(rank per event) ≤ (n/2) log q**:
the F_q[T] form of G2 ("per-event saving must beat per-event loss"). Rank-one events would cost ≈ log n each and
allow ≈ n log q / log n events — enough. The U-events are not rank one, and no reduction of them to rank-one events is
known; the only U-events that are factorisation-type functions of a single polynomial are the v = 1 events ("f + 1
has an odd-degree divisor").

## 5. Transfer to ℤ

### 5.1 Ingredient by ingredient

| Ingredient (F_q[T]) | What it gives here | Integer analogue | Status over ℤ | Gives RLD-U / T1-min over ℤ? |
|---|---|---|---|---|
| Colour layer at ∞: degree parity, q ≡ 3 (4) (Lemma 1.1) | T1 for U_q (Thm 1.3) | 2-adic layer 4ℤ ∪ (8ℤ − n) (Thm B/E of z48) | PROVED | T1 only (obstruction, not existence) |
| Unit shifts with free leading coefficient (Prop 1.7(ii)) | exceptional set = squares exactly for q > (n+1)², by one Weil sum | none: units {±1}, positivity | — | no (the mechanism does not exist over ℤ) |
| Exact CRT up to degree n (§3.8) | √n (prime family, PROVED), n^{2/3} (U, q = ∞, given Lemma C2) | level of distribution 1 for all moduli ≤ N (stronger than EH) | conjectural (EH) | no: Prop 3.7 is the integer CRT exponent; CRT caps G1/(D)17 |
| RH for Dirichlet L-functions (Weil) | least inert prime ≤ 2 log_q n + O(1); equidistribution in progressions; μ(z) ≍ z | GRH | conjecture | no: in F_q[T] RH holds and RLD-U is still open and numerically true (Table 4.1); (D)15/22 |
| Lang–Weil / Chebotarev for the word covers φ_σ (Thm 3.3) | exact large-q limit; q^d shifts of degree d integrated into one cover; positive-proportion failure (Thm 3.5) | none: needs n to be a point of a variety over a finite field with q → ∞ at fixed "degree" | — | no: fixed mass (no depth); error q^{n−1/2} = N^{1−1/(2n)} (§3.7(b)) |
| Monodromy of the word covers G_n (Conj 3.6) | the true density p_f(n)e^{−M_g(n)} = e^{−Θ(n²)} at q = ∞ | the Poisson word model ("independent shapes") | heuristic | would give finitely many non-square exceptions, but over ℤ it is not a separate input: it *is* the conclusion |
| Purity / middle-dimensional cohomology (Sawin; Sawin–Shusterman) | k-point Chowla for k < √q/(pe) | uniform k-point Chowla / Elliott with √N error | open (k = 2 log-averaged only) | for rank-one events only; U-events are high-rank (§4.3) |
| Pellet's formula + (s^p)′ = 0 | makes μ(r + s^p) a character in s | none (no Frobenius-linear structure in ℤ) | — | no |

### 5.2 The three questions of the brief, answered

**RH for curves vs GRH.** Present in F_q[T] as a theorem; it does not decide FF-RLD-U (open, numerically true) and
does not move the CRT exponents (Prop 3.7 attains exactly the integer CRT exponents, √ for the prime family and 2/3
for U). So GRH is not the missing input over ℤ either (Assessment, consistent with (D)15/22).

**Monodromy vs nothing.** The large-q depth breaker in F_q[T] is Chebotarev in the compositum of the word covers
plus the size of G_n. It acts on a fixed number m(n) ≈ 3n²/8 of shape events, each integrating q^{s+b} shifts
geometrically. Over ℤ there is no family of finite fields over which the integers vary, hence no G_n. Over ℤ the
analogue of "Frob_f ∈ G_n" is the profinite residue vector of n, and its information is exactly the CRT information.
The non-abelian, non-CRT part of G_n has no integer counterpart. (Lemma 3.4: G_n contains the boundary S_n, which
already is non-abelian; CRT corresponds to abelian quotients of bounded conductor.)

**Number of shifts vs degree.** In the large-q regime the number of shifts is irrelevant; the number of *shapes*
(≈ n²) is the mass, and it does not grow with q. That is why Goal 1 fails (Thm 3.5). In the fixed-q regime the depth
needed is ≍ n² (U) or ≍ n (prime family) events. The geometric methods available at fixed q control a number of
events bounded in terms of q (Sawin–Shusterman: k < √q/(pe), rank one). The relevant ratio is depth × log(rank) vs
(n/2) log q.

### 5.3 Conditional integer statements: tested

(a) *GRH (⇔ Weil) + level-1 distribution (⇔ exact CRT).* Both hold in F_q[T]. With them, the best provable FF bound
is the CRT one (Prop 3.7). No implication "GRH + EH ⇒ T1-min" can be proved by an argument that transfers to F_q[T]
unless the same argument proves FF-T1-min, and no such argument is known there either. FF-T1-min is presumably true
(Table 2.1, Table 4.1), so the FF world cannot *refute* such an implication. The test is negative only in this
weak sense (Assessment).
(b) *Katz–Sarnak-type statements for the quadratic family* L(s, χ_n) ⇔ the hyperelliptic ensemble y² = f. They
govern the colour data (f/A), i.e. rank-one information: least non-residue, inert-prime statistics. These separate
squares from non-squares but are not U-witnesses. Their integer versions (n-level densities) bear on the
Linnik-confinement door T2, not on T1-min. Their FF versions are theorems at large q, and do not decide U_q (Thm 3.5
holds regardless). So: no.
(c) *A Poisson/independence hypothesis for word statistics over ℤ* (the analogue of Conj 3.6) would give a finite
non-square exceptional set. But over ℤ it is a restatement of the conclusion (H⁻mom-type, LOWERTAIL_DEEP_ASTRA
Thm 7.1). In F_q[T] at large q it is a statement about a finite group at each n, checkable in principle. That is the
only genuinely new feature of the function-field model, and it does not transfer.

**Verdict on transfer (Assessment).** No ingredient that is a theorem in F_q[T] and has a standard integer analogue
(GRH, level-1 distribution, Katz–Sarnak for the quadratic family) yields RLD-U or T1-min, even in F_q[T]. The
ingredient that does carry the true densities in F_q[T] (monodromy of the word covers, at large q) has no integer
analogue, and it acts only in a fixed-mass regime.

## 6. Hostile reviews

(placeholder)
