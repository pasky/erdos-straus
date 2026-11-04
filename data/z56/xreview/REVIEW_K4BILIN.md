# Cross-model hostile review — K4BILIN

**Verdict: ACCEPT-WITH-FIXES.** Retain the narrowed Type I/P₁₂ advance, not the claimed single-hypothesis implication in Theorem V′.
Reviewed `side-agent/z56-k4bilin` at `ae37ab221b77e413b61a42aee2d7244a61c7de25`, including the revised memo, programs, data and internal review.
**ES remains OPEN.** This review does not certify K(4), an unconditional prime theorem, or completeness of the literature search.

## Per-claim audit

| Claim | Classification | Independent conclusion |
|---|---|---|
| Primitive weights; P(4,15) reduction | CORRECT | Gcd decomposition and Möbius inversion give r*; inert primes cannot divide a primitive norm. On odd S, r*=4·2^ω. HCKILL §1.1's reduction follows from its stated line-4 divisor criterion. |
| Lemma T*: expansion, CRT, tails, density, level | CORRECT-WITH-FIX | Proof survives; correct the endpoint inequalities and the small-endpoint main-term bound below. General prime powers in d are handled correctly. |
| Proposition P: ≫x/(log x)⁹ P₁₂ integers | CORRECT-WITH-FIX | The count and sieve proof survive. The appended assertion that **every** integer in the displayed set is >x^(1/13)-rough is WRONG; only the constructed sifted subset is. |
| Divisibility model w and Lemma N | CORRECT | The fixed-inert-prime box kills the multiplicative comparison. The generalization applies to models with the stated positive lower bound on the forbidden class. |
| W-local densities and definition of ν_W | CORRECT | Each δ has mean 1 and δ(0)/ℓ=g*(ℓ). These are legitimate candidate local factors, not an established comparison theorem. |
| (TII_W) ⇒ Theorem V′ under that hypothesis alone | GAP | Model Type I and model prime mass are not proved by the displayed Rankin calculation. “CONDITIONAL / outline” does not supply these missing premises. |
| Claimed necessary W exponent B≥A/2 | GAP as a deduction from N | ν_W vanishes on earlier inert-prime classes, so it does not satisfy N's uniform positive lower-bound hypothesis on the omitted prime's class. A separate averaged model-mass argument is needed. |
| Proposition D inequality | CORRECT | Cauchy–Schwarz in m followed by absolute values gives the stated correlation bound; the factors and sufficient scale xN are correct. |
| Four-fold/twisted-Type-I strategy; Route S | CORRECT as scoped assessments | Distinct roots in the dyadic range are not finite complexity in one variable. These are sufficient attempted strategies, not necessary barriers. |
| Prime-route budget >3/4 | CORRECT within the stated architecture | Full k-range costs 1/2, and positive semi-linear lower sieve needs θ_D>θ_z>1/4. No universal obstruction follows. |
| 0.757…0.908… thresholds; dispersion comparisons | EVIDENCE / scoped assessment | Threshold program reproduces exactly; grid outputs are not certified optima. Maynard III restrictions are accurately reported; 57/428 is exact. |
| Spectrum/B diagnostics and controls | EVIDENCE, reproduced | Decisive runs agree byte-for-byte. They do not validate all-coefficient Type II, W-tricked or otherwise. |

## Proof audit and repairs

