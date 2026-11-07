# Literature verification: weak arithmetic, primes, and integer-part models

**Scope.** Verdicts below concern whether the specific requested claim is supported by an accessible primary-source passage; they do not imply that unverified claims are false. Exact theorem numbers are given only when located. “Close paraphrase” is identified as such. Source access was incomplete for several paywalled papers, especially Mohsenipour; no construction details are inferred from a title or abstract.

## 1. Shepherdson (1964)

**Reference.** J. C. Shepherdson, “A non-standard model for a free variable fragment of number theory,” *Bulletin de l’Académie Polonaise des Sciences, Série des sciences mathématiques, astronomiques et physiques* **12** (1964), 79–86.

**Primary/near-primary verification.** Full original paper not accessed. Glivická & Glivický’s paper explicitly states the characterization, citing Shepherdson: Jana Glivická and Petr Glivický, “Shepherdson’s theorems for fragments of open induction,” arXiv:1701.02001 (2017), [HTML](https://arxiv.org/html/1701.02001v1), Introduction and Theorem 1.

> “A discretely ordered semiring M is a model of IOpen if and only if M is an integer part of the real closure R(M).” (Close paraphrase of the cited result; Theorem 1 of Glivická–Glivický states the equivalence in detail.)

The same source, Introduction, says Shepherdson proved there is a recursive nonstandard IOpen model, constructed as an integer part of a real closed field. The characterization is therefore **VERIFIED** through an explicit later restatement, but original text is not directly checked.

**Requested particular model claims.** The primary 1964 text was not available here for its construction details. Claims that Shepherdson's model is specifically a Puiseux-polynomial integer part, contains no nonstandard primes, or has a “rational” square root of 2 are **NOT FOUND** in the accessible primary material. “√2 rational” needs clarification: not a standard rational number; in some nonstandard models it may be a quotient of model elements. Do not cite as established without a direct source.

**Accessible secondary leads (not a substitute for the paper).** R. Kaye, *Models of Peano Arithmetic* (Oxford, 1991), is cited by Glivická–Glivický as foundational background, but no exact chapter passage was verified. Berarducci–Otero’s abstract does not establish Shepherdson-specific model properties. Verdict on the three model-specific assertions: **NOT FOUND**.

## 2. Berarducci & Otero (1996)

**Reference.** Alessandro Berarducci and Margarita Otero, “A recursive nonstandard model of normal open induction,” *The Journal of Symbolic Logic* **61**(4) (1996), 1228–1241. [JSTOR record](https://www.jstor.org/stable/2275813).

**Accessible primary-source abstract:**

> “In this paper we present a recursive nonstandard model of normal open induction with an unbounded set of infinite prime elements.”

That abstract-level result is **VERIFIED**. “Unbounded” here means the infinite primes are cofinal in the model’s ordering (a prime exceeds every prescribed element). The record is accessible; full construction was not accessed, so a precise representation of elements is **NOT FOUND** from the primary text during this verification.

The question whether its elements are real-evaluable functions, a ring of functions, or Puiseux-type polynomials with a specific coefficient field is **NOT FOUND**. Nor does the abstract settle any evaluation/constant-term homomorphism to Z. Avoid transferring properties of generalized power-series integer parts to this particular construction absent the paper.

## 3. Mohsenipour (2006) — central construction question

**Reference.** Shahram Mohsenipour, “A recursive nonstandard model for open induction with GCD property and cofinal primes,” in *Logic in Tehran*, Lecture Notes in Logic **26**, Association for Symbolic Logic, 2006, pp. 227–238. DOI: [10.1017/9781316755747.014](https://doi.org/10.1017/9781316755747.014). [Cambridge chapter landing page](https://www.cambridge.org/core/books/logic-in-tehran/recursive-nonstandard-model-for-open-induction-with-gcd-property-and-cofinal-primes/BE9EB45DC441D943BE92D760B8717B7E).

**Primary-source evidence accessible.** Cambridge preview of the chapter, p. 227, gives the opening passage (visible on the [landing page](https://www.cambridge.org/core/books/logic-in-tehran/recursive-nonstandard-model-for-open-induction-with-gcd-property-and-cofinal-primes/BE9EB45DC441D943BE92D760B8717B7E)):

> “Shepherdson provided an algebraic characterization for models of Iopen as follows: M is a model of open induction iff M is an integer part of its real closure. Berarducci and Otero [1] have constructed a recursive nonstandard model for normal open induction with cofinal primes. We modify their method to construct a recursive nonstandard model for open induction with cofinal primes in which the GCD property also holds.”

This verifies the stated result and its connection to Berarducci–Otero, but only at preview level (**PARTLY** for the requested construction). Chapter metadata confirms pp. 227–238 and 2006 print year. Cambridge’s chapter PDF URL was attempted but returned an anti-bot HTML page; no complete PDF or arXiv/author-hosted version was located.

**Elements / coefficient field / evaluation / prime form.** The accessible excerpt does not specify these. Whether the construction consists of Puiseux polynomials, which coefficient field or constant terms it uses, whether elements can be evaluated at real points, and whether a constant-term/evaluation map is a ring homomorphism to Z are all **NOT FOUND**. No source passage located says that `1+t` is prime (or identifies any particular displayed element as prime): **NOT FOUND**.

**Most important conclusion.** The source does verify existence of a recursive nonstandard model of IOpen with the GCD property and cofinal primes; it does **not**, in the accessible evidence, establish the stronger desired package “a nonstandard prime in a model with real-evaluable elements and a ring homomorphism to Z.” Whether Mohsenipour’s actual construction has that package remains **NOT FOUND**, not disproved. The claim must not be inferred from “cofinal primes.”

## 4. Macintyre & Marker (1989)

**Reference.** Angus Macintyre and David Marker, “Primes and their residue rings in models of open induction,” *Annals of Pure and Applied Logic* **43**(1) (1989), 57–77. [Publisher record](https://www.sciencedirect.com/science/article/pii/0168007289900250); DOI commonly indexed as 10.1016/0168-0072(89)90025-0.

The bibliographic reference is verified by the publisher record. Search-accessible primary abstract/title metadata verifies the paper’s subject, but the detailed theorem statements were not available for inspection. The asserted existence in models of IOpen of infinite primes and analysis of their residue rings is consistent with the title and citations, but exact main theorem/proposition numbers and verbatim statements are **NOT FOUND**. Do not invent a theorem number. Verdict for detailed claims: **PARTLY** (bibliography/subject only).

## 5. Generalized power series: Berarducci and Pitteloud

**Berarducci reference.** Alessandro Berarducci, “Factorization in generalized power series,” *Transactions of the American Mathematical Society* **352**(2) (2000), 553–577. Search results identify the paper’s central theorem as existence of irreducibles in a generalized power-series ring, but an accessible primary passage with theorem number and full statement was not retrieved. Exact claims such as “the series x^(1/n) is irreducible” and prime existence in the truncation integer part are **NOT FOUND** here; irreducible and prime must not be conflated.

**Pitteloud reference.** Daniel Pitteloud, “Existence of prime elements in rings of generalized power series,” *The Journal of Symbolic Logic* **66**(3) (2001), JSTOR [record](https://www.jstor.org/stable/2695102). The accessible JSTOR search snippet from the primary paper says:

> “Very recently, Berarducci (see [1]) proved that K((G^{≤0})) does have irreducible elements, hence answering a question of Conway and Gonshor …”

This establishes the distinction and motivation but not Pitteloud’s theorem text or number. Main theorem and hypotheses: **NOT FOUND** in the accessed primary passage. The record supports a result specifically about prime elements by title; a theorem-number-level verification awaits full text.

**Caution on transfer.** Generalized power-series results concern specified rings and should not be treated as results about Mohsenipour’s model unless an explicit identification is supplied.

## 6. Related induction and Diophantine papers

**Wilmers.** George Wilmers, “Bounded existential induction,” *The Journal of Symbolic Logic* **50**(1) (1985), 72–90. [JSTOR](https://www.jstor.org/stable/2273790). The primary-source abstract/snippet says:

> “In this paper we introduce a system IE1, called bounded existential induction, which may perhaps be regarded as the weakest natural system which is stronger …”

The snippet is truncated and no theorem statement was verified. Claims about IE1’s failure to prove specific Diophantine sentences: **NOT FOUND**.

**Otero (1990).** Margarita Otero, “On Diophantine equations solvable in models of open induction,” *The Journal of Symbolic Logic* **55** (1990); exact issue/pages and theorem number not verified. Search result indexed as paper abstract states: “We prove that each model of IOpen can be embedded in a model where the equation …” (snippet truncates before the equation/conclusion). **PARTLY**; do not supply an inferred theorem number.

**Otero (1993).** Margarita Otero, “Quadratic forms in normal open induction,” *The Journal of Symbolic Logic* **58** (1993), [JSTOR record](https://www.jstor.org/stable/2275215). Accessible first-page search snippet: “Models of normal open induction (NOI) are those normal domains associated to the fragment of Peano arithmetic based on the induction …” No main theorem passage or theorem number located: **PARTLY** (bibliography/intro only).

**Smith (1993).** S. T. Smith, “Building discretely ordered Bezout domains and GCD domains,” *Journal of Algebra* **159**(1) (1993), 191–239. Verified citation in Cambridge reference list. Main theorem text/number not accessed: **NOT FOUND**.

**D’Aquino (1996).** Paola D’Aquino, “Pell equations and exponentiation in fragments of arithmetic,” *Annals of Pure and Applied Logic* (1996). Exact volume/pages and theorem passage not verified. **NOT FOUND** at theorem-level.

**Smith (1992).** S. T. Smith, “Fermat’s last theorem and Bezout’s theorem in GCD domains,” *Journal of Pure and Applied Algebra* **79** (1992). Publisher search abstract states:

> “We show that IE1 ⊢ IOpen + Bez, where IE1 is the system of bounded existential induction.”

[Publisher record](https://www.sciencedirect.com/science/article/pii/0022404992901272). This abstract claim is **VERIFIED**; exact theorem number and full theorem statement not located. It does not itself say Fermat’s n=3 or n=4 is unprovable in IOpen; no such inference is made here.

## 7. Nonprovability and primes in weak arithmetic

**Open induction.** Berarducci–Otero’s abstract gives a recursive nonstandard model of normal open induction with unbounded infinite primes; Mohsenipour’s accessible preview gives a recursive nonstandard model of IOpen with GCD and cofinal primes. These are existence/model results, not by themselves statements that a particular named Diophantine Pi1 sentence is independent.

**Specific Pi1 claims.** No accessible primary source passage was located here proving that IOpen, normal IOpen, IOpen+GCD, or IE1 fails to prove irrationality of √2, Fermat n=3 or n=4, “every element has an irreducible divisor,” or infinitude of primes. Status of each requested nonprovability assertion: **NOT FOUND** in this verification. Smith (1992) abstract verifies IE1 proves IOpen plus Bezout-domain condition, not the requested negative claims.

**Arbitrarily large primes / prime divisors.** Cofinal-prime model results show these properties are not automatic in every model of the respective theory only if one establishes the relevant model-theoretic interpretation of the sentence; the accessible abstracts do not state a precise independence theorem. Whether IOpen proves arbitrarily large primes or every n≥2 has a prime divisor is **NOT VERIFIED** from primary theorem text here. In ordinary weak arithmetic, “every n≥2 has a prime divisor” is a bounded/least-counterexample argument and is much weaker than infinitude; do not identify it with the latter.

## 8. IE1, IΔ0, and infinitude of primes

The standard least-number-principle argument establishes that a number greater than 1 has an irreducible/prime divisor using bounded induction: among divisors >1 choose the least; if composite it has a smaller divisor >1. This is a mathematical argument, not a citation-verified theorem in the sources accessed above. Accordingly, the requested exact theorem number/source for IΔ0 proving every n≥2 has a prime divisor is **NOT FOUND** here; the underlying claim is ordinarily provable in IΔ0 (and hence in stronger IE1, subject to the usual language/definition of prime).

The Paris–Wilkie–Woods result is bibliographically identifiable as J. B. Paris, A. J. Wilkie, and A. R. Woods, “Provability of the pigeonhole principle and the existence of infinitely many primes,” *The Journal of Symbolic Logic* **53** (1988), 1235–1244. The accessible search result names the paper, but did not expose the primary theorem passage. Exact theorem number and exact consequence for IΔ0 alone versus IΔ0+WPHP are **NOT FOUND** in this verification. Thus the assertion that infinitude of primes is open for IΔ0 and that adding WPHP proves it is not confirmed here with a quotable primary statement. Do not convert this literature-level uncertainty into a verdict about the truth of the claim.

---

## Short findings (15 lines)

1. Shepherdson’s integer-part characterization of IOpen is directly restated as Theorem 1 in Glivická–Glivický (2017).
2. The original 1964 paper’s specific model construction details were not accessible.
3. Shepherdson’s “no nonstandard primes” and “√2 rational” claims remain unverified.
4. Berarducci–Otero’s 1996 abstract explicitly gives a recursive NOI model with an unbounded set of infinite primes.
5. “Unbounded” supports cofinality of that set; the abstract does not describe the ring elements.
6. Mohsenipour’s citation and chapter pages (227–238) are verified.
7. His accessible Cambridge preview explicitly claims recursive IOpen + GCD + cofinal primes.
8. That verifies the central existence result, but only at preview level.
9. I did not locate a complete Mohsenipour PDF or an alternative arXiv/author copy.
10. Therefore coefficient field, element form, real evaluation, and constant-term map to Z remain unknown here.
11. No accessible source says `1+t` is prime in Mohsenipour’s model.
12. The desired evaluation-homomorphism/nonstandard-prime combination is not established by the verified evidence.
13. Macintyre–Marker bibliography is verified, but exact theorem numbers/statements were inaccessible.
14. Smith (1992) abstract verifies IE1 ⊢ IOpen + Bez, not the specific Fermat nonprovability claims.
15. Separate “every n has a prime divisor” (least divisor) from “infinitely many primes”; theorem-level source checks remain incomplete.
