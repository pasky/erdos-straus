# z52 Astra: direct parent source checks and corrections

Accessed **2026-10-30** using the visit-webpage skill; these are short excerpts, not entire papers. Verification is of statements, not an independent proof audit.

## 1. Grynkiewicz: degree deficits and exponent budgets

David J. Grynkiewicz (single author), *A Generalization of the Chevalley-Warning and Ax-Katz Theorems with a View Towards Combinatorial Number Theory*, arXiv:2208.12895v1 (2022-08-26 per arXiv metadata in research ledger). https://arxiv.org/html/2208.12895v1. The reader's HTML “Published Time” is 2026-08-24; that is not silently substituted for the arXiv version date.

- Theorem 1.1: “If n > Σ deg f_i, then |V| ≡ 0 mod p.”
- Theorem 1.2: “If n > (m−1) max deg f_i + Σ deg f_i … then |V| ≡ 0 mod p^m.” This is the stated sufficient bound, not a claim of the strongest finite-field normalization.
- Theorem 1.5: “Let G be a finite abelian p-group. Then D(G)=D*(G).” Earlier defines D*(G)=1+Σ(n_i−1).
- Theorem 1.6: s(C_p²)=4p−3.
- Theorem 1.3 allows weighted sums and equations modulo differing prime powers, but charges degrees multiplied by ((t_i+1)p^{m_i}−1)/(p−1). Merely adding variables or choosing higher moduli is not a cost-free lift.

Original Chevalley/Warning/Ax/Katz/Olson papers NOT ACCESSED. These classical statements are checked through an authored mathematical source, not falsely represented as primary-source access.

## 2. Alon: nonvanishing and zero-sum

Noga Alon, *Combinatorial Nullstellensatz*, Combinatorics, Probability and Computing 8 (1999), 7–29, DOI 10.1017/S0963548398003413. Author PDF https://www.tau.ac.il/~nogaa/PDFS/null2.pdf, undated author-copy revision; journal 1999 version metadata.

- Theorem 1.2: degree Σt_i and nonzero coefficient of ∏x_i^{t_i} imply some nonzero value on any product of sets |S_i|>t_i.
- Theorem 1.1 is the ideal-membership form, NOT a coefficient formula (corrected research draft).
- Theorem 3.2: |A+B|≥min{p,|A|+|B|−1} for nonempty A,B⊆Z_p.
- Proposition 8.2: any 2p−1 members of Z_p contain p members summing to zero. Adjacent paragraph says the general EGZ result follows by induction.
- Lemma 8.3: a nonzero permanent of the replicated-column matrix certifies an additive basis. It needs (p−1)n columns and provides full coverage; not a logarithmic universal zero-sum theorem in cyclic groups.

## 3. Zagier: genuine finite-index forcing

Don Zagier, *A One-Sentence Proof That Every Prime p≡1 (mod 4) Is a Sum of Two Squares*, American Mathematical Monthly 97 (February 1990), p. 144, DOI 10.2307/2323918. https://people.mpim-bonn.mpg.de/zagier/files/doi/10.2307/2323918/fulltext.pdf. Unnumbered theorem/proof.

Source defines a finite positive-triple set x²+4yz=p and gives an involution with exactly one fixed point. Quote: “Only the last requires that p be a prime of the form 4k+1, the fixed point then being (1,1,k).” Swapping y,z then has a fixed point. The finite set is NOT all integer triples (research draft corrected to positive triples). Source: “the proof is not constructive: it does not give a method to actually find the representation”. This concerns the displayed argument, not impossibility of algorithms.

## 4. Lenstra: sparse height count, unrestricted first height

Hendrik W. Lenstra Jr., *Solving the Pell equation*, MSRI Publications 44 (2008), accessed 24-page author/book copy, §1 pp. 1–3. https://library.slmath.org/books/Book44/files/01lenstra.pdf. Source notes prior version Notices AMS 49 (2002), 182–192.

Quote: “there is a solution for every d” (positive nonsquare d fixed in preceding paragraph); ordered solutions obey x_n+y_n√d=(x_1+y_1√d)^n. Source explicitly identifies exponential growth and Dirichlet's unit theorem. The purely periodic expansion is of floor(√d)+√d, NOT √d itself (research draft corrected). O_D(log H) bounded-height count is an elementary consequence; no uniform polynomial-in-d first-height bound is claimed.

