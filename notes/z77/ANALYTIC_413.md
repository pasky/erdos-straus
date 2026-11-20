## §0

Result: On a primorial fibre in every long interval, even adding all short noncoprime endpoint-pair certificates does not remove the log-log loss in the **number of short witnesses** at the z75 all-integer height.  Label: PROVED (relative to the upper-bound sieve in `EXSET_I3.md` Lemma 4.2 and Mertens).

Scope: Actual integer counts for bounded certificate height, not lower bounds on the number of zeros. No improvement to the uniform exponent for R(n), to the fourth-root bound for N₂, to e*(n), or to the full ES exceptional-set exponent. ES in ℕ remains open.

Review: cross-model (`data/z77/ANALYTIC_413_REVIEW.md`, Opus; scope and presentation fixes applied).

Triage: BARRIER-SCOPED

STATUS delta: none

## 1. Keep the two-prime average

Assessment of the proposed upper-bound method: the identities below are exact (size estimates use `Z53_SQSIEVE.md` Lemma W); the square-root kernel comparison and the §2 prime savings are hypothetical. No lower bound on the actual off-diagonal is claimed.

Notation and positive square detector as in `notes/z76/ANALYTIC_34.md` §2. Discard u=B at divisor-bound cost. There are J unordered prime pairs Q=qr, P<q<r≤2P, J ≍ P²/(log P)². The off-diagonal needed is the **signed** average of S_Q (with an absolute constant as coefficient); symmetry permits unordered pairs, and taking an absolute value of the average is sufficient. The diagonal of the square detector costs ≪ε n^ε V/P. Use L=P²W/V; the individual Poisson lengths QW/V are comparable, not identical. Write a_Q,h(C)=V/(4QC) Φ̂(hV/(4QC)).

First separate the nonunit frequencies, not just h=0. For any h,

    G_C^Q(h) = G_C^q(h r⁻¹ mod q) G_C^r(h q⁻¹ mod r).

If h=q b with r∤b this is K_q(C) G_C^r(b); if Q|h it is K_q(C) K_r(C). No condition on n is needed; for q|n the special class 4Cn+1=0 is absent. If Q≤W and L≥1, the **entire nonzero imprimitive contribution** for each Q is

    ≪ W/√P + W/P².

Indeed the absolute C-sums of K_q and of K_q K_r are ≪ W (sum the exceptional progression majorants over C, as in z76), the primitive local G is ≪√P, and Σ_{b≠0} L⁻¹(1+|db|/L)⁻² ≪ 1/d for d=q,r,Q by integral comparison. This uniform estimate includes same-reduced-fraction resonances across different moduli. The h=0 modes cost ≪ V/Q+V/W as before. Take P=n^{ρ+o(1)} with ρ=β−θ, as required by the square detector diagonal. At the binding shape γ=α=θ, ρ=1−3θ>0, all these terms fit the target. Away from that shape we do not claim this discard always suffices.

Here is Cauchy **after** putting the unordered pairs *and* h on the inside. Truncate primitive |h|≤L n^ε, with power-negligible tails by Schwartz decay, choosing the decay order after ε. Index i=(Q,h), x_i=h/Q, t_i(C)=G_C^Q(h)/√Q, b_i(C)=√Q L a_Q,h(C)/P, so |t_i|≤4, |b_i|≪1. With T the truncated primitive part of the normalized prime-pair average,

    |T|² ≪ P² W [ (JL)⁻² Σ_{i,j} K_ij ],
    K_ij = Σ_{C∼W} b_i(C)conj(b_j(C)) t_i(C)conj(t_j(C))
                          · e(−n(x_i−x_j)/(4C)).                          (1)

The bracket is real nonnegative; individual cross terms need not be. This is Cauchy only in C, before any triangle inequality in i. The diagonal contribution to the bracket is O(W/(JL)) by rapid decay in h. Since each fraction is reduced and the pairs are unordered, x_i=x_j iff i=j. For i≠j there are **three** periodic conductors (upper bounds for the periods of the trace product): Q for identical moduli with unequal h, qrr′ for a shared prime q, qrq′r′ for disjoint pairs. In the middle case the q-traces have frequencies h/r and h′/r′ in F_q, not generally equal (nor independent); they agree exactly if hr′≡h′r mod q. This congruence alone does not make the real phase constant. In the disjoint case CRT gives four local factors but no orthogonality on the graph (C,1/C). No factorization of the **real exponential** into independent linear characters in q and r follows from CRT. A shared local factor or q′₁=q′₂ is not grounds for dropping the other terms.

