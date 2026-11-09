# Z69_IDEAB — independent ideation on Erdős–Straus (lane IDEAB, wave z69)

**ES is OPEN. Nothing here claims otherwise.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.

Status: Phase 1 in progress (written from own knowledge only; no repo memo / FRONTIER / git grep consulted;
only `z69_lanes.md` header+IDEAB and `z58_lanes.md` Common rules + falsifier table were read).

## §0 Falsifier table — placeholder
The mandatory falsifier table (F1 odd squares, F2 numerator 8 / C-even, F3 composites, F4 known zeros) is filled in
for the Phase-3 idea in §3, after Phase 1 is committed (the table's notation (★), R, 𝔊*, 𝔐 is campaign-internal and
I have deliberately not looked it up yet). During Phase 1 each idea carries its own "squares / six classes" line.

## §1 Phase-1 idea list (independent)

### 1.0 Working reformulations (all PROVED, elementary; derived here from scratch)
Let p ≡ 1 (mod 4) be prime (p ≡ 3 mod 4 is trivial). Every solution has p | exactly one or exactly two denominators.

* **(R1) two-divisor form.** Put e = 4x − p > 0 (e ≡ 3 mod 4), x = (p+e)/4. Then (ey − px)(ez − px) = p²x², hence
  ES(p) ⟺ ∃ e ≡ 3 (4) and δ | x² with δ ≡ −x (mod e) [**Type II**, p | y,z] or δ ≡ −4x² (mod e) [**Type I**, p | z only].
  Equivalently with coprime a,b | x: e | a+b (II) or e | a+pb (I).
* **(R2) six-parameter form (Elsholtz–Tao style).** II: 4abd = p+e, ce = a+b. I: 4abd = pe+1, ce = a+b.
  So both types ask for the *same* thing on two different numbers: N/4 has coprime divisors a,b with e | a+b, where
  N = p+e (II) or N = pe+1 (I).
* **(R3) one-equation forms.** II ⟺ pc = 4abcd − a − b ⟺ (4acd−1)(4bcd−1) = 4c²dp + 1.
  I ⟺ (4acd − p)(4bcd − p) = p² + 4c²d ⟺ (4acd − p) | (4a²d + 1).
* **(R4) residue-class ("identity") forms.** Fixing all but one parameter gives the congruence classes that polynomial
  identities cover:
  K1 (II, d free): p ≡ −e (mod 4ab), e | a+b.  K2 (II, b free): p ≡ −4a²d (mod 4k−1), ad | k.
  K3 (I, c free): p ≡ −f (mod 4ad), f | 4a²d+1.
  Two memorable special cases: **F1** ∃ q ≥ 1: (−p mod 4q) divides q+1;  **F2** ∃ k ≥ 1: (−p mod (4k−1)) divides k.
* **(R5) reciprocity lemma (why squares die).** In any Type I/II solution with gcd(a,b)=1 the Jacobi symbol of p at
  the odd part of ab is −1 when p ≡ 1 (8) (computation: (−e/a) = (a/e) for e ≡ 3 (4), so (p/ab) = (ab/e) = (−a²/e) = −1);
  in form K2 the modulus u = 4k−1 itself satisfies (p/u) = −1. So every "coprime-type" solution carries a
  quadratic-non-residue witness for p; n = m² has none (its solutions all come from m). Also: for odd prime q | x_e,
  (q/e) = (p/q). The six classes mod 840 are exactly the unit squares mod 840, i.e. p that look like squares at 2,3,5,7.
* **(R6) Euclid/continued-fraction form.** II ⟺ ∃ u ≡ 3 (4) and integers b,c ≥ 1 with a := bu − pc > 0 and
  4ac | u+1. Since then 0 < b/c − p/u = a/(cu) < 1/(2c²), b/c is automatically a convergent of p/u. For c = 1:
  **p/u = a − 1/(4d − 1/b)**, i.e. p is the numerator of a length-3 Hirzebruch–Jung (minus) continued fraction
  [[a, 4d, b]]; in SL₂ terms −p is the upper-right entry of TᵃL^{−4d}Tᵇ.
