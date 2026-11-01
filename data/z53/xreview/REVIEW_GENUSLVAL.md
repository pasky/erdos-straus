# GENUSLVAL — independent hostile review

Reviewed `side-agent/z53-genuslval` at `dc01f27bd749f0f8bbdba6cbc30baa5e5ed1211d`, especially `Z53_GENUSLVAL.md` §§2–3.
**Verdict: ACCEPT-WITH-FIXES (scope/wording only). Theorem U is CORRECT, unconditional and effective; “strengthened” is justified for FRONTIER §7.4.**
No mathematical gap was found in the constant `2/(3π⁴)`, the all-large-prime quantifier, or Proposition C in its stated restricted slices. ES remains OPEN.

## Per-claim decisions

| Claim | Classification | Independent finding |
|---|---|---|
| §1 definition of M_gen | CORRECT | Exactly `SINGLE_P_COUNT.md` Lemma 2.1, with ordered pairs; square-unit membership already excludes nonunits. Not M_BM, M₀, or R. |
| §2.1 Burgess, all fixed r | CORRECT | Full source checked, not merely its abstract; cube-free primitive conductors and effective conductor-uniform constants apply. |
| Lemma 2.1, character tails | CORRECT | Möbius removal of Euler factors and Abel summation give both stated bounds. |
| Lemma 2.2, hyperbola | CORRECT | Balanced cut and both remainder formulas re-derived; sign of the logarithmic tail in (b) is correct. |
| Lemma 2.3, genus subfamily | CORRECT | Mod-8 and odd-prime tests, projector signs, and the two-order weight agree with the repository definition. |
| Prop 2.4, window difference | CORRECT | Primitive conductors multiply to 4up; both nonprincipal constants and principal derivative constants cancel. Uniform power saving survives the h-convolution. |
| Prop 2.5, L-value average | CORRECT | Burgess in u after squarefree expansion controls nonsquare n; positive square n need no Siegel bound. |
| Theorem U / optimization / effectivity | CORRECT | All sums of errors are harmless, optimization gives 1/12, and r is fixed before p tends to infinity. |
| §2.8 square obstruction | CORRECT | At squares the second character becomes principal on its support, with identical unsigned sum and sign −1. |
| Prop C | CORRECT | Non-squarefree Euler factors, derivative sign, primitive discriminants, and omitted Euler factors all check. |
| §4 exact restricted-slice decomposition | CORRECT | Exact finite character expansion; its L-value approximation has the restrictions of Prop C. |
| §5 finite checks / §3.2 evidence | CORRECT on rerun | All 65 slices reproduced; independent literal square-unit checks and window reruns agree. |
| §7 “all that remains” of FRONTIER §7.3 | CORRECT-WITH-FIX | Restrict to eventual positivity of the aggregate prime count, not control of every individual coset or a full genus closed form. |
| Composite extension, large-sieve improvement, global closed form | Assessment only | Not proved here; they are not inputs to U or C and must remain unbanked. |

## Proof audit, line by line through the dependencies

