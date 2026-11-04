# Hostile cross-model review — FAMATTACK

**Verdict: ACCEPT-WITH-FIXES.** The main-term strengthening and the **narrowed** verdict survive;
there is no proof of positivity of R(p) for all sufficiently large primes. **ES remains OPEN.**
Reviewed `side-agent/z56-famattack` at `9e52e1f312cddb828da74d1bd7714494c1fdbacc`, not a moving draft.
Independent proof audit, independent census/statistical code, and source-engine reruns; no reliance on §8's verdict.

## Per-claim decisions

| Claim | Classification | Finding |
|---|---|---|
| Prop T: effective tiled genus lower bound | CORRECT | Per-window estimate is genuinely available before GENUSLVAL's first inequality; disjointness and finite-union errors work. Coefficient 0.0146005080955511. |
| Prop T′: tiled exact-class density | CORRECT | GENUSX hypotheses are preserved by strict margins; finite minimum δ is positive. Coefficient 0.00383263337508215. |
| Thm J: R ≥ ΣM^cls + ΣE; CU implies FA | CORRECT | Exact algebra and disjoint positive counts; choose the tiling loss η smaller than 28/(75π⁴), and CU parameter ε > 0. This is a sufficient reduction, not necessity. |
| Lemma L(a)–(c) | CORRECT | Divisor bijection, swap involution, three factorizations, and subtraction for privacy all check. The span formulation applies to bounded windows. |
| Lemma L(d) | CORRECT | p ≡ 1 (4), p ∤ u, odd part, and multiplicities are essential and now present. Reciprocity and the factor at 2 are correct. |
| Prop V(i)–(iii), displayed theorem | CORRECT | Expand the square, test R_j = 0, and use nonnegativity to extract one summand from an average. “Only” in (iii) means from that inequality alone. |
| Prop V's Poisson interpretation | CORRECT-WITH-FIX | The required condition is Σw_j M_j(M_j−1) > 0, not that every window have M_j > 1. |
| §3.1 engines; §3.5 census and decisive genus masses | CORRECT in audited ranges | Independent value-marking census agrees exactly; source counts and selected genus masses reproduce. Genus masses are floating-point evaluations of exact finite sums. |
| F1 registered outcome and dependence evidence | CORRECT-WITH-FIX | Leads triggered, kill condition not met, and positive net dependence all reproduce. The blanket negative-correlation magnitude bound is false. |
| Near-squares; Poisson tail arithmetic | CORRECT as EVIDENCE / Assessment | Both near-square baselines and model integrals reproduce; neither supplies a pointwise or causal theorem. |
| “No exact relation” / “no coordinate system” rhetoric | CORRECT-WITH-FIX | The swap itself is an exact cross-class relation. No theorem excluding every coordinate system or every other link is established. |
| “narrowed”, not “dead” | CORRECT | Main terms improve, residual remains open; positive average dependence does not preclude a pointwise compensation theorem. |

## Proof reconstruction and source check

1. GENUSLVAL Lemma 2.3 gives two distinct ordered pairs (u,2w),(2w,u) per admissible (u,w).
   Its projector leaves coefficient 1/φ(u) in front of Ση εη Sη. Prop 2.4 makes only η=1 survive;
   H_u/φ(u) ≥ (4/π²)(p/(p+1))/u and Prop 2.5 gives (2/π²)(α₁−α₀)log p−O(1).
   Thus the *restricted* genus mass, not just the full mass, has coefficient (8/π⁴)(γ−β)(α₁−α₀).
2. I checked those input steps: primitive conductors multiply to 4up, the twisted character remains
   nonprincipal because p divides its conductor, window subtraction cancels constants, and the nonsquare
   terms in the u-average save a power under α₀ > τ²(1+α₁)+3ε′. No rectangle optimality is used.
   The decisive external source, https://arxiv.org/abs/2511.17778 (v2), explicitly states Burgess for
   primitive cube-free modulus and all integer r, and explicit constants for r ≥ 3. The used conductors qualify.
3. For a strip with right endpoint a_i, C3 reduces to a_{i−1}(1−τ²) > τ²+τ²h+3ε′;
   a fixed lower margin permits h,ε′ small. The upper margin ensures β_i < γ_i. Distinct strips cannot
   duplicate a pair: the odd coordinate identifies u. Choose all margins, r, and finitely many strips before p.
   Integrating 3/4−5a/4 from 1/15 to 3/5 gives 8/45, so the effective lower bound follows.
4. For T′, use β_i = 2a_i+τ+margin and a_i < 1/5. These imply U's C2 as well as X's C2*.
   Integrating 3/4−3a from 1/15 to 1/5 gives 7/150. X's errors sum to O(p^{−min δ_t}log p).
   M^cls=M+T_u and R−M^cls=T_w+T_uw then prove J; CU supplies the positive leftover εΣM^cls.
