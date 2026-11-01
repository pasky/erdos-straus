# GENUSX hostile cross-model review

Reviewed `side-agent/z53-genusx` at `28fadbed2e5bb096e610dc43df23651bedf2bb5b`.
**Verdict: ACCEPT-WITH-FIXES. Theorem X survives; ES and the exact-divisor remainder remain OPEN.**
Scope: independently re-derived §3, its Theorem U dependency, and every labelled PROVED identity in §§1,4;
checked the decisive Burgess source and reran the numerical evidence. No subagent verdict was used.

## Per-claim assessment

| Claim | Classification | Finding |
|---|---|---|
| Lemma 1 / CRT decomposition | CORRECT | A non-real CRT character has at least one non-real factor; expanding the two projections gives exactly the three T terms. |
| Divisor-level form | CORRECT | From p+u=2ww″, cancellation of units gives w″=−1 mod u; the mod-8 condition gives w″=3 mod 4. Genus weight is 2^ω(u)/φ(u). |
| Lemmas 2, 4.5 / BM component | CORRECT | Reciprocity gives (w″/u)=χ₋₄(w″)(w″/p); the four signs are 1,−χ₋₄(w″),χ₋₄(w″)(w″/p),−(w″/p). T_w subtracts M_BM. |
| Theorem X / (X.1), T_u | CORRECT-WITH-FIX | State explicitly that r is a positive integer. With the displayed C1,C2*,C4, the proof and effective power saving are valid; no missing arithmetic hypothesis found. |
| Theorem X / positive lower bound | CORRECT | Additionally requires Theorem U's C3 and compatible Burgess parameters. This is a density lower bound, not a lower bound for R. |
| Optimisation c_X | CORRECT | Maximum at α₁=19/120, product 121/5120=5445/230400, c_X≈0.0019409123; attained as a limit of strict admissible windows. |
| Lemma 4.1 / Corollary 4.2 | CORRECT | w>U₁ and w″>p/(2X)≥4U₁ make both projections injective; r_w is unique and w′=ceil(p/w). |
| Lemma 4.3 | CORRECT, scoped | The displayed second moment is diagonal. This does not prohibit dispersion or a different enlargement/rearrangement. |
| Lemma 4.4 | CORRECT | Count roots x²=−w″ mod u, put t=(x²+w″)/u≥1, and substitute u=2ww″−p. Retain w″=3 mod 4. |
| Proposition 4.6 | CORRECT-WITH-FIX | Counting bound and greedy construction hold. Its consequence concerns interval-sum magnitude bounds, not every possible hypothesis about interval sums. |
| Remark 4.7 | WRONG for k=3 | χ³=1 does not include nontrivial quadratic characters. Therefore B^(3)−B^gen is not a pure non-real layer. No proved theorem depends on this remark. |
| §5 certificates / numerical evidence | AGREEMENT | Counts, identities, direct densities, variance tables and ladders reproduce; one rounded inequality needs repair below. |
| “Narrowed; what remains is B2” | ACCEPT AS ASSESSMENT | Exact reduction is to two unbounded centred divisor layers. Neither a B2 equivalence nor a general no-go theorem is established. |

## Independent derivation of Theorem X

1. Extend ρ by zero outside odd squarefree w coprime to up. At each prime, multiply its local series by
   (1−z)(1−χ_D(ℓ)z). This gives precisely the displayed h(ℓ),h(ℓ²),h(ℓ³), including h(ℓ)=−1 at ℓ|2up.
   Thus wρ(w)=(1*χ_D*h)(w), with Σ|h(c)|c^(θ′−1)≪p^o(1), effectively, for θ′=1/2−ε.
2. Set q=4u. A unit residue w=s forces a,b,c coprime to q in w=abc. The resulting convolution over c
   is exactly h(c)/c times the window difference of Φ_(s/c); no divisor-of-p+u condition is imposed.
3. For C₀=p^ε<c≤Y/q, harmonic sums on a progression and τ(n)≪p^o(1) bound the window by p^o(1)/u.
   The h-tail then contributes p^(−εθ′+o(1))/u. For c>Y/q, use the unrestricted harmonic divisor bound:
   the error is ≪p^(−θ′(β−α₁)+o(1)). C2*,C4 imply θ′(β−α₁)>α₁+ε/2, hence ≪p^(−ε/2+o(1))/u.
4. For c≤C₀ split b at B₀=q p^(τ_r+ε). The split is exact, with unit restrictions implicit in inverses.
   On b=v₀+qk, χ_D(b)=χ₋₄(v₀)(v₀/u)(q/p)χ_p(k+v₀q̄). This uses u,p=1 mod 4 and (q,p)=1.
5. Burgess is uniform in the shift v₀q̄. Write P=p^((r+1)/(4r²)+ε), K₀≈B₀/q.
   Partial summation gives |Σ_(B₀<b≤T,b=v mod q)χ_D(b)/b|≪_r P K₀^(−1/r)/q
   ≪p^(−ε/r)/q. The outer Σ1/a costs only log p. Floors and an initial term are absorbed in the constant.
6. For b≤B₀, the a-window harmonic sum is q^−1 log(X/Y)+O(cb/Y), uniformly in its unit residue.
   Multiplication by χ_D(b)/b and summation give q^−1 log(X/Y)Λ(B₀)+O(cB₀/Y).
   Since u²p^(τ_r+2ε−β)≪p^(−2ε), this error is O(p^(−ε)/u), after a harmless constant.
7. Sum against h(c)/c. The common main term is exactly the memo's 𝔐_u, independent of s.
   Any fixed δ<min(ε/r,εθ′,ε/2) absorbs the effective p^o(1) factors and proves (X.1).
