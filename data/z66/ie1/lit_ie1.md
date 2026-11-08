# IE1 / IOpen+Bezout literature check (primary-source verification)

Date: 2026-11-08. Working dir: /tmp/z66_ie1_lit1

**Access notes (no model/provider/auth/quota errors).** ScienceDirect PDFs (APAL, JPAA, J. Algebra) are behind a Cloudflare captcha: no full PDF was retrievable. For JPAA/J.Algebra/APAL-1996 I did get the **article landing page with the publisher abstract**. The APAL 1989 (Macintyre–Marker) and APAL 1990 (Kaye) landing pages stayed captcha-blocked. JSTOR/Cambridge Core (Wilmers, JSL 1985) are paywalled: I have the Cambridge Core "Extract" (first paragraphs) plus verbatim **JSTOR full-text search snippets** (from search-engine indexing of the JSTOR page). zbMATH Open reviews (API `https://api.zbmath.org/v1/document/_search`) are used as a reliable secondary source and are labelled as such. Raw dumps: `zb1.txt`, `zb2.txt`, `sda_*.md`, `cup_wilmers.md`.

Verdict legend: VERIFIED = primary full text read; PARTLY = abstract / snippet / review only; NOT FOUND.

---

## 1. G. Wilmers, "Bounded existential induction", J. Symbolic Logic 50(1) (1985) 72–90, doi:10.2307/2273790 (Zbl 0634.03029)

