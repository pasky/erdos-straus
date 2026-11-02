# Literature report: primes and simultaneous sum-of-two-squares shifts

**Research note.** I use “sum of two squares” in the ordinary sense; it permits prime factors `q ≡ 3 (mod 4)` to occur to even exponent. This is strictly weaker than the set `S`, whose members have no such prime factors. A primitive sum of two squares is in `S`, but ordinary representations need not be primitive (for example 9 = 3²+0²). “Quote” below means the source’s wording/formula, not a paraphrase. I mark conclusions not directly established by a source as **UNVERIFIED** rather than claiming literature exhaustiveness.

## Results directly relevant to the question

| Source | Exact source statement | Relevance / limit |
|---|---|---|
| **Kunjakanan Nath and Likun Xie (2025 preprint), “Almost primes and primes that are sums of two squares plus 1,” arXiv:2501.16723v1 (submitted 28 Jan 2025), Theorem 1.1; published in *Acta Arithmetica* (arXiv listing gives DOI 10.4064/aa250227-19-11).** [arXiv listing](https://arxiv.org/abs/2501.16723); [v1 full text](https://arxiv.org/html/2501.16723v1) | “`# {p ≤ x : p prime, p = m²+n²+1, m,n∈N, Ω(p+2)≤11} ≫ x/(log x)^(5/2).`” (Theorem 1.1.) Abstract: “we obtain a lower bound for the number of primes p≤x such that p−1 is a sum of two squares and p+2 has a bounded number of prime factors.” | The strongest close prime/shift result found: prime `p`, `p−1` a sum of two squares, and `p+2` an 11-almost-prime (counted with multiplicity). It does **not** give `p+2` a sum of squares, both shifts sums of squares, or either shifted value in `S`. Their proof explicitly invokes the vector sieve and semi-linear/linear sieves. The theorem states a positive lower bound of order `x/log^(5/2)x`. |
| **James Maynard (2016), “Dense clusters of primes in subsets,” *Compositio Mathematica* 152 (2016), 1517–1554; arXiv:1405.2593v2.** [arXiv listing](https://arxiv.org/abs/1405.2593); [full text](https://arxiv.org/html/1405.2593v2) | Abstract: “We prove a generalization of the author's work to show that any subset of the primes which is `well-distributed' in arithmetic progressions contains many primes which are close together.” | Theorem 3.1 is a distribution-hypothesis result for prime subsets, not a theorem that arbitrary simultaneous multiplicative conditions on distinct linear shifts are achieved. To apply it, the target prime subset must meet its quantitative distribution hypotheses. No verified application here establishes two shifted sums of squares or `S` conditions. |
| **Joni Teräväinen (2018), “On binary correlations of multiplicative functions,” *Forum of Mathematics, Sigma* 6 (2018), e10, 41 pp.; arXiv:1710.01195v2.** [arXiv listing](https://arxiv.org/abs/1710.01195) | Abstract: “We study logarithmically averaged binary correlations of bounded multiplicative functions g₁ and g₂.” It further says under uniform distribution in fixed-modulus progressions he obtains “a discorrelation estimate, showing that the correlation of g₁ and g₂ is asymptotic to the product of their mean values.” | This concerns logarithmic correlations over ordinary integers, not prime-indexed correlations `g(p+a)g(bp+c)`. The applications named by the abstract concern large prime factors of `n,n+1`, consecutive smooth numbers, and character sums over reducible quadratic polynomials. It supplies no theorem for prime `p` with two shifted norm conditions. |
| **Cochrane–Dressler, “Consecutive Triples of Sums of Two Squares”** (source PDF: [author-hosted manuscript](https://www.math.ksu.edu/~cochrane/research/sumsquare.pdf)). | The manuscript’s opening states: “Hooley (1973) gave an affirmative answer” to the question of infinitely many `n` with `n,n+h,n+k` sums of two squares for fixed positive `h,k`; it studies triples `n,n+1,n+2` and gives an upper bound `B₃(x) ≪ x/(log x)^(3/2)`. | These are integer-variable correlations, including consecutive triples, not prime `n` and not the stricter `S` condition. Bibliographic details and exact theorem numbering for this manuscript/Hooley original were not independently confirmed here: **UNVERIFIED**. |

## Answers to the requested subquestions

### (a) Iwaniec and `p=x²+y²+1`

Henryk Iwaniec, “Primes of the type φ(x,y)+A where φ is a quadratic form,” *Acta Arithmetica* 21 (1972), 203–234; [EuDML record](https://eudml.org/doc/205106), [journal PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa21/aa21118.pdf). The paper is the classical half-dimensional-sieve result for prime values of a positive definite binary quadratic form plus a fixed integer. The standard notable specialization is `x²+y²+1` (Linnik’s conjecture), with later work by Motohashi (1969/70, 1971/72), Iwaniec, and others refining the count; Matomäki’s 2007 paper states that it gives the first unconditional proof of infinitely many primes `p=m²+n²+1`.

The Iwaniec PDF retrieved in this session was not text-extractable, so I cannot responsibly provide a verbatim theorem number/statement from it. **UNVERIFIED:** theorem numbering and exact general-form statement; do not rely on a reconstructed quote. The associated technique is a half-dimensional sieve for the two-square condition and distribution of primes in progressions (Bombieri–Vinogradov-type input), but this is not itself a theorem that every prime `p+A` has only prime factors `1 mod 4`. A prime value of `φ+A` does not control the factorization of the different shifted integer. Hence it gives no `S` conclusion for `p+a`.

For the special shape `p=1+m²+n²`, Nath–Xie’s Theorem 1.1 above directly provides a quantitative result, but only coupled with `p+2` having at most 11 prime factors.

### (b) Two / three shifted sums of squares; prime variant

Hooley’s result, as reported in the Cochrane–Dressler manuscript, gives infinitely many `n` such that `n,n+h,n+k` are all sums of two squares for any fixed positive `h,k`. In particular, this implies infinitely many consecutive triples as a special case. The manuscript also gives an upper bound for the count of consecutive triples. These statements are for unrestricted integer `n`, not prime `n`, and “sum of two squares” does not mean `S`.

Teräväinen’s binary-correlation paper is about logarithmically averaged multiplicative functions over `n`, as quoted above. Its abstract does not assert prime-restricted correlations. No verified source found here proves infinitely many primes `p` for which two fixed distinct shifts are both sums of two squares. Exact Hooley and Cochrane–Dressler theorem details are **UNVERIFIED** because the primary PDF OCR was unavailable.

### (c) Maynard–Tao, Chebotarev, bounded gaps

Thorner’s “Bounded gaps between primes in Chebotarev sets” and Maynard’s “Dense clusters of primes in subsets” concern primes subject to specified Frobenian / arithmetic-progression distribution hypotheses. Maynard’s abstract quote above confirms the subset framework. Such results can produce nearby primes **inside an eligible subset**, but do not automatically prove that `p+a` or `bp+c` is a norm: those are conditions on shifted values, and require a separate theorem proving the relevant prime-set distribution. **No verified application was found** yielding infinitely many `p` with both `p+a` and `bp+c` in `S` (or both ordinary sums of squares).

Banks–Freiberg–Turnage-Butterbaugh and Pollack works were searched by topic; no source verified in this session supplies the requested two-shift conclusion. That negative survey conclusion is **UNVERIFIED** (not a proof that no such paper exists). A prime being in a Chebotarev class is a condition on the prime itself; it does not impose the required prime-factor restrictions on two separate linear forms.

### (d) Linear forms and quadratic-form correlations

Lilian Matthiesen, “Linear correlations amongst numbers represented by positive definite binary quadratic forms,” arXiv:1106.4690 (2011); *Acta Arithmetica* 154 (2012). [arXiv listing](https://arxiv.org/abs/1106.4690). The source describes the object as representation functions `r(n)=|{(x,y): f(x,y)=n}|` and linear correlations of those functions. It is a result about counting integer tuples/linear patterns with values represented by positive definite binary quadratic forms—not a prime variable with simultaneous norm constraints. **Exact theorem statement and number not verified from the source in this run.**

Tim Browning and Lilian Matthiesen, “Norm forms for arbitrary number fields as products of linear polynomials,” arXiv:1307.7641 (2013), *Annales Scientifiques de l’École Normale Supérieure* 50 (2017), 1383–1446. [arXiv listing](https://arxiv.org/abs/1307.7641); [journal record](https://www.numdam.org/articles/10.24033/asens.2348/). Its scope is norm-form varieties in which a field norm equals a product of linear polynomials, with integral-point/counting results. It does not supply, as far as verified here, a prime-value condition on one linear form together with two other forms that are norms. The precise theorem-level statement was not confirmed: **UNVERIFIED**.

No verified result found counting systems `(u,v)` with one linear form prime and two independent linear forms sums of two squares. The general integer correlation results cannot be read as prime-variable results.

### (e) Vector sieve / Chen-type results

Nath–Xie (above) is directly relevant and explicitly says its proof uses the vector sieve, a semi-linear sieve, and a linear sieve. It proves `p−1` is an ordinary sum of two squares while `p+2` has at most 11 prime factors. This is **not** the requested condition that `(p+a)(p+b)` be free of small primes `3 mod 4`, nor that both values be in `S`.

Search also found the cited framework of Brüdern–Fouvry, “Lagrange’s four squares theorem with almost prime squares,” *Ann. Sci. École Norm. Sup.* 27 (1994), 1–16; [EuDML](https://eudml.org/doc/153645). It is methodological background, not a verified result on two shifted prime forms. No verified weighted-sieve theorem was located proving `p+a∈S` and `p+b` with only a bounded number of `3 mod 4` prime factors. That negative claim is **UNVERIFIED**.

### (f) Prime in a thin norm set plus another norm shift

Friedlander–Iwaniec’s Gaussian-prime theorem proves infinitely many primes of the form `a²+b⁴` (not `a²+b²` with `b` prime). Fouvry–Iwaniec’s “Gaussian primes” work and later thin-variable prime-form work produce primes in special polynomial/norm-related sequences. No source verified here proves infinitely many primes `p=N(α)` for which `N(α)+c` is also a norm, let alone two such shifts. The requested assertion is not implied by primes represented by one norm form. Heath-Brown–Li work found in search concerns almost-prime triples / Chen-type results, not a verified two-norm-shift theorem. These negative survey conclusions are **UNVERIFIED**.

### (g) Distribution beyond 1/2 and shifted sieve weights

Bombieri–Friedlander–Iwaniec and later Maynard/Lichtman results improve distribution for particular sequences or weighted prime sums. A level of distribution for primes in progressions does not alone give a bilinear distribution theorem with two independent moduli encoding `p≡−a (mod d₁)` and `bp≡−c (mod d₂)`, nor an asymptotic for `Σ_p r(p+a)λ(bp+c)`. I found no verified source establishing the specific two-shift weighted sum requested. **UNVERIFIED** as an exhaustive absence statement.

## Verdict

1. **Is it known unconditionally that infinitely many primes `p` have `p+4∈S` and `4p+1∈S`?** No such theorem was located or verified. The answer based on this search is **not known from the sources found**; absence from this survey is not a proof of nonexistence in the literature. Importantly, even a theorem that both are ordinary sums of two squares would be weaker than the `S` requirement.
2. **Closest verified result:** Nath–Xie, Theorem 1.1: many primes `p=m²+n²+1` with `Ω(p+2)≤11`. Separately, Hooley’s unrestricted integer-variable theorem gives multiple shifted sums of two squares, including triples, but no prime restriction.
3. **Explicit open-problem quote:** The Nath–Xie introduction calls the twin-prime conjecture “one of the famous unsolved problems,” but it does not state the present two-norm-shift question as open. I did **not** verify an explicit published statement that `p+a` and `bp+c` simultaneously sums of two squares is open. Claims that specific named authors explicitly posed this exact variant are therefore **UNVERIFIED**. The report should not present a broad literature gap as a formal open-problem citation.

## Source verification notes

ArXiv abstract/listing pages and the full HTML of Nath–Xie v1, Teräväinen, and Maynard were fetched directly. Nath–Xie’s Theorem 1.1 was checked in the HTML theorem block. Iwaniec’s scanned PDF could not be text-extracted during this run; several other requested papers’ exact theorem statements were not confirmed at theorem level. Those have been called out above instead of given invented quotation or numbering. Search route: the required `web-search/search.py` and `visit.py` skills were read and used; sources are linked inline.