At the binding shape L=n^{ρ+o(1)} and the diagonal alone costs P W/√(JL)=n^{θ−ρ/2+o(1)}, which fits. But the **signed** off-diagonal contribution to the bracket must be bounded above, in this Cauchy argument, on the scale n^{θ−2ρ+o(1)} to certify n^{θ+o(1)} for T. If one uses a termwise W^{1/2} majorant even for all nonresonant normalized kernels (not proved), its output for T is of order P W^{3/4} in exponent arithmetic. This only fits for θ≥4/13: the excess in the *kernel* exponent is θ/2−(θ−2ρ)=2−13θ/2. At θ=3/10 the deficit is n^{1/20} in the signed mean of kernels, not the absence of a diagonal saving. Disjoint pairs have proportion 1−o(1); their period ≍P⁴ equals the C-length in exponent at 4/13 and exceeds it below. Completion with a free complete-period orthogonality is not justified. This calculation caps the **uniform square-root majorant in (1)**, not signed dispersion, a second average over C-shifts, or all large-sieve estimates.

## 2. Two different meanings of a prime saving

*Further differences after (2) of z76.* Applying the diagonal observation of z76 §5 to the binding vertex: Once the first shift by hQ has removed G, the z76 **positive diagonal majorant** P W/√H is already ≥P²√W by HQ≤W. At the binding vertex this requires 2ρ+θ/2≤θ, i.e. θ≥4/13, independently of how well one bounds the subsequent nonzero differences. An ordinary (step-one) A-process on the resulting unweighted model phase is exponent-pair substitution, already included when the substituted pair lies in the z76 optimized hull. Requiring that second shift to be a multiple of Q does not give free new periods: it increases the derivative scale by Q instead of 1 and shortens the admissible shift range. This is not an assertion that the full signed shift expansion is bounded below by its diagonal.

*What if the whole z76 bracket really had prefactor P^a instead of √Q ≍P?* This is arithmetic of a proposed estimate, **not a proved improvement**. Use the z76 pair k=1418/5119, l=2917/5119 and keep its other hypotheses and both terms of (3). Write r=β−θ, j=2(ar+γ−θ), d=1+2r+j−β−2γ. Then the final term exponent is ar+((1+l)γ+kd)/2 for d≥0. At vertex 1 one needs θ≥2m/(1−l+6m), m=a+(1+a)k; at vertex 2, where r=0, one needs θ≥(1+l+k)/(4+2l+3k) regardless of a. Exact three-vertex checks:

|a|vertex 1 requirement|global exponent for this substitution|
|---|---:|---:|
|1|7955/24966|7955/24966|
|1/2|9373/30321|4727/15282|
|0|1418/5355|4727/15282|

Even the *first* vertex with a square-root-of-P saving misses 4/13 for this pair. Other pairs or block-dependent arguments are not excluded. At the fourth-root shape W≍U² the unchanged shift majorant is ≥P²U, and the Cauchy model P W^{3/4} does not yield o(U). Furthermore a bound for the 4-divisible level is not a bound for **all** N₂ cycles. Fixed C gives just the divisor factorization (4Cu−1)(4CB−1)=4Cn+1; a bound per fibre does not count occupied fibres. No new such occupancy estimate here.

## 3. A sharp height qualification on the z75 lower tail

We now address the endpoint-pair proposal of `notes/z75/ANALYTIC_PUSH2.md` §4 and `EXSET_I3.md` §§4.5, 7, specifically for **many short** witnesses. Reset notation: let H→∞ denote interval length, λ=log H, W₀=⌊λ^{1/2}⌋, D=∏_{3≤p≤W₀}p over primes. In this section W₀ has nothing to do with the dyadic C-scale. Consider **any** interval I=(M,M+H] of positive integers. Let Z_Y(n) count the hits, *with labels*, of the following classes with their specified height ≤Y:

1. Native f=xy−1, 2≤f≤Y, residue n≡−x mod f, x|f+1. Allow all divisors x, hence both orientations by choosing either endpoint as x.
2. Endpoint pairs u,v≥1, uv≤Y, residue n≡−u−v mod uv, including ordered pairs with nontrivial gcd. A genuine hit for a middle letter divisible by four needs a stronger progression; we allow this whole progression.

These counts may overcount words; every word presented at either height (ignoring the degenerate native f=0,1) is covered since its remaining letter is determined. All short U₇ moduli with residue divisor are covered by 1. We do not include an unbounded number of labels at uncharged heights, and do not require disjointness of hit events.

**Theorem.** For W₀^{1000}≤Y with log Y=o(λ), every I contains ≫H/(4D) integers n≡1 mod 4 with

    Z_Y(n) ≪ (log W₀)² + (log Y)²/log W₀.                              (2)