**T*.** (i) The relation 4N₁−N₂=15 and the class 97 mod 120 give (N₁,N₂)=1 and all required coprimalities with 30 and d.
(ii) Charging the unused square divisors to divisor bounds gives the large-e tail x^(1−3η)/d+x^(1/2+η).
(iii) v≡5 mod 8 excludes squares. Opening r(v) yields a reduced progression modulo q=120de₂²k, with the doubled Smith main term.
The text incorrectly says e₁²≤E when e₁e₂≤E: only e₁²≤E² follows. Instead use
`q/Y ≪ d e₁²e₂/√x ≤ dE²/√x ≤ x^(−1/3+16η)`, Y=(x+4)/e₁².
Thus η<1/48 suffices asymptotically for the upper endpoint. At y<q the main term is **not uniformly O(1)**:
its Euler product can grow; O(x^δ) for any fixed δ>0 suffices, as does the at-most-one-term bound for the sum.
Allocate this δ inside the η margins. The Smith errors sum to d^(−1/2)x^(11/12+η); the extra endpoint errors are ≪x^(1/2+9η).
(iv) Expanding h(k)=1*ν and using bounded χ sums after inclusion–exclusion justifies the k-tail and hyperbola-boundary estimates.
The absolutely convergent square-divisor tail is ≪x^(1+δ)log(2E)/(dE), absorbed by the displayed error budget.
The three Euler contributions are 1+χ/ℓ, −1/ℓ², −1/ℓ². Hence E_ℓ=1+χ/ℓ−2/ℓ² and
`ℓ^(−j)(1−χ/ℓ)/E_ℓ = ℓ^(−j)ℓ/(ℓ+2χ)`; positivity follows from the L(1,χ) factor and an absolutely convergent positive correction.
Summing the first error to D=x^(1/6−ε) gives x^(1−ε/2+η); the two other errors are smaller with η=ε/10, ε sufficiently small.
This proves the advertised level **below** 1/6, not the endpoint without an ε loss.

**P.** g*(ℓ)=1/ℓ+O(ℓ⁻²) satisfies the dimension-one product axiom. At s=2.1, f(s)=0.16167079276492338>0.
The chosen ε<1/780 is sufficient for z>x^(1/13), so sifted survivors have Ω≤12, with multiplicities.
The displayed square-weight inequality is valid (including its S indicators). The standard nonnegative multiplicative mean bound has
prime sum 16·(1/2)log log x+O(1), giving Σ16^ω1_S≪x(log x)⁷. Cauchy–Schwarz then gives x/(log x)⁹.
However n=97, with shifts 101 and 389, belongs to the displayed set for every x≥97 and fails roughness for x=98¹³.
Fix the statement to “there are ≫x/(log x)⁹ such n which additionally have all prime factors >x^(1/13).”

**N and D.** First, f=1*h with squarefree-supported h(p)=c_p−1=O(1/p); CRT counting and completion of the absolutely convergent mean series give the stated model divisibility densities (and O_δ(x^δ) errors). T* at d=1 then gives λ₀>0.
In N's box there are ≍x/ℓ² pairs, all products are in the fixed class and have ℓ|mn+4.
For the positive comparison, c_p≥(1−1/p)² gives f(t)≥(φ(t)/t)²≫(log log x)⁻². This proves the logarithmic-saving obstruction.
The uniform polylogarithmic ℓ-range also fits inside both box lengths. It does not establish that W-tricking is the only possible formulation.
For D, write Σ_m α_m B_m, apply Cauchy–Schwarz, expand Σ_m|B_m|², then take absolute correlations.
Since Σ_{m≤x/N}τ(m)²≪(x/N)(log x)³, the stated correlation target is sufficient. The mixed terms and diagonal still require estimates.

