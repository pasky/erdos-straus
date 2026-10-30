# z52 Astra exclusion ledger — source checks

Access date for the source checks below: **2026-10-30**.

Scope: source-level screening of commonly cited neighboring results. This is a ledger, not a recommendation or a grading of the Astra approach. “Does not establish” below is strictly about the quoted theorem's quantifiers; it is not a claim that a stronger theorem is impossible. Pages were opened and read, not inferred from search-result snippets.

## Verified theorem scopes

### Heath-Brown / primitive roots

- **Source:** D. R. Heath-Brown, “Artin’s Conjecture for Primitive Roots,” *The Quarterly Journal of Mathematics* **37**(1) (1986), 27–38. DOI: [10.1093/qmath/37.1.27](https://doi.org/10.1093/qmath/37.1.27). The journal page is [here](https://academic.oup.com/qjmath/article/37/1/27/1515517); it returned a bot-verification screen on access, so it did not independently expose the theorem text.
- **Accessible statement checked:** K. Conrad, answer to “State of the art for primitive roots,” MathOverflow, posted 18 Aug. 2022, [full answer page](https://mathoverflow.net/questions/428755/state-of-the-art-for-primitive-roots#answer-428764). This opened with the full answer, not a snippet, and states Heath-Brown’s 1986 result as: Artin’s primitive-root conjecture holds for all but at most two prime values of the base, and all but at most three squarefree bases greater than 1. In particular, **at least one** of 2, 3, 5 is a primitive root modulo infinitely many primes.
- **Quantifier boundary:** the 2/3/5 conclusion is an **existential disjunction** over the three fixed bases. It does not say which one works; does not prove the conclusion for each of 2, 3, and 5; and does not give a result for every prime modulus or every individual input. The actual journal page was inaccessible here, so regard exact theorem wording as checked through the accessible secondary page, bibliographic metadata through the journal record.

### Chen / prime plus an almost-prime

- **Source:** J. R. Chen, “On the representation of a large even integer as the sum of a prime and the product of at most two primes,” *Scientia Sinica* **16** (1973), 157–176. DOI: [10.1360/ya1973-16-2-157](https://doi.org/10.1360/ya1973-16-2-157). The publisher record at [Science China Press / ScienceChina](https://www.sciengine.com/doi/10.1360/ya1973-16-2-157) was identified; its accessible record describes the result as every sufficiently large even integer being a prime plus a product of at most two primes.
- **Statement:** for every sufficiently large even integer \(N\), there is a representation \(N=p+P_2\), where \(p\) is prime and \(P_2\) has at most two prime factors (with multiplicity; conventions may include 1). This is an “all sufficiently large even N” statement, but the second summand is allowed to be composite.
- **Count qualification:** a 2024 Berkeley additive-number-theory lecture handout by Robert Baxter, “Chen’s Theorem,” [full PDF text](https://math.berkeley.edu/~avizeff/additive/talk_19.pdf), explicitly states the stronger representation-count formulation \(r(N)\gg S(N)N/(\log N)^2\), with \(r(N)\) counting odd-prime plus at-most-two-prime-factor representations and gives its singular-series definition. This is a secondary exposition, not the 1973 paper; constants/normalization depend on the definition of \(S(N)\). Neither formulation asserts two-prime Goldbach for every even N.

### Shao / Vinogradov three-prime theorem

- **Source:** Xuancheng Shao, “A New Proof of Vinogradov’s Three Primes Theorem,” arXiv:1303.2276v1, submitted 9 Mar. 2013, [record](https://arxiv.org/abs/1303.2276); the page identifies the author, title, version/date, and full-text PDF/HTML. The published article is *Discrete Analysis* (2017), Paper No. _DA_2017_1, according to the journal record.
- **Statement (as expressed in the abstract):** every sufficiently large odd positive integer is expressible as a sum of three primes. Thus this is pointwise existence for all sufficiently large odd targets, with no restriction that the primes be distinct or satisfy any special congruence.
- **Counts:** the checked abstract claims existence and a new proof, not a quantitative lower bound for the number of representations of each target. Do not convert this citation into a uniform pointwise representation-count claim without checking a theorem in the paper that states such a bound. A separate result in the same general area may give counts; this citation alone, as checked here, is not that claim.

### Erdős–Selfridge / consecutive products

- **Source:** P. Erdős and J. L. Selfridge, “The Product of Consecutive Integers is Never a Power,” *Illinois Journal of Mathematics* **19**(2) (1975), 292–301. DOI: [10.1215/ijm/1256050816](https://doi.org/10.1215/ijm/1256050816). [Full Project Euclid PDF](https://projecteuclid.org/journals/illinois-journal-of-mathematics/volume-19/issue-2/The-product-of-consecutive-integers-is-never-a-power/10.1215/ijm/1256050816.pdf) was opened and its text read.
- **Theorem 1 (source wording):** “The product of two or more consecutive positive integers is never a power.” The theorem concerns nontrivial perfect powers (exponent at least2). The PDF extraction confuses `≥` with `>` in its setup; the initial draft's `ℓ>2` restriction was an OCR error and is not used. The quoted Theorem1 covers two or more consecutive positive integers.
- **Quantifier boundary:** this rules out a perfect-power product of a consecutive block; it says nothing by itself about shifted-prime representations, prime-plus-powers, or arbitrary nonconsecutive factors.

## Distribution / heuristic results, not every-object existence

### Romanoff: positive density, not universal coverage

- **Source:** I. Romanoff, “Über einige Sätze der additiven Zahlentheorie,” *Mathematische Annalen* **109** (1934), 668–678. Bibliographic details are consistent with the source’s later literature; an opened 2024 arXiv survey [“A generalization of the Romanoff theorem,” arXiv:2401.15892v2](https://arxiv.org/html/2401.15892v2) identifies Romanoff’s 1934 result as positive lower density for integers representable as \(p+2^k\), with \(p\) prime and \(k\ge0\).
- **Exact safe reading:** positive lower density means a positive proportion in the asymptotic lower-density sense; it is not a claim that every sufficiently large integer, or every integer, is representable. No pointwise universal theorem is inferred here.

### Sierpiński and Riesel numbers: different expressions

- **Accessible source:** M. Kozek, “On powers associated with Sierpiński numbers, Riesel numbers, and positive odd integers \(k\) for which \(|k-2^n|\) is composite,” undergraduate research paper (2008), [Whittier institutional record/PDF](https://poetcommons.whittier.edu/cgi/viewcontent.cgi?article=1009&context=math). Direct PDF access returned HTTP 403, so the paper’s theorem text was not independently checked. Search indexing and later literature give the standard definitions, but those snippets are **not** treated as verified source statements in this ledger.
- **Lead only / not verified here:** standard terminology calls odd \(K\) Sierpiński when \(K2^n+1\) is composite for every positive \(n\), and Riesel when \(K2^n-1\) is composite for every nonnegative \(n\) (conventions about the starting index vary). These concern fixed-coefficient sequences \(K2^n\pm1\), not the assertion that every target \(N\) has or lacks a representation \(N=p+2^k\). The precise Sierpiński/Riesel references and any proposed “failure” claim are left **unverified** rather than promoted to theorem.

### Selfridge/Romanoff p + 2^k failure leads

- A possible association of “Selfridge” with exceptions or counterexamples for universal \(p+2^k\) representation was not pinned to an opened primary source. Romanoff’s positive-density theorem does not itself imply a complement or a pointwise failure statement. **Unverified lead; no exception, counterexample, or universal claim recorded.**

### Davenport–Heilbronn: aggregate asymptotics

- **Original source:** H. Davenport and H. Heilbronn, “On the density of discriminants of cubic fields. II,” *Proceedings of the Royal Society of London A* **322** (1971), 405–420. Bibliographic citation appears in the authors’ accessible paper below.
- **Accessible full source:** M. Bhargava, A. Shankar, and J. Tsimerman, “On the Davenport-Heilbronn theorems and second order terms,” arXiv:1005.0672v3, submitted 5 May 2010, revised 20 June 2012, [record and full text](https://arxiv.org/abs/1005.0672). The abstract states that the Davenport–Heilbronn theorems give main terms for (i) the number of cubic fields of bounded discriminant and (ii) the number of 3-torsion elements in class groups of quadratic fields of bounded discriminant; their paper proves second main terms too.
- **Quantifier boundary:** these are asymptotic counts/averages over discriminants or fields. They do not assert a prescribed property for each individual quadratic field, class group, discriminant, or target integer. In particular, an average 3-torsion theorem cannot be read as every-object existence.

### Cohen–Lenstra: explicitly heuristic

- **Source:** H. Cohen and H. W. Lenstra, “Heuristics on class groups of number fields,” in *Number Theory, Noordwijkerhout 1983*, Lecture Notes in Mathematics **1068**, Springer (1984), 33–62. Bibliographic citation and the authors’ description of the heuristic are given in the accessible Bhargava–Shankar–Tsimerman paper above (references and discussion of class-group distributions).
- **Scope:** the Cohen–Lenstra framework proposes probabilities for class-group structures, weighted in the imaginary-quadratic setting by reciprocal automorphism counts (with setting-dependent modifications). It is a heuristic distributional model, not a theorem and not a deterministic existence assertion for every individual object. Do not use it to fill a universal pointwise gap.

## Unverified items deliberately left open

1. Heath-Brown’s journal full text was blocked at source access; exact wording above is cross-checked through a complete, opened MathOverflow answer, while the journal record verifies citation metadata.
2. Chen’s original paper full text was not obtained. The basic statement is corroborated by the publisher’s accessible paper record; the count bound is attributed only to the opened 2024 lecture handout and its displayed conventions.
3. Shao’s accessible arXiv abstract supports the pointwise existence statement; no pointwise count lower bound is claimed here.
4. Any stronger “Romanoff/Sierpiński/Riesel/Selfridge counterexample to p+2^k for every object” formulation remains unverified. The standard Sierpiński/Riesel sequences are not interchangeable with the variable-prime representation problem.
