# Z2620 — DFI versus the actual ES Weil remainder

**PROVED exponent algebra / Assessment of applicability. ES is OPEN.**

`git grep Weil -- 'EXCEPTIONAL*.md'` locates the relevant uses, not just a generic barrier. EXCEPTIONAL_MN4.md §2.6, Proposition 7.1_m (lines 223–241) uses modulus k=ma², EF=kD, and gives
 R_a(q) ≪ 2^ω(q)τ(k)²(q√k+D/E+D/F).
In §2.7(b1), lines 260–265, summing a≈A and sieve q≤Q yields
 R_Weil/(AD) ≪ polylog(N) m^O(1) [Q²√m A/D + Q N^(−c₀)].
EXCEPTIONAL_TYPEI_LOGLOG.md §7 is the underlying fixed-a Poisson argument. These are complete (possibly twisted) Kloosterman sums at moduli involving ma²q, not already the separable moving-modulus bilinear form of DFI.

I read the original local PDF `sources/dfi-1997-kloosterman-fractions.pdf`, pp.23–25. **Citation correction:** PARITY_AUDIT B7 attributes the 3/8,11/48 bound to Theorem 1; it is Theorem 2, equation (1.5). Theorem 1, equation (1.4), is
 |B_a(M,N)| ≪ ||α||₂||β||₂ [(M+N)^(1/2)+(1+a/(MN))^(1/2)min(M,N)](MN)^ε.
Theorem 2 is ||α||₂||β||₂(a+MN)^(3/8)(M+N)^(11/48+ε). Their combination really does cover unbalanced as well as balanced polynomial ranges; it would be wrong to use only Theorem 2 and conclude DFI fails for M<N^(5/6). The theorem assumes independent one-variable coefficients α_mβ_n and (m,n)=1.

For coefficients bounded by 1, a≪MN, M=X^μ,N=X^ν, ignoring X^ε:
 E₁=(μ+ν)/2+max(max(μ,ν)/2,min(μ,ν));
 E₂=7(μ+ν)/8+11max(μ,ν)/48;
 E_DFI=min(E₁,E₂).
For ν=1:

| μ | trivial exponent | DFI best | saving | smooth-inner Weil completion benchmark |
|---|---:|---:|---:|---:|
| 1 | 2 | 95/48 | 1/48 | 3/2 |
| 9/10 | 19/10 | 37/20 | 1/20 | 3/2 |
| 4/5 | 9/5 | 17/10 | 1/10 | 3/2 |
| 1/2 | 3/2 | 5/4 | 1/4 | 3/2 |

The Weil column requires an interval/smooth inner weight and an ordinary nondegenerate inverse phase, with the usual gcd factors controlled; it is NOT available for arbitrary α_m. Thus neither a universal “DFI improves Weil” nor its converse follows. At balance DFI gains X^(1/48) only relative to the trivial X², not relative to the X^(3/2) smooth completion benchmark. Bettin–Chandee Theorem 1 with third length 1 gives X^(39/20), a 1/20 saving from X², under the same independence requirements.

For the actual ES cell set A=N^α,D=N^δ,Q=N^ρ and m polylogarithmic, the Weil exponent normalised by AD is 2ρ+α−δ (plus the axis term ρ−c₀). The first spectral term in MN4 (2.7), with bounded cusp factor, is 2ρ+(δ−α)/2. E.g. (α,δ,ρ)=(.4,.6,.04) gives −.12 versus +.18; (.5,.5,0) gives 0 for both; (.6,.4,.02) gives +.24 versus −.06. At the diagonal there is no polynomial sieve level from these terms.

Why DFI is not a drop-in replacement: in the (★) coordinates f=4uC−1, one has overline(4C)≡u (f), so e(h overline(4C)/f)=e(hu/f); u,C and f are coupled. Regarding f,C as independent would insert 1[f≡−1 (4C)] and the ES height condition into the coefficient, which is no longer α_Cβ_f. In MN4 the completed moduli ma²q and Fourier frequencies similarly depend on the outer a; retaining the Poisson weights and sieve restrictions requires a fresh reduction, not insertion of a bilinear exponent into an absolute Weil bound. Consequently no justified exponent change to 2ρ+α−δ, and no new exceptional-set exponent, follows from DFI as presently set up. This is an applicability conclusion for these equations, not a theorem ruling out all reorganisations.

Reproduce the rational exponent table with `timeout 20s uv run python scripts/z52d_p2_ZF0_Z2620_exponents.py`. No large computation is required. An attempted arbitrary-coefficient replacement by a hypothetical X^(1/48) cancellation would be an unproved assumption and is deliberately not reported as a gain.
