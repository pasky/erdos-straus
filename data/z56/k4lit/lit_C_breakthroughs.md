# Lit-C: 2018–2026 parity-breaking / Type II results in thin or multiplicatively constrained settings — what can feed P(4,15)?

Target: **P(4,15)**: infinitely many primes p ≡ 1 (mod 8) with p+4 ∈ S and 4p+1 ∈ S
(S = {n : every prime factor ≡ 1 mod 4}). Equivalent: lattice points of the det-15 shell
(det M = 15, ‖M‖² = 16p+34). Det-1 analogue: p−2, p+2 sums of two squares (Friedlander–Iwaniec hyperbolic PNT).

Method: arXiv API + PDFs of every paper below, pulled 2026-11-04 (text extracted with pypdf).
"VERIFIED" = statement quoted from the PDF or the arXiv abstract. "UNVERIFIED" = not read from source.
arXiv IDs 26xx.xxxxx are 2026 preprints. Most are v1 and have not been refereed.

---------------------------------------------------------------------------------------------------
## 0. THE SINGLE MOST IMPORTANT FINDING

**I found no paper (to Nov 2026) that unconditionally proves infinitely many primes p with two shifted
values both sums of two squares.** That covers p±2, p+4 & 4p+1, and p−1 & p+1.
The latest status statements, all read in the sources:

* **Sedunova, "On the hyperbolic prime number theorem", arXiv:2609.28200 (Sep 2026)**. This is exactly the det-1 analogue.
  The abstract says: "Friedlander and Iwaniec proved that the number of points of the orbit {γi : γ∈SL2(Z)} lying at a
  distance p−2 from the origin … with p≤x prime, is of order x/log x; the upper bound is unconditional, while
  the lower one rests on a strong hypothesis concerning the distribution of primes in arithmetic progressions."
  The paper states FI's hypothesis as Conjecture 1 (A(θ)): a BV-type remainder bound at level Q = x^{θ−ε}. It says
  "By [2] we have π_Γ(x) ≍ x/log x provided that A(θ) holds for some θ<1 sufficiently close to 1".
  Unconditional results: **Thm 1** s_Γ(x) = 6Cx + O(x^{11/12+ε}) (square-free distances) and **Thm 2** s^{(7)}_Γ(x) ≫ x/log x
  (≤7 prime factors). Theorem 2 rests on the level of distribution x^{1/6−ε} of r(n−2)r(n+2) (Lemma 2).
  **Conjecture 2 (R(θ))** is the level of distribution of r(n−2)r(n+2) in APs.
  **Thm 3**: R(θ) ⇒ s^{(⌊2/θ⌋)}_Γ(x) ≫ x/log x, and "R(1/2) implies s^{(4)}_Γ(x) ≫ x/log x".
  Remark 1: "the number 7 is not improved by any rearrangement of the sieve, only by a larger level of distribution."
* **Shparlinski–Xiao, "Arithmetic structure of L2-norms of SL2(Z) matrices", arXiv:2609.21460 (Sep 2026)**, abstract:
  the asymptotic for square-free R(γ)=Σa_i² has error O(X^{19/10+o(1)}). R(γ) "is squarefree and has at most 9 prime
  divisors for at least cN(X)/log X matrices". It calls the FI prime result "conditional on a very strong form of
  the Elliott–Halberstam conjecture".
* **Nath–Xie, "Almost primes and primes that are sums of two squares plus 1", arXiv:2501.16723**.
  **Thm 1.1**: #{p≤x : p = m²+n²+1, Ω(p+2) ≤ 9} ≫ x/(log x)^{5/2} (vector sieve: semi-linear + linear, plus
  Iwaniec switching). Remark 1.1: under an EH variant, Ω(p+2) ≤ 3. The intro (p.2) states:
  "We still do not have an asymptotic formula for the number of primes of the form p = m²+n²+1 up to any positive real
  number x unconditionally". The lower bound ≫ x/(log x)^{3/2} is Iwaniec's (semi-linear sieve).
  → This is the published analogue of our internal "one shift in S, the other with bounded factors" result.
  The best known result is still of the "bounded number of prime factors" type.

So P(4,15), and even its det-1 analogue, is open. The best unconditional results are almost-prime results limited by Type I level.

---------------------------------------------------------------------------------------------------
## 1. Summary table