## 5. Palindromes: three terms, but many candidates

Javier Cilleruelo, Florian Luca, Lewis Baxter, *Every positive integer is a sum of three palindromes*, arXiv:1602.06208v2 (2017-06-17). https://arxiv.org/html/1602.06208v2.

Theorem 1.2: “Let g≥5. Then any positive integer can be written as a sum of three base g palindromes.” §2: “The proof … is algorithmic … input a positive integer n and obtain a representation”. Small (<7-digit) inputs are handled separately. The independent-density estimate of order n^{1/2} for triple representations is OUR HEURISTIC, not a theorem of this source. It follows by comparing Θ_g(√n) palindromes through n with the n possible sum targets.

## 6. Zhang: current full Zaremba claim, not an ES theorem

Xin Zhang, *Expansion in SL₂(Z/qZ) and Zaremba’s Conjecture*, arXiv:2605.02518v2 (2026-05-08 per arXiv record; HTML has later rendering date). https://arxiv.org/html/2605.02518v2.

Theorem 1.2: “Zaremba's conjecture holds.” Following text: “Our method can only produce a large but an absolute bound.” Intro records BK M=50 density one and Huang M=5 density one. The proof plugs Theorem 3.6 into Shkredov's Theorem 8 framework. §4 defines Cantor sets of size ≍t^{2w_M} and uses intervals of power length. This verifies that a full claim exists; it does NOT independently certify its proof or journal acceptance. The campaign already recorded it in B2_ACROSS_FIELDS and LITERATURE_2026_UPDATE.

## 7. Geometry of numbers: source locator repaired

Zichao Dong, *Minkowski’s Theorem and Its Applications*, undated note in CMU 2018–19 reading-seminar archive, https://www.math.cmu.edu/~ttkocz/files/archive/teaching/1819/read-sem-notes.pdf. First note p. 3, unnumbered general-lattice theorem: bounded symmetric convex C with vol(C)>2^d det Λ has a nonzero lattice point. Next theorem proves two squares with det Λ=p and 0<a²+b²<2p. No original Minkowski publication access is claimed.

## 8. Post-review metadata checks

- **Pollack–Schorn:** parent opened https://www.pollack-math.net/finding3squares-6.pdf. Title is *Dirichlet’s proof of the three-square theorem: an algorithmic perspective*, authors Paul Pollack and Peter Schorn. Abstract explicitly gives the Gauss–Legendre forbidden form 4^k(8m+7). Correct publication: Math.Comp.88 (2019),1007–1019, DOI10.1090/mcom/3349 (reviewer Crossref check). The initial draft's DOI10.1090/mcom/3376 is unrelated and withdrawn. Author PDF revision date not stated; reader last-modified timestamp is not treated as publication date. AMS landing-page re-access gave CAPTCHA.
- **McGown–Treviño:** parent opened https://campus.lakeforest.edu/trevino/SurveyLeastNonResidue.pdf. Title page: *The least quadratic non-residue*, Kevin McGown and Enrique Treviño, July18,2019. §2 Thm2.6 gives Burgess's inequality; immediately following calculation gives n_p≤p^{1/(4√e)+ε} for sufficiently large p depending on ε (through p.6). No original Burgess paper was accessed.
- **Ivanov:** https://arxiv.org/abs/0906.5193 records v2 as **2019-08-25**, not August24. Quote: “last revised 25 Aug 2019 (this version, v2)”.
- **Elsholtz–Tao:** https://arxiv.org/abs/1107.1010, *Counting the number of solutions to the Erdős–Straus equation on unit fractions*, Christian Elsholtz and Terence Tao; v6 August2,2015, J.Aust.Math.Soc.94 (2013),50–105. Abstract states the prime-average bounds Nlog²N≪Σ_{p≤N}f(p)≪Nlog²NloglogN. HTML full-text request incorrectly redirected to a plot; no numbered full-text theorem is asserted from this access. The fixed-x divisor dictionary used in §2.1 is derived algebraically in the memo, and its attribution to the prior ET framework is not a claim of source-page verification of that exact formula.
