# BILINJAC hostile cross-review

**Verdict: ACCEPT-WITH-FIXES.** The central “narrowed” verdict survives; correct the three items below before recording the memo wholesale.
Reviewed `side-agent/z54-bilinjac` at `6ca056cfcf4f3985e7d2e605776d5ed242730509`, including predecessor lemmas, scripts and data.
This is upper-bound work only. No power saving is established unconditionally; ES remains OPEN.

## Per-claim audit

| Claim | Classification | Independent derivation / qualification |
|---|---|---|
| Lemma 2.1(a–c) | CORRECT | The s-window has length 4.5V < 4C; m=Ck has at most τ(m) factorisations; s²≤25V² and 4k≤(n+5V)/W. The divisor estimate uses the intended balanced/nonempty-block range V≪n. No lower mass bound follows. |
| F1, F2, F4, F5 identities | CORRECT | Polynomial reduction gives Q-periodicity; substitute m=Ck; finite Fourier inversion gives F4; ordered prime pairs give β_Q=2. Negative a introduces (−1/Q), not a positivity assumption. |
| F3 Poisson identity and sizes | CORRECT | Poisson on k=k₀+Qj gives the stated sign, phase and factor V/(4CQ). Completing the quadratic gives ordinary Kloosterman sums on nondegenerate classes, with Gauss/degenerate exceptions as in Lemma W. Frequency scale QW/V and Parseval give typical ℓ¹≈W√Q, ℓ²≈√V. Read coefficient “≈” as a typical scale, not a lower bound throughout the Schwartz tail. |
| F6 pair identity; prime coprimality | CORRECT | C=(n+u+B)/(4uB); gcd(u,B) divides n, hence is 1 when n=p>4V. The short-interval factorisation statement follows from u+B≤4V. |
| F6 noncoprime counterexample | WRONG | For (u,B,n)=(3,6,15), (n+u+B)/(uB)=4/3, which is not an integer divisible by 4. It fails the third bracket condition. In fact that condition alone is equivalent to 4uB∣n+u+B, even without coprimality. Fix 2 below. |
| Lemma 2.2(i–iii) | CORRECT | Normalized Parseval gives Σ abs(ĝ)²≤1; Cauchy gives Σ abs(ĝ)≤Q. At q, the complete mean numerator is 1 if q∤n and −(q−1) otherwise; CRT gives abs(ĝ(0,0))<1/Q. Fourier inversion and triangle inequality finish (iii). |
| Proposition M(i) | CORRECT | Every admissible square contributes 1 to each of P₀(P₀−1) ordered pairs. The diagonal in σ² is P₀−ν(a), bounded above by P₀. |
| Proposition M(ii) | CORRECT | Place weight h on min(K,A(X)) admissible squares. A uniform norm/support/range bound must cover that weight; dividing by P₀² gives the stated (1−1/P₀) obstruction. This concerns N_□, not an unconditional lower bound on actual strip N. |
| Proposition M(iii) | CORRECT | w′=√D δ₁ forces F(D)≥P₀(P₀−1)√D. Also D≤‖w‖₁² and D≥M_s², so β≥√D≥M_s. Any numerical bound D≤D₀ already implies N≤2√D₀+τ(n), without the character sieve. |
| Corollary M′(a,b) | CORRECT | HB Cor 2 really has the square-product norm. Sign splitting and Cauchy over ≍P₀² moduli give P₀√(P²+X)√D, with epsilon losses. Cor 4 after sign/2-adic splitting and normalization depends only on ranges and h. Both are direct norm-only uses, not universal exclusions. |
| Corollary M′(c,d) | CORRECT WITH SCOPE | CFS is an unweighted full-box result. Sparse weighted a-sums are not direct interval-character inputs. Λ=Λ_□+Λ_non proves only the stated identity-level objection to bounding Λ_non; weighted/completed PV/Burgess uses remain open. CFS's auxiliary formula is miscopied in LIT_CHECK, not in the main application. |
| Theorem R | CORRECT | For m²≤25V² and 2^{P₀}≥25V², at most P₀/2 auxiliary primes divide m; thus square-sieve detection works also with signed nonsquare a. Combine N≤2M_s+τ(n), S₁≪Vn^ε and Lemma 2.2: N≪n^ε(V/P+P² max abs(T)). P/log P absorbs into n^ε; V/P≥1 absorbs τ(n). |
| R's three conditional exponents | CORRECT | P=V^{δ/3} gives V^{1−δ/3}; δ=1/2 gives V^{5/6}=n^{5/24}. Direct square-root S_Q with P=V^{1/2} gives V^{1/2}=n^{1/8}. These are conditional, with epsilon losses and sufficiently large n. |
| Proposition R′ | CORRECT | Insert g(c,k)=e((ac+bk)/Q), a mean-zero unit-modulus Q-periodic function. Necessity holds only for the defined twist-blind implementation. |
| §5 divisor identity and calibration | CORRECT | Summing over m=Ck gives the restricted-divisor identity; Q=1 Poisson gives the stated main term/error. Li–Yang gives 4θ*=1.2579327039…, but no transfer to a dyadic piece. Ivić (1.13) is precisely the cited Jutila conjecture; no implication to TS is proved. |
| §5.3 exponent-pair arithmetic | CORRECT | For W=√n/16, n/(4C²)∈[16,64], so the reciprocal term dominates a/Q for h≠0. Triangle summation costs (V/W)(W/V)^{κ+1}W^λ=V^{κ+2λ}. Values 41/28, 3/2 and 1 are correct. This excludes only those majorant expressions. |
| §5.5 DFI arithmetic | CORRECT | Primary DFI (1.4) has a sum of two terms; its second term at a≈V⁴, M=N≈V, ‖α‖‖β‖≈V is V³. Equation (1.5) gives V^{1+3/2+11/48}=V^{131/48}. Neither is a no-go for reorganized forms. |
| §5.5 double large sieve | ASSESSMENT, NOT A THEOREM | With the stated separability/spreading assumptions, diagonal arithmetic gives √[(QV)(1/(QV))(QV²)]=V√Q; generic spacing gives V^{3/2}√Q. The inequality and assumptions are not verified, so no certified exclusion follows. |
| §5.5 all-Q 2-D additive large sieve | WRONG AS WRITTEN | Reducing nonprimitive frequencies to denominators does not remove their multiplicity. The displayed all-Q inequality fails for arbitrary box coefficients (Fix 1). Its optimized V² deficit is algebraically correct for that expression, but is not a justified estimate. |
| Inherited determinant claim | CORRECT RELATIVE TO QUOTED INPUTS | In HYP2CYCLE D, T=B₁B₂B₃ and b₁b₂b₃/(b₁+b₂+b₃)≥b_min²/3 give the HB15 expression ≥B_min^{2/√3}; HB14 gives the same comparison. Only auxiliary-count-bound × uniform-per-curve-bound implementations are excluded. |
| §7 computations / labels | AGREEMENT ON DECISIVE RERUNS | Full census and all 320 largest-scale strip output lines reproduce byte-for-byte; one full Poisson-shell instance also reproduces byte-for-byte. Independent enumeration and Fourier checks agree below. EVIDENCE remains finite-range, with sharp/Gaussian rather than compact Φ weights. |