5. L(a) follows from m=(n+u)/B=4uC−1, with inverse C=(m+1)/(4u); L(b) is swapping u,B;
   L(c) follows from gcd(n+u,n+u′) dividing u−u′. For odd ℓ|p+u, p∤u excludes ℓ|u and ℓ=p,
   so (ℓ/p)=(p/ℓ)=(−u/ℓ)=χ_{−4u}(ℓ). Multiply over N′ and use (p+u)/p=(u/p).
   Finally m≡−1 (4u) is odd and χ_{−4u}(m)=−1. Squares correctly annihilate each tile's genus mass.
6. V(i) is Σw(R−M)² ≥ ΣwM²−2ΣwMR. For V(ii), zero is consistent with the bound exactly
   when V ≥ ΣwM². For V(iii), a single term can exhaust V_𝒫 without extra hypotheses.

## Independent numerical audit

All shell runs used `ulimit -v 6000000`, CPU limits, and `timeout`; Python ran through `uv`.
New bounded audit scripts: `scripts/z56_xrev_famattack_census.c` and `scripts/z56_xrev_famattack_check.py`.
The C audit marks n=4uBC−u−B directly for u<B, without factoring n+u; memory is N+1 bytes.
The Python audit independently sieves interval primes, recomputes statistics, and checks source-engine samples.

| Check | Recomputed result |
|---|---|
| Complete 5 ≤ n ≤ 7,999,801, n ≡ 1 (4) census | 1,711 zeros: 13 primes, 1,413 odd squares, 285 other composites; byte-for-byte same zero list. Composite decades: 1,8,24,60,95,97. |
| Independent census through 10⁷ | Exactly the stated 14 prime zeros, largest 8,813,281. |
| Original exact engine | Existing brute checker: 1,499 odd n from 5 through 3001, no mismatch; all 299 nonsquare zeros and 33 spread-out high-p grids reproduce. |
| Genus engine | M(409)=3.9991, M(810001)=24.2513, M(8813281)=29.0834, all R*=0; 810001=241·3361. Three tested squares give M=0; R*(1000009)=20. |
| Dataset prime enumeration | Exactly 108,397 / 48,139 / 23,928 primes; all stored R positive and every R equals twice its grid sum. |
| Within-840 lead z-values | 10⁸: u01 −25.96, u02 −4.96, u04 −6.82, C34 −50.12; 10⁹: u01 −14.08, C34 −11.08; hold-out: u01 −8.78, C34 −8.62. |
| Joint-empty pooled k=8 ratios | 3.201 / 1.585 / 3.419; all k=2…8 entries agree with the table. |
| L-proxy controlled source rerun | C12 at 10⁹: +0.449; C34: −0.125. Residual off-diagonal shares u +.029/+.061, C +.264/+.308, as reported. |
| 965 near-square primes | Membership/primality checked; pooled total ratios .85835/.84315, and all pooled per-window ratios reproduce. |
| Model rerun | c=.0808: total 12.27, tail-one exponent 3.83; c=.0073: 1.148·10¹⁴, exponent 57.0; other exponents 44.6 and 124.1 reproduce. |

Limits: I did not regenerate every high-p grid, rerun the 1330-column/medium-prime regressions,
or independently certify the inherited exhaustive claim through 10¹⁰. None is needed for the accepted theorem
or the scoped narrowed verdict. The committed audit permits reproduction from an archive of the reviewed revision.

## Required fixes, in priority order

1. **Correct the evidence compression in §0, §3.2's final reading, and §6.** “All |r| ≤ 0.08” and the
   blanket “−0.02…−0.08” omit C34: −0.15222 within 840 at 10⁸ and −0.157 with L-proxy controls;
   at 10⁹ the controlled value is −0.125. Restrict that range to the u-window lead or report both.
   Replace “no compensation” by “some negative pairs, but net positive covariance and excess pooled joint emptiness”.
2. **Scope the claimed absence of links.** L(b) explicitly maps a class hit at u to a class hit at
   u′=B=(p+u)/m: (p+B)/u ≡ −1 (mod 4B). Thus the literal “no exact relation … beyond small primes
   and parity” in §2.3 (also §0) omits its own swap. Say no analysed link forces a first hit when all
   windows are empty. Replace §3.3's universal “No coordinate system” by a statement about the tested partitions.
   Keep the proposed dead-end line explicitly method-scoped, not a theorem killing union or variance routes.
3. **Fix the Poisson criterion after V.** ΣwM < ΣwM² is equivalent to ΣwM(M−1)>0; having every M>1
   is sufficient, not necessary (w=(1,1), M=(2,1/2) is a counterexample to necessity).
4. **Keep the model conclusion an Assessment.** “Checkable only with a mean near the full count's” is
   not proved: an upper bound on a Poisson tail integral is neither a deterministic checking threshold nor
   a lower bound on the true family mean. Use “this model with the proved coefficient suggests an impractical cutoff”.

With these corrections, bank Props T, T′, J, L and the displayed Prop V; retain the statistical findings as
finite-range evidence only. The registered F1 kill condition really was **not met** (checked against d99773fc).