1. **External input.** Read [arXiv:2511.17778v2](https://arxiv.org/pdf/2511.17778v2), pp. 1–3, especially Theorem 1.2.
   It gives an explicit bound for every integer r≥2, cube-free q, arbitrary interval length N, once q≥max(10¹¹⁴³,2^{4r−2}).
   Its extra factors involving log q, ω(q), m_r(q)≤τ_{2r}(q), and q/φ(q) are effectively O_{r,ε}(q^ε).
   The finitely bounded smaller conductors are covered effectively by periodic cancellation, enlarging C(r,ε).
   Thus the memo's (Bu) is available uniformly in conductor and character. Only r≥3 is used; no constant uniform in r is asserted or needed.
2. **L-tails.** For χ=χ*1[(n,e)=1], inclusion–exclusion gives |S(t)|≤τ(e)C f^θ t^{1−κ}.
   Integration of t^{−1−κ} gives (1+r); integration with log t gives the stated larger logarithmic-tail constant.
   When the average uses e=2m rather than squarefree e, replace it by rad(2m); τ(rad(2m))≤τ(2m). No change of bound.
3. **Hyperbola.** Put t=y/z. For two nonprincipal characters the error is exactly
   `−Σ_{a≤z}F(a)r_G(y/a)/a − Σ_{b≤t}G(b)r_F(y/b)/b − r_F(z)r_G(t)`.
   Choosing z=y^{1/2}(K_F/K_G)^{r/2} gives O_r((K_FK_G y^{−κ})^{1/2}), with 1≤z≤y under the stated hypothesis.
   With F=1, H(t)=log t+γ_E+r₁(t) yields the main term `L_G(log y+γ_E)+L′_G` and exactly the error bracket in Lemma 2.2(b).
4. **Genus projector.** For q=8uw, square units are 1 mod 8 and residues at every odd prime dividing uw.
   This gives (i)–(iii), including w₀=−(p+u)/2 mod 4. Each ordered pair weighs 2^{ω(u)+ω(w)}/(φ(u)φ(w)).
   The projector has factor 2^{−ω(u)−1}; including both orders leaves exactly `(1/φ(u))Σ_η ε_η S_η`, not twice or half that.
5. **Primitive characters.** For η=(·/d)χ₋₄^j, d|u, use its primitive representative (and η=1 identically for d=1,j=0).
   Write e=u/d. Then `ηχ_D=χ*·1[(n,2d)=1]`, with f_F=4^j d and f_G=4^{1−j}ep.
   Jacobi characters (·/d) are primitive of conductor d even when d≡3 mod 4; their discriminant is d* rather than d.
   Both conductors are odd squarefree or four times odd squarefree: v₂≤2, hence cube-free. Since u<p, p∤u, and p|f_G>1, G is never principal.
   Consequently f_F f_G=4up, not 16u²p. The actual finite-r window threshold is `(4up)^τ`, tending to exponent 1/4 only as r→∞.
6. **Window convolution.** Direct multiplication gives the stated squarefree h-factors and
   `Σ|h(c)|c^{−1+θ′}=p^{o(1)}` for fixed θ′<1/2, uniformly in u. At 1, H=(6/π²)∏_{ℓ|2up}ℓ/(ℓ+1).
   Cut c at p^ε. On the short part, β>τ(1+α₁)+4ε dominates K_FK_G≤p^{θ(1+α₁)+o(1)}.
   For η≠1, L_F L_G cancels between X/c and Y/c. For η=1, both L′_G and γ_E L_G cancel, as does −L_G log c.
   The remainder is H L_G log(X/Y). On the long c-part use Φ(y)≪(1+log X)² for y≥1 and Φ(y)=0 otherwise.
   The absolute h-tail gives a power saving; extending the short H-sum uses only L(1,χ_D)≪log(4up).
7. **Average in u.** Truncate each L-series at N=p^ν, ν=τ(1+α₁)+ε. Weighted tails total p^{−κε+o(1)}.
   For n=m², χ_{−4p}(n)(u/n)≥0; retaining n=1 gives `(2/π²)(α₁−α₀)log p+O(1)`.
   For nonsquare odd n=n₁m², n₁>1, the two progression characters have primitive conductors n₁ and 4n₁, both nonprincipal and cube-free.
   Expanding μ²(u) costs `Σ_e e^{−2+2/r}<∞` for r≥3. Abel summation gives |V(n)|≪p^{o(1)}n^θ U₀^{−κ}.
   Summing |V(n)|/n to N gives p^{θν−κα₀+o(1)}, negative by C3. This is an average over u, never over p.
8. **Assembly.** C1 puts every selected pair inside 𝒫(p), and the odd coordinate identifies it uniquely.
   `Σ_{u≤U₁}2^{ω(u)+1}/φ(u)≪log²p`, so the uniformly small per-character errors remain negligible.
   `H_u/φ(u)=(4/π²)(p/(p+1))u^{−1}∏_{ℓ|u}(1−ℓ^{−2})^{−1}`.
   Positivity of L(1,χ_D) permits dropping the last product. No quantitative lower bound for any individual L-value is used.
   Thus the coefficient is (8/π⁴)(γ−β)(α₁−α₀). At τ=1/4 its product maximum is 1/12 at α₁=1/3; at r=3 it is 1/24 at 5/16.
   For any requested loss, first choose a finite r and positive margins, then an effective p₀. No Siegel, zero-free strip, or limit uniform in r is hidden.
9. **Prop C.** Removing squarefreeness changes only the split local factor to `1+2Y/(ℓ−1)−(ℓ+1)Y²/(ℓ−1)`.
   The same weighted absolute convergence applies. With X=X_u, y₀=(4up)^τ p^{3ε}, the cut c≤X/y₀ leaves power-saving errors precisely when 1−α>τ(1+α)+5ε.
   The principal main term is `H[L(log X+γ_E)+L′]+LH′`; the sign of H′ is positive because H′(1)=−Σh(c)log c/c.
   The nonprincipal term is L_F L_G H_η. The relevant nonprincipal L and L′ are effectively O(log p) and O(log²p) (their moduli are ≤4up); writing L′/L inside the factored expression introduces no need to bound 1/L.

## Numerical audit

All executions used a shell timeout and virtual-memory limit (2–3 GB); arrays were inspected first (largest slice sieve ≈67 MB). Binaries were freshly compiled from the reviewed commit, not reused from `/tmp/z53slice`.
* Reran **all 65** recorded slices, all components, PARI L-values and Euler products to 2·10⁶: every recorded six-decimal direct/closed value agrees.
* For X≥10⁵: 18 slices, max absolute error **0.001150913635** at (8813281,5), max relative **0.129196454%**. For 10⁴≤X<10⁵: 15 slices, **0.003586750522**, **1.372128031%**. Other bin counts/errors also agree.
* Doubling the Euler cutoff to 4·10⁶ at (8813281,5) and (99999989,1) leaves the quoted error bounds intact. These approximations remain EVIDENCE, not interval-certified L-values.
* Independent enumeration of literal sets `{a² mod q:gcd(a,q)=1}`, with rational weight 1/|G²|, gives M_gen(409)=**18484931/4622310**, M_gen(577)=**75785224/14159145**; both agree with the engine. n=9,961 give exactly zero.
* Independently summed **all even B**, not just the proposed subfamily: at p=409, slices u=1,5,13,21 are **2620066/2311155, 0, 1/6, 1/3**; at p=577 they are **1429408/2831829, 2/3, 1/6, 1/3**. All match the projector.
* **45,056** character-identity checks include even arguments, ramified primes, and divisors d≡3 mod 4; primitive discriminants, product 4up, and omitted factors all agree.
* Reran §5 windows: family/main ratios **0.9721, 1.0031, 0.9682, 1.0389**; zero genus-test mismatches. Full M_gen at 5569,9601 is **6.240720681205, 7.926241150372**.
* Streamed the census: minimum M_gen/log²p **0.083869562649**, minimum M_gen/M₀ **0.569603698893**, both at 8089; maximum ratio **1.525456899971** at 15461. The samples are not all primes through 10⁷.
* Independently re-aggregated, rather than regenerated, `decomp_raw.tsv`: mean deficits P=**0.0091750512**, total=**0.0118450849**, hence **77.46%**; all six mean percentiles agree. This is restricted-family evidence only.

## Required fixes, in priority order

1. **Scope of §7 / proposed FRONTIER item 3.** Replace “what remains in §7.3 is entirely … X(p)” / “all that remains of this item” by: **“For eventual positivity of the aggregate (★) prime count, the genus lower-bound requirement is now met; control of the non-real remainder remains open.”** U does not resolve genus obstructions at an individual modulus/coset, address every n, or supply the global closed form left as Assessment in §3.1. Closing §7.4 is justified without these stronger readings.
2. **Avoid a new asymptotic in §4's shorthand.** `Σ₁≈LH log X>0` must not be read as a proved uniform equivalence when both u and p vary. Retain the full additive L′ and H′ terms from C; no bound in this memo makes them uniformly o(LH log X). This does not affect the window argument, where they cancel exactly.

**Bankable result:** U and restricted Prop C as stated. **Not bankable:** a full global genus formula, per-coset forcing, or any estimate for X(p). No proof change or weaker constant is required.
