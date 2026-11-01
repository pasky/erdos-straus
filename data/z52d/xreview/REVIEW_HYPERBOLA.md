# HYPERBOLA cross-model hostile review

Reviewed `side-agent/depth-hyperbola` at `8e798122f2290c2bb55dc7bcbc96534dc4e37a31`.
**Verdict: ACCEPT-WITH-FIXES.** The balanced-block conclusion **narrowed** survives. Do not import the unrestricted Corollary 4 or §7 wording unchanged. ES remains OPEN.

## Per-claim audit

Write m = min(U,V), Q = UV. Classifications concern the actual statements, not their numerical plausibility.

| Claim | Classification | Independent derivation / qualification |
|---|---|---|
| Lemma 0 | CORRECT | gcd(u,B) divides p; gcd = p forces u,B ≥ p and 4uB > p+u+B. Thus gcd = 1. Divisibility by 4 forces u+B odd. C is uniquely (p+u+B)/(4uB); dyadic intervals including (1/2,1] partition the coordinates. |
| E1, E2 | CORRECT | Character orthogonality gives q⁻¹Σ_{d∣q}c_d(n). The trial equation is (4uC−1)B=p+u; multiplying by the invertible 4C gives 4Cp+1. A fixed trial modulus has at most τ((m_trial+1)/4) factorisations. |
| E3: exact sawtooth and small arc | CORRECT | floor(n/q)−floor((n−1)/q) is the divisibility indicator. Substituting ψ gives (2.2); nonintegral n/q has distance ≥1/q≥1/(16UV), proving (2.3), with strict δ bound. |
| E5: hyperbola and Weil scale | CORRECT, scale comparison only | Multiplication gives xy=4Cp+1, and x=(p+u)/B, y=(p+B)/u gives the stated containing rectangle. At U=V≈p^{1/4}, its area is ≍p^{3/2}; φ(4p)XY/(4p)² and the Weil error both have exponent 1/2. A count for the containing box is not a count with the height/class restriction. |
| Thm 1(a,b) | CORRECT | B lies in one residue class modulo u, yielding floor(V/u)+1; summing uses Σ_{U<u≤2U}1/u≤1. For U=V each row has ≤1 point. Alternatively fix u, B or C and count divisors of p+u, p+B or 4Cp+1. |
| Thm 1(c), S1′ | CORRECT | A hit has 4uB≤p+u+B, so uB≪p, each coordinate is O(p), and the C-interval has O(p/(UV)+1) integers. Divisor bounds give p^{o(1)}min(U,V,p/(UV)+1). If U,V>p^{1/3}, the third quantity is O(p^{1/3}); otherwise use the smaller coordinate. O(log²p) blocks give R≪p^{1/3+o(1)}. Thus the 2/5−δ target is automatic for δ<1/15. |
| Prop 2 / E4 | CORRECT | The interval has U<x elements, hence a unique possible f(x). Mutual divisibility implies gcd(u,B)∣p; 2U<p makes it 1. Thus uB∣n, with precisely the additional factor-4 condition needed. A fixed point would divide p with 1<x<p. Each supported row/column square has ≤1 nonzero term. Only this direction of Cauchy–Schwarz has empty off-diagonal. |
| Lemma 3.1 | CORRECT | CRT gives multiplicativity. For odd ℓ, inclusion–exclusion of the two axes gives −c_ℓ(n)=1. For ℓ^k, k≥2, axes sum to zero and remaining allowed pairs have both coordinates divisible by ℓ, hence c=0. For 2^k, k≤2 is a complete sum; k≥3 reduces to one odd coordinate, and its complete even-residue Ramanujan sum is zero. |
| Thm 3 | CORRECT | Smooth Poisson in each residue class gives J/d² plus O(d⁻²(d/m)^B). Summing absolute coefficients costs at most Σ_{d≤D}d=O(D²). Since D≤m^{1−ε}, choose B>(A+2)/ε to get O(m^{−A}). No primality is used beyond coprimality to every d≤D. Smoothness is essential to this error. |
| Cor 3.2 | CORRECT, scoped as in its statement | For a square, a divisor f≡−1 mod 4u of n+u would have χ_{−4u}(f)=−1, but every prime factor of f has −u a nonzero square modulo it, giving χ(f)=+1. Hence N_w=0 and H_D=−L_D exactly. The common leading term is positive for nonzero weights; a uniform absolute remainder bound over rough n cannot give a fixed positive margin. This does not exclude prime-specific bounds or upper-bound arguments. |
| Cor 4: unit model and local-factor calculation | CORRECT | CRT on units gives λ_q/φ(4uB), with probability zero for non-admissible pairs. The coprime d₂ factor has expectation μ(d₂)c_{d₂}(u+B)/φ(d₂). Averaging unit lifts makes the ℓ^k factor zero for k>v_ℓ(q). Thus only d₁∣q and squarefree d₂ survive. |
| Cor 4: tail lemma | CORRECT | For squarefree d₂∣4uB, gcd(u+B,d₂)≤2gcd(u,B). There are ≤3τ(u)τ(B) divisors; 1/φ(d₂)≪log log X/X for d₂>X≥3. Splitting u=gu′, B=gB′ gives a product bounded by log⁸(2UV). Replace the text's W≤1 by a harmless factor ||W||∞ for general stated weights. |
| Cor 4: unrestricted O_{q,ε,w}(m^{−1+ε}) | GAP | The last line absorbs log⁸(2UV) into m^ε without relating max(U,V) to m. This is invalid for arbitrary aspect ratios (e.g. V=exp(U)). The displayed proof does not establish even uniform decay for that family. No counterexample to the conclusion is asserted. A balanced/polynomial-aspect version is CORRECT-WITH-FIX; see fix 1. |
| Thm 5(a,c) | CORRECT | Frequencies of denominator d number φ(d); summing q/e over divisor e≥K gives τ(q)q/K. The complete a-sum is c_d(n); only summing over d∣q gives q·1[q∣n]. These are exact identities, not a cancellation theorem. |
| Thm 5(b) | CORRECT-WITH-FIX | Put 4uB=kd, k≤K, and count factorisations of kd/4. Each contributing kd/4=uB≤4UV, so the clean bound is K max_{t≤4UV}τ(t)=Kp^{o(1)}. The printed maximum up to 4KUV does not itself justify p^{o(1)} for unrestricted K. |
| Thm 6(a) | CORRECT; citation not needed | A stronger elementary proof uses Fejér: 1[t∈Z]≤K_H(t)/(H+1), since K_H≥0 and K_H(0)=H+1. Summing gives N≤Q/(H+1)+HΔ_H/(H+1), which implies the stated weaker bound. Thus the Selberg coefficient quotation is not a decisive dependency. |
| Thm 6(b,c) | CORRECT, for the stated max-bound implementation | Expanding Σ_h(1−|h|/(H+1))|S_h|² gives Σ_{x,y}K_H(F(x)−F(y))≥(H+1)Q. Subtract Q², discard weights, then divide by 2H: Δ_H²≥(H+1)Q/(4H) when H+1≥2Q. For shorter H the asserted beyond-square-root input is sufficient, not necessary; square-root input gives no exponent improvement over min(U,V). The numerical 1.25 floor belongs to the particular weaker inequality (a). |
| Thm 6(e): Hessian / injectivity | CORRECT | Differentiating F gives det Hess F=(3p²+4p(u+B)+4uB)/(16u⁴B⁴)>0, with F_uu>0. Strict positive definiteness on the convex box makes ∇F injective. Integrating the leading determinant gives 147h²p²/(9216U³V³); inverse square-root determinant gives the stated 2.31–36.95 amplitude constants. |
| §3.5 dual ratio; Thm 6(e) analytic dual count | Assessment labels honest | The coprime populated-lattice count gives D²/(UV) frequency windows versus UV/D pairs, hence D³/(UV)². The full-box stationary image gives κ₀h²ρ²UV and threshold 7.92/ρ. Neither is a proved uniform transformation estimate for all excluded splits/support boundaries; neither rules out cancellation in a longer dual. |
| §3.7 route translations | CORRECT as bookkeeping, not universal no-go theorems | Fixed C gives one integer 4Cp+1 at modulus 4C. A ceiling piece has length ≍p/B², but the balanced u-window restricts m to an interval of length U/B<1. These observations do not decide other blocks, level averages or differently weighted transforms. |
| §5 evidence, §6 verdict, §7 proposed transfer | Evidence reproduced; verdict CORRECT-WITH-FIX | The data support finite-range swap-Poisson behaviour and a weak interior F-signal, not an asymptotic class-blindness theorem for actual primes. Narrowing specific implementations is justified; copying the unrestricted/smoothness-free statements is not. |