**Verdict: PARTLY.** Sources: Cambridge Core extract (https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/bounded-existential-induction/BC8F57CAE6FA2EF961E253495A3400C5), JSTOR snippets (https://www.jstor.org/stable/2273790), zbMATH review (M. Okada), and verbatim restatements in Smith (NDJFL 1993, full text read) and D'Aquino (NDJFL 1997, full text read).

- Opening (JSTOR snippet): "In this paper we introduce a system IE1, called bounded existential induction, which may perhaps be regarded as the weakest natural system which is stronger than open induction."
- **(a) Tennenbaum for IE1.**
  - JSTOR snippet: "**THEOREM 3.1.** Let M ⊨ IE1 be countable and nonstandard. Then + is not recursive. PROOF. We follow Tennenbaum's original idea in a suitably modified form …"
  - JSTOR snippet on multiplication (a result Wilmers credits to Paris): "… overspilling certain U1-properties of exponentiation, Jeff Paris has succeeded in proving the analogous result to 3.1 for multiplication: if M ⊨ IE1 is countable and nonstandard then [M's ·] is not recursive." (The snippet is OCR-garbled at the end.)
  - JSTOR snippet: "**THEOREM 4.11.** M↾+ is recursively saturated for any nonstandard M ⊨ IE1." "**COROLLARY 4.12.** If M is a countab[le] … such that M↾+ = N↾+. PROOF. As we noted above, M↾+ is a model of Presburger arithmetic …" (truncated; zbMATH: "In §4, the fact (2) [reducts to + are exactly the countable recursively saturated models of Presburger] for IE1 is shown (Theorem 4.11). The fact (1) [no nonstandard recursive model] is also obtained as this corollary (Corollary 4.12).")
  - zbMATH: "In §3 the author gives a direct short proof of the fact (1) for IE1, by modifying Tennenbaum's original proof for PA."
- **Other results, as Smith (1993) quotes them** (verbatim from the full text):
  - "**Theorem 2.3** [14] For every n ≥ 0, we have IE_{n+1} ⇒ IE_n ⇔ LE_n."
  - "**Lemma 2.7** [14] IE1 ⊢ ∀x[x > 0 → ∀y((x, y) = 1 → ∃z < x (yz ≡ 1 mod x))]." Wilmers' own wording, from a JSTOR snippet: "**LEMMA 2.4.** The following statement is provable in IE1: ∀x,y[((x,y) = 1 ∧ 1 < x < y) → ∃s < x (sy ≡ 1 mod x)]. PROOF. For fixed x, y by 2.1 (ii) we can apply LE1 …" Jeřábek (*On the theory of exponential integer parts*) says the argument even gives Bézout cofactors.
  - D'Aquino 1997, full text: "Wilmers showed in [16] that any nonstandard model of IE1 has a nonstandard initial segment which is a model of PA."
- **(b) Characterizations of models of IE1** (existential closedness, integer parts, …): **NOT FOUND** in any accessible text. Jeřábek–Kołodziejczyk (realclosures.pdf, Problem 6.1(a)) leave open whether every unbounded rcf with an IE1 integer part is recursively saturated. That suggests no integer-part characterization is known.
- **(c) Independence results.** None found in Wilmers. He lists open problems instead (JSTOR snippets): "(1) Is the hierarchy of systems IEn a proper hierarchy? (2) It is easily seen that, modulo PA⁻, the schemas IU1, IE1 and LE1 are all equivalent … Furthermore the schema LU1 implies each of them. But is LU1 implied by IE1? (This problem was raised by Laurie Kirby.) (3) Let M ⊨ IE1. Is every ∀F[?]-set coded in M? …" Smith (1993, full text): "(Actually, as is noted in [14], no proof is known that IE1 is strictly weaker than IΔ0.)" Also: "This theorem provides additional evidence concerning the remarkable strength of IE1." I could not determine which theorem this refers to. Snippet: "MRDP THEOREM (MATIJASEVIC [71]). §2. The systems IEn."
- **(d) How he builds models.** **NOT FOUND.** The accessible material only shows the paper proving properties of *all* nonstandard models (Tennenbaum argument, recursive saturation of +, PA initial segment). I saw no model construction.

## 2. S. T. Smith, "Fermat's last theorem and Bezout's theorem in GCD domains", J. Pure Appl. Algebra 79(1) (1992) 63–85, doi:10.1016/0022-4049(92)90127-2 (Zbl 0770.13014)

**Verdict: PARTLY** (publisher abstract read on the landing page https://www.sciencedirect.com/science/article/pii/0022404992901272; the PDF is captcha-blocked).

Abstract (verbatim): "We develop properties of GCD domains which enable us to show that Sophie Germain's theorem holds in all Z-rings with the GCD property. In particular, Sophie Germain's theorem and related results concerning Case I of Fermat's last theorem are provable in the weak system of arithmetic IOpen + GCD, open induction plus the GCD property. These results also hold in the stronger system IOpen + Bez, where Bez refers to Bezout's theorem which states that g.c.d.(x, y) is a linear combination of x and y. **We show that IE1 ⊢ IOpen + Bez**, where IE1 is the system of bounded existential induction. **In IE1 we can use infinite descent to prove that xⁿ + yⁿ = zⁿ has no nontrivial solutions for n = 4, 6 and 10.**"

zbMATH (M. Prest): "…if p is an odd prime not congruent to 1 modulo 8 then case 1 of Fermat's last theorem holds in the ring for n=2p … in any model of … bounded existential induction … Fermat's last theorem holds for n = 2, 6, 10." The review says 2, 6, 10; the abstract says 4, 6, 10. Trust the abstract.

Theorem numbers: not available. Glivický–Kala arXiv:1602.03580 (read) confirms: "Smith … proved that the theory IE1 … proves Fermat's Last Theorem for some small even exponents n (e.g., for n = 4, 6, 10). In the same paper, Smith also proves some special cases of FLT in the even weaker theory IOpen + 'every two elements have a greatest common divisor'."

## 3. S. T. Smith, "Building discretely ordered Bezout domains and GCD domains", J. Algebra 159(1) (1993) 191–239, doi:10.1006/jabr.1993.1154 (Zbl 0799.13010)

**Verdict: PARTLY** (publisher abstract read at https://www.sciencedirect.com/science/article/pii/S0021869383711543; theorem numbers come from secondary sources that I read in full).

Abstract (verbatim): "Using constructions due to A. Macintyre and D. Marker, we build GCD domains and Bezout domains with the open induction property. In fact we show that an open induction domain can be a principal ideal domain different from Z. The rings we construct are all countable or of cardinality ℵ1; we show that the order type of the infinite primes is arbitrary for GCD domains, subject to this cardinality restriction. This result also holds for countable Bezout domains. Our structures all have the additional property that any nonzero element is divisible by only finitely many n ∈ Z."

- **Construction:** Macintyre–Marker-style ω-chains. Jeřábek–Kołodziejczyk, "Real closures of models of weak arithmetic" (users.math.cas.cz/~jerabek/papers/realclosures.pdf, read; archived), describe "Smith [Smi93, Thm. 10.7] (building on [Wil78, MM89]) that there exists a nonstandard PID A ⊨ IOpen":
  - A0 = Z ⊆ A1 ⊆ …, each a discretely ordered UFD with a *parsimonious* hom φn : An → Ẑ.
  - "(i) The 'Ẑ-construction': … An+1 = {a/k : a ∈ An, k ∈ N, k | φn(a)}. This ensures that An is a Z-ring."
  - "(ii) The 'Wilkie construction' …"
  - "(iii) The 'construction F': … pick distinct nonstandard primes p, q ∈ An, and we put An+1 = An[v, (pv − 1)/q], where v ∈ L, v > An."
  - Result: "A is a model of IOpen …, a UFD, and every pair of primes has Bézout cofactors (due to construction F). The last two conditions imply that A is a PID."
- **Theorem numbers** cited by Mohsenipour (arXiv:1003.2117, read):
  - Thm 1.5: "M is factorial iff M has both of the GCD property and DCC".
  - Lemma 3.8: in a GCD domain irreducible ⇔ prime.
  - Lemma 3.4 and Lemma 3.7 (Bezout gcd's).
  - Lemma 5.1, Thms 5.3, 5.5: Ẑ-construction preserves parsimony / GCD / DCC.
  - Thms 6.8, 6.10, 6.12: transcendental extensions.
  - Thms 8.5, 8.7, 8.9: F-construction.
  - Thms 9.4, 9.8: unions of chains.
  - **Thm 10.7**: Bezout (PID) model of open induction. Thm 10.8 is the ℵ1 version.
- **Nonstandard primes?** Yes. The abstract says the order type of the infinite primes is arbitrary (countable Bezout case). Construction F explicitly uses pairs of nonstandard primes. Jeřábek: "IOpen + Bézout is known to disprove e.g. the rationality of √2, but not the existence of a greatest prime ([Smi93])."
- **Residue rings M/pM:** not stated in any accessible source. What can be said:
  - All chain members are Z-rings (Mohsenipour: "his chain of domains are ZR-rings"), so M/nM ≅ Z/nZ for standard n.
  - For nonstandard primes p in a Bezout domain, M/pM is a field. This is my algebraic remark, not a quoted result.
  - No description of these residue fields was found.

## 4. A. Macintyre, D. Marker, "Primes and their residue rings in models of open induction", Ann. Pure Appl. Logic 43(1) (1989) 57–77, doi:10.1016/0168-0072(89)90025-0 (Zbl 0675.03040)

**Verdict: PARTLY** (ScienceDirect captcha; zbMATH review by V. Yu. Sazonov read: https://zbmath.org/?q=an:0675.03040). Review (verbatim excerpts):

- "(A) … α ∈ R is an irreducible … ↛ α is a prime (i.e., R/αR is a domain); also, α is a prime ↛ R/αR is a field."
- "(B) The order type of the infinite primes may be arbitrary."
- "(C) All the infinite primes may be congruent to 1 mod 4 (resp. 3 mod 4)."
- "**(D) The residue field of an infinite prime may be any characteristic 0 field of infinite transcendence degree.**"
- "(E) The field of fractions may be elementarily equivalent to any ordered field which is dense in its real closure."
- "(F) Schinzel's hypothesis … may hold."
- "(G) Every infinite even integer may be the sum of two primes."
- "Here, except case (E), R is normal."
- "…from (D) … OI does not suffice to give quadratic non-residues for odd primes. Indeed, the residue field of such a prime may be algebraically closed. In the case of a real closed residue field such a prime cannot be a sum of squares, so Lagrange's theorem fails here. Moreover, there is a normal model of OI in which the primes are cofinal and no infinite prime is a sum of squares. Also, there is a (nonnormal) model R of OI in which Lagrange's theorem fails, but every positive element is a square of an element of F(R)."
- "All these models are constructed by union of chains arguments, involving repeated use of certain purely algebraic constructions."
- Open problem: "is there a recursive nonstandard model of OI with an infinite prime?"

Lemma numbers, via Mohsenipour arXiv:1003.2117:
- Lemma 1.3: remainder homomorphism M → Ẑ.
- Lemma 3.1: the Ẑ-construction yields a Z-ring.
- Lemma 3.2: irreducibles with unit image stay irreducible.
- **Lemma 3.26: the F-construction M[x, (1−xv)/w]** ("By Lemma 3.26 of (Macintyre-Marker [3]) we are sure that we can do the F-construction").
- Lemma 3.27: irreducibles stay irreducible under F.

## 5. P. D'Aquino, "Pell equations and exponentiation in fragments of arithmetic", Ann. Pure Appl. Logic 77(1) (1996) 1–34, doi:10.1016/0168-0072(95)00018-6 (Zbl 0855.03034)

**Verdict: PARTLY** (publisher abstract read at https://www.sciencedirect.com/science/article/pii/0168007295000186; PDF captcha-blocked).

Abstract (verbatim): "We study the relative strength of the two axioms (P) Every Pell equation has a nontrivial solution (exp) Exponentiation is total over weak fragments, and **we show they are equivalent over IE1**. We then define the graph of the exponential function using only existentially bounded quantifiers in the language of arithmetic expanded with the symbol #, where #(x, y) = x^[log2 y]. We prove the recursion laws of exponentiation in the corresponding fragment."

- So the equivalence is stated **over IE1** (hence also over IΔ0). Exact theorem numbers are not available.
- Consequence (my inference, not quoted): IE1 ⊬ (P), since IE1 ⊆ IΔ0 and IΔ0 ⊬ exp (Parikh).
- Related: D'Aquino, "Solving Pell equations locally in models of IΔ0", JSL 63 (1998) 402–410 (zbMATH, Kossak): "Any Pell equation x²−dy²=1 … has always a nontrivial solution modulo every element m ∈ M, for every model M ⊨ IΔ0."

## 6. R. Kaye, "Diophantine induction", Ann. Pure Appl. Logic 46(1) (1990) 1–40, doi:10.1016/0168-0072(90)90076-E (Zbl 0693.03038). Citation confirmed (Crossref, zbMATH).

**Verdict: PARTLY** (zbMATH review by R. Murawski plus a ResearchGate abstract snippet; ScienceDirect blocked).

- zbMATH: "Let I∃1⁻ be the subsystem of Peano arithmetic obtained by restricting the induction scheme to diophantine formulas without parameters. **The main result … says that I∃1⁻ ⊢ IE1⁻ + E ⊢ Matijasevič's theorem**, where IE1⁻ is the scheme of parameter-free bounded existential induction and E is an ∀∃ axiom expressing the existence of a function of exponential growth. This answers the question of Z. Adamowicz if I∃1 does prove Matijasevič's theorem. It is also connected with the problem: 'IΔ0 ⊢ Matijasevič's theorem?', which is still unsolved. The theorem is proved by means of a conservation result relating parameter and parameter-free induction schemes … The paper is concluded by some consequences of these results to the structure of countable nonstandard models of IE1⁻."
- Snippet (abstract): "We show that Matijasevič's Theorem on the diophantine representation of r.e. predicates is provable in the subsystem I∃⁻1 of Peano Arithmetic formed by restricting …"
- D'Aquino 1997 (full text) quotes Kaye's "**Theorem 1.2** (i) ∀E1(N) ⊢ IE1⁻; (ii) For every σ ∈ ∀E1(N) if M ⊨ IE1⁻ + ¬σ then M is not recursive." Line (i) is garbled in the extraction, and the reference is to Kaye [7] (possibly Kaye 1990 or Kaye's "Model-theoretic properties characterizing Peano arithmetic").
- No IE1 independence results were found.
- Related: Kaye, "Hilbert's tenth problem for weak theories of arithmetic", APAL 61 (1993) 63–73 (publisher abstract read via search index). It gives a negative answer to H10 for "some particular finite fragment of the weak theories IE1 … or IU1⁻".

## 7. P. D'Aquino, "Toward the limits of the Tennenbaum phenomenon", Notre Dame J. Formal Logic 38(1) (1997) 81–92, doi:10.1305/ndjfl/1039700698 (Zbl 0889.03052)

**Verdict: VERIFIED** (full text read via Jina reader of the Project Euclid PDF; saved as `dAquino1997_NDJFL_tennenbaum_fulltext.md`).

- Abstract: "We prove that PA# and its weak fragments, down to ∀E#1(N) and IE1^{−#}, are subject to the Tennenbaum phenomenon with respect to +, ·, and #. For the last two theories it is still unknown if they may have nonstandard recursive models in the usual language of arithmetic."
- On IE1: "Wilmers proved the same result for nonstandard models of IE1 (see [16])"; and "Wilmers showed in [16] that any nonstandard model of IE1 has a nonstandard initial segment which is a model of PA."
- Theorems:
  - **Thm 2.1**: the # of a nonstandard model of PA# is not recursive.
  - **Thm 3.2**: "If M is a nonstandard model of IE#1 then the operations +, ·, and [#] … are not recursive."
  - **Thm 3.3**: "Let M be a nonstandard model of IE1^{−#} and assume M is not a model of ∀E1(N). Then +, ·, # of M are not recursive."
  - **Thm 3.5**: nonstandard models of ∀E#1(N) have non-recursive +, ·, #.
- The proof uses an E1#-definition of the graph of exp via Pell equations x² − ((a+1)² − 1)y² = 1.
- Nothing about building IE1 models; nothing about Bezout.

## 8. Other models / independence for IE1 and IOpen+Bezout

- **S. T. Smith, "Quadratic residues and x³+y³=z³ in models of IE1 and IE2", NDJFL 34(3) (1993) 420–438, doi:10.1305/ndjfl/1093634730. VERIFIED** (full text; `smith1993_NDJFL_quadres_fulltext.md`).
  - Abstract: "It is unknown whether the fragment of arithmetic IE1 (or even the stronger system IΔ0) proves that every odd prime has a quadratic nonresidue. We show that one direction of the quadratic reciprocity law holds in IE1 when one of the primes is standard…"
  - **Cor 2.8**: if M ⊨ IE1 and p is prime in M, then M/pM is a field.
  - **Thm 3.11**: M ⊨ IE1, p, q primes, p standard: (q/p)=1 ⇒ (p/q)=1 unless p ≡ q ≡ 3 mod 4, in which case (p/q) = −1.
  - **Thm 4.2**: M ⊨ IE1, q odd prime: q = x²+y² ⇔ (−1/q)=1. This is the two-squares theorem for primes, *relative to* −1 being a QR.
  - **Thm 4.4**: the same for x²+2y² with (−2/q) and x²+3y² with (−3/q).
  - **Cor 4.5**: the same for x²+4y².
  - **Thm 5.2**: IE2 ⊢ x³+y³=z³ → x=0 ∨ y=0.
  - Open **Questions 5.1–5.6**, e.g. "Does IE1 prove that if q ≡ 1 mod 4 is prime then (−1/q)=1? Is this provable in IΔ0?" and "Can Fermat's last theorem for exponent 3 be proved in IE1?"
- **S. T. Smith, "Prime numbers and factorization in IE1 and weaker systems", JSL 57(3) (1992) 1057–1085 (Zbl 0768.03022). PARTLY** (author's abstract via zbMATH): "We show that IE1 proves that every element greater than 1 has a unique factorization into prime powers, although we have no way of recovering the exponents from the prime powers which appear. The situation is radically different in Bezout models of open induction. To facilitate the construction of counterexamples, we describe a method of changing irreducibles into powers of irreducibles, and we define the notion of a frugal homomorphism into Ẑ…" Mohsenipour cites its Lemmas 1.9, 1.10 for OI ⊬ OI+N ⊬ OI+GCD ⊬ OI+Bez.
- **Jeřábek & Kołodziejczyk, "Real closures of models of weak arithmetic" (AML 2013; preprint read, archived `jerabek_realclosures.pdf`). VERIFIED.**
  - **Thm 4.1**: "There exists an unbounded countable principal ideal domain A ⊨ IOpen (and therefore a model of Bézout + there exist unboundedly many primes + existence and uniqueness of prime factorization) such that rcl(A) is not recursively saturated."
  - It holds for IΔ0/IE2 under a cofinality assumption. **Problem 6.1(a)** asks whether it holds for IE1.
- **Enayat–Łełyk–Visser arXiv:2508.14758 (read).** **Thm B.1**: IE1 + ∀1-Coll ⊢ I∃1. **Thm B.2**: IE1 + Coll ⊢ PA.
- **Jeřábek arXiv:2209.01197 (read)**, Question 7.2: "Is every non-polynomially-bounded countable model of IE1 (or at least, IΔ0) an [exponential integer part]…?"
- **Not found:** any paper constructing a *specific* nonstandard model of IE1, or proving IE1 ⊬ φ for a concrete true number-theoretic φ (QNR existence, two/four squares, Pell, infinitude of primes) by a model construction. Here is what the sources do say:
  - Smith says the IE1 vs IΔ0 separation is unknown, and the QNR question is open even for IΔ0.
  - The only "independence" consequence available is IE1 ⊬ Pell, via D'Aquino's equivalence with exp plus Parikh. That is an inference, not a stated theorem.
  - For IOpen (+N, +GCD, +Bez), independence via Macintyre–Marker/Smith chain models is well documented: see items 3 and 4.

## 9. Mohsenipour, Bezout computable model

**Verdict: PARTLY — talk abstract only. No full paper found.**

- The abstract "A Bezout Computable Nonstandard Model of Open Induction" (Logic Colloquium 2008, Bern) is archived as `lc08_mohsenipour_abstract.pdf`, via https://web.archive.org/web/2009/http://www.lc08.iam.unibe.ch/abstracts.php?speaker=mohsenipour. Quote: "…we go one step further by bringing all of these materials together (Smith's chains, Berarducci-Otero's computable construction and Moniri's transseries) to produce a computable nonstandard model of Open Induction which is Bezout and has cofinal primes." Also: "Bezout is stronger than GCD and Bezout is weaker than IE1."
- Published full paper: only the GCD version, "A recursive nonstandard model for open induction with GCD property and cofinal primes", Logic in Tehran, Lect. Notes Logic 26 (2006) 227–238 (paywalled; summary not available).
- Jeřábek–Kołodziejczyk: "In [Moh06], it is stated (and proved for a slightly weaker theory) that IOpen + Bézout has recursive nonstandard models."
- Enayat et al. (2025) still cite [Moh06] as "the latest results in this direction".
- arXiv author search for Mohsenipour: no such paper. The closest is arXiv:1003.2117, "Hierarchies of subsystems of weak arithmetic", whose **Theorem C** is "Bez + (OI)p ⊬ (OI)p+1, p ≠ 3"; it gives no computable model.

## 10. J. Glivická, P. Glivický, "Shepherdson's theorems for fragments of open induction", arXiv:1701.02001

**Verdict: VERIFIED** (full text, archived). The paper contains **nothing about Bezout or IE1**. Its results:
- **Thm 1** (Shepherdson): M ⊆IP R(M) ⇔ M ⊨ IOpen.
- **Thm 2**: Presburger ⇔ M ⊆IP M/N.
- **Thm 3**: IOpenLin ⇔ M ⊆IP F(M).
- **Thm 5**: eIOpen ⇔ F(M) dense in R(M).
- **Cor 6**: IOpen = IOpenLin + eIOpen.
- **Open question 9**: "Are there variants of the Shepherdson's theorem for theories stronger than IOpen?"