| # | Paper (arXiv) | Setting | Mechanism for Type II / parity | Feeds P(4,15)? |
|---|---|---|---|---|
| 1 | Green–Sawhney 2410.04189 | primes x²+ny², x,y prime | Gowers-norm control of coordinate weights f(x)f'(y) via concatenation + quasipoly inverse thm | **No** (needs product weights in coordinates; our weights are radial) |
| 2 | Merikoski 2112.03617 | a²+(b²+1)², a²+(c³+d³)² | Heath-Brown device → counting problem → Weil bound; Harman sieve | **No** (prime = norm; our internal obstruction) |
| 3 | Merikoski 2302.11331 (Compositio 2025) | a²+b², b∈B sparse | Hecke L-functions on Q(i), zero-density | No (same) |
| 4 | Pratt 1806.02699; HB–Li 1504.00531; Maynard 1507.05080 | thin coordinate / incomplete norm forms | FI-type Type II + digit Fourier / geometry of numbers | No (same) |
| 5 | **Grimmelt–Merikoski–Pandey–Pascadi 2610.41356** | primes n²+h, almost all h | C–S → binary quadratic forms n₁r₂²−n₂r₁², Voronoi in h-average; Γ₀(d) spectral Type I₂ | **Indirect, medium**: closest template for a *shell* Type II; needs averaging over the shift/determinant |
| 6 | Grimmelt–Merikoski 2505.00489 / 2505.00493 / 2404.08502 | SL2(R) automorphic kernel averages | spectral methods on the kernel directly | **Medium (Type I only)**: tool to raise Sedunova's R(θ)=1/6 for shell sequences |
| 7 | Sedunova 2609.28200; Shparlinski–Xiao 2609.21460 | det-1 shell (hyperbolic PNT) | linear sieve + level of distribution | Status report: still conditional |
| 8 | **Lü–Wang–Wu 2610.20242 (v1, Oct 2026)** | claims Σ_p μ(p+2)=o(π(x)) | small-prime weights W + C–S in cofactor h → determinant equation bmn−ars=2(a−b) → "prime-list operator" moments | **Potentially high if correct; UNVERIFIED and doubtful** (see §3.8) |
| 9 | Lichtman 2009.08969; Lichtman–Teräväinen 2111.08912 | μ / non-pretentious f at shifted primes, on average over shift | MRT averaged Chowla + sieve | Only for averaged shifts; needs non-pretentious f |
| 10 | Tao–Teräväinen 1708.02610, 1809.02518; Teräväinen 1710.01195; Klurman–Mangerel–Teräväinen 2304.05344; Helfgott–Radziwiłł 2103.06853; Pilatte 2310.19357; Tao–Teräväinen 2512.01739 | log-averaged / almost-all-scale correlations of multiplicative functions | entropy decrement / expanders / structure theorems | No Λ in the correlation → not applicable to the prime variable |
| 11 | Matomäki–Teräväinen 2207.05038; Teräväinen 1510.06005; MPPTW 2610.09567 | E₂/E₃ in (almost) all short intervals | Dirichlet-polynomial Type II (Heath-Brown sparse MVT, large values) | No (short-interval Type II, no additive shift structure) |
| 12 | Lichtman 2309.08522; Pascadi 2505.00653; Stadlmann 2309.00425; Lichtman 2211.09641 | primes in APs beyond x^{1/2} | Deshouillers–Iwaniec spectral large sieve, triply-well-factorable weights | **Medium**: improves "bounded # of 3 mod 4 factors", cannot reach exact S alone (parity / fixed residue) |
| 13 | Fouvry–Radziwiłł 1811.08672, 1812.00562; Green 1604.04481; Granville–Shao 1703.06865; Drappeau–Topacogullari 1807.09569 (ANT 2019) | multiplicative f (incl. 1_S) in APs beyond x^{1/2} | Linnik dispersion + Bettin–Chandee / DFI Kloosterman-fraction bounds | **Medium-low**: S-side level >1/2 exists but only with a weak log saving (FR) or with τ, not primes (DT) |
| 14 | Kimmel–Kuperberg 2306.12855, 2406.04174 | consecutive S-numbers in APs | Maynard–Tao sieve style | No (no primes) |
| 15 | Banks 2610.15483 (on the "OpenAI proof" that Landau–Siegel zeros do not exist) | exceptional zeros | — | Removes the Siegel-zero conditional parity-breaking route (Heath-Brown, Tao–Teräväinen, Matomäki–Merikoski 2112.11412) |

---------------------------------------------------------------------------------------------------
## 2. Per-paper verified quotes and mechanism