## Decisive numerical checks

All executions used `ulimit -v 6000000` and explicit timeouts; no large Cartesian-product geometry was allocated.
Archive/executables and run logs are in `/tmp/xrev_HYPERBOLA/`; committed independent checker: `scripts/z52d_xrev_hyperbola_check.py`.

- Independently evaluated A_d(n) for **1,966** coprime residue cases, every d≤80: exact agreement with Lemma 3.1.
- Direct enumeration of all positive pairs, independently of remainder/factorisation searches: **204** small-prime/parameter cases agree on N_bal, N_int, S_u, S_C, R, T and M_Q.
- Recompiled the falsifier and reran **16** archived large-prime rows (four per window, including endpoints): all eight output fields agree exactly at stored precision. This is a spot-check, not a regeneration of all 160,000 counts.
- Independently recalculated the statistics from **all 160,000 rows**, without the author's analysis script. Means: **0.1416, 0.14986, 0.1444, 0.1381**. Histograms exactly match §5; var/(2M₀): **0.96859, 1.02885, 0.98318, 0.96116**.
- Fixed-rate swap-Poisson p-values: **0.6073, 0.0808, 0.6308, 0.0387**; fitted-rate values: **0.6529, 0.9427, 0.3912, 0.1313**. These agree with the table; fitted-rate non-rejection is not proof of the distribution.
- At 10¹², interior zeros: **9,798/100,000**. On p≡1 mod 4, interior slope **−0.01982±0.02747**, boundary slope **1.00160±0.00904**, R slope **0.96383±0.00877**. Block correlation with log F: **0.001215**; with M_Q: **0.024096**; with −T: **0.004705**. All agree.
- Recompiled/reran all four M₀ values: **0.14513321, 0.14594093, 0.14603095, 0.14603641**. Both interior values: **1.58707715, 4.63513751**. Agreement at all printed digits.
- Recompiled/reran **all 4,000** exponential sums: output is byte-identical to the archive. RMS/U **1.765122, 1.421918**; maxima/U **5.765411, 4.445578**. Best stated majorant: **13,448.184042 at H=508**.
- Reran smooth low-conductor computation: prediction **0.0200825839777798**, all 12 outputs **0.020082584** at nine decimals. This does **not** independently certify the memo's separate 45-digit spread claim.
- Reran Cor 4 illustrations: q=7 spreads **0.0804, 0.0157, 0.0028**; q=16 **0.0948, 0.0129, 0.0021**. Agreement; balanced examples do not repair arbitrary-aspect quantifiers.

