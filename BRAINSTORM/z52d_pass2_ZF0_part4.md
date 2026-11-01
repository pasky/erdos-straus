# ZF0 part 4: concrete word, class, order and graph tests

Completed: 9/9 items; ES remains open.
Outcomes: 5 interesting, 4 nothing, 0 covered/skipped/needs-compute.
Interesting: Z2825, Z2836, Z2843, Z2851, Z2881.
Exact scripts and per-item data accompany every computation; no PARI is required.
Positive gamma and HJ-product conventions are distinguished; finite results are CERTIFIED (computer), not unbounded existence theorems.

## Z2836 — fat closure, sparse three-letter extraction

PROVED: fix the actual HJ letters `M(k)=[[k,-1],[1,0]]`, k≥2, not the separate RS alphabet. With `T=R=[[1,1],[0,1]]` and `L=[[1,0],[1,1]]`, `T⁻¹M(k)T=R^(k−2)L`. Thus the full semigroup is the unique positive L/R words ending in L, and its generated group is all SL₂(Z) since it contains L and RL. It is not finitely generated: the words R^a L with one L cannot be composed from shorter such blocks.

In max-entry norm this semigroup has Θ(N²) elements: coprime bottom rows c≥d>0, c≤N, each give a solution 1≤a≤c, 0≤b≤d of ad−bc=1 ending in L, hence Ω(N²); all matrices with bottom row (c,d) have O(1+N/max(c,d)) possibilities, summing to O(N²). The usual critical exponent is half the norm-growth exponent, so **δ=1**, with no thin generated group.

CERTIFIED DFS counts at N=4096,8192 are **10,200,039**, **40,803,219**, giving **δ_eff=1.0000541518645807**. The count of exactly three original HJ letters with max norm n=tuv−u−v≤N is only **80,592**, **197,523**. The conjugated and original norms are comparable but not identical; no finite-bound equality between those height conventions is asserted. Three-letter counts are O(N log²N), so this extraction has limiting norm exponent 1 rather than the closure's 2. Reproduce `gcc -O2 scripts/z52d_p2_ZF0_Z2836_growth.c -o /tmp/zf0_growth; timeout 180s /tmp/zf0_growth`; complete dyadic table is in `data/z52b/pass2/ZF0/Z2836/growth.csv`.

Assessment: the suggested δ=1 premise is true for the full alphabet closure, but does not place the ES fixed-length slice under a fat-semigroup local-global theorem. QUESTION_R explicitly distinguishes self-levelled words from the RS semigroups.

## Z2825 — an explicit same-narrow-class, opposite-sign pair

Fix the **positive** matrix convention `gamma=[[A,p],[t,A*]]`, not the HJ product. Its primitive fixed form is `[t,A*−A,−p]`, discriminant `(A+A*)²−4`. Reduction uses the exact determinant-one substitution `Q(qx−y,x)` with q=ceil((-b+sqrt(D))/(2a)); repeated reduced forms give a canonical primitive minus-CF cycle. The script verifies discriminants and genus-character invariance during reduction. Prime-discriminant characters use a positive represented integer coprime to D.

CERTIFIED: **308 words**, **29 primes p<300, p≡1 mod4**, **11 (D,genus) cells with opposite signs**, **14 negative words in the principal genus**. A particularly decisive PROVED example is
`g13=[[3,13],[2,9]]`, from (t,u,v)=(2,2,5), and
`g17=[[5,17],[2,7]]=R g13 R⁻¹`, from (2,3,4).
Both have trace 12, discriminant 140, and reduced cycle `[(2,−14,7),(7,−14,2)]`; nevertheless `(3/13)=+1` and `(5/17)=−1`. This is stronger than merely matching genera. Also at **p=89, word (7,2,7)**, the fixed form `[7,35,−89]` has D=3717 and all prime-discriminant characters **χ_−3=χ_−7=χ_−59=+1**, while `(13/89)=−1`. Thus choosing a different genus character for that discriminant does not repair the premise.

