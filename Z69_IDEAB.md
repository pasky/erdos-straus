# Z69_IDEAB — independent ideation on Erdős–Straus. Verdict: **no NEW idea (25/25 already in the campaign); inconclusive / narrowed on UCOVER O2 (integer-side certificates + a five-prime reduction); HOT LEAD: no**

Lane IDEAB, wave z69 (brief `z52bbriefs/z69_lanes.md` §IDEAB; common rules `z58_lanes.md`).
**ES is OPEN. Nothing here proves or disproves ES or any case of it.** Internal, unrefereed.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z69_ideab_*`,
data `data/z69/ideab/` (< 1 MB). No provider / auth / quota error occurred in this lane (one hostile-review
subagent call; see §4).

**Protocol.** §1 (Phase 1: 24 ideas + sanity checks) was written from my own knowledge and committed (commit `d86981e6c`)
before anything in the repo other than the two brief files was read. §2 (lookup) and §3 (push) came after.
CERTIFIED in this memo means: an exact finite computation by the stated script, with the stated independent check;
it does not mean a second full-range engine unless said.

**Results in one paragraph.**
* (i) **Phase 1–2.** 24 independently generated approaches (+1 late) with key lemma / squares / six-classes lines;
  post-hoc lookup: **all 25 are already in the campaign** (table in §2), most of them with the same kill. Unprimed, I
  re-derived the (★) and López lines, T1 by reciprocity, the profinite uncovered set with its one-prime profiles,
  CONV-II and its exception 4545, open-induction unprovability, and ended at the same wall (one tied divisor event,
  polylog expected witnesses). That is weak EVIDENCE that the campaign's map of elementary approaches is saturated.
* (ii) **Phase 3 (UCOVER O2: does K = {1 mod 840, (n/11) = −1} meet U?).** Lemma E (PROVED): K_r ∩ U ≠ ∅ ⟺ the
  least ET-family-class modulus λ_ET(p) is unbounded on the primes of K_r. CERTIFIED: over all primes ≤ 10¹² the running
  maximum of λ ≤ λ_ET (least modulus in a superset enumeration; single engine, record primes double-checked) in K_2 and K_6 grows like in the square class (to 1979 and 1247); explicit residue classes show that
  **every finite family-class cover of the large primes of K_2 or K_6 needs a modulus > 10⁴**.
* (iii) **Level-by-level picture (Q-S and §3.6).** For a finite prime set S′ ∋ 11 the family classes with S′-smooth
  modulus have *finite* total weight (PROVED). For S′ = {2,3,5,7,11} they leave an uncovered part of the box B_r of
  measure ≈ 0.048 (r = 2) and ≈ 0.013 (r = 6), stable from 10⁶ to 10⁸ (CERTIFIED exact to 10⁷, Monte Carlo at 10⁸).
  Adding 13 kills nine resp. ten of the twelve residue classes mod 13 outright (level 10⁵) and leaves ≈ 1 % of the
  surviving square class v ≡ 3 resp. 4 mod 13 (level 10⁷, Monte Carlo). So at the two stages and the finite levels
  computed the uncovered set thins sharply but stays non-empty. EVIDENCE for O2 of a kind independent of UCOVER's
  profile computations; the finite-level survivors are generic squares at 3, 5, 7, and exist for r = 6 as well.
  Nothing is proved about all moduli at any stage; not a proof of O2; no bearing on ES itself.

## §0 Falsifier table (mandatory; for the Phase-3 object = Lemma E + the certificates + (Q-S))

The Phase-3 object is a statement about what *finite identity covers* (equivalently IOpen/NOI proofs, by
`Z65_LOGIC2.md` Thm D) can do on the class K. It is not a positivity mechanism, so the screens are passed vacuously;
the table records how it interacts with them.

| screen | behaviour |
|---|---|
| **F1 odd squares** | T1 (no family class contains a unit square residue) is *used as an engine*: a residue that is a square away from 11 can only be caught by classes with 11 ∣ modulus (§3.4). The five-prime runs check it: 0 compatible classes with 11 ∤ modulus at every level (§3.5; in the §3.6 runs with a non-residue coordinate at 13 such classes legitimately exist and are kept), and no class of modulus ≤ 3000 contains m², m < 200 odd (§3.2). Nothing here is an argument for positivity, so there is no step that "uses primality"; in a square class Lemma E returns sup λ = ∞, as it must. |
| **F2 numerator 8 / C-even** | No distinction between C odd and C even is made or needed: λ is the minimum over all seven ET families. Restricting the class table (e.g. to the C-even half of (★)) can only increase λ; Lemma E holds verbatim for any fixed set of families. Nothing here can "prove" R₈(p) > 0: the twelve R₈-zero primes simply have λ ≤ 248 through other families. |
| **F3 composites** | Lemma E and the certificates are about *unit* residue classes (primes). The 285 composite (★)-zeros all lie in some family class of modulus ≤ 548 (they have other solutions); 4545 has no Type II class but a Type I class (S1). Composites sharing a factor with a modulus are outside the statement. |
| **F4 known zeros** | The 14 (★)-zero primes have λ ≤ 239 (λ(409) = λ(577) = 7, λ(8 813 281) = 111, λ(1 726 201) = 239) and the 38 𝔊*-zero primes λ ≤ 239: λ is finite there because other lines solve them. No positivity of R or R_𝔊* is asserted anywhere. |

**HOT LEAD: no.** (Phase-1 ideas carry their own "squares / six classes" lines in §1.1.)

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
* **(R7) modular-hyperbola form.** c = 1, II ⟺ ∃ positive integers u, u* with uu* = 1 + 4dp and u ≡ u* ≡ −1 (mod 4d)
  (u = 4db−1, u* = 4da−1): integer *lifts* of a point of the modular hyperbola mod p, congruent to (−1,−1) modulo
  4 × the branch index. *[Corrected after internal review: the first version required u, u* ∈ [1,p), which is false —
  p = 5: 21 = 3·7. The lifts need not be reduced mod p.]*

### 1.1 The ideas
Format per idea: **Key lemma** (precise) · **Squares** (where non-squareness enters / why it fails on m²) ·
**Six classes** (how p ≡ 1,121,169,289,361,529 mod 840 are treated) · **Assessment**.

**I1. Profinite exceptional set ("converse Schinzel", uniform covering).**
Let U⁺ ⊂ Ẑ be the (open) union of all identity classes K1∪K2∪K3, viewed as cylinders in Ẑ; C := (1 + 4Ẑ) ∖ U⁺ (closed);
C^× := C ∩ Ẑ^× (this is the campaign's U) and S^× := (Ẑ^×)², the unit squares. Schinzel/Mordell: C^× ⊇ S^×. ES for a prime
p ≡ 1 (4) with a Type I/II solution ⟺ p ∉ C (p is an element of Ẑ, not a unit).
*[Corrected twice after internal review: the first version put C inside Ẑ^× (positive integers are not units of Ẑ); the
second claimed C ⊇ all squares of Ẑ (false: 0 is a square, 0 ∉ 1+4Ẑ) and "primes are dense" (true only in Ẑ^×). The
conjecture below is about unit profiles; the integer statement is IUC in S1.]*
*Key lemma (CONJECTURE UC):* C^× = S^×; equivalently (compactness) for every modulus m and every unit class
r mod m containing no square, **finitely many** identity classes cover all of r mod m. UC ⟹ ES for all large primes of every non-square unit class, hence ES (a prime lies in a non-square unit class modulo
some m). UC is strictly stronger than ES (ES only concerns the primes of each unit class, which are dense in Ẑ^× but are not all of it).
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
*Assessment:* pretty, probably only a restatement; gives access to Dedekind-sum reciprocity. Mid. *[Review note: with
entries equal to 1 allowed, [[a,4d,b]] is a formal minus continuant, not always the canonical HJ expansion; the lens-space
/ Dedekind-sum dictionary needs a, b ≥ 2.]*

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
For α ∈ Ẑ let R_α = {f ∈ ℚ[t] : f(α) ∈ Ẑ}, a discretely ordered Z-ring in which t is irreducible when α is a unit. ES(t) holds in R_α
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
needs N to be constant on a line — impossible for a non-degenerate N. So, apart from congruence identities in disguise (case (i)), there is **no quadratic-degree two-variable Type II
identity**; higher degree (a,b,d of total degree > 2 with cancellation) is excluded by e | a+b bounding deg e.
*Residual idea:* non-polynomial arithmetic functions of (X,Y), e.g. a = a prime factor of X: (p/q) = (D/q) for q | X, so
half of all p = X²+840Y² have a non-residue witness dividing X, governed by a quartic symbol ((−840)^{1/4}, a D₄ governing
field). *Squares:* Y = 0. *Six classes:* this idea is *only* for them. *Assessment:* identity version dead by the no-go;
the governing-field remark may be a useful *classifier* of hard primes (I19).

**I10. Unit/Pell orbits and the negative Pell equation.** For prime p ≡ 1 (4) the fundamental unit has norm −1
(X² + 1 = pY²) — a classical property separating such primes from squares *and* from most composites n ≡ 1 (4).
*Idea:* feed Pell data into K3: 4a²d + 1 = pY² (2a = X, d = 1) needs f | pY², f ≡ −p (mod 4a).
*Kill (PROVED):* all prime factors of Y are ≡ 1 (4) (they divide X²+1), so every divisor g of Y² is ≡ 1 (4), whereas
f = g or f = pg must be ≡ 3 (4). With dX² + 1 = pY² (d > 1) the congruence is not excluded but (Assessment, heuristic — not a no-go) the family is
exponentially sparse (Σ_j τ(Y_j²)/X_j < ∞): expected number of hits finite and tiny. More generally the positive
solution set is finite, so no infinite group orbit can live inside it. *Squares:* ℚ(√n) = ℚ, no units — the idea *does*
use non-squareness at an identifiable step. *Six classes:* none. *Assessment:* dead as a construction; the
"norm −1 unit" property survives only as a possible explanatory variable for composite failures (to test in Phase 2
against the campaign's F3 list).

**I11. Consecutive-integer formulation; simultaneous multiplicative constraints.** By R1/R2, with x = (p+3)/4:
Type II fails for p ⟺ for every j ≥ 0 the integer **x + j has no two coprime divisors a,b with a + b ≡ 0 (mod 4j+3)**;
Type I fails ⟺ the same for the integers ((4j+3)p + 1)/4. Let B_e = {m : no coprime a,b | m with e | a+b}; B_e is
"multiplicatively defined" (m ∈ B_e depends only on the multiset of residues mod e of the prime powers of m) and thin
(density ≍ (log)^{−1/2} or smaller). A counterexample is an x with x + j ∈ B_{4j+3} for all j ≥ 0 — a statement about a
run of consecutive integers in the spirit of Grimm / Erdős–Woods problems.
*Key lemma (needed):* for some explicit J, ⋂_{j ≤ J} (B_{4j+3} − j) contains no x with 4x−3 prime (or is finite).
*Squares:* for p = m² and every j with gcd(m, e) = 1 (so gcd(x+j, e) = 1), x + j lies in the *quadratic* part of B_e: by R5,
(q/e) = (p/q) = +1 for every prime q dividing x + j to an odd power, so all divisors lie in the kernel of the Jacobi character (·/e) while −1 does not *[corrected after review: "are squares mod e" is right only for prime e]*. Non-squareness enters as: ∃ q with (p/q) = −1,
hence the quadratic obstruction is absent for all j ≡ −x (mod q), j ≢ −x (mod q²). *Six classes:* those j are sparse
(spacing q ≥ 11), which is exactly why these primes are hard. *Assessment:* a clean way to *state* what a proof must do
(beat the non-quadratic part of B_e on a progression of j); tools for correlations of multiplicative functions
(Matomäki–Radziwiłł–Tao) give only almost-all statements. Not top-5 but it frames I12, I17.

**I12. Force smooth shifts by CRT, then a "divisors cover all residues" theorem.** Choose j ≡ −x (mod Q), Q = ∏_{q ≤ y} q
restricted to non-residue primes for p; then Q | x + j and e = 4j+3 < 4Q.
*Key lemma (needed, Erdős–Hall type):* if m has ≥ C log e distinct prime factors not all in a proper subgroup-coset
configuration mod e, then {a/b} ∋ −1 (mod e).
*Kill (PROVED, counting):* x + j has ≈ y/log y forced primes, giving 3^{π(y)} ratios a/b, against e ≍ e^{y}; the forced
part can never cover (Z/e)^×, and making e small again (e | a+b ≤ Q+1) just returns the K1 covering with ab | Q, whose
total weight Σ_{ab | Q} τ(a+b)/(4ab) is finite for each Q. *S-unit variant:* allow a,b to be S-units with unbounded
exponents (a = q^i, b = r^j, e | q^i + r^j, 4q^i r^j | p + e): infinitely many trials but Σ over S-unit pairs of
τ(a+b)/(4ab) ≤ C·∏_{q∈S}(1−1/q)^{−2} < ∞ — again a finite expected count, so no "infinitely many trials" argument.
*Squares / six classes:* uses only non-residue primes, so it is honest about squares; hard classes = few small such
primes. *Assessment:* dead; the general lesson (**every structured sub-family has finite total weight; divergence of
the full weight ≍ log³p needs all scales**) is a constraint on any constructive proof.

**I13. Largest denominator first ("subtraction") and induction.** Writing z = pk first: 4/p − 1/(pk) = (4k−1)/(pk), so
**Type II ⟺ ∃ k: (4k−1)/(pk) is a sum of two unit fractions ⟺ ∃ k and coprime a,b | k with pa + b ≡ 0 (mod 4k−1)** (this
is K2). Similarly 4/p = 4/(p+δ) + 4δ/(p(p+δ)) with 4 | p+δ is R1. *Induction attempt:* use ES for smaller numbers
(e.g. for x = (p+3)/4 or for k) to build the two-term representation. *Kill:* the two-term problem m/N = 1/y+1/z is a
divisor-class condition on N with modulus m ≈ 4k, unrelated to 3-term representations of 4/k; no descent step exists
because the surface 4xyz = n(xy+yz+zx) is linear in each variable (no Vieta involution, unlike Markoff).
*Squares:* the only "inductive" structure of ES is n ↦ mn, which is precisely how squares are solved and why it cannot help
primes. *Six classes:* n/a. *Assessment:* dead; recorded for the multilinearity remark.

**I14. Integral points on the Cayley cubic; Brauer–Manin with an archimedean region.** 1/x+1/y+1/z+1/w = 0 with
w = −n/4 is a hyperplane-type section of Cayley's 4-nodal cubic (Heath-Brown's count N(B) ~ cB log⁶B of rational points
uses the same torsor parametrization as R2). Signed solutions (4/n = 1/x+1/y−1/z) always exist, so the integral Hasse
principle holds trivially; ES asks for an integral point in the *positive* region of X_n(ℝ), a non-compact region of
logarithmic "volume" (≍ log³ n expected points).
*Key lemma (needed):* strong approximation on the relevant torsor *with* archimedean localisation of logarithmic size —
far beyond known technology (equidistribution of integral points needs volume ≥ n^δ).
*Squares:* the vanishing of coprime-type solutions for n = m² is a Brauer–Manin-type (reciprocity) obstruction on the
torsor where gcd(n, x) = 1; for non-square n it disappears. A *disproof* would need a new obstruction beyond the quadratic
one (I20). *Six classes:* no role. *Assessment:* good language, no mechanism. Not top-5.

**I15. Genus theory of the discriminants Δ = 4c²dp + 1.** R3 says: Δ = uv with u ≡ v ≡ −1 (mod 4cd). For c = d = 1 this
fails iff every prime factor of 4p+1 is ≡ 1 (4) *[the gloss "iff −1 is everywhere a local norm from ℚ(√(4p+1))" of the first version is false for non-squarefree 4p+1, e.g. p = 61, 245 = 5·7²; removed after review]* — a genus-type condition; pure genus
theory. For general (c,d) the condition "the discriminant has a divisor in the class −1 mod 4cd" is a statement about
the image of the ambiguous classes of ℚ(√Δ) under the characters of conductor 4cd, i.e. about ℚ(√Δ, ζ_{4cd}) — a
Rédei-symbol-like object. For c = 1 (Δ = 4dp+1 non-square) p splits in ℚ(√Δ) with 𝔭·𝔡 principal (form [d,1,−p] has discriminant 4dp+1). *[Scope "c = 1" added after review.]*
*Key lemma (needed):* a reciprocity law expressing χ(u) (χ mod 4cd, u | Δ) through symbols depending on p only, summed over
(c,d) with a sign-definite total. *Squares:* for p = m², (p/u) = 1 contradicts R5's (p/u) = −1: genus theory itself
kills them. *Six classes:* here (p/q) = 1 for q ≤ 7 forces u to contain a prime ≥ 11 that is a non-residue for p.
*Assessment:* the c = d = 1 case is a nice sanity anchor; the general case is a restatement unless a Rédei-type
reciprocity appears. Mid.

**I16. Divisor-in-progression sums with modulus tied to the shift.** R_II(p) = Σ_{a,d} #{f | p + 4a²d : f ≡ −1 (4ad)},
R_I(p) = Σ_{a,d} #{f | 4a²d + 1 : f ≡ −p (4ad)}. In R_I the numbers 4a²d+1 do **not** depend on p: R_I(p) =
#{(a,d,f) : f | 4a²d+1, 4ad | p + f} is a pure covering count; in R_II they do.
*Key lemma (needed):* a lower bound for the short-interval sum Σ_{a ≤ A} τ(p+a; 4a, −1) for a *single* p.
*Kill:* each term is one event of probability ≍ τ/a; dispersion/Kloosterman methods average over ≫ p^δ independent
moduli *and* over the number being divided; here both are tied to a. Same binary barrier as I4.
*Squares:* sum is 0. *Six classes:* none. *Assessment:* dead as analysis; but the p-independence of the Type I
family (a fixed, explicit, p-free table {(4ad, −f)}) is worth remembering for I1's computations.

**(R8) quadratic-order form (PROVED, added to 1.0).** In a Type II solution put f = 4acd − 1, e = 4abd − p. Then
**p + d(2a)² = f·e**, f ≡ −1, e ≡ −p (mod 4ad). So for d = 1 a solution *is* a positive binary form [f, 4a, e] of
discriminant −4p whose middle coefficient B = 4a divides f + 1; equivalently the element 1 + 2c√(−dp) of ℤ[√(−dp)] has an
ideal factor of norm ≡ −1 (mod 4cd). Dually, for Type I the integer p² + 4c²d = N(p + 2c√(−d)) has the divisor f = 4acd − p ≡ −p (mod 4cd); in ℤ[√(−d)] this is
an *ideal* factor of **p + 2c√(−d)** of that norm, in an order that does not depend on p (d = 1 impossible: p² + 4c² is a sum of
two coprime squares, so its divisors are ≡ 1 mod 4). *[Corrected after internal review: the first version said "a factor",
suggesting an element; the ideal need not be principal — p = 13, (a,b,c,d) = (1,2,1,5), 189 = 7·27, and 7 is not a
norm from ℤ[√−5].]*

**I17. Class group of discriminant −4dp; Heegner points on thin lines.** By R8 (d = 1): ES(p) ⟸ Cl(−4p) contains a form
[A,B,C] (not necessarily reduced; B > 0, 4 | B ≤ A+1) with **A ≡ −1 (mod B)**. Such forms represent A ≡ 3 (4), so they
live in the *non-principal genus* (genus character χ₋₄). In Heegner-point terms z = (−B + 2i√p)/(2A) lies on the line
x = −(1 + y/√p)/(2c), c = (A+1)/B. Expected number: ≍ L(1,χ₋₄ₚ)·log p reduced ones, ≍ log²p in all.
*Key lemma (needed):* for every prime p ≡ 1 (4) some class of the non-principal genus of Cl(−4dp) (some odd d) contains
such a form. Tools that work for *individual* p here: Duke equidistribution of Heegner points (power saving, but only
for regions of area ≫ p^{−δ}; the target is a curve), genus theory, composition. A structural hope: the property
"B | A+1" might be stable under composition with a fixed class or under an involution, making the set of good classes a
coset-like object which cannot be empty.
*Squares:* for n = m² the discriminant −4m² has no primitive form representing a number ≡ 3 (4) (norms from ℤ[i]):
the non-principal genus is *empty*. So non-squareness enters at an identifiable step: **χ₋₄ is a non-trivial genus
character of disc −4dn**. *Six classes:* 3 and 7 are inert, 5 splits; A must contain a prime q ≡ 3 (4) with (p/q) = −1,
so q ≥ 11: the good forms have A ≥ 11 but nothing else changes. *Numerator-8 remark:* for 8/p the same computation gives
p + 2d(2a)² = fe, i.e. only **even d**; any argument along I17 must use odd d (for d even, 2 | disc/4 and the genus
structure changes). *Assessment:* new to me, gives a place for individual-p tools and an honest use of non-squareness.
Top-5.

**I18. Stratify by the least non-residue; pseudosquare bound.** Let q(p) be the least prime with (p/q) = −1.
*Key lemma (form):* for each prime q and each non-residue class r mod q there is a finite identity family F_{q,r} covering
every n ≡ r (mod q) that is a square modulo all primes < q (this is UC of I1 restricted to the "pseudosquare corridor").
Then ES holds for all p with q(p) ≤ Q once the lemma is verified for q ≤ Q, i.e. for all p below the pseudosquare L_Q
(L_Q grows like e^{cQ/log Q}); under GRH q(p) < 2 log²p, giving ES conditionally on the lemma for all q.
*Squares:* q(m²) = ∞. *Six classes:* they are the corridor q(p) ≥ 11; Mordell's theorem is the lemma for q ≤ 7.
*Assessment:* this is the constructive face of I1; the computation "does the corridor at q = 11, 13 close?" is the
decisive experiment. Top-5 jointly with I1.

**I19. Extreme-value diagnostics (disproof-side heuristic).** For each one-parameter family (F1, F2, d = 1, …) the
number of solutions should be Poisson-like with mean μ_F(p) = c_F log²p·(local factors); the number of zeros up to N
is then ≈ Σ_p e^{−μ_F(p)}. *Key lemma (form):* none — this is a calibration device: a family whose observed zeros
exceed the Poisson prediction signals hidden structure (an obstruction), one with fewer signals hidden positive
correlation (a mechanism). *Squares:* the local factor must vanish there (product over real characters). *Six classes:*
local factors are smallest there. *Assessment:* EVIDENCE-type only; cheap; useful to choose which family to attack.

**I20. Disproof via a non-quadratic reciprocity obstruction.** Squares fail by one line of quadratic reciprocity (R5).
Look for a thin family T ⊄ {squares} containing primes on which a *higher* reciprocity law (quartic, Rédei, cubic)
forbids every K1/K2/K3 class. *Key lemma (form):* n ∈ T ⟹ for all (a,d,k): n ≢ −4a²d (mod 4k−1), etc. First test:
list the non-square integers with no coprime-type solution (I2) and look for algebraic shape (values of a polynomial or
norm form?). *Squares:* the model case. *Six classes:* T would have to live inside them. *Assessment:* I believe ES, so
low prior, but the experiment is the same as for I1/I2.

**I21. Function-field analogue.** In 𝔽_q[t] replace positivity by degree/monic conditions and ask for N-torsion-free
solutions of 4/N = 1/X+1/Y+1/Z; there RH is known and "individual N" equidistribution has genuine power savings.
*Key lemma (needed):* the analogue for irreducible N, proved by Weil/Deligne bounds on the curve family of R3.
*Squares:* same Jacobi obstruction. *Six classes:* analogue = N a square modulo all small-degree irreducibles.
*Assessment:* the binary barrier is a *size* (log-many solutions) phenomenon, not an RH phenomenon, so I expect the
analogue to be either trivial (no positivity) or equally hard. Likely tried. Low.

**I22. Ternary forms / weight 3/2.** For c = 1: 4dp + 1 = (2dX−1)² − (2dY)² with X = a+b, Y = a−b. Summing over d is not
a single quadratic form, but for *fixed* small d the count is a restricted representation number of a binary form, and
Σ_d could be a Fourier–Jacobi/Siegel-type coefficient. *Key lemma (needed):* identify Σ_d with a coefficient of a
weight-3/2 or Jacobi form and bound the cusp part (Duke–Iwaniec). *Squares:* weight-3/2 coefficients naturally vanish or
jump at squares (unary theta functions!) — suggestive. *Six classes:* uniform. *Assessment:* suggestive but I have no
candidate form; likely tried. Low-mid.

**I23. Work over a ring with units, then descend.** Solve 4/π = 1/α+1/β+1/γ in ℤ[√p] (where p = π², π = √p) or in ℤ[i]
(p = ππ̄), use the infinite unit group / the absence of positivity, and descend by trace.
*Kill (PROVED):* averaging 1/(πα) over Galois gives 4/p = Σ y_i/(p y_i² − x_i²) for α_i = x_i + y_i√p; requiring each term to
be a unit fraction is y | x² and denominator p y − x²/y, which every integer has: the descent condition is the original
problem verbatim. *Squares / six classes:* n/a. *Assessment:* dead.

**I24. Lenstra's "divisors in residue classes".** For modulus m > N^{1/3} an integer N has ≤ 11 divisors ≡ r (mod m), all
found in polynomial time by a Euclid/lattice argument. In R3 (c = 1) N = 4dp+1, m = 4d: the regime d > √p/4 — which
carries half of the expected log²p solutions — is exactly Lenstra's regime, and his construction is the convergent
structure R6. *Key lemma (needed):* turn Lenstra's *finiteness* proof into an *existence* statement after summing over d
(the lattice attached to d varies with d by a unipotent shear, cf. I3). *Squares:* the sheared lattices never contain
the required vector by R5. *Six classes:* none. *Assessment:* gives an algorithmic handle (each d costs polylog time
without factoring) relevant to I8's bounded-arithmetic angle; as a proof route it is R6 again. Mid.

### 1.2 Top 5 and Phase-1 sanity checks (all numerics small; scripts `scripts/z69_ideab_*`, data `data/z69/ideab/`)

**Top 5 (chosen before looking anything up):** T1 = I1+I18 (profinite exceptional set / corridor closing),
T2 = I2+I20 (what is C ∩ ℤ?), T3 = I17 (R8: forms of discriminant −4dp, non-principal genus),
T4 = I7+I8 (unprovability: IOpen; Z-ring models; bounded-arithmetic witnessing), T5 = I5 (parity — as a cheap kill).

**S0. Reformulations verified** (`z69_ideab_sanity.py`, primes p ≡ 1 (4), p < 2200; `sanity_2200.txt`). CERTIFIED on that range:
every solution of 4/p is Type I or II; "some Type II solution" ⟺ "some K2 class contains p" (0 mismatches / 159 primes);
F1, F2, R8(d=1) each produce exact solutions (checked with rationals); the F2 count equals the count of length-3 minus
continued fractions [[a,4d,b]] with numerator p (R6). Zeros below 2200: F1 {193}; F2 {409, 577}; R8(d=1)
{13, 37, 97, 181, 193, 541, 673, 757, 1033, 1093, 1297, 1621, 1777}.

**S1 (T2). Which n ≡ 1 (4) have no identity-type solution?** (`z69_ideab_ctype.c`, exhaustive.)
Type II := ∃ a,b,c,d ≥ 1 with nc = 4abcd − a − b (no gcd condition); Type I := n in some class K3
(∃ a,d and f | 4a²d+1 with n ≡ −f mod 4ad). *Exhaustiveness (PROVED):* Type II: x = abd and e = (a+b)/c ≤ a+b ≤ ab+1 ≤ x+1
give n/4 < x ≤ (n+1)/3. Type I: a class (a,d,f) yields c = (n+f)/(4ad), e = (4a²d+1)/f, b = ce − a = (an+c)/f; the mirror
a ↔ b is again an I-1 class with f′ = (4b²d+1)/e, and for a ≤ b, ce = a+b ≤ 2b gives f = (an+c)/b ≤ n + 2 < 2n; primality
is not used. CERTIFIED (single run of the C program; re-verified for n ≤ 20000 by the internal reviewer's independent
naive enumeration, §4):
* 5 ≤ n ≤ 2·10⁵, all n ≡ 1 (4): Type II zeros = the 223 odd squares ∪ {4545}; Type I zeros = the 223 odd squares ∪
  {105, 2961, 3705}; **zeros of both = exactly the odd squares**.
* non-square n ≡ 1 (4) up to 8·10⁶: Type II zeros {4545} only; Type I zeros {105, 2961, 3705} only; none in common.
  (4545 = 3²·5·101, 105 = 3·5·7, 2961 = 3²·7·47, 3705 = 3·5·13·19.)
So on this range **C ∩ ℤ = {odd squares}**: with both types allowed, non-squareness alone (no primality) suffices —
EVIDENCE for the integer form of I1: *CONJECTURE IUC: a positive integer n ≡ 1 (mod 4) has a Type I or Type II
identity-type solution iff n is not a square.* The one-type exceptional sets look *finite* ({4545}; {105, 2961, 3705}).

**S2 (T1). Corridor test of the strong (profinite) UC** (`z69_ideab_corridor.py 11 100000 3000`): n ≡ 1 (840),
n ≡ r (11), n < 9.24·10⁸, least modulus of an identity class (K1∪K2∪K3) containing n.
r = 7, 8, 10: always 11 (one K2 class each). **r = 2, 6: the maximum least modulus keeps growing with the range**
(r = 2: 143, 351, 479, 611 over the first 10², 10³, 10⁴, 10⁵ values; r = 6: 127, 279, 599, 935), at the same rate as in the
control square class r = 1 (136, 359, 536, 1271); the witnesses used are other primes (23, 19, 39, 31, 47, …), not 11.
EVIDENCE that **strong UC is false**: the class {1 mod 840, 2 mod 11} contains no squares yet is not covered by
finitely many identities. This matches a compactness heuristic: uncovered sets at every finite level are non-empty and
nested, so C is a Cantor-like closed set strictly larger than S; a prime is excluded from C not because its *class*
dies but because *it* dies. Consequence for T1/I18: the "least non-residue gives a bounded-modulus identity" route is
dead; what survives is the integer statement IUC (S1), which is a different kind of claim.

**S3 (T3). R8 / class group** (`z69_ideab_forms.py 60000`): for 3018 primes p ≡ 1 (4) below 6·10⁴ the d = 1 slice
(forms [f,4a,e] of disc −4p with 4a | f+1) has on average 4.3 / 8.1 / 11.8 unordered solutions on [5,10³), [10³,10⁴), [10⁴,6·10⁴) *[corrected after review: the first script truncated the enumeration and reported 5.9 / 10.2 / 14.2; `forms_60000.txt` is the corrected run; the zero list was unaffected]* and
33 zeros (last 58321; 5 of them in the six classes); reduced good forms alone miss 269 primes. So the d = 1 slice
is a genuine log²-family with slowly thinning zeros; a proof along I17 must use several odd d (discriminants −4dp).

**S4 (T5). Parity** (`sanity_2200.txt`): over 159 primes, the parities of (total #solutions, #Type I, #Type II,
½#F2, ½#R8, p mod 8) populate all 32 combinations roughly evenly. EVIDENCE: no parity law for any natural count.
I5 is dead in its naive form.

**S5 (T4).** I7 is a pen-and-paper proof (see I7); nothing to compute. Its literature status is a Phase-2 item.

**Phase-1 verdict.** Dead on arrival: I4, I5, I9 (identity version), I10, I12, I13, I16, I23, strong UC of I1/I18.
Alive: IUC (S1), I17 (R8), I7/I8 (unprovability), I3/I24 (R6 lattice structure), I11 (as a frame), I15, I19, I22.

--- *End of Phase 1 (committed before any repo/literature lookup).* ---

## §2 Phase 2 — post-hoc lookup (repo `git grep`, FRONTIER §§2, 3, 6; three web searches)

Dictionary (learned only now): the campaign's **(★)** is my F2 / "c = 1 line" (R(n) = #{4uBC − u − B = n}; my Phase-1
zeros 409, 577 are the first two of its 14 prime zeros); its "b = 1 line / López Type A" is my F1 (zero 193 ✓.);
its uncovered set "U" is my C; its "profiles e_{ℓ,g}" are my α_{q,r}; "B2 / tied-modulus divisor event" is the common
endpoint of my I4, I11, I12, I16; CONV-II is the Type II half of my IUC.

| # | idea | status | pointers (repo unless stated) | what my Phase 1 adds, if anything |
|---|---|---|---|---|
| I1 | profinite exceptional set, UC | **TRIED — strong UC refuted (PROVED)** | `Z66_UCOVER.md` Thm T (U ⊋ (Ẑ^×)², same one-prime profiles), `Z65_LOGIC2.md` Thm D (finite unions of classes ⟺ NOI-provability), `EXPONENT_COVERING.md` | S2 is independent EVIDENCE for the case UCOVER (iv) leaves as CONJECTURE (K = {1 mod 840, (n/11) = −1} meets U): in classes r = 2, 6 mod 11 the least modulus grows like in the square class. Nothing else. |
| I2 | structure of C ∩ ℤ; IUC | **TRIED-OPEN** | FRONTIER §2 l.269 CONJECTURE CONV-II (odd non-square n ≠ 4545 has N_II ≥ 1; CERTIFIED n ≤ 10¹⁰), `Z58_WILDCARD.md` §1, `Z59_CONV2.md`, `Z58_STRUCT2.md` Thm 4.1 (4545 = integral Hasse failure, BM set non-empty); Type I zeros 105, 2961, 3705 already in `KUDLA_ES.md` l.57 (n ≤ 2·10⁴) | S1 reproduces 4545 independently (n ≡ 1 mod 4, ≤ 8·10⁶) and extends the Type I (K3) zero list {105, 2961, 3705} from 2·10⁴ to 8·10⁶ for n ≡ 1 (4) (single engine). IUC is implied by CONV-II + N_I(4545) > 0. |
| I3 | Hirzebruch–Jung / continuant / lens space / Dedekind sums | **TRIED-DEAD** | FRONTIER §2.1 "SL₂ form", l.1510 ("HJ grammars (trap at 193)"), `DEDEKIND_ES.md`, `BRAINSTORM/bsA_lens_homotopy_surgery.md`, `Z68_SIGN.md`, `ES_CONNECTIONS_TODO.md` | nothing |
| I4 | modular hyperbola + Weil | **TRIED-DEAD** | FRONTIER l.480, §6 l.1281 ("tied modulus; need p^{1−o(1)} saving"), §7 item 1, `Z53_HYPKLOOST.md`, `PARITY_AUDIT.md` §2 | nothing (same kill) |
| I5 | parity by involution | **TRIED-DEAD** | FRONTIER l.590 (M5), §6 l.1409 (finite affine menus barred, (J)2 Thm 6.1), `WINDMILL.md`, `WINDMILL_REDUCTION.md`, `INVOLUTION_ES.md`, `Z62_PARITY(F).md` | S4 agrees (no parity law) |
| I6 | Lambert / mock-theta generating function | **TRIED-DEAD** | FRONTIER §2.3 (exact theta-quotient normal form, `METAPLECTIC_ES.md` Thm K), §6 l.1287 ("Eisenstein-only, exact, does not decide one integer"), (I)5/(J)7 (no fixed-level identity, via T1) | nothing |
| I7 | IOpen ⊬ ES (Shepherdson) | **TRIED — superseded** | `Z64_UNPROV.md` Thms A, A′, A″ (normal open induction + GCD + irreducible divisors ⊬ ES at *primes* of any square class), `Z58_LOGIC.md` | my 6-line largest-root proof is a cheaper special case (composite n = 4t+1, plain IOpen); no new content |
| I8 | primes in Z-ring/Bézout models; S¹₂ witnessing | **TRIED; open only from IE₁ up** | `Z64_UNPROV.md` Prop 5.1 (exactly the Buss-witnessing statement), `Z65_LOGIC2.md`, `Z66_IE1.md` (IOpen + Lagrange upward: arc method dead; IE₁/IΔ₀ OPEN) | nothing |
| I9 | identities over norm forms X² + DY² | **TRIED-DEAD** | `BRAINSTORM/ident_form_families` (O145b), `BRAINSTORM/s7_normform_collapse.md`, `POINTWISE_BINARYFORM` §6 (0 two-variable Type I families for u²+v²), `CLASS_FORCING.md` (governing fields) | my degree-count no-go is a re-derivation |
| I10 | Pell / norm −1 unit | **TRIED-DEAD** | `BRAINSTORM/z5_pell_unit_T1.md` ("the real unit is positivity-blind"), FRONTIER l.524, l.608, l.1537 | nothing |
| I11 | consecutive integers x+j ∈ B_{4j+3} | **TRIED-DEAD** | FRONTIER l.1510 ("consecutive blocks"), `SYNTHESIS_SPARKS4.md` l.85 (the (log n)^{−1/2} lottery), §3 B2 | nothing |
| I12 | CRT-forced smooth shifts; S-unit pairs | **TRIED-DEAD** | FRONTIER §6 l.1288 (CRT architectures capped), `BREADTH_Z45.md` §15, `Z53_HCHYP.md` (Erdős–Hall) | nothing |
| I13 | largest denominator first; induction | **TRIED-DEAD** | FRONTIER l.530 ("no Vieta-type involution") | nothing |
| I14 | Cayley cubic, Brauer–Manin | **TRIED-DEAD** | FRONTIER §2.2 (BM main term, PROVED), l.649 & `Z58_STRUCT2.md` (4545: BM set non-empty, no point — BM is *not* the only obstruction) | nothing |
| I15 | genus theory / Rédei for Δ = 4c²dp+1 | **TRIED-DEAD** | `Z53_GENUSREDEI.md`, `CLASS_FORCING.md`, FRONTIER l.506, l.964 ("class, not parity"), §6 l.1397 | nothing |
| I16 | divisor sums with tied modulus | **TRIED-DEAD** | FRONTIER §2.1 trial form, §6 l.1281, `PARITY_AUDIT.md` §2 | nothing |
| I17 | forms of disc −4dp, non-principal genus, Heegner points | **TRIED-DEAD** | `WINDMILL.md` l.432–472, `Z53_FORESTCLASS.md` (SMN: non-principal genus of −4p fails at 48 primes), `BRAINSTORM/z31_quadratic_forms.md`, `BRAINSTORM/z31_duke_equidistribution.md`, FRONTIER §6 l.1280 (Heegner small-scale equidistribution → scale constraint B3) | S3's census of the d = 1 slice (33 zeros < 6·10⁴) is consistent; nothing new |
| I18 | stratify by least non-residue; pseudosquares | **TRIED-DEAD** | `Z66_UCOVER.md` (iii)–(iv), `Z60_MS105.md`, FRONTIER l.1537 | S2 (see I1) |
| I19 | Poisson / extreme-value calibration | **TRIED (done)** | FRONTIER §2 l.200, l.359, §6 l.1284 ("far tail fatter than Poisson") | nothing |
| I20 | disproof via higher reciprocity | **TRIED-OPEN (nothing found)** | `Z58_DISPROOF` lane, `Z58_STRUCT2.md`, FRONTIER §6 l.1397 | nothing |
| I21 | function-field analogue | **TRIED** | `Z58_FFIELD.md`, FRONTIER l.671, l.1184 (a mute place makes the F_q[T] variant a theorem — the analogy does not transfer) | nothing |
| I22 | ternary / weight 3/2 | **TRIED-DEAD** | `Z58_TERNARY` (lane), `THREE_SQUARES.md`, FRONTIER l.413, l.444 | nothing |
| I23 | rings with units, descend by trace | **TRIED-DEAD** | `BRAINSTORM/z5_pell_unit_T1.md`, FRONTIER l.608 | nothing |
| I24 | Lenstra divisors in residue classes | **TRIED-DEAD** | `Z53_LATTICE.md`, FRONTIER l.1604 ("Lenstra/CHN/Shiu per-fibre bounds remove only n^{o(1)}") | nothing |

**Literature (web, 2026-11-09, three bounded searches):** nothing on ES in open induction outside the repo's own sources;
López, arXiv:2404.01508 ("A complete congruence system for the Erdős–Straus conjecture", Type A/B) is the published form
of F1 and is already the campaign's "b = 1 line"; no published statement of CONV-II / 4545 found. The repo's own
literature files (`LITERATURE_2026.md`, `Z58_LIT.md`) are far more complete than these searches.

*Legend.* TRIED-DEAD = explored in the repo and abandoned there (a specified menu failed, or a scoped barrier applies); it is
not a claim that a universal no-go theorem exists. TRIED-OPEN = explored, target still open.

**Phase-2 verdict (blunt).** 24 / 24 ideas (25 / 25 with the late I25) were already explored in the campaign; **I identified no NEW approach**. Independent ideation
re-derived the campaign's map — the (★)/F1 lines, T1 via reciprocity, the profinite set U and its one-prime profiles,
CONV-II and 4545, the open-induction unprovability, the class-group and HJ encodings, and the same kills — and arrived
at the same endpoint (one tied divisor event with polylog expected witnesses). The only items I could not find in
the repo are data footnotes: the Type I zero list to 8·10⁶ (I2) and the least-modulus growth in the classes 2, 6 mod 11 (I1)
(topic-level matching by `git grep`; I did not check that every derivation of §1 occurs verbatim).
That an unprimed pass lands on the same barrier, with the same exceptional integers, is itself (weak) EVIDENCE that the
campaign's map of *elementary* approaches is saturated.

**Late idea (after the Phase-1 commit, before its lookup): I25. Schur–Murty "Euclidean" forcing.** A Euclid-style
forcing of a prime divisor in a class a mod q exists iff a² ≡ 1 (mod q) (Schur 1912, Murty 1988); the tied class −1
always qualifies. On the ±1-subgroup "class = parity": if e ≡ 3 (4) is prime and a prime ℓ | (p+e)/4 has ℓ ≡ ±1 (mod e),
then ℓ ≡ (p/ℓ) (mod e) (R5). *Kill found by myself:* forcing needs the whole number ≡ −1, and then the whole number is
already a witness; when N ≡ +1 (the ES situation) nothing is forced. **Lookup: TRIED-DEAD** —
`BRAINSTORM/y3_euclid_schur_forcing.md` ("the ES class −1 is a Schur–Murty Euclidean class"), `DETERMINISTIC_EXISTENCE.md`.
So 25 / 25.

## §3 Phase 3 — the best TRIED-OPEN item with a twist: O2 of `Z66_UCOVER.md` from the integer side

**Choice (Assessment).** No idea is NEW. Of the TRIED-OPEN ones, CONV-II/IUC (I2) has no mechanism and a 10¹⁰ census
already; IE₁/IΔ₀ (I8) is out of reach in a lane; O1 of UCOVER (explicit ℓ₀) needs an explicit P_II(n) ≤ Cn^θ, θ < 1/2
(I checked: with max-divisor bounds the tail only closes from level k ≈ 10⁴ — hopeless for ℓ = 17). That leaves
**O2: does K = {n ≡ 1 (840), (n/11) = −1} meet U** (U = profinite units in no ET Prop 1.9 family class)? UCOVER has
profile evidence (two-prime profiles at 11, 13 surviving over (g,h) ≡ (2,2)); it is a CONJECTURE there. My Phase-1 S2 saw
the same phenomenon from the other side: among *integers* of the classes r = 2, 6 mod 11 the least identity modulus
keeps growing. Twist: make that integer-side statement exact and push the computation with all seven families.

**Pre-registered (before running anything in this section).**
* *Lemma E to prove:* K_r ∩ U ≠ ∅ ⟺ the least family-class modulus is unbounded over the primes of
  K_r := {1 mod 840, r mod 11}.
* *Computation:* for all primes p ≤ 10¹² in K_2, K_6 and in the control class K_1 = {1 mod 9240} (a square class):
  λ(p) := least modulus of an ET family class (I-1, I-2, I-3, I-4, II-1, II-2, II-3) containing p, moduli ≤ 10⁴.
* *Kill test A (against the conjecture):* if the running maximum of λ over K_2 or K_6 is constant over the last three
  decades of p while the control's keeps growing, O2 is probably *false* for that class; then try to exhibit the finite cover.
* *Kill test B (implementation):* λ(p) from the class table must equal λ computed from an independent brute-force
  enumeration of actual solutions on a sample; any mismatch voids the data.
* *What would be a result:* CERTIFIED finite-level statements "no set of family classes of modulus ≤ M covers the primes
  of K_r" for explicit M, plus a growth comparison with the control. *What would not:* any claim about ES itself.

### 3.1 Lemma E (PROVED; immediate from `Z65_LOGIC2.md` Thm D's compactness step + Dirichlet)
For a prime p let **λ_ET(p)** be the least modulus of an ET Prop 1.9 family class containing p (finite whenever p has a
Type I/II solution). The scripts compute **λ(p) ≤ λ_ET(p)**, the least modulus over a *superset* 𝔉⁺ of the family classes
(same seven parametrisations, without ET's coprimality side conditions; every class of 𝔉⁺ is still a valid polynomial
identity class). Every "λ(p) > M" below therefore implies λ_ET(p) > M; statements of the form "λ(p) ≤ M" are about 𝔉⁺.
Lemma E is stated for λ_ET and holds verbatim for λ (its proof only uses that there are finitely many classes per modulus). For a primitive class r mod q put K_{r,q} = (r + qẐ) ∩ Ẑ^×. Then
**K_{r,q} ∩ U = ∅ ⟺ sup{λ_ET(p) : p prime, p ≡ r (mod q)} < ∞** (sup over all but finitely many primes).
More precisely, fix one collection 𝔉 of classes with finitely many per modulus (ET's family classes with λ_ET, or 𝔉⁺ with λ)
and write λ_𝔉. For every M: *some unit residue class inside r mod q is missed by all 𝔉-classes of modulus ≤ M*
⟺ *some prime p > M, p ≡ r (q), has λ_𝔉(p) > M* ⟺ *infinitely many such primes exist*.
*Proof.* There are finitely many family classes of modulus ≤ M; let L be the lcm of q and their moduli. A family
class of modulus m | L either contains or is disjoint from a given residue class mod L. (⇐) If p > M has λ(p) > M then
p ∤ L, so p mod L is a unit class missed by all of them. (⇒) A missed unit class mod L contains infinitely many primes
(Dirichlet), each with λ > M. For the first equivalence: if K ∩ U = ∅, compactness gives a finite cover, say with
moduli ≤ M, and then no unit class is missed at level M; if π ∈ K ∩ U then for every M the class π mod L is missed. ∎
*Corollary (finite-level certificate).* One prime p ≡ r (q) with p > M₀ := λ(p) — or, more generally, one integer n ≡ r (q),
coprime to every prime ≤ M, lying in no 𝔉⁺-class of modulus ≤ M — certifies: **every finite set of ET family classes covering
the large primes of r mod q contains a modulus ≥ M₀ (resp. > M).** (The class of p, resp. n, modulo the lcm is a missed unit
class and contains infinitely many primes; 𝔉⁺ ⊇ ET's classes on unit residues ≡ 1 mod 4.)

### 3.2 Computation (CERTIFIED for the stated ranges; `scripts/z69_ideab_o2.py 1e12 10000 r…`, logs `o2_run_*.log`)
All primes p ≤ 10¹² in K_2, K_6 (n ≡ 1 mod 840, n ≡ 2 resp. 6 mod 11) and in the square-class control K_1 = {1 mod 9240};
family classes of all seven ET families with modulus ≤ 10⁴ (5000 moduli; the enumeration is a superset of ET's — no
coprimality side conditions — so "λ > M" here implies the same for ET's families). No prime is unresolved.

| class | #primes ≤ 10¹² | mean λ | max λ for p ≤ 10⁶, 10⁷, …, 10¹² | record prime |
|---|---|---|---|---|
| K_2 | 19 585 244 | 39.3 | 159, 239, 359, 519, 823, 1319, **1979** | 593 042 652 721 |
| K_6 | 19 584 884 | 39.2 | 99, 279, 428, 539, 791, 1056, **1247** | 928 241 301 961 |
| K_1 (control) | 19 585 148 | 40.3 | 79, 244, 279, 584, 1007, 1623, **2020** | 535 842 079 081 |

Tail counts #{p ≤ 10¹² : λ(p) > M}:

| M | 70 | 100 | 200 | 300 | 500 | 700 | 1000 | 1500 | 2000 |
|---|---|---|---|---|---|---|---|---|---|
| K_2 | 2 519 649 | 726 463 | 63 532 | 17 975 | 2 336 | 371 | 19 | 1 | 0 |
| K_6 | 2 519 771 | 727 483 | 63 892 | 17 854 | 1 254 | 174 | 17 | 0 | 0 |
| K_1 | 2 517 189 | 1 088 777 | 113 582 | 31 815 | 5 756 | 1 198 | 207 | 18 | 1 |

The most frequent least moduli are the same in all three classes (23, 19, 39, 31, 47, 59, 71, 43 — witnesses at *other*
primes); up to M = 70 the three tails agree to 0.1 %; beyond, the classes with 11 | modulus thin the K_2, K_6 tails by a
growing factor (≈ 1.5 at M = 100, ≈ 10 at M = 1000) but the tails do not stop.

**Kill test A (pre-registered): not triggered.** The running maximum of λ grew in each of the last three decades in
both classes (K_2: 823 → 1319 → 1979; K_6: 791 → 1056 → 1247), roughly ×1.2–1.6 per decade like the control.
**Kill test B (pre-registered): passed.** `scripts/z69_ideab_o2_check.py` recomputes λ by direct divisibility tests
on the defining conditions (no residue table, no CRT, no inverses) for all 75 record-setting primes of the three
classes and 300 random primes < 3·10⁸: 375 / 375 agree (`o2_check.log`; an earlier run at moduli ≤ 1100: 500 / 500).
Sanity on the campaign screens (table to modulus 3000): no class contains an odd square m², m < 200; all 14 (★)-zero
primes have λ ≤ 239 (e.g. λ(409) = λ(577) = 7, λ(8 813 281) = 111, λ(1 726 201) = 239), all 38 𝔊*-zero primes
λ ≤ 239, the twelve R₈-zero primes λ ≤ 248, and all 285 composite (★)-zeros lie in some class of modulus ≤ 548.

### 3.3 What this gives
* **CERTIFIED (via the Corollary).** Any finite set of ET family classes covering the large primes of K_2 contains a
  modulus ≥ 1979 (witness p = 593 042 652 721); for K_6, ≥ 1247 (witness p = 928 241 301 961). In the language of
  Thm D: the finite identity cover that Thm D extracts from an IOpen/NOI proof of "ES at all large primes of K_r" would
  contain a modulus at least that large (a statement about covers, not about the syntax of proofs). (Single engine for the full range; the witnesses themselves are double-checked by the
  independent direct test, which is all the Corollary needs.)
* **EVIDENCE for UCOVER O2** (K ∩ U ≠ ∅), of a kind independent of UCOVER's profile computations: on the integer
  side, K_2 and K_6 are indistinguishable from the square class up to a slowly growing constant factor; nothing
  suggests a finite cover. New relative to UCOVER (iv): the same holds for **r = 6**, where the two-prime (11, 13)
  profiles of UCOVER all die — so if K_6 ∩ U ≠ ∅ (CONJECTURE), its points are not (11, 13)-profiles.
* **Not obtained.** A proof of O2. By Lemma E it is equivalent to "λ is unbounded on the primes of K_r", and every
  route I see to unboundedness is again a covering-measure bound on a thin profile set, i.e. UCOVER's Theorem T with
  explicit constants (their O1), which I estimate closes only from ℓ-adic level ≈ 10⁴ with max-divisor bounds.
* **No bearing on ES itself.** Lemma E and the data are statements about what *finite identity covers* (equivalently
  open-induction proofs) can do; they neither prove nor threaten positivity at any prime.

### 3.4 Constructive certificates: "square away from 11" residues (plan, pre-registered)
*Observation (PROVED, from T1 = ET Prop 1.6).* The residue of a family class is never a unit square modulo its modulus.
Hence a unit residue π mod L that is a square modulo every prime power of L prime to 11, with π ≡ r (mod 11), r ∈ {2, 6},
can only lie in family classes whose modulus is divisible by 11. So to build a unit class of K_r missed by all family
classes of modulus ≤ M it suffices to choose, prime by prime (ℓ ≠ 11), a *square* residue mod ℓ^{v} that dodges the
(few) classes with 11 | modulus and largest other prime ℓ; these have modulus ≥ 11ℓ, so only primes ℓ ≤ M/11 carry
constraints. This generalises UCOVER's "1 away from ℓ" profiles to "any square away from 11".
*Plan.* Backtracking search (`scripts/z69_ideab_cert.py`) for M = 10⁴ and beyond; the output residue n mod lcm is then
verified (i) against the full class table of all seven families and all moduli ≤ M, without using the observation, and
(ii) by the independent direct test of §3.2. By Lemma E each success is a CERTIFIED statement "every finite family-class
cover of the large primes of K_r contains a modulus > M".
*Kill test C (pre-registered):* if the search dead-ends for some M ≤ 10⁴ after exhaustive backtracking over the primes
≤ 100, the square-away-from-11 profiles are all caught at that level — evidence that K_r ∩ U, if non-empty, needs
non-square coordinates elsewhere (as UCOVER's (2,2)-profiles at 11, 13 suggest for r = 2).
*[Review note: as implemented the search is bounded (≤ 40 candidates per prime, ≤ 2·10⁵ backtracks), so a failure would
have been UNDECIDED, not a kill. It did not occur.]*

**3.4 results (CERTIFIED).** `z69_ideab_cert.py M r 1`:
| M | r | relevant classes (11 ∣ modulus, compatible) | backtracks | least allowed fraction at a prime | violations against all classes ≤ M |
|---|---|---|---|---|---|
| 3000 | 2 | 151 of 37 263 | 0 | 0.40 (ℓ = 31) | 0 |
| 10⁴ | 2 | 651 of 173 664 | 167 | 0 on some branches (ℓ = 3) | 0 |
| 10⁴ | 6 | 650 of 173 664 | 0 | 0.11 (ℓ = 3) | 0 |

So (Lemma E) **every finite family-class cover of the large primes of K_2, or of K_6, contains a modulus > 10⁴**
(certificates: `data/z69/ideab/cert_M10000_r{2,6}.json`, a 4349-digit residue each, checked against all 173 664 classes
of all seven families without using the squares observation, and again by the direct divisibility test with no table:
`cert_M10000_direct.log`; the internal reviewer re-verified both with independent code). Kill test C not triggered. The only tight spot is the
prime 3 (3-adic digits to depth 8), i.e. the constraints live on the deep digits at the *small* primes. This suggests looking at small primes first:

**Question (Q-S).** Let S = {2,3,5,7,11} and B_r = (1+8ℤ₂)×(1+3ℤ₃)×(1+5ℤ₅)×(1+7ℤ₇)×(r+11ℤ₁₁). Do the family
classes with S-smooth modulus cover B_r?
* If **yes**: by compactness finitely many do, and then K_r ∩ U = ∅ — the unit profiles of K_r would lie in a finite
  union of polynomial-identity classes (a new Mordell-type class; O2 answered negatively for that r).
* If **no**: some S-point survives all S-smooth classes. This is *necessary* for K_r ∩ U ≠ ∅ but, as §3.6 shows, far from
  sufficient: the next prime removes most of what is left. *[Corrected by my own follow-up after the review: the first
  version said the other primes "were easy"; that was wrong.]*
Smooth moduli are sparse (7 838 below 10⁸), so the *truncation* of (Q-S) to moduli ≤ M can be decided far beyond 10⁴.
(A "covered" answer at some level would settle (Q-S); "not covered" at a level settles only that level.)

### 3.5 Question (Q-S): the five-prime core of O2 (`scripts/z69_ideab_smooth.py`)
All family classes (seven families, superset enumeration) with **S-smooth modulus ≤ M**, S = {2,3,5,7,11}; those
compatible with B_r; relative weight of a class = its Haar measure inside B_r. "Uncovered" = Haar measure of the part
of B_r in none of them, computed **exactly** (rational number, digit-tree recursion; `--exact`) up to M = 10⁷ and by Monte Carlo
(2·10⁵ points, standard error ≈ 0.0005 for r = 2 and ≈ 0.0003 for r = 6; agrees with the exact values to 3 decimals where
both exist) at 10⁸. The exact values at 10⁵–10⁷ are single-engine; the 10⁴ value 4071/42350 was recomputed by the internal
reviewer with an independent method (CRT inclusion–exclusion).

| M | smooth moduli | classes | compatible, r = 2 / 6 | total weight, r = 2 / 6 | uncovered measure, r = 2 | uncovered measure, r = 6 |
|---|---|---|---|---|---|---|
| 10⁴ | 522 | 15 325 | 49 / 54 | 4.873 / 4.665 | 4071/42350 = 0.096128 (exact) | 0.049318 (exact) |
| 10⁵ | 1 197 | 79 936 | 220 / 234 | 7.902 / 7.639 | 0.061468 (exact) | 0.019823 (exact) |
| 10⁶ | 2 432 | 332 051 | 772 / 811 | 9.118 / 8.897 | 0.050738 (exact) | 0.015685 (exact) |
| 10⁷ | 4 520 | 1 166 099 | 2 315 / 2 397 | 9.571 / 9.371 | 0.048518 (exact; MC 0.0484) | 0.013465 (exact; MC 0.0135) |
| 10⁸ | 7 838 | 3 580 758 | 6 048 / 6 181 | 9.719 / 9.525 | 0.0487 (MC) | 0.0133 (MC) |

At every level an explicit surviving cylinder is produced by a complete digit DFS and re-checked (e.g. M = 10⁸, r = 2:
x ≡ 113 (2⁹), 55 (3⁴), 161 (5⁴), 155 (7⁴), 959 (11³) meets no S-smooth class of modulus ≤ 10⁸; `smooth_M1e+08_r*.json`).
Sanity built into the run: the number of compatible classes with 11 ∤ modulus is 0 at every level, as T1 demands.

**Reading.**
* **PROVED (qualitative):** the total weight W_r(∞) of all compatible S-smooth classes is finite: a modulus m carries
  O_ε(m^ε) classes, each of weight ≤ 9240/m, and Σ_{m S-smooth} m^{−1+ε} = Π_{q∈S}(1 − q^{−1+ε})^{−1} < ∞. (This is what
  distinguishes the five-prime problem from the full one, whose weight diverges like a power of log M.)
* **CERTIFIED:** (Q-S) has answer "not covered" at every level M ≤ 10⁸, for r = 2 and r = 6, with uncovered measure
  exactly 0.048518… resp. 0.013465… at M = 10⁷ (rationals in `smooth_exact_1e7_r*.log`).
* **EVIDENCE:** the weight increments per decade are 3.03, 1.22, 0.45, 0.15 (ratio ≈ 0.35), so the weight beyond 10⁸
  is ≈ 0.08 and beyond 10⁹ ≈ 0.03, while the uncovered measure has stopped moving at ≈ 0.048 (r = 2) and ≈ 0.013
  (r = 6): the uncovered set of B_r under *all* S-smooth classes very probably has positive measure.
* **CONDITIONAL (union bound):** if W_r(∞) − W_r(M) < u_r(M) for one M (u_r = uncovered measure at level M), then
  B_r is not covered by S-smooth classes. For r = 2 the extrapolated crossing is at M ≈ 10⁹. Assessment (back-of-envelope
  only; no family-by-family derivation is archived): a *rigorous* tail bound from max-divisor inequalities
  (τ₃(n) ≤ 1.77·10⁴ n^{1/4}, τ(n) ≤ 8.45 n^{1/4}; the suprema are 17653.1… and 8.4469…, computed) would close the II-2
  family only beyond ≈ 10¹⁸ and the II-1/I-4/I-1 families beyond ≈ 10²², and exact enumeration that far would be a
  finite but multi-day computation; not attempted here. Finite total weight (> 1) alone does not give a surviving point.
* **What (Q-S) = "not covered" would and would not give.** It does *not* prove O2: a surviving S-point must still be
  extended over the primes ≥ 13, where the total weight diverges (heuristically like a power of log M; Assessment) so no union bound is available;
  a level-by-level (e.g. second-moment) argument is the route I would try. The extension is *not* automatic: see §3.6. It *does* explain the shape of the survivors: they are
  **generic squares at 3, 5, 7** (e.g. x ≡ 13 mod 27, 21 mod 25, 15 mod 49), not UCOVER's "1 away from 11, 13"
  profiles, which are caught early because the small residues −e, −f of the families cluster at ±1.
* Had the truncated (Q-S) come out "covered" at some level, the unit profiles of K_r would have been inside a finite
  union of identity classes — a new Mordell-type class. It did not, up to 10⁸. **(Q-S) itself, and O2, remain OPEN.**


### 3.6 The next stage (prime 13): the five-prime box is only the first level of a tree (added after the review)
`z69_ideab_smooth.py M r … --exact --extra 13:v` adds 13 to S and restricts the coordinate at 13 to v + 13ℤ₁₃
(any unit v; for non-residues v the classes with 11 ∤ modulus are kept). Logs `smooth13_*.log`. CERTIFIED (exact
rationals; single engine) unless marked MC.

| r | residues v mod 13 with B_r × (v + 13ℤ₁₃) **entirely covered** at level 10⁵ | surviving v: exact uncovered measure of the sub-box at 10⁴, 10⁵, 10⁶; MC at 10⁷ |
|---|---|---|
| 2 | 1, 4, 9 (single classes mod 143), 10 (mod 5720), 12 (mod 4004), 5, 6, 8, 11 | v = 3: 0.038451, 0.023898, 0.014690, 0.0116 (MC) · v = 2: 0.012310, 0.006801 · v = 7: 0.022800, 0.005012 |
| 6 | 1, 3, 10 (mod 143), 2 (mod 572), 12 (mod 4004), 5, 6, 8, 11 (mod 39, 52, …), 9 (jointly, no single class) | v = 4: –, 0.017897, –, 0.0099 (MC) · v = 7: –, 0.004427 |

* So at 13 only three (r = 2) resp. two (r = 6) of the twelve residue classes survive, exactly one of them a square
  class (v = 3 resp. v = 4). The S-survivor cylinder of §3.5 at level 10⁸ (113 mod 2⁹, 55 mod 3⁴, 161 mod 5⁴, 155 mod 7⁴,
  959 mod 11³) does **not** extend to any square residue at 13, in any lift: v = 1, 4, 9, 10, 12 are dead for every
  point of B_2, and the whole cylinder × (3 + 13ℤ₁₃) lies in the single II-2 class n ≡ 640 (mod 1287 = 3²·11·13)
  (a = 7, d = 23: 4ad = 644 | 1288, −4a²d ≡ 640; found by the round-2 reviewer; `z69_ideab_cert.py` with the preset
  had only shown that one lift fails).
  The certificates of §3.4 are unaffected (they were found by a search over all coordinates and verified against the
  full table); their residues mod 13 are 3 (r = 2) and 4 (r = 6) — exactly the unique surviving square classes, a
  consistency check between the two independent programs.
* At the stage {2,…,13} the finite-level uncovered measures *suggest* convergence to a positive value (r = 2, v = 3:
  decrements 0.0146, 0.0092, 0.0031 per decade; extrapolation ≈ 0.010–0.011 of the sub-box — EVIDENCE, the last point
  is Monte Carlo, and no tail bound exists), ≈ 4–5 times smaller than at the stage {2,…,11} (0.0485) *within one of
  twelve residue classes*. What is PROVED: for every finite prime set S′ ∋ 11 the S′-smooth classes have finite total
  weight (as in §3.5); and U has Haar measure 0 in Ẑ^× (for each prime q ≡ 3 (4) the II-2 class n ≡ −4 mod q, a = d = 1,
  is a family class; these are independent events of probability 1/(q−1) with divergent sum — remark of the round-2
  reviewer), so the all-modulus survivor measures of an exhausting sequence of prime sets tend to 0. What is *not*
  proved: that any stage has positive all-modulus measure, or is non-empty. **O2 asks whether the nested closed survivor
  sets (all moduli, S′ ↑ all primes) have non-empty intersection, i.e. whether all of them are non-empty.** (Q-S) is
  the first member of that sequence, not a "core"; the picture "Cantor-like set, thinning level by level" is a
  heuristic reading of the finite data.
* Explicit witnesses for the full-cover entries (parameters found independently by the round-2 reviewer; each modulus
  divides 120120, so each class contains the whole box): r = 2: v = 1 ↔ (143, 79) II-2 a=4, d=1; v = 4 ↔ (143, 134)
  II-2 a=9, d=4; v = 9 ↔ (143, 35) II-2 a=3, d=3; v = 10 ↔ (5720, 2961) II-3 a=26, d=1, e=55; v = 12 ↔ (4004, 2521) I-1
  a=91, d=11, f=13495. r = 6: v = 1 ↔ (143, 105) II-2 a=9, d=1; v = 5 ↔ (39, 31) II-2 a=1, d=2; v = 9: the three classes
  (396, 61), (99, 94), (1287, 919) cover the box jointly.
* Relation to UCOVER (iv): there, among profiles (g at 11, h at 13, **1 elsewhere**) only (g,h) ≡ (2,2) survives the cited
  finite-level profile computations. Without
  the "1 elsewhere" restriction the surviving residues mod 13 are {2, 3, 7} for r = 2 and {4, 7} for r = 6 (new data;
  finite level 10⁵; six-prime smooth moduli only — nothing is claimed about extending these survivors over the primes
  ≥ 17). In particular r = 6 has finite-level survivors, with generic squares at 3, 5, 7 — no contradiction with UCOVER,
  whose r = 6 profiles are "1 elsewhere", and consistent with the M = 10⁴ certificate for K_6.

## §4 Review log

**Internal hostile review** (deep-mode subagent, 2026-11-09; full report `data/z69/ideab/internal_review.md`; no provider /
auth / quota error). Verdict: "REJECT AS WRITTEN; no fatal defect found in the central finite-cover certificates."
18 findings; all addressed (two of the fixes — I1 and I11 — were themselves incomplete and were redone after round 2):
* **MAJOR, fixed.** (1) R7 wrongly required u, u* ∈ [1,p) — now integer lifts. (2) R8's Type I half conflated ideal and
  element factors — now "ideal factor", with the reviewer's counterexample. (4) C was defined inside Ẑ^× although primes and
  squares are not units of Ẑ — C now lives in Ẑ; R_α irreducibility restricted to unit α. (7) `z69_ideab_forms.py`
  truncated the d = 1 enumeration — script fixed, means corrected (4.3 / 8.1 / 11.8 unordered; zero list unchanged).
  (13) the optional direct-check path of `z69_ideab_cert.py` was broken — fixed (`direct_lambda` importable), run, and
  archived (`cert_M10000_direct.log`: no class up to 10⁴ for either certificate). (17) I11 ("squares mod e" → kernel of
  the Jacobi character) and I15 (false local-norm gloss removed).
* **MINOR, fixed.** (3) I9/I10 scope wording. (6) stale `ctype_20000.txt` (produced by the first, too loose Type I
  predicate) deleted. (8) legend for TRIED-DEAD; "no NEW approach identified" instead of "nothing is new". (9) Lemma E:
  collection of classes kept fixed, size hypothesis p > M₀ stated, proof-theoretic wording qualified. (15) tail
  thresholds relabelled Assessment, Monte Carlo errors stated. (16) kill test C is bounded-search (UNDECIDED on failure);
  `z69_ideab_smooth.py` now re-checks survivors against the raw table and asserts the T1 sanity count is 0. (18) text
  slips (number of smooth moduli, "finite union" wording, "(Q-S) decided at finite level").
* **Self-correction after the review (not prompted by it).** While wiring the S-survivor into the certificate search I
  found that it does not extend to the prime 13; the "five-prime core / other primes are easy" reading of §3.4–3.5 was
  wrong. §3.6 was added, the two affected bullets and the summary (iii) were rewritten, and `z69_ideab_smooth.py` /
  `z69_ideab_cert.py` gained the `--extra q:v` and preset options. The §3.6 numbers are single-engine.
* **Confirmed independently by the reviewer (OK):** exhaustiveness of the S1 searches and the zero sets for n ≤ 20000;
  the superset property of `build` on unit classes ≡ 1 mod 4; λ = 1979, 1247, 2020 for the three record primes and their
  primality; the sieve against `sympy.primerange` for X = 10⁶; both M = 10⁴ certificates (own code, plus per-modulus
  divisibility tests at 136 moduli); the smooth enumeration at 10⁴ (equals the restriction of the full table), the exact
  measure 4071/42350 by CRT inclusion–exclusion, and the stored M = 10⁶, r = 2 survivor against all 332 051 raw classes;
  the two divisor-bound suprema.
* **Not independently reproduced:** the full λ census to 10¹² (single engine; only the record primes and 375 + 84 sample
  primes are double-checked), the exact uncovered measures at 10⁵–10⁷, and the S1 census beyond 20000.

**Round 2** (focused deep-mode subagent on the post-review changes; report `data/z69/ideab/internal_review_round2.md`; no
provider error). Verdict: "REJECT THE REVISED MEMO AS WRITTEN; no FATAL defect found in the requested finite
computations." 16 findings; applied:
* **MAJOR, fixed.** (2) I1 still wrong after the first fix (C ⊉ all squares of Ẑ; primes dense only in Ẑ^×) — rewritten in
  terms of unit profiles. (3) I11 needed the coprimality hypothesis. (11, 16) the §3.6 / summary wording "converges to a
  positive value", "Cantor set", "as a measure-zero set must" overclaimed — now finite-level EVIDENCE only, with the
  reviewer's short proof that U has measure 0 and an explicit statement of what is not proved.
* **MINOR, fixed.** (4) I15 discriminant sentence scoped to c = 1. (6) summary uses λ_ET. (7) diagnostic text of
  `z69_ideab_smooth.py` for `--extra`. (10) the mangled `smooth13_1e5_r2.log` replaced by an intact rerun. (12) UCOVER
  comparison hedged. (14) preset option documented as one-lift; `z69_ideab_cert.py` refuses to write a certificate with
  violations. (15) the one-lift statement replaced by the reviewer's stronger exact obstruction (class 640 mod 1287).
* **Confirmed independently in round 2 (OK):** R7/R8 as corrected; S1 inequality f ≤ n+2; the corrected S3 means; Lemma E
  and Corollary; the six-prime enumeration at 10⁴ against the unrestricted table; the seven full-cover classes with explicit
  parameters; the exact measure 4071/105875 (r = 2, v = 3, M = 10⁴) by CRT inclusion–exclusion; 469147/19631040 at 10⁵
  by a fresh run; r = 6, v = 9 jointly covered; `cert.py 3000 2 1 3000` → 0 violations, direct test 3001.

**Open after this lane.** ES; UCOVER O2 (K ∩ U ≠ ∅); (Q-S) for r = 2, 6 beyond the truncation 10⁸. A cross-model review
is owed by the wave protocol. Not merged; waiting.
