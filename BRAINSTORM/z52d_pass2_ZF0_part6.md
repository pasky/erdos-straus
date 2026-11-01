# ZF0 part 6 — first-step audits

Completed: 9 items — 3 interesting, 6 nothing, 0 covered/skipped/needs-compute.
Interesting: Z2561 (count versus positivity bias), Z2901 (explicit BM threshold), Z2797 (norm-aware cap improvement).
All records: `data/z52b/pass2/ZF0_part6.jsonl`; remaining item audits are in their `ZF0/<mid>/audit.md` files.
Finite computations, exact identities and conditional consequences are labelled separately; all outputs validate.
ES remains OPEN; no certificate-existence theorem is claimed.

## Z2561 — divisor count is nearly parity-blind; its positivity is not

**EVIDENCE.** `Z1996` is not a separate result in pass2: `git grep Z1996 -- data/z52b/pass2` finds only citations. The actual `data/z52b/pass1/outcome_U03.jsonl:75` reports *slice success*, pooled over C, at 0.051 vs 0.052, not correlation of the number of divisors in class 3 mod 4. It cannot justify the pass1 conclusion for this item.

For odd N, write D(N)=#{d|N:d≡3 (4)}=(τ(N)−Σ_{d|N}χ₄(d))/2. The C sieve computes τ, the character divisor sum and λ exactly to 100,000,000; it independently checks the divisor count by brute force for every odd N≤10,000. APs are selected before the moments are computed.

| population | size | E[D|λ=+1] | E[D|λ=−1] | Pearson(D,λ) | P(D>0|+) | P(D>0|−) |
|---|---:|---:|---:|---:|---:|---:|
| N≡1 (4), N≤10⁷ | 2,500,000 | 3.639286657 | 3.619329499 | .002232869 | .716250230 | .632410748 |
| N≡1 (4), N≤10⁸ | 25,000,000 | 4.208189729 | 4.201716357 | .000601504 | .728037909 | .662503349 |
| N≡1 (24), N≤10⁸ | 4,166,667 | 2.465942841 | 2.459666454 | .000935089 | .591634174 | .494157954 |
| N≡1 (840), N≤10⁸ | 119,048 | 1.628804614 | 1.602209390 | .006116749 | .559735595 | .386258264 |
| N=4p+1, 3≤p≤12,499,999 prime | 818,702 | 5.310110139 | 5.293752317 | .001332936 | .798315874 | .754937260 |

The residue-matched classes 121,169 mod 840 also have positivity rates ≈.559 vs .386, so this is not peculiar to class 1. At p≡1 (24), D(4p+1) has positivity .59417 vs .51443; at p≡1 (840) the smaller sample reverses it (.38039 vs .51824). No universal parity bias is inferred.

For the 818,702 primes, C=1,C′=2 gives E[λ(4p+1)λ(8p+1)]=−.000439720, E[D(4p+1)D(8p+1)λ(4p+1)λ(8p+1)]=−.052668737. E[D₁D₂]=19.791826574 and Cov(D₁,D₂)=−9.510664646: local dependencies of the two forms matter. D at C=2 still means divisors 3 mod 4, NOT the actual class 7 mod 8 certificate count.

**Exact needed formulation / Assessment.** For L_C(n)=4Cn+1, n≡a (q), one needs prime-restricted, divisor-weighted correlations
Σ_{n≤X,n≡a(q)} Λ(n) W_C(L_C(n))W_C′(L_C′(n))λ(L_C(n))λ(L_C′(n)),
with W=D, or W=1[D>0] for positivity, and an error smaller than the appropriate untwisted count after local main terms are removed. For actual certificates replace D by D_{4C}⁻; uniformity in C,C′ is an additional requirement. Ordinary unweighted Chowla for fixed affine forms, even if proved, gives neither the prime restriction nor these divisor/indicator weights. The determinant of the distinct forms is 4(C−C′)≠0. The claimed OAI result is not treated as established.

Reproduce: `gcc -O2 -Wall scripts/z52d_p2_ZF0_Z2561_correlation.c -lm -o /tmp/z52d_Z2561`; `ulimit -v 8000000; timeout 600s nice -n 10 /tmp/z52d_Z2561 100000000`. Full moments and resource log: `data/z52b/pass2/ZF0/Z2561/`.

## Z2901 — an explicit unconditional BM threshold

**PROVED relative to Treviño's explicit Burgess theorem; conservative constants, not optimal.** For every prime p≥10^1000,
M_BM(p) ≥ [3/(32π²)](log p)².
This is only a main-term lower bound, not ES or the one-sided remainder hypothesis H⁻_BM.

