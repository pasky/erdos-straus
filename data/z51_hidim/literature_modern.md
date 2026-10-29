# Modern literature notes: high-dimensional sieve / shifted-factor lane

Source research only; statements below are paraphrases with hypotheses retained. All cited primary sources were opened/read (paper HTML or PDF text).

## Granville–Koukoulopoulos–Maynard: title and smoothed sieve weights

**Correct title:** Andrew Granville, Dimitris Koukoulopoulos, James Maynard, “Sieve weights and their smoothings” (not “Sieve weights and their smoothings” with different authors or a singular “smoothing”). *Ann. Sci. Éc. Norm. Supér.* (4) 54 (2021), no. 5, 1089–1177; arXiv:1606.06781v4 (8 Apr 2020).

- The abstract’s actual subject is asymptotic formulas for the **2k-th moments of partially smoothed divisor sums of μ**. It states the threshold phenomenon: for smoothing level A large compared with 2k the main contribution comes from integers with only large prime factors; past a threshold it instead comes from integers with many prime factors. This is an analysis of candidate sieve weights, not a prime-tuple counting theorem.
- Theorem 1.3, p. 9 of the arXiv PDF (journal pagination approximately pp. 1097–98): for fixed integers k≥1 and A≥0,
  `M_{f_A,2k}(R) = c_{k,A}(log R)^{E_{k,A}} + O((log R)^{E_{k,A}-1})`,
  where `E_{k,A}=max{ binom(2k,k)-2k(A+1), -1 }`. In particular `E_{k,0}=binom(2k,k)-2k`. For `R^{2k}≤x`, formula (1.15) specifically treats the 2kth power of `Σ_{d|n,R/2<d≤R} μ(d)` (not arbitrary smoothing). Implied constants depend at most on k,A: **fixed dimension/ moment order**, not uniform growing k.
- Theorem 1.4: for k≥1, ε∈(0,1), f supported on (-∞,1], and f∈C^A for an integer `A≥2` with f and derivatives through order A bounded, if `A > binom(2k,k)/(2k)=E_{k,0}/(2k)+1`, then the corresponding general smoothed weight `M_f(n;R)^{2k}` behaves like a sieve weight. This is the smoothing threshold highlighted by the authors; the theorem is not a uniform-in-k claim.

