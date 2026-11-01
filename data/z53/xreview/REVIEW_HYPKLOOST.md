# HYPKLOOST cross-model hostile review

**Verdict: ACCEPT-WITH-FIXES. Do not promote K(c) or the proposed FRONTIER text unchanged.**
Reviewed `side-agent/z53-hypkloost` at `d12819b02f8d763f9bfd21226122e5e831c7e328`.
ES remains OPEN. The scoped “narrowed” verdict survives, but the claimed universal DFI obstruction does not.

## Per-claim audit

| Claim | Classification | Independent check / qualification |
|---|---|---|
| (1.1), O1, F1 Parseval | CORRECT | Expand each divisibility indicator into additive characters, reduce h/q to a/d, then sum pairs. Distinct reduced frequencies are orthogonal under uniform n mod L; subtract the constant mode for covariance. Relative bins need not be orthogonal. |
| O2, K(a) | CORRECT | Coprime inverses satisfy B B̄ + u ū = uB+1 by congruences and the interval (1,2uB). Substituting b=a+c in the two detectors gives exactly (4.1); the 4-condition is correctly retained separately. |
| O3, coprime zero mode | CORRECT | Under 2U,2V<p a noncoprime pair cannot satisfy B dividing p+u. Möbius inversion gives the stated uniform O(U log(2m)/m) error: sum over B when U≥V, over u when V≥U. |
| O4, O5 | CORRECT | Progression counting and m=4uC−1 give the stated transformations; 0<u<m makes u the least positive residue −p mod m, and the converse recovers integral positive B,C. |
| B(a) | CORRECT | Periodising g(t−F) gives Fourier coefficients ĝ(h)e(−hF); decay gives uniform absolute convergence. Reindex ℓ=kq−n−s. The Fejér lower/upper bounds follow from sin x≥2x/π on [0,π/2] and absolute sin≤1. |
| B(b) | CORRECT | Exact quadrature on the odd q_max-grid points kills every nonconstant frequency when H<q_max/2. Every sample is constrained nonpositive. Uniform n mod q removes all nonzero h when H<q_min, giving exactly the stated intersection of hypotheses. |
| B(c) | CORRECT | The sharp threshold is valid; a citation-free construction is given below, independently verifying the Selberg-based conclusion. |
| C(a) | CORRECT | Sum over d dividing gcd(q,M) to obtain g·1[g divides n+s]/q. CRT gives precisely that conditional probability, not an arbitrary weighted truncation. |
| C(b) | CORRECT | Each nonprimitive Fourier mode is invariant under some order-ℓ subgroup. The signed tensor perturbation of uniform measure has masses 0,1/q,2/q, mass 1, and zero mass at 0; it annihilates every invariant summand. Thus mean(f)=ν(f)≤ν(1_0)=0. |
| C(c) | CORRECT | Apply C(b) separately to each positive-mean pair. Primitive frequencies need not form complete Ramanujan sums unless weights have Ramanujan form. The quoted high-conductor multiplicity is obtained by counting factorizations of kd/4. |
| E(a,b,c) | CORRECT | Fejér nonnegativity bounds hits. In the squared-sum identity the diagonal contributes (H+1) times the number of pairs; removing the zero mode proves the stated floor. Optimising square-root max input gives the geometric mean of side lengths, not a power improvement on their minimum. Empty containing boxes are vacuous. |
| K(b) | CORRECT | The additive zero modes are ≥U/2 and ≥V/2; the coprime asymptotic gives the analogous ceiling. It applies only to zero mode plus a nonnegative error allowance, not an exact evaluation or a coupled estimate. |
| K(c), DFI Theorem 1 | WRONG as a source claim and obstruction | The actual theorem is a SUM of two terms, not the PRODUCT quoted in the memo. It gives power savings in admissible skew ranges; explicit counterexample below. Arithmetic conditional on the erroneous quotation does not repair the source claim. |
| K(c), DFI Theorem 2 | CORRECT | Source (1.5) agrees. Comparing p^(3/8)(UV)^(11/96) with (UV)^(1/2) gives the necessary exponent UV>p^(36/37), ignoring constants/epsilon. This restriction is for Theorem 2, not all DFI estimates. |
| K(c), Bettin–Chandee | CORRECT-WITH-FIX | The first summand and the necessary C̄≲p^(1/21) calculation are correct. The second summand is mistranscribed in LIT_CHECK.md; correct it as below. The necessary condition alone is not sufficient. |
| Q(i–iii) | CORRECT | Expanding (cu−1)(cB−1)−pc=1 gives the equation. Fixing d≡−1 fixes the double coset, not the translations inside it. Conjugation gives lower-left −p. Additive detection shifts the Fourier index by a c-dependent k. No general Kuznetsov impossibility follows or is claimed. |
| §7 Heath-Brown specialization | CORRECT | Primary Theorem 14, printed p.562, confirms exponent d^(-(n−1)/(n−2)). The homogenised cubic is primitive linear in z with coprime coefficients, hence irreducible. With B4=1, T=V and k≪V^(2/(3√3)+ε)(log p)^5. This is only an upper bound for auxiliary curves. |
| F1/F3, LP, window numbers | CORRECT-WITH-FIX | Decisive numerical quantities reproduce; the prose claiming G(0)=0 for all subthreshold LP rows is false. See numerical audit. |
| Labels / survivors / verdict | CORRECT-WITH-FIX | Positive mean is correctly distinguished from positivity at one p; negative-mean certificates and joint/nonlinear methods remain open. Restrict the DFI obstruction to the actual theorem/range before recording the verdict. |