### 2.1 Green–Sawhney, "Primes of the form p² + nq²", arXiv:2410.04189 (v3 Jun 2026). Journal: UNVERIFIED
**Thm 1.1** (verified): for n ≡ 0 or 4 mod 6, W ∈ C_0^∞(R²),
Σ_{x,y} Λ(x)Λ(y)Λ(x²+ny²) W(x/N, y/N) = κ_n N² ∫W + O_{W,n}(N²(log log N)²/log N).
"In particular … infinitely many primes of the form x²+ny² with x, y prime." For n=4 this proves FI's Gaussian primes conjecture.
**Mechanism**: Type I/II in Z[√−n] for w(x+2iy)=f(x)f'(y). A Duke–Friedlander–Iwaniec sieve needs "Type I information up to
level X^{1/2−o(1)}, and Type II information up to X^{1/3−o(1)}". Both are derived from smallness of Gowers norms of
f = Λ − Λ_Cramér (Prop. 4.2 / 4.3), via quantitative concatenation (Kuca; Kravitz–Kuca–Leng) and Leng's
log-power Gowers bounds (from Leng–Sah–Sawhney). Type I at level X^{1/2} is "an interesting open question".
**Relevance**: the method needs a **coordinatewise product weight** f(x)f'(y) on a Gaussian integer whose **norm is the
prime**. In P(4,15) the prime is N(z)−4 (and (N(z')−1)/4), so the weight 1_P(N(z)−4) is radial, not a coordinate product.
In the shell picture the condition is p = (‖M‖²−34)/16, again quadratic in the coordinates. There is no factorization
of the prime in a number field, so the Type I/II split happens in Z, not in Z[i]. **Not applicable.**

### 2.2 Merikoski, "The polynomials X²+(Y²+1)² and X²+(Y³+Z³)² also capture their primes", arXiv:2112.03617
**Thm 1**: Σ_{p≤X} Σ_{p=a²+(b²+1)²} 1 ≍ X^{3/4}/log X. **Thm 2**: ≍ X^{5/6}/log X for a²+(c³+d³)², c,d>0.
**Thm 3**: primes a²+N(b_1..b_{k−1})² for an incomplete norm form (k large, Galois K).
**Mechanism** (§1.1): Type I up to D ≤ X^{3/4−η} (large sieve for roots of quadratic congruences). Type II only for
X^{1/4+η} ≪ N ≪ X^{1/3−η}, which is "not sufficient for an asymptotic formula", so Harman's sieve is used. Type II goes through
a Heath-Brown device, then a counting problem, then the Weil bound.
**Relevance**: the prime is again a Gaussian norm with a thin coordinate. This is covered by our proved obstruction
(the family cannot confine both shifts). The transferable idea is Harman's sieve with a *narrow* Type II range;
§3 explains why that matters.

### 2.3 Merikoski, "On Gaussian primes in sparse sets", arXiv:2302.11331, Compositio Math. 161 (2025) 181–243
**Thm 1.1**: there is δ>0 such that if |B∩[0,Y]| ≫ Y^{1−δ} then there are infinitely many primes a²+b² with b∈B.
**Thm 1.2**: Σ_{p=a²+b²≤X} 1_B(b) ≫_ε X^{1/2−ε}|B| for B ⊆ [ηX^{1/2},(1−η)X^{1/2}], |B| ≥ X^{1/2−δ}.
Mechanism: zeros of Hecke L-functions on Q(i). Relevance: none beyond §2.2.

### 2.4 Pratt 1806.02699; Heath-Brown–Li 1504.00531; Maynard 1507.05080; FI a²+b⁴
* Pratt **Thm 1.2**: an asymptotic for Σ_{m²+ℓ²≤x, (ℓ,Π)=1} 1_{A'}(ℓ)Λ(m²+ℓ²), where ℓ misses ≤3 fixed digits.
* HB–Li **Thm 1**: #{a²+p⁴ ≤ x prime} = ν·4J x^{3/4}/log²x (1+O_ε((log x)^{−1+ε})). They also prove equidistribution of primes
  "in which the moduli may be almost as large as x²" (abstract). Journal per brief: Invent. 2017 (UNVERIFIED).
* Maynard **Thm 1.1**: the expected asymptotic for prime values of incomplete norm forms if n ≥ 4k. **Thm 1.2**: ≫ for
  K=Q(θ^{1/n}), n ≥ 22k/7. Forum Math Pi 2020 per brief (journal UNVERIFIED).
All of these are norm forms with a thin coordinate, so the same obstruction applies. Not applicable.

### 2.5 Grimmelt–Merikoski–Pandey–Pascadi, "Primes and the Möbius function over quadratic polynomials", arXiv:2610.41356 (v1 Oct 2026)
**Thm 1.1**: for H = X^{1/2−ν}, Σ_{n²+h≤X} Λ(n²+h) = (1+O(ν)) S_h X^{1/2} for all but ≪_C H/(log X)^C values of h ≤ H.
**Thm 1.2**: for X^{2/5} ≤ H ≤ X/2, Σ Λ(n²+h) ≥ 0.098 S_h (X−h)^{1/2} for almost all h. The paper calls this "the first time that primes
have been detected in a thin polynomial sequence which does not factor over number fields".
**Thm 1.3**: Σ_{h≤H} |Σ μ(n²+h)| = o(HX^{1/2}) for H = X^{1/2−o(1)}.
**Mechanism** (§1.1): Harman sieve with Type I, Type I₂ (τ(r²+h) at level X^{ν+η}, via spectral methods on Γ₀(d), from [GM 2505.00489/00493]),
and Type II for X^{ν+η} < N < X^{−η}H^{1/2}. "An application of Cauchy–Schwarz on m creates a binary quadratic form
n₁r₂² − n₂r₁² whose representation counting function is morally like a Fourier coefficient of a GL(2) modular form of
conductor ≍ N². Another application of Cauchy–Schwarz on the h-average creates smooth sums that allow us to use
Voronoi summation." "Our Type II estimate is non-trivial as long as H ≥ X^{1/3+ε}." There is "a hard barrier at 1/3".
**Relevance (medium/indirect)**: this is the first success at breaking parity in a sequence that does not factor. The sequence is the
values of a quadratic, which is close in spirit to the shell sequence a_n = #{M : det M=15, ‖M‖²=16n+34}. It is also the
right toolbox (binary forms, Voronoi, Γ₀(d) spectral theory). **But the parity break comes from averaging over the shift h.** A
P(4,15) analogue would average over the determinant (det M = h) or over the shift, whereas the Erdős–Straus identity
needs the fixed pair (4,15). Usable only if an *averaged-over-det* statement is enough downstream.

### 2.6 Grimmelt–Merikoski: SL2(R) automorphic-kernel averages (2505.00489), greatest prime factor of n²+h (2505.00493), twisted divisor correlations (2404.08502)
2505.00489 abstract: "evaluates weighted averages of sums parametrised by congruence subgroups of SL2(Z) … spectral methods
are applied directly to the automorphic kernel instead of going over sums of Kloosterman sums".
2505.00493: P⁺(n²+h) ≥ n^{1.312} infinitely often, unconditional, uniform in h ≤ n^{1+o(1)} under a hypothesis on real characters.
**Relevance**: these are the natural tools for the **Type I side of the shell**. Sums over {M ∈ Mat₂(Z): det M=15, d | (‖M‖²−34)/16}
are sums over Hecke-translated Γ₀(d)-orbits. This could raise Sedunova's R(θ) from 1/6 (§0). It does not break parity.

### 2.7 Fouvry–Radziwiłł, "Level of distribution of unbalanced convolutions", arXiv:1811.08672
**Cor 1.3** (verified): let g be multiplicative with |g(n)| ≤ τ_k(n), and suppose n ↦ 1_{n prime}·g(n) is Siegel–Walfisz.
Then uniformly for Q ≤ x^{17/33−ε} and 1 ≤ |a| ≤ x/12:
Σ_{Q<q≤2Q, (a,q)=1} | Σ_{x<n≤2x, n≡a(q)} g(n) − (1/φ(q)) Σ_{(n,q)=1} g(n) | ≪_ε x/(log x)^{1−ε}.
(The PDF text reads "x(logx)1−ε". In context it is a saving: "we are saving k powers of the logarithm" for τ_k.)
"It is likely that if we could replace (log x)^{1−ε} with (log x)^{1+ε} … interesting consequences for prime numbers would ensue."
Mechanism: Linnik dispersion for α*β with β tiny and Siegel–Walfisz, plus Bettin–Chandee trilinear and DFI bilinear Kloosterman-fraction bounds.
Companion 1812.00562: "narrow" Type II (M = X^{1/2−δ}, N = X^{1/2+δ}) has exponent of distribution 1/2+δ−ε.
**Relevance to "S-level beyond 1/2"**: g = 1_S (or r/4) is multiplicative and 1-bounded. **Caveat**: 1_{p prime}1_S(p) =
1_{p≡1(4)} is *not* Siegel–Walfisz for even q, so a χ₄-twisted main term is needed (Granville–Shao handle this with
characters ψ_j). Also, 1_S has density (log x)^{−1/2}, so the saving (log x)^{1−ε} beats the trivial bound by only (log x)^{1/2−ε}.
That is far too weak for a sieve remainder, which must be o(x/(log x)^{3/2}) or smaller.
* Green 1604.04481, **Thm 1.1**: |f| ≤ 1 multiplicative, X^{1/3} < Q < X^{1/2+1/78−σ}, fixed 0<|a|<10Q. Then
  |E_{n≤X, n≡a(q)} f(n) − E_{n≤X} f(n)| ≤ ε except for ≤ Qε^{−1}X^{−cσε} primes q ∈ [Q,2Q).
* Granville–Shao 1703.06865, **Thm 1.8**: fixed a, Q ≤ x^{20/39−δ}, Σ_{q∼Q} |Δ(f,x;q,a)| ≪ x/(log x)^{1−ε}
  (1-Siegel–Walfisz f).
* Drappeau–Topacogullari 1807.09569 (ANT 13 (2019)), **Thm 1.1**: for f periodic over primes with |f| ≤ τ_A,
  Σ f(n)τ(n−1) = 2Σ_{χ, cond|D} Σ_{q≤√x} … + O(x/(log x)^N). This is "a result of Bombieri–Vinogradov type 'beyond √x' for the
  average of f … in the residue classes of a fixed integer and without absolute values".
  **Cor 1.5**: Σ_{n∈B, n≤x} τ(n−h) = x(log x)^{1/2}Σ β_{h,ℓ}(log x)^{−ℓ} + O(·), for B = the set of sums of two squares.
  → The **S-side with the divisor function** is fully under control beyond √x, through a Heath-Brown-type combinatorial identity
  for τ_{1/2}-like functions. The same with **Λ** in place of τ is exactly the open problem.

### 2.8 Lü–Wang–Wu, "On the Hardy–Littlewood–Chowla conjecture", arXiv:2610.20242 (v1, 14 Oct 2026, 52 pp.)
**Thm 1** (as claimed): Σ_{p≤x} μ(p+2) = o(π(x)). **Thm 2**: each sign of μ(p+2) has density 1/2 among the primes with
μ²(p+2)=1. If true, this is a parity-breaking result at a *fixed* shift (Hildebrand's 1989 conjecture).
**Mechanism (read from §2–5)**:
1. Vaughan: Λ = T1 − T2 + T3 with U=V=x^{1/5} and Z-sifted variables (Z = exp(L^{0.24})).
2. Insert weights W(n) = ∏_{i=1}^K ρ^{ω_i(n)−1}ω_i(n)/V_i built from prime sets P_i = (exp(L^{a_i}), exp(2L^{a_i})], 1/10<a_i<1/5.
3. Type II: expand W(mn+2) as Σ over a = p_1⋯p_K | mn+2. Write mn+2 = ah. Apply C–S **in h using only |μ(h)ρ^{ω(h)}| ≤ 1**.
   This gives |T_Y|² ≪ (X/Y) Q_Y, where Q_Y counts the **determinant equation b·mn − a·rs = 2(a−b)** (eq. 4.8).
4. Prop 4.2: Q_Y = Q_Y^maj + O(XYL^{−A}) for *arbitrary* sifted α, β ("prime-list operators", "parity conjugacy",
   moments of order 2R with R ≈ L^{1/2}). Prop 5.3: Q_Y^maj is small because α_m = μ(m) cancels on major arcs.
**My assessment (an explicit judgment, not a verification)**: after step 3 the target μ has dropped out entirely. Q_Y is an
average over pairs (a,b) of small (exp(L^{0.2})) moduli of *binary correlations of the Type II piece μ*c_V of Λ* along the
forms bn − an′ = 2(a−b). Bounding its minor arcs looks comparable in strength to averaged Hardy–Littlewood for Λ over only
exp((log x)^{0.2})-many forms. That regime is far below what Matomäki–Radziwiłł–Tao reach for Λ(n)Λ(n+h) (h ≤ x^{8/33+ε}, per
GMPP §1). The same skeleton would also seem to give unconditional two-point Chowla Σμ(n)μ(n+2)=o(x) at all scales, which
is still open: Helfgott–Radziwiłł and Pilatte get only log-averaged / almost-all-scales results. **Treat as UNVERIFIED and likely to
need correction until an independent expert check.** If it survives, its template (small-prime factor expansion → C–S in the
cofactor → determinant-equation Type II) is the most relevant parity-breaking mechanism here. Our target is also a
determinant-type lattice count. But it yields o(·) for a *signed* multiplicative function, and our target needs main terms
for nonnegative weights (see Lead B).

### 2.9 Shifted-prime Chowla/Elliott on average
* Lichtman 2009.08969 (QJM 2021), **Thm 1.1**: if H < X and log H/log₂X → ∞, then Σ_{h≤H} |Σ_{p≤X} μ(p+h)| = o(Hπ(X)).
* Lichtman–Teräväinen 2111.08912 (FMS 10 (2022) e57). **Thm 1.2(i)**: for (log X)^{ℓ+ε} ≤ H ≤ exp((log X)^a),
  Σ_{h1≤H} |Σ_{n≤X} μ(n+h1)⋯μ(n+h_k)Λ(n+a_1)⋯Λ(n+a_ℓ)| ≪ HX log log H/log H.
  **Thm 1.6 (HL–Elliott on average)**: the same for 1-bounded multiplicative f_1,…,f_k. The bound involves
  exp(−M(f_1;X,…)/(10000ℓε^{−1})), so f_1 must be non-pretentious.
**Relevance**: only averaged shifts, and the linear forms must be n+h, not 4n+1. 1_S is pretentious (it pretends to (1+χ₄)/2-type).
The natural non-pretentious companion is g(n) = i^{Ω₃(n)} (Ω₃ = number of prime factors ≡ 3 mod 4), see Lead B.
The averaged version would at best give "for almost all h: p+h ∈ S-type and 4p+1 cancellation", not P(4,15).

### 2.10 Correlations of multiplicative functions (no prime variable)
* Tao–Teräväinen 1708.02610 (Duke 2019): structure theorem for log-averaged correlations, odd-order log-Chowla, sign patterns
  of λ up to length 3 and μ up to length 4.
* Tao–Teräväinen 1809.02518 (ANT 13 (2019)): k-point Chowla "for k odd or equal to 2 for all scales X outside of a set of zero
  logarithmic density".
* Teräväinen 1710.01195 (FMS 6 (2018) e10): log-averaged binary correlation of real g₁, g₂ that are equidistributed in APs to fixed moduli
  is asymptotic to the product of the means.
* Klurman–Mangerel–Teräväinen 2304.05344: two-point correlations of non-pretentious f → 0 along a set of x of full upper log density.
* Helfgott–Radziwiłł 2103.06853: Σ λ(n)λ(n+1)/n = O(log x/(log log x)^{1/2}) (expansion of the divisibility graph).
  Pilatte 2310.19357: ≪ (log x)^{1−c}, "best possible with current methods". Theorem numbers UNVERIFIED (abstract only).
* Tao–Teräväinen 2512.01739: quantitative two-point correlation with a small power-of-log saving (built on Pilatte).
**Relevance**: no Λ in the correlation. The correlation 1_S(n+4)·1_S(4n+1) *without* primality is easy anyway
(divisor-type methods). **None of these touch the prime variable**, so they are not leads.

### 2.11 Short-interval almost primes
Teräväinen 1510.06005 (MPCPS 161 (2016)): E₃ in almost all [x, x+log^{1+ε}x], E₂ in almost all [x, x+log^{3.51}x].
Matomäki–Teräväinen 2207.05038 (TAMS 376 (2023)), **Thm 1.1**: E₂ numbers p₁p₂ ∈ (x, x+(log x)^{2.1}] for all but ≪ X/(log X)^δ
of x, with (log x)^{1.09} < p₁ ≤ (log x)^{1.1}. The new Type II uses Heath-Brown's sparse mean value theorem.
MPPTW 2610.09567: Gowers uniformity of Λ in all [X, X+X^{3/5+ε}], μ cancellation in X^{19/35+ε} (Guth–Maynard input).
Relevance: Dirichlet-polynomial Type II in short intervals. Nothing here handles two additive shifts. Not applicable.

### 2.12 Primes in APs beyond √x
* Lichtman 2309.08522, **Thm 1.7**: primes equidistributed against triply well-factorable λ_q of level x^{ϑ} with
  ϑ = (5−4θ)/(8−6θ) − ε (θ = Selberg exponent), uniformly for 0<|a|<x^ε. Abstract: level 66/107 ≈ 0.617 unconditionally,
  5/8 under Selberg. Applications: **Thm 1.1** π₂(x) ≲ 3.2290 Π₂(x); **Thm 1.2** G(a) ≲ 3.3907 Π_a(a).
* Pascadi 2505.00653 (abstract): primes and smooth numbers equidistributed to moduli x^{5/8−o(1)} with triply well-factorable
  weights for primes, **unconditional** (removes Selberg).
* Stadlmann 2309.00425 (abstract): primes equidistributed to smooth moduli up to x^{1/2+1/40−ε}.
* Lichtman 2211.09641: quadrilinear forms of moduli up to x^{17/32}.
**Relevance**: all of these need a **fixed residue a** (|a| < x^ε) and well-factorable weights. In our double sieve the moduli are
d₁d₂ with p ≡ −4 (mod d₁) and 4p ≡ −1 (mod d₂). The CRT residue is not a fixed integer (it comes from the quadratic polynomial
(p+4)(4p+1)), unless one sieves only one form at a time. They can improve the *numerics* of "bounded number of 3-mod-4
factors", but not reach exact membership in S.

### 2.13 Consecutive S-numbers (no primes)
Kimmel–Kuperberg 2306.12855 / 2406.04174: runs of consecutive sums of two squares in prescribed APs, positive density.
Not relevant to primality.

### 2.14 Siegel zeros
Banks 2610.15483 gives an explicit account of "the OpenAI manuscript" claiming no Landau–Siegel zeros: (1−β)log q ≥ 3.0×10^{−3}
for all q ≥ 3 (with Lu–Zaman–Zhao). Follow-ups: Kerr 2610.21099, Guo 2610.30476. GMPP §1.1 also cites "the new OpenAI breakthrough
on Landau-Siegel zeros". Consequence: the conditional parity-breaking under Siegel zeros (Matomäki–Merikoski 2112.11412:
asymptotic for Σ Λ(n)Λ(±n+h) uniformly in h=O(X) *assuming* Siegel zeros) **becomes vacuous**. It is not a route to P(4,15).

---------------------------------------------------------------------------------------------------
## 3. Structural observations used in ranking

(O1) **The "parity" obstruction here is 0-vs-2, not odd-vs-even.** For n ≡ 1 mod 4 (true for 4p+1, and for p+4 when p ≡ 1 mod 4),
n ≡ (−1)^{Ω₃(n)} mod 4, so Ω₃(n) is even. A half-dimensional sieve at level D sifts 3-mod-4 primes below z < D
(sifting limit β=1 for κ=1/2). If z ≥ x^{1/2−ε'}, survivors have Ω₃ ∈ {0,2}. The bad case is two 3-mod-4 primes near √x.
These two cases are separated by the completely multiplicative **g(n) = i^{Ω₃(n)}**, with g(p)=1 for p≡1(4) and g(p)=i for p≡3(4).
On n≡1(4), g = (−1)^{Ω₃/2}.
g is non-pretentious, because no character χ(p)p^{it} can be ≈ i on all p≡3(4) (χ(3)² = 1). So exact membership in S is a
Bombieri-asymptotic-sieve-type question: Type I level ~√x **plus** cancellation of g on the sequence.

(O2) **Type I level is the binding constraint on every route.** Write r(p+4) = 4Σ_{e|p+4}χ₄(e) (divisor switching, e ≤ √x) and sieve
4p+1 at level D. Then primes are needed in APs to moduli e·d up to x^{1/2}·D. BV allows only total modulus x^{1/2}. This explains our internal
"bounded Ω₃" result and the analogous Nath–Xie Ω ≤ 9. Doing divisor switching on both shifts gives Σ_p r(p+4)r(4p+1), which needs
moduli up to x: exactly FI's A(θ), θ → 1.

(O3) **Two choices of base sequence.** (i) Primes as base: needs EH-level for primes with non-fixed residues, so it is hopeless short of EH.
(ii) The **shell as base**, a_n = #{M: det M=15, ‖M‖² = 16n+34} (density ~ constant, not thin), sieved for primality.
This needs R(θ)-type Type I for a_n (spectral, currently θ = 1/6 for det 1) **and** a Type II estimate for a_n. GMPP shows such Type II
is reachable for quadratic sequences *on average over the shift*. This matches the FI hyperbolic-PNT programme.

---------------------------------------------------------------------------------------------------
## 4. HOT LEADS (ranked)

### Lead A (most plausible): shell-as-base Harman sieve, using spectral Type I + GMPP-type Type II
Mechanism: treat a_n (det-15 shell, or r(n+4)r(4n+1)) as a GL(2)/Hecke-orbit sequence.
* **Missing estimate A1 (Type I, parity-free)**: an R(θ)-type level of distribution for the det-15 shell,
  Σ_{d≤x^{θ}} |Σ_{n≤x, d|n} r(n+4)r(4n+1) − g(d)·c·x| ≪ x(log x)^{−A}, with θ ≥ 1/2 (and ideally ~3/4 as in FI's a²+b⁴ Type I).
  Today: θ = 1/6 for det 1 (Sedunova Lemma 2, via an individual error O(d^{−1/2}x^{11/12+ε})). Tools: the Grimmelt–Merikoski
  automorphic kernel (2505.00489), spectral large sieve with Hecke operator T₁₅. On its own A1 gives almost-primes
  with ≤ ⌊2/θ⌋ factors (Sedunova Thm 3 analogue). R(1/2) gives ≤ 4.
* **Missing estimate A2 (Type II, parity-breaking)**: Σ_{m∼M, n∼N} α_m β_n a_{mn} = main + O(x(log x)^{−A}), with β Siegel–Walfisz,
  for N in some range [x^{c₁}, x^{c₂}] wide enough for Harman's sieve (cf. Merikoski: [X^{1/4+η}, X^{1/3−η}] already gave ≍ with
  Type I up to X^{3/4−η}).
  Candidate route: C–S on m turns a_{mn} into counts of pairs of det-15 matrices, i.e. a quaternary/binary quadratic-form
  correlation. Then use Voronoi/Kuznetsov as in GMPP §1.1 / §7. **Obstacle**: GMPP's Type II needs the extra average over
  the shift h (non-trivial only for H ≥ X^{1/3+ε}). We have a single fixed determinant 15 and fixed shifts. The missing ingredient is a
  *fixed-shift* substitute for GMPP's second Cauchy–Schwarz over h. The SL2 orbit structure (Hecke equidistribution) might
  supply it: that is the FI hyperbolic-PNT gap, still open (Sedunova 2026).

### Lead B (parity-breaking in the (O1) form; depends on whether Lü–Wang–Wu survives)
P(4,15) would follow from a half-dimensional analogue of the Bombieri asymptotic sieve. Combine:
(B1) a sieve lower bound for #{p : r(p+4)>0, Ω₃(4p+1) ∈ {0,2}} ≫ x/(log x)^2. This needs level ≈ x^{1/2+} for the sequence
{4p+1 : weighted by r(p+4)}, the (O2) obstacle. With only x^{δ} it gives Ω₃ ≤ 1/δ (our internal result).
(B2) a **Hardy–Littlewood–Chowla-type cancellation**
  Σ_{p≤x} r(p+4) · 1_{(4p+1, P₃(z))=1} · i^{Ω₃(4p+1)} = o(x/(log x)^{2}).
After divisor switching on r, B2 needs Σ_{p≡−4 (e)} g(4p+1) = o(·) on average over e ≤ √x: a BV-type extension of a
"Σ_p μ(p+2)=o" statement with g = i^{Ω₃}. If LWW's method is correct, it is the only one in the literature attacking such
fixed-shift sums Σ_p f(ap+b). Its Type II (C–S in the cofactor after extracting small primes a | n; determinant equation)
uses multiplicativity of f only to split f(ah)=f(a)f(h). That holds for g = i^{Ω₃} (g(a)=1 when a has only 1-mod-4 primes).
**Caveat**: B1 still needs EH-type level, so Lead B helps only together with Lead A1, or if B1 can be replaced by an upper-bound
(Chen-switching) estimate for the Ω₃=2 contribution. That contribution is n = q₁q₂m with q₁, q₂ ≡ 3 (4) near √x and m tiny.
Its upper bound uses bilinear structure (Chen/Iwaniec switching as in Nath–Xie §2). Lower bound and upper bound are both
O(√ε')-small near s=1, which gives a genuine numerical contest. Worth a quick computation; I have not checked it.

### Lead C (incremental, safe): sharper "bounded Ω₃" via level beyond 1/2 + Chen/Iwaniec switching + vector sieve
Use Lichtman's 66/107 / Pascadi's 5/8 triply-well-factorable levels (fixed residue: sieve only p+4 ≡ 0 mod d with a=−4 fixed)
in the Nath–Xie vector-sieve framework, with Drappeau–Topacogullari / Fouvry–Radziwiłł for S-side remainder terms.
This cannot give exact S on both shifts by (O1)/(O2). It lowers the bound on Ω₃(4p+1) and could make the Lead B numerics
feasible. **Missing estimate**: a log-power-saving version of FR Cor 1.3 for g=1_S (χ₄-twisted main term), i.e.
Σ_{q∼Q} |Δ(1_S; x, q, a)| ≪ x/(log x)^{A} with Q = x^{1/2+δ}. FR explicitly say the (log x)^{1+ε} improvement is out of reach.

**Bottom line**: there is no off-the-shelf mechanism. The literature's parity breaks need either (i) a number-field factorization of
the prime (FI, HB, Maynard, Merikoski, Green–Sawhney), which is excluded by our obstruction, (ii) averaging over a shift (GMPP, Lichtman,
Lichtman–Teräväinen, MRT), or (iii) an unverified fixed-shift claim (LWW). P(4,15) needs a fixed-shift, non-factoring
Type II for a GL(2)-orbit sequence. The nearest attack is GMPP's Type II technology transplanted to the det-15 shell (Lead A2),
plus spectral Type I (A1).