## Source checks

- Read the primary Elsholtz–Tao PDF `sources/elsholtz-tao-1107.1010.pdf`, Proposition 1.7: exponent **2/5** is for the full f_II. The elementary **1/3** calculation for this subfamily stands independently.
- Downloaded/read [Shparlinski, arXiv:1103.2879](https://arxiv.org/pdf/1103.2879), Theorem 13 and (10): main term φ(m)XY/m² and error m^{1/2+o(1)} agree. The “out of reach” wording is the survey's historical assessment, not an impossibility result.
- Downloaded/read [Blomer–Khan–Young, arXiv:1203.2573](https://arxiv.org/pdf/1203.2573), Lemma 8.1 and Proposition 8.2. They are one-dimensional and include derivative/scale hypotheses. They do not themselves supply the memo's omitted uniform two-dimensional reduction; its Assessment label must remain.
- Re-derived the square obstruction directly through χ_{−4u}, rather than treating PARITY_AUDIT's label as proof. The Fejér argument above independently proves Thm 6(a), avoiding reliance on the secondary MathOverflow quotation.

## Required fixes, in priority order

1. **Cor 4 quantifiers:** add `max(U,V)≤min(U,V)^A` for fixed A (allow constants to depend on A), or retain the displayed `log⁸(2UV)` factor and stop claiming unrestricted uniform decay. To preserve the present general statement, supply a new tail argument uniform in aspect ratio. Propagate the restriction to §§0, 6–8. The balanced-block result needs no new mathematics.
2. **Do not upgrade smooth/model statements in §7:** say *smoothly weighted blocks*, with p>D (automatic for relevant UV≤p), for the O(m^{−A}) low-conductor formula. At D=1 with sharp cutoffs and U=V, L₁=(H_{2U}−H_U)²/4=J−(log 2)/(8U)+O(U⁻²), not J+O(U^{−A}) for every A. Also distinguish the product model's polynomial error from the low-conductor superpolynomial error.
3. **Keep verdicts implementation-specific everywhere:** frequency-count concentration in Thm 5 is not concentration of signed/weighted contribution; a tiny frequency fraction can carry the main term (Thm 3). “Closed/self-dual” should mean the explicitly evaluated fixed-conductor or max-bound step, not all Poisson/Voronoi/spectral methods. Keep cross-conductor cancellation, short-segment R1 and unbalanced Z1855 open. Keep “F lives in the strips” empirical/model-scoped, not a theorem about actual counts.
4. **Minor formal repairs:** use `max_{t≤4UV}τ(t)` in Thm 5(b); allow ||W||∞ in the tail lemma. Retain the Assessment labels for the B-process count and the unanalysed conductor splits. The proposed FRONTIER text must inherit these scopes rather than promoting them to PROVED.

After those fixes: **ACCEPT the narrowed verdict**, including the independent 1/3 benchmark correction. No claim here settles ES or rules out cancellation in general.
