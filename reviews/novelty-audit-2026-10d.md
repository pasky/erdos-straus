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