## Independent sharpness derivation for B(c)

Let h=q_max/2, choose 1/(q_max+2)<δ<1/q_max, and put
P(x)=Σ_{j=1}^h sin(jπ/(h+1))e((j−1)x), G(x)=(cos(2πx)−cos(2πδ))|P(x)|².
Then deg G=h, G(0)>0, and G≤0 at every required noninteger grid point.
The sine-vector recurrence gives ∫cos(2πx)|P|²=cos(π/(h+1))∫|P|².
Consequently ∫G=[cos(π/(h+1))−cos(2πδ)]∫|P|²>0. This verifies sharpness without relying on a citation transcription.

## Required fixes, in priority order

1. **MAJOR: replace DFI (1.4) and retract its universal no-saving consequence.**
   I inspected the actual PDF `sources/dfi-1997-kloosterman-fractions.pdf`, including the rendered printed p.24.
   Its Theorem 1 states
   `|B| ≪ ||α||||β|| [(U+V)^(1/2) + (1+a/(UV))^(1/2) min(U,V)] (UV)^ε`.
   With s=min(U,V), L=max(U,V), its ratio to the trivial norm factor √(sL), before epsilon, is
   `sqrt(1/s+1/L) + sqrt(s/L+a/L²)`.
   For a=p, U≈p^(1/5), V≈p^(3/5), this is O(p^(−1/10)), while C̄≈p^(1/5)/4.
   Both coordinates are below p and UV≪p: this is not an excluded geometric range.
   Thus “DFI only if C̄≲p^(1/37)” is false; that restriction belongs to Theorem 2 only.
   Correct LIT_CHECK §3, K(c), summaries §§0/7/9/10, and any derived ledger language.
   This is a saving for the KF sum, NOT automatically for N: the zero-mode ceiling K(b) still applies, and summing all b or coupling the other relation needs further work.
2. **Source repair:** [Bettin–Chandee, arXiv:1502.00769](https://arxiv.org/pdf/1502.00769), Theorem 1 (1.2), printed p.2, has second term `(AMN)^(3/8+ε)(AN+AM)^(1/8)`, not `(AMN)^(1/4+ε)(AN+AM)^(1/8)` as LIT_CHECK states. The first-term obstruction used here survives.
3. **MINOR:** correct the LP prose: H=31,47,71 have mean zero but G(0)=1, already in the saved output and identically in my rerun. The relaxation admits G(0)=0; it does not force the solver to return it. The theorem only forces nonpositive mean.
4. **Scope:** retain “narrowed”, not “dead”; distinguish no obtained saving for the block count from the now-demonstrable skew-range saving for a KF sum. Keep the proposed FRONTIER claims blocked until fixes 1–3 are propagated.

## Numerical audit

All shell commands used timeouts and `ulimit -v 6000000` (or a tighter limit); Python runs used uv.
Reproduction checker: `scripts/z53_xrev_hypkloost_check.py /tmp/xrev_HYPKLOOST`, under a 300-second timeout.
The script also imposes an address-space limit; arrays are at most 3000×83, with no dense pair×prime products.

- Recomputed all 10,800 rows' headline moments independently. Prime 10¹²: Var N=0.315036, zero fraction=0.924, relative/absolute cross shares=0.1419887164/0.1488628385. Prime 10¹⁰: Var N=0.2698648889, shares=0.0357540088/0.0182607344. Both square samples have Var N=0 and shares −1. Other control shares agree too.
- Rebuilt conductor C source and reran first/last rows of all seven sets: all 14 full-scale rows agree exactly at stored precision. Independently evaluated c_d(m)=Σ_{r dividing gcd(d,m)}r μ(d/r) with rational arithmetic for eight small n, U=2,V=3; maximum printed-bin discrepancy 4.44445·10⁻¹¹.
- Reran the entire 400-resample bootstrap analysis: `cond_stats.txt` reproduces byte-for-byte. Exchangeability/i.i.d. caveats are honestly stated; these intervals are not certified coverage.
- Recomputed KF moments from all stored rows: rms ratios 0.5665401, 0.9880016, 0.7860237; maxima 1.6636244, 2.8614647, 2.1865236; N₁ residual sds 16.8468328, 11.4079972, 4.4301693. Rebuilt KF source and reran four full-scale rows per geometry: all 12 agree exactly at stored precision.
- LP output reproduces byte-for-byte, including means 0.005311/0.001727/0.000712 at the sharp thresholds and zero means below. This remains floating-point evidence, not an exact LP certificate.
- All five window checks reproduce the quoted real values and truncation bounds; differences from saved text occur only in negligible imaginary roundoff. The six uniform-period frequency checks also agree to roundoff.
- I did not regenerate every expensive full-scale conductor/KF row; the full stored statistics plus independent small exact checks and full-scale spot reruns are the numerical scope of this review.

Primary HB source independently fetched: [math/0405392](https://arxiv.org/pdf/math/0405392), Theorem 14.
No exhaustive new literature search is claimed. The scoped S2 search conclusion is not a theorem of nonexistence.

**Bottom line:** B, C, E, reciprocity, the one-relation ceiling, and Q's bookkeeping withstand independent derivation. The empirical evidence agrees. The DFI misquotation is substantive and invalidates a proposed recorded obstruction, but does not establish a saving for N or resolve ES.