Reproduce `timeout 180s uv run --with sympy python scripts/z52d_p2_ZF0_Z2825_classes.py`. All forms, cycles, characters and maximal-order extensions are in `data/z52b/pass2/ZF0/Z2825/results.json`.

### Z2845 — source-checked partial-zeta computation

Jun–Lee, *Polynomial behavior of special values of partial zeta function of real quadratic fields at s=0*, arXiv:1111.6717v1, [§3 equation (9)](https://arxiv.org/html/1111.6717v1#S3.E9), gives `Σ[−B1(x_i)B1(x_(i−1))+(b_i/2)B2(x_i)]`. For modulus q=1, x_i=1, so each term is `(b_i−3)/12`. A primitive cycle is essential; the factor 1/6 seen in some cusp formulas uses a different period convention. Independent calibration: Q(sqrt3), principal narrow class, ζ(0)=1/12, since the two narrow values sum to zero and their difference is L(0,χ_−4)L(0,χ_−3)=1/6. Q(sqrt5) has value 0.

To compute **field**, rather than nonmaximal-order, values, factor D=f²D0 and extend I=<a,(−b+sqrt(D))/2> to O_D0. In the basis (1,ω), ω=(s+sqrt(D0))/2, HNF of generators I and ωI computes this extension exactly; then reduce its primitive norm form. The same script tabulates all 308 values. For all **28 nonempty prime fibres**, neither summing with word multiplicity nor summing once per distinct associated narrow class gives the sign sum. At p=13 these candidates are **5/6, 5/12**, against **0**; at p=17 they are **1/2, 1/4**, against **−2**. This rejects those precise natural unweighted identities, not arbitrary unspecified weights.

## Z2843 — explicit Ibukiyama-order embeddings and a real small-q filter

Source checked: Ibukiyama, *On maximal orders of division quaternion algebras over the rational number field with certain optimal embeddings*, Nagoya Math. J. 88 (1982), pp.181–195, [original PDF](https://projecteuclid.org/journalArticle/Download?urlid=nmj%2F1118787011). The introduction and Lemma 1.4 give the basis
`1, (1+β)/2, α(1+β)/2, (r+α)β/q`,
with α²=−p, β²=−q, αβ=−βα, q≡3 mod8, (−q/p)=−1, r²≡−p modq. These are not all maximal orders: the theorem exhausts those with the specified optimal embedding of Z[sqrt(−p)], with the separate O′ family when p≡3 mod4.

A trace-zero vector has coordinates `(C,B,K)/(2q)` along `(α,β,αβ)`, where C=qc, K=qc+2d, B=2qh+2rd for integers c,d,h. Its norm is `(pC²+qB²+pqK²)/(4q²)`. Exhaustive norm-shell enumeration follows from `|c|≤sqrt(4n/p)` and `|K|≤sqrt((4qn−pqc²)/p)`; B is then an integer square root with a residue check. No arbitrary coefficient box or floating test is used. An embedding is a pair of norms d,m with weighted dot product −2q², equivalent to uv+vu=1. Pairs are streamed, not Cartesian arrays.

CERTIFIED: all **45 odd primes p<200**, q<1000, **969 explicit maximal orders**, **720 distinct Λ_(d,ab)** induced by all Type-I tuples from `bsC_common.typeI_all(199)`, **14,937 tests**, **2,083 successful embeddings**, **387 distinct targets covered**, **44 primes covered**. Every basis is checked closed under multiplication with trace-Gram determinant −p²; every success satisfies u²=−d, v²=−m, uv+vu=1 and the generated lattice has exact index **e=(4dm−1)/p**.

The least Type-I level survives at **39 primes**. It rises at **73:3→23, 97:7→15, 113:3→7, 131:1→5, 179:1→5**; at **p=193** no tested q hosts any of `(d,m,e)=(5,29,3),(29,5,3),(26,13,7),(10,690,143)`. This last statement is only for q<1000, not a nonembedding theorem for every maximal order. The preliminary q<100 search covered 195 targets at 42 primes; increasing to 1000 resolves p=11 and 131 but not 193. Runtime about 12 seconds, largest individual norm shell 112 vectors.

Reproduce `timeout 600s uv run --with sympy python scripts/z52d_p2_ZF0_Z2843_ibukiyama.py`. `data/z52b/pass2/ZF0/Z2843/results.json` contains the complete per-prime/per-q tests, uncovered targets and integer basis coordinates for every embedding. Assessment: selecting an explicit small-q order is a genuine restriction, not the vacuous existential-maximal-order statement; its arithmetic cost is visible even in this small sample.

## Z2881 — factorization genera neither select words nor determine signs

CERTIFIED enumeration covers **484 (p,t)** with p<500, p≡1 mod4 and 2≤t≤12: **12,819 primitive reduced positive forms**, of which **1,779 ambiguous**. Reduced forms satisfy |b|≤a≤c, b≥0 on the boundary, gcd(a,b,c)=1; ambiguity is exactly b=0, |b|=a or a=c. The literal word factorization gives `[A,0,A*]`, but it is primitive only when gcd(A,A*)=1. Of **231 unordered word factorizations**, **155 are primitive**, **76 imprimitive**. For example p=13,t=2 gives `[3,0,9]`, whose primitive class has discriminant −12, not −108.

There are **17 levels with words in multiple genera**, and **66 genus cells containing both word and nonword ambiguous classes**. Explicitly p=37,t=7,N=260,D=−1040: `[13,0,20]` is a word (A,A*≡−1 mod7), while `[5,0,52]` is not; both have characters `(χ5,χ13,χ−4)=(−1,−1,+1)`.

The sign also fails to descend, even with **the same p,t**: p=457,t=2,N=915,D=−3660 has word forms `[3,0,305]` (u,v)=(2,153) and `[5,0,183]` (3,92). Both have `(χ−3,χ5,χ61)=(−1,−1,+1)`, but `(3/457)=+1` and `(5/457)=−1`. These prime-discriminant characters generate the genus-character group, so a different product does not fix this. This is the discriminant −4N experiment, distinct from the known genus encoding at discriminant −4tp.

Reproduce `timeout 180s uv run --with sympy python scripts/z52d_p2_ZF0_Z2881_ambiguous.py`; complete counts, word genera and collisions are in `data/z52b/pass2/ZF0/Z2881/results.json`. Assessment: content and residue data are indispensable, and the proposed ambiguous-class language alone loses both.

## Z2851 — the four-vertex relaxation has no failures below 20,000

Use edges `(a,b,c,d,e,f)=(01,02,03,12,13,23)` and reduced Laplacian
`L=[[a+d+e,-d,-e],[-d,b+d+f,-f],[-e,-f,c+e+f]]`.
If `det L=p` is prime, the critical group is cyclic of order p; any nonzero diagonal cofactor h modulo p gives a generator with pairing h/p. Hence `(h/p)=-1` is an exact certificate. This is the pairing of `bsA_selling_sandpile.md` D3, without its fan restriction.

Search all edge weights 0..30 with a≤b≤c (a vertex-permutation reduction): **162,539,696 graphs**, **2,858,722 odd-prime determinants below 20,000**, **2,261/2,261 odd primes covered**, no failures. This includes all **267 primes ≡1 mod24**. Witnesses in `data/z52b/pass2/ZF0/Z2851/witnesses.csv` use maximum weight 30. One may stop at this bounded subset because every target has a positive certificate; no absent-target inference from a weight cutoff is made.

Reproduce: `gcc -O2 scripts/z52d_p2_ZF0_Z2851_graphs.c -o /tmp/zf0_graphs`, then `timeout 180s /tmp/zf0_graphs 30`; independently verify with `timeout 60s uv run --with sympy python scripts/z52d_p2_ZF0_Z2851_verify.py`. Verification recomputes determinants, cofactors and Legendre symbols with SymPy and checks that the prime list is complete. Assessment: the relaxed graph rung appears much easier than selecting the ES fan shape, but this finite result proves nothing about unbounded p or ES itself.