## Required fixes, in priority order

1. **Delete or repair the all-Q additive-large-sieve claim in §5.5 and its §6 row.**
   The stated bound sums every (a,b) mod Q for every Q≤R, hence repeats (0,0) R times.
   Take unit coefficients on [1,L²]² and R=L. Then Σω²=L⁴, T_Q(0,0)=L⁴, so the left side is ≥L⁹.
   The claimed right-side expression is (L+L)⁴L⁴=16L⁸, a contradiction as L→∞ (also with sufficiently small epsilon losses).
   Nonprimitive rational frequencies likewise recur. Restricting to primitive pairs or retaining denominator multiplicities requires a new derivation, especially for Q=qq′.
   Safest fix: retain this only as an unverified heuristic and remove the asserted inequality/deficit. Prop M and Theorem R do not use it.
2. **Correct F6's bracket/counterexample.** With standard divisibility, “4∣(n+u+B)/(uB)” already asserts the desired condition.
   Delete the alleged failure without coprimality. If the intended warning concerns only the two divisibilities u∣n+B and B∣n+u, say so: the example does demonstrate their insufficiency for uB∣n+u+B.
   Under gcd(u,B)=1, those two divisibilities imply an integral quotient; imposing its divisibility by 4 is then legitimate.
3. **Correct `data/z54/bilinjac/LIT_CHECK.md` §2(b).** CFS p. 2 defines
   C(α)=√α+(1/(2π))Σ_{k≥1}k^{−2}∫₀^α √y[1−cos(2πk²/y)+sin(2πk²/y)]dy.
   The note instead has √α/(2π) and y in the integrand. Its main asymptotic/error exponents and the full-box applicability assessment are unaffected.