* **(R7) modular-hyperbola form.** c = 1, II ⟺ ∃ u,u* ∈ [1,p) with uu* = 1 + 4dp and u ≡ u* ≡ −1 (mod 4d): a point of
  the modular hyperbola mod p congruent to (−1,−1) modulo (4 × its own branch index).

### 1.1 The ideas
Format per idea: **Key lemma** (precise) · **Squares** (where non-squareness enters / why it fails on m²) ·
**Six classes** (how p ≡ 1,121,169,289,361,529 mod 840 are treated) · **Assessment**.

**I1. Profinite exceptional set ("converse Schinzel", uniform covering).**
Let U ⊂ Ẑ be the (open) union of all identity classes K1∪K2∪K3 and C = Ẑ^× ∖ U (closed). Schinzel/Mordell: C ⊇ S :=
{unit squares of Ẑ}. ES for p ≡ 1 (4) ⟺ no prime lies in C.
*Key lemma (CONJECTURE UC):* C ∩ {α ≡ 1 mod 4} = S; equivalently (compactness) for every modulus m and every unit class
r mod m containing no square, **finitely many** identity classes cover all of r mod m. UC ⟹ ES, since a prime is not a
square in Ẑ. UC is strictly stronger than ES (ES only says primes ∉ C, and primes are merely dense).
*Squares:* they are exactly the allowed exceptional set; non-squareness enters as "p ∉ S, so some finite level (m, r)
separates p from S". *Six classes:* p in a square class mod 840 is handled at the level m = 840·q^j with q the least
non-residue prime of p; UC predicts a **bound on the least identity modulus that is uniform over all n ≡ r (mod m)**
— a sharply testable prediction (and falsifiable: one non-square integer n with no coprime-type solution kills UC as stated
and forces a description of the true C).
*Assessment:* cleanest "structural" strengthening I know; the test is cheap. Top-5.

**I2. Structure theory of C when UC fails.** If some non-square integers n lie in C (no K1/K2/K3 class contains n),
describe C∩ℤ algebraically (e.g. "n = m²k with k from an explicit set", or "n divisible by …").
*Key lemma (form):* C ∩ ℤ ⊂ {n : n has property 𝒫} with 𝒫 visibly false for primes (as "is a square" is).
*Squares:* inside C by construction. *Six classes:* a prime in the six classes is excluded from C iff 𝒫 fails for it;
so the whole problem is transferred to *naming* 𝒫. *Assessment:* only meaningful after the I1 experiment; paired with I1.

**I3. Hirzebruch–Jung / continuant formulation (R6).** ES(c=1) ⟺ p = K⁻(a,4d,b) := 4abd − a − b ⟺ the lens space
L(p,u) (u = 4db−1) is surgery on a 3-chain with framings (−a,−4d,−b) ⟺ Dedekind sum identity
12·s(u,p) = (u+u*)/p + (a+4d+b−9).
*Key lemma (needed):* for fixed prime p the set {u mod p : HJ-length(p/u) = 3 with middle term ≡ 0 (4)} is non-empty;
a route would be exact formulas for the number of u with HJ-length ≤ 3 (Heilbronn/Porter-type statistics are asymptotic
only for *typical* length ≍ log p, so the length-3 stratum is a thin "cusp" of the distribution).
*Squares:* n = m² has length-3 expansions only with middle term ≢ 0 (4) or with gcd(u,n) > 1 — R5 is the reason.
*Six classes:* no special treatment; the method would have to see (p/u) = −1.
*Assessment:* pretty, probably only a restatement; gives access to Dedekind-sum reciprocity. Mid.

**I4. Modular hyperbola + Weil (R7).** Points (u,u*) of uu* ≡ 1 (mod p) are equidistributed in boxes of area ≫ p^{3/2+ε}
(Kloosterman/Weil) — an *individual-p* tool.
*Key lemma (needed):* a count, with error o(main), of points with (u,u*) ≡ (−1,−1) mod q, q = 4·(branch index).
*Obstruction found while writing it down:* the event has probability ≍ 1/p per point (the modulus is tied to the branch),
so detecting it needs all ≍ p harmonics; Weil saves only √p. Summing over the natural 2-parameter family gives main term
≍ log² p against error ≍ √p. *Squares:* the count is identically 0 on squares, so any asymptotic "main term" must be
cancelled by real characters there — the main term is not the naive one. *Six classes:* none.
*Assessment:* dead as stated (binary-problem barrier); recorded so it is not re-tried naively.