In particular take Y=exp(A(λ log λ)^{1/3}) for **any fixed** A>0, the *larger*, all-integer height of `notes/z75/ANALYTIC_PUSH2.md`. There are ≥H exp(−O(√λ)) inputs with at most O_A(λ^{2/3}/(log λ)^{1/3}) such hits. Thus it is **false** that ≫λ^{2/3} witnesses at that height could hold outside O(H exp(−cλ^{2/3})) integers, even adding all those nonunit endpoint pairs. This matches the multiplicity order in z75 at its height; no such improvement was claimed there. Applying z75’s smaller prime-case height exp(Aλ^{1/3}) to these **composite inputs**, the upper multiplicity on this fibre is even O_A(λ^{2/3}/log λ). An all-integer many-witness result at multiplicity δλ^{2/3} with that exceptional bound would need log Y ≫_δ λ^{1/3}√log λ for this union of presentations. The theorem is about an actual interval, not a lower bound on the cost of a proof architecture.

**Proof.** Take the single CRT fibre B={n≡0 (D), n≡1 (4)}. Its population in I is H/(4D)+O(1), with log D=O(W₀). A class n≡a mod d has relative density on B either zero or gcd(4D,d)/d (compatibility is equality modulo gcd(4D,d)); counting in I adds O(1) per compatible label to H/(4D) times this density. There are O(Y log(2Y)) labels of either kind by the divisor hyperbola sum, so the relative contribution of the entire boundary error tends to zero. For native classes x is invertible mod f, so (D,f)=1 is mandatory. The factor at 2 is at most 4. The resulting conditional first moment of all native labels is bounded by

    4 Σ_{2≤f≤Y, (D,f)=1} τ(f+1)/f ≪ (log W₀)² + (log Y)²/log W₀.

For clarity about the omitted prime 2: one can apply the proof of `EXSET_I3.md` Lemma 4.2 with q=1 sieving only **odd** primes ≤W₀; deleting the prime 2 multiplies its Mertens upper bound by at most 2, with the same level/error. In each dyadic block K≥W₀^{1000} this gives ≪K log K/log W₀ before dividing by K. For smaller blocks use Σ_{K<f≤2K}τ(f+1)≪K log(2K); summing the two ranges gives the display. No conditioning of a unit prime progression on a nonunit class is used.

For pairs the local factor relative to 1/(uv) at p|D is 1 when neither endpoint is divisible by p, zero when exactly one is, and p when both are. Indeed p|uv requires p|u+v, and D is squarefree. Dropping the 2-adic compatibility and using its maximal factor 4, sum the resulting nonnegative multiplicative weight over (u,v), with harmonic denominator uv. Dropping uv≤Y in favor of allowing **all** powers of primes ≤Y gives an upper Euler product. The ordinary local factor is (1−1/p)⁻²; at a pinned prime it is instead

    1 + p (Σ_{b≥1}p^{−b})² = 1 + p/(p−1)²,

whose ratio to the ordinary factor is 1−1/p+1/p². Mertens, and convergence of ∑p⁻², give an upper bound O((log Y)²/log W₀). In particular common primes genuinely restore the both-divisible cases, but not the full missing harmonic mass. This bound holds without any independence between labels. Markov on B proves (2), even for at least half its population after a constant adjustment. ∎

**What this does not settle.** Markov here bounds multiplicity from *above* by a quantity tending to infinity; these integers might all have a hit. Neither a loss-free upper bound for E_U or E_(★), nor removing the loss with **unrestricted** heights and counting all words, is refuted. The z75 result gives small native witnesses, whereas a method targeting zeros only need not provide many short ones. `EXSET_I3.md` Cor. 7.1 concerns native whole-avoider majorants, not the endpoint-pair count just estimated. For the full E(N) exponent the positive-tail or cap estimates still give no bias forced by ES failure; GRH/EH alone in those formulas supplies no such implication (`notes/z75/ANALYTIC_BREAK.md` §§5–6). No contradiction at odd squares, known composite zeros, numerator-eight zeros or prime (★)-zeros: nothing pointwise positive has been proved.

Replay: `ulimit -v 6000000; timeout 90 uv run --offline --no-project python scripts/z77_analytic413.py` (`data/z77/analytic413_checks.txt`). The script checks the entire affine triangle for each tabulated substitution by its vertices, CRT twists and exceptional modes by exact additive-phase coefficients, and the endpoint-pair fibre factors by counting classes. The cited native upper sieve and Weil bound are mathematical inputs, not numerical conclusions. These checks are not estimates for the signed nonresonant sum.