Primary URLs: [arXiv abstract/version](https://arxiv.org/abs/1606.06781), [full HTML](https://arxiv.org/html/1606.06781), [PDF](https://arxiv.org/pdf/1606.06781), [journal landing page](https://smf.emath.fr/publications/poids-de-crible-et-leurs-lissages).

## Maynard: “Dense clusters of primes in subsets”

James Maynard, “Dense clusters of primes in subsets,” *Compositio Math.* 152 (2016), no. 7, 1517–1554; arXiv:1405.2593 (2014).

- Theorem 3.1 (paper §3): Let α>0, 0<θ<1, and admissible `L={a_i n+b_i}_{i≤k}` with `1≤a_i,b_i≤x^α`, `k≤(log x)^α`, `1≤B≤x^α`. Assume Hypothesis 1: (i) the base set A is equidistributed on average modulo q≤x^θ with total error `≪ #A(x)/(log x)^{100k²}`; (ii) primes in each `L(A)∩P` satisfy an analogous average progression estimate over q≤x^θ, (q,B)=1; (iii) `#A(x;q,a)≪#A(x)/q`. If `k≥C(α,θ)` and the weighted mean prime density condition `(1/k)(φ(B)/B) Σ_{L∈L}(φ(a_i)/a_i)#P_{L,A}(x) ≥ δ #A(x)/log x` holds with `δ>(log k)^{-1}`, then
  `#{n∈A(x): at least C^{-1}δ log k of L_i(n) lie in P} ≫ #A(x) / ((log x)^k exp(Ck))`.
  Here C depends only on α,θ. Thus dimension can grow as a small power of log x, but all distribution hypotheses themselves have very strong k-dependent error `(log x)^(-100k²)` and constants; this is not an unconditional statement for arbitrary tuples.
- Consecutive-prime variant in the same theorem: when P is all primes, `k≤(log x)^{1/5}`, and all forms have common slope `a≪1` and shifts `|b_i|≤(log x)k^{-2}`, the primes may be required consecutive, with denominator loss `exp(Ck^5)` instead of `exp(Ck)`.
- The theorem produces **some** primes among the k forms, not all k. The introductory HL heuristic says all-k asymptotics for coefficients and k varying slightly with x are speculative; it is not proved by the paper.

Primary URLs: [arXiv abstract](https://arxiv.org/abs/1405.2593), [full HTML v2](https://arxiv.org/html/1405.2593v2), [published paper](https://www.cambridge.org/core/journals/compositio-mathematica/article/dense-clusters-of-primes-in-subsets/B49458BB98CB2D9C93ACF3BB09B4B08D), [Oxford author copy](https://ora.ox.ac.uk/objects/uuid:a08a24aa-e17c-4323-8aea-a1782d68c694/files/m19d2e3b9605819f668974f67909377e6).

## Ford: uniform shifted-prime factor-count upper bound (clarifying scope)

The primary Ford result located is Kevin Ford, “A Hardy–Ramanujan type inequality for shifted primes and sifted sets,” *Lithuanian Math. J.* 61 (2021), no. 3, 323–329 (with corrigendum in vol. 62 (2022), no. 1, 133). Ford’s Theorem 6.2 is reproduced in his 2023 sieve lecture notes (citing this paper): for fixed nonzero integer a, **uniformly for x≥4|a| and every k∈N**,

`#{2+|a|<p≤x : ω(p+a)=k} ≪_a (x/log x) (log_2 x + O(1))^{k-1}/(k-1)!`,

and likewise

`#{2+|a|<p≤x : ω((p+a)/2)=k} ≪_a (x/log x) (log_2 x + O(1))^{k-1}/(k-1)!`.

Here `ω(n)` counts distinct prime factors, `log_2 x=log log x`; the bound is uniform over all k (not merely k≤constant·log log x), with implied constant depending on a. This is an upper-tail / factorization statistic along shifted primes, **not** a uniform upper bound for the number of prime k-tuples. I found no distinct Ford theorem matching “uniform k-tuple upper bound” literally; do not conflate the above result with Selberg-sieve tuple bounds.

Primary URLs: [Ford paper, arXiv](https://arxiv.org/abs/2101.03440), [author PDF](https://www.ford126.web.illinois.edu/wwwpapers/HR_shift.pdf), and [Ford sieve lecture notes, §6.1 / Theorem 6.2](https://ford126.web.illinois.edu/sieve2023.pdf).

## Uniform Hardy–Littlewood hypotheses in growing dimension

William Banks, Kevin Ford, Terence Tao, “Large prime gaps and probabilistic models,” arXiv:1908.08613; primary version read by parent: v3, 12 Aug 2025. The initial research note's journal volume/year was not verified and is withdrawn. This source gives a **named Hardy–Littlewood-type uniformity hypothesis**, rather than a named “uniform Bateman–Horn upper conjecture.”

- Theorem 1.5 (“Hardy–Littlewood implies large gaps”), arXiv PDF pp. 7–8: assume `2 log_2 x/log x ≤ κ ≤ 1/2`, and a set A⊂N satisfies
  `#{n≤x : n+h∈A for every h∈H} = S(H) ∫_2^x dt/(log t)^{|H|} + O(x^{1−κ})`
  uniformly over all tuples `H⊂[0, (log x)^2]` with `|H|≤2κ log x/log_2 x` (notation in source uses `log_2 x=log log x`; S(H) is the singular series). Parent correction: the shift range is log SQUARED, not iterated log. Then the maximal A-gap obeys `G_A(x) ≫ κ (log x)^2/log_2 x` for all large x, absolute implied constant. The allowed cardinality grows up to order `log x/(log log x)` when κ is a fixed positive constant ≤1/2, while the uniform error is `O(x^{1−κ})`.
- Theorem 1.6 (“Averaged Hardy–Littlewood implies large gaps”) instead assumes an averaged version summed over tuple families and sizes as large as `k≤C y/log x`, with `log x≤y≤(log x)^2 log_2 x`;  its conclusion is `G_A(x)≥g((cξ−o(1))log_2 x)`, using the paper’s covering function g. This is an averaged conjectural hypothesis, not pointwise uniformity for each tuple.
- Theorem 1.3 concerns the paper’s **random model R**, not actual primes: for fixed `c∈[1/2,1)` and ε>0, almost surely an HL-type formula with error `O(x^{1−(1−c)/(8c²−2c)+ε})` holds uniformly for admissible `H` with `|H|≤(log x)^c` and `H⊂[0, exp((log x)^{1−c}/log_2 x)]` (parent checked v3, Theorem 1.3; the original note incorrectly squared the iterated logarithm). This is model evidence, not a theorem about primes.

A distinct earlier fixed-k uniformity is Gallagher’s theorem, quoted by Banks–Ford–Tao: if for every fixed k and every c>1 the HL conjecture holds uniformly for admissible `H⊂[0,c log x]`, then normalized prime gaps have an exponential distribution. That condition keeps k fixed first and is not the growing-k theorem 1.5.

Primary URLs: [arXiv abstract](https://arxiv.org/abs/1908.08613), [PDF](https://arxiv.org/pdf/1908.08613), [published article](https://link.springer.com/article/10.1007/s00222-023-01199-0), [Tao’s contemporaneous exposition](https://terrytao.wordpress.com/2019/08/26/large-prime-gaps-and-probabilistic-models/).

## Kubilius model for shifted factorizations

Kevin Ford, “Poisson approximation of prime divisors of shifted primes,” arXiv:2408.03803 (primary source; current version v4 dated 2026 in the search result). This modernizes the Kubilius model for `p+a`.

- Define independent variables W_q over primes q: if q|a then W_q=0; otherwise `P(W_q=v)=1/φ(q^v)−1/φ(q^{v+1})`, i.e. `P(W_q=0)=1−1/(q−1)` and `P(W_q=v)=1/q^v` for v≥1. This is the PNT-AP density for `q^v||(p+a)`.
- Hypothesis Z(γ): for each ε>0 some δ>0 exists such that, for every B≥1 and nonzero a,
  `Σ_{m≤x^{γ−ε}, P⁺(m)≤x^δ, (m,a)=1} |π(x;m,−a)−π(x)/φ(m)| ≪_{B,ε,a} x/(log x)^B`.
  The paper says Z(1/2) follows from Bombieri–Vinogradov, Z(1/2+1/42) from Maynard’s large-moduli result (Cor. 1.2 there), and Z(1) is conjectured (follows from Elliott–Halberstam).
- Theorem 1: under Z(γ), for fixed a≠0, A>0 and 0<α<γ, uniformly for `2≤y≤x`, with `u=log x/log y`, total variation distance between `(W_q:q≤y)` and the vector of valuations `(v_q(p+a):q≤y)` for a uniformly random prime `|a|+1<p≤x` is
  `≪_{a,A,α} exp(−αu log u) + (log x)^{−A}`.
  Implied constant independent of y; γ enters through α<γ and Z(γ). In particular applies to y=x^{o(1)} with u→∞.
- Theorem 2: for any number m of disjoint nonempty prime sets `T_i⊂[2,y]`, the vector of distinct-factor counts `ω(p+a,T_i)` (or multiplicities `Ω(p+a,T_i)`) is within total variation
  `≪_{a,A,α} Σ_i H₂(T_i)/(1+H₁(T_i)) + exp(−αu log u)+(log x)^{−A}`
  of independent Poisson variables with means respectively `H₁(T_i)=Σ_{q∈T_i}1/(q−1)` or `H₁′(T_i)=Σ q/(q−1)^2`. Estimate is explicitly uniform in m and the sets. This is a useful high-dimensional statement with explicit aggregate error.

Primary URLs: [arXiv abstract/version](https://arxiv.org/abs/2408.03803), [full HTML](https://arxiv.org/html/2408.03803), [PDF](https://arxiv.org/pdf/2408.03803), [Ford author-hosted PDF](https://ford126.web.illinois.edu/wwwpapers/Kubiliusshift.pdf).