**I5. Parity by involution (Zagier / Heath-Brown "one-sentence" style).**
*Key lemma (needed):* a finite set W_p ⊇ {solutions of pc = 4abcd − a − b} with two involutions σ, τ, where Fix(σ) is a
single explicit point for every prime p ≡ 1 (4) and Fix(τ) ⊂ {ES solutions}. Then |W_p| odd ⟹ ES(p).
Natural candidates: W = {(u,v,d): uv = 4dp+1} (all factorizations, all d ≤ p), or matrices [[u,p],[4d,v]] ∈ Γ₀(4) with
upper-right entry p, with σ a "windmill" move changing d and τ = transpose (u ↔ v).
*Squares:* the proof must break because for n = m² an extra σ-fixed point appears (as in Zagier's proof, where
compositeness creates extra fixed points). *Six classes:* none needed — parity arguments are blind to residue classes,
which is their attraction. *Obvious worry:* a ↔ b symmetry makes ordered counts even, and unordered counts have no reason to
be odd; quick test: tabulate the parity of the unordered Type II (c=1) and total counts over primes. *Assessment:*
long shot but nearly free to test. Top-5 (as a cheap kill).

**I6. Class-number / mock-theta generating function.** G(q) = Σ_{a,b,d ≥ 1} q^{4abd−a−b} = Σ_{a,b} q^{4ab−a−b}/(1−q^{4ab})
is a double Lambert (Appell–Lerch-like) series; for fixed d the exponent is an indefinite binary quadratic form
(unimodular Gram matrix [[4d,−1],[−1,0]], vectors (a,1),(b,1)).
*Key lemma (needed):* G = (modular/mock-modular object with explicit Eisenstein part) + (cuspidal part with a proved
coefficient bound smaller than the Eisenstein coefficient at primes). *Squares:* coefficients vanish at m² only after
restricting to gcd-coprime solutions, so the Eisenstein part must carry a factor like Σ over real characters that vanishes
on squares (L(1,χ_n)-like or a class number H(·)) — a strong structural prediction about what the "main term" is.
*Six classes:* would be uniform. *Assessment:* the cubic exponent 4abd makes this a sum over d of weight-1 indefinite
theta objects of varying level; no single automorphic form. I expect this was looked at; low prior. Not top-5.

**I7. Unprovability in open induction (IOpen).** *Claim (PROVED, short):* ES fails in Shepherdson's model
M = {a₀ + Σ_{i≥1} a_i t^{i/Q} : a₀ ∈ ℤ, a_i real algebraic}, hence IOpen ⊬ ES.
*Proof.* Take n = 4t + 1 ≥ 2. Suppose x,y,z ∈ M, positive, with 4/n = 1/x+1/y+1/z. Regard them as real polynomials in
s = t^{1/Q} on [0,∞); positivity in M = positivity for large s. If xyz had a root in [0,∞), let ρ be the largest; on
(ρ,∞) all three are positive and the identity holds pointwise, but as s → ρ⁺ the left side stays ≤ 4 while the right
side → +∞. So x,y,z > 0 on [0,∞), and their constant terms x₀,y₀,z₀ are positive integers with 1/x₀+1/y₀+1/z₀ =
4/n(0) = 4 > 3. Contradiction. ∎
(Conversely if the constant term a₀ of n is ≥ 2 and ES(a₀) holds in ℤ, then scaling x = x₀·n/a₀ solves ES(n) in M; so in
M the conjecture fails exactly "because 4/1 has no solution".)
*Squares / six classes:* n = 4t+1 is ≡ 1 modulo every standard integer, i.e. it sits over the profinite point α = 1 ∈ S;
the obstruction used is archimedean (4 > 3), not Jacobi. *Assessment:* a genuine (if easy) unprovability theorem in a
natural weak theory; M has no non-standard primes, so it says nothing about "ES for primes". Worth recording; Phase 2
must check whether it is in the literature. Candidate strengthening = I8.

