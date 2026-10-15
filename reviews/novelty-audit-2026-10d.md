# Novelty audit 2026-10d (task O223): wave Y, DISCOVERIES (J)39–(J)55

**Auditor:** side agent O223 (branch `side-agent/novelty-audit-d`). Priority audit
only; correctness is taken from the cited internal reviews.

**Search method.** Jina web search + Jina reader, arXiv abstract/full-text pages, zbMATH
Open API. Tags as in 10c: **[visited]** = page/PDF read in this pass; **[snippet]** =
search-result snippet only; **[memory]** = auditor recollection (weak). "Apparently
new" = not found in what was searched; it is not a priority certificate.

Archive of this pass: `sources/lit2026d/`.

(work in progress — sections filled in below, one target at a time)

---

## 1. Friezes, the Farey pentagon, Jacobi symbols ((J)40, (J)42, (J)45)

### 1.1 Findings (verified)

* **Morier-Genoud, "Counting Coxeter's friezes over a finite field via moduli
  spaces", arXiv:1907.12790v2** (Algebraic Combinatorics 2021 [memory for the journal
  data]) [visited; archived `sources/lit2026d/arxiv-1907.12790-morier-genoud.{pdf,txt}`].
  * Thm 1 (p. 2): the number of tame friezes of width w over F_q is an explicit
    polynomial in q; for width 2 it is 1 + q² (§3.5, p. 12).
  * **§3.5 (p. 12): "For q = 2 the five friezes … are defined by the coefficients
    (1, 1, 1, 0, 0) on the first row, up to cyclic permutation."** So every tame
    width-2 (pentagon) frieze over F₂ has exactly two zero entries, and they are
    adjacent.
  * **Bearing on (J)42 Lemma 1.1** ("exactly two of the five cluster variables
    (h′, c, m, s, h) are even, and they are adjacent"). For odd N the pentagon frieze with
    boundary (1,1,1,1,N) reduces mod 2 to a Coxeter frieze over F₂ with all-ones boundary
    (unimodularity survives reduction, so it is tame), and in a width-2 frieze the five
    non-trivial entries are the five diagonals. Lemma 1.1 is therefore the q = 2 case of
    Morier-Genoud's §3.5 list. **KNOWN** (as a statement about F₂-friezes); the
    "even edge" vocabulary and its use for the ES sign (Thm 1.2) are the campaign's.
* **Girstmair, "Periodic continued fractions and Kronecker symbols",
  arXiv:1504.02618** (J. Integer Seq. 18 (2015) [snippet]) [visited; archived
  `sources/lit2026d/arxiv-1504.02618-girstmair.{pdf,txt}`].
  * §2, p. 2–3: **"If s/t = [a₀, …, a_k] is a rational number, then the Jacobi symbol
    (s/t) … depends only on the residue classes of a₀, …, a_k mod 4."** He attributes
    this to his earlier papers: K. Girstmair, *Continued fractions and Jacobi symbols*,
    Int. J. Number Theory 7 (2011) 1543–1555, and *Periodic continued fractions and
    Jacobi symbols*, IJNT 8 (2012) 1519–1525 (the 2011 abstract [snippet]: "relations for
    Jacobi symbols … with a simple right-hand side depending on t, q, N (mod 4)").
    Also: Girstmair, *Jacobi symbols and Euler's number e*, JNT 2014 [snippet: "The
    Jacobi symbol (p_k/q_k) depends only on the residue classes a₀, …, a_k ∈ ℤ/4ℤ"].
  * **Bearing on (J)42 "Consequence (R208 D15): χ is a function of (c, m, s) mod 4."**
    This is Girstmair's statement transported from regular to Hirzebruch–Jung (minus)
    continued fractions; his inductive proof (reciprocity at each Euclid step) applies
    verbatim to the minus expansion. **KNOWN in substance (Girstmair 2011, regular CF).**
  * **Bearing on (J)45 SHARP 2** (the closed product formula
    (K_{r−1}/N) = ∏(K_i, −K_{i+1})₂ · (−1)^{#sign changes}). The ledger already says
    "classical in substance — the Jacobi symbol along a continued fraction". Exact
    sources to cite: Girstmair 2011 (IJNT 7) for the mod-4 dependence; Eisenstein's
    even-quotient algorithm and Shallit's analysis (J. Symb. Comput. 1990, "On the worst
    case of three algorithms for computing the Jacobi symbol" [snippet]) and Bach–Shallit,
    *Algorithmic Number Theory* I (1996) [snippet via MathWorld] for computing the Jacobi
    symbol from the continued fraction. The specific Hilbert-symbol/Maslov form with signed
    words was not found → **PARTIAL** (mechanism classical, the signed product formula
    apparently new as stated).
* **Bleicher, "A new algorithm for the expansion of Egyptian fractions", J. Number
  Theory 4 (1972) 342–382** [Eppstein's annotated bibliography visited,
  https://ics.uci.edu/~eppstein/numth/egypt/refs.html; paper itself not read]: the
  "Farey sequence method" — Egyptian fraction expansion by telescoping Farey neighbours
  (a/b − c/d = 1/(bd)). This is the classical ancestor of (J)40 Thm 2.1's "Farey
  telescoping"; Ventas (arXiv:2605.04551) is the ES-specific precursor already recorded.
* **Short–Van Son–Zabolotskii, "Frieze patterns and Farey complexes",
  arXiv:2312.12953, Adv. Math. 2025** [abstract visited via search results]: already
  cited by (J)42 §3; nothing ES-specific.
* **Citations of Ventas 2605.04551** (Semantic Scholar API, visited): only Dahan
  2608.24035 and Bello-Hernández–Benito–Fernández 2606.10922, both already in
  LITERATURE_2026. No frieze/cluster paper on Egyptian fractions found.
* **Searches with no relevant hit:** "frieze patterns Egyptian fractions", "Conway-Coxeter
  frieze Erdős–Straus", "Erdős–Straus Farey sequence Ford circles", "Egyptian fraction
  Farey neighbours telescoping Erdős–Straus continued fraction", "Jacobi symbol minus
  continued fraction Hirzebruch–Jung formula".

### 1.2 Verdicts

| Claim | Verdict | Notes |
|---|---|---|
| (J)40 Prop 1.1 (five continuants = pentagon frieze / cluster variables) | KNOWN (already attributed: Conway–Coxeter, MGO, CHJ) | no change |
| (J)40 Thm 2.1 (five slices = Ford fans / Farey telescoping) | PARTIAL (already: Ventas for V₁) | add Bleicher 1972 (Farey method) as the classical Egyptian-fraction ancestor |
| (J)40 Cor 2.2 ("(A/N) = −1 ⟺ some cluster variable ≡ 0 (mod 4)") | APPARENTLY NEW as a statement | it is DK Thm 4.5 / MODEL_SPECIFIC 3.1(a) restated; the frieze reading is new |
| (J)42 Lemma 1.1 (mod-2 rigidity: exactly two adjacent even entries) | **KNOWN** | Morier-Genoud arXiv:1907.12790 §3.5 p. 12: the 5 width-2 friezes over F₂ are the rotations of (1,1,1,0,0) |
| (J)42 Thm 1.2 (sign from the even edge, 3-case proof) | APPARENTLY NEW proof of a known statement | statement = DK Thm 4.5 / MODEL_SPECIFIC 3.1(a) (already said) |
| (J)42 D15 consequence "χ is a function of (c, m, s) mod 4" | **KNOWN in substance** | Girstmair IJNT 7 (2011); stated explicitly in arXiv:1504.02618 §2 |
| (J)42 polygon-size uniqueness (r = 3 only) | APPARENTLY NEW | ES-specific; nothing found |
| (J)45 SHARP 2 (signed Hilbert-symbol product formula) | PARTIAL | mechanism classical (Girstmair 2011; Eisenstein/Shallit/Bach–Shallit); signed/Maslov form apparently new as stated |

---

## 2. Three squares, the Hurwitz order, path lattices in ℤ³ ((J)48, (J)53)

### 2.1 Findings

* **Kim–Oh, "Representations of integral quadratic forms by sums of squares"** (survey,
  author copy https://www.math.snu.ac.kr/~bkoh/sos.pdf) [visited; archived
  `sources/lit2026d/kim-sums-of-squares-survey.{pdf,txt}`], p. 3: "If ℓ_p → L_p for all
  p, or equivalently ℓ → gen(L), then … ℓ → K for some K ∈ gen(L)", and the
  Mordell–Ko values g[n] = n + 3 (n ≤ 5) are "an immediate consequence of local
  representation theory and the fact that the class number of I_n is one for
  1 ≤ n ≤ 8". So **a positive binary (or ternary) ℤ-lattice is represented by
  x² + y² + z² iff it is represented locally everywhere** — textbook.
* **Mordell 1930 / Schinzel 2013** [visited: Schinzel, Bull. Pol. Acad. Sci. Math. 61
  (2013) 23–28, archived `sources/lit2026d/schinzel-binary-five-squares.pdf`], p. 23:
  Mordell (Quart. J. Math. 1 (1930) 276–288) proved that a positive binary
  f = aX² + 2hXY + bY² is a sum of **four** squares of integral linear forms iff
  Δ = ab − h² is a sum of three squares. This is the same "binary form ↔ its determinant"
  mechanism; the three-squares case is Gauss, *Disq. Arith.* art. 278–292 [memory; not
  opened] — the representation of a binary form of determinant D by x² + y² + z² as the
  orthogonal complement of a vector of norm D.
* **Hurwitz order / B_{2,∞}.** That ℤi + ℤj + ℤk is the trace-zero part of the Hurwitz
  order and that B_{2,∞} has one class of maximal orders is textbook (Voight, *Quaternion
  Algebras*, ch. 11 [memory]); Venkov's quaternionic proof of the three-squares theorem
  uses exactly this [memory]. The maximal-lattice argument of Thm B (norm-maximal
  lattices on I₃ ⊗ ℚ form one genus, gen(I₃) has one class) is O'Meara 91:2 + class
  number one, as TWO_FIBRES itself states.
* **ES-specific search.** "Erdős–Straus sum of three squares binary form", "Egyptian
  fractions quaternion order supersingular", "Erdős–Straus quaternion": no hit beyond
  the campaign's own sources. Nothing found linking 4/n to x² + y² + z² as lattices.

### 2.2 Verdicts

| Claim | Verdict | Notes |
|---|---|---|
| (J)48 Thm A (χ = +1 ⟺ path binary T_w (or n·G_w) is a Gram of integer vectors in ℤ³) | **KNOWN in substance; ES specialisation APPARENTLY NEW** | local–global for representations by the one-class genus of I₃ (Gauss DA 278–292; Mordell 1930; Ko 1937; Kim–Oh survey p. 3). The new input is only CHI_FLIP's local computation (χ = Hasse invariant at p). TWO_FIBRES §1 already says this; the ledger line should carry it. |
| (J)48 Thm B (odd-square-determinant path lattices are index-m sublattices of ℤ³) | **KNOWN in substance** (maximal lattices + h(I₃) = 1); the ES reading (T1 as an embedding) is new | same remark |
| (J)48 Prop A2 (χ = +1 classes = conic points mod p / S₄) | KNOWN in substance (sublattices of ℤ³ of index p² isotropic mod p ↔ isotropic lines; Brandt/Eichler level-p orders in the Hurwitz order, as in LPS) | already flagged in TWO_FIBRES |
| (J)53 Lemma "T1 deforms": tp + 1 = tm² + c² | elementary; APPARENTLY NEW as an ES statement | see §5 for the polynomial-family side |
| (J)53 CONJECTURE 3SQ | EVIDENCE; no literature analogue found | — |

---

## 3. The sibling numerator 7 and failure-free numerators ((J)46, (J)49, (J)41)

### 3.1 Findings

* **Pomerance–Weingartner, arXiv:2511.16817v2 = Ramanujan J. 69 (2026) Paper 31**
  [archived `sources/pw.txt`, re-read].
  * Cor 2.2 / Cor 2.4 (pp. 4–5): for m ≥ 4 and p prime, Type I ⟺ ∃ a, d, f with
    f | ma²d + 1, mad | p + f; Type II ⟺ ∃ a, b, e with e | a + b, mab | p + e — ET's
    parametrisation with 4 → m (also attributed to Aigner, J. Reine Angew. Math. 1964, and
    Nakayama).
  * **§6 (p. 12): "By sifting with the seven congruences in [ET, Proposition 1.9], with 4
    replaced by m, we have verified the m = 5 case up to 10¹⁸, the m = 6, 7, 8 cases up to
    10¹³ …".** So PW use exactly the m-analogues of the Mordell/ET polynomial congruence
    families for m = 7; they do not print which classes mod 105 / 840 those families
    leave uncovered.
  * **Table 1 (p. 13): exceptions n ≤ N: m = 4 none (N = 10¹⁸); m = 5: 1; m = 6: 1;
    m = 7: 1, 2 (N = 10¹³); m = 8: 1, 2, 3, 11, 17, 131, 241; m = 9: 1, 2, 5, 11, 19; …**
    Hence the numerators with no non-trivial failure known are 4, 5, 6, 7 (and 3, which is
    trivial since m ≤ k). Rem 8.3 (p. 21): "When m = 7, the first prime p > 7² without a
    Type II solution is 127."
  * ET arXiv:1107.1010 Rem 1.10 (p. 8) [archived `sources/lit2026/audit-elsholtz-tao-1107.1010.txt`]:
    "The results in this paper would also extend (with minor changes) to the more general
    situation in which the numerator 4 … is replaced by some other fixed positive integer".
* **Math.StackExchange q. 3374919, "7/n as a sum of three unit fractions"** (2019; answer
  2023) [visited]: the level-14 identity for odd n ≡ 2 (mod 7):
  7/(14k − 5) = 1/(3k − 1) + 1/(2(3k − 1)) + 1/(2n(3k − 1)), with the remark that
  Schinzel's square obstruction does not prevent it. So at least one of (J)49's level-14
  identities is on record as folklore.
* **Palamà, "Su di una congettura di Schinzel", Boll. UMI (3) 14 (1959) 82–94** [visited,
  bdim.eu open PDF; text kept as `sources/lit2026d/palama-1959-bumi-signed-sums.txt`]:
  concerns Schinzel's **signed** version (sums ±1/x₁ ± 1/x₂ ± 1/x₃), verified there for
  m < 23; not about positive 7/n. Palamà 1958 (5/n) and B. M. Stewart 1964 (5/n for
  n ≢ 1 (mod 278460)) are the classical numerator-5 covering results [secondary: ET
  references; AIMS Math. 6 (2021) snippet]. **No published "7/n for all n ≢ 1 (mod 105)"
  statement was found.**
* **Not accessed:** Guy, *Unsolved Problems* D11 (only the front matter was retrievable);
  Sierpiński, Mathesis 65 (1956); Aigner 1964; Webb, Časopis 101 (1976).
* **Searches with no relevant hit:** "7/n sum of three unit fractions congruence classes
  covered", "Schinzel conjecture m/n … 7/n except n congruent 1 modulo", "m/n … numerator 7
  all primes except congruence class modulo 105", zbMATH (Palamà, Schinzel conjecture).

### 3.2 Verdicts

| Claim | Verdict | Notes |
|---|---|---|
| (J)49 Thm 3.1 (7/p for every odd prime p ≢ 1 (mod 105); uncovered set {1} at levels 14/42/70/210, {1, 211, 421, 631} at 840) | **KNOWN IN SUBSTANCE / folklore; exact printed statement not found** | the identities are PW Cor 2.2/2.4 instances; PW §6 sieve with "ET Prop 1.9, 4 → m" for m = 7 is the same covering (unprinted); one level-14 identity is on MSE 3374919. Ledger already disclaims novelty — keep, add the PW §6 and MSE pointers. |
| (J)46 "7/p solvable at every prime ≤ 10⁸" (CERTIFIED) | **KNOWN (stronger)** | PW Table 1: no exception n ≤ 10¹³ other than 1, 2 |
| (J)46/(J)49 "4, 5, 6, 7 are the failure-free numerators" (implicit) | KNOWN as EVIDENCE | PW Table 1 (p. 13) |
| (J)49 SHARP 2 (full T1 for 4 \| M; fails for M = 3, 5, 6, 7, 11, 19) | **PARTIAL** | the 4 \| M half is ET §4 / Prop 1.6 with d ↦ hd, as stated; the failure certificates (7/9, 7/25, …) are trivial searches; "only 4 among failure-free numerators has full T1" APPARENTLY NEW as a statement |
| (J)46 Prop 1.1/Cor 1.2 (shot families carry T1 iff −M is a discriminant) | APPARENTLY NEW (elementary) | — |
| (J)46 Thm 4.2 ("Mordell's 840 = reach of universal one-slot χ-witnesses", A ∈ {2,3,5,7,8,15,20}) | APPARENTLY NEW as a characterisation | the six Mordell classes are classical (Mordell 1969; Yamamoto 1965) |
| (J)41 Cor 2.1 (8/131 = 1/20 + 1/131 + 9/2620 etc.; M^□ certificates at the PW failures) | APPARENTLY NEW (finite computation) | failures themselves = PW Table 1 (already attributed in (J)31) |
| (J)41 Thm 1.1(a) (M^□(n) at every odd non-square n, M ≡ 0 (4)) | APPARENTLY NEW, elementary (one Dirichlet prime + genus character) | no "square-numerator relaxation" found in the literature |

---

## 4. Function-field coverings and divisors in residue classes ((J)51, (J)54, FF_STERILE_SMALL)

### 4.1 Findings (verified)

* **Cohn–Heninger, "Ideal forms of Coppersmith's theorem and Guruswami–Sudan list
  decoding", arXiv:1008.1284v2 = Adv. Math. Commun. 9 (2015) 311–339** [visited; archived
  `sources/lit2026d/arxiv-1008.1284-cohn-heninger.{pdf,txt}`].
  * **Thm 1.2 (p. 3, "A polynomial analogue"):** for monic f(x) of degree d over F[z] and
    p(z) of degree n, one can find (in polynomial time, hence there are boundedly many)
    all w(z) with deg w < β²n/d and deg gcd(f(w), p) ≥ βn. With f(x) = r + Q·x (d = 1,
    after normalising), a divisor D of F of degree δ = βn in the class r mod Q is
    D = r + Qw with deg w = δ − deg Q, so the theorem applies as soon as
    δ − deg Q < δ²/n, i.e. **deg Q > δ(n − δ)/n — exactly (J)51 Lemma 1.5's threshold**.
    The authors say the polynomial statement "appear[s] to be new" in 2010/2013 and that
    for split p(z) it is the Guruswami–Sudan theorem.
  * p. 4: "Bernstein noted that the Guruswami–Sudan theorem is the polynomial analogue
    of a related theorem of Coppersmith, Howgrave-Graham, and Nagaraj" — i.e. of
    divisors in residue classes.
* **Bernstein, "Reducing lattice bases to find small-height values of univariate
  polynomials" (2006/2008, in *Algorithmic Number Theory*, MSRI Publ. 44)** [visited
  http://cr.yp.to/ntheory/smallheight-20060531.pdf; archived
  `sources/lit2026d/bernstein-smallheight-2006.{pdf,txt}`]. Abstract + p. 1: unifies
  Lenstra 1984, Konyagin–Pomerance, Coppersmith–Howgrave-Graham–Nagaraj (divisors in
  residue classes) and Guruswami–Sudan; **"The theorems and algorithms can easily be
  switched from Q to the rational function field F_q(t) … although better algorithms are
  often available in the function-field case."** Table p. 2 and §6 (pp. 12–13): the
  divisors-in-residue-classes threshold history (Lenstra 1/3, Konyagin–Pomerance 0.3,
  CHN 1/4 + ε, ε removed by Lenstra).
* **Hales, "Divisors in residue classes revisited", arXiv:2410.05030** [visited; archived
  `sources/lit2026d/arxiv-2410.05030-hales.{pdf,txt}`]. Thm 1.3 (p. 1): Lenstra's
  algorithm over **ℤ[x]** for monic N, S, r with 3 deg S ≥ deg N (algorithmic; no
  per-degree count). §4 discusses Lenstra's counting model.
* **Coppersmith–Howgrave-Graham–Nagaraj, Math. Comp. 77 (2008) 531–545** (ePrint 2004/339)
  [abstract visited]: number of divisors of N ≡ r (mod s), s ≥ N^α, α > 1/4, is
  O((α − 1/4)^{−3/2}); the size-N^β refinement (find all divisors ≥ N^β in a class mod
  N^α once α > β(1 − β)) is the standard Howgrave-Graham/May form of Theorem 1.1 in
  Cohn–Heninger (p. 2: |w| ≤ N^{β²/d}, gcd(f(w), N) ≥ N^β).
* **Erdős–Straus over F_q[T].** Searches "Erdős–Straus conjecture polynomial ring finite
  field analogue", "Egyptian fractions polynomials over finite fields 4/f", "unit fractions
  function field analogue Erdős–Straus Mordell": no paper on ES_q, its coverings, or
  sterile points. (Hits: covering systems in F_q[x], arXiv:2407.15146; Woods–Erdős for
  polynomial rings; Guerrieri et al. "From ancient Egyptian fractions to modern algebra" —
  Egyptian fractions in integral domains, not the 3-term ES_q problem [snippets].)

### 4.2 Verdicts

| Claim | Verdict | Notes |
|---|---|---|
| (J)51 Lemma 1.5 (FF Coppersmith–Howgrave-Graham, threshold deg Q > d(n − d)/n) | **KNOWN** | Cohn–Heninger arXiv:1008.1284 Thm 1.2 (p. 3) with d = 1; Bernstein 2006 p. 1 (function-field switch "easy"). The pigeonhole proof and the explicit count may be new as written; the threshold is not. |
| (J)51 Lemma 1.4 (FF Lenstra: 3 deg Q > deg F ⇒ ≤ 2 divisors of a given degree in a unit class) | **PARTIAL** | the 1/3 regime over polynomial rings is Hales arXiv:2410.05030 Thm 1.3 (ℤ[x], algorithmic) and Bernstein's F_q(t) remark; the sharp per-degree constant 2 over F_q[T] was not found. |
| (J)54 Cor 1.4 (ℤ: divisors of size n^β in a unit class mod n^ρ number ≤ n^{max(0, β(1−β)−ρ)+o(1)}) | **KNOWN in substance** | Howgrave-Graham/May form of Coppersmith (Cohn–Heninger Thm 1.1, p. 2) + splitting the range into n^{β(1−β)−ρ} blocks; the ledger already calls it "a standard Coppersmith-type trick". |
| (J)51 Thm 3.1 (ES_q(T^k) has no finite linear covering for q = 3^r, r ≥ 4) | APPARENTLY NEW | no ES_q literature found |
| (J)51 §4 (char 2 non-sterile by Frobenius) | APPARENTLY NEW, elementary | — |
| (J)54 Thm 3.4 (explicit r₀ = 2³² for sterile Mordell points over ℤ) | APPARENTLY NEW | 10c §2 verdicts on sterile points stand (only the square obstruction is in the literature; Yamamoto/Ionascu–Wilson expect coverability at integer level) |
| FF_STERILE_SMALL Lemma 1.4 (branch side-agent/ff-sterile-small, O220; refined class bound below the Coppersmith threshold, extra exponent max(0, d(n − d)/n − ρ)) | **KNOWN in substance** | the F_q[T] twin of (J)54 Cor 1.4: Cohn–Heninger Thm 1.2 + splitting the class into q^{d(n−d)/n−ρ} subclasses |
| FF_STERILE_SMALL Lemmas 1.1–1.3 (Euclidean-division routes), Thms 3.1/5.2/8.1 (q = 27, q = 9, A = T) | APPARENTLY NEW | ES-specific; no ES_q literature |

---

## 5. Polynomial families on p = m² ± k, the T1 deformation ((J)53, (J)55)

### 5.1 Findings (verified)

* **Schinzel, "On sums of three unit fractions with polynomial denominators", Funct.
  Approx. Comment. Math. 28 (2000) 187–194** [Project Euclid abstract page visited (PDF
  behind a bot wall); zbMATH review Zbl 0974.11015 visited via the zbMATH Open API].
  Abstract: "The equation m/(ax + b) = 1/F₁(x) + 1/F₂(x) + 1/F₃(x) is shown to be
  impossible under some conditions on polynomials ax + b and F₁, F₂, F₃." Review: no such
  identity exists when **(1) m ≡ 0 (mod 4), a > 0, (a, b) = 1 and b is a quadratic
  residue mod a**, or (2) a > 0, m > 3b > 0. **Only linear denominators ax + b.**
  * Bearing on (J)55: Schinzel 2000 is exactly the linear case that NEAR_SQUARE Thm 3.3
    Rem (i) says it "recovers". It does not treat quadratic n(m) = m² ± k.
  * **Bearing on (J)49 SHARP 2:** Schinzel's condition (1) is for **every m ≡ 0 (mod 4)**,
    i.e. the polynomial-identity shadow of "full T1 holds for every multiple of 4". The
    ledger attributes the 4 | M half to ET §4 via d ↦ hd; Schinzel 2000 (1) should be
    cited alongside (it is the published "4 | m ⇒ square classes are not polynomially
    solvable" statement).
* **Schuh, "Restrictions on polynomial solutions of diophantine equations with sums of
  three unit fractions", HAL hal-04368730 (2024)** [HAL API record visited; the PDF is
  behind an Anubis wall]. Abstract: "The equation m/(a + bw) = 1/x(w) + 1/y(w) + 1/z(w)
  is shown to be incompatible with integer valued polynomials x, y, z if b is prime and
  a, b are coprime. Less stringent conditions for b lead to the same conclusion too."
  **Linear denominators only.** (Schuh's other HAL items: hal-04994962 (2025, Pythagorean
  primes, = arXiv:2503.11672 in LITERATURE_2026) and hal-05660622 (2026, "solution based
  residue classes" 4kx + 1 + 4(k − l)) — both linear classes, no quadratic families.)
* **Ghermoul, arXiv:2508.07383** [archived in `sources/lit2026/`, re-read p. 1]: explicit
  multivariable polynomials p_i(x, y, z) with 4p_i + 1 solvable; no obstruction theory,
  no quadratic one-variable families n = m² ± k.
* **Searches with no relevant hit:** "Erdős–Straus polynomial identities quadratic
  polynomial n = m² + k", "4/(m² + k) sum of three unit fractions polynomial identity",
  "Erdős–Straus numbers of the form n² + 1", HAL author search (Schuh).

### 5.2 Verdicts

| Claim | Verdict | Notes |
|---|---|---|
| (J)55 Lemmas 1.1/1.3 (per-solution χ = −1 witnesses (−4d/n), (f/n)) | KNOWN in substance | ET Prop 1.6 / Yamamoto 1965 Lemma 4 mechanism (ledger already says "ET Prop 1.6's mechanism") |
| (J)55 Thm 2.2 (k > 0: every Type I/II family in m on m² + k has a fixed-character witness) | **APPARENTLY NEW** | Schinzel 2000 and Schuh 2024 are linear-denominator only; ET Prop 1.9 is linear in n |
| (J)55 Thm 3.3 (integer T1 points above the largest real root obstruct every family) | linear case **KNOWN** (Schinzel 2000; ET Prop 1.6; Mordell); polynomial n(m) APPARENTLY NEW | — |
| (J)55 Thm 3.4 (K-adic unit-square set Z_K⁺ sterile, Hilbert reciprocity in ℚ(√j)) | **APPARENTLY NEW** | nothing found |
| (J)55 Prop 4.1 / (J)53 "T1 deforms": tp + 1 = tm² + c² | APPARENTLY NEW (elementary) | — |
| (J)55 escaping families for k < 0 (e.g. 4/2801) | APPARENTLY NEW (computation) | — |