Full text downloaded from https://arxiv.org/pdf/1412.3062. Theorem 1/Table 1 gives |Sχ(M,N)|≤c₁(r)N^(1−1/r)p^((r+1)/(4r²))(log p)^(1/r), all N≥1, with c₁(10)=1.2562 for p≥10²⁰; Corollary 1 gives 2.74 for every r and p≥10⁷. Theorem 2 alone restricts N≤2p^(1/2+1/(4r)), so it does NOT by itself cover the entire hyperbolic sum. Corollary 2 removes that restriction for r≥3; Table 3 gives c₂(10)=1.5216 for p≥10²⁰ with log exponent 1/(2r). These bounds apply to a nonprincipal Legendre character for all offsets and lengths.

Put L=log p, g=sup_{t≤p}|Σ_{n≤t}χ(n)/n|, r=10. Partial summation at H=[c₂(r)(1+1/r)]^r p^((r+1)/(4r))√L gives
 g ≤ .275L + .5log L + 1+r+r log(c₂(r)(1+1/r))
   = .275L + .5log L + 16.1507259262.
Indeed the harmonic initial segment is ≤log H+1 and the Burgess tail is ≤(r+1)c₂p^((r+1)/(4r²))L^(1/(2r))H^(−1/r)=r. All lengths Y_u/d in BM_CORRECTED_COUNT Theorem 2.2 are ≤p/8, so this range suffices. This does not claim T(p)=o(L²): the proof uses positivity and the restricted pair family, just as that theorem does.

Here are explicit replacements for its O(1) terms. For X≥1, A=4/π², B=6/π²,
 S₁(X)=Σ_{u≤X,odd}φ(u)/u² ≥ A log X−3,
 Sκ(X)=Σ_{u≤X,odd}κ(u)/u ≤ B log X+3.
Proof: H_odd(t)=.5log t+c₀+E(t), c₀=(γ+log2)/2<.636, |E(t)|≤1/t. Expand φ/u=Σ μ(d)/d and κ=Σ μ²(d)/d over odd d. The error from E is ≤(1+log X)/X≤1; the lower S₁ bound loses at most .5Σ(log d)/d²<.5, c₀ζ(2)<1.047, and the tail of .5log X Σ μ(d)/d² at most log X/X≤1/e. Their sum is <3. For Sκ the negative log d term can be dropped and the remaining error is <3. The residues are Σ_{d odd}μ(d)/d²=8/π² and Σ_{d odd}μ²(d)/d²=12/π².

Choose X=√(p/8), so Y_u/u≥1. Möbius inversion of the harmonic sum gives Σ_{v≤Y_u,(u,v)=1}1/v ≥ (φ(u)/u)log Y_u−κ(u): the positive γ and prime-log terms can be dropped and the harmonic remainder costs ≤Σ_{d|u}|μ(d)|/d. Partial summation of S₁, followed by the swap factor in Theorem 2.2, gives the fully explicit bound (ℓ=L−log8)
 M_BM(p) ≥ { (3A/8)ℓ² −3ℓ −(g+1)[(B/2)ℓ+3] }/4.

**Numerical evaluation (EVIDENCE for the crossing; analytic safe threshold).** The right side first exceeds 3L²/(32π²) near L=345.5151014, i.e. p≈10^150.0553; this root is not advertised as a rigorously optimised threshold. At p₁=10^1000 the bound is 0.01593711494 L², safely above 0.009498860967 L². To verify all larger p without trusting a floating-point root, for L≥2300 use ℓ≥.999L, g+1≤.285L, 3ℓ≤3L, and (B/2)ℓ+3≤(.304+3/2300)L<.306L. Since 3A/8>.1519, the coefficient is ≥(.1519·.999²−3/2300−.285·.306)/4>.0157>.0095>3/(32π²). The bound on g is monotone after dividing by L and holds already at L=2300.

Reproduce: `timeout 20s uv run python scripts/z52d_p2_ZF0_Z2901_threshold.py`. Full text and evaluation: `data/z52b/pass2/ZF0/Z2901/{trevino.txt,threshold.json}`. No finite prime census to p₁, and no explicit remainder bound, is supplied.

## Z2797 — a norm-aware improvement, not a reverse-Minkowski shortcut