## Reproduction and independent numerical checks

Every shell invocation used `ulimit -v 6000000`, a CPU limit, and an external `timeout`; no unbounded dense calculation was run.
Files were extracted from the pinned branch into `/tmp/xrev_BILINJAC`; no reviewed-branch files were modified.
- Census: compiled with `gcc -O2`; reran X=10⁹ under 120 s. Entire `census_1e9.txt` is byte-identical, including maxima 20 and 14, decade means and square zeros.
- Independent fixed-n pair enumeration verifies 20 at 635674641, 14 at the prime 250810249, and 0 at 100003². This independently checks the extremal witnesses, not the exhaustive upper bound.
- Strip: reran `multi.py ... 14 100 30 ...` under 130 s. Entire `strip_1e14.txt` is byte-identical (100 primes, 30 squares, 30 near-squares, two P choices each).
- Independent F2 divisor enumeration, Euler-criterion characters and direct sparse Fourier sums give:

| n | V,W,P | mass A | S_Q rms/√A | max abs(S_Q)/√A | max abs(T₆₁)/√A |
|---|---|---:|---:|---:|---:|
| 10000000033 | 316,6250,18 | 117 | 0.66 | 1.11 | 2.87 |
| 10000600009 | 316,6250,18 | 106 | 0.75 | 1.46 | 2.79 |
| 100000000000031 | 3162,625000,56 | 1121 | 1.14 | 2.69 | 2.63 |

All columns agree with the lane C program; the last n is an additional check, not asserted to be one of its 100 sampled primes.
- Complete residue means: 225 exhaustive n/modulus cases (odd primes through 23; composite 15,35,77) verify Lemma 2.2's exact numerator and <Q bound.
- Poisson: reran `(n,V,W,q,q′)=(10000000033,316,6250,11,13)` under 150 s; its entire shell block matches the first block of `shells_1e10.txt` byte-for-byte. The other five shell runs were not rerun.
- Independent checks are preserved in `scripts/z54_xrev_bilinjac_check.py`; run with `timeout 120s uv run --with sympy python ...` after the memory/CPU limits.

## Primary-source verification

Read the relevant theorem pages directly, not merely the lane's transcriptions:
- HB Corollaries 2/4, manuscript pp. 3–4: https://ora.ox.ac.uk/objects/uuid:b188b365-d8d1-4267-8548-49f01e6cb6a7/files/m6af40476f1b860392271a2d8ecae593b
- DFI Theorems 1/2, printed p. 24: repository `sources/dfi-1997-kloosterman-fractions.pdf`.
- CFS Theorem 1 and C(α), p. 2: https://arxiv.org/pdf/math/9903197
- Li–Yang Theorem 1.2, p. 2: https://arxiv.org/pdf/2308.14859
- Ivić (1.9), (1.12)–(1.14), printed pp. 253–254: https://jtnb.centre-mersenne.org/item/10.5802/jtnb.669.pdf

## Verdict and label discipline

**Narrowed is justified:** the two specified norm-only square-sieve input classes add no useful information, while Theorem R supplies a sufficient twisted-strip hypothesis with the correct Q loss. It does not establish TS or make TS necessary for character-specific methods.
The literature-search conclusion is explicitly search-limited; the Jutila comparison is an analogy, not a reduction. Numerical consistency is not evidence of a uniform theorem, and the additive experiments use prime 61 rather than the composite moduli of TS.
After the listed corrections, record Prop M/M′, Lemma 2.2, Theorem R/R′ and the scoped arithmetic deficits. Do not promote either large-sieve Assessment to PROVED. Nothing here implies positivity or settles ES.