8. A is one unit class; A^gen is the average of the φ(u)/2^ω(u) classes in its square coset.
   Their identical main terms cancel, and averaging does not multiply the error by the coset size.
   Thus |T_u|≪Σ_(u≤U₁)p^(−δ)/u≪p^(−δ)log p. No relative-error assertion is needed.
9. For the positive density bound, Theorem U's convolution has conductor product 4up, with p in every
   twisted second conductor. Its u-average of L(1,χ_(−4up)) retains the positive n=1 term and bounds
   nonsquare n via squarefree Burgess sums in free u; C3 makes N^θ U₀^(−1/r) a power saving.
   H_u(1)/φ(u)≥(4/π²)(p/(p+1))/u and L(1,χ_D)>0 give c=(8/π⁴)(γ−β)(α₁−α₀).
   No individual Siegel lower bound is used. Optimising (3/4−3α₁)(15α₁−1)/16 gives the stated c_X.

**Source/effectivity check.** Visited [arXiv:2511.17778v2](https://arxiv.org/html/2511.17778v2), introduction and
Theorem 1.2: primitive cube-free conductors allow every integer r≥2, arbitrary interval shifts, and effective constants.
Its explicit threshold and divisor/log factors can be absorbed effectively into C(r,ε)f^ε; below that threshold
use periodicity and the trivial bound. For r=1, effective Pólya–Vinogradov supplies the quoted bound.
Prime-modulus χ_p is primitive and nonprincipal. All subsequent divisor bounds/Euler products are effective.

## Averaged-variable / B2 audit

p is fixed throughout. The outer u-range is a free squarefree interval, not a set of divisors of p±1.
w is a free squarefree interval; (w,p)=1 is automatic eventually since X<p. Its class s_u depends on p,
but (X.1) is uniform in *every* unit class, so selecting s_u is legitimate. The a,b,c variables factor free w,
not p+u. The c-coefficients depend on p but are bounded absolutely; no fictitious cancellation in c is used.
The b-progression's shift depends on p,u,a,c; Burgess is uniform in that shift. The a-sum uses absolute weights.
Genus-coset averaging is an exact finite identity, not an equidistribution assumption. Theorem U's auxiliary
L-series index n is also unrestricted; its u-average never imposes u|p±1. Thus there is no attached-average gap.
By contrast, on the exact shell u=r_w and w″=(p+u)/(2w) are attached to p: Burgess cannot simply be reused there.
The bankable reduction is X_𝔉=T_w+T_uw+o(1), with T_w=G−M and T_uw=R−G+o(1).
Both remain unbounded. Lemma 4.4 is a tied-divisor reformulation, not a proof that bounding G−M is equivalent to B2.
Separate X-w and X-uw bounds are a sufficient programme, not necessary individually for H⁻ (they could compensate).

## Numerical checks

`uv run --no-project scripts/z53_xrev_genusx_check.py /tmp/xrev_GENUSX` reruns the extracted engine and independently
computes statistics and raw-CRT densities. Commands use `ulimit -v 2097152`, CPU limits and wall-clock timeouts.
All 1,244 distinct saved engine windows agree; 1,249 saved records contain 1,437,466 shell records, zero identity errors.
The 150 squares contain 129,985 shell records, R=G=0 and E₁=−CBM; mean E₁/log²n=0.0042424913.
At 10001², a fresh D-mode run gives M=M^cls=0. All ten saved direct-density rows reproduce.
Independent all-pairs CRT calculation at p=100000049 gives R=2, G=3.4494233060, M=1.7177218144, M^cls=1.6111506195.
Selected M̂ reruns via PARI agree: 1.2292322374 (5212561), 1.5389346213 (8813281), 1.7263665984 (100000049).
M̂ is numerical evidence, not a newly certified class-number calculation; the full statistics use saved M̂ values.
At 10⁹,10¹⁰,10¹¹,10¹² the variance shares are respectively
(0.090347,0.929815), (0.103511,0.899390), (0.102287,0.928646), (0.097389,0.879579).
The corresponding swap-Poisson ratios are 0.999308,1.018195,0.882973,0.810351; all ladder summaries reproduce.
These are standard-window proxies, outside Theorem X's hypotheses, not a numerical test of its asymptotic bound.

## Required fixes, priority order

1. Specify integer r in Bu₁/Theorem X. Keep C1,C2*,C4 and, for positivity, Theorem U's C3 in every exported claim.
2. Repair §4.7: use B^(lcm(2,k))−B^gen, or for the pure cubic layer use B^(3)−B^(1).
   For example mod 7, χ³=1 selects character exponents 0,2,4; the quadratic character has exponent 3 and is absent.
3. Keep “B2” explicitly Assessment, with both T_w and T_uw unresolved; in §7 replace “needs cancellation of real
   characters” by “one sufficient route is such cancellation.” It is not a componentwise necessity theorem.
4. Prop 4.6 must say interval-sum *upper bounds compatible with |Σf|≤5*, not “every hypothesis” about interval sums.
   Exact signed interval data would determine f; multiplicativity/progression information is not covered.
   Indeed f(n)=(−1)^(n+1) already equals +1 on every odd w″ and has interval sums ≤1: magnitude-only scope is essential.
5. The six-of-nine observation survives rounding, but literal “G/M̂≥0.84” holds for only five: at p=1134241 the
   ratio is 0.839373039. Write “at least about 0.84” or “≥0.83.” Do not present the standard-window data as validating X.

**Final:** bank Theorem X's effective density equidistribution after the integer-parameter clarification.
Accept “narrowed” as a scoped assessment, not closure of B2 or of either remaining exact-divisor layer.
