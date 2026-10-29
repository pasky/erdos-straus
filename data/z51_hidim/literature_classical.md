# Classical sieve source audit — parent-checked correction of research notes

The initial research notes misattributed arXiv:1012.3809 to Sara Blight, reversed a sifting-limit inequality, and assigned a 2.445 coefficient to Ankeny–Onishi without reading the original. Those claims are withdrawn. The checked sources below supersede them.

## Richert, Lectures on Sieve Methods (TIFR lecture text)

Read primary text PDF: https://www.math.utoledo.edu/~codenth/Spring_13/3200/NT-books/Lectures_on_Sieve_Methods-Richert.pdf

Chapter 11, printed pp. 134–136, (11.3), (11.6), Theorems 11.2 and 11.4:
- Dimension condition: −L≤Σ_{w≤p<z}ω(p)log p/p−κlog(z/w)≤A₂.
- 1/G(z)=W(z)e^{γκ}Γ(κ+1){1+O(L/log z)}.
- Under the usual local bound Ω₁, dimension condition Ω₂(κ,L), and |R_d|≤ω(d), Theorem 11.4 gives
  S(A,P,z)≤Γ(κ+1)·∏_p[(1−ω(p)/p)(1−1/p)^{−κ}]·X/(log z)^κ·{1+O((log log(3z)+L)/log z)}, z≤√X.
- The text explicitly allows O constants to depend on κ,A₁,A₂. Taking κ=k and z≈√X gives the familiar leading constant 2^k k! for fixed admissible prime tuples, not a growing-k uniform statement.

Chapter 12, printed pp. 159–160: Ankeny–Onishi replaced Kuhn's constant weight by a logarithmic weight, more effective and smoothing the prime-divisor sum; Richert generalized it. This is the precise AO statement verified here. Original: N. C. Ankeny and H. Onishi, The general sieve, Acta Arith. 10 (1964/65), 31–62. Original theorem not obtained; no AO large-dimension numerical constant is used.

## C. S. Franze, Sifting Limits for the Λ²Λ⁻ Sieve

Read primary PDF: https://arxiv.org/pdf/1012.3809 (arXiv identifier v1; manuscript date June 6, 2022).

Printed pp. 1–2: βκ is the threshold beyond which the LOWER sieve becomes positive, not an upper-sieve constant. The introduction attributes βκ≲2.44κ for DHR to Diamond–Halberstam book Chapter 17, and Selberg's large-κ bound βκ≲2κ+19/36 to Collected Papers II, pp. 174–176. These are the paper's reports of prior work, not original proofs checked in this session; no exact asymptotic βκ∼cκ is invoked.

Theorem 1, p. 2: assuming (2) |A_d|=X/f(d)+R_d, (3) Σ_{d<X/(log X)^A} μ²(d)7^{ν(d)}|R_d|≪X/(log X)^{κ+1}, and (4) Σ_{p<s}log p/f(p)=κlog s+O(1), the displayed lower bound S(A,P,x^{1/βκ})≫x/(log x)^κ holds for the listed pairs κ=2,…,10, βκ=4.516,6.520,8.522,10.523,12.524,14.524,16.524,18.525,20.525. Table 1 compares DHR thresholds 4.266,6.640,9.072,11.534,14.014,16.504,18.998,21.495,23.992. Fixed dimensions; not RLD-U at fixed s and κ→∞.

## Opera de Cribro / DHR originals — access limits

Friedlander–Iwaniec, Opera de Cribro (2010): https://www.ams.org/books/coll/057/ . Book chapter was not directly accessible; do not treat a §7.6 attribution from secondary citations as a verified theorem. Diamond–Halberstam, A higher-dimensional sieve method (2008): https://doi.org/10.1017/CBO9780511542909 . Original DHR paper: https://doi.org/10.1016/0022-314X(88)90046-7 . The exact large-κ asymptotic in the book remains unverified here. The analysis uses Richert's explicit fixed-κ statement and an independently derived saddle estimate, not an unverified βκ constant.

## Best prime-tuple constant search — limited negative

Searches for uniform growing-k upper bounds and improvements of 2^k k! located no primary result giving e^{O(k)} in the required range. This is not a proof that no result exists. MathOverflow https://mathoverflow.net/questions/222202/upper-bound-for-the-first-hardy-littlewood-conjecture gives useful historical pointers, but its 2015 claim of best-known 2^k k! is not a current theorem. It explicitly has later discussion of improvements for k=2. We do not claim 2^k k! is universally the best known constant.