**PROVED relative to cited transference theorems; conditional cap improvements retain all original arithmetic hypotheses.** Restate Λ={x∈Z^k:∏_{s∈S}(s²)^x_s=1 mod q}, N=(q−1)/2, H=U_q, detΛ=N. Its dual modulo Z^k is the character group; Δ=λ₁^(1)(Λ*)=min(1,D_min). BALANCED_LATTICE Proposition 1.3 uses μ∞≤μ₂≤k/(2λ₁^(2)) and λ₁^(2)≥Δ/√k, giving L_min≤ceil(k^(3/2)/Δ).

**Finite recomputation (CERTIFIED character enumeration, numerical square roots avoided in the final improved ceiling).** At the two worst-case examples in BALANCED_LATTICE §6:

| q | S | Δ | old cap ceiling | cap using exact Euclidean dual minimum |
|---|---|---|---:|---:|
| 237971 | 3,5,7 | 141/118985 | 4385 | 3710 |
| 423883 | 3,5,7,11,13 | 1967/211941 | 1205 | 775 |

The last column is ceil(k/λ₁^(2)), still using the all-dimension k/2 Banaszczyk constant. The exact squared minima are 9261/14157430225 and 207839/4990998609 respectively. These are sufficient caps, not actual L_min and not ES certificates.

**Best verified Euclidean asymptotic constant.** Aggarwal–Stephens-Davidowitz, arXiv:1907.09020, Theorem 1.2, gives μ₂λ₁^(2)<(0.1275+o(1))k, improving Banaszczyk's asymptotic (1/(2π)+o(1))k. Hence the corresponding generic cap is (0.255+o(1))k^(3/2)/Δ. The paper expressly leaves o(1) unspecified; substituting .255 at k=3 or 5 is NOT a certified numerical threshold. We do not do that (the JSON reports those leading factors only with this warning).

**Stronger dimension dependence already follows from the correct norms.** Banaszczyk's 1996 Lemma 3, reproduced as Lemma 2.1 in Banaszczyk–Litvak–Pajor–Szarek, *The flatness theorem for non-symmetric convex bodies via the local theory of Banach spaces*, states μ(K,Λ)λ₁(H,Λ*)≤C₀ℓ(K)ℓ(H), with universal C₀ and Gaussian second moments ℓ. Use the cube K=B∞^k and its polar H=B₁^k. Direct Gaussian estimates give ℓ(K)≤√(2log(2k)+2), ℓ(H)≤k, hence
 L_min ≤ ceil(2C₀ k√(2log(2k)+2)/Δ).
This is O(k√log k)/Δ, not k^(3/2)/Δ. The constant C₀ is not explicit in the source, so it improves asymptotic thresholds but gives no further certified small-k number.

Thus BALANCED_LATTICE Corollary 1.4(b) improves from k^(C+3/2)N^(1/k) to O(k^(C+1)√log k)N^(1/k). Keeping its original GRH+EQ argument and its 1/ε≤y^(5+o(1)), Theorem 4.1's exponent becomes 6+o(1), rather than 13/2+o(1). Keeping GRH+S and 1/ε=y^(3+o(1)), Theorem 4.2 becomes 4+o(1), rather than 9/2+o(1). These are **CONDITIONAL** cap≥1 statements, NOT ES; neither EQ nor S is proved here. The underlying norm-aware transference is classical, not a new lattice theorem.

**Why R–SD is not a replacement constant.** The fully read Theorem 1.5 of arXiv:1611.05979 gives μ₂(Λ)≤10(log k+10)^(3/2)μ_det(Λ), with μ_det=max_{M⊆Λ*}√rank(M) det(M)^(−1/rank(M)). It controls ALL dual sublattice determinants, not just λ₁ or Δ. From Δ alone, Minkowski plus an inscribed cube gives det(M)^(1/j)≥λ₁^(2)/√j, hence μ_det≤k/λ₁^(2)≤k^(3/2)/Δ. Plugging this in yields a cap at most 20(log k+10)^(3/2)k^(3/2)/Δ, worse than Proposition 1.3. Better determinant information could help but is not supplied by the character-minimum hypothesis. The R–SD result concerns Euclidean covering radius and must not be applied directly as an ℓ∞/ℓ¹ constant.

Sources: `data/z52b/pass2/ZF0/Z2797/{rsd.txt,aggarwal.txt,flatness.txt,banasz1996_metadata.txt}`. Reproduce the finite computations: `ulimit -v 8000000; timeout 120s nice -n 10 uv run --with sympy python scripts/z52d_p2_ZF0_Z2797_lattice.py` (one character at a time, no O(N²) allocation). The source paper's Lemma 2.1 and §5 explicitly discuss the cube's k√log k Gaussian product.