**I8. Unprovability for *primes* in Z-ring / Bézout models; Schinzel's theorem as a model-theoretic statement.**
For α ∈ Ẑ let R_α = {f ∈ ℚ[t] : f(α) ∈ Ẑ}, a discretely ordered Z-ring in which t is irreducible. ES(t) holds in R_α
⟺ some polynomial identity is integral on a class α mod D ⟺ α ∈ U (the set of I1). So **R_α ⊭ ES(t) ⟺ α ∈ C**:
the closed set C of I1 is exactly the set of "types of non-standard primes at which congruence reasoning cannot prove ES".
*Key lemma (needed for a theorem about a named theory):* embed R_α (α ∈ S) in a model of IOpen + Bézout + normality
(Macintyre–Marker / Smith constructions keep t prime) without creating new solutions — solutions would be Puiseux-type
generalized polynomials, to be excluded by combining the largest-root argument of I7 with the Jacobi argument R5.
*Squares:* α ∈ S is the hypothesis. *Six classes:* the non-standard prime t is in the class 1 mod 840.
*Second half (bounded arithmetic):* ES is ∀Σᵇ₁; by Buss witnessing, S¹₂ ⊢ ES ⟹ a polynomial-time algorithm n ↦ (x,y,z).
Heuristically the least identity modulus for the worst p ≤ N is exp(c(log N)^{1/3}) (expected number of K1 hits with
ab ≤ T is ≍ log³T), so exhaustive identity search is *not* polynomial time: "S¹₂ ⊢ ES" would need a new algorithm
(CONDITIONAL statement, not a result). *Assessment:* I7+I8 together are the most concrete route to the brief's
"unprovable in a natural weak theory". Top-5.

**I9. Non-congruence identities over norm forms.** Every p in the six classes is p = X² + 840Y² (840 is idoneal; the
principal genus is exactly the square classes). Look for identities 4/(X²+DY²) = 1/x+1/y+1/z with x,y,z ∈ ℚ[X,Y]
integral on a class of (X,Y). Schinzel's theorem (one variable) does not forbid these: at points where X²+DY² is a square
the solution may degenerate to non-coprime type.
*Key lemma (needed):* existence of such an identity for each class of (X,Y) mod M up to signs.
*No-go found (PROVED, degree count):* with a,b,c,d,e ∈ ℚ[X,Y] and N of degree 2, 4abd − e = N, ce = a+b forces
(i) a congruence identity in disguise, or (ii) N + const reducible, or (iii) (4dac−1) | N + 4da² with a linear, which
needs N to be constant on a line — impossible for a non-degenerate N. So there is **no quadratic-degree two-variable
identity**; higher degree (a,b,d of total degree > 2 with cancellation) is excluded by e | a+b bounding deg e.
*Residual idea:* non-polynomial arithmetic functions of (X,Y), e.g. a = a prime factor of X: (p/q) = (D/q) for q | X, so
half of all p = X²+840Y² have a non-residue witness dividing X, governed by a quartic symbol ((−840)^{1/4}, a D₄ governing
field). *Squares:* Y = 0. *Six classes:* this idea is *only* for them. *Assessment:* identity version dead by the no-go;
the governing-field remark may be a useful *classifier* of hard primes (I19).

**I10. Unit/Pell orbits and the negative Pell equation.** For prime p ≡ 1 (4) the fundamental unit has norm −1
(X² + 1 = pY²) — a classical property separating such primes from squares *and* from most composites n ≡ 1 (4).
*Idea:* feed Pell data into K3: 4a²d + 1 = pY² (2a = X, d = 1) needs f | pY², f ≡ −p (mod 4a).
*Kill (PROVED):* all prime factors of Y are ≡ 1 (4) (they divide X²+1), so every divisor g of Y² is ≡ 1 (4), whereas
f = g or f = pg must be ≡ 3 (4). With dX² + 1 = pY² (d > 1) the congruence is not excluded but the family is
exponentially sparse (Σ_j τ(Y_j²)/X_j < ∞): expected number of hits finite and tiny. More generally the positive
solution set is finite, so no infinite group orbit can live inside it. *Squares:* ℚ(√n) = ℚ, no units — the idea *does*
use non-squareness at an identifiable step. *Six classes:* none. *Assessment:* dead as a construction; the
"norm −1 unit" property survives only as a possible explanatory variable for composite failures (to test in Phase 2
against the campaign's F3 list).