**V′: substantive missing proof, not just exposition.** Put h_q(t)=∏_{ℓ|q}(δ_ℓ(t)−1).
For an inert prime, the complete-residue mean of |δ_ℓ−1| is **4/ℓ**, not ≤3/ℓ; for a split prime it is 4(ℓ−2)/(ℓ(ℓ+2)).
Replacing 3^ω by C^ω in Rankin fixes that harmless constant, but does **not** fix the argument:
`Σ_{q>Q} C^ω(q)/q ≪ exp(−c log x/log log x)` bounds complete-period averages, not
`Σ_{t≤x} Σ_{q>Q}|h_q(t)|`, its divisibility-progressions variants, or the corresponding prime sum.
Incomplete periods have unaccounted errors; support moduli extend to P(W)=exp((log x)^(B+o(1))), far beyond x for B>1.
“q≤x^(1/3) is exact counting” also requires summing the floor errors with the m-coefficients; BV only treats the retained prime moduli.
A suitable fundamental-lemma/truncation argument might repair this, but it is absent. No counterexample to the properly truncated TII_W is asserted here.
Required additional inputs are a divisor-weighted Type I comparison with λ_Wν_W, and
`λ_W Σ_{√x<p≤x}ν_W(p) ≫ x/log x`, with uniform errors. Either prove them or add them explicitly to V′'s hypotheses.
State the weighted Harman extension with its size/error controls; the combinatorial extension is plausible, not the problematic arithmetic step.
Also put **mn≤x** explicitly in TII_W (and the Type I sum); as printed the unrestricted inner sum is not the finite sieve hypothesis.

## Independent computation and citation checks

All shell invocations used `ulimit -v 6000000` and `timeout` (the initial pwd used a smaller memory cap); largest timeout 600 s.
Arrays were inspected first: spectrum at 10¹⁰ uses ≈3.3 GB; typeii at 4·10⁸ ≈3.6 GB; jobs ran sequentially.
Recompiled with `gcc -O2 -Wall -Wextra -lm`: `spectrum 10000000000` and `typeii 400000000 97` match their committed data **byte-for-byte**.
The latter confirms 105771 prime S-pairs, A*=127232704, B_a*=0.03742 at N=20000, and exact B=T for the parity control.
`uv run --with numpy python scripts/z56_k4bilin_firoute.py` likewise matches `firoute.txt` byte-for-byte, including 0.7570 and 0.9081.
Independent trial division at 10⁶ gives Σa=352832, #positive=2254, #S-pairs=2037, #prime S-pairs=535,
Σμa=−3904, Σλa=−4800, Σa*=313920, Σμa*=−576, Σ_prime a=95296, Σ_prime a*=82688: all agree.
Independent residue enumeration recovers all eight exact densities 1/(ℓ+2χ); N's finite box gives 396 pairs, zero a*-mass, model mass 404.84879196545256.
These checks are reproducible with `scripts/z56_xrev_k4bilin_check.py`; they use bounded-memory trial division, not the lane's segmented sieve.
Read the primary FI 2009 text, Lemma 4.1/(4.2), and Nath–Xie arXiv:2501.16723, (3.4), Lemma 3.6 and §5: the invoked input formulas agree.
Fetched/read Maynard arXiv:2006.08250, Theorems 1.2–1.3: the small δ, factor-size restrictions and prime-minorant distinction agree.
Revisited Teräväinen's Harman notes (2015/01/harmans-sieve.html), Theorem 3 and proof: both Type I and Type II are prerequisites.
Lichtman's 66/107 remains an explicitly abstract-only citation here; no blanket “best possible/current record” claim is certified.

## Required fixes, priority order

1. **Major:** downgrade V′ to a proposed implication pending the model lemmas, or add those lemmas as hypotheses; fix finite support and qualify the claimed W-cutoff necessity. Update §§0, 4 and the proposed FRONTIER text accordingly.
2. **Required:** correct Proposition P's universal roughness assertion; retain the stronger lower bound for the explicitly rough subset.
3. **Minor but necessary:** repair T*'s e₁²≤E typo and small-endpoint O(1) assertion as above; retain sufficiently small parameters and ε losses.
4. **Scope:** write “approximately 0.4%” for rounded floating diagnostics; replace “must be W-tricked” by “the comparison must address the exhibited local obstruction.” Alternative coefficient restrictions/models are not ruled out.

The **narrowed** verdict follows from T*, P, N and the scoped prime-route budget. The revised diagnostics are honestly non-probative of uniform Type II.
Accept these surviving results after the fixes; do not record “TII_W alone ⇒ P(4,15)” as an established conditional theorem yet.
